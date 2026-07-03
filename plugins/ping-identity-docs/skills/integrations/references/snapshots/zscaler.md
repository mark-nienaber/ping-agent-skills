---
title: Changelog
description: The following is the change history for the Zscaler Internet Access Provisioner.
component: zscaler
page_id: zscaler:zscaler_internet_access_provisioner:pf_zscaler_zia_connector_changelog
canonical_url: https://docs.pingidentity.com/integrations/zscaler/zscaler_internet_access_provisioner/pf_zscaler_zia_connector_changelog.html
revdate: June 18, 2024
section_ids:
  zscaler-internet-access-provisioner-1-1-1-october-2023: Zscaler Internet Access Provisioner 1.1.1 – October 2023
  zscaler-internet-access-provisioner-1-1-february-2020: Zscaler Internet Access Provisioner 1.1 – February 2020
  zscaler-internet-access-provisioner-1-0-2-august-2019: Zscaler Internet Access Provisioner 1.0.2 – August 2019
  zscaler-internet-access-provisioner-1-0-1-july-2018: Zscaler Internet Access Provisioner 1.0.1 – July 2018
  zscaler-internet-access-provisioner-1-0-june-2018: Zscaler Internet Access Provisioner 1.0 – June 2018
---

# Changelog

The following is the change history for the Zscaler Internet Access Provisioner.

## Zscaler Internet Access Provisioner 1.1.1 – October 2023

* Fixed an issue that caused null values or missing members in `PATCH` operations for group updates.

* Improved efficiency of `PATCH` operations for group updates.

* Improved volume of log entries for group create and update operations to reduce log density.

## Zscaler Internet Access Provisioner 1.1 – February 2020

* Renamed the integration to "Zscaler Internet Access Provisioner" to match official branding.

* Added the ability to update the `username` attribute in Zscaler Internet Access.

* Improved error handling and reporting when encountering a user that does not have an ID.

* Improved provisioner efficiency by adding support for Patch operations for group updates.

* Fixed an issue that prevented synchronization of groups with certain special characters in the name.

* Fixed an issue that caused groups to be serialized incorrectly.

## Zscaler Internet Access Provisioner 1.0.2 – August 2019

* Fixed an issue that prevented synchronization of groups with certain special characters in the name.

## Zscaler Internet Access Provisioner 1.0.1 – July 2018

* Fixed compatibility issue when other System for Cross-domain Identity Management (SCIM)-based connectors exist along side Zscaler provisioning connections

## Zscaler Internet Access Provisioner 1.0 – June 2018

* Initial release.

* Added support for user and group life cycle management (including creates, updates, and deletes).

* Added support for adding users to groups.

* Added configuration options for workflow capabilities (for example, the ability to disable updates).

---

---
title: Changelog
description: Lists the changes made in each version of the Zscaler Private Access Connector.
component: zscaler
page_id: zscaler:zscaler_private_access_provisioner:pf_zscaler_zpa_connector_changelog
canonical_url: https://docs.pingidentity.com/integrations/zscaler/zscaler_private_access_provisioner/pf_zscaler_zpa_connector_changelog.html
revdate: June 18, 2024
section_ids:
  zscaler-private-access-provisioner-1-0-1-october-2023: Zscaler Private Access Provisioner 1.0.1 – October 2023
  zscaler-private-access-provisioner-1-0-april-2020: Zscaler Private Access Provisioner 1.0 – April 2020
---

# Changelog

Lists the changes made in each version of the Zscaler Private Access Connector.

## Zscaler Private Access Provisioner 1.0.1 – October 2023

* Fixed an issue that caused null values or missing members in `PATCH` operations for group updates.

* Improved efficiency of `PATCH` operations for group updates.

* Improved volume of log entries for group create and update operations to reduce log density.

## Zscaler Private Access Provisioner 1.0 – April 2020

* Initial release.

* Added support for user and group provisioning.

* Added support for ZPA SCIM attributes.

* Added configuration options for create, update, and disable/delete capabilities.

* Added configuration options for deprovisioning actions

---

---
title: Configuring provisioning
description: To enable user provisioning, configure System for Cross-domain Identity Management (SCIM) in Zscaler Internet Access, and then create a connection in PingFederate.
component: zscaler
page_id: zscaler:zscaler_internet_access_provisioner:pf_zscaler_zia_connector_configuring_provisioning
canonical_url: https://docs.pingidentity.com/integrations/zscaler/zscaler_internet_access_provisioner/pf_zscaler_zia_connector_configuring_provisioning.html
revdate: June 18, 2024
section_ids:
  steps: Steps
