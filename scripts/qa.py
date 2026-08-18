#!/usr/bin/env python3
"""Deterministic QA gate for generated ad creatives.

Layer 1 of references/qa-gate.md. Measures only what a machine measures better
than an eye: dimensions, safe area, text contrast, collage seams, thumbnail
legibility, focal dispersion, scrim opacity. Everything subjective is layer 2.

Usage:
    python scripts/qa.py out/ad_01.png --format 4:5
    python scripts/qa.py out/ad_01.png --format 4:5 --text-box 86,843,994,1290
    python scripts/qa.py out/*.png --format 4:5 --contact-sheet out/_contact.png
    python scripts/qa.py out/ad_01.png --json          # machine-readable only

Requires: pillow, numpy.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

try:
    import numpy as np
    from PIL import Image
except ImportError:  # pragma: no cover
    sys.exit("qa.py needs pillow and numpy:  pip install pillow numpy")


FORMATS = {
    "4:5": (1080, 1350),
    "9:16": (1080, 1920),
    "1:1": (1080, 1080),
    "16:9": (1920, 1080),
    "2:3": (1000, 1500),
    "4:1": (2048, 512),
}

MARGIN_RATIO = 0.08          # R08 / layout-system §1a
MIN_CONTRAST = 4.5           # layout-system §4a
MIN_THUMBNAIL_RETENTION = 0.40
MAX_FOCAL_REGIONS = 2        # R07
MIN_SCRIM_OPACITY = 0.85     # layout-system §3b


# ---------------------------------------------------------------- primitives

def _luminance(rgb: np.ndarray) -> np.ndarray:
    """WCAG relative luminance for an array of 0-255 RGB values."""
    c = rgb.astype(np.float64) / 255.0
    c = np.where(c <= 0.03928, c / 12.92, ((c + 0.055) / 1.055) ** 2.4)
    return 0.2126 * c[..., 0] + 0.7152 * c[..., 1] + 0.0722 * c[..., 2]


def _contrast_ratio(l1: float, l2: float) -> float:
    hi, lo = max(l1, l2), min(l1, l2)
    return (hi + 0.05) / (lo + 0.05)


def _gray(img: Image.Image) -> np.ndarray:
    return np.asarray(img.convert("L"), dtype=np.float64)


def _edges(g: np.ndarray) -> np.ndarray:
    """Gradient magnitude, no scipy."""
    gy = np.zeros_like(g)
    gx = np.zeros_like(g)
    gy[1:-1, :] = g[2:, :] - g[:-2, :]
    gx[:, 1:-1] = g[:, 2:] - g[:, :-2]
    return np.hypot(gx, gy)


def _block_reduce(a: np.ndarray, rows: int, cols: int) -> np.ndarray:
    """Mean-pool an array into a rows x cols grid."""
    h, w = a.shape
    ys = np.linspace(0, h, rows + 1).astype(int)
    xs = np.linspace(0, w, cols + 1).astype(int)
    return np.array([[a[ys[r]:ys[r + 1], xs[c]:xs[c + 1]].mean()
                      for c in range(cols)] for r in range(rows)])


# ------------------------------------------------------------------- checks

def check_dimensions(img: Image.Image, fmt: str | None) -> tuple[str, bool]:
    got = f"{img.width}x{img.height}"
    if not fmt:
        return got, True
    want = FORMATS.get(fmt)
    if want is None:
        return f"{got} (unknown format {fmt})", True
    ok = (img.width, img.height) == want
    return f"{got} {'ok' if ok else f'expected {want[0]}x{want[1]}'}", ok


def check_safe_area(g: np.ndarray) -> tuple[str, bool]:
    """Flag hard content (strong edges) sitting inside the 8% margin band."""
    h, w = g.shape
    m = int(round(min(h, w) * MARGIN_RATIO))
    e = _edges(g)
    interior = e[m:h - m, m:w - m]
    if interior.size == 0:
        return "canvas too small to measure", True
    thresh = max(np.percentile(interior, 99), 24.0)
    band = e.copy()
    band[m:h - m, m:w - m] = 0
    intrusion = float((band > thresh).sum()) / max(band.size, 1)
    ok = intrusion < 0.004
    return f"{'clear' if ok else 'content in margin'} ({intrusion * 100:.2f}%)", ok


def check_contrast(rgb: np.ndarray, box: tuple[int, int, int, int] | None) -> tuple[float, bool]:
    """Contrast between the light and dark populations inside the text box.

    Without a box, measure the bottom third — where the copy usually lives — and
    report without blocking: a background-only render (Mode B) has no copy yet.
    """
    h, w = rgb.shape[:2]
    if box:
        x0, y0, x1, y1 = box
    else:
        x0, y0, x1, y1 = 0, int(h * 0.66), w, h
    x0, y0 = max(0, x0), max(0, y0)
    x1, y1 = min(w, x1), min(h, y1)
    region = rgb[y0:y1, x0:x1]
    if region.size == 0:
        return 0.0, False
    lum = _luminance(region)
    fg = float(np.percentile(lum, 95))   # glyph pixels
    bg = float(np.percentile(lum, 20))   # backdrop
    ratio = _contrast_ratio(fg, bg)
    return round(ratio, 2), ratio >= MIN_CONTRAST or box is None


def check_collage(img: Image.Image) -> tuple[bool, bool]:
    """Detect grid/split-screen output (R06).

    A seam is a straight discontinuity running the *full* length of the canvas.
    A text bar or a panel edge that spans part of the width is not a seam, which
    is why the test is "share of lines crossing it", not "mean gradient".

    Measured on a downscaled copy: photographic grain averages out, structural
    seams survive at full amplitude.
    """
    small = img.convert("L")
    small = small.resize((240, max(1, round(240 * img.height / img.width))), Image.LANCZOS)
    sm = np.asarray(small, dtype=np.float64)
    h, w = sm.shape

    gy = np.abs(np.diff(sm, axis=0))         # horizontal seam candidates
    gx = np.abs(np.diff(sm, axis=1))         # vertical seam candidates
    strong = max(float(np.percentile(np.concatenate([gy.ravel(), gx.ravel()]), 99.0)), 4.0)

    h_share = (gy > strong).mean(axis=1)     # per row: share of columns crossing
    v_share = (gx > strong).mean(axis=0)     # per column: share of rows crossing

    def count(share: np.ndarray, span: int) -> int:
        inner = share[int(span * 0.12):int(span * 0.88)]
        peaks = inner > 0.92
        if peaks.size == 0:
            return 0
        return int(np.sum(peaks[1:] & ~peaks[:-1]) + (1 if peaks[0] else 0))

    v_seams = count(v_share, w)
    h_seams = count(h_share, h)
    # one horizontal seam is the legitimate photo/panel layout (layout §3a)
    is_collage = v_seams >= 1 or h_seams >= 2
    return is_collage, not is_collage


def check_thumbnail(img: Image.Image, box: tuple[int, int, int, int] | None) -> tuple[object, bool]:
    """How much of the copy block's detail survives at 150px wide (R33).

    Needs --text-box: on a photograph the metric measures grain, not legibility.
    """
    if not box:
        return "n/a (pass --text-box)", True
    region = img.crop(box)
    if region.width < 8 or region.height < 8:
        return 0.0, False
    full = _edges(_gray(region))
    scale = 150 / img.width
    small = region.resize(
        (max(1, int(region.width * scale)), max(1, int(region.height * scale))),
        Image.LANCZOS,
    ).resize(region.size, Image.NEAREST)
    lost = _edges(_gray(small))
    denom = float(full.mean())
    retention = float(lost.mean()) / denom if denom else 0.0
    retention = min(retention, 1.0)
    return round(retention, 2), retention >= MIN_THUMBNAIL_RETENTION


def check_focal(g: np.ndarray) -> tuple[int, bool]:
    """Count competing attention regions on a coarse local-contrast map (R07)."""
    grid = _block_reduce(_edges(g), 9, 7)
    hi = grid.max()
    if hi == 0:
        return 0, False
    strong = grid > hi * 0.62
    # flood-count 4-connected regions
    seen = np.zeros_like(strong, dtype=bool)
    regions = 0
    for r in range(strong.shape[0]):
        for c in range(strong.shape[1]):
            if strong[r, c] and not seen[r, c]:
                regions += 1
                stack = [(r, c)]
                seen[r, c] = True
                while stack:
                    y, x = stack.pop()
                    for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        ny, nx = y + dy, x + dx
                        if (0 <= ny < strong.shape[0] and 0 <= nx < strong.shape[1]
                                and strong[ny, nx] and not seen[ny, nx]):
                            seen[ny, nx] = True
                            stack.append((ny, nx))
    return regions, regions <= MAX_FOCAL_REGIONS


def check_scrim(rgb: np.ndarray, box: tuple[int, int, int, int] | None) -> tuple[object, bool]:
    """Is the text backdrop actually uniform and dark enough (layout §3b)?

    Returns the fraction of backdrop pixels within a tight luminance band —
    a busy photo under the copy scores low, a solid panel or full scrim scores high.
    Needs --text-box; without one there is no copy block to sit under.
    """
    if not box:
        return "n/a (pass --text-box)", True
    h, w = rgb.shape[:2]
    x0, y0, x1, y1 = box
    region = rgb[max(0, y0):min(h, y1), max(0, x0):min(w, x1)]
    if region.size == 0:
        return 0.0, False
    lum = _luminance(region)
    backdrop = lum[lum <= np.percentile(lum, 60)]  # ignore glyph pixels
    if backdrop.size == 0:
        return 0.0, False
    med = float(np.median(backdrop))
    uniform = float((np.abs(backdrop - med) < 0.06).mean())
    return round(uniform, 2), uniform >= MIN_SCRIM_OPACITY


# -------------------------------------------------------------------- runner

def audit(path: Path, fmt: str | None, box: tuple[int, int, int, int] | None) -> dict:
    img = Image.open(path).convert("RGB")
    rgb = np.asarray(img)
    g = _gray(img)

    results: dict[str, object] = {}
    failed: list[str] = []

    def record(name: str, value, ok: bool) -> None:
        results[name] = value
        if not ok:
            failed.append(name)

    record("dimensions", *check_dimensions(img, fmt))
    record("safe_area", *check_safe_area(g))
    record("contrast", *check_contrast(rgb, box))
    collage, ok = check_collage(img)
    record("collage", collage, ok)
    record("thumbnail", *check_thumbnail(img, box))
    record("focal_regions", *check_focal(g))
    record("scrim_uniformity", *check_scrim(rgb, box))

    return {
        "file": path.name,
        "verdict": "PASS" if not failed else "FAIL",
        "checks": results,
        "failed": failed,
    }


def contact_sheet(paths: list[Path], out: Path, cols: int = 3, cell: int = 420) -> None:
    """Build a contact sheet. Previous sheets are excluded by the caller's glob."""
    thumbs = []
    for p in paths:
        im = Image.open(p).convert("RGB")
        im.thumbnail((cell, cell), Image.LANCZOS)
        thumbs.append(im)
    if not thumbs:
        return
    rows = (len(thumbs) + cols - 1) // cols
    pad = 16
    sheet = Image.new("RGB", (cols * cell + pad * (cols + 1),
                              rows * cell + pad * (rows + 1)), (18, 18, 20))
    for i, im in enumerate(thumbs):
        r, c = divmod(i, cols)
        x = pad + c * (cell + pad) + (cell - im.width) // 2
        y = pad + r * (cell + pad) + (cell - im.height) // 2
        sheet.paste(im, (x, y))
    out.parent.mkdir(parents=True, exist_ok=True)
    sheet.save(out)


