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
