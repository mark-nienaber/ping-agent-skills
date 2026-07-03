---
title: Adding PingFederate as an authentication provider in Code42
description: To allow PingFederate to coordinate authentication with Code42, upload your SAML metadata.
component: code42-pingfederate
page_id: code42-pingfederate:single_sign-on_setup:pf_code42_integration_adding_pf_as_an_authentication_provider_in_code42
canonical_url: https://docs.pingidentity.com/integrations/code42-pingfederate/single_sign-on_setup/pf_code42_integration_adding_pf_as_an_authentication_provider_in_code42.html
revdate: June 26, 2024
section_ids:
  steps: Steps
---

# Adding PingFederate as an authentication provider in Code42

To allow PingFederate to coordinate authentication with Code42, upload your SAML metadata.

## Steps

1. Sign on to Code42 as an administrator.

2. Navigate to **Integrations > Identity Management**.

3. On the **Authentication** tab, click **Add authentication provider**.

4. On the **Add authentication provider** dialog, enter a name and select **Upload file**. Select the file that you exported in [Exporting SAML metadata from PingFederate](pf_code42_integration_exporting_saml_metadata_from_pf.html). Click **Create Provider**.

5. On the provider detail page, note the **Code42 Service Provider Metadata URL**.

---

---
title: Adding PingFederate as SCIM provider in Code42
description: To get your base URL and credentials to access Code42 API, add PingFederate as a SCIM provider.
component: code42-pingfederate
page_id: code42-pingfederate:provisioning_setup:pf_code42_integration_adding_pf_as_scim_provider_in_code42
canonical_url: https://docs.pingidentity.com/integrations/code42-pingfederate/provisioning_setup/pf_code42_integration_adding_pf_as_scim_provider_in_code42.html
revdate: June 26, 2024
section_ids:
  steps: Steps
---

# Adding PingFederate as SCIM provider in Code42

To get your base URL and credentials to access Code42 API, add PingFederate as a SCIM provider.

## Steps

1. Sign on to Code42 as an administrator.

2. Navigate to **Integrations > Identity Management**.

3. On the **Provisioning** tab, click **Add provisioning provider**, and then click **Add SCIM provider**.

4. On the **Add SCIM provisioning** dialog, enter a name and select the **OAuth token** credential type. Click **Next**.

5. On the **SCIM Provider Created** dialog, note the **Base URL** and **Token** values. You will use these in [Creating a provisioning connection](pf_code42_integration_creating_a_provisioning_connection.html). Click **Done**.

---

---
title: Code42 Integration Guide for PingFederate
description: You can integrate PingFederate with Code42 for user provisioning and single sign-on (SSO). This integration uses the downloadable SCIM Connector.
component: code42-pingfederate
page_id: code42-pingfederate::pf_code42_integration
canonical_url: https://docs.pingidentity.com/integrations/code42-pingfederate/pf_code42_integration.html
revdate: June 26, 2024
section_ids:
  features: Features
  intended-audience: Intended audience
  system-requirements: System requirements
---

# Code42 Integration Guide for PingFederate

You can integrate PingFederate with Code42 for user provisioning and single sign-on (SSO). This integration uses the downloadable SCIM Connector.

## Features

* Manages users in Code42 based on changes in a datastore that is attached to PingFederate.

  * Creates, updates, and disables users.

  * Allows you to enable the create, update, and disable capabilities independently.

* Enables browser-based single sign-on initiated by the service provider (SP).

## Intended audience

This document is intended for PingFederate administrators.

If you need help during the setup process, see the following resources:

* The following sections of the PingFederate documentation:

  * [Identity provider SSO configuration](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_ident_provid_sso_config.html)

  * [Datastores](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_managedatasourcestasklet_managedatasourcesstate.html)

  * [Managing IdP adapters](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_managing_idp_adapters.html)

  * [Managing digital signing certificates and decryption keys](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_certmanagementtasklet_dsigsigningcert_certmanagementstate.html)

  * [SP connection management](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_sp_connect_management.html)

  * [Configuring outbound provisioning](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_spconnectionconfigtasklet_saasprovisioningstate.html)

  * [Configuring outbound provisioning settings](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_protocolsettingstasklet_saasglobalprovisioningsettingsstate.html)

