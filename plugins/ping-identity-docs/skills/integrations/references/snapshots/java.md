---
title: Advanced installation and configuration
description: PingFederate system administrators might choose to override the automated PingFederate configuration and simplified deployment of the sample applications. Although the distribution is intended primarily for quick end-to-end testing and demonstration, it can also be used as a configuration exercise or to test more production-like deployments.
component: java
page_id: java:setup:pf_java_ik_advanced_installation_and_configuration
canonical_url: https://docs.pingidentity.com/integrations/java/setup/pf_java_ik_advanced_installation_and_configuration.html
revdate: June 21, 2024
---

# Advanced installation and configuration

PingFederate system administrators might choose to override the automated PingFederate configuration and simplified deployment of the sample applications. Although the distribution is intended primarily for quick end-to-end testing and demonstration, it can also be used as a configuration exercise or to test more production-like deployments.

This section provides guidelines for alternative uses for the sample application distribution.

|   |                                                                                                                                                                                                                                                                                                |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Detailed instructions for configuring separate PingFederate servers and deploying applications in different servlet containers are beyond the scope of this document.This document provides general information, but it might not be complete or applicable to every deployment configuration. |

---

---
title: Changelog
description: The following is the change history for the Java Integration Kit.
component: java
page_id: java:release_notes:pf_java_ik_changelog
canonical_url: https://docs.pingidentity.com/integrations/java/release_notes/pf_java_ik_changelog.html
revdate: November 6, 2025
section_ids:
  java-integration-kit-2-9-1-november-2025: Java Integration Kit 2.9.1 - November 2025
  java-integration-kit-2-9-0-february-2025: Java Integration Kit 2.9.0 - February 2025
  java-integration-kit-2-8-0-october-2023: Java Integration Kit 2.8.0 – October 2023
  java-integration-kit-2-7-3-december-2022: Java Integration Kit 2.7.3 – December 2022
  java-integration-kit-2-7-2-december-2021: Java Integration Kit 2.7.2 – December 2021
  java-integration-kit-2-7-1-september-2021: Java Integration Kit 2.7.1 – September 2021
  java-integration-kit-2-7-march-2021: Java Integration Kit 2.7 – March 2021
  java-integration-kit-2-6-2-february-2020: Java Integration Kit 2.6.2 – February 2020
  java-integration-kit-2-6-1-february-2020: Java Integration Kit 2.6.1 – February 2020
  java-integration-kit-2-6-january-2020: Java Integration Kit 2.6 – January 2020
  java-integration-kit-2-5-9-january-2020: Java Integration Kit 2.5.9 – January 2020
  java-integration-kit-2-5-8-august-2019: Java Integration Kit 2.5.8 – August 2019
  java-integration-kit-2-5-7-november-2018: Java Integration Kit 2.5.7 – November 2018
  java-integration-kit-2-5-6-april-2017: Java Integration Kit 2.5.6 – April 2017
  java-integration-kit-2-5-5-august-2016: Java Integration Kit 2.5.5 – August 2016
  java-integration-kit-2-5-4-may-2016: Java Integration Kit 2.5.4 – May 2016
  java-integration-kit-2-5-3-june-2015: Java Integration Kit 2.5.3 – June 2015
  java-integration-kit-2-5-2-june-2014: Java Integration Kit 2.5.2 – June 2014
  java-integration-kit-2-5-1-november-2012: Java Integration Kit 2.5.1 – November 2012
  java-integration-kit-2-5-may-2012: Java Integration Kit 2.5 – May 2012
  java-integration-kit-2-4-2-october-2010: Java Integration Kit 2.4.2 – October 2010
  java-integration-kit-2-4-1-august-2010: Java Integration Kit 2.4.1 – August 2010
  java-integration-kit-2-4-february-2010: Java Integration Kit 2.4 – February 2010
  java-integration-kit-2-3-november-2008: Java Integration Kit 2.3 – November 2008
  java-integration-kit-2-2-june-2008: Java Integration Kit 2.2 – June 2008
  java-integration-kit-2-1-april-2008: Java Integration Kit 2.1 – April 2008
  java-integration-kit-2-0-december-2007: Java Integration Kit 2.0 – December 2007
  java-integration-kit-1-3-november-2007: Java Integration Kit 1.3 – November 2007
  java-integration-kit-1-2-1-august-2007: Java Integration Kit 1.2.1 – August 2007
  java-integration-kit-1-2-may-2007: Java Integration Kit 1.2 – May 2007
---

# Changelog

The following is the change history for the Java Integration Kit.

## Java Integration Kit 2.9.1 - November 2025

* Updated library dependencies to address potential security vulnerabilities.

## Java Integration Kit 2.9.0 - February 2025

* Removed an advanced field in the adapter configuration that allowed administrators to skip password obfuscation for the exported OpenToken agent configuration file, `agent-config.txt`.

  You can find more details about this change in [Configuring an OpenToken SP adapter instance](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_config_opentoken_sp_adapt_instance.html) and [Configuring an OpenToken IdP adapter instance](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_config_opentoken_idp_adapt_instance.html) in the PingFederate documentation.

  |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
  | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | If you are using a third-party OpenToken integration and need to use a base64 password instead of an obfuscated password, refer to step 5 in [Configuring an OpenToken SP adapter instance](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_config_opentoken_sp_adapt_instance.html) or [Configuring an OpenToken IdP adapter instance](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_config_opentoken_idp_adapt_instance.html). |

## Java Integration Kit 2.8.0 – October 2023

* Added a new OpenToken agent that uses Jakarta EE 9.

* Added new sample applications that use Jakarta EE 9.

## Java Integration Kit 2.7.3 – December 2022

* Improved security by updating the bundled Apache Log4j2 component in the sample applications.

## Java Integration Kit 2.7.2 – December 2021

