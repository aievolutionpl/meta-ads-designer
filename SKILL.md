---
name: meta-ads-designer
description: Designs and generates posters, flyers, Meta/social ads and promo graphics that look art-directed instead of AI-generated - hierarchy, real typography, real light, one message per creative. Use when the user asks for an ad, poster, flyer, promo or social graphic for a business, restaurant, hotel or local brand, especially when a logo, venue, product or food photo is attached; also for product photography, lifestyle and e-commerce visuals, and image-editing prompts. Framework-agnostic - runs on Hermes, Claude Code, Codex, Cursor and ChatGPT.
license: MIT
metadata:
  version: 5.6.0
  author: AI Evolution Labs
  url: https://github.com/aievolutionpl/meta-ads-designer
---

# 🎨 Meta Ads Designer

> **"Don't generate objects in a void. Generate ads that look like a campaign — with hierarchy, typography, real light, and a structural message."**

This is a **universal plugin** that runs on any AI agent. It teaches **what beautiful design looks like** (the rules), then guides **how to produce it** (the workflow). It is **framework-agnostic** — the rules are the same whether you run on Hermes, Claude Code, Codex, Cursor, or ChatGPT. Host-specific tool details live in `INSTALL.md` and `references/`, never in the core rules.

**LOAD THIS when:** the user asks for a poster, flyer, meta ad, social ad, or promo graphic for a business/restaurant/hotel/local brand — especially when they upload a logo, service photos, or food photos as references. Also load for product photography, lifestyle visuals, e-commerce visuals, and image-editing prompts.

---

## ⚡ How to load this skill

**Read this file first.** It carries the intake, the routing, the workflow and the QA gate — enough to run a brief end to end. Pull anything else in **only at the step that needs it**. All paths are relative to this skill's own directory (call it `SKILL_DIR`), not to the user's working directory.

| Open | At which point |
|------|----------------|
| `visual-advertising-engine.md` | **Before writing any prompt for a commercial visual.** The 39-rule operating standard, `R01`–`R39` — every other file cites these IDs. |
| `design-rules.md` | You want the doctrine in prose, or the index of which file answers which question. |
| `references/layout-system.md` | Placing anything: grid, margins, panel heights, type scale, palettes. |
| `references/headline-system.md` | Writing the copy inside the ad: archetypes, character budgets, diacritics, CTAs. |
| `references/variation-matrix.md` | Step 3 — turning one promise into a test-ready set (lock brand, rotate one axis). `R35` |
| `references/hook-engineering.md` | Step 3 — the 20→3 hook gate: decide the message before the visual. `R36` |
| `references/creative-performance-loop.md` | Step 6.5 — publishing, measuring, and feeding results into the next brief. `R37` |
| `references/platform-compliance.md` | Step 5 — safe zones per platform and ratio re-layout (never a dumb crop). `R38` |
| `references/video-ugc-track.md` | The brief needs video/UGC/motion. `R39` |
| `references/model-routing.md` | Choosing the generator and the iteration budget before spending. |
| `references/competitor-ad-teardown.md` | Step 2 — turning winning competitor ads into testable briefs. |
| `references/prompt-library.md` | Filling the 5-slot prompt, or choosing a model. |
| `references/hospitality-food-services-playbook.md` | The brief is food, restaurant, hotel, venue or a local service. |
| `references/niche-playbooks.md` | Any other industry — 15 playbooks. |
| `references/anti-slop-registry.md` | An output looks generic and you need the named pattern and the grep gate. |
| `references/qa-gate.md` | Step 5 — the scored rubric behind the script. |
| `examples/` | You want a finished brief → prompt → verdict before writing your own. |
| `INSTALL.md` | Host setup, or the user asks how to install this. |

**Skip `core.md`.** It is the self-contained inject for chat hosts that have no skill loader (paste into ChatGPT/Gemini custom instructions). If you are reading `SKILL.md` you can reach the engine directly, and the engine outranks it.

---

## 🎯 Core rules (non-negotiable)

