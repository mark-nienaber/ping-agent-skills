---
title: Company Settings
description: You can view and modify environment-wide settings in DaVinci.
component: davinci
page_id: davinci:company_settings:davinci_company_settings
canonical_url: https://docs.pingidentity.com/davinci/company_settings/davinci_company_settings.html
llms_txt: https://docs.pingidentity.com/davinci/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 6, 2024
section_ids:
  viewing-company-information: Viewing company information
  changing-the-environment-name: Changing the environment name
  steps: Steps
  configuring-a-custom-domain: Configuring a custom domain
  steps-2: Steps
  managing-debug-logging: Managing debug logging
  about-this-task: About this task
  steps-3: Steps
  managing-multiple-flow-execution-settings: Managing multiple flow execution settings
---

# Company Settings

You can view and modify environment-wide settings in DaVinci.

## Viewing company information

View your company ID and JSON Web Key Set.

The **Company** tab displays the following parameters:

* **Company ID**: This is a unique identifier for your current environment. It is used for launching flows and for configuring PingOne to work with DaVinci.

* **JWKS**: This section displays the environment's JSON Web Key Set. It is used for launching flows.

## Changing the environment name

You can change the environment name that is displayed in the DaVinci user interface.

## Steps

1. Click the **Company** tab.

2. In the **Name** field, enter a name for your environment.

3. Click **Save**.

## Configuring a custom domain

Configure a domain for your company's DaVinci portal through PingOne.

## Steps

1. Sign on to your PingOne environment.

2. Create a custom domain according to the [Creating a Custom Domain in PingOne](https://docs.pingidentity.com/pingone/settings/p1_set_up_custom_domain.html) documentation.

3. If you are using the DaVinci external identity provider (IdP) in PingOne, update the URLs to use the new custom domain.

   1. Sign on to PingOne and go to **Integrations > External IDPs**.

   2. Open the PingOne DaVinci IdP, then click the **Pencil** icon.

   3. Click the **Connection** tab.

   4. Update the **Authorization Endpoint**, **Token Endpoint**, **JWKS Endpoint**, and **Issuer** fields to use the custom domain.

   5. Click **Save**.

## Managing debug logging

Enable or disable debug-level logging in your environment.

## About this task

Because debug logging can include sensitive information, its use may not be appropriate in your environment. When enabled, debug logging can be activated for any flow in its flow settings. When disabled, debug logging cannot be activated in any flow.

## Steps

1. Click the **Company** tab.

2. Select or deselect **Enable Analytics Debug View**.

3. Click **Save**.

## Managing multiple flow execution settings

You can manage DaVinci behavior when a user attempts to run multiple flows simultaneously.

* If multiple flow executions *aren't* allowed, when a user attempts to launch multiple flows, all of the flow executions fail.

* If multiple flow executions *are* allowed, when a user attempts to launch multiple flows, the first flow runs and other flows are paused. When the active flow execution ends, either because the flow completed successfully or because the tab was closed, the next flow executes.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Multiple flow executions aren't compatible with some flows and settings:* The **Multiple Sign-On Delay** feature in PingFederate cannot be used at the same time as this feature.

* Flows with external redirects, such as flows with external IdP providers or social login, will prevent other flows from pausing correctly.

* Flows launched with the widget can use this feature, but must use parameters to enable and configure it. Learn more in [Launching a flow with the widget](../integrating_flows_into_applications/davinci_launching_a_flow_with_the_widget.html). |

1. On the **Company** tab, select or clear **Allow Multiple Flow Executions in Browser**.

   1. (Optional) In the **Paused Flow Takeover Wait Time** field, enter a value in seconds to determine how long a paused flow waits to take over if the active flow unexpectedly ends. The minimum value is 3 and the maximum value is 15.

   2. (Optional) In the **Flow Lock Wait Timeout** field, enter a value in seconds to determine how long a flow can remain paused before it times out. The minimum value is 30 and the maximum value is 1200.

2. Click **Save**.