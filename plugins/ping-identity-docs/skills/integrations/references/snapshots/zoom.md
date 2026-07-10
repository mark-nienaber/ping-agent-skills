---
title: Add the Zoom metadata URL in PingFederate
description: To provide PingFederate with information about Zoom as a SAML partner, register the Zoom metadata URL.
component: zoom
page_id: zoom:setup:pf_zoom_connector_add_zoom_metadata
canonical_url: https://docs.pingidentity.com/integrations/zoom/setup/pf_zoom_connector_add_zoom_metadata.html
llms_txt: https://docs.pingidentity.com/integrations/zoom/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 5, 2025
section_ids:
  steps: Steps
---

# Add the Zoom metadata URL in PingFederate

To provide PingFederate with information about Zoom as a SAML partner, register the Zoom metadata URL.

## Steps

1. On the PingFederate administrative console, on the **Security > Partner Metadata URLs** tab, click **Add New URL**.

2. On the **URL** tab, in the **Name** field, enter a name.

3. In the **URL** field, enter `https://your_vanity_url.zoom.us/saml/metadata/sp`. Click **Load Metadata**, then **Next**.

4. On the **Certificate Summary** tab, click **Next**.

5. On the **Summary** tab, click **Done**.

6. On the **Partner Metadata URLs** tab, click **Save**.

---

---
title: Changelog
description: The following is the change history for the Zoom Provisioner.
component: zoom
page_id: zoom:release_notes:pf_zoom_connector_changelog
canonical_url: https://docs.pingidentity.com/integrations/zoom/release_notes/pf_zoom_connector_changelog.html
llms_txt: https://docs.pingidentity.com/integrations/zoom/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 5, 2025
section_ids:
  zoom-provisioner-1-3-june-2023: Zoom Provisioner 1.3 - June 2023
  zoom-provisioner-1-2-december-2022: Zoom Provisioner 1.2 - December 2022
  zoom-provisioner-1-0-march-2020: Zoom Provisioner 1.0 - March 2020
---

# Changelog

The following is the change history for the Zoom Provisioner.

## Zoom Provisioner 1.3 - June 2023

Added support for server-to-server OAuth apps, because JWT apps are being deprecated and won't be supported after September 1, 2023.

## Zoom Provisioner 1.2 - December 2022

Added the ability to restore a user's license when the user is re-enabled. Updating the license is no longer required.

## Zoom Provisioner 1.0 - March 2020

* Initial release

* Added support for user provisioning

* Added support for Zoom attributes

* Added support for API key and secret authentication

* Added configuration options for create, update, and disable/delete capabilities

* Added configuration options for deprovisioning actions

---

---
title: Configuring single sign-on
description: To allow PingFederate to act as an identity provider for Zoom, enable single sign-on (SSO) in PingFederate and Zoom, then create a connection.
component: zoom
page_id: zoom:setup:pf_zoom_connector_configuring_single_sign_on
canonical_url: https://docs.pingidentity.com/integrations/zoom/setup/pf_zoom_connector_configuring_single_sign_on.html
llms_txt: https://docs.pingidentity.com/integrations/zoom/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 5, 2025
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Configuring single sign-on

To allow PingFederate to act as an identity provider for Zoom, enable single sign-on (SSO) in PingFederate and Zoom, then create a connection.

## About this task

|   |                                                                                                                                                      |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Single sign-on integration is an optional part of this integration. If you only want to use the Zoom Provisioner for provisioning, skip these steps. |

## Steps

1. Complete the steps in [Enabling provisioning and single sign-on in PingFederate](pf_zoom_connector_enabling_provisioning_and_single_sign_on_in_pf.html).

2. Complete the steps in [Configuring single sign-on in Zoom](pf_zoom_connector_configuring_single_sign_on_in_zoom.html).

3. Complete the steps in [Add the Zoom metadata URL in PingFederate](pf_zoom_connector_add_zoom_metadata.html).

4. Complete the steps in [Creating a single sign-on connection](pf_zoom_connector_creating_a_single_sign_on_connection.html).

---

---
title: Configuring single sign-on in Zoom
description: To allow PingFederate to manage authentication, enable single sign-on (SSO) in Zoom.
component: zoom
page_id: zoom:setup:pf_zoom_connector_configuring_single_sign_on_in_zoom
canonical_url: https://docs.pingidentity.com/integrations/zoom/setup/pf_zoom_connector_configuring_single_sign_on_in_zoom.html
llms_txt: https://docs.pingidentity.com/integrations/zoom/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 5, 2025
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Configuring single sign-on in Zoom

