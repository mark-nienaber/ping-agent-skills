---
title: Enabling provisioning and single sign-on in PingFederate 10.1 or later
description: In the PingFederate administrative console, configure the datastore for PingFederate to use as the source of user data.
component: slack
page_id: slack:setup:pf_slack_connector_enabling_provisioning_and_single_sign_on_in_pf_101_or_later
canonical_url: https://docs.pingidentity.com/integrations/slack/setup/pf_slack_connector_enabling_provisioning_and_single_sign_on_in_pf_101_or_later.html
llms_txt: https://docs.pingidentity.com/integrations/slack/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 8, 2024
section_ids:
  steps: Steps
---

# Enabling provisioning and single sign-on in PingFederate 10.1 or later

## Steps

1. In the PingFederate administrative console, configure the datastore for PingFederate to use as the source of user data.

   For help, see [Datastores](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_datastores.html) in the PingFederate documentation.

2. Go to **System > Server > Protocol Settings > Federation Info**.

3. In the **SAML 2.0 Entity ID** field, enter a name for PingFederate to use when identifying itself to SAML partners.

4. On the **Outbound Provisioning** tab, in the **Provisioner Data Store** list, select the internal database that will store the synchronization state. Click **Save**.

   For more information, see [Configuring outbound provisioning settings](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_protocolsettingstasklet_saasglobalprovisioningsettingsstate.html) in the PingFederate documentation.

---

---
title: Getting a Slack API access token
description: Use the OAuth Configuration Service to exchange your Slack client ID and secret for an access token. PingFederate uses this access token to connect to Slack. The process differs slightly depending on your plan.
component: slack
page_id: slack:setup:pf_slack_connector_getting_a_slack_api_access_token
canonical_url: https://docs.pingidentity.com/integrations/slack/setup/pf_slack_connector_getting_a_slack_api_access_token.html
llms_txt: https://docs.pingidentity.com/integrations/slack/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 8, 2024
section_ids:
  getting-an-access-token-for-slack-standard-or-plus: Getting an access token for Slack Standard or Plus
  steps: Steps
  getting-an-access-token-for-slack-enterprise-grid: Getting an access token for Slack Enterprise Grid
  steps-2: Steps
---

# Getting a Slack API access token

Use the OAuth Configuration Service to exchange your Slack client ID and secret for an access token. PingFederate uses this access token to connect to Slack. The process differs slightly depending on your plan.

## Getting an access token for Slack Standard or Plus

Exchange your Slack Standard or Plus client ID and secret for an access token.

### Steps

