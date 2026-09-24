# Generated showcase: research → questions → prompt → image → analysis

This case produces the README showcase with an AI image model, following R50 and R51. All brands (PORA, NURT, NOC BRZMI) are fictional, and nothing here claims measured performance.

## 1 · Research note (abbreviated)

- Cafés in Kraków on Meta Ad Library mostly run plated dishes on dark wood → **gap:** hands and preparation in daylight.
- Bottle brands run clean packshots on white → **gap:** a loud performance banner with one verified offer.
- Event flyers in the city rely on DJ photos → **gap:** type as the hero.

## 2 · Questions asked (with the defaults accepted)

1. Offer and proof? → only the bottle has a verified first-order offer (−20%).
2. Audience? → cold, local, Instagram feed.
3. Style? → A) documentary, B) performance sticker, C) typographic poster: one per concept.
4. Placements? → 4:5, one image per concept.
5. Language? → Polish, with diacritics rendered in the image.

## 3 · Prompts

The exact prompts are in [prompts/readme-showcase.txt](prompts/readme-showcase.txt), one per concept, with every string quoted. Generate them with:

```bash
export FAL_KEY=...
python scripts/generate_fal.py examples/prompts/readme-showcase.txt --model <fal-model-id> --aspect 4:5 --out assets/showcase
```

The script writes the images and a `.log.json` with model, prompt, seed and request id.

## 4 · Analysis after generation

For each image: transcribe every word and compare it with the quoted copy (watch `ś`, `−`, `ł`); check that there is one focal point at thumbnail size; check hands, condensation and grain for artifacts; then ship it or change one decision and regenerate ([discovery-and-research.md](../references/discovery-and-research.md) §4). Record the verdicts below when the images are added.
