---
name: patient-medical-web-ui
description: Design and implement Simplified-Chinese-first consumer Web interfaces for appointments, consultations, medical reports, prescriptions, medication, follow-up, payment, records, and family-proxy care. Use after web-ui-design-router selects it or when explicitly requested. Not for clinician-facing EHRs or lifestyle-only wellness products.
---

# Patient Medical Web UI

Design for trust, comprehension, privacy, and safe next steps. This skill does not validate medical correctness or replace clinical, legal, security, or regulatory review. Preserve the stack; use React, TypeScript, and Vite for greenfield work.

## Entry invariant

Unless explicitly invoked, confirm selection by `web-ui-design-router`; otherwise load `../web-ui-design-router/SKILL.md` first.

## Work

1. Identify patient or proxy user, care stage, urgency, emotional context, health-literacy burden, sensitive fields, and the next safe action. Do not invent diagnoses, ranges, dosages, or treatment advice.
2. Read and follow [references/visual-research.md](references/visual-research.md). Browse current patient-service references and evidence-based healthcare design systems before substantial design work.
3. Read [references/tokens.md](references/tokens.md). Use a calm clinical palette and reserve semantic risk colors. Never encode medical meaning by color alone.
4. Read [references/patterns.md](references/patterns.md) for identity context, appointments, reports, prescriptions, payment, follow-up, and family proxy.
5. Use concise Simplified Chinese, familiar verbs, explicit dates and time zones, visible source/update time, and progressive disclosure. Preserve supplied clinical wording; flag uncertain or placeholder content.
6. Apply [references/states-and-antipatterns.md](references/states-and-antipatterns.md), including identity mismatch, expired authorization, unavailable results, urgent escalation, network failure, and masked sensitive data.
7. Render at 1440, 1280, 768, and 390 CSS pixels. Verify keyboard use, focus, WCAG 2.2 AA contrast/reflow, 200% zoom, non-color meaning, reduced motion, readable Chinese type, and error recovery. Automated checks do not prove conformance.

## Handoff

Report the patient job, safety-sensitive assumptions, privacy states, implemented flows, viewport evidence, accessibility checks, content requiring clinical review, and limitations.
