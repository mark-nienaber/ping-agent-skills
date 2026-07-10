---
title: Adding the OpenToken HTTP Module in IIS
description: The OpenToken HTTP module allows your IIS server to communicate with PingFederate using the OpenToken format.
component: microsoft-iis
page_id: microsoft-iis:setup:pf_iis_ik_adding_the_opentoken_http_module_in_iis
canonical_url: https://docs.pingidentity.com/integrations/microsoft-iis/setup/pf_iis_ik_adding_the_opentoken_http_module_in_iis.html
llms_txt: https://docs.pingidentity.com/integrations/microsoft-iis/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 2, 2025
section_ids:
  steps: Steps
  example: Example:
---

# Adding the OpenToken HTTP Module in IIS

The OpenToken HTTP module allows your IIS server to communicate with PingFederate using the OpenToken format.

## Steps

1. In the Internet Information Services (IIS) Manager, select the IIS server.

2. On the **Features View** tab, double-click **Modules**.

3. On the **Modules** window, in the **Actions** section, click **Add Managed Module**.

4. On the **Add Managed Module** dialog, in the **Name** field, enter a name.

   ### Example:

   `OpenTokenHttpModule`

5. In the **Type** field, enter the following:

   `OpenTokenModule.HttpModule, OpenTokenModule, Version=3.5.0.0, Culture=neutral, PublicKeyToken=f5ed9639debbca65`

   |   |                                                                                      |
   | - | ------------------------------------------------------------------------------------ |
   |   | The OpenToken HTTP Module doesn't automatically appear in the module selection list. |

6. Click **OK**.

---

---
title: Changelog
description: The following is the change history for the IIS Integration Kit.
component: microsoft-iis
page_id: microsoft-iis:release_notes:pf_iis_ik_changelog
canonical_url: https://docs.pingidentity.com/integrations/microsoft-iis/release_notes/pf_iis_ik_changelog.html
llms_txt: https://docs.pingidentity.com/integrations/microsoft-iis/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 2, 2025
section_ids:
  iis-integration-kit-3-5-march-2021: IIS Integration Kit 3.5 – March 2021
  iis-integration-kit-3-4-2-december-2020: IIS Integration Kit 3.4.2 – December 2020
  iis-integration-kit-3-4-1-february-2020: IIS Integration Kit 3.4.1 – February 2020
  iis-integration-kit-3-4-january-2019: IIS Integration Kit 3.4 – January 2019
  iis-integration-kit-3-3-1-june-2018: IIS Integration Kit 3.3.1 – June 2018
  iis-integration-kit-3-3-december-2017: IIS Integration Kit 3.3 – December 2017
  iis-integration-kit-3-2-june-2014: IIS Integration Kit 3.2 – June 2014
  iis-integration-kit-3-1-december-2012: IIS Integration Kit 3.1 – December 2012
  iis-integration-kit-3-0-october-2011: IIS Integration Kit 3.0 – October 2011
  iis-integration-kit-2-2-september-2009: IIS Integration Kit 2.2 – September 2009
  iis-integration-kit-2-1-june-2009: IIS Integration Kit 2.1 – June 2009
  iis-integration-kit-2-0-december-2008: IIS Integration Kit 2.0 – December 2008
  iis-integration-kit-1-1-september-2007: IIS Integration Kit 1.1 – September 2007
  iis-integration-kit-1-0-june-2007: IIS Integration Kit 1.0 – June 2007
---

# Changelog

The following is the change history for the IIS Integration Kit.

## IIS Integration Kit 3.5 – March 2021

* Added the ability to protect multiple sites under the same domain using one instance of the adapter.

* Fixed an issue that caused the adapter to ignore the `token-lifetime` and `secure-cookie` parameters in the `agent-config.txt` file.

## IIS Integration Kit 3.4.2 – December 2020

* Fixed an issue that caused the adapter to ignore the cookie settings in the agent config file.

* Fixed an issue that caused the samesite cookie and legacy cookie to become out of sync.

