---
title: Adding PingOne as an authentication provider in Code42
description: To allow PingOne to coordinate authentication with Code42, upload your SAML metadata.
component: code42-pingone
page_id: code42-pingone:single_sign-on_setup:p1_code42_integration_adding_p1_as_an_authentication_provider_in_code42
canonical_url: https://docs.pingidentity.com/integrations/code42-pingone/single_sign-on_setup/p1_code42_integration_adding_p1_as_an_authentication_provider_in_code42.html
llms_txt: https://docs.pingidentity.com/integrations/code42-pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 26, 2024
section_ids:
  steps: Steps
---

# Adding PingOne as an authentication provider in Code42

To allow PingOne to coordinate authentication with Code42, upload your SAML metadata.

## Steps

1. Sign on to Code42 as an administrator.

2. Navigate to **Integrations > Identity Management**.

3. On the **Authentication** tab, click **Add authentication provider**.

4. On the **Add authentication provider** dialog, enter a name and select **Upload file**. Select the `saml2-metadata-idp-***.xml` file that you downloaded in [Creating an SSO connection in PingOne](p1_code42_integration_creating_an_sso_connection_in_p1.html). Click **Create provider**.

5. In the **Attribute mapping** section, click the pencil icon.

6. Clear the **Use default mapping** checkbox.

7. In the **Username** field, enter `mail`.

   ![A screenshot that shows the Username attribute mapped to mail.](_images/npf1627424023450.jpg)

8. Click **Save**.

9. Go to **Environment > Organizations**.

10. Add a new organization, or select an existing one.

11. In the organization details, on the **Settings** list, select **Edit**.

    ![A screenshot that shows the Settings menu with Edit highlighted.](_images/qgd1627424715354.jpg)

12. On the **Security** tab, in the **Servers** section, clear the **Inherit security settings from parent** checkbox.

13. On the **Select an authentication method** list, select **SSO**, then select the authentication provider you added.

14. On the **Select a directory service** list, select **Local** for testing purposes.

15. Click **Save**.

16. If you see a prompt to enable single sign-on, enter `ENABLE`, then click **Enable**.

---

---
title: Adding PingOne as SCIM provider in Code42
description: To get your base URL and credentials to access Code42 API, add PingOne as a SCIM provider.
component: code42-pingone
page_id: code42-pingone:provisioning_setup:p1_code42_integration_adding_p1_as_scim_provider_in_code42
canonical_url: https://docs.pingidentity.com/integrations/code42-pingone/provisioning_setup/p1_code42_integration_adding_p1_as_scim_provider_in_code42.html
llms_txt: https://docs.pingidentity.com/integrations/code42-pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 26, 2024
section_ids:
  steps: Steps
---

# Adding PingOne as SCIM provider in Code42

To get your base URL and credentials to access Code42 API, add PingOne as a SCIM provider.

## Steps

1. Sign on to Code42 as an administrator.

2. Navigate to **Integrations > Identity Management**.

3. On the **Provisioning** tab, click **Add provisioning provider**, and then click **Add SCIM provider**.

4. On the **Add SCIM provisioning** dialog, enter a name and select the **OAuth token** credential type. Click **Next**.

5. On the **SCIM Provider Created** dialog, note the **Base URL** and **Token** values. You will use these in [Creating a provisioning connection in PingOne](p1_code42_integration_creating_a_provisioning_connection_in_p1.html). Click **Done**.

---

---
title: Code42 Integration Guide for PingOne
description: You can integrate PingOne with Code42 for user provisioning and single sign-on (SSO).
component: code42-pingone
page_id: code42-pingone::p1_code42_integration
canonical_url: https://docs.pingidentity.com/integrations/code42-pingone/p1_code42_integration.html
llms_txt: https://docs.pingidentity.com/integrations/code42-pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 26, 2024
section_ids:
  features: Features
  intended-audience: Intended audience
---

# Code42 Integration Guide for PingOne

You can integrate PingOne with Code42 for user provisioning and single sign-on (SSO).

## Features

* Manages users in Code42 based on changes in the PingOne identity store.

  * Creates, updates, and disables users.

* Enables browser-based single sign-on initiated by the identity provider (IdP).

