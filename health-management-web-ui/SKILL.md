---
name: health-management-web-ui
description: Design and implement Simplified-Chinese-first consumer Web interfaces for chronic-condition tracking, activity, diet, sleep, habits, health plans, reminders, and longitudinal wellness trends. Use after web-ui-design-router selects it or when explicitly requested. Not for diagnosis, prescriptions, urgent clinical risk, or clinician-facing systems.
---

# Health Management Web UI

Create a supportive, adult, and credible experience that helps people understand trends and take sustainable actions. Do not turn uncertain health data into medical certainty. Preserve the stack; use React, TypeScript, and Vite for greenfield work.

## Entry invariant

Unless explicitly invoked, confirm selection by `web-ui-design-router`; otherwise load `../web-ui-design-router/SKILL.md` first.

## Work

1. Identify user goal, measurement source, baseline, time horizon, adherence burden, accessibility needs, and boundary between coaching and medical care.
2. Read and follow [references/visual-research.md](references/visual-research.md). Browse current consumer-health and behavior-change references before substantial design work.
3. Read [references/tokens.md](references/tokens.md). Use calm teal/green/blue roles, accessible neutrals, restrained illustration, and separate brand from status semantics.
4. Read [references/patterns.md](references/patterns.md) for daily check-ins, trend explanation, plans, reminders, progress, chronic tracking, and escalation.
5. Show units, ranges, source, update time, missing-data meaning, and uncertainty. Prefer understandable trends and next steps over opaque health scores, streak pressure, or moralizing copy.
6. Apply [references/states-and-antipatterns.md](references/states-and-antipatterns.md), including device disconnect, skipped days, low confidence, abnormal observations, paused plans, and clinician-contact guidance.
7. Render at 1440, 1280, 768, and 390 CSS pixels. Verify keyboard use, focus, WCAG 2.2 AA contrast/reflow, 200% zoom, reduced motion, chart alternatives, and long Chinese copy; revise high-impact failures.

## Handoff

Report the user goal, evidence and uncertainty shown, implemented states, viewport evidence, accessibility checks, content requiring health-professional review, and limitations.