1. **Product First** — the product is the main character: visible, large, lit, sharper than surroundings, attractive angle. Never hide it in a big set. `R02`
2. **Reference = Source of Truth** — a supplied product photo is a technical document. NEVER change shape/proportions/color/construction/material/logo/lettering/mechanism. Only environment, light, frame, perspective, styling. Respect the product's physics. `R03`
3. **Commercial realism** — professional commercial photography, not "obvious AI ad". Correct perspective, scale, gravity, shadows, real materials. `R04`
4. **One creative = one idea** — one message, one focal point. Don't cram product + 7 benefits + promo + reviews. `R06`
5. **Hierarchy** — PRIMARY (product) → SECONDARY (context) → TERTIARY (subtle atmosphere). `R07`
6. **Negative space** — don't fill the frame. Space = premium + room for the headline. `R08`
7. **Lighting is part of the product** — say exactly what the light does (clean commercial / premium dramatic / natural lifestyle / food commercial). `R09`
8. **Think like a photographer** — decide camera position, angle, lens, depth of field, foreground/midground/background. `R10`
9. **Build depth** — foreground → subject → background. No flat images. `R11`
10. **Show product in use** — packshot alone isn't enough; a hand/gesture/POV gives context. `R12`
11. **Typography after the image** — strong photo first, then headline → support → CTA. Not a dashboard. `R17`
12. **Don't generate important text in-image** — if the model is weak at text, generate a clean visual and add real typography + the real logo later. `R18`
13. **Mobile-first composition — DEFAULT is 4:5 (1080×1350)**, the Instagram/Facebook feed default; 9:16 for Reels/Stories, 1:1 marketplace, 16:9 — only when the user asks. Compose for the format; don't rely on cropping. `R19`
14. **Series consistency** — product identical across 5–10 images; only context/frame/mood/light change. Like one shoot. `R20`
15. **Variation, not randomness** — hero · lifestyle · feature · close-up · problem · result · premium · UGC · unexpected angle. `R21`
16. **Food builds appetite** — texture, steam, gloss, juiciness, layers; Frozen-Time/Bullet-Time for dynamic scenes. Physically credible. `R15`
17. **Anti-slop** — no random neon, HUD, icons, gradients, arrows, fake logos, excessive bokeh, plastic surfaces. Every element has a function. `R05`
18. **Variation matrix** — a campaign is a test-ready set: lock the brand, rotate one axis per variant, never two. `R35`
19. **Hook & headline first** — decide the message before the visual; run the 20→3 hook gate. `R36`
20. **Performance feedback** — publish, measure, feed the winner into the next brief; ad promise = landing page promise. `R37`
21. **Platform compliance & multi-ratio** — safe zones per placement, every ratio by re-layout (never a dumb crop). `R38`
22. **Video & motion track** — static-first; motion serves the hook, never decorates. `R39`

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
- **Teardown the winners.** Reduce 3–5 proven competitor ads to angle + hook + layout + format, then re-express the structure for this client. See `references/competitor-ad-teardown.md`.

### 3 · Angle matrix
Define **5–10 distinct promises and layouts**, not 10 color swaps. Examples: heritage/luxury poster · editorial travel cover · minimal swiss grid · offer/CTA · events/nightlife · lifestyle/product-in-use · brand story · terrace/dining. Each ad tests a different angle.

Then turn the promise into a **variation matrix**: lock the brand, pick the one rotating axis, define 3 structurally different variants. Run the **20→3 hook gate** before the visual. See `references/variation-matrix.md` and `references/hook-engineering.md`.

### 3.5 · Creative generation (before writing any prompt)
Do **not** jump to the prompt. Run the engine's creative workflow first:
1. **Identify the product.** 2. **Identify the most important benefit.** 3. **Define the target.** 4. **Choose the marketing angle** (Problem / Effect / Lifestyle). 5. **Invent a simple visual metaphor or situation.** 6. **Choose the creative type** (from the library: hero, packshot, lifestyle, product-in-use, macro, problem/solution, result, UGC, editorial, scroll-stopper). 7. **Design the composition.** 8. **Define light and camera.** 9. **Add constraints.** 10. **Only then write the final prompt** using the 11-part architecture in `visual-advertising-engine.md` `R25`.

