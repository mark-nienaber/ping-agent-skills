---
title: Deploying the integration files
description: To get started with the integration, deploy the Zscaler Internet Access Provisioner files to your PingFederate directory.
component: zscaler
page_id: zscaler:zscaler_internet_access_provisioner:pf_zscaler_zia_connector_deploying_the_integration_files
canonical_url: https://docs.pingidentity.com/integrations/zscaler/zscaler_internet_access_provisioner/pf_zscaler_zia_connector_deploying_the_integration_files.html
llms_txt: https://docs.pingidentity.com/integrations/zscaler/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
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
llms_txt: https://docs.pingidentity.com/integrations/zscaler/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
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
llms_txt: https://docs.pingidentity.com/integrations/zscaler/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
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
llms_txt: https://docs.pingidentity.com/integrations/zscaler/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
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
llms_txt: https://docs.pingidentity.com/integrations/zscaler/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
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
llms_txt: https://docs.pingidentity.com/integrations/zscaler/llms.txt
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
component: zscaler
page_id: zscaler:zscaler_internet_access_provisioner:pf_zscaler_zia_connector_enabling_provisioning_and_single_sign_on_in_pf_101_or_later
canonical_url: https://docs.pingidentity.com/integrations/zscaler/zscaler_internet_access_provisioner/pf_zscaler_zia_connector_enabling_provisioning_and_single_sign_on_in_pf_101_or_later.html
llms_txt: https://docs.pingidentity.com/integrations/zscaler/llms.txt
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
title: Enabling provisioning and single sign-on in Zscaler
description: Register PingFederate as an identity provider in Zscaler and download the SAML metadata information.
component: zscaler
page_id: zscaler:zscaler_private_access_provisioner:pf_zscaler_zpa_connector_enabling_provisioning_and_single_sign_on_in_zscaler
canonical_url: https://docs.pingidentity.com/integrations/zscaler/zscaler_private_access_provisioner/pf_zscaler_zpa_connector_enabling_provisioning_and_single_sign_on_in_zscaler.html
llms_txt: https://docs.pingidentity.com/integrations/zscaler/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
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
llms_txt: https://docs.pingidentity.com/integrations/zscaler/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
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
llms_txt: https://docs.pingidentity.com/integrations/zscaler/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
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
llms_txt: https://docs.pingidentity.com/integrations/zscaler/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
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
llms_txt: https://docs.pingidentity.com/integrations/zscaler/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
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

---

---
title: Getting a base URL and bearer token from Zscaler
description: To enable provisioning to Zscaler Internet Access, enable the System for Cross-domain Identity Management (SCIM) feature and note your configuration information.
component: zscaler
page_id: zscaler:zscaler_internet_access_provisioner:pf_zscaler_zia_connector_getting_a_base_url_and_bearer_token_from_zscaler
canonical_url: https://docs.pingidentity.com/integrations/zscaler/zscaler_internet_access_provisioner/pf_zscaler_zia_connector_getting_a_base_url_and_bearer_token_from_zscaler.html
llms_txt: https://docs.pingidentity.com/integrations/zscaler/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 18, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Getting a base URL and bearer token from Zscaler

To enable provisioning to Zscaler Internet Access, enable the System for Cross-domain Identity Management (SCIM) feature and note your configuration information.

## About this task