## IIS Integration Kit 3.4.1 – February 2020

* Added support for the `SameSite` cookie flag in web browsers.

## IIS Integration Kit 3.4 – January 2019

* Added compatibility for IIS 8.5 and 10 environments.

## IIS Integration Kit 3.3.1 – June 2018

* Addressed compatibility issue with the 32-bit application pool.

## IIS Integration Kit 3.3 – December 2017

* Added the ability to use the `HttpOnly` flag on the session cookie. Learn more in the new `HttpOnlyCookie` attribute in the `pfisapi.conf` file.

* Added support for .NET Framework 4.0.

* Bug fixes.

## IIS Integration Kit 3.2 – June 2014

* Added support for allowlisting in the properties file for IIS (`pfisapi.conf`).

* Added units to the `TokenUpdateWindow` property in the `pfisapi.conf` file.

* Added documentation for the IIS limitation about HTTP POST issues with managed and native modules.

* Added support for IIS 8: Integrated Mode.

## IIS Integration Kit 3.1 – December 2012

* Added support for an exclusion resource list in the properties file for IIS (`pfisapi.conf`).

* Added support for version 2.5.1 of the OpenToken Adapter and OpenToken Agent.

## IIS Integration Kit 3.0 – October 2011

* Upgraded to .NET Framework 4.0.

* Requires IIS 7.0 or higher.

* Requires integrated pipeline mode for protected applications.

* Added support for both 32-and 64-bit application pool in IIS.

* Added the ability to control logging level.

* Replaced the ISAPI extension with OpenToken HTTP Module.

* Removed the OpenToken Exchange application.

* Fixed an issue that caused the TargetResource URL to truncate in certain situations.

* Fixed an issue with IIS crashing when the attribute data is too long.

## IIS Integration Kit 2.2 – September 2009

* Added the OpenToken Exchange service application to handle OpenToken query and POST transport methods.

* Added the `TokenUpdateWindow` property in the `pfisapi.conf` configuration file to enable browsers to reuse OpenTokens for a configurable period of time. This can optimize performance.

## IIS Integration Kit 2.1 – June 2009

* Added an alternative method for setting session attributes as HTTP headers without a prefix.

* Corrected OpenToken timestamp comparisons to prevent intermittent invalid OpenToken errors.

* Protected-resource URL filtering is no longer case-sensitive.

## IIS Integration Kit 2.0 – December 2008

* Ported the OpenToken IIS Agent to use the OpenToken Adapter and the OpenToken .NET library.

* Added support for the POST Transport Method from the OpenToken Adapter.

* Added support for URL filtering for protected resources.

* Added the ability to allow IIS web applications to download files.

## IIS Integration Kit 1.1 – September 2007

* Added a security patch to write all HTTP standard headers and PFTOKEN custom headers only. Any other HTTP custom headers will be removed.

* Simplified the IIS agent configuration file.

## IIS Integration Kit 1.0 – June 2007

* Initial Release

---

---
title: Configuring an OpenToken SP Adapter instance
description: Configure the OpenToken Adapter to determine how PingFederate communicates with your service provider application.
component: microsoft-iis
page_id: microsoft-iis:setup:pf_iis_ik_configuring_an_opentoken_sp_adapter_instance
canonical_url: https://docs.pingidentity.com/integrations/microsoft-iis/setup/pf_iis_ik_configuring_an_opentoken_sp_adapter_instance.html
llms_txt: https://docs.pingidentity.com/integrations/microsoft-iis/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 2, 2025
section_ids:
  steps: Steps
---

# Configuring an OpenToken SP Adapter instance

Configure the OpenToken Adapter to determine how PingFederate communicates with your service provider application.

## Steps

1. In the PingFederate admin console, go to **Authentication > Integration > IdP Adapters**. Click **Create new Instance**.

2. On the **Type** tab, set the basic adapter instance attributes.

   1. In the **Instance Name** field, enter a name for the adapter instance.

   2. In the **Instance ID** field, enter a unique identifier for the adapter instance.

   3. In the **Type** list, select **OpenToken Adapter**. Click **Next**.

