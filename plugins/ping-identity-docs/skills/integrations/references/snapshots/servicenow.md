---
title: Adding the Ping Identity provisioning role in ServiceNow
description: To allow PingFederate to manage users in ServiceNow, add the special Ping Identity provisioning role in your ServiceNow instance.
component: servicenow
page_id: servicenow:setup:pf_servicenow_connector_adding_the_ping_identity_provisioning_role_in_servicenow
canonical_url: https://docs.pingidentity.com/integrations/servicenow/setup/pf_servicenow_connector_adding_the_ping_identity_provisioning_role_in_servicenow.html
llms_txt: https://docs.pingidentity.com/integrations/servicenow/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 8, 2024
section_ids:
  steps: Steps
---

# Adding the Ping Identity provisioning role in ServiceNow

To allow PingFederate to manage users in ServiceNow, add the special Ping Identity provisioning role in your ServiceNow instance.

## Steps

1. Sign on to https\://*yourinstance*.servicenow\.com as an administrator.

2. Install the Ping Identity Provisioning Solution app.

   The app contains the provisioning role.

   1. In the ServiceNow admin console, navigate to **All Available Applications**.

   2. Search for and select the **Ping Identity Provisioning Solution** app.

   3. Click **Install**.

3. **Optional:** If you want the ServiceNow connector to be able to remove roles from users, grant additional permissions to the provisioning role.

   |   |                                                                                                                                                                                                                                                                                                                                                                                                                        |
   | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | Due to a limitation in the ServiceNow API, the ServiceNow Provisioner requires additional security permissions to be able to remove roles from users. We recommend that you only grant these permissions if you require the role removal functionality. Otherwise, skip these steps. For more details, see [Known issues and limitations](../release_notes/pf_servicenow_connector_known_issues_and_limitations.html). |

   1. In the upper-right corner, click your administrator account name. Click **Elevate Roles**.

      ![The ServiceNow account name menu.](_images/ndn1574898659542.jpg)

   2. On the **Elevate Roles** dialog, select **security\_admin**. Click **OK**.

   3. Go to **System Security > Access Control (ACL)**. Click **New**.

   4. On the **New record** tab, from the **Operation** list, select **Delete**.

   5. From the **Name** list, select **User Role (sys\_user\_has\_role)**.

   6. In the **Requires role** section, double-click **Insert a new row**.

   7. Enter `ping_identity_provisioning_role`, and then press enter.

      ![The new role field with ping\_identity\_provisioning\_role entered.](_images/gzk1574899230765.jpg)

   8. Click **Submit**.

---

---
title: Changelog
description: The following is the change history for the ServiceNow Provisioner.
component: servicenow
page_id: servicenow:release_notes:pf_servicenow_connector_changelog
canonical_url: https://docs.pingidentity.com/integrations/servicenow/release_notes/pf_servicenow_connector_changelog.html
llms_txt: https://docs.pingidentity.com/integrations/servicenow/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 25, 2024
section_ids:
  servicenow-provisioner-2-3-november-2023: ServiceNow Provisioner 2.3 – November 2023
  servicenow-provisioner-2-3-april-2023: ServiceNow Provisioner 2.3 – April 2023
  servicenow-provisioner-2-3-august-2022: ServiceNow Provisioner 2.3 – August 2022
  servicenow-provisioner-2-3-may-2021: ServiceNow Provisioner 2.3 – May 2021
  servicenow-provisioner-2-2-november-2020: ServiceNow Provisioner 2.2 – November 2020
  servicenow-provisioner-2-2-june-2020: ServiceNow Provisioner 2.2 – June 2020
  servicenow-provisioner-2-1-november-2019: ServiceNow Provisioner 2.1 – November 2019
  servicenow-provisioner-2-0-may-2018: ServiceNow Provisioner 2.0 – May 2018
  servicenow-provisioner-1-0-1-june-2015: ServiceNow Provisioner 1.0.1 – June 2015
  servicenow-provisioner-1-0-january-2015: ServiceNow Provisioner 1.0 – January 2015
---

# Changelog

The following is the change history for the ServiceNow Provisioner.

## ServiceNow Provisioner 2.3 – November 2023

* Certified with the Utah and Vancouver versions of ServiceNow.

## ServiceNow Provisioner 2.3 – April 2023

* Certified with the Tokyo version of ServiceNow.

## ServiceNow Provisioner 2.3 – August 2022

* Certified with the Rome and San Diego versions of ServiceNow.

## ServiceNow Provisioner 2.3 – May 2021

* Certified with the Quebec version of ServiceNow.

* Added support for mapping users to locations in ServiceNow.

## ServiceNow Provisioner 2.2 – November 2020

* Certified with the Paris version of ServiceNow.

* No software changes.

## ServiceNow Provisioner 2.2 – June 2020

* Added the **ServiceNow URL** field and removed the **ServiceNow Instance Name** field.

* Fixed an issue that caused an error when assigning a role when the provisioning user account did not also have that role.

* Added support for the Orlando version of ServiceNow.

## ServiceNow Provisioner 2.1 – November 2019

* Added support for the London, Madrid, and New York versions of ServiceNow.

* Added support for mapping users to departments in ServiceNow.

* Improved user ID validation when updating and deleting users.

* Removed support for the Jakarta and Instanbul versions of ServiceNow.

