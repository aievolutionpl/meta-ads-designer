# ✨ The Rules of Beautiful Advertising

> **The readable charter of the Meta Ads Designer plugin — and the index to everything else.**
> Framework-agnostic. Read this once, and every agent — Hermes, Claude Code, Codex, ChatGPT, Cursor — will stop producing AI-slop and start producing campaigns.

**Why this exists.** Image models have no taste. Left to themselves they converge on the same boring, unconvincing look: tiny clip-art icons, generic purple-blue gradients, default fonts, text slapped onto photos like a Canva template, invented dishes the restaurant never served, logos mangled by a redraw. This charter is the antidote.

**This file does not restate the rules.** The rules live in one place — [`visual-advertising-engine.md`](visual-advertising-engine.md), as stable IDs `R01`–`R34`. This charter explains the doctrine and tells you which file to open next.

**How to use it.**
- **As an agent skill** → load [`SKILL.md`](SKILL.md) (it routes from here).
- **As a paste-into-any-chat** → paste [`core.md`](core.md) as a custom instruction. It's the complete general-knowledge inject.
- **As a checklist** → run [`references/qa-gate.md`](references/qa-gate.md) on every output before you ship it.

---

## 0 · The one-line law

> **A great ad reads in one second, from a thumbnail, and looks like it was art-directed by a human.** If it could be mistaken for a Canva template or "an image from ChatGPT" — it's slop.

> **DON'T DECORATE. DIRECT.** One product. One idea. One strong visual.

---

## 1 · The map — which file answers which question

| Your question | Open |
|---------------|------|
| What are the rules? | [`visual-advertising-engine.md`](visual-advertising-engine.md) — R01–R34, authoritative |
| I need one page to paste into a chat | [`core.md`](core.md) |
| How big is the headline? What grid? What colors? | [`references/layout-system.md`](references/layout-system.md) |
| What should the headline actually *say*? | [`references/headline-system.md`](references/headline-system.md) |
| Is this output good enough to ship? | [`references/qa-gate.md`](references/qa-gate.md) |
| What does a finished prompt look like? | [`examples/`](examples/) — full briefs → prompts → verdicts |
| Restaurant / hotel / services brief | [`references/hospitality-food-services-playbook.md`](references/hospitality-food-services-playbook.md) |
| Other industries | [`references/niche-playbooks.md`](references/niche-playbooks.md) |
| Ready-made prompt skeletons | [`references/prompt-library.md`](references/prompt-library.md) |
| What exactly counts as "AI look"? | [`references/anti-slop-registry.md`](references/anti-slop-registry.md) |
| How do I install this on my agent? | [`INSTALL.md`](INSTALL.md) |

---

## 2 · The doctrine in seven sentences

1. **Product first** (R02) — the product is the main character, not the set.
2. **The reference is a technical document** (R03) — never redraw what the client sent you.
3. **Commercial realism** (R04) — real light, real gravity, real materials. Not "obvious AI ad".
4. **One creative = one idea** (R06) — one message, one focal point.
5. **Negative space is luxury** (R08) — a good ad has fewer elements than a weak one.
6. **Message first, scene second** (R24) — decide what the ad says, then build the picture that says it.
7. **A pretty photo is not an ad** (R17) — headline → subline → CTA → brand cue, or it's wallpaper.

---

## 3 · What "designed by a human" actually means

Three things separate an art-directed ad from a generated picture. Each has its own spec file, because each is a matter of **numbers**, not adjectives:

**Composition** — an 8% safe margin, a real grid, a panel at a defined height, one focal point at a defined size. "Generous margins" is not a spec; `86px on 1080` is. → [`layout-system.md`](references/layout-system.md)

**Typography** — a named typeface with a named weight at a named pixel size, paired deliberately, tracked correctly. "Modern sans-serif" is how you get Inter and a Canva look. → [`layout-system.md`](references/layout-system.md) §2

**Words** — a headline that only *this* business could have written. "AUTHENTIC FLAVOURS" is what the model reaches for when you don't decide. → [`headline-system.md`](references/headline-system.md)

Everything else — light, lens, depth, angle — is R09–R13 in the engine.

---

## 4 · The two production modes

Decide **before** you generate (full spec: [`layout-system.md`](references/layout-system.md) §5):