## Intended audience

This document is intended for PingOne administrators.

If you need help during the setup process, see the following resources:

* The following sections of the PingOne documentation:

  * [Provisioning](https://docs.pingidentity.com/pingone/integrations/p1_provisioning.html)

  * [Creating a SCIM connection](https://docs.pingidentity.com/pingone/integrations/p1_create_scim_connection.html)

  * [Adding an application](https://docs.pingidentity.com/pingone/applications/p1_applications_add_applications.html)

  * [Adding a user](https://docs.pingidentity.com/pingone/directory/p1_adduser.html)

* The following sections of the Code42 documentation:

  * [Identity management](https://support.code42.com/Administrator/Cloud/Configuring/Identity_management)

  * [Identity management reference](https://support.code42.com/Administrator/Cloud/Code42_console_reference/Identity_management_reference#Authentication)

  * [Introduction to SCIM provisioning](https://support.code42.com/Administrator/Cloud/Configuring/Introduction_to_SCIM_provisioning)

  * [How to configure SCIM provisioning](https://support.code42.com/Administrator/Cloud/Configuring/Introduction_to_SCIM_provisioning/How_to_configure_provisioning)

  * [Add authentication provider](https://support.code42.com/Administrator/Cloud/Code42_console_reference/Identity_management_reference#Add_authentication_provider)

---

---
title: Configuring a user filter on the provisioning rule
description: Complete the following procedures in order:
component: code42-pingone
page_id: code42-pingone:provisioning_setup:p1_code42_integration_configuring_a_user_filter_on_the_provisioning_rule
canonical_url: https://docs.pingidentity.com/integrations/code42-pingone/provisioning_setup/p1_code42_integration_configuring_a_user_filter_on_the_provisioning_rule.html
llms_txt: https://docs.pingidentity.com/integrations/code42-pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 26, 2024
section_ids:
  before-you-begin: Before you begin
  about-this-task: About this task
  steps: Steps
---

# Configuring a user filter on the provisioning rule

## Before you begin

Complete the following procedures in order:

1. [Creating a provisioning connection in PingOne](p1_code42_integration_creating_a_provisioning_connection_in_p1.html)

2. [Creating a provisioning rule in PingOne](p1_code42_integration_creating_a_provisioning_rule.html)

## About this task

Configure a user filter on the provisioning rule that you created in the [Creating a provisioning rule in PingOne](p1_code42_integration_creating_a_provisioning_rule.html) procedure to specify which PingOne user populations to provision to Code42:

## Steps

1. On the **Configuration** tab of the provisioning rule, click **User Filter**.

2. Click the **Pencil** icon to edit the filter.

3. Define the filter that determines which identities to provision to Code42.

   For more information, see [Adding a user filter](https://docs.pingidentity.com/pingone/integrations/p1_add_provisioning_filter.html) and [Example user filters](https://docs.pingidentity.com/pingone/integrations/p1_example_provisioning_filters.html).

   1. Enter the first condition:

      * All

        Select **All** or **Any** to determine how to evaluate the linked conditions. **All** functions as the boolean logical operator `AND`.

      * Any

        Select **All** or **Any** to determine how to evaluate the linked conditions. **Any** functions as the boolean logical operator `OR`.

      * Attribute

        The user attribute to filter by.

        |   |                                        |
        | - | -------------------------------------- |
        |   | Use the **Population Name** attribute. |

      * Operator

        The operator determines the context of the attribute and its value.

        |   |                                                     |
        | - | --------------------------------------------------- |
        |   | Equals is the only operator supported at this time. |

      * Value

        Enter an appropriate value for the specified attribute.

        |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
        | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
        |   | * For outbound provisioning rules, you must specify either a population or a group to define the users to be provisioned.

        * If you select a group in the filter, then updating or deleting the group can cause the provisioning rule to re-sync.

        * If you select a group in the filter, the filter includes all users with any kind of membership in the group, whether direct, dynamic membership based on a user filter, or inherited from parent groups. For more information, see [Groups](https://docs.pingidentity.com/pingone/directory/p1_groups.html). |

   2. Click **[icon: plus, set=fa]Add** to add more conditions or condition sets until you've specified all the PingOne user populations that you want to provision to Code42.

4. Click **Save**.

---

---
title: Configuring attribute mapping on the provisioning rule
description: Complete the following procedures in order:
component: code42-pingone
page_id: code42-pingone:provisioning_setup:p1_code42_integration_configuring_attribute_mapping_on_the_provisioning_rule
canonical_url: https://docs.pingidentity.com/integrations/code42-pingone/provisioning_setup/p1_code42_integration_configuring_attribute_mapping_on_the_provisioning_rule.html
llms_txt: https://docs.pingidentity.com/integrations/code42-pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 26, 2024
section_ids:
  before-you-begin: Before you begin
  about-this-task: About this task
  steps: Steps
---

# Configuring attribute mapping on the provisioning rule

## Before you begin

Complete the following procedures in order:

1. [Creating a provisioning connection in PingOne](p1_code42_integration_creating_a_provisioning_connection_in_p1.html)

2. [Creating a provisioning rule in PingOne](p1_code42_integration_creating_a_provisioning_rule.html)

## About this task

Configure attribute mapping on the provisioning rule that you created in the [Creating a provisioning rule in PingOne](p1_code42_integration_creating_a_provisioning_rule.html) procedure to map the PingOne user attributes from the SCIM attributes in the Code42 identity store. For outbound provisioning, the mapping is applied to the attribute coming from the PingOne directory before it is saved to the target identity store.

To configure attribute mapping:

## Steps

1. On the **Configuration** tab of the provisioning rule, click **Attribute Mapping**.

2. Click the **Pencil** icon to edit the mapping and confirm that the following default attributes are within the mapping.

   > **Collapse: Default Code42 SCIM attributes**
   >
   > | Code42 SCIM Attribute | PingOne PingOneUser Attribute |
   > | --------------------- | ----------------------------- |
   > | `userName`            | `Username`                    |
   > | `givenName`           | `Given Name`                  |
   > | `familyName`          | `Family Name`                 |
   > | `workPhone`           | `Primary Phone`               |
   > | `workEmail`           | `Email Address`               |

   1. If any of the default attributes are missing from the attribute mapping, add them. To add an attribute mapping, click **[icon: plus, set=fa]Add**, then select the source and target attribute.

      You must click **[icon: plus, set=fa]Add** for each attribute that you need to map.

      Learn more about configuring attribute mapping in [Adding attribute mapping for outbound provisioning](https://docs.pingidentity.com/pingone/integrations/p1_add_attribute_mapping_idp.html).

3. Map the following Code42 SCIM attributes.

   > **Collapse: Remaining Code42 SCIM attributes**
   >
   > | Code42 SCIM Attribute | PingOne PingOneUser Attribute |
   > | --------------------- | ----------------------------- |
   > | `externalId`          | `External ID`                 |
   > | `workCity`            | `Locality`                    |
   > | `workStreetAddeess`   | `Street Address`              |
   > | `workCountry`         | `Country Code`                |
   > | `workPostalCode`      | `Postal Code`                 |
   > | `userType`            | `Type`                        |
   > | `title`               | `Title`                       |
   > | `nickName`            | `Nickname`                    |
   > | `formattedName`       | `Formatted`                   |

4. Click **Save**.

---

---
title: Creating a provisioning connection in PingOne
description: To enable PingOne to manage users in Code42, create a provisioning connection.
component: code42-pingone
page_id: code42-pingone:provisioning_setup:p1_code42_integration_creating_a_provisioning_connection_in_p1
canonical_url: https://docs.pingidentity.com/integrations/code42-pingone/provisioning_setup/p1_code42_integration_creating_a_provisioning_connection_in_p1.html
llms_txt: https://docs.pingidentity.com/integrations/code42-pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 26, 2024
section_ids:
  before-you-begin: Before you begin
  steps: Steps
  creating-a-provisioning-rule-in-pingone: Creating a provisioning rule in PingOne
  before-you-begin-2: Before you begin
  about-this-task: About this task
  steps-2: Steps
  result: Result:
  result-2: Result:
  configuring-a-user-filter-on-the-provisioning-rule: Configuring a user filter on the provisioning rule
  before-you-begin-3: Before you begin
  about-this-task-2: About this task
  steps-3: Steps
  configuring-attribute-mapping-on-the-provisioning-rule: Configuring attribute mapping on the provisioning rule
  before-you-begin-4: Before you begin
  about-this-task-3: About this task
  steps-4: Steps
---

# Creating a provisioning connection in PingOne

To enable PingOne to manage users in Code42, create a provisioning connection.

## Before you begin

If you don't want to provision users from an existing PingOne population, you can add a new one. For help, see [Managing populations](https://docs.pingidentity.com/pingone/directory/p1_manage_populations.html) in the PingOne documentation.

## Steps

1. In PingOne, go to **Integrations > Provisioning**.

2. Click **[icon: plus, set=fa]**, then click **New Connection**.

3. In the **Choose a connection type** section, select **Identity Store**.

4. On the **SCIM Outbound** tile, click **Select**, and then click **Next**.

5. Enter a name and description for the provisioning connection, then click **Next**.

   The connection name will appear in your configured connections list after you complete and save the connection.

6. In the **Configure Authentication** section, enter the Code42 details:

   1. In the **SCIM base URL** field, enter the base URL that you noted in [Adding PingOne as SCIM provider in Code42](p1_code42_integration_adding_p1_as_scim_provider_in_code42.html).

   2. For **Users Resource**, use the default value of **/Users**.

   3. For **SCIM Version**, use the default selection, **2.0**.

   4. In the **Authentication Method** list, select **OAuth 2 Bearer Token**.

   5. In the **OAuth Access Token** field, enter the **Token** that you noted in [Adding PingOne as SCIM provider in Code42](p1_code42_integration_adding_p1_as_scim_provider_in_code42.html).

   6. For the **Auth Type Header**, use the default selection, **Bearer**.

   7. Click **Test Connection**.

   8. Resolve any issues that are reported, and then click **Next**.

7. In the **Configure Preferences** section, enter the provisioning options.

   1. Use the following default filter and deprovisioning actions:

      > **Collapse: Table**
      >
      > | Setting                    | Value                                                      |
      > | -------------------------- | ---------------------------------------------------------- |
      > | **User Filter Expression** | `username Eq "%s"`                                         |
      > | **User Identifier**        | `userName`                                                 |
      > | **Remove Action**          | **Disable**&#xA;&#xA;Code42 doesn't support user deletion. |

   2. **Optional:** Customize the provisioning options in the following table:

      | Setting                        | Description                                                                                                  |
      | ------------------------------ | ------------------------------------------------------------------------------------------------------------ |
      | **Allow users to be created**  | Determines whether PingOne creates a user in Code42 when the user is created in PingOne.                     |
      | **Allow users to be updated**  | Determines whether PingOne updates a user's attributes in Code42 when the user attributes change in PingOne. |
      | **Allow users to be disabled** | Determines whether PingOne disables a user in Code42 when the user is disabled in PingOne.                   |

   3. Click **Save**.

8. To enable your new provisioning connection, in its details pane, click the toggle.

## Creating a provisioning rule in PingOne

### Before you begin

Complete the [Creating a provisioning connection in PingOne](p1_code42_integration_creating_a_provisioning_connection_in_p1.html) procedure.

### About this task

Create a provisioning rule and assign the provisioning connection that you created in the previous procedure as the **Target** connection.

To create a provisioning rule:

### Steps

1. Go to **Integrations > Provisioning**.

2. Click **[icon: plus, set=fa]**, then **New Rule**.

3. Enter a name and description for the rule, and then click **Create Rule**.

   |   |                                       |
   | - | ------------------------------------- |
   |   | **Description** is an optional field. |

4. On the **Configuration** tab, assign a target connection:

   1. Click **Target**.

   2. In the **Available Connections** section, in the row for the provisioning connection that you created in the previous procedure, click **[icon: plus, set=fa]**to add it as the target connection.

      You can add a disabled connection to the target, but you must enable the connection before you can enable the associated rule.

      #### Result:

      PingOne is automatically selected as the **Source** connection.

5. Click **Save**.

   #### Result:

   The rule's name appears in the list on the **Rules** tab.

6. To enable the new rule, in its details pane, click the toggle.

## Configuring a user filter on the provisioning rule

### Before you begin

Complete the following procedures in order:

1. [Creating a provisioning connection in PingOne](p1_code42_integration_creating_a_provisioning_connection_in_p1.html)

2. [Creating a provisioning rule in PingOne](p1_code42_integration_creating_a_provisioning_rule.html)

### About this task

Configure a user filter on the provisioning rule that you created in the [Creating a provisioning rule in PingOne](p1_code42_integration_creating_a_provisioning_rule.html) procedure to specify which PingOne user populations to provision to Code42:

### Steps

1. On the **Configuration** tab of the provisioning rule, click **User Filter**.

2. Click the **Pencil** icon to edit the filter.

3. Define the filter that determines which identities to provision to Code42.

   For more information, see [Adding a user filter](https://docs.pingidentity.com/pingone/integrations/p1_add_provisioning_filter.html) and [Example user filters](https://docs.pingidentity.com/pingone/integrations/p1_example_provisioning_filters.html).

   1. Enter the first condition:

      * All

        Select **All** or **Any** to determine how to evaluate the linked conditions. **All** functions as the boolean logical operator `AND`.

      * Any

        Select **All** or **Any** to determine how to evaluate the linked conditions. **Any** functions as the boolean logical operator `OR`.

      * Attribute

        The user attribute to filter by.

        |   |                                        |
        | - | -------------------------------------- |
        |   | Use the **Population Name** attribute. |

      * Operator

        The operator determines the context of the attribute and its value.

        |   |                                                     |
        | - | --------------------------------------------------- |
        |   | Equals is the only operator supported at this time. |

      * Value

        Enter an appropriate value for the specified attribute.

        |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
        | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
        |   | * For outbound provisioning rules, you must specify either a population or a group to define the users to be provisioned.

        * If you select a group in the filter, then updating or deleting the group can cause the provisioning rule to re-sync.

        * If you select a group in the filter, the filter includes all users with any kind of membership in the group, whether direct, dynamic membership based on a user filter, or inherited from parent groups. For more information, see [Groups](https://docs.pingidentity.com/pingone/directory/p1_groups.html). |

   2. Click **[icon: plus, set=fa]Add** to add more conditions or condition sets until you've specified all the PingOne user populations that you want to provision to Code42.

4. Click **Save**.

## Configuring attribute mapping on the provisioning rule

### Before you begin

Complete the following procedures in order:

1. [Creating a provisioning connection in PingOne](p1_code42_integration_creating_a_provisioning_connection_in_p1.html)

2. [Creating a provisioning rule in PingOne](p1_code42_integration_creating_a_provisioning_rule.html)

### About this task

Configure attribute mapping on the provisioning rule that you created in the [Creating a provisioning rule in PingOne](p1_code42_integration_creating_a_provisioning_rule.html) procedure to map the PingOne user attributes from the SCIM attributes in the Code42 identity store. For outbound provisioning, the mapping is applied to the attribute coming from the PingOne directory before it is saved to the target identity store.

To configure attribute mapping:

### Steps

1. On the **Configuration** tab of the provisioning rule, click **Attribute Mapping**.

2. Click the **Pencil** icon to edit the mapping and confirm that the following default attributes are within the mapping.

   > **Collapse: Default Code42 SCIM attributes**
   >
   > | Code42 SCIM Attribute | PingOne PingOneUser Attribute |
   > | --------------------- | ----------------------------- |
   > | `userName`            | `Username`                    |
   > | `givenName`           | `Given Name`                  |
   > | `familyName`          | `Family Name`                 |
   > | `workPhone`           | `Primary Phone`               |
   > | `workEmail`           | `Email Address`               |

   1. If any of the default attributes are missing from the attribute mapping, add them. To add an attribute mapping, click **[icon: plus, set=fa]Add**, then select the source and target attribute.

      You must click **[icon: plus, set=fa]Add** for each attribute that you need to map.

      Learn more about configuring attribute mapping in [Adding attribute mapping for outbound provisioning](https://docs.pingidentity.com/pingone/integrations/p1_add_attribute_mapping_idp.html).

3. Map the following Code42 SCIM attributes.

   > **Collapse: Remaining Code42 SCIM attributes**
   >
   > | Code42 SCIM Attribute | PingOne PingOneUser Attribute |
   > | --------------------- | ----------------------------- |
   > | `externalId`          | `External ID`                 |
   > | `workCity`            | `Locality`                    |
   > | `workStreetAddeess`   | `Street Address`              |
   > | `workCountry`         | `Country Code`                |
   > | `workPostalCode`      | `Postal Code`                 |
   > | `userType`            | `Type`                        |
   > | `title`               | `Title`                       |
   > | `nickName`            | `Nickname`                    |
   > | `formattedName`       | `Formatted`                   |

4. Click **Save**.

---

---
title: Creating a provisioning rule in PingOne
description: Complete the Creating a provisioning connection in PingOne procedure.
component: code42-pingone
page_id: code42-pingone:provisioning_setup:p1_code42_integration_creating_a_provisioning_rule
canonical_url: https://docs.pingidentity.com/integrations/code42-pingone/provisioning_setup/p1_code42_integration_creating_a_provisioning_rule.html
llms_txt: https://docs.pingidentity.com/integrations/code42-pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 26, 2024
section_ids:
  before-you-begin: Before you begin
  about-this-task: About this task
  steps: Steps
  result: Result:
  result-2: Result:
---

# Creating a provisioning rule in PingOne

## Before you begin

Complete the [Creating a provisioning connection in PingOne](p1_code42_integration_creating_a_provisioning_connection_in_p1.html) procedure.

## About this task

Create a provisioning rule and assign the provisioning connection that you created in the previous procedure as the **Target** connection.

To create a provisioning rule:

## Steps

1. Go to **Integrations > Provisioning**.

2. Click **[icon: plus, set=fa]**, then **New Rule**.

3. Enter a name and description for the rule, and then click **Create Rule**.

   |   |                                       |
   | - | ------------------------------------- |
   |   | **Description** is an optional field. |

4. On the **Configuration** tab, assign a target connection:

   1. Click **Target**.

   2. In the **Available Connections** section, in the row for the provisioning connection that you created in the previous procedure, click **[icon: plus, set=fa]**to add it as the target connection.

      You can add a disabled connection to the target, but you must enable the connection before you can enable the associated rule.

      ### Result:

      PingOne is automatically selected as the **Source** connection.

5. Click **Save**.

   ### Result:

   The rule's name appears in the list on the **Rules** tab.

6. To enable the new rule, in its details pane, click the toggle.

---

---
title: Creating an SSO connection in PingOne
description: To allow PingOne to handle single sign-on (SSO) to Code42, add a Security Assertion Markup Language (SAML) application profile.
component: code42-pingone
page_id: code42-pingone:single_sign-on_setup:p1_code42_integration_creating_an_sso_connection_in_p1
canonical_url: https://docs.pingidentity.com/integrations/code42-pingone/single_sign-on_setup/p1_code42_integration_creating_an_sso_connection_in_p1.html
llms_txt: https://docs.pingidentity.com/integrations/code42-pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 26, 2024
section_ids:
  steps: Steps
---

# Creating an SSO connection in PingOne

To allow PingOne to handle single sign-on (SSO) *(tooltip: \<div class="paragraph">
\<p>The process of authenticating an identity (signing on) at one website (usually with a user ID and password) and then accessing resources secured by other domains without reauthenticating.\</p>
\</div>)* to Code42, add a Security Assertion Markup Language (SAML) *(tooltip: \<div class="paragraph">
\<p>A standard, XML-based, message-exchange framework enabling the secure transmittal of authentication tokens and other user attributes across domains.\</p>
\</div>)* application profile.

## Steps

1. In PingOne, go to **Applications > Applications** and click **[icon: plus, set=fa]**.

2. On the **Add Application** pane, enter a unique **Application Name**.

3. In the **Application Type** section, click **SAML Application**, then click **Configure**.

4. On the **SAML Configuration** page, enter your SAML details:

   1. Click **Manually Enter**.

   2. Enter the following connection details using your own Code42 console address.

      |   |                                                                                                                                                                                                     |
      | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      |   | You can find your Code42 console address in the address bar of your browser when you sign on to Code42.![A screenshot that shows the console address in the browser.](_images/tjx1627490950907.jpg) |

      > **Collapse: Connection details**
      >
      > | Setting       | Value                                                     |
      > | ------------- | --------------------------------------------------------- |
      > | **ACS URLs**  | `https://Code42-console-address/api/SsoAuthLoginResponse` |
      > | **Entity ID** | `https://Code42-console-address`                          |

   3. Click **Save**, then click the **Pencil** icon and enter the following configuration details.

      > **Collapse: Connection details continued**
      >
      > | Setting                         | Value                                    |
      > | ------------------------------- | ---------------------------------------- |
      > | **Assertion Validity Duration** | `180` or your preferred duration.        |
      > | **Target Application URL**      | `https://Code42-console-address/console` |

      Use the default settings for the rest of the configuration.

   4. Click **Save**.

5. On the **Attribute Mappings** tab, map the PingOne `Email Address` attribute to `mail`:

   ![A screenshot that shows the Email Address PingOne attribute mapped to mail.](_images/iqx1627422656367.jpg)

   1. Click the **Pencil** icon, then click **[icon: plus, set=fa]Add**.

   2. In the **Attributes** field, enter **mail**.

   3. In the **PingOne Mappings** list, select **Email Address**.

      |   |                                                                                                                                                                                                                                                 |
      | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      |   | If the `Email Address` attribute is unavailable, go to **Directory > User Attributes**, select the **Show disabled attributes** checkbox, and click the toggle next to **email**. Return to the **Attribute Mapping** tab for your application. |

   4. Select the **Required** checkbox, then click **Save**.

6. To enable the application, in its details pane, click the toggle.

7. On the **Configuration** tab, click **Download Metadata** to save the `saml2-metadata-idp-***.xml` file.

---

---
title: Testing single sign-on
description: Check your single sign-on (SSO) connection by adding a user and signing on.
component: code42-pingone
page_id: code42-pingone:single_sign-on_setup:p1_code42_integration_testing_single_sign_on
canonical_url: https://docs.pingidentity.com/integrations/code42-pingone/single_sign-on_setup/p1_code42_integration_testing_single_sign_on.html
llms_txt: https://docs.pingidentity.com/integrations/code42-pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 26, 2024
section_ids:
  steps: Steps
---

# Testing single sign-on

Check your single sign-on (SSO) connection by adding a user and signing on.

## Steps

1. Create a user and provision it to Code42. For help, see the **Configure provisioning** section.

2. Set a password for the user in PingOne.

3. In Code42, make sure the user is part of the organization you configured in [Adding PingOne as an authentication provider in Code42](p1_code42_integration_adding_p1_as_an_authentication_provider_in_code42.html).

4. Go to https\://*Code42-console-address*/login/#/login and enter the username.

5. When you are redirected to PingOne, enter the username and password to sign on.

---

---
title: Testing user provisioning
description: Check your provisioning connection by adding a user.
component: code42-pingone
page_id: code42-pingone:provisioning_setup:p1_code42_integration_testing_user_provisioning
canonical_url: https://docs.pingidentity.com/integrations/code42-pingone/provisioning_setup/p1_code42_integration_testing_user_provisioning.html
llms_txt: https://docs.pingidentity.com/integrations/code42-pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 26, 2024
section_ids:
  steps: Steps
---

# Testing user provisioning

Check your provisioning connection by adding a user.

## Steps

1. In PingOne, create a user:

   1. Go to **Directory > Users** and click the **[icon: plus, set=fa]**icon.

   2. In the **Username** field, enter a username in the form of an email address.

   3. In the **Population** list, select the population that you chose in [Creating a provisioning connection in PingOne](p1_code42_integration_creating_a_provisioning_connection_in_p1.html).

   4. Click **Save**.

2. Check for the user in Code42:

   1. In Code42, go to **Environment > Users**.

   2. Look for the user that you created in PingOne.

      If the user doesn't appear in Code42:

      1. In PingOne, go to **Directory > Users** and open the details pane for the use that you created.

      2. In the **Services** list, select **Sync Status**.

      3. Verify that the user is synced to your provisioning identity rule.