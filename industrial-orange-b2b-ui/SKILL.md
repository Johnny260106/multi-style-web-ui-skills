---
name: industrial-orange-b2b-ui
description: Design and implement light Web operations interfaces for manufacturing, equipment, engineering, warehousing, logistics, work orders, and fault handling, with a restrained industrial-orange identity. Use after web-ui-design-router selects it or when explicitly requested. Not for generic orange-branded SaaS or dark command-center screens.
---

# Industrial Orange B2B UI

Optimize for situational clarity, intervention speed, and traceability around physical operations. Preserve the existing stack; for a greenfield implementation default to React, TypeScript, and Vite.

## Entry invariant

Unless explicitly invoked, confirm that `web-ui-design-router` selected this skill; otherwise load `../web-ui-design-router/SKILL.md` first.

## Work

1. Establish operator role, asset hierarchy, operational state model, fault severity, required intervention, and audit trail.
2. Read and follow [references/visual-research.md](references/visual-research.md). Browse current industrial and operations references before substantial design work.
3. Read [references/tokens.md](references/tokens.md). Separate brand orange, caution, warning, danger, and offline states with distinct semantic tokens and labels.
4. Read [references/patterns.md](references/patterns.md) for asset status, work orders, process steps, maintenance timelines, maps, and exception queues.
5. Implement the primary intervention path before overview decoration. Use realistic identifiers, timestamps, units, ownership, and status history.
6. Apply [references/states-and-antipatterns.md](references/states-and-antipatterns.md), including stale telemetry, disconnected devices, delayed data, partial permissions, and destructive confirmation.
7. Render at 1440, 1280, 768, and 390 CSS pixels where supported. Verify keyboard order, focus, contrast, non-color status cues, reduced motion, dense-table overflow, and long Chinese labels; revise critical failures.

## Handoff

State the operational job, selected hierarchy, semantic color separation, implemented system states, viewport evidence, accessibility checks, and limitations.
