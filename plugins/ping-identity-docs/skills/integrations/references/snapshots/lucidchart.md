---
title: Changelog
description: Lucidchart Connector 1.0 – June 2018 (current release)
component: lucidchart
page_id: lucidchart:release_notes:pf_lucidchart_connector_changelog
canonical_url: https://docs.pingidentity.com/integrations/lucidchart/release_notes/pf_lucidchart_connector_changelog.html
llms_txt: https://docs.pingidentity.com/integrations/lucidchart/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 21, 2024
---

# Changelog

**Lucidchart Connector 1.0 – June 2018 (current release)**

* Initial release

* Added support for user life cycle management (including creates, updates, disables and deletes)

* Added configuration options for workflow capabilities (for example, the ability to disable updates)

---

---
title: Configure Lucidchart for SSO
description: To configure Lucidchart for SSO you will require metadata from your PingFederate Identity Provider (IdP) setup. For more information, see Exporting selected SAML metadata in the PingFederate documentation.
component: lucidchart
page_id: lucidchart:setup:pf_lucidchart_connector_configure_lucidchart_for_sso
canonical_url: https://docs.pingidentity.com/integrations/lucidchart/setup/pf_lucidchart_connector_configure_lucidchart_for_sso.html
llms_txt: https://docs.pingidentity.com/integrations/lucidchart/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 21, 2024
section_ids:
  before-you-begin: Before you begin
  steps: Steps
---

# Configure Lucidchart for SSO

## Before you begin

To configure Lucidchart for SSO you will require metadata from your PingFederate Identity Provider (IdP) setup. For more information, see [Exporting selected SAML metadata](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_exporting_selected_saml_metadata.html) in the PingFederate documentation.

To export your IdP metadata:

1. Go to **Server Configuration > Metadata Export**.

2. On the Metadata Mode screen, choose Select information to include in metadata manually and click Next.

3. On the Protocol screen, click Next.

4. On the Attribute Contract screen, click Next.

5. On the Signing Key screen, select the PingFederate signing certificate for use and click Next.

6. Follow the rest of the workflow to export a metadata XML file, including selecting the certificate to sign the metadata XML file in the Metadata Signing screen (as needed).

To configure Lucidchart for SSO:

