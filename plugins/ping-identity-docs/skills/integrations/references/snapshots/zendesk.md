---
title: Changelog
description: Zendesk Connector 2.1 – June 2017 (current release)
component: zendesk
page_id: zendesk:release_notes:pf_zendesk_connector_changelog
canonical_url: https://docs.pingidentity.com/integrations/zendesk/release_notes/pf_zendesk_connector_changelog.html
llms_txt: https://docs.pingidentity.com/integrations/zendesk/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 17, 2024
---

# Changelog

**Zendesk Connector 2.1 – June 2017 (current release)**

* Added Support for updating user emails

**Zendesk Connector 2.0 – October 2015**

* Added Support for Group Provisioning

* Added Support for provisioning additional user attributes

**Zendesk Connector 1.0 – October 2014**

* Initial Release

* Added Support for User Provisioning

---

---
title: Configuring SAML SSO in Zendesk
description: The following section describes the steps for configuring SP and IdP-initiated SSO to Zendesk.
component: zendesk
page_id: zendesk:setup:pf_zendesk_connector_configuring_saml_sso_in_zendesk
canonical_url: https://docs.pingidentity.com/integrations/zendesk/setup/pf_zendesk_connector_configuring_saml_sso_in_zendesk.html
llms_txt: https://docs.pingidentity.com/integrations/zendesk/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 17, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Configuring SAML SSO in Zendesk

The following section describes the steps for configuring SP and IdP-initiated SSO to Zendesk.

## About this task

|   |                                                                                                                                                                                                                                                                                                                    |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | This section requires two pieces of information that can be found within PingFederate. The first is the SAML 2.0 Entity ID, which can be found under on the **Server Settings** page and the second is the exported certificate used to sign the SAML assertion (configured in step 19 of Configure a Connection). |

## Steps

1. Navigate to `https://SUBDOMAIN.zendesk.com/agent/admin/` and sign in with your Admin credentials.

2. Navigate to **Security** under the **Settings** section to view single sign-on (SSO) configuration options.

3. If configuring SSO for **Admins & Agents**, select the **Admins & Agents** tab to view the Single sign-on (SSO) options.

4. If configuring SSO for **End-users**, select the **End-users** tab to view the Single sign-on (SSO) options.

5. Select **Single sign-on (SSO)** and select **SAML** to configure the options.

   1. Enter the PingFederate SAML endpoint into the **SAML SSO URL** field. `https://<pf_host>:<pf_port>/idp/SSO.saml2`

   2. Copy and paste the SHA1 fingerprint of the signing certificate into the Certificate fingerprint field.

      ![juc1563995864543](_images/juc1563995864543.jpg)

6. Click **Save** to complete Zendesk SSO Setup.

---

---
title: Creating a connection
description: To allow PingFederate to act as an identity provider and manage users in Zendesk, create a service provider (SP) connection.
component: zendesk
page_id: zendesk:setup:pf_zendesk_connector_creating_a_connection
canonical_url: https://docs.pingidentity.com/integrations/zendesk/setup/pf_zendesk_connector_creating_a_connection.html
llms_txt: https://docs.pingidentity.com/integrations/zendesk/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 17, 2024
section_ids:
  steps: Steps
---

# Creating a connection

To allow PingFederate to act as an identity provider and manage users in Zendesk, create a service provider (SP) connection.

## Steps

1. In the PingFederate administrator console, create a new SP connection:

   1. For PingFederate 10.1 or later: go to **Applications > Integration > SP Connections**. Click **Create Connection**.

   2. For PingFederate 10.0 or earlier: go to **Identity Provider > SP Connections**. Click **Create Connection**.

2. Configure the basic connection details with the Zendesk quick connection template.

   1. On the **Connection Template** tab, select **Use a template for this connection**.

   2. In the **Connection Template** list, select **Zendesk Provisioner**.

   3. In the **Metadata File** row, upload the zendesk-saml-metadata.xml file that you saved in [Obtain your Zendesk SAML 2.0 metadata XML file](pf_zendesk_connector_obtain_your_zendesk_saml_20_metadata_xml_file.html). Click **Next**.

   4. On the **Connection Type** tab, select **Browser SSO Profiles** and **Outbound Provisioning**. Click **Next**.

   5. On the **Connection Options** tab, click **Next**.

   6. On the **General Info** tab, in the **Connection Name** field, enter a name of your choosing. Click **Next**.

