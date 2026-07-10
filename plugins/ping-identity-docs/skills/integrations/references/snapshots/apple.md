---
title: Apple IdP Adapter settings reference
description: Field descriptions for the Apple IdP Adapter configuration screen.
component: apple
page_id: apple:setup:pf_apple_cic_apple_idp_adapter_settings_reference
canonical_url: https://docs.pingidentity.com/integrations/apple/setup/pf_apple_cic_apple_idp_adapter_settings_reference.html
llms_txt: https://docs.pingidentity.com/integrations/apple/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 1, 2024
---

# Apple IdP Adapter settings reference

Field descriptions for the Apple IdP Adapter configuration screen.

**Standard fields**

| Field                               | Description                                                                                                                                                                                                                                                                                                  |
| ----------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Team ID**                         | The **Team ID** that you noted in [Registering an Apple app](pf_apple_cic_registering_an_apple_app.html).This is used as `iss` in the client secret.                                                                                                                                                         |
| **Services ID**                     | The **Identifier** that you registered in [Registering an Apple service](pf_apple_cic_registering_an_apple_service.html).This is used as the `client_id` when the adapter requests access and refresh tokens. It is also used as `sub` when the adapter creates the client secret JWT.                       |
| **Key ID**                          | The **Key ID** that you noted in [Creating an Apple private key](pf_apple_cic_creating_an_apple_private_key.html).This is used as `kid` in the client secret.                                                                                                                                                |
| **Client Secret Signing Key**       | The private key `.p8` file that you downloaded in [Creating an Apple private key](pf_apple_cic_creating_an_apple_private_key.html).PingFederate encrypts this file when you add it to your configuration.                                                                                                    |
| **Error Redirect URL**              | When an error occurs in the adapter, PingFederate redirects the browser to this URL instead of the default error page.This field is blank by default.                                                                                                                                                        |
| **Authorization Callback Endpoint** | The PingFederate endpoint that Apple uses to respond to authorization requests. If you set a custom endpoint in the **Authorization callback URL** field in [Registering an Apple service](pf_apple_cic_registering_an_apple_service.html), change this field to match.This default value is `/apple-authn`. |

**Advanced fields**

| Field                          | Description                                                                                                                                                                                                                                                                                                                                                                                                                          |
| ------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Apple Authorization URL**    | The URL that PingFederate uses to send authorization requests to Apple. If Apple changes this endpoint, enter the new URL.The default value is `https://appleid.apple.com/auth/authorize`.                                                                                                                                                                                                                                           |
| **Apple Access Token URL**     | The URL that PingFederate uses to retrieve access tokens from Apple. If Apple changes this endpoint, enter the new URL.The default value is `https://appleid.apple.com/auth/token`.                                                                                                                                                                                                                                                  |
| **Apple ID URL**               | The URL that PingFederate uses to communicate with Apple ID.The default value is `https://appleid.apple.com`.                                                                                                                                                                                                                                                                                                                        |
| **Apple Public Key URL**       | The URL that PingFederate uses to retrieve the Apple public key.The default value is `https://appleid.apple.com/auth/keys`.                                                                                                                                                                                                                                                                                                          |
| **Client Secret Expiration**   | The amount of time in minutes that the client secret is valid. Enter a value between 1 and 262950 (6 months).The default value is `5`.                                                                                                                                                                                                                                                                                               |
| **Scopes**                     | The scopes that you want to request from Apple. Separate scopes with a space. See the note about scopes in [Known issues and limitations](../release_notes/pf_apple_cic_known_issues_and_limitations.html).Valid scopes include `openid`, `email`, and `name`.The default value is `openid email name`.                                                                                                                              |
| **Apple Sign-On Presentation** | Determines how the adapter presents the Apple sign-on form.- Redirect (default)

  The adapter redirects the browser to the Apple sign-on form.

- Pop-up window

  The adapter opens a new window with the Apple sign-on form on a PingFederate template. Use this option if automatic redirects are blocked by your users' browsers.This setting has no effect when using the adapter through the PingFederate authentication API. |