* The following sections of the Code42 documentation:

  * [Identity management](https://support.code42.com/Administrator/Cloud/Configuring/Identity_management)

  * [Identity management reference](https://support.code42.com/Administrator/Cloud/Code42_console_reference/Identity_management_reference#Authentication)

  * [Introduction to SCIM provisioning](https://support.code42.com/Administrator/Cloud/Configuring/Introduction_to_SCIM_provisioning)

  * [How to configure SCIM provisioning](https://support.code42.com/Administrator/Cloud/Configuring/Introduction_to_SCIM_provisioning/How_to_configure_provisioning)

  * [Introduction to single sign-on](https://support.code42.com/Administrator/Cloud/Configuring/Identity_management/Introduction_to_single_sign-on)

* The following sections of the SCIM Connector documentation:

  * [SCIM Provisioner](../scim/pf_scim_connector.html)

  * [Known issues and limitations](../scim/release_notes/pf_scim_connector_known_issues_and_limitations.html)

## System requirements

* PingFederate 9.0 or later.

* The Ping Identity SCIM Connector integration. See [Deploying the integration files](pf_code42_integration_deploying_the_integration_files.html).

* To allow PingFederate to make outbound connections to the Code42 API, you might need to allow the following domain in your firewall:

  * https\://\*.code42.com

---

---
title: Creating a channel
description: Integrating PingFederate with Code42 requires a specific attribute mapping configuration.
component: code42-pingfederate
page_id: code42-pingfederate:provisioning_setup:pf_code42_integration_creating_a_channel
canonical_url: https://docs.pingidentity.com/integrations/code42-pingfederate/provisioning_setup/pf_code42_integration_creating_a_channel.html
revdate: June 26, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Creating a channel

Integrating PingFederate with Code42 requires a specific attribute mapping configuration.

## About this task

For general information about creating a channel, see [Managing channels](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_saasmanagementtasklet_saasmanagementstate.html) in the PingFederate documentation

For more information about the attributes available in your channel configuration, see [Supported attributes reference](pf_code42_integration_supported_attributes_reference.html).

## Steps

1. On the **Manage Channels** tab, click **Create**.

2. On the **Channel Info** tab, in the **Channel Name** field, enter a name for the channel. Click **Next**.

3. On the **Source** tab, from the **Active Data Store** list, select the data store that you created in [Creating a provisioning connection](pf_code42_integration_creating_a_provisioning_connection.html). Click **Next**.

4. On the **Source Settings** and **Source Location** tabs, complete the configuration based on your environment.

5. On the **Attribute Mapping** tab, configure the attributes. You can use the following LDAP mappings, or adapt them for your data store type. Click **Next**.

   | Code42 attribute | Data store attribute                                                                                                                                                                                                                                                                                                                             |
   | ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
   | `userName`       | `mail`                                                                                                                                                                                                                                                                                                                                           |
   | `workEmail`      | `mail`                                                                                                                                                                                                                                                                                                                                           |
   | `department`     | `department`                                                                                                                                                                                                                                                                                                                                     |
   | `division`       | `division`                                                                                                                                                                                                                                                                                                                                       |
   | `externalId`     | `objectGUID`                                                                                                                                                                                                                                                                                                                                     |
   | `familyName`     | `sn`                                                                                                                                                                                                                                                                                                                                             |
   | `givenName`      | `givenName`                                                                                                                                                                                                                                                                                                                                      |
   | `manager`        | Populate this attribute with the Code42 ID that represents this user's manager.For example, Jake's manager Alice has a user ID of `123098456876789543` in Code42. In Active Directory, you set Jake's `msDS-cloudExtensionAttribute10` attribute to `123098456876789543`.Then, map this `manager` attribute to `msDS-cloudExtensionAttribute10`. |
   | `title`          | `title`                                                                                                                                                                                                                                                                                                                                          |
   | `userType`       | `employeeType`                                                                                                                                                                                                                                                                                                                                   |
   | `workCity`       | `l`(lowercase "L")                                                                                                                                                                                                                                                                                                                               |
   | `workCountry`    | `c`                                                                                                                                                                                                                                                                                                                                              |
   | `workState`      | `st`                                                                                                                                                                                                                                                                                                                                             |
   | `workStreet`     | `streetAddress`                                                                                                                                                                                                                                                                                                                                  |
   | `workPostalCode` | `postalCode`                                                                                                                                                                                                                                                                                                                                     |

---

---
title: Creating a provisioning connection
description: To allow PingFederate to manage users in Code42 using SCIM, create a service provider (SP) connection.
component: code42-pingfederate
page_id: code42-pingfederate:provisioning_setup:pf_code42_integration_creating_a_provisioning_connection
canonical_url: https://docs.pingidentity.com/integrations/code42-pingfederate/provisioning_setup/pf_code42_integration_creating_a_provisioning_connection.html
revdate: June 26, 2024
section_ids:
  steps: Steps
---

# Creating a provisioning connection

To allow PingFederate to manage users in Code42 using SCIM, create a service provider (SP) connection.

## Steps

1. In the PingFederate administrator console, create a new SP connection:

   * For PingFederate 10.1 or later: go to **Applications > Integration > SP Connections**. Click **Create Connection**.

   * For PingFederate 10.0 or earlier: go to **Identity Provider > SP Connections**. Click **Create Connection**.

2. Configure the basic connection details.

   1. On the **Connection Template** tab, select **Do not use a template for this connection**. Click **Next**

   2. On the **Connection Type** tab, select only **Outbound Provisioning**. From the **Type** list, select **SCIM Connector**. Click **Next**.

   3. On the **General Info** tab, in the **Partner's Entity ID** and **Connection Name** fields, enter a name of your choosing. Complete any other optional fields. Click **Next**.

3. On the **Outbound Provisioning** tab, configure the provisioning target and channel. Click **Next**.

   For help, see [Configuring outbound provisioning](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_spconnectionconfigtasklet_saasprovisioningstate.html) in the PingFederate documentation.

   1. Click **Configure Provisioning**.

   2. On the **Target** tab, in the **SCIM URL** field, enter the **Base URL** that you noted in [Adding PingFederate as SCIM provider in Code42](pf_code42_integration_adding_pf_as_scim_provider_in_code42.html).

   3. From the **SCIM Version** list, check that **2.0** is selected.

   4. From the **Authentication Method** list, select **Basic Authentication** or **OAuth 2 Bearer Token** based on the authentication method you selected in [Adding PingFederate as SCIM provider in Code42](pf_code42_integration_adding_pf_as_scim_provider_in_code42.html).

   5. In the **Username** and **Password** fields or **Access Token** field, enter the authentication details that you noted in [Adding PingFederate as SCIM provider in Code42](pf_code42_integration_adding_pf_as_scim_provider_in_code42.html).

      |   |                                                                                                   |
      | - | ------------------------------------------------------------------------------------------------- |
      |   | PingFederate verifies the authentication details when you activate the channel and SP connection. |

   6. From the **Unique User Identifier** list, select **userName**.

   7. From the **Remove User Action** list, select **Disable**.

   8. Under **Provisioning Options**, customize the provisioning connector actions as shown in [SCIM Connector settings reference for Code42](pf_code42_integration_scim_connector_settings_reference_for_code42.html). Click **Next**.

   9. On the **Manage Channels** tab, follow the steps in [Creating a channel](pf_code42_integration_creating_a_channel.html). Click **Done**.

   10. On the **Outbound Provisioning** tab, click **Next**.

4. On the **Activation and Summary** tab, above the **Summary** section, click the toggle to turn on the connection. Click **Save**.

---

---
title: Creating a single sign-on connection
description: To allow PingFederate to handle single sign-on (SSO) to Code42, create a service provider (SP) connection.
component: code42-pingfederate
page_id: code42-pingfederate:single_sign-on_setup:pf_code42_integration_creating_a_single_sign_on_connection
canonical_url: https://docs.pingidentity.com/integrations/code42-pingfederate/single_sign-on_setup/pf_code42_integration_creating_a_single_sign_on_connection.html
revdate: June 26, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
  choose-from: Choose from:
---

# Creating a single sign-on connection

To allow PingFederate to handle single sign-on (SSO) to Code42, create a service provider (SP) connection.

## About this task

|   |                                                                                                           |
| - | --------------------------------------------------------------------------------------------------------- |
|   | You can follow these steps to create a new SP connection, or you can modify your provisioning connection. |

## Steps

1. In the PingFederate administrator console, create a new SP connection:

   ### Choose from:

   * For PingFederate 10.1 or later: go to **Applications > Integration > SP Connections**. Click **Create Connection**.

   * For PingFederate 10.0 or earlier: go to **Identity Provider > SP Connections**. Click **Create Connection**.

2. On the **Connection Template** tab, select **Do not use a template for this connection**. Click **Next**.

3. On the **Connection Type** tab, select **Browser SSO Profiles** and clear any unwanted types. Click **Next**.

4. On the **Connection Options** tab, select only **Browser SSO**. Click **Next**.

5. On the **Import Metadata** tab, select **URL**, and then configure the Code42 metadata information.

   1. Click **Manage Partner Metadata URLs**.

   2. On the **SP Connection > Partner Metadata URLs** tab, click **Add New URL**.

   3. On the **SP Connection > Partner Metadata URLs > Metadata URL** tab, in the **Name** field, enter a name, such as `Code42`.

   4. In the URL field, paste the **Code42 Service Provider Metadata URL** that you noted in [Adding PingFederate as an authentication provider in Code42](pf_code42_integration_adding_pf_as_an_authentication_provider_in_code42.html). Clear the **Validate Metadata Signature** check box. Click **Next**.

   5. On the **Summary** tab, click **Done**.

   6. On the **SP Connection > Partner Metadata URLs** tab, click **Save**.

   7. On the **SP Connection > Import Metadata** tab, from the **Metadata URL** list, select the Code42 URL. Click **Load Metadata**. Click **Next**.

6. On the **General Info** tab, the basic connection information is populated by the metadata XML file. Click **Next**.

7. On the **Browser SSO** tab, configure browser SSO. Click **Next**.

   You can find a complete guide in [Configure IdP Browser SSO](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_spconnectionconfigtasklet_spbrowserssostate.html) in the PingFederate documentation.

   1. On the **Browser SSO > SAML Profiles** tab, select only **SP-Initiated SSO**.

   2. On the **Browser SSO > Protocol Settings > Allowable SAML Bindings** tab, select only **POST**.

   3. On the **Browser SSO > Protocol Settings > Signature Policy** tab, select **Always sign assertion**.

8. On the **Credentials** tab, configure the connection credentials.

   You can find a complete guide in [Configuring credentials](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_spconnectionconfigtasklet_credentialsstate.html) in the PingFederate documentation.

9. On the **Activation and Summary** tab, above the **Summary** section, turn on the connection. Click **Save**.

---

---
title: Deploying the integration files
description: To get started with the integration, deploy the SCIM Connector files to your PingFederate directory.
component: code42-pingfederate
page_id: code42-pingfederate::pf_code42_integration_deploying_the_integration_files
canonical_url: https://docs.pingidentity.com/integrations/code42-pingfederate/pf_code42_integration_deploying_the_integration_files.html
revdate: June 26, 2024
section_ids:
  steps: Steps
---

# Deploying the integration files

To get started with the integration, deploy the SCIM Connector files to your PingFederate directory.

## Steps

1. Download the SCIM Connector `.zip` archive from the [**Add-ons** tab of the PingFederate downloads page](https://www.pingidentity.com/en/resources/downloads/pingfederate.html) or the [Ping Identity Marketplace](https://marketplace.pingone.com/item/code42-sso-integration-provisioning).

2. Stop PingFederate.

3. If you're upgrading an existing deployment, delete the `pf-scim-quickconnection-<version>.jar` file from your `<pf_install>/pingfederate/server/default/deploy` directory.

4. Extract the `.zip` archive and merge the contents of the `dist` directory with your `<pf_install>/pingfederate/server/default/deploy` directory.

5. Enable the PingFederate provisioning engine:

   1. Open your `<pf_install>/pingfederate/bin/run.properties` file.Change `pf.provisioner.mode` to `STANDALONE`.

   2. Save the file.

      |   |                                                                                                                                                                                                                                        |
      | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      |   | To configure the `FAILOVER` mode instead, see [Deploying provisioning failover](https://docs.pingidentity.com/pingfederate/latest/server_clustering_guide/pf_deploy_provis_failover.html) in the PingFederate Server Clustering Guide. |

6. Start PingFederate.

7. If you operate PingFederate in a cluster, repeat steps 2-4 and step 6 for each engine node.

---

---
title: Enabling provisioning and single sign-on in PingFederate
description: To use PingFederate for provisioning and single sign-on, configure an external datastore and set a SAML entity ID.
component: code42-pingfederate
page_id: code42-pingfederate:enabling_provisioning_and_single_sign-on_in_pingfederate:pf_code42_integration_enabling_provisioning_and_single_sign_on_in_pf
canonical_url: https://docs.pingidentity.com/integrations/code42-pingfederate/enabling_provisioning_and_single_sign-on_in_pingfederate/pf_code42_integration_enabling_provisioning_and_single_sign_on_in_pf.html
revdate: June 26, 2024
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
component: code42-pingfederate
page_id: code42-pingfederate:enabling_provisioning_and_single_sign-on_in_pingfederate:pf_code42_integration_enabling_provisioning_and_single_sign_on_in_pf_100_or_earlier
canonical_url: https://docs.pingidentity.com/integrations/code42-pingfederate/enabling_provisioning_and_single_sign-on_in_pingfederate/pf_code42_integration_enabling_provisioning_and_single_sign_on_in_pf_100_or_earlier.html
revdate: June 27, 2024
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
component: code42-pingfederate
page_id: code42-pingfederate:enabling_provisioning_and_single_sign-on_in_pingfederate:pf_code42_integration_enabling_provisioning_and_single_sign_on_in_pf_101_or_later
canonical_url: https://docs.pingidentity.com/integrations/code42-pingfederate/enabling_provisioning_and_single_sign-on_in_pingfederate/pf_code42_integration_enabling_provisioning_and_single_sign_on_in_pf_101_or_later.html
revdate: June 27, 2024
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
title: Exporting SAML metadata from PingFederate
description: Export a metadata file that describes your PingFederate identity provider configuration.
component: code42-pingfederate
page_id: code42-pingfederate:single_sign-on_setup:pf_code42_integration_exporting_saml_metadata_from_pf
canonical_url: https://docs.pingidentity.com/integrations/code42-pingfederate/single_sign-on_setup/pf_code42_integration_exporting_saml_metadata_from_pf.html
revdate: June 26, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
  choose-from: Choose from:
---

# Exporting SAML metadata from PingFederate

Export a metadata file that describes your PingFederate identity provider configuration.

## About this task

You can find general information about these steps in [Metadata export](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_metadata_export.html) in the PingFederate documentation.

## Steps

1. In the PingFederate administrative console, go to the **Metadata Export** window.

   ### Choose from:

   * For PingFederate 10.1 or later: go to **System > Protocol Metadata > Metadata Export**.

   * For PingFederate 10.0 or earlier: go to **System > Metadata Export**.

2. If you see the **Metadata Role** tab, select **I am the identity provider (IdP)**. Click **Next**.

3. On the **Metadata Mode** tab, select **Select information to include in metadata manually**. Click **Next**.

4. On the **Protocol** tab, click **Next**.

5. On the **Attribute Contract** tab, click **Next**.

6. On the **Signing Key** tab, select a signing certificate. Click **Next**.

7. (Optional) On the **Metadata Signing** tab, select a certificate to sign the metadata XML file. Click **Next**.

8. On the **XML Encryption Certificate** tab, select the certificate that you want to use to encrypt the XML content. Click **Next**.

9. On the **Export & Summary** tab, click **Export**.

10. Save `metadata.xml`.

11. Click **Done**.

---

---
title: SCIM Connector settings reference for Code42
description: Lists the configuration settings for the SCIM Connector when integrating with Code42.
component: code42-pingfederate
page_id: code42-pingfederate:provisioning_setup:pf_code42_integration_scim_connector_settings_reference_for_code42
canonical_url: https://docs.pingidentity.com/integrations/code42-pingfederate/provisioning_setup/pf_code42_integration_scim_connector_settings_reference_for_code42.html
revdate: June 26, 2024
---

# SCIM Connector settings reference for Code42

Lists the configuration settings for the SCIM Connector when integrating with Code42.

| Field Name                                                                                                                                                                 | Description                                                                                                                                                                                                                                                                                              |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **SCIM URL**                                                                                                                                                               | The Code42 base URL that you noted in [Adding PingFederate as SCIM provider in Code42](pf_code42_integration_adding_pf_as_scim_provider_in_code42.html).                                                                                                                                                 |
| **SCIM Version**                                                                                                                                                           | Select **2.0**.                                                                                                                                                                                                                                                                                          |
| **Authentication Methods**                                                                                                                                                 | Select **OAuth 2 Bearer Token**.                                                                                                                                                                                                                                                                         |
| **OAuth 2 Bearer Token**                                                                                                                                                   |                                                                                                                                                                                                                                                                                                          |
| **Access Token**                                                                                                                                                           | The OAuth access token that you noted in [Adding PingFederate as SCIM provider in Code42](pf_code42_integration_adding_pf_as_scim_provider_in_code42.html).                                                                                                                                              |
| **SCIM Overrides**                                                                                                                                                         |                                                                                                                                                                                                                                                                                                          |
| **Unique User Identifier**                                                                                                                                                 | The attribute that uniquely identifies a user when PingFederate does not have access to the unique user ID that the target application assigns to a user.Select **userName**.                                                                                                                            |
| **Provisioning Options**                                                                                                                                                   |                                                                                                                                                                                                                                                                                                          |
| **User Create**                                                                                                                                                            | **Selected** (default) – PingFederate creates users in the target service.**Cleared** – PingFederate does not create users in the target service.                                                                                                                                                        |
| **User Update**                                                                                                                                                            | **Selected** (default) – PingFederate updates existing users in the target service. PingFederate can also re-enable disabled users.**Cleared** – PingFederate does not update existing users in the target service.                                                                                      |
| **User Disable / Delete**                                                                                                                                                  | **Selected** (default) – If **User Update** is also enabled, PingFederate removes users in the target service according to the **Remove User Action** setting in the connection configuration.**Cleared** – PingFederate does not remove users in the target service.                                    |
| **Provision Disabled Users**                                                                                                                                               | Code42 does not support provisioning disabled users. If a disabled user is targeted in your data store, PingFederate creates an active user in Code42.                                                                                                                                                   |
| &#xA;&#xA;If any of the above provisioning options are cleared, PingFederate logs a warning in the user workflow section of provisioner.log when the related action fails. |                                                                                                                                                                                                                                                                                                          |
| **Remove User Action**                                                                                                                                                     | This option applies when:- **User Disable / Delete** is selected, and

- a previously-provisioned user no longer meets the condition set on the **Source Location** screen, or

- a user has been disabled or deleted from the data store.Select **Disable**. Code42 does not support the delete option. |

---

---
title: Supported attributes reference
description: Lists the attributes that can be mapped for user provisioning to Code42.
component: code42-pingfederate
page_id: code42-pingfederate:provisioning_setup:pf_code42_integration_supported_attributes_reference
canonical_url: https://docs.pingidentity.com/integrations/code42-pingfederate/provisioning_setup/pf_code42_integration_supported_attributes_reference.html
revdate: June 26, 2024
---

# Supported attributes reference

Lists the attributes that can be mapped for user provisioning to Code42.

For more information on SCIM attributes see the [SCIM specification](https://datatracker.ietf.org/doc/html/rfc7643) and the SCIM enabled service provider documentation.

| Attribute      | Description                                                                                                                                                                                                                                                                       |
| -------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| userName       | A service provider's unique identifier for the user. This attribute is required.                                                                                                                                                                                                  |
| givenName      | The given name of the user, or first name in most Western languages (for example, 'Barbara' given the full name 'Ms. Barbara Jane Jensen, III').                                                                                                                                  |
| familyName     | The family name of the user, or last name in most Western languages (for example, 'Jensen' given the full name 'Ms. Barbara Jane Jensen, III').                                                                                                                                   |
| workEmail      | Work email for the user (for example, "bjensen\@example.com").                                                                                                                                                                                                                    |
| title          | The user's title, such as "Vice President".                                                                                                                                                                                                                                       |
| externalId     | A string that is an identifier for the resource as defined by the provisioning client.                                                                                                                                                                                            |
| workCity       | The work city or locality component for the user's mailing address.                                                                                                                                                                                                               |
| workState      | The work state or region component for the user's mailing address.                                                                                                                                                                                                                |
| workCountry    | The work country component for the user's mailing address. When specified, the value MUST be in ISO 3166-1 "alpha-2" code format [ISO3166](https://datatracker.ietf.org/doc/html/rfc7643#ref-ISO3166); for example, the United States and Sweden are "US" and "SE", respectively. |
| workStreet     | The work street address for the user, which can include the street number, street name, P.O. box, and multi-line extended street address information.                                                                                                                             |
| workPostalCode | The work ZIP or postal code component for the user's mailing address.                                                                                                                                                                                                             |
| division       | The division for the user.                                                                                                                                                                                                                                                        |
| department     | The department for the user.                                                                                                                                                                                                                                                      |
| manager        | The user ID for the user's manager in Code42.                                                                                                                                                                                                                                     |

---

---
title: Updating an existing deployment
description: If you're upgrading from a previous version of the SCIM Connector, note your existing service provider (SP) connection configuration and create a new connection.
component: code42-pingfederate
page_id: code42-pingfederate:updating_an_existing_deployment:pf_code42_integration_upgrading_an_existing_deployment
canonical_url: https://docs.pingidentity.com/integrations/code42-pingfederate/updating_an_existing_deployment/pf_code42_integration_upgrading_an_existing_deployment.html
revdate: June 26, 2024
section_ids:
  updating-an-existing-deployment-in-pingfederate-10-1-or-later: Updating an existing deployment in PingFederate 10.1 or later
  steps: Steps
  updating-an-existing-deployment-in-pingfederate-10-0-or-earlier: Updating an existing deployment in PingFederate 10.0 or earlier
  steps-2: Steps
---

# Updating an existing deployment

If you're upgrading from a previous version of the SCIM Connector, note your existing service provider (SP) connection configuration and create a new connection.

## Updating an existing deployment in PingFederate 10.1 or later

### Steps

1. Back up your current PingFederate configuration as shown in [Configuration archive](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_configurationarchivetasklet_selectimportexportstate.html) in the PingFederate documentation.

2. In the PingFederate administrative console, go to **Applications > Integration > SP Connections** and select your connection.

3. Note the attribute mappings for your existing SP connection.

   For help, see [Mapping attributes](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_saaschanneltasklet_saasattrmappingmgmtstate.html) in the PingFederate documentation.

4. Delete your existing SP connection.

   1. Go to **Applications > Integration > SP Connections**.

   2. For your existing connection, click **Select action**, and then click **Delete**. Click **Confirm.**

5. Complete the steps in [Deploying the integration files](../pf_code42_integration_deploying_the_integration_files.html).

6. Complete the steps in [Creating a provisioning connection](../provisioning_setup/pf_code42_integration_creating_a_provisioning_connection.html).

   * From **Outbound Provisioning > Manage Channels > Channel**, on the **Attribute Mapping** tab, configure the attribute mappings based on your notes.

7. Complete the steps in [Creating a single sign-on connection](../single_sign-on_setup/pf_code42_integration_creating_a_single_sign_on_connection.html).

## Updating an existing deployment in PingFederate 10.0 or earlier

### Steps

1. Back up your current PingFederate configuration as shown in [Configuration archive](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_configurationarchivetasklet_selectimportexportstate.html) in the PingFederate documentation.

2. In the PingFederate administrative console, go to **Identity Provider > SP Connections** and select your connection.

3. Note the attribute mappings for your existing SP connection.

   For help, see [Mapping attributes](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_saaschanneltasklet_saasattrmappingmgmtstate.html) in the PingFederate documentation.

4. Delete your existing SP connection.

   1. Go to **Identity Provider > SP Connections > Manage All**.

   2. For your existing connection, click **Select action**, and then click **Delete**. Click **Save.**

5. Complete the steps in [Deploying the integration files](../pf_code42_integration_deploying_the_integration_files.html).

6. Complete the steps in [Creating a provisioning connection](../provisioning_setup/pf_code42_integration_creating_a_provisioning_connection.html).

   * From **Outbound Provisioning > Manage Channels > Channel**, on the **Attribute Mapping** tab, configure the attribute mappings based on your notes.

7. Complete the steps in [Creating a single sign-on connection](../single_sign-on_setup/pf_code42_integration_creating_a_single_sign_on_connection.html).