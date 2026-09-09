---
name: meta-ads-designer
description: Art-direct social ads, posters and flyers and write model-independent image prompts when a user requests advertising visuals, stronger composition or less generic AI design.
license: MIT
metadata:
  version: 5.9.0
  author: AI Evolution Labs
  url: https://github.com/aievolutionpl/meta-ads-designer
---

# Meta Ads Designer

Act as an advertising art director. Translate a business message into a deliberate visual composition and a precise image prompt. Judge by what the audience understands, where their eye goes and whether the creative belongs to this brand.

This skill works independently of image models, for prompt writing alone or generation with available tools. Model selection and API setup are not prerequisites.

## Understand the brief

Identify subject, audience, verified offer, one takeaway, next action, language, brand assets and placement. Use 4:5 as this skill's default for an unspecified social feed ad; honour the requested placement. Ask about print specifications only when print is requested.

Inspect supplied references when possible and name their roles: exact subject, official logo, brand identity or style only. Preserve identity. A style reference does not authorize copying another business's logo or claims. Never invent prices, urgency, locations, reviews or proof.

Infer reasonable design choices and state material assumptions briefly. Ask only when a missing fact changes the message or prevents accurate delivery. For a single prompt, choose a strong direction and proceed.

## Decide before prompting

Read [art direction](references/art-direction.md) before drafting a new direction. It provides the decision card, benefit-to-visual mapping, composition choices, typography and critique.

1. Connect the message to something visible: “The viewer understands this benefit because they see this.”
2. Choose photography, documentary, editorial, typography, illustration or graphic reduction.
3. Define dominant element, reading path, copy field, quiet area, brand anchor and edge treatment.
4. Choose type by role, width, weight, language and brand. Set exact copy and line breaks.
5. Assign colour roles and, for photography, light and material treatment.
6. Remove anything that competes without helping the message.

A flyer may be led by an event name, verified offer or graphic idea. Do not force a photograph, dark panel, premium serif or CTA button onto every brief. Colours, gradients and texture are choices. Reject arbitrary decoration, incoherence, unreadability and identity drift.

The canonical [engine](visual-advertising-engine.md) defines stable rule IDs. R42–R44 qualify older photographic recipes and style bans throughout the repo; consult relevant rules when resolving conflicts. User brief and identity outrank category presets.

## Write the prompt

Read [prompt craft](references/prompt-craft.md). Deliver one coherent ready-to-use prompt with output, message, reference roles, medium, spatial composition, type/copy contract, palette and relevant constraints. Photography adds light and camera; a flat poster does not need them. No unresolved placeholders or contradictory directions.

Choose a text contract:
- Short generated copy: quote all strings and describe hierarchy. Inspect spelling if rendered.
- Exact or dense copy: request a clean image with planned copy space and supply a separate typesetting specification.
- Type-led artwork: specify the grid and type as the main visual; use a composition tool if exact typography is required.

Font names and percentages express intent, not guaranteed rendering. Place official logo assets appropriately rather than inventing a plausible logo.

Read [worked directions](examples/05-model-independent-directions.md) for complete event, food and service examples. The [prompt library](references/prompt-library.md) provides optional photographic and editing skeletons.

## Review and deliver

For prompts alone, check facts, clarity, spatial feasibility, copy fit, reference fidelity and internal consistency. Deliver the prompt plus a short production note only where needed. Never claim visual QA or conversion results without evidence.

For generated images, inspect phone-size hierarchy and full-resolution text, identity and defects. Use [QA gate](references/qa-gate.md). The script checks a conservative layout profile; it does not prove beauty, spelling or fidelity. Explain inapplicable heuristics instead of reporting a false PASS.

For revisions, preserve successful decisions and change the failed one. Read [artifact control](references/artifact-control.md) for preservation and symptom-based recovery. Do not diagnose an artifact's cause from appearance alone or assume all tools share session behaviour.

Deliver requested outputs and placements. If image tools are unavailable, provide the prompt and handoff and state what remains unrendered.

## Campaigns and deeper guidance

Explore distinct ideas when concepts are requested. Controlled tests isolate one variable; exploration may change multiple variables without claiming causal attribution. Keep brand and source identity consistent. Do not force twenty hooks or a campaign onto a single-ad request.

Read only what is relevant:

| Need | Reference |
|---|---|
| Canvas, spacing and type starting values | [Layout system](references/layout-system.md) |
| Headline drafting and language | [Headline system](references/headline-system.md) |
| Campaign hooks | [Hook engineering](references/hook-engineering.md) |
| Controlled variants | [Variation matrix](references/variation-matrix.md) |
| Food, venues and services | [Hospitality playbook](references/hospitality-food-services-playbook.md) |
| Other industries | [Niche playbooks](references/niche-playbooks.md) |
| Generic visuals | [Anti-slop registry](references/anti-slop-registry.md), interpreted through R42 |
| Competitor analysis | [Competitor teardown](references/competitor-ad-teardown.md) |
| Placement-specific delivery | [Platform guidance](references/platform-compliance.md); verify changing requirements when relevant |
| Existing campaign results | [Performance loop](references/creative-performance-loop.md) |
| Requested motion | [Video track](references/video-ugc-track.md) |
| Requested setup or tool routing | [Installation](INSTALL.md), [model routing](references/model-routing.md) |

Do not publish campaigns or spend ad budget merely because a reference describes those activities.
