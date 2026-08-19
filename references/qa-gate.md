# ✅ QA Gate — scored, not vibed

> **A checkbox list gets ticked without anybody looking at the image.** This gate has three layers that each produce evidence: a deterministic script, a structured vision pass, and a scored rubric with a shipping threshold.

**Ship condition: score ≥ 16/20 AND zero hard fails AND `scripts/qa.py` returns PASS.**

Run all three on **every** output. Not on the batch — on every image.

> ⚠️ **A PASS without `--text-box` is a partial PASS.** Four of the seven checks measure the copy block; with no box declared they report `n/a` and the script says so in its output. On any creative that carries text, pass `--text-box` (and `--logo-box` when a logo is placed) or the gate is checking dimensions and seams only.

---

## 1 · Layer 1 — deterministic checks (`scripts/qa.py`)

Things a machine measures better than an eye. No model call, no cost.

```bash
python scripts/qa.py out/ad_01.png --format 4:5 --text-box 86,900,994,1264
python scripts/qa.py out/ad_01.png --format 4:5 --text-box 86,900,994,1200 \
                                   --logo-box 780,1210,994,1264
python scripts/qa.py out/*.png --format 4:5 --contact-sheet out/_contact.png
```

The script's own behaviour is covered by `python scripts/test_qa.py` — thirteen
synthetic cases asserting that the canonical layouts pass and the known failure
modes fail. Run it after touching `qa.py`.

| Check | Rule | Needs | Fail condition |
|-------|------|-------|----------------|
| `dimensions` | R19 | `--format` | not the declared format's exact resolution |
| `safe_area` | R08 | `--text-box` / `--logo-box` | a declared box crosses the 8% margin, or the 9:16 chrome zones |
| `margin_activity` | R08 | — | **advisory, never fails.** Edge energy in the margin band. A full-bleed photo scores as high as a headline that crosses the margin, so this number tells you to look — `safe_area` is the verdict |
| `contrast` | layout §4a | `--text-box` | < 4.5:1 between the glyph population and the backdrop median inside the box |
| `collage` | R06 | — | a seam runs the full length of the canvas → the model produced a grid |
| `thumbnail` | R33 | `--text-box` | the copy block loses > 60% of its edge energy at 150px |
| `focal_regions` | R07 | — | saliency spread over > 2 strong regions |
| `scrim_uniformity` | layout §3b | `--text-box` | < 85% of the backdrop under the copy sits in one tight luminance band (a busy photo under the text) |

Output is JSON, so it drops straight into a report:

```json
{"file":"ad_01.png","verdict":"PASS","checks":{"dimensions":"1080x1350 ok",
 "safe_area":"clear (margin 86px, keep-out 86-1264px)",
 "margin_activity":"0.04% (quiet)","contrast":6.8,"collage":false,
 "thumbnail":0.81,"focal_regions":1,"scrim_uniformity":0.94},"failed":[]}
```

---

## 2 · Layer 2 — the vision pass (copy-paste prompt)

Send the image to a vision model with **this exact prompt**. Structured output is the point: it forces the model to look rather than agree.

````
You are the QA art director for a paid advertising campaign. Inspect the attached
ad image against the rules below. Be adversarial — your job is to find reasons to
reject it, not to be encouraging. If you cannot see something clearly, say so
rather than assuming it is fine.

Reference images supplied with this brief: [list them, or "none"]
Declared copy that should appear on the image:
  brand:    "<BRAND>"
  headline: "<HEADLINE>"
  subline:  "<SUBLINE>"
  cta:      "<CTA>"

Return ONLY this JSON, no prose:

