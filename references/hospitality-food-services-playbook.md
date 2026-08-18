# 🍽️ Hospitality · Food · Services — Playbook

> **Battle-tested rules for the three most common briefs.** Every rule here comes from real production campaigns (a coastal taverna, a seafront hotel, a local stove installer) — including the exact rejection modes that came back from the client and the layouts that passed QC. Follow this when the brief is a restaurant, hotel/venue, or a services business.

> **Where the numbers live:** exact grid, type scale, panel heights, gradient values, palettes and font pairings are in [`layout-system.md`](layout-system.md). What the copy says is in [`headline-system.md`](headline-system.md). How output is scored is in [`qa-gate.md`](qa-gate.md). This file is the niche judgement that sits on top of them.
> **Worked end-to-end examples of all three briefs:** [`../examples/`](../examples/).

---

## 1 · FOOD — how to make it look beautiful AND authentic

### 1a · Two modes — decide up front

| Mode | When | How |
|------|------|-----|
| **A · Real-food hero** | Client has real dish photos and cares about authenticity ("use OUR food") | Use the REAL photo as the hero + a **solid** dark/coloured text panel. **Never** AI-approximate the dishes. |
| **B · AI stylized food** | Client has NO usable food photos and accepts stylization | Generate a **dark studio editorial** background, then compose. |

### 1b · Winning layout for real food (Mode A) — QC'd 4.5/5

```
┌─────────────────────────────┐
│                             │
│     REAL FOOD PHOTO         │   ← top ~60–65%, full width
│     (hero, from refs)       │
│                             │
├─────────────────────────────┤
│  HEADLINE (white, bold)     │   ← bottom ~35–40%, SOLID dark/coloured
│  subline (one short line)   │      panel (navy or brand colour)
│  CTA button                 │
│  logo                       │
└─────────────────────────────┘
```

**Hard rule: clean hard separation — NO text sitting directly on the food.** If the dish fills the frame and you must use a scrim instead of a panel, it has to be tall and near-opaque: gradient height ≥720px reaching alpha 255 on 1080×1350 (layout-system §3b). A short 400px gradient is the naive value and it fails on bright food.

**Landscape photos:** don't force-crop a landscape table-spread to 4:5 (cuts ~50% width and clips plates). Use the "photo top + solid panel" layout instead of full-bleed cover-crop.

### 1c · AI stylized food (Mode B) — dark studio recipe

```
Dark studio editorial food photography. Black charcoal background.
Dramatic single spotlight from above on [DISH].
Rich saturated colors. Shot on Hasselblad H6D, 100mm f/2.8 macro.
4:5 vertical with generous dark negative space for typography.
NO TEXT, NO WATERMARK, NO LOGO, NO PEOPLE. Pure photograph.
```

Food must build appetite: texture, steam, gloss, juiciness, layers, sauce, crispness. For dynamic scenes use **Frozen-Time / Bullet-Time** (ingredients, sauce, crumbs frozen at peak motion) — but food must stay **physically credible**.

### 1d · Native in-render text for food/venue

When the client wants the copy **baked into the AI render** rather than pasted on afterwards (a common and reasonable ask — pasted-on text is what makes an ad look like a template):

- **Use a model proven to spell in-scene text.** Model capability changes fast — verify on your host rather than trusting a name (`prompt-library.md` §model selection). Pattern: prompt file with `Reference image N: '<abs-path>'` for the real dish/venue, plus a short text block + atmosphere cues + camera/lens specs.
- **Keep text SHORT** — brand + headline + one location line. More words = more spelling risk.
- Append: `CRITICAL: every word must be spelled PERFECTLY with no typos — double-check '<brand>', '<place>'.`
- **Never render a brand name containing an apostrophe, ampersand or accented character natively.** Leave the space and place the logo file (verified failure mode — see `../examples/01-restaurant-real-food.md`).
- **Vision-QA every variant** — native text can drift, especially missing apostrophes.

**Deterministic PIL overlay is a fallback** (tiny garbled footer), not the default composition method.

### 1e · Legibility on busy/light food photos (verified fixes)

When the background is a bright or dense food shot, the naive layout fails QC. Rules that fixed it:

- **ALL headline lines white** with a dark drop shadow (offset ~3px, alpha ~180). Do **NOT** make the second line gold/beige over food — it blends into lemon/sauce/meat. Reserve gold for small accents **on the dark gradient**, not on the food.
- **Subline in a clean sans-serif (Montserrat), not a thin script (GreatVibes).** Script is unreadable at subline size on a busy frame. Script only for large display accents.
- **Taller, near-opaque bottom gradient** (for 1080×1350: height ≥720px, alpha → 255) so the whole text block sits on dark navy.
- **Top logo wordmark**: add a drop shadow + a subtle top scrim (~150px tall, alpha ~175) so a white logo reads on a bright sky/facade.

### 1f · Headline font sizing — the #1 crop failure

Mode A crop-risk table and the full type scale live in [`layout-system.md`](layout-system.md) §2a–2b. The niche-specific part:

After the first pass **always** vision-QA the contact sheet for mid-word truncation, text touching edges, and headlines landing on busy areas of the food (→ deepen the scrim, or move to the panel layout). Food photos fail this more than any other category because the bright, high-frequency areas move between renders.

