# Patient-service patterns

- Identity context: prominently show whose care is being managed, relationship/authorization, masked identifiers, and a safe switch flow.
- Appointment: department/service, clinician, location or remote mode, date/time/timezone, preparation, cost, cancellation terms, and confirmation. Preserve selections after recoverable errors.
- Report: test name, result, unit, reference range where supplied, flag in words, specimen/time, source facility, update time, limitations, and next action. Never invent ranges or interpretation.
- Prescription/medication: supplied drug name, form, dose text, schedule, duration, prescriber, warnings, refill state, and contact path. Do not calculate or rewrite clinical instructions.
- Follow-up: purpose, due window, preparation, responsible service, status, and rescheduling.
- Payment: itemized amount, coverage/discount basis when supplied, pending/paid/refunded state, invoice, and support path.
- Urgent escalation: concise severity wording, immediate action, phone/emergency path, location relevance, and no competing promotion.

Use progressive disclosure for detail, but never hide safety-critical instructions, identity, abnormal flags, deadlines, or consent consequences behind hover/tooltips.
