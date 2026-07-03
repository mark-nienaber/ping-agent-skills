---
title: Changelog
description: Evernote Connector 2.0 – July 2018 (current release)
component: evernote
page_id: evernote:release_notes:pf_evernote_connector_changelog
canonical_url: https://docs.pingidentity.com/integrations/evernote/release_notes/pf_evernote_connector_changelog.html
revdate: June 11, 2024
---

# Changelog

**Evernote Connector 2.0 – July 2018 (current release)**

* Updated support for user life cycle management (including create, update and disable)

* Added configuration options for workflow capabilities (for example, the ability to disable updates)

* Added support for the below user attributes:

  * Display Name

  * External ID

* Added support for the Evernote SCIM 2.0 API.

* Removed support for hard delete (feature deprecated by Evernote)

* Removed support for reactivating a disabled user (feature deprecated by Evernote)

**Evernote Connector 1.0 – July 2014**

* Initial Release

---

---
title: Configure Evernote for provisioning
description: The following are the tasks to enable SCIM provisioning on the Evernote Admin Portal. Learn more about configuring Evernote for SCIM in Configure SCIM with your Evernote Teams account in the Evernote documentation.
component: evernote
page_id: evernote:setup:pf_evernote_connector_configure_evernote_for_provisioning
canonical_url: https://docs.pingidentity.com/integrations/evernote/setup/pf_evernote_connector_configure_evernote_for_provisioning.html
revdate: June 11, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Configure Evernote for provisioning

## About this task

