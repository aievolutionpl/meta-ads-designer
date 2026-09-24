# Meta Ads Designer

### Od briefu do reklamy z wyraźnym pomysłem.

Skill dla agentów AI, który pomaga dobierać **kompozycję, typografię, kolor i kierunek wizualny**, a następnie zapisywać te decyzje w precyzyjnych promptach do generowania obrazów.

[English](README.en.md) · [Instrukcja skilla](SKILL.md) · [Szybki start](#szybki-start) · [Przykłady](examples/README.md)

![Version](https://img.shields.io/badge/version-6.5.0-222222)
![License](https://img.shields.io/badge/license-MIT-222222)
![Model independent](https://img.shields.io/badge/prompts-model_independent-222222)

![Meta Ads Designer — AI-generated showcase](assets/showcase/hero.jpg)

| | | |
|---|---|---|
| ![PORA](assets/showcase/ad-pora.jpg) | ![NURT](assets/showcase/ad-nurt.jpg) | ![NOC BRZMI](assets/showcase/ad-noc-brzmi.jpg) |

*Przykłady wygenerowane w całości przez AI z promptów skilla: bez retuszu i bez nakładek w kodzie. Marki są fikcyjne. [Prompty, analiza i runda 2](examples/08-generated-showcase.md).*

## Co robi ten skill

Pomaga agentowi odpowiedzieć na pytania, które decydują o wyglądzie reklamy: co widz ma zrozumieć, na co spojrzy najpierw, jak ułożyć tekst i kiedy wybrać fotografię, ilustrację albo plakat typograficzny.

Działa przy tworzeniu reklam social media, flyerów, posterów, fotografii produktowej i koncepcji kampanii. Możesz zamówić sam prompt lub użyć go razem z narzędziem generowania obrazów. Wiedza projektowa jest niezależna od modelu.

## Zobacz, skąd bierze się efekt

| Brief | Decyzja projektowa | Co pokazuje grafika |
|---|---|---|
| Kawiarnia: zachęcić do spokojnego śniadania | Bliski kadr, naturalne światło, krótki nagłówek szeryfowy | Jeden apetyczny produkt i czytelny rytm obrazu oraz tekstu |
| Wydarzenie muzyczne: zwrócić uwagę na nazwę | Nazwa jako dominanta, skondensowany krój, mocny kontrast | Flyer, który działa bez zdjęcia |
| Ceramika: pokazać formę przedmiotu | Duża sylwetka, stonowana paleta, kierunkowy cień | Materiał i kształt prowadzą kompozycję |

Każda kreacja ma własny język wizualny. Łączy je hierarchia i świadomy dobór elementów.

Ten sam zestaw pomysłów można rozwinąć w spokojniejszym kierunku editorial:

![Wariant editorial: naturalne światło, spokojniejsze kolory i czytelna hierarchia](assets/meta-ads-designer-editorial.png)

*Druga plansza demonstracyjna. Zmienia się charakter art direction, a nie zakres możliwości skilla.*

## Nowość w 6.0: research, pytania i generacja AI

- **Zawsze generacja AI od zera.** Każda finalna reklama powstaje w modelu obrazu (API, Codex albo narzędzie hosta), razem z nagłówkiem i układem. Żadnego składania grafik w HTML czy kodzie (R50).
- **Najpierw research, potem pytania.** Agent sprawdza stronę marki, Meta Ad Library, konkurencję i opinie, a potem zadaje 3–6 trafnych pytań naraz, z domyślną odpowiedzią przy każdym. Dopiero z notatki decyzyjnej pisze prompty (R51).
- **Analiza po generacji.** Agent przepisuje każde słowo z obrazu, sprawdza wierność produktu i logo, robi test miniatury i zmienia jedną decyzję na iterację.

### Warstwa 2026

Skill wie teraz, jak wyglądają aktualne reklamy Meta i dlaczego pewne struktury przekonują:

- **Atlas stylów 2026** — dwadzieścia sześć języków wizualnych: od plakatu z wielką typografią i edytorialu z fleszem, przez natywne notatki, banery performance ze stickerem, po taktylny zin. Każdy ma typografię, kolor, sygnaturowy detal, fragment promptu i typowy błąd.
- **Formaty statyczne** — piętnaście szkieletów perswazji (stat drop, stos recenzji, produkt z calloutami, porównanie, offer stack…). Format jest dostępny tylko wtedy, gdy istnieje jego dowód.
- **Fakty platformy 2026** — ujednolicona strefa bezpieczna Reels/Stories (14% góra, 35% dół), eksport 4:5 w 1440×1800, rozszerzanie obrazu i generowane tła w Advantage+, etykiety „AI info” oraz grupowanie niemal identycznych reklam przez Andromedę.
- **Cztery nowe reguły, R45–R48** — jeden język wizualny na reklamę, format wynika z dowodu, różnorodność daje zasięg, projekt pod system placementów 2026.

## Jak działa

```mermaid
flowchart LR
    A["Brief: odbiorca i oferta"] --> B["Jedna myśl reklamy"]
    B --> C["Kompozycja, typografia, kolor"]
    C --> D["Gotowy prompt"]
    D --> E["Obraz i ocena wizualna"]
```

1. **Research i pytania** — agent bada markę, Ad Library i konkurencję, zadaje 3–6 pytań i spisuje notatkę decyzyjną.
1. **Brief** — agent ustala odbiorcę, prawdziwą ofertę, cel, format i dostępne materiały.
2. **Pomysł** — wybiera, co pokaże korzyść: produkt, działanie, detal, sytuacja lub typografia.
3. **Art direction** — wybiera format, na który pozwala dowód, i jeden język wizualny, a potem określa dominantę, kolejność czytania, przestrzeń na tekst, fonty i paletę.
4. **Prompt** — zapisuje konkretną kompozycję, dokładne treści i ograniczenia.
5. **Ocena** — sprawdza spójność promptu; po wygenerowaniu obrazu również czytelność, pisownię i zgodność z materiałami.

Jeśli prosisz tylko o prompt, praca kończy się na jego sprawdzeniu. Agent nie ocenia obrazu, którego nie widział.

## Szybki start

### W zwykłym czacie

Wklej [core.md](core.md) jako instrukcję lub dodaj go jako materiał do rozmowy. Potem podaj krótki brief:

> Przygotuj prompt do reklamy 4:5 mojej kawiarni. Odbiorcy: osoby szukające śniadania w okolicy. Załączam zdjęcie croissanta i logo. Cel: zachęcić do wizyty. Nagłówek: „Poranek ma warstwy.” Dobierz kompozycję, typografię i kolor. Zachowaj wygląd produktu i logo. Nie dodawaj niepotwierdzonych cen ani promocji.

### Jako skill dla agenta

Sklonuj repozytorium i umieść cały katalog w katalogu skilli swojego agenta:

```bash
git clone https://github.com/aievolutionpl/meta-ads-designer.git
```

Instrukcją wejściową jest [SKILL.md](SKILL.md). Szczegóły dla poszczególnych hostów znajdziesz w [INSTALL.md](INSTALL.md).

## Co pomaga ograniczyć AI-slop

- **Jedna dominanta.** Produkt, nazwa wydarzenia lub oferta ma pierwszeństwo przed dekoracją.
- **Typografia z rolą.** Konkretny krój, ciężar, szerokość, układ wierszy i hierarchia.
- **Kolor wynikający z marki.** Palety i style są dobierane do briefu; nie ma jednego „premium looku” dla wszystkich.
- **Prawdziwe materiały.** Referencje określają wygląd produktu, lokalu i identyfikacji.
- **Treść bez zmyślonych faktów.** Żadnych fikcyjnych opinii, cen, terminów czy wyników.
- **Korekta konkretnego problemu.** Agent poprawia kompozycję albo komunikat zamiast dopisywać „bardziej pięknie, cinematic, 8K”.

## Tekst i logo w reklamie

Cała reklama, łącznie z tekstem, powstaje w modelu AI. Skill pisze dokładne cytaty tekstu z polskimi znakami, podaje hierarchię i położenie, a logo i produkt przekazuje jako obrazy referencyjne. Po generacji agent przepisuje każde słowo z obrazu. Przy błędzie generuje ponownie albo robi celowaną edycję tym samym modelem, zamiast nakładać tekst kodem.

## Materiały w repozytorium

| Materiał | Do czego służy |
|---|---|
| [SKILL.md](SKILL.md) | Instrukcja agenta i dobór materiałów |
| [core.md](core.md) | Samodzielna instrukcja do wklejenia w czacie |
| [Art direction](references/art-direction.md) | Od celu marketingowego do kompozycji i typografii |
| [Prompt craft](references/prompt-craft.md) | Pisanie i sprawdzanie promptów |
| [Research i pytania](references/discovery-and-research.md) | Research, pytania przed generacją, notatka decyzyjna, analiza wyników |
| [Atlas stylów 2026](references/style-atlas-2026.md) | Dwadzieścia sześć języków wizualnych, trend slop, czytanie plansz referencyjnych |
| [Formaty statyczne](references/static-ad-formats.md) | Szkielety perswazji, dowód, lejek i dopasowanie do branży |
| [Przykłady promptów](examples/05-model-independent-directions.md) | Flyer, gastronomia i usługa lokalna |
| [Kierunki 2026](examples/07-2026-style-directions.md) | Briefy „format + styl” i zestaw kampanii pod Andromedę |
| [Visual Advertising Engine](visual-advertising-engine.md) | Kanoniczne reguły R01–R52 |
| [Layout system](references/layout-system.md) | Punkty wyjścia dla siatki, marginesów i skali tekstu |
| [Diagnostyka kreacji](references/creative-diagnostics.md) | Z eksportu Ads Managera do kolejnego briefu (`scripts/creative_diagnostics.py`) |
| [Platformy](references/platform-compliance.md) | Strefy bezpieczne, limity tekstu, Advantage+, etykiety AI |
| [QA gate](references/qa-gate.md) | Ocena rzeczywiście wygenerowanych obrazów |
| [Pozostałe przykłady](examples/README.md) | Briefy, prompty i omówienie decyzji |

## Weryfikacja i rozwój

```bash
pip install -r requirements.txt
python scripts/check_docs.py
python scripts/test_qa.py
python scripts/test_diagnostics.py
```

Kontrole dokumentacji sprawdzają linki, odwołania do reguł i wersje. Skrypt QA bada wybrane cechy techniczne obrazu; ocenę kompozycji, wiarygodności i zgodności z briefem trzeba wykonać osobno. Wyniki kampanii wymagają pomiaru po publikacji.

Zasady współpracy: [CONTRIBUTING.md](CONTRIBUTING.md). Historia zmian: [CHANGELOG.md](CHANGELOG.md).

---

Created by **AI Evolution Labs** · [MIT License](LICENSE) · [aievolutionlabs.io](https://aievolutionlabs.io/)
