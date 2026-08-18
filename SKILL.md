---
name: premium-ad-design
description: Marketing flyers/postery/meta ads — uczy jak wygląda piękny design i jak go wygenerować. Niche-driven workflow: brief + ref photos → research niszy → generacja → QA gate → delivery. PL. Używać do posterów, flyerów, meta ads i promocyjnych grafik dla firm/restauracji/hoteli/lokalnych biznesów, szczególnie gdy użytkownik wrzuca logo, zdjęcia serwisów lub jedzenia jako referencje.
version: 1.0.0
license: MIT
author: AI Evolution Labs
url: https://github.com/aievolutionpl/premium-ad-design
---

# 🎨 Premium Ad Design

> **"Nie generuj 'obiektów w próżni'. Generuj reklamy, które wyglądają jak kampania — z hierarchią, typografią, realnym światłem i strukturalnym przekazem."**

**ŁADUJ TEN SKILL, GDY:** użytkownik prosi o **poster, flyer, meta ad, social ad, promocyjny obrazek** dla firmy/restauracji/hotelu/lokalnego biznesu — zwłaszcza gdy wrzuca **logo, zdjęcia serwisów, wnętrz lub jedzenia** jako referencje i pyta "jak powinny wyglądać reklamy dla tej niszy".

To jest **doctrina designu** + **orkiestrator**. Nie zastępuje narzędzi — mówi **jak ma wyglądać piękny wynik**, a potem deleguje generację do właściwych skilli (`imagegen`, `reference-led-ad-production`, `premium-static-ad-production`, `gpt-image-prompt-framework`, `design-taste`, `jarvis-anti-slop`). Ładuj je, gdy docierasz do kroku generacji.

---

## 🔍 Dlaczego AI adsy wyglądają jak slop

Zanim nauczysz się "pięknego", musisz rozpoznać "slopowe". Oto powtarzalne wzorce, przez które grafik z ChatGPT wygląda jak wygenerowany:

| # | Slop | Symptom | Co zamiast tego |
|---|------|---------|-----------------|
| 1 | **Miniaturki / clip-art** | Małe ikonki, thumbnail-style grafiki zamiast pełnej kompozycji | Jeden duży hero + minimalne elementy wspierające |
| 2 | **Text-on-photo** | Ramki, gradienty, napisy naklejone na zdjęcie = Canva template | Natywny tekst w scenie ALBO czysta fotografia + solidny panel typografii |
| 3 | **Generyczny gradient** | Purple/blue gradient wszędzie, glassmorphism, glow orbs | Paleta brandu, JEDEN akcent, płaskie tło lub realna tekstura |
| 4 | **Inter + flat** | Defaultowy font, brak kontrastu wagi/rozmiaru | Prawdziwe fonty (2-3 rodziny), mocna hierarchia |
| 5 | **AI-wymyślone jedzenie** | Model tworzy dania, których lokal nie serwuje | Realne dania z ref photos jako hero |
| 6 | **Cream/sand tło** | Beżowy/kości słoniowej background "dla ciepła" | True white, nasycony kolor brandu, albo ciemny neutral |
| 7 | **Brak struktury** | Piękne zdjęcie, ale zero hierarchii: bez headlinu, CTA, brand cue | Jasna struktura: headline → subline → CTA → logo |
| 8 | **Logo AI-redraw** | Model przekręca/niszczy oficjalne logo | Nigdy nie redraw — wstaw oryginalny plik |

> **Złota zasada:** jeśli wynik dałoby się pomylić z szablonem Canvy albo z "obrazkiem od ChatGPT" — to slop. Piękny ad wygląda jak wycięty z profesjonalnej kampanii.

---

## 🏛️ THE DESIGN DOCTRINE — co składa się na piękny design

Te 7 filarów jest **nadrzędnych wobec wszystkich skilli generacji**. Każdy prompt i każdy wynik oceniasz pod nimi.

### 1. HIERARCHIA — jeden dominujący element
- Jeden focal point na grafikę: **TITLE**. Czytelny z miniaturki (3-5× większy niż body).
- Widz ma zrozumieć przekaz w **1 sekundę** ze scrolla.
- Nigdy dwa konkurujące focal points. Body max 3 krótkie linie.
- Reguła: **"przeczytaj tytuł z rozmiaru miniaturki"** — jeśli nie da się, powiększ/zrób krócej.

