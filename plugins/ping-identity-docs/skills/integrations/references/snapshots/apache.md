---
title: Apache Agent setup
description: To set up the Apache agent, you must copy a configuration file and a library from the extracted integration-kit distribution to your Apache installation and then modify the configuration file.
component: apache
page_id: apache:setup:pf_apache_linux_ik_agent_setup
canonical_url: https://docs.pingidentity.com/integrations/apache/setup/pf_apache_linux_ik_agent_setup.html
llms_txt: https://docs.pingidentity.com/integrations/apache/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: February 8, 2022
---

# Apache Agent setup

To set up the Apache agent, you must copy a configuration file and a library from the extracted integration-kit distribution to your Apache installation and then modify the configuration file.

|   |                                                                            |
| - | -------------------------------------------------------------------------- |
|   | The Apache agent setup is required for new installations and for upgrades. |

---

---
title: Apache Linux Integration Kit
description: The Apache Linux Integration Kit allows PingFederate to coordinate user authentication and single sign-on (SSO) between an Apache web application and an identity provider (IdP).
component: apache
page_id: apache::pf_apache_linux_ik
canonical_url: https://docs.pingidentity.com/integrations/apache/pf_apache_linux_ik.html
llms_txt: https://docs.pingidentity.com/integrations/apache/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 27, 2024
section_ids:
  components: Components
  intended-audience: Intended audience
  system-requirements: System requirements
---

# Apache Linux Integration Kit

The Apache Linux Integration Kit allows PingFederate to coordinate user authentication and single sign-on (SSO) *(tooltip: \<div class="paragraph">
\<p>The process of authenticating an identity (signing on) at one website (usually with a user ID and password) and then accessing resources secured by other domains without reauthenticating.\</p>
\</div>)* between an Apache web application and an identity provider (IdP) *(tooltip: \<div class="paragraph">
\<p>A service that manages identity information and provides authentication services to relying clients or SPs within a federated or distributed network.\</p>
\</div>)*.

|   |                                                                                                                                                                                                                                                           |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | For new integrations, try the [Agentless Integration Kit](../agentless/pf_agentless_ik.html). It can integrate with a variety of platforms using a modern RESTful approach, and it doesn't require you to integrate agent software into your application. |

## Components

* OpenToken Adapter

  Installed in PingFederate, this adapter uses the secure OpenToken standard to pass user attributes and session information from PingFederate to the Apache agent on the Apache server.

* Apache agent

  Installed on the server running Apache, this program watches for protected resource requests and determines whether to grant access or redirect the user to PingFederate for authentication with an IdP.

## Intended audience

This document is intended for PingFederate administrators.

Learn more about the setup process in the following sections of the PingFederate documentation:

* [Managing SP adapters](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_adaptermanagementtasklet_spadaptermanagementstate.html)

* [Configuring an OpenToken SP Adapter instance](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_config_opentoken_sp_adapt_instance.html)

## System requirements

* PingFederate 11.3 or later

* OpenSSL 1.1.1 or later

The Apache agent supports the following platforms:

* Apache HTTP Server 2.4:

  * Red Hat Enterprise Linux:

    * Red Hat Enterprise Linux 7

    * Red Hat Enterprise Linux 8

    * Red Hat Enterprise Linux 9

  * Canonical Ubuntu:

    * Canonical Ubuntu 18.04

    * Canonical Ubuntu 20.04

    * Canonical Ubuntu 22.04

    * Canonical Ubuntu 24.04

---

---
title: Changelog
description: The following is the change history for the Apache Linux Integration Kit.
component: apache
page_id: apache:release_notes:pf_apache_linux_ik_changelog
canonical_url: https://docs.pingidentity.com/integrations/apache/release_notes/pf_apache_linux_ik_changelog.html
llms_txt: https://docs.pingidentity.com/integrations/apache/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 27, 2024
section_ids:
  apache-linux-integration-kit-4-2-january-2025: Apache Linux Integration Kit 4.2 – January 2025
  apache-linux-integration-kit-4-1-1-august-2022: Apache Linux Integration Kit 4.1.1 – August 2022
  apache-linux-integration-kit-4-1-june-2022: Apache Linux Integration Kit 4.1 – June 2022
  apache-linux-integration-kit-4-0-january-2022: Apache Linux Integration Kit 4.0 – January 2022
  apache-linux-integration-kit-3-3-5-november-2021: Apache Linux Integration Kit 3.3.5 – November 2021
  apache-linux-integration-kit-3-3-4-september-2020: Apache Linux Integration Kit 3.3.4 – September 2020
  apache-linux-integration-kit-3-3-3-january-2020: Apache Linux Integration Kit 3.3.3 – January 2020
  apache-linux-integration-kit-3-3-2-july-2018: Apache Linux Integration Kit 3.3.2 – July 2018
  apache-linux-integration-kit-3-3-1-february-2018: Apache Linux Integration Kit 3.3.1 – February 2018
  apache-linux-integration-kit-3-3-july-2017: Apache Linux Integration Kit 3.3 – July 2017
  apache-linux-integration-kit-3-2-1-february-2017: Apache Linux Integration Kit 3.2.1 – February 2017
  apache-linux-integration-kit-3-2-january-2017: Apache Linux Integration Kit 3.2 – January 2017
  apache-linux-integration-kit-3-1-june-2016: Apache Linux Integration Kit 3.1 – June 2016
  apache-linux-integration-kit-3-1-april-2015: Apache Linux Integration Kit 3.1 – April 2015
  apache-linux-integration-kit-3-0-1-december-2014: Apache Linux Integration Kit 3.0.1 – December 2014
  apache-linux-integration-kit-3-0-may-2014: Apache Linux Integration Kit 3.0 – May 2014
  apache-linux-integration-kit-2-4-1-june-2013: Apache Linux Integration Kit 2.4.1 – June 2013
  apache-linux-integration-kit-2-3-6-march-2013: Apache Linux Integration Kit 2.3.6 – March 2013
  apache-linux-integration-kit-2-3-1-december-2012: Apache Linux Integration Kit 2.3.1 – December 2012
  apache-linux-integration-kit-2-3-december-2011: Apache Linux Integration Kit 2.3 – December 2011
  apache-linux-integration-kit-2-2-1-february-2010: Apache Linux Integration Kit 2.2.1 – February 2010
  apache-linux-integration-kit-2-2-september-2009: Apache Linux Integration Kit 2.2 – September 2009
  apache-linux-integration-kit-2-1-march-2009: Apache Linux Integration Kit 2.1 – March 2009
  apache-linux-integration-kit-2-0-november-2008: Apache Linux Integration Kit 2.0 – November 2008
  apache-linux-integration-kit-1-1-october-2008: Apache Linux Integration Kit 1.1 – October 2008
  apache-linux-integration-kit-1-0-september-2007: Apache Linux Integration Kit 1.0 – September 2007
