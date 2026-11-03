---
title: Adobe Admin Console
description: Configure the Advanced Identity Cloud Adobe Admin Console application to manage users, groups, and memberships with Adobe Admin Console
component: pingoneaic
page_id: pingoneaic:app-management:applications/adobe-admin-console
canonical_url: https://docs.pingidentity.com/pingoneaic/app-management/applications/adobe-admin-console.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
page_aliases: ["release-notes:rapid-channel/adobe-admin-console-app.adoc"]
section_ids:
  register-the-application: Register the application
  adobe-admin-console-requirements: Adobe Admin Console requirements
  configure-the-provisioner: Configure the provisioner
  configure-provisioning-and-reconciliation-resources: Configure provisioning and reconciliation resources
---

# Adobe Admin Console

The Advanced Identity Cloud Adobe Admin Console application lets you manage users, groups, and user group memberships between Adobe Admin Console and Advanced Identity Cloud. This application requires an Adobe Admin Console administrator account and a properly configured Adobe Admin Console.

## Register the application

1. In the Advanced Identity Cloud admin console, go to Applications > Applications, and click [icon: grid_view, set=material, size=inline] Browse App Catalog.

2. In the Browse App Catalog modal, select an application, and click Next.

3. Review the Application Integration information, and click Next.

4. In the Application Details window, specify the name, description, application owners, and logo for the application.

