<div align="center">

# 🎬 Meta Ads Designer

### The universal advertising standard for AI agents — design beautiful Meta / Instagram / Facebook ads and stop generating AI-slop.

**Meta Ads · Instagram · Facebook · Posters · Flyers · Product photography · E-commerce visuals** — for restaurants, hotels, local businesses and retail.

[🇵🇱 Polski](README.md) · [🇬🇧 English](README.en.md)

![Version](https://img.shields.io/badge/version-5.6.0-6a5acd)
![License](https://img.shields.io/badge/license-MIT-brightgreen)
![Format](https://img.shields.io/badge/default_format-4:5%20(1080×1350)-informational)
![Hosts](https://img.shields.io/badge/runs_on-ChatGPT%20%7C%20Codex%20%7C%20Hermes%20%7C%20Claude%20%7C%20Cursor-blue)
![Framework](https://img.shields.io/badge/framework-agnostic-success)
![PRs](https://img.shields.io/badge/PRs-welcome-2ea44f)

<br/>

<img src="assets/meta-ads-designer-banner.png" alt="Meta Ads Designer" width="100%"/>

> **Default format: 4:5 (1080×1350)** — Instagram/Facebook feed. The user can ask for another ratio; 4:5 is the default.

> **`DON'T DECORATE. DIRECT.`** — One product. One idea. One strong visual.

<br/>

</div>

---

## 🧩 Problem — why AI ads all look the same

Image models **have no taste**. Left to themselves they collapse into a single "AI look" — and that look is **always identical**, whether you're doing an ad for a restaurant, a hotel or a repair service. Here's what a "naked" model really produces when it isn't given rules:

| 🐘 What a "naked" model does | ➡️ How it shows up in practice |
|------------------------------|--------------------------------|
| **Weak typography** | Unnamed "rendered" fonts instead of chosen ones; typos and gibberish instead of words; Inter as the default everywhere. |
| **Every image the same** | The same purple-blue gradient, same poses, same faces — a pizzeria ad and a law-firm ad look identical. |
| **Tiny clip-art icons** | Always badly placed, pixelated, styleless — they ruin every generation. |
| **Too much text** | Paragraphs slapped onto a photo, unreadable on a phone; nothing is a message. |
| **Everything smells of AI-slop** | Neon glow, fake UIs, holograms, generic gradients — "an image from ChatGPT", not a campaign. |
| **Alters your reference photos** | People's faces, interiors and facades no longer match reality — the client doesn't recognize their own business. |
| **Makes things up / hallucinates** | A dish that isn't on the menu; an "AI-redrawn" logo; fictional signs and price tags that don't exist. |
| **No hierarchy** | From a phone thumbnail you can't see the product or the CTA — the ad dies in the feed. |

**The result reads as "an image from ChatGPT" — not as a professional campaign.**

### ✅ What Meta Ads Designer changes

The skill **replaces that lack of taste with operational rules** — the way an art director, a commercial photographer and a media buyer would if you hired them for one campaign:

- **The product is the hero** — recognizable in ~1s, well-lit, in the foreground.
- **Your photos are the Source of Truth** — the skill **won't let you** alter faces, interiors, dishes or logos. It uses them, doesn't rework them.
- **Real typography** — named fonts, max 3 families, contrast by weight and scale; zero typos.
- **One idea per creative** — the message is readable from a phone thumbnail.
- **Team-level quality** — product, source, commercial realism, hierarchy, anti-slop, QA before delivery.

---

## 🚀 Try it now (no install)

**Option A — one paste.** Paste the contents of **[`core.md`](core.md)** into ChatGPT / Claude / Gemini as a custom instruction, then type:

> *"Make a 4:5 social ad for my coffee shop. Here are my reference photos: [logo + drinks]. Follow the rules — product in the foreground, real food from my photos, my logo unchanged, one headline readable from a thumbnail, zero text-on-photo slop. Show 3 structurally different concepts."*

**Option B — as a skill** (Hermes / Claude Code / Codex / Cursor):
```bash
git clone https://github.com/aievolutionpl/meta-ads-designer.git
cp -r meta-ads-designer ~/.hermes/skills/marketing/   # or ~/.claude/skills/ ~/.codex/skills/ ~/.cursor/skills/
```

**Verify** — ask the agent: *"summarize the rules"*. It should name product-first, source of truth, commercial realism, hierarchy, negative space, anti-slop, hard fails. If it recites generic "make it premium" — it didn't load; paste again.

Full per-host steps: **[`INSTALL.md`](INSTALL.md)**.

---

## ⚙️ How the skill works

`Meta Ads Designer` is **framework-agnostic** — the same rules work on any agent (ChatGPT, Claude, Codex, Hermes, Cursor, any API). It is built **in layers** — each layer has one job and one way in:

```
┌────────────────────────────────────────────┐
│ visual-advertising-engine.md               │  ← THE standard (39 rules)
│   Product First · Source of Truth ·        │     Prompt Architecture ·
│   Hard Fails · Final Quality Check         │     Creative Workflow
└───────────────┬────────────────────────────┘
                │ summarized as
                ▼
┌─────────────────────────────┐
│      design-rules.md       │  ← THE charter (pasteable taste)
│   "The Rules of Beautiful   │     Works on ANY agent
│    Advertising"             │
└───────────────┬─────────────┘
                │ loaded by
        ┌───────┼───────┐
        ▼       ▼       ▼
   ┌────────┐ ┌───────┐ ┌──────────────────┐
   │SKILL.md│ │core.md│ │  references/     │
   │ manual │ │paste  │ │  depth:          │
   │        │ │1 page │ │  food/hotel/svc, │
   └────────┘ └───────┘ │  prompts, slop   │
                        └──────────────────┘
```

- **`visual-advertising-engine.md`** — *standard* (39 rules). What the agent applies **before** every commercial visual: Product First, Reference = Source of Truth, Prompt Architecture, Hard Fails, QA, Variation Matrix, Hook First, Performance Loop, Compliance, Video Track. **This is the canonical source** — new rules land here first.
- **`design-rules.md`** — *charter* (taste). English canonical. Self-contained — paste into any chat or inject into the system prompt.
- **`core.md`** — *complete general knowledge (inject)*. Per-platform formats, creative process, composition, typography, colour, light, layouts, copy, niches, production modes, prompt architecture, anti-slop, hard fails, QA — self-contained, paste into any chat.
- **`SKILL.md`** — *procedure* (agent manual). Brief → research → angles → creative → generate → QA → deliver. The skill loader reads the frontmatter.
- **`references/`** — *depth*: the battle-tested food/hotel/services playbook, layout system, headline system, variation matrix, hook engineering, performance loop, platform compliance, video/UGC track, model routing, competitor teardown, QA gate, ready prompts, the full anti-slop registry.

### Two production modes (decide before generating)
| Mode | What it is | When |
|------|-----------|------|
| **A · Native AI text** | Text **baked into** the AI render, in-scene. Best spelling: gpt-image-2 (Codex). Short strings. | Restaurant/venue/food — default. |
| **B · Deterministic composition** | Generate a clean background, then assemble the ad (official logo + exact typography + panels). | When text/logo fidelity matters (services, offers). |

### Workflow
```
1. BRIEF     — what, for whom, CTA, platforms (default 4:5) + gather refs
2. RESEARCH  — how do top brands in the niche present themselves?
3. ANGLES    — 5-10 different promises/layouts, not 10 color swaps
4. CREATIVE  — product → benefit → target → angle → metaphor → type →
               composition → light/camera → constraints → then the prompt
5. GENERATE  — one finished ad per generation
6. QA        — contact sheet + checklist; scale+pad (never crop) at edges
7. DELIVER   — files + contact sheet + notes
```

---

## 🧭 Agent instructions (you got this repo? read this)

This repo is a **skill for agents** — it's received either by a human (to paste a rule) or by an agent itself (to take action). If you're an agent about to **generate ads**, here's how to navigate — from zero to finished files:

**1. Enter the flow in this order (don't skip):**
```text
core.md  →  SKILL.md  →  (details)  →  references/
 (1 min)     (full          rules       (depth only
             procedure)     standard    when the brief fits)
```

**2. The "Source of Truth" rule applies to you too:** the client's photos are a technical document. **You do not alter** faces, interiors, dishes, logos, proportions or signs. You may change light, framing, perspective, set design, mood.

**3. Before generating anything, answer 4 questions:**
- **Format?** Default **4:5 (1080×1350)** — unless the user explicitly asks for another (9:16 Reels, 1:1 marketplace, 16:9).
- **Refs?** Have I gathered all the client's reference photos (product, venue, dishes, logo)? → paste them, don't describe them.
- **Mode?** A (native AI text in-scene) or B (deterministic composition — clean background + assembly in code)? Decide per the table above.
- **Routing?** Which part of the repo does this brief touch:

| Brief | Read |
|-------|------|
| Restaurant / food / venue | `references/hospitality-food-services-playbook.md` + `layout-system.md` §3 |
| Hotel / venue / property | `references/hospitality-food-services-playbook.md` (real-photo + deterministic typography) |
| Service / trade | `references/hospitality-food-services-playbook.md` (services) + mode B (fidelity) |
| Retail / product | `examples/04-retail-product-in-use.md` + `layout-system.md` |
| Specific niche | `references/niche-playbooks.md` |
| Not sure / something new | `design-rules.md` + `visual-advertising-engine.md` |

**4. Write the prompt like a commercial photographer** — product → benefit → audience → angle → metaphor → type → composition → light/camera → constraints. **Banned words** and anti-slop patterns: `references/anti-slop-registry.md`.

**5. QA before delivery** — `references/qa-gate.md`: thumbnail readability, correct spelling, one focal point, logo fidelity, zero invented dishes/facades. **Not sure it passes QA?** Don't deliver it.

**6. Deliver** — files + contact sheet + short notes on what and why. Show quality, not quantity.

---

## 🏛️ Rules (short — full standard in the Engine)

> **Product First · Reference = Source of Truth · One creative = One idea · Don't decorate, direct.**

1. **Hierarchy** — one dominant element, readable from a thumbnail, message in 1s.
2. **Real typography** — named fonts, max 3 families, contrast by weight and scale; **never** rendered gibberish instead of words.
3. **Brand palette + one accent** — never the purple-blue default.
4. **Negative space** — margins, breathing room; space = luxury.
5. **Imagery in context** — product in real use, real light, real people.
6. **Real food from refs** — never let AI invent dishes the venue doesn't serve.
7. **Logo fidelity** — never AI-redraw an official logo; insert the original.
8. **Ad spine** — headline → subline → CTA → brand cue. A pretty photo ≠ an ad.
9. **Zero AI-copy** — banned words; names and numbers instead of adjectives.
10. **QA before delivery** — thumbnail readability, correct spelling, one focal point, logo fidelity.

**More rules that make the difference:**
- **Commercial realism** — metal looks like metal, gravity works, shadows are. Photography, not "generic 3D".
- **Lighting is part of the product** — light is an element of the ad, not an accident.
- **Think like a photographer** — framing, depth, angle instead of "generate a logo on a gradient".
- **Build depth** — foreground / midground / background; the scene lives.
- **Three mandatory angles** — Problem → Effect → Lifestyle (for products and services).
- **Visual Creative Library** — collect proven compositions; don't start from zero every time.
- **Series consistency** — ads in one campaign are one family, not 10 one-offs.
- **Hard Fail Conditions** — concrete things that disqualify work: misspelled text, fake logos, invented dishes, text unreadable from a thumbnail.

---

## 📁 Repository structure

```
meta-ads-designer/
├── SKILL.md                        # Agent manual (procedure + routing)
├── core.md                         # Complete general knowledge (inject) — paste into any chat
├── visual-advertising-engine.md    # THE standard — 39 rules
├── design-rules.md                 # The charter (English canonical)
├── INSTALL.md                      # Setup + usage on every agent (incl. ChatGPT)
├── README.md                       # This manual (PL, main)
├── README.en.md                    # This manual (EN, extra)
├── CHANGELOG.md                    # Version history
├── LICENSE                         # MIT
├── CONTRIBUTING.md                 # How to add a rule (rule-ID policy, no-duplication rule)
├── requirements.txt                # pillow + numpy — dependencies for scripts/
├── .claude-plugin/plugin.json      # Plugin manifest (install via a Claude Code marketplace)
├── .github/workflows/ci.yml        # CI: check_docs.py + test_qa.py on every push
├── assets/meta-ads-designer-banner.png
├── examples/                       # Worked ad examples (anti, restaurant, hotel, services, retail)
├── scripts/                        # qa.py, test_qa.py, check_docs.py, extract_wordmark.py
└── references/
    ├── hospitality-food-services-playbook.md  # Depth: food / hotel / services
    ├── layout-system.md            # Layout + panel-heights + gradient values
    ├── headline-system.md          # Headline sizes and contrast
    ├── variation-matrix.md         # Test-ready sets: lock brand, rotate one axis (R35)
    ├── hook-engineering.md         # The 20→3 hook gate (R36)
    ├── creative-performance-loop.md # Publish → measure → feed the next brief (R37)
    ├── platform-compliance.md      # Safe zones + ratio re-layout per platform (R38)
    ├── video-ugc-track.md          # Video/UGC motion production (R39)
    ├── model-routing.md            # Generator + cost (decide before spend)
    ├── competitor-ad-teardown.md   # Winning competitor ads → briefs
    ├── qa-gate.md                  # QA gate and rejection criteria
    ├── anti-slop-registry.md       # Full banned-pattern compendium (visual + copy)
    ├── niche-playbooks.md          # 15 niche playbooks (food, hotel, fitness, beauty, real estate, tech…)
    └── prompt-library.md           # Ready prompts for any model
```

---

## 🧭 File map

| File | Purpose |
|------|---------|
| `core.md` | Complete general knowledge — paste into any chat/agent |
| `visual-advertising-engine.md` | Operating standard — 39 rules (canonical source) |
| `design-rules.md` | Charter — taste |
| `SKILL.md` | Agent manual (read by skill loaders) |
| `INSTALL.md` | Setup per host |
| `references/hospitality-food-services-playbook.md` | Deep rules for food / hotel / services |
| `references/layout-system.md` | Layout + panels + gradients |
| `references/headline-system.md` | Headline sizes and contrast |
| `references/variation-matrix.md` | Test-ready sets: lock brand, rotate one axis (R35) |
| `references/hook-engineering.md` | The 20→3 hook gate (R36) |
| `references/creative-performance-loop.md` | Publish → measure → feed the next brief (R37) |
| `references/platform-compliance.md` | Safe zones + ratio re-layout per platform (R38) |
| `references/video-ugc-track.md` | Video/UGC motion production (R39) |
| `references/model-routing.md` | Generator + cost (decide before spend) |
| `references/competitor-ad-teardown.md` | Winning competitor ads → briefs |
| `references/qa-gate.md` | QA gate and rejection criteria |
| `references/anti-slop-registry.md` | Banned-pattern list + grep gate |
| `references/niche-playbooks.md` | 15 industry playbooks (What works / Avoid / Headline / CTA) |
| `references/prompt-library.md` | Ready prompts |
| `README.md` | This manual (PL) |
| `README.en.md` | This manual (EN) |

---

## 🤝 Contributing

Have a rule that would save a campaign? Open a PR to `visual-advertising-engine.md` — it's the canonical source. See [`CONTRIBUTING.md`](CONTRIBUTING.md).

---

## 📜 License

MIT — use, remix, publish.

---

<br/>
<div align="center">
  <b>Created by</b><br/>
  <b>AI EVOLUTION LABS</b><br/>
  <sub>Channel Islands</sub><br/>
  <sub><a href="https://github.com/aievolutionpl/meta-ads-designer">github.com/aievolutionpl/meta-ads-designer</a></sub>
</div>

---

## 🌐 Web

- [aievolutionlabs.io](http://aievolutionlabs.io/)
- [aievolutionpolska.pl](https://www.aievolutionpolska.pl/)
