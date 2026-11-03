---
title: Alerts
description: Configure alerts to send messages about the status of particular resources in PingOne.
component: pingone
page_id: pingone:monitoring:p1_alerts
canonical_url: https://docs.pingidentity.com/pingone/monitoring/p1_alerts.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-05-20T00:00:00Z
keywords: ["alerts", "alert types"]
section_ids:
  alert-types: Alert types
---

# Alerts

PingOne can deliver alert messages based on the status of certain resources.

Because alerts are configured per environment, you can have different alerts for different environments, such as staging and production. PingOne filters duplicate alerts so that administrators don't receive multiple redundant alerts.

PingOne supports a number of alert types, including certificate and key expiration alerts, user license limit alerts, rate limit alerts, and so on.

## Alert types

The following table lists the different types of alerts:

| Option                                 | Description                                                                                                                                                                                                                                                                                                                                                |
| -------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Suspicious Traffic**                 | Provides an alert when the PingOne Protect service detects a significant increase in traffic that is suspected to be malicious.&#xA;&#xA;This alert requires a PingOne Protect license.                                                                                                                                                                    |
| **Data Quality Issue**                 | Provides an alert when PingOne Protect detects a data quality issue that could affect the accuracy of risk evaluations. This alert is triggered when there is a significant increase in the number of events that are missing key data elements or have other data quality issues.&#xA;&#xA;This alert requires a PingOne Protect license.                 |
| **Rate Limit Warning**                 | Provides an alert when peaks in HTTP traffic are detected that exceed 75% of the throughput allocation. The alert message gives specifics about the type and source of the traffic.                                                                                                                                                                        |
| **Rate Limit Exceeded**                | Provides an alert when peaks in HTTP traffic are detected that exceed 100% of the throughput allocation. The alert message gives specifics about the type and source of the traffic.                                                                                                                                                                       |
| **Certificate Expiring**               | Provides an alert when the expiration date for a certificate is 60 days away.                                                                                                                                                                                                                                                                              |
| **Certificate Expired**                | Provides an alert when a certificate expires.                                                                                                                                                                                                                                                                                                              |
| **KeyPair Expiring**                   | Provides an alert when the key pair expiration date is 60 days away.                                                                                                                                                                                                                                                                                       |
| **KeyPair Expired**                    | Provides an alert when a key pair expires.                                                                                                                                                                                                                                                                                                                 |
| **Approaching User License Limit**     | Provides an alert when the number of user identities stored in your directory exceeds 90% of the maximum allowed by your PingOne license agreement.                                                                                                                                                                                                        |
| **User License Limit Reached**         | Provides an alert when the number of user identities stored in your PingOne directory reaches the maximum number of user identities included in your PingOne license agreement. This reflects the total number of identities in the directory, not the number of active users identities. A limited number of user identities can still be added.          |
| **User License Limit Exceeded**        | Provides an alert when the number of user identities stored in your PingOne directory exceeds the maximum allowed by your license agreement. This reflects the total number of identities in the directory, not the number of active users. New user identities can no longer be created until existing identities are removed or your license is updated. |
| **License Rotated**                    | Provides an alert when a PingOne license has expired and a new license has replaced it.                                                                                                                                                                                                                                                                    |
| **License Expiring**                   | Provides an alert 2 weeks before the expiration of a PingOne license.                                                                                                                                                                                                                                                                                      |
| **License Expired**                    | Provides an alert when a PingOne license has expired.                                                                                                                                                                                                                                                                                                      |
| **Gateway Version Deprecating**        | Provides monthly alerts until 28 days remain after a `supportEndsOn` date is set for the gateway version. This is followed by weekly alerts for the next 3 weeks, and daily alerts during the final 7 days before its deprecation.                                                                                                                         |
| **Gateway Version Deprecated**         | Provides an alert when a gateway instance is running on a deprecated version.                                                                                                                                                                                                                                                                              |
| **Gateway Info Alerts**                | Provides an alert every 7 days when information that needs attention is detected, such as `Single Instance Connected`.                                                                                                                                                                                                                                     |
| **Gateway Warning Alerts**             | Provides an alert every 4 days when a warning condition is detected, such as `No TLS Verification`.                                                                                                                                                                                                                                                        |
| **Gateway Errors Alerts**              | Provides an alert every 4 hours when an error condition is detected, such as `No Instances Connected` or `Bad Credentials`.                                                                                                                                                                                                                                |
| **Gateway Long-Running Request Info**  | Provides an alert when multiple requests to the gateway client experience high latency in the past few minutes, signaling potential server slowdowns. Learn more in [troubleshooting steps](../integrations/p1_troubleshooting_an_ldap_gateway_instance.html#repeated-admin-alerts-for-long-running-ldap-requests).                                        |
| **Gateway Long-Running Request Error** | Provides an alert when a request takes longer than expected and likely contributes to user authentication errors. Learn more in [troubleshooting steps](../integrations/p1_troubleshooting_an_ldap_gateway_instance.html#repeated-admin-alerts-for-long-running-ldap-requests).                                                                            |

Learn more about alerts in the following topics:

* [Viewing alerts](p1_view_alerts.html)

* [Creating an alert](p1_add_alert.html)

* [Editing an alert](p1_edit_alert.html)

* [Deleting an alert](p1_delete_alert.html)

Learn more about all logging and reporting capabilities in PingOne in [PingOne Platform logging and reporting](../getting_started_with_pingone/p1_logging_reporting_overview.html).

---

---
title: Audit
description: Use the Audit page to review information about user events and actions performed in the PingOne admin console.
component: pingone
page_id: pingone:monitoring:p1_reporting
canonical_url: https://docs.pingidentity.com/pingone/monitoring/p1_reporting.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2024-04-17T00:00:00Z
section_ids:
  learn-more: Learn more
---

# Audit

Use the **Audit** page to run reports about events and actions performed in PingOne.

PingOne logs three types of data that are governed by different retention policies:

| Data Type                    | Description                                                                                                                                                                                                                                             |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| User events                  | User events include user creation or deletion, authentications, updates to the user record, and other transactions related to end-user activity. User events are retained for 90 days.                                                                  |
| PingOne admin console events | PingOne admin console events include configuration changes made to system settings, policies, applications, and integrations. Configuration events are retained for 2 years.                                                                            |
| DaVinci admin events         | DaVinci administrative events include events such as flow creation, connector updates, and variable changes. DaVinci administrative events are retained for 90 days. Learn more in [DaVinci administrative audit events](p1_davinci_audit_events.html). |

You can run audit reports from **Monitoring > Audit** or using the PingOne APIs to view data about user and console events. You can run queries against a maximum of 14 days at a time.

|   |                                                                                                                                                                                                                                       |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | To retain PingOne data for longer than the standard retention periods, set up webhooks to stream the data to your own repository and configure your own retention policy. Learn more in [Webhooks](../integrations/p1_webhooks.html). |

## Learn more

Learn more about PingOne logging and reporting capabilities in [PingOne Platform logging and reporting](../getting_started_with_pingone/p1_logging_reporting_overview.html).

Learn more about running audit reports in PingOne in the following topics:

* [Audit parameters](p1_auditparameters.html)

* [Running an audit report](p1_running_audit_report.html)

* [DaVinci administrative audit events](p1_davinci_audit_events.html)

* [Audit Activities](https://developer.pingidentity.com/pingone-api/platform/audit-activities.html) in the PingOne API documentation

---

---
title: Audit parameters
description: Use a combination of audit parameters to generate an auditing report in PingOne.
component: pingone
page_id: pingone:monitoring:p1_auditparameters
canonical_url: https://docs.pingidentity.com/pingone/monitoring/p1_auditparameters.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2024-05-03T00:00:00Z
page_aliases: ["p1_event_types.adoc"]
section_ids:
  time-range: Time Range
  selected-fields: Selected Fields
  time-zone: Time Zone
  filter-type: Filter Type
  secondary-filter-type: Secondary Filter Type
  available-dates-utc: Available Dates (UTC)
---

# Audit parameters

Use audit parameters to specify the details of your search results.

![A screen capture of the Audit Parameters section without any selections made.](_images/p1-monitoring-audit-params.png)

## Time Range

Limit the report results to a specific time period.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Data up to 14 days old relative to the current date is available immediately. Data older than 14 days must be requested from the **Audit** page or using the API. You can't request data for dates that are more than 2 years (730 days) before the current date.Depending on the number of days requested and the average number of events logged per day, the retrieval process can take from 2 to 24 hours. You can request a maximum of 14 days of data from within the data retention period, and you can't request additional data while another request is pending.If you have a valid email address in PingOne, you'll be notified when the requested data is available. At that point, you can return to the **Audit Parameters** page and run queries against the data for the timeframe requested. The retrieved data is available for 14 days from the date of the retrieval request. |

| Option            | Description                                                                                                                                                                                              |
| ----------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Relative**      | A time range relative to the current time. In the **Within** fields, select a number and a time period. For example, **2** and **weeks**.                                                                |
| **Specific Date** | A time range with a specified start and end date, such as "March 27 to April 10." Optionally, you can also include the time of day using the **Hour** and **Minute** fields for the start and end dates. |

|   |                                                                                                                                                       |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | If you enter a time range more than 2 years (730 days) from the current date, you're prompted to adjust the time range before submitting the request. |

## Selected Fields

Specify which fields appear in the results list.

| Option            | Description                                                                                                                                                                                                                                             |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Timestamp**     | Shows the date and time of the event. The format is: `MM/DD/YYYY hh:mm:ss`.                                                                                                                                                                             |
| **Event Type**    | Shows the type of event returned. You can find a complete list of events logged in PingOne in [Audit Reporting Events](https://developer.pingidentity.com/pingone-api/platform/reference/audit-reporting-events.html) in the PingOne API documentation. |
| **Description**   | Shows a brief description of the event.                                                                                                                                                                                                                 |
| **Client**        | Shows the name of the application or OAuth client that performed the event.                                                                                                                                                                             |
| **User Identity** | Shows the user who performed the action.                                                                                                                                                                                                                |
| **Population**    | Shows the population of the resource on which the event was performed.                                                                                                                                                                                  |
| **Resource Type** | Shows the type of resource affected by the event, such as an application, identity provider, or digital wallet.                                                                                                                                         |

## Time Zone

Specify the time zone to use for the display of the **Timestamp** in the results list.

## Filter Type

Limit the search results based on the specified filters.

| Option                  | Description                                                                                                                                                                                                                                                                                                                                          |
| ----------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Resource ID**         | Find activities that were performed on a specific resource, identified by its resource ID (UUID).For PingOne DaVinci events, enter a flow ID, variable ID, connector instance ID, flow policy ID, application ID, or UI template ID to scope results to a specific DaVinci resource.                                                                 |
| **Correlation ID**      | Find activities by correlation ID. When an HTTP request is received, it's assigned a correlation ID. You can use the correlation ID to associate HTTP responses with messages in the event log.                                                                                                                                                      |
| **Event Type**          | Find activities by event type. You can find a complete list of events logged in PingOne in [Audit Reporting Events](https://developer.pingidentity.com/pingone-api/platform/reference/audit-reporting-events.html) in the PingOne API documentation.                                                                                                 |
| **User ID (Actor)**     | Find activities performed by a specific user, identified by user ID. User IDs are immutable, so this filter provides a stable way to identify the user over time. If they change their username, you can still find the activities performed by that user.                                                                                           |
| **User Name (Actor)**   | Find activities performed by a specific user, identified by username. Because usernames can change, results might not refer to the same person over time. Use **User ID (Actor)** if you need a stable identifier.                                                                                                                                   |
| **Client (Actor)**      | Find activities performed by a specific OAuth client acting as the caller, such as the PingOne admin console (`adminui`), or a worker application using client credentials. You can enter an application ID or application name. This filter differs from the **Application** filter, which matches activities performed on an application.          |
| **Resource Population** | Find activities performed on resources in one or more populations, matched by the population ID associated with the target resource. Use this filter to return everything that happened to users in a given population. This filter differs from the **Population** filter, which only matches activities performed on a specific population object. |
| **Resource Type**       | Find activities performed on a specific type of resource, such as an application, identity provider, or digital wallet. This filter returns all activities whose target resource is the selected type, regardless of which specific resource was affected.                                                                                           |
| **Population**          | Find activities performed on a specific population object itself, such as when the population was created, updated, or deleted. This filter doesn't include activities performed on users in that population. Use **Resource Population** for that use case.                                                                                         |
| **User**                | Find activities performed on a specific user, identified by user ID (not by the username), such as updates to that user's profile, password, or credentials. This filter differs from **User ID (Actor)**, which matches activities performed by that user.                                                                                          |
| **Application**         | Find activities performed on a specific application resource, such as when the application was created, updated, or deleted. Enter an application ID or name. This filter differs from **Client (Actor)**, which matches activities performed by an application acting as the caller.                                                                |

## Secondary Filter Type

Specify a secondary filter to further refine your results.

You must specify a primary filter type before you can select a secondary filter type. The **Secondary Filter Type** list contains all of the filter types that you didn't select as your primary filter.

## Available Dates (UTC)

The **Available Dates (UTC)** section of the page lists the dates for the data that's available to query or that has been requested.

![A screen capture of the Audit Parameters section with a message indicating that data retrieval is in progress.](_images/p1-audit-data-retrieval-in-progress.png)

---

---
title: Authentication Dashboard
description: The Authentication Dashboard shows a summary of SSO and authentication activity through PingOne authentication.
component: pingone
page_id: pingone:monitoring:p1_authentication_dashboard
canonical_url: https://docs.pingidentity.com/pingone/monitoring/p1_authentication_dashboard.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-09-14T16:07:15Z
page_aliases: ["early-access-features:ea-p1_auth_dashboard.adoc", "p1_auth_dashboard.adoc"]
section_ids:
  limitations: Limitations
  accessing-the-dashboard: Accessing the dashboard
  filters: Filters
  charts: Charts
  total-successful-authentications: Total Successful Authentications
  successful-authentications: Successful Authentications
  total-identities: Total Identities
  total-unsuccessful-authentication-attempts: Total Unsuccessful Authentication Attempts
  unsuccessful-authentication-attempts: Unsuccessful Authentication Attempts
  total-password-resets: Total Password Resets
  password-resets: Password Resets
  successful-authentications-by-dayhour: Successful Authentications by Day/Hour
---

# Authentication Dashboard

The **Authentication Dashboard** shows a summary of authentication activity through PingOne authentication for the selected environment, including:

* Single sign-on (SSO) activity.

* User self-registration events.

* PingOne DaVinci success flows from successful authentication attempts.

* DaVinci failed flows from unsuccessful authentication attempts.

* Authentication through external identity providers (IdPs) configured in PingOne.

## Limitations

The Authentication Dashboard doesn't display the following activity:

* DaVinci authentication attempts that result in a timeout or user abandonment

* DaVinci authentications through social login connectors that bypass the DaVinci flow orchestration service, such as passwordless-only flows or sign-on with social accounts like Google

* DaVinci authentications that succeed after the user falls back to a previous authentication method following an initial failure

* Guest checkouts when a user is unable to sign on to their existing account and proceeds as a guest instead

## Accessing the dashboard

To access the **Authentication Dashboard**, in the PingOne admin console, go to **Monitoring > Authentication**.

![A screenshot of the Authentication Dashboard](_images/p1-authentication-dashboard.png)

## Filters

Use filters to refine the data displayed on the dashboard. You can limit data to a specific time range:

* **Today**: Displays data for the current day only.

* **From Yesterday**: Displays data for the previous day only.

* **Last 7 Days** (default): Displays data for the previous 7 days only.

* **Last 30 Days**: Displays data for the previous 30 days only.

* **Last 90 Days**: Displays data for the previous 90 days only.

* **This Month**: Displays data for the current calendar month only.

* **Last Month**: Displays data for the previous calendar month only.

* **Custom Range**: Enables you to define a date range within the last 6 months. Select a start date and an end date in the date picker, then click **Apply**.

This filter applies to all charts on the dashboard.

|   |                                                                        |
| - | ---------------------------------------------------------------------- |
|   | The Authentication Dashboard displays data only for the past 6 months. |

## Charts

Use the following controls to adjust the charts:

| Icon                                                                | Name         | Description                                                                                                                                                                                       |
| ------------------------------------------------------------------- | ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ![The Maximize icon.](../_images/p1-dashboard-maximize.png)         | Maximize     | Expands the chart to fill the dashboard.To minimize the chart, click the icon again.                                                                                                              |
| ![The Menu options icon.](../_images/p1-dashboard-menu-options.png) | Menu options | Options can vary for different types of charts:- **View summary data**: Displays chart data as a table.

- **Export**: Exports chart data to CSV or Excel format, depending on the type of chart. |
| ![The Sort visual icon.](../_images/p1-dashboard-sort-visual.png)   | Sort visual  | Sorts the chart data in ascending or descending order.                                                                                                                                            |

### Total Successful Authentications

Displays the total number of successful authentication attempts during the selected time period.

### Successful Authentications

Displays a bar chart showing the total number of successful authentication attempts by date and a rolling average line for the selected time period. Hover over a bar to view the number of authentications for that date.

### Total Identities

Displays the total number of users in the PingOne directory for the selected time period and a graph showing the total user count by date.

### Total Unsuccessful Authentication Attempts

Displays the total number of unsuccessful authentication attempts, including account lockouts and timeouts, during the specified time period.

### Unsuccessful Authentication Attempts

Displays a bar chart of unsuccessful authentication attempts, including account lockouts and timeouts, by date, and a rolling average line for the selected time period. Hover over a bar to view the number of unsuccessful attempts for that date.

### Total Password Resets

Displays the total number of times users successfully reset their password during the selected time period.

### Password Resets

Displays a bar chart of times users successfully reset their password by date and a rolling average line for the selected time period. Hover over a bar to view the number of successful password resets for that date.

### Successful Authentications by Day/Hour

Displays a heat map of average authentication activity by hour of the day and day of the week in the end user's local time zone. The color variations show usage trends throughout an average week.

Hover over the map to see the actual average of successful authentications to more accurately quantify the variation between periods. You can use this information to better understand user habits and identify periods of interest, such as typical highs and lows for authentication attempts.

---

---
title: Creating an alert
description: Create alerts in PingOne to receive notifications about the status of particular resources in your environment.
component: pingone
page_id: pingone:monitoring:p1_add_alert
canonical_url: https://docs.pingidentity.com/pingone/monitoring/p1_add_alert.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-05-26T00:00:00Z
keywords: ["create an alert", "add an alert"]
section_ids:
  steps: Steps
---

# Creating an alert

To enable alerts, you must configure an alert for the current environment. An alert includes information about which events trigger an alert and which email addresses will receive the alert.

## Steps

1. In the PingOne admin console, go to **Monitoring > Alerts** and click the **Plus** icon ([icon: plus, set=fa]).

   | Option              | Description                                                                                                                                                                                                                                                                                                                              |
   | ------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | **Name**            | Create a name for the alert.                                                                                                                                                                                                                                                                                                             |
   | **Email Addresses** | The addresses to which the alert will be sent. You can specify individual email addresses or mailing lists.&#xA;&#xA;If you have entered multiple email addresses, you can copy them to the clipboard after saving a new alert or when viewing an existing alert so that you can use them for additional alerts that you want to create. |
   | **Alert Types**     | Select the event types that will trigger the alert.&#xA;&#xA;One of the triggers for the Data Quality Issue alert is missing data from the PingOne Signals (Protect) SDK. If you activate this alert but choose not to implement the Signals SDK in your applications, you'll get email notifications about the missing data.            |

   ![A screen capture of adding or creating an alert.](_images/p1_create_an_alert.png)

2. Click **Save**.

---

---
title: Dashboards
description: Use dashboards to monitor and analyze activity in your PingOne platform and services.
component: pingone
page_id: pingone:monitoring:p1_dashboards
canonical_url: https://docs.pingidentity.com/pingone/monitoring/p1_dashboards.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-09-22T15:17:11Z
section_ids:
  pingone: PingOne
  pingone-services: PingOne Services
---

# Dashboards

**Dashboards** contains the different dashboards for PingOne and your configured PingOne services.

## PingOne

* [Authentication Dashboard](p1_authentication_dashboard.html): View a summary of sign-on activity for the selected environment.

* [User Demographics Dashboard](p1_user_demographic_dashboard.html): View a summary of user demographic profiles and activity for the selected environment.

* [API Usage Dashboard](../settings/p1_api_usage_dashboard.html): View your peak API usage trends and determine if you're approaching the base entitlements for any of your PingOne rate groups.

## PingOne Services

|   |                                                       |
| - | ----------------------------------------------------- |
|   | You'll only see dashboards for the services you have. |

* [Authorization Dashboard](../authorization_using_pingone_authorize/p1_az_dashboard.html): View a summary of metrics generated by requests to PingOne Authorize decision endpoints.

* [DaVinci Dashboard](https://docs.pingidentity.com/davinci/davinci_dashboard.html): View a summary of DaVinci flow and connector usage.

* [MFA Dashboard](p1_mfa_dashboard.html): View a summary of current user activity for the selected environment.

* [Threat Protection Dashboard](../threat_protection_using_pingone_protect/p1_protect_dashboard.html): View a summary of real-time PingOne Protect risk data.

* [Identity Verification Dashboard](../identity_verification_using_pingone_verify/p1_verify_monitoring.html#p1_verify_dashboard): View a summary of PingOne Verify transaction activity.

* [Provisioning Dashboard](../integrations/p1_provisioning_dashboard.html): View a summary of provisioning activity.

---

---
title: DaVinci administrative audit events
description: DaVinci administrative audit events are available in the PingOne audit report with unified filtering, retention, and webhook streaming.
component: pingone
page_id: pingone:monitoring:p1_davinci_audit_events
canonical_url: https://docs.pingidentity.com/pingone/monitoring/p1_davinci_audit_events.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-07-28T00:00:00Z
page_aliases: ["ea_p1_davinci_audit_events.adoc"]
section_ids:
  accessing-davinci-audit-events: Accessing DaVinci audit events
  retention-and-retrieval: Retention and retrieval
  p1-filtering-davinci-events: Filtering DaVinci events
  filter-by-resource-type: Filter by resource type
  filter-by-event-type: Filter by event type
  filter-by-resource-id: Filter by resource ID
  davinci-audit-event-reference: DaVinci audit event reference
  audit-event-structure: Audit event structure
  standard-fields: Standard fields
  davinci-specific-_embedded-fields: DaVinci-specific _embedded fields
  api-access: API access
---

# DaVinci administrative audit events

PingOne DaVinci administrative audit events are integrated into the PingOne centralized audit schema. DaVinci events appear alongside standard PingOne events in **Monitoring > Audit** and are subject to the same retention, retrieval, filtering, and webhook streaming capabilities. Learn more in [Audit](p1_reporting.html).

## Accessing DaVinci audit events

DaVinci audit events are visible in **Monitoring > Audit**. They appear alongside standard PingOne events and can be filtered to show only DaVinci-related activity.

Learn more about running audit reports in [Audit](p1_reporting.html).

### Retention and retrieval

Use the following retention windows to determine whether your audit data is available immediately or requires a retrieval request:

| Data age           | Availability                                                                               |
| ------------------ | ------------------------------------------------------------------------------------------ |
| Up to 14 days      | Available immediately in the PingOne admin console and through the API                     |
| Older than 14 days | Request retrieval from the **Audit** page. A prompt is displayed before results are shown. |

## Filtering DaVinci events

Use the available filters to narrow audit results by DaVinci resource type, event type, or a specific resource ID.

### Filter by resource type

In the **Filter Type** panel, select **Resource Type**. A **DaVinci** subsection is available with the following filters:

| Filter value              | Covers                              |
| ------------------------- | ----------------------------------- |
| **DaVinci Flows**         | Flow events and flow version events |
| **DaVinci Connectors**    | Connector instance events           |
| **DaVinci Variables**     | Variable events                     |
| **DaVinci Applications**  | Application events                  |
| **DaVinci Flow Policies** | Flow policy events                  |
| **DaVinci UI Templates**  | UI template events                  |

### Filter by event type

Select **Event Type** in the filter panel. All granular DaVinci event types are listed and multiple event types can be selected simultaneously.

### Filter by resource ID

Enter a flow ID, variable ID, connector instance ID, flow policy ID, application ID, or UI template ID in the **Resource ID** filter to scope results to a specific DaVinci resource.

## DaVinci audit event reference

The following 37 DaVinci administrative events are logged in PingOne.

|   |                                                                                                                                                                                                                                                                                                                                                                                             |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Rows 12 – 17 share the `DAVINCI.FLOW.CUSTOM_JAVASCRIPT.ADDED` action type for both flow-level and connector-level events. Differentiate by the `resources[].type` field: `DAVINCI_FLOW` for flow events (rows 12 – 15) and `DAVINCI_CONNECTOR` for connector events (rows 16 – 17). The context (direct creation, clone, or import) is reflected in `_embedded.davinciFlow.creationSource`. |

| #  | Action type (`action.type`)                      | Event type (`action.description`)              | Example description (`result.description`)                                                                |
| -- | ------------------------------------------------ | ---------------------------------------------- | --------------------------------------------------------------------------------------------------------- |
| 1  | `DAVINCI.FLOW.CREATED`                           | DaVinci Flow Created                           | Created DaVinci Flow '{name}'                                                                             |
| 2  | `DAVINCI.FLOW.UPDATED`                           | DaVinci Flow Updated                           | Updated DaVinci Flow '{name}'                                                                             |
| 3  | `DAVINCI.FLOW.DELETED`                           | DaVinci Flow Deleted                           | Deleted DaVinci Flow '{name}'                                                                             |
| 4  | `DAVINCI.FLOW.DEPLOYED`                          | DaVinci Flow Deployed                          | Deployed DaVinci Flow '{name}'                                                                            |
| 5  | `DAVINCI.FLOW.CLONED`                            | DaVinci Flow Cloned                            | Cloned DaVinci Flow 'CLONE-{name}' from '\\{source name}'                                                 |
| 6  | `DAVINCI.FLOW.IMPORTED`                          | DaVinci Flow Imported                          | Imported DaVinci Flow '{name}'                                                                            |
| 7  | `DAVINCI.FLOW.ENABLED`                           | DaVinci Flow Enabled                           | Enabled DaVinci Flow '{name}'                                                                             |
| 8  | `DAVINCI.FLOW.DISABLED`                          | DaVinci Flow Disabled                          | Disabled DaVinci Flow '{name}'                                                                            |
| 9  | `DAVINCI.FLOW.DEBUG_LOGGING.ENABLED`             | DaVinci Flow Debug Logging Enabled             | Debug logging enabled for DaVinci Flow '{name}'                                                           |
| 10 | `DAVINCI.FLOW.DEBUG_LOGGING.DISABLED`            | DaVinci Flow Debug Logging Disabled            | Debug logging disabled for DaVinci Flow '{name}'                                                          |
| 11 | `DAVINCI.COMPANY.ENABLE_ANALYTICS_DEBUG_VIEW`    | DaVinci Company Debug Logging Enabled          | Debug logging for Analytics enabled from Company Settings                                                 |
| 12 | `DAVINCI.FLOW.CUSTOM_JAVASCRIPT.ADDED`           | DaVinci Flow Custom JavaScript Added           | Custom JavaScript added during flow creation for DaVinci Flow '{name}'                                    |
| 13 | `DAVINCI.FLOW.CUSTOM_JAVASCRIPT.ADDED`           | DaVinci Flow Custom JavaScript Added           | Custom JavaScript added during flow cloning for DaVinci Flow '{name}'                                     |
| 14 | `DAVINCI.FLOW.CUSTOM_JAVASCRIPT.ADDED`           | DaVinci Flow Custom JavaScript Added           | Custom JavaScript added during flow import for DaVinci Flow '{name}'                                      |
| 15 | `DAVINCI.FLOW.CUSTOM_JAVASCRIPT.UPDATED`         | DaVinci Flow Custom JavaScript Updated         | Custom JavaScript updated in DaVinci Flow '{name}'                                                        |
| 16 | `DAVINCI.FLOW.CUSTOM_JAVASCRIPT.ADDED`           | DaVinci Connector Custom JavaScript Added      | Custom JavaScript added in '\\{connector name}' Connector Configurations                                  |
| 17 | `DAVINCI.FLOW.CUSTOM_JAVASCRIPT.ADDED`           | DaVinci Connector Custom JavaScript Updated    | Custom JavaScript updated in '\\{connector name}' Connector Configurations                                |
| 18 | `DAVINCI.FLOW.VERSION.REVERTED`                  | DaVinci Flow Version Reverted                  | Flow version reverted from version {n} to version {m}, new version created: {p} for DaVinci Flow '{name}' |
| 19 | `DAVINCI.FLOW.VERSION.ALIAS.UPDATED`             | DaVinci Flow Version Alias Updated             | Flow version alias updated for \\{flow name} (version {n}: {alias})                                       |
| 20 | `DAVINCI.FLOW.VERSION.DELETED`                   | DaVinci Flow Version Deleted                   | Flow version {n} deleted for DaVinci Flow '{name}'                                                        |
| 21 | `DAVINCI.FLOW.SESSION.CONFIGURATIONS.ADDED`      | DaVinci Flow Session Configurations Added      | Session configurations added in DaVinci Flow '{name}'                                                     |
| 22 | `DAVINCI.FLOW.SESSION.CONFIGURATIONS.OVERRIDDEN` | DaVinci Flow Session Configurations Overridden | Session configurations overridden in DaVinci Flow '{name}'                                                |
| 23 | `DAVINCI.CONNECTOR.CREATED`                      | DaVinci Connector Created                      | Created DaVinci Connector '{name}'                                                                        |
| 24 | `DAVINCI.CONNECTOR.UPDATED`                      | DaVinci Connector Updated                      | Updated DaVinci Connector '{name}'                                                                        |
| 25 | `DAVINCI.CONNECTOR.DELETED`                      | DaVinci Connector Deleted                      | Deleted DaVinci Connector '{name}'                                                                        |
| 26 | `DAVINCI.VARIABLE.CREATED`                       | DaVinci Variable Created                       | Created DaVinci Variable '{name}'                                                                         |
| 27 | `DAVINCI.VARIABLE.UPDATED`                       | DaVinci Variable Updated                       | Updated DaVinci Variable '{name}'                                                                         |
| 28 | `DAVINCI.VARIABLE.DELETED`                       | DaVinci Variable Deleted                       | Deleted DaVinci Variable '{name}'                                                                         |
| 29 | `DAVINCI.FLOW_POLICY.CREATED`                    | DaVinci Flow Policy Created                    | Created DaVinci Flow Policy '{name}'                                                                      |
| 30 | `DAVINCI.FLOW_POLICY.UPDATED`                    | DaVinci Flow Policy Updated                    | Updated DaVinci Flow Policy '{name}'                                                                      |
| 31 | `DAVINCI.FLOW_POLICY.DELETED`                    | DaVinci Flow Policy Deleted                    | Deleted DaVinci Flow Policy '{name}'                                                                      |
| 32 | `DAVINCI.APPLICATION.CREATED`                    | DaVinci Application Created                    | Created DaVinci Application '{name}'                                                                      |
| 33 | `DAVINCI.APPLICATION.UPDATED`                    | DaVinci Application Updated                    | Updated DaVinci Application '{name}'                                                                      |
| 34 | `DAVINCI.APPLICATION.DELETED`                    | DaVinci Application Deleted                    | Deleted DaVinci Application '{name}'                                                                      |
| 35 | `DAVINCI.UI_TEMPLATE.CREATED`                    | DaVinci UI Template Created                    | Created DaVinci UI Template '{name}'                                                                      |
| 36 | `DAVINCI.UI_TEMPLATE.UPDATED`                    | DaVinci UI Template Updated                    | Updated DaVinci UI Template '{name}'                                                                      |
| 37 | `DAVINCI.UI_TEMPLATE.DELETED`                    | DaVinci UI Template Deleted                    | Deleted DaVinci UI Template '{name}'                                                                      |

## Audit event structure

DaVinci audit events follow the standard PingOne audit event structure with DaVinci-specific `_embedded` fields.

### Standard fields

| Field                               | Description                                                                                                                        |
| ----------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| `id`                                | Unique audit event ID                                                                                                              |
| `recordedAt`                        | ISO 8601 timestamp when the event was recorded                                                                                     |
| `correlationId`                     | Request correlation ID                                                                                                             |
| `internalCorrelation.transactionId` | Internal DaVinci transaction ID                                                                                                    |
| `actors.client.name`                | Client application that performed the action (for example, `adminui`)                                                              |
| `actors.user.name`                  | User who performed the action (PingOne user email)                                                                                 |
| `actors.user.id`                    | PingOne user ID (UUID)                                                                                                             |
| `source.ipAddress`                  | IP address of the request origin                                                                                                   |
| `source.userAgent`                  | User-agent string                                                                                                                  |
| `action.type`                       | Machine-readable event type (for example, `DAVINCI.FLOW.CREATED`)                                                                  |
| `action.description`                | Human-readable event type label                                                                                                    |
| `resources[].type`                  | Resource type (for example, `DAVINCI_FLOW`, `DAVINCI_CONNECTOR`, `DAVINCI_VARIABLE`, `DAVINCI_APPLICATION`, `DAVINCI_UI_TEMPLATE`) |
| `resources[].id`                    | Resource ID                                                                                                                        |
| `resources[].name`                  | Resource name                                                                                                                      |
| `result.status`                     | `SUCCESS` or `FAILURE`                                                                                                             |
| `result.description`                | Human-readable result description                                                                                                  |

### DaVinci-specific `_embedded` fields

* `_embedded.davinciFlow`

  The following fields are present on flow events:

  | Field                | Description                                                                                           |
  | -------------------- | ----------------------------------------------------------------------------------------------------- |
  | `flowId`             | DaVinci internal flow ID                                                                              |
  | `flowName`           | Human-readable flow name                                                                              |
  | `flowStatus`         | `ACTIVE`, `DISABLED`, or similar                                                                      |
  | `logLevel`           | Current log level: `ERROR`, `DEBUG`, or `INFO`                                                        |
  | `flowType`           | Trigger type: `DEFAULT`, `PINGONE`, `SCHEDULED`, or similar                                           |
  | `flowVersion`        | Flow version number (present on update, enable, and disable events)                                   |
  | `modifiedAttributes` | Array of attribute paths changed during an update (for example, `graphData`, `flowSettings.logLevel`) |
  | `creationSource`     | On custom JavaScript add events: `DIRECT`, `CLONE`, or `IMPORT`                                       |
  | `targetNodeId`       | Node IDs containing the custom JavaScript                                                             |

* `_embedded.davinciFlowVersion`

  The following fields are present on flow version events:

  | Field                 | Description                                |
  | --------------------- | ------------------------------------------ |
  | `flowVersion`         | Version number affected                    |
  | `revertSourceVersion` | Source version number (revert events only) |
  | `flowVersionAlias`    | Version alias string                       |
  | `previousAlias`       | Previous alias value before update         |

* `_embedded.davinciConnector`

  The following fields are present on connector custom JavaScript events:

  | Field                  | Description                                 |
  | ---------------------- | ------------------------------------------- |
  | `connectorInstanceId`  | Connector instance ID                       |
  | `connectorDisplayName` | Display name of the connector instance      |
  | `connectorType`        | Connector type (for example, `PingOne MFA`) |
  | `connectorCategory`    | Connector category                          |

* `_embedded.companySettings`

  The following fields are present on company-level debug logging events:

  | Field                      | Description                                  |
  | -------------------------- | -------------------------------------------- |
  | `enableAnalyticsDebugView` | `true` when company debug logging is enabled |

## API access

DaVinci audit events are accessible through the standard PingOne Activities API:

```
GET /v1/environments/{environmentId}/activities
```

Filter by DaVinci event types using standard PingOne audit filter parameters. For example, `filter=action.type sw "DAVINCI"`.

Learn more in [Audit Activities](https://developer.pingidentity.com/pingone-api/platform/audit-activities.html) in the PingOne API documentation.

---

---
title: Deleting an alert
description: Delete alerts in PingOne.
component: pingone
page_id: pingone:monitoring:p1_delete_alert
canonical_url: https://docs.pingidentity.com/pingone/monitoring/p1_delete_alert.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-05-20T00:00:00Z
keywords: ["delete an alert", "remove an alert"]
section_ids:
  steps: Steps
---

# Deleting an alert

Use the **Alerts** page to remove alerts that you no longer need.

|   |                                                                                                                                                                                                    |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | To unsubscribe from specific alerts or remove an alert from a group of alerts, you don't need to delete the full alert. Learn more about editing alerts in [Editing an alert](p1_edit_alert.html). |

## Steps

1. In the PingOne admin console, go to **Monitoring > Alerts** and browse or search for the alert you want to delete.

2. Click the **More Options** icon (⋮) and select **Delete Alert**.

   ![The alert options list is expanded and shows options for viewing, editing, and deleting the alert, with the Delete Alert option selected.](_images/p1_delete_alert.png)

3. In the **Delete Alert** modal, click **Delete**.

---

---
title: Editing an alert
description: Edit existing alerts in PingOne.
component: pingone
page_id: pingone:monitoring:p1_edit_alert
canonical_url: https://docs.pingidentity.com/pingone/monitoring/p1_edit_alert.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-05-20T00:00:00Z
keywords: ["edit an alert", "modify an alert"]
section_ids:
  steps: Steps
---

# Editing an alert

Use the **Alerts** page to edit an existing alert.

## Steps

1. In the PingOne admin console, go to **Monitoring > Alerts** and browse or search for the alert that you want to edit.

2. Click the **More Options** icon (⋮) and select **Edit Alert**.

   ![A screen capture of editing an alert.](_images/p1_editing_an_alert.png)

3. Edit any of the following options:

   | Option              | Description                                                                                                                                                                                                                                                |
   | ------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | **Name**            | Edit the name of the alert.                                                                                                                                                                                                                                |
   | **Email Addresses** | Edit the addresses that receive the alert. You can specify one or more individual or mailing list email addresses. Multiple email addresses must be separated by commas.&#xA;&#xA;Copy the email addresses to the clipboard to use them for another alert. |
   | **Alert Types**     | Use the checkboxes to subscribe or unsubscribe to event types that trigger alerts. For example, if you clear the checkbox for **Certificate Expired**, that alert won't be triggered when a certificate in your environment expires.                       |

4. Click **Save**.

---

---
title: MFA dashboard
description: View a summary of MFA activity, SMS and voice usage, costs, and user devices in the PingOne MFA dashboard.
component: pingone
page_id: pingone:monitoring:p1_mfa_dashboard
canonical_url: https://docs.pingidentity.com/pingone/monitoring/p1_mfa_dashboard.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-07-10T00:00:00Z
---

# MFA dashboard

The **MFA dashboard** shows a summary of current multi-factor authentication (MFA) *(tooltip: \<div class="paragraph">
\<p>An electronic authentication method where a user is granted access only after presenting two or more verification factors for authentication.\</p>
\</div>)* activity, SMS and voice usage and costs, and user devices.

You can limit the data to a specific time range, authentication method, status, or device OS with filters.

Learn more about MFA dashboard charts in [MFA Dashboard](../strong_authentication_mfa/p1_using_mfa_dashboard.html).

---

---
title: Monitoring
description: Access PingOne dashboards, audit logs, and alerts from the Monitoring section of the admin console.
component: pingone
page_id: pingone:monitoring:p1_monitoring_menu
canonical_url: https://docs.pingidentity.com/pingone/monitoring/p1_monitoring_menu.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-07-10T00:00:00Z
---

# Monitoring

The **Monitoring** branch provides access to the platform and services dashboards, as well as to the **Audit** and **Alerts** pages.

For more information, see the following topics:

[Dashboards](p1_dashboards.html)

[Audit](p1_reporting.html)

[Alerts](p1_alerts.html)

---

---
title: Running an audit report
description: Run reports to see a summary of user events or actions performed in PingOne.
component: pingone
page_id: pingone:monitoring:p1_running_audit_report
canonical_url: https://docs.pingidentity.com/pingone/monitoring/p1_running_audit_report.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-07-23T00:00:00Z
section_ids:
  steps: Steps
  result: Result
  next-steps: Next steps
---

# Running an audit report

You can run reports to see a summary of user events or events for actions performed in the PingOne admin console.

|   |                                                                                                                                                                                                                       |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | You can find a complete list of events logged in PingOne in [Audit Reporting Events](https://developer.pingidentity.com/pingone-api/platform/reference/audit-reporting-events.html) in the PingOne API documentation. |

## Steps

1. In the PingOne admin console, go to **Monitoring > Audit** and enter the report parameters.

   Learn more in [Audit parameters](p1_auditparameters.html).

   ![A screen capture of the Audit Parameters section without any selections made.](_images/p1-monitoring-audit-params.png)

   | Option                    | Description                                                                                                                                                                                                                                                                                                                                                                                                  |
   | ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
   | **Time Range**            | Limit the report results to a specific time period.&#xA;&#xA;Data up to 14 days old relative to the current date is available immediately. Data older than 14 days must be requested from the Audit page or using the API. You can't request data for dates that are more than 2 years (730 days) before the current date.&#xA;&#xA;You can run reports or retrieve data for a maximum of 14 days at a time. |
   | **Filter Type**           | Limit the results to a particular type, user, or resource. Learn more about the filters available in [Audit parameters](p1_auditparameters.html).                                                                                                                                                                                                                                                            |
   | **Selected Fields**       | Specify which columns appear in the results list.                                                                                                                                                                                                                                                                                                                                                            |
   | **Time Zone**             | Specify the time zone to use in the results list. The timestamp shows the date and time for the selected time zone.                                                                                                                                                                                                                                                                                          |
   | **Secondary Filter Type** | Specify a secondary filter to further limit the results to a particular type, user, or resource. You must specify a primary filter type before you can select a secondary filter type.                                                                                                                                                                                                                       |

2. Click **Run Report**.

## Result

The information displayed depends on the date range for which you requested data.

* Within the 14-day window for immediate availability

  For example, on May 4, 2026, you enter a relative time range of 9 days, or a specific date range of `2026-04-26` to `2026-05-04`.

  Full results display immediately for the requested dates because no older data needs to be retrieved.

  ![A screen capture of the Audit Report results for a 9 day time range in the current 14-day reporting retrieval window.](_images/p1-audit-report-results.png)

* Outside of the 14-day window for immediate availability

  For example, on July 23, 2026, you enter a specific date range of `2026-07-01` to `2026-07-08`.

  The **Run Report** modal displays explaining that the requested data isn't immediately available and must be retrieved. The requested dates are displayed in the modal. Select the checkbox and then click **Run Report** to retrieve data for the requested dates.

  ![A screen capture of the Run Report modal with a message to retrieve data because requested dates aren't immediately available.](_images/p1-audit-retrieval-modal.png)

  A message indicating a data retrieval is in progress displays in the **Available Dates (UTC)** section of the **Audit Parameters** page.

* Includes both dates for which data is immediately available and dates for which data must be retrieved

  For example, on August 7, 2026, you enter a specific date range with a start date of `2026-07-16` and an end date of `2026-07-27`.

  This range includes 9 days of data that must be retrieved (`2026-07-16` to `2026-07-24`) and 3 days of immediately available data (`2026-07-25` to `2026-07-27`).

  The **Run Report** modal displays, and you must confirm that you want to retrieve the data for the dates that aren't immediately available. Select the checkbox and then click **Run Report** to retrieve data for the requested dates.

  ![A screen capture of the Run Report modal with a message to retrieve data for some dates because requested dates aren't immediately available.](_images/p1-audit-retrieval-modal-mixed-dates.png)

  The results display for the dates that are immediately available. A message indicating a retrieval request for the older data is in progress displays in the **Available Dates (UTC)** section of the **Audit Parameters** page.

  |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
  | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | * Depending on the number of days requested and the average number of events logged per day, the process can take from 2 to 24 hours.

  * You can request a maximum of 14 days of data within the data retention period, and you can't request additional data while another request is pending. If you request more than 14 days of data, or another request is pending, the checkbox in the **Run Report** modal is disabled and you can't submit the request.

  * If you have a valid email address in PingOne, you'll receive a notification email when the data is ready. After the data is retrieved, you can return to the **Audit Parameters** page and run reports against the data for the timeframe requested.

  * The retrieved data is available for 14 days from the date of the retrieval request. |

## Next steps

* To rearrange the columns in the report summary, click **Columns**. The **Re-order Columns** modal displays. Drag the columns into the order you want to display them, then click **Save**.

* To view the details of an event, click **View** in the **Details** column.

* To export your results to a CSV file, click **Export**.

---

---
title: User Demographics Dashboard
description: View a summary of user demographic profiles, identity counts, and authentication activity in the User Demographics Dashboard.
component: pingone
page_id: pingone:monitoring:p1_user_demographic_dashboard
canonical_url: https://docs.pingidentity.com/pingone/monitoring/p1_user_demographic_dashboard.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-07-10T00:00:00Z
section_ids:
  filters: Filters
  charts: Charts
---

# User Demographics Dashboard

The **User Demographics Dashboard** shows a summary of user demographic profiles and activity for the selected environment.

To access the **User Demographics Dashboard**, in the PingOne admin console, go to **Monitoring > User Demographics**.

![A screen capture of the User Demographics Dashboard.](_images/userdemographicsdashboard.png)

## Filters

You can limit the data to:

* **Today**

* **From Yesterday**

* **Last 7 Days** (Default)

* **Last 30 Days**

* **Last 90 Days**

* **This Month**

* **Last Month**

* **Custom Range**

|   |                                                                                                                                                                                   |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Data older than 180 days is not available for filtering. You can only select dates within a 6 month window\.The charts are always shown in UTC time, regardless of the selection. |

## Charts

Use the following controls to adjust the charts:

| Icon                                                                | Name         | Description                                                                                                                                                                                              |
| ------------------------------------------------------------------- | ------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ![The Maximize icon.](../_images/p1-dashboard-maximize.png)         | Maximize     | Expands the chart to fill the dashboard.To minimize the chart, click the icon again.                                                                                                                     |
| ![The Menu options icon.](../_images/p1-dashboard-menu-options.png) | Menu options | Options can vary for different types of charts:- **View summary data**: Displays chart data as a table.

- **Export to CSV**: Exports chart data to CSV or Excel format, depending on the type of chart. |

**Total Identities**

Displays the total count of identities in the environment at the current date and time.

|   |                                                                                                                                                                                      |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | The **Total Identities** and **Total Identities by Population** charts are not affected by the date filter. They always display current data, regardless of the selected date range. |

**Total Identities by Population Over Time**

Displays the daily changes in the total count of identities, broken down by population groups over time. This chart shows how the identity count changes, indicating trends in different populations.

The top 10 populations by number display in the chart distribution. All other populations are cumulatively counted under **Other**.

**Total Identities by Population**

Displays the current distribution of identities by population.

**Authentication OS Distribution**

Displays the distribution of authentication attempts by the operating system for the selected time period.

|   |                                                                                                                                                                                                                               |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Updates for **Authentication OS Distribution** and **Authentication Browser Distribution** happen once a day at midnight, UTC. Depending on your time zone, these updates might not be visible for you at the end of the day. |

**Authentication Browser Distribution**

Displays the distribution of authentication attempts by browser distribution for the selected time period.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | **Authentication OS Distribution** and **Authentication Browser Distribution** charts only display data for single sign-on (SSO) *(tooltip: \<div class="paragraph">&#xA;\<p>The process of authenticating an identity (signing on) at one website (usually with a user ID and password) and then accessing resources secured by other domains without reauthenticating.\</p>&#xA;\</div>)* and do not include multi-factor authentication (MFA) *(tooltip: \<div class="paragraph">&#xA;\<p>An electronic authentication method where a user is granted access only after presenting two or more verification factors for authentication.\</p>&#xA;\</div>)*. The [MFA dashboard](p1_mfa_dashboard.html) has the mobile Authentication OS distribution chart. |

**DaVinci OS Distribution**

Displays the distribution of DaVinci usage by operating system for the selected time period.

**DaVinci Browser Distribution**

Displays the distribution of DaVinci usage by browser for the selected time period.

**Protect OS Distribution**

Displays the distribution of successful Protect risk evaluations by Operating System for the selected time period.

**Protect Browser Distribution**

Displays the distribution of successful Protect risk evaluations by browser distribution for the selected time period.

**MFA OS Distribution**

Displays the distribution of MFA attempts by operating system for the selected time period.

---

---
title: User devices and app version charts
description: View user device usage by authentication method and mobile app usage by version using the User Devices and App Version charts.
component: pingone
page_id: pingone:monitoring:p1_user_devices_and_app_version_chart
canonical_url: https://docs.pingidentity.com/pingone/monitoring/p1_user_devices_and_app_version_chart.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-07-10T00:00:00Z
---

# User devices and app version charts

The **User Devices** chart enables you to view current information for user devices per authentication method, and mobile app users per app version.

Use the **User Devices/App Version** filter to select the chart type that you want to view.

**User Devices chart**: view devices used by authentication method.

![Screen shot showing the User Devices chart](_images/kmu1704098587222.png)

**App Version chart**: view mobile applications by version.

![Screen capture showing the App Version chart](_images/sdw1704099712927.png)

The filter options available vary depending on which chart you select:

* Authentication method

  Select the authentication methods you want to include in the results. For the App Version chart, only **Mobile app** is relevant.

* Primary/Secondary

  * **Primary** to view data for devices defined as the user's primary device only.

  * **Secondary** to view data for devices defined as the user's secondary devices only.

  * **Both** to include both primary and secondary devices.

* Mobile app OS

  View data per mobile OS. Select either:

  * **iOS** to view data for iOS devices only.

  * **Android** to view data for Android devices only.

  * **Both** to view data for iOS and Android devices.

* Amount/Percent

  View data by either the number of devices, or the percentage of the total number of devices.

---

---
title: Viewing alerts
description: View and manage alerts for your current environment in PingOne.
component: pingone
page_id: pingone:monitoring:p1_view_alerts
canonical_url: https://docs.pingidentity.com/pingone/monitoring/p1_view_alerts.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2024-05-07T00:00:00Z
keywords: ["view alerts", "manage alerts"]
section_ids:
  steps: Steps
---

# Viewing alerts

Use the **Alerts** page to view and manage alerts for your environment.

## Steps

1. In the PingOne admin console, go to **Monitoring > Alerts**.

   The **Alerts** page shows the alerts that are currently configured for your environment.

   ![A screen capture of the viewing alerts.](_images/p1_view_alerts.png)

2. Browse or search for the alert that you want to view, and click the entry to open the details panel.

   ![A screen capture of the alerts panel.](_images/p1_details_panel_view.png)

   The alert details panel shows the following:

   | Option              | Description                                                                                                                                                                                                       |
   | ------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | **Include alerts**  | The event types that will trigger the alert. To learn more about the different alert types, see [Alerts](p1_alerts.html).                                                                                         |
   | **Alert ID**        | The unique identifier for the alert.                                                                                                                                                                              |
   | **Email Addresses** | The email addresses to which the alert will be sent. You can specify one or more email addresses, separated by commas. When the alert is triggered, a notification will be sent to the specified email addresses. |
   | **Send Via**        | The alert channel used to deliver the alert. Only email is supported.                                                                                                                                             |