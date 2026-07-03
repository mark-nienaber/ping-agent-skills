---
title: Adding a decision endpoint
description: Add PingOne Authorize decision endpoints to expose authorization policies for evaluation.
component: pingone
page_id: pingone:authorization_using_pingone_authorize:p1az_adding_decision_endpoints
canonical_url: https://docs.pingidentity.com/pingone/authorization_using_pingone_authorize/p1az_adding_decision_endpoints.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 15, 2026
section_ids:
  steps: Steps
  result: Result:
---

# Adding a decision endpoint

Add PingOne Authorize endpoints for stages that align with your organization's policy deployment process.

## Steps

1. In the PingOne admin console, go to **Authorization > Decision Endpoints**.

2. Click **[icon: plus, set=fa]Add Endpoint**.

3. Enter an endpoint **Name** and a **Description** that reflects the endpoint's role in the deployment process.

   The maximum name length is 256 characters.

   ![Screen capture of the Creating New Decision Endpoint window.](_images/ttq1638497876819.png)

4. If you want to deploy a particular version of a policy to the endpoint, clear the **Use latest** checkbox and select the version in the **Policy Version** list.

   If you don't deploy a particular version, the endpoint uses the latest policy version. **Use latest** republishes the latest version each time a request is made to the endpoint and can cause a slower system response.

   |   |                                                                                |
   | - | ------------------------------------------------------------------------------ |
   |   | You should only enable **Use latest** during policy development and debugging. |

5. Select the **Record recent decisions** checkbox to keep track of the last 20 [recent decisions](p1az_recent_decisions.html) made for the endpoint during the last 24 hours.

   This allows you to visualize and examine recent decisions.

   |   |                                                                                                                       |
   | - | --------------------------------------------------------------------------------------------------------------------- |
   |   | This can cause a slower system response. You should only enable this setting during policy development and debugging. |

6. Click **Save**.

   ### Result:

   The new endpoint is added to the **Decision Endpoints** page. New endpoints are listed in alphabetical order after the three default endpoints.
