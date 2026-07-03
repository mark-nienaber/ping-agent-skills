---
title: Change signing certificates
description: The Dynamics CRM server may cache the signing certificate, which can cause trust errors when changing the PingFederate signing certificate. Reconfiguring claims-based authentication is recommended when you change the PingFederate signing certificate. After changing the signing certificate in the Dynamics CRM connection, do the following in the Dynamics CRM server:
component: dynamicscrm
page_id: dynamicscrm::pf_dynamicscrm_integration_change_signing_certificates
canonical_url: https://docs.pingidentity.com/integrations/dynamicscrm/pf_dynamicscrm_integration_change_signing_certificates.html
revdate: July 3, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Change signing certificates

## About this task

The Dynamics CRM server may cache the signing certificate, which can cause trust errors when changing the PingFederate signing certificate. Reconfiguring claims-based authentication is recommended when you change the PingFederate signing certificate. After changing the signing certificate in the Dynamics CRM connection, do the following in the Dynamics CRM server:

## Steps

1. In the Microsoft Dynamics CRM Deployment Manager, disable claims-based authentication.

2. Run `iisreset` from the command line on the Dynamics CRM Web server.

3. In the Microsoft Dynamics CRM Deployment Manager, reconfigure claims-based authentication.

4. In the Microsoft Dynamics CRM Deployment Manager, if previously enabled, reconfigure Internet-Facing Deployment.

5. Run `iisreset` from the command line on the Dynamics CRM Web server.

---

---
title: Configure credentials
description: Click Configure Credentials.
component: dynamicscrm
page_id: dynamicscrm:pingfederate_configuration:pf_dynamicscrm_integration_configure_credentials
canonical_url: https://docs.pingidentity.com/integrations/dynamicscrm/pingfederate_configuration/pf_dynamicscrm_integration_configure_credentials.html
revdate: June 18, 2024
section_ids:
  steps: Steps
---

# Configure credentials

## Steps

1. Click **Configure Credentials**.

2. Select the signing certificate you want to use.

3. Select **RSA SHA1** or **RSA SHA256** as the signing algorithm on the **Digital Signature Settings** screen.

   |   |                                                                                             |
   | - | ------------------------------------------------------------------------------------------- |
   |   | This certificate can be self-signed and can be exported for use by the Dynamics CRM server. |

4. If the Dynamics CRM server is configured for token signature validation, export the signing certificate.

   |   |                                                                                                                                                                 |
   | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | You will import the certificate into the Dynamics CRM server (see [Dynamics CRM configuration](../pf_dynamicscrm_integration_dynamics_crm_configuration.html)). |

---

---
title: Configure IdP token processor mapping
description: Click Map New Token Processor Instance and select a configured Username Token Processor as the Token Processor Instance.
component: dynamicscrm
page_id: dynamicscrm:pingfederate_configuration:pf_dynamicscrm_integration_configure_idp_token_processor_mapping
canonical_url: https://docs.pingidentity.com/integrations/dynamicscrm/pingfederate_configuration/pf_dynamicscrm_integration_configure_idp_token_processor_mapping.html
revdate: June 18, 2024
section_ids:
  steps: Steps
---

# Configure IdP token processor mapping

## Steps

1. Click **Map New Token Processor Instance** and select a configured Username Token Processor as the Token Processor Instance.

2. On the Attribute Retrieval screen, select the option to retrieve additional attributes from data stores to fulfill the attribute contract.

3. In the **Attribute Sources & User Lookup** screen, configure the LDAP data store that will return the upn attribute for the corresponding user, adding userPrincipalName as an additional attribute and including a filter value such as` sAMAccountName=${username}`.

4. On the Attribute Contract Fulfillment screen, select **Text** as the Source for SAML\_SUBJECT and enter an unused value. Select **LDAP** as the Source for upn and select **userPrincipalName** as the value.

5. Configure issuance criteria, if necessary.

---

---
title: Configure protocol settings
description: Click Configure Protocol Settings on the Protocol Settings screen
component: dynamicscrm
page_id: dynamicscrm:pingfederate_configuration:pf_dynamicscrm_integration_configure_protocol_settings
canonical_url: https://docs.pingidentity.com/integrations/dynamicscrm/pingfederate_configuration/pf_dynamicscrm_integration_configure_protocol_settings.html
revdate: July 3, 2024
section_ids:
  steps: Steps
