# October 2026 refresh: three craft-style directions

> Fictional teaching briefs for the styles added in 6.6.0: proof of process (27), cut-paper collage (28) and contact sheet with mark-up (29). No images were generated or scored. The finished prompts live in [`prompts/craft-collage-styles.txt`](prompts/craft-collage-styles.txt) and pass `python scripts/prompt_lint.py`.

Each case shows the decisions the late-2026 rules add: whether the trend cue has decayed (R53), how the static survives Advantage+ remix (R54), and what must come from real material rather than the model (R55).

## 1 · Bakery: proof of process

**Brief.** Fictional Kraków bakery WARSTWA. Croissants are laminated by hand over 48 hours and come out of the oven every hour from 7:00 (facts supplied by the owner). The owner supplies two phone photos: the bench and a tray of croissants. Goal: weekday breakfast visits from people within 2 km.

**Research note.**
- Every competitor in the Ad Library shows a plated croissant on dark wood → our gap: hands and the making.
- Two competitors use serif headlines on cream paper → decayed cue (R53), avoid it.
- Reviews repeat "still warm" and "crunchy" → the headline uses the customer's words.

**Working note.** Format: hand-held / in-use · Style: 27 proof of process · Hook: "still warm" from reviews · Signature device: unfinished dough beside the finished pastry, plus a provenance strip.

**Why it holds.** The proof is real because the scene is built from the owner's photos (R55). The provenance strip carries three verified facts, not adjectives. The headline passes the sell test (R52): what it is, why it matters and a reason to believe it.

**Remix note (R54).** Headline upper left, away from the hands; plain bench and wall at the edges so expansion invents nothing; the still reads as a first frame. Ask the user to review generated backgrounds and switch off text generation: the copy is exact Polish.

## 2 · Yerba drink: cut-paper collage

**Brief.** Fictional sparkling yerba drink ZAWRÓT, 80 mg caffeine per can, no sugar (from the label). Audience: students and young office workers who drink energy drinks. Goal: awareness before a retail launch.

**Research note.**
- The category runs neon, glow and splash renders → everyone looks the same; a flat, physical collage stands out.
- One competitor uses dithered photo textures → decayed (R53).
- The main objection is "energy drinks make me jittery" → the headline names the source of the caffeine.

**Working note.** Format: bold statement · Style: 28 cut-paper collage · Hook: contrast with energy drinks · Signature device: the can at giant scale with a real paper shadow, one person looking up.

**Why it holds.** One joke (scale), one strip of copy, two facts from the label. The person is a cut-out black-and-white photo, obviously staged, so nobody reads it as a real customer (R55). A comparison claim stays general ("not from an energy drink") because no head-to-head data was supplied.

**Remix note (R54).** The can and the strip are separate layers on a flat red ground, so expansion extends the red and static-to-video can move the paper without warping letters.

## 3 · Sock brand: contact sheet with mark-up

**Brief.** Fictional sock brand PRĄŻEK, twelve colourways of combed-cotton socks, sizes 36–46. The mustard colourway sold out and is back in stock (verified by the owner). Twelve real product photos are supplied.

**Research note.**
- Competitors show one pair on a foot → the range is the gap.
- The returning colour is real news → a reason to act now without inventing urgency.

**Working note.** Format: offer stack without a price, range first · Style: 29 contact sheet with mark-up · Hook: "Musztarda wraca." · Signature device: the grease-pencil circle around frame 7.

**Why it holds.** Twelve frames is the upper limit for thumbnail legibility. Every frame is a real colourway passed as a reference, so the grid cannot invent products (R55). The circle does the work a sticker would do in a performance banner, once.

**Remix note (R54).** The contact sheet sits centrally with grey desk around it. In a carousel, card 1 is this sheet and cards 2–4 are single colourways in the same light.

## What to steal

- Run the R53 check during research, not after the render: one line in the research note is enough.
- Name the remix risk in the working note for every static (R54).
- Decide what must be real before writing the prompt. Then pass it as a reference with a role (R55, R03).
