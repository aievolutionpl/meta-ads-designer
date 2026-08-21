# Changelog

All notable changes to Meta Ads Designer. Versions follow [SemVer](https://semver.org/): a MAJOR bump means the file layout or rule identifiers changed in a way that affects anyone who installed or forked the plugin.

---

## [5.6.0] — 2026-08-21

A **creative-systems** pass: the skill now treats an ad as one cell in a testable campaign that *learns*, not a one-off picture. Adds the variation matrix, the hook gate, the performance loop, platform compliance, and a video/UGC track — five new canonical rules and seven new reference docs.

### Added
- **`R35` Creative Variation Matrix** — a campaign is a test-ready set: lock the brand, rotate one axis per variant, never two. New `references/variation-matrix.md`.
- **`R36` Hook & Headline First** — the 20→3 hook gate: decide the message before the visual. New `references/hook-engineering.md`.
- **`R37` Performance Feedback Loop** — publish → measure → feed the winner into the next brief; creative → landing continuity. New `references/creative-performance-loop.md`.
- **`R38` Platform Compliance & Multi-Ratio** — per-platform safe zones; every ratio via re-layout, never a dumb crop. New `references/platform-compliance.md`.
- **`R39` Video & Motion Track** — static-first; motion serves the hook; model per motion job. New `references/video-ugc-track.md`.
- **`references/model-routing.md`** — generator + cost decision table (static & video), iteration budget before spend.
- **`references/competitor-ad-teardown.md`** — turn winning competitor ads into testable briefs (research step).

### Changed
- **`SKILL.md`** — the load table now routes to all seven new references with their rule IDs; workflow gained the variation-matrix/hook steps in §3, model routing + a video route in §4, a platform-compliance check in §5, native-per-placement + continuity-note delivery in §6, and a new **§6.5 Performance loop** step. Core rules list grows to 22 (adds `R35`–`R39`).
- **`visual-advertising-engine.md`** — canonical standard grows from 34 to 39 rules (`R01`–`R39`); the links table routes to the new references.
- **`README.md` / `README.en.md`** — version badge, "39 rules", and the new references in the structure tree and file map.

The QA gate, the scripts, and the `R01`–`R34` IDs are untouched — this is a purely additive release (no renumbering, no layout change).

---

## [5.5.0] — 2026-08-19

A structure pass over the skill itself. The rules were fine; the wrapper around them sent the agent to sections that don't exist, to a script path that doesn't resolve, and through ~730 lines of doctrine before it had heard the brief.

### Fixed
- **`SKILL.md` pointed at three sections that were never there.** `design-rules.md §10.5` (two production modes) and `§12` (the QA rule list) do not exist — that file stops at §9 — and the slop check was cited as `§9`, which is the platform-dimensions table. An agent following step 3.6 or the mandatory QA step in 5 found nothing. They now resolve to §4, §8 and §6, each quoted by title so a renumber is visible rather than silent.
- **The QA step told the agent to run `python scripts/qa.py`.** Installed to `~/.claude/skills/meta-ads-designer`, that path resolves against the user's project, where it does not exist. The step now resolves the skill's own directory first and names the dependency install.
- **`visual-advertising-engine.md §25` is a rule ID, not a section number** — cited as `R25` now, like everywhere else.

### Changed
- **`SKILL.md` no longer front-loads the doctrine.** "Load first (in order)" asked for the engine, the charter and the inject — about 730 lines — before the brief was even taken. It is now a load-when table: this file runs the brief, everything else opens at the step that needs it. `core.md` is marked as what it is, the paste-in for chat hosts with no skill loader, and taken off the agent's path.
- **The load table routes to all seven references.** `layout-system.md`, `headline-system.md`, `qa-gate.md`, `anti-slop-registry.md` and `niche-playbooks.md` previously appeared only inside the repo-structure tree, with no cue for when to open them.
- **Frontmatter is a valid Agent Skills header.** `version`, `author` and `url` are not spec keys and a strict loader rejects them; they moved under `metadata`. The description now leads with what the skill does and states its trigger, instead of opening on "Universal plugin that teaches agents…".
- **The 17 quick rules carry their canonical IDs** (`R02`, `R03`, …). The summary and the standard can now be diffed instead of trusted.

### Added
- **`scripts/check_docs.py`** — dead relative links, `§`-pointers to sections that don't exist, rule IDs no rule defines, an invalid `SKILL.md` frontmatter, and version drift between the frontmatter, the README badges and this file. Run against the previous commit it reports 8 problems, including every pointer fixed above.
- **`.github/workflows/ci.yml`** — `check_docs.py` and `test_qa.py` on every push and PR. `test_qa.py` has been in the repo since 5.4.0 with nothing running it.
- **`requirements.txt`** — `pillow`, `numpy`. `INSTALL.md` asked for a bare `pip install pillow numpy` with no pinned floor.
- **`.claude-plugin/plugin.json`** — installable through a Claude Code marketplace, not only by `cp -r`.

---

## [5.4.0] — 2026-08-19

An audit pass over the whole skill. The gate was making ship/no-ship calls it could not actually support, and the docs had drifted from the code and from each other.

### Fixed
- **`scripts/qa.py` — the contrast check reported 1.0 on correctly-set type.** It read the glyph population at the 95th percentile and the backdrop at the 20th, which assumes glyphs cover more than 5% of the text box. A well-set 88px headline on a roomy panel covers far less, so the check compared the panel against itself and failed the repo's own canonical layout. It now anchors on the box median and takes whichever luminance extreme lies further from it, which measures light-on-dark and dark-on-light alike.
- **`scripts/qa.py` — the safe-area check passed a headline sitting 5px from the edge.** The intrusion was expressed as a share of the whole canvas, then compared against 0.4%, a bar a blatant violation never reached. Worse, the metric can't be made to work: a busy full-bleed photograph puts as much edge energy in the margin band as a headline crossing it. `safe_area` is now an exact geometric check on the boxes you declare (`--text-box`, new `--logo-box`), and the old heuristic survives as `margin_activity`, reported and explicitly advisory.
- **`scripts/qa.py` — a PASS without `--text-box` looked like a full PASS.** Four of the seven checks measure the copy block. The report now carries a `note`, and the CLI warns on stderr, when they were skipped.
- **Version drift, again.** `SKILL.md` frontmatter still said 3.0.0 — the exact drift 5.0.0 claimed to have fixed — while the README badges said 5.0.0 and the release history had reached 5.3.0. All now 5.4.0. The 5.1–5.3 entries were also sitting below 3.0.0 at the bottom of this file; the history is now ordered newest-first throughout.
- **`core.md` gave 16:9 as 1080×608**, against 1920×1080 in `design-rules.md` §9 and in `qa.py`. An agent following the inject would have produced a canvas the gate rejects.
- **`layout-system.md` contradicted itself on the 4:5 bottom zone.** §1b listed a 120px keep-out; §3a's canonical panel layout deliberately runs its CTA/logo row 64px from the bottom. The zone is placement-dependent advice, not chrome, and is now labelled as such — only the 9:16 chrome zones are gated.
- **Headline budget mismatch:** `layout-system.md` §2a allowed `2 × 22` on a two-line headline, `headline-system.md` §3 capped the same headline at 40 characters total. Reconciled to ≤22 per line, ≤40 total.
- **The stop-slop grep printed `0` and `CLEAN` together** in both `qa-gate.md` and `anti-slop-registry.md` — `grep -c` exits non-zero on no matches, so the `|| echo` fired on the clean path. Rewritten with `-q`.
- **`INSTALL.md`'s file table listed `layout-system.md`, `headline-system.md` and `qa-gate.md` twice each.**
- **`CONTRIBUTING.md` still told contributors PL was canonical** and to "sync the EN mirror" — a mirror 5.0.0 deleted for having drifted. It now matches reality and states the no-duplication rule.
- **`extract_wordmark.py`'s docstring** claimed it keeps the original pixels. It keeps the original *shapes* (from the source alpha) and flattens colour to pure white or black — fine for a mono wordmark, wrong for a multi-colour mark. Documented, with the multi-colour case pointed back at the original file.

### Added
- **`scripts/test_qa.py`** — thirteen synthetic cases over `qa.py`: the canonical photo+panel layout passes, sparse white-on-navy type measures as high contrast, grey-on-grey fails, boxes crossing the margin or the 9:16 chrome fail, the photo/panel seam is not read as a collage, a 2×2 grid is, and the contact sheet builds. No test framework, same two dependencies as the gate. The 4:5 keep-out contradiction above surfaced here rather than in review.
- **`qa.py --logo-box`** — the logo is checked against the safe area alongside the copy.
- **`qa.py` `margin_activity`** — the advisory margin metric, with a plain-language note on whether the band is quiet or busy.

### Changed
- **`references/qa-gate.md`** rewritten around what the script actually emits: per-check "Needs" column, correct key names (`scrim_uniformity`, not `scrim_alpha`), a truthful sample JSON, and the partial-PASS warning up front.
- **`SKILL.md`** load order now includes `core.md`, the QA step names the exact command, and the repo map lists `CONTRIBUTING.md`, `assets/` and `test_qa.py`.

---

## [5.3.0] — niches expanded to a full per-industry encyclopedia
- `references/niche-playbooks.md` grew from 5 to **15 niches** (added fitness/gym, beauty/spa, real estate, automotive, education, health/clinic/supplements, finance/professional, tech/SaaS, fashion, pets/vet, creative services, wellness/retreats; enriched café, café-coffee, e-commerce retail). Each: What works / What to avoid / Headline archetypes / Typical CTA.
- `core.md` §11 expanded with a niche quick-map (food, hotel, services, retail, fitness, beauty, real estate, tech, finance) + pointers to the deep file.
- Updated niche-playbooks descriptions in README (PL/EN), SKILL, INSTALL.

---

## [5.2.0] — core.md expanded into complete general-knowledge guide
- `core.md` rebuilt from a 1-page rule digest into a self-contained general-knowledge guide for generating beautiful social-media ads: the law, per-platform formats (default 4:5), creative process, composition & hierarchy, real typography, colour, product-first + source of truth, lighting & camera, layouts, copy & headlines (specificity test), niche playbooks (food/hotel/services/retail), two production modes, prompt architecture, anti-slop, series & variation, hard fails, QA gate.
- Updated core.md descriptions across README (PL/EN), SKILL, INSTALL, design-rules, CONTRIBUTING.

---

## [5.1.0] — README overhaul
- Expanded **Problem** section: weak typography, same-look AI, clip-art icons, too much text, AI-slop, altered reference photos, hallucinated dishes/facades/logos, no hierarchy + what the skill changes.
- Added a readable **rules list** (10 core + 8 depth rules: commercial realism, lighting, depth, three angles, series consistency, hard fails).
- Reworked **How the skill works** (layers + two production modes + workflow).
- Added **Agent instructions** section — how an agent given the repo should navigate (core → SKILL → references, 4 pre-generation questions, routing table, QA, delivery).
- PL main (`README.md`) and EN extra (`README.en.md`) kept in sync.

---

## [5.0.1] — README language layout
- `README.md` is now the **Polish** main manual; English moved to **`README.en.md`** (extra).
- Updated language-switcher links and all internal references (`SKILL.md`, `INSTALL.md`, `CONTRIBUTING.md`).

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

## [4.2] — merged banner + README polish
- README (EN + PL) rewritten to explain how the skill works (layers: standard → charter → manual → core → references).
- Banner replaced with the client-supplied artwork (`assets/meta-ads-designer-banner.png`).
- Removed redundant `visual-advertising-engine.en.md` (engine is a single English canonical file) and `assets/make_banner.py`.
- Rebased/merged with the v5.0.0 PR (examples/, scripts/, layout/headline/qa references, CHANGELOG).

---

## [4.1.0] — 2026-08

- Hospitality / food / services playbook from production campaigns: real-food hero layout, dark studio recipe, native in-render text guidance, font sizing, logo handling, service angles. Two production modes and routing by brief type wired into the skill.

---

## [4.0.0]

- Renamed to **meta-ads-designer**; content rebranded (EN/PL). **4:5 (1080×1350) became the default format** across every file. New social preview banner.

---

## [3.1.0]

- Renamed to `art-director`; English flagship files (engine, charter, core); `CONTRIBUTING.md`; EN/PL READMEs.

---

## [3.0.0]

- **Visual Advertising Engine** introduced as the main standard: 34 rules covering Product First, Reference = Source of Truth, Prompt Architecture and Hard Fails.
