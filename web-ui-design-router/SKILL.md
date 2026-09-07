---
name: web-ui-design-router
description: Route any Web UI design, redesign, dashboard, frontend page, or visual implementation request to exactly one installed vertical UI skill before code is written. Use first for B2B systems, command-center cockpits, patient medical services, and consumer health-management products. Do not use for backend-only or non-visual work.
---

# Web UI Design Router

Select the governing visual system before implementation. Do not design or write UI code in this skill.

## Route

1. Inspect the brief and existing project for audience, primary job, domain language, information density, environment, brand constraints, and component library.
2. Read [references/routing.md](references/routing.md), score the candidates, and select one primary leaf skill.
3. If one candidate clearly dominates, state the selection and a one-sentence reason. If two remain plausible and the choice changes the product character, present only those two with a concise trade-off and ask the user to choose.
4. Load the selected sibling skill's `SKILL.md` and follow it through design, implementation, rendered verification, and revision. Resolve it relative to this folder as `../<skill-name>/SKILL.md`.
5. Never merge complete visual systems. A secondary skill may inform a bounded surface only when the product genuinely contains two contexts, such as a light administration console with a dark monitoring view. Name the primary system and the bounded override.

## Required selection output

Before loading the leaf skill, record:

- primary user and page job;
- selected skill;
- decisive routing signals;
- existing stack and constraints to preserve;
- any explicit brand input that overrides the preset.

If the user explicitly invokes a leaf skill, acknowledge that choice and load it without reopening style selection. For routing regression checks, read [references/trigger-tests.md](references/trigger-tests.md).