* Improved security by updating the bundled Apache Log4j2 component. Learm more in security bulletin [CVE-2021-44228](https://support.pingidentity.com/s/article/Log4j2-vulnerability-CVE-CVE-2021-44228) (requires sign-on).

* Added support for reading and writing OpenTokens with the Java native multimap method. Learn more in [Reading and writing OpenTokens](../setup/pf_java_ik_reading_and_writing_opentokens.html). There's no change to encoding or decoding attributes.

  The `commons-beanutils.jar` and `commons-collections-3.2.2.jar` libraries aren't required for this method.

## Java Integration Kit 2.7.1 – September 2021

* Improved the sample application configuration pages.

  * Removed the **PF SSO Directory Service ID** and **PF SSO Directory Service Shared Secret** fields, which relied on a feature that was deprecated in PingFederate 10.2.

  * You can now enter multiple or custom connection IDs. Learn more in [IdP sample application configuration reference](../setup/pf_java_ik_idp_sample_application_configuration_reference.html) and [SP sample application configuration reference](../setup/pf_java_ik_sp_sample_application_configuration_reference.html).

* Improved the sample `data.zip` archive by enabling the redirection validation setting in PingFederate by default.

## Java Integration Kit 2.7 – March 2021

* Added a new method for reading tokens as an alternate to the Apache Commons Multimap.

## Java Integration Kit 2.6.2 – February 2020

* Fixed an issue that could cause cross-site single logout to stop working after upgrading the adapter.

## Java Integration Kit 2.6.1 – February 2020

* Fixed an issue that caused session cookies to expire at the wrong time.

## Java Integration Kit 2.6 – January 2020

* Added the **SameSite Cookie** field to support the SameSite cookie flag in web browsers.

## Java Integration Kit 2.5.9 – January 2020

* Resolved an issue that caused an error in the sample application in PingFederate 9.1 and earlier.

* Resolved an issue in the sample application sign on button that could cause an error in an authentication policy tree.

## Java Integration Kit 2.5.8 – August 2019

* Added support for RFC 6265 compliance to the OpenToken SP adapter when extended attributes are sent as cookies.

* Added support to do SLO without external logout service configuration.

* Fixed minor bugs in the sample applications.

## Java Integration Kit 2.5.7 – November 2018

* Modernized the look and feel of the Java sample applications.

* Removed the preceding dot requirement in the **Cookie Domain** setting of the OpenToken Adapter **IdP Adapter** tab.

## Java Integration Kit 2.5.6 – April 2017

* Expanded character support for entity id.

## Java Integration Kit 2.5.5 – August 2016

* Update for compatibility with PingFederate 8.2.

## Java Integration Kit 2.5.4 – May 2016

* Added an **HttpOnly** field.

## Java Integration Kit 2.5.3 – June 2015

* Added support for log4j2.

## Java Integration Kit 2.5.2 – June 2014

* Added logging to the OpenToken Agent to log the name of the token and its value at the debug level.

* Added support to validate the resume path for the IdP sample application, only enabling redirection along a relative path.

* Updated Ping Identity logos for the sample applications.

* Added support for configuring a context path for the sample applications.

## Java Integration Kit 2.5.1 – November 2012

* Address a security issue in the previous release.

* Added support for OpenToken 2.5.1 Adapter and the OpenToken 2.5.1 Agent.

## Java Integration Kit 2.5 – May 2012

* Fixed several minor defects in the IdP and SP sample applications.

* Corrected the spelling of `AgentConfiguration.setObfuscatePasword()` method name to `AgentConfiguration.setObfuscatePassword()` and deprecated the misspelled method.

* Improved Javadoc documentation for several areas of the API.

## Java Integration Kit 2.4.2 – October 2010

* Removed extraneous configuration from the IdP and SP sample application data archive (data.zip).

* Added support for UTF-8 encoding in the IdP and SP sample applications for attributes.

## Java Integration Kit 2.4.1 – August 2010

* Rewrote the IdP and SP sample applications to provide reference OpenToken integration for Java web applications.

* Added buildable source code for IdP and SP sample applications.

## Java Integration Kit 2.4 – February 2010

* Added token Replay Prevention to the OpenToken IdP Adapter advanced settings.

## Java Integration Kit 2.3 – November 2008

* Added POST transport method for OpenToken when used by an SP.

* Added an option to specify session vs. persistent cookie.

* Added an option to set the `Secure` attribute on an OpenToken when a cookie is used.

* Added ability to bypass password obfuscation and strength enforcement for backward compatibility with previous Java OpenToken agents.

* Improved handling of `null` parameters for single logout via the back-channel (SOAP).

* Empty query string (`?`) is not automatically appended to the URL when redirecting to the Target Resource.

* Target Resource URL is URL-encoded.

## Java Integration Kit 2.2 – June 2008

* Added support for SAML 2.0 isPassive and ForceAuthn.

* Enforced UTF-8 encoding within OpenToken.

* Extended Force Sun JCE Provider option in the OpenToken Adapter to allow compatibility with SafeNet Luna HSM.

* Symmetric key in the OpenToken agent configuration file is encrypted.

* Combined the OpenToken Adapter and OpenToken Java library jar files into a single adapter file for easier deployment to PingFederate.

## Java Integration Kit 2.1 – April 2008

* Added `AgentConfiguration` class to simplify Agent instantiation.

* Added Agent Toolkit API Javadoc.

## Java Integration Kit 2.0 – December 2007

Modified to use an open-standard, secure token called OpenToken to pass user information between an application and PingFederate. The OpenToken is passed through the user's browser as a URL query parameter or an HTTP cookie. The data within the OpenToken is a set of key/value pairs, and the data is encrypted using common encryption algorithms.

## Java Integration Kit 1.3 – November 2007

* Added option to force the use of the Sun Java Cryptography Extension (JCE) on the agent JDK (when necessary to support the SafeNet Luna SA Hardware Security Module) If this option is not selected, the default JCE provider is used, either SunJCE or IBMJCE.

* Modified salt-value generation to correct `PFTOKEN` creation delay on Linux operating systems

* Added support for setting and retrieving multi-value attributes in the SAML assertion

* Added Secure Cookie option which ensures the `PFTOKEN` cookie is sent only on a secure channel

* Added Session Lifetime option to specify the duration (in seconds) for which the token can be reissued without authentication (added for other purposes and has no effect on the Java Integration Kit)

## Java Integration Kit 1.2.1 – August 2007

* Bundled Java sample application with distribution.

* Modified to allow backward compatibility of the Standard Adapter 1.2.1 with PingFederate 4.0.

## Java Integration Kit 1.2 – May 2007

* Added option to encode `PFTOKEN` for handling special characters.

* Added additional constructor to allow `PFTOKEN` to use default properties for all configuration options except password, holder name, and max age.

* Added `PFTOKEN` time stamp information in the log file.

---

---
title: Configuring an OpenToken SP Adapter instance
description: Configure the OpenToken Adapter to determine how PingFederate communicates with your service provider application.
component: java
page_id: java:setup:pf_java_ik_configuring_an_opentoken_sp_adapter_instance
canonical_url: https://docs.pingidentity.com/integrations/java/setup/pf_java_ik_configuring_an_opentoken_sp_adapter_instance.html
revdate: June 21, 2024
section_ids:
  steps: Steps
---

# Configuring an OpenToken SP Adapter instance

Configure the OpenToken Adapter to determine how PingFederate communicates with your service provider application.

## Steps

1. In the PingFederate administrative console, go to **Authentication > Integration > IdP Adapters**. Click **Create new Instance**.

2. On the **Type** tab, set the basic adapter instance attributes.

   1. In the **Instance Name** field, enter a name for the adapter instance.

   2. In the **Instance ID** field, enter a unique identifier for the adapter instance.

   3. In the **Type** list, select **OpenToken Adapter**. Click **Next**.

3. On the **Instance Configuration** tab, configure the adapter instance by referring to [Configuring an OpenToken SP Adapter instance](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_config_opentoken_sp_adapt_instance.html) in the PingFederate documentation. Click **Next**.

   |   |                                                                                                                                                                                                          |
   | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | If you use the application to protect multiple sites on the same domain, in the OpenToken Adapter instance configuration, select **None** for SameSite Cookie and select the **Secure Cookie** checkbox. |

4. Export the configuration file:

   1. On the **Actions** tab, click **Download**, and then click **Export**.

   2. Save the `agent-config.txt` file. Click **Next**.

5. On the **Extended Contract** tab, add any attributes that you expect to retrieve other than the SAML subject. Click **Next**.

6. On the **Target App Info** tab, enter the basic information about your SP application. Click **Next**.

7. On the **Summary** tab, check and save your configuration. Click **Save**.

8. Create or update an identity provider (IdP) connection to use the OpenToken Adapter instance as shown in [Service provider SSO configuration](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_servic_provid_sso_config.html) in the PingFederate documentation.

---

---
title: Custom application setup
description: You can configure the Java Integration Kit to integrate PingFederate with your identity provider (IdP) or service provider (SP) application.
component: java
page_id: java:setup:pf_java_ik_custom_application_setup
canonical_url: https://docs.pingidentity.com/integrations/java/setup/pf_java_ik_custom_application_setup.html
revdate: June 21, 2024
---

# Custom application setup

You can configure the Java Integration Kit to integrate PingFederate with your identity provider (IdP) or service provider (SP) application.

This section includes adapter configuration instructions for PingFederate administrators as well as application configuration instructions for Java developers.

If you want to see a working demonstration of the PingFederate before integrating your own applications, refer to [Sample application setup](pf_java_ik_sample_application_setup.html).

---

---
title: Decoding attributes
description: The readToken method inspects the cookie (or query parameters, depending on the configuration of the agent instance) and decodes the OpenToken, returning a Collection of attributes or null if no token is found or an error is encountered. In the case of an error, a TokenException is thrown.
component: java
page_id: java:setup:pf_java_ik_decoding_attributes
canonical_url: https://docs.pingidentity.com/integrations/java/setup/pf_java_ik_decoding_attributes.html
revdate: June 21, 2024
section_ids:
  sample-code: Sample code
---

# Decoding attributes

The `readToken` method inspects the cookie (or query parameters, depending on the configuration of the agent instance) and decodes the `OpenToken`, returning a `Collection` of attributes or `null` if no token is found or an error is encountered. In the case of an error, a `TokenException` is thrown.

The following example code shows how to use the `readToken` method:

|   |                                                                                                                                                                                   |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | This code is the same for both the Java native and Apache commons multimap methods described in [Reading and writing OpenTokens](pf_java_ik_reading_and_writing_opentokens.html). |

## Sample code

```
try {
   //See the "Reading and writing OpenTokens" topic for sample code
   //that instantiates and configures an Agent instance

Map userInfo = agent.readToken(request);
if(userInfo != null) {
    String username = (String)userInfo.get(Agent.TOKEN_SUBJECT);
}
}
catch(TokenException e) {
   // Handle exception
}
```

---

---
title: Deploy the sample applications
description: The Java Integration Kit includes two applications that act as identity provider (IdP) and service provider (SP) in the demonstration environment. Deploy the applications into the PingFederate servlet container as follows.
component: java
page_id: java:setup:pf_java_ik_deploy_the_sample_applications
canonical_url: https://docs.pingidentity.com/integrations/java/setup/pf_java_ik_deploy_the_sample_applications.html
revdate: June 21, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Deploy the sample applications

The Java Integration Kit includes two applications that act as identity provider (IdP) and service provider (SP) in the demonstration environment. Deploy the applications into the PingFederate servlet container as follows.

## About this task

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | As of Java Integration Kit 2.8, there are two versions of the OpenToken agent: the standard OpenToken agent and the Jakarta EE 9 OpenToken agent. The Jakarta EE 9 OpenToken agent has its own version of the sample applications located in the `/sample/jakarta` folder.- You can only deploy the sample Jakarta applications on servers that support Jakarta EE 9. Currently, PingFederate does not support Jakarta EE 9.

- You shouldn't deploy both versions of the OpenToken agent on the same instance because they need to listen to the same endpoint. |

|   |                                                                                                                                                                                                                                                                               |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | To test a custom configuration, you can deploy the applications in a separate container on your network and then make the necessary configuration changes as described in [Advanced installation and configuration](pf_java_ik_advanced_installation_and_configuration.html). |

## Steps

1. Stop PingFederate.

2. From the Java Integration Kit `.zip` archive, copy the `sample/IdpSample.war` and `sample/SpSample.war` files to `<pf_install>/pingfederate/server/default/deploy`.

3. Start PingFederate.

---

---
title: Deploying the applications to separate servlet containers
description: This configuration requires some familiarity with web-application deployment and the target-container configuration, as well as SSL certificate management.
component: java
page_id: java:setup:pf_java_ik_deploying_the_applications_to_separate_servlet_containers
canonical_url: https://docs.pingidentity.com/integrations/java/setup/pf_java_ik_deploying_the_applications_to_separate_servlet_containers.html
revdate: June 21, 2024
---

# Deploying the applications to separate servlet containers

|   |                                                                                                                                                             |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | This configuration requires some familiarity with web-application deployment and the target-container configuration, as well as SSL certificate management. |

You can deploy either or both of the sample applications into their own servlet containers (such as Tomcat), rather than the container running PingFederate. If you do this, you'll need to update the URLs indicated under [Manual configuration settings](pf_java_ik_manual_configuration_settings.html).

You might also need to update the Trusted CAs in PingFederate with the container's SSL server certificate, depending on the container's SSL configuration, and ensure the container server trusts the PingFederate certificate.

|   |                                                                                                                                                                                                                                                                                                                                                                                          |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | If you deploy either application in a separate container, update the PingFederate server hostname in the associated sample application, as shown in [IdP sample application configuration reference](pf_java_ik_idp_sample_application_configuration_reference.html) and [SP sample application configuration reference](pf_java_ik_sp_sample_application_configuration_reference.html). |

---

---
title: Deploying the Java agent
description: If you are upgrading this integration, we strongly recommend that you reinstall the OpenToken agent in all existing applications (IdP or SP).
component: java
page_id: java:setup:pf_java_ik_deploying_the_java_agent
canonical_url: https://docs.pingidentity.com/integrations/java/setup/pf_java_ik_deploying_the_java_agent.html
revdate: June 21, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
  choose-from: Choose from:
  choose-from-2: Choose from:
---

# Deploying the Java agent

## About this task

If you are upgrading this integration, we strongly recommend that you reinstall the OpenToken agent in all existing applications (IdP or SP).

|   |                                                                                                                                                   |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | As of Java Integration Kit 2.8, there are two versions of the OpenToken agent: the standard OpenToken agent and the Jakarta EE 9 OpenToken agent. |

## Steps

1. If you are upgrading this integration:

   1. Stop your web application.

   2. Remove the existing OpenToken agent file from your Java application server:

      ### Choose from:

      * If you're using the standard OpenToken agent, remove the `opentoken-agent-<version>.jar` from the `agent` folder.

      * If you're using the Jakarta EE 9 OpenToken agent, remove the `opentoken-agent-jakarta-<version>.jar` from the `agent/jakarta` folder

        |   |                                                                  |
        | - | ---------------------------------------------------------------- |
        |   | No code changes are required within applications when upgrading. |

2. From the integration `.zip` archive, copy the version-specific `agent/opentoken-agent-<version>.jar` file to your Java application server and make it available in the `CLASSPATH` of the Java application:

   ### Choose from:

   * If you're using the OpenToken agent, copy the `agent/opentoken-agent-<version>.jar` file.

   * If you're using the Jakarta EE 9 OpenToken agent, copy the `agent/jakarta/``opentoken-agent-jakarta-<version>.jar` file.

3. From the integration `.zip` archive, copy the necessary library file or files to your Java application server and make them available in the `CLASSPATH` of the Java application:

   | Option                           | Description                                                                                                                                     |
   | -------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
   | **Standard OpenToken agent**     | * `agent/lib/commons-beanutils.jar`\*

   * `agent/lib/commons-collections-3.2.2.jar`\*

   * `agent/lib/commons-logging.jar`                         |
   | **Jakarta EE 9 OpenToken agent** | - `agent/jakarta/lib/commons-beanutils.jar`\*

   - `agent/jakarta/lib/commons-collections-3.2.2.jar`\*

   - `agent/jakarta/lib/commons-logging.jar` |

   |   |                                                                                                                                            |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------ |
   |   | Files marked with an asterisk (`*`) are only necessary if you are using the Apache commons multimap function to read and write OpenTokens. |

4. If you are upgrading, restart your web application.

5. Repeat these steps as needed for additional custom applications.

   For a first-time installation, complete the integration as described in [Reading and writing OpenTokens](pf_java_ik_reading_and_writing_opentokens.html) (next) and in either [Identity provider applications](pf_java_ik_identity_provider_applications.html) or [Service provider applications](pf_java_ik_service_provider_applications.html).

---

---
title: Deploying the sample configuration archive
description: The data.zip archive configures a PingFederate to work with the sample applications.
component: java
page_id: java:setup:pf_java_ik_deploying_the_sample_configuration_archive
canonical_url: https://docs.pingidentity.com/integrations/java/setup/pf_java_ik_deploying_the_sample_configuration_archive.html
revdate: June 21, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
  result: Result:
---

# Deploying the sample configuration archive

The `data.zip` archive configures a PingFederate to work with the sample applications.

## About this task

In this configuration, a single instance of PingFederate serves both the identity provider (IdP) and service provider (SP) roles by sending messages to and from itself. Although this is a valid scenario for demonstration and testing, it is not applicable to a real situation.

For a more realistic test, you can deploy the configurations into instances of PingFederate running on different hosts and then make necessary configuration updates manually as shown in [Advanced installation and configuration](pf_java_ik_advanced_installation_and_configuration.html).

|   |                                                                                                                                                                                                         |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Deploying `data.zip` overwrites your entire PingFederate configuration. If you have configured adapters, data stores, partner connections, or any other settings, back up your configuration in step 2. |

## Steps

1. Start PingFederate.

2. Back up your current PingFederate configuration as shown in [Configuration archive](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_configurationarchivetasklet_selectimportexportstate.html) in the PingFederate documentation.

3. From the Java Integration Kit `.zip` archive, copy the `sample/data.zip` archive to `<pf_install>/pingfederate/server/default/data/drop-in-deployer/`.

   ### Result:

   PingFederate adopts the new configuration and renames the `data.zip` file with a time stamp.

---

---
title: Download manifest
description: The following files are included in the Java Integration Kit:
component: java
page_id: java:release_notes:pf_java_ik_download_manifest
canonical_url: https://docs.pingidentity.com/integrations/java/release_notes/pf_java_ik_download_manifest.html
revdate: June 21, 2024
---

# Download manifest

The following files are included in the Java Integration Kit:

* `Legal.pdf`: Copyright and license information.

* `agent`: Contains the OpenToken Agent and supporting libraries.

  * `opentoken-agent-<version>.jar`: A JAR file that contains the OpenToken Agent.

  * `lib`: Contains the libraries needed by the OpenToken Agent.

    * `commons-beanutils.jar`: The Apache Commons Bean Utility library.

    * `commons-collections-3.2.2.jar`: The Apache Commons Collections library.

    * `commons-logging.jar`: The Apache Commons Logging library.

  * `jakarta`: Contains the OpenToken Agent and supporting libraries using Jakarta EE 9.

    * `opentoken-agent-jakarta-<version>.jar`: A JAR file that contains the OpenToken Agent.

    * `lib`: Contains the libraries needed by the OpenToken Agent.

      * `commons-beanutils.jar`: The Apache Commons Bean Utility library.

      * `commons-collections-3.2.2.jar`: The Apache Commons Collections library.

      * `commons-logging.jar`: The Apache Commons Logging library.

* `dist/pingfederate/server/default`: Contains the integration files.

  * `deploy`: Contains the Java libraries.

    * `opentoken-adapter-<version>.jar`: JAR file that contains the OpenToken Adapter.

* `/docs/javadoc`: Contains the Agent Toolkit API Javadoc.

* `/sample`: Contains sample applications for testing the adapter.

  * `data.zip`: PingFederate configuration archive for the sample applications.

  * `/IdpSample.war`: Extracted WAR directory for the IdP sample application.

  * `/SpSample.war`: Extracted WAR directory for the SP sample application.

  * `/jakarta`: Contains the Jakarta EE 9 based sample applications for testing the adapter.

    * `/IdpSample.war`: Extracted WAR directory for the IdP sample application.

    * `/SpSample.war`: Extracted WAR directory for the SP sample application.

* `/sample_src`

  * `/idp`: Source code and supporting files for the IdP sample application.

  * `/sp`: Source code and supporting files for the SP sample application.

  * `/jakarta`: Contains the source code and supporting files for the IdP and SP sample applications for Jakarta EE 9.

    * `/idp`: Source code and supporting files for the IdP sample application for Jakarta EE 9.

    * `/sp`: Source code and supporting files for the SP sample application for Jakarta EE 9.

---

---
title: Encoding attributes
description: The writeToken method of the Agent class takes a java.util.Map collection of attributes and encodes them into an OpenToken, which is then written to the HTTP response.
component: java
page_id: java:setup:pf_java_ik_encoding_attributes
canonical_url: https://docs.pingidentity.com/integrations/java/setup/pf_java_ik_encoding_attributes.html
revdate: June 21, 2024
section_ids:
  sample-code: Sample code
---

# Encoding attributes

The `writeToken` method of the Agent class takes a `java.util.Map` collection of attributes and encodes them into an OpenToken, which is then written to the HTTP response.

|   |                                                                                             |
| - | ------------------------------------------------------------------------------------------- |
|   | To generate a valid token, the collection of attributes must contain a key named `subject`. |

If any errors are encountered while creating the token or writing the token out to the response, a `TokenException` is thrown.

The following example code shows how to use the writeToken method:

|   |                                                                                                                                                                                   |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | This code is the same for both the Java native and Apache commons multimap methods described in [Reading and writing OpenTokens](pf_java_ik_reading_and_writing_opentokens.html). |

## Sample code

```
String username = (String)request.getSession().getAttribute("username");
Map<String, String> userInfo = new HashMap<String, String>();
userInfo.put(Agent.TOKEN_SUBJECT, username);
String returnUrl = "https://<PingFederate-DNS>:9031" + request.getParameter("resume");
. . . .
try {
   UrlHelper urlHelper = new UrlHelper(returnUrl);
   //See the "Reading and writing OpenTokens" topic for sample code
   //that instantiates and configures an Agent instance
   agent.writeToken(userInfo,response,urlHelper,false);
   returnUrl = (String)urlHelper.toString();
}
catch(TokenException e) {
// Handle exception
}
```

---

---
title: Identity provider applications
description: You can use the Java Integration Kit to integrate your identity provider (IdP) application with PingFederate for single sign-on (SSO) and single logout (SLO). This section provides implementation guidelines and code examples for Java developers.
component: java
page_id: java:setup:pf_java_ik_identity_provider_applications
canonical_url: https://docs.pingidentity.com/integrations/java/setup/pf_java_ik_identity_provider_applications.html
revdate: June 21, 2024
---

# Identity provider applications

You can use the Java Integration Kit to integrate your identity provider (IdP) *(tooltip: \<div class="paragraph">
\<p>A service that manages identity information and provides authentication services to relying clients or SPs within a federated or distributed network.\</p>
\</div>)* application with PingFederate for single sign-on (SSO) *(tooltip: \<div class="paragraph">
\<p>The process of authenticating an identity (signing on) at one website (usually with a user ID and password) and then accessing resources secured by other domains without reauthenticating.\</p>
\</div>)* and single logout (SLO) *(tooltip: \<div class="paragraph">
\<p>The process of signing a user out of multiple sites where the user has started a SSO session.\</p>
\</div>)*. This section provides implementation guidelines and code examples for Java developers.

---

---
title: IdP sample application configuration reference
description: The sample applications automatically work with PingFederate configuration you deployed in Deploying the sample configuration archive. However, if you want to test your own deployment and sign-on scenarios, customize the sample application settings as follows:
component: java
page_id: java:setup:pf_java_ik_idp_sample_application_configuration_reference
canonical_url: https://docs.pingidentity.com/integrations/java/setup/pf_java_ik_idp_sample_application_configuration_reference.html
revdate: June 21, 2024
---

# IdP sample application configuration reference

The sample applications automatically work with PingFederate configuration you deployed in [Deploying the sample configuration archive](pf_java_ik_deploying_the_sample_configuration_archive.html). However, if you want to test your own deployment and sign-on scenarios, customize the sample application settings as follows:

| Field                         | Description                                                                                                                                                               |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **PF Base URL**               | The fully qualified host name, port, and path of the PingFederate server.The default value is `https://localhost:9031/`.                                                  |
| **SP Connections**            | The ID of the service provider (SP) connection to use.Separate multiple connection IDs with a pipe `\|` character.The default value is `localhost:default:entityId`.      |
| **IdP Adapter Instances**     | The ID of the OpenToken Adapter instance to use.Separate multiple adapter IDs with a pipe `\|` character.The default value is `OTPIdPJava`.                               |
| **Attribute Names List**      | Single and multi-value attributes to include in the assertion.Separate multiple attribute names with a pipe `\|` character.The default value is `password\|authnContext`. |
| **IdP OpenToken Config File** | If you customized the OpenToken Adapter configuration provided by the sample deployment, export the `agent-config.txt` file from it, then upload the file here.           |

---

---
title: IdP single logout (SLO)
description: When an IdP PingFederate server receives a request for single logout (SLO), it redirects the user's browser to the logout service defined in the IdP OpenToken Adapter configuration.
component: java
page_id: java:setup:pf_java_ik_idp_single_logout_slo
canonical_url: https://docs.pingidentity.com/integrations/java/setup/pf_java_ik_idp_single_logout_slo.html
revdate: June 21, 2024
section_ids:
  sequence: Sequence
---

# IdP single logout (SLO)

When an IdP PingFederate server receives a request for single logout (SLO), it redirects the user's browser to the logout service defined in the IdP OpenToken Adapter configuration.

The redirect URL includes an OpenToken containing the user attributes defined in the IdP OpenToken Adapter instance for the partner connection. The logout service should remove the user's session on the application server and redirect the user's browser back to the IdP PingFederate server.

The following diagram shows the flow of IdP-initiated SLO, but the architecture would also support SP-initiated SLO:

![tzt1563995426491](_images/tzt1563995426491.jpg)

## Sequence

1. User initiates a single logout request. The request targets the PingFederate server's `/idp/startSLO.ping` endpoint.

2. PingFederate sends a logout requests and receives responses for all SPs registered for the current SSO session.

3. If the application server has an SLO service configured, PingFederate redirects the request to the SLO service, which identifies and removes the user's session locally.

4. The application logout service redirects back to PingFederate to display a sign-off success page.

   If the web application doesn't have an SLO service configured, the adapter redirects back to PingFederate, which displays a sign-off success page.

---

---
title: IdP single sign-on (SSO)
description: When PingFederate is configured as an IdP, it needs to be able to identify a user before issuing a SAML assertion for that user. When using the OpenToken Adapter with PingFederate, this means that the PingFederate server attempts to read a cookie or query parameter containing an OpenToken and then use the values within to identify the user.
component: java
page_id: java:setup:pf_java_ik_idp_single_sign_on_sso
canonical_url: https://docs.pingidentity.com/integrations/java/setup/pf_java_ik_idp_single_sign_on_sso.html
revdate: June 21, 2024
---

# IdP single sign-on (SSO)

When PingFederate is configured as an IdP, it needs to be able to identify a user before issuing a SAML assertion for that user. When using the OpenToken Adapter with PingFederate, this means that the PingFederate server attempts to read a cookie or query parameter containing an OpenToken and then use the values within to identify the user.

The application that starts the SSO must include an OpenToken so that PingFederate can identify the user. Use the Agent API to write an OpenToken. The API is a Java object that provides access to functionality for writing an OpenToken to a given HTTP response.

---

---
title: Java Integration Kit
description: The Java Integration Kit allows PingFederate to integrate with identity provider (IdP) and service provider (SP) applications for single sign-on (SSO).
component: java
page_id: java::pf_java_ik
canonical_url: https://docs.pingidentity.com/integrations/java/pf_java_ik.html
revdate: June 21, 2024
section_ids:
  components: Components
  intended-audience: Intended audience
  system-requirements: System requirements
---

# Java Integration Kit

The Java Integration Kit allows PingFederate to integrate with identity provider (IdP) *(tooltip: \<div class="paragraph">
\<p>A service that manages identity information and provides authentication services to relying clients or SPs within a federated or distributed network.\</p>
\</div>)* and service provider (SP) *(tooltip: \<div class="paragraph">
\<p>In SAML, an entity that receives and accepts an authentication assertion issued by an IdP, typically for the purpose of allowing access to a protected resource.\</p>
\</div>)* applications for single sign-on (SSO) *(tooltip: \<div class="paragraph">
\<p>The process of authenticating an identity (signing on) at one website (usually with a user ID and password) and then accessing resources secured by other domains without reauthenticating.\</p>
\</div>)*.

|   |                                                                                                                                                                                                                                                           |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | For new integrations, try the [Agentless Integration Kit](../agentless/pf_agentless_ik.html). It can integrate with a variety of platforms using a modern RESTful approach, and it doesn't require you to integrate agent software into your application. |

## Components

OpenToken adapter and agent

* Allows developers to integrate their Java applications with a PingFederate server acting as an IdP or an SP:

  * On the IdP side, the integration kit allows an IdP server to receive user attributes from a Java IdP application.

  * On the SP side, the integration kit allows a Java SP application to receive user attributes from the SP server.

Sample applications

* The Integration Kit distribution also contains sample IdP and SP applications. These applications can be installed quickly to test OpenToken processing and review a working demonstration of end-to-end SSO and single logout (SLO) *(tooltip: \<div class="paragraph">
  \<p>The process of signing a user out of multiple sites where the user has started a SSO session.\</p>
  \</div>)*.

  The distribution includes source code and supporting files that application developers can modify or use as a reference.

## Intended audience

This document is intended for PingFederate administrators.

If you need help during the setup process, you can find more information in the following sections of the PingFederate documentation:

* [Managing IdP adapters](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_managing_idp_adapters.html)

* [Managing SP adapters](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_adaptermanagementtasklet_spadaptermanagementstate.html)

* [Authentication policies](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_authentication_policies.html)

* [OpenToken Adapter](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_opentoken_adapt.html)

## System requirements

* PingFederate 11.3 or later.

* Java SE Runtime Environment 1.8 or later on the agent side

* To use strong Advanced Encryption Standard (AES) encryption with a key size of more than 128 bits, you must install the Java Cryptography Extension (JCE) Unlimited Strength Jurisdiction Policy Files in your Java Development Kit (JDK) *(tooltip: \<div class="paragraph">
  \<p>A development environment for building applications and components using Java.\</p>
  \</div>)*.

---

---
title: JSPs and web page components
description: You can modify the JSPs, images, and cascading style sheets (CSSs) to customize the look and feel of the installed sample applications.
component: java
page_id: java:setup:pf_java_ik_jsps_and_web_page_components
canonical_url: https://docs.pingidentity.com/integrations/java/setup/pf_java_ik_jsps_and_web_page_components.html
revdate: June 21, 2024
---

# JSPs and web page components

You can modify the JSPs, images, and cascading style sheets (CSSs) to customize the look and feel of the installed sample applications.

* The JSP files are located in the following directories in the Java Integration Kit distribution:

  `sample_src/<sample>/webapp/WEB-INF/jsp`

  where *\<sample>* is either idp or sp

* Images and CSS files are located in:

  `sample_src/<sample>/webapp/images`

---

---
title: Known issues and limitations
description: The following are known issues or limitations with the Java Integration Kit.
component: java
page_id: java:release_notes:pf_java_ik_known_issues_and_limitations
canonical_url: https://docs.pingidentity.com/integrations/java/release_notes/pf_java_ik_known_issues_and_limitations.html
revdate: June 21, 2024
section_ids:
  known-issues: Known issues
  known-limitations: Known limitations
---

# Known issues and limitations

The following are known issues or limitations with the Java Integration Kit.

## Known issues

There are no known issues.

## Known limitations

* The user interface doesn't enforce this, but the adapter instance's `Token Name` field must be unique within a federation.

* Multi-value attributes fail if the SP adapter sends extended attributes as cookies because multiple cookies with the same name aren't allowed.

* When running the sample applications in a separate container, the back-channel web-SSO directory service fails unless the certificate is trusted by the JDK. As a result, the sample applications won't list available partners to SSO in the list.

  To get around this limitation, import the certificate into the JDK or web container's trusted certificate authority (CA) *(tooltip: \<div class="paragraph">
  \<p>An entity that issues digital certificates.\</p>
  \</div>)* store or use HTTP instead.

