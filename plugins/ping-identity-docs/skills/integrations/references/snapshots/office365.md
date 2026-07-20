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
title: Configure federation settings
description: Set the federation type to SAML.
component: office365
page_id: office365:office_365_provisioner:pf_office365_connector_configure_federation_settings
canonical_url: https://docs.pingidentity.com/integrations/office365/office_365_provisioner/pf_office365_connector_configure_federation_settings.html
llms_txt: https://docs.pingidentity.com/integrations/office365/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 3, 2024
---

# Configure federation settings

Set the federation type to SAML.

```
PS> Set-MsolDomainAuthentication -DomainName "$domainName"
            -Authentication Federated -PreferredAuthenticationProtocol Samlp
```

---

---
title: Configure license management
description: The Office 365 Connector supports the ability to manage the Office 365 licenses assigned to a user.
component: office365
page_id: office365:office_365_provisioner:pf_office365_connector_configure_license_management
canonical_url: https://docs.pingidentity.com/integrations/office365/office_365_provisioner/pf_office365_connector_configure_license_management.html
llms_txt: https://docs.pingidentity.com/integrations/office365/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 20, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Configure license management

## About this task

The Office 365 Connector supports the ability to manage the Office 365 licenses assigned to a user.

## Steps

1. The usageLocation field must be set to a static value, or mapped to an attribute containing the `ISO-3166` two-character country code for the location of the user.

2. The skuId field must either be set to a single static value or an attribute containing one or more license keys to be assigned to the user.

   |   |                                                                                                                             |
   | - | --------------------------------------------------------------------------------------------------------------------------- |
   |   | Each license specified in the skuId field can be either the actual ID of that license or the specified name of the license. |

3. The disabledPlans field may either be set to a single static value or an attribute containing product keys to be disabled for the user. The disabledPlans field cannot contain a list of product keys. To provide a list of product keys, set the disabledPlans field to a multi-valued LDAP attribute.

   |   |                                                                                                                                                        |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
   |   | If no disabledPlans are specified, the user will have access to all products available through their assigned licenses specified in their skuId field. |

   |   |                                                                                                                           |
   | - | ------------------------------------------------------------------------------------------------------------------------- |
   |   | Each product specified in the disabledPlans field can be either the actual ID of that product or the name of the product. |

4. Ensure the appropriate option for the Remove Licenses from User when skuID is Empty connection field is configured on the SP Connection configured for the Office 365 Connector:

   * **False** (default) - When disabled, if you choose to not configure the skuId field in your configuration's Attribute Mapping screen, or if the user's skuId field is cleared in the datastore, the user's licenses will not be removed from their account.

   * **True** - When enabled, if you choose to not configure the skuId field in your configuration's Attribute Mapping screen, or if the user's skuId field is cleared in the datastore, the user's licenses will be removed from their account.

---

---
title: Configure manager assignment
description: The Office 365 Connector supports the ability to assign a manager to a user.
component: office365
page_id: office365:office_365_provisioner:pf_office365_connector_configure_manager_assignment
canonical_url: https://docs.pingidentity.com/integrations/office365/office_365_provisioner/pf_office365_connector_configure_manager_assignment.html
llms_txt: https://docs.pingidentity.com/integrations/office365/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 20, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
  examplean-example-of-how-assigning-a-manager-to-a-user-works: ExampleAn example of how assigning a manager to a user works
---

# Configure manager assignment

## About this task

The Office 365 Connector supports the ability to assign a manager to a user.

## Steps

1. The pingSourceDn field must be mapped to an attribute containing a unique identifier for the user.

   |   |                                                                                                                          |
   | - | ------------------------------------------------------------------------------------------------------------------------ |
   |   | By default this is mapped to the distinguishedName field. We recommend leaving this field mapped to the default mapping. |

2. The manager field must either be set to a static value, or mapped to an attribute containing the value of the assigned manager's pingSourceDn field.

   |   |                                                                                                                |
   | - | -------------------------------------------------------------------------------------------------------------- |
   |   | By default this is mapped to the manager field. We recommend leaving this field mapped to the default mapping. |

## ExampleAn example of how assigning a manager to a user works

|   |                                                                                     |
| - | ----------------------------------------------------------------------------------- |
|   | The following assumes the default mappings for the pingSourceDn and manager fields. |

1. The manager is provisioned to Azure.

2. The employee is provisioned to Azure.

