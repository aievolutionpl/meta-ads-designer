---
name: meta-ads-designer
description: Universal plugin that teaches agents how to design beautiful posters, flyers, meta ads and promo graphics — and generate them without AI-slop. Framework-agnostic: works on Hermes, Claude Code, Codex, Cursor, ChatGPT and any agent. Load when the user asks for promotional images for a business/restaurant/hotel/local brand, especially when they upload logo, service or food reference photos.
version: 5.0.0
license: MIT
author: AI Evolution Labs
url: https://github.com/aievolutionpl/meta-ads-designer
---

# 🎨 Meta Ads Designer

> **"Don't generate objects in a void. Generate ads that look like a campaign — with hierarchy, typography, real light, and a structural message."**

This is a **universal plugin** that runs on any AI agent. It teaches **what beautiful design looks like** (the rules), **what the ad should say** (the copy), **what the numbers are** (the layout), and **whether it's good enough to ship** (the gate). Framework-agnostic — host-specific tool details live in `INSTALL.md`, never in the rules.

**LOAD THIS when:** the user asks for a poster, flyer, meta ad, social ad, or promo graphic for a business/restaurant/hotel/local brand — especially when they upload a logo, service photos, or food photos as references. Also for product photography, lifestyle visuals, e-commerce visuals, and image-editing prompts.

---

## ⚡ Load order

1. **`visual-advertising-engine.md`** — the canonical rules, `R01`–`R34`. **Read before any commercial visual.** Cite rule IDs in QA (`FAIL: R30-logo`).
2. **`references/layout-system.md`** — the numbers: grid, safe areas, type scale, font pairings, palettes, the three canonical layouts, the two production modes.
3. **`references/headline-system.md`** — what the ad actually says: the specificity test, ten archetypes, character budgets, the diacritics strategy.
4. **`references/qa-gate.md`** — the scored gate. Nothing ships without it.
5. **`examples/`** — finished briefs → finished prompts → QA verdicts. Read one before writing your first prompt.
6. `design-rules.md` (readable charter + index) · `references/` (niche depth) · `INSTALL.md` (host setup).

---

## 🎯 The non-negotiables

Full text in the engine; these are the ones that decide whether an output looks human-made:

1. **Product First** (R02) — visible, large, lit, sharper than its surroundings.
2. **Reference = Source of Truth** (R03) — never change shape, proportions, colour, construction, material, logo, lettering or mechanism. Label every reference's role.
3. **Commercial realism** (R04) — correct perspective, gravity, shadows, real materials.
4. **One creative = one idea** (R06) — one message, one focal point.
5. **Negative space** (R08) — 8% margins, nothing crossing them.
6. **Say what the light does** (R09) — source, size, direction, quality, where the shadow falls.
7. **Make the camera decision** (R10) — height, angle, focal length, aperture, what's sharp.
8. **Message first, scene second** (R24).
9. **Never let the model invent** logos, prices, names, contact details (R18, R30-logo).
10. **Mobile-first, default 4:5 (1080×1350)** (R19).
11. **Anti-slop** (R05) — every element has a function.

**Final principle: DON'T DECORATE. DIRECT.**

---

## 🔧 WORKFLOW — brief to finished pack

### 1 · Brief intake
Collect: **what** we promote, **for whom**, the **CTA**, the **platforms** (default **4:5**), and **references** (logo, venue, food, products). Also collect **the one fact the business owns** that competitors can't claim — the headline is built from it, and you cannot invent it.

### 2 · Research the niche
Meta Ad Library, Instagram, competitors. What's the standard here? What are this niche's clichés? **If the client has existing ads they like, that is the style source of truth** — elevate their look, don't substitute a generic "premium".

### 3 · Angle matrix
5–10 **distinct promises**, not colour swaps. One headline archetype per creative (`headline-system.md` §2). A batch of five should use five archetypes.

### 4 · Creative work (R28) — before any prompt
Product → benefit → target → angle (Problem/Effect/Lifestyle) → visual metaphor → creative type → **headline** → composition → light + camera → constraints → **only then** the prompt.

### 5 · Route by brief type
- **Food / restaurant** — real dish photos → real-food hero (photo top ~62% + solid panel ~38%, zero text on food). No usable photos → dark studio editorial. → `references/hospitality-food-services-playbook.md` §1, `examples/01`.
- **Hotel / venue** — a distinctive or listed facade is a **Mode B** decision; the model invents balconies. Real photo + deterministic typography and logo. → playbook §2, `examples/02`.
- **Services / local biz** — real install photos as refs → generate NEW premium scenes, never overlay on the client's raw photo. Problem→Effect as a **pair** of creatives, not a split-screen. → playbook §3, `examples/03`.
- **Retail / product** — mechanism needs two references (packshot + drawing). Pin every count. → `references/niche-playbooks.md`, `examples/04`.