* Support for UTF-8 encoding is limited to the sample applications and the attributes displayed. UTF-8 encoded usernames, passwords, and token names for the OpenToken configuration, SSO Directory Service configuration, and sample application configuration are not supported.

* The Java Integration Kit isn't compliant with FIPS-140 cryptographic standards. By forcing the Sun JCE to be used in the adapter, keys aren't stored in the hardware security module (HSM) *(tooltip: \<div class="paragraph">
  \<p>A dedicated cryptographic processor designed to manage and protect digital keys. HSMs act as trust anchors that protect the cryptographic key lifecycle by securely managing, processing, and storing cryptographic keys inside a hardened, tamper-resistant device.\</p>
  \</div>)*.

---

---
title: Manual configuration settings
description: Instead of using the sample data.zip archive from the Java Integration Kit package (see Deploying the sample configuration archive), you can configure PingFederate manually.
component: java
page_id: java:setup:pf_java_ik_manual_configuration_settings
canonical_url: https://docs.pingidentity.com/integrations/java/setup/pf_java_ik_manual_configuration_settings.html
revdate: June 21, 2024
section_ids:
  identity-provider-adapter-instance-settings: Identity provider adapter instance settings
  service-provider-adapter-instance-settings: Service provider adapter instance settings
  service-provider-default-urls: Service provider default URLs
