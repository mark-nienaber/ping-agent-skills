---
title: Changelog
description: For internal configuration management, the current release of the SAP NetWeaver Integration Kit supports the OpenToken 2.5.1 Adapter and OpenToken Agent.
component: sap-netweaver
page_id: sap-netweaver:release_notes:pf_sap_netweaver_ik_changelog
canonical_url: https://docs.pingidentity.com/integrations/sap-netweaver/release_notes/pf_sap_netweaver_ik_changelog.html
llms_txt: https://docs.pingidentity.com/integrations/sap-netweaver/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 25, 2024
section_ids:
  netweaver-integration-kit-version-2-3-december-2015-current-release: NetWeaver Integration Kit Version 2.3 – December 2015 (Current Release)
  netweaver-integration-kit-version-2-2-1-december-2012: NetWeaver Integration Kit Version 2.2.1 – December 2012
  netweaver-integration-kit-version-2-2-august-2012: NetWeaver Integration Kit Version 2.2 – August 2012
  netweaver-integration-kit-version-2-1-march-2012: NetWeaver Integration Kit Version 2.1 – March 2012
  netweaver-integration-kit-version-2-0-july-2008: NetWeaver Integration Kit Version 2.0 – July 2008
  netweaver-integration-kit-version-1-1-april-2007: NetWeaver Integration Kit Version 1.1 – April 2007
  netweaver-integration-kit-version-1-0-october-2006: NetWeaver Integration Kit Version 1.0 – October 2006
---

# Changelog

|   |                                                                                                                                                           |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | For internal configuration management, the current release of the SAP NetWeaver Integration Kit supports the OpenToken 2.5.1 Adapter and OpenToken Agent. |

## NetWeaver Integration Kit Version 2.3 – December 2015 (Current Release)

* Added support for NetWeaver 7.4.

## NetWeaver Integration Kit Version 2.2.1 – December 2012

* Updated to address security issue found since the previous release.

* Added support for the 2.5.1 version of the OpenToken Adapter and OpenToken Agent

## NetWeaver Integration Kit Version 2.2 – August 2012

* Added support for SAP NetWeaver 7.3

