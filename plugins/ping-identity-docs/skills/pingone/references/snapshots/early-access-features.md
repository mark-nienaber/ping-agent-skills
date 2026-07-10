---
component: pingone
page_id: pingone:early-access-features:ea_p1_create_provisioning_connection_gateway
canonical_url: https://docs.pingidentity.com/pingone/early-access-features/ea_p1_create_provisioning_connection_gateway.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
---

---

---
title: Audit report (early access)
description: Provides a detailed view of audit events in PingOne for the selected environment, including event details, timestamps,
component: pingone
page_id: pingone:early-access-features:ea-p1_audit_report
canonical_url: https://docs.pingidentity.com/pingone/early-access-features/ea-p1_audit_report.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 8, 2026
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
revdate: December 8, 2025
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
revdate: July 2, 2026
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

|   |                                                                                                                                                                                                                                                                                                                                                                                            |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | This feature is now available for early access in PingOne. Early access features and APIs are provided for preview purposes only and might change in the final version. Learn more about early access in [PingOne Early Access Features](p1_early_access_features.html) and [Managing opt-ins for early access features in PingOne](../settings/p1_managing_opt_ins_for_ea_features.html). |

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
revdate: December 1, 2025
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
revdate: October 1, 2025
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
title: DaVinci administrative audit events in PingOne (early access)
description: DaVinci administrative audit events are available in the PingOne audit report with unified filtering, retention, and webhook streaming.
component: pingone
page_id: pingone:early-access-features:ea_p1_davinci_audit_events
canonical_url: https://docs.pingidentity.com/pingone/early-access-features/ea_p1_davinci_audit_events.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 26, 2026
section_ids:
  accessing-davinci-audit-events: Accessing DaVinci audit events
  retention-and-retrieval: Retention and retrieval
  filtering-davinci-events: Filtering DaVinci events
  filter-by-resource-type: Filter by resource type
  filter-by-event-type: Filter by event type
  filter-by-resource-id: Filter by resource ID
  davinci-audit-event-reference: DaVinci audit event reference
  audit-event-structure: Audit event structure
  standard-fields: Standard fields
  davinci-specific-_embedded-fields: DaVinci-specific _embedded fields
  api-access: API access
---

# DaVinci administrative audit events in PingOne (early access)

PingOne DaVinci administrative audit events are integrated into the PingOne centralized audit schema. DaVinci events appear alongside standard PingOne events in **Monitoring > Audit** and are subject to the same retention, retrieval, filtering, and webhook streaming capabilities. Learn more in [Audit](../monitoring/p1_reporting.html).

## Accessing DaVinci audit events

DaVinci audit events are visible in **Monitoring > Audit**. They appear alongside standard PingOne events and can be filtered to show only DaVinci-related activity.

Learn more about running audit reports in [Audit](../monitoring/p1_reporting.html).

### Retention and retrieval

Use the following retention windows to determine whether your audit data is available immediately or requires a retrieval request:

| Data age           | Availability                                                                               |
| ------------------ | ------------------------------------------------------------------------------------------ |
| Up to 14 days      | Available immediately in the PingOne admin console and through the API                     |
| Older than 14 days | Request retrieval from the **Audit** page. A prompt is displayed before results are shown. |

## Filtering DaVinci events

Use the available filters to narrow audit results by DaVinci resource type, event type, or a specific resource ID.

### Filter by resource type

In the **Filter Type** panel, select **Resource Type**. A **DaVinci** subsection is available with the following filters:

| Filter value              | Covers                              |
| ------------------------- | ----------------------------------- |
| **DaVinci Flows**         | Flow events and flow version events |
| **DaVinci Connectors**    | Connector instance events           |
| **DaVinci Variables**     | Variable events                     |
| **DaVinci Applications**  | Application events                  |
| **DaVinci Flow Policies** | Flow policy events                  |
| **DaVinci UI Templates**  | UI template events                  |

### Filter by event type

Select **Event Type** in the filter panel. All granular DaVinci event types are listed and multiple event types can be selected simultaneously.