---

# Configuring provisioning

To enable user provisioning, configure System for Cross-domain Identity Management (SCIM) in Zscaler Internet Access, and then create a connection in PingFederate.

## Steps

1. Complete the steps in [Getting a base URL and bearer token from Zscaler](pf_zscaler_zia_connector_getting_a_base_url_and_bearer_token_from_zscaler.html).

2. Complete the steps in [Creating a provisioning connection](pf_zscaler_zia_connector_creating_a_provisioning_connection.html).

---

---
title: Configuring single sign-on
description: To allow PingFederate to act as an identity provider (IdP) for Zscaler Internet Access, configure single sign-on (SSO), exchange signing certificates, and create a connection.
component: zscaler
page_id: zscaler:zscaler_internet_access_provisioner:pf_zscaler_zia_connector_configuring_single_sign_on
canonical_url: https://docs.pingidentity.com/integrations/zscaler/zscaler_internet_access_provisioner/pf_zscaler_zia_connector_configuring_single_sign_on.html
revdate: June 18, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Configuring single sign-on

To allow PingFederate to act as an identity provider (IdP) for Zscaler Internet Access, configure single sign-on (SSO), exchange signing certificates, and create a connection.

## About this task

|   |                                                                                                    |
| - | -------------------------------------------------------------------------------------------------- |
|   | SSO is an optional part of this integration. If you only want user provisioning, skip these steps. |

## Steps

1. Complete the steps in [Creating a single sign-on connection](pf_zscaler_zia_connector_creating_a_single_sign_on_connection.html).

