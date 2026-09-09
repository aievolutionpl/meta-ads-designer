# 📦 Prompt Library — skeletons for any image model

> **These are skeletons, not finished prompts.** A prompt with a `[bracket]` left in it is unfinished (R25) — the model fills the bracket with its own average, and its average is slop. For **finished** prompts with every decision made, see [`../examples/`](../examples/).

Combine with the 11-part architecture (R25), the numbers in [`layout-system.md`](layout-system.md) and the copy method in [`headline-system.md`](headline-system.md). Always label each reference's role. Always request **one finished ad per generation**.

---

## Choose the medium first

Use [art direction](art-direction.md) for the visual decision and [prompt craft](prompt-craft.md) for final wording. Photographic fields below are conditional: a typographic flyer needs type and graphic form instead of a lens. R25 is the semantic checklist; five slots are a compact packaging option.

Specify one ad, not a contact sheet. A purposeful split composition is allowed when it serves one message. See [worked directions](../examples/05-model-independent-directions.md) for event, food and service prompts.

## 🧱 Universal skeleton

```
Create ONE SINGLE FINISHED AD ONLY — no collage, no grid, no split-screen.
Aspect ratio: 4:5 (vertical), final size 1080x1350.

Reference images (with role):
- Image A = subject, source of truth: preserve this EXACT subject/appearance.
- Image B = style only: take the colour grade, lighting and mood, nothing else.

OBJECTIVE:   [what the viewer must understand and feel in one second]
SUBJECT:     [main object/person/product — preserved from reference A]
ACTION:      [what is happening, if anything]
ENVIRONMENT: [place, time of day, weather — concrete, never abstract]
COMPOSITION: [where each element sits, in percentages of the frame,
              and which area is left clean for typography]
CAMERA:      [height, angle, focal length, aperture, what is sharp]
LIGHTING:    [source, size, direction, quality, where the shadow falls]
MATERIALS:   [what must read as real: metal, char, wool, glass]
BRAND MOOD:  [three adjectives, and one the ad must NOT be]
OUTPUT:      [platform] ad, 4:5, 1080x1350
CONSTRAINTS: [what must not change, plus every hallucination seen so far]

Native typography (Mode A only):
- brand line:  "BRAND"
- headline:    "HEADLINE"
- detail line: "DETAIL"
- CTA:         "CTA"
CRITICAL: every word spelled PERFECTLY — double-check 'BRAND', 'PLACE'.
```

**Rule of thumb:** if a slot could be answered by a different agency for a different client without changing a word, it isn't specific enough yet.

**Editing an existing image rather than making a new one?** The skeleton above gains two slots, and they are never written apart — see the edit template below (`R41`).

---

## 🍽️ Restaurant — real food hero

```
ONE SINGLE FINISHED AD — no collage, no text on the food. Aspect 4:5, 1080x1350.

Reference image A = subject, source of truth: the restaurant's REAL dish photo.
Reproduce THIS exact dish — same ingredients, same plating, same quantity.
Do not invent dishes, garnish or props.

COMPOSITION: real dish as hero filling the top 62%; a SOLID dark panel across
the bottom 38% holding the typography. Hard straight edge, no gradient blend,
no text over the food.
CAMERA: 45-degree angle at table eye level, 50mm, f/2.2, front of the plate sharp.
LIGHTING: late-afternoon window light from camera-left, warm, directional,
raking across the food so texture and gloss read. One soft shadow to the right.
MATERIALS: char, gloss, steam, blistering, condensation — whatever is actually there.
CONSTRAINTS: no invented dishes · no text on food · plating exactly as served ·
no people · no props not in the reference.

Native text on the panel only:
- brand, small serif:  "BRAND"
- headline, bold sans: "HEADLINE"
- detail line:         "Street · Town · opening hours"
- CTA:                 "RESERVE A TABLE"
CRITICAL: perfect spelling. Brand names with apostrophes → place the logo
file instead of rendering them (verified failure mode).
```

Finished version: [`../examples/01-restaurant-real-food.md`](../examples/01-restaurant-real-food.md).

---

