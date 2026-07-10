---
title: Changelog
description: Fixed an issue that caused the provisioning engine to see email1 and Email 1 as different devices. This could cause an error when the provisioning engine tried to add a new device instead of updating the existing device.
component: pingid-sdk
page_id: pingid-sdk:release_notes:pf_pid_sdk_connector_changelog
canonical_url: https://docs.pingidentity.com/integrations/pingid-sdk/release_notes/pf_pid_sdk_connector_changelog.html
llms_txt: https://docs.pingidentity.com/integrations/pingid-sdk/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 19, 2024
section_ids:
  pingid-sdk-connector-1-2-2-october-2020: PingID SDK Connector 1.2.2 – October 2020
  pingid-sdk-connector-1-2-1-september-2019: PingID SDK Connector 1.2.1 – September 2019
  pingid-sdk-connector-1-2-may-2019: PingID SDK Connector 1.2 – May 2019
  pingid-sdk-connector-1-1-october-2018: PingID SDK Connector 1.1 – October 2018
  pingid-sdk-connector-1-0-1-august-2018: PingID SDK Connector 1.0.1 – August 2018
  pingid-sdk-connector-1-0-april-2018: PingID SDK Connector 1.0 – April 2018
---

# Changelog

## PingID SDK Connector 1.2.2 – October 2020

* Fixed an issue that caused the provisioning engine to see `email1` and `Email 1` as different devices. This could cause an error when the provisioning engine tried to add a new device instead of updating the existing device.

## PingID SDK Connector 1.2.1 – September 2019

* Improved username validation and encoding to support API changes.

## PingID SDK Connector 1.2 – May 2019

* Fixed a library issue that prevented users from being deprovisioned in PingFederate 8.1.4 and earlier.

* Fixed an issue that caused the connector to use the wrong EU hostname.

* Added a PingID SDK configuration file upload option to speed up configuration in PingFederate 9.0 and later.

## PingID SDK Connector 1.1 – October 2018

* Added support for three Voice Number user attributes.

* Added support for **Primary Authentication Method Upon Creation** configuration.

* Improved error handling and reporting when PingID users contain no ID.

## PingID SDK Connector 1.0.1 – August 2018

* Fixed an issue when a device is updated. Any unchanged devices on the user account were being removed and re-added to the user.

## PingID SDK Connector 1.0 – April 2018

* Initial release

* Added support for PingID SDK v1.0

* Added support for user life cycle management (including creates, updates, disabling users, and deleting users)

* Added configuration options for workflow capabilities (for example, the ability to disable updates)

---

---
title: Configure provisioning
description: Configure PingFederate to provision users to PingID SDK.
component: pingid-sdk
page_id: pingid-sdk:setup:pf_pid_sdk_connector_configure_provisioning
canonical_url: https://docs.pingidentity.com/integrations/pingid-sdk/setup/pf_pid_sdk_connector_configure_provisioning.html
llms_txt: https://docs.pingidentity.com/integrations/pingid-sdk/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 19, 2024
section_ids:
  context_N10025_N10022_N10001: About this task
  steps: Steps
  ul_c5n_d54_phb: Choose from:
---

# Configure provisioning

## About this task

Configure PingFederate to provision users to PingID SDK.

|   |                                                                                                     |
| - | --------------------------------------------------------------------------------------------------- |
|   | You can follow these steps to create a new SP connection, or you can modify an existing connection. |

## Steps

1. In the PingFederate administrator console, configure the data store that PingFederate will use as the source of user data. For instructions, see [Datastores](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_managedatasourcestasklet_managedatasourcesstate.html) in the PingFederate documentation.

   * When targeting users and groups for provisioning, exclude the user account that you will use to administer users in your connection to PingID SDK. This prevents the PingFederate provisioning engine from interfering with the account that provisions users and groups.

2. Enable provisioning.

   1. On the **System > Protocol Settings > Roles & Protocols** screen, select **Enable Identity Provider IdP Role and Support the Following**.

   2. Select **Outbound Provisioning** and **SAML 2.0**. Click **Save**.

3. Create an SP connection with the PingID SDK quick connection template.

   1. On the **Identity Provider** screen, in the **SP Connections** area, click **Create new**.

   2. On the **Connection Template** screen, select **Use a template for this connection**.

   3. In the **Connection Template** list, select **PingID SDK Connector**. Click **Next**.

