# 📦 Prompt Library — ready-to-use recipes for any image model

> Combine these with the **5-slot framework** (SCENE / SUBJECT / DETAILS / USE CASE / CONSTRAINTS) and the rules in **`design-rules.md`**. Always supply reference images with a clear role. Always request **one finished ad per generation**.

---

## 🧱 Universal prompt skeleton

```
Create ONE SINGLE FINISHED AD ONLY — no collage, no grid, no split-screen.
Aspect ratio: 4:5 (vertical), final size 1080x1350.

Reference images (with role):
- Image A (product/venue/food hero): preserve this EXACT subject/appearance.
- Image B (style/atmosphere): take the color grade, lighting and mood.

SCENE:       [place, time of day, environment — concrete, not abstract]
SUBJECT:     [main object/person/product — preserve from reference A]
DETAILS:     [lighting, camera, colors, texture] — text "HEADLINE" in [font, color, position]
USE CASE:    [platform] promotional ad for [BRAND], 4:5
CONSTRAINTS: no extra text beyond "HEADLINE"/"SUBLINE"/"CTA"; preserve brand colors;
             no watermark; no collage

Native poster typography:
- Brand wordmark small serif at top: "BRAND"
- Headline large bold: "HEADLINE"
- Subline one line: "SUBLINE"
- CTA: "CTA"
CRITICAL: every word spelled PERFECTLY — double-check 'BRAND', 'PLACE'.
```

---

## 🍽️ Restaurant — real food hero

```
ONE SINGLE FINISHED AD — no collage, no text on the food. Aspect 4:5, 1080x1350.

Reference image: the restaurant's REAL dish photo — reproduce THIS exact dish
(ingredients, plating). Do not invent dishes.

Layout: real dish photo as hero in the upper ~62%; a clean solid dark panel in
the lower ~38% holding the typography. Hard separation — no text over the food.

SCENE: tavern table near a sunlit window, coastal bokeh, warm natural light
SUBJECT: the real dish from reference, plated exactly as served
DETAILS: editorial food photography, shallow depth of field, rich saturated
         color, real textures. Shot on medium format, 50mm f/1.8.
USE CASE: Instagram restaurant ad, 4:5
CONSTRAINTS: no invented dishes, no text over food, preserve the real plating

Native text on the dark panel:
- Brand small serif top: "DE L'ETANG"
- Headline bold: "SOUVLAKI, OFF THE GRILL"
- Location line: "Havre des Pas · St Helier · Jersey"
- CTA: "RESERVE YOUR TABLE"
CRITICAL: perfect spelling, correct apostrophes.
```

---

## 🏨 Hotel / venue — coastal editorial

```
ONE SINGLE PREMIUM HOTEL AD BACKGROUND — no text, no logo (logo added later).
Aspect 4:5. Reference: the venue's real facade/interior — preserve its identity.

SCENE: golden hour at the [venue], coast/marina/terrace in warm light
SUBJECT: the real facade/terrace, authentic architecture
DETAILS: travel-magazine editorial, Canon EOS R5, RF 24-70mm f/2.8L,
         golden-hour light, premium color grade, clean negative space in lower third
USE CASE: hotel promo ad, 4:5
CONSTRAINTS: no text, no logos, no people unless requested, no collage
```

---

## 🏪 Local business — product / installation

```
ONE SINGLE FINISHED AD — realistic, functional, premium. Aspect 4:5.
Reference: the client's real installation/product — keep the product exactly,
change the scene to a premium lifestyle context.

SCENE: professional/real context (modern living room, workshop, storefront)
SUBJECT: the real product/installation from the reference
DETAILS: new lighting (golden hour / directional), premium editorial look,
         real textures, product as hero, clean negative space
USE CASE: local business ad, 4:5
CONSTRAINTS: no abstract/artistic; keep realistic; no text on product; no overlay boxes

Native text (or caption if the brand bans in-image text):
- Headline: "HEADLINE" · Subline: "SUBLINE" · CTA: "CTA" · Logo: brand top
CRITICAL: perfect spelling.
```

---

## 🎨 Clean-photo + typography overlay (when you don't want in-scene text)

1. Generate a **clean photograph** (ZERO text in the prompt).
2. Add typography + logo deterministically (design tool / Pillow / overlay).
3. Overlay rules:
   - Headline white + drop shadow (offset ~3px, alpha ≥ 200).
   - Bottom gradient: tall enough that the whole text block sits on dark (not on the food); near-opaque.
   - Gold only as a small accent on the dark gradient — never on the food itself.
   - Subline in a clean sans (e.g. Montserrat), not a thin script.
   - Place the **original logo file** (extract a white wordmark from a solid-color logo if needed).

---

## ⚠️ Native text — avoiding misspellings

1. **Quote every word** you want rendered.
2. **Keep it short** — brand + headline + one location line. More words = more risk.
3. Add `CRITICAL: every word spelled perfectly` + name the proper nouns.
4. **Vision-check every variant** — native text can drift on longer copy or small type.
5. **Know your model:** some models render in-scene text well, others produce gibberish. If yours mangles text, switch to the clean-photo + overlay recipe, or keep on-image words under ~8.

---

## 🧭 Model selection (host-dependent, generic rules)

| You need | Prefer |
|----------|--------|
| In-scene text (headline on a wall / neon / panel) | a model known to render text well |
| Clean lifestyle / product photography | any good photographic model |
| Real dishes / product / building preserved | a reference-capable model, feed real refs |
| Deterministic typography + logo | clean photo + overlay pipeline |
| Polish in-scene text | only a model proven at Polish spelling (diacritics) |
