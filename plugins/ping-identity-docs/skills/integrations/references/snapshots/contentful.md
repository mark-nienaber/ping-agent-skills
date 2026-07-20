---
title: Configuring Browser SSO
description: For the single sign-on (SSO) part of your connection to Contentful, use the details below.
component: contentful
page_id: contentful:configuring_single_sign-on:pf_contentful_integration_configuring_browser_sso
canonical_url: https://docs.pingidentity.com/integrations/contentful/configuring_single_sign-on/pf_contentful_integration_configuring_browser_sso.html
llms_txt: https://docs.pingidentity.com/integrations/contentful/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
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
llms_txt: https://docs.pingidentity.com/integrations/contentful/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
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
llms_txt: https://docs.pingidentity.com/integrations/contentful/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
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
llms_txt: https://docs.pingidentity.com/integrations/contentful/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
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
llms_txt: https://docs.pingidentity.com/integrations/contentful/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
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
llms_txt: https://docs.pingidentity.com/integrations/contentful/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
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
llms_txt: https://docs.pingidentity.com/integrations/contentful/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
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
llms_txt: https://docs.pingidentity.com/integrations/contentful/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
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
title: Creating an access token in Contentful
description: To allow PingFederate to access Contentful, generate an access token and get the SCIM URL.
component: contentful
page_id: contentful:configuring_provisioning:pf_contentful_integration_creating_an_access_token_in_contentful
canonical_url: https://docs.pingidentity.com/integrations/contentful/configuring_provisioning/pf_contentful_integration_creating_an_access_token_in_contentful.html
llms_txt: https://docs.pingidentity.com/integrations/contentful/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 26, 2024
section_ids:
  steps: Steps
---

# Creating an access token in Contentful

To allow PingFederate to access Contentful, generate an access token and get the SCIM URL.

## Steps