4. On the **Connection Type** screen, clear **Browser SSO Profiles** and select **Outbound Provisioning**. Click **Next**.

5. On the **General Info** screen, click **Next**.

6. On the **Outbound Provisioning** screen, configure the provisioning target and channel.

   See [Configuring outbound provisioning](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_spconnectionconfigtasklet_saasprovisioningstate.html) in the PingFederate documentation.

   1. Click **Configure Provisioning**.

   2. On the **Target** screen, complete the **Application ID** field with the value that you noted in [Get information from the PingID SDK](pf_pid_sdk_connector_get_information_from_pid_sdk.html).

      |   |                                                                                        |
      | - | -------------------------------------------------------------------------------------- |
      |   | PingFederate verifies the credentials when you activate the channel and SP connection. |

   3. Complete the PingID SDK information by doing one of the following:

      ### Choose from:

      * For PingFederate 9.0 and later: On the **PingID SDK Properties** line, click **Choose File**. Select the `pingidsdk.properties` file that you saved in [Get information from the PingID SDK](pf_pid_sdk_connector_get_information_from_pid_sdk.html), and then click **Open**.

      * For PingFederate 8.x: Complete the required fields by copying and pasting the values from the `pingidsdk.properties` file that you saved in [Get information from the PingID SDK](pf_pid_sdk_connector_get_information_from_pid_sdk.html).

   4. From the **Primary Authentication Method Upon Creation** list, select a primary authentication method to set when the connector provisions new users to PingID SDK.

      |   |                                                                                                                                                                                                                                                                                                                                   |
      | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      |   | Users are prompted to authenticate using their primary device. If the user has no mapped attribute value (or an invalid value) for the selected method, the primary device pairing is set to the next valid attribute in this order: `email 1`, `email 2`, `email 3`, `SMS 1`, `SMS 2`, `SMS 3`, `voice 1`, `voice 2`, `voice 3`. |

   5. Optional: Under **Provisioning Options**, enable the provisioning features that you want.

      See [Provisioning options](pf_pid_sdk_connector_provisioning_options.html).

   6. In the **Remove User Action** list, select the deprovisioning action for users in PingID SDK. This is triggered when a user in the datastore is deleted, disabled, or no longer targeted for provisioning. Click **Next**.

   7. On the **Manage Channels** screen, create a channel. Click **Done**.

      See [Managing channels](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_saasmanagementtasklet_saasmanagementstate.html) in the PingFederate documentation.

      |   |                                                                                                                                                                                                                                                                                            |
      | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
      |   | To set up synchronization, use the **SP Connection > Configure Channels > Channel > Attribute Mapping** screen to populate the `Username` attribute with a matching attribute from the data store. See [Synchronize existing users](pf_pid_sdk_connector_synchronize_existing_users.html). |

   8. On the **Outbound Provisioning** screen, click **Next**.

7. On the **Activation and Summary** screen, above the **Summary** section, turn on the connection. Click **Save**.

---

---
title: Deploy the provisioning connector
description: This section describes the common steps required to install the PingFederate PingID SDK Connector.
component: pingid-sdk
page_id: pingid-sdk:setup:pf_pid_sdk_connector_deploy_the_provisioning_connector
canonical_url: https://docs.pingidentity.com/integrations/pingid-sdk/setup/pf_pid_sdk_connector_deploy_the_provisioning_connector.html
llms_txt: https://docs.pingidentity.com/integrations/pingid-sdk/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 19, 2024
section_ids:
  context_N10025_N10022_N10001: About this task
  steps: Steps
---

# Deploy the provisioning connector

## About this task

This section describes the common steps required to install the PingFederate PingID SDK Connector.

## Steps

1. Download the PingID SDK Connector `.zip` archive from the [**Add-ons** tab of the PingFederate downloads page](https://www.pingidentity.com/en/resources/downloads/pingfederate.html) or the [Ping Identity Marketplace](https://marketplace.pingone.com/item/pingid-sdk-integration-kit).

1) Stop PingFederate.

2) Delete any existing PingID SDK Connector files in the PingFederate directory.

   1. Go to `<pf_install>/pingfederate/server/default/deploy`.

   2. Delete `pf-pingidsdk-quickconnection-<version>.jar`.