---

# Configure protocol settings

## Steps

1. Click **Configure Protocol Settings** on the Protocol Settings screen

2. Enter the CRM Web site as the Endpoint URL.

   For example:

   ```
   https://ping.crm.com/default.aspx
   ```

---

---
title: Configure WS-Trust STS
description: "If you are not using active federation (for native client cases such as the Dynamics CRM plug-in for Outlook), then you do not need to configure WS-Trust STS settings: skip ahead to Configure credentials. If the task bar is showing WS-Trust STS, return to the Connection Type screen and clear the WS-Trust check box. Then go to the Credentials screen."
component: dynamicscrm
page_id: dynamicscrm:pingfederate_configuration:pf_dynamicscrm_integration_configure_ws_trust_sts
canonical_url: https://docs.pingidentity.com/integrations/dynamicscrm/pingfederate_configuration/pf_dynamicscrm_integration_configure_ws_trust_sts.html
revdate: July 3, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Configure WS-Trust STS

## About this task

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | If you are not using active federation (for native client cases such as the Dynamics CRM plug-in for Outlook), then you do not need to configure WS-Trust STS settings: skip ahead to [Configure credentials](pf_dynamicscrm_integration_configure_credentials.html). If the task bar is showing `WS-Trust STS`, return to the **Connection Type** screen and clear the WS-Trust check box. Then go to the **Credentials** screen. |

## Steps

1. Click **Configure WS-Trust STS**.

2. Enter the base URL of your Dynamics CRM Web site on the **Protocols Settings** screen.

   For example:

   ```
   https://ping.crm.com
   ```

3. Select the **Generate Key for SAML Holder of Key Subject Confirmation Method** check box.

4. When configuring token creation, extend the attribute contract on the **Attribute Contract** screen by adding `upn` and selecting `http://schemas.xmlsoap.org/ws/2005/05/identity/claims` as the attribute name format.

---

---
title: Create an SP connection
description: On the Connection Type screen, select the Browser SSO Profiles check box and select WS-Federation as the Protocol. If you are configuring the connection for active federation (for native client cases such as the Dynamics CRM plug-in for Outlook), select the WS-Trust STS check box. You must select SAML 1.1 as the Default Token Type.
component: dynamicscrm
page_id: dynamicscrm:pingfederate_configuration:pf_dynamicscrm_integration_create_an_sp_connection
canonical_url: https://docs.pingidentity.com/integrations/dynamicscrm/pingfederate_configuration/pf_dynamicscrm_integration_create_an_sp_connection.html
revdate: July 3, 2024
section_ids:
  steps: Steps
---

# Create an SP connection

## Steps

1. On the **Connection Type** screen, select the **Browser SSO Profiles** check box and select **WS-Federation** as the Protocol. If you are configuring the connection for active federation (for native client cases such as the Dynamics CRM plug-in for Outlook), select the **WS-Trust STS** check box. You must select **SAML 1.1** as the Default Token Type.

2. On the **General Info** screen, enter the CRM Web site in the **Partner's Realm** field.

   For example, `https://ping.crm.com/default.aspx`

3. Enter a value in the **Connection Name** field.

4. On the **Browser SSO** screen, click **Configure Browser SSO**.

5. On the **Assertion Lifetime** screen, update the lifetime of the assertion as needed. Note that Dynamics CRM uses the SAML token to determine the session lifetime; you may increase the **Minutes After** value to extend the CRM session lifetime beyond 5 minutes (the default value).

6. On the **Assertion Creation** screen, click **Configure Assertion Creation**.

7. On the **Identity Mapping** screen, select **User Principal Name**.

8. On the **Attribute Contract** screen, extend the contract by adding `upn` and selecting **http\://schemas.xmlsoap.org/ws/2005/05/identity/claims** as the attribute name format.

---

