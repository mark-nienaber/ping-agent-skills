---
title: Changelog
description: The following is the change history for the PHP Integration Kit.
component: php
page_id: php:release_notes:pf_php_ik_changelog
canonical_url: https://docs.pingidentity.com/integrations/php/release_notes/pf_php_ik_changelog.html
llms_txt: https://docs.pingidentity.com/integrations/php/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 21, 2024
---

# Changelog

The following is the change history for the PHP Integration Kit.

**PHP Integration Kit 2.5.2 – January 2016**

* Updated sample application data archive.

**PHP Integration Kit 2.5.1 – December 2012**

* Updated to address security issue found since the previous release.

* Added support for the 2.5.1 version of the OpenToken Adapter and OpenToken Agent.

* Added Support for PHP 5.4.8.

* Added Namespaces to the PHP OpenToken Agent.

**PHP Integration Kit 2.4 – March 2010**

* Added token Reply Prevention to the OpenToken IdP Adapter Advanced Settings.

**PHP Integration Kit 2.3 – November 2008**

* Added POST Transport Method for OpenToken when used by a service Provider.

* Added configuration to specify session cookie vs. persistent cookie.

* Added option to set the "`Secure`" attribute on an OpenToken when cookie is used.

* Correctly handles `null` parameters for SOAP SLO.

* Empty query string (`?`) is not automatically appended to the URL when redirecting to `TargetResource`.

* `TargetResource URL` is URL encoded.

**PHP Integration Kit 2.2 – June 2008**

* Added support for SAML 2.0 `isPassive` and `ForceAuthn`.

* Enforced UTF-8 encoding within the OpenToken adapter.

* Combined the OpenToken adapter and OpenToken Java library jar files into a single adapter file for easier deployment to PingFederate.

**PHP Integration Kit 1.2 – December 2007**

* Repaired OpenToken decoding to correct bit unpacking issue.

* Added Agent Toolkit API HTML documentation.

**PHP Integration Kit 1.1 – December 2007**

* Added support for sending and receiving multi-value attributes in the SAML assertion.

**PHP Integration Kit 1.0 – November 2007**

* Initial release.

---

---
title: Configuring an OpenToken Adapter instance
description: Configure the OpenToken Adapter to determine how PingFederate communicates with your application.
component: php
page_id: php:setup:pf_php_ik_configuring_an_opentoken_adapter_instance
canonical_url: https://docs.pingidentity.com/integrations/php/setup/pf_php_ik_configuring_an_opentoken_adapter_instance.html
llms_txt: https://docs.pingidentity.com/integrations/php/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 5, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Configuring an OpenToken Adapter instance

Configure the OpenToken Adapter to determine how PingFederate communicates with your application.

## About this task

These steps are for creating a service provider (SP) adapter instance. You can complete the equivalent steps to create an identity provider (IdP) adapter instance.

## Steps

1. Sign on to the PingFederate administrative console.

2. On the **Service Provider > Adapters** screen, click Create New Instance.

3. On the Type screen, set the basic adapter instance attributes.

   1. In the Instance Name field, type a name for the adapter instance.

   2. In the Instance ID field, type a unique identifier for the adapter instance.

   3. On the Type list, select OpenToken Adapter, and then click Next.

4. On the Instance Configuration screen, configure the adapter instance by referring to [Configuring an OpenToken SP Adapter instance](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_config_opentoken_sp_adapt_instance.html) in the PingFederate documentation. Click Next.

   * In your adapter instance configuration, in the Advanced Fields section, clear the Obfuscate Password check box. The PHP agent does not support encrypted passwords. The password is Base64 encoded.

5. Export the configuration file.

   1. On the Actions screen, click Download, and then click Export.

   2. Save `agent-config.txt`. Click Next.

6. On the Extended Contract screen, add any attributes that you expect to retrieve in addition to core contract attributes. Click Next.

7. On the Summary screen, check that the configuration is correct, and then click Done.

8. On the Manage SP Adapter Instances screen, click Save.

9. Create or update an identity provider (IdP) connection to use the OpenToken Adapter instance. See [Service provider SSO configuration](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_servic_provid_sso_config.html) in the PingFederate documentation.

---

---
title: Configuring PingFederate and the sample applications
description: To see a working demonstration of the PHP Integration Kit, deploy the configuration archive and sample applications.
component: php
page_id: php:setup:pf_php_ik_configuring_pf_and_the_sample_applications
canonical_url: https://docs.pingidentity.com/integrations/php/setup/pf_php_ik_configuring_pf_and_the_sample_applications.html
llms_txt: https://docs.pingidentity.com/integrations/php/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 21, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Configuring PingFederate and the sample applications

