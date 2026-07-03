---
title: Adding SSO to a connection
description: To enable single sign-on (SSO), modify the provisioning connection that you created in Creating a provisioning connection.
component: scim
page_id: scim:setup:pf_scim_connector_adding_sso_to_a_connection
canonical_url: https://docs.pingidentity.com/integrations/scim/setup/pf_scim_connector_adding_sso_to_a_connection.html
revdate: July 8, 2024
section_ids:
  steps: Steps
  choose-from: Choose from:
---

# Adding SSO to a connection

To enable single sign-on (SSO) *(tooltip: \<div class="paragraph">
\<p>The process of authenticating an identity (signing on) at one website (usually with a user ID and password) and then accessing resources secured by other domains without reauthenticating.\</p>
\</div>)*, modify the provisioning connection that you created in [Creating a provisioning connection](pf_scim_connector_creating_a_provisioning_connection.html).

## Steps

1. On the PingFederate administrative console, open your existing SP connection.

   ### Choose from:

   * For PingFederate 10.1 or later: go to **Applications > Integration > SP Connections**. Select your connection.

   * For PingFederate 10.0 or earlier: go to **Identity Provider > SP Connections**. Select your connection.

2. On the **Connection Type** tab select **Browser SSO Profiles**. Click **Next**.

3. On the **Browser SSO** tab, configure your SSO settings.

   You can find specific connection details in the documentation and administrative console provided by the target service.

   You can find configuration help in [Configuring IdP Browser SSO](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_spconnectionconfigtasklet_spbrowserssostate.html) in the PingFederate documentation.

4. On the **Activation and Summary** tab, above the **Summary** section, click the toggle to turn on the connection. Click **Save**.

---

---
title: Changelog
description: The following is the change history for the SCIM Provisioner.
component: scim
page_id: scim:release_notes:pf_scim_connector_changelog
canonical_url: https://docs.pingidentity.com/integrations/scim/release_notes/pf_scim_connector_changelog.html
revdate: August 14, 2025
section_ids:
  scim-provisioner-1-9-0-1-august-2025: SCIM Provisioner 1.9.0.1 - August 2025
  scim-provisioner-1-6-june-2024: SCIM Provisioner 1.6 – June 2024
  scim-provisioner-1-5-2-september-2023: SCIM Provisioner 1.5.2 – September 2023
  scim-provisioner-1-5-december-2022: SCIM Provisioner 1.5 – December 2022
  scim-provisioner-1-4-2-august-2021: SCIM Provisioner 1.4.2 – August 2021
  scim-provisioner-1-4-december-2020: SCIM Provisioner 1.4 – December 2020
  scim-provisioner-1-3-march-2020: SCIM Provisioner 1.3 – March 2020
  scim-provisioner-1-2-march-2019: SCIM Provisioner 1.2 – March 2019
  scim-provisioner-1-1-july-2018: SCIM Provisioner 1.1 – July 2018
  scim-provisioner-1-0-october-2017: SCIM Provisioner 1.0 – October 2017
---

# Changelog

The following is the change history for the SCIM Provisioner.

## SCIM Provisioner 1.9.0.1 - August 2025

* Added support for using custom schema URNs.

## SCIM Provisioner 1.6 – June 2024

* Added the ability to request specific OAuth scopes to the OAuth 2 client credentials authentication method. Learn more in [SCIM provisioner settings reference](../setup/pf_scim_connector_scim_connector_settings_reference.html).

* Fixed an issue that caused a JSON parsing error if non-standard fields were present in the SCIM 2.0 `Enterprise User Schema Extension`.

## SCIM Provisioner 1.5.2 – September 2023

* Fixed an issue with `type` sub-attribute case sensitivity that caused a `NullPointerException` error. `Type` sub-attribute values for phone numbers and photos are now case insensitive.

## SCIM Provisioner 1.5 – December 2022

* Added support for user custom attributes for SCIM 2.0.

* Added `homeEmail` and `otherEmail` attributes.

## SCIM Provisioner 1.4.2 – August 2021

* Fixed an issue that caused the **Check Connection** function to fail when correct credentials were provided.

* Fixed an issue that caused a `NullPointerException` error when the `photo` attribute was empty.

## SCIM Provisioner 1.4 – December 2020

* Added support for the PATCH method for group updates. Learn more in the [SCIM provisioner settings reference](../setup/pf_scim_connector_scim_connector_settings_reference.html).

* Improved backward compatibility for SCIM 1.1 headers.

* Fixed an issue that could cause the provisioner to parse groups incorrectly.

## SCIM Provisioner 1.3 – March 2020

* Added support for the `application/scim+json` HTTP header type.

* Improved support for services that limit the number of groups that can be retrieved per request by adding a **Results Per Page** field in the connection configuration.

* Improved the **SCIM URL** field in the connection configuration to work regardless of whether a trailing slash (`/`) is included in the URL.

* Fixed an issue that caused connection tests to return a success when the wrong credentials were used.

* Fixed an issue that caused groups to be serialized incorrectly.

## SCIM Provisioner 1.2 – March 2019

* Added configuration options for the Unique User Identifier.

* Improved error handling and reporting for cases where users in the target application do not have an ID.

## SCIM Provisioner 1.1 – July 2018

* Added the option to provision groups with common name (CN) or distinguished name (DN).

* Fixed an issue where SCIM v2 requests included SCIM v1.1 schema URN's.

* Fixed a compatibility issue when multiple SCIM SaaS connectors are deployed.

* Fixed an issue where the NO\_CONTENT HTTP response code was not being handled.

* Fixed an issue where the SERVER\_ERROR HTTP response code was not being handled.

* Fixed an issue where the user's active status was not updated correctly on update requests.

* Fixed an issue where SCIM v2 errors descriptions were not logged correctly.

* Fixed an issue where an empty return body on a user PUT would cause a JSON parse exception.

## SCIM Provisioner 1.0 – October 2017

* Initial release.

* Added support for user provisioning.

* Added support for group provisioning.

* Added support for adding users to groups.

* Added support for SCIM core and enterprise attributes.

* Added support for basic authentication, OAuth 2 bearer token and OAuth 2 client credentials authentication.

* Added support for SCIM overrides (Filter expression, authorization header type, users API path, groups API path).

* Added configuration options for CRUD capabilities.

* Added configuration options for provisioning disabled users.

