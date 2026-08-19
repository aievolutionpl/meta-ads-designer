# 03 · Services — Problem → Effect, with a real deadline

**Mode B** · 4:5 (1080×1350) · two creatives shown (the pair that tests the angle)

---

## 1 · Brief

> "We fit wood burning stoves. Autumn is our season — if people don't book by end of October they won't get fitted before Christmas. Last year we ran ads that just showed a stove and they did nothing. Photos attached, they're from real installs."

**Diagnosis before design:** "a stove and it did nothing" is a product-photo problem, not a stove problem. A stove on its own sells to people already shopping for stoves. The transformation — cold house to warm house, and the deadline that forces the decision — sells to people who haven't started yet, which is where the volume is.

**Assets:** 30 install photos (varying quality, some phone-shot in poor light), logo, real phone number, a genuine cut-off date.
**Decision:** **Mode B**. Long copy, a price claim, a phone number, and a logo — none of which may be approximate.

---

## 2 · Creative work (R28)

| Step | Decision |
|------|----------|
| 1 · Product | stove supply + installation, fitted before winter |
| 2 · Benefit | the house is warm and the bill drops, and it happens *this* season |
| 3 · Target | homeowners 35–65 in older, poorly-insulated housing stock |
| 4 · Angle | PROBLEM → EFFECT as a pair of creatives (R13, R22) |
| 5 · Metaphor | temperature as time: the same room, two Fridays apart |
| 6 · Creative type | #06 PROBLEM/SOLUTION and #07 RESULT |
| 7 · Headline | see §3 |
| 8 · Composition | full-bleed + scrim (layout-system §3b) — the install photos have their own negative space in the upper half |
| 9 · Light & camera | Problem: flat grey daylight, 35mm, cool grade. Effect: firelight as the only warm source at dusk. **The light does the argument.** |
| 10 · Constraints | stove identical to the reference; no fire outside the firebox; no invented flue routing |

**Why a pair, not a split-screen:** before/after in one frame halves the size of both halves and fails the thumbnail test (R33). Two creatives in one campaign, sequenced by the ad platform, keep both images full-size and let you measure which half of the argument does the work.

---

## 3 · Headline

| Draft | Archetype | Chars | Verdict |
|-------|-----------|-------|---------|
| `Stay warm this winter` | — | 21 | ❌ every heating company in the country |
| `Premium stove installation` | — | 26 | ❌ describes the seller, not the buyer |
| `Cold house Friday. Warm house Monday.` | CONTRAST | 37 | ✅ shipped on the Effect creative |
| `Book by 31 October or wait till spring` | DEADLINE | 38 | ✅ shipped on the Problem creative |
| `1,400 stoves fitted on this island` | PROOF | 34 | ✅ held for creative #3 |

**Effect creative:** headline `COLD HOUSE FRIDAY.` / `WARM HOUSE MONDAY.` (2×18, 64px) · subline `Fitted in a day. Survey is free.` (32 ch) · CTA `BOOK A SURVEY` (13 ch).

**Problem creative:** headline `BOOK BY 31 OCTOBER` / `OR WAIT TILL SPRING` (2×18, 64px) · subline `Last fitting slots before Christmas` (35 ch) · CTA `CALL 01534 000000` (17 ch).

The deadline is real. **Never invent urgency** — an invented cut-off is a lie the client has to live with, and it's the fastest way to lose a local reputation.

---

## 4 · The prompts

### 4a · Effect creative — background

```
ONE SINGLE PHOTOGRAPHIC BACKGROUND ONLY — no text, no words, no signage,
no logos, no numbers, no collage. Aspect 4:5, 1080x1350.

Reference image A = subject, source of truth: '/refs/install_0412.jpg'
Keep the stove identical: same body proportions, same door and hinge, same
glass shape, same handle, same flue diameter and vertical routing into the
chimney breast. Change only the room, the light and the styling.

OBJECTIVE: show what the house feels like once it's in.

SCENE: a granite-walled living room at dusk in late October. The stove is
lit and burning on a slate hearth against the chimney breast.

COMPOSITION: stove in the lower-left third, hearth line leading to camera-
right, a wool throw over a chair arm entering the frame in soft foreground
blur. Keep the upper 45% calm and low-contrast — typography goes there.

CAMERA: eye level from a seated position, 35mm, f/2.8. Stove sharp, room
falling away gently. Foreground → subject → background.

LIGHTING: the firebox is the only warm source, spilling low across the slate
and up the granite. Cool blue dusk from a window out of frame camera-right.
Realistic falloff, physically correct shadow direction. No glow bloom, no
orange haze, no lens flare, no HDR.

MATERIALS: cast iron matte texture, slate with visible grain, wool fibre,
firebox glass with a genuine reflection of the room.

BRAND MOOD: solid, local, unfussy. Warmth as relief, not as luxury.

CONSTRAINTS: stove identical to the reference in shape, proportions, door,
glass, handle, flue · no fire outside the firebox · no people · no text of
any kind anywhere in the image.
```

