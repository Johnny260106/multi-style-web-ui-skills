---
name: tech-blue-b2b-ui
description: Design and implement light, technology-blue Web interfaces for enterprise SaaS, AI, cloud, developer, analytics, and data-management products. Use after web-ui-design-router selects it or when explicitly requested. Not for command-center wallboards, industrial equipment operations, or consumer healthcare.
---

# Technology Blue B2B UI

Make complex enterprise work feel precise, calm, and fast. Preserve the existing stack and component library; in a greenfield implementation default to React, TypeScript, and Vite.

## Entry invariant

Unless the user explicitly invoked this skill, confirm that `web-ui-design-router` selected it. If not, load `../web-ui-design-router/SKILL.md` first.

## Work

1. Identify the operator, primary decision, critical data, action frequency, permission model, and error cost. Inspect existing tokens and components before proposing replacements.
2. Read and follow [references/visual-research.md](references/visual-research.md). For a new product or substantial redesign, browse current references before choosing the visual direction; do not design from model defaults.
3. Read [references/tokens.md](references/tokens.md). Establish semantic CSS variables and map the existing library to them; do not scatter raw colors through components.
4. Read [references/patterns.md](references/patterns.md) for dense tables, filters, navigation, analytics, details, and forms. Design the shortest path through the primary job before adding dashboard summaries.
5. Implement real interactions and realistic domain copy. Preserve routing, data contracts, and existing conventions. Avoid decorative gradients, arbitrary floating cards, and oversized KPI grids.
6. Read [references/states-and-antipatterns.md](references/states-and-antipatterns.md). Cover loading, empty, error, disabled, success, forbidden, partial data, and overflow.
7. Render and inspect at 1440, 1280, 768, and 390 CSS pixels when the surface supports those widths. Check keyboard flow, visible focus, text and non-text contrast, zoom/reflow, reduced motion, and horizontal overflow. Revise high-impact failures before completion.

## Handoff

Report the page job, chosen visual direction, tokens or component mappings changed, implemented states, viewport evidence, accessibility checks, and remaining limitations. Do not claim WCAG conformance from automated checks alone.
