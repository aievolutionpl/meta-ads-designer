#!/usr/bin/env python3
"""Structural check for the skill's own docs.

Every failure this catches has already happened in this repo at least once:
a pointer to `design-rules.md` §12 when that file stops at §9, a file table
listing a reference that was renamed, a version badge that drifted from the
frontmatter. Markdown has no compiler, so this is it.

Checks:
  1. relative links (.md/.py/.png/.html) resolve from the linking file
  2. `file.md` §N pointers resolve to a real `## N ·` heading in that file
  3. cited rule IDs (R01-R34) exist in visual-advertising-engine.md
  4. SKILL.md frontmatter is a valid Agent Skill header
  5. the version in SKILL.md, the README badges and CHANGELOG agree

Usage: python scripts/check_docs.py [--root .]     exits non-zero on any failure.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

LINK = re.compile(r"\[[^\]]*\]\(([A-Za-z0-9_./-]+\.(?:md|py|png|html))\)")
SECTION = re.compile(r"`([A-Za-z0-9_./-]+\.md)`\s*§([0-9]+(?:\.[0-9]+)?)")
HEADING = re.compile(r"^##\s+([0-9]+(?:\.[0-9]+)?)\s*·", re.M)
RULE_CITE = re.compile(r"`(R[0-9]{2})`")
RULE_DEF = re.compile(r"^##\s+(R[0-9]{2})\s*·", re.M)
NAME = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")

# Agent Skills frontmatter: anything outside this set belongs under `metadata`.
ALLOWED_KEYS = {"name", "description", "license", "allowed-tools", "metadata"}
MAX_DESCRIPTION = 1024


def md_files(root: Path) -> list[Path]:
    return sorted(p for p in root.rglob("*.md") if ".git" not in p.parts)


def check_links(root: Path, fails: list[str]) -> None:
    for f in md_files(root):
        for target in LINK.findall(f.read_text(encoding="utf-8")):
            if not (f.parent / target).exists():
                fails.append(f"{f.relative_to(root)}: dead link -> {target}")


def check_sections(root: Path, fails: list[str]) -> None:
    headings: dict[str, set[str]] = {}
    for f in md_files(root):
        headings[f.name] = set(HEADING.findall(f.read_text(encoding="utf-8")))
    for f in md_files(root):
        for target, section in SECTION.findall(f.read_text(encoding="utf-8")):
            name = Path(target).name
            if name not in headings:
                fails.append(f"{f.relative_to(root)}: §-pointer to unknown file {target}")
            elif section not in headings[name]:
                have = ", ".join(sorted(headings[name], key=float)) or "none"
                fails.append(
                    f"{f.relative_to(root)}: {target} §{section} does not exist (has: {have})"
                )


def check_rules(root: Path, fails: list[str]) -> None:
    engine = root / "visual-advertising-engine.md"
    if not engine.exists():
        fails.append("visual-advertising-engine.md is missing")
        return
    defined = set(RULE_DEF.findall(engine.read_text(encoding="utf-8")))
    for f in md_files(root):
        for rule in RULE_CITE.findall(f.read_text(encoding="utf-8")):
            if rule not in defined:
                fails.append(f"{f.relative_to(root)}: cites {rule}, not defined in the engine")


def frontmatter(skill: Path) -> dict[str, str]:
    text = skill.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return {}
    block = text.split("\n---\n", 1)[0][4:]
    out, indented = {}, False
    for line in block.split("\n"):
        if not line.strip():
            continue
        if line.startswith((" ", "\t")):  # nested under the previous key
            indented = True
            continue
        indented = False
        key, _, value = line.partition(":")
        out[key.strip()] = value.strip()
    del indented
    return out


def check_frontmatter(root: Path, fails: list[str]) -> dict[str, str]:
    skill = root / "SKILL.md"
    fm = frontmatter(skill)
    if not fm:
        fails.append("SKILL.md: no YAML frontmatter")
        return {}
    for key in ("name", "description"):
        if key not in fm:
            fails.append(f"SKILL.md: frontmatter is missing required `{key}`")
    for key in fm:
        if key not in ALLOWED_KEYS:
            fails.append(
                f"SKILL.md: `{key}` is not an Agent Skills frontmatter key — move it under `metadata`"
            )
    name = fm.get("name", "")
    if name and not NAME.match(name):
        fails.append(f"SKILL.md: name `{name}` must be lowercase letters, digits and hyphens")
    if name and name != root.name and root.name != ".":
        fails.append(f"SKILL.md: name `{name}` should match the skill directory `{root.name}`")
    description = fm.get("description", "")
    if len(description) > MAX_DESCRIPTION:
        fails.append(f"SKILL.md: description is {len(description)} chars, max {MAX_DESCRIPTION}")
    if description and " when " not in description.lower():
        fails.append("SKILL.md: description states no trigger — say when to use the skill")
    return fm


def check_version(root: Path, fm: dict[str, str], fails: list[str]) -> None:
    text = (root / "SKILL.md").read_text(encoding="utf-8")
    match = re.search(r"^\s+version:\s*([0-9]+\.[0-9]+\.[0-9]+)\s*$", text, re.M)
    if not match:
        fails.append("SKILL.md: no `version:` under `metadata`")
        return
    version = match.group(1)
    changelog = root / "CHANGELOG.md"
    if changelog.exists():
        latest = re.search(r"^## \[([0-9]+\.[0-9]+\.[0-9]+)\]", changelog.read_text(encoding="utf-8"), re.M)
        if latest and latest.group(1) != version:
            fails.append(f"CHANGELOG.md tops out at {latest.group(1)}, SKILL.md says {version}")
    for readme in ("README.md", "README.en.md"):
        path = root / readme
        if not path.exists():
            continue
        badge = re.search(r"badge/version-([0-9]+\.[0-9]+\.[0-9]+)", path.read_text(encoding="utf-8"))
        if badge and badge.group(1) != version:
            fails.append(f"{readme} badge says {badge.group(1)}, SKILL.md says {version}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", default=".", type=Path)
    args = parser.parse_args()
    root = args.root.resolve()

    fails: list[str] = []
    check_links(root, fails)
    check_sections(root, fails)
    check_rules(root, fails)
    fm = check_frontmatter(root, fails)
    check_version(root, fm, fails)

    if fails:
        print(f"FAIL — {len(fails)} problem(s):\n")
        for line in fails:
            print(f"  · {line}")
        return 1
    print(f"PASS — {len(md_files(root))} markdown files: links, §-pointers, rule IDs, frontmatter, version")
    return 0


if __name__ == "__main__":
    sys.exit(main())
