<div align="center">

# 🎬 Meta Ads Designer

### Uniwersalny standard reklamy dla agentów AI — projektuj piękne Meta / Instagram / Facebook adsy i przestań generować AI-slop.

**Meta Ads · Instagram · Facebook · Postery · Flyery · Fotografia produktowa · Grafiki e-commerce** — dla restauracji, hoteli, lokalnych biznesów i retailu.

[🇬🇧 English](README.md) · [PL](README.pl.md)

![Version](https://img.shields.io/badge/version-4.2.0-6a5acd)
![License](https://img.shields.io/badge/license-MIT-brightgreen)
![Format](https://img.shields.io/badge/default_format-4:5%20(1080×1350)-informational)
![Hosts](https://img.shields.io/badge/runs_on-ChatGPT%20%7C%20Codex%20%7C%20Hermes%20%7C%20Claude%20%7C%20Cursor-blue)
![Framework](https://img.shields.io/badge/framework-agnostic-success)
![PRs](https://img.shields.io/badge/PRs-welcome-2ea44f)

<br/>

<img src="assets/meta-ads-designer-banner.png" alt="Meta Ads Designer" width="100%"/>

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

> *"Zrób 4:5 social ad dla mojej kawiarni. Oto moje zdjęcia referencyjne: [logo + napoje]. Trzymaj się zasad — produkt na pierwszym planie, prawdziwe jedzenie z moich zdjęć, moje logo bez zmian, jeden headline czytelny z miniaturki, zero text-on-photo slopu. Pokaż 3 strukturalnie różne koncepty."*

**Opcja B — jako skill** (Hermes / Claude Code / Codex / Cursor):
```bash
git clone https://github.com/aievolutionpl/meta-ads-designer.git
cp -r meta-ads-designer ~/.hermes/skills/marketing/   # lub ~/.claude/skills/ ~/.codex/skills/ ~/.cursor/skills/
```

**Weryfikacja** — poproś agenta: *"podsumuj zasady"*. Powinien wymienić product-first, source of truth, commercial realism, hierarchię, negatywną przestrzeń, anti-slop, hard fails. Jeśli recytuje generyczne "make it premium" — nie wczytał; wklej ponownie.

Pełne kroki per host: **[`INSTALL.md`](INSTALL.md)**.

---

## ⚙️ Jak działa skill

`Meta Ads Designer` jest **framework-agnostic** — te same zasady działają na każdym agencie. Zbudowany jest **warstwowo**, każda ma jedno zadanie:

```
┌────────────────────────────────────────────┐
│ visual-advertising-engine.md               │  ← THE standard (34 zasady)
│   Product First · Source of Truth ·        │     Prompt Architecture ·
│   Hard Fails · Final Quality Check         │     Creative Workflow
└───────────────┬────────────────────────────┘
                │ podsumowany jako
                ▼
┌─────────────────────────────┐
│      design-rules.md       │  ← THE charter (wklejany gust)
│   "The Rules of Beautiful   │     Działa na KAŻDYM agencie
│    Advertising"             │
└───────────────┬─────────────┘
                │ ładowany przez
        ┌───────┼───────┐
        ▼       ▼       ▼
   ┌────────┐ ┌───────┐ ┌──────────────────┐
   │SKILL.md│ │core.md│ │  references/     │
   │ manual │ │wklejka│ │  głębia:         │
   │        │ │1 str. │ │  food/hotel/svc, │
   └────────┘ └───────┘ │  prompty, slop   │
                        └──────────────────┘
```

- **`visual-advertising-engine.md`** — *standard* (34 zasady). Co agent stosuje **przed** każdym komercyjnym visualem: Product First, Reference = Source of Truth, Prompt Architecture, Hard Fails, QA.
- **`design-rules.md`** — *charter* (gust). Angielski kanon. Samowystarczalny — wklejasz do dowolnego czatu lub wstrzykujesz do system promptu.
- **`core.md`** — *wklejka 1-stronicowa*. Esencja zasad + przykład słabego/mocnego promptu — najszybszy setup.
- **`SKILL.md`** — *procedura*. Brief → research → angles → creative → generate → QA → deliver. Loader skilli czyta frontmatter.
- **`references/`** — *głębia*: sprawdzony playbook food/hotel/serwisy, playbooki per nisza, gotowe prompty, pełny rejestr anti-slop.

### Dwa tryby produkcji (decyzja przed generacją)
| Tryb | Co to | Kiedy |
|------|-------|-------|
| **A · Natywny tekst AI** | Tekst **baked into** render AI, w scenie. Najlepsza pisownia: gpt-image-2 (Codex). Krótkie stringi. | Restauracja/venue/food — default. |
| **B · Kompozycja deterministyczna** | Generuj czyste tło, potem składaj ad (oficjalne logo + dokładna typografia + panele). | Gdy liczy się fidelity tekstu/logo (serwisy, oferty). |

### Workflow
```
1. BRIEF     — co, dla kogo, CTA, platformy (default 4:5) + zbierz refs
2. RESEARCH  — jak prezentują się topowe brandy w niszy?
3. ANGLES    — 5-10 różnych obietnic/layoutów, nie 10 color swaps
4. CREATIVE  — produkt → benefit → target → angle → metaphor → typ →
               kompozycja → światło/kamera → constraints → potem prompt
5. GENERATE  — jeden skończony ad per generacja
6. QA        — contact sheet + checklist; scale+pad (nigdy crop) przy krawędziach
7. DELIVER   — pliki + contact sheet + notki
```

---

## 🏛️ Zasady (skrót — pełny standard w Engine)

> **Product First · Reference = Source of Truth · One creative = One idea · Don't decorate, direct.**

1. **Hierarchia** — jeden dominujący element, czytelny z miniaturki, przekaz w 1s.
2. **Realna typografia** — nazwane fonty, max 3 rodziny, kontrast wagą i skalą.
3. **Paleta brandu + jeden akcent** — nigdy purple-blue default.
4. **Negatywna przestrzeń** — marże, oddech; przestrzeń = luksus.
5. **Imagery w kontekście** — produkt w realnym użyciu, realne światło, realni ludzie.
6. **Realne jedzenie z refs** — nigdy nie pozwól AI wymyślać dań, których lokal nie serwuje.
7. **Logo fidelity** — nigdy AI-redraw oficjalnego logo; wstaw oryginał.
8. **Ad spine** — headline → subline → CTA → brand cue. Piękne zdjęcie ≠ ad.
9. **Zero AI-copy** — zakazane słowa; nazwy i liczby zamiast przymiotników.
10. **QA przed wysyłką** — czytelność z miniaturki, poprawna pisownia, jeden focal point, logo fidelity.

Plus: **Commercial realism** · **Lighting is part of the product** · **Think like a photographer** · **Build depth** · **Trzy obowiązkowe kąty** (Problem/Efekt/Lifestyle) · **Visual Creative Library** · **Spójność serii** · **Hard Fail Conditions**.

---

## 📁 Struktura repo

```
meta-ads-designer/
├── SKILL.md                        # Manual agenta (procedura + routing)
├── core.md                         # 1-stronicowe zasady — wklej do dowolnego czatu
├── visual-advertising-engine.md    # THE standard — 34 zasady
├── design-rules.md                 # Charter (angielski kanon)
├── INSTALL.md                      # Setup + użycie na każdym agencie (w tym ChatGPT)
├── README.md                       # Ten manual (EN)
├── README.pl.md                    # Ten manual (PL)
├── CHANGELOG.md                    # Historia wersji
├── LICENSE                         # MIT
├── assets/meta-ads-designer-banner.png
├── examples/                       # Gotowe przykłady adów (anti, restauracja, hotel, serwisy, retail)
├── scripts/                        # extract_wordmark.py, qa.py
└── references/
    ├── hospitality-food-services-playbook.md  # Głębia: food / hotel / serwisy
    ├── layout-system.md            # Layout + panel-heights + gradient values
    ├── headline-system.md          # Rozmiary headline i kontrast
    ├── qa-gate.md                  # Brama QA i kryteria odrzucenia
    ├── anti-slop-registry.md       # Kompletne kompendium zakazów (visual + copy)
    ├── niche-playbooks.md          # Playbooki per nisza
    └── prompt-library.md           # Gotowe prompty dla dowolnego modelu
```

---

## 🧭 File map

| Plik | Do czego |
|------|----------|
| `core.md` | Wklejka 1-stron — wklej do dowolnego czatu/agenta |
| `visual-advertising-engine.md` | Standard operacyjny — 34 zasady |
| `design-rules.md` | Charter — gust |
| `SKILL.md` | Manual agenta (czyta loader skilli) |
| `INSTALL.md` | Setup per host |
| `references/hospitality-food-services-playbook.md` | Głębokie reguły food / hotel / serwisy |
| `references/prompt-library.md` | Gotowe prompty |
| `references/niche-playbooks.md` | Głębia per nisza |
| `references/anti-slop-registry.md` | Lista zakazów + grep gate |
| `README.md` | Ten manual |

---

## 🤝 Współpraca

Masz zasadę, która uratowałaby kampanię? Otwórz PR do `visual-advertising-engine.md` — to źródło kanoniczne. Zobacz [`CONTRIBUTING.md`](CONTRIBUTING.md).

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
