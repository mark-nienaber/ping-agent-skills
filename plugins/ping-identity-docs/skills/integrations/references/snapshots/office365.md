---
title: Add application to Azure AD
description: Add an application to Azure Active Directory to create and expose Microsoft Graph API endpoints for provisioning.
component: office365
page_id: office365:office_365_provisioner:pf_office365_connector_add_application_to_azure_ad
canonical_url: https://docs.pingidentity.com/integrations/office365/office_365_provisioner/pf_office365_connector_add_application_to_azure_ad.html
llms_txt: https://docs.pingidentity.com/integrations/office365/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 20, 2024
section_ids:
  steps: Steps
---

# Add application to Azure AD

Add an application to Azure Active Directory to create and expose Microsoft Graph API endpoints for provisioning.

## Steps

1. Complete the steps in [Register an application with the Microsoft identity platform](https://docs.microsoft.com/en-us/azure/active-directory/develop/active-directory-integrating-applications) in the [Microsoft identity platform documentation](https://docs.microsoft.com/en-us/azure/active-directory/develop/active-directory-developers-guide).

2. Note your Azure application ID and secret.

3. To allow the provisioner to manage all users, including deleting users or modifying administrators, assign the "User administrator" role to your Azure AD application.

   1. Complete the steps in ["Authorization\_RequestDenied" error message when you try to change a password if you use Graph API](https://support.microsoft.com/en-us/help/3004133/authorization-requestdenied-error-message-when-you-try-to-change-a-pas) in the Microsoft documentation.

4. Add the following application permissions to your application by completing the steps in .microsoft.com/en-us/azure/active-directory/develop/quickstart-configure-app-access-web-apis//\[Add permissions to access web APIs]:

   * `Application.ReadWrite.All`

   * `Group.ReadWrite.All`

   * `Organization.Read.All`

   * `User.ReadWrite.All`

---

---
title: Add federated domain
description: On the Windows machine with the account connection software, run the Windows Azure Active Directory Module for Windows Powershell application.
component: office365
page_id: office365:office_365_provisioner:pf_office365_connector_add_federated_domain
canonical_url: https://docs.pingidentity.com/integrations/office365/office_365_provisioner/pf_office365_connector_add_federated_domain.html
llms_txt: https://docs.pingidentity.com/integrations/office365/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 3, 2024
section_ids:
  steps: Steps
---

# Add federated domain

## Steps

1. On the Windows machine with the account connection software, run the **Windows Azure Active Directory Module for Windows Powershell** application.

   |   |                                                                                                                                                                                                                                             |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | Any instructions beginning with "PS>" indicate that the command to the right of the mentioned text is to be executed at the Powershell command line in the **Windows Azure Active Directory Module for Windows Powershell** command prompt. |

2. Connect to Azure Active Directory:

   ```
   PS> Connect-MsolService
   ```

3. Enter the username and password for the Azure account with administrative privileges.

   |   |                                                                                                                                                                                                                                                                                                                      |
   | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | Text surrounded by "<" and ">" is intended to be replaced with a substitution indicated by the text between the symbols. For example, if the name of your federated domain is `myfederateddomain.com`, then `<federated_domain_name>` should be replaced by `myfederateddomain.com` before execution of the command. |

4. Add the federated domain:

   ```
   PS> New-MsolDomain -name "<federated_domain_name>" -Authentication Federated
   ```

5. Get the domain label prefix value to aid in domain verification:

   ```
   PS> Get-MsolDomainVerificationDns -DomainName "<federated_domain_name>"
   ```

   Note the prefix of the value in the Label field and save for later use. (for example, the prefix will be in the format `ms##`)

   ![amf1563995521709](_images/amf1563995521709.jpg)

   |   |                                                                                                                                                                                                                                         |
   | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | To preserve some of the setup completed in the previous steps, leave the **Windows Azure Active Directory Module for Windows Powershell**command prompt window open until configuration of the Office 365 Connector has been completed. |

---

---
title: Add the signing certificate to Azure
description: The active signing certificate in PingFederate must be saved in Azure to secure the SSO communications between PingFederate and Office 365. SSO transactions cannot take place without the correct certificate added to Azure. Use the following procedure to add the signing certificate previously exported in Obtain PingFederate signing certificate to Azure.
component: office365
page_id: office365:office_365_provisioner:pf_office365_connector_add_the_signing_certificate_to_azure
canonical_url: https://docs.pingidentity.com/integrations/office365/office_365_provisioner/pf_office365_connector_add_the_signing_certificate_to_azure.html
llms_txt: https://docs.pingidentity.com/integrations/office365/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 20, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Add the signing certificate to Azure

## About this task

The active signing certificate in PingFederate must be saved in Azure to secure the SSO communications between PingFederate and Office 365. SSO transactions cannot take place without the correct certificate added to Azure. Use the following procedure to add the signing certificate previously exported in [Obtain PingFederate signing certificate](pf_office365_connector_obtain_pf_signing_certificate.html) to Azure.

## Steps

1. Open the exported certificate using a text editor.

2. Copy the certificate text to the clipboard without header, footer, whitespace or carriage returns.

3. Execute the Powershell commands below in the command prompt window used in [Configure federation settings](pf_office365_connector_configure_federation_settings.html).

   ```
   PS> $cert = "<SAVED_CERTIFICATE_TEXT>"
   PS> Set-MsolDomainFederationSettings -DomainName "$domainName" -SigningCertificate "$cert"
   ```

---

---
title: Changelog
description: The following is the change history for the Office 365 Provisioner.
component: office365
page_id: office365:office_365_provisioner:pf_office365_connector_changelog
canonical_url: https://docs.pingidentity.com/integrations/office365/office_365_provisioner/pf_office365_connector_changelog.html
llms_txt: https://docs.pingidentity.com/integrations/office365/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 20, 2024
section_ids:
  office-365-provisioner-2-3-december-2021: Office 365 Provisioner 2.3 – December 2021
  office-365-provisioner-2-2-june-2018: Office 365 Provisioner 2.2 – June 2018
  office-365-provisioner-2-1-march-2017: Office 365 Provisioner 2.1 – March 2017
  office-365-provisioner-2-0-2-january-2017: Office 365 Provisioner 2.0.2 – January 2017
  office-365-provisioner-2-0-1-july-2016: Office 365 Provisioner 2.0.1 – July 2016
  office-365-provisioner-2-0-january-2016: Office 365 Provisioner 2.0 – January 2016
  office-365-provisioner-1-1-2-december-2015: Office 365 Provisioner 1.1.2 – December 2015
  office-365-provisioner-1-1-1-june-2015: Office 365 Provisioner 1.1.1 – June 2015
  office-365-provisioner-1-1-february-2015: Office 365 Provisioner 1.1 – February 2015
  office-365-provisioner-1-0-may-2014: Office 365 Provisioner 1.0 – May 2014
---

# Changelog

The following is the change history for the Office 365 Provisioner.

## Office 365 Provisioner 2.3 – December 2021

* Migrated from the deprecated Azure Graph API to the Microsoft Graph API

|   |                                                                                                                                                  |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | Update your Azure AD application permissions as shown in [Add application to Azure AD](pf_office365_connector_add_application_to_azure_ad.html). |

## Office 365 Provisioner 2.2 – June 2018

* Added support for hard deleting users

* Added deprovisioning configuration options for CRUD capabilities

## Office 365 Provisioner 2.1 – March 2017

* Added configuration options for CRUD capabilities

* Added support for proxy connections

## Office 365 Provisioner 2.0.2 – January 2017

* Fixed deserialization issue due to a SaaS API change

## Office 365 Provisioner 2.0.1 – July 2016

* Fixed Group membership issue

## Office 365 Provisioner 2.0 – January 2016

* Added support for provisioning additional user attributes

* Added support for deleting groups

* Added additional license configuration support

* Azure Active Directory Graph API updated from version v1.5 to v1.6

* Improved exception handling and reporting

* Minor bug fixes

* Updates to user group mappings resulting in the removal of the memberOf attribute

## Office 365 Provisioner 1.1.2 – December 2015

* Fixed exception handling issue

## Office 365 Provisioner 1.1.1 – June 2015

* Fixed compatibility issues

## Office 365 Provisioner 1.1 – February 2015

* Support added for provisioning users with licenses

* Capability to assign managers to provisioned users

* Capability to update userPrincipalName

* Support for rename group

* Attribute changes require administrators to refresh the target and attribute mapping screens

* Support for non-base64 immutableId

* Resource and memberOf attributes removed

## Office 365 Provisioner 1.0 – May 2014

* Initial Release

* Support for SSO and SLO

* Support for User Provisioning

* Support for Group Provisioning

---

---
title: Choose an SSO configuration path
description: After installing the connector, use the table below as a reference to determine how to configure your Office 365 SSO deployment with PingFederate.
component: office365
page_id: office365:office_365_provisioner:pf_office365_connector_choose_an_sso_configuration_path
canonical_url: https://docs.pingidentity.com/integrations/office365/office_365_provisioner/pf_office365_connector_choose_an_sso_configuration_path.html
llms_txt: https://docs.pingidentity.com/integrations/office365/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 20, 2024
---

# Choose an SSO configuration path

After installing the connector, use the table below as a reference to determine how to configure your Office 365 SSO deployment with PingFederate.

|   |                                                                                                                                                                                 |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | If you are upgrading from a previous version of the Office 365 Connector, see [Upgrading an existing deployment](pf_office365_connector_upgrading_an_existing_deployment.html). |

| If you want:              | Then:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| SSO only to Office 365    | To implement this solution, follow instructions in [Configure an SSO connection](pf_office365_connector_configure_an_sso_connection.html).Note that some instructions include WS-Federation settings to ease transition to WS-Federation at a later time if desired.                                                                                                                                                                                                                                                                                                                                                                                                                  |
| SSO and SLO to Office 365 | To implement this solution, follow instructions in [Preparing Active Directory for federation](../../azure/azure_ad_and_office_365_integration_guide/pf_azuread_office365_integration_prepare_active_directory_for_federation.html) and [Install and configure PingFederate](../../azure/azure_ad_and_office_365_integration_guide/pf_azuread_office365_integration_install_and_configure_pf.html) in the Azure AD and Office 365 Integration Guide. Skip the steps marked with "SAML SSO" in this document.&#xA;&#xA;Although WS-Trust SLO is supported, SAML SLO is currently not supported due to a compatibility issue in the SAML implementation between PingFederate and Azure. |
| Active federation         | For active federation, refer to the guidelines and instructions in [Creating a connection to Azure Active Directory](../../azure/azure_ad_and_office_365_integration_guide/pf_azuread_office365_integration_creating_a_connection_to_azure_active_directory.html) in the Azure AD and Office 365 Integration Guide.                                                                                                                                                                                                                                                                                                                                                                   |

---

---
title: Configure an SSO connection
description: Create a new SP connection or select an existing SP connection from the SP Configuration menu.
component: office365
page_id: office365:office_365_provisioner:pf_office365_connector_configure_an_sso_connection
canonical_url: https://docs.pingidentity.com/integrations/office365/office_365_provisioner/pf_office365_connector_configure_an_sso_connection.html
llms_txt: https://docs.pingidentity.com/integrations/office365/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 3, 2024
section_ids:
  steps: Steps
---

# Configure an SSO connection

## Steps

1. Create a new SP connection or select an existing SP connection from the SP Configuration menu.

2. On the Connection Template screen, select Use a template for this connection and choose Office 365 from the Connection Template drop-down list.

   You will be asked to provide the `federationmetadata.xml` file you obtained earlier in [Download Office 365 SAML 2.0 metadata file](pf_office365_connector_download_office_365_saml_20_metadata_file.html).

   ![Screen capture of sp connection.](_images/gif1563995507676.png)

   |   |                                                                                                 |
   | - | ----------------------------------------------------------------------------------------------- |
   |   | If this selection is not available, verify the connector installation and restart PingFederate. |

3. On the Connection Type screen, ensure that the Browser SSO Profiles checkbox is selected and click Next.

   |   |                                                                                                                                                          |
   | - | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | If outbound provisioning will also be used, select Outbound Provisioning profile as well. The screenshot below shows an example where both are selected. |

   ![Screen capture of sp connection connection type.](_images/ucs1563995508906.png)

4. On the Connection Options screen, ensure Browser SSO is selected and click Next.

   ![Screen capture of connection options](_images/cyo1563995509629.png)

5. On the General Info screen, ensure that the Partner's Entity ID (Connection ID) and the Connection Name are accurate. Change details if required and click Next.

   |   |                                                                                                   |
   | - | ------------------------------------------------------------------------------------------------- |
   |   | By default, some fields are pre-populated as a result of using the Office 365 Connector template. |

   ![Screen capture of general info](_images/knt1563995510393.png)

6. On the Browser SSO screen, click Configure Browser SSO.

7. On the Assertion Creation screen, click Configure Assertion Creation.

8. On the IdP Adapter Mapping screen, click Map New Adapter Instance. If an HTML form adapter form already exists, select it from the drop down list and click Next. Otherwise, perform the following steps to create a new HTML form adapter:

   1. If an LDAP instance has not been configured in PingFederate, follow the instructions in [Configuring an LDAP connection](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_datasourcetasklet_ldapconfigstate.html).

   2. If a credential validator has not already been created, follow the instructions in [Configure the LDAP Username Password Credential Validator](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_configure_ldap_username_pcv.html).

   3. Complete the creation of the HTML form adapter using the instructions in [Configuring an HTML Form Adapter instance](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_config_html_form_adapt_instance.html).

   4. Once the above are completed, return to the IdP Adapter Mapping screen and click Next.

9. On the Mapping Method screen, select Retrieve additional attributes from a data store—​includes options to use alternate data stores and/or a failsafe mapping. Click Next.

   ![Screen capture of adapter contract](_images/ten1563995511411.png)

10. Click Add Attribute Source.

11. Fill in the Attribute Source Description field with an identifier of your choosing. Select the desired source datastore in the Active Data Store drop down list, then click Next.

12. On the LDAP Directory Search screen, enter the following values:

    * Base DN: where the users are found in the source datastore

    * Search Scope: select the appropriate value

    * Attributes to return from search:

      * **objectGUID**

      * **userPrincipalName**

        ![Screen capture of LDAP directory search.](_images/mhl1563995512303.png)

13. Click Next.

14. If you are in the LDAP Binary Attribute Encoding Types screen, confirm `objectGUID` is set to Base64, click Next.

    If you are NOT in the LDAP Binary Attribute Encoding Types screen, then `objectGUID` is not currently retrieved in binary format and the datastore settings must be updated. To update `objectGUID` in LDAP perform the following steps:

    1. Open a new private browser session and log in to the PingFederate Admin Console

    2. Click Data Stores, then Manage Datastores

    3. Select your source datastore

    4. Click LDAP Configuration

    5. Click Advanced

    6. Select the LDAP Binary Attributes tab

    7. Enter `objectGUID` in the BINARY ATTRIBUTE NAME field and click Add

    8. Click Done, Done, and Save

    9. Return to the LDAP Binary Attribute Encoding Types screen

    10. Confirm `objectGUID` is set to Base64 and click Next

        ![Screen capture of LDAP binary attribute encoding types](_images/msm1563995513062.png)

15. On the LDAP Filter screen, enter `userPrincipalName=${username}` in the Filter field.

    ![Screen capture ldap filer](_images/zof1563995513914.png)

16. Click Next.

17. On the Attribute Contract Fulfillment screen, set the following values:

    | Attribute Contract | Source | Value                                                |
    | ------------------ | ------ | ---------------------------------------------------- |
    | IDPEmail           | LDAP   | userPrincipalName                                    |
    | SAML\_NAME\_FORMAT | Text   | urn:oasis:names:tc:SAML:2.0:nameid-format:persistent |
    | SAML\_SUBJECT      | LDAP   | objectGUID                                           |

18. Click Next.

19. On the Attribute Source Summary screen, click Done.

20. On the Attribute Sources & User Lookup screen, click Next.

21. On the Failsafe Attribute Source screen, select Abort the SSO transaction and click Next.

    ![Screen capture of failsafe attribute source](_images/rmb1563995514904.png)

22. On the IdP Adapter Mapping summary screen, click Done.

23. On the Authentication Source Mapping screen, click Done.

24. On the Assertion Creation screen, click Done.

25. On the Protocol Settings screen, click Configure Protocol Settings.

26. On the Assertion Consumer Service URL screen, delete the binding `urn:oasis:names:tc:SAML:2.0:bindings:HTTP-POST-SimpleSign` and click Done. PingFederate does not support this binding and as such, it may result in validation errors.

27. On the Protocol Settings screen, click Done.

28. On the Browser SSO screen, click Next.

29. On the Credentials screen, click Configure Credentials.

30. On the Credentials > Digital Signature Settings screen, select the signing certificate and click Next.

31. On the Signature Verification Settings screen, click Manage Signature Verification Settings.

32. On the Trust Model screen, select the appropriate value and complete the steps for configuring the trust model and signature verification according to instructions in [Managing signature verification settings](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_managing_signature_verification_settings.html).

33. On the Signature Verification Summary screen, click Done.

34. On the Credentials screen, click Next.

35. On the Activation & Summary screen, set Connection Status to Active, then click Save.

---

---
title: Configuring single sign-on
description: The following section describes the steps for configuring single sign-on (SSO) to Office 365.
component: office365
page_id: office365:office_365_provisioner:pf_office365_connector_configuring_single_sign_on
canonical_url: https://docs.pingidentity.com/integrations/office365/office_365_provisioner/pf_office365_connector_configuring_single_sign_on.html
llms_txt: https://docs.pingidentity.com/integrations/office365/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 3, 2024
---

# Configuring single sign-on

The following section describes the steps for configuring single sign-on (SSO) to Office 365.

|   |                                                        |
| - | ------------------------------------------------------ |
|   | Configuring SSO is optional for outbound provisioning. |

|   |                                                                                                                                                                                                                                                                                                                                                                                 |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | A SAML connection is limited in functionality for this integration. For more information, see [Choose an SSO configuration path](pf_office365_connector_choose_an_sso_configuration_path.html). If SSO, SLO, and/or active federation are required, see [Azure AD and Office 365 Integration Guide](../../azure/pf_azuread_office365_integration.html) for configuration steps. |