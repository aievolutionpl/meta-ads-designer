# 📦 Prompt Library — gotowe szablony do generacji premium ads

> Łącz te szablony z **5-slotowym frameworkiem** (`gpt-image-prompt-framework`) i **design doctrine** (`premium-ad-design`). Zawsze: ref images z rolą, natywny tekst w cudzysłowie, `ONE SINGLE FINISHED AD ONLY`.

---

## 🧱 Uniwersalny szkielet promptu (Codex CLI / gpt-image-2)

```bash
codex exec --sandbox workspace-write --skip-git-repo-check --yolo "
Using image generation, create ONE SINGLE FINISHED AD ONLY — no collage, no grid, no split-screen.

Aspect ratio: 4:5 (vertical), final resized to 1080x1350.

Reference images (with role):
- Image A (product/venue/food hero): '/mnt/d/.../ref-A.jpeg' — preserve this EXACT subject/appearance.
- Image B (style/atmosphere): '/mnt/d/.../ref-B.jpeg' — take the color grade, lighting and mood.

SCENE:       [miejsce, pora dnia, środowisko — konkretne, nie abstrakcyjne]
SUBJECT:     [główny obiekt/osoba/produkt — zachowaj z ref A]
DETAILS:     [oświetlenie, kamera, kolory, tekstura] — text \"HEADLINE\" in [font, kolor, pozycja]
USE CASE:    [platforma] promotional ad for [BRAND], 4:5
CONSTRAINTS: no extra text beyond \"HEADLINE\"/\"SUBLINE\"/\"CTA\", preserve brand colors, no watermark, no collage

Native poster typography:
- Brand wordmark small serif at top: \"BRAND\"
- Headline large bold: \"HEADLINE\"
- Subline one line: \"SUBLINE\"
- CTA: \"CTA\"
CRITICAL: every word spelled PERFECTLY — double-check 'BRAND', 'PLACE'.

Save to: output/<brand>/<filename>.png
"
```

---

## 🍽️ Restauracja — real food hero (Codex, ref photos dań)

```text
ONE SINGLE FINISHED AD — no collage, no text on the food.
Aspect 4:5, 1080x1350.

Reference image: the restaurant's REAL dish photo — reproduce THIS exact dish
(ingredients, plating), do not invent dishes.

Layout: real dish photo as hero in the upper ~62%, a clean solid dark panel in
the lower ~38% holding the typography. Hard separation — no text over the food.

SCENE: tavern table near a sunlit window, coastal bokeh, warm natural light
SUBJECT: the real dish from reference, on the plate exactly as served
DETAILS: editorial food photography, shallow depth of field, rich saturated
         color, real textures. Shot on medium format 50mm f/1.8.
USE CASE: Instagram restaurant ad, 4:5
CONSTRAINTS: no invented dishes, no text over food, preserve the real plating

Native text on the dark panel:
- Brand small serif top: \"DE L'ETANG\"
- Headline bold: \"SOUVLAKI, OFF THE GRILL\"
- Location line: \"Havre des Pas · St Helier · Jersey\"
- CTA: \"RESERVE YOUR TABLE\"
CRITICAL: perfect spelling, correct apostrophes.
```

---

## 🏨 Hotel / venue — coastal editorial (Codex / NB2)

```text
ONE SINGLE PREMIUM HOTEL AD BACKGROUND — no text, no logo (logo added later).
Aspect 4:5.

Reference: the venue's real facade/interior photo — preserve its identity.

SCENE: golden hour at the [venue], coast/marina/terrace in warm light
SUBJECT: the real facade/terrace, authentic architecture
DETAILS: travel-magazine editorial, Canon EOS R5, RF 24-70mm f/2.8L,
         golden-hour light, premium color grade, clean negative space in lower third
USE CASE: hotel promo ad, 4:5
CONSTRAINTS: no text, no logos, no people unless requested, no collage
```

---

## 🏪 Lokalny biznes — product/installation (Codex, ref photos)

```text
ONE SINGLE FINISHED AD — realistic, functional, premium.
Aspect 4:5.

Reference: the client's real installation/product photo — keep the product
exactly, change scene to a premium lifestyle context.

SCENE: [professional/real context — e.g. modern living room / workshop]
SUBJECT: the real product/installation from the reference
DETAILS: new lighting (golden hour / directional), premium editorial look,
         real textures, product as hero, clean negative space
USE CASE: local business ad, 4:5
CONSTRAINTS: no abstract/artistic, keep realistic, no text on product, no overlay boxes

Native text (or caption if brand bans in-image text):
- Headline: \"HEADLINE\" · Subline: \"SUBLINE\" · CTA: \"CTA\" · Logo: brand top
CRITICAL: perfect spelling.
```

---

## 🎨 Czyste tło + PIL typografia (V2 — gdy nie chcesz natywnego tekstu)

1. Wygeneruj **czystą fotografię** (ZERO tekstu w prompcie).
2. Pobierz lokalnie, dodaj typografię + logo przez Pillow (patrz `premium-static-ad-production`).
3. Zasady PIL:
   - Headline white + drop shadow (offset ~3px, alpha ≥180).
   - Bottom gradient: height ≥720px dla 1080×1350, alpha → 255 (tekst na ciemnym, nie na jedzeniu).
   - Gold tylko jako mały akcent na ciemnym gradiencie, NIE na jedzeniu.
   - Subline w czystym sans (Montserrat), nie w thin script na jasnym tle.
   - Logo — wstaw oryginalny plik (extract white wordmark z solid-color logo jeśli trzeba).

---

## ⚠️ Zasady natywnego tekstu (unikanie literówek)
1. **Cytuj każde słowo** w cudzysłowie.
2. **Zrób tekst krótki** — brand + headline + jedna linia location. Więcej słów = więcej ryzyka błędów.
3. Dodaj `CRITICAL: every word spelled perfectly` + wymień nazwy własne.
4. **Vision-QA każdego wariantu** — natywny tekst może dryfować na dłuższych frazach.
5. Codex gpt-image-2 to jedyny pewny backend dla polskich napisów w scenie.
