<div align="center">

# 🎨 Premium Ad Design

### Doctrina pięknego designu dla agentów AI — postery, flyery, meta ads i promocyjne grafiki

**Uczy agenta, jak wygląda piękny design — i jak go wygenerować bez AI-slopu.**

![Version](https://img.shields.io/badge/version-1.0.0-6a5acd)
![License](https://img.shields.io/badge/license-MIT-brightgreen)
![Language](https://img.shields.io/badge/lang-PL-2ea44f)
![Framework](https://img.shields.io/badge/framework-agnostic-blue)

<br/>

> **„Nie generuj 'obiektów w próżni'. Generuj reklamy, które wyglądają jak kampania — z hierarchią, typografią, realnym światłem i strukturalnym przekazem."**

<br/>

</div>

---

## 🧩 Problem

Grafiki generowane przez ChatGPT **wyglądają tak samo** — i to źle:

| 🐘 To, co widzisz | ➡️ To, co dostajesz |
|-------------------|---------------------|
| Małe ikonki, thumbnail clip-art | brak pełnej kompozycji |
| Generyczne gradienty + purple | default, nie paleta brandu |
| Text-on-photo Canva look | brak natywnego tekstu w scenie |
| AI-wymyślone jedzenie | nie to, co serwuje lokal |
| Brak hierarchii | nic nie czytelne z miniaturki |

**To jest AI-slop.** Piękny ad wygląda jak wycięty z profesjonalnej kampanii — a ten skill uczy agenta dokładnie, jak to osiągnąć.

---

## ✨ Co daje ten skill

- **🏛️ Design Doctrine** — 7 filarów pięknego designu (hierarchia, typografia, kolor, przestrzeń, imagery, logo fidelity, struktura ad).
- **🚫 Anti-Slop Gate** — skompilowane kompendium zakazów z realnych rejectów produkcyjnych + programmatic grep gate.
- **🔧 Pełny workflow** — od brief intake i researchu niszy, przez generację, po QA gate i delivery.
- **🍽️ Niche Playbooks** — jak wygląda dobry ad w restauracji, hotelu, lokalnym biznesie, retailu i na eventach.
- **📦 Biblioteka promptów** — gotowe szablony Codex/gpt-image-2 do natychmiastowego użycia.

Framework-agnostic: **działa na Hermes, Claude Code, Codex, Cursor i każdym agencie** z natywnym loaderem skilli.

---

## 📁 Struktura

```
premium-ad-design/
├── SKILL.md                        # Doctrina + workflow + routing (serce)
├── references/
│   ├── anti-slop-registry.md       # Pełne kompendium zakazów visual + copy
│   ├── niche-playbooks.md          # Jak wygląda dobry ad w każdej niszy
│   └── prompt-library.md           # Gotowe szablony promptów
├── LICENSE                         # MIT
└── README.md
```

---

## 🚀 Instalacja

### Hermes Agent
```bash
# skopiuj do katalogu skilli
cp -r premium-ad-design ~/.hermes/skills/marketing/
```

### Claude Code / Codex / Cursor
```bash
cp -r premium-ad-design ~/.claude/skills/      # Claude Code
cp -r premium-ad-design ~/.codex/skills/       # Codex CLI
cp -r premium-ad-design ~/.cursor/skills/      # Cursor
```

Gotowe. Agent automatycznie załaduje `premium-ad-design` przy zadaniach typu "zrób flyer", "meta ad", "promocyjna grafika dla restauracji".

---

## 🧠 Jak to działa

```
BRIEF INTAKE (info + ref photos)
    ↓
RESEARCH NISZY (jak wyglądają dobre adsy w tej branży)
    ↓
ANGLE MATRIX (5-10 różnych kątów, nie color swaps)
    ↓
BACKEND / MODEL SELECTION (Codex vs NB2 vs PIL)
    ↓
GENERACJA (ref images + 5-slot prompt + design doctrine)
    ↓
QA GATE (contact sheet + vision_analyze + grep slop)
    ↓
DELIVERY (ZIP + contact sheet + koszt)
```

---

## 🎯 Design Doctrine (streszczenie)

1. **Hierarchia** — jeden dominujący element (TITLE), czytelny z miniaturki.
2. **Typografia** — prawdziwe fonty, max 3 rodziny, kontrast wagi/skali.
3. **Kolor** — paleta brandu + JEDEN akcent, zero default gradientów.
4. **Przestrzeń** — generozne marże, negatywna przestrzeń = luksus.
5. **Imagery** — produkt w kontekście, realne światło, realne jedzenie z ref.
6. **Logo fidelity** — nigdy nie AI-redraw oficjalnego logo.
7. **Struktura** — headline → subline → CTA → brand cue. Piękne zdjęcie bez struktury ≠ ad.

---

## 🍽️ Niche Playbooks

| Nisza | Hero | Layout |
|-------|------|--------|
| 🍽️ Restauracja | Realne danie z ref photo | Zdjęcie góra 60% + solidny panel dół 40% |
| 🏨 Hotel / venue | Facade, golden hour | Coastal editorial, direct-booking CTA |
| 🏪 Lokalny biznes | Realny produkt/instalacja | Premium lifestyle, czytelne CTA + logo |
| 🛍️ Retail | Produkt w użyciu | Real context, studio hero |
| 🎉 Event | Mocna typografia | 1 hero + data/miejsce/CTA |

---

## 🧭 Powiązane

Ten skill **orkiestruje** istniejące biblioteki zamiast ich dublować:

- [`imagegen`](https://github.com/aievolutionpl) — backendy, ref images, koszty
- `reference-led-ad-production` — refs od klienta, packi wielu stylów
- `premium-static-ad-production` — czyste tło + deterministyczna typografia
- `gpt-image-prompt-framework` — 5-slotowy framework promptów
- [`step-beyond`](https://github.com/aievolutionpl/step-beyond) — behavioralna proaktywność

---

## 📜 Licencja

MIT — używaj, remiksuj, publikuj.

---

<br/>
<div align="center">
  <b>Created by</b><br/>
  <b>AI EVOLUTION LABS</b><br/>
  <sub>Channel Islands</sub><br/>
  <sub><a href="https://github.com/aievolutionpl/premium-ad-design">github.com/aievolutionpl/premium-ad-design</a></sub>
</div>
