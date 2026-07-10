---
title: Developer Tools
description: Find developer tools, APIs, and integration resources for building with PingOne.
component: pingone
page_id: pingone:developer_tools:p1_dev_tools
canonical_url: https://docs.pingidentity.com/pingone/developer_tools/p1_dev_tools.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: February 8, 2024
---

# Developer Tools

Use the information in this section to find out more about developer tools, APIs, and integrating with other Ping Identity software.

* [PingOne Platform API Reference](p1_api_reference.html)

* [Tools for developers](p1_tools_for_devs.html)

* [Monitoring activity with Splunk](p1_monitor_activity_splunk.html)

* [Integrating with other Ping Identity software](p1_integrate_with_other_ping_software.html)

* [IP address and domain reference](p1_ip_address_domain_reference.html)

* [PingOne browser support](p1_browser_support.html)

---

---
title: Integrating with other Ping Identity software
description: Integrate PingOne with other Ping Identity software, including PingFederate for authentication and SSO, and PingDataSync for identity data synchronization.
component: pingone
page_id: pingone:developer_tools:p1_integrate_with_other_ping_software
canonical_url: https://docs.pingidentity.com/pingone/developer_tools/p1_integrate_with_other_ping_software.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 23, 2024
section_ids:
  pingfederate: PingFederate
  pingdatasync: PingDataSync
---

# Integrating with other Ping Identity software

PingOne can be integrated with other Ping Identity software, such as PingFederate and PingDataSync.

## PingFederate

PingFederate is an enterprise federation server that enables user authentication and single sign-on. It serves as a global authentication authority that allows employees, customers and partners to securely access all the applications they need from any device. PingFederate can connect to PingOne for identity and authentication services.

By sending transaction information and an optional device profile to PingOne when a user signs on, PingFederate can get a security risk assessment for the sign-on event. Including the risk assessment in your PingFederate authentication policy allows you to dynamically adjust the user's authentication requirements each time they sign on.

You can use PingFederate to retrieve user attributes from PingOne and validate user credentials when a user tries sign-on.

You can also use the PingFederate provisioning engine to manage users in PingOne.

Learn more about the integration kits in the following documentation:

* [PingOne Integration Kit](https://docs.pingidentity.com/integrations/pingone/pf_p1_ik.html)

* [PingOne MFA Integration Kit](https://docs.pingidentity.com/integrations/pingone/pingone_mfa_integration_kit/pf_p1_mfa_ik.html)

* [PingOne Protect Integration Kit](https://docs.pingidentity.com//integrations/pingone/pingone_protect_integration_kit/pf_p1_protect_ik.html)

## PingDataSync

You can use PingDataSync to synchronize PingDirectory Server with PingOne. Using data synchronization, you can:

* Unify identity data across multiple data sources.

* Migrate identity data with zero downtime.

* Keep passwords, credentials, and profiles up to date.

* Choose fast, one-time migrations or ongoing bi-directional synchronizations.

Learn more in the [PingDataSync Administration Guide](https://docs.pingidentity.com/pingdirectory/latest/pingdatasync_server_administration_guide/pd_sync_admin_guide.html).

---

---
title: IP address and domain reference
description: Configure your network rules for inbound and outbound traffic to ensure that PingOne works properly.
component: pingone
page_id: pingone:developer_tools:p1_ip_address_domain_reference
canonical_url: https://docs.pingidentity.com/pingone/developer_tools/p1_ip_address_domain_reference.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: December 6, 2024
section_ids:
  inbound: Inbound
  firewall-settings-for-end-users-accessing-pingone-from-your-network: Firewall settings for end users accessing PingOne from your network
  outbound: Outbound
---

# IP address and domain reference

Use the information in this section to configure your network rules for PingOne. For PingOne to function correctly, you might need to configure your network to allow appropriate inbound and outbound traffic.

## Inbound

PingOne provides services through several domains. The domains vary based on your organization's geography. These domains are for traffic inbound to PingOne.

Add the following domains to your allow list to ensure that the services are available.

| Geography                                                                   | Domain                                                                                                                                                                     |
| --------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Australia                                                                   | api.pingone.com.auapps.pingone.com.auassets.pingone.com.auauth.pingone.com.auconsole.pingone.com.auhttp-access-api.pingone.auuploads.pingone.com.auuploads2.pingone.com.au |
| Canada                                                                      | api.pingone.caapps.pingone.caassets.pingone.caauth.pingone.caconsole.pingone.cahttp-access-api.pingone.cauploads.pingone.cauploads2.pingone.ca                             |
| Europe                                                                      | api.pingone.euapps.pingone.euassets.pingone.euauth.pingone.euconsole.pingone.euhttp-access-api.pingone.euuploads.pingone.euuploads2.pingone.eu                             |
| North America (US)                                                          | api.pingone.comapps.pingone.comassets.pingone.comauth.pingone.comconsole.pingone.comhttp-access-api.pingone.comuploads.pingone.comuploads2.pingone.com                     |
| Singapore                                                                   | api.pingone.sgapps.pingone.sgassets.pingone.sgauth.pingone.sgconsole.pingone.sghttp-access-api.pingone.sguploads.pingone.sguploads2.pingone.sg                             |
| Asia Pacific (legacy)&#xA;&#xA;Available only for existing .asia customers. | api.pingone.asiaapps.pingone.asiaassets.pingone.asiaauth.pingone.asiaconsole.pingone.asiahttp-access-api.pingone.asiauploads.pingone.asiauploads2.pingone.asia             |

|   |                                                                                                                                                                                                                                                                                                    |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The http-access-api.pingone.\* domains handle requests from API gateway integration kits to PingOne Authorize API Access Management. Learn more about controlling access to your APIs in [API Access Management](../authorization_using_pingone_authorize/p1az_introduction.html#api-access-mgmt). |

## Firewall settings for end users accessing PingOne from your network

If your organization uses a firewall that restricts inbound traffic, follow the specific procedures for the operating system and the firewall you use to add the LaunchDarkly domain to the allow list. Adding this domain supports feature flag release management for early access or beta features in PingOne.

|   |                                                                                                         |
| - | ------------------------------------------------------------------------------------------------------- |
|   | End users accessing PingOne from outside your organization's network do not need to enable this domain. |

| Geography          | Domain           |
| ------------------ | ---------------- |
| North America - US | launchdarkly.com |

## Outbound

The static IP addresses listed in the Outbound section of the [PingOne IP Addresses](https://support.pingidentity.com/s/article/PingOne-IP-Addresses) article on the Ping Identity Support page are used for traffic outbound from PingOne to other services. They're geography-specific and not tied to individual PingOne environments. The static IP addresses are production NAT gateways in each geography that are used to send traffic for webhooks, provisioning, custom SMS, voice, or SMTP providers, and API calls made by PingOne DaVinci.

|   |                                                                                 |
| - | ------------------------------------------------------------------------------- |
|   | You might be prompted to sign on when accessing the Ping Identity Support page. |

Ensure that the static IP addresses are correctly tagged in your network infrastructure so they aren't inadvertently blocked.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Because PingOne operates as a multitenant platform, outbound requests from any environment might originate from the same shared, geography-specific IP addresses. Firewall or ingress controls based solely on the platform's static IP addresses should not be relied upon as a comprehensive security measure. These platform IP addresses are best leveraged for traffic identification, monitoring, and management, in conjunction with additional edge or ingress security controls. |

---

---
title: Monitoring activity with Splunk
description: Use Splunk to monitor PingOne activity data.
component: pingone
page_id: pingone:developer_tools:p1_monitor_activity_splunk
canonical_url: https://docs.pingidentity.com/pingone/developer_tools/p1_monitor_activity_splunk.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: April 23, 2025
page_aliases: ["p1_app_splunk_troubleshooting.adoc", "p1_splunk_app.adoc"]
section_ids:
  p1-add-splunk-app: Installing the PingOne App for Splunk
  before-you-begin: Before you begin
  about-this-task: About this task
  steps: Steps
  p1-splunk-troubleshoot: Troubleshooting the PingOne App for Splunk
  why-do-some-of-the-graphs-not-populate: Why do some of the graphs not populate?
  why-do-the-event-detail-charts-have-a-count-listed: Why do the Event Detail charts have a count listed?
  how-do-the-dashboard-table-fields-translate-from-pingone-webhook-json-data: How do the dashboard table fields translate from PingOne webhook JSON data?
  what-does-na-mean-when-populated-into-a-field-such-as-actor-actors-user-name: "What does \"N/A\" mean when populated into a field such as Actor (actors.user.name)?"
---

# Monitoring activity with Splunk

Use Splunk to monitor PingOne activity data.

## Installing the PingOne App for Splunk

The PingOne App for Splunk correlates your PingOne data into a meaningful dashboard. The app allows you to create custom dashboards and reporting, monitor activity data, and analyze event data over time.

### Before you begin

You must:

* Have a Splunk administrator account.

* [Create a webhook](../integrations/p1_create_webhook.html) to send your PingOne data to your Splunk instance. We recommend collecting the data in `index=pingone` so that the data model attached to the PingOne App for Splunk will automatically pick up the data.

  * Create a data input in Splunk to receive the webhook data from PingOne. In Splunk, click **Settings > Data inputs**.

  * For **HTTP Event Collector**, click **+Add new**. Send the data to `index=PingOne`. Make sure to copy the token provided by Splunk. Learn more in the [Splunk HTTP Event Collector](https://docs.splunk.com/Documentation/Splunk/latest/Data/UsetheHTTPEventCollector) documentation.

    ![A screen capture of the Splunk Index page with 'PingOne' as the selected index.](_images/uqb1675363189824.png)

    |   |                                                                                                                                          |
    | - | ---------------------------------------------------------------------------------------------------------------------------------------- |
    |   | To use a different index, refer to step 2 below to configure the PingOne App for Splunk to capture webhook data stored in other indexes. |

  * Create the webhook in PingOne and add a custom header, where you can enter the token provided by Splunk when you created the **HTTP Event Collector** input.

* Download the PingOne App for Splunk package in Splunkbase. Search for `PingOne` in Splunkbase to find the file.

### About this task

To install the [PingOne App for Splunk](https://splunkbase.splunk.com/app/6750):

### Steps

1. Sign on to Splunk and install the PingOne App for Splunk.

   1. Click **Apps > Manage Apps**.

   2. Click **Install app from file**.

      ![A screen capture of the Splunk Apps page with a red box around the Install app from file button.](_images/mwp1673286615442.png)

   3. To upload the PingOne App for Splunk package file, click **Browse**, select the file, and then click **Upload**.

      ![A screen capture of the Install App From File page in Splunk.](_images/smm1673287492338.png)

2. If your data is not in `index=pingone`, modify the macro to point to your data:

   1. Click **Settings > All configurations**.

      ![A screen capture of the Splunk Settings menu with a red box around All configurations.](_images/loq1673287883877.png)

   2. For the **App** field, filter on **PingOne App for Splunk** configurations and select the **PingOne\_data** macro.

      ![A screen capture of the Splunk All configurations page filtered on PingOne App For Splunk with a red box around the PingOne\_data macro.](_images/ssd1673288502247.png)

   3. To point the macro to your data, enter your index in the **Definition** box.

      The default is `index=PingOne`. Below is an example definition.

      ![A screen capture of an example index in the Definition box.](_images/stu1673289377506.png)

3. (Optional) Accelerate your data model to make a summary index of PingOne data.

   The summary index results in more efficient population of the dashboards and allows you to populate the tables over larger time ranges.

   1. Go to **Settings > Data models**.

      ![A screen capture of the Splunk Settings menu with a red box around Data mdoels.](_images/lrn1673290000178.png)

   2. Click **Edit > Edit Acceleration** for the PingOne data model.

      ![A screen capture of the Splunk Data Models page for the PingOne data model with the Edit menu open and a red box around Edit Acceleration.](_images/umg1673290334166.png)

   3. In the **Edit Acceleration** window, select the **Accelerate** checkbox.

   4. Select a **Summary Range**. Click **Save**.

      |   |                                                                                                                      |
      | - | -------------------------------------------------------------------------------------------------------------------- |
      |   | The dashboards only display accelerated data through the summary range selected, so choose a time range accordingly. |

      ![A screen capture of the Splunk Edit Acceleration window with the Accelerate check box selected and the Summary Range set to 3 Months.](_images/gak1673291190958.png)

   |   |                                                   |
   | - | ------------------------------------------------- |
   |   | It will take time for the summary index to build. |

## Troubleshooting the PingOne App for Splunk

See the following information for help troubleshooting the dashboards in the PingOne App for Splunk.

### Why do some of the graphs not populate?

If there are no results returned within the selected time range given, the dashboard widget shows as blank. If this activity is limited to one widget, such as a table or chart, on a dashboard, this likely means there were no relevant events to populate the chart.

### Why do the **Event Detail** charts have a count listed?

The data model collects aggregate data, which is used to populate the dashboards. Because the data collected are not raw log events, it's possible for multiple matching events to be aggregated. As an example, if a user account was unlocked 3 times in a second by the same administrator, the count value would be 3.

### How do the dashboard table fields translate from PingOne webhook JSON data?

In the PingOne App for Splunk prebuilt dashboards, the PingOne webhook JSON data translates to the following table headings.

| JSON Key                       | Field Name         |
| ------------------------------ | ------------------ |
| `action.type`                  | Action             |
| `result.description`           | Description        |
| `result.status`                | Status             |
| `actors.client.id`             | Client ID          |
| `actors.client.environment.id` | Environment ID     |
| `actors.client.name`           | Client Application |
| `actors.user.id`               | Actor ID           |
| `actors.user.name`             | Actor              |
| `resources.name`               | Target Resource    |
| `action.type`                  | Action             |

### What does "N/A" mean when populated into a field such as Actor (actors.user.name)?

In this case, "N/A" means that no value was included with the event. For instance, if the activity was performed by a worker app instead of a user account, the corresponding event data would have an N/A value in the dashboard results.

Certain dashboards allow you to filter N/A values in the results. For the **User Activity** dashboard:

* If **Filter No Actor** is set to `False`, N/A values are displayed.

  ![A screen capture of Filter No Actor set to False and the N/A values displaying in the chart.](_images/rur1673301795705.png)

* If **Filter No Actor** is set to `True`, N/A values will be removed from the results.

  ![A screen capture of Filter No Actor set to True and the N/A values not displaying in the chart.](_images/xps1673303026344.png)

---

---
title: PingOne browser support
description: PingOne supports the latest versions of Chrome, Firefox, Safari, and Edge.
component: pingone
page_id: pingone:developer_tools:p1_browser_support
canonical_url: https://docs.pingidentity.com/pingone/developer_tools/p1_browser_support.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: January 2, 2025
---

# PingOne browser support

PingOne is supported on the following browsers.

|   |                                                        |
| - | ------------------------------------------------------ |
|   | The minimum supported resolution is 1000 x 600 pixels. |

| Browser                     | Version                                                             |
| --------------------------- | ------------------------------------------------------------------- |
| Google Chrome               | Three most recent major versions                                    |
| Mozilla Firefox             | Three most recent major versions                                    |
| Apple Safari for MacOS      | Two most recent major versions                                      |
| Microsoft Edge              | Two most recent major versions                                      |
| Microsoft Internet Explorer | PingOne support for Internet Explorer 11 ended on January 31, 2023. |

|   |                                                                                                                                                                                                                                                                                                                                                                   |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | For PingOne to function properly, JavaScript must be enabled in the browser.Desktop applications that use embedded browsers are only supported if the embedded browser is supported. For example, some Windows applications use Internet Explorer as the embedded browser. Those applications aren't supported because PingOne doesn't support Internet Explorer. |

---

---
title: PingOne Platform API Reference
description: The PingOne API gives developers tools to manage users and integrate enterprise and third-party applications with PingOne.
component: pingone
page_id: pingone:developer_tools:p1_api_reference
canonical_url: https://docs.pingidentity.com/pingone/developer_tools/p1_api_reference.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: January 9, 2023
---

# PingOne Platform API Reference

The PingOne API gives developers the tools to manage users and integrate enterprise and third-party applications with the PingOne identity and application management platform.

You can find the PingOne Platform API Reference at <https://developer.pingidentity.com/pingone-api/platform/introduction.html>.

---

---
title: Tools for developers
description: Ping Identity provides developer tools, SDKs, and resources to integrate authentication and SSO services into your applications using PingOne.
component: pingone
page_id: pingone:developer_tools:p1_tools_for_devs
canonical_url: https://docs.pingidentity.com/pingone/developer_tools/p1_tools_for_devs.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: December 12, 2023
---

# Tools for developers

Ping Identity provides several tools that make it easy to get identity services such as authentication and SSO into your applications.

See the [Developer Tools](https://developer.pingidentity.com/en/tools.html) section in the [Ping Identity Developer](https://developer.pingidentity.com/) portal.

You can find the PingOne Native SDKs at [Native SDKs](https://developer.pingidentity.com/pingone-api/native-sdks/introduction.html).