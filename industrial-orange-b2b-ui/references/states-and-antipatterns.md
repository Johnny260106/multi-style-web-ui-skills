# States and anti-patterns

Model connected, reconnecting, offline, stale, delayed, estimated, maintenance, bypassed, alarm, acknowledged, resolved, and unknown separately. Show last-good timestamp and the operational consequence of missing data.

For commands, distinguish requested, queued, sent, confirmed, rejected, timed out, and cancelled. Never display success before device/system confirmation. Consequential remote actions need scope, target, effect, and explicit confirmation.

Avoid:

- using orange for brand, warning, alarm, selection, and charts simultaneously;
- unlabeled gauges or thresholds with no units;
- red/green-only status matrices;
- fake real-time movement or endlessly blinking alarms;
- burying stale-data warnings in tooltips;
- bulk commands without target review and result-by-result feedback;
- dense panels with equal visual weight;
- resetting filters or work-order drafts after recoverable errors.
