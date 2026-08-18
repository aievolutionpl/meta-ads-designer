# 04 · Retail — reference as source of truth, a series of five

**Mode A for the hero, B for the offer creative** · 4:5 (1080×1350) · full batch of five

---

## 1 · Brief

> "We make a pull-down kitchen shelf that brings the top cabinet contents down to counter height. We've got studio photos on white. We need ads. Our last agency gave us renders that don't match the actual product."

**"Renders that don't match the product" is the whole brief.** For a mechanical product, R03 is not a style preference — a customer who orders from an ad showing a mechanism that doesn't exist will return it and leave a review saying so.

**Assets:** 4 studio packshots on white, a mechanical drawing, brand colours, logo.
**Decision:** hero and lifestyle creatives in **Mode A** (short English copy, no punctuation traps). The offer creative with price and terms in **Mode B**.

---

## 2 · Creative work (R28)

| Step | Decision |
|------|----------|
| 1 · Product | pull-down shelf unit for a wall cabinet |
| 2 · Benefit | the top shelf becomes reachable without a step stool |
| 3 · Target | two distinct groups — shorter adults in rented kitchens, and older adults staying in their homes longer |
| 4 · Angle | PROBLEM (unreachable) → EFFECT (at hand height) → LIFESTYLE (calm morning) |
| 5 · Metaphor | the step stool that isn't there any more |
| 6 · Creative type | five: #06 problem · #04 product in use · #05 macro detail · #03 lifestyle · offer |
| 7 · Headlines | see §3 |
| 8 · Composition | product occupies 45–60% of frame height in every creative; negative space above for copy |
| 9 · Light & camera | natural lifestyle (R09), 50mm at counter height, soft window key from camera-left |
| 10 · Constraints | **the mechanism.** Same arm geometry, same travel path, same number of tiers, same fixings. And the physics: the shelf needs the space it descends from |

**The physics constraint is the one agents skip.** A pull-down mechanism generated without it produces a shelf hovering below a cabinet with no visible linkage — physically impossible, and instantly noticed by anyone in the category (R30-physics).

---

## 3 · Headlines (one per creative, five archetypes)

| # | Creative | Headline | Archetype | Chars |
|---|----------|----------|-----------|-------|
| 1 | problem | `THE TOP SHELF WINS` | CONTRAST | 18 |
| 2 | product in use | `IT COMES TO YOU` | CONCRETE | 15 |
| 3 | macro detail | `NO STOOL. NO STRETCH.` | CONTRAST | 21 |
| 4 | lifestyle | `FOR ANYONE UNDER 5'6"` | AUDIENCE | 21 |
| 5 | offer | `FITS A STANDARD 600MM CABINET` | NUMBER | 29 (2 lines) |

Note creative 4: the apostrophe and inch mark in `5'6"` are exactly the glyphs that break in-render text — that creative went to Mode B for the headline. Deciding this at the headline stage, not after a failed render, saves the regeneration.

Subline for #2: `Reaches counter height in one pull` (33 ch). CTA across the set: `SEE IT WORK` (11 ch) — one action, matching the one idea.

---

## 4 · The prompt (creative #2, product in use)

