# 🎬 Visual Advertising Engine

> **The canonical operating standard for every agent that generates advertising.** Applies to: ad generation · product photography · lifestyle visuals · Meta Ads creatives · social media graphics · e-commerce visuals · image-generation prompts · image-editing prompts · ad series & campaigns.

**This file is the single source of truth for the rules.** Every other file in this repo either points here (`SKILL.md`, `design-rules.md`) or condenses it for pasting (`core.md`). If two files disagree, this one wins.

**Rule IDs are stable.** Cite them in QA verdicts and code reviews: `FAIL: R03` (product changed), `FAIL: R30-logo`. Never renumber a rule — deprecate it and add a new ID.

| | |
|---|---|
| **Rules** | R01–R34 below |
| **Layout / type / color numbers** | [`references/layout-system.md`](references/layout-system.md) |
| **Headline & copy generation** | [`references/headline-system.md`](references/headline-system.md) |
| **QA gate (scored, machine-checkable)** | [`references/qa-gate.md`](references/qa-gate.md) |
| **Worked end-to-end examples** | [`examples/`](examples/) |

---

## R01 · MAIN GOAL

**We do not generate "pretty AI pictures."**

We generate images that could have been produced by:
- a professional advertising photographer
- an art director
- a good graphic designer
- a product stylist
- a media buyer who understands scroll and advertising

Every visual must fulfil **at least one** goal:
- stop attention
- show the product
- show the problem
- show the use case
- show the result
- build product desire
- increase brand credibility

> **If an image is only "pretty" but it's unclear what it sells — the creative is weak.**

---

## R02 · PRODUCT FIRST

**The product is the main character.**

The viewer must understand within about a second:
- what they see
- what is being advertised
- why it should interest them

The product must be:
- clearly visible
- appropriately large
- properly lit
- sharper than its surroundings
- shown at an attractive angle

> **Don't hide the product in a huge set. Don't build a beautiful interior where the product has to be searched for.**

---

## R03 · REFERENCE IMAGE = SOURCE OF TRUTH

If you receive a product photo, treat it like a **technical document**.

**NEVER change on your own:** shape · proportions · color · construction · material · logo · lettering · number of elements · mechanism · how the product works.

**AI MAY change:** environment · light · frame · perspective · set design · styling · mood.

But **not the product itself.**

If the product has an unusual mechanism, construction or way of working, the scene must **respect the product's physics**. Example: if a drop-down shelf slides vertically out from under a cabinet, there must be logical space it slides out of. Don't generate a construction that looks good but couldn't exist.

**Always name each reference's role in the prompt:** `Image A = subject (preserve exactly)`, `Image B = style/grade only`. An unlabelled reference gets averaged into the output.

---

## R04 · COMMERCIAL REALISM

**The target style:** professional commercial photography. **Not:** "obvious AI-generated advertisement".

Pay special attention to:
- correct perspective
- scale
- gravity
- contact of objects with surfaces
- correct shadows
- reflections
- textures
- materials
- natural depth of field
- correct human anatomy

**Materials must look like materials.** Metal like metal. Wood like wood. Glass like glass. Food should be moist, crispy, creamy or juicy when it actually is.

---

## R05 · ANTI AI-SLOP RULE

AI tends to add things nobody needs. **Automatically avoid:**
random neon · holograms · glowing lines · futuristic HUD · pseudo-interfaces · tiny icons · infographic bubbles · random gradients · arrows · fake logos · pseudo-lettering · excessive particles · random decorations · too-perfect interiors · excessive bokeh · plastic surfaces · aggressive HDR.

> **Don't use an effect just because the generator can create it. Every element must have a function.**

Full compendium: [`references/anti-slop-registry.md`](references/anti-slop-registry.md).

---

## R06 · ONE CREATIVE = ONE IDEA

Each ad has **one main message**. Don't try to show at once: product + 7 benefits + promotion + reviews + instructions + parameters + company story + CTA.

Pick **one reason** for a person to stop the scroll.

> One creative. One idea. One focal point.

---

## R07 · VISUAL HIERARCHY

- **PRIMARY** — what we see first. Most often: the product.
- **SECONDARY** — an element that explains context: a hand using the product, a kitchen, a person, food, a car, a bathroom, a garden.
- **TERTIARY** — subtle atmosphere elements. They must not compete for attention.

Two elements of equal weight = no hierarchy = FAIL. Type scale that enforces this: [`references/layout-system.md`](references/layout-system.md) §2.

---

## R08 · NEGATIVE SPACE

Don't fill the whole frame. Leave space. Negative space gives: premium feeling · room for a headline · easier ad reading · stronger hierarchy · calmer composition.

