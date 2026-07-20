---
title: Authentication API Support
description: You can use the PingFederate authentication API to integrate the GitHub IdP Adapter into your application.
component: github
page_id: github:github_login_integration_kit:pf_github_cic_authentication_api_support
canonical_url: https://docs.pingidentity.com/integrations/github/github_login_integration_kit/pf_github_cic_authentication_api_support.html
llms_txt: https://docs.pingidentity.com/integrations/github/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 25, 2024
---

# Authentication API Support

You can use the PingFederate authentication API to integrate the GitHub IdP Adapter into your application.

The PingFederate Authentication API provides access to the current state of the authentication flow as a user steps through the PingFederate authentication policy. You can find more information in [PingFederate authentication API](https://docs.pingidentity.com/pingfederate/latest/developers_reference_guide/pf_authentication_api.html) in the PingFederate documentation.

To integrate the GitHub IdP Adapter into your authentication flow, configure your application based on the states, actions, and models available in the PingFederate Authentication API Explorer. Learn more in [Exploring the Authentication API](https://docs.pingidentity.com/pingfederate/latest/developers_reference_guide/pf_exploring_authentication_api.html) in the PingFederate documentation.

---

---
title: Available user attributes
description: GitHub supports a multitude of attributes. The following table describes the most important ones.
component: github
page_id: github:github_login_integration_kit:pf_github_cic_available_user_attributes
canonical_url: https://docs.pingidentity.com/integrations/github/github_login_integration_kit/pf_github_cic_available_user_attributes.html
llms_txt: https://docs.pingidentity.com/integrations/github/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: November 3, 2025
---

# Available user attributes

GitHub supports a multitude of attributes. The following table describes the most important ones.

You can find an example payload in [JSON Pointer syntax reference](pf_github_cic_json_pointer_syntax_reference.html).

| Attribute       | Description                                                                                                                                                                                                                                  |
| --------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `access_token`  | The access token that GitHub provides to your application.                                                                                                                                                                                   |
| `email`         | The user's public email address, as shown on their GitHub profile page.                                                                                                                                                                      |
| `emails`        | The complete list of email addresses associated with the user, including primary, public, and other addresses. This data is retrieved from the email endpoint and requires the `email` scope. The result is a JSON array stored as a string. |
| `id`            | The unique ID for the user. This ID is only used in the context of your application.                                                                                                                                                         |
| `name`          | The user's name, as shown on the user's GitHub profile page.                                                                                                                                                                                 |
| `primary_email` | The user's email address that's marked as primary. This value is only available with the `email` scope.                                                                                                                                      |
| `username`      | The user's GitHub username.                                                                                                                                                                                                                  |

---

---
title: Changelog
description: Added a second SAML metadata file to handle the new GitHub EMU Entity ID and URL that point to https://<enterprise_slug>.ghe.com. These changes were introduced to handle data residency requirements.
component: github
page_id: github:github_emu_provisioner:pf_gh_emu_connector_changelog
canonical_url: https://docs.pingidentity.com/integrations/github/github_emu_provisioner/pf_gh_emu_connector_changelog.html
llms_txt: https://docs.pingidentity.com/integrations/github/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 25, 2024
section_ids:
  github-emu-provisoner-1-0-0-7-november-2024: GitHub EMU Provisoner 1.0.0.7 – November 2024
  github-emu-provisoner-1-0-april-2023: GitHub EMU Provisoner 1.0 – April 2023
---

# Changelog

## GitHub EMU Provisoner 1.0.0.7 – November 2024

* Added a second SAML metadata file to handle the new GitHub EMU **Entity ID** and URL that point to `https://<enterprise_slug>.ghe.com`. These changes were introduced to handle data residency requirements.

  |   |                                                                                                                                                                                                                                              |
  | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | The SAML metadata file that you select during setup pre-populates part of the adapter configuration. Learn more in steps 5 and 7 of [Configure PingFederate for provisioning and SSO](pf_gh_emu_configure_pf_for_provisioning_and_sso.html). |

## GitHub EMU Provisoner 1.0 – April 2023

* Initial release.

---

---
title: Changelog
description: The following is the change history for the GitHub Login Integration Kit.
component: github
page_id: github:github_login_integration_kit:pf_github_cic_changelog
canonical_url: https://docs.pingidentity.com/integrations/github/github_login_integration_kit/pf_github_cic_changelog.html
llms_txt: https://docs.pingidentity.com/integrations/github/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: February 19, 2026
section_ids:
  version-1-1-2-january-2026: Version 1.1.2 - January 2026
  version-1-1-1-november-2025: Version 1.1.1 - November 2025
  version-1-1-november-2020: Version 1.1 – November 2020
  version-1-0-august-2019: Version 1.0 – August 2019
---

# Changelog

The following is the change history for the GitHub Login Integration Kit.

## Version 1.1.2 - January 2026

* Removed third-party fonts and the `authn-api-messages.properties` file.

## Version 1.1.1 - November 2025

* Updated Apache Commons Text library version to address a potential security vulnerability.

## Version 1.1 – November 2020

* Added a setting to use browser redirect or pop-up window for the sign-on presentation.

* Added customizable sign-on templates for the pop-up window presentation.

* Added customizable user-facing language-pack messages.

* Added support for the [PingFederate authentication API](https://docs.pingidentity.com/pingfederate/latest/developers_reference_guide/pf_authentication_api.html).

* Added support for the [JavaScript Widget for the PingFederate Authentication API](https://github.com/pingidentity/pf-authn-js-widget).

## Version 1.0 – August 2019

* Initial release.

* Added support for social login using GitHub credentials.

* Added support for retrieving GitHub user and email information.

* Added support for overriding or adding default mappings between local attributes and GitHub attributes from the core or extended contract.

* Added the ability to configure when to retry a failed request.

* Added the ability to configure the maximum number of retries to perform.

* Added the ability to override the system-default proxy settings.

* Added the ability to configure API connection timeout settings.

* Added the ability to override GitHub API endpoints.

---

---
title: Changelog
description: Initial release
component: github
page_id: github:github_provisioner:pf_github_connector_changelog
canonical_url: https://docs.pingidentity.com/integrations/github/github_provisioner/pf_github_connector_changelog.html
llms_txt: https://docs.pingidentity.com/integrations/github/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 25, 2024
section_ids:
  github-connector-1-0-july-2018-current-release: GitHub Connector 1.0 – July 2018 (current release)
---

# Changelog

## GitHub Connector 1.0 – July 2018 (current release)

* Initial release

* Added support for user life cycle management (including creates, updates and deletes)

* Added configuration options for workflow capabilities (for example, the ability to disable updates)

---

---
title: Configure GitHub for provisioning and SSO
description: Complete the following task to enable provisioning and single sign-on (SSO) on the GitHub Admin Portal.
component: github
page_id: github:github_emu_provisioner:pf_gh_emu_configure_github_for_provisioning_and_sso
canonical_url: https://docs.pingidentity.com/integrations/github/github_emu_provisioner/pf_gh_emu_configure_github_for_provisioning_and_sso.html
llms_txt: https://docs.pingidentity.com/integrations/github/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 25, 2024
section_ids:
  before-you-begin: Before you begin
  about-this-task: About this task
  steps: Steps
---

# Configure GitHub for provisioning and SSO

Complete the following task to enable provisioning and single sign-on (SSO) *(tooltip: \<div class="paragraph">
\<p>The process of authenticating an identity (signing on) at one website (usually with a user ID and password) and then accessing resources secured by other domains without reauthenticating.\</p>
\</div>)* on the GitHub Admin Portal.

## Before you begin

To get the values that you need to configure a SAML integration in GitHub:

* [Obtaining PingFederate SAML 2.0 metadata](pf_github_emu_connector_obtain_pf_saml_20_metadata.html)

* [Obtain PingFederate signing certificate](pf_gh_emu_connector_obtain_pf_signing_cert.html)

## About this task

You must configure the SAML integration before you configure the SCIM provisioning integration in GitHub. SCIM provisioning calls fail with a `404` error if SAML authentication is not configured.

## Steps

* Sign on to GitHub and follow the [Configuring your enterprise](https://github.com/en/enterprise-cloud@latest/admin/identity-and-access-management/using-enterprise-managed-users-for-iam/configuring-saml-single-sign-on-for-enterprise-managed-users//) instructions in the GitHub documentation:

  1. For steps 7 and 8, enter the values that you collected in the [Obtaining PingFederate SAML 2.0 metadata](pf_github_emu_connector_obtain_pf_saml_20_metadata.html) procedure.

  2. For step 9, paste the certificate that you exported in the [Obtain PingFederate signing certificate](pf_gh_emu_connector_obtain_pf_signing_cert.html) procedure.

---

---
title: Configure GitHub for provisioning and SSO
description: Below are the tasks to enable provisioning and single sign-on (SSO) on the GitHub Admin Portal.
component: github
page_id: github:github_provisioner:pf_github_connector_configure_github_for_provisioning_and_sso
canonical_url: https://docs.pingidentity.com/integrations/github/github_provisioner/pf_github_connector_configure_github_for_provisioning_and_sso.html
llms_txt: https://docs.pingidentity.com/integrations/github/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 25, 2024
section_ids:
  before-you-begin: Before you begin
  about-this-task: About this task
  steps: Steps
---

# Configure GitHub for provisioning and SSO

## Before you begin

Below are the tasks to enable provisioning and single sign-on (SSO) on the GitHub Admin Portal.

|   |                                                                                                                                                                                       |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The SCIM API is only available on the GitHub "Enterprise" and "One" plans with SAML SSO enabled. For more information, see [SCIM REST API v3](https://developer.github.com/v3/scim/). |

To configure GitHub for provisioning and SSO you will require both metadata and signing certificate from your PingFederate Identity Provider (IdP) setup. For more information, see [Obtaining PingFederate SAML 2.0 metadata](pf_github_connector_obtain_pf_saml_20_metadata.html) and [Obtain PingFederate signing certificate](pf_github_connector_obtain_pf_signing_certificate.html).

## About this task

To configure GitHub for provisioning and SSO:

|   |                                                                                                                                                                                                                                                           |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | For more information on how to set up SSO for GitHub, see [Enabling and testing SAML single sign-on for your organization](https://help.github.com/articles/enabling-and-testing-saml-single-sign-on-for-your-organization/) in the GitHub documentation. |

## Steps

1. Log into your GitHub account as an administrative user for your organization.

2. In the top right corner of GitHub, click your profile photo, then click Your profile.

   ![An image of the GitHub profile menu options.](_images/gws1563995343086.png)

3. On the left side of your profile page, under Organizations, click the icon for your organization.

   ![An image of the GitHub organization icon.](_images/exd1563995343571.png)

4. Under your organization name, click Settings.

   ![An image of the GitHub organization settings menu.](_images/gzb1563995344049.png)

5. In the organization settings sidebar, click Security.

   ![An image of Security in the settings menu.](_images/jhr1563995348266.png)

6. Under SAML single sign-on, select Enable SAML authentication.

   ![An image of the SAML single sign-on checkbox.](_images/jnq1563995348754.png)

   |   |                                                                                                                                                                                                                                                                                                                                                                                         |
   | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | After enabling SAML SSO, you can download your single sign-on recovery codes so that you can access your organization even if your IdP is unavailable. For more information, see [Downloading your organization's SAML single sign-on recovery codes](https://help.github.com/articles/downloading-your-organization-s-saml-single-sign-on-recovery-codes) in the GitHub documentation. |

7. Open your PingFederate metadata XML file using a text editor.

8. In the Sign on URL field, type the HTTPS endpoint of your IdP for single sign-on requests. This value is the SingleSignOnService POST binding available in your PingFederate metadata file. For example, `https://<pf_hostname>:<pf_port>/idp/SSO.saml2`

9. **Optional:** In the Issuer field, type your SAML issuer's name. This verifies the authenticity of sent messages. This value is `entityID` available in your PingFederate metadata file.

10. Open your PingFederate signing certificate file using a text editor.

11. Under Public Certificate, paste your PingFederate signing certificate used to verify SAML responses.

    |   |                                                                                                                                                                 |
    | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    |   | GitHub requires the public certificate to be a valid x509 formatted certificate enclosed between `-----BEGIN CERTIFICATE-----` and `-----END CERTIFICATE-----`. |

12. Click the pencil icon to edit the Signature Method and Digest Method drop-downs, choose the hashing algorithm used by PingFederate issuer to verify the integrity of the requests.

13. Before enabling SAML SSO for your organization, click Test SAML configuration to ensure that the information you have entered is correct.

    |   |                                                                                                                                                                                                                                                                              |
    | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    |   | To enforce SAML SSO and remove all organization members who haven't authenticated via your IdP, see [Enforcing SAML single sign-on for your organization](https://help.github.com/articles/enforcing-saml-single-sign-on-for-your-organization) in the GitHub documentation. |

14. Click Save to complete the SAML single sign-on configuration.

---

---
title: Configure PingFederate for provisioning and SSO
description: Configure a service provider (SP) connection in PingFederate to manage outbound provisioning and single sign-on (SSO) to GitHub.
component: github
page_id: github:github_emu_provisioner:pf_gh_emu_configure_pf_for_provisioning_and_sso
canonical_url: https://docs.pingidentity.com/integrations/github/github_emu_provisioner/pf_gh_emu_configure_pf_for_provisioning_and_sso.html
llms_txt: https://docs.pingidentity.com/integrations/github/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 25, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
  choose-from: Choose from:
  choose-from-2: Choose from:
  example: Example:
---

# Configure PingFederate for provisioning and SSO

Configure a service provider (SP) *(tooltip: \<div class="paragraph">
\<p>In SAML, an entity that receives and accepts an authentication assertion issued by an IdP, typically for the purpose of allowing access to a protected resource.\</p>
\</div>)* connection in PingFederate to manage outbound provisioning and single sign-on (SSO) *(tooltip: \<div class="paragraph">
\<p>The process of authenticating an identity (signing on) at one website (usually with a user ID and password) and then accessing resources secured by other domains without reauthenticating.\</p>
\</div>)* to GitHub.

## About this task

Outbound provisioning details are managed within an SP connection and can be added to an existing SP connection.

|   |                                                                                                                                                                                                                                                                               |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The SCIM API requires that you have GitHub Enterprise Cloud with SAML SSO enabled for the enterprise. Learn more in [About SCIM](https://docs.github.com/en/enterprise-cloud@latest/rest/enterprise-admin/scim?apiVersion=2022-11-28#about-scim) in the GitHub documentation. |

## Steps

1. In the PingFederate administrative console, configure the datastore that PingFederate will use as the source of user data.

   You can find configuration instructions in [Datastores](https://docs.pingidentity.com/pingfederate/latest/introduction_to_pingfederate/pf_datastores.html) in the PingFederate documentation.

   |   |                                                                                                                                                                                                                                           |
   | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | On the **Data Store Type** tab, you must select **Directory (LDAP)** as the **Type**. GitHub EMU enterprises require SCIM provisioning, and **Directory (LDAP)** is the only datastore type supported for PingFederate SCIM provisioning. |

2. Create a new SP connection or select an existing SP connection from the **SP Connections** page.

3. On the **Connection Template** tab, select **Use a template for this connection**.

4. In the **Connection Template** list, select **GitHub EMU Connector**.

   |   |                                                                                                                                                                                                                     |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | You must select **GitHub EMU Connector**, not **GitHub Connector**. This integration only supports the EMU connector.If this selection isn't available, verify the connector installation and restart PingFederate. |

   ![Screen capture of the connection template tab showing the Use a Template for This Connection option selected and the GitHub EMU Connector selected in the Connection Template field.](_images/drt1682096317796.png)

5. In the **Metadata File** section, import one of the following metadata files.

   ### Choose from:

   * The enterprise's SAML metadata, which you can download at either of the following URLs:

     * https\://github.com/enterprises/*\<enterprise\_slug>*/saml/metadata

     * https\://*\<enterprise\_slug>*.ghe.com/enterprises/*\<enterprise\_slug>*/saml/metadata for EMU data residency

   * Either of the sample metadata files that are packaged with the GitHub EMU Connector:

     * `github-emu-saml-metadata.xml`

     * `github-emu-saml-enterprises-metadata.xml` for EMU data residency

6. On the **Connection Type** tab, ensure that both the **Outbound Provisioning** and **Browser SSO Profiles** check boxes are selected.

7. On the **General Info** tab, enter your corresponding enterprise name in the **Partner's Entity ID (Connection ID)** field, then click **Next**.

   |   |                                                                                                         |
   | - | ------------------------------------------------------------------------------------------------------- |
   |   | The default values on the **General Info** tab are from the metadata file that you selected previously. |

   Use the following format:

   ### Choose from:

   * https\://github.com/enterprises/*\<enterprise\_slug>*

     ![Screen capture of the General Info tab with the Partner's Entity ID, Connection Name, and Base URL fields populated.](_images/dky1682096702850.png)

   * https\://*\<enterprise\_slug>*.ghe.com/enterprises/*\<enterprise\_slug>* for EMU data residency

     ![Screen capture of the General Info tab with the Partner's Entity ID, Connection Name, and Base URL fields populated.](_images/updated_entityID.png)

8. On the **Browser SSO** tab, configure your browser SSO settings.

   Learn more about configuring browser SSO in the following sections of [Identity provider SSO configuration](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_ident_provid_sso_config.html):

   * [Managing IdP adapters](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_managing_idp_adapters.html)

   * [Configuring IdP Browser SSO](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_spconnectionconfigtasklet_spbrowserssostate.html)

     1. Click **Configure Browser SSO**.

     2. On the **Assertion Creation** tab, click **Next**.

     3. On the **Protocol Settings** tab, click **Configure Protocol Settings**.

     4. On the **Summary** tab, click **Assertion Consumer Service URL**, edit the existing entry on the **Assertion Consumer Service URL** page, and enter the **Endpoint URL** corresponding to your enterprise name.

        ### Example:

        * `https://github.com/enterprises/<enterprise slug>/saml/consume`

        * `https://<enterprise_slug>.ghe.com/enterprises/<enterprise_slug>/saml/consume` for EMU data residency

     5. Click **Update** and **Done**, then click **Done** on the **Protocol Settings** tab.

9. On the **Credentials** tab, click **Configure Credentials**, then go to the **Digital Signature Settings** tab, select the signing certificate, and click **Done**, then **Next**.

10. On the **Outbound Provisioning** tab, click **Configure Provisioning**.

11. On the **Target** tab, enter the **Base URL** and **Access Token** values.

    |   |                                                                                                                                                                                                                                  |
    | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    |   | Do not change any of the default **Provisioning Options** for this integration. Make sure that **User Create**, **User Update**, and **User Disable/Delete** are selected and that **Remove User Action** is set to **Disable**. |

    ![Screen capture of the Target tab with the default provisioning options configured.](_images/zbc1682096732294.png)

    See the following table for instructions on how to configure the required values.

    | Field Name               | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
    | ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
    | **Base URL**             | The base URL for GitHub. For example:- `https://api.github.com/scim/v2/enterprises/<enterprise slug>`

    - `https://api.<enterprise_slug>.ghe.com/scim/v2/enterprises/<enterprise_slug>` for EMU data residency&#xA;&#xA;You can find information on how to determine your enterprise name in Accessing an enterprise in the GitHub documentation.                                                                                                             |
    | **Access Token**         | The access token that the provisioner uses to make authenticated API calls to GitHub.                                                                                                                                                                                                                                                                                                                                                                        |
    | **Provisioning Options** |                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
    | **User Create**          | * True (default)

      Users will be created in GitHub.

      &#xA;&#xA;Make sure that User Create is selected for this integration.

    * False

      Users will not be created in GitHub.

      &#xA;&#xA;The provisioner.log will display a warning within the create user workflow that the user was not created in GitHub.                                                                                                                                             |
    | **User Update**          | - True (default)

      Users will be updated in GitHub.

      &#xA;&#xA;Make sure that User Update is selected for this integration.

    - False

      Users will not be updated in GitHub.

      &#xA;&#xA;The provisioner.log will display a warning within the update user workflow that the user was not updated in GitHub.Enabling a previously suspended user in GitHub will trigger a create and as such, users can be enabled when **User Update** is not selected. |
    | **User Disable/Delete**  | * True (default)

      Users will be suspended or disabled in GitHub.

      &#xA;&#xA;Make sure that User Disable/Delete is selected for this integration.

    * False

      Users will not be suspended or disabled in GitHub.

      &#xA;&#xA;The provisioner.log will display a warning indicating that the user was not suspended in GitHub.                                                                                                                            |
    | **Remove User Action**   | - Disable (default)

      PingFederate disables the user in GitHub.

      &#xA;&#xA;Make sure that Disable is selected for this integration.

    - Delete

      PingFederate suspends the user in GitHub.The **Remove User Action** applies when **User Disable/Delete** is selected, and either:- A previously provisioned user no longer meets the condition set on the **Source Location** tab.

    - A user has been disabled or deleted from the datastore.            |

12. Click **Next**.

13. Configure a channel and complete the provisioning configuration.

    |   |                                                                                                                                                                                                                                                         |
    | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    |   | If you aren't ready to complete the provisioning configuration, you can click **Save** and return to the configuration page later. To return to the configuration page, select the connection from **Identity Provider > SP Connections > Manage All**. |

    Learn more in the following sections under [Configuring outbound provisioning](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_spconnectionconfigtasklet_saasprovisioningstate.html) in the PingFederate documentation:

    * [Managing channels](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_saasmanagementtasklet_saasmanagementstate.html)

    * [Specifying channel information](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_saaschanneltasklet_saasgeneralinfostate.html)

    * [Identifying the source datastore](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_saaschanneltasklet_saassourceselectionstate.html)

    * [Modifying source settings](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_saaschanneltasklet_saassourcesettingsstate.html)

    * [Specifying a source location](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_saaschanneltasklet_saassourcelocationstate.html)

    * [Mapping attributes](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_saaschanneltasklet_saasattrmappingmgmtstate.html)

    * [Reviewing channel settings](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_saaschanneltasklet_saasactivationstate.html)

      |   |                                                                                                                     |
      | - | ------------------------------------------------------------------------------------------------------------------- |
      |   | Credentials will be verified when the channel and SP connection is set to **Active** and provisioning is initiated. |

      1. Go to the **Manage Channels** tab and select the name of a channel to edit it.

      2. On the **Attribute Mapping** tab, edit the **Roles** field by clicking **Edit** in the **Action** column.

         ![Screen capture of the Attribute Mapping tab, with the Roles field name highlighted.](_images/clt1704471109056.png)

      3. After the **Attribute Mapping** window for the **Roles** field opens, map the **Roles** field to an LDAP attribute containing the value for the GitHub enterprise role that the user will have when they are provisioned.

         The LDAP attribute must contain one of the following string values:

         * `enterprise_owner`

         * `billing_manager`

         * `user`

         * `guest_collaborator`

      4. Click **Done**.

      5. After you finish mapping attributes, click **Next**.

      6. In the **Channel Status** section of the **Activation and Summary** tab, click **Active**.

      7. Click **Done**.

14. Link users authenticating through SAML to their provisioned SCIM identities in the GitHub enterprise.

    |   |                                                                                                                                                                                                                                                                                             |
    | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    |   | The SAML `NameID` and SCIM `userName` values must match for each user. Otherwise, a PingFederate user attempting to access their EMU account through SAML authentication might get a `404` error and an error message such as:```
    Enterprise Managed Users must be provisioned via SCIM
    ``` |

    To make sure that these values match in PingFederate:

    1. On the **Attribute Contract Fulfillment** tab, make sure that the **Value** of the `SAML_SUBJECT` contract attribute is `sAMAccountName` if you are using Active Directory as the LDAP datastore, or `username` if you are using another LDAP datastore like PingDirectory.

       To find the **Attribute Contract Fulfillment** tab:

       1. On the **Browser SSO** tab, click **Configure Browser SSO**.

       2. Go to the **Assertion Creation** tab and click **Configure Assertion Creation**.

       3. Go to the **Authentication Source Mapping** tab, click **Map New Adapter Instance**, and then go to the **Attribute Contract Fulfillment** tab.

    2. On the **Attribute Mapping** tab, make sure that the **Username** field is mapped to the same attribute value that the `SAML_SUBJECT` contract attribute is mapped to on the **Attribute Contract Fulfillment tab**. For example, this value might be `sAMAccountName` if you are using Active Directory, or `username` if you are using PingDirectory.

15. (Optional) Configure the **Synchronization Frequency** of your outbound provisioning channels.

    By default, PingFederate attempts to process user, group, and group member updates and send these updates to GitHub every 60 seconds. This interval is controlled by the **Synchronization Frequency** value, which affects all outbound provisioning channels.

    To update this value:

    1. Go to **System > Server > Protocol Settings** and select the **Outbound Provisioning** tab.

    2. Enter a new **Synchronization Frequency** value, then click **Save**.

    ![Screen capture of the Outbound Provisioning tab of the Protocol Settings page with the Synchronization Frequency field highlighted.](_images/wqy1704473490259.png)

---

---
title: Configure PingFederate for provisioning and SSO
description: To configure a connection for outbound provisioning and SSO to GitHub, follow the instructions in this section. Outbound provisioning details are managed within an SP connection and may be added to an existing SP connection.
component: github
page_id: github:github_provisioner:pf_github_connector_configure_pf_for_provisioning_and_sso
canonical_url: https://docs.pingidentity.com/integrations/github/github_provisioner/pf_github_connector_configure_pf_for_provisioning_and_sso.html
llms_txt: https://docs.pingidentity.com/integrations/github/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 25, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Configure PingFederate for provisioning and SSO

## About this task

To configure a connection for outbound provisioning and SSO to GitHub, follow the instructions in this section. Outbound provisioning details are managed within an SP connection and may be added to an existing SP connection.

|   |                                                                                                                                                                                         |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The SCIM API requires GitHub Enterprise Cloud with SAML SSO enabled for the organization. See [About SCIM](https://help.github.com/en/articles/about-scim) in the GitHub documentation. |

## Steps

1. In the PingFederate administrator console, configure the datastore that PingFederate will use as the source of user data. You can find instructions in [Datastores](https://docs.pingidentity.com/pingfederate/latest/introduction_to_pingfederate/pf_datastores.html) in the PingFederate documentation.

   * When targeting users and groups for provisioning, exclude the user account that you will use to administer users in your connection to GitHub. This prevents the PingFederate provisioning engine from interfering with the account that provisions users and groups.

2. Create a new SP connection or select an existing SP connection from the SP Configuration menu.

3. On the Connection Template page, select Use a template for this connection and select GitHub Connector in the Connection Template list. When asked during the connection configuration steps, import the `github-saml-metadata.xml` packaged with this connector.

   ![An image of the Connection Template screen.](_images/jje1563995351447.png)

   |   |                                                                                                 |
   | - | ----------------------------------------------------------------------------------------------- |
   |   | If this selection is not available, verify the connector installation and restart PingFederate. |

4. On the Connection Type page, ensure both the Outbound Provisioning and Browser SSO Profiles checkboxes are selected.

5. On the General Info page, the default values are taken from the metadata file you selected in step 2. In the Partner's Entity ID (Connection ID) field and update with your corresponding organization name.

   ![An image of the General Info screen.](_images/wbr1563995352379.png)

6. Click Next to continue the Browser SSO configuration. You can find more information in the following sections under [Identity provider SSO configuration](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_ident_provid_sso_config.html):

   * [Managing IdP adapters](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_managing_idp_adapters.html)

   * [Configure IdP Browser SSO](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_spconnectionconfigtasklet_spbrowserssostate.html)

7. On the Assertion Creation page, click Next.

8. On the Protocol Settings page, click Configure Protocol Settings.

9. On the Summary page, navigate to Assertion Consumer Service URL.

10. On the Assertion Consumer Service URL screen, edit the existing entry. Enter the Endpoint URL corresponding to your organization name. For example, `https://github.com/orgs/<organization_name>/saml/consume`

11. Click Update and Done to proceed.

12. On the **Credentials > Digital Signature Settings** page, select the signing certificate.

13. On the Outbound Provisioning page, click Configure Provisioning.

14. On the Target page, enter the values for each field as required by the GitHub Connector.

    ![An image of the Target screen.](_images/les1563995353510.png)

    **Target screen options**

    | Field Name           | Description                                                                                                                                                                                                                                                                                                                                                                  |
    | -------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    | Base URL             | The base URL for GitHub. For example:```
    https://api.github.com/scim/v2/organizations/<organization_name>
    ```&#xA;&#xA;To determine your organization name, see Accessing an organization in the GitHub documentation.                                                                                                                                                       |
    | Access Token         | The access token used by the connector to make authenticated API calls to GitHub. You can find more information about obtaining the access token in [Obtain client ID and secret from GitHub](pf_github_connector_obtain_client_id_and_secret_from_github.html) and [Generate OAuth access tokens](pf_github_connector_generate_oauth_access_tokens.html).                   |
    | Provisioning Options |                                                                                                                                                                                                                                                                                                                                                                              |
    | User Create          | * True (default)

      Users will be created in GitHub.

    * False

      Users will not be created in GitHub.

      &#xA;&#xA;The provisioner.log will display a warning within the create user workflow that the user was not created in GitHub.                                                                                                                                       |
    | User Update          | - True (default)

      Users will be updated in GitHub.

    - False

      Users will not be updated in GitHub.

      &#xA;&#xA;The provisioner.log will display a warning within the update user workflow that the user was not updated in GitHub.Enabling a previously deleted user in GitHub will trigger a create and as such, users can be enabled when User Update is set to false. |
    | User Delete          | * True (default)

      Users will be deleted in GitHub.

    * False

      Users will not be deleted in GitHub.

      &#xA;&#xA;The provisioner.log will display a warning indicating that the user was not deleted in GitHub.                                                                                                                                                            |

15. Click Next to continue the provisioning configuration. Learn more in the following sections under [Configuring outbound provisioning](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_spconnectionconfigtasklet_saasprovisioningstate.html) in the PingFederate documentation:

    * [Managing channels](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_saasmanagementtasklet_saasmanagementstate.html)

    * [Specifying channel information](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_saaschanneltasklet_saasgeneralinfostate.html)

    * [Identifying the source datastore](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_saaschanneltasklet_saassourceselectionstate.html)

    * [Modifying source settings](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_saaschanneltasklet_saassourcesettingsstate.html)

    * [Specifying a source location](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_saaschanneltasklet_saassourcelocationstate.html)

    * [Mapping attributes](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_saaschanneltasklet_saasattrmappingmgmtstate.html)

    * [Reviewing channel settings](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_saaschanneltasklet_saasactivationstate.html)

      |   |                                                                                                                 |
      | - | --------------------------------------------------------------------------------------------------------------- |
      |   | Credentials will be verified when the channel and SP connection is set to Active and provisioning is initiated. |

      |   |                                                                                                                                                                                                                                                     |
      | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      |   | If you are not ready to complete the provisioning configuration, you can click Save and return to the configuration page later.To return to the configuration page, select the connection from **Identity Provider > SP Connections > Manage All**. |

---

---
title: Configuring an adapter instance
description: Configure the GitHub IdP Adapter to determine how PingFederate communicates with GitHub.
component: github
page_id: github:github_login_integration_kit:pf_github_cic_configuring_an_adapter_instance
canonical_url: https://docs.pingidentity.com/integrations/github/github_login_integration_kit/pf_github_cic_configuring_an_adapter_instance.html
llms_txt: https://docs.pingidentity.com/integrations/github/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: November 3, 2025
section_ids:
  steps: Steps
---

# Configuring an adapter instance

Configure the GitHub IdP Adapter to determine how PingFederate communicates with GitHub.

## Steps

1. In the PingFederate admin console, go to **Authentication > Integration > IdP Adapters**. Click **Create New Instance**.

2. On the **Type** tab, set the basic adapter instance attributes:

   1. In the **Instance Name** field, enter a name for the adapter instance.

   2. In the **Instance ID** field, enter a unique identifier for the adapter instance.

   3. In the **Type** list, select **GitHub IdP Adapter**. Click **Next**.

3. (Optional) On the **IdP Adapter** page, in the **Optional GitHub Attributes** section, override or add to the default mappings between local attributes and the attributes from the core or extended contract.

   You can find a list of available attributes in [Available user attributes](pf_github_cic_available_user_attributes.html) and the example JSON payload in [JSON Pointer syntax reference](pf_github_cic_json_pointer_syntax_reference.html).

   1. Click **Add a new row to 'Optional GitHub Attributes'**.

   2. In the **Local Attribute** field, enter the name of a local attribute.

   3. In the **GitHub Attribute** field, enter the JSON Pointer syntax for the value of the matching GitHub attribute.

      Learn more in [JSON Pointer syntax reference](pf_github_cic_json_pointer_syntax_reference.html).

   4. In the **Action** column, click **Update**.

   5. To add more attributes, repeat steps a - d.

4. On the **IdP Adapter** tab, configure the adapter instance by referring to [GitHub IdP Adapter settings reference](pf_github_cic_github_idp_adapter_settings_reference.html). Click **Next**.

5. On the **Actions** tab, click **Test Connection**. Resolve any reported issues, then click **Next**.

6. On the Extended Contract tab, add any attributes that you want to include in the contract. Click Next.

7. On the **Adapter Attributes** tab, set pseudonym and masking options as shown in [Set pseudonym and masking options](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_setting_pseudonym_masking_options.html) in the PingFederate documentation. Click **Next**.

8. On the **Adapter Contract Mapping** tab, configure the contract fulfillment details for the adapter as shown in [Define the IdP adapter contract](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_authnadapterinstancetasklet_plugincontractstate.html) in the PingFederate documentation. Click **Next**.

9. On the Summary tab, check your configuration, then click **Save**.

---

---
title: Creating a personal access token
description: To configure SCIM provisioning, you must create a personal access token under your GitHub enterprise setup user account.
component: github
page_id: github:github_emu_provisioner:pf_github_emu_connector_install_the_connector
canonical_url: https://docs.pingidentity.com/integrations/github/github_emu_provisioner/pf_github_emu_connector_install_the_connector.html
llms_txt: https://docs.pingidentity.com/integrations/github/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 25, 2024
section_ids:
  steps: Steps
---

# Creating a personal access token

To configure SCIM provisioning, you must create a personal access token under your GitHub enterprise setup user account.

## Steps

* Sign on to GitHub using the setup user account for your EMU enterprise and follow the instructions in [Creating a personal access token](https://docs.github.com/en/enterprise-cloud@latest/admin/managing-iam/provisioning-user-accounts-with-scim/configuring-scim-provisioning-for-users#creating-a-personal-access-token) in the GitHub documentation.

---

---
title: Deploying the integration files
description: To get started with the integration, deploy the GitHub Login Integration Kit files to your PingFederate directory.
component: github
page_id: github:github_login_integration_kit:pf_github_cic_deploying_the_integration_files
canonical_url: https://docs.pingidentity.com/integrations/github/github_login_integration_kit/pf_github_cic_deploying_the_integration_files.html
llms_txt: https://docs.pingidentity.com/integrations/github/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 25, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Deploying the integration files

To get started with the integration, deploy the GitHub Login Integration Kit files to your PingFederate directory.

## About this task

|   |                                                                                          |
| - | ---------------------------------------------------------------------------------------- |
|   | If you operate PingFederate in a cluster, the following steps refer to the console node. |

## Steps

1. Download the GitHub Login Integration Kit `.zip` archive from the [**Add-ons** tab of the PingFederate downloads page](https://www.pingidentity.com/en/resources/downloads/pingfederate.html) or the [Ping Identity Marketplace](https://marketplace.pingone.com/item/github-login-integration-kit).

2. Stop PingFederate, if it's running.

3. If you're upgrading an existing deployment, back up your customizations and delete earlier versions of the integration files:

   1. Back up any GitHub Login Integration Kit files that you customized in the `<pf_install>/pingfederate/server/default/conf/` directory.

   2. Delete the `pf-github-idp-adapter-<version>.jar` file from your `<pf_install>/pingfederate/server/default/deploy` directory.

4. Extract the `.zip` archive and merge the contents of the `dist` directory with your `<pf_install>/pingfederate` directory.

5. If there is more than one version of the `pf-authn-api-sdk-<version>.jar` file in your `<pf_install>/pingfederate/server/default/lib` directory, delete all but the latest version of the file.

6. If you backed up any customized files, modify the new files with your customizations.

7. Start PingFederate.

8. If you operate PingFederate in a cluster, repeat steps 2 - 7 for each engine node.

---

---
title: Download manifest
description: The distribution .zip file for the connector contains the following:
component: github
page_id: github:github_emu_provisioner:pf_gh_emu_download_manifest
canonical_url: https://docs.pingidentity.com/integrations/github/github_emu_provisioner/pf_gh_emu_download_manifest.html
llms_txt: https://docs.pingidentity.com/integrations/github/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 25, 2024
---

# Download manifest

The distribution `.zip` file for the connector contains the following:

* `github-emu-saml-metadata.xml`: SAML metadata file for use with a GitHub connection. Learn more in [Configure PingFederate for provisioning and SSO](pf_gh_emu_configure_pf_for_provisioning_and_sso.html).

* `github-emu-saml-enterprises-metadata.xml`: SAML metadata file for use with an EMU data residency connection. Learn more in [Configure PingFederate for provisioning and SSO](pf_gh_emu_configure_pf_for_provisioning_and_sso.html).

* `/legal`:

  * `Legal.pdf`: Copyright and license information.

* `/dist`: Contains libraries needed for the connector:

  * `pf-github-emu-quickconnection-<version>.jar`: PingFederate GitHub EMU Provisioner.

---

---
title: Download manifest
description: The following files are included in the GitHub Login Integration Kit .zip archive.
component: github
page_id: github:github_login_integration_kit:pf_github_cic_download_manifest
canonical_url: https://docs.pingidentity.com/integrations/github/github_login_integration_kit/pf_github_cic_download_manifest.html
llms_txt: https://docs.pingidentity.com/integrations/github/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: January 21, 2026
---

# Download manifest

The following files are included in the GitHub Login Integration Kit `.zip` archive.

* `ReadMeFirst.pdf`: Contains links to this online documentation.

* `legal/Legal.pdf`: Copyright and license information.

* `dist`: Contains the integration files.

  * `deploy`: Contains the Java libraries

    * `pf-github-idp-adapter-<version>.jar`: A `.jar` file that contains the GitHub IdP Adapter.

  * `conf`: Contains the HTML template that presents the GitHub sign-on form.

    * `language-packs`: Contains files with customizable user-facing messages.

      * `pingfederate-github-adapter-messages.properties`: A variable file that customizes the messages that appear on the template files.

    * `template`: Contains user-facing HTML template files.

      * `github-pop-up-template.html`: A template that opens a pop-up window to prompt the user to sign on.

      * `github-post-auth-template.html`: A template that returns the user to the PingFederate sign-on flow after they sign on with GitHub.

      * `assets`: Contains functional scripts and files used by the template.

        * `css/github.css`: A CSS file that customizes the appearance of the template files.

        * `fonts/end-user`: Contains template fonts and icons.

          * `icons`: Contains template icons.

        * `images`: Contains template image files.

          * `ping-logo.svg`: An image file with company branding.

* `lib/pf-authn-api-sdk-<version>.jar`: A `.jar` file that contains the PingFederate Authentication API SDK.

---

---
title: Download manifest
description: The distribution .zip file for the connector contains the following:
component: github
page_id: github:github_provisioner:pf_github_connector_download_manifest
canonical_url: https://docs.pingidentity.com/integrations/github/github_provisioner/pf_github_connector_download_manifest.html
llms_txt: https://docs.pingidentity.com/integrations/github/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 25, 2024
---

# Download manifest

The distribution `.zip` file for the connector contains the following:

* `ReadMeFirst.pdf `– contains links to this online documentation.

* `github-saml-metadata.xml` – SAML metadata file for use with a GitHub connection. For more information, see [Configure PingFederate for provisioning and SSO](pf_github_connector_configure_pf_for_provisioning_and_sso.html).

* `/legal`:

  * `Legal.pdf` – copyright and license information.

* `/dist` – contains libraries needed for the connector:

  * `pf-github-quickconnection-[version].jar `– PingFederate GitHub Connector

---

---
title: Enable outbound provisioning
description: After enabling outbound provisioning in the <pf_install>/pingfederate/bin/run.properties file, you must also activate the outbound provisioning role in the administrative console.
component: github
page_id: github:github_provisioner:pf_github_connector_enable_outbound_provisioning
canonical_url: https://docs.pingidentity.com/integrations/github/github_provisioner/pf_github_connector_enable_outbound_provisioning.html
llms_txt: https://docs.pingidentity.com/integrations/github/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 25, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Enable outbound provisioning

## About this task

After enabling outbound provisioning in the `<pf_install>/pingfederate/bin/run.properties` file, you must also activate the outbound provisioning role in the administrative console.

## Steps

1. Go to **Server Configuration > Server Settings > Roles & Protocol**.

2. Select the Outbound Provisioning checkbox.

   ![An image of the Roles & Protocols screen.](_images/pum1563995350344.png)

   |   |                                                                                                                                                                                                                                                                                                                                                                                             |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | Enabling outbound provisioning adds the outbound provisioning screen and requires the selection of a database to facilitate provisioning. Learn more in [Configuring outbound provisioning settings](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_spconnectionconfigtasklet_saasprovisioningstate.html) or click Help on the configuration screen. |

---

---
title: Enabling debug logging
description: To help with troubleshooting or monitoring, you can turn on activity logging for the adapter.
component: github
page_id: github:github_login_integration_kit:pf_github_cic_enabling_debug_logging
canonical_url: https://docs.pingidentity.com/integrations/github/github_login_integration_kit/pf_github_cic_enabling_debug_logging.html
llms_txt: https://docs.pingidentity.com/integrations/github/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 25, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Enabling debug logging

To help with troubleshooting or monitoring, you can turn on activity logging for the adapter.

## About this task

These steps are optional. For general information about logging, see [Enabling debug messages and console logging](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_enabling_debug_message_and_console_logging.html) in the PingFederate documentation.

## Steps

1. Open the `<pf_install>/pingfederate/server/default/conf/log4j2.xml` file for editing.

2. If you want to log activity for PingFederate and all adapters, do the following.

   1. Find the following section.

      ```html
      <AsyncRoot level="INFO" includeLocation="false">
      	<!-- <AppenderRef ref="CONSOLE" /> -->
      	<AppenderRef ref="FILE" />
      </AsyncRoot>
      ```

   2. Change `INFO` to `DEBUG`.

      ```html
      <AsyncRoot level="DEBUG" includeLocation="false">
      	<!-- <AppenderRef ref="CONSOLE" /> -->
      	<AppenderRef ref="FILE" />
      </AsyncRoot>
      ```

   3. If you want to see the adapter activity in the console, remove the comment tags.

      ```html
      <AsyncRoot level="INFO" includeLocation="false">
      	<AppenderRef ref="CONSOLE" />
      	<AppenderRef ref="FILE" />
      </AsyncRoot>
      ```

3. If you want to log activity just for the GitHub IdP Adapter, add the following line.

   ```html
   <Logger name="com.pingidentity.adapter.idp.github" level="DEBUG"/>
   ```

4. Save the file.

---

---
title: Enabling provisioning and single sign-on in PingFederate
description: To use PingFederate for provisioning and single sign-on, configure an external datastore and set a SAML entity ID.
component: github
page_id: github:github_emu_provisioner:pf_github_emu_connector_enabling_provisioning_and_sso_in_pf
canonical_url: https://docs.pingidentity.com/integrations/github/github_emu_provisioner/pf_github_emu_connector_enabling_provisioning_and_sso_in_pf.html
llms_txt: https://docs.pingidentity.com/integrations/github/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 25, 2024
section_ids:
  about-this-task: About this task
  enabling-provisioning-and-single-sign-on-in-pingfederate-10-1-or-later: Enabling provisioning and single sign-on in PingFederate 10.1 or later
  steps: Steps
  enabling-provisioning-and-single-sign-on-in-pingfederate-10-0-or-earlier: Enabling provisioning and single sign-on in PingFederate 10.0 or earlier
  steps-2: Steps
---

# Enabling provisioning and single sign-on in PingFederate

To use PingFederate for provisioning and single sign-on, configure an external datastore and set a SAML entity ID.

## About this task

Your external datastore acts as the source of data for provisioning. PingFederate also uses an internal datastore to store the state of synchronization between the source datastore and the target datastore.

For more information, see [Datastores](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_datastores.html) and [Configuring outbound provisioning settings](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_protocolsettingstasklet_saasglobalprovisioningsettingsstate.html) in the PingFederate documentation.

* PingFederate 10.1 or later

* PingFederate 10.0 or earlier

## Enabling provisioning and single sign-on in PingFederate 10.1 or later

### Steps

1. In the PingFederate administrative console, configure the datastore for PingFederate to use as the source of user data.

   For help, see [Datastores](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_datastores.html) in the PingFederate documentation.

2. Go to **System > Server > Protocol Settings > Federation Info**.

3. In the **SAML 2.0 Entity ID** field, enter a name for PingFederate to use when identifying itself to SAML partners.

4. On the **Outbound Provisioning** tab, in the **Provisioner Data Store** list, select the internal database that will store the synchronization state. Click **Save**.

   For more information, see [Configuring outbound provisioning settings](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_protocolsettingstasklet_saasglobalprovisioningsettingsstate.html) in the PingFederate documentation.

## Enabling provisioning and single sign-on in PingFederate 10.0 or earlier

### Steps

1. In the PingFederate administrative console, configure the datastore for PingFederate to use as the source of user data.

   For help, see [Datastores](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_datastores.html) in the PingFederate documentation.

2. Go to **System > Protocol Settings > Roles & Protocols**.

3. Select the **Enable Identity Provider IdP Role and Support the Following** check box.

4. Select the **SAML 2.0** and **Outbound Provisioning** check boxes. Click **Next**.

5. Click the **Federation Info** tab.

6. In the **SAML 2.0 Entity ID** field, enter a name for PingFederate to use to identify itself to SAML partners.

7. On the **Outbound Provisioning** tab, in the **Provisioner Data Store** list, select the internal database that will store the synchronization state. Click **Save**.

   For more information, see [Configuring outbound provisioning settings](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_protocolsettingstasklet_saasglobalprovisioningsettingsstate.html) in the PingFederate documentation.

---

---
title: Enabling provisioning and single sign-on in PingFederate 10.0 or earlier
description: In the PingFederate administrative console, configure the datastore for PingFederate to use as the source of user data.
component: github
page_id: github:github_emu_provisioner:pf_github_emu_connector_enabling_provisioning_and_sso_in_pf_100_or_earlier
canonical_url: https://docs.pingidentity.com/integrations/github/github_emu_provisioner/pf_github_emu_connector_enabling_provisioning_and_sso_in_pf_100_or_earlier.html
llms_txt: https://docs.pingidentity.com/integrations/github/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 25, 2024
section_ids:
  steps: Steps
---

# Enabling provisioning and single sign-on in PingFederate 10.0 or earlier

## Steps

1. In the PingFederate administrative console, configure the datastore for PingFederate to use as the source of user data.

   For help, see [Datastores](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_datastores.html) in the PingFederate documentation.

2. Go to **System > Protocol Settings > Roles & Protocols**.

3. Select the **Enable Identity Provider IdP Role and Support the Following** check box.

4. Select the **SAML 2.0** and **Outbound Provisioning** check boxes. Click **Next**.

5. Click the **Federation Info** tab.

6. In the **SAML 2.0 Entity ID** field, enter a name for PingFederate to use to identify itself to SAML partners.

7. On the **Outbound Provisioning** tab, in the **Provisioner Data Store** list, select the internal database that will store the synchronization state. Click **Save**.

   For more information, see [Configuring outbound provisioning settings](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_protocolsettingstasklet_saasglobalprovisioningsettingsstate.html) in the PingFederate documentation.

---

---
title: Enabling provisioning and single sign-on in PingFederate 10.1 or later
description: In the PingFederate administrative console, configure the datastore for PingFederate to use as the source of user data.
component: github
page_id: github:github_emu_provisioner:pf_github_emu_connector_enabling_provisioning_and_sso_in_pf_101_or_later
canonical_url: https://docs.pingidentity.com/integrations/github/github_emu_provisioner/pf_github_emu_connector_enabling_provisioning_and_sso_in_pf_101_or_later.html
llms_txt: https://docs.pingidentity.com/integrations/github/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 25, 2024
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