1. Sign on to [Contentful](https://app.contentful.com/) as the organization owner.

2. Go to **Organization settings > User provisioning**.

   1. On the Contentful dashboard, from the **Space** menu, select **Organization settings & subscriptions**.

      ![A screen recording that shows the dashboard. The user clicks the Space menu, and then clicks Organization settings & subscriptions.](../_images/imw1616083203486.gif)

   2. From the **Access Tools** menu, select **User provisioning**.

      ![A screen shot that shows the Access Tools menu.](_images/qgl1616443386990.jpg)

3. On the **User Provisioning** window, click **Generate personal access token**. On the **Generate Personal Access Token** modal, enter a name of your choosing. Click **Generate**.

4. Note the access token and the **SCIM URL**.

   You'll use these in [Creating a provisioning connection](pf_contentful_integration_creating_a_provisioning_connection.html).

---

---
title: Creating an HTML Form Adapter instance
description: If you don't have an existing sign-on method set up, configure a new HTML Form Adapter instance. This will allow your users to sign on to Contentful through PingFederate.
component: contentful
page_id: contentful:configuring_single_sign-on:pf_contentful_integration_creating_an_html_form_adapter_instance
canonical_url: https://docs.pingidentity.com/integrations/contentful/configuring_single_sign-on/pf_contentful_integration_creating_an_html_form_adapter_instance.html
llms_txt: https://docs.pingidentity.com/integrations/contentful/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 26, 2024
section_ids:
  steps: Steps
  choose-from: Choose from:
---

# Creating an HTML Form Adapter instance

If you don't have an existing sign-on method set up, configure a new HTML Form Adapter instance. This will allow your users to sign on to Contentful through PingFederate.

## Steps

1. In the PingFederate administrative console, create a new IdP adapter instance:

   ### Choose from:

   1. For PingFederate 10.1 or later: go to **Authentication > Integration > IdP Adapters**. Click **Create New Instance**.

   2. For PingFederate 10.0 or earlier: go to **Identity Provider > Adapters**. Click **Create New Instance**.

2. On the **Create Adapter Instances > Type** tab, set the basic adapter instance attributes.

   1. In the **Instance Name** field, enter a name for the adapter instance.

   2. In the **Instance ID** field, enter a unique identifier for the adapter instance.

   3. In the **Type** list, select **HTML Form IdP Adapter**. Click **Next**.

3. On the **IdP Adapter** tab, in the **Credential Validators** section, select your password credential validator.

   1. Click **Add new row to 'Credential Validators'**.

   2. In the list, select the password credential validator that you created in step 1 of [Configuring single sign-on](pf_contentful_integration_configuring_single_sign_on.html).

   3. Click **Update**.

4. Continue with the default **IdP Adapter** settings, or customize them based on [Configuring an HTML Form Adapter instance](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_config_html_form_adapt_instance.html) in the PingFederate documentation. Click **Next**.

5. On the **Extended Contract** tab, add attributes the following attributes, or the equivalent for your datastore. Click **Next**.

   * `givenName`

   * `mail`

   * `sn`

6. On the **Adapter Attributes** tab, for **username**, select **Pseudonym**. Click **Next**.

7. On the **Adapter Contract Mapping** tab, click **Next**.

8. On the **Summary** tab, click **Done**.

---

---
title: Deploying the integration files
description: To get started with the integration, deploy the SCIM Connector files to your PingFederate directory.
component: contentful
page_id: contentful::pf_contentful_integration_deploying_the_integration_files
canonical_url: https://docs.pingidentity.com/integrations/contentful/pf_contentful_integration_deploying_the_integration_files.html
llms_txt: https://docs.pingidentity.com/integrations/contentful/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 26, 2024
section_ids:
  steps: Steps
---

# Deploying the integration files

To get started with the integration, deploy the SCIM Connector files to your PingFederate directory.

## Steps

1. Download the SCIM Connector `.zip` archive from the [**Add-ons** tab of the PingFederate downloads page](https://www.pingidentity.com/en/resources/downloads/pingfederate.html) or the [Ping Identity Marketplace](https://marketplace.pingone.com/item/scim-provisioner).

2. Stop PingFederate.

3. If you're upgrading an existing deployment, delete the `pf-scim-quickconnection-<version>.jar` file from your `<pf_install>/pingfederate/server/default/deploy` directory.

4. Extract the `.zip` archive and merge the contents of the `dist` directory with your `<pf_install>/pingfederate` directory.

5. Enable the PingFederate provisioning engine:

   1. Open your `<pf_install>/pingfederate/bin/run.properties` file.

   2. Change `pf.provisioner.mode` to `STANDALONE`. Save the file.

      |   |                                                                                                                                                                                                                                             |
      | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      |   | To configure the `FAILOVER` mode instead, refer to [Deploying provisioning failover](https://docs.pingidentity.com/pingfederate/latest/server_clustering_guide/pf_deploy_provis_failover.html) in the PingFederate Server Clustering Guide. |

6. Start PingFederate.

7. If you operate PingFederate in a cluster, repeat steps 2 - 4 and step 6 for each engine node.

---

---
title: Downloading the Contentful SAML metadata file
description: To speed up the process of creating a service provider connection in PingFederate, download the connection details from Contentful.
component: contentful
page_id: contentful:configuring_single_sign-on:pf_contentful_integration_downloading_the_contentful_saml_metadata_file
canonical_url: https://docs.pingidentity.com/integrations/contentful/configuring_single_sign-on/pf_contentful_integration_downloading_the_contentful_saml_metadata_file.html
llms_txt: https://docs.pingidentity.com/integrations/contentful/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
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
llms_txt: https://docs.pingidentity.com/integrations/contentful/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
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

---

---
title: Enabling provisioning and single sign-on in PingFederate 10.0 or earlier
description: In the PingFederate administrative console, configure the datastore for PingFederate to use as the source of user data.
component: contentful
page_id: contentful:enabling_provisioning_and_single_sign-on_in_pingfederate:pf_contentful_integration_enabling_provisioning_and_single_sign_on_in_pf_100_or_earlier
canonical_url: https://docs.pingidentity.com/integrations/contentful/enabling_provisioning_and_single_sign-on_in_pingfederate/pf_contentful_integration_enabling_provisioning_and_single_sign_on_in_pf_100_or_earlier.html
llms_txt: https://docs.pingidentity.com/integrations/contentful/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 26, 2024
section_ids:
  steps: Steps
---

# Enabling provisioning and single sign-on in PingFederate 10.0 or earlier

## Steps

1. In the PingFederate administrative console, configure the datastore for PingFederate to use as the source of user data.

   Learn more in [Datastores](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_datastores.html) in the PingFederate documentation.

2. Go to **System > Protocol Settings > Roles & Protocols**.

3. Select the **Enable Identity Provider IdP Role and Support the Following** check box.

4. Select the **SAML 2.0** and **Outbound Provisioning** check boxes. Click **Next**.

5. Click the **Federation Info** tab.

6. In the **SAML 2.0 Entity ID** field, enter a name for PingFederate to use to identify itself to SAML partners.

7. On the **Outbound Provisioning** tab, in the **Provisioner Data Store** list, select the internal database that will store the synchronization state. Click **Save**.

   Learn more in [Configuring outbound provisioning settings](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_protocolsettingstasklet_saasglobalprovisioningsettingsstate.html) in the PingFederate documentation.

---

---
title: Enabling provisioning and single sign-on in PingFederate 10.1 or later
description: In the PingFederate administrative console, configure the datastore for PingFederate to use as the source of user data.
component: contentful
page_id: contentful:enabling_provisioning_and_single_sign-on_in_pingfederate:pf_contentful_integration_enabling_provisioning_and_single_sign_on_in_pf_101_or_later
canonical_url: https://docs.pingidentity.com/integrations/contentful/enabling_provisioning_and_single_sign-on_in_pingfederate/pf_contentful_integration_enabling_provisioning_and_single_sign_on_in_pf_101_or_later.html
llms_txt: https://docs.pingidentity.com/integrations/contentful/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 26, 2024
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
title: Exporting SAML metadata from PingFederate
description: Export a metadata file that describes your PingFederate identity provider configuration.
component: contentful
page_id: contentful:configuring_single_sign-on:pf_contentful_integration_exporting_saml_metadata_from_pf
canonical_url: https://docs.pingidentity.com/integrations/contentful/configuring_single_sign-on/pf_contentful_integration_exporting_saml_metadata_from_pf.html
llms_txt: https://docs.pingidentity.com/integrations/contentful/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
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

1. In the PingFederate administrative console, go to the **Metadata Export** page.

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
title: Exporting your PingFederate signing certificate
description: To allow Contentful to trust communications from PingFederate, you need to provide the signing certificate that you'll use in your connection.
component: contentful
page_id: contentful:configuring_single_sign-on:pf_contentful_integration_exporting_your_pf_signing_certificate
canonical_url: https://docs.pingidentity.com/integrations/contentful/configuring_single_sign-on/pf_contentful_integration_exporting_your_pf_signing_certificate.html
llms_txt: https://docs.pingidentity.com/integrations/contentful/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 26, 2024
section_ids:
  steps: Steps
---

# Exporting your PingFederate signing certificate

To allow Contentful to trust communications from PingFederate, you need to provide the signing certificate that you'll use in your connection.

## Steps

1. In the PingFederate administrative console, go to **Security > Signing & Decryption Keys & Certificates**.

2. If you don't have a signing certificate, create one.

   1. Click **Create New**.

   2. On the **Create Certificate** tab, enter the certificate details. Click **Next**.

      Learn more in the **Creating new certificates** section of [Managing digital signing certificates and decryption keys](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_certmanagementtasklet_dsigsigningcert_certmanagementstate.html) in the PingFederate documentation.

   3. On the **Summary** tab, click **Save**.

3. In the **Action** column for the certificate that you want to use for your connection, click **Export**.

4. On the **Export Certificate** tab, select **Certificate only**. Click **Next**.

5. On the **Export & Summary** tab, click **Export**.

6. Save the `.crt` file.

   You'll use the contents of this file in [Configuring single sign-on in Contentful](pf_contentful_integration_configuring_single_sign_on_in_contentful.html).

7. Click **Done**.

---

---
title: Upgrading an existing deployment
description: If you're upgrading from a previous version of the SCIM Connector, note your existing service provider (SP) connection configuration and create a new connection.
component: contentful
page_id: contentful:upgrading_an_existing_deployment:pf_contentful_integration_upgrading_an_existing_deployment
canonical_url: https://docs.pingidentity.com/integrations/contentful/upgrading_an_existing_deployment/pf_contentful_integration_upgrading_an_existing_deployment.html
llms_txt: https://docs.pingidentity.com/integrations/contentful/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 26, 2024
section_ids:
  upgrading-an-existing-deployment-in-pingfederate-10-1-or-later: Upgrading an existing deployment in PingFederate 10.1 or later
  steps: Steps
  upgrading-an-existing-deployment-in-pingfederate-10-0-or-earlier: Upgrading an existing deployment in PingFederate 10.0 or earlier
  steps-2: Steps
---

# Upgrading an existing deployment

If you're upgrading from a previous version of the SCIM Connector, note your existing service provider (SP) connection configuration and create a new connection.

## Upgrading an existing deployment in PingFederate 10.1 or later

### Steps

1. Back up your current PingFederate configuration as shown in [Configuration archive](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_configurationarchivetasklet_selectimportexportstate.html) in the PingFederate documentation.

2. In the PingFederate administrative console, go to **Applications > Integration > SP Connections** and select your connection.

3. Note the attribute mappings for your existing SP connection.

   Learn more in [Mapping attributes](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_saaschanneltasklet_saasattrmappingmgmtstate.html) in the PingFederate documentation.

4. Delete your existing SP connection.

   1. Go to **Applications > Integration > SP Connections**.

   2. For your existing connection, click **Select action**, and then click **Delete**. Click **Confirm.**

5. Complete the steps in [Deploying the integration files](../pf_contentful_integration_deploying_the_integration_files.html).

6. Complete the steps in [Creating a provisioning connection](../configuring_provisioning/pf_contentful_integration_creating_a_provisioning_connection.html).

   * From **Outbound Provisioning > Manage Channels > Channel**, on the **Attribute Mapping** tab, configure the attribute mappings based on your notes.

7. (Optional) Complete the steps in [Creating a single sign-on connection](../configuring_single_sign-on/pf_contentful_integration_creating_a_single_sign_on_connection.html).

## Upgrading an existing deployment in PingFederate 10.0 or earlier

### Steps

1. Back up your current PingFederate configuration as shown in [Configuration archive](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_configurationarchivetasklet_selectimportexportstate.html) in the PingFederate documentation.

2. In the PingFederate administrative console, go to **Identity Provider > SP Connections** and select your connection.

3. Note the attribute mappings for your existing SP connection.

   Learn more in [Mapping attributes](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_saaschanneltasklet_saasattrmappingmgmtstate.html) in the PingFederate documentation.

4. Delete your existing SP connection.

   1. Go to **Identity Provider > SP Connections > Manage All**.

   2. For your existing connection, click **Select action**, and then click **Delete**. Click **Save.**

5. Complete the steps in [Deploying the integration files](../pf_contentful_integration_deploying_the_integration_files.html).

6. Complete the steps in [Creating a provisioning connection](../configuring_provisioning/pf_contentful_integration_creating_a_provisioning_connection.html).

   * From **Outbound Provisioning > Manage Channels > Channel**, on the **Attribute Mapping** tab, configure the attribute mappings based on your notes.

7. (Optional) Complete the steps in [Creating a single sign-on connection](../configuring_single_sign-on/pf_contentful_integration_creating_a_single_sign_on_connection.html).

---

---
title: Upgrading an existing deployment in PingFederate 10.0 or earlier
description: Back up your current PingFederate configuration as shown in Configuration archive in the PingFederate documentation.
component: contentful
page_id: contentful:upgrading_an_existing_deployment:pf_contentful_integration_upgrading_an_existing_deployment_in_pf_100_or_earlier
canonical_url: https://docs.pingidentity.com/integrations/contentful/upgrading_an_existing_deployment/pf_contentful_integration_upgrading_an_existing_deployment_in_pf_100_or_earlier.html
llms_txt: https://docs.pingidentity.com/integrations/contentful/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 26, 2024
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

5. Complete the steps in [Deploying the integration files](../pf_contentful_integration_deploying_the_integration_files.html).

6. Complete the steps in [Creating a provisioning connection](../configuring_provisioning/pf_contentful_integration_creating_a_provisioning_connection.html).

   * From **Outbound Provisioning > Manage Channels > Channel**, on the **Attribute Mapping** tab, configure the attribute mappings based on your notes.

7. (Optional) Complete the steps in [Creating a single sign-on connection](../configuring_single_sign-on/pf_contentful_integration_creating_a_single_sign_on_connection.html).

---

---
title: Upgrading an existing deployment in PingFederate 10.1 or later
description: Back up your current PingFederate configuration as shown in Configuration archive in the PingFederate documentation.
component: contentful
page_id: contentful:upgrading_an_existing_deployment:pf_contentful_integration_upgrading_an_existing_deployment_in_pf_101_or_later
canonical_url: https://docs.pingidentity.com/integrations/contentful/upgrading_an_existing_deployment/pf_contentful_integration_upgrading_an_existing_deployment_in_pf_101_or_later.html
llms_txt: https://docs.pingidentity.com/integrations/contentful/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 26, 2024
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

5. Complete the steps in [Deploying the integration files](../pf_contentful_integration_deploying_the_integration_files.html).

6. Complete the steps in [Creating a provisioning connection](../configuring_provisioning/pf_contentful_integration_creating_a_provisioning_connection.html).

   * From **Outbound Provisioning > Manage Channels > Channel**, on the **Attribute Mapping** tab, configure the attribute mappings based on your notes.

7. (Optional) Complete the steps in [Creating a single sign-on connection](../configuring_single_sign-on/pf_contentful_integration_creating_a_single_sign_on_connection.html).