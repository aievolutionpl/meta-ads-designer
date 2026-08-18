# 🚫 Anti-Slop Registry — pełne kompendium

> Skompilowane z `jarvis-anti-slop` (visual/design) + `stop-slop` (copy) + realnych rejectów z produkcji. **Single source of truth:** obraz/design → ten plik + `jarvis-anti-slop`; copy → `stop-slop`. Nie utrzymuj rozbieżnych kopii.

---

## 1. Visual slop — NIGDY w promptach obrazów

### Gradient / efekty
| Banned | Zamiast |
|--------|---------|
| purple gradient / blue-to-purple | paleta brandu, jeden akcent |
| glassmorphism / frosted glass / glass card | płaskie tło lub realna tekstura |
| neon glow / glowing accents / glowing orbs | kierunkowe światło, realne źródła |
| gradient text | solidny kolor brandu |
| dark mode with glowing accents | paleta brandu, przemyślany ciemny neutral |

### Tło / dekoracje
| Banned | Zamiast |
|--------|---------|
| cream / sand / beige / ivory (bez powodu) | true white, nasycony kolor brandu, ciemny neutral |
| floating particles / magical sparkles | brak lub realne detale |
| geometric abstract shapes | konkretna scena / realna tekstura |
| isometric illustration (chyba że brand express) | fotografia / właściwy styl |

### Kompozycja / UI
| Banned | Zamiast |
|--------|---------|
| over-round cards (24px+ na małych) | 12-16px max, pill tylko dla tagów |
| repeating gradient stripes | czysta powierzchnia / przemyślana tekstura |
| hairline border + wide soft shadow razem | wybierz JEDNO: definiowana krawędź LUB miękka elewacja |
| cards inside cards (Cardocalypse) | max jeden poziom |
| massive icons bigger than content | ikona ≤ treść, którą wprowadza |

---

## 2. Treściowe slopy reklam — NIGDY w obrazie

- ❌ Małe ikonki / clip-art / thumbnail-style graphics zamiast pełnej kompozycji
- ❌ Text-on-photo Canva template (ramki + napis naklejony na zdjęcie)
- ❌ AI-wymyślone jedzenie, gdy klient ma realne zdjęcia dań
- ❌ Logo AI-redraw (przekręcone wordmarki, cresty) — wstaw oryginał
- ❌ Dwa focal points / brak hierarchii
- ❌ Tiny footer z fake danych kontaktowych / numerami
- ❌ Floating product na gradient + glow (produktowy slop)
- ❌ Piękne zdjęcie bez struktury (brak headline/CTA/brand cue) — to nie ad

---

## 3. Copy slop — NIGDY w obrazie ani captions

| Banned | Zamiast |
|--------|---------|
| delve, delved | look at / explore / cut |
| seamless, seamlessly | specific: "works without friction" |
| robust | nazwij realny failure mode |
| elevate | improve / raise / sharpen |
| empower | "let you" / "make possible" |
| tapestry | CUT |
| revolutionary / game-changer | konkret |
| 🚀 na headline | konkretna korzyść |
| "Powered by AI" | co robi |
| "Join the waitlist" | realne CTA |
| fake company logos | prawdziwe / brak |

**Reguły copy:** otwórz mocno, zajmij stanowisko, użyj nazw i liczb, czasowniki, zróżnicowana długość zdań, bez em dashów, koniec na najmocniejszym zdaniu.

---

## 4. Programmatic gate (uruchamiamy przed publikacją)

```bash
# 1. Visual gate (obraz / HTML / CSS)
grep -ci "purple\|glassmorphism\|neon glow\|glowing\|floating\|isometric" <plik> || echo "CLEAN"

# 2. Copy gate (proza / caption / email)
grep -ci "delve\|seamless\|empower\|elevate\|robust\|tapestry\|game-changer\|revolutionary\|🚀" <plik> || echo "CLEAN"
```

> ⚠️ **False positives:** CSS variables i nazwy klas (`--purple`, `.card-lp`) są legalne. Sprawdź kontekst, blokuj tylko realne slopy.
> ⚠️ **Meta-uwagi:** nie cytuj zakazanych słów w sekcji "QA" samego pliku — grep je złapie. Zamiast tego napisz "Zgodne z premium-ad-design / stop-slop — PASS".