> A good ad often has **fewer** elements than a weak one.

Minimum safe margin: **8% of the short edge** on every side (86px on 1080px). Nothing crosses it.

---

## R09 · LIGHTING IS PART OF THE PRODUCT

Don't write "professional lighting". Say **exactly what the light does**.

- **CLEAN COMMERCIAL** — large soft key light, subtle fill, controlled shadows, clean highlights. *For:* e-commerce, electronics, cosmetics, home products.
- **PREMIUM DRAMATIC** — directional key light, controlled rim light, darker environment, strong material definition. *For:* premium products, automotive, alcohol, design objects, food hero shots.
- **NATURAL LIFESTYLE** — soft daylight from one side, realistic ambient bounce, natural shadows. *For:* home, furniture, kitchen, family products, wellness.
- **FOOD COMMERCIAL** — strong directional light emphasizing texture, steam, gloss, sauce and crispy surfaces. Food must look so the viewer practically feels its texture.

Always name: the key light's **size, direction and quality** (e.g. "large soft window light from camera-left, 45°").

---

## R10 · THINK LIKE A PHOTOGRAPHER

Every prompt makes a **camera decision**. Decide: camera position · angle · distance · lens character · depth of field · foreground · midground · background.

- **HERO** — low or eye-level perspective. The product looks more important.
- **LIFESTYLE** — 35–50mm natural perspective. The scene looks like real photography.
- **DETAIL** — macro / close-up. Shows texture and quality.
- **ENVIRONMENTAL** — wider, but the product stays the focal point.

---

## R11 · BUILD DEPTH

Avoid flat images. Good commercial photography has **foreground → subject → background**. A softly blurred element in front → the main product sharp → subtle environment behind. Gives natural depth and a photographic character.

---

## R12 · SHOW PRODUCT IN USE

A packshot alone isn't enough. Also generate images showing: who uses the product · where · when · what problem it solves · what result it gives.

The face doesn't always have to be visible. A **hand, silhouette, gesture, POV or detail** often gives enough context.

---

## R13 · THREE MANDATORY MARKETING ANGLES

For every product prepare **at least three directions**:
- **PROBLEM** — the frustration or situation *before* the product. Example: a hard-to-reach upper cabinet.
- **EFFECT** — the result. Example: the shelf drops exactly to the user's height.
- **LIFESTYLE** — how the product fits into a better life. Example: elegant kitchen, calm morning, user comfortably reaches for spices.

---

## R14 · VISUAL CREATIVE LIBRARY

Generate **many different directions**, not the same packshot ten times. Basic set:

01. **HERO SHOT** — product dominates the frame, lots of air, strong light, minimal scene.
02. **PREMIUM PACKSHOT** — clean studio, controlled light, perfect materials.
03. **LIFESTYLE** — product in the user's natural environment.
04. **PRODUCT IN USE** — the product's most important function in one moment.
05. **MACRO DETAIL** — detail of material, mechanism or texture.
06. **PROBLEM / SOLUTION** — the problem visually contrasted with the solution.
07. **RESULT** — the effect of using it, above all.
08. **UGC STYLE** — more natural photography, less perfect, like a real customer recommendation.
09. **PREMIUM EDITORIAL** — big-brand campaign style, more character, less classic e-commerce.
10. **SCROLL STOPPER** — unusual perspective, action or moment, still a readable product.

---

## R15 · FOOD REQUIRES DIFFERENT RULES

Food advertising must **build appetite**. Priorities: texture · steam · sauce · gloss · crunchiness · juiciness · freshness · layers · ingredients.

Good directions: cinematic hero food · dark premium food photography · ingredients suspended in motion · sauce splash · exploded burger/pizza layers · macro texture · steam and heat · chef finishing moment.

For dynamic scenes use **Frozen-Time / Bullet-Time** — ingredients, sauce, crumbs and drops frozen at the peak of motion. Food must still look physically credible.

**Authenticity beats stylization.** If the client has real dish photos, they are the hero (R03 applies to food). AI-invented dishes the venue doesn't serve = instant reject (R30).

Layouts, panel heights, gradient values: [`references/layout-system.md`](references/layout-system.md) §3. Niche depth: [`references/hospitality-food-services-playbook.md`](references/hospitality-food-services-playbook.md).

---

## R16 · PEOPLE SHOULD SUPPORT THE PRODUCT

Don't add a person just to have one. A person should: use the product · react to it · show scale · create context · represent the customer. The product or the effect of using it stays most important.

Watch: hands · fingers · gaze · hand-product contact · anatomy · natural gestures.

