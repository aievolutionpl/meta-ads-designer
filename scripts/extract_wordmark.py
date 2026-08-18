#!/usr/bin/env python3
"""Extract a white wordmark from a solid-colour logo file.

For the common case: the client's logo is a white wordmark on a solid coloured
square, and the ad needs the wordmark alone, transparent, to sit on a photo.
This never redraws anything — it masks and crops the original pixels (R03/R30-logo).

Usage:
    python scripts/extract_wordmark.py logo.png logo_white.png
    python scripts/extract_wordmark.py logo.png logo_white.png --threshold 150
    python scripts/extract_wordmark.py logo.png logo_dark.png --invert   # dark mark on light bg

Requires: pillow, numpy.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

try:
    import numpy as np
    from PIL import Image
except ImportError:  # pragma: no cover
    sys.exit("extract_wordmark.py needs pillow and numpy:  pip install pillow numpy")


def extract(src: Path, dst: Path, threshold: int = 150, invert: bool = False,
            feather: bool = True) -> tuple[int, int]:
    im = Image.open(src).convert("RGBA")
    a = np.asarray(im).astype(np.int16)

    # The mark is whatever is brightest (or darkest) in every channel.
    if invert:
        level = np.maximum(np.maximum(a[:, :, 0], a[:, :, 1]), a[:, :, 2])
        mask = np.clip((threshold - level) * (255 / max(threshold, 1)), 0, 255)
        ink = 0
    else:
        level = np.minimum(np.minimum(a[:, :, 0], a[:, :, 1]), a[:, :, 2])
        mask = np.clip((level - threshold) * (255 / max(255 - threshold, 1)), 0, 255)
        ink = 255

    if not feather:
        mask = (mask > 0) * 255

    # Existing transparency in the source stays transparent.
    mask = np.minimum(mask, a[:, :, 3])

    out = np.zeros_like(a)
    out[:, :, :3] = ink
    out[:, :, 3] = mask
    img = Image.fromarray(out.astype(np.uint8))

    bbox = img.getbbox()
    if bbox is None:
        sys.exit(f"extract_wordmark.py: nothing above the threshold in {src.name} — "
                 f"try --threshold lower, or --invert")
    img = img.crop(bbox)
    dst.parent.mkdir(parents=True, exist_ok=True)
    img.save(dst)
    return img.width, img.height


def main() -> int:
    ap = argparse.ArgumentParser(description="Extract a wordmark from a solid-colour logo.")
    ap.add_argument("source", type=Path)
    ap.add_argument("output", type=Path)
    ap.add_argument("--threshold", type=int, default=150,
                    help="brightness cutoff, 0-255 (default 150)")
    ap.add_argument("--invert", action="store_true",
                    help="extract a DARK mark from a light background instead")
    ap.add_argument("--hard-edges", action="store_true",
                    help="binary mask instead of a feathered one (aliases more)")
    args = ap.parse_args()

    w, h = extract(args.source, args.output, args.threshold, args.invert,
                   feather=not args.hard_edges)
    print(f"{args.output}  {w}x{h}")
    if w < 180:
        print(f"warning: {w}px wide — below the 180px minimum for a legible wordmark "
              f"(layout-system §6). Use a higher-resolution source.", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
