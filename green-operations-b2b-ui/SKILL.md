---
name: green-operations-b2b-ui
description: Design and implement light green-led Web interfaces for energy, sustainability, carbon, agriculture, campus, resource-efficiency, and stable operations products. Use after web-ui-design-router selects it or when explicitly requested. Not for clinical patient care or incident-dominant industrial control.
---

# Green Operations B2B UI

Make resource flows, targets, trends, and operational health legible without equating everything green with success. Preserve the existing stack; use React, TypeScript, and Vite only for greenfield work.

## Entry invariant

Unless explicitly invoked, confirm selection by `web-ui-design-router`; otherwise load `../web-ui-design-router/SKILL.md` first.

## Work

1. Identify operator, resource model, reporting period, target baseline, data freshness, and actions users can take.
2. Read and follow [references/visual-research.md](references/visual-research.md). Browse current energy, sustainability, and operations references before substantial design work.
3. Read [references/tokens.md](references/tokens.md). Keep brand green separate from success and normal-state tokens; label all important states.
4. Read [references/patterns.md](references/patterns.md) for target progress, resource flows, trends, comparisons, facility hierarchy, and sustainability reporting.
5. Implement actionable drill-down and traceable calculations. Show units, denominators, time range, baseline, and data update time.
6. Apply [references/states-and-antipatterns.md](references/states-and-antipatterns.md), including missing meters, estimated values, stale data, target changes, and export failures.
7. Render at 1440, 1280, 768, and 390 CSS pixels where supported. Verify keyboard use, focus, contrast, chart alternatives, reduced motion, zoom/reflow, and overflow; revise critical failures.

## Handoff

Summarize the operating job, data meaning, token mapping, implemented states, viewport evidence, accessibility checks, and limitations.
