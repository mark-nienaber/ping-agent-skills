---
title: Alerts
description: Configure alerts to send messages about the status of particular resources in PingOne.
component: pingone
page_id: pingone:monitoring:p1_alerts
canonical_url: https://docs.pingidentity.com/pingone/monitoring/p1_alerts.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 20, 2026
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
revdate: April 17, 2024
section_ids:
  learn-more: Learn more
---

# Audit

PingOne logs three types of data that are governed by different retention policies:

* **User events**

  User events include user creation or deletion, authentications, updates to the user record, and other transactions related to end-user activity. User events are retained for 90 days.

* **PingOne** admin console events

  Configuration events include configuration changes made to system settings, policies, applications, and integrations. Configuration events are retained for 2 years.

* **DaVinci** admin events

  DaVinci administrative events, such as flow creation, connector updates, and variable changes. Learn more in [DaVinci administrative audit events in PingOne (early access)](../early-access-features/ea_p1_davinci_audit_events.html).

You can run audit reports from **Monitoring > Audit** or using the PingOne APIs to view data about user and console events. You can run queries against a maximum of 14 days at a time.

|   |                                                                                                                                                                                                                                       |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | To retain PingOne data for longer than the standard retention periods, set up webhooks to stream the data to your own repository and configure your own retention policy. Learn more in [Webhooks](../integrations/p1_webhooks.html). |

## Learn more

Learn more about PingOne logging and reporting capabilities in [PingOne Platform logging and reporting](../getting_started_with_pingone/p1_logging_reporting_overview.html).

Learn more about running audit reports in PingOne in the following topics:

* [Audit parameters](p1_auditparameters.html)

* [Running an audit report](p1_running_audit_report.html)

* [DaVinci administrative audit events in PingOne (early access)](../early-access-features/ea_p1_davinci_audit_events.html)

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
revdate: May 3, 2024
page_aliases: ["p1_event_types.adoc"]
section_ids:
  time-range: Time Range
  filter-type: Filter Type
  selected-fields: Selected Fields
  secondary-filter-type: Secondary Filter Type
---

# Audit parameters

Use audit parameters to specify the details of your search results.

## Time Range

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | Data up to 14 days old relative to the current date is available immediately. Data older than 14 days must be requested from the **Audit** page or using the API, and you can't request data for dates that are more than 2 years (730 days) before the current date.Depending on the number of days requested and the average number of events logged per day, the retrieval process can take from 2 to 24 hours. You can request a maximum of 14 days of data from within the data retention period, and you can't request additional data while another request is pending.If you have a valid email address in PingOne, you'll be notified when the requested data is available. At that point, you can return to the **Audit** page and run queries against the data for the timeframe requested. The retrieved data is available for 14 days from the date of the retrieval request. |

* **Relative**

  A time range relative to the current time. Under **Within**, select a number and a time period. For example, **2** **weeks**.

* **Specific Date**

  A time range with a specified start and end date, such as "March 27 to April 10." Optionally, you can specify the time of day using the **Hour** and **Minute** fields for the start and end dates.

|   |                                                                                                                                                          |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | If you enter a time range further than 2 years (730 days) from the current date, you're prompted to adjust the time range before submitting the request. |

## Filter Type

Limit the search results based on the specified parameters.

* **Resource ID**

  Find activities by resource ID. For PingOne DaVinci events, enter a flow ID, variable ID, connector instance ID, flow policy ID, application ID, or UI template ID to scope results to a specific DaVinci resource.

* **Correlation ID**

  Find activities by correlation ID. When an HTTP request is received, it's assigned a correlation ID. You can use the correlation ID to associate HTTP responses with messages in the event log.