---
title: Dynamics CRM configuration
description: Use the following steps to configure Dynamics CRM to consume the federation metadata provided by the PingFederate SP connection.
component: dynamicscrm
page_id: dynamicscrm::pf_dynamicscrm_integration_dynamics_crm_configuration
canonical_url: https://docs.pingidentity.com/integrations/dynamicscrm/pf_dynamicscrm_integration_dynamics_crm_configuration.html
revdate: July 3, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Dynamics CRM configuration

## About this task

Use the following steps to configure Dynamics CRM to consume the federation metadata provided by the PingFederate SP connection.

## Steps

1. Access the Dynamics CRM server.

2. If Dynamics CRM is configured for token signature validation, run mmc.exe and attach the Certificates (Local Computer) Snap-in.

   Import the signature verification certificate used in PingFederate or the certificate's CA certificate into the appropriate certificate store. See [Enabling ADFS 2.0 Token Signing](https://technet.microsoft.com/en-us/library/gg188574\(v=crm.6\).aspx) for more information on token signature validation.

3. If WS-Trust STS was configured for the CRM connection in PingFederate, import the encryption certificate used in PingFederate (see [Select WS-Trust encryption algorithm](pingfederate_configuration/pf_dynamicscrm_integration_select_ws_trust_encryption_algorithm.html)) along with the certificate's private key into the Dynamics CRM server's personal certificate store. The Dynamics CRM server searches this store when configuring claims-based authentication.

4. On the Dynamics CRM server, run the Microsoft Dynamics CRM Deployment Manager.

5. Select Configure Claims-based Authentication and click **Next**.

6. Enter the following URL for the Federation metadata URL and click **Next**:

   ```
   https://<pf_host>:<pf_port>/pf/federation_metadata.ping?PartnerSpId=<SPConnectionID>&forceIssuedTokenPolicy
   ```

   where:

   * \<pf\_host> is the host name or IP address where PingFederate is running.

   * \<pf\_port> is the port number for PingFederate.

   * \<SPConnectionID> is the ID for the PingFederate SP Connection you configured above – for example:

     ```
     https://ping.crm.com/default.aspx
     ```

     |   |                                                                                                                                                                                                                                       |
     | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
     |   | If an error appears stating that the Federation URL is unavailable, add PingFederate's server certificate (signed by the domain controller) to the Dynamics CRM server to establish trust with PingFederate's SSL server certificate. |

7. When prompted for the encryption certificate, use the same certificate shared with PingFederate (see [Select WS-Trust encryption algorithm](pingfederate_configuration/pf_dynamicscrm_integration_select_ws_trust_encryption_algorithm.html)).

8. Save the configuration and run iisreset from the command line so the Dynamics CRM server recognizes the changes.

---

---
title: Dynamics CRM Integration Guide
description: The purpose of this document is to guide a PingFederate and Microsoft Dynamics CRM 2011 (Dynamics CRM) administrator through the configuration of both products so that federated users can log on to Dynamics CRM using claims-based authentication. The document outlines how to configure an SP connection compatible with Dynamics CRM within PingFederate and how to configure Dynamics CRM to consume the federation metadata provided by the SP connection.
component: dynamicscrm
page_id: dynamicscrm::pf_dynamicscrm_integration
canonical_url: https://docs.pingidentity.com/integrations/dynamicscrm/pf_dynamicscrm_integration.html
revdate: June 18, 2024
---

# Dynamics CRM Integration Guide

The purpose of this document is to guide a PingFederate and Microsoft Dynamics CRM 2011 (Dynamics CRM) administrator through the configuration of both products so that federated users can log on to Dynamics CRM using claims-based authentication. The document outlines how to configure an SP connection compatible with Dynamics CRM within PingFederate and how to configure Dynamics CRM to consume the federation metadata provided by the SP connection.

|   |                                                                                |
| - | ------------------------------------------------------------------------------ |
|   | Knowledge of Dynamics CRM is assumed as well as familiarity with PingFederate. |

---

---
title: Known issues
description: "If you configure Internet-Facing Deployment in the Dynamics CRM Deployment Manager, you can ignore the following warning and still successfully complete the configuration: "The Discovery Web Service could not be accessed. The domain is unavailable or does not exist.""
component: dynamicscrm
page_id: dynamicscrm::pf_dynamicscrm_integration_known_issues
canonical_url: https://docs.pingidentity.com/integrations/dynamicscrm/pf_dynamicscrm_integration_known_issues.html
revdate: June 18, 2024
---

