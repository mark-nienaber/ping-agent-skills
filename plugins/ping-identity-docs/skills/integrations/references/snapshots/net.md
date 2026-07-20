---
title: .NET Integration Kit
description: The latest .NET Integration Kit supports .NET 8.0 and later, providing compatibility for PingFederate OpenToken-based integration with .NET 8-based IdP and SP applications.
component: net
page_id: net::pf_net_ik_versions
canonical_url: https://docs.pingidentity.com/integrations/net/pf_net_ik_versions.html
llms_txt: https://docs.pingidentity.com/integrations/net/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 8, 2026
section_ids:
  net-integration-kit-latest: .NET Integration Kit (latest)
  net-integration-kit-2-5: .NET Integration Kit 2.5
---

# .NET Integration Kit

## .NET Integration Kit (latest)

The latest .NET Integration Kit supports .NET 8.0 and later, providing compatibility for PingFederate OpenToken-based integration with .NET 8-based IdP and SP applications.

## .NET Integration Kit 2.5

This documentation is available for existing deployments of the .NET Integration 2.x. This version targets the .NET framework 4.0 runtime and won't be supported in future releases.

---

---
title: .NET Integration Kit 2.5
description: The .NET Integration Kit allows PingFederate to communicate user attributes with .NET-based web applications.
component: net
page_id: net:net-2x:pf_net_2x_ik
canonical_url: https://docs.pingidentity.com/integrations/net/net-2x/pf_net_2x_ik.html
llms_txt: https://docs.pingidentity.com/integrations/net/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 20, 2024
section_ids:
  components: Components
  intended-audience: Intended audience
  system-requirements: System requirements
---

# .NET Integration Kit 2.5

The .NET Integration Kit allows PingFederate to communicate user attributes with .NET-based web applications.

When PingFederate is serving an identity provider (IdP) role, it can receive user attributes from a .NET IdP application. When PingFederate is serving a service provider (SP) role, it can send user attributes to a .NET SP application.

|   |                                                                                                                                                                                                            |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | For new integrations, we encourage you to consider the [Agentless Integration Kit](../../agentless/pf_agentless_ik.html), which can integrate with a variety of platforms using a modern RESTful approach. |

## Components

* OpenToken Adapter

  * An adapter that allows PingFederate to send or receive user attributes in the OpenToken format. See [OpenToken Adapter](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_opentoken_adapt.html) in the PingFederate documentation.

* OpenToken Agent

  * An agent that runs within your .NET application that allows it to send or receive user attributes in the OpenToken format.

* Sample application

  * The Integration Kit distribution also contains sample IdP and SP applications. The applications may be installed quickly for testing OpenToken processing and to provide a working demonstration of end-to-end single sign-on (SSO) and single logout (SLO). Source code and supporting files are included in the distribution and may be modified or used as a reference for application developers.

## Intended audience

This document is intended for PingFederate administrators and web-application developers.

Before you start, you should be familiar with the following parts of the PingFederate documentation:

* [Managing IdP adapters](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_managing_idp_adapters.html)

* [Managing SP adapters](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_adaptermanagementtasklet_spadaptermanagementstate.html)

* [OpenToken Adapter](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_opentoken_adapt.html)

## System requirements

* PingFederate 9.0 or later.

* Microsoft .NET Framework 4.0 for the agent application.

---

---
title: .NET Integration Kit 3.0
description: The .NET Integration Kit allows PingFederate to communicate user attributes with ASP.NET Core 8-based applications.
component: net
page_id: net:net:pf_net_ik
canonical_url: https://docs.pingidentity.com/integrations/net/net/pf_net_ik.html
llms_txt: https://docs.pingidentity.com/integrations/net/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 24, 2026
section_ids:
  components: Components
  intended-audience: Intended audience
  system-requirements: System requirements
---

# .NET Integration Kit 3.0

The .NET Integration Kit allows PingFederate to communicate user attributes with ASP.NET Core 8-based applications.

When PingFederate is serving an identity provider (IdP) *(tooltip: \<div class="paragraph">
\<p>A service that manages identity information and provides authentication services to relying clients or SPs within a federated or distributed network.\</p>
\</div>)* role, it receives user attributes from a .NET 8 IdP application. When PingFederate is serving a service provider (SP) *(tooltip: \<div class="paragraph">
\<p>In SAML, an entity that receives and accepts an authentication assertion issued by an IdP, typically for the purpose of allowing access to a protected resource.\</p>
\</div>)* role, it sends user attributes to a .NET 8 SP application.

|   |                                                                                                                                                                                                                              |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | For new integrations, consider using the [Agentless Integration Kit](../../agentless/pf_agentless_ik.html) instead. The Agentless Integration Kit can integrate with a variety of platforms using a modern RESTful approach. |

## Components

