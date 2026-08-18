<div align="center">

# 🎬 Meta Ads Designer

### Uniwersalny standard reklamy dla agentów AI — przestań generować AI-slop, zacznij generować kampanie.

**Postery · Flyery · Meta Ads · Fotografia produktowa · Grafiki e-commerce** — dla restauracji, hoteli, lokalnych biznesów i retailu.

[🇬🇧 English](README.md) · [PL](README.pl.md)

![Version](https://img.shields.io/badge/version-4.0.0-6a5acd)
![License](https://img.shields.io/badge/license-MIT-brightgreen)
![Format](https://img.shields.io/badge/default_format-4:5%20(1080×1350)-informational)
![Hosts](https://img.shields.io/badge/runs_on-ChatGPT%20%7C%20Codex%20%7C%20Hermes%20%7C%20Claude%20%7C%20Cursor-blue)
![Framework](https://img.shields.io/badge/framework-agnostic-success)
![PRs](https://img.shields.io/badge/PRs-welcome-2ea44f)

<br/>

> **„Nie generuj 'obiektów w próżni'. Generuj reklamy, które wyglądają jak kampania — z hierarchią, typografią, realnym światłem i strukturalnym przekazem."**

> **Domyślny format: 4:5 (1080×1350)** — feed Instagram/Facebook. Użytkownik może poprosić o inny ratio; 4:5 to default.

> **`DON'T DECORATE. DIRECT.`** — Jeden produkt. Jedna idea. Jeden mocny visual.

<br/>

</div>

---

## 🧩 Problem — dlaczego AI adsy wyglądają tak samo

Modele obrazowe **nie mają gustu**. Pozostawione same sobie zbiegają do looku, który każdy rozpozna jako AI-slop:

| 🐘 Co widzi użytkownik | ➡️ Co produkuje model |
|------------------------|----------------------|
| Prawdziwy biznes z prawdziwymi zdjęciami | Małe ikonki clip-art, brak kompozycji |
| Ich prawdziwe jedzenie / lokal / produkt | AI-**wymyślone** dania, fake fasady |
| Ich prawdziwe logo | Zniekształcone AI-**redrawn** logo |
| Premium lokalna restauracja | Generyczny purple-blue gradient + Inter font |
| Zapadająca w pamięć oferta | Tekst naklejony na zdjęcie (Canva), bez komunikatu |

Efekt brzmi jak *"obrazek od ChatGPT"* — nie jak profesjonalna kampania. **Meta Ads Designer to naprawia.**

---

## 🚀 Wypróbuj teraz (bez instalacji)

**Opcja A — jedna wklejka.** Wklej zawartość **[`core.md`](core.md)** do ChatGPT / Claude / Gemini jako custom instruction, a potem wpisz:

> *"Zrób 4:5 social ad dla mojej kawiarni. Oto moje zdjęcia referencyjne: [logo + napoje]. Trzymaj się zasad Meta Ads Designer — produkt na pierwszym planie, prawdziwe jedzenie z moich zdjęć, moje logo bez zmian, jeden headline czytelny z miniaturki, zero text-on-photo slopu. Pokaż 3 strukturalnie różne koncepty."*

**Opcja B — jako skill** (Hermes / Claude Code / Codex / Cursor):
```bash
git clone https://github.com/aievolutionpl/meta-ads-designer.git
cp -r meta-ads-designer ~/.hermes/skills/marketing/   # lub ~/.claude/skills/ ~/.codex/skills/ ~/.cursor/skills/
```

**Weryfikacja** — poproś agenta: *"podsumuj zasady Meta Ads Designer"*. Powinien wymienić product-first, source of truth, commercial realism, hierarchię, negatywną przestrzeń, anti-slop, hard fails. Jeśli recytuje generyczne "make it premium" — nie wczytał; wklej ponownie.

Pełne kroki per host: **[`INSTALL.md`](INSTALL.md)**.

---

## ✨ Dlaczego działa na każdym agencie

`Meta Ads Designer` jest **framework-agnostic**. Te same zasady działają wszędzie — natywne skille na Hermes/Claude/Codex/Cursor, custom instruction w ChatGPT, albo wstrzyknięcie do system promptu dowolnego agenta/API.

```
┌────────────────────────────────────────────┐
│ visual-advertising-engine(.en).md          │  ← THE standard (34 zasady)
│   Product First · Source of Truth ·        │     Prompt Architecture ·
│   Hard Fails · Final Quality Check         │     Creative Workflow
└───────────────┬────────────────────────────┘
                │ podsumowany jako
                ▼
┌─────────────────────────────┐
│      design-rules(.en).md   │  ← THE charter (wklejany gust)
│   "The Rules of Beautiful   │     Działa na KAŻDYM agencie
│    Advertising"             │
└───────────────┬─────────────┘
                │ ładowany przez
        ┌───────┼───────┐
        ▼       ▼       ▼
   ┌────────┐ ┌───────┐ ┌──────────────┐
   │SKILL.md│ │core.md│ │  references/ │
   │ manual │ │wklejka│ │ głębia:      │
   │        │ │1 str. │ │ prompty,     │
   └────────┘ └───────┘ │ nisze, slop  │
                        └──────────────┘
```

**Podział jest celowy:** *standard* (co agent stosuje) → *charter* (gust, wklejany) → *manual* (procedura) → *core* (1-stronicowa wklejka) → *references* (głębia). Gust podróżuje; procedura się adaptuje.

---

## 🏛️ Zasady Pięknej Reklamy

Pełny standard 34 zasad w **`visual-advertising-engine.md`**. Skrót:

> **Product First · Reference = Source of Truth · One creative = One idea · Don't decorate, direct.**

1. **Hierarchia** — jeden dominujący element (produkt/tytuł), czytelny z miniaturki, przekaz w 1s.
2. **Realna typografia** — nazwane fonty (Playfair, Montserrat…), max 3 rodziny, kontrast wagą i skalą. Nigdy "modern sans-serif".
3. **Paleta brandu + jeden akcent** — nigdy purple-blue default; zero cream/sand "dla ciepła"; gradient tylko jako scrim.
4. **Negatywna przestrzeń** — generozne marże, oddech; przestrzeń = luksus.
5. **Imagery w kontekście** — produkt w realnym użyciu, realne światło, realni ludzie. Nigdy w próżni.
6. **Realne jedzenie z refs** — nigdy nie pozwól AI wymyślać dań, których lokal nie serwuje.
7. **Logo fidelity** — nigdy AI-redraw oficjalnego logo; wstaw oryginał.
8. **Ad spine** — headline → subline → CTA → brand cue. Piękne zdjęcie ≠ ad.
9. **Zero AI-copy** — zakazane słowa (delve, seamless, empower, elevate, robust, revolutionary, 🚀); nazwy i liczby zamiast przymiotników.
10. **QA przed wysyłką** — czytelność z miniaturki, poprawna pisownia (w tym polskie diakrytyki), jeden focal point, kontrast, logo fidelity.

Plus z Engine: **Commercial realism** (perspektywa, grawitacja, cienie, realne materiały) · **Lighting is part of the product** · **Think like a photographer** · **Build depth** · **Trzy obowiązkowe kąty** (Problem/Efekt/Lifestyle) · **Visual Creative Library** (hero, packshot, lifestyle, product-in-use, macro, problem/solution, result, UGC, editorial, scroll-stopper) · **Spójność serii** · **Hard Fail Conditions** · **DON'T DECORATE. DIRECT.**

---

## 🧠 Workflow

```
1. BRIEF     — co promujemy, dla kogo, CTA, platformy + zbierz refs
2. RESEARCH  — jak prezentują się topowe brandy w niszy? Jeśli klient ma
               adsy, które lubi — to jest źródło prawdy stylu
3. ANGLES    — 5-10 różnych obietnic/layoutów, nie 10 color swaps
4. CREATIVE  — produkt → benefit → target → angle → metaphor → typ →
               kompozycja → światło/kamera → constraints → potem prompt
5. GENERATE  — jeden skończony ad per generacja; refs z rolą
6. QA        — contact sheet + checklist; scale+pad (nigdy crop) przy krawędziach
7. DELIVER   — pliki + contact sheet + notki; raport model/koszt
```

---

## 📁 Struktura repo

```
meta-ads-designer/
├── SKILL.md                        # Agent operating manual (procedura + routing)
├── core.md                         # 1-stronicowe zasady do wklejenia
├── visual-advertising-engine.md    # THE standard — 34 zasady (PL)
├── visual-advertising-engine.en.md # THE standard — 34 zasady (EN)
├── design-rules.md                 # Charter — Zasady Pięknej Reklamy (PL)
├── design-rules.en.md              # Charter (EN)
├── INSTALL.md                      # Setup per host (w tym ChatGPT)
├── README.md                       # Ten manual (EN)
├── README.pl.md                    # Ten manual (PL)
├── LICENSE                         # MIT
└── references/
    ├── hospitality-food-services-playbook.md  # Głębia: food / hotel / serwisy (sprawdzone)
    ├── anti-slop-registry.md       # Kompletne kompendium zakazów (visual + copy)
    ├── niche-playbooks.md          # Playbooki per nisza (restauracja, hotel, …)
    └── prompt-library.md           # Gotowe prompty dla dowolnego modelu
```

---

## 🧭 File map

| Plik | Do czego |
|------|----------|
| `core.md` | **1-stronicowa wklejka** — wklej do dowolnego czatu/agenta |
| `visual-advertising-engine(.en).md` | **Standard operacyjny** — 34 zasady przed każdym komercyjnym visualem |
| `design-rules(.en).md` | Charter — gust |
| `SKILL.md` | Manual agenta (czyta loader skilli) |
| `INSTALL.md` | Setup per host |
| `references/hospitality-food-services-playbook.md` | Głębokie reguły food / hotel / serwisy |
| `references/prompt-library.md` | Gotowe prompty |
| `references/niche-playbooks.md` | Głębia per nisza |
| `references/anti-slop-registry.md` | Lista zakazów + grep gate |
| `README.md` | Ten manual |

---

## 🤝 Współpraca

Masz zasadę, która uratowałaby kampanię? Otwórz PR do `visual-advertising-engine.md` — to źródło kanoniczne; `core.md`, `SKILL.md` i README je podsumowują. Zobacz [`CONTRIBUTING.md`](CONTRIBUTING.md).

---

## 📜 Licencja

MIT — używaj, remiksuj, publikuj.

---

<br/>
<div align="center">
  <b>Created by</b><br/>
  <b>AI EVOLUTION LABS</b><br/>
  <sub>Channel Islands</sub><br/>
  <sub><a href="https://github.com/aievolutionpl/meta-ads-designer">github.com/aievolutionpl/meta-ads-designer</a></sub>
</div>
