# 📐 Layout System — the numbers that make it look designed

> **This file exists because "generous margins" is not a specification.** Everything here is a number an agent can execute and a QA script can verify. When a rule in [`visual-advertising-engine.md`](../visual-advertising-engine.md) says "appropriate negative space", this file says `86px`.

All values are given for the default canvas **1080×1350 (4:5)** and scale proportionally to other formats (§1c).

---

## 1 · Canvas, grid and safe areas

### 1a · The grid

| Property | Value (1080×1350) | Note |
|----------|-------------------|------|
| Columns | 12 | |
| Gutter | 24px | |
| Outer margin | **86px** (8% of the 1080 short edge) | nothing crosses it — R08 |
| Column width | (1080 − 2×86 − 11×24) / 12 = **53.7px** | |
| Baseline unit | 8px | all vertical spacing is a multiple of 8 |

**Practical spans:** headline blocks use 10–12 columns. A content card uses 10 columns. Never set text to a measure wider than ~12 columns or narrower than ~4.

### 1b · Safe areas by placement

| Format | Canvas | Outer margin | Extra keep-out |
|--------|--------|--------------|----------------|
| **4:5 feed** | 1080×1350 | 86px all sides | bottom 120px — *advisory*, some placements only |
| **9:16 story/reel** | 1080×1920 | 86px sides | **top 250px** (profile row), **bottom 320px** (CTA + caption) |
| **1:1** | 1080×1080 | 86px all sides | — |
| **16:9** | 1920×1080 | 96px all sides | — |
| **2:3 Pinterest** | 1000×1500 | 80px all sides | — |

Anything critical (headline, logo, price, CTA) lives **inside** the safe area. Decorative photography may bleed.

**What is gated and what is advice.** The 86px margin and the 9:16 chrome zones are hard — `scripts/qa.py --text-box` fails a creative that crosses them, because that chrome is drawn on top of the image. The 4:5 bottom 120px is advisory: the canonical photo+panel layout (§3a) deliberately runs its CTA/logo row at 64px from the bottom, and on a standard feed placement nothing covers it. Keep copy out of it when you can; don't redesign §3a to satisfy it.

### 1c · Scaling to other formats

Multiply every px value in this file by `canvas_short_edge / 1080`. For 9:16 (short edge still 1080) sizes stay identical — only the keep-out zones change. For 16:9 (1920×1080, short edge 1080) sizes stay identical; the grid becomes 12 columns across 1920 with 96px margins.

**Never** design once and crop. Recompose. When text or a logo ends up near an edge, fix with **scale+pad**, never a hard crop (R19).

---

## 2 · Type scale

### 2a · The scale (1080px-wide canvas)

| Role | Size | Weight | Tracking | Line-height | Max chars |
|------|------|--------|----------|-------------|-----------|
| **Eyebrow / label** | 24px | 600 | +8% (uppercase) | 1.2 | 24 |
| **Headline — 1 line** | 88px | 700–900 | −1% | 1.05 | 22 |
| **Headline — 2 lines** | 64px | 700–900 | −1% | 1.10 | ≤22 per line, ≤40 total |
| **Headline — 3 lines** | 48px | 700–900 | 0 | 1.15 | 3 × 26 |
| **Subline** | 34px | 400–500 | 0 | 1.35 | 45 |
| **Body / detail row** | 28px | 400 | 0 | 1.45 | 60 |
| **CTA (button label)** | 28px | 600 | +6% (uppercase) | 1.0 | 18 |
| **Legal / credit** | 18px | 400 | +2% | 1.3 | — |

**The hierarchy ratio (R07):** headline ≥ 3× body size. At 88/28 that's 3.1× — the minimum that survives a thumbnail. If your headline needs to drop below 48px to fit, **the copy is too long** — rewrite it ([`headline-system.md`](headline-system.md)), don't shrink the type.

**Never use more than 3 sizes on one ad**, and never more than 2 typeface families.

### 2b · Crop-risk table (verified on 4:5)

| Size | Safe for | Risk |
|------|----------|------|
| 36–44px | headlines of 1–3 words | very safe |
| 48–56px | headlines of 1–2 words | test on the contact sheet |
| 56–88px | single-word headers, big display | high crop risk — vision-QA required |
| 24–28px | body / subtitle | safe with a shadow |

This table applies to **Mode A (native in-render text)**, where the model chooses the actual rasterized size and mid-word truncation is the #1 failure. In Mode B you control the raster — use §2a instead.

### 2c · Font pairings (name real typefaces — R17)

