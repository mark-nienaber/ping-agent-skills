---
title: About groups and populations
description: Groups and populations are both used to organize users in PingOne, but they differ in several ways.
component: pingone
page_id: pingone:directory:p1_groups_vs_populations
canonical_url: https://docs.pingidentity.com/pingone/directory/p1_groups_vs_populations.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 3, 2024
section_ids:
  related-links: Related links
  p1-internal-external-groups: Internal and external groups
  p1-static-dynamic-groups: Static and dynamic groups
  p1-dynamic-group-ex: Dynamic group examples
  example-1: Example 1
  example-2: Example 2
  example-3: Example 3
  example-4: Example 4
  example-5: Example 5
  p1-nested-groups: Nested groups
  circular-references: Circular references
  p1-group-roles: Group roles
---

# About groups and populations

Groups and populations are both used to organize users in PingOne, but they differ in several ways.

A user can belong to multiple groups, but only one population. A population is a fundamental organizational unit, while groups offer more fine-grained control. For example, you could use a population to contain all your employees and use a group to define subsets, such as Marketing, HR, Contractors, or US Employees.

A population-level group can contain users from that population only, but an environment-level group can contain users from different populations in the same environment.

## Related links

* [Populations](p1_populations.html)

* [Viewing group membership](p1_view_group_membership.html)

* [Managing group membership](p1_add_members_to_group.html)

