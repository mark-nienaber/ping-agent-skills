---
title: Changelog
description: The following is the change history for the PingID Provisioner.
component: pingid
page_id: pingid:release_notes:pf_pid_connector_changelog
canonical_url: https://docs.pingidentity.com/integrations/pingid/release_notes/pf_pid_connector_changelog.html
revdate: March 31, 2026
section_ids:
  version-1-1-2: Version 1.1.2
  version-1-1-1: Version 1.1.1
  version-1-1: Version 1.1
  version-1-0-1: Version 1.0.1
  version-1-0: Version 1.0
---

# Changelog

The following is the change history for the PingID Provisioner.

## Version 1.1.2

Released in March 2026.

* Improved security by updating bundled components. Removed outdated third-party files and dependencies to address a potential security vulnerability.

## Version 1.1.1

Released in November 2021.

* Improved security by updating bundled components.

## Version 1.1

Released in March 2021.

* Added support for device management.

* Added support for the **Provision Disabled Users** and **User Create** provisioning settings. Learn more in [PingID Connector settings reference](../setup/pf_pid_connector_pid_connector_settings_reference.html).

* Added the **Manage Devices** and **Primary Devices on Create** settings. Learn more in [PingID Connector settings reference](../setup/pf_pid_connector_pid_connector_settings_reference.html).

* Added the ability to upload the `pingid.properties` file. Learn more in [Get your PingID settings file](../setup/pf_pid_connector_get_your_pid_settings_file.html).

## Version 1.0.1

Released in May 2018.

* Fixed an issue that caused deletion of users when **User Update** was set to `false` in the configuration settings.

## Version 1.0

Released in March 2018.

* Initial release.

* Added support for PingID API 4.9.

* Added support for user lifecycle management. This includes updates, disabling users, and deleting users.

* Added configuration options for workflow capabilities. For example, the ability to disable updates.

---

---
title: Creating a provisioning connection
description: To allow PingFederate to manage users in PingID, create a service provider (SP) connection.
component: pingid
page_id: pingid:setup:pf_pid_connector_creating_a_provisioning_connection
canonical_url: https://docs.pingidentity.com/integrations/pingid/setup/pf_pid_connector_creating_a_provisioning_connection.html
revdate: June 18, 2024
section_ids:
  steps: Steps
  choose-from: Choose from:
---

# Creating a provisioning connection

To allow PingFederate to manage users in PingID, create a service provider (SP) connection.

## Steps

1. In the PingFederate administrator console, create a new SP connection:

   ### Choose from:

   * For PingFederate 10.1 or later: go to **Applications > Integration > SP Connections**. Click **Create Connection**.

   * For PingFederate 10.0 or earlier: go to **Identity Provider > SP Connections**. Click **Create Connection**.

2. Configure the basic connection details with the PingID Provisioner quick connection template.

   1. On the **Connection Template** tab, select **Use a template for this connection**.

   2. In the **Connection Template** list, select **PingID Provisioner**. Click **Next**.

   3. On the **Connection Type** tab select only **Outbound Provisioning**. Click **Next**.

   4. On the **General Info** tab, in the **Partner's Entity ID** and **Connection Name** fields, enter a name of your choosing. Click **Next**.

3. On the **Outbound Provisioning** tab, configure provisioning with the following details.

   For help, see [Configuring outbound provisioning](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_spconnectionconfigtasklet_saasprovisioningstate.html) in the PingFederate documentation.

   1. Click **Configure Provisioning**.

   2. On the **Target** tab, configure the provisioning connector by referring to [PingID Connector settings reference](pf_pid_connector_pid_connector_settings_reference.html). Click **Next**.

   3. On the **Manage Channels** tab, create a channel as shown in [Managing channels](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_saasmanagementtasklet_saasmanagementstate.html) in the PingFederate documentation. Complete the attribute mappings by referring to [Supported attributes reference](pf_pid_connector_supported_attributes_reference.html).

