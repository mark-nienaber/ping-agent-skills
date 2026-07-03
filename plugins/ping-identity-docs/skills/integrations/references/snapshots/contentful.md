---
title: Configuring Browser SSO
description: For the single sign-on (SSO) part of your connection to Contentful, use the details below.
component: contentful
page_id: contentful:configuring_single_sign-on:pf_contentful_integration_configuring_browser_sso
canonical_url: https://docs.pingidentity.com/integrations/contentful/configuring_single_sign-on/pf_contentful_integration_configuring_browser_sso.html
revdate: June 26, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Configuring Browser SSO

For the single sign-on (SSO) part of your connection to Contentful, use the details below.

## About this task

|   |                                                                                                                                                                                                                                                                                                                       |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | For all other settings, you can use the default or customize the configuration for your needs. Learn more in [Configuring IdP Browser SSO](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_spconnectionconfigtasklet_spbrowserssostate.html) in the PingFederate documentation. |

## Steps

1. On the **Browser SSO** tab, click **Configure Browser SSO**.

2. On the **Browser SSO > SAML Profiles** tab, select only **IDP-Initiated SSO** and **SP-Initiated SSO**. Click **Next**.

3. On the **Assertion Lifetime** tab, click **Next**.

4. On the **Assertion Creation** tab, configure the assertion.

   1. Click **Configure Assertion Creation**.

   2. On the **Attribute Contract** tab, set the following name formats. Click **Next**.

      **Attribute name formats**

      | Attribute Contract | Subject Name format                                     |
      | ------------------ | ------------------------------------------------------- |
      | SAML\_SUBJECT      | `urn:oasis:names:tc:SAML:1.1:nameid-format:unspecified` |
      | email              | `urn:oasis:names:tc:SAML:2.0:attrname-format:uri`       |
      | givenname          | `urn:oasis:names:tc:SAML:2.0:attrname-format:basic`     |
      | surname            | `urn:oasis:names:tc:SAML:2.0:attrname-format:basic`     |

   3. On the **Authentication Source Mapping** tab, click **Map New Adapter Instance**.

   4. On the **IdP Adapter Mapping > Adapter Instance** tab, in the **Adapter Instance** list, select the adapter instance that you created in [Creating an HTML Form Adapter instance](pf_contentful_integration_creating_an_html_form_adapter_instance.html). Click **Next**.

   5. On the **Mapping Method** tab, click **Next**.

   6. On the **Attribute Contract Fulfillment** tab, select **Adapter** for all attributes. Click **Next**.

      ![A screenshot that shows the Attribute Contract Fulfillment tab with Adapter selected for every attribute.](_images/wqg1616516794672.jpg)

   7. On the **Issuance Criteria** tab, click **Next**.

   8. On the **Summary** tab, click **Done**.

   9. On the **Browser SSO > Assertion Creation > Authentication Source Mapping** tab, click **Next**.

   10. On the **Summary** tab, click **Done**.

5. On the **Protocol Settings** tab, configure the protocol settings.

   1. Click **Configure Protocol Settings**.

   2. On the **Assertion Consumer Service URL** tab, the default URL is populated by the Contentful `metadata.xml` file. Click **Next**.

   3. On the **Allowable SAML Bindings** tab, select only **POST** and **Redirect**. Click **Next**.

   4. On the **Signature Policy** tab, clear the **Require authn requests to be signed** check box. Click **Next**.

   5. On the **Encryption Policy** tab, click **Next**

   6. On the **Summary** tab, click **Done**.

   7. On the **Browser SSO > Protocol Settings** tab, click **Next**.

   8. On the **Summary** tab, click **Done**.

6. On the **SP Connection > Browser SSO** tab, click **Next**.

---

---
title: Configuring provisioning
description: You can configure PingFederate to manage users in your Contentful organization based on the users in your datastore.
component: contentful
page_id: contentful:configuring_provisioning:pf_contentful_integration_configuring_provisioning
canonical_url: https://docs.pingidentity.com/integrations/contentful/configuring_provisioning/pf_contentful_integration_configuring_provisioning.html
revdate: June 26, 2024
section_ids:
  steps: Steps
---

# Configuring provisioning

You can configure PingFederate to manage users in your Contentful organization based on the users in your datastore.

## Steps

1. To give PingFederate access to Contentful, complete the steps in [Creating an access token in Contentful](pf_contentful_integration_creating_an_access_token_in_contentful.html).

