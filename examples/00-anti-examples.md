# 00 · Anti-examples — the same brief, written two ways

> **Agents learn faster from a contrast than from a ban list.** Each pair below is one brief: the prompt an agent writes by default, what the model gives back, and the prompt that actually produces an ad.

---

## Pair 1 · Restaurant

### ❌ The default prompt

```
Create a beautiful Instagram ad for a Greek restaurant with delicious food,
warm atmosphere and elegant typography. Make it look premium and appetizing.
```

**What comes back, reliably:**
- A dish nobody at that restaurant cooks — king prawns saganaki with microgreens for a place that sells souvlaki off a charcoal grill. **AI-gourmet** (R30-product).
- `AUTHENTIC GREEK FLAVOURS` in a default sans, centred, with a soft drop shadow — a headline any of the other 40 Greek restaurants could use (fails the specificity test).
- Text sitting directly on the plate, so half the words land on a lemon wedge.
- A warm cream-beige background wash "for atmosphere" (anti-slop registry §1).
- No CTA, no location, no brand cue. A picture, not an ad (R17).

**Why:** the prompt made no decision. Every word — "beautiful", "delicious", "warm", "elegant", "premium" — is an adjective the model resolves with its own average. Adjectives are how you order slop.

### ✅ The finished prompt

```
ONE SINGLE FINISHED AD ONLY — no collage, no grid, no split-screen.
Aspect ratio 4:5, final size 1080x1350.

Reference image A = subject, source of truth: the real souvlaki plate photo.
Reproduce THIS exact dish — same cut of meat, same char marks, same flatbread,
same red onion and paprika. Do not add ingredients. Do not invent garnish.

COMPOSITION: the real dish photographed as the hero, filling the top 62% of the
frame edge to edge. The bottom 38% is a SOLID deep navy panel (#0A1F33), hard
straight edge between them, no gradient blend, no text anywhere on the food.

CAMERA: 45-degree angle, eye level with the table, 50mm, f/2.2, focus on the
front skewer, the back of the plate falling gently out of focus.

LIGHTING: late-afternoon window light from camera-left, warm, directional,
raking across the meat so the char and the glaze read as texture. Soft shadow
falling to camera-right. No fill from the front.

MATERIALS: charred edges, glossy meat, flatbread with visible blistering,
condensation on the glass at the edge of frame.

Native typography on the navy panel only:
- Small serif brand line, top of the panel: "DE L'ETANG"
- Headline, large bold sans, two lines: "SOUVLAKI OFF" / "THE GRILL"
- Detail line, small sans: "Havre des Pas · open till 11, Tue-Sun"
- CTA in a gold rule box: "RESERVE A TABLE"

CONSTRAINTS: no text on the food, no extra words beyond those quoted, no
watermark, no invented dishes, no people, no props that were not on the table.
CRITICAL: every word must be spelled PERFECTLY, including the apostrophe in
"DE L'ETANG" — double-check it.
```

**The difference in one line:** the second prompt makes eleven decisions the first one left to the model.

---

## Pair 2 · Local services

### ❌ The default prompt

```
Professional ad for a wood burning stove installation company. Modern, cozy
living room, warm lighting, premium quality feel. Add the company logo and
a call to action.
```

**What comes back:**
- A stove that doesn't exist — the model merges three stove designs into a plausible-looking one. If the client sent a reference of the model they actually fit, this is a hard fail (R30-product).
- A logo the model drew: right-ish shape, wrong letterforms, a crest that isn't theirs (R30-logo). **"Add the logo" is never a valid instruction to an image model.**
- `PREMIUM QUALITY YOU CAN TRUST` and `CONTACT US TODAY` — plus an invented phone number in a tiny footer.
- Fire glow rendered as neon orange bloom over the whole room (R05).

### ✅ The finished prompt (Mode B — background only)

```
ONE SINGLE PHOTOGRAPHIC BACKGROUND ONLY — no text, no words, no signage,
no logos, no numbers, no collage. Aspect ratio 4:5, 1080x1350.

Reference image A = subject, source of truth: the client's installed stove.
Keep the stove identical — same body proportions, same door and hinge, same
flue diameter and routing, same handle. Change only the room around it.

SCENE: a granite-walled island living room at dusk in late October. The stove
is lit and burning, sitting on a slate hearth against the chimney breast.

COMPOSITION: stove in the lower-left third, hearth line running to camera-
right, a wool throw over the arm of a chair entering the frame in soft
foreground blur. Keep the upper 40% of the frame calm and uncluttered — that
area will carry typography added afterwards.

CAMERA: eye level from a seated position, 35mm, f/2.8, stove sharp, the room
falling away gently.

LIGHTING: the firebox is the only warm source, spilling low across the slate;
cool blue dusk light from a window out of frame camera-right. Realistic falloff.
No glow bloom, no orange haze, no lens flare.

MATERIALS: cast iron with real matte texture, slate with visible grain, wool
with visible fibre, glass with a genuine reflection of the room.

CONSTRAINTS: the stove must remain identical to the reference in shape,
proportions, door design, flue and hardware. No fire outside the firebox.
No people. No text of any kind anywhere in the image.
```

Then the headline, the CTA, the real phone number and **the official logo file** are composed on top deterministically (layout-system §5, Mode B).

---

## Pair 3 · The headline alone

Same photograph, two headlines. This is the cheapest quality gain in the whole system.

| ❌ | ✅ | Why |
|---|---|---|
| `AUTHENTIC FLAVOURS` | `SOUVLAKI OFF THE GRILL` | names the actual dish and method |
| `YOUR PERFECT ESCAPE` | `SEA VIEW, FOUR MINUTES FROM THE HARBOUR` | a fact, not a feeling |
| `QUALITY YOU CAN TRUST` | `1,400 STOVES FITTED ON THIS ISLAND` | a number a competitor can't copy |
| `EXPERIENCE THE DIFFERENCE` | `COLD HOUSE FRIDAY. WARM HOUSE MONDAY.` | shows the transformation in six words |
| `BOOK YOUR STAY TODAY` | `BOOKED DIRECT: £40 CHEAPER THAN THE PORTALS` | gives a reason to act |

Method: [`references/headline-system.md`](../references/headline-system.md).

---

## The pattern behind all three pairs

| The weak version | The finished version |
|------------------|----------------------|
| adjectives (`beautiful`, `premium`, `cozy`) | decisions (`45-degree angle`, `#0A1F33`, `62%`) |
| "add the logo" | logo placed deterministically from the official file |
| the model picks the dish/product | the reference is declared as source of truth, role labelled |
| text position unspecified | text confined to a named region, with a hard edge |
| one paragraph | the 11-part architecture (R25) |
| no constraints | an explicit list of what must not change |

> **Every adjective you leave in the prompt is a decision you handed to a model that has no taste.**
