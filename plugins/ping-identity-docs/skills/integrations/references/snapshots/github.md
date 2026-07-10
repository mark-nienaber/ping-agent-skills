---
title: Obtain client ID and secret from GitHub
description: An OAuth app must be created in GitHub to access protected content in an organization. Upon OAuth app creation, client ID and secret will be generated.
component: github
page_id: github:github_provisioner:pf_github_connector_obtain_client_id_and_secret_from_github
canonical_url: https://docs.pingidentity.com/integrations/github/github_provisioner/pf_github_connector_obtain_client_id_and_secret_from_github.html
llms_txt: https://docs.pingidentity.com/integrations/github/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 25, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Obtain client ID and secret from GitHub

## About this task

An OAuth app must be created in GitHub to access protected content in an organization. Upon OAuth app creation, client ID and secret will be generated.

## Steps

1. Log into your GitHub account as an administrative user for your organization.

2. In the top right corner of GitHub, click your profile photo, then click Your profile.

   ![An image of the GitHub profile menu options.](_images/gws1563995343086.png)

3. On the left side of your profile page, under Organizations, click the icon for your organization.

   ![An image of the GitHub organization icon.](_images/exd1563995343571.png)

4. Under your organization name, click Settings.

   ![An image of the GitHub organization settings menu.](_images/gzb1563995344049.png)

5. In the developer settings sidebar, click OAuth Apps.

   ![An image of the GitHub developer settings menu.](_images/agf1563995344578.png)

6. On the OAuth Apps screen, click Register an application or New OAuth App.

   * Give your application a name, such as "PingFederate Provisioning".

   * Add the following URL to the Homepage URL field:

     `https://www.pingidentity.com`

   * Add the following URL to the Authorization callback URL field:

     `https://oauth.pingone.com/ocs/ppm/rest/v1/oauth/oastempcredresponse/`

     ![An image of the OAuth application registration screen.](_images/rtl1563995345017.png)

7. Click the Register application button to save your changes.

8. Copy the Client ID and Client Secret values to use in the next section.

   |   |                                                                                                                                                                                                                                                                                     |
   | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | Applications that are owned by the organization are automatically given access to the organization's resources. For more information, see [About OAuth App access restrictions](https://help.github.com/articles/about-oauth-app-access-restrictions/) in the GitHub documentation. |

---

---
title: Obtain PingFederate signing certificate
description: The following are the steps to obtain the signing certificate used for the digital signature verification of the PingFederate IdP. When asked during Configure GitHub for provisioning and SSO, provide the certificate that you have downloaded from PingFederate. Learn more in Managing digital signing certificates and decryption keys in the PingFederate documentation.
component: github
page_id: github:github_emu_provisioner:pf_gh_emu_connector_obtain_pf_signing_cert
canonical_url: https://docs.pingidentity.com/integrations/github/github_emu_provisioner/pf_gh_emu_connector_obtain_pf_signing_cert.html
llms_txt: https://docs.pingidentity.com/integrations/github/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 25, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Obtain PingFederate signing certificate

## About this task

The following are the steps to obtain the signing certificate used for the digital signature verification of the PingFederate IdP. When asked during [Configure GitHub for provisioning and SSO](pf_gh_emu_configure_github_for_provisioning_and_sso.html), provide the certificate that you have downloaded from PingFederate. Learn more in [Managing digital signing certificates and decryption keys](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_certmanagementtasklet_dsigsigningcert_certmanagementstate.html) in the PingFederate documentation.

To export an existing certificate:

## Steps

1. Sign onto the **PingFederate administrative console** as an administrative user for your organization.

2. Go to **Server Configuration > Certificate Management > Signing & Decryption Keys & Certificates**.

3. Click **Export** under **Action** for the certificate you want to export.

4. On the **Export Certificate** page, select **Certificate Only** export and then click **Next**.

5. On the **Export & Summary** page, click **Export** to save the certificate file on your system.

6. When finished, click **Done**.

7. Click **Cancel** to go back to the **Server Configuration** screen.

---

---
title: Obtain PingFederate signing certificate
description: The following are the steps to obtain the signing certificate used for the digital signature verification of the PingFederate IdP. When asked during Configure GitHub for provisioning and SSO, provide the certificate that you have downloaded from PingFederate. Learn more in Managing digital signing certificates and decryption keys in the PingFederate documentation.
component: github
page_id: github:github_provisioner:pf_github_connector_obtain_pf_signing_certificate
canonical_url: https://docs.pingidentity.com/integrations/github/github_provisioner/pf_github_connector_obtain_pf_signing_certificate.html
llms_txt: https://docs.pingidentity.com/integrations/github/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 25, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Obtain PingFederate signing certificate