| Component           | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| ------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| OpenToken Adapter   | An adapter that allows PingFederate to send or receive user attributes in the OpenToken format. Learn more in [OpenToken Adapter](http://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_opentoken_adapt.html) in the PingFederate documentation.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| OpenToken Agent     | An agent that runs within your ASP.NET Core 8 application providing classes for reading, writing, and deleting OpenToken                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Sample applications | Two sample applications are included to demonstrate end-to-end single sign-on (SSO) *(tooltip: \<div class="paragraph">&#xA;\<p>The process of authenticating an identity (signing on) at one website (usually with a user ID and password) and then accessing resources secured by other domains without reauthenticating.\</p>&#xA;\</div>)* and single logout (SLO) *(tooltip: \<div class="paragraph">&#xA;\<p>The process of signing a user out of multiple sites where the user has started a SSO session.\</p>&#xA;\</div>)*, and to serve as a reference for application developers:- An IdP sample application that authenticates users locally and issues an OpenToken to PingFederate's IdP adapter endpoint.

- An SP sample application that receives an OpenToken from PingFederate's SP adapter, validates it, and establishes a user session.Both applications can be deployed quickly for testing OpenToken processing. Source code and supporting files are included in the distribution and can be modified or used as a starting point for your own implementation. |

## Intended audience

This document is intended for PingFederate administrators and web-application developers.

Before you start, you should be familiar with the following parts of the PingFederate documentation:

* [Managing IdP adapters](http://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_managing_idp_adapters.html)

* [Managing SP adapters](http://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_adaptermanagementtasklet_spadaptermanagementstate.html)

* [OpenToken Adapter](http://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_opentoken_adapt.html)

## System requirements

* PingFederate 11.3 or later.

* Microsoft .NET SDK 8.0 or later.

---

---
title: Changelog
description: Added support for .NET 8
component: net
page_id: net:net:release_notes/pf_net_ik_changelog
canonical_url: https://docs.pingidentity.com/integrations/net/net/release_notes/pf_net_ik_changelog.html
llms_txt: https://docs.pingidentity.com/integrations/net/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 1, 2026
section_ids:
  net-integration-kit-3-0-jun-2026: .NET Integration Kit 3.0 - Jun 2026
  net-integration-kit-2-5-4-march-2020: .NET Integration Kit 2.5.4 – March 2020
  net-integration-kit-2-5-3-september-2019: .NET Integration Kit 2.5.3 – September 2019
  net-integration-kit-2-5-2-january-2016: .NET Integration Kit 2.5.2 – January 2016
  net-integration-kit-2-5-1-december-2012: .NET Integration Kit 2.5.1 – December 2012
  net-integration-kit-2-5-june-2012: .NET Integration Kit 2.5 – June 2012
  net-integration-kit-2-4-march-2010: .NET Integration Kit 2.4 – March 2010
  net-integration-kit-2-3-november-2008: .NET Integration Kit 2.3 – November 2008
  net-integration-kit-2-2-june-2008: .NET Integration Kit 2.2 – June 2008
  net-integration-kit-2-1-april-2008: .NET Integration Kit 2.1 – April 2008
  net-integration-kit-2-0-december-2007: .NET Integration Kit 2.0 – December 2007
  net-integration-kit-1-2-1-august-2007: .NET Integration Kit 1.2.1 – August 2007
  net-integration-kit-1-2-may-2007: .NET Integration Kit 1.2 – May 2007
---

# Changelog

## .NET Integration Kit 3.0 - Jun 2026

* Added support for .NET 8

## .NET Integration Kit 2.5.4 – March 2020

* Added support for the SameSite cookie flag in web browsers

## .NET Integration Kit 2.5.3 – September 2019

* Updated the included OpenToken Adapter to version 2.5.8

* Updated the included OpenToken Agent to version 2.5.3

* Improved the way token timestamps are handled

## .NET Integration Kit 2.5.2 – January 2016

* Updated sample application data archive

* Updated OpenToken Adapter to version 2.5.7

## .NET Integration Kit 2.5.1 – December 2012

* Updated to address security issue found since the previous release

* Added support for OpenToken 2.5.1 Adapter and the OpenToken 2.5.1 Agent

## .NET Integration Kit 2.5 – June 2012

* Added support for the Microsoft .NET Framework 4.0

* Added support for 64-bit CPUs

* Removed support of the Microsoft .NET Framework 2.0

## .NET Integration Kit 2.4 – March 2010

* Added token Replay Prevention to the OpenToken IdP Adapter Advanced Settings

## .NET Integration Kit 2.3 – November 2008

* Added POST Transport Method for OpenToken when used by a Service Provider

* Added configuration to specify session cookie vs. persistent cookie

* Added option to set the "`Secure`" attribute on an OpenToken when cookie is used

* Added ability to bypass password obfuscation and strength enforcement for backward compatibility with previous .NET OpenToken agents

* Correctly handles `null` parameters for SOAP SLO

* Empty query string (`?`) isn't automatically appended to the URL when redirecting to TargetResource

* TargetResource URL is URL encoded

* Corrected `not-before tolerance processing`

## .NET Integration Kit 2.2 – June 2008

* Added support for SAML 2.0 `isPassive` and `ForceAuthn`

* Enforced UTF-8 encoding within OpenToken

* Symmetric key in the OpenToken agent configuration file is encrypted

* Combined the OpenToken adapter and OpenToken Java library jar files into a single adapter file for easier deployment to PingFederate

## .NET Integration Kit 2.1 – April 2008

* Added `AgentConfiguration` class to simplify Agent instantiation

* Added Agent Toolkit API HTML Help file

## .NET Integration Kit 2.0 – December 2007

Modified to use an open-standard, secure token called OpenToken to pass user information between an application and PingFederate. The OpenToken is passed through the user's browser as a URL query parameter or an HTTP cookie. The data within the OpenToken is a set of key-value pairs, and the data is encrypted using common encryption algorithms.

## .NET Integration Kit 1.2.1 – August 2007

* Fixed buffer overflow issue in OpenToken Agent to allow dynamic buffer size for reading `PFTOKEN`

* OpenToken Agent `extractFromRequest` method corrected to only delete cookie if the `PFTOKEN` transport is cookie

* OpenToken Agent no longer writes messages to the Windows Event Log

* Modified to allow backward compatibility of the Standard Adapter 1.2.1 with PingFederate 4.0

* Bundled .NET sample application with distribution

## .NET Integration Kit 1.2 – May 2007

* Added an option to encode `PFTOKEN` for handling special characters

* Added an additional constructor to allow `PFTOKEN` to use default properties for all configuration options except password, holder name, and max age

* Added `PFTOKEN` time stamp information in the log file

---

---
title: Changelog
description: .NET Integration Kit 2.5.4 – March 2020
component: net
page_id: net:net-2x:release_notes/pf_net_ik_changelog
canonical_url: https://docs.pingidentity.com/integrations/net/net-2x/release_notes/pf_net_ik_changelog.html
llms_txt: https://docs.pingidentity.com/integrations/net/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 20, 2024
---

# Changelog

**.NET Integration Kit 2.5.4 – March 2020**

* Added support for the SameSite cookie flag in web browsers.

**.NET Integration Kit 2.5.3 – September 2019**

* Updated the included OpenToken Adapter to version 2.5.8.

* Updated the included OpenToken Agent to version 2.5.3.

* Improved the way token timestamps are handled.

**.NET Integration Kit 2.5.2 – January 2016**

* Updated sample application data archive.

* Updated OpenToken Adapter to version 2.5.7.

**.NET Integration Kit 2.5.1 – December 2012**

* Updated to address security issue found since the previous release

* Added support for OpenToken 2.5.1 Adapter and the OpenToken 2.5.1 Agent

**.NET Integration Kit 2.5 – June 2012**

* Added support for the Microsoft .NET Framework 4.0

* Added support for 64-bit CPUs

* Removed support of the Microsoft .NET Framework 2.0

**.NET Integration Kit 2.4 – March 2010**

* Added token Replay Prevention to the OpenToken IdP Adapter Advanced Settings

**.NET Integration Kit 2.3 – November 2008**

* Added POST Transport Method for OpenToken when used by a Service Provider

* Added configuration to specify session cookie vs. persistent cookie

* Added option to set the "`Secure`" attribute on an OpenToken when cookie is used

* Added ability to bypass password obfuscation and strength enforcement for backward compatibility with previous .NET OpenToken agents

* Correctly handles `null` parameters for SOAP SLO

* Empty query string (`?`) is not automatically appended to the URL when redirecting to TargetResource

* TargetResource URL is URL encoded

* Corrected `not-before tolerance processing`

**.NET Integration Kit 2.2 – June 2008**

* Added support for SAML 2.0 `isPassive` and `ForceAuthn`

* Enforced UTF-8 encoding within OpenToken

* Symmetric key in the OpenToken agent configuration file is encrypted

* Combined the OpenToken adapter and OpenToken Java library jar files into a single adapter file for easier deployment to PingFederate

**.NET Integration Kit 2.1 – April 2008**

* Added `AgentConfiguration` class to simplify Agent instantiation

* Added Agent Toolkit API HTML Help file

**.NET Integration Kit 2.0 – December 2007**

Modified to use an open-standard, secure token called OpenToken to pass user information between an application and PingFederate. The OpenToken is passed through the user's browser as a URL query parameter or an HTTP cookie. The data within the OpenToken is a set of key/value pairs, and the data is encrypted using common encryption algorithms.

**.NET Integration Kit 1.2.1 – August 2007**

* Fixed buffer overflow issue in OpenToken Agent to allow dynamic buffer size for reading `PFTOKEN`

* OpenToken Agent `extractFromRequest` method corrected to only delete cookie if the `PFTOKEN` transport is cookie

* OpenToken Agent no longer writes messages to the Windows Event Log

* Modified to allow backward compatibility of the Standard Adapter 1.2.1 with PingFederate 4.0

* Bundled .NET sample application with distribution

**.NET Integration Kit 1.2 – May 2007**

* Added an option to encode `PFTOKEN` for handling special characters

* Added an additional constructor to allow `PFTOKEN` to use default properties for all configuration options except password, holder name, and max age

* Added `PFTOKEN` time stamp information in the log file

---

---
title: Configuring an OpenToken IdP Adapter instance
description: Configure the OpenToken Adapter to determine how PingFederate communicates with your identity provider (IdP) application.
component: net
page_id: net:net:setup/pf_net_ik_configuring_opentoken_idp_adapter_instance
canonical_url: https://docs.pingidentity.com/integrations/net/net/setup/pf_net_ik_configuring_opentoken_idp_adapter_instance.html
llms_txt: https://docs.pingidentity.com/integrations/net/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 26, 2026
section_ids:
  steps: Steps
---

# Configuring an OpenToken IdP Adapter instance

Configure the OpenToken Adapter to determine how PingFederate communicates with your identity provider (IdP) *(tooltip: \<div class="paragraph">
\<p>A service that manages identity information and provides authentication services to relying clients or SPs within a federated or distributed network.\</p>
\</div>)* application.

## Steps

1. In the PingFederate admin console, go to **Authentication > Integration > IdP Adapters**.

2. Click **Create New Instance**.

3. On the **Type** tab, set the basic adapter instance attributes.

   1. In the **Instance Name** field, enter a name for the adapter instance.

   2. In the **Instance ID** field, enter a unique name for the adapter instance.

   3. In the **Type** list, select **OpenToken IdP Adapter**.

   4. Click **Next**.

4. On the **Instance Configuration** tab, configure the adapter instance.

   Learn more in [Configuring an OpenToken IdP Adapter instance](http://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_configuring_opentoken_idp_adapter_instance.html) in the PingFederate documentation.

5. Click **Next**.

6. Export the configuration file:

   1. On the **Actions** tab, click **Download**, and then click **Export**.

   2. Save the `agent-config.txt` file.

   3. Click **Next**.

7. On the **Extended Contract** tab, configure additional attributes as needed.

8. Click **Next**.

9. On the **Summary** tab, review your configuration and click **Save**.

10. Create or update a service provider (SP) *(tooltip: \<div class="paragraph">
    \<p>In SAML, an entity that receives and accepts an authentication assertion issued by an IdP, typically for the purpose of allowing access to a protected resource.\</p>
    \</div>)* connection to use the OpenToken Adapter instance.

    Learn more in the [Identity Provider SSO configuration](http://docs.pingidentity.com/pingfederate/13.0/administrators_reference_guide/pf_ident_provid_sso_config.html) in the PingFederate documentation.

---

---
title: Configuring an OpenToken SP Adapter instance
description: Configure the OpenToken Adapter to determine how PingFederate communicates with your service provider application.
component: net
page_id: net:net:setup/pf_net_ik_configuring_opentoken_sp_adapter_instance
canonical_url: https://docs.pingidentity.com/integrations/net/net/setup/pf_net_ik_configuring_opentoken_sp_adapter_instance.html
llms_txt: https://docs.pingidentity.com/integrations/net/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 20, 2024
section_ids:
  steps: Steps
---

# Configuring an OpenToken SP Adapter instance

Configure the OpenToken Adapter to determine how PingFederate communicates with your service provider application.

## Steps

1. In the PingFederate administrative console, go to **Application > Integration > SP Adapters**.

2. Click **Create new Instance**.

3. On the **Type** tab, set the basic adapter instance attributes.

   1. In the **Instance Name** field, enter a name for the adapter instance.

   2. In the **Instance ID** field, enter a unique identifier for the adapter instance.

   3. From the **Type** list, select **OpenToken Adapter**.

   4. Click **Next**.

4. On the **Instance Configuration** tab, configure the adapter instance.

   Learn more in [Configuring an OpenToken SP Adapter instance](http://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_config_opentoken_sp_adapt_instance.html) in the PingFederate documentation.

   |   |                                                                                                                                                                                                 |
   | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | If you use .NET to protect multiple sites on the same domain, in the OpenToken Adapter instance configuration, select **None** for SameSite Cookie, and select the **Secure Cookie** check box. |

   1. Click **Next**.

5. Export the configuration file:

   1. On the **Actions** tab, click **Download**, and then click **Export**.

   2. Save `agent-config.txt`.

   3. Click **Next**.

6. On the **Extended Contract** tab, add any attributes that you expect to retrieve other than the SAML subject.

   1. Click **Next**.

7. On the **Target App Info** tab, enter the basic information about your SP application.

   1. Click **Next**.

8. On the **Summary** tab, check and save your configuration.

   1. Click **Save**.

9. Create or update an identity provider (IdP) *(tooltip: \<div class="paragraph">
   \<p>A service that manages identity information and provides authentication services to relying clients or SPs within a federated or distributed network.\</p>
   \</div>)* connection to use the OpenToken Adapter instance as shown in [Service provider SSO configuration](http://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_servic_provid_sso_config.html) in the PingFederate documentation.

---

---
title: Configuring an OpenToken SP Adapter instance
description: Configure the OpenToken Adapter to determine how PingFederate communicates with your service provider application.
component: net
page_id: net:net-2x:setup/pf_net_ik_configuring_an_opentoken_sp_adapter_instance
canonical_url: https://docs.pingidentity.com/integrations/net/net-2x/setup/pf_net_ik_configuring_an_opentoken_sp_adapter_instance.html
llms_txt: https://docs.pingidentity.com/integrations/net/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 20, 2024
section_ids:
  steps: Steps
---

# Configuring an OpenToken SP Adapter instance

Configure the OpenToken Adapter to determine how PingFederate communicates with your service provider application.

## Steps

1. In the PingFederate administrative console, go to **Authentication > Integration > IdP Adapters**. Click Create new Instance.

2. On the Type tab, set the basic adapter instance attributes.

   1. In the Instance Name field, enter a name for the adapter instance.

   2. In the Instance ID field, enter a unique identifier for the adapter instance.

   3. From the Type list, select OpenToken Adapter. Click Next.

3. On the Instance Configuration tab, configure the adapter instance by referring to [Configuring an OpenToken SP Adapter instance](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_config_opentoken_sp_adapt_instance.html) in the PingFederate documentation. Click Next.

   |   |                                                                                                                                                                                         |
   | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | If you use .NET to protect multiple sites on the same domain, in the OpenToken Adapter instance configuration, select None for SameSite Cookie, and select the Secure Cookie check box. |

4. Export the configuration file:

   1. On the Actions tab, click Download, and then click Export.

   2. Save `agent-config.txt`. Click Next.

5. On the Extended Contract tab, add any attributes that you expect to retrieve other than the SAML subject. Click Next.

6. On the Target App Info tab, enter the basic information about your SP application. Click Next.

7. On the Summary tab, check and save your configuration. Click Save.

8. Create or update an identity provider (IdP) connection to use the OpenToken Adapter instance as shown in [Service provider SSO configuration](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_servic_provid_sso_config.html) in the PingFederate documentation.

---

---
title: Configuring IIS to use the sample applications
description: To see a working demonstration of the .NET Integration Kit, deploy the sample applications and configure your Internet Information Services (IIS) server.
component: net
page_id: net:net:setup/pf_net_ik_configuring_iis_sample_applications
canonical_url: https://docs.pingidentity.com/integrations/net/net/setup/pf_net_ik_configuring_iis_sample_applications.html
llms_txt: https://docs.pingidentity.com/integrations/net/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 29, 2026
page_aliases: ["pf_net_ik_configuring_iis_to_use_the_sample_applications.adoc"]
section_ids:
  before-you-begin: Before you begin
  setting-up-samples-as-applications-within-a-site: Setting up samples as applications within a site
---

# Configuring IIS to use the sample applications

To see a working demonstration of the .NET Integration Kit, deploy the sample applications and configure your Internet Information Services (IIS) server.

## Before you begin

* Windows Server 2016 or later with IIS 10.0+

* [.NET 8 Hosting Bundle](https://dotnet.microsoft.com/en-us/download/dotnet/8.0) installed on the IIS server (choose Hosting Bundle, not the runtime or SDK alone)

* An existing IIS website with an HTTPS binding to deploy the applications under

|   |                                                                                                                                                                         |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Install the .NET 8 Hosting Bundle after IIS. If IIS was installed after the Hosting Bundle, run the Hosting Bundle installer again to register the ASP.NET Core Module. |

## Setting up samples as applications within a site

1. Install the .NET 8 Hosting Bundle.

2. From the .NET Integration Kit `.zip` archive, copy the `sample/IdpSample` and `sample/SpSample` directories to your IIS server, such as `C:\inetpub\wwwroot`.

3. Create application pools.

   Each application requires its own application pool set to `No Managed Code`.

   1. Open IIS Manager.

   2. Click **Application Pools > Add Application Pool**.

   3. For the IdP application:

      |                           |                   |
      | ------------------------- | ----------------- |
      | **Name**                  | `IdpSamplePool`   |
      | **.NET CLR Version**      | `No Managed Code` |
      | **Managed pipeline mode** | `Integrated`      |

   4. For the SP application:

      |                           |                   |
      | ------------------------- | ----------------- |
      | **Name**                  | `SpSamplePool`    |
      | **.NET CLR Version**      | `No Managed Code` |
      | **Managed pipeline mode** | `Integrated`      |

4. Add the applications under the existing website.

   In IIS Manager, expand **Sites** and select the website under which you want to host the applications.

   1. Right-click the website and choose **Add Application**.

   2. For the IdP application:

      |                      |                                        |
      | -------------------- | -------------------------------------- |
      | **Alias**            | `IdpSample`                            |
      | **Application pool** | `IdpSamplePool`                        |
      | **Physical path**    | `C:\inetpub\wwwroot\IdpSample\publish` |

   3. For the SP application:

      |                      |                                       |
      | -------------------- | ------------------------------------- |
      | **Alias**            | `SpSample`                            |
      | **Application pool** | `SpSamplePool`                        |
      | **Physical path**    | `C:\inetpub\wwwroot\SpSample\publish` |

      The applications will be accessible at:

      IdP: https\://\<your-site>/IdpSample

      SP: https\://\<your-site>/SpSample

5. Configure permissions.

   The application pool identity must have read access to the publish directory and write access to the logs and config directories.

   1. Right-click **C:\inetpub\wwwroot\IdpSample\publish > Security > Edit > Add**

   2. Enter `IIS AppPool\IdpSamplePool`.

   3. Click **Check Names > OK > Read & Execute > OK**

   4. Repeat steps a - c on `C:\inetpub\wwwroot\IdpSample\publish\wwwroot\config`. Select **Modify** instead of **Read & Execute**.

      If application-level logging is enabled through `web.config` and `appsettings.json`, ensure the logs directory has Modify permission granted to the application pool identity.

   5. Repeat steps a - c on `C:\inetpub\wwwroot\SpSample\publish` using IIS `AppPool\SpSamplePool`.

   6. Repeat step d on `C:\inetpub\wwwroot\SpSample\publish\wwwroot\config` using IIS `AppPool\SpSamplePool`.

6. Verify the deployment.

   1. Go to https\://\<your-site>/IdpSample.

      The IdP application landing page should load.

   2. Go to https\://\<your-site>/SpSample.

      The SP application landing page should load.

7. If needed, go to https\://\<yoursite>/IdpSample/Config to review or update the following fields:

   | Field                        | Default                      | Description                                                                                                                                |
   | ---------------------------- | ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
   | **PingFederate Base URL**    | `https://localhost:9031/`    | Update if PingFederate is running on a different host or port.                                                                             |
   | **SP Connections**           | `localhost:default:entityId` | Update if your SP connection entity ID differs.                                                                                            |
   | **IdP Adapter Instances**    | `OTIdPJava`                  | Update if you used a different adapter instance ID.                                                                                        |
   | **Attribute Names List**     | `authnContext\|email\|role`  | Update to match the attributes configured in your IdP adapter's extended contract.                                                         |
   | **Agent Configuration File** | N/A                          | Upload a replacement `agent-config.txt` if you downloaded a new one from PingFederate after changing the adapter password or cipher suite. |

   1. Click **Save**.

8. If needed, go to https\://\<yoursite>/SpSample/Config to review or update the following fields:

   | Field                        | Default                                                                                                                                    |
   | ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
   | **PingFederate Base URL**    | `https://localhost:9031/`                                                                                                                  |
   | **IdP Connections**          | `localhost:default:entityId`                                                                                                               |
   | **SP Adapter Instances**     | `OTSPJava`                                                                                                                                 |
   | **Attribute Names List**     | `authnContext\|email\|role`                                                                                                                |
   | **Agent Configuration File** | Upload a replacement `agent-config.txt` if you downloaded a new one from PingFederate after changing the adapter password or cipher suite. |

9. Ensure the PingFederate configuration is updated to match the domain of Sample App deployed within IIS.

   1. For example, the **Authentication Service** field for the OpenToken IdP Adapter should be set to `https://localhost/IdpSample/Login`.

---

---
title: Configuring IIS to use the sample applications
description: To see a working demonstration of the .NET Integration Kit, deploy the sample applications and configure your Internet Information Services (IIS) server.
component: net
page_id: net:net-2x:setup/pf_net_ik_configuring_iis_to_use_the_sample_applications
canonical_url: https://docs.pingidentity.com/integrations/net/net-2x/setup/pf_net_ik_configuring_iis_to_use_the_sample_applications.html
llms_txt: https://docs.pingidentity.com/integrations/net/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 20, 2024
section_ids:
  steps: Steps
---

# Configuring IIS to use the sample applications

To see a working demonstration of the .NET Integration Kit, deploy the sample applications and configure your Internet Information Services (IIS) server.

## Steps

1. From the .NET Integration Kit `.zip` archive, copy the `sample/IdpSample` and `sample/SpSample` directories to your IIS server.

2. Create IIS applications that point to the `IdPSample` and `SPSample` directories.

   1. On the IIS Manager navigation pane, right-click your web site, and then click Add Application.

   2. In the Alias field, enter a name, such as `PingFederate .NET IdP Sample`.

   3. From the Application Pool list, select an application pool that uses .NET v4.0 and runs in Integrated mode.

   4. In the Physical path field, enter the path to the `IdpSample` directory that you copied in step 1.

   5. Finish configuring the application. Click OK.

   6. Repeat steps a-e to create a similar application for the `SpSample` directory.

3. Set the default web site document to `Default.aspx`.

   1. On the IIS Manager navigation pane, select your web site.

   2. In the details window, double-click Default Document.

   3. Set `Default.aspx` as the default content page.

4. Give ASP.NET permission to write to the sample application `config` directories.

   1. In File Explorer, right-click your `IdpSample/config` directory, and then click Properties.

   2. On the Config Properties dialog, on the Security tab, in the Group of user names section, select the ASP.NET account (IUSR or IIS\_IUSRS). Click Edit.

   3. On the Permissions for Config dialog, select Write. Click OK.

   4. On the IdpSample dialog, click OK.

   5. Repeat steps a-d for the `SpSample/config` directory.

---

---
title: Configuring PingFederate to use the sample applications
description: To see a working demonstration of the .NET Integration Kit, deploy the configuration archive and sample applications.
component: net
page_id: net:net:setup/pf_net_ik_configuring_pf_to_use_the_sample_applications
canonical_url: https://docs.pingidentity.com/integrations/net/net/setup/pf_net_ik_configuring_pf_to_use_the_sample_applications.html
llms_txt: https://docs.pingidentity.com/integrations/net/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 20, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Configuring PingFederate to use the sample applications

To see a working demonstration of the .NET Integration Kit, deploy the configuration archive and sample applications.

## About this task

The sample configuration archive configures a single instance of PingFederate with an example integration that uses both the IdP and SP sample applications. It automatically creates two instances of the OpenToken Adapter.

|   |                                                                                                                                                                                                                                                                                                                                                                                                             |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Deploying the configuration archive destroys your existing PingFederate configuration. Test it on a fresh installation of PingFederate, or back up your current configuration as shown in [Exporting an archive](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_configurationarchivetasklet_configurationarchiveexportstate.html) in the PingFederate documentation. |

## Steps

1. Start PingFederate.

2. In the Agentless Integration Kit `.zip` archive, copy `sample/data.zip` to `<pf_install>/pingfederate/server/deploy/drop-in-deployer`.

3. If your PingFederate instance is on a different computer than the sample applications, modify your configuration.

   1. In your IdP and SP adapter instance configurations, change any URLs with `http://localhost` to point to the correct host and port for the sample applications on your Internet Information Services (IIS) server.

   2. On the **Identity Provider > Default URL** tab, change `http://localhost` to point to the correct host and port for the sample applications. Repeat for the **Service Provider > Default URL** tab.

   3. In a browser, go to the sample application URL. On the **Configuration Options** page, change the PF Host Name to point to the host and port of your PingFederate server.

---

---
title: Configuring PingFederate to use the sample applications
description: To see a working demonstration of the .NET Integration Kit, deploy the configuration archive and sample applications.
component: net
page_id: net:net-2x:setup/pf_net_ik_configuring_pf_to_use_the_sample_applications
canonical_url: https://docs.pingidentity.com/integrations/net/net-2x/setup/pf_net_ik_configuring_pf_to_use_the_sample_applications.html
llms_txt: https://docs.pingidentity.com/integrations/net/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 20, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Configuring PingFederate to use the sample applications

To see a working demonstration of the .NET Integration Kit, deploy the configuration archive and sample applications.

## About this task

The sample configuration archive configures a single instance of PingFederate with an example integration that uses both the IdP and SP sample applications. It automatically creates two instances of the OpenToken Adapter.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                 |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Deploying the configuration archive will destroy your existing PingFederate configuration. Test it on a fresh installation of PingFederate, or back up your current configuration as shown in [Exporting an archive](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_configurationarchivetasklet_configurationarchiveexportstate.html) in the PingFederate documentation. |

## Steps

1. Start PingFederate.

2. In the Agentless Integration Kit `.zip` archive, copy `sample/data.zip` to `<pf_install>/pingfederate/server/deploy/drop-in-deployer`.

3. If your PingFederate instance is on a different computer than the sample applications, modify your configuration.

   1. In your IdP and SP adapter instance configurations, change any URLs with `http://localhost` to point to the correct host and port for the sample applications on your Internet Information Services (IIS) server.

   2. On the **Identity Provider > Default URL** tab, change `http://localhost` to point to the correct host and port for the sample applications. Repeat for the **Service Provider > Default URL** tab.

   3. In a browser, go to the sample application URL. On the **Configuration Options** page, change the PF Host Name to point to the host and port of your PingFederate server.

---

---
title: Custom application setup
description: You can configure the .NET Integration Kit to integrate PingFederate with your identity provider (IdP) or service provider (SP) application.
component: net
page_id: net:net:setup/pf_net_ik_custom_application_setup
canonical_url: https://docs.pingidentity.com/integrations/net/net/setup/pf_net_ik_custom_application_setup.html
llms_txt: https://docs.pingidentity.com/integrations/net/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 24, 2026
---

# Custom application setup

You can configure the .NET Integration Kit to integrate PingFederate with your identity provider (IdP) *(tooltip: \<div class="paragraph">
\<p>A service that manages identity information and provides authentication services to relying clients or SPs within a federated or distributed network.\</p>
\</div>)* or service provider (SP) *(tooltip: \<div class="paragraph">
\<p>In SAML, an entity that receives and accepts an authentication assertion issued by an IdP, typically for the purpose of allowing access to a protected resource.\</p>
\</div>)* application.

You can also find a working demonstration of the .NET Integration Kit in the [Sample applications setup](pf_net_ik_sample_applications_setup.html).

---

---
title: Custom application setup
description: You can configure the .NET Integration Kit to integrate PingFederate with your identity provider (IdP) or service provider (SP) application.
component: net
page_id: net:net-2x:setup/pf_net_ik_custom_application_setup
canonical_url: https://docs.pingidentity.com/integrations/net/net-2x/setup/pf_net_ik_custom_application_setup.html
llms_txt: https://docs.pingidentity.com/integrations/net/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 20, 2024
---

# Custom application setup

You can configure the .NET Integration Kit to integrate PingFederate with your identity provider (IdP) or service provider (SP) application.

If you would like to see a working demonstration of the .NET Integration Kit before integrating your own applications, see [Sample applications setup](pf_net_ik_sample_applications_setup.html) instead.

---

---
title: Deploying the OpenToken Agent
description: Deploy the OpenToken Agent to allow your web application to serialize user attributes into an OpenToken for IdPs, and validate and extract user attributes for SPs. Learn more in Integrating the OpenToken agent into your .NET 8 application.
component: net
page_id: net:net:setup/pf_net_ik_deploying_opentoken_agent
canonical_url: https://docs.pingidentity.com/integrations/net/net/setup/pf_net_ik_deploying_opentoken_agent.html
llms_txt: https://docs.pingidentity.com/integrations/net/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 24, 2026
page_aliases: ["pf_net_ik_deploying_the_opentoken_agent.adoc"]
section_ids:
  steps: Steps
---

# Deploying the OpenToken Agent

Deploy the OpenToken Agent to allow your web application to serialize user attributes into an OpenToken for IdPs, and validate and extract user attributes for SPs. Learn more in [Integrating the OpenToken agent into your .NET 8 application](pf_net_ik_integrating_the_opentoken_agent_into_your_net_application.html).

## Steps

1. From the .NET Integration Kit `.zip` archive, copy the `dist/opentoken-agent.dll` file to a location accessible to your ASP.NET Core 8 project.

2. Add a reference to `opentoken-agent.dll` in your `.csproj` file:

   ```shell
   <ItemGroup>
       <Reference Include="opentoken-agent">
         <HintPath>path/to/opentoken-agent.dll</HintPath>
       </Reference>
     </ItemGroup>
   ```

3. Refer to the API documentation in `dist/docs/` for the full reference of available classes and methods.

4. Refer to the sample application source code in `sample_src/` for end-to-end examples of IdP and SP integration.

---

---
title: Deploying the OpenToken Agent
description: To allow your web application to send and receive user attributes in OpenToken format, deploy theplatformOpenToken agent on your application server.
component: net
page_id: net:net-2x:setup/pf_net_ik_deploying_the_opentoken_agent
canonical_url: https://docs.pingidentity.com/integrations/net/net-2x/setup/pf_net_ik_deploying_the_opentoken_agent.html
llms_txt: https://docs.pingidentity.com/integrations/net/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 20, 2024
section_ids:
  steps: Steps
---

# Deploying the OpenToken Agent

To allow your web application to send and receive user attributes in OpenToken format, deploy theplatformOpenToken agent on your application server.

## Steps

1. Download the .NET Integration Kit `.zip` archive from the [**Add-ons** tab of the PingFederate downloads page](https://www.pingidentity.com/en/resources/downloads/pingfederate.html) or the [Ping Identity Marketplace](https://marketplace.pingone.com/item/net-integration-kit).

2. Stop your web application.

3. If you are upgrading from a previous version of the .NET Integration Kit, delete your existing `opentoken-agent.dll` file.

4. From the integration `.zip` archive, copy `dist/opentoken-agent.dll` to a location that your .NET application can access.

5. Start your web application.

6. If you have more than one web application, repeat steps 1-5 for each application.

---

---
title: Download manifest
description: The following files are included in the .NET Integration Kit .zip archive:
component: net
page_id: net:net:release_notes/pf_net_ik_download_manifest
canonical_url: https://docs.pingidentity.com/integrations/net/net/release_notes/pf_net_ik_download_manifest.html
llms_txt: https://docs.pingidentity.com/integrations/net/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 1, 2026
---

# Download manifest

The following files are included in the .NET Integration Kit `.zip` archive:

* `Legal.pdf`: Copyright and license information

* `/dist`: Contains the OpenToken agent for .NET:

  * `opentoken-agent.dll`: Agent Toolkit for .NET 8. Reference this library in your ASP.NET Core 8 application to read, write, and delete OpenToken.

  * `docs/` Agent Toolkit API documentation.

* `/sample`: Contains the prebuilt .NET 8 sample applications and the PingFederate configuration archive:

  * `/IdpSample`: IdP sample application binaries, ready to deploy.

  * `/SpSample`: SP sample application binaries, ready to deploy.

  * `data.zip`: PingFederate configuration archive. [Import this into PingFederate](http://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_configurationarchivetasklet_configurationarchiveimportstate.html) to configure the OpenToken Adapter instances and SP/IdP connections required to run the sample applications in standalone mode.

* `sample_src/`: Contains the full source code for both sample applications. Use this as a reference when integrating the OpenToken Agent into your own ASP.NET Core 8 application, or modify it to suit your environment.

  * `IdpSample/`: Source code for the IdP sample application.

  * `SpSample/` Source code for the SP sample application.

|   |                                                                                                                                                                              |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The OpenToken Adapter isn't included in this integration `.zip` archive. Learn more in [Updating the OpenToken Adapter](../setup/pf_net_ik_updating_opentoken_adapter.html). |

---

---
title: Download manifest
description: The following files are included in the .NET Integration Kit .zip archive:
component: net
page_id: net:net-2x:release_notes/pf_net_ik_download_manifest
canonical_url: https://docs.pingidentity.com/integrations/net/net-2x/release_notes/pf_net_ik_download_manifest.html
llms_txt: https://docs.pingidentity.com/integrations/net/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 20, 2024
---

# Download manifest

The following files are included in the .NET Integration Kit `.zip` archive:

* `ReadMeFirst.pdf`: Contains links to this online documentation.

* `/legal`: Contains the following document:

  * `Legal.pdf`: Copyright and license information

* `/dist`: Contains the OpenToken agent for .NET:

  * `opentoken-agent.chm`: Agent Toolkit API Documentation

  * `opentoken-agent.dll`: Agent Toolkit for .NET 4.0

* `/sample`: Contains the .NET sample applications:

  * `/IdpSample`: IdP Sample Application

  * `/SpSample`: SP Sample Application

  * `data.zip`: PingFederate configuration archive for the Sample Applications

|   |                                                                                                                                                                                                      |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The OpenToken Adapter is not included in this integration `.zip` archive. You can find more information in [Updating the OpenToken Adapter](../setup/pf_net_ik_updating_the_opentoken_adapter.html). |

---

---
title: IdP single logout integration
description: When a PingFederate identity provider (IdP) server receives a single logout (SLO) request, it redirects the user's browser to the Logout Service URL defined in the IdP OpenToken Adapter configuration. The Logout Service is responsible for removing the user's local session and redirecting the user's browser back to PingFederate to complete the logout flow.
component: net
page_id: net:net:setup/pf_net_ik_idp_slo_integration
canonical_url: https://docs.pingidentity.com/integrations/net/net/setup/pf_net_ik_idp_slo_integration.html
llms_txt: https://docs.pingidentity.com/integrations/net/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 26, 2026
section_ids:
  logout-flow: Logout flow
  processing-logout-requests: Processing logout requests
---

# IdP single logout integration

When a PingFederate identity provider (IdP) *(tooltip: \<div class="paragraph">
\<p>A service that manages identity information and provides authentication services to relying clients or SPs within a federated or distributed network.\</p>
\</div>)* server receives a single logout (SLO) *(tooltip: \<div class="paragraph">
\<p>The process of signing a user out of multiple sites where the user has started a SSO session.\</p>
\</div>)* request, it redirects the user's browser to the Logout Service URL defined in the [IdP OpenToken Adapter configuration](pf_net_ik_configuring_opentoken_idp_adapter_instance.html). The Logout Service is responsible for removing the user's local session and redirecting the user's browser back to PingFederate to complete the logout flow.

## Logout flow

The following diagram shows the flow of IdP-initiated SLO, but the architecture would also support SP-initiated SLO:

![eol1563995496884](../_images/eol1563995496884.jpg)

1. User initiates a single logout request. The request targets the PingFederate server's `/idp/startSLO.ping` endpoint.

2. PingFederate sends a logout requests and receives responses for all SPs registered for the current SSO session.

3. PingFederate redirects the user's browser to the IdP application's Logout Service, passing a resume query parameter.

4. The Logout Service clears the local user session and any OpenToken cookie, then redirects the browser back to PingFederate using the resume path to display a logout success page.

## Processing logout requests

The Logout Service endpoint must:

1. Remove the user's local session.

   If your application uses ASP.NET Core cookie authentication, sign out using `SignOutAsync` and clear the server-side session.

2. Delete the OpenToken cookie using `Agent.DeleteToken`

   This is applicable only when the agent is configured with `use-cookie=true`. If the agent uses query parameter mode, no cookie deletion is necessary.

3. Redirect back to PingFederate using the resume query parameter to complete the logout flow.

The following code snippet shows how to implement the Logout Service in an ASP.NET Core 8 controller:

```shell
using opentoken;

// 1. Clear local session and sign out (if using ASP.NET Core cookie authentication)
HttpContext.Session?.Clear();
await HttpContext.SignOutAsync(CookieAuthenticationDefaults.AuthenticationScheme);

// 2. Delete the OpenToken cookie (only applicable when
// use-cookie=true in agent-config.txt)
Agent agent = new Agent("<PATH_TO_FILE>/agent-config.txt");
agent.DeleteToken(Response);

// 3. Redirect back to PingFederate to complete the SLO flow
string? resumePath = Request.Query["resume"];
if (!string.IsNullOrEmpty(resumePath))
{
    string redirectUrl = "<PingFederate-base-url>".TrimEnd('/') + resumePath;
    Response.Redirect(redirectUrl, true);
}
```

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The Logout Service URL must match the **Logout Service** endpoint configured in the [IdP OpenToken Adapter instance](http://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_configuring_opentoken_idp_adapter_instance.html) in PingFederate.In ASP.NET Core 8, `HttpContext.Session?.Clear()` and `SignOutAsync` replace the legacy `Session.Abandon()` call used in the older .NET Framework integration.The `Agent.DeleteToken` method handles removal of both the primary cookie and the legacy fallback cookie written by the agent. |

---

---
title: IdP single logout integration
description: When an IdP PingFederate server receives a request for SLO, it redirects the user's browser to the Logout Service defined in the IdP OpenToken Adapter configuration. The redirect URL includes an OpenToken containing the user attributes defined in the IdP OpenToken Adapter instance for the partner connection. The Logout Service should remove the user's session on the application server and redirect the user's browser back to the IdP PingFederate server.
component: net
page_id: net:net-2x:setup/pf_net_ik_idp_single_logout_integration
canonical_url: https://docs.pingidentity.com/integrations/net/net-2x/setup/pf_net_ik_idp_single_logout_integration.html
llms_txt: https://docs.pingidentity.com/integrations/net/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 20, 2024
section_ids:
  logout-flow: Logout flow
  processing-logout-requests: Processing logout requests
---

# IdP single logout integration

When an IdP PingFederate server receives a request for SLO, it redirects the user's browser to the Logout Service defined in the IdP OpenToken Adapter configuration. The redirect URL includes an OpenToken containing the user attributes defined in the IdP OpenToken Adapter instance for the partner connection. The Logout Service should remove the user's session on the application server and redirect the user's browser back to the IdP PingFederate server.

## Logout flow

The following diagram shows the flow of IdP-initiated SLO, but the architecture would also support SP-initiated SLO.

![eol1563995496884](../_images/eol1563995496884.jpg)

1. User initiates a single logout request. The request targets the PingFederate server's `/idp/startSLO.ping` endpoint.

2. PingFederate sends a logout requests and receives responses for all SPs registered for the current SSO session.

3. PingFederate redirects the request to the IdP web application's Logout Service, which identifies and removes the user's session locally.

4. The application Logout Service redirects back to PingFederate to display a logout-success page.

## Processing logout requests

The following code snippet shows how to process a logout request and send it back to PingFederate through the user's browser:

```
// Remove local session
. . . .
IDictionary userInfo = new Dictionary<String, String>();
// Add userId for the logged on user as the token subject
userInfo.Add(Agent.TOKEN_SUBJECT, <userId>);
String returnUrl = "https://<{pingfed} DNS>:9031" + Request["resume"];
Response.Redirect(returnUrl);
```