Learn more in [About SCIM](https://help.zscaler.com/zia/about-scim) and [Configuring SCIM](https://help.zscaler.com/zia/configuring-scim) in the Zscaler Internet Access documentation.

## Steps

1. Sign on to Zscaler Internet Access as an administrator.

2. Go to **Administration > Settings > Company Profile** and note your **Company ID**.

   You'll use this as your organization ID in step 5.

3. Go to **Administration > Authentication > Authentication Settings**.

4. On the **Authentication Profile** tab, in the **Authentication Type** section, select **SAML**. Click **Configure SAML**.

5. Configure SAML and enable provisioning:

   1. In the **Configure SAML** window, select **Enable SCIM-Based Provisioning**.

   2. In the **Base URL** field, enter `https://scim.<Zscaler_cloud_name>.net/<organization_ID>/scim`.

      You can find the cloud name in the URL that you use to sign on to the Zscaler Internet Access service. For example, if you sign on to admin.zscalerbeta.net, then your cloud name is zscalerbeta.net.

   3. Note the **Bearer Token**. Click **Save**.

      You'll use the **Bearer Token** value in [Creating a provisioning connection](pf_zscaler_zia_connector_creating_a_provisioning_connection.html).

6. Click **Save**.

7. Activate the change as shown in [Saving and Activating Changes in the Admin Portal](https://help.zscaler.com/zia/saving-and-activating-changes-admin-portal) in the Zscaler Internet Access documentation.

---

---
title: Getting SAML details from Zscaler
description: To simplify the PingFederate configuration process, download your Zscaler Internet Access SAML metadata XML file.
component: zscaler
page_id: zscaler:zscaler_internet_access_provisioner:pf_zscaler_zia_connector_getting_saml_details_from_zscaler
canonical_url: https://docs.pingidentity.com/integrations/zscaler/zscaler_internet_access_provisioner/pf_zscaler_zia_connector_getting_saml_details_from_zscaler.html
llms_txt: https://docs.pingidentity.com/integrations/zscaler/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 18, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Getting SAML details from Zscaler

To simplify the PingFederate configuration process, download your Zscaler Internet Access SAML metadata XML file.

## About this task

For more information about configuring SAML, see [About SAML](https://help.zscaler.com/zia/about-saml) and [Configuring SAML](https://help.zscaler.com/zia/configuring-saml) in the Zscaler Internet Access documentation.

## Steps

1. Sign on to Zscaler Internet Access as an administrator.

2. Go to **Administration > Authentication > Authentication Settings**.

3. Click **Configure SAML**.

4. In the **SP's Metadata** section, click **Download**.

5. Save `zscaler-metadata.xml`.

---

---
title: Known issues and limitations
description: The following are known issues or limitations for the Zscaler Internet Access Provisioner.
component: zscaler
page_id: zscaler:zscaler_internet_access_provisioner:pf_zscaler_zia_connector_known_issues_and_limitations
canonical_url: https://docs.pingidentity.com/integrations/zscaler/zscaler_internet_access_provisioner/pf_zscaler_zia_connector_known_issues_and_limitations.html
llms_txt: https://docs.pingidentity.com/integrations/zscaler/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 18, 2024
section_ids:
  known-issues: Known issues
  known-limitations: Known limitations
---

# Known issues and limitations

The following are known issues or limitations for the Zscaler Internet Access Provisioner.

## Known issues

There are no known issues.

## Known limitations

* When an LDAP user is deleted in a targeted group distinguished name (DN), the provisioning connector does not propagate the deletion until a new user is added to the group. This limitation is compounded when the **User Create** provisioning option is disabled. Learn more about solutions in [SaaS provisioner does not remove the user](https://support.pingidentity.com/s/article/After-deleting-an-AD-user-account-SaaS-provisioner-does-not-remove-the-user-in-the-next-provisioning-cycle-when-Group-DN-is-specified) in the Knowledge Base.

* Because of PingFederate limitations, user attributes cannot be cleared once set.

* Because of PingFederate limitations, the group name is the only supported group attribute and must be the Common Name (CN) of the LDAP group being provisioned. Additional group attributes are not supported in PingFederate.

* Performance:

  * Zscaler Internet Access System for Cross-domain Identity Management (SCIM) servers have a rate limit of 5 requests per second. In order to avoid retries, reduce the number of threads in the PingFederate channel configuration. For more information, see [Specifying channel information](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_saaschanneltasklet_saasgeneralinfostate.html) in the PingFederate documentation and [SCIM API Examples](https://help.zscaler.com/zia/scim-api-examples) in the Zscaler Internet Access documentation.

  * When provisioning users to a group, all users must be set to active. If an inactive user is present, the active users and group will be provisioned but no users will be added to the group.

  * Rate limiting can prevent the connector from provisioning users to groups. If rate limiting forces a retry, and a user is created on the retry, the user's group memberships are applied the next time the relevant groups are updated.

---

---
title: Known issues and limitations
description: The following are known issues or limitations with the Zscaler Private Access Provisioner.
component: zscaler
page_id: zscaler:zscaler_private_access_provisioner:pf_zscaler_zpa_connector_known_issues_and_limitations
canonical_url: https://docs.pingidentity.com/integrations/zscaler/zscaler_private_access_provisioner/pf_zscaler_zpa_connector_known_issues_and_limitations.html
llms_txt: https://docs.pingidentity.com/integrations/zscaler/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 18, 2024
section_ids:
  known-issues: Known issues
  known-limitations: Known limitations
---

# Known issues and limitations

The following are known issues or limitations with the Zscaler Private Access Provisioner.

## Known issues

There are no known issues.

## Known limitations

* When an LDAP user is deleted in a targeted group distinguished name (DN), the provisioning connector does not propagate the deletion until a new user is added to the group. This limitation is compounded when the **User Create** provisioning option is disabled. For solutions, see [SaaS provisioner does not remove the user](https://support.pingidentity.com/s/article/After-deleting-an-AD-user-account-SaaS-provisioner-does-not-remove-the-user-in-the-next-provisioning-cycle-when-Group-DN-is-specified) in the Knowledge Base.

* Due to PingFederate limitations, user attributes cannot be cleared once set.

* Due to PingFederate limitations, the Group name is the only supported group attribute and must be the Common Name (CN) of the LDAP Group being provisioned. Additional group attributes are not supported in PingFederate.

* Performance

  * Zscaler SCIM servers have a rate limit of 5 requests per second. In order to avoid retries, reduce the number of threads in the PingFederate channel configuration. For more information, see [Specifying channel information](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_saaschanneltasklet_saasgeneralinfostate.html) in the PingFederate documentation and [SCIM API Examples](https://help.zscaler.com/zia/scim-api-examples) in the Zscaler documentation.

  * When provisioning users to a group, all users must be set to active. If an inactive user is present, the active users and group will be provisioned but no users will be added to the group.

  * Rate limiting can prevent the connector from provisioning users to groups. If rate limiting forces a retry, and a user is created on the retry, the user's group memberships are applied the next time the relevant groups are updated.

---

---
title: Overview of Zscaler integrations
description: The Zscaler Internet Access Connector allows PingFederate to integrate with Zscaler Internet Access for user provisioning, group provisioning, and single sign-on (SSO).
component: zscaler
page_id: zscaler::pf_is_overview_zscaler_integrations
canonical_url: https://docs.pingidentity.com/integrations/zscaler/pf_is_overview_zscaler_integrations.html
llms_txt: https://docs.pingidentity.com/integrations/zscaler/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 29, 2026
section_ids:
  zscaler-internet-access-connector: Zscaler Internet Access Connector
  zscaler-private-access-connector: Zscaler Private Access Connector
  configuring-pingfederate-as-an-external-idp-for-zidentity: Configuring PingFederate as an External IdP for ZIdentity
---

# Overview of Zscaler integrations

## Zscaler Internet Access Connector

The Zscaler Internet Access Connector allows PingFederate to integrate with Zscaler Internet Access for user provisioning, group provisioning, and single sign-on (SSO).

## Zscaler Private Access Connector

The Zscaler Private Access Connector allows PingFederate to integrate with Zscaler Private Access for user provisioning, group provisioning, and single sign-on (SSO).

## Configuring PingFederate as an External IdP for ZIdentity

Ping Identity and ZScaler have collaborated on a guide to configuring PingFederate as an external identity provider (IdP) *(tooltip: \<div class="paragraph">
\<p>A service that manages identity information and provides authentication services to relying clients or SPs within a federated or distributed network.\</p>
\</div>)* for ZIdentity.

Learn more in [Configuring PingFederate as an External IdP](https://help.zscaler.com/authentication-service/configuring-pingfederate-external-idp) in the ZScaler documentation.

---

---
title: Provisioning options reference
description: The following are setting descriptions for the Zscaler Internet Access provisioning capabilities.
component: zscaler
page_id: zscaler:zscaler_internet_access_provisioner:pf_zscaler_zia_connector_provisioning_options_reference
canonical_url: https://docs.pingidentity.com/integrations/zscaler/zscaler_internet_access_provisioner/pf_zscaler_zia_connector_provisioning_options_reference.html
llms_txt: https://docs.pingidentity.com/integrations/zscaler/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 18, 2024
---

# Provisioning options reference

The following are setting descriptions for the Zscaler Internet Access provisioning capabilities.

| Field Name      | Description                                                                                                                                                                   |
| --------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **User Create** | * Selected (default)

  PingFederate creates users in Zscaler Internet Access.

* Cleared

  PingFederate does not create users in Zscaler Internet Access.                   |
| **User Update** | - Selected (default)

  PingFederate updates existing users in Zscaler Internet Access.

- Cleared

  PingFederate does not update existing users in Zscaler Internet Access. |
| **User Delete** | * Selected (default)

  PingFederate removes users from Zscaler Internet Access.

* Cleared

  PingFederate does not remove users from Zscaler Internet Access.               |

|   |                                                                                                                                                                |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | If any of the above options are cleared, PingFederate logs a warning in the user workflow section of the `provisioner.log` file when the related action fails. |

---

---
title: Provisioning options reference
description: Lists the main provisioning capabilities available in the Zscaler connection configuration.
component: zscaler
page_id: zscaler:zscaler_private_access_provisioner:pf_zscaler_zpa_connector_provisioning_options_reference
canonical_url: https://docs.pingidentity.com/integrations/zscaler/zscaler_private_access_provisioner/pf_zscaler_zpa_connector_provisioning_options_reference.html
llms_txt: https://docs.pingidentity.com/integrations/zscaler/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 18, 2024
---

# Provisioning options reference

Lists the main provisioning capabilities available in the Zscaler connection configuration.

| Field Name                                                                                                                                                    | Description                                                                                                                                                                                                                                                                                                                                                                                                                   |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **User Create**                                                                                                                                               | **Selected** (default) – PingFederate creates users in Zscaler.**Cleared** – PingFederate does not create users in Zscaler.                                                                                                                                                                                                                                                                                                   |
| **User Update**                                                                                                                                               | **Selected** (default) – PingFederate updates existing users in Zscaler.**Cleared** – PingFederate does not update existing users in Zscaler.                                                                                                                                                                                                                                                                                 |
| **User Disable / User Delete**                                                                                                                                | **Selected** (default) – PingFederate disables or deletes users in Zscaler according to the **Remove User Action** setting.**Cleared** – PingFederate does not disable or delete users in Zscaler.                                                                                                                                                                                                                            |
| &#xA;&#xA;If any of the above options are cleared, PingFederate logs a warning in the user workflow section of provisioner.log when the related action fails. |                                                                                                                                                                                                                                                                                                                                                                                                                               |
| **Remove User Action**                                                                                                                                        | This option applies when **User Disable / User Delete** is selected and either of the following is true:- a previously provisioned user no longer meets the condition set on the **Source Location** tab.

- a user has been disabled or deleted from the data store.**Disable** (default) – PingFederate disables the user in Zscaler Private Access.**Delete** – PingFederate deletes the user from Zscaler Private Access. |

---

---
title: Registering PingFederate as an identity provider in Zscaler
description: Export your PingFederate signing certificate and use it to configure SAML in Zscaler Internet Access.
component: zscaler
page_id: zscaler:zscaler_internet_access_provisioner:pf_zscaler_zia_connector_registering_pf_as_an_identity_provider_in_zscaler
canonical_url: https://docs.pingidentity.com/integrations/zscaler/zscaler_internet_access_provisioner/pf_zscaler_zia_connector_registering_pf_as_an_identity_provider_in_zscaler.html
llms_txt: https://docs.pingidentity.com/integrations/zscaler/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 18, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Registering PingFederate as an identity provider in Zscaler

Export your PingFederate signing certificate and use it to configure SAML in Zscaler Internet Access.

## About this task

For more information on setting up single sign-on (SSO), see [Configuring SAML](https://help.zscaler.com/zia/configuring-saml) in the Zscaler Internet Access documentation.

## Steps

1. In PingFederate, export your signing certificate:

   1. Go to **Security > Signing & Decryption Keys & Certificates**.

   2. For the certificate that you want to use, in the **Action** column, click **Export**.

   3. On the **Export Certificate** tab, click **Next**.

   4. On the **Export & Summary** tab, click **Export**.

   5. Open the `.crt` file in a text editor and copy the contents.

   6. Rename the file extension to `.pem`.

2. In Zscaler Internet Access, configure SAML:

   1. Go to **Administration > Authentication > Authentication Settings**.

   2. On the **Authentication Profile** tab, in the **Authentication Type** section, select **SAML**. Click **Configure SAML**.

      ![A screenshot that shows the Authentication Profile settings with SAML selected.](_images/uvl1563995878221.png)

   3. In the **SAML Portal URL** field, enter your PingFederate SSO endpoint. For example:

      ```none
      https://<pf_host>:<pf_port>/idp/SSO.saml2
      ```

   4. In the **Login Name Attribute** field, enter the LDAP attribute that maps to the login name that users enter when they authentication with Zscaler Internet Access, such as `NameID`.

   5. In the **Public SSL Certificate** section, click **Upload**. Click **Choose File**, select the `.pem` file that you exported from PingFederate, and then click **Upload**.

   6. Click **Save** to exit the window.

   7. Click **Save** and activate the change as shown in [Saving and Activating Changes in the Admin Portal](https://help.zscaler.com/zia/saving-and-activating-changes-admin-portal) in the Zscaler Internet Access documentation.