3. The employee's manager, under their Organization tab in Active Directory (AD), is set to the manager in AD.

4. The Office 365 Connector will assign the manager as the employee's manager in Azure.

   |   |                                                                                                                                |
   | - | ------------------------------------------------------------------------------------------------------------------------------ |
   |   | To update or clear the employee's manager in Azure, change or clear the employee's manager under their Organization tab in AD. |

---

---
title: Configure outbound provisioning
description: Outbound provisioning details are managed within an SP connection. You can configure outbound provisioning with or without Browser SSO, WS-Trust STS, or both when you create a new SP connection. You also have the option to add outbound provisioning to an existing SP connection.
component: office365
page_id: office365:office_365_provisioner:pf_office365_connector_configure_outbound_provisioning
canonical_url: https://docs.pingidentity.com/integrations/office365/office_365_provisioner/pf_office365_connector_configure_outbound_provisioning.html
llms_txt: https://docs.pingidentity.com/integrations/office365/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 3, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Configure outbound provisioning

## About this task

Outbound provisioning details are managed within an SP connection. You can configure outbound provisioning with or without Browser SSO, WS-Trust STS, or both when you create a new SP connection. You also have the option to add outbound provisioning to an existing SP connection.

For SSO instructions, see [Configure SSO](pf_office365_connector_configure_an_sso_connection.html).

## Steps

1. Create a new SP connection or select an existing SP connection from the SP Configuration menu.

2. On the Connection Template screen, select the Use a template for this connection option and choose Office 365 Connector from the Connection Template drop-down list. You will be asked to provide the `federationmetadata.xml` file you obtained earlier in [Download Office 365 SAML 2.0 metadata file](pf_office365_connector_download_office_365_saml_20_metadata_file.html).

   ![gif1563995507676](_images/gif1563995507676.png)

   |   |                                                                                                 |
   | - | ----------------------------------------------------------------------------------------------- |
   |   | If this selection is not available, verify the connector installation and restart PingFederate. |

3. On the Connection Type screen, ensure the Outbound Provisioning checkbox is selected, and the Browser SSO Profiles checkbox is cleared (if appropriate).

4. On the General Info screen, the default values are taken from the metadata file you selected in an earlier step. We recommend using the metadata default values.

   ![knt1563995510393](_images/knt1563995510393.png)

5. Follow the connection wizard to configure the connection.

6. On the Outbound Provisioning screen, click Configure Provisioning.

