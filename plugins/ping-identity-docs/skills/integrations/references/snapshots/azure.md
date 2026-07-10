---
title: Adding review statuses to your authentication policy
description: By modifying your PingFederate authentication policy to include the Result from Azure AD Identity Protection, you can dynamically change authentication requirements based on security risk level.
component: azure
page_id: azure:azure_ad_identity_protection_integration_kit:pf_azuread_identityprotection_ik_adding_review_statuses_to_your_authentication_policy
canonical_url: https://docs.pingidentity.com/integrations/azure/azure_ad_identity_protection_integration_kit/pf_azuread_identityprotection_ik_adding_review_statuses_to_your_authentication_policy.html
llms_txt: https://docs.pingidentity.com/integrations/azure/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 21, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Adding review statuses to your authentication policy

By modifying your PingFederate authentication policy to include the Result from Azure AD Identity Protection, you can dynamically change authentication requirements based on security risk level.

## About this task

These steps are designed to help you add to an existing authentication policy. Learn more general information about configuring authentication policies in [PingFederate authentication API](https://docs.pingidentity.com/pingfederate/latest/developers_reference_guide/pf_authentication_api.html) in the PingFederate documentation.

## Steps

1. In the PingFederate administrative console, go to the **Policies** tab.

   **Choose from:**

   * For PingFederate 10.1 or later: go to **Authentication > Policies > Policies**.

   * For PingFederate 10.0 or earlier: go to **Identity Provider > Authentication Policies > Policies**.

2. Select the **IdP Authentication Policies** check box.

3. Open an existing authentication policy, or click **Add Policy**.

   Learn more about [Defining authentication policies](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_defining_auth_policies.html) in the PingFederate documentation.

4. In the **Policy** area, select the Microsoft IdP Adapter instance that you created in [Setting up the Microsoft Login Integration Kit](pf_azuread_identityprotection_ik_setting_up_the_microsoft_cloud_identity_connector.html).

   ![A screenshot that shows the authentication policy with the Microsoft IdP Adapter being added](_images/hcd1634163847787.jpg)

5. In the **Success** branch following the Microsoft IdP Adapter instance, select your Azure AD Identity Protection IdP Adapter instance.

   ![](_images/ztk1633716788773.jpg)

6. Map the Microsoft user ID into the Azure AD Identity Protection IdP Adapter instance.

   ![A screenshot that shows the Incoming User ID dialog with the user identifier selected](_images/teb1634164728456.jpg)

   1. Under the Azure AD Identity Protection IdP Adapter instance, click **Options**.

   2. On the **Options** dialog, from the **Source** list, select your Microsoft IdP Adapter instance.

   3. From the **Attribute** list, select the **id**. Click **Done**.

7. Define policy paths based on the information provided by Azure AD Identity Protection:

   ![](_images/jlv1633717420587.jpg)

   1. Under the Azure AD Identity Protection IdP Adapter instance, click **Rules**.

   2. On the **Rules** dialog, from the Attribute Name list, select **userRiskLevel**.

   3. From the **Condition** list, select **equal to**.

   4. In the **Value** field, enter "low", "medium", or "high", or one of the utility values "none", "hidden", "unknownFutureValue", or "noRiskData". The "noRiskData" value is set by the adapter when it does not find risk data for the user.

   5. In the **Result** field, enter a name. This appears as a new policy path that branches from the Azure AD Identity Protection IdP Adapter.

   6. If you want to add more authentication paths, click **Add** and repeat steps b-e.

   7. **Optional:** Clear the **Default to success** checkbox.

   8. Click **Done**.

8. Configure each of the authentication paths.

   ![](_images/nxl1633717796856.jpg)

9. Click **Done**. In the **Policies** window, click **Save**.

---

---
title: Associating the PCV with an IdP adapter instance
description: To use your new password credential validator (PCV) instance, you must associate it with an identity provider (IdP) adapter.
component: azure
page_id: azure:azure_ad_password_credential_validator:pf_azuread_pcv_associating_the_pcv_with_an_idp_adapter_instance
canonical_url: https://docs.pingidentity.com/integrations/azure/azure_ad_password_credential_validator/pf_azuread_pcv_associating_the_pcv_with_an_idp_adapter_instance.html
llms_txt: https://docs.pingidentity.com/integrations/azure/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 19, 2025
section_ids:
  before-you-begin: Before you begin
  steps: Steps
  next-steps: Next steps
---

# Associating the PCV with an IdP adapter instance

To use your new password credential validator (PCV) instance, you must associate it with an identity provider (IdP) adapter.

## Before you begin

Configure the Azure AD PCV with either the HTTP Basic or HTML Form IdP Adapter in PingFederate.

* HTML Basic Adapter

  The HTTP Basic Adapter provides user authentication through a PCV to integrate PingFederate with local authentication mechanisms. Learn more in [HTTP Basic Adapter](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_http_basic_adapt.html).

* HTML Form Adapter

  The HTML Form Adapter supports user authentication when it occurs outside of the PingFederate server through an application or the authentication module of an identity access management (IAM) system that leverages multiple user repositories and a PCV instance. Learn more in [HTML Form Adapter](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_html_form_adapt.html).

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | You can find help with configuring the IdP adapter instance in the PingFederate documentation:* [Configuring an HTTP Basic Adapter instance](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_config_http_basic_adapt_instance.html)

* [Configuring an HTML Form Adapter instance](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_config_html_form_adapt_instance.html) |

## Steps

1. In the PingFederate admin console, go to **Authentication > IdP Adapters** and select the configured HTTP Basic or HTML Form IdP adapter.

2. Configure the adapter to use the PCV you created previously:

   1. On the **IdP Adapter** tab, go to the **Credential Validators** section and click **Add a new row to 'Credential Validators'**.

   2. In the **Password Credential Validator Instance** list, select the PCV you created in [Configuring a password credential validator instance](pf_azuread_pcv_configuring_a_password_credential_validator_instance.html).

      Example:

      ![Screen capture showing the IdP Adapter tab with the Azure AD PCV selected as the PCV instance.](_images/azure_ad_create_adapter_instance_tab.png)

3. (Optional) Extend the contract.

   |   |                                                                                                                                                                                                                        |
   | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | When extending the contract, ensure you add the attributes in your PCV configuration and SP Connection too.If using PingFederate as the SP, you must extend the attributes in your SP Adapter and IdP Connection also. |

4. Save the configuration.

## Next steps

After associating the Azure AD Password Credential Validator with an IdP adapter instance, you can test the PCV's connection to the Microsoft Graph API.

In the PingFederate admin console, go to **Applications > SP Connection**. Use the configured SP connection to initiate SSO.

---

---
title: Authentication API support
description: You can use the PingFederate authentication API to integrate the Azure AD Identity Protection IdP Adapter into your application.
component: azure
page_id: azure:azure_ad_identity_protection_integration_kit:pf_azuread_identityprotection_ik_authentication_api_support
canonical_url: https://docs.pingidentity.com/integrations/azure/azure_ad_identity_protection_integration_kit/pf_azuread_identityprotection_ik_authentication_api_support.html
llms_txt: https://docs.pingidentity.com/integrations/azure/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 21, 2024
---

# Authentication API support

You can use the PingFederate authentication API to integrate the Azure AD Identity Protection IdP Adapter into your application.

The PingFederate Authentication API provides access to the current state of the authentication flow as a user steps through the PingFederate authentication policy. Learn more about [PingFederate authentication API](https://docs.pingidentity.com/pingfederate/latest/developers_reference_guide/pf_authentication_api.html) in the PingFederate documentation.

There are no states or actions for the Azure AD Identity Protection IdP Adapter in the authentication API, so you don't need to modify your application to use it. By including it in your authentication policy, it will be triggered automatically.

---

---
title: Azure AD and Office 365 Integration Guide
description: Integrating PingFederate with Microsoft Azure Active Directory (AD) and Microsoft Office 365 requires careful preparation and planning, which varies depending on the applications and use cases you're targeting.
component: azure
page_id: azure::pf_azuread_office365_integration
canonical_url: https://docs.pingidentity.com/integrations/azure/pf_azuread_office365_integration.html
llms_txt: https://docs.pingidentity.com/integrations/azure/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 21, 2024
section_ids:
  customers-already-running-azure-ad-connect: Customers already running Azure AD Connect
---

# Azure AD and Office 365 Integration Guide

Integrating PingFederate with Microsoft Azure Active Directory (AD) and Microsoft Office 365 requires careful preparation and planning, which varies depending on the applications and use cases you're targeting.

After configuration, PingFederate provides single sign-on (SSO) into Azure AD, enabling access to Office 365 and other applications connected to this service.

## Customers already running Azure AD Connect

If you reached this page by following the configuration export from Azure AD Connect, your Azure Active Directory domain will be configured for single sign-on for you and you can skip to [Install and configure PingFederate](azure_ad_and_office_365_integration_guide/pf_azuread_office365_integration_install_and_configure_pf.html).

Otherwise, complete the following prerequisite procedures:

* [Getting ready to integrate Azure Active Directory](azure_ad_and_office_365_integration_guide/pf_azuread_office365_integration_prerequisites.html)

* [Preparing Active Directory for federation](azure_ad_and_office_365_integration_guide/pf_azuread_office365_integration_prepare_active_directory_for_federation.html)

---

---
title: Azure AD Identity Protection IdP Adapter settings reference
description: The following are setting descriptions for the Azure AD Identity Protection IdP Adapter.
component: azure
page_id: azure:azure_ad_identity_protection_integration_kit:pf_azuread_identityprotection_ik_azure_ad_identity_protection_idp_adapter_settings_reference
canonical_url: https://docs.pingidentity.com/integrations/azure/azure_ad_identity_protection_integration_kit/pf_azuread_identityprotection_ik_azure_ad_identity_protection_idp_adapter_settings_reference.html
llms_txt: https://docs.pingidentity.com/integrations/azure/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 21, 2024
---

# Azure AD Identity Protection IdP Adapter settings reference

The following are setting descriptions for the Azure AD Identity Protection IdP Adapter.

**Standard fields**

| Field             | Description                                                                                                                                                                                                   |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Tenant ID**     | The tenant ID that you noted in [Setting up the Microsoft Login Integration Kit](pf_azuread_identityprotection_ik_setting_up_the_microsoft_cloud_identity_connector.html).This field is blank by default.     |
| **Client ID**     | The client ID that you noted in [Setting up the Microsoft Login Integration Kit](pf_azuread_identityprotection_ik_setting_up_the_microsoft_cloud_identity_connector.html).This field is blank by default.     |
| **Client Secret** | The client secret that you noted in [Setting up the Microsoft Login Integration Kit](pf_azuread_identityprotection_ik_setting_up_the_microsoft_cloud_identity_connector.html).This field is blank by default. |

**Advanced fields**

| Field                            | Description                                                                                                                                                                                                                         |
| -------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Microsoft Token Base URL**     | The Microsoft authentication base URL. If Microsoft changes this URL, enter the new URL.The default value is `https://login.microsoftonline.com`.                                                                                   |
| **Microsoft Graph API Base URL** | The Microsoft Graph API base URL. If Microsoft changes this URL, enter the new URL.The default value is `https://graph.microsoft.com/v1.0`.                                                                                         |
| **Microsoft Token Endpoint**     | The Microsoft endpoint used to get an access token. If Microsoft changes this URL, enter the new URL.The default value is `/oauth2/v2.0/token`.                                                                                     |
| **Scopes**                       | The scopes to request from Microsoft. If Microsoft changes this URL, enter the new URL.Separate multiple scopes with a comma.The default value is `https://graph.microsoft.com/.default`.                                           |
| **API Request Timeout**          | The amount of time in milliseconds that PingFederate allows when establishing a connection with Azure AD Identity Protection or waiting for a response to a request. A value of 0 disables the timeout.The default value is `5000`. |
| **Proxy Settings**               | Defines proxy settings for outbound HTTP requests.The default value is **System Defaults**.                                                                                                                                         |
| **Custom Proxy Host**            | The proxy server host name to use when **Proxy Settings** is set to **Custom**.This field is blank by default.                                                                                                                      |
| **Custom Proxy Port**            | The proxy server port to use when **Proxy Settings** is set to **Custom**.This field is blank by default.                                                                                                                           |

---

---
title: Azure AD Identity Protection Integration Kit
description: The Azure AD Identity Protection Integration Kit allows PingFederate to communicate with Azure AD Identity Protection for risk-based authentication.
component: azure
page_id: azure:azure_ad_identity_protection_integration_kit:pf_azuread_identityprotection_ik
canonical_url: https://docs.pingidentity.com/integrations/azure/azure_ad_identity_protection_integration_kit/pf_azuread_identityprotection_ik.html
llms_txt: https://docs.pingidentity.com/integrations/azure/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 21, 2024
section_ids:
  features: Features
  components: Components
  intended-audience: Intended audience
  system-requirements: System requirements
---

# Azure AD Identity Protection Integration Kit

The Azure AD Identity Protection Integration Kit allows PingFederate to communicate with Azure AD Identity Protection for risk-based authentication.

By sending a Microsoft user ID to Azure AD Identity Protection when a user signs on, PingFederate can get a security Result based on the user's history. You can use this to dynamically adjust the authentication requirements. For example, you could configure your PingFederate authentication policy to require multifactor authentication (MFA) when a user with a high-risk level signs on.

## Features

* Uses the Azure AD Identity Protection "riskyUsers" resource

* Supports the PingFederate [PingFederate authentication API](https://docs.pingidentity.com/pingfederate/latest/developers_reference_guide/pf_authentication_api.html)

* Supports the [JavaScript Widget for the PingFederate Authentication API](https://github.com/pingidentity/pf-authn-js-widget)

## Components

* Azure AD Identity Protection IdP Adapter:

  * When a user signs on through PingFederate, the adapter sends the user ID to Azure AD Identity Protection.

  * The adapter receives the user's Result and makes it available in the PingFederate authentication policy.

## Intended audience

This document is intended for PingFederate administrators.

Learn more about the setup process with the following resources:

* The following sections of the PingFederate documentation:

  * [Managing IdP adapters](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_managing_idp_adapters.html)

  * [Authentication policies](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_authentication_policies.html)

* The following sections of the Azure AD Identity Protection documentation:

  * [What is Identity Protection?](https://docs.microsoft.com/en-us/azure/active-directory/identity-protection/overview-identity-protection)

  * [What is risk](https://docs.microsoft.com/en-us/azure/active-directory/identity-protection/concept-identity-protection-risks)

  * [How To: Investigate risk](https://docs.microsoft.com/en-us/azure/active-directory/identity-protection/howto-identity-protection-investigate-risk)

## System requirements

* PingFederate 9.3 or later.

* A valid Azure AD Identity Protection license. Learn more about [License requirements](https://docs.microsoft.com/en-us/azure/active-directory/identity-protection/overview-identity-protection/) in the Azure AD Identity Protection documentation.

* This integration uses the [Microsoft Login Integration Kit](../../microsoft-login/pf_microsoft_login_ik.html) to get Microsoft user IDs. Setup details are provided in [Setting up the Microsoft Login Integration Kit](pf_azuread_identityprotection_ik_setting_up_the_microsoft_cloud_identity_connector.html).

---

---
title: Azure AD integrations
description: Password credential validators (PCV) allow PingFederate administrators to define a centralized location for username and password validation, allowing validator instances to be referenced by various PingFederate configurations.
component: azure
page_id: azure::pf_is_overview_of_azure_ad_integrations
canonical_url: https://docs.pingidentity.com/integrations/azure/pf_is_overview_of_azure_ad_integrations.html
llms_txt: https://docs.pingidentity.com/integrations/azure/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: August 12, 2024
section_ids:
  azure-ad-password-credential-validator: Azure AD Password Credential Validator
  pingfederate-integration-with-azure-active-directory-and-office-365: PingFederate Integration with Azure Active Directory and Office 365
---

# Azure AD integrations

## Azure AD Password Credential Validator

Password credential validators (PCV) allow PingFederate administrators to define a centralized location for username and password validation, allowing validator instances to be referenced by various PingFederate configurations.

## PingFederate Integration with Azure Active Directory and Office 365

This guide provides detailed steps for integrating PingFederate with Microsoft Azure Active Directory and Microsoft Office 365.

---

---
title: Azure AD Password Credential Validator
description: Password credential validators (PCVs) enable PingFederate administrators to define a centralized location for username or password validation, allowing various PingFederate configurations to reference PCV instances. The Azure AD Password Credential Validator uses the Microsoft Graph API for credential validation.
component: azure
page_id: azure:azure_ad_password_credential_validator:pf_azuread_pcv
canonical_url: https://docs.pingidentity.com/integrations/azure/azure_ad_password_credential_validator/pf_azuread_pcv.html
llms_txt: https://docs.pingidentity.com/integrations/azure/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 19, 2025
section_ids:
  features: Features
  intended-audience: Intended audience
  system-requirements: System requirements
---

# Azure AD Password Credential Validator

Password credential validators (PCVs) enable PingFederate administrators to define a centralized location for username or password validation, allowing various PingFederate configurations to reference PCV instances. The Azure AD Password Credential Validator uses the Microsoft Graph API for credential validation.

## Features

* Allows sign on with full usernames, such as `john.smith@mydomain.com`.

  |   |                                   |
  | - | --------------------------------- |
  |   | Short usernames aren't supported. |

* Returns an error message for failed sign-on attempts, such as one of the following:

  * `invalid credentials`

  * `account is disabled`

  * `forced password change`

* Supports non-federated single and multi-tenant Azure AD user accounts.

* Provides support for Azure AD Custom Properties (Directory Schema Extensions).

* Responses include all user group memberships.

|   |                                                                                                                                                                          |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | Review the [Azure AD Password Credential Validator's known issues and limitations](pf_azuread_pcv_known_issues_and_limitations.html) before implementing these features. |

## Intended audience

This document is intended for PingFederate admins and application developers.

Learn more about the PCV setup process in the following PingFederate resources:

* [Password credential validators](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_passwordcredentialvalidatortasklet_passwordcredentialvalidatormgmtstate.html)

* [SP connection management](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_sp_connect_management.html)

Learn more about the IdP adapter setup process in the following PingFederate resources:

* [HTTP Basic Adapter](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_http_basic_adapt.html)

  * [Configuring an HTTP Basic Adapter instance](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_config_http_basic_adapt_instance.html)

* [HTML Form Adapter](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_html_form_adapt.html)

  * [Configuring an HTML Form Adapter instance](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_config_html_form_adapt_instance.html)

Learn more about using PingFederate as an SP provider in the following PingFederate resources:

* [Managing SP adapters](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_adaptermanagementtasklet_spadaptermanagementstate.html)

* [Managing IdP connections](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_manag_idp_connect.html)

Learn more about Azure in the following Microsoft resources:

* [Register a Microsoft Entra app and create a service principal](https://learn.microsoft.com/en-us/entra/identity-platform/howto-create-service-principal-portal)

* [Get a user](https://learn.microsoft.com/en-us/graph/api/user-get?view=graph-rest-1.0\&tabs=http)

## System requirements

* PingFederate 11.3 or later.

  |   |                                                                                                                                                                                                                             |
  | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | Make sure you've configured either an HTTP Basic or HTML Form IdP Adapter instance. Learn more in [Associating the PCV with an IdP adapter instance](pf_azuread_pcv_associating_the_pcv_with_an_idp_adapter_instance.html). |

* A Microsoft Azure account with Active Directory or Active Directory B2C configured.

  |   |                                                                                                                                    |
  | - | ---------------------------------------------------------------------------------------------------------------------------------- |
  |   | Learn more about supported user account types in [Known issues and limitations](pf_azuread_pcv_known_issues_and_limitations.html). |

* An Azure AD application with the following permissions:

  * Microsoft Graph > Delegated Permission

    * Sign in and read user profile

    * Read directory data

* To allow PingFederate to make outbound connections to the Microsoft API, you might need to allow the following endpoints in your firewall:

  * Token endpoint

    `https://login.microsoftonline.com/<tenant>/oauth2/v2.0/token`

  * User attributes endpoint

    `https://graph.microsoft.com/v1.0/me/`

  * Group membership endpoint

    `https://graph.microsoft.com/v1.0/me/memberOf`

---

---
title: Azure AD PCV instance configuration settings reference
description: The following are setting descriptions for the Azure AD PCV.
component: azure
page_id: azure:azure_ad_password_credential_validator:pf_azuread_pcv_config_settings_reference
canonical_url: https://docs.pingidentity.com/integrations/azure/azure_ad_password_credential_validator/pf_azuread_pcv_config_settings_reference.html
llms_txt: https://docs.pingidentity.com/integrations/azure/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 19, 2025
---

# Azure AD PCV instance configuration settings reference

The following are setting descriptions for the Azure AD PCV.

|   |                                                                                                                                                                                                                                                               |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Learn more about obtaining the **Tenant ID**, **Client ID**, and **Client Secret** in [Register a Microsoft Entra app and create a service principal](https://docs.microsoft.com/en-us/azure/active-directory/develop/howto-create-service-principal-portal). |

> **Collapse: Standard fields**
>
> | Field                            | Description                                                                                                                                                                                |
> | -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
> | **Tenant ID** (Required)         | Enter the tenant ID Microsoft generates when you register an application in Azure.                                                                                                         |
> | **Client ID** (Required)         | Enter the client ID Microsoft generates when you register an application in Azure.                                                                                                         |
> | **Client Secret** (Required)     | Enter the client secret Microsoft generates when you register an application in Azure.                                                                                                     |
> | **Disable User Group Retrieval** | Select this checkbox to prevent the PCV from retrieving the `memberOf` attribute for users.&#xA;&#xA;If the user's group memberships aren't required, select Disable User Group Retrieval. |

> **Collapse: Advanced fields**
>
> | Field                                    | Description                                                                                                                                                             |
> | ---------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
> | **Microsoft Login Base URL** (Required)  | The base URL Microsoft uses for any authentication calls.The default value is `https://login.microsoftonline.com/`.                                                     |
> | **Microsoft Token Endpoint** (Required)  | The endpoint Microsoft uses to retrieve an access token.The default value is `/oauth2v2.0/token`.                                                                       |
> | **User Attributes Endpoint** (Required)  | The endpoint used to retrieve user attributes.The default value is `https://graph.microsoft.com/v1.0/me`.                                                               |
> | **Group Membership Endpoint** (Required) | The endpoint used to retrieve group membership info.The default value is `https://graph.microsoft.com/v1.0/me/memberOf`.                                                |
> | **API Request Timeout**                  | The amount of time, in milliseconds, that PingFederate waits for Microsoft APIs to respond to requests.A value of `0` disables the timeout.The default value is `5000`. |
> | **Proxy Settings** (Required)            | Defines proxy settings for outbound HTTP requests. Options include:- No Proxy
>
> - System Defaults
>
> - CustomThe default value is **System Defaults**.                     |
> | **Custom Proxy Host** (Optional)         | The proxy server hostname to use when **Proxy Settings** is set to **Custom**.                                                                                          |
> | **Custom Proxy Port** (Optional)         | The proxy server port to use when **Proxy Settings** is set to **Custom**.                                                                                              |

---

---
title: Changelog
description: The following is the change history for the Azure AD Identity Protection Integration Kit.
component: azure
page_id: azure:azure_ad_identity_protection_integration_kit:pf_azuread_identityprotection_ik_changelog
canonical_url: https://docs.pingidentity.com/integrations/azure/azure_ad_identity_protection_integration_kit/pf_azuread_identityprotection_ik_changelog.html
llms_txt: https://docs.pingidentity.com/integrations/azure/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 21, 2024
section_ids:
  azure-ad-identity-protection-integration-kit-1-0-october-2021: Azure AD Identity Protection Integration Kit 1.0 - October 2021
---

# Changelog

The following is the change history for the Azure AD Identity Protection Integration Kit.

## Azure AD Identity Protection Integration Kit 1.0 - October 2021

* Initial release.

* Added support for getting Result from the Azure AD Identity Protection "riskyUsers" resource.

* Added the ability to map any Azure AD Identity Protection API response attribute to an attribute in the PingFederate authentication policy.

* Added support for the [PingFederate authentication API](https://docs.pingidentity.com/pingfederate/latest/developers_reference_guide/pf_authentication_api.html).

* Added support for the [JavaScript Widget for the PingFederate Authentication API](https://github.com/pingidentity/pf-authn-js-widget).

* Added settings for API connection and request timeouts.

* Added settings to override the PingFederate system-default proxy settings.

---

---
title: Changelog
description: The following is the change history for the Azure AD Password Credential Validator.
component: azure
page_id: azure:azure_ad_password_credential_validator:pf_azuread_pcv_changelog
canonical_url: https://docs.pingidentity.com/integrations/azure/azure_ad_password_credential_validator/pf_azuread_pcv_changelog.html
llms_txt: https://docs.pingidentity.com/integrations/azure/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: April 8, 2026
section_ids:
  version-2-2-1: Version 2.2.1
  version-2-2: Version 2.2
  version-2-1-1: Version 2.1.1
  version-2-1: Version 2.1
  version-2-0: Version 2.0
  version-1-2: Version 1.2
  version-1-1: Version 1.1
  version-1-0: Version 1.0
---

# Changelog

The following is the change history for the Azure AD Password Credential Validator.

## Version 2.2.1

Released in April 2026.

* Updated the Jackson Core library to address a potential security vulnerability.

## Version 2.2

Released in January 2026.

* Added the ability to specify custom parameters in the Resource Owner Password Credentials (ROPC) request body. Learn more in step 3 in [Configuring a password credential validator instance](pf_azuread_pcv_configuring_a_password_credential_validator_instance.html).

## Version 2.1.1

Released in September 2025.

* Updated the dependencies that the Azure AD Password Credential Validator uses.

## Version 2.1

Released in January 2023.

* Added the **User Attributes Endpoint** and **Group Membership Endpoint** fields in the PCV to allow customization of the user attributes and group membership endpoint URLs. Learn more in the [Azure AD PCV instance configuration settings reference](pf_azuread_pcv_config_settings_reference.html).

## Version 2.0

Released in November 2021.

|   |                                                                                                                                                  |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | If you're upgrading from Azure AD PCV 1.2 or earlier and used the `objectID` attribute in your extended contract, update this attribute to `ID`. |

* Added the **Microsoft Login Base URL** and **Microsoft Token Endpoint** fields in the PCV to support any changes Microsoft makes to the API endpoint. Learn more in the [Azure AD PCV instance configuration settings reference](pf_azuread_pcv_config_settings_reference.html).

* Replaced the **Read Timeout** and **Connection Timeout** fields with the **API Request Timeout** field in the PCV. Learn more in the [Azure AD PCV instance configuration settings reference](pf_azuread_pcv_config_settings_reference.html).

* Changed to a standardized `.zip` file structure to make automated deployments easier.

## Version 1.2

Released in July 2019.

* Improved support for passwords with special characters.

* Added proxy connection override settings. Learn more in the advanced field descriptions in [Azure AD PCV instance configuration settings reference](pf_azuread_pcv_config_settings_reference.html).

* Added the **Read Timeout** and **Connection Timeout** fields.

## Version 1.1

Released in July 2017.

* You can now disable user membership retrieval to reduce network traffic and API calls (in configurations where this data isn't required). Learn more in the **Disable User Group Retrieval** field description in [Azure AD PCV instance configuration settings reference](pf_azuread_pcv_config_settings_reference.html).

* Fixed an issue that prevented the PCV from properly failing over to the next PCV in the chain of an HTML form adapter.

## Version 1.0

Released in Dec 2016.

* Initial release.

---

---
title: Configuring a federated domain
description: Add a new federated domain for your account.
component: azure
page_id: azure:azure_ad_and_office_365_integration_guide:pf_azuread_office365_integration_configuring_a_federated_domain
canonical_url: https://docs.pingidentity.com/integrations/azure/azure_ad_and_office_365_integration_guide/pf_azuread_office365_integration_configuring_a_federated_domain.html
llms_txt: https://docs.pingidentity.com/integrations/azure/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 21, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
  choose-from: Choose from:
---

# Configuring a federated domain

Add a new federated domain for your account.

## About this task

After signing up for Office 365, the only domain associated with your account is the onmicrosoft.com subdomain chosen during registration, such as contoso.onmicrosoft.com. To enable single sign-on (SSO) to Azure AD and Office 365, you should have another domain added to the environment.

If you've already added and verified such a domain, skip to [Step 2.](pf_azuread_office365_integration_configuring_multiple_domains.html)

|   |                                                                                                                                                                                |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | Running the Azure AD Connect tool and following its prompts makes these required configuration changes automatically. The steps outlined here can be run manually if required. |

## Steps

1. Add a federated domain to your account: Authenticate to Office 365 using the `Connect-MsolService` PowerShell `cmdlet` and enter the same credentials used when authenticating to the Microsoft Online Services portal.

   ### Choose from:

   * Add a new domain using Azure AD or Office 365 Admin Portals. Learn more in the following sections of the Microsoft documentation:

     * [Add a domain to Microsoft 365](https://support.office.com/en-us/article/add-a-domain-to-office-365-6383f56d-3d09-4dcb-9b41-b5f5a5efd611)

     * [Add your custom domain name using the Azure Active Directory portal](https://docs.microsoft.com/en-us/azure/active-directory/add-custom-domain)

   * Add a new domain manually with PowerShell.

     |   |                                                                                                                                                                                                    |
     | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
     |   | You can load this and the other `cmdlets` described here by launching PowerShell from the **Microsoft Azure Active Directory Module for Windows PowerShell** desktop and **Start** menu shortcuts. |

     1. To add a new domain, run the `New-MsolDomain -Name <name> -Authentication Managed` command.

     2. To get DNS verification records for the new domain, run the `Get-MsolDomainVerificationDns -DomainName <name>` command.

     3. To prove that you control the domain, use the output of the `Get-MsolDomainVerificationDNS` command to create a `.txt` record on the DNS server of the domain used in the previous step.

        |   |                                                                                                         |
        | - | ------------------------------------------------------------------------------------------------------- |
        |   | This server must be accessible over the Internet so that Microsoft servers can resolve and access them. |

        The DNS record name should match the Domain Name and the DNS record value should be `MS=<ms portion of the Label>`.

        The following is an example from the `Get-MsolDomainVerificationDNS` command.

        ![Screen capture showing the PowerShell prompt with the results of the Get-MsolDomainVerificationDNS command](_images/kfk1563995166854.jpg)

        |   |                                                                                                                                                                                                                                                                              |
        | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
        |   | Creating a DNS record value can vary between different DNS host providers. Learn more about how to [Add a domain to Microsoft 365](https://support.office.com/en-us/article/add-a-domain-to-office-365-6383f56d-3d09-4dcb-9b41-b5f5a5efd611) in the Microsoft documentation. |

        **Example Values for Creating a Text Record**

        | Record Type | Alias or hostname    | Destination or Points to Address      | TTL      |
        | ----------- | -------------------- | ------------------------------------- | -------- |
        | `.txt`      | `@ or jkdoctest.com` | `MS=ms60016396`                       | `1 Hour` |
        | `MX`        | `@ or jkdoctest.com` | `Ms60016396.msv1.invalid.outlook.com` | `1 Hour` |

     4. To prove your control of the domain, run the `Confirm-MsolDomain -DomainName <name>` command.

2. Complete the steps in [Enabling federated authentication](pf_azuread_office365_integration_enabling_federated_authentication.html).

3. Complete the steps in [Configuring multiple domains](pf_azuread_office365_integration_configuring_multiple_domains.html).

4. To verify that the domain settings are up to date and in effect, run the `Get-MsolDomainFederationSettings -DomainName <name>` command.

5. To change domain settings after the domain is created and verified, run the `Set-MsolDomainFederationSettings -DomainName` command with extra arguments for the settings that you want to change.

---

---
title: Configuring a password credential validator instance
description: Configure the Azure AD Password Credential Validator (PCV) to determine how PingFederate communicates with the Microsoft Graph API.
component: azure
page_id: azure:azure_ad_password_credential_validator:pf_azuread_pcv_configuring_a_password_credential_validator_instance
canonical_url: https://docs.pingidentity.com/integrations/azure/azure_ad_password_credential_validator/pf_azuread_pcv_configuring_a_password_credential_validator_instance.html
llms_txt: https://docs.pingidentity.com/integrations/azure/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: January 7, 2026
section_ids:
  steps: Steps
  example: Example:
  next-steps: Next steps
---

# Configuring a password credential validator instance

Configure the Azure AD Password Credential Validator (PCV) to determine how PingFederate communicates with the Microsoft Graph API.

## Steps

1. Sign on to the PingFederate admin console and go to **System > Password Credential Validators > Create New Instance**.

2. On the **Type** tab:

   1. In the **Instance Name** field, enter a descriptive name for the PCV instance.

   2. In the **Instance ID** field, enter a unique identifier for the PCV instance.

   3. In the **Type** list, select **Azure AD Password Credential Validator *\<version>***.

   4. Click **Next**.

   Example:

   ![Screen capture of the Create Credential Validator Instance Type tab showing the Instance Name, Instance ID, Type and Parent Instance fields.](_images/azure_ad_pcv_type_tab.png)

3. (Optional) On the **Instance Configuration** tab, in the **Custom Parameters** section, define any additional parameters to send in the Resource Owner Password Credentials (ROPC) request made to Microsoft.

   1. Click **Add a new row to 'Custom Parameters'**.

   2. In the **Parameter Name** field, enter the name of the request parameter you want to add to the ROPC request body.

      ### Example:

      `nca`

   3. In the **Parameter Value** field, enter the value you want to set for the named parameter.

   4. In the **Action** column, click **Update**.

   5. To add more attributes, repeat steps a - d.

4. On the **Instance Configuration** tab, configure the rest of the adapter instance by referring to [Azure AD PCV instance configuration settings reference](pf_azuread_pcv_config_settings_reference.html), then click **Next**.

5. On the **Extended Contract** tab, you can extend the attribute contract with any additional Azure AD attributes, including Azure AD custom properties. After you've done so, click **Next**.

   |   |                                                                                                                                                                                                                                                                                                 |
   | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | * Make sure to review the [Known issues and limitations](pf_azuread_pcv_known_issues_and_limitations.html) first.

   * If you're upgrading from Azure AD Password Credential Validator 1.2 or earlier and used the `objectID` attribute in your extended contract, update this attribute to `ID`. |

   The core contract contains the following attributes:

   > **Collapse: Show or hide core contract attributes**
   >
   > 1. `displayName`
   >
   > 2. `givenName`
   >
   > 3. `mail`
   >
   > 4. `memberOf`
   >
   > 5. `surname`
   >
   > 6. `username`
   >
   > 7. `userPrincipalName`

6. On the **Summary** tab, review your configuration, then click **Save**.

## Next steps

[Associate the PCV instance with an IdP adapter instance](pf_azuread_pcv_associating_the_pcv_with_an_idp_adapter_instance.html).

---

---
title: Configuring a username token processor instance
description: To allow email clients, mobile phones, and other active clients that use Office 365 to authenticate, users must provide the username and password of their AD domain account.
component: azure
page_id: azure:azure_ad_and_office_365_integration_guide:pf_azuread_office365_integration_configure_a_username_token_processor_instance
canonical_url: https://docs.pingidentity.com/integrations/azure/azure_ad_and_office_365_integration_guide/pf_azuread_office365_integration_configure_a_username_token_processor_instance.html
llms_txt: https://docs.pingidentity.com/integrations/azure/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 26, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Configuring a username token processor instance

To allow email clients, mobile phones, and other active clients that use Office 365 to authenticate, users must provide the username and password of their AD domain account.

## About this task

|   |                                                                                                    |
| - | -------------------------------------------------------------------------------------------------- |
|   | This configuration isn't required for browser-only implementations, such as passive WS-Federation. |

For this credential to be verified, Office 365 relays them to PingFederate using the WS-Trust protocol. For the username and password to be validated, a username token processor is set up to bind to the domain controller. Whenever requests are sent to PingFederate, they include a UsernameToken element that PingFederate passes along for authentication.

|   |                                                                                                                                                                                                                  |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | With PingFederate 6.11 or later, you can also configure the Kerberos token processor to allow the STS to accept and validate Kerberos tokens and to enable SSO for clients that support Kerberos authentication. |

## Steps

1. In the PingFederate administrative console, go to **Authentication > Token Exchange > Token Processors**.

2. Click **Create New Instance**.

3. On the **Type** tab, in the **Instance Name** field, enter a name for the token processor.

4. In the **Instance ID** field, enter an ID.

5. In the **Type** list, select **Username Token Processor**.

   |   |                                                                                                                                                                                                                                                                                                                                                                                         |
   | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | For PingFederate 7.2 or later, select **Username Token Processor** from in the **Type** list and follow the steps in the [Configuring a Username Token Processor instance](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_config_username_token_processor_instance.html) section of the PingFederate documentation. When finished, skip to step 8. |

   ![Screen capture of the Type tab showing the required Instance Name, Instance Id and Type fields.](_images/eip1563995175301.png)

6. Click **Next**.

7. On the **Instance Configuration** tab, select the LDAP Password Credential Validation instance that was previously configured.

8. Click **Next** on both the **Instance Configuration** and **Token Attributes** tabs.

9. Click **Done** on the **Summary** tab.

10. Click **Save** on the **Manage Token Processors** tab.

    |   |                                                                                                                                                                                                                                                                                                                                                                      |
    | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    |   | If you need to support multiple Office 365 subdomain accounts using one SP connection in PingFederate 7.2 or later, repeat steps 1-6 to create additional token processors against your LDAP password credential validators. Learn more in [Creating a password credential validator](pf_azuread_office365_integration_create_a_password_credential_validator.html). |

---

---
title: Configuring an adapter instance
description: Configure the Azure AD Identity Protection IdP Adapter to determine how PingFederate communicates with Azure AD Identity Protection.
component: azure
page_id: azure:azure_ad_identity_protection_integration_kit:pf_azuread_identityprotection_ik_configuring_an_adapter_instance
canonical_url: https://docs.pingidentity.com/integrations/azure/azure_ad_identity_protection_integration_kit/pf_azuread_identityprotection_ik_configuring_an_adapter_instance.html
llms_txt: https://docs.pingidentity.com/integrations/azure/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 21, 2024
section_ids:
  steps: Steps
---

# Configuring an adapter instance

Configure the Azure AD Identity Protection IdP Adapter to determine how PingFederate communicates with Azure AD Identity Protection.

## Steps

1. In the PingFederate administrative console, create a new IdP adapter instance.

   **Choose from:**

   * For PingFederate 10.1 or later: go to **Authentication > Integration > IdP Adapters**. Click **Create New Instance**.

   * For PingFederate 10.0 or earlier: go to **Identity Provider > Adapters**. Click **Create New Instance**.

2. On the **Type** tab, set the basic adapter instance attributes:

   1. In the **Instance Name** field, enter a name for the adapter instance.

   2. In the **Instance ID** field, enter a unique identifier for the adapter instance.

   3. From the **Type** list, select **Azure AD Identity Protection IdP Adapter**. Click **Next**.

3. On the **IdP Adapter** tab, in the **Azure AD Identity Protection API Response Mappings** section, map user data from the Azure AD Identity Protection response to the attribute contract:

   These attributes become available in your PingFederate authentication policy.

   1. Click **Add a new row to 'Azure AD Identity Protection API Response Mappings'**.

   2. In the **Local Attribute** field, enter a name of your choosing for an attribute.

   3. In the **Azure Attribute Mapping** field, enter the JSON Pointer syntax for the value of the matching Azure AD Identity Protection attributes as shown in [JSON Pointer syntax reference](pf_azuread_identityprotection_ik_json_pointer_syntax_reference.html). Alternately, leave the field blank to include the entire response as the value.

   4. In the **Action** column, click **Update**.

   5. To add more attributes, repeat steps a-d.

4. On the **IdP Adapter** tab, configure the adapter instance by referring to [Azure AD Identity Protection IdP Adapter settings reference](pf_azuread_identityprotection_ik_azure_ad_identity_protection_idp_adapter_settings_reference.html). Click **Next**.

5. On the **Extended Contract** tab, add any attributes that you included in the **Azure Response Mappings** section of the **IdP Adapter** tab. Click **Next**.

6. On the **Adapter Attributes** tab, set pseudonym and masking options as shown in [Set pseudonym and masking options](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_setting_pseudonym_masking_options.html) in the PingFederate documentation. Click **Next**.

7. On the **Adapter Contract Mapping** tab, configure the contract fulfillment details for the adapter as shown in [Define the IdP adapter contract](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_authnadapterinstancetasklet_plugincontractstate.html) in the PingFederate documentation. Click **Next**.

8. On the **Summary** tab, check and save your configuration.

   **Choose from:**

   * For PingFederate 10.1 or later: click **Save**.

   * For PingFederate 10.0 or earlier: click **Done**. On the **Manage IdP Adapter Instances** tab, click **Save**.

---

---
title: Configuring an IdP adapter
description: PingFederate supports a wide selection of integration kits that plug into the PingFederate server enabling it to interface with various identity management systems. After authentication, PingFederate can look up more attributes in various data stores to collect additional information that is placed in the SAML token passed to Office 365.
component: azure
page_id: azure:azure_ad_and_office_365_integration_guide:pf_azuread_office365_integration_create_an_idp_adapter
canonical_url: https://docs.pingidentity.com/integrations/azure/azure_ad_and_office_365_integration_guide/pf_azuread_office365_integration_create_an_idp_adapter.html
llms_txt: https://docs.pingidentity.com/integrations/azure/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 21, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Configuring an IdP adapter

PingFederate supports a wide selection of integration kits that plug into the PingFederate server enabling it to interface with various identity management systems. After authentication, PingFederate can look up more attributes in various data stores to collect additional information that is placed in the SAML token passed to Office 365.

## About this task

Regardless of which integration kit is used or the source of the attributes, two things need to be provided to Office 365:

* User Principal Name (UPN)

  Format as an email address and the domain name must match the domain name registered with Office 365. For example, if the domain contoso.com is created using the `New-MsolDomain` PowerShell command, then the UPN attribute value in the SAML assertion for all users must be their username followed by @contoso.com.

  |   |                                                                                                               |
  | - | ------------------------------------------------------------------------------------------------------------- |
  |   | The UPN of the user in AD can be different from what is placed in the SAML assertion created by PingFederate. |

* ImmutableID

  The Azure AD Connect copies this ID to the cloud when it creates Azure AD accounts. The ImmutableID, which uniquely represents the user in AD, is an immutable identifier used to associate local and remote identities. The AD attribute is a binary value and must be base-64 encoded to be transmitted in a SAML token.

  |   |                                                                                                                                                                  |
  | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | The expected value can be determined by examining the **ImmutableID** attribute output by the `Get-MsolUser` PowerShell command after synchronization is set up. |

PingFederate packages an HTML Form adapter that renders a simple HTML form where users can enter their username and password. This credential can be checked against AD using the previously configured password credential validator. Follow these steps to set up this adapter in PingFederate.

|   |                                                                                                                                                                                                                                                  |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | These installation steps are provided for a configuration where `objectGUID` attribute is selected for **ImmutableID**. If you are using different attribute for this purpose (such as `msDS-ConsistencyGuid`), be sure to align it accordingly. |

## Steps

1. In the PingFederate administrative console got to **My IdP Configuration > Adapters**.

2. On the **Manage IdP Adapter Instances** tab, click **Create New Instance**.

3. On the **Type** tab, enter an **Instance Name** and **Instance ID** and select **HTML Form IdP Adapter** as the **Type**.

4. On the **IdP Adapter** tab, click the **Add a new row to 'Credential Validators'**.

5. In the **Password Credential Validator Instance** list, select the validator ID you previously configured and click **Update**.

6. Click **Next**.

7. On the **Adapter Attributes** tab, select the **username** checkbox under **Pseudonym** and click **Next**.

8. On the **Summary** tab, click **Done**.

9. Click **Save** to complete the HTML Form IdP Adapter configuration.

---

---
title: Configuring an LDAP connection
description: If you're planning to provide SSO to users whose accounts reside in a directory server, ensure you have an LDAP data store defined for it in PingFederate.
component: azure
page_id: azure:azure_ad_and_office_365_integration_guide:pf_azuread_office365_integration_configure_an_ldap_connection
canonical_url: https://docs.pingidentity.com/integrations/azure/azure_ad_and_office_365_integration_guide/pf_azuread_office365_integration_configure_an_ldap_connection.html
llms_txt: https://docs.pingidentity.com/integrations/azure/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 21, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Configuring an LDAP connection

If you're planning to provide SSO to users whose accounts reside in a directory server, ensure you have an LDAP data store defined for it in PingFederate.

## About this task

Learn more about [Datastores](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_managedatasourcestasklet_managedatasourcesstate.html) in the PingFederate documentation.

|   |                                                                                                                                                                                                                                                                                 |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Ensure the `objectGUID` attribute is set to binary. It must be a binary attribute to create a connection to Office 365. Learn more in [Creating a connection to Azure Active Directory](pf_azuread_office365_integration_creating_a_connection_to_azure_active_directory.html). |

|   |                                                                                                                                                                                                        |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | If you need to support multiple Office 365 subdomain accounts through one SP connection in PingFederate 7.2 or later, create additional LDAP data store connections to LDAP servers of the subdomains. |

## Steps

1. In the PingFederate administrative console go to **Server Configuration > System Settings > Data Stores**.

2. Click **Add New Data Store**.

3. Select LDAP in the **Data Store Type** tab and click **Next**.

4. Populate the fields in the **LDAP Configuration** tab.

   1. In the **Hostname(s)** field enter the DNS name or IP address of the data store, which might include a port number such as `181.20.42.130:389`. For failover, you can enter multiple LDAP servers, each separated by a space.

   2. In the **LDAP Type** field, select **Active Directory**.

   3. Enter the **User DN** and password of a user account with read permission in Active Directory.

5. Click **Advanced** and then click the **LDAP Binary Attributes** tab.

6. In the **Binary Attribute Name** field, enter `objectGUID` and click **Add**.

7. Click **Done** and then click **Next**.

8. Review the summary and click **Save**.

---

---
title: Configuring assertion creation
description: Configure the assertion by mapping attributes from the necessary sources.
component: azure
page_id: azure:azure_ad_and_office_365_integration_guide:pf_azuread_office365_integration_configuring_assertion_creation
canonical_url: https://docs.pingidentity.com/integrations/azure/azure_ad_and_office_365_integration_guide/pf_azuread_office365_integration_configuring_assertion_creation.html
llms_txt: https://docs.pingidentity.com/integrations/azure/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 21, 2024
section_ids:
  steps: Steps
---

# Configuring assertion creation

Configure the assertion by mapping attributes from the necessary sources.

## Steps

1. On the **Assertion Creation** tab, click **Configure Assertion Creation**.

2. On the **Identity Mapping** tab, select **User Principal Name**. Click **Next**.

3. On the **Attribute Contract** tab, add the following attributes and then click **Next**.

   | Attribute          | Attribute Name Format                                   |
   | ------------------ | ------------------------------------------------------- |
   | `ImmutableID`      | http\://schemas.microsoft.com/LiveID/Federation/2008/05 |
   | `UPN`              | http\://schemas.xmlsoap.org/claims                      |
   | `SAML_NAME_FORMAT` | http\://schemas.xmlsoap.org/claims                      |

   |   |                                                                                                                                                                                                                                                                                            |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
   |   | The `SAML_NAME_FORMAT` is a pseudo-attribute that is used to define a specific attribute name format for `SAML_SUBJECT`. The current setting is ignored and a text value specified in the attribute contract fulfillment later on is used as the attribute name format for `SAML_SUBJECT`. |

4. On the **Authentication Source Mapping** tab, map your HTML Form adapter instance.

   Learn more about how to map your HTML form adapter instance in [Mapping an HTML form adapter instance](pf_azuread_office365_integration_mapping_an_html_form_adapter_instance.html).

5. On the **Assertion Creation > Summary** tab, click **Done**.

---

---
title: Configuring attribute source and user lookup for HTML Form Adapter instances
description: Complete the following to configure attribute source and user lookups for the HTML Form Adapter instances.
component: azure
page_id: azure:azure_ad_and_office_365_integration_guide:pf_azuread_office365_integration_configuring_attribute_source_and_user_lookup_for_html_form_adapter_instances
canonical_url: https://docs.pingidentity.com/integrations/azure/azure_ad_and_office_365_integration_guide/pf_azuread_office365_integration_configuring_attribute_source_and_user_lookup_for_html_form_adapter_instances.html
llms_txt: https://docs.pingidentity.com/integrations/azure/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 21, 2024
section_ids:
  steps: Steps
  example: Example:
  example-2: Example:
---

# Configuring attribute source and user lookup for HTML Form Adapter instances

Complete the following to configure attribute source and user lookups for the HTML Form Adapter instances.

## Steps

1. On the **Attribute Sources & User Lookup** tab, click **Add Attribute Source**.

2. On the **Data Store** tab, enter an attribute source ID and description of your choosing.

3. In the **Active Data Store** list, select the datastore connection that you created in [Configuring an LDAP connection](pf_azuread_office365_integration_configure_an_ldap_connection.html).

4. On the **LDAP Directory Search** tab, in the **Base DN** field, enter the base DN that contains the users whose attributes you want to retrieve.

   ### Example:

   ```shell
   CN=Users,DC=contoso,DC=com
   ```

5. In the **Root Object Class** list, select **\<Show All Attributes>**.

6. In the **Attribute** list, select **objectGUID**. Click **Add Attribute**.

7. In the **Attribute** list, select **userPrincipalName**. Click **Add Attribute**. Click **Next**.

8. On the **LDAP Binary Attribute Encoding Types** tab, click **Next**.

9. On the **LDAP Filter** tab, enter a filter to limit the search and then click **Next**.

   ### Example:

   ```shell
   (|(sAMAccountName=${username})(userPrincipalName=${username}))
   ```

   |   |                                                                                                                                      |
   | - | ------------------------------------------------------------------------------------------------------------------------------------ |
   |   | In this context, `${username}` contains the username from the HTML Form Adapter that PingFederate presents during browser-based SSO. |

10. Click **Done**.

---

---
title: Configuring attribute source and user lookup for token processors
description: Complete the following to configure attribute source and user lookups for the HTML Form Adapter instance and token processor parts of the setup process.
component: azure
page_id: azure:azure_ad_and_office_365_integration_guide:pf_azuread_office365_integration_configuring_attribute_source_and_user_lookup_for_token_processors
canonical_url: https://docs.pingidentity.com/integrations/azure/azure_ad_and_office_365_integration_guide/pf_azuread_office365_integration_configuring_attribute_source_and_user_lookup_for_token_processors.html
llms_txt: https://docs.pingidentity.com/integrations/azure/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 21, 2024
section_ids:
  steps: Steps
---

# Configuring attribute source and user lookup for token processors

Complete the following to configure attribute source and user lookups for the HTML Form Adapter instance and token processor parts of the setup process.

## Steps

1. On the **Attribute Sources & User Lookup** tab, click **Add Attribute Source**.

2. On the **Data Store** tab, enter an attribute source ID and description of your choosing.

3. From the **Active Data Store** list, select the datastore connection that you created in [Configuring an LDAP connection](pf_azuread_office365_integration_configure_an_ldap_connection.html).

4. On the **LDAP Directory Search** tab, in the **Base DN** field, enter the base DN that contains the users whose attributes you want to retrieve. For example, `CN=Users,DC=contoso,DC=com`.

5. From the **Root Object Class** list, select **\<Show All Attributes>**.

6. From the **Attribute** list, select **objectGUID**. Click **Add Attribute**.

7. From the **Attribute** list, select **userPrincipalName**. Click **Add Attribute**. Click **Next**.

8. On the **LDAP Binary Attribute Encoding Types** tab, click **Next**.

9. On the **LDAP Filter** tab, enter a filter to limit the search, and then click **Next**.

   Example filter for a username token processor:

   ```shell
   (|(sAMAccountName=${username})(userPrincipalName=${username}))
   ```

   Example filter for a Kerberos token processor:

   ```shell
   userPrincipalName=${principal}
   ```

   |   |                                                        |
   | - | ------------------------------------------------------ |
   |   | In this context, the username is always sent as a UPN. |

10. Click **Done**.