# 🚀 INSTALL — how to run Meta Ads Designer on any agent

This plugin is **framework-agnostic**. The same rules work on every agent. Pick your host below.

---

## 1 · Hermes Agent

```bash
git clone https://github.com/aievolutionpl/meta-ads-designer.git
cp -r meta-ads-designer ~/.hermes/skills/marketing/
```

Hermes auto-loads `meta-ads-designer` when you ask for posters/flyers/meta ads. The skill's `design-rules.md` + `SKILL.md` are read automatically.

---

## 2 · Claude Code

```bash
git clone https://github.com/aievolutionpl/meta-ads-designer.git
cp -r meta-ads-designer ~/.claude/skills/
```

Claude Code reads the `SKILL.md` frontmatter and loads the plugin on matching tasks.

---

## 3 · Codex CLI

```bash
git clone https://github.com/aievolutionpl/meta-ads-designer.git
cp -r meta-ads-designer ~/.codex/skills/
```

---

## 4 · Cursor / Windsurf

```bash
git clone https://github.com/aievolutionpl/meta-ads-designer.git
cp -r meta-ads-designer ~/.cursor/skills/   # Cursor
# or ~/.windsurf/skills/  # Windsurf
```

---

## 5 · ChatGPT / Claude / Gemini (chat, no skill loader)

These are chatbots, not skill runners — but the plugin still works, two ways:

**Option A — custom instruction (recommended):**
1. Open Settings → **Custom Instructions** (or the equivalent).
2. Paste the contents of **[`core.md`](core.md)**. It is written as a self-contained general-knowledge inject: formats, creative process, composition, typography, colour, light, layouts, copy, niches, the two production modes, prompt architecture, anti-slop, hard fails and the pass mark.

**Option B — knowledge/attachment:**
Attach `core.md` plus `references/layout-system.md` and `references/headline-system.md` as files, then prompt: *"Apply the Meta Ads Designer rules from the attached files."* Add `examples/01-restaurant-real-food.md` if you want the model to see a finished prompt before writing one.

> **Prompt starter:** "Make a 4:5 social ad for [business]. Here are the reference photos: [attach logo/venue/food]. Follow the Meta Ads Designer rules: one headline that passes the specificity test, real named typefaces, brand palette with one accent, 8% margins, no text-on-photo slop, real food from my photos, my logo unaltered, CTA 'Reserve a table'. Show me 3 structurally different concepts first, each using a different headline archetype."

---

## 6 · Any custom agent / API

Inject **`core.md`** into your system prompt (fully self-contained), or load `SKILL.md` if your harness supports native skills. For maximum strictness, inject `visual-advertising-engine.md` as well — it's the canonical rule set with stable IDs the agent can cite back to you.

---

## 7 · The scripts (optional but recommended)

The QA gate's deterministic layer and the wordmark extractor need two common packages:

```bash
pip install pillow numpy

python scripts/qa.py out/*.png --format 4:5 --text-box 86,843,994,1290
python scripts/extract_wordmark.py refs/logo.png build/logo_white.png
```

`qa.py` exits non-zero when any image fails, so it drops into CI or a pre-delivery hook. Everything else in the repo is plain Markdown with no dependencies.

---

## ✅ Verify it's loaded

Ask the agent: *"What is the specificity test, and what's the default margin on a 1080×1350 ad?"*
- **Correct:** "could a competitor paste this headline unchanged" — and "86px, 8% of the short edge".
- **Didn't load:** generic advice about making it premium and professional. Re-check the install path or re-paste.

---

## 🧭 Which file does what

| File | Use it for |
|------|-----------|
| `visual-advertising-engine.md` | **The rules** — R01–R34, single source of truth. Follow before any commercial visual |
| `references/layout-system.md` | The numbers — grid, type scale, palettes, layouts, production modes |
| `references/headline-system.md` | The words — archetypes, budgets, diacritics strategy, CTAs |
| `references/qa-gate.md` | The pass mark — script + vision prompt + scored rubric |
| `examples/` | Finished briefs → finished prompts → QA verdicts |
| `core.md` | The complete general-knowledge inject for chat hosts |
| `design-rules.md` | Readable charter + index to everything |
| `SKILL.md` | Agent operating manual (skill loaders read this) |
| `references/hospitality-food-services-playbook.md` | Deep rules: food / hotel / services |
| `references/layout-system.md` | Layout + panel-height + gradient values |
| `references/headline-system.md` | Headline sizing & contrast rules |
| `references/qa-gate.md` | QA gate & rejection criteria |
| `references/niche-playbooks.md` | 15 per-industry playbooks (What works / Avoid / Headline / CTA) |
| `references/prompt-library.md` | Prompt skeletons |
| `references/anti-slop-registry.md` | Full banned-pattern list + grep gate |
| `scripts/` | `qa.py`, `extract_wordmark.py` |
