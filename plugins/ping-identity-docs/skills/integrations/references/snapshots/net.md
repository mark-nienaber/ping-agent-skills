---
title: .NET Integration Kit
description: The .NET Integration Kit allows PingFederate to communicate user attributes with .NET-based web applications.
component: net
page_id: net::pf_net_ik
canonical_url: https://docs.pingidentity.com/integrations/net/pf_net_ik.html
revdate: June 20, 2024
section_ids:
  components: Components
  intended-audience: Intended audience
  system-requirements: System requirements
---

# .NET Integration Kit

The .NET Integration Kit allows PingFederate to communicate user attributes with .NET-based web applications.

When PingFederate is serving an identity provider (IdP) role, it can receive user attributes from a .NET IdP application. When PingFederate is serving a service provider (SP) role, it can send user attributes to a .NET SP application.

|   |                                                                                                                                                                                                         |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | For new integrations, we encourage you to consider the [Agentless Integration Kit](../agentless/pf_agentless_ik.html), which can integrate with a variety of platforms using a modern RESTful approach. |

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
title: Changelog
description: .NET Integration Kit 2.5.4 – March 2020
component: net
page_id: net:release_notes:pf_net_ik_changelog
canonical_url: https://docs.pingidentity.com/integrations/net/release_notes/pf_net_ik_changelog.html
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
title: Configuring an OpenToken SP Adapter instance
description: Configure the OpenToken Adapter to determine how PingFederate communicates with your service provider application.
component: net
page_id: net:setup:pf_net_ik_configuring_an_opentoken_sp_adapter_instance
canonical_url: https://docs.pingidentity.com/integrations/net/setup/pf_net_ik_configuring_an_opentoken_sp_adapter_instance.html
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
page_id: net:setup:pf_net_ik_configuring_iis_to_use_the_sample_applications
canonical_url: https://docs.pingidentity.com/integrations/net/setup/pf_net_ik_configuring_iis_to_use_the_sample_applications.html
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
page_id: net:setup:pf_net_ik_configuring_pf_to_use_the_sample_applications
canonical_url: https://docs.pingidentity.com/integrations/net/setup/pf_net_ik_configuring_pf_to_use_the_sample_applications.html
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
page_id: net:setup:pf_net_ik_custom_application_setup
canonical_url: https://docs.pingidentity.com/integrations/net/setup/pf_net_ik_custom_application_setup.html
revdate: June 20, 2024
---

# Custom application setup

You can configure the .NET Integration Kit to integrate PingFederate with your identity provider (IdP) or service provider (SP) application.

If you would like to see a working demonstration of the .NET Integration Kit before integrating your own applications, see [Sample applications setup](pf_net_ik_sample_applications_setup.html) instead.

---

---
title: Deploying the OpenToken Agent
description: To allow your web application to send and receive user attributes in OpenToken format, deploy theplatformOpenToken agent on your application server.
component: net
page_id: net:setup:pf_net_ik_deploying_the_opentoken_agent
canonical_url: https://docs.pingidentity.com/integrations/net/setup/pf_net_ik_deploying_the_opentoken_agent.html
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
page_id: net:release_notes:pf_net_ik_download_manifest
canonical_url: https://docs.pingidentity.com/integrations/net/release_notes/pf_net_ik_download_manifest.html
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
description: When an IdP PingFederate server receives a request for SLO, it redirects the user's browser to the Logout Service defined in the IdP OpenToken Adapter configuration. The redirect URL includes an OpenToken containing the user attributes defined in the IdP OpenToken Adapter instance for the partner connection. The Logout Service should remove the user's session on the application server and redirect the user's browser back to the IdP PingFederate server.
component: net
page_id: net:setup:pf_net_ik_idp_single_logout_integration
canonical_url: https://docs.pingidentity.com/integrations/net/setup/pf_net_ik_idp_single_logout_integration.html
revdate: June 20, 2024
section_ids:
  logout-flow: Logout flow
  processing-logout-requests: Processing logout requests
---

# IdP single logout integration

When an IdP PingFederate server receives a request for SLO, it redirects the user's browser to the Logout Service defined in the IdP OpenToken Adapter configuration. The redirect URL includes an OpenToken containing the user attributes defined in the IdP OpenToken Adapter instance for the partner connection. The Logout Service should remove the user's session on the application server and redirect the user's browser back to the IdP PingFederate server.

