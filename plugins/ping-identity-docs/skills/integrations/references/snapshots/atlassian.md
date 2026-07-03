---
title: Atlassian Cloud Provisioner
description: The Atlassian Cloud Provisioner allows PingFederate to integrate with Atlassian Cloud for user and group provisioning and single sign-on (SSO).
component: atlassian
page_id: atlassian:atlassian_cloud_provisioner:pf_atlassian_cloud_connector
canonical_url: https://docs.pingidentity.com/integrations/atlassian/atlassian_cloud_provisioner/pf_atlassian_cloud_connector.html
revdate: July 3, 2024
section_ids:
  features: Features
  intended-audience: Intended audience
  system-requirements: System requirements
---

# Atlassian Cloud Provisioner

The Atlassian Cloud Provisioner allows PingFederate to integrate with Atlassian Cloud for user and group provisioning and single sign-on (SSO).

## Features

* Manages users in Atlassian Cloud based on changes in an external data store that is attached to PingFederate.

  * Creates, updates, disable, and delete users.

  * Allows you to enable the create, update, disable, and delete capabilities independently.

  * Allows you to choose to disable or delete users when deprovisioning.

  * Allows you to provision disabled users.

  * Creates and deletes groups.

  * Updates group memberships.

* Browser-based single sign-on (SSO) initiated by the service provider (SP) or identity provider (IdP).

* Pre-populates some connection settings with the included quick connection template and SAML metadata file.

## Intended audience

This document is intended for PingFederate administrators. Before you start, familiarize yourself with:

* The following sections of the Atlassian Cloud documentation:

  * [Atlassian organizations](https://confluence.atlassian.com/cloud/atlassian-organizations-964957873.html)

  * [User provisioning](https://confluence.atlassian.com/cloud/user-provisioning-959305316.html)

  * [SAML single sign-on](https://confluence.atlassian.com/cloud/saml-single-sign-on-943953302.html)

* The following sections of the PingFederate documentation:

  * [Identity provider SSO configuration](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_ident_provid_sso_config.html)

  * [Datastores](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_managedatasourcestasklet_managedatasourcesstate.html)

  * [Managing IdP adapters](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_managing_idp_adapters.html)

  * [Managing digital signing certificates and decryption keys](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_certmanagementtasklet_dsigsigningcert_certmanagementstate.html)

  * [SP connection management](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_sp_connect_management.html)

  * [Configuring outbound provisioning](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_spconnectionconfigtasklet_saasprovisioningstate.html)

  * [Configuring outbound provisioning settings](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_protocolsettingstasklet_saasglobalprovisioningsettingsstate.html)

## System requirements

* PingFederate 11.3 or later.

  |   |                                                                                                                                                                                           |
  | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | To allow PingFederate to make outbound connections to the Atlassian Cloud API, you might need to add the following domains to the allow list for your firewall:https\://api.atlassian.com |

* An Atlassian Cloud administrator account.

* An [Atlassian Access](https://www.atlassian.com/software/access) subscription.

---

---
title: Atlassian configuration
description: Complete the configuration of the Authenticator Plugin:
component: atlassian
page_id: atlassian:atlassian_integration_kit:pf_atlassian_ik_atlassian_configuration
canonical_url: https://docs.pingidentity.com/integrations/atlassian/atlassian_integration_kit/pf_atlassian_ik_atlassian_configuration.html
revdate: July 2, 2024
---

# Atlassian configuration

Complete the configuration of the Authenticator Plugin:

|             |                                                |
| ----------- | ---------------------------------------------- |
| **Field**   | **Description**                                |
| Username    | The User Name of the SP Reference ID Adapter   |
| Pass Phrase | The Pass Phrase of the SP Reference ID Adapter |

|   |                                                                                                                                                                                                                                                              |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | If you are using a self-signed certificate you'll need to import it into the JVM keystore. See the [Importing your self-signed certificate into Atlassian](pf_atlassian_ik_importing_your_self_signed_certificate_into_atlassian.html) for more information. |

---

---
title: Atlassian Integration Kit
description: The Atlassian Integration Kit allows PingFederate to coordinate single sign-on (SSO) for on-premises deployments of Jira and Confluence.
component: atlassian
page_id: atlassian:atlassian_integration_kit:pf_atlassian_ik
canonical_url: https://docs.pingidentity.com/integrations/atlassian/atlassian_integration_kit/pf_atlassian_ik.html
revdate: July 3, 2024
section_ids:
  components: Components
  intended-audience: Intended audience
  system-requirements: System requirements
---

# Atlassian Integration Kit

The Atlassian Integration Kit allows PingFederate to coordinate single sign-on (SSO) for on-premises deployments of Jira and Confluence.

|   |                                                                                                                    |
| - | ------------------------------------------------------------------------------------------------------------------ |
|   | To integrate with Atlassian Cloud, see [Atlassian integrations](../pf_is_overview_of_atlassian_integrations.html). |

This integration requires the use of the Reference ID adapter, which is part of the Agentless Integration Kit. The Reference ID adapter is used to pass user identity information from PingFederate to the specific Atlassian product.

## Components

* Authenticator

  * This component uses the Atlassian Seraph API to enable SSO for Jira and Confluence.

* Atlassian plugin

  * This plugin allows you to configure the authenticator with the appropriate PingFederate settings.

## Intended audience

This document is intended for PingFederate administrators.

Before you start, you should be familiar with the following parts of the PingFederate documentation:

* [Identity provider SSO configuration](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_ident_provid_sso_config.html)

* [Managing IdP adapters](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_managing_idp_adapters.html)

## System requirements

* PingFederate 8.0 or later

* Agentless Integration Kit 1.5 or later

For Atlassian Jira integrations:

* Atlassian Jira 8.13

* Java 8 or later

For Atlassian Confluence integrations:

* Atlassian Confluence 7.4

* Java 8

---

---
title: Atlassian integrations
description: To integrate PingFederate with Atlassian Cloud for single sign-on (SSO), you don't need to download anything. For setup instructions, see Configuring SAML SSO with Atlassian Cloud and PingFederate.
component: atlassian
page_id: atlassian::pf_is_overview_of_atlassian_integrations
canonical_url: https://docs.pingidentity.com/integrations/atlassian/pf_is_overview_of_atlassian_integrations.html
revdate: August 12, 2024
section_ids:
  atlassian-cloud-sso-configuration-guide: Atlassian Cloud SSO configuration guide
  atlassian-cloud-connector: Atlassian Cloud Connector
  atlassian-integration-kit: Atlassian Integration Kit
---

# Atlassian integrations

## Atlassian Cloud SSO configuration guide

To integrate PingFederate with Atlassian Cloud for single sign-on (SSO), you don't need to download anything. For setup instructions, see [Configuring SAML SSO with Atlassian Cloud and PingFederate](https://docs.pingidentity.com/configuration_guides/atlassian_cloud/config_saml_atlassiancloud_pf.html).

## Atlassian Cloud Connector

The Atlassian Connector allows PingFederate to integrate with Atlassian Cloud for user and group provisioning as well as SSO.

## Atlassian Integration Kit

The Atlassian Integration Kit allows PingFederate to coordinate SSO for on-premises deployments of Jira and Confluence.

---

---
title: Basic authentication
description: Configuring PingFederate for basic authentication
component: atlassian
page_id: atlassian:atlassian_integration_kit:pf_atlassian_ik_basic_authentication
canonical_url: https://docs.pingidentity.com/integrations/atlassian/atlassian_integration_kit/pf_atlassian_ik_basic_authentication.html
revdate: July 2, 2024
---

# Basic authentication

* [Configuring PingFederate for basic authentication](pf_atlassian_ik_configuring_pf_for_basic_authn.html)

* [Atlassian configuration](pf_atlassian_ik_atlassian_configuration.html)

---

---
title: Changelog
description: The following is the change history for the Atlassian Cloud Provisioner.
component: atlassian
page_id: atlassian:atlassian_cloud_provisioner:pf_atlassian_cloud_connector_changelog
canonical_url: https://docs.pingidentity.com/integrations/atlassian/atlassian_cloud_provisioner/pf_atlassian_cloud_connector_changelog.html
revdate: July 3, 2024
section_ids:
  atlassian-cloud-provisioner-2-0-february-2025: Atlassian Cloud Provisioner 2.0 - February 2025
  atlassian-cloud-provisioner-1-0-may-2020: Atlassian Cloud Provisioner 1.0 – May 2020
---

# Changelog

The following is the change history for the Atlassian Cloud Provisioner.

## Atlassian Cloud Provisioner 2.0 - February 2025

* The Atlassian Cloud Provisioner now performs group updates with the `PATCH` operation instead of the `PUT` operation. This affects the group management capabilities described in [User and group management](pf_atlassian_cloud_connector_user_and_group_management.html).

## Atlassian Cloud Provisioner 1.0 – May 2020

* Initial Release

* Included support for user and group provisioning.

* Included support for Atlassian Cloud attributes.

* Included support for API key authentication.

* Included support for provisioning disabled users.

* Included configuration options for create, update, and disable/delete capabilities.

* Included configuration options for deprovisioning actions.

---

---
title: Changelog
description: Fixed a cross-site scripting (XSS) vulnerability by improving parameter sanitation.
component: atlassian
page_id: atlassian:atlassian_integration_kit:pf_atlassian_ik_changelog
canonical_url: https://docs.pingidentity.com/integrations/atlassian/atlassian_integration_kit/pf_atlassian_ik_changelog.html
revdate: July 2, 2024
section_ids:
  atlassian-integration-kit-2-2-april-2021: Atlassian Integration Kit 2.2 – April 2021
  atlassian-integration-kit-2-1-june-2019: Atlassian Integration Kit 2.1 – June 2019
  atlassian-integration-kit-2-0-1-june-2018: Atlassian Integration Kit 2.0.1 – June 2018
  atlassian-integration-kit-2-0-march-2018: Atlassian Integration Kit 2.0 – March 2018
  atlassian-integration-kit-1-1-1-july-2016: Atlassian Integration Kit 1.1.1 – July 2016
  atlassian-integration-kit-1-1-april-2016: Atlassian Integration Kit 1.1 – April 2016
  atlassian-integration-kit-1-0-march-2015: Atlassian Integration Kit 1.0 – March 2015
---

# Changelog

## Atlassian Integration Kit 2.2 – April 2021

* Fixed a cross-site scripting (XSS) vulnerability by improving parameter sanitation.

* Added support for the Atlassian Application Server REST API.

## Atlassian Integration Kit 2.1 – June 2019

* Added support for Atlassian Confluence 6.15.

* Added support for Atlassian Jira 8.x.

* Fixed a redirect loop that occurred when a user existed in the identity provider but not in Confluence.

* Improved error-handling for redirect situations.

## Atlassian Integration Kit 2.0.1 – June 2018

* Fixed a defect in AutoAddGroups functionality.

## Atlassian Integration Kit 2.0 – March 2018

* Compatibility updates for the latest Atlassian platforms.

## Atlassian Integration Kit 1.1.1 – July 2016

* Fixed an issue so Basic and Mutual SSL options are selectable in the plugin configuration.

## Atlassian Integration Kit 1.1 – April 2016

* Added support for Default Group Memberships (autoAddGroups)

* Added support for Jira 7

* Bug fixes

## Atlassian Integration Kit 1.0 – March 2015

* Atlassian Integration Kit 1.0 – March 2015

---

---
title: Configure the plugin
description: The URL to configure the Authenticator is http[s]://atlassian_hostname:atlassian_port/plugins/servlet/ping/config
component: atlassian
page_id: atlassian:atlassian_integration_kit:pf_atlassian_ik_configure_the_plugin
canonical_url: https://docs.pingidentity.com/integrations/atlassian/atlassian_integration_kit/pf_atlassian_ik_configure_the_plugin.html
revdate: July 3, 2024
---

# Configure the plugin

The URL to configure the Authenticator is `http[s]://atlassian_hostname:atlassian_port/plugins/servlet/ping/config`

The configuration page is also accessible at **Manage apps > PingFederate SSO Configuration > /**:

![iln1618251873607](_images/iln1618251873607.png)

**Configuration options**

| Field                   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Configuration Directory | Configuration settings are stored here. If using Mutual SSL, put certificates in this directory. For more information, see [Defining the Authenticator configuration directory](pf_atlassian_ik_defining_the_authenticator_configuration_directory.html).                                                                                                                                                                                                                                                    |
| Pickup URL              | `https://pf_host:pf_port/ext/ref/pickup`When configuring a pickup URL:- Always use HTTPS over HTTP

- Enable the Require SSL/TLS option within the PingFederate SP Reference ID adapter configuration

- If using Mutual SSL Authentication, `pf_port` in the Pickup URL must match the port specified in the PingFederate `run.properties` for the `pf.secondary.https.port` (Step 1 of [Configuring PingFederate for mutual SSL authentication](pf_atlassian_ik_configuring_pf_for_mutual_ssl_authn.html)) |
| SP Adapter Instance ID  | The Instance ID of your PingFederate SP Reference ID adapter.                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Authentication          | Determines the type of authentication to be performed between the Authenticator and the Reference ID adapter.**Mutual SSL**: You should use this option as it provides the highest level of security. For more information, see [Mutual SSL authentication](pf_atlassian_ik_mutual_ssl_authentication.html)**Basic**: Uses a username and passphrase to authenticate with PingFederate . For more information, see [Basic authentication](pf_atlassian_ik_basic_authentication.html)                         |

---

---
title: Configuring Atlassian
description: Copy the p12 file created in step 2.i from the previous section into the Configuration Directory of your Atlassian Server.
component: atlassian
page_id: atlassian:atlassian_integration_kit:pf_atlassian_ik_configuring_atlassian
canonical_url: https://docs.pingidentity.com/integrations/atlassian/atlassian_integration_kit/pf_atlassian_ik_configuring_atlassian.html
revdate: July 2, 2024
section_ids:
  steps: Steps
---

# Configuring Atlassian

## Steps

1. Copy the p12 file created in [step 2.i](pf_atlassian_ik_configuring_pf_for_mutual_ssl_authn.html#reuse_bookmark) from the previous section into the Configuration Directory of your Atlassian Server.

2. Export PingFederate's SSL Server Certificate:

   1. From the Administrator page choose **SSL Server Certificates**.

      ![nru1563995135636](_images/nru1563995135636.png)

   2. Click **Export** next to your Server Certificate.

      ![ggy1563995138930](_images/ggy1563995138930.png)

   3. Choose **Certificate Only** and click **Next**.

   4. Click **Export** to save the certificate.

      ![dwl1563995139515](_images/dwl1563995139515.png)

3. Copy the Server Certificate you exported in the previous step into the Configuration Directory of your Atlassian Server.

4. Complete the configuration of the Authenticator Plugin:

   | Field                    | Description                                                                                      |
   | ------------------------ | ------------------------------------------------------------------------------------------------ |
   | Client Keystore File     | The full name of the PKCS 12 file from Step 1 (do not include the full path, just the file name) |
   | Client Keystore Password | If there was a password assigned to the client certificate enter that here                       |
   | PingFederate Certificate | The full name of the certificate from Step 3 (do not include the full path, just the file name)  |

   |   |                                                                                                                               |
   | - | ----------------------------------------------------------------------------------------------------------------------------- |
   |   | When the configuration options are saved, the plugin will check to make sure the client and server certificates can be found. |

   |   |                                                                                                                                                                                                                                                                       |
   | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | If you are using a self-signed certificate, you'll need to import it into the JVM keystore. See the [Importing your self-signed certificate into Atlassian](pf_atlassian_ik_importing_your_self_signed_certificate_into_atlassian.html) section for more information. |

---

---
title: Configuring Jira
description: When accessing a direct link to a subpage within Jira with no user session, the login link does not work correctly. This is the workaround.
component: atlassian
page_id: atlassian:atlassian_integration_kit:pf_atlassian_ik_configuring_jira
canonical_url: https://docs.pingidentity.com/integrations/atlassian/atlassian_integration_kit/pf_atlassian_ik_configuring_jira.html
revdate: July 2, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Configuring Jira

## About this task

When accessing a direct link to a subpage within Jira with no user session, the login link does not work correctly. This is the workaround.

## Steps

1. Copy the following files from the distribution package to the Atlassian jsp directory: `<Atlassian Installation Directory>/Jira/atlassian-jira/`

   * `dist/jira/login.jsp`

   * `dist/jira/default.jsp`

2. Edit the two jsp files copied in the previous step and update the values for the four variables at the top of the file. For information on what these should be, refer to step 3 of [Configuring Seraph](pf_atlassian_ik_configuring_seraph.html).

3. Make a backup copy of `<Installation Directory>/Jira/atlassian-jira/WEB-INF/web.xml`.

4. Open this file in a text editor: `<Installation Directory>/Jira/atlassian-jira/WEB-INF/web.xml`

5. Disable the default and login pages by adding comment blocks around the \<servlet> and \<servlet-mapping> nodes.

   ```
   <!--
       <servlet>
           <servlet-name>jsp.default_jsp</servlet-name>
           <servlet-class>jsp.default_jsp</servlet-class>
       </servlet>
   -->

   <!--
       <servlet>
           <servlet-name>jsp.secure.default_jsp</servlet-name>
           <servlet-class>jsp.secure.default_jsp</servlet-class>
       </servlet>
   -->

   <!--
       <servlet>
           <servlet-name>jsp.secure.project.default_jsp</servlet-name>
           <servlet-class>jsp.secure.project.default_jsp</servlet-class>
       </servlet>
   -->

   <!--
       <servlet>
           <servlet-name>jsp.secure.admin.default_jsp</servlet-name>
           <servlet-class>jsp.secure.admin.default_jsp</servlet-class>
       </servlet>
   -->

   <!--
       <servlet-mapping>
           <servlet-name>jsp.default_jsp</servlet-name>
           <url-pattern>/default.jsp</url-pattern>
       </servlet-mapping>
   -->

   <!--
       <servlet-mapping>
           <servlet-name>jsp.secure.default_jsp</servlet-name>
           <url-pattern>/secure/default.jsp</url-pattern>
       </servlet-mapping>
   -->

   <!--
       <servlet-mapping>
           <servlet-name>jsp.secure.project.default_jsp</servlet-name>
           <url-pattern>/secure/project/default.jsp</url-pattern>
       </servlet-mapping>
   -->

   <!--
       <servlet-mapping>
           <servlet-name>jsp.secure.admin.default_jsp</servlet-name>
           <url-pattern>/secure/admin/default.jsp</url-pattern>
       </servlet-mapping>
   -->

   <!--
           <servlet>
               <servlet-name>jsp.login_jsp</servlet-name>
               <servlet-class>jsp.login_jsp</servlet-class>
           </servlet>
   -->

   <!--
           <servlet-mapping>
               <servlet-name>jsp.login_jsp</servlet-name>
               <url-pattern>/login.jsp</url-pattern>
           </servlet-mapping>
   -->
   ```

---

---
title: Configuring PingFederate for basic authentication
description: Create an instance of the Reference ID SP Adapter.
component: atlassian
page_id: atlassian:atlassian_integration_kit:pf_atlassian_ik_configuring_pf_for_basic_authn
canonical_url: https://docs.pingidentity.com/integrations/atlassian/atlassian_integration_kit/pf_atlassian_ik_configuring_pf_for_basic_authn.html
revdate: July 3, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Configuring PingFederate for basic authentication

Create an instance of the Reference ID SP Adapter.

## About this task

For a complete guide, see [Configuring a Reference ID SP Adapter instance](../../agentless/custom_application_setup/pf_agentless_ik_configuring_a_reference_id_sp_adapter_instance.html) in the Agentless Integration Kit documentation.

## Steps

1. In the **User Name** and **Pass Phrase** fields, enter your credentials.

2. Clear the **Allowed Subject DN** and **Allowed Issuer DN** fields.

3. From the **Transport Mode** list, select **Query Parameter**.

---

---
title: Configuring PingFederate for mutual SSL authentication
description: Configure a secondary SSL port. See the property pf.secondary.https.port in the table under Configuring PingFederate properties.
component: atlassian
page_id: atlassian:atlassian_integration_kit:pf_atlassian_ik_configuring_pf_for_mutual_ssl_authn
canonical_url: https://docs.pingidentity.com/integrations/atlassian/atlassian_integration_kit/pf_atlassian_ik_configuring_pf_for_mutual_ssl_authn.html
revdate: July 3, 2024
section_ids:
  steps: Steps
---

# Configuring PingFederate for mutual SSL authentication

## Steps

1. Configure a secondary SSL port. See the property `pf.secondary.https.port` in the table under [Configuring PingFederate properties](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_config_pf_propert.html).

2. Import the SSL Certificate of your Atlassian server into PingFederate. See [Manage trusted certificate authorities](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_certmanagementtasklet_trustedcas_certmanagementstate.html) in the PingFederate documentation. If you do not have an SSL certificate for the Atlassian server you can use PingFederate's Client Key/Certificate Utility to create one:

   1. From PingFederate's Admin Page go to: `Server Configuration > Certificate Management > SSL Client Keys & Certificates`:

      ![nru1563995135636](_images/nru1563995135636.png)

   2. Click `Create New`.

   3. For Common Name, enter the domain of your Atlassian server.

   4. Input a value for Organization.

   5. Optionally fill out the remaining fields.

      ![jte1563995136151](_images/jte1563995136151.png)

   6. Click `Next`.

   7. Click `Done`.

   8. From the list of certificates click `Export` on your new certificate:

      ![lfj1563995136832](_images/lfj1563995136832.png)

   9. Choose Certificate and private key.

      This creates a PKCS 12 certificate file (p12 extension), which will be used later in this guide.

   10. Click Previous and `Export` once again but this time choose Certificate.

       This will export the certificate file (crt extension).

   11. Import this certificate into PingFederate as a Trusted CA (`Server Configuration > Certificate Management > Trusted CAs`).

       See [Manage trusted certificate authorities](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_certmanagementtasklet_trustedcas_certmanagementstate.html) in the PingFederate documentation for more information.

3. Create an instance of Reference ID SP Adapter.

   For a complete guide, see [Configuring a Reference ID SP Adapter instance](../../agentless/custom_application_setup/pf_agentless_ik_configuring_a_reference_id_sp_adapter_instance.html) in the Agentless Integration Kit documentation.

   1. Clear the **User Name** and **Pass Phrase** fields.

   2. Input a value for **Allowed Subject DN**. For example, for the certificate shown in section 2.h. above, the DN would be: `CN=jira-server.com, O=ACME Inc., C=US`.

   3. From the **Transport Mode** list, select **Query Parameter**.

---

---
title: Configuring Seraph
description: The final step to linking the two systems is to configure the Seraph file within the Atlassian product.
component: atlassian
page_id: atlassian:atlassian_integration_kit:pf_atlassian_ik_configuring_seraph
canonical_url: https://docs.pingidentity.com/integrations/atlassian/atlassian_integration_kit/pf_atlassian_ik_configuring_seraph.html
revdate: July 2, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
  choose-from: Choose from:
  choose-from-2: Choose from:
---

# Configuring Seraph

## About this task

The final step to linking the two systems is to configure the Seraph file within the Atlassian product.

## Steps

1. Backup the existing seraph-config.xml. It's crucial to perform this step, because if there is an issue with your configuration you may need to restore this file to get back into your Atlassian server. This file can be located at:

   ### Choose from:

   * For Confluence:

     `<Atlassian Installation Directory>/Confluence/confluence/WEB-INF/classes`

   * For Jira:

     `<Atlassian Installation Directory>/Jira/atlassian-jira/WEB-INF/classes`

2. Open `seraph-config.xml` in your favorite editor.

3. Change the param-value of `login.url` and `link.login.url` to:

   `https://<pf_host>:<pf_port>/sp/startSSO.ping?PartnerIdpId=`

   `<idp_connection_entity_id>&SpSessionAuthnAdapterId=`

   `<sp_refid_adapter_instance_id>&TARGET=${originalurl}`

   `pf_host`: The PingFederate host

   `pf_port`: The PingFederate port. This should be the same value that was specified for the secondary SSL port in the [Mutual SSL authentication](pf_atlassian_ik_mutual_ssl_authentication.html)

   `idp_connection_entity_id`: The Partner Entity ID for the IdP connection (found under General Info section of the IdP Connection).

   `sp_refid_adapter_instance_id`: The Instance ID for the SP Reference ID adapter.

   |   |                                                                                                                                               |
   | - | --------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | This value determines where the user is redirected to in step 2 of [Overview of the SSO flow](pf_atlassian_ik_overview_of_the_sso_flow.html). |

   |   |                                                                                       |
   | - | ------------------------------------------------------------------------------------- |
   |   | The values for `login.url` and `link.login.url` must be URL-encoded and HTML-escaped. |

4. Change the authenticator class:

   ### Choose from:

   * For Confluence, remove this line:

     ```
     <authenticator class="com.atlassian.confluence.user.ConfluenceAuthenticator"/>
     ```

     Add this line:

     ```
     <authenticator class="com.pingidentity.adapters.atlassian.confluence.PFConfluenceAuthenticator"/>
     ```

   * For Jira, remove this line:

     ```
     <authenticator class="com.atlassian.jira.security.login.JiraSeraphAuthenticator"/>
     ```

     Add this line:

     ```
     <authenticator class="com.pingidentity.adapters.atlassian.jira.PFJiraAuthenticator"/>
     ```

5. Save the `seraph-config.xml`.

6. For Jira, follow these additional steps:

   1. Open `<Atlassian Installation Directory>/Jira/atlassian-jira/WEB-INF/classes/jira-application.properties`

   2. Disable the login gadget.

      `jira.disable.login.gadget=true`

   3. Save the file.

---

---
title: Configuring single sign-on
description: To allow PingFederate to act as an identity provider for Atlassian Cloud, enable single sign-on (SSO) in PingFederate and Atlassian Cloud, and create a connection.
component: atlassian
page_id: atlassian:atlassian_cloud_provisioner:pf_atlassian_cloud_connector_configuring_single_sign_on
canonical_url: https://docs.pingidentity.com/integrations/atlassian/atlassian_cloud_provisioner/pf_atlassian_cloud_connector_configuring_single_sign_on.html
revdate: July 3, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Configuring single sign-on

To allow PingFederate to act as an identity provider for Atlassian Cloud, enable single sign-on (SSO) in PingFederate and Atlassian Cloud, and create a connection.

## About this task

|   |                                                                                                                                                              |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | SSO integration is an optional part of this integration. If you only want to use the Atlassian Cloud Provisioner for provisioning, skip the following steps. |

## Steps

1. Complete the steps in [Enabling single sign-on in PingFederate](pf_atlassian_cloud_connector_enabling_single_sign_on_in_pf.html).

2. Complete the steps in [Enabling single sign-on in Atlassian](pf_atlassian_cloud_connector_enabling_single_sign_on_in_atlassian.html).

3. Complete the steps in [Creating a single sign-on connection](pf_atlassian_cloud_connector_creating_a_single_sign_on_connection.html).

---

---
title: Creating a provisioning connection
description: To allow PingFederate to manage users in Atlassian Cloud, create a service provider (SP) connection.
component: atlassian
page_id: atlassian:atlassian_cloud_provisioner:pf_atlassian_cloud_connector_creating_a_provisioning_connection
canonical_url: https://docs.pingidentity.com/integrations/atlassian/atlassian_cloud_provisioner/pf_atlassian_cloud_connector_creating_a_provisioning_connection.html
revdate: July 3, 2024
section_ids:
  steps: Steps
---

# Creating a provisioning connection

To allow PingFederate to manage users in Atlassian Cloud, create a service provider (SP) connection.

## Steps

1. In the PingFederate administrator console, configure the datastore that PingFederate will use as the source of user data.

   You can find specific instructions in [Datastores](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_managedatasourcestasklet_managedatasourcesstate.html) in the PingFederate documentation.

   * When targeting users and groups for provisioning, exclude the user account that you will use to administer users in your connection to Slack. This prevents the PingFederate provisioning engine from interfering with the account that provisions users and groups.

2. Enable provisioning:

   1. On the **System > Protocol Settings > Roles & Protocols** tab, select **Enable Identity Provider IdP Role and Support the Following**.

   2. Select **Outbound Provisioning**. Click **Save**.

3. On the **Identity Provider** tab, in the **SP Connections** area, open an existing connection or create a new one as follows:

   1. Click **Create new**.

   2. On the **Connection Template** tab, select **Use a template for this connection**.

   3. In the **Connection Template** list, select **Atlassian Provisioner**.

   4. Click **Choose File**, select the `atlassian-saml-metadata.xml` file from the Atlassian Cloud Provisioner `.zip` archive, and then click **Open**. Click **Next**.

4. On the **Connection Type** tab, select **Outbound Provisioning** and clear any unwanted types. Click **Next**.

5. On the **General Info** tab, in the **Base URL** field, enter the **Directory base URL** that you noted in [Getting an Atlassian API key](pf_atlassian_cloud_connector_getting_an_atlassian_api_key.html). The rest of the connection information is populated by the metadata XML file. Click **Next**.

6. On the **Outbound Provisioning** tab, configure the provisioning target and channel as shown in [Configuring outbound provisioning](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_spconnectionconfigtasklet_saasprovisioningstate.html) in the PingFederate documentation.

   1. Click **Configure Provisioning**.

   2. On the **Target** tab, in the **Directory base URL** field, enter the value that you noted in [Getting an Atlassian API key](pf_atlassian_cloud_connector_getting_an_atlassian_api_key.html).

   3. In the **API key** field, enter the value that you noted in [Getting an Atlassian API key](pf_atlassian_cloud_connector_getting_an_atlassian_api_key.html).

      |   |                                                                                  |
      | - | -------------------------------------------------------------------------------- |
      |   | PingFederate verifies the token when you activate the channel and SP connection. |

   4. Under **Provisioning Options**, customize the provisioning connector actions as shown in [Provisioning options reference](pf_atlassian_cloud_connector_provisioning_options_reference.html). Click **Next**.

   5. On the **Manage Channels** tab, create a channel as shown in [Manage channels](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_saasmanagementtasklet_saasmanagementstate.html) in the PingFederate documentation. Click **Done**.

      |   |                                                                                                                                                                                            |
      | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
      |   | For more information about the attributes available in your channel configuration, see [Supported attributes reference](pf_atlassian_cloud_connector_supported_attributes_reference.html). |

   6. On the **Outbound Provisioning** tab, click **Next**.

7. On the **Activation and Summary** tab, above the **Summary** section, turn on the connection. Click **Save**.

---

---
title: Creating a single sign-on connection
description: To allow PingFederate to act as an identity provider for Atlassian Cloud, create a service provider (SP) connection.
component: atlassian
page_id: atlassian:atlassian_cloud_provisioner:pf_atlassian_cloud_connector_creating_a_single_sign_on_connection
canonical_url: https://docs.pingidentity.com/integrations/atlassian/atlassian_cloud_provisioner/pf_atlassian_cloud_connector_creating_a_single_sign_on_connection.html
revdate: July 3, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
  choose-from: Choose from:
---

# Creating a single sign-on connection

To allow PingFederate to act as an identity provider for Atlassian Cloud, create a service provider (SP) connection.

## About this task

If you only want to use the Atlassian Cloud Provisioner for provisioning, skip these steps.

|   |                                                                                                     |
| - | --------------------------------------------------------------------------------------------------- |
|   | You can follow these steps to create a new SP connection, or you can modify an existing connection. |

## Steps

1. In the PingFederate administrator console, create a new SP connection:

   ### Choose from:

   * For PingFederate 10.1 or later: go to **Applications > Integration > SP Connections**. Click **Create Connection**.

   * For PingFederate 10.0 or earlier: go to **Identity Provider > SP Connections**. Click **Create Connection**.

2. Configure an SP connection with the Atlassian Cloud quick connection template:

   1. On the **Connection Template** tab, select **Use a template for this connection**.

   2. From the **Connection Template** list, select **Atlassian Provisioner**. Click **Next**.

   3. On the **Metadata File** row, upload the `atlassian-saml-metadata.xml` file. Click **Next**.

   4. On the **Connection Type** tab, click **Next**.

   5. On the **General Info** tab, click **Next**.

3. On the **Connection Type** tab, select **Browser SSO Profiles** and clear any unwanted types. Click **Next**.

4. On the **General Info** tab, complete the following fields. The rest of the connection information is populated by the metadata XML file. Click **Next**.

   1. In the **Partner's Entity ID** field, enter the **SP Entity ID** that you noted in [Enabling single sign-on in Atlassian](pf_atlassian_cloud_connector_enabling_single_sign_on_in_atlassian.html).

   2. In the **Base URL** field, enter the base URL that you noted in [Getting an Atlassian API key](pf_atlassian_cloud_connector_getting_an_atlassian_api_key.html).

5. On the **Browser SSO** tab, configure browser SSO:

   You can find a complete guide in [Configure IdP Browser SSO](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_spconnectionconfigtasklet_spbrowserssostate.html) in the PingFederate documentation.

   1. On the **Browser SSO > SAML Profiles** tab, select the **IdP-Initiated** and **SP-Initiated** checkboxes.

   2. On the **Browser SSO > Protocol Settings > Assertion Consumer Service** tab, in the **Binding** list, select **POST**. In the **Endpoint URL** field, enter the **SP Assertion Consumer Service URL** that you noted in [Enabling single sign-on in Atlassian](pf_atlassian_cloud_connector_enabling_single_sign_on_in_atlassian.html). Click **Add**.

   3. On the **Browser SSO > Protocol Settings > Assertion Creation > Attribute Contract** tab, for **SAML\_SUBJECT**, in the **Subject Name Format** list, select **urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress**.

6. On the **Credentials** tab, configure the connection credentials. Click **Next**.

   You can find a complete guide in [Configure credentials](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_spconnectionconfigtasklet_credentialsstate.html) in the PingFederate documentation.

7. On the **Outbound Provisioning** tab, configure the provisioning target and channel as shown in [Configuring outbound provisioning](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_spconnectionconfigtasklet_saasprovisioningstate.html) in the PingFederate documentation.

8. On the **Activation and Summary** tab, above the **Summary** section, click the toggle to turn on the connection. Click **Save**.

---

---
title: Defining the Authenticator configuration directory
description: Before using the plugin to configure the authenticator, you must define where the plugin will store the configuration settings. This information is stored in an environment variable.
component: atlassian
page_id: atlassian:atlassian_integration_kit:pf_atlassian_ik_defining_the_authenticator_configuration_directory
canonical_url: https://docs.pingidentity.com/integrations/atlassian/atlassian_integration_kit/pf_atlassian_ik_defining_the_authenticator_configuration_directory.html
revdate: July 3, 2024
section_ids:
  defining-the-authenticator-configuration-directory-unix: Defining the Authenticator configuration directory (Unix)
  steps: Steps
  defining-the-authenticator-configuration-directory-windows: Defining the Authenticator configuration directory (Windows)
  steps-2: Steps
  choose-from: Choose from:
---

# Defining the Authenticator configuration directory

Before using the plugin to configure the authenticator, you must define where the plugin will store the configuration settings. This information is stored in an environment variable.

## Defining the Authenticator configuration directory (Unix)

### Steps

1. Create a directory of your choosing on the Atlassian server. We suggest creating a subdirectory in your Atlassian instance: e.g. `<Atlassian Installation Directory>/pingfederate-settings`

   |   |                                                                                           |
   | - | ----------------------------------------------------------------------------------------- |
   |   | The user that is running Jira must have read/write permissions for the created directory. |

2. Within your Jira root directory, edit `./bin/setenv.sh`( `setenv.bat` on Windows)

3. At the top of this file insert the following (modify the actual path to suit your environment): `PINGFEDERATE_ATLASSIAN_DATA_PATH=<Atlassian Installation Directory>/pingfederate-settings; export PINGFEDERATE_ATLASSIAN_DATA_PATH`

4. Restart the Jira server.

## Defining the Authenticator configuration directory (Windows)

### Steps

1. Create a directory of your choosing on the Atlassian server.

   |   |                                                                                                                                  |
   | - | -------------------------------------------------------------------------------------------------------------------------------- |
   |   | You should create a subdirectory in your Atlassian instance, such as `<Atlassian Installation Directory>\pingfederate-settings`. |

2. Go to your Jira root directory and edit `.\bin\setenv.bat`.

3. At the start of the `.\bin\setenv.bat`file, insert the following:

   #### Choose from:

   * If Jira or Confluence is running as a standalone service (started using `startup.bat`):

     ```
     set PINGFEDERATE_ATLASSIAN_DATA_PATH=<Atlassian Installation Directory>\pingfederate-settings
     ```

   * If Jira or Confluence is started using Windows service, go to Jira's `bin` directory with a command prompt running as Administrator, where `Tomcat9.exe`binary is located and enter the following.

     ```
     tomcat9 //US//<service id>  --Environment=PINGFEDERATE_ATLASSIAN_DATA_PATH=<Atlassian Installation Directory>\pingfederate-settings
     ```

     |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
     | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
     |   | Depending on your version of Atlassian, you might need to change `tomcat9` to `tomcat8` in the command. To find out which version of Tomcat you have, check the documentation for your Atlassian product:- [Bundled Tomcat and Java versions](https://confluence.atlassian.com/doc/bundled-tomcat-and-java-versions-1005786018.html) for Confluence

     - [Bundled Tomcat and Java versions](https://confluence.atlassian.com/doc/bundled-tomcat-and-java-versions-1005786018.html) for Jira |

     |   |                                                                                                                                                                                                                                                                                                        |
     | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
     |   | To determine your service ID, open `services.msc` and select the Jira or Confluence service. The service ID appears in the details area. A service ID is formatted as `JIRA123456123456`.![Screen capture of the Services window showing Atlassian Confluence selected.](_images/sac1591655590669.png) |

4. Restart the Jira server.

---

---
title: Defining the Authenticator configuration directory (Unix)
description: "Create a directory of your choosing on the Atlassian server. We suggest creating a subdirectory in your Atlassian instance: e.g. <Atlassian Installation Directory>/pingfederate-settings"
component: atlassian
page_id: atlassian:atlassian_integration_kit:pf_atlassian_ik_defining_the_authenticator_configuration_directory_unix
canonical_url: https://docs.pingidentity.com/integrations/atlassian/atlassian_integration_kit/pf_atlassian_ik_defining_the_authenticator_configuration_directory_unix.html
revdate: July 3, 2024
section_ids:
  steps: Steps
---

# Defining the Authenticator configuration directory (Unix)

## Steps

1. Create a directory of your choosing on the Atlassian server. We suggest creating a subdirectory in your Atlassian instance: e.g. `<Atlassian Installation Directory>/pingfederate-settings`

   |   |                                                                                           |
   | - | ----------------------------------------------------------------------------------------- |
   |   | The user that is running Jira must have read/write permissions for the created directory. |

2. Within your Jira root directory, edit `./bin/setenv.sh`( `setenv.bat` on Windows)

3. At the top of this file insert the following (modify the actual path to suit your environment): `PINGFEDERATE_ATLASSIAN_DATA_PATH=<Atlassian Installation Directory>/pingfederate-settings; export PINGFEDERATE_ATLASSIAN_DATA_PATH`

4. Restart the Jira server.

---

---
title: Defining the Authenticator configuration directory (Windows)
description: Create a directory of your choosing on the Atlassian server.
component: atlassian
page_id: atlassian:atlassian_integration_kit:pf_atlassian_ik_defining_the_authenticator_configuration_directory_windows
canonical_url: https://docs.pingidentity.com/integrations/atlassian/atlassian_integration_kit/pf_atlassian_ik_defining_the_authenticator_configuration_directory_windows.html
revdate: July 3, 2024
section_ids:
  steps: Steps
  choose-from: Choose from:
---

# Defining the Authenticator configuration directory (Windows)

## Steps

1. Create a directory of your choosing on the Atlassian server.

   |   |                                                                                                                                  |
   | - | -------------------------------------------------------------------------------------------------------------------------------- |
   |   | You should create a subdirectory in your Atlassian instance, such as `<Atlassian Installation Directory>\pingfederate-settings`. |

2. Go to your Jira root directory and edit `.\bin\setenv.bat`.

3. At the start of the `.\bin\setenv.bat`file, insert the following:

   ### Choose from:

   * If Jira or Confluence is running as a standalone service (started using `startup.bat`):

     ```
     set PINGFEDERATE_ATLASSIAN_DATA_PATH=<Atlassian Installation Directory>\pingfederate-settings
     ```

   * If Jira or Confluence is started using Windows service, go to Jira's `bin` directory with a command prompt running as Administrator, where `Tomcat9.exe`binary is located and enter the following.

     ```
     tomcat9 //US//<service id>  --Environment=PINGFEDERATE_ATLASSIAN_DATA_PATH=<Atlassian Installation Directory>\pingfederate-settings
     ```

     |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
     | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
     |   | Depending on your version of Atlassian, you might need to change `tomcat9` to `tomcat8` in the command. To find out which version of Tomcat you have, check the documentation for your Atlassian product:- [Bundled Tomcat and Java versions](https://confluence.atlassian.com/doc/bundled-tomcat-and-java-versions-1005786018.html) for Confluence

     - [Bundled Tomcat and Java versions](https://confluence.atlassian.com/doc/bundled-tomcat-and-java-versions-1005786018.html) for Jira |

     |   |                                                                                                                                                                                                                                                                                                        |
     | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
     |   | To determine your service ID, open `services.msc` and select the Jira or Confluence service. The service ID appears in the details area. A service ID is formatted as `JIRA123456123456`.![Screen capture of the Services window showing Atlassian Confluence selected.](_images/sac1591655590669.png) |

4. Restart the Jira server.

---

---
title: Deploying the Agentless Integration Kit
description: The Atlassian Integration Kit relies on the Reference ID adapter included in the Agentless Integration Kit.
component: atlassian
page_id: atlassian:atlassian_integration_kit:pf_atlassian_ik_deploying_the_agentless_i
canonical_url: https://docs.pingidentity.com/integrations/atlassian/atlassian_integration_kit/pf_atlassian_ik_deploying_the_agentless_i.html
revdate: July 3, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Deploying the Agentless Integration Kit

## About this task

The Atlassian Integration Kit relies on the Reference ID adapter included in the Agentless Integration Kit.

## Steps

1. Download the Agentless Integration Kit `.zip` archive from the [**Add-ons** tab of the PingFederate downloads page](https://www.pingidentity.com/en/resources/downloads/pingfederate.html) or the [Ping Identity Marketplace](https://marketplace.pingone.com/item/agentless-integration-kit).

2. On the sidebar, click **Download Integration**.

3. On the sidebar, click **Get Documentation**.

4. Follow the documentation to deploy the Agentless Integration Kit.