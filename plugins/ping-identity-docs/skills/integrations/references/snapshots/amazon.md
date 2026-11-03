---
title: Access control in AWS using session tags
description: Amazon Web Services (AWS) session tags allow enterprises to use Ping Identity products for attribute-based access control (ABAC) in the AWS Single Sign-On (SSO) service.
component: amazon
page_id: amazon:aws_iam_identity_center_provisioner:pf_aws_singlesignon_connector_access_control_in_aws_using_session_tags
canonical_url: https://docs.pingidentity.com/integrations/amazon/aws_iam_identity_center_provisioner/pf_aws_singlesignon_connector_access_control_in_aws_using_session_tags.html
llms_txt: https://docs.pingidentity.com/integrations/amazon/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 3, 2024
---

# Access control in AWS using session tags

Amazon Web Services (AWS) session tags allow enterprises to use Ping Identity products for attribute-based access control (ABAC) in the AWS Single Sign-On (SSO) service.

For information and configuration steps, see [Amazon Web Services session tags integrations](../amazon_web_services_session_tags_integrations_guide/pf_awssessiontags_integration_amazon_web_services_session_tags_integrations_guide.html) in the Ping Identity integration documentation.

---

---
title: Deploying the integration files
description: To get started with the integration, deploy the Amazon Login Integration Kit files to your PingFederate directory.
component: amazon
page_id: amazon:amazon_login_integration_kit:pf_amazon_cic_deploying_the_integration_files
canonical_url: https://docs.pingidentity.com/integrations/amazon/amazon_login_integration_kit/pf_amazon_cic_deploying_the_integration_files.html
llms_txt: https://docs.pingidentity.com/integrations/amazon/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: October 24, 2025
section_ids:
  steps: Steps
---

# Deploying the integration files

To get started with the integration, deploy the Amazon Login Integration Kit files to your PingFederate directory.

## Steps