## Logout flow

The following diagram shows the flow of IdP-initiated SLO, but the architecture would also support SP-initiated SLO.

![eol1563995496884](_images/eol1563995496884.jpg)

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

---

---
title: IdP single sign-on integration
description: When PingFederate is configured as an identity provider (IdP), it needs to be able to identify a user prior to issuing a SAML assertion for that user. When using the OpenToken Adapter with PingFederate, this means that the PingFederate server attempts to read a cookie or query parameter containing an OpenToken and then use the values within to identify the user. The application that starts the SSO must include an OpenToken so that PingFederate can identify the user. Use the Agent API to write an OpenToken. The API is a .NET object that provides access to functionality for writing an OpenToken to a given HTTP response.
component: net
page_id: net:setup:pf_net_ik_idp_single_sign_on_integration
canonical_url: https://docs.pingidentity.com/integrations/net/setup/pf_net_ik_idp_single_sign_on_integration.html
revdate: June 20, 2024
section_ids:
  writing-attributes: Writing attributes
  passing-multi-value-attributes: Passing multi-value attributes
---

# IdP single sign-on integration

When PingFederate is configured as an identity provider (IdP), it needs to be able to identify a user prior to issuing a SAML assertion for that user. When using the OpenToken Adapter with PingFederate, this means that the PingFederate server attempts to read a cookie or query parameter containing an OpenToken and then use the values within to identify the user. The application that starts the SSO must include an OpenToken so that PingFederate can identify the user. Use the Agent API to write an OpenToken. The API is a .NET object that provides access to functionality for writing an OpenToken to a given HTTP response.

## Writing attributes

The writeToken method takes a `System.Collections.IDictionary` collection of attributes and encodes them into an OpenToken, which is then written to the HTTP response.

The collection of attributes must contain a key named `subject`.

If any errors are encountered while creating or writing the token to the HTTP response, a `TokenException` is thrown.

The following code snippet shows the writeToken method:

```
IDictionary userInfo = new Dictionary<String, String>();
// Add userId for the logged on user as the token subject
userInfo.Add(Agent.TOKEN_SUBJECT, <userId>);
String returnUrl = "https://<{pingfed} DNS>:9031" + Request["resume"];
. . . .
try {
   UrlHelper urlHelper = new UrlHelper(returnUrl);
   agent.WriteToken(userInfo,Response,urlHelper,false);
   returnUrl = urlHelper.ToString();
}
catch(TokenException e) {
  // Handle exception
}
```

## Passing multi-value attributes

The Agent Toolkit for .NET supports passing multi-value attributes to PingFederate. Each attribute appears in its own discrete `<AttributeValue>` element in the SAML 2.0 assertion or as a JSON array value in OAuth-based protocols. Multi-value attributes are passed using the `opentoken.MultiStringDictionary` collection.

The following code snippet shows how to pass multi-value attributes:

```
MultiStringDictionary userInfo = new MultiStringDictionary();
// Add userId for the logged on user as the token subject
userInfo.Add(Agent.TOKEN_SUBJECT, <userId>);

// Add an attribute GROUP with multiple values
userInfo.Add("GROUP", "Administrators");
userInfo.Add("GROUP", "Users");
String returnUrl = "https://<{pingfed} DNS>:9031" + Request["resume"];
. . . .
try {
   UrlHelper urlHelper = new UrlHelper(returnUrl);
   agent.WriteToken(userInfo,Response,urlHelper,false);
   returnUrl = urlHelper.ToString();
}
catch(TokenException e) {
   // Handle exception
}
```

---

---
title: Integrating the OpenToken agent into your .NET application
description: To use the .NET Integration Kit, modify your application to use the OpenToken Agent.
component: net
page_id: net:setup:pf_net_ik_integrating_the_opentoken_agent_into_your_net_application
canonical_url: https://docs.pingidentity.com/integrations/net/setup/pf_net_ik_integrating_the_opentoken_agent_into_your_net_application.html
revdate: June 27, 2024
section_ids:
  sample-code: Sample code
---

# Integrating the OpenToken agent into your .NET application

To use the .NET Integration Kit, modify your application to use the OpenToken Agent.