3. On the **Instance Configuration** tab, configure the adapter instance by referring to [Configuring an OpenToken SP Adapter instance](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_config_opentoken_sp_adapt_instance.html) in the PingFederate documentation. Click **Next**.

   |   |                                                                                                                                                                                               |
   | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | If you use IIS to protect multiple sites on the same domain, in the OpenToken Adapter instance configuration, select **None** for SameSite Cookie, and select the **Secure Cookie** checkbox. |

4. Export the configuration file:

   1. On the **Actions** tab, click **Download**, then **Export**.

   2. Save the `agent-config.txt` file. Click **Next**.

5. On the **Extended Contract** tab, add any attributes you expect to retrieve other than the SAML subject. Click **Next**.

6. On the **Target App Info** tab, enter the basic information about your SP application. Click **Next**.

7. On the **Summary** tab, check and save your configuration. Click **Save**.

8. Create or update an identity provider (IdP) connection to use the OpenToken Adapter instance as shown in [Service provider SSO configuration](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_servic_provid_sso_config.html) in the PingFederate documentation.

---

---
title: Configuring the OpenToken IIS Agent to omit the HTTP header prefix
description: If your IIS web application cannot accept HTTP request headers with the standard OpenToken prefix, use this alternative method.
component: microsoft-iis
page_id: microsoft-iis:session_information_and_http_request_headers:pf_iis_ik_configuring_the_opentoken_iis_agent_to_omit_the_http_header_prefix
canonical_url: https://docs.pingidentity.com/integrations/microsoft-iis/session_information_and_http_request_headers/pf_iis_ik_configuring_the_opentoken_iis_agent_to_omit_the_http_header_prefix.html
llms_txt: https://docs.pingidentity.com/integrations/microsoft-iis/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 2, 2025
section_ids:
  steps: Steps
---

# Configuring the OpenToken IIS Agent to omit the HTTP header prefix

If your IIS web application cannot accept HTTP request headers with the standard OpenToken prefix, use this alternative method.

## Steps

1. In the OpenToken Adapter instance configuration, on the **Extended Contract** tab, include an attribute named `pf_attribute_list`.

2. In the identity provider (IdP) connection configuration, map the `pf_attribute_list` attribute as a text field that contains a comma-separated list of all the attributes in the adapter contract.

   Learn more in [Configuring IdP adapter contract fulfillment](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_configplugincontracttasklet_plugincontractfulfillmentmappingstate.html) in the PingFederate documentation.

   ![Example of IdP adapter contract fulfillment](_images/iis_contract_fulfillment_example.png)

---

---
title: Deploying and configuring the OpenToken IIS Agent
description: Deploy the OpenToken IIS Agent on your IIS server to allow it to communicate with PingFederate.
component: microsoft-iis
page_id: microsoft-iis:setup:pf_iis_ik_deploying_and_configuring_the_opentoken_iis_agent
canonical_url: https://docs.pingidentity.com/integrations/microsoft-iis/setup/pf_iis_ik_deploying_and_configuring_the_opentoken_iis_agent.html
llms_txt: https://docs.pingidentity.com/integrations/microsoft-iis/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 2, 2025
section_ids:
  steps: Steps
---

# Deploying and configuring the OpenToken IIS Agent

Deploy the OpenToken IIS Agent on your IIS server to allow it to communicate with PingFederate.

## Steps