To see a working demonstration of the PHP Integration Kit, deploy the configuration archive and sample applications.

## About this task

The sample configuration archive configures a single instance of PingFederate with an example integration that uses both the IdP and SP sample applications. It automatically creates two instances of the OpenToken Adapter.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Deploying the configuration archive will destroy your existing PingFederate configuration. We recommend that you test it on a fresh installation of PingFederate, or back up your current configuration as shown in [Exporting an archive](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_configurationarchivetasklet_configurationarchiveexportstate.html) in the PingFederate documentation. |

## Steps

1. Start PingFederate.

2. From the Agentless Integration Kit `.zip` archive, copy `sample/data.zip` to `<pf_install>/pingfederate/server/deploy/drop-in-deployer`.

3. If your PHP server is not hosted on the same machine as PingFederate, adjust the URLs in the OpenToken Adapter instance configurations.

   1. Sign on to the PingFederate administrator console.

   2. On the **Identity Provider > Adapters** screen, click OTIdPPHP.

   3. On the IdP Adapter screen, click Show Advanced Fields.

   4. In the Authentication Service and Logout Service fields, change the localhost:9119 portion of the URL to point to your PHP server.

   5. Make the equivalent changes to the URLs in the **Service Provider > Adapters > OTSPPHP** adapter instance configuration.

4. Do one of the following:

   * [Deploying on Red Hat Linux](pf_php_ik_deploying_on_red_hat_linux.html).

   * [Deploying on Linux or Unix](pf_php_ik_deploying_on_linux_or_unix.html).

   * [Deploying on Windows](pf_php_ik_deploying_on_windows.html).

   * [Deploying on the PHP built-in web server](pf_php_ik_deploying_on_the_php_built_in_web_server.html)

---

---
title: Configuring your PHP server
description: To allow your PHP server to work with the PHP Integration Kit, check that the correct extensions are installed and configure your agent config file.
component: php
page_id: php:setup:pf_php_ik_configuring_your_php_server
canonical_url: https://docs.pingidentity.com/integrations/php/setup/pf_php_ik_configuring_your_php_server.html
llms_txt: https://docs.pingidentity.com/integrations/php/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 21, 2024
section_ids:
  steps: Steps
---

# Configuring your PHP server

To allow your PHP server to work with the PHP Integration Kit, check that the correct extensions are installed and configure your agent config file.

## Steps

1. On your PHP server, use the phpinfo() function to check that the cURL, mcrypt, zlib, and mhash extensions are installed.

2. Check that your PHP server is configured to process files with a .php extension.

   On the Apache HTTPD server, you can use the AddType command to add the extension:

   `AddType application/x-httpd-php .php`

   This step is not needed on the built-in PHP web server.

3. From the integration `.zip` archive, copy the `dist/pingidentity/opentoken` directory to your PHP `include` path as `/opentoken`.

4. Change `AGENT_CONFIG_FILE` in the `pingidentity/opentoken/helpers/config.php` file to point to the location of the `agent-config.txt` file that you saved in [Configuring an OpenToken Adapter instance](pf_php_ik_configuring_an_opentoken_adapter_instance.html).

   On Windows, use the network-path syntax:

   `\\<host>\<path>`

5. To avoid internationalization compatibility issues, enforce UTF-8 encoding by explicitly specify `default_charset=utf8` in your PHP server's `php.ini` file.

---

---
title: Custom application setup
description: You can configure theproductto integrate PingFederate with your identity provider (IdP) or service provider (SP) application.
component: php
page_id: php:setup:pf_php_ik_custom_application_setup
canonical_url: https://docs.pingidentity.com/integrations/php/setup/pf_php_ik_custom_application_setup.html
llms_txt: https://docs.pingidentity.com/integrations/php/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 21, 2024
---

# Custom application setup

You can configure theproductto integrate PingFederate with your identity provider (IdP) or service provider (SP) application.

If you would like to see a working demonstration of theproductbefore integrating your own applications, see [Sample application setup](pf_php_ik_sample_application_setup.html) instead.

---

---
title: Deploying on Linux or Unix
description: You can manually deploy the PHP Integration Kit sample applications on UNIX or other Linux platforms.
component: php
page_id: php:setup:pf_php_ik_deploying_on_linux_or_unix
canonical_url: https://docs.pingidentity.com/integrations/php/setup/pf_php_ik_deploying_on_linux_or_unix.html
llms_txt: https://docs.pingidentity.com/integrations/php/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 21, 2024
section_ids:
  steps: Steps