| Category | Display / headline | Body / support | Mood |
|----------|--------------------|----------------|------|
| Hospitality, hotel, fine dining | **Playfair Display** 700 · *fallback:* Cormorant Garamond, Georgia | **Montserrat** 400/600 · *fallback:* Inter, Helvetica | premium, traditional |
| Casual restaurant, taverna, bistro | **Archivo** 800 · *fallback:* Archivo Black, Impact | **Inter** 400/600 · *fallback:* Helvetica | warm, direct |
| Events, nightlife, promo | **Anton** 400 · *fallback:* Oswald 700, Impact | **Oswald** 400 · *fallback:* Barlow Condensed | loud, poster-like |
| Services, trades, home improvement | **Oswald** 600 · *fallback:* Barlow Condensed 700 | **Source Sans 3** 400 · *fallback:* Roboto | solid, functional |
| Retail, e-commerce, product | **Inter** 800 · *fallback:* Helvetica Now, Arial | **Inter** 400 | clean, neutral |
| Editorial / travel | **Didot** or **Cormorant** 600 · *fallback:* Playfair Display | **Lato** 400 · *fallback:* Inter | magazine |

All listed families are open-licence (SIL OFL) except Didot and Helvetica Now — substitute the fallback if you don't hold a licence.

**Never write "modern sans-serif", "elegant serif" or "clean font" in a prompt.** That is how every ad ends up in Inter.

### 2d · Casing and script rules

- **All-caps only for short labels** — eyebrows, badges, "STEP 01", CTA buttons (<4 words). Never all-caps body copy.
- **Uppercase always gets +6–8% tracking.** Lowercase gets 0 to −1%.
- **Script / handwriting fonts only above 56px**, and only as a display accent. At subline size on a busy photo they are unreadable — a verified rejection mode.
- **Polish and other diacritics:** verify the chosen family actually ships `ą ć ę ł ń ó ś ź ż`. Anton and many display faces do; some do not, and the renderer silently substitutes.

---

## 3 · The three canonical layouts

### 3a · Photo-top + solid panel (the safest, works for any niche)

```
┌─────────────────────────────┐  0
│                             │
│      REAL PHOTO (hero)      │  ← 0 → 843px  (62.5%)
│                             │
├─────────────────────────────┤  843
│  EYEBROW                    │  ← panel starts, solid fill
│  HEADLINE                   │  ← 2 lines max
│  subline                    │
│  [ CTA ]        logo        │
└─────────────────────────────┘  1350
```

| Element | Value |
|---------|-------|
| Photo height | 810–878px (60–65%) |
| Panel height | 472–540px (35–40%) |
| Panel fill | **solid** brand dark or brand color — not a gradient |
| Panel inner padding | 86px sides, 56px top, 64px bottom |
| Separation | hard edge. **Zero text on the photo.** |
| Logo | bottom-right or panel-centre, height 56–72px |

Use this whenever the photo is busy, bright, or landscape-shaped. A landscape table-spread force-cropped to 4:5 loses ~50% of its width and clips the plates — use this layout instead of a full-bleed cover-crop.

### 3b · Full-bleed + scrim (when the photo has its own negative space)

```
┌─────────────────────────────┐
│  logo (top, on top-scrim)   │  ← top scrim 150px, alpha 175
│                             │
│        PHOTO, full bleed    │
│                             │
│░░░░░░░░░░░░░░░░░░░░░░░░░░░░░│  ← gradient starts at y≈630
│▓▓ HEADLINE ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓│
│███ subline · CTA ███████████│  ← alpha reaches 255 by y≈1100
└─────────────────────────────┘
```

| Element | Value |
|---------|-------|
| Bottom gradient height | **≥720px** on 1350 (the naive 400px fails on bright food) |
| Gradient max alpha | **255** at the bottom, ease-in from 0 at the top of the gradient |
| Gradient color | brand dark (e.g. `#0A0E1A`), never pure black on a warm photo |
| Text drop shadow | offset 3px, blur 8px, alpha ≥200 |
| Top scrim (if a light logo sits on a bright sky) | 150px tall, alpha 175 |

**Rule:** the entire text block must sit where the scrim is ≥85% opaque. If any glyph sits on the raw photo, deepen the gradient — don't move on.

### 3c · Editorial split (poster / heritage / brand story)

```
┌─────────────────────────────┐
│   EYEBROW                   │  ← 86px margin, upper third is type
│   HEADLINE                   │
│   subline                    │
│                              │
│   ┌──────────────────────┐   │  ← photo as a placed block,
│   │       PHOTO          │   │     10 columns wide, not full bleed
│   └──────────────────────┘   │
│   detail row · logo          │
└─────────────────────────────┘
```

