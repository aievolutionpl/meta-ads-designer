# ✍️ Headline System — the words that make it an ad

> **Half of "looks designed by a human" is the text.** A perfect photograph with `AUTHENTIC FLAVOURS` on it is still slop. This file is how the agent decides what the ad says — before it decides how the ad looks (R28 step 7).

Character budgets here are locked to the type scale in [`layout-system.md`](layout-system.md) §2a. If a headline doesn't fit its budget, **rewrite the headline** — never shrink the type.

---

## 1 · The specificity test (run this first, on every headline)

> **Could a direct competitor paste this headline onto their own ad without changing a single word?**

If yes → delete it and start again. That one test removes most AI copy, because the model's default is a sentence that fits everyone.

| ❌ Interchangeable | ✅ Only this business could say it |
|-------------------|-----------------------------------|
| Authentic flavours | Souvlaki off the grill since 2004 |
| Your perfect escape | Sea view, 4 minutes from the harbour |
| Quality you can trust | 1,400 stoves fitted on this island |
| Experience the difference | Booked direct: £40 cheaper than the portals |
| Taste the tradition | Grandma's recipe, Tuesdays only |
| Premium comfort | Underfloor heating, on by the time you arrive |

**Second test — the swap test:** replace the business name with a competitor's. If the ad still makes sense, the headline carries no information.

---

## 2 · The ten archetypes

Pick one per creative. Different creatives in a batch should use **different archetypes** — that's what makes a series test different promises rather than different palettes (R21).

### A · CONCRETE
A specific fact only insiders know. The strongest default.
> `Souvlaki off the grill since 2004` · `Bread baked at 5am, gone by noon` · `28 tables, one fireplace`

### B · PLACE
Geography as the promise. Unbeatable for local business.
> `Four minutes from Havre des Pas` · `The last kitchen open past midnight` · `Above the harbour, below the castle`

### C · NUMBER / PRICE
A number is inherently non-generic.
> `Two courses, £18, until 6pm` · `1,400 stoves fitted on this island` · `Ready in 9 minutes`

### D · CONTRAST
Two states in one line. The verbal form of before/after (R22).
> `Cold house Friday. Warm house Monday.` · `Booked in 30 seconds. Remembered for years.` · `Same street. Different Sunday.`

### E · COMMAND
Imperative verb, one action. Pairs with a hard offer.
> `Book the corner table` · `Fit it before the frost` · `Come hungry`

### F · AUDIENCE
Names who it's for. Filters, and the right people feel seen.
> `For the ones who eat after work` · `For anyone who's given up on radiators` · `Built for people with four dogs`

### G · SEASON / DEADLINE
Time pressure that's actually true. Never invent one.
> `Install before October 31 — price locked` · `Open until the last ferry` · `Three Sundays left this season`

### H · PROOF
Evidence, not adjectives.
> `Same chef, same grill, eleven years` · `Rebooked by 6 in 10 guests` · `Recommended by 500 island homes`

### I · OBJECTION
Names the thing that stops people booking, and kills it.
> `No deposit. No finance forms.` · `Yes, we take walk-ins` · `Cancel free until the day before`

### J · SENSORY
Only for food, and only when the photo can't carry it alone.
> `Still hissing when it reaches you` · `Crust you can hear` · `Charred edges, soft middle`

**Archetypes to avoid entirely:** the pun, the rhetorical question ("Looking for great food?"), the brand-values statement, and anything containing the words in the banned list (§6).

---

## 3 · Character budgets

Locked to the type scale. Count characters **including spaces**.

| Element | Budget | Renders at | Note |
|---------|--------|------------|------|
| **Eyebrow** | ≤ 24 | 24px, uppercase | optional; a label, not a sentence |
| **Headline — 1 line** | ≤ 22 | 88px | the strongest option; aim here |
| **Headline — 2 lines** | ≤ 22 per line, ≤ 40 total | 64px | break on meaning, never mid-phrase |
| **Headline — 3 lines** | ≤ 26 per line, ≤ 72 total | 48px | only for CONTRAST or list forms |
| **Subline** | ≤ 45 | 34px | exactly one line. Never two. |
| **Detail row** (location / hours) | ≤ 60 | 28px | use `·` as the separator |
| **CTA** | ≤ 18 | 28px, uppercase | one action, one verb |
| **Body (caption, off-image)** | ≤ 125 | — | Meta truncates around here |

**Native in-render text (Mode A) additionally:** total rendered words on the image **≤ 12**. Every extra word multiplies the spelling-failure rate. Brand + headline + one location line is the ceiling.

---

## 4 · CTA by category

One action. One verb. No fluff, no "learn more".

| Category | EN | PL |
|----------|-----|-----|
| Restaurant | `Reserve a table` · `Order now` · `See the menu` | `Zarezerwuj stolik` · `Zamów teraz` · `Zobacz menu` |
| Hotel / venue | `Book direct` · `Check availability` · `See the rooms` | `Rezerwuj bezpośrednio` · `Sprawdź dostępność` · `Zobacz pokoje` |
| Services / trades | `Book a survey` · `Call today` · `See our work` | `Umów wizytę` · `Zadzwoń` · `Zobacz realizacje` |
| Retail / product | `Shop now` · `See the collection` · `Order today` | `Kup teraz` · `Zobacz kolekcję` · `Zamów` |
| Events | `Get tickets` · `Reserve your spot` | `Kup bilet` · `Zarezerwuj miejsce` |