* Added support for determining applications that the login module (`PFLoginModule)` apply to using `excludeUrI`

* Added support for the 2.5.0 version of the OpenToken Agent and Adapter

## NetWeaver Integration Kit Version 2.1 – March 2012

* Deep linking for SP-Initiated SSO added to the NetWeaver Login Module

* Extended the NetWeaver Login Module to support anonymous access for portal applications

## NetWeaver Integration Kit Version 2.0 – July 2008

* SP Initiated SSO functionality added to the NetWeaver Login Module

* SP functionality updated to use OpenToken

* SAP Certification for PingFederate 5 and NetWeaver 7

## NetWeaver Integration Kit Version 1.1 – April 2007

* SP Functionality for SAP NetWeaver

* SAP Certification

## NetWeaver Integration Kit Version 1.0 – October 2006

PingFederate Integration Kit Version 1.0 for NetWeaver was the initial release of the product. It provided the IdP functionality for SAP NetWeaver, whereby users who have been authenticated by NetWeaver can gain access to partner applications using SAML or WS-Federation.

---

---
title: Download manifest
description: The distribution .zip archive for the PingFederate Integration Kit for SAP NetWeaver contains the following:
component: sap-netweaver
page_id: sap-netweaver:release_notes:pf_sap_netweaver_ik_download_manifest
canonical_url: https://docs.pingidentity.com/integrations/sap-netweaver/release_notes/pf_sap_netweaver_ik_download_manifest.html
llms_txt: https://docs.pingidentity.com/integrations/sap-netweaver/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 25, 2024
---

# Download manifest

The distribution `.zip` archive for the PingFederate Integration Kit for SAP NetWeaver contains the following:

* `ReadMeFirst.pdf` – contains links to this online documentation

* `/legal` – contains this document:

  * `Legal.pdf` – copyright and license information

* `/dist` – contains the following libraries that are needed to run the adapter:

  * `pf-netweaver-adapter-1.0.jar` – the NetWeaver IdP Adapter JAR file (IdP only)

  * `PFLoginModuleJAR.jar` `–` PingFederate Login Module JAR file that can be used to create a custom Software Development Archive (SDA) or Enterprise Archive (EAR)

  * `PFLoginModuleLibrary.sda` `– `SDA for NetWeaver 7.0 that contains `PFLoginModule`

  * `PFLoginModuleLibrary.ear` `– `EAR for NetWeaver 7.3 and 7.4 that contains `PFLoginModule`

  * `opentoken-adapter-2.5.1.jar` – OpenToken Adapter JAR file

  * `opentoken-agent-2.5.1.jar` – OpenToken Agent JAR file

  * `commons-collections-3.2.jar` – Apache Commons Collections library

  * `commons-beanutils.jar` – Apache Commons Bean Utility library

  * `commons-logging.jar` – Apache Commons Logging library

---

---
title: IdP installation and setup
description: This section describes how to install and configure the PingFederate Integration Kit for SAP NetWeaver for an IdP.
component: sap-netweaver
page_id: sap-netweaver:setup:pf_sap_netweaver_ik_idp_installation_and_setup
canonical_url: https://docs.pingidentity.com/integrations/sap-netweaver/setup/pf_sap_netweaver_ik_idp_installation_and_setup.html
llms_txt: https://docs.pingidentity.com/integrations/sap-netweaver/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 5, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# IdP installation and setup

## About this task

This section describes how to install and configure the PingFederate Integration Kit for SAP NetWeaver for an IdP.

## Steps

1. Download the NetWeaver Integration Kit `.zip` archive from the [**Add-ons** tab of the PingFederate downloads page](https://www.pingidentity.com/en/resources/downloads/pingfederate.html) or the [Ping Identity Marketplace](https://marketplace.pingone.com/item/netweaver-integration-kit).

2. Shut down the PingFederate server.

3. Unzip the distribution `.zip` archive.

4. Copy the `pf-netweaver-adapter-1.0.jar` file from the `dist` directory to this location:

   `[PingFederate installation directory]/server/default/deploy`

5. Obtain the SSO extension library from SAP and install the libraries on the system running PingFederate (see [System requirements](../pf_sap_netweaver_ik.html#_system_requirements)).

6. Restart the PingFederate server.

7. Log on to the PingFederate administrative console and click **Adapters** from the My IdP Configuration side of the Main Menu.

   For more information, see [Configuring an IdP adapter instance](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_configuring_idp_adapter_instance.html) in the PingFederate documentation.

8. Click **Create New Adapter Instance**.

9. Enter the **Instance Name** and **Instance ID**. Select **PF4 NetWeaver IdP Adapter v1.0** as the **Type** and click **Next**.

10. Enter the values for adapter configuration described below and click **Next**.

    | Property           | Description                                                                                                                               |
    | ------------------ | ----------------------------------------------------------------------------------------------------------------------------------------- |
    | **Domain Name**    | Your domain name, preceded by a period (e.g., ".pingidentity.com").                                                                       |
    | **SAP TicketName** | The name of SAP session ticket for SSO.                                                                                                   |
    | **PSE File**       | The path to `verify.pse`. This file contains the public key for verifying the digital signature. Contact SAP support to obtain this file. |
    | **PAB Password**   | The private address-book password for accessing the public key.                                                                           |
    | **Login URL**      | An optional URL where the user is redirected if SAP session ticket is not found.                                                          |

11. Optionally, on the **Extended Contract** tab, you can configure additional attributes for the adapter. For more information, see [Key concepts](https://docs.pingidentity.com/pingfederate/latest/introduction_to_pingfederate/pf_key_conc.html) in the PingFederate documentation.

    For instance, you can use the extended adapter contract for Policy Server response-object attributes. Click **Next**.

12. On the **Adapter Attributes** tab, select **userId** under Pseudonym. You can also select any extended attributes specified in the previous tab. Click **Next**.

    For more information about this tab, see [Set pseudonym and masking options](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_setting_pseudonym_masking_options.html) in the PingFederate documentation.

13. On the **Summary** tab, verify that the information is correct and click **Done**.

14. Click **Save** to complete the adapter configuration.

---

---
title: Implementing IdP functionality
description: The NetWeaver IdP Adapter uses the SAP SSO extension library to decrypt the session ticket and pass the attributes to the PingFederate server, which maps the values into an assertion and sends the assertion to the SP's federation gateway. For more information about configuration setup and attribute mapping, see Configuring an IdP adapter instance and User attributes in the PingFederate documentation.
component: sap-netweaver
page_id: sap-netweaver:setup:pf_sap_netweaver_ik_implementing_idp_functionality
canonical_url: https://docs.pingidentity.com/integrations/sap-netweaver/setup/pf_sap_netweaver_ik_implementing_idp_functionality.html
llms_txt: https://docs.pingidentity.com/integrations/sap-netweaver/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 25, 2024
---

# Implementing IdP functionality

The NetWeaver IdP Adapter uses the SAP SSO extension library to decrypt the session ticket and pass the attributes to the PingFederate server, which maps the values into an assertion and sends the assertion to the SP's federation gateway. For more information about configuration setup and attribute mapping, see [Configuring an IdP adapter instance](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_configuring_idp_adapter_instance.html) and [User attributes](https://docs.pingidentity.com/pingfederate/latest/introduction_to_pingfederate/pf_user_attrib.html) in the PingFederate documentation.

The following figure illustrates the request flow and how the NetWeaver IdP Adapter is used in generating a SAML assertion:

![psr1563995640073](_images/psr1563995640073.jpg)

**Processing Steps**

1. The user's browser accesses the IdP application.

2. The SAP J2EE Server authenticates the user and creates a session ticket.

3. The user clicks a link that initiates a Single Sign-on (SSO) transaction to the partner application. The request is redirected to the PingFederate IdP Server.

4. The NetWeaver IdP Adapter retrieves the session ticket from the session cookie, decrypts the session ticket, and then transfers the attributes to the PingFederate IdP Server.

5. The PingFederate IdP server generates a SAML assertion and redirects the request, with the assertion, back through the user's browser to the SP site.

---

---
title: Implementing SP functionality
description: The PingFederate SP server receives an assertion (see Service provider SSO configuration in the PingFederate documentation), wraps the received attributes into OpenToken, and redirects to an application protected by NetWeaver. The PFLoginModule configured in NetWeaver extracts the UserID from OpenToken and authenticates the user. Note that UserID is the value of the "subject" attribute in the OpenToken.
component: sap-netweaver
page_id: sap-netweaver:setup:pf_sap_netweaver_ik_implementing_sp_functionality
canonical_url: https://docs.pingidentity.com/integrations/sap-netweaver/setup/pf_sap_netweaver_ik_implementing_sp_functionality.html
llms_txt: https://docs.pingidentity.com/integrations/sap-netweaver/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 25, 2024
---

# Implementing SP functionality

The PingFederate SP server receives an assertion (see [Service provider SSO configuration](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_servic_provid_sso_config.html) in the PingFederate documentation), wraps the received attributes into `OpenToken`, and redirects to an application protected by NetWeaver. The `PFLoginModule` configured in NetWeaver extracts the `UserID` from OpenToken and authenticates the user. Note that `UserID` is the value of the "subject" attribute in the OpenToken.

The following figure illustrates the request flow and how the PingFederate OpenToken SP Adapter wraps attributes from the assertion into `OpenToken` and passes them to SAP NetWeaver (J2EE Engine):

![qyr1563995644419](_images/qyr1563995644419.jpg)

**Processing Steps**

1. The PingFederate SP server receives a SAML assertion from the IdP.

2. The PingFederate SP server wraps the attributes from the SAML assertion into an `OpenToken` and redirects the token through the user's browser to the application(s) deployed on the SAP J2EE Server.

3. `PFLoginModule`, installed in SAP J2EE Server, parses the `OpenToken` and retrieves the `UserID`.

4. The SAP J2EE server authenticates the user using this UserID and grants access to the SAP Application.

---

---
title: Known issues and limitations
description: Known issues and limitations
component: sap-netweaver
page_id: sap-netweaver:release_notes:pf_sap_netweaver_ik_known_issues_and_limitations
canonical_url: https://docs.pingidentity.com/integrations/sap-netweaver/release_notes/pf_sap_netweaver_ik_known_issues_and_limitations.html
llms_txt: https://docs.pingidentity.com/integrations/sap-netweaver/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 25, 2024
---

# Known issues and limitations

**Known issues and limitations**

* Logout does not integrate with the JAAS module to perform Single Log-Out (SLO) because of the sequence SLO must take. Applications wishing to use SLO functionality must be modified to include a reference to PingFederate's SLO service within the application itself.

* Account linking is not supported.

* In cases where the SP-initiated SSO property (`enableSPSSO`) is set to true, and the `ssoURL` property is set incorrectly, authentication through PingFederate and access to the administrative console is not possible. IdP-initiated SSO requests can be made along with the NetWeaver administrative console URL as a Target Resource. This temporarily allows access to the NetWeaver administrative console to set the correct SSO URL.

  For example: https\://\<hostname>:\<port>/idp/startSSO.ping?PartnerSpId=\<hostname>:default:entityId\&TargetResource=http\://\<hostname>:\<port>/nwa

---

---
title: OpenToken adapter setup
description: If you have already deployed version 2.5.1 (or later) of the OpenToken Adapter skip steps 1 - 4 in the following procedure.
component: sap-netweaver
page_id: sap-netweaver:setup:pf_sap_netweaver_ik_opentoken_adapter_setup
canonical_url: https://docs.pingidentity.com/integrations/sap-netweaver/setup/pf_sap_netweaver_ik_opentoken_adapter_setup.html
llms_txt: https://docs.pingidentity.com/integrations/sap-netweaver/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 25, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# OpenToken adapter setup

## About this task

|   |                                                                                                                             |
| - | --------------------------------------------------------------------------------------------------------------------------- |
|   | If you have already deployed version 2.5.1 (or later) of the OpenToken Adapter skip steps 1 - 4 in the following procedure. |

## Steps

1. Stop the PingFederate server if it is running.

2. Remove any existing OpenToken Adapter files (`opentoken*.jar`) from the `<PF_install>/pingfederate/server/default/deploy` directory.

   The adapter JAR file is `opentoken-adapter-<version>.jar`.

   |   |                                                                                                          |
   | - | -------------------------------------------------------------------------------------------------------- |
   |   | In the same directory (`server/default/deploy`), delete the `opentoken-java-1.x.jar` file, if it exists. |

   |   |                                                                                                                          |
   | - | ------------------------------------------------------------------------------------------------------------------------ |
   |   | If it exists, delete the `opentoken-adapter.jar` file from the `<PF_install>/pingfederate/server/default/lib` directory. |

3. Unzip the integration-kit distribution file and copy `opentoken-adapter-2.5.1.jar` from the `/dist` directory to the PingFederate directory:

   `<PF_install>/pingfederate/server/default/deploy`

4. Start or restart the PingFederate server.

5. Configure an instance of the OpenToken Adapter. You can find instructions in [OpenToken Adapter](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_opentoken_adapt.html) in the PingFederate documentation.

6. On the **Adapter Actions** page in the adapter setup steps, click the **Invoke Download** link and then click **Export** to download the `agent-config.txt` properties file to a directory that's readable by the SAP J2EE Server.

---

---
title: SAP J2EE setup
description: Configure NetWeaver J2EE to create SSO tickets.
component: sap-netweaver
page_id: sap-netweaver:setup:pf_sap_netweaver_ik_sap_j2ee_setup
canonical_url: https://docs.pingidentity.com/integrations/sap-netweaver/setup/pf_sap_netweaver_ik_sap_j2ee_setup.html
llms_txt: https://docs.pingidentity.com/integrations/sap-netweaver/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 5, 2024
section_ids:
  steps: Steps
---

# SAP J2EE setup

## Steps

* Configure NetWeaver J2EE to create SSO tickets.

  For instructions, see the [SAP Help](https://help.sap.com/docs/SAP_NETWEAVER_700?version=7.0.37).

---

---
title: SAP J2EE setup for NetWeaver 7.0
description: To allow for deep linking for SP-initiated SSO, the login module appends the target-resource URL to the ssoUrl property. This feature is supported only for NetWeaver portals; for other applications the target resource is not appended and the user will go to the Default URL configured in PingFederate. For more information, see Configuring default URLs in the PingFederate documentation.
component: sap-netweaver
page_id: sap-netweaver:setup:pf_sap_netweaver_ik_sap_j2ee_setup_for_netweaver_70
canonical_url: https://docs.pingidentity.com/integrations/sap-netweaver/setup/pf_sap_netweaver_ik_sap_j2ee_setup_for_netweaver_70.html
llms_txt: https://docs.pingidentity.com/integrations/sap-netweaver/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 5, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# SAP J2EE setup for NetWeaver 7.0

## About this task

* To allow for deep linking for SP-initiated SSO, the login module appends the target-resource URL to the `ssoUrl` property. This feature is supported only for NetWeaver portals; for other applications the target resource is not appended and the user will go to the Default URL configured in PingFederate. For more information, see [Configuring default URLs](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_localsettingstasklet_configspeventsstate.html) in the PingFederate documentation.

* The login module JAR file (`PFLoginModuleJAR.jar`), along with supporting JARS included with this distribution, can be used to create a custom SDA for the NetWeaver platform. For more information see the [SAP Help](https://help.sap.com/docs/SAP_NETWEAVER_700/de4c79d6d1794786822442e1a131d859/e62eb540e4c5782ae10000000a155106.html?version=7.0.37).

## Steps

1. Deploy the login module included with this distribution (`PFLoginModuleLibrary.sda`) to NetWeaver using the Software Deployment Manager (SDM).

   |   |                                                                                                                                                                                                                 |
   | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | For information on how to deploy a login module, please refer to [SAP Help](https://help.sap.com/docs/SAP_NETWEAVER_700/de4c79d6d1794786822442e1a131d859/4899a22e7f020e27e10000000a421937.html?version=7.0.37). |

2. Add a reference to the `Classloader` through the Config Tool, using this value for the library `PingIdentity-PFLoginModuleLibrary`.

   |   |                                                                                                                                                                                                                                                          |
   | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | For information on how to add a reference, see [Adding a Reference to the Classloader of the Security Provider](https://help.sap.com/viewer/de4c79d6d1794786822442e1a131d859/7.0.37/en-US/2b23e4407211732ae10000000a155106.html) in the SAP Help Portal. |

3. Configure the login module through the Visual Administrator, using the class name `com.pingidentity.adapters.netweaver.sp.PFLoginModuleClass` and the following options:

   | Option                    | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
   | ------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | `agentPropertiesFileName` | Filename with full path to the location of OpenToken properties file. For example, `C:\agent-config.txt`.                                                                                                                                                                                                                                                                                                                                                                                                                         |
   | `pfBaseUrl`               | Base URL to the PingFederate SP instance.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
   | `enableSPSSO`             | If `true`, `PFLoginModule` redirects to the `ssoUrl` (below) if `OpenToken` is not found in the request. This enables SP-initiated SSO functionality for NetWeaver.The default value is `false`.                                                                                                                                                                                                                                                                                                                                  |
   | `ssoUrl`                  | URL for redirect if SP-initiated SSO, required only if is enabled (above). The value required is PingFederate's application endpoint to start the SSO: http\[s]://\<PF\_host>:\<port>/SP/startSSO.ping ?PartnerIdpId=\<connection\_id>For more information, see Developer Notes below.                                                                                                                                                                                                                                            |
   | `excludeUrI`              | List of excluded resource URIs using regular expressions. For example: `/webdynpro.`                                                                                                                                                                                                                                                                                                                                                                                                                                              |
   | `enableSSOCookie`         | If `true` and `enableSPSSO` is set to `true`, `PFLoginModule` redirects only if a cookie (an SSO Cookie, defined below) is found in the request. The SP sets an SSO Cookie in the user's browser during an initial IdP-initiated SSO event. When the user arrives at the NetWeaver SP in the future, with the SSO Cookie, the user is redirected to the `ssoUrl`.If `false` and `enableSPSSO` is set to `true`, the `PFLoginModule` redirects any user to the `ssoUrl`, regardless of any SSO Cookie.The default value is `false` |
   | `ssoCookieName`           | The name of the SSO cookie to set in the user's browser, required only if `enableSSOCookie` is set to `true`.                                                                                                                                                                                                                                                                                                                                                                                                                     |

   |   |                                                                                                                                                                                                                        |
   | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | For information on how to configure a login module, please refer to the [SAP Help](https://help.sap.com/docs/SAP_NETWEAVER_700/de4c79d6d1794786822442e1a131d859/48fdbdca9a8d2b34e10000000a421937.html?version=7.0.37). |

4. Configure an application to use the login module. A sample configuration, which allows for both SSO and direct authentication, is shown below:

   | Login Module                | Flag         |
   | --------------------------- | ------------ |
   | `EvaluateTicketLoginModule` | `SUFFICIENT` |
   | `PFLoginModule`             | `REQUISITE`  |
   | `BasicPasswordLoginModule`  | `REQUISITE`  |
   | `CreateTicketLoginModule`   | `OPTIONAL`   |

   |   |                                                                                                                                                                                                                                                       |
   | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | For information on how to configure an application, see [Configuring an Application to Use the Login Module](https://help.sap.com/viewer/de4c79d6d1794786822442e1a131d859/7.0.37/en-US/5b3fda40eacd3d43e10000000a155106.html) in the SAP Help Portal. |

---

---
title: SAP J2EE setup for NetWeaver 7.3
description: To allow for deep linking for SP-initiated SSO, the login module appends the target-resource URL to the ssoUrl property. This feature is supported only for NetWeaver portals; for other applications the target resource is not appended and the user will go to the Default URL configured in PingFederate. For more information, see Configuring default URLs in the PingFederate documentation.
component: sap-netweaver
page_id: sap-netweaver:setup:pf_sap_netweaver_ik_sap_j2ee_setup_for_netweaver_73
canonical_url: https://docs.pingidentity.com/integrations/sap-netweaver/setup/pf_sap_netweaver_ik_sap_j2ee_setup_for_netweaver_73.html
llms_txt: https://docs.pingidentity.com/integrations/sap-netweaver/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 27, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# SAP J2EE setup for NetWeaver 7.3

## About this task

* To allow for deep linking for SP-initiated SSO, the login module appends the target-resource URL to the `ssoUrl` property. This feature is supported only for NetWeaver portals; for other applications the target resource is not appended and the user will go to the Default URL configured in PingFederate. For more information, see [Configuring default URLs](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_localsettingstasklet_configspeventsstate.html) in the PingFederate documentation.

* The login module JAR file (`PFLoginModuleJAR.jar`), along with supporting JARS included with this distribution, can be used to create a custom EAR for the NetWeaver platform. For more information, see [Configuring the Login Module on the AS Java](https://help.sap.com/viewer/7ece2b41e5234afb98052b6ad1ab3e2f/7.3.20/en-US/48fdbdca9a8d2b34e10000000a421937.html) in the SAP Help Portal.

## Steps

1. Deploy the login module included with this distribution (`PFLoginModuleLibrary.ear`) to NetWeaver using the appropriate version of SAP NetWeaver Developer Studio.

   |   |                                                                                                                                                  |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------ |
   |   | For information on how to deploy a login module, please refer to [SAP Help](https://help.sap.com/viewer/product/SAP_NETWEAVER_730/7.3.17/en-US). |

2. Configure the login module through the NetWeaver Administrator, using the following options:

   | Option                    | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
   | ------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | `agentPropertiesFileName` | Filename with full path to the location of OpenToken properties file (for example, `C:\agent-config.txt)`.                                                                                                                                                                                                                                                                                                                                                                                                                         |
   | `pfBaseUrl`               | Base URL to the PingFederate SP instance.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
   | `enableSPSSO`             | If `true`, `PFLoginModule` redirects to the `ssoUrl` (below) if `OpenToken` is not found in the request. This enables SP-initiated SSO functionality for NetWeaver. The default value is `false`.                                                                                                                                                                                                                                                                                                                                  |
   | `ssoUrl`                  | URL for redirect if SP-initiated SSO, required only if is enabled (above). The value required is PingFederate's application endpoint to start the SSO:http\[s]://\<PF\_host>:\<port>/SP/startSSO.ping`?PartnerIdpId=<connection_id>`For more information, see Developer Notes below.                                                                                                                                                                                                                                               |
   | `excludeUrI`              | List of excluded resource URIs using regular expressions. For example: `./webdynpro.`                                                                                                                                                                                                                                                                                                                                                                                                                                              |
   | `enableSSOCookie`         | If `true` and `enableSPSSO` is set to `true`, `PFLoginModule` redirects only if a cookie (an SSO Cookie, defined below) is found in the request. The SP sets an SSO Cookie in the user's browser during an initial IdP-initiated SSO event. When the user arrives at the NetWeaver SP in the future, with the SSO Cookie, the user is redirected to the `ssoUrl`.If `false` and `enableSPSSO` is set to `true`, the `PFLoginModule` redirects any user to the `ssoUrl`, regardless of any SSO Cookie.The default value is `false`. |
   | `ssoCookieName`           | The name of the SSO cookie to set in the user's browser, required only if `enableSSOCookie` is set to `true`.                                                                                                                                                                                                                                                                                                                                                                                                                      |

   |   |                                                                                                                                                         |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | For information on how to configure a login module, please refer to the [SAP Help](https://help.sap.com/viewer/product/SAP_NETWEAVER_730/7.3.17/en-US). |

3. Configure an application to use the login module. A sample configuration which allows for both SSO and direct authentication is shown below:

   | Login Module                | Flag         |
   | --------------------------- | ------------ |
   | `EvaluateTicketLoginModule` | `SUFFICIENT` |
   | `PFLoginModule`             | `REQUISITE`  |
   | `BasicPasswordLoginModule`  | `REQUISITE`  |
   | `CreateTicketLoginModule`   | `OPTIONAL`   |

   |   |                                                                                                                                                                                                                                                       |
   | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | For information on how to configure an application, see [Configuring an Application to Use the Login Module](https://help.sap.com/viewer/de4c79d6d1794786822442e1a131d859/7.0.37/en-US/5b3fda40eacd3d43e10000000a155106.html) in the SAP Help Portal. |

---

---
title: SAP J2EE setup for NetWeaver 7.3 or 7.4
description: To allow for deep linking for SP-initiated SSO, the login module appends the target-resource URL to the ssoUrlproperty. This feature is supported only for NetWeaver portals; for other applications the target resource is not appended and the user will go to the Default URL configured in PingFederate. For more information, see Configuring default URLs in the PingFederate documentation.
component: sap-netweaver
page_id: sap-netweaver:setup:pf_sap_netweaver_ik_sap_j2ee_setup_for_netweaver_73_or_74
canonical_url: https://docs.pingidentity.com/integrations/sap-netweaver/setup/pf_sap_netweaver_ik_sap_j2ee_setup_for_netweaver_73_or_74.html
llms_txt: https://docs.pingidentity.com/integrations/sap-netweaver/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 5, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# SAP J2EE setup for NetWeaver 7.3 or 7.4

## About this task

* To allow for deep linking for SP-initiated SSO, the login module appends the target-resource URL to the ssoUrlproperty. This feature is supported only for NetWeaver portals; for other applications the target resource is not appended and the user will go to the Default URL configured in PingFederate. For more information, see [Configuring default URLs](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_localsettingstasklet_configspeventsstate.html) in the PingFederate documentation.

* The login module JAR file (`PFLoginModuleJAR.jar`), along with supporting JARS included with this distribution, can be used to create a custom EAR for the NetWeaver platform. For more information, see [Configuring the Login Module on the AS Java](https://help.sap.com/viewer/7ece2b41e5234afb98052b6ad1ab3e2f/7.3.20/en-US/48fdbdca9a8d2b34e10000000a421937.html) in the SAP Help Portal.

## Steps

1. Deploy the login module included with this distribution (`PFLoginModuleLibrary.ear`) to NetWeaver using the appropriate version of SAP NetWeaver Developer Studio.

   |   |                                                                                                                                                                                                 |
   | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | For information on how to deploy a login module, including how to deploy through shell scripts, please refer to [SAP Help](https://help.sap.com/viewer/product/SAP_NETWEAVER_730/7.3.17/en-US). |

2. Configure the login module through the NetWeaver Administrator, using the following options:

   | Option                    | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
   | ------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | Option                    | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
   | `agentPropertiesFileName` | Filename with full path to the location of OpenToken properties file for example, `C:\agent-config.txt`.                                                                                                                                                                                                                                                                                                                                                                                                        |
   | `pfBaseUrl`               | Base URL to the PingFederate SP instance.                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
   | `enableSPSSO`             | If true, `PFLoginModule` redirects to the `ssoUrl` (below) if `OpenToken` is not found in the request. This enables SP-initiated SSO functionality for NetWeaver.The default value is `false`.                                                                                                                                                                                                                                                                                                                  |
   | `ssoUrl`                  | URL for redirect if SP-initiated SSO, required only if is enabled (above). The value required is PingFederate's application endpoint to start the SSO: `http[s]://<PF_host>:<port>/SP/startSSO.ping?PartnerIdpId=<connection_id>`For more information, see Developer Notes below.                                                                                                                                                                                                                               |
   | `excludeUrI`              | List of excluded resource URIs using regular expressions. For example:`./webdynpro.`                                                                                                                                                                                                                                                                                                                                                                                                                            |
   | `enableSSOCookie`         | If true and `enableSPSSO` is set to `true`, `PFLoginModule` redirects *only* if a cookie (an SSO Cookie, defined below) is found in the request. The SP sets an SSO Cookie in the user's browser during an initial IdP-initiated SSO event. When the user arrives at the NetWeaver SP in the future, with the SSO Cookie, the user is redirected to the ssoUrl.If false and `enableSPSSO` is set to `true`, the PFLoginModule redirects any user to the ssoUrl, regardless of any SSO Cookie.(Default: `false`) |
   | `ssoCookieName`           | The name of the SSO cookie to set in the user's browser, required only if `enableSSOCookie` is set to true.                                                                                                                                                                                                                                                                                                                                                                                                     |

   |   |                                                                                                                                                         |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | For information on how to configure a login module, please refer to the [SAP Help](https://help.sap.com/viewer/product/SAP_NETWEAVER_730/7.3.17/en-US). |

3. Configure an application to use the login module. A sample configuration which allows for both SSO and direct authentication is shown below:

   | Option                      | Description |
   | --------------------------- | ----------- |
   | `Login Module`              | Flag        |
   | `EvaluateTicketLoginModule` | SUFFICIENT  |
   | `PFLoginModule`             | REQUISITE   |
   | `BasicPasswordLoginModule`  | REQUISITE   |
   | `CreateTicketLoginModule`   | OPTIONAL    |

   |   |                                                                                                                                                                                                                                                       |
   | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | For information on how to configure an application, see [Configuring an Application to Use the Login Module](https://help.sap.com/viewer/de4c79d6d1794786822442e1a131d859/7.0.37/en-US/5b3fda40eacd3d43e10000000a155106.html) in the SAP Help Portal. |

---

---
title: SAP NetWeaver Integration Kit
description: The PingFederate Integration Kit for SAP NetWeaver provides Identity Provider (IdP) and Service Provider (SP) functionality to PingFederate. This kit allows an enterprise to extend its existing NetWeaver investment by expanding the reach of the NetWeaver domain to federated partner applications.
component: sap-netweaver
page_id: sap-netweaver::pf_sap_netweaver_ik
canonical_url: https://docs.pingidentity.com/integrations/sap-netweaver/pf_sap_netweaver_ik.html
llms_txt: https://docs.pingidentity.com/integrations/sap-netweaver/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 25, 2024
section_ids:
  intended-audience: Intended audience
  system-requirements: System requirements
---

# SAP NetWeaver Integration Kit

The PingFederate Integration Kit for SAP NetWeaver provides Identity Provider (IdP) and Service Provider (SP) functionality to PingFederate. This kit allows an enterprise to extend its existing NetWeaver investment by expanding the reach of the NetWeaver domain to federated partner applications.

Additionally, this kit enables an SP enterprise to accept SAML assertions and provide single sign-on (SSO) to NetWeaver applications. The assertions may be sent using either the SAML protocol (version 2.0 or 1.x) or the WS-Federation passive-requestor protocol.

## Intended audience

This document is intended for PingFederate administrators.

Before you start, you should be familiar with the following parts of the PingFederate documentation:

* [Identity provider SSO configuration](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_ident_provid_sso_config.html)

* [Managing IdP adapters](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_managing_idp_adapters.html)

## System requirements

* PingFederate 6 or later

* NetWeaver Application Server 7.0, NetWeaver Application Server 7.3, or NetWeaver Application server 7.4

* For an IdP:

  * SAP Single Sign-on (SSO) Extension Library (`sapssoext`), which existing customers can obtain from SAP. See [Single Sign-On to Non-SAP Systems and Applications](https://help.sap.com/viewer/e815bb97839a4d83be6c4fca48ee5777/7.3.20/en-US/129f244183bb8639e10000000a1550b0.html) in the SAP documentation.

* For a SP:

  * The PingFederateOpenToken Adapter 2.5.1 or later installed on PingFederate

  * `PFLoginModule`, installed on the SAP NetWeaver Application Server

---

---
title: Testing the IdP adapter
description: You can test this adapter using the samples applications that are included in the Java Integration Kit.
component: sap-netweaver
page_id: sap-netweaver:setup:pf_sap_netweaver_ik_testing_the_idp_adapter
canonical_url: https://docs.pingidentity.com/integrations/sap-netweaver/setup/pf_sap_netweaver_ik_testing_the_idp_adapter.html
llms_txt: https://docs.pingidentity.com/integrations/sap-netweaver/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 25, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
  result: Result
---

# Testing the IdP adapter

## About this task

You can test this adapter using the samples applications that are included in the Java Integration Kit.

## Steps

1. Download the Java Integration kit from the [PingFederate server add-ons page](https://www.pingidentity.com/en/resources/downloads/pingfederate.html).

2. Complete the steps in [Sample application setup](../../java/setup/pf_java_ik_sample_application_setup.html) in the Java Integration Kit documentation to set up an IdP application.

3. Configure an instance of the NetWeaver IdP Adapter as shown in [IdP installation and setup](pf_sap_netweaver_ik_idp_installation_and_setup.html).

4. Reconfigure the SP connection to use the NetWeaver Adapter instance.

   Delete the existing adapter instance and map the NetWeaver Adapter instance in its place. For more information, see [Managing mappings](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_managing_mappings.html) in the PingFederate documentation.

5. On a web page protected by the NetWeaver Application Server, create an SSO link to the PingFederate `startSSO` endpoint, including the sample SP's connection ID, in the following format:

   ```
   [.codeph]``http[s]://<PF_host>:<port>/IdP/startSSO.ping ``
   ```

   ```
   [.codeph]``?PartnerSpId=<connection_id>``
   ```

   where:

   * `<PF_host>` is the machine running the PingFederate server,

   * `<port>` is the PingFederate port (refer to the PingFederate *Administrator's Manual*),

   * `<connection_id>` is the Connection ID of the SP connection.

6. Access the protected web page by authenticating through NetWeaver, and click the SSO link.

## Result

You are logged on to the Java sample application.

---

---
title: Testing the SP adapter
description: You can test this adapter using the samples applications that are included in the Java Integration Kit.
component: sap-netweaver
page_id: sap-netweaver:setup:pf_sap_netweaver_ik_testing_the_sp_adapter
canonical_url: https://docs.pingidentity.com/integrations/sap-netweaver/setup/pf_sap_netweaver_ik_testing_the_sp_adapter.html
llms_txt: https://docs.pingidentity.com/integrations/sap-netweaver/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 25, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Testing the SP adapter

## About this task

You can test this adapter using the samples applications that are included in the Java Integration Kit.

## Steps

1. Download the Java Integration kit from the [PingFederate server add-ons page](https://www.pingidentity.com/en/resources/downloads/pingfederate.html).

2. Complete the steps in [Sample application setup](../../java/setup/pf_java_ik_sample_application_setup.html) in the Java Integration Kit documentation to set up an SP application.

3. Configure an instance of the OpenToken SP Adapter and PFLoginModule. For more information, see [Implementing SP functionality](pf_sap_netweaver_ik_implementing_sp_functionality.html).

4. Reconfigure the IdP connection to use the OpenToken Adapter instance configured for NetWeaver.

   Delete the existing adapter instance for the connection and map the OpenToken Adapter instance in its place. See [Managing mappings](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_managing_mappings.html) in the PingFederate documentation.

5. Protect a web page using NetWeaver.

6. On the same NetWeaver server, create an unprotected web page with a hyperlink to PingFederate's SP-initiated SSO endpoint in the following format:

   ```none
   http[s]://<PF_host>:<port>/sp/startSSO.ping (1)(2)
   ?TargetResource=<protected_resource> (3)
   ?PartnerIdpId=<connection_id> (4)
   ```

   |       |                                                                        |
   | ----- | ---------------------------------------------------------------------- |
   | **1** | `<PF_host>` is the machine running the PingFederate server.            |
   | **2** | `<port>` is the port (refer to the PingFederate documentation).        |
   | **3** | `<protected_resource>` is the web page protected in the previous step. |
   | **4** | `<connection_id>` is the Connection ID of the IdP connection.          |

7. Click the SSO link on the unprotected web page.

   The SP application login page displays.

8. Add at least one of the users in the username drop-down list to NetWeaver.

9. On the IdP Application's login page, log in with a username managed by NetWeaver.

   You are redirected to the NetWeaver-protected web page.