* **Event Type**

  Find activities by event type. Select an event type in the list. DaVinci-specific event types are included and can be selected simultaneously to filter for multiple event types at the same time. You can find a complete list of events logged in PingOne in [Audit Reporting Events](https://developer.pingidentity.com/pingone-api/platform/reference/audit-reporting-events.html) in the PingOne API documentation.

* **User ID (Actor)**

  Find activities that were performed by a particular user, by user ID.

* **User Name (Actor)**

  Find activities that were performed by a particular user, by user name.

* **Client (Actor)**

  Find activities that were performed by a particular client. Select a client in the **Filter** list. The list of clients varies depending on your configuration.

* **Resource Population**

  Find activities that were performed in resources within a particular population. Select a population in the list.

* **Resource Type**

  Find activities that were performed on a particular type of resource. Select a resource in the list. A **DaVinci** subsection is available to filter for DaVinci-related audit events. Learn more about individual DaVinci resource type filters in [Filtering DaVinci events](../early-access-features/ea_p1_davinci_audit_events.html#filtering-davinci-events).

* **Population**

  Find activities that were performed on a particular population.

* **User**

  Find activities that were performed on a particular user.

* **Application**

  Find activities that were performed by a particular client application.

## Selected Fields

Specify which fields appear in the results list.

* **Timestamp**

  The date and time of the event. The format is: MM/DD/YYYY hh:mm:ss.

* **Event Name**

  A unique identifier for the event.

* **Description**

  A brief description of the event.

* **Client**

  The client that performed the event.

* **User Identity**

  The user for which the event was performed.

* **Population**

  The population for which the event was performed.

* **Resource Type**

  The type of resource for which the event was performed.

## Secondary Filter Type

Specify a secondary filter for your results.

|   |                                                                                                                                                                                                          |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | You must specify a primary filter type before you can select a secondary filter type. The **Secondary Filter Type** list contains all of the filter types that you didn't select as your primary filter. |

---

---
title: Authentication dashboard
description: View a summary of sign-on activity, MFA adoption, total identities, and password resets in the PingOne Authentication dashboard.
component: pingone
page_id: pingone:monitoring:p1_auth_dashboard
canonical_url: https://docs.pingidentity.com/pingone/monitoring/p1_auth_dashboard.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 10, 2026
section_ids:
  cards: Cards
  sign-ons-by-dayhour: Sign-ons by day/hour
---

# Authentication dashboard

The Authentication dashboard shows a summary of sign-on activity through PingOne sign-on policies for the selected environment.

|   |                                                                     |
| - | ------------------------------------------------------------------- |
|   | The Authentication dashboard does not include DaVinci transactions. |

You can limit the data to a specific time range, such as the current day, the current week, the current month, or the previous three months.

The graph at the top of the page shows sign-on activity at a glance, including the number of successful user sign-ons for the current day, and a graph showing the number of successful sign-ons and the number of failed sign-ons for the specified period.

## Cards

The cards show the following information:

* **MFA adoption**

  The current percentage of MFA-enabled users. Select a timeframe of 30 days, 12 weeks, or 1 year to see the evolution of the MFA adoption rate. This information can help administrators visualize trends and inform decisions.Hover over the area chart to see exact information on rate and date for a particular point in time. The back of the card shows a snapshot of historical rates.

* **Total identities**

  The number of active users for the specified period.

* **Total password resets**

  The number of times users have requested password resets over the specified period.

The cards show a graphical view on one side and a list view on the other. Click the icon on the top right of the card to toggle between views.

## Sign-ons by day/hour

The **Sign-ons by day/hour** shows relative authentication activity by hour of the day and day of the week. The color variations show usage trends throughout an average week.

Hover over the map to see the actual average of sign-ons to more accurately quantify the variation between periods. You can use this information to better understand users' habits as well as identify periods of interest, such as typical highs and lows.

---

---
title: Creating an alert
description: Create alerts in PingOne to receive notifications about the status of particular resources in your environment.
component: pingone
page_id: pingone:monitoring:p1_add_alert
canonical_url: https://docs.pingidentity.com/pingone/monitoring/p1_add_alert.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 26, 2026
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
revdate: January 2, 2025
section_ids:
  pingone: PingOne
  pingone-services: PingOne Services
---

# Dashboards

**Dashboards** contains the different dashboards for PingOne and your configured PingOne services.

## PingOne

* [Authentication Dashboard](p1_auth_dashboard.html): View a summary of sign-on activity for the selected environment.

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
title: Deleting an alert
description: Delete alerts in PingOne.
component: pingone
page_id: pingone:monitoring:p1_delete_alert
canonical_url: https://docs.pingidentity.com/pingone/monitoring/p1_delete_alert.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 20, 2026
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
revdate: May 20, 2026
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
revdate: July 10, 2026
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
revdate: July 10, 2026
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
description: Run reports to see a summary of actions performed in the PingOne admin console.
component: pingone
page_id: pingone:monitoring:p1_running_audit_report
canonical_url: https://docs.pingidentity.com/pingone/monitoring/p1_running_audit_report.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 22, 2024
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

   ![A screen capture of the Audit Parameters section without any selections made.](_images/p1-monitoring-audit-params.png)

   * **Time Range**: Limit the report results to a specified range of time.

     |   |                                                                                                                                                                                                                                                                                                                                                                                                                       |
     | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
     |   | Data up to 14 days old relative to the current date is available immediately. Data older than 14 days must be requested from the **Audit** page or using the API, and you can't request data for dates that are more than 2 years (730 days) before the current date. You can run reports a maximum of 14 days at a time. If you enter an invalid time range, you're prompted to adjust it before you run the report. |

   * **Filter type**: Limit the results to a particular type, user, or resource.

   * **Selected fields**: Specify which columns appear in the results list.

   * **Time zone**: Specify the time zone to use in the results list. The timestamp shows the date and time for the selected time zone.

   * **Secondary Filter Type**: Specify a secondary filter to limit the results to a particular type, user, or resource. You must specify a primary filter type before you can select a secondary filter type.

2. Click **Run**.

## Result

The information displayed depends on the date range for which you requested data:

* Within the 14-day window for immediate availability

  For example, on September 30, 2025, you enter a relative time range of 2 weeks, or a specific date range of `2025-09-22` to `2025-09-29`.

  Full results are displayed.

  ![p1 audit report results](_images/p1-audit-report-results.png)

* Outside of the 14-day window for immediate availability

  For example, on September 30, 2025, you enter a specific date range of `2025-09-09` to `2025-09-16`.

  The **Run Report** modal is displayed explaining that the requested data isn't immediately available and must be retrieved. The requested dates are displayed in the modal. Select the checkbox next to **Retrieve Event data from** `date1` **to** `date2` **(UTC)** and then click **Run Report**.

  If you have a valid email address in PingOne, you'll be notified when the data is ready. After the data is retrieved, you can return to the **Audit** page and run reports against it for 14 days from the retrieval date.

  ![A sample of the Run Report modal when all requested dates require retrieval](_images/p1-audit-retrieval-modal.png)

* Includes both dates for which data is immediately available and dates for which data must be retrieved

  For example, on October 21, 2025 you enter a specific date range with a start date of `2025-09-28` and an end date of `2025-10-10`. This range includes 10 days of data that must be retrieved (2025-09-28 to 2025-10-07) and 3 days of immediately available data (2025-10-08 to 2025-10-10).

  The **Run Report** modal is displayed, and you must confirm that you want to retrieve the data for the dates that aren't immediately available. Select the checkbox next to **Retrieve Event data from** `date1` **to** `date2` **(UTC)** and then click **Run Report**.

  ![A sample of the Run Report modal when some requested dates require retrieval but others are available immediately](_images/p1-audit-retrieval-modal-mixed-dates.png)

  The results for the dates that are immediately available are displayed, and the data for older dates is requested. If you have a valid email address in PingOne, you'll be notified when the additional data is ready for reporting, and at that point you can run the report again.

  ![A sample audit report showing immediate results and dates for data that was requested](_images/p1-audit-report-mixed-dates.png)

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | - The **Available Dates (UTC)** section lists the dates for the data that's available to query or has been requested.

- Depending on the number of days requested and the average number of events logged per day, the process can take from 2 to 24 hours. You can request a maximum of 14 days of data from within the data retention period and you can't request additional data while another request is pending.

  If you have a valid email address in PingOne, you'll be notified when the requested data is available. At that point, you can return to the **Audit** page and run queries against the data for the timeframe requested. The retrieved data is available for 14 days from the date of the retrieval request. |

## Next steps

* To rearrange the columns in the report summary, drag the column heading to the desired position.

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
revdate: July 10, 2026
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

|   |                                                                                                                                                                                                                           |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Updates for **Authenticate OS Distribution** and **Authenticate Browser Distribution** happen once a day at midnight, UTC. Depending on your time zone, these updates might not be visible for you at the end of the day. |

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
revdate: July 10, 2026
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
revdate: May 7, 2024
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