### Filter by resource ID

Enter a flow ID, variable ID, connector instance ID, flow policy ID, application ID, or UI template ID in the **Resource ID** filter to scope results to a specific DaVinci resource.

## DaVinci audit event reference

The following 37 DaVinci administrative events are logged in PingOne.

|   |                                                                                                                                                                                                                                                                                                                                                                                             |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Rows 12 – 17 share the `DAVINCI.FLOW.CUSTOM_JAVASCRIPT.ADDED` action type for both flow-level and connector-level events. Differentiate by the `resources[].type` field: `DAVINCI_FLOW` for flow events (rows 12 – 15) and `DAVINCI_CONNECTOR` for connector events (rows 16 – 17). The context (direct creation, clone, or import) is reflected in `_embedded.davinciFlow.creationSource`. |

| #  | Action type (`action.type`)                      | Event type (`action.description`)              | Example description (`result.description`)                                                                |
| -- | ------------------------------------------------ | ---------------------------------------------- | --------------------------------------------------------------------------------------------------------- |
| 1  | `DAVINCI.FLOW.CREATED`                           | DaVinci Flow Created                           | Created DaVinci Flow '{name}'                                                                             |
| 2  | `DAVINCI.FLOW.UPDATED`                           | DaVinci Flow Updated                           | Updated DaVinci Flow '{name}'                                                                             |
| 3  | `DAVINCI.FLOW.DELETED`                           | DaVinci Flow Deleted                           | Deleted DaVinci Flow '{name}'                                                                             |
| 4  | `DAVINCI.FLOW.DEPLOYED`                          | DaVinci Flow Deployed                          | Deployed DaVinci Flow '{name}'                                                                            |
| 5  | `DAVINCI.FLOW.CLONED`                            | DaVinci Flow Cloned                            | Cloned DaVinci Flow 'CLONE-{name}' from '\\{source name}'                                                 |
| 6  | `DAVINCI.FLOW.IMPORTED`                          | DaVinci Flow Imported                          | Imported DaVinci Flow '{name}'                                                                            |
| 7  | `DAVINCI.FLOW.ENABLED`                           | DaVinci Flow Enabled                           | Enabled DaVinci Flow '{name}'                                                                             |
| 8  | `DAVINCI.FLOW.DISABLED`                          | DaVinci Flow Disabled                          | Disabled DaVinci Flow '{name}'                                                                            |
| 9  | `DAVINCI.FLOW.DEBUG_LOGGING.ENABLED`             | DaVinci Flow Debug Logging Enabled             | Debug logging enabled for DaVinci Flow '{name}'                                                           |
| 10 | `DAVINCI.FLOW.DEBUG_LOGGING.DISABLED`            | DaVinci Flow Debug Logging Disabled            | Debug logging disabled for DaVinci Flow '{name}'                                                          |
| 11 | `DAVINCI.COMPANY.ENABLE_ANALYTICS_DEBUG_VIEW`    | DaVinci Company Debug Logging Enabled          | Debug logging for Analytics enabled from Company Settings                                                 |
| 12 | `DAVINCI.FLOW.CUSTOM_JAVASCRIPT.ADDED`           | DaVinci Flow Custom JavaScript Added           | Custom JavaScript added during flow creation for DaVinci Flow '{name}'                                    |
| 13 | `DAVINCI.FLOW.CUSTOM_JAVASCRIPT.ADDED`           | DaVinci Flow Custom JavaScript Added           | Custom JavaScript added during flow cloning for DaVinci Flow '{name}'                                     |
| 14 | `DAVINCI.FLOW.CUSTOM_JAVASCRIPT.ADDED`           | DaVinci Flow Custom JavaScript Added           | Custom JavaScript added during flow import for DaVinci Flow '{name}'                                      |
| 15 | `DAVINCI.FLOW.CUSTOM_JAVASCRIPT.UPDATED`         | DaVinci Flow Custom JavaScript Updated         | Custom JavaScript updated in DaVinci Flow '{name}'                                                        |
| 16 | `DAVINCI.FLOW.CUSTOM_JAVASCRIPT.ADDED`           | DaVinci Connector Custom JavaScript Added      | Custom JavaScript added in '\\{connector name}' Connector Configurations                                  |
| 17 | `DAVINCI.FLOW.CUSTOM_JAVASCRIPT.ADDED`           | DaVinci Connector Custom JavaScript Updated    | Custom JavaScript updated in '\\{connector name}' Connector Configurations                                |
| 18 | `DAVINCI.FLOW.VERSION.REVERTED`                  | DaVinci Flow Version Reverted                  | Flow version reverted from version {n} to version {m}, new version created: {p} for DaVinci Flow '{name}' |
| 19 | `DAVINCI.FLOW.VERSION.ALIAS.UPDATED`             | DaVinci Flow Version Alias Updated             | Flow version alias updated for \\{flow name} (version {n}: {alias})                                       |
| 20 | `DAVINCI.FLOW.VERSION.DELETED`                   | DaVinci Flow Version Deleted                   | Flow version {n} deleted for DaVinci Flow '{name}'                                                        |
| 21 | `DAVINCI.FLOW.SESSION.CONFIGURATIONS.ADDED`      | DaVinci Flow Session Configurations Added      | Session configurations added in DaVinci Flow '{name}'                                                     |
| 22 | `DAVINCI.FLOW.SESSION.CONFIGURATIONS.OVERRIDDEN` | DaVinci Flow Session Configurations Overridden | Session configurations overridden in DaVinci Flow '{name}'                                                |
| 23 | `DAVINCI.CONNECTOR.CREATED`                      | DaVinci Connector Created                      | Created DaVinci Connector '{name}'                                                                        |
| 24 | `DAVINCI.CONNECTOR.UPDATED`                      | DaVinci Connector Updated                      | Updated DaVinci Connector '{name}'                                                                        |
| 25 | `DAVINCI.CONNECTOR.DELETED`                      | DaVinci Connector Deleted                      | Deleted DaVinci Connector '{name}'                                                                        |
| 26 | `DAVINCI.VARIABLE.CREATED`                       | DaVinci Variable Created                       | Created DaVinci Variable '{name}'                                                                         |
| 27 | `DAVINCI.VARIABLE.UPDATED`                       | DaVinci Variable Updated                       | Updated DaVinci Variable '{name}'                                                                         |
| 28 | `DAVINCI.VARIABLE.DELETED`                       | DaVinci Variable Deleted                       | Deleted DaVinci Variable '{name}'                                                                         |
| 29 | `DAVINCI.FLOW_POLICY.CREATED`                    | DaVinci Flow Policy Created                    | Created DaVinci Flow Policy '{name}'                                                                      |
| 30 | `DAVINCI.FLOW_POLICY.UPDATED`                    | DaVinci Flow Policy Updated                    | Updated DaVinci Flow Policy '{name}'                                                                      |
| 31 | `DAVINCI.FLOW_POLICY.DELETED`                    | DaVinci Flow Policy Deleted                    | Deleted DaVinci Flow Policy '{name}'                                                                      |
| 32 | `DAVINCI.APPLICATION.CREATED`                    | DaVinci Application Created                    | Created DaVinci Application '{name}'                                                                      |
| 33 | `DAVINCI.APPLICATION.UPDATED`                    | DaVinci Application Updated                    | Updated DaVinci Application '{name}'                                                                      |
| 34 | `DAVINCI.APPLICATION.DELETED`                    | DaVinci Application Deleted                    | Deleted DaVinci Application '{name}'                                                                      |
| 35 | `DAVINCI.UI_TEMPLATE.CREATED`                    | DaVinci UI Template Created                    | Created DaVinci UI Template '{name}'                                                                      |
| 36 | `DAVINCI.UI_TEMPLATE.UPDATED`                    | DaVinci UI Template Updated                    | Updated DaVinci UI Template '{name}'                                                                      |
| 37 | `DAVINCI.UI_TEMPLATE.DELETED`                    | DaVinci UI Template Deleted                    | Deleted DaVinci UI Template '{name}'                                                                      |