### 2. TYPOGRAFIA — prawdziwe fonty, prawdziwy kontrast
- Konkretne rodziny (np. Playfair Display + Montserrat), **nigdy "modern sans-serif"**.
- Max **3 rodziny** na grafikę. Kontrast wagi i skali, nie tylko koloru.
- All-caps tylko do krótkich labeli (<4 słów), nigdy do body.
- Nazwij font w prompcie: `"bold condensed sans"`, `"elegant serif"`, `"geometric sans"`.

### 3. KOLOR — paleta brandu + JEDEN akcent
- Kolory z CONFIG.md / ref images, **nie default purple-gradient**.
- Tło: true white, nasycony kolor brandu, albo ciemny neutral. Nie cream/sand "dla ciepła".
- Akcent (złoto, czerwień, turkus...) użyty **oszczędnie**: ≤3 miejsca (label, linia, CTA).
- Gradient tylko funkcjonalny (scrim dla czytelności tekstu), nigdy dekoracyjny.

### 4. PRZESTRZEŃ — negatywna przestrzeń = luksus
- Generozne marże (~8% z każdej strony). Nic nie dotyka krawędzi.
- Biała przestrzeń to cecha, nie strata. "Oddech" wokół każdego elementu.
- Luksus/premium = kontrolowane ciemne cienie + highlighty + negatywna przestrzeń.

### 5. IMAGERY — produkt w kontekście, nie w próżni
- Produkt w realnym użyciu: ludzie, wnętrza, światło, pora dnia. **Nigdy obiekt na białym voidzie**.
- Realne światło: golden hour, directionał light, cień. Konkretne sceny, nie abstrakcyjne koncepty.
- Jedzenie: **realne dania z ref photos**, nie AI-inwencja.
- Fotografia, nie izometryczna ilustracja (chyba że brand express chcę).

### 6. LOGO FIDELITY — nigdy nie AI-redraw oficjalnego logo
- Oficjalne logo = chroniony asset. Wstaw oryginalny plik w finalnej kompozycji.
- Nie proś modelu o "narysowanie logo" — przekręci je.
- QA logo względem źródła. "Plausible" logo = FAIL.

### 7. STRUKTURA ADS — piękne zdjęcie to nie ad
- Finalna grafika musi mieć: **headline → subline → CTA → brand cue**.
- CTA = jedna jasna akcja ("Zarezerwuj stolik", "Zamów teraz", "Zadzwoń").
- Krótko. Headline 1-5 słów. Subline jedna linia.
- Jeśli to tylko piękne zdjęcie bez struktury — to nie ad, to wallpaper.

---

## 🚫 ANTI-SLOP GATE (kompendium zakazów)

Skompilowane z `jarvis-anti-slop` + realnych rejectów z produkcji. **Zanim wyślesz cokolwiek — przeleć tę listę.**

**Nigdy w promptach:**
- ❌ `purple gradient`, `blue-to-purple`, `glassmorphism`, `frosted glass`, `glass card`
- ❌ `neon glow`, `glowing accents`, `glowing orbs`, `floating particles`, `magical sparkles`
- ❌ `gradient text`, `dark mode with glowing accents`
- ❌ `isometric illustration` (chyba że brand express)
- ❌ `geometric abstract shapes` (overused AI bg)
- ❌ `cream`, `sand`, `beige`, `ivory` background (bez powodu)

**Nigdy w obrazie (treści):**
- ❌ Małe ikonki / clip-art / thumbnail-style graphics
- ❌ Text-on-photo jako Canva template (ramki + napis na zdjęciu)
- ❌ AI-wymyślone jedzenie, gdy klient ma realne zdjęcia dań
- ❌ Logo AI-redraw (przekręcone wordmarki, cresty)
- ❌ Dwa focal points / brak hierarchii
- ❌ Tiny footer z fake danych kontaktowych / numerami

**Copy zakazy (w obrazie i w captions):** `delve`, `seamless`, `empower`, `elevate`, `robust`, `tapestry`, `revolutionary`, `game-changer`, `🚀` na headline — patrz `jarvis-anti-slop` + `stop-slop`.

> **Programmatic gate** — uruchom przed publikacją każdego HTML/CSS/obrazu (z `jarvis-anti-slop`):
> ```bash
> grep -ci "purple\|glassmorphism\|neon glow\|glowing\|delve\|seamless\|game-changer\|revolutionary\|empower\|🚀" <plik> || echo "CLEAN"
> ```
> Uwaga na false positives z CSS variables i nazwami klas (patrz `jarvis-anti-slop`).