### 3.6 · Route by brief type
- **Food / restaurant:** two modes (see `design-rules.md` §4 "The two production modes"). If the client has real dish photos → **real-food hero** (photo top ~60–65% + solid panel bottom ~35–40%, zero text on food). If not → **dark studio editorial**. **Native AI text in-scene is the default** (keep strings SHORT: brand + headline + 1 location line; append `CRITICAL: every word spelled PERFECTLY`). Depth: `references/hospitality-food-services-playbook.md`.
- **Hotel / venue:** prefer **real-photo + deterministic typography/logo** over AI re-generation of the building. Design system: serif headline + clean sans body, coastal palette (navy/teal/cream/white/gold), real photo hero + content card. Produce structurally different styles (heritage poster · travel cover · swiss grid · terrace · dining · direct-booking · events · seaside · offer · brand story).
- **Services / local biz:** real product/install photos as refs → generate NEW premium scenes (never overlay on the client's raw photo). Angles: Problem→Effect · package tiers · deadline offers · transformation · benefit-led headline ≤40 chars. Use **deterministic composition** when text/logo fidelity matters.

### 4 · Generation
- **One finished ad per generation.** Never ask a model to make a batch or contact sheet in one image. Open with: `ONE SINGLE FINISHED AD ONLY — no collage, no grid, no split-screen.`
- **Use reference images with a clear role** for every subject you must preserve (face, product, logo, building). Name each ref's role: "Image A = subject, Image B = style".
- Fill the **5-slot prompt** (SCENE / SUBJECT / DETAILS / USE CASE / CONSTRAINTS — see `references/prompt-library.md`) and bake in the design rules from `design-rules.md`.
- **Native in-scene text** (if the model renders text well): quote EVERY rendered word in quotes; add `CRITICAL: every word spelled perfectly` + the names. Keep text short (brand + headline + one location line).
- **Route the model to the job** — native text, clean photo, re-composition, or video/UGC. Decide the generator and the iteration budget *before* spending: see `references/model-routing.md` and `INSTALL.md`.
- **The brief needs motion?** Run the video/UGC track (static-first, model per motion job): `references/video-ugc-track.md`.

### 5 · QA gate (mandatory)
1. Run `python "$SKILL_DIR/scripts/qa.py" <file> --format 4:5 --text-box x0,y0,x1,y1` (add `--logo-box` when a logo is placed). `SKILL_DIR` is the directory this file sits in — resolve it before you call the script; a bare `scripts/qa.py` resolves against the user's project, where it does not exist. Needs `pillow` and `numpy` (`pip install -r "$SKILL_DIR/requirements.txt"`). **Declare the boxes** — without them the safe-area, contrast, thumbnail and scrim checks report `n/a` and the PASS means only "right dimensions, no collage". Fix edge intrusions with **scale+pad**, never a crop.
2. Build a **contact sheet** (exclude prior contact sheets from the glob).
3. Inspect each ad against **every rule in `design-rules.md` §8 "The QA gate"** — thumbnail readability, spelling (incl. Polish diacritics), hierarchy, accent ≤3, logo fidelity, no fake footers, no text-on-photo slop, no AI-invented food, ad spine present, contrast.
4. **Check platform compliance** — safe zones for each placement and ratio re-layout (never a dumb crop). See `references/platform-compliance.md` (`R38`).
5. Fix minor issues deterministically (clean typography pass); regenerate when the visual is fundamentally wrong.

### 6 · Delivery
- Package final files + contact sheet + short notes; report the model/cost if paid. Save reference photos to the client folder for reuse.
- **Deliver native files per placement** (4:5 feed, 9:16 short, 1:1 marketplace, 16:9 video), each QA'd — not one image the client has to hack.
- **Continuity note** — if the landing page is known, state the promise the page must open with (creative → landing continuity, `R37` §4).

### 6.5 · Performance loop (after the campaign ships)
An ad is finished when its results come back. Publish → measure (CTR, CPA/ROAS, hook-through, 3s hold) → label the winning angle/format → carry it forward as the default in the next variation matrix. See `references/creative-performance-loop.md` (`R37`).

---

## 🚫 Quick slop check (before ANY output)

From `design-rules.md` §6 "Quick slop check" — if any of these is present, fix it:
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
├── core.md                 # Complete general knowledge (inject) — paste into any chat/agent
├── visual-advertising-engine.md  # THE 39-rule operating standard (canonical, EN)
├── design-rules.md         # Readable charter of beautiful advertising (English canonical)
├── INSTALL.md              # Setup + usage on every agent (incl. ChatGPT)
├── README.md               # Homepage / manual (PL, main)
├── README.en.md            # Homepage / manual (EN, extra)
├── CHANGELOG.md            # Version history
├── LICENSE                 # MIT
├── CONTRIBUTING.md         # How to add a rule (rule-ID policy, no-duplication rule)
├── requirements.txt        # pillow + numpy, for scripts/
├── .claude-plugin/         # plugin.json — install via a Claude Code marketplace
├── .github/workflows/ci.yml # runs check_docs.py + test_qa.py on every push
├── examples/               # Worked ad examples (food, hotel, services, retail)
├── assets/                 # Banner and generated hero images for the README
├── scripts/                # qa.py, test_qa.py (its self-test), extract_wordmark.py
└── references/
    ├── hospitality-food-services-playbook.md # Deep rules: food / hotel / services
    ├── layout-system.md        # Layout + panel-height + gradient values
    ├── headline-system.md      # Headline sizing & contrast rules
    ├── variation-matrix.md     # Test-ready sets: lock brand, rotate one axis (R35)
    ├── hook-engineering.md     # The 20→3 hook gate (R36)
    ├── creative-performance-loop.md # Publish → measure → feed the next brief (R37)
    ├── platform-compliance.md  # Safe zones + ratio re-layout per platform (R38)
    ├── video-ugc-track.md      # Video/UGC motion production (R39)
    ├── model-routing.md        # Generator + cost decision table
    ├── competitor-ad-teardown.md # Turn winning competitor ads into briefs
    ├── qa-gate.md              # QA gate & rejection criteria
    ├── anti-slop-registry.md   # Full banned-patterns compendium (visual + copy)
    ├── niche-playbooks.md      # 15 per-industry ad playbooks
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
