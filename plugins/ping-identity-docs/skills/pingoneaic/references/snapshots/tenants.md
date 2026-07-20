---
title: Advanced Identity Cloud analytics dashboard
description: PingOne Advanced Identity Cloud analytics dashboard provides a comprehensive snapshot of your Advanced Identity Cloud system usage. You can use the dashboard to gain valuable insights on your tenants:
component: pingoneaic
page_id: pingoneaic:tenants:analytics-dashboard
canonical_url: https://docs.pingidentity.com/pingoneaic/tenants/analytics-dashboard.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Identity Cloud", "Analytics", "Dashboard", "Troubleshooting"]
section_ids:
  monitor-users: Monitor the number of users and engagements
  filter-timelines: Filter timelines
  change-timeperiods: Change the time period for the trendline charts
  monitor-journeys: Monitor journeys
  filter-journeys: Filter journeys
  access-journey-pass-fail-details: Access journey pass/fail details
  access-metric-breakdown: Access the metric breakdown page
  access-top-five-and-journey-usage-widgets: Top Five Journeys by Outcome and Top Five Journeys by Usage widgets
  access-top-five: Access top five journeys by outcome and top five journeys by usage
  notice: Notice
---

# Advanced Identity Cloud analytics dashboard

PingOne Advanced Identity Cloud analytics dashboard provides a comprehensive snapshot of your Advanced Identity Cloud system usage. You can use the dashboard to gain valuable insights on your tenants:

* [Monitor the number of users and engagements](#monitor-users)

* [Monitor journeys](#monitor-journeys)

* [Access journey pass/fail details](#access-journey-pass-fail-details)

* [Top Five Journeys by Outcome and Top Five Journeys by Usage widgets](#access-top-five-and-journey-usage-widgets)

![Analytics Dashboard](../_images/idcloud-analytics-dashboard-new.png)

## Monitor the number of users and engagements

At the top of the Identity Cloud analytics dashboard, there is a summary of total number of users, applications, and organizations in your realm. These realm usage totals are summarized as follows:

* **Total Users**. Displays the total count of *active* and *inactive* users in this realm.

* **Applications**. Displays the total number of *current* applications in this realm.

* **Organizations**. Displays the total number of organizations in this realm.

![Analytics Dashboard Summary page](../_images/idcloud-analytics-dashboard-summary.png)

Below the realm usage totals, Identity Cloud analytics dashboard displays three trendline charts: user engagements, total users, and new users. These trendline charts are updated every two to three hours and are summarized as follows:

* **User Engagement**. Displays the trendline of the number of user engagements within a given time period; by default, the last 30 days. A user engagement is counted when a user is involved in an identity operation within the given time period. An identity operation can be any of the following:

  * Sign-in/authentication

  * Token refresh (for example, token issuance, validation, and refresh)

  * Password creation or change

    |   |                                                                                        |
    | - | -------------------------------------------------------------------------------------- |
    |   | A user who has multiple user engagements within a given time period is counted *once*. |

* **Total Users Trend**. Displays the trendline for total users (active and inactive) during the time period in this realm.

  |   |                                                                                                                                                                                                                                                                                      |
  | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
  |   | The total users trend number may differ from the `Total Users` number at the top of the page as the data depends on the selected time period and the update frequency. For example, new users who have been added to the system within the last hour may not appear yet on the page. |

* **Sign Ups**. Displays the trendline for new user sign-ups during the time period in this realm.

### Filter timelines

Each chart displays the usage numbers for the *current* time period, expressed as solid lines; the dotted lines display the numbers for the *previous* time period. For example, if the time period is `Last 30 days,` the solid line displays the numbers over the last 30 days from today's date; the dotted line displays the *previous* 30-day numbers.

To compare the numbers for a specific date, hover over a point on either line to display the numbers for the current and the previous time periods.

![Analytics Dashboard Trends page](../_images/idcloud-analytics-dashboard-trends.png)

By default, the Identity Cloud analytics dashboard displays the number of engagements, total users, and new user sign-ups for a 30-day period, you can filter the output by changing the time period.

### Change the time period for the trendline charts

1. Click Last 30 days, and select one of the following time periods:

   * **Today**. Displays the numbers for `today,` 12:00 a.m. to the current time.

   * **Yesterday**. Displays the numbers for `yesterday,` 12:00 a.m. to 12:00 p.m. on the previous day.

   * **Last 7 Days**. Displays the numbers for the last seven days from today's date.

   * **Last 30 Days**. Displays the last 30 days from today's date. This is the default time period.

     |   |                                                   |
     | - | ------------------------------------------------- |
     |   | All dates and time periods are based on UTC time. |

2. Click Apply to save your changes.

![Analytics Dashboard Trends time periods filtering](../_images/idcloud-analytics-dashboard-timeperiod.png)

## Monitor journeys

You can refer to a chart on the number of successful and failed journey outcomes within your realm on the Identity Cloud analytics dashboard. Scroll down the Identity Cloud analytics dashboard page to refer to the `Journeys` graph.

By default, the Identity Cloud analytics dashboard displays the aggregation of all successful and failed journeys on the Advanced Identity Cloud. These aggregations express four different types of information:

* Blue lines indicate successful journey outcomes.

* Red lines indicate failed journey outcomes.

* Solid lines indicate the journey outcomes that occurred within the *current* selected time period.

* Dotted lines indicate the journey outcomes in the *previous* time period.

|   |                                                                                         |
| - | --------------------------------------------------------------------------------------- |
|   | The journey usage is *not* counted if the journey is used as a node in another journey. |

![Analytics Dashboard Journeys section](../_images/idcloud-analytics-dashboard-journeys.png)

The Identity Cloud analytics dashboard also lets you filter the chart by journey type. The available journeys are listed on the Advanced Identity Cloud Journeys page and includes any custom journeys that you may have configured. For example:

* EvaluateRisk

* ForgottenUsername

* Login (default)

* PasswordGrant

* ProgressiveProfile

* Registration

* ResetPassword

* Sample Tree

* UpdatePassword

The categories are:

* Authentication

* Password Reset

* Progressive Profile

* Registration

* Username Reset

|   |                                                                               |
| - | ----------------------------------------------------------------------------- |
|   | The journeys and categories options come from any tag that you have selected. |

### Filter journeys

1. On the Journeys chart, click All journeys.

2. On the Filter Journeys dialog box, select one or more journeys on the drop-down list to include in your chart.

3. Click Apply to update your journeys chart. The changes appear immediately.

## Access journey pass/fail details

The Journeys chart also lets you drill down at specific points on a trendline to access its details, or *metric breakdown*. Red lines indicate failed journeys. Blue lines indicate successful journeys.

For example, you can use the Metric Breakdown page to review the journeys for the selected date, sorted by a ranking of percentage failures (default). The percentage is calculated for each journey as the total outcomes passed or failed, and then sorted in descending order from the highest failed journey by percentage to the lowest failed journey by percentage.

![Analytics Dashboard Metric Breakdown page sorted by percentage success or failures](../_images/idcloud-analytics-dashboard-metric-breakdown-percentage.png)

The Metric Breakdown page also lets you sort the journeys by *number* ranking. *Number* indicates the actual number of successful or failed outcomes for each journey.

The following table provides an example of how the analytics dashboard ranks by percentage and by number:

**Metric Breakdown Example of How Percentage Rank and Number Rank and Determined**

| Journey | Total Outcomes | Passed | Failed    | Percentage Rank | Number Rank |
| ------- | -------------- | ------ | --------- | --------------- | ----------- |
| A       | 900            | 630    | 270 (30%) | 2               | 1           |
| B       | 100            | 50     | 50 (50%)  | 1               | 2           |
| C       | 100            | 80     | 20 (20%)  | 3               | 3           |

|   |                                                     |
| - | --------------------------------------------------- |
|   | Timeouts are not displayed in the Journey outcomes. |

### Access the metric breakdown page

1. On the Journeys chart, hover anywhere over a trendline to view the successful or failed outcomes for that date, and then click View detail. The Metric Breakdown page appears with more insights on the individual journeys. By default, All Journeys and Percentage are selected.

2. On the Metric Breakdown page, click Number to display the number of failed and successful journeys sorted by rank.

   > **Collapse: Click to show how to access the metric breakdown page**
   >
   > ![How to access the Metric Breakdown page](../_images/idcloud-analytics-dashboard-metric-breakdown.gif)

## Top Five Journeys by Outcome and Top Five Journeys by Usage widgets

The Identity Cloud analytics dashboard displays two additional widgets providing trendlines into your journeys: Top Five Journeys by Outcome and Top Five Journeys by Usage. The Top Five Journeys by Outcome widget displays the top five journeys ranked by percentage failed or successful. The default selection is *Fail*. You can change the selection to *Success* to display top five successful journeys.

The Top Five Journeys by Usage widget displays the top five most or least used journeys. By default, the *most used* journeys are selected. Each bar chart provides the percentage usage of the journey in the given time period based on the outcomes only. For each journey, the calculation is based on the total number of outcomes for the journey divided by the total number of all journey outcomes in the time period.

|   |                                                                                                                                        |
| - | -------------------------------------------------------------------------------------------------------------------------------------- |
|   | The widgets only display the journey outcomes for the selected time period. The x-axis denotes the percentage outcomes in the journey. |

![Analytics Dashboard Top Five Journeys by Outcome and Top Five Journeys by Usage Widgets](../_images/idcloud-analytics-dashboard-top-five-usage-widgets.png)

### Access top five journeys by outcome and top five journeys by usage

1. On the Top Five Journeys by Outcome widget, the widget displays the top five *failed* journeys by default. Click Success to display the top five successful journeys.

2. On the Top Five Journeys by Usage widget, the widget displays the *most used* journeys by default. Click Least to display the least used journeys.

## Notice

The analytics dashboard service provides key insights and trends with respect to successful or failed journey outcomes, number of users, user engagement, number of new users (sign-ons), applications, and organizations. By leveraging this functionality, Ping Identity customers can better understand their usage of the Advanced Identity Cloud. This functionality also allows Ping Identity to maintain accurate billing information with respect to such use.

All data Ping Identity collects for the purposes of providing the analytics dashboard service is anonymized using industry standard practices. The purpose is to ensure that the data does not contain any personally identifiable information, and further, so it cannot be re-identified. This includes, but is not limited to, a one-way SHA-256 hashing function that returns a hexadecimal representation of a UUID. This ensures that no personally identifiable information is used by Ping Identity, or any other third-party or system.

---

---
title: Allow cross-domain requests with CORS
description: Cross-origin resource sharing (CORS) lets user agents make cross-domain server requests. In PingOne Advanced Identity Cloud, you can configure CORS to allow browsers from trusted domains to access Advanced Identity Cloud protected resources. For example, you might want a custom web application running on your own domain to get an end-user's profile information using the Advanced Identity Cloud REST API.
component: pingoneaic
page_id: pingoneaic:tenants:cors
canonical_url: https://docs.pingidentity.com/pingoneaic/tenants/cors.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Architecture", "Integration", "Scripts", "Security", "Setup &amp; Configuration", "Tenants"]
page_aliases: ["tenants:configure-cors.adoc"]
section_ids:
  configure-cors-using-esvs: Configure CORS using ESVs
  create-a-new-cors-configuration: Create a new CORS configuration
  activate-or-deactivate-a-cors-configuration: Activate or deactivate a CORS configuration
  edit-a-cors-configuration: Edit a CORS configuration
  view-cors-configurations: View CORS configurations
---

# Allow cross-domain requests with CORS

[Cross-origin resource sharing](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS) (CORS) lets user agents make cross-domain server requests. In PingOne Advanced Identity Cloud, you can configure CORS to allow browsers from trusted domains to access Advanced Identity Cloud protected resources. For example, you might want a custom web application running on your own domain to get an end-user's profile information using the Advanced Identity Cloud REST API.

By default, CORS is configured to let the [Ping SDKs](https://docs.pingidentity.com/sdks/latest) access Advanced Identity Cloud. You can add additional CORS configurations that let other APIs or SDKs access Advanced Identity Cloud.

![cors config](_images/cors-config.png)

## Configure CORS using ESVs

1. In your development environment:

   1. Use the Advanced Identity Cloud admin console to set up one or more CORS configurations for your environment:

      * [Create a new CORS configuration](#create-a-new-cors-configuration)

      * [Edit a CORS configuration](#edit-a-cors-configuration)

      * [Activate or deactivate a CORS configuration](#activate-or-deactivate-a-cors-configuration)

      You can create as many configurations as you need. The active configurations are combined to form the entire set of rules for resource sharing in your environment.

   2. For each CORS configuration:

      * If the `acceptedOrigins` field contains hard-coded configuration, use the Advanced Identity Cloud REST API to replace the value of the `acceptedOrigins` field with an ESV array. Learn more in [Insert ESV placeholders into CORS configuration](configuration-placeholders-api.html#configure-cors).

      * If the `acceptedOrigins` field already contains an ESV array, no action is needed.

   3. Check that the CORS configuration is working as expected in your development environment.

2. In your staging environment:

   1. If you created any new ESV arrays in step 1b, create corresponding ESVs with the same names in your staging environment.

   2. Run a promotion to move the configuration change from your development environment to your staging environment. Refer to:

      * [Manage self-service promotions using the API](self-service-promotions-api.html)

      * [Manage self-service promotions using the admin console](self-service-promotions-ui.html)

   3. Check that the CORS configuration is working as expected in your staging environment.

3. In your production environment:

   1. If you created any new ESV arrays in step 1b, create corresponding ESVs with the same names in your production environment.

   2. Run a promotion to move the configuration change from your staging environment to your production environment.

   3. Check that the CORS configuration is working as expected in your production environment.

## Create a new CORS configuration

1. In your development environment, open the TENANT menu (upper right), and choose Tenant settings.

2. On the Tenant Settings page, click Global Settings > Cross-Origin Resource Sharing (CORS).

3. Click + New CORS Configuration.

4. On the New CORS Configuration dialog box, choose a configuration type.

   |           |                                                                                                                                                                                                        |
   | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
   | Ping SDKs | Choose this option when you want to work with the Ping SDKs. Advanced Identity Cloud pre-configures accepted origins, methods, and headers for you. You can modify the configuration in the next step. |
   | Custom    | Choose this option when you want to use your own SDK, APIs, or other software components.                                                                                                              |

5. Click Next.

6. In the New CORS Configuration dialog box, provide CORS details.

   |                             |                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
   | --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
   | Name                        | Enter a display name. Use only numerals, letters, and hyphens (-).                                                                                                                                                                                                                                                                                                                                                                                     |
   | Accepted Origins            | Required. Accepted origins that will be allowed to make requests to Advanced Identity Cloud from your application in a cross-origin context. Wildcards are not supported. Each value should be identical to the origin of the CORS request. Example: `https://myapp.example.com:443`                                                                                                                                                                   |
   | Accepted Methods            | Defaults are `POST` and `GET`. The set of (non-simple) accepted HTTP methods allowed when making CORS requests to Advanced Identity Cloud. Use only uppercase characters.                                                                                                                                                                                                                                                                              |
   | Accepted Headers (optional) | Accepted header names when making requests from the above specified trusted domains. Header names are case-insensitive. By default, the following simple headers are explicitly accepted: `Cache-Control`, `Content-Language`, `ExpiresLast-Modified`, `Pragma`. If you don't specify values for this element, then the presence of any header in the CORS request, other than the simple headers listed above, will cause the request to be rejected. |

7. (Optional) Click Show advanced settings to display further CORS configuration settings:

   |                            |                                                                                                                                                                                                                                                                                                                                                                                       |
   | -------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | Exposed Headers (optional) | Add the response header names that Advanced Identity Cloud returns. The header names are case-insensitive. User agents can make use of any headers that are listed in this property, as well as these simple response headers: `Cache-Control`, `Content-Language`, `Expires`, `Last-Modified`, `Pragma`, and `Content-Type`. User agents must filter out all other response headers. |
   | Enable Caching             | Max age is the maximum length of time, in seconds, that the browser is allowed to cache the pre-flight response. The value is included in pre-flight responses, in the Access-Control-Max-Age header.                                                                                                                                                                                 |
   | Allow Credentials          | Enable this property if you send Authorization headers as part of the CORS requests, or need to include information in cookies when making requests.When enabled, AM sets the Access-Control-Allow-Credentials: true header.                                                                                                                                                          |

8. Click Save CORS Configuration.

## Activate or deactivate a CORS configuration

* To activate or deactivate all CORS configurations:

  1. In your development environment, open the TENANT menu (upper right), and choose Tenant settings.

  2. On the Tenant Settings page, click Global Settings > Cross-Origin Resource Sharing (CORS).

  3. On the CORS Configurations page, in the upper right side, click Activate or Deactivate.

* To deactivate an individual CORS configuration:

  1. In your development environment, open the TENANT menu (upper right), and choose Tenant settings.

  2. On the Tenant Settings page, click Global Settings > Cross-Origin Resource Sharing (CORS).

  3. On the CORS Configurations page, find the name of the configuration you want to deactivate.

  4. Click its More ([icon: ellipsis-h, set=fa]) menu, and choose Deactivate.

## Edit a CORS configuration

1. In your development environment, open the TENANT menu (upper right), and choose Tenant settings.

2. On the Tenant Settings page, click Global Settings > Cross-Origin Resource Sharing (CORS).

3. On the CORS Configurations page, find the name of the configuration you want to edit.

4. Click its More ([icon: ellipsis-h, set=fa]) menu, and choose Edit.

## View CORS configurations

1. Open the TENANT menu (upper right), and choose Tenant settings.

2. On the Tenant Settings page, click Global Settings > Cross-Origin Resource Sharing (CORS).

---

---
title: Architecture, availability, and disaster recovery
description: Advanced Identity Cloud is built on a highly available, globally distributed architecture that ensures your identity services remain operational even in the event of failures or disruptions. This architecture provides resilience, scalability, and performance for your identity management needs in the following ways:
component: pingoneaic
page_id: pingoneaic:tenants:environments-architecture-availability-disaster-recovery
canonical_url: https://docs.pingidentity.com/pingoneaic/tenants/environments-architecture-availability-disaster-recovery.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
page_aliases: ["product-information:high-availability-disaster-recovery.adoc"]
section_ids:
  deployment-options: Deployment options
  single-region: Single region
  multi-region-high-availability: Multi-region high availability
  comparison-of-deployment-options: Comparison of deployment options
---

# Architecture, availability, and disaster recovery

Advanced Identity Cloud is built on a highly available, globally distributed architecture that ensures your identity services remain operational even in the event of failures or disruptions. This architecture provides resilience, scalability, and performance for your identity management needs in the following ways:

* **Global services**: Load balancers, configuration storage, and ESV storage are global services and remain available during the failure of a single region.

* **Redundancy and scaling**: Workloads are deployed to clusters across multiple availability zones within a region to create redundancy. In the event of physical hardware failure within a particular zone, workloads are automatically redistributed to other zones. Ping Identity monitors your environments and appropriately scales each one to meet expected demands.

* **Availability and disaster recovery**: Two deployment options are available to meet different availability and disaster recovery requirements:

  * [Single region](#single-region) (default): This deployment option hosts identity-related services in a single main region, with data backed up hourly to a separate backup region. It supports restoration to the main region or the backup region in the event of data corruption or regional failure.

  * [Multi-region high availability](#multi-region-high-availability) (add-on capability): This deployment option hosts identity-related services across both a primary and a secondary region, with data replicated in near real-time. It allows for rapid failover to the secondary region in the event of a failure in the primary region, with a significantly better recovery time objective (RTO) and recovery point objective (RPO).

  For a quick comparison of these deployment options, refer to [Comparison of deployment options](#comparison-of-deployment-options).

## Deployment options

### Single region

This deployment option is available in all environments and is the default option included with your Advanced Identity Cloud subscription.

A single-region deployment hosts identity-related services in a single main region, spread across three availability zones for resilience. Data is backed up hourly to a separate backup region. This supports three key recovery scenarios:

* **Restore from backup**: In the event of data corruption, you can restore the datastore, including user identities and the identity schema, to any point within the retention period, which is 30 days for production environments. The available restore points are determined by the hourly backup schedule. An in-region restore typically takes under 1 hour, with an RPO of under 1 hour.

* **In-region disaster recovery**: In the event of a significant service disruption or infrastructure failure within the main region, but where the region is still operational, service can be restored from backup in under 1 hour with an RPO of under 1 hour.

* **Backup region disaster recovery**: In the event of a failure in the main region, and where the region is no longer operational, service can be restored in the backup region in under 4 hours with an RPO of under 1 hour.

![Single-region deployment diagram](_images/environments-deployment-single-region.png)

### Multi-region high availability

|   |                                                                                                                                                                                                                                                                                                        |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | Advanced Identity Cloud add-on capability\[[2](#_footnotedef_2 "View footnote.")]Contact your Ping Identity representative if you want to add this feature to your PingOne Advanced Identity Cloud subscription. Learn more in [Add-on capabilities](../product-information/add-on-capabilities.html). |

This deployment option is available in your staging and production environments only and is an add-on capability to your Advanced Identity Cloud subscription. It's also dependent on the [Outbound static IP addresses](environments-outbound-static-ip-addresses.html) feature.

A multi-region deployment hosts identity-related services across both a primary and a secondary region, with data replicated between them in near real-time. This active-passive setup allows for a much faster response to failures. In the event of a failure in the primary region, service can be failed over to the secondary region in under 10 minutes with an RPO of near zero\[[1](#_footnotedef_1 "View footnote.")].

No additional configuration is required from you to support the multi-region deployment compared to the standard single-region deployment. Both regions are available using the same hostname and IP addresses for inbound and outbound traffic. However, an additional hostname is provided to let you monitor the failover services in the secondary region.

Both regions must be in the same geographic area (geo). For example, both in the United States or both in Europe. If there isn't a second region in your geo, you can choose it from another geo, as long as it's geographically nearby. For example, Sydney (in the Australia geo) and Jakarta (in the Asia geo).

![Multi-region high availability deployment diagram](_images/environments-deployment-multi-region.png)

## Comparison of deployment options

| Feature                                                                                 | Single region                                                                                                                                                                                                                                                                                                          | Multi-region high availability                                                                                                                                                                                                                                                                                                                                        |
| --------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Default deployment option?                                                              | Default                                                                                                                                                                                                                                                                                                                | Add-on capability                                                                                                                                                                                                                                                                                                                                                     |
| Available in all environments?                                                          | All environments                                                                                                                                                                                                                                                                                                       | Staging and production only                                                                                                                                                                                                                                                                                                                                           |
| SLA                                                                                     | 99.99%                                                                                                                                                                                                                                                                                                                 | 99.99%                                                                                                                                                                                                                                                                                                                                                                |
| Load balancer                                                                           | Uses global load balancer to maintain availability during the failure of a single region.                                                                                                                                                                                                                              |                                                                                                                                                                                                                                                                                                                                                                       |
| Configuration and ESV storage                                                           | Configuration storage and ESV storage are global services and remain available during the failure of a single region.                                                                                                                                                                                                  |                                                                                                                                                                                                                                                                                                                                                                       |
| Identity, relationship, and token data storage                                          | Hosted in a single main region across three availability zones.                                                                                                                                                                                                                                                        | Hosted in a primary region and a secondary region across three zones per region.                                                                                                                                                                                                                                                                                      |
| Backup of disk snapshots                                                                | Taken hourly in the main region and backed up to a backup region.                                                                                                                                                                                                                                                      | Taken hourly in both regions and backed up to the same region.                                                                                                                                                                                                                                                                                                        |
| RCS endpoint configuration for staging and production environments                      | 3 endpoints in the main region                                                                                                                                                                                                                                                                                         | 3 endpoints in the primary region, 3 endpoints in the secondary region. Learn more in [Configure a remote connector server](../identities/sync-identities.html#task-5-configure-a-remote-server).                                                                                                                                                                     |
| Replication                                                                             | N/A                                                                                                                                                                                                                                                                                                                    | Identity, relationship, and token data are replicated between the primary and secondary regions in near real-time.                                                                                                                                                                                                                                                    |
| Recovery mechanism for regional failure where the region is no longer operational       | In the event of the main region having a failure and no longer being operational, service is restored in the backup region.                                                                                                                                                                                            | In the event of the primary region having a failure and no longer being operational, service is failed over to the secondary region.                                                                                                                                                                                                                                  |
| Production RTO for regional failure with service restored to backup or secondary region | Under 4 hours                                                                                                                                                                                                                                                                                                          | Under 10 minutes\[[1](#_footnotedef_1 "View footnote.")]                                                                                                                                                                                                                                                                                                              |
| Production RPO for regional failure with service restored to backup or secondary region | Under 1 hour                                                                                                                                                                                                                                                                                                           | Near zero\[[1](#_footnotedef_1 "View footnote.")]                                                                                                                                                                                                                                                                                                                     |
| Release deferral                                                                        | If you opt in to [release deferral](../release-notes/release-deferral.html), the release upgrade schedule is determined by the 7-day deferral period. Learn more in [Upgrade scenario for a single-region deployment](../release-notes/release-deferral.html#example-upgrade-scenario-for-a-single-region-deployment). | If you opt in to [release deferral](../release-notes/release-deferral.html), the release upgrade schedule is determined by both the 7-day deferral period and an additional multi-region delay period. Learn more in [Upgrade scenario for a multi-region deployment](../release-notes/release-deferral.html#example-upgrade-scenario-for-a-multi-region-deployment). |

For a more specific breakdown of RTO and RPO targets for different recovery scenarios, refer to [Recovery time objective (RTO) and recovery point objective (RPO)](environments.html#rto-and-rpo-characteristics).

***

[1](#_footnoteref_1). Multi-region deployment RTO and RPO values refer to the GA product that will be available in H2 2026. Learn more in [What are the RTO and RPO during the limited availability phase?](environments-architecture-multi-region-faq.html#what-are-the-rto-and-rpo-during-the-limited-availability-phase)[2](#_footnoteref_2). A [sandbox environment](environments-sandbox.html) is an [add-on capability](../product-information/add-on-capabilities.html).

---

---
title: Configure a Microsoft Azure tenant for MS Graph API email client
description: Use of the MS Graph API email client requires a properly configured Microsoft Azure tenant. The steps for configuring an Azure tenant should be used as an outline, as the specific options, menus, and features may have changed.
component: pingoneaic
page_id: pingoneaic:tenants:email-provider-configure-microsoft-azure-tenant
canonical_url: https://docs.pingidentity.com/pingoneaic/tenants/email-provider-configure-microsoft-azure-tenant.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
---

# Configure a Microsoft Azure tenant for MS Graph API email client

Use of the MS Graph API email client requires a properly configured Microsoft Azure tenant. The steps for configuring an Azure tenant should be used as an outline, as the specific options, menus, and features may have changed.

Microsoft Sandbox

If you need a sandbox for *testing only*, check out the [Microsoft developer sandbox subscription](https://learn.microsoft.com/en-us/office/developer-program/microsoft-365-developer-program-get-started). Although the sandbox accepts `sendMail` requests, the Microsoft Exchange service prevents messages from being delivered. The messages do show up in the sender's "sent" box, which should be sufficient for manual testing purposes.

1. Navigate to [Azure Active Directory | App registrations](https://portal.azure.com/#view/Microsoft_AAD_IAM/ActiveDirectoryMenuBlade/~/RegisteredApps).

2. Create the Advanced Identity Cloud client application:

   1. From the menu bar, click + New Registration.

   2. On the Register an application page, enter the application Name, such as `my-email-client`.

   3. For Supported account types, select the applicable option for your organization.

   4. Click Register.

   5. On the my-email-client page, from the main Essentials area, record the Application (client) ID.

      |   |                                                                                                                                                                                   |
      | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      |   | This is the value for `clientId` in the `auth` settings of the email configuration. Learn more in [`oauth2` properties](email-provider-configuration-reference.html#oath2-table). |

3. Add a client secret:

   1. On the my-email-client page, in the main Essentials area, click Add a certificate or secret.

      > **Collapse: Show Me**
      >
      > ![Azure app - add a secret link](../_images/azureAppAddSecretLink.png)

   2. On the Certificates & secrets page, select the Client secrets tab, and click + New client secret.

      > **Collapse: Show Me**
      >
      > ![Azure app - add a new client secret](../_images/azureNewClientSecret.png)

   3. In the Add a client secret window, enter the details, and click Add.

   4. Copy the Value and Secret ID to a secure place *before* leaving the Certificates & secrets page.

      |   |                                                                                                                                                                                          |
      | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      |   | Use the secret Value for `clientSecret` in the `auth` settings of the email configuration. Learn more in [`oauth2` properties](email-provider-configuration-reference.html#oath2-table). |

4. Add API permissions:

   1. From the side menu, click API permissions.

   2. On the API permissions page, click + Add a permission.

   3. In the Request API permissions windows, select the Microsoft APIs tab, and click Microsoft Graph.

   4. In the What type of permissions…​ area, click Application permissions.

   5. In the Select permissions search bar, type `send`.

   6. Expand the Mail node, and select Mail.Send.

   7. Click Add permissions.

      > **Collapse: Show Me**
      >
      > ![Azure app - Request API permissions](../_images/azureRequestAPIPermissions.png)

---

---
title: Configure email
description: PingOne Advanced Identity Cloud provides email functionality to communicate with end users. You can send emails from journeys, scripts, backend processes, or through the REST API.
component: pingoneaic
page_id: pingoneaic:tenants:email-configure
canonical_url: https://docs.pingidentity.com/pingoneaic/tenants/email-configure.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  email-capabilities: Email capabilities
  email-use-cases: Common use cases
---

# Configure email

PingOne Advanced Identity Cloud provides email functionality to communicate with end users. You can send emails from journeys, scripts, backend processes, or through the REST API.

## Email capabilities

Advanced Identity Cloud email functionality includes:

* **Email provider configuration**: Configure email provider settings to send email through your organization's mail server or a third-party service. Learn more in [Email provider](email-provider.html).

* **Email templates**: Create reusable, localized email templates with dynamic content using Handlebars expressions. Learn more in [Email templates](email-templates.html).

* **Programmatic emails**: Send email through REST API calls or from scripts for custom workflows and backend processes. Learn more in [Send email](email-send.html).

* **Journey-based emails**: Send email by adding nodes to your journeys, such as the [Email Template node](https://docs.pingidentity.com/auth-node-ref/latest/email-template.html), [Email Suspend node](https://docs.pingidentity.com/auth-node-ref/latest/email-suspend.html) or [OTP Sender node](https://docs.pingidentity.com/auth-node-ref/latest/otp-email-sender.html).

## Common use cases

Common use cases for sending emails include:

* Send welcome emails when end users register.

* Deliver password reset notifications.

* Provide multi-factor authentication (MFA) codes.

* Send account verification messages.

* Notify end users of account changes or security events.

---

---
title: Configure placeholders to use with ESVs
description: PingOne Advanced Identity Cloud lets you reference ESVs from configuration placeholders. This lets you use different configuration values for the development, staging, and production environments at runtime.
component: pingoneaic
page_id: pingoneaic:tenants:configuration-placeholders
canonical_url: https://docs.pingidentity.com/pingoneaic/tenants/configuration-placeholders.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
page_aliases: ["tenants:esvs-configuration-placeholders.adoc"]
section_ids:
  set_up_configuration_placeholders_to_reference_an_esv: Set up configuration placeholders to reference an ESV
  update_an_esv_referenced_by_a_configuration_placeholder: Update an ESV referenced by a configuration placeholder
  restart-identity-cloud-services: Restart Advanced Identity Cloud services
  delete-esv-referenced-by-configuration-placeholder: Delete an ESV referenced by a configuration placeholder
  define-and-promote-an-esv: Define and promote an ESV
---

# Configure placeholders to use with ESVs

PingOne Advanced Identity Cloud lets you reference ESVs from configuration placeholders. This lets you use different configuration values for the development, staging, and production environments at runtime.

For example, suppose you wanted to set a different email sender for each environment. You would set the configuration value of the email sender to an ESV with different values in each environment; for example, `dev-mycompany@example.com` (development), `staging-mycompany@example.com` (staging), and `mycompany@example.com` (production). Then, you would insert the ESV configuration placeholder into your configuration instead of a literal value.

|   |                                                                                                                                                                                                   |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Configuration placeholders that reference an undefined ESV cause promotions to fail. Learn more in [Configuration integrity checks](self-service-promotions.html#configuration-integrity-checks). |

## Set up configuration placeholders to reference an ESV

1. In your development environment:

   1. Create the ESV using one of the following:

      * [Create a variable](esvs-manage-ui.html#create-variables) or [create a secret](esvs-manage-ui.html#create-secrets) using the Advanced Identity Cloud admin console.

      * [Create a variable](https://docs.pingidentity.com/pingoneaic/_attachments/api/#operation/createVariables) or [create a secret](https://docs.pingidentity.com/pingoneaic/_attachments/api/#operation/createSecret) using the API (learn more in [Manage ESVs using the API](esvs-manage-api.html)).

   2. [Restart Advanced Identity Cloud services](#restart-identity-cloud-services).

   3. Insert the ESV configuration placeholder into your configuration. Learn more in:

      * [Manage configuration placeholders using the API](configuration-placeholders-api.html)

      * [Manage configuration placeholders using the admin console](configuration-placeholders-ui.html).

2. In your staging environment:

   1. Repeat step 1a for your staging environment. Ensure the ESV name is the same as you set up in the development environment.

   2. Run a promotion to move the configuration change from your development environment to your staging environment. Learn more in:

      * [Manage self-service promotions using the API](self-service-promotions-api.html)

      * [Manage self-service promotions using the admin console](self-service-promotions-ui.html)

3. In your production environment:

   1. Repeat step 1a for your production environment. Ensure the ESV name is the same as you set up in the development environment.

   2. Run a further promotion to move the configuration change from your staging environment to your production environment.

If you want to add more ESVs later, repeat the steps above and use a further series of promotions.

|   |                                                                                                                                                                                                                                                                |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Configuration placeholders can only be inserted into static configuration. You can find more information on what static configuration is and which areas of configuration are classified as static in the [promotion FAQs](self-service-promotions-faqs.html). |

## Update an ESV referenced by a configuration placeholder

1. Update the ESV using one of the following:

   * [Update a variable](https://docs.pingidentity.com/pingoneaic/_attachments/api/#operation/createVariables) or [add a new secret version](https://docs.pingidentity.com/pingoneaic/_attachments/api/#operation/createSecretVersion) to a secret using the API (learn more in [Manage ESVs using the API](esvs-manage-api.html)).

   * [Update a variable](esvs-manage-ui.html#update-variables) or [add a new secret version](esvs-manage-ui.html#update-secrets) to a secret using the Advanced Identity Cloud admin console.

2. Next, [Restart Advanced Identity Cloud services](#restart-identity-cloud-services).

## Restart Advanced Identity Cloud services

If you update an ESV referenced by a configuration placeholder, you also need to restart Advanced Identity Cloud services. This substitutes the updated secret or variable into the corresponding configuration placeholder.

1. Restart Advanced Identity Cloud services using one of the following:

   * [Restart](https://docs.pingidentity.com/pingoneaic/_attachments/api/#tag/Restart) using the API (learn more in [Manage ESVs using the API](esvs-manage-api.html)).

   * [Apply updates](esvs-manage-ui.html#apply-updates) using the Advanced Identity Cloud admin console.

## Delete an ESV referenced by a configuration placeholder

1. Remove the ESV configuration placeholder from your configuration in the development environment. Refer to:

   * [Manage configuration placeholders using the API](configuration-placeholders-api.html).

   * [Manage configuration placeholders using the admin console](configuration-placeholders-ui.html).

2. Run a promotion to move the configuration change from the development environment to the staging environment. Refer to:

   * [Manage self-service promotions using the API](self-service-promotions-api.html)

   * [Manage self-service promotions using the admin console](self-service-promotions-ui.html)

3. Run a further promotion to move the configuration change from the staging environment to the production environment.

4. Delete the ESV in each of the development, staging, and production environments using one of the following:

   * [Delete a variable](https://docs.pingidentity.com/pingoneaic/_attachments/api/#operation/deleteVariable) or [delete a secret](https://docs.pingidentity.com/pingoneaic/_attachments/api/#operation/deleteSecret) using the Advanced Identity Cloud API (learn more in [Manage ESVs using the API](esvs-manage-api.html)).

   * [Delete a variable](esvs-manage-ui.html#delete-variables) or [delete a secret](esvs-manage-ui.html#delete-secrets) using the Advanced Identity Cloud admin console.

## Define and promote an ESV

An example of using a variable would be to define a URL that a user is redirected to after logging in. In each environment, the URL would need a different value; for example, `dev-www.example.com` (development), `staging-www.example.com` (staging), and `www.example.com` (production).

To define and promote the variable:

1. Decide on a variable name; for example, `esv-myurl`. Learn more in [ESV naming](esvs.html#esv-naming).

2. Set an ESV variable in each of the development, staging, and production environments. To do this, choose one of the following options:

   * Use the Advanced Identity Cloud admin console to [create the variable](esvs-manage-ui.html#create-variables), then [apply the update](esvs-manage-ui.html#apply-updates).

   * Use the [variables](https://docs.pingidentity.com/pingoneaic/_attachments/api/#tag/Variables) API endpoint to create the variable, then use the [restart](https://docs.pingidentity.com/pingoneaic/_attachments/api/#tag/Restart) API endpoint to restart Identity Cloud services.

3. Insert the ESV configuration placeholder into your configuration in the development environment. For the example variable `esv-myurl` from step 1, the placeholder would be called `&{esv.myurl}`. Refer to:

   * [Manage configuration placeholders using the API](configuration-placeholders-api.html).

   * [Manage configuration placeholders using the admin console](configuration-placeholders-ui.html).

   |   |                                                                                                                                               |
   | - | --------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | Configuration placeholders can only be inserted into static configuration. Learn more in [promotion FAQs](self-service-promotions-faqs.html). |

4. Run a promotion to move the configuration change from the development environment to the staging environment. Refer to:

   * [Manage self-service promotions using the API](self-service-promotions-api.html)

   * [Manage self-service promotions using the admin console](self-service-promotions-ui.html)

5. Run a promotion to move the configuration change from the staging environment to the production environment.

The following illustration demonstrates the process:

![image$esv set variable](_images/esv-set-variable.png)

---

---
title: Configure Secure Connect with Equinix
description: You can find background information on Secure Connect in PingOne Advanced Identity Cloud in Create private network connections with Secure Connect.
component: pingoneaic
page_id: pingoneaic:tenants:secure-connect-configure-equinix
canonical_url: https://docs.pingidentity.com/pingoneaic/tenants/secure-connect-configure-equinix.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
page_aliases: ["tenants:private-network-connections-configure-equinix.adoc"]
section_ids:
  provide-requirements-for-equinix-interconnect-service: "Task 1: Provide requirements for Equinix Interconnect service"
  enable-equinix-interconnect-service: "Task 2: Enable Equinix Interconnect service"
  send-internal-certificates: "Task 3: (Optional) Configure support for services in your internal network"
---

# Configure Secure Connect with Equinix

You can find background information on Secure Connect in PingOne Advanced Identity Cloud in [Create private network connections with Secure Connect](secure-connect.html).

To configure Secure Connect with Equinix, you must complete the following tasks. Each task requires you to coordinate with Ping Identity support using a support case:

* [Task 1: Provide requirements for Equinix Interconnect service](#provide-requirements-for-equinix-interconnect-service)

* [Task 2: Enable Equinix Interconnect service](#enable-equinix-interconnect-service)

* [Task 3: (Optional) Configure support for services in your internal network](#send-internal-certificates)

|   |                                                                                                                                                                                                                                                          |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | - The minimum lead time for a provisioning request is two weeks.

- During the provisioning process, there will be approximately one hour of downtime for your environments. Ping Identity support will work with you on timeframes in the support case. |

## Task 1: Provide requirements for Equinix Interconnect service

In this task, you provide Ping Identity support with your requirements for the Equinix Interconnect service, including details of your network configuration and your Advanced Identity Cloud tenant environments.

1. Send Ping Identity support your requirements for an Interconnect service:

   1. Go to <https://support.pingidentity.com>.

   2. Click Create a case.

   3. Follow the steps in the case submission wizard by selecting your account and contract and answering questions about your tenant environments.

   4. On the Please answer the following questions to help us understand the issue you're facing page, enter the following details, and then click Next:

      | Field                                                | Value                                                                       |
      | ---------------------------------------------------- | --------------------------------------------------------------------------- |
      | What product family is experiencing the issue?       | Select PingOne Advanced Identity Cloud                                      |
      | What specific product is experiencing the issue?     | Select Configuration                                                        |
      | What version of the product are you using?           | Select NA                                                                   |
      | What Hostname(s) or Tenant ID(s) does this apply to? | Enter a comma-separated list of FQDNs for the relevant tenant environments. |

   5. On the Tell us about the issue page, enter the following details, and then click Next:

      | Field                                      | Value                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
      | ------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      | Provide a descriptive title for your issue | Enter `Requirements for Equinix Interconnect service`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
      | Describe the issue below                   | Enter the following details:- An ASN (Autonomous System Number) value for your private network router.

      - An MTU (Maximum Transmission Unit) value for the Interconnect connection.

      - Development environment information:

        * A CIDR block for the development environment. The CIDR prefix must be `/27` or numerically smaller. Learn more in [How do I choose CIDR blocks for my tenant environments?](secure-connect.html#how-do-i-choose-cidr-blocks-for-my-tenant-environments)

        * IP addresses or domain names for testing the development environment.

      - UAT\[[1](#_footnotedef_1 "View footnote.")] environment information:

        * CIDR blocks for any UAT environments. Each environment's CIDR prefix must be `/27` or numerically smaller.

        * IP addresses or domain names for testing any UAT environments.

      - Staging environment information:

        * A CIDR block for the staging environment. The CIDR prefix must be `/27` or numerically smaller.

        * IP addresses or domain names for testing the staging environment.

      - Production environment information:

        * A CIDR block for the production environment. The CIDR prefix must be `/27` or numerically smaller.

        * IP addresses or domain names for testing the production environment.

      - Your use case for this implementation.

      - Your preferred date/time for enabling the Interconnect connection. |

   6. Click Submit.

2. Ping Identity support works with you in the support case to agree a suitable date and time window for the enablement process.

3. Wait until the start of the enablement process window (agreed in the previous step) before moving to the next task.

## Task 2: Enable Equinix Interconnect service

In this task, you'll work with Ping Identity support to enable the Equinix Interconnect service.

1. Create a support case to request Google Cloud pairing keys from Ping Identity support:

   1. Go to <https://support.pingidentity.com>.

   2. Click Create a case.

   3. Follow the steps in the case submission wizard by selecting your account and contract and answering questions about your tenant environments.

   4. On the Please answer the following questions to help us understand the issue you're facing page, enter the following details, and then click Next:

      | Field                                                | Value                                                                       |
      | ---------------------------------------------------- | --------------------------------------------------------------------------- |
      | What product family is experiencing the issue?       | Select PingOne Advanced Identity Cloud                                      |
      | What specific product is experiencing the issue?     | Select Configuration                                                        |
      | What version of the product are you using?           | Select NA                                                                   |
      | What Hostname(s) or Tenant ID(s) does this apply to? | Enter a comma-separated list of FQDNs for the relevant tenant environments. |

   5. On the Tell us about the issue page, enter the following details, and then click Next:

      | Field                                      | Value                                       |
      | ------------------------------------------ | ------------------------------------------- |
      | Provide a descriptive title for your issue | Enter `Enable Equinix Interconnect service` |
      | Describe the issue below                   | Enter `Enable Equinix Interconnect service` |

   6. Click Submit to create the support case.

2. Monitor the support case while Ping Identity support performs these actions:

   1. Provides you with Google Cloud pairing keys for the appropriate region and availability zone.

   2. Provides you with static IP addresses for all Secure Connect environments.

   3. Works with you to agree on suitable dates and times for the provisioning process window.

3. Set up the Equinix Interconnect service in the Equinix Fabric portal:

   1. Open the [Equinix instructions for setting up Google Cloud Interconnect](https://docs.equinix.com/en-us/Content/Interconnection/Fabric/connections/Fabric-connect-google.htm) in your browser.

   2. Follow the steps under the heading Create Connection in the Equinix Fabric Portal, using the Google Cloud pairing keys provided in step 2a.

4. Update the support case to let Ping Identity support know you've completed the instructions in step 3.

5. Monitor the support case while Ping Identity support performs these actions:

   1. Activates a BGP configuration in GCP.

   2. Provides you with pairing keys and BGP IP addresses for all tenant environments to support Secure Connect. The number of pairing keys is dependent on the [level of availability](secure-connect.html#availability) you require.

6. In the Equinix portal, use the pairing keys to create direct connections to the BGP IP addresses, using the BGP ASN of 16550. Ping Identity accepts the connections.

7. Wait until the start of the provisioning process window (agreed in step 2c).

8. When the provisioning process window starts, monitor the support case while Ping Identity support performs these actions:

   1. Establishes BGP sessions.

   2. Validates the routes advertised by each party. The routes Ping Identity advertises with BGP are as follows:

      * The chosen CIDR block for the tenant environment.

      * 35.199.192.0/19 (Google Cloud DNS)

   3. Tests bidirectional network connectivity.

   4. Provides nodes in each tenant environment that should respond to queries from the private network.

   |   |                                                                                                                                                                                                 |
   | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | Ping Identity allows all traffic from the advertised subnets using BGP. You're responsible for configuring your firewall in your private network to allow traffic from Advanced Identity Cloud. |

## Task 3: (Optional) Configure support for services in your internal network

To support services in your internal network (for example, SMTP), Ping Identity can optionally perform the following actions:

* Create DNS forwarding zones. For assistance with this, create a support case in the [Ping Identity Support Portal](https://support.pingidentity.com).

* Add your internal certificate or CA into the trust store of your tenant environments. For assistance with this, refer to [Send Ping Identity a CA or TLS certificate](../realms/server-certificates.html#send-ping-a-ca-or-tls-certificate).

***

[1](#_footnoteref_1). A [user acceptance testing (UAT) environment](environments-uat.html) is an [add-on capability](../product-information/add-on-capabilities.html).

---

---
title: Create private network connections with Secure Connect
description: Contact your Ping Identity representative if you want to add Secure Connect to your PingOne Advanced Identity Cloud subscription. Learn more in Add-on capabilities.
component: pingoneaic
page_id: pingoneaic:tenants:secure-connect
canonical_url: https://docs.pingidentity.com/pingoneaic/tenants/secure-connect.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
page_aliases: ["tenants:private-network-connections.adoc"]
section_ids:
  use-cases: Use cases
  supported-services: Supported services
  configure-dns: Configure DNS
  faqs: FAQs
  can-i-still-access-identity-cloud-api-endpoints-over-the-public-internet: Can I still access Advanced Identity Cloud API endpoints over the public internet?
  can-i-still-access-the-identity-cloud-admin-console-over-the-public-internet: Can I still access the Advanced Identity Cloud admin console over the public internet?
  how-do-i-communicate-securely-with-my-tenant-environments: How do I communicate securely with my tenant environments?
  how-do-i-communicate-securely-to-my-private-network: How do I communicate securely to my private network?
  can-i-connect-google-cloud-to-another-cloud-provider-for-example-aws: Can I connect Google Cloud to another cloud provider? For example, AWS?
  how-do-i-choose-cidr-blocks-for-my-tenant-environments: How do I choose CIDR blocks for my tenant environments?
  google-cloud-interconnect: Google Cloud Interconnect
  availability: Availability
  partner-interconnect-service-providers: Partner Interconnect service providers
  equinix-fabric: Equinix Fabric
---

# Create private network connections with Secure Connect

|   |                                                                                                                                                                                                                                                                                                                                                                                                        |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | Advanced Identity Cloud add-on capabilityContact your Ping Identity representative if you want to add Secure Connect to your PingOne Advanced Identity Cloud subscription. Learn more in [Add-on capabilities](../product-information/add-on-capabilities.html).Secure Connect is currently also a [limited availability](../product-information/release-lifecycle.html#limited-availability) feature. |

You can use Secure Connect to provide dedicated, direct, and secure communication between your PingOne Advanced Identity Cloud network and your private network, such as an on-premises data center or IaaS provider. Secure Connect bypasses the public internet, improving latency, throughput, and security.

![secure connect network](_images/secure-connect-network.png)

Secure Connect is only available in development, UAT\[[1](#_footnotedef_1 "View footnote.")], staging, and production environments; it is not available in a sandbox\[[2](#_footnotedef_2 "View footnote.")] environment.

## Use cases

The following are examples of how you might use Secure Connect:

* Call an API endpoint in your private network from a journey script or journey authentication node in Advanced Identity Cloud.

* Send Advanced Identity Cloud emails from an internal MX/SMTP server not exposed to the public internet.

* Resolve an internal DNS name using a private DNS server; for example, an internal DNS name using the `.company` domain extension.

* Access PII/classified data which cannot be sent over public internet.

## Supported services

Ping Identity supports the following services using Secure Connect:

* DNS for internal domain names (53/udp)

* HTTP outbound (Advanced Identity Cloud → private network service) (80/tcp & 8080/tcp)

* HTTPS outbound (Advanced Identity Cloud → private network service) (443/tcp)

* HTTPS inbound (private network service → Advanced Identity Cloud) (443/tcp)

* SMTP outbound (Advanced Identity Cloud → private network service) (25/tcp)

* SMTPS outbound (Advanced Identity Cloud → private network service) (587/tcp)

This list represents the use cases Ping Identity explicitly tests against; however, you may test and use additional services to support your own private network use cases.

## Configure DNS

To support Secure Connect, configure your company's DNS to avoid collisions. Collisions can occur when the same IP address is allocated to resources inside different private networks and one or both private networks advertise the address publicly. This can cause traffic destined for one network to be incorrectly routed to the other network.

To avoid collisions, separate your company's DNS configuration into public and private zones. The private zone can advertise resources reachable using public and private addresses, but the public zone should only advertise resources reachable using public addresses and should not advertise private addresses.

Learn more in [RFC 1918](https://datatracker.ietf.org/doc/html/rfc1918).

## FAQs

### Can I still access Advanced Identity Cloud API endpoints over the public internet?

Yes, Advanced Identity Cloud API endpoints are still available over the public internet; however, Secure Connect also exposes the same API endpoints privately to let you communicate between your private network and Advanced Identity Cloud:

* Communicate inbound by calling API endpoints in your Advanced Identity Cloud tenant environments from your private network.

* Communicate outbound by calling API endpoints in your private network from your Advanced Identity Cloud tenant environments.

### Can I still access the Advanced Identity Cloud admin console over the public internet?

Yes, the Advanced Identity Cloud admin console is still available over the public internet and cannot be made private.

### How do I communicate securely with my tenant environments?

When you provision Secure Connect, you provide Ping Identity with CIDR ranges for each tenant environment. Ping Identity uses your CIDR ranges to create an internal endpoint for each Advanced Identity Cloud tenant environment. You then create private DNS records for these Advanced Identity Cloud endpoints and then create a [self-managed certificate](../realms/server-certificates.html#self-managed-certificates).

### How do I communicate securely to my private network?

For services like SMTP, Ping Identity can add your CA certificate into the trust store of your tenant environments. For assistance with this, learn more in [Send Ping Identity a CA or TLS certificate](../realms/server-certificates.html#send-ping-a-ca-or-tls-certificate).

### Can I connect Google Cloud to another cloud provider? For example, AWS?

Yes, you can connect Google Cloud to another cloud provider. In the example of AWS, you separately implement AWS Direct Connect, then set up virtual routing in your private network between Google Cloud and AWS. Learn more in [Partner Interconnect with multi-cloud enabled partners](https://cloud.google.com/architecture/patterns-for-connecting-other-csps-with-gcp#partner_interconnect_with_multi-cloud_enabled_partners).

### How do I choose CIDR blocks for my tenant environments?

Choose CIDR blocks for your tenant environments that allow sufficient IP addresses for the number of users and services you expect to connect to each environment from your private network.

The following table provides guidance on the number of IP addresses available for different CIDR blocks. The lower the numeric value of the CIDR block, the more IP addresses are available.

| CIDR block | Number of IP addresses | Guidance                                                                                                                                                |
| ---------- | ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `/27`      | 32                     | Suitable for up to 30 users and services. This CIDR block represents the minimum number of IP addresses you can choose when configuring Secure Connect. |
| `/26`      | 64                     | Suitable for up to 62 users and services.                                                                                                               |
| `/25`      | 128                    | Suitable for up to 126 users and services.                                                                                                              |
| `/24`      | 256                    | Suitable for up to 254 users and services.                                                                                                              |
| `/23`      | 512                    | Suitable for up to 510 users and services.                                                                                                              |
| `/22`      | 1,024                  | Suitable for up to 1,022 users and services.                                                                                                            |
| `/21`      | 2,048                  | Suitable for up to 2,046 users and services.                                                                                                            |
| `/20`      | 4,096                  | Suitable for up to 4,094 users and services.                                                                                                            |

## Google Cloud Interconnect

Secure Connect uses Google [Cloud Interconnect](https://cloud.google.com/network-connectivity/docs/interconnect/concepts/overview) to implement private network connections between your Advanced Identity Cloud tenant environments and your private network:

* The [Partner Interconnect](https://cloud.google.com/network-connectivity/docs/interconnect/concepts/partner-overview) option is supported for one service provider ([Equinix Fabric](#equinix-fabric)).

* The [Dedicated Interconnect](https://cloud.google.com/network-connectivity/docs/interconnect/concepts/dedicated-overview) option is not supported.

To implement this, Ping Identity creates VLAN attachments that are associated with a [cloud router](https://cloud.google.com/network-connectivity/docs/router/concepts/overview) in your Advanced Identity Cloud network. The cloud router creates a [BGP session](https://cloud.google.com/network-connectivity/docs/router/how-to/configuring-bgp) for the VLAN attachments and your corresponding private network router. The cloud router receives the routes your private network router advertises. These routes are added as custom dynamic routes in your Advanced Identity Cloud network. The cloud router also advertises routes for your tenant environments, using CIDR blocks you specify during provisioning.

### Availability

You can configure Google Cloud Interconnect to support [three-nines availability](https://cloud.google.com/network-connectivity/docs/interconnect/tutorials/partner-creating-999-availability) or [four-nines availability](https://cloud.google.com/network-connectivity/docs/interconnect/tutorials/partner-creating-9999-availability). The following table summarizes the different approaches:

| Availability        | Guidance                                                                        | Requirements                                                                                                                                                                                                                                                              |
| ------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Three-nines (99.9%) | Recommended only for non-critical applications where downtime can be tolerated. | At least two Interconnect connections. The connections must be located in the same metropolitan area, but in different edge availability domains (metropolitan availability zones).                                                                                       |
| Four-nines (99.99%) | Recommended for most production applications.                                   | At least four Interconnect connections, two connections in one metropolitan area and two connections in another. Interconnect connections that are in the same metropolitan area must be placed in different edge availability domains (metropolitan availability zones). |

### Partner Interconnect service providers

#### Equinix Fabric

Secure Connect uses the Partner Interconnect service for [Equinix Fabric](https://docs.equinix.com/en-us/Content/Interconnection/Fabric/Fabric-landing-main.htm) to provide private network connections between your Advanced Identity Cloud tenant environments and an Equinix private network.

To set up Partner Interconnect and Equinix in Advanced Identity Cloud, learn more in [Configure Secure Connect with Equinix](secure-connect-configure-equinix.html).

***

[1](#_footnoteref_1). A [user acceptance testing (UAT) environment](environments-uat.html) is an [add-on capability](../product-information/add-on-capabilities.html).[2](#_footnoteref_2). A [sandbox environment](environments-sandbox.html) is an [add-on capability](../product-information/add-on-capabilities.html).

---

---
title: Data residency
description: When you sign up for PingOne Advanced Identity Cloud, you specify the region where you want your data to reside. This is key in helping you meet data residency compliance requirements while letting you place data as close to your users as possible.
component: pingoneaic
page_id: pingoneaic:tenants:environments-data-residency
canonical_url: https://docs.pingidentity.com/pingoneaic/tenants/environments-data-residency.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Tenants", "Region"]
page_aliases: ["tenants:data-regions.adoc", "product-information:data-regions.adoc", "pingoneaic::environments/data-regions.adoc"]
section_ids:
  regions: Regions
  canada: Canada
  united-states: United States
  brazil: Brazil
  europe: Europe
  middle-east: Middle East
  asia: Asia
  australia: Australia
---

# Data residency

When you sign up for PingOne Advanced Identity Cloud, you specify the region where you want your data to reside. This is key in helping you meet data residency compliance requirements while letting you place data as close to your users as possible.

Advanced Identity Cloud uses [pre-configured ranges of IP addresses](https://www.gstatic.com/ipranges/cloud.json) in Google Cloud Platform (GCP) regions. The IP addresses are not exclusive to Ping Identity.

## Regions

The tables in this section show all the region abbreviations for the data regions that Advanced Identity Cloud uses. The region abbreviations are used in the naming convention of your [tenant environment FQDNs](environments.html#tenant-environment-fqdns).

The tables also indicate secondary backup regions when available.

### Canada

| Region                             | Abbreviation | Backup region                     |
| ---------------------------------- | ------------ | --------------------------------- |
| Montréal (northamerica-northeast1) | nane1        | A different region within Canada. |

### United States

| Region                    | Abbreviation | Backup region                                |
| ------------------------- | ------------ | -------------------------------------------- |
| Oregon (us-west1)         | usw1         | A different region within the United States. |
| Los Angeles (us-west2)    | usw2         | A different region within the United States. |
| Iowa (us-central1)        | usc1         | A different region within the United States. |
| South Carolina (us-east1) | use1         | A different region within the United States. |
| North Virginia (us-east4) | use4         | A different region within the United States. |

### Brazil

| Region                         | Abbreviation | Backup region                                                                                     |
| ------------------------------ | ------------ | ------------------------------------------------------------------------------------------------- |
| São Paulo (southamerica-east1) | sae1         | Regional selection is available. For more information, contact your Ping Identity representative. |

### Europe

| Region                     | Abbreviation | Backup region                     |
| -------------------------- | ------------ | --------------------------------- |
| Finland (europe-north1)    | en1          | A different region within Europe. |
| Belgium (europe-west1)     | ew1          | A different region within Europe. |
| London (europe-west2)      | ew2          | A different region within Europe. |
| Frankfurt (europe-west3)   | ew3          | A different region within Europe. |
| Netherlands (europe-west4) | ew4          | A different region within Europe. |
| Zurich (europe-west6)      | ew6          | A different region within Europe. |
| Paris (europe-west9)       | ew9          | A different region within Europe. |

### Middle East

| Region               | Abbreviation | Backup region                                                                                     |
| -------------------- | ------------ | ------------------------------------------------------------------------------------------------- |
| Doha (me-central1)   | mec1         | Regional selection is available. For more information, contact your Ping Identity representative. |
| Dammam (me-central2) | mec2         | Regional selection is available. For more information, contact your Ping Identity representative. |

### Asia

| Region                      | Abbreviation | Backup region                                                                                     |
| --------------------------- | ------------ | ------------------------------------------------------------------------------------------------- |
| Singapore (asia-southeast1) | ase1         | Regional selection is available. For more information, contact your Ping Identity representative. |
| Jakarta (asia-southeast2)   | ase2         | Regional selection is available. For more information, contact your Ping Identity representative. |
| Hong Kong (asia-east2)      | ae2          | Regional selection is available. For more information, contact your Ping Identity representative. |

### Australia

| Region                        | Abbreviation | Backup region                        |
| ----------------------------- | ------------ | ------------------------------------ |
| Sydney (australia-southeast1) | ausse1       | A different region within Australia. |

---

---
title: Development, staging, and production tenant environments
description: Each PingOne Advanced Identity Cloud account includes a development, a staging, and a production tenant environment. These three environments let you build, test, and deploy your IAM applications:
component: pingoneaic
page_id: pingoneaic:tenants:environments-development-staging-production
canonical_url: https://docs.pingidentity.com/pingoneaic/tenants/environments-development-staging-production.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["ESV", "Promotion", "Tenants", "Migration"]
page_aliases: ["pingoneaic::concepts-tenant-environments.adoc", "pingoneaic::environments/tenant-environments.adoc"]
section_ids:
  manage-configuration: Manage configuration
  promote-static-configuration: Promote static configuration
---

# Development, staging, and production tenant environments

Each PingOne Advanced Identity Cloud account includes a development, a staging, and a production tenant environment. These three environments let you build, test, and deploy your IAM applications:

| Tenant Environment | Description                                                                                                                                                                                                                                                                                                                                                                                       |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Development        | Used for building and adding new features.&#xA;&#xA;The number of identity objects in a development environment is limited to 10,000.&#xA;&#xA;The 10,000 limit applies to the total sum of all identity object types combined, including applications, assignments, custom identity objects, groups, OAuth 2.0 clients, organizations, relationships, roles, SAML entities, policies, and users. |
| Staging            | Used for testing development changes, including stress tests and scalability tests with realistic deployment settings.                                                                                                                                                                                                                                                                            |
| Production         | Used for deploying applications into operation for end users.                                                                                                                                                                                                                                                                                                                                     |

## Manage configuration

Advanced Identity Cloud has two types of configuration, dynamic and static. Learn more about the difference between them in [What kind of configuration changes can my company make?](self-service-promotions-faqs.html#what-kind-of-configuration-changes-can-my-company-make).

You can change dynamic configuration in any environment, but you can only change static configuration in your development environment. Advanced Identity Cloud therefore uses a *promotion* model to move static configuration changes through the three environments.

### Promote static configuration

The development environment is *mutable*. This means that you can make static configuration changes to the environment through one of the [admin UIs](../getting-started/getting-started-explore-platform.html) or through the [REST API](../developer-docs/postman-collection.html).

The staging and production environments are not mutable. This means that you cannot make static configuration changes to these environments directly. Instead, you must move the changes from the development environment to the staging environment by [running a promotion](self-service-promotions.html), then move the changes from the staging environment to the production environment by running a further promotion.

In situations where you want a static configuration value (such as an authentication token) to be distinct in each environment, you can set the value as an [ESV](esvs.html) in each environment, then insert the ESV [placeholder](configuration-placeholders.html) into your configuration, then move the configuration to your staging and production environments by running sequential promotions. Learn more in [Configure placeholders to use with ESVs](configuration-placeholders.html).

| Tenant environment | Mutable                  | Make static configuration changes                                                                                                                 |
| ------------------ | ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| Development        | [icon: check, set=fa]Yes | Use [admin UIs](../getting-started/getting-started-explore-platform.html) or [REST API](../developer-docs/authenticate-to-rest-api-overview.html) |
| Staging            | [icon: times, set=fa]No  | [Promote configuration](self-service-promotions.html)                                                                                             |
| Production         | [icon: times, set=fa]No  | [Promote configuration](self-service-promotions.html)                                                                                             |

---

---
title: Email provider
description: PingOne Advanced Identity Cloud uses email provider configuration to support email-dependent end-user journeys. For example, registration and password reset end-user journeys usually include an email component.
component: pingoneaic
page_id: pingoneaic:tenants:email-provider
canonical_url: https://docs.pingidentity.com/pingoneaic/tenants/email-provider.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Features", "Journeys", "REST API", "Setup &amp; Configuration", "Tenants", "Users"]
page_aliases: ["pingoneaic::email-overview.adoc", "tenants:email-service.adoc", "release-notes:rapid-channel/msgraph-email-rapid.adoc", "release-notes:rapid-channel/international-email.adoc"]
section_ids:
  built-in-smtp-server: Built-in SMTP server
  external-email-services: External email services
  international-email: International email addresses
  configure-an-email-provider-across-your-tenant-environments: Configure an email provider across your tenant environments
  configure-a-mutable-environment-to-use-an-email-provider: Configure a mutable environment to use an email provider
  configure-email-ui: Using the admin console
  configure-email-REST: Using the API
  sample-email-configuration: Sample email configuration
  revert-the-email-provider-to-use-the-built-in-smtp-server: Revert the email provider to use the built-in SMTP server
---

# Email provider

PingOne Advanced Identity Cloud uses *email provider* configuration to support email-dependent end-user [journeys](../journeys/journeys.html). For example, [registration](../journeys/journeys.html#registration) and [password reset](../journeys/journeys.html#reset-password) end-user journeys usually include an email component.

By default, Advanced Identity Cloud configures the email provider with default values to connect to a built-in SMTP server. At the start of your onboarding process, this lets you quickly create and test email-dependent journeys using the ready-to-use [email templates](email-templates.html).

During your onboarding process, you need to update the email provider configuration to use your own [external email service](#external-email-services) in order to provide robust email delivery to your end users.

Email provider configuration changes made in one realm are applied to both realms.

## Built-in SMTP server

The built-in SMTP server is preconfigured in Advanced Identity Cloud and enabled by default in your tenant development and sandbox\[[1](#_footnotedef_1 "View footnote.")] environments.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The built-in SMTP server is for testing purposes only and has the following limitations:- Outbound email is rate-limited to 10 messages per minute.

- All emails are sent from a standard address in the format `noreply@<tenant-fqdn>`, which overrides any sender address set in email templates or API calls. It provides consistent delivery and helps ensure messages are sent securely.

- It doesn't support OTP Email Sender nodes in password journeys.

- It doesn't support non-ASCII characters in email addresses.In your staging, UAT\[[2](#_footnotedef_2 "View footnote.")], and production tenant environments, you *must* update the email provider configuration to use your own external email provider. |

## External email services

Advanced Identity Cloud supports two external email service types:

* SMTP

  * Send emails through your own SMTP server or a third-party email service such as Amazon SES.

  * Can only be configured in mutable environments:

    * Use the admin console or API to set literal values for testing.

    * Use the API to set ESV placeholders to make the configuration compatible with promotion.

  * Use this configuration type for sending email to [international email addresses](#international-email).

* MS Graph API

  * Send emails using the [MS Graph API `sendMail`](https://learn.microsoft.com/en-us/graph/api/user-sendmail) endpoint.

  * Can only be configured in mutable environments:

    * Not configurable using the admin console.

    * Use the API to set literal values for testing or set ESV placeholders to make the configuration compatible with promotion.

## International email addresses

To use [international email addresses](https://en.wikipedia.org/wiki/International_email), you must:

* Use SMTP as the provider type.

* The SMTP provider must support international email addresses.

* Configure `mail.mime.allowutf8=true` using the [REST API](#configure-email-REST) or the [UI](#configure-email-ui). Learn more in [`smtpProperties` sub-properties](email-provider-configuration-reference.html#smtp-sub-prop-table).

## Configure an email provider across your tenant environments

The high-level process to set up an email provider across your tenant environments is as follows:

1. In your development environment:

   1. [Create and test a journey](../journeys/journeys.html) that uses an email node. By default, the email provider uses the built-in SMTP server to test the email node.

   2. When you're satisfied with your test results:

      1. Configure the email provider configuration to use an SMTP or MS Graph API external email service. Use the instructions in [Configure a mutable environment to use an email provider](#configure-a-mutable-environment-to-use-an-email-provider).

      2. Verify that your email templates work with the external email service.

   3. When you're satisfied that your external email provider is working correctly:

      1. [Insert ESV placeholders into the email provider configuration](configuration-placeholders-api.html#configure-tenant-email-provider) to make it compatible with the promotion process.

      2. [Restart Advanced Identity Cloud services](configuration-placeholders.html#restart-identity-cloud-services).

      3. Verify that your email templates work with the updated ESV configuration.

2. Determine the promotion order of your tenant environments. This will depend on whether you have a [standard promotion group of environments](self-service-promotions.html#standard-promotion-group-of-environments) or whether you also have [additional UAT environments](self-service-promotions.html#additional-uat-environments).

3. In promotion order, for each of the tenant environments in your promotion group, perform the following steps:

   1. Create the same ESVs in the tenant environment as you created in step 1c. Ensure the ESV values are correct for the tenant environment.

   2. Run a promotion to move the configuration changes to the tenant environment from its respective lower tenant environment. Learn more in:

      * [Manage self-service promotions using the admin console](self-service-promotions-ui.html)

      * [Manage self-service promotions using the API](self-service-promotions-api.html)

4. (Optional) If you have sandbox\[[1](#_footnotedef_1 "View footnote.")] environments, repeat steps 1b and 1c for each sandbox environment.

### Configure a mutable environment to use an email provider

In your development or sandbox\[[1](#_footnotedef_1 "View footnote.")] tenant environments, configure the email provider to use your own [external email service](#external-email-services):

* For SMTP, you can use the admin console or API.

* For MS Graph API, you can only use the API.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | - To understand how the instructions in this section fit into the process of configuring the email provider across your tenant environments, refer to step 1b in the [high-level process](#configure-an-email-provider-across-your-tenant-environments).

- For the complete list of API configuration options, learn more in [Email provider configuration reference](email-provider-configuration-reference.html).

- For sample API email configurations, learn more in [Sample email configuration](#sample-email-configuration).

- For instructions on configuring a Microsoft Azure tenant, learn more in [Configure a Microsoft Azure tenant for MS Graph API email client](email-provider-configure-microsoft-azure-tenant.html). |

#### Using the admin console

1. In the Advanced Identity Cloud admin console, go to Email > Provider.

2. On the Email Provider page, enable Use my own email provider.

3. Enter details in the following fields:

   |              |                                                                                                                                                                          |
   | ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
   | From Address | Email address of the organization or individual sending the email.Example: `mycompany@example.com`.                                                                      |
   | From Name    | Name of sending organization.                                                                                                                                            |
   | Host         | Hostname or IP address of your SMTP server.                                                                                                                              |
   | Port         | Port number of your SMTP server.Many SMTP servers require the use of a secure port such as 465 or 587. Many ISPs flag email from port 25 as spam.Default value is `587`. |
   | Username     | Username for your SMTP server account.                                                                                                                                   |
   | Password     | Password for your SMTP server account.                                                                                                                                   |

4. Click Show advanced settings, and edit the options and fields:

   |                                |                                                                                                                                                                                                                                                                                                 |
   | ------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | Socket Connection Timeout (ms) | Elapsed time before Advanced Identity Cloud times out due to unsuccessful socket connection to the SMTP server. A setting of `0` disables this timeout.The default is `300000` ms (5 minutes).                                                                                                  |
   | Socket Write Timeout (ms)      | Elapsed time before Advanced Identity Cloud times out because client can't write to the SMTP server. A setting of `0` disables this timeout.The default is `300000` (5 minutes).                                                                                                                |
   | Socket Timeout (ms)            | Elapsed time before Advanced Identity Cloud times out due to inactivity. A setting of `0` disables this timeout.The default is `300000` (5 minutes).                                                                                                                                            |
   | Use STARTTLS                   | * If enabled, and if the SMTP server supports the STARTTLS command, then Advanced Identity Cloud switches to a TLS-protected connection before issuing any login commands.

   * If the SMTP server does not support STARTTLS, the connection continues without the use of TLS.Enabled by default. |
   | Use SSL                        | If enabled, Advanced Identity Cloud uses SSL to connect to the SMTP server.Disabled by default.                                                                                                                                                                                                 |
   | Allow UTF-8                    | If enabled, adds support for UTF-8 (Non-ASCII) characters in the *local* part of email addresses (everything before the `@` character).Disabled by default.&#xA;&#xA;Do not set this property unless your SMTP provider supports UTF-8 characters. Learn more in International email addresses. |

5. To test your configuration, click Send Test Email.

   1. In the Send Test Email dialog box, enter your own email address.

   2. Click Send.

   If the test is successful, you'll get a test email in your email inbox.

6. To save the email provider configuration, click Save.

#### Using the API

You can edit the email service over REST at the `openidm/config/external.email` endpoint. The following example submits an email configuration over REST:

```
curl \
--header "Authorization: Bearer <access-token>" \(1)
--header "Accept-API-Version: resource=1.0" \
--header "Content-Type: application/json" \
--request PUT \
--data '{
    "host" : "smtp.gmail.com",
    "port" : 587,
    "debug" : false,
    "auth" : {
        "enable" : true,
        "username" : "admin",
        "password" : "Passw0rd"
    },
    "from" : "admin@example.com",
    "timeout" : 300000,
    "writetimeout" : 300000,
    "connectiontimeout" : 300000,
    "starttls" : {
        "enable" : true
    },
    "ssl" : {
        "enable" : false
    },
    "smtpProperties" : [
        "mail.smtp.ssl.protocols=TLSv1.2",
        "mail.smtps.ssl.protocols=TLSv1.2",
        "mail.mime.allowutf8=true"
    ],
    "threadPoolSize" : 20
}' \
"https://<tenant-env-fqdn>/openidm/config/external.email"
```

|       |                                                                                                                                                                                                                                         |
| ----- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **1** | Replace \<access-token> with an access token that has the `fr:idm:*` scope. Learn more in [Get an access token](https://developer.pingidentity.com/pingoneaic-api/authenticate-to-rest-api-with-access-token.html#get-an-access-token). |

#### Sample email configuration

This sample email configuration sets up the email provider:

* SMTP

* MS Graph API

```json
{
    "host" : "smtp.gmail.com",
    "port" : 587,
    "debug" : false,
    "auth" : {
        "enable" : true,
        "username" : "xxxxxxxx",
        "password" : "xxxxxxxx"
    },
    "timeout" : 300000,
    "writetimeout" : 300000,
    "connectiontimeout" : 300000,
    "starttls" : {
        "enable" : true
    },
    "ssl" : {
        "enable" : false
    },
    "smtpProperties" : [
        "mail.smtp.ssl.protocols=TLSv1.2",
        "mail.smtps.ssl.protocols=TLSv1.2",
        "mail.mime.allowutf8=true"
    ],
    "threadPoolSize" : 20
}
```

```json
{
    "type" : "msgraph",
    "mailEndpoint" : "https://graph.microsoft.com/v1.0/users/example@myTenant.onmicrosoft.com/sendMail",
    "from" : "example@myTenant.onmicrosoft.com",
    "auth" : {
        "enable" : true,
        "type" : "oauth2",
        "clientId" : "clientId",
        "clientSecret" : "clientSecret",
        "tokenEndpoint" : "https://login.microsoftonline.com/myTenant.onmicrosoft.com/oauth2/v2.0/token",
        "scope" : [
            "https://graph.microsoft.com/.default"
        ]
    },
    "timeout" : 300000,
    "writetimeout" : 300000,
    "connectiontimeout" : 300000,
    "threadPoolSize" : 20
}
```

### Revert the email provider to use the built-in SMTP server

If you need to revert the email provider to use the built-in SMTP server:

1. In the Advanced Identity Cloud admin console, go to Email > Provider.

2. On the Email Provider page, disable Use my own email provider.

3. Click Save.

|   |                                                                                                              |
| - | ------------------------------------------------------------------------------------------------------------ |
|   | The built-in SMTP server is for testing purposes only and has the limitations noted at the top of this page. |

***

[1](#_footnoteref_1). A [sandbox environment](environments-sandbox.html) is an [add-on capability](../product-information/add-on-capabilities.html).[2](#_footnoteref_2). A [user acceptance testing (UAT) environment](environments-uat.html) is an [add-on capability](../product-information/add-on-capabilities.html).

---

---
title: Email provider configuration reference
description: type
component: pingoneaic
page_id: pingoneaic:tenants:email-provider-configuration-reference
canonical_url: https://docs.pingidentity.com/pingoneaic/tenants/email-provider-configuration-reference.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  properties: Properties
  auth-sub-prop-table: auth sub-properties
  oath2-table: oauth2 properties
  smtp-sub-prop-table: smtpProperties sub-properties
---

# Email provider configuration reference

## Properties

| Property            | Description                                                                                                                                                                                                                                                                                                                                                                                                                              | Required? / Type Support                         |
| ------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------ |
| `type`              | The [email service type](email-provider.html#external-email-services), `smtp` or `msgraph`. When no type is specified, the default value is `smtp`.                                                                                                                                                                                                                                                                                      | No                                               |
| `mailEndpoint`      | The URI for the MS Graph API `sendMail` endpoint.Typical format:```none
https://graph.microsoft.com/v1.0/users/{user}@{tenant}.onmicrosoft.com/sendMail
```                                                                                                                                                                                                                                                                              | YesOnly for `msgraph` type.                      |
| `host`              | The hostname or IP address of the SMTP server.                                                                                                                                                                                                                                                                                                                                                                                           | YesOnly for `smtp` type.                         |
| `port`              | SMTP server port number, such as 25, 465, or 587.Many SMTP servers require the use of a secure port such as 465 or 587. Many ISPs flag email from port 25 as spam.                                                                                                                                                                                                                                                                       | YesOnly for `smtp` type.                         |
| `debug`             | When set to `true`, this option outputs diagnostic messages from the JavaMail library. Debug mode can be useful if you're having difficulty configuring the external email endpoint with your email server.                                                                                                                                                                                                                              | NoOnly for `smtp` type.                          |
| `from`              | Specifies a default From: address which displays when users receive emails from Advanced Identity Cloud.Although `from` is optional in the email configuration, the email service requires this property to send email. If you don't specify a `from` address in the email configuration, you must provide one in another way, for example:- From an email template.

- As a parameter in the email service request (`from` or `_from`). | No                                               |
| `auth`              | Contains authentication detail sub-properties. Learn more about [authentication sub-properties](#auth-sub-prop-table).                                                                                                                                                                                                                                                                                                                   | YesRequired sub-properties vary based on `type`. |
| `starttls`          | If `"enable" : true`, enables the use of the STARTTLS command (if supported by the server) to switch the connection to a TLS-protected connection before issuing any login commands. If the server doesn't support STARTTLS, the connection continues without the use of TLS.                                                                                                                                                            | NoOnly for `smtp` type.                          |
| `ssl`               | Set `"enable" : true` to use SSL to connect, and use the SSL port by default.                                                                                                                                                                                                                                                                                                                                                            | NoOnly for `smtp` type.                          |
| `smtpProperties`    | SMTP options. Learn more about [SMTP sub-properties](#smtp-sub-prop-table).                                                                                                                                                                                                                                                                                                                                                              | NoOnly for `smtp` type.                          |
| `threadPoolSize`    | Emails are sent in separate threads managed by a thread pool. This property sets the number of concurrent emails that can be handled at a specific time. The default thread pool size (if none is specified) is `20`.                                                                                                                                                                                                                    | No                                               |
| `connectiontimeout` | The socket connection timeout, in milliseconds. The default connection timeout (if none is specified) is `300000` milliseconds, or five minutes. A setting of 0 disables this timeout.                                                                                                                                                                                                                                                   | No                                               |
| `timeout`           | The socket read timeout, in milliseconds. The default read timeout (if none is specified) is `300000` milliseconds, or five minutes. A setting of 0 disables this timeout.                                                                                                                                                                                                                                                               | NoOnly for `smtp` type.                          |
| `writetimeout`      | The socket write timeout, in milliseconds. The default write timeout (if none is specified) is `300000` milliseconds, or five minutes. A setting of 0 disables this timeout.                                                                                                                                                                                                                                                             | NoOnly for `smtp` type.                          |

|   |                                                                                                                                                  |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | The `msgraph` type also supports the [External REST configuration properties](../external-services/external-rest.html#external.rest.properties). |

## `auth` sub-properties

| Property   | Description                                                                                                                                                                                                                                                             | Required? / Type Support |
| ---------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------ |
| `enable`   | Whether you need login credentials to connect to the server/API.If `"enable" : false,`, you can leave the entries for `"username"` and `"password"` empty:```json
"enable" : false,
"username" : "",
"password" : ""
```                                                | Yes                      |
| `username` | Account used to connect to the server/API.                                                                                                                                                                                                                              | No                       |
| `password` | Password used to connect to the server/API.                                                                                                                                                                                                                             | No                       |
| `type`     | Authentication type used to connect to the server/API:- `basic`—basic authentication using a username and password. Default value.

- `oauth2`—OAuth2 authentication. Requires additional `oauth2` properties. The `msgraph` configuration type only supports `oauth2`. | Yes                      |

## `oauth2` properties

| Property                                                                       | Description                                                                                                                                                                                  | Required? / Type Support |
| ------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------ |
| The following properties are only applicable when the `auth/type` is `oauth2`. |                                                                                                                                                                                              |                          |
| `clientId`                                                                     | Client ID used to request an access token from the token endpoint. Obtained during [Azure application creation](email-provider-configure-microsoft-azure-tenant.html#note-clientId).         | Yes                      |
| `clientSecret`                                                                 | Client secret used to request an access token from the token endpoint. Obtained during [Azure application creation](email-provider-configure-microsoft-azure-tenant.html#note-clientSecret). | Yes                      |
| `tokenEndpoint`                                                                | OAuth2 token endpoint.Typical format:```none
https://login.microsoftonline.com/{tenant}.onmicrosoft.com/oauth2/v2.0/token
```                                                                | Yes                      |
| `scope`                                                                        | Requested OAuth2 scopes in a JSON array of strings.                                                                                                                                          | Yes                      |
| `scopeDelimiter`                                                               | Scope delimiter to use. Defaults to space.                                                                                                                                                   | No                       |
| `grantType`                                                                    | The only supported grant type is `client_credentials`.                                                                                                                                       | No                       |

## `smtpProperties` sub-properties

| Property                   | Description                                                                                                                                                                                                                                                                      | Required? / Type Support |
| -------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------ |
| `mail.smtp.ssl.protocols`  | The enabled SMTP SSL connection protocols. Protocols are specified as a whitespace-separated list. The default protocol is TLSv1.2.                                                                                                                                              | NoOnly for `smtp` type.  |
| `mail.smtps.ssl.protocols` | The enabled SMTPS SSL connection protocols. Protocols are specified as a whitespace-separated list. The default protocol is TLSv1.2.                                                                                                                                             | NoOnly for `smtp` type.  |
| `mail.mime.allowutf8`      | Adds support for UTF-8 (Non-ASCII) characters in the *local* part of email addresses (everything before the `@` character) if set to `true`.&#xA;&#xA;Do not set this property unless your SMTP provider supports UTF-8 characters. Learn more in International email addresses. | NoOnly for `smtp` type.  |

---

---
title: Email templates
description: PingOne Advanced Identity Cloud provides preconfigured email templates for common end-user journeys.
component: pingoneaic
page_id: pingoneaic:tenants:email-templates
canonical_url: https://docs.pingidentity.com/pingoneaic/tenants/email-templates.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Features", "Journeys", "Setup &amp; Configuration", "Tenants", "Users"]
section_ids:
  create-a-new-email-template: Create a new email template
  edit-an-email-template: Edit an email template
  add-email-template-images: Add an image to an email template
  email-template-html-formatting: Use HTML formatting in an email template
  email-template-esvs: Use ESV variables in an email template
  email-template-add-esvs: Add ESV variables to an email template
  manage-email-template-locales: Manage email template locales
  delete-an-email-template: Delete an email template
  manage-email-templates: Manage email templates
  more-information-email-templates: More information
---

# Email templates

PingOne Advanced Identity Cloud provides preconfigured email templates for common end-user journeys.

You can customize email templates using [Markdown language](https://commonmark.org/help/). Advanced Identity Cloud uses a parser to let you preview your markup.

|   |                                                                                                                                                                                                           |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Email templates use [Handlebars expressions](https://handlebarsjs.com/guide/) to reference object data dynamically. For example, to reference the `userName` of an object:```html
{{object.userName}}
``` |

## Create a new email template

1. In the Advanced Identity Cloud admin console, go to Email > Templates.

2. On the Email Templates page, click + New Template.

3. Provide the following details:

   * Template Name: Display name for the template.

   * From Address: Enter an email address for the group or individual sending the email.

   * From Name: Enter a name for the group or individual sending the email.

   * Description: A brief description of the template.

4. Click Save. The new email opens in the email editor.

5. Learn more in [Edit an email template](#edit-an-email-template).

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | When you reference an email template, such as in a node or script, you must use its unique template ID. Advanced Identity Cloud generates this ID from the template's original name (converted to camelCase). The ID is immutable, meaning it won't change even if you rename the template later.You can find the template ID in the Advanced Identity Cloud admin console URL when editing the template. For example, the template ID for the Forgotten Username template is `forgottenUsername`:```none
https://<tenant-env-fqdn>/?realm=alpha#/email/templates/edit/forgottenUsername
``` |

## Edit an email template

1. In the Advanced Identity Cloud admin console, go to Email > Templates.

2. On the Email Templates page, click a template name to open the email editor.

3. To change the wording in the email template, edit the Markdown text in the left window on the page. You can also:

   * [Add an image to an email template](#add-email-template-images)

   * [Use HTML formatting in an email template](#email-template-html-formatting)

   * [Use ESV variables in an email template](#email-template-esvs)

4. Add, modify, or delete locales to suit your end-user audience. Learn more in [Manage email template locales](#manage-email-template-locales).

5. Repeat step 3 for each template locale.

6. To edit the template styles, click Styles, and edit the CSS style code.

7. To view available variables that you can use in the template, click Variables, and view the content on the Available Properties page. Click Done.

8. To edit the template settings, click the More ([icon: ellipsis-h, set=fa]) icon at the top right of the page, and select Settings.

9. Provide the following details:

   * Template Name: Display name for the template.

   * From Address: Enter an email address for the group or individual sending the email.

   * From Name: Enter a name for the group or individual sending the email.

   * Description: Enter a brief description of the template.

10. Click Update.

11. Click Save. This saves content changes in all template locales.

### Add an image to an email template

1. Upload your image to a hosted service, such as a content delivery network (CDN), so it is available over HTTPS. Local image paths are not permitted.

2. In the Advanced Identity Cloud admin console, go to Email > Templates.

3. On the Email Templates page, click a template name to open the email editor.

4. Edit the Markdown text to reference your image:

   * To add an image at full size:

     ```markdown
     ![alt text](<image url>)
     ```

     For example, the Markdown would look like this for an image hosted at `https://example.com/image.ext` where the alt text is `this is an example image`:

     ```markdown
     ![this is an example image](<https://example.com/image.ext>)
     ```

   * To add an image and resize it in pixels:

     ```markdown
     ![this is an example image](<https://example.com/image.ext> =100x100)
     ```

   * To add an image and resize it as a percentage:

     ```markdown
     ![this is an example image](<https://example.com/image.ext> =50%x50%)
     ```

5. Click Save.

### Use HTML formatting in an email template

Although you can't see HTML formatting in the editor, you can use inline HTML to format your email. Learn more in [Markdown Syntax: Inline HTML](https://daringfireball.net/projects/markdown/syntax#html).

1. In the Advanced Identity Cloud admin console, go to Email > Templates.

2. On the Email Templates page, click a template name to open the email editor.

3. Edit the Markdown text:

   * Specify HTML tags to format your content. For example:

     ```html
     <h1>Reset Password</h1>
     ```

   * To add a table, include both the `<thead>` and `<tbody>` tags; otherwise the table will not convert correctly to Markdown when saved. For example:

     ```html
     <table>
       <thead>
         <tr>
          <th>Header 1</th>
          <th>Header 2</th>
          <th>Header 3</th>
         </tr>
       </thead>
       <tbody>
         <tr>
           <td>Cell Text 1</td>
           <td>Cell Text 2</td>
           <td>Cell Text 3</td>
         </tr>
       </tbody>
     </table>
     ```

4. Click Styles, and add CSS styles for the tag to format it as required. For example:

   ```css
   h1 {
       font-family: Arial, Helvetica, sans-serif;
       color: #f96700;
       background-color: #032b75;
       font-size: 25px;
       padding: 10px;
   }
   ```

5. Click Save.

After saving your changes, the inline HTML tags are converted to Markdown, but the CSS styles for the tags persist. The CSS styles apply to all locales.

|   |                                                                                                                                                                |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Alternatively, you can click Advanced Editor and modify the template in HTML. However, if you swap to the Advanced Editor, you cannot change back to Markdown. |

### Use ESV variables in an email template

You can use ESV variables in email templates to dynamically present different text, images, or links depending on the specific tenant environment.

You can find background information on ESVs in PingOne Advanced Identity Cloud in [ESVs](esvs.html).

|   |                                                                                                                                                                 |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | To add ESV variables to an email template, you must use the Advanced Editor. After you have swapped to the Advanced Editor, you cannot change back to Markdown. |

#### Add ESV variables to an email template

1. Create the ESV variables to use in the email template:

   1. Create the variables using the [Advanced Identity Cloud admin console](esvs-manage-ui.html) or [variables APIs](esvs-manage-api.html).

   2. Restart Advanced Identity Cloud services by [applying updates in the Advanced Identity Cloud admin console](esvs-manage-ui.html#apply-updates) or using the [restart API](esvs-manage-api.html).

2. In the Advanced Identity Cloud admin console, go to Email > Templates.

3. On the Email Templates page, click a template name to open the email editor.

4. Click Advanced Editor.

5. Add the placeholder for one or more ESV variables. For example:

   ```html
   &{esv.my.variable}
   ```

6. Click Save.

Example

1. In step 1, add these two ESV variables:

   * `esv-test-link`, with a value of `https://test.example.com`

   * `esv-test-image`, with a value of `https://example.com/image.ext`

2. In step 5, add the link and image:

   * Add the link using the ESV placeholder, where the link text is the URL, for example:

     ```html
     <p>For more information, go to our website: &{esv.test.link}</p>
     ```

     |   |                                                                                                                                     |
     | - | ----------------------------------------------------------------------------------------------------------------------------------- |
     |   | You can also add the link using the `<a>` tag with the `href` attribute. This is useful if you want to display different link text. |

   * Add the image using the ESV placeholder, for example:

     ```html
     <p>
     <img src="&{esv.test.image}">
     </p>
     ```

   The preview in the left window shows the ESV placeholder and an image placeholder rather than the actual link and image as these are only resolved when the email is sent.

## Manage email template locales

You can create email content for different locales. When an email is sent during an end-user journey, Advanced Identity Cloud automatically selects the appropriate email template based on the value of the `accept-language` header, typically derived from the language set in the end user's browser.

|   |                                                                                           |
| - | ----------------------------------------------------------------------------------------- |
|   | Use the browser's developer tools to check the value set in the `accept-language` header. |

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | When sending email templates, you can use a script to override the language set in the end user's `accept-language` header. Use the `sendTemplate` action in your script and set the language in the `params._locale` object property. The language specified in the script takes precedence over the end user's browser language. Learn more in [Send email templates using a script](email-send.html#send_email_templates_using_a_script). |

The locale selector in the top left of the email template editor displays the current template's locale in the format Locale: *code*, where *code* is a [ISO-639-1 language code](https://en.wikipedia.org/wiki/List_of_ISO_639_language_codes), for example, `en` or `de`. Some preconfigured email templates, such as the registration template, already include content for the `en` (default) and `fr` locales.

To manage email template locales:

1. In the Advanced Identity Cloud admin console, go to Email > Templates.

2. On the Email Templates page, click a template name to open the email editor.

3. Switch, add, modify, or delete a locale:

   * To switch locale:

     1. Click Locale: *code*.

     2. Select a locale.

   * To add a locale:

     1. Click Locale: *code*.

     2. Click [icon: add, set=material, size=inline] Add Locale to open the Add Locale modal.

     3. Enter a [ISO-639-1 language code](https://en.wikipedia.org/wiki/List_of_ISO_639_language_codes) in the Code field.

     4. (Optional) Select Make Default to make the new locale the default for this template.

     5. Click Save to add the new locale to the template, populated with a copy of the content from the default locale. The changes apply immediately without saving the main template.

   * To modify a locale:

     1. Click Locale: *code*.

     2. Click the locale's edit icon ([icon: edit, set=material, size=inline]) to open the Edit Locale modal.

     3. To change the locale, enter a [ISO-639-1 language code](https://en.wikipedia.org/wiki/List_of_ISO_639_language_codes) in the Code field.

     4. To make the locale the default locale for the template, select Make Default.

     5. Click Save to close the modal window. Any changes apply immediately without saving the main template.

   * To delete a locale:

     1. Click Locale: *code*.

     2. Click the locale's edit icon ([icon: edit, set=material, size=inline]) to open the Edit Locale modal.

     3. Click Delete Locale to delete the locale and its content. The deletion applies immediately without saving the main template.

## Delete an email template

|   |                                              |
| - | -------------------------------------------- |
|   | Deleting an email template cannot be undone. |

1. In the Advanced Identity Cloud admin console, go to Email > Templates.

2. On the Email Templates page, click the More ([icon: ellipsis-h, set=fa]) icon adjacent to any template.

3. Select Delete.

4. In the dialog box, click Delete.

## Manage email templates

1. In the Advanced Identity Cloud admin console, go to Email > Templates.

2. On the Email Templates page, click the More ([icon: ellipsis-h, set=fa]) icon adjacent to any template, and do any of the following:

   * To disable a template, click Deactivate.

   * To enable a template, click Activate.

   * To duplicate a template, click Duplicate.

     1. In the Duplicate Template window, enter the following details:

        * Template Name: Display name for the template.

        * From Address: Enter an email address for the group or individual sending the email.

        * From Name: Enter a name for the group or individual sending the email.

        * Description: A brief description of the template.

     2. Click Save.

## More information

* [Email Suspend node](https://docs.pingidentity.com/auth-node-ref/latest/email-suspend.html)

* [Email Template node](https://docs.pingidentity.com/auth-node-ref/latest/email-template.html)

---

---
title: ESVs
description: Environment secrets and variables (ESVs) let you individually configure your sandbox[1], development, UAT[2], staging, and production tenant environments in PingOne Advanced Identity Cloud.
component: pingoneaic
page_id: pingoneaic:tenants:esvs
canonical_url: https://docs.pingidentity.com/pingoneaic/tenants/esvs.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Environment secrets and variables (ESVs)"]
section_ids:
  variables: Variables
  variable-expression-types: Variable expression types
  secrets: Secrets
  secret-versions: Secret versions
  encoding-format: Encoding format
  control-access-to-secrets: Control access to secrets
  comparison-of-secrets-and-variables: Comparison of secrets and variables
  preconditions-to-delete-an-esv: Preconditions to delete an ESV
  esv-naming: ESV naming
  esv-api-naming-convention: ESV API naming convention
  esv-legacy-naming-convention-and-api-compatibility: ESV legacy naming convention and API compatibility
  esv-descriptions: ESV descriptions
---

# ESVs

Environment secrets and variables (ESVs) let you individually configure your sandbox\[[1](#_footnotedef_1 "View footnote.")], development, UAT\[[2](#_footnotedef_2 "View footnote.")], staging, and production tenant environments in PingOne Advanced Identity Cloud.

Use variables to set values that need to be different for each tenant environment. For example, an authentication node might need one URL in your development environment, but a different URL in your production environment.

Use secrets to set values that need encrypting. The values may or may not need to be different for each tenant environment. For example, an MFA push notification node might need an authorization password to use an external SMS service.

|   |                                                                                                                                                                                                                                                                                          |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | ESV data is held in a global service and not subject to regional data storage. You therefore must not store personally identifiable information (PII) in ESVs. You are responsible for ensuring that your use of ESVs complies with all applicable data protection laws and regulations. |

|   |                                                                                                                                                                  |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | ESVs are an Advanced Identity Cloud only feature. In particular, ESV secrets should not be confused with secrets in the self-managed PingAM or PingIDM products. |

## Variables

Use ESV variables to set configuration values that need to be different for each tenant environment.

Variables are simple key-value pairs. Unlike secrets, they are not versioned. They should not contain sensitive values. The value of a variable must not exceed a maximum length of 65535 bytes (just under 64KiB).

You can reference ESV variables from configuration placeholders or scripts after you:

* Create or update the variables using the [variables APIs](esvs-manage-api.html) or the [Advanced Identity Cloud admin console](esvs-manage-ui.html).

* Restart Advanced Identity Cloud services using the [restart API](esvs-manage-api.html) or by [applying updates in the Advanced Identity Cloud admin console](esvs-manage-ui.html#apply-updates).

  |   |                                                                                                                                                                                   |
  | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | Other ways of restarting Advanced Identity Cloud services, such as by running a promotion, won't load ESV changes. This makes it easier to identify issues caused by ESV changes. |

The following table shows how to reference an ESV variable with the name `esv-my-variable`:

| Context                    | How to reference                                                                                                                                                | Access as soon as set                    |
| -------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------- |
| Configuration placeholders | `&{esv.my.variable}` Learn more in [Configure placeholders to use with ESVs](configuration-placeholders.html).                                                  | [icon: times, set=fa] (requires restart) |
| Scripts                    | `systemEnv.getProperty("esv.my.variable")` (AM) `identityServer.getProperty("esv.my.variable")` (IDM) Learn more in [Use ESVs in scripts](esvs-scripting.html). | [icon: times, set=fa] (requires restart) |

### Variable expression types

You must use the `expressionType` parameter to set an expression type when you create an ESV variable. This lets Advanced Identity Cloud correctly transform the value of the ESV variable to match the configuration property expression type when substituting it into configuration.

The expression type is set when the ESV variable is created, and it cannot be modified.

|   |                                                                                                                                                                                                                                                                                                                                                                            |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | When creating an ESV variable to use in an authentication node, use the [listLatestNodeDefinitions](../am-authentication/list-latest-node-definitions.html) action to find the required expression type. In the response, look for the `type` field in the schema for the relevant configuration property. Make sure the ESV `expressionType` matches the property `type`. |

Before the `expressionType` parameter was introduced, it was only possible to set expression types from within configuration, using expression level syntax; for example, `{"$int": "&{esv.journey.ldap.port|1389}"}`. The `expressionType` parameter supplements this expression level syntax and allows the ESV type to be identified without inspecting configuration.

|   |                                                                                                                                             |
| - | ------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Make sure the expression type that you set in configuration matches the expression type that you set in the ESV `expressionType` parameter. |

| Expression type | Description                                                                      | Examples                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| --------------- | -------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `string`        | String value (default)                                                           | Name&#xA;&#xA;&#x9;&#xA;&#xA;esv-email-provider-from-email&#xA;&#xA;&#xA;&#xA;&#xA;Placeholder&#xA;&#xA;&#x9;&#xA;&#xA;{"string": "&{esv.email.provider.from.email}"}&#xA;or&#xA;&{esv.email.provider.from.email}&#xA;&#xA;&#xA;&#xA;&#xA;Value&#xA;&#xA;&#x9;&#xA;&#xA;bjensen\@example.com                                                                                                                                                                                                                          |
| `array`         | JSON array                                                                       | Name&#xA;&#xA;&#x9;&#xA;&#xA;esv-cors-accepted-origins&#xA;&#xA;&#xA;&#xA;&#xA;Placeholder&#xA;&#xA;&#x9;&#xA;&#xA;{"$array": "&{esv.cors.accepted.origins}"}&#xA;&#xA;&#xA;&#xA;&#xA;Value&#xA;&#xA;&#x9;&#xA;&#xA;\["http\://example.org", "http\://example.com"]Name&#xA;&#xA;&#x9;&#xA;&#xA;esv-provisioner-base-contexts&#xA;&#xA;&#xA;&#xA;&#xA;Placeholder&#xA;&#xA;&#x9;&#xA;&#xA;{"$array": "&{esv.provisioner.base.contexts}"}&#xA;&#xA;&#xA;&#xA;&#xA;Value&#xA;&#xA;&#x9;&#xA;&#xA;\["dc=example,dc=com"] |
| `object`        | JSON object                                                                      | Name&#xA;&#xA;&#x9;&#xA;&#xA;esv-journey-welcome-description&#xA;&#xA;&#xA;&#xA;&#xA;Placeholder&#xA;&#xA;&#x9;&#xA;&#xA;{"$object": "&{esv.journey.welcome.description}"}&#xA;&#xA;&#xA;&#xA;&#xA;Value&#xA;&#xA;&#x9;&#xA;&#xA;{"en":"Example description","fr":"Exemple de description"}                                                                                                                                                                                                                           |
| `bool`          | Boolean value                                                                    | Name&#xA;&#xA;&#x9;&#xA;&#xA;esv-email-provider-use-ssl&#xA;&#xA;&#xA;&#xA;&#xA;Placeholder&#xA;&#xA;&#x9;&#xA;&#xA;{"$bool": "&{esv.email.provider.use.ssl}"}&#xA;&#xA;&#xA;&#xA;&#xA;Value&#xA;&#xA;&#x9;&#xA;&#xA;true                                                                                                                                                                                                                                                                                             |
| `int`           | Integer value                                                                    | Name&#xA;&#xA;&#x9;&#xA;&#xA;esv-email-provider-port&#xA;&#xA;&#xA;&#xA;&#xA;Placeholder&#xA;&#xA;&#x9;&#xA;&#xA;{"$int": "&{esv.email.provider.port}"}&#xA;&#xA;&#xA;&#xA;&#xA;Value&#xA;&#xA;&#x9;&#xA;&#xA;465                                                                                                                                                                                                                                                                                                     |
| `number`        | This type can transform any number value (integers, doubles, longs, and floats). |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `list`          | Comma-separated list                                                             | Name&#xA;&#xA;&#x9;&#xA;&#xA;esv-journey-ldap-servers&#xA;&#xA;&#xA;&#xA;&#xA;Placeholder&#xA;&#xA;&#x9;&#xA;&#xA;{"$list": "&{esv.journey.ldap.servers}"}&#xA;&#xA;&#xA;&#xA;&#xA;Value&#xA;&#xA;&#x9;&#xA;&#xA;userstore-0.userstore:1389,userstore-1.userstore:1389,userstore-2.userstore:1389	Ping Identity recommends using array type variables instead of list type variables. The two types are functionally equivalent, but the array type is more compatible with the UI.                                   |

|   |                                                                                                                                                                                    |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Existing ESVs will be migrated to use the `expressionType` parameter. If any existing ESVs contain combined types, they will be split into separate ESVs by the migration process. |

## Secrets

Use ESV secrets to set configuration values that need encrypting. The values may or may not need to be different for each tenant environment.

You can reference ESV secrets from configuration placeholders or scripts after you:

* Create or update the secrets using the [secrets APIs](esvs-manage-api.html) or the [Advanced Identity Cloud admin console](esvs-manage-ui.html).

* Restart Advanced Identity Cloud services using the [restart API](esvs-manage-api.html) or by [applying updates in the Advanced Identity Cloud admin console](esvs-manage-ui.html#apply-updates).

  |   |                                                                                                                                                                                   |
  | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | Other ways of restarting Advanced Identity Cloud services, such as by running a promotion, won't load ESV changes. This makes it easier to identify issues caused by ESV changes. |

You can reference secrets that are signing and encryption keys by mapping them to [secret labels](esvs-signing-encryption.html#secret-labels). Secrets referenced by secret label mappings can be accessed as soon as the ESV is set; restarting Advanced Identity Cloud services is not required.

The following table shows how to reference an ESV secret with the name `esv-my-secret`:

| Context                     | How to reference                                                                                                                                            | Access as soon as set                    |
| --------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------- |
| Configuration placeholders  | `&{esv.my.secret}` Learn more in [Configure placeholders to use with ESVs](configuration-placeholders.html).                                                | [icon: times, set=fa] (requires restart) |
| Scripts                     | `systemEnv.getProperty("esv.my.secret")` (AM) `identityServer.getProperty("esv.my.secret")` (IDM) Learn more in [Use ESVs in scripts](esvs-scripting.html). | [icon: times, set=fa] (requires restart) |
| Signing and encryption keys | [Map to secret label](esvs-signing-encryption.html#map-esv-secrets-to-secret-labels)                                                                        | [icon: check, set=fa]                    |

### Secret versions

Instead of having a single value, ESV secrets have one or more secret versions, each containing their own value. By design, the value of a secret version cannot be read back after it has been created. The value of a secret version must not exceed a maximum length of 65535 bytes (just under 64KiB).

To create a new secret version, its value must be different from the value of the latest secret version. If you try to create a new secret version with the same value as the latest version, the existing version is retained and no changes are made.

You can enable or disable secret versions by setting their status field to `ENABLED` or `DISABLED` using the REST API or clicking the Active toggle in the admin console. The latest version of a secret must be enabled for it to be used in your configuration.

The following rules ensure that a secret always has at least one enabled version:

* When you create a secret, the first version of the secret is automatically created and is enabled.

* You cannot disable the latest version of a secret.

* You cannot delete the latest version of a secret if the previous version is disabled.

|   |                                                                                                                                                                              |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Secret versions are an important feature of key rotation. Learn more in [Rotate keys in mapped ESV secrets](esvs-signing-encryption.html#rotate-keys-in-mapped-esv-secrets). |

### Encoding format

You can use the `encoding` parameter to set an encoding format when you create an ESV secret:

| Encoding format | Description                                                                                                                                                                           |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `generic`       | Use this format for secrets that are not keys, such as passwords.                                                                                                                     |
| `pem`           | Use this format for asymmetric keys; for example, a public and private RSA key pair. Learn more in [Generate an RSA key pair](esvs-signing-encryption.html#generate-an-rsa-key-pair). |
| `base64aes`     | Use this format for AES keys; for example, an AES-256 key. Learn more in [Generate an AES or HMAC key](esvs-signing-encryption.html#generate-an-aes-or-hmac-key).                     |
| `base64hmac`    | Use this format for HMAC keys; for example, a HMAC-SHA-512 key. Learn more in [Generate an AES or HMAC key](esvs-signing-encryption.html#generate-an-aes-or-hmac-key).                |

### Control access to secrets

There are 3 contexts where you can access an ESV secret:

1. From configuration placeholders; learn more in [Configure placeholders to use with ESVs](configuration-placeholders.html).

2. From scripts; learn more in [Use ESVs in scripts](esvs-scripting.html).

3. From mapped secret labels (for signing and encryption keys); learn more in [Use ESVs for signing and encryption keys](esvs-signing-encryption.html).

However, if the secret contains a signing and encryption key, you may want to restrict access from configuration placeholder and script contexts. To do this, you can use the `useInPlaceholders` boolean parameter when you create the secret:

| Context                    | Unrestricted access                                                                                                   | Restricted access             |
| -------------------------- | --------------------------------------------------------------------------------------------------------------------- | ----------------------------- |
|                            | `useInPlaceholders` = `true`                                                                                          | `useInPlaceholders` = `false` |
| Configuration placeholders | * Secret accessible

* Uses latest secret version

* Restart of Advanced Identity Cloud services required             | - Secret not accessible       |
| Scripts                    | * Secret accessible

* Uses latest secret version

* Restart of Advanced Identity Cloud services *not* required       |                               |
| Mapped secret labels       | - Secret accessible

- Uses all enabled secret versions

- Restart of Advanced Identity Cloud services *not* required |                               |

|   |                                                                                                                   |
| - | ----------------------------------------------------------------------------------------------------------------- |
|   | You can only set restricted access using the API. The UI currently creates secrets only with unrestricted access. |

### Comparison of secrets and variables

![esv variable secret comparison](_images/esv-variable-secret-comparison.png)

### Preconditions to delete an ESV

Before you delete an ESV, you may need to remove references to it from your environment:

* You cannot delete an ESV if it is referenced in a configuration placeholder. You must first remove the placeholder from configuration. Learn more in [Delete an ESV referenced by a configuration placeholder](configuration-placeholders.html#delete-esv-referenced-by-configuration-placeholder).

* You cannot delete an ESV if it is referenced in a script. You must first remove any scripts that reference the ESV.

* You cannot delete an ESV if it is referenced in an orphaned script\[[3](#_footnotedef_3 "View footnote.")]. You must first remove any orphaned scripts. You can do this by running a self-service promotion (which automatically cleans up orphaned scripts).

## ESV naming

### ESV API naming convention

The names of secrets and variables need to be prefixed with `esv-` and can only contain alphanumeric characters, hyphens, and underscores; for example, `esv-mysecret-1` or `esv-myvariable_1`. The maximum length, including prefix, is 124 characters.

### ESV legacy naming convention and API compatibility

Before the introduction of the ESV API endpoints, if ESVs were defined on your behalf as part of the promotion process, they were prefixed with `byos-`. Advanced Identity Cloud uses compatibility behavior to let you still use these legacy ESVs. The compatibility behavior depends on how far the legacy ESVs were promoted through your development, staging, and production tenant environments:

* Development, staging, and production environments

  If you promoted a legacy ESV to all your tenant environments, it will have been duplicated during the ESV migration process, so will be available in the API using the new `esv-` prefix.

  For example, `byos-myvariable123` will appear as `esv-myvariable123`. Scripts that reference the legacy ESV will still work; both `byos-myvariable123` and `esv-myvariable123` resolve to the same ESV.

* Development and staging environments only

  If you never promoted a legacy ESV to your production environment, it will have been ignored during the ESV migration process. However, you can still use the ESV API to create it in your production environment, as the compatibility behaviour looks for new ESVs that have a naming format like a legacy ESV (`byos-<hash>-<name>`). So any ESVs that are created with a naming format of `esv-<hash>-<name>` will also automatically create a `byos-<hash>-<name>` duplicate.

  For example, creating a new ESV called `esv-7765622105-myvariable` will automatically create another ESV called `byos-7765622105-myvariable`. Scripts that reference the legacy ESV will still work; both `byos-7765622105-myvariable` and `esv-7765622105-myvariable` resolve to the same ESV.

### ESV descriptions

ESVs have a description field. This lets you provide further information on how and where to use an ESV.

***

[1](#_footnoteref_1). A [sandbox environment](environments-sandbox.html) is an [add-on capability](../product-information/add-on-capabilities.html).[2](#_footnoteref_2). A [user acceptance testing (UAT) environment](environments-uat.html) is an [add-on capability](../product-information/add-on-capabilities.html).[3](#_footnoteref_3). Orphaned scripts are a legacy problem that can affect tenants that received support-assisted promotions before the introduction of self-service promotions.

---

---
title: Get audit and debug logs
description: PingOne Advanced Identity Cloud provides audit and debug logs to help you manage your tenant:
component: pingoneaic
page_id: pingoneaic:tenants:audit-debug-logs
canonical_url: https://docs.pingidentity.com/pingoneaic/tenants/audit-debug-logs.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Monitoring", "Tenants", "Troubleshooting"]
page_aliases: ["pingoneaic::tenant-audit-logs.adoc", "tenants:audit-logs.adoc"]
---

# Get audit and debug logs

PingOne Advanced Identity Cloud provides audit and debug logs to help you manage your tenant:

* Use audit logs to investigate user and system behavior.

* Use debug logs to investigate any issues that can arise in production.

You can access logs using one of the following methods:

* **Direct log access using REST API**: Retrieve log events directly from the `/monitoring/logs` REST API endpoint. With this method, you access each of your tenant environments individually and use REST API filters to refine log results. Learn more in [Retrieve log entries using REST API](audit-debug-logs-pull.html).

* **External monitoring tool using log streaming**: Use the `/environment/telemetry/*` REST API endpoints to configure each of your tenant environments to steam logs to an external monitoring tool or Security Information and Event Management (SIEM) for real-time security monitoring and error detection. This method lets you access a single external tool and use its interface to refine log results. You can integrate with Splunk or an OpenTelemetry-compatible SIEM such as Grafana Cloud, Datadog, or New Relic. Learn more in [Stream logs to an external monitoring tool](audit-debug-logs-push.html).

* **Advanced Identity Cloud admin console**: Monitor log entries in the admin console. This [beta](../product-information/release-lifecycle.html#beta) feature is limited to development and sandbox\[[1](#_footnotedef_1 "View footnote.")] environments. Learn more in [Monitor log entries in the admin console](audit-debug-logs-monitoring.html).

Advanced Identity Cloud stores logs in various [log sources](audit-debug-log-sources.html). When you retrieve or stream logs, you'll need to specify which sources you're interested in.

Advanced Identity Cloud stores logs for 30 days.

***

[1](#_footnoteref_1). A [sandbox environment](environments-sandbox.html) is an [add-on capability](../product-information/add-on-capabilities.html).

---

---
title: Introduction to self-service promotions
description: PingOne Advanced Identity Cloud lets you run self-service promotions to move static configuration between a sequential pair of tenant environments, either from the development environment to the staging environment (staging promotion), or from the staging environment to the production environment (production promotion).
component: pingoneaic
page_id: pingoneaic:tenants:self-service-promotions
canonical_url: https://docs.pingidentity.com/pingoneaic/tenants/self-service-promotions.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Architecture", "Availability", "Deployment", "Features", "Migration", "Planning", "Promotion", "Tenants"]
page_aliases: ["tenants:promote-configuration.adoc", "tenants:self-service-promotions-migration-faq.adoc", "tenants:self-service-promotions-migration-process-flow.adoc"]
section_ids:
  the-identity-cloud-configuration-model: The Advanced Identity Cloud configuration model
  static-and-dynamic-configuration: Static and dynamic configuration
  lower-and-upper-environments: Lower and upper environments
  standard-promotion-group-of-environments: Standard promotion group of environments
  additional-uat-environments: Additional UAT environments
  environment-locking: Environment locking
  configuration-integrity-checks: Configuration integrity checks
  integrity-check-for-missing-esvs: Integrity check for missing ESVs
  integrity-check-for-encrypted-secrets: Integrity check for encrypted secrets
---

# Introduction to self-service promotions

PingOne Advanced Identity Cloud lets you run self-service promotions to move static configuration between a sequential pair of tenant environments, either from the development environment to the staging environment (staging promotion), or from the staging environment to the production environment (production promotion).

|   |                                                                                                                   |
| - | ----------------------------------------------------------------------------------------------------------------- |
|   | Non-sequential promotions (between the development environment and the production environment) are not supported. |

If you promote configuration that accidentally causes instability or errors, Advanced Identity Cloud lets you run a self-service rollback to restore an upper environment to its previous configuration.

You can run a promotion or a rollback using the following options:

* [Manage self-service promotions using the API](self-service-promotions-api.html)

* [Manage self-service promotions using the admin console](self-service-promotions-ui.html)

## The Advanced Identity Cloud configuration model

The following video summarizes the concepts of the Advanced Identity Cloud configuration model:

**Video (Brightcove)**

\<https\://players.brightcove.net/771836189001/default\_default/index.html?videoId=6343467150112>

## Static and dynamic configuration

Learn about the difference between static and dynamic configuration in these FAQs:

* [What kind of configuration changes can my company make?](self-service-promotions-faqs.html#what-kind-of-configuration-changes-can-my-company-make)

* [How do we determine what is static and dynamic configuration?](self-service-promotions-faqs.html#how-do-we-determine-what-is-static-and-dynamic-configuration)

## Lower and upper environments

In a sequential pair of environments, we refer to the *lower* environment (the configuration source), and the *upper* environment (the configuration destination). The terms lower environment and upper environment therefore refer to different environments, depending on which environment you are promoting to.

### Standard promotion group of environments

A standard promotion group of environments consists of a development, staging, and production environment. If you have any [sandbox environments](environments-sandbox.html), they aren't included in this standard promotion group because it's not possible to promote to or from a sandbox environment.

For a standard promotion group of [development, staging, and production tenant environments](environments-development-staging-production.html), the lower and upper environments are:

|                      | Development environment                        | Staging environment                            | Production environment                         |
| -------------------- | ---------------------------------------------- | ---------------------------------------------- | ---------------------------------------------- |
| Staging promotion    | [icon: south, set=material, size=inline] lower | [icon: north, set=material, size=inline] upper |                                                |
| Production promotion |                                                | [icon: south, set=material, size=inline] lower | [icon: north, set=material, size=inline] upper |

Key:

* [icon: south, set=material, size=inline] lower = lower environment (configuration source)

* [icon: north, set=material, size=inline] upper = upper environment (configuration destination)

### Additional UAT environments

If you add any [UAT environments](environments-uat.html) to your promotion group of environments, they are inserted into the promotion process before the staging environment:

* If you add one UAT environment, the revised lower and upper environments are:

  |                      | Development environment                        | UAT environment                                | Staging environment                            | Production environment                         |
  | -------------------- | ---------------------------------------------- | ---------------------------------------------- | ---------------------------------------------- | ---------------------------------------------- |
  | UAT promotion        | [icon: south, set=material, size=inline] lower | [icon: north, set=material, size=inline] upper |                                                |                                                |
  | Staging promotion    |                                                | [icon: south, set=material, size=inline] lower | [icon: north, set=material, size=inline] upper |                                                |
  | Production promotion |                                                |                                                | [icon: south, set=material, size=inline] lower | [icon: north, set=material, size=inline] upper |

* If you add a second UAT environment, the revised lower and upper environments are:

  |                      | Development environment                        | UAT environment                                | UAT2 environment                               | Staging environment                            | Production environment                         |
  | -------------------- | ---------------------------------------------- | ---------------------------------------------- | ---------------------------------------------- | ---------------------------------------------- | ---------------------------------------------- |
  | UAT promotion        | [icon: south, set=material, size=inline] lower | [icon: north, set=material, size=inline] upper |                                                |                                                |                                                |
  | UAT2 promotion       |                                                | [icon: south, set=material, size=inline] lower | [icon: north, set=material, size=inline] upper |                                                |                                                |
  | Staging promotion    |                                                |                                                | [icon: south, set=material, size=inline] lower | [icon: north, set=material, size=inline] upper |                                                |
  | Production promotion |                                                |                                                |                                                | [icon: south, set=material, size=inline] lower | [icon: north, set=material, size=inline] upper |

* The lower and upper environments are revised in the same way for each additional UAT environment you add.

## Environment locking

|   |                                                                                                                                                                   |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Locking an environment prevents configuration changes that could disrupt a promotion or a rollback; however, all authentication flows continue to work as normal. |

Before you run a promotion or a rollback, you must lock the lower and upper environments. This prevents anyone else from locking either of those environments, which ensures only one promotion or rollback can be run at the same time in the same set of development, staging, and production environments.

Locking the lower and upper environments also blocks access to the ESV API in those environments. This prevents anyone else from accidentally disrupting a promotion or rollback by manipulating ESV configuration values. If the lower environment is also the development environment, then most Advanced Identity Cloud API endpoints are also restricted.

When a promotion or a rollback is complete, you must unlock the lower and upper environments to return the environments back to full functionality.

## Configuration integrity checks

When you run a promotion or a rollback, Advanced Identity Cloud performs integrity checks on your static configuration to protect the stability of the upper environment.

### Integrity check for missing ESVs

|          | Promotion                | Rollback                 |
| -------- | ------------------------ | ------------------------ |
| Checked? | [icon: check, set=fa]Yes | [icon: check, set=fa]Yes |

This integrity check looks for ESVs referenced in your static configuration, but not set in the upper environment.

Advanced Identity Cloud runs this integrity check on the whole configuration, not just configuration changes.

### Integrity check for encrypted secrets

|          | Promotion                | Rollback                |
| -------- | ------------------------ | ----------------------- |
| Checked? | [icon: check, set=fa]Yes | [icon: times, set=fa]No |

This integrity check looks for encrypted secrets embedded directly in your static configuration. It is best practice to store encrypted secrets in an ESV secret and update your configuration to reference the ESV secret instead.

Advanced Identity Cloud runs this integrity check on the whole configuration, not just configuration changes.

---

---
title: Localize tenant admin console and hosted pages
description: You can localize static content and server messages in the Advanced Identity Cloud admin, sign on, and end-user UIs using translation configuration. Translation configuration lets you define a locale-specific set of key/phrase translation pairs that override the default set of key/phrase pairs. You can override some or all of the default keys, in as many locales as you need. The translation configuration has an effect in all realms.
component: pingoneaic
page_id: pingoneaic:tenants:tenant-localize
canonical_url: https://docs.pingidentity.com/pingoneaic/tenants/tenant-localize.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Tenants", "Setup &amp; Configuration"]
section_ids:
  translation-configuration-format: Translation configuration format
  translating-enum-values: enum labels and localization
  translation-process: Translation process
  example-of-translation-process-with-a-four-letter-locale: Example of translation process with a four-letter locale
  example-of-translation-process-with-a-two-letter-locale: Example of translation process with a two-letter locale
  rest-api: REST API
  create-or-replace-translation-configuration: Create or replace translation configuration
  view-translation-configuration: View translation configuration
  delete-translation-configuration: Delete translation configuration
---

# Localize tenant admin console and hosted pages

You can localize static content and server messages in the Advanced Identity Cloud admin, sign on, and end-user UIs using translation configuration. Translation configuration lets you define a locale-specific set of key/phrase translation pairs that override the default set of key/phrase pairs. You can override some or all of the default keys, in as many locales as you need. The translation configuration has an effect in all realms.

The Advanced Identity Cloud UIs try to find a translation configuration for the locale requested by the browser of a tenant administrator (admin UI) or an end user (login UI and end-user UI). If no locale is found, Advanced Identity Cloud defaults to using the `en` (English) locale.

To manage translation configuration, use the `/openidm/config/uilocale/*` endpoint in the REST API.

## Translation configuration format

The translation configuration format for each locale includes the following:

```json
{
  "admin": {      (1)
    "sideMenu": {
      "securityQuestions": "Translation for predefined 'securityQuestions' key" (2)
    },
    "overrides": {
      "EmailAddress": "Translation for literal phrase 'Email Address'",  (3)
      "Name": "Translation for literal word 'Name'",  (3)
      "Owners": "Translation for literal word 'Owners'",  (3)
      "AppLogoURI": "Translation for literal phrase 'App Logo URI'"  (3)
    }
  },
  "enduser": {  (1)
    "pages": {
      "dashboard": {
        "widgets": {
          "welcome": {
            "greeting": "Translation for predefined 'greeting' key"  (2)
          }
        }
      }
    },
    "overrides": {
      "FirstName": "Translation for literal phrase 'First Name'",  (3)
      "LastName": "Translation for literal phrase 'Last Name'"  (3)
    }
  },
  "login": {  (1)
    "login": {
      "next": "Translation for predefined 'next' key"  (2)
    },
    "overrides": {
      "UserName": "Translation for literal phrase 'User Name'",  (3)
      "Password": "Translation for literal phrase 'Password'",  (3)
      "UnabletoresumesessionItmayhaveexpired": "Translation for literal phrase 'Unable to resume session. It may have expired.'"  (3)
    }
  },
  "shared": {  (1)
    "sideMenu": {
      "dashboard": "Translation for predefined 'dashboard' key"  (2)
    }
  }
}
```

|       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| ----- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **1** | The [`admin`](https://github.com/ForgeRock/platform-ui/tree/master/packages/platform-admin), [`enduser`](https://github.com/ForgeRock/platform-ui/tree/master/packages/platform-enduser), [`login`](https://github.com/ForgeRock/platform-ui/tree/master/packages/platform-login), and [`shared`](https://github.com/ForgeRock/platform-ui/tree/master/packages/platform-shared) top-level blocks correspond to the names of their respective UI packages in GitHub.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| **2** | Key/phrase translation pairs with *predefined* keys.Key/phrase translation pairs represent all text output that Advanced Identity Cloud presents by default. They are predefined in the `en` locale translation files for each package:- <https://github.com/ForgeRock/platform-ui/blob/master/packages/platform-admin/src/locales/en.json>

- <https://github.com/ForgeRock/platform-ui/blob/master/packages/platform-enduser/src/locales/en.json>

- <https://github.com/ForgeRock/platform-ui/blob/master/packages/platform-login/src/locales/en.json>

- <https://github.com/ForgeRock/platform-ui/blob/master/packages/platform-shared/src/locales/en.json>Use the packages to find the default key/phrase translations so that you can define translations for your locale.	To create different translations in the admin, enduser, and login blocks for a key from the shared block, copy the JSON structure for the shared key into each of the admin, enduser, and login blocks. This overrides the key in the shared block.                                                                            |
| **3** | Key/phrase translation pairs with *literal* keys.Key/phrase translation pairs defined within an `overrides` block are not predefined. Instead, the key is made from a literal phrase with all non-alphanumeric characters (including underscores) stripped out.Define translation pairs with literal keys to be a catch-all solution for any UI phrases that have not been defined, or for any unlocalized phrases that come directly from the backend servers.The example under the `login` top-level block shows two literal keys that translate the placeholder text from input fields that are part of an authentication journey. This approach can be taken to translate server output from authentication messages and journey nodes. The example under the `enduser` top-level block shows a similar approach that translates output from end-user account pages.	You can also add an overrides block to the shared top-level block. This is particularly useful for providing user-friendly display names for enum values defined in managed object schemas. Learn more in enum labels and localization. |

### `enum` labels and localization

Managed objects can be defined with an `enum` (enumeration) property, which restricts possible values to a defined set of options. For example, a `flight` field could have `enum: ["flying", "landing", "lost"]`, a `shirtSize` field could have `enum: ["S", "M", "L", "XL"]`, or a `favoriteColor` field could have `"enum": ["red","green","blue"]`.

You can use the raw values from these `enum` lists (`lost`, `blue`, `XL`) as keys within an `overrides` block in the translation configuration. This allows you to provide more user-friendly display labels or localized translations when presented in the UI.

|   |                                                                                                                                                                                                                                                                                                                                                                                                        |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | Similar to defining the `enum` values themselves in the [managed object schema](../idm-objects/creating-modifying-managed-objects.html#enum-managed-object), providing these display labels and translations for `enum` values is currently an API-only operation. Currently, you can't use the Advanced Identity Cloud admin console or the IDM admin console to manage enum labels or localizations. |

Typically, these overrides are placed in the `shared.overrides` block if the labels need to be consistent across all UIs. However, they can be placed in a context-specific `overrides` block if a particular UI requires different labels for the same `enum` value.

Example setting English labels:

```bash
curl \
--header "Authorization: Bearer <access-token>" \
--header "Content-Type: application/json" \
--header "Accept-API-Version: resource=1.0" \
--request POST \
--data '{
  "_id": "uilocale/en",
  "shared": {
    "overrides": {
      "red": "Deep Red",
      "green": "Forest Green",
      "blue": "Ocean Blue"
    }
  }
}' \
"https://<tenant-env-fqdn>/openidm/config/uilocale/en"
{
  "_id": "uilocale/en",
  "_rev": "...",
  "shared": {
    "overrides": {
      "red": "Deep Red",
      "green": "Forest Green",
      "blue": "Ocean Blue"
    }
  }
}
```

Example setting German translations:

```bash
curl \
--header "Authorization: Bearer <access-token>" \
--header "Content-Type: application/json" \
--header "Accept-API-Version: resource=1.0" \
--request POST \
--data '{
  "_id": "uilocale/de",
  "shared": {
    "overrides": {
      "red": "Dunkel Rot",
      "green": "Wald Grün",
      "blue": "Meer Blau"
    }
  }
}' \
"https://<tenant-env-fqdn>/openidm/config/uilocale/de"
{
  "_id": "uilocale/de",
  "_rev": "...",
  "shared": {
    "overrides": {
      "red": "Dunkel Rot",
      "green": "Wald Grün",
      "blue": "Meer Blau"
    }
  }
}
```

## Translation process

The Advanced Identity Cloud admin, login, and end-user UIs use a process that translates each key/phrase pair in a particular order.

The translation process initially determines a primary locale using the requested language from a tenant administrator's browser (admin UI) or end user's browser (login UI and end-user UI). If the locale is a two-letter language locale (for example, `es`) and no translation is found using that locale, the process falls back to the default `en` locale. If the locale is a four-letter language and region locale (for example, `es-ar`) and no translation is found using that locale, the process first falls back to the parent two-letter language locale (for example, `es`) and if no translation is found using that locale, the process falls back to the default `en` locale.

### Example of translation process with a four-letter locale

An example of the translation process for a browser with a four-letter locale of `fr-ca` (French Canadian) is:

1. Attempt to use the primary `fr-ca` locale:

   Look for the translation key in any translation configuration for the `fr-ca` locale:\
   `https://<tenant-env-fqdn>/openidm/config/uilocale/fr-ca`

   If the translation configuration is not present, a `404` response is returned.

2. Fall back to the `fr` locale:

   Look for the translation key in any translation configuration for the `fr` locale:\
   `https://<tenant-env-fqdn>/openidm/config/uilocale/fr`

   If the translation configuration is not present, a `404` response is returned.

3. Fall back to the default `en` locale:

   1. Look for the translation key in any translation configuration for the `en` locale:\
      `https://<tenant-env-fqdn>/openidm/config/uilocale/en`

      If the translation configuration is not present, a `404` response is returned.

   2. Look for the translation key in the translation files for the `en` locale :

      * `platform-admin/src/locales/en.json`

      * `platform-enduser/src/locales/en.json`

      * `platform-login/src/locales/en.json`

      * `platform-shared/src/locales/en.json`

### Example of translation process with a two-letter locale

The translation process for a browser with a two-letter locale of `fr` (French) follows the same logic as in [Example of translation process with a four-letter locale](#example-of-translation-process-with-a-four-letter-locale), starting at step 2.

Suppress 404 responses

You may notice one or more `404` responses in the browser console for the `/openidm/config/uilocale/*` endpoint. These are expected and do not indicate a UI error; the `404` responses mean that the [translation process](#translation-process) cannot locate a translation configuration override, which is valid if you have not added one.

To suppress the `404` responses, [create a translation configuration](#create-or-replace-translation-configuration) with an empty body for each locale reporting a `404` response. The translation process will still work as expected with no loss of functionality, falling back through locales until it finds a translation for each key.

## REST API

### Create or replace translation configuration

1. Create an [access token](../developer-docs/authenticate-to-rest-api-with-access-token.html#get_an_access_token) for the realm where you want to apply the translation.

2. Create or replace the translation configuration for each locale:

   > **Collapse: Show request**
   >
   > ```none
   > $ curl \
   > --request PUT 'https://<tenant-env-fqdn>/openidm/config/uilocale/<locale>' \ (1) (2)
   > --header 'Authorization: Bearer <access-token>' \  (3)
   > --header 'Content-Type: application/json' \
   > --data-raw '{                                      (4)
   >   "admin": {
   >     "sideMenu": {
   >       "securityQuestions": "Questions de sécurité"
   >     },
   >     "overrides": {
   >       "EmailAddress": "Adresse e-mail",
   >       "Name": "Nom",
   >       "Owners": "Les propriétaires",
   >       "AppLogoURI": "URI du logo de l'application"
   >     }
   >   },
   >   "enduser": {
   >     "pages": {
   >       "dashboard": {
   >         "widgets": {
   >           "welcome": {
   >             "greeting": "Bonjour"
   >           }
   >         }
   >       }
   >     },
   >     "overrides": {
   >       "FirstName": "Prénom",
   >       "LastName": "Nom de famille"
   >     }
   >   },
   >   "login": {
   >     "login": {
   >       "next": "Suivant"
   >     },
   >     "overrides": {
   >       "UserName": "Nom d'\''utilisateur",
   >       "Password": "Mot de passe",
   >       "UnabletoresumesessionItmayhaveexpired": "Impossible de reprendre la session. Elle a peut-être expiré."
   >     }
   >   },
   >   "shared": {
   >     "sideMenu": {
   >       "dashboard": "Tableau de bord"
   >     }
   >   }
   > }'
   > ```
   >
   > |       |                                                                                                                                                                                                                                                                              |
   > | ----- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   > | **1** | Replace \<tenant-env-fqdn> with the domain of your development environment; for example, `openam-mycompany.forgeblocks.com`.                                                                                                                                                 |
   > | **2** | Replace \<locale> with a locale identifier. Some examples are:- `en` (English)
   >
   > - `es` (Spanish)
   >
   > - `fr` (French)
   >
   > - `en-us` (English - United States)
   >
   > - `es-ar` (Spanish - Argentina)
   >
   > - `fr-ca` (French - Canada)                                                         |
   > | **3** | Replace \<access-token> with the access token.                                                                                                                                                                                                                               |
   > | **4** | Replace the example translation configuration with your own translation configuration. Refer to [Translation configuration format](#translation-configuration-format) and [`enum` labels and localization](#translating-enum-values) for details on structuring the payload. |

   > **Collapse: Show response**
   >
   > ```json
   > {
   >   "_id": "uilocale/fr",
   >   "admin": {
   >     "sideMenu": {
   >       "securityQuestions": "Questions de sécurité"
   >     },
   >     "overrides": {
   >       "EmailAddress": "Adresse e-mail",
   >       "Name": "Nom",
   >       "Owners": "Les propriétaires",
   >       "AppLogoURI": "URI du logo de l'application"
   >     }
   >   },
   >   "enduser": {
   >     "pages": {
   >       "dashboard": {
   >         "widgets": {
   >           "welcome": {
   >             "greeting": "Bonjour"
   >           }
   >         }
   >       }
   >     },
   >     "overrides": {
   >       "FirstName": "Prénom",
   >       "LastName": "Nom de famille"
   >     }
   >   },
   >   "login": {
   >     "login": {
   >       "next": "Suivant"
   >     },
   >     "overrides": {
   >       "UserName": "Nom d'utilisateur",
   >       "Password": "Mot de passe",
   >       "UnabletoresumesessionItmayhaveexpired": "Impossible de reprendre la session. Elle a peut-être expiré."
   >     }
   >   },
   >   "shared": {
   >     "sideMenu": {
   >       "dashboard": "Tableau de bord"
   >     }
   >   }
   > }
   > ```

   |   |                                                                                                                                                                                                  |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
   |   | The locale you specify in the PUT request becomes the name of the corresponding backend JSON file. For example, if the locale you create is `fr`, then the backend JSON file would be `fr.json`. |

### View translation configuration

View the translation configuration using a GET request. You do not need an access token to view the translation configuration because it is publicly accessible.

> **Collapse: Show request**
>
> ```none
> $ curl \
> --request GET 'https://<tenant-env-fqdn>/openidm/config/uilocale/<locale>' (1) (2)
> ```
>
> |       |                                                                                                                              |
> | ----- | ---------------------------------------------------------------------------------------------------------------------------- |
> | **1** | Replace \<tenant-env-fqdn> with the domain of your development environment; for example, `openam-mycompany.forgeblocks.com`. |
> | **2** | Replace \<locale> with a locale identifier, such as `fr`.                                                                    |

> **Collapse: Show response**
>
> ```json
> {
>   "_id": "uilocale/fr",
>   "admin": {
>     "sideMenu": {
>       "securityQuestions": "Questions de sécurité"
>     },
>     "overrides": {
>       "EmailAddress": "Adresse e-mail",
>       "Name": "Nom",
>       "Owners": "Les propriétaires",
>       "AppLogoURI": "URI du logo de l'application"
>     }
>   },
>   "enduser": {
>     "pages": {
>       "dashboard": {
>         "widgets": {
>           "welcome": {
>             "greeting": "Bonjour"
>           }
>         }
>       }
>     },
>     "overrides": {
>       "FirstName": "Prénom",
>       "LastName": "Nom de famille"
>     }
>   },
>   "login": {
>     "login": {
>       "next": "Suivant"
>     },
>     "overrides": {
>       "UserName": "Nom d'utilisateur",
>       "Password": "Mot de passe",
>       "UnabletoresumesessionItmayhaveexpired": "Impossible de reprendre la session. Elle a peut-être expiré."
>     }
>   },
>   "shared": {
>     "sideMenu": {
>       "dashboard": "Tableau de bord"
>     }
>   }
> }
> ```

|   |                                                                                                                                                                                                                                         |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | When attempting to view the default `en` translation, no results are returned. To view the default `en` translation, learn more in the UI package files specified in [View translation configuration](#view-translation-configuration). |

\+ If you receive a `404` response, the locale is not defined. To create a locale, learn more in [Create or replace translation configuration](#create-or-replace-translation-configuration).

### Delete translation configuration

1. Create an [access token](../developer-docs/authenticate-to-rest-api-with-access-token.html#get_an_access_token) for the realm where the translations are applied.

2. Delete the translation configuration:

   > **Collapse: Show request**
   >
   > ```none
   > $ curl \
   > --request DELETE 'https://<tenant-env-fqdn>/openidm/config/uilocale/<locale>' \  (1) (2)
   > --header 'Authorization: Bearer <access-token>' (3)
   > ```
   >
   > |       |                                                                                                                              |
   > | ----- | ---------------------------------------------------------------------------------------------------------------------------- |
   > | **1** | Replace \<tenant-env-fqdn> with the domain of your development environment; for example, `openam-mycompany.forgeblocks.com`. |
   > | **2** | Replace \<locale> with a locale identifier, such as `fr`.                                                                    |
   > | **3** | Replace \<access-token> with the access token.                                                                               |

   > **Collapse: Show response**
   >
   > ```json
   > {
   >   "_id": "uilocale/fr",
   >   "admin": {
   >     "sideMenu": {
   >       "securityQuestions": "Questions de sécurité"
   >     },
   >     "overrides": {
   >       "EmailAddress": "Adresse e-mail",
   >       "Name": "Nom",
   >       "Owners": "Les propriétaires",
   >       "AppLogoURI": "URI du logo de l'application"
   >     }
   >   },
   >   "enduser": {
   >     "pages": {
   >       "dashboard": {
   >         "widgets": {
   >           "welcome": {
   >             "greeting": "Bonjour"
   >           }
   >         }
   >       }
   >     },
   >     "overrides": {
   >       "FirstName": "Prénom",
   >       "LastName": "Nom de famille"
   >     }
   >   },
   >   "login": {
   >     "login": {
   >       "next": "Suivant"
   >     },
   >     "overrides": {
   >       "UserName": "Nom d'utilisateur",
   >       "Password": "Mot de passe",
   >       "UnabletoresumesessionItmayhaveexpired": "Impossible de reprendre la session. Elle a peut-être expiré."
   >     }
   >   },
   >   "shared": {
   >     "sideMenu": {
   >       "dashboard": "Tableau de bord"
   >     }
   >   }
   > }
   > ```

---

---
title: Log sources
description: Advanced Identity Cloud makes browsing the audit and debug logs easier by storing them in various sources.
component: pingoneaic
page_id: pingoneaic:tenants:audit-debug-log-sources
canonical_url: https://docs.pingidentity.com/pingoneaic/tenants/audit-debug-log-sources.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Monitoring", "Tenants", "Troubleshooting"]
page_aliases: ["pingoneaic::audit-debug-logs.adoc#sources"]
section_ids:
  view_log_sources: View log sources
  log-source-descriptions: Log source descriptions
  am-sources: AM sources
  environment-access: Environment changes
  idm-sources: IDM sources
  ws-federation-sources: WS-Federation sources
---

# Log sources

Advanced Identity Cloud makes browsing the audit and debug logs easier by storing them in various sources.

## View log sources

|   |                                                                                                                                                   |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | You need to [get an API key and secret](../developer-docs/authenticate-to-rest-api-with-api-key-and-secret.html) before you can view log sources. |

To view a list of the available log sources, use the `/monitoring/logs/sources` endpoint.

Example request:

```bash
$ curl \
--request GET 'https://<tenant-env-fqdn>/monitoring/logs/sources' \
--header 'x-api-key: <api-key>' \
--header 'x-api-secret: <api-secret>'
```

Example response showing available sources in a `result` array:

```json
{
  "result": [
    "am-access", (1)
    "am-activity",
    "am-authentication",
    "am-config",
    "am-core",
    "am-everything",
    "environment-access", (2)
    "idm-access", (3)
    "idm-activity",
    "idm-authentication",
    "idm-config",
    "idm-core",
    "idm-everything",
    "idm-recon",
    "idm-sync",
    "ws-activity", (4)
    "ws-config",
    "ws-core",
    "ws-everything"
  ],
  "resultCount": 18,
  "pagedResultsCookie": null,
  "totalPagedResultsPolicy": "NONE",
  "totalPagedResults": 1,
  "remainingPagedResults": 0
}
```

|       |                                                                                                                                                             |
| ----- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **1** | Start of log sources for AM audit events. Learn more in [AM sources](#am-sources).                                                                          |
| **2** | Log source for environment configuration changes. Learn more in [Environment changes](#environment-access).                                                 |
| **3** | Start of log sources for IDM audit events. Learn more in [IDM sources](#idm-sources).                                                                       |
| **4** | Start of log sources for WS-Federation\[[1](#_footnotedef_1 "View footnote.")] audit events. Learn more in [WS-Federation sources](#ws-federation-sources). |

## Log source descriptions

### AM sources

| Source            | Type         | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| ----------------- | ------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| am-access         | Audit        | Captures all incoming Advanced Identity Cloud access calls as audit events. This includes who, what, when, and the output for every access request.Audit events:* AM-ACCESS-ATTEMPT

* AM-ACCESS-OUTCOME> **Collapse: Show example**
>
> ```json
> {
>   "payload": {
>     "_id": "92c9b6a4-f36f-438a-b1d4-c6e6bd909da6-783933",
>     "client": {
>       "ip": "198.51.101.0"
>     },
>     "component": "OAuth",
>     "eventName": "AM-ACCESS-ATTEMPT",
>     "http": {
>       "request": {
>         "headers": {
>           "content-type": [
>             "application/x-www-form-urlencoded"
>           ],
>           "host": [
>             "<tenant-env-fqdn>"
>           ],
>           "user-agent": [
>             "Apache-HttpClient/4.5.13 (Java/11.0.11)"
>           ],
>           "x-forwarded-for": [
>             "198.51.101.0, 203.0.116.0, 192.0.3.255"
>           ],
>           "x-forwarded-proto": [
>             "https"
>           ]
>         },
>         "method": "POST",
>         "path": "https://<tenant-env-fqdn>/am/oauth2/realms/root/realms/alpha/access_token",
>         "secure": true
>       }
>     },
>     "level": "INFO",
>     "realm": "/alpha",
>     "request": {
>       "detail": {
>         "client_id": "RCSClient",
>         "grant_type": "client_credentials",
>         "scope": "fr:idm:*"
>       }
>     },
>     "source": "audit",
>     "timestamp": "<dateTime>",
>     "topic": "access",
>     "transactionId": "1634116808645-2e50ecbf0df5407a6870-226587/0"
>   },
>   "timestamp": "<dateTime>",
>   "type": "application/json"
> }
> ```> **Collapse: Access log format**
>
> * `_id`
>
>   A universally unique identifier (UUID) for the message object, such as `a568d4fe-d655-49a8-8290-bfc02095bec9-491`.
>
> * `timestamp`
>
>   The timestamp when Advanced Identity Cloud logged the message, in UTC format to millisecond precision: `yyyy-MM-ddTHH:mm:ss.msZ`. For example: `2015-11-14T00:16:04.653Z`
>
> * `eventName`
>
>   The name of the audit event. For example, `AM-ACCESS-ATTEMPT` and `AM-ACCESS-OUTCOME`.
>
> * `transactionId`
>
>   The UUID of the transaction, which identifies an external request when it comes into the system boundary. Any events generated while handling that request are assigned that transaction ID, so you could see the same transaction ID for different audit event topics. For example, `9c9e8d5c-2941-4e61-9c3c-8a990088e801`.
>
> * `userId`
>
>   The universal identifier for authenticated users. For example, `id=scarter,ou=user,o=shop,ou=services,dc=example,dc=com`.
>
> * `trackingIds`
>
>   A unique random string generated as an alias for each Advanced Identity Cloud session ID and OAuth 2.0 token.
>
>   When Advanced Identity Cloud generates an access or grant token, it also generates a unique random value and logs it as an alias. In this way, you can trace an access token back to its originating grant token, trace the grant token back to the session in which it was created, and then trace how the session was authenticated. An example of a `trackingIds` property in an OAuth 2.0/OpenID Connect 1.0 environment is:
>
>   ```
>   [ "1979edf68543ead001", "8878e51a-f2aa-464f-b1cc-b12fd6daa415", "3df9a5c3-8d1e-4ee3-93d6-b9bbe58163bc" ]
>   ```
>
> * `client.host`
>
>   The client hostname. This field is populated only if reverse DNS lookup is enabled.
>
> * `client.ip`
>
>   The client IP address.
>
> * `client.port`
>
>   The client port number.
>
> * `request.protocol`
>
>   The protocol associated with the request operation.
>
>   Possible values: `CREST`, `PLL`, `SAML2`.
>
> * `request.operation`
>
>   The request operation. For common REST operations, possible values are: `READ`, `ACTION`, `QUERY`.
>
>   For PLL operations, possible values are: `LoginIndex`, `SubmitRequirements`, `GetSession`, `REQUEST_ADD_POLICY_LISTENER`.
>
> * `request.detail`
>
>   Detailed information about the request operation. For example:
>
>   * `{"action":"idFromSession"}`
>
>   * `{"action":"validateGoto"}`
>
>   * `{"action":"validate"}`
>
>   * `{"action":"logout"}`
>
>   * `{"action":"schema"}`
>
>   * `{"action":"template"}`
>
>   The following examples show different authentication flows:
>
>   * For an OAuth 2.0 app journey flow:
>
>     ```json
>     {
>         "oAuth2Client":"myClient",
>         "configuredService":"oauth2Tree"
>     }
>     ```
>
>   * For a SAML 2.0 app journey flow:
>
>     ```json
>     {
>         "spEntity":"serviceprovider1",
>         "idpEntity":"identityprovider1",
>         "configuredService":"samlTree"
>     }
>     ```
>
>   * For a SAML 2.0 flow where Advanced Identity Cloud is the hosted IdP and the user has successfully authenticated:
>
>     ```json
>     {
>       "spEntity": "serviceprovider1",
>       "flowInitiator": "IDP",
>       "idpEntity": "identityprovider1",
>       "userID": "id=bjensen,ou=user,o=alpha,ou=services,dc=example,dc=com",
>       "nameID": "V5Xa3AO+5xbxUfPSF73imsTYu3Rm"
>     }
>     ```
>
> * `http.method`
>
>   The HTTP method requested by the client. For example, `GET`, `POST`, `PUT`.
>
> * `http.path`
>
>   The path of the HTTP request; for example, `https://<tenant-env-fqdn>//am/json/realms/root/realms/alpha/authenticate`.
>
> * `http.queryParameters`
>
>   The HTTP query parameter string. For example:
>
>   * `{ "_action": [ "idFromSession" ] }`
>
>   * `{ "_queryFilter": [ "true" ] }`
>
>   * `{ "_action": [ "validate" ] }`
>
>   * `{ "_action": [ "logout" ] }`
>
>   * `{ "realm": [ "/shop" ] }`
>
>   * `{ "_action": [ "validateGoto" ] }`
>
> * `http.request.headers`
>
>   The HTTP header for the request.
>
>   > **Collapse: Example**
>   >
>   > ```json
>   > {
>   >     "accept": [
>   >         "application/json"
>   >     ],
>   >     "accept-api-version": [
>   >         "protocol=1.0,resource=2.1"
>   >     ],
>   >     "content-type": [
>   >         "application/json"
>   >     ],
>   >     "host": [
>   >         "example.forgeblocks.com"
>   >     ],
>   >     "origin": [
>   >         "https://example.forgeblocks.com"
>   >     ],
>   >     "user-agent": [
>   >         "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:120.0) Gecko/20100101 Firefox/120.0"
>   >     ],
>   >     "x-forwarded-for": [
>   >         "188.39.235.130, 34.117.102.58, 10.154.0.3"
>   >     ],
>   >     "x-forwarded-proto": [
>   >         "https"
>   >     ],
>   >     "x-requested-with": [
>   >         "forgerock-sdk"
>   >     ]
>   > }
>   > ```
>
> * `http.request.cookies`
>
>   A JSON map of key-value pairs and appears as its own property to allow for denylisting fields or values.
>
> * `http.response.cookies`
>
>   Not used in Advanced Identity Cloud.
>
> * `response.status`
>
>   The response status of the request. For example, `SUCCESS`, `FAILURE`, or null.
>
> * `response.statusCode`
>
>   The response status code, depending on the protocol. For common REST, HTTP failure codes are displayed but HTTP success codes aren't. For PLL endpoints, PLL error codes are displayed.
>
> * `response.detail`
>
>   The message associated with `response.statusCode`. For example, the `response.statusCode` of `401` has a `response.detail` of `{ "reason": "Unauthorized" }`.
>
> * `response.elapsedTime`
>
>   The time to execute the access event, usually in millisecond precision.
>
> * `response.elapsedTimeUnits`
>
>   The elapsed time units of the response. For example, `MILLISECONDS`.
>
> * `component`
>
>   The Advanced Identity Cloud service utilized; for example, `Server Info`, `Users`, `Config`, `Session`, `Authentication`, `Policy`, `OAuth`, `SAML2`, `Web Policy Agent`, or `Java Policy Agent`.
>
> * `realm`
>
>   The realm where the operation occurred. For example, (`"/alpha"`).> **Collapse: Show schema**
>
> ```json
> {
>   "access": {
>     "schema": {
>       "$schema": "http://json-schema.org/draft-04/schema#",
>       "id": "/",
>       "type": "object",
>       "properties": {
>         "_id": {
>           "description": "The unique identifier for the message object",
>           "type": "string"
>         },
>         "timestamp": {
>           "description": "The time at which the event occurred, used by all topics",
>           "type": "string"
>         },
>         "eventName": {
>           "description": "The name of the event, used by all topics",
>           "type": "string"
>         },
>         "transactionId": {
>           "description": "The transaction ID of the event, used by all topics",
>           "type": "string"
>         },
>         "userId": {
>           "description": "The ID of the user responsible for the event, used by all topics",
>           "type": "string"
>         },
>         "trackingIds": {
>           "description": "The tracking IDs of the event, used by all topics",
>           "type": "array",
>           "items": {
>             "id": "0",
>             "type": "string"
>           }
>         },
>         "server": {
>           "type": "object",
>           "properties": {
>             "ip": {
>               "description": "The server ip address for an access event.ip",
>               "type": "string"
>             },
>             "port": {
>               "description": "The server port for an access event",
>               "type": "integer"
>             }
>           }
>         },
>         "client": {
>           "type": "object",
>           "properties": {
>             "ip": {
>               "description": "The client IP address for an access event",
>               "type": "string"
>             },
>             "port": {
>               "description": "The client port for an access event",
>               "type": "integer"
>             }
>           }
>         },
>         "request": {
>           "type": "object",
>           "properties": {
>             "protocol": {
>               "description": "The request protocol for an access event",
>               "type": "string"
>             },
>             "operation": {
>               "description": "The operation that triggered an activity or config event",
>               "type": "string"
>             },
>             "detail": {
>               "description": "The request detail for an access event",
>               "type": "object"
>             }
>           }
>         },
>         "http": {
>           "type": "object",
>           "properties": {
>             "request": {
>               "description": "The http request for an access event",
>               "type": "object",
>               "properties": {
>                 "secure": {
>                   "description": "The http secure property for an access event",
>                   "type": "boolean"
>                 },
>                 "method": {
>                   "description": "The http method for an access event",
>                   "type": "string"
>                 },
>                 "path": {
>                   "description": "The http path for an access event",
>                   "type": "string"
>                 },
>                 "queryParameters": {
>                   "description": "Http query parameters",
>                   "type": "object",
>                   "additionalProperties": {
>                     "type": "array",
>                     "items": {
>                       "type": "string"
>                     }
>                   }
>                 },
>                 "headers": {
>                   "description": "The http headers for an access event",
>                   "type": "object",
>                   "additionalProperties": {
>                     "type": "array",
>                     "items": {
>                       "type": "string"
>                     }
>                   }
>                 },
>                 "cookies": {
>                   "description": "The http cookies for an access event",
>                   "type": "object",
>                   "additionalProperties": {
>                     "type": "string"
>                   }
>                 }
>               }
>             },
>             "response": {
>               "description": "The http response for an access event",
>               "type": "object",
>               "properties": {
>                 "headers": {
>                   "description": "The http request headers for an access event",
>                   "type": "object",
>                   "additionalProperties": {
>                     "type": "array",
>                     "items": {
>                       "type": "string"
>                     }
>                   }
>                 }
>               }
>             }
>           }
>         },
>         "response": {
>           "type": "object",
>           "properties": {
>             "status": {
>               "description": "The response status for an access event",
>               "type": "string"
>             },
>             "statusCode": {
>               "description": "The response status code for an access event",
>               "type": "string"
>             },
>             "detail": {
>               "description": "The response detail for an access event",
>               "type": "object"
>             },
>             "elapsedTime": {
>               "description": "The response elapsedTime for an access event",
>               "type": "integer"
>             },
>             "elapsedTimeUnits": {
>               "description": "The response elapsed time units for an access event",
>               "type": "string"
>             }
>           }
>         }
>       }
>     }
>   }
> }
> ``` |
| am-activity       | Audit        | Captures state changes to objects that were created, updated, or deleted by Advanced Identity Cloud end users. This includes session, user profile, and device profile changes.Audit events:* AM-SELFSERVICE-REGISTRATION-COMPLETED

* AM-SELFSERVICE-PASSWORDCHANGE-COMPLETED

* AM-SESSION-CREATED

* AM-SESSION-IDLE\_TIME\_OUT

* AM-SESSION-MAX\_TIMED\_OUT

* AM-SESSION-LOGGED\_OUT

* AM-SESSION-DESTROYED

* AM-SESSION-PROPERTY\_CHANGED

* AM-IDENTITY-CHANGE

* AM-GROUP-CHANGE> **Collapse: Show example**
>
> ```json
> {
>   "timestamp": "<dateTime>",
>   "payload": {
>     "_id": "3fc956b8-00a1-4e10-b8aa-72295d003bfb-195032",
>     "objectId": "3fc956b8-00a1-4e10-b8aa-72295d003bfb-195023",
>     "transactionId": "cf2a721c-9cec-4224-bdd1-3a33e1f8ed56/4",
>     "level": "INFO",
>     "eventName": "AM-SESSION-CREATED",
>     "timestamp": "<dateTime>",
>     "component": "Session",
>     "source": "audit",
>     "topic": "activity",
>     "trackingIds": [
>       "3fc956b8-00a1-4e10-b8aa-72295d003bfb-195023"
>     ],
>     "realm": "/",
>     "userId": "id=amadmin,ou=user,ou=am-config",
>     "runAs": "id=amadmin,ou=user,ou=am-config",
>     "operation": "CREATE"
>   },
>   "type": "application/json"
> }
> ```> **Collapse: Activity log format**
>
> * `_id`
>
>   A universally unique identifier (UUID) for the message object, such as `a568d4fe-d655-49a8-8290-bfc02095bec9-487`.
>
> * `changedFields`
>
>   Not used.
>
> * `component`
>
>   The Advanced Identity Cloud service utilized. For example, `Session` or `ID Repo`.
>
> * `eventName`
>
>   The name of the audit event. For example, `AM-SESSION_CREATED`, `AM-SESSION-LOGGED_OUT`, `AM-NEW-CONNECTION-FACTORY`.
>
> * `level`
>
>   The activity log level, `INFO` by default.
>
> * `objectId`
>
>   The unique identifier of the object that was created, updated, or deleted. For logging sessions, the session `trackingId` is used in this field.
>
> * `operation`
>
>   The stage change operation performed on the object. For example, `CREATE` or `UPDATE`.
>
> - `runAs`
>
>   The user to run the activity as, used in delegated administration.
>
> - `transactionId`
>
>   The UUID of the transaction, which identifies an external request when it comes into the system boundary. Any events generated while handling that request are assigned that transaction ID, so you could see the same transaction ID for different audit event topics. For example, `9c9e8d5c-2941-4e61-9c3c-8a990088e801`.
>
> - `trackingIds`
>
>   An array containing the following:
>
>   * A random context ID that identifies the session
>
>   * A random string generated from an OAuth 2.0/OIDC 1.0 flow that could track an access token ID or a grant token ID.
>
>   For example, `[ "c120669f-f636-467d-8da0-590d72aeaf08-181706" ]`.
>
> - `userId`
>
>   The universal identifier for authenticated users. For example, `id=fe32c8fe-38a2-4159-a220-9385350f3aca,ou=user,ou=am-config`.
>
> - `timestamp`
>
>   The timestamp when Advanced Identity Cloud logged the message, in UTC format to millisecond precision: `yyyy-MM-ddTHH:mm:ss.msZ`. For example: `2015-11-14T00:16:04.652Z`
>
> - `type`
>
>   The data type,`application/json` by default.
>
> - source\`
>
>   The source of these logs, `am-activity`.> **Collapse: Show schema**
>
> ```json
> {
>   "activity": {
>     "schema": {
>       "$schema": "http://json-schema.org/draft-04/schema#",
>       "id": "/",
>       "type": "object",
>       "properties": {
>         "_id": {
>           "description": "The unique identifier for the message object",
>           "type": "string"
>         },
>         "timestamp": {
>           "description": "The time at which the event occurred, used by all topics",
>           "type": "string"
>         },
>         "eventName": {
>           "description": "The name of the event, used by all topics",
>           "type": "string"
>         },
>         "transactionId": {
>           "description": "The transaction ID of the event, used by all topics",
>           "type": "string"
>         },
>         "userId": {
>           "description": "The ID of the user responsible for the event, used by all topics",
>           "type": "string"
>         },
>         "trackingIds": {
>           "description": "The tracking IDs of the event, used by all topics",
>           "type": "array",
>           "items": {
>             "id": "0",
>             "type": "string"
>           }
>         },
>         "runAs": {
>           "description": "What the change that triggered an activity or config event was run as",
>           "type": "string"
>         },
>         "objectId": {
>           "description": "The object ID of the change that triggered an activity or config event",
>           "type": "string"
>         },
>         "operation": {
>           "description": "The operation that triggered an activity or config event",
>           "type": "string"
>         },
>         "before": {
>           "description": "The state before an activity or config event occurred",
>           "type": "object"
>         },
>         "after": {
>           "description": "The state after an activity or config event occurred",
>           "type": "object"
>         },
>         "changedFields": {
>           "description": "The changed fields after an activity or config event occurred",
>           "type": "array",
>           "items": {
>             "id": "1",
>             "type": "string"
>           }
>         },
>         "revision": {
>           "description": "The revision for an activity or config event",
>           "type": "string"
>         }
>       }
>     }
>   }
> }
> ```                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| am-authentication | Audit        | Captures when and how a user authenticated and related audit events.Advanced Identity Cloud records an authentication audit event for each authentication node and the journey outcome. A node can provide extra data in the standard audit event, which is logged when an authentication node completes.Audit events:- AM-BACK-CHANNEL-INITIALIZE

- AM-LOGOUT

- AM-LOGIN-COMPLETED

- AM-NODE-LOGIN-COMPLETED

  Advanced Identity Cloud logs this audit event each time an authentication node completes.

  > **Collapse: Show example**
  >
  > ```json
  > {
  >   "type": "application/json",
  >   "timestamp": "<dateTime>",
  >   "payload": {
  >     "topic": "authentication",
  >     "eventName": "AM-NODE-LOGIN-COMPLETED",
  >     "transactionId": "ad56bedd-7dab-45d1-84d9-505b0b64fd6d/6",
  >     "principal": [
  >       "amadmin"
  >     ],
  >     "timestamp": "<dateTime>",
  >     "component": "Authentication",
  >     "source": "audit",
  >     "realm": "/",
  >     "entries": [
  >       {
  >         "info": {
  >           "authLevel": "0",
  >           "displayName": "Page Node",
  >           "nodeId": "83a9d86e-d6f5-11ea-87d0-0242ac130003",
  >           "nodeOutcome": "outcome",
  >           "treeName": "FRLogin",
  >           "nodeType": "PageNode"
  >         }
  >       }
  >     ],
  >     "level": "INFO",
  >     "trackingIds": [
  >       "3fc956b8-00a1-4e10-b8aa-72295d003bfb-184020"
  >     ],
  >     "_id": "3fc956b8-00a1-4e10-b8aa-72295d003bfb-184022"
  >   }
  > }
  > ```

- AM-TREE-LOGIN-STARTED

  * Disabled by default in Advanced Identity Cloud.

- AM-TREE-LOGIN-COMPLETED

  * If authentication completes successfully, the event has a `result` of `SUCCESS`.

  * If authentication fails, the event has a `result` of `FAILED`.

  * If the authentication ends in an *exception*, the event has a `result` of `FAILED` with the following additional field:

    ```bash
    exception: "An exception occurred during the authentication process"
    ```

    These exceptions let you troubleshoot authentication journeys that failed due to misconfiguration.Learn more about `am-authentication` properties in [Authentication log format](https://docs.pingidentity.com/pingam/8/security-guide/sec-maint-audit-ref.html#authentication-log-format).> **Collapse: Authentication log format**
>
> * `_id`
>
>   A universally unique identifier (UUID) for the message object, such as `a568d4fe-d655-49a8-8290-bfc02095bec9-485`.
>
> * `timestamp`
>
>   The timestamp when Advanced Identity Cloud logged the message, in UTC format to millisecond precision: `yyyy-MM-ddTHH:mm:ss.msZ`. For example: `2015-11-14T00:16:04.640Z`
>
> * `eventName`
>
>   The name of the audit event. For example, `AM-LOGOUT` and `AM-NODE-LOGIN-COMPLETED`.
>
> * `transactionId`
>
>   The UUID of the transaction, which identifies an external request when it comes into the system boundary. Any events generated while handling that request are assigned that transaction ID, so you could see the same transaction ID for different audit event topics. For example, `9c9e8d5c-2941-4e61-9c3c-8a990088e801`.
>
> * `user.id`
>
>   The universal identifier for authenticated users. For example, `id=scarter,ou=user,o=shop,ou=services,dc=example,dc=com`.
>
> * `trackingIds`
>
>   An array containing a unique random context ID.
>
>   * For OAuth 2.0/OIDC flows, this field identifies the session and a random string generated that can track an access token ID or a grant token ID.
>
>   * For authentication journeys, this field identifies the journey.
>
> * `result`
>
>   The result of the authentication journey. Possible values are `SUCCESSFUL` or `FAILED`.
>
> * `principal`
>
>   The array of accounts used to authenticate. For example `[ "tenantadmin" ]` or `[ "scarter" ]`.
>
> * `context`
>
>   Not used
>
> * `entries`
>
>   A JSON representation of the authentication journey or node. Advanced Identity Cloud creates an event as each node completes and a final event at the end of the journey.
>
>   Example:
>
>   ```json
>   {
>     "entries": [
>       {
>         "info": {
>           "nodeOutcome": "outcome",
>           "treeName": "ldapService",
>           "displayName": "User Name Collector",
>           "nodeType": "UsernameCollectorNode",
>           "nodeId": "cfcd2084-95d5-35ef-a6e7-dff9f98764db",
>           "version": "2.0",
>           "authLevel": "0"
>           }
>         }
>      ]
>   }
>   ```
>
>   The version is logged only for node versions greater than 1.0.
>
> * `component`
>
>   The Advanced Identity Cloud service utilized. For example, `Authentication`.
>
> * `realm`
>
>   The realm where the operation occurred. For example, (`"/alpha"`).> **Collapse: Show schema**
>
> ```json
> {
>   "authentication": {
>     "schema": {
>       "$schema": "http://json-schema.org/draft-04/schema#",
>       "id": "/",
>       "type": "object",
>       "properties": {
>         "_id": {
>           "description": "The unique identifier for the message object",
>           "type": "string"
>         },
>         "timestamp": {
>           "description": "The time at which the event occurred, used by all topics",
>           "type": "string"
>         },
>         "eventName": {
>           "description": "The name of the event, used by all topics",
>           "type": "string"
>         },
>         "transactionId": {
>           "description": "The transaction ID of the event, used by all topics",
>           "type": "string"
>         },
>         "userId": {
>           "description": "The ID of the user responsible for the event, used by all topics",
>           "type": "string"
>         },
>         "trackingIds": {
>           "description": "The tracking IDs of the event, used by all topics",
>           "type": "array",
>           "items": {
>             "id": "0",
>             "type": "string"
>           }
>         },
>         "result": {
>           "description": "The result of the authentication event",
>           "type": "string"
>         },
>         "principal": {
>           "description": "The principal responsible for the authentication event",
>           "type": "array",
>           "items": {
>             "type": "string"
>           }
>         },
>         "context": {
>           "description": "The context of an authentication event",
>           "type": "object",
>           "properties": {}
>         },
>         "entries": {
>           "description": "The entries for an authentication event",
>           "type": "array",
>           "items": {
>             "type": "object",
>             "properties": {
>               "moduleId": {
>                 "description": "The module ID for the authentication event",
>                 "type": "string"
>               },
>               "result": {
>                 "description": "The result of the module authentication event",
>                 "type": "string"
>               },
>               "info": {
>                 "description": "The entries information for an authentication event",
>                 "type": "object",
>                 "properties": {}
>               }
>             }
>           }
>         }
>       }
>     }
>   }
> }
> ```                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| am-config         | Audit        | Captures access management configuration changes for Advanced Identity Cloud with a timestamp and by whom.Configuration changes can only be performed in development environments, so these logs are empty in staging and production environments.Audit events:* AM-CONFIG-CHANGE> **Collapse: Show example**
>
> ```json
> {
>   "payload": {
>     "_id": "92c9b6a4-f36f-438a-b1d4-c6e6bd909da6-822860",
>     "eventName": "AM-CONFIG-CHANGE",
>     "level": "INFO",
>     "objectId": "ou=Office365,ou=dashboardApp,ou=default,ou=GlobalConfig,ou=1.0,ou=dashboardService,ou=services,ou=am-config",
>     "operation": "CREATE",
>     "runAs": "id=bd220328-9762-458b-b05a-982ac3c7fc54,ou=user,ou=am-config",
>     "source": "audit",
>     "timestamp": "<dateTime>",
>     "topic": "config",
>     "trackingIds": [
>       "92c9b6a4-f36f-438a-b1d4-c6e6bd909da6-821644"
>     ],
>     "transactionId": "1634122041174-2e50ecbf0df5407a6870-229391/0",
>     "userId": "id=bd220328-9762-458b-b05a-982ac3c7fc54,ou=user,ou=am-config"
>   },
>   "timestamp": "<dateTime>",
>   "type": "application/json"
> }
> ```> **Collapse: Config log format**
>
> * `_id`
>
>   A universally unique identifier (UUID) for the message object. For example, `6a568d4fe-d655-49a8-8290-bfc02095bec9-843`.
>
> * `timestamp`
>
>   The timestamp when Advanced Identity Cloud logged the message, in UTC format to millisecond precision: `yyyy-MM-ddTHH:mm:ss.msZ`. For example, `2015-11-14T00:21:03.490Z`
>
> * `eventName`
>
>   The name of the audit event. For example, `AM-CONFIG-CHANGE`.
>
> * `transactionId`
>
>   The UUID of the transaction, which identifies an external request when it comes into the system boundary. Any events generated while handling the request will be assigned that transaction ID, so you could see the same transaction ID for different audit event topics. For example, `301d1a6e-67f9-4e45-bfeb-5e4047a8b432`.
>
> * `user.id`
>
>   Not used.
>
>   You can determine the value for this field by linking to the access event using the same `transactionId`.
>
> * `trackingIds`
>
>   Not used.
>
> * `runAs`
>
>   The user to run the activity as. Can be used in delegated administration.
>
> * `objectId`
>
>   The identifier of a system object that has been created, modified, or deleted. For example, `ou=SamuelTwo,ou=default,ou=OrganizationConfig,ou=1.0, ou=iPlanetAMAuthSAML2Service,ou=services,o=shop,ou=services,dc=example,dc=com`.
>
> * `operation`
>
>   The state change operation invoked: `CREATE`, `MODIFY`, or `DELETE`.
>
> * `before`
>
>   The JSON representation of the object prior to the activity.
>
>   Example:
>
>   ```json
>   {
>      "sunsmspriority":[
>         "0"
>      ],
>      "objectclass":[
>         "top",
>         "sunServiceComponent",
>         "organizationalUnit"
>      ],
>      "ou":[
>         "SamuelTwo"
>      ],
>      "sunserviceID":[
>         "serverconfig"
>      ]
>   }
>   ```
>
> * `after`
>
>   The JSON representation of the object after the activity.
>
>   Example:
>
>   ```json
>   {
>    "sunKeyValue":[
>         "forgerock-am-auth-saml2-auth-level=0",
>         "forgerock-am-auth-saml2-meta-alias=/sp",
>         "forgerock-am-auth-saml2-entity-name=http://",
>         "forgerock-am-auth-saml2-authn-context-decl-ref=",
>         "forgerock-am-auth-saml2-force-authn=none",
>         "forgerock-am-auth-saml2-is-passive=none",
>         "forgerock-am-auth-saml2-login-chain=",
>         "forgerock-am-auth-saml2-auth-comparison=none",
>         "forgerock-am-auth-saml2-req-binding= urn:oasis:names:tc:SAML:2.0:bindings:HTTP-Redirect",
>         "forgerock-am-auth-saml2-binding= urn:oasis:names:tc:SAML:2.0:bindings:HTTP-Artifact",
>         "forgerock-am-auth-saml2-authn-context-class-ref=",
>         "forgerock-am-auth-saml2-slo-relay=http://",
>         "forgerock-am-auth-saml2-allow-create=false",
>         "forgerock-am-auth-saml2-name-id-format= urn:oasis:names:tc:SAML:2.0:nameid-format:persistent"
>      ]
>   }
>   ```
>
> * `changedFields`
>
>   The fields that were changed. For example, `[ "sunKeyValue" ]`.
>
> * `revision`
>
>   Not used.
>
> * `component`
>
>   Not used.
>
> * `realm`
>
>   The realm where the operation occurred. For example, (`"/alpha"`).> **Collapse: Show schema**
>
> ```json
> {
>   "config": {
>     "schema": {
>       "$schema": "http://json-schema.org/draft-04/schema#",
>       "id": "/",
>       "type": "object",
>       "properties": {
>         "_id": {
>           "description": "The unique identifier for the message object",
>           "type": "string"
>         },
>         "timestamp": {
>           "description": "The time at which the event occurred, used by all topics",
>           "type": "string"
>         },
>         "eventName": {
>           "description": "The name of the event, used by all topics",
>           "type": "string"
>         },
>         "transactionId": {
>           "description": "The transaction ID of the event, used by all topics",
>           "type": "string"
>         },
>         "userId": {
>           "description": "The ID of the user responsible for the event, used by all topics",
>           "type": "string"
>         },
>         "trackingIds": {
>           "description": "The tracking IDs of the event, used by all topics",
>           "type": "array",
>           "items": {
>             "id": "0",
>             "type": "string"
>           }
>         },
>         "runAs": {
>           "description": "What the change that triggered an activity or config event was run as",
>           "type": "string"
>         },
>         "objectId": {
>           "description": "The object ID of the change that triggered an activity or config event",
>           "type": "string"
>         },
>         "operation": {
>           "description": "The operation that triggered an activity or config event",
>           "type": "string"
>         },
>         "before": {
>           "description": "The state before an activity or config event occurred",
>           "type": "object"
>         },
>         "after": {
>           "description": "The state after an activity or config event occurred",
>           "type": "object"
>         },
>         "changedFields": {
>           "description": "The changed fields after an activity or config event occurred",
>           "type": "array",
>           "items": {
>             "id": "1",
>             "type": "string"
>           }
>         },
>         "revision": {
>           "description": "The revision for an activity or config event",
>           "type": "string"
>         }
>       }
>      }
>     }
>   }
> }
> ```                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| am-core           | Debug        | Captures access management debug logs for Advanced Identity Cloud. Use am-core when debugging anything in access management without capturing audit events. am-core also captures logging in authentication scripts.Development and sandbox environments provide DEBUG level logs, with logs in several areas tuned to INFO or WARNING.To reduce log volumes, staging and production environments only provide WARNING level logs and above.To troubleshoot and view the latest entries in the stored logs, you can tail am-core source. Learn more in [Tail logs](audit-debug-logs-pull.html#tail-logs).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| am-everything     | Audit, Debug | Captures all access management audit and debug logs for Advanced Identity Cloud.This includes all the logs captured in `am-access`, `am-activity`, `am-authentication`, `am-config`, and `am-core`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |

### Environment changes

| Source             | Type  | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| ------------------ | ----- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| environment-access | Audit | Captures all modifications made to the environment, including ESVs, promotions, and configuration changes, as audit events.This log source specifically covers Advanced Identity Cloud's core environment and doesn't include access logs from AM, IDM, or WS-Federation services.Audit events:* ENVIRONMENT-ACCESS-OUTCOME

* ESV-ACCESS-OUTCOME

* PROMO-ACCESS-OUTCOME

* LOG-ACCESS-OUTCOME> **Collapse: Show example**
>
> ```json
> {
>   "payload": {
>     "_id": "3fcd63b4-a139-423b-8b05-26dc1b635995",
>     "client": {
>       "ip": "10.67.67.63",
>       "port": "54056"
>     },
>     "eventName": "ENVIRONMENT-ACCESS-OUTCOME",
>     "http": {
>       "request": {
>         "headers": {
>           "accept": [
>             "/"
>           ],
>           "accept-encoding": [
>             "gzip,deflate"
>           ],
>           "user-agent": [
>             "node-fetch/1.0 (+https://github.com/bitinn/node-fetch)"
>           ]
>         },
>         "method": "GET",
>         "path": "http://org-environment.org-environment:8080/environment/custom-domains/alpha",
>         "secure": false
>       }
>     },
>     "msg": "",
>     "response": {
>       "elapsedTime": 43,
>       "elapsedTimeUnits": "MILLISECONDS",
>       "status": "SUCCESS",
>       "statusCode": 200
>     },
>     "server": {
>       "ip": "10.67.67.68",
>       "port": "8080"
>     },
>     "severity": "info",
>     "source": "audit",
>     "timestamp": "2025-10-30T13:53:35.30291233Z",
>     "topic": "access",
>     "transactionId": "529d242d-24f2-475f-b677-946130b93988/0/4"
>   },
>   "source": "environment-access",
>   "timestamp": "2025-10-30T13:53:35.30311657Z",
>   "type": "application/json"
> }
> ```> **Collapse: Log format**
>
> * `_id`
>
>   A universally unique identifier (UUID) for the message object, such as `e47da30d-5385-4db7-8ead-be6de7381a6a`.
>
> * `timestamp`
>
>   The timestamp when Advanced Identity Cloud logged the message, in UTC format to nanosecond precision: `yyyy-MM-ddTHH:mm:ss.SSSSSSSSSZ`. For example, `2025-11-03T12:17:36.533249455Z`
>
> * `eventName`
>
>   The name of the audit event. For example, `ENVIRONMENT-ACCESS-OUTCOME`, `PROMO-ACCESS-OUTCOME`, `ESV-ACCESS-OUTCOME`, or `LOG-ACCESS-OUTCOME`.
>
> * `transactionId`
>
>   The UUID of the transaction, which identifies an external request when it comes into the system boundary. Any events generated while handling that request are assigned that transaction ID, so you could see the same transaction ID for different audit event topics.
>
>   For example, `3a351e01-2eea-495d-b0ea-ede8888b7b17/0`. The first part is a unique ID for the entire transaction, while the `/0` suffix is an incrementing index for each event within that transaction.
>
> * `userId`
>
>   The identifier for the authenticated administrator who performed the action. For example, `4f01d1f4-9b22-4810-aff8-4335bc047e9c`.
>
> * `trackingIds`
>
>   A unique random identifier that links an administrative API call to the OAuth 2.0 bearer token used for authentication. This allows tracing an environment change back to the specific administrative session that authorized it. For example, `["3cfe01fe-d0d8-41d5-a6d2-c94718489294-1219818"]`.
>
> * `client.ip`
>
>   The client IP address from which the administrative request originated.
>
> * `client.port`
>
>   The client port number.
>
> * `request.detail`
>
>   Information about the request operation. For example, `"auth_type" : "bearer_token"`.
>
> * `http.method`
>
>   The HTTP method requested by the client. For example, `GET`, `POST`, `PUT`.
>
> * `http.path`
>
>   The path of the HTTP request. For example, `https://<tenant-env-fqdn>/environment/certificates`.
>
> * `http.queryParameters`
>
>   The HTTP query parameter string. For example:
>
>   * `{ "_onlyPending" : [ "false"] }`
>
>   * `{ "_action" : [ "create"] }`
>
> * `http.request.headers`
>
>   The HTTP header for the request.
>
>   > **Collapse: Example**
>   >
>   > ```json
>   > {
>   >     "accept": [
>   >         "application/json"
>   >     ],
>   >     "accept-api-version": [
>   >         "protocol=1.0,resource=1.0"
>   >     ],
>   >     "accept-encoding" : [
>   >         "gzip, deflate"
>   >    ],
>   >     "content-type": [
>   >         "application/json"
>   >     ],
>   >     "user-agent": [
>   >         "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36"
>   >     ],
>   >     "x-forwarded-for" : [
>   >         "146.200.129.107, 34.120.62.48"
>   >     ],
>   >     "x-forwarded-proto" : [
>   >         "https"
>   >     ],
>   >     "x-real-ip" : [
>   >       "146.200.129.105"
>   >     ]
>   > }
>   > ```
>
> * `response.elapsedTime`
>
>   The time to execute the access event, usually in millisecond precision.
>
> * `response.status`
>
>   The response status of the request. For example, `SUCCESS`, `FAILURE`, or null.
>
> * `response.statusCode`
>
>   The response status code, depending on the protocol. For example, `200` for success or `401` for unauthorized.
>
> * `response.elapsedTimeUnits`
>
>   The elapsed time units of the response. For example, `MILLISECONDS`.
>
> * `server.ip`
>
>   The server IP address.
>
> * `server.port`
>
>   The server port number. |

### IDM sources

| Source             | Type         | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| ------------------ | ------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| idm-access         | Audit        | Captures messages for the identity management REST endpoints and the invocation of scheduled tasks. This is the who, what, and output for every identity management access request in Advanced Identity Cloud.Audit events:* access> **Collapse: Show example**
>
> ```json
> {
>   "payload": {
>     "_id": "32c02w2f-bafe-4bdf-a8e1-1ce94813c46b-123717",
>     "client": {
>       "ip": "198.51.101.0",
>       "port": 60572
>     },
>     "eventName": "access",
>     "http": {
>       "request": {
>         "headers": {
>           "host": [
>             "<tenant-env-fqdn>:443"
>           ],
>           "user-agent": [
>             "Blackbox Exporter/0.25.0"
>           ],
>           "x-forwarded-for": [
>             "34.102.86.57, 34.97.113.137, 120.211.3.20"
>           ],
>           "x-forwarded-proto": [
>             "https"
>           ],
>           "x-real-ip": [
>             "34.102.86.57"
>           ]
>         },
>         "method": "GET",
>         "path": "https://<tenant-env-fqdn>/openidm/info/ping",
>         "secure": true
>       }
>     },
>     "level": "INFO",
>     "request": {
>       "operation": "READ",
>       "protocol": "CREST"
>     },
>     "response": {
>       "elapsedTime": 10,
>       "elapsedTimeUnits": "MILLISECONDS",
>       "status": "SUCCESSFUL",
>       "statusCode": "200"
>     },
>     "roles": [
>       "internal/role/openidm-reg"
>     ],
>     "server": {
>       "ip": "10.68.2.21",
>       "port": 8080
>     },
>     "source": "audit",
>     "timestamp": "dateTime",
>     "topic": "access",
>     "transactionId": "6b3a1cbb-523d-48ae-bd11-1aca4b65c294/0",
>     "userId": "anonymous"
>   },
>   "source": "idm-access",
>   "timestamp": "dateTime",
>   "type": "application/json"
> }
> ```> **Collapse: Show schema**
>
> IDM access logs use a base schema and add several identity management-specific fields.
>
> Base schema
>
> ```json
> {
>   "access": {
>     "schema": {
>       "$schema": "http://json-schema.org/draft-04/schema#",
>       "id": "/",
>       "type": "object",
>       "properties": {
>         "_id": {
>           "description": "The unique identifier for the message object",
>           "type": "string"
>         },
>         "timestamp": {
>           "description": "The time at which the event occurred, used by all topics",
>           "type": "string"
>         },
>         "eventName": {
>           "description": "The name of the event, used by all topics",
>           "type": "string"
>         },
>         "transactionId": {
>           "description": "The transaction ID of the event, used by all topics",
>           "type": "string"
>         },
>         "userId": {
>           "description": "The ID of the user responsible for the event, used by all topics",
>           "type": "string"
>         },
>         "trackingIds": {
>           "description": "The tracking IDs of the event, used by all topics",
>           "type": "array",
>           "items": {
>             "id": "0",
>             "type": "string"
>           }
>         },
>         "server": {
>           "type": "object",
>           "properties": {
>             "ip": {
>               "description": "The server ip address for an access event.ip",
>               "type": "string"
>             },
>             "port": {
>               "description": "The server port for an access event",
>               "type": "integer"
>             }
>           }
>         },
>         "client": {
>           "type": "object",
>           "properties": {
>             "ip": {
>               "description": "The client IP address for an access event",
>               "type": "string"
>             },
>             "port": {
>               "description": "The client port for an access event",
>               "type": "integer"
>             }
>           }
>         },
>         "request": {
>           "type": "object",
>           "properties": {
>             "protocol": {
>               "description": "The request protocol for an access event",
>               "type": "string"
>             },
>             "operation": {
>               "description": "The operation that triggered an activity or config event",
>               "type": "string"
>             },
>             "detail": {
>               "description": "The request detail for an access event",
>               "type": "object"
>             }
>           }
>         },
>         "http": {
>           "type": "object",
>           "properties": {
>             "request": {
>               "description": "The http request for an access event",
>               "type": "object",
>               "properties": {
>                 "secure": {
>                   "description": "The http secure property for an access event",
>                   "type": "boolean"
>                 },
>                 "method": {
>                   "description": "The http method for an access event",
>                   "type": "string"
>                 },
>                 "path": {
>                   "description": "The http path for an access event",
>                   "type": "string"
>                 },
>                 "queryParameters": {
>                   "description": "Http query parameters",
>                   "type": "object",
>                   "additionalProperties": {
>                     "type": "array",
>                     "items": {
>                       "type": "string"
>                     }
>                   }
>                 },
>                 "headers": {
>                   "description": "The http headers for an access event",
>                   "type": "object",
>                   "additionalProperties": {
>                     "type": "array",
>                     "items": {
>                       "type": "string"
>                     }
>                   }
>                 },
>                 "cookies": {
>                   "description": "The http cookies for an access event",
>                   "type": "object",
>                   "additionalProperties": {
>                     "type": "string"
>                   }
>                 }
>               }
>             },
>             "response": {
>               "description": "The http response for an access event",
>               "type": "object",
>               "properties": {
>                 "headers": {
>                   "description": "The http request headers for an access event",
>                   "type": "object",
>                   "additionalProperties": {
>                     "type": "array",
>                     "items": {
>                       "type": "string"
>                     }
>                   }
>                 }
>               }
>             }
>           }
>         },
>         "response": {
>           "type": "object",
>           "properties": {
>             "status": {
>               "description": "The response status for an access event",
>               "type": "string"
>             },
>             "statusCode": {
>               "description": "The response status code for an access event",
>               "type": "string"
>             },
>             "detail": {
>               "description": "The response detail for an access event",
>               "type": "object"
>             },
>             "elapsedTime": {
>               "description": "The response elapsedTime for an access event",
>               "type": "integer"
>             },
>             "elapsedTimeUnits": {
>               "description": "The response elapsed time units for an access event",
>               "type": "string"
>             }
>           }
>         }
>       }
>     }
>   }
> }
> ```
>
> Identity management schema extensions
>
> ```json
> {
>   "access": {
>     "schema": {
>       "$schema": "http://json-schema.org/draft-04/schema#",
>       "id": "/",
>       "type": "object",
>       "properties": {
>         "roles": {
>           "type": "array",
>           "items": {
>             "id": "0",
>             "type": "string"
>           }
>         }
>       }
>     }
>   }
> }
> ```Learn more about `idm-access` properties in [Access event topic properties](https://docs.pingidentity.com/pingidm/8/audit-guide/access-event-prop.html). |
| idm-activity       | Audit        | Captures operations on internal (managed) and external (system) objects in Advanced Identity Cloud. idm-activity logs the changes to identity content, such as adding or updating users and changing passwords.Audit events:* activity> **Collapse: Show example**
>
> ```json
> {
>   "timestamp": "<dateTime>",
>   "type": "application/json",
>   "payload": {
>     "_id": "eebf2abb-e4f1-428f-8fbb-8c18ed3f9559-218925",
>     "transactionId": "1630077288251-f5190abcb8c2d0d42c31-136380/0",
>     "message": "",
>     "timestamp": "<dateTime>",
>     "eventName": "activity",
>     "userId": "bd220328-9762-458b-b05a-982ac3c7fc54",
>     "revision": "00000000478fd92b",
>     "operation": "PATCH",
>     "changedFields": [],
>     "runAs": "bd220328-9762-458b-b05a-982ac3c7fc54",
>     "passwordChanged": true,
>     "status": "SUCCESS",
>     "objectId": "managed/alpha_user/e70c4476-1305-408a-9246-ac76c64ba039"
>   }
> }
> ```> **Collapse: Show schema**
>
> IDM activity logs use a base schema and add several identity management-specific fields.
>
> Base schema
>
> ```json
> {
>   "activity": {
>     "schema": {
>       "$schema": "http://json-schema.org/draft-04/schema#",
>       "id": "/",
>       "type": "object",
>       "properties": {
>         "_id": {
>           "description": "The unique identifier for the message object",
>           "type": "string"
>         },
>         "timestamp": {
>           "description": "The time at which the event occurred, used by all topics",
>           "type": "string"
>         },
>         "eventName": {
>           "description": "The name of the event, used by all topics",
>           "type": "string"
>         },
>         "transactionId": {
>           "description": "The transaction ID of the event, used by all topics",
>           "type": "string"
>         },
>         "userId": {
>           "description": "The ID of the user responsible for the event, used by all topics",
>           "type": "string"
>         },
>         "trackingIds": {
>           "description": "The tracking IDs of the event, used by all topics",
>           "type": "array",
>           "items": {
>             "id": "0",
>             "type": "string"
>           }
>         },
>         "runAs": {
>           "description": "What the change that triggered an activity or config event was run as",
>           "type": "string"
>         },
>         "objectId": {
>           "description": "The object ID of the change that triggered an activity or config event",
>           "type": "string"
>         },
>         "operation": {
>           "description": "The operation that triggered an activity or config event",
>           "type": "string"
>         },
>         "before": {
>           "description": "The state before an activity or config event occurred",
>           "type": "object"
>         },
>         "after": {
>           "description": "The state after an activity or config event occurred",
>           "type": "object"
>         },
>         "changedFields": {
>           "description": "The changed fields after an activity or config event occurred",
>           "type": "array",
>           "items": {
>             "id": "1",
>             "type": "string"
>           }
>         },
>         "revision": {
>           "description": "The revision for an activity or config event",
>           "type": "string"
>         }
>       }
>     }
>   }
> }
> ```
>
> Identity management schema extensions
>
> ```json
> {
>   "activity": {
>     "schema": {
>       "$schema": "http://json-schema.org/draft-04/schema#",
>       "id": "/",
>       "type": "object",
>       "properties": {
>         "status": {
>           "type": "string"
>         },
>         "message": {
>           "type": "string"
>         },
>         "passwordChanged": {
>           "type": "boolean"
>         },
>         "context": {
>           "type": "string"
>         },
>         "provider": {
>           "type": "string"
>         }
>       }
>     }
>   }
> }
> ```Learn more about `idm-activity` properties in [Activity event topic properties](https://docs.pingidentity.com/pingidm/8/audit-guide/activity-event-prop.html).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| idm-authentication | Audit        | Captures the results when authenticating to an `/openidm` endpoint to complete certain actions on an object.If an authentication session already exists in access management, authentication to identity management is not required. In this instance, the authentication logs would appear for am-authentication, with identity management logs in idm-access and idm-activity.Audit events:* authentication> **Collapse: Show schema**
>
> IDM authentication logs use a base schema and add several identity management-specific fields.
>
> Base schema
>
> ```json
> {
>   "authentication": {
>     "schema": {
>       "$schema": "http://json-schema.org/draft-04/schema#",
>       "id": "/",
>       "type": "object",
>       "properties": {
>         "_id": {
>           "description": "The unique identifier for the message object",
>           "type": "string"
>         },
>         "timestamp": {
>           "description": "The time at which the event occurred, used by all topics",
>           "type": "string"
>         },
>         "eventName": {
>           "description": "The name of the event, used by all topics",
>           "type": "string"
>         },
>         "transactionId": {
>           "description": "The transaction ID of the event, used by all topics",
>           "type": "string"
>         },
>         "userId": {
>           "description": "The ID of the user responsible for the event, used by all topics",
>           "type": "string"
>         },
>         "trackingIds": {
>           "description": "The tracking IDs of the event, used by all topics",
>           "type": "array",
>           "items": {
>             "id": "0",
>             "type": "string"
>           }
>         },
>         "result": {
>           "description": "The result of the authentication event",
>           "type": "string"
>         },
>         "principal": {
>           "description": "The principal responsible for the authentication event",
>           "type": "array",
>           "items": {
>             "type": "string"
>           }
>         },
>         "context": {
>           "description": "The context of an authentication event",
>           "type": "object",
>           "properties": {}
>         },
>         "entries": {
>           "description": "The entries for an authentication event",
>           "type": "array",
>           "items": {
>             "type": "object",
>             "properties": {
>               "moduleId": {
>                 "description": "The module ID for the authentication event",
>                 "type": "string"
>               },
>               "result": {
>                 "description": "The result of the module authentication event",
>                 "type": "string"
>               },
>               "info": {
>                 "description": "The entries information for an authentication event",
>                 "type": "object",
>                 "properties": {}
>               }
>             }
>           }
>         }
>       }
>     }
>   }
> }
> ```
>
> Identity management schema extensions
>
> ```json
> {
>   "authentication": {
>     "schema": {
>       "$schema": "http://json-schema.org/draft-04/schema#",
>       "id": "/",
>       "type": "object",
>       "properties": {
>         "provider": {
>           "type": "string"
>         },
>         "method": {
>           "type": "string"
>         }
>       }
>     }
>   }
> }
> ```Learn more about `idm-authentication` properties in [Authentication event topic properties](https://docs.pingidentity.com/pingidm/8/audit-guide/auth-event-prop.html).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| idm-config         | Audit        | Captures identity management configuration changes for Advanced Identity Cloud with a timestamp and by whom.Configuration changes can only be performed in development environments, so these logs are empty in staging and production environments.Audit events:* CONFIG> **Collapse: Show example**
>
> ```json
> {
>   "payload": {
>     "_id": "f6a3a7b2-aaf3-426d-a998-a970f84bdf4b-1519486",
>     "changedFields": [
>       "/mappings"
>     ],
>     "eventName": "CONFIG",
>     "objectId": "sync",
>     "operation": "UPDATE",
>     "revision": null,
>     "runAs": "bd220328-9762-458b-b05a-982ac3c7fc54",
>     "timestamp": "<dateTime>",
>     "transactionId": "1634054726312-2e50ecbf0df5407a6870-202437/0",
>     "userId": "bd220328-9762-458b-b05a-982ac3c7fc54"
>   }
> }
> ```> **Collapse: Show schema**
>
> ```json
> {
>   "config": {
>     "schema": {
>       "$schema": "http://json-schema.org/draft-04/schema#",
>       "id": "/",
>       "type": "object",
>       "properties": {
>         "_id": {
>           "description": "The unique identifier for the message object",
>           "type": "string"
>         },
>         "timestamp": {
>           "description": "The time at which the event occurred, used by all topics",
>           "type": "string"
>         },
>         "eventName": {
>           "description": "The name of the event, used by all topics",
>           "type": "string"
>         },
>         "transactionId": {
>           "description": "The transaction ID of the event, used by all topics",
>           "type": "string"
>         },
>         "userId": {
>           "description": "The ID of the user responsible for the event, used by all topics",
>           "type": "string"
>         },
>         "trackingIds": {
>           "description": "The tracking IDs of the event, used by all topics",
>           "type": "array",
>           "items": {
>             "id": "0",
>             "type": "string"
>           }
>         },
>         "runAs": {
>           "description": "What the change that triggered an activity or config event was run as",
>           "type": "string"
>         },
>         "objectId": {
>           "description": "The object ID of the change that triggered an activity or config event",
>           "type": "string"
>         },
>         "operation": {
>           "description": "The operation that triggered an activity or config event",
>           "type": "string"
>         },
>         "before": {
>           "description": "The state before an activity or config event occurred",
>           "type": "object"
>         },
>         "after": {
>           "description": "The state after an activity or config event occurred",
>           "type": "object"
>         },
>         "changedFields": {
>           "description": "The changed fields after an activity or config event occurred",
>           "type": "array",
>           "items": {
>             "id": "1",
>             "type": "string"
>           }
>         },
>         "revision": {
>           "description": "The revision for an activity or config event",
>           "type": "string"
>         }
>       }
>      }
>     }
>   }
> }
> ```Learn more about `idm-config` properties in [Configuration event topic properties](https://docs.pingidentity.com/pingidm/8/audit-guide/config-event-prop.html).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| idm-core           | Debug        | Captures identity management debug logs for Advanced Identity Cloud. Use idm-core when debugging anything in identity management without capturing audit events.Development and sandbox environments provide FINE level logs, with logs in several areas tuned to INFO, WARNING and SEVERE.To reduce log volumes, staging and production environments only provide INFO and WARNING level logs and above.To troubleshoot and view the latest entries in the stored logs, you can tail idm-core source. Learn more in [Tail logs](audit-debug-logs-pull.html#tail-logs).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| idm-everything     | Audit, Debug | Captures identity management audit and debug logs for Advanced Identity Cloud.This includes all the logs captured in `idm-access`, `idm-activity`, `idm-authentication`, `idm-config`, `idm-recon`, `idm-sync`, and `idm-core`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| idm-recon          | Audit        | Captures reconciliation events for Advanced Identity Cloud.The corresponding audit topic for idm-recon is disabled by default in Advanced Identity Cloud. For reconciliation events to appear in the audit logs, you must [enable the recon event handler](audit-debug-logs-pull.html#update-audit-configuration).> **Collapse: Show schema**
>
> ```json
> {
>   "recon": {
>     "schema": {
>       "$schema": "http://json-schema.org/draft-04/schema#",
>       "id": "/",
>       "type": "object",
>       "properties": {
>         "_id": {
>           "type": "string"
>         },
>         "transactionId": {
>           "type": "string"
>         },
>         "timestamp": {
>           "type": "string"
>         },
>         "eventName": {
>           "type": "string"
>         },
>         "userId": {
>           "type": "string"
>         },
>         "trackingIds": {
>           "type": "array",
>           "items": {
>             "id": "0",
>             "type": "string"
>           }
>         },
>         "action": {
>           "type": "string"
>         },
>         "exception": {
>           "type": "string"
>         },
>         "linkQualifier": {
>           "type": "string"
>         },
>         "mapping": {
>           "type": "string"
>         },
>         "message": {
>           "type": "string"
>         },
>         "messageDetail": {
>           "type": "object",
>           "properties": {}
>         },
>         "situation": {
>           "type": "string"
>         },
>         "sourceObjectId": {
>           "type": "string"
>         },
>         "sourceObject": {
>           "type": "object"
>         },
>         "status": {
>           "type": "string"
>         },
>         "targetObjectId": {
>           "type": "string"
>         },
>         "targetObject": {
>           "type": "object"
>         },
>         "reconciling": {
>           "type": "string"
>         },
>         "ambiguousTargetObjectIds": {
>           "type": "string"
>         },
>         "reconAction": {
>           "type": "string"
>         },
>         "entryType": {
>           "type": "string"
>         },
>         "reconId": {
>           "type": "string"
>         }
>       }
>     }
>   }
> }
> ```Learn more about `idm-recon` event properties in [Reconciliation event topic properties](https://docs.pingidentity.com/pingidm/8/audit-guide/recon-event-prop.html).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| idm-sync           | Audit        | Captures any changes to an object resulting in automatic sync (live sync and implicit sync) when a repository is mapped to Advanced Identity Cloud. This includes situations and the actions taken on each object, by account. The idm-activity log contains additional details about each action.> **Collapse: Show schema**
>
> ```json
> {
>   "sync": {
>     "schema": {
>       "$schema": "http://json-schema.org/draft-04/schema#",
>       "id": "/",
>       "type": "object",
>       "properties": {
>         "_id": {
>           "type": "string"
>         },
>         "transactionId": {
>           "type": "string"
>         },
>         "timestamp": {
>           "type": "string"
>         },
>         "eventName": {
>           "type": "string"
>         },
>         "userId": {
>           "type": "string"
>         },
>         "trackingIds": {
>           "type": "array",
>           "items": {
>             "id": "0",
>             "type": "string"
>           }
>         },
>         "action": {
>           "type": "string"
>         },
>         "exception": {
>           "type": "string"
>         },
>         "linkQualifier": {
>           "type": "string"
>         },
>         "mapping": {
>           "type": "string"
>         },
>         "message": {
>           "type": "string"
>         },
>         "messageDetail": {
>           "type": "object",
>           "properties": {}
>         },
>         "situation": {
>           "type": "string"
>         },
>         "sourceObjectId": {
>           "type": "string"
>         },
>         "sourceObject": {
>           "type": "object"
>         },
>         "status": {
>           "type": "string"
>         },
>         "targetObjectId": {
>           "type": "string"
>         },
>         "targetObject": {
>           "type": "object"
>         }
>       }
>     }
>   }
> }
> ```Learn more about `idm-sync` event properties in [Synchronization event topic properties](https://docs.pingidentity.com/pingidm/8/audit-guide/sync-event-prop.html).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |

### WS-Federation sources

The following log sources are available for WS-Federation\[[1](#_footnotedef_1 "View footnote.")]:

| Source        | Type         | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| ------------- | ------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ws-activity   | Audit        | Captures WS-Federation user authentication events.> **Collapse: Show example**
>
> ```json
> {
>     "payload": {
>         "client": {
>             "ip": "10.100.2.27"
>         },
>         "eventName": "AUTHN_ATTEMPT",
>         "logFile": "audit.log",
>         "request": {
>             "adapterId": "1731608547",
>             "connectionId": "urn:federation:MicrosoftOnline",
>             "protocol": "WSFED",
>             "role": "IdP"
>         },
>         "response": {
>             "elapsedTime": "399",
>             "elapsedTimeUnits": "MILLISECONDS",
>             "status": "inprogress"
>         },
>         "server": {
>             "hostname": "pingfederate-engine-bd49cb65d-kkqzc"
>         },
>         "source": "audit",
>         "timestamp": "2024-12-03T19:37:39.024Z",
>         "topic": "activity",
>         "trackingId": "tid:JmiM3ipvXOC809styOOD13BAfeM",
>         "transactionId": "f5f1cb6d-3899-4f45-b399-19253531de55/0"
>     },
>     "timestamp": "2024-12-03T19:37:39.024843174Z",
>     "type": "application/json",
>     "source": "ws-activity"
> }
> ```> **Collapse: Activity log format**
>
> * payload.client.ip
>
>   The client IP address.
>
> * payload.eventName
>
>   The name of the audit event (for example, `AUTHN_REQUEST`, `AUTHN_ATTEMPT`, `SSO`, `AUTHN_SESSION_CREATED`).
>
> * payload.request:
>
>   * adapterId
>
>     The adapter instance ID(s) that were invoked (for example, `1731608547`).
>
>   * app
>
>     The target application URL if available.
>
>   * connectionId
>
>     The federation realm ID (for example, `urn:federation:MicrosoftOnline`).
>
>   * protocol
>
>     The associated authentication protocol (`WSFED`).
>
>   * subject
>
>     The user name (for example, `bjensen@example.com`).
>
>   * role
>
>     The authentication role (`IdP`, `SP`).
>
> * payload.response:
>
>   * status
>
>     The status of the SSO request (`success`, `failure`, `inprogress`).
>
>   * detail
>
>     Additional description of the event if available.
>
>   * elapsedTime
>
>     The time to execute the access event, usually in millisecond precision (for example, `170`).
>
>   * elapsedTimeUnits
>
>     The elapsed time units of the response (for example, `MILLISECONDS`).
>
> * payload.server.hostname
>
>   The hostname of the PingFederate container (for example, `pingfederate-engine-bd49cb65d-kkqzc`).
>
> * payload.topic
>
>   A shortened version of this log source (`activity`).
>
> * payload.timestamp
>
>   The timestamp when Advanced Identity Cloud logged the event, in UTC format to millisecond precision: `yyyy-MM-ddTHH:mm:ss.msZ` (for example, `2015-11-14T00:16:04.653Z`).
>
> * payload.trackingId
>
>   A unique ID for a user session (for example, `tid:JmiM3ipvXOC809styOOD13BAfeM`).
>
> * payload.transactionId
>
>   The UUID of the transaction, which identifies an external request when it comes into the system boundary. Any events generated while handling that request are assigned that transaction ID, so you could see the same transaction ID for different audit event topics (for example, `f5f1cb6d-3899-4f45-b399-19253531de55/0`).
>
> * timestamp
>
>   Refer to the description of **payload.timestamp**.
>
> * type
>
>   The log format (for example, `application/json`).
>
> * source
>
>   This log source (`ws-activity`). |
| ws-config     | Audit        | Captures WS-Federation configuration change events.> **Collapse: Show example**
>
> ```json
> {
>     "payload": {
>         "client": {
>             "ip": "10.40.15.194"
>         },
>         "http": {
>             "request": {
>                 "method": "GET",
>                 "path": "/configArchive/export"
>             }
>         },
>         "logFile": "admin-api.log",
>         "request": {
>             "authType": "Bearer",
>             "partnerId": "pingfederate-resource-server",
>             "user": "pingfederate-resource-server"
>         },
>         "response": {
>             "statusCode": "200"
>         },
>         "source": "audit",
>         "timestamp": "2024-12-08T18:15:03.028Z",
>         "topic": "config"
>     },
>     "timestamp": "2024-12-08T18:15:03.02886768Z",
>     "type": "application/json",
>     "source": "ws-config"
> }
> ```> **Collapse: Configuration log format**
>
> * payload.client.ip
>
>   The client IP address.
>
> * payload.eventName
>
>   The name of the administrative event (for example, `EXPORT`).
>
> * payload.http.request:
>
>   * method
>
>     The HTTP method for the request (for example, `POST`).
>
>   * path
>
>     The endpoint of the HTTP request.
>
> * payload.logFile
>
>   The log file name that generated this log entry (for example, `admin-api.log` or `admin.log`).
>
> * payload.message
>
>   Additional information of the event if available.
>
> * payload.request:
>
>   * authType
>
>     The type of authentication used (`Basic`, `Bearer`).
>
>   * adminSessionId
>
>     The unique administrative session ID.
>
>   * component
>
>     The configuration component (for example, `CONFIG_ARCHIVE`).
>
>   * partnerId
>
>     The federation realm ID (for example, `urn:federation:MicrosoftOnline`).
>
>   * roles
>
>     The administrative roles associated with this user (for example, `UserAdmin`).
>
>   * user
>
>     The administrative username (for example, `pingfederate-resource-server`).
>
> * payload.response.statusCode
>
>   The HTTP status code for the response.
>
> * payload.timestamp
>
>   The timestamp when Advanced Identity Cloud logged the event, in UTC format to millisecond precision: `yyyy-MM-ddTHH:mm:ss.msZ` (for example, `2015-11-14T00:16:04.653Z`).
>
> * payload.topic
>
>   A shortened version of this log source (`config`).
>
> * timestamp
>
>   Refer to the description of **payload.timestamp**.
>
> * type
>
>   The log format (for example, `application/json`).
>
> * source
>
>   This log source (`ws-config`).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| ws-core       | Debug        | Captures WS-Federation error and debug events.> **Collapse: Show example**
>
> ```json
> {
>     "payload": {
>         "level": "INFO",
>         "logFile": "server.log",
>         "logger": "org.sourceid.websso.servlet.reqparam.ValidationHub",
>         "message": "Created 2 validators for parameter SpSessionAuthnAdapterId",
>         "timestamp": "2024-12-02T23:13:20.208Z"
>     },
>     "timestamp": "2024-12-02T23:13:20.209188799Z",
>     "type": "application/json",
>     "source": "ws-core"
> }
> ```> **Collapse: Core log format**
>
> * payload.level
>
>   The level of the error or debug event (`FATAL`, `ERROR`, `WARN`, `INFO`, `DEBUG`, `TRACE`).
>
> * payload.logFile
>
>   The log file name that generated this log entry (for example, `server.log`).
>
> * payload.logger
>
>   The Java class that generated this log entry (for example, `com.pingidentity.pf.admin.rest.filter.OAuth2AdminAuthHandler`).
>
> * payload.message
>
>   A description of the event.
>
> * payload.timestamp
>
>   The timestamp when Advanced Identity Cloud logged the event, in UTC format to millisecond precision: `yyyy-MM-ddTHH:mm:ss.msZ` (for example, `2015-11-14T00:16:04.653Z`).
>
> * timestamp
>
>   Refer to the description of **payload.timestamp**.
>
> * type
>
>   The log format (for example, `application/json`).
>
> * source
>
>   This log source (`ws-core`).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| ws-everything | Audit, Debug | Captures WS-Federation audit and debug logs for Advanced Identity Cloud.This includes all the logs captured in `ws-activity`, `ws-config`, and `ws-core`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |

***

[1](#_footnoteref_1). [WS-Federation/WS-Trust](../app-management/register-a-custom-application.html#sso-microsoft-365) is an [add-on capability](../product-information/add-on-capabilities.html).

---

---
title: Manage configuration placeholders using the admin console
description: PingOne Advanced Identity Cloud lets you add placeholders to your configuration so you can reference the value of an ESV variable or an ESV secret instead of defining a static value.
component: pingoneaic
page_id: pingoneaic:tenants:configuration-placeholders-ui
canonical_url: https://docs.pingidentity.com/pingoneaic/tenants/configuration-placeholders-ui.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  ui-support-for-configuration-placeholders: Admin console support for configuration placeholders
  add-a-configuration-placeholder-to-a-field: Add a configuration placeholder to a field
  delete-a-configuration-placeholder-for-a-field: Delete a configuration placeholder for a field
  placeholder-field-states: Placeholder field states
  insertable-placeholder-fields: Insertable
  read-only-placeholder-fields: Read-only
  key_value_field_conversion_example: Key-value field conversion example
---

# Manage configuration placeholders using the admin console

PingOne Advanced Identity Cloud lets you add placeholders to your configuration so you can reference the value of an [ESV variable](esvs.html#variables) or an [ESV secret](esvs.html#secrets) instead of defining a static value.

For example, if you created an ESV variable named `esv-ldap-minimum-password-length`, you could reference its value in a journey by adding the placeholder `&{esv.ldap.minimum.password.length}` to the Minimum Password Length field of an [LDAP Decision node](https://docs.pingidentity.com/auth-node-ref/latest/ldap-decision.html).

## Admin console support for configuration placeholders

The Advanced Identity Cloud admin console has full support for viewing and removing placeholders. However, it supports adding placeholders only to these features:

* Journeys

* Federation IdPs for tenant administrators

To add placeholders to configuration outside these areas, use the API. Learn more in [Manage configuration placeholders using the API](configuration-placeholders-api.html).

|   |                                                                                                                                                                                                                                                          |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | In some areas of the Advanced Identity Cloud admin console, entering a placeholder into a field makes the field read-only, and creates the impression that you can add a placeholder to the field. However, this isn't valid and won't work as expected. |

## Add a configuration placeholder to a field

|   |                                                                                                                                                                 |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | If you create a new ESV in a separate tab or window, you may also need to reload the page you are working on to display the new ESV in a field's variable list. |

1. (Optional) Create a new ESV by following steps 1a and 1b in [Set up configuration placeholders to reference an ESV](configuration-placeholders.html).

2. In the Advanced Identity Cloud admin console, identify the [insertable placeholder field](#insertable-placeholder-fields) to which you want to add a placeholder.

3. Click on the field's token icon ([icon: token, set=material, size=inline]).

4. The UI displays a list of ESVs with a compatible [variable expression type](esvs.html#variable-expression-types) for the field; for example, for a field that expects a boolean value, the list contains only ESV variables with a `bool` expression type:

   ![image$ui esv insertable placeholder list](_images/ui-esv-insertable-placeholder-list.png)

   |   |                                                                                                                                                                                          |
   | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | The UI combines ESV secrets and ESV variables of expression type `string` into one list. This combined list displays for password fields and for text fields that expect a string value. |

5. (Optional) To filter the ESVs displayed in the list, enter a value in the field with a search icon ([icon: search, set=material, size=inline]).

6. Select an ESV from the list.

7. The UI displays the selected placeholder and changes the field to a [read-only placeholder field](#read-only-placeholder-fields).

8. (Optional) To edit the placeholder:

   1. Click on the field's clear icon ([icon: close, set=material, size=inline]).

   2. The UI reverts the field to an [insertable placeholder field](#insertable-placeholder-fields).

   3. Repeat steps 2–7 above.

9. Save the page that contains the field. This adds the placeholder to your configuration.

## Delete a configuration placeholder for a field

1. In the Advanced Identity Cloud admin console, identify the [read-only placeholder field](#read-only-placeholder-fields) for which you want to delete a placeholder.

2. Click on the field's clear icon ([icon: close, set=material, size=inline]).

3. The UI reverts the field to an [insertable placeholder field](#insertable-placeholder-fields).

4. (Optional) Set a new regular input value for the field.

5. Save the page that contains the field. This removes the placeholder from your configuration and replaces it with a regular input value.

## Placeholder field states

### Insertable

Fields into which you can add a placeholder are *insertable*. If a field is insertable, a token icon ([icon: token, set=material, size=inline]) displays when you hover your cursor over the field or when you focus on the field:

* For text, password, select, and tag fields, the icon is displayed inside the field on the right-hand side:

  ![image$ui esv insertable placeholder input text](_images/ui-esv-insertable-placeholder-input-text.png)

* For checkboxes, the icon is displayed outside the field to the right-hand side:

  ![image$ui esv insertable placeholder input checkbox](_images/ui-esv-insertable-placeholder-input-checkbox.png)

* For key-value fields, the icon is displayed to the right-hand side of the key-value field name:

  ![image$ui esv insertable placeholder input key value](_images/ui-esv-insertable-placeholder-input-key-value.png)

Until you add a configuration placeholder, insertable placeholder fields behave the same as regular input fields.

### Read-only

When you add a configuration placeholder to a placeholder field, it becomes *read-only*:

* For text, password, select, and tag fields, the placeholder displays inside the field, the field is grayed out, and the field value cannot be edited. The only part of the field that is interactive is the field's clear icon ([icon: close, set=material, size=inline]) on the right-hand side:

  ![image$ui esv read only placeholder input text](_images/ui-esv-read-only-placeholder-input-text.png)

* For checkboxes, the checkbox is replaced with a read-only text field below the checkbox label:

  ![image$ui esv read only placeholder input checkbox](_images/ui-esv-read-only-placeholder-input-checkbox.png)

* For key-value fields, the field name, controls, and summary are replaced entirely with a read-only text field. The read-only text field includes the key-value field name above the placeholder:

  ![image$ui esv read only placeholder input key value](_images/ui-esv-read-only-placeholder-input-key-value.png)

## Key-value field conversion example

An example of a key-value field is the Page Header field in the Page Node.

The following screenshot shows the Page Header field populated with `en` and `fr` keys containing locale-specific messages:

![image$ui journeys page node page header modal](_images/ui-journeys-page-node-page-header-modal.png)

To convert this data to an ESV, use the `object` type ESV variable and set the value as a JSON object:

```none
{
    "en":"Sign in",
    "fr":"Se connecter"
}
```

---

---
title: Manage configuration placeholders using the API
description: PingOne Advanced Identity Cloud lets you add placeholders to your configuration so you can reference the value of an ESV variable or an ESV secret instead of defining a static value.
component: pingoneaic
page_id: pingoneaic:tenants:configuration-placeholders-api
canonical_url: https://docs.pingidentity.com/pingoneaic/tenants/configuration-placeholders-api.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  examples: Examples
  configure-tenant-email-provider: Insert ESV placeholders into tenant email provider configuration
  configure-cors: Insert ESV placeholders into CORS configuration
  configure-pingone-worker-service: Insert ESV placeholders into the secondary configuration of a PingOne worker service
  configure-a-journey-node: Insert ESV placeholders into journey node configuration
  configure-ldap-connector: Insert an ESV placeholder into an LDAP connector
---

# Manage configuration placeholders using the API

PingOne Advanced Identity Cloud lets you add placeholders to your configuration so you can reference the value of an [ESV variable](esvs.html#variables) or an [ESV secret](esvs.html#secrets) instead of defining a static value.

For example, if you created an ESV variable named `esv-email-provider-port`, you could reference its value by adding a placeholder of `{"$int" : "&{esv.email.provider.port}"}` to your configuration.

To set a default value in a configuration placeholder, include it after a vertical bar. For example, the following expression sets a default email provider port of 465: `{"$int" : "&{esv.email.provider.port|465}"}`. If no ESV is set, the default value of 465 is used instead.

If you add a placeholder to your configuration and do not set a corresponding ESV or specify a default value, you will not be able to complete a successful promotion.

A configuration property can include a mix of static values and placeholders. For example, if you set `esv-hostname` to `id`, then `&{esv.hostname}.example.com` evaluates to `id.example.com`.

## Examples

### Insert ESV placeholders into tenant email provider configuration

This example shows how to configure placeholders in your tenant email provider configuration. Learn more in [Email provider](email-provider.html).

|   |                                                                                                                                                  |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | The configuration is using an SMTP external email provider, but the same approach can be used to update an MS Graph API external email provider. |

1. [Get an access token](../developer-docs/authenticate-to-rest-api-with-access-token.html#get_an_access_token) that has the `fr:idm:*` scope.

2. Get the email provider configuration:

   > **Collapse: Show request**
   >
   > ```bash
   > $ curl \
   > --request GET 'https://<tenant-env-fqdn>/openidm/config/external.email' \(1)
   > --header 'Content-Type: application/json' \
   > --header 'Accept-API-Version: resource=1.0' \
   > --header 'Authorization: Bearer <access-token>'(2)
   > ```
   >
   > |       |                                                                      |
   > | ----- | -------------------------------------------------------------------- |
   > | **1** | Replace \<tenant-env-fqdn> with the FQDN of your tenant environment. |
   > | **2** | Replace \<access-token> with the access token created in step 1.     |

   > **Collapse: Show response**
   >
   > ```json
   > {
   >     "_id": "external.email",
   >     "auth": {
   >         "enable": true,
   >         "password": "changeit",
   >         "username": "example.user"
   >     },
   >     "connectiontimeout": 30000,
   >     "debug": false,
   >     "from": "\"Example User\" <example.user@example.com>",
   >     "host": "smtp.example.com",
   >     "port": 465,
   >     "smtpProperties": [],
   >     "ssl": {
   >         "enable": true
   >     },
   >     "starttls": {
   >         "enable": false
   >     },
   >     "threadPoolSize": 21,
   >     "timeout": 30000,
   >     "writetimeout": 30000
   > }
   > ```

3. Create a local copy of the email provider configuration from step 2, then substitute in ESV placeholders:

   ```json
   {
       "auth": {
           "enable": true,
           "password": "&{esv.email.provider.password}", (1)
           "username": "&{esv.email.provider.username}" (2)
       },
       "connectiontimeout": 30000,
       "debug": false,
       "from": "\"Example User\" <&{esv.email.provider.from.email}>", (3)
       "host": "&{esv.email.provider.host}", (4)
       "port": {
           "$int": "&{esv.email.provider.port}" (5)
       },
       "smtpProperties": [],
       "ssl": {
           "enable": {
               "$bool": "&{esv.email.provider.use.ssl}" (6)
           }
       },
       "starttls": {
           "enable": false
       },
       "threadPoolSize": 21,
       "timeout": 30000,
       "writetimeout": 30000
   }
   ```

   |       |                                                                      |
   | ----- | -------------------------------------------------------------------- |
   | **1** | Substitution for ESV placeholder `&{esv.email.provider.password}`.   |
   | **2** | Substitution for ESV placeholder `&{esv.email.provider.username}`.   |
   | **3** | Substitution for ESV placeholder `&{esv.email.provider.from.email}`. |
   | **4** | Substitution for ESV placeholder `&{esv.email.provider.host}`        |
   | **5** | Substitution for ESV placeholder `&{esv.email.provider.port}`.       |
   | **6** | Substitution for ESV placeholder `&{esv.email.provider.use.ssl}`.    |

   The following table summarizes the ESVs that correspond with the above placeholders:

   | ESV name                        | ESV type | Expression type | Example value             |
   | ------------------------------- | -------- | --------------- | ------------------------- |
   | `esv-email-provider-password`   | Secret   | n/a             |                           |
   | `esv-email-provider-username`   | Variable | String          | example.user              |
   | `esv-email-provider-from-email` | Variable | String          | example.user\@example.com |
   | `esv-email-provider-host`       | Variable | String          | smtp.example.com          |
   | `esv-email-provider-port`       | Variable | Integer         | 465                       |
   | `esv-email-provider-use-ssl`    | Variable | Boolean         | true                      |

4. Update the email provider configuration:

   > **Collapse: Show request**
   >
   > ```bash
   > $ curl \
   > --request PUT 'https://<tenant-env-fqdn>/openidm/config/external.email' \(1)
   > --header 'Content-Type: application/json' \
   > --header 'Accept-API-Version: resource=1.0' \
   > --header 'Authorization: Bearer <access-token>' \(2)
   > --data-raw '<email-provider-configuration>'(3)
   > ```
   >
   > |       |                                                                                                                     |
   > | ----- | ------------------------------------------------------------------------------------------------------------------- |
   > | **1** | Replace \<tenant-env-fqdn> with the FQDN of your tenant environment.                                                |
   > | **2** | Replace \<access-token> with the access token created in step 1.                                                    |
   > | **3** | Replace \<email-provider-configuration> with the local copy of the email-provider configuration modified in step 3. |

   > **Collapse: Show response**
   >
   > ```json
   > {
   >     "_id": "external.email",
   >     "auth": {
   >         "enable": true,
   >         "password": "&{esv.email.provider.password}",
   >         "username": "&{esv.email.provider.username}"
   >     },
   >     "connectiontimeout": 30000,
   >     "debug": false,
   >     "from": "\"Example User\" <&{esv.email.provider.from.email}>",
   >     "host": "&{esv.email.provider.host}",
   >     "port": {
   >         "$int": "&{esv.email.provider.port}"
   >     },
   >     "smtpProperties": [],
   >     "ssl": {
   >         "enable": {
   >             "$bool": "&{esv.email.provider.use.ssl}"
   >         }
   >     },
   >     "starttls": {
   >         "enable": false
   >     },
   >     "threadPoolSize": 20,
   >     "timeout": 30000,
   >     "writetimeout": 30000
   > }
   > ```

### Insert ESV placeholders into CORS configuration

This example shows how to configure placeholders in your tenant CORS configuration. Learn more in [Allow cross-domain requests with CORS](cors.html).

1. [Get an access token](../developer-docs/authenticate-to-rest-api-with-access-token.html#get_an_access_token) that has the `fr:am:*` scope.

2. Get the CORS configuration:

   > **Collapse: Show request**
   >
   > ```bash
   > $ curl \
   > --request POST 'https://<tenant-env-fqdn>/am/json/global-config/services/CorsService/?_action=nextdescendents' \(1)
   > --header 'Content-Type: application/json' \
   > --header 'Accept-API-Version: resource=1.0' \
   > --header 'Authorization: Bearer <access-token>'(2)
   > ```
   >
   > |       |                                                                      |
   > | ----- | -------------------------------------------------------------------- |
   > | **1** | Replace \<tenant-env-fqdn> with the FQDN of your tenant environment. |
   > | **2** | Replace \<access-token> with the access token created in step 1.     |

   > **Collapse: Show response**
   >
   > ```json
   > {
   >     "result": [
   >         {
   >             "maxAge": 600,
   >             "exposedHeaders": [],
   >             "acceptedHeaders": [
   >                 "accept-api-version",
   >                 "x-requested-with"
   >             ],
   >             "allowCredentials": true,
   >             "acceptedMethods": [
   >                 "GET",
   >                 "POST",
   >                 "PUT",
   >                 "DELETE"
   >             ],
   >             "acceptedOrigins": [
   >                 "https://example.org",
   >                 "https://example.com",
   >                 "https://openam-example.forgeblocks.com"
   >             ],
   >             "enabled": true,
   >             "_id": "example-cors-config", (1)
   >             "_type": {
   >                 "_id": "configuration",
   >                 "name": "Cors Configuration",
   >                 "collection": true
   >             }
   >         }
   >     ]
   > }
   > ```
   >
   > |       |                                                                                |
   > | ----- | ------------------------------------------------------------------------------ |
   > | **1** | The ID of the CORS configuration; in this example it is `example-cors-config`. |

3. Create a local copy of the CORS configuration from step 2, then substitute in an ESV placeholder:

   ```json
   {
       "maxAge": 600,
       "exposedHeaders": [],
       "acceptedHeaders": [
           "accept-api-version",
           "x-requested-with"
       ],
       "allowCredentials": true,
       "acceptedMethods": [
           "GET",
           "POST",
           "PUT",
           "DELETE"
       ],
       "acceptedOrigins": {
           "$array": "&{esv.cors.accepted.origins}" (1)
       },
       "enabled": true,
       "_id": "example-cors-config",
       "_type": {
           "_id": "configuration",
           "name": "Cors Configuration",
           "collection": true
       }
   }
   ```

   |       |                                                                  |
   | ----- | ---------------------------------------------------------------- |
   | **1** | Substitution for ESV placeholder `&{esv.cors.accepted.origins}`. |

   The following table summarizes the ESV that corresponds with the above placeholder:

   | ESV name                    | ESV type | Expression type | Example value                                                                              |
   | --------------------------- | -------- | --------------- | ------------------------------------------------------------------------------------------ |
   | `esv-cors-accepted-origins` | Variable | Array           | \["https\://example.org","https\://example.com","https\://openam-example.forgeblocks.com"] |

4. Update the CORS configuration:

   > **Collapse: Show request**
   >
   > ```bash
   > $ curl \
   > --request PUT 'https://<tenant-env-fqdn>/am/json/global-config/services/CorsService/configuration/<cors-id>' \(1)(2)
   > --header 'Content-Type: application/json' \
   > --header 'Accept-API-Version: resource=1.0' \
   > --header 'Authorization: Bearer <access-token>' \(3)
   > --data-raw '<cors-configuration>'(4)
   > ```
   >
   > |       |                                                                                                            |
   > | ----- | ---------------------------------------------------------------------------------------------------------- |
   > | **1** | Replace \<tenant-env-fqdn> with the FQDN of your tenant environment.                                       |
   > | **2** | Replace \<cors-id> with the CORS configuration ID you found in step 2. For example, `example-cors-config`. |
   > | **3** | Replace \<access-token> with the access token created in step 1.                                           |
   > | **4** | Replace \<cors-configuration> with the local copy of the CORS configuration modified in step 3.            |

   > **Collapse: Show response**
   >
   > ```json
   > {
   >     "_id": "example-cors-settings",
   >     "_rev": "1594160724",
   >     "maxAge": 600,
   >     "exposedHeaders": [],
   >     "acceptedHeaders": [
   >         "accept-api-version",
   >         "x-requested-with"
   >     ],
   >     "allowCredentials": true,
   >     "acceptedMethods": [
   >         "GET",
   >         "POST",
   >         "PUT",
   >         "DELETE"
   >     ],
   >     "acceptedOrigins": {
   >         "$array": "&{esv.cors.accepted.origins}"
   >     },
   >     "enabled": true,
   >     "_type": {
   >         "_id": "configuration",
   >         "name": "Cors Configuration",
   >         "collection": true
   >     }
   > }
   > ```

### Insert ESV placeholders into the secondary configuration of a PingOne worker service

This example shows how to configure placeholders in the secondary configuration of a PingOne worker service. Learn more in [Use PingOne Protect for risk-based authentication and fraud detection](../integrations/pingone-protect.html).

1. [Get an access token](../developer-docs/authenticate-to-rest-api-with-access-token.html#get_an_access_token) that has the `fr:am:*` scope.

2. Get the PingOne worker service secondary configurations:

   > **Collapse: Show request**
   >
   > ```bash
   > $ curl \
   > --request POST 'https://<tenant-env-fqdn>/am/json/realms/root/realms/alpha/realm-config/services/pingOneWorkerService?_action=nextdescendents' \(1)
   > --header 'Content-Type: application/json' \
   > --header 'Accept-API-Version: resource=1.0' \
   > --header 'Authorization: Bearer <access-token>'(2)
   > ```
   >
   > |       |                                                                      |
   > | ----- | -------------------------------------------------------------------- |
   > | **1** | Replace \<tenant-env-fqdn> with the FQDN of your tenant environment. |
   > | **2** | Replace \<access-token> with the access token created in step 1.     |

   > **Collapse: Show response**
   >
   > ```json
   > {
   >     "result": [
   >         {
   >             "clientId": "faa...3c0",
   >             "clientSecretPurpose": "pingoneworkeraic",
   >             "apiUrl": "https://api.pingone.eu/v1",
   >             "authUrl": "https://auth.pingone.eu",
   >             "environmentId": "219...43e",
   >             "_id": "PingOne Worker", (1)
   >             "_type": {
   >                 "_id": "workers",
   >                 "name": "PingOne Worker AIC",
   >                 "collection": true
   >             }
   >         }
   >     ]
   > }
   > ```
   >
   > |       |                                                                                                           |
   > | ----- | --------------------------------------------------------------------------------------------------------- |
   > | **1** | The ID of the PingOne worker service secondary configuration. In this example, it's `PingOne Worker AIC`. |

3. Create a local copy of the PingOne worker service secondary configuration from step 2, then substitute in ESV placeholders:

   ```json
   {
       "result": [
           {
               "clientId": "&{esv.pingone.worker.client.id}", (1)
               "clientSecretPurpose": "pingoneworkeraic",
               "apiUrl": "https://api.pingone.eu/v1",
               "authUrl": "https://auth.pingone.eu",
               "environmentId": "&{esv.pingone.environment.id}", (2)
               "_id": "PingOne Worker",
               "_type": {
                   "_id": "workers",
                   "name": "PingOne Worker AIC",
                   "collection": true
               }
           }
       ]
   }
   ```

   |       |                                                                     |
   | ----- | ------------------------------------------------------------------- |
   | **1** | Substitution for ESV placeholder `&{esv.pingone.worker.client.id}`. |
   | **2** | Substitution for ESV placeholder `&{esv.pingone.environment.id}`.   |

   The following table summarizes the ESVs that correspond with the above placeholders:

   | ESV name                       | ESV type | Expression type | Example value |
   | ------------------------------ | -------- | --------------- | ------------- |
   | `esv-pingone-worker-client-id` | Variable | String          | faa...3c0     |
   | `esv-pingone-environment-id`   | Variable | String          | 219...43e     |

4. Update the PingOne worker service secondary configuration:

   > **Collapse: Show request**
   >
   > ```bash
   > $ curl \
   > --request PUT 'https://<tenant-env-fqdn>/am/json/realms/root/realms/alpha/realm-config/services/pingOneWorkerService/workers/<pingone-worker-secondary-configuration-id>' \(1)(2)
   > --header 'Content-Type: application/json' \
   > --header 'Accept-API-Version: resource=1.0' \
   > --header 'Authorization: Bearer <access-token>' \(3)
   > --data-raw '<pingone-worker-secondary-configuration>'(4)
   > ```
   >
   > |       |                                                                                                                                                                                                             |
   > | ----- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   > | **1** | Replace \<tenant-env-fqdn> with the FQDN of your tenant environment.                                                                                                                                        |
   > | **2** | Replace \<pingone-worker-secondary-configuration-id> with the PingOne worker service configuration ID you found in step 2, ensuring that any spaces are URL encoded. For example, `PingOne%20Worker%20AIC`. |
   > | **3** | Replace \<access-token> with the access token created in step 1.                                                                                                                                            |
   > | **4** | Replace \<pingone-worker-secondary-configuration> with the local copy of the CORS configuration modified in step 3.                                                                                         |

   > **Collapse: Show response**
   >
   > ```json
   > {
   >     "clientId": "&{esv.pingone.worker.client.id}",
   >     "clientSecretPurpose": "pingoneworkeraic",
   >     "apiUrl": "https://api.pingone.eu/v1",
   >     "authUrl": "https://auth.pingone.eu",
   >     "environmentId": "&{esv.pingone.environment.id}",
   >     "_id": "PingOne Worker AIC",
   >     "_type": {
   >         "_id": "workers",
   >         "name": "PingOne Worker",
   >         "collection": true
   >     }
   > }
   > ```

### Insert ESV placeholders into journey node configuration

This example shows how to configure placeholders in an LDAP decision node, but the approach can be adapted to configure placeholders in any journey node.

1. [Get an access token](../developer-docs/authenticate-to-rest-api-with-access-token.html#get_an_access_token) that has the `fr:am:*` scope.

2. Get the configuration of the journey that contains the LDAP decision node so you can extract the ID of the node:

   > **Collapse: Show request**
   >
   > ```bash
   > $ curl \
   > --request GET 'https://<tenant-env-fqdn>/am/json/realms/root/realms/<realm>/realm-config/authentication/authenticationtrees/trees/<journey-name>' \(1)(2)(3)
   > --header 'Content-Type: application/json' \
   > --header 'Accept-API-Version: protocol=2.1,resource=3.0' \
   > --header 'Authorization: Bearer <access-token>'(4)
   > ```
   >
   > |       |                                                                                                                           |
   > | ----- | ------------------------------------------------------------------------------------------------------------------------- |
   > | **1** | Replace \<tenant-env-fqdn> with the FQDN of your tenant environment.                                                      |
   > | **2** | Replace \<realm> with the realm that contains the journey that contains the LDAP decision node. For example, `alpha`.     |
   > | **3** | Replace \<journey-name> with the name of the journey that contains the LDAP decision node. For example, `UpdatePassword`. |
   > | **4** | Replace \<access-token> with the access token created in step 1.                                                          |

   > **Collapse: Show response**
   >
   > ```json
   > {
   >     "_id": "ldapJourney",
   >     "_rev": "1341035508",
   >     "identityResource": "managed/alpha_user",
   >     "entryNodeId": "76e74888-73e1-46e2-aa33-5e4c8b07ccec",
   >     "innerTreeOnly": false,
   >     "noSession": false,
   >     "mustRun": false,
   >     "enabled": true,
   >     "transactionalOnly": false,
   >     "uiConfig": {
   >         "categories": "[]"
   >     },
   >     "nodes": {
   >         "76e74888-73e1-46e2-aa33-5e4c8b07ccec": {
   >             "displayName": "Page Node",
   >             "nodeType": "PageNode",
   >             "version": "1.0",
   >             "connections": {
   >                 "outcome": "c12abfe7-ae71-42e6-a6b3-e8f4d4d05549"
   >             }
   >         },
   >         "2082c1ad-f5ad-4b6d-aada-dd4fff4dc6f3": { (1)
   >             "displayName": "LDAP Decision",
   >             "nodeType": "LdapDecisionNode",
   >             "version": "1.0",  (2)
   >             "connections": {
   >                 "CANCELLED": "e301438c-0bd0-429c-ab0c-66126501069a",
   >                 "EXPIRED": "e301438c-0bd0-429c-ab0c-66126501069a",
   >                 "FALSE": "e301438c-0bd0-429c-ab0c-66126501069a",
   >                 "LOCKED": "e301438c-0bd0-429c-ab0c-66126501069a",
   >                 "TRUE": "70e691a5-1e33-4ac3-a356-e7b6d60d92e0"
   >             }
   >         }
   >     },
   >     "staticNodes": {
   >         "startNode": {
   >             "x": 50,
   >             "y": 250
   >         },
   >         "70e691a5-1e33-4ac3-a356-e7b6d60d92e0": {
   >             "x": 792,
   >             "y": 181
   >         },
   >         "e301438c-0bd0-429c-ab0c-66126501069a": {
   >             "x": 795,
   >             "y": 307
   >         }
   >     }
   > }
   > ```
   >
   > |       |                                                                                                      |
   > | ----- | ---------------------------------------------------------------------------------------------------- |
   > | **1** | The ID of the `LdapDecisionNode` node. In this example, it's `2082c1ad-f5ad-4b6d-aada-dd4fff4dc6f3`. |
   > | **2** | The version of the `LdapDecisionNode` node. In this example, it's `1.0`.                             |

3. Get the configuration of the LDAP decision node:

   > **Collapse: Show request**
   >
   > ```bash
   > $ curl \
   > --request GET 'https://<tenant-env-fqdn>/am/json/realms/root/realms/<realm>/realm-config/authentication/authenticationtrees/nodes/LdapDecisionNode/<node-version>/<node-id>' \(1)(2)(3)(4)(5)
   > --header 'Content-Type: application/json' \
   > --header 'Accept-API-Version: protocol=2.1,resource=3.0' \
   > --header 'Authorization: Bearer <access-token>'(6)
   > ```
   >
   > |       |                                                                                                                       |
   > | ----- | --------------------------------------------------------------------------------------------------------------------- |
   > | **1** | Replace \<tenant-env-fqdn> with the FQDN of your tenant environment.                                                  |
   > | **2** | Replace \<realm> with the realm that contains the journey that contains the LDAP decision node. For example, `alpha`. |
   > | **3** | The node name specified is `LdapDecisionNode`.                                                                        |
   > | **4** | Replace \<node-version> with the node version you found in step 2. For example, `1.0`.                                |
   > | **5** | Replace \<node-id> with the node ID you found in step 2. For example, `2082c1ad-f5ad-4b6d-aada-dd4fff4dc6f3`.         |
   > | **6** | Replace \<access-token> with the access token created in step 1.                                                      |

   > **Collapse: Show response**
   >
   > ```json
   > {
   >     "_id": "2082c1ad-f5ad-4b6d-aada-dd4fff4dc6f3",
   >     "_rev": "-752122233",
   >     "searchFilterAttributes": [
   >         "mail"
   >     ],
   >     "userProfileAttribute": "uid",
   >     "primaryServers": [
   >         "userstore-0.userstore:1389",
   >         "userstore-1.userstore:1389",
   >         "userstore-2.userstore:1389"
   >     ],
   >     "ldapConnectionMode": "LDAP",
   >     "trustAllServerCertificates": false,
   >     "heartbeatInterval": 10,
   >     "returnUserDn": true,
   >     "searchScope": "SUBTREE",
   >     "heartbeatTimeUnit": "SECONDS",
   >     "secondaryServers": [],
   >     "ldapOperationsTimeout": 0,
   >     "userCreationAttrs": [],
   >     "minimumPasswordLength": 8,
   >     "accountSearchBaseDn": [
   >         "o=example"
   >     ],
   >     "adminPassword": null,
   >     "adminDn": "uid=admin",
   >     "beheraEnabled": true,
   >     "_type": {
   >         "_id": "LdapDecisionNode",
   >         "name": "LDAP Decision",
   >         "collection": true,
   >         "version": "1.0"
   >     },
   >     "_outcomes": [
   >         {
   >             "id": "TRUE",
   >             "displayName": "True"
   >         },
   >         {
   >             "id": "FALSE",
   >             "displayName": "False"
   >         },
   >         {
   >             "id": "LOCKED",
   >             "displayName": "Locked"
   >         },
   >         {
   >             "id": "CANCELLED",
   >             "displayName": "Cancelled"
   >         },
   >         {
   >             "id": "EXPIRED",
   >             "displayName": "Expired"
   >         }
   >     ]
   > }
   > ```

4. Create a local copy of the node configuration from step 3, then substitute in ESV placeholders:

   ```json
   {
       "searchFilterAttributes": [
           "mail"
       ],
       "userProfileAttribute": "uid",
       "primaryServers" : {
           "$list": "&{esv.journey.ldap.primary.servers}" (1)
       },
       "ldapConnectionMode": "LDAP",
       "trustAllServerCertificates": false,
       "heartbeatInterval": {
           "$int": "&{esv.journey.ldap.heartbeat.interval}" (2)
       },
       "returnUserDn": true,
       "searchScope": "SUBTREE",
       "heartbeatTimeUnit": "&{esv.journey.ldap.heartbeat.unit}", (3)
       "secondaryServers": [],
       "ldapOperationsTimeout": 0,
       "userCreationAttrs": [],
       "minimumPasswordLength": 8,
       "accountSearchBaseDn": [
           "o=example"
       ],
       "adminPassword": {
           "$string": "&{esv.journey.ldap.password}" (4)
       },
       "adminDn": "&{esv.journey.ldap.username}", (5)
       "beheraEnabled": {
           "$bool": "&{esv.journey.ldap.behera.enabled}" (6)
       },
       "_type": {
           "_id": "LdapDecisionNode",
           "name": "LDAP Decision",
           "collection": true,
           "version": "1.0"
       },
       "_outcomes": [
           {
               "id": "TRUE",
               "displayName": "True"
           },
           {
               "id": "FALSE",
               "displayName": "False"
           },
           {
               "id": "LOCKED",
               "displayName": "Locked"
           },
           {
               "id": "CANCELLED",
               "displayName": "Cancelled"
           },
           {
               "id": "EXPIRED",
               "displayName": "Expired"
           }
       ]
   }
   ```

   |       |                                                                            |
   | ----- | -------------------------------------------------------------------------- |
   | **1** | Substitution for ESV placeholder `&{esv.journey.ldap.primary.servers}`.    |
   | **2** | Substitution for ESV placeholder `&{esv.journey.ldap.heartbeat.interval}`. |
   | **3** | Substitution for ESV placeholder `&{esv.journey.ldap.heartbeat.unit}`.     |
   | **4** | Substitution for ESV placeholder `&{esv.journey.ldap.password}`.           |
   | **5** | Substitution for ESV placeholder `&{esv.journey.ldap.username}`.           |
   | **6** | Substitution for ESV placeholder `&{esv.journey.ldap.behera.enabled}`.     |

   The following table summarizes the ESVs that correspond with the above placeholders:

   | ESV name                              | ESV type | Expression type | Example value                                                                    |
   | ------------------------------------- | -------- | --------------- | -------------------------------------------------------------------------------- |
   | `esv-journey-ldap-primary-servers`    | Variable | List            | userstore-0.userstore:1389,userstore-1.userstore:1389,userstore-2.userstore:1389 |
   | `esv-journey-ldap-heartbeat-interval` | Variable | Integer         | 10                                                                               |
   | `esv-journey-ldap-heartbeat-unit`     | Variable | String          | SECONDS                                                                          |
   | `esv-journey-ldap-password`           | Secret   | n/a             | changeit                                                                         |
   | `esv-journey-ldap-username`           | Variable | String          | uid=myadmin                                                                      |
   | `esv-journey-ldap-behera-enabled`     | Variable | Boolean         | false                                                                            |

5. Update the configuration of the LDAP decision node:

   > **Collapse: Show request**
   >
   > ```bash
   > $ curl \
   > --request PUT 'https://<tenant-env-fqdn>/am/json/realms/root/realms/<realm>/realm-config/authentication/authenticationtrees/nodes/LdapDecisionNode/<node-version>/<node-id>' \(1)(2)(3)(4)(5)
   > --header 'Content-Type: application/json' \
   > --header 'Accept-API-Version: protocol=2.1,resource=3.0' \
   > --header 'Authorization: Bearer <access-token>' \(6)
   > --data-raw '<node-configuration>'(7)
   > ```
   >
   > |       |                                                                                                                       |
   > | ----- | --------------------------------------------------------------------------------------------------------------------- |
   > | **1** | Replace \<tenant-env-fqdn> with the FQDN of your tenant environment.                                                  |
   > | **2** | Replace \<realm> with the realm that contains the journey that contains the LDAP decision node. For example, `alpha`. |
   > | **3** | The node name specified is `LdapDecisionNode`.                                                                        |
   > | **4** | Replace \<node-version> with the node version you found in step 2. For example, `1.0`.                                |
   > | **5** | Replace \<node-id> with the node ID you found in step 2. For example, `2082c1ad-f5ad-4b6d-aada-dd4fff4dc6f3`.         |
   > | **6** | Replace \<access-token> with the access token created in step 1.                                                      |
   > | **7** | Replace \<node-configuration> with the local copy of the node configuration modified in step 4.                       |

   > **Collapse: Show response**
   >
   > ```json
   > {
   >     "_id": "2082c1ad-f5ad-4b6d-aada-dd4fff4dc6f3",
   >     "_rev": "1359037709",
   >     "searchFilterAttributes": [
   >         "mail"
   >     ],
   >     "userProfileAttribute": "uid",
   >     "primaryServers": {
   >         "$list": "&{esv.journey.ldap.servers}"
   >     },
   >     "ldapConnectionMode": "LDAP",
   >     "trustAllServerCertificates": false,
   >     "heartbeatInterval": {
   >         "$int": "&{esv.journey.ldap.heartbeat.interval}"
   >     },
   >     "returnUserDn": true,
   >     "searchScope": "SUBTREE",
   >     "heartbeatTimeUnit": "&{esv.journey.ldap.heartbeat.unit}",
   >     "secondaryServers": [],
   >     "ldapOperationsTimeout": 0,
   >     "userCreationAttrs": [],
   >     "minimumPasswordLength": 8,
   >     "accountSearchBaseDn": [
   >         "o=example"
   >     ],
   >     "adminPassword": {
   >         "$string": "&{esv.journey.ldap.password}"
   >     },
   >     "adminDn": "&{esv.journey.ldap.username}",
   >     "beheraEnabled": {
   >         "$bool": "&{esv.journey.ldap.behera.enabled}"
   >     },
   >     "_type": {
   >         "_id": "LdapDecisionNode",
   >         "name": "LDAP Decision",
   >         "collection": true,
   >         "version": "1.0"
   >     },
   >     "_outcomes": [
   >         {
   >             "id": "TRUE",
   >             "displayName": "True"
   >         },
   >         {
   >             "id": "FALSE",
   >             "displayName": "False"
   >         },
   >         {
   >             "id": "LOCKED",
   >             "displayName": "Locked"
   >         },
   >         {
   >             "id": "CANCELLED",
   >             "displayName": "Cancelled"
   >         },
   >         {
   >             "id": "EXPIRED",
   >             "displayName": "Expired"
   >         }
   >     ]
   > }
   > ```

### Insert an ESV placeholder into an LDAP connector

This example shows how to configure a placeholder for an LDAP connector configured with the password for an LDAP server.

When a connector is created, Advanced Identity Cloud stores any secret or password in the connector's configuration as an encrypted object. If the encrypted object is promoted, it cannot be unencrypted in an upper environment because the encryption keys are different in each environment. Therefore, the encrypted object must be stored in an ESV secret and replaced in the configuration with an ESV placeholder.

1. [Get an access token](../developer-docs/authenticate-to-rest-api-with-access-token.html#get_an_access_token) that has the `fr:idm:*` scope.

2. Get the configuration of the LDAP connector:

   > **Collapse: Show request**
   >
   > ```bash
   > $ curl \
   > --request GET 'https://<tenant-env-fqdn>/openidm/config/provisioner.openicf/<connector-id>' \(1)(2)
   > --header 'Content-Type: application/json' \
   > --header 'Authorization: Bearer <access-token>'(3)
   > ```
   >
   > |       |                                                                                          |
   > | ----- | ---------------------------------------------------------------------------------------- |
   > | **1** | Replace \<tenant-env-fqdn> with the FQDN of your tenant environment.                     |
   > | **2** | Replace \<connector-id> with the name of your connector. For example, `myldapconnector`. |
   > | **3** | Replace \<access-token> with the access token created in step 1.                         |

   > **Collapse: Show response**
   >
   > ```json
   > {
   >   "_id": "provisioner.openicf/myldapconnector",
   >   "configurationProperties": {
   >     "accountObjectClasses": [
   >       "top",
   >       "person",
   >       "organizationalPerson",
   >       "inetOrgPerson"
   >     ],
   >     "accountSearchFilter": null,
   >     "accountSynchronizationFilter": null,
   >     "accountUserNameAttributes": [
   >       "uid"
   >     ],
   >     "attributesToSynchronize": [],
   >     "baseContexts": [
   >       "ou=identities"
   >     ],
   >     "baseContextsToSynchronize": [
   >       "ou=identities"
   >     ],
   >     "blockSize": "100",
   >     "changeLogBlockSize": "100",
   >     "changeNumberAttribute": "changeNumber",
   >     "credentials": { (1)
   >       "$crypto": {
   >         "type": "x-simple-encryption",
   >         "value": {
   >           "cipher": "AES/CBC/PKCS5Padding",
   >           "data": "hfJKTFhe+c6wozK/OEKMEw==",
   >           "iv": "G/1aF6oKS5/bzlkEzsmK0A==",
   >           "keySize": 16,
   >           "mac": "QSp/OAIEPWp9vkDhyZtK5Q==",
   >           "purpose": "idm.config.encryption",
   >           "salt": "6gSguT4PDQdKsPOrcItx7Q==",
   >           "stableId": "openidm-sym-default"
   >         }
   >       } (2)
   >     },
   >     "failover": [],
   >     "filterWithOrInsteadOfAnd": false,
   >     "groupMemberAttribute": "uniqueMember",
   >     "groupObjectClasses": [],
   >     "groupSearchFilter": null,
   >     ...
   >     },
   >   ...
   > }
   > ```
   >
   > |       |                                                                              |
   > | ----- | ---------------------------------------------------------------------------- |
   > | **1** | Opening bracket of the encrypted object containing the connector's password. |
   > | **2** | Closing bracket of the encrypted object containing the connector's password. |

3. Create a local copy of the connector configuration from step 2, then substitute in an ESV placeholder for the encrypted object:

   ```json
   {
     "_id": "provisioner.openicf/myldapconnector",
     "configurationProperties": {
       "accountObjectClasses": [
         "top",
         "person",
         "organizationalPerson",
         "inetOrgPerson"
       ],
       "accountSearchFilter": null,
       "accountSynchronizationFilter": null,
       "accountUserNameAttributes": [
         "uid"
       ],
       "attributesToSynchronize": [],
       "baseContexts": [
         "ou=identities"
       ],
       "baseContextsToSynchronize": [
         "ou=identities"
       ],
       "blockSize": "100",
       "changeLogBlockSize": "100",
       "changeNumberAttribute": "changeNumber",
       "credentials": "&{esv.connector.ldap.password}", (1)
       "failover": [],
       "filterWithOrInsteadOfAnd": false,
       "groupMemberAttribute": "uniqueMember",
       "groupObjectClasses": [],
       "groupSearchFilter": null,
       ...
       },
     ...
   }
   ```

   |       |                                                                                            |
   | ----- | ------------------------------------------------------------------------------------------ |
   | **1** | Substitution of ESV placeholder `&{esv.connector.ldap.password}` for the encrypted object. |

   The following table summarizes the ESV that corresponds with the above placeholder and contains the encrypted object from the connector configuration returned in step 2:

   | ESV name                      | ESV type | Expression type | Example value                                                                                                                                                                                                                                                                                                                |
   | ----------------------------- | -------- | --------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | `esv-connector-ldap-password` | Secret   | n/a             | {"$crypto": {"type": "x-simple-encryption", "value": {"cipher": "AES/CBC/PKCS5Padding", "data": "hfJKTFhe+c6wozK/OEKMEw==", "iv": "G/1aF6oKS5/bzlkEzsmK0A==", "keySize": 16, "mac": "QSp/OAIEPWp9vkDhyZtK5Q==", "purpose": "idm.config.encryption", "salt": "6gSguT4PDQdKsPOrcItx7Q==", "stableId": "openidm-sym-default"}}} |

4. Update the connector configuration:

   > **Collapse: Show request**
   >
   > ```bash
   > $ curl \
   > --request PUT 'https://<tenant-env-fqdn>/openidm/config/provisioner.openicf/<connector-id>' \(1)(2)
   > --header 'Content-Type: application/json' \
   > --header 'Authorization: Bearer <access-token>'\(3)
   > --data-raw '<connector-configuration>'(4)
   > ```
   >
   > |       |                                                                                                           |
   > | ----- | --------------------------------------------------------------------------------------------------------- |
   > | **1** | Replace \<tenant-env-fqdn> with the FQDN of your tenant environment.                                      |
   > | **2** | Replace \<connector-id> with the name of your connector. For example, `myldapconnector`.                  |
   > | **3** | Replace \<access-token> with the access token created in step 1.                                          |
   > | **4** | Replace \<connector-configuration> with the local copy of the connector configuration modified in step 3. |

   > **Collapse: Show response**
   >
   > ```json
   > {
   >   "_id": "provisioner.openicf/myldapconnector",
   >   "configurationProperties": {
   >     "accountObjectClasses": [
   >       "top",
   >       "person",
   >       "organizationalPerson",
   >       "inetOrgPerson"
   >     ],
   >     "accountSearchFilter": null,
   >     "accountSynchronizationFilter": null,
   >     "accountUserNameAttributes": [
   >       "uid"
   >     ],
   >     "attributesToSynchronize": [],
   >     "baseContexts": [
   >       "ou=identities"
   >     ],
   >     "baseContextsToSynchronize": [
   >       "ou=identities"
   >     ],
   >     "blockSize": "100",
   >     "changeLogBlockSize": "100",
   >     "changeNumberAttribute": "changeNumber",
   >     "credentials": "&{esv.connector.ldap.password}",
   >     "failover": [],
   >     "filterWithOrInsteadOfAnd": false,
   >     "groupMemberAttribute": "uniqueMember",
   >     "groupObjectClasses": [],
   >     "groupSearchFilter": null,
   >     ...
   >     },
   >   ...
   > }
   > ```