* [Searching for users using SCIM queries](p1_searchforusers.html#scim-query-users)

## Internal and external groups

In PingOne, you can have internal groups, which are created and managed in PingOne, or external groups, which are created through a connection to an external identity provider (IdP) *(tooltip: \<div class="paragraph">
\<p>A service that manages identity information and provides authentication services to relying clients or SPs within a federated or distributed network.\</p>
\</div>)* or Lightweight Directory Access Protocol (LDAP) *(tooltip: \<div class="paragraph">
\<p>An open, cross platform protocol used for interacting with directory services.\</p>
\</div>)* gateway.

Internal groups are indicated on the **Groups** page with the **Internal Group** icon (![p1 internal group icon](_images/p1-internal-group-icon.png)) and are fully managed in PingOne. You can add, remove, and edit users directly.

You can create internal groups at the population level or the environment level. Administrators who are assigned roles scoped only to the population level can create groups for those populations only and cannot create groups at the environment level.

External groups are indicated on the **Groups** page with the **External Group** icon (![p1 external group icon](_images/p1-external-group-icon.png)). To view information about how the external groups are provisioned (for example, **Just-in-time**) and from where they are sourced (for example, **External IdP** or **LDAP Gateway**), click **Columns** and select **Sync Type** and **Group Source**. You can view the group membership for external groups in PingOne, but you can't add group members. Group membership is managed by the corresponding IdP or gateway from which the group originates. You can remove users, but the user might be added back to the group automatically the next time the group is synced with the source.

![A screenshot showing the Groups page with several internal groups and one external group. The details pane for the external group is open on the right.](_images/p1-external-groups-view.png)

## Static and dynamic groups

In PingOne, you can create static groups, dynamic groups, or a combination of both.

With static groups, you add or remove group members manually.

With dynamic groups, members are added based on rules. You'll set up an expression or filter to determine which users should be included in the group. If you change the filter criteria for a dynamic group, users will be added or removed automatically based on the current criteria in the filter. Likewise, as user attributes change to match or not match the filter, a user will be implicitly added or removed from the group.

Dynamic groups also allow you to add users directly. You can manually add users that do not match the SCIM filter.

For more information, see [Creating a group](p1_create_group.html) and [Managing group membership](p1_add_members_to_group.html).

### Dynamic group examples

You can use a custom filter to define dynamic internal groups, as in the following examples.

|   |                                                                                                                                                     |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | This topic is not applicable to external group membership. External group membership is managed through the source from which the group originates. |

#### Example 1

Filter with a simple **Any**. Include users from the following country codes:

* Country Code Equals `US`

* Country Code Equals `CA`

![Screen capture of the Create Dynamic Group page showing a filter Any with the Attribute of Country Code.](_images/vaj1669048225571.png)

#### Example 2

Filter with a simple **Any** using UUIDs. Include users from the following populations:

* Population ID Equals `10000000-0000-0000-0000-000000000001`

* Population ID Equals `20000000-0000-0000-0000-000000000001`

![Screen capture of the Create Dynamic Group page showing a filter Any with the Attribute Population ID.](_images/phf1669048669417.png)

#### Example 3

Filter with an **Any** and **All**. Include enabled users from the following populations:

* Population ID Equals `10000000-0000-0000-0000-000000000001`

* Population ID Equals `20000000-0000-0000-0000-000000000001`

* Enabled Equals `True`

![Screen capture of the Create Dynamic Group page showing a filter of Any and All with the Attributes Population ID and Enabled.](_images/vll1669049108863.png)

#### Example 4

Filter with an **All** and several **Any**. Include users from either of two populations in Canada, as well as a user with a particular email address.

* Population ID Equals `10000000-0000-0000-0000-000000000001`

* Country Code Equals `CA`

* Population ID Equals `20000000-0000-0000-0000-000000000001`

* Country Code Equals `CA`

* Email Address Equals `admin@example.com`

![Screen Capture of the Create a Dynamic Group page showing a filter of Any and All with the Attributes Population ID, Country Code and Email Address.](_images/fsw1669049382070.png)

#### Example 5

Filter with an **All** and several **Any**. All users from either of two populations that are in the US and also in the Sales department, as well as a user with a particular email address. Note that the Department attribute is a custom attribute.

* Population ID Equals `10000000-0000-0000-0000-000000000001`

* Country Code Equals `US`

* Department Equals `Sales`

* Population ID Equals `20000000-0000-0000-0000-000000000001`

* Country Code Equals `US`

* Department Equals `Sales`

* Email Address Equals `admin@example.com`

![A Screen Capture of the Create Dynamic Group page showing a filter of All and Any with the Attributes Population ID, Country Code, Department and Email Address.](_images/fyd1669049885664.png)

Learn more in [Managing group membership](p1_add_members_to_group.html).

## Nested groups

A nested group is a group that is a member of another group.

Use nested groups to allow inheritance of membership and application access from one group to its subgroups. Learn more in [Application access control](../applications/p1_application_access_control.html).

|   |                                                                             |
| - | --------------------------------------------------------------------------- |
|   | You cannot nest an environment-level group inside a population-level group. |

For example, assume an environment has three groups: Group A, Group B, and Group C. Each group has access to a single application: Group A has access to App1, Group B has access to App2, and Group C has access to App3.

If you nest Group B inside of Group A, and Group C inside of Group B, then application access will be as follows:

* Group A has access to App1.

* Group B has access to App1 and App2.

* Group C has access to App1, App2, and App3.

The following diagram illustrates this example.

![Nested groups diagram](_images/xxv1636400449025.png)

### Circular references

You can also nest groups inside their subgroups. Continuing the previous example, if you add Group A as a subgroup of Group C, creating a circular reference, then all three groups will have access to all three applications.

For more information, see [Creating a nested group](p1_create_nested_group.html), [Removing a nested group](p1_remove_nested_group.html), and [Managing group membership](p1_add_members_to_group.html).

## Group roles

To make permissions management easier, you can assign roles to groups and individual users.

Using group roles, you can:

* Manage roles for multiple users at once.

* Apply role changes in bulk.

* See users that have a certain role by viewing group members.

  You can use roles to manage permissions for groups of administrators. Learn more in [Managing administrators](../getting_started_with_pingone/p1_manage_administrators.html).

For security reasons, you can assign roles to static groups but not to dynamic groups. Dynamic groups include members based on a filter or rule. Users could be added to a dynamic group unintentionally and could inherit role assignments you don't want to give them. Learn more in [Static and dynamic groups](#p1-static-dynamic-groups).

When adding users to static groups that are assigned roles, be careful not to inadvertently assign a role to a user unintentionally when you add them to a group. If a user is assigned a role because they are in a group and you don't want them to have the role, remove the user from the group.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | * You can assign a role to a group you're a member of only if that role is assigned to you directly as an individual user, and is not assigned to you as part of a group that you belong to.

* If a built-in role you're assigned allows you to assign a different role, you can also assign that role to a group you are a member of. For example, the Identity Data Admin role has permissions that allow it to assign the Identity Data Admin Read Only role. If you're assigned the Identity Data Admin role, you can assign that role or the Identity Data Admin Read Only role to a group.

* An administrator might not have permissions to assign roles but can add or remove users from a group that has role assignments. For example, one administrator can assign roles to a group, and a different administrator can add or remove users from that group, depending on their role assignments.

* You can't add or remove yourself from a group that has roles assigned to it.

* Roles assigned to a group won't affect roles that are assigned to a user individually. If the role isn't assigned to the user directly, the role is removed when they're removed from the group.

* You can assign roles in up to 500 groups. |

Learn more in [Creating a group](p1_create_group.html) and [Managing group membership](p1_add_members_to_group.html).

---

---
title: Access user information to send to application developers
description: "You can use the API tab on the user details panel to access and copy PingOne user information in a format that's easy for application developers to use."
component: pingone
page_id: pingone:directory:p1_viewusersapi
canonical_url: https://docs.pingidentity.com/pingone/directory/p1_viewusersapi.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 24, 2024
---

# Access user information to send to application developers

You can use the **API** tab on the user details panel to access user information in a format that you can copy and give to your application developers. Use the PingOne admin console to access this information without having to make an API call.

1. In the PingOne admin console, go to **Directory > Users** and browse or search for the applicable user.

2. Click the user entry to open the details panel.

3. Click the **API** tab.

The **API** tab includes general information about the user, such as user ID, environment ID, and the URL at which the user data can be found. If a custom user schema is used, the data is available in JSON format. Click the **Copy** icon ([icon: copy, set=fa]) to copy any of this information to the clipboard and pass it to your developers.

---

---
title: Adding a custom administrator role
description: Learn how to create a custom administrator role in PingOne.
component: pingone
page_id: pingone:directory:p1_custom_role_add
canonical_url: https://docs.pingidentity.com/pingone/directory/p1_custom_role_add.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 22, 2026
section_ids:
  before-you-begin: Before you begin
  steps: Steps
  result: Result
---

# Adding a custom administrator role

Use the **Administrator Roles** page to add custom roles to the environment.

## Before you begin

You must have one of the following roles to create a custom role:

* Organization Admin

* Custom Roles Admin

* A custom role with permissions equivalent to the Custom Roles Admin

## Steps

1. In the sidebar, click the Ping Identity logo to open the **Environments** page.

2. Browse or search for the environment in which you want to add the new custom role and click it to open the details panel.

3. Click **Manage Environment**.

4. Go to **Directory > Administrator Roles** and click the **Custom Roles** tab.

5. Click **Add Custom Role**.

   |   |                                                                                                                                                                                  |
   | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | If you're creating this role outside of the **Administrators** environment, the role can be assigned only against resources within the environment or to the entire environment. |

6. From **Initial Permissions**, select a basis for the new role.

   * **Permissions Sets**

     * **No Permissions**: Start building a new role without any permissions included.

     * **Essential Permissions**: Start building a new role with the minimum set of permissions needed for the role to be usable.

   * **Roles**

     Select an existing role to use as the basis for the new role. Permissions included in the role are added to the new role. You can add or remove permissions as needed in the following steps. You can use a built-in role or custom role as the basis for a new role.

     |   |                                                                                                                      |
     | - | -------------------------------------------------------------------------------------------------------------------- |
     |   | You can use only roles that are assigned to you or that confer the permissions needed to assign that role to others. |

     |   |                                                                                                                                                                                                                                                                                                                                                                        |
     | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
     |   | Use an existing role as the basis for the new role, then remove the permissions you don't want the new role to have and add other permissions as needed. If you build a role without any starting permissions, users with that role could have issues accessing required functionality in the admin console. In some cases, the admin console might not load properly. |

7. Enter a **Name** for the new role.

   |   |                                                      |
   | - | ---------------------------------------------------- |
   |   | The role name must be unique within the environment. |

8. (Optional) Enter a **Description** for the new role.

   |   |                                                                           |
   | - | ------------------------------------------------------------------------- |
   |   | Enter information about the intended use of the role in your description. |

9. In **Assignable by**, select the roles that can assign this role to others.

10. In the **Advanced** section, select one or more of the following options to define the levels at which the role can be assigned:

    * **Organization** (available only if you're creating the role in the **Administrators** environment)

    * **Environment**

    * **Population**

    * **Application**

    * **Group**

      |   |                                                                                                                                  |
      | - | -------------------------------------------------------------------------------------------------------------------------------- |
      |   | Group role assignment applies only to users and groups. You can't assign a role at the group level for applications or gateways. |

    For example, if you want a role to be assigned only to manage individual populations in an environment but not the entire environment, select **Population**.

11. Click **Next**.

12. Add or remove permissions as needed.

    |   |                                                                                                                                                                |
    | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    |   | Leave **Automatically include essential permissions (recommended)** selected to ensure that your role has the minimum permissions needed to function properly. |

    ![alt A screenshot of the Assign Permissions page with the Organization category expanded](_images/p1-custom-role-add-assign-perms.png)

    The **Selected Permissions** tab lists the permissions that are currently selected for the role. The number in the tab header tells you how many permissions are currently associated with the role. The previous image shows a role with 335 permissions.

    There are several ways to locate permissions you want to add to or remove from the role:

    * Using the **Categories** list: In the left pane, permissions are organized under top-level categories that mirror the sidebar navigation pane in PingOne. Expand a top-level category to view the related categories and locate the permissions you want to add or remove from this role.

      The first number next to the category name indicates how many permissions in that subcategory are selected for inclusion in the role. The second number indicates the total number of permissions in that category. For example, in the previous screenshot, the current role configuration includes three of the permissions in the **Environment** category, and that category contains five permissions total. Click a category to view the permissions included in the category, including the permission name and a detailed description of what actions the permission allows the bearer to perform in PingOne.

    * Using the **Search** functionality: The search looks for your criteria in the permission name or detailed description.

      You can also search for a permission using the permission identifier, for example `dir:read:group`. The identifier is a three-part, colon-delimited string that represents the category, action, and resource to which the permission applies. For the previously mentioned identifier, `dir` represents the **Directory** category, `read` is the action, and `group` is the resource.

      ![alt Screenshot of the dir:read:group permission identifier in the search field of the Edit Permissions page with the Read Group permission in the search results.](_images/p1-custom-role-search-perms-identifier.png)

      Learn more about the identifiers for permissions in [PingOne Permissions by Identifier](https://developer.pingidentity.com/pingone-api/platform/reference/roles-and-permissions-in-pingone/pingone-permissions-by-identifier.html) in the PingOne API documentation.

      |   |                                                                                                                                                                                                                                                                                                                                                                    |
      | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
      |   | The string identifier is also used when a user tries to access an environment resource in PingOne, but does not have the appropriate permissions for access. A message uses the string identifier to indicate that they are missing a necessary permission. That string can be sent to an administrator to search for and update the user's permissions if needed. |

      ![A screenshot of the Users details pane with the Groups tab selected and a message displayed indicating that you can't view the page because you are missing a permission.](_images/p1-missing-permission-message.png)

    * Using the **Filter**: Click the **Filter** icon to find permissions based on the level at which they apply or the actions they permit.

      ![alt A screenshot of the permissions filter.](_images/p1-custom-roles-filter-to-find-perm.png)

      For example, select **Population** and **Delete** to find all permissions that can be applied at the population level and that allow the bearer to delete resources.

      ![alt A screenshot showing permissions found when selecting Population and Delete from the Filter box.](_images/p1-custom-role-filter-results.png)

      Labels below the **Search** box indicate the filters that are selected. Click the **X** on a label to remove the filter condition. Click **Clear All** to remove all conditions.

    * Using a combination of the search functionality and the filters.

    |   |                                                                                                                                                                                                                                      |
    | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
    |   | To find a permission that you want to remove from the role, perform searches and filtering on the **Selected Permissions** tab. To find a permission you want to add, perform searches and filtering on the **All Permissions** tab. |

13. Click **Next**.

    If you included privileged permissions in the role, you are prompted to confirm that you want to include them. Click **Continue** to include them, or click **Cancel** to go back and remove them from the role.

    |   |                                                                                                                   |
    | - | ----------------------------------------------------------------------------------------------------------------- |
    |   | Privileged permissions should be selected sparingly and only after careful consideration of the potential impact. |

14. Review the role on the next page and click **Save**.

## Result

The role is added to the **Custom Roles** tab on the **Administrator Roles** page and can now be assigned to users, groups, applications, or connections.

---

---
title: Adding a user in PingOne
description: Use the Users page to add users to the PingOne directory.
component: pingone
page_id: pingone:directory:p1_adduser
canonical_url: https://docs.pingidentity.com/pingone/directory/p1_adduser.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 16, 2024
section_ids:
  steps: Steps
  result: Result
---

# Adding a user in PingOne

Add users to the PingOne directory on the **Users** page.

The fields you can see and configure when adding a user in PingOne differ depending on your administrator role assignment:

* Identity Data Admin role or a custom role with equivalent permissions

  You can select or update the population for the user.

* Advanced Help Desk Admin role or a custom role with equivalent permissions scoped to the population level

  You can select or update the population for the user.

* Advanced Help Desk Admin role or a custom role with equivalent permissions scoped to the group level

  You can't see the **Population** field or assign a user to a population directly. The population assignment depends on the group to which you add the user.

|   |                                                                                                                                                                                                                                                                         |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | In environments using PingFederate as the identity provider (IdP), adding a user in PingOne doesn't create the user in the PingFederate user directory. The ability to create a user in PingOne is provided as an option for multi-factor authentication (MFA) testing. |

|   |                                                                                                                                |
| - | ------------------------------------------------------------------------------------------------------------------------------ |
|   | If your environment is configured with custom user attributes, the fields in the UI might not match the fields described here. |

## Steps

1. In the PingOne admin console, go to **Directory > Users**.

2. Click the **Plus** icon ([icon: plus, set=fa]) and select **Create User**.

3. Enter the following information.

   |   |                                                                                                                                            |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------ |
   |   | If your environment is configured with custom user attributes, the fields in the user interface might not match the fields described here. |

   | Field                               | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
   | ----------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | **Given Name**                      | The user's first name.                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
   | **Family Name**                     | The user's last name.                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
   | **Username** (required)             | A unique identifier for the user.&#xA;&#xA;In a workforce environment, you can't change the username after it is set.	&#xA;&#xA;Don't use sensitive personal information (SPI) in usernames. SPI includes details about political or religious affiliations, race, ethnicity, sexual orientation, medical or criminal history, and personal identification numbers such as Social Security numbers.                                                                                          |
   | **Email**                           | A valid email address for the user.                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
   | **Require Email to be Verified**    | Select to require users to verify their email address by entering an one-time passcode (OTP) sent to their email to complete the PingOne account creation.                                                                                                                                                                                                                                                                                                                                   |
   | **Population**                      | &#xA;&#xA;This field appears and is required if you're assigned the Identity Data Admin role, the Advanced Help Desk Admin scoped to the population level, or a custom role equivalent to one of those roles.The population to which you want to add the user. If a default population is configured for the environment, that population is selected automatically, but you can select a different population. Learn more in [Populations](p1_populations.html).                            |
   | **Group**                           | &#xA;&#xA;If you're assigned the Advanced Help Desk Admin or an equivalent custom role and it is scoped to the group level, this field is required. Otherwise this field is optional. Groups in this list are limited to those over which you have administrator permissions.The group to which you want to add the user. You can select only one group when you create a user, but you can edit the user after creation to add them to more groups. Learn more in [Groups](p1_groups.html). |
   | **Authoritative Identity Provider** | An authoritative IdP has authority over user records and credentials. By default, PingOne is the user's authoritative IdP, meaning that users authenticate and are managed in PingOne.If you've configured external IdPs in the environment, you can select one of them in the list. Learn more in [Authoritative identity providers](../integrations/p1_authoritative_idps.html).                                                                                                           |
   | **Password**                        | An initial password for the user.To generate a strong password you can provide to the user, click **Generate password**.Click the **Eye** icon ([icon: eye-slash, set=fa]) to show the password in plain text.                                                                                                                                                                                                                                                                               |

   ![Add user page](_images/p1-add-new-user.png)

4. Click **Save**.

## Result

The user is created in the PingOne directory. You can edit a user profile after creation to provide more information. Learn more in [Editing a user in PingOne](p1_edituser.html).

If you have the Advanced Help Desk Admin role or a custom role with equivalent permissions scoped to the group role, the user is assigned to a population based on the following factors:

* If the group you added the user to is a population-level group, the user is added to the same population to which the group belongs.

* If the group you added the user to is an environment-level group and a default population is defined for the environment, the user is added to the default population.

In edge cases where no default population is defined for the environment, the following occurs:

* If the administrator creating the user is in the same environment as the new user, the user is assigned to the same population as the administrator.

* If the administrator isn't in the same environment as the new user, user creation fails.

---

---
title: Adding user attributes
description: Use the Attributes page to add a user attribute to your PingOne environment.
component: pingone
page_id: pingone:directory:p1_adduserattributes
canonical_url: https://docs.pingidentity.com/pingone/directory/p1_adduserattributes.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 3, 2024
page_aliases: ["p1_enabling_user_attibutes.adoc"]
section_ids:
  steps: Steps
  related-links: Related links
---

# Adding user attributes

Use the **Attributes** page to add a user attribute to your environment.

## Steps

1. In the PingOne admin console, go to **Directory > User Attributes**.

2. Click the **[icon: plus, set=fa]**icon.

3. Select the attribute that you want to add:

   * **Declared**: Declared attributes are string attributes that applications can access through the PingOne API or the PingOne admin console. Declared attributes can be:

     * Unique

     * Multivalued

     * Enumerated

     * Validated (Regex)

   * **JSON**: JSON attributes are structured attributes that applications can access through the PingOne API or the PingOne admin console. Resources can use JSON attributes in their attribute mappings. You can use these attributes to pass complex information to applications through an access token. JSON attributes can be:

     * Multivalued

     * Validated (JSON Schema)

4. Click **Next**.

5. Enter the following information:

   * **Name**: A unique identifier for the attribute.

   * **Display Name**: The name of the attribute as you want it to look in the user interface.

   * **Description**: A brief description of the attribute.

6. Select the configuration options for the attribute:

   * **Enforce unique values**: Require that attribute values be unique across the environment.

   * **Allow multiple values**: Allow the attribute to support multiple values:

     * When a multi-valued attribute is mapped as part of an OpenID Connect (OIDC) *(tooltip: \<div class="paragraph">
       \<p>An authentication protocol built on top of OAuth that authenticates users and enables clients (relying parties) of all types to request and receive information about authenticated sessions and users. OIDC is extensible, allowing clients to use optional features such as encryption of identity data, discovery of OpenID Providers (OAuth authorization servers), and session management.\</p>
       \</div>)* or OAuth flow, the claim will be an array of values.

     * When a multi-valued attribute is mapped as part of a SAML flow, the multi-valued attribute will be a multi-valued SAML attribute in the SAML assertion. Learn more in [Mapping attributes](p1_editsamlattributemapping.html).

   * **No Validation**: No validation is needed.

   * **Enumerated Values**: Allows the attribute to have enumerated values.

   * **Regex Validation**: Requires that the attribute have a testable expression. Enter the following information to test an expression:

     * **Expression**: A unique identifier for the attribute.

     * **Description**: A brief description of the attribute.

     * **Values**: Examples of values that match or do not match the expression.

     |   |                                                                                           |
     | - | ----------------------------------------------------------------------------------------- |
     |   | After you create an attribute that is multi-valued, you can't change it to single-valued. |

7. Click **Save**.

8. To enable a user attribute, click the toggle to the right (blue).

   |   |                                                                                                                                         |
   | - | --------------------------------------------------------------------------------------------------------------------------------------- |
   |   | You can disable the user attribute by clicking the toggle to the left (gray) and clicking **Confirm** in the **Confirm Disable** modal. |

## Related links

* [Mapping attributes](p1_editsamlattributemapping.html)

---

---
title: Administrator Roles
description: Administrator roles give PingOne administrators access to resources in the admin console and determine the actions they can take in PingOne.
component: pingone
page_id: pingone:directory:p1_roles
canonical_url: https://docs.pingidentity.com/pingone/directory/p1_roles.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: August 11, 2025
section_ids:
  built-in-roles-tab: Built-In Roles tab
  built-in-pingone-administrator-roles: Built-in PingOne administrator roles
  advanced-identity-cloud-access: Advanced Identity Cloud Access
  pingfederate-access: PingFederate Access
  custom-roles-tab: Custom Roles tab
  custom-administrator-role-restrictions: Custom administrator role restrictions
  related-links: Related links
---

# Administrator Roles

An administrator role is a collection of permissions that you can assign to a user, application, or connection. Administrator roles give PingOne administrators access to resources in the PingOne admin console and determine the actions they can take in PingOne.

![Screenshot of the Administrator Roles page with the Built-in Roles tab in focus](_images/p1-admin-roles-page.png)

There are two types of administrator roles in PingOne:

* []()**Built-in roles**

  PingOne provides several built-in administrator roles, such as Environment Admin, Application Owner, and Organization Admin. These roles provide access to a wide variety of resources at multiple levels within PingOne.

  Roles can be assigned to:

  * Users

  * Groups

  * Worker applications

  * PingFederate gateways

  Roles can also be assigned at different levels:

  * Organization

  * Environment

  * Population

  * Group

  * Application

  Not all roles can be assigned at all levels, and group-level role assignment applies only to users and groups.

  The permissions included in each built-in role are designed to provide least-privilege access to the resources and actions that an administrator with that role would need to perform their job functions. For example, the Environment Admin role includes permissions for managing environments and resources within environments, while the Identity Data Admin role includes permissions for managing user identities and identity data.

  There are also built-in roles that are used to enable single sign-on (SSO) *(tooltip: \<div class="paragraph">
  \<p>The process of authenticating an identity (signing on) at one website (usually with a user ID and password) and then accessing resources secured by other domains without reauthenticating.\</p>
  \</div>)* to other Ping Identity products, such as PingOne Advanced Identity Cloud or PingFederate, and determine the administrator's level of access in those products.

  You can't modify built-in administrator roles.

  |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
  | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | Because PingOne doesn't have a global or super administrator role, role updates to support new features and functionality might be released in one of the following ways:- As updates to existing administrator roles

    New permissions might be added to existing administrator roles when new features are released to either early access or general availability.

  - As new administrator roles

    We might create a new administrator role to support a new feature. When new roles are added, we'll enable users with an existing administrator role to assign them, or assign them automatically to users who are already assigned a high-privilege role, such as Environment Admin or Identity Data Admin. |

* **Custom roles**

  You can create custom administrator roles to delegate administration of particular resources in an environment and provide least-privileged access to those resources. These roles are environment-specific and consist of a limited set of permissions that can be edited by administrators who have one of the following roles:

  * Organization Admin

  * Custom Roles Admin

  * A custom role with permissions equivalent to the Custom Roles Admin. Learn more in [Adding a custom administrator role](p1_custom_role_add.html).

  Like built-in roles, custom roles can be assigned to an individual user, group, worker application, or PingFederate gateway for a specified level in PingOne. Depending on the environment in which the role is created, a custom role can be assigned at the organization, environment, population, or group level.

  |   |                                                                                                                                                    |
  | - | -------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | Roles created for assignment at the group level can be assigned only to users and groups, and not to worker applications or PingFederate gateways. |

  If you want users from multiple environments to have access to the same custom administrator role, you must create the role in each of those environments.

Roles with the **Privileged** icon (![privileged permission icon](_images/p1-privileged-permission-icon.png)) include permissions that either provide access to sensitive information, such as personal user data, or allow the bearer to perform actions that could significantly impact the organization, such as deleting an environment. These permissions should be assigned sparingly.

|   |                                                                             |
| - | --------------------------------------------------------------------------- |
|   | Review the permissions associated with the role before you assign the role. |

* Learn more about assigning admin roles to users in [Managing user roles](p1_manage_user_roles.html).

* Learn more about assigning admin roles to a user group in [Managing group roles](p1_add_roles_to_a_group.html).

* You can also assign admin roles to worker applications. Learn more in [Configuring roles for a worker application](../applications/p1_configurerolesforworkerapplication.html).

* Learn more about the permissions associated with built-in administrator roles in [PingOne Role Permissions](https://developer.pingidentity.com/pingone-api/platform/reference/roles-and-permissions-in-pingone/pingone-role-permissions.html) in the PingOne API documentation.

## Built-In Roles tab

PingOne provides the following built-in administrator roles.

Click a role to open the details pane and view additional details about the role, including the levels to which it can be applied, for example, Environment or Application, and the permissions it includes. Built-in roles cannot be modified, but you can clone a built-in role to use it as the basis for a new custom role that you can modify.

### Built-in PingOne administrator roles

| Role                               | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| ---------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Advanced Help Desk Admin           | A role for managing user accounts, group membership, and identity credentials beyond the standard capabilities included in the Help Desk Admin role. Permissions for this role enable the administrator to perform full user lifecycle operations, manage group membership, issue and revoke credentials, and administer identity verification and MFA pairing keys to support escalated identity management tasks.                                                                                                                                                                                                                 |
| Application Owner                  | A role for managing specific applications to which they are assigned. Key permissions include assigning application access using groups, editing attributes, and configuring connection details for the application.This role has no other administrator permissions.                                                                                                                                                                                                                                                                                                                                                               |
| Authorize Gateway Policy Evaluator | This role grants the minimum permissions required for Authorize gateways to interact with PingOne. Permissions include reading gateway configuration and deployment details, such as the authorization policy version and minimum supported gateway instance version.To grant an Authorize gateway additional policy evaluation permissions, such as reading user details, checking group membership, and evaluating risk scores, create a custom administrator role and assign it to the Authorize gateway.                                                                                                                        |
| Client Application Developer       | A role for managing API client applications. The permissions for a client application developer are centered around managing applications and include functions such as creating and deleting client applications and resetting a client secret for an application.                                                                                                                                                                                                                                                                                                                                                                 |
| Configuration Read Only            | A subset of the Environment Admin role with read-only permissions only. For example, the Environment Admin role can read, update, and delete environments, but the Configuration Read Only role can read environment data only.Administrators with the Environment Admin or Configuration Read Only role can assign the Configuration Read Only role to users.                                                                                                                                                                                                                                                                      |
| DaVinci Admin                      | (Only applicable for PingOne environments that include the PingOne DaVinci service.) A role that gives PingOne administrators full read and write access to the DaVinci console. Create, edit, and delete DaVinci flows, deploy DaVinci flows, create, edit, and delete connections and variables.The user adding DaVinci to an environment is given the DaVinci Admin role.                                                                                                                                                                                                                                                        |
| DaVinci Admin Read Only            | (Only applicable for PingOne environments that include the PingOne DaVinci service.) A role that gives PingOne administrators read-only access to the DaVinci console. Read flows, connections, and variables.                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Environment Admin                  | A role for managing environments. The permissions for an environment administrator are centered around managing environments and include functions such as editing environments, managing populations, viewing password policies, and assigning certain roles.                                                                                                                                                                                                                                                                                                                                                                      |
| Help Desk Admin                    | A role for managing user multi-factor authentication (MFA) methods and devices and resolving account lockouts. The permissions for a Help Desk Admin are centered around enabling the administrator to help end users successfully authenticate with PingOne and include functions such as resetting passwords and adding or updating MFA methods and devices configured in the user record.                                                                                                                                                                                                                                        |
| Identity Data Admin                | A role for managing identities and identity data. The permissions for an identity data administrator are centered around managing user identities, and include functions like creating users and resetting a user's password.                                                                                                                                                                                                                                                                                                                                                                                                       |
| Identity Data Read Only            | A subset of the Identity Data Admin role, but with read-only permissions. For example, the Identity Data Admin role can read, update, and delete users, but the Identity Data Read Only role can read user data only. Administrators with the Identity Data Admin or Identity Data Read Only role can assign the Identity Data Read Only role to users.                                                                                                                                                                                                                                                                             |
| Organization Admin                 | A role for managing the entire organization. The permissions for an organization administrator are centered around managing organizations and include functions like creating, editing, and deleting organizations and environments.                                                                                                                                                                                                                                                                                                                                                                                                |
| Promotion Admin                    | A role for managing the promotion of environment configuration from one environment to another. The permissions for this role enable the administrator to create, update, and delete promotion variables and promotion snapshots, and create and execute promotions. To execute a promotion, the administrator must have this role in both the source environment from which the promotion is initiated and the target environment.&#xA;&#xA;This role currently functions only if you select the Configuration Management opt-in for early access. Learn more in Configuration management and promotion in PingOne (early access). |

### Advanced Identity Cloud Access

For PingOne environments that include SSO to PingOne Advanced Identity Cloud, PingOne includes Advanced Identity Cloud-specific roles. These roles give PingOne administrators access to Advanced Identity Cloud and determine their level of access.

> **Collapse: Details**
>
> | Role                                 | Description                                                                                                                 |
> | ------------------------------------ | --------------------------------------------------------------------------------------------------------------------------- |
> | Advanced Identity Cloud Super Admin  | A role for managing the Advanced Identity Cloud tenant with all administrator permissions, including adding administrators. |
> | Advanced Identity Cloud Tenant Admin | A role for managing the Advanced Identity Cloud tenant with most administrator permissions, except adding administrators.   |

### PingFederate Access

For PingOne environments that include SSO to PingFederate, PingOne includes PingFederate-specific roles. These roles give PingOne administrators access to PingFederate and determine their level of access to PingFederate.

> **Collapse: Details**
>
> | Role                                  | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
> | ------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
> | PingFederate Administrator            | Configure partner connections and most system settings, except the management of local accounts and the handling of local keys and certificates.                                                                                                                                                                                                                                                                                                                               |
> | PingFederate Auditor                  | View-only permissions for all administrative functions.&#xA;&#xA;If a user has the PingFederate Auditor role in addition to another PingFederate role, during SSO to PingFederate, the Auditor role is stripped out and only the other role remains. For example, if you have the PingFederate Auditor and PingFederate Administrator roles, when you SSO to PingFederate, the PingFederate Auditor role is removed, and you'll have only the PingFederate Administrator role. |
> | PingFederate Crypto Administrator     | Manage local keys and certificates.                                                                                                                                                                                                                                                                                                                                                                                                                                            |
> | PingFederate Expression Administrator | Map user attributes by using the OGNL (Object-Graph Navigation Language) expression language.                                                                                                                                                                                                                                                                                                                                                                                  |
> | PingFederate User Administrator       | Create users, deactivate users, change or reset passwords, and install replacement license keys.                                                                                                                                                                                                                                                                                                                                                                               |

## Custom Roles tab

If there are custom roles in the environment, they are listed on the **Custom Roles** tab.

### Custom administrator role restrictions

Custom administrator roles have certain restrictions that don't apply to the built-in administrator roles:

* Custom administrator roles are not currently supported in PingOne DaVinci.

* Custom administrator roles created in the **Administrators** environment can be assigned at the organization level to users, groups, applications, and gateways in the **Administrators** environment.

  |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
  | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
  |   | For the purposes of this documentation, the **Administrators** environment is the environment in your organization that is assigned the ADMIN license. If you renamed your **Administrators** environment, or if you assigned your ADMIN license to a different environment, that environment acts as your **Administrators** environment.If you have issues with your ADMIN license, contact Ping Identity Support. The ADMIN license is required for access to certain functionality in PingOne, including some aspects of custom roles. |

* Custom roles created in any environment other than the **Administrators** environment can't be assigned at the organization level. These roles can only be assigned against resources within the environment in which they were created or over the entire environment.

* Administrators with the Custom Roles Admin role can create custom roles, but only users with the roles selected in the **Assignable by** field for each custom role can assign that role.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | We are performing ongoing testing to ensure that all combinations of permissions work as expected for all of the pages in the PingOne admin console. However, it is possible that, at release time, certain combinations have not yet been tested. If you create a custom role, assign it, and find that certain pages do not load properly, know that we are continuing to test, and will resolve all issues. Make a note of the page that didn't load properly, and try again in a few weeks. |

If missing permissions are preventing the page from loading properly, a message similar to the following appears.

![A screenshot of the Users details pane with the Groups tab selected and a message displayed indicating that you can't view the page because you are missing a permission.](_images/p1-missing-permission-message.png)

## Related links

* [Viewing role details](p1_viewroledetails.html)

---

---
title: Attribute access control
description: Some PingOne platform self-management scopes allow organizations to specify which user profile attributes are accessible to end users.
component: pingone
page_id: pingone:directory:p1_attribute_access_control_user_atts
canonical_url: https://docs.pingidentity.com/pingone/directory/p1_attribute_access_control_user_atts.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 23, 2024
section_ids:
  related-links: Related links
---

# Attribute access control

Some PingOne platform self-management scopes allow organizations to specify which user profile attributes are accessible to end users.

An administrator might want to prevent end users from seeing or modifying particular attributes that should remain private, such as custom attributes for entitlements, internal foreign keys, account status information, or any profile data that should not be exposed to an individual user. With access control scopes, organizations can store additional private data in the user profile without risk that the end user can see the data.

These access control scopes designate a specific set of user attributes, which is often a subset of attributes that the user is allowed to read or update. For example, a `p1:update:user:email-only` scope could remove all other user schema attributes except the user's email address. A user with this scope could update only their email address. All other visible attributes would not allow modification.

## Related links

* [Configuring attribute access control](../applications/p1_configure_attribute_access_control.html)

---

---
title: Bypass MFA for a specific user
description: You can bypass multi-factor authentication (MFA) for a specific user for a specific duration. This suspends the requirement for a user to authenticate using their secondary authentication method for the specified amount of time.
component: pingone
page_id: pingone:directory:p1_pid_bypass_mfa
canonical_url: https://docs.pingidentity.com/pingone/directory/p1_pid_bypass_mfa.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  steps: Steps
---

# Bypass MFA for a specific user

You can bypass multi-factor authentication (MFA) for a specific user for a specific duration. This suspends the requirement for a user to authenticate using their secondary authentication method for the specified amount of time.

## Steps

1. In the PingOne admin console, go to **Directory > Users** and browse or search for the user that you want to edit.

2. Click the user entry to open the user details panel.

3. Click the **Services > Authentication** tab.

4. To bypass MFA for single sign-on (SSO), in the **Multi-Factor Authentication** section, click **Allow MFA bypass**, and then in the **Bypass** modal, select the bypass duration and click **Bypass**.

   The bypass time remaining and a **Resume** link are shown. Click **Resume** to resume MFA for the selected user.

5. (Workforce only) To bypass MFA for a specific service, in the **Integrations** section, next to the relevant service, click the **More Options (⋮)** icon and then select **Disable** or **Bypass**. Bypassing a service suspends the need for a user to authenticate using the secondary authentication method for a specified amount of time.

   |   |                                                                                                                                                                |
   | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | Audit events for bypassing a non-SSO service are only logged in the legacy PingID admin portal PingID report, and appear in the format `{service-name} bypass` |

---

---
title: Characters supported in PingOne user attributes
description: The characters supported in user attributes in PingOne vary depending on the attribute. Learn more in the following table.
component: pingone
page_id: pingone:directory:p1_user_atts_supported_characters
canonical_url: https://docs.pingidentity.com/pingone/directory/p1_user_atts_supported_characters.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 17, 2024
---

# Characters supported in PingOne user attributes

The characters supported in user attributes in PingOne vary depending on the attribute. Learn more in the following table.

| Attribute                                                                                                                                                                                                                                                                                        | Supported characters                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Email Address**                                                                                                                                                                                                                                                                                | Uppercase and lowercase English letters: A-Z; a-z                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                  | Arabic numerals: 0-9                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                  | The following symbols:- Exclamation mark (!)

- Pound sign (#)

- Dollar sign ($)

- Ampersand (&)

- Single quote (')

- Asterisk (\*)

- Period (.)

- Left and right parentheses ( )

- Comma (,)

- Left and right angle brackets (< >)

- Backslash (\\)

- Left and right square brackets (\[ ])

- Colon (:)

- Semicolon (;)

- At sign (@)

- Plus sign (+)

- Slash (/)

- Equals sign (=)

- Question mark (?)

- Caret (^)

- Underscore (\_)

- Backtick (\`)

- Right and left curly brackets ({ })

- Pipe (\|)

- Tilde (\~)

- Dash (-)                                                                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                  | Unicode characters between \u0080 and \uFFF                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                  | Double quotes (") if they meet the following criteria:- Must be used before the At sign (@)

  * Valid: "helloworld"@example.com

  * Invalid: helloworld@"example".com

- Must be separated by periods (.)

  * Valid: hello."world"@example.com

  * Invalid: hello"world"@example.com

- Must be paired correctly

  * Valid: "helloworld"@example.com

  * Invalid: helloworld"@example.com

- Characters after @ must be a properly formatted domain name                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| * **Username**

* **Name**

  * **Formatted**

  * **Given Name**

  * **Middle Name**

  * **Family Name**

  * **Honorific Prefix**

  * **Honorific Suffix**

* **Nickname**

* **Account ID**

* **Title**

* **Type**

* **Address**

  * **Locality**

  * **Region**

  * **Postal Code** | All characters in the following [Unicode general categories](https://en.wikipedia.org/wiki/Unicode_character_property#General_Category):* L - Letter

  * Lu

  * Ll

  * Lt

  * Lm

  * Lo

* M - Mark

  * Mn

  * Mc

  * Me

* N - Number

  * Nd

  * Nl

  * No

* P - Punctuation

  * Pc

  * Pd

  * Ps

  * Pe

  * Pi

  * Pf

  * Po

* S - Symbol

  * Sm

  * Sc

  * Sk

  * So

* Z - Separator

  * Zs

  * Zl

  * Zp                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| - **Address**

  * **Street Address**                                                                                                                                                                                                                                                            | All characters in the following [Unicode general categories](https://en.wikipedia.org/wiki/Unicode_character_property#General_Category):- L - Letter

  * Lu

  * Ll

  * Lt

  * Lm

  * Lo

- M - Mark

  * Mn

  * Mc

  * Me

- N - Number

  * Nd

  * Nl

  * No

- P - Punctuation

  * Pc

  * Pd

  * Ps

  * Pe

  * Pi

  * Pf

  * Po

- S - Symbol

  * So

- Z - Separator

  * Zs                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| * **Address**

  * **Country Code**                                                                                                                                                                                                                                                              | Two-letter country codes as listed in [ISO 3166-2](https://en.wikipedia.org/wiki/ISO_3166-2). Three-letter country codes are not supported.&#xA;&#xA;Any string of two uppercase letters is allowed, which means it is possible to enter a value that does not correspond to a country. For example, ZQ is valid in this attribute, but is not a valid country code.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| - **Primary Phone**

- **Mobile Phone**                                                                                                                                                                                                                                                          | All characters in the following [Unicode general categories](https://en.wikipedia.org/wiki/Unicode_character_property#General_Category):- L - Letter

  * Lu

  * Ll

  * Lt

  * Lm

  * Lo

- M - Mark

  * Mn

  * Mc

  * Me

- N - Number

  * Nd

  * Nl

  * No

- P - Punctuation

  * Pc

  * Pd

  * Ps

  * Pe

  * Pi

  * Pf

  * Po

- S - Symbol

  * Sm

  * Sc

  * Sk

  * So

- Z - Separator

  * Zs&#xA;&#xA;To allow for the many different ways phone numbers are written around the world, the selection of characters that are valid in this attribute is fairly broad. However, this also means that it is possible to enter a value that does not correspond to a valid phone number.&#xA;&#xA;The following list contains examples of different phone number formats:&#xA;&#xA;USA: +1 512 555 1212&#xA;&#xA;USA: +1-512-555-1212&#xA;&#xA;USA: (512) 555-1212&#xA;&#xA;Germany: (30) 1234 5678&#xA;&#xA;Australia: +61 3 1234 5678 |
| **Custom Attributes**                                                                                                                                                                                                                                                                            | Because administrators can define custom attributes that are set to **No Validation** or to a custom **Regex Validation**, supported characters will vary.If the attribute is set to use **No Validation**, all Unicode characters are supported.If the custom attribute is set to use **Regex Validation**, the **Expression** field supports all Unicode characters. The characters allowed by the expression defined in this field are the supported characters for the custom attribute.                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |

---

---
title: Creating a group
description: Create groups in PingOne.
component: pingone
page_id: pingone:directory:p1_create_group
canonical_url: https://docs.pingidentity.com/pingone/directory/p1_create_group.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: January 31, 2025
section_ids:
  steps: Steps
  next-steps: Next steps
---

# Creating a group

Use the **Groups** page to create groups. You can create static and dynamic groups. Learn more in [Static and dynamic groups](p1_groups_vs_populations.html#p1-static-dynamic-groups).

|   |                                                                                                                   |
| - | ----------------------------------------------------------------------------------------------------------------- |
|   | You must have the Identity Data Admin role or a custom role with equivalent permissions to create or edit groups. |

## Steps

1. In the PingOne admin console, go to **Directory > Groups**.

2. Click the **[icon: plus, set=fa]**icon.

3. Enter the following:

   * **Group Name**: A name for the group. The name must be unique within the environment for environment groups, and unique within a population for population groups.

   * **Description** (optional): A brief description of the group.

   * **Population** (optional): The population in which the group will be created. Users with the **Environment Admin** role can create groups at the environment level, but users with the **Identity Admin** role must assign a group to a population for which they are an **Identity Admin**. If you select a population, the group can contain users from that population only.

   * **Metadata Properties** (optional): Custom metadata properties associated with the group, represented as key-value pairs for administrative purposes.

     To add properties, click **[icon: plus, set=fa]Add** and do either of the following:

     * Enter a **Name** and **Value** in the corresponding fields.

       ![A screen capture of the Metadata Properties populated with two values](../_images/p1-metadata-properties-name-value.png)

     * To add complex properties that include JSON object values or to directly write properties as JSON, click **Edit JSON** and add the key-value data in the editor.

       ![A screen capture of the edit JSON modal in the Metadata Properties section](../_images/p1-metadata-properties.png)

     * To switch back to the field view, click **Edit Key-Value-Pairs**.

       |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
       | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
       |   | * You can't add metadata properties to the built-in system applications in PingOne, such as the **PingOne Admin Console**, **PingOne Application Portal**, and **PingOne Self-Service - MyAccount** applications.

       * To define more than 10 custom properties, you must use the JSON editor.

       * If you define fewer than 10 properties in the JSON editor, the **Overview** tab displays them in the **Name** and **Value** columns. Otherwise, they're displayed as JSON.

       * If you include a JSON object for any property value in the JSON editor, the **Overview** tab displays the properties as JSON. |

4. Click **Save**.

## Next steps

[Add members to your group](p1_add_members_to_group.html).

---

---
title: Creating a nested group
description: You must create the groups before you can nest them. Learn more in Nested groups and Creating a group.
component: pingone
page_id: pingone:directory:p1_create_nested_group
canonical_url: https://docs.pingidentity.com/pingone/directory/p1_create_nested_group.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: January 31, 2025
section_ids:
  before-you-begin: Before you begin
  steps: Steps
  choose-from: Choose from:
---

# Creating a nested group

## Before you begin

You must create the groups before you can nest them. Learn more in [Nested groups](p1_groups_vs_populations.html#p1-nested-groups) and [Creating a group](p1_create_group.html).

Use the **Groups** page to nest groups within other groups.

## Steps

1. In the PingOne admin console, go to **Directory > Groups** and browse or search for the group to use as the parent group.

2. Click the group entry to expand the details panel.

3. On the **Groups** tab, do one of the following:

   ### Choose from:

   * If the parent group doesn't have any nested groups, click **Manage Groups**.

   * If the parent group already has nested groups, click the **Pencil** icon.

4. Select the checkbox next to the group that you want to nest.

5. Click **Save**.

---

---
title: Custom role scenarios
description: The scenarios in this section detail several uses for PingOne custom administrator roles.
component: pingone
page_id: pingone:directory:p1_custom_roles_scenarios_intro
canonical_url: https://docs.pingidentity.com/pingone/directory/p1_custom_roles_scenarios_intro.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 12, 2025
section_ids:
  new-roles-created: New roles created
  custom-roles-scenario-1: "Scenario 1: Custom role assignment within a single environment"
  custom-roles-scenario-2: "Scenario 2: Custom role assignment from the Administrators environment"
  custom-roles-scenario-3: "Scenario 3: Custom role assignment for delegated administration of another environment"
---

# Custom role scenarios

Your organization wants you to create two custom roles for Support personnel. You're assigned the Custom Roles Admin role, and you have that role at the Organization level. This means you can create custom roles in all of the environments in the organization. These roles will be assigned and used in different ways in the three scenarios that follow.

The first role, Support Level 2, is an advanced role for help desk employees. We'll create this role first, because we want it to exist when we create the Support Level 1 role. This role includes all of the permissions we'll include in the Support Level 1 role, but also includes permissions for creating, reading, updating, and deleting users, locking user accounts, resetting user passwords, and assigning administrator roles to users. This role can be assigned by users with the Identity Data Admin role.

|   |                                                                                                                                                                                                                                                                                             |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Without a custom role, you would need to assign, at a minimum, the built-in Identity Data Admin role to give a user the permissions they need to perform these tasks. That role includes 160 permissions, many of which you might not need or want a support user in this capacity to have. |

The second role, Support Level 1, is an entry-level role for help desk employees and users with the role should only be able to read user records, and reset user passwords. This role can be assigned by users with the Identity Data Admin or the Support Level 2 roles.

|   |                                                                                                                                                                                                                |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Again, without custom roles, this user would require the built-in Identity Data Admin role at a minimum, because that's the role with the fewest permissions that includes the Reset User Password permission. |

You create these roles in the **Administrators** environment, because that's the environment in which administrator identities should be created. You select to include the essential permissions. There are currently four essential permissions, so the number of selected permissions is four plus the number of permissions you select manually. For example, you add seven permissions to the Support Level 2 role, so that role now has 11 total permissions assigned.

## New roles created

**Support Level 2 role summary**

![A screenshot of the Support Level 2 role summary.](_images/p1-custom-role-support-level-2.png)

**Support Level 1 role summary**

![A screenshot of the Support Level 1 role summary.](_images/p1-custom-role-support-level-1.png)

**New roles displayed on **Custom Roles** tab of **Administrator Roles** page**

![A screenshot of the Custom Roles tab of the Administrator Roles page showing the Support Level 1 and Support Level 2 roles.](_images/p1-custom-roles-support-roles-added.png)

|   |                                                                                                                                                                                                       |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The following scenarios show administrators assigning custom roles to users, but you can also assign custom roles to groups, worker applications, or PingFederate gateways, just like built-in roles. |

## Scenario 1: Custom role assignment within a single environment

The goal of this scenario is for a user in an environment to assign a custom role to another user in the same environment.

If two users exist in the same environment, and you create a custom role in that environment, a user with the applicable **Assignable by** role can assign the custom role to another user in the same environment.

In this scenario:

* User A has the Support Level 2 role in the CompanyA\_Support environment.

* User B is also in the CompanyA\_Support environment.

* Administrators with the Support Level 2 role can assign the Support Level 1 role.

* User A assigns the Support Level 1 role to User B.

  |   |                                                                                                                                                                                             |
  | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | Because this is not the **Administrators** environment, User A can't assign the role at the organization level or to any environment resource outside of the CompanyA\_Support environment. |

  ![A diagram showing User A assigning the custom Support Level 1 role to User B in the same environment.](_images/p1-custom-roles-scenario-1.png)

## Scenario 2: Custom role assignment from the Administrators environment

The goal of this scenario is to assign custom roles to two administrators and allow them to manage different environments in the organization.

To assign the Support Level 1 or Support Level 2 roles to users over multiple environments or the entire organization, the roles must be created in the **Administrators** environment. The general role assignment rules apply, which means:

* The user who is going to assign the custom role must exist in the Administrators environment.

* This user must have a role that can assign the new custom role.

* This user must have that role scoped over the environments in which you want them to be able to assign users to manage with the new custom role.

In this scenario:

* User C exists in the **Administrators** environment. They are assigned the Identity Data Admin role for all environments in the organization. The Identity Data Admin role can assign both the Support Level 1 and Support Level 2 roles.

* Because User C has the Identity Data Admin role for all of the environments in the organization, they can assign the Support Level 1 and Support Level 2 roles to users over any environment in the organization.

* User D and User E also exist in the **Administrators** environment.

* User C assigns the Support Level 1 role to User D and the Support Level 2 role to User E. Both are scoped to the CompanyA\_Support environment.

  ![A diagram outlining the scenario as documented.](_images/p1-custom-roles-scenario-2.png)

## Scenario 3: Custom role assignment for delegated administration of another environment

The goal of this scenario is for an administrator with a built-in role to assign custom support roles to users that are in a different environment.

In this scenario:

* User C exists in the **Administrators** environment. They are assigned the Identity Data Admin role for all environments in the organization.

* User F and User G exist in the CompanyA\_Support environment.

* Both the Support Level 1 and Support Level 2 roles are created in the **CompanyA\_Support** environment. These roles are assignable by the Identity Data Administrator role.

* Because User C has the Identity Data Admin role for all of the environments in the organization, they can assign the Support Level 2 role to User F in the CompanyA\_Support environment.

* User F can then assign the Support Level 1 role to User G because Support Level 1 role is assignable by either the Identity Data Admin or the Support Level 2 role, and the users both exist in the CompanyA\_Support environment.

  ![A diagram showing outlining the scenario as documented.](_images/p1-custom-roles-scenario-3.png)

---

---
title: Deleting a group
description: Use the Groups page to remove a group you no longer need.
component: pingone
page_id: pingone:directory:p1_delete_group
canonical_url: https://docs.pingidentity.com/pingone/directory/p1_delete_group.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: January 31, 2025
section_ids:
  steps: Steps
---

# Deleting a group

Use the **Groups** page to remove a group you no longer need.

## Steps

1. In the PingOne admin console, go to **Directory > Groups** and browse or search for the group you want to delete.

2. On the right side of the group entry, click the **More options (⋮)** icon and then click **Delete**.

3. In the confirmation message, click **Delete**.

---

---
title: Deleting a user
description: Use the Users page to remove user accounts that you no longer need.
component: pingone
page_id: pingone:directory:p1_deleteuser
canonical_url: https://docs.pingidentity.com/pingone/directory/p1_deleteuser.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 3, 2024
section_ids:
  steps: Steps
---

# Deleting a user

Use the **Users** page to remove user accounts that you no longer need. You can also disable a user account instead of deleting it. Learn more in [Enabling or unlocking a user account or device](p1_enable_a_user.html).

## Steps

1. In the PingOne admin console, go to **Directory > Users** and browse or search for the user you want to delete.

2. Click the **More Options (⋮)** icon, then click **Delete User**.

3. In the **Delete User** modal, click **Delete**.

---

---
title: Directory
description: The Directory branch contains the Users, Groups, Populations, User Attributes, and Administrator Roles pages.
component: pingone
page_id: pingone:directory:p1_directories_menu
canonical_url: https://docs.pingidentity.com/pingone/directory/p1_directories_menu.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 3, 2024
---

# Directory

The **Directory** branch contains the **Users**, **Groups**, **Populations**, **User Attributes**, and **Administrator Roles** pages.

See:

[Users](p1_aboutusers.html)

[Groups](p1_groups.html)

[Populations](p1_populations.html)

[User Attributes](p1_user_attributes.html)

[Administrator Roles](p1_roles.html)

---

---
title: Editing a group
description: Use the Groups page to edit existing groups in the PingOne Directory.
component: pingone
page_id: pingone:directory:p1_editing_a_group
canonical_url: https://docs.pingidentity.com/pingone/directory/p1_editing_a_group.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 12, 2025
section_ids:
  steps: Steps
---

# Editing a group

Use the **Groups** page to edit existing groups in the PingOne Directory.

## Steps

1. In the PingOne admin console, go to **Directory > Groups** and browse or search for the group you want to edit.

2. Click the group entry to expand the details panel.

3. On the **Overview** tab, edit the group name, description, or metadata properties. Learn more in [Creating a group](p1_create_group.html).

4. On the **Users** tab, edit the group membership. You can add users manually, dynamically, or a combination of both. Learn more in [Managing group membership](p1_add_members_to_group.html).

   |   |                                                                                                                                                                                                                                            |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
   |   | You can't add users to an external group in PingOne. Group membership is managed by the group source. You can remove users, but the user might be added back to the group automatically the next time the group is synced with the source. |

5. On the **Groups** tab, edit the nested groups. Learn more in [Nested groups](p1_groups_vs_populations.html#p1-nested-groups).

6. On the **Roles** tab, edit the group roles. Learn more in [Group roles](p1_groups_vs_populations.html#p1-group-roles).

7. Click the **X** in the upper right to close the group details panel.

---

---
title: Editing a user in PingOne
description: Use the Users page to edit users in the PingOne directory.
component: pingone
page_id: pingone:directory:p1_edituser
canonical_url: https://docs.pingidentity.com/pingone/directory/p1_edituser.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 12, 2025
section_ids:
  steps: Steps
---

# Editing a user in PingOne

Use the **Users** page to edit users in the PingOne directory.

This topic describes only the fields you can edit. Learn more about all of the fields you can view in [Viewing user details](p1_viewusers.html).

|   |                                                                                                                                                                                                                                                                              |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | * The fields you see and can edit vary based on your role assignment, whether you're in a Customer or a Workforce environment, and the services your license includes.

* If you have a PingID account connected to your environment, you can't edit the **Username** field. |

## Steps

1. In the PingOne admin console, go to **Directory > Users** and browse or search for the user you want to edit.

2. Click the user entry to open the details panel.

3. On the **Profile** tab, click the **Pencil** icon ([icon: pencil, set=fa]) and enter or edit user profile details, such as name, address, company information, contact information, and language preferences.

4. On the **Groups** tab, click [icon: pencil, set=fa]and add or remove the user from groups.

   If the user doesn't belong to any groups, you can click **Manage Groups** to add them to one.

   Learn more in [Groups](p1_groups.html).

5. On the **Roles** tab, edit administrator or application roles assigned to the user.

   * On the **Roles > Administrator Roles** tab, click **Grant Roles** to assign administrator roles to the user. These roles determine the actions administrators can take in PingOne and where the administrator can take them. Click the **Delete** icon ([icon: trash, set=fa]) to remove administrator roles from the user.

     |   |                                                                                                            |
     | - | ---------------------------------------------------------------------------------------------------------- |
     |   | If there aren't any application roles available in the environment, the settings are on the **Roles** tab. |

   * On the **Roles > Application Roles** tab, click [icon: pencil, set=fa]or click **Grant Application Roles** to assign or unassign roles that determine access to features and API resources in applications developed by your organization.

     |   |                                                                                             |
     | - | ------------------------------------------------------------------------------------------- |
     |   | If there aren't any application roles available in the environment, this tab isn't visible. |

     Learn more in [Managing user roles](p1_manage_user_roles.html).

6. On the **Services > Authentication** tab, manage authentication methods, the authoritative identity provider (IdP), active user sessions, and linked accounts for the user.

   |   |                                                                                                                                                                                                                                                                                                           |
   | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | Unpairing your last device or disabling MFA on your administrator account through the [PingOne Self-Service - MyAccount app](../user_experience/p1_self_service.html) will block your ability to authenticate. You'll need another administrator to re-enable your account or assist with device pairing. |

   * Click the **Multi-Factor Authentication** toggle to enable or disable MFA for the user.

   * To bypass MFA for single sign-on (SSO), in the **Multi-Factor Authentication** box, click **Allow MFA bypass**. In the **Bypass** modal, select the bypass duration and click **Bypass**.

     The bypass time remaining and a **Resume** link are shown. Click **Resume** to resume MFA requirements for the user before the bypass period has passed.

   * In the **Methods** section, you can manage the MFA methods and devices paired for the user.

     |   |                                                                                                                                                                                                        |
     | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
     |   | Click an entry to show the date and time that the method or device was paired. For mobile devices that have sent logs, this view also displays the date, time, and support ID of the most recent logs. |

     * To change the default device, locate the applicable authentication method, click the **More Options** (⋮) icon, and then click **Make Default**.

     * To unpair a method or device, locate the applicable authentication method, click the **More Options** (⋮) icon and then click **Unpair**. Unpairing a method removes it from the user profile.

     * To block an MFA method, click the **More Options** (⋮) icon for the method and select **Block**. Blocking a method prevents the user from using that method for MFA, but it doesn't remove the method from the user profile.

       After you block a device, the menu updates to show an **Unblock** option instead of **Block**.

   * In the **Authoritative Identity Provider** section, update the identity provider (IdP) that has authority over user records and defines where a user normally authenticates.

     By default, PingOne is a user's authoritative IdP, meaning that users authenticate with a PingOne username and password. If there are external IdPs configured for the environment, you can change the authoritative IdP to an external IdP:

     * Click the **More Options** (⋮) icon and select **Edit**.

     * On the **Authoritative Identity Provider** modal, select the applicable IdP and click **Save**.

     Learn more in [Authoritative identity providers](../integrations/p1_authoritative_idps.html).

   * In the **Sessions & Devices** section, you can end PingOne sessions that are active for the user.

     * To end a session, click the **More Options** (⋮) icon for the session and select **End Session**.

     Learn more in [Managing user sessions](p1_manage_user_sessions_intro.html).

   * In the **Linked accounts** section, manage any external accounts, such as Google or LinkedIn, that are linked to the user profile.

     To unlink an external account, click the **More Options** (⋮) icon, select **Unlink**, and select the applicable account.

   * (Workforce only) In the **Integrations** section, manage the services that should be enabled for the user and configure PingID settings:

     * To disable a service, locate the applicable service, click the **More Options** (⋮) icon, and then select **Disable**.

     * To bypass a service, locate the applicable service, click the **More Options** (⋮) icon, and then select **Bypass**. In the **Bypass** modal, select the bypass duration and click **Bypass**.

       Bypassing a service suspends the need for a user to authenticate using the secondary authentication method for a specified amount of time. After the specified time elapses, PingOne resumes the service automatically.

     * To configure PingID settings, click **Configure Now**. Learn more about PingID settings in [PingID User Life Cycle Management](https://docs.pingidentity.com/pingid/pingid_user_life_cycle_management/pid_user_life_cycle_management.html) in the PingID documentation.

7. (PingOne Credentials only) On the **Services > Credentials** tab, you can revoke credentials for the user. Learn more in [Managing a user's credentials](p1_manage_user_credentials.html).

8. (PingOne Verify only) On the **Services > ID Verification** tab , the actions you can take depend on whether you're in a Customer or a Workforce environment:

   * **Customer environments**

     View user ID verification (IDV) results and Identity Assurance (IDA). You can manage IDA claims and transactions. Learn more about enabling IDA in [Creating a verify policy](../identity_verification_using_pingone_verify/p1_verify_creating_verify_policy.html).

     * In the **Identity Assurance Claims** section:

       * Click **Show** to display IDA attributes that were verified during the IDV process and stored per policy configuration.

       * Click **Reset Data** to reset the identity assurance claims for the user.

     * In the **Transaction ID** section:

       * Click **View** to view the metadata **Result** for a specific transaction ID.

       * Click **Manually Approve** to approve user ID verification manually.

   * **Workforce environments**

     View the user verification history, reset verification status, or manually approve a user. Learn more in [PingOne Verify](../identity_verification_using_pingone_verify/p1_verify_start.html).

9. On the **API** tab, click the **Copy** icon ([icon: copy, set=fa]) to copy particular values, such as user ID, environment ID, and population ID. You can also copy the user record in JSON format.

   You can then forward this information to your application developers.

---

---
title: Editing user attributes
description: You can edit existing user attributes in your environment.
component: pingone
page_id: pingone:directory:p1_edituserattributes
canonical_url: https://docs.pingidentity.com/pingone/directory/p1_edituserattributes.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 3, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
  choose-from: Choose from:
  related-links: Related links
---

# Editing user attributes

You can edit existing user attributes in your environment.

## About this task

Core and standard attributes are system-provided attributes. While core attributes cannot be edited or disabled, standard attributes have a limited editing ability. Use the **Attributes** page to edit an existing user attribute.

## Steps

1. In the PingOne admin console, go to **Directory > User Attributes**.

2. Locate the attribute that you want to edit by browsing or searching for it.

   ### Choose from:

   * Click the **More Options** (⋮) icon and then click **Edit Attribute**.

   * Click the attribute that you want to edit, and then click the pencil icon.

3. Select the configuration options for the attribute:

   * **Enforce unique values**: Require that attribute values be unique across the environment.

   * **Allow multiple values**: Allow the attribute to support multiple values:

     * When a multi-valued attribute is mapped as part of an OIDC or OAuth flow, then the claim will be an array of values.

     * When a multi-valued attribute is mapped as part of a SAML flow, then the multi-valued attribute will be a multi-valued SAML attribute in the SAML assertion. See [Mapping attributes](p1_editsamlattributemapping.html).

   * **No Validation**: No validation is needed.

   * **Enumerated Values**: Allow the attribute to have enumerated values.

   * **Regex Validation**: Requires that the attribute have a testable expression. Enter the following information to test an expression:

     * **Expression**: A unique identifier for the attribute.

     * **Description**: A brief characterization of the attribute.

     * **Values**: Examples of values that match or do not match the expression.

       |   |                                                                                                                                                               |
       | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
       |   | After you create an attribute that is multi-valued, you cannot change it to single-valued. Not all attribute properties can be edited in the PingOne console. |

4. Click **Save**.

5. To enable a user attribute, click the toggle to the right (blue).

   |   |                                                                                                                                         |
   | - | --------------------------------------------------------------------------------------------------------------------------------------- |
   |   | You can disable the user attribute by clicking the toggle to the left (gray) and clicking **Confirm** in the **Confirm Disable** modal. |

## Related links

* [Mapping attributes](p1_editsamlattributemapping.html)

---

---
title: Enabling consent updates
description: Learn how to allow users to view and update their consents in PingOne.
component: pingone
page_id: pingone:directory:p1_enable_consent_updates
canonical_url: https://docs.pingidentity.com/pingone/directory/p1_enable_consent_updates.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 3, 2024
section_ids:
  steps: Steps
---

# Enabling consent updates

To allow users to view and update their consents in PingOne, you must enable the `Manage OAuth Consents` option for the self-service application. Selecting this option enables the **Application** section under **Consents** and enables the end user to revoke any OAuth consent by enabling the **Delete** icon ([icon: trash, set=fa]) for each consent.

## Steps

1. In the PingOne admin console, go to **User Experience > Self Service**.

2. Click the **Pencil** icon ([icon: pencil, set=fa]).

3. Select the **Manage OAuth Consents** checkbox.

   Selecting this option enables the following two scopes for the self-service application:

   * `p1:read:oauthConsents` Allows the user to view their OAuth consents.

   * `p1:update:oauthConsents` Allows the user to revoke their OAuth consents.

4. Click **Save**.

---

---
title: Enabling end users to view consents
description: You can allow end users to view their consents, but not revoke them, in PingOne.
component: pingone
page_id: pingone:directory:p1_enable_end_users_to_view_consents
canonical_url: https://docs.pingidentity.com/pingone/directory/p1_enable_end_users_to_view_consents.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 3, 2024
section_ids:
  steps: Steps
---

# Enabling end users to view consents

To allow end users to view their consents, but not revoke them, add the `p1:read:oauthConsents` scope to the self-service application.

## Steps

1. In the PingOne admin console, go to **Applications > Applications**.

2. Locate the **PingOne Self-Service - MyAccount** application, and click the application entry to open the details panel.

3. On the **Resources** tab, click the **Pencil** icon ([icon: pencil, set=fa]).

4. Add `p1:read:oauthConsents` to the **Allowed scopes** column.

5. Click **Save**.