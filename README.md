<div align="center">

# 🎨 Premium Ad Design

### The universal plugin that teaches AI agents how to design beautiful ads — and stop producing AI-slop

**Postery · Flyery · Meta ads · Promo graphics** — for restaurants, hotels, local businesses and retail.

![Version](https://img.shields.io/badge/version-3.0.0-6a5acd)
![License](https://img.shields.io/badge/license-MIT-brightgreen)
![Language](https://img.shields.io/badge/lang-PL-2ea44f)
![Hosts](https://img.shields.io/badge/runs_on-Hermes%20%7C%20Claude%20%7C%20Codex%20%7C%20Cursor%20%7C%20ChatGPT-blue)
![Status](https://img.shields.io/badge/framework-agnostic-success)

<br/>

> **„Don't generate objects in a void. Generate ads that look like a campaign — with hierarchy, typography, real light, and a structural message."**

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

The result reads as *"an image from ChatGPT"* — not a professional campaign. **This plugin fixes that.**

---

## ✨ The solution — rules, not vibes

`Premium Ad Design` distills hard-won production rules into a **universal charter of beautiful advertising**. It does **not** depend on any one tool or host — the rules are the same everywhere:

- ✅ **Hermes** — native skill
- ✅ **Claude Code** — native skill
- ✅ **Codex CLI** — native skill
- ✅ **Cursor / Windsurf** — native skill
- ✅ **ChatGPT / Claude / Gemini** — paste `design-rules.md` as a custom instruction
- ✅ **Any custom agent / API** — inject the ruleset into the system prompt

---

## 🏛️ The Rules of Beautiful Advertising

The heart of the plugin is the **Visual Advertising Engine** (`visual-advertising-engine.md`) — the full 34-rule operating standard. Here are the 10 headline rules; **the complete standard is in the Engine file.**

> **Product First · Reference = Source of Truth · One creative = One idea · Don't decorate, direct.**

1. **Hierarchy** — one dominant element (the TITLE / the product), readable from a thumbnail, message in 1 second.
2. **Real typography** — name real typefaces (Playfair, Montserrat…), max 3 families, contrast by weight & scale. Never "modern sans-serif".
3. **Brand palette + one accent** — never the purple-blue default; no cream/sand "for warmth"; gradient only as a scrim.
4. **Negative space** — generous margins (~8%), breathing room; space is luxury.
5. **Imagery in context** — product in real use, real light, real people. Never floating on a void.
6. **Real food from refs** — never let AI invent dishes the venue doesn't serve.
7. **Logo fidelity** — never AI-redraw an official logo; place the original file.
8. **Ad spine** — headline → subline → CTA → brand cue. A pretty photo is not an ad.
9. **No AI copy** — banned words (delve, seamless, empower, elevate, robust, revolutionary, 🚀); names & numbers over adjectives.
10. **QA before shipping** — thumbnail readability, correct spelling (incl. Polish diacritics), one focal point, contrast, logo fidelity.

---

## ⚙️ How it works — architecture

```
                   ┌──────────────────────────────────────────┐
                   │  visual-advertising-engine.md            │  ← THE standard
                   │  "Visual Advertising Engine"             │     (34 rules: Product
                   │   34-rule operating standard             │      First, Prompt
                   └──────────────┬───────────────────────────┘      Architecture,
                                  │ summarized as               Hard Fails)
                                  ▼
                   ┌─────────────────────────────┐
                   │   design-rules.md           │  ← THE charter (paste-able)
                   │   "The Rules of Beautiful   │     Works on ANY agent
                   │    Advertising"             │
                   └──────────────┬──────────────┘
                                  │ loaded by
        ┌─────────────────────────┼─────────────────────────┐
        ▼                         ▼                         ▼
   ┌───────────┐           ┌──────────────┐          ┌──────────────┐
   │  SKILL.md │           │   INSTALL.md │          │  references/ │
   │ agent     │           │   setup per  │          │  depth:      │
   │ operating │           │   host +     │          │  prompts,    │
   │ manual    │           │   ChatGPT    │          │  niches,     │
   └───────────┘           └──────────────┘          │  anti-slop   │
                                                     └──────────────┘
```

**The split is intentional:**
- **`visual-advertising-engine.md`** — the *operating standard* (34 rules): Product First, Reference = Source of Truth, Prompt Architecture, Creative Workflow, Hard Fails, Final Quality Check. This is what an agent follows before any commercial visual.
- **`design-rules.md`** — the *charter* (the taste). Self-contained, so it can be pasted into ChatGPT or injected into any system prompt. This is what changes an agent's taste.
- **`SKILL.md`** — the *procedure* (what to DO: brief → research → angles → creative → generate → QA → deliver). Skill loaders read its frontmatter.
- **`references/`** — the *depth* (ready prompts, per-industry playbooks, full slop registry).
- **`INSTALL.md`** — the *adapters* (how each host loads it).

The result: **the taste travels**, no matter which agent runs it.

---

## 🧠 The workflow it drives

```
1. BRIEF     — what we promote, for whom, the CTA, platforms + collect refs
               (logo, venue, food, products)
2. RESEARCH  — how do top brands in this niche present themselves? If the
               client has ads they like — that IS the style source of truth
3. ANGLES    — 5-10 distinct promises/layouts, not 10 color swaps
4. GENERATE  — one finished ad per generation; refs with a clear role
5. QA        — contact sheet + checklist; scale+pad (never crop) near edges
6. DELIVER   — files + contact sheet + notes; report model/cost
```

---

## 🚀 Quick start

### Hermes / Claude / Codex / Cursor
```bash
git clone https://github.com/aievolutionpl/premium-ad-design.git
cp -r premium-ad-design ~/.hermes/skills/marketing/   # Hermes
cp -r premium-ad-design ~/.claude/skills/             # Claude Code
cp -r premium-ad-design ~/.codex/skills/              # Codex
cp -r premium-ad-design ~/.cursor/skills/             # Cursor
```

### ChatGPT / Claude / Gemini (chat)
Open **Custom Instructions** and paste the ruleset, or attach `design-rules.md` as a file. Then prompt:

> *"Make a 4:5 social ad for [business]. Here are my reference photos: [attach logo/food/venue]. Follow the Premium Ad Design rules: one headline readable from a thumbnail, brand palette, real typography, no text-on-photo slop, real food from my photos, my logo unaltered, CTA 'Reserve a table'. Show 3 structurally different concepts first."*

**Verify it loaded:** ask the agent to *"summarize the 10 rules of beautiful advertising"* — it should name hierarchy, real typography, brand palette, negative space, context imagery, logo fidelity, ad spine, banned AI words, QA.

Full per-host steps: **`INSTALL.md`**.

---

## 📁 Repo structure

```
premium-ad-design/
├── SKILL.md                        # Agent operating manual (procedure + routing)
├── visual-advertising-engine.md    # THE standard — "Visual Advertising Engine" (34 rules)
├── design-rules.md                 # THE charter — "The Rules of Beautiful Advertising"
├── INSTALL.md                      # Setup + usage on every agent (incl. ChatGPT)
├── README.md                       # This manual
├── LICENSE                         # MIT
└── references/
    ├── anti-slop-registry.md       # Full banned-pattern compendium (visual + copy)
    ├── niche-playbooks.md          # Per-industry ad playbooks (restaurant, hotel, …)
    └── prompt-library.md           # Ready-to-use prompt recipes for any model
```

---

## 🧭 File map

| File | Use it for |
|------|-----------|
| `visual-advertising-engine.md` | **The operating standard** — 34 rules agents follow before any commercial visual |
| `design-rules.md` | The charter — paste into any chat, or read as the canonical taste |
| `SKILL.md` | Agent operating manual (skill loaders read this) |
| `INSTALL.md` | Setup per host |
| `references/prompt-library.md` | Ready-to-use prompt recipes |
| `references/niche-playbooks.md` | Per-industry depth |
| `references/anti-slop-registry.md` | Full banned-pattern list + grep gate |
| `README.md` | This manual |

---

## 🎯 Why it exists — the origin

Built from **real production rejections**, not theory. Every rule maps to an actual mistake caught on a live campaign: the restaurant ad that invented dishes the kitchen never served, the hotel pack that mangled the logo, the flyer that was a Canva template with text slapped on a photo, the "premium" pack that was 10 color swaps of the same layout. These are the rules that turned those into passing campaigns.

---

## 🤝 Contributing

Have a rule that would've saved a campaign? Open a PR against `design-rules.md` — that's the canonical source; `SKILL.md` and the README summarize it.

---

## 📜 License

MIT — use it, remix it, ship it.

---

<br/>
<div align="center">
  <b>Created by</b><br/>
  <b>AI EVOLUTION LABS</b><br/>
  <sub>Channel Islands</sub><br/>
  <sub><a href="https://github.com/aievolutionpl/premium-ad-design">github.com/aievolutionpl/premium-ad-design</a></sub>
</div>
