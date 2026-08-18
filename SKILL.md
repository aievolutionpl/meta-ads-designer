---
name: meta-ads-designer
description: Universal plugin that teaches agents how to design beautiful posters, flyers, meta ads and promo graphics — and generate them without AI-slop. Framework-agnostic: works on Hermes, Claude Code, Codex, Cursor, ChatGPT and any agent. Load when the user asks for promotional images for a business/restaurant/hotel/local brand, especially when they upload logo, service or food reference photos.
version: 3.0.0
license: MIT
author: AI Evolution Labs
url: https://github.com/aievolutionpl/meta-ads-designer
---

# 🎨 Meta Ads Designer

> **"Don't generate objects in a void. Generate ads that look like a campaign — with hierarchy, typography, real light, and a structural message."**

This is a **universal plugin** that runs on any AI agent. It teaches **what beautiful design looks like** (the rules), then guides **how to produce it** (the workflow). It is **framework-agnostic** — the rules are the same whether you run on Hermes, Claude Code, Codex, Cursor, or ChatGPT. Host-specific tool details live in `INSTALL.md` and `references/`, never in the core rules.

**LOAD THIS when:** the user asks for a poster, flyer, meta ad, social ad, or promo graphic for a business/restaurant/hotel/local brand — especially when they upload a logo, service photos, or food photos as references. Also load for product photography, lifestyle visuals, e-commerce visuals, and image-editing prompts.

---

## ⚡ Load first (in order)

1. **`visual-advertising-engine.md`** — the 34-rule operating standard (Product First, Reference = Source of Truth, Prompt Architecture, Hard Fails, QA). **Read this before any commercial visual.**
2. **`design-rules.md`** — the canonical charter of beautiful advertising (the readable summary of the engine).
3. Then follow the workflow below.
4. For host setup (Hermes / Claude / Codex / Cursor / ChatGPT): `INSTALL.md`.
5. For prompts and niche depth: `references/`.

---

## 🎯 Core rules (non-negotiable)

1. **Product First** — the product is the main character: visible, large, lit, sharper than surroundings, attractive angle. Never hide it in a big set.
2. **Reference = Source of Truth** — a supplied product photo is a technical document. NEVER change shape/proportions/color/construction/material/logo/lettering/mechanism. Only environment, light, frame, perspective, styling. Respect the product's physics.
3. **Commercial realism** — professional commercial photography, not "obvious AI ad". Correct perspective, scale, gravity, shadows, real materials.
4. **One creative = one idea** — one message, one focal point. Don't cram product + 7 benefits + promo + reviews.
5. **Hierarchy** — PRIMARY (product) → SECONDARY (context) → TERTIARY (subtle atmosphere).
6. **Negative space** — don't fill the frame. Space = premium + room for the headline.
7. **Lighting is part of the product** — say exactly what the light does (clean commercial / premium dramatic / natural lifestyle / food commercial).
8. **Think like a photographer** — decide camera position, angle, lens, depth of field, foreground/midground/background.
9. **Build depth** — foreground → subject → background. No flat images.
10. **Show product in use** — packshot alone isn't enough; a hand/gesture/POV gives context.
11. **Typography after the image** — strong photo first, then headline → support → CTA. Not a dashboard.
12. **Don't generate important text in-image** — if the model is weak at text, generate a clean visual and add real typography + the real logo later.
13. **Mobile-first composition — DEFAULT is 4:5 (1080×1350)**, the Instagram/Facebook feed default; 9:16 for Reels/Stories, 1:1 marketplace, 16:9 — only when the user asks. Compose for the format; don't rely on cropping.
14. **Series consistency** — product identical across 5–10 images; only context/frame/mood/light change. Like one shoot.
15. **Variation, not randomness** — hero · lifestyle · feature · close-up · problem · result · premium · UGC · unexpected angle.
16. **Food builds appetite** — texture, steam, gloss, juiciness, layers; Frozen-Time/Bullet-Time for dynamic scenes. Physically credible.
17. **Anti-slop** — no random neon, HUD, icons, gradients, arrows, fake logos, excessive bokeh, plastic surfaces. Every element has a function.