2. To configure PingFederate for provisioning to Contentful, complete the steps in [Creating a provisioning connection](pf_contentful_integration_creating_a_provisioning_connection.html).

---

---
title: Configuring single sign-on
description: You can configure PingFederate to act as an identity provider for Contentful, allowing users to access Contentful through single sign-on (SSO).
component: contentful
page_id: contentful:configuring_single_sign-on:pf_contentful_integration_configuring_single_sign_on
canonical_url: https://docs.pingidentity.com/integrations/contentful/configuring_single_sign-on/pf_contentful_integration_configuring_single_sign_on.html
revdate: June 26, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Configuring single sign-on

You can configure PingFederate to act as an identity provider for Contentful, allowing users to access Contentful through single sign-on (SSO).

## About this task

|   |                                                                                                                                      |
| - | ------------------------------------------------------------------------------------------------------------------------------------ |
|   | SSO integration is an optional part of this integration. If you only want to configure provisioning to Contentful, skip these steps. |

## Steps

1. To allow PingFederate to check user credentials against the datastore that you created in [Enabling provisioning and single sign-on in PingFederate](../enabling_provisioning_and_single_sign-on_in_pingfederate/pf_contentful_integration_enabling_provisioning_and_single_sign_on_in_pf.html), create a password credential validator. Learn more in [Password Credential Validators](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_passwordcredentialvalidatortasklet_passwordcredentialvalidatormgmtstate.html) and [Configuring the LDAP Username Password Credential Validator](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_configure_ldap_username_pcv.html) in the PingFederate documentation.

2. To provide users with a sign-on page, complete the steps in [Creating an HTML Form Adapter instance](pf_contentful_integration_creating_an_html_form_adapter_instance.html).

3. To make it easier to create a connection to Contentful, complete the steps in [Downloading the Contentful SAML metadata file](pf_contentful_integration_downloading_the_contentful_saml_metadata_file.html).

4. To configure PingFederate for SSO to Contentful, complete the steps in [Creating a single sign-on connection](pf_contentful_integration_creating_a_single_sign_on_connection.html).

5. To make it easier to configure Contentful, complete the steps in [Exporting SAML metadata from PingFederate](pf_contentful_integration_exporting_saml_metadata_from_pf.html).

6. To configure Contentful to authorize sign-on events from PingFederate,

---

---
title: Configuring single sign-on in Contentful
description: Complete the connection by entering your PingFederate URL and certificate in Contentful.
component: contentful
page_id: contentful:configuring_single_sign-on:pf_contentful_integration_configuring_single_sign_on_in_contentful
canonical_url: https://docs.pingidentity.com/integrations/contentful/configuring_single_sign-on/pf_contentful_integration_configuring_single_sign_on_in_contentful.html
revdate: June 26, 2024
section_ids:
  steps: Steps
---

# Configuring single sign-on in Contentful

Complete the connection by entering your PingFederate URL and certificate in Contentful.

## Steps

1. On the Contentful admin console, go to **Organization settings > Single Sign-On (SSO)**.

2. In the **SSO provider** list, select **Ping Identity**.

3. In the **Single Sign-On Redirect URL** field, enter `https://pf_host:pf_port/idp/SSO.saml2`.

   For example, https\://pf.example.com:9031/idp/SSO.saml2.

4. Using a text editor, copy the contents of the `.crt` file that you downloaded in [Exporting your PingFederate signing certificate](pf_contentful_integration_exporting_your_pf_signing_certificate.html).

5. In the **X.509 Certificate** field, paste the contents of the certificate file.

   ![A screen shot that shows the Your SSO provider details section with the redirect URL and X.509 Certificate entered in.](_images/nfk1616622227694.jpg)

6. Click **Test connection**.

7. In the **SSO name** field, type a friendly name for the connection.

8. Check your settings. After enabling SSO in the next step, the only way to change your SSO settings is to contact Contentful.

9. Click **Enable SSO**.