## About this task

The following are the steps to obtain the signing certificate used for the digital signature verification of the PingFederate IdP. When asked during [Configure GitHub for provisioning and SSO](pf_github_connector_configure_github_for_provisioning_and_sso.html), provide the certificate that you have downloaded from PingFederate. Learn more in [Managing digital signing certificates and decryption keys](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_certmanagementtasklet_dsigsigningcert_certmanagementstate.html) in the PingFederate documentation.

To export an existing certificate:

## Steps

1. Sign onto the **PingFederate administrative console** as an administrative user for your organization.

2. Go to **Server Configuration > Certificate Management > Signing & Decryption Keys & Certificates**.

3. Click **Export** under **Action** for the certificate you want to export.

4. On the **Export Certificate** page, select **Certificate Only** export and then click **Next**.

5. On the **Export & Summary** page, click **Export** to save the certificate file on your system.

6. When finished, click **Done**.

7. Click **Cancel** to go back to the **Server Configuration** screen.

---

---
title: Obtaining PingFederate SAML 2.0 metadata
description: To configure GitHub for provisioning and SSO, you will require the below information. These values can be obtained from your PingFederate Identity Provider (IdP) metadata. Learn more in Exporting connection-specific SAML metadata
component: github
page_id: github:github_emu_provisioner:pf_github_emu_connector_obtain_pf_saml_20_metadata
canonical_url: https://docs.pingidentity.com/integrations/github/github_emu_provisioner/pf_github_emu_connector_obtain_pf_saml_20_metadata.html
llms_txt: https://docs.pingidentity.com/integrations/github/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 27, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Obtaining PingFederate SAML 2.0 metadata

## About this task

To configure GitHub for provisioning and SSO, you will require the below information. These values can be obtained from your PingFederate Identity Provider (IdP) metadata. Learn more in [Exporting connection-specific SAML metadata](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_exportmetadatatasklet_exportconnectionstate.html)

* PingFederate SAML Endpoint

  * Example: `https://<pf_hostname>:<pf_port>/idp/SSO.saml2`

* Identity Provider Issuer

  * This is SAML 2.0 Entity ID from PingFederate.

**To export your IdP metadata**:

## Steps

1. Go to the **Server Configuration > Metadata Export** screen.

2. On the Metadata Mode screen, choose Select information to include in metadata manually and click Next.

3. On the Protocol screen, click Next.

4. On the Attribute Contract screen, click Next.

5. On the Signing Key screen, select the PingFederate signing certificate for use and click Next.

6. On the Metadata Signing screen, click Next.

7. On the XML Encryption Certificate screen, click Next.

8. On the Export & Summary screen, click Export to and save the metadata XML file for later use.

---

---
title: Obtaining PingFederate SAML 2.0 metadata
description: To configure GitHub for provisioning and SSO, you will require the below information. These values can be obtained from your PingFederate Identity Provider (IdP) metadata. Learn more in Exporting connection-specific SAML metadata
component: github
page_id: github:github_provisioner:pf_github_connector_obtain_pf_saml_20_metadata
canonical_url: https://docs.pingidentity.com/integrations/github/github_provisioner/pf_github_connector_obtain_pf_saml_20_metadata.html
llms_txt: https://docs.pingidentity.com/integrations/github/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 27, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Obtaining PingFederate SAML 2.0 metadata

## About this task

To configure GitHub for provisioning and SSO, you will require the below information. These values can be obtained from your PingFederate Identity Provider (IdP) metadata. Learn more in [Exporting connection-specific SAML metadata](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_exportmetadatatasklet_exportconnectionstate.html)

* PingFederate SAML Endpoint

  * Example: `https://<pf_hostname>:<pf_port>/idp/SSO.saml2`

* Identity Provider Issuer

  * This is SAML 2.0 Entity ID from PingFederate.

**To export your IdP metadata**:

## Steps

1. Go to the **Server Configuration > Metadata Export** screen.

2. On the Metadata Mode screen, choose Select information to include in metadata manually and click Next.

3. On the Protocol screen, click Next.

4. On the Attribute Contract screen, click Next.

