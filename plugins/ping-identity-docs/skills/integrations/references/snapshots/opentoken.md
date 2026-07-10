---
title: Changelog
description: The following is the change history for the OpenToken Token Translator.
component: opentoken
page_id: opentoken:release_notes:pf_opentoken_tt_changelog
canonical_url: https://docs.pingidentity.com/integrations/opentoken/release_notes/pf_opentoken_tt_changelog.html
llms_txt: https://docs.pingidentity.com/integrations/opentoken/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 21, 2024
section_ids:
  opentoken-token-translator-1-0-2-august-2022: OpenToken Token Translator 1.0.2 - August 2022
  opentoken-token-translator-1-0-1-december-2012: OpenToken Token Translator 1.0.1 - December 2012
  opentoken-token-translator-1-0-april-2009: OpenToken Token Translator 1.0 - April 2009
---

# Changelog

The following is the change history for the OpenToken Token Translator.

## OpenToken Token Translator 1.0.2 - August 2022

* Updated dependencies to address security issues.

## OpenToken Token Translator 1.0.1 - December 2012

* Updated to address security issue found since the previous release

* Added support for OpenToken 2.5.1 Adapter and the OpenToken 2.5.1 Agent

## OpenToken Token Translator 1.0 - April 2009

* Initial Release

---

---
title: Download manifest
description: The following files are included in the OpenToken Token Translator .zip archive:
component: opentoken
page_id: opentoken:release_notes:pf_opentoken_tt_download_manifest
canonical_url: https://docs.pingidentity.com/integrations/opentoken/release_notes/pf_opentoken_tt_download_manifest.html
llms_txt: https://docs.pingidentity.com/integrations/opentoken/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 21, 2024
---

# Download manifest

The following files are included in the OpenToken Token Translator `.zip` archive:

* `Legal.pdf` - copyright and license information

* `agent` - contains the OpenToken Agent and supporting libraries

  * `opentoken-agent-<version>.jar` - a JAR file that contains the OpenToken Agent

  * `lib` - contains the libraries needed by the OpenToken Agent

    * `commons-beanutils-1.9.4.jar` - the Apache Commons Bean Utility library

    * `commons-collections-3.2.2.jar` - the Apache Commons Collections library

    * `commons-logging-1.1.1.jar` - the Apache Commons Logging library

* `dist/pingfederate/server.default` - contains the integration files

  * `deploy` - contains the Java libraries

    * `pf-opentoken-token-translator-<version>.jar` - a JAR file that contains the OpenToken Token Translator JAR.

---

---
title: IdP installation and setup
description: This section describes how to install and configure the OpenToken Token Processor for PingFederate acting as an IdP.
component: opentoken
page_id: opentoken:setup:pf_opentoken_tt_idp_installation_and_setup
canonical_url: https://docs.pingidentity.com/integrations/opentoken/setup/pf_opentoken_tt_idp_installation_and_setup.html
llms_txt: https://docs.pingidentity.com/integrations/opentoken/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 5, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# IdP installation and setup

## About this task

This section describes how to install and configure the OpenToken Token Processor for PingFederate acting as an IdP.

## Steps

