# Platform Compliance & Multi-Ratio

> The operating tool behind **R38**: an ad is finished only when it survives the platform it ships on. Compose for the placement — safe zones, captions, CTA and ratios — and deliver a native file per placement, never one image the client has to hack.

A creative can pass QA on the canvas and still die under platform chrome: a CTA under a feed button, a headline hidden by the Stories UI, a 4:5 image cropped into a 9:16 short. Compliance is part of the deliverable.

---

## 1 · Why canvas-perfect dies in the feed

Platforms overlay their own UI on top of your creative: the caption/CTA bar on Meta feed, the top bar and bottom actions on Stories/Reels, the text-safe band on TikTok/Shorts, the shop overlay on marketplace. Design the margins for the *rendered* ad, not the naked image.

---

## 2 · Safe zones per platform

| Platform / placement | Ratio | Keep-clear zone |
|----------------------|-------|-----------------|
| **Meta / IG feed** | 4:5 (1080×1350) | Lower ~15% reserved for the caption/CTA bar; nothing critical within ~8% of the edges (R08) |
| **Meta / IG Reels, Stories** | 9:16 (1080×1920) | Top ~250px and bottom ~320px clear of UI overlays; text inside the central safe band |
| **TikTok** | 9:16 (1080×1920) | Right-side text-safe band + bottom caption area; keep key text central |
| **YouTube Shorts** | 9:16 (1080×1920) | Top title zone and bottom action rail clear; text central |
| **Marketplace / e-com** | 1:1 (1080×1080) | Product in-frame with margin for the shop overlay and title |

The 4:5/9:16 chrome zones are gated; the margin guidance is placement advice — see the layout numbers in [`layout-system.md`](layout-system.md).

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