**Final principle: DON'T DECORATE. DIRECT.** One product. One idea. One strong visual.

---

## 🔧 WORKFLOW — from brief to finished pack

### 1 · Brief intake
Collect: **what** we promote (product/service/offer/event), **for whom**, the **CTA**, the **platforms** (default ratio **4:5 = 1080×1350**, the Instagram/Facebook feed default; 9:16 for Reels/Stories, 1:1 for marketplace — use 4:5 unless the user asks otherwise), and **reference photos** (logo, venue, food, products). Treat supplied refs as source assets — preserve authenticity.

### 2 · Research the niche
Before generating, find out how top brands in this niche present themselves (Meta Ad Library, Instagram, competitors).
- What's the standard: editorial? dark studio? lifestyle? minimal?
- What are the clichés to avoid here? (e.g. AI-gourmet for a casual taverna)
- **If the client has existing ads they like — that is the source of truth for style.** Elevate *their* look; don't substitute your own generic "premium".

### 3 · Angle matrix
Define **5–10 distinct promises and layouts**, not 10 color swaps. Examples: heritage/luxury poster · editorial travel cover · minimal swiss grid · offer/CTA · events/nightlife · lifestyle/product-in-use · brand story · terrace/dining. Each ad tests a different angle.

### 3.5 · Creative generation (before writing any prompt)
Do **not** jump to the prompt. Run the engine's creative workflow first:
1. **Identify the product.** 2. **Identify the most important benefit.** 3. **Define the target.** 4. **Choose the marketing angle** (Problem / Effect / Lifestyle). 5. **Invent a simple visual metaphor or situation.** 6. **Choose the creative type** (from the library: hero, packshot, lifestyle, product-in-use, macro, problem/solution, result, UGC, editorial, scroll-stopper). 7. **Design the composition.** 8. **Define light and camera.** 9. **Add constraints.** 10. **Only then write the final prompt** using the 11-part architecture in `visual-advertising-engine.md` §25.

### 3.6 · Route by brief type
- **Food / restaurant:** two modes (see `design-rules.md` §10.5). If the client has real dish photos → **real-food hero** (photo top ~60–65% + solid panel bottom ~35–40%, zero text on food). If not → **dark studio editorial**. **Native AI text in-scene is the default** (keep strings SHORT: brand + headline + 1 location line; append `CRITICAL: every word spelled PERFECTLY`). Depth: `references/hospitality-food-services-playbook.md`.
- **Hotel / venue:** prefer **real-photo + deterministic typography/logo** over AI re-generation of the building. Design system: serif headline + clean sans body, coastal palette (navy/teal/cream/white/gold), real photo hero + content card. Produce structurally different styles (heritage poster · travel cover · swiss grid · terrace · dining · direct-booking · events · seaside · offer · brand story).
- **Services / local biz:** real product/install photos as refs → generate NEW premium scenes (never overlay on the client's raw photo). Angles: Problem→Effect · package tiers · deadline offers · transformation · benefit-led headline ≤40 chars. Use **deterministic composition** when text/logo fidelity matters.

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
meta-ads-designer/
├── SKILL.md                # This file — agent operating manual
├── core.md                 # 1-page injectable rules — paste into any chat/agent
├── visual-advertising-engine.md  # THE 34-rule operating standard (canonical, EN)
├── design-rules.md         # Readable charter of beautiful advertising (English canonical)
├── INSTALL.md              # Setup + usage on every agent (incl. ChatGPT)
├── README.md               # Homepage / manual (EN)
├── README.pl.md            # Homepage / manual (PL)
├── CHANGELOG.md            # Version history
├── LICENSE                 # MIT
├── examples/               # Worked ad examples (food, hotel, services, retail)
├── scripts/                # extract_wordmark.py, qa.py
└── references/
    ├── hospitality-food-services-playbook.md # Deep rules: food / hotel / services
    ├── layout-system.md        # Layout + panel-height + gradient values
    ├── headline-system.md      # Headline sizing & contrast rules
    ├── qa-gate.md              # QA gate & rejection criteria
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
  <sub><a href="https://github.com/aievolutionpl/meta-ads-designer">github.com/aievolutionpl/meta-ads-designer</a></sub>
</p>
