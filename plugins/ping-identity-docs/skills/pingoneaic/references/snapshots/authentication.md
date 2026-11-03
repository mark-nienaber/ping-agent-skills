---
title: Android Key Attestation settings
description: Configure Android Key Attestation to validate Android device integrity during authentication using hardware-backed key attestation
component: pingoneaic
page_id: pingoneaic:authentication:authentication-methods-android-key-attestation
canonical_url: https://docs.pingidentity.com/pingoneaic/authentication/authentication-methods-android-key-attestation.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Android Key Attestation", "device trust", "attestation"]
page_aliases: ["authentication:identity-verification-android-key-attestation.adoc"]
section_ids:
  configure-android-key-attestation: Configure Android Key Attestation settings
---

# Android Key Attestation settings

Android Key Attestation is an optional device binding feature for Android devices. It lets Advanced Identity Cloud verify that the keys used by a bound device are valid, haven't been revoked, and are stored in hardware-backed security storage.

This feature only applies when a journey uses the [Device Binding node](https://docs.pingidentity.com/auth-node-ref/latest/device-binding.html) with Android Key Attestation enabled. It applies to devices running Android N (24) or later. Advanced Identity Cloud doesn't perform attestation for non-Android devices, and Android Key Attestation isn't supported when the Device Binding node uses the `Application PIN` Authentication Type.

When Android Key Attestation is enabled, Advanced Identity Cloud verifies the device's attestation certificate chain using Google's hardware attestation root certificates and certificate revocation status information.

## Configure Android Key Attestation settings

1. In the Advanced Identity Cloud admin console, go to [icon: verified_user, set=material, size=inline] Authentication > Authentication Methods.

2. Click Android Key Attestation.

3. If the configuration is not already enabled, click Enable Android Key Attestation to create it with default settings before configuring it.

4. Configure the following settings:

   * Certificate revocation status list URL

     The URL to retrieve the certificate revocation status list (CRL).

     Keys are checked against the revocation status list to ensure they haven't been revoked or suspended. They can be revoked for a number of reasons, including mishandling or suspected extraction by an attacker.

     Defaults to `https://android.googleapis.com/attestation/status` (a list maintained by Google).

   * Google hardware attestation root certificate URL

     The URL for retrieving the Google hardware attestation root certificates. Learn more in [Verifying hardware-backed key pairs with Key Attestation](https://developer.android.com/training/articles/security-key-attestation#root_certificate) in the Android developer documentation.

     If you don't provide a URL, you must map the certificate using the secret label `am.services.attestation.google.public.key`. Learn more in [Use ESVs for signing and encryption keys](../tenants/esvs-signing-encryption.html).

5. Click Save.

---

---
title: Configure authentication methods
description: Configure authentication methods for MFA and device-based authentication, including push notifications, one-time passcodes, WebAuthn, and device binding
component: pingoneaic
page_id: pingoneaic:authentication:authentication-methods
canonical_url: https://docs.pingidentity.com/pingoneaic/authentication/authentication-methods.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Authentication", "Multi-factor Authentication (MFA)", "Push", "WebAuthn", "TOTP", "OATH", "Device Binding", "passkey"]
section_ids:
  common_use_cases: Common use cases
  configure_an_authentication_method: Configure an authentication method
  delete_an_authentication_method_configuration: Delete an authentication method configuration
---

# Configure authentication methods

Authentication methods provide the configuration that authentication journeys use to store device metadata, send push notifications, and verify authenticators. Before end users can use an authentication method in a journey, configure the relevant settings for the realm where the journey runs.

The default configuration lets you get started quickly, but make sure you review these values before they are used in production.

Learn more about MFA in [Multi-factor authentication (MFA)](../am-authentication/authn-mfa.html).

## Common use cases

* Push notifications for MFA

  Let end users approve sign on using a push notification on their mobile device. To enable this feature, you must configure two separate authentication methods:

  * Push Authentication, which manages how user devices are registered.

  * Push Notification Delivery, which configures how Advanced Identity Cloud sends push notifications.

  Learn more in [Push authentication settings](authentication-methods-push-authentication.html) and [Push notification delivery settings](authentication-methods-push-notification.html).

* TOTPs from an authenticator app

  Let end users authenticate with a time-based one-time passcode (TOTP) from an authenticator app. To enable this feature, configure the One-time Passcode (TOTP) authentication method to control how Advanced Identity Cloud stores OATH device profiles and, optionally, to encrypt that data.

  Learn more in [One-time passcode (TOTP) settings](authentication-methods-totp.html).

* Passkeys and WebAuthn

  Let end users authenticate with passkeys or WebAuthn. To enable this feature, configure the following authentication methods:

  * WebAuthn Verification to specify the `FIDO Metadata Service` endpoint Advanced Identity Cloud uses to validate authenticator attestations.

  * WebAuthn Storage & Encryption to control how Advanced Identity Cloud stores WebAuthn device profiles.

  Learn more in [WebAuthn verification settings](authentication-methods-webauthn-verification.html) and [WebAuthn storage & encryption settings](authentication-methods-webauthn-encryption.html).

* Device binding

  Associate trusted devices with end user identities, for example to support step-up or risk-based authentication. To enable this feature, configure the Device Binding authentication method to control how bound device data is stored and encrypted.

  If you use Android key attestation, also configure the Android Key Attestation settings.

  Learn more in [Device binding settings](authentication-methods-device-binding.html) and [Android Key Attestation settings](authentication-methods-android-key-attestation.html).

## Configure an authentication method

1. In the Advanced Identity Cloud admin console, go to [icon: verified_user, set=material, size=inline] Authentication > Authentication Methods.

   The page lists each authentication method and its current status.

2. Click the row for the method you want to configure.

   If the authentication method isn't enabled yet, click Enable *authentication-method-name* to create it with default settings before configuring it.

3. Update the settings and click Save.

## Delete an authentication method configuration

Deleting the authentication method configuration removes its settings.

1. In the Advanced Identity Cloud admin console, go to [icon: verified_user, set=material, size=inline] Authentication > Authentication Methods.

2. Click the row for the authentication method configuration you want to delete.

3. At the bottom of the page, click Delete *authentication-method-name*.

---

---
title: Configure basic social registration journeys
description: Configure basic Advanced Identity Cloud social authentication journeys, including account claiming and linking social accounts from the profile page
component: pingoneaic
page_id: pingoneaic:authentication:social-authentication-journeys
canonical_url: https://docs.pingidentity.com/pingoneaic/authentication/social-authentication-journeys.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Journeys", "Nodes &amp; Trees", "Social Authentication", "OAuth 2.0", "OpenID Connect (OIDC)"]
section_ids:
  social_identity_provider_nodes: Social identity provider nodes
  basic-reg-journey: Configure a social registration journey
  enforce-social-registration: Enforce social registration
  account-claiming: Configure social registration with account claiming
  social-auth-connect-through-profile: Let end users connect through their profile page
---

# Configure basic social registration journeys

Social registration journeys let end users register and sign on to your applications using their existing accounts from providers such as Google or Facebook. This offers a convenient experience for end users, as they don't need to create and remember a new password.

This page shows you how to build a basic social registration journey, configure account claiming for end users who might already have a local account, and let end users link their social accounts from their profile page.

|   |                                                                                                                                                                                                                                                                                                                                                                                          |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The [Ping Identity Marketplace](https://marketplace.pingone.com/item/login-with-self-service-journey) includes a prebuilt [Login with self-service](../journeys/solution-login-with-self-service-journey.html) journey. This sample journey lets end users sign on using a social identity provider or the username and password of an account in the Advanced Identity Cloud datastore. |

## Social identity provider nodes

There are two nodes associated with social identity providers:

* Select Identity Provider node

  The [Select Identity Provider node](https://docs.pingidentity.com/auth-node-ref/latest/select-identity-provider.html) prompts the end user to select a social identity provider for registration or sign on or (optionally) to continue with local registration or sign on.

  When the end user selects a provider, the journey continues to the [Social Provider Handler node](https://docs.pingidentity.com/auth-node-ref/latest/social-provider-handler.html).

* Social Provider Handler node

  The [Social Provider Handler node](https://docs.pingidentity.com/auth-node-ref/latest/social-provider-handler.html) communicates with the selected provider and collects the information provided after the end user has authorized the service. It runs the provider's configured *normalization* script to map the information into a format that Advanced Identity Cloud can consume.

  Next, the node uses a *transformation* script provided by Advanced Identity Cloud called `Normalized Profile to Managed User` to transform the profile information into a managed object.

  The node then queries the identity store available for the realm to check whether the end user already exists. If the end user exists, they are signed on. If the end user doesn't exist, the end user must be created.

## Configure a social registration journey

In a basic social registration journey, the end user can register with a social identity provider and create a local account in Advanced Identity Cloud.

To create a social registration journey:

1. In the Advanced Identity Cloud admin console, go to Journeys > Journeys.

   You can create a new journey, modify an existing journey, or duplicate an existing journey.

2. Add the nodes shown in the following journey and configure them as described.

   ![Example social registration with local authentication](_images/social-registration-with-local.png)

   > **Collapse: Page node (initial)**
   >
   > Learn more in [Page node](https://docs.pingidentity.com/auth-node-ref/latest/page.html).
   >
   > * Location:
   >
   >   * Add a Page node at the start of the journey and add the following nodes: [Platform Username node](https://docs.pingidentity.com/auth-node-ref/latest/platform-username.html), [Platform Password node](https://docs.pingidentity.com/auth-node-ref/latest/platform-password.html), and [Select Identity Provider node](https://docs.pingidentity.com/auth-node-ref/latest/select-identity-provider.html).
   >
   > * Connections:
   >
   >   * Connect the Start node to this Page node.
   >
   >   * Connect the Social Authentication outcome to the Social Provider Handler node.
   >
   >   * Connect Outcome to the Data Store Decision node.
   >
   > * Configuration:
   >
   >   * By default, the [Select Identity Provider node](https://docs.pingidentity.com/auth-node-ref/latest/select-identity-provider.html) supports both local and social authentication on the same page.
   >
   >   * To require social authentication only, deselect Include local authentication. Learn more in [Enforce social registration](#enforce-social-registration).

   > **Collapse: Social Provider Handler node**
   >
   > Learn more in [Social Provider Handler node](https://docs.pingidentity.com/auth-node-ref/latest/social-provider-handler.html).
   >
   > * Connections:
   >
   >   * Connect the Account exists outcome to the Increment Login Count node.
   >
   >   * Connect the No account exists outcome to the Required Attributes Present node.
   >
   >   * Connect the Social auth interrupted outcome to the initial Page node.
   >
   > * Configuration:
   >
   >   * In the Transformation Script field, select `Normalized Profile to Managed User`. This script transforms the normalized identity provider profile into a format that Advanced Identity Cloud can use.
   >
   >     Find information on the script and the available bindings in [normalized-profile-to-managed-user.js](../am-scripting/sample-scripts.html#normalized-profile-to-managed-user-js).
   >
   >     |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
   >     | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   >     |   | Social authentication uses two transformation steps:- First, the identity provider configuration runs its normalization script. This script receives the raw claims returned by the provider and converts them into a normalized profile format.
   >
   >     - Next, the **Social Provider Handler** node runs the transformation script selected in the node. This script maps the normalized profile to the managed user fields used to create or update the identity object in Advanced Identity Cloud. |
   >
   >   * In the Client Type field, select `BROWSER` when using the Ping Identity-provided user interfaces or Ping SDKs for JavaScript, or `NATIVE` when using the Ping SDKs for Android or iOS.

   > **Collapse: Data Store Decision node**
   >
   > Learn more in [Data Store Decision node](https://docs.pingidentity.com/auth-node-ref/latest/data-store-decision.html).
   >
   > * Connections:
   >
   >   * Connect the True outcome to the Increment Login Count node.
   >
   >   * Connect the False outcome to the Failure node.

   > **Collapse: Increment Login Count node**
   >
   > Learn more in [Increment Login Count node](https://docs.pingidentity.com/auth-node-ref/latest/increment-login-count.html).
   >
   > * Connections:
   >
   >   * Connect to the Success node.

   > **Collapse: Required Attributes Present node**
   >
   > Learn more in [Required Attributes Present node](https://docs.pingidentity.com/auth-node-ref/latest/required-attributes-present.html).
   >
   > * Connections:
   >
   >   * Connect the True outcome to the second Page node (containing the Platform Password node).
   >
   >   * Connect the False outcome to the third Page node (containing the Attribute Collector node).
   >
   > * Configuration:
   >
   >   * In the Identity Resource field, enter the relevant managed identity resource type, such as `managed/alpha_user`.
   >
   >     |   |                                                                                                                       |
   >     | - | --------------------------------------------------------------------------------------------------------------------- |
   >     |   | To check for the available managed identity resource types, go to Identities > Configure and review the current list. |
   >
   >   * At minimum, make sure your social registration flow can supply values for these managed user attributes: `userName`, `givenName`, `sn`, and `mail`.
   >
   >     Typical OIDC mappings:
   >
   >     * `userName`: `preferred_username`, falling back to `email`, then `sub`
   >
   >     * `givenName`: `given_name`
   >
   >     * `sn`: `family_name`
   >
   >     * `mail`: `email`

   > **Collapse: Page node (second, containing a Platform Password node)**
   >
   > * Connections:
   >
   >   * Connect to the Create Object node.

   > **Collapse: Page node (third, containing an Attribute Collector node)**
   >
   > * Connections:
   >
   >   * Connect to the second Page node (containing the Platform Password node).
   >
   > * Configuration:
   >
   >   * Configure the [Attribute Collector node](https://docs.pingidentity.com/auth-node-ref/latest/attribute-collector.html) to collect any required attributes that the provider doesn't return. In a typical social registration journey, these include `mail`, `givenName`, and `sn` attributes. Ensure the journey also resolves a suitable value for `userName`.

   > **Collapse: Create Object node**
   >
   > Learn more in [Create Object node](https://docs.pingidentity.com/auth-node-ref/latest/create-object.html).
   >
   > * Connections:
   >
   >   * Connect the Created outcome to the Increment Login Count node.
   >
   >   * Connect the Failed outcome to the Failure node.
   >
   > * Configuration:
   >
   >   * In the Identity Resource field, configure the relevant managed identity resource type, such as `managed/alpha_user`.

3. Click Save to save the journey.

### Enforce social registration

To modify the journey to enforce social registration, make the following changes:

1. In the Select Identity Provider node, deselect Include local authentication.

2. Remove the Platform Username and Platform Password nodes from the initial Page node.

3. Remove the Data Store Decision node.

The resulting journey looks similar to this:

![Example social registration enforcing social sign-on](_images/social-registration-without-local.png)

## Configure social registration with account claiming

If your end users have one or more social identity provider accounts, they can link them to the same Advanced Identity Cloud account.

The following example builds on the basic social registration journey shown in [Configure a social registration journey](#basic-reg-journey):

![Example social registration with account claiming](_images/social-registration-account-claiming.png)

The journey uses the [Identify Existing User node](https://docs.pingidentity.com/auth-node-ref/latest/identify-existing-user.html) to determine if the end user is already registered in Advanced Identity Cloud. By default, the node checks that the email address associated with the account is already registered in Advanced Identity Cloud.

Ensure that you configure the Transformation Script in the [Social Provider Handler node](https://docs.pingidentity.com/auth-node-ref/latest/social-provider-handler.html), and the Identity Resource field in the [Patch Object node](https://docs.pingidentity.com/auth-node-ref/latest/patch-object.html).

Learn more in [Configure a social registration journey](#basic-reg-journey).

## Let end users connect through their profile page

To let end users connect to social identity providers through the hosted account pages profile page, add a mapping for your social registration journey:

1. In the Advanced Identity Cloud admin console, go to Authentication > Self Service Journeys.

2. If the Status is inactive, click Activate to enable it.

3. In the Key field, enter `connectSocial`.

4. In the corresponding Journey list, select the social registration journey to assign to it.

5. Click Save.

---

---
title: Configure identity verification
description: Configure identity verification settings for your realm, including Jumio and OneSpan
component: pingoneaic
page_id: pingoneaic:authentication:identity-verification
canonical_url: https://docs.pingidentity.com/pingoneaic/authentication/identity-verification.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Identity verification", "Jumio", "OneSpan"]
---

# Configure identity verification

Advanced Identity Cloud helps you protect end-user registration, sign-on, and high-risk transactions through configurable identity and device verification. You can meet different security requirements by verifying an end user's government-issued ID and biometrics, adding document verification, or authorizing transactions. After configuring these settings, use them in your journey nodes to validate end users and their devices in real time.

To configure identity verification settings in the Advanced Identity Cloud admin console, go to [icon: power, set=material, size=inline] Integrations > Identity Verification.

The following identity verification options are available:

* Jumio

  Verify end-user identity using government-issued ID and biometric validation.

  Learn more in [Jumio settings](identity-verification-jumio.html).

* OneSpan

  Verify identity or authorize transactions using OneSpan.

  Learn more in [OneSpan settings](identity-verification-onespan.html).

---

---
title: Configure social authentication
description: Configure Advanced Identity Cloud social authentication with OAuth 2.0 or OIDC identity providers
component: pingoneaic
page_id: pingoneaic:authentication:social-authentication-configure
canonical_url: https://docs.pingidentity.com/pingoneaic/authentication/social-authentication-configure.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Journeys", "Nodes &amp; Trees", "Social Authentication", "OAuth 2.0", "OpenID Connect (OIDC)"]
section_ids:
  social-authentication-configuration-prerequisites: Before you begin
  social-authentication-configuration-register: Register the application with the identity provider
  social-authentication-configuration-redirect-url: Redirect URL requirements
  social-authentication-configuration-provider-specific-settings: Provider-specific settings
  add_the_provider_to_advanced_identity_cloud: Add the provider to Advanced Identity Cloud
  verify_preconfigured_settings: Verify preconfigured settings
---

# Configure social authentication

Social authentication lets users sign on to your applications using their existing accounts from providers such as Google or Facebook.

Advanced Identity Cloud can integrate with any OAuth 2.0 or OpenID Connect (OIDC) compliant identity provider. This page shows you how to register and configure an external social identity provider in Advanced Identity Cloud so that it can be used in your authentication journeys.

## Before you begin

Before you can configure social authentication in Advanced Identity Cloud, you must:

* Register a developer application with each social identity provider you want to support. This process will provide you with a *client ID* and *client secret*.

* Review the provider's documentation for any provider-specific prerequisites, such as enabling required APIs, scopes, or permissions.

### Register the application with the identity provider

Before you can add a social identity provider to Advanced Identity Cloud, you must register a developer application with each identity provider you want to support. During this process, you'll configure a redirect URL and obtain credentials.

When you've finished, you should have at a minimum:

* A client ID.

* A client secret (for confidential clients).

* The provider's endpoint URLs.

* The redirect URL you configured at the provider. Learn more about [redirect URL requirements](#social-authentication-configuration-redirect-url).

The provider's developer documentation describes their integration needs, as well as their API endpoints. For example, providers usually have different scopes that you can configure depending on your service's needs.

OAuth 2.0 and OIDC-compliant providers display much of the information you need to configure the identity provider client in their `.well-known` endpoint. For example, the endpoint should expose their endpoint URLs, and the signing and encryption algorithms they support.

Financial-grade providers might require additional security-related configuration, such as `acr` values or PKCE-related settings.

|   |                                                                                                     |
| - | --------------------------------------------------------------------------------------------------- |
|   | Keep the provider's developer documentation available because you'll need it during this procedure. |

#### Redirect URL requirements

A redirect URL is a path in Advanced Identity Cloud where the identity provider redirects the end user on successful authentication.

Follow these requirements when configuring the redirect URL:

* Set the redirect URL to your tenant's access management base URL. For example, `https://<tenant-env-fqdn>/am`. This is the path that the social identity provider redirects the user back to after successful authentication.

* Don't add realm names, journey names, or other query parameters to the redirect URL. The hosted journey pages store the realm, journey, and authentication session in the browser's local storage so Advanced Identity Cloud can resume the correct flow after the provider redirects back.

* The redirect URL registered with the social identity provider must exactly match the redirect URL configured in Advanced Identity Cloud.

#### Provider-specific settings

Some providers require you to enable a specific setting or API in their service:

* Google

  Enable the `Gmail API` in the Google Cloud console.

* Apple

  You must have access to the Apple Development Program (Enterprise program isn't eligible), and you must enable `Sign In With Apple` in the Apple Developer site.

* LINE

  You must apply for permission for your LINE channel to access a user's email address using OIDC:

  1. In the LINE Developers console, enable Email address permission.

  2. Agree to the terms and conditions, and follow the steps to complete the application.

  3. The console displays `Applied` when your application is accepted.

  If you don't have email permission, social registration fails with an `Invalid Attribute Syntax` error.

## Add the provider to Advanced Identity Cloud

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Make sure the redirect URL, client secret, and requested scopes are aligned on both sides. You must follow the [redirect URL requirements](#social-authentication-configuration-redirect-url) exactly.If your journey expects an email address, request the email scope explicitly. Some providers don't return an email claim unless that scope is included.A mismatch in these values can cause redirect loops, failed token exchange, or missing claims during sign on. |

To add the provider in Advanced Identity Cloud:

1. In the Advanced Identity Cloud admin console, go to [icon: power, set=material, size=inline] Integrations > Identity Providers.

2. Click [icon: add, set=material, size=inline] New identity provider.

   Advanced Identity Cloud includes scripts and configurations for common identity providers.

3. In the New identity provider modal, select the required identity provider.

   If the required provider doesn't appear, select one of the following to add a custom identity provider:

   * OAuth2

   * OpenID Connect

4. Click Next.

5. Enter the identity provider's required settings: Name, Client ID, the Redirect URL, and Scope Delimiter (usually an empty space).

6. (Optional) Click Show advanced settings and enter any additional provider-specific settings that are available during creation. Learn more about these fields in [Social identity provider settings](social-authentication-settings.html).

7. Click Save to save your changes and access all the configuration fields for the identity provider.

8. Provide the identity provider's remaining configuration details, and edit any required configuration details if needed. Learn more about each field in [Social identity provider settings](social-authentication-settings.html).

9. Click Save to save your changes.

   |   |                                                                                                                                                                                                                                                                                                                                    |
   | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | For OAuth 2.0 social identity providers, store the client secret in a secret store for greater security.Use the Client Secret Label Identifier to create a dynamic secret label to map to an alias for the secret.Learn more about secrets in [Use ESVs for signing and encryption keys](../tenants/esvs-signing-encryption.html). |

   Don't worry if some details are missing. You can edit the configuration later after saving the identity provider configuration for the first time.

### Verify preconfigured settings

Advanced Identity Cloud preconfigures many of the required settings for the default providers, but you should verify that the settings for the provider haven't changed. Key preconfigured fields include:

* The provider's URLs.

  For example, Authentication Endpoint URL, Access Token Endpoint URL, and User Profile Service URL.

* The OAuth Scopes field.

* The Well Known Endpoint for retrieving information about the provider.

  Leave this field empty for the `LINE (Browser)` configuration.

* The provider's button and logo. Click Edit in the Button preview to configure the UI settings.

* The script selected in the Transform Script list.

  This script is responsible for mapping attributes provided by the identity providers to a profile format compatible with Advanced Identity Cloud.

  Learn more in [Transform Script](social-authentication-settings.html#transform-script).

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Some features require choosing algorithms from those supported by the provider, as well as creating secrets. Consider the following points before configuring the provider:* Several capabilities in the identity provider client share the same secret IDs. For example, signing request objects and signing client authentication JWTs.

* For these capabilities, the corresponding secrets are also not isolated per identity provider client within the realm.Therefore, ensure that you configure features requiring secrets in a way that they are compatible across clients in the same realm.Learn more in [/oauth2/connect/rp/jwk_uri](../am-oidc1/managing-rp-jwk_uri.html). |

---

---
title: Device binding settings
description: Configure storage and encryption settings for device binding data used to associate trusted devices with user identities
component: pingoneaic
page_id: pingoneaic:authentication:authentication-methods-device-binding
canonical_url: https://docs.pingidentity.com/pingoneaic/authentication/authentication-methods-device-binding.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Authentication", "Multi-factor Authentication (MFA)", "device binding", "trusted device", "encryption"]
section_ids:
  configure-device-binding: Configure device binding settings
---

# Device binding settings

Device binding associates trusted devices with user identities. Journeys can use device binding to support risk-based or step-up authentication. For example, device binding can let end users skip a second factor on a device they've previously verified, or require stronger authentication when a sign-on comes from an unrecognized device.

Device binding settings control how Advanced Identity Cloud stores and protects data for bound devices.

By default, Advanced Identity Cloud creates the configuration with no encryption. For production environments, you should select an encryption scheme and store the associated key in an [ESV secret](../tenants/esvs-signing-encryption.html).

|   |                                                                                                                                                                                                                                                                                                                                                                                                               |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Updating the encryption key store setting after end users have bound their devices isn't supported. If you change encryption key information (in the configuration or in the secret stores) end users with existing bound devices can no longer sign on using those bound devices. You'll need to delete each affected end user's device profile so they can re-bind their device the next time they sign on. |

## Configure device binding settings

1. In the Advanced Identity Cloud admin console, go to [icon: verified_user, set=material, size=inline] Authentication > Authentication Methods.

2. Click Device Binding.

3. If device binding is not already enabled, click Enable Device Binding to create it with default settings before configuring it.

4. Configure the following settings:

   * Device Binding Attribute

     The user's attribute in which to store bound device data.

     Default value: `boundDevices`

   * Device Binding Encryption Scheme

     Encryption scheme to use to secure device binding data stored on the server.

     If enabled, the data for each bound device is encrypted using a unique random secret key using the given strength of AES encryption in CBC mode with PKCS#5 padding. An HMAC-SHA of the given strength (truncated to half-size) is used to ensure integrity protection and authenticated encryption. The unique random key is encrypted with the given RSA key pair and stored with the data.

     The possible values for this property are:

     * `AES-256/HMAC-SHA-512 with RSA Key Wrapping`

     * `AES-128/HMAC-SHA-256 with RSA Key Wrapping`

     * `No encryption of device settings.`

     Default value: `No encryption of device settings.`

   * Encryption Key Store

     Path to the key store from which to load encryption keys.

     |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
     | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
     |   | Updating this setting isn't currently supported in Advanced Identity Cloud. Changing its value may lead to a loss of functionality in this feature.For greater security, store encryption key information in [ESVs](../tenants/esvs-signing-encryption.html), instead of in the configuration. Use the [secret label](../am-reference/secret-id-mappings.html#encrypted-device-storage-secret-labels) `am.services.devicebinding.encryption` to map an alias for Device Binding secrets.If you update encryption key information in the configuration or in the secret stores, end users with existing device profiles can no longer sign on using those bound devices. Delete the end user's device profile so that they can create a new one when they next sign on. |

     |   |                                                                                                                                                                 |
     | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
     |   | If Advanced Identity Cloud finds a matching secret for the `am.services.devicebinding.encryption` label in the realm's ESV secret store, this value is ignored. |

     Default value: `/path/to/openam/security/keystores/keystore.jks`

   * Key Store Type

     Type of key store to load.

     This property is preconfigured in your Advanced Identity Cloud tenant and shouldn't be altered.

     Default value: `Java Key Store (JKS)`

   * Key Store Password

     Password to unlock the key store. This password is encrypted when it is saved in the Advanced Identity Cloud configuration. You should modify the default value.

     |   |                                                                                                                                                                 |
     | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
     |   | If Advanced Identity Cloud finds a matching secret for the `am.services.devicebinding.encryption` label in the realm's ESV secret store, this value is ignored. |

   * Key-Pair Alias

     Alias of the certificate and private key in the key store. The private key is used to encrypt and decrypt bound device data.

     |   |                                                                                                                                                                 |
     | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
     |   | If Advanced Identity Cloud finds a matching secret for the `am.services.devicebinding.encryption` label in the realm's ESV secret store, this value is ignored. |

   * Private Key Password

     Password to unlock the private key.

     |   |                                                                                                                                                                 |
     | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
     |   | If Advanced Identity Cloud finds a matching secret for the `am.services.devicebinding.encryption` label in the realm's ESV secret store, this value is ignored. |

5. Click Save.

---

---
title: Jumio settings
description: Configure Jumio to verify user identity using government-issued ID and selfie-based biometric verification
component: pingoneaic
page_id: pingoneaic:authentication:identity-verification-jumio
canonical_url: https://docs.pingidentity.com/pingoneaic/authentication/identity-verification-jumio.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Jumio", "identity verification", "document verification", "biometric"]
section_ids:
  before_you_begin: Before you begin
  configure-jumio: Configure Jumio settings
  delete-jumio: Delete the Jumio configuration
---

# Jumio settings

[Jumio](https://www.jumio.com/) is a third-party identity verification provider that integrates with Advanced Identity Cloud for authentication and registration journeys. It can capture and validate a user's government-issued ID document, compare it with a selfie, and use liveness detection to help verify the user's identity.

You must have a Jumio account to use this integration.

Learn more about using Jumio in journeys with the [Jumio identity verification](https://docs.pingidentity.com/auth-node-ref/latest/cloud/jumio-id-verify.html) nodes.

## Before you begin

Before configuring Jumio in Advanced Identity Cloud, ensure you have the following:

* An active Jumio account. To generate API credentials:

  1. In the Jumio Customer Portal, go to Settings > Managed Services > Identity Verification > API Credentials > OAuth2 Clients.

  2. Select Initialize and Retrieve & Delete permissions.

  3. Note the generated API token and secret.

* Your Jumio deployment region: US, EU, or SG (APAC).

* The fully qualified domain name (FQDN) of your Advanced Identity Cloud tenant, for use as the redirect URI in Jumio.

## Configure Jumio settings

1. In the Advanced Identity Cloud admin console, go to [icon: power, set=material, size=inline] Integrations > Identity Verification.

2. Click Jumio.

3. If Jumio is not already enabled, click Enable Jumio to create it with default settings before configuring it.

4. Configure the following settings:

   * Server

     The Jumio deployment region for your account. Select one of the following: `US`, `EU`, or `SG` (APAC).

   * Token

     The API token generated from the Jumio Customer Portal.

     To generate a token:

     1. In the Jumio Customer Portal, go to Settings > Managed Services > Identity Verification > API Credentials > OAuth2 Clients.

     2. Select Initialize and Retrieve & Delete permissions.

   * Secret

     The API secret generated alongside the token in the Jumio Customer Portal.

   * Merchant Reporting Criteria

     The `reportingCriteria` parameter configured in your Jumio setup.

     |   |                                                                        |
     | - | ---------------------------------------------------------------------- |
     |   | Don't include personally identifiable information (PII) in this field. |

   * Customer Internal Reference

     The `customerInternalReference` parameter configured in your Jumio setup.

     |   |                                                                        |
     | - | ---------------------------------------------------------------------- |
     |   | Don't include personally identifiable information (PII) in this field. |

   * Redirect URI

     The endpoint Jumio redirects users to after identity verification. Set this to `https://<tenant-env-fqdn>/am`, where *tenant-env-fqdn* is the fully qualified domain name of your Advanced Identity Cloud tenant.

5. Click Save.

## Delete the Jumio configuration

Deleting the configuration removes its settings.

1. In the Advanced Identity Cloud admin console, go to [icon: power, set=material, size=inline] Integrations > Identity Verification.

2. Click Jumio.

3. At the bottom of the page, click Delete Jumio.

---

---
title: One-time passcode (TOTP) settings
description: Configure storage, encryption, and behavior settings for one-time passcode (TOTP)
component: pingoneaic
page_id: pingoneaic:authentication:authentication-methods-totp
canonical_url: https://docs.pingidentity.com/pingoneaic/authentication/authentication-methods-totp.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Authentication", "Multi-factor Authentication (MFA)", "OATH", "TOTP", "HOTP", "one-time passcode", "device profile", "encryption"]
section_ids:
  configure-totp: Configure one-time passcode (TOTP) settings
---

# One-time passcode (TOTP) settings

Time-based one-time passcode (TOTP) settings control how Advanced Identity Cloud stores and protects the device metadata registered by users of OATH-based authenticator apps.

These settings are available by default. In most cases you don't need to change them to get started, but for production environments you should select an encryption scheme and store the associated key in an [ESV secret](../tenants/esvs-signing-encryption.html).

|   |                                                                                                                                                                                                         |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | In the admin console, this authentication method is labeled One-time Passcode (TOTP). The underlying OATH-based authentication flow supports both TOTP and HOTP, but TOTP is the default configuration. |

Learn more about configuring journeys that authenticate end users with OATH-based authentication in [Use codes from an authenticator app using OATH](../am-authentication/authn-mfa-about-oath.html).

## Configure one-time passcode (TOTP) settings

1. In the Advanced Identity Cloud admin console, go to [icon: verified_user, set=material, size=inline] Authentication > Authentication Methods.

2. Click One-time Passcode (TOTP).

3. If one-time passcode (TOTP) is not already enabled, click Enable One-time Passcode (TOTP) to create it with default settings before configuring it.

4. Configure the following settings:

   * Profile Storage Attribute

     Attribute for storing ForgeRock Authenticator OATH profiles.

   * Device Profile Encryption Scheme

     Encryption scheme to use to secure device profiles stored on the server.

     If enabled, each device profile is encrypted using a unique random secret key using the given strength of AES encryption in CBC mode with PKCS#5 padding. An HMAC-SHA of the given strength (truncated to half-size) is used to ensure integrity protection and authenticated encryption. The unique random key is encrypted with the given RSA key pair and stored with the data.

     The possible values for this property are:

     * `AES-256/HMAC-SHA-512 with RSA Key Wrapping`

     * `AES-128/HMAC-SHA-256 with RSA Key Wrapping`

     * `No encryption of device settings.`

     Default value: `No encryption of device settings.`

   * Encryption Key Store

     Path to the key store from which to load encryption keys.

     |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
     | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
     |   | Updating this setting isn't currently supported in Advanced Identity Cloud. Changing its value may lead to a loss of functionality in this feature.For greater security, store encryption key information in [ESVs](../tenants/esvs-signing-encryption.html), instead of in the configuration. Use the [secret label](../am-reference/secret-id-mappings.html#encrypted-device-storage-secret-labels) `am.services.authenticatoroath.encryption` to map an alias for ForgeRock Authenticator (OATH) secrets.If you update encryption key information, end users with existing device profiles won't be able to sign on using an authenticator app. Delete the end user's device profile so that they can create a new one when they next sign on. |

     |   |                                                                                                                                                                     |
     | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
     |   | If Advanced Identity Cloud finds a matching secret for the `am.services.authenticatoroath.encryption` label in the realm's ESV secret store, this value is ignored. |

   * Key Store Type

     Type of key store to load.

     This property is preconfigured in your Advanced Identity Cloud tenant and shouldn't be altered.

     Default value: `Java Cryptography Extension Key Store (JCEKS)`

   * Key Store Password

     Password to unlock the key store. This password will be encrypted.

     |   |                                                                                                                                                                     |
     | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
     |   | If Advanced Identity Cloud finds a matching secret for the `am.services.authenticatoroath.encryption` label in the realm's ESV secret store, this value is ignored. |

   * Key-Pair Alias

     Alias of the certificate and private key in the key store. The private key is used to encrypt and decrypt device profiles.

     |   |                                                                                                                                                                     |
     | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
     |   | If Advanced Identity Cloud finds a matching secret for the `am.services.authenticatoroath.encryption` label in the realm's ESV secret store, this value is ignored. |

   * Private Key Password

     Password to unlock the private key.

     |   |                                                                                                                                                                     |
     | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
     |   | If Advanced Identity Cloud finds a matching secret for the `am.services.authenticatoroath.encryption` label in the realm's ESV secret store, this value is ignored. |

   * ForgeRock Authenticator (OATH) Device Skippable Attribute Name

     The data store attribute that holds the user's decision to enable or disable obtaining and providing a password obtained from an authenticator app. This attribute must be writeable.

5. Click Save.

---

---
title: OneSpan settings
description: Configure the OneSpan settings to verify user identity and authorize transactions using OneSpan Intelligent Adaptive Authentication.
component: pingoneaic
page_id: pingoneaic:authentication:identity-verification-onespan
canonical_url: https://docs.pingidentity.com/pingoneaic/authentication/identity-verification-onespan.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["OneSpan", "identity verification", "transaction authorization"]
section_ids:
  before_you_begin: Before you begin
  configure-onespan: Configure OneSpan settings
  delete-onespan: Delete the OneSpan configuration
---

# OneSpan settings

[OneSpan](https://www.onespan.com/) is a third-party risk-based authentication provider that Advanced Identity Cloud integrates with to help reduce fraud, improve end user experience, and meet compliance requirements.

It uses OneSpan Intelligent Adaptive Authentication (IAA) to assess risk during authentication and step-up transactions, allowing you to apply the right level of friction based on the risk of each interaction.

You must have a OneSpan account to use this integration.

Learn more about using OneSpan in authentication journeys in [OneSpan](https://docs.pingidentity.com/auth-node-ref/latest/cloud/onespan-about.html).

## Before you begin

Before configuring OneSpan in Advanced Identity Cloud, ensure you have the following:

* A [OneSpan Developer Community account](https://community.onespan.com/user/registration) with access to the OneSpan sandbox.

* Your OneSpan IAA username and application reference identifier.

* Your target environment. For example `sdb` (sandbox) for development and testing, or `prod` for production.

Learn more in [Set up OneSpan](https://docs.pingidentity.com/auth-node-ref/latest/cloud/onespan-setup.html).

## Configure OneSpan settings

1. In the Advanced Identity Cloud admin console, go to [icon: power, set=material, size=inline] Integrations > Identity Verification.

2. Click OneSpan.

3. If OneSpan is not already enabled, click Enable OneSpan to create it with default settings before configuring it.

4. Configure the following settings:

   * OneSpan IAA Username

     The username associated with your OneSpan IAA account.

   * OneSpan IAA Environment

     The OneSpan IAA environment to connect to. Select one of the following:

     * `sdb`: For development and testing.

     * `prod`: For production.

     * `Sandbox`: For development and testing.

     * `Production_NA1`, `Production_EU1`, `Production_EU2`: Production environments by region.

     * `Staging_NA1`, `Staging_EU1`, `Staging_EU2`: Staging environments by region.

     * `UAT_EU1`: UAT environment in the EU1 region.

     * `CUSTOMIZED`: Use a custom URL. If you select this option, enter the URL in the Custom URL field.

   * customURL

     The URL for OneSpan API calls when OneSpan IAA environment is set to `CUSTOMIZED`.

   * Application Reference

     A unique identifier for this application in your OneSpan setup. This value is configured in your OneSpan account and is used to associate authentication events with your application.

   * ASP Public Key

     The application service provider's public key, used to verify signatures from OneSpan.

   * ASP Private Key

     The application service provider's private key, used to sign requests sent to OneSpan.

5. Click Save.

## Delete the OneSpan configuration

Deleting the configuration removes its settings.

1. In the Advanced Identity Cloud admin console, go to [icon: power, set=material, size=inline] Integrations > Identity Verification.

2. Click OneSpan.

3. At the bottom of the page, click Delete OneSpan.

---

---
title: Password policy
description: Configure password policies in Advanced Identity Cloud including expiration, complexity, and forced changes
component: pingoneaic
page_id: pingoneaic:authentication:password-policy
canonical_url: https://docs.pingidentity.com/pingoneaic/authentication/password-policy.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Authentication", "Customization", "Security", "Realms", "Setup &amp; Configuration"]
page_aliases: ["release-notes:rapid-channel/password-timestamps-rapid.adoc", "realms:policy-password.adoc", "realms:password-policy.adoc"]
section_ids:
  configure-a-password-policy: Configure a password policy
  force-end-user-password-changes: Force end-user password changes
  strategy-1-target-segments-of-end-users: "Strategy 1: Target segments of end users"
  strategy-2-target-oldest-passwords-first: "Strategy 2: Target oldest passwords first"
  password-timestamps: Password timestamps
---

# Password policy

Configure a password policy in PingOne Advanced Identity Cloud when you want a customized rule for creating valid sign-in passwords. The password policy applies to end users who sign in to your registered apps within a realm.

|   |                                                       |
| - | ----------------------------------------------------- |
|   | You can configure only one password policy per realm. |

By default, Advanced Identity Cloud password policy is set to the minimum security requirements established by the National Institute of Standards and Technology (NIST). Any changes you make to the password policy must conform to requirements contained in their guidelines. Learn more in [NIST Digital Identity Guidelines](https://pages.nist.gov/800-63-3/).

## Configure a password policy

1. In the Advanced Identity Cloud admin console, go to Authentication > Password Policy.

2. Choose the realm the password policy will apply to.

3. Edit password policy details.

   |                       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
   | --------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | Password length       | When enabled, the policy requires a password with the specified minimum number of characters. No maximum.                                                                                                                                                                                                                                                                                                                                                                                                                                      |
   | Cannot include        | Options to restrict the use of any of the following in the policy:- More than two consecutive characters (Example: aaaaaa)

   - Commonly used passwords (Examples: qwerty or 12345678)

   - Values in certain user attributes:

     * In the Forbidden *Realm* realm - User attributes list, select user attributes to validate passwords against.

     * In the Minimum *n* characters for each attribute field, enter a substring length between 3 - 64 to use when validating passwords against user attribute values. The default is 5 characters. |
   | Must contain          | When enabled, the policy requires the use of a specified 1 - 4 of the following:- Upper case letter

   - Lower case letter

   - Number

   - Space, pipe, or special character: ( ! " # $ % & ' ( ) \* + , - . / : ; < = > ? @ \[ \ ] ^ \_ \` { } \~ ) .                                                                                                                                                                                                                                                                                              |
   | Cannot reuse          | When enabled, the policy restricts the end user from reusing their current password and the specified number of previously set passwords.For example, if you set this value to 3, the end user can't reuse their current password or any of their last three passwords. The end user must create a new password that is different from any of those four passwords.                                                                                                                                                                            |
   | Force password change | When enabled, the policy forcibly expires each end-user password after the specified number of days, months, or years have elapsed from when the password was set. To handle expired passwords in an end-user journey, use the `Expired` outcome in the [Identity Store Decision node](https://docs.pingidentity.com/auth-node-ref/latest/cloud/identity-store-decision.html).	Refer to the considerations in Force end-user password changes before using this policy setting.                                                                |

4. Click Save.

## Force end-user password changes

You can combine a [password policy](#configure-a-password-policy) and the [Identity Store Decision node](https://docs.pingidentity.com/auth-node-ref/latest/cloud/identity-store-decision.html) to expire end-user passwords in a journey; the Force password change policy setting lets you define an expiry time interval, which is measured for each end user from when their password was last set.

If you are introducing such a policy for the first time, you may want to process your end users in batches in order to improve messaging about the changes. The following sections describe two high-level strategies to achieve this.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | If you are considering forcing your end users to change their passwords, review the [NIST Digital Identity Guidelines](https://pages.nist.gov/800-63-3/). In particular, NIST no longer recommends scheduled password changes; learn more in [Usability Considerations by Authenticator Type](https://pages.nist.gov/800-63-3/sp800-63b.html#102-usability-considerations-by-authenticator-type).The NIST guidelines are continually refined, so you should keep them in mind when setting password policy. |

### Strategy 1: Target segments of end users

Adapt the end-user login journey to use [dynamic groups](../idm-objects/manage-groups.html#add-users-to-group) or user properties to target a segment of end users to reset their password.

**Advantage**: You can segment users any way you like. For example, you may have a set of end users who could struggle with a password reset. You could add a property to each end user in the set and initially exclude end users with that property from a password reset. Then, at a later time, remove the exclusion when support is available for those end users.

**Disadvantage**: Creating new dynamic groups with large numbers of end users can incur a significant performance cost.

### Strategy 2: Target oldest passwords first

Adapt the end-user login journey to target all end users to reset their password, but initially set a very long expiry time interval to target the oldest passwords first. Then periodically reduce the expiry time interval to eventually target all passwords.

**Advantage**: This strategy segments end users by the date of their last password reset. Additionally, end users with the oldest passwords are targeted first.

## Password timestamps

Password timestamps let you view or query when a user password was last changed and when it is set to expire.

The following timestamp fields and properties are available:

| Field name on the user page | Property name in the managed object configuration *(tooltip: You can edit the managed object configuration over REST at the config/managed endpoint.)* |
| --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Password Last Changed Time  | `passwordLastChangedTime`                                                                                                                              |
| Password Expiration Time    | `passwordExpirationTime`                                                                                                                               |

Example query on `passwordLastChangedTime`

```
curl \
--header "Authorization: Bearer <access-token>" \
--header "Accept-API-Version: resource=1.0" \
--request GET \
"https://<tenant-env-fqdn>/openidm/managed/realm-name_user?_queryFilter=passwordLastChangedTime%20ge%20%222024-01-01T21:22:06.274Z%22&_fields=_id"
{
  "result": [
    {
      "_id": "453a73a9-3f50-4b04-8115-f3915fd1dd89",
      "_rev": "fa876a46-82e6-4a11-a3f4-6b4919815ea4-5851"
    }
  ],
  ...
}
```

---

---
title: Push authentication settings
description: Configure push authentication settings for journeys that use push notifications
component: pingoneaic
page_id: pingoneaic:authentication:authentication-methods-push-authentication
canonical_url: https://docs.pingidentity.com/pingoneaic/authentication/authentication-methods-push-authentication.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Authentication", "Multi-factor Authentication (MFA)"]
section_ids:
  configure-push-authentication: Configure push authentication settings
---

# Push authentication settings

Push authentication settings control how Advanced Identity Cloud stores and protects the device metadata registered by end users of an authenticator app. You must configure these settings to enable push authentication journeys in the realm where you create the journey.

By default, Advanced Identity Cloud creates the configuration with no encryption. For production environments, you should select an encryption scheme and store the associated key in an [ESV secret](../tenants/esvs-signing-encryption.html).

You must also configure [Push notification delivery](authentication-methods-push-notification.html) before Advanced Identity Cloud can send push notifications to end users' devices.

## Configure push authentication settings

1. In the Advanced Identity Cloud admin console, go to [icon: verified_user, set=material, size=inline] Authentication > Authentication Methods.

2. Click Push Authentication.

3. If push authentication is not already enabled, click Enable Push Authentication to create it with default settings before configuring it.

4. Configure the following settings:

   * Profile Storage Attribute

     The user attribute where Advanced Identity Cloud stores the device profiles registered for push authentication.

   * Device Profile Encryption Scheme

     Encryption scheme to use to secure device profiles stored on the server.

     If enabled, each device profile is encrypted using a unique random secret key using the given strength of AES encryption in CBC mode with PKCS#5 padding. An HMAC-SHA of the given strength (truncated to half-size) is used to ensure integrity protection and authenticated encryption. The unique random key is encrypted with the given RSA key pair and stored with the data.

     The possible values for this property are:

     * `AES-256/HMAC-SHA-512 with RSA Key Wrapping`

     * `AES-128/HMAC-SHA-256 with RSA Key Wrapping`

     * `No encryption of device settings.`

     Default value: `No encryption of device settings.`

   * Encryption Key Store

     Path to the key store from which to load encryption keys.

     |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
     | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
     |   | Updating this setting isn't currently supported in Advanced Identity Cloud. Changing its value may lead to a loss of functionality in this feature.For greater security, store encryption key information in [ESVs](../tenants/esvs-signing-encryption.html), instead of in the configuration. Use the [secret label](../am-reference/secret-id-mappings.html#encrypted-device-storage-secret-labels) `am.services.authenticatorpush.encryption` to map an alias for push authentication secrets.If you update encryption key information in the configuration or in the secret stores, end users with existing device profiles can no longer sign on using push authentication on those devices. Delete the end user's device profile so that they can create a new one when they next sign on. |

     |   |                                                                                                                                                                     |
     | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
     |   | If Advanced Identity Cloud finds a matching secret for the `am.services.authenticatorpush.encryption` label in the realm's ESV secret store, this value is ignored. |

   * Key Store Type

     Type of key store to load.

     This property is preconfigured in your Advanced Identity Cloud tenant and shouldn't be altered.

     Default value: `Java Cryptography Extension Key Store (JCEKS).`

   * Key Store Password

     Password to unlock the key store. This password is encrypted when it is saved in the Advanced Identity Cloud configuration.

     |   |                                                                                                                                                                     |
     | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
     |   | If Advanced Identity Cloud finds a matching secret for the `am.services.authenticatorpush.encryption` label in the realm's ESV secret store, this value is ignored. |

   * Key-Pair Alias

     Alias of the certificate and private key in the key store. The private key is used to encrypt and decrypt device profiles.

     |   |                                                                                                                                                                     |
     | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
     |   | If Advanced Identity Cloud finds a matching secret for the `am.services.authenticatorpush.encryption` label in the realm's ESV secret store, this value is ignored. |

   * Private Key Password

     Password to unlock the private key.

     |   |                                                                                                                                                                     |
     | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
     |   | If Advanced Identity Cloud finds a matching secret for the `am.services.authenticatorpush.encryption` label in the realm's ESV secret store, this value is ignored. |

   * ForgeRock Authenticator (Push) Device Skippable Attribute Name

     The name of the attribute in a user's profile used to store their decision on skipping push authentication.

5. Click Save.

---

---
title: Push notification delivery settings
description: Configure the infrastructure used to deliver push notifications to user devices, including AWS SNS credentials and endpoints
component: pingoneaic
page_id: pingoneaic:authentication:authentication-methods-push-notification
canonical_url: https://docs.pingidentity.com/pingoneaic/authentication/authentication-methods-push-notification.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Authentication", "Multi-factor Authentication (MFA)", "Push", "push notifications", "SNS", "AWS"]
section_ids:
  configure-push-notification-delivery: Configure push notification delivery settings
---

# Push notification delivery settings

Push notification delivery settings configure the AWS Simple Notification Service (SNS) infrastructure that Advanced Identity Cloud uses to send push notifications to end users' devices.

You must configure these settings before end users can receive push notifications from the PingID app. This configuration requires AWS credentials that are specific to your Advanced Identity Cloud environment. You retrieve these from [Backstage](https://backstage.pingidentity.com) before configuring push notification delivery.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Advanced Identity Cloud uses an external AWS service to send push notifications. Its configuration requires access keys and other metadata. As a Ping Identity customer, you have streamlined access to the required metadata.Before you start, log in to [Backstage](https://backstage.pingidentity.com), then follow the instructions in [How To Configure Service Credentials (Push Auth, Docker) in Backstage](https://backstage.pingidentity.com/help/docs/how-to-configure-service-credentials-push-auth,-docker-in-backstage.html).Download the AWS credential data in JSON format and refer to that as you configure push notification delivery. |

|   |                                                                                                                                                                                                                                                                                                                                   |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | If you update the AWS credentials for push notification delivery after end users have registered their devices, you must [re-register all end user devices](../am-authentication/authn-mfa-reset-devices.html). Devices registered with the previous credentials will encounter authorization errors until they're re-registered. |

You must also configure [Push Authentication](authentication-methods-push-authentication.html) to control how Advanced Identity Cloud stores device profiles.

## Configure push notification delivery settings

1. In the Advanced Identity Cloud admin console, go to [icon: verified_user, set=material, size=inline] Authentication > Authentication Methods.

2. Click Push Notification Delivery.

3. If push notification delivery is not already enabled, click Enable Push Notification Delivery to create it with default settings before configuring it.

4. Configure the following settings:

   * SNS Access Key ID

     The Amazon Simple Notification Service Access Key ID. Find more information in [Create an AWS (Push Auth) Credential](https://backstage.forgerock.com/knowledge/backstagehelp/article/a92326771#aws) in Backstage.

     For example, you might set this property to: AKIAIOSFODNN7EXAMPLE

   * SNS Access Key Secret

     Amazon Simple Notification Service Access Key Secret. Find more information in [Create an AWS (Push Auth) Credential](https://backstage.pingidentity.com/help/docs/how-to-configure-service-credentials-push-auth,-docker-in-backstage.html#aws) in Backstage.

   |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
   | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | For greater security, you can store this secret in the realm secret store.Map the secret to the secret label `am.services.pushnotification.sns.accesskey.secret`.If a secret is mapped to this secret label, Advanced Identity Cloud uses that secret and ignores the value of the SNS Access Key Secret property.If a secret is mapped to this secret label and Advanced Identity Cloud can't locate the secret, it falls back to the value of the SNS Access Key Secret property. |

   * SNS Endpoint for APNS

     The Simple Notification Service endpoint in Amazon Resource Name format, used to send push messages to the Apple Push Notification Service (APNS).

     For example, you might set this property to: arn:aws:sns:us-east-1:1234567890:app/APNS/production

   * SNS Endpoint for GCM

     The Simple Notification Service endpoint in Amazon Resource Name format, used to send push messages over Google Cloud Messaging (GCM).

     For example, you might set this property to: arn:aws:sns:us-east-1:1234567890:app/GCM/production

   * SNS Client Region

     Region of your registered Amazon Simple Notification Service client. Find more information in <https://docs.aws.amazon.com/general/latest/gr/rande.html>.

     The possible values for this property are:

     * `us-gov-west-1`

     * `us-east-1`

     * `us-west-1`

     * `us-west-2`

     * `eu-west-1`

     * `eu-west-2`

     * `eu-central-1`

     * `ap-southeast-1`

     * `ap-southeast-2`

     * `ap-southeast-3`

     * `ap-northeast-1`

     * `ap-northeast-2`

     * `sa-east-1`

     * `ca-central-1`

     * `cn-north-1`

   * Message Transport Delegate Factory

     The fully qualified class name of the factory responsible for creating the PushNotificationDelegate. The class must implement `org.forgerock.openam.services.push.PushNotificationDelegate`.

   * Response Cache Duration

     The minimum lifetime to keep unanswered message records in the message dispatcher cache, in seconds. To keep unanswered message records indefinitely, set this property to `0`.

   * Response Cache Concurrency

     Level of concurrency to use when accessing the message dispatcher cache. Must be greater than `0`. Choose a value to accommodate as many threads as will ever concurrently access the message dispatcher cache.

   * Response Cache Size

     Maximum size of the message dispatcher cache, in number of records. If set to `0` the cache can grow indefinitely. If the number of records that need to be stored exceeds this maximum, then older items in the cache will be removed to make space.

5. Click Save.

---

---
title: Social authentication
description: Manage Advanced Identity Cloud social authentication with OAuth 2.0 or OIDC identity providers
component: pingoneaic
page_id: pingoneaic:authentication:social-authentication
canonical_url: https://docs.pingidentity.com/pingoneaic/authentication/social-authentication.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Journeys", "Nodes &amp; Trees", "Social Authentication", "OAuth 2.0", "OpenID Connect (OIDC)"]
page_aliases: ["am-authentication:social-authentication.adoc", "self-service:social-registration.adoc"]
section_ids:
  social-authentication-flows: End user flows involved in social authentication
  supported-provider-types: Supported provider types
  default-social-providers: Default social identity provider configurations
  custom-social-providers: Custom social identity provider configurations
  social_authentication_flow: Social authentication flow
---

# Social authentication

Social authentication (also known as social sign-on or social login) lets end users register and sign on to your applications using their existing accounts from social identity providers such as Google or Facebook. Instead of creating a new username and password for your application, end users can authenticate with a trusted provider they already use. Advanced Identity Cloud supports this by integrating with any OAuth 2.0 or OpenID Connect (OIDC) compliant identity provider.

Social authentication offers several benefits:

* **Improved end user experience**: Simplifies registration and sign-on, reducing friction for new users.

* **Increased conversion rates**: Users are more likely to sign up when they don't have to fill out long registration forms or remember another password.

* **Verified email addresses**: Social providers often supply a verified email address, which can increase the quality of your user data.

* **Access to profile data**: With user consent, you can retrieve profile information (such as name and profile picture) from the social provider to personalize the end user experience.

## End user flows involved in social authentication

It's important to understand the different end user flows for social authentication:

* Social registration

  A new user creates an account in Advanced Identity Cloud using their social identity. Advanced Identity Cloud creates a local user profile and links it to the social provider account.

* Social sign-on

  An existing user signs on to your application using their linked social identity.

* Account linking (or account claiming)

  A user who already has a local Advanced Identity Cloud account (created with a username and password) can link one or more social identities to that existing account. This allows them to sign on using either their local credentials or any of their linked social accounts.

Learn more about creating journeys for these flows in [Configure basic social registration journeys](social-authentication-journeys.html).

## Supported provider types

Advanced Identity Cloud supports social identity providers that are OAuth 2.0 or OIDC 1.0-compliant.

### Default social identity provider configurations

The following social identity providers are configured by default:

| Identity provider     | Specification | Configuration ID    |
| --------------------- | ------------- | ------------------- |
| Amazon                | OAuth 2.0     | `amazonConfig`      |
| Apple                 | OIDC          | `appleConfig`       |
| Facebook              | OAuth 2.0     | `facebookConfig`    |
| Google                | OIDC          | `googleConfig`      |
| Instagram             | OAuth 2.0     | `instagramConfig`   |
| itsme(1)              | OIDC          | `itsmeConfig`       |
| LINE (Browser)        | OIDC          | `lineBrowserConfig` |
| LINE (Native)         | OIDC          | `lineNativeConfig`  |
| LinkedIn (Legacy) (2) | OAuth 2.0     | `linkedInConfig`    |
| LinkedIn              | OIDC          | `linkedInV2Config`  |
| Microsoft             | OAuth 2.0     | `microsoftConfig`   |
| Salesforce            | OAuth 2.0     | `salesforceConfig`  |
| Twitter               | OAuth 2.0     | `twitterConfig`     |
| VK (Vkontakte)        | OAuth 2.0     | `vkConfig`          |
| WeChat                | OAuth 2.0     | `weChatConfig`      |
| WordPress             | OAuth 2.0     | `wordpressConfig`   |
| Yahoo                 | OIDC          | `yahooConfig`       |

(1) To integrate with [itsme](https://www.itsme.be/en/), you must obtain an Organization Validation (OV) certificate.

(2) The OAuth 2.0 version of the profile is [deprecated by LinkedIn](https://learn.microsoft.com/en-us/linkedin/consumer/integrations/self-serve/sign-in-with-linkedin).

### Custom social identity provider configurations

You can add providers that aren't configured by default, as long as these providers use OAuth 2.0 or OIDC:

| Identity provider                                                         | Specification | Configuration ID |
| ------------------------------------------------------------------------- | ------------- | ---------------- |
| Any social identity provider that implements the OAuth 2.0 specification. | OAuth 2.0     | `oauth2Config`   |
| Any social identity provider that implements the OIDC specification.      | OIDC          | `oidcConfig`     |

## Social authentication flow

The following diagram illustrates the social authentication flow.

![A user authenticating with Advanced Identity Cloud using a social identity provider.](_images/social-login-flow.svg)

---

<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width,initial-scale=1">
    <title>Social identity provider settings | PingOne Advanced Identity Cloud</title>
    <link rel="canonical" href="https://docs.pingidentity.com/pingoneaic/authentication/social-authentication-settings.html">
    <link rel="alternate" type="text/markdown" title="Markdown version of Social identity provider settings" href="https://docs.pingidentity.com/pingoneaic/authentication/social-authentication-settings.md">
    <link rel="alternate" type="text/markdown" title="AI-friendly Index" href="/llms.txt" />
    <link rel="prev" href="social-authentication-configure.html">
    <link rel="next" href="social-authentication-journeys.html">
    <meta name="description" content="Configure social identity provider clients with OAuth2, OIDC, JWT, and encryption settings">
    <meta name="keywords" content="Authentication, Social Authentication, Setup &amp; Configuration">
    <meta name="generator" content="Antora 3.2.2">
    <link rel="stylesheet" href="https://cdn.forgerock.com/docs-ui/adoc/prod-ping/vendor.antora-styles.css">
    <link rel="stylesheet" href="https://cdn.forgerock.com/docs-ui/adoc/prod-ping/ping.antora-styles.css">
    <meta name="datePublished" content="2026-11-02T14:25:42.065Z">
    <meta name="productname" content="PingOne Advanced Identity Cloud">
    <meta name="productversion" content="latest">
    <meta name="doctype" content="article">
    <meta property="og:site_name" content="PingOne Advanced Identity Cloud">
    <meta property="og:title" content="Social identity provider settings">
    <meta property="og:url" content="https://docs.pingidentity.com/pingoneaic/authentication/social-authentication-settings.html">
    <meta property="og:description" content="Configure social identity provider clients with OAuth2, OIDC, JWT, and encryption settings">
    <meta property="og:image" content="https://cdn-docs.pingidentity.com/images/logos/pingidentity-horizontal-1200x630.png">
    <meta name="twitter:card" content="summary_large_image">

    <script type="application/ld+json">
{
  "@context": {
    "@vocab": "https://schema.org/",
    "dcterms": "http://purl.org/dc/terms/"
  },
  "@graph": [
    {
      "@type": "TechArticle",
      "@id": "https://docs.pingidentity.com/pingoneaic/authentication/social-authentication-settings.html",
      "headline": "Social identity provider settings",
      "datePublished": "2026-11-02T14:25:42.065Z",
      "inLanguage": "en",
      "author": {
        "@type": "Organization",
        "name": "Ping Identity",
        "url": "https://www.pingidentity.com"
      },
      "url": "https://docs.pingidentity.com/pingoneaic/authentication/social-authentication-settings.html",
      "mainEntityOfPage": "https://docs.pingidentity.com/pingoneaic/authentication/social-authentication-settings.html",
      "description": "Configure social identity provider clients with OAuth2, OIDC, JWT, and encryption settings",
      "keywords": [
        "Authentication",
        "Social Authentication",
        "Setup &amp; Configuration"
      ],
      "isPartOf": {
        "@id": "https://docs.pingidentity.com#website"
      },
      "about": {
        "@id": "/pingoneaic/home.html#pingoneaic",
        "name": "PingOne Advanced Identity Cloud",
        "softwareVersion": "latest"
      }
    },
    {
      "@type": "WebSite",
      "@id": "https://docs.pingidentity.com#website",
      "name": "Ping Identity Documentation",
      "url": "https://docs.pingidentity.com"
    }
  ]
}
    </script>
    <!-- Google Tag Manager -->
    <script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start': new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src='https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);})(window,document,'script','dataLayer','GTM-TNNP2HN3');</script>
    <!-- End Google Tag Manager -->
    <link rel="icon" href="https://docs.pingidentity.com/favicon.ico" type="image/x-icon">
  </head>
  <body class="article">
<header id="shared-navbar">
  <div id="ping-navbar"></div>
</header>

<div class="mobile-header">
    <button class="nav-toggle"><i class="material-icons material-icons-outlined md-24">list</i></button>
        <h3 class="title"><a href="../home.html">PingOne Advanced Identity Cloud</a></h3>
</div>
<div class="body">
    <!-- Google Tag Manager (noscript) -->
  <noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-TNNP2HN3" height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
  <!-- End Google Tag Manager (noscript) -->
  <div class="nav-container" data-component="pingoneaic" data-version="">
  <aside class="nav">
    <div class="panels">
      <button class="nav-menu-toggle" aria-label="Toggle expand/collapse all" style="display: none"></button>
  <h3 class="title"><a href="../home.html">PingOne Advanced Identity Cloud</a></h3>
            <div class="nav-panel-menu is-active" data-panel="menu">
  <nav class="nav-menu">
<ul class="nav-list">
  <li class="nav-item" data-depth="0">
    <h5 class="nav-title">Release Information</h5>
<ul class="nav-list">
  <li class="nav-item" data-depth="1">
        <span class="nav-item-toggle">
    <a class="nav-link" href="../release-notes/release-notes.html">Release notes</a>
        </span>
<ul class="nav-list">
  <li class="nav-item" data-depth="2">
        <span class="nav-item-toggle">
    <a class="nav-link" href="../release-notes/regular-channel-changelog.html">Regular channel changelog</a>
        </span>
<ul class="nav-list">
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../release-notes/regular-channel-changelog-archive.html">Regular channel changelog archive</a>
        
  </li>
</ul>
  </li>
  <li class="nav-item" data-depth="2">
        <span class="nav-item-toggle">
    <a class="nav-link" href="../release-notes/rapid-channel-changelog.html">Rapid channel changelog</a>
        </span>
<ul class="nav-list">
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../release-notes/rapid-channel-changelog-archive.html">Rapid channel changelog archive</a>
        
  </li>
</ul>
  </li>
  <li class="nav-item" data-depth="2">
        <span class="nav-item-toggle">
    <a class="nav-link" href="../release-notes/rapid-channel-features.html">Rapid channel features</a>
        </span>
<ul class="nav-list">
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../release-notes/rapid-channel/DOCS-11265/reports-optional-parameters.html">Advanced reports optional parameters</a>
        
  </li>
</ul>
  </li>
</ul>
  </li>
  <li class="nav-item" data-depth="1">
        
    <a class="nav-link" href="../release-notes/release-process.html">Release process</a>
        
  </li>
  <li class="nav-item" data-depth="1">
        
    <a class="nav-link" href="../release-notes/release-deferral.html">Release deferral</a>
        
  </li>
</ul>
  </li>
  <li class="nav-item" data-depth="0">
    <h5 class="nav-title">Getting Started</h5>
<ul class="nav-list">
  <li class="nav-item" data-depth="1">
        
    <a class="nav-link" href="../getting-started/overview.html">What is Advanced Identity Cloud?</a>
        
  </li>
  <li class="nav-item" data-depth="1">
        
    <a class="nav-link" href="../getting-started/getting-started-concepts.html">Key concepts</a>
        
  </li>
  <li class="nav-item" data-depth="1">
        
    <a class="nav-link" href="../getting-started/getting-started-help.html">Getting help</a>
        
  </li>
  <li class="nav-item" data-depth="1">
        <span class="nav-item-toggle">
    <a class="nav-link" href="../getting-started/getting-started.html">Start here</a>
        </span>
<ul class="nav-list">
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="../getting-started/getting-started-about.html">About the getting started guide</a>
        
  </li>
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="../getting-started/getting-started-access-tenant.html">Task 1: Get access to your tenant</a>
        
  </li>
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="../getting-started/getting-started-explore-platform.html">Task 2: Explore the platform</a>
        
  </li>
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="../getting-started/getting-started-create-users.html">Task 3: Add end users</a>
        
  </li>
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="../getting-started/getting-started-self-registration.html">Task 4: Design user self-registration experiences</a>
        
  </li>
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="../getting-started/getting-started-authentication.html">Task 5: Design user authentication experiences</a>
        
  </li>
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="../getting-started/getting-started-account-recovery.html">Task 6: Design account recovery experiences</a>
        
  </li>
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="../getting-started/getting-started-profile-management.html">Task 7: Design profile management experiences</a>
        
  </li>
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="../getting-started/getting-started-branding.html">Task 8: Apply basic branding to journey and account pages</a>
        
  </li>
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="../getting-started/getting-started-oidc-app.html">Task 9: Integrate an OIDC application for SSO</a>
        
  </li>
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="../getting-started/getting-started-next-steps.html">Getting started: Next steps</a>
        
  </li>
</ul>
  </li>
</ul>
  </li>
  <li class="nav-item" data-depth="0">
    <h5 class="nav-title">Planning</h5>
<ul class="nav-list">
  <li class="nav-item" data-depth="1">
        <span class="nav-item-toggle">
    <a class="nav-link" href="../planning/plan-identity-cloud.html">Plan for Advanced Identity Cloud</a>
        </span>
<ul class="nav-list">
  <li class="nav-item" data-depth="2">
        <span class="nav-item-toggle">
    <a class="nav-link" href="../planning/plan-identity-cloud-assess-and-plan.html">Phase 1 - Assess and plan</a>
        </span>
<ul class="nav-list">
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../planning/plan-identity-cloud-functionality-differences.html">Functionality differences when moving from self-managed</a>
        
  </li>
</ul>
  </li>
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="../planning/plan-identity-cloud-transform.html">Phase 2 - Transform</a>
        
  </li>
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="../planning/plan-identity-cloud-adopt.html">Phase 3 - Adopt and refine</a>
        
  </li>
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="../planning/plan-identity-cloud-enable.html">Phase 4 - Enable</a>
        
  </li>
</ul>
  </li>
  <li class="nav-item" data-depth="1">
        <span class="nav-item-toggle">
    <a class="nav-link" href="../planning/plan-object-modeling.html">Plan for data object modeling</a>
        </span>
<ul class="nav-list">
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="../planning/plan-object-modeling-key-functions.html">Key functions</a>
        
  </li>
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="../planning/plan-object-modeling-approach.html">Approach</a>
        
  </li>
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="../planning/plan-object-modeling-user-data.html">Separate users for logical needs</a>
        
  </li>
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="../planning/plan-object-modeling-relationships.html">Organize your identities using relationships</a>
        
  </li>
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="../planning/plan-object-modeling-identity-mappings.html">Plan to synchronize identities</a>
        
  </li>
</ul>
  </li>
  <li class="nav-item" data-depth="1">
        
    <a class="nav-link" href="../planning/plan-security.html">Plan for security in Advanced Identity Cloud</a>
        
  </li>
</ul>
  </li>
  <li class="nav-item" data-depth="0">
    <h5 class="nav-title">Identity for AI</h5>
<ul class="nav-list">
  <li class="nav-item" data-depth="1">
        <span class="nav-item-toggle">
    <a class="nav-link" href="../identity-for-ai/ai-agent-identities.html">Secure your AI-driven solutions using AI agent identities</a>
        </span>
<ul class="nav-list">
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="../identity-for-ai/ai-agent-identities-enable.html">Enable the AI agents feature</a>
        
  </li>
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="../identity-for-ai/ai-agent-identities-ui.html">Manage using the admin console</a>
        
  </li>
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="../identity-for-ai/ai-agent-identities-api.html">Manage using the API</a>
        
  </li>
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="../identity-for-ai/ai-agent-identities-supplementary-information.html">Supplementary information</a>
        
  </li>
</ul>
  </li>
  <li class="nav-item" data-depth="1">
        
    <a class="nav-link" href="../identity-for-ai/ai-agent-identities-configure-on-behalf-of-authentication-flow.html">Configure an "on behalf of" authentication flow</a>
        
  </li>
  <li class="nav-item" data-depth="1">
        
    <a class="nav-link" href="../identity-for-ai/ai-agent-identities-configure-autonomous-agent-flow.html">Configure an autonomous AI agent flow</a>
        
  </li>
  <li class="nav-item" data-depth="1">
        
    <a class="nav-link" href="../identity-for-ai/ai-agent-identities-configure-dcr-onboarding-flow.html">Configure a DCR onboarding flow</a>
        
  </li>
</ul>
  </li>
  <li class="nav-item" data-depth="0">
    <h5 class="nav-title">Tenants</h5>
<ul class="nav-list">
  <li class="nav-item" data-depth="1">
        <span class="nav-item-toggle">
    <a class="nav-link" href="../tenants/environments.html">Tenant environments</a>
        </span>
<ul class="nav-list">
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="../tenants/environments-development-staging-production.html">Development, staging, and production tenant environments</a>
        
  </li>
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="../tenants/environments-uat.html">UAT tenant environment</a>
        
  </li>
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="../tenants/environments-sandbox.html">Sandbox tenant environment</a>
        
  </li>
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="../tenants/environments-outbound-static-ip-addresses.html">Outbound static IP addresses</a>
        
  </li>
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="../tenants/environments-data-residency.html">Where your data resides</a>
        
  </li>
  <li class="nav-item" data-depth="2">
        <span class="nav-item-toggle">
    <a class="nav-link" href="../tenants/environments-architecture-availability-disaster-recovery.html">Architecture, availability, and disaster recovery</a>
        </span>
<ul class="nav-list">
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../tenants/environments-architecture-multi-region-faq.html">Multi-region high availability FAQ</a>
        
  </li>
</ul>
  </li>
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="../tenants/environments-release-information.html">Release information</a>
        
  </li>
</ul>
  </li>
  <li class="nav-item" data-depth="1">
        
    <a class="nav-link" href="../tenants/tenant-settings.html">Tenant settings</a>
        
  </li>
  <li class="nav-item" data-depth="1">
        
    <a class="nav-link" href="../tenants/tenant-administrator-settings.html">Tenant administrator settings</a>
        
  </li>
  <li class="nav-item" data-depth="1">
        <span class="nav-item-toggle">
    <a class="nav-link" href="../tenants/tenant-localize.html">Localize tenant admin console and hosted pages</a>
        </span>
<ul class="nav-list">
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="../tenants/tenant-localize-ui.html">Manage localization using the admin console</a>
        
  </li>
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="../tenants/tenant-localize-api.html">Manage localization using the API</a>
        
  </li>
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="../tenants/tenant-localize-supplementary-information.html">Supplementary information</a>
        
  </li>
</ul>
  </li>
  <li class="nav-item" data-depth="1">
        <span class="nav-item-toggle">
    <a class="nav-link" href="../federation/configure-federated-access-for-tenant-administrators.html">Configure federated access for tenant administrators</a>
        </span>
<ul class="nav-list">
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="../federation/set-up-federation-idp-microsoft-entra-id.html">Set up Microsoft Entra ID as a federation IdP</a>
        
  </li>
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="../federation/set-up-federation-idp-microsoft-ad-fs.html">Set up Microsoft Active Directory Federation Services as a federation IdP</a>
        
  </li>
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="../federation/set-up-federation-idp-oidc.html">Set up an OIDC-compliant IdP as a federation IdP</a>
        
  </li>
</ul>
  </li>
  <li class="nav-item" data-depth="1">
        <span class="nav-item-toggle">
    <a class="nav-link" href="../realms/realms-preface.html">Manage realms</a>
        </span>
<ul class="nav-list">
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="../realms/alpha-bravo-realms.html">Alpha and Bravo realms</a>
        
  </li>
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="../realms/realm-settings.html">Realm settings</a>
        
  </li>
</ul>
  </li>
  <li class="nav-item" data-depth="1">
        <span class="nav-item-toggle">
    <a class="nav-link" href="../realms/domains-preface.html">Manage domains</a>
        </span>
<ul class="nav-list">
  <li class="nav-item" data-depth="2">
        <span class="nav-item-toggle">
    <a class="nav-link" href="../realms/custom-domains.html">Configure customer-friendly domain names</a>
        </span>
<ul class="nav-list">
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../realms/custom-domains-ui.html">Manage using the admin console</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../realms/custom-domains-api.html">Manage using the API</a>
        
  </li>
</ul>
  </li>
  <li class="nav-item" data-depth="2">
        <span class="nav-item-toggle">
    <a class="nav-link" href="../realms/cookie-domains.html">Control cookie scope for custom domains</a>
        </span>
<ul class="nav-list">
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../realms/cookie-domains-ui.html">Manage using the admin console</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../realms/cookie-domains-api.html">Manage using the API</a>
        
  </li>
</ul>
  </li>
</ul>
  </li>
  <li class="nav-item" data-depth="1">
        <span class="nav-item-toggle">
    <a class="nav-link" href="../tenants/tenant-security-preface.html">Manage tenant security</a>
        </span>
<ul class="nav-list">
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="../tenants/tls-secrets-signing-trust-encryption.html">Understand the security behind your tenant</a>
        
  </li>
  <li class="nav-item" data-depth="2">
        <span class="nav-item-toggle">
    <a class="nav-link" href="../realms/server-certificates.html">Secure tenant connections with TLS certificates</a>
        </span>
<ul class="nav-list">
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../realms/server-certificates-ui.html">Manage using the admin console</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../realms/server-certificates-api.html">Manage using the API</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../realms/server-certificates-utility-tasks.html">Server certificate utility tasks</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../realms/ssl-certificate-reference.html">SSL certificate reference</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../realms/server-certificates-best-practices.html">Server certificate best practices</a>
        
  </li>
</ul>
  </li>
  <li class="nav-item" data-depth="2">
        <span class="nav-item-toggle">
    <a class="nav-link" href="../tenants/secure-connect.html">Create private network connections with Secure Connect</a>
        </span>
<ul class="nav-list">
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../tenants/secure-connect-configure-equinix.html">Configure Secure Connect with Equinix</a>
        
  </li>
</ul>
  </li>
  <li class="nav-item" data-depth="2">
        <span class="nav-item-toggle">
    <a class="nav-link" href="../tenants/proxy-connect.html">Restrict network access with Proxy Connect</a>
        </span>
<ul class="nav-list">
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../tenants/proxy-connect-ui.html">Manage using the admin console</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../tenants/proxy-connect-api.html">Manage using the API</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../tenants/proxy-connect-traffic-exemptions.html">Proxy Connect traffic exemptions</a>
        
  </li>
</ul>
  </li>
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="../realms/gateways-agents.html">Secure access to web resources</a>
        
  </li>
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="../tenants/cors.html">Allow cross-domain requests with CORS</a>
        
  </li>
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="../tenants/content-security-policy.html">Secure hosted pages with Content Security Policy</a>
        
  </li>
</ul>
  </li>
  <li class="nav-item" data-depth="1">
        <span class="nav-item-toggle">
    <a class="nav-link" href="../tenants/configuration-preface.html">Manage tenant configuration and ESVs</a>
        </span>
<ul class="nav-list">
  <li class="nav-item" data-depth="2">
        <span class="nav-item-toggle">
    <a class="nav-link" href="../tenants/esvs.html">ESVs</a>
        </span>
<ul class="nav-list">
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../tenants/esvs-manage-ui.html">Manage using the admin console</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../tenants/esvs-manage-api.html">Manage using the API</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../tenants/esvs-scripting.html">Use ESVs in scripts</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        <span class="nav-item-toggle">
    <a class="nav-link" href="../tenants/esvs-signing-encryption.html">Use ESVs for signing and encryption keys</a>
        </span>
<ul class="nav-list">
  <li class="nav-item" data-depth="4">
        
    <a class="nav-link" href="../tenants/esvs-rotate-saml2-certificates.html">Rotate SAML 2.0 certificates using ESVs</a>
        
  </li>
</ul>
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../tenants/esvs-override-global-configuration.html">Use ESVs to override global configuration</a>
        
  </li>
</ul>
  </li>
  <li class="nav-item" data-depth="2">
        <span class="nav-item-toggle">
    <a class="nav-link" href="../tenants/configuration-placeholders.html">Configure placeholders to use with ESVs</a>
        </span>
<ul class="nav-list">
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../tenants/configuration-placeholders-ui.html">Manage using the admin console</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../tenants/configuration-placeholders-api.html">Manage using the API</a>
        
  </li>
</ul>
  </li>
  <li class="nav-item" data-depth="2">
        <span class="nav-item-toggle">
    <a class="nav-link" href="../tenants/self-service-promotions.html">Promote your configuration</a>
        </span>
<ul class="nav-list">
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../tenants/self-service-promotions-faqs.html">Self-service promotion process FAQs</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../tenants/self-service-promotions-ui.html">Manage using the admin console</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../tenants/self-service-promotions-api.html">Manage using the API</a>
        
  </li>
</ul>
  </li>
</ul>
  </li>
  <li class="nav-item" data-depth="1">
        
    <a class="nav-link" href="../tenants/service-accounts.html">Access REST APIs using service accounts</a>
        
  </li>
  <li class="nav-item" data-depth="1">
        
    <a class="nav-link" href="../tenants/analytics-dashboard.html">Monitor tenant usage</a>
        
  </li>
  <li class="nav-item" data-depth="1">
        
    <a class="nav-link" href="../tenants/monitoring.html">Monitor tenant uptime and performance</a>
        
  </li>
  <li class="nav-item" data-depth="1">
        <span class="nav-item-toggle">
    <a class="nav-link" href="../tenants/audit-debug-logs.html">Get audit and debug logs</a>
        </span>
<ul class="nav-list">
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="../tenants/audit-debug-logs-pull.html">Retrieve log entries using REST API</a>
        
  </li>
  <li class="nav-item" data-depth="2">
        <span class="nav-item-toggle">
    <a class="nav-link" href="../tenants/audit-debug-logs-push.html">Stream logs to an external monitoring tool</a>
        </span>
<ul class="nav-list">
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../tenants/audit-debug-logs-push-api.html">Manage log streaming using the API</a>
        
  </li>
</ul>
  </li>
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="../tenants/audit-debug-logs-monitoring.html">Monitor log entries in the admin console</a>
        
  </li>
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="../tenants/audit-debug-log-sources.html">Log sources</a>
        
  </li>
</ul>
  </li>
  <li class="nav-item" data-depth="1">
        <span class="nav-item-toggle">
    <a class="nav-link" href="../tenants/email-configure.html">Configure email</a>
        </span>
<ul class="nav-list">
  <li class="nav-item" data-depth="2">
        <span class="nav-item-toggle">
    <a class="nav-link" href="../tenants/email-provider.html">Email provider</a>
        </span>
<ul class="nav-list">
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../tenants/email-provider-ui.html">Manage using the admin console</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../tenants/email-provider-api.html">Manage using the API</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../tenants/email-provider-configure-microsoft-azure-tenant.html">Configure a Microsoft Azure tenant for the Microsoft Graph email provider</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../tenants/email-provider-configuration-reference.html">Email provider configuration reference</a>
        
  </li>
</ul>
  </li>
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="../tenants/email-templates.html">Email templates</a>
        
  </li>
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="../tenants/email-send.html">Send email</a>
        
  </li>
</ul>
  </li>
</ul>
  </li>
  <li class="nav-item" data-depth="0">
    <h5 class="nav-title">Authentication</h5>
<ul class="nav-list">
  <li class="nav-item" data-depth="1">
        <span class="nav-item-toggle">
    <a class="nav-link" href="../journeys/journeys.html">Nodes and journeys</a>
        </span>
<ul class="nav-list">
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="../journeys/node-versions.html">Node versions</a>
        
  </li>
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="../journeys/auth-nodes.html">Journey nodes</a>
        
  </li>
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="../journeys/node-designer.html">Custom nodes</a>
        
  </li>
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="../journeys/marketplace.html">Marketplace journey nodes</a>
        
  </li>
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="../end-user/debug-enduser-journeys.html">Debug end-user journeys</a>
        
  </li>
  <li class="nav-item" data-depth="2">
        <span class="nav-item-toggle">
    <a class="nav-link" href="../self-service/self-service-journeys.html">Self-service journeys</a>
        </span>
<ul class="nav-list">
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../self-service/self-service-journeys-mappings.html">Self-service journey mappings</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../self-service/login.html">Sign-on (login)</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../self-service/username-recovery.html">Username recovery</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../self-service/password-reset.html">Password reset</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../self-service/update-password.html">Password update</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../self-service/self-registration.html">User self-registration</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../self-service/progressive-profile.html">Progressive profile</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../self-service/scripting-for-user-self-service.html">Scripting tips</a>
        
  </li>
</ul>
  </li>
  <li class="nav-item" data-depth="2">
        <span class="nav-item-toggle">
    <a class="nav-link" href="../journeys/solution-journeys.html">Sample journeys</a>
        </span>
<ul class="nav-list">
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../journeys/solution-login-with-self-service-journey.html">Sign on with self-service</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../journeys/solution-financial-services-journey.html">Financial services journey</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../journeys/solution-money-transfer-journey.html">Money transfer journey</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../journeys/solution-threat-detection-journey.html">Threat detection with PingOne Protect journey</a>
        
  </li>
</ul>
  </li>
</ul>
  </li>
  <li class="nav-item" data-depth="1">
        <span class="nav-item-toggle">
    <a class="nav-link" href="social-authentication.html">Social authentication</a>
        </span>
<ul class="nav-list">
  <li class="nav-item" data-depth="2">
        <span class="nav-item-toggle">
    <a class="nav-link" href="social-authentication-configure.html">Configure social authentication</a>
        </span>
<ul class="nav-list">
  <li class="nav-item is-current-page" data-depth="3">
        
    <a class="nav-link" href="social-authentication-settings.html">Social identity provider settings</a>
        
  </li>
</ul>
  </li>
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="social-authentication-journeys.html">Configure basic social registration journeys</a>
        
  </li>
</ul>
  </li>
  <li class="nav-item" data-depth="1">
        <span class="nav-item-toggle">
    <a class="nav-link" href="authentication-methods.html">Configure authentication methods</a>
        </span>
<ul class="nav-list">
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="authentication-methods-push-authentication.html">Push authentication</a>
        
  </li>
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="authentication-methods-push-notification.html">Push notification delivery</a>
        
  </li>
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="authentication-methods-totp.html">One-time passcode (TOTP)</a>
        
  </li>
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="authentication-methods-webauthn-verification.html">WebAuthn verification</a>
        
  </li>
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="authentication-methods-webauthn-encryption.html">WebAuthn storage and encryption</a>
        
  </li>
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="authentication-methods-device-binding.html">Device binding</a>
        
  </li>
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="authentication-methods-android-key-attestation.html">Android Key Attestation</a>
        
  </li>
</ul>
  </li>
  <li class="nav-item" data-depth="1">
        <span class="nav-item-toggle">
    <a class="nav-link" href="identity-verification.html">Configure identity verification</a>
        </span>
<ul class="nav-list">
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="identity-verification-jumio.html">Jumio</a>
        
  </li>
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="identity-verification-onespan.html">OneSpan</a>
        
  </li>
</ul>
  </li>
  <li class="nav-item" data-depth="1">
        
    <a class="nav-link" href="password-policy.html">Create end-user password policies</a>
        
  </li>
</ul>
  </li>
  <li class="nav-item" data-depth="0">
    <h5 class="nav-title">Authorization</h5>
<ul class="nav-list">
  <li class="nav-item" data-depth="1">
        <span class="nav-item-toggle">
    <a class="nav-link" href="../authorization/oauth2-provider.html">OAuth2 provider</a>
        </span>
<ul class="nav-list">
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="../authorization/oauth2-provider-settings.html">OAuth 2.0 provider settings</a>
        
  </li>
</ul>
  </li>
  <li class="nav-item" data-depth="1">
        
    <a class="nav-link" href="../authorization/remote-consent-service.html">Remote consent service</a>
        
  </li>
</ul>
  </li>
  <li class="nav-item" data-depth="0">
    <h5 class="nav-title">Application Management</h5>
<ul class="nav-list">
  <li class="nav-item" data-depth="1">
        <span class="nav-item-toggle">
    <a class="nav-link" href="../app-management/applications.html">Application management</a>
        </span>
<ul class="nav-list">
  <li class="nav-item" data-depth="2">
        <span class="nav-item-toggle">
    <a class="nav-link" href="../app-management/register-an-application.html">Register an application</a>
        </span>
<ul class="nav-list">
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../app-management/app-catalog.html">App catalog</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../app-management/register-a-template-application.html">Register an application from the app catalog</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../app-management/register-a-custom-application.html">Register a custom application</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../app-management/register-an-sso-application.html">Register a WS-Federation or WS-Trust application</a>
        
  </li>
</ul>
  </li>
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="../app-management/configure-app-authorization-policy.html">Configure an application authorization policy</a>
        
  </li>
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="../app-management/application-journeys.html">Application journeys</a>
        
  </li>
  <li class="nav-item" data-depth="2">
        <span class="nav-item-toggle">
    <a class="nav-link" href="../app-management/provision-an-application.html">Provision an application</a>
        </span>
<ul class="nav-list">
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../app-management/applications/active-directory.html">Active Directory</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../app-management/applications/adobe-admin-console.html">Adobe Admin Console</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../app-management/applications/as400.html">AS400</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../app-management/applications/atlassian-jira.html">Atlassian Jira</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../app-management/applications-agent-governance/aws-bedrock.html">AWS Bedrock</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../app-management/applications-agent-governance/aws-bedrock-agentcore.html">AWS Bedrock AgentCore</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../app-management/applications/aws-iam.html">AWS IAM</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../app-management/applications/aws-identity-center.html">AWS Identity Center</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../app-management/applications-agent-governance/azure-ai-foundry.html">Azure AI Foundry</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../app-management/applications/beyondtrust.html">BeyondTrust</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../app-management/applications/csv-file.html">CSV File</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../app-management/applications/database-table.html">Database Table</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../app-management/applications/directory-services.html">Directory Services (DS)</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../app-management/applications/docusign.html">DocuSign</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../app-management/applications/epic.html">Epic</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../app-management/applications-agent-governance/google-vertex-ai.html">Google Vertex AI</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../app-management/applications/google-workspace.html">Google Workspace</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../app-management/applications/ldap.html">LDAP</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../app-management/applications/microsoft-entra.html">Microsoft Entra</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../app-management/applications-agent-governance/microsoft-copilot-studio.html">Microsoft Copilot Studio</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../app-management/applications/csv-multifile.html">Multi-file CSV</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../app-management/applications/oracle-ebs.html">Oracle E-Business Suite (EBS)</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../app-management/applications/oracle-peoplesoft.html">Oracle PeopleSoft</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../app-management/applications/pingone.html">PingOne</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../app-management/applications/advanced-identity-cloud.html">PingOne Advanced Identity Cloud</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../app-management/applications/powershell.html">PowerShell</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../app-management/applications/saas-rest.html">SaaS REST</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../app-management/applications/saas-rest-rcs.html">SaaS REST (connector server)</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../app-management/applications/salesforce.html">Salesforce</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../app-management/applications/sap-s4hana.html">SAP S/4HANA</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../app-management/applications/sap-successfactors.html">SAP SuccessFactors</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../app-management/applications/sap-user-management.html">SAP User Management</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../app-management/applications/scim.html">SCIM</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../app-management/applications/scripted-groovy.html">Scripted Groovy</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../app-management/applications/scripted-rest.html">Scripted REST</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../app-management/applications/scripted-table.html">Scripted Table</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../app-management/applications/servicenow.html">ServiceNow</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../app-management/applications/snowflake.html">Snowflake</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../app-management/applications/webex.html">Webex</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../app-management/applications/workday.html">Workday</a>
        
  </li>
</ul>
  </li>
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="../app-management/manage-users-and-roles.html">Manage end users and roles</a>
        
  </li>
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="../app-management/manage-app-status.html">Manage application registrations</a>
        
  </li>
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="../app-management/standalone-oauth2-clients.html">Standalone OAuth 2.0 clients</a>
        
  </li>
  <li class="nav-item" data-depth="2">
        <span class="nav-item-toggle">
    <a class="nav-link" href="../app-management/standalone-provisioners.html">Standalone provisioners</a>
        </span>
<ul class="nav-list">
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../app-management/standalone-provisioner-properties.html">Manage properties</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../app-management/standalone-provisioner-schedules.html">Manage schedules</a>
        
  </li>
</ul>
  </li>
</ul>
  </li>
  <li class="nav-item" data-depth="1">
        <span class="nav-item-toggle">
    <a class="nav-link" href="../realms/applications.html">Application management (legacy)</a>
        </span>
<ul class="nav-list">
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="../realms/applications-saml2-jsp.html">Test SAML 2.0 SSO using JSP flows</a>
        
  </li>
</ul>
  </li>
</ul>
  </li>
  <li class="nav-item" data-depth="0">
    <h5 class="nav-title">Identities</h5>
<ul class="nav-list">
  <li class="nav-item" data-depth="1">
        
    <a class="nav-link" href="../identities/identity-cloud-identity-schema.html">Advanced Identity Cloud identity schema</a>
        
  </li>
  <li class="nav-item" data-depth="1">
        <span class="nav-item-toggle">
    <a class="nav-link" href="../identities/manage-identities.html">Manage identities</a>
        </span>
<ul class="nav-list">
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="../identities/roles-assignments.html">Roles and assignments</a>
        
  </li>
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="../identities/organizations.html">Organizations</a>
        
  </li>
</ul>
  </li>
  <li class="nav-item" data-depth="1">
        <span class="nav-item-toggle">
    <a class="nav-link" href="../identities/configure-object-types.html">Configure managed objects</a>
        </span>
<ul class="nav-list">
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="../identities/manage-object-types.html">Create and modify managed object types</a>
        
  </li>
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="../identities/customize-object-types.html">Customize managed object types</a>
        
  </li>
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="../identities/constrain-identity-queries.html">Constrain identity queries</a>
        
  </li>
  <li class="nav-item" data-depth="2">
        <span class="nav-item-toggle">
    <a class="nav-link" href="../identities/configure-relationships.html">Configure relationships</a>
        </span>
<ul class="nav-list">
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../identities/manage-rdvps.html">Manage relationship-derived virtual properties (RDVPs)</a>
        
  </li>
</ul>
  </li>
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="../identities/advanced-sync-managed-objects.html">Manage advanced sync</a>
        
  </li>
</ul>
  </li>
  <li class="nav-item" data-depth="1">
        <span class="nav-item-toggle">
    <a class="nav-link" href="../identities/advanced-sync.html">Advanced sync</a>
        </span>
<ul class="nav-list">
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="../identities/advanced-sync-mappings.html">Configure mappings</a>
        
  </li>
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="../identities/advanced-sync-correlation.html">Configure correlation</a>
        
  </li>
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="../identities/advanced-sync-reconciliation.html">Run reconciliation</a>
        
  </li>
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="../identities/advanced-sync-schedules.html">Manage schedules</a>
        
  </li>
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="../identities/advanced-sync-situation-rules.html">Define situation rules</a>
        
  </li>
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="../identities/advanced-sync-event-hooks.html">Configure event hooks</a>
        
  </li>
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="../identities/advanced-sync-advanced-reconciliation.html">Configure advanced reconciliation</a>
        
  </li>
</ul>
  </li>
  <li class="nav-item" data-depth="1">
        
    <a class="nav-link" href="../identities/user-identity-properties-attributes-reference.html">User identity attributes and properties reference</a>
        
  </li>
  <li class="nav-item" data-depth="1">
        <span class="nav-item-toggle">
    <a class="nav-link" href="../identities/import-sync-identities-preface.html">Import, sync, and migrate identities</a>
        </span>
<ul class="nav-list">
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="../identities/bulk-import-identities.html">Bulk import identities</a>
        
  </li>
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="../identities/sync-identities.html">Sync identities with an external resource</a>
        
  </li>
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="../identities/pass-through-authentication.html">Validate passwords with a remote service</a>
        
  </li>
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="../identities/manage-scheduled-jobs.html">Configure scheduled jobs</a>
        
  </li>
</ul>
  </li>
</ul>
  </li>
  <li class="nav-item" data-depth="0">
    <h5 class="nav-title">UIs &amp; User Experience</h5>
<ul class="nav-list">
  <li class="nav-item" data-depth="1">
        <span class="nav-item-toggle">
    <a class="nav-link" href="../end-user/end-user-ux-options.html">End-user UX options</a>
        </span>
<ul class="nav-list">
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="../end-user/end-user-ux-options-compare.html">Compare end-user UX options</a>
        
  </li>
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="../end-user/end-user-ux-journey-flows.html">End-user UX journey flows</a>
        
  </li>
  <li class="nav-item" data-depth="2">
        <span class="nav-item-toggle">
    <a class="nav-link" href="../end-user/sdks.html">Ping SDKs</a>
        </span>
<ul class="nav-list">
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../end-user/upload-android-assetlinks.html">Upload an Android assetlinks.json file</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../end-user/upload-ios-apple-app-site-association.html">Upload an iOS apple-app-site-association file</a>
        
  </li>
</ul>
  </li>
</ul>
  </li>
  <li class="nav-item" data-depth="1">
        <span class="nav-item-toggle">
    <a class="nav-link" href="../end-user/hosted-pages.html">Hosted pages</a>
        </span>
<ul class="nav-list">
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="../end-user/hosted-pages-customize.html">Customize hosted pages</a>
        
  </li>
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="../end-user/hosted-pages-localize.html">Localize hosted pages</a>
        
  </li>
  <li class="nav-item" data-depth="2">
        <span class="nav-item-toggle">
    <a class="nav-link" href="../end-user/hosted-account-pages.html">Hosted account pages</a>
        </span>
<ul class="nav-list">
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../end-user/hosted-account-pages-navigation-profiles.html">Manage navigation profiles</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../end-user/hosted-account-pages-navigation-menu-items-visibility-and-arrangement.html">Customize navigation menu items</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../end-user/hosted-account-pages-navigation-menu-supplementary-information.html">Navigation menu supplementary information</a>
        
  </li>
</ul>
  </li>
</ul>
  </li>
</ul>
  </li>
  <li class="nav-item" data-depth="0">
    <h5 class="nav-title">PingOne Services</h5>
<ul class="nav-list">
  <li class="nav-item" data-depth="1">
        <span class="nav-item-toggle">
    <a class="nav-link" href="../integrations/pingone.html">Integrate PingOne services for enhanced IAM capabilities</a>
        </span>
<ul class="nav-list">
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="../integrations/pingone-set-up-environments.html">Set up mapped PingOne environments</a>
        
  </li>
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="../integrations/pingone-set-up-product-connections.html">Set up PingOne product connections</a>
        
  </li>
</ul>
  </li>
  <li class="nav-item" data-depth="1">
        <span class="nav-item-toggle">
    <a class="nav-link" href="../integrations/pingone-protect.html">Use PingOne Protect for risk-based authentication and fraud detection</a>
        </span>
<ul class="nav-list">
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="../integrations/pingone-protect-use-cases.html">PingOne Protect use cases</a>
        
  </li>
</ul>
  </li>
  <li class="nav-item" data-depth="1">
        
    <a class="nav-link" href="../integrations/pingone-verify.html">Use PingOne Verify for identity verification and proofing capabilities</a>
        
  </li>
  <li class="nav-item" data-depth="1">
        
    <a class="nav-link" href="../integrations/pingone-credentials.html">Use PingOne Credentials to issue and manage digital verifiable credentials</a>
        
  </li>
</ul>
  </li>
  <li class="nav-item" data-depth="0">
    <h5 class="nav-title">Identity Governance</h5>
<ul class="nav-list">
  <li class="nav-item" data-depth="1">
        
    <a class="nav-link" href="../identity-governance/administration/getting-started-what-is-iga.html">What is Identity Governance</a>
        
  </li>
  <li class="nav-item" data-depth="1">
        <span class="nav-item-toggle">
    <a class="nav-link" href="../identity-governance/administration/administator-tasks-preface.html">Administrator tasks</a>
        </span>
<ul class="nav-list">
  <li class="nav-item" data-depth="2">
        <span class="nav-item-toggle">
    <a class="nav-link" href="../identity-governance/administration/admin-ui.html">Getting started</a>
        </span>
<ul class="nav-list">
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../identity-governance/administration/getting-started-key-considerations.html">Key considerations</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../identity-governance/administration/getting-started-general-setup-steps.html">General IGA process</a>
        
  </li>
</ul>
  </li>
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="../identity-governance/administration/view-access-graph.html">Access graph</a>
        
  </li>
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="../identity-governance/administration/governance-accounts.html">Manage accounts</a>
        
  </li>
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="../identity-governance/administration/governance-audit-log.html">Audit logs</a>
        
  </li>
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="../identity-governance/administration/unmanaged-apps.html">Unmanaged applications</a>
        
  </li>
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="../identity-governance/administration/scopes.html">Manage scopes</a>
        
  </li>
  <li class="nav-item" data-depth="2">
        <span class="nav-item-toggle">
    <a class="nav-link" href="../identity-governance/administration/entitlements.html">Entitlements</a>
        </span>
<ul class="nav-list">
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../identity-governance/administration/entitlements-prepare-applications.html">Prepare applications for entitlements</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../identity-governance/administration/entitlements-manage.html">Manage entitlements</a>
        
  </li>
</ul>
  </li>
  <li class="nav-item" data-depth="2">
        <span class="nav-item-toggle">
    <a class="nav-link" href="../identity-governance/administration/access-request-preface.html">Access requests</a>
        </span>
<ul class="nav-list">
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../identity-governance/administration/glossary.html">Manage governance glossary</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../identity-governance/administration/governance-request-types.html">Manage access requests and request types</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        <span class="nav-item-toggle">
    <a class="nav-link" href="../identity-governance/administration/workflow-configure.html">Manage workflows</a>
        </span>
<ul class="nav-list">
  <li class="nav-item" data-depth="4">
        
    <a class="nav-link" href="../identity-governance/administration/workflow-nodes.html">Workflow nodes</a>
        
  </li>
  <li class="nav-item" data-depth="4">
        
    <a class="nav-link" href="../identity-governance/administration/workflow-modify-default.html">Copy and edit the default workflows</a>
        
  </li>
  <li class="nav-item" data-depth="4">
        
    <a class="nav-link" href="../identity-governance/administration/workflow-modify-default-email-templates.html">Modify default workflow email templates</a>
        
  </li>
  <li class="nav-item" data-depth="4">
        
    <a class="nav-link" href="../identity-governance/administration/workflow-create-rest.html">Create workflows using REST APIs</a>
        
  </li>
  <li class="nav-item" data-depth="4">
        
    <a class="nav-link" href="../identity-governance/administration/workflow-examples.html">Workflow use cases</a>
        
  </li>
</ul>
  </li>
  <li class="nav-item" data-depth="3">
        <span class="nav-item-toggle">
    <a class="nav-link" href="../identity-governance/administration/governance-forms.html">Manage forms</a>
        </span>
<ul class="nav-list">
  <li class="nav-item" data-depth="4">
        
    <a class="nav-link" href="../identity-governance/administration/governance-forms-events.html">Form events</a>
        
  </li>
  <li class="nav-item" data-depth="4">
        
    <a class="nav-link" href="../identity-governance/administration/governance-forms-fields.html">Form fields</a>
        
  </li>
  <li class="nav-item" data-depth="4">
        
    <a class="nav-link" href="../identity-governance/administration/governance-forms-app-request.html">Create an application request form</a>
        
  </li>
  <li class="nav-item" data-depth="4">
        
    <a class="nav-link" href="../identity-governance/administration/governance-forms-custom-request.html">Create a form for custom request types</a>
        
  </li>
</ul>
  </li>
  <li class="nav-item" data-depth="3">
        <span class="nav-item-toggle">
    <a class="nav-link" href="../identity-governance/administration/access-request-configure.html">Manage access requests</a>
        </span>
<ul class="nav-list">
  <li class="nav-item" data-depth="4">
        
    <a class="nav-link" href="../identity-governance/administration/access-request-admin-console.html">Review request items using the admin UI</a>
        
  </li>
  <li class="nav-item" data-depth="4">
        
    <a class="nav-link" href="../identity-governance/administration/configure-user-display-properties.html">Configure user display properties</a>
        
  </li>
  <li class="nav-item" data-depth="4">
        
    <a class="nav-link" href="../identity-governance/administration/troubleshooting-access-requests.html">Troubleshooting access requests</a>
        
  </li>
</ul>
  </li>
</ul>
  </li>
  <li class="nav-item" data-depth="2">
        <span class="nav-item-toggle">
    <a class="nav-link" href="../identity-governance/administration/access-review-certification-preface.html">Certification campaigns</a>
        </span>
<ul class="nav-list">
  <li class="nav-item" data-depth="3">
        <span class="nav-item-toggle">
    <a class="nav-link" href="../identity-governance/administration/access-review-manage-templates.html">Configure data to review using templates</a>
        </span>
<ul class="nav-list">
  <li class="nav-item" data-depth="4">
        
    <a class="nav-link" href="../identity-governance/administration/template-identity-cert.html">Identity certification</a>
        
  </li>
  <li class="nav-item" data-depth="4">
        
    <a class="nav-link" href="../identity-governance/administration/template-entitlement-cert.html">Entitlement assignment certification</a>
        
  </li>
  <li class="nav-item" data-depth="4">
        
    <a class="nav-link" href="../identity-governance/administration/template-role-membership-cert.html">Role membership certification</a>
        
  </li>
  <li class="nav-item" data-depth="4">
        
    <a class="nav-link" href="../identity-governance/administration/template-entitlement-composition.html">Entitlement composition certification</a>
        
  </li>
  <li class="nav-item" data-depth="4">
        
    <a class="nav-link" href="../identity-governance/administration/template-identity-profile-cert.html">Identity profile certification</a>
        
  </li>
  <li class="nav-item" data-depth="4">
        
    <a class="nav-link" href="../identity-governance/administration/template-role-composition-cert.html">Role composition certification</a>
        
  </li>
</ul>
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../identity-governance/administration/access-review-manage-campaigns.html">Kick off data review using campaigns</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../identity-governance/administration/organization-certification-preface.html">Certify access by organization</a>
        
  </li>
</ul>
  </li>
  <li class="nav-item" data-depth="2">
        <span class="nav-item-toggle">
    <a class="nav-link" href="../identity-governance/administration/event-certification-preface.html">Events</a>
        </span>
<ul class="nav-list">
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../identity-governance/administration/event-certification-editor.html">Create a certification event</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../identity-governance/administration/event-workflow-editor.html">Create a workflow event</a>
        
  </li>
</ul>
  </li>
  <li class="nav-item" data-depth="2">
        <span class="nav-item-toggle">
    <a class="nav-link" href="../identity-governance/administration/sod-policies-preface.html">Segregation of duties</a>
        </span>
<ul class="nav-list">
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../identity-governance/administration/sod-rules.html">Manage rules</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../identity-governance/administration/sod-policies.html">Manage policies</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../identity-governance/administration/sod-policy-scans.html">Manage policy scans</a>
        
  </li>
</ul>
  </li>
  <li class="nav-item" data-depth="2">
        <span class="nav-item-toggle">
    <a class="nav-link" href="../identity-governance/administration/governance-lifecycle-mgmt.html">Governance lifecycle management</a>
        </span>
<ul class="nav-list">
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../identity-governance/administration/governance-lcm-authorization.html">Access authorization</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../identity-governance/administration/lcm-user.html">Configure user lifecycle management</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../identity-governance/administration/lcm-role.html">Configure role lifecycle management</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../identity-governance/administration/lcm-entitlement.html">Configure entitlement lifecycle management</a>
        
  </li>
</ul>
  </li>
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="../identity-governance/administration/governance-notifications.html">Notifications</a>
        
  </li>
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="../identity-governance/administration/governance-recommendations-preface.html">Recommendations</a>
        
  </li>
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="../identity-governance/administration/iga-reports.html">Reports</a>
        
  </li>
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="../identity-governance/administration/iga-agent-governance.html">Agent Governance</a>
        
  </li>
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="../identity-governance/administration/governance-activity-collectors.html">Activity collectors</a>
        
  </li>
  <li class="nav-item" data-depth="2">
        <span class="nav-item-toggle">
    <a class="nav-link" href="../identity-governance/rest-api/rest-api-preface.html">REST API</a>
        </span>
<ul class="nav-list">
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../identity-governance/rest-api/endpoints/rest-iga-access-token.html">Generate an access token</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../identity-governance/rest-api/endpoints/rest-iga.html">Identity Governance API</a>
        
  </li>
</ul>
  </li>
</ul>
  </li>
  <li class="nav-item" data-depth="1">
        <span class="nav-item-toggle">
    <a class="nav-link" href="../identity-governance/administration/access-modeling-preface.html">Access Modeling</a>
        </span>
<ul class="nav-list">
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="../identity-governance/administration/iga-access-modeling-admin.html">Administer Access Modeling</a>
        
  </li>
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="../identity-governance/end-user/iga-access-modeling-end-user.html">Use Access Modeling</a>
        
  </li>
</ul>
  </li>
  <li class="nav-item" data-depth="1">
        <span class="nav-item-toggle">
    <a class="nav-link" href="../identity-governance/end-user/end-user-tasks-preface.html">End-user tasks</a>
        </span>
<ul class="nav-list">
  <li class="nav-item" data-depth="2">
        <span class="nav-item-toggle">
    <a class="nav-link" href="../identity-governance/end-user/end-user-ui.html">Getting started</a>
        </span>
<ul class="nav-list">
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../identity-governance/end-user/end-user-recommendations.html">End-user recommendations</a>
        
  </li>
</ul>
  </li>
  <li class="nav-item" data-depth="2">
        <span class="nav-item-toggle">
    <a class="nav-link" href="../identity-governance/end-user/manage-inbox-preface.html">Manage inbox</a>
        </span>
<ul class="nav-list">
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../identity-governance/end-user/access-request-approve-access.html">Approve access</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../identity-governance/end-user/fulfillment-tasks.html">Manage tasks</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../identity-governance/end-user/access-review-user-cert-items.html">Run access reviews</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../identity-governance/end-user/sod-violations.html">Manage violations</a>
        
  </li>
</ul>
  </li>
  <li class="nav-item" data-depth="2">
        <span class="nav-item-toggle">
    <a class="nav-link" href="../identity-governance/end-user/manage-my-access-preface.html">Manage my access</a>
        </span>
<ul class="nav-list">
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../identity-governance/end-user/manage-my-roles.html">Manage my roles</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../identity-governance/end-user/manage-my-entitlements.html">Manage my entitlements</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../identity-governance/end-user/manage-my-machine-accounts.html">Manage my machine accounts</a>
        
  </li>
</ul>
  </li>
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="../identity-governance/end-user/manage-my-directory-preface.html">Manage my directory</a>
        
  </li>
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="../identity-governance/end-user/manage-my-requests-preface.html">Manage my requests</a>
        
  </li>
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="../identity-governance/end-user/iga-agent-governance-enduser.html">Agent Governance: custodian and reviewer tasks</a>
        
  </li>
  <li class="nav-item" data-depth="2">
        <span class="nav-item-toggle">
    <a class="nav-link" href="../identity-governance/end-user/administer-preface.html">Manage users, roles, and entitlements</a>
        </span>
<ul class="nav-list">
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../identity-governance/end-user/manage-user-lcm.html">Manage users</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../identity-governance/end-user/manage-role-lcm.html">Manage roles</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../identity-governance/end-user/manage-entitlement-lcm.html">Manage entitlements</a>
        
  </li>
</ul>
  </li>
</ul>
  </li>
</ul>
  </li>
  <li class="nav-item" data-depth="0">
    <h5 class="nav-title">Reports</h5>
<ul class="nav-list">
  <li class="nav-item" data-depth="1">
        
    <a class="nav-link" href="../reports/administration/about-reports.html">About reports</a>
        
  </li>
  <li class="nav-item" data-depth="1">
        
    <a class="nav-link" href="../reports/administration/reports-important-points.html">Important points</a>
        
  </li>
  <li class="nav-item" data-depth="1">
        
    <a class="nav-link" href="../reports/administration/analytic-reports.html">Manage reports</a>
        
  </li>
  <li class="nav-item" data-depth="1">
        <span class="nav-item-toggle">
    <a class="nav-link" href="../reports/administration/advanced-reports.html">Advanced Reporting</a>
        </span>
<ul class="nav-list">
  <li class="nav-item" data-depth="2">
        <span class="nav-item-toggle">
    <a class="nav-link" href="../reports/use-cases/use-cases-reports.html">Use cases</a>
        </span>
<ul class="nav-list">
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../reports/use-cases/custom-attributes-for-user-in-advanced-reports.html">Custom attribute for user objects</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../reports/use-cases/custom-attributes-for-relationship-in-advanced-reports.html">Custom attribute for relationships</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../reports/use-cases/custom-attributes-for-organization-in-advanced-reports.html">Custom attribute for organization objects</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../reports/use-cases/custom-objects-reports.html">Custom objects use cases</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../reports/use-cases/use-case-historical-data-reporting.html">Historical data report</a>
        
  </li>
</ul>
  </li>
</ul>
  </li>
  <li class="nav-item" data-depth="1">
        
    <a class="nav-link" href="../reports/rest-api/reports-api.html">Reports API</a>
        
  </li>
</ul>
  </li>
  <li class="nav-item" data-depth="0">
    <h5 class="nav-title">Access Management</h5>
<ul class="nav-list">
  <li class="nav-item" data-depth="1">
        <span class="nav-item-toggle">
    <a class="nav-link" href="../am-authentication/preface.html">Authentication and SSO</a>
        </span>
<ul class="nav-list">
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="../am-authentication/authn-introduction-authn.html">What is authentication in Advanced Identity Cloud?</a>
        
  </li>
  <li class="nav-item" data-depth="2">
        <span class="nav-item-toggle">
    <a class="nav-link" href="../am-authentication/authn-implementation-authn.html">Configure authentication</a>
        </span>
<ul class="nav-list">
  <li class="nav-item" data-depth="3">
        <span class="nav-item-toggle">
    <a class="nav-link" href="../am-authentication/auth-nodes-and-journeys.html">Nodes and journeys</a>
        </span>
<ul class="nav-list">
  <li class="nav-item" data-depth="4">
        
    <a class="nav-link" href="../am-authentication/configure-authentication-trees.html">Configure journeys</a>
        
  </li>
  <li class="nav-item" data-depth="4">
        
    <a class="nav-link" href="../am-authentication/list-latest-node-definitions.html">List latest node definitions</a>
        
  </li>
  <li class="nav-item" data-depth="4">
        
    <a class="nav-link" href="../am-authentication/auth-tree-webhooks.html">Configure authentication webhooks</a>
        
  </li>
</ul>
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../am-authentication/redirection-url-precedence.html">Redirect users on authentication success/failure</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../am-authentication/realm-auth-config.html">Configure authentication settings</a>
        
  </li>
</ul>
  </li>
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="../am-authentication/authn-from-browser.html">Authenticate with a browser</a>
        
  </li>
  <li class="nav-item" data-depth="2">
        <span class="nav-item-toggle">
    <a class="nav-link" href="../am-authentication/authn-rest.html">Authenticate over REST</a>
        </span>
<ul class="nav-list">
  <li class="nav-item" data-depth="3">
        <span class="nav-item-toggle">
    <a class="nav-link" href="../am-authentication/login-using-rest.html">Log in over REST</a>
        </span>
<ul class="nav-list">
  <li class="nav-item" data-depth="4">
        
    <a class="nav-link" href="../am-authentication/authenticate-endpoint-parameters.html">Authenticate endpoints</a>
        
  </li>
</ul>
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../am-authentication/rest-using-ssotokens.html">Session tokens after authentication</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../am-authentication/logout-using-rest.html">Log out over REST</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        <span class="nav-item-toggle">
    <a class="nav-link" href="../am-authentication/callbacks-supported.html">Return callback information</a>
        </span>
<ul class="nav-list">
  <li class="nav-item" data-depth="4">
        
    <a class="nav-link" href="../am-authentication/callbacks-interactive.html">Interactive callbacks</a>
        
  </li>
  <li class="nav-item" data-depth="4">
        
    <a class="nav-link" href="../am-authentication/callbacks-read-only.html">Read-only callbacks</a>
        
  </li>
  <li class="nav-item" data-depth="4">
        
    <a class="nav-link" href="../am-authentication/callbacks-backchannel.html">Backchannel callbacks</a>
        
  </li>
</ul>
  </li>
</ul>
  </li>
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="../am-authentication/about-sso.html">Single sign-on</a>
        
  </li>
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="../am-authentication/suspended-auth.html">Suspend journey progress</a>
        
  </li>
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="../am-authentication/backchannel-authentication.html">Backchannel authentication</a>
        
  </li>
  <li class="nav-item" data-depth="2">
        <span class="nav-item-toggle">
    <a class="nav-link" href="../am-authentication/authn-mfa.html">Multi-factor authentication (MFA)</a>
        </span>
<ul class="nav-list">
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../am-authentication/authn-mfa-webauthn.html">Authenticate using a device</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        <span class="nav-item-toggle">
    <a class="nav-link" href="../am-authentication/authn-mfa-about-push.html">Authenticate using push notification</a>
        </span>
<ul class="nav-list">
  <li class="nav-item" data-depth="4">
        
    <a class="nav-link" href="../am-authentication/push-authentication-journeys.html">Configure journeys for push notifications</a>
        
  </li>
  <li class="nav-item" data-depth="4">
        
    <a class="nav-link" href="../am-authentication/mfa-authenticating-push.html">Test push authentication</a>
        
  </li>
  <li class="nav-item" data-depth="4">
        
    <a class="nav-link" href="../am-authentication/mfa-push-passwordless-limitations.html">Limitations of passwordless push authentication</a>
        
  </li>
</ul>
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../am-authentication/authn-mfa-about-oath.html">Authenticate using OTPs from an authenticator app</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        <span class="nav-item-toggle">
    <a class="nav-link" href="../am-authentication/authn-mfa-devices.html">Manage devices for MFA</a>
        </span>
<ul class="nav-list">
  <li class="nav-item" data-depth="4">
        
    <a class="nav-link" href="../am-authentication/authenticator-app.html">Authenticator apps</a>
        
  </li>
  <li class="nav-item" data-depth="4">
        
    <a class="nav-link" href="../am-authentication/register-authenticator-app.html">Register an authenticator app</a>
        
  </li>
  <li class="nav-item" data-depth="4">
        
    <a class="nav-link" href="../am-authentication/authn-mfa-using-lost.html">Recover after replacing a lost device</a>
        
  </li>
  <li class="nav-item" data-depth="4">
        
    <a class="nav-link" href="../am-authentication/authn-mfa-using-out-of-sync.html">Recover after a device becomes out of sync</a>
        
  </li>
  <li class="nav-item" data-depth="4">
        
    <a class="nav-link" href="../am-authentication/authn-mfa-reset-devices.html">Reset registered devices using REST</a>
        
  </li>
  <li class="nav-item" data-depth="4">
        
    <a class="nav-link" href="../am-authentication/authn-mfa-list-devices.html">List registered devices over REST</a>
        
  </li>
  <li class="nav-item" data-depth="4">
        
    <a class="nav-link" href="../am-authentication/rename-mfa-devices.html">Rename registered devices over REST</a>
        
  </li>
</ul>
  </li>
</ul>
  </li>
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="../am-authentication/radius-authentication.html">RADIUS authentication</a>
        
  </li>
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="../am-authentication/account-lockout.html">Account lockout</a>
        
  </li>
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="../am-authentication/authn-reference.html">Authentication reference</a>
        
  </li>
</ul>
  </li>
  <li class="nav-item" data-depth="1">
        <span class="nav-item-toggle">
    <a class="nav-link" href="../am-authorization/preface.html">Authorization</a>
        </span>
<ul class="nav-list">
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="../am-authorization/what-is-authz-decision.html">What is authorization in Advanced Identity Cloud?</a>
        
  </li>
  <li class="nav-item" data-depth="2">
        <span class="nav-item-toggle">
    <a class="nav-link" href="../am-authorization/configuring-policies.html">Grant access through policies</a>
        </span>
<ul class="nav-list">
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../am-authorization/policies-ui.html">Policies in the UI</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../am-authorization/rest-api-authz-policies.html">Policies over REST</a>
        
  </li>
</ul>
  </li>
  <li class="nav-item" data-depth="2">
        <span class="nav-item-toggle">
    <a class="nav-link" href="../am-authorization/configuring-resource-types.html">Define a template for policy resources</a>
        </span>
<ul class="nav-list">
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../am-authorization/resource-types-ui.html">Resource types in the UI</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../am-authorization/rest-api-authz-resource-types.html">Resource types over REST</a>
        
  </li>
</ul>
  </li>
  <li class="nav-item" data-depth="2">
        <span class="nav-item-toggle">
    <a class="nav-link" href="../am-authorization/configuring-policy-sets.html">Group similar policies through policy sets</a>
        </span>
<ul class="nav-list">
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../am-authorization/policy-sets-ui.html">Policy sets in the UI</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../am-authorization/rest-api-authz-applications.html">Policy sets over REST</a>
        
  </li>
</ul>
  </li>
  <li class="nav-item" data-depth="2">
        <span class="nav-item-toggle">
    <a class="nav-link" href="../am-authorization/requesting-authorization.html">Request authorization from Advanced Identity Cloud</a>
        </span>
<ul class="nav-list">
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../am-authorization/rest-api-authz-policy-decisions.html">Request policy decisions over REST</a>
        
  </li>
</ul>
  </li>
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="../am-authorization/transactional-authorization.html">Authorize one-time access</a>
        
  </li>
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="../am-authorization/oauth2-authorization.html">Dynamic OAuth 2.0 authorization</a>
        
  </li>
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="../am-authorization/scripted-policy-condition.html">Create scripts for policy evaluation</a>
        
  </li>
</ul>
  </li>
  <li class="nav-item" data-depth="1">
        <span class="nav-item-toggle">
    <a class="nav-link" href="../am-sessions/preface.html">Sessions</a>
        </span>
<ul class="nav-list">
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="../am-sessions/about-sessions.html">Introduction to sessions and cookies</a>
        
  </li>
  <li class="nav-item" data-depth="2">
        <span class="nav-item-toggle">
    <a class="nav-link" href="../am-sessions/client-side-sessions.html">Client-side sessions</a>
        </span>
<ul class="nav-list">
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../am-sessions/configure-client-side-sessions.html">Configure client-side sessions</a>
        
  </li>
</ul>
  </li>
  <li class="nav-item" data-depth="2">
        <span class="nav-item-toggle">
    <a class="nav-link" href="../am-sessions/server-side-sessions.html">Server-side sessions</a>
        </span>
<ul class="nav-list">
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../am-sessions/configure-server-side-sessions.html">Configure server-side sessions</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../am-sessions/manage-sessions-ui.html">View and terminate sessions (UI)</a>
        
  </li>
</ul>
  </li>
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="../am-sessions/session-state-session-termination.html">Configure session termination</a>
        
  </li>
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="../am-sessions/enable-active-session-quotas.html">Manage active session quotas</a>
        
  </li>
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="../am-sessions/managing-sessions-REST.html">Manage sessions over REST</a>
        
  </li>
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="../am-sessions/session-upgrade.html">Upgrade a session with multi-factor authentication (MFA)</a>
        
  </li>
</ul>
  </li>
  <li class="nav-item" data-depth="1">
        <span class="nav-item-toggle">
    <a class="nav-link" href="../am-oauth2/preface.html">OAuth 2.0</a>
        </span>
<ul class="nav-list">
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="../am-oauth2/am-as-authz-server.html">How Advanced Identity Cloud works as an authorization server</a>
        
  </li>
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="../am-oauth2/openam-oauth2-client.html">How Advanced Identity Cloud works as a client and resource server</a>
        
  </li>
  <li class="nav-item" data-depth="2">
        <span class="nav-item-toggle">
    <a class="nav-link" href="../am-oauth2/token-storage.html">Token storage</a>
        </span>
<ul class="nav-list">
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../am-oauth2/client-side-tokens.html">Client-side tokens</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../am-oauth2/server-side-tokens.html">Server-side tokens</a>
        
  </li>
</ul>
  </li>
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="../am-oauth2/oauth2-scopes.html">Scopes</a>
        
  </li>
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="../am-oauth2/oauth2-manage-consent.html">Manage consent</a>
        
  </li>
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="../am-oauth2/oauth2-remote-consent.html">Remote consent</a>
        
  </li>
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="../am-oauth2/oauth2-register-client.html">Register client applications</a>
        
  </li>
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="../am-oauth2/oauth2-cimd.html">Client ID metadata document (CIMD)</a>
        
  </li>
  <li class="nav-item" data-depth="2">
        <span class="nav-item-toggle">
    <a class="nav-link" href="../am-oauth2/oauth2-client-auth.html">Authenticate OAuth2.0 client applications</a>
        </span>
<ul class="nav-list">
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../am-oauth2/client-auth-header.html">Use an authorization header (HTTP Basic)</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../am-oauth2/client-auth-form.html">Use form parameters (HTTP Post)</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../am-oauth2/client-auth-jwt.html">Use a JWT profile</a>
        
  </li>
</ul>
  </li>
  <li class="nav-item" data-depth="2">
        <span class="nav-item-toggle">
    <a class="nav-link" href="../am-oauth2/oauth2-proof-of-possession.html">Prove client identity with proof-of-possession</a>
        </span>
<ul class="nav-list">
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../am-oauth2/oauth2-PoP-JWK.html">Use JWK-based proof-of-possession</a>
        
  </li>
</ul>
  </li>
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="../am-oauth2/oauth2-refresh-tokens.html">Issue refresh tokens</a>
        
  </li>
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="../am-oauth2/oauth2-macaroons.html">Share tokens using macaroons</a>
        
  </li>
  <li class="nav-item" data-depth="2">
        <span class="nav-item-toggle">
    <a class="nav-link" href="../am-oauth2/oauth2-implementing-flows.html">OAuth 2.0 grant flows</a>
        </span>
<ul class="nav-list">
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../am-oauth2/oauth2-authz-grant.html">Authorization code grant</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../am-oauth2/oauth2-authz-grant-pkce.html">Authorization code grant with PKCE</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../am-oauth2/oauth2-authz-grant-par.html">Authorization code grant with PAR</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../am-oauth2/oauth2-implicit-grant.html">Implicit grant</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../am-oauth2/oauth2-ropc-grant.html">Resource owner password credentials grant</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../am-oauth2/oauth2-client-cred-grant.html">Client credentials grant</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../am-oauth2/oauth2-device-flow.html">Device authorization grant</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../am-oauth2/oauth2-device-flow-pkce.html">Device authorization grant with PKCE</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../am-oauth2/oauth2-saml2-bearer-grant.html">SAML 2.0 profile for authorization</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../am-oauth2/oauth2-jwt-bearer-grant.html">JWT profile for authorization</a>
        
  </li>
</ul>
  </li>
  <li class="nav-item" data-depth="2">
        <span class="nav-item-toggle">
    <a class="nav-link" href="../am-oauth2/token-exchange.html">Exchange tokens for impersonation or delegation</a>
        </span>
<ul class="nav-list">
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../am-oauth2/token-exchange-impersonation.html">Example of impersonation</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../am-oauth2/token-exchange-delegation.html">Example of delegation</a>
        
  </li>
</ul>
  </li>
  <li class="nav-item" data-depth="2">
        <span class="nav-item-toggle">
    <a class="nav-link" href="../am-oauth2/oauth2-client-endpoints.html">OAuth 2.0 endpoints</a>
        </span>
<ul class="nav-list">
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../am-oauth2/oauth2-parameters.html">OAuth 2.0 endpoint parameters</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../am-oauth2/oauth2-par-endpoint.html">/oauth2/par</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../am-oauth2/oauth2-authorize-endpoint.html">/oauth2/authorize</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../am-oauth2/oauth2-bc-authorize-endpoint.html">/oauth2/bc-authorize</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../am-oauth2/oauth2-access_token-endpoint.html">/oauth2/access_token</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../am-oauth2/rest-api-oauth2-device-code.html">/oauth2/device/code</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../am-oauth2/rest-api-oauth2-device-user.html">/oauth2/device/user</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../am-oauth2/oauth2-token-revoke-endpoint.html">/oauth2/token/revoke</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../am-oauth2/oauth2-introspect-endpoint.html">/oauth2/introspect</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../am-oauth2/oauth2-introspect-macaroon-endpoint.html">/json/token/macaroon</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../am-oauth2/legacy-oauth2-endpoints.html">/oauth2/tokeninfo (Legacy)</a>
        
  </li>
</ul>
  </li>
  <li class="nav-item" data-depth="2">
        <span class="nav-item-toggle">
    <a class="nav-link" href="../am-oauth2/oauth2-admin-endpoints.html">OAuth 2.0 administration endpoints</a>
        </span>
<ul class="nav-list">
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../am-oauth2/rest-api-oauth2-client-admin-endpoint.html">/realm-config/agents/OAuth2Client</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../am-oauth2/rest-api-oauth2-applications-endpoint.html">/users/user/oauth2/applications</a>
        
  </li>
</ul>
  </li>
  <li class="nav-item" data-depth="2">
        <span class="nav-item-toggle">
    <a class="nav-link" href="../am-oauth2/plugins-customize.html">Customize OAuth 2.0 with JavaScript</a>
        </span>
<ul class="nav-list">
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../am-oauth2/modifying-access-tokens-scripts.html">Access tokens</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../am-oauth2/plugins-auth-endpoint-data-provider.html">Authorize endpoint data provider</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../am-oauth2/plugins-scope-evaluator.html">Scope evaluation</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../am-oauth2/plugins-scope-validator.html">Scope validation</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../am-oauth2/plugins-user-info-claims.html">Modify &amp; override claims</a>
        
  </li>
</ul>
  </li>
</ul>
  </li>
  <li class="nav-item" data-depth="1">
        <span class="nav-item-toggle">
    <a class="nav-link" href="../am-oidc1/preface.html">OIDC 1.0</a>
        </span>
<ul class="nav-list">
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="../am-oidc1/oidc-am-provider.html">How Advanced Identity Cloud works as an OIDC provider</a>
        
  </li>
  <li class="nav-item" data-depth="2">
        <span class="nav-item-toggle">
    <a class="nav-link" href="../am-oidc1/configure-openid-connect-provider.html">Configure the OIDC provider</a>
        </span>
<ul class="nav-list">
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../am-oidc1/encrypting-oidc-idtokens.html">Encrypt ID tokens and backchannel logout tokens</a>
        
  </li>
</ul>
  </li>
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="../am-oidc1/understanding-openid-connect-scopes-and-claims.html">Claims</a>
        
  </li>
  <li class="nav-item" data-depth="2">
        <span class="nav-item-toggle">
    <a class="nav-link" href="../am-oidc1/oauth2-dynamic-client-registration.html">Register clients dynamically</a>
        </span>
<ul class="nav-list">
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../am-oidc1/dynamic-client-registration-script.html">Customize dynamic client registration</a>
        
  </li>
</ul>
  </li>
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="../am-oidc1/oidc-client-auth.html">Authenticate OIDC clients</a>
        
  </li>
  <li class="nav-item" data-depth="2">
        <span class="nav-item-toggle">
    <a class="nav-link" href="../am-oidc1/oidc-implementing-flows.html">Implement OIDC grant flows</a>
        </span>
<ul class="nav-list">
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../am-oidc1/openid-connect-backchannel-request-flow.html">Backchannel request grant</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../am-oidc1/openid-connect-hybrid-flow.html">Hybrid grant</a>
        
  </li>
</ul>
  </li>
  <li class="nav-item" data-depth="2">
        <span class="nav-item-toggle">
    <a class="nav-link" href="../am-oidc1/manage-sessions-openid-connect.html">Manage OIDC authenticated sessions</a>
        </span>
<ul class="nav-list">
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../am-oidc1/session-management.html">Manage sessions</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../am-oidc1/backchannel-logout.html">Backchannel logout</a>
        
  </li>
</ul>
  </li>
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="../am-oidc1/oidc-authentication-requirements.html">Authentication requirements</a>
        
  </li>
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="../am-oidc1/oidc-mobile-connect.html">Authenticate using GSMA mobile connect</a>
        
  </li>
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="../am-oidc1/oidc-additional-use-cases.html">ID token uses</a>
        
  </li>
  <li class="nav-item" data-depth="2">
        <span class="nav-item-toggle">
    <a class="nav-link" href="../am-oidc1/oidc-client-endpoints.html">OIDC 1.0 endpoints</a>
        </span>
<ul class="nav-list">
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../am-oidc1/rest-api-oidc-userinfo-endpoint.html">/oauth2/userinfo</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../am-oidc1/rest-api-oidc-idtoken-validation.html">/oauth2/idtokeninfo</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../am-oidc1/rest-api-oidc-checksession-endpoint.html">/oauth2/connect/checkSession</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../am-oidc1/rest-api-oidc-endsession-endpoint.html">/oauth2/connect/endSession</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../am-oidc1/rest-api-oauth2-register-endpoint.html">/oauth2/register</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../am-oidc1/rest-api-oidc-discovery-webfinger.html">/.well-known/webfinger</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../am-oidc1/rest-api-oidc-discovery-configuration.html">/oauth2/.well-known/openid-configuration</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../am-oidc1/managing-jwk_uri.html">/oauth2/connect/jwk_uri</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../am-oidc1/managing-rp-jwk_uri.html">/oauth2/connect/rp/jwk_uri</a>
        
  </li>
</ul>
  </li>
</ul>
  </li>
  <li class="nav-item" data-depth="1">
        <span class="nav-item-toggle">
    <a class="nav-link" href="../am-saml2/preface.html">SAML 2.0</a>
        </span>
<ul class="nav-list">
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="../am-saml2/saml2-introduction.html">Introduction to SAML 2.0</a>
        
  </li>
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="../am-saml2/saml2-configuration.html">Deployment considerations</a>
        
  </li>
  <li class="nav-item" data-depth="2">
        <span class="nav-item-toggle">
    <a class="nav-link" href="../am-saml2/saml2-providers-and-cots.html">Set up IdPs, SPs, and CoTs</a>
        </span>
<ul class="nav-list">
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../am-saml2/configure-providers.html">Configure IdPs and SPs with journeys</a>
        
  </li>
</ul>
  </li>
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="../am-saml2/saml2-encryption.html">Sign and encrypt messages</a>
        
  </li>
  <li class="nav-item" data-depth="2">
        <span class="nav-item-toggle">
    <a class="nav-link" href="../am-saml2/saml2-sso-slo.html">Implement SSO and SLO</a>
        </span>
<ul class="nav-list">
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../am-saml2/saml2-integrated-mode.html">SSO in integrated mode</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../am-saml2/saml2-standalone-mode.html">SSO and SLO in standalone mode</a>
        
  </li>
</ul>
  </li>
  <li class="nav-item" data-depth="2">
        <span class="nav-item-toggle">
    <a class="nav-link" href="../am-saml2/saml2-linking-accounts.html">Federate identities</a>
        </span>
<ul class="nav-list">
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../am-saml2/choose-persistent-or-transient-federation.html">Choose persistent or transient federation</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../am-saml2/enable-persistent-federation.html">Enable persistent federation</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../am-saml2/enable-transient-federation.html">Enable transient federation</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../am-saml2/auto-federation.html">Link identities automatically with auto-federation</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../am-saml2/linking-auth-tree.html">Link identities for authentication</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../am-saml2/auto-federate-using-anonymous.html">Link identities to a single, shared account</a>
        
  </li>
</ul>
  </li>
  <li class="nav-item" data-depth="2">
        <span class="nav-item-toggle">
    <a class="nav-link" href="../am-saml2/customize-saml2-plugins.html">Customize SAML 2.0</a>
        </span>
<ul class="nav-list">
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../am-saml2/custom-idp-attribute-mapper.html">IdP attribute mapper</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../am-saml2/custom-idp-adapter.html">IdP adapter</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../am-saml2/custom-sp-account-mapper.html">SP account mapper</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../am-saml2/custom-sp-adapter.html">SP adapter</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../am-saml2/custom-nameid-mapper.html">NameID mapper</a>
        
  </li>
</ul>
  </li>
  <li class="nav-item" data-depth="2">
        <span class="nav-item-toggle">
    <a class="nav-link" href="../am-saml2/saml2-reference.html">Configuration reference</a>
        </span>
<ul class="nav-list">
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../am-saml2/saml2-error-codes.html">SAML error codes</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../am-saml2/saml2-hosted-idp-configuration.html">Hosted IdP</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../am-saml2/saml2-remote-idp-configuration.html">Remote IdP</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../am-saml2/saml2-hosted-sp-configuration.html">Hosted SP</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../am-saml2/saml2-remote-sp-configuration.html">Remote SP</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../am-saml2/saml2-cot-configuration.html">CoT</a>
        
  </li>
</ul>
  </li>
</ul>
  </li>
  <li class="nav-item" data-depth="1">
        <span class="nav-item-toggle">
    <a class="nav-link" href="../am-rest/preface.html">REST API</a>
        </span>
<ul class="nav-list">
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="../am-rest/rest-api-versioning.html">REST API versions</a>
        
  </li>
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="../am-rest/rest-realms.html">Specify realms in URLs</a>
        
  </li>
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="../am-rest/rest-endpoints.html">REST API endpoints</a>
        
  </li>
</ul>
  </li>
  <li class="nav-item" data-depth="1">
        <span class="nav-item-toggle">
    <a class="nav-link" href="../am-scripting/preface.html">Script with JavaScript</a>
        </span>
<ul class="nav-list">
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="../am-scripting/scripting-env.html">Scripting environment</a>
        
  </li>
  <li class="nav-item" data-depth="2">
        <span class="nav-item-toggle">
    <a class="nav-link" href="../am-scripting/next-generation-scripts.html">Next-generation scripts</a>
        </span>
<ul class="nav-list">
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../am-scripting/library-scripts.html">Library scripts</a>
        
  </li>
</ul>
  </li>
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="../am-scripting/cache-manager.html">Cache script values</a>
        
  </li>
  <li class="nav-item" data-depth="2">
        <span class="nav-item-toggle">
    <a class="nav-link" href="../am-scripting/scripting-api.html">Scripting API</a>
        </span>
<ul class="nav-list">
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../am-scripting/script-bindings.html">Common bindings</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        <span class="nav-item-toggle">
    <a class="nav-link" href="../am-scripting/scripting-api-node.html">Scripted Decision node API</a>
        </span>
<ul class="nav-list">
  <li class="nav-item" data-depth="4">
        
    <a class="nav-link" href="../am-scripting/scripting-api-node-migrate.html">Migrate decision node scripts to next-generation scripts</a>
        
  </li>
</ul>
  </li>
  <li class="nav-item" data-depth="3">
        <span class="nav-item-toggle">
    <a class="nav-link" href="../am-scripting/policy-condition-scripting-api.html">Policy condition script API</a>
        </span>
<ul class="nav-list">
  <li class="nav-item" data-depth="4">
        
    <a class="nav-link" href="../am-scripting/policy-condition-migrate.html">Migrate policy condition scripts to next-generation scripts</a>
        
  </li>
</ul>
  </li>
  <li class="nav-item" data-depth="3">
        <span class="nav-item-toggle">
    <a class="nav-link" href="../am-scripting/oauth2-scripting-api.html">OAuth 2.0 / OIDC scripting API</a>
        </span>
<ul class="nav-list">
  <li class="nav-item" data-depth="4">
        
    <a class="nav-link" href="../am-scripting/access-token-modification-migrate.html">Migrate OAuth scripts to next-generation scripts</a>
        
  </li>
  <li class="nav-item" data-depth="4">
        
    <a class="nav-link" href="../am-scripting/access-token-modification-api.html">Access token modification scripting API</a>
        
  </li>
  <li class="nav-item" data-depth="4">
        
    <a class="nav-link" href="../am-scripting/authorize-endpoint-data-provider-api.html">Authorization endpoint data provider scripting API</a>
        
  </li>
  <li class="nav-item" data-depth="4">
        
    <a class="nav-link" href="../am-scripting/user-info-claims-api.html">OIDC claims scripting API</a>
        
  </li>
  <li class="nav-item" data-depth="4">
        
    <a class="nav-link" href="../am-scripting/may-act-api.html">May act scripting API</a>
        
  </li>
  <li class="nav-item" data-depth="4">
        
    <a class="nav-link" href="../am-scripting/scope-evaluation-api.html">Scope evaluation scripting API</a>
        
  </li>
  <li class="nav-item" data-depth="4">
        
    <a class="nav-link" href="../am-scripting/scope-validation-api.html">Scope validation scripting API</a>
        
  </li>
  <li class="nav-item" data-depth="4">
        
    <a class="nav-link" href="../am-scripting/dcr-api.html">Dynamic client registration scripting API</a>
        
  </li>
</ul>
  </li>
  <li class="nav-item" data-depth="3">
        <span class="nav-item-toggle">
    <a class="nav-link" href="../am-scripting/saml2-scripting-api.html">SAML 2.0 scripting API</a>
        </span>
<ul class="nav-list">
  <li class="nav-item" data-depth="4">
        
    <a class="nav-link" href="../am-scripting/saml2-idp-adapter-api.html">IdP adapter scripting API</a>
        
  </li>
  <li class="nav-item" data-depth="4">
        
    <a class="nav-link" href="../am-scripting/saml2-idp-attribute-mapper-api.html">IdP attribute mapper scripting API</a>
        
  </li>
  <li class="nav-item" data-depth="4">
        
    <a class="nav-link" href="../am-scripting/saml2-nameid-mapper-api.html">NameID mapper scripting API</a>
        
  </li>
  <li class="nav-item" data-depth="4">
        
    <a class="nav-link" href="../am-scripting/saml2-sp-account-mapper-api.html">SP account mapper scripting API</a>
        
  </li>
  <li class="nav-item" data-depth="4">
        
    <a class="nav-link" href="../am-scripting/saml2-sp-adapter-api.html">SP adapter scripting API</a>
        
  </li>
</ul>
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../am-scripting/social-idp-profile-transformation-api.html">Social IdP scripting API</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../am-scripting/p1verify-completion-decision-api.html">PingOne Verify Completion Decision node API</a>
        
  </li>
</ul>
  </li>
  <li class="nav-item" data-depth="2">
        <span class="nav-item-toggle">
    <a class="nav-link" href="../am-scripting/manage-scripts-rest.html">Manage scripts over REST</a>
        </span>
<ul class="nav-list">
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../am-scripting/rest-api-scripts-query.html">Query scripts</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../am-scripting/rest-api-scripts-read.html">Read a script</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../am-scripting/rest-api-scripts-validate.html">Validate a script</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../am-scripting/rest-api-scripts-create.html">Create a script</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../am-scripting/rest-api-scripts-update.html">Update a script</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../am-scripting/rest-api-scripts-delete.html">Delete a script</a>
        
  </li>
</ul>
  </li>
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="../am-scripting/sample-scripts.html">Sample scripts</a>
        
  </li>
</ul>
  </li>
  <li class="nav-item" data-depth="1">
        <span class="nav-item-toggle">
    <a class="nav-link" href="../am-reference/preface.html">Reference</a>
        </span>
<ul class="nav-list">
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="../am-reference/services-configuration.html">Configure services</a>
        
  </li>
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="../am-reference/secret-id-mappings.html">Secret labels for signing and encryption</a>
        
  </li>
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="../am-reference/prometheus-metrics.html">AM Prometheus metrics</a>
        
  </li>
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="../am-reference/glossary.html">Glossary</a>
        
  </li>
</ul>
  </li>
</ul>
  </li>
  <li class="nav-item" data-depth="0">
    <h5 class="nav-title">Identity Management</h5>
<ul class="nav-list">
  <li class="nav-item" data-depth="1">
        <span class="nav-item-toggle">
    <a class="nav-link" href="../idm-objects/preface.html">Object modeling</a>
        </span>
<ul class="nav-list">
  <li class="nav-item" data-depth="2">
        <span class="nav-item-toggle">
    <a class="nav-link" href="../idm-objects/managed-objects.html">Managed objects</a>
        </span>
<ul class="nav-list">
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../idm-objects/creating-modifying-managed-objects.html">Create and modify managed object types</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../idm-objects/managed-object-virtual-properties.html">Virtual properties</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../idm-objects/managed-objects-scripts.html">Extend functionality through scripts</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../idm-objects/object-meta-data.html">Enable self-service by tracking user metadata</a>
        
  </li>
</ul>
  </li>
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="../idm-objects/users.html">Manage identities</a>
        
  </li>
  <li class="nav-item" data-depth="2">
        <span class="nav-item-toggle">
    <a class="nav-link" href="../idm-objects/relationships.html">Relationships between objects</a>
        </span>
<ul class="nav-list">
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../idm-objects/relationships-between-objects.html">Create a relationship between two objects</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../idm-objects/relationships-custom.html">Manage custom relationship properties</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../idm-objects/relationships-notification.html">Configure relationship change notification</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../idm-objects/relationships-validation.html">Validate relationships between objects</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../idm-objects/object-relationship-update-differences.html">Relationship update methods and their effects</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../idm-objects/reverse-relationships.html">Query relationships bidirectionally</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../idm-objects/conditional-relationships.html">Grant relationships conditionally</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../idm-objects/view-relationships-over-rest.html">View relationships over REST</a>
        
  </li>
</ul>
  </li>
  <li class="nav-item" data-depth="2">
        <span class="nav-item-toggle">
    <a class="nav-link" href="../idm-objects/roles.html">Roles</a>
        </span>
<ul class="nav-list">
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../idm-objects/managed-roles.html">Managed roles</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../idm-objects/roles-over-rest.html">Manipulate roles</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../idm-objects/roles-temporal-constraints.html">Use temporal constraints to restrict effective roles</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../idm-objects/working-with-role-assignments.html">Use assignments to provision users</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../idm-objects/effective-roles-and-assignments.html">Effective roles and effective assignments</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../idm-objects/roles-change-notification.html">Roles and relationship change notification</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../idm-objects/groups-and-access-to-idm.html">Map external groups to internal authz roles</a>
        
  </li>
</ul>
  </li>
  <li class="nav-item" data-depth="2">
        <span class="nav-item-toggle">
    <a class="nav-link" href="../idm-objects/groups.html">Groups</a>
        </span>
<ul class="nav-list">
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../idm-objects/manage-groups.html">Manage groups</a>
        
  </li>
</ul>
  </li>
  <li class="nav-item" data-depth="2">
        <span class="nav-item-toggle">
    <a class="nav-link" href="../idm-objects/organizations.html">Organizations</a>
        </span>
<ul class="nav-list">
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../idm-objects/manage-orgs-rest.html">Manage organizations over REST</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../idm-objects/orgs-in-high-latency-environments.html">Grow organizations downward if possible</a>
        
  </li>
</ul>
  </li>
  <li class="nav-item" data-depth="2">
        <span class="nav-item-toggle">
    <a class="nav-link" href="../idm-objects/policies.html">Use policies to validate data</a>
        </span>
<ul class="nav-list">
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../idm-objects/configuring-default-policy.html">Apply policies to managed objects</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../idm-objects/policies-over-REST.html">Manage policies over REST</a>
        
  </li>
</ul>
  </li>
  <li class="nav-item" data-depth="2">
        <span class="nav-item-toggle">
    <a class="nav-link" href="../idm-objects/access-data-objects-preface.html">Access data objects</a>
        </span>
<ul class="nav-list">
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../idm-objects/data-scripts.html">Access data objects using scripts</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        <span class="nav-item-toggle">
    <a class="nav-link" href="../idm-objects/data-rest.html">Access data objects using the REST API</a>
        </span>
<ul class="nav-list">
  <li class="nav-item" data-depth="4">
        
    <a class="nav-link" href="../idm-objects/queries.html">Define and call data queries</a>
        
  </li>
</ul>
  </li>
  <li class="nav-item" data-depth="3">
        <span class="nav-item-toggle">
    <a class="nav-link" href="../idm-objects/remote-proxy.html">Use a remote proxy to access data objects</a>
        </span>
<ul class="nav-list">
  <li class="nav-item" data-depth="4">
        
    <a class="nav-link" href="../idm-objects/remote-proxy-setup.html">Setup</a>
        
  </li>
  <li class="nav-item" data-depth="4">
        
    <a class="nav-link" href="../idm-objects/remote-proxy-advanced-usage.html">Advanced usage</a>
        
  </li>
  <li class="nav-item" data-depth="4">
        
    <a class="nav-link" href="../idm-objects/remote-proxy-create-sync-mappings.html">Create sync mappings</a>
        
  </li>
  <li class="nav-item" data-depth="4">
        
    <a class="nav-link" href="../idm-objects/remote-proxy-authentication-methods.html">Authentication methods</a>
        
  </li>
  <li class="nav-item" data-depth="4">
        
    <a class="nav-link" href="../idm-objects/remote-proxy-scripting-examples.html">Scripting examples</a>
        
  </li>
  <li class="nav-item" data-depth="4">
        
    <a class="nav-link" href="../idm-objects/remote-proxy-troubleshooting.html">Troubleshooting</a>
        
  </li>
  <li class="nav-item" data-depth="4">
        
    <a class="nav-link" href="../idm-objects/remote-proxy-security-best-practices.html">Security best practices</a>
        
  </li>
</ul>
  </li>
</ul>
  </li>
  <li class="nav-item" data-depth="2">
        <span class="nav-item-toggle">
    <a class="nav-link" href="../idm-objects/appendix-objects.html">Data models and objects reference</a>
        </span>
<ul class="nav-list">
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../idm-objects/appendix-managed-objects.html">Managed objects</a>
        
  </li>
</ul>
  </li>
</ul>
  </li>
  <li class="nav-item" data-depth="1">
        <span class="nav-item-toggle">
    <a class="nav-link" href="../idm-auth/preface.html">Authentication and authorization</a>
        </span>
<ul class="nav-list">
  <li class="nav-item" data-depth="2">
        <span class="nav-item-toggle">
    <a class="nav-link" href="../idm-auth/authentication.html">Authentication</a>
        </span>
<ul class="nav-list">
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../idm-auth/authentication-and-roles.html">Authentication and roles</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../idm-auth/rsfilter-module.html">Authentication through OAuth 2.0 and subject mappings</a>
        
  </li>
</ul>
  </li>
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="../idm-auth/authorization-and-roles.html">Authorization and roles</a>
        
  </li>
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="../idm-auth/delegated-admin.html">Delegated administration</a>
        
  </li>
</ul>
  </li>
  <li class="nav-item" data-depth="1">
        <span class="nav-item-toggle">
    <a class="nav-link" href="../idm-synchronization/preface.html">Synchronization</a>
        </span>
<ul class="nav-list">
  <li class="nav-item" data-depth="2">
        <span class="nav-item-toggle">
    <a class="nav-link" href="../idm-synchronization/sync-overview.html">Synchronization overview</a>
        </span>
<ul class="nav-list">
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../idm-synchronization/sync-types.html">Types of synchronization</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../idm-synchronization/sync-config.html">Configure synchronization at a high level</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../idm-synchronization/sync-data-model.html">Data mapping model</a>
        
  </li>
</ul>
  </li>
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="../idm-synchronization/sync-connections.html">Configure a connection between resources</a>
        
  </li>
  <li class="nav-item" data-depth="2">
        <span class="nav-item-toggle">
    <a class="nav-link" href="../idm-synchronization/mappings.html">Map attributes between resources</a>
        </span>
<ul class="nav-list">
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../idm-synchronization/cfg-mapping-resource.html">Configure mapping</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../idm-synchronization/remove-sync-mapping.html">Remove mapping</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../idm-synchronization/mapping-transforming-attributes.html">Transform attributes</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../idm-synchronization/mapping-default-attributes.html">Default attribute values</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../idm-synchronization/mapping-conditions.html">Create conditions on attributes</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../idm-synchronization/linking-multiple-targets.html">Map a single object to multiple objects</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../idm-synchronization/prevent-accidental-deletion.html">Prevent accidental target deletion</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../idm-synchronization/scripts-in-mappings.html">Manage objects during sync using script hooks</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../idm-synchronization/reusing-links.html">Reuse links between mappings</a>
        
  </li>
</ul>
  </li>
  <li class="nav-item" data-depth="2">
        <span class="nav-item-toggle">
    <a class="nav-link" href="../idm-synchronization/chap-situations-actions.html">Synchronization situations and actions</a>
        </span>
<ul class="nav-list">
  <li class="nav-item" data-depth="3">
        <span class="nav-item-toggle">
    <a class="nav-link" href="../idm-synchronization/sync-situations.html">How situations are assessed</a>
        </span>
<ul class="nav-list">
  <li class="nav-item" data-depth="4">
        
    <a class="nav-link" href="../idm-synchronization/source-reconciliation.html">Source reconciliation situations</a>
        
  </li>
  <li class="nav-item" data-depth="4">
        
    <a class="nav-link" href="../idm-synchronization/target-reconciliation.html">Target reconciliation situations</a>
        
  </li>
  <li class="nav-item" data-depth="4">
        
    <a class="nav-link" href="../idm-synchronization/autosync-and-livesync.html">Implicit and liveSync situations</a>
        
  </li>
</ul>
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../idm-synchronization/sync-actions.html">Take an action from an assigned situation</a>
        
  </li>
</ul>
  </li>
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="../idm-synchronization/chap-correlation.html">Correlate source &amp; target objects</a>
        
  </li>
  <li class="nav-item" data-depth="2">
        <span class="nav-item-toggle">
    <a class="nav-link" href="../idm-synchronization/chap-sync-operations.html">Synchronization operations</a>
        </span>
<ul class="nav-list">
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../idm-synchronization/manage-recon.html">Manage reconciliation</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../idm-synchronization/manage-livesync.html">Manage liveSync</a>
        
  </li>
</ul>
  </li>
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="../idm-synchronization/chap-restricting-sync.html">Filter sync data</a>
        
  </li>
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="../idm-synchronization/chap-implicit-live-sync.html">Enhance implicit sync and liveSync</a>
        
  </li>
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="../idm-synchronization/chap-schedules.html">Schedule synchronization</a>
        
  </li>
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="../idm-synchronization/clustered-recon.html">Clustered reconciliation</a>
        
  </li>
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="../idm-synchronization/import-data.html">Import bulk data</a>
        
  </li>
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="../idm-synchronization/chap-performance.html">Tune reconciliation performance</a>
        
  </li>
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="../idm-synchronization/synchronization-ref.html">Synchronization reference</a>
        
  </li>
</ul>
  </li>
  <li class="nav-item" data-depth="1">
        <span class="nav-item-toggle">
    <a class="nav-link" href="../idm-scripting/preface.html">Scripting in JavaScript</a>
        </span>
<ul class="nav-list">
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="../idm-scripting/script-call.html">Call a script from the IDM configuration</a>
        
  </li>
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="../idm-scripting/script-endpoint.html">Validate scripts over REST</a>
        
  </li>
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="../idm-scripting/script-custom-endpoints.html">Create custom endpoints to launch scripts</a>
        
  </li>
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="../idm-scripting/custom-scripted-actions.html">Register custom scripted actions</a>
        
  </li>
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="../idm-scripting/request-context.html">Request context chain</a>
        
  </li>
  <li class="nav-item" data-depth="2">
        <span class="nav-item-toggle">
    <a class="nav-link" href="../idm-scripting/script-triggers.html">Script triggers</a>
        </span>
<ul class="nav-list">
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../idm-scripting/script-triggers-managedConfig.html">In managed objects</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../idm-scripting/script-triggers-mappings.html">In mappings</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../idm-scripting/script-triggers-routerConfig.html">In the router configuration</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../idm-scripting/script-variables-augment-security.html">Populate the security context of an authenticated user using a script</a>
        
  </li>
</ul>
  </li>
  <li class="nav-item" data-depth="2">
        <span class="nav-item-toggle">
    <a class="nav-link" href="../idm-scripting/script-vars.html">Variables available in scripts</a>
        </span>
<ul class="nav-list">
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../idm-scripting/script-variables-custom-endpoints.html">Custom endpoint script variables</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../idm-scripting/script-variables-identity-server.html">Retrieve property information from config files</a>
        
  </li>
</ul>
  </li>
  <li class="nav-item" data-depth="2">
        <span class="nav-item-toggle">
    <a class="nav-link" href="../idm-scripting/router-config.html">Manage the uniform interface to objects with the router service</a>
        </span>
<ul class="nav-list">
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../idm-scripting/filter-objects.html">Filter objects</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../idm-scripting/script-pattern-match.html">Improve performance with pattern matching</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../idm-scripting/script-sequence.html">Script execution sequence</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../idm-scripting/filter-script-scope.html">Script scope</a>
        
  </li>
</ul>
  </li>
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="../idm-scripting/scripting-func-engine.html">Functions available for use in identity scripts</a>
        
  </li>
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="../idm-scripting/scripting-func-logs.html">Logging in identity-related scripts</a>
        
  </li>
</ul>
  </li>
  <li class="nav-item" data-depth="1">
        <span class="nav-item-toggle">
    <a class="nav-link" href="../idm-schedules/preface.html">Schedule tasks on objects</a>
        </span>
<ul class="nav-list">
  <li class="nav-item" data-depth="2">
        <span class="nav-item-toggle">
    <a class="nav-link" href="../idm-schedules/schedules.html">Schedule reconciliation and synchronization</a>
        </span>
<ul class="nav-list">
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../idm-schedules/scheduler-configuration-file.html">Configure the scheduler service</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        <span class="nav-item-toggle">
    <a class="nav-link" href="../idm-schedules/configure-schedules.html">Configure schedules</a>
        </span>
<ul class="nav-list">
  <li class="nav-item" data-depth="4">
        
    <a class="nav-link" href="../idm-schedules/configure-static-schedules.html">Configure schedules in static configuration</a>
        
  </li>
  <li class="nav-item" data-depth="4">
        
    <a class="nav-link" href="../idm-schedules/configure-dynamic-schedules.html">Configure schedules in dynamic configuration</a>
        
  </li>
</ul>
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../idm-schedules/schedules-dst.html">Manage daylight saving time with schedules</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../idm-schedules/persistent-schedules.html">Run schedules missed while a server was offline</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../idm-schedules/scheduler-examples.html">Schedule examples</a>
        
  </li>
</ul>
  </li>
  <li class="nav-item" data-depth="2">
        <span class="nav-item-toggle">
    <a class="nav-link" href="../idm-schedules/task-scanner.html">Scan data to trigger tasks</a>
        </span>
<ul class="nav-list">
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../idm-schedules/task-scanner-rest.html">Manage scanning tasks using REST</a>
        
  </li>
</ul>
  </li>
</ul>
  </li>
  <li class="nav-item" data-depth="1">
        
    <a class="nav-link" href="../idm-security/secure-sensitive-data.html">Secure identity data</a>
        
  </li>
  <li class="nav-item" data-depth="1">
        
    <a class="nav-link" href="../connectors/connectors.html">Connectors</a>
        
  </li>
  <li class="nav-item" data-depth="1">
        
    <a class="nav-link" href="../external-services/external-rest.html">Make dynamic HTTP calls using the external REST service</a>
        
  </li>
  <li class="nav-item" data-depth="1">
        <span class="nav-item-toggle">
    <a class="nav-link" href="../idm-rest-api/preface.html">Identity and object-related REST APIs</a>
        </span>
<ul class="nav-list">
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="../idm-rest-api/rest-and-idm.html">REST &amp; IDM</a>
        
  </li>
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="../idm-rest-api/rest-api-versioning.html">REST API versioning</a>
        
  </li>
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="../idm-rest-api/rest-structure.html">REST API structure</a>
        
  </li>
  <li class="nav-item" data-depth="2">
    <span class="nav-text  nav-item-toggle">REST endpoints</span>
<ul class="nav-list">
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../idm-rest-api/endpoints/rest-bulk-import.html">Bulk import</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../idm-rest-api/endpoints/rest-email.html">Email</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../idm-rest-api/endpoints/rest-feature.html">Feature enablement</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../idm-rest-api/endpoints/rest-internal.html">Internal objects</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../idm-rest-api/endpoints/rest-managed-groups.html">Managed groups</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../idm-rest-api/endpoints/rest-managed-organizations.html">Managed organizations</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../idm-rest-api/endpoints/rest-managed-users.html">Managed users</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../idm-rest-api/endpoints/rest-privileges.html">Privileges</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../idm-rest-api/endpoints/rest-recon.html">Reconciliation operations</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../idm-rest-api/endpoints/rest-task-scanner.html">Scanning tasks</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../idm-rest-api/endpoints/rest-schedules.html">Schedules</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../idm-rest-api/endpoints/rest-schema.html">Schema</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../idm-rest-api/endpoints/rest-scripts.html">Scripts</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../idm-rest-api/endpoints/rest-server-config.html">Server configuration</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../idm-rest-api/endpoints/rest-info.html">Server state</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../idm-rest-api/endpoints/rest-sync.html">Synchronization service</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../idm-rest-api/endpoints/rest-system-objects.html">System objects</a>
        
  </li>
</ul>
  </li>
</ul>
  </li>
</ul>
  </li>
  <li class="nav-item" data-depth="0">
    <h5 class="nav-title">Developer Docs</h5>
<ul class="nav-list">
  <li class="nav-item" data-depth="1">
        <span class="nav-item-toggle">
    <a class="nav-link" href="../developer-docs/scripting.html">Scripting</a>
        </span>
<ul class="nav-list">
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="../developer-docs/scripting-auth.html">Extend Advanced Identity Cloud with scripting</a>
        
  </li>
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="../developer-docs/scripting-custom-endpoints.html">Extend behavior with custom endpoints</a>
        
  </li>
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="../developer-docs/scripting-event-hooks.html">Trigger scripts during events on identity objects</a>
        
  </li>
</ul>
  </li>
  <li class="nav-item" data-depth="1">
        <span class="nav-item-toggle">
    <a class="nav-link" href="../developer-docs/authenticate-to-rest-api-overview.html">REST API</a>
        </span>
<ul class="nav-list">
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="../developer-docs/authenticate-to-rest-api-with-api-key-and-secret.html">Access monitoring and logging endpoints with an API key and secret</a>
        
  </li>
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="../developer-docs/authenticate-to-rest-api-with-access-token.html">Access endpoints with an access token</a>
        
  </li>
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="../developer-docs/postman-collection.html">Postman collection</a>
        
  </li>
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="../developer-docs/api-reference.html">API reference</a>
        
  </li>
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="../developer-docs/api-custom-headers.html">API custom headers</a>
        
  </li>
  <li class="nav-item" data-depth="2">
        <span class="nav-item-toggle">
    <a class="nav-link" href="../developer-docs/crest/about-crest.html">Advanced Identity Cloud REST</a>
        </span>
<ul class="nav-list">
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../developer-docs/crest/create.html">Create</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../developer-docs/crest/read.html">Read</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../developer-docs/crest/update.html">Update</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../developer-docs/crest/delete.html">Delete</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../developer-docs/crest/patch.html">Patch</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../developer-docs/crest/action.html">Action</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../developer-docs/crest/query.html">Query</a>
        
  </li>
  <li class="nav-item" data-depth="3">
        
    <a class="nav-link" href="../developer-docs/crest/status-codes.html">HTTP status codes</a>
        
  </li>
</ul>
  </li>
</ul>
  </li>
</ul>
  </li>
  <li class="nav-item" data-depth="0">
    <h5 class="nav-title">Use Case Catalog</h5>
<ul class="nav-list">
  <li class="nav-item" data-depth="1">
        
    <a class="nav-link" href="../use-cases/preface-pages/about-use-case-catalog.html">About the use case catalog</a>
        
  </li>
  <li class="nav-item" data-depth="1">
        <span class="nav-item-toggle">
    <a class="nav-link" href="../use-cases/preface-pages/administration.html">Administration</a>
        </span>
<ul class="nav-list">
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="../use-cases/use-case-add-tenant-admins.html">Set up administrators</a>
        
  </li>
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="../use-cases/use-case-audit-logging.html">Read audit logs using REST</a>
        
  </li>
</ul>
  </li>
  <li class="nav-item" data-depth="1">
        <span class="nav-item-toggle">
    <a class="nav-link" href="../use-cases/preface-pages/authentication.html">Authentication</a>
        </span>
<ul class="nav-list">
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="../use-cases/use-case-mfa-with-push.html">Sign on with MFA using push notifications</a>
        
  </li>
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="../use-cases/use-case-lost-second-factor.html">Replace lost second-factor authentication devices</a>
        
  </li>
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="../use-cases/use-case-sso-saml-salesforce-sp.html">Salesforce as SP (SAML)</a>
        
  </li>
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="../use-cases/use-case-sso-oidc-entra-id.html">Microsoft Entra ID (Azure AD) as OpenID provider</a>
        
  </li>
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="../use-cases/use-case-sso-oidc-sp-okta.html">Okta as RP (OIDC)</a>
        
  </li>
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="../use-cases/use-case-pass-through-auth.html">Pass-through auth (PTA) with Microsoft Entra ID (Azure AD)</a>
        
  </li>
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="../use-cases/use-case-external-entra.html">Advanced Identity Cloud as an External Authentication Method for Microsoft Entra ID (Azure AD)</a>
        
  </li>
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="../use-cases/use-case-temenos.html">Advanced Identity Cloud as a Temenos identity provider</a>
        
  </li>
</ul>
  </li>
  <li class="nav-item" data-depth="1">
        <span class="nav-item-toggle">
    <a class="nav-link" href="../use-cases/preface-pages/authorization.html">Authorization</a>
        </span>
<ul class="nav-list">
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="../use-cases/use-case-app-authz-journeys.html">Authorize application access in journeys</a>
        
  </li>
</ul>
  </li>
  <li class="nav-item" data-depth="1">
        <span class="nav-item-toggle">
    <a class="nav-link" href="../use-cases/preface-pages/customization.html">Customization</a>
        </span>
<ul class="nav-list">
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="../use-cases/use-case-customize-theme.html">Customize a theme for hosted pages</a>
        
  </li>
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="../use-cases/use-case-email-template.html">Customize emails</a>
        
  </li>
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="../use-cases/use-case-last-login-time.html">Create a script in a journey to record last login time</a>
        
  </li>
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="../use-cases/use-case-access-token-for-journeys.html">Get an access token in a journey</a>
        
  </li>
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="../use-cases/use-case-journey-session-properties-oidc.html">Expose journey session properties in the OIDC ID token</a>
        
  </li>
</ul>
  </li>
  <li class="nav-item" data-depth="1">
        <span class="nav-item-toggle">
    <a class="nav-link" href="../use-cases/preface-pages/data-identity-management.html">Data (identity) management</a>
        </span>
<ul class="nav-list">
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="../use-cases/use-case-test-users-and-roles.html">Create test users and roles</a>
        
  </li>
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="../use-cases/use-case-dynamic-role.html">Assign roles to users dynamically</a>
        
  </li>
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="../use-cases/use-case-create-orgs.html">Delegate administration with organizations</a>
        
  </li>
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="../use-cases/use-case-manage-reports.html">Enable managers to manage their direct reports</a>
        
  </li>
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="../use-cases/use-case-idc-with-ping-directory.html">Provision users to and from Advanced Identity Cloud and PingDirectory</a>
        
  </li>
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="../use-cases/use-case-provision-from-entra-id.html">Provision users from Microsoft Entra</a>
        
  </li>
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="../use-cases/use-case-provision-rcs-ad.html">Provision data from Active Directory (AD) using RCS</a>
        
  </li>
</ul>
  </li>
  <li class="nav-item" data-depth="1">
        <span class="nav-item-toggle">
    <a class="nav-link" href="../use-cases/preface-pages/self-service.html">Self-service</a>
        </span>
<ul class="nav-list">
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="../use-cases/use-case-user-registration.html">User registration</a>
        
  </li>
</ul>
  </li>
  <li class="nav-item" data-depth="1">
        
    <a class="nav-link" href="../use-cases/preface-pages/third-party-integrations.html">Third-party integrations</a>
        
  </li>
</ul>
  </li>
  <li class="nav-item" data-depth="0">
    <h5 class="nav-title">Product Information</h5>
<ul class="nav-list">
  <li class="nav-item" data-depth="1">
        
    <a class="nav-link" href="../product-information/global-identity-cloud-locations.html">Global data regions</a>
        
  </li>
  <li class="nav-item" data-depth="1">
        
    <a class="nav-link" href="../product-information/supported-browsers.html">Supported browsers</a>
        
  </li>
  <li class="nav-item" data-depth="1">
        
    <a class="nav-link" href="../product-information/security-compliance.html">Security and compliance</a>
        
  </li>
  <li class="nav-item" data-depth="1">
        
    <a class="nav-link" href="../product-information/penetration-and-load-testing-policy.html">Penetration testing &amp; load testing policy</a>
        
  </li>
  <li class="nav-item" data-depth="1">
        
    <a class="nav-link" href="../product-information/release-lifecycle.html">Product lifecycle &amp; releases</a>
        
  </li>
  <li class="nav-item" data-depth="1">
        <span class="nav-item-toggle">
    <a class="nav-link" href="../product-information/migration-dependent-features.html">Migration dependent features</a>
        </span>
<ul class="nav-list">
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="../product-information/migration-dependent-features/application-management-migration-faq.html">Application management migration FAQ</a>
        
  </li>
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="../product-information/migration-dependent-features/deferred-release-migration-faq.html">Deferred release migration FAQ</a>
        
  </li>
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="../product-information/migration-dependent-features/deprecated-identity-management-native-console-faq.html">Deprecated identity management native console FAQ</a>
        
  </li>
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="../product-information/migration-dependent-features/event-hooks-migration-faq.html">Event hooks migration FAQ</a>
        
  </li>
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="../product-information/migration-dependent-features/group-identity-migration-faq.html">Group identity migration FAQ</a>
        
  </li>
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="../product-information/migration-dependent-features/rcs-configuration-migration-faq.html">RCS configuration migration FAQ</a>
        
  </li>
  <li class="nav-item" data-depth="2">
        
    <a class="nav-link" href="../product-information/migration-dependent-features/tenant-administrator-mandatory-2-step-verification-faq.html">Tenant administrator mandatory 2-step verification FAQ</a>
        
  </li>
</ul>
  </li>
  <li class="nav-item" data-depth="1">
        
    <a class="nav-link" href="../product-information/add-on-capabilities.html">Add-on capabilities</a>
        
  </li>
  <li class="nav-item" data-depth="1">
        
    <a class="nav-link" href="../product-information/deprecation-notices.html">Deprecation notices</a>
        
  </li>
</ul>
  </li>
</ul>
  </nav>
</div>
      <div class="nav-panel-explore" data-panel="explore">
  <div class="context">
    <span class="title">PingOne Advanced Identity Cloud</span>
    <span class="version"></span>
  </div>
  <ul class="components">
        <li class="component is-current">
          <div class="title"><a href="../home.html">PingOne Advanced Identity Cloud</a></div>
        </li>
  </ul>
</div>
    </div>
  </aside>
</div>
  <div class="right-content">
    <main class="article">
  <div class="content">
<article class="doc">
<div class="toolbar" role="navigation">
    <a href="../home.html" class="home-link"></a>
    <nav class="breadcrumbs" aria-label="breadcrumbs">
  <ul>
    <li><a href="../home.html">PingOne Advanced Identity Cloud</a></li>
    <li><a href="social-authentication.html">Social authentication</a></li>
    <li><a href="social-authentication-configure.html">Configure social authentication</a></li>
    <li><a href="social-authentication-settings.html">Social identity provider settings</a></li>
  </ul>
</nav>
</div>
<div id="fr-expand-content" hidden>
  <a class="fr-link-collapse collapsed fr-expand-link"
     data-toggle="tooltip"
     title="Expand/collapse hidden content"
     href="#">Expand/Collapse All</a>
</div>
<h1 class="page">Social identity provider settings</h1>
<div id="preamble">
<div class="sectionbody">
<div class="paragraph">
<p>This page provides a reference for the settings available when you <a href="social-authentication-configure.html" class="xref page">configure a social identity provider</a> in Advanced Identity Cloud.
These settings control how Advanced Identity Cloud interacts with the external provider.</p>
</div>
<div class="paragraph">
<p>The settings available depend on the type of provider you are configuring (OIDC or OAuth 2.0) and the authentication methods you choose, but they generally include endpoint URLs, client authentication methods, and security options.</p>
</div>
</div>
</div>
<div class="sect1">
<h2 id="status-and-button-preview"><a class="anchor" href="#status-and-button-preview"></a>Status and button settings</h2>
<div class="sectionbody">
<div class="dlist">
<dl>
<dt class="hdlist1">Active / Inactive</dt>
<dd>
<p>Whether the provider is enabled.</p>
<div class="paragraph">
<p>Required: Yes.</p>
</div>
</dd>
<dt class="hdlist1">Button preview</dt>
<dd>
<p>Click <span class="label">Edit</span> to open the <span class="label">Edit UI Configuration</span> modal, where you specify a map of properties that determine how the social identity provider button displays in the hosted journey pages.</p>
<details>
<summary class="title">Common properties affecting how a button displays in hosted pages</summary>
<div class="content">
<div class="ulist">
<ul>
<li>
<p><code>buttonClass</code>: Adds the specified class to the identity provider button,
for any additional styling you want to apply.</p>
</li>
<li>
<p><code>buttonCustomStyle</code>: Any custom CSS you wish to apply to the button outside of normal End User UI styling.</p>
</li>
<li>
<p><code>buttonCustomStyleHover</code>: Adds custom styling when the cursor is hovering over the button.</p>
</li>
<li>
<p><code>buttonDisplayName</code>: The name of the identity provider,
which will be included either on the button or in the button&#8217;s <code>alt</code> attribute, depending on styling.</p>
</li>
<li>
<p><code>buttonImage</code>: A relative path to an image in the End User UI.</p>
</li>
</ul>
</div>
</div>
</details>
<div class="paragraph">
<p>Required: Yes</p>
</div>
</dd>
</dl>
</div>
</div>
</div>
<div class="sect1">
<h2 id="general_settings"><a class="anchor" href="#general_settings"></a>General settings</h2>
<div class="sectionbody">
<div class="dlist">
<dl>
<dt class="hdlist1">Client ID</dt>
<dd>
<p>The <code>client_id</code> parameter as described in <a href="https://www.rfc-editor.org/rfc/rfc6749.html#section-2.2">section 2.2</a>
of <em class="ref">The OAuth 2.0 Authorization Framework</em> specification.</p>
<div class="paragraph">
<p>Required: Yes.</p>
</div>
</dd>
<dt class="hdlist1">Client Secret</dt>
<dd>
<p>The <code>client_secret</code> parameter as described in <a href="https://www.rfc-editor.org/rfc/rfc6749.html#section-2.3">section 2.3</a>
of <em class="ref">The OAuth 2.0 Authorization Framework</em> specification.</p>
<div class="admonitionblock important">
<table>
<tr>
<td class="icon">
<i class="fa icon-important" title="Important"></i>
</td>
<td class="content">
<div class="paragraph">
<p>This property is deprecated.
Select <span class="label">Use Secret Store for secrets</span> and use the <span class="label">Secret Label Identifier</span> instead to store the secret securely.</p>
</div>
<div class="paragraph">
<p>If you set a <span class="label">Secret Label Identifier</span> and Advanced Identity Cloud finds a matching secret in a secret store, the <span class="label">Client Secret</span> is ignored.</p>
</div>
</td>
</tr>
</table>
</div>
<div class="paragraph">
<p>Required: No.</p>
</div>
</dd>
<dt class="hdlist1">Use Secret Store for secrets</dt>
<dd>
<p>When selected, the <span class="label">Secret Label Identifier</span> field is displayed, allowing you to create a secret label for mapping to a secret in a secret store.
This is the recommended way to manage client secrets.</p>
</dd>
<dt class="hdlist1">Secret Label Identifier</dt>
<dd>
<p>An identifier used to create a <em>secret label</em> for mapping to a secret in a secret store.
This field is displayed only when you select <span class="label">Use Secret Store for secrets</span>.</p>
<div class="paragraph">
<p>Advanced Identity Cloud uses this identifier to create a specific secret label for this service instance,
using the template <code>am.social.providers.<span class="var">identifier</span>.secret</code> where <span class="var">identifier</span> is the value of
<span class="label">Secret Label Identifier</span>.</p>
</div>
<div class="paragraph">
<p>The identifier can only contain alphanumeric characters <code>a-z</code>, <code>A-Z</code>, <code>0-9</code>,
and periods (<code>.</code>). It can&#8217;t start or end with a period.</p>
</div>
<div class="paragraph">
<p>If you set a <span class="label">Secret Label Identifier</span> and Advanced Identity Cloud finds a matching secret in a secret store, the <span class="label">Client Secret</span> is ignored.</p>
</div>
<div class="paragraph">
<p>Required: No.</p>
</div>
</dd>
<dt class="hdlist1">OAuth Scopes</dt>
<dd>
<p>The list of scopes to request from the provider.</p>
<div class="paragraph">
<p>The scopes that the provider returns depends on the permissions that the resource owner,
such as the end user, grants to the client application.</p>
</div>
<div class="paragraph">
<p>For example, Google exposes its supported scopes in their
<a href="https://developers.google.com/identity/protocols/oauth2/scopes">OAuth 2.0 Scopes for Google APIs</a> documentation.</p>
</div>
<div class="paragraph">
<p>Required: Yes.</p>
</div>
</dd>
<dt class="hdlist1">Auth ID Key</dt>
<dd>
<p>The attribute the social identity provider uses to identify an authenticated individual.
For example, <code>id</code>, <code>sub</code>, and <code>user_id</code>.</p>
<div class="paragraph">
<p>Required: Yes.</p>
</div>
</dd>
<dt class="hdlist1">Authentication Endpoint URL</dt>
<dd>
<p>The URL to the social provider&#8217;s endpoint handling authentication as described in
<a href="https://www.rfc-editor.org/rfc/rfc6749.html#section-3.1">section 3.1</a> of <em class="ref">The OAuth 2.0 Authorization Framework</em>.
For example, <code>https://accounts.google.com/o/oauth2/v2/auth</code>.</p>
<div class="paragraph">
<p>Required: Yes.</p>
</div>
</dd>
<dt class="hdlist1">Access Token Endpoint URL</dt>
<dd>
<p>The URL to the endpoint handling access tokens as described in
<a href="https://www.rfc-editor.org/rfc/rfc6749.html#section-3.2">section 3.2</a>
of <em class="ref">The OAuth 2.0 Authorization Framework</em> specification.
For example, <code>https://www.googleapis.com/oauth2/v4/token</code>.</p>
<div class="paragraph">
<p>Required: Yes.</p>
</div>
</dd>
<dt class="hdlist1">User Profile Service URL</dt>
<dd>
<p>The user profile URL that returns profile information.
For example, <code>https://www.googleapis.com/oauth2/v3/userinfo</code>.</p>
<div class="paragraph">
<p>This URL should return JSON objects in its response.</p>
</div>
<div class="paragraph">
<p>Required: No.</p>
</div>
</dd>
<dt class="hdlist1">Token Introspection Endpoint URL</dt>
<dd>
<p>The URL to the endpoint handling access token validation, as described in the
<a href="https://www.rfc-editor.org/info/rfc7662"><em>OOAuth 2.0 Token Introspection</em></a> specification.
For example, <code>https://oauth2.googleapis.com/tokeninfo</code>.</p>
<div class="paragraph">
<p>Required: No.</p>
</div>
</dd>
<dt class="hdlist1">Redirect URL</dt>
<dd>
<p>The URL to which the identity provider will redirect the user after authenticating, as described in
<a href="https://www.rfc-editor.org/rfc/rfc6749.html#section-3.1.2">Section 3.1.2</a>
of <em class="ref">The OAuth 2.0 Authorization Framework</em> specification.</p>
<div class="paragraph">
<p>Set the redirect URL to the tenant’s access management base URL.
For example, <code>https://<span class="var">&lt;tenant-env-fqdn></span>/am</code>.
Follow the <a href="social-authentication-configure.html#social-authentication-configuration-redirect-url" class="xref page">redirect URL requirements</a> exactly.
The URL is also registered in the identity provider&#8217;s service.</p>
</div>
<div class="paragraph">
<p>If you&#8217;re using an app built with the Ping SDKs for Android or iOS, you can also use a custom URI scheme as the redirect. For example, <code>com.example.sdkapp:redirect_uri_path</code> or <code>auth://com.example.ios.sdkapp</code>.</p>
</div>
<div class="admonitionblock important">
<table>
<tr>
<td class="icon">
<i class="fa icon-important" title="Important"></i>
</td>
<td class="content">
<div class="ulist">
<ul>
<li>
<p>When using the <code>FORM_POST</code> response mode, you must specify the <code>form_post</code> endpoint in the redirection URL.
For example, <code>https://<span class="var">&lt;tenant-env-fqdn></span>/oauth2/client/form_post/<em class="var">social IdP client</em></code>.</p>
<div class="paragraph">
<p>Find more information in <a href="#response-mode">Response Mode</a>.</p>
</div>
</li>
<li>
<p>If you encounter domain validation prompts when using <code>forgeblocks.com</code> and <code>id.forgerock.io</code> domains
as redirect URLs in your Google OAuth 2.0 applications, you must <a href="../realms/custom-domains.html" class="xref page">use a custom domain</a>,
and then set up <a href="../realms/custom-domains.html#custom-domain-google" class="xref page">domain verification with Google</a>.</p>
</li>
<li>
<p>If you encounter <code>No provider found</code> errors when using <code>forgeblocks.com</code> and <code>id.forgerock.io</code>
domains as redirect URLs in your OAuth 2.0 applications, either modify the redirect URL to include a realm identifier,
or <a href="../realms/custom-domains.html" class="xref page">use a custom domain</a>:</p>
<div class="ulist">
<ul>
<li>
<p>Incorrect:</p>
<div class="listingblock">
<div class="content">
<pre>https://<span class="var"><em>&lt;tenant-env-fqdn&gt;</em></span>/am/oauth2/client/form_post/...</pre>
</div>
</div>
</li>
<li>
<p>Correct:</p>
<div class="listingblock">
<div class="content">
<pre>https://<span class="var"><em>&lt;tenant-env-fqdn&gt;</em></span>/am/oauth2/<span class="var">&lt;realm&gt;</span>/client/form_post/...</pre>
</div>
</div>
<div class="paragraph">
<p><em>or</em></p>
</div>
<div class="listingblock">
<div class="content">
<pre>https://<span class="var">&lt;custom-domain&gt;</span>/am/oauth2/client/form_post/...</pre>
</div>
</div>
<div class="paragraph">
<p>A custom domain acts as a realm DNS alias, so when it&#8217;s used as a redirect URL, you don&#8217;t have to specify the realm
because Advanced Identity Cloud implicitly knows which realm to use.</p>
</div>
</li>
</ul>
</div>
</li>
</ul>
</div>
</td>
</tr>
</table>
</div>
<div class="paragraph">
<p>Required: Yes.</p>
</div>
</dd>
<dt class="hdlist1">Redirect after form post URL</dt>
<dd>
<p>The URL of a custom login page or application.
Advanced Identity Cloud will send processed form post data related to social login authentication to that URL
as the value of the <code>form_post_entry</code> query parameter.</p>
<div class="paragraph">
<p>To continue the authentication journey,
the custom login page is responsible for making a call to the Advanced Identity Cloud <code>/json/authenticate</code> endpoint
with the authentication ID (<code>authID</code>) and the processed form data (<code>form_post_entry</code>).</p>
</div>
<div class="paragraph">
<p>Configure this property when the following is true:</p>
</div>
<div class="ulist">
<ul>
<li>
<p>The <code>FORM_POST</code> response mode is configured.</p>
</li>
<li>
<p>Your users log in to Advanced Identity Cloud using custom login pages,
such as apps using the Ping SDKs, instead of the Ping Identity-provided user interfaces.</p>
<div class="paragraph">
<p>Required: No.</p>
</div>
</li>
</ul>
</div>
</dd>
<dt class="hdlist1">Scope Delimiter</dt>
<dd>
<p>The delimiter used to separate scope values.
For example, a blank space (<kbd></kbd>), or a comma character (<kbd>,</kbd>).</p>
<div class="paragraph">
<p>Most providers use a blank space.</p>
</div>
<div class="paragraph">
<p>Required: Yes.</p>
</div>
<div class="admonitionblock note">
<table>
<tr>
<td class="icon">
<i class="fa icon-note" title="Note"></i>
</td>
<td class="content">
This field is not applicable to the Twitter social provider and is hidden from the configuration.
</td>
</tr>
</table>
</div>
</dd>
<dt class="hdlist1">Client Authentication Method</dt>
<dd>
<p>How the client should authenticate to the provider.
Possible values are:</p>
<div class="openblock">
<div class="content">
<div class="dlist">
<dl>
<dt class="hdlist1"><code>CLIENT_SECRET_POST</code></dt>
<dd>
<p>The client sends the client ID and the secret in the <code>client_ID</code> and the <code>client_secret</code> parameters
in the body of the request.</p>
</dd>
<dt class="hdlist1"><code>CLIENT_SECRET_BASIC</code></dt>
<dd>
<p>The client sends the client ID and the secret in a basic authorization header with the base64-encoded value of <em class="var">client-id:client-secret</em>.</p>
</dd>
<dt class="hdlist1"><code>PRIVATE_KEY_JWT</code></dt>
<dd>
<p>The client sends its credentials to the provider in a signed JWT as specified in the
<a href="https://www.rfc-editor.org/info/rfc7523">
JSON Web Token (JWT) Profile for OAuth 2.0 Client Authentication and Authorization Grants</a>.</p>
</dd>
<dt class="hdlist1"><code>ENCRYPTED_PRIVATE_KEY_JWT</code></dt>
<dd>
<p>The client sends its credentials to the provider in a signed,
then encrypted JWT as specified in the <a href="https://www.rfc-editor.org/info/rfc7523">
JSON Web Token (JWT) Profile for OAuth 2.0 Client Authentication and Authorization Grants</a>.</p>
</dd>
</dl>
</div>
</div>
</div>
<div class="paragraph">
<p>Some authentication methods require additional configuration:</p>
</div>
<details id="JWT-auth-signing">
<summary class="title">How do I configure JWT authentication with signed JWTs?</summary>
<div class="content">
<div class="olist loweralpha">
<ol class="loweralpha" type="a">
<li>
<p>Obtain a list of supported signing algorithms from the provider&#8217;s <code>.well-known</code> endpoint,
and decide which one you will use.</p>
</li>
<li>
<p>In the <span class="label">JWT Signing Algorithm</span> field,
enter the signing algorithm that Advanced Identity Cloud will use to sign the JWT.
For example, <code>RSA256</code>.</p>
<div class="paragraph">
<p>This field may already be configured if the client is sending request objects.</p>
</div>
</li>
<li>
<p>Provide a JWK with the public key to the identity provider.
Read their documentation for more information.</p>
<div class="paragraph">
<p>For example, you could copy the contents of the public JWK in a field in the provider&#8217;s service configuration,
or you could configure the realm&#8217;s <code>/oauth2/connect/rp/jwk_uri</code> endpoint, which exposes the client&#8217;s public keys.</p>
</div>
<div class="paragraph">
<p>Configure the realm&#8217;s <code>/oauth2/connect/rp/jwk_uri</code> endpoint in the provider, which exposes the client&#8217;s public keys.
Read the provider&#8217;s documentation for more information.</p>
</div>
</li>
<li>
<p>Change the value in the <span class="label">Private Key JWT Expiration Time (seconds)</span> field, if needed.
It has a sensible value preconfigured, but you may need to tune it for your provider.</p>
</li>
</ol>
</div>
</div>
</details>
<details>
<summary class="title">How do I configure JWT authentication with signed and encrypted JWTs?</summary>
<div class="content">
<div class="olist loweralpha">
<ol class="loweralpha" type="a">
<li>
<p>Follow the steps in <a href="#JWT-auth-signing">How do I configure JWT authentication with signed JWTs?</a> to configure Advanced Identity Cloud to sign authentication JWTs.</p>
<div class="paragraph">
<p>Now you&#8217;re ready to configure Advanced Identity Cloud to encrypt authentication JWTs.</p>
</div>
</li>
<li>
<p>Obtain a list of supported encryption algorithms and methods from the provider&#8217;s <code>.well-known</code> endpoint,
and decide which one you will use.</p>
</li>
<li>
<p>In the <span class="label">JWT Encryption Algorithm</span> field, select the encryption algorithm.</p>
<div class="paragraph">
<p>If the required encryption algorithm doesn&#8217;t appear in the list,
check the reference entry for the <a href="#jwt-encryption-algorithm">JWT Encryption Algorithm</a> field for information on how to add it.</p>
</div>
<div class="paragraph">
<p>This field may already be configured if the client is encrypting request objects.</p>
</div>
</li>
<li>
<p>In the <span class="label">JWT Encryption Method</span> field, select the encryption method.</p>
<div class="paragraph">
<p>This field may already be configured if the client is encrypting request objects.</p>
</div>
</li>
<li>
<p>In the <span class="label">JWKS URI Endpoint</span> field, configure the URI containing the provider&#8217;s public JWK set.</p>
<div class="paragraph">
<p>Obtain the URI from the provider&#8217;s <code>.well-known</code> endpoint, or their documentation.</p>
</div>
<div class="paragraph">
<p>Advanced Identity Cloud uses the JWK URI to fetch the provider&#8217;s public encryption key.</p>
</div>
</li>
<li>
<p>Perform one of the following steps depending on the encryption method you configured:</p>
<div class="olist lowerroman">
<ol class="lowerroman" type="i">
<li>
<p>If you chose Direct AES Encryption method, select <code>NONE</code> in the <span class="label">JWT Signing Algorithm</span> field.
Signing is redundant with this encryption method.</p>
</li>
<li>
<p>If you chose an encryption method different from the Direct AES Encryption method, configure signing.
Find more information in <a href="#JWT-auth-signing">How do I configure JWT authentication with signed JWTs?</a>.</p>
</li>
</ol>
</div>
</li>
</ol>
</div>
</div>
</details>
<div class="paragraph">
<p>Required: Yes.</p>
</div>
</dd>
<dt class="hdlist1">PKCE Method</dt>
<dd>
<p>Specifies the PKCE transformation method Advanced Identity Cloud uses
when making requests to the provider&#8217;s authorization endpoint, as specified in
<a href="https://www.rfc-editor.org/rfc/rfc7636.html#section-4.2">Section 4.2</a>
of the <em class="ref">Proof Key for Code Exchange by OAuth Public Clients</em> specification.</p>
<div class="paragraph">
<p>Select <code>NONE</code> to disable PKCE transformations.</p>
</div>
<div class="paragraph">
<p>Required: No.</p>
</div>
</dd>
<dt class="hdlist1">Request Parameter JWT Option</dt>
<dd>
<p>(OIDC providers only) Specifies whether Advanced Identity Cloud should provide a request object JWT to the provider.
Possible values are:</p>
<div class="dlist">
<dl>
<dt class="hdlist1"><code>NONE</code></dt>
<dd>
<p>Advanced Identity Cloud doesn&#8217;t send a request object to the provider.</p>
</dd>
<dt class="hdlist1"><code>REFERENCE</code></dt>
<dd>
<p>The request object JWT is stored by Advanced Identity Cloud, which exposes a unique identifier for it using the <code>oauth2/request_uri</code> endpoint for the realm.
The endpoint URL and the JWT&#8217;s unique identifier are passed to the provider in the <code>request_uri</code> parameter of the request.</p>
<div class="paragraph">
<p>Ensure that the provider can reach the endpoint.</p>
</div>
<div class="paragraph">
<p>An example of the URL is
<code>https://platform.example.com:8443/am/realms/root/realms/myRealm/oauth2/request_uri/<em>requestobjectID</em></code></p>
</div>
<div class="admonitionblock note">
<table>
<tr>
<td class="icon">
<i class="fa icon-note" title="Note"></i>
</td>
<td class="content">
<div class="paragraph">
<p>When integrating with <a href="https://www.itsme.be/en/">itsme<sup>&#174;</sup></a>, ensure that the base URL of Advanced Identity Cloud contains the <code>443</code> port.
For example, <code>https://platform.example.com:443/am</code>.</p>
</div>
</td>
</tr>
</table>
</div>
<details>
<summary class="title">How do I configure the Base URL Source service?</summary>
<div class="content">
<div class="olist loweralpha">
<ol class="loweralpha" type="a">
<li>
<p>Under <span class="label">Native Consoles &gt; Access Management</span>, go to <span class="label">Realms &gt; <em>Realm Name</em> &gt; Services</span>.</p>
</li>
<li>
<p>Add a <code>Base URL Source</code> service (if one isn&#8217;t already configured) or select it to change its properties:</p>
<div class="imageblock">
<div class="content">
<img src="_images/base-URL-itsme.png" alt="A screenshot showing itsme example configuration details for the Base URL Source service" width="600">
</div>
</div>
</li>
</ol>
</div>
</div>
</details>
</dd>
<dt class="hdlist1"><code>VALUE</code></dt>
<dd>
<p>Advanced Identity Cloud appends the JWT as the value of the <code>request</code> parameter of the request.</p>
<details id="how-to-sign-request-objects">
<summary class="title">How do I configure the client to send signed request objects?</summary>
<div class="content">
<div class="olist loweralpha">
<ol class="loweralpha" type="a">
<li>
<p>In the <span class="label">Request Parameter JWT Option</span> field, select either <code>VALUE</code> or <code>REFERENCE</code>.</p>
<div class="paragraph">
<p>Read your identity provider&#8217;s documentation for more information.</p>
</div>
</li>
<li>
<p>Obtain a list of supported signing algorithms from the provider&#8217;s <code>.well-known</code> endpoint,
and decide which one you will use.</p>
</li>
<li>
<p>In the <span class="label">JWT Signing Algorithm</span> field,
select the signing algorithm that Advanced Identity Cloud will use to sign the request object.
For example, <code>RS256</code>.</p>
<div class="paragraph">
<p>This field may already be configured if the client is using JWT client authentication.</p>
</div>
</li>
<li>
<p>Provide a JWK with the public key to the identity provider.
Read their documentation for more information.</p>
<div class="paragraph">
<p>For example, you could copy the contents of the public JWK in a field in the provider&#8217;s service configuration,
or you could configure the realm&#8217;s <code>/oauth2/connect/rp/jwk_uri</code> endpoint, which exposes the client&#8217;s public keys.</p>
</div>
<div class="paragraph">
<p>Configure the realm&#8217;s <code>/oauth2/connect/rp/jwk_uri</code> endpoint in the provider, which exposes the client&#8217;s public keys.
Read the provider&#8217;s documentation for more information.</p>
</div>
</li>
</ol>
</div>
</div>
</details>
<details>
<summary class="title">How do I configure the client to send signed and encrypted request objects?</summary>
<div class="content">
<div class="olist loweralpha">
<ol class="loweralpha" type="a">
<li>
<p>Follow the steps in <a href="#how-to-sign-request-objects">How do I configure the client to send signed request objects?</a> to configure Advanced Identity Cloud to send signed request objects.</p>
<div class="paragraph">
<p>Now you&#8217;re ready to configure Advanced Identity Cloud to send encrypted request objects.</p>
</div>
</li>
<li>
<p>Select <span class="label">Encrypt Request Parameter JWT</span>.</p>
</li>
<li>
<p>Obtain a list of supported encryption algorithms and methods from the provider&#8217;s <code>.well-known</code> endpoint,
and decide which one you will use.</p>
</li>
<li>
<p>In the <span class="label">JWT Encryption Algorithm</span> field, select the encryption algorithm.</p>
<div class="paragraph">
<p>If the required encryption algorithm doesn&#8217;t appear in the list,
check the reference entry for the <a href="#jwt-encryption-algorithm">JWT Encryption Algorithm</a> field for information on how to add it.</p>
</div>
<div class="paragraph">
<p>This field may already be configured if the client is encrypting authentication JTWs.</p>
</div>
</li>
<li>
<p>In the <span class="label">JWT Encryption Method</span> field, select the encryption method.</p>
<div class="paragraph">
<p>This field may already be configured if the client is encrypting authentication JWTs.</p>
</div>
</li>
<li>
<p>In the <span class="label">JWKS URI Endpoint</span> field, configure the URI containing the provider&#8217;s public JWK set.</p>
<div class="paragraph">
<p>Obtain the URI from the provider&#8217;s <code>.well-known</code> endpoint.</p>
</div>
<div class="paragraph">
<p>Advanced Identity Cloud uses the JWK URI to fetch the provider&#8217;s public encryption key.</p>
</div>
</li>
<li>
<p>Perform one of the following steps depending on the encryption method you configured:</p>
<div class="olist lowerroman">
<ol class="lowerroman" type="i">
<li>
<p>If you chose Direct AES Encryption method, select <code>NONE</code> in the <span class="label">JWT Signing Algorithm</span> field.
Signing is redundant with this encryption method.</p>
</li>
<li>
<p>If you chose an encryption method different from the Direct AES Encryption method, configure signing.
Find more information in <a href="#how-to-sign-request-objects">How do I configure the client to send signed request objects?</a>.</p>
</li>
</ol>
</div>
</li>
</ol>
</div>
</div>
</details>
</dd>
</dl>
</div>
</dd>
<dt class="hdlist1">Require exp claim in Request Object</dt>
<dd>
<p>(OIDC providers only) If selected, the <code>exp</code> claim must be included in JWT request objects in
the <a href="../am-oauth2/oauth2-authorize-endpoint.html" class="xref page">/oauth2/authorize</a> request.</p>
<div class="paragraph">
<p>The <code>exp</code> (expiration time) claim defines the lifetime of the JWT, after which the
JWT is no longer valid.</p>
</div>
<div class="paragraph">
<p>The default value of this attribute is false.</p>
</div>
</dd>
<dt class="hdlist1">Encrypt Request Parameter JWT</dt>
<dd>
<p>Specifies whether the request parameter must be encrypted when <span class="label">Request Parameter JWT Option</span>
is set to <code>REFERENCE</code> or <code>VALUE</code>.</p>
</dd>
<dt class="hdlist1">ACR Values</dt>
<dd>
<p>(OIDC providers only) A space-separated list, in order of preference, of the client&#8217;s <code>acr</code> values.</p>
<div class="paragraph">
<p>Required: No.</p>
</div>
</dd>
<dt class="hdlist1">Well Known Endpoint</dt>
<dd>
<p>(OIDC providers only) The URL for retrieving information about the provider,
such as endpoints, and public keys.
For example, <code>https://accounts.google.com/.well-known/openid-configuration</code>.</p>
<div class="admonitionblock note">
<table>
<tr>
<td class="icon">
<i class="fa icon-note" title="Note"></i>
</td>
<td class="content">
Leave this field empty for the <code>LINE (Browser)</code> configuration.
</td>
</tr>
</table>
</div>
<div class="paragraph">
<p>Required: No.</p>
</div>
</dd>
<dt class="hdlist1">Request Object Audience</dt>
<dd>
<p>(OIDC providers only) The intended audience (<code>aud</code>) of the request object
when the <span class="label">Request Parameter JWT Option</span> field is set to <code>VALUE</code> or <code>REFERENCE</code>.</p>
<div class="paragraph">
<p>When not configured, Advanced Identity Cloud uses the value of the <span class="label">Issuer</span> field.</p>
</div>
</dd>
<dt class="hdlist1">Private Key JWT Audience</dt>
<dd>
<p>(OIDC providers only) The intended audience (<code>aud</code>) of the private key JWT when performing an authentication using the <code>PRIVATE_KEY_JWT</code> client authentication method.</p>
<div class="paragraph">
<p>When not configured, Advanced Identity Cloud uses the value of the <span class="label">Access Token Endpoint URL</span> field.</p>
</div>
</dd>
<dt class="hdlist1">OP Encrypts ID Tokens</dt>
<dd>
<p>(OIDC providers only) Whether the provider encrypts ID Tokens.</p>
<details>
<summary class="title">How do I configure Advanced Identity Cloud to receive encrypted tokens?</summary>
<div class="content">
<div class="paragraph">
<p>Provide a JWK with the public key to the identity provider.
Read the identity provider&#8217;s documentation for more information.</p>
</div>
<div class="paragraph">
<p>For example, you could copy the contents of the public JWK in a field in the provider&#8217;s service configuration,
or you could configure the realm&#8217;s <code>/oauth2/connect/rp/jwk_uri</code> endpoint, which exposes the client&#8217;s public keys.</p>
</div>
<div class="paragraph">
<p>Configure the realm&#8217;s <code>/oauth2/connect/rp/jwk_uri</code> endpoint in the provider, which exposes the client&#8217;s public keys.
Read the provider&#8217;s documentation for more information.</p>
</div>
</div>
</details>
<div class="paragraph">
<p>Required: No.</p>
</div>
</dd>
<dt class="hdlist1">Issuer</dt>
<dd>
<p>(OIDC providers only) The issuer of ID Tokens.</p>
<div class="paragraph">
<p>Specify a regular expression or a string value that exactly matches the value returned in the ID token.
What you set here depends on the value of the <a href="#issuer-comparison-check">Issuer comparison check</a> property.</p>
</div>
<div class="paragraph">
<p>Obtain the <code>issuer</code> value from the provider&#8217;s <code>.well-known</code> endpoint.</p>
</div>
<div class="paragraph">
<p>Required: Yes.</p>
</div>
</dd>
<dt class="hdlist1">Enable Native Nonce</dt>
<dd>
<p>(OIDC providers only) When selected, the provider native SDK must include a <code>nonce</code> claim in the ID token.
The value of the claim must be the value of the <code>nonce</code> claim sent in the Authentication Request.</p>
<div class="paragraph">
<p>Required: No.</p>
</div>
</dd>
<dt class="hdlist1">User Info Response Format</dt>
<dd>
<p>(OIDC providers only) The format in which the provider&#8217;s <code>userinfo</code> endpoint returns data.</p>
<div class="paragraph">
<p>Some options require additional configuration:</p>
</div>
<details id="signed-userinfo-JWT">
<summary class="title">How do I configure the client to receive signed userinfo JWTs?</summary>
<div class="content">
<div class="paragraph">
<p>In the <span class="label">JWKS URI Endpoint</span> field, configure the URL containing the provider&#8217;s public JWK set.
Obtain it from the provider&#8217;s <code>.well-known</code> endpoint, or their documentation.</p>
</div>
<div class="paragraph">
<p>Advanced Identity Cloud uses this URL to fetch the provider&#8217;s public signing key.</p>
</div>
</div>
</details>
<details>
<summary class="title">How do I configure the client to receive signed, then encrypted userinfo JWTs?</summary>
<div class="content">
<div class="olist arabic">
<ol class="arabic">
<li>
<p>Follow the steps in <a href="#signed-userinfo-JWT">How do I configure the client to receive signed userinfo JWTs?</a> to configure Advanced Identity Cloud to receive signed JWTs.</p>
<div class="paragraph">
<p>Now you&#8217;re ready to configure Advanced Identity Cloud to receive encrypted JWTs.</p>
</div>
</li>
<li>
<p>Provide a JWK with the public key to the identity provider.
Read their documentation for more information.</p>
<div class="paragraph">
<p>For example, you could copy the contents of the public JWK in a field in the provider&#8217;s service configuration,
or you could configure the realm&#8217;s <code>/oauth2/connect/rp/jwk_uri</code> endpoint, which exposes the client&#8217;s public keys.</p>
</div>
</li>
<li>
<p>Configure the realm&#8217;s <code>/oauth2/connect/rp/jwk_uri</code> endpoint in the provider, which exposes the client&#8217;s public keys.
Read the provider&#8217;s documentation for more information.</p>
</li>
</ol>
</div>
</div>
</details>
<div class="paragraph">
<p>Possible values are:</p>
</div>
<div class="dlist">
<dl>
<dt class="hdlist1"><code>JSON</code></dt>
<dd>
<p>The provider&#8217;s <code>userinfo</code> endpoint returns a JSON object.</p>
</dd>
<dt class="hdlist1"><code>SIGNED_JWT</code></dt>
<dd>
<p>The provider&#8217;s <code>userinfo</code> endpoint returns a signed JWT.</p>
</dd>
<dt class="hdlist1"><code>SIGNED_THEN_ENCRYPTED_JWT</code></dt>
<dd>
<p>The provider&#8217;s <code>userinfo</code> endpoint returns a signed, then encrypted JWT.</p>
</dd>
</dl>
</div>
</dd>
<dt class="hdlist1">JWKS URI Endpoint</dt>
<dd>
<p>The URI that contains the public keys of the identity provider.
Advanced Identity Cloud uses these keys to verify signatures or to encrypt objects.</p>
<div class="paragraph">
<p>Configure this field when:</p>
</div>
<div class="ulist">
<ul>
<li>
<p><span class="label">Client Authentication Method</span> is set to <code>ENCRYPTED_PRIVATE_KEY_JWT</code>.</p>
</li>
<li>
<p><span class="label">Encrypt Request Parameter JWT</span> is selected.</p>
</li>
<li>
<p><span class="label">User Info Response Format</span> is set to <code>SIGNED_JWT</code> or <code>SIGNED_THEN_ENCRYPTED_JWT</code>.</p>
</li>
</ul>
</div>
<div class="paragraph">
<p>Required: No.</p>
</div>
</dd>
<dt class="hdlist1">Claims</dt>
<dd>
<p>Any claims on the request object, in JSON format. These claims must conform to the
<a href="https://openid.net/specs/openid-connect-core-1_0.html#ClaimsParameter">claims request parameter</a>, as defined in the
<em>OpenID Connect specification</em>.</p>
</dd>
<dt class="hdlist1">JWT Signing Algorithm</dt>
<dd>
<p>The signing algorithm supported by the provider that Advanced Identity Cloud uses to sign the following:</p>
<div class="ulist">
<ul>
<li>
<p>Client authentication JWTs when <span class="label">Client Authentication Method</span> is set to <code>PRIVATE_KEY_JWT</code>.</p>
</li>
<li>
<p>(OIDC providers only) Request JWTs when <span class="label">Request Parameter JWT Option</span>
is set to <code>VALUE</code> or <code>REFERENCE</code>.</p>
</li>
</ul>
</div>
<div class="paragraph">
<p>Obtain a list of the supported algorithms from the provider&#8217;s <code>.well-known</code> endpoint.
Select <code>NONE</code> if the client will encrypt the JWT with the Direct AES Encryption method,
because the signature will be redundant.<br>
Required: No.</p>
</div>
</dd>
</dl>
</div>
<div id="jwt-encryption-algorithm" class="dlist">
<dl>
<dt class="hdlist1">JWT Encryption Algorithm</dt>
<dd>
<p>The encryption algorithm supported by the provider that Advanced Identity Cloud uses to encrypt
client authentication JWTs. Applies only when <span class="label">Client Authentication Method</span> is set to <code>PRIVATE_KEY_JWT</code>, and OIDC providers request JWTs when <span class="label">Request Parameter JWT Option</span>
is set to <code>VALUE</code> or <code>REFERENCE</code>.</p>
<div class="paragraph">
<p>When set to <code>NONE</code>, Advanced Identity Cloud won&#8217;t encrypt the JWTs.
Obtain a list of the supported algorithms from the provider&#8217;s <code>.well-known</code> endpoint.</p>
</div>
<div class="paragraph">
<p>Required: No.</p>
</div>
</dd>
<dt class="hdlist1">JWT Encryption Method</dt>
<dd>
<p>The encryption method supported by the provider that Advanced Identity Cloud uses to encrypt the following:</p>
<div class="ulist">
<ul>
<li>
<p>Client authentication JWTs when <span class="label">Client Authentication Method</span> is set to <code>PRIVATE_KEY_JWT</code>.</p>
</li>
<li>
<p>(OIDC providers only) Request JWTs when <span class="label">Request Parameter JWT Option</span>
is set to <code>VALUE</code> or <code>REFERENCE</code>.</p>
</li>
</ul>
</div>
<div class="paragraph">
<p>Use in conjunction with <code>JWT Encryption Algorithm</code>.
Obtain a list of the supported methods from the provider&#8217;s <code>.well-known</code> endpoint.<br>
Required: No.</p>
</div>
</dd>
<dt class="hdlist1">Private Key JWT Expiration Time (seconds)</dt>
<dd>
<p>Specifies the amount of time, in seconds,
that Advanced Identity Cloud will cache the client authentication JWT before creating a new one.</p>
<div class="paragraph">
<p>Caching the JWT avoids creating a new one for every client authentication.
However, the JWT can also become invalid if the provider changes its configuration.</p>
</div>
<div class="paragraph">
<p>Required: No.</p>
</div>
</dd>
</dl>
</div>
<div id="response-mode" class="dlist">
<dl>
<dt class="hdlist1">Response Mode</dt>
<dd>
<p>(OIDC providers only) Specify the way the provider returns ID tokens to Advanced Identity Cloud.
Possible values are:</p>
<div class="ulist">
<ul>
<li>
<p><code>DEFAULT</code>. The provider returns the ID token as query parameters, as explained in the
<a href="https://openid.net/specs/openid-connect-core-1_0.html">OpenID Connect Core 1.0 incorporating errata set 1</a> specification.</p>
<div class="paragraph">
<p>Most preconfigured providers use the <code>DEFAULT</code> response mode.</p>
</div>
</li>
<li>
<p><code>FORM_POST</code>. The provider returns the ID token by submitting an HTML form using the HTTP POST method,
as explained in the
<a href="https://openid.net/specs/oauth-v2-form-post-response-mode-1_0.html">OAuth 2.0 Form Post Response Mode</a> specification.</p>
<div class="paragraph">
<p>When using this response mode, add the <code>/oauth2/client/form_post/<em class="var">social IdP client</em></code> URI
to the <span class="label">Redirect URL</span>, where <em class="var">social IdP client</em> is the name of the social identity provider client
that you&#8217;re configuring.
For example, <code>https://<span class="var">&lt;tenant-env-fqdn></span>/oauth2/client/form_post/myAppleClient</code> or <code>https://<span class="var">&lt;tenant-env-fqdn></span>/oauth2/alpha/client/form_post/myAppleClient</code> if you need to specify a realm.</p>
</div>
</li>
</ul>
</div>
<div class="paragraph">
<p>By default, the <code>form_post</code> endpoint processes the post data, encrypts it,
and redirects with it back to the authentication journey to resume authentication.</p>
</div>
<div class="paragraph">
<p>+
However, environments using custom login pages need to configure the <span class="label">Redirect after form post URL</span> property
to redirect back to the custom login pages.</p>
</div>
<div class="paragraph">
<p>+
Required: Yes.</p>
</div>
</dd>
</dl>
</div>
<div id="revocation-checking-option" class="dlist">
<dl>
<dt class="hdlist1">Certificate Revocation Checking Options</dt>
<dd>
<p>Specify one or more options to be used by the TLS certificate revocation checking mechanism.</p>
<div class="paragraph">
<p>The possible values are:</p>
</div>
<div class="ulist">
<ul>
<li>
<p><code>ONLY_END_ENTITY</code>: Only check the revocation status of end-entity certificates.</p>
</li>
<li>
<p><code>PREFER_CRLS</code>: Prefer certificate revocation lists (CRLs) to Online Certificate Status Protocol (OCSP).</p>
</li>
<li>
<p><code>NO_FALLBACK</code>: Disable the fallback mechanism.</p>
</li>
<li>
<p><code>SOFT_FAIL</code>: Allow revocation check to succeed if the revocation status cannot be determined due to a network error.</p>
</li>
<li>
<p><code>DISABLE_REVOCATION_CHECKING</code>: Disable all revocation checking.</p>
</li>
</ul>
</div>
<div class="openblock">
<div class="content">
<div class="paragraph">
<p>Including <code>DISABLE_REVOCATION_CHECKING</code> as one of the options will prevent any revocation checking.
For further details of the other options, refer to:
<a href="https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/security/cert/PKIXRevocationChecker.Option.html">PKIXRevocationChecker.Option</a>.</p>
</div>
<div class="paragraph">
<p>If no options are selected, the default behavior is to enable revocation checking with <code>SOFT_FAIL</code>.</p>
</div>
<div class="paragraph">
<p>If the certificate doesn&#8217;t specify any OCSP or CRL endpoints, the revocation checking will hard fail even if the <code>SOFT_FAIL</code> option is selected.
In this case, an administrator could disable revocation checking.</p>
</div>
</div>
</div>
</dd>
</dl>
</div>
<div id="use-custom-trust-store" class="dlist">
<dl>
<dt class="hdlist1">Use Custom TrustStore</dt>
<dd>
<p>Specifies whether a custom truststore is used to verify the server certificate of the
<code>.well-known</code> endpoint or JWKs URI of an OpenID provider (OP) in a TLS handshake.</p>
<div class="paragraph">
<p>If selected, a secret label is generated dynamically using the alphanumeric characters of
the client configuration name. For example, a client configuration called <code>sampleOidcConfig</code>
results in a secret label named <code>am.services.oidc.reliant.party.sampleOidcConfig.truststore</code>.</p>
</div>
<div class="paragraph">
<p>Map the generated secret label to an <a href="../tenants/esvs-signing-encryption.html#map-esv-secrets-to-secret-labels" class="xref page">ESV secret</a>.</p>
</div>
<div class="paragraph">
<p>If this setting is not selected, the default truststore is used to verify the server certificate.</p>
</div>
</dd>
</dl>
</div>
<div id="request-native-app-for-userinfo" class="dlist">
<dl>
<dt class="hdlist1">Request Native App for UserInfo</dt>
<dd>
<p>(Apple SSO) When selected, this flag indicates that the native app can send the user&#8217;s <code>userinfo</code> in JSON format.</p>
<div class="paragraph">
<p>Apple returns the <code>userinfo</code> only <em>once</em>, when the user first consents to send their details, and not on subsequent
authentication attempts. In addition, the user has the option <em>not</em> to consent to Apple sending their <code>userinfo</code>.</p>
</div>
<div class="paragraph">
<p>If you&#8217;re progressively profiling the <code>userinfo</code> with data from other social providers (usually using a <a href="https://docs.pingidentity.com/auth-node-ref/latest/patch-object.html">Patch Object node</a>) there is a risk of overwriting the user&#8217;s details with blank values when the user authenticates through Apple SSO.</p>
</div>
<div class="paragraph">
<p>To mitigate this risk, you can add a <a href="https://docs.pingidentity.com/auth-node-ref/latest/scripted-decision.html">Scripted Decision node</a> to your authentication journey to assess whether
<code>userinfo</code> is provided.</p>
</div>
<details>
<summary class="title">How do I use a Scripted Decision node to check <code>userinfo</code>?</summary>
<div class="content">
<div class="paragraph">
<p>The <a href="../am-scripting/sample-scripts.html#normalized-profile-to-managed-user-js" class="xref page">normalized-profile-to-managed-user.js</a>
script sets a boolean flag (<code>nameEmptyOrNull</code>) that indicates whether Apple returned the user&#8217;s <code>firstName</code> and <code>lastName</code>.</p>
</div>
<div class="paragraph">
<p>Add a <a href="https://docs.pingidentity.com/auth-node-ref/latest/scripted-decision.html">Scripted Decision node</a> to your journey that evaluates the flag and sets the outcome accordingly; for example:</p>
</div>
<div id="tabs_1" class="openblock tabs is-loading">
<div class="content">
<div class="ulist tablist">
<ul>
<li id="tabs_1_next_generation" class="tab">
<p>Next-generation</p>
</li>
<li id="tabs_1_legacy" class="tab">
<p>Legacy</p>
</li>
</ul>
</div>
<div id="tabs_1_next_generation--panel" class="tabpanel" aria-labelledby="tabs_1_next_generation">
<div class="listingblock">
<div class="content">
<pre class="highlightjs highlight"><code class="language-javascript hljs" data-lang="javascript">if (nodeState.get('nameEmptyOrNull')) {
  action.goTo("true");
} else {
  action.goTo("false");
}</code></pre>
</div>
</div>
</div>
<div id="tabs_1_legacy--panel" class="tabpanel" aria-labelledby="tabs_1_legacy">
<div class="listingblock">
<div class="content">
<pre class="highlightjs highlight"><code class="language-javascript hljs" data-lang="javascript">var fr = JavaImporter(org.forgerock.openam.auth.node.api.Action);

if (nodeState.get('nameEmptyOrNull')) {
  action = fr.Action.goTo("true").build();
} else {
action = fr.Action.goTo("false").build();
}</code></pre>
</div>
</div>
</div>
</div>
</div>
<div class="paragraph">
<p>You can now configure your journey to patch the <code>userinfo</code> object based on the outcome of the <a href="https://docs.pingidentity.com/auth-node-ref/latest/scripted-decision.html">Scripted Decision node</a>.
If you need to progressively profile the user information on every authentication,
<em>regardless of whether the user&#8217;s first name and last name are returned by the OIDC provider</em>,
you can use another <a href="https://docs.pingidentity.com/auth-node-ref/latest/scripted-decision.html">Scripted Decision node</a> that does the following:</p>
</div>
<div class="ulist">
<ul>
<li>
<p>If the user details aren&#8217;t present, route the <code>userinfo</code> patch through a <a href="https://docs.pingidentity.com/auth-node-ref/latest/patch-object.html">Patch Object node</a>
configured to ignore the <code>firstName</code> and <code>lastName</code>. (In the <span class="label">Ignored Fields</span> list, add <code>givenName</code> to ignore
the <code>firstName</code> and <code>sn</code> to ignore the <code>lastName</code>.)</p>
</li>
<li>
<p>If the user details are present, route the <code>userinfo</code> patch through a <a href="https://docs.pingidentity.com/auth-node-ref/latest/patch-object.html">Patch Object node</a> that patches the full object.</p>
</li>
</ul>
</div>
<div class="paragraph">
<p>Learn more in <a href="https://support.pingidentity.com/s/article/First-name-and-last-name-get-blanked-out-when-signing-in-to-Advanced-Identity-Cloud-or-PingAM-using-Apple-social-signon">First name and last name are missing when signing in to Identity Cloud or PingAM using Apple social sign-on</a>.</p>
</div>
</div>
</details>
<div class="paragraph">
<p>Required: No.</p>
</div>
</dd>
</dl>
</div>
<div id="transform-script" class="dlist">
<dl>
<dt class="hdlist1">Transform Script</dt>
<dd>
<p>A script to convert the provider&#8217;s raw profile object into a normalized object,
also referred to as a <em>normalization</em> script.</p>
<div class="openblock">
<div class="content">
<div class="paragraph">
<p>Each social identity provider returns different user profile information using their own attribute names.</p>
</div>
<div class="paragraph">
<p>For example, Google&#8217;s OIDC <code>/userinfo</code> endpoint returns claims, which Advanced Identity Cloud stores in a <code>rawProfile</code> object.
The following <code>google-profile-normalization.js</code> script maps the attributes of this object to Advanced Identity Cloud profile attributes:</p>
</div>
<div id="tabs_2" class="openblock tabs is-loading">
<div class="content">
<div class="ulist tablist">
<ul>
<li id="tabs_2_next_generation" class="tab">
<p>Next-generation</p>
</li>
<li id="tabs_2_legacy" class="tab">
<p>Legacy</p>
</li>
</ul>
</div>
<div id="tabs_2_next_generation--panel" class="tabpanel" aria-labelledby="tabs_2_next_generation">
<div class="listingblock">
<div class="content">
<pre class="highlightjs highlight"><code class="language-javascript hljs" data-lang="javascript">function () {
    var normalizedProfileData = {};
    normalizedProfileData.id = rawProfile.get('sub');
    normalizedProfileData.displayName = rawProfile.get('name');
    normalizedProfileData.givenName = rawProfile.get('given_name');
    normalizedProfileData.familyName = rawProfile.get('family_name');
    normalizedProfileData.photoUrl = rawProfile.get('picture');
    normalizedProfileData.email = rawProfile.get('email');
    normalizedProfileData.username = rawProfile.get('email');
    normalizedProfileData.locale = rawProfile.get('locale');
    return normalizedProfileData;
}();</code></pre>
</div>
</div>
</div>
<div id="tabs_2_legacy--panel" class="tabpanel" aria-labelledby="tabs_2_legacy">
<div class="listingblock">
<div class="content">
<pre class="highlightjs highlight"><code class="language-javascript hljs" data-lang="javascript">(function () {
    var frJava = JavaImporter(
        org.forgerock.json.JsonValue
    );

    var normalizedProfileData = frJava.JsonValue.json(frJava.JsonValue.object());

    normalizedProfileData.put('id', rawProfile.get('sub'));
    normalizedProfileData.put('displayName', rawProfile.get('name'));
    normalizedProfileData.put('givenName', rawProfile.get('given_name'));
    normalizedProfileData.put('familyName', rawProfile.get('family_name'));
    normalizedProfileData.put('photoUrl', rawProfile.get('picture'));
    normalizedProfileData.put('email', rawProfile.get('email'));
    normalizedProfileData.put('username', rawProfile.get('email'));
    normalizedProfileData.put('locale', rawProfile.get('locale'));

    return normalizedProfileData;
}());</code></pre>
</div>
</div>
</div>
</div>
</div>
<div class="paragraph">
<p>The script returns a JsonValue object containing normalized attributes in the following format:</p>
</div>
<div class="listingblock">
<div class="content">
<pre class="highlightjs highlight"><code class="language-bash hljs" data-lang="bash">("<span class="var"><em>platformAttributeName</em></span>", rawProfile.<span class="var"><em>providerAttributeName</em></span>)</code></pre>
</div>
</div>
<div class="paragraph">
<p>Even if field names are the same, such as <code>email</code> and <code>rawProfile.email</code>,
they still need to be mapped for them to be included in the returned JSON object.</p>
</div>
<div class="paragraph">
<p>Advanced Identity Cloud provides default scripts for other preconfigured identity providers.
Find information about the bindings and expected return values in the <code><span class="var"><em>identity provider</span></em>-profile-normalization.*</code>
scripts in <a href="../am-scripting/sample-scripts.html" class="xref page">Sample scripts</a> and in the <a href="../am-scripting/social-idp-profile-transformation-api.html" class="xref page">Social IdP scripting API</a>.</p>
</div>
<div class="paragraph">
<p>To write your own script in Javascript for an identity provider,
go to <span class="label">Realms &gt; <em>Realm Name</em> &gt; Scripts</span>, and use the provided scripts as a reference.</p>
</div>
<div class="paragraph">
<p>When a user authenticates, the social authentication journey calls another transformation script
set in the <a href="https://docs.pingidentity.com/auth-node-ref/latest/social-provider-handler.html">Social Provider Handler node</a> to convert the attributes again;
this time into an identity object that Advanced Identity Cloud can process.</p>
</div>
<div class="admonitionblock important">
<table>
<tr>
<td class="icon">
<i class="fa icon-important" title="Important"></i>
</td>
<td class="content">
<div class="paragraph">
<p>Social authentication nodes expect every attribute to have a value.
In other words, the attributes returned by the identity provider can&#8217;t be empty or <code>null</code>, or the journey will end with an error.</p>
</div>
<div class="paragraph">
<p>For example, if a user tries to log in using Google as the identity provider, but they didn&#8217;t configure a surname in their account, Google returns <code>null</code> as the value of the <code>familyName</code> for the identity, and social authentication fails.</p>
</div>
<div class="paragraph">
<p>Ensure all users have their social profiles configured correctly, or modify the transformation scripts so that they don&#8217;t collect null or empty attributes.</p>
</div>
</td>
</tr>
</table>
</div>
<div class="paragraph">
<p>Required: Yes</p>
</div>
</div>
</div>
</dd>
</dl>
</div>
<div id="issuer-comparison-check" class="dlist">
<dl>
<dt class="hdlist1">Issuer comparison check</dt>
<dd>
<p>(OIDC providers only)
Determines how the expected issuer value should match the actual value of the <code>iss</code> claim:</p>
<div class="ulist">
<ul>
<li>
<p><code>EXACT</code>: Advanced Identity Cloud performs a string comparison between the expected and actual issuer values,
which must result in an exact match.</p>
</li>
<li>
<p><code>REGEX</code>: Advanced Identity Cloud evaluates the expected issuer value as a regular expression,
against which the actual value must match.</p>
<div class="paragraph">
<p>This lets social identity providers use a common issuer value for multiple tenants,
which is replaced with a unique value during the OIDC authentication flow.
For example, <code><a href="https://login.microsoftonline.com/(.*)/v2.0$" class="bare">https://login.microsoftonline.com/(.*)/v2.0$</a></code>
is successfully matched against <code>https://login.microsoftonline.com/tenant-d5c6a592-eec6-47f0/v2.0</code>.</p>
</div>
<div class="admonitionblock note">
<table>
<tr>
<td class="icon">
<i class="fa icon-note" title="Note"></i>
</td>
<td class="content">
<div class="paragraph">
<p>Consider the performance impact when constructing regular expressions as the comparison
is performed for each social identity provider interaction.</p>
</div>
<div class="paragraph">
<p>Also, ensure the regular expression is as specific as possible to avoid matching
against incorrect issuer values.</p>
</div>
</td>
</tr>
</table>
</div>
</li>
</ul>
</div>
</dd>
</dl>
</div>
</div>
</div>
<nav class="pagination">
  <span class="prev"><a href="social-authentication-configure.html">Configure social authentication</a></span>
  <span class="next"><a href="social-authentication-journeys.html">Configure basic social registration journeys</a></span>
</nav>
<div id="article-footer" class="doc-feedback-footer"></div>
</article>
<aside class="toc sidebar" data-title="On This Page" data-levels="3">
  <div class="toc-menu"></div>
</aside>
  </div>
</main>
  </div>
</div>
<footer id="shared-footer"><div id="ping-footer">
  <p class="llms-notice"><a href="/llms.txt">AI Index (llms.txt)</a></p>
  <p class="copyright">Copyright &copy; 2026 <a href="https://pingidentity.com">Ping Identity Corporation</a></p>
</div>
</footer>

<footer class="pdf-only">Copyright © 2010-2026 Ping Identity Corporation</footer>

  <script src="https://cdn.forgerock.com/docs-ui/adoc/prod-ping/vendor.antora-scripts.js"></script>
  <script id="site-script" src="https://cdn.forgerock.com/docs-ui/adoc/prod-ping/ping.antora-scripts.js" data-sync-storage-key="frPersistTabs" data-sync-storage-scope="local" data-ui-root-path=""></script>
  </body>
</html>

---

---
title: WebAuthn storage &amp; encryption settings
description: Configure encryption for stored WebAuthn device profile data, including the profile storage attribute and encryption key settings
component: pingoneaic
page_id: pingoneaic:authentication:authentication-methods-webauthn-encryption
canonical_url: https://docs.pingidentity.com/pingoneaic/authentication/authentication-methods-webauthn-encryption.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Authentication", "Multi-factor Authentication (MFA)", "WebAuthn", "FIDO", "passkey", "device profile", "encryption"]
section_ids:
  configure-webauthn-encryption: Configure WebAuthn storage & encryption settings
---

# WebAuthn storage & encryption settings

WebAuthn storage and encryption settings control how Advanced Identity Cloud stores and protects the device metadata registered by end users of WebAuthn authenticators, including passkeys and security keys.

By default, Advanced Identity Cloud creates the configuration with no encryption. For production environments, you should select an encryption scheme and store the associated key in an [ESV secret](../tenants/esvs-signing-encryption.html).

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Updating the encryption key store setting after end users have registered their devices isn't supported. If you change encryption key information (in the configuration or in the secret stores) end users with existing device profiles can no longer sign on using their existing registered passkeys or security keys. You'll need to delete each affected end user's device profile so they can re-register the next time they sign on. |

Learn more about configuring how Advanced Identity Cloud validates authenticator attestations in [WebAuthn verification settings](authentication-methods-webauthn-verification.html).

## Configure WebAuthn storage & encryption settings

1. In the Advanced Identity Cloud admin console, go to [icon: verified_user, set=material, size=inline] Authentication > Authentication Methods.

2. Click WebAuthn Storage & Encryption.

3. If WebAuthn storage & encryption is not already enabled, click Enable WebAuthn Storage & Encryption to create it with default settings before configuring it.

4. Configure the following settings:

   * Profile Storage Attribute

     The end user's attribute in which to store WebAuthn profiles.

   * Device Profile Encryption Scheme

     Encryption scheme to use to secure device profiles stored on the server.

     If enabled, each device profile is encrypted using a unique random secret key using the given strength of AES encryption in CBC mode with PKCS#5 padding. An HMAC-SHA of the given strength (truncated to half-size) is used to ensure integrity protection and authenticated encryption. The unique random key is encrypted with the given RSA key pair and stored with the data.

     The possible values for this property are:

     * `AES-256/HMAC-SHA-512 with RSA Key Wrapping`

     * `AES-128/HMAC-SHA-256 with RSA Key Wrapping`

     * `No encryption of device settings.`

     Default value: `No encryption of device settings.`

   * Encryption Key Store

     Path to the key store from which to load encryption keys.

     |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
     | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
     |   | Updating this setting isn't currently supported in Advanced Identity Cloud. Changing its value may lead to a loss of functionality in this feature.For greater security, store encryption key information in [ESVs](../tenants/esvs-signing-encryption.html), instead of in the configuration. Use the [secret label](../am-reference/secret-id-mappings.html#encrypted-device-storage-secret-labels) `am.services.authenticatorwebauthn.encryption` to map an alias for WebAuthn Profile Encryption secrets.If you update encryption key information in the configuration or in the secret stores, end users with existing device profiles can no longer sign on using their existing registered passkeys or security keys. Delete the end user's device profile so that they can create a new one when they next sign on. |

     |   |                                                                                                                                                                         |
     | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
     |   | If Advanced Identity Cloud finds a matching secret for the `am.services.authenticatorwebauthn.encryption` label in the realm's ESV secret store, this value is ignored. |

   * Key Store Type

     Type of key store to load.

     This property is preconfigured in your Advanced Identity Cloud tenant and shouldn't be altered.

     Default value: `Java Cryptography Extension Key Store (JCEKS)`

   * Key Store Password

     Password to unlock the key store. This password is encrypted when it is saved in the Advanced Identity Cloud configuration.

     |   |                                                                                                                                                                         |
     | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
     |   | If Advanced Identity Cloud finds a matching secret for the `am.services.authenticatorwebauthn.encryption` label in the realm's ESV secret store, this value is ignored. |

   * Key-Pair Alias

     Alias of the certificate and private key in the key store. The private key is used to encrypt and decrypt device profiles.

     |   |                                                                                                                                                                         |
     | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
     |   | If Advanced Identity Cloud finds a matching secret for the `am.services.authenticatorwebauthn.encryption` label in the realm's ESV secret store, this value is ignored. |

   * Private Key Password

     Password to unlock the private key.

5. Click Save.

---

---
title: WebAuthn verification settings
description: Configure the FIDO Metadata Service endpoint and revocation settings that Advanced Identity Cloud uses to verify WebAuthn authenticator attestations
component: pingoneaic
page_id: pingoneaic:authentication:authentication-methods-webauthn-verification
canonical_url: https://docs.pingidentity.com/pingoneaic/authentication/authentication-methods-webauthn-verification.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Authentication", "Multi-factor Authentication (MFA)", "WebAuthn", "FIDO", "passkey", "attestation", "metadata"]
section_ids:
  configure-webauthn-verification: Configure WebAuthn verification settings
---

# WebAuthn verification settings

WebAuthn verification settings control how Advanced Identity Cloud obtains and validates metadata from the [FIDO Metadata Service (MDS)](https://fidoalliance.org/metadata/).

When an end user registers a WebAuthn authenticator, Advanced Identity Cloud can verify the authenticator's attestation, which is a signed statement from the device manufacturer confirming the authenticator's model and security properties. The FIDO MDS provides the metadata and root certificates needed to perform this verification.

These settings are available by default. You only need to configure them if you want to use a custom metadata source, such as a local or non-default metadata blob location, or if you want to enable revocation checking during attestation validation.

Learn more about how to configure Advanced Identity Cloud to store WebAuthn device profiles in [WebAuthn storage & encryption settings](authentication-methods-webauthn-encryption.html).

## Configure WebAuthn verification settings

1. In the Advanced Identity Cloud admin console, go to [icon: verified_user, set=material, size=inline] Authentication > Authentication Methods.

2. Click WebAuthn Verification.

3. If WebAuthn verification is not already enabled, click Enable WebAuthn Verification to create it with default settings before configuring it.

4. Configure the following settings:

   * Metadata service URIs

     The list of locations from which to download the [metadata blob](https://fidoalliance.org/specs/mds/fido-metadata-service-v3.0-ps-20210518.html#metadata-blob).

     Advanced Identity Cloud verifies the blob signature against secrets mapped to the `am.authentication.nodes.webauthn.fidometadataservice.rootcertificate` secret label.

   * Enforce revocation check

     This setting specifies whether Advanced Identity Cloud must check revocation entries from certificates.

     The setting is disabled by default, so Advanced Identity Cloud doesn't check presented certificates for revocation.

     If you enable this setting, Advanced Identity Cloud must be able to verify any attestation certificate's trust chain with a CRL or OCSP entry during processing.

     |   |                                                                                            |
     | - | ------------------------------------------------------------------------------------------ |
     |   | Certificates downloaded from the FIDO Metadata Service might not have a CRL or OCSP entry. |

5. Click Save.