---

## R17 · TYPOGRAPHY COMES AFTER THE IMAGE

First a strong photograph, **then** the ad. Hierarchy:
- **HEADLINE** — short, bold, readable.
- **SUPPORT** — optionally one short sentence.
- **CTA** — only if actually needed.

Avoid: many fonts · big text blocks · badges everywhere · small descriptions · random buttons · 6 different text sizes. **An ad should not look like a dashboard.**

Type scale, pairings, tracking: [`references/layout-system.md`](references/layout-system.md) §2. What the words say: [`references/headline-system.md`](references/headline-system.md).

---

## R18 · DON'T LET THE MODEL INVENT TEXT

Two production modes — decide **before** generating (see [`references/layout-system.md`](references/layout-system.md) §5):

- **Mode A · Native in-render text** — the copy is baked into the AI render. Only when the model spells reliably. Quote every rendered word, keep strings short, append the spelling directive, vision-QA every variant.
- **Mode B · Deterministic composition** — generate a clean background (`no text, no logos, no signage`), then compose typography and the official logo file with code/design tool.

Either way: **never let the model invent** logos · prices · product names · slogans · labels · contact details. A "plausible" logo is a FAIL (R30).

---

## R19 · MOBILE-FIRST COMPOSITION

Design for the phone first.

- **META FEED — 4:5 (1080×1350).** **The default for static ads.** Use 4:5 unless the user explicitly asks otherwise.
- **REELS / STORIES — 9:16 (1080×1920).** Keep key elements out of the top 250px / bottom 320px UI zones.
- **MARKETPLACE / E-COMMERCE — 1:1 (1080×1080)**, or whatever the marketplace requires.

> Don't generate one image and hope random cropping solves every placement. Compose for the specific format. When text or a logo sits near an edge, resize with **scale+pad**, never a hard crop.

---

## R20 · SERIES MUST HAVE CONSISTENCY

If generating 5–10 images of the same product: **the product must be identical.** Change: context · frame · mood · light · situation · perspective. Don't change the product. A series should look like **one campaign shot during one shoot**.

---

## R21 · CREATE VARIATION, NOT RANDOMNESS

Don't create 10 × almost-the-same photo. Create: hero · lifestyle · feature · close-up · problem · result · premium · UGC · unexpected angle · emotional use case. **That is real creative diversity.**

A colour swap is not a variant. Two creatives are different when they test **different promises**, not different palettes.

---

## R22 · BEFORE / AFTER

Use Before/After **only when it instantly shows the product's value**: chaos → order · dark → light · dirty → clean · inconvenient access → product at hand height. Don't do before/after just because it's a popular format.

---

## R23 · GOOD SCROLL STOPPERS

Scroll-stopping doesn't mean "add more effects". Stop attention through: an unusual perspective · extreme close-up · a moment of action · frozen motion · interesting foreground · strong scale contrast · unexpected context · a very simple composition · a face or gesture · showing the problem.

---

## R24 · BUILD THE SCENE AROUND THE BENEFIT

Don't start with "make a beautiful kitchen". Start with **"what should this ad say?"**. Convenience → build a scene of convenience. Premium → a scene of quality. Speed → the time-saving moment. Taste → the food's texture. **Message first. Scene second.**

---

## R25 · PROMPT ARCHITECTURE

Every final prompt has this structure:

1. **OBJECTIVE** — what should the image communicate?
2. **SUBJECT** — who is the main character?
3. **ACTION / CONTEXT** — what is happening?
4. **ENVIRONMENT** — where are we?
5. **COMPOSITION** — how are the elements arranged?
6. **CAMERA** — perspective and lens character.
7. **LIGHTING** — exact light character.
8. **MATERIALS / TEXTURES** — what must look especially good?
9. **BRAND MOOD** — premium, playful, minimal, natural, etc.
10. **OUTPUT** — format and use case.
11. **CONSTRAINTS** — what absolutely must not change.

**A finished prompt has no placeholders.** If any bracket `[like this]` survives into the final prompt, it isn't finished. Fully worked examples: [`examples/`](examples/).

---

## R26 · EXAMPLE OF A WEAK PROMPT

> "Create a beautiful premium ad for this product in a modern luxury environment with cinematic lighting."

Too little. The generator has to invent almost everything — and its defaults are the slop in R05.

---

## R27 · EXAMPLE OF A STRONG PROMPT