## Audit event structure

DaVinci audit events follow the standard PingOne audit event structure with DaVinci-specific `_embedded` fields.

### Standard fields

| Field                               | Description                                                                                                                        |
| ----------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| `id`                                | Unique audit event ID                                                                                                              |
| `recordedAt`                        | ISO 8601 timestamp when the event was recorded                                                                                     |
| `correlationId`                     | Request correlation ID                                                                                                             |
| `internalCorrelation.transactionId` | Internal DaVinci transaction ID                                                                                                    |
| `actors.client.name`                | Client application that performed the action (for example, `adminui`)                                                              |
| `actors.user.name`                  | User who performed the action (PingOne user email)                                                                                 |
| `actors.user.id`                    | PingOne user ID (UUID)                                                                                                             |
| `source.ipAddress`                  | IP address of the request origin                                                                                                   |
| `source.userAgent`                  | User-agent string                                                                                                                  |
| `action.type`                       | Machine-readable event type (for example, `DAVINCI.FLOW.CREATED`)                                                                  |
| `action.description`                | Human-readable event type label                                                                                                    |
| `resources[].type`                  | Resource type (for example, `DAVINCI_FLOW`, `DAVINCI_CONNECTOR`, `DAVINCI_VARIABLE`, `DAVINCI_APPLICATION`, `DAVINCI_UI_TEMPLATE`) |
| `resources[].id`                    | Resource ID                                                                                                                        |
| `resources[].name`                  | Resource name                                                                                                                      |
| `result.status`                     | `SUCCESS` or `FAILURE`                                                                                                             |
| `result.description`                | Human-readable result description                                                                                                  |