---

# Deploying on Linux or Unix

You can manually deploy the PHP Integration Kit sample applications on UNIX or other Linux platforms.

## Steps

1. From the integration `.zip` archive, copy the `sample` directory to root level of the DocumentRoot of your Apache HTTP server. This makes the directory accessible at https\://*hostname*/sample.

2. Move the `sample/config` directory to a directory on the server that is outside the DocumentRoot. This protects the `config` directory from unauthorized access.

3. Update the location of the `agent-config.txt` files. Modify the following files to point to the new location of the `config` directory.

   1. Open `sample/idp/pingidentity/opentoken/helpers/config.php` for editing.

   2. Change the following line based on the new location of your `config` directory:

      ```
      const   AGENT_CONFIG_FILE = "../config/idp/agent-config.txt";
      ```

   3. Repeat the equivalent steps a-b in `sample/sp/pingidentity/opentoken/helpers/config.php` for your SP `agent-config.txt` file.

4. Update the location of the `config.properties` files. Modify the following files to point to the new location of the `config` directory.

   1. Open `sample/idp/Const.php` for editing.

   2. Change the following line based on the new location of your `config` directory:

      ```
      define("CONFIG_FILE", "../config/idp/config.properties");
      ```

   3. Repeat the equivalent steps a-b in `sample/sp/Const.php` for your SP `config.properties` file.

5. Change the ownership and permission of the sample application configuration files for the user and/or group that runs the Apache server by doing the following:

   `chown –R <apache_user> <config_dir>/`**`chmod u+w <config_dir>/`**

6. If your PingFederate server is hosted on another computer, go to the following URLs and change the PF Host Name value in the SP and IdP sample applications configuration.

   * https\://*hostname*/sample/idp/ConfigUI.php

   * https\://*hostname*/sample/sp/ConfigUI.php

---

---
title: Deploying on Red Hat Linux
description: You can deploy the PHP Integration Kit sample applications on Linux Red Hat using the included installation script.
component: php
page_id: php:setup:pf_php_ik_deploying_on_red_hat_linux
canonical_url: https://docs.pingidentity.com/integrations/php/setup/pf_php_ik_deploying_on_red_hat_linux.html
llms_txt: https://docs.pingidentity.com/integrations/php/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 21, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Deploying on Red Hat Linux

You can deploy the PHP Integration Kit sample applications on Linux Red Hat using the included installation script.

## About this task

The script copies the sample applications to the Apache HTTP server DocumentRoot, copies configuration files, and changes file permissions and ownership.

## Steps

1. On the computer that hosts your Apache HTTP server, sign on as root.

2. Check that the Apache HTTP server is running.

3. Check the `httpd.conf` file to determine the DocumentRoot of the Apache HTTP server. The installation script will prompt you for this information.

4. From the integration `.zip` archive, copy the `sample` directory to the host computer.

5. At a shell command prompt, change the current directory to the sample director.

6. Execute the installation script using the following commands:

   1. `chmod u+x ./install.sh`

   2. `./install.sh`

7. Enter `y` (yes) to accept the detected Apache user.

---

---
title: Deploying on the PHP built-in web server
description: Check that the PHP path environment variable points to the correct location of PHP.
component: php
page_id: php:setup:pf_php_ik_deploying_on_the_php_built_in_web_server
canonical_url: https://docs.pingidentity.com/integrations/php/setup/pf_php_ik_deploying_on_the_php_built_in_web_server.html
llms_txt: https://docs.pingidentity.com/integrations/php/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 21, 2024
section_ids:
  steps: Steps
---

# Deploying on the PHP built-in web server

## Steps

1. Check that the PHP path environment variable points to the correct location of PHP.

2. Create a public HTML directory to host the sample applications.

3. From the integration `.zip` archive, copy the `sample` directory to root level of the new public HTML directory. This makes the directory accessible at `https://hostname/sample`.

4. Move the `sample/config` directory to a directory on the server that is outside the public HTML directory. This protects the `config` directory from unauthorized access.

5. Update the location of the `agent-config.txt` files. Modify the following files to point to the new location of the `config` directory.

   1. Open `sample/idp/pingidentity/opentoken/helpers/config.php` for editing.

   2. Change the following line based on the new location of your `config` directory:

      ```
      const   AGENT_CONFIG_FILE = "../config/idp/agent-config.txt";
      ```

   3. Repeat the equivalent steps a-b in `sample/sp/pingidentity/opentoken/helpers/config.php` for your SP `agent-config.txt` file.

