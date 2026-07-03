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
