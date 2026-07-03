---
title: Changelog
description: Egnyte Connector 1.0 – January 2015 (current release)
component: egnyte
page_id: egnyte:release_notes:pf_egnyte_connector_changelog
canonical_url: https://docs.pingidentity.com/integrations/egnyte/release_notes/pf_egnyte_connector_changelog.html
revdate: June 10, 2024
---

# Changelog

**Egnyte Connector 1.0 – January 2015 (current release)**

* Initial release

* Added support for user provisioning

* Added support for browser-based single sign-on

---

---
title: Configure Egnyte for SSO
description: To proceed with configuring Egnyte for SSO, you will require the below details from PingFederate.
component: egnyte
page_id: egnyte:setup:pf_egnyte_connector_configure_egnyte_for_sso
canonical_url: https://docs.pingidentity.com/integrations/egnyte/setup/pf_egnyte_connector_configure_egnyte_for_sso.html
revdate: June 10, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Configure Egnyte for SSO

## About this task

To proceed with configuring Egnyte for SSO, you will require the below details from PingFederate.

* Identity provider login URL

  * Example: https\://*\<pf\_hostname>*:*\<pf\_port>*/idp/SSO.saml2

* Identity provider entity ID

  * This is the SAML 2.0 Entity ID from PingFederate, which can be found on the **Server Configuration > Server Settings > Federation Info** screen. For more information, see [Specifying federation information](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_protocolsettingstasklet_federationinfostate.html).

* Identity provider certificate

  * This is the public signing certificate from PingFederate used to sign the SAML assertion (configured in your SP connection). For more information, see [Manage digital signing certificates and decryption keys](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_certmanagementtasklet_dsigsigningcert_certmanagementstate.html).

