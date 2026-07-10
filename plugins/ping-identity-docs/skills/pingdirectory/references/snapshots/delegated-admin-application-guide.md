---
title: Adding a user to a group
description: You can add users to groups from the Manage Users page and from the Manage Groups page in the Delegated Admin GUI.
component: pingdirectory
version: 11.1
page_id: pingdirectory:delegated_admin_application_guide:pd_da_add_user_to_group
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/delegated_admin_application_guide/pd_da_add_user_to_group.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 13, 2023
page_aliases: ["pd_da_add_user_to_configured_group.adoc", "pd_da_add_user_from_manage_users_window.adoc", "pd_da_add_user_from_manage_groups_window.adoc"]
section_ids:
  adding-a-new-user-to-a-configured-group: Adding a new user to a configured group
  about-this-task: About this task
  steps: Steps
  adding-a-user-from-the-manage-users-window: Adding a user from the Manage Users window
  steps-2: Steps
  result: Result:
  adding-a-user-from-the-manage-groups-window: Adding a user from the Manage Groups window
  steps-3: Steps
  result-2: Result:
---

# Adding a user to a group

You can add users to groups from the **Manage Users** page and from the **Manage Groups** page in the Delegated Admin GUI.

## Adding a new user to a configured group

### About this task

When the delegated admin rights for a user REST resource type have the `resources-in-specific-groups` admin scope, a user is added to one of the configured groups when you create the user:

* For admins with rights to only one group, the new user is automatically added to that group. No field for `Select Group` displays.

* For admins with rights to more than one group, the admin selects a group to add the user to in the `Select Group` list.

* Admins can select from both static and dynamic groups.

* For dynamic groups, in addition to selecting the group, the new entry must also match criteria for membership of that group.

  For example, in a dynamic group of members with `uid=user.111*`, the `uid` starts with `user.111`.

To create a new user in that group, an administrator must:

### Steps

1. In the `Select Group` list, select the group name.

2. Enter the value for `uid` that starts with `user.111`.

## Adding a user from the Manage Users window

You can add users to groups using the **Manage Users** window in the Delegated Admin GUI.

### Steps

1. In the Delegated Admin GUI, go to the **Manage Users** window.

2. Use to search field to search for the user to add to a group.

3. Click the **Expand** icon on the appropriate user profile.

4. To edit the user profile, click the **Pencil** icon.

5. Click the **Group Membership** tab.

6. Use the search field to search for the appropriate group.

7. To add the user to the respective group, in the **Nonmember Groups** list, click **[icon: plus, set=fa]**.

   #### Result:

   The group moves to the **Member Groups** list.

## Adding a user from the Manage Groups window

You can add users to groups using the **Manage Groups** window in the Delegated Admin GUI.

### Steps

1. In the Delegated Admin GUI, go to the **Manage Groups** window.

2. To filter by group resource type, make a selection from the drop-down list for the group resource type you want to search within.

3. (Optional) To narrow your results, use the search field to search for the appropriate group.

4. Click the **Expand** icon on your chosen group.

5. To edit the group profile, click the **Pencil** icon.

6. Under the group name, click **Group Membership**.

7. (Optional) To filter entries by resource type, make a selection from the **Select a Type** drop-down list.

   |   |                                                                                                                                                                     |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | If there is a parent resource type, a second drop-down list appears. Make an additional selection, or leave it to **All** to see all entries in that resource type. |

8. Use the search field to search for the appropriate entry.

9. To add an entry to the group, from the **Nonmembers** list, click **[icon: plus, set=fa]**.

   #### Result:

   The user moves to the **Members** list.

---

---
title: Authentication configuration
description: The delegated administrator signs on to Delegated Admin through your chosen identity provider (IdP), which is configured as the authentication server and OpenID Connect (OIDC) provider.
component: pingdirectory
version: 11.1
page_id: pingdirectory:delegated_admin_application_guide:pd_da_authn_config
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/delegated_admin_application_guide/pd_da_authn_config.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 18, 2023
section_ids:
  interaction-with-the-pingdirectory-server: Interaction with the PingDirectory server
  authorization-by-the-pingdirectory-server: Authorization by the PingDirectory server
---

# Authentication configuration

The delegated administrator signs on to Delegated Admin through your chosen identity provider (IdP) *(tooltip: \<div class="paragraph">
\<p>A service that manages identity information and provides authentication services to relying clients or SPs within a federated or distributed network.\</p>
\</div>)*, which is configured as the authentication server and OpenID Connect (OIDC) *(tooltip: \<div class="paragraph">
\<p>An authentication protocol built on top of OAuth that authenticates users and enables clients (relying parties) of all types to request and receive information about authenticated sessions and users. OIDC is extensible, allowing clients to use optional features such as encryption of identity data, discovery of OpenID Providers (OAuth authorization servers), and session management.\</p>
\</div>)* provider.

The IdP validates the user's credentials against the PingDirectory server, encapsulates information claims about the user's identity, and issues an access token *(tooltip: \<div class="paragraph">
\<p>A data object by which a client authenticates to a resource server and lays claim to authorizations for accessing particular resources.\</p>
\</div>)* to Delegated Admin. Delegated Admin then presents the token to the PingDirectory server in the HTTP Authorization request header.

## Interaction with the PingDirectory server

The PingDirectory server is configured to accept access tokens by using access token validators. The values that the IdP sets for the access token `sub` claim must be mappable to a distinguished name (DN) *(tooltip: \<div class="paragraph">
\<p>A name uniquely identifying an object within the hierarchy of a directory tree.\</p>
\</div>)* in the PingDirectory server. Setting up an access token validator for use with Delegated Admin requires some coordination with the server configuration. In the suggested default configuration, the access token contains the entryUUID of the administrator user entry in the `sub` claim. This value is mapped back to a PingDirectory server entry by using an Exact Match Identity Mapper.

## Authorization by the PingDirectory server

After validation, the PingDirectory server checks the Delegated Admin configuration for authorization of the delegated administrator. Users or groups of users are authorized as delegated administrators in the PingDirectory server admin console or with the `dsconfig` tool.

---

---
title: Changing the application logo
description: You can change the Ping Identity logo to your corporate logo.
component: pingdirectory
version: 11.1
page_id: pingdirectory:delegated_admin_application_guide:pd_da_change_application_logo
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/delegated_admin_application_guide/pd_da_change_application_logo.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 21, 2023
section_ids:
  about-this-task: About this task
  steps: Steps
  result: Result
---

# Changing the application logo

You can change the Ping Identity logo to your corporate logo.

## About this task

Support for corporate logos includes, but is not limited to, the following file types:

* `JPG`

* `PNG`

* `SVG`

To maintain an appropriate aspect ratio, logo images are resized in Delegated Admin to a height of 22px and a maximum width of 150px.

## Steps

1. To change the Ping Identity logo to your corporate logo, add the following line to the `config.js` configuration file:

   ```
   window.HEADER_BAR_LOGO = '<filename>';
   ```

2. Add the logo to the build directory.

   |   |                                                          |
   | - | -------------------------------------------------------- |
   |   | Make sure to use the same file name specified in step 1. |

## Result

The corporate logo appears in the header, and the Ping Identity logo relegates to the sidebar in grayscale, preceded by "Powered by".

---

---
title: Changing the default OIDC grant type
description: To change the Delegated Admin application's default OpenID Connect (OIDC) grant type, use the PingFederate admin console and the Delegated Admin config.js file.
component: pingdirectory
version: 11.1
page_id: pingdirectory:delegated_admin_application_guide:pd_da_change_oidc_grant_type
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/delegated_admin_application_guide/pd_da_change_oidc_grant_type.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 22, 2023
section_ids:
  steps: Steps
  example: Example:
---

# Changing the default OIDC grant type

To change the Delegated Admin application's default OpenID Connect (OIDC) grant type, use the PingFederate admin console and the Delegated Admin `config.js` file.