3) Deploy the provisioning connector.

   1. Extract the PingID SDK Connector distribution file, and then go to `dist`.

   2. Copy `pf-pingidsdk-quickconnection-<version>.jar` to `<pf_install>` `/pingfederate/server/default/deploy`.

4) Enable the PingFederate provisioning engine.

   1. In `<pf_install>/pingfederate/bin`, open `run.properties` for editing.

   2. Change `pf.provisioner.mode` to `STANDALONE`. Save the file.

      |   |                                                                                                                                                                                                                                          |
      | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      |   | To configure the `FAILOVER` mode instead, see [Deploying provisioning failover](https://docs.pingidentity.com/pingfederate/latest/server_clustering_guide/pf_deploy_provis_failover.html) in the PingFederate *Server Clustering Guide*. |

5) Start PingFederate.

6) If you operate PingFederate in a cluster, repeat steps 1 - 5 for each instance of PingFederate.

---

---
title: Download manifest
description: The distribution .zip archive for the connector contains the following:
component: pingid-sdk
page_id: pingid-sdk:release_notes:pf_pid_sdk_connector_download_manifest
canonical_url: https://docs.pingidentity.com/integrations/pingid-sdk/release_notes/pf_pid_sdk_connector_download_manifest.html
llms_txt: https://docs.pingidentity.com/integrations/pingid-sdk/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 19, 2024
---

# Download manifest

The distribution `.zip` archive for the connector contains the following:

* `ReadMeFirst.pdf `– contains links to this online documentation.

* `/legal`:

  * `Legal.pdf` – copyright and license information.

* `/dist` – contains libraries needed for the connector:

  * `pf-pingidsdk-quickconnection-<version>.jar` – PingFederate PingID SDK Connector

---

---
title: Get information from the PingID SDK
description: PingFederate needs connection information and an application ID from PingOne to manage users in the PingID SDK.
component: pingid-sdk
page_id: pingid-sdk:setup:pf_pid_sdk_connector_get_information_from_pid_sdk
canonical_url: https://docs.pingidentity.com/integrations/pingid-sdk/setup/pf_pid_sdk_connector_get_information_from_pid_sdk.html
llms_txt: https://docs.pingidentity.com/integrations/pingid-sdk/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 19, 2024
section_ids:
  context_N10025_N10022_N10001: About this task
  steps: Steps
---

# Get information from the PingID SDK

## About this task

PingFederate needs connection information and an application ID from PingOne to manage users in the PingID SDK.

## Steps

1. Sign on to the PingOne administrator console.

2. Export the configuration file for the PingID SDK:

   1. On the **Setup > PingID > Client Integration** screen, under **Integrate with PingID SDK**, click **Download**.

   2. Save the `pingidsdk.properties` file to a temporary location.