6. Update the location of the `config.properties` files. Modify the following files to point to the new location of the `config` directory.

   1. Open `sample/idp/Const.php` for editing.

   2. Change the following line based on the new location of your `config` directory:

      ```
      define("CONFIG_FILE", "../config/idp/config.properties");
      ```

   3. Repeat the equivalent steps a-b in `sample/sp/Const.php` for your SP `config.properties` file.

7. From the public HTML directory, execute the following command to start the PHP built-in Web Server:

   `php –s <hostname>:<port>`

---

---
title: Deploying on Windows
description: You can manually deploy the PHP Integration Kit sample applications on Windows computers.
component: php
page_id: php:setup:pf_php_ik_deploying_on_windows
canonical_url: https://docs.pingidentity.com/integrations/php/setup/pf_php_ik_deploying_on_windows.html
llms_txt: https://docs.pingidentity.com/integrations/php/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 21, 2024
section_ids:
  steps: Steps
---

# Deploying on Windows

You can manually deploy the PHP Integration Kit sample applications on Windows computers.

## Steps

1. From the integration `.zip` archive, copy the `sample` directory to root level of the DocumentRoot of your Apache HTTP server. This makes the directory accessible at `https://hostname/sample`.

2. Move the `sample/config` directory to a directory on the server that is outside the DocumentRoot. This protects the `config` directory from unauthorized access.

3. Update the location of the `agent-config.txt` files. Modify the following files to point to the new location of the `config` directory.

   1. Open `sample/idp/pingidentity/opentoken/helpers/config.php` for editing.

   2. Change the following line based on the new location of your `config` directory:

      ```
      const   AGENT_CONFIG_FILE = "../config/idp/agent-config.txt";
      ```

   3. Repeat the equivalent steps a-b in `sample/sp/pingidentity/opentoken/helpers/config.php` for your SP `agent-config.txt` file.

4. Update the location of the `config.properties` files. Modify the following files to point to the new location of the `config` directory.

   1. Open `sample/idp/Const.php` for editing.

   2. Change the following line based on the new location of your `config` directory:

      ```
      define("CONFIG_FILE", "../config/idp/config.properties");
      ```

   3. Repeat the equivalent steps a-b in `sample/sp/Const.php` for your SP `config.properties` file.

5. Use Windows Task Manager to determine the user that runs the Apache server.

6. Change the security properties for the `config` to give full control to the user that runs the Apache server.

7. If your PingFederate server is hosted on another computer, go to the following URLs and change the **PF Host Name** value in the SP and IdP sample applications configuration.

   * `https://hostname/sample/idp/ConfigUI.php`

   * `https://hostname/sample/sp/ConfigUI.php`

---

---
title: Download manifest
description: The following files are included in the PHP Integration Kit .zip archive:
component: php
page_id: php:release_notes:pf_php_ik_download_manifest
canonical_url: https://docs.pingidentity.com/integrations/php/release_notes/pf_php_ik_download_manifest.html
llms_txt: https://docs.pingidentity.com/integrations/php/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 21, 2024
---

# Download manifest

The following files are included in the PHP Integration Kit `.zip` archive:

* `ReadMeFirst.pdf` – contains links to this online documentation.

* `legal` – a directory that contains this document:

  * `Legal.pdf` – copyright and license information.

* `dist` - a directory that contains libraries needed to run the adapter:

  * `opentoken-adapter-<version>.jar` - OpenToken Adapter JAR file.

  * `pingidentity/opentoken` – directory containing files for the Agent Toolkit for PHP.

    * `agent.php`

    * `/helpers` – directory containing:

      * `config.php`

      * `keyvalueserializer.php`

      * `multistringarray.php`

      * `opentoken.php`

      * `passwordkeygenerator.php`

      * `token.php`

* `sample`

  * `common` – directory that contains common files for the sample applications.

  * `config` – a directory that contains configuration files for the sample applications.

  * `idp` – a directory that contains the IdP sample application.

  * `sp` – a directory that contains the SP sample application.

  * `data.zip` – a PingFederate configuration archive to use with the sample applications.

  * `install.sh` – an installation shell script for the sample applications.

---

---
title: IdP single logout integration
description: When an IdP PingFederate server receives a request for SLO, it redirects the user's browser to the Logout Service defined in the IdP OpenToken Adapter configuration. The redirect URL includes an OpenToken containing the user attributes defined in the IdP OpenToken Adapter instance for the partner connection. The Logout Service should remove the user's session on the application server and redirect the user's browser back to the IdP PingFederate server. The diagram below shows the flow of IdP-initiated SLO, but the architecture would also support SP-initiated SLO.
component: php
page_id: php:setup:pf_php_ik_idp_single_logout_integration
canonical_url: https://docs.pingidentity.com/integrations/php/setup/pf_php_ik_idp_single_logout_integration.html
llms_txt: https://docs.pingidentity.com/integrations/php/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 21, 2024
---