## 🏨 Hotel / venue — editorial background (Mode B)

```
ONE SINGLE PHOTOGRAPHIC BACKGROUND ONLY — no text, no words, no signage,
no logos, no numbers, no collage. Aspect 4:5, 1080x1350.

Reference image A = subject, source of truth: the venue's real facade/terrace.
Preserve the architecture exactly: window proportions, storey count, roofline,
render colour, balustrade. Do not redraw or "improve" the building.

SCENE: [named location], golden hour, [season].
COMPOSITION: building occupying two-thirds, clean sky in the upper third,
nothing crossing the outer 8% margin, negative space held for typography.
CAMERA: standing eye level, 24-70mm at 35mm, f/4.
LIGHTING: low golden-hour sun from camera-left, long raking light, held
shadows, travel-magazine grade, no HDR halo.
CONSTRAINTS: architecture identical to the reference · no invented balconies
or signage · no people · no text of any kind.
```

Finished version: [`../examples/02-hotel-editorial.md`](../examples/02-hotel-editorial.md).

---

## 🏪 Local business — product / installation

```
ONE SINGLE PHOTOGRAPHIC BACKGROUND ONLY — no text, no logos, no numbers.
Aspect 4:5, 1080x1350.

Reference image A = subject, source of truth: the client's real installation.
Keep the product identical — body proportions, door, hinge, hardware, how it
connects. Change only the room, the light and the styling.

SCENE: a real, lived-in context at [time of day].
COMPOSITION: product in the lower-left third, leading line to camera-right,
soft foreground element entering the frame. Upper 45% kept calm for typography.
CAMERA: seated eye level, 35mm, f/2.8, product sharp.
LIGHTING: [the one real source], realistic falloff, physically correct shadows.
No glow bloom, no haze, no flare.
CONSTRAINTS: product identical to the reference · pin every count (tiers,
fixings, storeys) · no lettering or badges anywhere on the product ·
no people · no text.
```

Finished version: [`../examples/03-services-problem-effect.md`](../examples/03-services-problem-effect.md).

---

## 🎨 Mode B — clean photo + deterministic typography

1. Generate a **clean photograph** with zero text in the prompt, and an explicitly **planned empty area** for the copy. A background generated without that instruction produces the pasted-on look no matter how good the typography is.
2. Compose typography + the official logo file deterministically (design tool, PIL, HTML).
3. Apply the numbers in [`layout-system.md`](layout-system.md): 86px margins, the type scale, scrim ≥720px reaching alpha 255, contrast ≥4.5:1, accent in ≤3 places.
4. Extract a white wordmark if needed: `python scripts/extract_wordmark.py logo.png logo_white.png`.
5. Score it: `python scripts/qa.py out/ad.png --format 4:5 --text-box x0,y0,x1,y1`.

---

## ✏️ Reference-image edit — the preservation contract

The template for changing something in an image that already exists. **Most commercial work is this**, and its dominant failure is not a dirty texture — it is the model rebuilding what nobody asked it to touch (`R41`, [`artifact-control.md`](artifact-control.md) §7).

```
Edit the supplied reference image. ONE change only.

Reference image A = the scene, source of truth: this exact room/subject.
Reference image B = the new object, source of truth: this exact product.

EDIT INSTRUCTIONS: Replace only [the one element] with the object in
  reference B. Match its scale, perspective, contact shadows and
  reflections to the existing scene light.
PRESERVE: the original room layout, architecture, proportions, furniture
  placement, flooring, camera position and perspective. Do not redesign
  the room, move furniture, alter architecture, or change the framing.
LIGHTING: retain the existing light direction and quality; refine only
  for a premium commercial-photography finish.
MATERIALS: keep wood, stone, glass, plaster and metal physically
  believable — metal behaves like metal, glass like glass.
CONSTRAINTS: no edge halos, no glow around the new object, no texture
  bleed across the boundary, no duplicated objects, no warped geometry,
  no melted edges, no impossible reflections. Nothing added that was
  not asked for.
```

### The three preservation blocks

Drop the one that fits into `PRESERVE`:

