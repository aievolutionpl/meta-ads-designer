# Model Routing & Cost Discipline

> The operating tool behind **R39 (routing)** and the cost side of the whole skill: decide *which* model, *when*, and *how much iteration is worth* before you spend. A model that is excellent for one job is wrong for another, and blind generation is how budgets leak.

Different generators have different strengths: spelling native text, clean product photography, precise motion, lip-sync, cinematic video. Routing picks the model for the job instead of forcing every brief through one default pipeline.

---

## 1 · Decision before spend

Before generating, answer three questions:

1. **What is the job?** Native in-scene text · clean product photo · video motion · UGC talking-head · re-composition/editing.
2. **Which model is best at that job?** Route by the table below — never by habit.
3. **What is a reasonable iteration budget?** How many attempts before the angle is wrong, not the model? (R35 keeps you from re-rolling the same brief.)

If the brief is new or uncertain, **generate small first**: one finished ad (R34) to validate the angle, then scale.

---

## 2 · Static image routing

| Job | Route to |
|-----|----------|
| **Native in-scene text** (Mode A, R18) | The model best at reliable spelling — keep strings short, QA every variant |
| **Clean product / commercial photo** (Mode B) | A strong photorealism model; compose typography/logo deterministically after |
| **Recomposition / editing** | An editing-capable model working from the reference (R03) |
| **Series consistency** (R20) | One model for the whole set so the product stays identical |

Rule of thumb: a model that renders text well for in-scene headlines; a clean-photo pipeline for everything else. Host-specific install notes: `INSTALL.md`.

---

## 3 · Video / motion routing

| Motion job | Route to |
|------------|----------|
| **Precise product demo** | A model with controlled camera/motion (frame-accuracy matters) |
| **Cinematic, multi-scene story** | A model with smooth transitions and strong scene continuity |
| **UGC / audio-led talking-head** | A model with lip-sync and natural speech timing |
| **Motion from stills** | A frame-accurate pipeline over the stills you already QA'd |

Route per the motion track: [`video-ugc-track.md`](video-ugc-track.md) §5.

---

## 4 · Cost & iteration discipline

- **Validate before you scale.** One finished creative first; a winning direction earns a batch (R35, R37).
- **QA before long renders.** For video, QA the hero frame and first second first — a bad first frame wastes the whole render.
- **Name the cost.** If the platform charges per generation, report the model and the number of generations in the delivery (SKILL.md step 6).
- **Prefer the free/deterministic path when fidelity matters** (Mode B, R18): compose real typography and the official logo deterministically instead of paying for a model to guess at it.

---

## 5 · Fallback when a model under-delivers

- **Spelling fails** → switch to Mode B (deterministic composition) rather than re-rolling a model that can't spell.
- **Product drifts** → strengthen the reference role (R03) or switch to an editing model; do not accept a changed product.
- **Motion is weak** → go back to a strong static hero rather than ship a weak video (R39: static-first).
- **Fatigue / repetition** → the model isn't the problem; re-route to a different generation strategy (new angle, R13) instead of re-rolling the same prompt.

A routing failure is a decision problem, not a coin to keep flipping.