2. Ensure that your traffic is being forwarded to Zscaler Internet Access.

   Learn more in [Choosing Traffic Forwarding Methods](https://help.zscaler.com/zia/choosing-traffic-forwarding-methods) in the Zscaler Internet Access documentation.

3. Complete the steps in [Registering PingFederate as an identity provider in Zscaler](pf_zscaler_zia_connector_registering_pf_as_an_identity_provider_in_zscaler.html).

---

---
title: Creating a provisioning connection
description: To allow PingFederate to manage users in Zscaler Internet Access, create a service provider (SP) connection.
component: zscaler
page_id: zscaler:zscaler_internet_access_provisioner:pf_zscaler_zia_connector_creating_a_provisioning_connection
canonical_url: https://docs.pingidentity.com/integrations/zscaler/zscaler_internet_access_provisioner/pf_zscaler_zia_connector_creating_a_provisioning_connection.html
revdate: June 18, 2024
section_ids:
  steps: Steps
---

# Creating a provisioning connection

To allow PingFederate to manage users in Zscaler Internet Access, create a service provider (SP) connection.

## Steps

1. In the PingFederate administrator console, create a new SP connection:

   * For PingFederate 10.1 or later: go to **Applications > Integration > SP Connections**. Click **Create Connection**.

   * For PingFederate 10.0 or earlier: go to **Identity Provider > SP Connections**. Click **Create Connection**.

2. Configure the basic connection details with the Zscaler Internet Access quick connection template:

   1. On the **Connection Template** tab, select **Use a template for this connection**.

   2. In the **Connection Template** list, select **Zscaler ZIA Provisioner**.

   3. In the **Metadata File** row, upload the `zscaler-metadata.xml` file that you saved in [Getting SAML details from Zscaler](pf_zscaler_zia_connector_getting_saml_details_from_zscaler.html). Click **Next**.

   4. On the **Connection Type** tab, select only **Outbound Provisioning**. Click **Next**.

   5. On the **General Info** tab, in the **Connection Name** field, enter a name for the connection. Click **Next**.

3. On the **Outbound Provisioning** tab, configure provisioning, as shown in [Configuring outbound provisioning](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_spconnectionconfigtasklet_saasprovisioningstate.html) in the PingFederate documentation, with the following details:

   1. On the **Target** page, enter the **Base URL** and **Bearer Token** values that you noted in [Getting a base URL and bearer token from Zscaler](pf_zscaler_zia_connector_getting_a_base_url_and_bearer_token_from_zscaler.html).

      |   |                                                                                         |
      | - | --------------------------------------------------------------------------------------- |
      |   | PingFederate verifies the access token when you activate the channel and SP connection. |

   2. **Optional:** In the **Provisioning Options** section, customize the provisioning connector actions as shown in [Provisioning options reference](pf_zscaler_zia_connector_provisioning_options_reference.html). Click **Next**.

   3. On the **Manage Channels** page, create a channel as shown in [Managing channels](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_saasmanagementtasklet_saasmanagementstate.html) in the PingFederate documentation. Click **Done**.

      |   |                                                                                                                                                                             |
      | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      |   | Learn more about the attributes available for your channel configuration in [Supported attributes reference](pf_zscaler_zia_connector_supported_attributes_reference.html). |

   4. On the **Outbound Provisioning** tab, click **Next**.

4. On the **Activation and Summary** tab, above the **Summary** section, click the toggle to turn on the connection. Click **Save**.

---

---
title: Creating a provisioning connection
description: To allow PingFederate to manage users in Zscaler Private Access, create a service provider (SP) connection.
component: zscaler
page_id: zscaler:zscaler_private_access_provisioner:pf_zscaler_zpa_connector_creating_a_provisioning_connection
canonical_url: https://docs.pingidentity.com/integrations/zscaler/zscaler_private_access_provisioner/pf_zscaler_zpa_connector_creating_a_provisioning_connection.html
revdate: June 18, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Creating a provisioning connection

To allow PingFederate to manage users in Zscaler Private Access, create a service provider (SP) connection.

## About this task

|   |                                                                                                           |
| - | --------------------------------------------------------------------------------------------------------- |
|   | You can follow these steps to create a new SP connection, or you can modify your provisioning connection. |

## Steps

1. In the PingFederate administrator console, configure the data store that PingFederate will use as the source of user data. For instructions, see [Datastores](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_managedatasourcestasklet_managedatasourcesstate.html) in the PingFederate documentation.

   * When targeting users and groups for provisioning, exclude the user account that you will use to administer users in your connection to Zscaler Private Access. This prevents the PingFederate provisioning engine from interfering with the account that provisions users and groups.

2. Enable provisioning.

   1. On the **System > Protocol Settings > Roles & Protocols** screen, select **Enable Identity Provider IdP Role and Support the Following**.

   2. Select **Outbound Provisioning**. Click **Save**.

3. On the **Identity Provider** screen, in the **SP Connections** area, open an existing connection or create a new one as follows:

   1. Click **Create new**.

   2. On the **Connection Template** screen, select **Use a template for this connection**.

   3. In the **Connection Template** list, select **Zscaler ZPA Connector**.

   4. Click **Choose File**, select the `sp_metadata.xml` file that you downloaded in [Enabling provisioning and single sign-on in Zscaler](pf_zscaler_zpa_connector_enabling_provisioning_and_single_sign_on_in_zscaler.html), and then click **Open**. Click **Next**.

4. On the **Connection Type** screen, select **Outbound Provisioning** and clear any unwanted types. Click **Next**.

5. On the **General Info** screen, the basic connection information is populated by the metadata XML file. Click **Next**.

6. On the **Outbound Provisioning** screen, configure the provisioning target and channel as shown in [Configuring outbound provisioning](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_spconnectionconfigtasklet_saasprovisioningstate.html) in the PingFederate documentation.

   1. Click **Configure Provisioning**.

   2. On the **Target** screen, in the **Base URL** field, enter the **SCIM Service Provider Endpoint** that you noted in [Enabling provisioning and single sign-on in Zscaler](pf_zscaler_zpa_connector_enabling_provisioning_and_single_sign_on_in_zscaler.html).

   3. On the **Target** screen, enter the **Bearer Token** that you noted in [Enabling provisioning and single sign-on in Zscaler](pf_zscaler_zpa_connector_enabling_provisioning_and_single_sign_on_in_zscaler.html).

      |   |                                                                                         |
      | - | --------------------------------------------------------------------------------------- |
      |   | PingFederate verifies the access token when you activate the channel and SP connection. |

   4. Under **Provisioning Options**, customize the provisioning connector actions as shown in [Provisioning options reference](pf_zscaler_zpa_connector_provisioning_options_reference.html). Click **Next**.

   5. On the **Manage Channels** screen, create a channel as shown in [Managing channels](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_saasmanagementtasklet_saasmanagementstate.html) in the PingFederate documentation. Click **Done**.

      |   |                                                                                                                                                                                        |
      | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      |   | For more information about the attributes available in your channel configuration, see [Supported attributes reference](pf_zscaler_zpa_connector_supported_attributes_reference.html). |

   6. On the **Outbound Provisioning** screen, click **Next**.

7. On the **Activation and Summary** screen, above the **Summary** section, turn on the connection. Click **Save**.

---

---
title: Creating a single sign-on connection
description: To allow PingFederate to handle single sign-on (SSO) to Zscaler Internet Access, create a service provider (SP) connection.
component: zscaler
page_id: zscaler:zscaler_internet_access_provisioner:pf_zscaler_zia_connector_creating_a_single_sign_on_connection
canonical_url: https://docs.pingidentity.com/integrations/zscaler/zscaler_internet_access_provisioner/pf_zscaler_zia_connector_creating_a_single_sign_on_connection.html
revdate: June 18, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Creating a single sign-on connection

To allow PingFederate to handle single sign-on (SSO) to Zscaler Internet Access, create a service provider (SP) connection.

## About this task

|   |                                                                                                        |
| - | ------------------------------------------------------------------------------------------------------ |
|   | You can follow these steps to create a new connection, or you can modify your provisioning connection. |

## Steps

1. In the PingFederate administrator console, create a new SP connection:

   * For PingFederate 10.1 or later: go to **Applications > Integration > SP Connections**. Click **Create Connection**.

   * For PingFederate 10.0 or earlier: go to **Identity Provider > SP Connections**. Click **Create Connection**.

2. Configure the basic connection details with the Zscaler Internet Access quick connection template:

   1. On the **Connection Template** tab, select **Use a template for this connection**.

   2. In the **Connection Template** list, select **Zscaler ZIA Provisioner**.

   3. In the **Metadata File** row, upload the `zscaler-metadata.xml` file that you saved in [Getting SAML details from Zscaler](pf_zscaler_zia_connector_getting_saml_details_from_zscaler.html). Click **Next**.

   4. On the **Connection Type** tab, select **Browser SSO Profiles**. Click **Next**.

   5. On the **General Info** tab, in the **Connection Name** field, enter a name for the connection. Click **Next**.

3. On the **Browser SSO** tab, configure SSO as shown in [Configuring IdP Browser SSO](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_spconnectionconfigtasklet_spbrowserssostate.html) in the PingFederate documentation, with the following details:

   1. On the **Browser SSO > SAML Profiles** tab, select only **IdP-Initiated SSO** and **SP-Initiated SSO**.

      |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
      | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      |   | It is recommended to leverage SP-initiated SSO because IdP-initiated SSO is not commonly used.Learn more in [IdP-Initiated SAML](https://help.zscaler.com/zia/about-saml) in the Zscaler Internet Access documentation and [Setting Assertion Consumer Service URLs (SAML)](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_spprotocolsettingstasklet_assertionconsumerservicestate.html) in the PingFederate documentation.If you want to use both IdP-initiated SSO and SP-initiated SSO, both endpoints are accessible using the `ACSIdx` parameter.Learn more in [IdP endpoints](https://docs.pingidentity.com/pingfederate/latest/developers_reference_guide/pf_idp_endpoints.html) in the PingFederate documentation. |

   2. On the **Browser SSO > Protocol Settings > Allowable SAML Bindings** tab, select only **POST**.

   3. On the **Browser SSO > Protocol Settings > Signature Policy** tab, select **Always sign assertion**.

4. On the **Credentials** tab, configure the connection credentials as shown in [Configuring credentials](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_spconnectionconfigtasklet_credentialsstate.html) in the PingFederate documentation. Click **Next**.

5. On the **Activation and Summary** tab, above the **Summary** section, click the toggle to turn on the connection. Click **Save**.

---

---
title: Creating a single sign-on connection
description: To allow PingFederate to handle single sign-on (SSO) to Zscaler Private Access, create a service provider (SP) connection.
component: zscaler
page_id: zscaler:zscaler_private_access_provisioner:pf_zscaler_zpa_connector_creating_a_single_sign_on_connection
canonical_url: https://docs.pingidentity.com/integrations/zscaler/zscaler_private_access_provisioner/pf_zscaler_zpa_connector_creating_a_single_sign_on_connection.html
revdate: June 18, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Creating a single sign-on connection

To allow PingFederate to handle single sign-on (SSO) to Zscaler Private Access, create a service provider (SP) connection.

## About this task

|   |                                                                                                           |
| - | --------------------------------------------------------------------------------------------------------- |
|   | You can follow these steps to create a new SP connection, or you can modify your provisioning connection. |

## Steps

1. In the PingFederate administrator console, configure the data store that PingFederate will use as the source of user data. For instructions, see [Datastores](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_managedatasourcestasklet_managedatasourcesstate.html) in the PingFederate documentation.

2. On the **Identity Provider** tab, in the **SP Connections** area, open an existing connection or create a new one as follows:

   1. Click **Create new**.

   2. On the **Connection Template** tab, select **Use a template for this connection**.

   3. In the **Connection Template** list, select **Zscaler ZPA Connector**.

   4. Click **Choose File**, select the `sp_metadata.xml` file that you downloaded in [Enabling provisioning and single sign-on in Zscaler](pf_zscaler_zpa_connector_enabling_provisioning_and_single_sign_on_in_zscaler.html), and then click **Open**. Click **Next**.

3. On the **Connection Type** tab, select **Browser SSO Profiles** and clear any unwanted types. Click **Next**.

4. On the **General Info** tab, the basic connection information is populated by the metadata XML file. Click **Next**.

5. On the **Browser SSO** tab, configure browser SSO.

   For a complete guide, see [Configuring IdP Browser SSO](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_spconnectionconfigtasklet_spbrowserssostate.html) in the PingFederate documentation.

   1. On the **Browser SSO > SAML Profiles** tab, select only **IdP-Initiated SSO** and **SP-Initiated SSO**.

   2. On the **Browser SSO > Protocol Settings > Allowable SAML Bindings** tab, select only **POST**.

   3. On the **Browser SSO > Protocol Settings > Signature Policy** tab, select **Always sign assertion**.

6. On the **Credentials** tab, configure the connection credentials. Click **Next**.

   For a complete guide, see [Configuring credentials](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_spconnectionconfigtasklet_credentialsstate.html) in the PingFederate documentation.

   * On the **Credentials > Signature Verification Settings > Signature Verification Certificate** tab, click **Manage Certificates** and import the certificate that you downloaded in [Enabling provisioning and single sign-on in Zscaler](pf_zscaler_zpa_connector_enabling_provisioning_and_single_sign_on_in_zscaler.html).

7. On the **Activation and Summary** tab, above the **Summary** section, turn on the connection. Click **Save**.

---

---
title: Deploying the integration files
description: To get started with the integration, deploy the Zscaler Internet Access Provisioner files to your PingFederate directory.
component: zscaler
page_id: zscaler:zscaler_internet_access_provisioner:pf_zscaler_zia_connector_deploying_the_integration_files
canonical_url: https://docs.pingidentity.com/integrations/zscaler/zscaler_internet_access_provisioner/pf_zscaler_zia_connector_deploying_the_integration_files.html
revdate: June 18, 2024
section_ids:
  steps: Steps
---

# Deploying the integration files

To get started with the integration, deploy the Zscaler Internet Access Provisioner files to your PingFederate directory.

## Steps

1. Download the Zscaler Internet Access Provisioner `.zip` archive from the [**Add-ons** tab of the PingFederate downloads page](https://www.pingidentity.com/en/resources/downloads/pingfederate.html) or the [Ping Identity Marketplace](https://marketplace.pingone.com/item/zscaler-internet-access-zia-sso-provisioner).

2. Stop PingFederate.

3. If you're upgrading an existing deployment, delete the `pf-zscaler-zia-quickconnection-<version>.jar` file from your `<pf_install>/pingfederate/server/default/deploy` directory.

4. Extract the `.zip` archive and merge the contents of the `dist` directory with your `<pf_install>/pingfederate/server/default/deploy` directory.

5. Enable the PingFederate provisioning engine:

   1. Open your `<pf_install>/pingfederate/bin/run.properties` file.

   2. Change `pf.provisioner.mode` to `STANDALONE`.

   3. Save the file.

   |   |                                                                                                                                                                                                                                        |
   | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | To configure the `FAILOVER` mode instead, see [Deploying provisioning failover](https://docs.pingidentity.com/pingfederate/latest/server_clustering_guide/pf_deploy_provis_failover.html) in the PingFederate Server Clustering Guide. |

6. Start PingFederate.

7. If you operate PingFederate in a cluster, repeat steps 2-4 and step 6 for each engine node.

---

---
title: Deploying the integration files
description: To get started with the integration, deploy the Zscaler Private Access Provisioner files to your PingFederate directory.
component: zscaler
page_id: zscaler:zscaler_private_access_provisioner:pf_zscaler_zpa_connector_deploying_the_integration_files
canonical_url: https://docs.pingidentity.com/integrations/zscaler/zscaler_private_access_provisioner/pf_zscaler_zpa_connector_deploying_the_integration_files.html
revdate: June 18, 2024
section_ids:
  steps: Steps
---

# Deploying the integration files

To get started with the integration, deploy the Zscaler Private Access Provisioner files to your PingFederate directory.

## Steps

1. Download the Zscaler Private Access Provisioner `.zip` archive from the [**Add-ons** tab of the PingFederate downloads page](https://www.pingidentity.com/en/resources/downloads/pingfederate.html) or the [Ping Identity Marketplace](https://marketplace.pingone.com/item/zscaler-private-access-zpa-scim-provisioning-integration).

2. Stop PingFederate.

3. If you're upgrading an existing deployment, delete the `pf-zscaler-zpa-quickconnection-<version>.jar` file from your `<pf_install>/pingfederate/server/default/deploy` directory.

4. Extract the `.zip` archive and merge the contents of the `dist` directory with your `<pf_install>/pingfederate/server/default/deploy` directory.

5. Enable the PingFederate provisioning engine:

   1. Open your `<pf_install>/pingfederate/bin/run.properties` file.

   2. Change `pf.provisioner.mode` to `STANDALONE`.

   3. Save the file.

   |   |                                                                                                                                                                                                                                        |
   | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | To configure the `FAILOVER` mode instead, see [Deploying provisioning failover](https://docs.pingidentity.com/pingfederate/latest/server_clustering_guide/pf_deploy_provis_failover.html) in the PingFederate Server Clustering Guide. |

6. Start PingFederate.

7. If you operate PingFederate in a cluster, repeat steps 2-4 and step 6 for each engine node.

---

---
title: Download manifest
description: The following files are included in the Zscaler Internet Access Provisioner .zip archive:
component: zscaler
page_id: zscaler:zscaler_internet_access_provisioner:pf_zscaler_zia_connector_download_manifest
canonical_url: https://docs.pingidentity.com/integrations/zscaler/zscaler_internet_access_provisioner/pf_zscaler_zia_connector_download_manifest.html
revdate: June 18, 2024
---

# Download manifest

The following files are included in the Zscaler Internet Access Provisioner `.zip` archive:

* `legal` – a directory that contains the legal document.

  * `Legal.pdf` – copyright and license information.

* `dist` – contains the integration files.

  * `pf-zscaler-zia-quickconnection-<version>.jar` – The Zscaler Internet Access Provisioner quick connection template.

---

---
title: Download manifest
description: The following files are included in the Zscaler Private Access Provisioner .zip archive:
component: zscaler
page_id: zscaler:zscaler_private_access_provisioner:pf_zscaler_zpa_connector_download_manifest
canonical_url: https://docs.pingidentity.com/integrations/zscaler/zscaler_private_access_provisioner/pf_zscaler_zpa_connector_download_manifest.html
revdate: June 18, 2024
---

# Download manifest

The following files are included in the Zscaler Private Access Provisioner `.zip` archive:

* `legal` – a directory that contains the legal document.

  * `Legal.pdf` – copyright and license information.

* `dist` – contains the integration files.

  * `pf-zscaler-zpa-quickconnection-<version>.jar` – The Zscaler Private Access Provisioner quick connection template.

---

---
title: Enabling provisioning and single sign-on in PingFederate
description: To use PingFederate for provisioning and single sign-on, configure an external datastore and set a SAML entity ID.
component: zscaler
page_id: zscaler:zscaler_internet_access_provisioner:pf_zscaler_zia_connector_enabling_provisioning_and_single_sign_on_in_pf
canonical_url: https://docs.pingidentity.com/integrations/zscaler/zscaler_internet_access_provisioner/pf_zscaler_zia_connector_enabling_provisioning_and_single_sign_on_in_pf.html
revdate: June 18, 2024
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
component: zscaler
page_id: zscaler:zscaler_internet_access_provisioner:pf_zscaler_zia_connector_enabling_provisioning_and_single_sign_on_in_pf_100_or_earlier
canonical_url: https://docs.pingidentity.com/integrations/zscaler/zscaler_internet_access_provisioner/pf_zscaler_zia_connector_enabling_provisioning_and_single_sign_on_in_pf_100_or_earlier.html
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
component: zscaler
page_id: zscaler:zscaler_internet_access_provisioner:pf_zscaler_zia_connector_enabling_provisioning_and_single_sign_on_in_pf_101_or_later
canonical_url: https://docs.pingidentity.com/integrations/zscaler/zscaler_internet_access_provisioner/pf_zscaler_zia_connector_enabling_provisioning_and_single_sign_on_in_pf_101_or_later.html
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
title: Enabling provisioning and single sign-on in Zscaler
description: Register PingFederate as an identity provider in Zscaler and download the SAML metadata information.
component: zscaler
page_id: zscaler:zscaler_private_access_provisioner:pf_zscaler_zpa_connector_enabling_provisioning_and_single_sign_on_in_zscaler
canonical_url: https://docs.pingidentity.com/integrations/zscaler/zscaler_private_access_provisioner/pf_zscaler_zpa_connector_enabling_provisioning_and_single_sign_on_in_zscaler.html
revdate: June 18, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Enabling provisioning and single sign-on in Zscaler

Register PingFederate as an identity provider in Zscaler and download the SAML metadata information.

## About this task

For more information about configuring Zscaler, see [Configuring an IdP for Single Sign-On](https://help.zscaler.com/zpa/configuring-idp-single-sign) and [Enabling SCIM for Identity Management](https://help.zscaler.com/zpa/enabling-scim-identity-management) in the Zscaler Private Access documentation.

## Steps

1. Sign on to Zscaler Private Access as an administrator.

2. On the **Administration > Authentication > Settings** page, click **Add IdP Configuration**.

3. On the **Add IdP Configuration** modal, on the **IdP Information** tab, complete the basic information. Click **Next**.

   |   |                                                                                                                                                                                                                                                |
   | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | If you cannot select an authentication domain, contact Zscaler. For more information, see [Configuring Authentication Settings](https://help.zscaler.com/zpa/configuring-authentication-settings) in the Zscaler Private Access documentation. |

4. On the **SP Metadata** tab, click **Download Metadata**. Save the file as `sp_metadata.xml`.

5. Click **Download Certificate**. You will use this in [Creating a single sign-on connection](pf_zscaler_zpa_connector_creating_a_single_sign_on_connection.html). Click **Next**.

6. On the **Create IdP** tab, complete the information from PingFederate.

   1. For the **IdP Metadata File**, upload the `metadata.xml` file that you exported in [Exporting SAML metadata from PingFederate](pf_zscaler_zpa_connector_exporting_saml_metadata_from_pf.html).

   2. For the **IdP Certificate**, upload your PingFederate signing certificate. For instructions, see [Managing digital signing certificates and decryption keys](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_certmanagementtasklet_dsigsigningcert_certmanagementstate.html) in the PingFederate documentation.

   3. In the **Single Sign-On URL** field, enter your PingFederate single sign-on endpoint based on the following.

      ```none
      https://pf_host:pf_port/idp/SSO.saml2
      ```

   4. In the **IdP Entity ID** field, enter the **SAML 2.0 Entity ID** that you created in [Enabling single sign-on in PingFederate](pf_zscaler_zpa_connector_enabling_single_sign_on_in_pf.html).

7. In the **SCIM** section, configure SCIM provisioning. Click **Save**.

   1. For **SCIM Sync**, click **Enable**.

   2. Note the **SCIM Service Provider Endpoint** and **Bearer Token**. You will use these in [Creating a provisioning connection](pf_zscaler_zpa_connector_creating_a_provisioning_connection.html).

---

---
title: Enabling single sign-on in PingFederate
description: Before you can configure single sign-on in Zscaler Private Access, you need to set a SAML entity ID in PingFederate.
component: zscaler
page_id: zscaler:zscaler_private_access_provisioner:pf_zscaler_zpa_connector_enabling_single_sign_on_in_pf
canonical_url: https://docs.pingidentity.com/integrations/zscaler/zscaler_private_access_provisioner/pf_zscaler_zpa_connector_enabling_single_sign_on_in_pf.html
revdate: June 18, 2024
section_ids:
  enabling-single-sign-on-in-pingfederate-10-1-or-later: Enabling single sign-on in PingFederate 10.1 or later
  steps: Steps
  enabling-single-sign-on-in-pingfederate-10-0-or-earlier: Enabling single sign-on in PingFederate 10.0 or earlier
  steps-2: Steps
---

# Enabling single sign-on in PingFederate

Before you can configure single sign-on in Zscaler Private Access, you need to set a SAML entity ID in PingFederate.

## Enabling single sign-on in PingFederate 10.1 or later

### Steps

1. On the PingFederate administrative console, go to **System > Protocol Settings > Federation Info**.

2. In the **SAML 2.0 Entity ID** field, enter a name for PingFederate to use to identify itself to SAML partners.

3. Click **Save**.

## Enabling single sign-on in PingFederate 10.0 or earlier

### Steps

1. On the PingFederate administrative console, go to **System > Protocol Settings > Roles & Protocols**.

2. Select the **Enable Identity Provider IdP Role and Support the Following** check box.

3. Select the **SAML 2.0** check box. Click **Next**.

4. Go to the **Federation Info** tab.

5. In the **SAML 2.0 Entity ID** field, enter a name for PingFederate to use to identify itself to SAML partners.

6. Click **Save**.

---

---
title: Enabling single sign-on in PingFederate 10.0 or earlier
description: On the PingFederate administrative console, go to System > Protocol Settings > Roles & Protocols.
component: zscaler
page_id: zscaler:zscaler_private_access_provisioner:pf_zscaler_zpa_connector_enabling_single_sign_on_in_pf_100_or_earlier
canonical_url: https://docs.pingidentity.com/integrations/zscaler/zscaler_private_access_provisioner/pf_zscaler_zpa_connector_enabling_single_sign_on_in_pf_100_or_earlier.html
revdate: June 27, 2024
section_ids:
  steps: Steps
---

# Enabling single sign-on in PingFederate 10.0 or earlier

## Steps

1. On the PingFederate administrative console, go to **System > Protocol Settings > Roles & Protocols**.

2. Select the **Enable Identity Provider IdP Role and Support the Following** check box.

3. Select the **SAML 2.0** check box. Click **Next**.

4. Go to the **Federation Info** tab.

5. In the **SAML 2.0 Entity ID** field, enter a name for PingFederate to use to identify itself to SAML partners.

6. Click **Save**.

---

---
title: Enabling single sign-on in PingFederate 10.1 or later
description: On the PingFederate administrative console, go to System > Protocol Settings > Federation Info.
component: zscaler
page_id: zscaler:zscaler_private_access_provisioner:pf_zscaler_zpa_connector_enabling_single_sign_on_in_pf_101_or_later
canonical_url: https://docs.pingidentity.com/integrations/zscaler/zscaler_private_access_provisioner/pf_zscaler_zpa_connector_enabling_single_sign_on_in_pf_101_or_later.html
revdate: June 27, 2024
section_ids:
  steps: Steps
---

# Enabling single sign-on in PingFederate 10.1 or later

## Steps

1. On the PingFederate administrative console, go to **System > Protocol Settings > Federation Info**.

2. In the **SAML 2.0 Entity ID** field, enter a name for PingFederate to use to identify itself to SAML partners.

3. Click **Save**.

---

---
title: Exporting SAML metadata from PingFederate
description: Export a metadata file that describes your PingFederate identity provider configuration.
component: zscaler
page_id: zscaler:zscaler_private_access_provisioner:pf_zscaler_zpa_connector_exporting_saml_metadata_from_pf
canonical_url: https://docs.pingidentity.com/integrations/zscaler/zscaler_private_access_provisioner/pf_zscaler_zpa_connector_exporting_saml_metadata_from_pf.html
revdate: June 18, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
  choose-from: Choose from:
---

# Exporting SAML metadata from PingFederate

Export a metadata file that describes your PingFederate identity provider configuration.

## About this task

For general information about these steps, see [Metadata export](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_metadata_export.html) in the PingFederate documentation.

## Steps

1. In the PingFederate administrative console, go to the **Metadata Export** window\..

   ### Choose from:

   * For PingFederate 10.1 or later: go to **System > Protocol Metadata > Metadata Export**.

   * For PingFederate 10.0 or earlier: go to **System > Metadata Export**.

2. If you see the **Metadata Role** tab, select **I am the identity provider (IdP)**. Click **Next**.

3. On the **Metadata Mode** tab, select **Select information to include in metadata manually**. Click **Next**.

4. On the **Protocol** tab, click **Next**.

5. On the **Attribute Contract** tab, click **Next**.

6. On the **Signing Key** tab, select a signing certificate. Click **Next**.

7. **Optional:** On the **Metadata Signing** tab, select a certificate to sign the metadata XML file. Click **Next**.

8. On the **XML Encryption Certificate** tab, select the certificate that you want to use to encrypt the XML content. Click **Next**.

9. On the **Export & Summary** tab, click **Export**.

10. Save `metadata.xml`.

11. Click **Done**.