The following are the tasks to enable SCIM provisioning on the Evernote Admin Portal. Learn more about configuring Evernote for SCIM in [Configure SCIM with your Evernote Teams account](https://help.evernote.com/hc/en-us/articles/115010419308) in the Evernote documentation.

|   |                                                                                                                                                                                                                                                                                                                                                                                                  |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | To enable SCIM provisioning, you must enable single sign-on (SSO). Learn more in [Configure Evernote for SSO](pf_evernote_connector_configure_evernote_for_sso.html). SCIM is only available in Evernote Teams accounts created on or after September 15, 2017. Learn more in [How to determine when an Evernote Teams account was created](https://help.evernote.com/hc/articles/115011455527). |

## Steps

1. Sign on to your Evernote account as an administrative user for your organization.

2. Go to the [Evernote Business Admin Console](https://www.evernote.com/business/AccountSettings.action).

3. On the left sidebar, go to **Integrations > SCIM**.

4. Generate a bearer token by clicking the **Generate token** link.

5. Copy the bearer token value for later use.

   |   |                                                                               |
   | - | ----------------------------------------------------------------------------- |
   |   | You must copy the token immediately, as it will disappear on your next visit. |

---

---
title: Configure Evernote for SSO
description: To configure Evernote for single sign-on (SSO), you must have the signing certificate from your PingFederate identity provider (IdP) setup. Learn more in Obtain PingFederate signing certificate.
component: evernote
page_id: evernote:setup:pf_evernote_connector_configure_evernote_for_sso
canonical_url: https://docs.pingidentity.com/integrations/evernote/setup/pf_evernote_connector_configure_evernote_for_sso.html
revdate: June 11, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Configure Evernote for SSO

## About this task

To configure Evernote for single sign-on (SSO), you must have the signing certificate from your PingFederate identity provider (IdP) setup. Learn more in [Obtain PingFederate signing certificate](pf_evernote_connector_obtain_pf_signing_certificate.html).

|   |                                                                                                                                                                                                                                                          |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Only Evernote Teams account admins are authorized to configure SSO. Learn more about Evernote SSO configuration in [Configure SSO for your Evernote Teams account](https://help.evernote.com/hc/en-us/articles/209005217) in the Evernote documentation. |

## Steps

1. Sign on to your Evernote account as an administrative user for your organization.

2. Go to the [Evernote Business Admin Console](https://www.evernote.com/business/AccountSettings.action).

3. On the left sidebar, go to **Security > Single Sign-On**.

4. In the **SAML HTTP Request URL** field, enter the HTTPS endpoint of your IdP for SSO requests.

   For example, https\://*\<pf\_hostname>*:*\<pf\_port>*/idp/SSO.saml2

5. Open your PingFederate signing certificate file using a text editor.

6. Under **X.509 Certificate**, paste your PingFederate signing certificate used to verify SAML responses.

7. Enter a **Session Duration**. This is the number of hours the SSO token will remain valid before employees must re-authorize their token.

   The default value is 24 hours.

8. Click **Save & Enable**

   |   |                                                                                                                                                                  |
   | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | Clicking **Save & Enable** will require you to successfully perform SSO to enable this functionality. SSO must be enabled by an Evernote Business account admin. |

---

---
title: Configure PingFederate for provisioning
description: To configure a connection for outbound provisioning to Evernote, follow the instructions in this section. Outbound provisioning details are managed within a service provider (SP) connection and can be added to an existing SP connection.
component: evernote
page_id: evernote:setup:pf_evernote_connector_configure_pf_for_provisioning
canonical_url: https://docs.pingidentity.com/integrations/evernote/setup/pf_evernote_connector_configure_pf_for_provisioning.html
revdate: June 11, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Configure PingFederate for provisioning

## About this task

To configure a connection for outbound provisioning to Evernote, follow the instructions in this section. Outbound provisioning details are managed within a service provider (SP) connection and can be added to an existing SP connection.

|   |                                                                                                                                                                                                                                                                                                                                |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | Single sign-on (SSO) is required for SCIM provisioning with Evernote. SCIM is available only in Evernote Teams accounts created on or after September 15, 2017. Learn more in [How to determine when an Evernote Teams account was created](https://help.evernote.com/hc/articles/115011455527) in the Evernote documentation. |

## Steps

1. In the PingFederate administrative console, configure the datastore that PingFederate will use as the source of user data.

   Learn more in [Datastores](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_managedatasourcestasklet_managedatasourcesstate.html) in the PingFederate documentation.

   * When targeting users and groups for provisioning, exclude the user account that you will use to administer users in your connection to Evernote. This prevents the PingFederate provisioning engine from interfering with the account that provisions users and groups.

2. Select the existing SP connection created in [Configure PingFederate for SSO](pf_evernote_connector_configure_pf_for_sso.html) from the **Identity Provider > SP Connections > Manage All** menu.

3. On the **Activation & Summary** screen, go to **Connection Type** and select the **Outbound Provisioning** and **Browser SSO Profiles** checkboxes.

4. On the **Outbound Provisioning** screen, click **Configure Provisioning**.

5. On the **Target** screen, enter the values for each field as required by the Evernote Connector.

   ![A screen capture of the Target screen.](_images/kqb1563995312793.png)

   **Target screen options**

   | Field Name               | Description                                                                                                                                                                                                                                                                                                                                                                                                                               |
   | ------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | **Base URL**             | The base URL for Evernote.- https\://m1.svc.evernote.com/scim/v2/                                                                                                                                                                                                                                                                                                                                                                         |
   | **Bearer Token**         | The bearer token used by the connector to make authenticated API calls to Evernote. Learn more about obtaining the bearer token in [Configure Evernote for provisioning](pf_evernote_connector_configure_evernote_for_provisioning.html).                                                                                                                                                                                                 |
   | **Provisioning Options** |                                                                                                                                                                                                                                                                                                                                                                                                                                           |
   | **User Create**          | **True** (default): Users will be created in Evernote.&#xA;&#xA;Due to Evernote API limitations, new users cannot be created with the same username as a previously deactivated user.**False**: Users will not be created in Evernote.&#xA;&#xA;The provisioner.log will display a warning within the create user workflow that the user was not created in Evernote.                                                                     |
   | **User Update**          | **True** (default): Users will be updated in Evernote.**False**: Users will not be updated in Evernote.&#xA;&#xA;The provisioner.log will display a warning within the update user workflow that the user was not updated in Evernote.                                                                                                                                                                                                    |
   | **User Disable**         | **True** (default): Users will be disabled in Evernote.&#xA;&#xA;Due to Evernote API limitations, once a user is deactivated, they cannot be reactivated with the provisioner. A deactivated user can only be reactivated in the Evernote Teams Admin Console.**False**: Users will not be disabled in Evernote.&#xA;&#xA;The provisioner.log will display a warning within the user workflow that the user was not disabled in Evernote. |

6. Click **Next** to continue the provisioning configuration.

   Learn more in the following sections under [Outbound provisioning for IdPs](https://docs.pingidentity.com/pingfederate/latest/introduction_to_pingfederate/pf_outboun_provis_for_idp.html) in the PingFederate documentation:

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

     |   |                                                                                                                                                                                                                                                          |
     | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
     |   | If you are not ready to complete the provisioning configuration, you can click **Save** and return to the configuration page later. To return to the configuration page, select the connection from **Identity Provider > SP Connections > Manage All**. |

---

---
title: Configure PingFederate for SSO
description: To configure a connection for single sign-on (SSO) to Evernote, follow the instructions in this section. Outbound provisioning details are managed within a service provider (SP) connection and can be added to an existing SP connection.
component: evernote
page_id: evernote:setup:pf_evernote_connector_configure_pf_for_sso
canonical_url: https://docs.pingidentity.com/integrations/evernote/setup/pf_evernote_connector_configure_pf_for_sso.html
revdate: June 11, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Configure PingFederate for SSO

## About this task

To configure a connection for single sign-on (SSO) to Evernote, follow the instructions in this section. Outbound provisioning details are managed within a service provider (SP) connection and can be added to an existing SP connection.

|   |                                                                                                                                                                                                                                                                                                               |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | SSO is required for SCIM provisioning with Evernote. SCIM is available only in Evernote Teams accounts created on or after September 15, 2017. Learn more in [How to determine when an Evernote Teams account was created](https://help.evernote.com/hc/articles/115011455527) in the Evernote documentation. |

## Steps

1. Create a new SP connection or select an existing SP connection from the **SP Configuration** menu.

2. On the **Connection Template** screen, select **Use a template for this connection** and choose **Evernote Connector** in the **Connection Template** list. When asked during the connection configuration steps, import the `evernote-saml-metadata.xml` packaged with this connector.

   ![An image of the Connection Template screen.](_images/meb1563995310023.png)

   |   |                                                                                                 |
   | - | ----------------------------------------------------------------------------------------------- |
   |   | If this selection is not available, verify the connector installation and restart PingFederate. |

3. On the **Connection Type** screen, ensure that the **Browser SSO Profiles** checkbox is selected and the **Outbound Provisioning** checkbox is cleared.

   ![An image of the Connection Type screen.](_images/ueu1563995310996.png)

4. On the **General Info** screen, the default values are taken from the metadata file you selected in an earlier step. We recommend using the metadata default values.

   ![An image of the General Info screen.](_images/vnb1563995311687.png)

5. Click **Next** to continue the Browser SSO configuration.

   Learn more in the following sections under [Identity provider SSO configuration](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_ident_provid_sso_config.html) in the PingFederate documentation:

   * [Managing IdP adapters](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_managing_idp_adapters.html)

   * [Configure IdP Browser SSO](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_spconnectionconfigtasklet_spbrowserssostate.html)

   * [Configuring credentials](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_spconnectionconfigtasklet_credentialsstate.html)

6. On the **Attribute Contract** screen, set the **Subject Name Format** for SAML\_SUBJECT to the below value:

   * urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress

7. On the authentication adapter's **Attribute Contract Fulfillment** screen, map SAML\_SUBJECT to email address. Evernote requires SAML\_SUBJECT to contain the user's email address, which must match the Evernote user's business email address.

8. On the **Credentials > Digital Signature Settings** screen, select the signing certificate.

9. On the **Activation & Summary** screen, set **Connection Status** to **ACTIVE**, then click **Save**.

   |   |                                                                                                                                                                                                                                                 |
   | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | If you are not ready to complete the SSO configuration, you can click **Save** and return to the configuration page later. To return to the configuration page, select the connection from **Identity Provider > SP Connections > Manage All**. |

---

---
title: Download manifest
description: The distribution .zip archive for the connector contains the following:
component: evernote
page_id: evernote:release_notes:pf_evernote_connector_download_manifest
canonical_url: https://docs.pingidentity.com/integrations/evernote/release_notes/pf_evernote_connector_download_manifest.html
revdate: June 11, 2024
---

# Download manifest

The distribution `.zip` archive for the connector contains the following:

* `ReadMeFirst.pdf`: Contains links to this online documentation.

* `evernote-saml-metadata.xml`: SAML metadata file for use with an Evernote connection. Learn more in [Configure PingFederate for SSO](../setup/pf_evernote_connector_configure_pf_for_sso.html).

* `/legal`:

  * `Legal.pdf`: Copyright and license information.

* `/dist`: Contains libraries needed for the connector:

  * `pf-evernote-quickconnection-[version].jar`: PingFederate Evernote Connector

---

---
title: Enable outbound provisioning
description: After enabling outbound provisioning in the <pf_install>/pingfederate/bin/run.properties file, you must also activate the outbound provisioning role in the administrative console.
component: evernote
page_id: evernote:setup:pf_evernote_connector_enable_outbound_provisioning
canonical_url: https://docs.pingidentity.com/integrations/evernote/setup/pf_evernote_connector_enable_outbound_provisioning.html
revdate: June 11, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Enable outbound provisioning

## About this task

After enabling outbound provisioning in the `<pf_install>/pingfederate/bin/run.properties` file, you must also activate the outbound provisioning role in the administrative console.

## Steps

1. Go to the **Server Configuration > Server Settings > Roles & Protocols** screen.

2. Select the **Outbound Provisioning** checkbox.

   ![An image of the Roles & Protocols screen.](_images/ngv1563995314486.png)

   |   |                                                                                                                                                                                                                                                                                                                                                                                                                                               |
   | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | Enabling outbound provisioning adds the outbound provisioning screen, requiring the selection of a database to facilitate provisioning. Learn more in [Configuring outbound provisioning settings](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_protocolsettingstasklet_saasglobalprovisioningsettingsstate.html) in the PingFederate documentation or click **Help** from the configuration screen. |

---

---
title: Evernote Provisioner
description: The PingFederate Evernote Provisioner enables an enterprise to provision users to Evernote. A quick connection template is also included to simplify the configuration of single sign-on (SSO).
component: evernote
page_id: evernote::pf_evernote_connector
canonical_url: https://docs.pingidentity.com/integrations/evernote/pf_evernote_connector.html
revdate: June 11, 2024
section_ids:
  features: Features
  intended-audience: Intended audience
  system-requirements: System requirements
---

# Evernote Provisioner

The PingFederate Evernote Provisioner enables an enterprise to provision users to Evernote. A quick connection template is also included to simplify the configuration of single sign-on (SSO).

## Features

* Browser-based SP and IdP-initiated SSO

* Includes support for user life cycle management (including create, update, and disable).

* Includes configuration options for workflow capabilities (for example, the ability to disable updates).

## Intended audience

This document is intended for PingFederate administrators.

Learn more about the setup process in the following sections of the PingFederate documentation:

* [SP connection management](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_sp_connect_management.html)

* [Identity provider SSO configuration](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_ident_provid_sso_config.html)

* [Datastores](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_datastores.html)

* [Configuring outbound provisioning](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_spconnectionconfigtasklet_saasprovisioningstate.html)

* [Configuring outbound provisioning settings](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_protocolsettingstasklet_saasglobalprovisioningsettingsstate.html)

## System requirements

* PingFederate 7.3 or later with Java 8

* To allow outbound connections, you might need to allow the following endpoints on your firewall:

  * https\://m1.svc.evernote.com

SSO is required for SCIM provisioning with Evernote. SCIM is available only in Evernote Teams accounts created on or after September 15, 2017. Learn more in [How to determine when an Evernote Teams account was created](https://help.evernote.com/hc/articles/115011455527) in the Evernote documentation.

You can find more information on Evernote in the [Evernote website](https://evernote.com/).

---

---
title: Install the connector
description: This section describes the common steps required to install the PingFederate Evernote Provisioner Connector.
component: evernote
page_id: evernote:setup:pf_evernote_connector_install_the_connector
canonical_url: https://docs.pingidentity.com/integrations/evernote/setup/pf_evernote_connector_install_the_connector.html
revdate: June 11, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Install the connector

## About this task

This section describes the common steps required to install the PingFederate Evernote Provisioner Connector.

## Steps

1. Download the Evernote Provisioner `.zip` archive from the [**Add-ons** tab of the PingFederate downloads page](https://www.pingidentity.com/en/resources/downloads/pingfederate.html) or the [Ping Identity Marketplace](https://marketplace.pingone.com/item/evernote-single-signon-integration).

2. Stop the PingFederate server if it is running.

3. Extract the Evernote Connector distribution `.zip` archive.

4. Copy the contents of the `dist` directory into the `<pf_install>/pingfederate/server/default/deploy` directory:

5. (Optional) If you plan to use the connector for outbound provisioning, edit the `run.properties` file located in `<pf_install>/pingfederate/bin`, changing the property `pf.provisioner.mode` to `STANDALONE`.

   For example: `pf.provisioner.mode=STANDALONE`

   |   |                                                                                                                                                                                                                                                        |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
   |   | Learn more about using the `FAILOVER` setting for runtime deployment in [Deploying provisioning failover](https://docs.pingidentity.com/pingfederate/latest/server_clustering_guide/pf_deploy_provis_failover.html) in the PingFederate documentation. |

6. Start the PingFederate server.

---

---
title: Known issues and limitations
description: Due to a limitation with PingFederate 8.1 and earlier versions, when configuring two SP connections with the same provisioner, the second connection built may be pre-populated with the channel from the first connection. To avoid conflicts, delete this pre-populated channel and create a unique channel for each connection.
component: evernote
page_id: evernote:release_notes:pf_evernote_connector_known_issues_and_limitations
canonical_url: https://docs.pingidentity.com/integrations/evernote/release_notes/pf_evernote_connector_known_issues_and_limitations.html
revdate: June 11, 2024
---

# Known issues and limitations

* Due to a limitation with PingFederate 8.1 and earlier versions, when configuring two SP connections with the same provisioner, the second connection built may be pre-populated with the channel from the first connection. To avoid conflicts, delete this pre-populated channel and create a unique channel for each connection.

* When an LDAP user is deleted in a targeted group distinguished name (DN), the provisioning connector does not propagate the deletion until a new user is added to the group. This limitation is compounded when the **User Create** provisioning option is disabled. Learn more in [SaaS provisioner does not remove the user](https://support.pingidentity.com/s/article/After-deleting-an-AD-user-account-SaaS-provisioner-does-not-remove-the-user-in-the-next-provisioning-cycle-when-Group-DN-is-specified) in the Ping Identity Knowledge Base.

* Due to PingFederate limitations, user attributes cannot be cleared after they're set.

* Provisioning disabled users from the User Store (LDAP) to Evernote is not supported.

* Due to Evernote API limitations, after a user is deactivated, they cannot be reactivated with the provisioner. A deactivated user can only be reactivated in the Evernote Teams Admin Console.

* Due to Evernote API limitations, new users cannot be created with the same username as a previously deactivated user.

---

---
title: Obtain PingFederate signing certificate
description: The following are the steps to obtain the signing certificate that is used for the digital signature verification of the PingFederate identity provider (IdP). When asked during Configure Evernote for SSO, provide the certificate that you have downloaded from PingFederate. Learn more in Managing digital signing certificates and decryption keys in the PingFederate documentation.
component: evernote
page_id: evernote:setup:pf_evernote_connector_obtain_pf_signing_certificate
canonical_url: https://docs.pingidentity.com/integrations/evernote/setup/pf_evernote_connector_obtain_pf_signing_certificate.html
revdate: June 11, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Obtain PingFederate signing certificate

## About this task

The following are the steps to obtain the signing certificate that is used for the digital signature verification of the PingFederate identity provider (IdP). When asked during [Configure Evernote for SSO](pf_evernote_connector_configure_evernote_for_sso.html), provide the certificate that you have downloaded from PingFederate. Learn more in [Managing digital signing certificates and decryption keys](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_certmanagementtasklet_dsigsigningcert_certmanagementstate.html) in the PingFederate documentation.

To export an existing certificate:

## Steps

1. Sign on to the PingFederate Administrative Console as an administrative user for your organization.

2. Go to **Server Configuration > Certificate Management > Signing & Decryption Keys & Certificates**.

3. Click **Export** under **Action** for the certificate you want to export.

4. On the **Export Certificate** screen, select **Certificate Only** export and then click **Next**.

5. On the **Export & Summary** screen, click **Export** to save the certificate file on your system.

6. Click **Done**.

7. Click **Cancel** to go back to the **Server Configuration** screen.

---

---
title: Supported attributes reference
description: The following table consists of the attributes that can be mapped for user provisioning.
component: evernote
page_id: evernote:setup:pf_evernote_connector_supported_attributes_reference
canonical_url: https://docs.pingidentity.com/integrations/evernote/setup/pf_evernote_connector_supported_attributes_reference.html
revdate: June 11, 2024
---

# Supported attributes reference

The following table consists of the attributes that can be mapped for user provisioning.

| Attribute    | Description                                                                                                                                       |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| Username     | Evernote's unique identifier for the user. The expected format is user\@domain (for example, 'bjensen\@example.com'). This attribute is required. |
| Display Name | The name of the user, suitable for display to users. This attribute is required.                                                                  |
| External ID  | A string that is an identifier for the resource as defined by the provisioning client.                                                            |

---

---
title: Upgrade an existing connector
description: Before stopping the PingFederate server to upgrade the Evernote Connector, go to the Attribute Mapping screen for existing channel configurations and note the current configuration.
component: evernote
page_id: evernote:setup:pf_evernote_connector_upgrade_an_existing_connector
canonical_url: https://docs.pingidentity.com/integrations/evernote/setup/pf_evernote_connector_upgrade_an_existing_connector.html
revdate: June 11, 2024
section_ids:
  steps: Steps
---

# Upgrade an existing connector

## Steps

1. Before stopping the PingFederate server to upgrade the Evernote Connector, go to the **Attribute Mapping** screen for existing channel configurations and note the current configuration.

   |   |                                                                                                                                                                             |
   | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | The upgrade process removes existing mappings and defaults on the **Attribute Mapping** screen. These must be configured again before activating the channel configuration. |

2. Disable the existing service provider (SP) connection where the Evernote Connector is configured.

3. Delete the existing Evernote Connector SP connection and save.

4. Stop the PingFederate server if it is running.

5. Extract the new Evernote Connector distribution `.zip` archive into a holding directory.

6. Remove any older versions of `pf-evernote-quickconnection-[version].jar` from:

   `<pf_install>/pingfederate/server/default/deploy`

7. Remove the following files from the same directory if they are present:

   * `evernote-business-provisioning-api-1.28.jar`

   * `pf-evernote-oauth-helper.war`

8. From the `dist` directory of the new version of the connector, copy the file:

   `pf-evernote-quickconnection-2.0.jar`

   into the directory:

   `<pf_install>/pingfederate/server/default/deploy`

9. Start the PingFederate server.

10. Create a new SP connection, using **Evernote Connector** as the connection template.

11. Follow instructions in [Configure PingFederate for SSO](pf_evernote_connector_configure_pf_for_sso.html) and [Configure PingFederate for provisioning](pf_evernote_connector_configure_pf_for_provisioning.html) in order to configure metadata.

12. Go to the **Attribute Mapping** screen for existing channel configurations and click **Refresh Fields**.

13. Ensure all new required fields (if any), are mapped appropriately or have a default value.

14. When you have completed the attribute configuration, click **Done**, **Done**, and **Save**.

15. Activate the SP connection to resume outbound provisioning.

---

---
title: User management
description: The Evernote Provisioner synchronizes users from your datastore to Evernote. The behavior of each provisioning capability is described below.
component: evernote
page_id: evernote::pf_evernote_connector_user_management
canonical_url: https://docs.pingidentity.com/integrations/evernote/pf_evernote_connector_user_management.html
revdate: June 11, 2024
section_ids:
  synchronizing-existing-users: Synchronizing existing users
  user-provisioning: User provisioning
  user-updates: User updates
  user-deprovisioning: User deprovisioning
---

# User management

The Evernote Provisioner synchronizes users from your datastore to Evernote. The behavior of each provisioning capability is described below.

You can configure these capabilities in the [Configure PingFederate for provisioning](setup/pf_evernote_connector_configure_pf_for_provisioning.html) step of the setup process.

## Synchronizing existing users

PingFederate synchronizes users based on the `Username` attribute in Evernote. If a user already exists in your datastore and Evernote, mapping this attribute correctly links the two records together.

For example:

* In Evernote, Janet's `Username` is `bjensen@example.com`.

* In your datastore, Janet's `mail` is `bjensen@example.com`.

* On the **Attribute Mapping** tab of your provisioning connection configuration, you map the `Username` attribute to `mail`.

* When the provisioning connector runs, the datastore user is provisioned with a `Username` of `bjensen@example.com`. That matches Janet's existing `Username` in Evernote, so her information in the datastore is synchronized to her Evernote account.

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