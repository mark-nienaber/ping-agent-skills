---
title: Aquera Connector settings reference
description: Lists the configuration settings and provisioning options for the Aquera Provisioner.
component: aquera
page_id: aquera:setup:pf_aquera_connector_aquera_connector_settings_reference
canonical_url: https://docs.pingidentity.com/integrations/aquera/setup/pf_aquera_connector_aquera_connector_settings_reference.html
revdate: June 27, 2024
---

# Aquera Connector settings reference

Lists the configuration settings and provisioning options for the Aquera Provisioner.

| Field Name                                                                                                                                                                 | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **SCIM URL**                                                                                                                                                               | The SCIM URL that you noted in [Add an application in Aquera](pf_aquera_connector_add_an_application_in_aquera.html).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Bearer Token Authentication                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| **Access Token**                                                                                                                                                           | The bearer token for the target service.If you noted a bearer token in [Add an application in Aquera](pf_aquera_connector_add_an_application_in_aquera.html), enter it here.                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Basic Authentication                                                                                                                                                       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| **Basic Authentication Username**                                                                                                                                          | The username of the administrator account on the target service.If you noted a username in [Add an application in Aquera](pf_aquera_connector_add_an_application_in_aquera.html), enter it here.                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| **Basic Authentication Password**                                                                                                                                          | The password of the administrator account on the target service.If you noted password in [Add an application in Aquera](pf_aquera_connector_add_an_application_in_aquera.html), enter it here.                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Provisioning Options&#xA;&#xA;Some Aquera apps do not support all of the following provisioning options. Check the documentation for the target service.                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| **User Create**                                                                                                                                                            | * Selected (default)

  PingFederate creates users in the target service.

* Cleared

  PingFederate does not create users in the target service.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| **User Update**                                                                                                                                                            | - Selected (default)

  PingFederate updates existing users in the target service.

- Cleared

  PingFederate does not update existing users in the target service.                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| **User Disable / Delete**                                                                                                                                                  | * Selected (default)

  PingFederate removes users from the target service according to the **Remove User Action** setting.&#xA;&#xA;You might need to enable User Update for this to work with some services.* Cleared

  PingFederate does not remove users from the target service.                                                                                                                                                                                                                                                                                                                                              |
| **Provision Disabled Users**                                                                                                                                               | - Selected

  PingFederate creates users in the target service with a "disabled" status.

- Cleared (default)

  If a user has a "disabled" status, PingFederate does not create the user in the target service.                                                                                                                                                                                                                                                                                                                                                                                                                    |
| &#xA;&#xA;If any of the above provisioning options are cleared, PingFederate logs a warning in the user workflow section of provisioner.log when the related action fails. |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| **Remove User Action**                                                                                                                                                     | This option applies when **User Disable / Delete** is selected, and either:* a previously-provisioned user no longer meets the condition set on the **Source Location** tab, or

* a user has been disabled or deleted from the data store.- Disable (default)

  PingFederate disables the user in the target service.

- Delete

  PingFederate deletes the user from the target service.&#xA;&#xA;Some target applications do not support hard deleting users through external interfaces. For those services, users are disabled.	&#xA;&#xA;Some Aquera apps also include a deleteOnDeactivation setting on the Aquera console. |

---

---
title: Aquera Provisioner
description: The Aquera Provisioner allows PingFederate to integrate with any application supported by Aquera for user provisioning and single sign-on (SSO).
component: aquera
page_id: aquera::pf_aquera_connector
canonical_url: https://docs.pingidentity.com/integrations/aquera/pf_aquera_connector.html
revdate: June 27, 2024
section_ids:
  features: Features
  intended-audience: Intended audience
  system-requirements: System requirements
---

# Aquera Provisioner

The Aquera Provisioner allows PingFederate to integrate with any application supported by Aquera for user provisioning and single sign-on (SSO).

## Features

* Manages users in the target service based on changes in an external data store that is attached to PingFederate.

  * Creates, updates, disables, and deletes users.

  * Allows you to enable the create, update, disable, and delete capabilities independently.

  * Allows you to choose whether to disable or delete users when deprovisioning.

  * Allows you to provision disabled users.

* Manages groups in the target service based on changes in an external data store that is attached to PingFederate.

  * Creates, updates, and deletes groups.

  * Updates group memberships.

* Enables browser-based SSO initiated by the service provider (SP) or identity provider (IdP).