5. On the Signing Key screen, select the PingFederate signing certificate for use and click Next.

6. On the Metadata Signing screen, click Next.

7. On the XML Encryption Certificate screen, click Next.

8. On the Export & Summary screen, click Export to and save the metadata XML file for later use.

---

---
title: Overview of GitHub integrations
description: The PingFederate GitHub Login Integration Kit allows PingFederate to use GitHub as an identity provider (IdP). This allows users to access service provider (SP) applications by signing onto GitHub.
component: github
page_id: github::pf_is_overview_of_github_integrations
canonical_url: https://docs.pingidentity.com/integrations/github/pf_is_overview_of_github_integrations.html
llms_txt: https://docs.pingidentity.com/integrations/github/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: November 4, 2025
section_ids:
  github-login-integration-kit-formerly-the-github-cloud-identity-connector: GitHub Login Integration Kit (formerly the GitHub Cloud Identity Connector)
  github-provisioner-also-called-the-github-connector: GitHub Provisioner (also called the GitHub Connector)
  github-emu-provisioner-also-called-the-github-emu-connector: GitHub EMU Provisioner (also called the GitHub EMU Connector)
---

# Overview of GitHub integrations

## GitHub Login Integration Kit (formerly the GitHub Cloud Identity Connector)

The PingFederate GitHub Login Integration Kit allows PingFederate to use GitHub as an identity provider (IdP) *(tooltip: \<div class="paragraph">
\<p>A service that manages identity information and provides authentication services to relying clients or SPs within a federated or distributed network.\</p>
\</div>)*. This allows users to access service provider (SP) *(tooltip: \<div class="paragraph">
\<p>In SAML, an entity that receives and accepts an authentication assertion issued by an IdP, typically for the purpose of allowing access to a protected resource.\</p>
\</div>)* applications by signing onto GitHub.

## GitHub Provisioner (also called the GitHub Connector)

The PingFederate GitHub Provisioner enables an enterprise to provision users to GitHub.

* Requires a GitHub Enterprise or One plan with SAML SSO enabled.

* A quick connection template is included to simplify the configuration of single sign-on (SSO) *(tooltip: \<div class="paragraph">
  \<p>The process of authenticating an identity (signing on) at one website (usually with a user ID and password) and then accessing resources secured by other domains without reauthenticating.\</p>
  \</div>)*.

## GitHub EMU Provisioner (also called the GitHub EMU Connector)

The PingFederate GitHub Enterprise Managed Users (EMU) Provisioner enables an enterprise to provision users *and groups* to GitHub.

* Requires a GitHub Enterprise Cloud account with Enterprise Managed Users and SAML SSO enabled.

* A quick connection template is included to simplify the configuration of SSO.

---

---
title: Overview of the SSO flow
description: With the GitHub Login Integration Kit, PingFederate includes the GitHub authentication API in the sign-on flow.
component: github
page_id: github:github_login_integration_kit:pf_github_cic_overview_of_the_sso_flow
canonical_url: https://docs.pingidentity.com/integrations/github/github_login_integration_kit/pf_github_cic_overview_of_the_sso_flow.html
llms_txt: https://docs.pingidentity.com/integrations/github/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 25, 2024
section_ids:
  description: Description
---

# Overview of the SSO flow

With the GitHub Login Integration Kit, PingFederate includes the GitHub authentication API in the sign-on flow.

The following figure illustrates a service provider (SP)-initiated single sign-on (SSO) scenario in which PingFederate authenticates users to an SP application using the GitHub IdP Adapter.

![Diagram showing the SSO flow using the GitHub IdP Adapter.](_images/github-login-ik-sso-flow-overview-diagram.png)

## Description

1. The user opens a web application and chooses the GitHub sign-on option.

2. The sign-on link points to the GitHub IdP Adapter, which redirects the browser to GitHub with the client ID and a list of requested permissions.

3. On GitHub, the user authenticates their identity and then authorizes the requested permissions.

4. GitHub redirects the browser…​

5. …​to the GitHub IdP Adapter authorization callback endpoint with an authorization code.

   If the user fails to authenticate or doesn't authorize the request, the response includes an error code instead.

6. PingFederate sends GitHub the **Client ID**, **Client Secret**, authorization code, and the PingFederate **Authorization Callback Endpoint**.

7. GitHub returns an access token.

8. PingFederate sends GitHub a request for user attributes and presents the access token.