4. On the **Activation and Summary** tab, above the **Summary** section, click the toggle to turn on the connection. Click **Save**.

---

---
title: Deploying the integration files
description: To get started with the integration, deploy the PingID Provisioner files to your PingFederate directory.
component: pingid
page_id: pingid:setup:pf_pid_connector_deploying_the_integration_files
canonical_url: https://docs.pingidentity.com/integrations/pingid/setup/pf_pid_connector_deploying_the_integration_files.html
revdate: June 19, 2024
section_ids:
  steps: Steps
---

# Deploying the integration files

To get started with the integration, deploy the PingID Provisioner files to your PingFederate directory.

## Steps

1. Download the PingID Provisioner `.zip` archive from the [**Add-ons** tab of the PingFederate downloads page](https://www.pingidentity.com/en/resources/downloads/pingfederate.html) or the [Ping Identity Marketplace](https://marketplace.pingone.com/item/pingid-provisioner).

2. Stop PingFederate.

3. If you're upgrading an existing deployment, delete the `pf-pingid-quickconnection-<version>.jar` file from your `<pf_install>/pingfederate/server/default/deploy` directory.

4. Extract the `.zip` archive and merge the contents of the `dist` directory with your `<pf_install>/pingfederate/server/default/deploy` directory.

5. Enable the PingFederate provisioning engine:

   1. Open your `<pf_install>/pingfederate/bin/run.properties` file.

   2. Change `pf.provisioner.mode` to `STANDALONE`. Save the file.

      |   |                                                                                                                                                                                                                                        |
      | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      |   | To configure the `FAILOVER` mode instead, see [Deploying provisioning failover](https://docs.pingidentity.com/pingfederate/latest/server_clustering_guide/pf_deploy_provis_failover.html) in the PingFederate Server Clustering Guide. |

6. Start PingFederate.

7. If you operate PingFederate in a cluster, repeat steps 2 - 4 and step 6 for each engine node.

---

---
title: Device management
description: As part of the provisioning process, the PingID Provisioner can add and update the authentication devices associated with each user in PingID.
component: pingid
page_id: pingid::pf_pid_connector_device_management
canonical_url: https://docs.pingidentity.com/integrations/pingid/pf_pid_connector_device_management.html
revdate: June 19, 2024
section_ids:
  nicknames: Nicknames
  mapping-attributes-to-nicknames: Mapping attributes to nicknames
  device-management: Device management
  primary-devices: Primary devices
---

# Device management

As part of the provisioning process, the PingID Provisioner can add and update the authentication devices associated with each user in PingID.

For general information about devices, see [PingID authentication for the web](https://docs.pingidentity.com/pingid-user-guide/secure_authentication_with_pingid/pid_ug_authentication_for_the_web.html) and [Managing your devices](https://docs.pingidentity.com/pingid-user-guide/managing_your_devices/pid_manage_your_devices.html) in the PingID documentation.

## Nicknames

PingID assigns nicknames to authentication devices. These nicknames appear in the user interface, such as on the device management page. The PingID Provisioner also uses nicknames to identify the devices it manages.

The following are the "managed" nicknames used by the provisioning connector:

* `Email 1`

* `Email 2`

* `Email 3`

* `SMS Number 1`

* `SMS Number 2`

* `SMS Number 3`

* `Voice Number 1`

* `Voice Number 2`

* `Voice Number 3`

The connector can only manage these nine devices.

## Mapping attributes to nicknames

Each of the managed devices can be populated by a matching user attribute on the **Attribute Mapping** tab of the channel configuration. The matching attributes are prefixed with "MFA", such as "MFA SMS Number 1".

You can map these attributes in the [Creating a provisioning connection](setup/pf_pid_connector_creating_a_provisioning_connection.html) part of the setup process.

## Device management

The PingID Provisioner can compare the device values (the email address or phone number) in PingID against the values in the datastore. The datastore is always considered the source of truth when updating the nine managed devices, but you can choose how the connector handles other devices it finds. Alternately, you can turn off device management and use PingID as the source of truth.

You can configure the connector's device management behavior using the **Manage devices** setting in the [Creating a provisioning connection](setup/pf_pid_connector_creating_a_provisioning_connection.html) part of the setup process.

**Manage devices setting**

| Setting                   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| ------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Do not manage devices** | PingFederate doesn't provision or manage any devices in PingID.Users can manage their own devices as shown in [Managing your devices](https://docs.pingidentity.com/pingid-user-guide/managing_your_devices/pid_manage_your_devices.html) in the PingID documentation.                                                                                                                                                                                                                                                                                      |
| **Merge devices**         | PingFederate provisions devices to PingOne for Enterprise using the nine managed nicknames.When updating a user, if there is a conflict between the datastore and PingID for one of the managed devices, the datastore takes precedence. PingFederate removes and re-creates the device in PingID with the new value.&#xA;&#xA;When updating the user's "primary" device, the user has to choose it as their primary device again.The provisioner doesn't change devices with non-managed nicknames, such as devices added by the user or an administrator. |
| **Overwrite devices**     | This behaves the same as **Merge devices**, except the provisioner removes all devices with non-managed nicknames, such as devices added by the user or an administrator.                                                                                                                                                                                                                                                                                                                                                                                   |

## Primary devices

In PingID, each user can have one "primary" device. The user is prompted to authenticate using this device by default.

When creating a new user, the PingID Provisioner can set a primary device automatically. You can customize this behavior with the **Primary Device on Create** setting in the [Creating a provisioning connection](setup/pf_pid_connector_creating_a_provisioning_connection.html) part of the setup process.

When updating existing users, the PingID Provisioner doesn't set or change the primary device.

**Primary Device on Create**

| Setting                | Description                                                                           |
| ---------------------- | ------------------------------------------------------------------------------------- |
| **Do not manage**      | PingID Provisioner can provision devices, but it doesn't set a primary device.        |
| **MFA Email 1**        | PingID Provisioner sets `Email 1` as the user's primary authentication device.        |
| **MFA SMS Number 1**   | PingID Provisioner sets `SMS Number 1` as the user's primary authentication device.   |
| **MFA Voice Number 1** | PingID Provisioner sets `Voice Number 1` as the user's primary authentication device. |

---

---
title: Download manifest
description: The following files are included in the PingID Provisioner .zip archive:
component: pingid
page_id: pingid:release_notes:pf_pid_connector_download_manifest
canonical_url: https://docs.pingidentity.com/integrations/pingid/release_notes/pf_pid_connector_download_manifest.html
revdate: June 18, 2024
---

# Download manifest

The following files are included in the PingID Provisioner `.zip` archive:

* `ReadMeFirst.pdf` – contains links to this online documentation

* `Legal.pdf` – copyright and license information

* `dist` – contains the integration files

  * `deploy/pf-pingid-quickconnection-<version>.jar` – The PingID Provisioner quick connection template.

---

---
title: Enabling provisioning in PingFederate
description: To use PingFederate for provisioning, configure an external datastore.
component: pingid
page_id: pingid:setup:pf_pid_connector_enabling_provisioning_in_pf
canonical_url: https://docs.pingidentity.com/integrations/pingid/setup/pf_pid_connector_enabling_provisioning_in_pf.html
revdate: June 19, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
  choose-from: Choose from:
---

# Enabling provisioning in PingFederate

To use PingFederate for provisioning, configure an external datastore.

## About this task

Your external datastore acts as the source of data for provisioning. PingFederate also uses an internal datastore to store the state of synchronization between the source datastore and the target datastore.

For more information, see [Datastores](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_datastores.html) in the PingFederate documentation.

## Steps

1. Configure the datastore for PingFederate to use as the source of user data.

   For instructions, see [Datastores](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_datastores.html) in the PingFederate documentation.

   |   |                                                                                                                                                                                                                                                                                       |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | When targeting users and groups for provisioning, exclude the user account that you will use to administer users in your connection to PingOne for Enterprise. This prevents the PingFederate provisioning engine from interfering with the account that provisions users and groups. |

2. Do one of the following:

   ### Choose from:

   * For PingFederate 10.1 or later: Go to **System > Server > Protocol Settings**.

   * For PingFederate 10.0 or earlier: Enable the identity provider (IdP) and outbound provisioning roles:

     1. Go to **System > Protocol Settings > Roles & Protocols**.

     2. Select **Enable Identity Provider IdP Role and Support the Following**.

     3. Select **Outbound Provisioning**. Click **Next**.

3. On the **Outbound Provisioning** tab, select the PingFederate internal datastore. Click **Save**.

   For help, see [Configuring outbound provisioning settings](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_protocolsettingstasklet_saasglobalprovisioningsettingsstate.html) in the PingFederate documentation.

---

---
title: Get your PingID settings file
description: Download your PingID settings file to make it easier to set up your service provider connection.
component: pingid
page_id: pingid:setup:pf_pid_connector_get_your_pid_settings_file
canonical_url: https://docs.pingidentity.com/integrations/pingid/setup/pf_pid_connector_get_your_pid_settings_file.html
revdate: June 19, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Get your PingID settings file

Download your PingID settings file to make it easier to set up your service provider connection.

## About this task

For more information, see the **PingID Properties File** section of the [PingID API overview](https://apidocs.pingidentity.com/pingid-api/guide/pingid-api/pid_c_PingIDapiOverview/#The-PingID-Properties-File) in the PingID API documentation.

## Steps

1. Sign on to the PingOne for Enterprise administrative console and open the PingID dashboard.

2. Go to **Setup > PingID**.

3. On the **Client Integration** tab, in the **Integrate with PingFederate** section, click **Download**, then save the `pingid.properties` file.

   |   |                                                                                                                          |
   | - | ------------------------------------------------------------------------------------------------------------------------ |
   |   | You will use this file in [PingID Connector settings reference](pf_pid_connector_pid_connector_settings_reference.html). |

---

---
title: Known issues and limitations
description: The following are known issues or limitations with the PingID Provisioner.
component: pingid
page_id: pingid:release_notes:pf_pid_connector_known_issues_and_limitations
canonical_url: https://docs.pingidentity.com/integrations/pingid/release_notes/pf_pid_connector_known_issues_and_limitations.html
revdate: August 1, 2024
section_ids:
  known-issues: Known issues
  known-limitations: Known limitations
---

# Known issues and limitations

The following are known issues or limitations with the PingID Provisioner.

## Known issues

There are no known issues.

## Known limitations

* When an LDAP user is deleted in a targeted group distinguished name (DN), the provisioning connector does not propagate the deletion until a new user is added to the group. This limitation is compounded when the **User Create** provisioning option is disabled. For solutions, see [SaaS provisioner does not remove the user](https://support.pingidentity.com/s/article/After-deleting-an-AD-user-account-SaaS-provisioner-does-not-remove-the-user-in-the-next-provisioning-cycle-when-Group-DN-is-specified) in the Knowledge Base.

* Due to PingFederate limitations, user attributes cannot be cleared once set.

* Due to a limitation in the PingID API, changes made to the user's username are not reflected in the PingOne WebPortal.

---

---
title: PingID Connector settings reference
description: Field descriptions for the PingID Provisioner configuration.
component: pingid
page_id: pingid:setup:pf_pid_connector_pid_connector_settings_reference
canonical_url: https://docs.pingidentity.com/integrations/pingid/setup/pf_pid_connector_pid_connector_settings_reference.html
revdate: June 18, 2024
---

# PingID Connector settings reference

Field descriptions for the PingID Provisioner configuration.

**Provisioning connector settings reference**

| Field                                                                                                                                                             | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **PingID Properties**                                                                                                                                             | For PingFederate 10.2 and later.Upload the `pingid.properties` file that you downloaded in [Get your PingID settings file](pf_pid_connector_get_your_pid_settings_file.html).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| **Manage Devices**                                                                                                                                                | Determines how the connector manages devices (authentication methods) in PingID.For more detail, see [Device management](../pf_pid_connector_device_management.html).- Do not manage devices

  PingFederate doesn't provision or manage any devices in PingID.

- Merge devices

  If there is a conflict between the datastore and PingID for one of the managed devices, the datastore takes precedence.

  &#xA;&#xA;When updating the user's "primary" device, the user has to choose it as their primary device again.

  The provisioner doesn't change devices with non-managed nicknames, such as devices added by the user or an administrator.

- Overwrite devices

  This behaves the same as **Merge devices**, except the provisioner removes all devices with non-managed nicknames, such as devices added by the user or an administrator. |
| **Primary Device on Create**                                                                                                                                      | Determines which device (authentication method) the connector sets as the primary when provisioning a new user to PingID.For more detail, see [Device management](../pf_pid_connector_device_management.html).- Do not manage

  PingFederate provisions devices but doesn't set any as the primary device.

- MFA Email 1

  Sets `Email 1` as the primary device.

- MFA SMS Number 1

  Sets `Number 1` as the primary device.

- MFA Voice Number 1

  Sets `Voice Number 1` as the primary device.                                                                                                                                                                                                                                                                                                                                                     |
| **Provisioning Options**                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| **User Create**                                                                                                                                                   | **Selected** (default) – PingFederate creates users in PingID.**Cleared** – PingFederate does not create users in PingID.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| **User Update**                                                                                                                                                   | **Selected** (default) – PingFederate updates existing users in PingID.**Cleared** – PingFederate does not update existing users in PingID.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| **User Disable / Delete**                                                                                                                                         | **Selected** (default) – PingFederate disables or deletes users in PingID.&#xA;&#xA;PingFederate can only re-enable a user if User Update is selected.**Cleared** – PingFederate does not disable or delete users in PingID.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| **Provision Disabled Users**                                                                                                                                      | This option applies when:- The **User Create** option is selected, and

- The provisioning engine targets a user in the datastore that has a "disabled" status.**Selected** (default) – PingFederate creates the user in PingID with a "disabled" status.**Cleared** – PingFederate does not create the user in PingID.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| &#xA;&#xA;If any of the Provision Options are cleared, PingFederate logs a warning in the user workflow section of provisioner.log when the related action fails. |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| **Remove User Action**                                                                                                                                            | This option applies when:- **User Disable / Delete** is selected, and

- a previously-provisioned user no longer meets the condition set on the **Source Location** screen, or

- a user has been disabled or deleted from the data store.**Disable** (default): PingFederate disables the user in PingID.**Delete**: PingFederate deletes the user from PingID.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |

---

---
title: PingID Provisioner
description: The PingID Provisioner allows PingFederate to integrate with PingID for user provisioning.
component: pingid
page_id: pingid::pf_pid_connector
canonical_url: https://docs.pingidentity.com/integrations/pingid/pf_pid_connector.html
revdate: February 10, 2026
section_ids:
  features: Features
  intended-audience: Intended audience
  system-requirements: System requirements
---

# PingID Provisioner

The PingID Provisioner allows PingFederate to integrate with PingID for user provisioning.

|   |                                                                                                                                                                                                                                                                                                                                                                                                 |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | If you're using PingID from PingOne, you must switch to the PingOne provisioner. The PingID Provisioner isn't supported in PingOne.Learn more in [Provisioning](https://docs.pingidentity.com/pingone/integrations/p1_provisioning.html) and [PingFederate](https://docs.pingidentity.com/pingone/integrations/p1_pf_connection.html) in the Integrations section of the PingOne documentation. |

## Features

* Manages users in PingID based on changes in an external data store that is attached to PingFederate

  * Creates, updates, disables, and deletes users

  * Allows you to enable the create, update, disable, and delete capabilities independently

  * Allows you to choose whether to disable or delete users when deprovisioning

  * Allows you to provision disabled users

* Manages users' devices (authentication methods) in PingID

  * Enrolls and manages up to nine devices

  * Allows you to set the management behavior

  * Allows you to set a primary authentication device

## Intended audience

This document is intended for PingFederate administrators.

If you need help during the setup process, see the following resources:

* PingFederate documentation:

  * [SP connection management](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_sp_connect_management.html)

  * [Managing digital signing certificates and decryption keys](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_certmanagementtasklet_dsigsigningcert_certmanagementstate.html)

  * [Datastores](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_datastores.html)

  * [Configuring outbound provisioning](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_spconnectionconfigtasklet_saasprovisioningstate.html)

  * [Configuring outbound provisioning settings](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_protocolsettingstasklet_saasglobalprovisioningsettingsstate.html)

* PingID documentation:

  * [PingID Administration Guide](https://docs.pingidentity.com/pingid/pid_landing_page.html)

  * [Automatically update and remove PingID users](https://docs.pingidentity.com/pingid/pingid_user_life_cycle_management/pid_automatically_update_remove_pid_users.html)

## System requirements

* PingFederate 9.0 or later

* To allow PingFederate to make outbound connections, you might need to allow the one of the following endpoints in your firewall:

  * North America: idpxnyl3m.pingidentity.com

  * Europe: idpxnyl3m.pingidentity.eu

  * Australia: idpxnyl3m.pingidentity.com.au

---

---
title: Supported attributes reference
description: The following attributes can be mapped for user provisioning to PingID.
component: pingid
page_id: pingid:setup:pf_pid_connector_supported_attributes_reference
canonical_url: https://docs.pingidentity.com/integrations/pingid/setup/pf_pid_connector_supported_attributes_reference.html
revdate: June 18, 2024
---

# Supported attributes reference

The following attributes can be mapped for user provisioning to PingID.

For general information about attributes, see the **AddUser** section of [PingID User Management API](https://apidocs.pingidentity.com/pingid-api/guide/pingid-api/pid_c_PingIDapiUserManagement/#AddUser) in the PingID API documentation.

| Attribute            | Description                                                                                                                                                                                                                                         |
| -------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `Username`           | The unique identifier for the user in PingID. A username cannot be updated. This attribute is required.                                                                                                                                             |
| `Email`              | The email for the user (for example, "bjensen\@example.com").                                                                                                                                                                                       |
| `First Name`         | The given name of the user, or first name in most Western languages (for example, 'Barbara' given the full name 'Ms. Barbara Jane Jensen, III').                                                                                                    |
| `Last Name`          | The family name of the user, or last name in most Western languages (for example, 'Jensen' given the full name 'Ms. Barbara Jane Jensen, III').                                                                                                     |
| `MFA Email 1`        | An email address to use as an authentication device.                                                                                                                                                                                                |
| `MFA Email 2`        | An email address to use as an authentication device.                                                                                                                                                                                                |
| `MFA Email 3`        | An email address to use as an authentication device.                                                                                                                                                                                                |
| `MFA SMS Number 1`   | A phone number to use as an SMS authentication device.For detailed requirements, see [SMS and voice authentication](https://docs.pingidentity.com/pingid/pingid_service_management/pid_sms_voice_authentication.html) in the PingID documentation.  |
| `MFA SMS Number 2`   | A phone number to use as an SMS authentication device.                                                                                                                                                                                              |
| `MFA SMS Number 3`   | A phone number to use as an SMS authentication device.                                                                                                                                                                                              |
| `MFA Voice Number 1` | A phone number to use as a voice authentication device.For detailed requirements, see [SMS and voice authentication](https://docs.pingidentity.com/pingid/pingid_service_management/pid_sms_voice_authentication.html) in the PingID documentation. |
| `MFA Voice Number 2` | A phone number to use as a voice authentication device.                                                                                                                                                                                             |
| `MFA Voice Number 3` | A phone number to use as a voice authentication device.                                                                                                                                                                                             |

---

---
title: Upgrading an existing deployment
description: If you are upgrading from a previous version of the PingID Provisioner, note your existing service provider (SP) connection configuration and create a new connection.
component: pingid
page_id: pingid:setup:pf_pid_connector_upgrading_an_existing_deployment
canonical_url: https://docs.pingidentity.com/integrations/pingid/setup/pf_pid_connector_upgrading_an_existing_deployment.html
revdate: June 19, 2024
section_ids:
  steps: Steps
  choose-from: Choose from:
  choose-from-2: Choose from:
---

# Upgrading an existing deployment

If you are upgrading from a previous version of the PingID Provisioner, note your existing service provider (SP) connection configuration and create a new connection.

## Steps

1. Back up your current PingFederate configuration as shown in [Configuration archive](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_configurationarchivetasklet_selectimportexportstate.html) in the PingFederate documentation.

2. In the PingFederate administrative console, open your existing SP connection

   ### Choose from:

   * For PingFederate 10.1 or later: go to **Applications > Integration > SP Connections** and select your connection.

   * For PingFederate 10.0 or earlier: go to **Identity Provider > SP Connections** and select your connection.

3. Note the attribute mappings for your existing SP connection. For help, see [Mapping attributes](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_saaschanneltasklet_saasattrmappingmgmtstate.html) in the PingFederate documentation.

4. Delete your existing SP connection.

   ### Choose from:

   * For PingFederate 10.1 or later:

     1. Go to **Applications > Integration > SP Connections**.

     2. For your existing connection, click **Select action**, and then click **Delete**. Click **Confirm.**

   * For PingFederate 10.0 or earlier:

     1. Go to **Identity Provider > SP Connections > Manage All**.

     2. For your existing connection, click **Select action**, and then click **Delete**. Click **Save.**

5. Complete the steps in [Deploying the integration files](pf_pid_connector_deploying_the_integration_files.html).

6. Complete the steps in [Creating a provisioning connection](pf_pid_connector_creating_a_provisioning_connection.html).

   * From **Outbound Provisioning > Manage Channels > Channel**, on the **Attribute Mapping** tab, configure the attribute mappings based on your notes.

---

---
title: User management
description: The PingID Provisioner synchronizes users from your datastore to PingOne for Enterprise. The following describes the behavior of each provisioning capability.
component: pingid
page_id: pingid::pf_pid_connector_user_management
canonical_url: https://docs.pingidentity.com/integrations/pingid/pf_pid_connector_user_management.html
revdate: June 19, 2024
section_ids:
  synchronizing-existing-users: Synchronizing existing users
  user-provisioning: User provisioning
  user-updates: User updates
  user-deprovisioning: User deprovisioning
---

# User management

The PingID Provisioner synchronizes users from your datastore to PingOne for Enterprise. The following describes the behavior of each provisioning capability.

|   |                                                                                                                                                                                                                                       |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | You can configure the following capabilities and specify which users to provision when you get to the [Creating a provisioning connection](setup/pf_pid_connector_creating_a_provisioning_connection.html) part of the setup process. |

## Synchronizing existing users

PingFederate synchronizes users based on the `username` attribute in PingOne for Enterprise. If a user already exists in your datastore and PingOne for Enterprise, mapping this attribute correctly links the two records together.

For example:

* In PingOne for Enterprise, Janet's `username` is `jsmith`.

* In your datastore, Janet's `sAMAccountName` is `jsmith`.

* On the **Attribute Mapping** tab of your provisioning connection configuration, map the `username` attribute to `sAMAccountName`.

* When the provisioning connector runs, the datastore user is provisioned with a `username` of `jsmith`. That matches Janet's existing `username` in PingOne for Enterprise, so her information in the datastore is synchronized to her PingOne for Enterprise account.

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