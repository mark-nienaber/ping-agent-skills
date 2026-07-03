---
title: Apache module configuration
description: "The configuration options for the Apache module are listed in the table below. Update the directives as needed in the module's configuration file: <apache installation>/conf/extra/httpd-pfoam.conf"
component: oam
page_id: oam:setup:pf_oam_ik_apache_module_configuration
canonical_url: https://docs.pingidentity.com/integrations/oam/setup/pf_oam_ik_apache_module_configuration.html
revdate: June 21, 2024
---

# Apache module configuration

The configuration options for the Apache module are listed in the table below. Update the directives as needed in the module's configuration file: `<apache installation>/conf/extra/httpd-pfoam.conf`

**Table 1. Configuration directives**

| Field                     | Description                                                                                         | Default Value  |
| ------------------------- | --------------------------------------------------------------------------------------------------- | -------------- |
| OAMCookieName             | Cookie name containing the OAM 11g Session Token. Example: `OAMAuthnCookie_webgate.mydomain.com:80` | n/a            |
| PFResumePath              | Parameter containing the relative sso url passed from PingFederate                                  | resumePath     |
| SessionTokenParameterName | Parameter Name used to pass OAM session token to PingFederate                                       | OAMAuthnCookie |
| PFBaseUrl                 | Base URL for PingFederate used in conjunction with resumePath. Example: `https://mydomain.com:9031` | n/a            |

|   |                                                               |
| - | ------------------------------------------------------------- |
|   | Restart the Apache server after making configuration changes. |

---

---
title: Apache module installation
description: This procedure shows you how to add the mod_pfoam.so module to your Apache installation.
component: oam
page_id: oam:setup:pf_oam_ik_apache_module_installation
canonical_url: https://docs.pingidentity.com/integrations/oam/setup/pf_oam_ik_apache_module_installation.html
revdate: July 5, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Apache module installation

## About this task

This procedure shows you how to add the `mod_pfoam.so` module to your Apache installation.

## Steps