1. If your IIS server is version 8 or later, add the IIS server role and role services:

   1. In **Server Manager**, on the **Manage** menu, click **Add Roles and Features**.

   2. In the **Add Roles and Features Wizard**, on the **Before You Begin** tab, click **Next**.

   3. On the **Installation Type** tab, select **Role-based or feature-based installation**. Click **Next**.

   4. On the **Server Selection** tab, select the IIS server. Click **Next**.

   5. On the **Server Roles** page, select **Web Server (IIS)**.

   6. On the **Features** tab, click **Next**.

   7. On the **Web Server Role (IIS) > Role Services** tab, in **Web Server > Application Development**, select **.NET 3.5 Extensibility** and **.NET 4.6 Extensibility**.

      Depending on your version of Windows, you might need to select **.NET 4.5 Extensibility** or **.NET 4.7 Extensibility**.

   8. If you receive a message that asks you to add features that are required for Web Server (IIS), click **Add Features**.

   9. Click **Next**.

   10. On the **Confirmation** tab, check that the configuration is correct. Click **Install**.

       |   |                                     |
       | - | ----------------------------------- |
       |   | This step can take several minutes. |

   11. Once the installation is complete, click **Close**.

2. Deploy the OpenToken IIS Agent:

   1. Extract the IIS Integration Kit distribution file on the IIS server, and then go to `dist/(x86)` or `dist/(x64)`.

   2. Run `setup.exe` to install the OpenToken HTTP Module into the Windows Global Assembly Cache.

   3. If your IIS server is version 7, register IIS with .NET Framework 4.0 by entering the following command at the Windows command prompt:

      `<Windows_install>\Microsoft.NET\Framework\v4.0.30319\aspnet_regiis-iru`

   4. Move the `agent-config.txt` that you exported in [Configuring an OpenToken SP Adapter instance](pf_iis_ik_configuring_an_opentoken_sp_adapter_instance.html) to `C:\Program Files\Ping Identity Corporation\OpenToken IIS Agent(n-bit)\conf` or your equivalent.

3. Configure the OpenToken IIS Agent properties file:

   1. Open `C:\Program Files\Ping Identity Corporation\OpenToken IIS Agent(n-bit)\conf\pfisapi.conf` for editing.

   2. Configure it to suit your environment based on the property descriptions in the file.

   3. If you use IIS to protect multiple sites on the same domain, set `SameSiteCookie=None` and `SecureCookie=YES`.

   4. Save the file.

   5. If you backed up a previous copy of the file in [Upgrading an existing deployment](pf_iis_ik_upgrading_an_existing_deployment.html), refer to that file to add new properties and restore your previous settings.

   6. Restart IIS.

      |   |                                                                                                                                                                                                                                               |
      | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      |   | You can test your configuration by deploying the sample application (`PFIsapiSample`) that is included in the installation. Learn more in `C:\Program Files\Ping Identity Corporation\OpenToken IIS Agent(n-bit)\samples` or your equivalent. |

---

---
title: Download manifest
description: The following files are included in the IIS Integration Kit .zip archive:
component: microsoft-iis
page_id: microsoft-iis:release_notes:pf_iis_ik_download_manifest
canonical_url: https://docs.pingidentity.com/integrations/microsoft-iis/release_notes/pf_iis_ik_download_manifest.html
llms_txt: https://docs.pingidentity.com/integrations/microsoft-iis/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 2, 2025
---

# Download manifest

The following files are included in the IIS Integration Kit `.zip` archive:

* `ReadMeFirst.pdf`: Contains links to this online documentation.

* `Legal.pdf`: Copyright and license information.

* `dist`: Contains the agent and supporting files that the adapter needs:

  * `x64`: Contains agent installation files for 64-bit Windows architecture:

    * `setup.exe`: Installation program for the OpenToken IIS Agent.

    * `Support Files.msi`: Installation supporting files for the OpenToken IIS Agent.

    * `conf`: Contains the configuration files.

    * `Module Retargetable Folder`: Contains IIS agent configuration data and a sample application.

    * `Global Assembly Cache Folder`: Contains IIS agent DLLs.

  * `x86`: Contains agent installation files for 32-bit Windows architecture:

    * `setup.exe`: Installation program for the PingFederate OpenToken IIS Agent.

    * `Supporting Files.msi`: Installation supporting files for the OpenToken IIS Agent.

    * `conf`: Contains configuration files.

    * `Module Retargetable Folder`: Contains IIS agent configuration data and a sample application.

    * `Global Assembly Cache Folder`: Contains IIS agent DLLs.

