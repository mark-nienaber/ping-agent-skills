---
title: Active Directory
description: Configure the Advanced Identity Cloud Active Directory application to provision users and groups to an Active Directory instance
component: pingoneaic
page_id: pingoneaic:app-management:applications/active-directory
canonical_url: https://docs.pingidentity.com/pingoneaic/app-management/applications/active-directory.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  register-the-application: Register the application
  configure-the-provisioner: Configure the provisioner
  configure-provisioning-and-reconciliation-resources: Configure provisioning and reconciliation resources
---

# Active Directory

The Active Directory application template allows you to provision users and groups to an Active Directory instance.

## Register the application

1. In the Advanced Identity Cloud admin console, go to Applications, and click [icon: grid_view, set=material, size=inline] Browse App Catalog.

2. In the Browse App Catalog modal, select an application, and click Next.

3. Review the Application Integration information, and click Next.

4. In the Application Details window, specify the name, description, application owners, and logo for the application.

5. To make the application an [Authoritative](../applications.html#target_and_authoritative_applications) source of identity data, select the Authoritative check box. This option is not available for every application.

6. Click Create Application.

## Configure the provisioner

After you register the application, you can configure provisioning.

1. In the Advanced Identity Cloud admin console, on the Provisioning tab, click Set up Provisioning:

   * If setting up provisioning for the first time:

     1. If you haven't configured a remote server, click New Connector Server and follow the steps to create a server.

     2. If you configured one remote server, it's automatically selected.

     3. If you configured multiple remote servers, choose a server.

   * When editing existing settings in the Connection area, click Settings.

2. Configure the following fields:

   | Field                              | Description                                                                                                                                                                                                                                         |
   | ---------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | Host Name or IP                    | The hostname or IP address for the Active Directory domain controller.                                                                                                                                                                              |
   | Port                               | The port for connecting to the Active Directory domain controller.                                                                                                                                                                                  |
   | Use SSL                            | Enable to use SSL to connect to the Active Directory domain controller. The default value is `true`.                                                                                                                                                |
   | Login Account DN                   | The distinguished name for the login account.                                                                                                                                                                                                       |
   | Password                           | The password for the login account.                                                                                                                                                                                                                 |
   | Base DNs                           | The base context for Active Directory users and groups.                                                                                                                                                                                             |
   | Base DNs to Synchronize (optional) | The base context for Active Directory users and groups to synchronize.&#xA;&#xA;Although this field is optional, an authoritative app requires this context for liveSync to function. You should also verify the bind account can query uSNChanged. |

3. Click Show advanced settings.

4. To filter users and groups:

   * To only connect a subset of users by applying a query filter based on user attributes, enable Filter users.

     * To apply a filter to users manually:

       1. Choose to assign to if All or Any conditions are met.

       2. Set the conditions for assigning filters.

       3. In the User Object Classes field, enter the names of object classes a user must have for inclusion.

          |   |                                                                                                                                                                                                                                           |
          | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
          |   | If you installed Microsoft Exchange, you can add properties to `extensionAttribute1` through `extensionAttribute15` only if you add `msExchCustomAttributes` to the application's User Object Classes list and set Read Schema to `true`. |

     * To use a query to apply a filter to users:

       1. Click Advanced Editor.

       2. Edit the query code.

   * To only connect a subset of groups by applying a query filter based on user attributes, enable Filter groups.

     * To apply a filter to groups manually:

       1. Choose to assign to if All or Any conditions are met.

       2. Set the conditions for assigning filters.

     * To filter users and groups:

       1. Click Advanced Editor.

       2. Edit the query code.

5. To use block-based LDAP controls, enable Use Block-based controls.

6. To use paged results control, enable Use Paged Results control. If Use Block-based controls is enabled, specifies the LDAP Paged Results control is preferred over the VLV control when retrieving entries. The default value is `true`.

7. To set the change log attribute in the change log entry, set the Change Number Attribute field. The default value is `changeNumber`.

8. To set the object classes that Advanced Identity Cloud uses as filters when synchronizing, add classes to the Object Classes to synchronize field. The default value is `user`.

9. To set the sort attribute to use VLV indexes on the resource, set the Virtual List View (VLV) Sort Attribute field. The default value is `sAMAccountName`.

10. To set the name of the attribute that holds the password, set the Password Attribute field. The default value is `unicodePwd`.

11. To have the LDAP provisioner read the schema from the server, enable Read Schema. The default value is `false`.

12. To have Advanced Identity Cloud modify group membership when entries are renamed or deleted, enable Maintain LDAP Group Membership. The default value is `true`.

13. To specify the group attribute to update with the DN of newly added users, set the Group Member Attribute field. The default value is `member`.

14. To specify the name of the attribute that maps to the OpenICF UID attribute, set the UID Attribute field. The default value is `objectGUID`.

15. To specify the password hash algorithm, set the Password Hash Algorithm field.

16. Enter the Account Username Attributes that hold the account's username.

17. To synchronize only the modified properties on a target resource, select Exclude Unmodified.

18. To use timestamps for liveSync operations instead of the changelog, select Timestamp for Sync Token.

19. Set any of the following options:

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

20. Click Connect.

21. Verify the information in the Details tab.

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

1. In the Advanced Identity Cloud admin console, go to Applications, and click [icon: grid_view, set=material, size=inline] Browse App Catalog.

2. In the Browse App Catalog modal, select an application, and click Next.

3. Review the Application Integration information, and click Next.

4. In the Application Details window, specify the name, description, application owners, and logo for the application.

5. To make the application an [Authoritative](../applications.html#target_and_authoritative_applications) source of identity data, select the Authoritative check box. This option is not available for every application.

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
title: App catalog
description: Browse the Advanced Identity Cloud app catalog to find and register provisioning applications including Salesforce, Workday, and Active Directory
component: pingoneaic
page_id: pingoneaic:app-management:app-catalog
canonical_url: https://docs.pingidentity.com/pingoneaic/app-management/app-catalog.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Application Management"]
section_ids:
  templated_applications: Templated applications
  ai_services: AI services
  collaboration: Collaboration
  customer_relationship_management_crm: Customer Relationship Management (CRM)
  enterprise_resource_planning_erp: Enterprise Resource Planning (ERP)
  healthcare: Healthcare
  human_resources: Human resources
  it_infrastructure: IT infrastructure
  mainframes: Mainframes
  privileged_access_management_pam: Privileged Access Management (PAM)
  single_sign_on: Single sign-on
  uncategorized: Uncategorized
  custom_applications: Custom applications
  next_step: Next step
---

# App catalog

|   |                                                                                                                                                                                                                                       |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The topics in this section are for tenants created on or after January 12, 2023. Learn more in [Application management migration FAQ](../product-information/migration-dependent-features/application-management-migration-faq.html). |

## Templated applications

These pre-configured integrations can be discovered and registered directly on the [icon: apps, set=material, size=inline] Applications page by clicking [icon: grid_view, set=material, size=inline] Browse App Catalog.

### AI services

![](_images/app-logos/aws.svg)

#### [AWS Bedrock](applications-agent-governance/aws-bedrock.html)

![](_images/app-logos/aws.svg)

#### [AWS Bedrock AgentCore](applications-agent-governance/aws-bedrock-agentcore.html)

![](_images/app-logos/microsoft.svg)

#### [Azure AI Foundry](applications-agent-governance/azure-ai-foundry.html)

![](_images/app-logos/google.svg)

#### [Google Vertex AI](applications-agent-governance/google-vertex-ai.html)

![](_images/app-logos/copilot.svg)

#### [Microsoft Copilot Studio](applications-agent-governance/microsoft-copilot-studio.html)

### Collaboration

![](_images/app-logos/adobe.svg)

#### [Adobe Admin Console](applications/adobe-admin-console.html)

![](_images/app-logos/docusign.svg)

#### [DocuSign](applications/docusign.html)

![](_images/app-logos/google.svg)

#### [Google Workspace](applications/google-workspace.html)

![](_images/app-logos/snowflake.svg)

#### [Snowflake](applications/snowflake.html)

![](_images/app-logos/webex.svg)

#### [Webex](applications/webex.html)

### Customer Relationship Management (CRM)

![](_images/app-logos/salesforce.svg)

#### [Salesforce](applications/salesforce.html)

![](_images/app-logos/salesforce.svg)

#### [Salesforce Community](applications/salesforce.html)

### Enterprise Resource Planning (ERP)

![](_images/app-logos/oracle.svg)

#### [Oracle E-Business Suite](applications/oracle-ebs.html)

![](_images/app-logos/microsoft-365.svg)

#### [Microsoft 365](register-a-custom-application.html#sso-microsoft-365)

![](_images/app-logos/successfactors.svg)

#### [SAP User Management](applications/sap-user-management.html)

### Healthcare

![](_images/app-logos/epic.svg)

#### [Epic EMP](applications/epic.html)

![](_images/app-logos/epic.svg)

#### [Epic SER](applications/epic.html)

### Human resources

![](_images/app-logos/successfactors.svg)

#### [SAP SuccessFactors HR](applications/sap-successfactors.html)

![](_images/app-logos/servicenow.svg)

#### [ServiceNow](applications/servicenow.html)

![](_images/app-logos/workday.svg)

#### [Workday](applications/workday.html)

### IT infrastructure

![](_images/app-logos/active-directory.svg)

#### [Active Directory](applications/active-directory.html)

![](_images/app-logos/atlassian.svg)

#### [Atlassian Jira](applications/atlassian-jira.html)

![](_images/app-logos/aws.svg)

#### [AWS IAM](applications/aws-iam.html)

![](_images/app-logos/fr-ds.svg)

#### [Directory Services (DS)](applications/directory-services.html)

![](_images/app-logos/ldap.svg)

#### [LDAP](applications/ldap.html)

![](_images/app-logos/powershell.svg)

#### [Powershell](applications/powershell.html)

![](_images/app-logos/saas-rest.svg)

#### [SaaS REST](applications/saas-rest.html)

![](_images/app-logos/saas-rest.svg)

#### [SaaS REST (Connector Server)](applications/saas-rest-rcs.html)

### Mainframes

![](_images/app-logos/ibm.svg)

#### [AS400](applications/as400.html)

### Privileged Access Management (PAM)

![](_images/app-logos/beyondtrust.svg)

#### [BeyondTrust](applications/beyondtrust.html)

### Single sign-on

![](_images/app-logos/ping.svg)

#### [PingOne](applications/pingone.html)

### Uncategorized

![](_images/app-logos/csv.svg)

#### [CSV File](applications/csv-file.html)

![](_images/app-logos/database.svg)

#### [Database Table](applications/database-table.html)

![](_images/app-logos/microsoft.svg)

#### [Microsoft Entra](applications/microsoft-entra.html)

![](_images/app-logos/csv.svg)

#### [Multi-file CSV](applications/csv-multifile.html)

![](_images/app-logos/successfactors.svg)

#### [SAP SuccessFactors Account](applications/sap-successfactors.html)

![](_images/app-logos/scim.svg)

#### [SCIM](applications/scim.html)

![](_images/app-logos/groovy.svg)

#### [Scripted Groovy](applications/scripted-groovy.html)

![](_images/app-logos/scripted-rest.svg)

#### [Scripted REST](applications/scripted-rest.html)

![](_images/app-logos/scripted-sql.svg)

#### [Scripted Table](applications/scripted-table.html)

## Custom applications

These options do not appear as pre-built templates in the application catalog. Use these options when you need to construct a bespoke integration from scratch using generic web protocols such as OIDC, SAML, or WS-Fed.

![](_images/app-logos/custom-app.svg)

#### [Custom Application](register-a-custom-application.html)

![](_images/app-logos/custom-wsfed-app.svg)

#### [Custom WS-Fed](register-a-custom-application.html#sso-custom-wsfed)

## Next step

* [icon: check-square-o, set=fa][Application management](applications.html)

* [icon: check-square-o, set=fa][App catalog](app-catalog.html)

* [icon: square-o, set=fa]*[Register an application](register-an-application.html)* or *[Register a custom or SSO application](register-a-custom-application.html)*

* [icon: square-o, set=fa][Configure an application authorization policy](configure-app-authorization-policy.html)

* [icon: square-o, set=fa][Provision an application](provision-an-application.html)

* [icon: square-o, set=fa][Manage end users and roles](manage-users-and-roles.html)

* [icon: square-o, set=fa][Manage application registrations](manage-app-status.html)

---

---
title: Application journeys
description: Configure OIDC and SAML applications to use a specific journey so authentication always runs with app-specific requirements
component: pingoneaic
page_id: pingoneaic:app-management:application-journeys
canonical_url: https://docs.pingidentity.com/pingoneaic/app-management/application-journeys.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Application Management", "Setup &amp; Configuration"]
section_ids:
  oidc-application-journeys: OIDC application journeys
  saml-application-journeys: SAML 2.0 application journeys
  configure-application-journey: Configure an application journey
---

# Application journeys

You can configure OpenID Connect (OIDC) and SAML 2.0 applications to redirect authentication requests to a specified journey. This lets you customize the authentication experience for users accessing the application, for example, by requiring multi-factor authentication (MFA) or organizational checks.

The redirect contains a transaction condition advice to make sure the journey is always run, regardless of existing sessions and configured authentication context class reference (`acr`) values.

Find an example of a journey that enforces application-specific authorization rules in the [Authorize application access in journeys](../use-cases/use-case-app-authz-journeys.html) use case.

## OIDC application journeys

To associate a journey with an OAuth 2.0 / OIDC application, the application must be configured for the `Authorization Code`, `Implicit`, or `Device Code` grant types.

Journeys that are associated with an application override other authentication settings, including `acr` claims. If a relying party (RP) requests an `acr` claim (voluntary or essential) or if default `acr` values are set in the OIDC client profile, the claim is returned in the ID token regardless of the provider configuration.

To verify that Advanced Identity Cloud uses the associated journey for authentication, check the log messages written to the [am-access and am-authentication log files](../tenants/audit-debug-log-sources.html#log-source-descriptions).

|   |                                                                                                                                                                                                                                                                                                                                        |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | You can use a script to access information about the incoming OAuth 2.0 request. Configure your journey to include a [Scripted Decision node](https://docs.pingidentity.com/auth-node-ref/latest/scripted-decision.html) that queries the [oauthApplication](../am-scripting/scripting-api-node.html#oauthapp-binding) script binding. |

## SAML 2.0 application journeys

Configure your SAML 2.0 application so that a specific authentication journey is always run for users authenticating with your application. The federation flow invokes the associated journey ignoring any existing sessions or authentication context requirements.

|   |                                                                                                                                                                                                                                                                                                                        |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | You can use a script to access information about the SAML request. Configure your journey to include a [Scripted Decision node](https://docs.pingidentity.com/auth-node-ref/latest/scripted-decision.html) that queries the [samlApplication](../am-scripting/scripting-api-node.html#samlapp-binding) script binding. |

## Configure an application journey

To trigger a specific journey every time a user authenticates to your OIDC or SAML 2.0 application, follow these steps:

1. In the Advanced Identity Cloud admin console, go to Applications and select your custom OIDC or SAML 2.0 application.

2. Click the Sign On tab.

3. Find the journey configuration section:

   * For SAML 2.0 applications, after you have [set up SSO](register-a-custom-application.html#custom-saml-app-setup-sso), go to Settings.

   * For OIDC applications, go to General Settings > Show advanced settings > Authentication.

4. Enable the option to `Use a journey to authenticate users to this application`.

5. Select a journey from the list and save your changes.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                              |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | * To prevent users from authenticating directly through this journey, either for security reasons or because the journey is insufficient as a complete authentication service, configure it as a [transactional authentication journey](../am-authentication/configure-authentication-trees.html#configure-transactional-auth-journey).

* You can't delete a journey if it's referenced by an OIDC or SAML 2.0 application. |

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
section_ids:
  provisioning-applications: Provisioning applications
  sso-applications: SSO applications
  oidc_openid_connect_applications: OpenID Connect (OIDC)
  samlv2_applications: SAML 2.0 applications
  bookmark_applications: Bookmark applications
  wsfed-applications: WS-Fed applications
  best_practices_for_registering_applications: Best practices for registering applications
  next_step: Next step
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

You register and manage applications in the Advanced Identity Cloud admin console from the Applications page. For simpler API access use cases, you can register a [Standalone OAuth 2.0 client](standalone-oauth2-clients.html).

|   |                                                                                                                                                                                            |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | Don't use the admin console under Native Consoles > Identity Management for application management, as it doesn't support the functionality needed to fully configure application objects. |

## Provisioning applications

To simplify provisioning, Advanced Identity Cloud provides an extensive [app catalog](app-catalog.html). The catalog includes predefined templates for many popular cloud-based applications (such as HR and CRM solutions) and frameworks for scripted connectors (such as Scripted REST and Scripted Groovy).

Based on your configuration, Advanced Identity Cloud can automatically create, update, or delete user accounts in a connected application.

Each provisioning application relies on a connector to connect to the external resources such as LDAP and flat files.

All provisioning applications are either *authoritative* or *target* applications.

* Authoritative applications

  Authoritative applications act as a source of identities. Running reconciliation on an authoritative application synchronizes user account changes (new accounts, updated accounts, deleted accounts) **from** the authoritative application (for example, Workday) **into** Advanced Identity Cloud. You don't assign users to an authoritative application within Advanced Identity Cloud. You manage them in the source application.

  You specify an application as authoritative when you register the application.

* Target applications

  Running reconciliation on a target application identifies accounts and detects changes in the target application (for example, ServiceNow) and synchronizes that information into Advanced Identity Cloud. This process is used for account discovery and to reconcile changes made directly in the target application. You can assign users and roles to the application directly within Advanced Identity Cloud to trigger outbound provisioning.

  |   |                                                                                                                                                               |
  | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | Reconciliation does not automatically remove applications from users in Advanced Identity Cloud when accounts are deleted directly in the target application. |

You must [register the application](register-an-application.html) before you can [provision the application](provision-an-application.html).

|   |                                                                                                                               |
| - | ----------------------------------------------------------------------------------------------------------------------------- |
|   | Currently, most of the application templates in the app catalog are for provisioning with external applications, not for SSO. |

## SSO applications

You typically configure SSO applications by creating a custom application based on a standard protocol. Advanced Identity Cloud supports several protocols, allowing you to integrate with a wide range of external services. While most are configured manually from scratch, some integrations such as Microsoft 365 have dedicated templates.

Learn more in [Register a custom or SSO application](register-a-custom-application.html)

|   |                                                                                                                                                                                                                                                                                                                                                                     |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The applications you configure in the Applications page trust Advanced Identity Cloud as their IdP. You can also configure Advanced Identity Cloud to trust external IdPs (such as Google or Facebook) for user authentication. This is commonly known as *social authentication*. Learn more in [Social authentication](../self-service/social-registration.html). |

### OpenID Connect (OIDC)

OIDC is a modern, token-based identity protocol built on top of the OAuth 2.0 authorization framework. It's ideal for verifying the end-user's identity and obtaining basic profile information, while enabling third-party applications (such as web, mobile, and SPAs) to securely access data or act on the user's behalf.

When you register a custom OIDC application, you can choose from several types:

| Type                                      | Description                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| ----------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Native / SPA applications with PKCE       | Native applications are built for specific platforms, such as mobile phones or desktops. Single-page applications (SPAs) run entirely in a user's web browser. Both types are considered public clients because they can't securely store a secret. They use the Proof Key for Code Exchange (PKCE) standard to secure the authentication flow\.Learn more in [Authorization code grant with PKCE](../am-oauth2/oauth2-authz-grant-pkce.html). |
| Web applications                          | Traditional web applications run on a server. Because the back-end code isn't exposed to the public, they're considered confidential clients and can securely use a client secret to communicate with Advanced Identity Cloud.                                                                                                                                                                                                                 |
| Service / Machine-to-machine applications | Machine-to-machine (M2M) applications, such as daemons or CLIs, act on behalf of themselves rather than an end user. They authenticate directly without user interaction.                                                                                                                                                                                                                                                                      |

### SAML 2.0 applications

SAML is an XML-based open standard for exchanging authentication and authorization data. It's widely used in enterprise federation scenarios. Register a SAML application if the application you're connecting to requires it.

Learn more in [SAML 2.0 introduction](../am-saml2/saml2-introduction.html).

### Bookmark applications

A Bookmark application is a simple, non-federated entry in an IdP's application catalog or user portal.

Its purpose isn't to perform authentication itself, but to provide a centralized and managed link to an external application, especially those that don't support modern SSO protocols like SAML or OIDC.

### WS-Fed applications

WS-Federation is an identity protocol that is part of the larger Web Services Security (WS-Security) framework.

|   |                                                                                                                                                                                                                                                                                     |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Using this protocol to integrate with applications like Microsoft 365 requires the WS-Federation [add-on capability](../product-information/add-on-capabilities.html). Contact your Ping Identity representative to add WS-Federation to your Advanced Identity Cloud subscription. |

## Best practices for registering applications

Before you register an application with Advanced Identity Cloud, consider the following:

* To set up SSO with SAML, make sure you have the application's metadata and entity ID.

* Know the settings required for configuring provisioning. Learn more in [Provision an application](provision-an-application.html).

* Know which users and groups should have access to your application.

## Next step

* [icon: check-square-o, set=fa][Application management](applications.html)

* [icon: square-o, set=fa][App catalog](app-catalog.html)

* [icon: square-o, set=fa][Register an application](register-an-application.html) or [Register a custom or SSO application](register-a-custom-application.html)

* [icon: square-o, set=fa][Configure an application authorization policy](configure-app-authorization-policy.html)

* [icon: square-o, set=fa][Provision an application](provision-an-application.html)

* [icon: square-o, set=fa][Manage end users and roles](manage-users-and-roles.html)

* [icon: square-o, set=fa][Manage application registrations](manage-app-status.html)

---

---
title: AS400
description: Configure the Advanced Identity Cloud AS400 application to manage and synchronize users between an IBM AS400 mainframe and Advanced Identity Cloud
component: pingoneaic
page_id: pingoneaic:app-management:applications/as400
canonical_url: https://docs.pingidentity.com/pingoneaic/app-management/applications/as400.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
page_aliases: ["release-notes:rapid-channel/as400-connector.adoc"]
section_ids:
  register-the-application: Register the application
  configure-the-provisioner: Configure the provisioner
  configure-provisioning-and-reconciliation-resources: Configure provisioning and reconciliation resources
---

# AS400

AS400 is a mainframe on-premises computer and database that can store identity data. The AS400 application enables you to manage and synchronize users between AS400 and Advanced Identity Cloud. The application can only be a [target application](../applications.html#target_and_authoritative_applications).

The following instructions assume you have access to an AS400 instance as an administrator.

## Register the application

1. In the Advanced Identity Cloud admin console, go to Applications, and click [icon: grid_view, set=material, size=inline] Browse App Catalog.

2. In the Browse App Catalog modal, select an application, and click Next.

3. Review the Application Integration information, and click Next.

4. In the Application Details window, specify the name, description, application owners, and logo for the application.

5. To make the application an [Authoritative](../applications.html#target_and_authoritative_applications) source of identity data, select the Authoritative check box. This option is not available for every application.

6. Click Create Application.

## Configure the provisioner

After you register the application, you can configure provisioning.

1. Set up a [remote connector server (RCS)](../../identities/sync-identities.html).

2. Set up the [AS400 connector](https://docs.pingidentity.com/openicf/connector-reference/as400.html#install_the_as400_connector) with your RCS.

3. In the Advanced Identity Cloud admin console, on the Provisioning tab:

   * If setting up provisioning for the first time, click Set up Provisioning.

   * When editing existing settings in the Connection area, click Settings.

4. Configure the following fields:

   | Field     | Description                                                                          |
   | --------- | ------------------------------------------------------------------------------------ |
   | Host Name | Host name or IP address of AS400.                                                    |
   | User Name | The username to log in to AS400.                                                     |
   | Password  | The password to log in to AS400.                                                     |
   | Use SSL?  | Enable to use SSL to connect to the AS400 application. The default value is `false`. |

5. Optionally, click Show advanced settings to set any of the following options:

   **Application specific settings**

   | Option                         | Description                                                                                                                                               |
   | ------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | Maximum Connections (optional) | The maximum number of connections.                                                                                                                        |
   | Maximum Lifetime (optional)    | The maximum time for an available connection to exist. The default value is 86400000 milliseconds.                                                        |
   | Maximum Inactivity (optional)  | The the maximum amount of inactive time before an available connection closes. The default value is 3600000 milliseconds.                                 |
   | Maximum Use Time (optional)    | The maximum time a connection can be in use before it closes. The default value is `-1` which indicates that there is no time limit.                      |
   | Maximum Use Count (optional)   | The maximum number of times a connection can be used before it is replaced in the pool. The default value is `-1` which indicates that there is no limit. |
   | Is run Maintenance             | Indicates whether the maintenance thread is used to cleanup expired connections. The default is `true`.                                                   |
   | Is thread used                 | Indicates whether threads are used in communication with the host servers and for running maintenance. The default is `true`.                             |
   | Cleanup Interval (optional)    | Specifies how often the maintenance daemon runs. The default value is 300000 milliseconds.                                                                |
   | Exclude Unmodified             | Select this option to synchronize only the modified properties on a target resource.                                                                      |

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

6. Click Connect.

7. Verify the information in the Details tab.

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
title: Atlassian Jira
description: Configure the Advanced Identity Cloud Atlassian Jira application to manage and synchronize data between Advanced Identity Cloud and Jira
component: pingoneaic
page_id: pingoneaic:app-management:applications/atlassian-jira
canonical_url: https://docs.pingidentity.com/pingoneaic/app-management/applications/atlassian-jira.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  register-the-application: Register the application
  configure-the-provisioner: Configure the provisioner
  configure-provisioning-and-reconciliation-resources: Configure provisioning and reconciliation resources
---

# Atlassian Jira

The Advanced Identity Cloud Atlassian Jira application lets you manage and synchronize data between Advanced Identity Cloud and Atlassian Jira.

## Register the application

1. In the Advanced Identity Cloud admin console, go to Applications, and click [icon: grid_view, set=material, size=inline] Browse App Catalog.

2. In the Browse App Catalog modal, select an application, and click Next.

3. Review the Application Integration information, and click Next.

4. In the Application Details window, specify the name, description, application owners, and logo for the application.

5. To make the application an [Authoritative](../applications.html#target_and_authoritative_applications) source of identity data, select the Authoritative check box. This option is not available for every application.

6. Click Create Application.

## Configure the provisioner

After you register the application, you can configure provisioning.

1. In the Advanced Identity Cloud admin console, on the Provisioning tab:

   * If setting up provisioning for the first time, click Set up Provisioning.

   * When editing existing settings in the Connection area, click Settings.

2. Configure the following fields:

   | Field                 | Description                                                                                               |
   | --------------------- | --------------------------------------------------------------------------------------------------------- |
   | SCIM Endpoint         | The URL defining the root for the SCIM endpoint. For example, `https://myserver.com/service/scim`.        |
   | SCIM Protocol Version | Choose version 1 or version 2. The default is 1.                                                          |
   | Authentication Method | The method for authenticating on the remote server: `BASIC`, `OAUTH`, or `TOKEN`. The default is `TOKEN`. |

3. Depending on the Authentication Method, configure the applicable fields:

   * BASIC

   * OAUTH

   * TOKEN

   | Field    | Description                                             |
   | -------- | ------------------------------------------------------- |
   | User     | The basic authentication username for the SCIM service. |
   | Password | The basic authentication password for the SCIM service. |

   | Field          | Description                                                                        |
   | -------------- | ---------------------------------------------------------------------------------- |
   | Token Endpoint | The OAuth 2.0 endpoint where a new access token is requested for the SCIM service. |
   | Client Id      | The OAuth 2.0 client identifier for the SCIM service.                              |
   | Client Secret  | The OAuth 2.0 client secret for the SCIM service.                                  |
   | Scope          | The OAuth 2.0 scope to use.                                                        |
   | Grant Type     | The OAuth 2.0 grant type to use (`client_credentials` or `refresh_token`).         |
   | Refresh Token  | Used by the `refresh_token` Grant Type.                                            |

   | Field      | Description                          |
   | ---------- | ------------------------------------ |
   | Auth Token | The auth token for the SCIM service. |

4. Configure the HTTP connection pool:

   | Field               | Description                                                                  |
   | ------------------- | ---------------------------------------------------------------------------- |
   | Maximum Connections | The maximum size of the http connection pool. The default is 10 connections. |

5. Optionally, click Show advanced settings to set any of the following options:

   **Application specific settings**

   | Field                    | Description                                                                                                                                                                                                                                                                                      |
   | ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
   | Disable Http Compression | Content compression is enabled by default. Select this property to true to disable it.                                                                                                                                                                                                           |
   | Connection Timeout       | Define a timeout (in seconds) for the underlying http connection. The default is 30 seconds.                                                                                                                                                                                                     |
   | Debug/Test settings      | 	Only use these settings for test environments. Don't enable for production environments.Selecting this option displays the following options:- Accept Self Signed Certificates: Enable to accept self-signed certificates.

   - Disable Host Name Verifier: Enable to disable hostname verifiers. |
   | Read Schema              | Read/discover the schema from the Atlassian SCIM endpoint. If `true` (enabled), the application reads the schema from the server. If `false` (disabled), the application provides a default schema based on the object classes in the configuration. The default value is `true` (enabled).      |
   | Exclude Unmodified       | Select this option to synchronize only the modified properties on a target resource.                                                                                                                                                                                                             |

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

6. Click Connect.

7. Verify the information in the Details tab.

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
title: AWS Bedrock
description: Configure the Advanced Identity Cloud AWS Bedrock application template to discover and govern AI agents hosted in AWS Bedrock
component: pingoneaic
page_id: pingoneaic:app-management:applications-agent-governance/aws-bedrock
canonical_url: https://docs.pingidentity.com/pingoneaic/app-management/applications-agent-governance/aws-bedrock.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  prerequisites-aic: Prerequisites in Advanced Identity Cloud
  prerequisites-aws-bedrock: Prerequisites in AWS Bedrock
  create-an-iam-access-policy: Create an IAM access policy
  create-an-iam-user-for-explicit-credentials: Create an IAM user for explicit credentials
  register-the-application: Register the application
  configure-the-provisioner: Configure the provisioner
  configure-provisioning-and-reconciliation-resources: Configure provisioning and reconciliation resources
---

# AWS Bedrock

The AWS Bedrock application automatically discovers the AI agents you have hosted in AWS Bedrock. Once discovered, the platform gives you complete visibility into their core components:

* **Capabilities:** Associated tools, knowledge bases, and guardrails.

* **Security and access:** Execution credentials and IAM-based identity bindings.

The application combines identity creation and governance using separate reconciliation processes. A reconciliation on the Account provisioner object type creates and updates agent identities, and a reconciliation on the Agent Tool provisioner object type updates agent tools and entitlements.

## Prerequisites in Advanced Identity Cloud

Before using the AWS Bedrock application, ensure you've taken these actions:

* Purchased the Agent Governance add-on capability for Advanced Identity Cloud.

* Modified the user managed object with a `custom_iga_identity_type` property in the Alpha realm. Learn more in [Create the identity type](../../identity-governance/administration/iga-agent-governance.html#create-the-identity-type).

* Obtained the AWS Bedrock connector JAR file. This isn't available to download from Backstage yet, but is available from your Ping Identity representative.

## Prerequisites in AWS Bedrock

### Create an IAM access policy

The AWS Bedrock application needs read permissions for Bedrock and an S3 inventory bucket.

1. In the AWS console, go to IAM > Policies > Create policy.

2. On the JSON tab, paste a policy similar to the following:

   ```json
   {
     "Version": "2012-10-17",
     "Statement": [
       {
         "Sid": "ReadBedrockAgents",
         "Effect": "Allow",
         "Action": [ (1)
           "bedrock:ListAgents",
           "bedrock:GetAgent",
           "bedrock:ListAgentAliases",
           "bedrock:GetAgentAlias",
           "bedrock:ListAgentActionGroups",
           "bedrock:GetAgentActionGroup",
           "bedrock:ListAgentKnowledgeBases",
           "bedrock:ListAgentCollaborators",
           "bedrock:GetGuardrail"
         ],
         "Resource": "*"
       },
       {
         "Sid": "ReadBedrockInventoryArtifacts",
         "Effect": "Allow",
         "Action": [ (1)
           "s3:GetObject"
         ],
         "Resource": "arn:aws:s3:::<inventory-bucket>/latest/*" (2)
       }
     ]
   }
   ```

   |       |                                                                                                                                                  |
   | ----- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
   | **1** | Note that the policy is read-only and doesn't allow any modifications to Bedrock agents or S3 inventory artifacts.                               |
   | **2** | Replace `<inventory-bucket>` with the name of your S3 inventory bucket. You can configure this name in the application's Inventory Bucket field. |

3. Select Next.

4. Name the policy `iga-bedrock-application-policy`, then select Create policy.

### Create an IAM user for explicit credentials

Choose one of the following options:

* If you intend to use the default credentials provider to access AWS Bedrock, you don't need to create an IAM user and can skip to the next section.

* If you intend to use explicit credentials to access AWS Bedrock, create an IAM user using these steps:

  1. In the AWS console, go to IAM > Users > Create user.

  2. Enter a username, for example `iga-bedrock-application`.

  3. Select Next.

  4. Under Set permissions, choose Attach policies directly.

  5. Search for `iga-bedrock-application-policy`, select it, then select Next > Create user.

  6. Open the user, then select the Security credentials tab.

  7. Select Create access key.

  8. For Use case, select Application running outside AWS, then select Next.

  9. Copy the access key ID and secret access key. You'll need these for the `Access Key ID` and `Secret Access Key` application properties.

## Register the application

1. In the Advanced Identity Cloud admin console, go to [icon: apps, set=material, size=inline] Applications, and click [icon: grid_view, set=material, size=inline] Browse App Catalog.

2. In the Browse App Catalog modal, select an application, and click Next.

3. Review the Application Integration information, and click Next.

4. In the Application Details window, specify the name, description, application owners, and logo for the application.

5. Leave the Authoritative checkbox unselected.

6. Click Create Application.

## Configure the provisioner

1. In the Advanced Identity Cloud admin console, go to [icon: apps, set=material, size=inline] Applications.

2. Click the application you just registered to open the application details page.

3. Click the Provisioning tab, then compare the message displayed with these options:

   * You haven't set up provisioning yet\
     This message indicates that Advanced Identity Cloud has found a connector server with a compatible connector installed, but you haven't set up provisioning yet. In this case, click Set up Provisioning to set up provisioning for the application.

   * No Connector Servers available\
     This message indicates that Advanced Identity Cloud either can't find a connector server to use for provisioning or that it can find a connector server but it doesn't have a compatible connector installed for this application.

     > **Collapse: Show guidance**
     >
     > * If you haven't set up a connector server:
     >
     >   1. [Register a remote server](../../identities/sync-identities.html#task-1-register-a-remote-server)
     >
     >   2. (Optional) [Reset the client secret](../../identities/sync-identities.html#task-2-reset-the-client-secret)
     >
     >   3. [Download a remote server](../../identities/sync-identities.html#task-3-download-a-remote-server)
     >
     >   4. Add the AWS Bedrock connector JAR file to the remote server's connectors folder.
     >
     >   5. [Configure the remote server](../../identities/sync-identities.html#task-5-configure-a-remote-server)
     >
     >   6. Refresh the AWS Bedrock application page in your browser, then begin step 3 again.
     >
     > * If you've already set up a connector server:
     >
     >   1. Add the AWS Bedrock connector JAR file to the remote server's connectors folder, then restart the connector server.
     >
     >   2. Refresh the AWS Bedrock application page in your browser, then begin step 3 again.

4. In the Connect to AWS Bedrock modal, enter the following information:

   * Region: Enter your AWS region. For example, enter `us-east-1`.

   * Account ID: Enter your AWS account ID from the AWS Management Console. For example, `423456789000`.

   * Inventory Bucket: Enter the S3 bucket name for agent inventory. You must create this bucket in AWS first. Learn more in [AWS Bedrock documentation](https://docs.aws.amazon.com/bedrock/).

   * Use Default Credentials Provider: Enable to use the default AWS credentials chain, or disable to enter an access key ID and secret access key.

   * Access Key ID (optional): If you disabled the default credentials provider, enter your AWS access key ID. For example, `AMZ4XF91LDHBOGFEQYKW`.

   * Secret Access Key (optional): If you disabled the default credentials provider, enter your AWS secret access key.

5. (Optional) Click Show advanced settings to set any of the following options:

   > **Collapse: Show advanced settings options**
   >
   > **Application specific settings**
   >
   > | Option             | Description                                                                          |
   > | ------------------ | ------------------------------------------------------------------------------------ |
   > | Exclude Unmodified | Select this option to synchronize only the modified properties on a target resource. |
   >
   > **Pool configuration**
   >
   > | Field                                   | Description                                                                                                                                                                           |
   > | --------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   > | Max idle and active container instances | The maximum number of idle and active container instances. The default value is `10`.                                                                                                 |
   > | Max Idle Connector Instances            | The maximum number of idle connector instances. The default value is `10`.                                                                                                            |
   > | Set Timeout Period                      | Select to enable a timeout period for the connection. After enabling, configure the following:- Timeout period (ms): The timeout period in milliseconds.                              |
   > | Set Minimum Idle Time                   | Select to set a minimum time (in milliseconds) before an idle object is removed. After enabling, configure the following:- Min idle time (ms): The minimum idle time in milliseconds. |
   > | Min Idle Instances                      | The minimum number of idle connector instances.                                                                                                                                       |
   >
   > **Result Handler configuration**
   >
   > | Field                                                                   | Description                                                                       |
   > | ----------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
   > | Enable for connectors with the attribute normalizer interface           | Enables the attribute normalizer interface for supported connectors.              |
   > | Enable local filtering/search features                                  | Enables local filtering and search capabilities.                                  |
   > | Enable case insensitive filter                                          | Configures filters to ignore case sensitivity.                                    |
   > | Enable configuration of search attributes; disable for local connectors | Enables search attribute configuration. Disable this option for local connectors. |
   >
   > 1. In the Operation Timeouts (ms) area, select the operations to enforce timeouts on and enter the duration in milliseconds.
   >
   >    Available operations include Create, Validate, Test, Enable a Script on the Connector, Schema, Delete, Update, Sync, Authenticate, Get, Enable a Script on the Target, and Search.
   >
   > 2. In the Operation Rate Limits area, select the operations to enforce rate limits on.
   >
   >    You can enforce limits on specific operations, including Create, Validate, Test, Script on Connector, Schema, Delete, Update, Sync, Authenticate, Get, Script on Target, and Search.
   >
   >    For each selected operation, configure the following fields:
   >
   >    | Field           | Description                        |
   >    | --------------- | ---------------------------------- |
   >    | Request Limit   | Requests allowed over time.        |
   >    | Request Period  | Limit resets after this time (ms). |
   >    | Request Timeout | Time before exception thrown (ms). |

6. Click Connect.

7. Verify that the status shows Connected.

## Configure provisioning and reconciliation resources

To configure provisioning and reconciliation resources, follow the instructions in [Onboard AI agents](../../identity-governance/administration/iga-agent-governance.html#onboard-ai-agents) in the Agent Governance documentation.

---

---
title: AWS Bedrock AgentCore
description: Configure the Advanced Identity Cloud AWS Bedrock AgentCore application template to discover and govern AI agents hosted in AWS Bedrock AgentCore
component: pingoneaic
page_id: pingoneaic:app-management:applications-agent-governance/aws-bedrock-agentcore
canonical_url: https://docs.pingidentity.com/pingoneaic/app-management/applications-agent-governance/aws-bedrock-agentcore.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  prerequisites-aic: Prerequisites in Advanced Identity Cloud
  prerequisites-aws-bedrock-agentcore: Prerequisites in AWS Bedrock AgentCore
  create-an-iam-access-policy: Create an IAM access policy
  create-an-iam-user-for-explicit-credentials: Create an IAM user for explicit credentials
  register-the-application: Register the application
  configure-the-provisioner: Configure the provisioner
  configure-provisioning-and-reconciliation-resources: Configure provisioning and reconciliation resources
---

# AWS Bedrock AgentCore

The Amazon Bedrock AgentCore application discovers and governs AI agents created in Amazon Bedrock AgentCore.

## Prerequisites in Advanced Identity Cloud

Before using the AWS Bedrock AgentCore application, ensure you've taken these actions:

* Purchased the Agent Governance add-on capability for Advanced Identity Cloud.

* Modified the user managed object with a `custom_iga_identity_type` property in the Alpha realm. Learn more in [Create the identity type](../../identity-governance/administration/iga-agent-governance.html#create-the-identity-type).

* Obtained the AWS Bedrock AgentCore connector JAR file. This isn't available to download from Backstage yet, but is available from your Ping Identity representative.

## Prerequisites in AWS Bedrock AgentCore

### Create an IAM access policy

The AWS Bedrock AgentCore application needs read permissions for Bedrock AgentCore.

1. In the AWS console, go to IAM > Policies > Create policy.

2. On the JSON tab, paste a policy similar to the following:

   ```json
   {
     "Version": "2012-10-17",
     "Statement": [
       {
         "Sid": "BedrockAgentCoreConnectorReadOnly",
         "Effect": "Allow",
         "Action": [ (1)
           "bedrock-agentcore:ListAgentRuntimes",
           "bedrock-agentcore:GetAgentRuntime",
           "bedrock-agentcore:GetAgentRuntimeEndpoint",
           "bedrock-agentcore:GetResourcePolicy"
         ],
         "Resource": "*" (2)
       }
     ]
   }
   ```

   |       |                                                                                                                                                                             |
   | ----- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | **1** | Note that the policy is read-only and doesn't allow any modifications to Bedrock AgentCore agents.                                                                          |
   | **2** | `ListAgentRuntimes` requires `Resource: "*"`. The other read actions can be scoped to AgentCore runtime ARNs if your AWS environment supports the narrower resource policy. |

3. Select Next.

4. Name the policy `iga-bedrock-agentcore-application-policy`, then select Create policy.

### Create an IAM user for explicit credentials

Choose one of the following options:

* If you intend to use the default credentials provider to access AWS Bedrock AgentCore, you don't need to create an IAM user and can skip to the next section.

* If you intend to use explicit credentials to access AWS Bedrock AgentCore, create an IAM user using these steps:

  1. In the AWS console, go to IAM > Users > Create user.

  2. Enter a username, for example `iga-bedrock-agentcore-application`.

  3. Select Next.

  4. Under Set permissions, choose Attach policies directly.

  5. Search for `iga-bedrock-agentcore-application-policy`, select it, then select Next > Create user.

  6. Open the user, then select the Security credentials tab.

  7. Select Create access key.

  8. For Use case, select Application running outside AWS, then select Next.

  9. Copy the access key ID and secret access key. You'll need these for the `Access Key ID` and `Secret Access Key` application properties.

## Register the application

1. In the Advanced Identity Cloud admin console, go to [icon: apps, set=material, size=inline] Applications, and click [icon: grid_view, set=material, size=inline] Browse App Catalog.

2. In the Browse App Catalog modal, select an application, and click Next.

3. Review the Application Integration information, and click Next.

4. In the Application Details window, specify the name, description, application owners, and logo for the application.

5. Leave the Authoritative checkbox unselected.

6. Click Create Application.

## Configure the provisioner

1. In the Advanced Identity Cloud admin console, go to [icon: apps, set=material, size=inline] Applications.

2. Click the application you just registered to open the application details page.

3. Click the Provisioning tab, then compare the message displayed with these options:

   * You haven't set up provisioning yet\
     This message indicates that Advanced Identity Cloud has found a connector server with a compatible connector installed, but you haven't set up provisioning yet. In this case, click Set up Provisioning to set up provisioning for the application.

   * No Connector Servers available\
     This message indicates that Advanced Identity Cloud either can't find a connector server to use for provisioning or that it can find a connector server but it doesn't have a compatible connector installed for this application.

     > **Collapse: Show guidance**
     >
     > * If you haven't set up a connector server:
     >
     >   1. [Register a remote server](../../identities/sync-identities.html#task-1-register-a-remote-server)
     >
     >   2. (Optional) [Reset the client secret](../../identities/sync-identities.html#task-2-reset-the-client-secret)
     >
     >   3. [Download a remote server](../../identities/sync-identities.html#task-3-download-a-remote-server)
     >
     >   4. Add the AWS Bedrock AgentCore connector JAR file to the remote server's connectors folder.
     >
     >   5. [Configure the remote server](../../identities/sync-identities.html#task-5-configure-a-remote-server)
     >
     >   6. Refresh the AWS Bedrock AgentCore application page in your browser, then begin step 3 again.
     >
     > * If you've already set up a connector server:
     >
     >   1. Add the AWS Bedrock AgentCore connector JAR file to the remote server's connectors folder, then restart the connector server.
     >
     >   2. Refresh the AWS Bedrock AgentCore application page in your browser, then begin step 3 again.

4. In the Connect to AWS Bedrock AgentCore modal, enter the following information:

   * Region: Enter your AWS region. For example, enter `us-east-1`.

   * Use Default Credentials Provider: Enable to use the default AWS credentials chain, or disable to enter an access key ID and secret access key.

   * Access Key ID (optional): If you disabled the default credentials provider, enter your AWS access key ID. For example, `AMZ4XF91LDHBOGFEQYKW`.

   * Secret Access Key (optional): If you disabled the default credentials provider, enter your AWS secret access key.

5. (Optional) Click Show advanced settings to set any of the following options:

   > **Collapse: Show advanced settings options**
   >
   > **Application specific settings**
   >
   > | Option             | Description                                                                          |
   > | ------------------ | ------------------------------------------------------------------------------------ |
   > | Exclude Unmodified | Select this option to synchronize only the modified properties on a target resource. |
   >
   > **Pool configuration**
   >
   > | Field                                   | Description                                                                                                                                                                           |
   > | --------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   > | Max idle and active container instances | The maximum number of idle and active container instances. The default value is `10`.                                                                                                 |
   > | Max Idle Connector Instances            | The maximum number of idle connector instances. The default value is `10`.                                                                                                            |
   > | Set Timeout Period                      | Select to enable a timeout period for the connection. After enabling, configure the following:- Timeout period (ms): The timeout period in milliseconds.                              |
   > | Set Minimum Idle Time                   | Select to set a minimum time (in milliseconds) before an idle object is removed. After enabling, configure the following:- Min idle time (ms): The minimum idle time in milliseconds. |
   > | Min Idle Instances                      | The minimum number of idle connector instances.                                                                                                                                       |
   >
   > **Result Handler configuration**
   >
   > | Field                                                                   | Description                                                                       |
   > | ----------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
   > | Enable for connectors with the attribute normalizer interface           | Enables the attribute normalizer interface for supported connectors.              |
   > | Enable local filtering/search features                                  | Enables local filtering and search capabilities.                                  |
   > | Enable case insensitive filter                                          | Configures filters to ignore case sensitivity.                                    |
   > | Enable configuration of search attributes; disable for local connectors | Enables search attribute configuration. Disable this option for local connectors. |
   >
   > 1. In the Operation Timeouts (ms) area, select the operations to enforce timeouts on and enter the duration in milliseconds.
   >
   >    Available operations include Create, Validate, Test, Enable a Script on the Connector, Schema, Delete, Update, Sync, Authenticate, Get, Enable a Script on the Target, and Search.
   >
   > 2. In the Operation Rate Limits area, select the operations to enforce rate limits on.
   >
   >    You can enforce limits on specific operations, including Create, Validate, Test, Script on Connector, Schema, Delete, Update, Sync, Authenticate, Get, Script on Target, and Search.
   >
   >    For each selected operation, configure the following fields:
   >
   >    | Field           | Description                        |
   >    | --------------- | ---------------------------------- |
   >    | Request Limit   | Requests allowed over time.        |
   >    | Request Period  | Limit resets after this time (ms). |
   >    | Request Timeout | Time before exception thrown (ms). |

6. Click Connect.

7. Verify that the status shows Connected.

## Configure provisioning and reconciliation resources

To configure provisioning and reconciliation resources, follow the instructions in [Onboard AI agents](../../identity-governance/administration/iga-agent-governance.html#onboard-ai-agents) in the Agent Governance documentation.

---

---
title: AWS IAM
description: Configure the Advanced Identity Cloud AWS IAM application to provision users and manage AWS resource access permissions
component: pingoneaic
page_id: pingoneaic:app-management:applications/aws-iam
canonical_url: https://docs.pingidentity.com/pingoneaic/app-management/applications/aws-iam.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  register-the-application: Register the application
  configure-the-provisioner: Configure the provisioner
  configure-provisioning-and-reconciliation-resources: Configure provisioning and reconciliation resources
---

# AWS IAM

AWS Identity and Access Management (IAM) is a web service that helps you securely control access to AWS resources. You can use the Advanced Identity Cloud AWS IAM application to manage permissions that control which AWS resources users can access.

|   |                                                                                                                                                                                                          |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | To use this application, you must have an AWS administrator account with proper access to AWS as described in the [AWS documentation](https://docs.aws.amazon.com/IAM/latest/APIReference/welcome.html). |

## Register the application

1. In the Advanced Identity Cloud admin console, go to Applications, and click [icon: grid_view, set=material, size=inline] Browse App Catalog.

2. In the Browse App Catalog modal, select an application, and click Next.

3. Review the Application Integration information, and click Next.

4. In the Application Details window, specify the name, description, application owners, and logo for the application.

5. To make the application an [Authoritative](../applications.html#target_and_authoritative_applications) source of identity data, select the Authoritative check box. This option is not available for every application.

6. Click Create Application.

## Configure the provisioner

1. In the Advanced Identity Cloud admin console, on the Provisioning tab:

   * If setting up provisioning for the first time, click Set up Provisioning.

   * When editing existing settings in the Connection area, click Settings.

2. Configure the following fields:

   | Field               | Description                                                                                                                         |
   | ------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
   | Access Key          | The AWS access key ID for the IAM user whose credentials are used to call AWS APIs.                                                 |
   | Secret Key          | The AWS secret access key associated with the access key ID.                                                                        |
   | Role ARN            | The Amazon Resource Name (ARN) for the role.                                                                                        |
   | Region              | The host region of the AWS instance.                                                                                                |
   | Parent Organization | The unique identifier assigned to the parent entity in the AWS Organization hierarchy. Required for Organizational Unit operations. |

3. Optionally, click Show advanced settings to set any of the following options:

   **Application specific settings**

   | Field                          | Description                                                                                            |
   | ------------------------------ | ------------------------------------------------------------------------------------------------------ |
   | Page Size                      | The page size for search operations. The default is `100`.                                             |
   | Credential Expiration Duration | The temporary credentials expiration time in seconds. The default is `3600` seconds.                   |
   | Connection Timeout             | Define a timeout (in milliseconds) for the underlying connection. The default is `10000` milliseconds. |
   | Maximum Connections            | The maximum number of connections. The default is `10` connections.                                    |
   | Exclude Unmodified             | Select this option to synchronize only the modified properties on a target resource.                   |

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

4. Click Connect.

5. Verify the information in the Details tab.

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
title: Azure AI Foundry
description: Configure the Advanced Identity Cloud Azure AI Foundry application template to discover and govern AI agents hosted in Azure AI Foundry
component: pingoneaic
page_id: pingoneaic:app-management:applications-agent-governance/azure-ai-foundry
canonical_url: https://docs.pingidentity.com/pingoneaic/app-management/applications-agent-governance/azure-ai-foundry.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  prerequisites-aic: Prerequisites in Advanced Identity Cloud
  prerequisites-azure-ai-foundry: Prerequisites in Azure AI Foundry
  register-the-application: Register the application
  configure-the-provisioner: Configure the provisioner
  configure-provisioning-and-reconciliation-resources: Configure provisioning and reconciliation resources
---

# Azure AI Foundry

The Azure AI Foundry application automatically discovers the AI agents you have hosted in Azure AI Foundry. Once discovered, the platform gives you complete visibility into their core components:

* **Capabilities:** Associated tools, knowledge bases, and guardrails.

* **Security and access:** Execution credentials and IAM-based identity bindings.

The application combines identity creation and governance using separate reconciliation processes. A reconciliation on the Account provisioner object type creates and updates agent identities, and a reconciliation on the Agent Tool provisioner object type updates agent tools and entitlements.

## Prerequisites in Advanced Identity Cloud

Before using the Azure AI Foundry application, ensure you've taken these actions:

* Purchased the Agent Governance add-on capability for Advanced Identity Cloud.

* Modified the user managed object with a `custom_iga_identity_type` property in the Alpha realm. Learn more in [Create the identity type](../../identity-governance/administration/iga-agent-governance.html#create-the-identity-type).

* Obtained the Azure AI Foundry connector JAR file. This isn't available to download from Backstage yet, but is available from your Ping Identity representative.

## Prerequisites in Azure AI Foundry

Before you configure the connector, you must register an application with Microsoft Entra and configure the Azure AI Foundry project. You need a Microsoft Azure subscription to complete this procedure.

1. Sign on to the [Azure portal](https://portal.azure.com/) as an administrative user.

2. Select App registrations under Azure services.

3. On the Register an application page, enter a name for the application and select the supported account types.

4. On the new registration page, make a note of the Application (client) ID and the Directory (tenant) ID.

5. Generate a client secret. Select Certificates & secrets > New client secret, enter a description, and click Add. Copy the client secret value.

6. Note the Azure subscription ID and the resource group where your Azure AI Foundry project resides.

## Register the application

1. In the Advanced Identity Cloud admin console, go to [icon: apps, set=material, size=inline] Applications, and click [icon: grid_view, set=material, size=inline] Browse App Catalog.

2. In the Browse App Catalog modal, select an application, and click Next.

3. Review the Application Integration information, and click Next.

4. In the Application Details window, specify the name, description, application owners, and logo for the application.

5. Leave the Authoritative checkbox unselected.

6. Click Create Application.

## Configure the provisioner

1. In the Advanced Identity Cloud admin console, go to [icon: apps, set=material, size=inline] Applications.

2. Click the application you just registered to open the application details page.

3. Click the Provisioning tab, then compare the message displayed with these options:

   * You haven't set up provisioning yet\
     This message indicates that Advanced Identity Cloud has found a connector server with a compatible connector installed, but you haven't set up provisioning yet. In this case, click Set up Provisioning to set up provisioning for the application.

   * No Connector Servers available\
     This message indicates that Advanced Identity Cloud either can't find a connector server to use for provisioning or that it can find a connector server but it doesn't have a compatible connector installed for this application.

     > **Collapse: Show guidance**
     >
     > * If you haven't set up a connector server:
     >
     >   1. [Register a remote server](../../identities/sync-identities.html#task-1-register-a-remote-server)
     >
     >   2. (Optional) [Reset the client secret](../../identities/sync-identities.html#task-2-reset-the-client-secret)
     >
     >   3. [Download a remote server](../../identities/sync-identities.html#task-3-download-a-remote-server)
     >
     >   4. Add the Azure AI Foundry connector JAR file to the remote server's connectors folder.
     >
     >   5. [Configure the remote server](../../identities/sync-identities.html#task-5-configure-a-remote-server)
     >
     >   6. Refresh the Azure AI Foundry application page in your browser, then begin step 3 again.
     >
     > * If you've already set up a connector server:
     >
     >   1. Add the Azure AI Foundry connector JAR file to the remote server's connectors folder, then restart the connector server.
     >
     >   2. Refresh the Azure AI Foundry application page in your browser, then begin step 3 again.

4. In the Connect to Azure AI Foundry modal, enter the following information:

   * Tenant ID: Enter your Entra ID tenant GUID. For example, enter `c9fe364e-8947-4045-8d4d-e281f1edd60e`.

   * Subscription ID: Enter your Azure AI Foundry subscription GUID. For example, `94f2e268-3f99-4b86-b2da-d031500cdf1f`.

   * Resource Group: Enter your Azure AI Foundry resource group. The expected format is `/subscriptions/<subscription-id>/resourceGroups/<resource-group-name>/providers/Microsoft.CognitiveServices/accounts/<foundry-resource-name>`.

   * Project Location: Enter your Azure AI Foundry project location. For example, `eastus`, `westeurope`, or `australiacentral`.

   * Client ID: Enter the client ID of the Azure App Registration used to authenticate with Azure AI Foundry. For example, `2d7b3e1c-4f8a-41a9-bc2e-0e9f57a34d12`.

   * Client Secret: Enter the client secret of the Azure App Registration used to authenticate with Azure AI Foundry.

   * Use Managed Identity: Select this checkbox to authenticate securely using Azure's keyless infrastructure tokens. This leverages Microsoft Entra ID to grant access based on the application host's environment permissions, eliminating the security risks and administrative overhead of storing and rotating a static client ID and client secret.

   * Agent Service Endpoint: Enter the base URL for the Azure AI Foundry project you want to connect to. The expected format is `https://<resource>.services.ai.azure.com/api/projects/<project>`.

   * Agent API Flavor: Choose one of the following options to specify which API endpoint to use for agent discovery:

     * Enter `classic` to scan for native, security-governed agents (`/agents`).

     * Enter `new` to scan for stateful models relying on the Azure OpenAI Assistants architecture (`/assistants`).

     * Enter `both` to ingest your entire AI footprint across both endpoint versions.

   * Scan Offline Inventory: Select this checkbox to perform a deep metadata scan of your workspace asset registry and deployment blueprints. This allows the application to extract and catalog underlying identity bindings, service accounts, data connections, and tool credentials. This ensures full security governance even over inactive or pre-production assets.

   * Tools Inventory URL: Specify the secure HTTPS endpoint used to retrieve the JSON catalog of your agents' custom tools and API connectors. This must be an Azure Blob Storage Shared Access Signature (SAS) URL or an Azure Function HTTP trigger URL that provides authorized read-access to your tools manifest.

   * Agent API Version: Specify the data plane API version used to interact with your agents' inference and execution routes. This field defaults to `v1` to match the native Azure AI Foundry Assistants and thread management endpoint specifications.

5. (Optional) Click Show advanced settings to set any of the following options:

   > **Collapse: Show advanced settings options**
   >
   > **Application specific settings**
   >
   > | Option             | Description                                                                          |
   > | ------------------ | ------------------------------------------------------------------------------------ |
   > | Exclude Unmodified | Select this option to synchronize only the modified properties on a target resource. |
   >
   > **Pool configuration**
   >
   > | Field                                   | Description                                                                                                                                                                           |
   > | --------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   > | Max idle and active container instances | The maximum number of idle and active container instances. The default value is `10`.                                                                                                 |
   > | Max Idle Connector Instances            | The maximum number of idle connector instances. The default value is `10`.                                                                                                            |
   > | Set Timeout Period                      | Select to enable a timeout period for the connection. After enabling, configure the following:- Timeout period (ms): The timeout period in milliseconds.                              |
   > | Set Minimum Idle Time                   | Select to set a minimum time (in milliseconds) before an idle object is removed. After enabling, configure the following:- Min idle time (ms): The minimum idle time in milliseconds. |
   > | Min Idle Instances                      | The minimum number of idle connector instances.                                                                                                                                       |
   >
   > **Result Handler configuration**
   >
   > | Field                                                                   | Description                                                                       |
   > | ----------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
   > | Enable for connectors with the attribute normalizer interface           | Enables the attribute normalizer interface for supported connectors.              |
   > | Enable local filtering/search features                                  | Enables local filtering and search capabilities.                                  |
   > | Enable case insensitive filter                                          | Configures filters to ignore case sensitivity.                                    |
   > | Enable configuration of search attributes; disable for local connectors | Enables search attribute configuration. Disable this option for local connectors. |
   >
   > 1. In the Operation Timeouts (ms) area, select the operations to enforce timeouts on and enter the duration in milliseconds.
   >
   >    Available operations include Create, Validate, Test, Enable a Script on the Connector, Schema, Delete, Update, Sync, Authenticate, Get, Enable a Script on the Target, and Search.
   >
   > 2. In the Operation Rate Limits area, select the operations to enforce rate limits on.
   >
   >    You can enforce limits on specific operations, including Create, Validate, Test, Script on Connector, Schema, Delete, Update, Sync, Authenticate, Get, Script on Target, and Search.
   >
   >    For each selected operation, configure the following fields:
   >
   >    | Field           | Description                        |
   >    | --------------- | ---------------------------------- |
   >    | Request Limit   | Requests allowed over time.        |
   >    | Request Period  | Limit resets after this time (ms). |
   >    | Request Timeout | Time before exception thrown (ms). |

6. Click Connect.

7. Verify that the status shows Connected.

## Configure provisioning and reconciliation resources

To configure provisioning and reconciliation resources, follow the instructions in [Onboard AI agents](../../identity-governance/administration/iga-agent-governance.html#onboard-ai-agents) in the Agent Governance documentation.

---

---
title: BeyondTrust
description: Configure the Advanced Identity Cloud BeyondTrust application to manage and synchronize data from Advanced Identity Cloud to BeyondTrust
component: pingoneaic
page_id: pingoneaic:app-management:applications/beyondtrust
canonical_url: https://docs.pingidentity.com/pingoneaic/app-management/applications/beyondtrust.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
page_aliases: ["release-notes:rapid-channel/beyondtrust-app.adoc"]
section_ids:
  register-the-application: Register the application
  configure-the-provisioner: Configure the provisioner
  configure-provisioning-and-reconciliation-resources: Configure provisioning and reconciliation resources
---

# BeyondTrust

The Advanced Identity Cloud BeyondTrust application lets you manage and synchronize data from Advanced Identity Cloud to BeyondTrust.

## Register the application

1. In the Advanced Identity Cloud admin console, go to Applications, and click [icon: grid_view, set=material, size=inline] Browse App Catalog.

2. In the Browse App Catalog modal, select an application, and click Next.

3. Review the Application Integration information, and click Next.

4. In the Application Details window, specify the name, description, application owners, and logo for the application.

5. To make the application an [Authoritative](../applications.html#target_and_authoritative_applications) source of identity data, select the Authoritative check box. This option is not available for every application.

6. Click Create Application.

## Configure the provisioner

1. In the Advanced Identity Cloud admin console, on the Provisioning tab:

   * If setting up provisioning for the first time, click Set up Provisioning.

   * When editing existing settings in the Connection area, click Settings.

2. Configure the following fields:

   | Field               | Description                                                                                   |
   | ------------------- | --------------------------------------------------------------------------------------------- |
   | SCIM Endpoint       | The HTTP URL defining the root for the SCIM endpoint (https\://myserver.com/service/scim/v2). |
   | Token Endpoint      | The OAuth 2.0 endpoint where a new access token is requested for the SCIM service.            |
   | Client Id           | The OAuth 2.0 client identifier for the SCIM service.                                         |
   | Client Secret       | The OAuth 2.0 client secret for the SCIM service.                                             |
   | Maximum Connections | The maximum size of the http connection pool. The default is 10 connections.                  |

3. Optionally, click Show advanced settings to set any of the following options:

   **Application specific settings**

   | Field                    | Description                                                                                                                                                                                                                                                                                      |
   | ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
   | Disable Http Compression | Content compression is enabled by default. Select this property to true to disable it.                                                                                                                                                                                                           |
   | Connection Timeout       | Define a timeout (in seconds) for the underlying http connection. The default is 30 seconds.                                                                                                                                                                                                     |
   | Debug/Test settings      | 	Only use these settings for test environments. Don't enable for production environments.Selecting this option displays the following options:- Accept Self Signed Certificates: Enable to accept self-signed certificates.

   - Disable Host Name Verifier: Enable to disable hostname verifiers. |
   | Read Schema              | Read/discover the schema from the BeyondTrust SCIM endpoint. If `true` (enabled), the application reads the schema from the server. If `false` (disabled), the application provides a default schema based on the object classes in the configuration. The default value is `true` (enabled).    |
   | Exclude Unmodified       | Select this option to synchronize only the modified properties on a target resource.                                                                                                                                                                                                             |

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

4. Click Connect.

5. Verify the information in the Details tab.

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
title: Configure an application authorization policy
description: Configure Advanced Identity Cloud authorization policies for custom or SSO applications to control who can authenticate to the application
component: pingoneaic
page_id: pingoneaic:app-management:configure-app-authorization-policy
canonical_url: https://docs.pingidentity.com/pingoneaic/app-management/configure-app-authorization-policy.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Application Management", "Setup &amp; Configuration"]
section_ids:
  benefits-authorization-policy: Benefits of application authorization policies
  use-cases-authorization-policy: Example use cases
  add-authorization-policy: Add an authorization policy to an application
  manage-authorization-policy: Manage an authorization policy
  policy-condition-builder: Policy condition builder
  policy_condition_builder_elements: Policy condition builder elements
  example_policy: Example policy
  next_steps: Next steps
---

# Configure an application authorization policy

Use application authorization policies to control who can sign on to OpenID Connect (OIDC) and SAML applications in Advanced Identity Cloud. When you add a policy to an application, only users who meet the policy's conditions can authenticate. During sign-on, the [App Policy Decision node](https://docs.pingidentity.com/auth-node-ref/latest/app-policy-decision.html) in the authentication journey evaluates the policy to determine whether to grant access.

|   |                                                                                                                                                                                                                                                                                                                                                             |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The application policy builder supports a simplified set of policy conditions. If you need conditions or constructs that aren't available in the application UI, use the [AM native admin console](../am-authorization/policy-sets-ui.html). When using the AM native admin console, you must add custom policies to the `Customer Application Policy Set`. |

## Benefits of application authorization policies

Configuring an application authorization policy provides the following benefits:

* **Stronger security**: Enforce granular access control by restricting access based on user, group, application, and environmental conditions.

* **Simplified maintenance**: Add, edit, activate, and deactivate policies directly from the application UI without modifying the authentication journey for routine policy changes.

* **Reusable journeys**: Use a single authentication journey for multiple applications, where each application has its own distinct authorization policy to control access.

* **Separation of duties**: Allow a tenant administrator to build a reusable authentication journey, while an application owner manages access to their specific application by configuring the application's authorization policy.

### Example use cases

* **Group-scoped HR portal**: An OIDC application for payroll is restricted to members of the `HR-Staff` group. If an employee is removed from the group, they lose access automatically with no need to update the journey or the application's SSO configuration.

* **High-risk app**: An application containing sensitive data is restricted to users who have authenticated with multi-factor authentication (MFA) and are using a trusted device.

* **Contractor access**: Contractors are allowed to authenticate, but only during working hours and only from an approved IP address.

Find an example of a journey that enforces application-specific authorization rules in the [Authorize application access in journeys](../use-cases/use-case-app-authz-journeys.html) use case.

## Add an authorization policy to an application

1. In the Advanced Identity Cloud admin console, go to [icon: apps, set=material, size=inline] Applications and select the application.

2. Click the Sign On tab.

3. In the Access Policy section, click [icon: add, set=material, size=inline] Create a Policy.

4. In the Add Access Policy modal, choose the policy type:

   * User-based Access: Restrict access to the application based on user attributes and application membership.

   * Group-based Access: Restrict access to the application based on group membership.

   * Environmental: Restrict access to the application based on environmental conditions, such as IP address or a date range.

   * Custom: Build a policy using the supported conditions, groups, and comparators to restrict access.

5. Click Next.

6. [Build the policy](#policy-condition-builder) and click Save.

## Manage an authorization policy

After you save a policy, you can manage it from the Access Policy section of the application's Sign On tab. Click the Ellipsis ([icon: more_horiz, set=material, size=inline]) icon to the right of the policy to:

* Edit the policy's conditions.

* Activate or Deactivate the policy. When a policy is deactivated, it isn't evaluated during sign-on.

* Delete the policy.

## Policy condition builder

The policy condition builder lets you construct policies based on user, group, and environmental conditions.

You can use the policy condition builder to:

* Add one or more conditions.

* Group conditions together.

* Choose how values are compared.

* Combine conditions into a policy that is evaluated when the authentication journey runs.

### Policy condition builder elements

| Element    | Purpose                                                                                                                                                                            |
| ---------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Condition  | A single rule to evaluate, such as group membership, role value, application assignment, IP range, or another supported user or environment attribute.                             |
| Group      | A logical grouping of conditions that are evaluated together.                                                                                                                      |
| Comparator | Defines how the selected value is checked. For example equals, contains, starts with, or ends with, depending on the condition type.                                               |
| Value      | The user, group, attribute value, IP range, date, or other input that the condition evaluates against. The available value field depends on the selected condition and comparator. |

### Example policy

This example shows how to create a policy that grants access to the application only if the user is in the `Finance` group and has application membership. The example assumes that you have a `Finance` [group set up in Advanced Identity Cloud](../idm-objects/manage-groups.html#create-a-group).

1. In the Advanced Identity Cloud admin console, go to Applications and select the application.

2. Click the Sign On tab.

3. In the Access Policy section, click [icon: add, set=material, size=inline] Create a Policy.

4. In the Add Access Policy modal, select Custom and click Next.

5. Select All to restrict access to users who meet all the criteria.

6. For the first condition, select User Group Membership as the condition type, equals as the comparator, and the finance group (for example, Finance) as the value.

7. Click [icon: add, set=material, size=inline] then Add Condition.

8. For the second condition, select User Application Membership.

   ![Add access policy modal with the first condition added and the user application membership condition being added.](_images/add-access-policy.png)

9. Click Save to save the policy. The policy is automatically activated and added to the application.

Only users who are in the `Finance` group and have access to the application can sign on to the application. Users who don't meet both criteria are denied access.

## Next steps

* [icon: check-square-o, set=fa][Application management](applications.html)

* [icon: check-square-o, set=fa][App catalog](app-catalog.html)

* [icon: check-square-o, set=fa][Register an application](register-an-application.html) or [Register a custom or SSO application](register-a-custom-application.html)

* [icon: check-square-o, set=fa][Configure an application authorization policy](configure-app-authorization-policy.html)

* [icon: square-o, set=fa]*[Manage end users and roles](manage-users-and-roles.html)*

* [icon: square-o, set=fa][Manage application registrations](manage-app-status.html)

---

---
title: CSV File
description: Configure the Advanced Identity Cloud CSV File application to provision users from a single CSV file using a remote connector server
component: pingoneaic
page_id: pingoneaic:app-management:applications/csv-file
canonical_url: https://docs.pingidentity.com/pingoneaic/app-management/applications/csv-file.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  register-the-application: Register the application
  configure-the-provisioner: Configure the provisioner
  configure-provisioning-and-reconciliation-resources: Configure provisioning and reconciliation resources
---

# CSV File

The CSV File application template allows you to provision users from a CSV file.

## Register the application

1. In the Advanced Identity Cloud admin console, go to Applications, and click [icon: grid_view, set=material, size=inline] Browse App Catalog.

2. In the Browse App Catalog modal, select an application, and click Next.

3. Review the Application Integration information, and click Next.

4. In the Application Details window, specify the name, description, application owners, and logo for the application.

5. To make the application an [Authoritative](../applications.html#target_and_authoritative_applications) source of identity data, select the Authoritative check box. This option is not available for every application.

6. Click Create Application.

## Configure the provisioner

1. In the Advanced Identity Cloud admin console, on the Provisioning tab, click Set up Provisioning:

   * If setting up provisioning for the first time:

     1. If you have not configured a remote server, click New Connector Server and follow the steps to create a server.

     2. If you configured one remote server, it is automatically selected.

     3. If you configured multiple remote servers, choose a server.

   * When editing existing settings in the Connection area, click Settings.

2. Follow the steps on the Set up CSV modal.

3. Click Next.

4. Configure the following fields:

   | Field           | Description                                                                                                                        |
   | --------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
   | CSV File        | The full file path to the CSV file that is the application data source. The path uses the file location format /opt/data/file.csv. |
   | UID Column      | The UID column name in the CSV file; the primary search key. The default value is `uid`.                                           |
   | Password Column | The password column name in the CSV file; the primary search key. The default is `password`.                                       |

5. Optionally, click Show advanced settings to set any of the following options:

   **Application specific settings**

   | Field                    | Description                                                                          |
   | ------------------------ | ------------------------------------------------------------------------------------ |
   | Quote Character          | The character used to enclose values. The default value is `"`.                      |
   | Field Delimiter          | The character that delimits each field. The default value is `,`.                    |
   | Newline String           | The character that represents a new line in the CSV file. The default value is `\n`. |
   | Space Replacement String | The character used to replace spaces within column names. The default value is `_`.  |
   | Sync Retention Count     | The default value is `3`.                                                            |
   | Exclude Unmodified       | Select this option to synchronize only the modified properties on a target resource. |

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

6. Click Connect.

7. Verify the information in the Details tab.

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
title: Database Table
description: Configure the Advanced Identity Cloud Database Table application to provision users to a JDBC database table
component: pingoneaic
page_id: pingoneaic:app-management:applications/database-table
canonical_url: https://docs.pingidentity.com/pingoneaic/app-management/applications/database-table.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  register-the-application: Register the application
  configure-the-provisioner: Configure the provisioner
  configure-provisioning-and-reconciliation-resources: Configure provisioning and reconciliation resources
---

# Database Table

The Database Table application template allows you to provision users to a database table.

## Register the application

1. In the Advanced Identity Cloud admin console, go to Applications, and click [icon: grid_view, set=material, size=inline] Browse App Catalog.

2. In the Browse App Catalog modal, select an application, and click Next.

3. Review the Application Integration information, and click Next.

4. In the Application Details window, specify the name, description, application owners, and logo for the application.

5. To make the application an [Authoritative](../applications.html#target_and_authoritative_applications) source of identity data, select the Authoritative check box. This option is not available for every application.

6. Click Create Application.

## Configure the provisioner

1. In the Advanced Identity Cloud admin console, on the Provisioning tab, click Set up Provisioning:

   * If setting up provisioning for the first time:

     1. If you have not configured a remote server, click New Connector Server and follow the steps to create a server.

     2. If you configured one remote server, it is automatically selected.

     3. If you configured multiple remote servers, choose a server.

   * When editing existing settings in the Connection area, click Settings.

2. Configure the following fields:

   | Field               | Description                                                                                                                                                                                                                                                                                                                                           |
   | ------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | JDBC Connection Url | The URl for the JDBC database address that contains the table that you are provisioning. The format of the url depends on the type of database. For example, `jdbc:mysql://localhost:3306/contractordb?serverTimezone=UTC` or `jdbc:oracle:thin:@//localhost:3306/contractordb`. The address includes the name of the database you are connecting to. |
   | JDBC Driver         | The class name of the driver you are using to connect to a database. The name varies depending on the type of database you are using, such as `oracle.jdbc.OracleDriver` or `com.mysql.jdbc.Driver`.                                                                                                                                                  |
   | Username            | The username sent to the JDBC driver to establish a connection.                                                                                                                                                                                                                                                                                       |
   | Password            | The password sent to the JDBC driver to establish a connection.                                                                                                                                                                                                                                                                                       |
   | Table               | The name of the table in the JDBC database that contains the user accounts. The default is `TABLE_NAME`.                                                                                                                                                                                                                                              |
   | Key Column          | The column value that is the unique identifier for rows in the table. The default is `KEY_COLUMN`.                                                                                                                                                                                                                                                    |

3. Optionally, click Show advanced settings to set any of the following options:

   **Application specific settings**

   | Field                                    | Description                                                                                                                                                                                                           |
   | ---------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | Validate resources and passwords         | Enable to validate resources and passwords. After enabling this option, in the Password Column field, enter the name of the column in the table that holds the password values.                                       |
   | Activate Sync ICF Interface              | Enable to poll for synchronization events, which are native changes to target objects. After enabling this option, in the Change Log Column field, enter the change log column that stores the latest change time.    |
   | Allow empty string                       | Enable to allow empty strings instead of null values, except for OracleSQL.                                                                                                                                           |
   | Quote Database Column Names              | Enable to place specific quote characters around column names in the SQL that is generated to access the database. After enabling this option, in the Quote Characters field, enter the characters to use for quotes. |
   | Rethrow All SQL Exceptions               | Enable to show SQL Exceptions with `code = 0`. The default value is `true`.                                                                                                                                           |
   | Native Timestamps                        | Enable to retrieve timestamp data.                                                                                                                                                                                    |
   | All Native                               | Enable to retrieve in a database-native format.                                                                                                                                                                       |
   | Validate Connection                      | Enable to specify a SQL query used to validate connections. After enabling this option, in the Validation SQL Query (optional) field, enter the SQL query for validating connections.                                 |
   | Validation Interval (ms)                 | Enter the validation interval in milliseconds. The default value is `3000`.                                                                                                                                           |
   | Validation Connection Query Timeout (ms) | Enter the validation connection query timeout in milliseconds. The default value is `-1`.                                                                                                                             |
   | Initial Pool size                        | Enter the initial pool size. The default value is `10`.                                                                                                                                                               |
   | Maximum Idle                             | Enter the maximum idle time. The default value is `100`.                                                                                                                                                              |
   | Minimum Idle                             | Enter the minimum idle time. The default value is `10`.                                                                                                                                                               |
   | Maximum Wait (ms)                        | Enter the maximum wait time in milliseconds. The default value is `30000`.                                                                                                                                            |
   | Maximum Active                           | Enter the maximum active time. The default value is `100`.                                                                                                                                                            |
   | Maximum Age (ms)                         | Enter the maximum age in milliseconds. The default value is `0`.                                                                                                                                                      |
   | Minimum Evictable Idle Time (ms)         | Enter the minimum evictable idle time in milliseconds. The default value is `60000`.                                                                                                                                  |
   | Time Between Eviction Runs(ms)           | Enter the time between eviction checks in milliseconds. The default value is `5000`.                                                                                                                                  |
   | Test Connection When Idle                | Enable to test the connection when idle.                                                                                                                                                                              |
   | Test Connection On Borrow                | Enable to test the connection on borrow.                                                                                                                                                                              |
   | Exclude Unmodified                       | Select this option to synchronize only the modified properties on a target resource.                                                                                                                                  |

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

4. Click Connect.

5. Verify the information in the Details tab.

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
title: Directory Services (DS)
description: Configure the Advanced Identity Cloud Directory Services (PingDS) application to provision users and groups to a PingDS instance
component: pingoneaic
page_id: pingoneaic:app-management:applications/directory-services
canonical_url: https://docs.pingidentity.com/pingoneaic/app-management/applications/directory-services.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  register-the-application: Register the application
  configure-the-provisioner: Configure the provisioner
  configure-provisioning-and-reconciliation-resources: Configure provisioning and reconciliation resources
---

# Directory Services (DS)

The Directory Services (DS) (also known as PingDS) application template allows you to provision users and groups to a PingDS instance.

## Register the application

1. In the Advanced Identity Cloud admin console, go to Applications, and click [icon: grid_view, set=material, size=inline] Browse App Catalog.

2. In the Browse App Catalog modal, select an application, and click Next.

3. Review the Application Integration information, and click Next.

4. In the Application Details window, specify the name, description, application owners, and logo for the application.

5. To make the application an [Authoritative](../applications.html#target_and_authoritative_applications) source of identity data, select the Authoritative check box. This option is not available for every application.

6. Click Create Application.

## Configure the provisioner

1. In the Advanced Identity Cloud admin console, on the Provisioning tab, click Set up Provisioning:

   * If setting up provisioning for the first time:

     1. If you have not configured a remote server, click New Connector Server and follow the steps to create a server.

     2. If you configured one remote server, it is automatically selected.

     3. If you configured multiple remote servers, choose a server.

   * When editing existing settings in the Connection area, click Settings.

2. Configure the following fields:

   | Field                                            | Description                                                               |
   | ------------------------------------------------ | ------------------------------------------------------------------------- |
   | Host Name or IP                                  | The hostname or IP address for the Directory Services domain controller.  |
   | Port                                             | The port for connecting to the Directory Services domain controller.      |
   | Use SSL                                          | Enable to use SSL to connect to the Directory Services domain controller. |
   | Login Account DN                                 | The distinguished name for the login account.                             |
   | Password                                         | The password for the login account.                                       |
   | Base DNs for Directory Services users and groups | The base context for Directory Services users and groups.                 |

3. Click Show advanced settings.

4. To filter users and groups:

   * To only connect a subset of users by applying a query filter based on user attributes, enable Filter users.

     * To apply a filter to users manually:

       1. Choose to assign to if All or Any conditions are met.

       2. Set the conditions for assigning filters.

       3. In the User Object Classes field, enter the names of object classes a user must have for inclusion.

     * To use a query to apply a filter to users:

       1. Click Advanced Editor.

       2. Edit the query code.

   * To only connect a subset of groups by applying a query filter based on user attributes, enable Filter groups.

     * To apply a filter to groups manually:

       1. Choose to assign to if All or Any conditions are met.

       2. Set the conditions for assigning filters.

     * To filter users and groups:

       1. Click Advanced Editor.

       2. Edit the query code.

5. To use block-based LDAP controls, enable Use Block-based controls.

6. To use paged results control, enable Use Paged Results control. If Use Block-based controls is enabled, specifies the LDAP Paged Results control is preferred over the VLV control when retrieving entries. The default value is `true`.

7. To set the change log attribute in the change log entry, set the Change Number Attribute field. The default value is `changeNumber`.

8. To set the object classes that Advanced Identity Cloud uses as filters when synchronizing, add classes to the Object Classes to synchronize field. The default value is `inetOrgPerson`.

9. To set the sort attribute to use VLV indexes on the resource, set the Virtual List View (VLV) Sort Attribute field. The default value is `uid`.

10. To set the name of the attribute that holds the password, set the Password Attribute field. The default value is `userPassword`.

11. To have the LDAP provisioner read the schema from the server, enable Read Schema. The default value is `false`.

12. To have Advanced Identity Cloud modify group membership when entries are renamed or deleted, enable Maintain LDAP Group Membership. The default value is `false`.

13. To specify the group attribute to update with the DN of newly added users, set Group Member Attribute field. The default value is `uniqueMember`.

14. To specify the name of the attribute that maps to the OpenICF UID attribute, set UID Attribute field. The default value is `entryUUID`.

15. To use timestamps for liveSync operations instead of the changelog, select Timestamp for Sync Token.

16. To synchronize only the modified properties on a target resource, select Exclude Unmodified.

17. Set any of the following options:

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

18. Click Connect.

19. Verify the information in the Details tab.

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
title: DocuSign
description: Configure the Advanced Identity Cloud DocuSign application to manage DocuSign accounts and synchronize them with Advanced Identity Cloud identities
component: pingoneaic
page_id: pingoneaic:app-management:applications/docusign
canonical_url: https://docs.pingidentity.com/pingoneaic/app-management/applications/docusign.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
page_aliases: ["release-notes:rapid-channel/docusign-app.adoc"]
section_ids:
  register-the-application: Register the application
  configure-the-provisioner: Configure the provisioner
  configure-provisioning-and-reconciliation-resources: Configure provisioning and reconciliation resources
---

# DocuSign

The Advanced Identity Cloud DocuSign application lets you manage DocuSign service accounts and synchronize DocuSign accounts and Advanced Identity Cloud identities.

## Register the application

1. In the Advanced Identity Cloud admin console, go to Applications, and click [icon: grid_view, set=material, size=inline] Browse App Catalog.

2. In the Browse App Catalog modal, select an application, and click Next.

3. Review the Application Integration information, and click Next.

4. In the Application Details window, specify the name, description, application owners, and logo for the application.

5. To make the application an [Authoritative](../applications.html#target_and_authoritative_applications) source of identity data, select the Authoritative check box. This option is not available for every application.

6. Click Create Application.

## Configure the provisioner

You must have a DocuSign administrator account and be able to add an integrator key ([DocuSign Documentation](https://support.docusign.com/guides/ndse-admin-guide-api-and-keys)).

|   |                                                                                                                                                                    |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | To modify the settings for an existing provisioning connection, in the Advanced Identity Cloud admin console, click the Provisioning tab, and then click Settings. |

1. In DocuSign, set up a DocuSign app and integration key:

   1. Log in to DocuSign and go to [Integrations > Apps and Keys](https://apps-d.docusign.com/admin/apps-and-keys).

   2. On the Apps and Keys page, in the My Account Information area, copy and save the following values:

      | DocuSign field   | Advanced Identity Cloud application field |
      | ---------------- | ----------------------------------------- |
      | API Account ID   | Account                                   |
      | Account Base URI | Service Endpoint URI                      |

      > **Collapse: Show Me**
      >
      > ![DocuSign My Account Information](../_images/docusign-my-account-area.png)

   3. Click Add App and Integration Key.

      > **Collapse: Show Me**
      >
      > ![DocuSign Add App and Integration Key button](../_images/docusign-add-app-integration-key-btn.png)

   4. In the Add Integration Key modal, enter an App Name, and click Create App.

      > **Collapse: Show Me**
      >
      > ![DocuSign Add Integration Key modal](../_images/docusign-add-integration-key-modal.png)

   5. On the Apps and Keys > App Name page, copy the Integration Key and save the value. Use this value as the Client Id in Advanced Identity Cloud.

      > **Collapse: Show Me**
      >
      > ![DocuSign Add Integration Key modal](../_images/docusign-copy-integration-key.png)

   6. In the Authentication area, click + Add Secret Key, and copy and save the value. Use this value as the Client Secret in Advanced Identity Cloud.

      > **Collapse: Show Me**
      >
      > ![DocuSign Add Secret Key](../_images/docusign-add-secret-key.png)

   |   |                                                                                          |
   | - | ---------------------------------------------------------------------------------------- |
   |   | Keep DocuSign open, as you'll need to add information during provisioning configuration. |

2. In the Advanced Identity Cloud admin console, click the Provisioning tab, and then click Set up Provisioning.

3. In the Configure DocuSign Connected App modal, copy the Redirect URI, and click Next.

   > **Collapse: Show Me**
   >
   > ![Configure DocuSign modal](../_images/ui-applications-configure-docusign-modal.png)

4. In DocuSign, in the Additional settings area, click Add URI, paste the redirect URI, and click Save.

   > **Collapse: Show Me**
   >
   > ![DocuSign Add URI](../_images/docusign-add-uri.png)

5. Go to Integrations > API Usage Center, and from the API Limit area, make note of the following:

   * Hourly Limit

   * Burst Limit

     > **Collapse: Show Me**
     >
     > ![DocuSign API Limit](../_images/docusign-api-limit.png)

   Use these values in the Advanced Identity Cloud advanced settings.

6. In the Advanced Identity Cloud admin console, configure the following fields:

   | Field                | Description                                                                           |
   | -------------------- | ------------------------------------------------------------------------------------- |
   | Service Endpoint URI | The DocuSign Account Base URI.                                                        |
   | Account              | The DocuSign API Account ID.                                                          |
   | Client ID            | The client ID for OAuth 2.0 flow. The DocuSign Integration Key.                       |
   | Client Secret        | The client secret for OAuth 2.0 flow. The DocuSign Secret Key.                        |
   | Maximum Connections  | The maximum size of the HTTP connection pool. The default is 10 connections.          |
   | Connection Timeout   | The timeout for the underlying HTTP connection in seconds. The default is 30 seconds. |

7. Optionally, click Show advanced settings to set any of the following options:

   **Application specific settings**

   | Field or option                      | Description                                                                                                                                                                                                                                                                                      |
   | ------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
   | Use Basic Auth for Token Negotiation | Select this option to send the client ID and client secret to DocuSign as authorization headers. If the option is not selected, the ID and secret are sent as form data.                                                                                                                         |
   | Hour Rate Limit                      | The hourly rate limit for the DocuSign API. The DocuSign Hourly Limit.                                                                                                                                                                                                                           |
   | Burst Rate Limit                     | The burst rate limit for the DocuSign API. The DocuSign Burst Limit.                                                                                                                                                                                                                             |
   | Disable Http Compression             | Content compression is enabled by default. Select this option to disable it.                                                                                                                                                                                                                     |
   | Debug/Test settings                  | 	Only use these settings for test environments. Don't enable for production environments.Selecting this option displays the following options:- Accept Self Signed Certificates: Enable to accept self-signed certificates.

   - Disable Host Name Verifier: Enable to disable hostname verifiers. |
   | Exclude Unmodified                   | Select this option to synchronize only the modified properties on a target resource.                                                                                                                                                                                                             |

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

8. Click Connect.

9. Verify the information in the Details tab.

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
title: Epic
description: Configure the Advanced Identity Cloud Epic application to provision users to an Epic instance. Contact Ping Identity for setup details
component: pingoneaic
page_id: pingoneaic:app-management:applications/epic
canonical_url: https://docs.pingidentity.com/pingoneaic/app-management/applications/epic.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
page_aliases: ["release-notes:rapid-channel/epic-app-template.adoc"]
section_ids:
  register-the-application: Register the application
  configure-the-provisioner: Configure the provisioner
  configure-provisioning-and-reconciliation-resources: Configure provisioning and reconciliation resources
---

# Epic

The Epic application template allows you to provision users to an Epic instance.

## Register the application

1. In the Advanced Identity Cloud admin console, go to Applications, and click [icon: grid_view, set=material, size=inline] Browse App Catalog.

2. In the Browse App Catalog modal, select an application, and click Next.

3. Review the Application Integration information, and click Next.

4. In the Application Details window, specify the name, description, application owners, and logo for the application.

5. To make the application an [Authoritative](../applications.html#target_and_authoritative_applications) source of identity data, select the Authoritative check box. This option is not available for every application.

6. Click Create Application.

## Configure the provisioner

Contact your Ping Customer Success Outcome Manager (CSOM) or Account Executive to learn about this application.

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
title: Google Vertex AI
description: Configure the Advanced Identity Cloud Google Vertex AI application template to discover and govern AI agents hosted in Google Vertex AI
component: pingoneaic
page_id: pingoneaic:app-management:applications-agent-governance/google-vertex-ai
canonical_url: https://docs.pingidentity.com/pingoneaic/app-management/applications-agent-governance/google-vertex-ai.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  prerequisites-aic: Prerequisites in Advanced Identity Cloud
  prerequisites-google-vertex-ai: Prerequisites in Google Vertex AI
  register-the-application: Register the application
  configure-the-provisioner: Configure the provisioner
  configure-provisioning-and-reconciliation-resources: Configure provisioning and reconciliation resources
---

# Google Vertex AI

The Google Vertex AI application automatically discovers the AI agents you created in Google Dialogflow CX and Vertex AI Agent Engine. Once discovered, the platform gives you complete visibility into their core components:

* **Capabilities:** Associated tools, knowledge bases, and guardrails.

* **Security and access:** Execution credentials and IAM-based identity bindings.

The application combines identity creation and governance using separate reconciliation processes. A reconciliation on the Account provisioner object type creates and updates agent identities, and a reconciliation on the Agent Tool provisioner object type updates agent tools and entitlements.

## Prerequisites in Advanced Identity Cloud

Before using the Google Vertex AI application, ensure you've taken these actions:

* Purchased the Agent Governance add-on capability for Advanced Identity Cloud.

* Modified the user managed object with a `custom_iga_identity_type` property in the Alpha realm. Learn more in [Create the identity type](../../identity-governance/administration/iga-agent-governance.html#create-the-identity-type).

* Obtained the Google Vertex AI connector JAR file. This isn't available to download from Backstage yet, but is available from your Ping Identity representative.

## Prerequisites in Google Vertex AI

Before you can use the application, you must configure a Google Cloud service account with the appropriate IAM roles. You need a Google Cloud subscription to complete this procedure:

1. Sign on to the Google Cloud console as an administrative user.

2. Navigate to IAM & Admin > Service Accounts and create a new service account (or choose an existing principal) to act as the connector identity.

3. Grant the service account the following standard IAM roles at the project level to enable resource discovery:

   * **Dialogflow Reader** (`roles/dialogflow.reader`)

   * **Vertex AI Viewer** (`roles/aiplatform.viewer`)

4. (Optional) If your environment requires organization-wide asset discovery, ensure the service account principal is also granted the following specific permission:

   * `cloudasset.assets.searchAllResources`

5. Configure your chosen authentication method to capture the runtime credentials:

   * **For Workload Identity**: Bind the Google Cloud service account to your local environment infrastructure or Kubernetes service account.

   * **For Explicit Keys**: Select the service account, navigate to the Keys tab, select Add Key > Create new key, and choose JSON format. Download and securely save the key file. You will need this configuration data to set up the provisioner.

## Register the application

1. In the Advanced Identity Cloud admin console, go to [icon: apps, set=material, size=inline] Applications, and click [icon: grid_view, set=material, size=inline] Browse App Catalog.

2. In the Browse App Catalog modal, select an application, and click Next.

3. Review the Application Integration information, and click Next.

4. In the Application Details window, specify the name, description, application owners, and logo for the application.

5. Leave the Authoritative checkbox unselected.

6. Click Create Application.

## Configure the provisioner

1. In the Advanced Identity Cloud admin console, go to [icon: apps, set=material, size=inline] Applications.

2. Click the application you just registered to open the application details page.

3. Click the Provisioning tab, then compare the message displayed with these options:

   * You haven't set up provisioning yet\
     This message indicates that Advanced Identity Cloud has found a connector server with a compatible connector installed, but you haven't set up provisioning yet. In this case, click Set up Provisioning to set up provisioning for the application.

   * No Connector Servers available\
     This message indicates that Advanced Identity Cloud either can't find a connector server to use for provisioning or that it can find a connector server but it doesn't have a compatible connector installed for this application.

     > **Collapse: Show guidance**
     >
     > * If you haven't set up a connector server:
     >
     >   1. [Register a remote server](../../identities/sync-identities.html#task-1-register-a-remote-server)
     >
     >   2. (Optional) [Reset the client secret](../../identities/sync-identities.html#task-2-reset-the-client-secret)
     >
     >   3. [Download a remote server](../../identities/sync-identities.html#task-3-download-a-remote-server)
     >
     >   4. Add the Google Vertex AI connector JAR file to the remote server's connectors folder.
     >
     >   5. [Configure the remote server](../../identities/sync-identities.html#task-5-configure-a-remote-server)
     >
     >   6. Refresh the Google Vertex AI application page in your browser, then begin step 3 again.
     >
     > * If you've already set up a connector server:
     >
     >   1. Add the Google Vertex AI connector JAR file to the remote server's connectors folder, then restart the connector server.
     >
     >   2. Refresh the Google Vertex AI application page in your browser, then begin step 3 again.

4. In the Connect to Google Vertex AI modal, enter the following information:

   * Project ID: Enter your GCP project ID. For example, `finance-ai-agents-prod`.

   * Location: Enter your GCP location. For example, `us-central1`, `europe-west3`, or `australia-southeast1`.

   * Agent API Flavor: Choose one of the following options for agent discovery based on how your assistants are built in Google Cloud:

     * Select `Dialogflow CX` for visual, state-based conversational virtual agents.

     * Select `Vertex AI Agent Engine` for code-first programmatic agent frameworks.

     * Select `Both` to discover a hybrid deployment of both styles.

   * Complete the following fields according to your chosen authentication method:

     * Use Workload Identity: Select this checkbox to allow the application to automatically discover identity tokens from the environment using Application Default Credentials (ADC). To use this option, ensure your runtime environment is properly bound to a Google Cloud service account with the necessary Vertex AI permissions.

     * Service Account Key JSON: Use this field to provide the JSON key for a GCP service account with the necessary permissions to access the Vertex AI API.

   * Scan Offline Inventory: Select to enable scanning of offline inventory for identity bindings, service accounts, connections, and tool credentials.

   * GCS Identity Bindings URL: Specify the storage path to the JSON or CSV file containing IAM role mappings and identity bindings for your agents. The application reads this file during discovery to audit which user identities, groups, or external principals are authorized to invoke each agent. The GCS URL might look like `gs://<your-bucket-name>/agent-identity-bindings.json`.

   * GCS Service Accounts URL: Specify the storage path to the file containing the Google Cloud service accounts associated with your agent fleet. This allows the application to discover and catalog the underlying infrastructure identities that your agents use to interact with downstream GCP services. The GCS URL might look like `gs://<your-bucket-name>/agent-service-accounts.json`.

   * GCS Tool Credentials URL: Specify the storage path to the file or bucket location where third-party API keys and external credentials used by the agents' tools are cataloged. The application reads this data to flag and monitor unsecured secrets or external authentication paths mapped to your agents. The GCS URL might look like `gs://<your-bucket-name>/agent-tool-credentials.json`.

5. (Optional) Click Show advanced settings to set any of the following options:

   > **Collapse: Show advanced settings options**
   >
   > **Application specific settings**
   >
   > | Option             | Description                                                                          |
   > | ------------------ | ------------------------------------------------------------------------------------ |
   > | Exclude Unmodified | Select this option to synchronize only the modified properties on a target resource. |
   >
   > **Pool configuration**
   >
   > | Field                                   | Description                                                                                                                                                                           |
   > | --------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   > | Max idle and active container instances | The maximum number of idle and active container instances. The default value is `10`.                                                                                                 |
   > | Max Idle Connector Instances            | The maximum number of idle connector instances. The default value is `10`.                                                                                                            |
   > | Set Timeout Period                      | Select to enable a timeout period for the connection. After enabling, configure the following:- Timeout period (ms): The timeout period in milliseconds.                              |
   > | Set Minimum Idle Time                   | Select to set a minimum time (in milliseconds) before an idle object is removed. After enabling, configure the following:- Min idle time (ms): The minimum idle time in milliseconds. |
   > | Min Idle Instances                      | The minimum number of idle connector instances.                                                                                                                                       |
   >
   > **Result Handler configuration**
   >
   > | Field                                                                   | Description                                                                       |
   > | ----------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
   > | Enable for connectors with the attribute normalizer interface           | Enables the attribute normalizer interface for supported connectors.              |
   > | Enable local filtering/search features                                  | Enables local filtering and search capabilities.                                  |
   > | Enable case insensitive filter                                          | Configures filters to ignore case sensitivity.                                    |
   > | Enable configuration of search attributes; disable for local connectors | Enables search attribute configuration. Disable this option for local connectors. |
   >
   > 1. In the Operation Timeouts (ms) area, select the operations to enforce timeouts on and enter the duration in milliseconds.
   >
   >    Available operations include Create, Validate, Test, Enable a Script on the Connector, Schema, Delete, Update, Sync, Authenticate, Get, Enable a Script on the Target, and Search.
   >
   > 2. In the Operation Rate Limits area, select the operations to enforce rate limits on.
   >
   >    You can enforce limits on specific operations, including Create, Validate, Test, Script on Connector, Schema, Delete, Update, Sync, Authenticate, Get, Script on Target, and Search.
   >
   >    For each selected operation, configure the following fields:
   >
   >    | Field           | Description                        |
   >    | --------------- | ---------------------------------- |
   >    | Request Limit   | Requests allowed over time.        |
   >    | Request Period  | Limit resets after this time (ms). |
   >    | Request Timeout | Time before exception thrown (ms). |

6. Click Connect.

7. Verify that the status shows Connected.

## Configure provisioning and reconciliation resources

To configure provisioning and reconciliation resources, follow the instructions in [Onboard AI agents](../../identity-governance/administration/iga-agent-governance.html#onboard-ai-agents) in the Agent Governance documentation.

---

---
title: Google Workspace
description: Configure the Advanced Identity Cloud Google Workspace application to provision users and groups to a Google Workspace instance
component: pingoneaic
page_id: pingoneaic:app-management:applications/google-workspace
canonical_url: https://docs.pingidentity.com/pingoneaic/app-management/applications/google-workspace.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  register-the-application: Register the application
  configure-the-provisioner: Configure the provisioner
  configure-provisioning-and-reconciliation-resources: Configure provisioning and reconciliation resources
---

# Google Workspace

The Google Workspace application template allows you to provision users and groups to a Google Workspace instance.

## Register the application

1. In the Advanced Identity Cloud admin console, go to Applications, and click [icon: grid_view, set=material, size=inline] Browse App Catalog.

2. In the Browse App Catalog modal, select an application, and click Next.

3. Review the Application Integration information, and click Next.

4. In the Application Details window, specify the name, description, application owners, and logo for the application.

5. To make the application an [Authoritative](../applications.html#target_and_authoritative_applications) source of identity data, select the Authoritative check box. This option is not available for every application.

6. Click Create Application.

## Configure the provisioner

1. In the Advanced Identity Cloud admin console, on the Provisioning tab:

   * If setting up provisioning for the first time, click Set up Provisioning.

   * When editing existing settings in the Connection area, click Settings.

2. In the Configure Google Workspace App modal, copy the values:

   * Authorized JavaScript Origins

   * Authorized Redirect URI

3. In a new browser tab, sign on to the [Google Apps Developers Console](https://console.developers.google.com/start) and update your existing project or create a new project:

   1. [Enable the following APIs](https://support.google.com/googleapi/answer/6158841) for your project:

      * [Admin SDK API](https://console.cloud.google.com/apis/library/admin.googleapis.com)

      * [Enterprise License Manager API](https://console.cloud.google.com/apis/library/licensing.googleapis.com)

   2. Set up an OAuth 2.0 client:

      The Google Workspace application template uses OAuth 2.0 to authorize the connection to the Google service:

      1. In the Google Apps Developers Console, select Credentials > Create Credentials > OAuth client ID.

      2. Click Configure Consent Screen, select Internal, and click Create.

      3. On the OAuth consent screen, enter an Application name; for example, `Advanced Identity Cloud`, and click Save.

         This name displays for all applications registered in this project.

      4. Select Credentials > Create Credentials > OAuth client ID > Web application, and enter the previously copied information in the following fields:

         * Authorized JavaScript origins

           The URI that clients use to access your application copied from the Configure Google Workspace App modal in Advanced Identity Cloud.

         * Authorized redirect URIs

           The OAuth redirect URI copied from the Configure Google Workspace App modal in Advanced Identity Cloud.

      5. Click Create.

      6. On the OAuth client created modal, copy and save the Client ID and Client Secret.

   3. Add Advanced Identity Cloud to the Trusted Apps list:

      1. Sign on to the [Google Admin Console](https://admin.google.com/).

      2. From the upper-left menu, select Security > API Controls.

      3. Select Manage Third-Party App Access, click Change Access, and change the Advanced Identity Cloud app settings to Trusted.

4. Return to the Advanced Identity Cloud admin console browser tab, and in the Configure Google Workspace App modal, click Next.

5. In the Connect to Google Workspace modal, enter the Client ID, Client Secret, and Domain.

6. Optionally, click Show advanced settings to set any of the following options:

   **Application specific settings**

   | Option             | Description                                                                          |
   | ------------------ | ------------------------------------------------------------------------------------ |
   | Exclude Unmodified | Select this option to synchronize only the modified properties on a target resource. |

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

7. Click Connect.

8. When you are redirected to Google, log in using your admin credentials.

9. On the next screen, click Allow. You are then redirected back to the Advanced Identity Cloud admin console.

10. Verify the information in the Details tab.

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