```
ONE SINGLE FINISHED AD ONLY — no collage, no grid, no split-screen.
Aspect ratio 4:5, final size 1080x1350.

Reference image A = subject, source of truth: '/refs/packshot_front.jpg'
Reference image B = mechanism reference, source of truth: '/refs/drawing.png'
The product must be identical to reference A in shape, proportions, colour,
finish, number of tiers, rail profile, arm geometry and fixings. The descent
path must match reference B: the unit slides down and forward on twin arms
from inside the cabinet carcass. The cabinet above must have the internal
space the unit descends from — do not generate a mechanism that could not fit.

OBJECTIVE: show, in one frame, that the top shelf now comes to hand height.

SUBJECT: the pull-down shelf, half-descended, loaded with everyday jars and
a bag of flour — real kitchen contents, not styled props.

ACTION: one adult hand on the rail, mid-pull, natural grip, relaxed fingers.
No face in frame.

ENVIRONMENT: a real, lived-in contemporary kitchen. Wooden worktop with a
board and a mug on it. Not a showroom.

COMPOSITION: the unit occupies the centre-left, filling about 55% of the frame
height, sharper than everything around it. Clean negative space across the top
25% of the frame for the headline. Foreground: the worktop edge, softly blurred.

CAMERA: counter height, eye level with the descending shelf, 50mm, f/2.5.
Product sharp, cabinet doors and background falling gently out of focus.

LIGHTING: natural lifestyle — large soft window light from camera-left,
realistic ambient bounce off the worktop, one soft shadow to camera-right.
No studio rim light, no glow.

MATERIALS: powder-coated metal reading as metal, oak worktop reading as oak,
glass jars with genuine refraction.

BRAND MOOD: practical, calm, domestic. Not premium-luxury.

Native typography, in the clean upper area ONLY:
- headline, bold sans, one line: "IT COMES TO YOU"
- subline, small sans: "Reaches counter height in one pull"
- CTA, small caps: "SEE IT WORK"

OUTPUT: Meta feed ad, 4:5, 1080x1350.

CONSTRAINTS: product identical to reference A · mechanism identical to
reference B · no extra tiers · no invented brackets · no text on the product ·
no words beyond those quoted · no deformed hands · no watermark.
CRITICAL: every word must be spelled PERFECTLY.
```

---

## 5 · What came back (first pass)

**Creative #2 — score 12/20, FIX.**

| Criterion | Score | Note |
|-----------|-------|------|
| Hierarchy | 2 | product is unambiguously first |
| Product | **1** | correct silhouette, but the model added a third tier |
| Realism | 2 | kitchen reads as real, light correct |
| Typography | **1** | headline rendered over a bright window reflection, contrast 3.1:1 |
| Copy | 2 | spelled correctly, within budget |
| Color | 2 | brand colour on the CTA only |
| Space | 2 | upper 25% held clean as instructed |
| Logo | **0** | the model added a small invented wordmark to the rail — `R30-logo`, hard fail |
| Thumbnail | 1 | headline legible, subline gone |
| Idea | **1** | the *action* reads, but the benefit needs the headline to land |

**Batch-level finding:** across the five creatives the product appeared with three different tier counts. That's an R20 failure — a series where the product changes is not a campaign, it's five unrelated images.

---

## 6 · The fix

1. **Tier count and branding pinned explicitly:** `exactly two tiers` and `no lettering, badge or logo anywhere on the product — the rails are bare metal`. The invented wordmark is the model filling an empty surface; telling it the surface is bare is what stops it.
2. **Headline moved off the window reflection** — repositioned to the upper-left quadrant where the cabinet door gives a flat mid-tone, contrast to 7.4:1. Alternative, when nothing on the plate is flat enough: switch that creative to Mode B.
3. **Series locked to one render of the product.** The approved creative #2 output became reference A for creatives #3–#5, so the mechanism stopped drifting (R20).
4. Creative #4's `5'6"` headline composed deterministically as planned.

**Second pass: 17, 18, 16, 18, 19 — all five ship.** Archetypes used: contrast, concrete, contrast, audience, number — one repeat, acceptable across five.

---

## 7 · What to steal

- **A mechanism needs two references:** the packshot for appearance and the drawing for how it moves. One reference gives you a plausible-looking impossible product.
- **Pin the countable things.** `exactly two tiers`, `four fixings`, `three storeys` — models drift on counts more than on shapes.
- **Empty product surfaces attract invented branding.** Say the surface is bare.
- **Promote your best output to reference.** Once one creative is approved, feed it as the source of truth for the rest of the series. This is the cheapest fix for series consistency there is.
- **Decide the mode from the glyphs**, at the headline stage. `5'6"` was never going to survive a native render, and knowing that before generating saved five attempts.