|   |                                                                                                                                                                                                             |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | For more information on how to set up SSO for Lucidchart, see [SAML and SCIM: An Overview](https://lucidchart.zendesk.com/hc/en-us/articles/207300096-Lucidchart-and-SAML) in the LucidChart documentation. |

## Steps

1. Log into your Lucidchart account as an administrative user for your organization.

2. Go to Team > App Integration > SAML.

3. Select the checkbox for Enable SAML Integration.

4. Enter your Lucidchart account domain in the Domain field under the section Lucidchart Sign in URL.

   |   |                                                                                                                                                                                                                                                                                                                                                 |
   | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | Enter the domain only, not a full URL. The SAML integration will use your domain to generate a Lucidchart sign-in URL that will be provided to PingFederate. For example, if you enter acme.com as your domain, the URL will be <https://www.lucidchart/saml/sso/acme.com>. A user may go directly to this URL to initiate SAML single sign on. |

5. Under the Identity Providers section, select Add Identity Provider.

6. Open your IdP metadata `.xml`file using a text editor. Copy the text from the `.xml` file and paste it into the text box under Identity Provider Metadata.

7. Provide a description for Identity Provider Name, select the product Lucidchart and click Add Provider.

   ![Image of the Add Identity Provider screen.](_images/ycf1563995475735.png)

8. Under Download Service Provider Metadata, select Download Metadata and Save changes.

   ![Image of the Download Service Provider Metadata screen.](_images/fqd1563995476284.png)

---

---
title: Configure PingFederate for SSO
description: The following section describes the steps for configuring single sign-on (SSO) to Lucidchart. Configuring SAML SSO involves both configuring PingFederate SP connection and the Lucidchart SSO screens.
component: lucidchart
page_id: lucidchart:setup:pf_lucidchart_connector_configure_pf_for_sso
canonical_url: https://docs.pingidentity.com/integrations/lucidchart/setup/pf_lucidchart_connector_configure_pf_for_sso.html
llms_txt: https://docs.pingidentity.com/integrations/lucidchart/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 21, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Configure PingFederate for SSO

## About this task

The following section describes the steps for configuring single sign-on (SSO) to Lucidchart. Configuring SAML SSO involves both configuring PingFederate SP connection and the Lucidchart SSO screens.

|   |                                                        |
| - | ------------------------------------------------------ |
|   | Configuring SSO is optional for outbound provisioning. |

To configure PingFederate for SSO:

## Steps

1. Create a new SP connection or select an existing SP connection from the SP Configuration menu.

2. On the Connection Template screen, select the Use a template for this connection option and choose Lucidchart Connector from the Connection Template drop-down list. You will be asked to provide the `metadata.xml` file you obtained earlier in [Configure Lucidchart for SSO](pf_lucidchart_connector_configure_lucidchart_for_sso.html).

   ![Image of the Connection Template screen.](_images/acx1563995472841.png)

   |   |                                                                                                 |
   | - | ----------------------------------------------------------------------------------------------- |
   |   | If this selection is not available, verify the connector installation and restart PingFederate. |

3. On the Connection Type screen, ensure that the Browser SSO Profiles checkbox is selected.

4. On the General Info screen, the default values are taken from the metadata file you selected in an earlier step. We recommend using the metadata default values.

   ![Image of the General Info screen.](_images/gft1563995477063.png)

5. Click Next to continue the Browser SSO configuration. For more information, see the following sections under [Identity provider SSO configuration](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_ident_provid_sso_config.html):

   * [Managing IdP adapters](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_managing_idp_adapters.html)

   * [Configure IdP Browser SSO](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_spconnectionconfigtasklet_spbrowserssostate.html)

   * [Configuring credentials](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_spconnectionconfigtasklet_credentialsstate.html)

6. On the **Browser SSO > SAML Profiles** screen, ensure that the IdP-initiated SSO and SP-initiated SSO profiles are selected and click Next.

   ![An image of the SAML Profiles screen.](_images/ykh1563995477812.png)

7. On the **Browser SSO > Protocol Settings > Allowable SAML Bindings** screen, ensure that the POST and Redirect profiles are selected (clear Artifact and SOAP). Click Next.

   ![An image of the Allowable SAML Bindings screen.](_images/cxl1563995478475.png)

8. On the **Credentials > Digital Signature Settings** screen, select the signing certificate.

9. On the Activation & Summary screen, set Connection Status to ACTIVE, then click Save.

---

---
title: Configure provisioning
description: To configure a connection for outbound provisioning to Lucidchart, follow the instructions in this section.
component: lucidchart
page_id: lucidchart:setup:pf_lucidchart_connector_configure_provisioning
canonical_url: https://docs.pingidentity.com/integrations/lucidchart/setup/pf_lucidchart_connector_configure_provisioning.html
llms_txt: https://docs.pingidentity.com/integrations/lucidchart/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 21, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Configure provisioning

## About this task

To configure a connection for outbound provisioning to Lucidchart, follow the instructions in this section.

Outbound provisioning details are managed within an SP connection. You can configure outbound provisioning with or without Browser SSO, WS-Trust STS, or both when you create a new SP connection. You can also add outbound provisioning to an existing SP connection.

## Steps

1. In the PingFederate administrator console, configure the data store that PingFederate will use as the source of user data. For instructions, see [Datastores](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_managedatasourcestasklet_managedatasourcesstate.html) in the PingFederate documentation.

   * When targeting users and groups for provisioning, exclude the user account that you will use to administer users in your connection to Lucidchart. This prevents the PingFederate provisioning engine from interfering with the account that provisions users and groups.

2. Create a new SP connection or select an existing SP connection from the SP Configuration menu.

3. On the Connection Template screen, select Use a template for this connection and choose Lucidchart Connector from the Connection Template drop-down list. When asked during the connection configuration steps, import the `lucidchart-saml-metadata.xml` packaged with this connector.

   ![Image of the Connect Template screen.](_images/acx1563995472841.png)

   |   |                                                                                                 |
   | - | ----------------------------------------------------------------------------------------------- |
   |   | If this selection is not available, verify the connector installation and restart PingFederate. |

4. On the Connection Type screen, ensure the Outbound Provisioning checkbox is selected, and the Browser SSO Profiles checkbox is cleared (if appropriate).

5. On the General Info screen, the default values are taken from the metadata file you selected in step 2. We recommend using the metadata default values.

   ![Image of the General Info screen.](_images/nzp1563995473563.png)

6. Follow the connection wizard to configure the connection.

7. On the Outbound Provisioning screen, click Configure Provisioning.

8. On the Target screen, enter the values for each field as required by the Lucidchart Connector.

   ![Image of the Target screen.](_images/oop1563995474636.png)

   **Table 1. Target screen options**

   | Field Name               | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
   | ------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | Base URL                 | The base URL for Lucidchart.For more information on obtaining the base URL, see [Obtain base URL and bearer token](pf_lucidchart_connector_obtain_base_url_and_bearer_token.html).                                                                                                                                                                                                                                                                                                                          |
   | Bearer Token             | The bearer token used by the connector to make authenticated API calls to Lucidchart. For more information on obtaining the bearer token, see [Obtain base URL and bearer token](pf_lucidchart_connector_obtain_base_url_and_bearer_token.html).                                                                                                                                                                                                                                                            |
   | **Provisioning Options** |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
   | User Create              | **True** (default) – Users will be created in Lucidchart.**False** – Users will not be created in Lucidchart.&#xA;&#xA;The provisioner.log will display a warning within the create user workflow that the user was not created in Lucidchart.                                                                                                                                                                                                                                                              |
   | User Update              | **True** (default) – Users will be updated in Lucidchart.**False** – Users will not be updated in Lucidchart.&#xA;&#xA;The provisioner.log will display a warning within the update user workflow that the user was not updated in Lucidchart.                                                                                                                                                                                                                                                              |
   | User Disable / Delete    | **True** (default) – Users will be disabled or deleted in Lucidchart.&#xA;&#xA;A disabled user can only be re-enabled if User Update is true.**False** – Users will not be disabled or deleted in Lucidchart.&#xA;&#xA;The provisioner.log will display a warning within the user workflow that the user was not disabled or deleted in Lucidchart.                                                                                                                                                         |
   | Provision Disabled Users | This option is only relevant if you select User Create.**True** (default) – If a disabled user in the user store is targeted for provisioning, it will be created in a disabled state in Lucidchart.**False** – If a disabled user in the user store is targeted for provisioning, it will be not be created in Lucidchart.&#xA;&#xA;The provisioner.log will display a warning within the create user workflow indicating that the user was not created in Lucidchart.                                     |
   | Remove User Action       | Select a deprovision method (Disable or Delete). Deprovisioning is triggered when previously provisioned users no longer meet the condition set in the Source Location screen, or when a user has been suspended or deleted from the data store. This option is only applicable if User Disable / Delete is set to True.**Disable** (default) – Deactivates the user account in Lucidchart (also known as a soft delete).**Delete** – Removes the user account in Lucidchart (also known as a hard delete). |

9. Click Next to continue the provisioning configuration. For more information, see the following sections under [Outbound provisioning for IdPs](https://docs.pingidentity.com/pingfederate/latest/introduction_to_pingfederate/pf_outboun_provis_for_idp.html) in the PingFederate documentation:

   * [Managing channels](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_saasmanagementtasklet_saasmanagementstate.html)

   * [Specifying channel information](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_saaschanneltasklet_saasgeneralinfostate.html)

   * [Identifying the source datastore](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_saaschanneltasklet_saassourceselectionstate.html)

   * [Modifying source settings](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_saaschanneltasklet_saassourcesettingsstate.html)

   * [Specifying a source location](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_saaschanneltasklet_saassourcelocationstate.html)

   * [Mapping attributes](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_saaschanneltasklet_saasattrmappingmgmtstate.html)

   * [Reviewing channel settings](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_saaschanneltasklet_saasactivationstate.html)

     |   |                                                                                                                 |
     | - | --------------------------------------------------------------------------------------------------------------- |
     |   | Credentials will be verified when the channel and SP connection is set to Active and provisioning is initiated. |

     |   |                                                                                                                                                                                                                                                      |
     | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
     |   | If you are not ready to complete the provisioning configuration, you can click Save and return to the configuration page later. To return to the configuration page, select the connection from **Identity Provider > SP Connections > Manage All**. |

---

---
title: Configure SAML SSO
description: The following section describes the steps for configuring single sign-on (SSO) to Lucidchart.
component: lucidchart
page_id: lucidchart:setup:pf_lucidchart_connector_configure_saml_sso
canonical_url: https://docs.pingidentity.com/integrations/lucidchart/setup/pf_lucidchart_connector_configure_saml_sso.html
llms_txt: https://docs.pingidentity.com/integrations/lucidchart/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 21, 2024
---

# Configure SAML SSO

The following section describes the steps for configuring single sign-on (SSO) to Lucidchart.

|   |                                                        |
| - | ------------------------------------------------------ |
|   | Configuring SSO is optional for outbound provisioning. |

* [Configure Lucidchart for SSO](pf_lucidchart_connector_configure_lucidchart_for_sso.html)

* [Configure PingFederate for SSO](pf_lucidchart_connector_configure_pf_for_sso.html)

---

---
title: Download manifest
description: The distribution .zip archive for the connector contains the following:
component: lucidchart
page_id: lucidchart:release_notes:pf_lucidchart_connector_download_manifest
canonical_url: https://docs.pingidentity.com/integrations/lucidchart/release_notes/pf_lucidchart_connector_download_manifest.html
llms_txt: https://docs.pingidentity.com/integrations/lucidchart/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 21, 2024
---

# Download manifest

The distribution `.zip` archive for the connector contains the following:

* `ReadMeFirst.pdf `– contains links to this online documentation.

* `lucidchart-saml-metadata.xml` – SAML metadata file for use with a Lucidchart connection. For more information, see [Configure provisioning](../setup/pf_lucidchart_connector_configure_provisioning.html).

* `/legal`:

  * `Legal.pdf` – copyright and license information.

* `/dist` – contains libraries needed for the connector:

  * `pf-lucidchart-quickconnection-[version].jar `– PingFederate Lucidchart Connector

---

---
title: Enable outbound provisioning
description: After enabling outbound provisioning in the <pf_install>/pingfederate/bin/run.properties file, you must also activate the outbound provisioning role in the administrative console.
component: lucidchart
page_id: lucidchart:setup:pf_lucidchart_connector_enable_outbound_provisioning
canonical_url: https://docs.pingidentity.com/integrations/lucidchart/setup/pf_lucidchart_connector_enable_outbound_provisioning.html
llms_txt: https://docs.pingidentity.com/integrations/lucidchart/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 21, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Enable outbound provisioning

## About this task

After enabling outbound provisioning in the `<pf_install>/pingfederate/bin/run.properties` file, you must also activate the outbound provisioning role in the administrative console.

## Steps

1. Go to the Server Configuration > Server Settings > Roles & Protocol screen.

2. Select the Outbound Provisioning check box.

   ![Image of the Roles & Protocol screen.](_images/jwv1563995471374.png)

   |   |                                                                                                                                                                                                                                                                                                                                                                           |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | Enabling outbound provisioning adds the outbound provisioning screen and requires the selection of a database to facilitate provisioning. For more information, see [Configuring outbound provisioning settings](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_protocolsettingstasklet_saasglobalprovisioningsettingsstate.html). |

---

---
title: Install the connector
description: This section describes the common steps required to install the PingFederate Lucidchart Connector.
component: lucidchart
page_id: lucidchart:setup:pf_lucidchart_connector_install_the_connector
canonical_url: https://docs.pingidentity.com/integrations/lucidchart/setup/pf_lucidchart_connector_install_the_connector.html
llms_txt: https://docs.pingidentity.com/integrations/lucidchart/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 21, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Install the connector

## About this task

This section describes the common steps required to install the PingFederate Lucidchart Connector.

## Steps

1. Download the Lucidchart Provisioner `.zip` archive from the [**Add-ons** tab of the PingFederate downloads page](https://www.pingidentity.com/en/resources/downloads/pingfederate.html) or the [Ping Identity Marketplace](https://marketplace.pingone.com/item/lucidchart-single-signon-integration).

2. Stop the PingFederate server if it is running.

3. Unzip the Lucidchart Connector distribution `.zip`file.

4. Copy the contents of the `dist` directory into the directory:

   `<pf_install>/pingfederate/server/default/deploy`

5. **Optional:** If you plan to use the connector for outbound provisioning, edit the `run.properties` file located in `<pf_install>/pingfederate/bin`, changing the property `pf.provisioner.mode` to `STANDALONE`. For example:

   `pf.provisioner.mode=STANDALONE`

   |   |                                                                                                                                                                                                                           |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | For information about using the FAILOVER setting for runtime deployment, see [Deploying provisioning failover](https://docs.pingidentity.com/pingfederate/latest/server_clustering_guide/pf_deploy_provis_failover.html). |

6. Start the PingFederate server.

---

---
title: Known issues and limitations
description: Due to a limitation with PingFederate 8.1 and earlier versions, when configuring two SP connections with the same provisioner, the second connection built may be pre-populated with the channel from the first connection. To avoid conflicts, delete this pre-populated channel and create a unique channel for each connection.
component: lucidchart
page_id: lucidchart:release_notes:pf_lucidchart_connector_known_issues_and_limitations
canonical_url: https://docs.pingidentity.com/integrations/lucidchart/release_notes/pf_lucidchart_connector_known_issues_and_limitations.html
llms_txt: https://docs.pingidentity.com/integrations/lucidchart/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 21, 2024
---

# Known issues and limitations

* Due to a limitation with PingFederate 8.1 and earlier versions, when configuring two SP connections with the same provisioner, the second connection built may be pre-populated with the channel from the first connection. To avoid conflicts, delete this pre-populated channel and create a unique channel for each connection.

* When an LDAP user is deleted in a targeted group distinguished name (DN), the provisioning connector does not propagate the deletion until a new user is added to the group. This limitation is compounded when the **User Create** provisioning option is disabled. For solutions, see [SaaS provisioner does not remove the user](https://support.pingidentity.com/s/article/After-deleting-an-AD-user-account-SaaS-provisioner-does-not-remove-the-user-in-the-next-provisioning-cycle-when-Group-DN-is-specified) in the Knowledge Base.

* Due to PingFederate limitations, user attributes cannot be cleared once set.

**Performance limitations**

* Due to Lucidchart API limitations, there will be a performance impact to creating users when mapping External ID or Roles. Both External ID and Roles may fail to be added to a user on the initial create. Should this happen, an exception will be thrown and an update to the user will be attempted on the next provisioning cycle.

* Due to Lucidchart API limitations, attempting to update a user immediately after creating them may result in user not found exceptions. This is due to a delay in Lucidchart between creating a user and being able to modify the user. Failed attempts to update the user will be reattempted on the next provisioning cycle.

---

---
title: Lucidchart Provisioner
description: The PingFederate Lucidchart Provisioner enables an enterprise to provision users to Lucidchart.
component: lucidchart
page_id: lucidchart::pf_lucidchart_connector
canonical_url: https://docs.pingidentity.com/integrations/lucidchart/pf_lucidchart_connector.html
llms_txt: https://docs.pingidentity.com/integrations/lucidchart/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 21, 2024
section_ids:
  features: Features
  intended-audience: Intended audience
  system-requirements: System Requirements
---

# Lucidchart Provisioner

The PingFederate Lucidchart Provisioner enables an enterprise to provision users to Lucidchart.

A quick connection template is also included to simplify the configuration of single sign-on (SSO). Additional details on Lucidchart can be found on the [Lucidchart website](https://www.lucidchart.com/).

## Features

* Browser-based SP and IdP-initiated SSO

* Includes support for user life cycle management (including creates, updates, disables and deletes)

* Includes configuration options for workflow capabilities (for example, the ability to disable updates)

## Intended audience

This document is intended for PingFederate administrators.

If you need help during the setup process, see the following sections of the PingFederate documentation:

* [SP connection management](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_sp_connect_management.html)

* [Identity provider SSO configuration](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_ident_provid_sso_config.html)

* [Datastores](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_datastores.html)

* [Configuring outbound provisioning](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_spconnectionconfigtasklet_saasprovisioningstate.html)

* [Configuring outbound provisioning settings](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_protocolsettingstasklet_saasglobalprovisioningsettingsstate.html)

## System Requirements

* PingFederate 7.3 or later with Java 8

* Might require the following endpoints to be whitelisted on the firewall to allow outbound connections:

  * <https://www.lucidchart.com/scim/v2/chart>

* An Enterprise account is required for SCIM and SAML single sign-on with Lucidchart. To upgrade to Enterprise, visit Lucidchart's [pricing page](https://www.lucidchart.com/users/registerLevel?km_HelpCenterRevTracking=lcsaml;utm_source=Chart_HC\&t4=A\&tP=1&<em>hstc=215508872.bd4c9a6fae6cc53c0d8f58c7c049d99e.1467402096587.1468264075091.1468267227250.14\&utm_campaign=Pricing_Page\&t10=A\&utm_medium=5_Active&</em>hsfp=4208821684&__hssc=215508872.22.1468267227250) or [contact sales](https://lucidchart.zendesk.com/hc/en-us/requests/new?ticket_form_id=2130).

---

---
title: Obtain base URL and bearer token
description: Below are the tasks to enable SCIM provisioning on the Lucidchart Admin Portal.
component: lucidchart
page_id: lucidchart:setup:pf_lucidchart_connector_obtain_base_url_and_bearer_token
canonical_url: https://docs.pingidentity.com/integrations/lucidchart/setup/pf_lucidchart_connector_obtain_base_url_and_bearer_token.html
llms_txt: https://docs.pingidentity.com/integrations/lucidchart/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 21, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Obtain base URL and bearer token

## About this task

Below are the tasks to enable SCIM provisioning on the Lucidchart Admin Portal.

## Steps

1. Log into your Lucidchart account as an administrative user for your organization.

2. Go to Team > App Integration.

3. Under App Integration select SCIM.

4. Click Generate Token.

5. On the SCIM screen, note the displayed values for later use.

   * Base URL: This is the base URL for Lucidchart.

   * Bearer Token: This token is used by the connector to make authenticated API calls to Lucidchart.

---

---
title: Supported attributes reference
description: The following table consists of the attributes that can be mapped for user provisioning.
component: lucidchart
page_id: lucidchart:setup:pf_lucidchart_connector_supported_attributes_reference
canonical_url: https://docs.pingidentity.com/integrations/lucidchart/setup/pf_lucidchart_connector_supported_attributes_reference.html
llms_txt: https://docs.pingidentity.com/integrations/lucidchart/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 21, 2024
---

# Supported attributes reference

The following table consists of the attributes that can be mapped for user provisioning.

| Attribute   | Description                                                                                                                                                                                                                                                                        |
| ----------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Username    | Lucidchart's unique identifier for the user. A username cannot be updated. This attribute is required.                                                                                                                                                                             |
| Email       | The email for the user (for example, "bjensen\@example.com"). This attribute is required.                                                                                                                                                                                          |
| First Name  | The given name of the user, or first name in most Western languages (for example, 'Barbara' given the full name 'Ms. Barbara Jane Jensen, III'). This attribute is required.                                                                                                       |
| Last Name   | The family name of the user, or last name in most Western languages (for example, 'Jensen' given the full name 'Ms. Barbara Jane Jensen, III'). This attribute is required.                                                                                                        |
| External ID | A string that is an identifier for the resource as defined by the provisioning client. For relevant Lucidchart API limitations, see [Known issues and limitations](../release_notes/pf_lucidchart_connector_known_issues_and_limitations.html).                                    |
| Roles       | The user's role or roles. The role used here must already exist in Lucidchart; the application does not create new roles. For relevant Lucidchart API limitations, see [Known issues and limitations](../release_notes/pf_lucidchart_connector_known_issues_and_limitations.html). |

---

---
title: User management
description: The Lucidchart Provisioner synchronizes users from your datastore to Lucidchart. The following describes the behavior of each provisioning capability.
component: lucidchart
page_id: lucidchart::pf_lucidchart_connector_user_management
canonical_url: https://docs.pingidentity.com/integrations/lucidchart/pf_lucidchart_connector_user_management.html
llms_txt: https://docs.pingidentity.com/integrations/lucidchart/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 21, 2024
section_ids:
  synchronizing-existing-users: Synchronizing existing users
  user-provisioning: User provisioning
  user-updates: User updates
  user-deprovisioning: User deprovisioning
---

# User management

The Lucidchart Provisioner synchronizes users from your datastore to Lucidchart. The following describes the behavior of each provisioning capability.

|   |                                                                                                                                                                                                                      |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | You can configure the following capabilities and specify which users to provision when you get to the [Configure provisioning](setup/pf_lucidchart_connector_configure_provisioning.html) part of the setup process. |

## Synchronizing existing users

PingFederate synchronizes users based on the `Username` attribute in Lucidchart. If a user already exists in your datastore and Lucidchart, mapping this attribute correctly links the two records together.

For example:

* In Lucidchart, Janet's `Username` is `bjensen`.

* In your datastore, Janet's `sAMAccountName` is `bjensen`.

* On the **Attribute Mapping** tab of your provisioning connection configuration, map the `Username` attribute to `sAMAccountName`.

* When the provisioning connector runs, the datastore user is provisioned with a `Username` of `bjensen`. That matches Janet's existing `Username` in Lucidchart, so her information in the datastore is synchronized to her Lucidchart account.

## User provisioning

PingFederate provisions users when any of the following happens:

* A user is added to the datastore group or filter that is targeted by the provisioning connector.

* A user with `disabled` status is added to the datastore group or filter that is targeted by the provisioning connector, and the Provision disabled users provisioning option is enabled. This feature is not available in all provisioning connectors.

|   |                                                                                                                                                |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------- |
|   | You can define which users PingFederate targets for provisioning on the **Source Location** tab of your provisioning connection configuration. |

## User updates

PingFederate updates users when a user attribute changes in your datastore.

|   |                                                                                                                                                   |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | You can define which attributes PingFederate monitors for changes on the **Attribute Mapping** tab of your provisioning connection configuration. |

## User deprovisioning

PingFederate deprovisions users when any of the following happens:

* A user is deleted from the user store.

* A user is disabled in the user store.

* A user is removed from the datastore group or filter that is targeted by the provisioning connector.