The following section describes the steps to configure SSO in Egnyte. For more information, see [Single Sign-On (SSO) Configuration](https://helpdesk.egnyte.com/hc/en-us/articles/201638954-Single-Sign-On-SSO-Configuration).

|   |                                                                                                                                                                                                                                                                                                                                                                             |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | For users to sign in through SAML SSO, their authType attribute must be set to 'sso'. The authType attribute may be set when the user is provisioned or by an administrator on the user's profile under **Settings > Configuration > Users & Groups**. For more information, see [Supported attributes reference](pf_egnyte_connector_supported_attributes_reference.html). |

## Steps

1. Log in to your Egnyte subdomain as an administrative user for your organization.

2. Navigate to **Settings > Configuration > Security & Authentication**.

3. Under the **Single Sign-on Authentication** section:

   * Select SAML 2.0 as the **Single sign-on authentication** type.

   * Select PingFederate as the **Identity provider**.

   * Set the **Identity provider login URL**, **Identity provider entity ID**, and **Identity provider certificate**.

     |   |                                                                                                                                                                             |
     | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
     |   | The **Identity provider certificate** is the PEM-encoded X.509 certificate from PingFederate. Paste the entire certificate, but remove the BEGIN and END CERTIFICATE lines. |

   * Set the **Default user mapping**. The value of the SAML\_SUBJECT sent in your SP connection's attribute contract must match this mapping.

   * Optional: Set the **User domain-specific Issuer value** based on your business use.

     ![An image of a Single Sign-On Authentication sample configuration in Egnyte.](_images/dkt1563995302634.png)

4. Click the **Save** button.

---

---
title: Configure PingFederate for SSO
description: "The following section describes the steps for configuring single sign-on (SSO) to Egnyte. Configuring SAML SSO involves configuring both the PingFederate SP connection and Egnyte SSO screens. NOTE: Configuring SSO is optional for outbound provisioning."
component: egnyte
page_id: egnyte:setup:pf_egnyte_connector_configure_pf_for_sso
canonical_url: https://docs.pingidentity.com/integrations/egnyte/setup/pf_egnyte_connector_configure_pf_for_sso.html
revdate: June 10, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Configure PingFederate for SSO

## About this task

The following section describes the steps for configuring single sign-on (SSO) to Egnyte. Configuring SAML SSO involves configuring both the PingFederate SP connection and Egnyte SSO screens. NOTE: Configuring SSO is optional for outbound provisioning.

## Steps

1. Create a new SP connection or select an existing SP connection from the **SP Configuration** menu.

2. On the **Connection Template** screen, select **Use a template for this connection** and choose **Egnyte** from the **Connection Template** drop-down list. When asked during the connection configuration steps, import the `egnyte-saml-metadata.xml` you prepared earlier in [Obtain Egnyte SAML 2.0 metadata](pf_egnyte_connector_obtain_egnyte_saml_20_metadata.html).

   ![Image of the Connection Template screen.](_images/ium1563995291929.png)

   |   |                                                                                                 |
   | - | ----------------------------------------------------------------------------------------------- |
   |   | If this selection is not available, verify the connector installation and restart PingFederate. |

3. On the **Connection Type** screen, ensure the **Outbound Provisioning** check box is selected, and the **Browser SSO Profiles** check box is cleared (if appropriate).

4. On the **General Info** screen, the default values are taken from the metadata file you selected in step 2.

   ![Image of the General Info screen.](_images/npb1563995293321.png)

5. Click **Next** to continue the Browser SSO configuration. For more information, see the following sections under [Identity provider SSO configuration](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_ident_provid_sso_config.html):

   * [Managing IdP adapters](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_managing_idp_adapters.html)

   * [Configure IdP Browser SSO](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_spconnectionconfigtasklet_spbrowserssostate.html)

   * [Configuring credentials](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_spconnectionconfigtasklet_credentialsstate.html)

     |   |                                                                                                                                                                                                                                                                            |
     | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
     |   | The SAML\_SUBJECT configured on the **IdP Adapter Mapping > Attribute Contract Fulfillment** screen must match the **Default user mapping** configured in Egnyte. For more information, see [Configure Egnyte for SSO](pf_egnyte_connector_configure_egnyte_for_sso.html). |

6. On the **Protocol Settings > Allowable SAML Bindings** screen, ensure that both **POST** and **Redirect** are selected.

7. On the **Credentials > Digital Signature Settings** screen, select the signing certificate.

8. On the **Activation & Summary** screen, set **Connection Status** to Active, then click **Save**.

   |   |                                                                                                                                                                                                                                                 |
   | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | If you are not ready to complete the SSO configuration, you can click **Save** and return to the configuration page later. To return to the configuration page, select the connection from **Identity Provider > SP Connections > Manage All**. |

---

---
title: Configure provisioning
description: To configure a connection for outbound provisioning to Egnyte, follow the instructions in this section. Outbound provisioning details are managed within an SP connection and may be added to an existing SP connection.
component: egnyte
page_id: egnyte:setup:pf_egnyte_connector_configure_provisioning
canonical_url: https://docs.pingidentity.com/integrations/egnyte/setup/pf_egnyte_connector_configure_provisioning.html
revdate: June 10, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Configure provisioning

## About this task

To configure a connection for outbound provisioning to Egnyte, follow the instructions in this section. Outbound provisioning details are managed within an SP connection and may be added to an existing SP connection.

## Steps

1. In the PingFederate administrator console, configure the data store that PingFederate will use as the source of user data. For instructions, see [Datastores](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_managedatasourcestasklet_managedatasourcesstate.html) in the PingFederate documentation.

   * When targeting users and groups for provisioning, exclude the user account that you will use to administer users in your connection to Egnyte. This prevents the PingFederate provisioning engine from interfering with the account that provisions users and groups.

2. Create a new SP connection or select an existing SP connection from the **SP Configuration** menu.

3. On the **Connection Template** screen, select **Use a template for this connection** and choose **Egnyte** from the **Connection Template** drop-down list. When asked during the connection configuration steps, import the `egnyte-saml-metadata.xml` you prepared earlier in [Obtain Egnyte SAML 2.0 metadata](pf_egnyte_connector_obtain_egnyte_saml_20_metadata.html).

   ![An image of the Connection Template screen.](_images/ium1563995291929.png)

   |   |                                                                                                 |
   | - | ----------------------------------------------------------------------------------------------- |
   |   | If this selection is not available, verify the connector installation and restart PingFederate. |

4. On the **Connection Type** screen, ensure the **Outbound Provisioning** check box is selected, and the **Browser SSO Profiles** check box is cleared (if appropriate).

5. On the **General Info** screen, the default values are taken from the metadata file you selected in step 2.

   ![Image of the General Info screen.](_images/npb1563995293321.png)

6. Follow the connection wizard to configure the connection.

7. On the **Outbound Provisioning** screen, click **Configure Provisioning**.

8. On the **Target** screen, enter the values for each field as required by the Egnyte Connector.

   ![Image of the Target screen.](_images/swp1563995294589.png)

   **Target screen options**

   | Field Name               | Description                                                                                                                                                                                      |
   | ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
   | **OAuth\_Access\_Token** | The OAuth access token for the Egnyte account. For more information, see [Obtain access token](pf_egnyte_connector_obtain_access_token.html).                                                    |
   | **Subdomain**            | The subdomain portion of the URL used to access your organization's Egnyte. For example, if the URL used to access Egnyte is https\://*myCompany*.egnyte.com/ then the subdomain is *myCompany*. |

9. Click **Next** to continue the provisioning configuration. For more information, see the following sections under [Outbound provisioning for IdPs](https://docs.pingidentity.com/pingfederate/latest/introduction_to_pingfederate/pf_outboun_provis_for_idp.html) in the PingFederate documentation:

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
title: Configure SAML SSO
description: The following section describes the steps for configuring single sign-on (SSO) to Egnyte.
component: egnyte
page_id: egnyte:setup:pf_egnyte_connector_configure_saml_sso
canonical_url: https://docs.pingidentity.com/integrations/egnyte/setup/pf_egnyte_connector_configure_saml_sso.html
revdate: June 10, 2024
---

# Configure SAML SSO

The following section describes the steps for configuring single sign-on (SSO) to Egnyte.

|   |                                                        |
| - | ------------------------------------------------------ |
|   | Configuring SSO is optional for outbound provisioning. |

* [Configure Egnyte for SSO](pf_egnyte_connector_configure_egnyte_for_sso.html)

* [Configure PingFederate for SSO](pf_egnyte_connector_configure_pf_for_sso.html)

---

---
title: Download manifest
description: The distribution .zip archive for the connector contains the following:
component: egnyte
page_id: egnyte:release_notes:pf_egnyte_connector_download_manifest
canonical_url: https://docs.pingidentity.com/integrations/egnyte/release_notes/pf_egnyte_connector_download_manifest.html
revdate: June 10, 2024
---

# Download manifest

The distribution `.zip` archive for the connector contains the following:

* `ReadMeFirst.pdf` – contains links to this online documentation.

* `egnyte-saml-metadata.xml` – SAML metadata file for use with an Egnyte connection. For more information, see [Obtain Egnyte SAML 2.0 metadata](../setup/pf_egnyte_connector_obtain_egnyte_saml_20_metadata.html).

* `/legal`:

  * `Legal.pdf` – copyright and license information.

* `/dist` – contains libraries needed for the connector:

  * `pf-egnyte-quickconnection-1.0.0.2.jar` – PingFederate Egnyte Connector

  * `prov-cpl-2.0.1.jar` – PingFederate Common Provisioning Layer

  * `gson.2.2.4.jar` – Used to serialize and deserialize objects in the Egnyte Connector

---

---
title: Egnyte Provisioner
description: The PingFederate Egnyte Provisioner enables an enterprise to provision users to Egnyte. A quick connection template is also included to simplify the configuration of single sign-on (SSO).
component: egnyte
page_id: egnyte::pf_egnyte_connector
canonical_url: https://docs.pingidentity.com/integrations/egnyte/pf_egnyte_connector.html
revdate: June 10, 2024
section_ids:
  features: Features
  intended-audience: Intended audience
  system-requirements: System requirements
---

# Egnyte Provisioner

The PingFederate Egnyte Provisioner enables an enterprise to provision users to Egnyte. A quick connection template is also included to simplify the configuration of single sign-on (SSO).

## Features

* Browser-based SP and IdP-initiated SSO

* Includes support for user life cycle management (including creates, updates, and disables).

## Intended audience

This document is intended for PingFederate administrators.

If you need help during the setup process, see the following sections of the PingFederate documentation:

* [SP connection management](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_sp_connect_management.html)

* [Identity provider SSO configuration](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_ident_provid_sso_config.html)

* [Datastores](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_datastores.html)

* [Configuring outbound provisioning](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_spconnectionconfigtasklet_saasprovisioningstate.html)

* [Configuring outbound provisioning settings](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_protocolsettingstasklet_saasglobalprovisioningsettingsstate.html)

## System requirements

* PingFederate 7.3 or later with Java 8

* Might require the following endpoints to be whitelisted on the firewall to allow outbound connections:

  * The URL used to access your organization's Egnyte. For example, https\://*myCompany*.egnyte.com/

For additional details on Egnyte, see the [Egnyte website](https://www.egnyte.com/).

---

---
title: Enable outbound provisioning
description: After enabling outbound provisioning in the <pf_install>/pingfederate/bin/run.properties file, you must also activate the outbound provisioning role in the administrative console.
component: egnyte
page_id: egnyte:setup:pf_egnyte_connector_enable_outbound_provisioning
canonical_url: https://docs.pingidentity.com/integrations/egnyte/setup/pf_egnyte_connector_enable_outbound_provisioning.html
revdate: June 10, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Enable outbound provisioning

## About this task

After enabling outbound provisioning in the `<pf_install>/pingfederate/bin/run.properties` file, you must also activate the outbound provisioning role in the administrative console.

## Steps

1. Go to the **Server Configuration > Server Settings > Roles & Protocols** screen.

2. Select the **Outbound Provisioning** check box.

   ![An image of the Roles & Protocols screen.](_images/wia1563995299735.png)

   |   |                                                                                                                                                                                                                                                                                                                                                                                                                         |
   | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | Enabling outbound provisioning adds the outbound provisioning screen, requiring the selection of a database to facilitate provisioning. For more information, see [Configuring outbound provisioning settings](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_protocolsettingstasklet_saasglobalprovisioningsettingsstate.html) or click **Help** from the configuration screen. |

---

---
title: Install the connector
description: This section describes the common steps required to install the PingFederate Egnyte Connector.
component: egnyte
page_id: egnyte:setup:pf_egnyte_connector_install_the_connector
canonical_url: https://docs.pingidentity.com/integrations/egnyte/setup/pf_egnyte_connector_install_the_connector.html
revdate: June 10, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Install the connector

## About this task

This section describes the common steps required to install the PingFederate Egnyte Connector.

## Steps

1. Download the Egnyte Provisioner `.zip` archive from the [**Add-ons** tab of the PingFederate downloads page](https://www.pingidentity.com/en/resources/downloads/pingfederate.html) or the [Ping Identity Marketplace](https://marketplace.pingone.com/item/egnyte-single-signon-integration).

2. Stop the PingFederate server if it is running.

3. Extract the Egnyte Connector distribution `.zip` archive.

4. Copy the contents of the `dist` directory into the `<pf_install>/pingfederate/server/default/deploy` directory.

5. (Optional) If you plan to use the connector for outbound provisioning, edit the `run.properties` file located in `<pf_install>/pingfederate/bin`, changing the property `pf.provisioner.mode` to `STANDALONE`.

   For example: `pf.provisioner.mode=STANDALONE`

   |   |                                                                                                                                                                                                                                                  |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
   |   | To configure the `FAILOVER` mode instead, learn more in [Deploying provisioning failover](https://docs.pingidentity.com/pingfederate/latest/server_clustering_guide/pf_deploy_provis_failover.html) in the PingFederate server clustering guide. |

6. Start the PingFederate server.

---

---
title: Known issues and limitations
description: Due to a limitation with PingFederate 8.1 and earlier versions, when configuring two SP connections with the same provisioner, the second connection built may be pre-populated with the channel from the first connection. To avoid conflicts, delete this pre-populated channel and create a unique channel for each connection.
component: egnyte
page_id: egnyte:release_notes:pf_egnyte_connector_known_issues_and_limitations
canonical_url: https://docs.pingidentity.com/integrations/egnyte/release_notes/pf_egnyte_connector_known_issues_and_limitations.html
revdate: June 10, 2024
---

# Known issues and limitations

* Due to a limitation with PingFederate 8.1 and earlier versions, when configuring two SP connections with the same provisioner, the second connection built may be pre-populated with the channel from the first connection. To avoid conflicts, delete this pre-populated channel and create a unique channel for each connection.

* When an LDAP user is deleted in a targeted group distinguished name (DN), the provisioning connector does not propagate the deletion until a new user is added to the group. This limitation is compounded when the **User Create** provisioning option is disabled. For solutions, see [SaaS provisioner does not remove the user](https://support.pingidentity.com/s/article/After-deleting-an-AD-user-account-SaaS-provisioner-does-not-remove-the-user-in-the-next-provisioning-cycle-when-Group-DN-is-specified) in the Knowledge Base.

* Due to PingFederate limitations, user attributes cannot be cleared once set.

* Due to an issue that has been reported to the service provider, users that have had their authType set to 'sso' will no longer be able to log in with their standard username and password.

* Due to an issue that has been reported to the service provider, the service provider returns an HTTP status code of 500 on some requests to update a user.

* Due to a limitation with the service provider's API, a user's role can only be updated through the service provider's administrative console.

**Performance limitations**

* Due to Egnyte API limitations, API calls are rate limited. This will prevent requests from being completed. For more information, see [Frequently Asked Questions](https://developers.egnyte.com/Frequently_Asked_Questions) on the Egnyte developers site.

---

---
title: Obtain access token
description: Once you have obtained your API key, you are able to use it to generate an access token using cURL.
component: egnyte
page_id: egnyte:setup:pf_egnyte_connector_obtain_access_token
canonical_url: https://docs.pingidentity.com/integrations/egnyte/setup/pf_egnyte_connector_obtain_access_token.html
revdate: June 10, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Obtain access token

## About this task

Once you have obtained your API key, you are able to use it to generate an access token using [cURL](http://curl.haxx.se/docs/manpage.html).

|   |                                                                                                                                                                                                                                                                       |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | After creating your application, Egnyte must approve it before you can use the API key to generate your access token. For more information, see [Frequently Asked Questions](https://developers.egnyte.com/Frequently_Asked_Questions) on the Egnyte developers site. |

## Steps

1. From an application or terminal capable of running cURL commands, run the following cURL command:

   ```shell
   curl -v --request POST -H "Content-Type: application/x-www-form-urlencoded"
   -d grant_type=password -d username=YOUR_USERNAME -d password=YOUR_PASSWORD
   -d client_id=YOUR_API_KEY https://YOUR_SUBDOMAIN.egnyte.com/puboauth/token
   ```

   where:

   * *YOUR\_USERNAME* is the username of an administrative user on the Egnyte subdomain you wish to provision users.

     |   |                                                                                                                                                |
     | - | ---------------------------------------------------------------------------------------------------------------------------------------------- |
     |   | The administrative user for you Egnyte subdomain is not the same account that you used to generate the application on Egnyte's developer site. |

   * *YOUR\_PASSWORD* is the password for the administrative user of your Egnyte subdomain.

   * *YOUR\_API\_KEY* is the API key identified in [Obtain API key](pf_egnyte_connector_obtain_api_key.html).

   * *YOUR\_SUBDOMAIN* is the subdomain portion of the URL used to access your organization's Egnyte. For example, if the URL used to access Egnyte is https\://*myCompany*.egnyte.com/ then the subdomain is *myCompany*.

2. Note the presented access token for later use in [Configure provisioning](pf_egnyte_connector_configure_provisioning.html). ![An image of the cURL command and expected access token results.](_images/sri1563995295504.jpg)

---

---
title: Obtain API key
description: The Egnyte Connector's outbound provisioning functionality is built using Egnyte's REST API, which requires an authorized OAuth 2.0 access token. To generate your access token in Obtain access token, you will first need to obtain an API key.
component: egnyte
page_id: egnyte:setup:pf_egnyte_connector_obtain_api_key
canonical_url: https://docs.pingidentity.com/integrations/egnyte/setup/pf_egnyte_connector_obtain_api_key.html
revdate: June 10, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Obtain API key

## About this task

The Egnyte Connector's outbound provisioning functionality is built using Egnyte's REST API, which requires an authorized OAuth 2.0 access token. To generate your access token in [Obtain access token](pf_egnyte_connector_obtain_access_token.html), you will first need to obtain an API key.

To obtain an API key, you will need to have a registered account on [Egnyte's developer site](https://developers.egnyte.com/). The developer site will be used to create an application which will contain the API key. The following steps will be used to create your application and obtain the API key:

## Steps

1. Log in to [Egnyte's developer site](https://developers.egnyte.com/) with an administrative developer account.

2. Go to **My Account > Applications > Create a New Application**.

3. Complete the form to register your new application with the following options:

   * Enter a name for the application.

   * Set the **Type** to **Internal Application (own company use only)**.

   * Set the **Current User Base** to **New App**.

   * Set the **Platform** to **Other**.

   * Set the **Egnyte domain you will use for testing** to your Egnyte subdomain. This is the subdomain portion of the URL used to access your organization's Egnyte. For example, if the URL used to access Egnyte is https\://*myCompany*.egnyte.com/ then the subdomain is *myCompany*.

   * Ensure the **Issue a new key for Egnyte REST API** check box is selected.

   * Select the check box, indicating that you have read and agree to the [Egnyte API Terms of Service](https://developers.egnyte.com/apps/tos) and click the **Register Application** button.

4. Once your application is registered, note the **Key** for later use in [Obtain access token](pf_egnyte_connector_obtain_access_token.html).

   ![An image of the registered application.](_images/fyp1563995297225.png)

   |   |                                                                                                                                                                                                                                                                                                                |
   | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | After creating your application, Egnyte must approve it before you can use the API key to generate your access token in [Obtain access token](pf_egnyte_connector_obtain_access_token.html). For more information, see [Frequently Asked Questions](https://developers.egnyte.com/Frequently_Asked_Questions). |

---

---
title: Obtain Egnyte SAML 2.0 metadata
description: The connector's quick-connection template uses a metadata XML file to assist in configuring many settings in the SP connection. When asked during the connection configuration steps, import the egnyte-saml-metadata.xml packaged with this connector.
component: egnyte
page_id: egnyte:setup:pf_egnyte_connector_obtain_egnyte_saml_20_metadata
canonical_url: https://docs.pingidentity.com/integrations/egnyte/setup/pf_egnyte_connector_obtain_egnyte_saml_20_metadata.html
revdate: June 27, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Obtain Egnyte SAML 2.0 metadata

## About this task

The connector's quick-connection template uses a metadata XML file to assist in configuring many settings in the SP connection. When asked during the connection configuration steps, import the `egnyte-saml-metadata.xml` packaged with this connector.

To prepare your metadata.xml:

## Steps

1. Open the `egnyte-saml-metadata.xml` file packaged with the connector in a text editor of your choice.

2. Replace all instances of *SUBDOMAIN* with the subdomain portion of the URL used to access your organization's Egnyte.

   For example, if the URL used to access Egnyte is https\://*myCompany*.egnyte.com/ then the *SUBDOMAIN* is *myCompany*.

3. Once you have updated the *SUBDOMAIN*, save the metadata file changes.

---

---
title: Supported attributes reference
description: The following table consists of the attributes that can be mapped on a user during provisioning. For more information, see the Egnyte User Management API.
component: egnyte
page_id: egnyte:setup:pf_egnyte_connector_supported_attributes_reference
canonical_url: https://docs.pingidentity.com/integrations/egnyte/setup/pf_egnyte_connector_supported_attributes_reference.html
revdate: June 10, 2024
---

# Supported attributes reference

The following table consists of the attributes that can be mapped on a user during provisioning. For more information, see the Egnyte [User Management API](https://developers.egnyte.com/docs/User_Management_API_Documentation).

|                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Attribute**     | **Description**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| email             | The Egnyte username for the user. This attribute is required.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| authType          | The authentication type for the user. This attribute is required. Available options include:- ad (Active Directory) – Users with their `authType` set to this option will be able to authenticate through Active Directory. This requires your Egnyte domain to be configured for **Active Directory Authentication** under **Settings > Configuration > Security & Authentication**. When setting this option on a user, the user must also have a userPrincipalName set.

- sso (SAML SSO) – Users with their `authType` set to this option will be able to authenticate using single sign-on (SSO). This requires your Egnyte domain to be configured for **Single Sign-on Authentication** under **Settings > Configuration > Security & Authentication**. When setting this option on a user, the user must also have an idpUserId set.

- egnyte (Internal Egnyte) – Users with their authType set to this option will be able to log in to Egnyte using their Egnyte account credentials. |
| externalId        | An immutable unique identifier for the user. This can be any plain text value identifier. This attribute is required. WARNING: This field is immutable meaning once set, it can never be updated.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| familyName        | The last name of the user. This attribute is required.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| givenName         | The first name of the user. This attribute is required.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| sendInvite        | If set to true when creating a user, an invitation email will be sent if the user is created in active state in the LDAP data store. If the user is disabled in the LDAP data store when they are created, no email is sent. This attribute is required. Available options include:- true

- false                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| userName          | The Egnyte username for the user. This attribute is required.	Usernames must start with a letter or digit. Special characters are not supported (with the exception of periods, hyphens, and underscores).	It is not possible to change a user's userName after they are created.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| userType          | The type of the user. This attribute is required. Acceptable options include:- admin

- power

- standard                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| idpUserId         | Only required if the user's authType is set to 'sso'.This is how the user is identified within the SAML response from an SSO identity provider. For example, the SAML subject 'bjensen' or '<bjensen@example.com>'.&#xA;&#xA;The idpUserId of a user must match the Default user mapping configured in Egnyte. For more information, see Configure Egnyte for SSO.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| role              | The role assigned to the user. Available options include 'default' or other existing custom role names.	This option is only available to users with a userType of 'power'.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| userPrincipalName | Only required if the user's authType is set to 'ad'.This field is used to bind child authentication policies to a user when using Active Directory authentication in a multi-domain setup. For example, 'bjensen\@example.com'.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |

---

---
title: User management
description: The Egnyte Provisioner synchronizes users from your datastore to Egnyte. The behavior of each provisioning capability is described below.
component: egnyte
page_id: egnyte::pf_egnyte_connector_user_management
canonical_url: https://docs.pingidentity.com/integrations/egnyte/pf_egnyte_connector_user_management.html
revdate: June 10, 2024
section_ids:
  synchronizing-existing-users: Synchronizing existing users
  user-provisioning: User provisioning
  user-updates: User updates
  user-deprovisioning: User deprovisioning
---

# User management

The Egnyte Provisioner synchronizes users from your datastore to Egnyte. The behavior of each provisioning capability is described below.

You can configure these capabilities in the [Configure provisioning](setup/pf_egnyte_connector_configure_provisioning.html) step of the setup process.

## Synchronizing existing users

PingFederate synchronizes users based on the `Username` attribute in Egnyte. If a user already exists in your datastore and Egnyte, mapping this attribute correctly links the two records together.

For example:

* In Egnyte, Janet's `Username` is `bjensen@example.com`.

* In your datastore, Janet's `mail` is `bjensen@example.com`.

* On the **Attribute Mapping** tab of your provisioning connection configuration, you map the `Username` attribute to `mail`.

* When the provisioning connector runs, the datastore user is provisioned with a `Username` of `bjensen@example.com`. That matches Janet's existing `Username` in Egnyte, so her information in the datastore is synchronized to her Egnyte account.

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