# 🧬 Artifact Control — keeping the render clean

> The operating tool behind **R40** (clean renders) and **R41** (minimal effective edit). Every other rule in this skill assumes the render came back clean. This one is about the renders that don't: the cellular webbing across a knitted jumper, the noise clusters in the foliage, the faint ghost of the last image bleeding into this one, the product that quietly changed shape on generation four.
>
> Artifacting is not bad luck and it is not a model you have to accept. It is **eight named failure modes with eight named causes** — four from how you ask for a new image, four from how you ask to change an existing one — and every one of them is decided at setup, before you spend anything.

Sources: [ApiPass — How to Solve GPT Image 2 Artifacting Issues](https://apipass.dev/blogs/how-to-solve-gpt-image-2-artifacting-issues), [ApiPass — The Artifact Issue: Reasons and Solutions](https://apipass.dev/blogs/gpt-image-2-launch-tiling-texture-artifact), [ApiPass — Leftovers from Previous Chat Images](https://apipass.dev/blogs/gpt-image-2-artifacting-previous-image-ghosting), [Rewarx — Fixing Artifacts & Noise for Ecommerce](https://www.rewarx.com/blogs/chatgpt-image-2-artifacts-noise-issues-guide), [Rewarx — Product Consistency Issues](https://www.rewarx.com/blogs/gpt-image-2-product-consistency-issues).

Written against GPT Image 2's documented behaviour, but the mechanics — subject risk, style conflict, context bleed, quality tier, edit scope — are general. Verify the specifics on your host and this month's model (`model-routing.md` §5).

---

## 1 · The failure modes

Name the mode before you fix anything. The fixes do not transfer between modes — re-rolling a style collision forever will never clear it, and sharpening a prompt will never clear context bleed.

There are two families. **Generation artifacts (A–D)** come from how you asked for a new image. **Edit artifacts (E–H)** come from how you asked to change an existing one, and they are the ones that bite hardest in production, because most commercial work is editing.

### Generation artifacts

| # | Mode | What you see | Root cause | Fix |
|---|------|--------------|------------|-----|
| **A** | **Texture dissolution** | Noise clusters, Voronoi cells, webbing, netting over fine repeating structures | The subject demands fine repeating/organic micro-detail at scale | §2 + §3 |
| **B** | **Style collision** | Incoherent, muddy output that matches neither descriptor | Two style descriptors that cannot physically coexist | §4 |
| **C** | **Context bleed / ghosting** | Faint shapes, colours or objects from an earlier image in this session | The editing memory that makes in-chat refinement work, firing unintentionally | §5 |
| **D** | **Quality-tier grime** | Softness, mush, dirty edges, weak transparency | Draft-tier quality settings used for a final asset | §6 |

### Edit artifacts

| # | Mode | What you see | Root cause | Fix |
|---|------|--------------|------------|-----|
| **E** | **Reference drift** | The room, face, layout or product changed when you only asked for one thing | No preservation contract — silence reads as permission | §7 + §8 |
| **F** | **Edge halo / bleed** | A glow, seam or smeared boundary around the edited object; texture leaking across it | The edit was too large to integrate, or lighting wasn't held | §7 |
| **G** | **Duplication / warping** | A second copy of an object, melted geometry, impossible reflections | The model re-solved a region it should have preserved | §7 |
| **H** | **Overload** | A busy, cluttered image with no hero left | Several visual ideas were requested at once | §7 |

> **Diagnostic order.** Ask §5 first — *was this the first image in the session?* Mode C is the single largest cause and it is invisible in the prompt; a perfect prompt on generation six still produces a dirty image. Then ask §7 — *did I actually say what to preserve?*

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

**Use only the negatives the scene can actually produce.** A prompt carrying every possible constraint dilutes the ones that matter and spends attention on hazards that were never in the frame — there is no point banning malformed hands in a packshot with no people. Pick the block that fits the subject: texture negatives for fine-detail scenes, geometry and boundary negatives for edits (§7), anatomy negatives only when there is a person.

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

### The rule — one concept, one image family

The blunt version ("never generate twice in a session") is wrong, because it forbids the legitimate case: iterating on the image you just made. The accurate rule is **one concept = one image family = one session.**

A **same-family** turn is a direct iteration of the concept already on screen. Stay in the session:

> change the camera angle · change the lighting · fix the text · remove one object · replace one product · adjust framing · improve realism · polish quality

A **new-family** turn is a different concept wearing the same conversation. Open a fresh session:

> an entirely new scene · a new advertising concept · a different room · a new campaign direction · a different composition · a different visual story

**The failure everyone hits is running a new family inside an old one** — a new subject, a new campaign, a new room, in the thread that already made three images. Different subject is *not* protection; unrelated prompts ghost each other just as readily.

Four rules follow:

1. **One concept per session.** Not per campaign, not per client — per concept.
2. **Same-family iteration is allowed, but it is not free.** Each turn costs a little cleanliness. Keep families short, and when the image is nearly right but the *prompt* was wrong, refine the prompt and open a clean session rather than nudging a dirty one.
3. **A new family always gets a new session**, restating only the current concept and the references it actually needs.
4. **At scale, prefer the API to the chat interface.** Each API call is an independent request where you control exactly what context is passed in, so cross-image bleed is meaningfully lower. For any campaign that ships a set (`R20`, `R35`), this is the default route.

### What this changes in this skill's workflow

`R34` already demands **one finished ad per generation**. Mode C extends it: **one concept per session.** A variation matrix of three structurally different variants (`R35`) is three families, so three clean sessions — never three turns in one. That is also what protects series consistency (`R20`): a ghosted variant will not match its siblings.

> **Symptom check.** If an output carries a shape, colour cast or object you never asked for, and you cannot find it in your prompt — stop debugging the prompt. Check what you generated earlier in that session.

---

## 6 · Mode D — quality tier and settings

Before blaming the prompt, check the request settings.

- **Low quality is for drafts and iteration only** — never for a final product shot or a campaign asset. Switching from low to medium/high is the first move when output looks noisy, soft or dirty.
- **Transparent backgrounds need medium or high.** This matters directly for e-commerce packshots and any cut-out product asset.
- **Draft cheap, ship high.** Validate the angle at low tier (which is exactly the "generate small first" discipline in [`model-routing.md`](model-routing.md) §1), then re-render the winner at high. Do not ship the draft.
- **Grime, tiling and reference carryover are not quality-parameter problems.** If raising the tier doesn't clear it, you are in mode A, B or C — go back to §1 and re-diagnose.

---

## 7 · Modes E–H — the edit artifacts

**The core principle of every edit: preserve what already works, change only what was requested.**

Most commercial image work is not generation, it is editing — swap this product into that room, change the background behind this person, relight this scene. The dominant failure is not a dirty texture. It is **the model rebuilding things nobody asked it to touch**, because an edit instruction with no preservation contract reads as a licence to re-solve the whole frame.

| | Asked for | Got back |
|---|---|---|
| ❌ | "replace the stove" | a redesigned room, moved furniture, new flooring |
| ❌ | "change the clothing" | a different face |
| ❌ | "improve the lighting" | a new composition |
| ✅ | "replace the stove" | the same room, one new stove, matched shadows |

### E · Reference drift

The room, face, layout, proportions or product changed alongside the thing you asked for. **Cause: silence.** Anything you did not explicitly protect is fair game — the model has no way to know that the flooring was load-bearing to the brief.

**Fix:** write the preservation contract (§8). Then shrink the edit: one element per turn, not four.

### F · Edge halo and texture bleed

A glow, dark seam or smeared boundary rings the edited object; texture leaks across the join; the object looks pasted rather than photographed.

**Fix:** reduce the *scale* of the edit — a smaller ask integrates better than a large one. Then say what the boundary must do: hold the original lighting and background, and give the object **real contact shadows and reflections consistent with the scene's existing light direction**. An object with no contact shadow always reads as a sticker (`R04`).

### G · Duplication and warped geometry

A second copy of an object appears, geometry melts, reflections become impossible, hands gain fingers. The model re-solved a region it should have left alone.

**Fix:** name the geometry as protected (§8), and add only the relevant negatives: `no duplicated objects, no warped geometry, no melted edges, no impossible reflections`. If it persists, the edit is too big — split it into two turns.

### H · Overload

The image came back busy: several ideas competing, no hero left, decorative elements nobody briefed.

**Fix:** this is `R06` (one creative = one idea) failing at the edit layer. Strip the secondary ideas and return to one hero, one environment, one message. Every additional simultaneous change also multiplies the risk of E, F and G.

---

## 8 · The preservation contract

**Every edit prompt carries two slots that generation prompts don't need:** what changes, and what must not. Never write one without the other — an `EDIT INSTRUCTIONS` slot with no `PRESERVE` slot is how mode E happens.

```
EDIT INSTRUCTIONS: [the one thing that changes]
PRESERVE:          [everything that must survive untouched]
```

### Copy-paste preservation blocks

**Scene / interior:**

> Preserve the original room layout, architecture, proportions, furniture placement, flooring, camera position and perspective. Change only the [element].

**Faces and people:**

> Preserve facial identity, bone structure, proportions, age, skin features and expression. Do not redesign the face.

**Products:**

> Preserve the exact product geometry, proportions, materials, branding and recognisable design details. Use the supplied product reference as the dominant visual anchor.

**Integration** — pair with any of the above when placing an object into an existing scene:

> Match the object's scale, perspective, contact shadows and reflections to the existing scene. Integrate the boundary cleanly with no halo, glow or texture bleed.

### The default preserve-list

Unless the brief explicitly says otherwise, these survive every edit: room layout · architecture · proportions · subject identity · facial features · product shape · product branding · furniture placement · camera orientation · the overall visual logic of the frame.

### Edit priority order

When an edit involves judgement, resolve in this order. **Reference accuracy outranks creative improvement** — always.

1. Preserve identity and composition
2. Make the requested change
3. Match lighting and perspective
4. Repair edge integration
5. Improve realism
6. Remove artifacts
7. Polish

An edit that made the picture *nicer* while losing the room is a failed edit, not a bonus.

---

## 9 · Reference-image discipline (e-commerce & brand consistency)

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

## 10 · Repair vs. regenerate

Once an artifact is in a finished render, the fix depends on its size. **Match the tool to the damage** — the efficient workflow is hybrid.

| Damage | Do this |
|--------|---------|
| **Major** — garbled background, wrong proportions, extra limbs/fingers, dissolved subject | **Regenerate.** Faster and better than repair. Fix the prompt first (§3/§4) and start a clean session (§5) |
| **Minor** — one small texture anomaly, a local blemish, a soft patch | **Repair locally.** Mask the area and regenerate only those pixels, so the rest of the approved image is untouched |
| **Soft / undefined detail from low resolution** | **Upscale** — this smooths noise and resolves undefined detail. It does not remove structural artifacts |
| **Anything touching the product itself** | **Regenerate.** Never repair a product into being "close enough" — `R03` is absolute |

> **Upscaling is not artifact removal.** It makes a clean image bigger and a webbed image bigger and webbed. Diagnose first.

---

## 11 · Failure recovery — symptom to remedy

Read the symptom, apply the named remedy. Do not re-roll blind: none of these clear by chance.

| Symptom | Mode | Remedy |
|---------|------|--------|
| Worms, cells, webbing, strange micro-texture | A | Cut unnecessary high-frequency detail (fog, particles, glitter, foliage, grain, repeating pattern). Add the anti-cellular constraint block (§3d). Bound the detail to one surface |
| Muddy render matching neither style asked for | B | Two colliding descriptors. Pick one and regenerate — re-rolling cannot resolve it (§4) |
| Ghost objects, un-briefed shapes or colour casts | C | Start a fresh session. Restate only the current concept and the references it needs (§5) |
| Soft, dirty, mushy final asset | D | Raise the quality tier. If it doesn't clear, re-diagnose — you are in A, B or C (§6) |
| The room / scene changed far too much | E | Add the scene preservation block. Name architecture, layout, furniture, perspective and framing as protected; change only [X] (§8) |
| Product shape or proportions changed | E | State that exact geometry and proportions must be preserved; make the product reference the dominant anchor. Never accept a drifted product — `R03` is absolute |
| Face changed identity | E | Add the face preservation block. Split the edit so identity and wardrobe never change in the same turn (§8) |
| Halo or glow around the edited object | F | Shrink the edit. Explicitly preserve the original lighting and background, and request clean boundary integration with real contact shadows (§7) |
| Object looks pasted on | F | Ask for matched scale, perspective, contact shadows and reflections consistent with the scene's existing light |
| Duplicated object or melted geometry | G | Name the geometry as protected; add only the relevant negatives. If it persists, split the edit into two turns (§7) |
| Image became busy, no hero left | H | Remove the secondary visual ideas. One hero, one environment, one message (`R06`) |

> **The meta-remedy: make the ask smaller.** Modes E through H are all, at bottom, one failure — too much requested in one turn. Two clean edits beat one ambitious one, every time.

---

## 12 · Artifact QA — what to look for

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

## 13 · Pre-flight checklist

Run before spending anything on a commercial visual (SKILL.md step 4):

- [ ] **Mode A screen** — does the brief contain a high-risk subject (§2)? If yes: bounded layout prompt (§3a), one sharp zone (§3b), materials not density adjectives (§3c), negative-constraint block (§3d).
- [ ] **Mode B screen** — do any two style descriptors collide (§4)? Could one artist in one medium produce both? Is any named style obscure enough to need describing instead?
- [ ] **Mode C screen** — is this concept its own **image family** in a fresh session (§5)?
- [ ] **Mode D screen** — is the quality tier right for the deliverable, not for the draft?
- [ ] **References** — 2–3 maximum, each with a labelled role, anchoring specifics not vibes (§9).
- [ ] **Post-render** — inspected at 100% against §12 before it enters the QA gate.

**If this is an edit rather than a new image, add:**

- [ ] **Is this one concept, or several?** One element changes per turn. Several changes at once is how E, F, G and H all arrive together (§7).
- [ ] **Is the `PRESERVE` slot written?** An `EDIT INSTRUCTIONS` slot without one is an open licence to redraw the frame (§8).
- [ ] **Is integration specified?** Scale, perspective, contact shadows and reflections matched to the existing scene — or the object ships as a sticker.
- [ ] **Same image family?** A direct iteration stays in the session; a new concept opens a fresh one (§5).