| **Apple Pop-Up Template**      | The template file that presents the Apple sign-on form. Applies only when **Apple Login Presentation** is set to **Pop-up window**.The default value is `apple-pop-up-template.html`.                                                                                                                                                                                                                                                |
| **Apple Post-Auth Template**   | The template file that the adapter presents after the user signs on. Applies only when **Apple Login Presentation** is set to **Pop-up window**.The default value is `apple-post-auth-template.html`.                                                                                                                                                                                                                                |
| **Apple Messages File**        | The language-pack file associated with the Apple pop-up template.The default value is `pingfederate-apple-adapter-messages`.                                                                                                                                                                                                                                                                                                         |
| **Retry Request**              | Determines whether PingFederate will retry requests after it receives a response with a failure code.This check box is cleared by default.                                                                                                                                                                                                                                                                                           |
| **Maximum Retries Limit**      | Determines how many times PingFederate retries a request.The default value is `5`.                                                                                                                                                                                                                                                                                                                                                   |
| **Retry Error Codes**          | A list of response codes that you want to trigger a retry. Separate response codes with a comma.The default value is `400`.                                                                                                                                                                                                                                                                                                          |
| **API Request Timeout**        | The amount of time in milliseconds that PingFederate waits for Apple to respond to requests. A value of `0` disables the timeout.The default value is `2000`.                                                                                                                                                                                                                                                                        |
| **Connection Timeout**         | The amount of time in milliseconds that PingFederate allows to establish a connection with Apple. A value of 0 disables the timeout.The default value is `2000`.                                                                                                                                                                                                                                                                     |
| **Proxy Settings**             | Defines proxy settings for outbound HTTP requests.The default value is **System Defaults**.                                                                                                                                                                                                                                                                                                                                          |
| **Custom Proxy Host**          | The proxy server host name to use when **Proxy Settings** is set to **Custom**.This field is blank by default.                                                                                                                                                                                                                                                                                                                       |
| **Custom Proxy Port**          | The proxy server port to use when **Proxy Settings** is set to **Custom**.This field is blank by default.                                                                                                                                                                                                                                                                                                                            |

---

---
title: Apple Login Integration Kit
description: The Apple Login Integration Kit allows PingFederate to use Apple as an identity provider (IdP). This allows users to access service provider (SP) applications by signing in with their Apple ID.
component: apple
page_id: apple::pf_apple_cic
canonical_url: https://docs.pingidentity.com/integrations/apple/pf_apple_cic.html
llms_txt: https://docs.pingidentity.com/integrations/apple/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 28, 2024
section_ids:
  section_N10039_N10036_N10001: Features
  section_xnk_szc_4jb: Components
  section_yjm_tzc_4jb: Intended audience
  section_i5t_tzc_4jb: System requirements
---

# Apple Login Integration Kit

The Apple Login Integration Kit allows PingFederate to use Apple as an identity provider (IdP). This allows users to access service provider (SP) applications by signing in with their Apple ID.

## Features

