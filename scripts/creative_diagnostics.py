#!/usr/bin/env python3
"""Creative diagnostics from a Meta Ads Manager CSV export.

Turns per-ad numbers into creative decisions: which ads are fatigued, which
lose at the hook, which lose after the click, and what the next brief should
change (R37, R47, references/creative-diagnostics.md). It reads numbers; it
never judges an image. Thresholds are third-party 2026 benchmarks, compared
against the account's own median, not universal truths.

Usage:
    python scripts/creative_diagnostics.py export.csv
    python scripts/creative_diagnostics.py export.csv --json
    python scripts/creative_diagnostics.py export.csv --min-impressions 3000

Column names are matched loosely (English Ads Manager export headers). Only
`Ad name` and `Impressions` are required; every other check runs when its
column exists and reports "n/a" otherwise. Standard library only.
"""

from __future__ import annotations

import argparse
import csv
import json
import statistics
import sys
from pathlib import Path

ALIASES = {
    "ad": ["ad name", "ad"],
    "impressions": ["impressions"],
    "reach": ["reach"],
    "frequency": ["frequency"],
    "spend": ["amount spent", "amount spent (usd)", "amount spent (pln)", "amount spent (eur)", "spend"],
    "clicks": ["link clicks", "clicks (all)", "clicks"],
    "ctr": ["ctr (link click-through rate)", "ctr (all)", "ctr"],
    "cpm": ["cpm (cost per 1,000 impressions)", "cpm"],
    "results": ["results", "purchases", "leads", "conversions"],
    "cpa": ["cost per result", "cost per purchase", "cost per lead", "cpa"],
    "views3s": ["3-second video plays", "video plays at 3 seconds"],
    "thruplays": ["thruplays"],
}

FREQ_WATCH, FREQ_REPLACE = 2.5, 3.5      # cold prospecting (creative-performance-loop §5)
CTR_LOW = 0.70                           # below 70% of the account median
CPA_HIGH = 1.40                          # above 140% of the account median
CPM_HIGH = 1.30                          # above 130% of the account median
HOOK_LOW = 0.70                          # hook rate below 70% of the median
HOLD_LOW = 0.70                          # thruplay/3s hold below 70% of the median


def _num(raw: str | None) -> float | None:
    if raw is None:
        return None
    s = str(raw).strip().replace("%", "").replace(" ", "").replace(" ", "")
    if not s or s in {"-", "—"}:
        return None
    if s.count(",") == 1 and "." not in s:
        s = s.replace(",", ".")
    s = s.replace(",", "")
    try:
        return float(s)
    except ValueError:
        return None


def load(path: Path) -> list[dict]:
    text = path.read_text(encoding="utf-8-sig")
    dialect = csv.Sniffer().sniff(text[:4096], delimiters=",;\t")
    rows = list(csv.DictReader(text.splitlines(), dialect=dialect))
    if not rows:
        return []
    headers = {h.strip().lower(): h for h in rows[0].keys() if h}
    cols = {}
    for key, names in ALIASES.items():
        for n in names:
            if n in headers:
                cols[key] = headers[n]
                break
    if "ad" not in cols or "impressions" not in cols:
        raise SystemExit("creative_diagnostics: need at least 'Ad name' and 'Impressions' columns")
    out = []
    for r in rows:
        ad = {"ad": (r.get(cols["ad"]) or "").strip()}
        for key, col in cols.items():
            if key != "ad":
                ad[key] = _num(r.get(col))
        if ad["ad"]:
            out.append(ad)
    return out


def derive(ad: dict) -> dict:
    imp = ad.get("impressions") or 0
    if ad.get("ctr") is None and ad.get("clicks") is not None and imp:
        ad["ctr"] = ad["clicks"] / imp * 100
    if ad.get("cpm") is None and ad.get("spend") is not None and imp:
        ad["cpm"] = ad["spend"] / imp * 1000
    if ad.get("cpa") is None and ad.get("spend") is not None and ad.get("results"):
        ad["cpa"] = ad["spend"] / ad["results"]
    if ad.get("frequency") is None and ad.get("reach"):
        ad["frequency"] = imp / ad["reach"]
    ad["hook"] = ad["views3s"] / imp * 100 if ad.get("views3s") is not None and imp else None
    ad["hold"] = (ad["thruplays"] / ad["views3s"] * 100
                  if ad.get("thruplays") is not None and ad.get("views3s") else None)
    return ad


def median(ads: list[dict], key: str) -> float | None:
    vals = [a[key] for a in ads if a.get(key) is not None and a[key] > 0]
    return statistics.median(vals) if vals else None