---

# Manual configuration settings

Instead of using the sample `data.zip` archive from the Java Integration Kit package (see [Deploying the sample configuration archive](pf_java_ik_deploying_the_sample_configuration_archive.html)), you can configure PingFederate manually.

|   |                                                                                                                                                                                                         |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | If you have a difficult time with the manual configuration, deploy the sample `data.zip` file. Then you can refer to the sample configuration as you create your own adapter instances and connections. |

The following tables list the required adapter settings for the Java sample applications.

## Identity provider adapter instance settings

Refer to the **IdP Adapter** tab of the identity provider adapter configuration.

| Field Name                 | Value                                                                                                                                                                                                                                                                                                                                                                                           |
| -------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Password**               | Must be six characters long and contain at least:- One uppercase letter

- One lowercase letter

- One numberThis password is included in the `agent-config.txt` file used by the application. It doesn't have to match the password you choose for the service provider adapter instance.&#xA;&#xA;The sample applications are preconfigured to use the following password:&#xA;&#xA;Changeme1 |
| **Authentication Service** | https\://*\<pf\_host>*:*\<pf\_port>*/IdpSample/MainPage?cmd=sso                                                                                                                                                                                                                                                                                                                                 |
| **Advanced Fields**        |                                                                                                                                                                                                                                                                                                                                                                                                 |
| **Logout Service**         | https\://*\<pf\_host>*:*\<pf\_port>*/IdpSample/MainPage?cmd=slo                                                                                                                                                                                                                                                                                                                                 |

