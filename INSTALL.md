# 🚀 INSTALL — how to run Premium Ad Design on any agent

This plugin is **framework-agnostic**. The same rules work on every agent. Pick your host below.

---

## 1 · Hermes Agent

```bash
git clone https://github.com/aievolutionpl/premium-ad-design.git
cp -r premium-ad-design ~/.hermes/skills/marketing/
```

Hermes auto-loads `premium-ad-design` when you ask for posters/flyers/meta ads. The skill's `design-rules.md` + `SKILL.md` are read automatically.

---

## 2 · Claude Code

```bash
git clone https://github.com/aievolutionpl/premium-ad-design.git
cp -r premium-ad-design ~/.claude/skills/
```

Claude Code reads the `SKILL.md` frontmatter and loads the plugin on matching tasks.

---

## 3 · Codex CLI

```bash
git clone https://github.com/aievolutionpl/premium-ad-design.git
cp -r premium-ad-design ~/.codex/skills/
```

---

## 4 · Cursor / Windsurf

```bash
git clone https://github.com/aievolutionpl/premium-ad-design.git
cp -r premium-ad-design ~/.cursor/skills/   # Cursor
# or ~/.windsurf/skills/  # Windsurf
```

---

## 5 · ChatGPT / Claude / Gemini (chat, no skill loader)

These are chatbots, not skill runners — but the plugin still works, two ways:

**Option A — custom instruction (recommended):**
1. Open ChatGPT → Settings (or "Customize ChatGPT") → **Custom Instructions**.
2. Paste the **`design-rules.md`** file content (or this condensed version):

> "You are an expert art director for AI-generated advertising. Before creating ANY poster, flyer, meta ad or promo graphic, follow THE RULES OF BEAUTIFUL ADVERTISING: (1) one dominant element — a title readable from a thumbnail; (2) real named typefaces, max 3 families, contrast by weight and scale; (3) brand palette + one accent, never purple-blue gradient or cream/sand bg; (4) generous margins and negative space; (5) product in real context with real light — never floating on a void; (6) food must be the client's real dishes, never AI-invented; (7) never let AI redraw an official logo — place the original; (8) every ad needs the spine headline → subline → CTA → brand cue; (9) no banned AI words (delve, seamless, empower, elevate, robust, revolutionary, 🚀); (10) QA before delivering: thumbnail readability, correct spelling, one focal point, logo fidelity, contrast. Always ask for the client's reference photos (logo, venue, food, products) and use them to preserve authenticity."

**Option B — knowledge/attachment:**
- In ChatGPT you can attach `design-rules.md` as a file (paid plans allow file upload). Then prompt: "Apply THE RULES OF BEAUTIFUL ADVERTISING from the attached file."

> **Prompt starter for the chat:** "Make a 4:5 social ad for [business]. Here are the reference photos: [attach logo/venue/food]. Follow the Premium Ad Design rules: one headline readable from a thumbnail, brand palette, real typography, no text-on-photo slop, real food from my photos, my logo unaltered, CTA 'Reserve a table'. Show me 3 structurally different concepts first."

---

## 6 · Any custom agent / API

Inject **`design-rules.md`** into your system prompt (it's fully self-contained), or load `SKILL.md` if your harness supports native skills.

---

## ✅ Verify it's loaded

Ask the agent: *"Summarize the 10 rules of beautiful advertising from the Premium Ad Design plugin."*
- Correct = the agent lists hierarchy, real typography, brand palette, negative space, imagery in context, logo fidelity, ad spine, banned AI words, QA.
- If it recites generic "make it premium and professional" — it didn't load the rules. Re-check the install path / re-paste.

---

## 🧭 Which file does what

| File | Use it for |
|------|-----------|
| `design-rules.md` | The rules — paste into any chat, or read as the canonical charter |
| `SKILL.md` | Agent operating manual (skill loaders read this) |
| `INSTALL.md` | This file — setup per host |
| `references/prompt-library.md` | Ready-to-use prompt recipes |
| `references/niche-playbooks.md` | Per-industry depth |
| `references/anti-slop-registry.md` | Full banned-pattern list + grep gate |
| `README.md` | The manual / homepage |