3. On the **Browser SSO** tab, configure your browser SSO settings as shown in [Configuring IdP Browser SSO](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_spconnectionconfigtasklet_spbrowserssostate.html) in the PingFederate documentation.

   1. On the **Browser SSO > SAML Profiles** tab, select only **IdP-Initiated SSO** and **SP-Initiated SSO**.

   2. On the **Browser SSO > Assertion Creation > Attribute Contract** tab, set the following name format.

      | Attribute Contract | Subject Name Format                                                      |
      | ------------------ | ------------------------------------------------------------------------ |
      | **SAML\_SUBJECT**  | `[.codeph]`urn:oasis:names:tc:SAML:1.1:nameid-format:unspecified\`\`\`\` |

   3. On the **Browser SSO > Protocol Settings > Signature Policy** tab, select the **Always Sign Assertion** check box.

4. On the **Credentials** tab, configure the connection credentials as shown in [Configuring credentials](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_spconnectionconfigtasklet_credentialsstate.html) in the PingFederate documentation. Click **Next**.

5. On the **Credentials > Digital Signature Settings** tab, select the **Include the certificate in the signature \<KEYINFO> element** check box.

6. On the **Outbound Provisioning** tab, configure provisioning as shown in [Configuring outbound provisioning](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_spconnectionconfigtasklet_saasprovisioningstate.html) in the PingFederate documentation:

   1. On the **Target** tab, enter the Zendesk Administator email, Sub-domain and API Token you obtained in [Obtain required information](pf_zendesk_connector_obtain_required_information.html).

   2. On the **Manage Channels > Attribute Mapping** tab, complete the attribute mappings as shown in [Managing channels](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_saasmanagementtasklet_saasmanagementstate.html) in the PingFederate documentation.

      Provide a source of data or provide a default value for the `role` attribute. This attribute only accepts specific values, which are explained in the [Supported attributes reference](pf_zendesk_connector_supported_attributes_reference.html).

7. On the **Activation and Summary** tab, above the **Summary** section, click the toggle to turn on the connection. Click **Save**.

---

---
title: Deploying the integration files
description: To get started with the integration, deploy the Zendesk Provisioner files to your PingFederate directory.
component: zendesk
page_id: zendesk:setup:pf_zendesk_connector_deploying_the_integration_files
canonical_url: https://docs.pingidentity.com/integrations/zendesk/setup/pf_zendesk_connector_deploying_the_integration_files.html
llms_txt: https://docs.pingidentity.com/integrations/zendesk/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 17, 2024
section_ids:
  steps: Steps
---

# Deploying the integration files

To get started with the integration, deploy the Zendesk Provisioner files to your PingFederate directory.

## Steps

1. Download the Zendesk Provisioner `.zip` archive from the [**Add-ons** tab of the PingFederate downloads page](https://www.pingidentity.com/en/resources/downloads/pingfederate.html) or the [Ping Identity Marketplace](https://marketplace.pingone.com/item/zendesk-sso-integration).

2. Stop PingFederate.

3. If you're upgrading an existing deployment, delete the `pf-zendesk-quickconnection-<version>.jar` file from your `<pf_install>/pingfederate/server/default/deploy` directory.

4. Extract the `.zip` archive and merge the contents of the `dist` directory with your `<pf_install>/pingfederate/server/default/deploy` directory.

   Enable the PingFederate provisioning engine:

   1. Open your `<pf_install>/pingfederate/bin/run.properties` file.Change `pf.provisioner.mode` to `STANDALONE`. Save the file.

      |   |                                                                                                                                                                                                                                        |
      | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      |   | To configure the `FAILOVER` mode instead, see [Deploying provisioning failover](https://docs.pingidentity.com/pingfederate/latest/server_clustering_guide/pf_deploy_provis_failover.html) in the PingFederate Server Clustering Guide. |

5. Start PingFederate.

6. If you operate PingFederate in a cluster, repeat steps 2-4 and step 6 for each engine node.

---

---
title: Download manifest
description: The distribution .zip archive for the Connector contains the following:
component: zendesk
page_id: zendesk:release_notes:pf_zendesk_connector_download_manifest
canonical_url: https://docs.pingidentity.com/integrations/zendesk/release_notes/pf_zendesk_connector_download_manifest.html
llms_txt: https://docs.pingidentity.com/integrations/zendesk/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 17, 2024
---

# Download manifest

The distribution `.zip` archive for the Connector contains the following:

* `ReadMeFirst.pdf` – contains links to this online documentation.

* `zendesk-saml-metadata.xml` – The metadata used for Browser SSO

* `legal`:

  * `Legal.pdf` – copyright and license information.

* `dist` – contains libraries needed for the Connector:

  * `pf-zendesk-quickconnection-2.1.jar` – PingFederate Zendesk Connector

---

---
title: Enabling provisioning and single sign-on in PingFederate
description: To use PingFederate for provisioning and single sign-on, configure an external datastore and set a SAML entity ID.
component: zendesk
page_id: zendesk:setup:pf_zendesk_connector_enabling_provisioning_and_single_sign_on_in_pf
canonical_url: https://docs.pingidentity.com/integrations/zendesk/setup/pf_zendesk_connector_enabling_provisioning_and_single_sign_on_in_pf.html
llms_txt: https://docs.pingidentity.com/integrations/zendesk/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 17, 2024
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
component: zendesk
page_id: zendesk:setup:pf_zendesk_connector_enabling_provisioning_and_single_sign_on_in_pf_100_or_earlier
canonical_url: https://docs.pingidentity.com/integrations/zendesk/setup/pf_zendesk_connector_enabling_provisioning_and_single_sign_on_in_pf_100_or_earlier.html
llms_txt: https://docs.pingidentity.com/integrations/zendesk/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
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
component: zendesk
page_id: zendesk:setup:pf_zendesk_connector_enabling_provisioning_and_single_sign_on_in_pf_101_or_later
canonical_url: https://docs.pingidentity.com/integrations/zendesk/setup/pf_zendesk_connector_enabling_provisioning_and_single_sign_on_in_pf_101_or_later.html
llms_txt: https://docs.pingidentity.com/integrations/zendesk/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
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
title: Known issues and limitations
description: Known Limitations
component: zendesk
page_id: zendesk:release_notes:pf_zendesk_connector_known_issues_and_limitations
canonical_url: https://docs.pingidentity.com/integrations/zendesk/release_notes/pf_zendesk_connector_known_issues_and_limitations.html
llms_txt: https://docs.pingidentity.com/integrations/zendesk/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 17, 2024
---

# Known issues and limitations

**Known Limitations**

* Because of a limitation with PingFederate 8.1 and earlier versions, when configuring two service provider (SP) connections with the same provisioner, the second connection built can be pre-populated with the channel from the first connection. To avoid conflicts, delete this pre-populated channel and create a unique channel for each connection.

* Single logout (SLO) is not supported.

* User attributes cannot be cleared once set, they can only be updated.

* Emails that contain plus (+) symbols are not supported and may cause issues with provisioning.

* Syncing with existing groups is not supported. The connector is not able to manage groups, or add users to groups that it has not created.

* There is the potential to have a user in Zendesk managed by two users in Active Directory. This occurs when a new user is created with the secondary email of another user.

---

---
title: Obtain required information
description: Before you can configure this connector, you must complete the following steps.
component: zendesk
page_id: zendesk:setup:pf_zendesk_connector_obtain_required_information
canonical_url: https://docs.pingidentity.com/integrations/zendesk/setup/pf_zendesk_connector_obtain_required_information.html
llms_txt: https://docs.pingidentity.com/integrations/zendesk/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 17, 2024
section_ids:
  obtain-your-zendesk-administrator-email: Obtain your Zendesk administrator email
  obtain-your-zendesk-subdomain: Obtain your Zendesk subdomain
  obtain-your-zendesk-saml-2-0-metadata-xml-file: Obtain your Zendesk SAML 2.0 metadata XML file
  about-this-task: About this task
  steps: Steps
  example: Example:
  provision-existing-user-accounts-on-zendesk: Provision existing user accounts on Zendesk
  obtain-your-zendesk-api-token: Obtain your Zendesk API token
  about-this-task-2: About this task
  steps-2: Steps
---

# Obtain required information

Before you can configure this connector, you must complete the following steps.

|   |                                                                                                                                                 |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Some of the following steps result in information that you'll need for subsequent tasks. You should copy this information to a secure location. |

* [Obtain your Zendesk administrator email](pf_zendesk_connector_obtain_your_zendesk_administrator_email.html)

* [Obtain your Zendesk subdomain](pf_zendesk_connector_obtain_your_zendesk_subdomain.html)

* [Obtain your Zendesk API token](pf_zendesk_connector_obtain_your_zendesk_api_token.html)

* [Obtain your Zendesk SAML 2.0 metadata XML file](pf_zendesk_connector_obtain_your_zendesk_saml_20_metadata_xml_file.html)

* [Provision existing user accounts on Zendesk](pf_zendesk_connector_provision_existing_user_accounts_on_zendesk.html)

## Obtain your Zendesk administrator email

This connector requires a valid administrator account email to be used when configuring a service provider (SP) connection for outbound provisioning.

|   |                                                                                                   |
| - | ------------------------------------------------------------------------------------------------- |
|   | You only require this information if you're configuring this connector for outbound provisioning. |

## Obtain your Zendesk subdomain

This connector requires the subdomain, such as *\<YourSubDomain>*.zendesk.com, to access your Zendesk for single sign-on (SSO) and outbound provisioning.

## Obtain your Zendesk SAML 2.0 metadata XML file

### About this task

This connectors quick-connection template uses a metadata XML file to assist in configuring many settings in the SP connection. Before configuring your SP connection, you must first prepare the `zendesk-saml-metadata.xml` that comes packaged with the Zendesk Connector.

### Steps

1. Open the `zendesk-saml-metadata.xml` file that came packaged with the Zendesk Connector in a text editor.

2. Replace all instances of `SUBDOMAIN` with your Zendesk subdomain value:

   #### Example:

   If your Zendesk subdomain is `pingidentity1234567890`, then `SUBDOMAIN.zendesk.com` would become `pingidentity1234567890.zendesk.com`.

3. Save your changes.

## Provision existing user accounts on Zendesk

When configuring the connector, make sure that the value mapped to the `email` attribute matches the existing Zendesk user's email address exactly as it appears in Zendesk.

For example, on the **Attribute Mapping** tab, the user's `email` attribute on Zendesk is mapped to the user `mail` attribute in your LDAP. This will synchronize a user that already exists on Zendesk with an `email` address in Zendesk of `john.smith@mydomain.com`. In this case, the user's `mail` attribute in LDAP would also have to be `john.smith@mydomain.com`.

When the Zendesk connector provisions for the first time, this address is used to synchronize the user in your LDAP data store with the user in Zendesk.

## Obtain your Zendesk API token

### About this task

The Zendesk Connector's outbound provisioning functionality is built using Zendesk's REST API, which requires an authorized OAuth 2.0 Access Token.

|   |                                                                                                    |
| - | -------------------------------------------------------------------------------------------------- |
|   | You only require this information if you are configuring this connector for outbound provisioning. |

### Steps

1. Sign on to Zendesk with your administrator account.

2. Click the **Gear** icon and select **API** in the **Channels** category.

3. On the **Settings** tab, ensure the **Token Access** check box is selected.

4. Note the **API token** value.

   |   |                                                                                                                                                                                                                   |
   | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | These steps are subject to change at the discretion of Zendesk. If these steps are different from the steps in this document, contact your Zendesk representative for updated steps for obtaining this API token. |

---

---
title: Obtain your Zendesk administrator email
description: This connector requires a valid administrator account email to be used when configuring a service provider (SP) connection for outbound provisioning.
component: zendesk
page_id: zendesk:setup:pf_zendesk_connector_obtain_your_zendesk_administrator_email
canonical_url: https://docs.pingidentity.com/integrations/zendesk/setup/pf_zendesk_connector_obtain_your_zendesk_administrator_email.html
llms_txt: https://docs.pingidentity.com/integrations/zendesk/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 17, 2024
---

# Obtain your Zendesk administrator email

This connector requires a valid administrator account email to be used when configuring a service provider (SP) connection for outbound provisioning.

|   |                                                                                                   |
| - | ------------------------------------------------------------------------------------------------- |
|   | You only require this information if you're configuring this connector for outbound provisioning. |

---

---
title: Obtain your Zendesk API token
description: The Zendesk Connector's outbound provisioning functionality is built using Zendesk's REST API, which requires an authorized OAuth 2.0 Access Token.
component: zendesk
page_id: zendesk:setup:pf_zendesk_connector_obtain_your_zendesk_api_token
canonical_url: https://docs.pingidentity.com/integrations/zendesk/setup/pf_zendesk_connector_obtain_your_zendesk_api_token.html
llms_txt: https://docs.pingidentity.com/integrations/zendesk/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 17, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Obtain your Zendesk API token

## About this task

The Zendesk Connector's outbound provisioning functionality is built using Zendesk's REST API, which requires an authorized OAuth 2.0 Access Token.

|   |                                                                                                    |
| - | -------------------------------------------------------------------------------------------------- |
|   | You only require this information if you are configuring this connector for outbound provisioning. |

## Steps

1. Sign on to Zendesk with your administrator account.

2. Click the **Gear** icon and select **API** in the **Channels** category.

3. On the **Settings** tab, ensure the **Token Access** check box is selected.

4. Note the **API token** value.

   |   |                                                                                                                                                                                                                   |
   | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | These steps are subject to change at the discretion of Zendesk. If these steps are different from the steps in this document, contact your Zendesk representative for updated steps for obtaining this API token. |

---

---
title: Obtain your Zendesk SAML 2.0 metadata XML file
description: This connectors quick-connection template uses a metadata XML file to assist in configuring many settings in the SP connection. Before configuring your SP connection, you must first prepare the zendesk-saml-metadata.xml that comes packaged with the Zendesk Connector.
component: zendesk
page_id: zendesk:setup:pf_zendesk_connector_obtain_your_zendesk_saml_20_metadata_xml_file
canonical_url: https://docs.pingidentity.com/integrations/zendesk/setup/pf_zendesk_connector_obtain_your_zendesk_saml_20_metadata_xml_file.html
llms_txt: https://docs.pingidentity.com/integrations/zendesk/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 27, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
  example: Example:
---

# Obtain your Zendesk SAML 2.0 metadata XML file

## About this task

This connectors quick-connection template uses a metadata XML file to assist in configuring many settings in the SP connection. Before configuring your SP connection, you must first prepare the `zendesk-saml-metadata.xml` that comes packaged with the Zendesk Connector.

## Steps

1. Open the `zendesk-saml-metadata.xml` file that came packaged with the Zendesk Connector in a text editor.

2. Replace all instances of `SUBDOMAIN` with your Zendesk subdomain value:

   ### Example:

   If your Zendesk subdomain is `pingidentity1234567890`, then `SUBDOMAIN.zendesk.com` would become `pingidentity1234567890.zendesk.com`.

3. Save your changes.

---

---
title: Obtain your Zendesk subdomain
description: This connector requires the subdomain, such as <YourSubDomain>.zendesk.com, to access your Zendesk for single sign-on (SSO) and outbound provisioning.
component: zendesk
page_id: zendesk:setup:pf_zendesk_connector_obtain_your_zendesk_subdomain
canonical_url: https://docs.pingidentity.com/integrations/zendesk/setup/pf_zendesk_connector_obtain_your_zendesk_subdomain.html
llms_txt: https://docs.pingidentity.com/integrations/zendesk/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 17, 2024
---

# Obtain your Zendesk subdomain

This connector requires the subdomain, such as *\<YourSubDomain>*.zendesk.com, to access your Zendesk for single sign-on (SSO) and outbound provisioning.

---

---
title: Provision existing user accounts on Zendesk
description: When configuring the connector, make sure that the value mapped to the email attribute matches the existing Zendesk user's email address exactly as it appears in Zendesk.
component: zendesk
page_id: zendesk:setup:pf_zendesk_connector_provision_existing_user_accounts_on_zendesk
canonical_url: https://docs.pingidentity.com/integrations/zendesk/setup/pf_zendesk_connector_provision_existing_user_accounts_on_zendesk.html
llms_txt: https://docs.pingidentity.com/integrations/zendesk/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 17, 2024
---

# Provision existing user accounts on Zendesk

When configuring the connector, make sure that the value mapped to the `email` attribute matches the existing Zendesk user's email address exactly as it appears in Zendesk.

For example, on the **Attribute Mapping** tab, the user's `email` attribute on Zendesk is mapped to the user `mail` attribute in your LDAP. This will synchronize a user that already exists on Zendesk with an `email` address in Zendesk of `john.smith@mydomain.com`. In this case, the user's `mail` attribute in LDAP would also have to be `john.smith@mydomain.com`.

When the Zendesk connector provisions for the first time, this address is used to synchronize the user in your LDAP data store with the user in Zendesk.

---

---
title: Supported attributes reference
description: The following table consists of the attributes that can be mapped on a user during provisioning.
component: zendesk
page_id: zendesk:setup:pf_zendesk_connector_supported_attributes_reference
canonical_url: https://docs.pingidentity.com/integrations/zendesk/setup/pf_zendesk_connector_supported_attributes_reference.html
llms_txt: https://docs.pingidentity.com/integrations/zendesk/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 17, 2024
---

# Supported attributes reference

The following table consists of the attributes that can be mapped on a user during provisioning.

| Attribute               | Description                                                                                                                                                                                                                  |
| ----------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `email`                 | The primary email address of the user.&#xA;&#xA;An update to the email attribute will make the new email as primary and leave the old email as secondary.                                                                    |
| `external_id`           | A unique id you can set on a user.                                                                                                                                                                                           |
| `name`                  | The name of the user                                                                                                                                                                                                         |
| `alias`                 | An Agent's alias that is displayed visible by end-user type users.                                                                                                                                                           |
| `custom_role_id`        | The if of the custom role for the user. The id of a custom role can be obtained from Zendesk after creating it.                                                                                                              |
| `details`               | Any details you wish to store about the user.                                                                                                                                                                                |
| `locale_id`             | The id of the user's locale. The id of a locale can be obtained from Zendesk.                                                                                                                                                |
| `moderator`             | Designates whether the user has forum moderation capabilities. Acceptable options include: "true" or "false".                                                                                                                |
| `notes`                 | A general note field for the user.                                                                                                                                                                                           |
| `only_private_comments` | Designates whether the user can only create private comments. Acceptable options include: "true" or "false".                                                                                                                 |
| `organization_id`       | The id of the organization this user is associated with. The id of an organization can be obtained from Zendesk after creating it.Example: An organization called "`Employee`" may have an id that looks like "`187178237`". |
| `phone`                 | The primary phone number of a user.                                                                                                                                                                                          |
| `role`                  | The role of the user in Zendesk. Acceptable options include: "end-user", "agent" and "admin".                                                                                                                                |
| `signature`             | The user's signature. Only available for agents and admins.                                                                                                                                                                  |
| `tags`                  | A multi value attribute representing all the user's tags. Tags will only be present if your account has user tagging enabled.                                                                                                |
| `ticket_restriction`    | Specifies which tickets the user has access to. Possible values are: "organization", "groups", "assigned", "requested", null.                                                                                                |
| `time_zone`             | The user's time zone.                                                                                                                                                                                                        |
| `verified`              | Designates if the user's identity has been verified. Acceptable options include: "true" or "false".                                                                                                                          |

---

---
title: Upgrading an existing deployment
description: If you're upgrading from a previous version of the Zendesk Provisioner, note your existing service provider (SP) connection configuration and create a new connection.
component: zendesk
page_id: zendesk:setup:pf_zendesk_connector_upgrading_an_existing_deployment
canonical_url: https://docs.pingidentity.com/integrations/zendesk/setup/pf_zendesk_connector_upgrading_an_existing_deployment.html
llms_txt: https://docs.pingidentity.com/integrations/zendesk/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 17, 2024
section_ids:
  upgrading-an-existing-deployment-in-pingfederate-10-1-or-later: Upgrading an existing deployment in PingFederate 10.1 or later
  steps: Steps
  upgrading-an-existing-deployment-in-pingfederate-10-0-or-earlier: Upgrading an existing deployment in PingFederate 10.0 or earlier
  steps-2: Steps
---

# Upgrading an existing deployment

If you're upgrading from a previous version of the Zendesk Provisioner, note your existing service provider (SP) connection configuration and create a new connection.

## Upgrading an existing deployment in PingFederate 10.1 or later

### Steps

1. Back up your current PingFederate configuration as shown in [Configuration archive](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_configurationarchivetasklet_selectimportexportstate.html) in the PingFederate documentation.

2. In the PingFederate administrative console, go to **Applications > Integration > SP Connections** and select your connection.

   Note the attribute mappings for your existing SP connection.

   For help, see [Mapping attributes](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_saaschanneltasklet_saasattrmappingmgmtstate.html) in the PingFederate documentation.

3. Delete your existing SP connection.

   1. Go to **Applications > Integration > SP Connections**.For your existing connection, click **Select action**, and then click **Delete**. Click **Confirm.**

4. Complete the steps in [Deploying the integration files](pf_zendesk_connector_deploying_the_integration_files.html).

5. Complete the steps in [Creating a connection](pf_zendesk_connector_creating_a_connection.html).

6. From **Outbound Provisioning > Manage Channels > Channel**, on the **Attribute Mapping** tab, configure the attribute mappings based on your notes.

7. Complete the steps in [Configuring SAML SSO in Zendesk](pf_zendesk_connector_configuring_saml_sso_in_zendesk.html).

## Upgrading an existing deployment in PingFederate 10.0 or earlier

### Steps

1. Back up your current PingFederate configuration as shown in [Configuration archive](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_configurationarchivetasklet_selectimportexportstate.html) in the PingFederate documentation.

2. In the PingFederate administrative console, go to **Identity Provider > SP Connections** and select your connection.

   Note the attribute mappings for your existing SP connection.

   For help, see [Mapping attributes](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_saaschanneltasklet_saasattrmappingmgmtstate.html) in the PingFederate documentation.

3. Delete your existing SP connection.

   1. Go to **Identity Provider > SP Connections > Manage All**.For your existing connection, click **Select action**, and then click **Delete**. Click **Save.**

4. Complete the steps in [Deploying the integration files](pf_zendesk_connector_deploying_the_integration_files.html).

5. Complete the steps in [Creating a connection](pf_zendesk_connector_creating_a_connection.html).

6. From **Outbound Provisioning > Manage Channels > Channel**, on the **Attribute Mapping** tab, configure the attribute mappings based on your notes.

7. Complete the steps in [Configuring SAML SSO in Zendesk](pf_zendesk_connector_configuring_saml_sso_in_zendesk.html).

---

---
title: Upgrading an existing deployment in PingFederate 10.0 or earlier
description: Back up your current PingFederate configuration as shown in Configuration archive in the PingFederate documentation.
component: zendesk
page_id: zendesk:setup:pf_zendesk_connector_upgrading_an_existing_deployment_in_pf_100_or_earlier
canonical_url: https://docs.pingidentity.com/integrations/zendesk/setup/pf_zendesk_connector_upgrading_an_existing_deployment_in_pf_100_or_earlier.html
llms_txt: https://docs.pingidentity.com/integrations/zendesk/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 27, 2024
section_ids:
  steps: Steps
---

# Upgrading an existing deployment in PingFederate 10.0 or earlier

## Steps

1. Back up your current PingFederate configuration as shown in [Configuration archive](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_configurationarchivetasklet_selectimportexportstate.html) in the PingFederate documentation.

2. In the PingFederate administrative console, go to **Identity Provider > SP Connections** and select your connection.

   Note the attribute mappings for your existing SP connection.

   For help, see [Mapping attributes](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_saaschanneltasklet_saasattrmappingmgmtstate.html) in the PingFederate documentation.

3. Delete your existing SP connection.

   1. Go to **Identity Provider > SP Connections > Manage All**.For your existing connection, click **Select action**, and then click **Delete**. Click **Save.**

4. Complete the steps in [Deploying the integration files](pf_zendesk_connector_deploying_the_integration_files.html).

5. Complete the steps in [Creating a connection](pf_zendesk_connector_creating_a_connection.html).

6. From **Outbound Provisioning > Manage Channels > Channel**, on the **Attribute Mapping** tab, configure the attribute mappings based on your notes.

7. Complete the steps in [Configuring SAML SSO in Zendesk](pf_zendesk_connector_configuring_saml_sso_in_zendesk.html).

---

---
title: Upgrading an existing deployment in PingFederate 10.1 or later
description: Back up your current PingFederate configuration as shown in Configuration archive in the PingFederate documentation.
component: zendesk
page_id: zendesk:setup:pf_zendesk_connector_upgrading_an_existing_deployment_in_pf_101_or_later
canonical_url: https://docs.pingidentity.com/integrations/zendesk/setup/pf_zendesk_connector_upgrading_an_existing_deployment_in_pf_101_or_later.html
llms_txt: https://docs.pingidentity.com/integrations/zendesk/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 27, 2024
section_ids:
  steps: Steps
---

# Upgrading an existing deployment in PingFederate 10.1 or later

## Steps

1. Back up your current PingFederate configuration as shown in [Configuration archive](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_configurationarchivetasklet_selectimportexportstate.html) in the PingFederate documentation.

2. In the PingFederate administrative console, go to **Applications > Integration > SP Connections** and select your connection.

   Note the attribute mappings for your existing SP connection.

   For help, see [Mapping attributes](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_saaschanneltasklet_saasattrmappingmgmtstate.html) in the PingFederate documentation.

3. Delete your existing SP connection.

   1. Go to **Applications > Integration > SP Connections**.For your existing connection, click **Select action**, and then click **Delete**. Click **Confirm.**

4. Complete the steps in [Deploying the integration files](pf_zendesk_connector_deploying_the_integration_files.html).

5. Complete the steps in [Creating a connection](pf_zendesk_connector_creating_a_connection.html).

6. From **Outbound Provisioning > Manage Channels > Channel**, on the **Attribute Mapping** tab, configure the attribute mappings based on your notes.

7. Complete the steps in [Configuring SAML SSO in Zendesk](pf_zendesk_connector_configuring_saml_sso_in_zendesk.html).

---

---
title: User and group management
description: The Zendesk Provisioner synchronizes users and groups from your datastore to Zendesk. The following describes the behavior of each provisioning capability.
component: zendesk
page_id: zendesk::pf_zendesk_connector_user_and_group_management
canonical_url: https://docs.pingidentity.com/integrations/zendesk/pf_zendesk_connector_user_and_group_management.html
llms_txt: https://docs.pingidentity.com/integrations/zendesk/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 17, 2024
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

The Zendesk Provisioner synchronizes users and groups from your datastore to Zendesk. The following describes the behavior of each provisioning capability.

|   |                                                                                                                                                                                                                 |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | You can configure the following capabilities and specify which users to provision when you get to the [Creating a connection](setup/pf_zendesk_connector_creating_a_connection.html) part of the setup process. |

## Synchronizing existing users

PingFederate synchronizes users based on the `email` attribute in Zendesk. If a user already exists in your datastore and Zendesk, mapping this attribute correctly links the two records together.

For example:

* In Zendesk, Janet's `email` is `jsmith@example.com`.

* In your datastore, Janet's `mail` is `jsmith@example.com`.

* On the **Attribute Mapping** tab of your provisioning connection configuration, map the `email` attribute to `mail`.

* When the provisioning connector runs, the datastore user is provisioned with a `email` of `jsmith@example.com`. That matches Janet's existing `email` in Zendesk, so her information in the datastore is synchronized to her Zendesk account.

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

PingFederate synchronizes groups from the datastore to the target service based on the group name.

For example:

* In Zendesk, there is a group is named `Accounting`.

* In your datastore, there is a group with a `CN` of `Accounting`.

* When the provisioning connector runs, the two groups are synchronized.

## Group provisioning

PingFederate provisions groups when a group is added to the datastore filter that is targeted by the provisioning connector.

You can define which groups PingFederate targets for provisioning and monitors for changes on the **Source Location** tab in your provisioning connection configuration.

## Group name updates

PingFederate renames groups when they are renamed in the datastore.

## Group membership updates

PingFederate updates group memberships when memberships change in the datastore, whether the change is in the group's properties or a user's properties.

Group memberships in the datastore overwrite the group memberships in Zendesk.

## Group deletion

PingFederate deletes groups when any of the following happens:

* The group is deleted in the datastore.

* The group is removed from the datastore group or filter that is targeted by the provisioning connector.

|   |                                                     |
| - | --------------------------------------------------- |
|   | Group deletions are permanent and cannot be undone. |