The agent API allows your web application to directly read or write an OpenToken package.

Instantiate the OpenToken Agent by invoking a constructor and loading the `agent-config.txt` configuration file that you saved in [Configuring an OpenToken SP Adapter instance](pf_net_ik_configuring_an_opentoken_sp_adapter_instance.html). This configuration file includes the name of the cookie that the agent object will write, as well as the key to use when encrypting a new OpenToken. If the agent does not find an agent-config.txt file, it throws an exception.

## Sample code

Modify your .NET application based on the following sample code.

```
using System;using System.
Collections.Generic;
using System.Text;
using opentoken;
using System.IO;
using opentoken.util;
using System.Collections;
using System.Collections.Generic;
. . . .
Agent agent = new Agent( "<PATH_TO_FILE>/agent-config.txt");
```

---

---
title: Known issues and limitations
description: There are no known issues.
component: net
page_id: net:release_notes:pf_net_ik_known_issues_and_limitations
canonical_url: https://docs.pingidentity.com/integrations/net/release_notes/pf_net_ik_known_issues_and_limitations.html
revdate: June 20, 2024
section_ids:
  known-issues: Known issues
  known-limitations: Known limitations
---

# Known issues and limitations

## Known issues

There are no known issues.

## Known limitations

* The OpenToken name given to any one Adapter instance must be unique within the given federation. This however is not enforced in the user interface.

* SP and IdP Sample applications are bundled with the integration kit only from presentation point of view. There is ability to create more than one unique session under the PingFederate IdP associated with a user using the demo sample applications. The situation should not appear in production environment if you are not using the bundled demo sample application in production.

* The SP adapter has the ability to send extended attributes through cookies or query parameters along with the OpenToken. So long as these additional attributes have only one value each, this works fine, however, if there are any multi-value attribute only the first value would be sent, partly because we can only set one cookie per value name.

* After replacing the agent configuration, it is sometimes necessary to disallow and then re-allow IIS write access to the file.

---

---
title: Overview of the SSO flow
description: With the .NET Integration Kit, PingFederate exchanges user attributes with your .NET application through an OpenToken token.
component: net
page_id: net::pf_net_ik_overview_of_the_sso_flow
canonical_url: https://docs.pingidentity.com/integrations/net/pf_net_ik_overview_of_the_sso_flow.html
revdate: June 20, 2024
---

# Overview of the SSO flow

With the .NET Integration Kit, PingFederate exchanges user attributes with your .NET application through an OpenToken token.

The following figure shows a basic identity-provider (IdP)-intiated single sign-on (SSO) scenario in which PingFederate federation servers using the .NET Integration Kit exist on both sides of the identity federation:

![bco1563995493632](_images/bco1563995493632.jpg)

**Description**

1. A user initiates an SSO transaction.

2. The IdP application inserts user attributes into the agent toolkit for .NET, which encrypts the data internally and generates an OpenToken token.

3. A request containing the OpenToken is redirected to the PingFederate IdP server.

4. The server invokes the OpenToken IdP Adapter, which retrieves the OpenToken, decrypts, parses, and passes the user attributes to the PingFederate IdP server. The PingFederate IdP server then generates a SAML assertion.

5. The SAML assertion is sent to the SP site.

6. The PingFederate SP server parses the SAML assertion and passes the user attributes to the OpenToken SP Adapter. The adapter encrypts the data internally and generates an OpenToken.

7. A request containing the OpenToken is redirected to the SP application.

8. The Agent Toolkit for .NET decrypts and parses the OpenToken and makes the user attributes available to the SP Application.

---

---
title: Sample applications setup
description: You can configure the .NET Integration Kit to work with the included sample applications.
component: net
page_id: net:setup:pf_net_ik_sample_applications_setup
canonical_url: https://docs.pingidentity.com/integrations/net/setup/pf_net_ik_sample_applications_setup.html
revdate: June 20, 2024
section_ids:
  components: Components
  system-requirements: System requirements
---

# Sample applications setup

You can configure the .NET Integration Kit to work with the included sample applications.

The applications provide a means of testing an end-to-end Identity Provider (IdP) and Service Provider (SP) integration with PingFederate using this integration kit.

This sample application distribution includes startup components that automatically configure PingFederate to act as both an IdP and an SP:

* The IdP server is configured to look up and send authentication information to the SP.

* The SP server is configured to forward this information to the SP sample application to create the local user session. The SP server will also be configured to send authentication requests to the IdP on behalf of local users.

## Components

* Identity provider (IdP) sample application

  * Acts as an IdP application in your demonstration environment.

* Service provider (SP) sample application

  * Acts as an SP application in your demonstration environment.

* PingFederate configuration archive

  * This `data.zip` archive automatically configures PingFederate with OpenToken Adapter instances to work with the two sample applications.

## System requirements

* PingFederate 9.0 or later.

* The OpenToken Adapter. See [Updating the OpenToken Adapter](pf_net_ik_updating_the_opentoken_adapter.html).

* Windows Server 2008 64-bit or 32-bit.

* Microsoft Internet Information Services (IIS) with the following:

  * Running version 7 or later.

  * The correct time (recently synchronized).

  * The correct time zone.

* Microsoft .NET Framework 4.0 installed and registered with IIS.

---

---
title: SP single logout (SLO)
description: When an SP PingFederate server receives a request for SLO, it redirects the user's browser to the Logout Service as configured in the SP OpenToken Adapter instance. As part of the redirect, PingFederate and the OpenToken Adapter include both an OpenToken and a resumePath query parameter.
component: net
page_id: net:setup:pf_net_ik_sp_single_logout_slo
canonical_url: https://docs.pingidentity.com/integrations/net/setup/pf_net_ik_sp_single_logout_slo.html
revdate: June 20, 2024
---

# SP single logout (SLO)

When an SP PingFederate server receives a request for SLO, it redirects the user's browser to the Logout Service as configured in the SP OpenToken Adapter instance. As part of the redirect, PingFederate and the OpenToken Adapter include both an OpenToken and a resumePath query parameter.

* The OpenToken includes attributes about the user.

* The resumePath query parameter provides the target application URL.

A user can have multiple sessions. This logout sequence, as shown in the following diagram, will occur for each of the user's sessions controlled by the SP PingFederate server.

![kcs1563995501655](_images/kcs1563995501655.jpg)

**Sequence**

1. PingFederate receives an SLO request under the SAML 2.0 protocol.

2. PingFederate, via the OpenToken Adapter, redirects the browser to the Application Server's Logout Service.

3. The Logout Service returns to PingFederate, indicating that the logout was successful.

The code needed to perform an SP SLO is identical to that required for an IdP SLO.

---

---
title: SP single sign-on integration
description: When PingFederate is configured as an SP, it takes inbound SAML assertions and converts them to some local format (cookie or otherwise) that can be used by an application to create a user's session. For an OpenToken, the PingFederate adapter takes the attributes and values from the SAML assertion and stores them in an OpenToken cookie or query parameter in the user's browser. The user is then redirected to the target application, which can then identify the user from the OpenToken, using the Agent API.
component: net
page_id: net:setup:pf_net_ik_sp_single_sign_on_integration
canonical_url: https://docs.pingidentity.com/integrations/net/setup/pf_net_ik_sp_single_sign_on_integration.html
revdate: June 20, 2024
section_ids:
  reading-attributes: Reading attributes
  receiving-multi-value-attributes: Receiving multi-value attributes
---

# SP single sign-on integration

When PingFederate is configured as an SP, it takes inbound SAML assertions and converts them to some local format (cookie or otherwise) that can be used by an application to create a user's session. For an `OpenToken`, the PingFederate adapter takes the attributes and values from the SAML assertion and stores them in an `OpenToken` cookie or query parameter in the user's browser. The user is then redirected to the target application, which can then identify the user from the `OpenToken`, using the `Agent` API.

As with the IdP, you can use the Agent API to read tokens directly. The Agent API is a .NET class that provides access to functionality for reading an `OpenToken` from a given HTTP request.

## Reading attributes

The readToken method inspects the cookie (or query parameters, depending on the agent configuration), decodes the OpenToken, and returns a collection of attributes.

If there is no token, it returns a `null` result. If an errors occurs while reading the token, it returns a `null` result and a `TokenException` is thrown.

The following code snippet shows the readToken method:

