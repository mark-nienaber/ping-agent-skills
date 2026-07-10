---
title: Authentication API Support
description: You can use the PingFederate Authentication API to integrate the LinkedIn IdP Adapter into your application.
component: linkedin
page_id: linkedin::pf_linkedin_cic_authentication_api_support
canonical_url: https://docs.pingidentity.com/integrations/linkedin/pf_linkedin_cic_authentication_api_support.html
llms_txt: https://docs.pingidentity.com/integrations/linkedin/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 17, 2025
---

# Authentication API Support

You can use the PingFederate Authentication API to integrate the LinkedIn IdP Adapter into your application.

The PingFederate Authentication API provides access to the current state of the authentication flow as a user steps through the PingFederate authentication policy. Learn more in [PingFederate authentication API](https://docs.pingidentity.com/pingfederate/latest/developers_reference_guide/pf_authentication_api.html) in the PingFederate documentation.

To integrate the LinkedIn IdP Adapter into your authentication flow, configure your application based on the states, actions, and models available in the PingFederate Authentication API Explorer. You can find help in [Exploring the Authentication API](https://docs.pingidentity.com/pingfederate/latest/developers_reference_guide/pf_exploring_authentication_api.html) in the PingFederate documentation.

---

---
title: Changelog
description: The following is the change history for the LinkedIn Login Integration Kit.
component: linkedin
page_id: linkedin:release_notes:pf_linkedin_cic_changelog
canonical_url: https://docs.pingidentity.com/integrations/linkedin/release_notes/pf_linkedin_cic_changelog.html
llms_txt: https://docs.pingidentity.com/integrations/linkedin/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: February 19, 2026
section_ids:
  version-3-0-2-january-2026: Version 3.0.2 - January 2026
  version-3-0-1-november-2025: Version 3.0.1 - November 2025
  version-3-0-august-2025: Version 3.0 - August 2025
  version-2-2-december-2020: Version 2.2 – December 2020
  version-2-1-february-2020: Version 2.1 – February 2020
  version-2-0-1-february-2019: Version 2.0.1 – February 2019
  version-2-0-january-2019: Version 2.0 – January 2019
  version-1-1-1-august-2018: Version 1.1.1 – August 2018
  version-1-1-october-2017: Version 1.1 – October 2017
  version-1-0-1-july-2013: Version 1.0.1 – July 2013
  version-1-0-february-2011: Version 1.0 – February 2011
---

# Changelog

The following is the change history for the LinkedIn Login Integration Kit.

## Version 3.0.2 - January 2026

* Removed third-party fonts and the `authn-api-messages.properties` file.

## Version 3.0.1 - November 2025

* Fixed an issue that caused the adapter to ignore the value of the **PingFederate Base URL** field and fail to produce an error if the value of the field was invalid.

* Updated library dependencies to address potential security vulnerabilities.

## Version 3.0 - August 2025

|   |                                                                                                                                                                                                                                                                                                                |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | LinkedIn IdP Adapter 2.2 and earlier aren't compatible with recent changes to the LinkedIn API. When upgrading from LinkedIn Login Integration Kit 2.2 or earlier, make sure to follow the instructions in [Upgrading an existing deployment](../setup/pf_linkedin_cic_upgrading_an_existing_deployment.html). |

* Added support for the API endpoints and scopes described in [Sign In with LinkedIn using OpenID Connect](https://learn.microsoft.com/en-us/linkedin/consumer/integrations/self-serve/sign-in-with-linkedin-v2) in the LinkedIn documentation.

* Updated the [Core contract attributes](../setup/pf_linkedin_cic_core_contract_attributes.html).

* Deprecated API endpoints and scopes that are no longer relevant.

## Version 2.2 – December 2020

* Added a setting to use browser redirect or pop-up window for the sign-on presentation.

* Added customizable sign-on templates for the pop-up window presentation.

* Added customizable user-facing language-pack messages.

* Added support for the [JavaScript Widget for the PingFederate Authentication API](https://github.com/pingidentity/pf-authn-js-widget).

* Added support for the [PingFederate authentication API](https://docs.pingidentity.com/pingfederate/latest/developers_reference_guide/pf_authentication_api.html).

## Version 2.1 – February 2020

* Added the ability to retrieve user attributes and email addresses with the same adapter instance.

## Version 2.0.1 – February 2019

* Fixed an issue that prevented the LinkedIn IdP Adapter from working in some OAuth scenarios.

* Changed some fields on the adapter configuration page to match LinkedIn terminology.

## Version 2.0 – January 2019

* Updated the adapter to conform to OAuth 2.0 standards and version 2.0 of LinkedIn's APIs. You can find a description of the API changes in the [Self-Serve v1 to v2 API Migration Frequently Asked Questions](https://docs.microsoft.com/en-us/linkedin/consumer/integrations/self-serve/migration-faq?context=linkedin/consumer/context) in the LinkedIn documentation.

## Version 1.1.1 – August 2018

|   |                                                                                                           |
| - | --------------------------------------------------------------------------------------------------------- |
|   | LinkedIn IdP Adapter 1.1.1 and earlier aren't compatible with the March 2019 changes to the LinkedIn API. |

* Simplified logout handling within the adapter by removing the **Perform Logout** checkbox and unnecessary iframe-based redirects.

## Version 1.1 – October 2017

* Added compatibility updates for the latest LinkedIn API.

## Version 1.0.1 – July 2013

* Added masking to the **Application ID** and **Application Secret** fields in the adapter instance configuration tab.

* Added support for Scribe 1.3.3.

## Version 1.0 – February 2011

* Initial release.

---

---
title: Configuring an adapter instance
description: Configure the LinkedIn IdP Adapter to determine how PingFederate communicates with LinkedIn.
component: linkedin
page_id: linkedin:setup:pf_linkedin_cic_configuring_an_adapter_instance
canonical_url: https://docs.pingidentity.com/integrations/linkedin/setup/pf_linkedin_cic_configuring_an_adapter_instance.html
llms_txt: https://docs.pingidentity.com/integrations/linkedin/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 17, 2025
section_ids:
  steps: Steps
---

# Configuring an adapter instance

Configure the LinkedIn IdP Adapter to determine how PingFederate communicates with LinkedIn.

## Steps

1. In the PingFederate administrative console, go to **Authentication > Integration > IdP Adapters**. Click **Create New Instance**.

2. On the **Type** tab, set the basic adapter instance attributes.

   1. In the **Instance Name** field, enter a name for the adapter instance.

   2. In the **Instance ID** field, enter a unique identifier for the adapter instance.

   3. In the **Type** list, select **LinkedIn IdP Adapter**. Click **Next**.

3. (Optional) On the **IdP Adapter** screen, in the **Optional LinkedIn Attributes** section, define mappings between local attributes and the attributes from the core or extended contract.

   You can find a list of available attributes in [Core contract attributes](pf_linkedin_cic_core_contract_attributes.html).

   1. Click **Add a new row to 'Attribute Selector'**.

   2. In the **Local Attribute** field, enter the name of a local attribute.

   3. In the **LinkedIn Attribute** field, enter the JSON Pointer syntax for the value of the matching LinkedIn attribute.

      Learn more in [JSON Pointer syntax reference](pf_linkedin_cic_json_pointer_syntax_reference.html).

      |   |                                                                                            |
      | - | ------------------------------------------------------------------------------------------ |
      |   | The **Permissions** field on the **IdP Adapter** page determines the available attributes. |

   4. In the **Action** column, click **Update**.

   5. To add more attributes, repeat steps a - d.

4. On the **IdP Adapter** tab, configure the adapter instance by referring to [LinkedIn IdP Adapter settings](pf_linkedin_cic_linkedin_idp_adapter_settings.html). Click **Next**.

5. On the **Actions** tab, click **Test Connection**. Resolve any reported issues, then click **Next**.

6. On the **Extended Contract** tab, add the attributes that you want to include in the contract:

   1. Add the list of local attributes that you mapped on the **IdP Adapter** tab.

   2. Add any other LinkedIn attributes that you want to include in the contract.

      |   |                                                                                                                                                                                                                                                                                                         |
      | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      |   | The values for unmapped LinkedIn attributes will be populated with raw JSON and could include arrays. You can find more information in [Object Types](https://docs.microsoft.com/en-us/linkedin/shared/references/v2/object-types?context=linkedin/consumer/context) in the LinkedIn API documentation. |

   3. Click **Next**

7. On the **Adapter Attributes** tab, set pseudonym and masking options as shown in [Set pseudonym and masking options](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_setting_pseudonym_masking_options.html) in the PingFederate documentation. Click **Next**.

8. On the **Adapter Contract Mapping** tab, configure the contract fulfillment details for the adapter as shown in [Define the IdP adapter contract](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_authnadapterinstancetasklet_plugincontractstate.html) in the PingFederate documentation. Click **Next**.

9. On the **Summary** tab, check and save your configuration.

10. If you created this adapter instance to replace a previous one, update the adapter mappings in any related service provider connections.

---

---
title: Core contract attributes
description: access_token
component: linkedin
page_id: linkedin:setup:pf_linkedin_cic_core_contract_attributes
canonical_url: https://docs.pingidentity.com/integrations/linkedin/setup/pf_linkedin_cic_core_contract_attributes.html
llms_txt: https://docs.pingidentity.com/integrations/linkedin/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 17, 2025
---

# Core contract attributes

| Attribute                  | Details                                                                                                                          |
| -------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| `access_token`             | The access token that LinkedIn provides to your application.                                                                     |
| `access_token_expires_in`  | The access token's expiration date.                                                                                              |
| `email`                    | The user's primary email address.                                                                                                |
| `email_verified`           | Indicator that the user's primary email has been verified.                                                                       |
| `family_name`              | The user's last name.                                                                                                            |
| `given_name`               | The user's first name.                                                                                                           |
| `sub`                      | A unique identifying value for the member.                                                                                       |
| `id_token`                 | The ID token that LinkedIn provides to your application.                                                                         |
| `name`                     | The full name of the user.                                                                                                       |
| `picture`                  | A URL leading to the user's profile picture.                                                                                     |
| `refresh_token`            | The refresh token that LinkedIn provides to your application.&#xA;&#xA;LinkedIn only provides refresh tokens to select partners. |
| `refresh_token_expires_in` | The refresh token's expiration date.                                                                                             |
| `scope`                    | The OpenID scope used.                                                                                                           |

---

---
title: Deploying the integration files
description: To get started with the integration, deploy the LinkedIn Login Integration Kit files to your PingFederate directory.
component: linkedin
page_id: linkedin:setup:pf_linkedin_cic_deploying_the_integration_files
canonical_url: https://docs.pingidentity.com/integrations/linkedin/setup/pf_linkedin_cic_deploying_the_integration_files.html
llms_txt: https://docs.pingidentity.com/integrations/linkedin/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 17, 2025
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Deploying the integration files

To get started with the integration, deploy the LinkedIn Login Integration Kit files to your PingFederate directory.

## About this task

|   |                                                                                          |
| - | ---------------------------------------------------------------------------------------- |
|   | If you operate PingFederate in a cluster, the following steps refer to the console node. |

## Steps

1. Download the LinkedIn Login Integration Kit `.zip` archive from the [**Add-ons** tab on the PingFederate downloads page](https://www.pingidentity.com/en/resources/downloads/pingfederate.html) or the [Ping Identity Marketplace](https://marketplace.pingone.com/item/linkedin-login-integration-kit).

2. Stop PingFederate.

3. If you're upgrading an existing deployment, back up your customizations and delete earlier versions of the integration files:

   1. Back up any LinkedIn Login Integration Kit files that you customized in the `<pf_install>/pingfederate/server/default/conf/` directory.

   2. Delete the `pf-linkedin-adapter-<version>.jar` file from your `<pf_install>/pingfederate/server/default/deploy` directory.

4. Extract the `.zip` archive and merge the contents of the `dist` directory with your `<pf_install>/pingfederate` directory.

5. If there is more than one version of the `pf-authn-api-sdk-<version>.jar` file in your `<pf_install>/pingfederate/server/default/lib` directory, delete all but the latest version of the file.

6. If you backed up any customized files, modify the new files with your customizations.

7. Start PingFederate.

8. If you operate PingFederate in a cluster, repeat steps 2 - 8 for each engine node.

---

---
title: Download manifest
description: The following files are included in the LinkedIn Login Integration Kit .zip archive.
component: linkedin
page_id: linkedin:release_notes:pf_linkedin_cic_download_manifest
canonical_url: https://docs.pingidentity.com/integrations/linkedin/release_notes/pf_linkedin_cic_download_manifest.html
llms_txt: https://docs.pingidentity.com/integrations/linkedin/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: January 21, 2026
---

# Download manifest

The following files are included in the LinkedIn Login Integration Kit `.zip` archive.

* `ReadMeFirst.pdf`: Contains links to this online documentation.

* `legal/Legal.pdf`: Copyright and license information.

* `dist`: Contains the integration files.

  * `deploy`: Contains the Java libraries.

    * `pf-linkedin-adapter-<version>.jar`: JAR file that contains the LinkedIn IdP Adapter.

  * `conf`: Contains the HTML template that presents the LinkedIn sign-on form.

    * `language-packs`: Contains files with customizable user-facing messages.

      * `pingfederate-linkedin-adapter-messages.properties`: A variable file that customizes the messages that appear on the template files.

    * `template`: Contains user-facing HTML template files.

      * `linkedin-pop-up-template.html`: Template that opens a pop-up window to prompt the user to sign on.

      * `linkedin-post-auth-template.html`: Template that returns the user to the PingFederate sign-on flow after they sign on with LinkedIn.

      * `assets`: Contains functional scripts and files used by the template.

        * `css/linkedin.css`: CSS file that customizes the appearance of the template files.

        * `fonts/end-user`: Contains template fonts and icons.

          * `icons`: Contains template icons.

        * `images`: Contains template image files.

          * `ping-logo.svg`: An image file with company branding.

  * `lib/pf-authn-api-sdk-<version>.jar`: A JAR file that contains the PingFederate Authentication API SDK.

---

---
title: Enabling debug logging
description: To help with troubleshooting or monitoring, you can turn on activity logging for the adapter.
component: linkedin
page_id: linkedin:troubleshooting:pf_linkedin_cic_enabling_debug_logging
canonical_url: https://docs.pingidentity.com/integrations/linkedin/troubleshooting/pf_linkedin_cic_enabling_debug_logging.html
llms_txt: https://docs.pingidentity.com/integrations/linkedin/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 17, 2024
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

2. If you want to log activity for PingFederate and all adapters, do the following:

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

3. To log activity just for the LinkedIn IdP Adapter, add the following line:

   ```html
   <Logger name="com.pingidentity.adapter.idp.linkedin" level="DEBUG"/>
   ```

4. Save the file.

---

---
title: Integrating social sign-on into your application
description: To complete your LinkedIn sign-on integration, add a sign-on hyperlink to your application.
component: linkedin
page_id: linkedin:setup:pf_linkedin_cic_integrating_social_sign_on_into_your_application
canonical_url: https://docs.pingidentity.com/integrations/linkedin/setup/pf_linkedin_cic_integrating_social_sign_on_into_your_application.html
llms_txt: https://docs.pingidentity.com/integrations/linkedin/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 21, 2025
section_ids:
  steps: Steps
---

# Integrating social sign-on into your application

To complete your LinkedIn sign-on integration, add a sign-on hyperlink to your application.

## Steps

1. If your application is outside the PingFederate domain, configure an SP connection:

   1. Create a service provider (SP) connection to your application as shown in [SP connection management](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_sp_connect_management.html) in the PingFederate documentation.

      |   |                                                                                                                                                                                                                                                                      |
      | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      |   | Use the LinkedIn IdP Adapter instance as an authentication source. Learn more in [Mapping an adapter instance](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_mapping_adapter_instance.html) in the PingFederate documentation. |

   2. In your web application, create a hyperlink to allow users to sign on to the SP application. Use the following URL and replace the variables based on the descriptions in the following table:

      `https://<pf_host>:<pf_port>/idp/startSSO.ping?PartnerSpId=<ConnectionId>`

      | Variable          | Description                                                                                         |
      | ----------------- | --------------------------------------------------------------------------------------------------- |
      | *\<pf\_host>*     | The host name or IP address of the PingFederate server.                                             |
      | *\<pf\_port>*     | The port number for PingFederate.                                                                   |
      | *\<ConnectionId>* | The federation identifier of the SP for the connection that uses the LinkedIn IdP Adapter instance. |

2. If your application is inside the PingFederate domain, configure an adapter-to-adapter mapping:

   1. Create an SP connection to your application as shown in [SP connection management](http://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_sp_connect_management.html) in the PingFederate documentation.

      |   |                                                                                                                                                                                                                                                                     |
      | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      |   | Use the LinkedIn IdP Adapter instance as an authentication source. Learn more in [Mapping an adapter instance](http://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_mapping_adapter_instance.html) in the PingFederate documentation. |

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
      | *\<IdpAdapterId>* | The instance ID of the LinkedIn IdP Adapter instance.                                     |
      | *\<SpAdapterId>*  | The instance ID of the SP adapter instance that has been integrated with the application. |

---

---
title: JSON Pointer syntax reference
description: JSON Pointer defines a syntax for identifying a specific value within a JSON payload. Using the sample payload and JSON Pointer examples below, identify the attributes you want to populate your attribute contract with.
component: linkedin
page_id: linkedin:setup:pf_linkedin_cic_json_pointer_syntax_reference
canonical_url: https://docs.pingidentity.com/integrations/linkedin/setup/pf_linkedin_cic_json_pointer_syntax_reference.html
llms_txt: https://docs.pingidentity.com/integrations/linkedin/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 17, 2025
section_ids:
  example-json-payload: Example JSON payload
---

# JSON Pointer syntax reference

JSON Pointer defines a syntax for identifying a specific value within a JSON payload. Using the sample payload and JSON Pointer examples below, identify the attributes you want to populate your attribute contract with.

You can find more information in the following resources:

* You can find a complete technical description of JSON Pointer syntax in [IETF RFC 6901 - JavaScript Object Notation (JSON) Pointer](https://tools.ietf.org/html/rfc6901).

* Learn more about LinkedIn JSON payload structure in [Object Types](https://learn.microsoft.com/en-us/linkedin/shared/references/v2/object-types) in the LinkedIn API documentation.

## Example JSON payload

This example uses the `https://api.linkedin.com/v2/userinfo` user data API URL with the default `profile`, `openid`, and `email` permissions. You can find more information in the following resources:

* Learn more about the user data API in the **LinkedIn User Data v2 URL** table entry in [LinkedIn IdP Adapter settings](pf_linkedin_cic_linkedin_idp_adapter_settings.html).

* Learn more about the default permissions in the **Permissions** table entry in the [LinkedIn IdP Adapter settings](pf_linkedin_cic_linkedin_idp_adapter_settings.html).

```json
{
    "sub": "vaz8tJ1Aah",
    "email_verified": true,
    "name": "Example User",
    "locale": {
        "country": "US",
        "language": "en"
    },
    "given_name": "Example",
    "family_name": "User",
    "email": "user@example.com",
    "picture": "https://medialicdn.com/dms/image/v2/example_user"
}
```

**JSON Pointer Syntax**

| Description  | JSON Pointer      | Example value |
| ------------ | ----------------- | ------------- |
| `Given name` | `/given_name`     | `Example`     |
| `Country`    | `/locale/country` | `US`          |
| `User ID`    | `/sub`            | `vaz8tJ1Aah`  |

---

---
title: Known issues and limitations
description: There are no known issues.
component: linkedin
page_id: linkedin:release_notes:pf_linkedin_cic_known_issues_and_limitations
canonical_url: https://docs.pingidentity.com/integrations/linkedin/release_notes/pf_linkedin_cic_known_issues_and_limitations.html
llms_txt: https://docs.pingidentity.com/integrations/linkedin/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 17, 2025
section_ids:
  known-issues: Known issues
  known-limitations: Known limitations
---

# Known issues and limitations

## Known issues

There are no known issues.

## Known limitations

* LinkedIn doesn't support single logout (SLO).

---

---
title: LinkedIn IdP Adapter settings
description: Field descriptions for the LinkedIn IdP Adapter configuration page:
component: linkedin
page_id: linkedin:setup:pf_linkedin_cic_linkedin_idp_adapter_settings
canonical_url: https://docs.pingidentity.com/integrations/linkedin/setup/pf_linkedin_cic_linkedin_idp_adapter_settings.html
llms_txt: https://docs.pingidentity.com/integrations/linkedin/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 17, 2025
---

# LinkedIn IdP Adapter settings

Field descriptions for the LinkedIn IdP Adapter configuration page:

> **Collapse: Standard fields**
>
> | Field Name                    | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
> | ----------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
> | **Client ID**                 | The client ID that you noted in [Register PingFederate as a Microsoft Application](pf_linkedin_cic_register_pf_as_a_microsoft_application.html).This field is required.                                                                                                                                                                                                                                                                                                                                                                                                                   |
> | **Client Secret**             | The client secret that you noted in [Register PingFederate as a Microsoft Application](pf_linkedin_cic_register_pf_as_a_microsoft_application.html).This field is required.                                                                                                                                                                                                                                                                                                                                                                                                               |
> | **Permissions**               | The combined scopes of authority that PingFederate and the application want to request from the LinkedIn user.These permissions determine which LinkedIn attributes can be added in the **Attributes** section of the **IdP Adapter** tab.Use a space to separate multiple permissions.The default value is `profile openid email`.                                                                                                                                                                                                                                                       |
> | **Error Redirect URL**        | (Optional) The URL of a custom page that displays when PingFederate receives an error response from LinkedIn. This URL can contain query parameters. The URL has an `errorMessage` query parameter appended to it that contains a brief description of the error.If this field is blank, users will see a generic error page.Learn more about using custom pages in [Customizable user-facing pages](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_custom_user_facing_pages.html) in the PingFederate documentation.This field is blank by default. |
> | **Unauthorized Redirect URL** | (Optional) The URL of a custom page that displays when PingFederate receives a response from LinkedIn that says the user declined the authorization request. This URL can contain query parameters.If no URL is specified, users will see a default error page.Learn more about using custom pages in [Customizable user-facing pages](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_custom_user_facing_pages.html) in the PingFederate documentation.This field is blank by default.                                                               |
> | **Callback Endpoint**         | The PingFederate endpoint that LinkedIn uses to respond to authorization requests. If you set a custom endpoint in [Register PingFederate as a Microsoft Application](pf_linkedin_cic_register_pf_as_a_microsoft_application.html), change this field to match.This default value is `/linkedin-authn`.                                                                                                                                                                                                                                                                                   |

> **Collapse: Advanced fields**
>
> | Field Name                                                                                                            | Description                                                                                                                                                                                                                                                                                                                                                                                                               |
> | --------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
> | **PingFederate Base URL**                                                                                             | (Optional) The fully-qualified host name, port, and path (if applicable) of the PingFederate server. For example, `https://sso.example.com:9031`.This field affects the redirect URL set in the [Register PingFederate as a Microsoft Application](pf_linkedin_cic_register_pf_as_a_microsoft_application.html) step.If this override field is blank, the URL is determined automatically.This field is blank by default. |
> | **LinkedIn Authentication v2 URL**                                                                                    | The LinkedIn API endpoint that PingFederate uses to get the verification codes.The default value is `https://www.linkedin.com/oauth/v2/authorization`.                                                                                                                                                                                                                                                                    |
> | **LinkedIn Access Token v2 URL**                                                                                      | The LinkedIn API endpoint that PingFederate uses to get access tokens.The default value is `https://www.linkedin.com/oauth/v2/accessToken`.                                                                                                                                                                                                                                                                               |
> | **LinkedIn User Data v2 URL**                                                                                         | The LinkedIn API endpoint that PingFederate uses to get user attributes.The default value is `https://api.linkedin.com/v2/userinfo`.                                                                                                                                                                                                                                                                                      |
> | **LinkedIn Sign-On Presentation**                                                                                     | Determines how the user is directed to LinkedIn for authentication.&#xA;&#xA;Some browsers block automatic redirects.If you select **Pop-up window** and aren't using PingFederate in authentication API mode, the adapter presents a template file.                                                                                                                                                                      |
> | **LinkedIn Pop-up Template**&#xA;&#xA;Applies only when the LinkedIn Sign-On Presentation is set to Pop-up window.    | The template file that presents the LinkedIn sign-on form.The default value is `linkedin-pop-up-template.html`.                                                                                                                                                                                                                                                                                                           |
> | **LinkedIn Post Auth Template**&#xA;&#xA;Applies only when the LinkedIn Sign-On Presentation is set to Pop-up window. | The template file that the adapter presents after the user signs on.The default value is `linkedin-post-auth-template.html`.                                                                                                                                                                                                                                                                                              |
> | **LinkedIn Messages File**                                                                                            | The language-pack file associated with the **LinkedIn Pop-up Template**.The default value is `pingfederate-linkedin-adapter-messages`.                                                                                                                                                                                                                                                                                    |
> | **Retry Request**                                                                                                     | Determines whether PingFederate will retry requests after it receives a response with a failure code.This checkbox is selected by default.                                                                                                                                                                                                                                                                                |
> | **Maximum Retries Limit**                                                                                             | Determines how many times PingFederate will retry a request.The default value is `5`.                                                                                                                                                                                                                                                                                                                                     |
> | **Retry Error Codes**                                                                                                 | Determines which response codes are considered failures.The default value is `429`.                                                                                                                                                                                                                                                                                                                                       |
> | **API Request Timeout**                                                                                               | The amount of time in milliseconds that PingFederate allows when establishing a connection with LinkedIn or waiting for a response to a request. A value of `0` disables the timeout.The default value is `5000`.                                                                                                                                                                                                         |
> | **Proxy Settings**                                                                                                    | Defines proxy settings for outbound HTTP requests.The default value is **System Defaults**.                                                                                                                                                                                                                                                                                                                               |
> | **Custom Proxy Host**                                                                                                 | The proxy server host name to use when **Proxy Settings** is set to **Custom**.This field is blank by default.                                                                                                                                                                                                                                                                                                            |
> | **Custom Proxy Port**                                                                                                 | The proxy server port to use when **Proxy Settings** is set to **Custom**.This field is blank by default.                                                                                                                                                                                                                                                                                                                 |

---

---
title: LinkedIn Login Integration Kit
description: The LinkedIn Login Integration Kit allows PingFederate to use LinkedIn as an identity provider (IdP). This allows users to access service provider (SP) applications by signing into LinkedIn.
component: linkedin
page_id: linkedin::pf_linkedin_cic
canonical_url: https://docs.pingidentity.com/integrations/linkedin/pf_linkedin_cic.html
llms_txt: https://docs.pingidentity.com/integrations/linkedin/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 17, 2025
section_ids:
  features: Features
  components: Components
  intended-audience: Intended audience
  system-requirements: System requirements
---

# LinkedIn Login Integration Kit

The LinkedIn Login Integration Kit allows PingFederate to use LinkedIn as an identity provider (IdP). This allows users to access service provider (SP) applications by signing into LinkedIn.

## Features

* Supports the [PingFederate authentication API](https://docs.pingidentity.com/pingfederate/latest/developers_reference_guide/pf_authentication_api.html).

* Supports the [JavaScript Widget for the PingFederate Authentication API](https://github.com/pingidentity/pf-authn-js-widget).

## Components

LinkedIn IdP Adapter

* Allows PingFederate to communicate with the LinkedIn API to process sign-on requests and get user information.

Templates

* Allows the adapter to prompt the user to sign on. The template can be presented with a browser redirect or as a pop-up window.

* Allows you to modify the appearance of the sign-on prompt.

Language packs

* Allows you to customize or localize the messages returned by the PingFederate authentication API and shown on the templates during authentication. Learn more in [Localizing messages for end users](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_local_message_end_users.html) in the PingFederate documentation.

## Intended audience

This document is intended for PingFederate administrators.

If you need help during the setup process, you can find more information in the following resources:

* PingFederate documentation:

  * [Identity provider SSO configuration](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_ident_provid_sso_config.html)

  * [Managing IdP adapters](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_managing_idp_adapters.html)

  * [Authentication policies](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_authentication_policies.html)

  * [SP connection management](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_sp_connect_management.html)

* [Sign in with LinkedIn](https://docs.microsoft.com/en-us/linkedin/consumer/integrations/self-serve/sign-in-with-linkedin) in the Microsoft LinkedIn documentation.

## System requirements

* PingFederate 11.3

* A LinkedIn developer account

---

---
title: Overview of the SSO flow
description: With the LinkedIn Login Integration Kit, PingFederate includes the LinkedIn authentication API in the sign-on flow.
component: linkedin
page_id: linkedin::pf_linkedin_cic_overview_of_the_sso_flow
canonical_url: https://docs.pingidentity.com/integrations/linkedin/pf_linkedin_cic_overview_of_the_sso_flow.html
llms_txt: https://docs.pingidentity.com/integrations/linkedin/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 17, 2025
section_ids:
  description: Description
---

# Overview of the SSO flow

With the LinkedIn Login Integration Kit, PingFederate includes the LinkedIn authentication API in the sign-on flow.

The following figure illustrates a single sign-on (SSO) scenario in which PingFederate authenticates users to an SP application using the LinkedIn IdP Adapter.

A flowchart depicting the SSO flow between the browser and LinkedIn.

## Description

1. The user opens a web application and chooses the LinkedIn sign-on option.

2. The sign-on link points to the LinkedIn IdP Adapter, which redirects the browser…​

3. ..to LinkedIn with a list of requested permissions. On LinkedIn, the user authenticates their identity and then authorizes the requested permissions.

4. LinkedIn redirects the browser…​

5. …​to the LinkedIn IdP Adapter authorization callback endpoint with an authorization code.

   If the user fails to authenticate or does not authorize the request, the response includes an error code instead.

6. PingFederate sends LinkedIn the authorization code.

7. LinkedIn returns an access token.

8. PingFederate sends LinkedIn a request for user attributes, and presents the access token.

9. LinkedIn verifies the access token, and provides the user information.

10. PingFederate redirects the user to the web application with the user attributes.

---

---
title: Register PingFederate as a Microsoft Application
description: To allow PingFederate to process social sign-on requests with LinkedIn, add PingFederate as an OAuth application in the LinkedIn admin console.
component: linkedin
page_id: linkedin:setup:pf_linkedin_cic_register_pf_as_a_microsoft_application
canonical_url: https://docs.pingidentity.com/integrations/linkedin/setup/pf_linkedin_cic_register_pf_as_a_microsoft_application.html
llms_txt: https://docs.pingidentity.com/integrations/linkedin/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 17, 2025
section_ids:
  steps: Steps
---

# Register PingFederate as a Microsoft Application

To allow PingFederate to process social sign-on requests with LinkedIn, add PingFederate as an OAuth application in the LinkedIn admin console.

## Steps

1. Sign on to <https://developer.linkedin.com/> using a LinkedIn developer account.

2. Click **Create App**.

3. Complete the **Create an app** form, then click **Create app**.

4. Click the **Auth** tab.

5. In the **Application credentials** section, note the **Client ID** and **Client Secret**.

   You'll use these in [Configuring an adapter instance](pf_linkedin_cic_configuring_an_adapter_instance.html).

6. In the **OAuth 2.0 settings** section, click the **Edit** icon.

7. Enter the callback endpoint of the LinkedIn IdP Adapter, such as `https://pf.example.com:9031/ext/linkedin-authn`. Click **Update**.

   |   |                                                                                                                                                                                                                                                                                            |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
   |   | The default endpoint is `/linkedin-authn`. If you set a custom endpoint here, enter the matching value in the **Authorization Callback Endpoint** field of your adapter instance configuration in [Configuring an adapter instance](pf_linkedin_cic_configuring_an_adapter_instance.html). |

---

---
title: Troubleshooting
description: Description:
component: linkedin
page_id: linkedin:troubleshooting:pf_linkedin_cic_troubleshooting
canonical_url: https://docs.pingidentity.com/integrations/linkedin/troubleshooting/pf_linkedin_cic_troubleshooting.html
llms_txt: https://docs.pingidentity.com/integrations/linkedin/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 17, 2025
section_ids:
  pingfederate-cant-connect-to-the-linkedin-api: PingFederate can't connect to the LinkedIn API
  linkedin-presents-the-user-with-an-unauthorized-page: LinkedIn presents the user with an Unauthorized page
  all-sso-attempts-fail: All SSO attempts fail
  linkedin-does-not-return-values-for-some-requested-attributes: LinkedIn does not return values for some requested attributes
---

# Troubleshooting

## PingFederate can't connect to the LinkedIn API

Description:

* When [configuring an adapter instance](../setup/pf_linkedin_cic_configuring_an_adapter_instance.html), you receive an error when you click **Test Connection**.

Recommendation:

* Check the **Client ID** and **Client Secret** values for the PingFederate application that you registered on <https://developer.linkedin.com/>.

* Copy and paste the values directly into the adapter instance configuration. Run the test again.

## LinkedIn presents the user with an **Unauthorized** page

Description:

* LinkedIn presents the user with an **Unauthorized** page containing a link to an error page provided by the LinkedIn IdP Adapter instance.

Explanation:

* During authentication, the user declined to give authorization to LinkedIn. Ask the user to repeat the process and authorize LinkedIn.

|   |                                                                                                                                                                                                 |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | You can customize this error page. Learn more in the **Unauthorized Redirect URL** table entry in [LinkedIn IdP Adapter settings](../setup/pf_linkedin_cic_linkedin_idp_adapter_settings.html). |

## All SSO attempts fail

Description:

* For all users, attempting to sign on to an application through the LinkedIn IdP Adapter fails. The PingFederate server log includes the following error: "Attribute retrieval from LinkedIn failed".

Recommendation:

* Check whether you are using the correct LinkedIn API endpoint for the permissions that you have requested. In your adapter instance configuration, check that the following settings and fields are in agreement:

  * Permissions

  * LinkedIn User Data V2 URL

Learn more in [LinkedIn IdP Adapter settings](../setup/pf_linkedin_cic_linkedin_idp_adapter_settings.html).

## LinkedIn does not return values for some requested attributes

Description:

* After successful authentication and authorization, LinkedIn does not return values for some of the requested attributes.

Explanation:

* Some attributes require specific LinkedIn partner programs. Learn more in [Frequently Asked Questions](https://developer.linkedin.com/support/faq) in the LinkedIn developer documentation.

---

---
title: Upgrading an existing deployment
description: If you're upgrading from a previous version of the LinkedIn Login Integration Kit, you might need to take extra steps.
component: linkedin
page_id: linkedin:setup:pf_linkedin_cic_upgrading_an_existing_deployment
canonical_url: https://docs.pingidentity.com/integrations/linkedin/setup/pf_linkedin_cic_upgrading_an_existing_deployment.html
llms_txt: https://docs.pingidentity.com/integrations/linkedin/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 22, 2025
section_ids:
  steps: Steps
---

# Upgrading an existing deployment

If you're upgrading from a previous version of the LinkedIn Login Integration Kit, you might need to take extra steps.

## Steps

1. Back up your current PingFederate configuration as shown in [Configuration archive](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_configurationarchivetasklet_selectimportexportstate.html) in the PingFederate documentation.

2. If you're upgrading from LinkedIn IdP Adapter 2.2 or earlier:

   1. Note your adapter instance configuration.

   2. Delete the adapter instance.

   3. Complete the steps in [Deploying the integration files](pf_linkedin_cic_deploying_the_integration_files.html).

   4. Complete the steps in [Configuring an adapter instance](pf_linkedin_cic_configuring_an_adapter_instance.html). Configure the adapter instance settings based on your notes, making the following changes:

   |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
   | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | * Update the **LinkedIn User Data v2 URL** field

     * Related Change: The `https://api.linkedin.com/v2/me` API endpoint that the LinkedIn IdP Adapter used to retrieve user information in LinkedIn Login Integration Kit 2.2 and earlier is now unavailable.

     * Required Action: When you upgrade the LinkedIn IdP Adapter, make sure the **LinkedIn User Data v2 URL** field contains the new API URL, `https://api.linkedin.com/v2/userinfo`. Learn more in [LinkedIn IdP Adapter settings](pf_linkedin_cic_linkedin_idp_adapter_settings.html).

   * Update the **Permissions** field

     * Related Change: The API endpoint that the LinkedIn IdP Adapter used to retrieve email addresses is now unavailable. As a result, LinkedIn Login Integration Kit 3.0 has deprecated the **LinkedIn User Email V2 URL** field and the `r_emailadress`, `r_liteprofile`, and `r_fullprofile` permissions.

     * Required Action: Make sure the **Permissions** field contains the new default permissions, `profile`, `openid`, and `email`. Learn more in [LinkedIn IdP Adapter settings](pf_linkedin_cic_linkedin_idp_adapter_settings.html).

       Additionally, you can find a sample user information payload using the new API URL and permissions in [JSON Pointer syntax reference](pf_linkedin_cic_json_pointer_syntax_reference.html).

   * Check Optional LinkedIn Attributes

     * Related Change: If you mapped any attributes in the **Optional LinkedIn Attributes** section when configuring an adapter instance, your configuration might be broken or no longer relevant.

     * Required Action: Review your adapter configuration and fix any errors reported during the connection test. Learn more in [Configuring an adapter instance](pf_linkedin_cic_configuring_an_adapter_instance.html).

   * Update any configurations using the `id` core contract attribute

     * Related Change: LinkedIn Login Integration Kit 3.0 has replaced the `id` core contract attribute with the `sub` core contract attribute to align with the response body schema described in [Sign In with LinkedIn using OpenID Connect](https://learn.microsoft.com/en-us/linkedin/consumer/integrations/self-serve/sign-in-with-linkedin-v2).

     * Required Action: Review your authentication policy and connection configuration. Change all instances of `id` to `sub`. Learn more in [Core contract attributes](pf_linkedin_cic_core_contract_attributes.html). |