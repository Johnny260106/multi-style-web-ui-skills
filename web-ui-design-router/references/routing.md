# Routing model

Choose by product semantics, not by the user's favorite color. Brand colors can override tokens after the product type is selected.

| Candidate | Strong signals | Do not choose when |
|---|---|---|
| `tech-blue-b2b-ui` | AI, cloud, developer platform, enterprise SaaS, analytics, permissions, dense tables | the page is primarily physical operations, public medical care, or a wallboard |
| `industrial-orange-b2b-ui` | manufacturing, equipment, warehouse, engineering, logistics, work orders, fault handling | orange is merely a brand color for an unrelated SaaS product |
| `green-operations-b2b-ui` | energy, sustainability, agriculture, campus operations, carbon, efficiency, stable operations | green would blur brand and medical/success semantics |
| `dark-cockpit-ui` | real-time monitoring, situation awareness, command center, large screen, NOC/SOC wallboard | users perform long forms, dense CRUD, or routine office work |
| `patient-medical-web-ui` | appointments, consultations, reports, prescriptions, medication, payment, records, family proxy | the product is lifestyle coaching without a care journey |
| `health-management-web-ui` | chronic-condition tracking, activity, diet, habits, daily plans, reminders, longitudinal trends | the task communicates diagnoses, prescriptions, or urgent clinical risk |

## Tie-breakers

- Administration plus wallboard: route the administration shell to its B2B skill and the wallboard route to `dark-cockpit-ui`; never darken the whole product by default.
- Patient care plus wellness: patient care owns identity, reports, medication, appointments, and risk communication; wellness owns daily tracking and coaching surfaces.
- Industrial plus green operations: choose orange when incident response and equipment intervention dominate; choose green when efficiency, resources, and long-term operating targets dominate.
- Brand-only color request: retain the domain skill and adapt its brand tokens. Do not route solely on a requested hue.

Ask a question only when the top two candidates are materially tied after these rules.
