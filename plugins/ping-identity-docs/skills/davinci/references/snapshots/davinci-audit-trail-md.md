---
title: Audit Trail
description: DaVinci administrative audit events are now part of the PingOne centralized audit framework. You can view and filter DaVinci events alongside standard PingOne events in the PingOne admin console.
component: davinci
page_id: davinci::davinci_audit_trail
canonical_url: http://docs.pingidentity.com/davinci/davinci_audit_trail.html
llms_txt: http://docs.pingidentity.com/davinci/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 26, 2026
section_ids:
  legacy-audit-trail: Legacy audit trail
---

# Audit Trail

DaVinci administrative audit events are now part of the PingOne centralized audit framework. You can view and filter DaVinci events alongside standard PingOne events in the PingOne admin console.

Learn more in the PingOne [Audit](http://docs.pingidentity.com/pingone/monitoring/p1_reporting.html) documentation.

|   |                                                                                                                                                                                                                                                                                                                                                |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | During the transition period, DaVinci audit events are written to both the legacy DaVinci **Audit Trail** and [PingOne Audit](http://docs.pingidentity.com/pingone/monitoring/reporting.html) simultaneously for approximately 3–4 months. After the transition period ends, the legacy DaVinci **Audit Trail** tab will stop being populated. |

## Legacy audit trail

The **Audit Trail** tab in the DaVinci user interface provides a list of administrative events for the current user.

When you click the **Audit Trail** tab, the 10 most recent administrative events appear. Administrative events include:

* Login events for the DaVinci user interface

* Multi-factor authentication (MFA) events for the DaVinci user interface

* The creation or deletion of a flow, connector, application, or other entity

* The addition of custom JavaScript to a flow during flow creation, import, cloning or modification

* The addition of custom JavaScript to a connector that can run external scripts

Each event displays relevant information including:

* The event message, which indicates the type of event and its success or failure

* The date and time of the event

* The name and ID of the team member who initiated the event

To view additional event details, expand the event. You can click the **Next Page** and **Previous Page** icons to view earlier or later events.