| Editing | Block |
|---------|-------|
| **A scene / interior** | `Preserve the original room layout, architecture, proportions, furniture placement, flooring, camera position and perspective. Change only [X].` |
| **A person** | `Preserve facial identity, bone structure, proportions, age, skin features and expression. Do not redesign the face.` |
| **A product** | `Preserve the exact product geometry, proportions, materials, branding and recognisable design details. Use the supplied product reference as the dominant visual anchor.` |

### Four rules that go with it

1. **Never write `EDIT INSTRUCTIONS` without `PRESERVE`.** Anything you don't name is fair game — silence reads as permission.
2. **One element per turn.** Simultaneous changes produce drift, halos, duplication and clutter all at once. Two clean edits beat one ambitious one.
3. **Reference accuracy outranks creative improvement.** An edit that made the picture nicer while losing the room is a failed edit.
4. **Only the negatives this scene can produce.** Geometry and boundary negatives for edits; anatomy negatives only when there is a person. Every possible constraint in one prompt dilutes the ones that matter.

---

## 🧬 Anti-artifact block — append on any fine-texture brief

Add to the `CONSTRAINTS` slot whenever the scene carries fur, knit, weave, foliage, water, crumb, seeds, stone, rust or particles — the subjects that dissolve into noise (`R40`, [`artifact-control.md`](artifact-control.md) §2):

```
STRICTLY NO cellular texture, NO webbing, NO netting, NO neural-network
patterns, NO repeating Voronoi patterns, NO noise clusters, NO tiled or
repeating texture fills, NO speckled grain across flat surfaces.
Micro-texture is readable ONLY on [the one named surface]; every other
surface is smooth, even, or out of focus.
```

Three rules that go with it:

1. **Never write a density adjective.** `ultra-detailed`, `intricate`, `hyper-detailed`, `rich texture`, `8k` are requests for unbounded micro-repetition. Name the material instead — "char blistering on one edge", "brushed steel with a visible grain direction".
2. **Keep `COMPOSITION` a layout specification.** Discrete bounded parts in percentages — which is what the skeleton above already asks for. A holistic atmospheric description is what artifacts.
3. **Never collide two styles.** If one artist in one medium could not produce both descriptors at once, the render will try to satisfy both and come back noisy. Check the `BRAND MOOD` slot too.

**Reduce high-frequency detail, don't just ban it.** Where an atmospheric element genuinely belongs in the scene, ask for less of it rather than none — "a small number of subtle natural sparks" instead of "thousands of glowing sparks flying everywhere"; "very subtle atmospheric haze" instead of "dense fog filling the room". Quantity is what dissolves into noise, not the element itself.

**Session hygiene beats every prompt fix here:** generate each of these prompts in a **fresh session**, one image only. Re-prompting in a session that already produced an image is the largest single cause of dirty output — refine the prompt and open a clean room instead ([`artifact-control.md`](artifact-control.md) §5).

---

## ⚠️ Native text — avoiding misspellings

1. **Quote every word** you want rendered.
2. **Keep it short** — brand + headline + one detail line. ≤12 rendered words total.
3. Add `CRITICAL: every word spelled perfectly` and name the proper nouns.
4. **Never render punctuation-heavy brand names** (apostrophes, ampersands, accents, inch marks). Leave the space, place the file.
5. **Diacritics → Mode B.** Polish `ą ć ę ł ń ó ś ź ż` is the highest-failure case (headline-system §5).
6. **Vision-QA every variant** — and ask the model to *transcribe* what it reads, not to confirm that the spelling is right.

---

## 🧭 Model selection (host-dependent)

Model capability changes faster than this repo. Verify on your host rather than trusting a name.

| You need | Prefer |
|----------|--------|
| In-scene text (headline on a panel, wall or neon) | a model verified to render text on *your* host, this month |
| Clean lifestyle / product photography | any strong photographic model |
| Real dishes / product / building preserved | a reference-capable model, fed the real refs with labelled roles |
| Deterministic typography + logo | any clean-photo model + a composition step (Mode B) |
| Diacritics of any kind in-image | none — use Mode B |
