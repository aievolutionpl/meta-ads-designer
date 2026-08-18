<div align="center">

# 🎬 Meta Ads Designer

### Uniwersalny standard reklamy dla agentów AI — przestań generować AI-slop, zacznij generować kampanie.

**Postery · Flyery · Meta Ads · Fotografia produktowa · Grafiki e-commerce** — dla restauracji, hoteli, lokalnych biznesów i retailu.

[🇬🇧 English](README.md) · [PL](README.pl.md)

![Version](https://img.shields.io/badge/version-5.0.0-6a5acd)
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
┌──────────────────────────────────────────────────┐
│  visual-advertising-engine.md                    │  ← ZASADY, R01–R34
│  jedno źródło prawdy · stabilne ID reguł         │     cytuj je w QA
└───────┬──────────────────────────────────────────┘
        │ wykonywane przez
        ▼
┌────────────────────┬────────────────────┬────────────────────┐
│ layout-system.md   │ headline-system.md │ qa-gate.md         │
│ siatka · skala     │ archetypy          │ skrypt + vision    │
│ palety · layouty   │ budżety · CTA      │ + rubryka punktowa │
│ JAK MA WYGLĄDAĆ    │ CO MA MÓWIĆ        │ CZY MOŻNA WYSŁAĆ   │
└────────────────────┴─────────┬──────────┴────────────────────┘
                               │ pokazane w
                               ▼
                      ┌──────────────────┐
                      │    examples/     │  ← gotowe briefy → prompty
                      │  zero placeholder│     → werdykty QA → poprawki
                      └────────┬─────────┘
                               │ ładowane przez
                 ┌─────────────┼─────────────┐
                 ▼             ▼             ▼
           ┌──────────┐  ┌──────────┐  ┌──────────────┐
           │ SKILL.md │  │ core.md  │  │ references/  │
           │ workflow │  │ wklejka  │  │ głębia nisz  │
           │          │  │ 1 strona │  │ + anti-slop  │
           └──────────┘  └──────────┘  └──────────────┘
```

**Podział jest celowy.** Zasady mówią *co znaczy dobrze*; trzy pliki systemowe zamieniają to na **liczby, słowa i próg jakości**; examples to udowadniają; `SKILL.md` to wykonuje; `core.md` jedzie wszędzie. Gust podróżuje; procedura się adaptuje.

---

## 🏛️ Co to faktycznie egzekwuje

Pełny standard w **[`visual-advertising-engine.md`](visual-advertising-engine.md)** — 34 zasady ze stabilnymi ID (`R01`–`R34`), które cytujesz w werdykcie QA.

> **Product First · Reference = Source of Truth · One creative = One idea · Don't decorate, direct.**

**Zasady** — hierarchia czytelna z miniaturki · commercial realism (perspektywa, grawitacja, cienie, realne materiały) · światło opisane przez to, *co robi* · jawna decyzja kamery · głębia · produkt w użyciu · trzy obowiązkowe kąty (Problem/Efekt/Lifestyle) · spójność serii · anti-slop · hard fails.

**Liczby** ([`layout-system.md`](references/layout-system.md)) — siatka 12-kolumnowa, marginesy 86px, skala typograficzna w px, nazwane pary fontów z fallbackami, startowe palety per branża, trzy kanoniczne layouty z dokładnymi wysokościami paneli i wartościami scrimu, kontrast ≥4.5:1.

**Słowa** ([`headline-system.md`](references/headline-system.md)) — test specyficzności, dziesięć archetypów headline'u, budżety znakowe spięte ze skalą typograficzną, CTA per branża po PL i EN, oraz strategia diakrytyków, dzięki której polski headline nie wyrenderuje się jako `ZOSTAN` bez ogonka.

**Próg** ([`qa-gate.md`](references/qa-gate.md)) — `scripts/qa.py` do tego, co mierzy maszyna, prompt vision zwracający strukturalny JSON (transkrybuje tekst, a nie potakuje), i rubryka 10 kryteriów. Wysyłasz przy **≥16/20 i zerowych hard failach**.

### Jeden test, który wycina większość AI-copy

> Czy konkurent mógłby wkleić ten headline na swoją reklamę bez zmiany choćby jednego słowa?

| ❌ | ✅ |
|---|---|
| Autentyczne smaki | Souvlaki prosto z grilla |
| Twoja idealna ucieczka | Widok na morze, 4 minuty od portu |
| Jakość, której możesz zaufać | 1400 kominków zamontowanych na wyspie |
| Poczuj różnicę | Zimny dom w piątek. Ciepły w poniedziałek. |

---

## 🧠 Workflow

```
1. BRIEF     — co promujemy, dla kogo, CTA, platformy + zbierz refs
2. RESEARCH  — jak prezentują się topowe brandy w niszy? Jeśli klient ma
               adsy, które lubi — to jest źródło prawdy stylu
3. ANGLES    — 5-10 różnych obietnic/layoutów, nie 10 color swaps
4. CREATIVE  — produkt → benefit → target → angle → metaphor → typ →
               kompozycja → światło/kamera → constraints → potem prompt
5. TRYB      — tekst natywny w renderze czy kompozycja deterministyczna?
               (diakrytyki, apostrofy, ceny, logo → deterministyczna)
6. GENERATE  — jeden skończony ad per generacja; refs z nazwaną rolą;
               prompt 11-częściowy, ZERO placeholderów
7. QA        — scripts/qa.py + vision pass + rubryka; wysyłka przy >=16/20
8. DELIVER   — pliki + contact sheet + punktacja per obraz + notki
```

---

## 📁 Struktura repo

```
meta-ads-designer/
├── SKILL.md                        # Manual agenta (procedura + routing)
├── visual-advertising-engine.md    # ZASADY, R01–R34 — jedno źródło prawdy
├── design-rules.md                 # Czytelny charter + indeks do reszty
├── core.md                         # 1-stronicowa wklejka do dowolnego czatu
├── INSTALL.md                      # Setup per host
├── CHANGELOG.md
├── examples/                       # Gotowe briefy → prompty → werdykty QA
│   ├── 00-anti-examples.md         #   słaby vs skończony, obok siebie
│   ├── 01-restaurant-real-food.md  #   Tryb A · real-food hero
│   ├── 02-hotel-editorial.md       #   Tryb B · editorial split
│   ├── 03-services-problem-effect.md
│   └── 04-retail-product-in-use.md
├── references/
│   ├── layout-system.md            # Siatka, skala, palety, layouty, tryby
│   ├── headline-system.md          # Archetypy, budżety, diakrytyki, CTA
│   ├── qa-gate.md                  # Gate punktowy + prompt vision + rubryka
│   ├── hospitality-food-services-playbook.md
│   ├── niche-playbooks.md
│   ├── prompt-library.md
│   └── anti-slop-registry.md
├── scripts/
│   ├── qa.py                       # Deterministyczna warstwa QA
│   └── extract_wordmark.py         # Biały wordmark z logo na jednolitym tle
└── LICENSE
```

---

## 🧭 File map

| Chcę… | Otwórz |
|-------|--------|
| wkleić jedną stronę do czatu | `core.md` |
| poznać zasady | `visual-advertising-engine.md` |
| wiedzieć, jak duży jest headline | `references/layout-system.md` |
| wiedzieć, co headline ma mówić | `references/headline-system.md` |
| zdecydować, czy to wysyłam | `references/qa-gate.md` + `scripts/qa.py` |
| zobaczyć skończony prompt | `examples/` |
| ogarnąć brief restauracji / hotelu / serwisu | `references/hospitality-food-services-playbook.md` |
| zainstalować to na swoim agencie | `INSTALL.md` |

---

## 🤝 Współpraca

Masz zasadę, która uratowałaby kampanię? Otwórz PR do `visual-advertising-engine.md` — to źródło kanoniczne, reszta plików je podsumowuje. Nowe zasady dostają kolejne wolne `R`; istniejących nigdy nie przenumerowujemy. Zobacz [`CONTRIBUTING.md`](CONTRIBUTING.md).

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
