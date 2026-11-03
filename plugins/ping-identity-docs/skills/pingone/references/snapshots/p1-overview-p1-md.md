---
title: Overview page
description: The PingOne environment Overview page shows sign-on activity and enabled services.
component: pingone
page_id: pingone::p1_overview_p1
canonical_url: https://docs.pingidentity.com/pingone/p1_overview_p1.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-07-30T00:00:00Z
---

# Overview page

The **Overview** page in the PingOne admin console shows the environment name and ID, as well as a link to the **Environment Properties**.

The **Environment Capabilities** section lists the PingOne capabilities and connected products included in the environment. You can also [add capabilities](settings/p1_add_a_service.html) and configure single sign-on (SSO) connections to other Ping Identity products, such as PingOne Advanced Identity Cloud, PingFederate, and PingAccess from this page.

![A screen capture of the Overview page in the PingOne admin console.](_images/p1-admin-overview-pg.png)

To add a capability or SSO connection to your environment, click the **Plus** icon ([icon: plus, set=fa]) in the **Environment Capabilities** section. The **Add a Capability** list displays the available services and products that you can add to your environment.

![A screen capture of the Services section of the Overview page.](_images/p1-overview-pg-add-services.png)

Products that require additional configuration after they're added to your environment are listed in the **Optional Connections** section and include a **Not Set Up** label. Learn more in [Deploying products and services](getting_started_with_pingone/p1_deploy_products.html).

|   |                                                                                                                                                                                                                                                                      |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | To access detailed information about a service, click the capability name to open the [dashboard](monitoring/p1_dashboards.html) for the service. You can also view the dashboards by going to **Monitoring** and selecting the applicable dashboard in the sidebar. |