### 6 · Choose the production mode (`layout-system.md` §5)
- **Mode A · native in-render text** — short Latin-script copy, ≤12 rendered words, model verified to spell. Quote every word; append the spelling directive.
- **Mode B · deterministic** — logo fidelity, long copy, prices, **any diacritics**. Generate a background with **planned negative space**, then compose.

Decide from the glyphs, at the headline stage. An apostrophe or a `ł` decides this, not taste.

### 7 · Generation
- **One finished ad per generation.** Open with `ONE SINGLE FINISHED AD ONLY — no collage, no grid, no split-screen.`
- Label every reference: `Image A = subject (preserve exactly)`, `Image B = style only`.
- Fill all 11 slots (R25) with **no placeholders left**.
- When a hallucination appears, add it to CONSTRAINTS **by name** — generic preservation language doesn't prevent a repeat.

### 8 · QA gate (mandatory) — `references/qa-gate.md`
1. `python scripts/qa.py out/*.png --format 4:5 --text-box x0,y0,x1,y1`
2. Vision pass with the structured-JSON prompt (§2 of the gate) — it **transcribes** the text rather than confirming it.
3. Score 10 criteria × 0/1/2. **Ship at ≥16/20 with zero hard fails.** Any hard fail → regenerate, don't retouch.
4. Batch: contact sheet (exclude prior sheets from the glob), series consistency (R20), archetype diversity (R21).

### 9 · Delivery
Package files + contact sheet + per-image scores + notes. Report the model/cost if paid. Save references to the client folder for reuse. Say plainly what was fixed and what was regenerated.

---

## 🚫 Quick slop check (before ANY output)

purple/blue default gradient · glassmorphism · neon glow · gradient text · tiny clip-art icons · text slapped on a photo · cream/sand bg · over-round cards · cards-in-cards · icons > content · isometric default · AI-invented food · AI-redrawn logo · an interchangeable headline · a pretty photo with no ad structure.

Full list with fixes: `references/anti-slop-registry.md`.

---

## 🧭 Host routing

| Host | How to load | Notes |
|------|-------------|-------|
| **Hermes** | copy to `~/.hermes/skills/marketing/` | native skill loader |
| **Claude Code** | copy to `~/.claude/skills/` | native skill loader |
| **Codex CLI** | copy to `~/.codex/skills/` | native skill loader |
| **Cursor** | copy to `~/.cursor/skills/` | native skill loader |
| **ChatGPT / Claude / Gemini (chat)** | paste `core.md` as a custom instruction | self-contained one-pager |
| **Any custom agent / API** | inject `core.md` into the system prompt | self-contained |

Full steps per host: `INSTALL.md`.

---

## 📁 Repo structure

```
meta-ads-designer/
├── SKILL.md                        # This file — agent operating manual
├── visual-advertising-engine.md    # THE rules, R01–R34 — single source of truth
├── design-rules.md                 # Readable charter + index to everything
├── core.md                         # 1-page injectable — paste into any chat
├── INSTALL.md                      # Setup on every host
├── CHANGELOG.md
├── examples/                       # Finished briefs → prompts → QA verdicts
│   ├── 00-anti-examples.md         #   weak vs finished, side by side
│   ├── 01-restaurant-real-food.md  #   Mode A, real-food hero
│   ├── 02-hotel-editorial.md       #   Mode B, editorial split
│   ├── 03-services-problem-effect.md
│   └── 04-retail-product-in-use.md
├── references/
│   ├── layout-system.md            # Grid, type scale, palettes, layouts, modes
│   ├── headline-system.md          # Archetypes, budgets, diacritics, CTAs
│   ├── qa-gate.md                  # Scored gate + vision prompt + rubric
│   ├── hospitality-food-services-playbook.md
│   ├── niche-playbooks.md
│   ├── prompt-library.md
│   └── anti-slop-registry.md
└── scripts/
    ├── qa.py                       # Deterministic QA layer
    └── extract_wordmark.py         # White wordmark from a solid-colour logo
```

---

## 📜 License

MIT — use it, remix it, ship it.

---

<br>
<p align="center">
  <b>Created by</b><br>
  <b>AI EVOLUTION LABS</b><br>
  <sub>Channel Islands</sub><br>
  <sub><a href="https://github.com/aievolutionpl/meta-ads-designer">github.com/aievolutionpl/meta-ads-designer</a></sub>
</p>