|   |                                                                                                                                                                                                                                                                                                                                                                                    |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The endpoints in these tables assume you deployed the sample applications in the same servlet container as PingFederate. If you deployed the applications elsewhere, change the hostname (`localhost`) and port accordingly. Learn more in [Deploying the applications to separate servlet containers](pf_java_ik_deploying_the_applications_to_separate_servlet_containers.html). |

## Service provider adapter instance settings

Refer to the **Instance Configuration** tab of the service provider adapter instance configuration.

| Field Name                          | Value                                                                                                                                                                                                                                                                                                                                                                                            |
| ----------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Password**                        | Must be six characters long and contain at least:- One uppercase letter

- One lowercase letter

- One numberThis password is included in the `agent-config.txt` file used by the application. It doesn't have to match the password you choose for the identity provider adapter instance.&#xA;&#xA;The sample applications are preconfigured to use the following password:&#xA;&#xA;Changeme1 |
| **Advanced Fields**                 |                                                                                                                                                                                                                                                                                                                                                                                                  |
| **Account Link Service** (Optional) | https\://*\<pf\_host>*:*\<pf\_port>*/SpSample/MainPage?cmd=accountlink                                                                                                                                                                                                                                                                                                                           |
| **Logout Service**                  | https\://*\<pf\_host>*:*\<pf\_port>*/SpSample/MainPage?cmd=slo                                                                                                                                                                                                                                                                                                                                   |