1. Go to the Ping Identity [OAuth Configuration Service](https://oauth.pingone.com/ocs/ppm/rest/v1/oauth/oasrequestform).

2. From the product list, select **Slack Connector**.

3. Enter the **Client ID** and **Client Secret** that you noted in [Registering PingFederate as an app in Slack](pf_slack_connector_registering_pf_as_an_app_in_slack.html).

   ![Screenshot showing the OCS with a client ID and secret entered in.](_images/kug1615501848165.jpg)

4. Click **Connect**.

5. If you receive a prompt to sign on, sign on with your Workspace Owner account.

6. When you receive a message that your application is requesting permission to administer your Slack team, click **Authorize**.

7. On the OAuth Configuration Service page, copy the **Access Token**.

   You will use the access token in [Creating a provisioning connection](pf_slack_connector_creating_a_provisioning_connection.html).

   ![Screenshot showing the Ping Identity OAuth Configuration Service with a modal window titled Service Response. The Access Token field has an access token string in it.](_images/jep1615502497836.jpg)

## Getting an access token for Slack Enterprise Grid

Exchange your Slack Enterprise Grid client ID and secret for an access token.

### Steps

1. In an "Incognito" (or "Private") browser window, go to the Ping Identity [OAuth Configuration Service](https://oauth.pingone.com/ocs/ppm/rest/v1/oauth/oasrequestform) (OCS).

2. From the product list, select **Slack Connector**.

3. Enter the **Client ID** and **Client Secret** that you noted in [Registering PingFederate as an app in Slack](pf_slack_connector_registering_pf_as_an_app_in_slack.html).

   ![Screenshot showing the OCS with a client ID and secret entered in.](_images/kug1615501848165.jpg)

4. Click **Connect**.

5. In the **Sign in to your workspace** window, enter the URL for your Slack organization, such as `mycompany.enterprise`**.slack.com**. Click **Continue**.

   ![Screenshot showing the Sign in to your workspace window with the organization ID entered in.](_images/vij1615501965907.jpg)

6. Click **Org Owners can also sign in here**.

   ![Screenshot showing the sign on options.](_images/aad1615502169763.jpg)

7. Enter your administrator credentials. Click **Sign in**.

   ![Screenshot showing the sign-on prompt with administrator credentials entered in.](_images/gxv1615502266804.jpg)

8. When you receive a message that your application is requesting permission, check that the request is for the organization. Do NOT select a Workspace from the **Please select an option** list. Click **Allow**.

   ![Screenshot showing the permission prompt. The word "organization" is highlighted. The Please select an option list does not have a Workplace selected.](_images/fti1615502383665.jpg)

9. On the OAuth Configuration Service page, copy the **Access Token**.

   You will use the access token in [Creating a provisioning connection](pf_slack_connector_creating_a_provisioning_connection.html).

   ![Screenshot showing the Ping Identity OAuth Configuration Service with a modal window titled Service Response. The Access Token field has an access token string in it.](_images/jep1615502497836.jpg)

---

---
title: Getting an access token for Slack Enterprise Grid
description: Exchange your Slack Enterprise Grid client ID and secret for an access token.
component: slack
page_id: slack:setup:pf_slack_connector_getting_an_access_token_for_slack_enterprise_grid
canonical_url: https://docs.pingidentity.com/integrations/slack/setup/pf_slack_connector_getting_an_access_token_for_slack_enterprise_grid.html
llms_txt: https://docs.pingidentity.com/integrations/slack/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 8, 2024
section_ids:
  steps: Steps
---

# Getting an access token for Slack Enterprise Grid

Exchange your Slack Enterprise Grid client ID and secret for an access token.

## Steps

1. In an "Incognito" (or "Private") browser window, go to the Ping Identity [OAuth Configuration Service](https://oauth.pingone.com/ocs/ppm/rest/v1/oauth/oasrequestform) (OCS).

2. From the product list, select **Slack Connector**.

3. Enter the **Client ID** and **Client Secret** that you noted in [Registering PingFederate as an app in Slack](pf_slack_connector_registering_pf_as_an_app_in_slack.html).

   ![Screenshot showing the OCS with a client ID and secret entered in.](_images/kug1615501848165.jpg)

4. Click **Connect**.

5. In the **Sign in to your workspace** window, enter the URL for your Slack organization, such as `mycompany.enterprise`**.slack.com**. Click **Continue**.

   ![Screenshot showing the Sign in to your workspace window with the organization ID entered in.](_images/vij1615501965907.jpg)

6. Click **Org Owners can also sign in here**.

   ![Screenshot showing the sign on options.](_images/aad1615502169763.jpg)

7. Enter your administrator credentials. Click **Sign in**.

   ![Screenshot showing the sign-on prompt with administrator credentials entered in.](_images/gxv1615502266804.jpg)

8. When you receive a message that your application is requesting permission, check that the request is for the organization. Do NOT select a Workspace from the **Please select an option** list. Click **Allow**.

   ![Screenshot showing the permission prompt. The word "organization" is highlighted. The Please select an option list does not have a Workplace selected.](_images/fti1615502383665.jpg)

9. On the OAuth Configuration Service page, copy the **Access Token**.

   You will use the access token in [Creating a provisioning connection](pf_slack_connector_creating_a_provisioning_connection.html).

   ![Screenshot showing the Ping Identity OAuth Configuration Service with a modal window titled Service Response. The Access Token field has an access token string in it.](_images/jep1615502497836.jpg)

---

---
title: Getting an access token for Slack Standard or Plus
description: Exchange your Slack Standard or Plus client ID and secret for an access token.
component: slack
page_id: slack:setup:pf_slack_connector_getting_an_access_token_for_slack_standard_or_plus
canonical_url: https://docs.pingidentity.com/integrations/slack/setup/pf_slack_connector_getting_an_access_token_for_slack_standard_or_plus.html
llms_txt: https://docs.pingidentity.com/integrations/slack/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 8, 2024
section_ids:
  steps: Steps
---

# Getting an access token for Slack Standard or Plus

Exchange your Slack Standard or Plus client ID and secret for an access token.

## Steps

1. Go to the Ping Identity [OAuth Configuration Service](https://oauth.pingone.com/ocs/ppm/rest/v1/oauth/oasrequestform).

2. From the product list, select **Slack Connector**.

3. Enter the **Client ID** and **Client Secret** that you noted in [Registering PingFederate as an app in Slack](pf_slack_connector_registering_pf_as_an_app_in_slack.html).

   ![Screenshot showing the OCS with a client ID and secret entered in.](_images/kug1615501848165.jpg)

4. Click **Connect**.

5. If you receive a prompt to sign on, sign on with your Workspace Owner account.

6. When you receive a message that your application is requesting permission to administer your Slack team, click **Authorize**.

7. On the OAuth Configuration Service page, copy the **Access Token**.

   You will use the access token in [Creating a provisioning connection](pf_slack_connector_creating_a_provisioning_connection.html).

   ![Screenshot showing the Ping Identity OAuth Configuration Service with a modal window titled Service Response. The Access Token field has an access token string in it.](_images/jep1615502497836.jpg)

---

---
title: Known issues and limitations
description: There are no known issues.
component: slack
page_id: slack:release_notes:pf_slack_connector_known_issues_and_limitations
canonical_url: https://docs.pingidentity.com/integrations/slack/release_notes/pf_slack_connector_known_issues_and_limitations.html
llms_txt: https://docs.pingidentity.com/integrations/slack/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 8, 2024
section_ids:
  known-issues: Known issues
  known-limitations: Known limitations
---

# Known issues and limitations

## Known issues

There are no known issues.

## Known limitations

* Attributes

  * Due to a limitation in Slack, the username attribute cannot be updated after it is set.

  * Due to limitations in PingFederate, user attributes cannot be cleared after they are set.

  * The unique user identifier (`userName` or `primaryEmail`) that you choose when you create your connection to Slack can only be changed be deleting the connection, restarting PingFederate, and then creating a new connection.

  * When using multiple channels, the same unique user identifier mapping is required to coordinate manager assignments across different channels.

* Deprovisioning

  * When an LDAP user is deleted in a targeted group distinguished name (DN), the provisioning connector does not propagate the deletion until a new user is added to the group. This limitation is compounded when the **User Create** provisioning option is disabled. For solutions, see [SaaS provisioner does not remove the user](https://support.pingidentity.com/s/article/After-deleting-an-AD-user-account-SaaS-provisioner-does-not-remove-the-user-in-the-next-provisioning-cycle-when-Group-DN-is-specified) in the Knowledge Base.

* Provisioning

  * Due to a limitation in Slack, PingFederate cannot create users in a disabled state. If a user is disabled in your datastore, it will not be created in Slack by the provisioner.

  * For more information on Slack provisioning limitations, see .slack.com/scim//\[SCIM API] in the Slack API documentation.

* Configuration

  * In PingFederate 8.1 and earlier, when you configure a second SP connection with the provisioning connector, the second connection may be pre-populated with the channel from the first connection. To avoid conflicts, remove this pre-populated channel and create a unique channel for each connection.

---

---
title: Preparing your SAML metadata file
description: Modify the SAML details in the included saml-metadata.xml file. This file makes it easier to configure your connection in PingFederate.
component: slack
page_id: slack:setup:pf_slack_connector_preparing_your_saml_metadata_file
canonical_url: https://docs.pingidentity.com/integrations/slack/setup/pf_slack_connector_preparing_your_saml_metadata_file.html
llms_txt: https://docs.pingidentity.com/integrations/slack/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 8, 2024
section_ids:
  steps: Steps
---

# Preparing your SAML metadata file

Modify the SAML details in the included `saml-metadata.xml` file. This file makes it easier to configure your connection in PingFederate.

## Steps

1. In a text editor, open the `saml-metadata.xml` file that is included in the Slack Provisioner `.zip` archive.

2. In the `.xml` file, find the `Location="https://TEAM_NAME.slack.com/sso/saml"` line. Modify it with your Slack Workspace or Enterprise Grid name.

   For example, `Location="https://myworkspace.slack.com/sso/saml"`.

3. Remove the trailing slash (`/`) from `entityID="https://slack.com/"`.

   Result: `entityID="https://slack.com"`

4. Save your changes.

   You'll use this file in [Creating a provisioning connection](pf_slack_connector_creating_a_provisioning_connection.html).

---

---
title: Provisioning options reference
description: The table provided lists the main provisioning capabilities available in the Slack connection configuration.
component: slack
page_id: slack:setup:pf_slack_connector_provisioning_options_reference
canonical_url: https://docs.pingidentity.com/integrations/slack/setup/pf_slack_connector_provisioning_options_reference.html
llms_txt: https://docs.pingidentity.com/integrations/slack/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 8, 2024
---

# Provisioning options reference

The table provided lists the main provisioning capabilities available in the Slack connection configuration.

| Field Name                                                                                                                                                    | Description                                                                                                                                                                               |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **User Create**                                                                                                                                               | **Selected** (default) – PingFederate creates users in Slack.**Cleared** – PingFederate does not create users in Slack.                                                                   |
| **User Update**                                                                                                                                               | **Selected** (default) – PingFederate updates existing users in Slack. PingFederate can also re-enable disabled users.**Cleared** – PingFederate does not update existing users in Slack. |
| **User Disable**                                                                                                                                              | **Selected** (default) – PingFederate disables users in Slack.**Cleared** – PingFederate does not disable users in Slack.                                                                 |
| &#xA;&#xA;If any of the above options are cleared, PingFederate logs a warning in the user workflow section of provisioner.log when the related action fails. |                                                                                                                                                                                           |

---

---
title: Registering PingFederate as an app in Slack
description: Before PingFederate can access the Slack API, it needs an access token. To get the access token, you need to register PingFederate as an app in Slack.
component: slack
page_id: slack:setup:pf_slack_connector_registering_pf_as_an_app_in_slack
canonical_url: https://docs.pingidentity.com/integrations/slack/setup/pf_slack_connector_registering_pf_as_an_app_in_slack.html
llms_txt: https://docs.pingidentity.com/integrations/slack/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 8, 2024
section_ids:
  steps: Steps
---

# Registering PingFederate as an app in Slack

Before PingFederate can access the Slack API, it needs an access token. To get the access token, you need to register PingFederate as an app in Slack.

## Steps

1. Sign on to Slack as an Admin or workspace Owner.

   If you don't already have a Slack workspace, create one. For help, see [Getting started for workspace creators](https://slack.com/intl/en-ca/help/articles/217626298-Getting-started-for-workspace-creators) in the Slack documentation.

2. Go to the Slack [Your Apps](https://api.slack.com/apps) window.

3. Click **Create New App**.

4. On the **Create a Slack App** modal, enter a name and select a workspace. Click **Create App**.

5. On the **Basic Information** window, in the **App Credentials** section, note the **Client ID** and **Client Secret**.

   You will use these in [Getting a Slack API access token](pf_slack_connector_getting_a_slack_api_access_token.html).

6. In the navigation pane, click **OAuth & Permissions**.

7. On the **OAuth & Permissions** window, in the **Redirect URLs** section, add the Ping Identity OAuth Configuration Service (OCS).

   1. Click **Add New Redirect URL**.

   2. In the **Redirect URLs** field, enter the following:

      ```
      https://oauth.pingone.com/ocs/ppm/rest/v1/oauth/oastempcredresponse/
      ```

   3. Click **Add**. Click **Save URLs**.

8. In the **Scopes** section, add the admin scope.

   1. In the **User Token Scopes** section, click **Add an OAuth Scope**.

   2. Select **Admin**.

9. Submit your app to the [Slack App Directory](https://slack.com/apps).

   |   |                                                                                      |
   | - | ------------------------------------------------------------------------------------ |
   |   | This step is required for Slack Enterprise Grid, but optional for other Slack plans. |

   1. In the navigation pane, click **Manage Distribution**.

   2. In the **Remove Hard Coded Information** section, select the **I've reviewed and removed any hard-coded information** check box.

   3. Click **Activate Public Distribution**.

---

---
title: Slack Provisioner
description: The Slack Provisioner allows PingFederate to integrate with Slack for user provisioning and single sign-on (SSO).
component: slack
page_id: slack::pf_slack_connector
canonical_url: https://docs.pingidentity.com/integrations/slack/pf_slack_connector.html
llms_txt: https://docs.pingidentity.com/integrations/slack/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 8, 2024
section_ids:
  features: Features
  intended-audience: Intended audience
  system-requirements: System requirements
---

# Slack Provisioner

The Slack Provisioner allows PingFederate to integrate with Slack for user provisioning and single sign-on (SSO).

## Features

* Supports all Slack plans, including Standard, Plus, and Enterprise Grid.

* Manages users in Slack based on changes in an external datastore that is attached to PingFederate.

  * Creates, updates, and disables users.

  * Allows you to enable the create, update, and disable capabilities independently.

  * Allows you to choose to disable users when deprovisioning.

* Browser-based SSO initiated by the service provider (SP) or identity provider (IdP).

* Pre-populates some connection settings with the included quick connection template and SAML metadata file.

## Intended audience

This document is intended for PingFederate administrators.

If you need help during the setup process, see the following resources:

* The following sections of the PingFederate documentation:

  * [Identity provider SSO configuration](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_ident_provid_sso_config.html)

  * [Datastores](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_datastores.html)

  * [SP connection management](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_sp_connect_management.html)

  * [Configuring outbound provisioning](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_spconnectionconfigtasklet_saasprovisioningstate.html)

  * [Configuring outbound provisioning settings](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_protocolsettingstasklet_saasglobalprovisioningsettingsstate.html)

- The following sections of the Slack documentation:

  * [Manage members with SCIM Provisioning](https://slack.com/intl/en-ca/help/articles/212572638-Manage-members-with-SCIM-provisioning)

  * [SAML single sign-on](https://slack.com/intl/en-ca/help/articles/203772216-SAML-single-sign-on)

  * [Guide to single sign-on settings](https://slack.com/intl/en-ca/help/articles/220403548-Guide-to-single-sign-on-settings)

## System requirements

* PingFederate 9.0 or later.

* A Slack Workspace Owner account.

* A Slack Plus or Enterprise Grid plan is required to use the optional SSO functionality.

* To allow PingFederate to make outbound connections to the Slack API, you might need to allow the following domain in your firewall:

  * https\://api.slack.com

---

---
title: Supported attributes reference
description: The table provided lists the attributes that can be mapped for user provisioning to Slack.
component: slack
page_id: slack:setup:pf_slack_connector_supported_attributes_reference
canonical_url: https://docs.pingidentity.com/integrations/slack/setup/pf_slack_connector_supported_attributes_reference.html
llms_txt: https://docs.pingidentity.com/integrations/slack/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 25, 2024
---

# Supported attributes reference

The table provided lists the attributes that can be mapped for user provisioning to Slack.

| Attribute         | Description                                                                                                                                                                                             |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| userName          | The user's unique identifier in Slack. A user's userName cannot be updated once it is created.This attribute is required.                                                                               |
| primaryEmail      | The user's email address.This attribute is required.                                                                                                                                                    |
| givenName         | The given name of the user, or first name in most Western languages. For example, "Barbara" given the full name "Ms. Barbara Jane Jensen, III".                                                         |
| familyName        | The family name of the user, or last name in most Western languages. For example, "Jensen" given the full name "Ms. Barbara Jane Jensen, III".                                                          |
| honorificPrefix   | The honorific prefix or prefixes of the user, or title in most Western languages. For example, "Ms." given the full name "Ms. Barbara Jane Jensen, III".                                                |
| displayName       | The name of the user, suitable for display to end-users.                                                                                                                                                |
| title             | The user's title, such as "Vice President".                                                                                                                                                             |
| preferredLanguage | Indicates the user's preferred written or spoken languages and is generally used for selecting a localized user interface.                                                                              |
| userType          | Used to identify the relationship between the organization and the user. Typical values used might be "Contractor", "Employee", "Intern", "Temp", "External", and "Unknown", but any value can be used. |
| locale            | Used to indicate the user's default location for purposes of localizing such items as currency, date time format, or numerical representations.                                                         |
| profileUrl        | A URI that is a uniform resource locator that points to a location representing the user's online profile, such as a web page.                                                                          |
| profilePhotoUrl   | A URI that is a uniform resource locator that points to the user's profile photo. The resource MUST be a file (for example, a GIF, JPEG, or PNG image file) rather than a web page containing an image. |
| timezone          | The user's time zone, in IANA Time Zone database format, such as "America/Los_Angeles".                                                                                                                 |
| roles             | A role for the user that represents who the user is, such as "Student", "Faculty". This attribute can only accept one value.                                                                            |
| primaryPhone      | The primary phone number for the user, such as "+1-201-555-0123".                                                                                                                                       |
| mobilePhone       | The mobile phone number for the user, such as "+1-201-555-0123".                                                                                                                                        |
| streetAddress     | The work street address for the user, which may include house number, street name, P.O. box, and multi-line extended street address information.                                                        |
| locality          | The work locality or locality component for the user's mailing address.                                                                                                                                 |
| region            | The region or state component for the user's mailing address.                                                                                                                                           |
| postalCode        | The work ZIP or postal code component for the user's mailing address.                                                                                                                                   |
| country           | The work country component for the user's mailing address.                                                                                                                                              |
| employeeNumber    | A string identifier, typically numeric or alphanumeric, assigned to a person, often based on order of hire or association with an organization.                                                         |
| costCenter        | The cost center for the user.                                                                                                                                                                           |
| organization      | The organization for the user.                                                                                                                                                                          |
| division          | The division for the user.                                                                                                                                                                              |
| department        | The department for the user.                                                                                                                                                                            |

---

---
title: Upgrading an existing deployment
description: If you're upgrading from a previous version of the Slack Provisioner, note your existing service provider (SP) connection configuration and create a new connection.
component: slack
page_id: slack:setup:pf_slack_connector_upgrading_an_existing_deployment
canonical_url: https://docs.pingidentity.com/integrations/slack/setup/pf_slack_connector_upgrading_an_existing_deployment.html
llms_txt: https://docs.pingidentity.com/integrations/slack/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 8, 2024
section_ids:
  upgrading-an-existing-deployment-in-pingfederate-10-1-or-later: Upgrading an existing deployment in PingFederate 10.1 or later
  steps: Steps
  upgrading-an-existing-deployment-in-pingfederate-10-0-or-earlier: Upgrading an existing deployment in PingFederate 10.0 or earlier
  steps-2: Steps
---

# Upgrading an existing deployment

* If you're upgrading from a previous version of the Slack Provisioner, note your existing service provider (SP) connection configuration and create a new connection.

## Upgrading an existing deployment in PingFederate 10.1 or later

### Steps

1. Back up your current PingFederate configuration as shown in [Configuration archive](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_configurationarchivetasklet_selectimportexportstate.html) in the PingFederate documentation.

2. In the PingFederate administrative console, go to **Applications > Integration > SP Connections** and select your connection.

   Note the attribute mappings for your existing SP connection.

   For help, see [Mapping attributes](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_saaschanneltasklet_saasattrmappingmgmtstate.html) in the PingFederate documentation.

3. Delete your existing SP connection.

   1. Go to **Applications > Integration > SP Connections**.For your existing connection, click **Select action**, and then click **Delete**. Click **Confirm.**

4. Complete the steps in [Deploying the integration files](pf_slack_connector_deploying_the_integration_files.html).

5. Complete the steps in [Creating a provisioning connection](pf_slack_connector_creating_a_provisioning_connection.html).

   * From **Outbound Provisioning > Manage Channels > Channel**, on the **Attribute Mapping** tab, configure the attribute mappings based on your notes.

6. Complete the steps in [Creating a single sign-on connection](pf_slack_connector_creating_a_single_sign_on_connection.html).

## Upgrading an existing deployment in PingFederate 10.0 or earlier

### Steps

1. Back up your current PingFederate configuration as shown in [Configuration archive](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_configurationarchivetasklet_selectimportexportstate.html) in the PingFederate documentation.

2. In the PingFederate administrative console, go to **Identity Provider > SP Connections** and select your connection.

   Note the attribute mappings for your existing SP connection.

   For help, see [Mapping attributes](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_saaschanneltasklet_saasattrmappingmgmtstate.html) in the PingFederate documentation.

3. Delete your existing SP connection.

   1. Go to **Identity Provider > SP Connections > Manage All**.For your existing connection, click **Select action**, and then click **Delete**. Click **Save.**

4. Complete the steps in [Deploying the integration files](pf_slack_connector_deploying_the_integration_files.html).

5. Complete the steps in [Creating a provisioning connection](pf_slack_connector_creating_a_provisioning_connection.html).

   * From **Outbound Provisioning > Manage Channels > Channel**, on the **Attribute Mapping** tab, configure the attribute mappings based on your notes.

6. Complete the steps in [Creating a single sign-on connection](pf_slack_connector_creating_a_single_sign_on_connection.html).

---

---
title: Upgrading an existing deployment in PingFederate 10.0 or earlier
description: Back up your current PingFederate configuration as shown in Configuration archive in the PingFederate documentation.
component: slack
page_id: slack:setup:pf_slack_connector_upgrading_an_existing_deployment_in_pf_100_or_earlier
canonical_url: https://docs.pingidentity.com/integrations/slack/setup/pf_slack_connector_upgrading_an_existing_deployment_in_pf_100_or_earlier.html
llms_txt: https://docs.pingidentity.com/integrations/slack/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 8, 2024
section_ids:
  steps: Steps
---

# Upgrading an existing deployment in PingFederate 10.0 or earlier

## Steps

1. Back up your current PingFederate configuration as shown in [Configuration archive](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_configurationarchivetasklet_selectimportexportstate.html) in the PingFederate documentation.

2. In the PingFederate administrative console, go to **Identity Provider > SP Connections** and select your connection.

   Note the attribute mappings for your existing SP connection.

   For help, see [Mapping attributes](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_saaschanneltasklet_saasattrmappingmgmtstate.html) in the PingFederate documentation.

3. Delete your existing SP connection.

   1. Go to **Identity Provider > SP Connections > Manage All**.For your existing connection, click **Select action**, and then click **Delete**. Click **Save.**

4. Complete the steps in [Deploying the integration files](pf_slack_connector_deploying_the_integration_files.html).

5. Complete the steps in [Creating a provisioning connection](pf_slack_connector_creating_a_provisioning_connection.html).

   * From **Outbound Provisioning > Manage Channels > Channel**, on the **Attribute Mapping** tab, configure the attribute mappings based on your notes.

6. Complete the steps in [Creating a single sign-on connection](pf_slack_connector_creating_a_single_sign_on_connection.html).

---

---
title: Upgrading an existing deployment in PingFederate 10.1 or later
description: Back up your current PingFederate configuration as shown in Configuration archive in the PingFederate documentation.
component: slack
page_id: slack:setup:pf_slack_connector_upgrading_an_existing_deployment_in_pf_101_or_later
canonical_url: https://docs.pingidentity.com/integrations/slack/setup/pf_slack_connector_upgrading_an_existing_deployment_in_pf_101_or_later.html
llms_txt: https://docs.pingidentity.com/integrations/slack/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 8, 2024
section_ids:
  steps: Steps
---

# Upgrading an existing deployment in PingFederate 10.1 or later

## Steps

1. Back up your current PingFederate configuration as shown in [Configuration archive](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_configurationarchivetasklet_selectimportexportstate.html) in the PingFederate documentation.

2. In the PingFederate administrative console, go to **Applications > Integration > SP Connections** and select your connection.

   Note the attribute mappings for your existing SP connection.

   For help, see [Mapping attributes](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_saaschanneltasklet_saasattrmappingmgmtstate.html) in the PingFederate documentation.

3. Delete your existing SP connection.

   1. Go to **Applications > Integration > SP Connections**.For your existing connection, click **Select action**, and then click **Delete**. Click **Confirm.**

4. Complete the steps in [Deploying the integration files](pf_slack_connector_deploying_the_integration_files.html).

5. Complete the steps in [Creating a provisioning connection](pf_slack_connector_creating_a_provisioning_connection.html).

   * From **Outbound Provisioning > Manage Channels > Channel**, on the **Attribute Mapping** tab, configure the attribute mappings based on your notes.

6. Complete the steps in [Creating a single sign-on connection](pf_slack_connector_creating_a_single_sign_on_connection.html).

---

---
title: User and group management
description: The Slack Provisioner links users and groups from the data store to Slack. The behavior of each provisioning capability is described below.
component: slack
page_id: slack::pf_slack_connector_user_and_group_management
canonical_url: https://docs.pingidentity.com/integrations/slack/pf_slack_connector_user_and_group_management.html
llms_txt: https://docs.pingidentity.com/integrations/slack/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 8, 2024
section_ids:
  synchronizing-existing-users: Synchronizing existing users
  user-provisioning: User provisioning
  user-updates: User updates
  user-deprovisioning: User deprovisioning
  synchronizing-existing-groups: Synchronizing existing groups
  group-provisioning: Group provisioning
  group-name-updates: Group name updates
  group-membership-updates: Group membership updates
  group-deletion: Group deletion
---

# User and group management

The Slack Provisioner links users and groups from the data store to Slack. The behavior of each provisioning capability is described below.

## Synchronizing existing users

By default, the provisioning connector synchronizes based on the `userName` attribute in Slack. You can change the default mapping in [Creating a provisioning connection](setup/pf_slack_connector_creating_a_provisioning_connection.html).

For example:

* In Slack, Janet's `userName` is `jsmith`.

* In your data store, Janet's `sAMAccountName` is `jsmith`.

* On the **Attribute Mapping** tab of your PingFederate channel configuration, you map the `userName` attribute to `sAMAccountName`.

* When the provisioning connector runs, the data store user is provisioned with a `userName` of `jsmith`. That matches Janet's existing `userName` in Slack, so her information in the data store is synchronized to her Slack account.

## User provisioning

Triggered by either of the following:

* A user is added to the data store group or filter that is targeted by the provisioning connector.

* A user with "disabled" status is added to the data store group or filter that is targeted by the provisioning connector, and the **Provision disabled users** provisioning option is enabled.

The target is determined by the **Source Location** tab in the provisioning connector configuration.

## User updates

Triggered when a change occurs to a user attribute that is mapped in the provisioning connector configuration, such as an attribute change or the user being re-enabled from a disabled status.

## User deprovisioning

Triggered by any of the following:

* A user is deleted from the user store.

* A user is disabled in the user store.

* A user is removed from the data store group or filter that is targeted by the provisioning connector.

The **Remove User Action** setting in the connection configuration determines whether the deprovisioning action disables or deletes the user.

## Synchronizing existing groups

The provisioning connector synchronizes groups from the data store to Slack based on the group name.

For example:

* In Slack, there is a group is named `Accounting`.

* In your data store, there is a group with a `CN` of `Accounting`.

* When the provisioning connector runs, the two groups are synchronized.

## Group provisioning

Triggered when a group is added to the data store filter that is targeted by the provisioning connector.

The target is determined by the **Source Location** tab in the provisioning connector configuration.

## Group name updates

Renaming the group in the data store will trigger PingFederate to rename the group in Slack.

## Group membership updates

Changing group memberships through the group's properties or a user's properties will trigger PingFederate to update the group membership in Slack.

Group memberships in the data store overwrite the group memberships in Slack.

## Group deletion

Triggered by any of the following:

* Deleting the group in the data store will trigger PingFederate to delete the group in Slack. Group deletions are permanent and cannot be undone.

* The group is removed from the data store group or filter that is targeted by the provisioning connector.