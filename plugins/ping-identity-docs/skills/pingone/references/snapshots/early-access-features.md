---
component: pingone
page_id: pingone:early-access-features:ea_p1_create_provisioning_connection_gateway
canonical_url: https://docs.pingidentity.com/pingone/early-access-features/ea_p1_create_provisioning_connection_gateway.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
---

---

---
title: Agent Detection (CUA) Dashboard (early access)
description: The Agent Detection (CUA) Dashboard shows a summary of computer-using agent (CUA) activity detected by PingOne Protect.
component: pingone
page_id: pingone:early-access-features:ea-p1_agent_detection_dashboard
canonical_url: https://docs.pingidentity.com/pingone/early-access-features/ea-p1_agent_detection_dashboard.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-10-29T16:49:34Z
section_ids:
  accessing-the-dashboard: Accessing the dashboard
  filters: Filters
  charts: Charts
  total-cua-detections: Total CUA Detections
  agent-detections-cua-over-time: Agent Detections (CUA) Over Time
  human-vs-cua-activity-over-time: Human vs. CUA Activity Over Time
  human-vs-cua-activity: Human vs. CUA Activity
  requests-by-agent: Requests by Agent
---

# Agent Detection (CUA) Dashboard (early access)

The **Agent Detection (CUA) Dashboard** is now available for early access in PingOne.