```
try {
   IDictionary userInfo = agent.ReadToken(Request);
   if(userInfo != null) {
      String username = (String)userInfo[Agent.TOKEN_SUBJECT];
   }
}
catch(TokenException e) {
   // Handle exception
}
```

## Receiving multi-value attributes

The Agent Toolkit for .NET supports receiving multi-value attributes from PingFederate. Multi-value attributes are passed using the `opentoken.MultiStringDictionary` collection.

The following code snippet shows how to process multi-value attributes:

```
try {
   MultiStringDictionary userInfo =
    agent.ReadTokenMultiStringDictionary(Request);
   if(userInfo != null) {
      String username = userInfo[Agent.TOKEN_SUBJECT][0];
      List<String> groups = userInfo["GROUP"];
   }
}
catch(TokenException e) {
   // Handle exception
}
```

---

---
title: SP single sign-on integration using account linking
description: If an SP's SSO implementation employs account linking, the flow of events is somewhat different since a user must authenticate to the SP application the first time SSO is initiated (for more information, see Key concepts in the PingFederate documentation). In this case, PingFederate and the OpenToken Adapter support an integration mechanism to redirect the user to an Account Link Service to which a user can authenticate initially. Upon successful authentication, the user's browser is redirected back to PingFederate with an OpenToken, which PingFederate uses to create an account link for the user. For subsequent SSO requests, PingFederate uses the account link established in the first SSO request to identify the user. It then creates an OpenToken and sends it to the Authentication Service associated with the application.
component: net
page_id: net:setup:pf_net_ik_sp_single_sign_on_integration_using_account_linking
canonical_url: https://docs.pingidentity.com/integrations/net/setup/pf_net_ik_sp_single_sign_on_integration_using_account_linking.html
revdate: June 20, 2024
section_ids:
  linking-accounts: Linking accounts
---

# SP single sign-on integration using account linking

If an SP's SSO implementation employs account linking, the flow of events is somewhat different since a user must authenticate to the SP application the first time SSO is initiated (for more information, see [Key concepts](https://docs.pingidentity.com/pingfederate/latest/introduction_to_pingfederate/pf_key_conc.html) in the PingFederate documentation). In this case, PingFederate and the OpenToken Adapter support an integration mechanism to redirect the user to an Account Link Service to which a user can authenticate initially. Upon successful authentication, the user's browser is redirected back to PingFederate with an OpenToken, which PingFederate uses to create an account link for the user. For subsequent SSO requests, PingFederate uses the account link established in the first SSO request to identify the user. It then creates an OpenToken and sends it to the Authentication Service associated with the application.

![qww1563995499860](_images/qww1563995499860.jpg)

1. PingFederate receives an assertion under either the SAML 2.0, OpenID Connect, or WS-Federation protocol.

2. If this is the first time the user has initiated SSO to this SP, PingFederate redirects the browser to the Application Server's Account Link Service, where the user must authenticate. Upon successful authentication, an OpenToken is returned to PingFederate, and an account link is established for this user within PingFederate. This account link is used on subsequent SSO transactions.

3. PingFederate retrieves the local user ID from its account link data store. Through the OpenToken Adapter, PingFederate generates an OpenToken based on the assertion and account link. PingFederate then redirects the user's browser to the web application's SSO Authentication Service, passing the OpenToken in the redirect.

4. The Authentication Service extracts the contents of the OpenToken, establishes a session for the user, and redirects the user's browser to the Target Resource (the resumePath URL sent as a query parameter).

## Linking accounts

In an Account Linking event, the user's browser is redirected to the configured Account Linking service in the SP OpenToken Adapter instance. The application should capture the resumePath upon a GET request to this URL with something similar to the following:

```
IDictionary userInfo = new Dictionary<String, String>();
// Add userId for the logged on user as the token subject
userInfo.Add(Agent.TOKEN_SUBJECT, <userId>);
String returnUrl = "https://<{pingfed} DNS>:9031" + Request["resume"];
. . . .
try {
   UrlHelper urlHelper = new UrlHelper(returnUrl);
   //For sample code that instantiates and configures an Agent instance, see the
   //"Integrating the OpenToken Agent into your application" topic in the documentation
   agent.WriteToken(userInfo,Response,urlHelper,false);
   returnUrl = urlHelper.ToString();
}
catch(TokenException e) {
    // Handle exception
}
Response.Redirect(returnUrl);
```