* Supports the PingFederate [PingFederate authentication API](https://docs.pingidentity.com/pingfederate/latest/developers_reference_guide/pf_authentication_api.html).

* Supports the [JavaScript Widget for the PingFederate Authentication API](https://github.com/pingidentity/pf-authn-js-widget).

## Components

Apple IdP Adapter

* Allows PingFederate to communicate with the Apple API to process sign-on requests and get user information.

Templates

* Allows the adapter to prompt the user to sign on. The template can be presented with a browser redirect or as a pop-up window.

* Allows you to modify the appearance of the sign-on prompt.

Language packs

* Allows you to customize or localize the messages returned by the PingFederate authentication API and shown on the templates during authentication. For help, see [Localizing messages for end users](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_local_message_end_users.html) in the PingFederate documentation.

## Intended audience

This document is intended for PingFederate administrators.

If you need help during the setup process, learn more in the following resources:

* The following sections of the PingFederate documentation:

  * [Identity provider SSO configuration](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_ident_provid_sso_config.html)

  * [Managing IdP adapters](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_managing_idp_adapters.html)

  * [Authentication policies](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_authentication_policies.html)

  * [SP connection management](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_sp_connect_management.html)

- The following sections of the Apple developer documentation:

  * [About Sign in with Apple](https://help.apple.com/developer-account/?lang=en#/devde676e696)

  * [Sign in with Apple Overview](https://developer.apple.com/sign-in-with-apple/)

  * [Sign in with Apple REST API](https://developer.apple.com/documentation/sign_in_with_apple/sign_in_with_apple_rest_api)

## System requirements

* PingFederate 10.3 or later.

* An Apple Developer account. To sign up, visit [What You Need To Enroll](https://developer.apple.com/programs/enroll/) on the Apple Developer Program site.

* End users must have two-factor authentication set up to use Sign in with Apple.

---

---
title: Authentication API Support
description: You can use the PingFederate authentication API to integrate the Apple IdP Adapter into your application.
component: apple
page_id: apple::pf_apple_cic_authentication_api_support
canonical_url: https://docs.pingidentity.com/integrations/apple/pf_apple_cic_authentication_api_support.html
llms_txt: https://docs.pingidentity.com/integrations/apple/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 28, 2024
---

# Authentication API Support

You can use the PingFederate authentication API to integrate the Apple IdP Adapter into your application.

The PingFederate Authentication API provides access to the current state of the authentication flow as a user steps through the PingFederate authentication policy. For more information, see [PingFederate authentication API](https://docs.pingidentity.com/pingfederate/latest/developers_reference_guide/pf_authentication_api.html) in the PingFederate documentation. To integrate the Apple IdP Adapter into your authentication flow, configure your application based on the states, actions, and models available in the PingFederate Authentication API Explorer. For help, see [Exploring the Authentication API](https://docs.pingidentity.com/pingfederate/latest/developers_reference_guide/pf_exploring_authentication_api.html) in the PingFederate documentation.

---

---
title: Available user attributes
description: Lists the attributes supported by Sign in with Apple.
component: apple
page_id: apple:setup:pf_apple_cic_available_user_attributes
canonical_url: https://docs.pingidentity.com/integrations/apple/setup/pf_apple_cic_available_user_attributes.html
llms_txt: https://docs.pingidentity.com/integrations/apple/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 1, 2024
---

# Available user attributes

Lists the attributes supported by Sign in with Apple.

For more details about the following attributes, see [Retrieving the User's Information from Apple ID Servers](https://developer.apple.com/documentation/signinwithapplerestapi/authenticating_users_with_sign_in_with_apple) in the Apple Developer documentation.

For the `email`, `first_name`, and `lastname` attributes, see the note about scopes in [Known issues and limitations](../release_notes/pf_apple_cic_known_issues_and_limitations.html).

| Attribute        | Description                                                                                                                                                                     |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `iss`            | The issuer-registered claim key, which has the value https\://appleid.apple.com.                                                                                                |
| `user_id`        | The unique identifier for the user. This is Apple's primary identifier for the user.                                                                                            |
| `aud`            | The **client\_id** for your Apple Developer account.                                                                                                                            |
| `email`          | The user's email address. The user may choose to share their real email address or an anonymous one that uses the private email relay service.Available with the `email` scope. |
| `email_verified` | A Boolean value that indicates whether the service has verified the email. The value of this claim is always true because the servers only return verified email addresses.     |
| `access_token`   | The access token provided by Apple.                                                                                                                                             |
| `first_name`     | The user's first name.Available with the `name` scope.                                                                                                                          |
| `last_name`      | The user's last name.Available with the `name` scope.                                                                                                                           |

---

---
title: Changelog
description: The following is the change history for the Apple Login Integration Kit.
component: apple
page_id: apple:release_notes:pf_apple_cic_changelog
canonical_url: https://docs.pingidentity.com/integrations/apple/release_notes/pf_apple_cic_changelog.html
llms_txt: https://docs.pingidentity.com/integrations/apple/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 28, 2024
section_ids:
  section_brq_1ns_k1c: Apple Cloud Identity Connector 1.1.2 – February 2024
  section_N1001D_N1001A_N10001: Apple Cloud Identity Connector 1.1.1 – September 2021
  section_akd_dqg_1rb: Apple Cloud Identity Connector 1.1 – November 2020
  section_onj_cqg_1rb: Apple Cloud Identity Connector 1.0.1 – December 2019
  section_vnt_bqg_1rb: Apple Cloud Identity Connector 1.0 – November 2019
---

# Changelog

The following is the change history for the Apple Login Integration Kit.

## Apple Cloud Identity Connector 1.1.2 – February 2024

* Fixed an issue that caused `email_verified` data to be handled incorrectly.

## Apple Cloud Identity Connector 1.1.1 – September 2021

* Fixed an issue that could cause the incorrect first and last name to be returned when a user signed on with Apple.

## Apple Cloud Identity Connector 1.1 – November 2020

* Added a setting to use browser redirect or pop-up window for the sign-on presentation.

* Added customizable sign-on templates for the pop-up window presentation.

* Added customizable user-facing language-pack messages.

* Added support for the [PingFederate authentication API](https://docs.pingidentity.com/pingfederate/latest/developers_reference_guide/pf_authentication_api.html).

* Added support for the [JavaScript Widget for the PingFederate Authentication API](https://github.com/pingidentity/pf-authn-js-widget).

## Apple Cloud Identity Connector 1.0.1 – December 2019

* Added a workflow to serve the Apple domain verification file directly through PingFederate. (Note: Domain verification is no longer needed as of July 2020, and has been removed from the documentation.)

## Apple Cloud Identity Connector 1.0 – November 2019

* Initial release.

* Added support for social login using Apple credentials.

* Added support for retrieving Apple user information, email, and name.

* Added the ability to override Apple API endpoints.

* Added the ability to customize the error redirect URL.

* Added the ability to configure when to retry a failed request.

* Added the ability to configure the maximum amount of retries to perform.

* Added the ability to override the system-default proxy settings.

* Added the ability to configure API connection timeout settings.

---

---
title: Configuring an adapter instance
description: Configure the Apple IdP Adapter to determine how PingFederate communicates with Apple Apple.
component: apple
page_id: apple:setup:pf_apple_cic_configuring_an_adapter_instance
canonical_url: https://docs.pingidentity.com/integrations/apple/setup/pf_apple_cic_configuring_an_adapter_instance.html
llms_txt: https://docs.pingidentity.com/integrations/apple/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 28, 2024
section_ids:
  steps: Steps
---

# Configuring an adapter instance

Configure the Apple IdP Adapter to determine how PingFederate communicates with Apple Apple.

## Steps

1. In the PingFederate administrative console, go to **Identity Provider > Adapters**. Click **Create New Instance**.

2. On the **Type** tab, set the basic adapter instance attributes.

   1. In the **Instance Name** field, enter a name for the adapter instance.

   2. In the **Instance ID** field, enter a unique identifier for the adapter instance.

   3. From the **Type** list, select **Apple IdP Adapter**. Click **Next**.

3. On the **IdP Adapter** tab, configure the adapter instance by referring to [Apple IdP Adapter settings reference](pf_apple_cic_apple_idp_adapter_settings_reference.html). Click **Next**.

4. On the **Extended Contract** tab, add any **Local Attributes** that you added in the **Apple Response Mappings** table. Click **Next**.

5. On the **Adapter Attributes** tab, set pseudonym and masking options as shown in [Set pseudonym and masking options](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_setting_pseudonym_masking_options.html) in the PingFederate documentation. Click **Next**.

6. On the **Adapter Contract Mapping** tab, configure the contract fulfillment details for the adapter as shown in [Define the IdP adapter contract](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_authnadapterinstancetasklet_plugincontractstate.html) in the PingFederate documentation. Click **Next**.

7. On the **Summary** tab, click **Done**. On the **Manage IdP Adapter Instances** tab, click **Save**.

---

---
title: Creating an Apple private key
description: To allow PingFederate to process social sign-on requests with Apple, add PingFederate as an OpenID Connect application in the Apple administrative console. PingFederate uses the resulting private key to sign the client secret JWT that it sends to Apple.
component: apple
page_id: apple:setup:pf_apple_cic_creating_an_apple_private_key
canonical_url: https://docs.pingidentity.com/integrations/apple/setup/pf_apple_cic_creating_an_apple_private_key.html
llms_txt: https://docs.pingidentity.com/integrations/apple/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 28, 2024
section_ids:
  steps: Steps
---

# Creating an Apple private key

To allow PingFederate to process social sign-on requests with Apple, add PingFederate as an OpenID Connect application in the Apple administrative console. PingFederate uses the resulting private key to sign the client secret JWT that it sends to Apple.

## Steps

1. Sign on to the Apple [Certificates, Identifiers & Profiles](https://developer.apple.com/account/resources/identifiers/list) page using an Apple Developer administrator account.

2. On the **Keys** page, next to the **Keys** heading, click **Add (+)**.

3. On the **Register a New Key** page, in the **Key Name** field, enter a name, such as `My PingFederate Client Secret Signing Key`.

4. Select **Sign in with Apple**. Click **Configure**.

5. On the **Configure Key** page, from the **Choose a Primary App ID** list, select the app that you registered in [Registering an Apple app](pf_apple_cic_registering_an_apple_app.html). Click **Save**.

6. On the **Register a New Key** page, click **Continue**.

7. Verify your configuration, and then click **Register**.

8. On the **Download Your Key** page, note the **Key ID**. You will use this in [Configuring an adapter instance](pf_apple_cic_configuring_an_adapter_instance.html).

9. Click **Download**, and then save the `.p8` file. You will use this in [Configuring an adapter instance](pf_apple_cic_configuring_an_adapter_instance.html). Click **Done**.

   |   |                                                                         |
   | - | ----------------------------------------------------------------------- |
   |   | You can only download your private key once. Keep it in a secure place. |

---

---
title: Deploying the integration files
description: To get started with the integration, deploy the Apple Login Integration Kit files to your PingFederate directory.
component: apple
page_id: apple:setup:pf_apple_cic_deploying_the_integration_files
canonical_url: https://docs.pingidentity.com/integrations/apple/setup/pf_apple_cic_deploying_the_integration_files.html
llms_txt: https://docs.pingidentity.com/integrations/apple/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 28, 2024
section_ids:
  context_w741ab1b7b1_w742ab1b7_w743ab1: About this task
  steps: Steps
---

# Deploying the integration files

To get started with the integration, deploy the Apple Login Integration Kit files to your PingFederate directory.

## About this task

|   |                                                                                          |
| - | ---------------------------------------------------------------------------------------- |
|   | If you operate PingFederate in a cluster, the following steps refer to the console node. |

## Steps

1. Download the Apple Login Integration Kit `.zip` archive from the [**Add-ons** tab of the PingFederate downloads page](https://www.pingidentity.com/en/resources/downloads/pingfederate.html) or the [Ping Identity Marketplace](https://marketplace.pingone.com/item/apple-login-integration-kit).

2. Stop PingFederate.

3. If you're upgrading an existing deployment, back up your customizations and delete earlier versions of the integration files:

   1. Back up any Apple Login Integration Kit files that you customized in the `<pf_install>/pingfederate/server/default/conf/` directory.

   2. Delete the `pf-apple-idp-adapter-<version>.jar` file from your `<pf_install>/pingfederate/server/default/deploy` directory.

4. Extract the `.zip` archive and merge the contents of the `dist` directory with your `<pf_install>/pingfederate` directory.

5. If there is more than one version of the `pf-authn-api-sdk-<version>.jar` file in your `<pf_install>/pingfederate/server/default/lib` directory, delete all but the latest version of the file.

6. If you backed up any customized files, modify the new files with your customizations.

7. Start PingFederate.

8. If you operate PingFederate in a cluster, repeat steps 2-8 for each engine node.

---

---
title: Download manifest
description: The following files are included in the Apple Login Integration Kit .zip archive:
component: apple
page_id: apple:release_notes:pf_apple_cic_download_manifest
canonical_url: https://docs.pingidentity.com/integrations/apple/release_notes/pf_apple_cic_download_manifest.html
llms_txt: https://docs.pingidentity.com/integrations/apple/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 28, 2024
---

# Download manifest

The following files are included in the Apple Login Integration Kit `.zip` archive:

* `legal/Legal.pdf`: Copyright and license information.

* `dist/pingfederate/server/default`: Contains the integration files

  * `deploy`: Contains the Java libraries

    * `pf-apple-idp-adapter-<version>.jar`: A `.jar` file that contains the Apple IdP Adapter.

  * `conf`: Contains the HTML template that presents the Apple sign-on form.

    * `language-packs/apple-messages.properties`: A variable file that provides adapter-specific template messages

      * `pingfederate-apple-adapter-messages.properties`: A variable file that customizes the messages that appear on the template files.

    * `template`: Contains user-facing HTML template files

      * `apple-pop-up-template.html`: A template that opens a pop-up window to prompt the user to sign on.

      * `apple-post-auth-template.html`: A template that returns the user to the PingFederate sign-on flow after they sign on with Apple.

      * `assets` – contains functional scripts and files used by the template

        * `css/apple.css`: A CSS file that customizes the appearance of the template files.

        * `fonts/end-user`: Contains template fonts and icons

          * `icons`: Contains template icons

        * `images`: Contains template image files

          * `ping-logo.svg`: An image file with company branding

  * `lib/pf-authn-api-sdk-<version>.jar`: A `.jar` file that contains the PingFederate Authentication API SDK

---

---
title: Enabling debug logging
description: To help with troubleshooting or monitoring, you can turn on activity logging for the adapter.
component: apple
page_id: apple:troubleshooting:pf_apple_cic_enabling_debug_logging
canonical_url: https://docs.pingidentity.com/integrations/apple/troubleshooting/pf_apple_cic_enabling_debug_logging.html
llms_txt: https://docs.pingidentity.com/integrations/apple/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 28, 2024
section_ids:
  context_w734ab1b7b1_w735ab1b7_w736ab1: About this task
  steps: Steps
---

# Enabling debug logging

To help with troubleshooting or monitoring, you can turn on activity logging for the adapter.

## About this task

These steps are optional. You can find general information about logging in [Enabling debug messages and console logging](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_enabling_debug_message_and_console_logging.html) in the PingFederate documentation.

## Steps

1. Open the `<pf_install>/pingfederate/server/default/conf/log4j2.xml` file for editing.

2. If you want to log activity for PingFederate and all adapters:

   1. Find the following section.

      ```html
      <AsyncRoot level="INFO" includeLocation="false">
      	<!-- <AppenderRef ref="CONSOLE" /> -->
      	<AppenderRef ref="FILE" />
      </AsyncRoot>
      ```

   2. Change `INFO` to `DEBUG`.

      ```html
      <AsyncRoot level="DEBUG" includeLocation="false">
      	<!-- <AppenderRef ref="CONSOLE" /> -->
      	<AppenderRef ref="FILE" />
      </AsyncRoot>
      ```

   3. If you want to see the adapter activity in the console, remove the comment tags.

      ```html
      <AsyncRoot level="INFO" includeLocation="false">
      	<AppenderRef ref="CONSOLE" />
      	<AppenderRef ref="FILE" />
      </AsyncRoot>
      ```

3. If you want to log activity just for the Apple IdP Adapter, add the following line.

   ```html
   <Logger name="com.pingidentity.adapter.idp.apple" level="DEBUG"/>
   ```

4. Save the file.

---

---
title: Integrating Sign in with Apple into your application
description: To complete your Sign in with Apple integration, create an SP connection or adapter mapping and then add a sign-on hyperlink to your application.
component: apple
page_id: apple:setup:pf_apple_cic_integrating_sign_in_with_apple_into_your_application
canonical_url: https://docs.pingidentity.com/integrations/apple/setup/pf_apple_cic_integrating_sign_in_with_apple_into_your_application.html
llms_txt: https://docs.pingidentity.com/integrations/apple/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 28, 2024
section_ids:
  steps: Steps
---

# Integrating Sign in with Apple into your application

To complete your Sign in with Apple integration, create an SP connection or adapter mapping and then add a sign-on hyperlink to your application.

## Steps

1. If your application is outside the PingFederate domain, configure a service provider (SP) connection.

   1. Create an SP connection that uses your IdP adapter instance as shown in [SP connection management](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_sp_connect_management.html) and [Mapping an adapter instance](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_mapping_adapter_instance.html) in the PingFederate documentation.

   2. In your web application, create a hyperlink to allow users to sign on to the SP application. Use the following URL and replace the variables based on the descriptions in the following table.

      https\://*pf\_host*:*pf\_port*/idp/startSSO.ping?PartnerSpId=*ConnectionId*

      | Variable          | Description                                                                                      |
      | ----------------- | ------------------------------------------------------------------------------------------------ |
      | *\<pf\_host>*     | The host name or IP address of the PingFederate server.                                          |
      | *\<pf\_port>*     | The port number for PingFederate.                                                                |
      | *\<ConnectionId>* | The federation identifier of the SP for the connection that uses the Apple IdP Adapter instance. |

   3. Brand your link with a **Sign in with Apple** button. For instructions, see [Sign in with Apple Buttons](https://developer.apple.com/design/human-interface-guidelines/sign-in-with-apple/overview/buttons/) in the Apple Developer documentation.

2. If your application is inside the PingFederate domain, configure an adapter-to-adapter mapping.

   1. On the **System > Protocol Settings > Roles & Protocols** tab, select the **Enable Identity Provider (IdP) role and support for the following** and **Enable Service Provider (SP) role and support for the following** check boxes.

   2. In both the **Enable Identity Provider** and **Enable Service Provider** sections, select any protocol check box, such as **SAML 2.0**. Click **Save**.

      |   |                                                                                                                                  |
      | - | -------------------------------------------------------------------------------------------------------------------------------- |
      |   | PingFederate requires a protocol selection to activate the roles. The protocol that you select is not used for this integration. |

   3. On the **Service Provider > Adapters** tab, create or select an adapter instance that is integrated with the application as shown in [SP application integration settings](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_sp_applicat_integra_settings.html) in the PingFederate documentation.

   4. On the **Identity Provider > Adapter-to-Adapter Mappings** tab, configure the IdP-to-SP adapter mapping as shown in [Adapter-to-adapter mappings](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_adaptertoadapter_mappings.html) in the PingFederate documentation.

   5. In your web application, create a hyperlink to allow users to sign on to the SP application. Use the following URL and replace the variables based on the descriptions in the table below:

      https\://*pf\_host*:*pf\_port*/pf/adapter2adapter.ping?IdpAdapterId=*IdpAdapterId*\&SpSessionAuthnAdapterId=*SpAdapterId*

      | Variable          | Description                                                                               |
      | ----------------- | ----------------------------------------------------------------------------------------- |
      | *\<pf\_host>*     | The host name or IP address of the PingFederate server.                                   |
      | *\<pf\_port>*     | The port number for PingFederate.                                                         |
      | *\<IdpAdapterId>* | The instance ID of the Apple IdP Adapter instance.                                        |
      | *\<SpAdapterId>*  | The instance ID of the SP adapter instance that has been integrated with the application. |

   6. Brand your link with a **Sign in with Apple** button. For instructions, see [Sign in with Apple Buttons](https://developer.apple.com/design/human-interface-guidelines/sign-in-with-apple/overview/buttons/) in the Apple Developer documentation.

---

---
title: Known issues and limitations
description: The following are known issues or limitations for the Apple Cloud Identity Connector.
component: apple
page_id: apple:release_notes:pf_apple_cic_known_issues_and_limitations
canonical_url: https://docs.pingidentity.com/integrations/apple/release_notes/pf_apple_cic_known_issues_and_limitations.html
llms_txt: https://docs.pingidentity.com/integrations/apple/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 28, 2024
section_ids:
  section_xnp_ccn_w3b: Known issues
  section_zxl_dcn_w3b: Known limitations
---

# Known issues and limitations

The following are known issues or limitations for the Apple Cloud Identity Connector.

## Known issues

There are no known issues.

## Known limitations

* Sign in with Apple ID does not create a session in the browser, so sign in is required every time and there is no single logout function.

* Apple handles scope requests in a unique way:

  * The `email` scope behaves as follows:

    * If you request this scope the first time a user signs on, Apple will return the email address. If you then request this scope at a later time, Apple will return the email address.

    * If you do not request this scope the first time a user signs on, Apple will not return the email address. If you then request this scope at a later time, Apple will not return the email address.

  * The `name` scope behaves as follows:

    * If you request this scope the first time a user signs on, Apple will return the name. If you then request this scope at a later time, Apple will not return the name.

    * If you do not request this scope the first time a user signs on, Apple will not return the name. If you then request this scope at a later time, Apple will not return the name.

  * If you need these attributes, have your application capture and store the values.

  * To reset these scenarios, the user has to manually revoke permissions from your application and then sign in again.

---

---
title: Overview of the SSO flow
description: With the Apple Cloud Identity Connector, PingFederate includes an Apple authentication API in the sign-on flow.
component: apple
page_id: apple::pf_apple_cic_overview_of_the_sso_flow
canonical_url: https://docs.pingidentity.com/integrations/apple/pf_apple_cic_overview_of_the_sso_flow.html
llms_txt: https://docs.pingidentity.com/integrations/apple/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 28, 2024
section_ids:
  section_N1006C_N10024_N10001: Description
---

# Overview of the SSO flow

With the Apple Cloud Identity Connector, PingFederate includes an Apple authentication API in the sign-on flow.

The following figure illustrates a service provider (SP)-initiated single sign-on (SSO) scenario in which PingFederate authenticates users to an SP application using the Apple IdP Adapter.

![dpj1573071410609](_images/dpj1573071410609.png)

## Description

1. The user opens a web application and chooses the **Sign in with Apple** option.

2. The sign-on link points to the PingFederate Apple IdP Adapter, which redirects the browser…​

3. …​to Apple with the client ID and a list of requested scopes. On the Apple site, the user authenticates their identity and then authorizes the requested scopes.

4. Apple redirects the browser…​

5. …​to the PingFederate Apple IdP Adapter authorization callback endpoint with an authorization code.

   If the user fails to authenticate or does not authorize the request, the response includes an error code instead.

6. The Apple IdP Adapter generates a client secret JSON object. PingFederate sends the client secret, client ID, and nonce value to Apple.

   |   |                                                                                                                                                                                                                               |
   | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | For more about the client secret object, see [Creating the Client Secret](https://developer.apple.com/documentation/signinwithapplerestapi/generate_and_validate_tokens#response-codes) in the Apple Developer documentation. |

7. Apple returns an access token, refresh token, and an identity token.

   |   |                                                                                                                                                                                                                                                            |
   | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | For more about the identity token object, see [Retrieve the User's Information from Apple ID Servers](https://developer.apple.com/documentation/signinwithapplerestapi/authenticating_users_with_sign_in_with_apple) in the Apple Developer documentation. |

8. The Apple IdP Adapter uses the Apple public key to verify the identity token.

9. PingFederate redirects the user to the web application with the user attributes from the identity token.

---

---
title: Registering an Apple app
description: To allow PingFederate to process social sign-on requests with Apple, add PingFederate as an OpenID Connect application on the Apple Developer site.
component: apple
page_id: apple:setup:pf_apple_cic_registering_an_apple_app
canonical_url: https://docs.pingidentity.com/integrations/apple/setup/pf_apple_cic_registering_an_apple_app.html
llms_txt: https://docs.pingidentity.com/integrations/apple/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 28, 2024
section_ids:
  steps: Steps
---

# Registering an Apple app

To allow PingFederate to process social sign-on requests with Apple, add PingFederate as an OpenID Connect application on the Apple Developer site.

## Steps

1. Sign on to the Apple [Certificates, Identifiers & Profiles](https://developer.apple.com/account/resources/identifiers/list) page with an Apple Developer administrator account.

2. On the **Identifiers** screen, next to the **Identifiers** heading, click **Add (+)**.

3. On the **Register a new identifier** screen, select **App IDs**. Click **Continue**.

4. Select **App**. Click **Continue**.

5. On the **Register an App ID** screen, in the **Description** field, enter a description for your application.

6. In the **Bundle ID** field, enter a name for your application, such as `com.example.mywebapp`.

7. In the **Capabilities** section, select **Sign in with Apple**. Click **Continue**.

8. On the **Confirm your App ID** screen, under **App ID Prefix**, note your **Team ID**, such as "3R6RFC464N". You will use this in [Configuring an adapter instance](pf_apple_cic_configuring_an_adapter_instance.html). Click **Register**.

---

---
title: Registering an Apple service
description: To allow PingFederate to process social sign-on requests with Apple, add PingFederate as a Sign in with Apple service on the Apple Developer site.
component: apple
page_id: apple:setup:pf_apple_cic_registering_an_apple_service
canonical_url: https://docs.pingidentity.com/integrations/apple/setup/pf_apple_cic_registering_an_apple_service.html
llms_txt: https://docs.pingidentity.com/integrations/apple/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 28, 2024
section_ids:
  context_bgd_sg5_wbc: About this task
  steps: Steps
---

# Registering an Apple service

To allow PingFederate to process social sign-on requests with Apple, add PingFederate as a Sign in with Apple service on the Apple Developer site.

## About this task

You can find official Apple documentation and troubleshooting suggestions in [Configure Sign in with Apple for the web](https://help.apple.com/developer-account/?lang=en#/dev1c0e25352) in the Apple Developer documentation.

## Steps

1. Sign on to the [Apple Developer site](https://developer.apple.com) with an Apple Developer administrator account.

2. On the **Certificates, Identifiers & Profiles > Identifiers** page, next to the **Identifiers** heading, click **+**.

3. On the **Register a new identifier** page, select **Services IDs**. Click **Continue**.

4. On the **Register a Services ID** page, in the **Description** field, enter a description for your application.

5. In the **Identifier** field, enter a name for your application, such as `com.example.mywebservice`. You will use this as the **Services ID** in [Configuring an adapter instance](pf_apple_cic_configuring_an_adapter_instance.html). Click **Continue**. Click **Register**.

   |   |                                                                                                                                  |
   | - | -------------------------------------------------------------------------------------------------------------------------------- |
   |   | This is different from the bundle ID that you entered in [Registering an Apple app](pf_apple_cic_registering_an_apple_app.html). |

6. On the **Identifiers** page, select the service that you created.

7. On the **Edit your Services ID Configuration** page, select **Sign in with Apple**. Click **Configure**.

8. On the **Web Authentication Configuration** modal, from the **Primary App ID** list, select the app that you registered in [Registering an Apple app](pf_apple_cic_registering_an_apple_app.html).

9. In the **Register Website URLs** section, in the **Domains and subdomains** field, enter the domain or domains for your web application, such as `example.com`.

10. In the **Return URLs** field, enter the Apple IdP Adapter callback endpoint on your PingFederate server, based on the following: `https://pf_host:pf_port/ext/apple-authn`. Click **Next**. Click **Done**.

11. Click **Continue**. Click **Save**.