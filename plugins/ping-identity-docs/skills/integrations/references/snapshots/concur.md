---
title: Changelog
description: Concur Connector 1.0 – May 2015 (current release)
component: concur
page_id: concur:release_notes:pf_concur_connector_changelog
canonical_url: https://docs.pingidentity.com/integrations/concur/release_notes/pf_concur_connector_changelog.html
llms_txt: https://docs.pingidentity.com/integrations/concur/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 26, 2024
---

# Changelog

**Concur Connector 1.0 – May 2015 (current release)**

* Initial release

* Added support for user provisioning

* Added support for browser-based single sign-on

---

---
title: Concur Provisioner
description: The PingFederate Concur Provisioner enables an enterprise to provision users to Concur. A quick connection template is also included to simplify the configuration of single sign-on (SSO).
component: concur
page_id: concur::pf_concur_connector
canonical_url: https://docs.pingidentity.com/integrations/concur/pf_concur_connector.html
llms_txt: https://docs.pingidentity.com/integrations/concur/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 26, 2024
section_ids:
  features: Features
  intended-audience: Intended audience
  system-requirements: System Requirements
---

# Concur Provisioner

The PingFederate Concur Provisioner enables an enterprise to provision users to Concur. A quick connection template is also included to simplify the configuration of single sign-on (SSO).