---

---
title: Testing
description: You can test the .NET Integration Kit using one of the sample applications bundled with this distribution.
component: net
page_id: net:setup:pf_net_ik_testing
canonical_url: https://docs.pingidentity.com/integrations/net/setup/pf_net_ik_testing.html
revdate: June 20, 2024
---

# Testing

You can test the .NET Integration Kit using one of the sample applications bundled with this distribution.

See [Sample applications setup](pf_net_ik_sample_applications_setup.html).

|   |                                                                                                                                                                                                                                                        |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | Do not install the `data.zip` archive as shown in [Configuring PingFederate to use the sample applications](pf_net_ik_configuring_pf_to_use_the_sample_applications.html). This will overwrite the PingFederate configuration that you just completed. |

---

---
title: Updating the OpenToken Adapter
description: The .NET Integration Kit relies on the OpenToken Adapter that is distributed with the Java Integration Kit. Update the OpenToken Adapter to get the latest feature and security updates.
component: net
page_id: net:setup:pf_net_ik_updating_the_opentoken_adapter
canonical_url: https://docs.pingidentity.com/integrations/net/setup/pf_net_ik_updating_the_opentoken_adapter.html
revdate: June 20, 2024
section_ids:
  steps: Steps
---

# Updating the OpenToken Adapter

The .NET Integration Kit relies on the OpenToken Adapter that is distributed with the Java Integration Kit. Update the OpenToken Adapter to get the latest feature and security updates.

## Steps

1. Download the Java Integration Kit `.zip` archive from the **Add-ons** tab of the [PingFederate downloads page](https://www.pingidentity.com/en/resources/downloads/pingfederate.html).

2. Stop PingFederate.

3. Delete the `opentoken-adapter-<version>.jar` file from your `<pf_install>/pingfederate/server/default/deploy` directory.

4. From the Java Integration Kit `.zip` archive, copy the contents of `dist/pingfederate` to your `<pf_install>/pingfederate` directory.

   |   |                                                                                                                                                                                                              |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
   |   | The `commons-collections`, `commons-beanutils`, and `commons-logging` libraries are provided as a convenience and should be installed only if they are not already contained in the application `CLASSPATH`. |

5. Start PingFederate.

6. If you operate PingFederate in a cluster, repeat steps 2-5 for each engine node.

---

---
title: Using the IdP sample application
description: The .NET Integration Kit identity provider (IdP) sample application demonstrates IdP-initiated single sign-on (SSO) and single logout (SLO) use cases.
component: net
page_id: net:setup:pf_net_ik_using_the_idp_sample_application
canonical_url: https://docs.pingidentity.com/integrations/net/setup/pf_net_ik_using_the_idp_sample_application.html
revdate: July 5, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Using the IdP sample application

The .NET Integration Kit identity provider (IdP) sample application demonstrates IdP-initiated single sign-on (SSO) and single logout (SLO) use cases.

## About this task

The IdP sample application simulates the IdP-initiated SSO/SLO scenario in which users authenticate to an IdP locally in order to access a remote SP application. In this scenario, users may be accessing a company portal that provides links to partner applications such as local news and weather, stock market information, and HR and 401(k) benefits.

When you authenticate locally to the IdP sample application, no communication occurs between that application and PingFederate. The user authenticates using the local user store; no SAML use cases are invoked. However, when you click a link to a third-party application, such as your company's health care provider, the IdP initiates an SSO transaction.

## Steps

1. Start the PingFederate and Internet Information Services (IIS) servers.

2. In a browser, open the sample application:

   `https://hostname/IdpSample`

3. On the main page, click Login Locally.

4. On the Identity Provider Login page, sign on as any of the listed users with a password of `test`.

5. Click Login.

6. On the Identity Provider page, try the following:

   1. **Optional:** To begin an IdP-iniated SSS to the SP sample application, click the Single Sign-On. This starts a user session on the SP and redirects you to the SP sample application. For more information, see [Using the SP Sample Application](pf_net_ik_using_the_sp_sample_application.html).

   2. **Optional:** After signing on to the SP sample application and returning to the Identity Provider main page, click Single Sign-Out to initiate a SLO request to the SP. This ends your user session on the SP as well as your local user session.