|   |                                                                                                                                                                                                                                                     |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | This integration requires the latest version of the OpenToken Adapter, which is distributed separately as part of the Java Integration Kit. Learn more in [Updating the OpenToken Adapter](../setup/pf_iis_ik_updating_the_opentoken_adapter.html). |

---

---
title: Internet Information Services (IIS) Integration Kit
description: The IIS Integration Kit allows PingFederate to coordinate user authentication and single sign-on (SSO) between an IIS web application and an identity provider (IdP).
component: microsoft-iis
page_id: microsoft-iis::pf_iis_ik
canonical_url: https://docs.pingidentity.com/integrations/microsoft-iis/pf_iis_ik.html
llms_txt: https://docs.pingidentity.com/integrations/microsoft-iis/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 2, 2025
section_ids:
  components: Components
  intended-audience: Intended audience
  system-requirements: System requirements
---

# Internet Information Services (IIS) Integration Kit

The IIS Integration Kit allows PingFederate to coordinate user authentication and single sign-on (SSO) between an IIS web application and an identity provider (IdP).

|   |                                                                                                                                                                                                                                                           |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | For new integrations, try the [Agentless Integration Kit](../agentless/pf_agentless_ik.html). It can integrate with a variety of platforms using a modern RESTful approach, and it doesn't require you to integrate agent software into your application. |

## Components

* OpenToken Adapter

  Installed in PingFederate, this adapter uses the secure OpenToken standard to pass user attributes and session information from PingFederate to the OpenToken IIS Module on the IIS server.

* OpenToken IIS Agent

  Installed on the server running IIS, this program watches for protected resource requests and determines whether to grant access or redirect the user to PingFederate for authentication with an IdP.

* OpenToken HTTP Module

  Installed in IIS, this module reads OpenToken payloads from PingFederate that contain user attributes and session information.

## Intended audience

This document is intended for PingFederate administrators and web application developers.

If you need help during the setup process, see the following sections of the PingFederate documentation:

* [Managing SP adapters](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_adaptermanagementtasklet_spadaptermanagementstate.html)

* [Configuring an OpenToken SP Adapter instance](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_config_opentoken_sp_adapt_instance.html)

## System requirements

* PingFederate 9.0 or later

* IIS 7.0 or later using Integrated Mode

* ASP .NET application with .NET Framework 4.0

---

---
title: Known issues and limitations
description: The following are known issues or limitations for the IIS Integration Kit.
component: microsoft-iis
page_id: microsoft-iis:release_notes:pf_iis_ik_known_issues_and_limitations
canonical_url: https://docs.pingidentity.com/integrations/microsoft-iis/release_notes/pf_iis_ik_known_issues_and_limitations.html
llms_txt: https://docs.pingidentity.com/integrations/microsoft-iis/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 2, 2025
section_ids:
  known-issues: Known issues
  known-limitations: Known limitations
---

# Known issues and limitations

The following are known issues or limitations for the IIS Integration Kit.

## Known issues

There are no known issues.

## Known limitations

* If IIS has been previously installed and then uninstalled, the installer doesn't recognize IIS 7.0 (or 7.5) as uninstalled, nor does it stop the installation.

* The IIS Integration Kit doesn't support newline characters (such as `\n` and `\r`) within attributes.

* When using Form POST as the transport mode in the SP OpenToken adapter, it might be necessary to add a trailing `/` into the URL to access the protected resources.

* The OpenToken name you specify in the adapter setup must be unique within the given federation, but the admin console doesn't enforce this.

* When using the installer to upgrade by uninstalling and reinstalling the agent, you must restart IIS after uninstall and before reinstall to ensure that old DLL's aren't used. You can reset IIS with the `resetiis /noforce` command.

* After uninstalling, you must remove any application mappings you set up manually. The uninstall script cannot remove these mappings.

* When using cookie as the OpenToken transport method, the domain configured in the adapter setup must match the domain configured in the `pfisapi.conf` file. If these don't match, you can end up with a persistent cookie. This is not enforced in the admin console.