1. Download the OAM Integration Kit `.zip` archive from the [**Add-ons** tab of the PingFederate downloads page](https://www.pingidentity.com/en/resources/downloads/pingfederate.html) or the [Ping Identity Marketplace](https://marketplace.pingone.com/item/integration-kit-for-oracle-access-manager).

2. Stop PingFederate.

3. From the extracted distribution `.zip` archive:

   1. Copy `dist/mod_pfoam.so` to `<apache installation>/modules`.

   2. Copy `conf/httpd-pfoam.conf` to `<apache installation>/conf/extra`.

4. Open your Apache server configuration file (`httpd.conf`).

5. Look for the first `LoadModule` directive in the `httpd.conf` file.

6. Immediately before the `LoadModule` directive, insert the following line:

   `LoadModule pfoam module`

7. At the end of the `httpd.conf` file, insert the following line:

   `Include conf/extra/httpd-pfoam.conf`

---

---
title: Changelog
description: OAM Integration Kit 3.1 – April 2018 (Current Release)
component: oam
page_id: oam:release_notes:pf_oam_ik_changelog
canonical_url: https://docs.pingidentity.com/integrations/oam/release_notes/pf_oam_ik_changelog.html
revdate: June 21, 2024
---

# Changelog

**OAM Integration Kit 3.1 – April 2018 (Current Release)**

* Added support for dynamic target resources: The adapter now uses the target resource contained within the request to determine where the user should be redirected to after successful SSO.

* Bug fix: The adapter will include the value of the Access Manager parameter OAM\_REQ in the response if it was present in the initial request (as required by the OAM Server)

* Security update

**OAM Integration Kit 3.0 – May 2016**

* Initial Release

---

---
title: Download manifest
description: The distribution .zip archive for the OAM Integration Kit contains the following:
component: oam
page_id: oam:release_notes:pf_oam_ik_download_manifest
canonical_url: https://docs.pingidentity.com/integrations/oam/release_notes/pf_oam_ik_download_manifest.html
revdate: June 21, 2024
---

# Download manifest

The distribution `.zip` archive for the OAM Integration Kit contains the following:

* ReadMeFirst.pdf

* /dist - contains libraries needed to run the adapter

  * pf-oam-adapter-3.1.0.jar - OAM Adapter JAR file

  * mod\_pfoam.so - Apache 2.4 Module, compiled on Redhat 6.7

  * PingOpenTokenAuthPlugin.jar - OAM Authentication plugin used for SP use case

* /conf - contains libraries needed to run the adapter:

  * httpd-pfoam.conf - Sample Apache configuration file for mod\_pfoam.so

  * jps-config.xml - OAM configuration file

---

---
title: IdP adapter instance configuration
description: After installing the OAM Integration Kit and the Access Server SDK library, you can configure your SP connection to use an instance of the OAM Adapter. The first part of this process is configuring the adapter instance.
component: oam
page_id: oam:setup:pf_oam_ik_idp_adapter_instance_configuration
canonical_url: https://docs.pingidentity.com/integrations/oam/setup/pf_oam_ik_idp_adapter_instance_configuration.html
revdate: July 5, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
  result: Result
---

# IdP adapter instance configuration

## About this task

After installing the OAM Integration Kit and the Access Server SDK library, you can configure your SP connection to use an instance of the OAM Adapter. The first part of this process is configuring the adapter instance.

## Steps

1. Log on to the PingFederate administrative console and click Adapters under IdP Configuration on the Main Menu screen.

2. On the Manage IdP Adapter Instances screen, click Create New Instance.

3. Enter the Adapter Name and Adapter ID. Select OAM 11g IdP Adapter 3.1.0 as the Adapter Type and click Next.

4. On the IdP Adapter screen, enter the values for adapter configuration as described on the screen and click Next.

   ![hss1563995550350](_images/hss1563995550350.png)

   |   |                                                                                                                                                                                                                                                                                       |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | The Authentication Level Identifier is taken from the user's session token. The default/recommended value is authLevel. For the user's Authentication Level to be sent in the assertion, you must add the Authentication Level Identifier to the Adapter Contract (see step 5 below). |

5. Optionally, on the Extended Adapter Contract screen, you can configure additional attributes for the adapter. For instance, you can use the extended adapter contract for Policy Server response-object attributes. For more information, see [Extending an IdP adapter contract](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_extending_idp_adapter_contract.html) in the PingFederate documentation.

6. Click Next.

7. Select userId as the unique id. You may also select any extended attributes specified in the previous screen.

8. On the Summary screen, verify that the information is correct and click Done.

9. On the Manage Adapter Instances screen, click Save to complete the adapter configuration.

   ## Result

   You can now use this adapter instance for an SP connection. For information on setting up or modifying a connection, see [SP connection management](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_sp_connect_management.html) in the PingFederate documentation.

---

---
title: IdP adapter testing
description: You can test this adapter using the SP sample application that ships with PingFederate. Follow this procedure to verify adapter functions:
component: oam
page_id: oam:setup:pf_oam_ik_idp_adapter_testing
canonical_url: https://docs.pingidentity.com/integrations/oam/setup/pf_oam_ik_idp_adapter_testing.html
revdate: July 5, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
  result: Result
---

# IdP adapter testing

## About this task

You can test this adapter using the SP sample application that ships with PingFederate. Follow this procedure to verify adapter functions:

## Steps

1. Set up PingFederate to run the SP sample application according to instructions in the Sample Application Quick Start Guide.

2. Configure an instance of the OAM Adapter (see [OAM IdP configuration](pf_oam_ik_oam_idp_configuration.html)).

3. Reconfigure the SP connection to the sample application to use the OAM Adapter Instance by deleting the existing adapter instance and map the OAM Adapter instance in its place. See [Managing mappings](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_managing_mappings.html) in the PingFederate documentation.

   |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
   | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | Use the default setting on the Assertion Mapping screen. On the Attribute Contract Fulfillment screen, map SAML\_SUBJECT to the Adapter value userId. If you have extended the Adapter Contract and wish to send the extended-attribute value to the SP during SSO, you will need to add a corresponding attribute to the Attribute Contract for the SP connection. Then map this attribute to the additional adapter attribute value (for example, authLevel).For any attributes in the Attribute Contract for which there are no related Adapter attributes, select Text in the Source drop-down list for each attribute and enter "test" (or any other text) in the associated text boxes. |

4. On a web page protected by the OAM Access Gate, create an "SSO" link to the PingFederate startSSO endpoint, including the sample SP's connection ID, in the following format:

   `http[s]://<PF_host>:<port>/IdP/startSSO.ping?PartnerIdPId=<connection_id>`

   where:

   * \<PF\_host> is the machine running the PingFederate server

   * \<port> is the PingFederate port and

   * \<connection\_id> is the Connection ID of the SP connection to the sample application.

5. Access the protected web page by authenticating through OAM Webgate, and click the SSO link.

   ## Result

   You will be logged on to the sample SP application. If you have modified the connection Attribute Contract to include Authentication Level and extended the Adapter Contract, you should see the authLevel displayed in the "User Attributes" table.

---

---
title: IdP implementation
description: This section describes using the OAM Integration Kit as an identity provider (IdP).
component: oam
page_id: oam:setup:pf_oam_ik_idp_implementation
canonical_url: https://docs.pingidentity.com/integrations/oam/setup/pf_oam_ik_idp_implementation.html
revdate: June 21, 2024
---

# IdP implementation

This section describes using the OAM Integration Kit as an identity provider (IdP).

The OAM IdP Adapter uses the Access Server SDK to decrypt the OAM session cookie and pass attributes to the PingFederate server. You can then add attribute values to the Attribute Contract in the PingFederate administrative console and transfer them to a partner application in a SAML assertion. (For more information, see: Creating an Attribute Contract in the PingFederate Administrator's Manual.)

The following figure illustrates the request flow and how the OAM IdP Adapter is used to facilitate generating a SAML WS-Federation assertion from the ObSSOCookie:

![OAM IdP Overview](_images/dju1563995548553.png)OAM IdP Overview

**Processing Steps**

1. User initiates single sign on through PingFederate.

2. The OAM IdP Adapter redirects the user to an OAM Protected Resource.

3. OAM Webgate authenticates the user.

4. After successful authentication an OAM 11g session is established and a host level cookie is created for the Webgate.

5. User is allowed access to the OAM protected resource at which point the Ping Web Filter intercepts this request and sends the host level OAM Session token to PingFederate.

6. OAM IdP Adapter validates the session token using Access Server APIs.

7. The user information is passed to PingFederate, which can create an assertion and send it to the required relying party (aka service provider).

   * [OAM IdP configuration](pf_oam_ik_oam_idp_configuration.html)

   * [Apache module installation](pf_oam_ik_apache_module_installation.html)

   * [Apache module configuration](pf_oam_ik_apache_module_configuration.html)

   * [PingFederate IdP configuration](pf_oam_ik_pf_idp_configuration.html)

   * [IdP adapter instance configuration](pf_oam_ik_idp_adapter_instance_configuration.html)

   * [IdP adapter testing](pf_oam_ik_idp_adapter_testing.html)

---

---
title: Known issues and limitations
description: Known Issues
component: oam
page_id: oam:release_notes:pf_oam_ik_known_issues_and_limitations
canonical_url: https://docs.pingidentity.com/integrations/oam/release_notes/pf_oam_ik_known_issues_and_limitations.html
revdate: June 21, 2024
---

# Known issues and limitations

**Known Issues**

* If the following error is raised in the server.log, perform the steps listed to resolve the issue:

  ```
  ERROR [SystemErr] oracle.security.am.common.nap.ObMessageChannelImpldoSSLHandShake
  SEVERE: SSL handshake error sun.security.validator.ValidatorException:
  PKIX path validation failed: java.security.cert.CertPathValidatorException:
  Algorithm constraints check failed on disabled signature algorithm: MD5withRSA
  ```

  **Steps to resolve:**

  1. Edit `<JAVA_HOME>/jre/lib/security/java.security`.

  2. Remove the value `MD5` from the property: `jdk.certpath.disabledAlgorithms`.

  3. Remove the value `MD5withRSA` from the property: `jdk.tls.disabledAlgorithms`.

  4. Save the file and restart PingFederate.

**Known Limitations**

* The PingFederate instance, acting as the Service Provider Server and implementing the OAM Integration Kit, must be in the same domain as the OAM Access Server.

* The OAM Access Server may return additional values not specified in the IdP adapter's extended contract. For instance, for an LDAP lookup, the OAM Access Server may send a userDN. In order to perform attribute masking on these additional values, you must add the fields to the extended adapter contract, then and mask the attribute there.

* The OAM adapters are designed for Single Sign-On only. Single Log-Out is not supported in this release.

* Any attribute being mapped to SAML\_SUBJECT, such as userId, will not be masked in the server.log file even if it is marked as such. This is because SAML standard already provides facilities for ensuring privacy and confidentiality of the SAML\_SUBJECT, and can never be masked by PingFederate.

* Failing to run the configureAccessGate or similar utility in the OAM SDK will result in an error saying that OBACCESS\_INSTALL\_DIR has not been set. Refer to your OAM SDK documentation for more information.

* Placing the authn\_pingfed.dll in the wrong directory will result in the same OBACCESS\_INSTALL\_DIR error. Be sure to copy authn\_pingfed.dll plug-in to the Access Server lib path, not the Access Server SDK lib path.

* The authn\_pingfed.dll packaged with the kit has been tested against OAM 6.1 (NetPoint COREid 6.1).

* Any attributes returned by an OAM Action will always be masked in the server.log file as they are being gathered by the adapter.

* Due to the difficulty and complexity of setting up a OAM environment, limited configuration elements were tested with regard to this installation. Please consult your OAM Access Server User Manuals for details on configuring these products.

---

---
title: OAM IdP configuration
description: These steps are necessary to configure OAM for operation as an identity provider (IdP) with PingFederate.
component: oam
page_id: oam:setup:pf_oam_ik_oam_idp_configuration
canonical_url: https://docs.pingidentity.com/integrations/oam/setup/pf_oam_ik_oam_idp_configuration.html
revdate: July 5, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# OAM IdP configuration

## About this task

These steps are necessary to configure OAM for operation as an identity provider (IdP) with PingFederate.

|   |                                                                                                                                                                                                       |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | You can find more information on the Webgate configuration files in [OAM documentation](https://docs.oracle.com/cd/E40329_01/doc.1112/e49451/webgate_apache.htm#WGINS76171) for configuring Webgates. |

## Steps

1. Create an OAM Apache 11g Webgate (or use an existing one).

2. Create a new folder in the PingFederate Server, to store the Webgate configuration files. This folder will henceforth be referred to as the Agent Config Location. This path must be specified during the PingFederate Configuration.

3. Copy the Webgate configuration files to the Agent Config Location folder.

---

---
title: OAM SP configuration
description: From the extracted distribution .zip archive, deploy the authentication plug-in jar, dist/PingOpenTokenAuthPlugin.jar, within OAM 11g and create an Authentication Module. For information on authentication plugins see About the Custom Plug-in Life Cycle in the OAM documentation.
component: oam
page_id: oam:setup:pf_oam_ik_oam_sp_configuration
canonical_url: https://docs.pingidentity.com/integrations/oam/setup/pf_oam_ik_oam_sp_configuration.html
revdate: June 21, 2024
section_ids:
  steps: Steps
---

# OAM SP configuration

## Steps

1. From the extracted distribution `.zip` archive, deploy the authentication plug-in jar, `dist/PingOpenTokenAuthPlugin.jar`, within OAM 11g and create an Authentication Module. For information on authentication plugins see [About the Custom Plug-in Life Cycle](https://docs.oracle.com/cd/E27559_01/dev.1112/e27134/authnapi.htm#AIDEV191) in the OAM documentation.

2. The authentication plugin requires the opentoken configuration file (agent-config.txt) which can be obtained through the SP adapter configuration as described in the section below. Specify the location of this file for the authentication plugin property *opentokenConfigFile*.

3. Create or update an authentication scheme to use the plug-in deployed in Step 1. Use the following values for the authentication scheme parameters.

   **Table 1. Configuration directives**

   | Parameter              | Value                                                    |
   | ---------------------- | -------------------------------------------------------- |
   | Challenge Method       | Form                                                     |
   | Challenge Redirect URL | `/oam/server/`                                           |
   | Authentication Module  | Select the authentication module from step 1.            |
   | Challenge URL          | `\http(s)://<PF_HOST:PF_PORT>/ext/pf-oam-authn/sso.ping` |
   | Context Type           | external                                                 |

4. Configure an OAM Webgate to use the updated authentication scheme.

---

---
title: Oracle Access Manager (OAM) Integration Kit
description: The PingFederate Oracle Access Manager (OAM) Integration Kit adds Identity Provider (IdP) and Service Provider (SP) Adapters to PingFederate.
component: oam
page_id: oam::pf_oam_ik
canonical_url: https://docs.pingidentity.com/integrations/oam/pf_oam_ik.html
revdate: June 21, 2024
section_ids:
  intended-audience: Intended audience
  system-requirements: System requirements
---

# Oracle Access Manager (OAM) Integration Kit

The PingFederate Oracle Access Manager (OAM) Integration Kit adds Identity Provider (IdP) and Service Provider (SP) Adapters to PingFederate.

The OAM IdP Adapter allows an IdP enterprise to extend an existing OAM investment by using the SAML or WS-Federation protocols to expand the reach of the OAM domain to partner applications. The OAM SP Adapter allows an SP enterprise to accept SAML or WS-Federation assertions and provide SSO to OAM-protected applications

## Intended audience

This document is intended for PingFederate administrators and web application developers.

If you need help during the setup process, see the following sections of the PingFederate documentation:

* [Managing SP adapters](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_adaptermanagementtasklet_spadaptermanagementstate.html)

* [Configuring an OpenToken SP Adapter instance](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_config_opentoken_sp_adapt_instance.html)

## System requirements

* PingFederate 8.x or later

* OAM Server 11g R2

* OAM Access SDK11.1.2.3.0 (installed on the same machine running the PingFederate server)

* OAM 11g Webgate running on Apache 2.4

* Redhat 6.7 (if using the precompiled module included in this distribution

---

---
title: PingFederate IdP configuration
description: Unzip the distribution .zip archive and copy this file to the server/default/deploy folder in your PingFederate server installation:
component: oam
page_id: oam:setup:pf_oam_ik_pf_idp_configuration
canonical_url: https://docs.pingidentity.com/integrations/oam/setup/pf_oam_ik_pf_idp_configuration.html
revdate: July 5, 2024
section_ids:
  steps: Steps
---

# PingFederate IdP configuration

## Steps

1. Unzip the distribution `.zip` archive and copy this file to the server/default/deploy folder in your PingFederate server installation:

   `dist/pf-oam-adapter-3.1.0.jar`

2. Copy the following file to the Agent Config Location folder, which was created in Step 2 of [OAM IdP configuration](pf_oam_ik_oam_idp_configuration.html):

   `conf/jps-config.xml`

3. Add the following to `run.properties` within `<PF_HOME>/bin` folder:

   `oracle.security.jps.config=<AGENT_CONFIG_LOCATION>/jps-config.xml`

   |   |                                                                                      |
   | - | ------------------------------------------------------------------------------------ |
   |   | Ensure that the Agent Config Location path uses forward slashes (/), as shown above. |

4. Install and configure the OAM Access Server SDK. For information on the Access Server SDK, refer to your OAM documentation.

   |   |                                                                                                                                                       |
   | - | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | The Access Server SDK functions as a gate to the OAM Access Server and some files will need to be copied to the server where PingFederate is running. |

5. Copy the following files from the Access Server SDK to `<PF_INSTALL>/server/default/deploy`:

   * `oamasdk-api.jar`

   * `opss_standalone/modules/`

     * `oracle.idm_11.1.1/identitystore.jar`

     * `oracle.pki_11.1.1/oraclepki.jar`

     * `oracle.jps_11.1.1/* (all files)`

     * `oracle.osdt_11.1.1/* (all files)`

       |   |                                                                                                                                               |
       | - | --------------------------------------------------------------------------------------------------------------------------------------------- |
       |   | The files listed above pertain to the specified version of the OAM SDK in the System Requirements. Other versions may require different files |

6. Start or restart the PingFederate server.

---

---
title: PingFederate SP configuration
description: Unzip the distribution .zip archive and copy the following file to the server/default/deploy folder in your PingFederate server installation:
component: oam
page_id: oam:setup:pf_oam_ik_pf_sp_configuration
canonical_url: https://docs.pingidentity.com/integrations/oam/setup/pf_oam_ik_pf_sp_configuration.html
revdate: July 5, 2024
section_ids:
  steps: Steps
---

# PingFederate SP configuration

## Steps

1. Unzip the distribution `.zip` archive and copy the following file to the `server/default/deploy` folder in your PingFederate server installation:

   `dist/pf-oam-adapter-3.1.0.jar`

2. Add the following to `<PF_INSTALL>/bin/run.properties`:

   `pf.oam.ik.ssoUrl=<PF_SSO_URL>`

   where PF\_SSO\_URL is the Sp-initiated Single sign on URL. For example:

   ```
   https://<PF_HOST>:<PF_PORT>/sp/startSSO.ping?PartnerIdpId=<PARTNER_ID>
   ```

   |   |                                                                                         |
   | - | --------------------------------------------------------------------------------------- |
   |   | The Target Resource URL will be determined by the adapter based on the request context. |

3. Start or restart the PingFederate Server.

---

---
title: SP adapter instance configuration
description: After installing the OAM Integration Kit, you can configure your SP connection to use an instance of the OAM SP Adapter. The first part of this process is configuring the adapter instance.
component: oam
page_id: oam:setup:pf_oam_ik_sp_adapter_instance_configuration
canonical_url: https://docs.pingidentity.com/integrations/oam/setup/pf_oam_ik_sp_adapter_instance_configuration.html
revdate: July 5, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
  result: Result
---

# SP adapter instance configuration

## About this task

After installing the OAM Integration Kit, you can configure your SP connection to use an instance of the OAM SP Adapter. The first part of this process is configuring the adapter instance.

## Steps

1. Log on to the PingFederate administrative console and click Adapters under SP Configuration on the Main Menu screen.

2. On the Manage SP Adapter Instances screen, click Create New Instance.

3. Enter the Adapter Name and Adapter ID. Select OAM 11g SP Adapter 3.1.0 as the Adapter Type and click Next.

4. On the SP Adapter screen, enter the values for adapter configuration as described on the screen and click Next.

   ![SP Instance Configuration](_images/kfv1563995553325.png)Figure 1. SP Instance Configuration

5. Download the opentoken configuration file (agent-config.txt). This will be used during authentication plugin configuration for the OAM server. Click Next.

6. Optionally, on the Extended Adapter Contract screen, you can configure additional attributes for the adapter. (See the Extending an Adapter Contract in the PingFederate Administrator's Manual.)

   |   |                                                                               |
   | - | ----------------------------------------------------------------------------- |
   |   | Extended attributes are not supported in this version of OAM Integration Kit. |

7. Click Next.

8. On the Summary screen, verify that the information is correct and click Done.

9. On the Manage Adapter Instances screen, click Save to complete the adapter configuration.

   ## Result

   You can now use this adapter instance for an IdP connection. For information on setting up or modifying a connection, see [Managing IdP adapters](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_managing_idp_adapters.html) in the PingFederate documentation.

---

---
title: SP adapter testing
description: You can test this adapter using the IdP sample application that ships with PingFederate. Follow this procedure to verify adapter functions:
component: oam
page_id: oam:setup:pf_oam_ik_sp_adapter_testing
canonical_url: https://docs.pingidentity.com/integrations/oam/setup/pf_oam_ik_sp_adapter_testing.html
revdate: July 5, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
  result: Result
---

# SP adapter testing

## About this task

You can test this adapter using the IdP sample application that ships with PingFederate. Follow this procedure to verify adapter functions:

## Steps

1. Set up PingFederate to run the IdP sample application according to instructions in the Sample ApplicationQuick Start Guide.

2. Configure an instance of the OAM SP Adapter (see [OAM SP configuration](pf_oam_ik_oam_sp_configuration.html)).

3. Reconfigure the IdP connection to the sample application to use the OAM Adapter instance by deleting the existing adapter instance for the connection and mapping the OAM Adapter instance in its place (see Configuring Adapter Mapping and User Lookup in the PingFederate Administrator's Manual).

4. From the Main Menu, click Adapters under My SP Configuration on the Main Menu screen.

5. Delete the Adapter Instance that was previously used by the sample-application connection.

6. Configure an OAM 11g Webgate to use the custom authentication plug-in.

7. Access an OAM protected resource within the OAM 11g Webgate from the previous step. You should arrive at the IdP sample application's login page.

8. Add at least one of the users in the username drop-down list to the OAM Identity Manager. Refer to your OAM documentation for more information.

   Alternatively, you can add users already in OAM Identity Manager to the sample application's user-properties file (see the *Quick Start Guide* for the location of this file).

9. Add the same user(s) to the Authorization Rule in the Policy Domain governing the protected Web page.

10. On the IdP sample application's login page, log in with a username managed by OAM.

    ## Result

    You should be allowed access to OAM-protected Web page.

---

---
title: SP implementation
description: The OAM SP Adapter uses an authentication scheme deployed within Oracle Access Manager to create a session for the user.
component: oam
page_id: oam:setup:pf_oam_ik_sp_implementation
canonical_url: https://docs.pingidentity.com/integrations/oam/setup/pf_oam_ik_sp_implementation.html
revdate: June 21, 2024
---

# SP implementation

The OAM SP Adapter uses an authentication scheme deployed within Oracle Access Manager to create a session for the user.

The following figure illustrates the request flow and how the OAM SP Adapter is used to facilitate using a SAML WS-Federation assertion to create an OAM session:

![OAM SP Implementation](_images/acg1563995552020.png)OAM SP Implementation

**Processing Steps**

1. An SSO assertion is sent to PingFederate acting as an SP.

2. The OAM Sp Adapter redirects the user to an OAM Protected Resource secured with a PingFederate custom authentication scheme.

3. OAM Webgate sends a request to authenticate the user.

4. OAM Server redirects the authentication request to PingFederate.

5. OAM SP Adapter sends the required credentials back to the OAM Server.

6. The OAM Server validates the credentials and an 11g session is established.

   * [OAM SP configuration](pf_oam_ik_oam_sp_configuration.html)

   * [PingFederate SP configuration](pf_oam_ik_pf_sp_configuration.html)

   * [SP adapter instance configuration](pf_oam_ik_sp_adapter_instance_configuration.html)

   * [SP adapter testing](pf_oam_ik_sp_adapter_testing.html)

---

---
title: Upgrade instructions
description: Use the following instructions to upgrade an existing OAM 3.0 installation to the current version.
component: oam
page_id: oam:setup:pf_oam_ik_upgrade_instructions
canonical_url: https://docs.pingidentity.com/integrations/oam/setup/pf_oam_ik_upgrade_instructions.html
revdate: June 21, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Upgrade instructions

## About this task

Use the following instructions to upgrade an existing OAM 3.0 installation to the current version.

## Steps

1. Stop PingFederate.

2. Delete the previous adapter: `<PF_INSTALL>/server/default/deploy/pf-oam-adapter-*.jar`

3. From the extracted distribution `.zip` archive:

   * Copy `dist/mod_pfoam.so` to `<apache installation>/modules`

   * Copy `dist/pf-oam-adapter-3.1.0.jar` to `<PF_INSTALL>/server/default/deploy`

4. Copy the following files from the Access Server SDK to `<PF_INSTALL>/server/default/deploy`:

   * oamasdk-api.jar

   * opss\_standalone/modules/

     * oracle.idm\_11.1.1/identitystore.jar

     * oracle.pki\_11.1.1/oraclepki.jar

     * oracle.jps\_11.1.1/\* (all files)

     * oracle.osdt\_11.1.1/\* (all files)

       |   |                                                                                                                                                |
       | - | ---------------------------------------------------------------------------------------------------------------------------------------------- |
       |   | The files listed above pertain to the specified version of the OAM SDK in the System Requirements. Other versions may require different files. |

5. Start PingFederate.

6. Verify configuration within PingFederate for all OAM IdP Adapters.

---

---
title: Upgrade instructions
description: Use the following instructions to upgrade an existing OAM 3.0 installation to the current version.
component: oam
page_id: oam:setup:szw1563995039121
canonical_url: https://docs.pingidentity.com/integrations/oam/setup/szw1563995039121.html
revdate: June 21, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Upgrade instructions

## About this task

Use the following instructions to upgrade an existing OAM 3.0 installation to the current version.

## Steps

1. Stop PingFederate.

2. Delete the previous adapter: `<PF_INSTALL>/server/default/deploy/pf-oam-adapter-*.jar`

3. From the extracted distribution `.zip` archive, copy `dist/pf-oam-adapter-3.1.0.jar` to `<PF_INSTALL>/server/default/deploy`

4. Edit `<PF_INSTALL>/bin/run.properties` to remove the `TargetResource` query parameter from the property `pf.oam.ik.ssoUrl`. For example, the URL should look similar to: `https://<PF_HOST>:<PF_PORT>/sp/startSSO.ping?PartnerIdpId=<PARTNER_ID>`

5. Start PingFederate.

6. Verify configuration within PingFederate for all OAM SP Adapters.