|   |                                                                                                                                                                                                                                                                                       |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Updates and support have ended for this integration. The availability of this user guide and the related product download is intended only for those who have existing solutions that use this integration. Learn more about Concur in the [Concur website](https://www.concur.com/). |

## Features

* Browser-based IdP-initiated SSO

* Includes support for user life cycle management (including creates, updates, and disables).

## Intended audience

This document is intended for PingFederate administrators.

If you need help during the setup process, see the following sections of the PingFederate documentation:

* [SP connection management](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_sp_connect_management.html)

* [Identity provider SSO configuration](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_ident_provid_sso_config.html)

* [Datastores](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_datastores.html)

* [Configuring outbound provisioning](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_spconnectionconfigtasklet_saasprovisioningstate.html)

* [Configuring outbound provisioning settings](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_protocolsettingstasklet_saasglobalprovisioningsettingsstate.html)

## System Requirements

* PingFederate 7.3 or later with Java 8.

---

---
title: Configure Concur for SSO
description: To proceed with configuring Concur for single sign-on (SSO), you must have the following information from PingFederate.
component: concur
page_id: concur:setup:pf_concur_connector_configure_concur_for_sso
canonical_url: https://docs.pingidentity.com/integrations/concur/setup/pf_concur_connector_configure_concur_for_sso.html
llms_txt: https://docs.pingidentity.com/integrations/concur/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 26, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Configure Concur for SSO

## About this task

To proceed with configuring Concur for single sign-on (SSO), you must have the following information from PingFederate.

* Identity provider certificate

  * This is the X.509 certificate from PingFederate used for SSO in your SP connection. Learn more in [Managing digital signing certificates and decryption keys](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_certmanagementtasklet_dsigsigningcert_certmanagementstate.html).

To configure Concur for SSO:

## Steps

1. Obtain the Base64 X.509 certificate that will be used for SSO in your SP connection.

2. Contact your Concur account representative to obtain a work order which will enable the Concur technical team to assist you in setting up SSO for your organization. Ensure the X.509 certificate is included in your request.

---

---
title: Configure PingFederate for SSO
description: The following section describes the steps for configuring single sign-on (SSO) to Concur. Configuring SAML SSO involves configuring both the PingFederate SP connection and Concur.
component: concur
page_id: concur:setup:pf_concur_connector_configure_pf_for_sso
canonical_url: https://docs.pingidentity.com/integrations/concur/setup/pf_concur_connector_configure_pf_for_sso.html
llms_txt: https://docs.pingidentity.com/integrations/concur/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 26, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Configure PingFederate for SSO

## About this task

The following section describes the steps for configuring single sign-on (SSO) to Concur. Configuring SAML SSO involves configuring both the PingFederate SP connection and Concur.

|   |                                                        |
| - | ------------------------------------------------------ |
|   | Configuring SSO is optional for outbound provisioning. |

## Steps

1. Create a new SP connection or select an existing SP connection from the **SP Configuration** menu.

2. On the **Connection Template** page, select the **Use a template for this connection** option and select **Concur** in the **Connection Template** drop-down list. When asked during the connection configuration steps, import the `saml-metadata.xml` packaged with this connector.

   ![An image of the Connection Template screen.](_images/kgo1563995204444.png)

3. On the **Connection Type** page, ensure that the **Browser SSO Profiles** checkbox is selected.

4. On the **General Info** page, the default values are taken from the metadata file you selected in step 2. We recommend using the metadata default values.

   ![An image of the General Info screen.](_images/pam1563995209722.png)

5. Click **Next** to continue the Browser SSO configuration. Learn more in the following sections under [Identity provider SSO configuration](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_ident_provid_sso_config.html):

   * [Managing IdP adapters](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_managing_idp_adapters.html)

   * [Configure IdP Browser SSO](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_spconnectionconfigtasklet_spbrowserssostate.html)

   * [Configuring credentials](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_spconnectionconfigtasklet_credentialsstate.html)

     |   |                                                                                                                                                       |
     | - | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
     |   | The SAML\_SUBJECT configured on the **IdP Adapter Mapping > Attribute Contract Fulfillment** page must match the user's loginId configured in Concur. |

6. On the **Credentials > Digital Signature Settings** page, select the signing certificate.

7. On the **Activation & Summary** page, set **Connection Status** to **Active**, then click **Save**.

   |   |                                                                                                                                                                                                                                                 |
   | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | If you are not ready to complete the SSO configuration, you can click **Save** and return to the configuration page later. To return to the configuration page, select the connection from **Identity Provider > SP Connections > Manage All**. |

---

---
title: Configure provisioning
description: To configure a connection for outbound provisioning to Concur, follow the instructions in this section.
component: concur
page_id: concur:setup:pf_concur_connector_configure_provisioning
canonical_url: https://docs.pingidentity.com/integrations/concur/setup/pf_concur_connector_configure_provisioning.html
llms_txt: https://docs.pingidentity.com/integrations/concur/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 26, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Configure provisioning

## About this task

To configure a connection for outbound provisioning to Concur, follow the instructions in this section.

Outbound provisioning details are managed within a service provider (SP) connection. You can configure outbound provisioning with or without Browser SSO, WS-Trust STS, or both when you create a new SP connection. You can also add outbound provisioning to an existing SP connection.

## Steps

1. In the PingFederate administrative console, configure the datastore that PingFederate will use as the source of user data. Learn more in [Datastores](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_managedatasourcestasklet_managedatasourcesstate.html) in the PingFederate documentation.

   * When targeting users and groups for provisioning, exclude the user account that you will use to administer users in your connection to Concur. This prevents the PingFederate provisioning engine from interfering with the account that provisions users and groups.

2. Create a new SP connection or select an existing SP connection from the **SP Configuration** menu.

3. On the **Connection Template** page, select **Use a template for this connection** and select **Concur** in the **Connection Template** drop-down list. When asked during the connection configuration steps, import the `saml-metadata.xml` packaged with this connector.

   ![An image of the Connection Template screen.](_images/kgo1563995204444.png)

   |   |                                                                                                 |
   | - | ----------------------------------------------------------------------------------------------- |
   |   | If this selection is not available, verify the connector installation and restart PingFederate. |

4. On the **Connection Type** page, ensure the **Outbound Provisioning** checkbox is selected, and the **Browser SSO Profiles** checkbox is cleared (if appropriate).

5. On the **General Info** page, the default values are taken from the metadata file you selected in step 2. We recommend using the metadata default values.

   ![An image of the General Info screen.](_images/mey1563995205457.png)

6. Follow the connection wizard to configure the connection.

7. On the **Outbound Provisioning** page, click **Configure Provisioning**.

8. On the **Target** page, enter the values for each field as required by the Concur Connector.

   ![An image of the Target screen.](_images/urm1563995207208.png)

   | Field Name               | Description                                                                                                                                                                                                                  |
   | ------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | **OAUTH\_ACCESS\_TOKEN** | The OAuth access token for the Concur account.Learn more in [Obtain key and secret](pf_concur_connector_obtain_key_and_secret.html) and [Generate OAuth access token](pf_concur_connector_generate_oauth_access_token.html). |

9. Click **Next** to continue the provisioning configuration. Learn more in the following sections under [Outbound provisioning for IdPs](https://docs.pingidentity.com/pingfederate/latest/introduction_to_pingfederate/pf_outboun_provis_for_idp.html) in the PingFederate documentation:

   * [Managing channels](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_saasmanagementtasklet_saasmanagementstate.html)

   * [Specifying channel information](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_saaschanneltasklet_saasgeneralinfostate.html)

   * [Identifying the source datastore](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_saaschanneltasklet_saassourceselectionstate.html)

   * [Modifying source settings](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_saaschanneltasklet_saassourcesettingsstate.html)

   * [Specifying a source location](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_saaschanneltasklet_saassourcelocationstate.html)

   * [Mapping attributes](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_saaschanneltasklet_saasattrmappingmgmtstate.html)

   * [Reviewing channel settings](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_saaschanneltasklet_saasactivationstate.html)

     |   |                                                                                                                                              |
     | - | -------------------------------------------------------------------------------------------------------------------------------------------- |
     |   | Many fields are required based on your Concur account configuration. Ensure that you are sending data for all user fields that are required. |

     |   |                                                                                                                     |
     | - | ------------------------------------------------------------------------------------------------------------------- |
     |   | Credentials will be verified when the channel and SP connection is set to **Active** and provisioning is initiated. |

     |   |                                                                                                                                                                                                                                                          |
     | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
     |   | If you are not ready to complete the provisioning configuration, you can click **Save** and return to the configuration page later. To return to the configuration page, select the connection from **Identity Provider > SP Connections > Manage All**. |

---

---
title: Configure SAML SSO
description: The following section describes the steps for configuring single sign-on (SSO) to Concur.
component: concur
page_id: concur:setup:pf_concur_connector_configure_saml_sso
canonical_url: https://docs.pingidentity.com/integrations/concur/setup/pf_concur_connector_configure_saml_sso.html
llms_txt: https://docs.pingidentity.com/integrations/concur/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 26, 2024
---

# Configure SAML SSO

The following section describes the steps for configuring single sign-on (SSO) to Concur.

|   |                                                        |
| - | ------------------------------------------------------ |
|   | Configuring SSO is optional for outbound provisioning. |

---

---
title: Download manifest
description: "The distribution .zip: Archive for the connector contains the following:"
component: concur
page_id: concur:release_notes:pf_concur_connector_download_manifest
canonical_url: https://docs.pingidentity.com/integrations/concur/release_notes/pf_concur_connector_download_manifest.html
llms_txt: https://docs.pingidentity.com/integrations/concur/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 26, 2024
---

# Download manifest

The distribution `.zip`: Archive for the connector contains the following:

* `ReadMeFirst.pdf`: Contains links to this online documentation.

* `saml-metadata.xml`: The metadata used for Browser SSO

* `/legal`:

  * `Legal.pdf`: Copyright and license information.

* `/dist`: Contains libraries needed for the connector:

  * `pf-concur-quickconnection-1.0.jar`: PingFederate Concur Connector

  * `prov-cpl-2.0.2.jar`: PingFederate Common Provisioning Layer

---

---
title: Enable outbound provisioning
description: After enabling outbound provisioning in the <pf_install>/pingfederate/bin/run.properties file, you must also activate the outbound provisioning role in the administrative console.
component: concur
page_id: concur:setup:pf_concur_connector_enable_outbound_provisioning
canonical_url: https://docs.pingidentity.com/integrations/concur/setup/pf_concur_connector_enable_outbound_provisioning.html
llms_txt: https://docs.pingidentity.com/integrations/concur/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 26, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Enable outbound provisioning

## About this task

After enabling outbound provisioning in the `<pf_install>/pingfederate/bin/run.properties` file, you must also activate the outbound provisioning role in the administrative console.

## Steps

1. Go to the **Server Configuration > Server Settings > Roles & Protocols** page.

2. Select the **Outbound Provisioning** checkbox.

   ![An image of the Roles & Protocols screen.](_images/alx1563995203433.png)

   |   |                                                                                                                                                                                                                                                                                                                                                                                                         |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | Enabling outbound provisioning adds the outbound provisioning page, requiring the selection of a database to facilitate provisioning. Learn more in [Configuring outbound provisioning settings](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_protocolsettingstasklet_saasglobalprovisioningsettingsstate.html) or click **Help** from the configuration page. |

---

---
title: Generate OAuth access token
description: In a browser, go to the Ping Identity OAuth Configuration Service.
component: concur
page_id: concur:setup:pf_concur_connector_generate_oauth_access_token
canonical_url: https://docs.pingidentity.com/integrations/concur/setup/pf_concur_connector_generate_oauth_access_token.html
llms_txt: https://docs.pingidentity.com/integrations/concur/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 26, 2024
section_ids:
  steps: Steps
---

# Generate OAuth access token

## Steps

1. In a browser, go to the Ping Identity [OAuth Configuration Service](https://oauth.pingone.com/ocs/ppm/rest/v1/oauth/oasrequestform).

2. Select **Concur Web Connector** in the list.

   ![An image of the OAuth Configuration Service screen.](_images/jzu1563995200159.png)

3. Enter the **Key** value you previously obtained into the **ClientID** field.

4. Enter the **Secret** value you previously obtained into the **Client Secret** field.

5. Click **Connect**.

6. Sign on to Concur as an administrative user for your organization.

   |   |                                                                                                                                                                     |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | If you are already signed into Concur you will not be asked to sign on again. Please be sure that the account you are signed in under is an administrative account. |

7. Click the **Allow** button to generate your access token.

8. You should be redirected to the OAuth Configuration Service and presented with an access token.

   ![An image of the OAuth Configuration Service response.](_images/bzj1563995200993.png)

9. Copy the **Access Token** to use when configuring the Concur Connector.

---

---
title: Install the connector
description: This section describes the common steps required to install the PingFederate Concur Connector.
component: concur
page_id: concur:setup:pf_concur_connector_install_the_connector
canonical_url: https://docs.pingidentity.com/integrations/concur/setup/pf_concur_connector_install_the_connector.html
llms_txt: https://docs.pingidentity.com/integrations/concur/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 26, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Install the connector

## About this task

This section describes the common steps required to install the PingFederate Concur Connector.

If you experience issues with deployment, installation, or configuration, visit [Ping Identity Support & Community](https://support.pingidentity.com/s/).

## Steps

1. Download the Concur Provisioner `.zip` archive from the [**Add-ons** tab of the PingFederate downloads page](https://www.pingidentity.com/en/resources/downloads/pingfederate.html) or the [Ping Identity Marketplace](https://marketplace.pingone.com/home).

2. Stop the PingFederate server if it is running.

3. Extract the Concur Connector distribution `.zip` archive.

4. Copy the contents of the `dist` directory into the directory:

   `<pf_install>/pingfederate/server/default/deploy`

5. (Optional) If you plan to use the connector for outbound provisioning, edit the `run.properties` file located in `<pf_install>/pingfederate/bin`, changing the property `pf.provisioner.mode` to `STANDALONE`. For example:

   `pf.provisioner.mode=STANDALONE`

   |   |                                                                                                                                                                                                                                        |
   | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | To configure the `FAILOVER` mode instead, see [Deploying provisioning failover](https://docs.pingidentity.com/pingfederate/latest/server_clustering_guide/pf_deploy_provis_failover.html) in the PingFederate server clustering guide. |

6. Start the PingFederate server.

---

---
title: Known issues and limitations
description: Due to a limitation with PingFederate 8.1 and earlier versions, when configuring two SP connections with the same provisioner, the second connection built may be pre-populated with the channel from the first connection. To avoid conflicts, delete this pre-populated channel and create a unique channel for each connection.
component: concur
page_id: concur:release_notes:pf_concur_connector_known_issues_and_limitations
canonical_url: https://docs.pingidentity.com/integrations/concur/release_notes/pf_concur_connector_known_issues_and_limitations.html
llms_txt: https://docs.pingidentity.com/integrations/concur/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 26, 2024
---

# Known issues and limitations

* Due to a limitation with PingFederate 8.1 and earlier versions, when configuring two SP connections with the same provisioner, the second connection built may be pre-populated with the channel from the first connection. To avoid conflicts, delete this pre-populated channel and create a unique channel for each connection.

* When an LDAP user is deleted in a targeted group distinguished name (DN), the provisioning connector does not propagate the deletion until a new user is added to the group. This limitation is compounded when the **User Create** provisioning option is disabled. Learn more about solutions in [SaaS provisioner does not remove the user](https://support.pingidentity.com/s/article/After-deleting-an-AD-user-account-SaaS-provisioner-does-not-remove-the-user-in-the-next-provisioning-cycle-when-Group-DN-is-specified) in the Knowledge Base.

* Due to PingFederate limitations, user attributes cannot be cleared once set.

* Custom attributes that are connected (multi-level) lists are not supported.

* Concur does not have support UTF-8 for all user fields.

* Due to API limitations, fields required in your Concur organization cannot be made create-only.

* Due to API limitations, users that are hard-deleted or no longer targeted by the provisioner in the data store are not disabled on Concur. If this occurs, an error will continue to appear in the provisioning logs stating what has happened. To resolve the issue in PingFederate, the user's record must be manually removed from the `channel_user` table in the database that monitors provisioning.

* Due to API limitations, updating a user's `loginId` and `employeeId` in the same request will result in a new user being created rather than the existing user being updated.

---

---
title: Obtain key and secret
description: The Concur Connectors Outbound Provisioning functionality is built using Concur's REST API, which requires an OAuth 2.0 access token for authentication. To obtain the access token, you must first obtain your key and secret from Concur.
component: concur
page_id: concur:setup:pf_concur_connector_obtain_key_and_secret
canonical_url: https://docs.pingidentity.com/integrations/concur/setup/pf_concur_connector_obtain_key_and_secret.html
llms_txt: https://docs.pingidentity.com/integrations/concur/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 26, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Obtain key and secret

## About this task

The Concur Connectors Outbound Provisioning functionality is built using Concur's REST API, which requires an OAuth 2.0 access token for authentication. To obtain the access token, you must first obtain your key and secret from Concur.

|   |                                                                                                                                                                         |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Concur provides Web Services, such as provisioning, as an optional service to customers. Verify with Concur that you have Web Services available as part of your setup. |

## Steps

1. Sign on to your Concur account as an administrative user for your organization.

2. Go to **Administration > Company > Web Services**.

3. Select **Register Partner Application**.

4. Create a new application or modify an existing application with the following options:

   1. Enter a name for the application.

   2. Enter a description for the application.

   3. Ensure the **Active** field is set to **Active**.

   4. In the **APIs** list, ensure **Users- Add or Update User Accounts** is selected.

   5. Copy the Application Authorization's **Key** and **Secret** value for later use in [Generate OAuth access token](pf_concur_connector_generate_oauth_access_token.html).

      ![An image of the New Partner Application screen.](_images/hak1563995201879.png)

---

---
title: Supported attributes reference
description: The following table consists of the attributes that can be mapped on a user during provisioning.
component: concur
page_id: concur:setup:pf_concur_connector_supported_attributes_reference
canonical_url: https://docs.pingidentity.com/integrations/concur/setup/pf_concur_connector_supported_attributes_reference.html
llms_txt: https://docs.pingidentity.com/integrations/concur/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 26, 2024
---

# Supported attributes reference

The following table consists of the attributes that can be mapped on a user during provisioning.

Learn more in [User](https://developer.concur.com/api-reference/user/) in the Concur API reference documentation.

|   |                                                                                                                                              |
| - | -------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Many fields are required based on your Concur account configuration. Ensure that you are sending data for all user fields that are required. |

| Attribute                 | Description                                                                                                                                                                                                                   |
| ------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| loginId                   | The URL-encoded Concur login of the user. This value must be unique. This attribute is required.                                                                                                                              |
| empId                     | The unique identifier for the user. This attribute is required.                                                                                                                                                               |
| emailAddress              | The user's email address.                                                                                                                                                                                                     |
| Password                  | The user's password. This element can be used to enter the password for a new user, but cannot be used to update the password for an existing user. This attribute is required.                                               |
| crnKey                    | The 3-letter [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) currency code for the user's reimbursement currency. For example, United States Dollar is USD.                                                                |
| ctryCode                  | The [ISO 3166-1 alpha-2](http://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country code. For example, United States is US.                                                                                                     |
| ctrySubCode               | The user's two-character country code and two-character state or province code. For example, Washington State, United States is US-WA.                                                                                        |
| custom1 through custom21  | The custom fields on the Employee form. Varies depending on configuration. There are two types of custom lists: simple lists and connected (multi-level) lists. We do not support connected lists.                            |
| expenseUserApprover       | Whether the user is an Expense approver. Available options include: Y/N.                                                                                                                                                      |
| expenseUser               | Whether the user has access to Expense. Available options include: Y/N.                                                                                                                                                       |
| firstName                 | The user's first name.                                                                                                                                                                                                        |
| invoiceUserApprover       | Whether the user is an Invoice approver. Available options include: Y/N.                                                                                                                                                      |
| invoiceUser               | Whether the user has access to Invoice. Available options include: Y/N.                                                                                                                                                       |
| lastName                  | The user's last name.                                                                                                                                                                                                         |
| ledgerKey                 | The user's assigned account code ledger. For example, Default. NOTE: This is required for new users.                                                                                                                          |
| localeName                | The user's language locale code. Learn more in [Locale Codes](https://developer.concur.com/tools-support/reference/locale-codes.html) in the Concur API reference documentation.For example, United States English is en\_US. |
| mI                        | The user's middle initial.                                                                                                                                                                                                    |
| orgUnit1 through orgUnit6 | The custom organizational unit fields on the Employee form. Varies depending on configuration.                                                                                                                                |
| tripUser                  | Whether the user has access to Travel. Available options include: Y/N.                                                                                                                                                        |
| isTestEmp                 | Whether the user is a test user. Available options include: Y/N.                                                                                                                                                              |

---

---
title: User management
description: The Concur Provisioner synchronizes users from your datastore to Concur. The following describes the behavior of each provisioning capability.
component: concur
page_id: concur::pf_concur_connector_user_management
canonical_url: https://docs.pingidentity.com/integrations/concur/pf_concur_connector_user_management.html
llms_txt: https://docs.pingidentity.com/integrations/concur/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 26, 2024
section_ids:
  synchronizing-existing-users: Synchronizing existing users
  user-provisioning: User provisioning
  user-updates: User updates
  user-deprovisioning: User deprovisioning
---

# User management

The Concur Provisioner synchronizes users from your datastore to Concur. The following describes the behavior of each provisioning capability.

|   |                                                                                                                                                                                                                  |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | You can configure the following capabilities and specify which users to provision when you get to the [Configure provisioning](setup/pf_concur_connector_configure_provisioning.html) part of the setup process. |

## Synchronizing existing users

PingFederate synchronizes users based on the `empId` attribute in Concur. If a user already exists in your datastore and Concur, mapping this attribute correctly links the two records together.

For example:

* In Concur, Janet's `empId` is `123abc`.

* In your datastore, Janet's `employeeID` is `123abc`.

* On the **Attribute Mapping** tab of your provisioning connection configuration, map the `empId` attribute to `employeeID`.

* When the provisioning connector runs, the datastore user is provisioned with a `empId` of `123abc`. That matches Janet's existing `empId` in Concur, so her information in the datastore is synchronized to her Concur account.

## User provisioning

PingFederate provisions users when any of the following happens:

* A user is added to the datastore group or filter that is targeted by the provisioning connector.

* A user with `disabled` status is added to the datastore group or filter that is targeted by the provisioning connector, and the **Provision disabled users** provisioning option is enabled. This feature is not available in all provisioning connectors.

|   |                                                                                                                                                |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------- |
|   | You can define which users PingFederate targets for provisioning on the **Source Location** tab of your provisioning connection configuration. |

## User updates

PingFederate updates users when a user attribute changes in your datastore.

|   |                                                                                                                                                   |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | You can define which attributes PingFederate monitors for changes on the **Attribute Mapping** tab of your provisioning connection configuration. |

## User deprovisioning

PingFederate deprovisions users when any of the following happens:

* A user is deleted from the user store.

* A user is disabled in the user store.

* A user is removed from the datastore group or filter that is targeted by the provisioning connector.