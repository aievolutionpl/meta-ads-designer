# Platform Compliance & Multi-Ratio

> The operating tool behind **R38** and **R48**: an ad is finished only when it survives the platform it ships on. Compose for the placement — safe zones, captions, CTA and ratios — and deliver a native file per placement, never one image the client has to hack.

A creative can pass QA on the canvas and still die under platform chrome: a CTA under a feed button, a headline hidden by the Stories UI, a 4:5 image cropped into a 9:16 short. Compliance is part of the deliverable.

---

## 1 · Why canvas-perfect dies in the feed

Platforms overlay their own UI on top of your creative: the caption/CTA bar on Meta feed, the top bar and bottom actions on Stories/Reels, the text-safe band on TikTok/Shorts, the shop overlay on marketplace. Design the margins for the *rendered* ad, not the naked image.

---

## 2 · Safe zones per platform

| Platform / placement | Ratio | Keep-clear zone |
|----------------------|-------|-----------------|
| **Meta / IG feed** | 4:5 (design 1080×1350, export 1440×1800) | Lower ~15% reserved for the caption/CTA bar; nothing critical within ~8% of the edges (R08) |
| **Meta / IG Reels, Stories** | 9:16 (1080×1920) | Unified safe zone since March 2026: top 14% (~269px), bottom 35% (~672px), sides 6% (~65px) clear of UI; text inside the central band (R48) |
| **TikTok** | 9:16 (1080×1920) | Right-side text-safe band + bottom caption area; keep key text central |
| **YouTube Shorts** | 9:16 (1080×1920) | Top title zone and bottom action rail clear; text central |
| **Marketplace / e-com** | 1:1 (1080×1080) | Product in-frame with margin for the shop overlay and title |

The 9:16 chrome zones are gated by `scripts/qa.py`; the 4:5 bottom zone is placement advice — see the layout numbers in [`layout-system.md`](layout-system.md). Stories alone overlay less of the bottom (about 20%), but one 9:16 file usually serves both placements, so design to the Reels zone.

---

## 3 · Ratios & re-layout (never a dumb crop)

Changing ratio is a **recomposition**, not a crop. Cropping removes hierarchy (R07) — a headline or CTA that survives on 4:5 silently vanishes on 9:16.

- **Re-layout the type:** the headline, subline, CTA and logo are **re-seated** for the new frame, on the same or a re-arranged layout.
- **Re-position the product:** the hero stays the focal point (R02) and keeps its margin (R08) in the new ratio.
- **Recheck the gate:** every re-ratioed version passes QA (R34) on its own — never inherited from the source.
- **Scale+pad over crop** at the edges, exactly as the QA step prescribes.

Deliver **one native file per placement** (4:5 feed, 9:16 short, 1:1 marketplace, 16:9 video) rather than asking the user to reformat.

---

## 4 · Caption, CTA and text-overlay spec

- **Ad spine stays complete** in every placement: headline → subline → CTA → brand cue.
- **CTA is legible and reachable** — not under a platform button, not overlapping the caption bar.
- **On-screen text is large and purposeful** (R39 for video); never a mini-caption that disappears at feed size (R33).
- **Diacritics correct** in every ratio and format (R30-text).

---

## 5 · Deliverables per placement

For a campaign brief, deliver:

1. The **master** creative (largest useful ratio) + the QA verdict.
2. **Native re-layouts** for each requested placement, each QA'd.
3. A **compliance note** naming the safe zone and CTA position per file.
4. If the landing page is known, the **continuity note** (R37 §4) that ties ad promise to page.

If a placement can't be produced without breaking hierarchy, say so and propose the re-layout instead of shipping a cropped loser.

---

## 6 · The 2026 Meta placement system (R48)

Research summary, September 2026. Platform numbers change; verify them in the [Meta Ads Guide](https://www.facebook.com/business/ads-guide/update) before final delivery.

### 6a · Text fields around the image

| Field | Visible before truncation | Design consequence |
|---|---|---|
| Primary text | ~125 characters, then "See more" (the field accepts more) | The hook lives in the first line and in the image |
| Headline | 40 characters; small phones may show ~27 | Front-load the key words |
| Description | ~30 characters | Optional; never the only place for essential information |

### 6b · Text on the image

The old 20% text rule was retired in 2020, so text-heavy images are no longer rejected. Practitioners still report weaker delivery and CTR when text covers more than roughly a third of the image. Use on-image text for the hook, offer or one proof point, and move the rest to the text fields. Type-led formats (bold statement, native interface) are deliberate exceptions: the type is the image, so keep it large and short.

### 6c · Advantage+ creative enhancements

Advantage+ can adjust brightness and contrast, add template overlays and text bars, rephrase and move text, expand images to fill other placements, animate stills and generate new backgrounds. Several enhancements have been on by default. Meta's in-house image model (Muse Image, announced 7 July 2026) is rolling into these tools during Q3 2026.

Design consequences:
- **Keep critical content central.** Expansion adds pixels around the frame; anything at the edge may be recomposed.
- **Leave clean, extendable edges.** Plain backgrounds, sky, walls and soft-focus areas expand believably; a product cut off at the edge invites invented product.
- **Name the risky enhancements.** For product-fidelity, food, real-estate and regulated work, recommend the user review or switch off image expansion, background generation and text generation, and check every placement preview before launch.
- **Supply native ratios yourself** when fidelity matters, instead of relying on automatic expansion.

### 6d · AI disclosure and misleading formats

- Ads created or significantly edited with generative AI can carry an "AI info" label in the ad's details and in the Ad Library. Meta applies it for its own tools and when it detects provenance signals such as C2PA metadata. It is a transparency notice, not a penalty. Never strip provenance data or disguise AI use to avoid it.
- Never draw fake functional UI: play buttons on a still, close icons, notification badges, fake checkboxes or system alerts.
- Never imitate a real person, news outlet, platform account or another brand's interface.
- Before/after imagery and some health, weight-loss, finance and personal-attribute claims are restricted. Check the current advertising standards for the category before choosing those formats ([static-ad-formats.md](static-ad-formats.md) §3).

### 6e · Sources

- [Meta Ads Guide](https://www.facebook.com/business/ads-guide/update), the source of truth for current specs.
- Safe-zone summaries of the March 2026 unified update, for example [Aperture](https://aperture.london/blog/meta-ad-safe-zones-2026) and [AdNabu](https://blog.adnabu.com/meta-ads/meta-safe-zones/).
- Character-limit references such as [SocialRails](https://socialrails.com/blog/facebook-ad-character-limits).
- Advantage+ enhancement guides, for example [Flighted](https://www.flighted.co/blog/metas-advantage-plus-ai-creative-enhancements-each-one-explained), and coverage of Muse Image ([Forbes](https://www.forbes.com/sites/gabrielalinzainescu/2026/07/08/metas-new-image-model-is-competing-for-ad-budgets/)).
- Meta, [Expanding GenAI transparency for ads](https://about.fb.com/news/2025/02/gen-ai-transparency-metas-ads-products/), and Meta Help, [How AI-generated images are labeled in ads](https://www.meta.com/help/artificial-intelligence/355108217670024/).