* When using a non-session cookie as the OpenToken transport method, there isn't a session cookie configuration defined in the agent config file. Set the `SessionCookie` type in the `pfisapi.conf` file by removing the `#` and setting it to `YES` or `NO`.

* Classic managed pipeline mode isn't supported.

* Attempting to access the POST data of a request in a native module in IIS 7 after the data has been accessed by a managed module (such as the OpenToken Module) prevents the native module from accessing the data. This is a limitation of IIS 7.

  The issue also applies when using Query Parameter as the transport method. The only workaround for this issue is to use Cookie as the transport method

* The OpenToken Module can't be selected from the list of module types. Instead, enter it manually, as shown in [Adding the OpenToken HTTP Module in IIS](../setup/pf_iis_ik_adding_the_opentoken_http_module_in_iis.html).

* You can only add the OpenToken Module at the global server level. If you require implementation on a per-website basis, contact Ping Identity about [PingAccess](https://www.pingidentity.com/en/software/pingaccess.html).

---

---
title: Overview of the OpenToken IIS Agent
description: The OpenToken IIS Agent acts as a filter in front of an application or protected resource. The basic responsibilities of the agent are to filter requests to determine whether a request is for a protected resource:
component: microsoft-iis
page_id: microsoft-iis::pf_iis_ik_overview_of_the_opentoken_iis_agent
canonical_url: https://docs.pingidentity.com/integrations/microsoft-iis/pf_iis_ik_overview_of_the_opentoken_iis_agent.html
llms_txt: https://docs.pingidentity.com/integrations/microsoft-iis/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 2, 2025
---

# Overview of the OpenToken IIS Agent

The OpenToken IIS Agent acts as a filter in front of an application or protected resource. The basic responsibilities of the agent are to filter requests to determine whether a request is for a protected resource:

* If the request is for an unprotected resource, the agent passes the request to the application.

* If the request is for a protected resource, the agent checks to see if there's a PingFederate session available and if it meets the policy for the session.

* If a session exists and the session meets the policy for the request, then the agent passes the request back to the application.

* If a session doesn't exist, or if the existing session doesn't meet the session policy for that request, the agent redirects the user's browser through the PingFederate server to an Identity Provider (IdP) for authentication. After authentication, PingFederate redirects the user back to the protected resource with a valid session.

---

---
title: Overview of the SSO flow
description: With the IIS Integration Kit, PingFederate handles authentication requests to an identity provider (IdP) on behalf of IIS.
component: microsoft-iis
page_id: microsoft-iis::pf_iis_ik_overview_of_the_sso_flow
canonical_url: https://docs.pingidentity.com/integrations/microsoft-iis/pf_iis_ik_overview_of_the_sso_flow.html
llms_txt: https://docs.pingidentity.com/integrations/microsoft-iis/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 2, 2025
section_ids:
  description: Description
---

# Overview of the SSO flow

With the IIS Integration Kit, PingFederate handles authentication requests to an identity provider (IdP) *(tooltip: \<div class="paragraph">
\<p>A service that manages identity information and provides authentication services to relying clients or SPs within a federated or distributed network.\</p>
\</div>)* on behalf of IIS.

![Diagram of the SP-initiated SSO flow.](_images/iis_sso_flow_diagram.png)

The figure above illustrates an SP-initiated SSO scenario, showing the request flow and how the PingFederate OpenToken Adapter wraps attributes from an assertion into a secure OpenToken and passes it to IIS. You can find more information in [OpenToken Adapter](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_opentoken_adapt.html) in the PingFederate documentation.

## Description

1. A user attempts to access a resource on the IIS server protected by the OpenToken IIS Agent.

2. The user is redirected to the PingFederate server for authentication.

3. If an OpenToken session already exists, the user is granted immediate access.

4. The PingFederate server redirects the user's browser to an IdP for authentication using either the SAML or WS-Federation protocols. The IdP partner authenticates the user and returns a SAML assertion.

5. PingFederate validates the assertion and creates an OpenToken for the user including any configured attributes. PingFederate then redirects the browser, including the OpenToken, back to the OpenToken IIS Agent's OpenToken Exchange service, which converts the OpenToken into a cookie and redirects to the original resource.

6. The OpenToken IIS Agent verifies the OpenToken and grants access to the protected resource. The User ID and any attributes from the OpenToken are exposed to the resource as HTTP Request Headers.

---

---
title: Session information and HTTP request headers
description: The OpenToken IIS Agent uses HTTP request headers to provide session information and user attributes from the OpenToken Adapter to the protected application.
component: microsoft-iis
page_id: microsoft-iis:session_information_and_http_request_headers:pf_iis_ik_session_information_and_http_request_headers
canonical_url: https://docs.pingidentity.com/integrations/microsoft-iis/session_information_and_http_request_headers/pf_iis_ik_session_information_and_http_request_headers.html
llms_txt: https://docs.pingidentity.com/integrations/microsoft-iis/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 2, 2025
---

# Session information and HTTP request headers

The OpenToken IIS Agent uses HTTP request headers to provide session information and user attributes from the OpenToken Adapter to the protected application.

This allows the application to use the information to support various features, such as making authorization decisions or providing personalized content. The application has access to the following session and attribute information:

* Attributes from the OpenToken Adapter contract

  By default, these include the subject (`SUBJECT`) and attributes specified on the **Extended Contract** tab of the adapter instance configuration. Only the attributes fulfilled at runtime are available to the application. Attributes with a `NULL` value are not included in the OpenToken.

* `NOT-ON-OR-AFTER`

  The time the token expires.

* `RENEW-UNTIL`

  The time the session expires. Tokens can't be renewed past this time.

* `AUTH_NOT-BEFORE`

  The time the session began.

* `AUTHNCONTEXT`

  Information from the SAML assertion that describes how the user was authenticated by the identity provider (IdP). You can find a complete description in the authentication context section in [Terminology](https://docs.pingidentity.com/pingfederate/latest/introduction_to_pingfederate/pf_terminology.html) in the PingFederate documentation.

For security reasons, each HTTP request header is prepended with a specific (configurable) prefix. The OpenToken IIS Agent always removes and rewrites these prefixed request headers for each request.

If applications protected by the OpenToken IIS Agent can't be modified to accept headers with this prefix, you can [Configure the OpenToken IIS Agent to omit the HTTP header prefix](pf_iis_ik_configuring_the_opentoken_iis_agent_to_omit_the_http_header_prefix.html).

---

---
title: Updating the OpenToken Adapter
description: To get started with the integration, download the latest version of the OpenToken Adapter and deploy it to your PingFederate directory.
component: microsoft-iis
page_id: microsoft-iis:setup:pf_iis_ik_updating_the_opentoken_adapter
canonical_url: https://docs.pingidentity.com/integrations/microsoft-iis/setup/pf_iis_ik_updating_the_opentoken_adapter.html
llms_txt: https://docs.pingidentity.com/integrations/microsoft-iis/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 17, 2025
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Updating the OpenToken Adapter

To get started with the integration, download the latest version of the OpenToken Adapter and deploy it to your PingFederate directory.

## About this task

Although the OpenToken Adapter is included in PingFederate and the IIS Integration Kit, the latest version of the OpenToken Adapter is distributed separately as part of the Java Integration Kit. Follow these steps to make sure you have the latest version available.

## Steps

1. Download the Java Integration Kit `.zip` archive from the **Add-ons** tab of the [PingFederate downloads page](https://www.pingidentity.com/en/resources/downloads/pingfederate.html) or the [Ping Identity Marketplace](https://marketplace.pingone.com/item/java-integration-kit).

2. Stop PingFederate.

3. If you're upgrading an existing deployment, delete the following files from `<pf_install>/pingfederate/server/default/deploy`:

   * `opentoken-adapter-<version>.jar`

   * `opentoken-java-<version>.jar`

4. In the `.zip` archive, copy `dist/opentoken-adapter-<version>.jar` to `<pf_install>/pingfederate/server/default/deploy`.

5. Start PingFederate.

6. If you operate PingFederate in a cluster, repeat steps 2 - 5 for each engine node.

---

---
title: Upgrading an existing deployment
description: If you're updating an existing deployment of the IIS Integration Kit, back up your configuration and remove the previous agent before deploying the latest version.
component: microsoft-iis
page_id: microsoft-iis:setup:pf_iis_ik_upgrading_an_existing_deployment
canonical_url: https://docs.pingidentity.com/integrations/microsoft-iis/setup/pf_iis_ik_upgrading_an_existing_deployment.html
llms_txt: https://docs.pingidentity.com/integrations/microsoft-iis/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 2, 2025
section_ids:
  steps: Steps
---

# Upgrading an existing deployment

If you're updating an existing deployment of the IIS Integration Kit, back up your configuration and remove the previous agent before deploying the latest version.

## Steps

1. Update the OpenToken Adapter in PingFederate as shown in [Updating the OpenToken Adapter](pf_iis_ik_updating_the_opentoken_adapter.html).

2. Back up your existing `C:\Program Files\Ping Identity Corporation\OpenToken IIS Agent(x-bit)\conf\pfisapi.conf` file to a safe location.

   Refer to this copy when you complete the [Deploying and configuring the OpenToken IIS Agent](pf_iis_ik_deploying_and_configuring_the_opentoken_iis_agent.html) step.

3. If you're upgrading from a previous deployment, open your backup copy of `pfisapi.conf` for editing. Add the following sections:

   |   |                                                                                                                                                                          |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
   |   | The `pfisapi.conf` file included in the latest IIS Integration Kit `.zip` archive shows the placement of these parameters and includes the most up to date descriptions. |

   ```
   #--------------
   # Basic Options
   #--------------

   # (OPTIONAL) List of protected absolute URIs. Multiple patterns can be used.
   # with a separator '|'. Regular expressions are allowed.
   # This overrides values entered in ProtectedResourceList
   # The default value is blank.
   ProtectedUriList=

   # (OPTIONAL) List of excluded absolute URIs. Multiple patterns can be used.
   # with a separator '|'. Regular expressions allowed.
   # This will override any values entered in ExcludeList.
   # The default value is blank.
   ExcludeUriList=

   # (OPTIONAL) Lifetime of the OpenToken cookie in seconds.
   # If set to -1, the token-lifetime in the agent-config.txt file is used.
   # Any other value overrides the token-lifetime in in the agent-config.txt file.
   # The default value is -1.
   CookieAge=-1

   # (Required)
   # The SameSite cookie attribute is set to this value.
   # The allowed values for this setting are: Strict, Lax, None, and Nothing
   # The "Strict", "Lax", and "None" value changes the SameSite cookie attribute setting.
   # The "Nothing" value leaves the SameSite cookie attribute unset in the OpenToken Session Cookie.
   # For the "None" value, you must use secure attributes because cross-site cookies can only be accessed over HTTPS connections.
   # If the cookie is not secure and the "None" value is selected, the SameSite cookie attribute will not be set.
   # The default value is Nothing.
   SameSiteCookie=Nothing

   #-----------------
   # Advanced Options
   #-----------------

   # (OPTIONAL) Determines whether the cookie will be a session cookie or a persistent cookie.
   # Setting to YES will result in SessionCookie. This overrides the value in the agent-config.txt file.
   # Possible values are 'YES' and 'NO'.
   # The default value is blank.
   # SessionCookie=
   ```

4. Set values for any new parameters. Save the file.

5. Stop IIS.

6. Remove the existing OpenToken HTTP Module from IIS.

   1. In the Internet Information Services (IIS) Manager, select the IIS server.

   2. On the **Features View** tab, double-click **Modules**.

   3. On the **Modules** tab, select the OpenToken HTTP Module.

   4. In the **Actions** area, click **Remove**.

7. In the Windows Control Panel, uninstall the **OpenToken IIS Agent** program.

8. Start IIS.