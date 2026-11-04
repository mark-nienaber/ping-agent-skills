---
title: (Workforce only) Configuring offline MFA
description: Offline multi-factor authentication (MFA) allows users to authenticate when the PingOne server is unreachable. If your organization is using MFA as a primary or secondary mode of authentication for federated single sign-on (SSO), you can implement the offline MFA feature of the PingOne MFA IdP Adapter adapter, so you can circumvent unforeseen outages or network issues preventing users from signing on to access their applications.
component: pingone
page_id: pingone:pingone_mfa_integration_kit:pf_p1_mfa_ik_configuring_offline_mfa
canonical_url: https://docs.pingidentity.com/integrations/pingone/pingone_mfa_integration_kit/pf_p1_mfa_ik_configuring_offline_mfa.html
llms_txt: https://docs.pingidentity.com/integrations/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 28, 2026
section_ids:
  before-you-begin: Before you begin
  steps: Steps
---

# (Workforce only) Configuring offline MFA

Offline multi-factor authentication (MFA) allows users to authenticate when the PingOne server is unreachable. If your organization is using MFA as a primary or secondary mode of authentication for federated single sign-on (SSO), you can implement the offline MFA feature of the PingOne MFA IdP Adapter adapter, so you can circumvent unforeseen outages or network issues preventing users from signing on to access their applications.

When the PingOne server is available, the adapter caches each user's device credentials in an LDAP data source. If the PingOne server can't be reached, the adapter uses those cached credentials to authenticate the user locally.

|   |                                                                      |
| - | -------------------------------------------------------------------- |
|   | PingOne MFA policies are not enforced during offline authentication. |

## Before you begin

Before configuring offline MFA, make sure that you have the following:

* **PingOne Workforce environment with the **PingFederate Administrator** role**: The **PingFederate Administrator** role is required to use offline MFA.

* **PingOne MFA IdP Adapter 4.1** or later.

* **LDAP data source**: An LDAP data source must be configured in PingFederate to store offline device credentials as an attribute on the user object.

* **Encryption key** (recommended): An encryption key is strongly recommended to protect device data at rest. Without an encryption key, device credentials are stored as plain text in LDAP, and the **Allow Offline Devices Without Encryption** checkbox must be selected before you can save the configuration.

* **Unlimited Strength Java Cryptography Extension (JCE)**: Required for supporting the 256-byte key size for cryptographic algorithms. Without it, the feature will return an exception related to the missing library and will not function.

## Steps

1. In the PingFederate administrative console, go to **Authentication > Integration > IdP Adapters** and select the PingOne MFA IdP Adapter adapter, or create a new one.

2. On the **IdP Adapter** tab, click **Show Advanced Fields**.

3. Configure the offline MFA fields:

   * **LDAP Data Source**: Select the LDAP data source where your user objects are stored. Offline device data is currently configured to reside directly on the user object.

   * **Encryption Key For Devices**: A base64url-encoded 256-bit key used to encrypt device credentials before saving them to LDAP.

     |   |                                                                                                                                                                                                                                             |
     | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
     |   | If the encryption key is changed, users must authenticate online at least once for their cached device credentials to be re-encrypted with the new key. Until then, offline authentication follows the **No Devices Failure Mode** setting. |

   * **Allow Offline Devices Without Encryption**: Select the checkbox to confirm that device credentials will be stored as plain text. Required if the **Encryption Key** field is empty.

   * **LDAP Search Scope**: Select the scope used when searching the directory for the user's device data. Only applies when device data is stored on the user object.

   * **LDAP Data Source Filter**: An LDAP search filter used to locate the user entry. Use `${username}` as a placeholder for the authenticating user's username. For example, for Active Directory: `sAMAccountName=${username}`.

   * **State Attribute**: The name of an LDAP attribute on the user object that overrides how that user is authenticated during offline authentication. When set, the adapter reads this attribute to determine whether to bypass or block the individual user. If left empty, no per-user override is applied.

4. In the **Service Unavailable Failure Mode** field, configure how the adapter behaves when it's unable to access PingOne. Options include:

   * **Block user**: Block the user's sign-on attempt.

   * **Bypass authentication**: Authenticate the user without requiring MFA.

   * **Enforce offline authentication**: The adapter requires offline MFA authentication regardless of PingOne availability. Use this option temporarily if PingOne is down and passive offline authentication isn't prompting users to authenticate offline.

   * **Passive offline authentication**: The adapter attempts offline MFA when PingOne is unreachable, then falls back to the **No Devices Failure Mode** setting if the user has no cached offline credentials.

5. Click **Done**, then click **Save**.

---

---
title: (Workforce only) Transitioning from the PingID Adapter to the PingOne MFA IdP Adapter
description: Learn how to transition your PingFederate deployment from the PingID Adapter to the PingOne MFA IdP Adapter.
component: pingone
page_id: pingone:pingone_mfa_integration_kit:pf_p1_mfa_ik_transitioning_from_pingid_adapter
canonical_url: https://docs.pingidentity.com/integrations/pingone/pingone_mfa_integration_kit/pf_p1_mfa_ik_transitioning_from_pingid_adapter.html
llms_txt: https://docs.pingidentity.com/integrations/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 7, 2026
section_ids:
  requirements: Requirements
  migrating-your-configuration: Migrating your configuration
  _changed_fields: Changed fields
  changed-behavior: Changed behavior
  _changed_attributes: Changed attributes
  authentication-domain-changes: Authentication domain changes
  unsupported-features: Unsupported Features
---

# (Workforce only) Transitioning from the PingID Adapter to the PingOne MFA IdP Adapter

If you currently use the PingID Adapter for PingFederate integration, you can now use the PingOne MFA Integration Kit to integrate directly from PingOne without requiring the legacy PingID admin portal. This topic covers requirements, differences in field names and attributes, and features not yet available in the PingOne MFA Integration Kit.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The PingOne MFA Integration Kit and the PingID Adapter are not interchangeable versions of the same product.- The PingID Adapter integrates directly with the PingID service.

- The PingOne MFA Integration Kit integrates with PingOne and requires either:

  * Singapore and Canada geographies: a PingOne for Workforce environment.

  * All other geographies: a PingOne environment with the PingID service.

    You must create a new adapter instance and reconfigure your PingFederate authentication policies to use the PingOne MFA IdP Adapter. |

There are a few key differences to be aware of before you start:

* Configuration

  * **PingOne MFA IdP Adapter**: Configuration is split between PingOne admin portal and the adapter.

  * **PingID Adapter**: Configuration is split between the PingID admin portal and the adapter itself.

* Authenticator flow UI

  * **PingOne MFA IdP Adapter**: Includes Native UI HTML files, which are bundled with the adapter.

  * **PingID Adapter**: No native UI

* Device Management

  * **PingOne MFA IdP Adapter**: Device management can be handled natively in the adapter, without requiring device management through an external application.

  * **PingID Adapter**: Device management requires an external application (such as the PingID admin portal **Devices page**, or the PingOne **MyAccounts** page).

* Download manifest

  The PingOne MFA Integration Kit has a different download manifest from the PingID Adapter. Before deploying, review the [PingOne MFA Integration Kit download manifest](pf_p1_mfa_ik_download_manifest_4.0.html) to make sure you have the correct files.

## Requirements

| Requirement                 | Details                                                                                                                                                       |
| --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| PingFederate                | 11.3 or later                                                                                                                                                 |
| PingOne MFA Integration Kit | 4.1 or later                                                                                                                                                  |
| Java                        | 17 or later                                                                                                                                                   |
| PingOne environment         | Singapore and Canada geographies: requires a PingOne for Workforce environment.All other geographies: requires a PingOne environment with the PingID service. |

|   |                                                                                                                          |
| - | ------------------------------------------------------------------------------------------------------------------------ |
|   | Passwordless authentication using the PingID Desktop App (including Conditional UI) requires PingFederate 13.x or later. |

## Migrating your configuration

Create a new PingOne MFA IdP Adapter instance and use it to recreate your configuration manually. Test the configuration and when you are done, transition your users to use the new PingOne MFA IdP Adapter instance.

1. [Update the PingOne MFA Integration Kit and deploy it](pf_p1_mfa_ik_deploying_the_integration_files_4.0.html) to your PingFederate instance.

2. [Connect PingFederate to PingOne](pf_p1_mfa_ik_connecting_pf_to_p1_4.0.html).

