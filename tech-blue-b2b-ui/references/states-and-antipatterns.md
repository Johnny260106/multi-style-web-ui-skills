# States and anti-patterns

Every data surface needs a distinct initial load, background refresh, empty-first-use, empty-filter-result, partial data, recoverable error, unavailable dependency, forbidden, and stale-data state. Actions need idle, hover, focus, pressed, pending, success, failure, disabled-with-reason, and duplicate-submission protection.

Keep user filters and edits across recoverable failures. Place recovery next to the failure and state what was preserved. Skeletons must approximate final geometry; do not use them for long uncertain waits without status text.

Avoid:

- dashboard-first navigation that hides the real workflow;
- four interchangeable KPI cards regardless of page purpose;
- every object inside a rounded card;
- icon-only critical actions without accessible names;
- placeholder charts, perfect round metrics, and fake “live” badges;
- hover-only controls, color-only status, inaccessible custom selects, and low-contrast gray text;
- destructive actions beside routine actions with equal emphasis;
- optimistic success for operations that have not been confirmed by the system.
