# States, safety, and anti-patterns

Cover identity unverified, wrong patient/proxy context, authorization pending/expired, result pending/amended/unavailable, prescription expired, appointment conflict, payment pending/refunded, network retry, masked data, and urgent escalation. Use explicit Chinese text and recovery actions.

Never infer diagnosis, urgency, dosage, reference ranges, treatment, or prognosis. Clearly mark placeholder/demo content. Consequential actions require target identity and effect review; duplicate submissions must be prevented.

Avoid:

- color-only abnormal results or vague “有风险” labels;
- unqualified AI diagnosis or certainty language;
- generic doctor stock photos used as trust proof;
- gamification, confetti, streak loss, or shame around care adherence;
- hiding medical source, timestamp, units, or amendments;
- ambiguous consent toggles and preselected optional data sharing;
- exposing sensitive data in notifications, URLs, analytics labels, or screenshots;
- claiming legal, clinical, privacy, or WCAG compliance without the appropriate review.