3. [Configure a new PingOne MFA IdP Adapter instance](pf_p1_mfa_ik_configuring_an_adapter_instance_4.0.html), referring to [Changed fields](#_changed_fields) for field names that changed.

4. Update your PingFederate authentication policies to use the new adapter instance.

5. If your authentication policies use PingID Adapter output attributes in downstream policy steps, update them to use the equivalent PingOne MFA Integration Kit attributes. See [Changed attributes](#_changed_attributes).

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | * If your users authenticate with passkeys devices, you must:

  1. Update the relevant FIDO policy to use a compatible domain (preferably the PingFederate root domain) as the `rpid`.

  2. Make sure users with Passkey devices registered with the PingOne domain re-register their Passkeys.

  Learn more in [Authentication domain changes](#authentication-domain-changes) and [Unsupported Features](#unsupported-features).

* If your PingOne MFA policy still includes the legacy FIDO implementation (listing FIDO biometrics and Security Key as authentication methods), you must update it to FIDO2. Learn more in [Updating an existing MFA policy to use FIDO2](https://docs.pingidentity.com/strong_authentication_mfa/p1_updating_an_mfa_policy_to_fido2.html) in the PingOne documentation. |

## Changed fields

The following PingID Adapter fields have new names or different behavior in the PingOne MFA IdP Adapter.

**Field name changes from the PingID Adapter to the PingOne MFA IdP Adapter**

| PingID Adapter field                                    | PingOne MFA IdP Adapter field                                                                           | Notes                                                                                                                                                                                                                                                                                                            |
| ------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Authentication During Errors                            | **Service Unavailable Failure Mode**                                                                    | Expanded to include offline MFA options: **Passive offline authentication** and **Enforce offline authentication**. Learn more in [(Workforce only) Configuring offline MFA](pf_p1_mfa_ik_configuring_offline_mfa.html).                                                                                         |
| Users Without a Paired Device                           | **No Devices Failure Mode**                                                                             | Updated to account for offline MFA scenarios.                                                                                                                                                                                                                                                                    |
| Allow only predefined values for phone or email devices | **Email Field Behavior**, **SMS Field Behavior**, **Voice Field Behavior**, **WhatsApp Field Behavior** | Replaced by per-method field behavior settings. Each field accepts **None** (blank), **Pre-populate** (editable), or **Pre-populate and Restrict** (read-only from the user directory). Learn more in [PingOne MFA IdP Adapter settings reference](pf-p1-mfa-ik-p1-mfa-idp-adapter-settings-reference_4.0.html). |
| Require PingID Registration                             | **Prompt Users to Set Up MFA**                                                                          | Controls whether users without a paired device are prompted to register an authentication method during sign-on.                                                                                                                                                                                                 |
| LDAP Username Mapping                                   | **Use Username Attribute During Authentication**                                                        | Renamed in the PingOne MFA IdP Adapter. Controls whether the value from **Username Attribute** is used during authentication as well as provisioning. Learn more in [PingOne MFA IdP Adapter settings reference](pf-p1-mfa-ik-p1-mfa-idp-adapter-settings-reference_4.0.html).                                   |
| Enforce authentication after device registration        | **Enforce authentication after device registration**                                                    | The field name is unchanged. In the PingOne MFA IdP Adapter, configure this setting in the adapter's Advanced fields instead of in the PingID admin portal. Learn more in [PingOne MFA IdP Adapter settings reference](pf-p1-mfa-ik-p1-mfa-idp-adapter-settings-reference_4.0.html).                             |
| HTML Template                                           | **HTML Template Prefix**                                                                                | The PingOne MFA IdP Adapter uses a prefix to resolve HTML template files. Specify the prefix that matches your custom templates, or leave blank to use the bundled default templates.                                                                                                                            |
| PingID Heartbeat Timeout                                | **API Request Timeout**                                                                                 | Controls the timeout for requests to the PingOne MFA API.                                                                                                                                                                                                                                                        |
| PingID Properties File Name                             | N/A                                                                                                     | The PingID Adapter required a PingID-specific properties file. The PingOne MFA IdP Adapter does not use a separate properties file; all configuration is in the adapter itself.                                                                                                                                  |
| Keep cookies at sign-off                                | Requires the Remember Me adapter                                                                        | SLO is supported when the Remember Me adapter is configured in your PingFederate authentication policy. Learn more in [Remembered devices setup](pf-p1-mfa-ik-remembered-device-setup_4.0.html).                                                                                                                 |
| Refresh UserId Cookie, Cookie Duration                  | N/A                                                                                                     | The PingID Adapter managed its own cookie lifecycle. Cookie sign-off and refresh behavior is handled by PingFederate session management, not the PingOne MFA IdP Adapter.                                                                                                                                        |

## Changed behavior

The following PingID Adapter behaviors work differently in the PingOne MFA IdP Adapter.

* Just-in-time (JIT) registration

  * **PingOne MFA IdP Adapter**: The PingOne MFA IdP Adapter also provisions missing authentication methods for existing PingOne users, as well as new users with no devices. If a user exists in PingOne but is missing one or more authentication methods, the adapter provisions a device on initial sign-on. Learn more in [Enabling user and authentication method provisioning](pf_p1_mfa_ik_enabling_user_and_authentication_method_provisioning_4.0.html).

  * **PingID Adapter**: JIT only runs if the user has no devices.

* Protect risk evaluation

  * **PingOne MFA IdP Adapter**: Protect risk evaluation is handled by the [PingOne Protect Integration Kit](../pingone_protect_integration_kit/pf_p1_protect_ik_overview_sso_flow.html) that's chained before the MFA adapter in the PingFederate authentication policy. The MFA adapter receives and acts on the Protect results.

  * **PingID Adapter**: Risk evaluation was configured directly in the adapter through the Risk Level and PingOne Protect API Response Mapping fields.

## Changed attributes

The PingID Adapter wrote authentication results to the `pingid.authentication.type` output attribute. The PingOne MFA Integration Kit uses `pingone.mfa.status`, which has a different set of values.

If your authentication policies use `pingid.authentication.type` for branching decisions, update them to reference `pingone.mfa.status` instead. The `pingone.mfa.status` values distinguish between web and mobile sign-on contexts. Learn more in [PingOne MFA attributes reference](pf_p1_mfa_ik_p1_mfa_status_attributes_reference_4.0.html).

**Attribute changes from the PingID Adapter to the PingOne MFA IdP Adapter**

| PingID Adapter attribute     | PingOne MFA IdP Adapter attribute | Notes                                                                                                                                                             |
| ---------------------------- | --------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `pingid.authentication.type` | `pingone.mfa.status`              | Values differ. See [PingOne MFA attributes reference](pf_p1_mfa_ik_p1_mfa_status_attributes_reference_4.0.html) for the full list of `pingone.mfa.status` values. |

## Authentication domain changes

The following differences exist between the PingOne MFA Integration Kit and the PingID Adapter:

* **PingID Adapter**: Redirected users to the PingOne regional domain (pingone.\<geography_name>) to complete authentication.

* **PingOne MFA IdP Adapter**: Users sign on entirely on your custom domain. The adapter does not redirect users to a PingOne domain during authentication.

  If your users authenticate with passkeys or FIDO devices, when transitioning to the PingOne MFA Integration Kit, you'll need to update the relevant FIDO policy to use a compatible domain (preferably the PingFederate root domain) as the `rpid`.

  Learn more in [Using FIDO device with PingOne custom domain configuration](pf_p1_mfa_ik_configuring_domains_for_fido_device_support_4.0.html) and [Configuring a PingFederate policy for a consistent passwordless authentication experience](pid_configuring_pf_policy_for_passwordless_authentication.html).

## Unsupported Features

The following features are not currently supported in the PingOne MFA Integration Kit:

* PingID-compatible post-authentication attributes

* Mandatory enrollment date

* Passkeys registered with the PingOne domain can't be used for authentication. The users should use the PingOne MFA Integration Kit device management to re-register their Passkey device. In a future release, the option to re-register a Passkey to a compatible domain will be included as part of the authentication flow.

---

---
title: Adding a language pack
description: The PingOne MFA Integration Kit supports localized user-facing messages through PingFederate's language pack mechanism. You can add a language pack to display adapter messages in a language other than English.
component: pingone
page_id: pingone:pingone_mfa_integration_kit:pf_p1_mfa_ik_adding_a_language_pack_4.0
canonical_url: https://docs.pingidentity.com/integrations/pingone/pingone_mfa_integration_kit/pf_p1_mfa_ik_adding_a_language_pack_4.0.html
llms_txt: https://docs.pingidentity.com/integrations/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: August 31, 2026
section_ids:
  about-this-task: About this task
  steps: Steps
  result: Result
---

# Adding a language pack

The PingOne MFA Integration Kit supports localized user-facing messages through PingFederate's language pack mechanism. You can add a language pack to display adapter messages in a language other than English.

## About this task

The adapter uses PingFederate's `LanguagePackMessages` class and standard Java `ResourceBundle` locale fallback. When a user authenticates, PingFederate selects the properties file that best matches the user's locale. If no matching locale file exists, PingFederate falls back to English.

The PingOne MFA Integration Kit 4.1 download includes adapter message files for the following languages:

* Canadian French

* Czech

* Dutch

* English

* French

* German

* Hungarian

* Italian

* Japanese

* Korean

* Polish

* Portuguese

* Russian

* Simplified Chinese

* Thai

* Turkish

The PingOne MFA Integration Kit download includes one adapter-specific message file for each supported language. To enable a locale in PingFederate, two files are required in the PingFederate language-packs folder:

* `pingone-mfa-messages_<locale>.properties` — the adapter-specific messages file included in the PingOne MFA Integration Kit download

* `pingfederate-messages_<locale>.properties` — the core PingFederate messages file copied from the PingFederate installation

|   |                                                                                                                                                                                                                  |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Both files must be present in the `language-packs` folder. If `pingfederate-messages_<locale>.properties` is absent, PingFederate silently falls back to English even when the adapter-specific file is present. |

## Steps

1. In the PingOne MFA Integration Kit download, locate the `language-packs` folder. For more information about the download contents, refer to [Download manifest](pf_p1_mfa_ik_download_manifest_4.0.html).

2. Select the pretranslated adapter message file for the language you want to use.

   The file uses the following naming pattern:

   ```
   {file-prefix}-messages_<locale>.properties
   ```

3. Copy the selected adapter message file to `<pf_install>/server/default/conf/language-packs`. To customize the messages, edit only the values on the right side of each `=` sign. Do not change the message keys.

   The download includes adapter message files for Czech, German, English, Canadian French, French, Hungarian, Italian, Japanese, Korean, Dutch, Polish, Portuguese, Russian, Thai, Turkish, and Simplified Chinese.

4. In your PingFederate installation, locate `<pf_install>/server/default/conf/language-packs`. Copy `pingfederate-messages.properties` and rename the copy to use the same locale tag:

   ```
   pingfederate-messages_<locale>.properties
   ```

   For example: `pingfederate-messages_fr.properties`

5. Place both locale files in `<pf_install>/server/default/conf/language-packs`:

   * `pingone-mfa-messages_<locale>.properties`

   * `pingfederate-messages_<locale>.properties`

6. Restart the PingFederate server.

## Result

When a user authenticates and their browser locale matches the locale tag you configured, the adapter displays messages in that language.

---

---
title: Adding an application in DaVinci
description: Create an application to associate your PingFederate integration with your flow.
component: pingone
page_id: pingone:pingone_davinci_integration_kit:pf_p1_davinci_ik_adding_an_application_in_davinci
canonical_url: https://docs.pingidentity.com/integrations/pingone/pingone_davinci_integration_kit/pf_p1_davinci_ik_adding_an_application_in_davinci.html
llms_txt: https://docs.pingidentity.com/integrations/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 19, 2024
section_ids:
  steps: Steps
---

# Adding an application in DaVinci

Create an application to associate your PingFederate integration with your flow.

## Steps

1. Sign on to the DaVinci admin portal.

2. Create a blank flow:

   1. Go to **Flows** and click **[icon: plus, set=fa]Add Flow**.

   2. Select **Blank Flow**.

   3. On the **Add Flow** dialog, enter a name for your flow. Click **Create**.

   4. Complete the flow as described in [Building a flow in DaVinci](pf_p1_davinci_ik_building_a_flow_in_davinci.html).

3. Add an application:

   1. Go to **Applications**.

   2. Click **[icon: plus, set=fa]Add Application**

   3. On the **Add Application** dialog, enter a name for your application. Click **Create**.

   4. Click your application.

4. Add a flow policy to your application:

   1. On the **Flow Policy** tab, click **[icon: plus, set=fa]Add Flow Policy**.

   2. Select the flow that you made in step 2. Select **Latest Version** or another version. Click **Create My Flow Policy**.

   3. On the **Edit Your Weight Distribution** dialog, in the **Analytics - Select Success Nodes** list, select your **Send success JSON response** node. Click **Save My Flow Policy**.

   4. On the **Flow Policy** tab, note your **Policy ID**. You'll use this to configure the DaVinciadapter.

5. On the **General** tab, note your **Company ID** and **API Key**. You'll use these to configure the DaVinci adapter.

---

---
title: Adding device profiling to a browser-based authentication page
description: You can adapt these instructions to add device profiling to any web page included in an adapter, such as the Identifier First Adapter or a custom adapter. The page must meet the criteria listed in Device profiling methods.
component: pingone
page_id: pingone:pingone_protect_integration_kit:pf_p1_protect_ik_adding_device_profiling_browser
canonical_url: https://docs.pingidentity.com/integrations/pingone/pingone_protect_integration_kit/pf_p1_protect_ik_adding_device_profiling_browser.html
llms_txt: https://docs.pingidentity.com/integrations/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: August 12, 2026
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Adding device profiling to a browser-based authentication page

## About this task

You can adapt these instructions to add device profiling to any web page included in an adapter, such as the Identifier First Adapter or a custom adapter. The page must meet the criteria listed in [Device profiling methods](pf_p1_protect_ik_device_profiling_methods.html).

To use the HTML Form Adapter:

* [Configure a risk provider instance](pf_p1_protect_ik_configuring_provider_instance.html)

* [Configure an HTML Form Adapter instance](http://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_html_form_adapter_advanced_fields.html) to use the risk provider

## Steps

1. If you're modifying an external web application, copy the following files from the integration `.zip` archive to a location that your page can access.

   * `signals-sdk-<version>.js`

   * `pingone-protect-device-profile-implementation.js`. (If you are using version 1.0.1 or earlier of the integration kit, the file is called `pingone-protect-device-profiling.js`)

2. Add the following external script references to the sign-on page:

   |   |                                                   |
   | - | ------------------------------------------------- |
   |   | The scripts must be added in the following order. |

   ```
   <script type="text/javascript" src="signals-sdk-<version>.js"></script>
   <script type="text/javascript" src="pingone-protect-device-profile-implementation.js"></script>
   ```

   |   |                                                                                                                                                                                                         |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | If you are using version 1.0.1 or earlier of the integration kit, replace the reference to `pingone-protect-device-profile-implementation.js` with a reference to `pingone-protect-device-profiling.js` |

3. When you complete the steps in [Configuring an adapter instance](pf_p1_protect_ik_configuring_an_adapter_instance.html), you can enable risk evaluation for active sessions.

   Follow the steps in [Configuring authentication sessions](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_config_auth_sessions.html) to set up sessions for the PingOne Protect Adapter, and complete steps 2a, 2b, and 3.

---

---
title: Adding device profiling to a browser-based authentication page
description: "There are two ways for device profiling data to be collected: by the PingOne Risk IdP Adapter, or by a previous adapter such as the HTML Form Adapter."
component: pingone
page_id: pingone:pingone_risk_integration_kit:pf_p1_risk_ik_adding_device_profiling_to_an_authentication_page
canonical_url: https://docs.pingidentity.com/integrations/pingone/pingone_risk_integration_kit/pf_p1_risk_ik_adding_device_profiling_to_an_authentication_page.html
llms_txt: https://docs.pingidentity.com/integrations/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 12, 2024
section_ids:
  about-this-task: About this task
  adding-device-profiling-to-a-browser-based-authentication-page-using-the-pingone-risk-signals-sdk-with-integration-kit-1-3-1: Adding device profiling to a browser-based authentication page using the PingOne Risk (Signals) SDK with integration kit 1.3.1
  about-this-task-2: About this task
  steps: Steps
  adding-device-profiling-to-a-browser-based-authentication-page-using-the-pingone-risk-signals-sdk-and-integration-kit-1-3-or-earlier: Adding device profiling to a browser-based authentication page using the PingOne Risk (Signals) SDK and integration kit 1.3 or earlier
  about-this-task-3: About this task
  steps-2: Steps
  adding-device-profiling-to-a-browser-based-authentication-page-using-fingerprint-js: Adding device profiling to a browser-based authentication page using Fingerprint JS
  about-this-task-4: About this task
  steps-3: Steps
---

# Adding device profiling to a browser-based authentication page

There are two ways for device profiling data to be collected: by the PingOne Risk IdP Adapter, or by a previous adapter such as the HTML Form Adapter.

## About this task

Getting the device profile on the HTML Form Adapter page reduces the perceived wait times for the user. Learn more in [Device profiling methods](pf_p1_risk_ik_device_profiling_methods.html).

## Adding device profiling to a browser-based authentication page using the PingOne Risk (Signals) SDK with integration kit 1.3.1

### About this task

You can adapt these instructions to add device profiling to any page, such as the HTML Form Adapter or your web application. The page must meet the criteria listed in [Device profiling methods](pf_p1_risk_ik_device_profiling_methods.html).

|   |                                                                                                                                                                                 |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | PingOne Risk Integration Kit version 1.3.1 must be deployed before any changes can be made on the HTML side. SDK version 5.2 and later requires adapter version 1.3.1 or later. |

### Steps

1. If you are modifying an external web application, copy the following files from the integration `.zip` archive to a location that your page can access.

   * `pingone-risk-profiling-signals-sdk.js`

   * `pingone-risk-management-embedded.js`

   * `signals-sdk-<version>.js`

2. **Optional:** Edit the `pingone-risk-profiling-signals-sdk.js` file and add your PingOne environment ID.

   ```
   function profileDevice(callback) {
       // Initialize the SDK
       // replace <envid> with the PingOne console > Environment > Environment ID value
       onPingOneSignalsReady(function () {
           _pingOneSignals.initSilent({
                envId: "<envid>",
               behavioralDataCollection: false,
               deviceAttributesBlackList: []
           }).then(function ()
   ```

3. Add the following external script references to the sign-on page:

   |   |                                                   |
   | - | ------------------------------------------------- |
   |   | The scripts must be added in the following order. |

   ```
   <script type="text/javascript" src="signals-sdk-<version>.js"></script>
   <script type="text/javascript" src="pingone-risk-profiling-signals-sdk.js"></script>
   <script type="text/javascript" src="pingone-risk-management-embedded.js"></script>
   ```

4. **Optional:** Customize the device profile cookie name prefix to suit your environment.

   1. Open `pingone-risk-management-embedded.js` for editing.

   2. On the following line, change the value to a name of your choosing:

      ```
      var cookieNamePrefix = "pingone.risk.device.profile";
      ```

   3. Save the file.

5. When you complete the steps in [Configuring an adapter instance](pf_p1_risk_ik_configuring_an_adapter_instance.html), follow the instructions to set the **Device profiling method** to **Captured by a previous adapter**. Update the **Cookie Name Prefix** field if you customized it above.

## Adding device profiling to a browser-based authentication page using the PingOne Risk (Signals) SDK and integration kit 1.3 or earlier

### About this task

You can adapt these instructions to add device profiling to any page, such as the HTML Form Adapter or your web application. The page must meet the criteria listed in [Device profiling methods](pf_p1_risk_ik_device_profiling_methods.html).

### Steps

1. If you are modifying an external web application, copy the following files from the integration `.zip` archive to a location that your page can access.

   * `pingone-risk-profiling-signals-sdk.js`

   * `pingone-risk-management-embedded.js`

   * `signals-sdk.js`

2. Edit the `pingone-risk-profiling-signals-sdk.js` file and add your PingOne environment ID.

   |   |                                                                           |
   | - | ------------------------------------------------------------------------- |
   |   | The PingOne Risk SDK won't work if the PingOne environment ID is missing. |

   ```
   function profileDevice(callback) {
       // Initialize the SDK
       // replace <envid> with the PingOne console > Environment > Environment ID value
       onPingOneSignalsReady(function () {
           _pingOneSignals.initSilent({
                envId: "<envid>",
               deviceAttributesBlackList: []
           }).then(function ()
   ```

3. Add the following external script references to the sign-on page:

   |   |                                                   |
   | - | ------------------------------------------------- |
   |   | The scripts must be added in the following order. |

   ```
   <script type="text/javascript" src="signals-sdk.js"></script>
   <script type="text/javascript" src="pingone-risk-profiling-signals-sdk.js"></script>
   <script type="text/javascript" src="pingone-risk-management-embedded.js"></script>
   ```

4. **Optional:** Customize the device profile cookie name prefix to suit your environment.

   1. Open `pingone-risk-management-embedded.js` for editing.

   2. On the following line, change the value to a name of your choosing:

      ```
      var cookieNamePrefix = "pingone.risk.device.profile";
      ```

   3. Save the file.

5. When you complete the steps in [Configuring an adapter instance](pf_p1_risk_ik_configuring_an_adapter_instance.html), follow the instructions to set the **Device profiling method** to **Captured by a previous adapter**. Update the **Cookie Name Prefix** field if you customized it above.

## Adding device profiling to a browser-based authentication page using Fingerprint JS

### About this task

You can adapt these instructions to add device profiling to any page, such as the HTML Form Adapter or your web application. The page must meet the criteria listed in [Device profiling methods](pf_p1_risk_ik_device_profiling_methods.html).

|   |                                                                                                                                                           |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The PingOne Risk (Signals) SDK is the preferred way to get device profiling and is recommended for use in the PingOne Risk Integration Kit 1.3 and later. |

### Steps

1. If you are modifying an external web application, copy the following files from the integration `.zip` archive to a location that your page can access.

   * `fingerprint2-<version>.min.js`

   * `pingone-risk-management-profiling.js`

   * `pingone-risk-management-embedded.js`

2. Add the following external script references to the sign-on page.

   |   |                                                   |
   | - | ------------------------------------------------- |
   |   | The scripts must be added in the following order: |

   ```
   <script type="text/javascript" src="fingerprint2-<version>.min.js"></script>
   <script type="text/javascript" src="{file-prefix}-profiling.js"></script>
   <script type="text/javascript" src="{file-prefix}-embedded.js"></script>
   ```

3. Edit the `pingone-risk-management-embedded.js` file to use Fingerprint JS according to the comments in the file.

4. **Optional:** Customize the device profile cookie name prefix to suit your environment.

   1. Open `pingone-risk-management-embedded.js` for editing.

   2. On the following line, change the value to a name of your choosing:

      ```
      var cookieNamePrefix = "pingone.risk.device.profile";
      ```

   3. Save the file.

5. When you complete the steps in [Configuring an adapter instance](pf_p1_risk_ik_configuring_an_adapter_instance.html), follow the instructions to set the **Device profiling method** to **Captured by a previous adapter**. Update the **Cookie Name Prefix** field if you customized it above.

---

---
title: Adding device profiling to a browser-based authentication page using Fingerprint JS
description: You can adapt these instructions to add device profiling to any page, such as the HTML Form Adapter or your web application. The page must meet the criteria listed in Device profiling methods.
component: pingone
page_id: pingone:pingone_risk_integration_kit:pf_p1_risk_ik_adding_device_profiling_to_a_browser_based_authn_page_using_fingerprint_js
canonical_url: https://docs.pingidentity.com/integrations/pingone/pingone_risk_integration_kit/pf_p1_risk_ik_adding_device_profiling_to_a_browser_based_authn_page_using_fingerprint_js.html
llms_txt: https://docs.pingidentity.com/integrations/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 12, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Adding device profiling to a browser-based authentication page using Fingerprint JS

## About this task

You can adapt these instructions to add device profiling to any page, such as the HTML Form Adapter or your web application. The page must meet the criteria listed in [Device profiling methods](pf_p1_risk_ik_device_profiling_methods.html).

|   |                                                                                                                                                           |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The PingOne Risk (Signals) SDK is the preferred way to get device profiling and is recommended for use in the PingOne Risk Integration Kit 1.3 and later. |

## Steps

1. If you are modifying an external web application, copy the following files from the integration `.zip` archive to a location that your page can access.

   * `fingerprint2-<version>.min.js`

   * `pingone-risk-management-profiling.js`

   * `pingone-risk-management-embedded.js`

2. Add the following external script references to the sign-on page.

   |   |                                                   |
   | - | ------------------------------------------------- |
   |   | The scripts must be added in the following order: |

   ```
   <script type="text/javascript" src="fingerprint2-<version>.min.js"></script>
   <script type="text/javascript" src="{file-prefix}-profiling.js"></script>
   <script type="text/javascript" src="{file-prefix}-embedded.js"></script>
   ```

3. Edit the `pingone-risk-management-embedded.js` file to use Fingerprint JS according to the comments in the file.

4. **Optional:** Customize the device profile cookie name prefix to suit your environment.

   1. Open `pingone-risk-management-embedded.js` for editing.

   2. On the following line, change the value to a name of your choosing:

      ```
      var cookieNamePrefix = "pingone.risk.device.profile";
      ```

   3. Save the file.

5. When you complete the steps in [Configuring an adapter instance](pf_p1_risk_ik_configuring_an_adapter_instance.html), follow the instructions to set the **Device profiling method** to **Captured by a previous adapter**. Update the **Cookie Name Prefix** field if you customized it above.

---

---
title: Adding device profiling to a browser-based authentication page using the PingOne Risk (Signals) SDK and integration kit 1.3 or earlier
description: You can adapt these instructions to add device profiling to any page, such as the HTML Form Adapter or your web application. The page must meet the criteria listed in Device profiling methods.
component: pingone
page_id: pingone:pingone_risk_integration_kit:pf_p1_risk_ik_adding_device_profiling_to_a_browser_based_authn_page_using_p1risk_signals_sdk_and_ik_13_or_earlier
canonical_url: https://docs.pingidentity.com/integrations/pingone/pingone_risk_integration_kit/pf_p1_risk_ik_adding_device_profiling_to_a_browser_based_authn_page_using_p1risk_signals_sdk_and_ik_13_or_earlier.html
llms_txt: https://docs.pingidentity.com/integrations/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 12, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Adding device profiling to a browser-based authentication page using the PingOne Risk (Signals) SDK and integration kit 1.3 or earlier

## About this task

You can adapt these instructions to add device profiling to any page, such as the HTML Form Adapter or your web application. The page must meet the criteria listed in [Device profiling methods](pf_p1_risk_ik_device_profiling_methods.html).

## Steps

1. If you are modifying an external web application, copy the following files from the integration `.zip` archive to a location that your page can access.

   * `pingone-risk-profiling-signals-sdk.js`

   * `pingone-risk-management-embedded.js`

   * `signals-sdk.js`

2. Edit the `pingone-risk-profiling-signals-sdk.js` file and add your PingOne environment ID.

   |   |                                                                           |
   | - | ------------------------------------------------------------------------- |
   |   | The PingOne Risk SDK won't work if the PingOne environment ID is missing. |

   ```
   function profileDevice(callback) {
       // Initialize the SDK
       // replace <envid> with the PingOne console > Environment > Environment ID value
       onPingOneSignalsReady(function () {
           _pingOneSignals.initSilent({
                envId: "<envid>",
               deviceAttributesBlackList: []
           }).then(function ()
   ```

3. Add the following external script references to the sign-on page:

   |   |                                                   |
   | - | ------------------------------------------------- |
   |   | The scripts must be added in the following order. |

   ```
   <script type="text/javascript" src="signals-sdk.js"></script>
   <script type="text/javascript" src="pingone-risk-profiling-signals-sdk.js"></script>
   <script type="text/javascript" src="pingone-risk-management-embedded.js"></script>
   ```

4. **Optional:** Customize the device profile cookie name prefix to suit your environment.

   1. Open `pingone-risk-management-embedded.js` for editing.

   2. On the following line, change the value to a name of your choosing:

      ```
      var cookieNamePrefix = "pingone.risk.device.profile";
      ```

   3. Save the file.

5. When you complete the steps in [Configuring an adapter instance](pf_p1_risk_ik_configuring_an_adapter_instance.html), follow the instructions to set the **Device profiling method** to **Captured by a previous adapter**. Update the **Cookie Name Prefix** field if you customized it above.

---

---
title: Adding device profiling to a browser-based authentication page using the PingOne Risk (Signals) SDK with integration kit 1.3.1
description: You can adapt these instructions to add device profiling to any page, such as the HTML Form Adapter or your web application. The page must meet the criteria listed in Device profiling methods.
component: pingone
page_id: pingone:pingone_risk_integration_kit:pf_p1_risk_ik_adding_device_profiling_to_a_browser_based_authn_page_using_p1risk_signals_sdk_with_ik_131
canonical_url: https://docs.pingidentity.com/integrations/pingone/pingone_risk_integration_kit/pf_p1_risk_ik_adding_device_profiling_to_a_browser_based_authn_page_using_p1risk_signals_sdk_with_ik_131.html
llms_txt: https://docs.pingidentity.com/integrations/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 12, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Adding device profiling to a browser-based authentication page using the PingOne Risk (Signals) SDK with integration kit 1.3.1

## About this task

You can adapt these instructions to add device profiling to any page, such as the HTML Form Adapter or your web application. The page must meet the criteria listed in [Device profiling methods](pf_p1_risk_ik_device_profiling_methods.html).

|   |                                                                                                                                                                                 |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | PingOne Risk Integration Kit version 1.3.1 must be deployed before any changes can be made on the HTML side. SDK version 5.2 and later requires adapter version 1.3.1 or later. |

## Steps

1. If you are modifying an external web application, copy the following files from the integration `.zip` archive to a location that your page can access.

   * `pingone-risk-profiling-signals-sdk.js`

   * `pingone-risk-management-embedded.js`

   * `signals-sdk-<version>.js`

2. **Optional:** Edit the `pingone-risk-profiling-signals-sdk.js` file and add your PingOne environment ID.

   ```
   function profileDevice(callback) {
       // Initialize the SDK
       // replace <envid> with the PingOne console > Environment > Environment ID value
       onPingOneSignalsReady(function () {
           _pingOneSignals.initSilent({
                envId: "<envid>",
               behavioralDataCollection: false,
               deviceAttributesBlackList: []
           }).then(function ()
   ```

3. Add the following external script references to the sign-on page:

   |   |                                                   |
   | - | ------------------------------------------------- |
   |   | The scripts must be added in the following order. |

   ```
   <script type="text/javascript" src="signals-sdk-<version>.js"></script>
   <script type="text/javascript" src="pingone-risk-profiling-signals-sdk.js"></script>
   <script type="text/javascript" src="pingone-risk-management-embedded.js"></script>
   ```

4. **Optional:** Customize the device profile cookie name prefix to suit your environment.

   1. Open `pingone-risk-management-embedded.js` for editing.

   2. On the following line, change the value to a name of your choosing:

      ```
      var cookieNamePrefix = "pingone.risk.device.profile";
      ```

   3. Save the file.

5. When you complete the steps in [Configuring an adapter instance](pf_p1_risk_ik_configuring_an_adapter_instance.html), follow the instructions to set the **Device profiling method** to **Captured by a previous adapter**. Update the **Cookie Name Prefix** field if you customized it above.

---

---
title: Adding device profiling to an authentication API-based application
description: Use the following instructions to add device profiling to a web application using the PingOne Protect SDK. For more information about the authentication API, see Authentication API in the PingFederate documentation or PingOne Protect Native SDKs in the PingOne Native SDK documentation.
component: pingone
page_id: pingone:pingone_protect_integration_kit:pf_p1_protect_ik_adding_device_profiling_to_an_api_application
canonical_url: https://docs.pingidentity.com/integrations/pingone/pingone_protect_integration_kit/pf_p1_protect_ik_adding_device_profiling_to_an_api_application.html
llms_txt: https://docs.pingidentity.com/integrations/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 28, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
  choose-from: Choose from:
---

# Adding device profiling to an authentication API-based application

## About this task

Use the following instructions to add device profiling to a web application using the PingOne Protect SDK. For more information about the authentication API, see [Authentication API](https://docs.pingidentity.com/pingfederate/latest/developers_reference_guide/pf_authentication_api.html) in the PingFederate documentation or [PingOne Protect Native SDKs](http://apidocs.pingidentity.com/pingone/native-sdks/v1/api/#pingone-protect-native-sdks) in the PingOne Native SDK documentation.

## Steps

1. Implement the Signals SDK by following the steps in [PingOne Protect Native SDKs](https://apidocs.pingidentity.com/pingone/native-sdks/v1/api/#pingone-protect-native-sdks).

2. Configure functions to format the device profile and submit it to the authentication API. Use the following code sample as a guide.

   |   |                                                                                                                                                                                                                                                                                         |
   | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | The `pingone-protect-device-profiling.js` assumes you are using the web SDK. If using a mobile device and you want to send the `deviceProfile` check the [SDK documentation](http://apidocs.pingidentity.com/pingone/native-sdks/v1/api/#pingone-risk-native-sdks) and use accordingly. |

   ```
   function onCompletion(flowId, deviceProfile) {
   	submitDeviceProfile(flowId, deviceProfile);
   }

   function submitDeviceProfile(flowId, deviceProfile) {
   	var myHeaders = new Headers();
   	myHeaders.append("X-XSRF-Header", "test");
   	myHeaders.append("Content-Type", "application/vnd.pingidentity.submitDeviceProfile+json");
   ​
   	var raw = JSON.stringify({
       	"signalsSdkDeviceProfile": deviceProfile
   	});
   ​
   	var requestOptions = {
       	method: 'POST',
       	headers: myHeaders,
       	body: raw,
       	redirect: 'follow'
   	};
   ​
   	fetch("https://pf_host:pf_port/pf-ws/authn/flows/" + flowId, requestOptions)
       	.then(response => response.text())
       	.then(result => console.log(result))
       	.catch(error => console.log('error', error));
   }
   ```

   When the authentication API is in the `DEVICE_PROFILE_REQUIRED` state, your application should `submitDeviceProfile` with the value from the `profileDevice(callback)` method.

3. When you complete the steps in [Configuring an adapter instance](pf_p1_protect_ik_configuring_an_adapter_instance.html), set the device profiling method. The provider or the adapter can receive the payload sent by the authentication API.

   ### Choose from:

   * If the provider is configured, you must add the payload to the `checkUsernamePassword` `requestOptions` API call in the captchaResponse.

     ```json
     {
       "username": "string",
       "password": "string",
       "rememberMyUsername": "boolean",
       "thisIsMyDevice": "boolean",
       "captchaResponse": "string"
     }
     ```

   * When using the PingOne Protect IdP Adapter, submit the payload following the `submitDeviceProfile` `requestOptions` action of the authentication API.

     |   |                                                                                                                                                                                                                                     |
     | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
     |   | For more information on these options, see [Exploring the authentication API](https://docs.pingidentity.com/pingfederate/latest/developers_reference_guide/pf_exploring_authentication_api.html) in the PingFederate documentation. |

---

---
title: Adding device profiling to an authentication API-based application
description: If you are using the PingFederate authentication application programming interface (API) and want to avoid using HTTP cookies, modify your application to collect the device profile and send it to the authentication API.
component: pingone
page_id: pingone:pingone_risk_integration_kit:pf_p1_risk_ik_adding_device_profiling_to_an_authentication_api_based_application
canonical_url: https://docs.pingidentity.com/integrations/pingone/pingone_risk_integration_kit/pf_p1_risk_ik_adding_device_profiling_to_an_authentication_api_based_application.html
llms_txt: https://docs.pingidentity.com/integrations/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 12, 2024
section_ids:
  adding-device-profiling-to-an-authentication-api-based-application-using-the-pingone-risk-signals-sdk-and-integration-kit-1-3-1: Adding device profiling to an authentication API-based application using the PingOne Risk (Signals) SDK and integration kit 1.3.1
  about-this-task: About this task
  steps: Steps
  adding-device-profiling-to-an-authentication-api-based-application-using-the-pingone-risk-signals-sdk-and-integration-kit-1-3-or-earlier: Adding device profiling to an authentication API-based application using the PingOne Risk (Signals) SDK and integration kit 1.3 or earlier
  about-this-task-2: About this task
  steps-2: Steps
  adding-device-profiling-to-an-authentication-api-based-application-using-fingerprint-js: Adding device profiling to an Authentication API-based application using Fingerprint JS
  about-this-task-3: About this task
  steps-3: Steps
---

# Adding device profiling to an authentication API-based application

If you are using the PingFederate authentication application programming interface (API) *(tooltip: \<div class="paragraph">
\<p>A specification of interactions available for building software to access an application or service.\</p>
\</div>)* and want to avoid using HTTP cookies, modify your application to collect the device profile and send it to the authentication API.

## Adding device profiling to an authentication API-based application using the PingOne Risk (Signals) SDK and integration kit 1.3.1

### About this task

Use the following instructions to add device profiling to a web application using the PingOne Risk (Signals) SDK. Learn more about the authentication API in [Authentication API](https://docs.pingidentity.com/pingfederate/latest/developers_reference_guide/pf_authentication_api.html) in the PingFederate documentation or [PingOne Risk Native SDKs](http://apidocs.pingidentity.com/pingone/native-sdks/v1/api/#pingone-risk-native-sdks) in the PingOne Native SDK documentation.

|   |                                                                                                                                                                                  |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | PingOne Risk Integration Kit version 1.3.1 must be deployed before any changes can be made on the HTML side. SDK version 5.2.1 or later requires adapter version 1.3.1 or later. |

### Steps

1. Implement the Signals SDK by following the steps in [PingOne Risk Native SDKs](https://apidocs.pingidentity.com/pingone/native-sdks/v1/api/#pingone-risk-native-sdks).

2. Configure functions to format the device profile and submit it to the authentication API. Use the following code sample as a guide.

   |   |                                                                                                                                                                                                                                                                                           |
   | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | The `pingone-risk-profiling-signals-sdk.js` assumes you are using the web SDK. If using a mobile device and you want to send the `deviceProfile` check the [SDK documentation](http://apidocs.pingidentity.com/pingone/native-sdks/v1/api/#pingone-risk-native-sdks) and use accordingly. |

   ```
   function onCompletion(flowId, deviceProfile) {
   	submitDeviceProfile(flowId, deviceProfile);
   }

   function submitDeviceProfile(flowId, deviceProfile) {
   	var myHeaders = new Headers();
   	myHeaders.append("X-XSRF-Header", "test");
   	myHeaders.append("Content-Type", "application/vnd.pingidentity.submitDeviceProfile+json");
   ​
   	var raw = JSON.stringify({
       	"signalsSdkDeviceProfile": deviceProfile
   	});
   ​
   	var requestOptions = {
       	method: 'POST',
       	headers: myHeaders,
       	body: raw,
       	redirect: 'follow'
   	};
   ​
   	fetch("https://pf_host:pf_port/pf-ws/authn/flows/" + flowId, requestOptions)
       	.then(response => response.text())
       	.then(result => console.log(result))
       	.catch(error => console.log('error', error));
   }
   ```

   When the authentication API is in the `DEVICE_PROFILE_REQUIRED` state, your application should `submitDeviceProfile` with the value from the `profileDevice(callback)` method.

3. When you complete the steps in [Configuring an adapter instance](pf_p1_risk_ik_configuring_an_adapter_instance.html), set the **Device profiling method** to **Captured by previous adapter**.

## Adding device profiling to an authentication API-based application using the PingOne Risk (Signals) SDK and integration kit 1.3 or earlier

### About this task

Use the following instructions to add device profiling to a web application using the PingOne Risk (Signals) SDK. Learn more about the authentication API in [Authentication API](https://docs.pingidentity.com/pingfederate/latest/developers_reference_guide/pf_authentication_api.html) in the PingFederate documentation or [PingOne Risk Native SDKs](http://apidocs.pingidentity.com/pingone/native-sdks/v1/api/#pingone-risk-native-sdks) in the PingOne Native SDK documentation.

### Steps

1. Implement the Signals SDK by following the steps in [PingOne Risk Native SDKs](https://apidocs.pingidentity.com/pingone/native-sdks/v1/api/#pingone-risk-native-sdks).

2. Configure functions to format the device profile and submit it to the authentication API. Use the following code sample as a guide.

   |   |                                                                                                                                                                                                                                                                                           |
   | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | The `pingone-risk-profiling-signals-sdk.js` assumes you are using the web SDK. If using a mobile device and you want to send the `deviceProfile` check the [SDK documentation](http://apidocs.pingidentity.com/pingone/native-sdks/v1/api/#pingone-risk-native-sdks) and use accordingly. |

   ```
   function onCompletion(flowId, deviceProfile) {
   	submitDeviceProfile(flowId, deviceProfile);
   }

   function submitDeviceProfile(flowId, deviceProfile) {
   	var myHeaders = new Headers();
   	myHeaders.append("X-XSRF-Header", "test");
   	myHeaders.append("Content-Type", "application/vnd.pingidentity.submitDeviceProfile+json");
   ​
   	var raw = JSON.stringify({
       	"signalsSdkDeviceProfile": deviceProfile
   	});
   ​
   	var requestOptions = {
       	method: 'POST',
       	headers: myHeaders,
       	body: raw,
       	redirect: 'follow'
   	};
   ​
   	fetch("https://pf_host:pf_port/pf-ws/authn/flows/" + flowId, requestOptions)
       	.then(response => response.text())
       	.then(result => console.log(result))
       	.catch(error => console.log('error', error));
   }
   ```

   When the authentication API is in the `DEVICE_PROFILE_REQUIRED` state, your application should `submitDeviceProfile` with the value from the `profileDevice(callback)` method.

3. When you complete the steps in [Configuring an adapter instance](pf_p1_risk_ik_configuring_an_adapter_instance.html), set the **Device profiling method** to **Captured by previous adapter**.

## Adding device profiling to an Authentication API-based application using Fingerprint JS

### About this task

Use the following instructions to add device profiling to a web application using Fingerprint JS. Learn more about the authentication API in [Authentication API](https://docs.pingidentity.com/pingfederate/latest/developers_reference_guide/pf_authentication_api.html) in the PingFederate documentation.

|   |                                                                                                                                                           |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The PingOne Risk (Signals) SDK is the preferred way to get device profiling and is recommended for use in the PingOne Risk Integration Kit 1.3 and later. |

### Steps

1. Copy the following files from the integration `.zip` archive to your web server.

   * `fingerprint2-<version>.min.js`

   * `pingone-risk-management-profiling.js`

2. Add the following external script references to the sign-on page:

   |   |                                                   |
   | - | ------------------------------------------------- |
   |   | The scripts must be added in the following order. |

   ```
   <script type="text/javascript" src="fingerprint2-<version>.min.js"></script>
   <script type="text/javascript" src="{file-prefix}-profiling.js"></script>
   ```

3. Configure your application to call the `profileDevice(onCompletion)` function. This creates the device profile.

4. Configure functions to format the device profile and submit it to the authentication API. Use the following code sample as a guide.

   ```
   function onCompletion(flowId, components) {
       var deviceProfile = transformComponentsToDeviceProfile(components);
       submitDeviceProfile(flowId, deviceProfile);
   }
   ​
   function submitDeviceProfile(flowId, deviceProfile) {
       var myHeaders = new Headers();
       myHeaders.append("X-XSRF-Header", "test");
       myHeaders.append("Content-Type", "application/vnd.pingidentity.submitDeviceProfile+json");
   ​
       var raw = JSON.stringify({
           "deviceProfile": deviceProfile
       });
   ​
       var requestOptions = {
           method: 'POST',
           headers: myHeaders,
           body: raw,
           redirect: 'follow'
       };
   ​
       fetch("https://pf_host:pf_port/pf-ws/authn/flows/" + flowId, requestOptions)
           .then(response => response.text())
           .then(result => console.log(result))
           .catch(error => console.log('error', error));
   }
   ```

   When the authentication API is in the `DEVICE_PROFILE_REQUIRED` state, your application should `submitDeviceProfile` with a value structured as follows:

   ```html
   {
      "deviceProfile":{
         "userAgent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:82.0) Gecko/20100101 Firefox/82.0",
         "language":"en-CA",
         "colorDepth":24,
         "deviceMemory":null,
         "hardwareConcurrency":12,
         "screenResolution":[
            3440,
            1440
         ],
         "availableScreenResolution":[
            3440,
            1417
         ],
         "timezoneOffset":480,
         "timezone":"America/Los_Angeles",
         "sessionStorage":true,
         "localStorage":true,
         "indexedDb":true,
         "addBehaviour":false,
         "openDatabase":false,
         "cpuClass":null,
         "platform":"MacIntel",
         "plugins":[
         ],
         "webgl":[
            "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAASwAAACWCAYAAABkW7XSAAARYUlEQVR4nO3c30vcj57f8effUWg5F1
   		 [...]
   		 WEBGL_draw_buffers;WEBGL_lose_context",
            "webgl aliased line width range:[1, 1]",
            "webgl aliased point size range:[1, 8191]",
            [...]
            "webgl fragment shader low int precision rangeMin:24",
            "webgl fragment shader low int precision rangeMax:24"
         ],
         "webglVendorAndRenderer":"ATI Technologies Inc.~AMD Radeon Pro 560X OpenGL Engine",
         "adBlock":false,
         "hasLiedLanguages":false,
         "hasLiedResolution":false,
         "hasLiedOs":false,
         "hasLiedBrowser":false,
         "touchSupport":[
            "0",
            "false",
            "false"
         ],
         "fonts":[
            "Andale Mono",
            "Arial",
            [...]
            "Wingdings",
            "Wingdings 2",
            "Wingdings 3"
         ],
         "audio":"35.7383295930922"
      }
   }
   ```

5. When you complete the steps in [Configuring an adapter instance](pf_p1_risk_ik_configuring_an_adapter_instance.html), set the **Device profiling method** to **Captured by this adapter**.

---

---
title: Adding device profiling to an Authentication API-based application using Fingerprint JS
description: Use the following instructions to add device profiling to a web application using Fingerprint JS. Learn more about the authentication API in Authentication API in the PingFederate documentation.
component: pingone
page_id: pingone:pingone_risk_integration_kit:pf_p1_risk_ik_adding_device_profiling_to_an_authtication_api_based_app_using_fingerprint_js
canonical_url: https://docs.pingidentity.com/integrations/pingone/pingone_risk_integration_kit/pf_p1_risk_ik_adding_device_profiling_to_an_authtication_api_based_app_using_fingerprint_js.html
llms_txt: https://docs.pingidentity.com/integrations/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 12, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Adding device profiling to an Authentication API-based application using Fingerprint JS

## About this task

Use the following instructions to add device profiling to a web application using Fingerprint JS. Learn more about the authentication API in [Authentication API](https://docs.pingidentity.com/pingfederate/latest/developers_reference_guide/pf_authentication_api.html) in the PingFederate documentation.

|   |                                                                                                                                                           |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The PingOne Risk (Signals) SDK is the preferred way to get device profiling and is recommended for use in the PingOne Risk Integration Kit 1.3 and later. |

## Steps

1. Copy the following files from the integration `.zip` archive to your web server.

   * `fingerprint2-<version>.min.js`

   * `pingone-risk-management-profiling.js`

2. Add the following external script references to the sign-on page:

   |   |                                                   |
   | - | ------------------------------------------------- |
   |   | The scripts must be added in the following order. |

   ```
   <script type="text/javascript" src="fingerprint2-<version>.min.js"></script>
   <script type="text/javascript" src="{file-prefix}-profiling.js"></script>
   ```

3. Configure your application to call the `profileDevice(onCompletion)` function. This creates the device profile.

4. Configure functions to format the device profile and submit it to the authentication API. Use the following code sample as a guide.

   ```
   function onCompletion(flowId, components) {
       var deviceProfile = transformComponentsToDeviceProfile(components);
       submitDeviceProfile(flowId, deviceProfile);
   }
   ​
   function submitDeviceProfile(flowId, deviceProfile) {
       var myHeaders = new Headers();
       myHeaders.append("X-XSRF-Header", "test");
       myHeaders.append("Content-Type", "application/vnd.pingidentity.submitDeviceProfile+json");
   ​
       var raw = JSON.stringify({
           "deviceProfile": deviceProfile
       });
   ​
       var requestOptions = {
           method: 'POST',
           headers: myHeaders,
           body: raw,
           redirect: 'follow'
       };
   ​
       fetch("https://pf_host:pf_port/pf-ws/authn/flows/" + flowId, requestOptions)
           .then(response => response.text())
           .then(result => console.log(result))
           .catch(error => console.log('error', error));
   }
   ```

   When the authentication API is in the `DEVICE_PROFILE_REQUIRED` state, your application should `submitDeviceProfile` with a value structured as follows:

   ```html
   {
      "deviceProfile":{
         "userAgent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:82.0) Gecko/20100101 Firefox/82.0",
         "language":"en-CA",
         "colorDepth":24,
         "deviceMemory":null,
         "hardwareConcurrency":12,
         "screenResolution":[
            3440,
            1440
         ],
         "availableScreenResolution":[
            3440,
            1417
         ],
         "timezoneOffset":480,
         "timezone":"America/Los_Angeles",
         "sessionStorage":true,
         "localStorage":true,
         "indexedDb":true,
         "addBehaviour":false,
         "openDatabase":false,
         "cpuClass":null,
         "platform":"MacIntel",
         "plugins":[
         ],
         "webgl":[
            "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAASwAAACWCAYAAABkW7XSAAARYUlEQVR4nO3c30vcj57f8effUWg5F1
   		 [...]
   		 WEBGL_draw_buffers;WEBGL_lose_context",
            "webgl aliased line width range:[1, 1]",
            "webgl aliased point size range:[1, 8191]",
            [...]
            "webgl fragment shader low int precision rangeMin:24",
            "webgl fragment shader low int precision rangeMax:24"
         ],
         "webglVendorAndRenderer":"ATI Technologies Inc.~AMD Radeon Pro 560X OpenGL Engine",
         "adBlock":false,
         "hasLiedLanguages":false,
         "hasLiedResolution":false,
         "hasLiedOs":false,
         "hasLiedBrowser":false,
         "touchSupport":[
            "0",
            "false",
            "false"
         ],
         "fonts":[
            "Andale Mono",
            "Arial",
            [...]
            "Wingdings",
            "Wingdings 2",
            "Wingdings 3"
         ],
         "audio":"35.7383295930922"
      }
   }
   ```

5. When you complete the steps in [Configuring an adapter instance](pf_p1_risk_ik_configuring_an_adapter_instance.html), set the **Device profiling method** to **Captured by this adapter**.

---

---
title: Adding device profiling to an authentication API-based application using the PingOne Risk (Signals) SDK and integration kit 1.3 or earlier
description: Use the following instructions to add device profiling to a web application using the PingOne Risk (Signals) SDK. Learn more about the authentication API in Authentication API in the PingFederate documentation or PingOne Risk Native SDKs in the PingOne Native SDK documentation.
component: pingone
page_id: pingone:pingone_risk_integration_kit:pf_p1_risk_ik_adding_device_profiling_to_an_authtication_api_based_app_using_the_p1risk_signals_sdk_and_ik_13_or_earlier
canonical_url: https://docs.pingidentity.com/integrations/pingone/pingone_risk_integration_kit/pf_p1_risk_ik_adding_device_profiling_to_an_authtication_api_based_app_using_the_p1risk_signals_sdk_and_ik_13_or_earlier.html
llms_txt: https://docs.pingidentity.com/integrations/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 12, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Adding device profiling to an authentication API-based application using the PingOne Risk (Signals) SDK and integration kit 1.3 or earlier

## About this task

Use the following instructions to add device profiling to a web application using the PingOne Risk (Signals) SDK. Learn more about the authentication API in [Authentication API](https://docs.pingidentity.com/pingfederate/latest/developers_reference_guide/pf_authentication_api.html) in the PingFederate documentation or [PingOne Risk Native SDKs](http://apidocs.pingidentity.com/pingone/native-sdks/v1/api/#pingone-risk-native-sdks) in the PingOne Native SDK documentation.

## Steps

1. Implement the Signals SDK by following the steps in [PingOne Risk Native SDKs](https://apidocs.pingidentity.com/pingone/native-sdks/v1/api/#pingone-risk-native-sdks).

2. Configure functions to format the device profile and submit it to the authentication API. Use the following code sample as a guide.

   |   |                                                                                                                                                                                                                                                                                           |
   | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | The `pingone-risk-profiling-signals-sdk.js` assumes you are using the web SDK. If using a mobile device and you want to send the `deviceProfile` check the [SDK documentation](http://apidocs.pingidentity.com/pingone/native-sdks/v1/api/#pingone-risk-native-sdks) and use accordingly. |

   ```
   function onCompletion(flowId, deviceProfile) {
   	submitDeviceProfile(flowId, deviceProfile);
   }

   function submitDeviceProfile(flowId, deviceProfile) {
   	var myHeaders = new Headers();
   	myHeaders.append("X-XSRF-Header", "test");
   	myHeaders.append("Content-Type", "application/vnd.pingidentity.submitDeviceProfile+json");
   ​
   	var raw = JSON.stringify({
       	"signalsSdkDeviceProfile": deviceProfile
   	});
   ​
   	var requestOptions = {
       	method: 'POST',
       	headers: myHeaders,
       	body: raw,
       	redirect: 'follow'
   	};
   ​
   	fetch("https://pf_host:pf_port/pf-ws/authn/flows/" + flowId, requestOptions)
       	.then(response => response.text())
       	.then(result => console.log(result))
       	.catch(error => console.log('error', error));
   }
   ```

   When the authentication API is in the `DEVICE_PROFILE_REQUIRED` state, your application should `submitDeviceProfile` with the value from the `profileDevice(callback)` method.

3. When you complete the steps in [Configuring an adapter instance](pf_p1_risk_ik_configuring_an_adapter_instance.html), set the **Device profiling method** to **Captured by previous adapter**.

---

---
title: Adding device profiling to an authentication API-based application using the PingOne Risk (Signals) SDK and integration kit 1.3.1
description: Use the following instructions to add device profiling to a web application using the PingOne Risk (Signals) SDK. Learn more about the authentication API in Authentication API in the PingFederate documentation or PingOne Risk Native SDKs in the PingOne Native SDK documentation.
component: pingone
page_id: pingone:pingone_risk_integration_kit:pf_p1_risk_ik_adding_device_profiling_to_an_authtication_api_based_app_using_the_p1risk_signals_sdk_and_ik_131
canonical_url: https://docs.pingidentity.com/integrations/pingone/pingone_risk_integration_kit/pf_p1_risk_ik_adding_device_profiling_to_an_authtication_api_based_app_using_the_p1risk_signals_sdk_and_ik_131.html
llms_txt: https://docs.pingidentity.com/integrations/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 12, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Adding device profiling to an authentication API-based application using the PingOne Risk (Signals) SDK and integration kit 1.3.1

## About this task

Use the following instructions to add device profiling to a web application using the PingOne Risk (Signals) SDK. Learn more about the authentication API in [Authentication API](https://docs.pingidentity.com/pingfederate/latest/developers_reference_guide/pf_authentication_api.html) in the PingFederate documentation or [PingOne Risk Native SDKs](http://apidocs.pingidentity.com/pingone/native-sdks/v1/api/#pingone-risk-native-sdks) in the PingOne Native SDK documentation.

|   |                                                                                                                                                                                  |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | PingOne Risk Integration Kit version 1.3.1 must be deployed before any changes can be made on the HTML side. SDK version 5.2.1 or later requires adapter version 1.3.1 or later. |

## Steps

1. Implement the Signals SDK by following the steps in [PingOne Risk Native SDKs](https://apidocs.pingidentity.com/pingone/native-sdks/v1/api/#pingone-risk-native-sdks).

2. Configure functions to format the device profile and submit it to the authentication API. Use the following code sample as a guide.

   |   |                                                                                                                                                                                                                                                                                           |
   | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | The `pingone-risk-profiling-signals-sdk.js` assumes you are using the web SDK. If using a mobile device and you want to send the `deviceProfile` check the [SDK documentation](http://apidocs.pingidentity.com/pingone/native-sdks/v1/api/#pingone-risk-native-sdks) and use accordingly. |

   ```
   function onCompletion(flowId, deviceProfile) {
   	submitDeviceProfile(flowId, deviceProfile);
   }

   function submitDeviceProfile(flowId, deviceProfile) {
   	var myHeaders = new Headers();
   	myHeaders.append("X-XSRF-Header", "test");
   	myHeaders.append("Content-Type", "application/vnd.pingidentity.submitDeviceProfile+json");
   ​
   	var raw = JSON.stringify({
       	"signalsSdkDeviceProfile": deviceProfile
   	});
   ​
   	var requestOptions = {
       	method: 'POST',
       	headers: myHeaders,
       	body: raw,
       	redirect: 'follow'
   	};
   ​
   	fetch("https://pf_host:pf_port/pf-ws/authn/flows/" + flowId, requestOptions)
       	.then(response => response.text())
       	.then(result => console.log(result))
       	.catch(error => console.log('error', error));
   }
   ```

   When the authentication API is in the `DEVICE_PROFILE_REQUIRED` state, your application should `submitDeviceProfile` with the value from the `profileDevice(callback)` method.

3. When you complete the steps in [Configuring an adapter instance](pf_p1_risk_ik_configuring_an_adapter_instance.html), set the **Device profiling method** to **Captured by previous adapter**.

---

---
title: Adding PingOne MFA to your authentication policy
description: By modifying your PingFederate authentication policy to include the PingOne MFA IdP Adapter, you can challenge users to complete a multi-factor authentication (MFA) step.
component: pingone
page_id: pingone:pingone_mfa_integration_kit:pf_p1_mfa_ik_adding_p1_mfa_to_your_authentication_policy_4.0
canonical_url: https://docs.pingidentity.com/integrations/pingone/pingone_mfa_integration_kit/pf_p1_mfa_ik_adding_p1_mfa_to_your_authentication_policy_4.0.html
llms_txt: https://docs.pingidentity.com/integrations/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: March 18, 2025
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Adding PingOne MFA to your authentication policy

By modifying your PingFederate authentication policy to include the PingOne MFA IdP Adapter, you can challenge users to complete a multi-factor authentication (MFA) step.

## About this task

These steps are designed to help you add to an existing authentication policy. You can find more information about configuring authentication policies in [Authentication policies](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_authentication_policies.html) in the PingFederate documentation.

|   |                                                                                                                                                                                                                 |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | **Changes in Version 4.0:**- **Attribute Mapping:** The `id_token` and `access_token` core contracts are removed. You must manually update policies to use `pingone.mfa.enrollment` or `pingone.mfa.device.id`. |

## Steps

1. In the PingFederate administrative console, go to **Authentication > Policies > Policies**.

2. Select the **IdP Authentication Policies** checkbox.

3. Open an existing authentication policy, or click **Add Policy**.

   Learn more in [Defining authentication policies](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_defining_auth_policies.html) in the PingFederate documentation.

4. In the **Policy** area, in the **Select** list, select a PingOne MFA IdP Adapter instance.

   |   |                                                                                                         |
   | - | ------------------------------------------------------------------------------------------------------- |
   |   | In the adapter configuration, ensure a selection is made in the **MFA Policy for Authentication** list. |

   ![Adding the to the authentication policy](_images/zcr1599149554163.jpg)

5. Map the PingOne user ID or username into the PingOne MFA IdP Adapter instance.

   |   |                                                                                                                                                                                                                                                                                                            |
   | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | In version 4.0, the PingOne MFA IdP Adapter returns claims directly in the attribute map. To avoid errors, you must set the **Source** to **Adapter**.Attributes include:- `pingone.mfa.enrollment`

   - `pingone.mfa.device.id`You can use these attributes to define additional policy rules and branches. |

   ![Passing the user ID from the first-factor authentication adapter to the](_images/dnb1651867080726.png)

   1. Under the PingOne MFA IdP Adapter instance, click **Options**.

   2. In the **Options** modal, in the **Source** list, select a previous authentication source that collects the PingOne user ID or username.

      |   |                                                                                                                                                                                                                                                                                                                     |
      | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      |   | The adapter uses the **Username Attribute** value as the username when provisioning new users.In version 4.0, the **User Not Found** failure mode only applies if a user does not exist in the directory. It no longer covers disabled users or users with the MFA service disabled, as it did in earlier versions. |

   3. In the **Attribute** list, select the user ID. Click **Done**.

   4. (Optional) Select the **User ID Authenticated** checkbox.

      |   |                                                                                                                                                                                                                                                             |
      | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      |   | The **User ID Authenticated** checkbox indicates whether the mapped user ID has been authenticated by the authentication source and therefore can be trusted by the current adapter. Device management options are limited if the user isn't authenticated. |

6. (Optional) Define policy paths based on the `pingone.mfa.status` or `pingone.mfa.status.reason` attributes.

   ![Branching the authentication policy based on the pingone.mfa.status attribute.](_images/dxf1601405103816.jpg)

   1. Under the PingOne MFA IdP Adapter instance, click **Rules**.

   2. In the **Rules** modal, in the **Attribute Name** list, select **pingone.mfa.status** or **pingone.mfa.status.reason**.

   3. In the **Condition** list, select **equal to**.

   4. In the **Value** field, enter a value from [PingOne MFA attributes reference](pf_p1_mfa_ik_p1_mfa_status_attributes_reference_4.0.html).

   5. In the **Result** field, enter a name. This appears as a new policy path that branches from the authentication source.

   6. If you want to add more authentication paths, click **Add** and repeat steps a-e.

   7. Click **Done**.

7. Configure each of the authentication paths.

   ![The complete authentication policy](_images/xxp1599151225895.jpg)

8. Click **Done**.

9. Configure tracked HTTP parameters:

   1. On the **Tracked HTTP Parameters** tab, in the **Parameter Name** field, enter the name of the parameter that you want to track.

      For example:

      * To enable automatic device pairing, enter `mobilePayload`.

   2. Click **Add**.

   3. Click **Save**.

   4. Repeat the previous steps for any other parameters that you want to add.

---

---
title: Adding PingOne MFA to your authentication policy
description: By modifying your PingFederate authentication policy to include the PingOne MFA IdP Adapter, you can challenge users to complete a multi-factor authentication (MFA) step.
component: pingone
page_id: pingone:pingone_mfa_integration_kit_3.2:pf_p1_mfa_ik_adding_p1_mfa_to_your_authentication_policy
canonical_url: https://docs.pingidentity.com/integrations/pingone/pingone_mfa_integration_kit_3.2/pf_p1_mfa_ik_adding_p1_mfa_to_your_authentication_policy.html
llms_txt: https://docs.pingidentity.com/integrations/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: March 18, 2025
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Adding PingOne MFA to your authentication policy

By modifying your PingFederate authentication policy to include the PingOne MFA IdP Adapter, you can challenge users to complete a multi-factor authentication (MFA) step.

## About this task

These steps are designed to help you add to an existing authentication policy. You can find more information about configuring authentication policies in [Authentication policies](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_authentication_policies.html) in the PingFederate documentation.

## Steps

1. In the PingFederate administrative console, go to **Authentication > Policies > Policies**.

2. Select the **IdP Authentication Policies** checkbox.

3. Open an existing authentication policy, or click **Add Policy**.

   Learn more in [Defining authentication policies](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_defining_auth_policies.html) in the PingFederate documentation.

4. In the **Policy** area, in the **Select** list, select a PingOne MFA IdP Adapter instance.

   ![Adding the to the authentication policy](_images/zcr1599149554163.jpg)

5. Map the PingOne user ID or username into the PingOne MFA IdP Adapter instance.

   ![Passing the user ID from the first-factor authentication adapter to the](_images/dnb1651867080726.png)

   1. Under the PingOne MFA IdP Adapter instance, click **Options**.

   2. In the **Options** modal, in the **Source** list, select a previous authentication source that collects the PingOne user ID or username.

      |   |                                                                                                                                                                                            |
      | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
      |   | If you left the **Username Attribute** field blank in your PingOne MFA IdP Adapter configuration, the adapter also uses this value as the username when provisioning new users to PingOne. |

   3. In the **Attribute** list, select the user ID. Click **Done**.

   4. (Optional) Select the **User ID Authenticated** checkbox.

      |   |                                                                                                                                                                                                                                                             |
      | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      |   | The **User ID Authenticated** checkbox indicates whether the mapped user ID has been authenticated by the authentication source and therefore can be trusted by the current adapter. Device management options are limited if the user isn't authenticated. |

6. (Optional) Define policy paths based on the `pingone.mfa.status` or `pingone.mfa.status.reason` attributes.

   ![Branching the authentication policy based on the pingone.mfa.status attribute.](_images/dxf1601405103816.jpg)

   1. Under the PingOne MFA IdP Adapter instance, click **Rules**.

   2. In the **Rules** modal, in the **Attribute Name** list, select **pingone.mfa.status** or **pingone.mfa.status.reason**.

   3. In the **Condition** list, select **equal to**.

   4. In the **Value** field, enter a value from [PingOne MFA attributes reference](pf_p1_mfa_ik_p1_mfa_status_attributes_reference.html).

   5. In the **Result** field, enter a name. This appears as a new policy path that branches from the authentication source.

   6. If you want to add more authentication paths, click **Add** and repeat steps a-e.

   7. Click **Done**.

7. Configure each of the authentication paths.

   ![The complete authentication policy](_images/xxp1599151225895.jpg)

8. Click **Done**.

9. Configure tracked HTTP parameters:

   1. On the **Tracked HTTP Parameters** tab, in the **Parameter Name** field, enter the name of the parameter that you want to track.

      For example:

      * To enable automatic device pairing, enter `mobilePayoad`.

      * To configure the PingOne MFA IdP Adapter to support the prompt parameter, enter `prompt`.

   2. Click **Add**.

   3. Click **Save**.

   4. Repeat the previous steps for any other parameters that you want to add.

---

---
title: Adding PingOne Verify to your authentication policy
description: By modifying your PingFederate authentication policy to include the PingOne Verify IdP Adapter, you can challenge users to verify their identity as part of the authentication process.
component: pingone
page_id: pingone:pingone_verify_integration_kit:pf_p1_verify_ik_adding_p1_verify_to_your_authentication_policy
canonical_url: https://docs.pingidentity.com/integrations/pingone/pingone_verify_integration_kit/pf_p1_verify_ik_adding_p1_verify_to_your_authentication_policy.html
llms_txt: https://docs.pingidentity.com/integrations/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: August 2, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Adding PingOne Verify to your authentication policy

By modifying your PingFederate authentication policy to include the PingOne Verify IdP Adapter, you can challenge users to verify their identity as part of the authentication process.

## About this task

Use these steps to add to an existing authentication policy. You can find general information about configuring authentication policies in [Authentication policies](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_authentication_policies.html) in the PingFederate documentation.

## Steps

1. In the PingFederate administrative console, go to **Authentication > Policies > Policies**.

2. On the **Policies** tab, select the **IdP Authentication Policies** checkbox.

3. Open an existing authentication policy, or click **Add Policy**.

   You can find more information in [Defining authentication policies](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_defining_auth_policies.html) in the PingFederate documentation.

4. In the **Policy** section, in the **Select** list, select a PingOne Verify IdP Adapter instance.

   ![Adding the to the authentication policy](../_images/gvz1607722317720.jpg)

5. Map the PingOne `user ID` or `username` into the PingOne Verify IdP Adapter instance.

   ![Passing the user ID from the first-factor authentication adapter to the](../_images/mar1607722605939.jpg)

   1. Under the PingOne Verify IdP Adapter instance, click **Options**.

   2. On the **Options** window, in the **Source** list, select a previous authentication source that collects the PingOne user ID or username.

   3. In the **Attribute** list, select the user ID.

   4. Select the **User ID Authenticated** checkbox.

   5. Click **Done**.

6. (Optional) Define policy paths based on verification results.

   |   |                                                                                                                                                                                                                                                                                                                                               |
   | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | Depending on the failure mode settings in your adapter configuration, the adapter can potentially return a `success` result in the authentication policy even when the user verification process did not succeed. It can be useful to create separate policy paths for a successful adapter result and a successful user verification result. |

   ![Screen shot that shows the Rules dialog in the authentication policy with two paths configured based on the transactionStatus attribute.](../_images/vne1610049349809.png)

   1. Under the PingOne Verify IdP Adapter instance, click **Rules**.

   2. On the **Rules** window, in the **Attribute Name** list, select **transactionStatus**.

   3. In the **Condition** list, select **equal to**.

   4. In the **Value** field, enter `SUCCESS` or `BYPASS`.

      * SUCCESS

        The user successfully verified their identity.

      * BYPASS

        An error occurred, and the verification process was not completed, but the adapter is configured to bypass verification and continue the authentication flow.

   5. In the **Result** field, enter a name.

      This appears as a new policy path that branches from the authentication source.

   6. To add more authentication paths, click **Add** and repeat steps a-e.

   7. Click **Done**.

7. Configure each of the authentication paths, including **Fail**, **Success**, and any paths that you defined in the **Rules** window.

   ![The complete authentication policy](../_images/pji1607722789395.jpg)

8. Click **Done**.

9. In the **Policies** window, click **Save**.

---

---
title: Adding PingOne Verify to your authentication policy
description: By modifying your PingFederate authentication policy to include the PingOne Verify IdP Adapter, you can challenge users to verify their identity as part of the authentication process.
component: pingone
page_id: pingone:pingone_verify_integration_kit_11:pf_p1_verify_ik_adding_p1_verify_to_your_authentication_policy_11
canonical_url: https://docs.pingidentity.com/integrations/pingone/pingone_verify_integration_kit_11/pf_p1_verify_ik_adding_p1_verify_to_your_authentication_policy_11.html
llms_txt: https://docs.pingidentity.com/integrations/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: August 2, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
  choose-from: Choose from:
---

# Adding PingOne Verify to your authentication policy

By modifying your PingFederate authentication policy to include the PingOne Verify IdP Adapter, you can challenge users to verify their identity as part of the authentication process.

## About this task

Use these steps to add to an existing authentication policy. You can find general information about configuring authentication policies in [Authentication policies](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_authentication_policies.html) in the PingFederate documentation.

## Steps

1. In the PingFederate administrative console, go to the **Policies** tab.

   ### Choose from:

   * For PingFederate 10.1 or later: go to **Authentication > Policies > Policies**.

   * For PingFederate 10.0 or earlier: go to **Identity Provider > Authentication Policies > Policies**.

2. Select the **IdP Authentication Policies** checkbox.

3. Open an existing authentication policy, or click **Add Policy**.

   For more information, see [Defining authentication policies](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_defining_auth_policies.html) in the PingFederate documentation.

4. In the **Policy** section, in the **Select** list, select a PingOne Verify IdP Adapter instance.

   ![Adding the to the authentication policy](../_images/gvz1607722317720.jpg)

5. Map the PingOne `user ID` or `username` into the PingOne Verify IdP Adapter instance.

   ![Passing the user ID from the first-factor authentication adapter to the](../_images/mar1607722605939.jpg)

   1. Under the PingOne Verify IdP Adapter instance, click **Options**.

   2. On the **Options** window, in the **Source** list, select a previous authentication source that collects the PingOne user ID or username.

   3. In the **Attribute** list, select the user ID.

   4. For PingFederate 10.2 and later, select the **User ID Authenticated** checkbox.

   5. Click **Done**.

6. **Optional:** Define policy paths based on verification results.

   |   |                                                                                                                                                                                                                                                                                                                                               |
   | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | Depending on the failure mode settings in your adapter configuration, the adapter can potentially return a `success` result in the authentication policy even when the user verification process did not succeed. It can be useful to create separate policy paths for a successful adapter result and a successful user verification result. |

   ![Screen shot that shows the Rules dialog in the authentication policy with two paths configured based on the transactionStatus attribute.](../_images/vne1610049349809.png)

   1. Under the PingOne Verify IdP Adapter instance, click **Rules**.

   2. On the **Rules** window, in the **Attribute Name** list, select **transactionStatus**.

   3. In the **Condition** list, select **equal to**.

   4. In the **Value** field, enter `SUCCESS` or `BYPASS`.

      * SUCCESS

        The user successfully verified their identity.

      * BYPASS

        An error occurred, and the verification process was not completed, but the adapter is configured to bypass verification and continue the authentication flow.

   5. In the **Result** field, enter a name.

      This appears as a new policy path that branches from the authentication source.

   6. To add more authentication paths, click **Add** and repeat steps a-e.

   7. Click **Done**.

7. Configure each of the authentication paths, including **Fail**, **Success**, and any paths that you defined in the **Rules** window.

   ![The complete authentication policy](../_images/pji1607722789395.jpg)

8. Click **Done**.

9. In the **Policies** window, click **Save**.

---

---
title: Adding PingOne Verify to your user registration flow
description: By modifying your PingFederate authentication policy to include the PingOne Verify IdP Adapter policy fragment, you can challenge users to verify their identity as part of the self-service registration process.
component: pingone
page_id: pingone:pingone_verify_integration_kit:pf_p1_verify_ik_adding_p1_verify_user_registration_flow
canonical_url: https://docs.pingidentity.com/integrations/pingone/pingone_verify_integration_kit/pf_p1_verify_ik_adding_p1_verify_user_registration_flow.html
llms_txt: https://docs.pingidentity.com/integrations/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: August 6, 2026
section_ids:
  steps: Steps
---

# Adding PingOne Verify to your user registration flow

By modifying your PingFederate authentication policy to include the PingOne Verify IdP Adapter policy fragment, you can challenge users to verify their identity as part of the self-service registration process.

## Steps

1. In the PingFederate administrative console, go to **Authentication > Policies > Policies**.

2. Select the **IdP Authentication Policies** checkbox.

3. Open the authentication policy that you created in your initial registration configuration.

4. In the **Policy** area, define a policy path for user registration.

   1. Under the HTML Form Adapter instance, click **Rules**.

   2. On the **Rules** dialog, from the **Attribute Name** list, select **policy.action**.

   3. In the **Condition** list, select **equal to**.

   4. In the **Value** field, enter `identity.registration`.

   5. In the **Result** field, enter a name, such as `Registration`.

      This appears as a new policy path that branches from the HTML Form Adapter.

   6. Click **Done**.

5. After the HTML Form Adapter instance, for the **Fail** path, select **Done**.

6. After the HTML Form Adapter instance, for the **Registration** path, select the local identity profile that you created for PingOne Verify.

   1. Click **Local Identity Mapping**.

   2. On the **Inbound Mapping** tab, map the registration form fields to the input policy contract attributes.

      **Table 1. Example mappings**

      | Inbound Mapping Fulfillment | Value                   |
      | --------------------------- | ----------------------- |
      | `firstName`                 | `regFirstName`          |
      | `email`                     | `registrar@example.com` |

   3. On the **Contract Fulfillment** tab, map values for the outbound contract.

      | Outbound Mapping Fulfillment | Source                                   | Value       |
      | ---------------------------- | ---------------------------------------- | ----------- |
      | `attr1`                      | Local Identity (Verify Identity Profile) | `email`     |
      | `subject`                    | Local Identity (Verify Identity Profile) | `firstName` |

   4. Click **Done**.

7. After the HTML Form Adapter instance, for the **Success** path, configure the standard (non-registration) authentication path.

8. Click **Done**.

9. In the **Policies** window, click **Save**.

---

---
title: Adding PingOne Verify to your user registration flow
description: By modifying your PingFederate authentication policy to include the PingOne Verify IdP Adapter policy fragment, you can challenge users to verify their identity as part of the self-service registration process.
component: pingone
page_id: pingone:pingone_verify_integration_kit_11:pf_p1_verify_ik_adding_p1_verify_to_your_user_registration_flow_11
canonical_url: https://docs.pingidentity.com/integrations/pingone/pingone_verify_integration_kit_11/pf_p1_verify_ik_adding_p1_verify_to_your_user_registration_flow_11.html
llms_txt: https://docs.pingidentity.com/integrations/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 3, 2024
section_ids:
  steps: Steps
---

# Adding PingOne Verify to your user registration flow

By modifying your PingFederate authentication policy to include the PingOne Verify IdP Adapter policy fragment, you can challenge users to verify their identity as part of the self-service registration process.

## Steps

1. In the PingFederate administrative console, go to **Authentication > Policies > Policies**.

2. Select the **IdP Authentication Policies** checkbox.

3. Open the authentication policy that you created in your initial registration configuration.

4. In the **Policy** area, define a policy path for user registration.

   1. Under the HTML Form Adapter instance, click **Rules**.

   2. On the **Rules** dialog, in the **Attribute Name** list, select **policy.action**.

   3. In the **Condition** list, select **equal to**.

   4. In the **Value** field, enter `identity.registration`.

   5. In the **Result** field, enter a name, such as `Registration`. This appears as a new policy path that branches from the PingOne Verify IdP Adapter.

   6. Click **Done**.

5. After the HTML Form Adapter instance, for the **Fail** path, select **Done**.

6. After the HTML Form Adapter instance, for the **Registration** path, select the local identity profile that you created for PingOne Verify.

   1. Click **Local Identity Mapping**.

   2. On the **Inbound Mapping** tab, map the registration form fields to the input policy contract attributes.

      **Table 1. Example mappings**

      | Inbound Mapping Fulfillment | Value                  |
      | --------------------------- | ---------------------- |
      | firstName                   | regFirstName           |
      | email                       | registrar\@example.com |

   3. On the **Contract Fulfillment** tab, map values for the outbound contract.

      **Table 2. Example mappings**

      | Outbound Mapping Fulfillment | Source                                   | Value     |
      | ---------------------------- | ---------------------------------------- | --------- |
      | attr1                        | Local Identity (Verify Identity Profile) | email     |
      | subject                      | Local Identity (Verify Identity Profile) | firstName |

   4. Click **Done**.

7. After the HTML Form Adapter instance, for the **Success** path, configure the standard (non-registration) authentication path.

8. Click **Done**.

9. In the **Policies** window, click **Save**.