| Mode | What it is | When |
|------|-----------|------|
| **A · Native in-render text** | Copy baked into the AI render, in-scene, end-to-end. Keep strings SHORT (brand + headline + one location line); quote every rendered word; append the spelling directive. | The user wants a fully-generated visual, the model spells reliably, and the copy is short and Latin-script. |
| **B · Deterministic composition** | Generate a clean background only (`no text, no logo, no signage, no collage`), then compose the ad in code/Figma: official logo file, exact copy, brand panels, safe margins. | Logo fidelity or exact copy matters; long copy; Polish diacritics; legal/price lines; anything that must be pixel-correct. |

**Both can coexist in one batch** (e.g. 5 native + 5 deterministic). Deliver a combined contact sheet. QA text spelling either way.

---

## 5 · Copy — the words inside the ad

- **Open with force** — a wrong belief, a strong claim, a concrete example.
- **Take a real position.** If you can invert it, it has no stance.
- **Use names and numbers** — "54 KB" not "lightweight", "London Eye 5 min walk" not "great location".
- **Lead with verbs. Active voice.**
- **Vary sentence length** — uniform rhythm is the deepest AI tell.
- **No em dashes** — use commas, colons, semicolons.

**The specificity test:** could a competitor paste this headline onto their own ad without changing a word? If yes, it's slop. Archetypes, character budgets and the Polish-diacritics strategy: [`references/headline-system.md`](references/headline-system.md).

### Banned AI words (never in an ad)
`delve · seamless · empower · elevate · robust · tapestry · revolutionary · game-changer · "in today's world" · "let's dive in" · "in summary" · 🚀 on a headline · "Powered by AI" · fake company logos · "Join the waitlist" on a fake product`

---

## 6 · Quick slop check (before ANY output)

If any of these is present, fix it:

purple/blue default gradient · glassmorphism · neon glow · gradient text · tiny clip-art icons · text slapped on a photo · cream/sand bg · over-round cards · cards-in-cards · icons > content · gray-on-tinted text · isometric default · AI-invented food · AI-redrawn logo · a pretty photo with no ad structure.

Full compendium with fixes: [`references/anti-slop-registry.md`](references/anti-slop-registry.md).

---

## 7 · The workflow

```
1. BRIEF     — what are we promoting, for whom, what CTA, which platforms,
               and collect the refs (logo, venue, food, products).
2. RESEARCH  — how do the top brands in this niche present themselves?
               (Meta Ad Library, Instagram, competitors). If the client has
               existing ads they like — THAT is the style source of truth.
3. ANGLES    — define 5–10 distinct promises/layouts, not 10 color swaps.
4. CREATIVE  — product → benefit → target → angle → metaphor → type →
               headline → composition → light/camera → constraints  (R28)
5. GENERATE  — one finished ad per generation. Use refs with a clear role.
               A model must never make a batch/collage in one image.
6. QA        — score every output against references/qa-gate.md; fix or redo.
7. DELIVER   — package files + contact sheet + notes. Report the model/cost.
```

---

## 8 · The QA gate

Every output is scored: **10 criteria × 0/1/2, ship at ≥16/20 with zero hard fails.** The gate includes a copy-paste vision-QA prompt that returns structured JSON, plus `scripts/qa.py` for the things a machine can measure (dimensions, safe area, contrast, collage detection, thumbnail legibility).

→ [`references/qa-gate.md`](references/qa-gate.md)

---

## 9 · Platform dimensions (quick reference)

| Platform | Aspect | Resolution |
|----------|--------|-----------|
| Instagram Feed | 4:5 | 1080×1350 |
| Instagram Story / Reels / TikTok | 9:16 | 1080×1920 |
| Instagram Square / Facebook | 1:1 | 1080×1080 |
| Facebook / LinkedIn / YouTube | 16:9 | 1920×1080 |
| Pinterest | 2:3 | 1000×1500 |
| Banner | 4:1 | 2048×512 |

> **DEFAULT: 4:5 (1080×1350)** — the Instagram/Facebook feed default. Use 4:5 unless the user explicitly asks for another ratio. Compose for the specific format.

**Rule:** when text or logos live near the edge, resize with **scale+pad**, never a hard crop. Safe areas per format: [`layout-system.md`](references/layout-system.md) §1.

---

*This charter is part of the **Meta Ads Designer** plugin. Rules: `visual-advertising-engine.md`. Agent workflow: `SKILL.md`. Install: `INSTALL.md`.*