---

# Changelog

The following is the change history for the Apache Linux Integration Kit.

## Apache Linux Integration Kit 4.2 – January 2025

* Added support for:

  * Red Hat Enterprise Linux 9

  * Canonical Ubuntu 22.04

  * Canonical Ubuntu 24.04

## Apache Linux Integration Kit 4.1.1 – August 2022

* Fixed an issue that could cause errors with specific string lengths for the cookie name.

## Apache Linux Integration Kit 4.1 – June 2022

* Reimplemented fragment preservation with a new approach.

## Apache Linux Integration Kit 4.0 – January 2022

* Added support for:

  * Red Hat Enterprise Linux 8

  * Canonical Ubuntu 18.04

  * Canonical Ubuntu 20.04

* Ended support for:

  * Red Hat Enterprise Linux 6

  * Canonical Ubuntu 14.04

  * Canonical Ubuntu 16.10

* Updated OpenSSL version to 1.1.1 for Red Hat Enterprise Linux 7.

* Improved redirect handling. When users are redirected back from PingFederate after a flow, the Apache Linux Integration Kit agent can now preserve fragments in the URI, such as `#MyHomePage`. You can enable this behavior with the **PingFederateEnableFragmentPreservation** setting in the `mod_pf.conf` file.

## Apache Linux Integration Kit 3.3.5 – November 2021

* Improved the way the adapter handles browser cookie attributes and expired cookies.

* Removed the OpenToken Adapter from the `.zip` archive. The latest version is available in the Java Integration Kit. Learn more in [Updating the OpenToken Adapter](../setup/pf_apache_linux_ik_updating_the_opentoken_adapter.html).

* Changed to a standardized `.zip` file structure to make automated deployments easier.

## Apache Linux Integration Kit 3.3.4 – September 2020

* Fixed an issue that could insert bad characters into legacy cookie names.

## Apache Linux Integration Kit 3.3.3 – January 2020

* Added support for the `SameSite` cookie flag in web browsers.

## Apache Linux Integration Kit 3.3.2 – July 2018

* Added the ability to read cookie HTTP request header case insensitively.

* Removed module info from the Server HTTP response header.

## Apache Linux Integration Kit 3.3.1 – February 2018

* Added support for the Amazon Web Services Application Load Balancer.

* Fixed a URL encoding issue with special characters.

## Apache Linux Integration Kit 3.3 – July 2017

* Removed support for Red Hat Enterprise Linux 5.

* Improved query parameter encoding.

* Improved cookie name parsing.

## Apache Linux Integration Kit 3.2.1 – February 2017

* Fixed an issue with retrieving the session token.

## Apache Linux Integration Kit 3.2 – January 2017

* Added the ability to encode query parameters.

* Added the ability to disable virtual hosts by port value.

* Added support for Ubuntu 16.10.

* Added support for the `HttpOnly` flag on cookies. `HttpOnly` prevents the cookie from being intercepted or manipulated. This mitigates a significant portion of vulnerabilities, such as cross-site scripting (XSS), to which the cookie would otherwise be susceptible. This ensures the Apache agent's behavior and security considerations are consistent with behavior for other adapters and agents. You can control this behavior with the `PingFederateCookieHttpOnly` setting in the `mod_pf.conf` file.

* Bug fixes.

## Apache Linux Integration Kit 3.1 – June 2016

* Added support for Oracle HTTP Server.

## Apache Linux Integration Kit 3.1 – April 2015

* Added support for Apache 2.2 on Red Hat Enterprise Linux 5.0 (64-bit).

* Optimized OpenToken lookup.

* Fixed a security vulnerability.

## Apache Linux Integration Kit 3.0.1 – December 2014

* Added Apache 2.4 support for Red Hat Enterprise Linux 7.0 and Ubuntu 14.04.

* Fixed an issue that caused the Apache agent to handle directories containing spaces improperly.

