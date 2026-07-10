---
title: Authentication API support
description: You can use the PingFederate authentication API to integrate the Microsoft IdP Adapter into your application.
component: microsoft-login
page_id: microsoft-login::pf_microsoft_login_ik_authentication_api_support
canonical_url: https://docs.pingidentity.com/integrations/microsoft-login/pf_microsoft_login_ik_authentication_api_support.html
llms_txt: https://docs.pingidentity.com/integrations/microsoft-login/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 23, 2025
---

# Authentication API support

You can use the PingFederate authentication API to integrate the Microsoft IdP Adapter into your application.

The PingFederate Authentication API provides access to the current state of the authentication flow as a user steps through the PingFederate authentication policy. Learn more in [PingFederate authentication API](https://docs.pingidentity.com/pingfederate/latest/developers_reference_guide/pf_authentication_api.html) in the PingFederate documentation.

To integrate the Microsoft IdP Adapter into your authentication flow, configure your application based on the states, actions, and models available in the PingFederate Authentication API Explorer. You can find help in [Exploring the Authentication API](https://docs.pingidentity.com/pingfederate/latest/developers_reference_guide/pf_exploring_authentication_api.html) in the PingFederate documentation.

---

---
title: Changelog
description: The following is the change history for the Microsoft Login Integration Kit.
component: microsoft-login
page_id: microsoft-login:release_notes:pf_microsoft_login_ik_changelog
canonical_url: https://docs.pingidentity.com/integrations/microsoft-login/release_notes/pf_microsoft_login_ik_changelog.html
llms_txt: https://docs.pingidentity.com/integrations/microsoft-login/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 17, 2025
section_ids:
  microsoft-login-integration-kit-1-2-september-2024: Microsoft Login Integration Kit 1.2 – September 2024
  microsoft-login-integration-kit-1-1-july-2024: Microsoft Login Integration Kit 1.1 – July 2024
  microsoft-login-integration-kit-1-0-1-august-2021: Microsoft Login Integration Kit 1.0.1 – August 2021
  microsoft-login-integration-kit-1-0-june-2021: Microsoft Login Integration Kit 1.0 – June 2021
---

# Changelog

The following is the change history for the Microsoft Login Integration Kit.

## Microsoft Login Integration Kit 1.2 – September 2024

* Updated the [Core contract attributes](../setup/pf_microsoft_login_ik_core_contract_attributes.html) to include the `idToken`, `accessToken`, and `tenantId` values. The `tenantId` value is decoded from the `idToken` JSON Web Token (JWT).

## Microsoft Login Integration Kit 1.1 – July 2024

* Added the ability to send a **login\_hint** parameter to pre-fill the **Username** field on the Microsoft user sign-on page. Learn more in the **Include Login Hint** field description in [Microsoft IdP Adapter settings reference](../setup/pf_microsoft_login_ik_idp_adapter_settings_reference.html).

* Added the ability to send a prompt parameter to confirm user interaction during the authentication process. Learn more in the **Include Prompt** field description in [Microsoft IdP Adapter settings reference](../setup/pf_microsoft_login_ik_idp_adapter_settings_reference.html).

* Added the ability to send other request parameters in the authorization request to Microsoft. Learn more in step 3 in [Configuring an adapter instance](../setup/pf_microsoft_login_ik_configuring_an_adapter_instance.html).

## Microsoft Login Integration Kit 1.0.1 – August 2021

* Added the **Supported Account Types** setting to simplify matching account types with your Entra ID application settings.

  Additionally, the **Tenant ID** field is now called **Single Tenant ID** for clarity.

  |   |                                                                          |
  | - | ------------------------------------------------------------------------ |
  |   | If you're upgrading, your current adapter configuration will still work. |

## Microsoft Login Integration Kit 1.0 – June 2021

* Initial release.

* Added the ability to use browser redirect or pop-up window for the sign-on presentation. Learn more in the **Microsoft Sign-on Presentation** field description in [Microsoft IdP Adapter settings reference](../setup/pf_microsoft_login_ik_idp_adapter_settings_reference.html).

* Added customizable user-facing language-pack messages and customizable sign-on templates for the pop-up window presentation. Learn more in [Download manifest](pf_microsoft_login_ik_download_manifest.html).

* Added support for the [PingFederate authentication API](https://docs.pingidentity.com/pingfederate/latest/developers_reference_guide/pf_authentication_api.html).

* Added support for the [JavaScript Widget for the PingFederate Authentication API](https://github.com/pingidentity/pf-authn-js-widget).

---

---
title: Configuring an adapter instance
description: Configure the Microsoft IdP Adapter to determine how PingFederate communicates with Entra ID (formerly Azure AD).
component: microsoft-login
page_id: microsoft-login:setup:pf_microsoft_login_ik_configuring_an_adapter_instance
canonical_url: https://docs.pingidentity.com/integrations/microsoft-login/setup/pf_microsoft_login_ik_configuring_an_adapter_instance.html
llms_txt: https://docs.pingidentity.com/integrations/microsoft-login/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 17, 2025
section_ids:
  steps: Steps
---

# Configuring an adapter instance

Configure the Microsoft IdP Adapter to determine how PingFederate communicates with Entra ID (formerly Azure AD).

## Steps

1. In the PingFederate admin console, go to **Authentication > Integration > IdP Adapters**. Click **Create New Instance**.

2. On the **Type** tab, set the basic adapter instance attributes:

   1. In the **Instance Name** field, enter a name for the adapter instance.

   2. In the **Instance ID** field, enter a unique identifier for the adapter instance.

   3. In the **Type** list, select **Microsoft IdP Adapter**. Click **Next**.

3. (Optional) On the **IdP Adapter** tab, in the **Additional Parameters** section, add any additional parameters to send in the authorization request to Microsoft, then map them to the local chained attribute:

   1. Click **Add a new row to 'Additional Parameters'**.

   2. In the **Parameter** field, enter the name of a query string parameter that you want to send.

   3. In the **Local Chained Attribute** field, enter the name of the chained attribute whose value will be used as the parameter value in the authorization request to Microsoft.

   4. In the **Action** column, click **Update**.

   5. To add more attributes, repeat steps a - d.

4. On the **IdP Adapter** tab, finish configuring the adapter instance by referring to [Microsoft IdP Adapter settings reference](pf_microsoft_login_ik_idp_adapter_settings_reference.html). Click **Next**.

5. On the **Actions** tab, test your connection to Entra ID. Resolve any issues that are reported, and then click **Next**.

6. On the **Extended Contract** tab, add any attributes that you want to include in the contract. Click **Next**.

7. On the **Adapter Attributes** tab, set pseudonym and masking options as shown in [Set pseudonym and masking options](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_setting_pseudonym_masking_options.html) in the PingFederate documentation. Click **Next**.

8. On the **Adapter Contract Mapping** tab, configure the contract fulfillment details for the adapter as shown in [Define the IdP adapter contract](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_authnadapterinstancetasklet_plugincontractstate.html) in the PingFederate documentation. Click **Next**.

9. On the **Summary** tab, check your configuration, then click **Save**.

---

---
title: Core contract attributes
description: The following are the core contract attributes for the Microsoft IdP Adapter.
component: microsoft-login
page_id: microsoft-login:setup:pf_microsoft_login_ik_core_contract_attributes
canonical_url: https://docs.pingidentity.com/integrations/microsoft-login/setup/pf_microsoft_login_ik_core_contract_attributes.html
llms_txt: https://docs.pingidentity.com/integrations/microsoft-login/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 2, 2025
---

# Core contract attributes

The following are the core contract attributes for the Microsoft IdP Adapter.

| Attribute           | Details                                                                                                           |
| ------------------- | ----------------------------------------------------------------------------------------------------------------- |
| `businessPhones`    | The user's business phone number.                                                                                 |
| `displayName`       | The user's full name.                                                                                             |
| `givenName`         | The user's first name.                                                                                            |
| `id`                | The user's Microsoft user ID.                                                                                     |
| `jobTitle`          | The user's job title.                                                                                             |
| `mail`              | The user's email address.                                                                                         |
| `mobilePhone`       | The user's mobile phone number.                                                                                   |
| `officeLocation`    | The company office location.                                                                                      |
| `preferredLanguage` | Preferred language configured on Microsoft.                                                                       |
| `surname`           | The user's last name.                                                                                             |
| `userPrincipalName` | The user's principal name from Microsoft.                                                                         |
| `idToken`           | A JWT from Microsoft that's used in authentication.                                                               |
| `accessToken`       | A JWT from Microsoft that's used in authorization.                                                                |
| `tenantId`          | A header claim encoded in the `idToken` JWT that lists which tenant the user is authenticating to during sign-on. |

---

---
title: Deploying the integration files
description: To get started with the integration, deploy the Microsoft Login Integration Kit files to your PingFederate directory.
component: microsoft-login
page_id: microsoft-login:setup:pf_microsoft_login_ik_deploying_the_integration_files
canonical_url: https://docs.pingidentity.com/integrations/microsoft-login/setup/pf_microsoft_login_ik_deploying_the_integration_files.html
llms_txt: https://docs.pingidentity.com/integrations/microsoft-login/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 17, 2025
section_ids:
  steps: Steps
---

# Deploying the integration files

To get started with the integration, deploy the Microsoft Login Integration Kit files to your PingFederate directory.

## Steps

1. Download the Microsoft Login Integration Kit `.zip` archive from the [**Add-ons** tab of the PingFederate downloads page](https://www.pingidentity.com/en/resources/downloads/pingfederate.html) or the [Ping Identity Marketplace](https://marketplace.pingone.com/item/microsoft-login-integration-kit).

2. Stop PingFederate if it's running.

3. If you're upgrading an existing deployment, back up your customizations and delete previous versions of the integration files.

   1. Back up any Microsoft Login Integration Kit files that you customized in `<pf_install>/pingfederate/server/default/conf/`.

   2. Delete `pf-microsoft-idp-adapter-<version>.jar` from `<pf_install>/pingfederate/server/default/deploy`.

4. Extract the `.zip` archive and merge the contents of the `dist` directory with your `<pf_install>/pingfederate` directory.

5. If there's more than one version of the `pf-authn-api-sdk-<version>.jar` file in your `<pf_install>/pingfederate/server/default/lib` directory, delete all but the latest version of the file.

6. If you backed up any customized files, modify the new files with your customizations.

7. Start PingFederate.

8. If you operate PingFederate in a cluster, repeat steps 2 - 7 for each engine node.

---

---
title: Download manifest
description: The following files are included in the Microsoft Login Integration Kit download.
component: microsoft-login
page_id: microsoft-login:release_notes:pf_microsoft_login_ik_download_manifest
canonical_url: https://docs.pingidentity.com/integrations/microsoft-login/release_notes/pf_microsoft_login_ik_download_manifest.html
llms_txt: https://docs.pingidentity.com/integrations/microsoft-login/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 2, 2025
---

# Download manifest

The following files are included in the Microsoft Login Integration Kit download.

* `Legal.pdf`: Copyright and license information.

* `dist/pingfederate/server/default`: Contains the integration files.

  * `deploy`: Contains the Java libraries.

    * `pf-microsoft-idp-adapter-<version>.jar`: A JAR file that contains the Microsoft IdP Adapter.

  * `conf`: Contains the HTML template that presents the Microsoft sign-on form.

    * `language-packs`: Contains files with customizable user-facing messages.

      * `authn-api-messages.properties`: A version of the common PingFederate authentication API variable file that includes adapter-specific messages.

      * `pingfederate-microsoft-adapter-messages.properties`: A variable file that customizes the messages that appear on the template files.

    * `template`: Contains user-facing HTML template files.

      * `assets`: Contains functional scripts and files used by the template.

        * `css/microsoft.css`: A CSS file that customizes the appearance of the template files.

        * `fonts/end-user`: Contains template fonts and icons.

          * `icons`: Contains template icons.

        * `images`: Contains template image files.

          * `ping-logo.svg`: An image file with company branding.

        * `microsoft-pop-up-template.html`: A template that opens a pop-up window to prompt the user to sign on.

        * `microsoft-post-auth-template.html`: A template that returns the user to the PingFederate sign-on flow after they sign on with Microsoft.

  * `lib/pf-authn-api-sdk-<version>.jar`: A JAR file that contains the PingFederate Authentication API SDK.

---

---
title: Enabling debug logging
description: To help with troubleshooting or monitoring, you can turn on activity logging for the adapter.
component: microsoft-login
page_id: microsoft-login:troubleshooting:pf_microsoft_login_ik_enabling_debug_logging
canonical_url: https://docs.pingidentity.com/integrations/microsoft-login/troubleshooting/pf_microsoft_login_ik_enabling_debug_logging.html
llms_txt: https://docs.pingidentity.com/integrations/microsoft-login/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 2, 2025
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Enabling debug logging

To help with troubleshooting or monitoring, you can turn on activity logging for the adapter.

## About this task

These steps are optional. You can find general information about logging in [Enabling debug messages and console logging](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_enabling_debug_message_and_console_logging.html) in the PingFederate documentation.

## Steps

1. Open the `<pf_install>/pingfederate/server/default/conf/log4j2.xml` file for editing.

2. To log activity for PingFederate and all adapters:

   1. Find the following section:

      ```html
      <AsyncRoot level="INFO" includeLocation="false">
      	<!-- <AppenderRef ref="CONSOLE" /> -->
      	<AppenderRef ref="FILE" />
      </AsyncRoot>
      ```

   2. Change `INFO` to `DEBUG`:

      ```html
      <AsyncRoot level="DEBUG" includeLocation="false">
      	<!-- <AppenderRef ref="CONSOLE" /> -->
      	<AppenderRef ref="FILE" />
      </AsyncRoot>
      ```

   3. If you want to see the adapter activity in the console, remove the comment tags:

      ```html
      <AsyncRoot level="INFO" includeLocation="false">
      	<AppenderRef ref="CONSOLE" />
      	<AppenderRef ref="FILE" />
      </AsyncRoot>
      ```

3. To log activity for only the Microsoft IdP Adapter, add the following line:

   ```html
   <Logger name="com.pingidentity.adapter.idp.microsoft" level="DEBUG"/>
   ```

4. Save the file.

---

---
title: Integrating social sign-on into your application
description: To complete your Microsoft sign-on integration, add a sign-on hyperlink to your application.
component: microsoft-login
page_id: microsoft-login:setup:pf_microsoft_login_ik_integrating_social_sign_on_into_your_application
canonical_url: https://docs.pingidentity.com/integrations/microsoft-login/setup/pf_microsoft_login_ik_integrating_social_sign_on_into_your_application.html
llms_txt: https://docs.pingidentity.com/integrations/microsoft-login/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 23, 2025
section_ids:
  steps: Steps
---

# Integrating social sign-on into your application

To complete your Microsoft sign-on integration, add a sign-on hyperlink to your application.

## Steps

1. If your application is outside the PingFederate domain, configure an SP connection:

   1. Create a service provider (SP) connection to your application as shown in [SP connection management](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_sp_connect_management.html) in the PingFederate documentation.

      |   |                                                                                                                                                                                                                                                                       |
      | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      |   | Use the Microsoft IdP Adapter instance as an authentication source. Learn more in [Mapping an adapter instance](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_mapping_adapter_instance.html) in the PingFederate documentation. |

   2. In your web application, create a hyperlink to allow users to sign on to the SP application. Use the following URL and replace the variables based on the descriptions in the following table:

      `https://<pf_host>:<pf_port>/idp/startSSO.ping?PartnerSpId=<ConnectionId>`

      | Variable          | Description                                                                                          |
      | ----------------- | ---------------------------------------------------------------------------------------------------- |
      | *\<pf\_host>*     | The host name or IP address of the PingFederate server.                                              |
      | *\<pf\_port>*     | The port number for PingFederate.                                                                    |
      | *\<ConnectionId>* | The federation identifier of the SP for the connection that uses the Microsoft IdP Adapter instance. |

2. If your application is inside the PingFederate domain, configure an adapter-to-adapter mapping:

   1. Create an SP connection to your application as shown in [SP connection management](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_sp_connect_management.html) in the PingFederate documentation.

      |   |                                                                                                                                                                                                                                                                       |
      | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      |   | Use the Microsoft IdP Adapter instance as an authentication source. Learn more in [Mapping an adapter instance](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_mapping_adapter_instance.html) in the PingFederate documentation. |

   2. On the **System > Protocol Settings > Roles & Protocols** page, select **Enable Identity Provider (IdP) role and support for the following** and **Enable Service Provider (SP) role and support for the following**.

   3. In both the **Enable Identity Provider** and **Enable Service Provider** sections, select any protocol, such as **SAML 2.0**. Click **Save**.

      |   |                                                                                                                                  |
      | - | -------------------------------------------------------------------------------------------------------------------------------- |
      |   | PingFederate requires a protocol selection to activate the roles. The protocol that you select is not used for this integration. |

   4. On the **Service Provider > Adapters** page, create or select an adapter instance that's integrated with the application as shown in [SP application integration settings](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_sp_applicat_integra_settings.html) in the PingFederate documentation.

   5. On the **Identity Provider > Adapter-to-Adapter Mappings** page, configure the IdP-to-SP adapter mapping as shown in [Adapter-to-adapter mappings](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_adaptertoadapter_mappings.html) in the PingFederate documentation.

   6. In your web application, create a hyperlink to allow users to sign on to the SP application. Use the following URL and replace the variables based on the descriptions in the table below:

      `https://<pf_host>:<pf_port>/pf/adapter2adapter.ping?IdpAdapterId=<IdpAdapterId>&SpSessionAuthnAdapterId=<SpAdapterId>`

      | Variable          | Description                                                                               |
      | ----------------- | ----------------------------------------------------------------------------------------- |
      | *\<pf\_host>*     | The host name or IP address of the PingFederate server.                                   |
      | *\<pf\_port>*     | The port number for PingFederate.                                                         |
      | *\<IdpAdapterId>* | The instance ID of the Microsoft IdP Adapter instance.                                    |
      | *\<SpAdapterId>*  | The instance ID of the SP adapter instance that has been integrated with the application. |

---

---
title: Known issues and limitations
description: The following are known issues or limitations with the Microsoft Login Integration Kit.
component: microsoft-login
page_id: microsoft-login:release_notes:pf_microsoft_login_ik_known_issues_and_limitations
canonical_url: https://docs.pingidentity.com/integrations/microsoft-login/release_notes/pf_microsoft_login_ik_known_issues_and_limitations.html
llms_txt: https://docs.pingidentity.com/integrations/microsoft-login/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 2, 2025
section_ids:
  known-issues: Known issues
  known-limitations: Known limitations
---

# Known issues and limitations

The following are known issues or limitations with the Microsoft Login Integration Kit.

## Known issues

There are no known issues.

## Known limitations

There are no known limitations.

---

---
title: Microsoft IdP Adapter settings reference
description: Field descriptions for the Microsoft IdP Adapter configuration screen.
component: microsoft-login
page_id: microsoft-login:setup:pf_microsoft_login_ik_idp_adapter_settings_reference
canonical_url: https://docs.pingidentity.com/integrations/microsoft-login/setup/pf_microsoft_login_ik_idp_adapter_settings_reference.html
llms_txt: https://docs.pingidentity.com/integrations/microsoft-login/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 17, 2025
---

# Microsoft IdP Adapter settings reference

Field descriptions for the Microsoft IdP Adapter configuration screen.

> **Collapse: Standard fields**
>
> | Field Name                    | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
> | ----------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
> | **Supported Account Types**   | The type of accounts that users can sign on with. The **Single tenant** and **Multitenant** options support organizational accounts from a school or work directory. Personal accounts are not associated with an organization.Do one of the following:- For standard configurations, select **Personal accounts only**.
>
> - For advanced configurations, if you selected a different option in [Registering PingFederate as an application in Entra ID](pf_microsoft_login_ik_registering_pf_as_an_application_in_azure.html), make the same selection here.The default selection is **Personal accounts only**. |
> | **Single Tenant ID**          | If you selected **Single tenant** for **Support Account Types**, enter the **Directory (tenant) ID** that you noted in [Registering PingFederate as an application in Entra ID](pf_microsoft_login_ik_registering_pf_as_an_application_in_azure.html). Otherwise, leave this field blank.This field is blank by default.                                                                                                                                                                                                                                                                                         |
> | **Client ID**                 | The **Application (client) ID** that you noted in [Registering PingFederate as an application in Entra ID](pf_microsoft_login_ik_registering_pf_as_an_application_in_azure.html).                                                                                                                                                                                                                                                                                                                                                                                                                                |
> | **Client Secret**             | The client secret **Value** that you noted in [Registering PingFederate as an application in Entra ID](pf_microsoft_login_ik_registering_pf_as_an_application_in_azure.html).                                                                                                                                                                                                                                                                                                                                                                                                                                    |
> | **Error Redirect URL**        | The URL that PingFederate redirects the user to when the adapter encounters an error.If this field is blank, the adapter shows the default error page.                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
> | **Unauthorized Redirect URL** | The URL that PingFederate redirects to when the user doesn't authorize Microsoft to share their information.If this field is blank, the adapter shows the default error page.                                                                                                                                                                                                                                                                                                                                                                                                                                    |

> **Collapse: Advanced fields**
>
> | Field Name                           | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
> | ------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
> | **Include Login Hint**               | If selected, the incoming **User Id** value (if provided) is sent as a **login\_hint** query string parameter value to Microsoft.Microsoft uses this value to pre-fill the **Username** field on the Microsoft user sign-on page.                                                                                                                                                                                                                                                                                                                                                                                      |
> | **Include Prompt**                   | If selected, PingFederate automatically maps and sends the standard PingFederate-supported OIDC prompt parameter as the **prompt** parameter value in the authorization request to Microsoft.&#xA;&#xA;This applies only if PingFederate receives the prompt parameter through an authentication policy that has a value of consent or login.To send other values in the authorization request, use the **Additional Parameters** table and provide the value in an incoming chained attribute. Learn more in step 3 of [Configuring an adapter instance](pf_microsoft_login_ik_configuring_an_adapter_instance.html). |
> | **Microsoft Login Base URL**         | The base URL Microsoft uses for any authentication calls. The default value is:```none
> https://login.microsoftonline.com/
> ```                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
> | **Authorization Callback Endpoint**  | The PingFederate endpoint that Microsoft uses to respond to authorization requests. The default value is:```none
> /microsoft-authn
> ```&#xA;&#xA;If you set a custom endpoint in the Redirect URI field in Registering PingFederate as an application in Entra ID, change this field to match.                                                                                                                                                                                                                                                                                                                           |
> | **Microsoft Authorization Endpoint** | The endpoint used to request an authorization code from Microsoft. The default value is:```none
> /oauth2/v2.0/authorize
> ```                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
> | **Microsoft Token Endpoint**         | The endpoint Microsoft uses to retrieve an access token. The default value is:```none
> /oauth2/v2.0/token
> ```                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
> | **Microsoft Logout Endpoint**        | The logout endpoint Microsoft uses to end the user's session. The default value is:```none
> /oauth2/v2.0/logout
> ```                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
> | **Microsoft User Info URL**          | The URL used to retrieve Microsoft user data. The default value is:```none
> https://graph.microsoft.com/v1.0/me
> ```                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
> | **Scopes**                           | A list of comma-separated scopes to request from Microsoft. The default value is:```none
> openid, User.Read
> ```&#xA;&#xA;You must add the User.Read scope.                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
> | **Microsoft Sign-on Presentation**   | Determines how the user is directed to Microsoft for authentication. Options include:- **Redirect**
>
> - **Pop-up window**&#xA;&#xA;Some browsers block automatic redirects. If you select Pop-up window and aren't using PingFederate in authentication API mode, the adapter presents a template file.                                                                                                                                                                                                                                                                                                                 |
> | **Microsoft Pop-up Template**        | The template file that presents the Microsoft sign-on form.&#xA;&#xA;Applies only when Microsoft Sign-on Presentation is set to Pop-up window\.The default value is:```none
> microsoft-pop-up-template.html
> ```                                                                                                                                                                                                                                                                                                                                                                                                         |
> | **Microsoft Post Auth Template**     | The template file that the adapter presents after the user signs on.&#xA;&#xA;Applies only when Microsoft Sign-on Presentation is set to Pop-up window\.The default value is:```none
> microsoft-post-auth-template.html
> ```                                                                                                                                                                                                                                                                                                                                                                                             |
> | **Microsoft Messages File**          | The language-pack file associated with **Microsoft Pop-up Template**.The default value is:```none
> pingfederate-microsoft-adapter-messages
> ```                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
> | **Retry Request**                    | Select this checkbox to retry a request if the API fails with error codes configured.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
> | **Maximum Retries Limit**            | Determines how many times PingFederate will retry a request.The default value is `5`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
> | **Retry Error Codes**                | Determines which response codes are considered failures.The default value is `403`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
> | **API Request Timeout**              | The amount of time in milliseconds that PingFederate allows when establishing a connection with Entra ID or waiting for a response to a request. A value of 0 disables the timeout.The default value is `5000`.                                                                                                                                                                                                                                                                                                                                                                                                        |
> | **Proxy Settings**                   | Defines proxy settings for outbound HTTP requests.The default value is **System Defaults**.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
> | **Custom Proxy Host**                | The proxy server host name to use when **Proxy Settings** is set to **Custom**.This field is blank by default.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
> | **Custom Proxy Port**                | The proxy server port to use when **Proxy Settings** is set to **Custom**.This field is blank by default.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |

---

---
title: Microsoft Login Integration Kit
description: The Microsoft Login Integration Kit allows PingFederate to use Microsoft as an identity provider (IdP). This allows users to access service provider (SP) applications by signing into Microsoft.
component: microsoft-login
page_id: microsoft-login::pf_microsoft_login_ik
canonical_url: https://docs.pingidentity.com/integrations/microsoft-login/pf_microsoft_login_ik.html
llms_txt: https://docs.pingidentity.com/integrations/microsoft-login/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 17, 2025
section_ids:
  features: Features
  components: Components
  intended-audience: Intended audience
  system-requirements: System requirements
---

# Microsoft Login Integration Kit

The Microsoft Login Integration Kit allows PingFederate to use Microsoft as an identity provider (IdP). This allows users to access service provider (SP) applications by signing into Microsoft.

## Features

* Supports the [PingFederate authentication API](https://docs.pingidentity.com/pingfederate/latest/developers_reference_guide/pf_authentication_api.html).

* Supports the [JavaScript Widget for the PingFederate Authentication API](https://github.com/pingidentity/pf-authn-js-widget).

## Components

* Microsoft IdP Adapter

  * Allows PingFederate to communicate with the Microsoft API to process sign-on requests and get user information.

* Templates

  * Allow the adapter to prompt the user to sign on.

  * Allow you to modify the appearance of the sign-on prompt.

  |   |                                                                                                                                                                                                                                                                                  |
  | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | You choose whether to present the template with a browser redirect or as a pop-up window. Learn more in the **Microsoft Sign-on Presentation** field description in [Microsoft IdP Adapter settings reference](setup/pf_microsoft_login_ik_idp_adapter_settings_reference.html). |

* Language packs

  * Allow you to customize or localize the messages returned by the PingFederate authentication API and shown on the templates during authentication. Learn more in [Localizing messages for end users](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_local_message_end_users.html) in the PingFederate documentation.

## Intended audience

This document is intended for PingFederate administrators.

If you need help during the setup process, use the following resources:

* PingFederate documentation:

  * [Identity provider SSO configuration](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_ident_provid_sso_config.html)

  * [Managing IdP adapters](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_managing_idp_adapters.html)

  * [Authentication policies](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_authentication_policies.html)

  * [SP connection management](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_sp_connect_management.html)

* [Register an application with the Microsoft identity platform](https://docs.microsoft.com/en-us/azure/active-directory/develop/quickstart-register-app) in the Microsoft documentation.

## System requirements

* PingFederate 11.3 or later

* A Microsoft developer account with Entra ID

---

---
title: Overview of the SSO flow
description: With the Microsoft Login Integration Kit, PingFederate includes the Microsoft authentication API in the sign-on flow.
component: microsoft-login
page_id: microsoft-login::pf_microsoft_login_ik_overview_of_the_sso_flow
canonical_url: https://docs.pingidentity.com/integrations/microsoft-login/pf_microsoft_login_ik_overview_of_the_sso_flow.html
llms_txt: https://docs.pingidentity.com/integrations/microsoft-login/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 23, 2025
section_ids:
  description: Description
---

# Overview of the SSO flow

With the Microsoft Login Integration Kit, PingFederate includes the Microsoft authentication API in the sign-on flow.

The following figure illustrates a single sign-on (SSO) scenario in which PingFederate authenticates users to an SP application using the Microsoft IdP Adapter.

![Diagram showing the SSO flow using the Microsoft IdP Adapter.](_images/ms_login_ik_sso_flow_diagram.png)

## Description

1. The user opens a web application and chooses the Microsoft sign-on option. The sign-on link points to the Microsoft IdP Adapter.

2. The Microsoft IdP Adapter redirects the browser to Microsoft with a list of requested permissions.

3. On Microsoft, the user authenticates their identity and then authorizes the requested permissions.

4. Microsoft redirects the browser to the Microsoft IdP Adapter authorization callback endpoint with an authorization code.

   If the user fails to authenticate or does not authorize the request, the response includes an error code instead.

5. PingFederate sends Microsoft the authorization code.

6. Microsoft returns an access token.

7. PingFederate sends Microsoft a request for user attributes, and presents the access token.

8. Microsoft verifies the access token, and provides the user information.

9. PingFederate redirects the user to the web application with the user attributes.

---

---
title: Registering PingFederate as an application in Entra ID
description: To allow PingFederate to process social sign-on requests with Microsoft, add PingFederate as an OAuth application in the Entra ID (formerly Microsoft Azure) portal.
component: microsoft-login
page_id: microsoft-login:setup:pf_microsoft_login_ik_registering_pf_as_an_application_in_azure
canonical_url: https://docs.pingidentity.com/integrations/microsoft-login/setup/pf_microsoft_login_ik_registering_pf_as_an_application_in_azure.html
llms_txt: https://docs.pingidentity.com/integrations/microsoft-login/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 2, 2025
section_ids:
  steps: Steps
---

# Registering PingFederate as an application in Entra ID

To allow PingFederate to process social sign-on requests with Microsoft, add PingFederate as an OAuth application in the Entra ID (formerly Microsoft Azure) portal.

You can find more information in [Register an application](https://docs.microsoft.com/en-us/azure/active-directory/develop/quickstart-register-app//) in the Microsoft Entra ID documentation.

## Steps

1. Sign on to the [Microsoft Entra ID admin center](https://entra.microsoft.com/) and go to the tenant you want to register the application in.

   To ensure you have the correct permissions for creating an application, you must use an account that has at least the [Application Developer](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#application-developer) role.

2. Go to **Entra ID > App registrations**. Click **New registration**.

3. On the **Register an application** page:

   1. In the **Name** field, enter a name for the application.

   2. In the **Supported account types** section, select the account types that have permission to access the application.

      The default selection is **Personal Microsoft accounts only**.

      |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
      | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      |   | Advanced configurations can provide access to organizational accounts in addition to, or instead of, personal Microsoft accounts. Learn more about the available options in [Register an application](https://docs.microsoft.com/en-us/azure/active-directory/develop/quickstart-register-app//) in the Microsoft documentation.Note that each individual organization must have `User.Read.All` set in its API permissions. External organizations might not have this set.Remember your **Support account types** selection. You'll make the same selection in [Microsoft IdP Adapter settings reference](pf_microsoft_login_ik_idp_adapter_settings_reference.html). |

   3. In the **Redirect URI** section, select **Web** and enter the PingFederate **Authorization Callback Endpoint**.

      The default value is `https://<pf_host>:<pf_port>/ext/microsoft-authn`.

      |   |                                                                                                                                                                                                                                                                                                                                                                                                |
      | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      |   | If you set a custom value here, write it down. You'll use it again in [Microsoft IdP Adapter settings reference](pf_microsoft_login_ik_idp_adapter_settings_reference.html).You can find more information about redirect URI configuration in [Add a redirect URI](https://learn.microsoft.com/en-us/entra/identity-platform/how-to-add-redirect-uri) in the Microsoft Entra ID documentation. |

   4. Click **Register**.

4. On the application **Overview** page, in the **Essentials** section, note the **Application (client) ID**. If you selected the **Single tenant** option for **Supported Account Types**, also note the **Directory (tenant) ID**.

   |   |                                                                                                                                       |
   | - | ------------------------------------------------------------------------------------------------------------------------------------- |
   |   | You'll use this information in [Microsoft IdP Adapter settings reference](pf_microsoft_login_ik_idp_adapter_settings_reference.html). |

5. Add a client secret:

   1. Go to the **Certificates & secrets** page, click the **Client secrets** tab, then click **+ New client secret**.

   2. On the **Add a client secret** page, in the **Description** field, enter a meaningful description.

   3. In the **Expires** list, select an expiration period, then click **Add**.

      |   |                                                                                                                                                                                                                                                        |
      | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
      |   | Microsoft recommends that you set an expiration value of less than 12 months. Learn more in [Add a client secret](https://learn.microsoft.com/en-us/entra/identity-platform/how-to-add-credentials?tabs=client-secret) in the Microsoft documentation. |

      ![Screen capture of the Certificates and secrets page with the Certificates & secrets section in the menu highlighted along with the New client secret button and the Value field.](_images/ms_login_ik_add_a_client_secret.png)

   4. Note the client secret **Value**.

      |   |                                                                                                                                                                                                           |
      | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      |   | The secret value is never displayed again after you leave this page.You'll use this information in [Microsoft IdP Adapter settings reference](pf_microsoft_login_ik_idp_adapter_settings_reference.html). |