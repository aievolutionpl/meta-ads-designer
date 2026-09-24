#!/usr/bin/env python3
"""Self-test for scripts/creative_diagnostics.py — synthetic Ads Manager exports."""

from __future__ import annotations

import subprocess
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import creative_diagnostics as cd

CSV = """Ad name,Impressions,Reach,Amount spent (PLN),Link clicks,Results,3-second video plays,ThruPlays
A fatigued,40000,10000,800,400,20,,
B weak hook,30000,20000,600,300,15,3000,1500
C winner,30000,25000,600,900,40,12000,6000
D wrong click,30000,25000,600,600,5,,
E median,30000,25000,600,450,16,9000,4500
F tiny,200,200,5,1,0,,
"""


def run() -> dict:
    with tempfile.TemporaryDirectory() as raw:
        p = Path(raw) / "export.csv"
        p.write_text(CSV, encoding="utf-8")
        ads = [cd.derive(a) for a in cd.load(p) if (a.get("impressions") or 0) >= 1000]
        med = {k: cd.median(ads, k) for k in ("ctr", "cpm", "cpa", "hook", "hold")}
        out = {a["ad"]: cd.diagnose(a, med)[0] for a in ads}
        cli = subprocess.run([sys.executable, str(Path(__file__).parent / "creative_diagnostics.py"), str(p)],
                             capture_output=True, text=True)
        out["_cli"] = cli.returncode
    return out


def main() -> int:
    r = run()
    checks = [
        ("frequency 4.0 is flagged as fatigued", any("fatigued" in f for f in r["A fatigued"])),
        ("low 3s-view rate is flagged as a weak hook", any("weak hook" in f for f in r["B weak hook"])),
        ("strong CTR and CPA is labelled a winner", r["C winner"] == ["winner"]),
        ("clicks without conversions flag high CPA", any("high CPA" in f for f in r["D wrong click"])),
        ("the median ad is healthy", r["E median"] == []),
        ("ads under the impression floor are skipped", "F tiny" not in r),
        ("the CLI exits 0", r["_cli"] == 0),
    ]
    fails = 0
    for name, ok in checks:
        print(f"  {'ok  ' if ok else 'FAIL'} {name}")
        fails += not ok
    print(f"\n{len(checks) - fails}/{len(checks)} cases passed")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