## Apache Linux Integration Kit 3.0 – May 2014

* Added support for Red Hat Enterprise Linux 6.5.

* Added the ability to specify custom virtual host configurations.

* Added the ability to expose OpenToken attributes for unprotected resources in the `mod_pf.conf` file.

* Added the ability to use Allow/Deny directives in combination with `Satisfy Any` to achieve IP allow or deny directives.

## Apache Linux Integration Kit 2.4.1 – June 2013

* Added support for Apache Server 2.4.

|   |                                                                           |
| - | ------------------------------------------------------------------------- |
|   | Skipped versions 2.3.7 through 2.4 for internal configuration management. |

## Apache Linux Integration Kit 2.3.6 – March 2013

* Added support for:

  * Ubuntu 12.04 LTS.

  * Apache Server 2.2.

## Apache Linux Integration Kit 2.3.1 – December 2012

* Fixed a security vulnerability.

* Added support for the OpenToken 2.5.1 adapter and agent.

## Apache Linux Integration Kit 2.3 – December 2011

* Added the ability to disable the Apache agent for specific virtual hosts in the `mod_pf.conf` file.

* Added the ability to specify the Cache-Control HTTP header value in the `mod_pf.conf` file.

* Added support for passing multivalued attributes through the HTTP headers.

* Fixed an issue that caused automatic escaping of single and double quotes in attribute values. These are exposed to the application through the HTTP headers and server variables.

## Apache Linux Integration Kit 2.2.1 – February 2010

* Fixed an issue that caused the Apache agent to truncate `POST` data.

## Apache Linux Integration Kit 2.2 – September 2009

* Added a start page and error page for the Apache agent. Learn more in [Download manifest](pf_apache_linux_ik_download_manifest.html).

* Added support for the default RHEL OpenSSL installation.

* Fixed an issue that caused Application Schemes, Hosts, and Port options to fail to work with the OpenToken when sent as a query parameter.

* Fixed an issue that caused the Apache agent to fail to check the `POST` and query values, then the cookie for a valid OpenToken.

## Apache Linux Integration Kit 2.1 – March 2009

* Added support for:

  * Red Hat Enterprise Linux 4 and 5 (32-bit and 64-bit).

  * Apache 2.0 and 2.2.

  * Prefork and worker multiprocessing modules.

  * Reverse proxies

* Added richer support for single logout.

* Added the ability to use an alternative method to set session attributes as HTTP headers or environment variables without a prefix.

## Apache Linux Integration Kit 2.0 – November 2008

* Removed deprecated functionality that wasn't specific to PingFederate to simplify the Apache module.

* Added the ability to expose attributes as HTTP request headers.

* Added the ability to log the SAML subject in the Apache `access_log`.

* Updated the OpenToken library to support password obfuscation.

* Updated the OpenToken library to support the `POST` transport method.

* Fixed an issue that required Cancel URLs to be contained in a protected resource.

* Fixed an issue that caused the cookie domain to be validated against the agent configuration file if `query` or `POST` is used as the initial transport method.

## Apache Linux Integration Kit 1.1 – October 2008

* Added support for `dynamic TargetResource`.

* Removed items that aren't necessary for the PingFederate implementation to simplify the configuration.

* Added the ability for filters to use the full request URL, including query parameters, to determine whether to protect a resource.

* Fixed an issue that caused the module to fail to start up if the transport mode was set to **Query Parameter** in the OpenToken adapter setup. The OpenToken session now uses the `cookie-domain` property out of the `mod_plaa.conf` file instead of the `mod_pf.conf` file.

* The Apache Linux Integration Kit now ships with OpenToken 2.2.2. OpenToken 2.2.2 fixed an issue that appended a question mark (`?`) to the target resource URL, which Apache couldn't process.

## Apache Linux Integration Kit 1.0 – September 2007

* Initial release.

---

---
title: Configuring an OpenToken SP Adapter instance
description: Configure the OpenToken Adapter to determine how PingFederate communicates with your service provider application.
component: apache
page_id: apache:setup:pf_apache_linux_ik_configuring_an_opentoken_sp_adapter_instance
canonical_url: https://docs.pingidentity.com/integrations/apache/setup/pf_apache_linux_ik_configuring_an_opentoken_sp_adapter_instance.html
llms_txt: https://docs.pingidentity.com/integrations/apache/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 27, 2024
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

   3. From the **Type** list, select **OpenToken Adapter**. Click **Next**.

3. On the **Instance Configuration** tab, configure the adapter instance by referring to [Configuring an OpenToken SP Adapter instance](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_config_opentoken_sp_adapt_instance.html) in the PingFederate documentation. Click **Next**.

   |   |                                                                                                                                                                                                   |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | If you use Apache to protect multiple sites on the same domain, in the OpenToken Adapter instance configuration, select **None** for SameSite Cookie, and select the **Secure Cookie** check box. |

4. Export the configuration file:

   1. On the **Actions** tab, click **Download** and then click **Export**.

   2. Save `agent-config.txt`. Click **Next**.

5. On the **Extended Contract** tab, add any attributes that you expect to retrieve other than the SAML subject. Click **Next**.

6. On the **Target App Info** tab, enter the basic information about your SP application. Click **Next**.

7. On the **Summary** tab, check and save your configuration. Click **Save**.

