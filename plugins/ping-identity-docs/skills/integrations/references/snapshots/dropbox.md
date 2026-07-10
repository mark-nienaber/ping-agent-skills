---
title: Changelog
description: Added configuration options for CRUD capabilities
component: dropbox
page_id: dropbox:release_notes:pf_dropbox_connector_changelog
canonical_url: https://docs.pingidentity.com/integrations/dropbox/release_notes/pf_dropbox_connector_changelog.html
llms_txt: https://docs.pingidentity.com/integrations/dropbox/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 11, 2024
section_ids:
  dropbox-connector-2-1-april-2017-current-release: Dropbox Connector 2.1 – April 2017 (current release)
  dropbox-connector-2-0-1-april-2016: Dropbox Connector 2.0.1 – April 2016
  dropbox-connector-2-0-september-2015: Dropbox Connector 2.0 – September 2015
  dropbox-connector-1-0-august-2013: Dropbox Connector 1.0 – August 2013
---

# Changelog

## Dropbox Connector 2.1 – April 2017 (current release)

* Added configuration options for CRUD capabilities

## Dropbox Connector 2.0.1 – April 2016

* Added Support for proxy connections

## Dropbox Connector 2.0 – September 2015

* Added Support for additional User attributes

* Added Support for Group Provisioning

* Added Support for adding Users to Groups

## Dropbox Connector 1.0 – August 2013

* Initial Release

* Added Support for User Provisioning

---

---
title: Completing setup of SAML SSO to Dropbox
description: The following section describes the steps for configuring service provider (SP)- and identity provider (IdP)-initiated single sign-on (SSO) to Dropbox.
component: dropbox
page_id: dropbox:setup:pf_dropbox_connector_completing_setup_of_saml_sso_to_dropbox
canonical_url: https://docs.pingidentity.com/integrations/dropbox/setup/pf_dropbox_connector_completing_setup_of_saml_sso_to_dropbox.html
llms_txt: https://docs.pingidentity.com/integrations/dropbox/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 11, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
  result: Result:
---

# Completing setup of SAML SSO to Dropbox

The following section describes the steps for configuring service provider (SP)- and identity provider (IdP)-initiated single sign-on (SSO) to Dropbox.

## About this task

|   |                                                                                                                                                                                                                                                                                                                                                               |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | This section requires two pieces of information from PingFederate:- The PingFederate SSO Application Endpoint, which can be found on the **Activation & Summary** page, in the **SP Connection** section

- The exported certificate used to sign the SAML assertion (configured in [Creating a connection](pf_dropbox_connector_creating_a_connection.html)) |

## Steps

1. Go to <https://www.dropbox.com/team/admin/> and sign on with your team owner credentials.

2. Go to **Authentication** to view the **Single sign-on** section.

3. Select the **Enable single sign-on** checkbox and click **Optional** or **Required** based on your SSO requirements.