## Service provider default URLs

See the **Default URLs** tab of the service provider configuration.

| Field       | Value                                                   |
| ----------- | ------------------------------------------------------- |
| For SSO URL | https\://*\<pf\_host>*:*\<pf\_port>*/SpSample/MainPage/ |
| For SLO URL | https\://*\<pf\_host>*:*\<pf\_port>*/SpSample/MainPage/ |

---

---
title: Modifying sample source files
description: The Java Integration Kit distribution provides the source files for the sample applications in the sample_src directory, including Java code and supporting JSPs, images, style sheets and other components.
component: java
page_id: java:setup:pf_java_ik_modifying_sample_source_files
canonical_url: https://docs.pingidentity.com/integrations/java/setup/pf_java_ik_modifying_sample_source_files.html
revdate: June 21, 2024
section_ids:
  jsps-and-web-page-components: JSPs and web page components
  rebuilding-the-sample-applications: Rebuilding the sample applications
  about-this-task: About this task
  steps: Steps
---

# Modifying sample source files

The Java Integration Kit distribution provides the source files for the sample applications in the `sample_src` directory, including Java code and supporting JSPs, images, style sheets and other components.

Developers can use these files to change the appearance and behavior of the samples, create different samples for testing, or develop actual prototypes for production purposes. In addition, the commented Java code is engineered into discrete classes and methods that can be repurposed to work with existing web applications.

