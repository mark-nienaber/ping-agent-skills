---
title: Changelog
description: Added support for handling rate-limiting responses from Slack
component: slack
page_id: slack:release_notes:pf_slack_connector_changelog
canonical_url: https://docs.pingidentity.com/integrations/slack/release_notes/pf_slack_connector_changelog.html
revdate: June 25, 2024
section_ids:
  slack-connector-3-0-2-march-2020: Slack Connector 3.0.2 – March 2020
  slack-connector-3-0-1-november-2019: Slack Connector 3.0.1 – November 2019
  slack-connector-3-0-october-2017: Slack Connector 3.0 – October 2017
  slack-connector-2-2-1-june-2017: Slack Connector 2.2.1 – June 2017
  slack-connector-2-2-may-2017: Slack Connector 2.2 – May 2017
  slack-connector-2-1-1-march-2017: Slack Connector 2.1.1 – March 2017
  slack-connector-2-1-january-2017: Slack Connector 2.1 – January 2017
  slack-connector-2-0-december-2015: Slack Connector 2.0 – December 2015
  slack-connector-1-0-october-2015: Slack Connector 1.0 – October 2015
---

# Changelog

## Slack Connector 3.0.2 – March 2020

* Added support for handling rate-limiting responses from Slack

## Slack Connector 3.0.1 – November 2019

* Fixed an issue that caused the connector to update the wrong phone number attribute as a result of a change in the Slack API

## Slack Connector 3.0 – October 2017

* Added deprovisioning configuration options for CRUD capabilities

* Added support for additional user attributes

## Slack Connector 2.2.1 – June 2017

* Fixed an issue with deserialization the response due to an API change

## Slack Connector 2.2 – May 2017

* Added configuration options for the Unique User Identifier

## Slack Connector 2.1.1 – March 2017

* Optimized HTTP calls to Slack

* Fixed synchronization on update of users that were previously created with "User Create Enabled" set to false in configurable options

## Slack Connector 2.1 – January 2017

* Added configuration options for CRUD capabilities

## Slack Connector 2.0 – December 2015

* Added Support for Group Provisioning

## Slack Connector 1.0 – October 2015

* Initial Release

* Added Support for User Provisioning

---

---
title: Configuring Browser SSO
description: Use the following details for the Browser SSO part of your single sign-on (SSO) connection to Slack.
component: slack
page_id: slack:setup:pf_slack_connector_configuring_browser_sso
canonical_url: https://docs.pingidentity.com/integrations/slack/setup/pf_slack_connector_configuring_browser_sso.html
revdate: July 8, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Configuring Browser SSO

Use the following details for the **Browser SSO** part of your single sign-on (SSO) connection to Slack.

## About this task

|   |                                                                                                                                                                                                                                                                                                                       |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | For all other settings, you can use the default or customize the configuration for your needs. For help, see [Configuring IdP Browser SSO](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_spconnectionconfigtasklet_spbrowserssostate.html) in the PingFederate documentation. |

