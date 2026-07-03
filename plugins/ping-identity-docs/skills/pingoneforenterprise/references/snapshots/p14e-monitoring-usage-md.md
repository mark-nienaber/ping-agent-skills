---
title: PingOne for Enterprise usage monitoring
description: The following reports help you track single sign-on (SSO) usage, which partially determines your PingOne for Enterprise billing.
component: pingoneforenterprise
page_id: pingoneforenterprise::p14e_monitoring_usage
canonical_url: https://docs.pingidentity.com/pingoneforenterprise/p14e_monitoring_usage.html
revdate: June 7, 2022
section_ids:
  pingone-for-enterprise-usage-reports: PingOne for Enterprise usage reports
  pingone-sso-for-saas-apps-usage-reports: PingOne SSO for SaaS Apps usage reports
  subscriptions: Subscriptions
---

# PingOne for Enterprise usage monitoring

The following reports help you track single sign-on (SSO) usage, which partially determines your PingOne for Enterprise billing.

To run these reports, go to **Dashboard > Reporting**. For more information see [Reports](pingone_for_enterprise/p14e_reports.html).

## PingOne for Enterprise usage reports

* SSO Summary

  This report lists the number of SSO transactions by application during the specified time period. Because the report tracks SSO usage by application, the same user is counted multiple times if they access multiple applications. Therefore, the report total will be higher than your actual SSO usage.

* SSO User Summary

  This report lists all of the usernames that used SSO during the specified period. You can export the list to audit or count it. Deleting users from **Users by Service** deletes them from this report, but it doesn't delete them from Ping's historical records for billing and licensing purposes. Deleted users are restored to the report the next time they use SSO. For more information, see [Temporarily hiding a user's service](pingone_for_enterprise/p14e_temporarily_hide_users_service.html).

## PingOne SSO for SaaS Apps usage reports

* SSO Summary by Customer

  This report lists the unique usernames that accessed each of your applications through PingOne SSO for SaaS Apps. Because the report tracks SSO usage by application, the same user is counted multiple times if they access multiple applications. Therefore, the report total will be higher than your actual SSO usage.

* SSO User Count

  This report provides a count of unique usernames that accessed your applications through PingOne SSO for SaaS Apps for each of your customers. Because this report counts totals for each customer rather than by application, you can use these numbers to determine exact SSO usage by customer. Summing these amounts gives you the total number of unique users, which will match Ping's internal usage numbers for billing and licensing purposes.

## Subscriptions

You can also set up real-time SSO usage monitoring through the **Subscriptions** tab. Setting up an **SSO** subscription in PingOne for Enterprise or PingOne SSO for SaaS Apps allows you to send SSO events to your own external system so that you can track the number of unique users.

For more information, see [Subscriptions](pingone_for_enterprise/p14e_subscriptions.html).
