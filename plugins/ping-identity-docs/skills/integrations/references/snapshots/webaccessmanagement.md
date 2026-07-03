---
title: IdP deployment note
description: "The adapter configuration supports a \"login URL\" parameter. If the WAM session cookie is not found in the request, then the PingFederate server redirects the request to the URL page along with the relative resumePath, which is generated from PingFederate and intended for asynchronous communication between the adapter and the external application. (The state is saved in PingFederate, and processing is resumed when the application redirects to the resumePath.)"
component: webAccessManagement
page_id: webAccessManagement:web_access_management_wam_integration_kit:pf_wam_ik_idp_deployment_note
canonical_url: https://docs.pingidentity.com/integrations/webAccessManagement/web_access_management_wam_integration_kit/pf_wam_ik_idp_deployment_note.html
revdate: June 18, 2024
---

# IdP deployment note

The adapter configuration supports a "login URL" parameter. If the WAM session cookie is not found in the request, then the PingFederate server redirects the request to the URL page along with the relative `resumePath,` which is generated from PingFederate and intended for asynchronous communication between the adapter and the external application. (The state is saved in PingFederate, and processing is resumed when the application redirects to the `resumePath`.)

The login URL page can authenticate the user and redirect the request back to PingFederate. An example of a JSP code snippet for redirecting the request is shown below.

```javascript
<%
  String resumePath = request.getParameter("resumePath");
    if(resumePath != null) {
      resumePath = <PingFed_URL> + resumePath; (1)
      response.sendRedirect(resumePath);
    }
%>
```

|       |                                                                        |
| ----- | ---------------------------------------------------------------------- |
| **1** | `<PingFed_URL>` is the fully-qualified URL of the PingFederate server. |

---

---
title: IdP process overview
description: The following figure illustrates the request flow and how the WAM IdP Adapter is leveraged in generating a SAML/WS-Federation assertion using a WAM session cookie.
component: webAccessManagement
page_id: webAccessManagement:web_access_management_wam_integration_kit:pf_wam_ik_idp_process_overview
canonical_url: https://docs.pingidentity.com/integrations/webAccessManagement/web_access_management_wam_integration_kit/pf_wam_ik_idp_process_overview.html
revdate: June 18, 2024
section_ids:
  processing-steps: Processing Steps
---

# IdP process overview

The following figure illustrates the request flow and how the WAM IdP Adapter is leveraged in generating a SAML/WS-Federation assertion using a WAM session cookie.

![vwa1563995785356](_images/vwa1563995785356.jpg)

## Processing Steps

1. The user's browser attempts to access the IdP application. The third-party WAM Web Agent intercepts the request and asks for the user's identity. The user enters the requested credentials and submits the login page.

2. The WAM Server validates the user's credentials and creates a WAM session cookie. The user now has access to the application.

3. The user clicks a link that initiates an SSO transaction to the partner application. The request is redirected to the PingFederate IdP Server. The WAM session cookie generated in step 2 is included in the request.

4. The PingFederate WAM IdP Adapter uses the WAM plug-in to decrypt the WAM session cookie and then transfers the attributes to the PingFederate IdP Server. You can create an attribute contract to map the WAM session cookie and response attributes. For more information, see [Defining an attribute contract](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_usersessioncreationtasklet_createattributecontractstate.html) in the PingFederate documentation.

5. The PingFederate IdP server generates a SAML/WS-Federation assertion and redirects the request, with the assertion, back through the user's browser to the SP site.

---

---
title: Install or upgrade the adapter
description: This topic describes how to install the WAM Integration Kit for both the IdP and the SP adapters.
component: webAccessManagement
page_id: webAccessManagement:web_access_management_wam_integration_kit:pf_wam_ik_install_or_upgrade_the_adapter
canonical_url: https://docs.pingidentity.com/integrations/webAccessManagement/web_access_management_wam_integration_kit/pf_wam_ik_install_or_upgrade_the_adapter.html
revdate: June 18, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Install or upgrade the adapter

