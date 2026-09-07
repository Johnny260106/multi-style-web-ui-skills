# Industrial patterns

- Asset hierarchy: organization → site → line/zone → equipment → component. Keep location and parent context visible.
- Equipment status: identity, connectivity, current mode, last data time, critical readings, active issue, owner, and next action.
- Exception queue: severity, consequence, age, asset, assignee, acknowledgement, SLA, and resolution state; support fast filtering and keyboard review.
- Work order: problem evidence, safety prerequisites, assignment, steps, parts, timestamps, attachments, completion proof, and audit trail.
- Maintenance timeline: distinguish planned, due, overdue, completed, and cancelled; display timezone and responsible role.
- Process view: use diagrams only when topology matters. Provide an accessible list/table equivalent and avoid decorative pipes.
- Maps/floor plans: pair markers with a synchronized list, clustering, search, selected state, and textual location.

Mobile Web should support field lookup, acknowledgement, evidence capture, and essential updates. Avoid shrinking the desktop control room into a phone.
