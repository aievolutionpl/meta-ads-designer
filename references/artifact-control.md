# 🧬 Artifact Control — keeping the render clean

> The operating tool behind **R40**. Every other rule in this skill assumes the render came back clean. This one is about the renders that don't: the cellular webbing across a knitted jumper, the noise clusters in the foliage, the faint ghost of the last image bleeding into this one, the product that quietly changed shape on generation four.
>
> Artifacting is not bad luck and it is not a model you have to accept. It is **four named failure modes with four named causes**, and every one of them is decided by how you set up the generation — before you spend anything.

Sources: [ApiPass — How to Solve GPT Image 2 Artifacting Issues](https://apipass.dev/blogs/how-to-solve-gpt-image-2-artifacting-issues), [ApiPass — The Artifact Issue: Reasons and Solutions](https://apipass.dev/blogs/gpt-image-2-launch-tiling-texture-artifact), [ApiPass — Leftovers from Previous Chat Images](https://apipass.dev/blogs/gpt-image-2-artifacting-previous-image-ghosting), [Rewarx — Fixing Artifacts & Noise for Ecommerce](https://www.rewarx.com/blogs/chatgpt-image-2-artifacts-noise-issues-guide), [Rewarx — Product Consistency Issues](https://www.rewarx.com/blogs/gpt-image-2-product-consistency-issues).

Written against GPT Image 2's documented behaviour, but the mechanics — subject risk, style conflict, context bleed, quality tier — are general. Verify the specifics on your host and this month's model (`model-routing.md` §5).

---

## 1 · The four failure modes

Name the mode before you fix anything. The fixes do not transfer between modes — re-rolling a style conflict forever will never clear it, and sharpening a prompt will never clear context bleed.

| # | Mode | What you see | Root cause | Fix lives in |
|---|------|--------------|------------|--------------|
| **A** | **Texture dissolution** | Noise clusters, Voronoi cells, webbing, netting over fine repeating structures | The subject demands fine repeating/organic micro-detail at scale | §2 + §3 |
| **B** | **Style collision** | Incoherent, muddy, noisy output that matches neither descriptor | Two style descriptors that cannot physically coexist | §4 |
| **C** | **Context bleed / ghosting** | Faint shapes, colours or objects from an earlier image in this session | The editing memory that makes in-chat refinement work, firing unintentionally | §5 |
| **D** | **Quality-tier grime** | Softness, mush, dirty edges, weak transparency | Draft-tier quality settings used for a final asset | §6 |

> **Diagnostic order.** Always ask §5 first — *was this the first image in the session?* The majority of artifact-filled outputs come from mode C, and mode C is invisible in the prompt. A perfect prompt on generation six still produces a dirty image.

---

## 2 · Mode A — the high-risk subject register

These subjects tend to dissolve into noise clusters, Voronoi cells or webbing. This is the broadest and most commonly reported class. **Recognise them at brief intake (SKILL.md step 1), not after the render.**

**Natural environments** — forests, dense foliage, grass at scale, water surface detail, fog, smoke, clouds, rain, snowfall, sand, gravel.

**Fantastical / particulate lighting** — glowing particles, embers, sparks, sparkle, bokeh swarms, dust motes, magical glow, light-shafts full of debris. *(Most of these are already banned by R05 as slop. Mode A is a second, independent reason to cut them.)*

**Surfaces with inherent micro-repetition** — animal fur, feathers, scales, chainmail, knitwear and fabric weaves, lace, mesh, wicker, rust, cracked earth, brick and stone courses, dense foam, crumb structure, sesame seeds, herbs and micro-garnish scattered at scale.

### Why this matters to *this* skill

The high-risk register is not exotic — it is **half the commercial briefs in this repo**:

| Brief | The mode-A trap |
|-------|-----------------|
| Food / restaurant | Sesame and poppy seeds, herb scatter, crumb, char blistering, batter, salad leaves, foam, condensation fields |
| Fashion / apparel | Knit, weave, lace, tweed, denim texture, faux fur, sequins |
| Hotel / venue | Foliage, gravel drives, thatch, stonework, sea surface, roof tiles |
| Home & garden | Lawn, hedging, gravel, decking grain, brickwork, wicker |
| Pets | Fur — the single highest-risk commercial subject |
| Jewellery / beauty | Glitter, sparkle, micro-texture on skin, powder |

Do not conclude "avoid these industries". Conclude: **on these briefs, apply §3 before writing the prompt.**

---

## 3 · Mode A fixes — bound the detail, don't ask for more of it

### 3a · Write the prompt as a layout specification

The single highest-leverage change. **Describe the scene as discrete, bounded parts — not as a holistic atmosphere.** A prompt that builds upon itself renders clean; a prompt that competes with itself renders noise.

Atmospheric prompting hands the model an unbounded field of micro-detail to invent. Bounded prompting tells it where each thing starts and stops.

| ❌ Holistic / atmospheric | ✅ Bounded / layout specification |
|---------------------------|-----------------------------------|
| "a magical forest full of glowing particles and lush detail" | "three birch trunks in the left third, sharp; an even mid-grey haze behind them; the ground plane clean and out of focus" |
| "a cosy knitted jumper, ultra-detailed, rich texture everywhere" | "the jumper fills the lower two-thirds; cable knit readable only along the sleeve cuff in the foreground; the body of the jumper soft and out of focus" |
| "a rustic table covered in fresh herbs and seeds" | "one plated dish centred, sharp; a clean matte oak surface around it; no scattered garnish outside the plate" |

This is already the skill's house style — the 11-part prompt architecture (`R25`) and the percentage-based `COMPOSITION` slot in [`prompt-library.md`](prompt-library.md) are layout specifications by construction. **Mode A is the reason that architecture is not optional on a high-risk subject.**

### 3b · Put the detail in one place and defocus the rest

Give the fine texture **one small sharp zone** and take it away everywhere else. This is not a compromise — it is what `R10` (think like a photographer) and `R11` (build depth) already require. A 50mm at f/2.2 gives one sharp plane; the model then only has to resolve micro-detail in that plane.

- Name the **one** surface allowed to carry readable micro-texture.
- Name what is **soft, even, or out of focus** — explicitly, not by omission.
- Keep negative space genuinely empty (`R08`). An empty area cannot artifact.

### 3c · Name the material, don't name the density

"Ultra-detailed", "intricate", "hyper-detailed", "rich texture", "8k detail" are **requests for unbounded micro-repetition**. They are the direct trigger for mode A. Cut them.

Replace them with the physical description the material actually needs (`R09` / `MATERIALS` slot): "brushed steel with a visible grain direction", "char blistering on one edge of the flatbread", "matte wool". A named material renders; a density adjective dissolves.

### 3d · Negative constraints — say what must not be rendered

Explicitly telling the model what *not* to render produces meaningfully cleaner results. Append to the `CONSTRAINTS` slot on any mode-A brief:

```
STRICTLY NO cellular texture, NO webbing, NO netting, NO neural-network
patterns, NO repeating Voronoi patterns, NO noise clusters, NO tiled or
repeating texture fills, NO speckled grain across flat surfaces.
```

This block is a **constraint, not a style cue** — it belongs in `CONSTRAINTS` with the rest of the negatives (`R25`), never in the scene description.

### 3e · Composite instead of asking for everything at once

If the brief genuinely needs a busy field *and* a clean hero, generate them separately: **product on a clean background first, then bring the busy element in as a second step.** Two clean renders composited beat one render that had to resolve both. This is the same Mode B (deterministic composition) route the skill already prefers when fidelity matters (`R18`).

---

## 4 · Mode B — style collision

When a prompt carries two style descriptors that cannot coexist, the model **does not pick one and discard the other — it tries to satisfy both at once**, and the unresolved conflict surfaces as artifacting. The canonical example: *"Impressionist style, ultra-detailed textures"* — two descriptors that are each other's opposite, leaving the model nowhere coherent to go.

**The test:** could a single human artist, in a single medium, produce both at once? If not, it is a collision.

| Collides — pick one | Combines cleanly — shares a visual logic |
|---------------------|------------------------------------------|
| Impressionist + ultra-detailed | Oil painting + hyper-realism |
| Minimalist + maximalist ornament | Watercolour + impressionism |
| Flat vector + photorealistic depth of field | Pixel art + vaporwave |
| Soft-focus dreamy + razor-sharp macro | Film photography + documentary realism |
| Matte print + glossy hyperreal render | Studio product photography + high-key commercial |

Styles that share a common visual logic can be combined freely and **often produce better results than either style alone** — this is a creative tool, not just a hazard to avoid.

**A second, quieter collision source:** obscure or non-standard style references. A style that isn't well represented in training data leaves the model unable to resolve the specification, and it falls back to degraded output. If a named style, movement or studio is niche, **describe its visual mechanics instead of naming it** — light, palette, contrast, grain, framing. This is what `R09`/`R10` already ask for, and it is more reliable than a name in every case.

> Cross-check the `BRAND MOOD` slot (`R25`) too: three adjectives that pull against each other are a style collision wearing a marketing hat.

---

## 5 · Mode C — context bleed (the biggest cause, and the easiest fix)

**The mechanism.** Modern image models are built for in-chat editing, which requires the model to remember what a prior image looked like. That memory is the same mechanism that produces unintentional ghosting. It is a systematic bleed of visual tokens from prior turns — not a glitch.

**The observed pattern.** The first image in a session is almost always clean. Quality degrades with each subsequent generation in that session. The effect compounds. The vast majority of artifact-filled images come from exactly this cause — and it holds **even when the prompts are completely unrelated subjects**.

### The rules

1. **One fresh session per image generated from scratch.** Not per campaign, not per client — per image.
2. **Never reuse a conversation across unrelated generations.** Different subject is not protection.
3. **Iterating? Open a new session and regenerate from a refined prompt** — do not keep adjusting the same image in the same thread. This inverts the instinct: the fix for a nearly-right image is a better prompt in a clean room, not another nudge in a dirty one.
4. **Deliberate editing is the one exception.** When you *want* the model to hold the previous image — a genuine edit of that exact asset — the memory is the feature. Stay in the session, do the edit, and stop. Then leave.
5. **At scale, prefer the API to the chat interface.** Each API call is an independent request where you control exactly what context is passed in, so cross-image bleed is meaningfully lower. For any campaign that ships a set (`R20`, `R35`), this is the default route.

### What this changes in this skill's workflow

`R34` already demands **one finished ad per generation**. Mode C extends it: **one finished ad per *session*.** A variation matrix of three variants (`R35`) is three clean sessions, not three turns in one — and that is also what protects series consistency (`R20`), since a ghosted variant will not match its siblings.

> **Symptom check.** If an output carries a shape, colour cast or object you never asked for, and you cannot find it in your prompt — stop debugging the prompt. Check what you generated earlier in that session.

---

## 6 · Mode D — quality tier and settings

Before blaming the prompt, check the request settings.

- **Low quality is for drafts and iteration only** — never for a final product shot or a campaign asset. Switching from low to medium/high is the first move when output looks noisy, soft or dirty.
- **Transparent backgrounds need medium or high.** This matters directly for e-commerce packshots and any cut-out product asset.
- **Draft cheap, ship high.** Validate the angle at low tier (which is exactly the "generate small first" discipline in [`model-routing.md`](model-routing.md) §1), then re-render the winner at high. Do not ship the draft.
- **Grime, tiling and reference carryover are not quality-parameter problems.** If raising the tier doesn't clear it, you are in mode A, B or C — go back to §1 and re-diagnose.

---

## 7 · Reference-image discipline (e-commerce & brand consistency)

The same model that artifacts textures also drifts products. Both are anchoring problems.

**Why products drift.** The model has no explicit rule set for your brand aesthetic, so it interprets the same prompt multiple ways — subtle differences in tone, shadow direction, background texture. Across a catalogue this reads as a fragmented storefront and it costs shopper trust.

**Anchor with references, but not with too many.**

- Use **2–3 strong references, maximum.** More references create conflicting instructions — the reference-set version of a style collision (§4).
- **Label every reference's role** (`R03`): subject / source of truth vs. style only. An unlabelled reference is an invitation to blend.
- Anchor the **specifics**, not the vibe: exact brand colour values, an approved lighting reference, an approved background treatment, an approved packshot.
- **Reduce interpretation room** with concrete material, lighting and camera description. Every ambiguity you leave is a decision the model makes differently next time.

**Generate options, then select.** On a high-risk subject, render several variants and ship the one with the fewest artifacts. This is a *selection* step, not a re-roll — it does not license iterating in a dirty session (§5).

**Document the anchors.** Write the chosen references, colour values and lighting setup into the client folder (SKILL.md step 6). Undocumented references get picked informally, and informal selection is how a brand drifts across a catalogue over months.

---

## 8 · Repair vs. regenerate

Once an artifact is in a finished render, the fix depends on its size. **Match the tool to the damage** — the efficient workflow is hybrid.

| Damage | Do this |
|--------|---------|
| **Major** — garbled background, wrong proportions, extra limbs/fingers, dissolved subject | **Regenerate.** Faster and better than repair. Fix the prompt first (§3/§4) and start a clean session (§5) |
| **Minor** — one small texture anomaly, a local blemish, a soft patch | **Repair locally.** Mask the area and regenerate only those pixels, so the rest of the approved image is untouched |
| **Soft / undefined detail from low resolution** | **Upscale** — this smooths noise and resolves undefined detail. It does not remove structural artifacts |
| **Anything touching the product itself** | **Regenerate.** Never repair a product into being "close enough" — `R03` is absolute |

> **Upscaling is not artifact removal.** It makes a clean image bigger and a webbed image bigger and webbed. Diagnose first.

---

## 9 · Artifact QA — what to look for

Artifacting is one of the few failure modes a deterministic script genuinely cannot call: **sensor grain, fabric weave and Voronoi webbing all read as high-frequency energy**, so any threshold strict enough to catch webbing rejects legitimate photography. That is why there is no `qa.py` check for it — it belongs to the vision pass ([`qa-gate.md`](qa-gate.md) §2), inspected at 100%.

Inspect **at full resolution, not at thumbnail size.** Artifacting hides at 150px and is the first thing a client sees at 100%. Check, in order:

1. **Every fine-texture surface** — fur, knit, foliage, crumb, stone, hair. Cells, webbing or netting where there should be material.
2. **Flat surfaces** — walls, skies, panels, seamless backgrounds. Speckle or tiling on a surface that should be even.
3. **Transitions** — where a busy field meets a clean one. Artifacts collect at the boundary.
4. **Anything you did not ask for** — a shape, object or colour cast with no line in the prompt behind it. That is mode C; check the session, not the prompt.
5. **Repeating structure** — the same patch of texture recurring across the frame at a regular interval.
6. **The product against its reference** (`R03`) — shape, proportion, colour, construction, lettering. Drift is an artifact too, and the most expensive one.

**Hard fail:** visible cellular/webbing/noise-cluster texture anywhere in the frame, a tiled or repeating texture fill, or any un-briefed element traceable to a previous generation. These are not "acceptable at this budget" — they are the single clearest tell that an ad was machine-made, which is the one thing this whole skill exists to prevent (`R05`).

---

## 10 · Pre-flight checklist

Run before spending anything on a commercial visual (SKILL.md step 4):

- [ ] **Mode A screen** — does the brief contain a high-risk subject (§2)? If yes: bounded layout prompt (§3a), one sharp zone (§3b), materials not density adjectives (§3c), negative-constraint block (§3d).
- [ ] **Mode B screen** — do any two style descriptors collide (§4)? Could one artist in one medium produce both? Is any named style obscure enough to need describing instead?
- [ ] **Mode C screen** — is this a **fresh session**? Am I generating exactly one image in it?
- [ ] **Mode D screen** — is the quality tier right for the deliverable, not for the draft?
- [ ] **References** — 2–3 maximum, each with a labelled role, anchoring specifics not vibes (§7).
- [ ] **Post-render** — inspected at 100% against §9 before it enters the QA gate.