For more context on subject format requirements, see [SAML NameID Format urn:oasis:names:tc:SAML:2.0:nameid-format:persistent](https://support.pingidentity.com/s/article/SAML-Name-ID-urn-oasis-names-tc-SAML-2-0-nameid-format-persistent) in the Ping Identity Knowledge Center.

## Steps

1. On the **Browser SSO** tab, click **Configure Browser SSO**.

2. On the **Browser SSO > SAML Profiles** tab, select only **IDP-Initiated SSO** and **SP-Initiated SSO**. Click **Next**.

3. On the **Assertion Lifetime** tab, click **Next**.

4. On the **Assertion Creation** tab, configure the assertion.

   The following steps only cover the critical settings for the Slack connection. For a complete guide, see [Managing authentication source mappings](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_assertioncreationtasklet_idpadaptermappingstate.html) in the PingFederate documentation.

   1. Click **Configure Assertion Creation**.

   2. On the **Attribute Contract** tab, set the following name format.

      | Attribute Contract | Subject Name Format                                     |
      | ------------------ | ------------------------------------------------------- |
      | SAML\_SUBJECT      | `urn:oasis:names:tc:SAML:1.1:nameid-format:unspecified` |

   3. In the **Extended the Contract** section, add the following attributes, and then click **Next**.

      **Extend the Contract Mappings**

      | Extend the Contract | Attribute name Format                                     |
      | ------------------- | --------------------------------------------------------- |
      | SAML\_NAME\_FORMAT  | `urn:oasis:names:tc:SAML:2.0:attrname-format:unspecified` |
      | User.Email          | `urn:oasis:names:tc:SAML:2.0:attrname-format:unspecified` |

   4. On the **Authentication Source Mapping** tab, select or create your authentication source.

      For help, see [Managing authentication source mappings](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_assertioncreationtasklet_idpadaptermappingstate.html) in the PingFederate documentation.

   5. On your authentication source **Mapping Method**tab, select **Retrieve additional attributes from a data store**.

   6. On your authentication source **Attribute Sources & User Lookup**tab, select or create your LDAP datastore.

   7. On your authentication source **Attribute Sources & User Lookup**tab, select or create your LDAP datastore. On the **LDAP Directory Search** tab, use the following configuration.

      For more information, see [Specifying directory properties and attributes](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_specify_directory_properties_and_attributes.html) in the PingFederate documentation.

      ![A screenshot that shows the LDAP Directory Search tab](_images/ljw1563995734086.png)

   8. On the **Browser SSO > Assertion Creation > IdP Adapter Mapping > Attribute Contract Fulfillment** tab, map the attributes as follows. Click **Next**.

      |   |                                                                                                                                                                                            |
      | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
      |   | This allows the connection to provide Slack with the required `urn:oasis:names:tc:SAML:2.0:nameid-format:persistent` name format, which PingFederate does not provide as a default option. |

      | Attribute Contract | Source      | Value                                                  |
      | ------------------ | ----------- | ------------------------------------------------------ |
      | SAML\_NAME\_FORMAT | **text**    | `urn:oasis:names:tc:SAML:2.0:nameid-format:persistent` |
      | SAML\_SUBJECT      | **Adapter** | `username`                                             |
      | User.Email         | **LDAP**    | `mail`                                                 |

      ![A screenshot that shows the Attribute Contract Fulfillment tab with the attributes mapped.](_images/vku1563995733409.png)

5. On the **Browser SSO > Protocol Settings > Signature Policy** tab, clear the **Require authn requests…​** and **Always sign assertion** check boxes. Click **Next**.

6. On the **Encryption Policy** tab, select **None**. Click **Next**.

7. On the **Browser SSO > Protocol Settings** tab, click **Next**.

8. On the **Summary** tab, click **Done**.

9. On the **SP Connection > Browser SSO** tab, click **Next**.

---

---
title: Configuring single sign-on
description: To allow PingFederate to act as an identity provider for Slack, create a connection and enable single sign-on (SSO) in Slack.
component: slack
page_id: slack:setup:pf_slack_connector_configuring_single_sign_on
canonical_url: https://docs.pingidentity.com/integrations/slack/setup/pf_slack_connector_configuring_single_sign_on.html
revdate: July 8, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Configuring single sign-on

To allow PingFederate to act as an identity provider for Slack, create a connection and enable single sign-on (SSO) in Slack.

## About this task

|   |                                                                                                                                            |
| - | ------------------------------------------------------------------------------------------------------------------------------------------ |
|   | SSO integration is an optional part of this integration. If you only want to use the Slack Provisioner for provisioning, skip these steps. |

## Steps

1. Complete the steps in [Creating a single sign-on connection](pf_slack_connector_creating_a_single_sign_on_connection.html).

2. Complete the steps in [Configuring single sign-on in Slack](pf_slack_connector_configuring_single_sign_on_in_slack.html).

---

---
title: Configuring single sign-on in Slack
description: To allow PingFederate to manage authentication, enable single sign-on (SSO) in Slack.
component: slack
page_id: slack:setup:pf_slack_connector_configuring_single_sign_on_in_slack
canonical_url: https://docs.pingidentity.com/integrations/slack/setup/pf_slack_connector_configuring_single_sign_on_in_slack.html
revdate: July 8, 2024
section_ids:
  configuring-sso-in-slack-standard-or-plus: Configuring SSO in Slack Standard or Plus
  about-this-task: About this task
  steps: Steps
  result: Result:
  configuring-sso-in-slack-enterprise-grid: Configuring SSO in Slack Enterprise Grid
  about-this-task-2: About this task
  steps-2: Steps
  result-2: Result:
---

# Configuring single sign-on in Slack

To allow PingFederate to manage authentication, enable single sign-on (SSO) in Slack.

## Configuring SSO in Slack Standard or Plus

If you use Slack Standard or Plus, configure SSO as follows.

### About this task

For help, see the [Plus plan](https://slack.com/intl/en-ca/help/articles/203772216-SAML-single-sign-on#plus-plan-1) tab in [SAML single sign-on](https://slack.com/intl/en-ca/help/articles/203772216-SAML-single-sign-on) in the Slack documentation.

### Steps

1. Sign on to Slack as a Workspace Owner.

2. Click your workspace name, and then click **Administration > Workspace Settings**.

3. In the navigation pane, click **Authentication**.

4. On the **Settings & Permissions** page, for **SAML Authentication**, click **Configure**.

5. Select **Custom SAML 2.0** and click **Configure**.

6. In the **SAML 2.0 Endpoint (HTTP)** field, enter `https://pf_host:pf_port/idp/SSO.saml2`.

   For example: `https://pf.example.com:9031/idp/SSO.saml2`

7. In the **Identity Provider Issuer** field, enter the **SAML 2.0 Entity ID** that you created in [Enabling provisioning and single sign-on in PingFederate](pf_slack_connector_enabling_provisioning_and_single_sign_on_in_pf.html).

8. In the **Public Certificate** field, enter the contents of your PingFederate signing certificate.

   To get your certificate, see **Exporting a certificate** in [Managing digital signing certificates and decryption keys](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_certmanagementtasklet_dsigsigningcert_certmanagementstate.html) in the PingFederate documentation.

9. Click **Save Configuration**.

10. Sign out of Slack, and then sign back on using SSO.

    #### Result:

    This saves your configuration and sends an email to team members inviting them set up SSO with their Slack accounts.

## Configuring SSO in Slack Enterprise Grid

If you use Slack Enterprise Grid, configure SSO as follows.

### About this task

For help, see the [Enterprise Grid plan](https://slack.com/intl/en-ca/help/articles/203772216-SAML-single-sign-on#enterprise-grid-plan-1) tab in [SAML single sign-on](https://slack.com/intl/en-ca/help/articles/203772216-SAML-single-sign-on) in the Slack documentation.

### Steps

1. Sign on to Slack Enterprise Grid as a Workspace Owner.

2. Go to **Manage Organization > Security > SSO Settings > Configure SSO**.

   ![A screen recording that shows the dashboard. The user clicks Manage Organization, and then clicks Security.](_images/fvm1617230085096.gif)

3. In the **SAML 2.0 Endpoint (HTTP)** field, enter `https://pf_host:pf_port/idp/SSO.saml2`.

   For example: `https://pf.example.com:9031/idp/SSO.saml2`

4. In the **Identity Provider Issuer** field, enter the **SAML 2.0 Entity ID** that you created in [Enabling provisioning and single sign-on in PingFederate](pf_slack_connector_enabling_provisioning_and_single_sign_on_in_pf.html).

5. In the **Service Provider Issuer URL**, use the default value of **<https://slack.com>**.

6. In the **Public (X.509) Certificate** field, enter the contents of your PingFederate signing certificate.

   To get your certificate, see **Exporting a certificate** in [Managing digital signing certificates and decryption keys](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_certmanagementtasklet_dsigsigningcert_certmanagementstate.html) in the PingFederate documentation.

7. Enable authentication request signing.

   1. Select the **Sign the AuthnRequest** check box.

   2. Copy the certificate text.

   3. Create a new `.crt` file on your computer and paste the certificate text.

   4. In PingFederate, import the `.crt` file as a trusted certificate authority.

   For help, see [Manage trusted certificate authorities](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_certmanagementtasklet_trustedcas_certmanagementstate.html) in the PingFederate documentation.

8. Clear the **Sign the Assertion** check box.

   ![A screenshot that shows the SAML Response Signing section with the correct settings.](_images/bdv1617989116378.jpg)

9. Click **Test Configuration**.

10. Save your configuration.

11. Sign out of Slack, and then sign back on using SSO.

    #### Result:

    This saves your configuration and sends an email to team members inviting them set up SSO with their Slack accounts.

---

---
title: Configuring SSO in Slack Enterprise Grid
description: If you use Slack Enterprise Grid, configure SSO as follows.
component: slack
page_id: slack:setup:pf_slack_connector_configuring_sso_in_slack_enterprise_grid
canonical_url: https://docs.pingidentity.com/integrations/slack/setup/pf_slack_connector_configuring_sso_in_slack_enterprise_grid.html
revdate: July 8, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
  result: Result:
---

# Configuring SSO in Slack Enterprise Grid

If you use Slack Enterprise Grid, configure SSO as follows.

## About this task

For help, see the [Enterprise Grid plan](https://slack.com/intl/en-ca/help/articles/203772216-SAML-single-sign-on#enterprise-grid-plan-1) tab in [SAML single sign-on](https://slack.com/intl/en-ca/help/articles/203772216-SAML-single-sign-on) in the Slack documentation.

## Steps

1. Sign on to Slack Enterprise Grid as a Workspace Owner.

2. Go to **Manage Organization > Security > SSO Settings > Configure SSO**.

   ![A screen recording that shows the dashboard. The user clicks Manage Organization, and then clicks Security.](_images/fvm1617230085096.gif)

3. In the **SAML 2.0 Endpoint (HTTP)** field, enter `https://pf_host:pf_port/idp/SSO.saml2`.

   For example: `https://pf.example.com:9031/idp/SSO.saml2`

4. In the **Identity Provider Issuer** field, enter the **SAML 2.0 Entity ID** that you created in [Enabling provisioning and single sign-on in PingFederate](pf_slack_connector_enabling_provisioning_and_single_sign_on_in_pf.html).

5. In the **Service Provider Issuer URL**, use the default value of **<https://slack.com>**.

6. In the **Public (X.509) Certificate** field, enter the contents of your PingFederate signing certificate.

   To get your certificate, see **Exporting a certificate** in [Managing digital signing certificates and decryption keys](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_certmanagementtasklet_dsigsigningcert_certmanagementstate.html) in the PingFederate documentation.

7. Enable authentication request signing.

   1. Select the **Sign the AuthnRequest** check box.

   2. Copy the certificate text.

   3. Create a new `.crt` file on your computer and paste the certificate text.

   4. In PingFederate, import the `.crt` file as a trusted certificate authority.

   For help, see [Manage trusted certificate authorities](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_certmanagementtasklet_trustedcas_certmanagementstate.html) in the PingFederate documentation.

8. Clear the **Sign the Assertion** check box.

   ![A screenshot that shows the SAML Response Signing section with the correct settings.](_images/bdv1617989116378.jpg)

9. Click **Test Configuration**.

10. Save your configuration.

11. Sign out of Slack, and then sign back on using SSO.

    ### Result:

    This saves your configuration and sends an email to team members inviting them set up SSO with their Slack accounts.

---

---
title: Configuring SSO in Slack Standard or Plus
description: If you use Slack Standard or Plus, configure SSO as follows.
component: slack
page_id: slack:setup:pf_slack_connector_configuring_sso_in_slack_standard_or_plus
canonical_url: https://docs.pingidentity.com/integrations/slack/setup/pf_slack_connector_configuring_sso_in_slack_standard_or_plus.html
revdate: July 8, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
  result: Result:
---

# Configuring SSO in Slack Standard or Plus

If you use Slack Standard or Plus, configure SSO as follows.

## About this task

For help, see the [Plus plan](https://slack.com/intl/en-ca/help/articles/203772216-SAML-single-sign-on#plus-plan-1) tab in [SAML single sign-on](https://slack.com/intl/en-ca/help/articles/203772216-SAML-single-sign-on) in the Slack documentation.

## Steps

1. Sign on to Slack as a Workspace Owner.

2. Click your workspace name, and then click **Administration > Workspace Settings**.

3. In the navigation pane, click **Authentication**.

4. On the **Settings & Permissions** page, for **SAML Authentication**, click **Configure**.

5. Select **Custom SAML 2.0** and click **Configure**.

6. In the **SAML 2.0 Endpoint (HTTP)** field, enter `https://pf_host:pf_port/idp/SSO.saml2`.

   For example: `https://pf.example.com:9031/idp/SSO.saml2`

7. In the **Identity Provider Issuer** field, enter the **SAML 2.0 Entity ID** that you created in [Enabling provisioning and single sign-on in PingFederate](pf_slack_connector_enabling_provisioning_and_single_sign_on_in_pf.html).

8. In the **Public Certificate** field, enter the contents of your PingFederate signing certificate.

   To get your certificate, see **Exporting a certificate** in [Managing digital signing certificates and decryption keys](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_certmanagementtasklet_dsigsigningcert_certmanagementstate.html) in the PingFederate documentation.

9. Click **Save Configuration**.

10. Sign out of Slack, and then sign back on using SSO.

    ### Result:

    This saves your configuration and sends an email to team members inviting them set up SSO with their Slack accounts.

---

---
title: Creating a provisioning connection
description: To allow PingFederate to manage users in Slack, create a service provider (SP) connection.
component: slack
page_id: slack:setup:pf_slack_connector_creating_a_provisioning_connection
canonical_url: https://docs.pingidentity.com/integrations/slack/setup/pf_slack_connector_creating_a_provisioning_connection.html
revdate: July 8, 2024
section_ids:
  steps: Steps
---

# Creating a provisioning connection

To allow PingFederate to manage users in Slack, create a service provider (SP) connection.

## Steps

1. In the PingFederate administrator console, create a new SP connection:

   1. For PingFederate 10.1 or later: go to **Applications > Integration > SP Connections**. Click **Create Connection**.

   2. For PingFederate 10.0 or earlier: go to **Identity Provider > SP Connections**. Click **Create Connection**.

2. Configure the basic connection details with the Slack quick connection template.

   1. On the **Connection Template** tab, select **Use a template for this connection**.

   2. From the **Connection Template** list, select **Slack Provisioner**.

   3. On the **Metadata File** row, select the saml-metadata.xml file that you saved in [Preparing your SAML metadata file](pf_slack_connector_preparing_your_saml_metadata_file.html). Click **Next**.

   4. On the **Connection Type** tab select only **Outbound Provisioning**. Click **Next**.

   5. On the **Connection Options** tab, click **Next**.

   6. On the **General Info** tab, in the **Connection Name** field, enter a name of your choosing. Click **Next**.

3. On the **Outbound Provisioning** tab, configure the provisioning target and channel as shown in [Configuring outbound provisioning](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_spconnectionconfigtasklet_saasprovisioningstate.html) in the PingFederate documentation.

   1. Click **Configure Provisioning**.

   2. On the **Target** tab, enter the **OAuth 2 Access Token** that you noted in [Getting a Slack API access token](pf_slack_connector_getting_a_slack_api_access_token.html).

      |   |                                                                                  |
      | - | -------------------------------------------------------------------------------- |
      |   | PingFederate verifies the token when you activate the channel and SP connection. |

   3. **Optional:** If your environment requires you to use the `userName` attribute to synchronize users between your datastore and Slack, select it from the **Unique User Identifier** list. Otherwise, use `primaryEmail`.

      |   |                                                                                                                                                                              |
      | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      |   | You cannot change this selection without deleting the connection. See [Known issues and limitations](../release_notes/pf_slack_connector_known_issues_and_limitations.html). |

   4. Under **Provisioning Options**, customize the provisioning connector actions as shown in [Provisioning options reference](pf_slack_connector_provisioning_options_reference.html). Click **Next**.

   5. On the **Manage Channels** tab, create a channel as shown in [Managing channels](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_saasmanagementtasklet_saasmanagementstate.html) in the PingFederate documentation. Click **Done**.

      |   |                                                                                                                                                                                  |
      | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      |   | For more information about the attributes available in your channel configuration, see [Supported attributes reference](pf_slack_connector_supported_attributes_reference.html). |

   6. On the **Outbound Provisioning** tab, click **Next**.

4. On the **Activation and Summary** tab, above the **Summary** section, click the toggle to turn on the connection. Click **Save**.

---

---
title: Creating a single sign-on connection
description: To allow PingFederate to handle single sign-on (SSO) to Slack, create a service provider (SP) SSO connection.
component: slack
page_id: slack:setup:pf_slack_connector_creating_a_single_sign_on_connection
canonical_url: https://docs.pingidentity.com/integrations/slack/setup/pf_slack_connector_creating_a_single_sign_on_connection.html
revdate: July 8, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Creating a single sign-on connection

To allow PingFederate to handle single sign-on (SSO) to Slack, create a service provider (SP) SSO connection.

## About this task

|   |                                                                                                     |
| - | --------------------------------------------------------------------------------------------------- |
|   | You can follow these steps to create a new SP connection, or you can modify an existing connection. |

|   |                                                                                                                        |
| - | ---------------------------------------------------------------------------------------------------------------------- |
|   | SSO isn't required for provisioning. If you only want to use the Slack Provisioner for provisioning, skip these steps. |

## Steps

1. In the PingFederate administrator console, create a new SP connection:

   1. For PingFederate 10.1 or later: go to **Applications > Integration > SP Connections**. Click **Create Connection**.

   2. For PingFederate 10.0 or earlier: go to **Identity Provider > SP Connections**. Click **Create Connection**.

2. Configure the basic connection details with the Slack quick connection template.

   1. On the **Connection Template** tab, select **Use a template for this connection**.

   2. From the **Connection Template** list, select **Slack Provisioner**.

   3. On the **Metadata File** row, select the `saml-metadata.xml` file that you saved in [Preparing your SAML metadata file](pf_slack_connector_preparing_your_saml_metadata_file.html). Click **Next**.

   4. On the **Connection Type** tab select **Browser SSO Profiles**. Click **Next**.

   5. On the **Connection Options** tab, select only **Browser SSO**. Click **Next**.

   6. If you see the **Metadata URL** tab, clear the **Enable automatic reloading** check box. Click **Next**.

   7. On the **General Info** tab, in the **Connection Name** field, enter a name for your connection. Click **Next**.

3. On the **Browser SSO** tab, complete the steps in [Configuring Browser SSO](pf_slack_connector_configuring_browser_sso.html).

4. On the **Credentials** tab, configure the connection credentials.

   For a complete guide, see [Configuring credentials](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_spconnectionconfigtasklet_credentialsstate.html) in the PingFederate documentation.

   1. Click **Configure Credentials**.

   2. On the **Digital Signature Settings** tab, select your signing certificate.

   3. Clear the **Include the certificate in the signature \<KEYINFO> element** check box. Click **Next**.

   4. On the **Summary** tab, click **Done**.

   5. On the **SP Connection > Credentials** tab, click **Next**.

5. On the **Activation and Summary** tab, above the **Summary** section, click the toggle to turn on the connection. Click **Save**.

---

---
title: Deploying the integration files
description: To get started with the integration, deploy the Slack Provisioner files to your PingFederate directory.
component: slack
page_id: slack:setup:pf_slack_connector_deploying_the_integration_files
canonical_url: https://docs.pingidentity.com/integrations/slack/setup/pf_slack_connector_deploying_the_integration_files.html
revdate: July 8, 2024
section_ids:
  steps: Steps
---

# Deploying the integration files

To get started with the integration, deploy the Slack Provisioner files to your PingFederate directory.

## Steps

1. Download the Slack Provisioner `.zip` archive from the [**Add-ons** tab of the PingFederate downloads page](https://www.pingidentity.com/en/resources/downloads/pingfederate.html) or the [Ping Identity Marketplace](https://marketplace.pingone.com/item/slack-single-signon-integration).

2. Stop PingFederate.

3. If you're upgrading an existing deployment, delete the `pf-slack-quickconnection-<version>.jar` file from your `<pf_install>/pingfederate/server/default/deploy` directory.

4. Extract the `.zip` archive and merge the contents of the `dist` directory with your `<pf_install>/pingfederate/server/default/deploy` directory.

5. Enable the PingFederate provisioning engine: Open your `<pf_install>/pingfederate/bin/run.properties` file.Change `pf.provisioner.mode` to `STANDALONE`. Save the file.

   |   |                                                                                                                                                                                                                                        |
   | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | To configure the `FAILOVER` mode instead, see [Deploying provisioning failover](https://docs.pingidentity.com/pingfederate/latest/server_clustering_guide/pf_deploy_provis_failover.html) in the PingFederate Server Clustering Guide. |

6. Start PingFederate.

7. If you operate PingFederate in a cluster, repeat steps 2-4 and step 6 for each engine node.

---

---
title: Download manifest
description: The following files are included in the Slack Provisioner .zip archive:
component: slack
page_id: slack:release_notes:pf_slack_connector_download_manifest
canonical_url: https://docs.pingidentity.com/integrations/slack/release_notes/pf_slack_connector_download_manifest.html
revdate: July 8, 2024
---

# Download manifest

The following files are included in the Slack Provisioner `.zip` archive:

* `legal/Legal.pdf` – copyright and license information.

* `dist` – contains the integration files

  * `pf-slack-quickconnection-<version>.jar` – The Slack Provisioner quick connection template.

* `saml-metadata.xml` – a modifiable metadata file used to create the connection.

---

---
title: Enabling provisioning and single sign-on in PingFederate
description: To use PingFederate for provisioning and single sign-on (SSO), configure an external datastore and set a SAML entity ID.
component: slack
page_id: slack:setup:pf_slack_connector_enabling_provisioning_and_single_sign_on_in_pf
canonical_url: https://docs.pingidentity.com/integrations/slack/setup/pf_slack_connector_enabling_provisioning_and_single_sign_on_in_pf.html
revdate: July 8, 2024
section_ids:
  about-this-task: About this task
  enabling-provisioning-and-single-sign-on-in-pingfederate-10-1-or-later: Enabling provisioning and single sign-on in PingFederate 10.1 or later
  steps: Steps
  enabling-provisioning-and-single-sign-on-in-pingfederate-10-0-or-earlier: Enabling provisioning and single sign-on in PingFederate 10.0 or earlier
  steps-2: Steps
---

# Enabling provisioning and single sign-on in PingFederate

To use PingFederate for provisioning and single sign-on (SSO), configure an external datastore and set a SAML entity ID.

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
component: slack
page_id: slack:setup:pf_slack_connector_enabling_provisioning_and_single_sign_on_in_pf_100_or_earlier
canonical_url: https://docs.pingidentity.com/integrations/slack/setup/pf_slack_connector_enabling_provisioning_and_single_sign_on_in_pf_100_or_earlier.html
revdate: July 8, 2024
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
component: slack
page_id: slack:setup:pf_slack_connector_enabling_provisioning_and_single_sign_on_in_pf_101_or_later
canonical_url: https://docs.pingidentity.com/integrations/slack/setup/pf_slack_connector_enabling_provisioning_and_single_sign_on_in_pf_101_or_later.html
revdate: July 8, 2024
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
title: Getting a Slack API access token
description: Use the OAuth Configuration Service to exchange your Slack client ID and secret for an access token. PingFederate uses this access token to connect to Slack. The process differs slightly depending on your plan.
component: slack
page_id: slack:setup:pf_slack_connector_getting_a_slack_api_access_token
canonical_url: https://docs.pingidentity.com/integrations/slack/setup/pf_slack_connector_getting_a_slack_api_access_token.html
revdate: July 8, 2024
section_ids:
  getting-an-access-token-for-slack-standard-or-plus: Getting an access token for Slack Standard or Plus
  steps: Steps
  getting-an-access-token-for-slack-enterprise-grid: Getting an access token for Slack Enterprise Grid
  steps-2: Steps
---

# Getting a Slack API access token

Use the OAuth Configuration Service to exchange your Slack client ID and secret for an access token. PingFederate uses this access token to connect to Slack. The process differs slightly depending on your plan.

## Getting an access token for Slack Standard or Plus

Exchange your Slack Standard or Plus client ID and secret for an access token.

### Steps

1. Go to the Ping Identity [OAuth Configuration Service](https://oauth.pingone.com/ocs/ppm/rest/v1/oauth/oasrequestform).

2. From the product list, select **Slack Connector**.

3. Enter the **Client ID** and **Client Secret** that you noted in [Registering PingFederate as an app in Slack](pf_slack_connector_registering_pf_as_an_app_in_slack.html).

   ![Screenshot showing the OCS with a client ID and secret entered in.](_images/kug1615501848165.jpg)

4. Click **Connect**.

5. If you receive a prompt to sign on, sign on with your Workspace Owner account.

6. When you receive a message that your application is requesting permission to administer your Slack team, click **Authorize**.

7. On the OAuth Configuration Service page, copy the **Access Token**.

   You will use the access token in [Creating a provisioning connection](pf_slack_connector_creating_a_provisioning_connection.html).

   ![Screenshot showing the Ping Identity OAuth Configuration Service with a modal window titled Service Response. The Access Token field has an access token string in it.](_images/jep1615502497836.jpg)

## Getting an access token for Slack Enterprise Grid

Exchange your Slack Enterprise Grid client ID and secret for an access token.

### Steps

1. In an "Incognito" (or "Private") browser window, go to the Ping Identity [OAuth Configuration Service](https://oauth.pingone.com/ocs/ppm/rest/v1/oauth/oasrequestform) (OCS).

2. From the product list, select **Slack Connector**.

3. Enter the **Client ID** and **Client Secret** that you noted in [Registering PingFederate as an app in Slack](pf_slack_connector_registering_pf_as_an_app_in_slack.html).

   ![Screenshot showing the OCS with a client ID and secret entered in.](_images/kug1615501848165.jpg)

4. Click **Connect**.

5. In the **Sign in to your workspace** window, enter the URL for your Slack organization, such as `mycompany.enterprise`**.slack.com**. Click **Continue**.

   ![Screenshot showing the Sign in to your workspace window with the organization ID entered in.](_images/vij1615501965907.jpg)

6. Click **Org Owners can also sign in here**.

   ![Screenshot showing the sign on options.](_images/aad1615502169763.jpg)

7. Enter your administrator credentials. Click **Sign in**.

   ![Screenshot showing the sign-on prompt with administrator credentials entered in.](_images/gxv1615502266804.jpg)

8. When you receive a message that your application is requesting permission, check that the request is for the organization. Do NOT select a Workspace from the **Please select an option** list. Click **Allow**.

   ![Screenshot showing the permission prompt. The word "organization" is highlighted. The Please select an option list does not have a Workplace selected.](_images/fti1615502383665.jpg)

9. On the OAuth Configuration Service page, copy the **Access Token**.

   You will use the access token in [Creating a provisioning connection](pf_slack_connector_creating_a_provisioning_connection.html).

   ![Screenshot showing the Ping Identity OAuth Configuration Service with a modal window titled Service Response. The Access Token field has an access token string in it.](_images/jep1615502497836.jpg)

---

---
title: Getting an access token for Slack Enterprise Grid
description: Exchange your Slack Enterprise Grid client ID and secret for an access token.
component: slack
page_id: slack:setup:pf_slack_connector_getting_an_access_token_for_slack_enterprise_grid
canonical_url: https://docs.pingidentity.com/integrations/slack/setup/pf_slack_connector_getting_an_access_token_for_slack_enterprise_grid.html
revdate: July 8, 2024
section_ids:
  steps: Steps
---

# Getting an access token for Slack Enterprise Grid

Exchange your Slack Enterprise Grid client ID and secret for an access token.

## Steps

1. In an "Incognito" (or "Private") browser window, go to the Ping Identity [OAuth Configuration Service](https://oauth.pingone.com/ocs/ppm/rest/v1/oauth/oasrequestform) (OCS).

2. From the product list, select **Slack Connector**.

3. Enter the **Client ID** and **Client Secret** that you noted in [Registering PingFederate as an app in Slack](pf_slack_connector_registering_pf_as_an_app_in_slack.html).

   ![Screenshot showing the OCS with a client ID and secret entered in.](_images/kug1615501848165.jpg)

4. Click **Connect**.

5. In the **Sign in to your workspace** window, enter the URL for your Slack organization, such as `mycompany.enterprise`**.slack.com**. Click **Continue**.

   ![Screenshot showing the Sign in to your workspace window with the organization ID entered in.](_images/vij1615501965907.jpg)

6. Click **Org Owners can also sign in here**.

   ![Screenshot showing the sign on options.](_images/aad1615502169763.jpg)

7. Enter your administrator credentials. Click **Sign in**.

   ![Screenshot showing the sign-on prompt with administrator credentials entered in.](_images/gxv1615502266804.jpg)

8. When you receive a message that your application is requesting permission, check that the request is for the organization. Do NOT select a Workspace from the **Please select an option** list. Click **Allow**.

   ![Screenshot showing the permission prompt. The word "organization" is highlighted. The Please select an option list does not have a Workplace selected.](_images/fti1615502383665.jpg)

9. On the OAuth Configuration Service page, copy the **Access Token**.

   You will use the access token in [Creating a provisioning connection](pf_slack_connector_creating_a_provisioning_connection.html).

   ![Screenshot showing the Ping Identity OAuth Configuration Service with a modal window titled Service Response. The Access Token field has an access token string in it.](_images/jep1615502497836.jpg)

---

---
title: Getting an access token for Slack Standard or Plus
description: Exchange your Slack Standard or Plus client ID and secret for an access token.
component: slack
page_id: slack:setup:pf_slack_connector_getting_an_access_token_for_slack_standard_or_plus
canonical_url: https://docs.pingidentity.com/integrations/slack/setup/pf_slack_connector_getting_an_access_token_for_slack_standard_or_plus.html
revdate: July 8, 2024
section_ids:
  steps: Steps
---

# Getting an access token for Slack Standard or Plus

Exchange your Slack Standard or Plus client ID and secret for an access token.

## Steps

1. Go to the Ping Identity [OAuth Configuration Service](https://oauth.pingone.com/ocs/ppm/rest/v1/oauth/oasrequestform).

2. From the product list, select **Slack Connector**.

3. Enter the **Client ID** and **Client Secret** that you noted in [Registering PingFederate as an app in Slack](pf_slack_connector_registering_pf_as_an_app_in_slack.html).

   ![Screenshot showing the OCS with a client ID and secret entered in.](_images/kug1615501848165.jpg)

4. Click **Connect**.

5. If you receive a prompt to sign on, sign on with your Workspace Owner account.

6. When you receive a message that your application is requesting permission to administer your Slack team, click **Authorize**.

7. On the OAuth Configuration Service page, copy the **Access Token**.

   You will use the access token in [Creating a provisioning connection](pf_slack_connector_creating_a_provisioning_connection.html).

   ![Screenshot showing the Ping Identity OAuth Configuration Service with a modal window titled Service Response. The Access Token field has an access token string in it.](_images/jep1615502497836.jpg)

---

---
title: Known issues and limitations
description: There are no known issues.
component: slack
page_id: slack:release_notes:pf_slack_connector_known_issues_and_limitations
canonical_url: https://docs.pingidentity.com/integrations/slack/release_notes/pf_slack_connector_known_issues_and_limitations.html
revdate: July 8, 2024
section_ids:
  known-issues: Known issues
  known-limitations: Known limitations
---

# Known issues and limitations

## Known issues

There are no known issues.

## Known limitations

* Attributes

  * Due to a limitation in Slack, the username attribute cannot be updated after it is set.

  * Due to limitations in PingFederate, user attributes cannot be cleared after they are set.

  * The unique user identifier (`userName` or `primaryEmail`) that you choose when you create your connection to Slack can only be changed be deleting the connection, restarting PingFederate, and then creating a new connection.

  * When using multiple channels, the same unique user identifier mapping is required to coordinate manager assignments across different channels.

* Deprovisioning

  * When an LDAP user is deleted in a targeted group distinguished name (DN), the provisioning connector does not propagate the deletion until a new user is added to the group. This limitation is compounded when the **User Create** provisioning option is disabled. For solutions, see [SaaS provisioner does not remove the user](https://support.pingidentity.com/s/article/After-deleting-an-AD-user-account-SaaS-provisioner-does-not-remove-the-user-in-the-next-provisioning-cycle-when-Group-DN-is-specified) in the Knowledge Base.

* Provisioning

  * Due to a limitation in Slack, PingFederate cannot create users in a disabled state. If a user is disabled in your datastore, it will not be created in Slack by the provisioner.

  * For more information on Slack provisioning limitations, see .slack.com/scim//\[SCIM API] in the Slack API documentation.

* Configuration

  * In PingFederate 8.1 and earlier, when you configure a second SP connection with the provisioning connector, the second connection may be pre-populated with the channel from the first connection. To avoid conflicts, remove this pre-populated channel and create a unique channel for each connection.

---

---
title: Preparing your SAML metadata file
description: Modify the SAML details in the included saml-metadata.xml file. This file makes it easier to configure your connection in PingFederate.
component: slack
page_id: slack:setup:pf_slack_connector_preparing_your_saml_metadata_file
canonical_url: https://docs.pingidentity.com/integrations/slack/setup/pf_slack_connector_preparing_your_saml_metadata_file.html
revdate: July 8, 2024
section_ids:
  steps: Steps
---

# Preparing your SAML metadata file

Modify the SAML details in the included `saml-metadata.xml` file. This file makes it easier to configure your connection in PingFederate.

## Steps

1. In a text editor, open the `saml-metadata.xml` file that is included in the Slack Provisioner `.zip` archive.

2. In the `.xml` file, find the `Location="https://TEAM_NAME.slack.com/sso/saml"` line. Modify it with your Slack Workspace or Enterprise Grid name.

   For example, `Location="https://myworkspace.slack.com/sso/saml"`.

3. Remove the trailing slash (`/`) from `entityID="https://slack.com/"`.

   Result: `entityID="https://slack.com"`

4. Save your changes.

   You'll use this file in [Creating a provisioning connection](pf_slack_connector_creating_a_provisioning_connection.html).

---

---
title: Provisioning options reference
description: The table provided lists the main provisioning capabilities available in the Slack connection configuration.
component: slack
page_id: slack:setup:pf_slack_connector_provisioning_options_reference
canonical_url: https://docs.pingidentity.com/integrations/slack/setup/pf_slack_connector_provisioning_options_reference.html
revdate: July 8, 2024
---

# Provisioning options reference

The table provided lists the main provisioning capabilities available in the Slack connection configuration.

| Field Name                                                                                                                                                    | Description                                                                                                                                                                               |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **User Create**                                                                                                                                               | **Selected** (default) – PingFederate creates users in Slack.**Cleared** – PingFederate does not create users in Slack.                                                                   |
| **User Update**                                                                                                                                               | **Selected** (default) – PingFederate updates existing users in Slack. PingFederate can also re-enable disabled users.**Cleared** – PingFederate does not update existing users in Slack. |
| **User Disable**                                                                                                                                              | **Selected** (default) – PingFederate disables users in Slack.**Cleared** – PingFederate does not disable users in Slack.                                                                 |
| &#xA;&#xA;If any of the above options are cleared, PingFederate logs a warning in the user workflow section of provisioner.log when the related action fails. |                                                                                                                                                                                           |

---

---
title: Registering PingFederate as an app in Slack
description: Before PingFederate can access the Slack API, it needs an access token. To get the access token, you need to register PingFederate as an app in Slack.
component: slack
page_id: slack:setup:pf_slack_connector_registering_pf_as_an_app_in_slack
canonical_url: https://docs.pingidentity.com/integrations/slack/setup/pf_slack_connector_registering_pf_as_an_app_in_slack.html
revdate: July 8, 2024
section_ids:
  steps: Steps
---

# Registering PingFederate as an app in Slack

Before PingFederate can access the Slack API, it needs an access token. To get the access token, you need to register PingFederate as an app in Slack.

## Steps

1. Sign on to Slack as an Admin or workspace Owner.

   If you don't already have a Slack workspace, create one. For help, see [Getting started for workspace creators](https://slack.com/intl/en-ca/help/articles/217626298-Getting-started-for-workspace-creators) in the Slack documentation.

2. Go to the Slack [Your Apps](https://api.slack.com/apps) window.

3. Click **Create New App**.

4. On the **Create a Slack App** modal, enter a name and select a workspace. Click **Create App**.

5. On the **Basic Information** window, in the **App Credentials** section, note the **Client ID** and **Client Secret**.

   You will use these in [Getting a Slack API access token](pf_slack_connector_getting_a_slack_api_access_token.html).

6. In the navigation pane, click **OAuth & Permissions**.

7. On the **OAuth & Permissions** window, in the **Redirect URLs** section, add the Ping Identity OAuth Configuration Service (OCS).

   1. Click **Add New Redirect URL**.

   2. In the **Redirect URLs** field, enter the following:

      ```
      https://oauth.pingone.com/ocs/ppm/rest/v1/oauth/oastempcredresponse/
      ```

   3. Click **Add**. Click **Save URLs**.

8. In the **Scopes** section, add the admin scope.

   1. In the **User Token Scopes** section, click **Add an OAuth Scope**.

   2. Select **Admin**.

9. Submit your app to the [Slack App Directory](https://slack.com/apps).

   |   |                                                                                      |
   | - | ------------------------------------------------------------------------------------ |
   |   | This step is required for Slack Enterprise Grid, but optional for other Slack plans. |

   1. In the navigation pane, click **Manage Distribution**.

   2. In the **Remove Hard Coded Information** section, select the **I've reviewed and removed any hard-coded information** check box.

   3. Click **Activate Public Distribution**.