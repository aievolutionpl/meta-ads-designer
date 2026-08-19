#!/usr/bin/env python3
"""Self-test for scripts/qa.py — builds synthetic creatives and asserts verdicts.

The QA gate is the one part of this repo that makes automated ship/no-ship calls,
so it needs evidence that it calls them correctly. Every case here is a layout the
rules describe, or a failure mode the rules exist to catch.

    python scripts/test_qa.py        # exits non-zero on the first failed case

Requires: pillow, numpy (same as qa.py). No test framework.
"""

from __future__ import annotations

import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

try:
    from PIL import Image, ImageDraw, ImageFont
except ImportError:  # pragma: no cover
    sys.exit("test_qa.py needs pillow and numpy:  pip install pillow numpy")

import qa

W, H = 1080, 1350
PANEL_TOP = 843                       # layout-system §3a, 62.5%
TEXT_BOX = (86, 900, 994, 1230)
NAVY = (10, 31, 51)

FONT_CANDIDATES = [
    "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
    "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf",
    "/System/Library/Fonts/Supplemental/Arial Bold.ttf",
    "C:/Windows/Fonts/arialbd.ttf",
]


def _font(size: int):
    for path in FONT_CANDIDATES:
        if Path(path).exists():
            return ImageFont.truetype(path, size)
    sys.exit("test_qa.py: no scalable font found — install DejaVu or Liberation")


def photo_panel_ad() -> Image.Image:
    """The canonical layout: photo top 62.5%, solid panel below, copy in the panel."""
    im = Image.new("RGB", (W, H), (188, 150, 108))
    dr = ImageDraw.Draw(im)
    for y in range(0, PANEL_TOP, 3):                     # some photographic variation
        dr.line([(0, y), (W, y)], fill=(188 - y // 20, 150 - y // 30, 108 - y // 40))
    dr.rectangle([0, PANEL_TOP, W, H], fill=NAVY)
    dr.text((86, 920), "SOUVLAKI OFF", font=_font(88), fill=(255, 255, 255))
    dr.text((86, 1020), "THE GRILL", font=_font(88), fill=(255, 255, 255))
    dr.text((86, 1150), "Havre des Pas \u00b7 open till 11", font=_font(34),
            fill=(228, 228, 228))
    return im


def low_contrast_ad() -> Image.Image:
    """Same layout, mid-grey copy on a mid-grey panel — below 4.5:1."""
    im = photo_panel_ad()
    dr = ImageDraw.Draw(im)
    dr.rectangle([0, PANEL_TOP, W, H], fill=(120, 124, 130))
    dr.text((86, 920), "SOUVLAKI OFF", font=_font(88), fill=(150, 154, 160))
    dr.text((86, 1020), "THE GRILL", font=_font(88), fill=(150, 154, 160))
    return im


def collage_ad() -> Image.Image:
    """A 2x2 grid — what a model returns when asked for "a set of ads"."""
    im = Image.new("RGB", (W, H), (245, 245, 245))
    dr = ImageDraw.Draw(im)
    dr.rectangle([0, 0, W // 2, H // 2], fill=(30, 30, 30))
    dr.rectangle([W // 2, H // 2, W, H], fill=(30, 30, 30))
    return im


CASES = []


def case(name):
    def wrap(fn):
        CASES.append((name, fn))
        return fn
    return wrap


@case("canonical photo+panel ad passes")
def _(tmp: Path):
    photo_panel_ad().save(tmp / "good.png")
    r = qa.audit(tmp / "good.png", "4:5", TEXT_BOX)
    assert r["verdict"] == "PASS", r
    assert r["checks"]["contrast"] >= 4.5, r["checks"]["contrast"]


@case("sparse white-on-navy type measures as high contrast, not 1.0")
def _(tmp: Path):
    photo_panel_ad().save(tmp / "good.png")
    r = qa.audit(tmp / "good.png", "4:5", TEXT_BOX)
    assert r["checks"]["contrast"] > 10, r["checks"]["contrast"]


@case("grey-on-grey copy fails the contrast check")
def _(tmp: Path):
    low_contrast_ad().save(tmp / "low.png")
    r = qa.audit(tmp / "low.png", "4:5", TEXT_BOX)
    assert "contrast" in r["failed"], r


@case("a text box crossing the 8% margin fails safe_area")
def _(tmp: Path):
    photo_panel_ad().save(tmp / "good.png")
    r = qa.audit(tmp / "good.png", "4:5", (20, 900, 1060, 1230))
    assert "safe_area" in r["failed"], r


@case("a text box inside the 9:16 story chrome fails safe_area")
def _(tmp: Path):
    photo_panel_ad().resize((1080, 1920)).save(tmp / "story.png")
    r = qa.audit(tmp / "story.png", "9:16", (86, 1650, 994, 1800))
    assert "safe_area" in r["failed"], r


@case("the canonical 4:5 panel layout is not failed by advisory chrome")
def _(tmp: Path):
    photo_panel_ad().save(tmp / "good.png")
    r = qa.audit(tmp / "good.png", "4:5", (86, 900, 994, 1264))
    assert "safe_area" not in r["failed"], r


@case("a logo box crossing the margin fails safe_area")
def _(tmp: Path):
    photo_panel_ad().save(tmp / "good.png")
    r = qa.audit(tmp / "good.png", "4:5", TEXT_BOX, logo_box=(900, 1150, 1070, 1210))
    assert "safe_area" in r["failed"], r


@case("no --text-box reports partial coverage instead of a clean PASS")
def _(tmp: Path):
    photo_panel_ad().save(tmp / "good.png")
    r = qa.audit(tmp / "good.png", "4:5", None)
    assert "note" in r, r
    assert r["checks"]["safe_area"].startswith("n/a"), r


@case("a 2x2 grid is caught as a collage")
def _(tmp: Path):
    collage_ad().save(tmp / "collage.png")
    r = qa.audit(tmp / "collage.png", "4:5", None)
    assert r["checks"]["collage"] is True, r


@case("the photo/panel seam is not mistaken for a collage")
def _(tmp: Path):
    photo_panel_ad().save(tmp / "good.png")
    r = qa.audit(tmp / "good.png", "4:5", TEXT_BOX)
    assert r["checks"]["collage"] is False, r


@case("wrong dimensions fail the format check")
def _(tmp: Path):
    photo_panel_ad().resize((1080, 1080)).save(tmp / "square.png")
    r = qa.audit(tmp / "square.png", "4:5", None)
    assert "dimensions" in r["failed"], r


@case("88px headline survives the thumbnail check")
def _(tmp: Path):
    photo_panel_ad().save(tmp / "good.png")
    r = qa.audit(tmp / "good.png", "4:5", TEXT_BOX)
    assert r["checks"]["thumbnail"] >= qa.MIN_THUMBNAIL_RETENTION, r


@case("contact sheet is built and excludes itself")
def _(tmp: Path):
    for i in range(3):
        photo_panel_ad().save(tmp / f"ad_{i}.png")
    sheet = tmp / "_contact.png"
    qa.contact_sheet(sorted(tmp.glob("ad_*.png")), sheet)
    assert sheet.exists() and Image.open(sheet).width > 0


def main() -> int:
    failures = 0
    with tempfile.TemporaryDirectory() as raw:
        tmp = Path(raw)
        for name, fn in CASES:
            try:
                fn(tmp)
                print(f"  ok   {name}")
            except AssertionError as exc:
                failures += 1
                print(f"  FAIL {name}\n       {exc}", file=sys.stderr)
    print(f"\n{len(CASES) - failures}/{len(CASES)} cases passed")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