### DaVinci-specific `_embedded` fields

* `_embedded.davinciFlow`

  The following fields are present on flow events:

  | Field                | Description                                                                                           |
  | -------------------- | ----------------------------------------------------------------------------------------------------- |
  | `flowId`             | DaVinci internal flow ID                                                                              |
  | `flowName`           | Human-readable flow name                                                                              |
  | `flowStatus`         | `ACTIVE`, `DISABLED`, or similar                                                                      |
  | `logLevel`           | Current log level: `ERROR`, `DEBUG`, or `INFO`                                                        |
  | `flowType`           | Trigger type: `DEFAULT`, `PINGONE`, `SCHEDULED`, or similar                                           |
  | `flowVersion`        | Flow version number (present on update, enable, and disable events)                                   |
  | `modifiedAttributes` | Array of attribute paths changed during an update (for example, `graphData`, `flowSettings.logLevel`) |
  | `creationSource`     | On custom JavaScript add events: `DIRECT`, `CLONE`, or `IMPORT`                                       |
  | `targetNodeId`       | Node IDs containing the custom JavaScript                                                             |

* `_embedded.davinciFlowVersion`

  The following fields are present on flow version events:

  | Field                 | Description                                |
  | --------------------- | ------------------------------------------ |
  | `flowVersion`         | Version number affected                    |
  | `revertSourceVersion` | Source version number (revert events only) |
  | `flowVersionAlias`    | Version alias string                       |
  | `previousAlias`       | Previous alias value before update         |

* `_embedded.davinciConnector`

  The following fields are present on connector custom JavaScript events:

  | Field                  | Description                                 |
  | ---------------------- | ------------------------------------------- |
  | `connectorInstanceId`  | Connector instance ID                       |
  | `connectorDisplayName` | Display name of the connector instance      |
  | `connectorType`        | Connector type (for example, `PingOne MFA`) |
  | `connectorCategory`    | Connector category                          |

* `_embedded.companySettings`

  The following fields are present on company-level debug logging events:

  | Field                      | Description                                  |
  | -------------------------- | -------------------------------------------- |
  | `enableAnalyticsDebugView` | `true` when company debug logging is enabled |