1. Download the OpenToken Token Translator `.zip` archive from the [**Add-ons** tab of the PingFederate downloads page](https://www.pingidentity.com/en/resources/downloads/pingfederate.html) or the [Ping Identity Marketplace](https://marketplace.pingone.com/item/opentoken-token-translator).

2. Stop PingFederate.

3. Copy the `pf-opentoken-token-translator-<version>.jar` file from the deploy directory of this distribution to the `<pf-install>/pingfederate/server/default/deploy` directory of your PingFederate server installation.

   |   |                                                                                                                                                                       |
   | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | If you have a previous version of the OpenToken Token Translator file installed, please delete it from the above location and replace it with the version referenced. |

4. Log on to the PingFederate administrative console and click Token Processors under IdP Configuration on the main menu.

   If you do not see Token Processors on the Main Menu, enable WS-Trust by going to the Server Settings Roles & Protocols screen and selecting WS-Trust for the IdP Role.

   |   |                                                                                                                                                                                                                        |
   | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | To enable token exchange, you may be prompted to provide SAML 1.x and SAML 2.0 federation identifiers for the STS on the Federation Info screen. Refer to the Federation Info screen's Help page for more information. |

5. On the Manage Token Processor Instances tab, click Create New Instance.

6. On the Type tab, enter an Instance Name and Instance ID, and select OpenToken Token Processor as the Type.

7. Click Next.

8. On the Instance Configuration screen, enter a strong password for generating the encryption key.

9. Click Show Advanced Fields to set other encryption and validation options.

   For more information, see the screen description column.

10. Click Next.

11. On the Actions screen, click Download and then Export to save the `agent-config.txt` file.

    The WSC application that generates the OpenToken will need this information.

12. Click Next.

13. On the Extended Contract tab, add any attributes that you want to map into the SAML assertion, in addition to the subject.

14. Click Next.

15. (Optional) On the Token Attributes screen, select any or all attributes whose values should be masked in PingFederate log files.

    Additionally, you can select Mask all OGNL-expression generated log values.

16. Click Next.

17. On the Summary tab, verify that the information is correct and click Done.

18. On the Manage Token Processor Instances screen, click Save.

---

---
title: Install the OpenToken agent API
description: Complete the following to install the Java OpenToken Agent API.
component: opentoken
page_id: opentoken:setup:pf_opentoken_tt_install_the_opentoken_agent_api
canonical_url: https://docs.pingidentity.com/integrations/opentoken/setup/pf_opentoken_tt_install_the_opentoken_agent_api.html
llms_txt: https://docs.pingidentity.com/integrations/opentoken/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 21, 2024
section_ids:
  steps: Steps
---

# Install the OpenToken agent API

Complete the following to install the Java OpenToken Agent API.

## Steps

1. Copy the following JAR files to a location in the CLASSPATH of the Java application:

   * `opentoken-agent-2.7.2.jar`

   * `commons-collections-3.2.2.jar`

     |   |                                                                      |
     | - | -------------------------------------------------------------------- |
     |   | Version 3.2.2 or later of the Apache Commons Collection is required. |

2. Ensure the following Apache Commons libraries are also available in the application CLASSPATH:

   * `commons-beanutils-1.9.4.jar`

   * `commons-logging-1.1.1.jar`

---

---
title: OpenToken Token Generator Settings Reference
description: Field descriptions for the OpenToken Token Generator configuration screen.
component: opentoken
page_id: opentoken:setup:pf_opentoken_generator_settings
canonical_url: https://docs.pingidentity.com/integrations/opentoken/setup/pf_opentoken_generator_settings.html
llms_txt: https://docs.pingidentity.com/integrations/opentoken/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 21, 2024
---

# OpenToken Token Generator Settings Reference

Field descriptions for the OpenToken Token Generator configuration screen.

**Table 1. Standard fields**

| Field            | Description                                                                             |
| ---------------- | --------------------------------------------------------------------------------------- |
| Password         | The password to use for generating the encryption key. Also known as the shared secret. |
| Confirm Password | Must match the value entered in the Password field.                                     |

**Table 2. Advanced fields**

| Field                        | Description                                                                                                                                                                                                                                                                                                                             |
| ---------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Cipher Suite                 | The algorithm, cipher mode, and key size that should be used for encrypting the token.The default selected value is AES-128/CBC.                                                                                                                                                                                                        |
| Token Lifetime               | The duration in seconds for which the token is valid. Valid range is 1 to 28800.The default value is `300` (5 minutes).                                                                                                                                                                                                                 |
| Session Lifetime             | The duration in seconds for which the token may be re-issued without authentication. Valid range is 1 to 259200.The default value is `43200` (12 hours).                                                                                                                                                                                |
| Not Before Tolerance         | The amount of time in seconds to allow for clock skew between servers. Valid range is 0 to 3600.The default value is `0`.                                                                                                                                                                                                               |
| Force SunJCE Provider        | If selected, the SunJCE provider is forced for encryption and decryption.                                                                                                                                                                                                                                                               |
| Use Verbose Error Messages   | If selected, use verbose TokenException messages.                                                                                                                                                                                                                                                                                       |
| Obfuscate Password           | If selected, the password will be obfuscated and password-strength validation will be applied. Clearing the checkbox allows backward compatibility with previous OpenToken agents.                                                                                                                                                      |
| Skip Trimming of Backslashes | If not selected, it prevents insecure content from affecting the security of your application and the agent. Update your applications with the latest version of the agent.It is recommended to not change the value of this flag to avoid a negative security impact, such as someone maliciously adding slashes to exploit the system |

---

---
title: OpenToken Token Processor Settings Reference
description: Field descriptions for the OpenToken Token Processor configuration screen.
component: opentoken
page_id: opentoken:setup:pf_opentoken_token_processor_settings
canonical_url: https://docs.pingidentity.com/integrations/opentoken/setup/pf_opentoken_token_processor_settings.html
llms_txt: https://docs.pingidentity.com/integrations/opentoken/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 21, 2024
---

# OpenToken Token Processor Settings Reference

Field descriptions for the OpenToken Token Processor configuration screen.

**Standard fields**

| Field            | Description                                                                             |
| ---------------- | --------------------------------------------------------------------------------------- |
| Password         | The password to use for generating the encryption key. Also known as the shared secret. |
| Confirm Password | Must match the value entered in the Password field.                                     |

**Advanced fields**

| Field                              | Description                                                                                                                                                                                                                                     |
| ---------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Cipher Suite                       | The algorithm, cipher mode, and key size that should be used for encrypting the token.The default selected value is AES-128/CBC.                                                                                                                |
| Token Lifetime                     | The duration in seconds for which the token is valid. Valid range is 1 to 28800.The default value is `300` (5 minutes).                                                                                                                         |
| Session Lifetime                   | The duration in seconds for which the token may be re-issued without authentication. Valid range is 1 to 259200.The default value is `43200` (12 hours).                                                                                        |
| Not Before Tolerance               | The amount of time in seconds to allow for clock skew between servers. Valid range is 0 to 3600.The default value is `0`.                                                                                                                       |
| Force SunJCE Provider              | If selected, the SunJCE provider is forced for encryption and decryption.                                                                                                                                                                       |
| Use Verbose Error Messages         | If selected, use verbose TokenException messages.                                                                                                                                                                                               |
| Obfuscate Password                 | If selected, the password will be obfuscated and password-strength validation will be applied. Clearing the checkbox allows backward compatibility with previous OpenToken agents.                                                              |
| Skip Malformed Attribute Detection | If not selected, it prevents insecure content from affecting the security of your application/agent. It is recommended to update your applications with the latest version of the agent.It is recommended to not change the value of this flag. |

---

---
title: OpenToken Token Translator
description: The PingFederate OpenToken Token Translator provides a Token Processor and a Token Generator for use with the PingFederate WS-Trust Security Token Service (STS).
component: opentoken
page_id: opentoken::pf_opentoken_tt
canonical_url: https://docs.pingidentity.com/integrations/opentoken/pf_opentoken_tt.html
llms_txt: https://docs.pingidentity.com/integrations/opentoken/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 21, 2024
section_ids:
  intended-audience: Intended audience
  system-requirements: System requirements
---

# OpenToken Token Translator

The PingFederate OpenToken Token Translator provides a Token Processor and a Token Generator for use with the PingFederate WS-Trust Security Token Service (STS).

The Token Processor allows an Identity Provider (IdP) STS to accept and validate an OpenToken from a Web Service Client (WSC) and then map user attributes into a SAML token for the WSC to send to a Web Service Provider (WSP). The Token Generator allows a Service Provider (SP) STS to issue an OpenToken for a WSP, including mapped attributes from an incoming SAML token.

|   |                                                                                                                                                                                                                                                                                                                                    |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Ping Identity provides a Java STS-Client Software Development Kit (SDK) for enabling web service applications (client or provider) to interact with the PingFederate STS. You can download the Java Client SDK from the [PingFederate server add-ons page](https://www.pingidentity.com/en/resources/downloads/pingfederate.html). |

OpenToken is an open-standard, secure session cookie used to pass user information between an application and PingFederate. For STS purposes, the OpenToken is passed as a Web Services Security (WSS) binary security token in WS-Trust messages. The data within the OpenToken is a set of key/value pairs, encrypted using common encryption algorithms, as illustrated below:

![qnc1563995538233](_images/qnc1563995538233.png)

This translator package includes a Java Application Programmer Interface (API) for WSC and WSP developers to use for writing or reading an OpenToken, respectively.

## Intended audience

This document is intended for PingFederate administrators.

If you need help during the setup process, see the following resources:

* The following sections of the PingFederate documentation:

  * [WS-Trust STS configuration](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_wstrust_sts_config.html)

## System requirements

* PingFederate 9.3 or later

* To use the Java API, J2SE Java Runtime Environment 1.5 or later is required on the WSC and WSP

* To use strong Advanced Encryption Standard (AES) encryption with a key size of more than 128 bits, the Java Cryptography Extension (JCE) Unlimited Strength Jurisdiction Policy Files must be installed in your JDK on PingFederate, as well as the WSC and WSP.

---

---
title: Read an OpenToken as a WSP
description: The Agent API provides access to functionality for reading an OpenToken received in an Issue request from the PingFederate STS.
component: opentoken
page_id: opentoken:setup:pf_opentoken_tt_read_an_opentoken_as_a_wsp
canonical_url: https://docs.pingidentity.com/integrations/opentoken/setup/pf_opentoken_tt_read_an_opentoken_as_a_wsp.html
llms_txt: https://docs.pingidentity.com/integrations/opentoken/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 21, 2024
section_ids:
  java-sample-code: Java Sample Code
---

# Read an OpenToken as a WSP

The Agent API provides access to functionality for reading an OpenToken received in an Issue request from the PingFederate STS.

## Java Sample Code

The code snippet below demonstrates using the PingFederate STS Java Client SDK to retrieve the OpenToken issued from the PingFederate STS and using the OpenToken Agent API to read the OpenToken. If any errors are encountered while creating the token, a TokenException is thrown:

```
// Configure STS Client
              (SP-side, IdP connection) AgentConfiguration spAgentConfiguration = new
              AgentConfiguration(); spAgentConfiguration.setPassword("Password1");
              spAgentConfiguration.setCipherSuite(Token.CIPHER_SUITE_AES128CBC);    // Instantiate the OpenToken agent
   Agent spAgent = new Agent(spAgentConfiguration);
// Configure STS
              Client STSClientConfiguration spStsConfig = new STSClientConfiguration();
              spStsConfig.setStsEndpoint("https://sp.domain.com:9031/sp/sts.wst");
              spStsConfig.setOutTokenType(TokenType.BINARY);
              spStsConfig.setOutTokenValueType(TokenType.OPENTOKEN);    // Instantiate STS Client
   STSClient spStsClient = new STSClient(spStsConfig);
   // Send RST Issue request to STS
   Element opentoken = spStsClient.issueToken(new Saml20Token(samlToken));
   // Read OpenToken
String otk = textContent(opentoken);
MultiMap otkValues = new MultiValueMap();
otkValues = spAgent.readTokenToMultiMap(otk);
```

---

---
title: SP installation and setup
description: Download the OpenToken Token Translator .zip archive from the Add-ons tab of the PingFederate downloads page or the Ping Identity Marketplace.
component: opentoken
page_id: opentoken:setup:pf_opentoken_tt_sp_installation_and_setup
canonical_url: https://docs.pingidentity.com/integrations/opentoken/setup/pf_opentoken_tt_sp_installation_and_setup.html
llms_txt: https://docs.pingidentity.com/integrations/opentoken/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 5, 2024
section_ids:
  steps: Steps
---

# SP installation and setup

## Steps

1. Download the OpenToken Token Translator `.zip` archive from the [**Add-ons** tab of the PingFederate downloads page](https://www.pingidentity.com/en/resources/downloads/pingfederate.html) or the [Ping Identity Marketplace](https://marketplace.pingone.com/item/opentoken-token-translator).

2. Stop PingFederate.

3. Copy the `pf-opentoken-token-translator-<version>.jar` file from the dist directory of this distribution to the `<pf-install>/pingfederate/server/default/deploy` directory of your PingFederate server installation.

   |   |                                                                                                                                                                       |
   | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | If you have a previous version of the OpenToken Token Translator file installed, please delete it from the above location and replace it with the version referenced. |

4. Log on to the PingFederate administrative console and click Token Generators under SP Configuration on the main menu.

   If you don't see Token Generators on the main menu, enable WS-Trust by going to the Server Settings Roles & Protocols screen and selecting WS-Trust for the SP Role.

   |   |                                                                                                                                                                                                                          |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
   |   | To enable token validation, you may be prompted to provide SAML 1.x and SAML 2.0 federation identifiers for the STS on the Federation Info screen. Refer to the Federation Info screen's Help page for more information. |

5. On the Manage Token Generator Instances tab, click Create New Instance.

6. On the Type tab, enter an Instance Name and Instance ID, and select OpenToken Token Generator as the Type.

7. Click Next.

8. On the Instance Configuration page, enter in a strong password for generating the encryption key. Optionally, you can click Show Advanced Fields to set other encryption and validation options. Refer to the screen Description column for more information.

9. Click Next.

10. On the Actions page, click Download and then Export to save the `agent-config.txt`file.

    The WSP application that receives the OpenToken will need this information later.

11. Click Next.

12. On the Extended Contract tab, add any attributes that you want to map from the SAML assertion, in addition to the subject.

13. Click Next.

14. On the Summary tab, verify that the information is correct and click Done.

15. On the Manage Token Generator Instances screen, click Save.

---

---
title: The OpenToken agent API
description: WSC and WSP application developers can use the Java OpenToken Agent API (included in this distribution) to write and read an OpenToken.
component: opentoken
page_id: opentoken:setup:pf_opentoken_tt_the_opentoken_agent_api
canonical_url: https://docs.pingidentity.com/integrations/opentoken/setup/pf_opentoken_tt_the_opentoken_agent_api.html
llms_txt: https://docs.pingidentity.com/integrations/opentoken/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 21, 2024
---

# The OpenToken agent API

WSC and WSP application developers can use the Java OpenToken Agent API (included in this distribution) to write and read an OpenToken.

The API provide access to functionality for writing an OpenToken at the WSC to be exchanged for a SAML token, and for reading an OpenToken at the WSP that was issued from a SAML token.

|   |                                                                                                                                                                                                                                                                                                                                      |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | The Agent API may be used in conjunction with the Java STS Client SDK for interacting with the PingFederate WS-Trust endpoints. You can download the Java Client SDK from the [PingFederate server add-ons page](https://www.pingidentity.com/en/resources/downloads/pingfederate.html). Examples in this section implement the SDK. |

|   |                                                                                                                                                                                                     |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | If you have already installed a previous version of the OpenToken Agent, we recommend removing the existing Agent JAR file and installing the current version to address potential security issues. |

---

---
title: Write an OpenToken as a WSC
description: The OpenToken Agent API provides access to functionality for writing an OpenToken as a WSC to include in an Issue request to the PingFederate STS.
component: opentoken
page_id: opentoken:setup:pf_opentoken_tt_write_an_opentoken_as_a_wsc
canonical_url: https://docs.pingidentity.com/integrations/opentoken/setup/pf_opentoken_tt_write_an_opentoken_as_a_wsc.html
llms_txt: https://docs.pingidentity.com/integrations/opentoken/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 21, 2024
section_ids:
  java-sample-code: Java Sample Code
---

# Write an OpenToken as a WSC

The OpenToken Agent API provides access to functionality for writing an OpenToken as a WSC to include in an Issue request to the PingFederate STS.

## Java Sample Code

The writeToken method of the Agent class takes an org.apache.commons.collections.MultiMap collection of attributes and encodes them into an OpenToken.

|   |                                                                                                    |
| - | -------------------------------------------------------------------------------------------------- |
|   | The collection of attributes must contain a key named "subject" for a valid token to be generated. |

If any errors are encountered while creating the token, a TokenException is thrown.

The code snippet below demonstrates generating an OpenToken and using the PingFederate STS Java Client SDK to send the OpenToken to the PingFederate STS:

```
// Configure the Opentoken
              agent AgentConfiguration agentConfiguration = new AgentConfiguration();
              agentConfiguration.setPassword("2Federate");
              agentConfiguration.setCipherSuite(Token.CIPHER_SUITE_AES128CBC);    // Instantiate the OpenToken agent
   Agent agent = new Agent(agentConfiguration);
   // Set OpenToken attributes
   MultiMap values = new MultiValueMap();
   values.put(Agent.TOKEN_SUBJECT, "joe");
   values.put("foo", "bar");
   String tokenData = agent.writeToken(values);
// Configure STS
              Client STSClientConfiguration idpStsConfig = new STSClientConfiguration();
              idpStsConfig.setAppliesTo("http://sp.domain.com");
              idpStsConfig.setStsEndpoint("https://idp.domain.com:9031/idp/sts.wst");
              idpStsConfig.setInTokenType(TokenType.BINARY);
              idpStsConfig.setInTokenValueType(TokenType.OPENTOKEN);    // Instantiate STS Client
   STSClient idpStsClient = new STSClient(idpStsConfig);
   // Send RST Issue request to STS
   Element samlToken = idpStsClient.issueToken(tokenData);
```

---

---
title: WS-Trust STS processing
description: The following figure shows a basic Web Services scenario using the PingFederate WS-Trust STS in the role of both IdP and SP:
component: opentoken
page_id: opentoken::pf_opentoken_tt_ws_trust_sts_processing
canonical_url: https://docs.pingidentity.com/integrations/opentoken/pf_opentoken_tt_ws_trust_sts_processing.html
llms_txt: https://docs.pingidentity.com/integrations/opentoken/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 21, 2024
---

# WS-Trust STS processing

The following figure shows a basic Web Services scenario using the PingFederate WS-Trust STS in the role of both IdP and SP:

![rim1563995538988](_images/rim1563995538988.png)

**Processing Steps**

1. A WSC sends a Request Security Token (RST) message containing an OpenToken as a SOAP request to the PingFederate STS IdP endpoint.

2. The OpenToken Token Processor validates the OpenToken and, if valid, maps attributes from the OpenToken into a SAML token. PingFederate issues the SAML token based upon the SP connection configuration and embeds the token in a Request Security Token Response (RSTR) which is returned to the WSC.

3. The WSC binds the issued SAML token into a WSS header and sends it via a SOAP request to the WSP.

4. The WSP sends an RST Issue request containing the SAML token to the PingFederate STS SP endpoint. PingFederate validates the SAML token and, if valid, maps attributes from the SAML token in to an OpenToken. Ping Federate issues the Open Token based upon the OpenToken Token Generator configuration and embeds the token in an RSTR which is returned to the WSP.

5. The WSP receives the OpenToken in the RSTR for local domain processing.