8. Create or update an identity provider (IdP) connection to use the OpenToken Adapter instance as shown in [Service provider SSO configuration](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_servic_provid_sso_config.html) in the PingFederate documentation.

---

---
title: Configuring the Apache agent
description: Configure the Apache agent by modifying the mod_pf.conf file that you copied in Deploying the Apache agent.
component: apache
page_id: apache:setup:pf_apache_linux_ik_configuring_the_apache_agent
canonical_url: https://docs.pingidentity.com/integrations/apache/setup/pf_apache_linux_ik_configuring_the_apache_agent.html
llms_txt: https://docs.pingidentity.com/integrations/apache/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 27, 2024
section_ids:
  steps: Steps
---

# Configuring the Apache agent

Configure the Apache agent by modifying the `mod_pf.conf` file that you copied in [Deploying the Apache agent](pf_apache_linux_ik_deploying_the_agent.html).

## Steps

1. Edit the `<apache_home>/conf/mod_pf.conf` file by modifying the example configuration and any optional properties based on your environment and needs.

   Comments above each property describe the function and possible values for that property.

2. Save the file and restart Apache to load the new configuration.

---

---
title: Deploying the Apache agent
description: To use the Apache agent, copy the files to your Apache directory and modify your Apache configuration.
component: apache
page_id: apache:setup:pf_apache_linux_ik_deploying_the_agent
canonical_url: https://docs.pingidentity.com/integrations/apache/setup/pf_apache_linux_ik_deploying_the_agent.html
llms_txt: https://docs.pingidentity.com/integrations/apache/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 27, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
  result: Result:
---

# Deploying the Apache agent

To use the Apache agent, copy the files to your Apache directory and modify your Apache configuration.

## About this task

The PingFederate Apache agent is represented by the `<apache_home>/conf/mod_pf.conf` Apache module (dynamic library) and an auxiliary OpenToken library. The behavior of the Apache agent is controlled by properties contained in the `mod_pf.conf` file.

## Steps

