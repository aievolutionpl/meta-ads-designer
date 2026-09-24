# Model-independent advertising prompts

Use after choosing a direction in [art-direction.md](art-direction.md). This translates R25 and R42–R44 into one usable production instruction.

## 1 · Compile decisions, not the whole rulebook

Keep the brief and reasoning outside the generator prompt. Include only decisions the image maker needs. No model names, invented parameters, magic quality phrases or exhaustive negative lists.

The existing eleven R25 fields remain the semantic checklist. They may be combined into natural prose. For typography or illustration, replace irrelevant camera/material instructions with graphic form and type instructions.

A final prompt should specify:
1. Deliverable: finished ad or image background, ratio and intended placement.
2. Communication: the single message and visual mechanism.
3. Source roles: what to preserve, what is only a style reference.
4. Art direction: medium and visible stylistic properties.
5. Composition: dominant element, reading order, copy field, quiet space.
6. Typography and copy: exact strings, line breaks, role, alignment, prominence.
7. Colour and finish: palette roles; light/materials only where relevant.
8. Constraints: facts and identity to preserve, plus a few likely failure modes.

If the request is prompt-only, return the ready-to-paste prompt with a short production note where needed. Do not demand image tools, run pixel QA or claim that an unseen image passes. If the request includes image generation, use available tools and inspect the result.

## 2 · Choose the text contract

**Finished ad with generated text:** quote every intended string, declare no other copy, specify hierarchy and line breaks. Use for short copy when the available renderer can handle it. Inspect the actual lettering afterwards.

**This is the default (R50):** the model renders the complete ad, text included. Describe type by class, weight, width, case and position ("heavy condensed grotesk, all caps, upper left, two lines"). Font names state intent only.

**Graphic/type-led composition:** the headline itself may be the hero. Specify the grid, the words, the weight contrast and the one supporting device, and let the model render the whole poster.

**Text-free image plus separate typesetting** exists only when the user explicitly asks for it. Otherwise fix text errors with a regeneration or a targeted model edit.

## 3 · Prompt preflight

Check before sending:
- No unresolved placeholders in a final prompt.
- One deliverable, one chosen visual direction and one message.
- No unsupported offer facts or assets claimed as attached when absent.
- Headline and support fit the declared number of lines.
- Hero, copy and logo do not compete for the same region.
- Instructions agree: not “no text” and “render headline”; not “flat poster” and “photographic depth”.
- Constraints target this image, not every possible artifact.
- No claim that named fonts, exact pixels, spelling or identity are guaranteed by prompting.

If facts are missing, omit them or request them; do not put plausible invented facts in a production prompt.

## 4 · Revision by diagnosis

| Observation | Change in the next instruction |
|---|---|
| Attractive but generic | Replace the generic setting with a specific use moment or brand device |
| Unclear offer | Resolve the takeaway and headline before changing the lighting |
| Busy hierarchy | Remove a secondary idea; enlarge one focal element; consolidate details |
| Copy unreadable | Shorten copy or reserve a larger calm field; typeset separately if needed |
| Looks pasted together | Align image direction, type edges, colour roles and spacing |
| Product drift | Reassert source identity and narrow the edit; consider source compositing |
| Wrong style | Describe visible formal properties, not more mood adjectives |

Keep successful decisions. Judge the revision against the original brief and reference, not just the previous attempt.

