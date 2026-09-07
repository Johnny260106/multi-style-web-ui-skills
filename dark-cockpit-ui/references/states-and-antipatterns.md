# States and anti-patterns

Streams need connecting, live, delayed, stale, reconnecting, partial, paused, failed, and recovered states. Show last successful update and which panels are affected. Alarms need new, seen, acknowledged, assigned, escalated, resolved, and reopened states.

Prevent silent failure: an animated “live” dot is insufficient. When degraded, retain last-good data with an explicit timestamp and visual treatment that cannot be confused with live data.

Avoid:

- neon borders around every panel and cyan text everywhere;
- tiny dense labels that only work in a design mockup;
- fake radar, particles, moving grid backgrounds, or endless pulses;
- equal-sized symmetric panels with no mission hierarchy;
- relying on red/green or glow alone for alarm meaning;
- maps without a synchronized list or accessible fallback;
- auto-rotating views that users cannot pause;
- dark cockpit styling for forms, settings, and routine CRUD administration.