> "Create a premium commercial product photograph using the supplied product reference as the exact source of truth. Place the unchanged product prominently in the foreground of a minimal contemporary kitchen during natural morning light. Show one realistic hand interacting with the product to immediately communicate its core function. Use an eye-level 50mm commercial photography perspective, strong subject separation, subtle foreground depth and a softly defocused environment. Large soft directional window light from camera-left should define the product materials and produce physically realistic shadows. Keep the background simple, neutral and premium with generous negative space above the product for advertising copy. The product must remain identical to the reference in shape, proportions, colors, materials, logo and mechanical details. No additional product features, no fake text, no decorative UI, no neon effects, no excessive props, no visual clutter. 4:5 vertical Meta Ads composition."

---

## R28 · CREATIVE GENERATION WORKFLOW

**Do not write the prompt first.** In order:

1. **Identify the product.**
2. **Identify the most important benefit.**
3. **Define the target.**
4. **Choose the marketing angle** — Problem / Effect / Lifestyle (R13).
5. **Invent a simple visual metaphor or situation.**
6. **Choose the creative type** (R14).
7. **Write the headline** ([`references/headline-system.md`](references/headline-system.md)) — the words decide the composition, not the reverse.
8. **Design the composition** ([`references/layout-system.md`](references/layout-system.md)).
9. **Define the light and camera** (R09, R10).
10. **Add constraints** (R03, R05).
11. **Only now write the final prompt** (R25).

---

## R29 · SELF-CRITIQUE

After generating a concept, evaluate it:
- Does it look like a real ad campaign?
- Does it look like typical AI generation?
- Is the product correct?
- Is the benefit clear?
- Is the scene physically logical?
- Can anything be removed?
- Would the photograph still work without text?

> **If it looks like typical AI graphics — redesign. Don't try to save it by adding more effects.**

---

## R30 · HARD FAIL CONDITIONS

Automatically reject a visual if:

| ID | Condition |
|----|-----------|
| `R30-product` | the product changed construction |
| `R30-logo` | the logo is wrong, redrawn or invented |
| `R30-text` | lettering is fake, misspelled or gibberish |
| `R30-anatomy` | hands or anatomy are deformed |
| `R30-physics` | the product's physics is wrong |
| `R30-scale` | the product is too small |
| `R30-chaos` | the image is chaotic |
| `R30-ui` | there's too much UI or icons |
| `R30-background` | the background draws more attention than the product |
| `R30-stock` | it looks like stock AI |
| `R30-function` | elements have no logical function |
| `R30-overload` | the ad tries to convey too many things |

A hard fail is not fixable by retouching. Regenerate.

---

## R31 · THE REMOVAL TEST

**"Can I remove something without worsening the message?"** If yes — remove it. A simpler creative with a strong idea beats a complicated one without a clear purpose.

---

## R32 · DESIGNER TEST

Imagine the visual goes to: Apple · Nike · IKEA · a premium restaurant · a high-end architecture brand · a professional ad agency. Don't copy those brands. Just ask: **"Would an art director accept the photography quality, hierarchy and composition?"** If not — improve it.

---

## R33 · META ADS TEST

Shrink the image to phone-screen size (or 150px wide). Check: do I still understand the ad? · is the product visible? · does the focal point still work? · can the headline be read? · does the scene stop attention? If the ad only works on a big monitor, it isn't designed for social media.

---

## R34 · FINAL QUALITY CHECK

Every visual passes the **scored gate** in [`references/qa-gate.md`](references/qa-gate.md) before delivery — 10 criteria × 0/1/2, threshold **≥16/20 with zero hard fails**. The checklist below is the human-readable version of that gate:

- [ ] One clear goal (R01)
- [ ] One main focal point (R06, R07)
- [ ] Product immediately visible (R02)
- [ ] Product 1:1 with the reference (R03)
- [ ] Correct perspective, materials, light, shadows, physics (R04)
- [ ] Clean background, no AI slop (R05)
- [ ] No fake text, no invented logo (R18, R30)
- [ ] Appropriate negative space and margins (R08)
- [ ] Mobile-first readability at thumbnail size (R19, R33)
- [ ] Clear marketing angle; headline is specific to this business (R24, headline test)
- [ ] Visual works even without copy (R29)
- [ ] Format matches the placement (R19)
- [ ] The whole looks like a professional ad (R32)

---

## 🏁 FINAL PRINCIPLE — DON'T DECORATE. DIRECT.

Don't treat the image generator as a tool for adding more and more effects. Treat it like a **production crew**. First decide: what we show · why we show it · where the viewer looks · what emotions we want · what benefit must be understood. Only later choose: light · lens · set design · styling · color · effects.

> **The best AI ad shouldn't look like an AI ad. It should look like a very well-planned photo campaign.**

**One product. One idea. One strong visual.**
