# Cockpit patterns

- Mission header: current scope, clock/timezone, overall system state, data freshness, shift/operator context, and global controls.
- Overview hierarchy: one primary operational question, a small set of consequential signals, event queue, spatial/temporal context, then supporting details.
- Alarm queue: severity, source, age, consequence, acknowledgement, owner, and next action. Sorting must not allow a new critical alarm to disappear silently.
- Live chart: visible time window, current marker, thresholds, gaps, update cadence, pause/resume, and accessible summary/table.
- Map/topology: synchronized event list, search, selected state, clustering, textual location, and a non-map fallback.
- Drill-down: preserve time range and selected entity; provide a clear route back to overview without losing context.
- Wallboard: supports passive distance viewing; interaction-heavy tasks move to a workstation detail view.

Use CSS grid and responsive breakpoints, not a scaled 1920px canvas. Design graceful degradation when a feed or panel is unavailable.