To improve authentication security, switch your default OIDC grant type to **Authorization Code** with **Require Proof Key for Code Exchange (PKCE)**. The Authorization Code with PKCE grant type hides access tokens during authentication with JavaScript applications. In comparison, the Implicit grant type displays access tokens in the URL redirect during OIDC authentication.

|   |                                                                                                                                                                                                                                                       |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | We deprecated support for the Implicit grant type and will remove it in a future release. Use the Authorization Code with PKCE grant type instead. Learn more about [OAuth grant types](https://oauth.net/2/grant-types/) in the OAuth documentation. |

The following example changes the default OIDC grant type from **Implicit** to **Authorization Code** with **Require Proof Key for Code Exchange (PKCE)**.

## Steps

1. In the PingFederate admin console, go to **Applications > OAuth > Clients**.

2. From the **Clients** list, select the **dadmin** client.

3. In the **Allowed Grant Types** section:

   1. Select the **Authorization Code** checkbox.

   2. Clear the **Implicit** checkbox.

   3. Select the **Require Proof Key for Code Exchange (PKCE)** checkbox.

   4. Click **Save**.

4. From your `<server-root>` directory, open the Delegated Admin application's `config.js` file and set the `AUTHENTICATE_WITH_PKCE` variable to `true`.

   ### Example:

   ```
   /*
    * Indicates if this app should authenticate using the 'Authorization Code with PKCE' OAuth grant.
    * If true, the 'Authorization Code with PKCE grant will be used. If false, the 'Implicit' grant
    * will be used. * DEFAULT: window.AUTHENTICATE_WITH_PKCE = true;
    */
   window.AUTHENTICATE_WITH_PKCE = true;
   ```

   |   |                                                                                                            |
   | - | ---------------------------------------------------------------------------------------------------------- |
   |   | If you don't already have the `AUTHENTICATE_WITH_PKCE` variable in your `config.js` file, you must add it. |

---

---
title: Compatibility matrix
description: The following matrix identifies the minimum versions of the PingDirectory server required to access the full functionality provided by each release of Delegated Admin.
component: pingdirectory
version: 11.1
page_id: pingdirectory:delegated_admin_application_guide:pd_da_compatibility_matrix
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/delegated_admin_application_guide/pd_da_compatibility_matrix.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: January 25, 2024
---

# Compatibility matrix

The following matrix identifies the minimum versions of the PingDirectory server required to access the full functionality provided by each release of Delegated Admin.

|   |                                                                                                         |
| - | ------------------------------------------------------------------------------------------------------- |
|   | When using PingFederate as the identity provider, Delegated Admin requires PingFederate 9.0.0 or later. |

| Delegated Admin | PingDirectory server |
| --------------- | -------------------- |
| 5.1.0           | 9.3.0.0              |
| 5.0.0           | 9.3.0.0              |
| 4.10.0          | 9.1.0.0              |
| 4.9.0           | 9.1.0.0 EA           |
| 4.8.0           | 9.0.0.0              |
| 4.7.0           | 9.0.0.0 EA           |
| 4.6.0           | 8.3.0.0              |
| 4.5.0           | 8.3.0.0 EA           |
| 4.4.1           | 8.2.0.0              |
| 4.4.0           | 8.2.0.0              |
| 4.3.0           | 8.2.0.0 EA           |

---

---
title: Configuration overview
description: To operate Delegated Admin, you must install and configure PingDirectory server and have one of the following identity provider (IdP) options available:
component: pingdirectory
version: 11.1
page_id: pingdirectory:delegated_admin_application_guide:pd_da_config_overview
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/delegated_admin_application_guide/pd_da_config_overview.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 13, 2023
---

# Configuration overview

To operate Delegated Admin, you must install and configure PingDirectory server and have one of the following identity provider (IdP) *(tooltip: \<div class="paragraph">
\<p>A service that manages identity information and provides authentication services to relying clients or SPs within a federated or distributed network.\</p>
\</div>)* options available:

* An installed and configured PingFederate server

* Other configured OpenID Connect (OIDC) *(tooltip: \<div class="paragraph">
  \<p>An authentication protocol built on top of OAuth that authenticates users and enables clients (relying parties) of all types to request and receive information about authenticated sessions and users. OIDC is extensible, allowing clients to use optional features such as encryption of identity data, discovery of OpenID Providers (OAuth authorization servers), and session management.\</p>
  \</div>)* providers

For installation instructions, see the documentation for each product. Learn more about the Delegated Admin [Installation requirements](../installing_the_pingdirectory_suite_of_products/pd_da_install_requirements.html).

To configure support for [Delegated Admin on a PingDirectory server](pd_da_config_delegated_admin_rights_pd_server.html), complete the following tasks:

* Configure users as Delegated Admin administrators.

* Configure attributes and attribute searching.

* Configure groups whose management requires delegation.

To configure support for [using PingFederate as the IdP](pd_da_config_pf_server.html), complete the following tasks:

* Configure PingFederate as the identity provider for Delegated Admin.

* Configure PingFederate as the OAuth server for Delegated Admin.

* Register Delegated Admin as a client.

* Register the PingDirectory server as an OAuth token validator client.

To configure support for [using an OIDC provider as the IdP](pd_da_config_oidc_idp.html), complete the following tasks:

* Configure the OIDC provider as the identity provider for Delegated Admin.

* Configure an identity mapper.

* Configure an access token validator.

---

---
title: Configuring a resource&#8217;s summary display in the Delegated Admin GUI
description: The Delegated Admin GUI provides a summary of attributes for a resource. For example, the user and group resource profiles show a summary.
component: pingdirectory
version: 11.1
page_id: pingdirectory:delegated_admin_application_guide:pd_da_config_resource_summary_display_gui
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/delegated_admin_application_guide/pd_da_config_resource_summary_display_gui.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 20, 2023
section_ids:
  about-this-task: About this task
  steps: Steps
  choose-from: Choose from:
---

# Configuring a resource's summary display in the Delegated Admin GUI

The Delegated Admin GUI provides a summary of attributes for a resource. For example, the user and group resource profiles show a summary.

## About this task

By default, a resource's summary shows all required attributes and all search attributes for the resource. However, you can explicitly set the items to include in the summary.

If you configure any attributes to appear in the summary, the default selection does not appear.

To configure an attribute to appear in the summary, either use `dsconfig` to set the `include-in-summary` property or use the PingDirectory admin console to select the **Include In Summary** checkbox.

## Steps

* For a given resource, configure each attribute to include in the summary.

  ### Choose from:

  * Use `dsconfig`.

    Use the `set-delegated-admin-attribute-prop` subcommand, where *\<name\_of\_type>* is the resource type and *\<type\_of\_attribute>* is the name of an existing attribute for the given resource.

    ```shell
    $ bin/dsconfig set-delegated-admin-attribute-prop \
      --type-name  <name_of_type>  \
      --attribute-type  <type_of_attribute>  \
      --set include-in-summary:true
    ```

    The following example includes the `cn` attribute in the summary for the `users` resource type:

    ```shell
    $ bin/dsconfig set-delegated-admin-attribute-prop \
      --type-name users \
      --attribute-type cn \
      --set include-in-summary:true
    ```

    |   |                                                                                             |
    | - | ------------------------------------------------------------------------------------------- |
    |   | To remove an attribute from the summary, use the same command but change `true` to `false`. |

  * Use the PingDirectory admin console.

    1. Sign on to the PingDirectory admin console.

    2. From the **Configuration** page, click **REST Resource Types**.

    3. To edit a resource type, select it from the **Name** column.

    4. Go to the **Delegated Admin Attributes** section.

    5. To edit an attribute, click the **Pencil** icon.

    6. Select the **Include In Summary** checkbox.

       |   |                                                                                     |
       | - | ----------------------------------------------------------------------------------- |
       |   | To remove an attribute from the summary, clear its **Include In Summary** checkbox. |

---

---
title: Configuring attributes and attribute search on the PingDirectory server
description: Use the Delegated Admin installation file to configure attributes and attribute search.
component: pingdirectory
version: 11.1
page_id: pingdirectory:delegated_admin_application_guide:pd_da_config_attr_search_pd_server
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/delegated_admin_application_guide/pd_da_config_attr_search_pd_server.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 18, 2023
page_aliases: ["pd_da_constructed_attributes.adoc", "pd_da_set_attribute_read_only.adoc"]
section_ids:
  about-this-task: About this task
  steps: Steps
  example: Example:
  example-2: Example:
  example-3: Example:
  example-4: Example:
  example-5: Example:
  example-6: Example:
  example-7: Example:
  example-8: Example:
  constructed-attributes: Constructed attributes
  setting-an-attribute-to-read-only: Setting an attribute to read-only
  about-this-task-2: About this task
  steps-2: Steps
  example-9: Example:
  example-10: Example:
---

# Configuring attributes and attribute search on the PingDirectory server

Use the Delegated Admin installation file to configure attributes and attribute search.

## About this task

The file that installs Delegated Admin specifies the following values:

* Object class of user entries through `structural-ldap-objectclass:inetOrgPerson`

* Number of user attributes *(tooltip: \<div class="paragraph">
  \<p>Distinct characteristics that describe a subject. If the subject is a website user, attributes can include a name, group affiliation, email address, and attributes alike.\</p>
  \</div>)* to expose

  |   |                                                                                                                                                                                                                                                                                                                                                              |
  | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
  |   | Delegated Admin supports the following attribute types:- `Boolean`

  - `Integer`

  - `String`

  - `DateTime`

  - distinguished name (DN) *(tooltip: \<div class="paragraph">&#xA;\<p>A name uniquely identifying an object within the hierarchy of a directory tree.\</p>&#xA;\</div>)*

  - Custom attributes

  - Constructed attributes

  - Multivalued attributes |

## Steps

1. If necessary, change the attribute that is designated as the primary attribute.

   ### Example:

   ```shell
   $ bin/dsconfig set-rest-resource-type-prop \
     --type-name users \
     --set primary-display-attribute-type:mail
   ```

2. Configure any additional user attributes to appear in Delegated Admin by specifying the Lightweight Directory Access Protocol (LDAP) *(tooltip: \<div class="paragraph">
   \<p>An open, cross platform protocol used for interacting with directory services.\</p>
   \</div>)* attribute type to expose and by providing a display name for it.

   ### Example:

   ```shell
   $ bin/dsconfig create-delegated-admin-attribute \
     --type-name users \
     --attribute-type customAttr \
     --set "display-name:My custom attribute"
   ```

3. Configure attributes with distinguished name (DN) syntax on resource types to provide a reference from one resource to another.

   Such an attribute is the standard LDAP `manager` attribute.

   The referencing resource doesn't have to be the same type of resource as the referenced resource. Delegated Admin allows the referenced resource to be selected without displaying the actual value of the DN.

   ### Example:

   In this example, the `manager` attribute is included in the users resource type, and its value is constrained to reference only resources of type `managers`. The `managers` REST Resource Type is assumed to have already been defined.

   ```shell
   $ bin/dsconfig create-delegated-admin-attribute \
     --type-name users \
     --attribute-type manager \
     --set display-name:Manager \
     --set reference-resource-type:managers
   ```

   ### Example:

   Additionally, the Delegated Admin resource rights for the administrator must provide either read or reference permission to `managers`.

   ```shell
   $ bin/dsconfig create-delegated-admin-resource-rights \
     --rights-name Admin \
     --rest-resource-type managers \
     --set enabled:true \
     --set admin-permission:reference \
     --set admin-scope:all-resources-in-base
   ```

   For more information about resource rights and permissions, see [Configuring delegated administrator rights on the PingDirectory server](pd_da_config_delegated_admin_rights_pd_server.html).

4. Use the following command to set the search filter, where `%%` represents the search text entered in the web application.

   ### Example:

   ```shell
   $ bin/dsconfig set-rest-resource-type-prop \
     --type-name users \
     --set 'search-filter-pattern:(|(cn=*%%*)(mail=%%*)(uid=%%*))'
   ```

   When search text is entered in Delegated Admin, the property `search-filter-pattern` specifies which attributes to search in the PingDirectory server. To satisfy the query, define the appropriate attribute indexes for the PingDirectory server. For more information, see the PingDirectory Server Administration Guide.

5. To manage users whose profiles feature a large number of attributes, place the attributes in logical groupings, called attribute categories, and give them a specific display order.

   ### Example:

   The following commands create attribute categories and specify their display order.

   ```shell
   $ bin/dsconfig create-delegated-admin-attribute-category \
     --display-name "Basic Information" \
     --set display-order-index:1

   $ bin/dsconfig create-delegated-admin-attribute-category \
     --display-name "Contact Information" \
     --set display-order-index:2

   $ bin/dsconfig create-delegated-admin-attribute-category \
     --display-name "Other Attributes" \
     --set display-order-index:3
   ```

6. The following example commands assign attributes to a category and specify the display order of each attribute within its category.

   ### Example:

   ```shell
   $ bin/dsconfig set-delegated-admin-attribute-prop \
     --type-name users \
     --attribute-type cn \
     --set "attribute-category:Basic Information" \
     --set display-order-index:1

   $ bin/dsconfig set-delegated-admin-attribute-prop \
     --type-name users \
     --attribute-type sn \
     --set "attribute-category:Basic Information" \
     --set display-order-index:2
   ```

   Unassigned attributes are displayed in a miscellaneous category.

7. For multivalued LDAP attributes, indicate whether the application should present them as multivalued.

   If not specified, the attributes are presented in the application as single-valued, even if the LDAP schema definition for the attribute allows multiple values.

   |   |                                                                                      |
   | - | ------------------------------------------------------------------------------------ |
   |   | This setting does not apply to attributes that are handled by custom UI form fields. |

   ### Example:

   ```shell
   $ bin/dsconfig set-delegated-admin-attribute-prop \
    --type-name users \
    --attribute-type mail \
    --set multi-valued:true
   ```

## Constructed attributes

A constructed attribute is an attribute whose value is computed from values that are assigned to other attributes. For example, the system might construct a full- or common-name attribute, `cn`, from values that are assigned to the standard `givenName` and `sn` attributes, as follows:

```
dsconfig create-constructed-attribute \
  --attribute-name ReqConstructedCN --set attribute-type:cn \
  --set 'value-pattern:{givenName} {sn}'
```

Beginning with Delegated Admin 3.5.0 and PingDirectory server 7.3.0.1, the value of a constructed attribute can be updated automatically whenever the value of a source attribute is created or when it is edited.

```
dsconfig set-rest-resource-type-prop \
  --type-name users  \
  --set post-create-constructed-attribute:ReqConstructedCN  \
  --set update-constructed-attribute:ReqConstructedCN
```

In these examples, a change to the value of `givenName` or `sn` forces a corresponding change to the value of `cn`. Attributes that contribute to a required constructed attribute are identified in the UI as **Required** even if they were not originally designated as such. Because `cn` is a required attribute in this example, `givenName` and `sn` are also required.

|   |                                                                                         |
| - | --------------------------------------------------------------------------------------- |
|   | An attribute's capability of being changed after its creation is called its mutability. |

As with standard attributes, constructed attributes are stored as LDAP *(tooltip: \<div class="paragraph">
\<p>An open, cross platform protocol used for interacting with directory services.\</p>
\</div>)* attributes in a database like the PingDirectory server.

## Setting an attribute to read-only

### About this task

Beginning with Delegated Admin 3.5.0 and PingDirectory 7.3.0.1, you can set user access to standard and constructed attributes to `read-only` and `read/write`. You should restrict access to constructed attributes to `read-only`. Read-only attributes do not appear on the UI pages that are associated with the creation of users groups and other objects.

### Steps

* Use the `dsconfig` tool to set a standard or constructed attribute as `read-only`.

  #### Example:

  ```
  dsconfig set-delegated-admin-attribute \
    --type-name users  \
    --attribute-type modifyTimestamp  \
    --set mutability:read-only
  ```

  #### Example:

  The following example resets a standard or constructed attribute from `read-only` to `read/write`:

  ```
  dsconfig set-delegated-admin-attribute \
    --type-name users  \
    --attribute-type modifyTimestamp  \
    --reset mutability
  ```

---

---
title: Configuring Delegated Admin
description: This section describes the necessary configuration to support Delegated Admin after the application is installed successfully.
component: pingdirectory
version: 11.1
page_id: pingdirectory:delegated_admin_application_guide:pd_da_config_delegated_admin
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/delegated_admin_application_guide/pd_da_config_delegated_admin.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 13, 2023
---

# Configuring Delegated Admin

This section describes the necessary configuration to support Delegated Admin after the application is installed successfully.

At a minimum, you must configure the following properties on the PingDirectory server:

* Delegated administrator rights

* REST resource type

* Attributes and attribute searching

---

---
title: Configuring Delegated Admin as a new client (create OAuth client for Delegated Admin)
description: The following task configures Delegated Admin as a new client and outlines how to create an OAuth client for Delegated Admin.
component: pingdirectory
version: 11.1
page_id: pingdirectory:delegated_admin_application_guide:pd_da_config_delegated_admin_new_client
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/delegated_admin_application_guide/pd_da_config_delegated_admin_new_client.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: October 3, 2023
section_ids:
  about-this-task: About this task
  steps: Steps
  next-steps: Next steps
---

# Configuring Delegated Admin as a new client (create OAuth client for Delegated Admin)

The following task configures Delegated Admin as a new client and outlines how to create an OAuth *(tooltip: \<div class="paragraph">
\<p>A standard framework that enables an application (OAuth client) to obtain access tokens from an OAuth authorization server for the purpose of retrieving protected resources on a resource server.\</p>
\</div>)* client for Delegated Admin.

## About this task

To configure Delegated Admin as a new client:

## Steps

1. Sign on to the PingFederate admin console.

2. Go to **Applications → OAuth → Clients**.

3. Click **Add Client**.

4. For both the **Client ID** and **Name**, specify `dadmin`.

5. Set **Client Authentication** to **None**.

   |   |                             |
   | - | --------------------------- |
   |   | Do not set a client secret. |

6. For **Redirect URIS**, enter the appropriate URI for your environment based on the following table and then click **Add**.

   |                                                                              |                                                   |
   | ---------------------------------------------------------------------------- | ------------------------------------------------- |
   | For Delegated Admin on a PingDirectory server or a PingDirectoryProxy server | `https://<server-host>:<server-port>/delegator/*` |
   | For Delegated Admin on a web server hosted locally                           | `http://localhost:<server-port>/*`                |

7. Make the following selections:

   1. In the **Bypass Authorization Approval** section, select **Bypass**.

   2. In the **Exclusive Scopes** section, select **Allow Exclusive Scopes** and then select **urn:pingidentity:directory-delegated-admin**.

   3. In the **Allowed Grant Types** section, select **Authorization Code**.

   4. In the **Default Access Token Manager** list, select the token manager that you created in step 3 of [Configuring the OAuth server](pd_da_config_oauth_server.html).

   5. Select the checkbox for **Require Proof Key for Code Exchange (PKCE)**.

   6. In the **OpenID Connect** section, select the OpenID Connect (OIDC) policy that you created in step 5 of [Configuring the OAuth server](pd_da_config_oauth_server.html).

8. Click **Save**.

## Next steps

After completing the previous steps, configure the following settings to display the name of the administrator who is signed on to the client application:

1. Add the `profile` scope and ensure it is available to the OAuth client used for the Delegated Admin application.

2. Add and fulfill the `name` attribute as part of the contract for both the access token and the ID token supplied to the Delegated Admin application.

3. Set the `PROFILE_SCOPE_ENABLED` configuration variable for Delegated Admin in the `config.js` file to `true`.

   ```
   /**
    * Configuration wrapper object for Delegated Admin
    */
   window.PD_DADMIN_CONFIG = {
     /**
      * Set to true if the "profile" scope is supported for the Delegated Admin OIDC client on
      * PingFederate and you wish to use it to show the current user's name in the navigation.
      * DEFAULT: false
      */
     PROFILE_SCOPE_ENABLED: true,
   };
   ```

---

---
title: Configuring delegated administrator rights on the PingDirectory server
description: To delegate users or groups as administrators, use the PingDirectory admin console (Delegated Admin rights and resource rights) or the dsconfig create-delegated-admin-rights and create-delegated-admin-resource-rights commands.
component: pingdirectory
version: 11.1
page_id: pingdirectory:delegated_admin_application_guide:pd_da_config_delegated_admin_rights_pd_server
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/delegated_admin_application_guide/pd_da_config_delegated_admin_rights_pd_server.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 18, 2023
section_ids:
  about-this-task: About this task
  steps: Steps
  example: Example:
  example-2: Example:
  example-3: Example:
---

# Configuring delegated administrator rights on the PingDirectory server

To delegate users or groups as administrators, use the PingDirectory admin console (Delegated Admin rights and resource rights) or the `dsconfig create-delegated-admin-rights` and `create-delegated-admin-resource-rights` commands.

## About this task

To use Delegated Admin, an administrator must possess rights that are designated through the PingDirectory server configuration in addition to valid credentials and an access token that the PingDirectory server can validate.

* Admin Permissions

  * `create`

    The administrator can create new resources of this type.

  * `read`

    The administrator can read resources of this type.

    |   |                                                                                                                                                          |
    | - | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
    |   | The `create`, `delete`, `update`, `update-profile`, `reset-password`, and `manage-group-membership`, `update` permissions require the `read` permission. |

  * `update`

    The administrator can edit resources of this type.

  * `delete`

    The administrator can delete resources of this type.

  * `update-profile`

    The administrator can update user profiles but isn't allowed password- change-related privileges.

    For group and generic type resources, the `update-profile` permission gives the same rights as the `update` permission.

  * `reset-password`

    The administrator can reset passwords without the ability to change other user attributes.

  * `manage-group-membership`

    The administrator can manage the membership of a group resource by adding or removing members. This permission is only applicable to group resource types.

  * `reference`

    The administrator can reference resources when selecting a parent during the creation of another resource. With the reference permission specified, the administrator can use a parent REST resource type without seeing the option to manage the parent resource type. For example, if the parent type for users is Organizational Unit, the administrator can have reference rights to the Organizational Unit resource type only. The administrator can create users without seeing the **Manage Organizational Unit** navigation option.

    The administrator can reference resource types in Delegated Admin attributes. For example, the administrator can select user entries from a list based on their distinguished name (DN) *(tooltip: \<div class="paragraph">
    \<p>A name uniquely identifying an object within the hierarchy of a directory tree.\</p>
    \</div>)* without displaying the actual values of the DNs.

  * `download`

    The administrator can download reports for resources of this type. With this permission, the **Download Report** button shows on the **Reporting** page for the administrator.

  * `upload`

    The administrator can upload a `.csv` file to import resources of this type. With this permission, the **Upload File** button shows on the **Reporting** page for the administrator.

    |   |                                                                                                                                                        |
    | - | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
    |   | For the parent resource type to be available for the creation of new entries under the parent, the `read` or `reference` permission must be specified. |

    To prevent changes that might break the configuration of the app, the app does not allow changes to RDN attributes of a resource entry DN, for resources referenced in the Delegated Admin server configuration. This includes the following configuration elements:

    * `admin-user-DN` and `admin-group-DN` of Admin Rights

    * `resource-subtree` and `resources-in-group` of Admin Resource Rights

      For example, if an Admin Rights configuration contains `admin-group-DN: cn=Admin Group,dc=example,dc=com` and some administrator has rights to modify that particular group through the app, then the `cn` attribute of that group can't be changed without invalidating the configuration. The attribute label has a lock icon and a message indicating that the value can only be changed by a server administrator.

      The example commands that follow illustrate the configuration options for delegated administration and are performed on the PingDirectory server.

      |   |                                                                                                                                                                  |
      | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      |   | Administrators who manage only specific subtrees can't create users in an organization that does not reside under, or at the same level as, one of the subtrees. |

## Steps

* Restrict an administrator to manage users in specified subtrees.

  ### Example:

  ```shell
  $ bin/dsconfig create-delegated-admin-rights \
    --rights-name admin1 \
    --set "admin-user-dn:uid=admin1,ou=people,dc=example,dc=com" \
    --set enabled:true

  $ bin/dsconfig create-delegated-admin-resource-rights \
    --rights-name admin1 \
    --rest-resource-type users \
    --set admin-scope:resources-in-specific-subtrees \
    --set "resource-subtree:ou=org1,dc=example,dc=com" \
    --set admin-permission:create \
    --set admin-permission:read \
    --set admin-permission:update \
    --set admin-permission:delete \
    --set enabled:true
  ```

* Restrict an administrator to managing the member users of one or more specified groups.

  ### Example:

  In the following example, assume the existence of a static or dynamic group entry whose members include the users to be managed.

  ```shell
  $ bin/dsconfig create-delegated-admin-rights \
    --rights-name admin1 \
    --set "admin-user-dn:uid=admin1,ou=people,dc=example,dc=com"
    --set enabled:true
  $ bin/dsconfig create-delegated-admin-resource-rights \
    --rights-name admin1 \
    --rest-resource-type users \
    --set admin-scope:resources-in-specific-groups \
    --set "resources-in-group:cn=User Group,dc=example,dc=com" \
    --set admin-permission:read \
    --set admin-permission:update \
    --set enabled:true
  ```

* Assign the delegated admin rights to a group REST resource type that matches the specified group.

  For more information, see [Manage groups](pd_da_manage_groups.html).

* Rather than delegate a single user as an administrator, delegate an entire group of users as administrators.

  For more information about the PingDirectory server administrators and configuring dynamic and static groups, see the PingDirectory Server Administration Guide.

  ### Example:

  In this example, groups can be configured to manage specific subtrees or groups with the `resources-in-specific-subtrees` or `resources-in-group` setting for the `admin-scope`.

  ```shell
  $ bin/dsconfig create-delegated-admin-rights \
    --rights-name admin-group1 \
    --set "admin-group-dn:cn=Admin Group,ou=people,dc=example,dc=com"
    --set enabled:true

  $ bin/dsconfig create-delegated-admin-resource-rights \
    --rights-name admin-group1 \
    --rest-resource-type users \
    --set admin-scope:all-resources-in-base \
    --set admin-permission:create \
    --set admin-permission:read \
    --set admin-permission:update \
    --set admin-permission:delete \
    --set enabled:true
  ```

---

---
title: Configuring other OIDC identity providers
description: Learn how to configure an OIDC provider as the identity provider for Delegated Admin.
component: pingdirectory
version: 11.1
page_id: pingdirectory:delegated_admin_application_guide:pd_da_config_oidc_idp
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/delegated_admin_application_guide/pd_da_config_oidc_idp.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  steps: Steps
  next-steps: Next steps
---

# Configuring other OIDC identity providers

Complete the following steps to configure a non-PingFederate OpenID Connect (OIDC) *(tooltip: \<div class="paragraph">
\<p>An authentication protocol built on top of OAuth that authenticates users and enables clients (relying parties) of all types to request and receive information about authenticated sessions and users. OIDC is extensible, allowing clients to use optional features such as encryption of identity data, discovery of OpenID Providers (OAuth authorization servers), and session management.\</p>
\</div>)* provider as the identity provider for Delegated Admin.

## Steps

1. Create an OIDC client and specify the following values:

   * **Redirect URI**: http\://*\<hostname:port>*/delegator/

     This is the server that hosts the Delegated Admin web application. Your OIDC client might also call this value **Redirect URL**, **Callback URI**, or **Callback URL**.

   * **Scopes**: urn:pingidentity:directory-delegated-admin

   * **Grant type**: Authorization code

   * **PKCE enforcement**: Required

   * **Token endpoint authentication method**: None

2. Make a note of the following OIDC client values, which are required to install Delegated Admin:

   * **Client ID**

   * **OIDC authority URL**

     This value represents the base URL of the OIDC client's Discovery endpoint. Your OIDC provider might use a different name for this URL.

## Next steps

After installing Delegated Admin, configure [PingDirectory to use the OIDC provider as the identity provider](pd_da_config_oidc_pd.html).

---

---
title: Configuring PingDirectory to use an OIDC identity provider
description: Learn how to configure PingDirectory to use the OIDC provider as the identity provider for Delegated Admin.
component: pingdirectory
version: 11.1
page_id: pingdirectory:delegated_admin_application_guide:pd_da_config_oidc_pd
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/delegated_admin_application_guide/pd_da_config_oidc_pd.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  steps: Steps
---

# Configuring PingDirectory to use an OIDC identity provider

To configure PingDirectory to use a non-PingFederate OpenID Connect (OIDC) *(tooltip: \<div class="paragraph">
\<p>An authentication protocol built on top of OAuth that authenticates users and enables clients (relying parties) of all types to request and receive information about authenticated sessions and users. OIDC is extensible, allowing clients to use optional features such as encryption of identity data, discovery of OpenID Providers (OAuth authorization servers), and session management.\</p>
\</div>)* provider as the identity provider for Delegated Admin, you must do the following:

1. Add any new attributes to be mapped from the OIDC provider to the PingDirectory schema and the appropriate user entries.

2. Create an identity mapper that maps OIDC users to PingDirectory entries.

3. Create an access token validator that uses the identity mapper to match claims in the access token to PingDirectory entry attributes. Learn more in [Handling signed tokens](../managing_access_control/pd_ds_handle_signed_tokens.html).

The following steps provide a sample configuration for completing these tasks. The configuration assumes that:

* You create an `externalIDPID` attribute in the PingDirectory schema and add it to user entries.

  * The attribute contains the unique ID for the PingDirectory user in the OIDC provider.

* The OIDC provider generates a JSON Web Token (JWT) *(tooltip: \<div class="paragraph">
  \<p>An IETF standard container format for a JSON object used for the secure exchange of content, such as identity or entitlement information. You can find the industry standard in \<a href="https\://datatracker.ietf.org/doc/html/rfc7519">RFC 7519\</a>.\</p>
  \</div>)* with a `sub` claim.

* The `sub` claim gets mapped to the `externalIDPID` attribute in the PingDirectory user entry.

|   |                                                                              |
| - | ---------------------------------------------------------------------------- |
|   | Update any values to match your environment and OIDC provider configuration. |

## Steps

1. Import the following LDIF file to create an auxiliary object class named `externalIDPUser` with the `externalIDPID` attribute:

   ```ldif
   objectClass: top
   objectClass: ldapSubentry
   objectClass: subschema
   cn: schema
   attributeTypes: ( externalIDPID-OID NAME 'externalIDPID' USAGE userApplications X-SCHEMA-FILE '99-user.ldif' )
   objectClasses: ( externalIDPUser-OID NAME 'externalIDPUser' AUXILIARY MUST externalIDPID X-SCHEMA-FILE '99-user.ldif' )
   ```

2. Add the `externalIDPUser` object class and `externalIDPID` attribute to any Delegated Admin user entries. The attribute value should be the ID of the user on the OIDC provider.

   ```
   bin/ldapmodify <<+
   dn: uid=externalIDPUser,ou=People,dc=example,dc=com
   changetype: modify
   add: objectClass
   objectClass: externalIDPUser
   -
   add: externalIDPID
   externalIDPID: 078ec98d-9dc2-4cc3-9a7e-db0e65d75fe6
   +
   ```

3. Create an identity mapper that matches users based on the `externalIDPID` attribute:

   ```
   dsconfig create-identity-mapper \
     --mapper-name "External IDP User Mapper" \
     --type exact-match \
     --set "description:Used to match the identifier to the externalIDPID attribute" \
     --set enabled:true \
     --set match-attribute:externalIDPID
   ```

4. Create an HTTP external server for the OIDC provider. Replace *\<OIDC-authority-URL>* with the base URL of the OIDC client's Discovery endpoint.

   ```
   dsconfig create-external-server \
     --server-name "External IDP HTTP Server" \
     --type http \
     --set base-url:<OIDC-authority-URL>
   ```

5. Create a JWT access token validator using the identity mapper and external server created in the previous steps. Replace *\<IdP-JWKS-endpoint>* with the URL of the JSON Web Key Set (JWKS) endpoint for the OIDC client.

   ```
   dsconfig create-access-token-validator \
     --validator-name "External IDP Access Token Validator" \
     --type jwt \
     --set "identity-mapper:External IDP User Mapper" \
     --set enabled:true \
     --set "authorization-server:External IDP HTTP Server" \
     --set jwks-endpoint-path:<IdP-JWKS-endpoint>
   ```

---

---
title: Configuring PingFederate as the identity provider
description: The following task configures the PingFederate server as the identity provider (IdP) for the PingDirectory server.
component: pingdirectory
version: 11.1
page_id: pingdirectory:delegated_admin_application_guide:pd_da_config_pf_as_idp
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/delegated_admin_application_guide/pd_da_config_pf_as_idp.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 20, 2024
section_ids:
  before-you-begin: Before you begin
  steps: Steps
---

# Configuring PingFederate as the identity provider

The following task configures the PingFederate server as the identity provider (IdP) *(tooltip: \<div class="paragraph">
\<p>A service that manages identity information and provides authentication services to relying clients or SPs within a federated or distributed network.\</p>
\</div>)* for the PingDirectory server.

## Before you begin

Download the LDAPS certificate from the PingDirectory server. For more information, see [Exporting certificates](../managing_servers_and_certificates/pd_ds_export_certificates.html).

## Steps

1. Sign on to the PingFederate admin console.

2. Import the PingDirectory server LDAPS certificate:

   1. Go to **Security → Certificate & Key Management → Trusted CAs**.

   2. Click **Import**, click **Choose File** to browse to the certificate, click **Next**, and then click **Save**.

3. Add an Lightweight Directory Access Protocol (LDAP) *(tooltip: \<div class="paragraph">
   \<p>An open, cross platform protocol used for interacting with directory services.\</p>
   \</div>)* datastore:

   1. Go to **System → Data Stores**.

   2. Click **Add New Data Store**.

   3. Specify a **Name** for the datastore.

   4. Set **Type** to **Directory (LDAP)**.

   5. Click **Next**.

   6. In the **Hostname(s)** field, enter the PingDirectory server host name and LDAPS port, separated by a colon (for example, 10.101.113.75:1636) and click **Add**.

   7. Select the **Use LDAPS** checkbox.

   8. Set **LDAP Type** to PingDirectory.

   9. In the **User DN** field, enter one of the following values based on your PingDirectory configuration:

      * `cn=dmanager`

      * `cn=Directory Manager`

        |   |                                                                                                  |
        | - | ------------------------------------------------------------------------------------------------ |
        |   | These values are based on the assumption that Delegated Admin will run as the directory manager. |

   10. In the **Password** field, specify the root password.

   11. Click **Advanced** and then **Advanced LDAP Options**.

       1. Select the **Create New Connections If Necessary** checkbox.

       2. Clear the **Verify LDAPS Hostname** checkbox.

       3. Click **Done**.

   12. Click **Test Connection**.

   13. Click **Next**.

   14. Click **Save**.

4. Create the HTML form IdP Adapter.

   The adapter authenticates users against the PingDirectory server.

   1. Go to **Authentication → IdP Adapters → Create New Instance**

   2. In the **Instance Name** field, enter a name such as `PingDirectoryIdP`.

   3. Specify an **Instance ID**.

   4. Set **Type** to **HTML Form IdP Adapter**.

   5. Click **Next**.

   6. Go to the bottom of the page and click **Manage Password Credential Validators**.

   7. Create a validator to authenticate users against the PingDirectory server:

      1. Click **Create New Instance**.

      2. Specify an **Instance Name**.

      3. Specify an **Instance ID**.

      4. Set **Type** to **LDAP User Name Password Credential Validator**.

      5. Click **Next**.

      6. Specify an **LDAP Datastore**.

      7. Specify an **Search Base**.

      8. Enter the following text in the **Search Filter** field to use the email address or username to sign on to the system.

         `(|(uid=${username})(mail=${username}))`

      9. Click **Next** and extend the contract with `entryUUID` and `cn`.

         |   |                              |
         | - | ---------------------------- |
         |   | These values are used later. |

      10. Click **Next**, **Done**, or **Save** until you reach the **Create Adapter Instance** screen.

   8. Add a new row to **Password Credential Validators**, choose the new LDAP Password Credential Validator, and click **Update**.

   9. Go to the **Extended Contract** tab and extend the adapter contract with `entryUUID` and `cn`.

   10. Go to the **Adapter Attributes** tab, select `entryUUID` for a pseudonym, and then click **Next**, **Next**, **Done**, and **Save**.

       Learn more about [Configuring the LDAP Username Password Credential Validator](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_configure_ldap_username_pcv.html) in the PingFederate documentation.

5. Enable session tracking:

   1. Go to **Authentication → Sessions**

   2. Select the **Track Adapter Sessions For Logout** checkbox.

   3. Select the **Track Revoked Sessions On Logout** checkbox.

   4. Select the **Enable Authentication Sessions For All Sources** checkbox.

   5. Click **Save**.

---

---
title: Configuring the OAuth server
description: The following task configures the PingFederate server for OAuth and OpenID Connect (OIDC) authentication.
component: pingdirectory
version: 11.1
page_id: pingdirectory:delegated_admin_application_guide:pd_da_config_oauth_server
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/delegated_admin_application_guide/pd_da_config_oauth_server.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: October 3, 2023
section_ids:
  steps: Steps
  choose-from: Choose from:
---

# Configuring the OAuth server

The following task configures the PingFederate server for OAuth and OpenID Connect (OIDC) *(tooltip: \<div class="paragraph">
\<p>An authentication protocol built on top of OAuth that authenticates users and enables clients (relying parties) of all types to request and receive information about authenticated sessions and users. OIDC is extensible, allowing clients to use optional features such as encryption of identity data, discovery of OpenID Providers (OAuth authorization servers), and session management.\</p>
\</div>)* authentication.

## Steps

1. Sign on to the PingFederate admin console.

2. Set the identity provider (IdP) *(tooltip: \<div class="paragraph">
   \<p>A service that manages identity information and provides authentication services to relying clients or SPs within a federated or distributed network.\</p>
   \</div>)* adapter mapping:

   1. Go to **Authentication > OAuth > IdP Adapter Grant Mapping**.

   2. From the **Source Adapter Instance** list, select the IdP adapter you created in [Configuring PingFederate as the identity provider](pd_da_config_pf_as_idp.html) and click **Add Mapping**.

   3. Click **Next**.

      |   |                                |
      | - | ------------------------------ |
      |   | No attribute source is needed. |

   4. On the **Contract Fulfillment** tab, set the contracts as shown in the following table:

      | Contract       | Source      | Value         |
      | -------------- | ----------- | ------------- |
      | **USER\_KEY**  | **Adapter** | **entryUUID** |
      | **USER\_NAME** | **Adapter** | **cn**        |

   5. Click **Next** and then click **Next** again.

   6. Click **Save**.

3. Set up Access Token Management.

   Select an existing instance or click **Applications > OAuth > Access Token Management > Create New Instance**.

   ### Choose from:

   * If selecting an existing instance, click the **Instance Configuration** tab.

     |   |                                                                                                                                                                                                                                                                                                                                                                                                        |
     | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
     |   | With an existing instance, a JSON Web Token (JWT) *(tooltip: \<div class="paragraph">&#xA;\<p>An IETF standard container format for a JSON object used for the secure exchange of content, such as identity or entitlement information. You can find the industry standard in \<a href="https\://datatracker.ietf.org/doc/html/rfc7519">RFC 7519\</a>.\</p>&#xA;\</div>)* is configured automatically. |

   * If creating a new instance, specify the required fields and set **Type** to **JSON Web Tokens**.

     |   |                                                                          |
     | - | ------------------------------------------------------------------------ |
     |   | Take note of your new instance name. You'll need that information later. |

     1. Use symmetric encryption for the JWT by adding a row in the **Symmetric Keys** section using 32 bytes or 64 characters of hex.

        |   |                                                                                                                                                                                         |
        | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
        |   | This encryption only requires a symmetric key, not a certificate and private key. This step requires the client to validate the token by hitting the validation endpoint on the server. |

     2. Set **JWS Algorithm** to **HMAC Using SHA-256**.

     3. Set **Active Symmetric Key ID** to your symmetric key and click **Next**.

     4. On the **Session Validation** tab, select all options and click **Next**.

     5. On the **Access Token Attribute Contract** tab, list at least one attribute to be defined in the access token, add `sub`, click **Next** until you reach the last section, and then click **Save**.

4. Set up access token mapping:

   1. Go to **Applications > OAuth > Access Token Mappings**.

   2. Set **Context** to **Default**, set **Access Token Manager** to the access token manager you created in the last step, and click **Add Mapping**.

   3. Click **Next** in the **Attribute Source & User Lookup** section to go to the **Contract Fulfillment** section.

   4. In the **sub** row, make the following selections:

      * In the **Source** list, select **Persistent Grant**.

      * In the **Value** list, select **USER\_KEY**.

   5. Click **Next** until you reach the **Summary** section. Click **Save**.

5. Set up the OpenID Connect policy:

   1. Go to **Applications > OAuth > OpenID Connect Policy Management**.

   2. Click **Add Policy**.

   3. Specify a **Policy ID**.

   4. Specify a **Name**.

   5. Choose the previously created access token manager and click **Next**.

   6. Delete all extended contract attributes except `sub`.

      Other scopes are defined, if configured.

   7. Click **Next** to reach the **Contract Fulfillment** section.

   8. Fulfill the OpenID Connect (OIDC) contract **sub** with the access token attribute `sub`.

   9. Click **Next** and then click **Done**.

   10. If a default OIDC policy is not already defined, set this new policy as the default and click **Save**.

6. Add scopes for PingDirectory server APIs:

   1. Go to **System > OAuth Settings > Scope Management**.

   2. Click the **Exclusive Scopes** tab.

   3. Add a scope with a **Scope Value** of `urn:pingidentity:directory-delegated-admin` and a **Scope Description** of `DAScope`.

   4. Click **Save**.

---

---
title: Configuring the PingDirectory server as the token validator (create OAuth client for PingDirectory)
description: When creating a PingFederate access token validator in the PingDirectory server, use the pingdirectory client ID and secret.
component: pingdirectory
version: 11.1
page_id: pingdirectory:delegated_admin_application_guide:pd_da_config_pd_server_token_validator
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/delegated_admin_application_guide/pd_da_config_pd_server_token_validator.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: October 3, 2023
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Configuring the PingDirectory server as the token validator (create OAuth client for PingDirectory)

When creating a PingFederate access token validator in the PingDirectory server, use the `pingdirectory` client ID and secret.

## About this task

The PingDirectory server uses an identity mapper to match the `sub` claim against the `entryUUID` attribute.

To configure the PingDirectory server as the token validator:

## Steps

1. Sign on to the PingFederate admin console.

2. Go to **Applications → OAuth → Clients**.

3. Click **Add Client**.

4. For both the **Client ID** and **Name**, specify `pingdirectory`.

5. In the **Client Authentication** section, select **Client Secret**.

6. In the **Client Secret** section, select **Change Secret** and then enter or generate a secret.

7. Copy the secret key.

8. In the **Allowed Grant Types** section, select **Access Token Validation (Client is a Resource Server)**.

9. Set the **Default Access Token Manager** to the access token manager you created in step 3 of [Configuring the OAuth server](pd_da_config_oauth_server.html).

10. Click **Save**.

---

---
title: Configuring the PingFederate server
description: PingFederate offers many configuration options. This section provides an example PingFederate 10.1 configuration that supports Delegated Admin.
component: pingdirectory
version: 11.1
page_id: pingdirectory:delegated_admin_application_guide:pd_da_config_pf_server
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/delegated_admin_application_guide/pd_da_config_pf_server.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 13, 2023
---

# Configuring the PingFederate server

PingFederate offers many configuration options. This section provides an example PingFederate 10.1 configuration that supports Delegated Admin.

|   |                                                                                                                                                                                                                                             |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | We deprecated support for the Implicit grant type and will remove it in a future release. Use the Authorization Code with PKCE grant type instead. Learn more in [Changing the default OIDC grant type](pd_da_change_oidc_grant_type.html). |

Configuring the PingFederate server includes the following:

* [Configuring PingFederate as the identity provider](pd_da_config_pf_as_idp.html)

* [Configuring the OAuth server](pd_da_config_oauth_server.html)

* [Configuring the PingDirectory server as the token validator (create OAuth client for PingDirectory)](pd_da_config_pd_server_token_validator.html)

* [Configuring Delegated Admin as a new client (create OAuth client for Delegated Admin)](pd_da_config_delegated_admin_new_client.html)

* [Setting cross-origin resource sharing (CORS) settings](pd_da_set_cors_settings.html)

---

---
title: Configuring the session timeout
description: By default, Delegated Admin has an idle session timeout value of 30 minutes. To adjust this value, perform the following steps.
component: pingdirectory
version: 11.1
page_id: pingdirectory:delegated_admin_application_guide:pd_da_config_session_timeout
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/delegated_admin_application_guide/pd_da_config_session_timeout.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: October 5, 2023
section_ids:
  steps: Steps
---

# Configuring the session timeout

By default, Delegated Admin has an idle session timeout value of 30 minutes. To adjust this value, perform the following steps.

## Steps

1. Open the `config.js` configuration file in a text editor.

2. Add the following line to the configuration file:

   ```
   window.TIMEOUT_LENGTH_MINS=<TimeoutValue>;
   ```

   *\<TimeoutValue>* is an integer that represents the session timeout value in minutes.

   To view an example outline that features this setting, see `example.config.js`.

3. Save your changes to `config.js`.

---

---
title: Configuring user self-service
description: The PingFederate server provides end users with the ability to self-service their own profiles.
component: pingdirectory
version: 11.1
page_id: pingdirectory:delegated_admin_application_guide:pd_da_config_user_self_service
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/delegated_admin_application_guide/pd_da_config_user_self_service.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: March 14, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
  example: Example:
  result: Result:
  example-2: Example:
---

# Configuring user self-service

The PingFederate server provides end users with the ability to self-service their own profiles.

## About this task

To enable users created by delegated administrators to manage their own profiles through the PingFederate local identity profile-management feature, you need to perform additional configuration steps in both PingDirectory and PingFederate.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Import the PingFederate LDAP Data Interchange Format (LDIF) *(tooltip: \<div class="paragraph">&#xA;\<p>An IETF standard file format for representing LDAP directory content and modifications to directory content. Typically used to import and export LDAP-based directory information.\</p>&#xA;\</div>)* first in PingDirectoryProxy and then in PingDirectory. Constructed attributes need to be created only in PingDirectoryProxy. Creating and rebuilding indexes (part of the self-service configuration) is done on PingDirectory. |

## Steps

1. Configure PingFederate for profile management.

   To allow users to change their passwords, enable **Allow Password Changes** in the HTML Form Adapter. You must make this change if you want to create passwords that the user must change on the first use. For example PingFederate configuration steps, see [Customer IAM configuration](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_customer_iam_config.html) in the PingFederate documentation.

   [Setting up PingDirectory for customer identities](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_setting_up_pd_for_customer_identit.html) in the PingFederate documentation includes some of the following required steps on the PingDirectory server.

2. To create passwords that the user must change on the first use after account creation or a password reset, configure a PingDirectory password policy to force users to change their passwords.

   ### Example:

   This policy requires that you enable **Allow Password Change**s as mentioned above.

   ```
   dsconfig set-password-policy-prop --policy-name "Default Password Policy" \
   --set force-change-on-add:true --set force-change-on-reset:true
   ```

   ### Result:

   With these changes, when a user signs on to the PingFederate self-service page, the page prompts the user to change their password.

3. Import the required additional Lightweight Directory Access Protocol (LDAP) *(tooltip: \<div class="paragraph">
   \<p>An open, cross platform protocol used for interacting with directory services.\</p>
   \</div>)* schema provided by PingFederate into PingDirectory.

   1. On the PingFederate server, copy the LDIF file `local-identity-pingdirectory.ldif` from the following location: `<pf_install>/pingfederate/server/default/conf/local-identity/ldif-scripts/local-identity-pingdirectory.ldif`.

   2. Use the `scopy` command to securely copy the LDIF file to your local machine.

4. Update the LDAP schema.

   1. Sign on to the PingDirectory admin console.

   2. Go to **LDAP Schema → Schema Utilities**.

   3. Click **Import Schema Element**.

   4. Copy the schema changes from the file `<pf_install>/pingfederate/server/default/conf/local-identity/ldif-scripts/local-identity-pingdirectory.ldif`.

   5. Paste the schema changes into the text area.

   6. Click **Import**.

5. Create an equality index for the pf-connected-identity attribute.

   ```shell
   $ bin/dsconfig create-local-db-index \
     --backend-name userRoot \
     --index-name pf-connected-identity \
     --set index-type:equality
   ```

6. After adding the index, use the rebuild-index utility to build the indexes.

   ### Example:

   The following sample builds the required index.

   ```shell
   $ bin/rebuild-index \
     --baseDN "dc=example,dc=com" \
     --index pf-connected-identity
   ```

7. Configure PingDirectory Server Composed Attributes.

   In previous versions of Delegated Admin, the remaining configuration was achieved by setting a constructed attribute on the user REST resource type. In the latest version, composed attribute plugins should be used instead as they provide the following advantages:

   * The populate-composed-attribute-values tool can be used to enable self-service for any existing users.

   * Self-service is enabled for any users not created through the Delegated Admin app.

     Configure two Composed Attribute Plugins as follows:

     |   |                                                                                                                                                                                                                                                                                                                     |
     | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
     |   | *\<users-base-dn>* and *\<users-object-class>* must be replaced with the search base distinguished name (DN) *(tooltip: \<div class="paragraph">&#xA;\<p>A name uniquely identifying an object within the hierarchy of a directory tree.\</p>&#xA;\</div>)* and structural object class of your REST Resource Type. |

     ```shell
     $ bin/dsconfig create-plugin \
       --plugin-name pf-connected-identities \
       --type composed-attribute \
       --set enabled:true \
       --set attribute-type:objectClass \
       --set value-pattern:pf-connected-identities \
       --set target-attribute-exists-during-initial-population-behavior:merge-existing-and-composed-values \
       --set "include-base-dn:<users-base-dn>" \
       --set "include-filter:(objectClass=<users-object-class>)"

     $ bin/dsconfig create-plugin \
       --plugin-name pf-connected-identity \
       --type composed-attribute \
       --set enabled:true \
       --set attribute-type:pf-connected-identity \
       --set "value-pattern:auth-source=pf-local-identity:user-id={entryUUID}" \
       --set "include-base-dn:<users-base-dn>" \
       --set "include-filter:(objectClass=<users-object-class>)"
     ```

     If you configure composed attribute plugins as described after upgrading an existing deployment, then you should remove the old constructed attribute configuration as follows.

     ```shell
     $ bin/dsconfig set-rest-resource-type-prop --type-name users \
       --remove auxiliary-ldap-objectclass:pf-connected-identities \
       --remove post-create-constructed-attribute:pf-connected-identity \
       --remove update-constructed-attribute:pf-connected-identity
     ```

8. (Optional) Enable self-service for any existing users not already linked to PingFederate.

   ```shell
   $ bin/populate-composed-attribute-values -h  <host>  -p  <port>  -D "cn=Directory Manager" -w  <password>
   ```

---

---
title: Creating a group
description: You can add users as members to groups that delegated administrators create and manage. You can also add subgroups as members to a group.
component: pingdirectory
version: 11.1
page_id: pingdirectory:delegated_admin_application_guide:pd_da_create_group
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/delegated_admin_application_guide/pd_da_create_group.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: October 5, 2023
---

# Creating a group

You can add users as members to groups that delegated administrators create and manage. You can also add subgroups as members to a group.

The configuration for each delegated group type consists of the following elements:

* Group REST resource type

  Defines the attributes to locate groups in the directory information tree (DIT).

* Parent DN or Parent resource type

  Specifies the location in which to create groups in the DIT.

  * To specify a parent distinguished name (DN) *(tooltip: \<div class="paragraph">
    \<p>A name uniquely identifying an object within the hierarchy of a directory tree.\</p>
    \</div>)* for a resource type, enter the value in the **Parent DN** text box in the **Resource Creation** section. The parent DN is often identical to the search base DN, such as `ou=customers,ou=Groups, dc=example,dc=com`.

  * To specify a parent resource type, select a value from the **Parent Resource Type** list in the **Resource Creation** section. Delegated administrators are subsequently presented with a list box that lets them select a resource, and the group is created under the selected parent resource. If you specify a parent resource type, set a value for the **Primary Display Attribute Type** in the **Delegated Admin** section. This setting determines the values that are displayed in the Delegated Admin GUI. For example, a primary display attribute type of `ou` displays the `ou` value in the list box for each resource within the parent resource type.

* Attributes

  These attributes are presented to the delegated administrators.

To configure a group REST resource type, go to **Configuration > REST Resource Types** page in the PingDirectory admin console.

When creating or editing a REST resource type, the **Search Base DN** field in the **General Configuration** section determines the data structure that is searched in Delegated Admin, and the **Display Name** field in the **Delegated Admin** section specifies the label of the REST resource in the Delegated Admin GUI.

**PingDirectory Attributes**

| PingDirectory admin console |                                                                                                                                                                                   | Delegated Admin GUI                                                                    |
| --------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| UI field                    | Window and section                                                                                                                                                                | UI field onNew Group page                                                              |
| `Display Name`              | **Configuration > REST Resource Types**. Create or edit a REST resource type, and then go to the **Delegated Admin** section.                                                     | `Select a Type` label                                                                  |
| `REST Resource Type`        | **Configuration > Delegated Admin Rights**. Create or edit Delegated Admin rights, and then click **New Delegated Admin Resource Rights**.                                        | `Select a Type` option                                                                 |
| `Parent Resource Type`      | **Configuration > REST Resource Types**. Create or edit a REST resource type, and then go to the **Resource Creation** section.                                                   | Display name for parent resource type                                                  |
| `Display Name`              | **Configuration > REST Resource Types**. Create or edit a REST resource type, and then go to the **Delegated Admin Attributes** section. Click **New Delegated Admin Attribute**. | Additional fields such as `CN`, `Description`, `Business Category`, and `Organization` |