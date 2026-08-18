---
name: premium-ad-design
description: Universal plugin that teaches agents how to design beautiful posters, flyers, meta ads and promo graphics — and generate them without AI-slop. Framework-agnostic: works on Hermes, Claude Code, Codex, Cursor, ChatGPT and any agent. Load when the user asks for promotional images for a business/restaurant/hotel/local brand, especially when they upload logo, service or food reference photos.
version: 2.0.0
license: MIT
author: AI Evolution Labs
url: https://github.com/aievolutionpl/premium-ad-design
---

# 🎨 Premium Ad Design

> **"Don't generate objects in a void. Generate ads that look like a campaign — with hierarchy, typography, real light, and a structural message."**

This is a **universal plugin** that runs on any AI agent. It teaches **what beautiful design looks like** (the rules), then guides **how to produce it** (the workflow). It is **framework-agnostic** — the rules are the same whether you run on Hermes, Claude Code, Codex, Cursor, or ChatGPT. Host-specific tool details live in `INSTALL.md` and `references/`, never in the core rules.

**LOAD THIS when:** the user asks for a poster, flyer, meta ad, social ad, or promo graphic for a business/restaurant/hotel/local brand — especially when they upload a logo, service photos, or food photos as references.

---

## ⚡ Load first

1. **`design-rules.md`** — the canonical rules of beautiful advertising (this is the heart; read it before generating).
2. Then follow the workflow below.
3. For host setup (Hermes / Claude / Codex / Cursor / ChatGPT): `INSTALL.md`.
4. For prompts and niche depth: `references/`.

---

## 🔧 WORKFLOW — from brief to finished pack

### 1 · Brief intake
Collect: **what** we promote (product/service/offer/event), **for whom**, the **CTA**, the **platforms** (IG feed 4:5, Stories 9:16, FB 1:1, print), and **reference photos** (logo, venue, food, products). Treat supplied refs as source assets — preserve authenticity.

### 2 · Research the niche
Before generating, find out how top brands in this niche present themselves (Meta Ad Library, Instagram, competitors).
- What's the standard: editorial? dark studio? lifestyle? minimal?
- What are the clichés to avoid here? (e.g. AI-gourmet for a casual taverna)
- **If the client has existing ads they like — that is the source of truth for style.** Elevate *their* look; don't substitute your own generic "premium".

### 3 · Angle matrix
Define **5–10 distinct promises and layouts**, not 10 color swaps. Examples: heritage/luxury poster · editorial travel cover · minimal swiss grid · offer/CTA · events/nightlife · lifestyle/product-in-use · brand story · terrace/dining. Each ad tests a different angle.

### 4 · Generation
- **One finished ad per generation.** Never ask a model to make a batch or contact sheet in one image. Open with: `ONE SINGLE FINISHED AD ONLY — no collage, no grid, no split-screen.`
- **Use reference images with a clear role** for every subject you must preserve (face, product, logo, building). Name each ref's role: "Image A = subject, Image B = style".
- Fill the **5-slot prompt** (SCENE / SUBJECT / DETAILS / USE CASE / CONSTRAINTS — see `references/prompt-library.md`) and bake in the design rules from `design-rules.md`.
- **Native in-scene text** (if the model renders text well): quote EVERY rendered word in quotes; add `CRITICAL: every word spelled perfectly` + the names. Keep text short (brand + headline + one location line).
- Model choice is host-specific — see `references/prompt-library.md` and `INSTALL.md`. Rule of thumb: a model that renders text well for in-scene headlines; a clean-photo pipeline for everything else.

### 5 · QA gate (mandatory)
1. Check dimensions; **scale+pad** (never crop) when text/logo is near an edge.
2. Build a **contact sheet** (exclude prior contact sheets from the glob).
3. Inspect each ad against **every rule in `design-rules.md` §12** — thumbnail readability, spelling (incl. Polish diacritics), hierarchy, accent ≤3, logo fidelity, no fake footers, no text-on-photo slop, no AI-invented food, ad spine present, contrast.
4. Fix minor issues deterministically (clean typography pass); regenerate when the visual is fundamentally wrong.

### 6 · Delivery
- Package final files + contact sheet + short notes; report the model/cost if paid.
- Save reference photos to the client folder for reuse.

---

## 🚫 Quick slop check (before ANY output)

From `design-rules.md` §9 — if any of these is present, fix it:
purple/blue default gradient · glassmorphism · neon glow · gradient text · tiny clip-art icons · text slapped on a photo · cream/sand bg · over-round cards · cards-in-cards · icons > content · gray-on-tinted text · isometric default · AI-invented food · AI-redrawn logo · a pretty photo with no ad structure.

---

## 🧭 Host routing

| Host | How to load | Notes |
|------|-------------|-------|
| **Hermes** | copy to `~/.hermes/skills/marketing/` | native skill loader |
| **Claude Code** | copy to `~/.claude/skills/` | native skill loader |
| **Codex CLI** | copy to `~/.codex/skills/` | native skill loader |
| **Cursor** | copy to `~/.cursor/skills/` | native skill loader |
| **ChatGPT / Claude / Gemini (chat)** | paste `design-rules.md` as a custom instruction, or attach it as a knowledge file | the ruleset is self-contained |
| **Any custom agent / API** | inject `design-rules.md` into the system prompt | the ruleset is self-contained |

Full steps per host: `INSTALL.md`.

---

## 📁 Repo structure

```
premium-ad-design/
├── SKILL.md                # This file — agent operating manual
├── design-rules.md         # THE rules of beautiful advertising (paste-able charter)
├── INSTALL.md              # Setup + usage on every agent (incl. ChatGPT)
├── README.md               # Homepage / manual
├── LICENSE                 # MIT
└── references/
    ├── anti-slop-registry.md   # Full banned-patterns compendium (visual + copy)
    ├── niche-playbooks.md      # Per-industry ad playbooks
    └── prompt-library.md       # Ready-to-use prompt recipes (any model)
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
  <sub><a href="https://github.com/aievolutionpl/premium-ad-design">github.com/aievolutionpl/premium-ad-design</a></sub>
</p>
