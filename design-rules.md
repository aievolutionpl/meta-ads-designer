# ✨ The Rules of Beautiful Advertising

> **The universal design charter for AI-generated posters, flyers, meta ads and promo graphics.**
> Framework-agnostic. Read this once, and every agent — Hermes, Claude Code, Codex, ChatGPT, Cursor — will stop producing AI-slop and start producing campaigns.

**Why this exists.** Image models have no taste. Left to themselves they converge on the same boring, unconvincing look: tiny clip-art icons, generic purple-blue gradients, default fonts, text slapped onto photos like a Canva template, invented dishes the restaurant never served, logos mangled by a redraw. This charter is the antidote — the hard rules that separate *"an image from ChatGPT"* from *"a professional campaign."*

**How to use it.**
- **As an agent skill** → load `SKILL.md` (it points here).
- **As a paste-into-any-chat** → paste this file (or its key sections) into ChatGPT / Claude / Gemini as a custom instruction, or attach it as a knowledge file.
- **As a checklist** → run the QA list at the end on every output before you ship it.

---

## 0 · The one-line law

> **A great ad reads in one second, from a thumbnail, and looks like it was art-directed by a human.** If it could be mistaken for a Canva template or "an image from ChatGPT" — it's slop.

---

## 1 · Hierarchy — one dominant element

- **One focal point per graphic: the TITLE.** Make it 3–5× the body size.
- A viewer must get the message **in 1 second** from a social-feed scroll.
- **Never two competing focal points.** One title, one supporting visual, optional short body.
- Body copy: max **3 short lines**. If it's longer, push detail into a diagram or a caption — **never shrink type to fit more words**.
- Test: **"can I read the title at thumbnail size?"** If no → make it bigger or shorter.

## 2 · Typography — real type, real contrast

- **Name real typefaces.** `Playfair Display` / `Didot` / `Cormorant` (display serif), `Archivo` / `Oswald` / `Anton` / `Montserrat` (bold sans). **Never "modern sans-serif".**
- **Pair one display font + one clean sans.** Max **3 families** per graphic.
- **Hierarchy via weight and scale, not just color.** Title bold + large; body regular + smaller.
- **Readable from a thumbnail.** Big title, clear contrast.
- **All-caps only for short labels** — eyebrows, badges, "STEP 01", CTA buttons (<4 words). **Never all-caps body copy.**
- **Script/display fonts only for large accents** — never at subline/body size where they become unreadable.
- **Generous letter-spacing (tracking)** on uppercase labels = premium feel. Normal tracking on body.

## 3 · Color — brand palette + one accent

- **Use the brand palette**, never the default purple-blue gradient.
- **Background:** true white, a saturated brand color, or a **dark neutral** (near-black navy `#0A0E1A`). Avoid cream/sand/beige "for warmth" — it reads as default AI.
- **One accent color**, used sparingly — **≤3 places** (a label, a line, a CTA). Gold `#D4A853` + black is the proven premium editorial pair.
- **Gradients only for function** (a scrim so text reads over a photo), never as decoration.
- **Contrast is non-negotiable.** Text over a photo needs a scrim/gradient + a drop shadow (alpha ≥ 200).

## 4 · Space — negative space is luxury

- **Generous margins (~8% on each side).** Nothing touches the edges.
- **White/empty space is a feature, not waste.** "Breathing room" around every element.
- Premium = **controlled dark shadows + controlled highlights + negative space.** Cramped = cheap.

## 5 · Imagery — context, not voids

- **Product in real use** — real people, real interiors, real environments, real time of day. **Never a product floating on a void or a gradient.**
- **Real light:** golden hour, directional light, soft shadows. Describe concrete scenes, not abstract concepts.
- **Food = real dishes from reference photos.** Never let the model invent dishes the venue doesn't serve — "AI-gourmet" (king prawns saganaki for a casual taverna) is an instant rejection.
- **Photography over abstract illustration.** Isometric/geometric/floating-icons reads as AI-slop unless the brand explicitly wants it.
- **Lens language adds realism:** "shot on 50mm f/1.8, shallow depth of field", "medium format", "Canon EOS R5, RF 24-70mm f/2.8L".

## 6 · Logo fidelity — never let AI redraw a logo

- **Official logos are protected assets.** Place the **original file** in the final composition; preserve proportions, alpha, colors.
- **Never** ask an image model to "draw the logo" — it will distort or invent it.
- **QA the logo against the source.** A "plausible" logo is a FAIL.
- If a brand bans in-image text, keep the visual clean and put brand message in the caption.

## 7 · Ad structure — a pretty photo is not an ad

- Every ad needs the spine: **headline → subline → CTA → brand cue**.
- **CTA = one clear action:** "Reserve a table", "Order now", "Call us", "Book direct". No fluff.
- **Headline 1–5 words. Subline one line.** Short beats clever.
- If it's just a beautiful photo with no message or action — it's wallpaper, not an ad.

---

## 8 · Copy — the words inside the ad

- **Open with force** — a wrong belief, a strong claim, a concrete example.
- **Take a real position.** If you can invert it, it has no stance.
- **Use names and numbers** — "54 KB" not "lightweight", "London Eye 5 min walk" not "great location".
- **Lead with verbs. Active voice.**
- **Vary sentence length** — uniform rhythm is the deepest AI tell.
- **No em dashes** — use commas, colons, semicolons.