# IdP single logout integration

When an IdP PingFederate server receives a request for SLO, it redirects the user's browser to the Logout Service defined in the IdP OpenToken Adapter configuration. The redirect URL includes an OpenToken containing the user attributes defined in the IdP OpenToken Adapter instance for the partner connection. The Logout Service should remove the user's session on the application server and redirect the user's browser back to the IdP PingFederate server. The diagram below shows the flow of IdP-initiated SLO, but the architecture would also support SP-initiated SLO.

![ypq1563995582468](_images/ypq1563995582468.jpg)

**Processing Steps**

1. User initiates a single logout request. The request targets the PingFederate server's `/idp/startSLO.ping` endpoint.

2. PingFederate sends a logout request and receives responses from all SPs registered for the current SSO session.

3. PingFederate redirects the request to the IdP Web application's Logout Service, which identifies and removes the user's session locally.

4. The application Logout Service redirects back to PingFederate to display a logout-success page.

   * [Sample code](pf_php_ik_idpslo_sample_code.html)

---

---
title: IdP single sign-on integration
description: When PingFederate is configured as an IdP, it needs to be able to identify a user prior to issuing a SAML assertion for that user. When using the OpenToken Adapter with PingFederate, this means that the PingFederate server attempts to read a cookie or query parameter containing an OpenToken and then use the values within to identify the user. The application that starts the SSO must include an OpenToken so that PingFederate can identify the user. Use the Agent API to write an OpenToken. The Agent API is a PHP object that provides access to functionality for writing an OpenToken to a given HTTP response.
component: php
page_id: php:setup:pf_php_ik_idp_single_sign_on_integration
canonical_url: https://docs.pingidentity.com/integrations/php/setup/pf_php_ik_idp_single_sign_on_integration.html
llms_txt: https://docs.pingidentity.com/integrations/php/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 21, 2024
---

# IdP single sign-on integration

When PingFederate is configured as an IdP, it needs to be able to identify a user prior to issuing a SAML assertion for that user. When using the OpenToken Adapter with PingFederate, this means that the PingFederate server attempts to read a cookie or query parameter containing an OpenToken and then use the values within to identify the user. The application that starts the SSO must include an OpenToken so that PingFederate can identify the user. Use the Agent API to write an OpenToken. The Agent API is a PHP object that provides access to functionality for writing an OpenToken to a given HTTP response.

