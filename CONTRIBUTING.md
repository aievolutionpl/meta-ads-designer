# 🤝 Contributing to Meta Ads Designer

Thanks for helping make AI agents produce less slop and more campaigns. 🙌

This is a **rules repo** — the value is the design doctrine. Every contribution should make the standard sharper, more specific, or more practical.

## Where changes go

| File | Role | When to edit it |
|------|------|-----------------|
| **`visual-advertising-engine.md`** | The canonical standard (34 rules) | **Adding/refining a rule → edit here FIRST.** This is the source of truth. English. |
| `design-rules.md` | The readable charter (English canonical) | Summarize a rule already in the engine. |
| `core.md` | The complete general-knowledge inject | Add only if a rule is so essential it must be in the inject. |
| `SKILL.md` | Agent manual | Procedural/workflow changes. |
| `references/` | Depth (prompts, niches, slop registry) | Concrete, reusable additions (a prompt recipe, a niche pattern, a new slop tell). |
| `README.md` / `README.en.md` | Manuals | `README.md` = Polish main; `README.en.md` = English. Keep in sync. |

## Rule of thumb
**Rule first, summary second.** New principles go into `visual-advertising-engine.md`. Don't only patch the README — a rule that lives only in the manual won't reach agents.

## What makes a good contribution
A rule is useful if it would **prevent a real rejection**. Anchor it in a concrete failure if you can:
- ❌ "Make it look premium" (vague)
- ✅ "Never AI-redraw an official logo — place the original file; a 'plausible' logo is a FAIL" (specific, actionable)

## Process
1. Fork + branch (`feat/my-rule`).
2. Edit the canonical file (`visual-advertising-engine.md`). Give a new rule the next free ID; never renumber an existing one — deprecate it and add a new ID.
3. Update the summary in `core.md` / `design-rules.md` only if the rule is headline-grade.
4. Keep README (PL + EN) in sync if it lists rules.
5. Run `python scripts/check_docs.py` — it fails on dead links, `§`-pointers to sections that don't exist, cited rule IDs the engine never defines, an invalid `SKILL.md` frontmatter, and a version that drifted between the frontmatter, the README badges and this changelog.
6. If you touched `scripts/`, run `python scripts/test_qa.py` and add a case for the behaviour you changed.
7. Open a PR with a one-line "why": the real rejection this rule would have caught.

## Style
- **English is canonical for the rules.** `visual-advertising-engine.md`, `design-rules.md`, `core.md` and `references/` are English; `README.md` is the Polish manual and `README.en.md` the English one. There is no EN mirror of the engine — the duplicate was removed in 5.0.0 because the two copies had drifted.
- **One fact, one home.** If a number lives in `layout-system.md`, other files link to it rather than restating it. Restated numbers drift.
- Banned-word-free copy (we practice what we preach — no "delve", "seamless", "empower"...).

## License
By contributing you agree your work is released under MIT.