### Banned AI words (never in an ad)
`delve · seamless · empower · elevate · robust · tapestry · revolutionary · game-changer · "in today's world" · "let's dive in" · "in summary" · 🚀 on a headline · "Powered by AI" · fake company logos · "Join the waitlist" on a fake product`

---

## 9 · The Anti-Slop Registry (what "AI look" means, banned)

| Tell | Fix |
|------|-----|
| Purple/blue gradient everywhere | Brand colors, one accent |
| Glassmorphism / frosted glass / glow orbs | Flat surface or real texture |
| Gradient text | Solid brand color |
| Tiny clip-art icons / thumbnail graphics | One big hero + minimal support |
| Text slapped on a photo (Canva look) | Native text in scene, or photo + solid panel |
| Cream/sand/beige background | True white / brand color / dark neutral |
| Overly round cards (24px+ on small cards) | 12–16px max; pills only for tags/buttons |
| Cards inside cards | One level max |
| Icons bigger than the content they introduce | Icon ≤ content |
| Gray text on tinted bg | Darker shade of the bg hue, or ink |
| Isometric / geometric-abstract as default | Photography / real context |
| AI-invented food | Real dishes from refs |
| AI-redrawn logo | Original file |
| Hairline border + soft wide shadow together | Pick ONE: defined edge OR soft elevation |

---

## 10 · Niche playbooks — how a good ad looks per industry

### 🍽️ Restaurant / food
- **Real food wins.** Use the venue's real dish photos as the hero. Never AI-invented dishes.
- **Winning layout:** real photo (top ~60–65%) + a solid dark/colored panel (bottom ~35–40%) holding headline/subline/CTA/logo. **Clean separation — no text on the food.**
- Dark-studio editorial only when the client has no usable food photos and accepts stylization.
- Native text in scene (where the model renders it well): brand small at top, big bold headline, short location line.

### 🏨 Hotel / venue / accommodation
- **Coastal editorial:** golden hour, travel-magazine quality, lens language.
- **Facade as hero** (real ref), then a direct-booking CTA.
- Layouts: heritage poster · seaside escape · terrace/dining · events · direct-booking offer · arrival/evening.

### 🏪 Local business (services, retail, home improvement)
- Real product/installation photos as refs → generate **new premium scenes** (different light, time of day, lifestyle). **Don't** paste overlays onto the client's raw photos.
- Readable CTA + logo fidelity + location/phone.
- Realistic and functional — no abstract/artistic theatrics.

### 🛍️ Retail / product
- Product **in use** in real context — not floating on a gradient.
- Studio hero: clean background, directional light, product hero, no clutter.

### 🎉 Event / nightlife
- Strong typography, big title readable from a thumbnail.
- Event rows (date/place) readable, not crowded.
- One hero + date/place/CTA.

---

## 11 · Workflow — the repeatable path

```
1. BRIEF     — what are we promoting, for whom, what CTA, which platforms,
               and collect the refs (logo, venue, food, products).
2. RESEARCH  — how do the top brands in this niche present themselves?
               (Meta Ad Library, Instagram, competitors). If the client has
               existing ads they like — THAT is the style source of truth.
3. ANGLES    — define 5–10 distinct promises/layouts, not 10 color swaps.
4. GENERATE  — one finished ad per generation. Use refs with a clear role.
               A model must never make a batch/collage in one image.
5. QA        — build a contact sheet; check every rule below; fix or redo.
6. DELIVER   — package files + contact sheet + notes. Report the model/cost.
```

---

## 12 · The QA checklist — run this on EVERY output

- [ ] Title readable at thumbnail size
- [ ] Text spelled exactly (incl. Polish diacritics ą ć ę ł ń ó ś ź ż)
- [ ] One focal point; hierarchy obvious in 1 second
- [ ] Accent color used ≤3 places
- [ ] Logo is clean, not AI-distorted (original file)
- [ ] No fake contact details / tiny footers
- [ ] No text-on-photo slop / AI-invented food / floating icons
- [ ] Ad spine present: headline → subline → CTA → brand cue
- [ ] Contrast OK (scrim + shadow over photos)
- [ ] Correct dimensions for the platform (IG feed 4:5 1080×1350, Stories 9:16, etc.)

---

## 13 · Platform dimensions (quick reference)

| Platform | Aspect | Resolution |
|----------|--------|-----------|
| Instagram Feed | 4:5 | 1080×1350 |
| Instagram Story / Reels / TikTok | 9:16 | 1080×1920 |
| Instagram Square / Facebook | 1:1 | 1080×1080 |
| Facebook / LinkedIn / YouTube | 16:9 | 1920×1080 |
| Pinterest | 2:3 | 1000×1500 |
| Banner | 4:1 | 2048×512 |

**Rule:** when text or logos live near the edge, resize with **scale+pad**, never a hard crop (crop cuts content).

---

*This charter is part of the **Premium Ad Design** plugin. For install instructions on every agent, see `INSTALL.md`. For the design-doctrine summary and the procedural agent workflow, see `SKILL.md`.*