4. In the **Sign in URL** field, enter the PingFederate SSO Application endpoint.

   https\://*pf\_host*:*pf\_port*/idp/startSSO.ping?PartnerSpId=*connection\_id*

   where:

   * *pf\_host* is the machine running the PingFederate server.

   * *pf\_port* is the PingFederate port (default value: 9031).

   * *connection\_id* is the connection ID of the SP connection, for example, [https://www.dropbox.com/](https://www.dropbox.com/%29).

5. Import the signing certificate into the X.509 certificate field.

   ![Scren capture of the Authentication section showing Enable single sign-on selected and Required clicked.](_images/vyy1563995261066.png)

6. Click **Save Changes** to complete the Dropbox SSO setup.

   ### Result:

   When saved, emails are sent to team members to instruct them on how to initiate signing on.

---

---
title: Creating a connection
description: To allow PingFederate to act as an identity provider (IdP) and manage users in Dropbox, create a service provider (SP) connection.
component: dropbox
page_id: dropbox:setup:pf_dropbox_connector_creating_a_connection
canonical_url: https://docs.pingidentity.com/integrations/dropbox/setup/pf_dropbox_connector_creating_a_connection.html
llms_txt: https://docs.pingidentity.com/integrations/dropbox/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 11, 2024
section_ids:
  steps: Steps
  choose-from: Choose from:
---

# Creating a connection

To allow PingFederate to act as an identity provider (IdP) and manage users in Dropbox, create a service provider (SP) connection.

## Steps

1. In the PingFederate administrator console, create a new SP connection:

   ### Choose from:

   * For PingFederate 10.1 or later: go to **Applications > Integration > SP Connections**. Click **Create Connection**.

   * For PingFederate 10.0 or earlier: go to **Identity Provider > SP Connections**. Click **Create Connection**.

2. Configure the basic connection details with the Dropbox quick connection template:

   1. On the **Connection Template** tab, click **Use a template for this connection**.

   2. In the **Connection Template** list, select **Dropbox Provisioner**.

   3. On the **Metadata File** row, upload the `saml-metadata.xml` file that you saved in [Preparing the Dropbox SAML 2.0 metadata XML file](pf_dropbox_connector_preparing_the_dropbox_saml_20_metadata_xml_file.html). Click **Next**.

   4. On the **Connection Type** tab select the **Browser SSO Profiles** and **Outbound Provisioning** checkboxes. Click **Next**.

   5. On the **Connection Options** tab, click **Next**.

   6. On the **General Info** tab, the default values are taken from the metadata file you uploaded earlier. Click **Next**.

3. On the **Browser SSO** tab, configure browser single sign-on (SSO).

   Learn more in [Configuring IdP Browser SSO](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_spconnectionconfigtasklet_spbrowserssostate.html) in the PingFederate documentation.

   1. On the **Browser SSO > SAML Profiles** tab, select the **IDP-Initiated SSO** and **SP-Initiated SSO** checkboxes.

   2. On the **Browser SSO > Assertion Creation > Attribute Contract** tab, in the **SAML\_SUBJECT** row, select **urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress** in the **Subject Name Format** list.

   3. On the **Browser SSO > Protocol Settings > Allowable SAML Bindings** tab, select the **Post** and **Redirect** checkboxes. Click **Next**.

4. On the **Browser SSO > Protocol Settings > Signature Policy** tab, select the **Always sign the SAML Assertion** checkbox. Click **Next**.

5. On the **Credentials** tab, configure the connection credentials as shown in [Configuring credentials](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_spconnectionconfigtasklet_credentialsstate.html) in the PingFederate documentation. Click **Next**.

6. On the **Outbound Provisioning** tab, configure provisioning with the following details.

   Learn more in [Configuring outbound provisioning](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_spconnectionconfigtasklet_saasprovisioningstate.html) in the PingFederate documentation.

   1. On the **Target** tab, complete the fields as follows:

      | Field Name               | Description                                                                                                                                                                                                                                                                                                                                                                           |
      | ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      | **OAuth 2 Access Token** | The OAuth 2.0 access token for authentication.To obtain the access token, you must first [Obtain an App Key and Secret from Dropbox](pf_dropbox_connector_obtain_an_app_key_and_secret_from_dropbox.html). When you have obtained the app key and secret from Dropbox, you can [Generate Your OAuth 2.0 Access Token](pf_dropbox_connector_generate_your_oauth_20_access_token.html). |
      | **User Create Enabled**  | * `True` (default): Users will be created in Dropbox through PingFederate.

      * `False`: Users will not be created in Dropbox.&#xA;&#xA;The provisioner.log displays a warning within the create user workflow that the user was not created in Dropbox.                                                                                                                                |
      | **User Update Enabled**  | - `True` (default): Users will be updated in Dropbox through PingFederate.

      - `False`: Users will not be updated in Dropbox.&#xA;&#xA;The provisioner.log will display a warning within the update user workflow that the user was not updated in Dropbox.                                                                                                                            |

   2. (Optional) In the **Provisioning Options** section, customize the provisioning connector behavior. Click **Next**.

   3. On the **Manage Channels > Attribute Mapping** tab, at the bottom of the attribute list, click **Refresh Fields** to get fields and specifications from your Dropbox site.

   4. Complete the attribute mappings by referring to [Supported attributes reference](pf_dropbox_connector_supported_attributes_reference.html).

   Learn more in [Managing channels](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_saasmanagementtasklet_saasmanagementstate.html) in the PingFederate documentation.

7. On the **Activation and Summary** tab, above the **Summary** section, click the toggle to enable the connection. Click **Save**.

---

---
title: Deploying the integration files
description: To get started with the integration, deploy the Dropbox Provisioner files to your PingFederate directory.
component: dropbox
page_id: dropbox:setup:pf_dropbox_connector_deploying_the_integration_files
canonical_url: https://docs.pingidentity.com/integrations/dropbox/setup/pf_dropbox_connector_deploying_the_integration_files.html
llms_txt: https://docs.pingidentity.com/integrations/dropbox/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 11, 2024
section_ids:
  steps: Steps
---

# Deploying the integration files

To get started with the integration, deploy the Dropbox Provisioner files to your PingFederate directory.

## Steps

1. Download the Dropbox Provisioner `.zip` archive from the [**Add-ons** tab of the PingFederate downloads page](https://www.pingidentity.com/en/resources/downloads/pingfederate.html) or the [Ping Identity Marketplace](https://marketplace.pingone.com/item/dropbox-provisioner).

2. Stop PingFederate.

3. If you're upgrading an existing deployment, delete the `pf-dropbox-quickconnection-<version>.jar` file from your `<pf_install>/pingfederate/server/default/deploy` directory.

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
description: The distribution .zip archive for the Dropbox Connector contains the following files:
component: dropbox
page_id: dropbox:release_notes:pf_dropbox_connector_download_manifest
canonical_url: https://docs.pingidentity.com/integrations/dropbox/release_notes/pf_dropbox_connector_download_manifest.html
llms_txt: https://docs.pingidentity.com/integrations/dropbox/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 11, 2024
---

# Download manifest

The distribution `.zip` archive for the Dropbox Connector contains the following files:

* `ReadMeFirst.pdf`: Contains links to this online documentation

* `saml-metadata.xml`: The metadata used for browser single sign-on (SSO)

* `/legal`: Contains the following document:

  * `Legal.pdf`: Copyright and license information

* `/dist`: Contains libraries needed for the connector:

  * `pf-dropbox-quickconnection-2.1.jar`: The PingFederate Dropbox Connector

---

---
title: Dropbox Provisioner
description: The PingFederate provisioner for Dropbox allows an enterprise to provision its users to Dropbox. This Dropbox Provisioner includes a quick connection template to easily setup a single sign-on (SSO) connection requiring Dropbox provisioning.
component: dropbox
page_id: dropbox::pf_dropbox_connector
canonical_url: https://docs.pingidentity.com/integrations/dropbox/pf_dropbox_connector.html
llms_txt: https://docs.pingidentity.com/integrations/dropbox/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 11, 2024
section_ids:
  features: Features
  intended-audience: Intended audience
  system-requirements: System requirements
---

# Dropbox Provisioner

The PingFederate provisioner for Dropbox allows an enterprise to provision its users to Dropbox. This Dropbox Provisioner includes a quick connection template to easily setup a single sign-on (SSO) connection requiring Dropbox provisioning.

This guide provides instructions for quickly configuring PingFederate to connect to Dropbox for secure internet SSO. This configuration also lays the foundation for implementing optional outbound provisioning (formerly software as a service (SaaS) provisioning).

## Features

* Outbound user provisioning

* Outound group provisioning

* Ability to add users to groups

* Browser-based service provider (SP)- and identity provider (IdP)-initiated SSO

## Intended audience

This document is intended for PingFederate administrators.

If you need help during the setup process, learn more in the following sections of the PingFederate documentation:

* [SP connection management](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_sp_connect_management.html)

* [Identity provider SSO configuration](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_ident_provid_sso_config.html)

* [Datastores](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_datastores.html)

* [Configuring outbound provisioning](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_spconnectionconfigtasklet_saasprovisioningstate.html)

* [Configuring outbound provisioning settings](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_protocolsettingstasklet_saasglobalprovisioningsettingsstate.html)

## System requirements

* PingFederate 7.2.1 or later

* You might need to add the following endpoints to the allow list on the firewall to allow outbound connections:

  * https\://api.dropboxapi.com/

---

---
title: Enabling provisioning in PingFederate
description: To use PingFederate for provisioning, configure an external datastore.
component: dropbox
page_id: dropbox:setup:pf_dropbox_connector_enabling_provisioning_in_pf
canonical_url: https://docs.pingidentity.com/integrations/dropbox/setup/pf_dropbox_connector_enabling_provisioning_in_pf.html
llms_txt: https://docs.pingidentity.com/integrations/dropbox/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 11, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
  choose-from: Choose from:
---

# Enabling provisioning in PingFederate

To use PingFederate for provisioning, configure an external datastore.

## About this task

Your external datastore acts as the source of data for provisioning. PingFederate also uses an internal datastore to store the state of synchronization between the source datastore and the target datastore.

Learn more in [Datastores](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_datastores.html) in the PingFederate documentation.

## Steps

1. Configure the datastore for PingFederate to use as the source of user data.

   Learn more in [Datastores](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_datastores.html) in the PingFederate documentation.

   |   |                                                                                                                                                                                                                                                                        |
   | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | When targeting users and groups for provisioning, exclude the user account that you will use to administer users in your connection to Dropbox. This prevents the PingFederate provisioning engine from interfering with the account that provisions users and groups. |

2. Do one of the following:

   ### Choose from:

   * For PingFederate 10.1 or later: Go to **System > Server > Protocol Settings**.

   * For PingFederate 10.0 or earlier: Enable the identity provider (IdP) and outbound provisioning roles:

     1. Go to **System > Protocol Settings > Roles & Protocols**.

     2. Select **Enable Identity Provider IdP Role and Support the Following**.

     3. Select **Outbound Provisioning**. Click **Next**.

3. On the **Outbound Provisioning** tab, select the PingFederate internal datastore. Click **Save**.

   Learn more in [Configuring outbound provisioning settings](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_protocolsettingstasklet_saasglobalprovisioningsettingsstate.html) in the PingFederate documentation.

---

---
title: Generate Your OAuth 2.0 Access Token
description: Go to the Ping Identity OAuth Configuration Service.
component: dropbox
page_id: dropbox:setup:pf_dropbox_connector_generate_your_oauth_20_access_token
canonical_url: https://docs.pingidentity.com/integrations/dropbox/setup/pf_dropbox_connector_generate_your_oauth_20_access_token.html
llms_txt: https://docs.pingidentity.com/integrations/dropbox/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 11, 2024
section_ids:
  steps: Steps
---

# Generate Your OAuth 2.0 Access Token

## Steps

1. Go to the Ping Identity [OAuth Configuration Service](https://oauth.pingone.com/ocs/ppm/rest/v1/oauth/oasrequestform).

2. In the connector menu, select **Dropbox Connector**.

3. In the **ClientID** field, enter the **App Key** you obtained previously.

4. In the **Client Secret** field, enter the **App Secret** you obtained previously and click **Connect**.

   ![Screen capture of the Ping Identity OAuth Configuration Service.](_images/tqv1563995250546.png)

5. Sign on to Dropbox as an administrative user.

   |   |                                                                                                                                                                |
   | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | If you are already signed on to Dropbox, you will not be asked to sign on again. Make sure that the account you are signed on as is an administrative account. |

6. Click **Allow** to generate your Access Token.

   ![Screen capture of the Dropbox pop-up message saying that PingFederate Provision would like to access your team information, as well as the ability to add, edit and delete team members, followed by the Cancel and Allow buttons.](_images/upv1563995251936.png)

7. Copy the **Access Token** to use when configuring the Dropbox Connector.

---

---
title: Known issues and limitations
description: The following are known issues and limitations of the Dropbox Connector.
component: dropbox
page_id: dropbox:release_notes:pf_dropbox_connector_known_issues_and_limitations
canonical_url: https://docs.pingidentity.com/integrations/dropbox/release_notes/pf_dropbox_connector_known_issues_and_limitations.html
llms_txt: https://docs.pingidentity.com/integrations/dropbox/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 11, 2024
---

# Known issues and limitations

The following are known issues and limitations of the Dropbox Connector.

* Single logout (SLO) is not supported.

* User attributes cannot be cleared after they are set.

* Because of API limitations, a user's email cannot be updated until the user has activated their account.

* Because of API limitations, a user cannot suspend or un-suspend until the user has activated their account.

* Because of API limitations, if a user's given name or surname fails to update due to the new value containing unsupported characters (\*|:"<>?), an error might not be reported in the provisioning logs.

* Because of API limitations, a user cannot be added to a group until the user has activated their account.

* The `externalId` attribute is not supported for group provisioning

---

---
title: Obtain an App Key and Secret from Dropbox
description: The Dropbox Connectors Outbound Provisioning functionality is built using Dropbox's REST API, which requires an OAuth 2.0 access token for authentication. To obtain the access token, you must obtain an app key and secret from Dropbox.
component: dropbox
page_id: dropbox:setup:pf_dropbox_connector_obtain_an_app_key_and_secret_from_dropbox
canonical_url: https://docs.pingidentity.com/integrations/dropbox/setup/pf_dropbox_connector_obtain_an_app_key_and_secret_from_dropbox.html
llms_txt: https://docs.pingidentity.com/integrations/dropbox/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 11, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Obtain an App Key and Secret from Dropbox

## About this task

The Dropbox Connectors Outbound Provisioning functionality is built using Dropbox's REST API, which requires an OAuth 2.0 access token for authentication. To obtain the access token, you must obtain an app key and secret from Dropbox.

## Steps

1. Sign on to Dropbox as an administrative user.

2. Go to **My Apps for Dropbox**.

3. Click the **Create app** button.

4. Click **Dropbox Business API** as the API to use.

5. Click **Team member management** as the type of access you need.

6. Give your application a name, such as `PingFederate Provisioning`.

7. Click **Create app**.

8. Copy the **App Key** and **App secret** values to use in the next section.

9. Add the following URL to the **Redirect URIs**.

   https\://oauth.pingone.com/ocs/ppm/rest/v1/oauth/oastempcredresponse/

10. (Optional) Click the **Apply for production** button to open your app to more users.

    |   |                                                                            |
    | - | -------------------------------------------------------------------------- |
    |   | Development status only allows your app to be accessed by up to 100 users. |

---

---
title: Obtaining your OAuth access token
description: For this procedure you will need to perform two steps:
component: dropbox
page_id: dropbox:setup:pf_dropbox_connector_obtaining_your_oauth_access_token
canonical_url: https://docs.pingidentity.com/integrations/dropbox/setup/pf_dropbox_connector_obtaining_your_oauth_access_token.html
llms_txt: https://docs.pingidentity.com/integrations/dropbox/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 11, 2024
---

# Obtaining your OAuth access token

For this procedure you will need to perform two steps:

1. [Obtain an App Key and Secret from Dropbox](pf_dropbox_connector_obtain_an_app_key_and_secret_from_dropbox.html).

2. [Generate Your OAuth 2.0 Access Token](pf_dropbox_connector_generate_your_oauth_20_access_token.html).

---

---
title: Preparing the Dropbox SAML 2.0 metadata XML file
description: This Connector's quick-connection template uses a metadata XML file to assist in configuring many settings in the service provider (SP) connection.
component: dropbox
page_id: dropbox:setup:pf_dropbox_connector_preparing_the_dropbox_saml_20_metadata_xml_file
canonical_url: https://docs.pingidentity.com/integrations/dropbox/setup/pf_dropbox_connector_preparing_the_dropbox_saml_20_metadata_xml_file.html
llms_txt: https://docs.pingidentity.com/integrations/dropbox/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 27, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Preparing the Dropbox SAML 2.0 metadata XML file

This Connector's quick-connection template uses a metadata XML file to assist in configuring many settings in the service provider (SP) connection.

## About this task

When asked during the connection configuration steps, import the `saml-metadata.xml` packaged with this connector.

## Steps

1. Open the `saml-metadata.xml` file contained with your connector with a text editor of your choice.

2. No changes are required, unless you have an SP connection already created with the same entity ID.

3. When you have updated the `saml-metadata.xml` file, save your changes.

---

---
title: Supported attributes reference
description: Given Name
component: dropbox
page_id: dropbox:setup:pf_dropbox_connector_supported_attributes_reference
canonical_url: https://docs.pingidentity.com/integrations/dropbox/setup/pf_dropbox_connector_supported_attributes_reference.html
llms_txt: https://docs.pingidentity.com/integrations/dropbox/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 11, 2024
---

# Supported attributes reference

| Attribute             | Description                                                                                                                                                                                         |
| --------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `Given Name`          | The user's first name.                                                                                                                                                                              |
| `Surname`             | The user's last name.                                                                                                                                                                               |
| `Email`               | The user's email address.                                                                                                                                                                           |
| `Role`                | The user's role in Dropbox. Valid options are:- `member_only`

- `support_admin`

- `team_admin`

- `user_management_admin`                                                                         |
| `Send Welcome Email`  | Whether to send a newly created user a welcome email. Valid options are `true` or `false`.&#xA;&#xA;If set to false, no email invitation is sent to the user.                                       |
| `Wipe Data on Delete` | Whether to delete data on user devices when they are suspended (deleted or disabled). Valid options are `true` or `false`. If not specified, Dropbox assumes it should delete data on user devices. |
| `External ID`         | A unique external identifier for the user.                                                                                                                                                          |

---

---
title: Upgrading existing Dropbox connectors
description: Before stopping the PingFederate server to upgrade the Dropbox Connector, on the Attribute Mapping tab for existing channel configurations, record the current configuration.
component: dropbox
page_id: dropbox:setup:pf_dropbox_connector_upgrading_existing_dropbox_connectors
canonical_url: https://docs.pingidentity.com/integrations/dropbox/setup/pf_dropbox_connector_upgrading_existing_dropbox_connectors.html
llms_txt: https://docs.pingidentity.com/integrations/dropbox/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 11, 2024
section_ids:
  steps: Steps
---

# Upgrading existing Dropbox connectors

## Steps

1. Before stopping the PingFederate server to upgrade the Dropbox Connector, on the **Attribute Mapping** tab for existing channel configurations, record the current configuration.

   |   |                                                                                                                                                                          |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
   |   | The upgrade process removes existing mappings and defaults on the **Attribute Mapping** tab. You must configure these again before activating the channel configuration. |

2. Disable the existing service provider (SP) connection where the Dropbox Connector is configured.

3. Delete the existing Dropbox Connector SP connection and save.

4. Stop the PingFederate server if it is running.

5. Extract the Dropbox Connector distribution `.zip` archive into a holding directory.

6. Remove any versions of `pf-dropbox-quickconnection-.x.jar` from the `<pf_install>/pingfederate/server/default/deploy` directory.

7. Remove the following files from the same directory if they are present:

   * `pf-dropbox-oauth-helper.war`

   * `gson-2.2.4.jar`

8. From the `/dist` directory of the new version of the connector, copy the `pf-dropbox-quickconnection-2.0.jar` to the `<pf_install>/pingfederate/server/default/deploy` directory.

   |   |                                                                   |
   | - | ----------------------------------------------------------------- |
   |   | Make sure to remove existing versions of Dropbox Connector files. |

9. Start the PingFederate server.

10. Create a new SP connection using Dropbox as the connection template.

11. Follow the instructions in the [Creating a connection](pf_dropbox_connector_creating_a_connection.html) section to configure Metadata and OAuth.

12. Access the Attribute Mapping for existing channel configurations and click **Refresh Fields**.

13. Ensure all new required fields, if any, are mapped appropriately or have a default value.

14. When you have finished the attribute configuration, click **Done**, **Done**, and **Save**.

15. Click the toggle to activate the SP Connection to resume outbound provisioning.

---

---
title: User and group management
description: The Dropbox Provisioner synchronizes users and groups from your datastore to Dropbox. The following sections describe the behavior of each provisioning capability.
component: dropbox
page_id: dropbox::pf_dropbox_connector_user_and_group_management
canonical_url: https://docs.pingidentity.com/integrations/dropbox/pf_dropbox_connector_user_and_group_management.html
llms_txt: https://docs.pingidentity.com/integrations/dropbox/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 11, 2024
section_ids:
  synchronizing-existing-users: Synchronizing existing users
  user-provisioning: User provisioning
  user-updates: User updates
  synchronizing-existing-groups: Synchronizing existing groups
  group-provisioning: Group provisioning
  group-name-updates: Group name updates
  group-membership-updates: Group membership updates
  group-deletion: Group deletion
---

# User and group management

The Dropbox Provisioner synchronizes users and groups from your datastore to Dropbox. The following sections describe the behavior of each provisioning capability.

## Synchronizing existing users

PingFederate synchronizes users based on the `Email` attribute in Dropbox. If a user already exists in your datastore and Dropbox, mapping this attribute correctly links the two records together.

For example:

* In Dropbox, Janet's `Email` is `jsmith@domain.com`.

* In your datastore, Janet's `mail` is `jsmith@domain.com`.

* On the **Attribute Mapping** tab of your provisioning connection configuration, map the `Email` attribute to `mail`.

* When the provisioning connector runs, the datastore user is provisioned with a `Email` of `jsmith@domain.com`. That matches Janet's existing `Email` in Dropbox, so her information in the datastore is synchronized to her Dropbox account.

## User provisioning

PingFederate provisions users when any of the following happens:

* A user is added to the datastore group or filter that is targeted by the provisioning connector.

* A user with "disabled" status is added to the datastore group or filter that is targeted by the provisioning connector, and the **Provision disabled users** provisioning option is enabled.

## User updates

PingFederate updates users when a user attribute changes in your datastore.

The **Attribute Mapping** tab of your provisioning connection configuration defines which attributes PingFederate monitors for changes.

## Synchronizing existing groups

PingFederate synchronizes groups from the datastore to the target service based on the group name.

For example:

* In Dropbox, there is a group is named `Accounting`.

* In your datastore, there is a group with a `CN` of `Accounting`.

* When the provisioning connector runs, the two groups are synchronized.

## Group provisioning

PingFederate provisions groups when a group is added to the datastore filter that is targeted by the provisioning connector.

## Group name updates

PingFederate renames groups when they are renamed in the datastore.

## Group membership updates

PingFederate updates group memberships when memberships change in the datastore, whether the change is in the group's properties or a user's properties.

Group memberships in the datastore overwrite the group memberships in Dropbox.

## Group deletion

PingFederate deletes groups when any of the following happen:

* The group is deleted in the datastore.

* The group is removed from the datastore group or filter that is targeted by the provisioning connector.

Group deletions are permanent and cannot be undone.