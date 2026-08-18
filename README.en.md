<div align="center">

# 🎬 Meta Ads Designer

### The visual advertising engine for AI agents — design beautiful Meta / Instagram / Facebook ads, and stop producing AI-slop.

**Meta Ads · Instagram · Facebook · Posters · Flyers · Product photography · E-commerce visuals** — for restaurants, hotels, local businesses and retail.

[🇵🇱 Polski](README.md) · [🇬🇧 English](README.en.md)

![Version](https://img.shields.io/badge/version-5.0.0-6a5acd)
![License](https://img.shields.io/badge/license-MIT-brightgreen)
![Format](https://img.shields.io/badge/default_format-4:5%20(1080×1350)-informational)
![Hosts](https://img.shields.io/badge/runs_on-ChatGPT%20%7C%20Codex%20%7C%20Hermes%20%7C%20Claude%20%7C%20Cursor-blue)
![Framework](https://img.shields.io/badge/framework-agnostic-success)
![PRs](https://img.shields.io/badge/PRs-welcome-2ea44f)

<br/>

<img src="assets/meta-ads-designer-banner.png" alt="Meta Ads Designer" width="100%"/>

> **Default format: 4:5 (1080×1350)** — the Instagram/Facebook feed default. The user can request any other ratio; 4:5 is the default.

> **`DON'T DECORATE. DIRECT.`** — One product. One idea. One strong visual.

<br/>

</div>

---

## 🧩 The problem — why AI ads all look the same

Image models have **no taste**. Left to themselves they converge on a look anyone can spot as AI-slop:

| 🐘 What the user sees | ➡️ What the model produces |
|-----------------------|----------------------------|
| A real business, with real photos | Tiny clip-art icons, no composition |
| Their actual food / venue / product | AI-**invented** dishes, fake facades |
| Their real logo | A distorted AI-**redrawn** logo |
| A premium local restaurant | A generic purple-blue gradient + Inter font |
| A memorable offer | Text slapped on a photo (Canva template), no message |

The result reads as *"an image from ChatGPT"* — not a professional campaign. **Meta Ads Designer fixes that.**

---

## 🚀 Try it right now (no install)

**Option A — one paste.** Put the contents of **[`core.md`](core.md)** into ChatGPT / Claude / Gemini as a custom instruction, then prompt:

> *"Make a 4:5 social ad for my coffee shop. Here are my reference photos: [attach logo + drinks]. Follow the rules — product first, real food from my photos, my logo unaltered, one headline readable from a thumbnail, no text-on-photo slop. Show me 3 structurally different concepts."*

**Option B — as a skill** (Hermes / Claude Code / Codex / Cursor):
```bash
git clone https://github.com/aievolutionpl/meta-ads-designer.git
cp -r meta-ads-designer ~/.hermes/skills/marketing/   # or ~/.claude/skills/ ~/.codex/skills/ ~/.cursor/skills/
```

**Verify it loaded** — ask the agent to *"summarize the rules"*. It should name product-first, source of truth, commercial realism, hierarchy, negative space, anti-slop, hard fails. If it recites generic "make it premium", it didn't load — re-paste.

Full per-host steps: **[`INSTALL.md`](INSTALL.md)**.

---

## ⚙️ How the skill works

`Meta Ads Designer` is **framework-agnostic** — the same rules travel to any agent. It is built in **layers**, each with one job:

```
┌────────────────────────────────────────────┐
│ visual-advertising-engine.md               │  ← THE standard (34 rules)
│   Product First · Source of Truth ·        │     Prompt Architecture ·
│   Hard Fails · Final Quality Check         │     Creative Workflow
└───────────────┬────────────────────────────┘
                │ summarized as
                ▼
┌─────────────────────────────┐
│      design-rules.md       │  ← THE charter (paste-able taste)
│   "The Rules of Beautiful   │     Works on ANY agent
│    Advertising"             │
└───────────────┬─────────────┘
                │ loaded by
        ┌───────┼───────┐
        ▼       ▼       ▼
   ┌────────┐ ┌───────┐ ┌──────────────────┐
   │SKILL.md│ │core.md│ │  references/     │
   │ manual │ │inject │ │  depth:          │
   │        │ │1-page │ │  food/hotel/svc, │
   └────────┘ └───────┘ │  prompts, slop   │
                        └──────────────────┘
```

- **`visual-advertising-engine.md`** — the *standard* (34 rules). What an agent follows **before** any commercial visual: Product First, Reference = Source of Truth, Prompt Architecture, Hard Fails, QA.
- **`design-rules.md`** — the *charter* (the taste). English canonical. Self-contained, so it can be pasted into any chat or injected into any system prompt.
- **`core.md`** — the *one-page inject*. The essential rules + the weak/strong prompt example, for the fastest possible setup.
- **`SKILL.md`** — the *procedure*. Brief → research → angles → creative → generate → QA → deliver. Skill loaders read its frontmatter.
- **`references/`** — the *depth*: a battle-tested food/hotel/services playbook, per-industry niche playbooks, ready prompt recipes, and the full anti-slop registry.

### Two production modes (decide before generating)
| Mode | What it is | When |
|------|-----------|------|
| **A · Native AI text** | Copy **baked into** the AI render, in-scene. Best spelling: gpt-image-2 (Codex). Keep strings SHORT. | Restaurant/venue/food ads — the default. |
| **B · Deterministic composition** | Generate a clean background only, then compose the final ad (official logo + exact type + panels). | When text/logo fidelity matters most (services, offers). |

### The workflow it drives
```
1. BRIEF     — what, for whom, CTA, platforms (default 4:5) + collect refs
2. RESEARCH  — how do top brands in this niche present themselves?
3. ANGLES    — 5-10 distinct promises/layouts, not 10 colour swaps
4. CREATIVE  — product → benefit → target → angle → metaphor → type →
               composition → light/camera → constraints → then the prompt
5. GENERATE  — one finished ad per generation
6. QA        — contact sheet + checklist; scale+pad (never crop) near edges
7. DELIVER   — files + contact sheet + notes
```

---

## 🏛️ The rules (headlines — full standard in the Engine)

> **Product First · Reference = Source of Truth · One creative = One idea · Don't decorate, direct.**

1. **Hierarchy** — one dominant element, readable from a thumbnail, message in 1 second.
2. **Real typography** — name real typefaces, max 3 families, contrast by weight & scale.
3. **Brand palette + one accent** — never the purple-blue default.
4. **Negative space** — margins, breathing room; space is luxury.
5. **Imagery in context** — product in real use, real light, real people.
6. **Real food from refs** — never let AI invent dishes the venue doesn't serve.
7. **Logo fidelity** — never AI-redraw an official logo; place the original.
8. **Ad spine** — headline → subline → CTA → brand cue. A pretty photo is not an ad.
9. **No AI copy** — banned words; names & numbers over adjectives.
10. **QA before shipping** — thumbnail readability, correct spelling, one focal point, logo fidelity.

Plus: **Commercial realism** · **Lighting is part of the product** · **Think like a photographer** · **Build depth** · **Three mandatory angles** (Problem/Effect/Lifestyle) · **The Visual Creative Library** · **Series consistency** · **Hard Fail Conditions**.

---

## 📁 Repo structure

```
meta-ads-designer/
├── SKILL.md                        # Agent operating manual (procedure + routing)
├── core.md                         # 1-page injectable rules — paste into any chat
├── visual-advertising-engine.md    # THE standard — 34 rules
├── design-rules.md                 # The charter (English canonical)
├── INSTALL.md                      # Setup + usage on every agent (incl. ChatGPT)
├── README.md                       # This manual (PL, main)
├── README.en.md                    # This manual (EN, extra)
├── CHANGELOG.md                    # Version history
├── LICENSE                         # MIT
├── assets/meta-ads-designer-banner.png
├── examples/                       # Worked ad examples (anti, restaurant, hotel, services, retail)
├── scripts/                        # extract_wordmark.py, qa.py
└── references/
    ├── hospitality-food-services-playbook.md  # Deep rules: food / hotel / services
    ├── layout-system.md            # Layout + panel-height + gradient values
    ├── headline-system.md          # Headline sizing & contrast rules
    ├── qa-gate.md                  # QA gate & rejection criteria
    ├── anti-slop-registry.md       # Full banned-pattern compendium (visual + copy)
    ├── niche-playbooks.md          # Per-industry ad playbooks
    └── prompt-library.md           # Ready-to-use prompt recipes for any model
```

---

## 🧭 File map

| File | Use it for |
|------|-----------|
| `core.md` | The one-page inject — paste into any chat/agent |
| `visual-advertising-engine.md` | The operating standard — 34 rules |
| `design-rules.md` | The charter — the taste |
| `SKILL.md` | Agent operating manual (skill loaders read this) |
| `INSTALL.md` | Setup per host |
| `references/hospitality-food-services-playbook.md` | Deep rules for food / hotel / services |
| `references/prompt-library.md` | Ready-to-use prompt recipes |
| `references/niche-playbooks.md` | Per-industry depth |
| `references/anti-slop-registry.md` | Full banned-pattern list + grep gate |
| `README.md` | This manual (PL) |
| `README.en.md` | This manual (EN) |

---

## 🤝 Contributing

Have a rule that would've saved a campaign? Open a PR against `visual-advertising-engine.md` — it's the canonical source. See [`CONTRIBUTING.md`](CONTRIBUTING.md).

---

## 📜 License

MIT — use it, remix it, ship it.

---

<br/>
<div align="center">
  <b>Created by</b><br/>
  <b>AI EVOLUTION LABS</b><br/>
  <sub>Channel Islands</sub><br/>
  <sub><a href="https://github.com/aievolutionpl/meta-ads-designer">github.com/aievolutionpl/meta-ads-designer</a></sub>
</div>