1. Download the Amazon Login Integration Kit `.zip` archive from the [**Add-ons** tab of the PingFederate downloads page](https://www.pingidentity.com/en/resources/downloads/pingfederate.html) or the [Ping Identity Marketplace](https://marketplace.pingone.com/item/amazon-login-integration-kit).

2. Stop PingFederate.

3. If you're upgrading an existing deployment, back up your customizations and delete earlier versions of the integration files:

   1. Back up any Amazon Login Integration Kit files that you customized in the `<pf_install>/pingfederate/server/default/conf/` directory.

   2. Delete the `pf-amazon-idp-adapter-<version>.jar` file from your `<pf_install>/pingfederate/server/default/deploy` directory.

4. Extract the `.zip` archive and merge the contents of the `dist` directory with your `<pf_install>/pingfederate` directory.

5. If there is more than one version of the `pf-authn-api-sdk-<version>.jar` file in your `<pf_install>/pingfederate/server/default/lib` directory, delete all but the latest version of the file.

6. If you backed up any customized files, modify the new files with your customizations.

7. Start PingFederate.

8. If you operate PingFederate in a cluster, repeat steps 2 - 8 for each engine node.

---

---
title: Deploying the integration files
description: To get started with the integration, deploy the Amazon Web Services Connector files to your PingFederate installation directory. This must be done on the administrative node installation first, regardless of whether you use PingFederate in STANDALONE mode or as part of a cluster.
component: amazon
page_id: amazon:amazon_web_services_connector:pf_aws_connector_deploying_the_integration_files
canonical_url: https://docs.pingidentity.com/integrations/amazon/amazon_web_services_connector/pf_aws_connector_deploying_the_integration_files.html
llms_txt: https://docs.pingidentity.com/integrations/amazon/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 23, 2024
section_ids:
  steps: Steps
  result: Result:
---

# Deploying the integration files

To get started with the integration, deploy the Amazon Web Services Connector files to your PingFederate installation directory. This must be done on the administrative node installation first, regardless of whether you use PingFederate in `STANDALONE` mode or as part of a cluster.

## Steps

1. Download the Amazon Web Services Connector `.zip` archive from the [**Add-ons** tab of the PingFederate downloads page](https://www.pingidentity.com/en/resources/downloads/pingfederate.html) or the [Ping Identity Marketplace](https://marketplace.pingone.com/item/amazon-web-services-sso-integration).

2. Stop PingFederate.

3. If you're upgrading an existing deployment, delete the `pf-aws-quickconnection-<version>.jar` file from your `<pf_install>/pingfederate/server/default/deploy` directory.

4. Extract the `.zip` archive and copy the `pf-aws-quickconnection-<version>.jar` file from the `dist` directory to the `<pf_install>/pingfederate/server/default/deploy` directory.

   |   |                                                                                                                                                                               |
   | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | You will use the supplied `aws-saml-metadata.xml` file later in the [Creating a provisioning connection](pf_aws_connector_creating_a_provisioning_connection.html) procedure. |

5. Enable the PingFederate provisioning engine:

   1. Open your `<pf_install>/pingfederate/bin/run.properties` file.

   2. Change `pf.provisioner.mode` to `STANDALONE`. Save the file.

      |   |                                                                                                                                                                                                                                        |
      | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      |   | To configure the `FAILOVER` mode instead, see [Deploying provisioning failover](https://docs.pingidentity.com/pingfederate/latest/server_clustering_guide/pf_deploy_provis_failover.html) in the PingFederate Server Clustering Guide. |

6. Start PingFederate.

   ### Result:

   If you are using the PingFederate provisioning engine in `STANDALONE` mode on the administrative node, you have completed the deploying the integration files procedure. Otherwise, continue to step 7.

7. If you are using the PingFederate provisioning engine in any mode other than `STANDALONE` mode, including `FAILOVER` mode in a clustered environment, repeat steps 2-4 and step 6 for each engine node.

---

---
title: Deploying the integration files
description: To get started with the integration, deploy the AWS IAM Identity Center Provisioner files to your PingFederate directory.
component: amazon
page_id: amazon:aws_iam_identity_center_provisioner:pf_aws_singlesignon_connector_deploying_the_integration_files
canonical_url: https://docs.pingidentity.com/integrations/amazon/aws_iam_identity_center_provisioner/pf_aws_singlesignon_connector_deploying_the_integration_files.html
llms_txt: https://docs.pingidentity.com/integrations/amazon/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 27, 2026
section_ids:
  steps: Steps
---

# Deploying the integration files

To get started with the integration, deploy the AWS IAM Identity Center Provisioner files to your PingFederate directory.

## Steps

1. Download the AWS IAM Identity Center Provisioner `.zip` archive from the [**Add-ons** tab of the PingFederate downloads page](https://www.pingidentity.com/en/resources/downloads/pingfederate.html) or the [Ping Identity Marketplace](https://marketplace.pingone.com/item/aws-iam-identity-center-provisioner).

2. Stop PingFederate.

3. If you're upgrading an existing deployment, delete the `pf-aws-sso-quickconnection-<version>.jar` file from the filepath`<pf_install>/pingfederate/server/default/deploy` directory in your admin node.

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
description: The following files are included in the Amazon Login Integration Kit .zip archive:
component: amazon
page_id: amazon:amazon_login_integration_kit:pf_amazon_cic_download_manifest
canonical_url: https://docs.pingidentity.com/integrations/amazon/amazon_login_integration_kit/pf_amazon_cic_download_manifest.html
llms_txt: https://docs.pingidentity.com/integrations/amazon/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: January 21, 2026
---

# Download manifest

The following files are included in the Amazon Login Integration Kit `.zip` archive:

* `ReadMeFirst.pdf`: Contains links to this online documentation.

* `legal/Legal.pdf`: Contains copyright and license information.

* `dist` – contains the integration files

  * `deploy` – contains the Java libraries

    * `pf-amazon-idp-adapter-<version>.jar`: A `.jar` file that contains the Amazon IdP Adapter.

  * `conf`: Contains the HTML template that presents the Amazon sign-on form.

    * `language-packs`: Contains files with customizable user-facing messages.

      * `pingfederate-amazon-adapter-messages.properties`: A variable file that customizes the messages that appear on the template files.

    * `template`: Contains user-facing HTML template files.

      * `amazon-pop-up-template.html`: A template that opens a pop-up window to prompt the user to sign on.

      * `amazon-post-auth-template.html`: A template that returns the user to the PingFederate sign-on flow after they sign on with Amazon.

      * `assets`: Contains functional scripts and files used by the template.

        * `css/amazon.css`: A CSS file that customizes the appearance of the template files.

        * `fonts/end-user`: Contains template fonts and icons.

          * `icons`: Contains template icons.

        * `images`: Contains template image files.

          * `ping-logo.svg`: An image file with company branding.

  * `lib/pf-authn-api-sdk-<version>.jar`: A `.jar` file that contains the PingFederate Authentication API SDK.

---

---
title: Download manifest
description: The following files are included in the Amazon Web Services Connector .zip archive:
component: amazon
page_id: amazon:amazon_web_services_connector:pf_aws_connector_download_manifest
canonical_url: https://docs.pingidentity.com/integrations/amazon/amazon_web_services_connector/pf_aws_connector_download_manifest.html
llms_txt: https://docs.pingidentity.com/integrations/amazon/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 3, 2024
---

# Download manifest

The following files are included in the Amazon Web Services Connector `.zip` archive:

* `legal/Legal.pdf` – copyright and license information.

* `dist` – contains the integration files

  * `pf-aws-quickconnection-<version>.jar` – The Amazon Web Services Connector quick connection template.

* `aws-saml-metadata.xml` – a modifiable metadata file used to create the connection.

---

---
title: Download manifest
description: The following files are included in the AWS IAM Identity Center Provisioner .zip archive:
component: amazon
page_id: amazon:aws_iam_identity_center_provisioner:pf_aws_singlesignon_connector_download_manifest
canonical_url: https://docs.pingidentity.com/integrations/amazon/aws_iam_identity_center_provisioner/pf_aws_singlesignon_connector_download_manifest.html
llms_txt: https://docs.pingidentity.com/integrations/amazon/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 3, 2024
---

# Download manifest

The following files are included in the AWS IAM Identity Center Provisioner `.zip` archive:

* `Legal.pdf` – copyright and license information

* `dist` – contains the integration files

  * `pf-aws-sso-quickconnection-<version>.jar` – The AWS IAM Identity Center Provisioner quick connection template.

---

---
title: Enabling debug logging
description: To help with troubleshooting or monitoring, you can turn on activity logging for the adapter.
component: amazon
page_id: amazon:amazon_login_integration_kit:pf_amazon_cic_enabling_debug_logging
canonical_url: https://docs.pingidentity.com/integrations/amazon/amazon_login_integration_kit/pf_amazon_cic_enabling_debug_logging.html
llms_txt: https://docs.pingidentity.com/integrations/amazon/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 10, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Enabling debug logging

To help with troubleshooting or monitoring, you can turn on activity logging for the adapter.

## About this task

These steps are optional. You can find general information about logging in [Enabling debug messages and console logging](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_enabling_debug_message_and_console_logging.html) in the PingFederate documentation.

## Steps

1. Open the `<pf_install>/pingfederate/server/default/conf/log4j2.xml` file for editing.

2. If you want to log activity for PingFederate and all adapters, do the following:

   1. Find the following section:

      ```html
      <AsyncRoot level="INFO" includeLocation="false">
      	<!-- <AppenderRef ref="CONSOLE" /> -->
      	<AppenderRef ref="FILE" />
      </AsyncRoot>
      ```

   2. Change `INFO` to `DEBUG`:

      ```html
      <AsyncRoot level="DEBUG" includeLocation="false">
      	<!-- <AppenderRef ref="CONSOLE" /> -->
      	<AppenderRef ref="FILE" />
      </AsyncRoot>
      ```

   3. If you want to see the adapter activity in the console, remove the comment tags:

      ```html
      <AsyncRoot level="INFO" includeLocation="false">
      	<AppenderRef ref="CONSOLE" />
      	<AppenderRef ref="FILE" />
      </AsyncRoot>
      ```

3. If you want to log activity for the Amazon IdP Adapter only, add the following line:

   ```html
   <Logger name="com.pingidentity.adapter.idp.amazon" level="DEBUG"/>
   ```

4. Save the file.

---

---
title: Enabling provisioning and single sign-on in PingFederate
description: To use PingFederate for provisioning and single sign-on, configure an external datastore and set a SAML entity ID.
component: amazon
page_id: amazon:aws_iam_identity_center_provisioner:pf_aws_singlesignon_connector_enabling_provisioning_and_single_sign_on_in_pf
canonical_url: https://docs.pingidentity.com/integrations/amazon/aws_iam_identity_center_provisioner/pf_aws_singlesignon_connector_enabling_provisioning_and_single_sign_on_in_pf.html
llms_txt: https://docs.pingidentity.com/integrations/amazon/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 3, 2024
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
component: amazon
page_id: amazon:aws_iam_identity_center_provisioner:pf_aws_singlesignon_connector_enabling_provisioning_and_single_sign_on_in_pf_100_or_earlier
canonical_url: https://docs.pingidentity.com/integrations/amazon/aws_iam_identity_center_provisioner/pf_aws_singlesignon_connector_enabling_provisioning_and_single_sign_on_in_pf_100_or_earlier.html
llms_txt: https://docs.pingidentity.com/integrations/amazon/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 3, 2024
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
component: amazon
page_id: amazon:aws_iam_identity_center_provisioner:pf_aws_singlesignon_connector_enabling_provisioning_and_sso_in_pf_101_or_later
canonical_url: https://docs.pingidentity.com/integrations/amazon/aws_iam_identity_center_provisioner/pf_aws_singlesignon_connector_enabling_provisioning_and_sso_in_pf_101_or_later.html
llms_txt: https://docs.pingidentity.com/integrations/amazon/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 3, 2024
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
title: Exporting SAML metadata from PingFederate
description: Export a metadata file that describes your PingFederate identity provider configuration.
component: amazon
page_id: amazon:amazon_web_services_connector:pf_aws_connector_exporting_saml_metadata_from_pf
canonical_url: https://docs.pingidentity.com/integrations/amazon/amazon_web_services_connector/pf_aws_connector_exporting_saml_metadata_from_pf.html
llms_txt: https://docs.pingidentity.com/integrations/amazon/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 3, 2024
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

1. In the PingFederate administrative console, go to the **Metadata Export** window.

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
title: Exporting SAML metadata from PingFederate
description: Export a metadata file that describes your PingFederate identity provider configuration.
component: amazon
page_id: amazon:aws_iam_identity_center_provisioner:pf_aws_singlesignon_connector_exporting_saml_metadata_from_pf
canonical_url: https://docs.pingidentity.com/integrations/amazon/aws_iam_identity_center_provisioner/pf_aws_singlesignon_connector_exporting_saml_metadata_from_pf.html
llms_txt: https://docs.pingidentity.com/integrations/amazon/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 3, 2024
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

1. In the PingFederate administrative console, go to the **Metadata Export** window.

   ### Choose from:

   * For PingFederate 10.1 or later: go to **System > Protocol Metadata > Metadata Export**.

   * For PingFederate 10.0 or earlier: go to **System > Metadata Export**.

2. If you see the **Metadata Role** tab, select **I am the identity provider (IdP)**. Click **Next**.

3. On the **Metadata Mode** tab, select **Select information to include in metadata manually**. Click **Next**.

4. On the **Protocol** tab, click **Next**.

5. On the **Attribute Contract** tab, click **Next**.

6. On the **Signing Key** tab, select a signing certificate. Click **Next**.

7. **Optional:** On the **Metadata Signing** tab, select a certificate to sign the metadata XML file. Click **Next**.

8. On the **XML Encryption Certificate** tab, click **Next**.

9. On the **Export & Summary** tab, click **Export**.

10. Save `metadata.xml`.

11. Click **Done**.

---

---
title: Integrating social sign-on into your application
description: To complete your Amazon sign-on integration, add a sign-on hyperlink to your application.
component: amazon
page_id: amazon:amazon_login_integration_kit:pf_amazon_cic_integrating_social_sign_on_into_your_application
canonical_url: https://docs.pingidentity.com/integrations/amazon/amazon_login_integration_kit/pf_amazon_cic_integrating_social_sign_on_into_your_application.html
llms_txt: https://docs.pingidentity.com/integrations/amazon/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: October 24, 2025
section_ids:
  steps: Steps
---

# Integrating social sign-on into your application

To complete your Amazon sign-on integration, add a sign-on hyperlink to your application.

## Steps

1. If your application is outside the PingFederate domain, configure an SP connection as follows:

   1. Create a service provider (SP) *(tooltip: \<div class="paragraph">
      \<p>In SAML, an entity that receives and accepts an authentication assertion issued by an IdP, typically for the purpose of allowing access to a protected resource.\</p>
      \</div>)* connection as shown in [SP connection management](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_sp_connect_management.html) and [Mapping an adapter instance](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_mapping_adapter_instance.html) in the PingFederate documentation.

      |   |                                                                  |
      | - | ---------------------------------------------------------------- |
      |   | Use the Amazon IdP Adapter instance as an authentication source. |

   2. In your web application, create a hyperlink to allow users to sign on to the SP application. Use the following URL and replace the variables based on the descriptions in the following table.

      ```none
      https://<pf_host>:<pf_port>/idp/startSSO.ping?PartnerSpId=<ConnectionId>
      ```

      > **Collapse: Variables**
      >
      > | Variable          | Description                                                                                       |
      > | ----------------- | ------------------------------------------------------------------------------------------------- |
      > | *\<pf_host>*      | The host name or IP address of the PingFederate server.                                           |
      > | *\<pf_port>*      | The port number for PingFederate.                                                                 |
      > | *\<ConnectionId>* | The federation identifier of the SP for the connection that uses the Amazon IdP Adapter instance. |

2. If your application is inside the PingFederate domain, configure an adapter-to-adapter mapping as follows:

   1. On the **System > Protocol Settings > Roles & Protocols** page, select **Enable Identity Provider (IdP) role and support for the following** and **Enable Service Provider (SP) role and support for the following**.

   2. In both the **Enable Identity Provider** and **Enable Service Provider** sections, select any protocol, such as **SAML 2.0**. Click **Save**.

      |   |                                                                                                                                 |
      | - | ------------------------------------------------------------------------------------------------------------------------------- |
      |   | PingFederate requires a protocol selection to activate the roles. The protocol that you select isn't used for this integration. |

   3. On the **Service Provider > Adapters** page, create or select an adapter instance that's integrated with the application as shown in [SP application integration settings](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_sp_applicat_integra_settings.html) in the PingFederate documentation.

   4. On the **Identity Provider > Adapter-to-Adapter Mappings** page, configure the IdP-to-SP adapter mapping as shown in [Adapter-to-adapter mappings](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_adaptertoadapter_mappings.html) in the PingFederate documentation.

   5. In your web application, create a hyperlink to allow users to sign on to the SP application. Use the following URL and replace the variables based on the descriptions in the table below:

      `https://<pf_host>:<pf_port>/pf/adapter2adapter.ping?IdpAdapterId=<IdpAdapterId>&SpSessionAuthnAdapterId=<SpAdapterId>`

      > **Collapse: Variables**
      >
      > | Variable          | Description                                                                        |
      > | ----------------- | ---------------------------------------------------------------------------------- |
      > | *\<pf_host>*      | The host name or IP address of the PingFederate server.                            |
      > | *\<pf_port>*      | The port number for PingFederate.                                                  |
      > | *\<IdpAdapterId>* | The instance ID of the Amazon IdP Adapter instance.                                |
      > | *\<SpAdapterId>*  | The instance ID of the SP adapter instance that's integrated with the application. |

---

---
title: Known issues and limitations
description: The following are known issues or limitations for the Amazon Login Integration Kit.
component: amazon
page_id: amazon:amazon_login_integration_kit:pf_amazon_cic_known_issues_and_limitations
canonical_url: https://docs.pingidentity.com/integrations/amazon/amazon_login_integration_kit/pf_amazon_cic_known_issues_and_limitations.html
llms_txt: https://docs.pingidentity.com/integrations/amazon/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: October 24, 2025
section_ids:
  known-issues: Known issues
  known-limitations: Known limitations
---

# Known issues and limitations

The following are known issues or limitations for the Amazon Login Integration Kit.

## Known issues

There are no known issues.

## Known limitations

* single logout (SLO) *(tooltip: \<div class="paragraph">
  \<p>The process of signing a user out of multiple sites where the user has started a SSO session.\</p>
  \</div>)*

  SLO isn't supported because of a limitation on the Amazon side.

---

---
title: Known issues and limitations
description: There are no known issues.
component: amazon
page_id: amazon:amazon_web_services_connector:pf_aws_connector_known_issues_and_limitations
canonical_url: https://docs.pingidentity.com/integrations/amazon/amazon_web_services_connector/pf_aws_connector_known_issues_and_limitations.html
llms_txt: https://docs.pingidentity.com/integrations/amazon/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 3, 2024
section_ids:
  known-issues: Known issues
  known-limitations: Known limitations
---

# Known issues and limitations

## Known issues

There are no known issues.

## Known limitations

* Groups

  * Before deleting a group, Amazon Web Services (AWS) requires you to remove all users from the group. Otherwise, an error will occur in the AWS API.

  * AWS does not allow a user to be a member of more than 10 groups.

* Deprovisioning

  * AWS does not support disabled users. These users are deleted instead.

  * When an LDAP user is deleted in a targeted Group DN, the provisioning connector does not propagate the deletion until a new user is added to the group. This limitation is compounded when the **User Create** provisioning option is disabled. For solutions, see [SaaS provisioning connector does not remove the user](https://support.pingidentity.com/s/article/After-deleting-an-AD-user-account-SaaS-provisioner-does-not-remove-the-user-in-the-next-provisioning-cycle-when-Group-DN-is-specified) in the Knowledge Base.

* When a user is created with a `passwordResetRequired` value other than `true` or `TRUE`, the provisioning connector sets the value to `false` in AWS.

* Attributes

  * Due to limitations in PingFederate, user attributes cannot be cleared after they are set.

  * Due to limitations in PingFederate, the "Create only" attribute mapping option is not available for the `UserName` attribute.

* In PingFederate 8.1 and earlier, when you configure a second SP connection with the provisioning connector, the second connection may be pre-populated with the channel from the first connection. To avoid conflicts, remove this pre-populated channel and create a unique channel for each connection.

---

---
title: Known issues and limitations
description: The following are known issues or limitations with the AWS IAM Identity Center Provisioner.
component: amazon
page_id: amazon:aws_iam_identity_center_provisioner:pf_aws_singlesignon_connector_known_issues_and_limitations
canonical_url: https://docs.pingidentity.com/integrations/amazon/aws_iam_identity_center_provisioner/pf_aws_singlesignon_connector_known_issues_and_limitations.html
llms_txt: https://docs.pingidentity.com/integrations/amazon/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 3, 2024
section_ids:
  known-issues: Known issues
  known-limitations: Known limitations
---

# Known issues and limitations

The following are known issues or limitations with the AWS IAM Identity Center Provisioner.

## Known issues

There are no known issues.

## Known limitations

* Attributes

  * After an attribute is set, it can be updated but not cleared.

* Deprovisioning

  * When an LDAP user is deleted in a targeted group distinguished name (DN), the provisioning connector does not propagate the deletion until a new user is added to the group. This limitation is compounded when the **User Create** provisioning option is disabled. For solutions, see [SaaS provisioner does not remove the user](https://support.pingidentity.com/s/article/After-deleting-an-AD-user-account-SaaS-provisioner-does-not-remove-the-user-in-the-next-provisioning-cycle-when-Group-DN-is-specified) in the Knowledge Base.

---

---
title: Overview of the SSO flow
description: With the Amazon Login Integration Kit, PingFederate includes an Amazon authentication server in the sign-on flow to access service provider (SP) applications.
component: amazon
page_id: amazon:amazon_login_integration_kit:pf_amazon_cic_overview_of_the_sso_flow
canonical_url: https://docs.pingidentity.com/integrations/amazon/amazon_login_integration_kit/pf_amazon_cic_overview_of_the_sso_flow.html
llms_txt: https://docs.pingidentity.com/integrations/amazon/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: October 24, 2025
section_ids:
  processing-steps: Processing Steps
---

# Overview of the SSO flow

With the Amazon Login Integration Kit, PingFederate includes an Amazon authentication server in the sign-on flow to access service provider (SP) *(tooltip: \<div class="paragraph">
\<p>In SAML, an entity that receives and accepts an authentication assertion issued by an IdP, typically for the purpose of allowing access to a protected resource.\</p>
\</div>)* applications.

The following diagram shows a SP-initiated SSO *(tooltip: \<div class="paragraph">
\<p>In SAML, an identity federation transaction in which the initial action for SSO occurs at the SP site.\</p>
\</div>)* scenario in which PingFederate authenticates users to an SP application using the Amazon IdP Adapter.

![Diagram showing SP-initiated SSO with PingFederate and Amazon.](_images/amazon_login_ik_sso_flow_overview_diagram.png)

## Processing Steps

1. The user opens a web application and selects the Amazon sign-on option.

2. The sign-on link points to the PingFederate Amazon IdP Adapter, which redirects the browser to Amazon with a list of requested permissions and the authorization callback endpoint.

3. On Amazon, the user authenticates their identity and then authorizes the requested permissions.

4. Amazon redirects the browser to the PingFederate Amazon IdP Adapter authorization callback endpoint.

5. Amazon includes an authorization code while redirecting the browser.

   If the user fails to authenticate or doesn't authorize the request, the response includes an error code instead.

6. PingFederate sends Amazon the client ID, client secret, authorization code, and the PingFederate authorization callback URL.

7. Amazon returns an access token.

8. PingFederate sends Amazon a request for user attributes and presents the access token.

9. Amazon verifies the access token and provides the user information.

10. PingFederate redirects the user to the web application with the user attributes.

---

---
title: Provisioning options
description: User Create
component: amazon
page_id: amazon:amazon_web_services_connector:pf_aws_connector_provisioning_options
canonical_url: https://docs.pingidentity.com/integrations/amazon/amazon_web_services_connector/pf_aws_connector_provisioning_options.html
llms_txt: https://docs.pingidentity.com/integrations/amazon/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 3, 2024
---

# Provisioning options

| Field Name                                                                                                                                                    | Description                                                                                                                               |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| **User Create**                                                                                                                                               | **Selected** (default) – PingFederate creates users in Amazon Web Services (AWS).**Cleared** – PingFederate does not create users in AWS. |
| **User Update**                                                                                                                                               | **Selected** (default) – PingFederate updates existing users in AWS.**Cleared** – PingFederate does not update existing users in AWS.     |
| **User Delete**                                                                                                                                               | **Selected** (default) – PingFederate deletes users in AWS.**Cleared** – PingFederate does not delete users in AWS.                       |
| &#xA;&#xA;If any of the above options are cleared, PingFederate logs a warning in the user workflow section of provisioner.log when the related action fails. |                                                                                                                                           |

---

---
title: Provisioning options reference
description: The AWS IAM Identity Center Provisioner allows you to enable actions independently and customize other provisioning options.
component: amazon
page_id: amazon:aws_iam_identity_center_provisioner:pf_aws_singlesignon_connector_provisioning_options_reference
canonical_url: https://docs.pingidentity.com/integrations/amazon/aws_iam_identity_center_provisioner/pf_aws_singlesignon_connector_provisioning_options_reference.html
llms_txt: https://docs.pingidentity.com/integrations/amazon/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 3, 2024
---

# Provisioning options reference

The AWS IAM Identity Center Provisioner allows you to enable actions independently and customize other provisioning options.

| Field Name                   | Description                                                                                                                                                                                                                                                                                                                                                                                                 |
| ---------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **User Create**              | * Selected (default)

  PingFederate creates users in AWS IAM Identity Center.

* Cleared

  PingFederate does not create users in AWS IAM Identity Center.                                                                                                                                                                                                                                                 |
| **User Update**              | - Selected (default)

  PingFederate updates existing users in AWS IAM Identity Center.

- Cleared

  PingFederate does not update existing users in AWS IAM Identity Center.                                                                                                                                                                                                                               |
| **User Disable / Delete**    | * Selected (default)

  PingFederate removes users from AWS IAM Identity Center according to the **Remove User Action** setting.

* Cleared

  PingFederate does not remove users from AWS IAM Identity Center.                                                                                                                                                                                             |
| **Provision Disabled Users** | - Selected

  PingFederate creates users in AWS IAM Identity Center with a "disabled" status.

- Cleared (default)

  If a user has a "disable" status, PingFederate does not create the user in AWS IAM Identity Center.                                                                                                                                                                                   |
|                              | &#xA;&#xA;If any of the above options are cleared, PingFederate logs a warning in the user workflow section of provisioner.log when the related action fails.                                                                                                                                                                                                                                               |
| **Remove User Action**       | This option applies when:- **User Disable / Delete** is selected, and

- a previously-provisioned user no longer meets the condition set on the **Source Location** tab, or

- a user has been disabled or deleted from the data store.

  * Delete

    PingFederate deletes the user from AWS IAM Identity Center.

  * Disable (default)

    PingFederate disables the user in AWS IAM Identity Center. |