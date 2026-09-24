# Creative diagnostics: from numbers to the next brief

> The operating tool behind **R49**. When the user supplies results, such as an Ads Manager export, a screenshot of metrics or a verbal report, read them as evidence about the *creative* and turn every problem into one concrete change for the next brief. Metrics diagnose; they never design.

Skills for Meta ads are most useful as repeatable jobs with a fixed input and output: diagnose a CPA spike, detect creative fatigue, analyse competitor creative, write the client summary. This file is the designer's version of those jobs.

---

## 1 · Input contract

- **Best:** a CSV export from Ads Manager at ad level, with `Ad name`, `Impressions`, `Reach` or `Frequency`, `Amount spent`, `Link clicks` or `CTR`, `Results` or `Cost per result`, and for video `3-second video plays` and `ThruPlays`.
- **Acceptable:** a screenshot or pasted table. Transcribe the numbers first and say which are missing.
- **Not evidence:** "it isn't working" without numbers. Ask for the export, or proceed with a creative review and say that performance was not assessed.

Run the helper when a CSV is available:

```bash
python scripts/creative_diagnostics.py export.csv            # readable report
python scripts/creative_diagnostics.py export.csv --json     # for further processing
```

It compares each ad with the account's own median, skips ads under 1,000 impressions and prints a next-brief action for each flag. It uses only the Python standard library.

## 2 · Symptom → creative cause → change

Read the funnel in order and stop at the first break: the earliest broken step explains the later ones.

| Symptom | Likely creative cause | Change in the next brief |
|---|---|---|
| Frequency ≥ 2.5 (cold) and CTR falling | Fatigue: the audience has seen it | New concept: persona, hook, format or style (R47). A recolour will not help |
| Low 3-second view rate / thumb-stop | The first frame does not stop the scroll | Bigger promise, one focal point, stronger contrast, type as hero (R36, R45) |
| Good hook, weak hold (ThruPlay ÷ 3 s) | The opening promises more than the middle delivers | Show product or proof earlier; cut the setup (R39) |
| Low CTR, normal hook | The message or the offer is not landing | New hook mechanism or a proof format: stat drop, review stack (R46) |
| High CPM, normal targeting | Low relevance, or a near-duplicate of other ads | Make it visibly distinct from the rest of the set (R47) |
| Good CTR, high CPA | Ad and landing page promise different things | Continuity note: the page must open with the ad's promise (R37 §4) |
| Low CTR and high CPA | The creative attracts the wrong click or none | Re-decide the audience moment and the takeaway before the visuals (R43) |
| Clear winner | The angle works for this audience | Iterate for new personas and settings; keep the angle (R47) |

## 3 · Output contract

Deliver four things, in this order:

1. **Verdict per ad:** healthy, watch, replace or winner, each with the number behind it.
2. **Pattern across ads:** what the winners share (format, style, hook, persona) and what the losers share. Name the variable only when it was actually isolated. Otherwise call it a hypothesis.
3. **Next briefs:** for each ad to replace, one brief line in the working-note format, for example `Persona: first-time buyer · Hook: objection kill · Format: comparison · Style: native interface`.
4. **What is unknown:** missing columns, small samples and attribution limits.

## 4 · Guardrails

- Never claim a creative change *caused* a result unless a controlled test isolated it (R43).
- Under roughly 1,000 impressions or a few conversions, report a hint, not a verdict.
- Compare with the account's own median before quoting industry benchmarks; verticals differ widely.
- Do not change budgets, pause ads or publish anything because a diagnosis suggests it. Recommend it; the user acts.
- Numbers never override brand identity, facts or the proof rule. A "winning" fake-urgency ad is still a hard fail.

## 5 · Sources

- Metaflow, [Best 10 Claude skills for Meta ads](https://metaflow.life/blog/claude-skills-for-meta-ads): skills as repeatable jobs, with CPA diagnostics, creative fatigue detection and competitor creative analysis among the highest-leverage.
- Fatigue thresholds: [creative-performance-loop.md](creative-performance-loop.md) §5 and its sources.
