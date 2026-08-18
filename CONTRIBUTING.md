# 🤝 Contributing to Meta Ads Designer

Thanks for helping make AI agents produce less slop and more campaigns. 🙌

This is a **rules repo** — the value is the design doctrine. Every contribution should make the standard sharper, more specific, or more practical.

## Where changes go

| File | Role | When to edit it |
|------|------|-----------------|
| **`visual-advertising-engine.md`** | The canonical standard (34 rules) | **Adding/refining a rule → edit here FIRST.** This is the source of truth. |
| `visual-advertising-engine.en.md` | EN mirror of the standard | Update together with the PL file (keep both in sync). |
| `design-rules.md` / `design-rules.en.md` | The readable charter | Summarize a rule already in the engine. |
| `core.md` | The 1-page inject | Add only if a rule is so essential it must be in the inject. |
| `SKILL.md` | Agent manual | Procedural/workflow changes. |
| `references/` | Depth (prompts, niches, slop registry) | Concrete, reusable additions (a prompt recipe, a niche pattern, a new slop tell). |
| `README.md` / `README.pl.md` | Manuals | Keep in sync (EN + PL). |

## Rule of thumb
**Rule first, summary second.** New principles go into `visual-advertising-engine.md`. Don't only patch the README — a rule that lives only in the manual won't reach agents.

## What makes a good contribution
A rule is useful if it would **prevent a real rejection**. Anchor it in a concrete failure if you can:
- ❌ "Make it look premium" (vague)
- ✅ "Never AI-redraw an official logo — place the original file; a 'plausible' logo is a FAIL" (specific, actionable)

## Process
1. Fork + branch (`feat/my-rule`).
2. Edit the canonical file (engine) + sync the EN mirror.
3. Update the summary in `core.md` / `design-rules.md` only if the rule is headline-grade.
4. Keep README (EN + PL) in sync if it lists rules.
5. Open a PR with a one-line "why": the real rejection this rule would have caught.

## Style
- **PL is canonical** for the standard; keep the EN mirror identical in meaning.
- Banned-word-free copy (we practice what we preach — no "delve", "seamless", "empower"...).

## License
By contributing you agree your work is released under MIT.