---

## 🔧 WORKFLOW — od briefu do gotowego packa

### Krok 1 · BRIEF INTAKE (co promujemy)
Użytkownik zwykle wrzuca: podstawowe info + logo + zdjęcia serwisów/jedzenia. Zebierz:
- **Co** promujemy (produkt / usługa / oferta / wydarzenie)
- **Dla kogo** (audience)
- **CTA** (co ma zrobić odbiorca)
- **Platformy** (IG feed 4:5, Stories 9:16, FB/Meta 1:1 lub 4:5, print A4)
- **Ref photos** — pobierz pełne URL z Discord CDN (z parametrami podpisu `?ex=&is=&hm=`), zapisz do workspace
- **Brand** — kolory, fonty, logo, ton z CONFIG.md / ref images

### Krok 2 · RESEARCH NISZY (jak wyglądają dobre adsy w tej branży)
Zanim zaczniesz generować — ustal, co działa w tej niszy. Pytania:
- Jak prezentują się topowe firmy w tej branży? (Meta Ad Library, IG, konkurenci)
- Jaki jest standard: editorial? dark studio? lifestyle? minimal?
- Co jest **fake/klisze**, których trzeba unikać w tej niszy? (np. AI-gourmet dla casual taverny)
- Jeśli klient ma istniejące adsy i mówi "tak mi się podoba" — **to jest źródło prawdy stylu**, nie twoja generyczna estetyka. Podnieś ich styl, nie wymyślaj własnego.

### Krok 3 · ANGLE MATRIX (5-10 różnych kątów)
Nie rób 10 color swaps. Zdefiniuj **różne obietnice i layouty**:
`heritage/luxury poster` · `editorial travel cover` · `minimal swiss grid` · `offer/CTA` · `events nightlife` · `lifestyle/product in use` · `brand story` · `terrace/dining` ...
Każdy ad testuje inną obietnicę, nie tylko inną paletę.

### Krok 4 · BACKEND / MODEL SELECTION
| Potrzeba | Backend #1 | Fallback |
|----------|-----------|----------|
| Natywny tekst w scenie (headline na ścianie/neon) | **Codex CLI (gpt-image-2)** | NB2 (FAL) |
| Czysta fotografia lifestyle / produkt | Codex CLI | NB2 / flux-dev |
| Czyste tło + PIL typografia (V2) | NB2 → PIL | Codex |
| Ref-driven food/hotel (realne zdjęcia) | **Codex z ref images** | NB2 ref-mode |
| Polskie napisy w scenie | **TYLKO Codex gpt-image-2** | — |

> Pamiętaj: Codex output 4:5 = **1122×1402** (nie crop — scale+pad do 1080×1350). Patrz `imagegen`.

### Krok 5 · GENERACJA
- **Ref images zawsze** dla twarzy/produktu/logo/budynku. Podaj rolę każdej ref (`Image A = pose`, `Image B = style`).
- **Jeden skończony ad per generacja** — nigdy batch/contact sheet w jednym obrazie. `count:1`.
- Prompt starter dla modeli obrazów: `ONE SINGLE FINISHED AD ONLY — no collage, no grid, no split-screen.`
- Wypełnij **5 slotów** z `gpt-image-prompt-framework` (SCENE / SUBJECT / DETAILS / USE CASE / CONSTRAINTS) + design doctrine.
- Natywny tekst: cytuj KAŻDE słowo w cudzysłowie, `CRITICAL: every word spelled perfectly`.

### Krok 6 · QA GATE (obowiązkowy)
1. Sprawdź wymiary (`file <sciezka>`), scale+pad jeśli trzeba.
2. Zbuduj **contact sheet** (wyklucz poprzednie contact sheets z globa).
3. `vision_analyze` każdy ad wg checklisty:
   - [ ] Tytuł czytelny z miniaturki
   - [ ] Tekst przeliterowany poprawnie (zwłaszcza PL diacritics ą ć ę ł ń ó ś ź ż)
   - [ ] Hierarchia: 1 focal point, 1 sekunda
   - [ ] Akcent ≤3 miejsca
   - [ ] Logo czyste, nie AI-zniekształcone
   - [ ] Brak fake danych / małych footerów
   - [ ] Żadnego text-on-photo slopu / AI-food
   - [ ] Wymiary zgodne z briefem