---

## 2 · HOTELS / VENUES — premium but authentic

### 2a · Core principle
Prefer **real-photo + deterministic typography/layout** over AI re-generation of the building/facade. Preserves authenticity and avoids AI-slop interiors or redrawn signage.

### 2b · Design system (premium/traditional)
- Default feed: **1080×1350 / 4:5**.
- Real photo as hero/top image or full background.
- **Cream/off-white content card** for copy (rests on the photo), OR solid dark panel.
- **Serif headline + clean sans body** for premium/traditional.
- **Coastal palette** when relevant: navy, teal, cream, white, gold.
- CTA as a **dark rounded button**.
- Keep copy short — hospitality flyers become unreadable fast (3 bullets max).

### 2c · 10 structurally different styles (not colour swaps)
1. Luxury heritage facade poster
2. Editorial travel magazine cover
3. Minimal Swiss grid
4. Coastal blue gradient hero
5. Boutique restaurant promo
6. Terrace / afternoon tea flyer
7. Events / nightlife poster
8. Family seaside escape
9. Direct booking offer
10. Multi-panel brand story

### 2d · AI background recipe (coastal editorial)
```
Premium coastal editorial photography. Golden hour at [LOCATION].
Shot on Canon EOS R5, RF 24-70mm f/2.8L. Travel magazine quality.
4:5 vertical with clean negative space. NO TEXT, NO WATERMARK, NO LOGO.
```

### 2e · Angles that test distinct promises (not palettes)
Heritage · seafront escape · terrace · dining · direct booking · events · arrival/evening · destination · offer · brand story.

---

## 3 · SERVICES (installation, home improvement, local biz) — show the result

### 3a · Real install/product photos → NEW premium scenes
- Use real product/installation photos as **references**, then generate **new premium scenes** (different light, time of day, lifestyle).
- **Don't** paste overlays onto the client's raw photos.
- Readable CTA + logo fidelity + location/phone.

### 3b · Angles that sell services
- **Problem → Effect** (hard-to-reach cabinet → shelf at hand height). Ship it as a **pair of full-size creatives**, not a split-screen — a before/after squeezed into one frame halves both halves and fails the thumbnail test (R33). Worked example: [`../examples/03-services-problem-effect.md`](../examples/03-services-problem-effect.md).
- **Package tiers** (e.g. "Installation included", "Finance available — £0 deposit").
- **Deadline offers** (seasonal price lock: "Install before Oct 31"). The deadline must be real — never invent urgency for a local business that has to live with it.
- **Transformation** (chaos → order, dark → light, dirty → clean).
- **Benefit-led headline ≤40 chars**, body ≤125 chars.

### 3c · Build the scene around the benefit
Don't start with "make a beautiful kitchen". Start with "what should this ad say?". Convenience → scene of convenience. Premium → scene of quality. Speed → the time-saving moment. **Message first, scene second.**

---

## 4 · Deterministic composition (when NOT using native AI text)

### 4a · Two-layer workflow
1. **Generate fresh AI backgrounds first** from the reference photos (as style refs), never text-on-photo. `ONE SINGLE ... BACKGROUND ONLY — no text, no logos, no words, no signage, no collage, no grid` + leave negative space for typography.
2. **Compose the final ad deterministically** (PIL / HTML / Figma): official logo file + exact headline/subline/CTA + brand panels + safe margins + real fonts.

### 4b · Deterministic typography checklist
- Official logo only; never AI-redrawn logo.
- Headline 1–5 words; subline one short line; CTA one clear action.
- Min 8% margin on 4:5 ads.
- Use contrast panels/gradients when photography is busy.
- No tiny fake footer/contact lines.

### 4c · White wordmark extraction from a solid-colour logo

When the logo is a white wordmark on a solid colour (e.g. white type on a blue square) and you need the wordmark alone, transparent:

```bash
python ../scripts/extract_wordmark.py refs/logo.png build/logo_white.png
# dark mark on a light background:
python ../scripts/extract_wordmark.py refs/logo.png build/logo_dark.png --invert
```

The script masks and crops the original pixels — it never redraws anything (R03).

Place the extracted wordmark prominently (top centre, ~300–320px wide on 1080px ad) with a drop shadow + top scrim so it reads over bright backgrounds. **Never** substitute a text rendering of the brand name for the official logo.

---

## 5 · Marketing psychology — angle + copy levers

- **Angle matrix:** test 3 angles × 2 hooks. Each angle = one core promise + "why this wins" (whitespace, geo advantage, competitor gap).
- **Copy variants:** **Direct** ("Get X. Here's how.") · **Story** ("Last winter, the Smiths froze…") · **Authority** ("As seen in 500+ homes…") · **Urgency** ("Install before Oct 31 — price lock").
- **Headline ≤40 chars, benefit-led.** Body ≤125 chars. Full budgets and the ten archetypes: [`headline-system.md`](headline-system.md).
- **Build the scene around the benefit** — message first, scene second (R24).
- **One creative = one idea.** Pick one reason to stop the scroll (R06).
