# Changelog

All notable changes to Meta Ads Designer. Versions follow [SemVer](https://semver.org/): a MAJOR bump means the file layout or rule identifiers changed in a way that affects anyone who installed or forked the plugin.

---

## [5.0.0] — 2026-08-18

The plugin knew what good design *is*. This release makes it executable: numbers instead of adjectives, a copy system instead of a word ban, a scored gate instead of a checklist, and finished examples instead of placeholders.

### Added
- **`references/layout-system.md`** — the numbers. 12-column grid, 8% safe areas per placement, a type scale in px with character budgets, named font pairings with fallbacks and licence notes, starter palettes per category, three canonical layouts with exact panel heights and scrim values, and the two production modes as a decision table.
- **`references/headline-system.md`** — the words. The specificity test, ten headline archetypes with real examples, character budgets locked to the type scale, CTAs per category in EN/PL, a Polish-diacritics strategy, a banned-constructions list, and an eight-step generation routine with a worked example.
- **`references/qa-gate.md`** — the pass mark. Three layers: `scripts/qa.py`, a copy-paste vision prompt returning structured JSON, and a 10-criteria rubric scored 0/1/2 with a shipping threshold of ≥16/20 and zero hard fails.
- **`scripts/qa.py`** — deterministic QA: dimensions, safe-area intrusion, WCAG text contrast, collage/grid detection, thumbnail legibility, focal dispersion, scrim uniformity, plus contact-sheet building. Exits non-zero on failure, so it drops into CI.
- **`scripts/extract_wordmark.py`** — extracts a white (or dark) wordmark from a solid-colour logo by masking the original pixels, never redrawing them. Warns below the 180px legibility minimum.
- **`examples/`** — five files. Four end-to-end cases (restaurant Mode A, hotel Mode B, services Problem→Effect, retail series) each running brief → creative work → headline drafting → finished prompt → QA score → the fix, plus `00-anti-examples.md` showing the same brief written weakly and properly.
- **`CHANGELOG.md`** — this file.

### Changed
- **Rules now have stable IDs.** `visual-advertising-engine.md` numbers every rule `R01`–`R34`, with sub-ids for hard fails (`R30-logo`, `R30-text`). Cite them in QA verdicts. IDs are permanent and never renumbered.
- **`design-rules.md` stopped restating the rules** and became the readable charter plus the index to every other file. It was one of four places the same 17 rules were written out.
- **`SKILL.md`** rewritten around the new load order, with mode selection and the scored gate as explicit workflow steps.
- **`core.md`** rewritten: the same doctrine plus the layout numbers, the headline method and the pass mark, still one page.
- **`references/anti-slop-registry.md`** and **`references/niche-playbooks.md`** translated to English and extended with headline archetypes per niche.
- **`references/prompt-library.md`** reframed as skeletons that point at the finished examples, with the model-selection table de-hardcoded (capability changes faster than this repo).
- **`references/hospitality-food-services-playbook.md`** de-duplicated against the new system files, client names removed, scrim values reconciled with `layout-system.md`, and the inline Python replaced by `scripts/extract_wordmark.py`.
- **`INSTALL.md`** points chat hosts at `core.md` rather than the charter, and documents the scripts.
- **`CONTRIBUTING.md`** documents the rule-ID policy and the no-duplication rule.

### Removed
- **`visual-advertising-engine.en.md`** — it was byte-identical to the file it was supposedly mirroring.
- **`design-rules.en.md`** — the two copies had already drifted (the EN version carried a workflow step the PL one didn't). English is now canonical for the rules; `README.md` is the Polish main manual and `README.en.md` the English extra.

### Fixed
- Version drift between `SKILL.md` frontmatter (3.0.0), the README badges (4.0.0) and the release history (v4.1) — all now 5.0.0.
- Contradictory scrim values between the playbook (`alpha 220 / 530px`) and its own legibility section (`alpha 255 / ≥720px`) — reconciled to one value in `layout-system.md`.
- Type sizing given in `pt` in one file and `px` in another.

### Migration notes
- Anyone linking to `visual-advertising-engine.en.md` or `design-rules.en.md` should point at `visual-advertising-engine.md` / `design-rules.md`.
- Skill installs: re-copy the folder; the new `examples/` and `scripts/` directories are part of the plugin.
- `pip install pillow numpy` if you want the deterministic QA layer. Everything else stays dependency-free Markdown.

---

## [4.1.0] — 2026-08

- Hospitality / food / services playbook from production campaigns: real-food hero layout, dark studio recipe, native in-render text guidance, font sizing, logo handling, service angles. Two production modes and routing by brief type wired into the skill.

## [4.0.0]

- Renamed to **meta-ads-designer**; content rebranded (EN/PL). **4:5 (1080×1350) became the default format** across every file. New social preview banner.

## [3.1.0]

- Renamed to `art-director`; English flagship files (engine, charter, core); `CONTRIBUTING.md`; EN/PL READMEs.

## [3.0.0]

- **Visual Advertising Engine** introduced as the main standard: 34 rules covering Product First, Reference = Source of Truth, Prompt Architecture and Hard Fails.

## [4.2] — merged banner + README polish
- README (EN + PL) rewritten to explain how the skill works (layers: standard → charter → manual → core → references).
- Banner replaced with the client-supplied artwork (`assets/meta-ads-designer-banner.png`).
- Removed redundant `visual-advertising-engine.en.md` (engine is a single English canonical file) and `assets/make_banner.py`.
- Rebased/merged with the v5.0.0 PR (examples/, scripts/, layout/headline/qa references, CHANGELOG).

## [5.0.1] — README language layout
- `README.md` is now the **Polish** main manual; English moved to **`README.en.md`** (extra).
- Updated language-switcher links and all internal references (`SKILL.md`, `INSTALL.md`, `CONTRIBUTING.md`).