{
  "transcribed_text": ["every string of text you can read on the image, verbatim,
                       including partial or truncated words"],
  "spelling_errors": [{"found": "", "expected": "", "severity": "hard|soft"}],
  "text_matches_declared_copy": true|false,
  "truncated_or_clipped_text": true|false,
  "focal_points": <integer: how many elements compete for first attention>,
  "product_matches_reference": true|false|"no_reference",
  "product_changes_observed": ["shape/color/logo/lettering/mechanism changes"],
  "logo_present": true|false,
  "logo_appears_redrawn": true|false|"unsure",
  "invented_food_or_props": true|false,
  "accent_color_placements": <integer>,
  "text_sits_on_busy_area": true|false,
  "anatomy_errors": ["deformed hands, extra fingers, impossible limbs"],
  "physics_errors": ["floating objects, wrong shadows, missing contact"],
  "slop_tells_present": ["from: neon, glow, glassmorphism, gradient text,
                          floating particles, isometric, HUD, clip-art icons,
                          fake UI, excessive bokeh, plastic surfaces"],
  "ad_spine": {"headline": true|false, "subline": true|false,
               "cta": true|false, "brand_cue": true|false},
  "readable_at_thumbnail": true|false,
  "reads_as_ai_generated": true|false,
  "one_sentence_verdict": "",
  "hard_fails": ["R30-product|R30-logo|R30-text|R30-anatomy|R30-physics|
                  R30-scale|R30-chaos|R30-ui|R30-background|R30-stock|
                  R30-function|R30-overload"],
  "score": {"hierarchy":0-2, "product":0-2, "realism":0-2, "typography":0-2,
            "copy":0-2, "color":0-2, "space":0-2, "logo":0-2,
            "thumbnail":0-2, "idea":0-2},
  "total": <sum, out of 20>
}
````

**Reading the result:**
- Any entry in `hard_fails` → regenerate. Do not retouch.
- `spelling_errors` with `severity: hard` → regenerate (Mode A) or re-render the text layer (Mode B).
- `total < 16` → fix the lowest-scoring criteria and re-run.
- `reads_as_ai_generated: true` with `total ≥ 16` → trust the flag, not the score. Redesign.

---

## 3 · Layer 3 — the scored rubric

Ten criteria, 0/1/2 each. This is what `score` in the vision JSON refers to, and what a human uses when reviewing by eye.

| # | Criterion | 0 — fail | 1 — passable | 2 — good |
|---|-----------|----------|--------------|----------|
| 1 | **Hierarchy** (R07) | two or more elements compete; eye doesn't land | one focal point but weak separation | one obvious focal point in <1s, clear 2nd and 3rd level |
| 2 | **Product / subject** (R02) | small, obscured, or ambiguous | visible but not dominant | large, lit, sharper than surroundings, attractive angle |
| 3 | **Realism** (R04) | wrong physics, deformed anatomy, fake materials | mostly plausible, one soft tell | reads as a real photograph; correct light, shadows, contact |
| 4 | **Typography** (R17, layout §2) | >3 sizes or >2 families; default font; mid-word clipping | correct sizes, unremarkable pairing | named pairing, correct tracking, hierarchy ratio ≥3× |
| 5 | **Copy** (headline-system) | interchangeable headline, banned words, misspelling | specific but long or flat | passes the specificity test; within budget; spine reads as one voice |
| 6 | **Color** (layout §4) | default gradient, >3 accent placements, contrast <4.5:1 | brand palette, contrast ok | brand palette, one accent used ≤3×, deliberate contrast |
| 7 | **Space** (R08) | frame full, elements touching edges | margins present but tight | 8% margins respected, deliberate negative space |
| 8 | **Logo** (R30-logo) | AI-redrawn, distorted, or a text substitute | official file but cramped or low contrast | official file, correct clear space, reads on its backdrop |
| 9 | **Thumbnail** (R33) | headline unreadable at 150px | headline readable, detail lost | full message survives at 150px |
| 10 | **The idea** (R01, R06) | pretty picture, no message | a message, weakly expressed | one idea, expressed visually, would work without the copy |

**Thresholds**
- **≥ 18** — ship.
- **16–17** — ship if the deductions are on criteria 7–9 (fixable in a deterministic pass); otherwise fix.
- **12–15** — fix and re-score. Usually typography or copy.
- **< 12** — regenerate from a new prompt. Don't patch.
- **Any hard fail at any score** — regenerate.

---

## 4 · Batch QA

1. Build a **contact sheet** from the batch (exclude previous contact sheets from the glob — a verified footgun).
2. Score every image individually; a batch verdict hides the weak ones.
3. Check **series consistency** (R20): the product/venue must be identical across the set. Only context, frame, mood and light change.
4. Check **angle diversity** (R21): count distinct headline archetypes and creative types. `5 creatives, 5 archetypes` is the target; `5 creatives, 1 archetype, 5 palettes` is a failed batch.
5. Report per image: score, verdict, failed rule IDs, and what changed on the second pass.

**Report format:**

```
ad_01  18/20  PASS   —
ad_02  14/20  FIX    typography (mid-word clip, 88px→64px), copy (generic headline)
ad_03   9/20  REDO   R30-logo (redrawn crest), R30-stock
ad_04  17/20  PASS   space (subline 40px from edge — padded)
ad_05  16/20  PASS   —
batch: 3 ship, 1 fixed, 1 regenerated · archetypes used: concrete, place, number, proof, deadline
```

---

## 5 · Text-file gate (copy, prompts, captions)

For the written deliverables around the image. This does **not** check images — see layer 1 for those.

```bash
# Visual-slop vocabulary leaking into prompts
grep -Eiq "purple gradient|glassmorphism|neon glow|glowing orbs|floating particles|isometric" "$f" \
  && echo "SLOP" || echo "CLEAN"

# AI copy tells in captions/prose
grep -Eiq "delve|seamless|empower|elevate|robust|tapestry|game-changer|revolutionary|unlock|unleash|🚀" "$f" \
  && echo "SLOP" || echo "CLEAN"

# Placeholders that survived into a final prompt (R25)
grep -En "\[[A-Z_ ]+\]|<BRAND>|HEADLINE\"" "$f" && echo "UNFINISHED PROMPT"
```

> ⚠️ **False positives:** CSS variables and class names (`--purple`, `.card-lp`) are legitimate. Check context.
> ⚠️ **Meta note:** don't quote banned words in a file's own QA section — the grep will catch them. Write "stop-slop gate — PASS" instead.

---

## 6 · Quick reference card

```
gate      script PASS  +  vision JSON  +  score ≥16/20  +  zero hard fails
layers    1. scripts/qa.py       — dimensions, safe area, contrast, collage, thumbnail
             (always pass --text-box, or four of seven checks report n/a)
          2. vision prompt (§2)  — structured JSON, adversarial, transcribes all text
          3. rubric (§3)         — 10 criteria × 0/1/2
redo      any hard fail · score <12 · reads_as_ai_generated
fix       score 12–17 → lowest criteria first, re-score
batch     contact sheet · per-image scores · series consistency · archetype diversity
```