3. Get the application ID that PingOne assigned to PingFederate.

   1. Create an application to represent PingFederate in PingOne by completing the [Configuring a new PingID SDK app](https://docs.pingidentity.com/pingid/pingid_sdk/pid_sdk_config_new_app.html) procedure in the PingID *Administration Guide*.

      |   |                                                                                                                                                      |
      | - | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
      |   | Under **Alternate Authentication Methods**, enable authentication methods to make the associated attributes available to the provisioning connector. |

   2. On the **Applications > PingID SDK Applications** screen, note the **Application ID** for the application that you created.

---

---
title: Known issues and limitations
description: There are no known issues.
component: pingid-sdk
page_id: pingid-sdk:release_notes:pf_pid_sdk_connector_known_issues_and_limitations
canonical_url: https://docs.pingidentity.com/integrations/pingid-sdk/release_notes/pf_pid_sdk_connector_known_issues_and_limitations.html
llms_txt: https://docs.pingidentity.com/integrations/pingid-sdk/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 19, 2024
section_ids:
  section_ypj_xnn_phb: Known issues
  section_mk1_ynn_phb: Known limitations
---

# Known issues and limitations

## Known issues

There are no known issues.

## Known limitations

* Due to a limitation with PingFederate 8.1 and earlier versions, when configuring two SP connections with the same provisioner, the second connection built may be pre-populated with the channel from the first connection. To avoid conflicts, delete this pre-populated channel and create a unique channel for each connection.

* When an LDAP user is deleted in a targeted group distinguished name (DN), the provisioning connector does not propagate the deletion until a new user is added to the group. This limitation is compounded when the **User Create** provisioning option is disabled. For solutions, see [SaaS provisioner does not remove the user](https://support.pingidentity.com/s/article/After-deleting-an-AD-user-account-SaaS-provisioner-does-not-remove-the-user-in-the-next-provisioning-cycle-when-Group-DN-is-specified) in the Knowledge Base.

* Due to PingFederate limitations, user attributes cannot be cleared once set.

* Provisioning options may interact to produce undesired results if configured against recommendations. For example, we recommend that Provision Disabled Users be set to false when Remove User Action is Delete. If it is set to true, the following can occur:

  * A user exists in an active state in the user store and in PingID SDK. The user is disabled in the user store, so the provisioner deletes it from PingID SDK. An attribute of the user is updated in the user store. The provisioner will then re-create the user in PingID SDK in a disabled state.

- The PingID SDK Connector manages all mapped email, SMS, and voice pairings. A device nickname of `Email 1` and an attribute name of `email1` are considered a pair. If the connector finds a device nickname (not attribute name) of `email1` (created by a previous version of the connector) and a device nickname of `Email 1`, the latter takes priority and the former is removed.

- If the selected **Primary Authentication Method Upon Creation** has no mapped attribute value or an invalid value, the primary device pairing will be set to the next available mapped attribute value. The order is Email (1, 2, 3), SMS (1, 2, 3), Voice (1, 2, 3).

**Assigning a user to multiple applications**

* When managing multiple PingID SDK Applications, it is possible for a user to have a different active status in each application due to device pairings.

* The PingID SDK create and suspend endpoints are global across all applications managed by your admin account. This means that if a user's status changes in one application, the same action will be taken on all applications managed by your admin account.

  * If you create a user in one application with a device to pair, the user will be created in an `active` state in that application and a `not_active` state in other applications.

  * If there are two applications, each of which has an SP connection set up for it. In one SP connection, the Remove User Action is set to Disable and in the other it is set to Delete. A user in the directory has been targeted by both connections and as such, that user exists in both applications. The user is then disabled in the directory. Provisioner logs will show a delete and a create. The user will end up in a suspended state in both applications.

  * If there are two applications, each of which has an SP connection set up for it. In one SP connection, the Remove User Action is set to Disable and in the other it is set to Delete. Create a user in application A with an email or other device to pair. Create a user with the same username in the directory without the email or device. The user will then exist in an `active` state in application A and a `not_active` state in application B. Disable the user in the directory. The user will then be suspended in both applications. Enable the user in the directory. The user will then be `not_active` in both applications.

---

---
title: PingID SDK Provisioner
description: The PingID SDK Provisioner allows PingFederate to manage users in PingID SDK based on changes in an external user datastore.
component: pingid-sdk
page_id: pingid-sdk::pf_pid_sdk_connector
canonical_url: https://docs.pingidentity.com/integrations/pingid-sdk/pf_pid_sdk_connector.html
llms_txt: https://docs.pingidentity.com/integrations/pingid-sdk/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 19, 2024
section_ids:
  section_cys_3hx_nkb: Features
  section_qp5_hhx_nkb: Components
  section_byd_3hx_nkb: Intended audience
  section_byk_3hx_nkb: System requirements
---

# PingID SDK Provisioner

The PingID SDK Provisioner allows PingFederate to manage users in PingID SDK based on changes in an external user datastore.

## Features

* Manages users in PingID SDK based on changes in an external data store that is attached to PingFederate

  * Creates, updates, disables, and deletes users

  * Enable the create, update, disable and delete capabilities independently

- Allows you to set a primary authentication method (email, SMS, voice) for new users that are provisioned to PingID SDK

- Manages all email, SMS, and voice pairings

  * Does not remove pairings that already exist in PingID SDK unless the device nickname of the pairing matches that of the attribute name in the connector

* See a list of [Supported attributes reference](setup/pf_pid_sdk_connector_supported_attributes_reference.html)

## Components

PingID SDK provisioning connector

* Allows PingFederate to manage users in PingID SDK based on changes in an external user datastore.

* Includes a quick-connection template that pre-populates some configuration settings.

## Intended audience

This document is intended for PingFederate administrators. Before you start, you should be familiar with the following:

* [PingID SDK Overview](https://apidocs.pingidentity.com/pingid-sdk/guide/overview/) in the PingID SDK documentation.

* The following sections of the PingFederate documentation:

  * [Identity provider SSO configuration](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_ident_provid_sso_config.html)

  * [Datastores](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_managedatasourcestasklet_managedatasourcesstate.html)

  * [Managing IdP adapters](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_managing_idp_adapters.html)

  * [Managing digital signing certificates and decryption keys](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_certmanagementtasklet_dsigsigningcert_certmanagementstate.html)

  * [SP connection management](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_sp_connect_management.html)

  * [Configuring outbound provisioning](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_spconnectionconfigtasklet_saasprovisioningstate.html)

  * [Configuring outbound provisioning settings](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_protocolsettingstasklet_saasglobalprovisioningsettingsstate.html)

## System requirements

* PingFederate 9.0 or later.

* To allow PingFederate to make outbound connections to the PingID SDK API, you may need to whitelist the following domains in your firewall:

  * North America: sdk.pingid.com

  * Europe: sdk.pingid.eu

  * Australia: sdk.pingid.com.au

---

---
title: Provisioning options
description: User Create
component: pingid-sdk
page_id: pingid-sdk:setup:pf_pid_sdk_connector_provisioning_options
canonical_url: https://docs.pingidentity.com/integrations/pingid-sdk/setup/pf_pid_sdk_connector_provisioning_options.html
llms_txt: https://docs.pingidentity.com/integrations/pingid-sdk/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 19, 2024
---

# Provisioning options

| Field Name                                                                                                                                                    | Description                                                                                                                                                                                                                                                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **User Create**                                                                                                                                               | **Selected** (default): PingFederate creates users.**Cleared**: PingFederate does not create users.                                                                                                                                                                                                                                                |
| **User Update**                                                                                                                                               | **Selected** (default): PingFederate updates existing users.**Cleared**: PingFederate does not update existing users.                                                                                                                                                                                                                              |
| **User Disable/Delete**                                                                                                                                       | **Selected** (default): PingFederate disable or delete users.&#xA;&#xA;PingFederate can only re-enable a user if User Update is selected.**Cleared**: PingFederate does not disable or delete users.&#xA;&#xA;The Remove User Action option controls whether PingFederate deletes or disables users.                                               |
| **Provision Disabled Users**                                                                                                                                  | **Selected**: When a user is flagged as "disabled" in the data store, PingFederate provisions the user with a "disabled" flag.&#xA;&#xA;Only enable this option if User Create is enabled, and Remove User Action is set to Disable.**Cleared** (default): PingFederate does not provision users that are flagged as "disabled" in the data store. |
| &#xA;&#xA;If any of the above options are cleared, PingFederate logs a warning in the user workflow section of provisioner.log when the related action fails. |                                                                                                                                                                                                                                                                                                                                                    |

---

---
title: Supported attributes reference
description: The following table lists the attributes that can be mapped for user provisioning.
component: pingid-sdk
page_id: pingid-sdk:setup:pf_pid_sdk_connector_supported_attributes_reference
canonical_url: https://docs.pingidentity.com/integrations/pingid-sdk/setup/pf_pid_sdk_connector_supported_attributes_reference.html
llms_txt: https://docs.pingidentity.com/integrations/pingid-sdk/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 19, 2024
---

# Supported attributes reference

The following table lists the attributes that can be mapped for user provisioning.

For more details, see the following topics in the PingID SDK API documentation:

* [Users API](https://apidocs.pingidentity.com/pingid-sdk/guide/server-api/pid_c_SDKapiUsers/)

* [Offline devices (SMS) pairing API](https://apidocs.pingidentity.com/pingid-sdk/guide/server-api/pid_c_SDKotpDevicesPair/)

* [Offline devices (email) pairing API](https://apidocs.pingidentity.com/pingid-sdk/guide/server-api/pid_c_SDKotpEmailDevicesPair/)

* [Offline devices (voice) pairing API](https://apidocs.pingidentity.com/pingid-sdk/guide/server-api/pid_c_SDKvoiceDevicesPair/)

|   |                                                                                                                                                                                                                                                                                                                                                                                         |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The PingID SDK Connector manages all mapped email, SMS, and voice pairings. A device nickname of `Email 1` and an attribute name of `email1` are considered a pair. If the connector finds a device nickname (not attribute name) of `email1` (created by a previous version of the connector) and a device nickname of `Email 1`, the latter takes priority and the former is removed. |

| Attribute      | Description                                                                                                                                                                                                  |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Username       | PingID SDK's unique identifier for the user. A username cannot be changed.This attribute is required.                                                                                                        |
| First Name     | The given name of the user.For example, "Barbara" in the full name "Ms. Barbara Jane Jensen, III".                                                                                                           |
| Last Name      | The family name of the user.For example, "Jensen" in the full name "Ms. Barbara Jane Jensen, III".                                                                                                           |
| Email 1        | An email address to use for pairing.                                                                                                                                                                         |
| Email 2        | A second email address to use for pairing.                                                                                                                                                                   |
| Email 3        | A third email address to use for pairing.                                                                                                                                                                    |
| SMS Number 1   | A phone number to use for SMS pairing.The phone number must begin with the country code. The PingID SDK server removes all characters except for numbers, so the number doesn't require specific formatting. |
| SMS Number 2   | A second phone number to use for SMS pairing.                                                                                                                                                                |
| SMS Number 3   | A third phone number to use for SMS pairing.                                                                                                                                                                 |
| Voice Number 1 | A phone number to use for voice calls.The phone number must begin with the country code. The PingID SDK server removes all characters except for numbers, so the number doesn't require specific formatting. |
| Voice Number 2 | A second phone number to use for voice calls.                                                                                                                                                                |
| Voice Number 3 | A third phone number to use for voice calls.                                                                                                                                                                 |

---

---
title: Synchronize existing users
description: When the provisioning connector updates users between the data store and PingID SDK, it synchronizes users that share an identical Username attribute.
component: pingid-sdk
page_id: pingid-sdk:setup:pf_pid_sdk_connector_synchronize_existing_users
canonical_url: https://docs.pingidentity.com/integrations/pingid-sdk/setup/pf_pid_sdk_connector_synchronize_existing_users.html
llms_txt: https://docs.pingidentity.com/integrations/pingid-sdk/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 19, 2024
---

# Synchronize existing users

When the provisioning connector updates users between the data store and PingID SDK, it synchronizes users that share an identical `Username` attribute.

Example scenario:

* In PingID SDK, Janet's `Username` is `jsmith`.

* In your data store, Janet's `sAMAccountName` is `jsmith`.

* On the **Attribute Mapping** screen, you map the `Username` attribute to `sAMAccountName`.

* When the provisioning connector runs, the data store user is provisioned with a `Username` of `jsmith`. That matches Janet's existing `Username` in PingID SDK, so her information in the data store is synchronized to her PingID SDK account.

---

---
title: Upgrade an existing connector
description: Upgrading from a previous version of the PingID SDK Connector? Create a new connection and copy the configuration from your existing connection.
component: pingid-sdk
page_id: pingid-sdk:setup:pf_pid_sdk_connector_upgrade_an_existing_connector
canonical_url: https://docs.pingidentity.com/integrations/pingid-sdk/setup/pf_pid_sdk_connector_upgrade_an_existing_connector.html
llms_txt: https://docs.pingidentity.com/integrations/pingid-sdk/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 19, 2024
section_ids:
  context_N10025_N10022_N10001: About this task
  steps: Steps
---

# Upgrade an existing connector

## About this task

Upgrading from a previous version of the PingID SDK Connector? Create a new connection and copy the configuration from your existing connection.

## Steps

1. Note the attribute mapping configuration from your existing provisioning connection.

   1. On the PingFederate administrator console, on the **Identity Provider** screen, in the **SP Connections** area, click your existing provisioning connection.

   2. On the **Outbound Provisioning** screen, click **Configure Provisioning**.

   3. On the **Manage Channels** screen, click your existing channel configuration.

   4. On the **Attribute Mapping** screen, note your existing attribute mappings.

2. Disable and delete your existing provisioning connection.

   1. On the **Identity Provider** screen, in the **SP Connections** area, click **Manage All**.

   2. Disable your existing provisioning connection.

   3. Click **Select Action**, and then click **Delete**. Click **Save**.

3. Complete the steps in [Deploy the provisioning connector](pf_pid_sdk_connector_deploy_the_provisioning_connector.html).

4. Complete the steps in [Configure provisioning](pf_pid_sdk_connector_configure_provisioning.html) to configure a new SP connection.

   1. On the **Outbound Provisioning > Manage Channels > Attribute Mapping** screen, configure the attribute mappings based on your notes from step 1.