# Known issues

* If you configure Internet-Facing Deployment in the Dynamics CRM Deployment Manager, you can ignore the following warning and still successfully complete the configuration: "The Discovery Web Service could not be accessed. The domain is unavailable or does not exist."

* Active login for Dynamics CRM Outlook clients is supported only when the claims provider for the Dynamics CRM Outlook client is the same claims provider as the Dynamics CRM server. This means all Outlook client computers need to be configured to login to the SAML claims provider (which is the default behavior). In other words, the HKEY\_LOCAL\_MACHINE\Software\Policies\Microsoft\MSCRMClient\HomeRealmUrl registry key on the Outlook client computer must not be set. See [Configure Microsoft Dynamics CRM for Outlook to use Claims-based Authentication](http://technet.microsoft.com/en-us/library/gg188615.aspx) for more information (technet.microsoft.com/en-us/library/gg188615.aspx).

---

---
title: Map an IdP adapter
description: Click Map New Adapter Instance and select the HTML Form IdP Adapter as the Adapter Instance.
component: dynamicscrm
page_id: dynamicscrm:pingfederate_configuration:pf_dynamicscrm_integration_map_an_idp_adapter
canonical_url: https://docs.pingidentity.com/integrations/dynamicscrm/pingfederate_configuration/pf_dynamicscrm_integration_map_an_idp_adapter.html
revdate: June 18, 2024
section_ids:
  steps: Steps
---

# Map an IdP adapter

## Steps

1. Click **Map New Adapter Instance** and select the HTML Form IdP Adapter as the Adapter Instance.

2. On the **Assertion Mapping** screen, select the option button to retrieve additional attributes from a data store including options to use alternate data stores and/or a failsafe mapping.

3. Click **Add Attribute Source** and configure the LDAP data source, adding `userPrincipalName` as an additional attribute and including a filter value such as `sAMAccountName=${username}`.

4. On the **Attribute Contract Fulfillment** screen, select **Text** as the Source for SAML\_SUBJECT and enter an unused value. Select **LDAP** as the Source for upn and select **userPrincipalName** as the value.

5. On the **Failsafe Attribute Source** screen, select the **Abort the SSO Transaction** option.

---

---
title: PingFederate configuration
description: Configure PingFederate to include an SP Connection (see SP connection management).
component: dynamicscrm
page_id: dynamicscrm:pingfederate_configuration:pf_dynamicscrm_integration_pf_configuration
canonical_url: https://docs.pingidentity.com/integrations/dynamicscrm/pingfederate_configuration/pf_dynamicscrm_integration_pf_configuration.html
revdate: June 18, 2024
---

# PingFederate configuration

Configure PingFederate to include an SP Connection (see [SP connection management](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_sp_connect_management.html)).

---

---
title: Prerequisites
description: The following must be installed and configured in order to complete the configuration:
component: dynamicscrm
page_id: dynamicscrm::pf_dynamicscrm_integration_prerequisites
canonical_url: https://docs.pingidentity.com/integrations/dynamicscrm/pf_dynamicscrm_integration_prerequisites.html
revdate: June 18, 2024
---

# Prerequisites

The following must be installed and configured in order to complete the configuration:

* Install (in your JDK) the Unlimited Strength Java TM Cryptographic Extension (JCE) Policy Files in order to use the AES-256 encryption algorithm used by Dynamics CRM.

* Install PingFederate 6.11 or higher.

  |   |                                                                                                                                                                                                                     |
  | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | If you need to support active clients, such as native desktop applications, for use with Dynamics CRM, ensure that PingFederate is installed with a license that enables the WS-Trust Security Token Service (STS). |

* Obtain two certificates for use by PingFederate and Dynamics CRM to establish trust between the two services. The first certificate is an encryption certificate that encrypts data between PingFederate and Dynamics CRM. The second certificate is a signing certificate used to digitally sign the SAML assertions returned from PingFederate.

* Configure a connection to the Active Directory LDAP data store (see Configuring an LDAP Connection).

* Configure the HTML Form IdP Adapter with an LDAP Username Password Credential Validator (see [Configuring an HTML Form Adapter instance](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_config_html_form_adapt_instance.html)).

* If you are configuring the connection for active federation, install and configure the Username Token Translator 1.1 (or higher) to use LDAP bind as the processing scheme with the Active Directory LDAP data store created above. Contact [Ping Identity support](https://community.pingidentity.com/) for information about this plug-in.

  |   |                                                                                                                                           |
  | - | ----------------------------------------------------------------------------------------------------------------------------------------- |
  |   | For PingFederate 7.2 or higher, Username Token Processor is part of the product and does not require a separate download or installation. |

* In order for the connector to work properly you must configure PingFederate to "Omit Line Breaks in Digital Signatures" by adding the following java startup option to your run.sh, run.bat and/or PingFederateService.conf file:

  ```
  -Dorg.apache.xml.security.ignoreLineBreaks=true
  ```

* For this release, Microsoft Dynamics CRM 2011 for active login with Microsoft Office TM Outlook versions 2007 or later were tested.

---

---
title: Save and activate the connection
description: Save and activate the connection on the Activation & Summary screen.
component: dynamicscrm
page_id: dynamicscrm:pingfederate_configuration:pf_dynamicscrm_integration_save_and_activate_the_connection
canonical_url: https://docs.pingidentity.com/integrations/dynamicscrm/pingfederate_configuration/pf_dynamicscrm_integration_save_and_activate_the_connection.html
revdate: June 18, 2024
section_ids:
  steps: Steps
---

# Save and activate the connection

## Steps

1. Save and activate the connection on the **Activation & Summary** screen.

---

---
title: Select WS-Trust encryption algorithm
description: This step is only necessary if WS-Trust is being used.
component: dynamicscrm
page_id: dynamicscrm:pingfederate_configuration:pf_dynamicscrm_integration_select_ws_trust_encryption_algorithm
canonical_url: https://docs.pingidentity.com/integrations/dynamicscrm/pingfederate_configuration/pf_dynamicscrm_integration_select_ws_trust_encryption_algorithm.html
revdate: July 3, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Select WS-Trust encryption algorithm

## About this task

|   |                                                        |
| - | ------------------------------------------------------ |
|   | This step is only necessary if WS-Trust is being used. |

## Steps

1. On the **Select XML Encryption Certificate** screen, select **AES-256** as the Block Encryption Algorithm.

2. Select the encryption certificate for Dynamics CRM claims encryption from the drop-down list.

   This is the same encryption certificate used in [Dynamics CRM configuration](../pf_dynamicscrm_integration_dynamics_crm_configuration.html).

   |   |                                                                                                   |
   | - | ------------------------------------------------------------------------------------------------- |
   |   | If AES-256 is unavailable, make sure the high-level encryption libraries were imported correctly. |

---

---
title: Share the signing certificate with the Dynamics CRM server
description: Click Manage Certificates.
component: dynamicscrm
page_id: dynamicscrm:pingfederate_configuration:pf_dynamicscrm_integration_share_the_signing_certificate_with_the_dynamics_crm_server
canonical_url: https://docs.pingidentity.com/integrations/dynamicscrm/pingfederate_configuration/pf_dynamicscrm_integration_share_the_signing_certificate_with_the_dynamics_crm_server.html
revdate: June 18, 2024
section_ids:
  steps: Steps
---

# Share the signing certificate with the Dynamics CRM server

## Steps

1. Click **Manage Certificates**.

2. Click **Export** on the **Manage Digital Signing Certificates** screen for the signing certificate you want to export.

3. On the Export & Summary screen, click **Export**. Transfer the certificate to the Dynamics CRM server and import it into the appropriate Certificate store using the Microsoft Management Console Certificates Snap-in.

   |   |                                                                                                                                                                                                         |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | See [Enabling ADFS 2.0 Token Signing](http://technet.microsoft.com/en-us/library/gg188574.aspx) for more information on token signature validation (technet.microsoft.com/en-us/library/gg188574.aspx). |

4. Click **Done** until you return to the Digital Signature Settings screen.