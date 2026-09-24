#!/usr/bin/env python3
"""Generate ad images with a fal.ai image model (R50: ads are generated, never coded).

Reads a prompt file (one prompt; or several separated by a line with `---`),
submits each to fal.ai's queue API, waits, and saves the images next to a JSON
log of prompt, model, request id and seed so every README image is reproducible.

Usage:
    export FAL_KEY=...                       # never commit the key
    python scripts/generate_fal.py prompts.txt --model fal-ai/<model-id> --out assets/generated
    python scripts/generate_fal.py prompts.txt --model fal-ai/<model-id> --aspect 4:5 --n 2
    python scripts/generate_fal.py prompts.txt --model fal-ai/<edit-model-id> --image-url https://... (reference)

Model ids and accepted parameters differ per model; check the model page on
fal.ai. Extra parameters can be passed as --param key=value (repeatable).
Standard library only. Needs network access to queue.fal.run and fal.media.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import time
import urllib.request
from pathlib import Path

QUEUE = "https://queue.fal.run"
SIZES = {"4:5": "portrait_4_3", "9:16": "portrait_16_9", "1:1": "square_hd", "16:9": "landscape_16_9"}


def call(url: str, key: str, payload: dict | None = None) -> dict:
    data = json.dumps(payload).encode() if payload is not None else None
    req = urllib.request.Request(url, data=data, method="POST" if data else "GET",
                                 headers={"Authorization": f"Key {key}", "Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=120) as r:
        return json.loads(r.read())


def generate(model: str, key: str, args: dict, timeout: int = 600) -> dict:
    job = call(f"{QUEUE}/{model}", key, args)
    status_url, response_url = job["status_url"], job["response_url"]
    start = time.time()
    while time.time() - start < timeout:
        st = call(status_url, key)
        if st.get("status") == "COMPLETED":
            res = call(response_url, key)
            res["_request_id"] = job.get("request_id")
            return res
        if st.get("status") in {"FAILED", "ERROR"}:
            raise RuntimeError(f"fal job failed: {st}")
        time.sleep(3)
    raise TimeoutError("fal job did not finish in time")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("prompts", type=Path)
    ap.add_argument("--model", required=True, help="fal model id, e.g. fal-ai/<model>")
    ap.add_argument("--out", type=Path, default=Path("out"))
    ap.add_argument("--aspect", default="4:5", choices=sorted(SIZES))
    ap.add_argument("--n", type=int, default=1, help="images per prompt")
    ap.add_argument("--image-url", action="append", default=[], help="reference image URL (edit models)")
    ap.add_argument("--param", action="append", default=[], help="extra model parameter key=value")
    a = ap.parse_args()

    key = os.environ.get("FAL_KEY")
    if not key:
        print("generate_fal: set FAL_KEY in the environment", file=sys.stderr)
        return 2
    prompts = [p.strip() for p in a.prompts.read_text(encoding="utf-8").split("\n---\n") if p.strip()]
    a.out.mkdir(parents=True, exist_ok=True)
    log = []
    for i, prompt in enumerate(prompts, 1):
        args = {"prompt": prompt, "num_images": a.n, "image_size": SIZES[a.aspect], "aspect_ratio": a.aspect}
        if a.image_url:
            args["image_urls"] = a.image_url
        for kv in a.param:
            k, _, v = kv.partition("=")
            args[k] = json.loads(v) if v[:1] in "[{0123456789tfn" and v not in {"", "none"} else v
        print(f"[{i}/{len(prompts)}] generating…", file=sys.stderr)
        res = generate(a.model, key, args)
        for j, img in enumerate(res.get("images", []), 1):
            path = a.out / f"{a.prompts.stem}-{i:02d}-{j}.png"
            urllib.request.urlretrieve(img["url"], path)
            log.append({"file": path.name, "model": a.model, "prompt": prompt,
                        "seed": res.get("seed"), "request_id": res.get("_request_id")})
            print(path)
    (a.out / f"{a.prompts.stem}.log.json").write_text(json.dumps(log, indent=2, ensure_ascii=False), encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main())
