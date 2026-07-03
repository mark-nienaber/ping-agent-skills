---
title: Compatibility
description: The Advanced Identity Cloud/PingAM Login Widget supports the following server versions:
component: login-widget
page_id: login-widget:release-notes:compatibility
canonical_url: https://developer.pingidentity.com/login-widget/release-notes/compatibility.html
revdate: Thu, 25 May 2023 13:44:17 +0100
keywords: ["Compatibility", "Features", "Source Code", "SDK"]
section_ids:
  supported_server_versions: Supported server versions
  supported-os: Supported operating systems and browsers
  webviews_unsupported_sdks: JavaScript Compatibility with WebViews
  supported-callbacks: Supported authentication journey callbacks
---

# Compatibility

## Supported server versions

The Advanced Identity Cloud/PingAM Login Widget supports the following server versions:

* PingOne Advanced Identity Cloud

* PingAM 6.5, 7.0, 7.1, 7.2, 7.3, 7.4, 7.5, 8.0, and later

## Supported operating systems and browsers

The Advanced Identity Cloud/PingAM Login Widget supports the [desktop](#js-desktop-browsers) and [mobile](#js-desktop-browsers) browsers listed below.

**Minimum supported Desktop browser versions**

* Chrome 83

* Firefox 77

* Safari 13

* Microsoft Edge 83 (Chromium)

**Supported Mobile browsers**

* iOS (Safari) - Two most recent major versions of the operating system.

* Android (Chrome) - Two most recent major versions of the operating system.

### JavaScript Compatibility with WebViews

A WebView allows you to embed a web browser into your native Android or iOS application to display HTML pages, and run JavaScript apps.

For example, the Android system WebView is based on the Google Chrome engine, and the iOS WebView is based on the Safari browser engine.

However, it is important to note that WebViews do not implement the full feature set of their respective browsers. For example, some of the browser-provided APIs that the Advanced Identity Cloud/PingAM Login Widget requires are not available in a WebView, such as the WebAuthn APIs.

In addition, there are concerns that a WebView does not provide the same level of security as their full browser counterparts.

As the Advanced Identity Cloud/PingAM Login Widget requires full, spec-compliant, browser-supplied APIs for full functionality we **do not** support usage within a WebView.

We also do not support or test usage with any wrappers around WebViews.

Whilst you might be able to implement simple use-cases using the Advanced Identity Cloud/PingAM Login Widget within a WebView, we recommend that you use an alternative such as opening a full browser, or using an in-app instance of a full browser such as [Custom Tabs](https://developer.android.com/develop/ui/views/layout/webapps/overview-of-android-custom-tabs) for Android or [SFSafariViewController](https://developer.apple.com/documentation/safariservices/sfsafariviewcontroller) for iOS.

## Supported authentication journey callbacks

The Advanced Identity Cloud/PingAM Login Widget support the following authentication journey callbacks when using the following servers:

* PingOne Advanced Identity Cloud

* PingAM

| Callback name                                 | Callback description                                                                                                                                                                                               | Supported? |
| --------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------- |
| `BooleanAttributeInputCallback``SDK 2.1`      | Collects true or false.                                                                                                                                                                                            | ✅          |
| `ChoiceCallback`                              | Collects single user input from available choices, retrieves selected choice from user interaction.                                                                                                                | ✅          |
| `ConfirmationCallback`                        | Retrieve a selected option from a list of options.                                                                                                                                                                 | ✅          |
| `ConsentMappingCallback``SDK 2.0`             | Prompts the user to consent to share their profile data.                                                                                                                                                           | ❌          |
| `DeviceBindingCallback`                       | Cryptographically bind a mobile device to a user account.                                                                                                                                                          | ❌          |
| `DeviceProfileCallback``SDK 2.0`              | Collects meta and/or location data about the authenticating device.                                                                                                                                                | ✅          |
| `DeviceSigningVerifierCallback`               | Verify ownership of a bound device by signing a challenge.                                                                                                                                                         | ❌          |
| `HiddenValueCallback`                         | Returns form values that are not visually rendered to the end user.                                                                                                                                                | ✅          |
| `IdPCallback`                                 | Provides the information required for connecting to an identity provider (IdP) for social sign-on.                                                                                                                 | ✅          |
| `KbaCreateCallback` `SDK 2.0`                 | Collects knowledge-based answers. For example, the name of your first pet.                                                                                                                                         | ✅          |
| `MetadataCallback` [(1)](#webauthn-callback)  | Injects key-value metadata into the authentication process.For example, the [WebAuthn](#webauthn-callback) nodes use this callback to return the data the SDK requires to perform authentication and registration. | ✅          |
| `NameCallback`                                | Collects a username.                                                                                                                                                                                               | ✅          |
| `NumberAttributeInputCallback``SDK 2.1`       | Collects a number.                                                                                                                                                                                                 | ✅          |
| `PasswordCallback`                            | Collects a password or one-time pass code.                                                                                                                                                                         | ✅          |
| `PingOneProtectEvaluationCallback``SDK 4.4`   | Collects captured contextual data from the client to perform risk evaluations.                                                                                                                                     | ✅          |
| `PingOneProtectInitializeCallback``SDK 4.4`   | Instructs the client to start capturing contextual data for risk evaluations                                                                                                                                       | ✅          |
| `PollingWaitCallback`                         | Instructs the client to wait for the given period and resubmit the request.                                                                                                                                        | ✅          |
| `ReCaptchaCallback`                           | Provides data required to use a CAPTCHA in your apps.                                                                                                                                                              | ✅          |
| `ReCaptchaEnterpriseCallback`                 | Provides data required to use reCAPTCHA Enterprise in your apps.                                                                                                                                                   | ✅`SDK 4.6` |
| `RedirectCallback`                            | Redirects the user's browser or user-agent.                                                                                                                                                                        | ✅          |
| `SelectIdPCallback`                           | Provides a list of identity providers (IdPs) users can choose from to perform social sign-on.                                                                                                                      | ✅          |
| `StringAttributeInputCallback``SDK 2.0`       | Collects the values of attributes for use elsewhere in a tree.                                                                                                                                                     | ✅          |
| `SuspendedTextOutputCallback``SDK 2.1`        | Pause and resume authentication, sometimes known as "magic links".                                                                                                                                                 | ✅          |
| `TermsAndConditionsCallback``SDK 2.0`         | Collects a user's acceptance of the configured Terms & Conditions.                                                                                                                                                 | ✅          |
| `TextInputCallback`                           | Collects text input from the end user. For example, a nickname for their account.                                                                                                                                  | ✅`SDK 3.4` |
| `TextOutputCallback`                          | Provides a message to be displayed to a user with a given message type.                                                                                                                                            | ✅          |
| `TextOutputCallback`*(`messageType` === `4`)* | Some nodes use the `TextOutputCallback` callback to include JavaScript that is intended to be run on the client.In this case the `mesageType` property equals `4`.                                                 | ✅          |
| `ValidatedPasswordCallback``SDK 2.0`          | Collects a password value with optional password policy validation.                                                                                                                                                | ✅          |
| `ValidatedUsernameCallback``SDK 2.0`          | Collects a username value with optional username policy validation.                                                                                                                                                | ✅          |

> **Collapse: Show the nodes that might return each callback**
>
> The table below lists the nodes that might return supported callbacks.
>
> The actual callbacks a node returns depends on its configuration. It might not return all the callbacks listed in this table.
>
> | Callback                                | Auth nodes that might return callback                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
> | --------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
> | `BooleanAttributeInputCallback`         | * [Attribute Collector node](https://docs.pingidentity.com/auth-node-ref/latest/attribute-collector.html)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
> | `ChoiceCallback`                        | - [Choice Collector node](https://docs.pingidentity.com/auth-node-ref/latest/choice-collector.html)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
> | `ConfirmationCallback`                  | * [LDAP Decision node](https://docs.pingidentity.com/auth-node-ref/latest/ldap-decision.html)
>
> * [Message node](https://docs.pingidentity.com/auth-node-ref/latest/message.html)
>
> * [MFA Registration Options node](https://docs.pingidentity.com/auth-node-ref/latest/mfa-registration-options.html)
>
> * [OATH Token Verifier node](https://docs.pingidentity.com/auth-node-ref/latest/oath-token-verifier.html)
>
> * [Polling Wait node](https://docs.pingidentity.com/auth-node-ref/latest/polling-wait.html)
>
> * [Push Wait node](https://docs.pingidentity.com/auth-node-ref/latest/push-wait.html)
>
> * [WebAuthn Authentication node](https://docs.pingidentity.com/auth-node-ref/latest/webauthn-authentication.html)
>
> * [OATH Registration node](https://docs.pingidentity.com/auth-node-ref/latest/oath-registration.html) |
> | `ConsentMappingCallback`                | - [Consent Collector node](https://docs.pingidentity.com/auth-node-ref/latest/consent-collector.html)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
> | `DeviceBindingCallback`                 | * [Device Binding node](https://docs.pingidentity.com/auth-node-ref/latest/device-binding.html)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
> | `DeviceProfileCallback`                 | - [Device Profile Collector node](https://docs.pingidentity.com/auth-node-ref/latest/device-profile-collector.html)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
> | `DeviceSigningVerifierCallback`         | * [Device Signing Verifier node](https://docs.pingidentity.com/auth-node-ref/latest/device-signing-verifier.html)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
> | `HiddenValueCallback`                   | - [Amster Jwt Decision node](https://docs.pingidentity.com/auth-node-ref/latest/am-only/amster-jwt-decision.html)
>
> - [Push Wait node](https://docs.pingidentity.com/auth-node-ref/latest/push-wait.html)
>
> - [WebAuthn Authentication node](https://docs.pingidentity.com/auth-node-ref/latest/webauthn-authentication.html)
>
> - [WebAuthn Registration node](https://docs.pingidentity.com/auth-node-ref/latest/webauthn-registration.html)                                                                                                                                                                                                                                                                                                                                                                                     |
> | `IdPCallback`                           | * [Social Provider Handler node](https://docs.pingidentity.com/auth-node-ref/latest/social-provider-handler.html)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
> | `KbaCreateCallback`                     | - [KBA Definition node](https://docs.pingidentity.com/auth-node-ref/latest/kba-definition.html)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
> | `MetaDataCallback`                      | * [WebAuthn Authentication node](https://docs.pingidentity.com/auth-node-ref/latest/webauthn-authentication.html)
>
> * [WebAuthn Registration node](https://docs.pingidentity.com/auth-node-ref/latest/webauthn-registration.html)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
> | `NameCallback`                          | - [Username Collector node](https://docs.pingidentity.com/auth-node-ref/latest/am-only/username-collector.html)
>
> - [Datastore Decision node](https://docs.pingidentity.com/auth-node-ref/latest/data-store-decision.html)
>
> - [OATH Token Verifier node](https://docs.pingidentity.com/auth-node-ref/latest/oath-token-verifier.html)
>
> - [Platform Username node](https://docs.pingidentity.com/auth-node-ref/latest/platform-username.html)
>
> - [Configuration Provider node](https://docs.pingidentity.com/auth-node-ref/latest/config-provider.html)                                                                                                                                                                                                                                                                          |
> | `NumberAttributeInputCallback`          | * [Attribute Collector node](https://docs.pingidentity.com/auth-node-ref/latest/attribute-collector.html)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
> | `PasswordCallback`                      | - [Create Password node](https://docs.pingidentity.com/auth-node-ref/latest/am-only/create-password.html)
>
> - [Password Collector node](https://docs.pingidentity.com/auth-node-ref/latest/am-only/password-collector.html)
>
> - [Datastore Decision node](https://docs.pingidentity.com/auth-node-ref/latest/data-store-decision.html)
>
> - [KBA Verification node](https://docs.pingidentity.com/auth-node-ref/latest/kba-verification.html)
>
> - [LDAP Decision node](https://docs.pingidentity.com/auth-node-ref/latest/ldap-decision.html)
>
> - [One-time Password Collector Decision node](https://docs.pingidentity.com/auth-node-ref/latest/otp-collector-decision.html)
>
> - [Platform Password node](https://docs.pingidentity.com/auth-node-ref/latest/platform-password.html)                                                 |
> | `PingOneProtectEvaluationCallback`      | * [PingOne Protect Evaluation node](https://docs.pingidentity.com/auth-node-ref/latest/pingone/pingone-protect-evaluation.html)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
> | `PingOneProtectInitializeCallback`      | - [PingOne Protect Initialization node](https://docs.pingidentity.com/auth-node-ref/latest/pingone/pingone-protect-initialize.html)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
> | `PollingWaitCallback`                   | * [Combined MFA Registration node](https://docs.pingidentity.com/auth-node-ref/latest/combined-mfa-registration.html)
>
> * [Push Registration node](https://docs.pingidentity.com/auth-node-ref/latest/push-registration.html)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
> | `ReCaptchaCallback`                     | - [CAPTCHA node](https://docs.pingidentity.com/auth-node-ref/latest/captcha.html)
>
> - [Legacy CAPTCHA node (deprecated)](https://docs.pingidentity.com/auth-node-ref/latest/legacy-captcha.html)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
> | `ReCaptchaEnterpriseCallback`           | * [reCAPTCHA Enterprise node](https://docs.pingidentity.com/auth-node-ref/latest/recaptcha-enterprise.html)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
> | `RedirectCallback`                      | - [Provision IDM Account node](https://docs.pingidentity.com/auth-node-ref/latest/am-only/provision-IDM-account.html)
>
> - [Identity Assertion node](https://docs.pingidentity.com/auth-node-ref/latest/identity-assertion-node.html)
>
> - [Social Provider Handler node](https://docs.pingidentity.com/auth-node-ref/latest/social-provider-handler.html)                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
> | `SelectIdPCallback`                     | * [Select Identity Provider node](https://docs.pingidentity.com/auth-node-ref/latest/select-identity-provider.html)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
> | `StringAttributeInputCallback`          | - [Attribute Collector node](https://docs.pingidentity.com/auth-node-ref/latest/attribute-collector.html)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
> | `SuspendedTextOutputCallback`           | * [Email Suspend node](https://docs.pingidentity.com/auth-node-ref/latest/email-suspend.html)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
> | `TermsAndConditionsCallback`            | - [Accept Terms and Conditions node](https://docs.pingidentity.com/auth-node-ref/latest/accept-terms-and-conditions.html)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
> | `TextInputCallback`                     | * [Configuration Provider node](https://docs.pingidentity.com/auth-node-ref/latest/config-provider.html)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
> | `TextOutputCallback`                    | - [Create Password node](https://docs.pingidentity.com/auth-node-ref/latest/am-only/create-password.html)
>
> - [Display Username node](https://docs.pingidentity.com/auth-node-ref/latest/display-username.html)
>
> - [LDAP Decision node](https://docs.pingidentity.com/auth-node-ref/latest/ldap-decision.html)
>
> - [Message node](https://docs.pingidentity.com/auth-node-ref/latest/message.html)
>
> - [MFA Registration Options node](https://docs.pingidentity.com/auth-node-ref/latest/mfa-registration-options.html)                                                                                                                                                                                                                                                                                                          |
> | `TextOutputCallback (messageType == 4)` | * [WebAuthn Authentication node](https://docs.pingidentity.com/auth-node-ref/latest/webauthn-authentication.html)
>
> * [WebAuthn Registration node](https://docs.pingidentity.com/auth-node-ref/latest/webauthn-registration.html)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
> | `ValidatedPasswordCallback`             | - [Platform Password node](https://docs.pingidentity.com/auth-node-ref/latest/platform-password.html)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
> | `ValidatedUsernameCallback`             | * [Platform Username node](https://docs.pingidentity.com/auth-node-ref/latest/platform-username.html)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |

> **Collapse: Show the callbacks each node might return**
>
> The table below lists the supported callbacks that a node might return.
>
> The actual callbacks a node returns depends on its configuration. It might not return all the callbacks listed in this table.
>
> |                                                                                                                                   |                                                                                                      |
> | --------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
> | Auth node                                                                                                                         | Callbacks the node might return                                                                      |
> | [Accept Terms and Conditions node](https://docs.pingidentity.com/auth-node-ref/latest/accept-terms-and-conditions.html)           | `TermsAndConditionsCallback`                                                                         |
> | [Amster Jwt Decision node](https://docs.pingidentity.com/auth-node-ref/latest/am-only/amster-jwt-decision.html)                   | `HiddenValueCallback`                                                                                |
> | [Attribute Collector node](https://docs.pingidentity.com/auth-node-ref/latest/attribute-collector.html)                           | `BooleanAttributeInputCallback``NumberAttributeInputCallback``StringAttributeInputCallback`          |
> | [CAPTCHA node](https://docs.pingidentity.com/auth-node-ref/latest/captcha.html)                                                   | `ReCaptchaCallback`                                                                                  |
> | [Choice Collector node](https://docs.pingidentity.com/auth-node-ref/latest/choice-collector.html)                                 | `ChoiceCallback`                                                                                     |
> | [Combined MFA Registration node](https://docs.pingidentity.com/auth-node-ref/latest/combined-mfa-registration.html)               | `PollingWaitCallback`                                                                                |
> | [Configuration Provider node](https://docs.pingidentity.com/auth-node-ref/latest/config-provider.html)                            | `NameCallback``TextInputCallback`                                                                    |
> | [Consent Collector node](https://docs.pingidentity.com/auth-node-ref/latest/consent-collector.html)                               | `ConsentMappingCallback`                                                                             |
> | [Create Password node](https://docs.pingidentity.com/auth-node-ref/latest/am-only/create-password.html)                           | `PasswordCallback``TextOutputCallback`                                                               |
> | [Datastore Decision node](https://docs.pingidentity.com/auth-node-ref/latest/data-store-decision.html)                            | `NameCallback``PasswordCallback`                                                                     |
> | [Device Binding node](https://docs.pingidentity.com/auth-node-ref/latest/device-binding.html)                                     | `DeviceBindingCallback`                                                                              |
> | [Device Profile Collector node](https://docs.pingidentity.com/auth-node-ref/latest/device-profile-collector.html)                 | `DeviceProfileCallback`                                                                              |
> | [Device Signing Verifier node](https://docs.pingidentity.com/auth-node-ref/latest/device-signing-verifier.html)                   | `DeviceSigningVerifierCallback`                                                                      |
> | [Display Username node](https://docs.pingidentity.com/auth-node-ref/latest/display-username.html)                                 | `TextOutputCallback`                                                                                 |
> | [Email Suspend node](https://docs.pingidentity.com/auth-node-ref/latest/email-suspend.html)                                       | `SuspendedTextOutputCallback`                                                                        |
> | [Identity Assertion node](https://docs.pingidentity.com/auth-node-ref/latest/identity-assertion-node.html)                        | `RedirectCallback`                                                                                   |
> | [KBA Definition node](https://docs.pingidentity.com/auth-node-ref/latest/kba-definition.html)                                     | `KbaCreateCallback`                                                                                  |
> | [KBA Verification node](https://docs.pingidentity.com/auth-node-ref/latest/kba-verification.html)                                 | `PasswordCallback`                                                                                   |
> | [LDAP Decision node](https://docs.pingidentity.com/auth-node-ref/latest/ldap-decision.html)                                       | `ConfirmationCallback``PasswordCallback``TextOutputCallback`                                         |
> | [Legacy CAPTCHA node (deprecated)](https://docs.pingidentity.com/auth-node-ref/latest/legacy-captcha.html)                        | `ReCaptchaCallback`                                                                                  |
> | [Message node](https://docs.pingidentity.com/auth-node-ref/latest/message.html)                                                   | `ConfirmationCallback``TextOutputCallback`                                                           |
> | [MFA Registration Options node](https://docs.pingidentity.com/auth-node-ref/latest/mfa-registration-options.html)                 | `ConfirmationCallback``TextOutputCallback`                                                           |
> | [OATH Registration node](https://docs.pingidentity.com/auth-node-ref/latest/oath-registration.html)                               | `ConfirmationCallback`                                                                               |
> | [OATH Token Verifier node](https://docs.pingidentity.com/auth-node-ref/latest/oath-token-verifier.html)                           | `ConfirmationCallback``NameCallback`                                                                 |
> | [One-time Password Collector Decision node](https://docs.pingidentity.com/auth-node-ref/latest/otp-collector-decision.html)       | `PasswordCallback`                                                                                   |
> | [Password Collector node](https://docs.pingidentity.com/auth-node-ref/latest/am-only/password-collector.html)                     | `PasswordCallback`                                                                                   |
> | [PingOne Protect Evaluation node](https://docs.pingidentity.com/auth-node-ref/latest/pingone/pingone-protect-evaluation.html)     | `PingOneProtectEvaluationCallback`                                                                   |
> | [PingOne Protect Initialization node](https://docs.pingidentity.com/auth-node-ref/latest/pingone/pingone-protect-initialize.html) | `PingOneProtectInitializeCallback`                                                                   |
> | [Platform Password node](https://docs.pingidentity.com/auth-node-ref/latest/platform-password.html)                               | `PasswordCallback``ValidatedPasswordCallback`                                                        |
> | [Platform Username node](https://docs.pingidentity.com/auth-node-ref/latest/platform-username.html)                               | `NameCallback``ValidatedUsernameCallback`                                                            |
> | [Polling Wait node](https://docs.pingidentity.com/auth-node-ref/latest/polling-wait.html)                                         | `ConfirmationCallback`                                                                               |
> | [Provision IDM Account node](https://docs.pingidentity.com/auth-node-ref/latest/am-only/provision-IDM-account.html)               | `RedirectCallback`                                                                                   |
> | [Push Registration node](https://docs.pingidentity.com/auth-node-ref/latest/push-registration.html)                               | `PollingWaitCallback`                                                                                |
> | [Push Wait node](https://docs.pingidentity.com/auth-node-ref/latest/push-wait.html)                                               | `ConfirmationCallback``HiddenValueCallback`                                                          |
> | [reCAPTCHA Enterprise node](https://docs.pingidentity.com/auth-node-ref/latest/recaptcha-enterprise.html)                         | `ReCaptchaEnterpriseCallback`                                                                        |
> | [Select Identity Provider node](https://docs.pingidentity.com/auth-node-ref/latest/select-identity-provider.html)                 | `SelectIdPCallback`                                                                                  |
> | [Social Provider Handler node](https://docs.pingidentity.com/auth-node-ref/latest/social-provider-handler.html)                   | `IdPCallback``RedirectCallback`                                                                      |
> | [Username Collector node](https://docs.pingidentity.com/auth-node-ref/latest/am-only/username-collector.html)                     | `NameCallback`                                                                                       |
> | [WebAuthn Authentication node](https://docs.pingidentity.com/auth-node-ref/latest/webauthn-authentication.html)                   | `ConfirmationCallback``HiddenValueCallback``MetaDataCallback``TextOutputCallback (messageType == 4)` |
> | [WebAuthn Registration node](https://docs.pingidentity.com/auth-node-ref/latest/webauthn-registration.html)                       | `HiddenValueCallback``MetaDataCallback``TextOutputCallback (messageType == 4)`                       |

(1) The [WebAuthn Authentication node](https://docs.pingidentity.com/auth-node-ref/latest/webauthn-authentication.html) and the [WebAuthn Registration node](https://docs.pingidentity.com/auth-node-ref/latest/webauthn-registration.html) both use a `MetaDataCallback` when the Return challenge as JavaScript is *NOT* enabled.

The Advanced Identity Cloud/PingAM Login Widget handles either the `MetaDataCallback` or the JavaScript-based payload.
