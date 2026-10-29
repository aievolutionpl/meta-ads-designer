#!/usr/bin/env python3
"""Lint image-generation prompts before spending credits on them.

The image gate (`qa.py`) can only judge a render after it exists. Most failed
renders were already visible in the prompt: a placeholder that survived, copy
with no "no other text", a mood line instead of a benefit, a fake play button,
a trend cue everybody already uses. This catches those in the text.

Checks, each tagged with the rule it enforces:
  FAIL  R25        unresolved placeholders ([BRAND], <HEADLINE>, {offer}, 'X', TODO)
  FAIL  R18 / R50  quoted copy without "no other text"
  FAIL  R52        copy slop inside quoted strings (unproven superlatives, banned words)
  FAIL  R48-fake-ui  play buttons, close icons, notification badges (unless negated)
  WARN  R52        headline over 6 words, any string over 12 words, a question, an em dash
  WARN  R40        density adjectives (ultra-detailed, 8k, intricate)
  WARN  R53        decayed trend cues (dithering, ASCII, scanlines, halftone, grain overlay)
  WARN  R05        visual slop vocabulary (purple gradient, neon glow, glassmorphism)
  WARN  R55        evidence words (real customer, testimonial, before/after, making-of)
  WARN  R48        no aspect ratio or output size stated

Negated mentions ("no neon glow", "without a play button") are allowed.
Styles 13-16 use glow and floating 3D on purpose (R42); a WARN there is expected.

Usage:
    python scripts/prompt_lint.py prompts.txt [more.txt ...]   # prompts split by a '---' line
    echo "..." | python scripts/prompt_lint.py -
    python scripts/prompt_lint.py prompts.txt --strict          # WARN also fails
    python scripts/prompt_lint.py prompts.txt --json

Exits 1 when any prompt has a FAIL (or a WARN with --strict). Standard library only.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import asdict, dataclass
from pathlib import Path

QUOTED = re.compile(r'"([^"\n]+)"|“([^”\n]+)”|„([^”“"\n]+)[”“"]|«([^»\n]+)»')
PLACEHOLDER = re.compile(
    r"\[[A-Za-z_ .\-/]+\]|<[A-Z_]{2,}>|\{[A-Za-z_ ]+\}|\bTODO\b|\bTBD\b|\bXXX\b|lorem ipsum", re.I
)
SINGLE_LETTER = re.compile(r"^[XYZ]$")
NO_OTHER_TEXT = re.compile(
    r"no (other|additional|further|extra) (text|words|lettering|copy)|nothing else|"
    r"no text other than|only (this|these) (text|words)|żadnego innego tekstu|bez innego tekstu",
    re.I,
)
RATIO = re.compile(r"\b(4:5|9:16|1:1|16:9|3:4|2:3|1\.91:1)\b|\b\d{3,4}\s*[×x]\s*\d{3,4}\b|\b(square|portrait|landscape)\b", re.I)
HEADLINE_CUE = re.compile(r"\b(headline|nagłówek|nagłówkiem)\b", re.I)
NEGATION = re.compile(r"\b(no|not|without|never|avoid|nor|zero|bez|żadn\w*)\b", re.I)

COPY_SLOP = [
    r"najlepsz\w*", r"wyjątkow\w*", r"premium", r"jakoś\w*", r"odkryj\w*", r"poczuj\w*", r"przenieś się",
    r"delve\w*", r"seamless\w*", r"empower\w*", r"elevate\w*", r"robust", r"tapestry", r"revolutionary",
    r"game[- ]changer", r"unlock\w*", r"unleash\w*", r"the (ultimate|perfect|best)\b", r"your perfect",
    r"world[- ]class", r"next[- ]level", r"🚀",
]
FAKE_UI = [
    r"play button", r"play icon", r"close (icon|button|x)", r"notification (badge|dot|bubble)",
    r"unread badge", r"red badge", r"system alert", r"tappable", r"progress bar", r"mute icon",
]
DENSITY = [r"ultra[- ]detailed", r"hyper[- ]detailed", r"intricate", r"\b8k\b", r"\b4k\b", r"masterpiece",
           r"trending on artstation", r"hyper[- ]?realistic", r"ultra[- ]realistic"]
DECAYED = [r"dither\w*", r"\bascii\b", r"pixel grid", r"scan ?lines?", r"grain overlay", r"film grain overlay",
           r"halftone (background|pattern|overlay|texture)"]
VISUAL_SLOP = [r"purple gradient", r"blue[- ]to[- ]purple", r"glassmorphism", r"frosted glass", r"neon glow",
               r"glowing (orbs?|accents?)", r"floating particles", r"magical sparkles?", r"gradient text"]
EVIDENCE = [r"real customer", r"actual customer", r"testimonial", r"before[ /-]+(and[ -]+)?after",
            r"behind[- ]the[- ]scenes", r"making[- ]of", r"our (team|staff|employees)", r"user[- ]generated"]


@dataclass
class Finding:
    level: str
    rule: str
    message: str


def split_prompts(text: str) -> list[str]:
    return [p.strip() for p in re.split(r"\n-{3,}\n", text) if p.strip()]


def quoted(prompt: str) -> list[str]:
    return [next(g for g in m.groups() if g is not None).strip() for m in QUOTED.finditer(prompt)]


def headline(prompt: str, strings: list[str]) -> str | None:
    """The first string quoted after the word "headline"; else the first multi-word string.

    A one-word first string is usually the brand name, not the headline.
    """
    cue = HEADLINE_CUE.search(prompt)
    if cue:
        after = quoted(prompt[cue.end():])
        if after:
            return after[0]
    return next((s for s in strings if len(s.split()) > 1), None)


def negated(prompt: str, start: int) -> bool:
    """True when the mention sits in a clause that starts with a negation."""
    clause_start = max(prompt.rfind(c, 0, start) for c in ".;:\n,(") + 1
    return bool(NEGATION.search(prompt[clause_start:start]))


def mentions(prompt: str, patterns: list[str], allow_negation: bool = True) -> list[str]:
    hits = []
    for pat in patterns:
        for m in re.finditer(pat, prompt, re.I):
            if allow_negation and negated(prompt, m.start()):
                continue
            hits.append(m.group(0))
    return sorted(set(h.lower() for h in hits))


def lint(prompt: str) -> list[Finding]:
    out: list[Finding] = []
    strings = quoted(prompt)

    holes = sorted(set(PLACEHOLDER.findall(prompt))) + [f'"{s}"' for s in strings if SINGLE_LETTER.match(s)]
    if holes:
        out.append(Finding("FAIL", "R25", "unresolved placeholder: " + ", ".join(holes)))

    if strings and not NO_OTHER_TEXT.search(prompt):
        out.append(Finding("FAIL", "R50", 'quoted copy but no "no other text": the model will invent extra words (R18)'))
    if not strings:
        out.append(Finding("WARN", "R50", "no quoted copy: fine for a text-free image, otherwise quote every string exactly"))

    copy = "\n".join(strings)
    slop = mentions(copy, COPY_SLOP, allow_negation=False)
    if slop:
        out.append(Finding("FAIL", "R52", "copy slop in quoted text: " + ", ".join(slop)))
    head = headline(prompt, strings)
    if head and len(head.split()) > 6:
        out.append(Finding("WARN", "R52", f'headline has {len(head.split())} words, keep it to 6: "{head}"'))
    for s in strings:
        if len(s.split()) > 12:
            out.append(Finding("WARN", "R52", f'{len(s.split())} words on the image, move the rest to Meta text fields: "{s[:60]}…"'))
        if s.rstrip().endswith("?"):
            out.append(Finding("WARN", "R52", f'question as copy, state the benefit instead: "{s}"'))
        if "—" in s:
            out.append(Finding("WARN", "R52", f'em dash in copy, use a comma, colon or "·": "{s}"'))

    for level, rule, pats, label in (
        ("FAIL", "R48-fake-ui", FAKE_UI, "fake functional UI"),
        ("WARN", "R40", DENSITY, "density adjectives request micro-repetition, describe the material"),
        ("WARN", "R53", DECAYED, "decayed trend cue, check the Ad Library before borrowing it"),
        ("WARN", "R05", VISUAL_SLOP, "visual slop vocabulary (expected only in styles 13–16, R42)"),
        ("WARN", "R55", EVIDENCE, "evidence words, build from real references or make the staging obvious"),
    ):
        hits = mentions(prompt, pats)
        if hits:
            out.append(Finding(level, rule, f"{label}: " + ", ".join(hits)))

    if not RATIO.search(prompt):
        out.append(Finding("WARN", "R48", "no aspect ratio or size stated (feed default 4:5, Reels/Stories 9:16)"))
    return out


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("files", nargs="+", help="prompt files, or - for stdin")
    ap.add_argument("--strict", action="store_true", help="treat WARN as failure")
    ap.add_argument("--json", action="store_true", help="print findings as JSON")
    a = ap.parse_args()

    report = []
    for name in a.files:
        text = sys.stdin.read() if name == "-" else Path(name).read_text(encoding="utf-8")
        for i, prompt in enumerate(split_prompts(text), 1):
            report.append({"file": name, "prompt": i, "preview": prompt[:70],
                           "findings": [asdict(f) for f in lint(prompt)]})

    bad = {"FAIL", "WARN"} if a.strict else {"FAIL"}
    failed = sum(any(f["level"] in bad for f in r["findings"]) for r in report)
    if a.json:
        print(json.dumps(report, indent=2, ensure_ascii=False))
    else:
        for r in report:
            levels = {f["level"] for f in r["findings"]}
            verdict = "FAIL" if "FAIL" in levels else "WARN" if "WARN" in levels else "PASS"
            print(f"{r['file']} #{r['prompt']}  {verdict}  {r['preview']}…")
            for f in r["findings"]:
                print(f"    {f['level']:4}  {f['rule']:<12} {f['message']}")
        print(f"\n{len(report) - failed}/{len(report)} prompts pass" + (" (strict)" if a.strict else ""))
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
