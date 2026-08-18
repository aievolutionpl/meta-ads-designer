# 01 · Restaurant — real food hero, native in-render text

**Mode A** · 4:5 (1080×1350) · one creative from a batch of five

---

## 1 · Brief

> "We're a Greek taverna by the seafront, family run since 2004. Midweek evenings are quiet. Can you make us some Instagram ads? I'll send photos of the souvlaki and the mezze. Make it look premium — like those fancy restaurant ads. And can the text be part of the picture, I don't want it looking stuck on."

**What the client got wrong, and how to handle it:** "premium — like those fancy restaurant ads" would push us into dark-studio fine-dining stylization, which would misrepresent a casual charcoal-grill taverna and set the wrong price expectation. Don't argue and don't silently ignore it: deliver premium **craft** (light, composition, typography) on **their** food, and say so in the handover. Authenticity outranks the aesthetic reference (R03).

**Assets:** 6 real dish photos (phone camera, decent daylight), logo as a PNG wordmark, no brand palette.
**Constraint accepted:** text baked into the render → **Mode A**, copy in English, no diacritics → safe.

---

## 2 · Creative work (R28)

| Step | Decision |
|------|----------|
| 1 · Product | charcoal-grilled pork souvlaki with flatbread — their highest-margin, most photographed plate |
| 2 · Benefit | it's actually grilled over charcoal, to order, by the same family for 20 years |
| 3 · Target | locals aged 25–50 deciding where to eat *tonight*, within ~15 minutes of the seafront |
| 4 · Angle | EFFECT — the plate as it arrives (R13) |
| 5 · Metaphor | none needed. The dish, shot honestly, is the argument. Metaphor here would be decoration (R31) |
| 6 · Creative type | HERO SHOT + real-food layout (R14 #01) |
| 7 · Headline | see §3 |
| 8 · Composition | photo-top + solid panel, 62/38 (layout-system §3a) — their photos are landscape, so a full-bleed crop would clip the plate |
| 9 · Light & camera | 45° eye level, 50mm f/2.2, late-afternoon window light from camera-left, raking (R09 food commercial) |
| 10 · Constraints | reproduce the exact dish; no text on food; no invented garnish; no people |

**Angle diversity for the batch of five (R21):** concrete dish · place · deadline (midweek offer) · proof (20 years) · sensory. Five archetypes, five layouts — not five colourways.

---

## 3 · Headline

Five drafts against the ≤22-character single-line budget:

| Draft | Archetype | Chars | Verdict |
|-------|-----------|-------|---------|
| `Authentic Greek flavours` | — | 24 | ❌ a competitor could paste it verbatim |
| `Taste the Mediterranean` | — | 23 | ❌ same, plus a banned construction |
| `Souvlaki off the grill` | CONCRETE | 22 | ✅ names the dish and the method |
| `Grilling since 2004` | PROOF | 19 | ✅ keep for creative #4 |
| `Four minutes from the sea` | PLACE | 25 | ✅ over budget for one line — keep for creative #2 at 64px/2 lines |

**Shipped:** headline `SOUVLAKI OFF THE GRILL` (2 lines, 64px) · detail line `Havre des Pas · open till 11, Tue–Sun` (37 ch) · CTA `RESERVE A TABLE` (15 ch).

The spine read aloud: *"Souvlaki off the grill. Havre des Pas, open till 11, Tuesday to Sunday. Reserve a table."* One voice, three facts, no adjectives.

---

## 4 · The prompt

```
ONE SINGLE FINISHED AD ONLY — no collage, no grid, no split-screen.
Aspect ratio 4:5, final size 1080x1350.

Reference image A = subject, source of truth: '/refs/souvlaki_plate.jpg'
Reproduce THIS exact dish: same cut and char of the pork, same number of
skewers, same flatbread, same red onion, same paprika dusting, same plate.
Do not add ingredients, garnish, microgreens, sauces or props that are not
in the reference.

OBJECTIVE: make a local scrolling at 7pm want this plate tonight.

COMPOSITION: the real dish as the hero, filling the top 62% of the frame
edge to edge. The bottom 38% is a SOLID deep navy panel (#0A1F33) with a
hard straight horizontal edge — no gradient blend, no fade, no text of any
kind on the food.

CAMERA: 45-degree angle at table eye level, 50mm, f/2.2. Focus on the front
skewer; the back of the plate falls gently out of focus. Slight foreground
blur from the table edge.

LIGHTING: late-afternoon window light from camera-left, warm and directional,
raking across the meat so char marks and glaze read as texture. One soft
shadow falling to camera-right. No frontal fill, no glow, no HDR.

MATERIALS: charred edges, glossy meat surface, blistered flatbread, matte
ceramic plate, condensation on a glass at the frame edge.

BRAND MOOD: warm, family-run, coastal, unpretentious. Not fine dining.

Native typography, on the navy panel ONLY:
- brand line, small serif, top of panel: "DE L'ETANG"
- headline, bold sans, two lines: "SOUVLAKI OFF" / "THE GRILL"
- detail line, small sans: "Havre des Pas · open till 11, Tue-Sun"
- CTA inside a thin gold rule box: "RESERVE A TABLE"

OUTPUT: Instagram/Facebook feed ad, 4:5, 1080x1350.

CONSTRAINTS: no text on the food · no words beyond those quoted above ·
no watermark · no invented dishes · no people · no cutlery that isn't in
the reference · no logo drawn by the model.
CRITICAL: every word must be spelled PERFECTLY, including the apostrophe
in "DE L'ETANG" and the hyphen in "Tue-Sun" — double-check both.
```

---

## 5 · What came back (first pass)

**Score: 13/20 — FIX.**

| Criterion | Score | Note |
|-----------|-------|------|
| Hierarchy | 2 | dish reads first, panel second |
| Product | 2 | dish reproduced accurately, char marks preserved |
| Realism | 2 | light and shadow correct |
| Typography | **1** | headline rendered at roughly 80px and `SOUVLAKI` clipped the right margin |
| Copy | **0** | brand rendered as `DE LETANG` — apostrophe dropped. Hard fail `R30-text` |
| Color | 2 | navy panel solid, gold used once |
| Space | **1** | detail line 40px from the bottom edge, inside the 8% margin |
| Logo | 2 | none drawn, as instructed — placed later |
| Thumbnail | 2 | headline readable at 150px |
| Idea | 2 | works without the copy |

The apostrophe is the classic Mode A failure — it happened on 3 of 5 renders in this batch. It is also invisible to anyone who doesn't know the brand, which is exactly why it has to be checked mechanically.

---

## 6 · The fix

1. **Brand line moved to Mode B.** The dish, headline and detail line stayed native; `DE L'ETANG` was rendered deterministically from the logo file afterwards. A brand name with punctuation is not worth five regenerations.
2. **Headline dropped to two lines at 64px** and the copy shortened, per layout-system §2b — a 22-character line at 88px was crop-risky on a 1080px canvas.
3. **Panel padding raised** to 64px bottom so the detail line cleared the safe area.
4. Re-run: `python scripts/qa.py out/ad_01.png --format 4:5 --text-box 86,843,994,1290` → PASS, and the vision pass returned `spelling_errors: []`.

**Second pass: 18/20 — ship.** (Deductions: typography 1 for a slightly tight two-line lockup; space 1 for a panel that could breathe more.)

---

## 7 · What to steal

- **Never render a brand name containing punctuation natively.** Apostrophes, ampersands, accented characters and hyphens are the highest-failure glyphs. Leave a gap and place the logo.
- **Photo-top + solid panel beats a full-bleed crop** whenever the client's photos are landscape — which is almost always, because phones shoot landscape at tables.
- **A dish name in the headline is free specificity.** `SOUVLAKI` cannot be reused by the pizza place next door; `AUTHENTIC FLAVOURS` can.
- **Vision-QA transcribes text, it doesn't confirm it.** Ask the model to *transcribe what it sees* and compare to the declared string yourself — asking "is the spelling correct?" gets a yes.