def main() -> int:
    ap = argparse.ArgumentParser(description="Deterministic QA gate for ad creatives.")
    ap.add_argument("images", nargs="+", type=Path)
    ap.add_argument("--format", dest="fmt", choices=sorted(FORMATS), default=None,
                    help="expected placement format (default: skip the check)")
    ap.add_argument("--text-box", dest="box", default=None,
                    help="x0,y0,x1,y1 of the copy block — sharpens contrast/scrim/thumbnail")
    ap.add_argument("--contact-sheet", dest="sheet", type=Path, default=None)
    ap.add_argument("--json", action="store_true", help="JSON only, no human summary")
    args = ap.parse_args()

    box = None
    if args.box:
        try:
            parts = tuple(int(v) for v in args.box.split(","))
        except ValueError:
            return _die("--text-box must be four integers: x0,y0,x1,y1")
        if len(parts) != 4:
            return _die("--text-box must be four integers: x0,y0,x1,y1")
        box = parts  # type: ignore[assignment]

    paths = [p for p in args.images if p.suffix.lower() in {".png", ".jpg", ".jpeg", ".webp"}]
    if not paths:
        return _die("no images given")

    reports = [audit(p, args.fmt, box) for p in paths]

    if args.sheet:
        contact_sheet([p for p in paths if p.resolve() != args.sheet.resolve()], args.sheet)

    print(json.dumps(reports if len(reports) > 1 else reports[0], indent=2))

    if not args.json:
        print("\n--- summary ---", file=sys.stderr)
        for r in reports:
            note = ", ".join(r["failed"]) or "—"
            print(f"{r['file']:<28} {r['verdict']:<5} {note}", file=sys.stderr)

    return 0 if all(r["verdict"] == "PASS" for r in reports) else 1


def _die(msg: str) -> int:
    print(f"qa.py: {msg}", file=sys.stderr)
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