The Agent Toolkit for PHP makes use of Namespaces, which enable the Agent API to be auto-loaded with other applications. For more information on auto-loading, see [Autoloading Classes](http://php.net/manual/en/language.oop5.autoload.php) in the PHP documentation.

|   |                                                                               |
| - | ----------------------------------------------------------------------------- |
|   | The sample code in this guide assumes that the Agent APIs are already loaded. |

The following is sample code for auto-loading. Other auto-loading frameworks such as [Zend](http://framework.zend.com) can be used instead.

```
spl_autoload_extensions(".php");
spl_autoload_register();
```

Instantiating the agent object is done simply by invoking a constructor, as in the example below:

```
<?php
   use pingidentity\opentoken\agent;
   $myagent = new Agent();
?>
```

When the agent object is instantiated, it uses the `config.php` file to find the configuration data generated when the OpenToken Adapter was configured. This configuration data includes the name of the cookie that the agent object will write, as well as the key to use when encrypting a new OpenToken. If the file specified in `config.php` is not found, the agent constructor will throw an exception.

The writeTokenToHTTPResponse method takes an array of attributes and encodes them into an OpenToken, which is then written to the HTTP response.

|   |                                                                                                                  |
| - | ---------------------------------------------------------------------------------------------------------------- |
|   | The array of attributes parameter must contain a key named "subject" in order for a valid token to be generated. |

If any errors are encountered while creating the token or writing it out to the response, the `lastError` attribute of the agent instance will contain a message with a description of the error.

---

---
title: Known issues and limitations
description: The following are known issues or limtiations for the PHP Integration Kit.
component: php
page_id: php:release_notes:pf_php_ik_known_issues_and_limitations
canonical_url: https://docs.pingidentity.com/integrations/php/release_notes/pf_php_ik_known_issues_and_limitations.html
llms_txt: https://docs.pingidentity.com/integrations/php/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 21, 2024
section_ids:
  known-issues: Known issues
  known-limitations: Known limitations
---

# Known issues and limitations

The following are known issues or limtiations for the PHP Integration Kit.

## Known issues

There are no known issues.

## Known limitations

* The Agent Toolkit for PHP supports AES/128/CBC and 3DES/168/CBC.

* The Agent Toolkit for PHP does *not* support AES/256/CBC.

* The **Token Name** field in the adapter configuration must be unique within the given federation, however is not enforced in the user-interface.

* The AES/256/CBC cipher suite is not supported, due to limitations in the PHP mcrypt libraries.

* All plain-text files have UNIX-style line feeds. This may result in difficulty editing files on a Windows computer.

* Password obfuscation is not supported by the agent.

* The sample application does not support local logout when set to cookie transport mode

* If the SP adapter is set to send extended attributes as cookies, multi-value attributes will fail, because multiple cookies with the same name are not allowed.

---

---
title: Overview of the SSO flow
description: The PHP Integration Kit consists of two parts:
component: php
page_id: php::pf_php_ik_overview_of_the_sso_flow
canonical_url: https://docs.pingidentity.com/integrations/php/pf_php_ik_overview_of_the_sso_flow.html
llms_txt: https://docs.pingidentity.com/integrations/php/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 5, 2024
---

# Overview of the SSO flow

The PHP Integration Kit consists of two parts:

* The OpenToken Adapter, which runs within the PingFederate server

* The Agent Toolkit for PHP, which resides within the PHP user application

The following figure shows a basic IdP-initiated single sign-on (SSO) scenario in which PingFederate federation servers using the PHP Integration Kit exist on both sides of the identity federation:

![guf1563995594120](_images/guf1563995594120.jpg)

**Processing Steps**

1. A user initiates an SSO transaction.

2. The IdP application inserts user attributes into the Agent Toolkit for PHP, which encrypts the data internally and generates an `OpenToken`.

3. A request containing the `OpenToken` is redirected to the PingFederate IdP server.

4. The server invokes the OpenToken IdP Adapter, which retrieves the `OpenToken`, decrypts, parses, and passes the user attributes to the PingFederate IdP server. The PingFederate IdP server then generates a Security Assertion Markup Language (SAML) assertion.

5. The SAML assertion is sent to the SP site.

6. The PingFederate SP server parses the SAML assertion and passes the user attributes to the OpenToken SP Adapter. The Adapter encrypts the data internally and generates an `OpenToken`.

7. A request containing the OpenToken is redirected to the SP application.

8. The Agent Toolkit for PHP decrypts and parses the OpenToken and makes the user attributes available to the SP Application.

   |   |                                                                                                                                                                                                                                                                                   |
   | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | PingFederate can be configured to look up additional attributes from either an IdP or SP data store. For more information, see [Datastores](https://docs.pingidentity.com/pingfederate/latest/introduction_to_pingfederate/pf_datastores.html) in the PingFederate documentation. |

---

---
title: Passing multi-value attributes
description: The Agent Toolkit for PHP supports passing multi-value attributes to PingFederate that will each appear in its own discrete <AttributeValue> element in the SAML 2.0 assertion or as a JSON array value in OAuth-based protocols. Multi-value attributes are passed using the MultiStringArray PHP class distributed with the Agent Toolkit for PHP.
component: php
page_id: php:setup:pf_php_ik_passing_multi_value_attributes
canonical_url: https://docs.pingidentity.com/integrations/php/setup/pf_php_ik_passing_multi_value_attributes.html
llms_txt: https://docs.pingidentity.com/integrations/php/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 5, 2024
---

# Passing multi-value attributes

The Agent Toolkit for PHP supports passing multi-value attributes to PingFederate that will each appear in its own discrete `<AttributeValue>` element in the SAML 2.0 assertion or as a JSON array value in OAuth-based protocols. Multi-value attributes are passed using the `MultiStringArray` PHP class distributed with the Agent Toolkit for PHP.

The following code snippet demonstrates how to pass multi-valued attributes using the Agent Toolkit for PHP:

```
 <?php
    # Use and instantiate an agent
    use pingidentity\opentoken\agent;

 use pingidentity\opentoken\helpers\multistringarray;
    $myagent = new Agent();

    # Setup an array of values
    $myvalues = MultiStringArray()

    # Single Value Attribute
    $myvalues->add(TOKEN_SUBJECT, <$userId>);

    #Multiple Value Attribute
    $myvalues->add("MultiValueAttr", "value1");
    $myvalues->add("MultiValueAttr", "value2");
    $myvalues->add("MultiValueAttr", "value3");

    # Generate and write the token to a cookie (assuming that's
    # our configuration)
    $myagent->writeTokenToHTTPResponse($myvalues);
 ?>
```

---

---
title: PHP Integration Kit
description: The PHP Integration Kit allows PHP applications to integrate with a PingFederate server acting as either an identity provider (IdP) or service provider (SP).
component: php
page_id: php::pf_php_ik
canonical_url: https://docs.pingidentity.com/integrations/php/pf_php_ik.html
llms_txt: https://docs.pingidentity.com/integrations/php/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 5, 2024
section_ids:
  components: Components
  intended-audience: Intended audience
  system-requirements: System requirements
---

# PHP Integration Kit

The PHP Integration Kit allows PHP applications to integrate with a PingFederate server acting as either an identity provider (IdP) or service provider (SP).

|   |                                                                                                                                                                                                                                                                                                         |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Updates and support have ended for this integration, because this integration relies on the "mcrypt" extension, which was deprecated after PHP 7.1. The availability of this user guide and the related product download is intended only for those who have existing solutions using this integration. |

|   |                                                                                                                                                                                                                                       |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | For new integrations, we encourage you to use the [Agentless Integration Kit](../agentless/pf_agentless_ik.html), which offers samesite cookie support and can integrate with a variety of platforms using a modern RESTful approach. |

## Components

* OpenToken adapter and agent

  * Allows developers to integrate their PHP applications with a PingFederate server acting as either an identity provider (IdP) or a service provider (SP). The integration kit allows an IdP server to receive user attributes from a PHP IdP application. On the SP side, the integration kit allows a PHP SP application to receive user attributes from the SP server.

* Sample applications

  * The Integration Kit distribution also contains sample IdP and SP applications. The applications may be installed quickly for testing OpenToken processing and to provide a working demonstration of end-to-end single sign-on (SSO) and single logout (SLO). Source code and supporting files are included in the distribution and may be modified or used as a reference for application developers.

## Intended audience

This document is intended for PingFederate administrators and web application developers.

Before starting, we recommend that you familiarize yourself with the following sections of the PingFederate documentation:

* [Identity provider SSO configuration](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_ident_provid_sso_config.html)

* [Service provider SSO configuration](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_servic_provid_sso_config.html)

* [OpenToken Adapter](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_opentoken_adapt.html)

## System requirements

* PingFederate 8.0 or later.

* A web server running PHP 5.4.8 to 7.1.

* The following extensions must be available on the PHP server:

  * `cURL` – enables IdP and SP applications to communicate with PingFederate. This is required for both the Windows and Linux installations of PHP 5.4.8.

  * `mcrypt` – used to encrypt and decrypt the OpenToken. Information and download: <https://php.net/mcrypt> and <http://mcrypt.sourceforge.net>.

  * `mhash` – used to generate `hmacs` and secure keys from passwords. Information and download: <https://php.net/mhash> and <http://mhash.sourceforge.net>.

  * `zlib` – used for data compression. The PHP kit uses the `gzuncompress` method to uncompress data. Information and download: <https://php.net/manual/en/ref.zlib.php>.

---

---
title: Receiving multi-value attributes
description: The Agent Toolkit for PHP receives multi-value attributes passed in the SAML assertion from PingFederate using the MultiStringArray PHP class distributed with the Agent Toolkit for PHP.
component: php
page_id: php:setup:pf_php_ik_receiving_multi_value_attributes
canonical_url: https://docs.pingidentity.com/integrations/php/setup/pf_php_ik_receiving_multi_value_attributes.html
llms_txt: https://docs.pingidentity.com/integrations/php/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 5, 2024
---

# Receiving multi-value attributes

The Agent Toolkit for PHP receives multi-value attributes passed in the SAML assertion from PingFederate using the MultiStringArray PHP class distributed with the Agent Toolkit for PHP.

The following code snippet demonstrates how to get the multi-value attributes using the Agent Toolkit for PHP:

```
 <?php
    # Use and instantiate an agent
    use pingidentity\opentoken\agent;
  use pingidentity\opentoken\helpers\multistringarray;

      $myagent = new Agent();

      # read OpenToken into a MultiStringArray ($userInfo)
      $userInfo = $myagent->readTokenFromHttpRequestToMultiStringArray();

      # retrieve single value attribute
      $username = $userinfo->get(TOKEN_SUBJECT, 0);

      # retrieve multiple value attribute. Returns an array of values.
      $multiValues = $userinfo->get("MultiValueAttr");

 ?>
```

---

---
title: Sample application setup
description: To see a working demonstration of the PHP Integration Kit, you can deploy the included sample applications.
component: php
page_id: php:setup:pf_php_ik_sample_application_setup
canonical_url: https://docs.pingidentity.com/integrations/php/setup/pf_php_ik_sample_application_setup.html
llms_txt: https://docs.pingidentity.com/integrations/php/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 21, 2024
section_ids:
  components: Components
  intended-audience: Intended audience
  system-requirements: System requirements
---

# Sample application setup

To see a working demonstration of the PHP Integration Kit, you can deploy the included sample applications.

## Components

* Identity provider (IdP) sample application

  * Acts as an IdP application in your demonstration environment.

* Service provider (SP) sample application

  * Acts as an SP application in your demonstration environment.

* PingFederate configuration archive

  * This data.zip archive automatically configures PingFederate with OpenToken Adapter instances to work with the two sample applications.

  * The IdP server looks up and sends authentication information to the SP.

  * The SP server forwards this information to the SP sample application to create the local user session.

  * The SP server also sends authentication requests to the IdP on behalf of local users.

## Intended audience

The installation and basic usage portions of this guide are intended for PingFederate administrators and web-application architects and developers who want to test the deployment of the PHP Integration Kit or validate end-to-end integration. Some knowledge of the PingFederate administrative console and identity federation using SAML is helpful but not required.

Sections describing the optional use of the PHP source code and advanced alternative deployment scenarios are intended, respectively, for experienced PHP developers and administrators with some expertise using and deploying PingFederate in a production environment.

## System requirements

* PingFederate 9.0 or later.

* A web server running PHP 5.4.8 or later.

* The OpenToken Adapter (included).

* A PHP server with the following:

  * The cURL, mcrypt, mhash, and zlib extensions installed.

  * The correct time (recently synchronized).

  * The correct time zone. Set the correct time zone in your `php.ini` file. For example, `date.timezone = America/Halifax;`

    For a list of supported time zones, see [Timezones](http://php.net/manual/en/timezones.php) in the PHP documentation.

* The Appropriate Error reporting Level in php.ini file:

  `error_reporting = E_ALL & ~E_DEPRECATED & ~E_STRICT;`

* The installation script is designed for Apache HTTP server on a Linux platform derived from Red Hat.

* The `data.zip` configuration archive assumes that your PHP server is on the same machine as PingFederate.

---

---
title: Sample code
description: Below is an example code snippet for processing a logout request and redirecting the user's browser back to PingFederate:
component: php
page_id: php:setup:pf_php_ik_idpslo_sample_code
canonical_url: https://docs.pingidentity.com/integrations/php/setup/pf_php_ik_idpslo_sample_code.html
llms_txt: https://docs.pingidentity.com/integrations/php/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 5, 2024
---

# Sample code

Below is an example code snippet for processing a logout request and redirecting the user's browser back to PingFederate:

```
 <?php
     # Use and instantiate an agent
     use pingidentity\opentoken\agent;
     $myagent = new Agent();

     # Setup an array of values
     $myvalues = array(TOKEN_SUBJECT => "user1");

     # Generate and write the token to a string (assuming that's
     # our configuration)
     $queryParam = $myagent->writeTokenToHTTPResponse($myvalues);

     $resumePath = $_GET['resume'];
     $returnUrl = "https://<SERVER_NAME>:9031/" . $resumePath;

     session_destroy();
     ob_end_clean();

     if ($queryParam)
     {
       if (strpos($returnUrl, "?") == FALSE)
       {
         $returnUrl = $returnUrl . "?";
       }
       $returnUrl = $returnUrl . $queryParam;
     }

     header("Location: " . $returnUrl);
 ?>
```

---

---
title: Sample code
description: The code snippet below demonstrates the use of the writeTokenToHTTPResponse method:
component: php
page_id: php:setup:pf_php_ik_idpsso_sample_code
canonical_url: https://docs.pingidentity.com/integrations/php/setup/pf_php_ik_idpsso_sample_code.html
llms_txt: https://docs.pingidentity.com/integrations/php/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 5, 2024
---

# Sample code

The code snippet below demonstrates the use of the `writeTokenToHTTPResponse` method:

```
 <?php
    # Use and instantiate an agent
    use pingidentity\opentoken\agent;
    $myagent = new Agent();

    # Setup an array of values
    $myvalues = array(TOKEN_SUBJECT => "$userId");

    # Generate and write the token to a cookie (assuming that's
    # our configuration)
    $myagent->writeTokenToHTTPResponse($myvalues);
?>
```