## ServiceNow Provisioner 2.0 – May 2018

* Added support for Istanbul, Jakarta, and Kingston.

* Added configuration options for CRUD capabilities.

* Added configuration options for provisioning disabled users.

## ServiceNow Provisioner 1.0.1 – June 2015

* Fixed compatibility issues.

## ServiceNow Provisioner 1.0 – January 2015

* Initial release.

* Added support for browser-based SP and IdP-initiated SSO.

* Added support for outbound user provisioning.

---

---
title: Configuring provisioning
description: To allow PingFederate to manage users in ServiceNow, create a user to represent PingFederate in ServiceNow, and then create a service provider connection.
component: servicenow
page_id: servicenow:setup:pf_servicenow_connector_configuring_provisioning
canonical_url: https://docs.pingidentity.com/integrations/servicenow/setup/pf_servicenow_connector_configuring_provisioning.html
llms_txt: https://docs.pingidentity.com/integrations/servicenow/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 8, 2024
section_ids:
  steps: Steps
---

# Configuring provisioning

To allow PingFederate to manage users in ServiceNow, create a user to represent PingFederate in ServiceNow, and then create a service provider connection.

## Steps

1. In your ServiceNow instance, check that every user, even those not targeted for provisioning, has a `Username` attribute set.

   The connector uses this attribute for synchronization with the data store.

2. If you want PingFederate to manage the departments or locations assigned to users in ServiceNow, merge any duplicate `department` or `location` objects with different capitalization, such as `Accounting` and `accounting`.

   For more information, see [Known issues and limitations](../release_notes/pf_servicenow_connector_known_issues_and_limitations.html).

3. Complete the steps in [Adding the Ping Identity provisioning role in ServiceNow](pf_servicenow_connector_adding_the_ping_identity_provisioning_role_in_servicenow.html).

4. Complete the steps in [Creating a provisioning user in ServiceNow](pf_servicenow_connector_creating_a_provisioning_user_in_servicenow.html).

5. Complete the steps in [Creating a provisioning connection](pf_servicenow_connector_creating_a_provisioning_connection.html).

---

---
title: Configuring single sign-on
description: To allow PingFederate to act as an identity provider for ServiceNow, configure SSO, exchange signing certificates, and create a connection.
component: servicenow
page_id: servicenow:setup:pf_servicenow_connector_configuring_single_sign_on
canonical_url: https://docs.pingidentity.com/integrations/servicenow/setup/pf_servicenow_connector_configuring_single_sign_on.html
llms_txt: https://docs.pingidentity.com/integrations/servicenow/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 8, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Configuring single sign-on

To allow PingFederate to act as an identity provider for ServiceNow, configure SSO, exchange signing certificates, and create a connection.

## About this task

|   |                                                                                                                                                            |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Single sign-on integration is an optional part of this integration. If you only want to use the ServiceNow Provisioner for provisioning, skip these steps. |

## Steps