* Added configuration options for deprovisioning actions.

---

---
title: Configuring single sign-on
description: To allow PingFederate to act as an identity provider for the target service, modify your connection to include single sign-on (SSO).
component: scim
page_id: scim:setup:pf_scim_connector_configuring_single_sign_on
canonical_url: https://docs.pingidentity.com/integrations/scim/setup/pf_scim_connector_configuring_single_sign_on.html
revdate: July 8, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Configuring single sign-on

To allow PingFederate to act as an identity provider for the target service, modify your connection to include single sign-on (SSO) *(tooltip: \<div class="paragraph">
\<p>The process of authenticating an identity (signing on) at one website (usually with a user ID and password) and then accessing resources secured by other domains without reauthenticating.\</p>
\</div>)*.

## About this task

|   |                                                                                                                        |
| - | ---------------------------------------------------------------------------------------------------------------------- |
|   | SSO is not required for provisioning. If you only want to use the SCIM Provisioner for provisioning, skip these steps. |

## Steps

1. Complete the steps in [Adding SSO to a connection](pf_scim_connector_adding_sso_to_a_connection.html).

2. On the target service, configure SSO by following the documentation provided by the service. When prompted for information about PingFederate, refer to [PingFederate SSO details for the service provider](pf_scim_connector_pf_sso_details_for_the_service_provider.html).

---

---
title: Creating a provisioning connection
description: To allow PingFederate to manage users in the target service, create a service provider (SP) connection.
component: scim
page_id: scim:setup:pf_scim_connector_creating_a_provisioning_connection
canonical_url: https://docs.pingidentity.com/integrations/scim/setup/pf_scim_connector_creating_a_provisioning_connection.html
revdate: July 8, 2024
section_ids:
  steps: Steps
  choose-from: Choose from:
---

# Creating a provisioning connection

To allow PingFederate to manage users in the target service, create a service provider (SP) connection.

## Steps

1. In the PingFederate administrative console, create a new SP connection:

   ### Choose from:

   * For PingFederate 10.1 or later: go to **Applications > Integration > SP Connections**. Click **Create Connection**.

   * For PingFederate 10.0 or earlier: go to **Identity Provider > SP Connections**. Click **Create Connection**.

2. Configure the basic connection details with the the target service quick connection template:

   1. On the **Connection Template** tab, select **Use a template for this connection**.

   2. In the **Connection Template** list, select **SCIM Provisioner**. Click **Next**.

   3. On the **Connection Type** tab select **Outbound Provisioning**. Click **Next**.

   4. On the **General Info** tab, in the **Connection Name** field, enter a name of your choosing. Click **Next**.

3. On the **Outbound Provisioning** tab, configure provisioning with the following details.

   Learn more in [Configuring outbound provisioning](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_spconnectionconfigtasklet_saasprovisioningstate.html) in the PingFederate documentation.

   1. On the **Target** screen, enter the URL and authentication details that you noted in [Gathering information from the service provider](pf_scim_connector_gathering_information_from_the_service_provider.html).

      |   |                                                                                                   |
      | - | ------------------------------------------------------------------------------------------------- |
      |   | PingFederate verifies the authentication details when you activate the channel and SP connection. |

   2. Under **Provisioning Options**, customize the provisioning connector behavior by referring to [SCIM provisioner settings reference](pf_scim_connector_scim_connector_settings_reference.html). Click **Next**.

   3. On the **Manage Channels > Attribute Mapping** tab, complete the attribute mappings by referring to [Supported attributes reference](pf_scim_connector_supported_attributes_reference.html).

      Learn more in [Managing channels](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_saasmanagementtasklet_saasmanagementstate.html) in the PingFederate documentation.

4. On the **Activation and Summary** tab, above the **Summary** section, click the toggle to turn on the connection. Click **Save**.

---

---
title: Deploying the integration files
description: To get started with the integration, deploy the SCIM Provisioner files to your PingFederate directory.
component: scim
page_id: scim:setup:pf_scim_connector_deploying_the_integration_files
canonical_url: https://docs.pingidentity.com/integrations/scim/setup/pf_scim_connector_deploying_the_integration_files.html
revdate: July 8, 2024
section_ids:
  steps: Steps
---

# Deploying the integration files

To get started with the integration, deploy the SCIM Provisioner files to your PingFederate directory.

## Steps

