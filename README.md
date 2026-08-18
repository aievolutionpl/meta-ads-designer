<div align="center">

# 🎬 Meta Ads Designer

### The visual advertising engine for AI agents — design beautiful Meta / Instagram / Facebook ads, and stop generating AI-slop.

**Meta Ads · Instagram · Facebook · Posters · Flyers · Product photography · E-commerce visuals** — for restaurants, hotels, local businesses and retail.

[🇵🇱 Polski](README.pl.md) · [EN](README.md)

![Version](https://img.shields.io/badge/version-5.0.0-6a5acd)
![License](https://img.shields.io/badge/license-MIT-brightgreen)
![Format](https://img.shields.io/badge/default_format-4:5%20(1080×1350)-informational)
![Hosts](https://img.shields.io/badge/runs_on-ChatGPT%20%7C%20Codex%20%7C%20Hermes%20%7C%20Claude%20%7C%20Cursor-blue)
![Framework](https://img.shields.io/badge/framework-agnostic-success)
![PRs](https://img.shields.io/badge/PRs-welcome-2ea44f)

<br/>

> **„Don't generate objects in a void. Generate ads that look like a campaign — with hierarchy, typography, real light, and a structural message."**

> **Default format: 4:5 (1080×1350)** — the Instagram/Facebook feed default. The user can request any other ratio; 4:5 is the default.

> **`DON'T DECORATE. DIRECT.`** — One product. One idea. One strong visual.

<br/>

<img src="assets/meta-ads-designer-banner.png" alt="Meta Ads Designer — Don't Decorate. Direct." width="100%"/>

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

> *"Make a 4:5 social ad for my coffee shop. Here are my reference photos: [attach logo + drinks]. Follow the Meta Ads Designer rules — product first, real food from my photos, my logo unaltered, one headline readable from a thumbnail, no text-on-photo slop. Show me 3 structurally different concepts."*

**Option B — as a skill** (Hermes / Claude Code / Codex / Cursor):
```bash
git clone https://github.com/aievolutionpl/meta-ads-designer.git
cp -r meta-ads-designer ~/.hermes/skills/marketing/   # or ~/.claude/skills/ ~/.codex/skills/ ~/.cursor/skills/
```

**Verify it loaded** — ask the agent to *"summarize the Meta Ads Designer rules"*. It should name product-first, source of truth, commercial realism, hierarchy, negative space, anti-slop, hard fails. If it recites generic "make it premium", it didn't load — re-paste.

Full per-host steps: **[`INSTALL.md`](INSTALL.md)**.

---

## ✨ Why it works on any agent

`Meta Ads Designer` is **framework-agnostic**. The same rules travel everywhere — native skills on Hermes/Claude/Codex/Cursor, custom instructions on ChatGPT, or system-prompt injection on any agent/API.

```
┌──────────────────────────────────────────────────┐
│  visual-advertising-engine.md                    │  ← THE rules, R01–R34
│  single source of truth · stable rule IDs        │     cite them in QA
└───────┬──────────────────────────────────────────┘
        │ executed with
        ▼
┌────────────────────┬────────────────────┬────────────────────┐
│ layout-system.md   │ headline-system.md │ qa-gate.md         │
│ grid · type scale  │ archetypes         │ script + vision    │
│ palettes · layouts │ budgets · CTAs     │ + scored rubric    │
│ WHAT IT LOOKS LIKE │ WHAT IT SAYS       │ IS IT GOOD ENOUGH  │
└────────────────────┴─────────┬──────────┴────────────────────┘
                               │ demonstrated by
                               ▼
                      ┌──────────────────┐
                      │    examples/     │  ← finished briefs → prompts
                      │  no placeholders │     → QA verdicts → fixes
                      └────────┬─────────┘
                               │ loaded by
                 ┌─────────────┼─────────────┐
                 ▼             ▼             ▼
           ┌──────────┐  ┌──────────┐  ┌──────────────┐
           │ SKILL.md │  │ core.md  │  │ references/  │
           │ workflow │  │ 1-page   │  │ niche depth  │
           │          │  │ inject   │  │ + anti-slop  │
           └──────────┘  └──────────┘  └──────────────┘
```

**The split is intentional.** The rules say *what good means*; the three system files turn that into **numbers, words and a pass mark**; the examples prove it; `SKILL.md` runs it; `core.md` travels anywhere. Taste travels; procedure adapts.

---

## 🏛️ What it actually enforces

Full standard in **[`visual-advertising-engine.md`](visual-advertising-engine.md)** — 34 rules with stable IDs (`R01`–`R34`) you can cite in a QA verdict.

> **Product First · Reference = Source of Truth · One creative = One idea · Don't decorate, direct.**

**The rules** — hierarchy readable from a thumbnail · commercial realism (perspective, gravity, shadows, real materials) · lighting described by what it *does* · an explicit camera decision · depth · product in use · three mandatory angles (Problem/Effect/Lifestyle) · series consistency · anti-slop · hard-fail conditions.

**The numbers** ([`layout-system.md`](references/layout-system.md)) — 12-column grid, 86px margins, a type scale in px, named font pairings with fallbacks, starter palettes per category, three canonical layouts with exact panel heights and scrim values, contrast ≥4.5:1.

**The words** ([`headline-system.md`](references/headline-system.md)) — the specificity test, ten headline archetypes, character budgets locked to the type scale, CTAs per category in EN/PL, and a diacritics strategy that stops Polish copy from rendering as `ZOSTAN` with a missing tail.

**The pass mark** ([`qa-gate.md`](references/qa-gate.md)) — `scripts/qa.py` for what a machine measures, a structured-JSON vision prompt that transcribes rather than approves, and a 10-criteria rubric. Ship at **≥16/20 with zero hard fails**.

### The one test that removes most AI copy

> Could a direct competitor paste this headline onto their own ad without changing a word?

| ❌ | ✅ |
|---|---|
| Authentic flavours | Souvlaki off the grill |
| Your perfect escape | Sea view, four minutes from the harbour |
| Quality you can trust | 1,400 stoves fitted on this island |
| Experience the difference | Cold house Friday. Warm house Monday. |

---

## 🧠 The workflow it drives

```
1. BRIEF     — what we promote, for whom, the CTA, platforms + collect refs
2. RESEARCH  — how do top brands in this niche present themselves? If the
               client has ads they like — that IS the style source of truth
3. ANGLES    — 5-10 distinct promises/layouts, not 10 color swaps
4. CREATIVE  — product → benefit → target → angle → metaphor → type →
               composition → light/camera → constraints → then the prompt
6. MODE      — native in-render text, or deterministic composition?
               (diacritics, apostrophes, prices, logos → deterministic)
7. GENERATE  — one finished ad per generation; refs with a labelled role;
               11-part prompt with NO placeholders left
8. QA        — scripts/qa.py + vision pass + rubric; ship at >=16/20
9. DELIVER   — files + contact sheet + per-image scores + notes
```

---

## 📁 Repo structure

```
meta-ads-designer/
├── SKILL.md                        # Agent operating manual (procedure + routing)
├── visual-advertising-engine.md    # THE rules, R01–R34 — single source of truth
├── design-rules.md                 # Readable charter + index to everything
├── core.md                         # 1-page injectable — paste into any chat
├── INSTALL.md                      # Setup on every host
├── CHANGELOG.md
├── examples/                       # Finished briefs → prompts → QA verdicts
│   ├── 00-anti-examples.md         #   weak vs finished, side by side
│   ├── 01-restaurant-real-food.md  #   Mode A · real-food hero
│   ├── 02-hotel-editorial.md       #   Mode B · editorial split
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
├── scripts/
│   ├── qa.py                       # Deterministic QA layer
│   └── extract_wordmark.py         # White wordmark from a solid-colour logo
└── LICENSE
```

---

## 🧭 File map

| I want to… | Open |
|-----------|------|
| paste one page into a chat | `core.md` |
| know the rules | `visual-advertising-engine.md` |
| know how big the headline is | `references/layout-system.md` |
| know what the headline should say | `references/headline-system.md` |
| decide whether to ship it | `references/qa-gate.md` + `scripts/qa.py` |
| see a finished prompt | `examples/` |
| handle a restaurant / hotel / services brief | `references/hospitality-food-services-playbook.md` |
| install it on my agent | `INSTALL.md` |

---

## 🤝 Contributing

Have a rule that would've saved a campaign? Open a PR against `visual-advertising-engine.md` — it's the canonical source, and everything else summarizes it. New rules get the next free `R` id and never renumber an existing one. See [`CONTRIBUTING.md`](CONTRIBUTING.md).

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
