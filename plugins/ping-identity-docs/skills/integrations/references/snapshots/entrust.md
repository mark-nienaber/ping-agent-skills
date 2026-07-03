---
title: Authentication API Support
description: You can use the PingFederate authentication API to integrate the Entrust IdP Adapter into your application.
component: entrust
page_id: entrust:authentication_api_support:pf_entrust_ik_authentication_api_support
canonical_url: https://docs.pingidentity.com/integrations/entrust/authentication_api_support/pf_entrust_ik_authentication_api_support.html
revdate: June 10, 2024
---

# Authentication API Support

You can use the PingFederate authentication API to integrate the Entrust IdP Adapter into your application.

The PingFederate Authentication API provides access to the current state of the authentication flow as a user steps through the PingFederate authentication policy. For more information, see [PingFederate authentication API](https://docs.pingidentity.com/pingfederate/latest/developers_reference_guide/pf_authentication_api.html) in the PingFederate documentation. To integrate the Entrust IdP Adapter into your authentication flow, configure your application based on the states, actions, and models available in the PingFederate Authentication API Explorer. For help, see [Exploring the Authentication API](https://docs.pingidentity.com/pingfederate/latest/developers_reference_guide/pf_exploring_authentication_api.html) in the PingFederate documentation.

---

---
title: Changelog
description: The following is the change history for the Entrust Identity Enterprise Integration Kit.
component: entrust
page_id: entrust:release_notes:pf_entrust_ik_changelog
canonical_url: https://docs.pingidentity.com/integrations/entrust/release_notes/pf_entrust_ik_changelog.html
revdate: June 10, 2024
section_ids:
  entrust-identity-enterprise-integration-kit-1-5-february-2024: Entrust Identity Enterprise Integration Kit 1.5 - February 2024
  entrust-identity-enterprise-integration-kit-1-4-september-2023: Entrust Identity Enterprise Integration Kit 1.4 - September 2023
  entrust-identity-enterprise-integration-kit-1-3-november-2022: Entrust Identity Enterprise Integration Kit 1.3 - November 2022
  entrust-identity-enterprise-integration-kit-1-2-june-2022: Entrust Identity Enterprise Integration Kit 1.2 – June 2022
  entrust-identity-enterprise-integration-kit-1-1-april-2022: Entrust Identity Enterprise Integration Kit 1.1 – April 2022
  entrust-identity-enterprise-integration-kit-1-0-january-2022: Entrust Identity Enterprise Integration Kit 1.0 – January 2022
---

# Changelog

The following is the change history for the Entrust Identity Enterprise Integration Kit.

## Entrust Identity Enterprise Integration Kit 1.5 - February 2024

* Added the ability for users to resend authentication requests for supported authenticators. For more information, see [Models, objects, and error codes](../authentication_api_support/pf_entrust_ik_models_objects_and_error_codes.html).

* Fixed knowledge-based authentication UI display issues.

* Added the ability to include the subject, when available, in the [audit log framework](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_security_audit_loggin.html).

## Entrust Identity Enterprise Integration Kit 1.4 - September 2023

* Added support for token push notifications that use mutual authentication. For more information, see <https://entrust.us.trustedauth.com/help/authentication/posts/5.26/> and [Entrust IdP Adapter settings reference](../setup/pf_entrust_ik_entrust_idp_adapter_settings_reference.html).

## Entrust Identity Enterprise Integration Kit 1.3 - November 2022

* Added the ability to handle Entrust API error codes so that it can be used for policy branching.

* Added the ability to display custom error messages based on the Entrust API error codes returned.

* Fixed an issue that caused `errorMessage` and `errorMessageDetails` to not populate in a clustered deployment.

## Entrust Identity Enterprise Integration Kit 1.2 – June 2022

* Added support for `TEMP_ACCESS_CODE` (Temporary Access Tokens).

* Added support for `SMARTCREDENTIALPUSH` (Mobile Smart Credential Push).

* Updated authenticator and message names for all authenticators in the template files.

## Entrust Identity Enterprise Integration Kit 1.1 – April 2022

* Added support for customizable error template.

* Added support for TOKEN and KBA authentication options.

* Added the ability for administrators to skip authentication selection.

* Added the ability for users to choose another authentication option in the input required state.

* Updated to the latest jackson-databind libraries.

* Updated push notifications to do better error handling for canceled or suspicious use cases.

## Entrust Identity Enterprise Integration Kit 1.0 – January 2022

* Initial Release

---

---
title: Configuring an adapter instance
description: Configure the Entrust IdP Adapter to determine how PingFederate communicates with Entrust.
component: entrust
page_id: entrust:setup:pf_entrust_ik_configuring_an_adapter_instance
canonical_url: https://docs.pingidentity.com/integrations/entrust/setup/pf_entrust_ik_configuring_an_adapter_instance.html
revdate: June 10, 2024
section_ids:
  steps: Steps
---

# Configuring an adapter instance

Configure the Entrust IdP Adapter to determine how PingFederate communicates with Entrust.

## Steps

1. In the PingFederate administrative console, create a new IdP adapter instance.

   1. Go to **Authentication > Integration > IdP Adapters**.

   2. Click **Create New Instance**.

2. On the **Type** tab, set the basic adapter instance attributes.

   1. In the **Instance Name** field, enter a name for the adapter instance.

   2. In the **Instance ID** field, enter a unique identifier for the adapter instance.

   3. From the **Type** list, select **Entrust IdP Adapter**. Click **Next**.

3. On the **IdP Adapter** tab, configure the adapter instance by referring to [Entrust IdP Adapter settings reference](pf_entrust_ik_entrust_idp_adapter_settings_reference.html). Click **Next**.

On the **Extended Contract** tab, add any attributes that you want to include in the contract. Click **Next**.

1. On the **Adapter Attributes** tab, set pseudonym and masking options as shown in [Set pseudonym and masking options](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_setting_pseudonym_masking_options.html) in the PingFederate documentation. Click **Next**.

2. On the **Adapter Contract Mapping** tab, configure the contract fulfillment details for the adapter as shown in [Define the IdP adapter contract](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_authnadapterinstancetasklet_plugincontractstate.html) in the PingFederate documentation. Click **Next**.

3. On the **Summary** tab, check and save your configuration. Click **Save**.

4. Create or modify a connection to the service provider using the Entrust IdP Adapter instance. See [SP connection management](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_sp_connect_management.html) in the PingFederate documentation.

---

---
title: Deploying the integration files
description: To get started with the integration, deploy the Entrust Identity Enterprise Integration Kit files to your PingFederate directory.
component: entrust
page_id: entrust:setup:pf_entrust_ik_deploying_the_integration_files
canonical_url: https://docs.pingidentity.com/integrations/entrust/setup/pf_entrust_ik_deploying_the_integration_files.html
revdate: June 10, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Deploying the integration files

To get started with the integration, deploy the Entrust Identity Enterprise Integration Kit files to your PingFederate directory.

## About this task

|   |                                                                                          |
| - | ---------------------------------------------------------------------------------------- |
|   | If you operate PingFederate in a cluster, the following steps refer to the console node. |

## Steps

1. Download the Entrust Identity Enterprise Integration Kit `.zip` archive from the [**Add-ons** tab of the PingFederate downloads page](https://www.pingidentity.com/en/resources/downloads/pingfederate.html) or the [Ping Identity Marketplace](https://marketplace.pingone.com/item/entrust-identity-enterprise-integration-kit).

2. Stop PingFederate.

3. If you are upgrading an existing deployment, back up your customizations and delete previous versions of the integration files.

   1. Back up any Entrust Identity Enterprise Integration Kit files that you customized in `<pf_install>/pingfederate/server/default/conf/`.

   2. Delete `pf-entrust-adapter-<version>.jar` from `<pf_install>/pingfederate/server/default/deploy`.

4. Extract the `.zip` archive and merge the contents of the `dist` directory with your `<pf_install>/pingfederate` directory.

5. If there is more than one version of the `pf-authn-api-sdk-<version>.jar` file in your `<pf_install>/pingfederate/server/default/lib` directory, delete all but the latest version of the file.

6. If you backed up any customized files, modify the new files with your customizations.

7. Start PingFederate.

8. If you operate PingFederate in a cluster, repeat steps 2-8 for each engine node.

---

---
title: Download manifest
description: The following files are included in the Entrust Identity Enterprise Integration Kit .zip archive:
component: entrust
page_id: entrust:release_notes:pf_entrust_ik_download_manifest
canonical_url: https://docs.pingidentity.com/integrations/entrust/release_notes/pf_entrust_ik_download_manifest.html
revdate: June 10, 2024
---

# Download manifest

The following files are included in the Entrust Identity Enterprise Integration Kit `.zip` archive:

* `Legal.pdf` – copyright and license information

* `dist/pingfederate/server/default` – contains the integration files

  * `deploy` – contains the Java libraries

    * `pf-entrust-adapter-<version>.jar` – JAR file that contains the Entrust IdP Adapter.

  * `conf` – contains the HTML template that presents the Entrust Identity Enterprise sign-on form.

  * `template` – contains user-facing HTML template files

    * `entrust-user-id-required.html`

    * `entrust-input-required.html`

    * `entrust-authenticator-selection-required.html`

    * `entrust-failed.html`

      * `assets` – contains functional scripts and files used by the template

    * `scripts` – contains script files used to collect and send information

      * `profileDevice.js`

      * `machineSecret.js`

      * `jquery-<version>.min.js` – A JavaScript file that contains the jQuery library

      * `deviceProfileEmbedded.js`

    * `images` – contains template image files

      * `ping-logo.svg` – an image file with company branding

      * `spinner.svg` – an image file used in a spinner animation

    * `css` – contains CSS files for the templates.

      * `entrust.css` – a CSS file that customizes the appearance of the template files.

      * `end-user/<version>/end-user.css` – a CSS file that customizes the appearance of the template files.

    * `fonts/end-user/icons` – contains template icons

      * `language-packs`

    * `entrust-messages.properties`

* `lib/pf-authn-api-sdk-<version>.jar` – a JAR file that contains the PingFederate Authentication API SDK

---

---
title: Enabling debug logging
description: To help with troubleshooting or monitoring, you can turn on activity logging for the adapter.
component: entrust
page_id: entrust:troubleshooting:pf_entrust_ik_enable_debug_logging
canonical_url: https://docs.pingidentity.com/integrations/entrust/troubleshooting/pf_entrust_ik_enable_debug_logging.html
revdate: June 10, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Enabling debug logging

To help with troubleshooting or monitoring, you can turn on activity logging for the adapter.

## About this task

These steps are optional. For general information about logging, see [Enabling debug messages and console logging](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_enabling_debug_message_and_console_logging.html) in the PingFederate documentation.

## Steps

1. Open the `<pf_install>/pingfederate/server/default/conf/log4j2.xml` file for editing.

2. If you want to log activity for PingFederate and all adapters, do the following.

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

3. If you want to log activity just for the Entrust IdP Adapter, add the following line.

   ```html
   <Logger name="com.pingidentity.adapters.entrust" level="DEBUG"/>
   ```

4. Save the file.

---

---
title: Entrust Identity Enterprise Integration Kit
description: The Entrust Identity Enterprise Integration Kit allows PingFederate to use the Entrust service for multi-factor authentication (MFA).
component: entrust
page_id: entrust::pf_entrust_ik
canonical_url: https://docs.pingidentity.com/integrations/entrust/pf_entrust_ik.html
revdate: June 10, 2024
section_ids:
  features: Features
  components: Components
  intended-audience: Intended audience
  system-requirements: System requirements
---

# Entrust Identity Enterprise Integration Kit

The Entrust Identity Enterprise Integration Kit allows PingFederate to use the Entrust service for multi-factor authentication (MFA).

## Features

* Supports the PingFederate [PingFederate authentication API](https://docs.pingidentity.com/pingfederate/latest/developers_reference_guide/pf_authentication_api.html).

* Supports the [JavaScript Widget for the PingFederate Authentication API](https://github.com/pingidentity/pf-authn-js-widget).

## Components

Entrust IdP Adapter

* Allows PingFederate to communicate with the Entrust Identity Enterprise for MFA.

Templates

* Allows you to modify the appearance of the authentication prompts.

Language packs

* Allows you to customize or localize the messages returned by the PingFederate authentication API and shown on the templates during authentication. For help, see [Localizing messages for end users](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_local_message_end_users.html) in the PingFederate documentation.

## Intended audience

This document is intended for PingFederate administrators.

If you need help during the setup process, see the following resources:

* The following sections of the PingFederate documentation:

  * [Identity provider SSO configuration](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_ident_provid_sso_config.html)

  * [Managing IdP adapters](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_managing_idp_adapters.html)

  * [Authentication policies](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_authentication_policies.html)

## System requirements

* PingFederate 10.3 or later

---

---
title: Entrust IdP Adapter settings reference
description: Field descriptions for the Entrust IdP Adapter configuration screen.
component: entrust
page_id: entrust:setup:pf_entrust_ik_entrust_idp_adapter_settings_reference
canonical_url: https://docs.pingidentity.com/integrations/entrust/setup/pf_entrust_ik_entrust_idp_adapter_settings_reference.html
revdate: June 10, 2024
---

# Entrust IdP Adapter settings reference

Field descriptions for the Entrust IdP Adapter configuration screen.

**Standard Fields**

| Field              | Description                                                                                                                  |
| ------------------ | ---------------------------------------------------------------------------------------------------------------------------- |
| **Service Domain** | The domain of the Entrust service.Format is `<customer>.<region>.trustedauth.com`For example: `mycompany.us.trustedauth.com` |
| **Application ID** | The application ID for the Identity as a Service application.                                                                |

**Advanced Fields**

| Field                                       | Description                                                                                                                                                                                                                                                                                   |
| ------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Authenticators Endpoint**                 | The endpoint used to get user authenticators.The default endpoint is `api/web/v2/authentication/users`.                                                                                                                                                                                       |
| **Select Authenticator Endpoint**           | The endpoint used to select the authenticator.The default endpoint is `/api/web/v2/authentication/users/authenticate/%s`The `%s` will be replaced by the authenticator used.                                                                                                                  |
| **Complete Authentication Endpoint**        | The endpoint used to complete authentication actions.The default endpoint is `api/web/v1/authentication/users/authenticate/%s/complete`.The `%s` will be replaced by the authenticator used.                                                                                                  |
| **Logout Endpoint**                         | The endpoint used to complete logout.The default endpoint is `/api/web/v1/authentication/logout`.                                                                                                                                                                                             |
| **HTML Template Prefix**                    | Identifies the set of HTML templates that the adapter uses.If you customized the template file names in `/server/default/conf/template`, enter the new prefix here.The default value is `entrust`.                                                                                            |
| **Messages Files**                          | Identifies the customizable language-pack file that the adapter uses.If you customize the `languaged-pack` file name in the `/server/default/conf/language-packs` directory, enter the new name here.The default value is `entrust-messages`.                                                 |
| **Error Message Key Prefix**                | Prefix for error messages in the language pack.The default value is `entrust.error`.                                                                                                                                                                                                          |
| **API Request Timeout**                     | The amount of time in milliseconds that PingFederate allows when establishing a connection with Entrust or waiting for a response to a request. A value of 0 disables the timeout.The default value is `5000`.                                                                                |
| **Default to Primary Authenticator**        | If selected, the user will default to the primary authenticator set in Entrust.                                                                                                                                                                                                               |
| **Enable Token Push With Mutual Challenge** | If selected, token push requests from the adapter enable a mutual authentication challenge unless the chained attribute `enable-token-push-with-mutual-challenge` is set to `false` and overrides this value, which is specific to the adapter instance.This check box is cleared by default. |
| **Show Failed Screen**                      | If selected, the adapter displays an authentication failed page when it encounters an error.This check box is selected by default.                                                                                                                                                            |
| **Branch on Error**                         | A comma-separated list of error codes from Entrust that can be used for conditional branching in the policy.The error codes listed are handled as a success.                                                                                                                                  |
| **Proxy Settings**                          | Defines proxy settings for outbound HTTP requests.The default value is **System Defaults**.                                                                                                                                                                                                   |
| **Custom Proxy Host**                       | The proxy server host name to use when **Proxy Settings** is set to **Custom**.This field is blank by default.                                                                                                                                                                                |
| **Custom Proxy Port**                       | The proxy server port to use when **Proxy Settings** is set to **Custom**.This field is blank by default.                                                                                                                                                                                     |

---

---
title: Known issues and limitations
description: The following are known issues or limitations for the Entrust Identity Enterprise Integration Kit.
component: entrust
page_id: entrust:release_notes:pf_entrust_ik_known_issues_and_limitations
canonical_url: https://docs.pingidentity.com/integrations/entrust/release_notes/pf_entrust_ik_known_issues_and_limitations.html
revdate: June 10, 2024
section_ids:
  known-issues: Known issues
  known-limitations: Known limitations
---

# Known issues and limitations

The following are known issues or limitations for the Entrust Identity Enterprise Integration Kit.

## Known issues

* For `TOKENPUSH` and `SMARTCREDENTIALPUSH` use-cases, if the user does not act on the push notification received on their Entrust application, the input required page will keep attempting to complete the transaction.

## Known limitations

* The adapter supports resource rules with an authentication decision of **Skip Password** for first factor for low risk cases.

* When using the PingFederate authentication API and a user completes a `TOKENPUSH` or `SMARTCREDENTIALPUSH` authenticator, the user is taken to the `INPUT_REQUIRED` state. The user can submit the default template to continue and finish the flow.

---

---
title: Models, objects, and error codes
description: When using the Entrust IdP Adapter through the PingFederate authentication API, the adapter uses the following state models, action models, objects, and error codes.
component: entrust
page_id: entrust:authentication_api_support:pf_entrust_ik_models_objects_and_error_codes
canonical_url: https://docs.pingidentity.com/integrations/entrust/authentication_api_support/pf_entrust_ik_models_objects_and_error_codes.html
revdate: June 10, 2024
section_ids:
  state-models: State models
  action-models: Action models
  objects: Objects
  error-codes: Error Codes
---

# Models, objects, and error codes

When using the Entrust IdP Adapter through the PingFederate authentication API, the adapter uses the following state models, action models, objects, and error codes.

## State models

| Status                             | Response Model                                                                                                                                                                                                                                                                                                                                             | Action                                                                                         | Description                                                                                     |
| ---------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| `USER_ID_REQUIRED`                 | This state has no model.                                                                                                                                                                                                                                                                                                                                   | * `checkuserId`

* `cancel`                                                                    | The user must select the one-time device from the list to proceed with the authentication flow. |
| `AUTHENTICATOR_SELECTION_REQUIRED` | - `authenticators:` The list of authenticators available to the user.                                                                                                                                                                                                                                                                                      | * `selectAuthenticator`

* `cancel`                                                            | The user must select an authenticator for authentication.                                       |
| `INPUT_REQUIRED`                   | - `authenticator (string): `The authenticator that the user selected.

- `gridChallenge (GridChallenge):` The information that's needed for grid authentication.

- `kbaChallenge (KbaChallenge):` The information that's needed for KBA authentication.

- `tokenPushMutualChallenge (string):` The optional token push mutual challenge that's received. | * `checkInput`

* `showAlternativeAuthentication`

* `resendAuthenticationRequest`

* `cancel` | The user must complete authentication via an input.                                             |
| `ENTRUST_FAILED`                   | - `code (string):` The error code.

- `message (string):` The developer-facing error message.

- `userMessage (string):` The user-facing error message.                                                                                                                                                                                                    | * `cancel`                                                                                     | Entrust authentication failed.                                                                  |

## Action models

| Action                          | Request Model                                                                                                                                             | Errors                      | Description                                           |
| ------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------- | ----------------------------------------------------- |
| `checkuserId`                   | * `userId (string):` The user ID that's used for authentication.                                                                                          | This action has no errors.  | Submits the user ID for authentication.               |
| `cancel`                        | This action has no model.                                                                                                                                 | This action has no errors.  | Cancels the current operation.                        |
| `selectAuthenticator`           | - `authenticator (string):` The authenticator that the user selected.                                                                                     | * Error: `VALIDATION_ERROR` | Selects an authenticator as an authentication method. |
| `checkInput`                    | - `input (string): `The response that's required for authentication.

- `answers(array[KbaAnswer]):` The KBA response that's required for authentication. | * Error: `VALIDATION_ERROR` | Validates the input from the user.                    |
| `showAlternativeAuthentication` | This action has no model.                                                                                                                                 | This action has no errors.  | Shows the list of alternative authentication options. |
| `resendAuthenticationRequest`   | This action has no model.                                                                                                                                 | - Error: `VALIDATION_ERROR` | Resends the current authentication request.           |

## Objects

**GridChallenge**

| Parameter Name    | Type         | Description                                                    |
| ----------------- | ------------ | -------------------------------------------------------------- |
| `cells`           | String array | The cells used for the input.                                  |
| `numCharsPerCell` | Integer      | The number of characters per cell.                             |
| `serialNumbers`   | String array | The list of serial numbers of the grid cards that can be used. |

**KbaChallenge**

| Parameter name  | Type                    | Description                       |
| --------------- | ----------------------- | --------------------------------- |
| `id`            | String                  | The ID used for the challenge.    |
| `userQuestions` | Array of `UserQuestion` | The questions used for the input. |

**UserQuestion**

| Parameter name | Type   | Description                               |
| -------------- | ------ | ----------------------------------------- |
| `id`           | String | The ID for the user question.             |
| `question`     | String | The question value for the user question. |
| `answer`       | String | The answer value for the user question.   |

**KbaAnswer**

| Parameter name | Type   | Description                        |
| -------------- | ------ | ---------------------------------- |
| `id`           | String | The ID of the question.            |
| `answer`       | String | The answer value for the question. |

## Error Codes

An error code is returned if the call flow state has not reached a dead end, and the user can still authenticate with a device.

**Top level error codes**

| Error code         | Message                                 | HTTP status |
| ------------------ | --------------------------------------- | ----------- |
| `VALIDATION_ERROR` | One or more validation errors occurred. | 400         |

**Detail level error codes**

| Error code              | Message                                                       | userMessageKey          | Parent code        |
| ----------------------- | ------------------------------------------------------------- | ----------------------- | ------------------ |
| `INVALID_AUTHENTICATOR` | Selected authenticator is not a valid form of authentication. | `invalid.authenticator` | `VALIDATION_ERROR` |
| `INVALID_INPUT`         | The input entered is incorrect.                               | `invalid.input`         | `VALIDATION_ERROR` |
| `INVALID_INPUT_FORMAT`  | The format of input is incorrect.                             | `invalid.input.format`  | `VALIDATION_ERROR` |
| `GENERAL_ERROR`         | Authentication error.                                         | `general.error`         | `VALIDATION_ERROR` |
| `ACCOUNT_LOCKED_OUT`    | The user account is locked.                                   | `account.locked.out`    | `VALIDATION_ERROR` |
| `PUSH_CANCELLED`        | User canceled push notification transaction.                  | `push.cancel`           | `VALIDATION_ERROR` |
| `PUSH_SUSPICIOUS`       | User marked the push notification transaction as suspicious.  | `push.suspicious`       | `VALIDATION_ERROR` |

---

---
title: Overview of the SSO flow
description: With the Entrust Identity Enterprise Integration Kit, PingFederate includes Entrust in the sign-on flow.
component: entrust
page_id: entrust::pf_entrust_ik_overview_of_the_sso_flow
canonical_url: https://docs.pingidentity.com/integrations/entrust/pf_entrust_ik_overview_of_the_sso_flow.html
revdate: June 10, 2024
section_ids:
  description: Description
---

# Overview of the SSO flow

With the Entrust Identity Enterprise Integration Kit, PingFederate includes Entrust in the sign-on flow.

## Description

1. The user initiates SSO from an SP application through the PingFederate SP server.

   |   |                                                                                                                                                                                                                                                                                                                                                                   |
   | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | This SP-initiated scenario represents the optimal use case, where both the identity provider (IdP) and SP use PingFederate. If your SP partner does not support this scenario, however, PingFederate accepts any valid SAML authentication request.You can also enable IdP-initiated SSO. In this case, the SSO flow would not include this step or the next one. |

2. The PingFederate SP server generates a SAML `AuthnRequest` and sends it to the PingFederate IdP server.

3. The IdP requests authentication from the adapter and it asks for the User ID.

4. The adapter sends the User ID to Entrust.

5. Entrust responds with a list of authenticators configured for the user.

   |   |                                                                                                                                                      |
   | - | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | If the **Default to Primary Authenticator** setting is enabled, the adapter displays the appropriate window. This setting is not enabled by default. |

6. The adapter displays the list of authenticators and the user selects the one they want to use.

7. The adapter sends the selected authenticator to Entrust.

8. Entrust responds with the next step to the user (sends SMS OTP, TOTP, Entrust soft token push notification, mobile smart credential push authentication, Grid card selection, KBA) and the adapter.

9. The adapter presents the appropriate screen (enter OTP, KBA, grid selection, enter temporary access tokens) and sends the user response to Entrust.

10. Entrust validates the credentials sent and responds to PingFederate.

11. If the validation fails, the user is denied. If validation succeeds, the PingFederate IdP server generates a SAML assertion with the username as the Subject and passes it to the PingFederate SP server.

---

---
title: Registering PingFederate as an application in Entrust
description: To process sign-on requests, PingFederate requires access to the Entrust Authentication API. You can grant access in the Entrust admin console.
component: entrust
page_id: entrust:setup:pf_entrust_ik_registering_pf_as_an_application_in_entrust
canonical_url: https://docs.pingidentity.com/integrations/entrust/setup/pf_entrust_ik_registering_pf_as_an_application_in_entrust.html
revdate: June 10, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
  result: Result:
---

# Registering PingFederate as an application in Entrust

To process sign-on requests, PingFederate requires access to the Entrust Authentication API. You can grant access in the Entrust admin console.

## About this task

For more information about registering authentication agents, see Integrate API applications in the Entrust documentation.

## Steps

1. Sign on to the Entrust admin console.

2. Go to **Resources > Applications**.

3. In the **Applications** window, click **Add**.

4. In the **Select an Application Template** window, in the **API Applications** section, click **Authentication API**.

5. In the **Add Authentication API** window, in the **Application Name** field, enter a name for your application.

6. In the **Application Description** field, enter a description for your application.

7. **Optional:** Add a custom application logo.

   1. Next to **Application logo**, click the **[icon: plus, set=fa]**icon.

   2. Click the **Upload** icon.

   3. Browse to your chosen file and click **Open**.

   4. Resize your image if required, then click **OK**.

8. Click **Next**.

9. In the **General Settings** window, for Source of the Client IP Address for Risk Conditions, select one of the following.

   | Option                            | Description                                                              |
   | --------------------------------- | ------------------------------------------------------------------------ |
   | Not Provided                      | The IP address is not provided and is not extracted from the connection. |
   | Provided in the API               | The IP address is provided in the request body of the API.               |
   | From the incoming HTTP connection | The IP address is extracted from the connection.                         |

10. Click Submit.

    ### Result:

    The **Application ID** is generated.

11. Copy and paste the **Application ID** into PingFederate.

12. Click **Done**.