## About this task

This topic describes how to install the WAM Integration Kit for both the IdP and the SP adapters.

|   |                                                                                                                          |
| - | ------------------------------------------------------------------------------------------------------------------------ |
|   | If you have already deployed version 2.5.1 or later of the OpenToken Adapter, skip steps 1-3 in the following procedure. |

## Steps

1. Download the WAM Integration Kit `.zip` archive from the [**Add-ons** tab of the PingFederate downloads page](https://www.pingidentity.com/en/resources/downloads/pingfederate.html) or the [Ping Identity Marketplace](https://marketplace.pingone.com/item/wam-integration-kit).

2. Stop the PingFederate server if it is running.

3. Delete the following files from the `<PF_install>/pingfederate/server/default/deploy` directory:

   * The WAM adapter JAR file (`pf-wam-adapter-<version>.jar`)

   * Any existing OpenToken Adapter files (`opentoken*.jar`)

     * If the adapter JAR filename indicates version 2.1 or earlier, delete the supporting library `opentoken-java-1.x.jar`.

4. Unzip the integration-kit distribution file and copy the following files from the `/dist` directory to the `<PF_install>/pingfederate/server/default/deploy` directory.

   * `opentoken-adapter-2.5.1.jar`

   * `pf-wam-adapter-2.0.0.jar`

5. If you are running PingFederate 6.0 as a Windows service, add the following line to the `Java Library Path` section of the `pingfederate/sbin/wrapper/PingFederateService.conf` file:

   ```properties
   wrapper.java.library.path.append_system_path=true
   ```

6. Start the PingFederate server.

---

---
title: Known issues and limitations
description: Known Limitations
component: webAccessManagement
page_id: webAccessManagement:web_access_management_wam_token_translator:pf_wam_tt_known_issues_and_limitations
canonical_url: https://docs.pingidentity.com/integrations/webAccessManagement/web_access_management_wam_token_translator/pf_wam_tt_known_issues_and_limitations.html
revdate: June 27, 2024
---

# Known issues and limitations

**Known Limitations**

* Due to a limitation with PingFederate 8.1 and earlier versions, when configuring two SP connections with the same provisioner, the second connection built may be pre-populated with the channel from the first connection. To avoid conflicts, delete this pre-populated channel and create a unique channel for each connection.

---

---
title: OAM-specific configuration
description: When configuring the OAM adapter, the following values are needed:
component: webAccessManagement
page_id: webAccessManagement:web_access_management_wam_integration_kit:pf_wam_ik_oam_specific_configuration
canonical_url: https://docs.pingidentity.com/integrations/webAccessManagement/web_access_management_wam_integration_kit/pf_wam_ik_oam_specific_configuration.html
revdate: June 18, 2024
---

# OAM-specific configuration

When configuring the OAM adapter, the following values are needed:

| Field                         | Description                                                                                                                | Example Value                                  |
| ----------------------------- | -------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------- |
| Cookie Path                   | Relative path in the URL where the cookie is active.                                                                       | `/`                                            |
| Protected Resource            | The path (and optionally, the hostname) that defines the protected resource. This value comes from your OAM configuration. | `http://<OAM Host Identifier>/<Resource Path>` |
| Error URL                     | Optional field containing a URL used as a redirection target in the event of an error during SSO when using this adapter.  |                                                |
| User Identifier               | HTTP header used to identify the end userID.                                                                               | `OAM_REMOTE_USER`                              |
| Session Token Name            | The name of the encrypted cookie used for SSO.                                                                             | `ObSSOCookie`                                  |
| Session Token Loggedoff Value | The value the Session Token should be set to when the user has logged out of OAM.                                          | `loggedoutcontinue`                            |

|   |                                                                                                                                                    |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The above values are examples and are dependent on the OAM environment. Ask your Oracle administrator for the values required in your environment. |

Learn more about this configuration in the [Oracle Access Manager documentation](https://docs.oracle.com/cd/E52734_01/oam/index.html).

---

---
title: Overview of Web Access Management integrations
description: The PingFederate Web Access Management (WAM) Integration Kit allows developers to integrate their applications with a PingFederate server acting as either an identity provider (IdP) or a Service Provider (SP).
component: webAccessManagement
page_id: webAccessManagement::pf_is_overview_of_wam_integrations
canonical_url: https://docs.pingidentity.com/integrations/webAccessManagement/pf_is_overview_of_wam_integrations.html
revdate: August 12, 2024
section_ids:
  pingfederate-web-access-management-integration-kit: PingFederate Web Access Management Integration Kit
  pingfederate-web-access-management-token-translator: PingFederate Web Access Management Token Translator
---

# Overview of Web Access Management integrations

## PingFederate Web Access Management Integration Kit

The PingFederate Web Access Management (WAM) Integration Kit allows developers to integrate their applications with a PingFederate server acting as either an identity provider (IdP) or a Service Provider (SP).

## PingFederate Web Access Management Token Translator

The PingFederate Web Access Management (WAM) Token Translator provides a Token Processor and a Token Generator for use with the PingFederate WS-Trust Security Token Service (STS).

---

---
title: SP deployment notes
description: The following notes provide additional information for using the WAM Integration Kit as an SP:
component: webAccessManagement
page_id: webAccessManagement:web_access_management_wam_integration_kit:pf_wam_ik_sp_deployment_notes
canonical_url: https://docs.pingidentity.com/integrations/webAccessManagement/web_access_management_wam_integration_kit/pf_wam_ik_sp_deployment_notes.html
revdate: June 18, 2024
---

# SP deployment notes

The following notes provide additional information for using the WAM Integration Kit as an SP:

* The WAM SP Adapter relies on a custom authentication scheme to validate the authentication request coming from the PingFederate SP Adapter. The secret specified in the SP Adapter is verified against the one configured with the scheme. You can create custom authentication schemes for specific WAM systems using their API.

  The authentication scheme for OAM is included in the samples folder at the following location: `<integration_kit_install_dir>` `/sdk/samples/oam/PingCustomAuthPlugin.java`

* To support Account Linking, the Account Linking Service has to be implemented and then protected by the WAM Web Agent. This could be done as a `JSP` page that redirects back to PingFederate. The relative `resumePath` is sent as part of the request and the `JSP` page needs to create the absolute URL and redirect, as shown below.

  ```javascript
  <%
    String resumePath = request.getParameter("resumePath");
      if(resumePath != null) {
        resumePath = <PingFed_URL> + resumePath; (1)
        response.sendRedirect(resumePath);
      }
  %>
  ```

  |       |                                                                                                                                                                                                                                                                                                                                  |
  | ----- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  | **1** | `<PingFed_URL>` is the fully-qualified URL of the PingFederate server.`resumePath` is generated from PingFederate and intended for asynchronous communication between the adapter and the external application. The state is saved in PingFederate and processing is resumed when the application redirects to the `resumePath`. |

  The WAM SP Adapter retrieves the user information from the WAM session cookie and resumes SSO.

---

---
title: SP process overview
description: The following figure illustrates the request flow and how the WAM SP Adapter leverages a SAML/WS-Federation assertion to create a WAM session cookie.
component: webAccessManagement
page_id: webAccessManagement:web_access_management_wam_integration_kit:pf_wam_ik_sp_process_overview
canonical_url: https://docs.pingidentity.com/integrations/webAccessManagement/web_access_management_wam_integration_kit/pf_wam_ik_sp_process_overview.html
revdate: June 18, 2024
section_ids:
  processing-steps: Processing Steps
---

# SP process overview

The following figure illustrates the request flow and how the WAM SP Adapter leverages a SAML/WS-Federation assertion to create a WAM session cookie.

![ezn1563995791248](_images/ezn1563995791248.jpg)

## Processing Steps

1. The PingFederate SP server receives a SAML/WS-Federation assertion from the IdP.

2. PingFederate parses the assertion.

3. The WAM SP Adapter uses the WAM plug-in to create a WAM session cookie and embeds the cookie in the response.

4. A request containing the WAM session cookie is redirected to the browser.

5. The request is then redirected to the SP Application, which is protected by the third-party WAM Web Agent.

6. The third-party WAM Web Agent intercepts the request, extracts and validates the WAM session cookie, and allows access to the application.

---

---
title: Test the IdP adapter
description: You can test this adapter using the samples applications that are included in the Java Integration Kit. Follow this procedure to verify adapter functions:
component: webAccessManagement
page_id: webAccessManagement:web_access_management_wam_integration_kit:pf_wam_ik_test_the_idp_adapter
canonical_url: https://docs.pingidentity.com/integrations/webAccessManagement/web_access_management_wam_integration_kit/pf_wam_ik_test_the_idp_adapter.html
revdate: June 18, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Test the IdP adapter

## About this task

You can test this adapter using the samples applications that are included in the Java Integration Kit. Follow this procedure to verify adapter functions:

## Steps

1. Download the Java Integration kit from the [PingFederate server add-ons page](https://www.pingidentity.com/en/resources/downloads/pingfederate.html).

2. Complete the steps in [Sample application setup](../../java/setup/pf_java_ik_sample_application_setup.html) in the Java Integration Kit documentation to set up an IdP application.

3. Configure an instance of the WAM Adapter.

4. Reconfigure the SP connection to use the WAM Adapter instance.

   Delete the existing adapter instance and map the WAM Adapter instance in its place. For details, see [Managing mappings](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_managing_mappings.html) in the PingFederate documentation.

5. On a web page protected by the third-party WAM web Agent, create an "SSO" link to the PingFederate `startSSO` endpoint, including the sample SP's connection ID, in the following format:

   ```none
   http[s]://<PF_host>:<port>/IdP/startSSO.ping?PartnerSpId=<connection_id>
   ```

   * `<PF_host>` is the machine running the PingFederate server.

   * `<port>` is the PingFederate port (default value: `9031`).

   * `<connection_id>` is the Connection ID of the SP connection.

6. Access the protected web page by authenticating through the WAM web Agent and click the SSO link.

7. You are logged on to the Java sample application.

---

---
title: Test the SP adapter
description: You can test this adapter using the samples applications that are included in the Java Integration Kit.
component: webAccessManagement
page_id: webAccessManagement:web_access_management_wam_integration_kit:pf_wam_ik_test_the_sp_adapter
canonical_url: https://docs.pingidentity.com/integrations/webAccessManagement/web_access_management_wam_integration_kit/pf_wam_ik_test_the_sp_adapter.html
revdate: June 18, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Test the SP adapter

## About this task

You can test this adapter using the samples applications that are included in the Java Integration Kit.

## Steps

1. Download the Java Integration kit from the [PingFederate server add-ons page](https://www.pingidentity.com/en/resources/downloads/pingfederate.html).

2. Complete the steps in [Sample application setup](../../java/setup/pf_java_ik_sample_application_setup.html) in the Java Integration Kit documentation to set up an SP application.

3. Configure an instance of the WAM Adapter as shown in [Setting Up the SP Adapter](pf_wam_ik_configuring_an_sp_adapter_instance.html).

4. Reconfigure the IdP connection to use the WAM Adapter instance.

   Delete the existing adapter instance for the connection and map the WAM Adapter instance in its place.

5. From the Main Menu, click **Adapters** under My SP Configuration.

6. Protect a web page using the WAM web Agent.

7. On the same web server, create an unprotected web page with a hyperlink to PingFederate's SP-initiated SSO endpoint in the following format:

   ```none
   http[s]://<PF_host>:<port>/sp/startSSO.ping?TargetResource=<protected_resource>&PartnerIdpId=<connection_id>
   ```

   * `<PF_host>` is the machine running the PingFederate server.

   * `<port>` is the port (default value: `9031`).

   * `<protected_resource>` is the web page protected in the previous step.

   * `<connection_id>` is the Connection ID of the IdP connection.

8. Click the SSO link on the unprotected web page.

   You should arrive at the IdP application's login page.

9. Add at least one of the users in the username drop-down list to the WAM Server.

   Refer to your WAM platform documentation for more information.

10. On the IdP application's login page, log in with a username managed by your WAM platform.

    You should be redirected to a WAM platform-protected web page. Independently, you can view cookies from your browser to see that a WAM session cookie has been created.

---

---
title: Token generator sample code
description: The code snippet below demonstrates using the PingFederate Java STS Client SDK to retrieve a WAM session token through the PingFederate STS.
component: webAccessManagement
page_id: webAccessManagement:web_access_management_wam_token_translator:pf_wam_tt_token_generator_sample_code
canonical_url: https://docs.pingidentity.com/integrations/webAccessManagement/web_access_management_wam_token_translator/pf_wam_tt_token_generator_sample_code.html
revdate: July 5, 2024
---

# Token generator sample code

The code snippet below demonstrates using the PingFederate Java STS Client SDK to retrieve a WAM session token through the PingFederate STS.

```javascript
 // Configure STS Client (SP side / IdP Connection)
 STSClientConfiguration stsConfig = new STSClientConfiguration();
 stsConfig.setStsEndpoint("https://sp.domain.com:9031/sp/sts.wst");
 stsConfig.setOutTokenType(TokenType.BINARY);

 // Instantiate the STSClient
 STSClient stsClient = new STSClient(stsConfig);

 // Send an RST Issue request to {pingfed} STS
 Element wamsessionToken = stsClient.issueToken(samlToken);
```

---

---
title: Token processor sample code
description: The code snippet below demonstrates using the PingFederate Java STS Client SDK to send a WAM session token to the PingFederate STS.
component: webAccessManagement
page_id: webAccessManagement:web_access_management_wam_token_translator:pf_wam_tt_token_processor_sample_code
canonical_url: https://docs.pingidentity.com/integrations/webAccessManagement/web_access_management_wam_token_translator/pf_wam_tt_token_processor_sample_code.html
revdate: July 5, 2024
---

# Token processor sample code

The code snippet below demonstrates using the PingFederate Java STS Client SDK to send a WAM session token to the PingFederate STS.

```javascript
 // Example method for obtaining the WAM Session token.
 // You will need to implement this for your environment.
 String wamSessionToken = getWAMSessionToken();

 // Configure STS Client (IdP side / SP Connection)
 STSClientConfiguration stsConfig = new STSClientConfiguration();
 stsConfig.setAppliesTo("http://sp.domain.com");
 stsConfig.setStsEndpoint("https://idp.domain.com:9031/idp/sts.wst");
 stsConfig.setInTokenType(TokenType.BINARY);

 // Instantiate the STSClient
 STSClient stsClient = new STSClient(stsConfig);

 // Send an RST Issue request to {pingfed} STS
 Element samlToken = stsClient.issueToken(wamSessionToken);
```

---

---
title: Token translator installation
description: This topic describes how to install the WAM Token Translator to configure the Token Processor, Token Generator, or both.
component: webAccessManagement
page_id: webAccessManagement:web_access_management_wam_token_translator:pf_wam_tt_token_translator_installation
canonical_url: https://docs.pingidentity.com/integrations/webAccessManagement/web_access_management_wam_token_translator/pf_wam_tt_token_translator_installation.html
revdate: June 27, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Token translator installation

## About this task

This topic describes how to install the WAM Token Translator to configure the Token Processor, Token Generator, or both.

|   |                                                                                                                                  |
| - | -------------------------------------------------------------------------------------------------------------------------------- |
|   | If you have already deployed version 2.5.1 or later of the OpenToken Adapter, skip steps 1 through 3 in the following procedure. |

## Steps

1. Download the WAM Token Translator `.zip` archive from the [**Add-ons** tab of the PingFederate downloads page](https://www.pingidentity.com/en/resources/downloads/pingfederate.html) or the [Ping Identity Marketplace](https://marketplace.pingone.com/item/wam-token-translator).

2. Stop the PingFederate server if it is running.

3. Delete any existing OpenToken Adapter files (`opentoken*.jar`) from the `<PF_install>/pingfederate/server/default/deploy` directory.

   * If the adapter JAR filename indicates version 2.1 or earlier, delete the supporting library `opentoken-java-1.x.jar`.

4. Unzip the token translator distribution file and copy the following files from the `/dist` directory to the `<PF_install>/pingfederate/server/default/deploy` directory.

   * `opentoken-adapter-2.5.1.jar`

   * `pf-wam-token-translator-2.0.jar`

5. If you are running PingFederate 6.0 as a Windows service, add the following line to the `Java Library Path` section of the `pingfederate/sbin/wrapper/PingFederateService.conf` file:

   ```properties
   wrapper.java.library.path.append_system_path=true
   ```

6. Start the PingFederate server.

---

---
title: Using the STS client SDK
description: Ping Identity provides a Java STS-Client SDK for enabling Web Service applications (Client or Provider) to interact with the PingFederate STS. The SDK is available for download on the PingFederate server add-ons page.
component: webAccessManagement
page_id: webAccessManagement:web_access_management_wam_token_translator:pf_wam_tt_using_the_sts_client_sdk
canonical_url: https://docs.pingidentity.com/integrations/webAccessManagement/web_access_management_wam_token_translator/pf_wam_tt_using_the_sts_client_sdk.html
revdate: June 27, 2024
---

# Using the STS client SDK

Ping Identity provides a Java STS-Client SDK for enabling Web Service applications (Client or Provider) to interact with the PingFederate STS. The SDK is available for download on the [PingFederate server add-ons page](https://www.pingidentity.com/en/resources/downloads/pingfederate.html).

The SDK provides functionality for sending a security token to the PingFederate STS for exchange with a returned SAML token, which can then be used to access Web Services across domains. The following code examples show how to send a token and request the exchange. Refer to the SDK documentation for modifications that apply to your site.

---

---
title: WAM plug-in installation for OAM
description: Deploy the pre-built OAM-compatible WAM plug-in for both IdP and SP adapters.
component: webAccessManagement
page_id: webAccessManagement:web_access_management_wam_integration_kit:pf_wam_ik_wam_plug_in_installation_for_oam
canonical_url: https://docs.pingidentity.com/integrations/webAccessManagement/web_access_management_wam_integration_kit/pf_wam_ik_wam_plug_in_installation_for_oam.html
revdate: June 18, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# WAM plug-in installation for OAM

## About this task

Deploy the pre-built OAM-compatible WAM plug-in for both IdP and SP adapters.

You can find more information on configuring the WAM plug-in for OAM in [OAM-specific configuration](pf_wam_ik_oam_specific_configuration.html).

## Steps

1. Get the necessary OAM API library (`oamasdk-api.jar`) from the [Oracle Identity Management Download site](http://www.oracle.com/technetwork/middleware/downloads/oid-11g-161194.html) and save it to the `<PF_install>/pingfederate/server/default/deploy` directory.

2. Copy the applicable plugin file to the `<PF_install>/pingfederate/server/default/deploy` directory:

   * If you are using OAM 10g, copy `<integration_kit_install_dir>/dist/oam/pf-oam-plugin.jar`.

   * If you are using OAM 11g, copy `<integration_kit_install_dir>/dist/oam11g/pf-oam-11g-plugin.jar`.

3. Complete the [Install or upgrade the adapter](pf_wam_ik_install_or_upgrade_the_adapter.html) procedure before restarting the PingFederate server (refer to the next section).

---

---
title: WAM plug-in installation for OAM
description: This section describes how to deploy the pre-built OAM-compatible WAM plug-in for both Token Processors and Token Generators.
component: webAccessManagement
page_id: webAccessManagement:web_access_management_wam_token_translator:pf_wam_tt_wam_plug_in_installation_for_oam
canonical_url: https://docs.pingidentity.com/integrations/webAccessManagement/web_access_management_wam_token_translator/pf_wam_tt_wam_plug_in_installation_for_oam.html
revdate: July 5, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# WAM plug-in installation for OAM

## About this task

This section describes how to deploy the pre-built OAM-compatible WAM plug-in for both Token Processors and Token Generators.

## Steps

1. Get the necessary OAM API library (`oamasdk-api.jar`) from the [Oracle Identity Management Download site](https://www.oracle.com/middleware/technologies/identity-management/downloads.html) and save it to the `<PF_install>/pingfederate/server/default/deploy` directory.

2. Copy the `<token_translator_install_dir>/dist/pf-oam-plugin.jar` file to the `<PF_install>/pingfederate/server/default/deploy` directory.

3. Complete the [Token translator installation](pf_wam_tt_token_translator_installation.html) prior to restarting the PingFederate server (see next section).

---

---
title: WAM plug-in installation for RSA
description: This section describes how to deploy the pre-built RSA-compatible WAM plug-in for both IdP and SP adapters.
component: webAccessManagement
page_id: webAccessManagement:web_access_management_wam_integration_kit:pf_wam_ik_wam_plug_in_installation_for_rsa
canonical_url: https://docs.pingidentity.com/integrations/webAccessManagement/web_access_management_wam_integration_kit/pf_wam_ik_wam_plug_in_installation_for_rsa.html
revdate: June 18, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# WAM plug-in installation for RSA

## About this task

This section describes how to deploy the pre-built RSA-compatible WAM plug-in for both IdP and SP adapters.

## Steps

1. The additional RSA API libraries for creating a WAM plug-in to interact with PingFederate are included in the `<integration_kit_install_dir>/dist/rsa` directory.

   * `axm-runtime-api-6.1.4.jar`

   * `jsafeFIPS-6.1.jar`

   * `jsafeJCEFIPS-6.1.jar`

2. Copy the RSA API libraries from the `<integration_kit_install_dir>/dist/rsa` directory into the `<PF_install>/pingfederate/server/default/deploy` directory.

3. Copy the `pf-rsa-plugin.jar` from the `<integration_kit_install_dir>/dist/rsa` directory into the `<PF_install>/pingfederate/server/default/deploy`.

4. Complete the [Install or upgrade the adapter](pf_wam_ik_install_or_upgrade_the_adapter.html) prior to restarting the PingFederate server.

---

---
title: WAM plug-in installation for RSA
description: This section describes how to deploy the pre-built RSA-compatible WAM plug-in for both Token Processor and Token Generators.
component: webAccessManagement
page_id: webAccessManagement:web_access_management_wam_token_translator:pf_wam_tt_wam_plug_in_installation_for_rsa
canonical_url: https://docs.pingidentity.com/integrations/webAccessManagement/web_access_management_wam_token_translator/pf_wam_tt_wam_plug_in_installation_for_rsa.html
revdate: July 5, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# WAM plug-in installation for RSA

## About this task

This section describes how to deploy the pre-built RSA-compatible WAM plug-in for both Token Processor and Token Generators.

## Steps

1. Copy the following API libraries from the `<token_translator_install_dir>/dist/rsa` directory to `<PF_install>/pingfederate/server/default/deploy`:

   * `axm-runtime-api-6.1.4.jar`

   * `jsafeFIPS-6.1.jar`

   * `jsafeJCEFIPS-6.1.jar`

   * `pf-rsa-plugin.jar`

2. Complete the [Token translator installation](pf_wam_tt_token_translator_installation.html) prior to restarting the PingFederate server.

---

---
title: WAM plug-ins
description: This kit ships with WAM plug-ins compatible with OAM 10g and 11g, RSA Access Manager 6.1, and a simple SDK to create custom WAM plug-ins for other systems.
component: webAccessManagement
page_id: webAccessManagement:web_access_management_wam_token_translator:pf_wam_tt_wam_plug_ins
canonical_url: https://docs.pingidentity.com/integrations/webAccessManagement/web_access_management_wam_token_translator/pf_wam_tt_wam_plug_ins.html
revdate: July 5, 2024
---

# WAM plug-ins

This kit ships with WAM plug-ins compatible with OAM 10g and 11g, RSA Access Manager 6.1, and a simple SDK to create custom WAM plug-ins for other systems.

---

---
title: Web Access Management (WAM) Integration Kit
description: The PingFederate WAM Integration Kit allows developers to integrate their applications with a PingFederate server acting as either an identity provider (IdP) or a Service Provider (SP).
component: webAccessManagement
page_id: webAccessManagement::pf_wam_ik
canonical_url: https://docs.pingidentity.com/integrations/webAccessManagement/pf_wam_ik.html
revdate: June 18, 2024
section_ids:
  intended-audience: Intended audience
  system-requirements: System requirements
---

# Web Access Management (WAM) Integration Kit

The PingFederate WAM Integration Kit allows developers to integrate their applications with a PingFederate server acting as either an identity provider (IdP) or a Service Provider (SP).

The WAM IdP Adapter allows an IdP enterprise to extend an existing investment by using the SAML or WS-Federation protocols to expand the reach of the WAM domain to partner applications. The WAM SP Adapter allows an SP enterprise to accept SAML or WS-Federation assertions and provide secure internet single sign-on (SSO) to applications protected by a supported WAM system.

|   |                                                                                                                                                                                                                                                                                    |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | This kit is designed to work with WAM products from multiple vendors. A WAM plug-in is required to connect the integration kit with each third-party system. This kit ships with WAM plug-ins compatible with Oracle Access Manager (OAM) 11g R2, and with RSA Access Manager 6.1. |

|   |                                                                                                                       |
| - | --------------------------------------------------------------------------------------------------------------------- |
|   | The current RSA plugin does not support Adaptive Authentication. It is only qualified against Authentication Manager. |

A simple software development kit (SDK) is also included to create custom WAM plug-ins for other systems. If you are creating a WAM plug-in for any third-party product other than OAM and RSA Access Manager, you must complete the tasks in the WAM plug-in SDK `README.txt` file located in the `<integration_kit_install_dir>/sdk` directory.

## Intended audience

This document is intended for PingFederate administrators with experience in the configuration and maintenance of the OAM Access Server or RSA Access Manager and other WAM tools, and developers with experience using JAVA SDKs

Before you start, you should be familiar with the following parts of the PingFederate documentation:

* [Identity provider SSO configuration](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_ident_provid_sso_config.html)

* [Managing IdP adapters](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_managing_idp_adapters.html)

Please consult the WAM tool documentation if you encounter any difficulties in areas not directly associated with PingFederate or the WAM Integration Kit.

## System requirements

* PingFederate 6.x or later

* WAM plug-in for the desired third-party system, built and deployed per the WAM plug-in SDK documentation

* Associated vendor-supplied libraries to support the WAM plug-in you are using

* Fully functional WAM plug-ins for OAM and RSA are included in the WAM Integration Kit package

* Separate third-party Web Agent configured using the WAM server administrative software

  |   |                                                                                                                 |
  | - | --------------------------------------------------------------------------------------------------------------- |
  |   | PingFederate must be running in the same domain as the third-party WAM Web Agent for the applicable WAM Server. |