9. GitHub verifies the access token and provides the user information.

10. PingFederate redirects the user to the web application with the user attributes.

---

---
title: Registering PingFederate as an OAuth application in GitHub
description: To allow PingFederate to process social sign-on requests with GitHub, add PingFederate as an OAuth application in the GitHub administrative console.
component: github
page_id: github:github_login_integration_kit:pf_github_cic_registering_pf_as_an_oauth_application_in_github
canonical_url: https://docs.pingidentity.com/integrations/github/github_login_integration_kit/pf_github_cic_registering_pf_as_an_oauth_application_in_github.html
llms_txt: https://docs.pingidentity.com/integrations/github/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: November 4, 2025
section_ids:
  steps: Steps
---

# Registering PingFederate as an OAuth application in GitHub

To allow PingFederate to process social sign-on requests with GitHub, add PingFederate as an OAuth application in the GitHub administrative console.

## Steps

1. Sign on to the GitHub [App settings page](https://github.com/settings/apps) using a GitHub account.

2. Click the **OAuth Apps** tab, then click **New OAuth app**.

3. On the **Register a new OAuth app** page:

   1. In the **Application name** field, enter a name, such as `PingFederate`.

   2. In the **Homepage URL**, enter the hostname (or virtual hostname) and port of your PingFederate server, such as `https://pf.example.com:9031`.

   3. (Optional) In the **Application Description** field, enter a description of the application.

   4. In the **Authorization callback URL** field, enter the hostname (or virtual hostname) and port of your PingFederate server followed by the GitHub IdP Adapter instance endpoint, such as `https://pf.example.com:9031/ext/github-authn`.

      |   |                                                                                                                                                                                                                                                                                        |
      | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      |   | The default endpoint is `/github-authn`. If you set a custom endpoint here, enter the matching value in the **Authorization Callback Endpoint** field of your adapter instance configuration in [Configuring an adapter instance](pf_github_cic_configuring_an_adapter_instance.html). |

   5. (Optional) If you want to use GitHub's device flow to perform additional authorization, select the **Enable Device Flow** checkbox.

      |   |                                                                                                                                                                                                                                                                          |
      | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
      |   | You can find more information in [Device Flow](https://docs.github.com/en/apps/oauth-apps/building-oauth-apps/authorizing-oauth-apps#device-flow) in the GitHub documentation.Using device flow isn't required to include the GitHub authentication API in the SSO flow. |

   6. Click **Register application**.

4. On the **OAuth application** page, note the **Client ID** field, then enter the hostname (or virtual hostname and **Client Secret**) to use in [Configuring an adapter instance](pf_github_cic_configuring_an_adapter_instance.html).

---

---
title: Supported attributes reference
description: The following table consists of the attributes that can be mapped for user provisioning. Find more information about available attributes in SCIM in the GitHub documentation.
component: github
page_id: github:github_emu_provisioner:pf_gh_emu_supported_attributes_ref
canonical_url: https://docs.pingidentity.com/integrations/github/github_emu_provisioner/pf_gh_emu_supported_attributes_ref.html
llms_txt: https://docs.pingidentity.com/integrations/github/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 25, 2024
---

# Supported attributes reference

The following table consists of the attributes that can be mapped for user provisioning. Find more information about available attributes in [SCIM](https://docs.github.com/en/enterprise-cloud@latest/rest/enterprise-admin/scim?apiVersion=2022-11-28#about-scim) in the GitHub documentation.

| Attribute      | Description                                                                                                                                                                                                                                                                                                                                                                                          |
| -------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Username       | GitHub's unique identifier for the user. This attribute is required.&#xA;&#xA;GitHub usernames can't exceed 39 characters. This character limit includes the underscore and short code that GitHub attaches to a normalized username.&#xA;&#xA;Find more information about username components and normalization in Username considerations for external authentication in the GitHub documentation. |
| Email          | The email for the user (for example, "bjensen\@example.com"). This attribute is required.                                                                                                                                                                                                                                                                                                            |
| External ID    | A string that is an identifier for the resource as defined by the provisioning client.&#xA;&#xA;External ID is mapped to a binary attribute ObjectGUID in AD, and needs to be added to PingFederate's binary attribute list in the Data Store.                                                                                                                                                       |
| First Name     | The given name of the user, or first name in most Western languages (for example, 'Barbara' given the full name 'Ms. Barbara Jane Jensen, III').                                                                                                                                                                                                                                                     |
| Last Name      | The family name of the user, or last name in most Western languages (for example, 'Jensen' given the full name 'Ms. Barbara Jane Jensen, III').                                                                                                                                                                                                                                                      |
| Display Name   | A human-readable name for a user.                                                                                                                                                                                                                                                                                                                                                                    |
| Formatted Name | The user's full name, including all middle names, titles and suffixes, formatted for display.                                                                                                                                                                                                                                                                                                        |
| Roles          | A list of the user's roles.For more information, see [Provision a SCIM enterprise user](https://github.com/en/enterprise-server@latest/rest/enterprise-admin/scim//) in the GitHub documentation.                                                                                                                                                                                                    |

---

---
title: Supported attributes reference
description: The following table consists of the attributes that can be mapped for user provisioning. For more information on available attributes, see SCIM in the GitHub documentation.
component: github
page_id: github:github_provisioner:pf_github_connector_supported_attributes_reference
canonical_url: https://docs.pingidentity.com/integrations/github/github_provisioner/pf_github_connector_supported_attributes_reference.html
llms_txt: https://docs.pingidentity.com/integrations/github/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 25, 2024
---

# Supported attributes reference

The following table consists of the attributes that can be mapped for user provisioning. For more information on available attributes, see [SCIM](https://developer.github.com/v3/scim/) in the GitHub documentation.

| Attribute   | Description                                                                                                                                                                  |
| ----------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Username    | GitHub's unique identifier for the user. This attribute is required.                                                                                                         |
| Email       | The email for the user (for example, `bjensen@example.com`). This attribute is required.                                                                                     |
| First Name  | The given name of the user, or first name in most Western languages (for example, 'Barbara' given the full name 'Ms. Barbara Jane Jensen, III'). This attribute is required. |
| Last Name   | The family name of the user, or last name in most Western languages (for example, 'Jensen' given the full name 'Ms. Barbara Jane Jensen, III'). This attribute is required.  |
| External ID | A string that is an identifier for the resource as defined by the provisioning client.                                                                                       |

---

---
title: User and group management
description: The GitHub EMU Provisioner synchronizes users and groups from your datastore to GitHub.
component: github
page_id: github:github_emu_provisioner:pf_github_emu_connector_user_and_group_management
canonical_url: https://docs.pingidentity.com/integrations/github/github_emu_provisioner/pf_github_emu_connector_user_and_group_management.html
llms_txt: https://docs.pingidentity.com/integrations/github/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: August 1, 2024
section_ids:
  user-provisioning: User provisioning
  user-updates: User updates
  user-deprovisioning: User deprovisioning
  group-provisioning: Group provisioning
  group-name-updates: Group name updates
  group-membership-updates: Group membership updates
  group-deletion: Group deletion
---

# User and group management

The GitHub EMU Provisioner synchronizes users and groups from your datastore to GitHub.

SCIM API provisioning calls sent from the PingFederate Enterprise Managed User (EMU) Provisioner create the users, groups, and group memberships in a GitHub EMU enterprise. If an EMU enterprise account hasn't been created via SCIM provisioning, PingFederate users cannot use a GitHub EMU account to login and access their GitHub EMU enterprise.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The GitHub EMU Provisioner sends a SCIM API `GET` call with a `<SCIM User ID>` value of `0` to `/scim/v2/enterprises/<enterprise>/Users/<SCIM User ID>` as part of a connection check that's performed before every provisioning operation. This `GET` call causes `404` errors in the PingFederate and GitHub enterprise logs, because there isn't a `<SCIM User ID>` with a value of `0`. These error messages can be safely ignored. This is expected behavior and it does not indicate an issue. |

|   |                                                                                                                                                                                                                                 |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | You can configure the following capabilities and specify which users to provision during the [Configure PingFederate for provisioning and SSO](pf_gh_emu_configure_pf_for_provisioning_and_sso.html) part of the setup process. |

## User provisioning

PingFederate provisions users if a user is added to the datastore group or filter that is targeted by the provisioner.

You can define which users PingFederate targets for provisioning on the **Source Location** tab of your provisioning connection configuration. You can find more information in [Specifying a source location](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_saaschanneltasklet_saassourcelocationstate.html).

## User updates

PingFederate updates users when a user attribute changes in your datastore.

You can define which attributes PingFederate monitors for changes on the **Attribute Mapping** tab of your provisioning connection configuration.

## User deprovisioning

PingFederate deprovisions users if:

* A user is suspended from the user store.

* A user is disabled in the user store.

* A user is removed from the datastore group or filter targeted by the provisioner.

When the **Remove User Action** setting in the connection configuration is set to **Disable**, PingFederate sends a `PATCH` SCIM deprovisioning call to GitHub for an enterprise managed user, and the user account gets suspended in the GitHub enterprise. If the same user account in the datastore is re-provisioned, the enterprise managed user account becomes unsuspended.

|   |                                                                                                                                                                                                                                                                                                                                                                                                               |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Make sure to configure this setting for **Disable**. If the **Remove User Action** setting is set to **Delete**, PingFederate sends a `DELETE` SCIM deprovisioning call to GitHub for an enterprise managed user, and the user account gets suspended in the GitHub enterprise. If the same user account in the datastore is re-provisioned, the enterprise managed user account does not become unsuspended. |

## Group provisioning

PingFederate provisions groups when you add a group to the datastore filter that is targeted by the provisioner. You can define which groups PingFederate targets for provisioning and monitors for changes on the **Source Location** tab in your provisioner configuration.

After you successfully provision a group to a GitHub EMU enterprise, an enterprise owner can see the group by following the steps in [this GitHub article](https://docs.github.com/en/enterprise-cloud@latest/admin/identity-and-access-management/provisioning-user-accounts-for-enterprise-managed-users/managing-team-memberships-with-identity-provider-groups#viewing-idp-groups-group-membership-and-connected-teams). When mapping a team in the GitHub EMU enterprise to a group, an EMU organization owner makes selections from the list of groups that are provisioned to the enterprise.

## Group name updates

PingFederate renames groups when they are renamed in the datastore.

## Group membership updates

PingFederate updates group memberships when memberships change in the datastore, regardless of whether the change is in the group's properties or a user's properties.

Group memberships in the datastore overwrite the group memberships in GitHub.

## Group deletion

PingFederate deletes groups if:

* The group is deleted in the datastore.

* The group is removed from the datastore group or filter targeted by the provisioner.

|   |                                                     |
| - | --------------------------------------------------- |
|   | Group deletions are permanent and cannot be undone. |

---

---
title: User management
description: The GitHub Provisioner synchronizes users from your datastore to GitHub. The behavior of each provisioning capability is described below.
component: github
page_id: github:github_provisioner:pf_github_connector_user_management
canonical_url: https://docs.pingidentity.com/integrations/github/github_provisioner/pf_github_connector_user_management.html
llms_txt: https://docs.pingidentity.com/integrations/github/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 25, 2024
section_ids:
  synchronizing-existing-users: Synchronizing existing users
  user-provisioning: User provisioning
  user-updates: User updates
  user-deprovisioning: User deprovisioning
---

# User management

The GitHub Provisioner synchronizes users from your datastore to GitHub. The behavior of each provisioning capability is described below.

You can configure these capabilities in the [Configure PingFederate for provisioning and SSO](pf_github_connector_configure_pf_for_provisioning_and_sso.html) step of the setup process.

## Synchronizing existing users

PingFederate synchronizes users based on the `Username` attribute in GitHub. If a user already exists in your datastore and GitHub, mapping this attribute correctly links the two records together.

For example:

* In GitHub, Janet's `Username` is `bjensen@example.com`.

* In your datastore, Janet's `mail` is `bjensen@example.com`.

* On the **Attribute Mapping** tab of your provisioning connection configuration, you map the `Username` attribute to `mail`.

* When the provisioning connector runs, the datastore user is provisioned with a `Username` of `bjensen@example.com`. That matches Janet's existing `Username` in GitHub, so her information in the datastore is synchronized to her GitHub account.

## User provisioning

PingFederate provisions users when one of the following happens:

* A user is added to the datastore group or filter that is targeted by the provisioning connector.

The **Source Location** tab of your provisioning connection configuration defines which users PingFederate targets for provisioning.

## User updates

PingFederate updates users when a user attribute changes in your datastore.

The **Attribute Mapping** tab of your provisioning connection configuration defines which attributes PingFederate monitors for changes.

## User deprovisioning

PingFederate deprovisions users when one of the following happens:

* A user is deleted from the user store.

* A user is disabled in the user store.

* A user is removed from the datastore group or filter that is targeted by the provisioning connector.