# 02 · Hotel — editorial background + deterministic typography

**Mode B** · 4:5 (1080×1350) · one creative from a batch of ten structurally different styles

---

## 1 · Brief

> "We're a seafront hotel, Victorian building, 40 rooms. Most of our bookings come through Booking.com and they take 15%. We want ads that push people to book direct. Here's our logo and some photos of the building and the terrace."

**The real objective is not "a beautiful hotel ad" — it's a margin recovery.** That changes the creative: the ad must give a *reason* to book direct, not just show the hotel. Message first, scene second (R24).

**Assets:** logo (white wordmark on a navy square), 20 photos of the facade, terrace, rooms and the bay.
**Decision:** **Mode B**. The building is a listed Victorian facade — any AI re-generation invents windows, changes the roofline and redraws the signage over the door. The photo is the asset; the design goes on top (playbook §2a).

---

## 2 · Creative work (R28)

| Step | Decision |
|------|----------|
| 1 · Product | direct booking of a sea-view room |
| 2 · Benefit | booking direct is genuinely cheaper — the client confirmed an average £40 gap on a two-night stay |
| 3 · Target | UK domestic travellers, 35–65, planning 2–8 weeks ahead, price-comparing across portals |
| 4 · Angle | OBJECTION — "the portal must be cheaper" is the belief blocking the booking |
| 5 · Metaphor | none. The number *is* the creative |
| 6 · Creative type | PREMIUM EDITORIAL (R14 #09) |
| 7 · Headline | see §3 |
| 8 · Composition | editorial split (layout-system §3c) — type in the top third on a flat navy field, the terrace photo placed as a bounded rectangle below |
| 9 · Light & camera | golden hour, 24–70mm at the wide end, from the promenade looking back at the terrace |
| 10 · Constraints | real facade, no redrawn signage, official logo file, no invented amenities |

**Why the editorial split, not a full-bleed hero:** a full-bleed golden-hour hotel shot with a headline over it is the single most generic hospitality ad there is. Placing the photo as a *bounded block* on a flat brand field reads as designed, and it also gives the £40 claim somewhere clean to live.

---

## 3 · Headline

| Draft | Archetype | Chars | Verdict |
|-------|-----------|-------|---------|
| `Your perfect seaside escape` | — | 27 | ❌ banned construction, interchangeable |
| `Book direct and save` | COMMAND | 20 | ❌ true but toothless — every hotel says it |
| `£40 cheaper, booked direct` | NUMBER | 26 | ✅ two lines at 64px |
| `The portals don't tell you this` | OBJECTION | 31 | ✅ strong, but the payoff has to live in the subline — riskier |
| `Same room. Forty pounds less.` | CONTRAST | 29 | ✅ shipped |

**Shipped:** headline `SAME ROOM.` / `FORTY POUNDS LESS.` (2 lines, 64px, Playfair Display 700) · subline `Book direct on our own site — always` (36 ch, Montserrat 400) · CTA `CHECK AVAILABILITY` (18 ch, exactly at budget).

Words, not digits, for the price: it keeps the line typographically even and reads less like a discount sticker. Use digits when the number is the scroll-stopper (`1,400 stoves`), words when the number is the argument.

---

## 4 · The prompts

### 4a · Background (AI)

```
ONE SINGLE PHOTOGRAPHIC BACKGROUND ONLY — no text, no words, no signage,
no logos, no numbers, no people, no collage. Aspect 4:5, 1080x1350.

Reference image A = subject, source of truth: '/refs/terrace_evening.jpg'
Preserve the building exactly: the Victorian bay windows, the balustrade,
the awning line, the render colour, the window proportions and the number
of storeys. Do not redraw, restyle or "improve" the architecture.

OBJECTIVE: make the viewer feel the last hour of a good day here.

SCENE: the hotel's own sea-facing terrace, forty minutes before sunset in
late September. Tables laid, glasses on them, nobody seated yet.

COMPOSITION: shot from the promenade looking back at the terrace, the
building occupying the right two-thirds, the bay opening to the left.
Generous clean sky in the upper third. Nothing crossing the outer 8% margin.

CAMERA: standing eye level, 24-70mm at 35mm, f/4, the whole terrace sharp,
gentle falloff on the far balustrade.

LIGHTING: low golden-hour sun from camera-left, long warm raking light
across the render and the balustrade, cool shadow filling the sea side.
Travel-magazine grade: warm highlights, held shadows, no HDR halo.

MATERIALS: painted render with visible texture, weathered stone balustrade,
linen tablecloths, glass catching the low sun.

BRAND MOOD: coastal, Victorian, calm, well-kept. Not luxury-resort.

OUTPUT: background plate for a 4:5 feed ad; typography added separately.

CONSTRAINTS: architecture identical to the reference · no invented balconies,
signage or lettering · no people · no boats added to the bay · no text of any
kind anywhere in the image.
```

### 4b · Composition (deterministic)

```
canvas      1080x1350, background #0A1F33
photo       the generated plate, placed 86,470 → 994,1080 (10 columns wide)
eyebrow     "JERSEY · SEAFRONT"     24px Montserrat 600, +8% tracking, #D4A853
headline    "SAME ROOM."            64px Playfair Display 700, #F4F1EA, y=150
            "FORTY POUNDS LESS."    64px Playfair Display 700, #F4F1EA, y=222
subline     "Book direct on our own site — always"
                                    34px Montserrat 400, #F4F1EA at 80%, y=320
cta         "CHECK AVAILABILITY"    28px Montserrat 600, +6% tracking,
                                    on a 2px #D4A853 rule box, y=1150
logo        logo_white.png, 64px tall, bottom-centre, y=1230
margins     86px enforced on all four sides
```

Extract the white wordmark from the navy-square logo first:

```bash
python scripts/extract_wordmark.py refs/logo.png build/logo_white.png
```

---

## 5 · What came back (first pass)

**Score: 16/20 — PASS with fixes.**

| Criterion | Score | Note |
|-----------|-------|------|
| Hierarchy | 2 | headline dominates, photo supports |
| Product | **1** | the *offer* is the product here, and it reads — but the room itself is never shown |
| Realism | 2 | facade preserved, light plausible |
| Typography | 2 | Playfair/Montserrat pairing, correct tracking |
| Copy | 2 | passes the specificity test |
| Color | 2 | navy + one gold accent, used twice |
| Space | 2 | 86px margins clean |
| Logo | 2 | official file, extracted cleanly |
| Thumbnail | **1** | `FORTY POUNDS LESS.` readable; the subline disappears at 150px |
| Idea | 2 | the ad still argues without the photo |

The AI plate itself needed two attempts: the first added a **balcony the building doesn't have** on the third storey — `R30-product`, regenerate, no retouching. Worth noting because it's the exact reason this brief is Mode B in the first place.

---

## 6 · The fix

1. **Subline dropped from the thumbnail's job.** It stays for people who stop, but the headline now carries the whole claim alone — that's the test in R33, not "can I read everything".
2. **Second creative added to the batch** showing the room interior, so the set covers both the offer and the product (the `product: 1` deduction).
3. Facade regenerated with an explicit `no balconies, three storeys only` line appended to CONSTRAINTS — naming the specific hallucination is more effective than a general "preserve the architecture".

---

## 7 · What to steal

- **A listed or distinctive building is a Mode B decision, always.** The model will invent a balcony, and a local will notice.
- **Name the specific hallucination in CONSTRAINTS after it happens.** Generic preservation language doesn't prevent a repeat; `no balconies, three storeys only` does.
- **The editorial split is the fastest way out of generic hospitality.** Photo as a placed block on a flat brand field, type in the top third.
- **Extract the wordmark once, reuse across the batch** — and check it's ≥180px wide before you place it (layout-system §6).
- **When the client's business problem is commission, the ad's job is the objection, not the view.**