The Aquera Provisioner implements the official SCIM specifications provided from [simplecloud.info](http://www.simplecloud.info/). The following table provides a brief summary.

| Feature                        | Outbound provisioning                                                                                                           |
| ------------------------------ | ------------------------------------------------------------------------------------------------------------------------------- |
| SCIM specification             | Step 2.0                                                                                                                        |
| Data format                    | JSON                                                                                                                            |
| User and group CRUD operations | Yes                                                                                                                             |
| Custom schema support          | Yes. The connector retrieves the target service schema from Aquera.                                                             |
| Filtering support              | Users: YesGroups: Yes, if the target service supports it. Otherwise, the connector attempts to get all groups and find a match. |
| PATCH                          | Users: NoGroups: Yes                                                                                                            |
| Authentication method          | Basic authentication and bearer token authentication                                                                            |
| Source data stores             | Active Directory and other LDAPv3-compliant directory servers                                                                   |

Attribute support varies by target service. The Aquera Provisioner dynamically gets attributes from Aquera for each target service.

## Intended audience

This document is intended for PingFederate administrators.

Learn more about the setup process from the following resources:

* PingFederate documentation:

  * [SP connection management](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_sp_connect_management.html)

  * [Identity provider SSO configuration](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_ident_provid_sso_config.html)

  * [Managing digital signing certificates and decryption keys](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_certmanagementtasklet_dsigsigningcert_certmanagementstate.html)

  * [Datastores](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_datastores.html)

  * [Configuring outbound provisioning](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_spconnectionconfigtasklet_saasprovisioningstate.html)

  * [Configuring outbound provisioning settings](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_protocolsettingstasklet_saasglobalprovisioningsettingsstate.html)

* Aquera documentation:

  * [Aquera User Guide](https://support.aquera.com/hc/en-us/articles/360056052093-Aquera-User-Guide)

  * [Connectors](https://support.aquera.com/hc/en-us/categories/115000284613-Connectors) documentation for the target service

## System requirements

* PingFederate 9.0 or later.

* To allow PingFederate to make outbound connections, you might need to allow the following Aquera endpoint (use your tenant ID):

  * http\://api.aquera.com/Tenants/:*tenantid*

---

---
title: Changelog
description: The following is the change history for the Aquera Provisioner.
component: aquera
page_id: aquera:release_notes:pf_aquera_connector_changelog
canonical_url: https://docs.pingidentity.com/integrations/aquera/release_notes/pf_aquera_connector_changelog.html
revdate: June 27, 2024
---

# Changelog

The following is the change history for the Aquera Provisioner.

**Aquera Provisioner 1.0 – December 2020**

* Initial release.

* Included support for user provisioning.

* Included support for group provisioning.

* Included support for adding users to groups.

* Included support for SCIM core and enterprise attributes.

* Included support for dynamic attribute retrieval of custom attributes.

* Included support for bearer token and HTTP basic authentication.

* Included configuration options for CRUD capabilities.

* Included configuration options for provisioning disabled users.

* Included configuration options for deprovisioning actions.

---

---
title: Configuring single sign-on
description: To allow PingFederate to act as an identity provider for the target service, modify your connection to include single sign-on (SSO).
component: aquera
page_id: aquera:setup:pf_aquera_connector_configuring_single_sign_on
canonical_url: https://docs.pingidentity.com/integrations/aquera/setup/pf_aquera_connector_configuring_single_sign_on.html
revdate: June 27, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Configuring single sign-on

To allow PingFederate to act as an identity provider for the target service, modify your connection to include single sign-on (SSO).

## About this task

|   |                                                                                                                          |
| - | ------------------------------------------------------------------------------------------------------------------------ |
|   | SSO is not required for provisioning. If you only want to use the Aquera Provisioner for provisioning, skip these steps. |

## Steps

1. Complete the steps in [Adding SSO to a connection](pf_aquera_connector_adding_sso_to_a_connection.html).

2. On the target service, configure single sign-on by following the documentation provided by the service. When prompted for information about PingFederate, see [PingFederate SSO details for the service provider](pf_aquera_connector_pf_sso_details_for_the_service_provider.html).

---

---
title: Creating a provisioning connection
description: To allow PingFederate to manage users in the target service, create a service provider (SP) connection.
component: aquera
page_id: aquera:setup:pf_aquera_connector_creating_a_provisioning_connection
canonical_url: https://docs.pingidentity.com/integrations/aquera/setup/pf_aquera_connector_creating_a_provisioning_connection.html
revdate: June 27, 2024
section_ids:
  steps: Steps
  choose-from: Choose from:
---

# Creating a provisioning connection

To allow PingFederate to manage users in the target service, create a service provider (SP) connection.

## Steps

1. In the PingFederate administrator console, create a new SP connection:

   ### Choose from:

   * For PingFederate 10.1 or later: go to **Applications > Integration > SP Connections**. Click **Create Connection**.

   * For PingFederate 10.0 or earlier: go to **Identity Provider > SP Connections**. Click **Create Connection**.

2. Configure the basic connection details with the the target service quick connection template.

   1. On the **Connection Template** tab, select **Use a template for this connection**.

   2. From the **Connection Template** list, select **Aquera Provisioner**. Click **Next**.

   3. On the **Connection Type** tab select **Outbound Provisioning**. Click **Next**.

   4. On the **General Info** tab, in the **Connection Name** field, enter a name of your choosing. Click **Next**.

3. On the **Outbound Provisioning** tab, configure provisioning with the following details.

   Learn more in [Configuring outbound provisioning](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_spconnectionconfigtasklet_saasprovisioningstate.html) in the PingFederate documentation.

   1. On the **Target** page, enter the URL and authentication details that you noted in [Add an application in Aquera](pf_aquera_connector_add_an_application_in_aquera.html).

      |   |                                                                                                   |
      | - | ------------------------------------------------------------------------------------------------- |
      |   | PingFederate verifies the authentication details when you activate the channel and SP connection. |

   2. Under **Provisioning Options**, customize the provisioning connector behavior by referring to [Aquera Connector settings reference](pf_aquera_connector_aquera_connector_settings_reference.html). Click **Next**.

   3. On the **Manage Channels > Attribute Mapping** tab, at the end of the page, click **Refresh Fields**. Complete the required (`*`) attribute mappings and any optional mappings that you want.

      The **Refresh Fields** button causes PingFederate to get the attribute schema from the target service. The schema can include custom attributes (marked with `IANUser`) and standard SCIM attributes. Learn more about standard SCIM attributes in [Supported attributes reference](pf_aquera_connector_supported_attributes_reference.html).

      Learn about mapping attributes in [Managing channels](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_saasmanagementtasklet_saasmanagementstate.html) in the PingFederate documentation.

4. On the **Activation and Summary** tab, above the **Summary** section, click the toggle to turn on the connection. Click **Save**.

---

---
title: Deploying the integration files
description: To get started with the integration, deploy the Aquera Provisioner files to your PingFederate directory.
component: aquera
page_id: aquera:setup:pf_aquera_connector_deploying_the_integration_files
canonical_url: https://docs.pingidentity.com/integrations/aquera/setup/pf_aquera_connector_deploying_the_integration_files.html
revdate: June 27, 2024
section_ids:
  steps: Steps
---

# Deploying the integration files

To get started with the integration, deploy the Aquera Provisioner files to your PingFederate directory.

## Steps

1. Download the Aquera Provisioner `.zip` archive from the [**Add-ons** tab of the PingFederate downloads page](https://www.pingidentity.com/en/resources/downloads/pingfederate.html) or the [Ping Identity Marketplace](https://marketplace.pingone.com/item/aquera-provisioner).

2. Stop PingFederate.

3. If you're upgrading an existing deployment, delete the `pf-aquera-quickconnection-<version>.jar` file from your `<pf_install>/pingfederate/server/default/deploy` directory.

4. Extract the `.zip` archive and merge the contents of the `dist` directory with your `<pf_install>/pingfederate/server/default/deploy` directory.

5. Enable the PingFederate provisioning engine:

   1. Open your `<pf_install>/pingfederate/bin/run.properties` file.

   2. Change `pf.provisioner.mode` to `STANDALONE`. Save the file.

      |   |                                                                                                                                                                                                                                                      |
      | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      |   | Learn more about configuring the `FAILOVER` mode instead in [Deploying provisioning failover](https://docs.pingidentity.com/pingfederate/latest/server_clustering_guide/pf_deploy_provis_failover.html) in the PingFederate Server Clustering Guide. |

6. Start PingFederate.

7. If you operate PingFederate in a cluster, repeat steps 2 - 4 and step 6 for each engine node.

---

---
title: Download manifest
description: The following files are included in the Aquera Provisioner .zip archive:
component: aquera
page_id: aquera:release_notes:pf_aquera_connector_download_manifest
canonical_url: https://docs.pingidentity.com/integrations/aquera/release_notes/pf_aquera_connector_download_manifest.html
revdate: June 27, 2024
---

# Download manifest

The following files are included in the Aquera Provisioner `.zip` archive:

* `ReadMeFirst.pdf`: Contains links to this online documentation

* `Legal.pdf`: Copyright and license information

* `dist`: Contains the integration files

  * `deploy/pf-aquera-quickconnection-<version>.jar`: The Aquera Provisioner quick connection template.

---

---
title: Enabling provisioning and single sign-on in PingFederate 10.0 or earlier
description: In the PingFederate administrative console, configure the datastore for PingFederate to use as the source of user data.
component: aquera
page_id: aquera:setup:pf_aquera_connector_enabling_provisioning_and_single_sign_on_in_pf_100_or_earlier
canonical_url: https://docs.pingidentity.com/integrations/aquera/setup/pf_aquera_connector_enabling_provisioning_and_single_sign_on_in_pf_100_or_earlier.html
revdate: June 27, 2024
section_ids:
  steps: Steps
---

# Enabling provisioning and single sign-on in PingFederate 10.0 or earlier

## Steps

1. In the PingFederate administrative console, configure the datastore for PingFederate to use as the source of user data.

   For help, see [Datastores](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_datastores.html) in the PingFederate documentation.

2. Go to **System > Protocol Settings > Roles & Protocols**.

3. Select the **Enable Identity Provider IdP Role and Support the Following** checkbox.

4. Select the **SAML 2.0** and **Outbound Provisioning** checkboxes. Click **Next**.

5. Click the **Federation Info** tab.

6. In the **SAML 2.0 Entity ID** field, enter a name for PingFederate to use to identify itself to SAML partners.

7. On the **Outbound Provisioning** tab, in the **Provisioner Data Store** list, select the internal database that will store the synchronization state. Click **Save**.

   Learn more in [Configuring outbound provisioning settings](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_protocolsettingstasklet_saasglobalprovisioningsettingsstate.html) in the PingFederate documentation.

---

---
title: Enabling provisioning and single sign-on in PingFederate 10.1 or later
description: In the PingFederate administrative console, configure the datastore for PingFederate to use as the source of user data.
component: aquera
page_id: aquera:setup:pf_aquera_connector_enabling_provisioning_and_single_sign_on_in_pf_101_or_later
canonical_url: https://docs.pingidentity.com/integrations/aquera/setup/pf_aquera_connector_enabling_provisioning_and_single_sign_on_in_pf_101_or_later.html
revdate: June 27, 2024
section_ids:
  steps: Steps
---

# Enabling provisioning and single sign-on in PingFederate 10.1 or later

## Steps

1. In the PingFederate administrative console, configure the datastore for PingFederate to use as the source of user data.

   Learn more in [Datastores](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_datastores.html) in the PingFederate documentation.

2. Go to **System > Server > Protocol Settings > Federation Info**.

3. In the **SAML 2.0 Entity ID** field, enter a name for PingFederate to use when identifying itself to SAML partners.

4. On the **Outbound Provisioning** tab, in the **Provisioner Data Store** list, select the internal database that will store the synchronization state. Click **Save**.

   Learn more in [Configuring outbound provisioning settings](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_protocolsettingstasklet_saasglobalprovisioningsettingsstate.html) in the PingFederate documentation.

---

---
title: Enabling single sign-on in PingFederate
description: To use PingFederate for provisioning and single sign-on, configure an external datastore and set a SAML entity ID.
component: aquera
page_id: aquera:setup:pf_aquera_connector_enabling_provisioning_and_single_sign_on_in_pf
canonical_url: https://docs.pingidentity.com/integrations/aquera/setup/pf_aquera_connector_enabling_provisioning_and_single_sign_on_in_pf.html
revdate: June 27, 2024
section_ids:
  about-this-task: About this task
  enabling-provisioning-and-single-sign-on-in-pingfederate-10-1-or-later: Enabling provisioning and single sign-on in PingFederate 10.1 or later
  steps: Steps
  enabling-provisioning-and-single-sign-on-in-pingfederate-10-0-or-earlier: Enabling provisioning and single sign-on in PingFederate 10.0 or earlier
  steps-2: Steps
---

# Enabling single sign-on in PingFederate

To use PingFederate for provisioning and single sign-on, configure an external datastore and set a SAML entity ID.

## About this task

Your external datastore acts as the source of data for provisioning. PingFederate also uses an internal datastore to store the state of synchronization between the source datastore and the target datastore.

Learn more in [Datastores](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_datastores.html) and [Configuring outbound provisioning settings](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_protocolsettingstasklet_saasglobalprovisioningsettingsstate.html) in the PingFederate documentation.

## Enabling provisioning and single sign-on in PingFederate 10.1 or later

### Steps

1. In the PingFederate administrative console, configure the datastore for PingFederate to use as the source of user data.

   Learn more in [Datastores](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_datastores.html) in the PingFederate documentation.

2. Go to **System > Server > Protocol Settings > Federation Info**.

3. In the **SAML 2.0 Entity ID** field, enter a name for PingFederate to use when identifying itself to SAML partners.

4. On the **Outbound Provisioning** tab, in the **Provisioner Data Store** list, select the internal database that will store the synchronization state. Click **Save**.

   Learn more in [Configuring outbound provisioning settings](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_protocolsettingstasklet_saasglobalprovisioningsettingsstate.html) in the PingFederate documentation.

## Enabling provisioning and single sign-on in PingFederate 10.0 or earlier

### Steps

1. In the PingFederate administrative console, configure the datastore for PingFederate to use as the source of user data.

   For help, see [Datastores](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_datastores.html) in the PingFederate documentation.

2. Go to **System > Protocol Settings > Roles & Protocols**.

3. Select the **Enable Identity Provider IdP Role and Support the Following** checkbox.

4. Select the **SAML 2.0** and **Outbound Provisioning** checkboxes. Click **Next**.

5. Click the **Federation Info** tab.

6. In the **SAML 2.0 Entity ID** field, enter a name for PingFederate to use to identify itself to SAML partners.

7. On the **Outbound Provisioning** tab, in the **Provisioner Data Store** list, select the internal database that will store the synchronization state. Click **Save**.

   Learn more in [Configuring outbound provisioning settings](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_protocolsettingstasklet_saasglobalprovisioningsettingsstate.html) in the PingFederate documentation.

---

---
title: Known issues and limitations
description: The following are known issues or limitations with the Aquera Provisioner.
component: aquera
page_id: aquera:release_notes:pf_aquera_connector_known_issues_and_limitations
canonical_url: https://docs.pingidentity.com/integrations/aquera/release_notes/pf_aquera_connector_known_issues_and_limitations.html
revdate: June 27, 2024
section_ids:
  known-issues: Known issues
  known-limitations: Known limitations
---

# Known issues and limitations

The following are known issues or limitations with the Aquera Provisioner.

## Known issues

There are no known issues.

## Known limitations

SP connections

* The Unique User Identifier cannot be changed in an SP connection configuration. To change to a different Unique User Identifier, delete the existing connection, restart PingFederate, and then create a connection with the new Unique User Identitier.

* All SP connections with the same target must use the same Unique User Identifier. If multiple SP connections are created for the same target, every subsequent connection will use the Unique User Identifier configured in the first connection that was created.

Attributes

* When mapping attributes, Aquera can return invalid schemas for some services. This can cause unexpected behavior. If you experience issues, confirm the correct schema in the documentation for the target service.

* If the target service does not specify type or primary information on multi-value attributes (email, phone, address), unexpected behavior can occur. During an update, existing attributes on the SaaS may not be removed, and the desired value may not be correctly set as primary.

* The connector cannot clear a user attribute once it has been set.

Other

* This connector does not support PATCH user updates.

* When an LDAP user is deleted in a targeted group distinguished name (DN), the provisioning connector does not propagate the deletion until a new user is added to the group. This limitation is compounded when the **User Create** provisioning option is disabled. Learn more in [SaaS provisioner does not remove the user](https://support.pingidentity.com/s/article/After-deleting-an-AD-user-account-SaaS-provisioner-does-not-remove-the-user-in-the-next-provisioning-cycle-when-Group-DN-is-specified) in the Knowledge Base.

* If the target service interprets or implements the SCIM standards differently, it can result in unexpected behavior.

---

---
title: PingFederate SSO details for the service provider
description: When enabling single sign-on (SSO) in the target service, you will require some or all of the following information from PingFederate.
component: aquera
page_id: aquera:setup:pf_aquera_connector_pf_sso_details_for_the_service_provider
canonical_url: https://docs.pingidentity.com/integrations/aquera/setup/pf_aquera_connector_pf_sso_details_for_the_service_provider.html
revdate: June 27, 2024
section_ids:
  metadata-file: Metadata file
  saml-endpoint: SAML endpoint
  identity-provider-issuer: Identity provider issuer
  signing-certificate: Signing certificate
---

# PingFederate SSO details for the service provider

When enabling single sign-on (SSO) in the target service, you will require some or all of the following information from PingFederate.

## Metadata file

Some target services allow you to import a SAML metadata file that contains some of the information below. Learn more about exporting your metadata file in [Metadata export](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_metadata_export.html) in the PingFederate documentation.

## SAML endpoint

The PingFederate SAML endpoint is:

```
https://<pf_hostname>:<pf_port>/idp/SSO.saml2
```

## Identity provider issuer

This is SAML 2.0 Entity ID from PingFederate, which can be found under the **Server Settings** page. Learn more in [Specifying federation information](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_protocolsettingstasklet_federationinfostate.html).

|   |                                                                                                                                                                                                                 |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | In order to override SAML 2.0 Entity ID on the **Server Settings** page for your SP Connection, navigate to the General Info screen to add a Virtual Server ID. This value will be sent as the SAML Issuer URL. |

## Signing certificate

This is the public signing certificate that PingFederate uses to sign the SAML assertion. Learn more about exporting your certificate in [Managing digital signing certificates and decryption keys](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_certmanagementtasklet_dsigsigningcert_certmanagementstate.html).

---

---
title: Supported attributes reference
description: The following list describes standard SCIM attributes. Attribute support varies by target service. The Aquera Provisioner dynamically gets attributes from Aquera for each target service.
component: aquera
page_id: aquera:setup:pf_aquera_connector_supported_attributes_reference
canonical_url: https://docs.pingidentity.com/integrations/aquera/setup/pf_aquera_connector_supported_attributes_reference.html
revdate: June 27, 2024
---

# Supported attributes reference

The following list describes standard SCIM attributes. Attribute support varies by target service. The Aquera Provisioner dynamically gets attributes from Aquera for each target service.

Learn more about SCIM attributes in the [SCIM specification](https://tools.ietf.org/html/rfc7643#section-4.1.1) and the target service documentation.

| Attribute               | Description                                                                                                                                                                                                                                                                                                                     |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `userName`              | A service provider's unique identifier for the user.This attribute is required.                                                                                                                                                                                                                                                 |
| `givenName`             | The given name of the user, or first name in most Western languages (for example, 'Barbara' given the full name 'Ms. Barbara Jane Jensen, III').                                                                                                                                                                                |
| `familyName`            | The family name of the user, or last name in most Western languages (for example, 'Jensen' given the full name 'Ms. Barbara Jane Jensen, III').                                                                                                                                                                                 |
| `middleName`            | The middle name(s) of the user (for example, "Jane" given the full name "Ms. Barbara Jane Jensen, III").                                                                                                                                                                                                                        |
| `honorificPrefix`       | The honorific prefix(es) of the user, or title in most Western languages (for example, "Ms." given the full name "Ms. Barbara Jane Jensen, III").                                                                                                                                                                               |
| `honorificSuffix`       | The honorific suffix(es) of the user, or suffix in most Western languages (for example, "III" given the full name "Ms. Barbara Jane Jensen, III").                                                                                                                                                                              |
| `formattedName`         | The full name, including all middle names, titles, and suffixes as appropriate, formatted for display (for example, "Ms. Barbara Jane Jensen, III").                                                                                                                                                                            |
| `workEmail`             | Work email for the user (for example, "bjensen\@example.com").                                                                                                                                                                                                                                                                  |
| `displayName`           | The name of the user, suitable for display to end-users.                                                                                                                                                                                                                                                                        |
| `title`                 | The user's title, such as "Vice President".                                                                                                                                                                                                                                                                                     |
| `externalId`            | A string that is an identifier for the resource as defined by the provisioning client.                                                                                                                                                                                                                                          |
| `password`              | This attribute is intended to be used as a means to set, replace, or compare (for example, filter for equality) a password.                                                                                                                                                                                                     |
| `preferredLanguage`     | Indicates the user's preferred written or spoken languages and is generally used for selecting a localized user interface.                                                                                                                                                                                                      |
| `userType`              | Used to identify the relationship between the organization and the user. Typical values used might be "Contractor", "Employee", "Intern", "Temp", "External", and "Unknown", but any value may be used.                                                                                                                         |
| `locale`                | Used to indicate the user's default location for purposes of localizing such items as currency, date time format, or numerical representations.                                                                                                                                                                                 |
| `nickName`              | The casual way to address the user in real life. For example,"Bob" or "Bobby" instead of "Robert".                                                                                                                                                                                                                              |
| `profileUrl`            | A URI that is a uniform resource locator that points to a location representing the user's online profile (for example, a web page).                                                                                                                                                                                            |
| `profilePhotoUrl`       | A URI that is a uniform resource locator that points to the user's profile photo. The resource MUST be a file (for example, a GIF, JPEG, or PNG image file) rather than a web page containing an image.                                                                                                                         |
| `profileThumbnailUrl`   | A URI that is a uniform resource locator that points to the user's profile thumbnail. The resource MUST be a file (for example, a GIF, JPEG, or PNG image file) rather than a web page containing an image.                                                                                                                     |
| `timezone`              | The user's time zone, in IANA Time Zone database format (for example, "America/Los\_Angeles").                                                                                                                                                                                                                                  |
| `workPhone`             | The work phone number for the user (for example, "+1-201-555-0123").                                                                                                                                                                                                                                                            |
| `mobilePhone`           | The mobile phone number for the user (for example, "+1-201-555-0123").                                                                                                                                                                                                                                                          |
| `pagerPhone`            | The pager number for the user (for example, "+1-201-555-0123").                                                                                                                                                                                                                                                                 |
| `faxPhone`              | The fax number for the user (for example, "+1-201-555-0123").                                                                                                                                                                                                                                                                   |
| `homePhone`             | The home phone number for the user (for example, "+1-201-555-0123").                                                                                                                                                                                                                                                            |
| `otherPhone`            | Another phone number that can be used to reach the user (for example, "+1-201-555-0123").                                                                                                                                                                                                                                       |
| `workStreetAddress`     | The work street address for the user, which may include house number, street name, P.O. box, and multi-line extended street address information.                                                                                                                                                                                |
| `workCity`              | The work city or locality component for the user's mailing address.                                                                                                                                                                                                                                                             |
| `workState`             | The work state or region component for the user's mailing address.                                                                                                                                                                                                                                                              |
| `workPostalCode`        | The work ZIP or postal code component for the user's mailing address.                                                                                                                                                                                                                                                           |
| `workCountry`           | The work country component for the user's mailing address. When specified, the value MUST be in ISO 3166-1 "alpha-2" code format [ISO3166](https://tools.ietf.org/html/rfc7643#ref-ISO3166); for example, the United States and Sweden are "US" and "SE", respectively.                                                         |
| `workFormattedAddress`  | The user's full work address, formatted for display.                                                                                                                                                                                                                                                                            |
| `homeStreetAddress`     | The home street address for the user, which may include house number, street name, P.O. box, and multi-line extended street address information.                                                                                                                                                                                |
| `homeCity`              | The home city or locality component for the user's mailing address.                                                                                                                                                                                                                                                             |
| `homeState`             | The home state or region component for the user's mailing address.                                                                                                                                                                                                                                                              |
| `homePostalCode`        | The home ZIP or postal code component for the user's mailing address.                                                                                                                                                                                                                                                           |
| `homeCountry`           | The home country component for the user's mailing address. When specified, the value MUST be in ISO 3166-1 "alpha-2" code format [ISO3166](https://tools.ietf.org/html/rfc7643#ref-ISO3166); for example, the United States and Sweden are "US" and "SE", respectively.                                                         |
| `homeFormattedAddress`  | The user's full home address, formatted for display.                                                                                                                                                                                                                                                                            |
| `otherStreetAddress`    | An alternate street address for the user, which may include house number, street name, P.O. box, and multi-line extended street address information.                                                                                                                                                                            |
| `otherCity`             | The alternate city or locality component for the user's mailing address.                                                                                                                                                                                                                                                        |
| `otherState`            | The alternate state or region component for the user's mailing address.                                                                                                                                                                                                                                                         |
| `otherPostalCode`       | The alternate ZIP or postal code component for the user's mailing address.                                                                                                                                                                                                                                                      |
| `otherCountry`          | The alternate country component for the user's mailing address. When specified, the value MUST be in ISO 3166-1 "alpha-2" code format [ISO3166](https://tools.ietf.org/html/rfc7643#ref-ISO3166); for example, the United States and Sweden are "US" and "SE", respectively.                                                    |
| `otherFormattedAddress` | The alternate address for the user, formatted for display.                                                                                                                                                                                                                                                                      |
| `qqIm`                  | The QQ instant messaging address for the user.                                                                                                                                                                                                                                                                                  |
| `skypeIm`               | The Skype instant messaging address for the user.                                                                                                                                                                                                                                                                               |
| `gtalkIm`               | The Google Talk instant messaging address for the user.                                                                                                                                                                                                                                                                         |
| `aimIm`                 | The AOL Instant Messenger instant messaging address for the user.                                                                                                                                                                                                                                                               |
| `icqIm`                 | The ICQ instant messaging address for the user.                                                                                                                                                                                                                                                                                 |
| `yahooIm`               | The Yahoo Messenger instant messaging address for the user.                                                                                                                                                                                                                                                                     |
| `msnIm`                 | The MSN Messenger instant messaging address for the user.                                                                                                                                                                                                                                                                       |
| `xmppIm`                | The XMPP instant messaging address for the user.                                                                                                                                                                                                                                                                                |
| `entitlements`          | A list of entitlements for the user that represent a thing the user has. An entitlement may be an additional right to a thing, object, or service.                                                                                                                                                                              |
| `roles`                 | A list of roles for the user that collectively represent who the user is. For example, "Student", "Faculty".                                                                                                                                                                                                                    |
| `certificates`          | A list of certificates associated with the resource (for example, a user). Each value contains exactly one DER-encoded X.509 certificate (see [Section 4 of RFC5280](https://tools.ietf.org/html/rfc5280#section-4)), which MUST be base64 encoded per [Section 4 of \[RFC4648](https://tools.ietf.org/html/rfc4648#section-4). |
| `employeeNumber`        | A string identifier, typically numeric or alphanumeric, assigned to a person, often based on order of hire or association with an organization.                                                                                                                                                                                 |
| `costCenter`            | The cost center for the user.                                                                                                                                                                                                                                                                                                   |
| `organization`          | The organization for the user.                                                                                                                                                                                                                                                                                                  |
| `division`              | The division for the user.                                                                                                                                                                                                                                                                                                      |
| `department`            | The department for the user.                                                                                                                                                                                                                                                                                                    |

---

---
title: Upgrading an existing deployment
description: If you're upgrading from a previous version of the Aquera Provisioner, note your existing service provider (SP) connection configuration and create a new connection.
component: aquera
page_id: aquera:setup:pf_aquera_connector_upgrading_an_existing_deployment
canonical_url: https://docs.pingidentity.com/integrations/aquera/setup/pf_aquera_connector_upgrading_an_existing_deployment.html
revdate: June 27, 2024
section_ids:
  upgrading-an-existing-deployment-in-pingfederate-10-1-or-later: Upgrading an existing deployment in PingFederate 10.1 or later
  steps: Steps
  upgrading-an-existing-deployment-in-pingfederate-10-0-or-earlier: Upgrading an existing deployment in PingFederate 10.0 or earlier
  steps-2: Steps
---

# Upgrading an existing deployment

If you're upgrading from a previous version of the Aquera Provisioner, note your existing service provider (SP) connection configuration and create a new connection.

## Upgrading an existing deployment in PingFederate 10.1 or later

### Steps

1. Back up your current PingFederate configuration as shown in [Configuration archive](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_configurationarchivetasklet_selectimportexportstate.html) in the PingFederate documentation.

2. In the PingFederate administrative console, go to **Applications > Integration > SP Connections** and select your connection.

3. Note the attribute mappings for your existing SP connection.

   Learn more in [Mapping attributes](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_saaschanneltasklet_saasattrmappingmgmtstate.html) in the PingFederate documentation.

4. Delete your existing SP connection.

   1. Go to **Applications > Integration > SP Connections**.

   2. For your existing connection, click **Select action**, and then click **Delete**. Click **Confirm.**

5. Complete the steps in [Deploying the integration files](pf_aquera_connector_deploying_the_integration_files.html).

6. Complete the steps in [Creating a provisioning connection](pf_aquera_connector_creating_a_provisioning_connection.html).

   * From **Outbound Provisioning > Manage Channels > Channel**, on the **Attribute Mapping** tab, configure the attribute mappings based on your notes.

7. (Optional) Complete the steps in [Adding SSO to a connection](pf_aquera_connector_adding_sso_to_a_connection.html).

## Upgrading an existing deployment in PingFederate 10.0 or earlier

### Steps

1. Back up your current PingFederate configuration as shown in [Configuration archive](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_configurationarchivetasklet_selectimportexportstate.html) in the PingFederate documentation.

2. In the PingFederate administrative console, go to **Identity Provider > SP Connections** and select your connection.

3. Note the attribute mappings for your existing SP connection.

   Learn more in [Mapping attributes](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_saaschanneltasklet_saasattrmappingmgmtstate.html) in the PingFederate documentation.

4. Delete your existing SP connection.

   1. Go to **Identity Provider > SP Connections > Manage All**.

   2. For your existing connection, click **Select action**, and then click **Delete**. Click **Save.**

5. Complete the steps in [Deploying the integration files](pf_aquera_connector_deploying_the_integration_files.html).

6. Complete the steps in [Creating a provisioning connection](pf_aquera_connector_creating_a_provisioning_connection.html).

   * From **Outbound Provisioning > Manage Channels > Channel**, on the **Attribute Mapping** tab, configure the attribute mappings based on your notes.

7. (Optional) Complete the steps in [Adding SSO to a connection](pf_aquera_connector_adding_sso_to_a_connection.html).

---

---
title: Upgrading an existing deployment in PingFederate 10.0 or earlier
description: Back up your current PingFederate configuration as shown in Configuration archive in the PingFederate documentation.
component: aquera
page_id: aquera:setup:pf_aquera_connector_upgrading_an_existing_deployment_in_pf_100_or_earlier
canonical_url: https://docs.pingidentity.com/integrations/aquera/setup/pf_aquera_connector_upgrading_an_existing_deployment_in_pf_100_or_earlier.html
revdate: June 27, 2024
section_ids:
  steps: Steps
---

# Upgrading an existing deployment in PingFederate 10.0 or earlier

## Steps

1. Back up your current PingFederate configuration as shown in [Configuration archive](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_configurationarchivetasklet_selectimportexportstate.html) in the PingFederate documentation.

2. In the PingFederate administrative console, go to **Identity Provider > SP Connections** and select your connection.

3. Note the attribute mappings for your existing SP connection.

   Learn more in [Mapping attributes](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_saaschanneltasklet_saasattrmappingmgmtstate.html) in the PingFederate documentation.

4. Delete your existing SP connection.

   1. Go to **Identity Provider > SP Connections > Manage All**.

   2. For your existing connection, click **Select action**, and then click **Delete**. Click **Save.**

5. Complete the steps in [Deploying the integration files](pf_aquera_connector_deploying_the_integration_files.html).

6. Complete the steps in [Creating a provisioning connection](pf_aquera_connector_creating_a_provisioning_connection.html).

   * From **Outbound Provisioning > Manage Channels > Channel**, on the **Attribute Mapping** tab, configure the attribute mappings based on your notes.

7. (Optional) Complete the steps in [Adding SSO to a connection](pf_aquera_connector_adding_sso_to_a_connection.html).

---

---
title: Upgrading an existing deployment in PingFederate 10.1 or later
description: Back up your current PingFederate configuration as shown in Configuration archive in the PingFederate documentation.
component: aquera
page_id: aquera:setup:pf_aquera_connector_upgrading_an_existing_deployment_in_pf_101_or_later
canonical_url: https://docs.pingidentity.com/integrations/aquera/setup/pf_aquera_connector_upgrading_an_existing_deployment_in_pf_101_or_later.html
revdate: June 27, 2024
section_ids:
  steps: Steps
---

# Upgrading an existing deployment in PingFederate 10.1 or later

## Steps

1. Back up your current PingFederate configuration as shown in [Configuration archive](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_configurationarchivetasklet_selectimportexportstate.html) in the PingFederate documentation.

2. In the PingFederate administrative console, go to **Applications > Integration > SP Connections** and select your connection.

3. Note the attribute mappings for your existing SP connection.

   Learn more in [Mapping attributes](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_saaschanneltasklet_saasattrmappingmgmtstate.html) in the PingFederate documentation.

4. Delete your existing SP connection.

   1. Go to **Applications > Integration > SP Connections**.

   2. For your existing connection, click **Select action**, and then click **Delete**. Click **Confirm.**

5. Complete the steps in [Deploying the integration files](pf_aquera_connector_deploying_the_integration_files.html).

6. Complete the steps in [Creating a provisioning connection](pf_aquera_connector_creating_a_provisioning_connection.html).

   * From **Outbound Provisioning > Manage Channels > Channel**, on the **Attribute Mapping** tab, configure the attribute mappings based on your notes.

7. (Optional) Complete the steps in [Adding SSO to a connection](pf_aquera_connector_adding_sso_to_a_connection.html).

---

---
title: User and group management
description: The Aquera Provisioner synchronizes users and groups from your datastore to the target service. The behavior of each provisioning capability is described below.
component: aquera
page_id: aquera::pf_aquera_connector_user_and_group_management
canonical_url: https://docs.pingidentity.com/integrations/aquera/pf_aquera_connector_user_and_group_management.html
revdate: June 27, 2024
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

The Aquera Provisioner synchronizes users and groups from your datastore to the target service. The behavior of each provisioning capability is described below.

Learn more about configuring these capabilities in the [Creating a provisioning connection](setup/pf_aquera_connector_creating_a_provisioning_connection.html) step of the setup process.

## Synchronizing existing users

PingFederate synchronizes users based on the `userName` attribute in the target service. If a user already exists in your datastore and the target service, mapping this attribute correctly links the two records together.

For example:

* In the target service, Janet's `userName` is `jsmith`.

* In your datastore, Janet's `sAMAccountName` is `jsmith`.

* On the **Attribute Mapping** tab of your provisioning connection configuration, you map the `userName` attribute to `sAMAccountName`.

* When the provisioning connector runs, the datastore user is provisioned with a `userName` of `jsmith`. That matches Janet's existing `userName` in the target service, so her information in the datastore is synchronized to her the target service account.

## User provisioning

PingFederate provisions users when one of the following happens:

* A user is added to the datastore group or filter that is targeted by the provisioning connector.

* A user with "disabled" status is added to the datastore group or filter that is targeted by the provisioning connector, and the **Provision disabled users** provisioning option is enabled.

The **Source Location** tab of your provisioning connection configuration defines which users PingFederate targets for provisioning.

## User updates

PingFederate updates users when a user attribute changes in your datastore.

The **Attribute Mapping** tab of your provisioning connection configuration defines which attributes PingFederate monitors for changes.

## User deprovisioning

PingFederate deprovisions users when one of the following happens:

* A user is deleted from the user store.

* A user is disabled in the user store.

* A user is removed from the datastore group or filter that is targeted by the provisioning connector.

The **Remove User Action** setting in your provisioning connection configuration defines whether PingFederate disables or deletes the user.

Some Aquera apps also include a **deleteOnDeactivation** setting on the Aquera console.

## Synchronizing existing groups

PingFederate synchronizes groups from the datastore to the target service based on the group name.

For example:

* In the target service, there is a group is named `Accounting`.

* In your datastore, there is a group with a `CN` of `Accounting`.

* When the provisioning connector runs, the two groups are synchronized.

## Group provisioning

PingFederate provisions groups when a group is added to the datastore filter that is targeted by the provisioning connector.

The **Source Location** tab in your provisioning connection configuration defines which groups PingFederate targets for provisioning and monitors for changes.

Some Aquera apps do not support group creation. In this case, create groups manually in the target service. The connector will then be able to update the groups.

## Group name updates

PingFederate renames groups when they are renamed in the datastore.

## Group membership updates

PingFederate updates group memberships when memberships change in the datastore, whether the change is in the group's properties or a user's properties.

Group memberships in the datastore overwrite the group memberships in the target service.

## Group deletion

PingFederate deletes groups when any of the following happen:

* The group is deleted in the datastore.

* The group is removed from the datastore group or filter that is targeted by the provisioning connector.

Group deletions are permanent and cannot be undone.

Some Aquera apps do not support group deletion. In this case, delete groups manually in the target service.