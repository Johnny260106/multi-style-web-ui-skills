---
name: dark-cockpit-ui
description: Design and implement dark Web command-center, NOC/SOC, real-time monitoring, situation-awareness, and large-screen cockpit interfaces. Use after web-ui-design-router selects it or when explicitly requested. Not for routine CRUD administration, long forms, or making an entire B2B product dark by default.
---

# Dark Cockpit UI

Optimize for distance viewing, change detection, and rapid escalation. A cockpit is an operational instrument, not a decorative dashboard. Preserve the stack; use React, TypeScript, and Vite for greenfield work.

## Entry invariant

Unless explicitly invoked, confirm selection by `web-ui-design-router`; otherwise load `../web-ui-design-router/SKILL.md` first.

## Work

1. Establish viewing distance, target displays, refresh cadence, event severity, operator actions, and failure behavior.
2. Read and follow [references/visual-research.md](references/visual-research.md). Browse current monitoring, command-center, and data-visualization references before choosing the composition.
3. Read [references/tokens.md](references/tokens.md). Use layered navy surfaces, neutral readable text, limited cyan/blue emphasis, and reserved warning/danger colors.
4. Read [references/patterns.md](references/patterns.md) for overview hierarchy, real-time events, maps, timelines, chart density, and detail reveal.
5. Implement responsive composition for 16:9 displays and ordinary desktops. Do not scale a fixed canvas or rely on tiny text to fit more data.
6. Apply [references/states-and-antipatterns.md](references/states-and-antipatterns.md), including stale streams, reconnecting, partial feeds, acknowledged alarms, and degraded mode.
7. Render at 1920×1080, 1440×900, 1280×720, and 768 CSS pixels when applicable. Check distance legibility, keyboard use, focus, contrast, non-color alarms, reduced motion, burn-in-prone decoration, and overflow.

## Handoff

Report the monitoring job, display assumptions, hierarchy, refresh and failure states, rendered evidence, accessibility checks, and limitations.
