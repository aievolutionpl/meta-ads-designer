# 🤝 Contributing to Meta Ads Designer

Thanks for helping make AI agents produce less slop and more campaigns. 🙌

This is a **rules repo** — the value is the design doctrine. Every contribution should make the standard sharper, more specific, or more executable.

## Where changes go

| File | Role | When to edit it |
|------|------|-----------------|
| **`visual-advertising-engine.md`** | The canonical rules, `R01`–`R34` | **Adding or refining a rule → edit here FIRST.** Single source of truth. |
| `references/layout-system.md` | The numbers — grid, type scale, palettes, layouts, modes | A value changed, or a new one is needed. Numbers live here, nowhere else. |
| `references/headline-system.md` | The words — archetypes, budgets, diacritics, CTAs | A new archetype, a budget correction, a language-specific rule. |
| `references/qa-gate.md` + `scripts/qa.py` | The pass mark | A new check, a threshold change, a rubric criterion. |
| `examples/` | Finished briefs → prompts → verdicts | A new brief type, or a real failure mode worth showing. |
| `core.md` | The 1-page inject | Only if a rule is so essential it must travel in the inject. |
| `design-rules.md` | Readable charter + index | A new file exists and the map needs updating. |
| `SKILL.md` | Agent manual | Procedural/workflow changes. |
| `references/` (rest) | Niche depth, prompt skeletons, slop registry | Concrete, reusable additions. |
| `README.md` / `README.pl.md` | Manuals | Keep both in sync. |

## Two rules for the rules

**1 · Rule first, summary second.** New principles go into `visual-advertising-engine.md`. A rule that lives only in the README won't reach agents.

**2 · Rule IDs are permanent.** A new rule gets the next free `R` id. Never renumber, never reuse — QA verdicts, examples and other repos cite these IDs. To retire a rule, mark it deprecated and leave the id in place.

## Don't duplicate

If a value appears in two files, one of them will drift — this repo has already been through that. Numbers belong in `layout-system.md`; every other file **links** to them. The same goes for copy rules (`headline-system.md`) and QA thresholds (`qa-gate.md`).

## What makes a good contribution

A rule is useful if it would **prevent a real rejection**. Anchor it in a concrete failure:

- ❌ "Make it look premium" — vague, unexecutable
- ✅ "Never AI-redraw an official logo — place the original file; a 'plausible' logo is a FAIL" — specific, checkable
- ✅ "Never render a brand name containing an apostrophe natively; leave the space and place the logo" — a failure mode with a fix

Prefer numbers to adjectives, and a named failure to a general principle.

## Process

1. Fork + branch (`feat/my-rule`).
2. Edit the canonical file for that kind of change (see the table).
3. Update `core.md` only if the rule is headline-grade.
4. Update `design-rules.md`'s index if you added a file.
5. If you touched `scripts/`, run it against a real image before opening the PR.
6. Keep README (EN + PL) in sync if it lists files.
7. Open the PR with a one-line "why": the real rejection this would have caught.

## Style

- **English is canonical** for the rules and references. `README.pl.md` is the Polish manual; Polish-specific guidance (diacritics, CTAs) lives inside the English files where it belongs.
- Banned-word-free copy — we practise what we preach.
- No em dashes in ad copy examples. Commas, colons, or a `·`.

## License

By contributing you agree your work is released under MIT.