**Direct-booking beats portal language** for hospitality: `Book direct` carries a reason (price, control), `Book now` doesn't.

---

## 5 · Polish (and other diacritics) — the strategy

Polish diacritics `ą ć ę ł ń ó ś ź ż` are the single most common in-render text failure. Models drop the ogonek, swap `ł`→`l`, or produce a glyph that's subtly wrong — and a native speaker sees it instantly. It's the difference between "professional" and "made by a foreigner with AI".

**The decision rule:**

| Situation | Do this |
|-----------|---------|
| Polish copy, any length | **Mode B (deterministic).** Default. Render the text yourself with a font verified to carry Polish glyphs. |
| Polish copy, client insists on a fully generated image | Write the headline **using only diacritic-free words** (§5a), keep it ≤ 3 words, and vision-QA every variant |
| Polish copy, long or containing a proper noun with diacritics | Mode B. No exceptions. |
| Latin-script copy without diacritics (EN, most brand names) | Mode A is fine |

### 5a · Diacritic-free Polish headlines that still sound native

Polish has plenty of strong words with no diacritics. Build the headline from them when you must render natively:

> `PROSTO Z GRILLA` · `OTWARTE DO PIERWSZEJ` · `DWA DANIA, 49 ZL` · `REZERWUJ STOLIK` · `TYLKO W SOBOTY` · `DOWOZIMY NA MIEJSCE` · `PIERWSZY RAZ OD LAT` · `BEZ ZALICZKI`

Watch: `zł` → write `ZL` only if the brand accepts it, otherwise Mode B. Never fake a diacritic with an apostrophe.

### 5b · Font check
Before rendering Polish deterministically, confirm the family ships the glyphs. Verified safe: Montserrat, Inter, Lato, Source Sans 3, Oswald, Playfair Display, Archivo. Verify anything else — a missing glyph is silently substituted and the line ends up in two typefaces.

```python
from fontTools.ttLib import TTFont
cmap = TTFont("font.ttf").getBestCmap()
missing = [c for c in "ąćęłńóśźżĄĆĘŁŃÓŚŹŻ" if ord(c) not in cmap]
print("MISSING:", missing or "none")
```

---

## 6 · Banned in headlines

**Words:** `delve · seamless · empower · elevate · robust · tapestry · revolutionary · game-changer · unlock · unleash · discover the difference · experience · journey · in today's world · let's dive in`

**Constructions:**
- Rhetorical questions (`Looking for great food?`)
- `Your + abstract noun` (`Your perfect escape`, `Your journey begins`)
- `The ultimate / the perfect / the best + category`
- Adjective stacks (`fresh, authentic, delicious`)
- Any emoji in the headline (🚀 especially)
- Em dashes — use a comma, colon or a `·`
- Ellipses trailing into nothing
- ALL CAPS on anything longer than 4 words

**Punctuation rules:** a headline ends without a full stop unless it's two sentences (CONTRAST archetype). Apostrophes must be typographic `’` in Mode B; in Mode A, name them explicitly in the prompt — a missing apostrophe in a brand name is a verified failure mode.

---

## 7 · The generation routine

For every creative, in order:

1. **Write down the one fact** the business has that competitors don't. If you don't have one, ask the client — do not invent it.
2. **Pick an archetype** (§2) that carries that fact. Different archetype per creative in the batch.
3. **Draft five headlines** against the budget (§3). Five, not one — the first is always the generic one.
4. **Run the specificity test** (§1) on each. Usually 3 of 5 die here.
5. **Pick the shortest survivor.** Length is a tiebreak; short wins.
6. **Write the subline as the proof** of the headline's claim, in ≤45 characters. Not a restatement.
7. **Pick the CTA** (§4) — it must match the ad's one idea (R06).
8. **Read the three lines aloud in sequence.** Headline → subline → CTA should sound like one person talking, not three.

### Worked example

> **Brief:** casual Greek taverna, coastal town, has real photos of its souvlaki, wants more evening covers midweek.
>
> **Fact they own:** same grill, same family, since 2004; four minutes from the seafront promenade.
>
> **Five drafts:** ~~`Authentic Greek flavours`~~ (interchangeable) · ~~`Taste the Mediterranean`~~ (interchangeable) · `Souvlaki off the grill` (CONCRETE, 21 ch) · `Grilling since 2004` (PROOF, 19 ch) · `Four minutes from the sea` (PLACE, 25 ch — over 1-line budget)
>
> **Chosen:** headline `Souvlaki off the grill` (22 ch, 1 line, 88px) · subline `Havre des Pas · open till 11, Tue–Sun` (37 ch) · CTA `Reserve a table` (15 ch)
>
> **Why it works:** the headline names the actual dish and the actual cooking method — a competitor selling moussaka can't reuse it. The subline carries the two facts a midweek diner needs. Nothing on the plate is text.

---

## 8 · Quick reference card

```
test        could a competitor paste this? → if yes, rewrite
archetypes  concrete · place · number · contrast · command
            audience · deadline · proof · objection · sensory
budgets     headline ≤22 (1 line) / ≤40 (2 lines) · subline ≤45
            CTA ≤18 · detail row ≤60 · caption ≤125
mode A cap  ≤12 rendered words total on the image
polish      diacritics → Mode B, always (or diacritic-free words only)
banned      elevate · seamless · your perfect X · rhetorical questions
routine     one owned fact → archetype → 5 drafts → kill 3 → shortest wins
```