### 4b · Problem creative — background

Same prompt with three changes, and **only** three — this is R20 series consistency in practice:

```
SCENE: the same granite-walled living room, mid-morning, the stove not yet
installed. Bare chimney breast, hearth empty, a portable electric heater on
the floor with its cable running across the slate.

LIGHTING: flat grey daylight from the window camera-right. No warm source
anywhere in the frame. Cool, slightly desaturated grade. Honest, not styled.

CONSTRAINTS: ... no stove in this image · the room must be recognisably the
same room as the reference plate · no people · no text.
```

### 4c · Composition (deterministic, both creatives)

```
canvas      1080x1350
scrim       bottom gradient, 0 → 255 alpha, top of gradient at y=630,
            fully opaque by y=1100, colour #12232E
headline    64px Oswald 600, #FFFFFF, drop shadow 3px / alpha 200, y=1080
subline     34px Source Sans 3 400, #FFFFFF at 85%, y=1180
cta         28px Source Sans 3 600, +6% tracking, on #F2A03D fill, y=1240
logo        official file, 56px tall, bottom-right inside the 86px margin
margins     86px all sides
```

---

## 5 · What came back (first pass)

**Effect creative — score 15/20, FIX.**

| Criterion | Score | Note |
|-----------|-------|------|
| Hierarchy | 2 | stove reads first, then the headline |
| Product | 2 | stove reproduced correctly on the third attempt (see below) |
| Realism | **1** | firelight initially spilled onto the ceiling as an orange wash |
| Typography | 2 | Oswald at 64px, clean two-line lockup |
| Copy | 2 | contrast headline works |
| Color | 2 | amber CTA is the only accent |
| Space | 2 | margins clean |
| Logo | 2 | official file |
| Thumbnail | **1** | white headline over the brightest part of the scrim gradient |
| Idea | **1** | reads as a nice room; the *transformation* only lands with the pair |

**Attempts 1 and 2 were hard fails** (`R30-product`): the model gave the stove a curved door on attempt 1 and moved the flue to a rear exit on attempt 2. Both times the fix was to add the specific deviation to CONSTRAINTS by name. A general "preserve the product" line does not survive a scene change.

---

## 6 · The fix

1. **Scrim raised** — gradient top moved from y=630 to y=560 and the opaque point from y=1100 to y=1040, so the whole headline sits at ≥85% opacity. `scripts/qa.py --text-box 86,1040,994,1264` went from `scrim_uniformity: 0.71` to `0.96`.
2. **Firelight wash removed** by naming it: `light falls off within one metre of the firebox; the ceiling stays dark`. Vague negatives ("no glow") are weaker than a positive physical constraint.
3. **The pair shipped together**, sequenced Problem → Effect. Neither creative was rewritten to carry both halves — that would have broken R06.

**Second pass: Effect 18/20, Problem 17/20 — both ship.**

---

## 7 · What to steal

- **Name the specific deviation, don't restate the rule.** `no curved door, flue exits vertically` beats another sentence about preserving the product.
- **Change three lines, not the prompt**, when generating the other half of a pair. That's what makes a series look like one shoot (R20).
- **Positive physical constraints beat negative ones.** "Light falls off within one metre" is executable; "no glow bloom" is a hope.
- **Deadlines must be real.** If the client can't name a genuine cut-off, use PROOF or OBJECTION instead.
- **Before/after belongs in the campaign, not in the frame.** Two full-size creatives beat one split-screen that fails at thumbnail size.