def diagnose(ad: dict, med: dict) -> tuple[list[str], list[str]]:
    flags, actions = [], []
    f = ad.get("frequency")
    if f is not None and f >= FREQ_REPLACE:
        flags.append(f"fatigued (frequency {f:.1f})")
        actions.append("replace with a new concept: different persona, hook or format, not a recolour (R47)")
    elif f is not None and f >= FREQ_WATCH:
        flags.append(f"fatigue watch (frequency {f:.1f})")
        actions.append("brief the replacement now; keep 3-5 approved variants ready")

    def low(key, ratio):
        return ad.get(key) is not None and med.get(key) and ad[key] < med[key] * ratio

    def high(key, ratio):
        return ad.get(key) is not None and med.get(key) and ad[key] > med[key] * ratio

    if low("hook", HOOK_LOW):
        flags.append(f"weak hook ({ad['hook']:.1f}% vs median {med['hook']:.1f}%)")
        actions.append("rebuild the first frame: bigger promise, stronger contrast, one focal point (R36)")
    if low("hold", HOLD_LOW):
        flags.append(f"weak hold ({ad['hold']:.1f}% vs median {med['hold']:.1f}%)")
        actions.append("hook works, story doesn't: show the product/proof earlier, cut the middle")
    if low("ctr", CTR_LOW):
        flags.append(f"low CTR ({ad['ctr']:.2f}% vs median {med['ctr']:.2f}%)")
        actions.append("message isn't landing: test a new hook or a proof format (stat drop, reviews)")
    if high("cpm", CPM_HIGH):
        flags.append(f"high CPM ({ad['cpm']:.2f} vs median {med['cpm']:.2f})")
        actions.append("low relevance or a near-duplicate of other ads: make it visibly distinct")
    ctr_ok = ad.get("ctr") is not None and med.get("ctr") and ad["ctr"] >= med["ctr"]
    if high("cpa", CPA_HIGH):
        flags.append(f"high CPA ({ad['cpa']:.2f} vs median {med['cpa']:.2f})")
        actions.append("clicks but no conversions: check ad-to-landing continuity and offer clarity (R37 §4)"
                       if ctr_ok else "fix the promise before the page: the creative attracts the wrong click")
    if not flags:
        is_winner = (ad.get("cpa") is not None and med.get("cpa") and ad["cpa"] <= med["cpa"] * 0.8) or \
                    (ad.get("ctr") is not None and med.get("ctr") and ad["ctr"] >= med["ctr"] * 1.3)
        if is_winner:
            flags.append("winner")
            actions.append("iterate for new personas and settings; keep the angle, change the context (R47)")
    return flags, actions


def main() -> int:
    ap = argparse.ArgumentParser(description="Creative diagnostics from a Meta Ads Manager CSV export.")
    ap.add_argument("csv", type=Path)
    ap.add_argument("--min-impressions", type=int, default=1000,
                    help="skip ads below this volume: small samples are noise (default 1000)")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    ads = [derive(a) for a in load(args.csv)]
    ads = [a for a in ads if (a.get("impressions") or 0) >= args.min_impressions]
    if not ads:
        print("no ads above the impression floor", file=sys.stderr)
        return 1
    med = {k: median(ads, k) for k in ("ctr", "cpm", "cpa", "hook", "hold")}

    report = []
    for a in ads:
        flags, actions = diagnose(a, med)
        report.append({"ad": a["ad"], "impressions": int(a["impressions"]),
                       "flags": flags, "next_brief": actions})
    report.sort(key=lambda r: (r["flags"] == ["winner"], -len(r["flags"])))

    if args.json:
        print(json.dumps({"medians": med, "ads": report}, indent=2))
        return 0
    def fmt(v, d=2, unit=""):
        return "n/a" if v is None else f"{v:.{d}f}{unit}"
    print(f"{len(ads)} ads · medians: CTR {fmt(med['ctr'], 2, '%')} · CPM {fmt(med['cpm'])} · "
          f"CPA {fmt(med['cpa'])} · hook {fmt(med['hook'], 1, '%')} · hold {fmt(med['hold'], 1, '%')}\n")
    for r in report:
        print(f"■ {r['ad']}  ({r['impressions']:,} impr.)")
        for f, act in zip(r["flags"], r["next_brief"]):
            print(f"   {f}\n     → {act}")
        if not r["flags"]:
            print("   healthy · no action")
        print()
    return 0


if __name__ == "__main__":
    sys.exit(main())
