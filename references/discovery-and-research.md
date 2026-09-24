# Discovery and research before generation

> The operating tool behind **R51**. A generated ad is only as good as the prompt, and the prompt is only as good as what the agent knows. Before the first generation, the agent researches and asks a few sharp questions. Then it writes the prompt, generates with an image model and analyses the result.

The order is fixed: **research → questions → decision note → prompt → generate → analyse → refine.**

---

## 1 · Research first, so the questions are smart

Do this before asking anything, with whatever tools the host has (web search, fetch, browser, the user's files). Spend minutes, not hours.

| Look at | To learn |
|---|---|
| The brand's website, Instagram and Facebook page | Real products, prices, tone of voice, palette, typefaces, photography style, existing claims |
| Meta Ad Library (brand name, then 2–3 competitors, same country) | What the category already runs, which ads have run longest (the strongest signal), which formats and hooks are overused |
| Competitors' feeds and top posts | Where the visual gap is: what nobody in the niche does |
| Reviews (Google, Booking, marketplace) | The customer's own words: real benefits, objections and proof you may quote with permission |
| Seasonal and local context | Dates, weather, holidays and local events that make the ad current |
| Current style references (Behance, Dribbble, Pinterest) | A visual language to borrow in principle ([style-atlas-2026.md](style-atlas-2026.md) §6) |

Write the findings as a short **research note**: 5–8 bullets, each ending with its implication for the ad. Example: "Every competitor shows a plated dish on dark wood → our gap: hands and preparation in daylight."

If research tools are unavailable, say so and rely on the questions.

## 2 · Ask a few questions, once

Ask **3–6 questions in one message**, only what research could not answer and what would change the prompt. Offer a recommended default for each, so the user can reply "ok" or just a letter. Never interrogate: one round, then proceed with stated assumptions.

Pick from this bank by what is actually unknown:

**Offer and proof**
1. What exactly are we promoting, and is there a verified offer (price, discount, deadline)? *Default: no offer, a benefit-led ad.*
2. What proof can we show: a number, real reviews, the founder, a before/after? *Default: none; lead with the product.*

**Audience and moment**
3. Who is it for, and at what moment do they see it: first contact (cold) or people who already know you (retargeting)? *Default: cold, broad local audience.*
4. What stops them from buying today: price, trust, "not now", not knowing you? *Default: not knowing you.*

**Visual and brand**
5. Which style is closer: A) bold and loud, B) calm and premium, C) natural "shot on a phone", D) graphic/typographic? *Default: from the research, stated.*
6. Do you have a product photo, logo or venue photos to use as references? Which must be kept exactly? *Default: generate the scene; use the logo as a reference only if supplied.*
7. Brand colours or fonts that must appear, or anything that must never appear? *Default: palette taken from the website.*

**Delivery**
8. Placements: feed 4:5, Reels/Stories 9:16, or both? How many concepts? *Default: 4:5, three distinct concepts.*
9. Language and exact headline, or should I write it? *Default: I write it in the brand's language.*
10. Which image model or tool do you use (Codex, an API model, another app)? *Default: the one available in this session.*

Skip a question when the brief, the files or the research already answer it. A user who says "just do it" gets zero questions and a visible list of assumptions.

## 3 · The decision note (before any prompt)

Compress research and answers into one block the user can approve at a glance:

```
BRIEF      : product · offer (verified?) · audience + moment · objection
INSIGHT    : one line from research, e.g. the visual gap in the niche
CONCEPTS   : 1) persona · hook · format · style
             2) …   3) …   (distinct per R47)
REFERENCES : image A = exact product · image B = logo · style = named language
COPY       : exact headline / subline / CTA per concept, in the ad's language
OUTPUT     : model · ratio(s) · number of variations per concept
```

For a single quick ad, the note can be three lines. For a campaign, show it and wait for a yes before generating many images.

## 4 · After generation: analyse, don't admire

For every image, report in this order:
1. **Transcribe** every word visible in the image and compare it with the approved copy (spelling, diacritics).
2. **Fidelity:** does the product, logo or venue match the reference?
3. **Thumbnail test:** at phone size, what is seen first, second and third?
4. **Idea:** can someone say what is advertised in one second?
5. **Defects:** hands, physics, texture artifacts, invented text or UI ([qa-gate.md](qa-gate.md)).
6. **Verdict and one change:** ship, or name the single decision the next generation changes (R41, R49).

Regenerate with a corrected prompt; do not fix a generated ad by drawing over it with code (R50).