5. To make the application an [Authoritative](../register-an-application.html#target_and_authoritative_applications) source of identity data, select the Authoritative check box. This option is not available for every application.

6. Click Create Application.

## Adobe Admin Console requirements

|   |                                                                                                                                              |
| - | -------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The steps for configuring Adobe Admin Console should be used as an outline, as the specific options, menus, and features could have changed. |

Before you can configure the Advanced Identity Cloud application, you must create and configure a project in Adobe Admin Console. You need an Adobe Admin Console developer account to complete this procedure:

1. Create or log in to an [Adobe Admin Console developer account](https://developer.adobe.com/console/home/).

2. From the Adobe Developer Console, click the [Projects tab](https://developer.adobe.com/console/projects), and then click Create new project.

   > **Collapse: Show Me**
   >
   > ![Create a project in the Adobe Developer Console](../_images/adobe-admin-console-create-project.png)

3. On the Project Name page, click Add API.

   > **Collapse: Show Me**
   >
   > ![Adobe Developer Console, add API](../_images/adobe-admin-console-add-api.png)

4. In the Add an API window, select User Management API, and click Next.

   > **Collapse: Show Me**
   >
   > ![Adobe Admin Console, Add User Management API](../_images/adobe-admin-console-add-user-mgmt-api.png)

5. In the Add Credential area, select OAuth Server-to-Server, enter a Credential name, and then click Save configured API.

   > **Collapse: Show Me**
   >
   > ![Add credential area of the Add an API flow](../_images/adobe-admin-console-api-credential.png)

6. On the Project Name > User Management API page, in the Connected credentials area, click the credential you just added (OAuth Server-to-Server).

   > **Collapse: Show Me**
   >
   > ![Adobe Developer Console, connected credentials](../_images/adobe-admin-console-connected-credentials.png)

7. From the Credential detail tab, make note of the following:

   * CLIENT ID

   * CLIENT SECRET

   * SCOPES

   * ORGANIZATION ID

   > **Collapse: Show Me**
   >
   > ![Adobe Developer Console, credentials tab](../_images/adobe-admin-console-credentials-tab.png)

   Use these values when you configure provisioning for an Advanced Identity Cloud Adobe Admin Console application.

## Configure the provisioner

After you register the application, you can configure provisioning.

1. Complete [Adobe Admin Console requirements](#adobe-admin-console-requirements).

2. In the Advanced Identity Cloud admin console, on the Provisioning tab:

   * If setting up provisioning for the first time, click Set up Provisioning.

   * If editing existing settings, in the Connection area, click Settings.

3. Configure the following fields:

   | Field                    | Description                                                                                                                                                               |
   | ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | Service URI              | The service endpoint URI.                                                                                                                                                 |
   | Organization ID          | Your organization's unique ID. For example, `12345@AdobeOrg`.Refer to [Adobe Admin Console requirements](#adobe-admin-console-requirements) for help locating this value. |
   | Token Endpoint           | The endpoint to query for a new access token.                                                                                                                             |
   | Client ID                | The client ID for OAuth 2.0 flow\.Refer to [Adobe Admin Console requirements](#adobe-admin-console-requirements) for help locating this value.                            |
   | Client Secret (optional) | The client secret for OAuth 2.0 flow\.Refer to [Adobe Admin Console requirements](#adobe-admin-console-requirements) for help locating this value.                        |

4. Optionally, click Show advanced settings to set any of the following options:

   **Application specific settings**

   | Field                 | Description                                                                                                                                |
   | --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
   | Scope (optional)      | The OAuth 2.0 scope(s) to use.Refer to [Adobe Admin Console requirements](#adobe-admin-console-requirements) for help locating this value. |
   | Group Read Rate Limit | Defines throttling for group read operations either per second ("30/sec") or per minute ("100/min").                                       |
   | User Read Rate Limit  | Defines throttling for user read operations either per second ("30/sec") or per minute ("100/min").                                        |
   | Write Rate Limit      | Defines throttling for write operations (create/update/delete) either per second ("30/sec") or per minute ("100/min").                     |
   | Maximum Connections   | The maximum size of the HTTP connection pool. The default is 10 connections.                                                               |
   | Connection Timeout    | The timeout for the underlying HTTP connection in seconds. The default is 30 seconds.                                                      |

   **Pool configuration**

   | Field                                   | Description                                                                                                                                                                           |
   | --------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | Max idle and active container instances | The maximum number of idle and active container instances. The default value is `10`.                                                                                                 |
   | Max Idle Connector Instances            | The maximum number of idle connector instances. The default value is `10`.                                                                                                            |
   | Set Timeout Period                      | Select to enable a timeout period for the connection. After enabling, configure the following:- Timeout period (ms): The timeout period in milliseconds.                              |
   | Set Minimum Idle Time                   | Select to set a minimum time (in milliseconds) before an idle object is removed. After enabling, configure the following:- Min idle time (ms): The minimum idle time in milliseconds. |
   | Min Idle Instances                      | The minimum number of idle connector instances.                                                                                                                                       |

   **Result Handler configuration**

   | Field                                                                   | Description                                                                       |
   | ----------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
   | Enable for connectors with the attribute normalizer interface           | Enables the attribute normalizer interface for supported connectors.              |
   | Enable local filtering/search features                                  | Enables local filtering and search capabilities.                                  |
   | Enable case insensitive filter                                          | Configures filters to ignore case sensitivity.                                    |
   | Enable configuration of search attributes; disable for local connectors | Enables search attribute configuration. Disable this option for local connectors. |

   1. In the Operation Timeouts (ms) area, select the operations to enforce timeouts on and enter the duration in milliseconds.

      Available operations include Create, Validate, Test, Enable a Script on the Connector, Schema, Delete, Update, Sync, Authenticate, Get, Enable a Script on the Target, and Search.

   2. In the Operation Rate Limits area, select the operations to enforce rate limits on.

      You can enforce limits on specific operations, including Create, Validate, Test, Script on Connector, Schema, Delete, Update, Sync, Authenticate, Get, Script on Target, and Search.

      For each selected operation, configure the following fields:

      | Field           | Description                        |
      | --------------- | ---------------------------------- |
      | Request Limit   | Requests allowed over time.        |
      | Request Period  | Limit resets after this time (ms). |
      | Request Timeout | Time before exception thrown (ms). |

5. Click Connect.

6. Verify the information in the Details tab.

## Configure provisioning and reconciliation resources

Use the object type list to select a provisioning and reconciliation resource, such as `Account`. The selected object type determines the side tabs that display, as each resource has different provisioning and reconciliation requirements.

![Sub-tabs under the Provisioning tab](../_images/ui-workforce-provisioning.png)

| Provisioning side tab | Description                                                                                                                                                                                                                                                                                                | Related sections                                                                                                                                      |
| --------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| Details               | View and manage an application, including name, ID, and native type.                                                                                                                                                                                                                                       | Select the specific application from [Provision settings for an application](../provision-an-application.html#provision_settings_for_an_application). |
| Properties            | View and manage properties for the selected object type.                                                                                                                                                                                                                                                   | [Manage application attributes](../provision-an-application.html#manage_application_attributes)                                                       |
| Data                  | View data about the selected object type.                                                                                                                                                                                                                                                                  | [View user access data](../provision-an-application.html#view_user_access_data)                                                                       |
| Mapping               | View and manage mappings from the Advanced Identity Cloud admin console properties to external system properties and from external system properties to the Advanced Identity Cloud admin console properties.                                                                                              | [Manage mappings](../provision-an-application.html#manage_mappings)                                                                                   |
| Reconciliation        | Preview mappings on target applications between external systems and the Advanced Identity Cloud admin console, and reconcile the data between the two systems.View and manage rules for the users and groups that use your application.View and manage schedules for Full and Incremental reconciliation. | [Reconcile and synchronize end-user accounts](../provision-an-application.html#recon-sync-end-users)                                                  |
| Privacy & Consent     | Manage end-user data sharing and synchronization.                                                                                                                                                                                                                                                          | [Configure end-user data sharing](../provision-an-application.html#config-end-user-data-sharing)                                                      |
| Rules                 | View and manage provisioning rules for mappings between Advanced Identity Cloud and a target application.                                                                                                                                                                                                  | [Manage provisioning rules](../provision-an-application.html#manage-provisioning-rules)                                                               |
| Advanced Sync         | Create and manage mappings between a managed object type and an application or between applications.                                                                                                                                                                                                       | [Manage advanced sync](../provision-an-application.html#manage-advanced-sync)                                                                         |

---

---
title: Application management
description: Learn how Advanced Identity Cloud applications work, including provisioning, SSO with OIDC and SAML, and best practices for registration
component: pingoneaic
page_id: pingoneaic:app-management:applications
canonical_url: https://docs.pingidentity.com/pingoneaic/app-management/applications.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Application Management"]
page_aliases: ["release-notes:rapid-channel/app-management.adoc"]
---

# Application management

|   |                                                                                                                                                                                                                                       |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The topics in this section are for tenants created on or after January 12, 2023. Learn more in [Application management migration FAQ](../product-information/migration-dependent-features/application-management-migration-faq.html). |

In Advanced Identity Cloud, an *application* is an object that represents an external service you want to connect to. This service might be a popular cloud-based application (such as Salesforce or Workday), a directory service (such as LDAP or Active Directory), or your own custom-built application.

You can configure an application for two main functions:

* **Provisioning**: Automates the creation and management of user accounts in external applications.

* **Single sign-on (SSO)**: Lets end users access external applications using their Advanced Identity Cloud credentials. Through standard protocols such as OpenID Connect (OIDC), SAML, or WS-Federation, users authenticate once with Advanced Identity Cloud and can access applications without reentering credentials. Sometimes, these protocols also let users consent to delegated access, enabling applications to act on their behalf within approved scopes.

Applications are therefore comprehensive objects. They can also include authorization, authentication, and identity management policies.