10. **Optional:** If you want SSO to be the only sign-on method, contact Contentful and ask for [Restricted SSO](https://www.contentful.com/faq/sso/?utm_source=webapp\&utm_medium=idp-setup-form\&utm_campaign=in-app-help/). This prevents users from signing on using email or third-party services, such as GitHub, Google, or Twitter.

---

---
title: Contentful Integration Guide
description: You can integrate PingFederate with Contentful for provisioning and single sign-on (SSO). This integration uses the downloadable SCIM Connector.
component: contentful
page_id: contentful::pf_contentful_integration
canonical_url: https://docs.pingidentity.com/integrations/contentful/pf_contentful_integration.html
revdate: June 26, 2024
section_ids:
  features: Features
  intended-audience: Intended audience
  system-requirements: System requirements
---

# Contentful Integration Guide

You can integrate PingFederate with Contentful for provisioning and single sign-on (SSO). This integration uses the downloadable SCIM Connector.

## Features

* Manages users in Contentful based on changes in a datastore that is attached to PingFederate.

  * Creates and deletes users.

  * Allows you to enable the create and delete capabilities independently.

    |   |                                                                                                                                                                                |
    | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
    |   | Contentful doesn't allow attribute updates for existing users. When a user is "deleted", they are removed from the organization, but not removed from the Contentful platform. |

* Manages groups in Contentful based on changes in your datastore.

  * Creates, updates, and deletes groups.

  * Updates group memberships.

* Enables browser-based SSO initiated by the identity provider (IdP) or service provider (SP).

## Intended audience

This document is intended for PingFederate administrators.

If you need help during the setup process, refer to the following resources:

* The following sections of the PingFederate documentation:

  * General setup

    * [Datastores](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_datastores.html)

    * [SP connection management](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_sp_connect_management.html)

  * Provisioning setup

    * [Configuring outbound provisioning](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_spconnectionconfigtasklet_saasprovisioningstate.html)

    * [Configuring outbound provisioning settings](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_protocolsettingstasklet_saasglobalprovisioningsettingsstate.html)

  * SSO setup

    * [Password Credential Validators](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_passwordcredentialvalidatortasklet_passwordcredentialvalidatormgmtstate.html)

    * [Managing digital signing certificates and decryption keys](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_certmanagementtasklet_dsigsigningcert_certmanagementstate.html)

    * [Identity provider SSO configuration](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_ident_provid_sso_config.html)

* The following section of the Contentful documentation:

  * [SCIM FAQ](https://www.contentful.com/help/scim-faq/#supported-scim-features)

  * [FAQ / Single sign-on (SSO)](https://www.contentful.com/faq/sso/)

* The following sections of the SCIM Connector documentation:

  * [SCIM Provisioner](../scim/pf_scim_connector.html)

  * [Known issues and limitations](../scim/release_notes/pf_scim_connector_known_issues_and_limitations.html)

## System requirements

* PingFederate 9.0 or later.

* To allow PingFederate to make outbound HTTPS connections, you might need to allow the https\://\*.contentful.com. hostname in your firewall.

* Owner access to your Enterprise Contentful organization.

---

---
title: Creating a channel
description: Integrating PingFederate with Contentful requires a specific attribute mapping configuration.
component: contentful
page_id: contentful:configuring_provisioning:pf_contentful_integration_creating_a_channel
canonical_url: https://docs.pingidentity.com/integrations/contentful/configuring_provisioning/pf_contentful_integration_creating_a_channel.html
revdate: June 26, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Creating a channel

Integrating PingFederate with Contentful requires a specific attribute mapping configuration.

## About this task

Learn more about creating a channel in [Managing channels](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_saasmanagementtasklet_saasmanagementstate.html) in the PingFederate documentation

## Steps

1. On the **Configure Channels > Target** tab, click **Create**.

2. On the **Channel > Channel Info** tab, in the **Channel Name** field, enter a name for the channel. Click **Next**.

3. On the **Source** tab, from the **Active Data Store** list, select the data store that you created in [Enabling provisioning and single sign-on in PingFederate](../enabling_provisioning_and_single_sign-on_in_pingfederate/pf_contentful_integration_enabling_provisioning_and_single_sign_on_in_pf.html). Click **Next**.

4. On the **Source Settings** and **Source Location** tabs, complete the configuration based on your environment.

   Learn more in [Modifying source settings](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_saaschanneltasklet_saassourcesettingsstate.html) and [Specifying a source location](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_saaschanneltasklet_saassourcelocationstate.html) in the PingFederate documentation.

5. On the **Attribute Mapping** tab, configure the attributes as follows. You can use the following LDAP mappings, or adapt them for your datastore type. Click **Next**.

   Learn more about user attributes in the [Users](https://www.contentful.com/developers/docs/references/scim-api/#/reference) section of **SCIM API endpoints** in the Contentful documentation.

   | Contentful attribute | Datastore attribute |
   | -------------------- | ------------------- |
   | `userName`           | `mail`              |
   | `email`              | `mail`              |
   | `lastName`           | `sn`                |
   | `firstName`          | `givenName`         |

6. On the **Activation and Summary** tab, for the **Channel Status**, select **Active**. Click **Done**.

7. On the **Manage Channels** tab, click **Done**.

---

---
title: Creating a provisioning connection
description: To allow PingFederate to manage users in Contentful using SCIM, create a service provider (SP) connection.
component: contentful
page_id: contentful:configuring_provisioning:pf_contentful_integration_creating_a_provisioning_connection
canonical_url: https://docs.pingidentity.com/integrations/contentful/configuring_provisioning/pf_contentful_integration_creating_a_provisioning_connection.html
revdate: June 26, 2024
section_ids:
  steps: Steps
  choose-from: Choose from:
---

# Creating a provisioning connection

To allow PingFederate to manage users in Contentful using SCIM, create a service provider (SP) connection.

## Steps

1. In the PingFederate administrator console, create a new SP connection:

   ### Choose from:

   * For PingFederate 10.1 or later: go to **Applications > Integration > SP Connections**. Click **Create Connection**.

   * For PingFederate 10.0 or earlier: go to **Identity Provider > SP Connections**. Click **Create Connection**.

2. Configure the basic connection details.

   1. On the **Connection Template** tab, select **Do not use a template for this connection**. Click **Next**

   2. On the **Connection Type** tab, select only **Outbound Provisioning**. In the **Type** list, select **SCIM Connector**. Click **Next**.

   3. On the **General Info** tab, in the **Partner's Entity ID** and **Connection Name** fields, enter a name of your choosing. Complete any other optional fields. Click **Next**.

3. On the **Outbound Provisioning** tab, configure provisioning with the following details.

   Learn more in [Configuring outbound provisioning](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_spconnectionconfigtasklet_saasprovisioningstate.html) in the PingFederate documentation.

   1. Click **Configure Provisioning**.

   2. On the **Target** tab, in the **SCIM URL** field, enter the **SCIM URL** that you noted in [Creating an access token in Contentful](pf_contentful_integration_creating_an_access_token_in_contentful.html).

   3. In the **SCIM Version** list, verify that **2.0** is selected.

   4. In the **Authentication Method** list, select **OAuth 2 Bearer Token**.

   5. In the **Access Token** field, enter the access token that you noted in [Creating an access token in Contentful](pf_contentful_integration_creating_an_access_token_in_contentful.html).

      |   |                                                                                                   |
      | - | ------------------------------------------------------------------------------------------------- |
      |   | PingFederate verifies the authentication details when you activate the channel and SP connection. |

   6. In the **Unique User Identifier** list, make sure **userName** is selected.

   7. In the **Provisioning Options** section, select only **User Create** and **User Disable/Delete**.

   8. In the **Remove User Action** list, select **Delete**. Click **Next**.

      |   |                                                                                                                                                  |
      | - | ------------------------------------------------------------------------------------------------------------------------------------------------ |
      |   | This option deletes the user from your Contentful organization but not the Contentful platform. Contentful doesn't support the "disable" option. |

   9. On the **Manage Channels** tab, follow the steps in [Creating a channel](pf_contentful_integration_creating_a_channel.html).

   10. On the **Outbound Provisioning** tab, click **Next**.

4. On the **Activation and Summary** tab, above the **Summary** section, turn on the connection. Click **Save**.

---

---
title: Creating a single sign-on connection
description: To allow PingFederate to handle single sign-on (SSO) to Contentful, create a separate service provider (SP) SSO connection.
component: contentful
page_id: contentful:configuring_single_sign-on:pf_contentful_integration_creating_a_single_sign_on_connection
canonical_url: https://docs.pingidentity.com/integrations/contentful/configuring_single_sign-on/pf_contentful_integration_creating_a_single_sign_on_connection.html
revdate: June 26, 2024
section_ids:
  steps: Steps
  choose-from: Choose from:
---

# Creating a single sign-on connection

To allow PingFederate to handle single sign-on (SSO) to Contentful, create a separate service provider (SP) SSO connection.

## Steps

1. In the PingFederate administrator console, create a new SP connection:

   ### Choose from:

   * For PingFederate 10.1 or later: go to **Applications > Integration > SP Connections**. Click **Create Connection**.

   * For PingFederate 10.0 or earlier: go to **Identity Provider > SP Connections**. Click **Create Connection**.

2. On the **Connection Template** tab, select **Do not use a template for this connection**. Click **Next**.

3. On the **Connection Type** tab, select **Browser SSO Profiles**. From the **Protocol** list, select **SAML 2.0**. Click **Next**.

4. On the **Connection Options** tab, select only **Browser SSO**. Click **Next**.

5. On the **Import Metadata** tab, select **File**, and then upload the `metadata.xml` file that you downloaded in [Downloading the Contentful SAML metadata file](pf_contentful_integration_downloading_the_contentful_saml_metadata_file.html). Click **Next**.

6. If you see the **Metadata Summary** tab, click **Next**.

7. On the **General Info** tab, the basic connection information is populated by the metadata XML file. Click **Next**.

8. On the **Browser SSO** tab, complete the steps in [Configuring Browser SSO](pf_contentful_integration_configuring_browser_sso.html).

9. On the **Credentials** tab, select your signing certificate.

   1. Click **Configure Credentials**.

   2. On the **Digital Signature Settings** tab, from the **Signing Certificate** list, select the certificate that you exported in [Exporting your PingFederate signing certificate](pf_contentful_integration_exporting_your_pf_signing_certificate.html). Click **Next**.

   3. On the **Summary** tab, click **Done**.

   4. On the **SP Connection > Credentials** tab, click **Next**.

10. On the **Activation and Summary** tab, above the **Summary** section, turn on the connection. Click **Save**.

---

---
title: Downloading the Contentful SAML metadata file
description: To speed up the process of creating a service provider connection in PingFederate, download the connection details from Contentful.
component: contentful
page_id: contentful:configuring_single_sign-on:pf_contentful_integration_downloading_the_contentful_saml_metadata_file
canonical_url: https://docs.pingidentity.com/integrations/contentful/configuring_single_sign-on/pf_contentful_integration_downloading_the_contentful_saml_metadata_file.html
revdate: June 26, 2024
section_ids:
  steps: Steps
---

# Downloading the Contentful SAML metadata file

To speed up the process of creating a service provider connection in PingFederate, download the connection details from Contentful.

## Steps

1. Sign on to [Contentful](https://app.contentful.com/) as an organization administrator.

2. Go to **Organization settings > Single Sign-On (SSO)**.

   1. On the Contentful dashboard, from the **Space** menu, select **Organization settings & subscriptions**.

      ![A screen recording that shows the dashboard. The user clicks the Space menu, and then clicks Organization settings & subscriptions.](../_images/imw1616083203486.gif)

   2. From the **Access Tools** menu, select **Single Sign-On (SSO)**.

      ![A screen shot that shows the Access Tools menu.](_images/sre1616453199353.jpg)

3. On the **Single Sign-On (SSO)** window, download the Contentful `metadata.xml` file.

   ![A screen shot that shows the download icon following the page title 's service provider details.](_images/vwy1616453535738.jpg)

   |   |                                                                                                                                                                   |
   | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | Leave this page open. You'll return to it in [Configuring single sign-on in Contentful](pf_contentful_integration_configuring_single_sign_on_in_contentful.html). |

---

---
title: Enabling provisioning and single sign-on in PingFederate
description: To use PingFederate for provisioning and single sign-on, configure an external datastore and set a SAML entity ID.
component: contentful
page_id: contentful:enabling_provisioning_and_single_sign-on_in_pingfederate:pf_contentful_integration_enabling_provisioning_and_single_sign_on_in_pf
canonical_url: https://docs.pingidentity.com/integrations/contentful/enabling_provisioning_and_single_sign-on_in_pingfederate/pf_contentful_integration_enabling_provisioning_and_single_sign_on_in_pf.html
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

3. Select the **Enable Identity Provider IdP Role and Support the Following** check box.

4. Select the **SAML 2.0** and **Outbound Provisioning** check boxes. Click **Next**.

5. Click the **Federation Info** tab.

6. In the **SAML 2.0 Entity ID** field, enter a name for PingFederate to use to identify itself to SAML partners.

7. On the **Outbound Provisioning** tab, in the **Provisioner Data Store** list, select the internal database that will store the synchronization state. Click **Save**.

   Learn more in [Configuring outbound provisioning settings](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_protocolsettingstasklet_saasglobalprovisioningsettingsstate.html) in the PingFederate documentation.