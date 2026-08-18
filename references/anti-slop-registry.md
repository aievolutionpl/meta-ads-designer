# 🚫 Anti-Slop Registry — the full compendium

> Compiled from production campaigns plus the widely-known anti-slop registries (visual/design + copy). This is the long form of `design-rules.md` §6 and R05 in the engine. Visual bans below; copy bans in §3.

---

## 1 · Visual slop — never in an image prompt

### Gradients / effects
| Banned | Instead |
|--------|---------|
| purple gradient / blue-to-purple | brand palette, one accent |
| glassmorphism / frosted glass / glass card | flat surface or a real texture |
| neon glow / glowing accents / glowing orbs | directional light, real sources |
| gradient text | a solid brand colour |
| dark mode with glowing accents | brand palette, a considered dark neutral |

### Background / decoration
| Banned | Instead |
|--------|---------|
| cream / sand / beige / ivory (with no reason) | true white, a saturated brand colour, a dark neutral |
| floating particles / magical sparkles | nothing, or real detail |
| geometric abstract shapes | a concrete scene / a real texture |
| isometric illustration (unless the brand is expressly built on it) | photography / the brand's actual style |

### Composition / UI
| Banned | Instead |
|--------|---------|
| over-round cards (24px+ on small elements) | 12–16px max; pills only for tags and buttons |
| repeating gradient stripes | a clean surface or a considered texture |
| hairline border + wide soft shadow together | pick ONE: a defined edge OR soft elevation |
| cards inside cards | one level, maximum |
| icons larger than the content they introduce | icon ≤ the content it introduces |
| six text sizes on one graphic | three, maximum (layout-system §2a) |

---

## 2 · Ad-specific slop — never in a creative

- ❌ Tiny icons / clip-art / thumbnail-style graphics instead of a real composition
- ❌ Text-on-photo Canva template (a box with a caption stuck onto a photo) — **the #1 rejection**
- ❌ AI-invented food when the client has real dish photos
- ❌ AI-redrawn logo (mangled wordmarks, invented crests) — place the original file
- ❌ Two focal points, or none
- ❌ A tiny footer of fake contact details or invented phone numbers
- ❌ Floating product on a gradient with a glow — the classic product-ad slop
- ❌ A beautiful photograph with no structure (no headline, no CTA, no brand cue) — that's wallpaper, not an ad
- ❌ A landscape photo force-cropped to 4:5 with the subject clipped — use the photo+panel layout instead
- ❌ Script or handwriting fonts at subline size on a busy photo — unreadable
- ❌ An interchangeable headline (`AUTHENTIC FLAVOURS`) — see the specificity test in `headline-system.md` §1

---

## 3 · Copy slop — never in an image or a caption

| Banned | Instead |
|--------|---------|
| delve, delved | look at / explore / cut |
| seamless, seamlessly | be specific: "works without friction" |
| robust | name the actual failure mode |
| elevate | improve / raise / sharpen |
| empower | "lets you" / "makes it possible" |
| tapestry | cut it |
| revolutionary / game-changer | the concrete claim |
| unlock / unleash | the actual verb |
| 🚀 in a headline | a concrete benefit |
| "Powered by AI" | what it does |
| "Join the waitlist" (on a product that isn't real) | a real CTA |
| fake company logos | the real one, or none |

**Copy rules:** open with force, take a position, use names and numbers, lead with verbs, vary sentence length, no em dashes, end on the strongest sentence. Full method: [`headline-system.md`](headline-system.md).

---

## 4 · Programmatic gate

Text deliverables (prompts, captions, prose) — run before publishing:

```bash
# 1. Visual-slop vocabulary leaking into prompts
grep -Eic "purple gradient|glassmorphism|neon glow|glowing orbs|floating particles|isometric" "$f" || echo "CLEAN"

# 2. AI copy tells
grep -Eic "delve|seamless|empower|elevate|robust|tapestry|game-changer|revolutionary|unlock|unleash|🚀" "$f" || echo "CLEAN"
```

Images — the grep above cannot see them. Use the real gate:

```bash
python scripts/qa.py out/*.png --format 4:5 --text-box 86,843,994,1290
```

→ [`qa-gate.md`](qa-gate.md) for all three layers.

> ⚠️ **False positives:** CSS variables and class names (`--purple`, `.card-lp`) are legitimate. Check context before blocking.
> ⚠️ **Meta note:** don't quote banned words in a file's own QA section — the grep will catch them. Write "stop-slop gate — PASS" instead.