4. Kontrast: biały tekst na zdjęciu wymaga shadow alpha ≥200 + scrim gradient (patrz `premium-static-ad-production`).
5. Fix deterministycznie (PIL) tylko drobiazgi; regeneruj, gdy wizualnie złe.

### Krok 7 · DELIVERY
- ZIP (finalne pliki + contact sheet + README), podaj koszt (`🖼️ model — X credits`).
- Krótkie potwierdzenie na Discord — bez narracji podczas pracy.
- Zapisz refs do `Agents/<BRAND>/REF IMAGES/` dla reuse.

---

## 🍽️ NICHE PLAYBOOKS

### Restauracja / jedzenie
- **Real food wins.** Klient ma zdjęcia dań → **użyj ich jako hero**, nie AI-inwencji. AI-gourmet (krewetki king prawns, kleftiko) dla casual taverny = natychmiastowy reject ("food doesn't look like what we serve").
- Zwycięski layout: **real photo (góra ~60-65%) + solidny ciemny/kolorowy panel (dół ~35-40%)** z headline/subline/CTA/logo. Czysta separacja, zero tekstu na jedzeniu.
- Dark studio editorial tylko, gdy klient **nie ma** użytecznych zdjęć i akceptuje stylizację.
- Natywny tekst w scenie (Codex) dobra opcja: brand mały serif u góry, headline duży bold, location line krótka.
- **Nigdy text-on-photo Canva template** (#1 reject).

### Hotel / venue
- Coastal editorial: golden hour, travel-magazine quality, Canon R5 spec.
- Facade jako hero (real ref), direct-booking CTA.
- Layouty: heritage poster, seaside escape, terrace/dining, events, direct booking offer.
- Logo na facade — wstaw oryginał deterministycznie, nie przez AI.

### Lokalny biznes (usługi, retail)
- Czytelne CTA + logo fidelity + lokalizacja/telefon.
- Realne zdjęcia produktu/instalacji jako ref → generuj nowe sceny premium (inne światło, pora dnia, lifestyle), NIE overlay na oryginale.
- Zero abstrakcyjnych/artystycznych — realistyczne i funkcjonalne.

### Wydarzenie / nightlife
- Poster z mocną typografią, duży tytuł, event rows czytelne z miniaturki.
- Nie przeciążaj: 1 hero + data/miejsce/CTA.

---

## 🧭 ROUTING — do jakiego skilla oddelegować co

| Sytuacja | Skill |
|----------|-------|
| Wybór backendu, resize, ref images, koszty, brand-specific rules | `imagegen` |
| Refs od klienta + pack wielu stylów 4:5 | `reference-led-ad-production` / `reference-photo-promo-flyers` |
| Czyste tło + deterministyczna typografia/logo (V2) | `premium-static-ad-production` |
| Pisanie promptów (5 slotów, ref role, PL spelling) | `gpt-image-prompt-framework` |
| Carousels / serie slajdów | `design-taste` + `carousel-design` |
| Ostatnia bramka jakości | `jarvis-anti-slop` + `stop-slop` |

---

## ✅ QA CHECKLIST (wydruk do każdego packa)

- [ ] Wymiary zgodne z briefem (1080×1350 dla 4:5 itd.)
- [ ] Tekst przeliterowany poprawnie (PL diacritics!)
- [ ] Headline czytelny z miniaturki
- [ ] Jeden focal point, hierarchia w 1 sekundę
- [ ] Akcent ≤3 miejsca
- [ ] Logo czyste (nie AI-redraw) / oryginalny plik
- [ ] Zero fake danych kontaktowych
- [ ] Zero text-on-photo slopu / AI-food / floating icons
- [ ] Struktura: headline → subline → CTA → brand cue
- [ ] Kontrast tekstu na zdjęciu (scrim + shadow)
- [ ] Contact sheet + ZIP + koszt zgłoszone

---

## 📜 Licencja

MIT — używaj, remiksuj, publikuj.

---

<br>
<p align="center">
  <b>Created by</b><br>
  <b>AI EVOLUTION LABS</b><br>
  <sub>Channel Islands</sub><br>
  <sub><a href="https://github.com/aievolutionpl/premium-ad-design">github.com/aievolutionpl/premium-ad-design</a></sub>
</p>