Type occupies the top 35–40%, the photo is a **placed rectangle** with margin on all sides, background is a flat brand color. Nothing overlaps. This is the layout that reads most "designed" and least "AI" — use it when the photo alone is not strong enough to carry the frame.

---

## 4 · Color

### 4a · Rules with numbers

- **One accent color, used in ≤3 places** (a label, a rule, the CTA).
- **Text contrast ≥ 4.5:1** against whatever is directly behind it, measured at the text bounding box — not "roughly dark enough". `scripts/qa.py` measures this.
- **Background is one of three things:** true white `#FFFFFF`, a saturated brand color, or a dark neutral. Avoid cream/sand/beige "for warmth" — it reads as default AI.
- **Gradients only for function** (a scrim so text reads over a photo), never as decoration.

### 4b · Starter palettes per category

| Category | Dark | Light | Accent | Notes |
|----------|------|-------|--------|-------|
| Hospitality / coastal | `#0A1F33` navy | `#F4F1EA` off-white | `#D4A853` gold | the proven premium editorial pair |
| Fine dining / dark studio | `#0D0D0D` charcoal | `#EDE8E0` | `#B8863B` bronze | accent only on the dark panel |
| Casual food / taverna | `#1C2B2D` deep green | `#FFFFFF` | `#E2571E` terracotta | warm, not luxury |
| Services / trades | `#12232E` slate | `#FFFFFF` | `#F2A03D` amber | high contrast, functional |
| Events / nightlife | `#08080B` near-black | `#FFFFFF` | `#FF2E63` hot pink *or* one brand hue | one accent only |
| Retail / product | `#111111` | `#FFFFFF` | brand hue | let the product carry the color |

**These are starting points, not identities.** If the client has a brand palette, it wins — always (R03 applies to brand assets too).

---

## 5 · Production modes — the decision

| | **Mode A · Native in-render text** | **Mode B · Deterministic composition** |
|---|---|---|
| **What** | copy baked into the AI render | clean AI background + code/design-tool composition |
| **Choose when** | short Latin-script copy; the model spells reliably; user wants "fully generated" | logo fidelity matters; long copy; diacritics; prices/legal; exact brand colors |
| **Prompt opens with** | `ONE SINGLE FINISHED AD ONLY — no collage, no grid, no split-screen.` | `ONE SINGLE ... BACKGROUND ONLY — no text, no logos, no words, no signage, no collage.` |
| **Text handling** | quote **every** rendered word; keep to brand + headline + one line; append `CRITICAL: every word must be spelled PERFECTLY — double-check '<brand>', '<place>'.` | the model renders no text at all |
| **Logo** | risky — prefer to leave space and place the file afterwards | official file, placed; never AI-drawn |
| **QA** | vision-QA every variant for spelling drift | verify contrast, margins, logo clear space |
| **Failure mode** | misspellings, missing apostrophes, mid-word truncation | looks pasted-on if the background has no planned negative space |

**Both modes can ship in one batch.** Deliver a combined contact sheet.

**Mode B's non-negotiable:** the background prompt must **plan the negative space** ("clean negative space in the lower third for typography"). A background generated without that instruction produces the Canva look no matter how good the typography is.

---

## 6 · Logo placement

| Property | Value |
|----------|-------|
| Height on a 1080-wide canvas | 56–72px (panel/footer), up to 120px as a top-centre wordmark |
| Clear space | ≥ 1× the logo's cap height on every side |
| Minimum legible width | 180px for a wordmark, 96px for a mark |
| On a bright background | white version + drop shadow, or a 150px top scrim at alpha 175 |
| Source | **the official file, always.** Never a text rendering of the brand name, never an AI redraw (R30-logo) |

Extracting a white wordmark from a solid-color logo: `scripts/extract_wordmark.py`.

---

## 7 · Quick reference card

```
canvas      1080×1350 (4:5 default)
margin      86px  ·  baseline 8px  ·  gutter 24px
headline    88px 1-line / 64px 2-line / 48px 3-line, weight 700–900
subline     34px  ·  body 28px  ·  CTA 28px upper +6% ·  eyebrow 24px
ratio       headline ≥ 3× body
panel       photo 62.5% / panel 37.5%, solid fill, hard edge
scrim       ≥720px tall, alpha → 255, text shadow 3px/alpha 200
contrast    ≥ 4.5:1 at the text bounding box
accent      ≤ 3 placements
fonts       ≤ 2 families, ≤ 3 sizes, named — never "modern sans-serif"
logo        56–72px, official file, clear space ≥ 1 cap height
```