1. In ServiceNow, install the SSO integration plugin.

   |   |                                                                                                                                                                                                                        |
   | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | For official documentation, see [Activate and set up SAML 2.0](https://docs.servicenow.com/bundle/vancouver-platform-security/page/integrate/saml/task/t_ActivateTheSAML2Plugin.html) in the ServiceNow documentation. |

   1. In your ServiceNow instance, go to **System Definition > Plugins**.

   2. Click **Integration - Multiple Provider Single Sign-On Installer**.

   3. On the **Integration - Multiple Provider Single Sign-On Installer** detail screen, in the **Related Links** section, click **Activate/Repair**.

   4. On the **Activate Plugin** dialog, click **Activate**.

   5. After the installation finishes, click **Close & Reload Form**.

2. Complete the steps in [Registering PingFederate as an identity provider in ServiceNow](pf_servicenow_connector_registering_pf_as_an_identity_provider_in_servicenow.html).

3. Complete the steps in [Exchanging signing certificates](pf_servicenow_connector_exchanging_signing_certificates.html).

4. Complete the steps in [Creating a single sign-on connection](pf_servicenow_connector_creating_a_single_sign_on_connection.html).

---

---
title: Creating a provisioning connection
description: To allow PingFederate to manage users in ServiceNow, configure a service provider (SP) connection.
component: servicenow
page_id: servicenow:setup:pf_servicenow_connector_creating_a_provisioning_connection
canonical_url: https://docs.pingidentity.com/integrations/servicenow/setup/pf_servicenow_connector_creating_a_provisioning_connection.html
llms_txt: https://docs.pingidentity.com/integrations/servicenow/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 8, 2024
section_ids:
  steps: Steps
---

# Creating a provisioning connection

To allow PingFederate to manage users in ServiceNow, configure a service provider (SP) connection.

## Steps

1. On the **Identity Provider** screen, in the **SP Connections** area, open an existing connection or create a new one as follows:

   1. Click **Create new**.

   2. On the **Connection Template** screen, select **Use a template for this connection**.

   3. In the **Connection Template** list, select **ServiceNow Connector**.

   4. Click **Choose File**, select the `servicenow-saml-metadata.xml` file from the ServiceNow Provisioner `.zip` archive, and then click **Open**. Click **Next**.

2. On the **Connection Type** screen, select **Outbound Provisioning** and clear any unwanted types. Click **Next**.

3. On the **General Info** screen, in the **Partner's Entity ID**, **Connection Name**, and **Base URL** fields, change *yourinstance* to your ServiceNow instance name. Click **Next**.

4. On the **Outbound Provisioning** screen, configure the provisioning target and channel.

   See [Configuring outbound provisioning](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_spconnectionconfigtasklet_saasprovisioningstate.html) in the PingFederate documentation.

   1. Click **Configure Provisioning**.

   2. On the **Target** screen, in the **Administrator Username** and **Administrator Password** fields, enter the credentials for the user that you created in [Creating a provisioning user in ServiceNow](pf_servicenow_connector_creating_a_provisioning_user_in_servicenow.html).

      |   |                                                                                        |
      | - | -------------------------------------------------------------------------------------- |
      |   | PingFederate verifies the credentials when you activate the channel and SP connection. |

   3. In the **ServiceNow URL** field, enter the URL of your ServiceNow instance. For example, `https://yourinstance.service-now.com`.

   4. Under **Provisioning Options**, customize the provisioning connector actions as shown in [Provisioning options reference](pf_servicenow_connector_provisioning_options_reference.html). Click **Next**.

   5. On the **Manage Channels** screen, create a channel. Click **Done**.

   See [Managing channels](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_saasmanagementtasklet_saasmanagementstate.html) in the PingFederate documentation.

   1. On the **Outbound Provisioning** screen, click **Next**.

5. On the **Activation and Summary** screen, above the **Summary** section, turn on the connection. Click **Save**.

---

---
title: Creating a provisioning user in ServiceNow
description: To allow PingFederate to connect to ServiceNow, create a provisioning user in ServiceNow.
component: servicenow
page_id: servicenow:setup:pf_servicenow_connector_creating_a_provisioning_user_in_servicenow
canonical_url: https://docs.pingidentity.com/integrations/servicenow/setup/pf_servicenow_connector_creating_a_provisioning_user_in_servicenow.html
llms_txt: https://docs.pingidentity.com/integrations/servicenow/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 8, 2024
section_ids:
  steps: Steps
---

# Creating a provisioning user in ServiceNow

To allow PingFederate to connect to ServiceNow, create a provisioning user in ServiceNow.

## Steps

1. In your ServiceNow instance, create the user credentials that PingFederate will use to connect.

   1. Go to **User Administration > Users**. Click **New**.

   2. In the **New Record** window, in the **User ID** field, enter `ping_identity_provisioning_solution_user`.

   3. In the **Password** field, enter a password of your choosing.

   4. Select the **Web service access only** and **Internal integration user** check boxes.

   5. Click **Submit**.

2. Assign the provisioning role to the user.

   1. In your ServiceNow instance, go to **User Administration > Users** and click the newly created user.

   2. On the **Roles** tab, click **Edit**.

   3. In the **Collection** field, search for the `x_pir_ping_prov.ping_identity_provisioning_role` role.

   4. Click the right arrow to add it to the **Roles** list.

   5. Click **Save**.

---

---
title: Creating a single sign-on connection
description: To allow PingFederate to handle single sign-on (SSO) to ServiceNow, create a service provider (SP) connection.
component: servicenow
page_id: servicenow:setup:pf_servicenow_connector_creating_a_single_sign_on_connection
canonical_url: https://docs.pingidentity.com/integrations/servicenow/setup/pf_servicenow_connector_creating_a_single_sign_on_connection.html
llms_txt: https://docs.pingidentity.com/integrations/servicenow/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 8, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Creating a single sign-on connection

To allow PingFederate to handle single sign-on (SSO) to ServiceNow, create a service provider (SP) connection.

## About this task

|   |                                                                                                           |
| - | --------------------------------------------------------------------------------------------------------- |
|   | You can follow these steps to create a new SP connection, or you can modify your provisioning connection. |

## Steps

1. In the PingFederate administrator console, configure an SP connection.

   1. On the **Identity Provider** tab, in the **SP Connections** area, click **Create new**.

   2. On the **Connection Template** tab, select **Use a template for this connection**.

   3. In the **Connection Template** list, select **ServiceNow Connector**.

   4. Click **Choose File**, select the `sn-metadata.xml` file that you exported in [Exchanging signing certificates](pf_servicenow_connector_exchanging_signing_certificates.html), and then click **Open**. Click **Next**.

2. On the **Connection Type** tab, select **Browser SSO Profiles**. If you don't want provisioning, clear **Outbound Provisioning**. Click **Next**.

3. On the **Connection Options** tab, click **Next**.

4. On the **General Info** tab, in the **Partner's Entity ID**, **Connection Name**, and **Base URL** fields, change *yourinstance* to your ServiceNow instance name. Click **Next**.

5. On the **Browser SSO** tab, configure browser SSO.

   For a complete guide, see [Configure IdP Browser SSO](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_spconnectionconfigtasklet_spbrowserssostate.html) in the PingFederate documentation.

   1. On the **Browser SSO > SAML Profiles** tab, select only **IdP-Initiated SSO** and **SP-Initiated SSO**.

   2. On the **Browser SSO > Protocol Settings > Allowable SAML Bindings** tab, select only **POST** and **Redirect**.

6. On the **Credentials** tab, configure the connection credentials.

   For a complete guide, see [Configuring credentials](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_spconnectionconfigtasklet_credentialsstate.html) in the PingFederate documentation.

   1. On the **Credentials > Digital Signature Settings** tab, from the **Signing Certificate** list, select the certificate that you want to use with ServiceNow.

   2. Select **Include the certificate in the signature \<KEYINFO> element**. Click **Done**.

7. On the **Activation and Summary** tab, above the **Summary** section, click the toggle button to enable the connection. Click **Save**.

---

---
title: Deploying the integration files
description: To get started with the integration, deploy the ServiceNow Provisioner files to your PingFederate directory.
component: servicenow
page_id: servicenow:setup:pf_servicenow_connector_deploying_the_integration_files
canonical_url: https://docs.pingidentity.com/integrations/servicenow/setup/pf_servicenow_connector_deploying_the_integration_files.html
llms_txt: https://docs.pingidentity.com/integrations/servicenow/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 8, 2024
section_ids:
  steps: Steps
---

# Deploying the integration files

To get started with the integration, deploy the ServiceNow Provisioner files to your PingFederate directory.

## Steps

1. Download the ServiceNow Provisioner `.zip` archive from the [**Add-ons** tab of the PingFederate downloads page](https://www.pingidentity.com/en/resources/downloads/pingfederate.html) or the [Ping Identity Marketplace](https://marketplace.pingone.com/item/servicenow-single-signon-integration).

2. Stop PingFederate.

3. If you're upgrading an existing deployment, delete the `pf-servicenow-quickconnection-<version>.jar` file from your `<pf_install>/pingfederate/server/default/deploy` directory.

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
description: The following files are included in the ServiceNow Provisioner .zip archive:
component: servicenow
page_id: servicenow:release_notes:pf_servicenow_connector_download_manifest
canonical_url: https://docs.pingidentity.com/integrations/servicenow/release_notes/pf_servicenow_connector_download_manifest.html
llms_txt: https://docs.pingidentity.com/integrations/servicenow/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 8, 2024
---

# Download manifest

The following files are included in the ServiceNow Provisioner `.zip` archive:

* `legal/Legal.pdf` – copyright and license information.

* `dist` – contains the integration files

  * `pf-servicenow-quickconnection-<version>.jar` – The ServiceNow Provisioner quick connection template.

* `servicenow-saml-metadata.xml` – a modifiable metadata file used to create the connection.

---

---
title: Enabling provisioning in PingFederate
description: To use PingFederate for provisioning, configure an external datastore.
component: servicenow
page_id: servicenow:setup:pf_servicenow_connector_enabling_provisioning_in_pf
canonical_url: https://docs.pingidentity.com/integrations/servicenow/setup/pf_servicenow_connector_enabling_provisioning_in_pf.html
llms_txt: https://docs.pingidentity.com/integrations/servicenow/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 8, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
  choose-from: Choose from:
---

# Enabling provisioning in PingFederate

To use PingFederate for provisioning, configure an external datastore.

## About this task

Your external datastore acts as the source of data for provisioning. PingFederate also uses an internal datastore to store the state of synchronization between the source datastore and the target datastore.

For more information, see [Datastores](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_datastores.html) in the PingFederate documentation.

## Steps

1. Configure the datastore for PingFederate to use as the source of user data.

   For instructions, see [Datastores](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_datastores.html) in the PingFederate documentation.

   |   |                                                                                                                                                                                                                                                                           |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | When targeting users and groups for provisioning, exclude the user account that you will use to administer users in your connection to ServiceNow. This prevents the PingFederate provisioning engine from interfering with the account that provisions users and groups. |

2. Do one of the following:

   ### Choose from:

   * For PingFederate 10.1 or later: Go to **System > Server > Protocol Settings**.

   * For PingFederate 10.0 or earlier: Enable the identity provider (IdP) and outbound provisioning roles:

     1. Go to **System > Protocol Settings > Roles & Protocols**.

     2. Select **Enable Identity Provider IdP Role and Support the Following**.

     3. Select **Outbound Provisioning**. Click **Next**.

3. On the **Outbound Provisioning** tab, select the PingFederate internal datastore. Click **Save**.

   For help, see [Configuring outbound provisioning settings](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_protocolsettingstasklet_saasglobalprovisioningsettingsstate.html) in the PingFederate documentation.

---

---
title: Exchanging signing certificates
description: To allow PingFederate and ServiceNow to communicate securely, exchange the signing certificates between the two systems.
component: servicenow
page_id: servicenow:setup:pf_servicenow_connector_exchanging_signing_certificates
canonical_url: https://docs.pingidentity.com/integrations/servicenow/setup/pf_servicenow_connector_exchanging_signing_certificates.html
llms_txt: https://docs.pingidentity.com/integrations/servicenow/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 8, 2024
section_ids:
  steps: Steps
---

# Exchanging signing certificates

To allow PingFederate and ServiceNow to communicate securely, exchange the signing certificates between the two systems.

## Steps

1. In PingFederate, export your signing certificate. On the PingFederate admin console, go to **Security > Signing & Decryption Keys & Certificates**.For the certificate that you want to use, in the **Action** column, click **Export**.On the **Export Certificate** screen, click **Next**.On the **Export & Summary** screen, click **Export**.Open the `*.crt` file in a text editor.

2. In ServiceNow, import your PingFederate signing certificate.

   1. On your ServiceNow instance, go to **SAML 2 Single Sign-on > Certificate**. Click **New**.

   2. On the **New record** screen, in the **Name** field, enter `SAML 2.0`.

   3. **Optional:** In the **Short description** field, enter a description. This appears on the **Certificate** screen.

   4. In the **PEM Certificate** field, paste the contents of the `*.crt` file that you exported from PingFederate.

   5. Click **Submit**.

3. In ServiceNow, export your ServiceNow single logout (SLO) certificate.

   1. On your ServiceNow instance, go to **SAML 2 Single Sign-on > Certificate**. Click **SAML 2.0 SP Keystore**.

   2. On the **SAML 2.0 SP Keystore** screen, download the certificate keystore by clicking **saml2sp\_keystore**.

   3. Extract the certificate from `saml2sp_keystore` as shown in [How to print the Public Key of a Certificate using Keytool](https://hi.service-now.com/kb_view.do?sysparm_article=KB0714222) in the ServiceNow documentation.

   4. Copy the output of the command to a text file on your computer, and save it as `sn-certificate.crt`.

4. In PingFederate, import your ServiceNow SLO certificate as a trusted certificate authority (CA).

   1. On the PingFederate admin console, go to **Security > Trusted CAs**.

   2. On the **Trusted CAs** screen, click **Import**.

   3. On the **Import Certificate** screen, select `sn-certificate.crt`. Click **Next**.

   4. On the **Summary** screen, click **Save**.

5. In ServiceNow, export your SAML 2.0 metadata.

   1. On your ServiceNow instance, go to **SAML 2 Single Sign-on > Metadata**.

   2. Copy the metadata block to a text file on your computer, and save it as `sn-metadata.xml`.

   You will use this in [Creating a single sign-on connection](pf_servicenow_connector_creating_a_single_sign_on_connection.html).

---

---
title: Known issues and limitations
description: The following are known issues or limitations with the ServiceNow Connector.
component: servicenow
page_id: servicenow:release_notes:pf_servicenow_connector_known_issues_and_limitations
canonical_url: https://docs.pingidentity.com/integrations/servicenow/release_notes/pf_servicenow_connector_known_issues_and_limitations.html
llms_txt: https://docs.pingidentity.com/integrations/servicenow/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 25, 2024
section_ids:
  known-issues: Known issues
  known-limitations: Known limitations
---

# Known issues and limitations

The following are known issues or limitations with the ServiceNow Connector.

## Known issues

* Avoid naming `department` and `location` objects with the same format as ServiceNow system IDs, such as `972456281bcc3010dbb0dd7ebd4bcbcc`. This might cause users to be provisioned with an incorrect department or location.

## Known limitations

* Attributes

  * Due to limitations in PingFederate, user attributes cannot be cleared after they are set.

  * Due to a limitation with PingFederate 9.0 and 9.0.1, the `manager` attribute cannot be mapped and used. There is no impact to other functionality.

  * When using the manager attribute, if the user's manager is not managed by the provisioner, the user will be created with an exception thrown. PingFederate will continue to retry the user indefinitely.

  * User role values must contain only URL-safe characters.

  * Due to a limitation in the ServiceNow API, the ServiceNow Connector requires additional security permissions to be able to remove roles from users. If you try to remove a role from a user without granting these permissions, your data store will become out of sync with ServiceNow, and an error will appear in `provisioner.log`. You can grant the permissions as shown in [Adding the Ping Identity provisioning role in ServiceNow](../setup/pf_servicenow_connector_adding_the_ping_identity_provisioning_role_in_servicenow.html).

* Provisioning

  * PingFederate uses the `Username` attribute to synchronize users between the data store and ServiceNow, as described in [User management](../pf_servicenow_connector_user_management.html). When attempting to provisioning a user that does not have a `Username`, PingFederate logs an error in provisioner.log and keeps trying until the `Username` is present.

  * When provisioning users, the username attribute must only contain URL-safe characters.

  * If a new user is created with the same username as an existing user, a duplicate user will not be created. Instead, the existing user will be updated with any information in the create.

  * For `department` objects that contain the `^` character in the name, the ServiceNow API causes the creation of multiple departments with the same name.

  * For the `department` and `location` objects, the ServiceNow API ignores capitalization. When provisioning a user that matches multiple departments or locations in ServiceNow (such as `Accounting` and `accounting`), PingFederate provisions the user with an empty `department` or `location` attribute and logs an error in provisioner.log.

* Deprovisioning

  * When an LDAP user is deleted in a targeted group distinguished name (DN), the provisioning connector does not propagate the deletion until a new user is added to the group. This limitation is compounded when the **User Create** provisioning option is disabled. For solutions, see [SaaS provisioner does not remove the user](https://support.pingidentity.com/s/article/After-deleting-an-AD-user-account-SaaS-provisioner-does-not-remove-the-user-in-the-next-provisioning-cycle-when-Group-DN-is-specified) in the Knowledge Base.

* Performance

  * When synchronizing user roles, PingFederate performs multiple calls to the ServiceNow API. This can impact provisioning performance.

  * When using the default mapping for the manager attribute, the process for adding a manager involves an Active Directory search, followed by a database lookup to get the ServiceNow manager ID. This can impact provisioning performance. To improve performance, you can use a custom attribute mapping to link the manager attribute to a manager's email.

* Configuration

  * When using multiple channels, the same `Username` mapping is required to coordinate manager assignments across different channels.

---

---
title: Provisioning options reference
description: The following are setting descriptions for the ServiceNow provisioning capabilities.
component: servicenow
page_id: servicenow:setup:pf_servicenow_connector_provisioning_options_reference
canonical_url: https://docs.pingidentity.com/integrations/servicenow/setup/pf_servicenow_connector_provisioning_options_reference.html
llms_txt: https://docs.pingidentity.com/integrations/servicenow/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 8, 2024
---

# Provisioning options reference

The following are setting descriptions for the ServiceNow provisioning capabilities.

| Field Name                   | Description                                                                                                                                                                                     |
| ---------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **User Create**              | * Selected (default)

  PingFederate creates users in ServiceNow.

* Cleared

  PingFederate does not create users in ServiceNow.                                                               |
| **User Update**              | - Selected (default)

  PingFederate updates existing users in ServiceNow.

- Cleared

  PingFederate does not update existing users in ServiceNow.                                             |
| **User Disable**             | * Selected (default)

  PingFederate disables users in ServiceNow.

* Cleared

  PingFederate does not disable users in ServiceNow.                                                             |
|                              | &#xA;&#xA;If any of the above options are cleared, PingFederate logs a warning in the user workflow section of the provisioner.log file when the related action fails.                          |
| **Provision Disabled Users** | - Selected

  PingFederate creates users in ServiceNow with a "disabled" status.

- Cleared (default)

  If a user has a "disable" status, PingFederate does not create the user in ServiceNow. |

---

---
title: Registering PingFederate as an identity provider in ServiceNow
description: To allow PingFederate to coordinate authentication for ServiceNow, configure the SAML 2.0 properties.
component: servicenow
page_id: servicenow:setup:pf_servicenow_connector_registering_pf_as_an_identity_provider_in_servicenow
canonical_url: https://docs.pingidentity.com/integrations/servicenow/setup/pf_servicenow_connector_registering_pf_as_an_identity_provider_in_servicenow.html
llms_txt: https://docs.pingidentity.com/integrations/servicenow/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 25, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Registering PingFederate as an identity provider in ServiceNow

To allow PingFederate to coordinate authentication for ServiceNow, configure the SAML 2.0 properties.

## About this task

For official documentation, see [External single sign-on (SSO)](https://docs.servicenow.com/bundle/vancouver-platform-security/page/integrate/single-sign-on/concept/c_MultipleProviderSingleSignOn.html) in the ServiceNow documentation.

## Steps

1. In your ServiceNow instance, go to **SAML 2 Single Sign-on > Properties**.

2. On the **SAML 2.0 Single Sign-on properties** screen, select **Enable external authentication**.

3. In the **Identity Provider properties** section, in the **Identity Provider URL** field, enter your PingFederate URL based on the following:

   https\://*pf\_host*:*pf\_port*

4. In the **base URL to the Identity Provider's AuthnRequest service** field, enter your PingFederate SSO endpoint based on the following:

   https\://*pf\_host*:*pf\_port*/idp/SSO.saml2

5. **Optional:** Select **Sign AuthnRequest**.

6. In the **base URL to the Identity Provider's SingleLogOutRequest service** field, enter your PingFederate SSO endpoint based on the following:

   https\://*pf\_host*:*pf\_port*/idp/SLO.saml2

7. In the **protocol binding for the Identity Provider's SIngleLogoutRequest service** field, enter `urn:oasis:names:tc:SAML:2.0:bindings:HTTP-POST`.

8. Select **Sign LogoutRequest**.

9. In the **Service Provider (ServiceNow) properties** section, update the **instance homepage**, **entity identification**, and **audience uri** fields to point your ServiceNow instance.

10. In the **User table** field, enter `user_name`.

11. In the **NameID policy** field, enter `urn:oasis:names:tc:SAML:1.1:nameid-format:unspecified`.

12. Click **Save**.

---

---
title: ServiceNow Provisioner
description: The PingFederate ServiceNow Provisioner allows PingFederate to integrate with ServiceNow for user provisioning and single sign-on (SSO).
component: servicenow
page_id: servicenow::pf_servicenow_connector
canonical_url: https://docs.pingidentity.com/integrations/servicenow/pf_servicenow_connector.html
llms_txt: https://docs.pingidentity.com/integrations/servicenow/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 8, 2024
section_ids:
  features: Features
  intended-audience: Intended audience
  system-requirements: System requirements
---

# ServiceNow Provisioner

The PingFederate ServiceNow Provisioner allows PingFederate to integrate with ServiceNow for user provisioning and single sign-on (SSO).

## Features

* Manages users in ServiceNow based on changes in an external data store that is attached to PingFederate.

  * Creates, updates, and disables users.

  * Allows you to enable the create, update, and disable capabilities independently.

  * Allows you to provision disabled users.

* Browser-based single sign-on (SSO) and single logout (SLO) initiated by the service provider (SP) or identity provider (IdP).

* Pre-populates some connection settings with the included quick connection template and SAML metadata file.

## Intended audience

This document is intended for PingFederate administrators.

Before you start, you should be familiar with the following:

* The following sections of the PingFederate documentation:

  * [Identity provider SSO configuration](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_ident_provid_sso_config.html)

  * [Datastores](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_managedatasourcestasklet_managedatasourcesstate.html)

  * [Managing digital signing certificates and decryption keys](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_certmanagementtasklet_dsigsigningcert_certmanagementstate.html)

  * [SP connection management](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_sp_connect_management.html)

  * [Configuring outbound provisioning](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_spconnectionconfigtasklet_saasprovisioningstate.html)

  * [Configuring outbound provisioning settings](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_protocolsettingstasklet_saasglobalprovisioningsettingsstate.html)

* The following sections of the ServiceNow documentation:

  * [User administration](https://docs.servicenow.com/bundle/vancouver-platform-administration/page/administer/roles/concept/c_UserAdministration.html)

  * [External single sign-on (SSO)](https://docs.servicenow.com/bundle/vancouver-platform-security/page/integrate/single-sign-on/concept/c_MultipleProviderSingleSignOn.html)

* [Known issues and limitations](release_notes/pf_servicenow_connector_known_issues_and_limitations.html) for this integration.

## System requirements

* PingFederate 9.0 or later.

* To allow PingFederate to make outbound connections to the ServiceNow API, you might need to whitelist the following domain in your firewall:

  * https\://*yourinstance*.service-now\.com

  * https\://*yourinstance*.servicenowservices.com

* Administrator access to a ServiceNow instance running one of the following versions:

  * Vancouver

  * Utah

  * Tokyo

  * San Diego

  * Rome

  * Quebec

  * Paris

  * Orlando

  * New York

  * Madrid

  * London

---

---
title: Supported attributes reference
description: The following attributes can be mapped for user provisioning to ServiceNow.
component: servicenow
page_id: servicenow:setup:pf_servicenow_connector_supported_attributes_reference
canonical_url: https://docs.pingidentity.com/integrations/servicenow/setup/pf_servicenow_connector_supported_attributes_reference.html
llms_txt: https://docs.pingidentity.com/integrations/servicenow/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 25, 2024
---

# Supported attributes reference

The following attributes can be mapped for user provisioning to ServiceNow.

For more information about these attributes, see [Create a user](https://docs.servicenow.com/bundle/vancouver-platform-administration/page/administer/users-and-groups/task/t_CreateAUser.html) in the ServiceNow documentation.

| Attribute            | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| UserName             | The user's unique identifier in ServiceNow\.This attribute maps to the user's `user_id` in ServiceNow. The ServiceNow Provisioner uses this value to synchronize pre-existing users in ServiceNow with the data store.&#xA;&#xA;This user attribute is required for provisioning. It must be unique and is not cannot be updated. For more information, see Known issues and limitations.                                                                                                                                                                                                                                                  |
| First name           | The user's given name. For example, "Barbara" in "Ms. Barbara Jane Jensen, III".                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Last name            | The user's family name. For example, "Jensen" given the full name "Ms. Barbara Jane Jensen, III".                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Middle name          | The user's middle name or names. For example, "Jane" given the full name "Ms. Barbara Jane Jensen, III".                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Prefix               | The user's honorific prefix or prefixes, such as "Ms.", "Mr.", or "Dr." This attribute maps to the user's "introduction" in ServiceNow.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Gender               | The user's gender.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Email                | The user's email address.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Title                | The user's business title, such as "Software engineer".                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Department           | The user's department or work group, such as "Sales".                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Password             | The user's password. Passwords cannot be mapped from a source data store, so this field can be used to set a literal default value.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Password Needs Reset | When set to **true**, the user must change their password at next login.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Language             | The user's language. Uses the two-character language code as defined by the ISO 639-1 standard.This attribute has a default value in ServiceNow. Languages might need to be updated in ServiceNow to account for other allowable values for this field.                                                                                                                                                                                                                                                                                                                                                                                    |
| Location             | The user's geographical location.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Photo                | The user's photo.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Business Phone       | The user's business phone number.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Mobile Phone         | The user's mobile phone number.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Home Phone           | The user's home phone number.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Street               | The user's street address.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| City                 | The user's city or locale.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| State/Province       | The user's state, province, or territory.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Zip/Postal Code      | The user's ZIP or postal code.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Country Code         | The user's country. Uses the two-character country code as defined by the ISO-3166-1 alpha-2 standard.This attribute has a default value in ServiceNow. County Codes might need to be updated in ServiceNow to account for other allowable values for this field.                                                                                                                                                                                                                                                                                                                                                                          |
| Roles                | The user's role, such as "Student" or "Faculty".This attribute supports multiple values.The ServiceNow Provisioner can only assign roles that are already assigned to the user account that you use for provisioning.The ServiceNow Provisioner does not create new roles, so the roles must already exist in ServiceNow\.By default, the ServiceNow Provisioner can set roles but not remove them. To remove this limitation, you can grant elevated security permissions, as shown in [Adding the Ping Identity provisioning role in ServiceNow](pf_servicenow_connector_adding_the_ping_identity_provisioning_role_in_servicenow.html). |
| Notification         | Determines whether to enable notifications. Select **Enable** or **Disable**.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Employee Number      | A string identifier, typically numeric or alphanumeric, assigned to a person, often based on order of hire or association with an organization.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Time Zone            | The user's time zone. Uses IANA time zone database format. For example, "America/Los\_Angeles".&#xA;&#xA;The ServiceNow Provisioner can only set time zones that are already assigned to the user account that you use for provisioning. The time zone might need to be updated in ServiceNow to account for other allowable values in this field.                                                                                                                                                                                                                                                                                         |
| Time Format          | The user's time format. For details on time formatting, see [Global date and time field format](https://docs.servicenow.com/en-US/bundle/vancouver-platform-administration/page/administer/time/reference/r_FormatDateAndTimeFields.html) in the ServiceNow documentation.&#xA;&#xA;The ServiceNow Provisioner can only set time formats that are already assigned to the user account that you use for provisioning.                                                                                                                                                                                                                      |
| Manager              | The distinguished name (DN) representing the manager for the user.&#xA;&#xA;During the first synchronization between ServiceNow and your data store, you might see errors in provisioner.log because the manager for a user has not been provisioned yet. The user is still created without the manager attribute. On the next retry, the manager will exist and the user's manager attribute will be updated.	&#xA;&#xA;This attribute is not supported in PingFederate 9.0 and 9.0.1.                                                                                                                                                    |

---

---
title: Upgrading an existing deployment
description: If you are upgrading from a previous version of the ServiceNow Provisioner, note your existing service provider (SP) connection configuration and create a new connection.
component: servicenow
page_id: servicenow:setup:pf_servicenow_connector_upgrading_an_existing_deployment
canonical_url: https://docs.pingidentity.com/integrations/servicenow/setup/pf_servicenow_connector_upgrading_an_existing_deployment.html
llms_txt: https://docs.pingidentity.com/integrations/servicenow/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 8, 2024
section_ids:
  steps: Steps
---

# Upgrading an existing deployment

If you are upgrading from a previous version of the ServiceNow Provisioner, note your existing service provider (SP) connection configuration and create a new connection.

## Steps

1. Back up your current PingFederate configuration as shown in [Configuration archive](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_configurationarchivetasklet_selectimportexportstate.html) in the PingFederate documentation.

2. In the PingFederate administrative console, open your existing SP connection.

   1. For PingFederate 10.1 or later: go to **Applications > Integration > SP Connections** and select your connection.

   2. For PingFederate 10.0 or earlier: go to **Identity Provider > SP Connections** and select your connection.

3. Note the attribute mappings for your existing SP connection. For help, see [Mapping attributes](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_saaschanneltasklet_saasattrmappingmgmtstate.html) in the PingFederate documentation.

4. Delete your existing SP connection.

   1. For PingFederate 10.1 or later:

      1. Go to **Applications > Integration > SP Connections**.

      2. For your existing connection, click **Select action**, and then click **Delete**. Click **Confirm.**

   2. For PingFederate 10.0 or earlier:

      1. Go to **Identity Provider > SP Connections > Manage All**.

      2. For your existing connection, click **Select action**, and then click **Delete**. Click **Save.**

5. Complete the steps in [Deploying the integration files](pf_servicenow_connector_deploying_the_integration_files.html).

6. Complete the steps in [Creating a provisioning connection](pf_servicenow_connector_creating_a_provisioning_connection.html).

   * From **Outbound Provisioning > Manage Channels > Channel**, on the **Attribute Mapping** tab, configure the attribute mappings based on your notes.

---

---
title: User management
description: The ServiceNow Provisioner links users from the data store to ServiceNow. The behavior of each provisioning capability is described below.
component: servicenow
page_id: servicenow::pf_servicenow_connector_user_management
canonical_url: https://docs.pingidentity.com/integrations/servicenow/pf_servicenow_connector_user_management.html
llms_txt: https://docs.pingidentity.com/integrations/servicenow/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 8, 2024
section_ids:
  synchronizing-existing-users: Synchronizing existing users
  user-provisioning: User provisioning
  user-updates: User updates
  user-deprovisioning-disabling: User deprovisioning (disabling)
---

# User management

The ServiceNow Provisioner links users from the data store to ServiceNow. The behavior of each provisioning capability is described below.

## Synchronizing existing users

By default, the ServiceNow Provisioner synchronizes users from the data store to the target service by matching an attribute in the data store to the `Username` attribute in the target service.

For example:

* In ServiceNow, Janet's `Username` is `jsmith`.

* In your data store, Janet's `sAMAccountName` is `jsmith`.

* On the **Attribute Mapping** tab, you map the `Username` attribute to `sAMAccountName`.

* When the provisioning connector runs, the data store user is provisioned with a `Username` of `jsmith`. That matches Janet's existing `Username` in ServiceNow, so her information in the data store is synchronized to her ServiceNow account.

You can map the matching data store attribute when you configure your channel in [Creating a provisioning connection](setup/pf_servicenow_connector_creating_a_provisioning_connection.html).

## User provisioning

Triggered by any of the following:

* A user is added to the data store group or filter that is targeted by the provisioning connector.

* A user with "disabled" status is added to the data store group or filter that is targeted by the provisioning connector, and the **Provision disabled users** provisioning option is enabled.

The target is determined by the **Source Location** tab in the provisioning connector configuration.

## User updates

Triggered when a change occurs to a user attribute that is mapped in the provisioning connector configuration.

## User deprovisioning (disabling)

Triggered by any of the following:

* A user is deleted from the user store.

* A user is disabled in the user store.

* A user is removed from the data store group or filter that is targeted by the provisioning connector.