This section further identifies the source file directories and describes how to rebuild the sample applications, as a means of highlighting file locations and build scripts that developers could use for other customizing purposes.

## JSPs and web page components

You can modify the JSPs, images, and cascading style sheets (CSSs) to customize the look and feel of the installed sample applications.

* The JSP files are located in the following directories in the Java Integration Kit distribution:

  `sample_src/<sample>/webapp/WEB-INF/jsp`

  where *\<sample>* is either idp or sp

* Images and CSS files are located in:

  `sample_src/<sample>/webapp/images`

## Rebuilding the sample applications

As a Java developer, you can make changes to the source code for any of the sample applications for your own needs.

### About this task

The source code for the sample applications is located in `sample_src/<sample>/java`.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | As of Java Integration Kit 2.8, there are two versions of the OpenToken agent: the standard OpenToken agent and the Jakarta EE 9 OpenToken agent. The Jakarta EE 9 OpenToken agent has its own version of the sample applications. The source code for the Jakarta EE 9 sample applications is located in the `jakarta/idp` and `jakarta/sp` files.You can only deploy the sample Jakarta applications on servers that support Jakarta EE 9, such as Tomcat 10.1. Currently, PingFederate does not support Jakarta EE 9. |

After you modify the source code, you can build and repackage the application using `ant` commands executed from the `<sample>` directory for the `build.xml` file included in that directory. You can package either another WAR directory or a compressed WAR file (depending on deployment needs) using the following commands:

|   |                                                                                                                                                                                                                                                                                                                                                                          |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | For backward compatibility, the `build.xml` configuration file is set to use version 1.5 of the Java Development Kit (JDK) *(tooltip: \<div class="paragraph">&#xA;\<p>A development environment for building applications and components using Java.\</p>&#xA;\</div>)*. To recompile using the current JDK version, change the version number in the `build.xml` file. |

### Steps

1. Create a WAR directory. From the `<sample>` directory, enter:

   ```
   ant
   ```

2. Create a WAR file. From the `<sample>` directory, enter:

   ```
   ant war
   ```