1. Download the Apache Linux Integration Kit `.zip` archive from the [**Add-ons** tab of the PingFederate downloads page](https://www.pingidentity.com/en/resources/downloads/pingfederate.html) or the [Ping Identity Marketplace](https://marketplace.pingone.com/item/apache-linux-integration-kit-for-pingfederate).

2. In the Apache Linux Integration Kit `.zip` archive, copy the contents of the `apache-agent/lib` directory that corresponds to your Linux version into your Apache `/modules` directory. If the files already exist, overwrite them.

   |   |                                                                                                                                                            |
   | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | For an Apache HTTP Server running on Canonical Ubuntu, use the modules found in the corresponding version's subdirectory: `Apache_2.4/Ubuntu<version>_64`. |

3. For new installations, in the integration-kit `apache-agent/config` directory, copy the `mod_pf.conf`, `start_page_template.html`, `fragment_preservation_request_template.html`, and the `error_page_template.html` files into the `/conf` directory of your Apache installation (or the `/etc/apache2/conf-available/` directory in Ubuntu).

4. Copy the `agent-config.txt` file that you downloaded in [Configuring an OpenToken SP Adapter instance](pf_apache_linux_ik_configuring_an_opentoken_sp_adapter_instance.html) to the Apache `/conf` folder.

5. If you're using Security Enhanced Linux, run the following commands as the root user:

   ```none
   chcon --reference /usr/sbin/httpd /etc/httpd/modules/mod_pf.so
   chcon --reference /usr/sbin/httpd /etc/httpd/modules/libopentoken.so
   ```

   This allows the agent to run in the `httpd` context.

   |   |                                                            |
   | - | ---------------------------------------------------------- |
   |   | The preceding paths assume the default Linux installation. |

6. In the Apache `httpd.conf` file, add the following statement above any other `LoadModule` statements:

   ```none
   LoadModule access_compat_module modules/mod_access_compat.so
   LoadFile modules/libopentoken.so
   LoadModule pf_module modules/mod_pf.so
   PingFederateConfigurationFile conf/mod_pf.conf
   ```

   |   |                                                                                                                                                                       |
   | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | Depending on the Ubuntu version, the module installation with default Apache could require additional steps. If so, perform steps 6a - 6c. Otherwise, skip to step 7. |

   1. Place the `.so` files in the `/usr/lib/apache2/modules/` directory.

      ### Result:

      A configuration file (`/etc/apache2/mods-available/mod_pf.load`) is created to load the module. It contains the following statements:

      ```none
      LoadModule access_compat_module /usr/lib/apache2/modules/mod_access_compat.so
      LoadFile  /usr/lib/apache2/modules/libopentoken.so
      LoadModule pf_module  /usr/lib/apache2/modules/mod_pf.so
      ```

   2. Link this file as enabled modules in the `/etc/apache2/mods-enabled/` directory:

      ```none
      sudo ln -s ../mods-available/mod_pf.load mod_pf.load
      ```

   3. Link the `/etc/apache2/conf-available/mod_pf.conf` file as enabled conf in the `/etc/apache2/conf-enabled` file:

      ```none
      sudo ln -s ../conf-available/mod_pf.conf mod_pf.conf
      ```

7. Add the following statement within all `Directory` contexts that the agent should handle:

   ```none
   AuthType PFApacheAgent
   ```

   |   |                                                                                                                                                                                                                                                                                                                                                            |
   | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | Use a "deny by default" configuration for all directories that you want the Apache agent to protect:```none
   Order Deny,Allow
   Deny from all
   ```Learn more about `AuthType` examples in [Apache Integration Kit AuthType examples](https://support.pingidentity.com/s/article/Apache-Integration-Kit-AuthType-examples) in the Ping Identity Knowledge Base. |

8. Restart Apache.

---

---
title: Download manifest
description: The following files are included in the Apache Linux Integration Kit .zip archive.
component: apache
page_id: apache:release_notes:pf_apache_linux_ik_download_manifest
canonical_url: https://docs.pingidentity.com/integrations/apache/release_notes/pf_apache_linux_ik_download_manifest.html
llms_txt: https://docs.pingidentity.com/integrations/apache/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 27, 2024
---

# Download manifest

The following files are included in the Apache Linux Integration Kit `.zip` archive.

* `Legal.pdf`: Copyright and license information.

* `apache-agent`: Contains the PingFederate Apache agent files.

  * `config`: Contains configuration files.

    * `mod_pf.conf`: Apache agent module configuration file.

    * `start_page_template.html`: Apache agent start-page template.

    * `error_page_template.html`: Apache agent error-page template.

  * `lib/Apache_2.4`

    * `RHEL7_64`: Contains the RHEL 7.x 64-bit.

      * `libopentoken.so`: OpenToken library.

      * `mod_pf.so`: Apache agent module.

    * `RHEL8_64`: Contains the RHEL 8.x 64-bit.

      * `libopentoken.so`: OpenToken library.

      * `mod_pf.so`: Apache agent module.

    * `RHEL9_64`: Contains the RHEL 9.x 64-bit.

      * `libopentoken.so`: OpenToken library.

      * `mod_pf.so`: Apache agent module.

    * `Ubuntu18_64`: Contains the Canonical Ubuntu 18.04 64-bit.

      * `libopentoken.so`: OpenToken library.

      * `mod_pf.so`: Apache agent module.

    * `Ubuntu20_64`: Contains the Canonical Ubuntu 20.04 64-bit.

      * `libopentoken.so`: OpenToken library.

      * `mod_pf.so`: Apache agent module.

    * `Ubuntu22_64`: Contains the Canonical Ubuntu 22.04 64-bit.

      * `libopentoken.so`: OpenToken library.

      * `mod_pf.so`: Apache agent module.

    * `Ubuntu24_64`: Contains the Canonical Ubuntu 24.04 64-bit.

      * `libopentoken.so`: OpenToken library.

      * `mod_pf.so`: Apache agent module.

---

---
title: Error handling
description: When an error occurs, the Apache agent redirects the browser to the PingFederateErrorPageURL address in your <apache_home>/conf/mod_pf.conf file.
component: apache
page_id: apache:apache_agent_information:pf_apache_linux_ik_error_handling
canonical_url: https://docs.pingidentity.com/integrations/apache/apache_agent_information/pf_apache_linux_ik_error_handling.html
llms_txt: https://docs.pingidentity.com/integrations/apache/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 27, 2024
---

# Error handling

When an error occurs, the Apache agent redirects the browser to the `PingFederateErrorPageURL` address in your `<apache_home>/conf/mod_pf.conf` file.

|   |                                                                 |
| - | --------------------------------------------------------------- |
|   | This value isn't enabled by default, but examples are provided. |

---

---
title: Known issues and limitations
description: The following are known issues or limitations for the Apache Linux Integration Kit.
component: apache
page_id: apache:release_notes:pf_apache_linux_ik_known_issues_and_limitations
canonical_url: https://docs.pingidentity.com/integrations/apache/release_notes/pf_apache_linux_ik_known_issues_and_limitations.html
llms_txt: https://docs.pingidentity.com/integrations/apache/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 27, 2024
section_ids:
  known-issues: Known issues
  known-limitations: Known limitations
---

# Known issues and limitations

The following are known issues or limitations for the Apache Linux Integration Kit.

## Known issues

* URL encoding in the `PingFederateFilter` and `PingFederateFilterAnonymous` isn't supported.

* In some configurations, Apache fails to load the module with the following being the last log entry: `Deobfuscating password for the password-based keys generation`.

  To overcome this issue, ensure the agent module is loaded immediately after the authz-related modules.

## Known limitations

* `Satisfy All` isn't supported when used in conjunction with the `Allow` directive for access control.

* `RequireAll` isn't supported.

* The `PingFederateFilter` doesn't support:

  * URL encoded characters or non-ASCII characters.

  * Query strings

* The PingFederate Apache agent relies on path comparison to protect resources. Other modules in Apache such as `mod_speling` and `mod_rewrite` can affect the way the PingFederate Apache agent evaluates resources.

* To support fragment preservation, the # symbol in URL fragment must be URL encoded.

---

---
title: Logging
description: The PingFederate Apache agent uses an Apache API logging scheme that writes into the standard logs/error_log file. This file is created automatically at startup with the verbosity level controlled by LogLevel in your httpd.conf file.
component: apache
page_id: apache:apache_agent_information:pf_apache_linux_ik_logging
canonical_url: https://docs.pingidentity.com/integrations/apache/apache_agent_information/pf_apache_linux_ik_logging.html
llms_txt: https://docs.pingidentity.com/integrations/apache/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 27, 2024
---

# Logging

The PingFederate Apache agent uses an Apache API logging scheme that writes into the standard `logs/error_log` file. This file is created automatically at startup with the verbosity level controlled by `LogLevel` in your `httpd.conf` file.

The PingFederate Apache agent has six internally distinguished verbosity levels, ranging from `0` to `5`. The first four correspond to Apache definitions in `error/warn/notice/info`. The last two levels are for logging HTTP requests, responses, and cURL-library debug output, if necessary. The default level is `0`, which logs only errors.

|   |                                                                                                                                                                          |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | The Apache agent logs all of its output at the `info` level. To access this output, set the Apache `LogLevel` to `info` in `httpd.conf`, then restart the Apache server. |

---

---
title: Memory usage
description: "The Apache agent uses the Apache Portable Runtime (APR) pools for allocation of most data: either the configuration-time pool for storing configuration variables or request-time pools for processing sessions."
component: apache
page_id: apache:apache_agent_information:pf_apache_linux_ik_memory_usage
canonical_url: https://docs.pingidentity.com/integrations/apache/apache_agent_information/pf_apache_linux_ik_memory_usage.html
llms_txt: https://docs.pingidentity.com/integrations/apache/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 27, 2024
---

# Memory usage

The Apache agent uses the Apache Portable Runtime (APR) pools for allocation of most data: either the configuration-time pool for storing configuration variables or request-time pools for processing sessions.

Heap is used only for temporary data with a short usage time and sensitive size, such as:

* Dynamic reallocations on compressed-token decompression

* Parsing session information

* Operations with the OpenToken library

---

---
title: Overview of the SSO flow
description: The Apache agent acts as a filter in front of an external protected resource, such as an application.
component: apache
page_id: apache::pf_apache_linux_ik_overview_of_the_sso_flow
canonical_url: https://docs.pingidentity.com/integrations/apache/pf_apache_linux_ik_overview_of_the_sso_flow.html
llms_txt: https://docs.pingidentity.com/integrations/apache/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 27, 2024
---

# Overview of the SSO flow

The Apache agent acts as a filter in front of an external protected resource, such as an application.

For each request, the Apache agent does one of the following:

* If the request is for an unprotected resource, the Apache agent passes the request to the application.

* If the request is for a protected resource, the Apache agent checks to see if there is a PingFederate session available and if the session parameters meet session policy for that session.

* If a session exists and the session meets session policy for that request, the Apache agent passes the request through to the application.

* If a session doesn't exist or if the existing session doesn't meet the session policy for that request, the Apache agent redirects the browser through the PingFederate server to an identity provider (IdP) for authentication. After authentication, PingFederate redirects the user back to the protected resource with a valid session.

The following diagram illustrates a service provider (SP)-initiated single sign-on (SSO) scenario, showing the request flow and how the PingFederate OpenToken Adapter wraps attributes from an assertion into a secure token (OpenToken) and passes the token to Apache.

![A diagram that shows the flow of information between the server, PingFederate, and the browser.](_images/lop1563995115032.png)

In this flow:

1. A user attempts to access a resource on the Apache server protected by the PingFederate Apache agent.

   1. The user is redirected to the PingFederate server for authentication.

   2. If an OpenToken session already exists, the user is granted immediate access.

2. The PingFederate server redirects the user's browser to an IdP for authentication using either the SAML or WS-Federation protocols. The IdP partner authenticates the user and returns a SAML assertion.

3. PingFederate validates the assertion and creates an OpenToken for the user including any configured attributes. PingFederate then redirects the browser, including the OpenToken, back to the Apache agent.

4. The Apache agent verifies the OpenToken and grants access to the protected resource. The User ID and any attributes from the OpenToken are exposed to the resource as HTTP request headers or Apache environment variables.

---

---
title: Session information and user attributes
description: The PingFederate Apache agent passes session information and user attributes from the adapter to the application.
component: apache
page_id: apache:apache_agent_information:pf_apache_linux_ik_session_information_and_user_attributes
canonical_url: https://docs.pingidentity.com/integrations/apache/apache_agent_information/pf_apache_linux_ik_session_information_and_user_attributes.html
llms_txt: https://docs.pingidentity.com/integrations/apache/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 27, 2024
---

# Session information and user attributes

The PingFederate Apache agent passes session information and user attributes from the adapter to the application.

The Apache agent includes the information in HTTP request headers or Apache environment variables. This information can then be used by the application for authorization decisions or for generation of content specific to the user making the request.

The following session and attribute information is exposed to the application:

* Attributes from the OpenToken Adapter contract

  The subject (`SUBJECT`) and any attributes that you add on the **Extended Contract** tab of the adapter configuration. Only the attributes fulfilled at runtime are exposed to the application. Attributes with a `NULL` value aren't included in the OpenToken.

* `NOT-ON-OR-AFTER`

  The time until inactivity timeout is reached.

* `RENEW-UNTIL`

  The time until overall session timeout is reached.

* `AUTH_NOT-BEFORE`

  The time when the session was created.

* `AUTHNCONTEXT`

  Information from the SAML assertion that describes how the user was authenticated at the IdP.

For security reasons, each HTTP request header or Apache environment variable is first pre-pended with a specific prefix. Learn more about configuring the prefix in [Configuring the Apache agent](../setup/pf_apache_linux_ik_configuring_the_apache_agent.html). The Apache agent always removes and rewrites the prefixed request headers and environment variables for each request.

If you can't modify your applications to accept headers with this prefix, you can configure the Apache agent to add a prefix to the HTTP headers or environment variables. In this case, on the **Extended Contract** tab of the OpenToken Adapter configuration, include an attribute named `pf_attribute_list`. Map that attribute in your identity provider (IdP) connection as a text field containing a comma-separated list of all the attributes in the adapter contract. This attribute list is sent in the OpenToken and used by the Apache agent to overwrite headers in the request.

Learn more about [Configuring target session fulfillment](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_configuring_target_session_fulfillment.html) in the PingFederate documentation.

---

---
title: Session logout
description: The PingFederateCancelURL address in your <apache_home>/conf/mod_pf.conf file initiates a user-session logout. This URL specifies a resource that directs the Apache agent to:
component: apache
page_id: apache:apache_agent_information:pf_apache_linux_ik_session_logout
canonical_url: https://docs.pingidentity.com/integrations/apache/apache_agent_information/pf_apache_linux_ik_session_logout.html
llms_txt: https://docs.pingidentity.com/integrations/apache/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 27, 2024
---

# Session logout

The `PingFederateCancelURL` address in your `<apache_home>/conf/mod_pf.conf` file initiates a user-session logout. This URL specifies a resource that directs the Apache agent to:

1. Initiate a single logout (SLO), if configured

2. Expire the PingFederate session

3. Clean up any resources associated with the session

4. Pass control back to the application so that it can clean up its own session

---

---
title: Session validation
description: PingFederate validates both an inactivity timeout and an overall session timeout:
component: apache
page_id: apache:apache_agent_information:pf_apache_linux_ik_session_validation
canonical_url: https://docs.pingidentity.com/integrations/apache/apache_agent_information/pf_apache_linux_ik_session_validation.html
llms_txt: https://docs.pingidentity.com/integrations/apache/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 27, 2024
---

# Session validation

PingFederate validates both an inactivity timeout and an overall session timeout:

* Inactivity timeout

  The amount of time that a session can be inactive when no new browser requests are received and before a user is required to reauthenticate.

* Overall session timeout

  The total amount of time that a session can be active, regardless of activity, before the user is required to re-authenticate.

If either of the timeout limits has expired, the Apache agent cancels the existing session and redirects the browser to the `PingFederateLoginPageUrl` address in your `<apache_home>/conf/mod_pf.conf` file. This starts a service provider (SP)-initiated single sign-on (SSO) request at the identity provider (IdP).

|   |                                                                                                           |
| - | --------------------------------------------------------------------------------------------------------- |
|   | Session cancellation enforces session cleanup in the PingFederate server and session cookie obsolescence. |

---

---
title: Setting up virtual hosts
description: Each virtual host can optionally have its own respective Apache agent configuration.
component: apache
page_id: apache:setup:pf_apache_linux_ik_setting_up_virtual_hosts
canonical_url: https://docs.pingidentity.com/integrations/apache/setup/pf_apache_linux_ik_setting_up_virtual_hosts.html
llms_txt: https://docs.pingidentity.com/integrations/apache/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 27, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Setting up virtual hosts

Each virtual host can optionally have its own respective Apache agent configuration.

## About this task

If no custom configuration is provided, a virtual host uses the agent configuration from the base server.

## Steps

* If you want to use this feature, add the following to the Apache `httpd.conf` file in the virtual host context:

  ```none
  PingFederateConfigurationFile conf/mod_pf_vhost.conf
  ```

  In this example, `mod_pf_vhost.conf` is an agent configuration file that contains settings unique to the virtual host. PingFederate attributes from the base server configuration aren't merged with the virtual host when the `PingFederateConfigurationFile` attribute is specified for the virtual host.

---

---
title: SSL support
description: The Apache agent supports TLS/SSL, using standard Apache SSL support for connections to the server from browsers.
component: apache
page_id: apache:apache_agent_information:pf_apache_linux_ik_ssl_support
canonical_url: https://docs.pingidentity.com/integrations/apache/apache_agent_information/pf_apache_linux_ik_ssl_support.html
llms_txt: https://docs.pingidentity.com/integrations/apache/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 27, 2024
---

# SSL support

The Apache agent supports TLS/SSL, using standard Apache SSL support for connections to the server from browsers.

---

---
title: Testing the Apache agent
description: The Apache agent includes a protected start page to help you verify your configuration. This feature is for testing purposes only and is disabled by default.
component: apache
page_id: apache:setup:pf_apache_linux_ik_testing_the_agent
canonical_url: https://docs.pingidentity.com/integrations/apache/setup/pf_apache_linux_ik_testing_the_agent.html
llms_txt: https://docs.pingidentity.com/integrations/apache/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 27, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Testing the Apache agent

The Apache agent includes a protected start page to help you verify your configuration. This feature is for testing purposes only and is disabled by default.

## About this task

The start page initiates a single sign-on transaction with the identity provider partner. If it succeeds, it displays the HTTP headers that the Apache agent will expose to your application. These headers correspond to attributes from the SAML assertion.

## Steps

1. Turn on the test page:

   1. Edit the `<apache_home>/conf/mod_pf.conf` by adding `#` to comment out the `PingFederateStartPageURL` property.

   2. Save the file and restart Apache.

2. Modify the following URL for your environment and then open it in a browser.

   ```none
   http://apache-server/protected-path/?cmd=PingStartPage
   ```

3. When you finish testing, revert your changes to `mod_pf.conf`.

   |   |                                                                                   |
   | - | --------------------------------------------------------------------------------- |
   |   | For security reasons, you should disable this feature in production environments. |

4. Restart Apache.

---

---
title: Updating the OpenToken Adapter
description: The Apache Linux Integration Kit relies on the OpenToken Adapter that is distributed with the Java Integration Kit. Update the OpenToken Adapter to get the latest feature and security updates.
component: apache
page_id: apache:setup:pf_apache_linux_ik_updating_the_opentoken_adapter
canonical_url: https://docs.pingidentity.com/integrations/apache/setup/pf_apache_linux_ik_updating_the_opentoken_adapter.html
llms_txt: https://docs.pingidentity.com/integrations/apache/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 27, 2024
section_ids:
  steps: Steps
---

# Updating the OpenToken Adapter

The Apache Linux Integration Kit relies on the OpenToken Adapter that is distributed with the Java Integration Kit. Update the OpenToken Adapter to get the latest feature and security updates.

## Steps

1. Download the Java Integration Kit `.zip` archive from the **Add-ons** tab of the [PingFederate downloads page](https://www.pingidentity.com/en/resources/downloads/pingfederate.html).

2. Stop PingFederate.

3. Delete the `opentoken-adapter-<version>.jar` file from your `<pf_install>/pingfederate/server/default/deploy` directory.

4. From the Java Integration Kit `.zip` archive, copy the contents of `dist/pingfederate` to your `<pf_install>/pingfederate` directory.

   |   |                                                                                                                                                                                                             |
   | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | The `commons-collections`, `commons-beanutils`, and `commons-logging` libraries are provided as a convenience and should be installed only if they aren't already contained in the application `CLASSPATH`. |

5. Start PingFederate.

6. If you operate PingFederate in a cluster, repeat steps 2-5 for each engine node.

---

---
title: Upgrading an existing deployment
description: If you're upgrading from a previous version of the Apache Linux Integration Kit, modify your existing configuration files.
component: apache
page_id: apache:setup:pf_apache_linux_ik_upgrading_an_existing_deployment
canonical_url: https://docs.pingidentity.com/integrations/apache/setup/pf_apache_linux_ik_upgrading_an_existing_deployment.html
llms_txt: https://docs.pingidentity.com/integrations/apache/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 27, 2024
section_ids:
  steps: Steps
---

# Upgrading an existing deployment

If you're upgrading from a previous version of the Apache Linux Integration Kit, modify your existing configuration files.

## Steps

1. Stop Apache.

2. Download the Apache Linux Integration Kit `.zip` archive from the **Add-ons** tab of the [PingFederate downloads page](https://www.pingidentity.com/en/resources/downloads/pingfederate.html).

3. From the `.zip` archive, copy `apache-agent/lib/<your platform>/libopentoken.so` to the Apache modules directory.

4. Edit your existing `mod_pf.conf` file:

   1. Add the following if it doesn't already exist.

      ```none
      # Enables or disables the "http only" attribute of the cookie. Http only cookies
      # inform the browser that the cookie shouldn't be accessible by client-side scripts.
      # The default is set to "yes"

      PingFederateCookieHttpOnly              yes
      ```

   2. Set the value to `yes` or `no` to suit your environment. Save the file.

5. Edit your existing `mod_pf.so` file:

   1. Add the following if it doesn't already exist.

      ```none
      # (Required)
      # The SameSite cookie attribute is set to this value. Set this to match the value of
      # 'cookie-samesite-attribute' in the Agent configuration file (defined in
      # PingFederateAgentConfigurationFile), if that is defined.
      # The allowed values for this setting are: Strict, Lax, None, and Nothing
      # The "Strict", "Lax", and "None" value changes the SameSite cookie attribute setting.
      # The "Nothing" value leaves the SameSite cookie attribute unset in the OpenToken Session Cookie.
      # For the "None" value, you must use secure attributes because cross-site cookies can only be
      # accessed over HTTPS connections.
      # If the cookie is not secure and the "None" value is selected, the SameSite cookie attribute
      # will not be set.

      PingFederateCookieSameSiteAttribute	Nothing
      ```

   2. Set the value to `Strict`, `Lax`, `None`, or `Nothing` to suit your environment. Save the file.

6. Add the following if it doesn't already exist.

   ```none
   # (Optional)
   # Enables or disables fragment preservation in requests.
   # When set to "yes", preserves request fragment and redirects user back
   # to the URI with fragment.
   # To prevent sensitive data leakage, ensure that no sensitive information
   # is present in a preserved fragment.
   # The default is "no".
   PingFederateEnableFragmentPreservation   no

   # (Optional)
   # The HTML template used to generate client side (JavaScript-based) redirects for
   # fragment preservation. If not specified, a prebuilt template is used.
   # Path could be an absolute or relative to the httpd.conf ServerRoot
   # definition.

   #PingFederateFragmentPreservationPageTemplateFile conf/fragment_preservation_request_template.html
   ```

7. Start Apache.

8. Update the OpenToken Adapter in PingFederate as shown in [Updating the OpenToken Adapter](pf_apache_linux_ik_updating_the_opentoken_adapter.html).

9. Reinstall the Apache agent as shown in [Apache Agent setup](pf_apache_linux_ik_agent_setup.html).