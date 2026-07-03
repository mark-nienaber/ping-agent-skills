---
title: Adding an API Proxy in Apigee
description: Configure the API Proxy where you want to reach a target endpoint.
component: pingaccess
version: 9.1
page_id: pingaccess:agents_and_integrations:pa_adding_an_api_proxy_in_apigee
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/agents_and_integrations/pa_adding_an_api_proxy_in_apigee.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 28, 2025
section_ids:
  steps: Steps
---

# Adding an API Proxy in Apigee

Configure the API Proxy where you want to reach a target endpoint.

## Steps

1. Go to **API Proxies > Create Proxy** and click the **Reverse Proxy** tab.

2. In the **Name** field, enter a name for the API proxy.

3. In the **Base Path** field, enter the base path of the API.

4. In the **Target (existing API)** field, enter the Uniform Resource Locator (URL) *(tooltip: \<div class="paragraph">
   \<p>Identifies a resource according to its internet location.\</p>
   \</div>)* of the service invoked by the proxy.

5. Click **Next**.

6. In the **Common Policies** section, select **Pass through (no authorization)**.

7. Click **Next**.

8. In the **Optional Deployment** section, select the deployment environment.

9. Click **Create and Deploy**.
