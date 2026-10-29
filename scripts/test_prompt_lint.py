#!/usr/bin/env python3
"""Self-test for scripts/prompt_lint.py — known-good and known-bad prompts."""

from __future__ import annotations

import subprocess
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import prompt_lint as pl

GOOD = (
    'Vertical 4:5 documentary photo of a baker folding dough in window light. '
    'Upper third, heavy black sans: "Croissant w 12 minut". Below it, smaller: "Zamów do 9:00". '
    "No other text. No play button, no neon glow."
)


def rules(prompt: str, level: str | None = None) -> set[str]:
    return {f.rule for f in pl.lint(prompt) if level is None or f.level == level}


def main() -> int:
    with tempfile.TemporaryDirectory() as raw:
        p = Path(raw) / "set.txt"
        p.write_text(GOOD + "\n---\n" + GOOD.replace("No other text. ", ""), encoding="utf-8")
        cli = subprocess.run([sys.executable, str(Path(__file__).parent / "prompt_lint.py"), str(p)],
                             capture_output=True, text=True)
        good_only = Path(raw) / "good.txt"
        good_only.write_text(GOOD, encoding="utf-8")
        cli_good = subprocess.run([sys.executable, str(Path(__file__).parent / "prompt_lint.py"), str(good_only)],
                                  capture_output=True, text=True)

    checks = [
        ("a complete prompt has no findings", pl.lint(GOOD) == []),
        ("negated slop and fake UI are allowed", not rules(GOOD) & {"R05", "R48-fake-ui"}),
        ("a [BRAND] placeholder fails R25", "R25" in rules(GOOD.replace("baker", "[BRAND] baker"), "FAIL")),
        ("a lone 'X' as copy fails R25", "R25" in rules(GOOD.replace("Croissant w 12 minut", "X"), "FAIL")),
        ("quoted copy without 'no other text' fails R50",
         "R50" in rules(GOOD.replace("No other text. ", ""), "FAIL")),
        ("Polish unproven superlative fails R52",
         "R52" in rules(GOOD.replace("Croissant w 12 minut", "Najlepszy croissant"), "FAIL")),
        ("banned English word fails R52",
         "R52" in rules(GOOD.replace("Croissant w 12 minut", "Unlock flaky mornings"), "FAIL")),
        ("an un-negated play button fails R48-fake-ui",
         "R48-fake-ui" in rules(GOOD + " A white play button sits in the centre.", "FAIL")),
        ("a seven-word headline warns", "R52" in rules(GOOD.replace("Croissant w 12 minut", "One two three four five six seven"), "WARN")),
        ("the headline is found after the word 'headline', not the brand name",
         pl.headline('Ad for "ACME". Headline: "One two three four five six seven". No other text.',
                     pl.quoted('Ad for "ACME". Headline: "One two three four five six seven".')) == "One two three four five six seven"),
        ("a one-word brand name is not taken for the headline",
         pl.headline('Ad for "ACME" with "Two words".', ["ACME", "Two words"]) == "Two words"),
        ("a question as copy warns", "R52" in rules(GOOD.replace("Croissant w 12 minut", "Głodny?"), "WARN")),
        ("dithering warns as a decayed cue", "R53" in rules(GOOD + " Dithered texture over the photo.", "WARN")),
        ("density adjectives warn", "R40" in rules(GOOD + " Ultra-detailed, 8k.", "WARN")),
        ("a testimonial warns under R55", "R55" in rules(GOOD + " Styled as a real customer testimonial.", "WARN")),
        ("a missing ratio warns", "R48" in rules(GOOD.replace("Vertical 4:5 ", ""), "WARN")),
        ("typographic quotes are read as copy", pl.quoted("Headline: „Noc brzmi” and “Bilety”") == ["Noc brzmi", "Bilety"]),
        ("prompt files split on ---", len(pl.split_prompts(GOOD + "\n---\n" + GOOD)) == 2),
        ("the CLI exits 1 when one prompt fails", cli.returncode == 1),
        ("the CLI exits 0 on a clean file", cli_good.returncode == 0),
    ]
    fails = 0
    for name, ok in checks:
        print(f"  {'ok  ' if ok else 'FAIL'} {name}")
        fails += not ok
    print(f"\n{len(checks) - fails}/{len(checks)} cases passed")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