1. Download the SCIM Provisioner `.zip` archive from the [**Add-ons** tab of the PingFederate downloads page](https://www.pingidentity.com/en/resources/downloads/pingfederate.html) or the [Ping Identity Marketplace](https://marketplace.pingone.com/item/scim-provisioner).

2. Stop PingFederate.

3. If you're upgrading an existing deployment, delete the `pf-scim-quickconnection-<version>.jar` file from your `<pf_install>/pingfederate/server/default/deploy` directory.

4. Extract the `.zip` archive and merge the contents of the `dist` directory with your `<pf_install>/pingfederate/server/default/deploy` directory.

5. Enable the PingFederate provisioning engine:

   1. Open your `<pf_install>/pingfederate/bin/run.properties` file.

   2. Change `pf.provisioner.mode` to `STANDALONE`. Save the file.

      |   |                                                                                                                                                                                                                                        |
      | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      |   | To configure the `FAILOVER` mode instead, see [Deploying provisioning failover](https://docs.pingidentity.com/pingfederate/latest/server_clustering_guide/pf_deploy_provis_failover.html) in the PingFederate Server Clustering Guide. |

6. Start PingFederate.

7. If you operate PingFederate in a cluster, repeat steps 2-4 and step 6 for each engine node.

---

---
title: Download manifest
description: The following files are included in the SCIM Provisioner .zip archive:
component: scim
page_id: scim:release_notes:pf_scim_connector_download_manifest
canonical_url: https://docs.pingidentity.com/integrations/scim/release_notes/pf_scim_connector_download_manifest.html
revdate: July 8, 2024
---

# Download manifest

The following files are included in the SCIM Provisioner `.zip` archive:

* `Legal.pdf`: Copyright and license information.

* `dist`: Contains the integration files.

  * `pf-scim-quickconnection-<version>.jar`: The SCIM Provisioner quick connection template.

---

---
title: Enabling provisioning and single sign-on in PingFederate
description: To use PingFederate for provisioning and single sign-on, configure an external datastore and set a SAML entity ID.
component: scim
page_id: scim:setup:pf_scim_connector_enabling_provisioning_and_single_sign_on_in_pf
canonical_url: https://docs.pingidentity.com/integrations/scim/setup/pf_scim_connector_enabling_provisioning_and_single_sign_on_in_pf.html
revdate: July 8, 2024
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

   Learn more in [Datastores](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_datastores.html) in the PingFederate documentation.

2. Go to **System > Protocol Settings > Roles & Protocols**.

3. Select the **Enable Identity Provider IdP Role and Support the Following** checkbox.

4. Select the **SAML 2.0** and **Outbound Provisioning** checkboxes. Click **Next**.

5. Click the **Federation Info** tab.

6. In the **SAML 2.0 Entity ID** field, enter a name for PingFederate to use to identify itself to SAML partners.

7. On the **Outbound Provisioning** tab, in the **Provisioner Data Store** list, select the internal database that will store the synchronization state. Click **Save**.

   Learn more in [Configuring outbound provisioning settings](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_protocolsettingstasklet_saasglobalprovisioningsettingsstate.html) in the PingFederate documentation.

---

---
title: Enabling provisioning and single sign-on in PingFederate 10.0 or earlier
description: In the PingFederate administrative console, configure the datastore for PingFederate to use as the source of user data.
component: scim
page_id: scim:setup:pf_scim_connector_enabling_provisioning_and_single_sign_on_in_pf_100_or_earlier
canonical_url: https://docs.pingidentity.com/integrations/scim/setup/pf_scim_connector_enabling_provisioning_and_single_sign_on_in_pf_100_or_earlier.html
revdate: July 8, 2024
section_ids:
  steps: Steps
---

# Enabling provisioning and single sign-on in PingFederate 10.0 or earlier

## Steps

1. In the PingFederate administrative console, configure the datastore for PingFederate to use as the source of user data.

   Learn more in [Datastores](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_datastores.html) in the PingFederate documentation.

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
component: scim
page_id: scim:setup:pf_scim_connector_enabling_provisioning_and_single_sign_on_in_pf_101_or_later
canonical_url: https://docs.pingidentity.com/integrations/scim/setup/pf_scim_connector_enabling_provisioning_and_single_sign_on_in_pf_101_or_later.html
revdate: July 8, 2024
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
title: Gathering information from the service provider
description: Before you configure the SCIM Connector, collect the connection details from the target service.
component: scim
page_id: scim:setup:pf_scim_connector_gathering_information_from_the_service_provider
canonical_url: https://docs.pingidentity.com/integrations/scim/setup/pf_scim_connector_gathering_information_from_the_service_provider.html
revdate: June 25, 2024
section_ids:
  steps: Steps
---

# Gathering information from the service provider

Before you configure the SCIM Connector, collect the connection details from the target service.

## Steps

1. Note your SCIM URL from the SCIM-enabled SP.

2. Note your client credentials from the SCIM-enabled SP. This will depend on the authentication method used by the SP, which might include:

   * **Basic Authentication**: Username and password.

   * **OAuth 2.0 Bearer Token**: Access token.

   * **OAuth 2.0 Client Credentials**: Client ID, client secret, token endpoint.

---

---
title: Known issues and limitations
description: The following are known issues or limitations with the SCIM Provisioner.
component: scim
page_id: scim:release_notes:pf_scim_connector_known_issues_and_limitations
canonical_url: https://docs.pingidentity.com/integrations/scim/release_notes/pf_scim_connector_known_issues_and_limitations.html
revdate: July 8, 2024
section_ids:
  known-issues: Known issues
  known-limitations: Known limitations
---

# Known issues and limitations

The following are known issues or limitations with the SCIM Provisioner.

## Known issues

There are no known issues.

## Known limitations

Service provider (SP) connections:

* The Unique User Identifier cannot be changed in an SP connection configuration. To change to a different Unique User Identifier, delete the existing connection, restart PingFederate, and then create a connection with the new Unique User Identitier.

* All SP connections with the same target must use the same Unique User Identifier. If multiple SP connections are created for the same target, every subsequent connection will use the Unique User Identifier configured in the first connection that was created.

Attributes:

* The connector has a limit of one value per type (home, work, other, and so on) for multi-value attributes (email, phone, address).

* If the SaaS does not specify type or primary information on multi-value attributes (email, phone, address), unexpected behavior can occur. During an update, existing attributes on the SaaS may not be removed, and the desired value may not be correctly set as primary.

* The connector cannot clear a user attribute once it has been set.

* If the target application supports two email attributes and one attribute is empty, the connector populates both attributes with the email address and sets both as "primary". This can produce unexpected effects in some target applications.

Group provisioning:

* When provisioning groups, only required attributes, such as [`displayName` and `members`](https://datatracker.ietf.org/doc/html/rfc7643#section-4.2), are supported. [Common attributes](https://datatracker.ietf.org/doc/html/rfc7643#section-3.1), such as `id` and `externalID`, are not supported because they're optional attributes.

Other:

* When an LDAP user is deleted in a targeted group distinguished name (DN), the provisioning connector doesn't propagate the deletion until a new user is added to the group. This limitation is compounded when the **User Create** provisioning option is disabled. You can find solutions in [SaaS provisioner does not remove the user](https://support.pingidentity.com/s/article/After-deleting-an-AD-user-account-SaaS-provisioner-does-not-remove-the-user-in-the-next-provisioning-cycle-when-Group-DN-is-specified) in the Knowledge Base.

* SCIM-compliant service providers can implement or interpret the SCIM standards differently, which could result in behavior that's not consistent with the SCIM Provisioner intended use.

---

---
title: PingFederate SSO details for the service provider
description: When enabling single sign-on (SSO) in the target service, you will require some or all of the following information from PingFederate.
component: scim
page_id: scim:setup:pf_scim_connector_pf_sso_details_for_the_service_provider
canonical_url: https://docs.pingidentity.com/integrations/scim/setup/pf_scim_connector_pf_sso_details_for_the_service_provider.html
revdate: July 8, 2024
section_ids:
  metadata-file: Metadata file
  saml-endpoint: SAML endpoint
  identity-provider-issuer: Identity provider issuer
  signing-certificate: Signing certificate
---

# PingFederate SSO details for the service provider

When enabling single sign-on (SSO) *(tooltip: \<div class="paragraph">
\<p>The process of authenticating an identity (signing on) at one website (usually with a user ID and password) and then accessing resources secured by other domains without reauthenticating.\</p>
\</div>)* in the target service, you will require some or all of the following information from PingFederate.

## Metadata file

Some target services allow you to import a Security Assertion Markup Language (SAML) *(tooltip: \<div class="paragraph">
\<p>A standard, XML-based, message-exchange framework enabling the secure transmittal of authentication tokens and other user attributes across domains.\</p>
\</div>)* metadata file that contains some of the following information. Learn more about exporting your metadata file in [Metadata export](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_metadata_export.html) in the PingFederate documentation.

## SAML endpoint

The PingFederate SAML endpoint is:

```
https://<pf_hostname>:<pf_port>/idp/SSO.saml2
```

## Identity provider issuer

This is SAML 2.0 Entity ID from PingFederate, which can be found on the **Server Settings** page. Learn more in [Specifying federation information](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_protocolsettingstasklet_federationinfostate.html).

|   |                                                                                                                                                                                                    |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | To override SAML 2.0 Entity ID on the **Server Settings** page for your SP Connection, go to the **General Info** page to add a Virtual Server ID. This value will be sent as the SAML Issuer URL. |

## Signing certificate

This is the public signing certificate that PingFederate uses to sign the SAML assertion. Learn more about exporting your certificate in [Managing digital signing certificates and decryption keys](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_certmanagementtasklet_dsigsigningcert_certmanagementstate.html).

---

---
title: SCIM Provisioner
description: The SCIM Provisioner allows PingFederate to integrate with a wide range of services that support the System for Cross-domain Identity Management (SCIM) for user provisioning and single sign-on (SSO).
component: scim
page_id: scim::pf_scim_connector
canonical_url: https://docs.pingidentity.com/integrations/scim/pf_scim_connector.html
revdate: June 25, 2024
section_ids:
  features: Features
  specifications: Specifications
  components: Components
  intended-audience: Intended audience
  system-requirements: System requirements
---

# SCIM Provisioner

The SCIM Provisioner allows PingFederate to integrate with a wide range of services that support the System for Cross-domain Identity Management (SCIM) *(tooltip: \<div class="paragraph">
\<p>An application-level, HTTP-based protocol for provisioning and managing user identity information. SCIM supplies a common schema for representing users and groups and provides a REST API.\</p>
\</div>)* for user provisioning and single sign-on (SSO) *(tooltip: \<div class="paragraph">
\<p>The process of authenticating an identity (signing on) at one website (usually with a user ID and password) and then accessing resources secured by other domains without reauthenticating.\</p>
\</div>)*.

## Features

* Manages users in the target service based on changes in an external datastore that is attached to PingFederate:

  * Creates, updates, disables, and deletes users

  * Allows you to enable the create, update, disable, and delete capabilities independently

  * Allows you to choose whether to disable or delete users when deprovisioning

  * Allows you to provision disabled users

* Manages groups in the target service based on changes in an external datastore that is attached to PingFederate:

  * Creates, updates, and deletes groups

  * Updates group memberships

* Enables browser-based SSO initiated by the service provider (SP) *(tooltip: \<div class="paragraph">
  \<p>In SAML, an entity that receives and accepts an authentication assertion issued by an IdP, typically for the purpose of allowing access to a protected resource.\</p>
  \</div>)* or identity provider (IdP) *(tooltip: \<div class="paragraph">
  \<p>A service that manages identity information and provides authentication services to relying clients or SPs within a federated or distributed network.\</p>
  \</div>)*.

## Specifications

The SCIM Connector implements the official specifications provided from [simplecloud.info](http://www.simplecloud.info/).

> **Collapse: The following table provides a brief summary:**
>
> | Feature                        | Outbound provisioning                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
> | ------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
> | SCIM specification             | 1.1, 2.0                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
> | Data format                    | JavaScript Object Notation (JSON) *(tooltip: \<div class="paragraph">&#xA;\<p>An open, lightweight data-interchange format that uses human-readable text to store and transmit data.\</p>&#xA;\</div>)*                                                                                                                                                                                                                                                                                                                                                                                              |
> | User and group CRUD operations | Yes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
> | Custom schema support          | * Users
>
>   Yes
>
> * Groups
>
>   No                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
> | Filtering support              | - Users
>
>   Yes
>
> - Groups
>
>   The connector allows group filtering by retrieving all groups and finding a match.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
> | PATCH                          | * Users
>
>   No
>
> * Groups
>
>   Yes. Learn more in the [SCIM provisioner settings reference](setup/pf_scim_connector_scim_connector_settings_reference.html).                                                                                                                                                                                                                                                                                                                                                                                                                                             |
> | Authentication method          | HTTP Basic Authentication, OAuth *(tooltip: \<div class="paragraph">&#xA;\<p>A standard framework that enables an application (OAuth client) to obtain access tokens from an OAuth authorization server for the purpose of retrieving protected resources on a resource server.\</p>&#xA;\</div>)* bearer token and OAuth client *(tooltip: \<div class="paragraph">&#xA;\<p>The application in an OAuth framework that requests access to resources. If the request is approved by the authorization server, the client is issued an access token for the resources.\</p>&#xA;\</div>)* credentials |
> | Source data stores             | Active Directory and other LDAPv3-compliant directory servers                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |

## Components

The SCIM provisioning and SSO connector:

* Allows PingFederate to manage users in the service based on changes in an external user data store

* (Optional configuration) Allows PingFederate to create an SSO connection to the service

* Includes a quick-connection template that pre-populates some configuration settings

## Intended audience

This document is intended for PingFederate administrators. If you need help during the setup process, see the following resources:

* PingFederate documentation:

  * [SP connection management](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_sp_connect_management.html)

  * [Identity provider SSO configuration](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_ident_provid_sso_config.html)

  * [Managing digital signing certificates and decryption keys](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_certmanagementtasklet_dsigsigningcert_certmanagementstate.html)

  * [Datastores](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_datastores.html)

  * [Configuring outbound provisioning](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_spconnectionconfigtasklet_saasprovisioningstate.html)

  * [Configuring outbound provisioning settings](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_protocolsettingstasklet_saasglobalprovisioningsettingsstate.html)

* [The SCIM 1.1 Developer Guide](https://www.pingidentity.com/developer/en/resources/scim-1-1-developers-guide.html#overview) on the Ping Identity Developer site

* [The SCIM specification](http://www.simplecloud.info/#Specification) on simplecloud.info

## System requirements

* PingFederate 9.0 or later.

* To allow PingFederate to make outbound connections, you might need to allow SCIM endpoints in your firewall.

---

---
title: SCIM provisioner settings reference
description: Configuration settings and provisioning options for the SCIM Provisioner.
component: scim
page_id: scim:setup:pf_scim_connector_scim_connector_settings_reference
canonical_url: https://docs.pingidentity.com/integrations/scim/setup/pf_scim_connector_scim_connector_settings_reference.html
revdate: June 25, 2024
---

# SCIM provisioner settings reference

Configuration settings and provisioning options for the SCIM Provisioner.

| Field Name                        | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| --------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **SCIM URL**                      | The SCIM base URL for the target service. For example:http\://scim-example.com/v2/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| **SCIM Version**                  | The SCIM version supported by the target service. The options are:- **2.0** (default)

- **1.1**.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| **Authentication Methods**        | The authentication method expected by the target service. The options are:- **None** (default)

- **Basic Authentication**

- **OAuth 2 Bearer Token**

- **OAuth 2 Client Credentials**.&#xA;&#xA;When an authentication method is selected, only the data required for that method will be processed. Entries in fields for other authentication methods will be ignored.                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Basic Authentication              |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| **Basic Authentication Username** | The username of the administrator account on the target service.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| **Basic Authentication Password** | The password of the administrator account on the target service.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| OAuth 2 Bearer Token              |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| **Access Token**                  | The OAuth access token for the target service.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| OAuth 2 Client Credentials        |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| **Token Request Endpoint**        | The endpoint that the connector uses to get an access token. For example:https\://scim-example.com/as/token.oauth2                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| **Client ID**                     | The client ID for the target service.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| **Client Secret**                 | The client secret the target service.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| **Scope**                         | An optional field that allows an admin to specify a comma-delimited list of OAuth scopes that access tokens requested from the SCIM provider should contain.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| SCIM Overrides                    |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| **Unique User Identifier**        | The attribute that uniquely identifies a user when PingFederate does not have access to the unique user ID that the target application assigns to a user.- userName (default)

  The value of the user name attribute. This sets the following filter expression:

  ```
  userName eq  <userName_value>
  ```

- workEmail

  The value of the work email attribute. Use when synchronization based on the username is not desirable. This sets the following filter expression:

  ```
  emails eq  <workEmail_value>
  ```To override a default filter, use the **Filter Expression** field.&#xA;&#xA;To change the unique user identifier:&#xA;&#xA;Delete the existing SP connection.&#xA;&#xA;Restart PingFederate.&#xA;&#xA;Create an SP Connection with the new Unique User Identifier setting. |
| **Filter Expression**             | A rule that determines how the connector uses the unique user identifier to match existing users in the target application to users in the data store.This expression overrides the default filter expression that is set by the **Unique User Identifier** field.The filter expression contains three parts:```
<attribute_name> <operation> <attribute_value>
```The *\<attribute\_value>* is represented by `"%s"` in the expression. It is populated by the value of the Unique User Identifier.Example filter expressions:- `username eq "%s"`

- `email co "%s"`&#xA;&#xA;Check the target service documentation and the SCIM Filtering specification to see which filter expressions are supported.                                                                                              |
| **Authorization Header Type**     | The type of HTTP authorization header used. For example, `oauth2`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| **Users API Path**                | The users API path is used when the users endpoint deviates from the SCIM specification (`/Users` is used by default when left blank).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| **Groups Path API**               | The groups API path is used when the groups endpoint deviates from the SCIM specification (`/Groups` is used by default when left blank).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| **Results Per Page**              | Determines the number of groups that PingFederate requests per `GET` request when searching all groups for a match. If the target service has a limit, change this value to match.A value of `-1` retrieves the largest page size allowed by the target service.The default value is `1000`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Provisioning Options              |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| **User Create**                   | * Selected (default)

  PingFederate creates users in the target service.

* Cleared

  PingFederate does not create users in the target service.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| **User Update**                   | - Selected (default)

  PingFederate updates existing users in the target service.

- Cleared

  PingFederate does not update existing users in the target service.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| **User Disable / Delete**         | * Selected (default)

  PingFederate removes users from the target service according to the **Remove User Action** setting.

  &#xA;&#xA;You might need to enable User Update for this to work with some services.

* Cleared

  PingFederate does not remove users from the target service.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| **Provision Disabled Users**      | - Selected

  PingFederate creates users in the target service with a "disabled" status.

- Cleared (default)

  If a user has a "disabled" status, PingFederate does not create the user in the target service.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|                                   | &#xA;&#xA;If any of the previous provisioning options are cleared, PingFederate logs a warning in the user workflow section of provisioner.log when the related action fails.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| **Remove User Action**            | * Delete

  PingFederate deletes the user from the target service.

* Disable (default)

  PingFederate disables the user in the target service.&#xA;&#xA;Some target applications do not support hard deleting users through external interfaces. For those services, users are disabled.This option applies when **User Disable / Delete** is selected, and either:* A previously provisioned user no longer meets the condition set on the **Source Location** tab.

* A user has been disabled or deleted from the data store.                                                                                                                                                                                                                                                                      |
| **Group Name Source**             | - Common Name (CN) (default)

  PingFederate provisions groups to the target service with a name equal to the common name (CN) of the group in the datastore.

- Distinguished Name (DN)

  PingFederate provisions groups with a name equal to the distinguished name (DN) of the group in the datastore.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| **Use PATCH for Group Updates**   | * Selected

  PingFederate uses the `PATCH` method to update groups in the target service. Select this option if the target service supports `PATCH` updates to use lighter API calls.

* Cleared (default)

  PingFederate uses the `PUT` method to update groups in the target service.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| **Custom Attribute Schema URNs**  | An optional field that allows an admin to explicitly specify a comma-delimited list of schema URNS for which to look for custom attributes.This is only required if the SCIM provider doesn't follow the standard naming convention for schema extensions that define custom attributes. For example, URNs such as:urn:ietf:params:scim:schemas:extension:*\<Organization Name>*:2.0:User.                                                                                                                                                                                                                                                                                                                                                                                                              |

---

---
title: Supported attributes reference
description: The following standard SCIM attributes can be mapped for user provisioning. Different attributes will be supported depending on the target service.
component: scim
page_id: scim:setup:pf_scim_connector_supported_attributes_reference
canonical_url: https://docs.pingidentity.com/integrations/scim/setup/pf_scim_connector_supported_attributes_reference.html
revdate: June 25, 2024
---

# Supported attributes reference

The following standard SCIM attributes can be mapped for user provisioning. Different attributes will be supported depending on the target service.

Learn more about SCIM attributes in [SCIM specification](https://tools.ietf.org/html/rfc7643#section-4.1.1) and the target service documentation.

| Attribute               | Description                                                                                                                                                                                                                                                                                                                       |
| ----------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `userName`              | A service provider's unique identifier for the user.This attribute is required.                                                                                                                                                                                                                                                   |
| `givenName`             | The given name of the user, or first name in most Western languages.For example, `Barbara`, given the full name Ms. Barbara Jane Jensen, III.                                                                                                                                                                                     |
| `familyName`            | The family name of the user, or last name in most Western languages.For example, `Jensen`, given the full name Ms. Barbara Jane Jensen, III.                                                                                                                                                                                      |
| `middleName`            | The middle name or names of the user.For example, `Jane`, given the full name Ms. Barbara Jane Jensen, III.                                                                                                                                                                                                                       |
| `honorificPrefix`       | The honorific prefix or prefixes of the user, or title in most Western languages.For example, `Ms.`, given the full name Ms. Barbara Jane Jensen, III.                                                                                                                                                                            |
| `honorificSuffix`       | The honorific suffix or suffixes of the user, or suffix in most Western languages.For example, `III`, given the full name Ms. Barbara Jane Jensen, III.                                                                                                                                                                           |
| `formattedName`         | The full name, including all middle names, titles, and suffixes as appropriate, formatted for display.For example, `Ms. Barbara Jane Jensen, III`.                                                                                                                                                                                |
| `workEmail`             | Work email for the user.For example, `bjensen@example.com`.                                                                                                                                                                                                                                                                       |
| `homeEmail`             | Home email for the user.For example, `bjensen@example.com`.                                                                                                                                                                                                                                                                       |
| `otherEmail`            | Other email for the user.For example, `bjensen@example.com`.                                                                                                                                                                                                                                                                      |
| `displayName`           | The name of the user, suitable for display to end-users.                                                                                                                                                                                                                                                                          |
| `title`                 | The user's title, such as `Vice President`.                                                                                                                                                                                                                                                                                       |
| `externalId`            | A string that is an identifier for the resource as defined by the provisioning client.                                                                                                                                                                                                                                            |
| `password`              | This attribute is intended to be used as a means to set, replace, or compare (for example, filter for equality) a password.                                                                                                                                                                                                       |
| `preferredLanguage`     | Indicates the user's preferred written or spoken languages and is generally used for selecting a localized user interface.                                                                                                                                                                                                        |
| `userType`              | Used to identify the relationship between the organization and the user.Typical values used might be `Contractor`, `Employee`, `Intern`, `Temp`, `External`, and `Unknown`, but any value can be used.                                                                                                                            |
| `locale`                | Used to indicate the user's default location for purposes of localizing such items as currency, date time format, or numerical representations.                                                                                                                                                                                   |
| `nickName`              | The casual way to address the user in real life.For example, `Bob` or `Bobby` instead of `Robert`.                                                                                                                                                                                                                                |
| `profileUrl`            | A URI that is a uniform resource locator that points to a location representing the user's online profile.For example, a web page.                                                                                                                                                                                                |
| `profilePhotoUrl`       | A URI that is a uniform resource locator that points to the user's profile photo.The resource must be a file (for example, a GIF, JPEG, or PNG image file) rather than a web page containing an image.                                                                                                                            |
| `profileThumbnailUrl`   | A URI that is a uniform resource locator that points to the user's profile thumbnail. The resource must be a file (for example, a GIF, JPEG, or PNG image file) rather than a web page containing an image.                                                                                                                       |
| `timezone`              | The user's time zone, in IANA Time Zone database format.For example, `America/Los_Angeles`.                                                                                                                                                                                                                                       |
| `workPhone`             | The work phone number for the user.For example, `+1-201-555-0123`.                                                                                                                                                                                                                                                                |
| `mobilePhone`           | The mobile phone number for the user.For example, `+1-201-555-0123`.                                                                                                                                                                                                                                                              |
| `pagerPhone`            | The pager number for the user.For example, `+1-201-555-0123`.                                                                                                                                                                                                                                                                     |
| `faxPhone`              | The fax number for the user.For example, `+1-201-555-0123`.                                                                                                                                                                                                                                                                       |
| `homePhone`             | The home phone number for the user.For example, `+1-201-555-0123`.                                                                                                                                                                                                                                                                |
| `otherPhone`            | Another phone number that can be used to reach the user.For example, `+1-201-555-0123`.                                                                                                                                                                                                                                           |
| `workStreetAddress`     | The work street address for the user, which could include house number, street name, P.O. box, and multiline extended street address information.                                                                                                                                                                                 |
| `workCity`              | The work city or locality component for the user's mailing address.                                                                                                                                                                                                                                                               |
| `workState`             | The work state or region component for the user's mailing address.                                                                                                                                                                                                                                                                |
| `workPostalCode`        | The work ZIP or postal code component for the user's mailing address.                                                                                                                                                                                                                                                             |
| `workCountry`           | The work country component for the user's mailing address.When specified, the value must be in ISO 3166-1 "alpha-2" code format \[[ISO3166](https://tools.ietf.org/html/rfc7643#ref-ISO3166)]. For example, the United States and Sweden are `US` and `SE`, respectively.                                                         |
| `workFormattedAddress`  | The user's full work address, formatted for display.                                                                                                                                                                                                                                                                              |
| `homeStreetAddress`     | The home street address for the user, which may include house number, street name, P.O. box, and multi-line extended street address information.                                                                                                                                                                                  |
| `homeCity`              | The home city or locality component for the user's mailing address.                                                                                                                                                                                                                                                               |
| `homeState`             | The home state or region component for the user's mailing address.                                                                                                                                                                                                                                                                |
| `homePostalCode`        | The home ZIP or postal code component for the user's mailing address.                                                                                                                                                                                                                                                             |
| `homeCountry`           | The home country component for the user's mailing address.When specified, the value MUST be in ISO 3166-1 "alpha-2" code format \[[ISO3166](https://tools.ietf.org/html/rfc7643#ref-ISO3166)]. For example, the United States and Sweden are `US` and `SE`, respectively.                                                         |
| `homeFormattedAddress`  | The user's full home address, formatted for display.                                                                                                                                                                                                                                                                              |
| `otherStreetAddress`    | An alternate street address for the user, which may include house number, street name, P.O. box, and multi-line extended street address information.                                                                                                                                                                              |
| `otherCity`             | The alternate city or locality component for the user's mailing address.                                                                                                                                                                                                                                                          |
| `otherState`            | The alternate state or region component for the user's mailing address.                                                                                                                                                                                                                                                           |
| `otherPostalCode`       | The alternate ZIP or postal code component for the user's mailing address.                                                                                                                                                                                                                                                        |
| `otherCountry`          | The alternate country component for the user's mailing address.When specified, the value MUST be in ISO 3166-1 "alpha-2" code format \[[ISO3166](https://tools.ietf.org/html/rfc7643#ref-ISO3166)]. For example, the United States and Sweden are `US` and `SE`, respectively.                                                    |
| `otherFormattedAddress` | The alternate address for the user, formatted for display.                                                                                                                                                                                                                                                                        |
| `qqIm`                  | The QQ instant messaging address for the user.                                                                                                                                                                                                                                                                                    |
| `skypeIm`               | The Skype instant messaging address for the user.                                                                                                                                                                                                                                                                                 |
| `gtalkIm`               | The Google Talk instant messaging address for the user.                                                                                                                                                                                                                                                                           |
| `aimIm`                 | The AOL Instant Messenger instant messaging address for the user.                                                                                                                                                                                                                                                                 |
| `icqIm`                 | The ICQ instant messaging address for the user.                                                                                                                                                                                                                                                                                   |
| `yahooIm`               | The Yahoo Messenger instant messaging address for the user.                                                                                                                                                                                                                                                                       |
| `msnIm`                 | The MSN Messenger instant messaging address for the user.                                                                                                                                                                                                                                                                         |
| `xmppIm`                | The XMPP instant messaging address for the user.                                                                                                                                                                                                                                                                                  |
| `entitlements`          | A list of entitlements for the user that represent a thing the user has.An entitlement could be an additional right to a thing, object, or service.                                                                                                                                                                               |
| `roles`                 | A list of roles for the user that collectively represent who the user is.For example, `Student` and `Faculty`.                                                                                                                                                                                                                    |
| `certificates`          | A list of certificates associated with the resource (for example, a user).Each value contains exactly one DER-encoded X.509 certificate (refer to [Section 4 of RFC5280](https://tools.ietf.org/html/rfc5280#section-4)), which MUST be base64 encoded per [Section 4 of RFC4648](https://tools.ietf.org/html/rfc4648#section-4). |
| `employeeNumber`        | A string identifier, typically numeric or alphanumeric, assigned to a person, often based on order of hire or association with an organization.                                                                                                                                                                                   |
| `costCenter`            | The cost center for the user.                                                                                                                                                                                                                                                                                                     |
| `organization`          | The organization for the user.                                                                                                                                                                                                                                                                                                    |
| `division`              | The division for the user.                                                                                                                                                                                                                                                                                                        |
| `department`            | The department for the user.                                                                                                                                                                                                                                                                                                      |
| `manager`               | The `id` of the SCIM resource representing the user's manager.                                                                                                                                                                                                                                                                    |

---

---
title: Upgrading an existing deployment
description: If you're upgrading from a previous version of the SCIM Provisioner, note your existing service provider (SP) connection configuration and create a new connection.
component: scim
page_id: scim:setup:pf_scim_connector_upgrading_an_existing_deployment
canonical_url: https://docs.pingidentity.com/integrations/scim/setup/pf_scim_connector_upgrading_an_existing_deployment.html
revdate: July 8, 2024
section_ids:
  upgrading-an-existing-deployment-in-pingfederate-10-1-or-later: Upgrading an existing deployment in PingFederate 10.1 or later
  steps: Steps
  upgrading-an-existing-deployment-in-pingfederate-10-0-or-earlier: Upgrading an existing deployment in PingFederate 10.0 or earlier
  steps-2: Steps
---

# Upgrading an existing deployment

If you're upgrading from a previous version of the SCIM Provisioner, note your existing service provider (SP) connection configuration and create a new connection.

## Upgrading an existing deployment in PingFederate 10.1 or later

### Steps

1. Back up your current PingFederate configuration as shown in [Configuration archive](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_configurationarchivetasklet_selectimportexportstate.html) in the PingFederate documentation.

2. In the PingFederate administrative console, go to **Applications > Integration > SP Connections** and select your connection.

3. Note the attribute mappings for your existing SP connection.

   Learn more in [Mapping attributes](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_saaschanneltasklet_saasattrmappingmgmtstate.html) in the PingFederate documentation.

4. Delete your existing SP connection.

   1. Go to **Applications > Integration > SP Connections**.

   2. For your existing connection, click **Select action**, and then click **Delete**. Click **Confirm.**

5. Complete the steps in [Deploying the integration files](pf_scim_connector_deploying_the_integration_files.html).

6. Complete the steps in [Creating a provisioning connection](pf_scim_connector_creating_a_provisioning_connection.html).

   * Go to **Outbound Provisioning > Manage Channels > Channel**. On the **Attribute Mapping** tab, configure the attribute mappings based on your notes.

7. (Optional) Complete the steps in [Adding SSO to a connection](pf_scim_connector_adding_sso_to_a_connection.html).

## Upgrading an existing deployment in PingFederate 10.0 or earlier

### Steps

1. Back up your current PingFederate configuration as shown in [Configuration archive](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_configurationarchivetasklet_selectimportexportstate.html) in the PingFederate documentation.

2. In the PingFederate administrative console, go to **Identity Provider > SP Connections** and select your connection.

3. Note the attribute mappings for your existing SP connection.

   Learn more in [Mapping attributes](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_saaschanneltasklet_saasattrmappingmgmtstate.html) in the PingFederate documentation.

4. Delete your existing SP connection.

   1. Go to **Identity Provider > SP Connections > Manage All**.

   2. For your existing connection, click **Select action**, and then click **Delete**. Click **Save.**

5. Complete the steps in [Deploying the integration files](pf_scim_connector_deploying_the_integration_files.html).

6. Complete the steps in [Creating a provisioning connection](pf_scim_connector_creating_a_provisioning_connection.html).

   * Go to **Outbound Provisioning > Manage Channels > Channel**. On the **Attribute Mapping** tab, configure the attribute mappings based on your notes.

7. (Optional) Complete the steps in [Adding SSO to a connection](pf_scim_connector_adding_sso_to_a_connection.html).

---

---
title: Upgrading an existing deployment in PingFederate 10.0 or earlier
description: Back up your current PingFederate configuration as shown in Configuration archive in the PingFederate documentation.
component: scim
page_id: scim:setup:pf_scim_connector_upgrading_an_existing_deployment_in_pf_100_or_earlier
canonical_url: https://docs.pingidentity.com/integrations/scim/setup/pf_scim_connector_upgrading_an_existing_deployment_in_pf_100_or_earlier.html
revdate: July 8, 2024
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

5. Complete the steps in [Deploying the integration files](pf_scim_connector_deploying_the_integration_files.html).

6. Complete the steps in [Creating a provisioning connection](pf_scim_connector_creating_a_provisioning_connection.html).

   * Go to **Outbound Provisioning > Manage Channels > Channel**. On the **Attribute Mapping** tab, configure the attribute mappings based on your notes.

7. (Optional) Complete the steps in [Adding SSO to a connection](pf_scim_connector_adding_sso_to_a_connection.html).

---

---
title: Upgrading an existing deployment in PingFederate 10.1 or later
description: Back up your current PingFederate configuration as shown in Configuration archive in the PingFederate documentation.
component: scim
page_id: scim:setup:pf_scim_connector_upgrading_an_existing_deployment_in_pf_101_or_later
canonical_url: https://docs.pingidentity.com/integrations/scim/setup/pf_scim_connector_upgrading_an_existing_deployment_in_pf_101_or_later.html
revdate: July 8, 2024
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

5. Complete the steps in [Deploying the integration files](pf_scim_connector_deploying_the_integration_files.html).

6. Complete the steps in [Creating a provisioning connection](pf_scim_connector_creating_a_provisioning_connection.html).

   * Go to **Outbound Provisioning > Manage Channels > Channel**. On the **Attribute Mapping** tab, configure the attribute mappings based on your notes.

7. (Optional) Complete the steps in [Adding SSO to a connection](pf_scim_connector_adding_sso_to_a_connection.html).

---

---
title: User and group management
description: The SCIM Provisioner synchronizes users and groups from your datastore to the target service. The following describes the behavior of each provisioning capability.
component: scim
page_id: scim::pf_scim_connector_user_and_group_management
canonical_url: https://docs.pingidentity.com/integrations/scim/pf_scim_connector_user_and_group_management.html
revdate: July 8, 2024
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

The SCIM Provisioner synchronizes users and groups from your datastore to the target service. The following describes the behavior of each provisioning capability.

|   |                                                                                                                                                                                                                                        |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | You can configure the following capabilities and specify which users to provision when you get to the [Creating a provisioning connection](setup/pf_scim_connector_creating_a_provisioning_connection.html) part of the setup process. |

## Synchronizing existing users

PingFederate synchronizes users based on the `userName` attribute in the target service. If a user already exists in your datastore and the target service, mapping this attribute correctly links the two records together. For example:

* In the target service, Janet's `userName` is `jsmith`.

* In your datastore, Janet's `sAMAccountName` is `jsmith`.

* On the **Attribute Mapping** tab of your provisioning connection configuration, map the `userName` attribute to `sAMAccountName`.

* When the provisioning connector runs, the datastore user is provisioned with a `userName` of `jsmith`. That matches Janet's existing `userName` in the target service, so her information in the datastore is synchronized to her the target service account.

## User provisioning

PingFederate provisions users when any of the following happens:

* A user is added to the datastore group or filter that is targeted by the provisioning connector.

* A user with `disabled` status is added to the datastore group or filter that is targeted by the provisioning connector, and the**Provision disabled users** provisioning option is enabled. This feature is not available in all provisioning connector versions.

You can define which users PingFederate targets for provisioning on the **Source Location** tab of your provisioning connection configuration.

## User updates

PingFederate updates users when a user attribute changes in your datastore.

You can define which attributes PingFederate monitors for changes on the **Attribute Mapping** tab of your provisioning connection configuration.

## User deprovisioning

PingFederate deprovisions users when any of the following happens:

* A user is deleted from the user store.

* A user is disabled in the user store.

* A user is removed from the datastore group or filter that is targeted by the provisioning connector.

The **Remove User Action** setting in the connection configuration determines whether the deprovisioning action disables or deletes the user.

## Synchronizing existing groups

PingFederate synchronizes groups from the datastore to the target service based on the group name. For example:

* In the target service, there is a group is named `Accounting`.

* In your datastore, there is a group with a `CN` of `Accounting`.

* When the provisioning connector runs, the two groups are synchronized.

## Group provisioning

PingFederate provisions groups when a group is added to the datastore filter that is targeted by the provisioning connector.

You can define which groups PingFederate targets for provisioning and monitors for changes on the **Source Location** tab in your provisioning connection configuration.

|   |                                                                                                                                                                                                                                                                                                                                            |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | When provisioning groups, only required attributes, such as [`displayName` and `members`](https://datatracker.ietf.org/doc/html/rfc7643#section-4.2), are supported. [Common attributes](https://datatracker.ietf.org/doc/html/rfc7643#section-3.1), such as `id` and `externalID`, are not supported because they're optional attributes. |

## Group name updates

PingFederate renames groups when they are renamed in the datastore.

## Group membership updates

PingFederate updates group memberships when memberships change in the datastore, whether the change is in the group's properties or a user's properties.

Group memberships in the datastore overwrite the group memberships in the target service.

## Group deletion

PingFederate deletes groups when any of the following happens:

* The group is deleted in the datastore.

* The group is removed from the datastore group or filter that is targeted by the provisioning connector.

|   |                                                     |
| - | --------------------------------------------------- |
|   | Group deletions are permanent and cannot be undone. |