7. On the Target screen, enter the values for each field as required by the Office 365 Connector.

   ![Image of the Target screen.](_images/bgt1563995515875.png)

   | Field Name                                    | Value                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
   | --------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | Application ID                                | The application ID for the application created in Azure. For more information, see [Add application to Azure AD](pf_office365_connector_add_application_to_azure_ad.html).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
   | Application Secret                            | The secret generated during application creation in Azure. For more information, see [Add application to Azure AD](pf_office365_connector_add_application_to_azure_ad.html).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
   | Global Default Password                       | The default password. Only used if the password attribute is not mapped, or value of the mapped field is empty.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
   | Do a Base64 Conversion on ImmutableID         | **True** (default) is recommended. Set to false if the ImmutableID is not base64. The conversion assumes it is mapped to a hex number.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
   | Remove Licenses from User when SkuId is Empty | **False** (default) – When disabled, if you choose to not configure the skuId field in your configuration's Attribute Mapping screen, or if the user's skuId field is cleared in the datastore, the user's licenses will not be removed from their account.**True** – When enabled, if you choose to not configure the skuId field in your configuration's Attribute Mapping screen, or if the user's skuId field is cleared in the datastore, the user's licenses will be removed from their account.                                                                                                                                                                                                                                                                                                                                                |
   | Tenant Domain                                 | The tenant domain configured in Azure, which is retrieved by going to the application properties and selecting view endpoints, and copying the ID from the URL under Windows Azure AD Graph API Endpoint.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
   | **Provisioning Options**                      |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
   | User Create                                   | **True**(default) – Users will be created in Office 365.**False** – Users will not be created in Office 365.&#xA;&#xA;The provisioner.log will display a warning within the create user workflow that the user was not created in Office 365.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
   | User Update                                   | **True** (default) – Users will be updated in Office 365.**False** – Users will not be updated in Office 365.&#xA;&#xA;The provisioner.log will display a warning within the update user workflow that the user was not updated in Office 365.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
   | User Disable / Delete                         | \[**True** (default) – Users will be disabled or deleted in Office 365.**False** – Users will not be disabled or deleted in Office 365.&#xA;&#xA;The provisioner.log will display a warning indicating that the user was not disabled or deleted in Office 365.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
   | Provision Disabled Users                      | This option is only relevant if User Create is True.**True** (default) – Office 365 users will be created in a disabled state.**False** – Office 365 users will not be created in a disabled state. This is desirable for scenarios where there are disabled users in the data store, not intended for creation in Office 365 during initial synchronization.&#xA;&#xA;The provisioner.log will display a warning within the create user workflow indicating that the user was not created in Office 365.                                                                                                                                                                                                                                                                                                                                             |
   | Remove User Action                            | Select a deprovision method (Disable or Delete). Deprovisioning is triggered when previously provisioned users no longer meet the condition set in the Source Location screen, or when a user has been suspended or deleted from the data store. This option is only applicable if User Disable / Delete is set to True.**Disable** (default) – when selected, if you delete a user from Active Directory, the user will be disabled in Office 365 (also known as a soft delete).**Delete** – when selected, if you delete a user from Active Directory, the user will be deleted in Office 365 (also known as a hard delete).&#xA;&#xA;When a user is deleted in Azure Active Directory, the deleted user is retained for 30 days from the deletion date. During that time, the user and its properties can be restored under Users > Deleted users. |

   |   |                                                                                                              |
   | - | ------------------------------------------------------------------------------------------------------------ |
   |   | For user provisioning to succeed, the users' userPrincipalName domain must match a verified domain in Azure. |

8. Click Next to continue the provisioning configuration.

   For more information, see the following sections under [Configuring outbound provisioning](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_spconnectionconfigtasklet_saasprovisioningstate.html):

   * [Manage channels](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_saasmanagementtasklet_saasmanagementstate.html)

   * [Specifying channel information](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_saaschanneltasklet_saasgeneralinfostate.html)

   * [Identifying the source datastore](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_saaschanneltasklet_saassourceselectionstate.html)

   * [Modify source settings](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_saaschanneltasklet_saassourcesettingsstate.html)

   * [Specify a source location](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_saaschanneltasklet_saassourcelocationstate.html)

   * [Map attributes](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_saaschanneltasklet_saasattrmappingmgmtstate.html)

   * [Review channel settings](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_saaschanneltasklet_saasactivationstate.html)

     |   |                                                                                                                 |
     | - | --------------------------------------------------------------------------------------------------------------- |
     |   | Credentials will be verified when the channel and SP connection is set to Active and provisioning is initiated. |

     |   |                                                                                                                                                                                                                                                      |
     | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
     |   | If you are not ready to complete the provisioning configuration, you can click Save and return to the configuration page later. To return to the configuration page, select the connection from **Identity Provider > SP Connections > Manage All**. |

---

---
title: Configuring PingFederate to omit line breaks in digital signatures
description: Configure PingFederate to omit line breaks in digital signatures by performing the following steps.
component: office365
page_id: office365:office_365_provisioner:pf_office365_connector_configuring_pf_to_omit_line_breaks_in_digital_signatures
canonical_url: https://docs.pingidentity.com/integrations/office365/office_365_provisioner/pf_office365_connector_configuring_pf_to_omit_line_breaks_in_digital_signatures.html
llms_txt: https://docs.pingidentity.com/integrations/office365/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 3, 2024
section_ids:
  steps: Steps
---

# Configuring PingFederate to omit line breaks in digital signatures

Configure PingFederate to omit line breaks in digital signatures by performing the following steps.

## Steps

1. Open `<pf_install>/pingfederate/bin/run.properties` in a text editor.

2. If not already present, add a new line to the file as follows: `org.apache.xml.security.ignoreLineBreaks=true`

3. Save the file.

4. Stop PingFederate and restart it to pick up the change.

---

---
title: Configuring provisioning
description: To configure a connection for outbound provisioning to Office 365, complete the instructions the following sections:
component: office365
page_id: office365:office_365_provisioner:pf_office365_connector_configuring_provisioning
canonical_url: https://docs.pingidentity.com/integrations/office365/office_365_provisioner/pf_office365_connector_configuring_provisioning.html
llms_txt: https://docs.pingidentity.com/integrations/office365/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 20, 2024
---

# Configuring provisioning

To configure a connection for outbound provisioning to Office 365, complete the instructions the following sections:

1. [Add application to Azure AD](pf_office365_connector_add_application_to_azure_ad.html)

2. [Configure outbound provisioning](pf_office365_connector_configure_outbound_provisioning.html)

3. [Configure license management](pf_office365_connector_configure_license_management.html)

4. [Configure manager assignment](pf_office365_connector_configure_manager_assignment.html)

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

---

---
title: Create an Azure account
description: The following steps outline how to create an Azure account for this integration. You will create the Azure account with the same credentials as those used with the Office 365 tenant to provide access to Azure Active Directory. This step is required for both provisioning and SSO.
component: office365
page_id: office365:office_365_provisioner:pf_office365_connector_create_an_azure_account
canonical_url: https://docs.pingidentity.com/integrations/office365/office_365_provisioner/pf_office365_connector_create_an_azure_account.html
llms_txt: https://docs.pingidentity.com/integrations/office365/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 20, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Create an Azure account

## About this task

The following steps outline how to create an Azure account for this integration. You will create the Azure account with the same credentials as those used with the Office 365 tenant to provide access to Azure Active Directory. This step is required for both provisioning and SSO.

## Steps

1. Navigate to the [Microsoft Azure Portal](https://login.microsoftonline.com/organizations/oauth2/v2.0/authorize?redirect_uri=https%3A%2F%2Fportal.azure.com%2Fsignin%2Findex%2F\&response_type=code%20id_token\&scope=https%3A%2F%2Fmanagement.core.windows.net%2F%2Fuser_impersonation%20openid%20email%20profile\&state=OpenIdConnect.AuthenticationProperties%3DUbvQD2JzApJzBBV52lFIB7hLEG6N2Yr6G-KrUFBfx3UT-xjhlnIStqsmQBTDzjA5FjU6XbcgxP8LBcM17ra05lwZt7XrIe5iu_I4utiEeKQ7ErzRT5cdxIwOvQ-5XeA8IDUSTi7QPv4gXG5GYVpmzYWcTsamCTPnTritI5FoE3D470JD4aZUguCnrIwCgAxb76-eaSNv30N5ikDI7n2FO24-yqt9cPgJVYKYeqfafFqzY0VPJpzDCL7GjjUQcS6lE9o9IA0jxjC7IHqSkBi6NbGZNlPY71beVRCaKMLeXaAwXCgzz1yaRrKy0afrm2GanSwnS7tj_umnK0L-wnYXOS0Fh4lKddze3SG0OCXtlyWknPRxxRwHBH4M-5atc3eYBb7fhATkfbwlSRNk7ry1dA\&response_mode=form_post\&nonce=637752782926851920.YmMyYmY2NTctZDUwZC00YTFkLTk4M2ItMDhmZTFiNjIwNTMzN2FlZmRmOGYtYTJmOC00YjJhLTk5MWMtMDgwMzc3YjQ0NTgw\&client_id=c44b4083-3bb0-49c1-b47d-974e53cbdf3c\&site_id=501430\&client-request-id=d42d7eb7-53d6-4a45-93b8-a5754b557972\&x-client-SKU=ID_NET472\&x-client-ver=6.11.0.0).

2. Create an account using the same credentials as the Office 365 account.

---

---
title: Deploying the integration files
description: To get started with the integration, deploy the Office 365 Provisioner files to your PingFederate directory.
component: office365
page_id: office365:office_365_provisioner:pf_office365_connector_deploying_the_integration_files
canonical_url: https://docs.pingidentity.com/integrations/office365/office_365_provisioner/pf_office365_connector_deploying_the_integration_files.html
llms_txt: https://docs.pingidentity.com/integrations/office365/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 3, 2024
section_ids:
  steps: Steps
---

# Deploying the integration files

To get started with the integration, deploy the Office 365 Provisioner files to your PingFederate directory.

## Steps

1. Download the Office 365 Provisioner `.zip` archive from the [**Add-ons** tab of the PingFederate downloads page](https://www.pingidentity.com/en/resources/downloads/pingfederate.html) or the [Ping Identity Marketplace](https://marketplace.pingone.com/item/office-365-single-signon-integration).

2. Stop PingFederate.

3. If you're upgrading an existing deployment, delete the `pf-office365-quickconnection-<version>.jar` file from your `<pf_install>/pingfederate/server/default/deploy` directory.

4. Extract the `.zip` archive and merge the contents of the `dist` directory with your `<pf_install>/pingfederate/server/default/deploy` directory.

5. Enable the PingFederate provisioning engine:

   1. Open your `<pf_install>/pingfederate/bin/run.properties` file.

   2. Change `pf.provisioner.mode` to `STANDALONE`. Save the file.

      |   |                                                                                                                                                                                                                                        |
      | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      |   | To configure the `FAILOVER` mode instead, see [Deploying provisioning failover](https://docs.pingidentity.com/pingfederate/latest/server_clustering_guide/pf_deploy_provis_failover.html) in the PingFederate Server Clustering Guide. |

6. Start PingFederate.

7. If you operate PingFederate in a cluster, repeat steps 2-4 and step 6 for each engine node.

---

---
title: DNS updates
description: Add a DNS redirect from a sub-domain of the federated domain to point to the PingFederate server so that <sub-domain>.<federated_domain_name> points to <PingFederate_domain_name_or_IP> where <sub-domain> is a unique identifier for the PingFederate server.
component: office365
page_id: office365:office_365_provisioner:pf_office365_connector_dns_updates
canonical_url: https://docs.pingidentity.com/integrations/office365/office_365_provisioner/pf_office365_connector_dns_updates.html
llms_txt: https://docs.pingidentity.com/integrations/office365/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 20, 2024
section_ids:
  steps: Steps
---

# DNS updates

## Steps

1. Add a DNS redirect from a sub-domain of the federated domain to point to the PingFederate server so that `<sub-domain>.<federated_domain_name>` points to `<PingFederate_domain_name_or_IP>` where `<sub-domain>` is a unique identifier for the PingFederate server.

   For example, redirect `pf.myfederateddomain.com` to `pfnode.mycompany.com` where `pfnode.mycompany.com` resolves to the PingFederate server.

2. To assist in verification of the domain, add a TXT record to the DNS settings of the federated domain. Insert the domain label prefix recorded recorded in the [Add federated domain](pf_office365_connector_add_federated_domain.html) step where indicated below.

   ```
   type: TXT, alias/host name: @, destination/points to address: MS=<domain_label_prefix>, ttl: 1hour
   ```

---

---
title: Download manifest
description: The following files are included in the Office 365 Provisioner .zip archive.
component: office365
page_id: office365:office_365_provisioner:pf_office365_connector_download_manifest
canonical_url: https://docs.pingidentity.com/integrations/office365/office_365_provisioner/pf_office365_connector_download_manifest.html
llms_txt: https://docs.pingidentity.com/integrations/office365/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 3, 2024
---

# Download manifest

The following files are included in the Office 365 Provisioner `.zip` archive.

The distribution `.zip` archive for the connector contains the following:

* `/legal`:

  * `Legal.pdf` – copyright and license information.

* `/dist` – contains libraries needed for the connector:

  * `pf-office365-quickconnection-<version>.jar`– PingFederate Office 365 Connector

---

---
title: Download Office 365 SAML 2.0 metadata file
description: This connector's quick-connection template uses a metadata .xml file from Office 365 to assist in configuring many settings in the SP Connection. When asked during the SP Connection configuration steps, import the federationmetadata.xml that you downloaded from Office 365.
component: office365
page_id: office365:office_365_provisioner:pf_office365_connector_download_office_365_saml_20_metadata_file
canonical_url: https://docs.pingidentity.com/integrations/office365/office_365_provisioner/pf_office365_connector_download_office_365_saml_20_metadata_file.html
llms_txt: https://docs.pingidentity.com/integrations/office365/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 27, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Download Office 365 SAML 2.0 metadata file

## About this task

This connector's quick-connection template uses a metadata `.xml` file from Office 365 to assist in configuring many settings in the SP Connection. When asked during the SP Connection configuration steps, import the `federationmetadata.xml` that you downloaded from Office 365.

## Steps

1. Download the SAML 2.0 metadata for Office 365 from [Microsoft](https://nexus.microsoftonline-p.com/federationmetadata/saml20/federationmetadata.adoc).

2. Save the `.xml`file to a desired location.

---

---
title: Enabling provisioning and single sign-on in PingFederate
description: To use PingFederate for provisioning and single sign-on, configure an external datastore and set a SAML entity ID.
component: office365
page_id: office365:office_365_provisioner:pf_office365_connector_enabling_provisioning_and_single_sign_on_in_pf
canonical_url: https://docs.pingidentity.com/integrations/office365/office_365_provisioner/pf_office365_connector_enabling_provisioning_and_single_sign_on_in_pf.html
llms_txt: https://docs.pingidentity.com/integrations/office365/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 3, 2024
section_ids:
  about-this-task: About this task
  enabling-provisioning-and-single-sign-on-in-pingfederate-10-1-or-later: Enabling provisioning and single sign-on in PingFederate 10.1 or later
  steps: Steps
  enabling-provisioning-and-single-sign-on-in-pingfederate-10-0-or-earlier: Enabling provisioning and single sign-on in PingFederate 10.0 or earlier
  steps-2: Steps
---

# Enabling provisioning and single sign-on in PingFederate

To use PingFederate for provisioning and single sign-on, configure an external datastore and set a SAML entity ID.

## About this task

Your external datastore acts as the source of data for provisioning. PingFederate also uses an internal datastore to store the state of synchronization between the source datastore and the target datastore.

For more information, see [Datastores](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_datastores.html) and [Configuring outbound provisioning settings](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_protocolsettingstasklet_saasglobalprovisioningsettingsstate.html) in the PingFederate documentation.

* PingFederate 10.1 or later

* PingFederate 10.0 or earlier

## Enabling provisioning and single sign-on in PingFederate 10.1 or later

### Steps

1. In the PingFederate administrative console, configure the datastore for PingFederate to use as the source of user data.

   For help, see [Datastores](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_datastores.html) in the PingFederate documentation.

2. Go to System > Server > Protocol Settings > Federation Info.

3. In the SAML 2.0 Entity ID field, enter a name for PingFederate to use when identifying itself to SAML partners.

4. On the Outbound Provisioning tab, in the Provisioner Data Store list, select the internal database that will store the synchronization state. Click Save.

   For more information, see [Configuring outbound provisioning settings](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_protocolsettingstasklet_saasglobalprovisioningsettingsstate.html) in the PingFederate documentation.

## Enabling provisioning and single sign-on in PingFederate 10.0 or earlier

### Steps

1. In the PingFederate administrative console, configure the datastore for PingFederate to use as the source of user data.

   For help, see [Datastores](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_datastores.html) in the PingFederate documentation.

2. Go to System > Protocol Settings > Roles & Protocols.

3. Select the Enable Identity Provider IdP Role and Support the Following check box.

4. Select the SAML 2.0 and Outbound Provisioning check boxes. Click Next.

5. Click the Federation Info tab.

6. In the SAML 2.0 Entity ID field, enter a name for PingFederate to use to identify itself to SAML partners.

7. On the Outbound Provisioning tab, in the Provisioner Data Store list, select the internal database that will store the synchronization state. Click Save.

   For more information, see [Configuring outbound provisioning settings](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_protocolsettingstasklet_saasglobalprovisioningsettingsstate.html) in the PingFederate documentation.

---

---
title: Enabling provisioning and single sign-on in PingFederate 10.0 or earlier
description: In the PingFederate administrative console, configure the datastore for PingFederate to use as the source of user data.
component: office365
page_id: office365:office_365_provisioner:pf_office365_connector_enabling_provisioning_and_single_sign_on_in_pf_100_or_earlier
canonical_url: https://docs.pingidentity.com/integrations/office365/office_365_provisioner/pf_office365_connector_enabling_provisioning_and_single_sign_on_in_pf_100_or_earlier.html
llms_txt: https://docs.pingidentity.com/integrations/office365/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 3, 2024
section_ids:
  steps: Steps
---

# Enabling provisioning and single sign-on in PingFederate 10.0 or earlier

## Steps

1. In the PingFederate administrative console, configure the datastore for PingFederate to use as the source of user data.

   For help, see [Datastores](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_datastores.html) in the PingFederate documentation.

2. Go to System > Protocol Settings > Roles & Protocols.

3. Select the Enable Identity Provider IdP Role and Support the Following check box.

4. Select the SAML 2.0 and Outbound Provisioning check boxes. Click Next.

5. Click the Federation Info tab.

6. In the SAML 2.0 Entity ID field, enter a name for PingFederate to use to identify itself to SAML partners.

7. On the Outbound Provisioning tab, in the Provisioner Data Store list, select the internal database that will store the synchronization state. Click Save.

   For more information, see [Configuring outbound provisioning settings](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_protocolsettingstasklet_saasglobalprovisioningsettingsstate.html) in the PingFederate documentation.