The **Agent Detection (CUA) Dashboard** shows a summary of computer-using agent (CUA) activity detected by PingOne Protect in the environment. Data in the dashboard is based on PingOne Protect risk evaluations using the Bot Detection predictor and its agent type detection capabilities. Learn more in [PingOne Protect Bot Detection predictor](../threat_protection_using_pingone_protect/p1_protect_risk_predictors.html#bot-detection).

The **Agent Detection (CUA) Dashboard** tracks transactions evaluated by PingOne Protect that result in a high score for artificial intelligence (AI)-based browser automation. You can use it to measure how effectively your configured PingOne Protect risk policies identify CUA activity across the environment. Metrics reflect only transactions evaluated by PingOne Protect, not all PingOne traffic.

|   |                                                                                                                                                                                                 |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | To populate the **Agent Detection (CUA) Dashboard**, you must:- Add PingOne Protect and PingOne DaVinci to your PingOne environment.

- Configure a DaVinci flow that includes PingOne Protect. |

## Accessing the dashboard

To access the **Authentication Dashboard**, in the PingOne admin console, go to **Monitoring > Agent Detection (CUA)**.

![A screenshot of the Agent Detection (CUA) Dashboard](_images/p1-agent-detection-dashboard.png)

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

|   |                                                                                   |
| - | --------------------------------------------------------------------------------- |
|   | The **Agent Detection (CUA) Dashboard** displays data only for the past 6 months. |

## Charts

Use the following controls to adjust the charts:

| Icon                                                                | Name         | Description                                                                                                                                                                                       |
| ------------------------------------------------------------------- | ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ![The Maximize icon.](../_images/p1-dashboard-maximize.png)         | Maximize     | Expands the chart to fill the dashboard.To minimize the chart, click the icon again.                                                                                                              |
| ![The Menu options icon.](../_images/p1-dashboard-menu-options.png) | Menu options | Options can vary for different types of charts:- **View summary data**: Displays chart data as a table.

- **Export**: Exports chart data to CSV or Excel format, depending on the type of chart. |
| ![The Sort visual icon.](../_images/p1-dashboard-sort-visual.png)   | Sort visual  | Sorts the chart data in ascending or descending order.                                                                                                                                            |

### Total CUA Detections

Displays the total number of requests evaluated by PingOne Protect that scored high for AI-based browser automation during the selected time period.

### Agent Detections (CUA) Over Time

Displays a rolling average line of CUA detections over time for the selected time period.

### Human vs. CUA Activity Over Time

Displays the number of human versus CUA requests for the selected time period.

### Human vs. CUA Activity

Displays a circle chart with the percentage of human versus CUA requests for the selected time period.

### Requests by Agent

Displays the percentage of CUA requests by agent type, such as Microsoft Copilot and Claude Code, for the selected time period.

---

---
title: Audit report (early access)
description: The refreshed PingOne audit report UI provides improved navigation and filtering for reviewing audit events in the admin console.
component: pingone
page_id: pingone:early-access-features:ea-p1_audit_report
canonical_url: https://docs.pingidentity.com/pingone/early-access-features/ea-p1_audit_report.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-08-13T00:00:00Z
keywords: ["audit report;audit events;event details;timestamps;filtering;exporting"]
section_ids:
  running-an-audit-report: Running an audit report
  steps: Steps
---

# Audit report (early access)

PingOne is introducing a refreshed UI for the audit report in the PingOne admin console. While the core functionality and most features remain consistent with the previous version, the updated UI includes several improvements designed to enhance your experience. Changes include:

* A modern and intuitive layout for easier navigation.

* An updated **Time Zone** list for easier selection.

* An improved method for reordering selected fields using the **Gear** icon ([icon: gear, set=fa]) located next to **Columns**.

Lean more about running audit reports in [Audit](../monitoring/p1_reporting.html).

![A screen capture of the main audit page and ui refresh.](_images/p1_intro_audit_report.png)

You can run reports to see a summary of user events or events for actions performed in the PingOne admin console.

|   |                                                                                                                                                                                                                       |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | You can find a complete list of events logged in PingOne in [Audit Reporting Events](https://developer.pingidentity.com/pingone-api/platform/reference/audit-reporting-events.html) in the PingOne API documentation. |

## Running an audit report

### Steps

1. In the PingOne admin console, go to **Monitoring > Audit** and enter the report parameters:

   | Option                    | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
   | ------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | **Time Range**            | Limit the report results to a specified range of time.&#xA;&#xA;Data up to 14 days old relative to the current date is available immediately.&#xA;&#xA;Data older than 14 days must be requested from the Audit page or using the API, and you can't request data for dates that are more than 2 years (730 days) before the current date.&#xA;&#xA;You can run reports a maximum of 14 days at a time. If you enter an invalid time range, you're prompted to adjust it before you run the report. |
   | **Selected Fields**       | Specify which columns appear in the results list.                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
   | **Time Zone**             | Specify the time zone to use in the results list. The timestamp shows the date and time for the selected time zone.                                                                                                                                                                                                                                                                                                                                                                                 |
   | **Filter Type**           | Limit the results to a particular type, user, or resource.                                                                                                                                                                                                                                                                                                                                                                                                                                          |
   | **Secondary Filter Type** | Specify a secondary filter to limit the results to a particular type, user, or resource. You must specify a primary filter type before you can select a secondary filter type.                                                                                                                                                                                                                                                                                                                      |

2. Click **Run Report**.

---

---
title: Configuration management and promotion in PingOne (early access)
description: Native configuration promotion capabilities are now available for early access in PingOne. For the purposes of early access, this feature is available for sandbox environments only.
component: pingone
page_id: pingone:early-access-features:ea-p1_promote
canonical_url: https://docs.pingidentity.com/pingone/early-access-features/ea-p1_promote.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  configuration-management-constraints-and-considerations: Configuration management constraints and considerations
  p1-promotion-retention: Promotion retention
  alternative-promotion-strategies: Alternative promotion strategies
---

# Configuration management and promotion in PingOne (early access)

Native configuration promotion capabilities are now available for early access in PingOne. For the purposes of early access, this feature is available for sandbox environments only.

The **Promote** section provides access to the native PingOne configuration management tools. These tools allow you to automate the promotion of configuration resources (such as applications, DaVinci flows, and policies) from one environment to another environment from the PingOne admin console or using the PingOne APIs.

Learn more about using the PingOne configuration management APIs to perform promotions during early access in the [Configuration Management (early access)](https://developer.pingidentity.com/pingone-api-ea/platform/early-access/configuration-management.html) section of the PingOne API documentation.

PingOne configuration management offers a secure, flexible way to promote configuration resources across environments. This automated process streamlines resource deployment and eliminates manual production changes, which reduces errors and downtime.

Key capabilities include:

* The ability to create, update, and delete configuration resources seamlessly across environments.

* Dynamic configuration support using promotion variables to manage environment-specific resource differences.

* Automatic dependency management to ensure smooth transitions between environments.

* Rollback support so that you can revert the most recent promotion and restore resources to their previous state instantly in the event of errors or unexpected outcomes.

* Auditing and reporting features to provide oversight and ensure compliance.

At the start of the promotion process, PingOne generates snapshots of your source and target environments, compares the two, and provides information about the environment resources that can be promoted. You can promote a single configuration resource or multiple resources.

## Configuration management constraints and considerations

Before you start using PingOne configuration management, review the following constraints and considerations to ensure that it meets your needs and to understand how to use it effectively.

* You can promote to only one target environment at a time from PingOne and the environments must be in the same PingOne organization. Cross-organization promotions aren't currently supported.

* You can promote up to 100 configuration resources in a single promotion. Dependencies that are automatically included with the selected resource don't count toward this limit.

* Full environment promotions (promoting all configuration resources from one environment to another) aren't currently supported, unless the environment contains fewer than 100 configuration resources. Resources must be configured individually. There is no select all option.

* The following PingOne services don't support configuration promotion:

  * PingOne Authorize

  * PingOne Credentials

  * PingOne Privilege

  * PingOne Recognize

* You must have the new Promotion Admin role or a custom role with equivalent permissions in both the source and target environments to create and complete a promotion and to create and assign promotion variables.

* Both the source and target environments should include the same PingOne services and connected products. For example, if your source environment includes PingOne MFA and PingOne Protect, your target environment should also include PingOne MFA and PingOne Protect. If you try to promote configuration resources from your source environment for a service that your target environment doesn't include, you might cause issues in your target environment.

* Runtime and user data can't be promoted. For example, user profiles, session and device data, and audit logs can't be promoted. You can find a complete list of non-promotable data in [Excluded Resources (early access)](https://developer.pingidentity.com/pingone-api-ea/platform/early-access/configuration-management/promotions/excluded-resources.html) in the PingOne API documentation.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | - Don't make configuration changes directly in your production environments. Instead, emulate the workflow defined in [Typical configuration management workflow (early access)](ea-p1_promote_typical_workflow.html), modifying as needed for your use cases and PingOne infrastructure. This workflow ensures the integrity of your production environments and minimizes the introduction of issues that could impact end users.

- Promote small, easily testable sets of resources to simplify testing and troubleshooting. For example, promote a single authentication flow and its dependencies, then test the flow in the target environment before promoting additional resources. |

## Promotion retention

The following retention policies apply to promotions in PingOne:

* You can create a maximum of 1000 promotions per environment. When you create promotion 1001, the oldest promotion is automatically deleted from the system.

* The five most recent promotions are retained at all times.

* Promotions older than 90 days are deleted from the system unless they're one of the five most recent promotions.

* Promotions in the following statuses are removed if they're more than 30 days old, unless they're one of the five most recent promotions:

  * Ready

  * Failed

  * In Progress

  * New

## Alternative promotion strategies

If your organization uses Terraform for infrastructure as code (IaC), you can leverage official PingOne Terraform providers to manage configuration promotion. Learn more in the [PingOne Cloud - Getting started](https://developer.pingidentity.com/terraform/products/pingone/getting_started.html) section of the Configuration Automation - Terraform documentation.

Similarly, if your organization has well-established DevOps and DevSecOps teams, you might already have mechanisms in place to automate PingOne configuration management.

Discuss these options with your internal stakeholders to determine the best promotion path for your needs.

---

---
title: Configuration promotion scenarios (early access)
description: The scenarios in this section detail several different types of PingOne configuration promotions.
component: pingone
page_id: pingone:early-access-features:ea-p1_promotion_scenarios_intro
canonical_url: https://docs.pingidentity.com/pingone/early-access-features/ea-p1_promotion_scenarios_intro.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2025-12-08T00:00:00Z
section_ids:
  assumptions: Assumptions
---

# Configuration promotion scenarios (early access)

For the purposes of these scenarios, we'll use the following configuration resources which will be referenced in steps and in screenshots. These resources are for example purposes only.

* Source environment: **Promotion-Source**

* Target environment: **Promotion-Target**

* PingOne applications:

  * **My First App** (scenario 1)

  * **My SAML app** (scenarios 2 and 5)

* PingOne DaVinci flow: **Test Registration, Password Reset, and Recovery** (scenario 3)

* DaVinci application: **PingOne SSO Connection** (scenario 4)

* DaVinci flow policies: **PingOne - Sign On and Registration** and **New flow policy** (scenario 4)

* **Test IdP** (scenario 6)

## Assumptions

The user performing the promotions has the Promotion Admin role in both environments, and the two environments include the following PingOne services:

* PingOne SSO

* PingOne MFA

* PingOne DaVinci

Each scenario includes instructions for how to configure the promotion, and then how to verify the results of the promotion.

* [Scenario 1: Simple promotion without dependencies (early access)](ea-p1_config_promotion_scenario_1.html)

* [Scenario 2: Promotion with dependencies (early access)](ea-p1_config_promotion_scenario_2.html)

* [Scenario 3: Promotion of a PingOne DaVinci flow (early access)](ea-p1_config_promotion_scenario_3.html)

* [Scenario 4: Promotion of a PingOne DaVinci flow policy (early access)](ea-p1_config_promotion_scenario_4.html)

* [Scenario 5: Promotion of deleted resource (early access)](ea-p1_config_promotion_scenario_5.html)

* [Scenario 6: Sensitive variable creation (early access)](ea-p1_config_promotion_scenario_6.html)

---

---
title: Configuration resources requiring special handling (early access)
description: Some configuration resources require special handling or behave a bit differently than other resources. Others can't be promoted directly because they're environment specific or include attributes that aren't compatible with the promotion process.
component: pingone
page_id: pingone:early-access-features:ea-p1_configuration_management_special_handling
canonical_url: https://docs.pingidentity.com/pingone/early-access-features/ea-p1_configuration_management_special_handling.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  resources-excluded-from-promotion: Resources excluded from promotion
  deleted-configuration-resources: Deleted configuration resources
  davinci-resources: DaVinci resources
  davinci-flows: DaVinci flows
  davinci-flow-policies: DaVinci flow policies
  davinci-applications: DaVinci applications
  secrets-and-passwords: Secrets and passwords
  certificates: Certificates
  user-attributes: User attributes
  ldap-gateway: LDAP gateway
---

# Configuration resources requiring special handling (early access)

Some configuration resources require special handling or behave a bit differently than other resources. Others can't be promoted directly because they're environment specific or include attributes that aren't compatible with the promotion process.

## Resources excluded from promotion

Some resources can't be promoted at all. Excluded resources generally fall into the following categories:

* **User and operational data**: Resources that contain user-specific or operational data, such as audit logs, user profiles, or device and session data, are excluded from promotion to prevent data integrity issues.

* **Environment-specific secrets and keys**: These resources are inherently tied to a specific environment for security reasons and can't be promoted or used by another environment. These resources should always be configured in the promotion as sensitive promotion variables.

* **Roles and permissions**: Although you can promote resources that require permissions or roles, the administrative access to them isn't promoted. This includes administrator role assignment and application role assignments. After the resource is promoted, you must manually assign the appropriate roles and permissions to the resource in the target environment.

You can find a complete list of excluded resources in the [Excluded Resources (early access)](https://developer.pingidentity.com/pingone-api-ea/platform/early-access/configuration-management/promotions/excluded-resources.html) section of the PingOne API documentation.

## Deleted configuration resources

When you delete a configuration resource from the source environment after it has been promoted to the target environment, that resource remains in the target environment until you explicitly delete it there. You can use the promotion service to handle the deletion. A deletion promotion works similarly to a standard promotion, but instead of creating or updating the resource in the target environment, the promotion service deletes it.

Learn more in [scenario 5](ea-p1_config_promotion_scenario_5.html).

## DaVinci resources

The promotion service fully supports the promotion of PingOne DaVinci resources, including flows, subflows, flow policies, connectors, and DaVinci applications. However, there are several differences in how certain types of DaVinci resources are processed during promotion.

As with other configuration resources, you can map DaVinci dependencies to existing resources in the target environment or create them as new resources, but dependency behavior varies depending on the type of DaVinci resource you select for direct promotion.

### DaVinci flows

When you promote a DaVinci flow, the promotion service identifies all of the dependent configurations used in the flow if they're referenced correctly. Only the most recent deployed version of the flow is promoted to the target environment. For example, if your flow has four versions, and version 3 is the most recent deployed version, only version 3 is promoted. Similarly, if the flow includes subflows, only the subflow versions referenced by the flow are promoted.

Learn more in [Flows](https://docs.pingidentity.com/davinci/flows/davinci_flows.html) in the DaVinci documentation.

### DaVinci flow policies

When you promote a DaVinci flow policy, the promotion service identifies the flows referenced by the policy and the specific versions of the flows referenced. All flow versions used in the policy are promoted as dependencies of the policy.

For example, you decide to promote a a flow policy that references two flows, and the policy uses version 2 of flow A and versions 1 and 3 of flow B. In this case, version 2 of flow A and versions 1 and 3 of flow B are all promoted as dependencies of the flow policy.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | DaVinci flow policies are always linked to a DaVinci application. If you promote a flow policy directly, the associated DaVinci application is promoted as a dependency of the flow policy. This application isn't listed on the **Auto-Selected Dependencies** page when you configure the promotion, but it will be listed when you confirm the promotion configuration.If the application has additional flow policies associated with it, those policies aren't promoted as dependencies of the application.To promote all flow policies associated with a DaVinci application, promote the application directly instead of promoting the flow policies individually.Learn more in [Flow Policies](https://docs.pingidentity.com/davinci/applications/davinci_flow_policies.html) in the DaVinci documentation. |

### DaVinci applications

When you promote a DaVinci application, the promotion service identifies all associated flow policies and promotes them as dependencies of the application. The specific versions of the flow policies referenced by the application are promoted.

Learn more in [Applications](https://docs.pingidentity.com/davinci/applications/davinci_applications.html) in the DaVinci documentation.

## Secrets and passwords

Many configuration resources in PingOne use secrets or passwords to connect third-party services, such as an external identity provider (IdP) or a PingOne DaVinci connector. When you select a resource to promote that includes attributes for secrets or passwords, PingOne requires you to create sensitive variables for promotion, which are stored securely and encrypted anywhere they appear. Learn more in [Sensitive variables](ea-p1_promotion_key_concepts.html#p1-promote-sensitive-variables).

## Certificates

Certificates can't be promoted directly, and certificate references in other resources require special handling:

* **Default certificates**: If a resource in the source environment references a default certificate, the promotion service automatically maps that reference to the default certificate in the target environment during the promotion.

* **Certificates as variables**: For non-default certificates, you must create promotion variables to store the certificate IDs for both the source and target environments. During the promotion, the service substitutes the variable value for the certificate ID in the target environment.

The following example illustrates this process:

1. Create verification certificates in both the source and target environments.

2. Create a SAML application in the source environment that uses the verification certificate for that environment.

3. Create a promotion variable for the certificate ID attribute of the SAML application, setting the source environment value to the certificate ID in the source environment and the target environment value to the certificate ID in the target environment.

4. Promote the SAML application from the source environment to the target environment.

The SAML application in the source environment uses the certificate ID defined in the variable for that environment. The SAML application promoted to the target environment uses the certificate ID defined in the variable for the target environment.

Learn more about certificates in [Certificates](../settings/p1_certificates.html).

## User attributes

Individual user attributes are supported for promotion. However, when you promote an application or FIDO policy that references custom user attributes, all schema attributes are added to the promotion plan. You can manually exclude them before you run the promotion.

Learn more in [User Attributes](../directory/p1_user_attributes.html).

## LDAP gateway

Gateway credentials can't be promoted or managed using promotion variables. These credentials must be created in each environment after the gateway is promoted.

Learn more in [LDAP gateways](../integrations/p1_ldap_gateways.html).

---

---
title: Configuring a custom push notification provider (early access)
description: Configure a custom push notification provider for PingOne MFA for sending push notifications.
component: pingone
page_id: pingone:early-access-features:ea-p1_configure_custom_push_provider
canonical_url: https://docs.pingidentity.com/pingone/early-access-features/ea-p1_configure_custom_push_provider.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-07-02T00:00:00Z
section_ids:
  steps: Steps
  provider_configuration: Provider configuration
  authorization-methods: Authorization methods
  body-option: Body option
  payload_format: Payload format
  apns-json-payload-example: APNs JSON payload example
  fcm-json-payload-example: FCM JSON payload example
  hms-json-payload-example: HMS JSON payload example
---

# Configuring a custom push notification provider (early access)

|   |                                                                                                                                                                                                                                                                                                                                                                                               |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | This feature is now available for early access in PingOne. Early access features and APIs are provided for preview purposes only and might change in the final version. Learn more about early access in [Early Access Features in PingOne](p1_early_access_features.html) and [Managing opt-ins for early access features in PingOne](../settings/p1_managing_opt_ins_for_ea_features.html). |

Use the **Senders** page to configure a custom push notification provider for PingOne MFA.

## Steps

1. In the PingOne admin console, go to **Settings > Senders**.

2. Click **+**, in the **Sender Type** list, select **Push**, and then click **Next**.

   **Provider Type** is set with the value **Custom Provider**.

3. On the **Provider Configuration** page, enter the values from the [Provider configuration table](#provider_configuration).

4. Under **Body**, if you choose **Form**, click **+ Add Key, Value** for each key-value pair that you want to enter.

5. Under **Headers**, click **+ Add Header** to add any additional headers required by your push gateway.

   When you select **Body > Form** the header key value pair is prepopulated with `content-type` `application/x-www-form-urlencoded`. When you select **Raw**, the header key-value pair is prepopulated with `content-type` `application/json`. You can edit or remove this default header as needed.

6. Click **Save**.

You can configure up to three custom push providers, which are always available for use.

To use a custom push provider, you must select it in the native application configuration. Learn more in [Editing an application - Native](../applications/p1_edit_application_native.html).

Learn how to use the Push Delivery Settings API to create a custom push sender in [Push Delivery Settings](https://developer.pingidentity.com/pingone-api-ea/platform/early-access/push-delivery-settings.html) in the PingOne developer early access documentation.

|   |                                                                                                                                                                                                                                                                                                                                                                                 |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | * When using a custom provider, if there are repeated errors within a short period or long delays before responses from the provider, PingOne assumes that there is an underlying issue and temporarily activates a circuit breaker, suspending notification attempts for that provider.

* Custom providers use a five-second connect timeout and a three-second read timeout. |

## Provider configuration

| Field             | Type      | Description                                                                                                                                                                                                                                                                                                                                                                                                                     |
| ----------------- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Provider Name** | Mandatory | A meaningful name for your push provider. It prepopulates to **Custom Provider**.                                                                                                                                                                                                                                                                                                                                               |
| **Authorization** | Mandatory | The authorization method, learn more in [Authorization methods](#authorization_methods).                                                                                                                                                                                                                                                                                                                                        |
| **Type**          | Fixed     | The HTTP method used for push notification requests to the associated endpoint. It's always **POST** for push providers.                                                                                                                                                                                                                                                                                                        |
| **URL**           | Mandatory | The endpoint on your custom push gateway that receives push notification requests.                                                                                                                                                                                                                                                                                                                                              |
| **Body**          | Mandatory | Defines the request body format sent to your gateway. Learn more about **Body** formats in [Body option](#body_option).The body must include the `${push-data}` variable, which PingOne replaces with the full push payload object at runtime. Learn more in [Payload format](#payload_format). You can optionally include the `${push-provider}` variable to identify the push provider type, such as `APNS`, `FCM`, or `HMS`. |
| **Headers**       | Optional  | Any additional HTTP headers your gateway requires.                                                                                                                                                                                                                                                                                                                                                                              |

## Authorization methods

| []()Authorization method        | Description                                                                                                                                                           |
| ------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Basic**                       | Enter the **username** and **password** for the provider account. Once set, you can click **Change Account** to enter a new password for the custom provider account. |
| **Bearer**                      | Set a static bearer token for the provider account.                                                                                                                   |
| **OAuth2 – Client Credentials** | Use an authorization server that issues access tokens based on client ID and client secret.                                                                           |
| **Custom Header**               | Use a custom HTTP header name and value for authorization.                                                                                                            |

## Body option

| []()Body option | Description                                                                                                                                                                                                         |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Form**        | The notification request body is in the form of key and value pairs.                                                                                                                                                |
| **Raw**         | The notification request body in a raw payload. Enter the notification request as JSON text according to your gateway's expectation. For instance, `{ "pushData": "${push-data}", "pushType": "${push-provider}" }` |

## Payload format

PingOne sends the `${push-data}` payload to your configured gateway endpoint, which forwards it to the appropriate service, either **Apple Push Notification service (APNs)**, **Firebase Cloud Messaging (FCM)**, or **Huawei Mobile Services (HMS)**. The PingOne payload uses a modified payload format. Your gateway must map it to the format that the target service expects before forwarding. The payload contains fields shared by both services, and fields specific to that service:

| Field                    | Service | Description                                                                   |
| ------------------------ | ------- | ----------------------------------------------------------------------------- |
| `priority`               | All     | Delivery priority.                                                            |
| `dryRun`                 | All     | When `true`, the request is validated without being delivered.                |
| `ttl`                    | All     | Time-to-live in seconds.                                                      |
| `pushToken`              | All     | Device token identifying the target device.                                   |
| `packageName`            | FCM HMS | Application package name.                                                     |
| `collapseKey`            | FCM     | An identifier used for grouping messages.                                     |
| `bundleId`               | APNs    | iOS application bundle identifier.                                            |
| `pushType`               | APNs    | APNs push type, like `alert` or `background`.                                 |
| `badgeNumber`            | APNs    | Badge count to display on the app icon.                                       |
| `contentAvailable`       | APNs    | When `true`, wakes the app in the background to download new content.         |
| `categoryName`           | APNs    | Action category registered in the app for actionable notifications.           |
| `localizedAlertKey`      | APNs    | Localization key for the alert body string.                                   |
| `localizedAlertTitleKey` | APNs    | Localization key for the alert title string.                                  |
| `alertTitle`             | APNs    | Fallback alert title.                                                         |
| `alertBody`              | APNs    | Fallback alert body text.                                                     |
| `soundFileName`          | APNs    | Sound file to play on delivery.                                               |
| `interruptionLevel`      | APNs    | iOS 15+ interruption level.                                                   |
| `mutableContent`         | APNs    | Allows a Notification Service Extension to modify the payload before display. |
| `data`                   | All     | PingOne-populated custom key-value pairs delivered to the application.        |

### APNs JSON payload example

```json
{
  "priority": "high",
  "dryRun": false,
  "ttl": 3600,
  "pushToken": "<your_apns_token>",
  "bundleId": "com.example.yourapp",
  "pushType": "alert",
  "badgeNumber": 1,
  "contentAvailable": true,
  "categoryName": "auth_request",
  "localizedAlertKey": "AUTH_ALERT",
  "localizedAlertTitleKey": "AUTH_TITLE",
  "alertTitle": "Authentication Request",
  "alertBody": "Tap to approve your sign-in.",
  "soundFileName": "default",
  "interruptionLevel": "time-sensitive",
  "mutableContent": true,
  "data": {
    "key1": "value1",
    "key2": "value2"
  }
}
```

### FCM JSON payload example

```json
{
  "priority": "high",
  "dryRun": false,
  "ttl": 0,
  "pushToken": "<your_fcm_token>",
  "packageName": "com.example.yourapp",
  "data": {
    "key1": "value1",
    "key2": "value2"
  }
}
```

## HMS JSON payload example

```json
{
  "priority": "high",
  "dryRun": false,
  "ttl": 0,
  "pushToken": "your_hms_token",
  "data": {
    "key1": "value1",
    "key2": "value2"
  },
  "packageName": "com.example.yourapp",
  "collapseKey": 0
}
```

---

---
title: Configuring and running a promotion (early access)
description: Promote PingOne resources from a source environment to a target environment using the Promotions page.
component: pingone
page_id: pingone:early-access-features:ea-p1_configure_promotion
canonical_url: https://docs.pingidentity.com/pingone/early-access-features/ea-p1_configure_promotion.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2025-12-01T00:00:00Z
section_ids:
  before-you-begin: Before you begin
  steps: Steps
  result: Result
  verify-the-promotion: Verify the promotion
  steps-2: Steps
---

# Configuring and running a promotion (early access)

Configure and run a promotion to move PingOne configuration resources from a source environment to a target environment.

## Before you begin

* You must have at least two environments in your organization, and both environments should include the same PingOne services:

  * Source environment

    This environment contains resources you want to promote to another environment.

  * Target environment

    This is the environment to which you are promoting resources from a source environment.

* You must have the Promotion Admin role or a custom role with equivalent permissions in both environments.

* Ensure that promotion variables were created for resources that require them. Learn more in [Promotion variables (early access)](ea-p1_promotion_variables.html).

* Review the [promotion retention policies](ea-p1_promote.html#p1-promotion-retention).

## Steps

1. In the PingOne admin console for your source environment, go to **Promote > Promotions**.

2. Click **Run a Promotion**.

   If you haven't configured a target environment for your promotions from this source environment, you're prompted to select one. If you've already configured a target environment, you're prompted to confirm that the target environment listed is correct.

   |   |                                                                                                                                                                                                                                                                                                                                                           |
   | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | To change the target environment, cancel out of the modal and go to **Settings > Environment Properties**. Select a different environment from the **Target Environment** field in the **Configuration Management** section of the **Environment Properties** page. Then return to **Promotion Variables** and start the variable creation process again. |

   After you confirm the target environment, PingOne takes snapshots of both environments, compares configuration resources, and lists the resources that you can promote.

   ![A screenshot of the Select Resources to Promote page without anything selected.](_images/p1-promote-select-resources.png)

3. On the **Select Resources to Promote** page, search for and select the resources you want to promote.

   |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
   | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | * If a **View Warnings** button appears, click it to review any potential issues that might affect the promotion, such as broken references. Cancel the promotion, address any issues that relate to the resources you want to promote, then restart the promotion.

     ![A screenshot of the View Warnings button on the Select Resources to Promote page.](_images/p1-promote-view-warnings.png)

   * You can promote up to 100 configuration resources in a single promotion. Dependencies that are automatically included with the selected resource don't count toward this limit.

   * You should promote small, easily testable sets of resources to simplify testing and troubleshooting. |

4. Click **Next**.

5. On the **Map Resources** page, map the resource to an existing resource in the target environment or add it as a new resource.

   This page displays only if you haven't promoted a particular resource to the target environment before. After the resource is promoted, the promotion service recognizes that the resource exists in both environments and remembers the mapping for future promotions.

   * **Map** to an existing resource in the target environment

     If the promotion service finds a resource in the target environment that might match the resource you want to promote, the **Map** toggle is set to on (blue) and the matching resource is selected in the **Target** list. When you run the promotion, the version from the source environment overwrites the version in the target environment.

     ![A screen capture of the Map Resources modal with a matching resource in the Target field.](_images/p1-promote-map-to-existing-resource.png)

     If you don't want to map the resource as the configuration service suggests, select a different resource in the **Target** list, or click the **Map** toggle to off (gray) to create the resource as new in the target environment.

   * **Promote as New Resource**

     If the promotion service doesn't find a clear match in the target environment for the resource, the **Map** toggle is off by default. This means that when you run the promotion, the resource is created as new in the target environment. You can also choose to map the resource manually by clicking the **Map** toggle to on (blue) and selecting a resource from the **Target** list.

     ![A screen capture of the Map Resources modal with My First App in the Source field.](_images/p1-promote-map-resources.png)

6. Click **Confirm and Continue**.

   If the resource includes dependencies, the **Auto-Selected Dependencies** modal opens.

   If a configuration resource is required by the parent resource and the promotion service doesn't find a matching resource in the target environment, you must also promote that resource. If a configuration resource has a dependency for which a corresponding or matching resource already exists in the target environment, you can choose not to promote the dependency.

7. Select to map or create the listed dependencies and click **Continue**.

8. On the **Confirm Promotion** page, review the promotion summary and add release notes.

9. Click **Run Promotion**

   |   |                                                                                                                                                                                                                                                                                                                                                 |
   | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | Run the promotion soon after completing the promotion configuration to ensure that you are capturing the most up-to-date configuration in the source environment. The promotion can become stale if significant configuration changes are made in the source environment between the time that you configure the promotion and when you run it. |

### Result

You're returned to the **Promotions** page and the current promotion is listed with a status of **In Progress**. After a few seconds, refresh the page.

|   |                                                                                                                                          |
| - | ---------------------------------------------------------------------------------------------------------------------------------------- |
|   | Most promotions will complete within 30 seconds. This time can vary based on the size and number of resources included in the promotion. |

The status will change to **Success** for a successful promotion.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | If the status changes to **Failed**, click the **More Options** icon (⋮) and select **View**. Some resources might have been promoted successfully while others failed. Review the details to determine which resources were affected and troubleshoot any issues, then run the promotion again. You can also rollback a promotion to revert the changes made by a promotion that completed with some errors. Learn more in [Rolling back a promotion (early access)](ea-p1_promotion_rolling_back.html). |

## Verify the promotion

To verify the results of the promotion, first confirm the details of the promotion in the source environment. Then check the target environment and ensure that it matches what you expect.

### Steps

1. In the PingOne admin console for your source environment, go to **Promote > Promotions**.

2. Locate the promotion in the list, click the **More Options** icon (⋮), and select **View**.

   * Overview tab

     The **Overview** tab shows information about when the promotion was started and completed, the source and target environments, the status of the promotion, and any release notes that were added.

     ![A screenshot of the Overview tab for the initial promotion of My First App.](_images/p1-promote-promotion-complete-overview-tab-myfirstapp.png)

   * Promoted Resources tab

     The **Promoted Resources** tab shows the details about the resources that were promoted.

     ![A screenshot of the Promoted Resources tab for the initial promotion of My First App.](_images/p1-promote-promotion-complete-promoted-resources-tab.png)

3. On the **Overview** tab, click **View Target Environment**.

   You're taken to the admin console for the target environment so that you can confirm that the promoted resources exist and match what you expect.

---

---
title: Creating promotion variables (early access)
description: Use promotion variables in PingOne to allow promoted resources to have different attribute values in different environments.
component: pingone
page_id: pingone:early-access-features:ea-p1_create_promotion_variable
canonical_url: https://docs.pingidentity.com/pingone/early-access-features/ea-p1_create_promotion_variable.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2025-10-01T00:00:00Z
section_ids:
  before-you-begin: Before you begin
  steps: Steps
  next-steps: Next steps
  learn-more: Learn more
---

# Creating promotion variables (early access)

Use promotion variables to allow resources to have different attribute values in different environments.

If you don't create promotion variables for a configuration resource, that resource is promoted to the target environment with all of the same configuration as the resource in the source environment.

|   |                                                                              |
| - | ---------------------------------------------------------------------------- |
|   | There are some configuration resources for which you can't create variables. |

## Before you begin

* You must have at least two environments in your organization to create variables, and you must have the Promotion Admin role or a custom role with equivalent permissions in both environments:

  * Source environment

    This environment contains resources you want to promote to another environment.

  * Target environment

    This is the environment to which you are promoting resources from a source environment.

* The two environments should include the same PingOne services, or your promotion could fail.

## Steps

1. Sign on to the PingOne admin console for your source environment.

2. Go to **Promote > Promotion Variables** and click **Create Promotion Variable**.

   If you haven't configured a target environment for your promotions from this source environment, you're prompted to select one. If you've already configured a target environment, you're prompted to confirm that the target environment listed is correct.

   |   |                                                                                                                                                                                                                                                                                                                                                           |
   | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | To change the target environment, cancel out of the modal and go to **Settings > Environment Properties**. Select a different environment from the **Target Environment** field in the **Configuration Management** section of the **Environment Properties** page. Then return to **Promotion Variables** and start the variable creation process again. |

3. On the **Create Variables** page, in the **Resource Details** section, select a **Category** and then a **Sub-category**, if applicable.

   Categories and subcategories are groupings of configuration resources that allow you to narrow down the list and find what you are looking for more easily. Examples of categories include applications, policies, and so on. Only categories that apply to the resources you have in your environment are listed.

   For example, if you don't have any applications in your environment other than those delivered with PingOne, the **Applications** category isn't listed.

   ![A screen capture of the first page of the Create Variables workflow with the Category list expanded.](_images/p1-promote-variables-select-category.png)

   |   |                                                                                                                                                                                                                               |
   | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | You might need to click **Reload resources list** to pick up categories for configuration resources that were recently added to the environment. It could take a couple of minutes to retrieve the updated list of resources. |

4. In the **Resource** list, select the resource for which you want to create variables.

   The **Attributes** list displays after you select the category, and shows all of the application configuration attributes related to the resource for which you can create variables.

5. Select the attributes for which you want to define variables, then click **Next**.

   ![A screen capture of the Create Variables workflow showing Application in the Category field](_images/p1-promote-create-variable-select-attributes.png)

   |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
   | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | Depending on the resource selected, variables might be required for certain attributes. Sensitive variables must be created for passwords or secrets, for example. These attributes are selected automatically and you can't clear them. Learn more in [Sensitive variables](ea-p1_promotion_key_concepts.html#p1-promote-sensitive-variables).![A screen capture of the Attributes list showing a required attribute that is selected and can't be cleared.](_images/p1-promote-required-sensitive-variable.png) |

6. Define the values to use in the target environment.

   The values for the source environment are displayed on the left, and you define the target environment values on the right.

   ![A screen capture of the second page of the Create Variables workflow showing the source environment values for Signoff URLs and Redirect URIs on the left and fields with new values for the target environment on the right.](_images/p1-promote-set-variables-for-target.png)

   |   |                                                                                                                                                                                                                                                                                                                                                                         |
   | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | If you are defining a sensitive variable, the value in the source environment is hashed and can't be revealed or copied. You must enter a new value for the target environment. You can click the **Eye** icon ([icon: eye, set=fa]) to view the value you are entering until you click **Next**. After the value is saved, it is hashed and can't be viewed or copied. |

   In this example, variable values were set for **Signoff URLs** and **Redirect URIs**.

7. After you complete the entries for all of the variables, click **Next**.

8. On the **Review and Save** page, confirm the variable configuration and click **Save**.

You return to the **Promotion Variables** page. The resource for which you created variables is listed in the **Resources with Variables** section.

![A screen capture showing the Promotion Variables page with My First App added to the Resources with Variables list.](_images/p1-promote-variables-with-resource.png)

You can click the **More Options** icon (⋮) to view, edit, or delete the variables associated with the resource.

You can also change the view to show a list of all variables created in the environment by clicking the arrow next to **Resources with Variables** and selecting **Individual Variables**.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Variables are always created and configured in the source environment. When you create a variable for a resource attribute, you are defining the value that the attribute should have in the target environment *after* the resource is promoted.If you want to view the variables in the target environment before the resource has been promoted from the source environment, you must use the **Individual Variables** list. The resource isn't listed in the **Resources with Variables** list in the target environment until after it's been promoted for the first time. |

![A screen capture of the Promotion Variables page showing the Individual Variables list.](_images/p1-promote-variables-list-variables.png)

## Next steps

Configure and run a promotion.

## Learn more

* [Configuration management and promotion in PingOne (early access)](ea-p1_promote.html)

* [Configuring and running a promotion (early access)](ea-p1_configure_promotion.html)

* [Configuration promotion scenarios (early access)](ea-p1_promotion_scenarios_intro.html)

---

---
title: Early Access Features in PingOne
description: PingOne early access features are opt-in, environment-level capabilities available for preview before general availability.
component: pingone
page_id: pingone:early-access-features:p1_early_access_features
canonical_url: https://docs.pingidentity.com/pingone/early-access-features/p1_early_access_features.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-09-21T17:11:06Z
---

# Early Access Features in PingOne

This section provides early access documentation for the PingOne features available to customers who opt in to preview new functionality.

Early access features can be enabled only at the environment level. You can't enable an early access feature for an entire organization.

Not all features are enabled for early access. Additionally, early access features related to services that aren't in the environment or that aren't allowable by the license assigned to the environment aren't available for opt-in.

You can opt in to early access features through the PingOne admin console or the PingOne API. Learn more in the following topics:

* Admin console: [Managing opt-ins for early access features in PingOne](../settings/p1_managing_opt_ins_for_ea_features.html)

* API: [Early Access Features](https://developer.pingidentity.com/pingone-api/platform/environments/early-access-features.html)

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Early access features are provided for preview purposes only and aren't covered under standard Support service level agreements (SLAs). You can open support cases for feedback, bug reports, configuration questions, or other inquiries related to early access features, but resolution times for these cases will vary. These cases often require collaboration with our Engineering and Product teams, so timelines might exceed the usual SLAs for your Support package.Topics for these features are draft documentation for early access purposes only and aren't complete or final. |

* [PingOne Remote MCP Server (early access)](ea-p1_mcp_server_settings_app.html)

* [Configuration management and promotion (early access)](ea-p1_promote.html)

* [Agent Detection (CUA) Dashboard (early access)](ea-p1_agent_detection_dashboard.html)

* [New email and banner alerts for approaching license entitlement limits (early access)](ea-p1_license_entitlement_limit_alerts.html)

* [Configuring a custom push notification provider (early access)](ea-p1_configure_custom_push_provider.html)

* [PingOne Authorize admin APIs (early access)](ea-p1-az-policy-admin-apis.html)

* [NFC verification from PingOne Verify (early access)](ea-p1_verify_nfc_verification.html)

---

---
title: Editing promotion variables (early access)
description: If you need to change the value of a promotion variable that you have already created in PingOne, you can edit the variable from the Promotion Variables page.
component: pingone
page_id: pingone:early-access-features:ea-p1_edit_promotion_variable
canonical_url: https://docs.pingidentity.com/pingone/early-access-features/ea-p1_edit_promotion_variable.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  before-you-begin: Before you begin
  steps: Steps
---

# Editing promotion variables (early access)

If you need to change the value of a promotion variable that you have already created in PingOne, you can edit the variable from the **Promotion Variables** page.

## Before you begin

You must have created promotion variables in PingOne to edit them. Learn more in [Creating promotion variables (early access)](ea-p1_create_promotion_variable.html).

## Steps

1. Sign on to the PingOne admin console for the environment in which the variable was created.

2. Go to **Promote > Promotion Variables**, locate the applicable variable in the **Resources with Variables** list, and click it to expand the details panel.

3. Click the **Pencil** icon ([icon: pencil, set=fa]) to edit the variable.

4. Update the variable value as needed, then click **Save**.

---

---
title: Key concepts (early access)
description: Understand the key concepts of native configuration promotion in PingOne.
component: pingone
page_id: pingone:early-access-features:ea-p1_promotion_key_concepts
canonical_url: https://docs.pingidentity.com/pingone/early-access-features/ea-p1_promotion_key_concepts.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-04-16T00:00:00Z
section_ids:
  source-and-target-environments: Source and target environments
  snapshots: Snapshots
  promotion-variables: Promotion variables
  p1-promote-sensitive-variables: Sensitive attributes and variables
  promotions-and-promotion-plans: Promotions and promotion plans
  rollback: Rollback
  mapping: Mapping
  dependencies: Dependencies
  missing-or-broken-references: Missing or broken references
---

# Key concepts (early access)

Familiarize yourself with the following key concepts to understand how configuration promotion works in PingOne and to ensure that you can use it effectively.

## Source and target environments

In PingOne configuration promotion, the *source* environment is the environment that contains the configuration resources you want to promote. The *target* environment is the environment to which you want to promote those configuration resources. In a typical development workflow, you might promote configuration resources from a development environment (the source) to a test environment (the target), and then later promote those same resources from the test environment (the source) to a production environment (the target).

Learn more in [Typical configuration management workflow (early access)](ea-p1_promote_typical_workflow.html).

## Snapshots

A snapshot is a point-in-time representation of the configuration resources in a PingOne environment. When you create a promotion, PingOne automatically generates snapshots of both the source and target environments. These snapshots capture the current state of all configuration resources in each environment, allowing the promotion service to compare them and identify differences.

## Promotion variables

Promotion variables are placeholders that you can define and use within configuration resources to represent values that might differ between environments. By using promotion variables, you can create a single configuration resource that can be adapted to different environments without needing to create separate versions of the resource for each environment.

For example, you might have sign-on URLs that differ between your development, test, and production environments. Instead of hardcoding these URLs into your application configuration, you can define a promotion variable and use that variable in the application configuration. When you promote the application to a different environment, you can specify the appropriate value for the sign-on URL in that environment.

Warnings display if the use of variables is recommended for a resource. For example, if you have an application with a sign-on URL that differs between environments, the promotion service might recommend that you use a promotion variable that URL attribute. You can run the promotion without variables, unless the variable is required. However, using promotion variables can help make your promotions more flexible and adaptable to different environments.

## Sensitive attributes and variables

Some attributes in PingOne are marked as sensitive, such as passwords or client secrets. These attributes require the use of sensitive variables for promotion. Sensitive variables are promotion variables that are encrypted. After they're created, their values are hidden and can't be viewed or copied from the PingOne admin console or in API operations. If you try to promote a resource that contains sensitive attributes without creating variables for them, you'll be prompted to create the variables before continuing.

Learn more in [Promotion variables (early access)](ea-p1_promotion_variables.html).

## Promotions and promotion plans

A promotion is the process of moving configuration resources from a source environment to a target environment in PingOne. A promotion is done in two phases:

* Phase 1 - Planning the promotion: Consider the configuration resources you want to promote. Create any promotion variables for these resources, then initiate a promotion. Select the resources you want to promote and map the resources and their dependencies as applicable to resources in the target environment.

* Phase 2 - Running the promotion: When you run the promotion, configuration resources are created or updated in the target environment based on the selections you made during the planning phase.

Learn more in [Configuring and running a promotion (early access)](ea-p1_configure_promotion.html).

## Rollback

Rollback is the process of undoing a promotion or setting the target environment back to the state it was in immediately prior to the promotion. You should always use the rollback mechanism if you have an issue with a promotion and need to start over.

In PingOne, you can roll back only the most recent promotion, and the promotion can be rolled back whether it failed or succeeded. When you roll back a promotion, everything that was promoted is rolled back. You can't roll back a subset of the resources that were promoted.

Learn more in [Rolling back a promotion (early access)](ea-p1_promotion_rolling_back.html).

## Mapping

Mapping is the critical process of linking a specific resource in a source environment to its corresponding resource in a target environment. This process ensures that the system knows whether to create a brand new resource in the target environment or update an existing resource when you run the promotion.

The first time you promote a resource, the promotion service compares the source and target environments and attempts to identify matching resources based on attributes such as resource name or other comparison markers. Based on the comparison, the service makes suggestions as follows:

* No match found: If the service doesn't find a match for the resource in the target environment, it defaults to **Promote as New Resource**. When you run the promotion, the configuration resource or dependent resource is created in the target environment. That new resource is automatically mapped to the resource in the source environment.

* Potential match found: If the service finds a reasonable match for the resource in the target environment, it selects the match by default for mapping purposes.

In either instance, the final decision is left to the administrator running the promotion. Mapping occurs only the first time you promote a resource to a specific target environment.

For example, you know that different naming conventions are used in your source and target environments. You understand that the **Customer App** application in the target environment corresponds to the **My First App** application in the source environment. However, when you initiate the promotion of **My First App**, the promotion service doesn't recognize **Customer App** as a match and recommends creating **My First App** as new in the target environment. You can override that recommendation and instead map **My First App** to **Customer App** before you run the promotion.

Similarly, you can reject a match recommended by the promotion service. For example, if the service recommends mapping **My First App** to **Test App** in the target environment, but you know that **Test App** is unrelated to **My First App**, you can change the mapping to **Promote as New Resource** or map it to a different resource before you run the promotion.

In future promotions of the resource to the same target environment, the system remembers the mapping you selected.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | In some cases, you might not be prompted to map a selected resource. For example, if there's never more than a single instance of a resource in an environment, you aren't prompted to map that resource during promotion because there's no possibility of confusion. Similarly, if the promotion service doesn't find any reasonable matches for a resource in the target environment, you aren't prompted to map it because the only option is to promote it as new. |

## Dependencies

Many resources in an environment include dependencies as part of their configuration, and those dependencies can in turn have their own dependencies. If you tried to promote resources without including their dependencies, they wouldn't function as intended in the target environment.

For example, a DaVinci flow might be configured to include a multi-factor authentication (MFA) connector. The MFA connector might be configured to use an MFA policy. The MFA connector is a direct dependency of the flow, while the MFA policy is an indirect dependency of the flow.

These relationships are illustrated in the following diagram:

![A diagram showing the MFA Device Authentication Flow with a direct dependency on the MFA Connector, which has a direct dependency on the MFA Policy. The flow also has an indirect dependency on the MFA Policy through the MFA Connector.](_images/p1-promote-dependencies-diagram2.png)

If the MFA policy isn't promoted to the target environment with the flow, the connector won't work properly, and the flow could fail.

The PingOne promotion service automatically tracks these direct and indirect dependencies for you. When you select a resource for promotion, the service identifies all of its dependencies and includes them in the promotion plan, ensuring that you promote a complete and functional configuration.

When you promote the flow, you're given the option to map these dependencies to corresponding resources in the target environment, or to create them as new, in the same manner as the main resource you're promoting.

If the configuration service doesn't find a version of the dependency in the target environment, it's considered a required dependency and must be created as new in the target environment. You can't remove required dependencies. For example, a DaVinci flow might reference a subflow. If the subflow doesn't exist in the target environment and isn't brought over as a dependency of the main flow, the main flow itself won't run properly in the target environment.

## Missing or broken references

In some cases, a configuration resource might include references to resources that no longer exist in the environment. If you try to promote a resource with missing references, the promotion might fail because the promotion service can't find the referenced resource.

For example, you have an application that references an authentication flow that was deleted from the source environment. If you try to promote that application, the promotion service can't find the referenced authentication flow in the source environment snapshot and returns an error.

The promotion interface displays warnings when you initiate a promotion that includes missing references. Review the warnings to determine if they apply to what you want to promote. You can still promote a resource that includes warnings for broken references, but the promotion could fail and the resource might not work properly in the target environment if the reference isn't resolved.

|   |                                                                                                                                                                       |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Resolve missing references before you promote a resource either by restoring the deleted resource or by removing the reference from the resource you want to promote. |

---

---
title: New email and banner alerts for approaching license entitlement limits (early access)
description: New alert types have been added to Monitoring > Alerts and as banner alerts in the PingOne admin console. The alerts are available for early access.
component: pingone
page_id: pingone:early-access-features:ea-p1_license_entitlement_limit_alerts
canonical_url: https://docs.pingidentity.com/pingone/early-access-features/ea-p1_license_entitlement_limit_alerts.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  learn-more: Learn more
---

# New email and banner alerts for approaching license entitlement limits (early access)

New alert types have been added to **Monitoring > Alerts** and as banner alerts in the PingOne admin console. The alerts are available for early access.

* License Entitlement Warning

  The usage for the specified entitlement has exceeded 80% of the limit included in your license agreement.

* License Entitlement High

  The usage for the specified entitlement has exceeded 90% of the limit included in your license agreement.

* License Entitlement Exceeded

  The usage for the specified entitlement has exceeded the limit included in your license agreement.

When you configure these alerts, an email message is sent to the specified address when you reach the defined threshold for the entitlement. Each time a new threshold is reached, a new alert is shown. The alerts are cleared at the start of the next license period, or when a different license is assigned to the environment.

The corresponding banner alerts are shown in the PingOne admin console when you reach these thresholds. After a banner alert is acknowledged, it's not shown to the user again until a new threshold is reached.

These alerts trigger auditing events that you can view in the auditing report, and you can create webhook subscriptions to monitor them. Learn more in [Running an audit report](../monitoring/p1_running_audit_report.html) and [Creating or editing a webhook](../integrations/p1_create_webhook.html).

|   |                                                                                                                              |
| - | ---------------------------------------------------------------------------------------------------------------------------- |
|   | These alerts are currently enabled only for PingOne MFA, PingOne Verify, and PingOne DaVinci transaction-based entitlements. |

## Learn more

* [PingOne standard platform limits](../getting_started_with_pingone/p1_platform_limits.html)

* [Alerts](../monitoring/p1_alerts.html)

---

---
title: NFC verification from PingOne Verify (early access)
description: NFC verification is now available for early access verify.
component: pingone
page_id: pingone:early-access-features:ea-p1_verify_nfc_verification
canonical_url: https://docs.pingidentity.com/pingone/early-access-features/ea-p1_verify_nfc_verification.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 17, 2026
page_aliases: ["ea-p1verify_documentation_authentication.adoc"]
section_ids:
  creating-a-verify-policy: Creating a verify policy
  steps: Steps
  next-steps: Next steps
---

# NFC verification from PingOne Verify (early access)

**NFC Verification** is now available for early access verify. This capability lets users use near-field communication (NFC) verification on their mobile device to read a secure, embedded NFC chip on their government-issued ID or passport. This verification method is only available through in-app experiences on mobile devices.

NFC verification is one of many types of verification that PingOne Verify offers, as shown in the following table:

| Verification                         | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| ------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Government ID**                    | Verification based on government-issued documents. For example, a driver license or a passport.By default, government ID verifications use an automated inspection system. If automated verification is unsupported or fails due to poor image quality, the process falls back to manual inspection or a step-up approach (automated followed by manual).Verification is performed on PingOne Verify transactions by default, unless a customized verify policy is assigned to the transaction when it's created. |
| **Digital Identity**                 | For users in India, you can also perform Aadhaar eID verification using DigiLocker. This method lets users share official identity attributes from their Aadhaar card through their government-backed digital wallet. By using this electronic path instead of image-only checks, you can reduce document failures while maintaining compliance with Indian digital identity standards.                                                                                                                           |
| **NFC Verification**                 | Verification based on an embedded chip in a government-issued document. Near-field communication (NFC) verification uses Signicat ReadID to read a secure NFC chip on a user's ID or passport. This verification method is available only on mobile devices.&#xA;&#xA;This feature is currently available for early access.                                                                                                                                                                                       |
| **Facial Comparison**                | A live photo (selfie) compared with government ID documents for verification.Verification is performed on PingOne Verify transactions by default, unless a customized verify policy is assigned to the transaction when it's created.                                                                                                                                                                                                                                                                             |
| **Liveness**                         | A liveness check on the live photo (selfie) for verification.Verification is performed on PingOne Verify transactions by default, unless a customized verify policy is added to the transaction when it's created.                                                                                                                                                                                                                                                                                                |
| **Phone**                            | Phone verification using one-time passcode (OTP).                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| **Email**                            | Email verification using OTP.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| **Identity Data**                    | Data Matching compares the identity data extracted during verification with data from an identity record.                                                                                                                                                                                                                                                                                                                                                                                                         |
| **Data-based Identity Verification** | Verify user identity attributes with trusted third-party data.                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| **Device Ownership and Risk**        | Verify the end user legally owns or is associated with the phone number or email being used to complete the verification transaction.                                                                                                                                                                                                                                                                                                                                                                             |

## Creating a verify policy

A verify policy dictates what's required to verify a user, such as an ID verification, facial comparison, or liveness. Users can now choose **NFC Verification** when creating a verify policy. It's included in the list of policies in the following steps:

## Steps

1. In the PingOne admin console, go to **Identity Verification > Verify Policies**.

   |   |                                                                           |
   | - | ------------------------------------------------------------------------- |
   |   | A default verify policy based on your environment capabilities is listed. |

2. Click the **[icon: plus, set=fa]**icon.

3. Enter or edit the following:

   > **Collapse: Policy configuration**
   >
   > | Field                                | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
   > | ------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   > | **Name**                             | The policy's name.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
   > | **Description**                      | The policy's description.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
   > | **Store Verified Claims**            | Stores verified personally identifiable information (PII) in the Identity Assurance (IDA) object within the PingOne Directory. Learn more in [Viewing user details](../directory/p1_viewusers.html) and [Editing a user in PingOne](../directory/p1_edituser.html).Select the checkbox to enable storing verified claims.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
   > | **Configuration**                    | * **Transaction Timeout**: Time period (in minutes) in which data can be collected after a transaction is created. The maximum transaction timeout is 30 minutes.
   >
   > * **Data Collection Timeout**: Time period (in minutes) in which data can be collected after initiating verification from the UI. By default, the data collection timeout is set to 15 minutes. The maximum data collection timeout is 30 minutes.
   >
   > * **Data Collection Only**: Click the toggle to enable data collection from a user without verification.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
   > | **Government ID**                    | Verification based on government-issued documents. For example, a driver license or a passport.Configure the following policy settings:* **ID Verification**: Select **Required** or **Disabled** to determine whether the end user must provide a government ID for verification.
   >
   >   &#xA;&#xA;If Government ID is Required, a government ID must be collected to compare with a selfie.
   >
   > * **Document Authentication Provider**: The provider used to authenticate government documents. Select **Mitek** or **Veriff** (default).
   >
   > * **Inspection Type**: Select the type of inspection performed on government-issued documents:
   >
   >   * **Automatic**: Artificial intelligence (AI)-based analytics examine the ID document to determine if it's original and unaltered.
   >
   >   * **Manual**: A human agent trained in document authentication examines the photo of the ID to determine its authenticity.
   >
   >   * **Step-Up to Manual**: Automated inspection is tried first. If the document can't be verified, the service switches to manual inspection.
   >
   >     &#xA;&#xA;Manual and Step-Up to Manual inspection types require an additional license.
   >
   > * **Government ID Retry Attempts**: The number of times a user can retry scanning an ID if the first attempt fails. Possible values for government ID retry attempts are 0 - 3.
   >
   > * **Enable AAMVA**: Click the toggle to enable verification of ID information against the issuing agency database, the [AAMVA Driver's License Data Verification (DLDV)](https://www.aamva.org/technology/systems/verification-systems/dldv) service. Learn more in [PingOne Verify and the American Association of Motor Vehicle Administrator's system of record](../identity_verification_using_pingone_verify/p1_verify_aamva_dldv.html).
   >
   > * **Fail Expired IDs**: Click the toggle to fail verification for expired IDs. |
   > | **Digital Identity**                 | **Enable Aadhaar Verification (India)**: Click the toggle to enable user verification of Aadhaar eIDs through the DigiLocker wallet.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
   > | **NFC Verification**                 | Near-field communication (NFC) verification based on an embedded chip in a government-issued document using Signicat ReadID.&#xA;&#xA;This feature is currently available for early access.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
   > | **Facial Comparison**                | A live photo (selfie) compared with government ID documents or reference selfie for verification.Configure the following policy settings:* **Facial Comparison**: Select **Required**, **Optional**, or **Disabled** to determine whether the end user must provide a selfie for verification.
   >
   >   &#xA;&#xA;If Facial Comparison is Required, a government ID and selfie must be collected.
   >
   > * **Threshold**: The probability that selfies are likely to match with document images (facial comparison) or pass liveness checks (liveness). Select **Low**, **Medium**, or **High** threshold.
   >
   >   &#xA;&#xA;Selfies are less likely to match or pass with a higher threshold.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
   > | **Liveness**                         | A liveness check on the live photo (selfie) for verification.Configure the following policy settings:* **Liveness**: Select **Required**, **Optional**, or **Disabled** to determine whether the end user must provide a selfie for verification.
   >
   >   &#xA;&#xA;If Liveness is Required, a selfie must be collected.&#xA;&#xA;Disabling Liveness automatically deactivates the backend injection attack detection (IAD) process. IAD detects and blocks attempts to bypass the device camera using synthetic or prerecorded media.
   >
   > * **Threshold**: The probability that selfies are likely to match with document images (facial comparison) or pass liveness checks (liveness). Select **Low**, **Medium**, or **High** threshold.
   >
   >   &#xA;&#xA;Selfies are less likely to match or pass with a higher threshold.
   >
   > * **Selfie Retry Attempts**: The number of times a user can retake a selfie if the first attempt fails. Possible values for selfie retry attempts are 0 - 3.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
   > | **Phone**                            | Configure the following policy settings:* **Phone Verification**: Select **Required** or **Disabled** to determine whether the end user must provide their phone number for verification.
   >
   > * **Create MFA Device**: Click the toggle to enable registration of a user's phone number as a trusted multi-factor authentication (MFA) device after successful OTP or web link verification.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
   > | **Email**                            | Configure the following policy settings:* **Email Verification**: Select **Required** or **Disabled** to determine whether the end user must provide their email address for verification.
   >
   > * **Create MFA Device**: Click the toggle to enable registration of a user's email address as a trusted MFA device after successful OTP or web link verification.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
   > | **Identity Data**                    | **Data Matching** compares the identity data extracted during verification with data from an identity record.Configure the following policy settings:* **Attribute**: Lists **Given Name**, **Family Name**, **Full Name**, **Date of Birth**, and **Address**.
   >
   > * **Confidence Threshold**: The probability that an attribute (the data extracted during verification) matches the data from an identity record. Select **None**, **Low**, **Medium**, or **High**.
   >
   >   &#xA;&#xA;Selecting None leaves an attribute unconfigured and no matching occurs.
   >
   > * **Required**: Select the checkbox to make the value of an attribute required.
   >
   >   &#xA;&#xA;The verification fails automatically if a required value can't be extracted during verification or isn't included in the transaction input.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
   > | **Data-Based Identity Verification** | Verify user identity attributes with trusted third-party data.Configure the following policy settings:* **US Data-Based Identity Verification**: Select **Enabled** or **Disabled**.
   >
   > * **Threshold**: Assesses whether there's fraud or risk associated with the user. Select **Low**, **Medium**, or **High**.
   >
   > * **Required Contractual Obligation**: Select the checkbox to acknowledge that by enabling this feature, you're contractually obligated to obtain user consent.
   >
   >   &#xA;&#xA;You must select the Required Contractual Obligation checkbox to enable the Data-Based Identity Verification policy.Learn more in [PingOne Verify and data-based verification](../identity_verification_using_pingone_verify/p1_verify_data_based_verification.html).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
   > | **Device Ownership and Risk**        | Verify the end user legally owns or is associated with the phone number or email being used to complete the verification transaction.Configure the following policy settings:* **Device Ownership Check**: Select **Enabled** or **Disabled**.
   >
   > * **Phone Number Risk Threshold**: Determines the acceptable risk level for phone behavioral data inferred from the carrier history and other data sources. This field is required if **Device Ownership Check** is set to **Enabled**. Select **Medium** (default) or **High**.
   >
   > * **Phone-to-Name Threshold**: Determines linkage between phone and name. Select **Medium** (default) or **High**.You can also configure the following thresholds:* (Optional) **Email-to-Phone Threshold**: Select **Medium** or **High**.
   >
   > * (Optional) **Email-to-Name Threshold**: Select **Medium** or **High**.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |

4. Click **Save**.

### Next steps

Find your new policy on **Verify Policies** page, then trigger a verify transaction using the verify policy. Learn more in [Configuring and setting up PingOne Verify](../identity_verification_using_pingone_verify/p1_verify_configuration_setup.html).

---

---
title: PingOne Authorize admin APIs (early access)
description: The PingOne Authorize admin APIs, available in early access, provide programmatic access to authorization policies and Trust Framework definitions.
component: pingone
page_id: pingone:early-access-features:ea-p1-az-policy-admin-apis
canonical_url: https://docs.pingidentity.com/pingone/early-access-features/ea-p1-az-policy-admin-apis.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-09-08T17:59:20Z
keywords: ["PingOne Authorize;admin APIs;authorization policies;Trust Framework;early access"]
---

# PingOne Authorize admin APIs (early access)

The PingOne Authorize admin APIs are available in early access. You can use these APIs to manage the following PingOne Authorize resources programmatically:

* Authorization policies, rules, and statements

* Trust Framework elements, including attributes, conditions, processors, and services

Learn more in the [PingOne Authorize Admin APIs (early access)](https://developer.pingidentity.com/pingone-api-ea/authorize/early-access/pingone-authorize-admin-apis.html) section of the PingOne API reference.

---

---
title: PingOne Remote MCP Server (early access)
description: Learn about the new PingOne Remote MCP Server and how to enable it in your environment.
component: pingone
page_id: pingone:early-access-features:ea-p1_mcp_server_settings_app
canonical_url: https://docs.pingidentity.com/pingone/early-access-features/ea-p1_mcp_server_settings_app.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-10-14T14:42:09Z
section_ids:
  mcp-server-settings: MCP Server settings
  new-system-application: New system application
  configuring-custom-redirect-uris: Configuring custom redirect URIs
  steps: Steps
  result: Result
  learn-more: Learn more
---

# PingOne Remote MCP Server (early access)

The PingOne Remote MCP Server is now available for early access (EA).

The PingOne Remote MCP Server lets artificial intelligence (AI) clients connect to PingOne through a single remote Model Context Protocol (MCP) endpoint. Because the server is remote, you don't need to install, configure, or run a local MCP server.

After configuring a supported client, administrators authenticate through PingOne with OAuth 2.0. They can then securely use MCP tools to administer the PingOne platform.

All MCP tools adhere to the PingOne roles and permissions model. Administrators can only access and use tools supported by their existing roles.

## MCP Server settings

To support the release of the PingOne Remote MCP Server, we've added a new **MCP Server** page in the **Settings** section of the PingOne admin console. Enable or disable the PingOne Remote MCP Server for the environment on this page (MCP server access is disabled by default).

To enable the PingOne Remote MCP Server, click **Enable MCP Access**.

![A screenshot of the MCP Server settings page in the PingOne admin console.](_images/p1-mcp-server-settings.png)

You must have the Environment Admin role or a custom role with equivalent permissions to enable or disable the PingOne Remote MCP Server.

|   |                                                                                                                                                                                                                                                                         |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | For this EA release, enabling the PingOne Remote MCP Server provides access to all of the available PingOne MCP tools. During EA, you should enable the server in non-production environments only. More granular tool controls will be introduced in a future release. |

## New system application

We've also added a new **PingOne MCP Server** system application. This application allows administrators to access and use the PingOne Remote MCP server to manage the environment's configuration and data. It's enabled by default and can't be disabled.

|   |                                                                                                                                                                                |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | The **PingOne MCP Server** application won't appear in the PingOne admin console unless an administrator has opted in to the remote MCP feature for that specific environment. |

![A screenshot of the PingOne Applications page showing the new MCP Server system application.](_images/p1-mcp-server-system-app.png)

### Configuring custom redirect URIs

By default, the **PingOne MCP Server** application uses two system-provided redirect URIs. Instead of using the default URIs, you can optionally add custom redirect URIs to which PingOne forwards the OIDC response after authentication. Learn more in [Redirect URIs](../applications/p1_wildcard_redirect_uri.html).

#### Steps

1. In the PingOne admin console, go to **Applications > Applications** and click the **PingOne MCP Server** application to open the details panel.

2. On the **Overview** tab, click the **Pencil** icon ([icon: pencil, set=fa]).

3. Click **[icon: plus, set=fa]Add Custom Redirect URI**.

4. Enter the redirect URI your MCP client uses to receive the OIDC response.

   Learn more about using a wildcard or loopback IP address in [Redirect URIs](../applications/p1_wildcard_redirect_uri.html).

5. To add additional URIs, click **[icon: plus, set=fa]Add Custom Redirect URI**.

6. (Optional) Select the **Allow Redirect URI Patterns** checkbox to use a wildcard for flexibility in managing redirect URIs.

7. Click **Save**.

|   |                                                                           |
| - | ------------------------------------------------------------------------- |
|   | To revert to using the default redirect URIs, click **Restore Defaults**. |

#### Result

The new redirect URIs are displayed on the **Redirect URIs** tab of the **MCP Server** page.

## Learn more

Learn more about the [PingOne Remote MCP Server](https://developer.pingidentity.com/build-with-ai/pingone-mcp-server/p1-overview.html) in the Build with AI documentation.

---

---
title: Promotion variables (early access)
description: Define and manage variables for use in PingOne configuration promotion.
component: pingone
page_id: pingone:early-access-features:ea-p1_promotion_variables
canonical_url: https://docs.pingidentity.com/pingone/early-access-features/ea-p1_promotion_variables.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-04-27T12:51:39Z
section_ids:
  sensitive-variables: Sensitive variables
  additional-considerations: Additional considerations
---

# Promotion variables (early access)

Use promotion variables to set configuration values that need to be different in each environment, such as third-party integrations or URLs. For example, an application might need one redirect URI in your testing environment, but a different redirect URI in your production environment.

You can specify configuration resource property values for either the source or target environment to be substituted for existing property values when you run a promotion. If you don't set a promotion variable for a property, it will be used as is and the value will be the same in both the source and target environments.

Some properties require the use of variables. In most cases, however, variable use is optional. You can determine which properties should use variables based on your use cases and requirements.

|   |                                                                                                                                                                                                           |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Configure your promotion variables before starting a promotion. Update your list of variables regularly, particularly after you perform significant configuration changes that you might want to promote. |

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Not all properties for configuration resources can be set up as variables. You can find a complete list of configuration resources and the associated properties that can be used as promotion variables in [Variable Resources (early access)](https://developer.pingidentity.com/pingone-api-ea/platform/early-access/configuration-management/promotion-variables/variable-resources.html) in the PingOne API documentation. |

## Sensitive variables

Some attributes in PingOne are marked as sensitive, such as passwords or client secrets. These attributes require the use of sensitive variables for promotion. Sensitive variables are promotion variables that are encrypted, and, after they're created, their values are hidden and can't be viewed or copied from the PingOne admin console or in API operations. If you try to promote a resource that contains sensitive attributes without creating variables for them, you'll be prompted to create the variables before continuing.

|   |                                                                                                                                                                                                                                                                                          |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | When you edit a sensitive variable, you must reenter the entire value. The existing value isn't displayed for security reasons, and can't be copied from the user interface. Ensure that you store the actual value of the sensitive variable in a secure location for future reference. |

## Additional considerations

* Variable values are only processed and applied during a promotion. Changing variable values doesn't affect the promotion resource until you use the new values in a promotion of that resource. You should review your promotion variables and update them as needed before running a promotion.

* If you set up variables for configuration resources and then change those resources directly without updating the variables, the variable values will overwrite your changes during subsequent promotion operations. This is because the promotion operation will use the existing variable set.

---

---
title: Promotions (early access)
description: Use the Promotions page to create and manage promotions and rollbacks in PingOne.
component: pingone
page_id: pingone:early-access-features:ea-p1_promotions
canonical_url: https://docs.pingidentity.com/pingone/early-access-features/ea-p1_promotions.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-04-27T12:51:39Z
---

# Promotions (early access)

PingOne configuration management offers a secure, flexible way to promote configuration resources across environments. This automated process streamlines resource deployment and eliminates manual production changes, reducing errors and downtime.

A promotion or rollback includes, at a minimum:

* Source and target environment references.

* Automatically generated source and target snapshots.

* The resource or resources to promote to the target environment.

* A promotion plan for the promotion operation.

---

---
title: Rolling back a promotion (early access)
description: Roll back a promotion to reset the target environment back to the state it was in immediately prior to the promotion.
component: pingone
page_id: pingone:early-access-features:ea-p1_promotion_rolling_back
canonical_url: https://docs.pingidentity.com/pingone/early-access-features/ea-p1_promotion_rolling_back.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-02-23T00:00:00Z
section_ids:
  limitations-and-considerations: Limitations and considerations
  steps: Steps
  result: Result
  verifying-the-rollback: Verifying the rollback
  steps-2: Steps
  result-2: Result
---

# Rolling back a promotion (early access)

If a promotion causes issues in your target environment, you can roll it back, which restores the environment to its state immediately before the promotion. You can roll back both successful and failed promotions. A rollback undoes all changes made by the promotion.

## Limitations and considerations

* You can roll back only the most recent promotion to the target environment, and all promoted resources are rolled back. You can't select a subset of resources to roll back. You also can't roll back a rollback.

* A promotion can sometimes affect resources that weren't part of the promotion plan. For example, if you promote the deletion of a policy that was assigned to an application, the promotion also deletes the association between the application and the policy in the target environment. To restore the target environment to its previous state, a rollback must not only restore the deleted policy, but also restore the association between the policy and the application. In this case, the application is considered an indirectly affected resource, and is included in the rollback.

* If you make manual changes to promoted resources in the target environment after the initial promotion and before the rollback, those changes might be overwritten during the rollback.

## Steps

1. In the PingOne admin console for your source environment, go to **Promote > Promotions**.

2. In the list of promotions, locate the most recent promotion, click the **More Options** (⋮) icon, and select **Roll Back**.

3. On the **Review Rollback** page, review the summary and add release notes.

   ![A screen capture of the Review Rollback page showing the Rollback tab and listing two resources that will be rolled back.](_images/p1-promote-review-rollback-rollback.png)

4. (Optional) To review the details of the promotion you are rolling back, click the **Previous Promotion** tab.

   This tab shows details about the configuration resources that were promoted and will be rolled back, including any dependencies.

   ![A screen capture of the Review Rollback page showing the Previous Promotion tab with details about the promotion that is being rolled back.](_images/p1-review-rollback-previous-promotion.png)

5. Click **Roll Back Promotion**.

### Result

You're returned to the **Promotions** page. The rollback shows a status of **In Progress**. After a couple of minutes, refresh the page. The status changes to **Success** for a successful rollback.

The promotion you rolled back now shows a status of **Rolled Back**.

![A screenshot of the Promotions list showing a promotion with a status of Rolled Back and a rollback with a status of Success.](_images/p1-promotions-list-showing-rollback.png)

## Verifying the rollback

To verify the results of the rollback, first confirm the details of the rollback in the source environment, then check the target environment and ensure that it matches what you expect.

### Steps

1. In the PingOne admin console for your source environment, go to **Promote > Promotions**.

2. Locate the rollback in the list, click the **More Options** icon (⋮), and select **View**.

   * Overview tab

     The **Overview** tab shows information about when the rollback was started and completed, the source and target environments, the status of the rollback, and any release notes that were added.

     ![A screenshot of the Rollback tab of the rollback details panel.](_images/p1-promote-rollback-details-overview-tab.png)

   * Rolled Back Resources tab

     The **Rolled Back Resources** tab shows the details about the resources that were rolled back.

     ![A screen capture of the Rolled Back Resources tab of the rollback details panel showing the resources that were included in the promotion that you rolled back.](_images/p1-review-rollback-previous-promotion.png)

3. On the **Overview** tab, click the link to the target environment in the **Original Promotion Environment** field.

### Result

You're taken to the PingOne admin console for the target environment so that you can confirm that the results of the rollback match what you expect.

---

---
title: "Scenario 1: Simple promotion without dependencies (early access)"
description: Promote a PingOne resource with no dependencies from a source to a target environment, including setting up promotion variables.
component: pingone
page_id: pingone:early-access-features:ea-p1_config_promotion_scenario_1
canonical_url: https://docs.pingidentity.com/pingone/early-access-features/ea-p1_config_promotion_scenario_1.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-08-13T00:00:00Z
section_ids:
  configure-promotion-variables-in-the-source-environment: Configure promotion variables in the source environment
  steps: Steps
  result: Result
  result-2: Result
  configure-and-run-the-promotion-in-the-source-environment: Configure and run the promotion in the source environment
  steps-2: Steps
  result-3: Result
  verify-the-promotion: Verify the promotion
  steps-3: Steps
  result-4: Result
---

# Scenario 1: Simple promotion without dependencies (early access)

The goal of this scenario is for you to complete the first promotion of the **My First App** application from the **Promotion-Source** environment to the **Promotion-Target** environment. As part of the promotion, you'll also create some promotion variables.

In this first scenario, **My First App** has no dependencies.

## Configure promotion variables in the source environment

As you prepare for your promotion, you've determined that although you want most of the configuration for **My First App** to be the same in both the source and target environments, you want to use different URLs for the **Signoff URLs** and **Redirect URIs** settings. To manage these differences, use promotion variables, which you'll create in the **Promotion-Source** environment.

### Steps

1. Sign on to the PingOne admin console for the **Promotion-Source** environment.

2. Go to **Promote > Promotion Variables** and click **Create Promotion Variable**.

3. In the **Select Target Environment** modal, select **Promotion-Target** in the **Target Environment** list.

4. Select **The correct environment is selected and I want to continue** and click **Confirm**.

   ![A screenshot of the Select Target Environment modal with Promotion-Target selected in the Target Environment list and the confirmation checkbox selected.](_images/p1-promote-select-target-env.png)

   After you confirm the target environment, PingOne determines the resources for which you can create variables.

5. On the **Create Variables** page, in the **Resource Details** section, select **Application** in the **Category** list.

   ![A screen capture of the first page of the Create Variables workflow with the Category list expanded.](_images/p1-promote-scenario1-select-resource-category.png)

   Categories allow you to narrow down the list and find what you're looking for more easily.

   |   |                                                                                                                                                  |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------ |
   |   | You might need to click **Reload resources list** to pick up categories for configuration resources that were recently added to the environment. |

   ### Result

   The subcategory auto-fills with **Web App** because **My First App** is the only application in the environment, and it's an OIDC web application. Because there are no other applications in this environment, **My First App** is also selected automatically in the **Resource** list.

   The **Attributes** list shows all of the application configuration attributes for which you can create variables.

   ![A screen capture of the Create Variables workflow showing Application in the Category field, WEB-APP in the Sub-category field, and My First App in the Resource field.](_images/p1-promote-variables-select-subcat-and-resource.png)

6. Select **Signoff URLs** and **Redirect URIs**, then click **Next**.

   ![A screen capture of the Create Variables workflow showing Application in the Category field](_images/p1-promote-create-variable-select-attributes.png)

7. Set the following variable values to use in the **Promotion-Target** environment.

   The values for the source environment are displayed on the left, and you define the target environment values on the right.

   * **Signoff URLs**: `https://test-myfirstapp.com/signoff`

   * **Redirect URIs**: `https://test-myfirstapp.com`

   ![A screen capture of the second page of the Create Variables workflow showing the source environment values for Signoff URLs and Redirect URIs on the left and fields with new values for the target environment on the right.](_images/p1-promote-set-variables-for-target.png)

8. Click **Next**.

9. On the **Review and Save** page, confirm the variable configuration and click **Save**.

### Result

You're returned to the **Promotion Variables** page. **My First App** is listed in the **Resources with Variables** section.

![A screen capture showing the Promotion Variables page with My First App added to the Resources with Variables list.](_images/p1-promote-variables-with-resource.png)

## Configure and run the promotion in the source environment

To configure the promotion, you'll confirm the target environment and select **My First App** as the resource to promote. Next, you'll decide whether the resource should be created as new in the target environment or mapped to an existing resource. Finally, you'll review the promotion details and run the promotion.

### Steps

1. In the PingOne admin console for the **Promotion-Source** environment, go to **Promote > Promotions**.

2. Click **Run a Promotion**.

3. In the **Confirm Target Environment** modal, ensure that **Promotion-Target** is selected in the **Target Environment** list.

4. Select **The correct environment is selected and I want to continue** and click **Confirm**.

   ![A screenshot of the Confirm Target Environment modal with Promotion-Target selected in the Target Environment list and the confirmation checkbox selected.](_images/p1-promote-confirm-target-env.png)

   After you confirm the target environment, PingOne takes snapshots of the two environments, compares configuration resources, and lists the resources that you can promote.

   ![A screenshot of the Select Resources to Promote page without anything selected.](_images/p1-promote-select-resources.png)

5. On the **Select Resources to Promote** page, search for **My First App** and select it.

   ![A screenshot of the Select Resources to Promote page with app in the search bar and My First App selected.](_images/p1-promote-select-resource-myfirstapp.png)

6. Click **Next**.

   Because this is the first time you're promoting the app to the target environment, you're prompted to map it to a resource in the target environment.

   On the **Map Resources** page, you can see that the promotion service didn't find a corresponding resource in the **Promotion-Target** environment. In this case, you'll promote the app as a new resource.

   ![A screenshot of the Map Resources modal showing My First App in the Source field.](_images/p1-promote-map-resources.png)

7. Click **Confirm and Continue**.

8. On the **Confirm Promotion** page, review the details for the promotion.

   ![A screenshot of the Confirm Promotion page](_images/p1-promote-confirm-promotion-my-first-app.png)

   To view the JSON for the resource you're promoting, click the down arrow on the right side of the table. Viewing the JSON allows you to visually inspect and verify the exact configuration values for the resource before you run the promotion.

   ![A screenshot of the JSON for My First App, showing the configured variables and other details.](_images/p1-promote-confirm-promotion-my-first-app-json.png)

9. Click **Run Promotion**.

### Result

You're returned to the **Promotions** page and the current promotion is listed with a status of **In Progress**. After about 30 seconds, refresh the page. The status will change to **Success** for a successful promotion.

![A screenshot of the Promotions page showing a successful promotion.](_images/p1-promote-promotion-successful.png)

## Verify the promotion

To verify the results of the promotion, first confirm the details of the promotion in the source environment, then ensure that the **My First App** application now exists in the target environment.

### Steps

1. In the PingOne admin console for the **Promotion-Source** environment, go to **Promote > Promotions**.

2. Locate the promotion in the list, click the **More Options** icon (⋮), and select **View**.

   |   |                                                                                                                    |
   | - | ------------------------------------------------------------------------------------------------------------------ |
   |   | Promotions are listed in reverse chronological order, so the most recent promotion appears at the top of the list. |

   * Overview tab

     The **Overview** tab shows information about when the promotion was started and completed, the source and target environments, the status of the promotion, and any release notes that were added.

     ![A screenshot of the Overview tab for the initial promotion of My First App.](_images/p1-promote-promotion-complete-overview-tab-myfirstapp.png)

   * Promoted Resources tab

     The **Promoted Resources** tab shows the details about the resources that were promoted.

     ![A screenshot of the Promoted Resources tab for the initial promotion of My First App.](_images/p1-promote-promotion-complete-promoted-resources-tab.png)

3. On the **Overview** tab, click **View Target Environment**.

   You're taken to the PingOne admin console for the target environment so that you can confirm that the promoted resources exist and match what you expect.

4. For this scenario, go to **Applications > Applications**, browse or search for **My First App**, and click it to open the details panel.

   ![A screenshot of the details panel for the My First app application in the target environment](_images/p1-promote-verify-in-target-my-first-app.png)

### Result

**My First App** now exists in the **Promotion-Target** environment, and the values for the **Signoff URLs** and **Redirect URIs** match the values you configured when you [configured the variables](#configure-promotion-variables-in-the-source-environment) for the promotion.