## API access

DaVinci audit events are accessible through the standard PingOne Activities API:

```
GET /v1/environments/{environmentId}/activities
```

Filter by DaVinci event types using standard PingOne audit filter parameters. For example, `filter=action.type sw "DAVINCI"`.

Learn more in [Audit Activities](https://developer.pingidentity.com/pingone-api/platform/audit-activities.html) in the PingOne API documentation.

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
revdate: April 16, 2026
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
title: New Authentication Dashboard (early access)
description: The Authentication Dashboard shows a summary of SSO and authentication activity through PingOne authentication.
component: pingone
page_id: pingone:early-access-features:ea-p1_auth_dashboard
canonical_url: https://docs.pingidentity.com/pingone/early-access-features/ea-p1_auth_dashboard.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: April 7, 2025
section_ids:
  limitations: Limitations
  accessing-the-dashboard: Accessing the dashboard
  filters: Filters
  charts: Charts
  total-successful-authentications: Total Successful Authentications
  successful-authentications: Successful Authentications
  total-identities: Total Identities
  total-unsuccessful-authentication-attempts: Total Unsuccessful Authentication Attempts
  unsuccessful-authentication-attempts: Unsuccessful Authentication Attempts
  total-password-resets: Total Password Resets
  password-resets: Password Resets
  successful-authentications-by-dayhour: Successful Authentications by Day/Hour
---

# New Authentication Dashboard (early access)

For the purposes of early access, this topic describes the new Authentication Dashboard.

The **Authentication Dashboard** shows a summary of authentication activity through PingOne authentication for the selected environment, including:

* Single sign-on (SSO) activity.

* User self-registration events.

* PingOne DaVinci success flows from successful authentication attempts.

* DaVinci failed flows from unsuccessful authentication attempts.

* Authentication through external identity providers (IdPs) configured in PingOne.

## Limitations

The Authentication Dashboard doesn't display the following activity:

* DaVinci authentication attempts that result in a timeout or user abandonment

* DaVinci authentications through social login connectors that bypass the DaVinci flow orchestration service, such as passwordless-only flows or sign-on with social accounts like Google

* DaVinci authentications that succeed after the user falls back to a previous authentication method following an initial failure

* Guest checkouts when a user is unable to sign on to their existing account and proceeds as a guest instead

## Accessing the dashboard

To access the **Authentication Dashboard**, in the PingOne admin console, go to **Monitoring > Authentication**.

![A screenshot of the Authentication Dashboard](_images/p1-authentication-dashboard.png)

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

|   |                                                                        |
| - | ---------------------------------------------------------------------- |
|   | The Authentication Dashboard displays data only for the past 6 months. |

## Charts

Use the following controls to adjust the charts:

| Icon                                                                | Name         | Description                                                                                                                                                                                       |
| ------------------------------------------------------------------- | ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ![The Maximize icon.](../_images/p1-dashboard-maximize.png)         | Maximize     | Expands the chart to fill the dashboard.To minimize the chart, click the icon again.                                                                                                              |
| ![The Menu options icon.](../_images/p1-dashboard-menu-options.png) | Menu options | Options can vary for different types of charts:- **View summary data**: Displays chart data as a table.

- **Export**: Exports chart data to CSV or Excel format, depending on the type of chart. |
| ![The Sort visual icon.](../_images/p1-dashboard-sort-visual.png)   | Sort visual  | Sorts the chart data in ascending or descending order.                                                                                                                                            |

### Total Successful Authentications

Displays the total number of successful authentication attempts during the selected time period.

### Successful Authentications

Displays a bar chart showing the total number of successful authentication attempts by date and a rolling average line for the selected time period. Hover over a bar to view the number of authentications for that date.

### Total Identities

Displays the total number of users in the PingOne directory for the selected time period and a graph showing the total user count by date.

### Total Unsuccessful Authentication Attempts

Displays the total number of unsuccessful authentication attempts, including account lockouts and timeouts, during the specified time period.

### Unsuccessful Authentication Attempts

Displays a bar chart of unsuccessful authentication attempts, including account lockouts and timeouts, by date, and a rolling average line for the selected time period. Hover over a bar to view the number of unsuccessful attempts for that date.

### Total Password Resets

Displays the total number of times users successfully reset their password during the selected time period.

### Password Resets

Displays a bar chart of times users successfully reset their password by date and a rolling average line for the selected time period. Hover over a bar to view the number of successful password resets for that date.

### Successful Authentications by Day/Hour

Displays a heat map of average authentication activity by hour of the day and day of the week in the end user's local time zone. The color variations show usage trends throughout an average week.

Hover over the map to see the actual average of successful authentications to more accurately quantify the variation between periods. You can use this information to better understand user habits and identify periods of interest, such as typical highs and lows for authentication attempts.

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
title: PingOne Early Access Features
description: This section provides early access documentation for the PingOne features available to customers who opt in to preview new functionality.
component: pingone
page_id: pingone:early-access-features:ea-p1_early_access_features
canonical_url: https://docs.pingidentity.com/pingone/early-access-features/ea-p1_early_access_features.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
---

# PingOne Early Access Features

This section provides early access documentation for the PingOne features available to customers who opt in to preview new functionality.

Early access features can be enabled only at the environment level. You can't enable an early access feature for an entire organization.

Not all features are enabled for early access. Additionally, early access features related to services that aren't in the environment or that aren't allowable by the license assigned to the environment aren't available for opt-in.

Learn more in [Managing opt-ins for early access features in PingOne](../settings/p1_managing_opt_ins_for_ea_features.html).

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Early access features are provided for preview purposes only and aren't covered under standard Support service level agreements (SLAs). You can open support cases for feedback, bug reports, configuration questions, or other inquiries related to early access features, but resolution times for these cases will vary. These cases often require collaboration with our Engineering and Product teams, so timelines might exceed the usual SLAs for your Support package.Topics for these features are draft documentation for early access purposes only and aren't complete or final. |

* [Configuration management and promotion (early access)](ea-p1_promote.html)

* [New Authentication Dashboard (early access)](ea-p1_auth_dashboard.html)

* [New email and banner alerts for approaching license entitlement limits (early access)](ea-p1_license_entitlement_limit_alerts.html)

---

---
title: PingOne Early Access Features
description: This section provides early access documentation for the PingOne features available to customers who opt in to preview new functionality.
component: pingone
page_id: pingone:early-access-features:p1_early_access_features
canonical_url: https://docs.pingidentity.com/pingone/early-access-features/p1_early_access_features.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
---

# PingOne Early Access Features

This section provides early access documentation for the PingOne features available to customers who opt in to preview new functionality.

Early access features can be enabled only at the environment level. You can't enable an early access feature for an entire organization.

Not all features are enabled for early access. Additionally, early access features related to services that aren't in the environment or that aren't allowable by the license assigned to the environment aren't available for opt-in.

Learn more in [Managing opt-ins for early access features in PingOne](../settings/p1_managing_opt_ins_for_ea_features.html).

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Early access features are provided for preview purposes only and aren't covered under standard Support service level agreements (SLAs). You can open support cases for feedback, bug reports, configuration questions, or other inquiries related to early access features, but resolution times for these cases will vary. These cases often require collaboration with our Engineering and Product teams, so timelines might exceed the usual SLAs for your Support package.Topics for these features are draft documentation for early access purposes only and aren't complete or final. |

* [Configuration management and promotion (early access)](ea-p1_promote.html)

* [New Authentication Dashboard (early access)](ea-p1_auth_dashboard.html)

* [New email and banner alerts for approaching license entitlement limits (early access)](ea-p1_license_entitlement_limit_alerts.html)

* [Audit report (early access)](ea-p1_audit_report.html)

* [DaVinci administrative audit events in PingOne (early access)](ea_p1_davinci_audit_events.html)

* [Configuring a custom push notification provider (early access)](ea-p1_configure_custom_push_provider.html)

* [Provisioning the PingOne connection with PingOne environments (early access)](ea_p1_provisioning_connection_pingone.html)

---

---
title: Promotion variables (early access)
description: Define and manage variables for use in PingOne configuration promotion.
component: pingone
page_id: pingone:early-access-features:ea-p1_promotion_variables
canonical_url: https://docs.pingidentity.com/pingone/early-access-features/ea-p1_promotion_variables.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
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
revdate: MMMM D, YYYY
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
title: Provisioning the PingOne connection with PingOne environments (early access)
description: The PingOne provisioning connection links two environments, either within the same organization or across different organizations.
component: pingone
page_id: pingone:early-access-features:ea_p1_provisioning_connection_pingone
canonical_url: https://docs.pingidentity.com/pingone/early-access-features/ea_p1_provisioning_connection_pingone.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: April 10, 2026
section_ids:
  provisioning-capabilities: Provisioning capabilities
  before-you-begin: Before you begin
  steps: Steps
  result: Result:
  validation: Validation
  pingone-directory-attributes: PingOne directory attributes
---

# Provisioning the PingOne connection with PingOne environments (early access)

The PingOne provisioning connection links two environments, either within the same organization or across different organizations. By integrating the PingOne connection with PingOne, you can automate the lifecycle of user identities and groups, ensuring that access between your source and target environments is synchronized.

## Provisioning capabilities

| Resource   | Capability     | Description                                                                                                                              | Inbound | Outbound |
| ---------- | -------------- | ---------------------------------------------------------------------------------------------------------------------------------------- | ------- | -------- |
| User       | Create         | Generates a new user record in the destination.                                                                                          | Yes     | Yes      |
|            | Read           | Retrieves or polls user attributes for synchronization.                                                                                  | Yes     | Yes      |
|            | Update         | Modifies existing attributes, such as `job title`.                                                                                       | Yes     | Yes      |
|            | Delete         | Deletes a user or temporarily suspends an account.                                                                                       | Yes     | Yes      |
| Group      | Create         | Provisions a new group in the target application.&#xA;&#xA;Only internal and native PingOne groups are supported for group provisioning. | No      | Yes      |
|            | Rename         | Updates the display name or identifier of an existing group.                                                                             | No      | Yes      |
|            | Delete         | Removes a group from the target application.                                                                                             | No      | Yes      |
| Membership | Add and remove | Handles additions and removals of users within groups.                                                                                   | No      | Yes      |

## Before you begin

Make sure that you have:

* Administrator access to both the source and target PingOne environments in the same or cross organization.

* The necessary API access and administrator approvals to test and confirm the connection works.

* Created a worker application for OAuth authentication in the target PingOne environment and assign the following roles:

  * **Environment Admin**

  * **Identity Data Admin**

  * **Identity Data Read Only**

  * **Organization Admin**

* The following PingOne configuration values required for OAuth or Token authentication:

  * **Service URI**

  * **Environment ID**

  * **Authentication Method**

  * **Client ID**

  * **Client Secret**

  * **Token Endpoint**

  * **Grant Type**

  * **Authentication Token**

* Users assigned to a specific population or group in PingOne designated for provisioning. Learn more in [Adding a user in PingOne](../directory/p1_adduser.html) and [Managing groups](../directory/p1_managing_groups.html).

## Steps

1. Create a PingOne connection:

   1. In the PingOne admin console, go to **Integrations > Provisioning**.

   2. Click the **Plus** icon (+) and then click **New Connection**.

   3. Click **Select** for **Identity Store**.

   4. Click **Select** for the **PingOne** connection, and click **Next**.

   5. []()In the **Configure Authentication** section, enter the following configurations that apply to your PingOne account:

      * **Authentication Method**: Select one of the following:

        * **OAUTH**: Enter the following:

          | Configuration      | Example                                             |
          | ------------------ | --------------------------------------------------- |
          | **Service URI**    | `https://api.test-one-pingone.com/v1`               |
          | **Environment ID** | `11111111-2222-3333-4444-555555555555`              |
          | **Client ID**      | `aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee`              |
          | **Client Secret**  | `example-client-secret`                             |
          | **Token Endpoint** | `https://auth.test-one-pingone.com/env_id/as/token` |
          | **Grant Type**     | `client_credentials`                                |

        * **Token**: Enter the **Authentication Token**, such as `example-authentication-token`.

   6. Click **Test Connection** to verify that PingOne can establish a connection.

      ### Result:

      If there are any issues with the connection, a **Test Connection Failed** modal opens. Click **Next** to resume the setup with an invalid connection.

      |   |                                                                                                                                                                                                                                                                                                               |
      | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      |   | You can't use the connection for provisioning until you've established a valid connection. If the connection fails, click **Cancel** in the **Test Connection Failed** modal, verify that you have entered the configuration details in [step e](#p1_configure_authentication_step) correctly, and try again. |

   7. Click **Next**.

   8. In the **User Actions** section, select the following as needed:

      | Field                        | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
      | ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
      | **Enable users creation**    | Creates a user in the target identity store when the user is created in the source identity store.                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
      | **Enable users updation**    | Updates user attributes in the target identity store when the user is updated in the source identity store.If **Enable users updation** is selected, you can choose to select **Enable users disable**, which disables a user in the target identity store when the user is disabled in the source identity store.                                                                                                                                                                                                                                     |
      | **Enable users deprovision** | Deprovisions a user in the target identity store when the user is deprovisioned in the source identity store. If **Enable users deprovision** is selected, the following options appear:- **Remove Action**: Removes or disables a user in the target identity store when the user is deleted in the source identity store. Select **Delete** or **Disable**.

        &#xA;&#xA;Remove Action is only available if you select Enable users disable.

      - **Deprovision on rule deletion**: Deprovisions users if the associated provisioning rule is deleted. |

   9. Click **Save**.

   10. To enable the connection, click the toggle at the top of the details panel to the right (blue).

       |   |                                                                           |
       | - | ------------------------------------------------------------------------- |
       |   | You can disable the connection by clicking the toggle to the left (gray). |

2. Create an [inbound](../integrations/p1_create_provisioning_rule_inbound.html) or [outbound](../integrations/p1_create_provisioning_rule_outbound.html) rule and select the existing PingOne connection as the target or source. You can optionally add [attribute mappings](#pingone-directory-attributes).

## Validation

Confirm users and groups are successfully provisioned to PingOne. View the [sync status](../integrations/p1_view_sync_status.html) to review synchronization results and any errors. You can find examples in [Outbound provisioning sync summary examples](../integrations/p1_outbound_group_provisioning_sync_summary_examples.html).

## PingOne directory attributes

The following table lists common PingOne attributes that can be mapped for user provisioning:

| Attribute       | Description                                                                 |
| --------------- | --------------------------------------------------------------------------- |
| `Username`      | The username value used for the target account.                             |
| `Email`         | The email address mapped from PingOne Directory.                            |
| `Enabled`       | Indicates whether the target user account is enabled.                       |
| `Given Name`    | The user's first name.                                                      |
| `Family Name`   | The user's last name.                                                       |
| `Population ID` | The unique identifier of the target population where users are provisioned. |

---

---
title: Rolling back a promotion (early access)
description: Roll back a promotion to reset the target environment back to the state it was in immediately prior to the promotion.
component: pingone
page_id: pingone:early-access-features:ea-p1_promotion_rolling_back
canonical_url: https://docs.pingidentity.com/pingone/early-access-features/ea-p1_promotion_rolling_back.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: February 23, 2026
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
description: Learn how to promote a PingOne resource that has no dependencies and understand how to configure promotion variables for the promotion.
component: pingone
page_id: pingone:early-access-features:ea-p1_config_promotion_scenario_1
canonical_url: https://docs.pingidentity.com/pingone/early-access-features/ea-p1_config_promotion_scenario_1.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: December 8, 2025
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