To allow PingFederate to manage authentication, enable single sign-on (SSO) in Zoom.

## About this task

You can find more information in [Getting Started with SSO](https://support.zoom.us/hc/en-us/articles/201363003-Getting-Started-with-SSO) in the Zoom documentation.

## Steps

1. Sign on to the Zoom [Single sign-on](https://zoom.us/account/sso) page as an administrator.

2. Click **Enable Single Sign-On**.

3. In the **Sign-in page URL** field, enter `https://pf_host:pf_port/idp/SSO.saml2`.

4. (Optional) In the **Sign-out page URL** field, enter `https://pf_host:pf_port/idp/SLO.saml2`.

5. In the **Identity Provider Certificate** field, enter the contents of your PingFederate signing certificate, without the `Begin Certificate` and `End Certificate` lines.

   To get your certificate, refer to the **Exporting a certificate** section in [Managing digital signing certificates and decryption keys](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_certmanagementtasklet_dsigsigningcert_certmanagementstate.html) in the PingFederate documentation.

6. Note the **Service Provider (SP) Entity ID** for use in [Creating a single sign-on connection](pf_zoom_connector_creating_a_single_sign_on_connection.html).

7. In the **Issuer (IDP Entity ID)** field, enter the **SAML 2.0 Entity ID** that you created in [Enabling provisioning and single sign-on in PingFederate](pf_zoom_connector_enabling_provisioning_and_single_sign_on_in_pf.html).

8. In the **Binding** list, select a method.

9. In the **Signature Hash Algorithm** section, click **SHA-256**.

10. In the **Security** section, select **Sign SAML request** and **Save SAML response logs on user sign-in**.

11. In the **Provision User** list, select **Prior to Sign-In**. Click **Save Changes**.

---

---
title: Creating a provisioning connection
description: To allow PingFederate to manage users in Zoom, create a service provider (SP) connection.
component: zoom
page_id: zoom:setup:pf_zoom_connector_creating_a_provisioning_connection
canonical_url: https://docs.pingidentity.com/integrations/zoom/setup/pf_zoom_connector_creating_a_provisioning_connection.html
llms_txt: https://docs.pingidentity.com/integrations/zoom/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 5, 2025
section_ids:
  steps: Steps
---

# Creating a provisioning connection

To allow PingFederate to manage users in Zoom, create a service provider (SP) connection.

## Steps

1. In the PingFederate administrator console, create a new SP connection:

   Choose from:

   * For PingFederate 10.1 or later, go to **Applications > Integration > SP Connections**. Click **Create Connection**.

   * For PingFederate 10.0 or earlier, go to **Identity Provider > SP Connections**. Click **Create Connection**.

2. Configure the basic connection details with the Zoom quick connection template:

   1. On the **Connection Template** tab, select **Use a template for this connection**.

   2. In the **Connection Template** list, select **Zoom Provisioner**.

   3. On the **Metadata File** row, select the `zoom-saml-metadata.xml` file you modified in [Getting a vanity URL for Zoom](pf_zoom_connector_getting_a_vanity_url_for_zoom.html). Click **Next**.

   4. On the **Connection Type** tab select only **Outbound Provisioning**. Click **Next**.

   5. On the **Connection Options** tab, click **Next**.

   6. On the **General Info** tab, in the **Connection Name** field, enter a name for the connection. Click **Next**.

3. On the **Outbound Provisioning** tab, configure the provisioning target and channel as shown in [Configuring outbound provisioning](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_spconnectionconfigtasklet_saasprovisioningstate.html) in the PingFederate documentation.

   1. Click **Configure Provisioning**.

   2. On the **Target** tab, enter the account ID, client ID, and client secret noted in step 4.

      |   |                                                                                           |
      | - | ----------------------------------------------------------------------------------------- |
      |   | PingFederate verifies the configurations when you activate the channel and SP connection. |

   3. Under **Provisioning Options**, customize the provisioning connector actions as shown in [Provisioning options reference](pf_zoom_connector_provisioning_options_reference.html). Click **Next**.

   4. On the **Manage Channels** tab, create a channel as shown in [Managing channels](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_saasmanagementtasklet_saasmanagementstate.html) in the PingFederate documentation. Click **Done**.

      |   |                                                                                                                                                                                        |
      | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      |   | You can find more information about the attributes available in your channel configuration in [Supported attributes reference](pf_zoom_connector_supported_attributes_reference.html). |

   5. On the **Outbound Provisioning** tab, click **Next**.

4. On the **Activation and Summary** tab, above the **Summary** section, turn on the connection. Click **Save**.

---

---
title: Creating a single sign-on connection
description: To allow PingFederate to handle authentication for Zoom, create a service provider (SP) connection.
component: zoom
page_id: zoom:setup:pf_zoom_connector_creating_a_single_sign_on_connection
canonical_url: https://docs.pingidentity.com/integrations/zoom/setup/pf_zoom_connector_creating_a_single_sign_on_connection.html
llms_txt: https://docs.pingidentity.com/integrations/zoom/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 5, 2025
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Creating a single sign-on connection

To allow PingFederate to handle authentication for Zoom, create a service provider (SP) connection.

## About this task

|   |                                                                                                           |
| - | --------------------------------------------------------------------------------------------------------- |
|   | You can follow these steps to create a new SP connection, or you can modify your provisioning connection. |

## Steps

1. In the PingFederate administrator console, create a new SP connection:

   Choose from:

   * For PingFederate 10.1 or later, go to **Applications > Integration > SP Connections**. Click **Create Connection**.

   * For PingFederate 10.0 or earlier, go to **Identity Provider > SP Connections**. Click **Create Connection**.

2. Configure the basic connection details with the Zoom quick connection template:

   1. On the **Connection Template** tab, select **Use a template for this connection**.

   2. In the **Connection Template** list, select **Zoom Provisioner**.

   3. On the **Metadata File** row, select the `zoom-saml-metadata.xml` file you modified in [Getting a vanity URL for Zoom](pf_zoom_connector_getting_a_vanity_url_for_zoom.html). Click **Next**.

   4. On the **Connection Type** tab select **Browser SSO Profiles**. Click **Next**.

   5. On the **Connection Options** tab, select only **Browser SSO**. Click **Next**.

   6. If you see the **Metadata URL** tab, clear the **Enable automatic reloading** checkbox. Click **Next**.

   7. On the **General Info** tab, in the **Connection Name** field, enter a name for your connection. Click **Next**.

3. On the **Browser SSO** tab, configure browser SSO.

   You can find a complete guide in [Configure IdP Browser SSO](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_spconnectionconfigtasklet_spbrowserssostate.html) in the PingFederate documentation.

   1. On **Browser SSO > SAML Profiles**, select all four checkboxes.

   2. On **Browser SSO > Protocol Settings > SLO Service URLs**, in the **Binding** list, select the method you chose for **Binding** in [Configuring single sign-on in Zoom](pf_zoom_connector_configuring_single_sign_on_in_zoom.html).

      1. In the **Endpoint URL** and **Response URL** fields, enter `/saml/SingleLogout`. Click **Add**.

   3. On **Browser SSO > Protocol Settings > Allowable SAML Bindings**, select the method that you chose for **Binding** in [Configuring single sign-on in Zoom](pf_zoom_connector_configuring_single_sign_on_in_zoom.html).

4. On the **Credentials** tab, configure the connection credentials. In the **Signing Algorithm** list, select **RSA SHA256**. Click **Next**.

   You can find a complete guide in [Configure credentials](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_spconnectionconfigtasklet_credentialsstate.html) in the PingFederate documentation.

5. On the **Activation and Summary** tab, above the **Summary** section, turn on the connection. Click **Save**.

---

---
title: Creating a Zoom app
description: To integrate PingFederate with Zoom, add it as a server-to-server OAuth app.
component: zoom
page_id: zoom:setup:pf_zoom_connector_creating_an_app_in_zoom
canonical_url: https://docs.pingidentity.com/integrations/zoom/setup/pf_zoom_connector_creating_an_app_in_zoom.html
llms_txt: https://docs.pingidentity.com/integrations/zoom/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 5, 2025
section_ids:
  steps: Steps
  result: Result:
  result-2: Result:
---

# Creating a Zoom app

To integrate PingFederate with Zoom, add it as a server-to-server OAuth app.

## Steps

1. Go to the [Zoom App Marketplace](https://marketplace.zoom.us).

2. In the top right corner of the screen, click the **Develop** list and select **Build App**.

   ### Result:

   The **Choose your app type** page displays.

   ![Screen capture of the Choose your app type page.](_images/choose_your_app_type.png)

3. On the **Server-to-Server OAuth** app type tile, click **Create**.

4. In the **App Name** field, enter the name of the app. Click **Create**.

   ### Result:

   The account ID, client ID, and client secret for your new application display on the **App credentials** tab. Remember where this information is stored, as you'll need it to create a provisioning connection.

5. On the **Information** tab, add information about your app.

   For example, create a meaningful short description.

6. Enter the company name.

   |   |                                                   |
   | - | ------------------------------------------------- |
   |   | This information is required to activate the app. |

7. In the **Developer Contact Information** section, enter your name and email address in the appropriate fields. Click **Continue**.

8. On the **Feature** tab, click the toggle to enable the features you want, then click **Continue**.

   For example, add events, team chats, and multi-platform support.

9. On the **Scopes** tab, click **Add Scopes** and select the following scopes:

   * User scopes

     * **user:master**: Allows the app to view and manage sub account user information.

     * **user:read:admin**: Allows the app to view information for all users in a Zoom account. For example, profile information, user settings, user permissions, and the user's scheduling privileges.

     * **user:write:admin**: Allows the app to view and manage user profile information, such as settings and permissions.

   * Account scopes

     * **account:master**: Allows the app to view and manage sub accounts.

     * **account:read:admin**: Allows an app to view account and sub account information. This includes account settings, account lock settings, managed domains, and the account's trusted domains.

     * **account:write:admin**: Allows an app to manage sub accounts on behalf of a master account. This includes creating or disassociating a sub account from a master account, updating an account's owner or account settings, and updating lock settings.

   * SCIM2 scope

     * **scim2**: Allows an app to provide support for provisioning support.

10. After you're finished, click **Done**.

11. Go to the **Activation** tab and click **Activate your app**.

---

---
title: Deploying the integration files
description: To get started with the integration, deploy the Zoom Provisioner files to your PingFederate directory.
component: zoom
page_id: zoom:setup:pf_zoom_connector_deploying_the_integration_files
canonical_url: https://docs.pingidentity.com/integrations/zoom/setup/pf_zoom_connector_deploying_the_integration_files.html
llms_txt: https://docs.pingidentity.com/integrations/zoom/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 5, 2025
section_ids:
  steps: Steps
---

# Deploying the integration files

To get started with the integration, deploy the Zoom Provisioner files to your PingFederate directory.

## Steps

1. Download the Zoom Provisioner `.zip` archive from the [**Add-ons** tab of the PingFederate downloads page](https://www.pingidentity.com/en/resources/downloads/pingfederate.html) or the [Ping Identity Marketplace](https://marketplace.pingone.com/item/zoom-single-signon-integration).

2. Stop PingFederate.

3. If you're upgrading an existing deployment, delete the `pf-zoom-quickconnection-<version>.jar` file from your `<pf_install>/pingfederate/server/default/deploy` directory.

4. Extract the `.zip` archive and merge the contents of the `dist` directory with your `<pf_install>/pingfederate/server/default/deploy` directory.

5. Enable the PingFederate provisioning engine:

   1. Open your `<pf_install>/pingfederate/bin/run.properties` file.

   2. Change `pf.provisioner.mode` to `STANDALONE`. Save the file.

      |   |                                                                                                                                                                                                                                                  |
      | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
      |   | To configure the `FAILOVER` mode instead, learn more in [Deploying provisioning failover](https://docs.pingidentity.com/pingfederate/latest/server_clustering_guide/pf_deploy_provis_failover.html) in the PingFederate server clustering guide. |

6. Start PingFederate.

7. If you operate PingFederate in a cluster, repeat steps 2 - 4 and step 6 for each engine node.

---

---
title: Download manifest
description: The following files are included in the Zoom Provisioner .zip archive:
component: zoom
page_id: zoom:release_notes:pf_zoom_connector_download_manifest
canonical_url: https://docs.pingidentity.com/integrations/zoom/release_notes/pf_zoom_connector_download_manifest.html
llms_txt: https://docs.pingidentity.com/integrations/zoom/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 5, 2025
---

# Download manifest

The following files are included in the Zoom Provisioner `.zip` archive:

* `legal/Legal.pdf`: Copyright and license information.

* `dist`: Contains the integration files.

  * `pf-zoom-quickconnection-<version>.jar`: The Zoom Provisioner quick connection template.

* `zoom-saml-metadata.xml`: A modifiable metadata file used to create the connection.

---

---
title: Enabling provisioning and single sign-on in PingFederate
description: To use PingFederate for provisioning and single sign-on, configure an external datastore and set a SAML entity ID.
component: zoom
page_id: zoom:setup:pf_zoom_connector_enabling_provisioning_and_single_sign_on_in_pf
canonical_url: https://docs.pingidentity.com/integrations/zoom/setup/pf_zoom_connector_enabling_provisioning_and_single_sign_on_in_pf.html
llms_txt: https://docs.pingidentity.com/integrations/zoom/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 5, 2025
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

   You can find help in [Datastores](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_datastores.html) in the PingFederate documentation.

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
component: zoom
page_id: zoom:setup:pf_zoom_connector_enabling_provisioning_and_single_sign_on_in_pf_100_or_earlier
canonical_url: https://docs.pingidentity.com/integrations/zoom/setup/pf_zoom_connector_enabling_provisioning_and_single_sign_on_in_pf_100_or_earlier.html
llms_txt: https://docs.pingidentity.com/integrations/zoom/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 5, 2025
section_ids:
  steps: Steps
---

# Enabling provisioning and single sign-on in PingFederate 10.0 or earlier

## Steps

1. In the PingFederate administrative console, configure the datastore for PingFederate to use as the source of user data.

   You can find help in [Datastores](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_datastores.html) in the PingFederate documentation.

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
component: zoom
page_id: zoom:setup:pf_zoom_connector_enabling_provisioning_and_single_sign_on_in_pf_101_or_later
canonical_url: https://docs.pingidentity.com/integrations/zoom/setup/pf_zoom_connector_enabling_provisioning_and_single_sign_on_in_pf_101_or_later.html
llms_txt: https://docs.pingidentity.com/integrations/zoom/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 5, 2025
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
title: Getting a vanity URL for Zoom
description: Before you can integrate with Zoom, you need to apply for a custom Zoom URL for your organization and add it to your connection metadata file.
component: zoom
page_id: zoom:setup:pf_zoom_connector_getting_a_vanity_url_for_zoom
canonical_url: https://docs.pingidentity.com/integrations/zoom/setup/pf_zoom_connector_getting_a_vanity_url_for_zoom.html
llms_txt: https://docs.pingidentity.com/integrations/zoom/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 5, 2025
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Getting a vanity URL for Zoom

Before you can integrate with Zoom, you need to apply for a custom Zoom URL for your organization and add it to your connection metadata file.

## About this task

|   |                                                                          |
| - | ------------------------------------------------------------------------ |
|   | Zoom typically takes 1 - 2 business days to process vanity URL requests. |

## Steps

1. Sign on to the Zoom [Account Profile](https://zoom.us/account) page as an administrator.

2. In the **Vanity URL** section, click **Apply**.

3. On the **Apply for Vanity URL** dialog, enter a URL following the [Guidelines for Vanity URL Requests](https://support.zoom.us/hc/en-us/articles/215062646-Guidelines-for-Vanity-URL-Requests) in the Zoom documentation. Click **Apply**.

4. After your request is approved, copy the vanity URL to the `.xml` metadata file used to configure the connection in PingFederate:

   1. In a text editor, open the `zoom-saml-metadata.xml` file included in the integration `.zip` file.

   2. In the `.xml` file, replace every instance of *https\://your\_vanity\_url.zoom.us* with the vanity URL that you requested.

   3. Save the changes.

   You will use this file in [Creating a single sign-on connection](pf_zoom_connector_creating_a_single_sign_on_connection.html).

---

---
title: Known issues and limitations
description: The following are known issues or limitations with the Zoom Provisioner.
component: zoom
page_id: zoom:release_notes:pf_zoom_connector_known_issues_and_limitations
canonical_url: https://docs.pingidentity.com/integrations/zoom/release_notes/pf_zoom_connector_known_issues_and_limitations.html
llms_txt: https://docs.pingidentity.com/integrations/zoom/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 5, 2025
section_ids:
  known-issues: Known issues
  known-limitations: Known limitations
---

# Known issues and limitations

The following are known issues or limitations with the Zoom Provisioner.

## Known issues

There aren't any known issues.

## Known limitations

* This integration doesn't support group provisioning.

* When an LDAP user is deleted in a targeted group distinguished name (DN), the provisioning connector doesn't propagate the deletion until a new user is added to the group. This limitation is compounded when the **User Create** provisioning option is disabled. You can find solutions in [SaaS provisioner does not remove the user](https://support.pingidentity.com/s/article/After-deleting-an-AD-user-account-SaaS-provisioner-does-not-remove-the-user-in-the-next-provisioning-cycle-when-Group-DN-is-specified) in the Ping Identity Knowledge Base.

* Because of PingFederate limitations, user attributes cannot be cleared once set.

* Zoom only allows a single value for the `Roles` attribute.

* Zoom doesn't allow users with the admin role to be disabled or deleted. Change the user's role first.

* Because of a limitation in Zoom, if a user's attributes change at the same time they're enabled or disabled, only the `disabled` status is updated in Zoom. The attributes are updated the next time a change is made to that user.

---

---
title: Provisioning options reference
description: The following table lists the main provisioning capabilities available in the Zoom connection configuration.
component: zoom
page_id: zoom:setup:pf_zoom_connector_provisioning_options_reference
canonical_url: https://docs.pingidentity.com/integrations/zoom/setup/pf_zoom_connector_provisioning_options_reference.html
llms_txt: https://docs.pingidentity.com/integrations/zoom/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 5, 2025
---

# Provisioning options reference

The following table lists the main provisioning capabilities available in the Zoom connection configuration.

| Field Name                                                                                                                                                       | Description                                                                                                                                                                                                                                                                                                                                                        |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **User Create**                                                                                                                                                  | * **Selected** (default)

  PingFederate creates users in Zoom.

* **Cleared**

  PingFederate doesn't create users in Zoom.                                                                                                                                                                                                                                       |
| **User Update**                                                                                                                                                  | - **Selected** (default)

  PingFederate updates existing users in Zoom. PingFederate can also re-enable disabled users in Zoom.

- **Cleared**

  PingFederate doesn't update existing users in Zoom.                                                                                                                                                             |
| **User Disable / Delete**                                                                                                                                        | * **Selected** (default)

  PingFederate removes users in Zoom according to the **Remove User Action** setting.

* **Cleared**

  PingFederate doesn't disable or delete users in Zoom.                                                                                                                                                                            |
| &#xA;&#xA;If any of the previous options are cleared, PingFederate logs a warning in the user workflow section of provisioner.log when the related action fails. |                                                                                                                                                                                                                                                                                                                                                                    |
| **Remove User Action**                                                                                                                                           | This option applies when **User Disable / Delete** is selected, and either:- A previously-provisioned user no longer meets the condition set on the **Source Location** tab

- A user has been disabled or deleted from the datastore.* **Disable** (default)

  PingFederate disables the user in Zoom.

* **Delete**

  PingFederate deletes the user from Zoom. |

---

---
title: Supported attributes reference
description: The following table lists the attributes that can be mapped for user provisioning to Zoom.
component: zoom
page_id: zoom:setup:pf_zoom_connector_supported_attributes_reference
canonical_url: https://docs.pingidentity.com/integrations/zoom/setup/pf_zoom_connector_supported_attributes_reference.html
llms_txt: https://docs.pingidentity.com/integrations/zoom/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: March 25, 2025
---

# Supported attributes reference

The following table lists the attributes that can be mapped for user provisioning to Zoom.

| Attribute      | Description                                                                                                               |
| -------------- | ------------------------------------------------------------------------------------------------------------------------- |
| `Username`     | The user's unique identifier in Zoom. Must be in email address format.	This attribute is required.                        |
| `Email`        | The user's email address.                                                                                                 |
| `Department`   | The user's department or work group.For example, `Sales`.                                                                 |
| `Family Name`  | The user's family name.For example, `Jensen`, given the full name Ms. Barbara Jane Jensen, III.                           |
| `Given Name`   | The user's given name.For example, `Barbara`, given the full name Ms. Barbara Jane Jensen, III.                           |
| `Locale`       | Indicates the user's default location to localize such items as currency, date time format, or numerical representations. |
| `Organization` | The user's organization.                                                                                                  |
| `Phone`        | The user's phone number, formatted as `+1 2015550123`.                                                                    |
| `Roles`        | Roles held by the user.For example, `Student` or `Engineer`.                                                              |
| `Title`        | The user's title.For example, `Vice President`.                                                                           |
| `User Type`    | The account type.This can be `Basic`, `Licensed`, or `On-Prem`.                                                           |

---

---
title: Upgrading an existing deployment
description: If you're upgrading from a previous version of the Zoom Provisioner, note your existing service provider (SP) connection configuration and create a new connection.
component: zoom
page_id: zoom:setup:pf_zoom_connector_upgrading_an_existing_deployment
canonical_url: https://docs.pingidentity.com/integrations/zoom/setup/pf_zoom_connector_upgrading_an_existing_deployment.html
llms_txt: https://docs.pingidentity.com/integrations/zoom/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 5, 2025
section_ids:
  upgrading-an-existing-deployment-in-pingfederate-10-1-or-later: Upgrading an existing deployment in PingFederate 10.1 or later
  steps: Steps
  upgrading-an-existing-deployment-in-pingfederate-10-0-or-earlier: Upgrading an existing deployment in PingFederate 10.0 or earlier
  steps-2: Steps
---

# Upgrading an existing deployment

If you're upgrading from a previous version of the Zoom Provisioner, note your existing service provider (SP) connection configuration and create a new connection.

## Upgrading an existing deployment in PingFederate 10.1 or later

### Steps

1. Back up your current PingFederate configuration as shown in [Configuration archive](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_configurationarchivetasklet_selectimportexportstate.html) in the PingFederate documentation.

2. In the PingFederate administrative console, go to **Applications > Integration > SP Connections** and select your connection.

3. Note the attribute mappings for your existing SP connection.

   You can find help in [Mapping attributes](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_saaschanneltasklet_saasattrmappingmgmtstate.html) in the PingFederate documentation.

4. Delete your existing SP connection:

   1. Go to **Applications > Integration > SP Connections**.

   2. For your existing connection, click **Select action**, and then click **Delete**. Click **Confirm.**

5. Complete the steps in [Deploying the integration files](pf_zoom_connector_deploying_the_integration_files.html).

6. Complete the steps in [Creating a provisioning connection](pf_zoom_connector_creating_a_provisioning_connection.html).

   1. Go to **Outbound Provisioning > Manage Channels > Channel**, and on the **Attribute Mapping** tab, configure the attribute mappings based on your notes.

7. (Optional) Complete the steps in [Creating a single sign-on connection](pf_zoom_connector_creating_a_single_sign_on_connection.html).

## Upgrading an existing deployment in PingFederate 10.0 or earlier

### Steps

1. Back up your current PingFederate configuration as shown in [Configuration archive](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_configurationarchivetasklet_selectimportexportstate.html) in the PingFederate documentation.

2. In the PingFederate administrative console, go to **Identity Provider > SP Connections** and select your connection.

3. Note the attribute mappings for your existing SP connection.

   You can find help in [Mapping attributes](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_saaschanneltasklet_saasattrmappingmgmtstate.html) in the PingFederate documentation.

4. Delete your existing SP connection:

   1. Go to **Identity Provider > SP Connections > Manage All**.

   2. For your existing connection, click **Select action**, and then click **Delete**. Click **Save.**

5. Complete the steps in [Deploying the integration files](pf_zoom_connector_deploying_the_integration_files.html).

6. Complete the steps in [Creating a provisioning connection](pf_zoom_connector_creating_a_provisioning_connection.html).

   1. Go to **Outbound Provisioning > Manage Channels > Channel**, and on the **Attribute Mapping** tab, configure the attribute mappings based on your notes.

7. (Optional) Complete the steps in [Creating a single sign-on connection](pf_zoom_connector_creating_a_single_sign_on_connection.html).

---

---
title: Upgrading an existing deployment in PingFederate 10.0 or earlier
description: Back up your current PingFederate configuration as shown in Configuration archive in the PingFederate documentation.
component: zoom
page_id: zoom:setup:pf_zoom_connector_upgrading_an_existing_deployment_in_pf_100_or_earlier
canonical_url: https://docs.pingidentity.com/integrations/zoom/setup/pf_zoom_connector_upgrading_an_existing_deployment_in_pf_100_or_earlier.html
llms_txt: https://docs.pingidentity.com/integrations/zoom/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 5, 2025
section_ids:
  steps: Steps
---

# Upgrading an existing deployment in PingFederate 10.0 or earlier

## Steps

1. Back up your current PingFederate configuration as shown in [Configuration archive](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_configurationarchivetasklet_selectimportexportstate.html) in the PingFederate documentation.

2. In the PingFederate administrative console, go to **Identity Provider > SP Connections** and select your connection.

3. Note the attribute mappings for your existing SP connection.

   You can find help in [Mapping attributes](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_saaschanneltasklet_saasattrmappingmgmtstate.html) in the PingFederate documentation.

4. Delete your existing SP connection:

   1. Go to **Identity Provider > SP Connections > Manage All**.

   2. For your existing connection, click **Select action**, and then click **Delete**. Click **Save.**

5. Complete the steps in [Deploying the integration files](pf_zoom_connector_deploying_the_integration_files.html).

6. Complete the steps in [Creating a provisioning connection](pf_zoom_connector_creating_a_provisioning_connection.html).

   1. Go to **Outbound Provisioning > Manage Channels > Channel**, and on the **Attribute Mapping** tab, configure the attribute mappings based on your notes.

7. (Optional) Complete the steps in [Creating a single sign-on connection](pf_zoom_connector_creating_a_single_sign_on_connection.html).

---

---
title: Upgrading an existing deployment in PingFederate 10.1 or later
description: Back up your current PingFederate configuration as shown in Configuration archive in the PingFederate documentation.
component: zoom
page_id: zoom:setup:pf_zoom_connector_upgrading_an_existing_deployment_in_pf_101_or_later
canonical_url: https://docs.pingidentity.com/integrations/zoom/setup/pf_zoom_connector_upgrading_an_existing_deployment_in_pf_101_or_later.html
llms_txt: https://docs.pingidentity.com/integrations/zoom/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 5, 2025
section_ids:
  steps: Steps
---

# Upgrading an existing deployment in PingFederate 10.1 or later

## Steps

1. Back up your current PingFederate configuration as shown in [Configuration archive](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_configurationarchivetasklet_selectimportexportstate.html) in the PingFederate documentation.

2. In the PingFederate administrative console, go to **Applications > Integration > SP Connections** and select your connection.

3. Note the attribute mappings for your existing SP connection.

   You can find help in [Mapping attributes](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_saaschanneltasklet_saasattrmappingmgmtstate.html) in the PingFederate documentation.

4. Delete your existing SP connection:

   1. Go to **Applications > Integration > SP Connections**.

   2. For your existing connection, click **Select action**, and then click **Delete**. Click **Confirm.**

5. Complete the steps in [Deploying the integration files](pf_zoom_connector_deploying_the_integration_files.html).

6. Complete the steps in [Creating a provisioning connection](pf_zoom_connector_creating_a_provisioning_connection.html).

   1. Go to **Outbound Provisioning > Manage Channels > Channel**, and on the **Attribute Mapping** tab, configure the attribute mappings based on your notes.

7. (Optional) Complete the steps in [Creating a single sign-on connection](pf_zoom_connector_creating_a_single_sign_on_connection.html).

---

---
title: User management
description: The Zoom Provisioner links users from the datastore to Zoom. The following describes the behavior of each provisioning capability.
component: zoom
page_id: zoom::pf_zoom_connector_user_management
canonical_url: https://docs.pingidentity.com/integrations/zoom/pf_zoom_connector_user_management.html
llms_txt: https://docs.pingidentity.com/integrations/zoom/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 5, 2025
section_ids:
  synchronizing-existing-users: Synchronizing existing users
  user-provisioning: User provisioning
  user-updates: User updates
  user-deprovisioning: User deprovisioning
---

# User management

The Zoom Provisioner links users from the datastore to Zoom. The following describes the behavior of each provisioning capability.

## Synchronizing existing users

By default, the provisioning connector synchronizes users from the datastore to the target service by matching the `mail` attribute in the datastore to the `Username` attribute in the target service. You can change the default mapping in [Creating a provisioning connection](setup/pf_zoom_connector_creating_a_provisioning_connection.html).

For example:

* In the target service, Janet's `Username` is `jsmith@example.com`.

* In your datastore, Janet's `mail` is `jsmith@example.com`.

* On the **Attribute Mapping** tab of your PingFederate channel configuration, you map the `Username` attribute to `mail`.

* When the provisioning connector runs, the datastore user is provisioned with a `Username` of `jsmith`. That matches Janet's existing `Username` in the target service, so her information in the datastore is synchronized to her target service account.

## User provisioning

User provisioning is triggered when a user is added to the datastore group or filter targeted by the provisioning connector.

The target is determined by the **Source Location** tab in the provisioning connection configuration.

## User updates

User updates are triggered when a change occurs to a user attribute mapped in the provisioning connector configuration.

## User deprovisioning

User deprovisioning is triggered by any of the following:

* A user is deleted from the user store.

* A user is disabled in the user store.

* A user is removed from the data store filter targeted by the provisioning connector.

The **Remove User Action** setting in the connection configuration determines whether the deprovisioning action disables or deletes the user.