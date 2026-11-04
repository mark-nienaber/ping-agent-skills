---
title: Deprecated
description: Deprecated. Track functionality deprecated in the Orchestration SDKs and likely to be removed in a future release
component: orchsdks
page_id: orchsdks:release-notes:deprecations/deprecations
canonical_url: https://developer.pingidentity.com/orchsdks/release-notes/deprecations/deprecations.html
llms_txt: https://developer.pingidentity.com/orchsdks/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: Thu, 25 May 2023 13:44:17 +0100
section_ids:
  dep-JS400: Deprecated since Orchestration SDK for JavaScript 4.0
---

# Deprecated

The functionality listed here is deprecated, and likely to be removed in a future release.

## Deprecated since Orchestration SDK for JavaScript 4.0

* JavaScript `support` configuration property

  The `support` configuration property has been removed in Orchestration SDK for JavaScript 4.0.

  This property could be used to change the way the SDK would make requests to the `/authorize` endpoint in OAuth 2.0 interactions.

  If you configured the SDK to use the `modern` option, you might notice that your app uses the default iframe method to call the `/authorize` endpoint if you upgrade to this version of the SDK. This technical difference will not negatively impact your app's user-experience or require any code changes.

  If you were using the `legacy` option or not providing a value for the `support` property at all, you will likely obtain improvements in latency and a reduction of errors in the logs when upgrading to Orchestration SDK for JavaScript 4.0.

---

---
title: Developer Experience changelog
description: Track the latest releases for the Ping orchestration SDKs across Android, iOS, and JavaScript platforms
component: orchsdks
page_id: orchsdks:release-notes:changelogs/developer_experience_changelog_rss
canonical_url: https://developer.pingidentity.com/orchsdks/release-notes/changelogs/developer_experience_changelog_rss.html
llms_txt: https://developer.pingidentity.com/orchsdks/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  latest_releases: Latest Releases
  unified_ios_2_2_0: Orchestration SDK for iOS 2.2.0
  key_features: Key features
  added: Added
  updated: Updated
  breaking_changes: Breaking changes
  changed: Changed
  fixed: Fixed
  unified_react_native_1_1_0: Orchestration SDK for React Native 1.1.0
  key_features_2: Key features
  unified_android_2_2_0: Orchestration SDK for Android 2.2.0
  key_features_3: Key features
  added_2: Added
  changed_2: Changed
  fixed_2: Fixed
  unified_javascript_2_3_0: Orchestration SDK for JavaScript 2.3.0
  key_features_4: Key features
  enhancements: Enhancements
  unified_javascript_2_2_0: Orchestration SDK for JavaScript 2.2.0
  enhancements_2: Enhancements
  breaking_changes_2: Breaking Changes
  changes: Changes
  unified_ios_2_1_1: Orchestration SDK for iOS 2.1.1
  updated_2: Updated
  unified_javascript_2_1_1: Orchestration SDK for JavaScript 2.1.1
  fixes: Fixes
  unified_ios_2_1_0: Orchestration SDK for iOS 2.1.0
  key_features_5: Key features
  enhancements_3: Enhancements
  fixes_2: Fixes
  unified_javascript_2_1_0: Orchestration SDK for JavaScript 2.1.0
  key_features_6: Key features
  added_3: Added
  updated_3: Updated
  fixed_3: Fixed
  unified_android_2_1_0: Orchestration SDK for Android 2.1.0
  key_features_7: Key features
  enhancements_4: Enhancements
  fixes_3: Fixes
  unified_react_native_1_0_0: Orchestration SDK for React Native 1.0.0
  key_features_8: Key features
  unified_android_2_0_1: Orchestration SDK for Android 2.0.1
  fixes_4: Fixes
  unified_android_2_0_0: Orchestration SDK for Android 2.0.0
  key_features_9: Key features
  enhancements_5: Enhancements
  unified_ios_2_0_0: Orchestration SDK for iOS 2.0.0
  key_features_10: Key features
  enhancements_6: Enhancements
  fixes_5: Fixes
  unified_javascript_2_0_0: Orchestration SDK for JavaScript 2.0.0
  key_features_11: Key features
  enhancements_7: Enhancements
  fixes_6: Fixes
---

# Developer Experience changelog

Subscribe to get automatic updates:

* [icon: rss-square, set=fa][Orchestration SDKs Changelog RSS feed](developer_experience_changelog_rss.xml)

* [icon: square-envelope, set=fa][Orchestration SDKs Changelog email notifications](https://backstage.forgerock.com/account/notifications/settings)

## Latest Releases

### Orchestration SDK for iOS 2.2.0

**October 20, 2026**

#### Key features

* **PingOne Recognize**

  A new `recognize` module provides privacy-preserving facial biometrics for enrollment and sign-in in authentication journeys.

  Learn more in [Integrating PingOne Recognize](../../journey/use-cases/recognize/index.html).

* Facebook Limited Login

  Sign in to Facebook using the OIDC ID-token flow instead of the classic access-token login.

  In PingOne Advanced Identity Cloud and PingAM journeys, configure an OIDC Social Identity Provider with a name containing `fb-limited` to opt in; existing provider names such as `facebook` continue to use classic access-token login.

  In DaVinci Custom HTML and PingOne Forms, set the new `facebookLimitedLoginEnabled` property on the Facebook collector to choose between the classic `accessToken` and Limited Login `idToken` payloads.

  Learn more in [Authenticating with external identity providers on iOS](../../journey/use-cases/external-idp/ios/index.html).

#### Added

* Added a new `pingonemfa` module for PingOne MFA integration, with DaVinci `MobilePairingCollector` support for pairing PingOne MFA accounts directly within a DaVinci flow.

* Added `ImageCollector` to support image display in DaVinci forms. \[SDKS-5143]

* Added `MetadataCollector` to support the DaVinci SDK Integrator connector's pause/resume model, so the app can invoke on-device SDKs and return a result or error before the flow continues. \[SDKS-5142]

* Added `trigger` and `isAutomatic` properties to the DaVinci FIDO collectors. \[SDKS-4552]

* Added a present-only launch mode to `BrowserLauncher` through `browserMode: .custom`.

  `launch()` resolves as soon as the browser UI is presented, without waiting for a callback. Use this for use cases such as session handoff or in-app SSO, where no redirect back to the app is expected. \[SDKS-5357]

* Added `OidcError.configurationError` to report a configuration that has neither a usable `discoveryEndpoint` nor a pre-supplied `openId` object. \[SDKS-5301]

* Added opt-in commercial device-model-name resolution to `DeviceProfileCallback` through `PlatformCollector(includeModelName: true)`; the default `PlatformCollector()` payload is unchanged. \[SDKS-5275]

#### Updated

* Redesigned the PingExample sample app with a shared design system. \[SDKS-5054]

* Updated the Facebook iOS SDK dependency to 18.1.0. \[SDKS-5160]

* The `oidc.discoveryEndpoint` property in unified JSON configuration is now required only when no `oidc.openId` sub-object is supplied.

  An `openId` block without `discoveryEndpoint` replaces the discovery document and requires `tokenEndpoint`. \[SDKS-5301]

* Restored `OidcClientConfig.openId` as a publicly settable property, and `oidcInitialize()` now skips OpenID discovery when it is pre-supplied, restoring the 2.0.0 no-discovery configuration path. \[SDKS-5301]

#### Breaking changes

* `PingJourney` no longer has a hard dependency on `PingDeviceProfile`. \[SDKS-5443]

  Previously, every `PingJourney` consumer's binary transitively linked `PingDeviceProfile`, whose `BluetoothCollector` instantiates `CBCentralManager`, causing App Store Connect to flag the app for a missing `NSBluetoothAlwaysUsageDescription` even when no `DeviceProfileCallback` node was used.

  If your journeys use the Device Profile Collector node, add the `PingDeviceProfile` product or pod explicitly to your own `Package.swift` or `Podfile`.

* `OidcError` has a new `configurationError` case, so exhaustive `switch` statements over `OidcError` need a new branch. \[SDKS-5301]

#### Changed

* A JSON configuration with a blank `oidc.discoveryEndpoint` and no `oidc.openId` sub-object now fails at parse time instead of at first use. \[SDKS-5301]

* `OidcClientConfig.oidcInitialize()` cancellation is now isolated per caller: cancelling one caller's own task still returns promptly with `CancellationError`, but no longer cancels the shared discovery operation for any other caller currently sharing it. \[SDKS-5301]

* `CallbackRegistry.callback(from:)` now logs a debug message when a journey response contains a callback type with no registered handler, such as a `DeviceProfileCallback` in an app that did not add the `PingDeviceProfile` module, making the missing-module misconfiguration diagnosable instead of silently dropping the callback. \[SDKS-5443]

* `SubmitCollector`, `FlowCollector`, and `MetadataCollector` now expose `actionKey` through the new `ActionKeyProvider` protocol. \[SDKS-5290]

#### Fixed

* Fixed DaVinci FIDO registration and authentication not launching automatically when the form's `trigger` property is not `BUTTON`. \[SDKS-4552]

* Fixed FIDO2 client-side WebAuthn errors (cancellation, timeout, and similar) not routing to the DaVinci error branch. \[SDKS-4478]

* Fixed `QRCodeCollector` not preserving the complete QR code data URI in `content`. \[SDKS-5299]

* Fixed `OidcWebClient` `.authSession` and `.ephemeralAuthSession` not completing for Universal Link (https) redirect URIs. \[SDKS-5239]

* Fixed `OidcWebClient.authorize()` collapsing `FailureNode.cause` to `.unknown`, losing typed browser-cancellation and unsupported-OS error identity. \[SDKS-5295]

* Fixed 5xx PingAM responses with a parseable error body being misclassified as `FailureNode` instead of `ErrorNode`, diverging from Android. \[SDKS-5358]

* Fixed `Journey.start(backchannelUri:)` not rejecting whitespace-only `authIndexType` and `authIndexValue`, diverging from Android. \[SDKS-5359]

* Fixed the asynchronous `OidcClient.generateAuthorizeUrl(customParams:)` silently falling back to the standard (non-PAR) flow when called before `OidcClientConfig.oidcInitialize()`, which could emit `additionalParameters` onto the returned URL instead of the PAR POST body. The synchronous overload never supported PAR and is unaffected. \[SDKS-5403]

* Fixed `swift build` (macOS) failing in `PingOidc`: `OidcDeviceClient.authorize(verificationUriComplete:)` now throws `BrowserError.httpsCallbackUnsupportedOS` on non-iOS platforms instead of referencing the iOS-only `BrowserLauncher` type, and the `PingOneMFA` target's `PingOneSDK` dependency is iOS-conditioned. \[SDKS-5443]

### Orchestration SDK for React Native 1.1.0

**October 8, 2026**

#### Key features

* **DaVinci module for React Native.**

  The first public release of the `@ping-identity/rn-davinci` module lets your React Native app run DaVinci flows end to end, with form rendering and submission.

  Learn more in [Using the DaVinci module for React Native](../../davinci/usage/react-native/index.html).

* **PingOne Protect fraud prevention in DaVinci flows.**

  The new `@ping-identity/rn-protect` module collects behavioral data and sends Protect signals during DaVinci flows, so your React Native app can assess fraud risk.

  Learn more in [Getting started with PingOne Protect on React Native](../../davinci/use-cases/protect/react-native/index.html).

* **External IdP (social sign-on) collectors in DaVinci flows.**

  Authenticate with external identity providers such as Apple, Google, and Facebook directly from DaVinci flows in your React Native app.

  Learn more in [Configure a React Native app for social sign-on](../../davinci/use-cases/external-idp/react-native/index.html).

* **FIDO and passkeys in DaVinci flows.**

  Register and authenticate passkeys in DaVinci flows with the new `FidoRegistrationCollector` and `FidoAuthenticationCollector`.

  Learn more in [Getting started with FIDO on React Native](../../davinci/use-cases/fido/react-native/index.html).

* **Device Authorization Grant in OIDC sign-on.**

  Sign in on devices with limited input, such as smart TVs or set-top boxes, using the new `createOidcDeviceClient` and `useDeviceAuthGrant` APIs.

  Learn more in [Authenticating devices with the Device Authorization Grant](../../oidc/use-cases/device-authorization-grant/index.html).

* **Pushed Authorization Request (PAR) in OIDC sign-on.**

  Send OAuth 2.0 authorization parameters directly to the server before the redirect begins, keeping them out of the browser URL, through the new `par` client config option.

  Learn more in [Securing OIDC sign-on with Pushed Authorization Requests](../../oidc/use-cases/par/index.html).

**Added**

* Added DaVinci `BooleanCollector` and `ReadOnlyTextCollector` support, plus auto-submit for collectors flagged auto-capable by the flow.

* Added DaVinci polling and QRCode collectors so flows can wait on out-of-band status and display QR codes.

* Added DaVinci phone number collector support for phone extension fields (`extension`, `showExtension`, `extensionLabel`).

* Added DaVinci label collector support for `richContent`.

* Added DaVinci password collector support for server-provided validation rules, structured password-policy validation errors (`INVALID_LENGTH`, `UNIQUE_CHARACTER`, `MAX_REPEAT`, `MIN_CHARACTERS`) with native constraint values, and a `validate` method for on-demand collector validation.

**Updated**

* Improved the `useJourneyForm` hook with typed, normalized form fields for simpler Journey callback handling in `@ping-identity/rn-journey`.

* Updated Journey `ContinueNode` to expose UI metadata, such as page header, description, submit button text, and page footer details.

* Improved Expo compatibility with config plugin ownership.

* Updated OATH typed errors to carry violated policy details, so callers can react without parsing message strings.

**Fixed**

* `SOCIAL_LOGIN_BUTTON` no longer reported in unsupported fields when an IdP collector is present in `@ping-identity/rn-davinci`.

### Orchestration SDK for Android 2.2.0

**September 25, 2026**

#### Key features

* **PingOne Recognize**

  A new `recognize` module provides privacy-preserving facial biometrics for enrollment and sign-in in authentication journeys.

  Learn more in [Integrating PingOne Recognize](../../journey/use-cases/recognize/index.html).

* **Backchannel authentication** \[SDKS-5157]

  The Orchestration SDK now supports transactional backchannel authentication in authentication journeys, so a third party can initiate a sign-in or transaction on behalf of your user, and your app completes it after the user approves it on their device.

  |   |                                                                                                                                                                                                                                                                       |
  | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | This is not OIDC Client-Initiated Backchannel Authentication (CIBA).This feature uses a proprietary backchannel authentication mechanism in Advanced Identity Cloud and PingAM; a transactional authentication pattern that is unrelated to the OIDC CIBA grant type. |

  Learn more in [Backchannel authentication](../../journey/use-cases/backchannel-auth/index.html).

#### Added

* Added a new `pingonemfa` module for PingOne MFA integration, with DaVinci `MobilePairingCollector` support for pairing PingOne MFA accounts directly within a DaVinci flow.

* Added `MetadataCollector` for DaVinci flows to support exchanging custom SDK metadata. \[SDKS-5168]

* Added `ImageCollector` for DaVinci forms to display images. \[SDKS-5169]

* Added an optional HTTP status code to `ErrorNode`. \[SDKS-5202]

#### Changed

* Changed FIDO2 authentication to support per-request API selection with `useFido2ApiClient`. \[SDKS-5411]

#### Fixed

* Fixed the browser redirect URI scheme manifest placeholder to apply only to debug builds, allowing release consumers to provide their own value. \[SDKS-5296]

* Fixed Journey `submitButtonText`/`pageFooter` to resolve against the device's ordered preferred-locale list. \[SDKS-5310]

* Fixed OIDC `refresh()` to no longer delete the cached token from storage or revoke a non-expired access token before refreshing. \[SDKS-5414]

* Fixed OAuth 2.0 Device Authorization Grant polling to retry on transient network and transport failures instead of terminating the flow. \[SDKS-5124]

* Fixed `AbstractValidatedCallback` throwing when PingAM returns an empty `policies` array instead of an object. \[SDKS-5260]

* Fixed `QRCodeCollector.id()` to return a stable key from the collector configuration instead of a random value. \[SDKS-5293]

* Fixed FIDO2 collectors to report WebAuthn and credential errors as actionable events instead of generic submit failures. \[SDKS-4477]

* Fixed Journey FIDO2 passkey registration crashes on API 33. \[SDKS-5411]

* Fixed Jackson dependency versions to address security vulnerabilities (CVE-2026-54512, CVE-2026-54513, CVE-2026-54514, CVE-2026-54515). \[SDKS-5199]

* Fixed missing blank-secret validation on `OathCredential`, and `OathType` now serializes as lowercase.

### Orchestration SDK for JavaScript 2.3.0

**September 25, 2026**

#### Key features

* **PingOne Recognize**

  The Journey client now supports PingOne Recognize enrollment and authentication callbacks, providing privacy-preserving facial biometrics for enrollment and sign-in in authentication journeys.

  Learn more in [Integrating PingOne Recognize](../../journey/use-cases/recognize/javascript/index.html).

#### Enhancements

* Enhanced `WebAuthn.isConditionalMediationSupported` to now accept an optional journey step. In addition to checking browser support, the method now also reports whether the server requested conditional mediation for that step, so the result reflects the journey's configuration.

* Custom storage configuration types are now exported from the OIDC client, so you can write strongly typed custom storage implementations in TypeScript.

### Orchestration SDK for JavaScript 2.2.0

**September 16, 2026**

#### Enhancements

* Added `MetadataCollector` support for DaVinci flows to support exchanging custom SDK metadata.

* Added JSON client config helper re-exports from the respective client packages, so a single import can build a client configuration from the unified JSON config.

* Added `create-journey-step` export so a Journey step is easy to deserialize after it has been serialized.

#### Breaking Changes

* Changed the device client `tokenStore` configuration to accept a `CustomStorageObject` instead of the legacy `TokenStoreObject`.

  This is a breaking change for custom token-store implementations. Learn more in [Incompatible changes](../breaking/breaking-changes.html#JSUNIFIED220).

#### Changes

* Changed FIDO/WebAuthn `DOMException` handling in DaVinci flows to catch errors and send them to DaVinci instead of failing generically.

* Removed the `@forgerock/javascript-sdk` dependency from `device-client`.

* Fixed the HTTP header to send `ping-sdk` instead of `forgerock-sdk`.

### Orchestration SDK for iOS 2.1.1

**September 4, 2026**

#### Updated

* Updated RecaptchaEnterprise dependency to 18.9.1 for Xcode 27 and iOS 27 compatibility. \[SDKS-5306]

### Orchestration SDK for JavaScript 2.1.1

**August 10, 2026**

#### Fixes

* Fixed the OIDC client to always include `prompt=none` on background authorization calls, for both standard and PAR flows.

### Orchestration SDK for iOS 2.1.0

**July 22, 2026**

#### Key features

* **Pushed Authorization Requests (PAR)** \[SDKS-4235]

  PAR sends OAuth 2.0 authorization parameters directly to the server before the redirect begins, keeping them out of the browser URL and reducing the chance of them being tampered with or exposed in logs or referrer headers.

  Learn more in [Configuring iOS apps for Pushed Authorization Requests](../../oidc/use-cases/par/ios.html).

* **OAuth 2.0 Device Authorization Grant** \[SDKS-4785]

  The Device Authorization Grant is designed for devices with no browser or keyboard, such as smart TVs or set-top boxes. Users authenticate on a secondary device like a phone, and the primary device receives a token once sign-in completes.

  Learn more in [Configuring iOS apps for the Device Authorization Grant](../../oidc/use-cases/device-authorization-grant/ios.html).

* **Standardized JSON configuration** \[SDKS-5066]

  All SDK modules now support a shared JSON object or file for configuration. This makes it straightforward to manage settings across environments and to share a single configuration file across Android, iOS, and JavaScript.

  Learn more in:

  * [Using common JSON configuration for the iOS DaVinci module](../../davinci/usage/ios/02-configuring-the-davinci-module.html#common-json-configuration)

  * [Using common JSON configuration for the iOS Journey module](../../journey/usage/ios/03-configuring-the-journey-module.html#common-json-configuration)

  * [Using common JSON configuration for the iOS OIDC module](../../oidc/usage/ios-centralized-login.html#ios_oidc_common_json_configuration)

#### Enhancements

* Added `PollingCollector` for DaVinci flows. \[SDKS-4682]

* Added `QRCodeCollector` for DaVinci flows. \[SDKS-4680]

* Added `BooleanCollector` to support Checkbox and Switch input types in DaVinci forms. \[SDKS-4920]

* Added `ReadOnlyTextCollector` for DaVinci forms. \[SDKS-4928]

* Added rich text and embedded link support to `LabelCollector` through new `RichContent` and `RichContentReplacement` types. \[SDKS-4245]

* Added support for phone number extensions in `PhoneNumberCollector`. \[SDKS-4668]

* Added `PushError.pushNumberChallengeError` to surface a distinct failure for Push Number Challenge responses. \[SDKS-5115]

* Added `preferImmediatelyAvailableCredentials` option to FIDO authentication to restrict the ceremony to locally-available credentials only, if they exist. \[SDKS-5212]

* Added `AuthMigration` module for migrating existing sessions from the legacy ForgeRock SDK. \[SDKS-4773]

* Added Page Node description, header, and footer support. \[SDKS-4762]

#### Fixes

* Fixed permanent authentication failure after iCloud device migration caused by a Secure Enclave key mismatch. \[SDKS-5172]

* Fixed `PingFido` WebAuthn registration ignoring the configured `displayName` during passkey creation. \[SDKS-5211]

* Fixed `PasswordCollector` not handling nested password policies. \[SDKS-4695]

* Fixed PIN verification during device binding registration. \[SDKS-5015]

* Fixed `Protect` collector being triggered multiple times within a flow. \[SDKS-4769]

* Fixed browser close and reset logic. \[SDKS-4717]

* Fixed device binding authenticators incorrectly reporting as supported on the simulator. \[SDKS-4836]

* Fixed `DeviceBindingConfig` device name defaulting to the user-assigned name instead of the device model. \[SDKS-4850]

* Fixed `DefaultDeviceIdentifier` to reuse the legacy device identifier when available. \[SDKS-4630]

* Fixed Swift build failures caused by a platform bump and missing `canImport` guards. \[SDKS-4916]

* Fixed FIDO ceremony logs not routing through the workflow logger. \[SDKS-4924]

### Orchestration SDK for JavaScript 2.1.0

**July 8, 2026**

#### Key features

* **Pushed Authorization Requests (PAR)**

  PAR sends OAuth 2.0 authorization parameters directly to the server before the redirect begins, keeping them out of the browser URL and reducing the chance of them being tampered with or exposed in logs or referrer headers.

  Learn more in [Configuring JavaScript apps for Pushed Authorization Requests](../../oidc/use-cases/par/javascript.html).

* **Standardized JSON configuration**

  All SDK modules now support a shared JSON object or file for configuration. This makes it straightforward to manage settings across environments and to share a single configuration file across Android, iOS, and JavaScript.

  Learn more in:

  * [Using common JSON configuration for the JavaScript DaVinci module](../../davinci/usage/javascript/02-configuring-the-davinci-module.html#common-json-configuration)

  * [Using common JSON configuration for the JavaScript Journey module](../../journey/usage/javascript/03-configuring-the-journey-module.html#common-json-configuration)

  * [Using common JSON configuration for the JavaScript OIDC module](../../oidc/usage/javascript-centralized-login.html#javascript_oidc_common_json_configuration)

#### Added

* Added `PollingCollector` for DaVinci flows.

* Added `QrCodeCollector` for DaVinci flows.

* Added `BooleanCollector` and `ValidatedBooleanCollector` to support Checkbox input types in DaVinci forms.

* Added `PhoneNumberExtensionCollector` for phone number fields that include an extension.

* Added `ValidatedPasswordCollector` for password fields with embedded policy validation.

* Added `ImageCollector` for `IMAGE` form fields in DaVinci forms.

* Added `subscribe` method to journey and OIDC client instances.

* Added WebAuthn conditional mediation (passkey autofill) support.

* Added `user.session()` method for silent OIDC session verification (`prompt=none`).

#### Updated

* Updated rich-text support of the `ReadOnlyCollector` to handle links in Translatable Rich Text (Forms).

#### Fixed

* Fixed RTK Query cache lookups in `cache.getLatestResponse()` and `cache.getResponseWithId()`.

* Fixed `resume()` to correctly forward redirect query parameters from the authorization response.

* Fixed `JourneyLoginFailure` not being returned when the server sends a login failure response.

### Orchestration SDK for Android 2.1.0

**July 7, 2026**

#### Key features

* **Pushed Authorization Requests (PAR)** \[SDKS-4231]

  PAR sends OAuth 2.0 authorization parameters directly to the server before the redirect begins, keeping them out of the browser URL and reducing the chance of them being tampered with or exposed in logs or referrer headers.

  Learn more in [Configuring Android apps for Pushed Authorization Requests](../../oidc/use-cases/par/android.html).

* **OAuth 2.0 Device Authorization Grant** \[SDKS-4784]

  The Device Authorization Grant is designed for devices with no browser or keyboard, such as smart TVs or set-top boxes. Users authenticate on a secondary device like a phone, and the primary device receives a token once sign-in completes.

  Learn more in [Configuring Android apps for the Device Authorization Grant](../../oidc/use-cases/device-authorization-grant/android.html).

* **Standardized JSON configuration** \[SDKS-5065]

  All SDK modules now support a shared JSON object or file for configuration. This makes it straightforward to manage settings across environments and to share a single configuration file across Android, iOS, and JavaScript.

  Learn more in:

  * [Using common JSON configuration for the Android DaVinci module](../../davinci/usage/android/02-configuring-the-davinci-module.html#common-json-configuration)

  * [Using common JSON configuration for the Android Journey module](../../journey/usage/android/03-configuring-the-journey-module.html#common-json-configuration)

  * [Using common JSON configuration for the Android OIDC module](../../oidc/usage/android-centralized-login.html#android_oidc_common_json_configuration)

* **Android 17 support** \[SDKS-5191]

  Verified the Orchestration SDK for Android works with Android 17.

#### Enhancements

* Added `PollingCollector` for DaVinci flows. \[SDKS-4681]

* Added `QrCodeCollector` for DaVinci flows. \[SDKS-4679]

* Added `BooleanCollector` to support Checkbox and Switch input types in DaVinci forms. \[SDKS-4919]

* Added `ReadOnlyTextCollector` for DaVinci forms to support Terms of Service and agreement displays. \[SDKS-4927]

* Added support for links in Translatable Rich Text (Forms). \[SDKS-4246]

* Added support for phone number extensions in `PhoneNumberCollector`. \[SDKS-4669]

#### Fixes

* Fixed OATH and Push URI parsers to propagate typed `InvalidUriException` for structural URI parse errors. \[SDKS-5074]

* Fixed Ktor CIO engine dropping repeated `Set-Cookie` headers with mixed casing (KTOR-8614 workaround). \[SDKS-4742]

* Fixed Push Number Challenge not surfacing a distinct failure for wrong-number responses. \[SDKS-5116]

* Fixed `PasswordCollector` not handling nested Password policies. \[SDKS-4694]

### Orchestration SDK for React Native 1.0.0

**June 29, 2026**

#### Key features

* **Initial release**

  The initial release of the **Orchestration SDK for React Native** is now available.

  This release supports the following key features:

  * **Authentication journeys**.

    Learn more in [Getting Started with the Journey module for React Native](../../journey/usage/react-native/index.html).

  * **Magic links** for suspending and resuming authentication journeys.

    Learn more in [Setting up magic links](../../journey/use-cases/magic-links/index.html).

  * **Device binding** in authentication journeys.

    Learn more in [Introducing Device Binding](../../journey/use-cases/device-binding/index.html).

  * **Device profiling** in authentication journeys.

    Learn more in [Introducing Device Profiling](../../journey/use-cases/device-profiling/index.html).

  * **OATH-based MFA** in authentication journeys.

    Learn more in [Integrating OATH-based one-time passcode auth journeys](../../journey/use-cases/oath/index.html).

  * **Push-based MFA** in authentication journeys.

    Learn more in [Integrating with Push MFA auth journeys](../../journey/use-cases/push/index.html).

  * **FIDO** and **Passkeys** in authentication journeys.

    Learn more in [Integrating with FIDO (WebAuthn) auth journeys](../../journey/use-cases/fido/index.html).

  * **Social sign-on** with external identity providers.

    Learn more in [Introducing Social Sign-on](../../journey/use-cases/external-idp/index.html).

  * **Self-managing MFA devices** registered in Advanced Identity Cloud and PingAM.

    Learn more in [Managing registered devices](../../journey/use-cases/device-self-service/index.html).

  * **User profile self-service** for reading and updating authenticated user profiles.

    Learn more in [Introducing user profile self-service](../../journey/use-cases/user-self-service/index.html).

### Orchestration SDK for Android 2.0.1

**June 1, 2026**

#### Fixes

* Upgraded `bcpkix-jdk18on` from `1.81` to `1.84` to address a security vulnerability (CVE-2026-5588).

### Orchestration SDK for Android 2.0.0

**April 15, 2026**

#### Key features

* **Initial release**

  The initial release of the **Orchestration SDK for Android** is now available with new features and additional support.

  This release supports the following key features:

  * **Authentication journeys**. \[SDKS-3917]

    Learn more in [Introducing Advanced Identity Cloud and PingAM Journey support](../../journey/index.html).

  * **OATH-based MFA** in authentication journeys. \[SDKS-4021]

    Learn more in [Integrating OATH-based one-time passcode auth journeys](../../journey/use-cases/oath/index.html).

  * **Push-based MFA** in authentication journeys. \[SDKS-4023]

    Learn more in [Integrating with Push MFA auth journeys](../../journey/use-cases/push/index.html).

  * **FIDO** and **Passkeys** in authentication journeys and DaVinci flows. \[SDKS-4023]

    Learn more in [Integrating with FIDO (WebAuthn) auth journeys](../../journey/use-cases/fido/index.html) and [Integrating with FIDO (WebAuthn) DaVinci flows](../../davinci/use-cases/fido/index.html).

  * **Device binding** in authentication journeys. \[SDKS-4115]

    Learn more in [Introducing Device Binding](../../journey/use-cases/device-binding/index.html).

  * **Device profiling** in authentication journeys. \[SDKS-4300]

    Learn more in [Introducing Device Profiling](../../journey/use-cases/device-profiling/index.html).

  * **reCAPTCHA Enterprise** in authentication journeys. \[SDKS-4300]

    Learn more in [Integrate with Google reCAPTCHA Enterprise](../../journey/use-cases/recaptcha-enterprise/index.html).

  * **Self-managing MFA devices** registered in Advanced Identity Cloud and PingAM. \[SDKS-4190]

    Learn more in [Managing registered devices](../../journey/use-cases/device-self-service/index.html).

#### Enhancements

* Added new `network` module. \[SDKS-4505]

* Added new `mfa-commons` module. \[SDKS-4106]

* Added new `auth-migration` module. \[SDKS-4716]

* Added new `device-binding-migration` modules. \[SDKS-4115]

* Added new `device-id` module. \[SDKS-4120]

* Added new `device-root` module. \[SDKS-4365]

### Orchestration SDK for iOS 2.0.0

**April 15, 2026**

#### Key features

* **Initial release**

  The initial release of the **Orchestration SDK for iOS** is now available with new features and additional support.

  This release supports the following key features:

  * **Authentication journeys**. \[SDKS-3918]

    Learn more in [Introducing Advanced Identity Cloud and PingAM Journey support](../../journey/index.html).

  * **OATH-based MFA** in authentication journeys. \[SDKS-4100]

    Learn more in [Integrating OATH-based one-time passcode auth journeys](../../journey/use-cases/oath/index.html).

  * **Push-based MFA** in authentication journeys. \[SDKS-4105]

    Learn more in [Integrating with Push MFA auth journeys](../../journey/use-cases/push/index.html).

  * **FIDO** and **Passkeys** in authentication journeys and DaVinci flows. \[SDKS-4137]

    Learn more in [Integrating with FIDO (WebAuthn) auth journeys](../../journey/use-cases/fido/index.html) and [Integrating with FIDO (WebAuthn) DaVinci flows](../../davinci/use-cases/fido/index.html).

  * **Device binding** in authentication journeys. \[SDKS-4117]

    Learn more in [Introducing Device Binding](../../journey/use-cases/device-binding/index.html).

  * **Device profiling** in authentication journeys. \[SDKS-4128]

    Learn more in [Introducing Device Profiling](../../journey/use-cases/device-profiling/index.html).

  * **reCAPTCHA Enterprise** in authentication journeys. \[SDKS-4440]

    Learn more in [Integrate with Google reCAPTCHA Enterprise](../../journey/use-cases/recaptcha-enterprise/index.html).

  * **Self-managing MFA devices** registered in Advanced Identity Cloud and PingAM. \[SDKS-4491]

    Learn more in [Managing registered devices](../../journey/use-cases/device-self-service/index.html).

#### Enhancements

* Added new `PingNetwork` module. \[SDKS-4496]

* Added new `PingDeviceId` module. \[SDKS-4122]

* Added new `PingTamperDetector` module. \[SDKS-4366]

* Added new `PingJourneyPlugin` and `PingDavinciPlugin` modules. \[SDKS-4492]

* Added new `PingCommons` module. \[SDKS-4104]

* Added support for core callbacks in the `PingJourney` module. \[SDKS-4060]

* Added support for native social login to Facebook, Google, and Apple in Advanced Identity Cloud and PingAM journeys. \[SDKS-3898]

* Added migration mechanism for existing device binding data from the ForgeRock SDK to the Orchestration SDK for iOS. \[SDKS-4495]

#### Fixes

* Updated `PingStorage` module to allow multiple DaVinci/Journey instances to have separate cookies, sessions, and token storage. \[SDKS-4588]

### Orchestration SDK for JavaScript 2.0.0

**April 15, 2026**

#### Key features

* **Initial release**

  The initial release of the **Orchestration SDK for JavaScript** is now available with new features and additional support.

  This release supports the following key features:

  * **Authentication journeys**.

    Learn more in [Introducing Advanced Identity Cloud and PingAM Journey support](../../journey/index.html).

  * **FIDO** and **Passkeys** in authentication journeys.

    Learn more in [Integrating with FIDO (WebAuthn) auth journeys](../../journey/use-cases/fido/index.html).

  * **reCAPTCHA Enterprise** in authentication journeys.

    Learn more in [Integrate with Google reCAPTCHA Enterprise](../../journey/use-cases/recaptcha-enterprise/index.html).

  * **Self-managing MFA devices** registered in Advanced Identity Cloud and PingAM.

    Learn more in [Managing registered devices](../../journey/use-cases/device-self-service/index.html).

#### Enhancements

* Added well-known OIDC endpoint discovery support.

  The **journey** client can now fetch configuration from the `.well-known/openid-configuration` endpoint. The realm path is automatically inferred from the well-known issuer URL.

  Learn more in [Configuring the Journey module in JavaScript](../../journey/usage/javascript/03-configuring-the-journey-module.html).

#### Fixes

* Fixed error handling in the `storage` client and `davinci-client`.

  * Added `isGenericError` type guard to `sdk-utilities` for runtime error validation.

  * Fixed storage client to properly catch errors from custom storage implementations, honoring the errors-as-values contract.

  * Improved `davinci-client` error handling to use explicit error checks instead of try-catch.

---

---
title: Getting support
description: Find support resources, professional services, and troubleshooting articles for Orchestration SDK from Ping Identity
component: orchsdks
page_id: orchsdks:release-notes:support
canonical_url: https://developer.pingidentity.com/orchsdks/release-notes/support.html
llms_txt: https://developer.pingidentity.com/orchsdks/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Compatibility", "Features", "Source Code", "SDK"]
section_ids:
  troubleshooting: Troubleshooting
  additional_articles: Additional Articles
---

# Getting support

Ping Identity provides support services, professional services, training, and partner services to assist you in setting up and maintaining your deployments. For a general overview of these services, see <https://www.pingidentity.com>.

Ping Identity has staff members around the globe who support our international customers and partners. For details on Ping Identity's support offering, visit <https://www.pingidentity.com/support>.

Ping Identity publishes comprehensive documentation online:

* The Ping Identity [Knowledge Base](https://support.pingidentity.com/s/knowledge-base) offers a large and increasing number of up-to-date, practical articles that help you deploy and manage Ping Identity Platform software.

  While many articles are visible to everyone, Ping Identity customers have access to much more, including advanced information for customers using Ping Identity Platform software in a mission-critical capacity.

* Ping Identity product documentation, such as this document, aims to be technically accurate and complete with respect to the software documented. It is visible to everyone and covers all product features and examples of how to use them.

## Troubleshooting

For troubleshooting information, see the following articles in the Knowledge Base:

* [Orchestration SDK Troubleshooting](https://support.pingidentity.com/s/article/Troubleshooting-ForgeRock-SDKs)

### Additional Articles

* [How do I troubleshoot issues with the CORS filter in PingAM/OpenAM (All versions)?](https://support.pingidentity.com/s/article/How-do-I-troubleshoot-issues-with-CORS-in-PingAM)

---

---
title: Incompatible changes
description: Deprecated. Review incompatible SDK changes for Android, iOS, and JavaScript that may affect your deployment before upgrading
component: orchsdks
page_id: orchsdks:release-notes:breaking/breaking-changes
canonical_url: https://developer.pingidentity.com/orchsdks/release-notes/breaking/breaking-changes.html
llms_txt: https://developer.pingidentity.com/orchsdks/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: Wed, 16 Sep 2026 12:00:00 +0000
section_ids:
  JSUNIFIED220: Orchestration SDK for JavaScript 2.2.0
  ANDROID482: Ping (ForgeRock) SDK for Android 4.8.2
  IOS400: Ping (ForgeRock) SDK for iOS 4.0.0
  ANDROID400: Ping (ForgeRock) SDK for Android 4.0.0
  JS400: Ping (ForgeRock) SDK for JavaScript 4.0.0
---

# Incompatible changes

*Incompatible changes* refer to changes that impact existing functionality and might have an effect on your deployment.

Before you upgrade the Orchestration SDK, review these items and make the appropriate changes to your scripts and plugins.

## Orchestration SDK for JavaScript 2.2.0

* Device client custom token store interface change

  The `@forgerock/device-client` package no longer depends on the legacy `@forgerock/javascript-sdk` package.

  The device client has an ignored `tokenStore` configuration property. If you are using TypeScript, and were passing in `TokenStoreObject` to this property, you should update it to use `CustomStorageObject` instead, from `@forgerock/sdk-types`, to prevent type errors.

  The property still has no affect on the device client, so it is unlikely that you will be affected by this change.

## Ping (ForgeRock) SDK for Android 4.8.2

* Upgraded cryptographic libraries

  The libraries the Orchestration SDK for Android use to handle **application PIN** unlocking during device binding have been updated in this release.

  If you application supports an application PIN during device binding you must update your app to use the updated library when upgrading to Orchestration SDK for Android 4.8.2.

  1. In the **Project** tree view of your Android Studio project, open your `build.gradle` file.

  2. In the `dependencies` section, update the application PIN dependency as follows:

     Old dependency:

     ```kotlin
     implementation 'com.madgag.spongycastle:bcpkix-jdk15on:1.58.0.0'
     ```

     Updated dependency:

     ```kotlin
     implementation 'org.bouncycastle:bcpkix-jdk18on:1.81'
     ```

  3. In the `android` section, and the following packaging statement to handle any potential manifest conflicts:

     ```kotlin
     android {
         packaging {
             resources.excludes.add("META-INF/versions/9/OSGI-INF/MANIFEST.MF")
         }
     }
     ```

## Ping (ForgeRock) SDK for iOS 4.0.0

* Exception changes

  * The `FRAClient.updateAccount()` method now throws `AccountError.accountLocked` when attempting to update a locked account.

  * The `HOTPMechanism.generateCode()` and `TOTPMechanism.generateCode()` methods now throw AccountError.accountLocked when attempting to get an OATH token for a locked account.

* Method signature changes

  The signature of the following methods has changed:

  * `WebAuthnRegistrationCallback`

    * Old

      ```swift
      public func register(
        node: Node? = nil,
        onSuccess: @escaping StringCompletionCallback,
        onError: @escaping ErrorCallback
      )
      ```

    * New

      ```swift
      public func register(
        node: Node? = nil,
        window: UIWindow? = UIApplication.shared.windows.first,
        deviceName: String? = nil,
        usePasskeysIfAvailable: Bool = false,
        onSuccess: @escaping StringCompletionCallback,
        onError: @escaping ErrorCallback
      )
      ```

  * `WebAuthnAuthenticationCallback`

    * Old

      ```swift
      public func authenticate(
        node: Node? = nil,
        onSuccess: @escaping StringCompletionCallback,
        onError: @escaping ErrorCallback
      )
      ```

    * New

      ```swift
      public func authenticate(
        node: Node? = nil,
        window: UIWindow? = UIApplication.shared.windows.first,
        preferImmediatelyAvailableCredentials: Bool = false,
        usePasskeysIfAvailable: Bool = false,
        onSuccess: @escaping StringCompletionCallback,
        onError: @escaping ErrorCallback
      )
      ```

  * `FacebookSignInHandler`

    * Old

      ```swift
      public static func handle(
        _ application: UIApplication,
        _ url: URL,
        _ options: [UIApplication.OpenURLOptionsKey : Any] = [:]
      ) -> Bool
      ```

    * New

      ```swift
      public static func application(
        _ application: UIApplication,
        didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey : Any]? = nil
      ) -> Bool
      ```

      |   |                                                                                                                                                                                                                           |
      | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      |   | In ForgeRock SDK for Android 4.0.0 and later, make calls to the method using:`application(_ application:, didFinishLaunchingWithOptions launchOptions: )`Not the previous call:`application(_ app:, open url:, options:)` |

## Ping (ForgeRock) SDK for Android 4.0.0

* Removed support for native single sign-on (SSO)

  The Android platform has deprecated `sharedUserId` that underpins the ForgeRock SDK for Android native SSO implementation.

  This native SSO implementation will not be viable after `sharedUserId` is removed from the Android platform.

  Due to this deprecation, ForgeRock SDK for Android 4.0.0 removes support for Android native single sign-on, as well as the following related changes:

  * `AuthenticatorService` is removed. Remove `<service>` from your `AndroidManifest.xml` file.

  * The ForgeRock SDK for Android no longer requires the following permissions:

    * `android.permission.AUTHENTICATE_ACCOUNTS`

    * `android.permission.GET_ACCOUNTS`

    * `android.permission.MANAGE_ACCOUNTS`

    * `android.permission.USE_CREDENTIALS`

  * The ForgeRock SDK for Android no longer requires the following configuration properties:

    * `forgerock`

    * `forgerock_account_name`

    * `forgerock_webauthn_account_name`

    * `forgerock_webauthn_max_credential`

    * `forgerock_enable_sso`

* Method signature changes

  The signature of the following methods has changed:

  * `WebAuthnRegistrationCallback`

    * Old

      ```java
      public void register(Node node,FRListener<Void> listener)
      ```

    * New

      ```java
      suspend fun register(context: Context, node: Node)
      ```

  * `WebAuthAuthenticationCallback`

    * Old

      ```java
      public void authenticate(
        @NonNull Fragment fragment,
        @NonNull Node node,
        @Nullable WebAuthnKeySelector selector,
        FRListener<Void> listener
      )
      ```

    * New

      ```java
      suspend fun authenticate(
        context: Context,
        node: Node,
        selector: WebAuthnKeySelector = WebAuthnKeySelector.DEFAULT
      )
      ```

  * `org.forgerock.android.auth.FRAClient`

    * Old

      ```java
      public boolean updateAccount(@NonNull Account account)
      ```

    * New

      ```java
      public boolean updateAccount(@NonNull Account account)
        throws AccountLockException
      ```

  * `org.forgerock.android.auth.HOTPMechanism`

    * Old

      ```java
      public OathTokenCode getOathTokenCode()
        throws OathMechanismException
      ```

    * New

      ```java
      public OathTokenCode getOathTokenCode()
        throws OathMechanismException, AccountLockException
      ```

  * `org.forgerock.android.auth.OathMechanism`

    * Old

      ```java
      public abstract OathTokenCode getOathTokenCode()
        throws OathMechanismException
      ```

    * New

      ```java
      public abstract OathTokenCode getOathTokenCode()
        throws OathMechanismException, AccountLockException
      ```

  * `org.forgerock.android.auth.TOTPMechanism`

    * Old

      ```java
      public OathTokenCode getOathTokenCode()
        throws OathMechanismException
      ```

    * New

      ```java
      public OathTokenCode getOathTokenCode()
        throws OathMechanismException, AccountLockException
      ```

## Ping (ForgeRock) SDK for JavaScript 4.0.0

* No longer provides Universal Module Definition (UMD) support

  This version of the ForgeRock SDK for JavaScript does not provide a UMD bundle.

  If you require UMD support, you can:

  * Use an earlier version of the ForgeRock SDK for JavaScript, such as 3.4.0.

  * Clone the repository with the latest source code and configure it locally to provide UMD support.

    |   |                                                                                                                          |
    | - | ------------------------------------------------------------------------------------------------------------------------ |
    |   | Support for CommonJS (CJS) and ES Modules (ESM) is not affected and still provided in ForgeRock SDK for JavaScript 4.0.0 |

* Removal of `indexedDB` token store

  The `indexedDB` option has been removed from the `tokenStore` configuration property in ForgeRock SDK for JavaScript 4.0.0. The `indexedDB` option did not offer sufficient functionality or reliability when the browser is using a private or incognito window.

  If you are using the `indexedDB` option after upgrading to ForgeRock SDK for JavaScript 4.0.0 it is ignored and the SDK defaults to using the `localStorage` option instead. A warning message is output to the browser console.

  This change will not affect the functionality of your app.

* Updated `Policy` types

  Updated policy types so that a `PolicyRequirement` array is output from `failedPolicies`.

* Removed duplicate modules

  Removed the `FRUI` and `Event` modules from the ForgeRock SDK for JavaScript repository.

  These modules were incorrectly duplicated from the [`forgerock-javascript-sdk-ui`](https://github.com/ForgeRock/forgerock-javascript-sdk-ui) repository.

---

---
title: Interface stability
description: Understand interface stability labels used in the SDK documentation, including Evolving and Internal/Undocumented interfaces and the rules that apply to each
component: orchsdks
page_id: orchsdks:release-notes:stability
canonical_url: https://developer.pingidentity.com/orchsdks/release-notes/stability.html
llms_txt: https://developer.pingidentity.com/orchsdks/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: Tue, 23 May 2023 18:14:09 +0100
keywords: ["Compatibility", "Features", "Source Code", "SDK"]
section_ids:
  release-levels: Product release levels
  interface-stability: Product stability labels
---

# Interface stability

Interfaces labelled as *Evolving* in the documentation may change without warning. In addition, the following rules apply:

* Interfaces that are not described in released product documentation should be considered *Internal/Undocumented*.

* Also refer to [Deprecated](deprecations/deprecations.html) features and [Incompatible changes](breaking/breaking-changes.html).

## Product release levels

Ping Identity defines Major, Minor, Maintenance, and Patch product release levels. The version number reflects release level. The release level tells you what sort of compatibility changes to expect.

**Release level definitions**

| Release Label      | Version Numbers                                               | Characteristics                                                                                                                                                                                                                                                                                                                 |
| ------------------ | ------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Major              | Version: x\[.0.0] (trailing 0s are optional)                  | * Bring major new features, minor features, and bug fixes.

* Can include changes even to Stable interfaces.

* Can remove previously Deprecated functionality, and in rare cases remove Evolving functionality that has not been explicitly Deprecated.

* Include changes present in previous Minor and Maintenance releases. |
| Minor              | Version: x.y\[.0] (trailing 0s are optional)                  | - Bring minor features, and bug fixes.

- Can include backwards-compatible changes to Stable interfaces in the same Major release, and incompatible changes to Evolving interfaces.

- Can remove previously Deprecated functionality.

- Include changes present in previous Minor and Maintenance releases.                   |
| Maintenance, Patch | Version: x.y.z\[.p]The optional *p* reflects a Patch version. | * Bring bug fixes

* Are intended to be fully compatible with previous versions from the same Minor release.                                                                                                                                                                                                                    |

## Product stability labels

Ping Identity Platform software supports many features, protocols, APIs, GUIs, and command-line interfaces. Some of these are standard and very stable. Others offer new functionality that is continuing to evolve.

Ping Identity acknowledges you invest in these features and interfaces and so need to understand when they are expected to change. For that reason, we define stability labels and use these definitions in Ping Identity Platform products.

**Stability label definitions**

| Stability Label       | Definition                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Stable                | This documented feature or interface is expected to undergo backwards-compatible changes only for major releases.Changes may be announced at least one minor release before they take effect.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Evolving              | This documented feature or interface is continuing to evolve and so is expected to change, potentially in backwards-incompatible ways even in a minor release. Changes are documented at the time of product release.While new protocols and APIs are still in the process of standardization, they are Evolving. This applies, for example, to recent Internet-Draft implementations and to newly developed functionality.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Legacy                | This feature or interface has been replaced with an improved version, and is no longer receiving development effort from Ping Identity.You should migrate to the newer version, however the existing functionality will remain.Legacy features or interfaces will be marked as *Deprecated* if they are scheduled to be removed from the product.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Deprecated            | This feature or interface is deprecated, and likely to be removed in a future release.For previously stable features or interfaces, the change was likely announced in a previous release.Deprecated features or interfaces will be removed from Ping Identity products.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Removed               | This feature or interface was deprecated in a previous release, and has now been removed from the product.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Technology Preview    | Technology previews provide access to new features that are considered as new technology that is not yet supported. Technology preview features may be functionally incomplete, and the function as implemented is subject to change without notice.*DO NOT DEPLOY A TECHNOLOGY PREVIEW INTO A PRODUCTION ENVIRONMENT.*Customers are encouraged to test drive the technology preview features in a non-production environment, and are welcome to make comments and suggestions about the features in the associated forums.Ping Identity does not guarantee that a technology preview feature will be present in future releases, the final complete version of the feature is liable to change between preview and the final version. Once a technology preview moves into the completed version, said feature will become part of Ping Identity Platform.Technology previews are provided on an "AS-IS" basis for evaluation purposes only, and Ping Identity accepts no liability or obligations for the use thereof. |
| Internal/Undocumented | Internal and undocumented features or interfaces can change without notice.If you depend on one of these features or interfaces, contact support to discuss your needs.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |

---

---
title: Limitations
description: Known issues and limitations for the Orchestration SDKs across Android, iOS, and JavaScript platforms
component: orchsdks
page_id: orchsdks:release-notes:limitations
canonical_url: https://developer.pingidentity.com/orchsdks/release-notes/limitations.html
llms_txt: https://developer.pingidentity.com/orchsdks/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: Wed, 8 Apr 2025 12:47:20 +0100
keywords: ["Compatibility", "Features", "Source Code", "SDK"]
section_ids:
  all_platforms: All platforms
  orchestration_sdk_for_android: Orchestration SDK for Android
  environment: Environment
  symptoms: Symptoms
  cause: Cause
  solution: Solution
  orchestration_sdk_for_ios: Orchestration SDK for iOS
  orchestration_sdk_for_javascript: Orchestration SDK for JavaScript
---

# Limitations

This page lists current known issues and limitations of the Orchestration SDKs.

## All platforms

* The Orchestration SDKs ***do not*** support authentication chains nor modules.

## Orchestration SDK for Android

* Using auth tabs for social sign-on to Facebook might fail if the Facebook app is also installed.

  > **Collapse: Details**
  >
  > Using the Orchestration SDK for Android for social sign-on to Facebook using an auth tab might fail on devices where the Facebook app is installed.
  >
  > The authentication flow exits the browser before completion, resulting in a `BrowserCanceledException` response in the client Android application.
  >
  > ## Environment
  >
  > This issue only occurs in following environment:
  >
  > * You are using Facebook as an external identity provider.
  >
  > * The client device has the Facebook app installed.
  >
  > * You have not imported the native Facebook SDK for Android into the app project.
  >
  >   * The client app has fallen-back to using an auth tab in Chrome to perform the social sign-in.
  >
  > Learn more about configuring social sign-on in Android apps in the following pages:
  >
  > * [Configure Android apps for social sign-on with Journeys](../davinci/use-cases/external-idp/android/index.html)
  >
  > * [Configure Android apps for social sign-on with DaVinci](../journey/use-cases/external-idp/android/index.html)
  >
  > ## Symptoms
  >
  > The following symptoms are indicative of this issue occurring:
  >
  > * The client app launches the web browser to authenticate the user with Facebook, but closes it again immediately.
  >
  > * The user returns to the client application without being able to authenticate to Facebook.
  >
  > * In the client application, the value of `redirectUri` is `null`.
  >
  > * The Orchestration SDK for Android outputs the following console output:
  >
  >   ```text
  >   Result from AuthTab, resultCode: 0, redirectUri: null
  >   BrowserCanceledException: Browser was canceled
  >   ```
  >
  > ## Cause
  >
  > The Android Facebook app is able to intercept the authentication flow in an auth tab by using Android intent resolution.
  >
  > This causes the social sign-on flow to exit the auth tab prematurely, without returning the necessary redirect URI to the client application.
  >
  > Without the redirect URI, the client application assumes the user closed the auth tab and returns the `BrowserCancelledException`, causing social sign-on to fail.
  >
  > ## Solution
  >
  > The Orchestration SDK for Android supports Facebook's native SDK libraries, which handle social sign-on directly rather than redirecting the user in a web browser.
  >
  > This can provide a smoother, more integrated experience for your users than the redirect method.
  >
  > To support a native experience you add the native libraries as dependencies in your Android application:
  >
  > ```gradle
  > // Facebook native sign-on SDK for Android
  > implementation("com.facebook.android:facebook-login:18.1.3")
  > ```
  >
  > Learn more about embedding Facebook libraries for social sign-on at:
  >
  > * [DaVinci flows](../davinci/use-cases/external-idp/android/04_customize_the_user_experience.html#android-facebook-sdk)
  >
  > * [Authentication journeys](../journey/use-cases/external-idp/android/04_customize_the_user_experience.html#android-facebook-sdk)

* Displaying CAPTCHAs or using the Ping (ForgeRock) Authenticator module in your application requires the presence of the Google Play Services.

* The Authenticator module of the Orchestration SDK for Android only supports Firebase Cloud Messaging service as a Push Notification provider.

* Social sign-on with auth journeys requires PingAM 7.1 or the latest version of PingOne Advanced Identity Cloud.

* Biometric authentication is only supported on Android 7.0 or newer.

* Biometric authentication with auth journeys requires PingAM 7.1 or the latest version of PingOne Advanced Identity Cloud.

* Biometric authentication requires the use of Google Play Services.

* When a biometric dialog, such as the *provide fingerprint* dialog, is dismissed, the application may become unresponsive.

* Biometric authentication does not distinguish individual biometrics (fingerprints or faces), but is limited to any registered for the device's current user account.

* Orchestration SDK for Android apps do not function correctly if they are minimized to picture-in-picture mode in [Android custom tabs](https://developer.chrome.com/docs/android/custom-tabs).

  The Orchestration SDK is not able to detect being minimized until API support from Google is available in Android.

## Orchestration SDK for iOS

* Data encryption with Secure Enclave is only available for iOS 10+ devices with TouchID or FaceID.

* Social signon with auth journeys requires PingAM 7.1 or the latest version of PingOne Advanced Identity Cloud.

* The Google Sign-In SDK is only compatible with CocoaPods (Swift Package Manager is not supported).

* Sign In With Apple is only supported in iOS 13 and above.

* Biometric authentication with auth journeys requires PingAM 7.1 or the latest version of PingOne Advanced Identity Cloud.

* Biometric authentication does not distinguish between individual biometrics (fingerprints or faces), but is limited to the collection of biometrics registered for the device's current user account.

* For Biometric authentication, iOS only supports the ES256 signing algorithm, this is configured in the WebAuthn Registration node.

* For "usernameless" biometric authentication support in auth journeys, "limit registrations" must be disabled within the WebAuthn Registration node.

* Device Binding is not supported on iOS simulators. You must use a physical device to test Device Binding.

## Orchestration SDK for JavaScript

* The Orchestration SDK for JavaScript is currently unable to revoke PingOne-issued OIDC tokens when using Firefox and Safari, due to third-party cookie protection.

* When resources are protected by PingGateway, the Orchestration SDK for JavaScript can only support transactional authorization if PingAM and PingGateway are on the same origin.

* FireFox does not support Touch ID as a WebAuthn device on Mac therefore it limits some WebAuthn node configurations.

* The SDK requires polyfills to function in IE 11 and Legacy Edge.

* In WebKit for both macOS and iOS, the "Prevent Cross-site Tracking" option, which is enabled by default, can prevent the SDK from functioning when the app and PingAM are under different origins.

* Collecting location information requires the user's system preferences to allow browser access to location information.

* IndexedDB as a token storage strategy has a known issue with Firefox Private Mode. Use `localStorage` as an alternative.

* Social login with Apple requires the use of a form POST, so the "Redirect URL" cannot be an SPA as they are unable to handle a POST request.

---

---
title: Orchestration SDK for Android changelog
description: Release history for Orchestration SDK for Android, listing new features, enhancements, bug fixes, and security updates for each version
component: orchsdks
page_id: orchsdks:release-notes:changelogs/changelog_android
canonical_url: https://developer.pingidentity.com/orchsdks/release-notes/changelogs/changelog_android.html
llms_txt: https://developer.pingidentity.com/orchsdks/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: Fri, 25 Sep 2026 12:00:00 +0000
keywords: ["Features", "Source Code", "SDK", "DaVinci"]
section_ids:
  unified_android_2_2_0: Orchestration SDK for Android 2.2.0
  key_features: Key features
  added: Added
  changed: Changed
  fixed: Fixed
  unified_android_2_1_0: Orchestration SDK for Android 2.1.0
  key_features_2: Key features
  enhancements: Enhancements
  fixes: Fixes
  unified_android_2_0_1: Orchestration SDK for Android 2.0.1
  fixes_2: Fixes
  unified_android_2_0_0: Orchestration SDK for Android 2.0.0
  key_features_3: Key features
  enhancements_2: Enhancements
  davinci_android_1_3_0: DaVinci client for Android 1.3.0
  enhancements_3: Enhancements
  fixes_3: Fixes
  davinci_android_1_2_0: DaVinci client for Android 1.2.0
  enhancements_4: Enhancements
  davinci_android_1_1_0: DaVinci client for Android 1.1.0
  enhancements_5: Enhancements
  fixes_4: Fixes
  davinci_android_1_0_0: DaVinci client 1.0.0
  enhancements_6: Enhancements
---

# Orchestration SDK for Android changelog

Subscribe to get automatic updates:

* [icon: rss-square, set=fa][Orchestration SDKs Changelog RSS feed](developer_experience_changelog_rss.xml)

* [icon: square-envelope, set=fa][Orchestration SDKs Changelog email notifications](https://backstage.forgerock.com/account/notifications/settings)

## Orchestration SDK for Android 2.2.0

**September 25, 2026**

### Key features

* **PingOne Recognize**

  A new `recognize` module provides privacy-preserving facial biometrics for enrollment and sign-in in authentication journeys.

  Learn more in [Integrating PingOne Recognize](../../journey/use-cases/recognize/index.html).

* **Backchannel authentication** \[SDKS-5157]

  The Orchestration SDK now supports transactional backchannel authentication in authentication journeys, so a third party can initiate a sign-in or transaction on behalf of your user, and your app completes it after the user approves it on their device.

  |   |                                                                                                                                                                                                                                                                       |
  | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | This is not OIDC Client-Initiated Backchannel Authentication (CIBA).This feature uses a proprietary backchannel authentication mechanism in Advanced Identity Cloud and PingAM; a transactional authentication pattern that is unrelated to the OIDC CIBA grant type. |

  Learn more in [Backchannel authentication](../../journey/use-cases/backchannel-auth/index.html).

### Added

* Added a new `pingonemfa` module for PingOne MFA integration, with DaVinci `MobilePairingCollector` support for pairing PingOne MFA accounts directly within a DaVinci flow.

* Added `MetadataCollector` for DaVinci flows to support exchanging custom SDK metadata. \[SDKS-5168]

* Added `ImageCollector` for DaVinci forms to display images. \[SDKS-5169]

* Added an optional HTTP status code to `ErrorNode`. \[SDKS-5202]

### Changed

* Changed FIDO2 authentication to support per-request API selection with `useFido2ApiClient`. \[SDKS-5411]

### Fixed

* Fixed the browser redirect URI scheme manifest placeholder to apply only to debug builds, allowing release consumers to provide their own value. \[SDKS-5296]

* Fixed Journey `submitButtonText`/`pageFooter` to resolve against the device's ordered preferred-locale list. \[SDKS-5310]

* Fixed OIDC `refresh()` to no longer delete the cached token from storage or revoke a non-expired access token before refreshing. \[SDKS-5414]

* Fixed OAuth 2.0 Device Authorization Grant polling to retry on transient network and transport failures instead of terminating the flow. \[SDKS-5124]

* Fixed `AbstractValidatedCallback` throwing when PingAM returns an empty `policies` array instead of an object. \[SDKS-5260]

* Fixed `QRCodeCollector.id()` to return a stable key from the collector configuration instead of a random value. \[SDKS-5293]

* Fixed FIDO2 collectors to report WebAuthn and credential errors as actionable events instead of generic submit failures. \[SDKS-4477]

* Fixed Journey FIDO2 passkey registration crashes on API 33. \[SDKS-5411]

* Fixed Jackson dependency versions to address security vulnerabilities (CVE-2026-54512, CVE-2026-54513, CVE-2026-54514, CVE-2026-54515). \[SDKS-5199]

* Fixed missing blank-secret validation on `OathCredential`, and `OathType` now serializes as lowercase.

## Orchestration SDK for Android 2.1.0

**July 7, 2026**

### Key features

* **Pushed Authorization Requests (PAR)** \[SDKS-4231]

  PAR sends OAuth 2.0 authorization parameters directly to the server before the redirect begins, keeping them out of the browser URL and reducing the chance of them being tampered with or exposed in logs or referrer headers.

  Learn more in [Configuring Android apps for Pushed Authorization Requests](../../oidc/use-cases/par/android.html).

* **OAuth 2.0 Device Authorization Grant** \[SDKS-4784]

  The Device Authorization Grant is designed for devices with no browser or keyboard, such as smart TVs or set-top boxes. Users authenticate on a secondary device like a phone, and the primary device receives a token once sign-in completes.

  Learn more in [Configuring Android apps for the Device Authorization Grant](../../oidc/use-cases/device-authorization-grant/android.html).

* **Standardized JSON configuration** \[SDKS-5065]

  All SDK modules now support a shared JSON object or file for configuration. This makes it straightforward to manage settings across environments and to share a single configuration file across Android, iOS, and JavaScript.

  Learn more in:

  * [Using common JSON configuration for the Android DaVinci module](../../davinci/usage/android/02-configuring-the-davinci-module.html#common-json-configuration)

  * [Using common JSON configuration for the Android Journey module](../../journey/usage/android/03-configuring-the-journey-module.html#common-json-configuration)

  * [Using common JSON configuration for the Android OIDC module](../../oidc/usage/android-centralized-login.html#android_oidc_common_json_configuration)

* **Android 17 support** \[SDKS-5191]

  Verified the Orchestration SDK for Android works with Android 17.

### Enhancements

* Added `PollingCollector` for DaVinci flows. \[SDKS-4681]

* Added `QrCodeCollector` for DaVinci flows. \[SDKS-4679]

* Added `BooleanCollector` to support Checkbox and Switch input types in DaVinci forms. \[SDKS-4919]

* Added `ReadOnlyTextCollector` for DaVinci forms to support Terms of Service and agreement displays. \[SDKS-4927]

* Added support for links in Translatable Rich Text (Forms). \[SDKS-4246]

* Added support for phone number extensions in `PhoneNumberCollector`. \[SDKS-4669]

### Fixes

* Fixed OATH and Push URI parsers to propagate typed `InvalidUriException` for structural URI parse errors. \[SDKS-5074]

* Fixed Ktor CIO engine dropping repeated `Set-Cookie` headers with mixed casing (KTOR-8614 workaround). \[SDKS-4742]

* Fixed Push Number Challenge not surfacing a distinct failure for wrong-number responses. \[SDKS-5116]

* Fixed `PasswordCollector` not handling nested Password policies. \[SDKS-4694]

## Orchestration SDK for Android 2.0.1

**June 1, 2026**

### Fixes

* Upgraded `bcpkix-jdk18on` from `1.81` to `1.84` to address a security vulnerability (CVE-2026-5588).

## Orchestration SDK for Android 2.0.0

**April 15, 2026**

### Key features

* **Initial release**

  The initial release of the **Orchestration SDK for Android** is now available with new features and additional support.

  This release supports the following key features:

  * **Authentication journeys**. \[SDKS-3917]

    Learn more in [Introducing Advanced Identity Cloud and PingAM Journey support](../../journey/index.html).

  * **OATH-based MFA** in authentication journeys. \[SDKS-4021]

    Learn more in [Integrating OATH-based one-time passcode auth journeys](../../journey/use-cases/oath/index.html).

  * **Push-based MFA** in authentication journeys. \[SDKS-4023]

    Learn more in [Integrating with Push MFA auth journeys](../../journey/use-cases/push/index.html).

  * **FIDO** and **Passkeys** in authentication journeys and DaVinci flows. \[SDKS-4023]

    Learn more in [Integrating with FIDO (WebAuthn) auth journeys](../../journey/use-cases/fido/index.html) and [Integrating with FIDO (WebAuthn) DaVinci flows](../../davinci/use-cases/fido/index.html).

  * **Device binding** in authentication journeys. \[SDKS-4115]

    Learn more in [Introducing Device Binding](../../journey/use-cases/device-binding/index.html).

  * **Device profiling** in authentication journeys. \[SDKS-4300]

    Learn more in [Introducing Device Profiling](../../journey/use-cases/device-profiling/index.html).

  * **reCAPTCHA Enterprise** in authentication journeys. \[SDKS-4300]

    Learn more in [Integrate with Google reCAPTCHA Enterprise](../../journey/use-cases/recaptcha-enterprise/index.html).

  * **Self-managing MFA devices** registered in Advanced Identity Cloud and PingAM. \[SDKS-4190]

    Learn more in [Managing registered devices](../../journey/use-cases/device-self-service/index.html).

### Enhancements

* Added new `network` module. \[SDKS-4505]

* Added new `mfa-commons` module. \[SDKS-4106]

* Added new `auth-migration` module. \[SDKS-4716]

* Added new `device-binding-migration` modules. \[SDKS-4115]

* Added new `device-id` module. \[SDKS-4120]

* Added new `device-root` module. \[SDKS-4365]

## DaVinci client for Android 1.3.0

**November 28, 2025**

### Enhancements

* Added support for PingOne Protect, by using the new `PingProtect` module. \[SDKS-4069]

  Learn more in [Evaluating risk with PingOne Protect](../../davinci/use-cases/protect/index.html).

* Added support for Android 16 and updated `compileSdk` to version 36 and `minSdk` to 29. \[SDKS-4278]

### Fixes

* Enhanced form handling in the DaVinci SDK to automatically reset form values after submission. \[SDKS-4511]

* Improved SDK storage configuration to simplify overrides. \[SDKS-4109]

* Enhanced Storage module with cache strategy support. \[SDKS-4112]

* Refactored logger initialization for session and cookie configurations. \[SDKS-4358]

* Updated `PhoneNumberCollector` to support new JSON format. \[SDKS-4198]

* Upgraded datastore library to version 1.1.7. \[SDKS-4207]

## DaVinci client for Android 1.2.0

**July 8, 2025**

### Enhancements

* Added support for native social login with Google and Facebook. \[SDKS-3449]

* Added support for PingOne Forms one-time passcode (MFA) components `DEVICE_REGISTRATION`, `DEVICE_AUTHENTICATION`, and `PHONE_NUMBER`. \[SDKS-3562]

* Added access to the previous `ContinueNode` node from an `ErrorNode`. \[SDKS-3890]

* Added access to the `key` attribute of `LabelCollector`. \[SDKS-3957]

* Added support for StrongBox when generating keys. \[SDKS-4098]

## DaVinci client for Android 1.1.0

**April 17, 2025**

### Enhancements

* Added support for additional [PingOne Form fields](../../davinci/compatibility.html#form-connector-fields-release-notes). \[SDKS-3649]

  * Label

  * Checkbox

  * Dropdown

  * Combobox

  * Radio list

  * Flow link

* Added an `external-idp` module to support social sign on with supported external IDPs by using browser redirects. \[SDKS-3662]

  Supported external IDPs:

  * Apple

  * Facebook

  * Google

* Added `Accept-Language` header to support localization. \[SDKS-3622]

* Added ability to validate PingOne Form fields. \[SDKS-3649]

* Added support for default values in PingOne Form fields. \[SDKS-3649]

* Added an interface to access `ErrorNode` and validation errors. \[SDKS-3649]

* Added a `browser` module. \[SDKS-3662]

* Added dynamic environment switching in the test sample app. \[SDKS-3642]

### Fixes

* Fixed an issue affecting the global logger when configuring a logger in DaVinci client configuration. \[SDKS-3616]

## DaVinci client 1.0.0

**December 16, 2024**

### Enhancements

* Initial release of the DaVinci client for Android.

---

---
title: Orchestration SDK for iOS changelog
description: Release history for Orchestration SDK for iOS, covering new features, improvements, and fixes across all versions
component: orchsdks
page_id: orchsdks:release-notes:changelogs/changelog_ios
canonical_url: https://developer.pingidentity.com/orchsdks/release-notes/changelogs/changelog_ios.html
llms_txt: https://developer.pingidentity.com/orchsdks/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: Tue, 20 Oct 2026 12:00:00 +0000
keywords: ["Features", "Source Code", "SDK", "DaVinci"]
section_ids:
  unified_ios_2_2_0: Orchestration SDK for iOS 2.2.0
  key_features: Key features
  added: Added
  updated: Updated
  breaking_changes: Breaking changes
  changed: Changed
  fixed: Fixed
  unified_ios_2_1_1: Orchestration SDK for iOS 2.1.1
  updated_2: Updated
  unified_ios_2_1_0: Orchestration SDK for iOS 2.1.0
  key_features_2: Key features
  enhancements: Enhancements
  fixes: Fixes
  unified_ios_2_0_0: Orchestration SDK for iOS 2.0.0
  key_features_3: Key features
  enhancements_2: Enhancements
  fixes_2: Fixes
  davinci_ios_1_3_1: DaVinci client for iOS 1.3.1
  updated_3: Updated
  fixes_3: Fixes
  davinci_ios_1_3_0: DaVinci client for iOS 1.3.0
  enhancements_3: Enhancements
  updated_4: Updated
  davinci_ios_1_2_0: DaVinci client for iOS 1.2.0
  enhancements_4: Enhancements
  fixes_4: Fixes
  changes: Changes
  davinci_ios_1_1_0: DaVinci client for iOS 1.1.0
  enhancements_5: Enhancements
  davinci_ios_1_0_0: DaVinci client 1.0.0
  enhancements_6: Enhancements
---

# Orchestration SDK for iOS changelog

Subscribe to get automatic updates:

* [icon: rss-square, set=fa][Orchestration SDKs Changelog RSS feed](developer_experience_changelog_rss.xml)

* [icon: square-envelope, set=fa][Orchestration SDKs Changelog email notifications](https://backstage.forgerock.com/account/notifications/settings)

## Orchestration SDK for iOS 2.2.0

**October 20, 2026**

### Key features

* **PingOne Recognize**

  A new `recognize` module provides privacy-preserving facial biometrics for enrollment and sign-in in authentication journeys.

  Learn more in [Integrating PingOne Recognize](../../journey/use-cases/recognize/index.html).

* Facebook Limited Login

  Sign in to Facebook using the OIDC ID-token flow instead of the classic access-token login.

  In PingOne Advanced Identity Cloud and PingAM journeys, configure an OIDC Social Identity Provider with a name containing `fb-limited` to opt in; existing provider names such as `facebook` continue to use classic access-token login.

  In DaVinci Custom HTML and PingOne Forms, set the new `facebookLimitedLoginEnabled` property on the Facebook collector to choose between the classic `accessToken` and Limited Login `idToken` payloads.

  Learn more in [Authenticating with external identity providers on iOS](../../journey/use-cases/external-idp/ios/index.html).

### Added

* Added a new `pingonemfa` module for PingOne MFA integration, with DaVinci `MobilePairingCollector` support for pairing PingOne MFA accounts directly within a DaVinci flow.

* Added `ImageCollector` to support image display in DaVinci forms. \[SDKS-5143]

* Added `MetadataCollector` to support the DaVinci SDK Integrator connector's pause/resume model, so the app can invoke on-device SDKs and return a result or error before the flow continues. \[SDKS-5142]

* Added `trigger` and `isAutomatic` properties to the DaVinci FIDO collectors. \[SDKS-4552]

* Added a present-only launch mode to `BrowserLauncher` through `browserMode: .custom`.

  `launch()` resolves as soon as the browser UI is presented, without waiting for a callback. Use this for use cases such as session handoff or in-app SSO, where no redirect back to the app is expected. \[SDKS-5357]

* Added `OidcError.configurationError` to report a configuration that has neither a usable `discoveryEndpoint` nor a pre-supplied `openId` object. \[SDKS-5301]

* Added opt-in commercial device-model-name resolution to `DeviceProfileCallback` through `PlatformCollector(includeModelName: true)`; the default `PlatformCollector()` payload is unchanged. \[SDKS-5275]

### Updated

* Redesigned the PingExample sample app with a shared design system. \[SDKS-5054]

* Updated the Facebook iOS SDK dependency to 18.1.0. \[SDKS-5160]

* The `oidc.discoveryEndpoint` property in unified JSON configuration is now required only when no `oidc.openId` sub-object is supplied.

  An `openId` block without `discoveryEndpoint` replaces the discovery document and requires `tokenEndpoint`. \[SDKS-5301]

* Restored `OidcClientConfig.openId` as a publicly settable property, and `oidcInitialize()` now skips OpenID discovery when it is pre-supplied, restoring the 2.0.0 no-discovery configuration path. \[SDKS-5301]

### Breaking changes

* `PingJourney` no longer has a hard dependency on `PingDeviceProfile`. \[SDKS-5443]

  Previously, every `PingJourney` consumer's binary transitively linked `PingDeviceProfile`, whose `BluetoothCollector` instantiates `CBCentralManager`, causing App Store Connect to flag the app for a missing `NSBluetoothAlwaysUsageDescription` even when no `DeviceProfileCallback` node was used.

  If your journeys use the Device Profile Collector node, add the `PingDeviceProfile` product or pod explicitly to your own `Package.swift` or `Podfile`.

* `OidcError` has a new `configurationError` case, so exhaustive `switch` statements over `OidcError` need a new branch. \[SDKS-5301]

### Changed

* A JSON configuration with a blank `oidc.discoveryEndpoint` and no `oidc.openId` sub-object now fails at parse time instead of at first use. \[SDKS-5301]

* `OidcClientConfig.oidcInitialize()` cancellation is now isolated per caller: cancelling one caller's own task still returns promptly with `CancellationError`, but no longer cancels the shared discovery operation for any other caller currently sharing it. \[SDKS-5301]

* `CallbackRegistry.callback(from:)` now logs a debug message when a journey response contains a callback type with no registered handler, such as a `DeviceProfileCallback` in an app that did not add the `PingDeviceProfile` module, making the missing-module misconfiguration diagnosable instead of silently dropping the callback. \[SDKS-5443]

* `SubmitCollector`, `FlowCollector`, and `MetadataCollector` now expose `actionKey` through the new `ActionKeyProvider` protocol. \[SDKS-5290]

### Fixed

* Fixed DaVinci FIDO registration and authentication not launching automatically when the form's `trigger` property is not `BUTTON`. \[SDKS-4552]

* Fixed FIDO2 client-side WebAuthn errors (cancellation, timeout, and similar) not routing to the DaVinci error branch. \[SDKS-4478]

* Fixed `QRCodeCollector` not preserving the complete QR code data URI in `content`. \[SDKS-5299]

* Fixed `OidcWebClient` `.authSession` and `.ephemeralAuthSession` not completing for Universal Link (https) redirect URIs. \[SDKS-5239]

* Fixed `OidcWebClient.authorize()` collapsing `FailureNode.cause` to `.unknown`, losing typed browser-cancellation and unsupported-OS error identity. \[SDKS-5295]

* Fixed 5xx PingAM responses with a parseable error body being misclassified as `FailureNode` instead of `ErrorNode`, diverging from Android. \[SDKS-5358]

* Fixed `Journey.start(backchannelUri:)` not rejecting whitespace-only `authIndexType` and `authIndexValue`, diverging from Android. \[SDKS-5359]

* Fixed the asynchronous `OidcClient.generateAuthorizeUrl(customParams:)` silently falling back to the standard (non-PAR) flow when called before `OidcClientConfig.oidcInitialize()`, which could emit `additionalParameters` onto the returned URL instead of the PAR POST body. The synchronous overload never supported PAR and is unaffected. \[SDKS-5403]

* Fixed `swift build` (macOS) failing in `PingOidc`: `OidcDeviceClient.authorize(verificationUriComplete:)` now throws `BrowserError.httpsCallbackUnsupportedOS` on non-iOS platforms instead of referencing the iOS-only `BrowserLauncher` type, and the `PingOneMFA` target's `PingOneSDK` dependency is iOS-conditioned. \[SDKS-5443]

## Orchestration SDK for iOS 2.1.1

**September 4, 2026**

### Updated

* Updated RecaptchaEnterprise dependency to 18.9.1 for Xcode 27 and iOS 27 compatibility. \[SDKS-5306]

## Orchestration SDK for iOS 2.1.0

**July 22, 2026**

### Key features

* **Pushed Authorization Requests (PAR)** \[SDKS-4235]

  PAR sends OAuth 2.0 authorization parameters directly to the server before the redirect begins, keeping them out of the browser URL and reducing the chance of them being tampered with or exposed in logs or referrer headers.

  Learn more in [Configuring iOS apps for Pushed Authorization Requests](../../oidc/use-cases/par/ios.html).

* **OAuth 2.0 Device Authorization Grant** \[SDKS-4785]

  The Device Authorization Grant is designed for devices with no browser or keyboard, such as smart TVs or set-top boxes. Users authenticate on a secondary device like a phone, and the primary device receives a token once sign-in completes.

  Learn more in [Configuring iOS apps for the Device Authorization Grant](../../oidc/use-cases/device-authorization-grant/ios.html).

* **Standardized JSON configuration** \[SDKS-5066]

  All SDK modules now support a shared JSON object or file for configuration. This makes it straightforward to manage settings across environments and to share a single configuration file across Android, iOS, and JavaScript.

  Learn more in:

  * [Using common JSON configuration for the iOS DaVinci module](../../davinci/usage/ios/02-configuring-the-davinci-module.html#common-json-configuration)

  * [Using common JSON configuration for the iOS Journey module](../../journey/usage/ios/03-configuring-the-journey-module.html#common-json-configuration)

  * [Using common JSON configuration for the iOS OIDC module](../../oidc/usage/ios-centralized-login.html#ios_oidc_common_json_configuration)

### Enhancements

* Added `PollingCollector` for DaVinci flows. \[SDKS-4682]

* Added `QRCodeCollector` for DaVinci flows. \[SDKS-4680]

* Added `BooleanCollector` to support Checkbox and Switch input types in DaVinci forms. \[SDKS-4920]

* Added `ReadOnlyTextCollector` for DaVinci forms. \[SDKS-4928]

* Added rich text and embedded link support to `LabelCollector` through new `RichContent` and `RichContentReplacement` types. \[SDKS-4245]

* Added support for phone number extensions in `PhoneNumberCollector`. \[SDKS-4668]

* Added `PushError.pushNumberChallengeError` to surface a distinct failure for Push Number Challenge responses. \[SDKS-5115]

* Added `preferImmediatelyAvailableCredentials` option to FIDO authentication to restrict the ceremony to locally-available credentials only, if they exist. \[SDKS-5212]

* Added `AuthMigration` module for migrating existing sessions from the legacy ForgeRock SDK. \[SDKS-4773]

* Added Page Node description, header, and footer support. \[SDKS-4762]

### Fixes

* Fixed permanent authentication failure after iCloud device migration caused by a Secure Enclave key mismatch. \[SDKS-5172]

* Fixed `PingFido` WebAuthn registration ignoring the configured `displayName` during passkey creation. \[SDKS-5211]

* Fixed `PasswordCollector` not handling nested password policies. \[SDKS-4695]

* Fixed PIN verification during device binding registration. \[SDKS-5015]

* Fixed `Protect` collector being triggered multiple times within a flow. \[SDKS-4769]

* Fixed browser close and reset logic. \[SDKS-4717]

* Fixed device binding authenticators incorrectly reporting as supported on the simulator. \[SDKS-4836]

* Fixed `DeviceBindingConfig` device name defaulting to the user-assigned name instead of the device model. \[SDKS-4850]

* Fixed `DefaultDeviceIdentifier` to reuse the legacy device identifier when available. \[SDKS-4630]

* Fixed Swift build failures caused by a platform bump and missing `canImport` guards. \[SDKS-4916]

* Fixed FIDO ceremony logs not routing through the workflow logger. \[SDKS-4924]

## Orchestration SDK for iOS 2.0.0

**April 15, 2026**

### Key features

* **Initial release**

  The initial release of the **Orchestration SDK for iOS** is now available with new features and additional support.

  This release supports the following key features:

  * **Authentication journeys**. \[SDKS-3918]

    Learn more in [Introducing Advanced Identity Cloud and PingAM Journey support](../../journey/index.html).

  * **OATH-based MFA** in authentication journeys. \[SDKS-4100]

    Learn more in [Integrating OATH-based one-time passcode auth journeys](../../journey/use-cases/oath/index.html).

  * **Push-based MFA** in authentication journeys. \[SDKS-4105]

    Learn more in [Integrating with Push MFA auth journeys](../../journey/use-cases/push/index.html).

  * **FIDO** and **Passkeys** in authentication journeys and DaVinci flows. \[SDKS-4137]

    Learn more in [Integrating with FIDO (WebAuthn) auth journeys](../../journey/use-cases/fido/index.html) and [Integrating with FIDO (WebAuthn) DaVinci flows](../../davinci/use-cases/fido/index.html).

  * **Device binding** in authentication journeys. \[SDKS-4117]

    Learn more in [Introducing Device Binding](../../journey/use-cases/device-binding/index.html).

  * **Device profiling** in authentication journeys. \[SDKS-4128]

    Learn more in [Introducing Device Profiling](../../journey/use-cases/device-profiling/index.html).

  * **reCAPTCHA Enterprise** in authentication journeys. \[SDKS-4440]

    Learn more in [Integrate with Google reCAPTCHA Enterprise](../../journey/use-cases/recaptcha-enterprise/index.html).

  * **Self-managing MFA devices** registered in Advanced Identity Cloud and PingAM. \[SDKS-4491]

    Learn more in [Managing registered devices](../../journey/use-cases/device-self-service/index.html).

### Enhancements

* Added new `PingNetwork` module. \[SDKS-4496]

* Added new `PingDeviceId` module. \[SDKS-4122]

* Added new `PingTamperDetector` module. \[SDKS-4366]

* Added new `PingJourneyPlugin` and `PingDavinciPlugin` modules. \[SDKS-4492]

* Added new `PingCommons` module. \[SDKS-4104]

* Added support for core callbacks in the `PingJourney` module. \[SDKS-4060]

* Added support for native social login to Facebook, Google, and Apple in Advanced Identity Cloud and PingAM journeys. \[SDKS-3898]

* Added migration mechanism for existing device binding data from the ForgeRock SDK to the Orchestration SDK for iOS. \[SDKS-4495]

### Fixes

* Updated `PingStorage` module to allow multiple DaVinci/Journey instances to have separate cookies, sessions, and token storage. \[SDKS-4588]

## DaVinci client for iOS 1.3.1

**November 25, 2025**

### Updated

* Updated all targets to use the Swift 6 compiler. \[SDKS-4499]

### Fixes

* Fixed an issue in the `PingProtect` module causing a crash on iOS 17+ due to an incorrect actor executor assumption. \[SDKS-4494]

## DaVinci client for iOS 1.3.0

**October 23, 2025**

### Enhancements

* Added support for PingOne Protect, by using the new `PingProtect` module. \[SDKS-4073]

  Learn more in [Evaluating risk with PingOne Protect](../../davinci/use-cases/protect/index.html).

### Updated

* Updated to handle the country code format in the `PhoneNumber` collector. \[SDKS-4199]

* Redesigned and improved the PingExample app. \[SDKS-4104]

## DaVinci client for iOS 1.2.0

**July 8, 2025**

### Enhancements

* Added support for native social login with Apple, Google, and Facebook. \[SDKS-3450]

* Added support for PingOne Forms one-time passcode (MFA) components `DEVICE_REGISTRATION`, `DEVICE_AUTHENTICATION`, and `PHONE_NUMBER`. \[SDKS-3563]

* Added access to the previous `ContinueNode` node from an `ErrorNode`. \[SDKS-3891]

* Added access to the `key` attribute of `LabelCollector`. \[SDKS-3956]

### Fixes

* Resolved an issue where cookies were incorrectly cleared from in-memory storage when requests contain a `Set-Cookie` header \[SDKS-4189]

### Changes

* Renamed the `PingExternal-idp` module to `PingExternalIdP`. \[SDKS-3958]

  You must update the module name in your code if you are using the previous module name and upgrade to DaVinci client for iOS 1.2.0.

## DaVinci client for iOS 1.1.0

**April 17, 2025**

### Enhancements

* Added support for additional [PingOne Form fields](../../davinci/compatibility.html#form-connector-fields-release-notes). \[SDKS-3671, SDKS-3672]

  * Label

  * Checkbox

  * Dropdown

  * Combobox

  * Radio list

  * Flow link

* Added an `external-idp` module to support social sign on with supported external IDPs by using browser redirects. \[SDKS-3720, SDKS-3920]

  Supported external IDPs:

  * Apple

  * Facebook

  * Google

* Added `Accept-Language` header to support localization. \[SDKS-3623]

* Added ability to validate PingOne Form fields. \[SDKS-3671, SDKS-3672]

* Added support for default values in PingOne Form fields. \[SDKS-3674]

* Added a `PingBrowser` module. \[SDKS-3920]

* Added Swift 6 support. \[SDKS-3728]

## DaVinci client 1.0.0

**December 16, 2024**

### Enhancements

* Initial release of the DaVinci client for iOS.

---

---
title: Orchestration SDK for JavaScript changelog
description: Release history for Orchestration SDK for JavaScript, covering new features, enhancements, and fixes across all versions
component: orchsdks
page_id: orchsdks:release-notes:changelogs/changelog_javascript
canonical_url: https://developer.pingidentity.com/orchsdks/release-notes/changelogs/changelog_javascript.html
llms_txt: https://developer.pingidentity.com/orchsdks/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: Fri, 25 Sep 2026 12:00:00 +0000
keywords: ["Features", "Source Code", "SDK", "DaVinci"]
section_ids:
  unified_javascript_2_3_0: Orchestration SDK for JavaScript 2.3.0
  key_features: Key features
  enhancements: Enhancements
  unified_javascript_2_2_0: Orchestration SDK for JavaScript 2.2.0
  enhancements_2: Enhancements
  breaking_changes: Breaking Changes
  changes: Changes
  unified_javascript_2_1_1: Orchestration SDK for JavaScript 2.1.1
  fixes: Fixes
  unified_javascript_2_1_0: Orchestration SDK for JavaScript 2.1.0
  key_features_2: Key features
  added: Added
  updated: Updated
  fixed: Fixed
  unified_javascript_2_0_0: Orchestration SDK for JavaScript 2.0.0
  key_features_3: Key features
  enhancements_3: Enhancements
  fixes_2: Fixes
  davinci_js_1_3_0: DaVinci client for JavaScript 1.3.0
  enhancements_4: Enhancements
  davinci_js_1_2_0: DaVinci client for JavaScript 1.2.0
  enhancements_5: Enhancements
  davinci_js_1_1_0: DaVinci client for JavaScript 1.1.0
  enhancements_6: Enhancements
  updated_2: Updated
  davinci_javascript_1_0_0: DaVinci client 1.0.0
  enhancements_7: Enhancements
---

# Orchestration SDK for JavaScript changelog

Subscribe to get automatic updates:

* [icon: rss-square, set=fa][Orchestration SDKs Changelog RSS feed](developer_experience_changelog_rss.xml)

* [icon: square-envelope, set=fa][Orchestration SDKs Changelog email notifications](https://backstage.forgerock.com/account/notifications/settings)

## Orchestration SDK for JavaScript 2.3.0

**September 25, 2026**

### Key features

* **PingOne Recognize**

  The Journey client now supports PingOne Recognize enrollment and authentication callbacks, providing privacy-preserving facial biometrics for enrollment and sign-in in authentication journeys.

  Learn more in [Integrating PingOne Recognize](../../journey/use-cases/recognize/javascript/index.html).

### Enhancements

* Enhanced `WebAuthn.isConditionalMediationSupported` to now accept an optional journey step. In addition to checking browser support, the method now also reports whether the server requested conditional mediation for that step, so the result reflects the journey's configuration.

* Custom storage configuration types are now exported from the OIDC client, so you can write strongly typed custom storage implementations in TypeScript.

## Orchestration SDK for JavaScript 2.2.0

**September 16, 2026**

### Enhancements

* Added `MetadataCollector` support for DaVinci flows to support exchanging custom SDK metadata.

* Added JSON client config helper re-exports from the respective client packages, so a single import can build a client configuration from the unified JSON config.

* Added `create-journey-step` export so a Journey step is easy to deserialize after it has been serialized.

### Breaking Changes

* Changed the device client `tokenStore` configuration to accept a `CustomStorageObject` instead of the legacy `TokenStoreObject`.

  This is a breaking change for custom token-store implementations. Learn more in [Incompatible changes](../breaking/breaking-changes.html#JSUNIFIED220).

### Changes

* Changed FIDO/WebAuthn `DOMException` handling in DaVinci flows to catch errors and send them to DaVinci instead of failing generically.

* Removed the `@forgerock/javascript-sdk` dependency from `device-client`.

* Fixed the HTTP header to send `ping-sdk` instead of `forgerock-sdk`.

## Orchestration SDK for JavaScript 2.1.1

**August 10, 2026**

### Fixes

* Fixed the OIDC client to always include `prompt=none` on background authorization calls, for both standard and PAR flows.

## Orchestration SDK for JavaScript 2.1.0

**July 8, 2026**

### Key features

* **Pushed Authorization Requests (PAR)**

  PAR sends OAuth 2.0 authorization parameters directly to the server before the redirect begins, keeping them out of the browser URL and reducing the chance of them being tampered with or exposed in logs or referrer headers.

  Learn more in [Configuring JavaScript apps for Pushed Authorization Requests](../../oidc/use-cases/par/javascript.html).

* **Standardized JSON configuration**

  All SDK modules now support a shared JSON object or file for configuration. This makes it straightforward to manage settings across environments and to share a single configuration file across Android, iOS, and JavaScript.

  Learn more in:

  * [Using common JSON configuration for the JavaScript DaVinci module](../../davinci/usage/javascript/02-configuring-the-davinci-module.html#common-json-configuration)

  * [Using common JSON configuration for the JavaScript Journey module](../../journey/usage/javascript/03-configuring-the-journey-module.html#common-json-configuration)

  * [Using common JSON configuration for the JavaScript OIDC module](../../oidc/usage/javascript-centralized-login.html#javascript_oidc_common_json_configuration)

### Added

* Added `PollingCollector` for DaVinci flows.

* Added `QrCodeCollector` for DaVinci flows.

* Added `BooleanCollector` and `ValidatedBooleanCollector` to support Checkbox input types in DaVinci forms.

* Added `PhoneNumberExtensionCollector` for phone number fields that include an extension.

* Added `ValidatedPasswordCollector` for password fields with embedded policy validation.

* Added `ImageCollector` for `IMAGE` form fields in DaVinci forms.

* Added `subscribe` method to journey and OIDC client instances.

* Added WebAuthn conditional mediation (passkey autofill) support.

* Added `user.session()` method for silent OIDC session verification (`prompt=none`).

### Updated

* Updated rich-text support of the `ReadOnlyCollector` to handle links in Translatable Rich Text (Forms).

### Fixed

* Fixed RTK Query cache lookups in `cache.getLatestResponse()` and `cache.getResponseWithId()`.

* Fixed `resume()` to correctly forward redirect query parameters from the authorization response.

* Fixed `JourneyLoginFailure` not being returned when the server sends a login failure response.

## Orchestration SDK for JavaScript 2.0.0

**April 15, 2026**

### Key features

* **Initial release**

  The initial release of the **Orchestration SDK for JavaScript** is now available with new features and additional support.

  This release supports the following key features:

  * **Authentication journeys**.

    Learn more in [Introducing Advanced Identity Cloud and PingAM Journey support](../../journey/index.html).

  * **FIDO** and **Passkeys** in authentication journeys.

    Learn more in [Integrating with FIDO (WebAuthn) auth journeys](../../journey/use-cases/fido/index.html).

  * **reCAPTCHA Enterprise** in authentication journeys.

    Learn more in [Integrate with Google reCAPTCHA Enterprise](../../journey/use-cases/recaptcha-enterprise/index.html).

  * **Self-managing MFA devices** registered in Advanced Identity Cloud and PingAM.

    Learn more in [Managing registered devices](../../journey/use-cases/device-self-service/index.html).

### Enhancements

* Added well-known OIDC endpoint discovery support.

  The **journey** client can now fetch configuration from the `.well-known/openid-configuration` endpoint. The realm path is automatically inferred from the well-known issuer URL.

  Learn more in [Configuring the Journey module in JavaScript](../../journey/usage/javascript/03-configuring-the-journey-module.html).

### Fixes

* Fixed error handling in the `storage` client and `davinci-client`.

  * Added `isGenericError` type guard to `sdk-utilities` for runtime error validation.

  * Fixed storage client to properly catch errors from custom storage implementations, honoring the errors-as-values contract.

  * Improved `davinci-client` error handling to use explicit error checks instead of try-catch.

## DaVinci client for JavaScript 1.3.0

**November 25, 2025**

### Enhancements

* Added support for the Ping Protect collector

  Learn more in [Evaluating risk with PingOne Protect](../../davinci/use-cases/protect/index.html).

* Added support for pre-filled phone number and country code

## DaVinci client for JavaScript 1.2.0

**July 8, 2025**

### Enhancements

* Added support for PingOne Forms one-time passcode (MFA) components `DEVICE_REGISTRATION`, `DEVICE_AUTHENTICATION`, and `PHONE_NUMBER`.

## DaVinci client for JavaScript 1.1.0

**April 17, 2025**

### Enhancements

* Added support for additional [PingOne Form fields](../../davinci/compatibility.html#form-connector-fields-release-notes).

  * Label

  * Checkbox

  * Dropdown

  * Combobox

  * Radio list

  * Flow link

* Added support for social sign on with supported external IDPs.

  Supported external IDPs:

  * Apple

  * Facebook

  * Google

* Added the ability to call start with query parameters which the DaVinci client appends to the `/authorize` call.

* Added request middleware to amend outgoing HTTP requests, for example to override `Accept-Language` headers.

* Added ability to validate PingOne Form fields.

* Added support for default values in PingOne Form fields.

### Updated

* Updated dependency on `@forgerock/javascript-sdk` to `4.7.0`.

* Updated error node to now be submittable to help the app recover from an error state.

* Updated the checks to determine what node state the DaVinci Client is in based on the response from PingOne.

## DaVinci client 1.0.0

**December 16, 2024**

### Enhancements

* Initial release of the DaVinci client JavaScript.

---

---
title: Orchestration SDK for React Native changelog
description: Release history for Orchestration SDK for React Native, listing new features, enhancements, bug fixes, and security updates for each version
component: orchsdks
page_id: orchsdks:release-notes:changelogs/changelog_react_native
canonical_url: https://developer.pingidentity.com/orchsdks/release-notes/changelogs/changelog_react_native.html
llms_txt: https://developer.pingidentity.com/orchsdks/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: Thu, 08 Oct 2026 12:00:00 +0000
keywords: ["Features", "Source Code", "SDK", "React Native"]
section_ids:
  unified_react_native_1_1_0: Orchestration SDK for React Native 1.1.0
  key_features: Key features
  unified_react_native_1_0_0: Orchestration SDK for React Native 1.0.0
  key_features_2: Key features
---

# Orchestration SDK for React Native changelog

Subscribe to get automatic updates:

* [icon: rss-square, set=fa][Orchestration SDKs Changelog RSS feed](developer_experience_changelog_rss.xml)

* [icon: square-envelope, set=fa][Orchestration SDKs Changelog email notifications](https://backstage.forgerock.com/account/notifications/settings)

## Orchestration SDK for React Native 1.1.0

**October 8, 2026**

### Key features

* **DaVinci module for React Native.**

  The first public release of the `@ping-identity/rn-davinci` module lets your React Native app run DaVinci flows end to end, with form rendering and submission.

  Learn more in [Using the DaVinci module for React Native](../../davinci/usage/react-native/index.html).

* **PingOne Protect fraud prevention in DaVinci flows.**

  The new `@ping-identity/rn-protect` module collects behavioral data and sends Protect signals during DaVinci flows, so your React Native app can assess fraud risk.

  Learn more in [Getting started with PingOne Protect on React Native](../../davinci/use-cases/protect/react-native/index.html).

* **External IdP (social sign-on) collectors in DaVinci flows.**

  Authenticate with external identity providers such as Apple, Google, and Facebook directly from DaVinci flows in your React Native app.

  Learn more in [Configure a React Native app for social sign-on](../../davinci/use-cases/external-idp/react-native/index.html).

* **FIDO and passkeys in DaVinci flows.**

  Register and authenticate passkeys in DaVinci flows with the new `FidoRegistrationCollector` and `FidoAuthenticationCollector`.

  Learn more in [Getting started with FIDO on React Native](../../davinci/use-cases/fido/react-native/index.html).

* **Device Authorization Grant in OIDC sign-on.**

  Sign in on devices with limited input, such as smart TVs or set-top boxes, using the new `createOidcDeviceClient` and `useDeviceAuthGrant` APIs.

  Learn more in [Authenticating devices with the Device Authorization Grant](../../oidc/use-cases/device-authorization-grant/index.html).

* **Pushed Authorization Request (PAR) in OIDC sign-on.**

  Send OAuth 2.0 authorization parameters directly to the server before the redirect begins, keeping them out of the browser URL, through the new `par` client config option.

  Learn more in [Securing OIDC sign-on with Pushed Authorization Requests](../../oidc/use-cases/par/index.html).

**Added**

* Added DaVinci `BooleanCollector` and `ReadOnlyTextCollector` support, plus auto-submit for collectors flagged auto-capable by the flow.

* Added DaVinci polling and QRCode collectors so flows can wait on out-of-band status and display QR codes.

* Added DaVinci phone number collector support for phone extension fields (`extension`, `showExtension`, `extensionLabel`).

* Added DaVinci label collector support for `richContent`.

* Added DaVinci password collector support for server-provided validation rules, structured password-policy validation errors (`INVALID_LENGTH`, `UNIQUE_CHARACTER`, `MAX_REPEAT`, `MIN_CHARACTERS`) with native constraint values, and a `validate` method for on-demand collector validation.

**Updated**

* Improved the `useJourneyForm` hook with typed, normalized form fields for simpler Journey callback handling in `@ping-identity/rn-journey`.

* Updated Journey `ContinueNode` to expose UI metadata, such as page header, description, submit button text, and page footer details.

* Improved Expo compatibility with config plugin ownership.

* Updated OATH typed errors to carry violated policy details, so callers can react without parsing message strings.

**Fixed**

* `SOCIAL_LOGIN_BUTTON` no longer reported in unsupported fields when an IdP collector is present in `@ping-identity/rn-davinci`.

## Orchestration SDK for React Native 1.0.0

**June 29, 2026**

### Key features

* **Initial release**

  The initial release of the **Orchestration SDK for React Native** is now available.

  This release supports the following key features:

  * **Authentication journeys**.

    Learn more in [Getting Started with the Journey module for React Native](../../journey/usage/react-native/index.html).

  * **Magic links** for suspending and resuming authentication journeys.

    Learn more in [Setting up magic links](../../journey/use-cases/magic-links/index.html).

  * **Device binding** in authentication journeys.

    Learn more in [Introducing Device Binding](../../journey/use-cases/device-binding/index.html).

  * **Device profiling** in authentication journeys.

    Learn more in [Introducing Device Profiling](../../journey/use-cases/device-profiling/index.html).

  * **OATH-based MFA** in authentication journeys.

    Learn more in [Integrating OATH-based one-time passcode auth journeys](../../journey/use-cases/oath/index.html).

  * **Push-based MFA** in authentication journeys.

    Learn more in [Integrating with Push MFA auth journeys](../../journey/use-cases/push/index.html).

  * **FIDO** and **Passkeys** in authentication journeys.

    Learn more in [Integrating with FIDO (WebAuthn) auth journeys](../../journey/use-cases/fido/index.html).

  * **Social sign-on** with external identity providers.

    Learn more in [Introducing Social Sign-on](../../journey/use-cases/external-idp/index.html).

  * **Self-managing MFA devices** registered in Advanced Identity Cloud and PingAM.

    Learn more in [Managing registered devices](../../journey/use-cases/device-self-service/index.html).

  * **User profile self-service** for reading and updating authenticated user profiles.

    Learn more in [Introducing user profile self-service](../../journey/use-cases/user-self-service/index.html).

---

---
title: Release Notes
description: Find the latest release notes and changelogs for the Orchestration SDKs, including Android, iOS, and JavaScript SDK updates
component: orchsdks
page_id: orchsdks:release-notes:index
canonical_url: https://developer.pingidentity.com/orchsdks/release-notes/index.html
llms_txt: https://developer.pingidentity.com/orchsdks/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: Fri, 16 May 2025 12:17:11 +0100
keywords: ["Compatibility", "Features", "Source Code", "SDK"]
section_ids:
  unified_ios_2_2_0: Orchestration SDK for iOS 2.2.0
  key_features: Key features
  added: Added
  updated: Updated
  breaking_changes: Breaking changes
  changed: Changed
  fixed: Fixed
  unified_react_native_1_1_0: Orchestration SDK for React Native 1.1.0
  key_features_2: Key features
  unified_android_2_2_0: Orchestration SDK for Android 2.2.0
  key_features_3: Key features
  added_2: Added
  changed_2: Changed
  fixed_2: Fixed
  unified_javascript_2_3_0: Orchestration SDK for JavaScript 2.3.0
  key_features_4: Key features
  enhancements: Enhancements
  unified_javascript_2_2_0: Orchestration SDK for JavaScript 2.2.0
  enhancements_2: Enhancements
  breaking_changes_2: Breaking Changes
  changes: Changes
  unified_ios_2_1_1: Orchestration SDK for iOS 2.1.1
  updated_2: Updated
  unified_javascript_2_1_1: Orchestration SDK for JavaScript 2.1.1
  fixes: Fixes
  unified_ios_2_1_0: Orchestration SDK for iOS 2.1.0
  key_features_5: Key features
  enhancements_3: Enhancements
  fixes_2: Fixes
  unified_javascript_2_1_0: Orchestration SDK for JavaScript 2.1.0
  key_features_6: Key features
  added_3: Added
  updated_3: Updated
  fixed_3: Fixed
  unified_android_2_1_0: Orchestration SDK for Android 2.1.0
  key_features_7: Key features
  enhancements_4: Enhancements
  fixes_3: Fixes
  unified_react_native_1_0_0: Orchestration SDK for React Native 1.0.0
  key_features_8: Key features
  unified_android_2_0_1: Orchestration SDK for Android 2.0.1
  fixes_4: Fixes
  unified_android_2_0_0: Orchestration SDK for Android 2.0.0
  key_features_9: Key features
  enhancements_5: Enhancements
  unified_ios_2_0_0: Orchestration SDK for iOS 2.0.0
  key_features_10: Key features
  enhancements_6: Enhancements
  fixes_5: Fixes
  unified_javascript_2_0_0: Orchestration SDK for JavaScript 2.0.0
  key_features_11: Key features
  enhancements_7: Enhancements
  fixes_6: Fixes
  davinci_android_1_3_0: DaVinci client for Android 1.3.0
  enhancements_8: Enhancements
  fixes_7: Fixes
  davinci_js_1_3_0: DaVinci client for JavaScript 1.3.0
  enhancements_9: Enhancements
  davinci_ios_1_3_1: DaVinci client for iOS 1.3.1
  updated_4: Updated
  fixes_8: Fixes
  davinci_ios_1_3_0: DaVinci client for iOS 1.3.0
  enhancements_10: Enhancements
  updated_5: Updated
  davinci_android_1_2_0: DaVinci client for Android 1.2.0
  enhancements_11: Enhancements
  davinci_ios_1_2_0: DaVinci client for iOS 1.2.0
  enhancements_12: Enhancements
  fixes_9: Fixes
  changes_2: Changes
  davinci_js_1_2_0: DaVinci client for JavaScript 1.2.0
  enhancements_13: Enhancements
  davinci_android_1_1_0: DaVinci client for Android 1.1.0
  enhancements_14: Enhancements
  fixes_10: Fixes
  davinci_ios_1_1_0: DaVinci client for iOS 1.1.0
  enhancements_15: Enhancements
  davinci_js_1_1_0: DaVinci client for JavaScript 1.1.0
  enhancements_16: Enhancements
  updated_6: Updated
  davinci_android_1_0_0: DaVinci client 1.0.0
  enhancements_17: Enhancements
  enhancements_18: Enhancements
  enhancements_19: Enhancements
---

# Release Notes

Subscribe to get automatic updates:

* [icon: rss-square, set=fa][Orchestration SDKs Changelog RSS feed](changelogs/developer_experience_changelog_rss.xml)

* [icon: square-envelope, set=fa][Orchestration SDKs Changelog email notifications](https://backstage.forgerock.com/account/notifications/settings)

## Orchestration SDK for iOS 2.2.0

**October 20, 2026**

### Key features

* **PingOne Recognize**

  A new `recognize` module provides privacy-preserving facial biometrics for enrollment and sign-in in authentication journeys.

  Learn more in [Integrating PingOne Recognize](../journey/use-cases/recognize/index.html).

* Facebook Limited Login

  Sign in to Facebook using the OIDC ID-token flow instead of the classic access-token login.

  In PingOne Advanced Identity Cloud and PingAM journeys, configure an OIDC Social Identity Provider with a name containing `fb-limited` to opt in; existing provider names such as `facebook` continue to use classic access-token login.

  In DaVinci Custom HTML and PingOne Forms, set the new `facebookLimitedLoginEnabled` property on the Facebook collector to choose between the classic `accessToken` and Limited Login `idToken` payloads.

  Learn more in [Authenticating with external identity providers on iOS](../journey/use-cases/external-idp/ios/index.html).

### Added

* Added a new `pingonemfa` module for PingOne MFA integration, with DaVinci `MobilePairingCollector` support for pairing PingOne MFA accounts directly within a DaVinci flow.

* Added `ImageCollector` to support image display in DaVinci forms. \[SDKS-5143]

* Added `MetadataCollector` to support the DaVinci SDK Integrator connector's pause/resume model, so the app can invoke on-device SDKs and return a result or error before the flow continues. \[SDKS-5142]

* Added `trigger` and `isAutomatic` properties to the DaVinci FIDO collectors. \[SDKS-4552]

* Added a present-only launch mode to `BrowserLauncher` through `browserMode: .custom`.

  `launch()` resolves as soon as the browser UI is presented, without waiting for a callback. Use this for use cases such as session handoff or in-app SSO, where no redirect back to the app is expected. \[SDKS-5357]

* Added `OidcError.configurationError` to report a configuration that has neither a usable `discoveryEndpoint` nor a pre-supplied `openId` object. \[SDKS-5301]

* Added opt-in commercial device-model-name resolution to `DeviceProfileCallback` through `PlatformCollector(includeModelName: true)`; the default `PlatformCollector()` payload is unchanged. \[SDKS-5275]

### Updated

* Redesigned the PingExample sample app with a shared design system. \[SDKS-5054]

* Updated the Facebook iOS SDK dependency to 18.1.0. \[SDKS-5160]

* The `oidc.discoveryEndpoint` property in unified JSON configuration is now required only when no `oidc.openId` sub-object is supplied.

  An `openId` block without `discoveryEndpoint` replaces the discovery document and requires `tokenEndpoint`. \[SDKS-5301]

* Restored `OidcClientConfig.openId` as a publicly settable property, and `oidcInitialize()` now skips OpenID discovery when it is pre-supplied, restoring the 2.0.0 no-discovery configuration path. \[SDKS-5301]

### Breaking changes

* `PingJourney` no longer has a hard dependency on `PingDeviceProfile`. \[SDKS-5443]

  Previously, every `PingJourney` consumer's binary transitively linked `PingDeviceProfile`, whose `BluetoothCollector` instantiates `CBCentralManager`, causing App Store Connect to flag the app for a missing `NSBluetoothAlwaysUsageDescription` even when no `DeviceProfileCallback` node was used.

  If your journeys use the Device Profile Collector node, add the `PingDeviceProfile` product or pod explicitly to your own `Package.swift` or `Podfile`.

* `OidcError` has a new `configurationError` case, so exhaustive `switch` statements over `OidcError` need a new branch. \[SDKS-5301]

### Changed

* A JSON configuration with a blank `oidc.discoveryEndpoint` and no `oidc.openId` sub-object now fails at parse time instead of at first use. \[SDKS-5301]

* `OidcClientConfig.oidcInitialize()` cancellation is now isolated per caller: cancelling one caller's own task still returns promptly with `CancellationError`, but no longer cancels the shared discovery operation for any other caller currently sharing it. \[SDKS-5301]

* `CallbackRegistry.callback(from:)` now logs a debug message when a journey response contains a callback type with no registered handler, such as a `DeviceProfileCallback` in an app that did not add the `PingDeviceProfile` module, making the missing-module misconfiguration diagnosable instead of silently dropping the callback. \[SDKS-5443]

* `SubmitCollector`, `FlowCollector`, and `MetadataCollector` now expose `actionKey` through the new `ActionKeyProvider` protocol. \[SDKS-5290]

### Fixed

* Fixed DaVinci FIDO registration and authentication not launching automatically when the form's `trigger` property is not `BUTTON`. \[SDKS-4552]

* Fixed FIDO2 client-side WebAuthn errors (cancellation, timeout, and similar) not routing to the DaVinci error branch. \[SDKS-4478]

* Fixed `QRCodeCollector` not preserving the complete QR code data URI in `content`. \[SDKS-5299]

* Fixed `OidcWebClient` `.authSession` and `.ephemeralAuthSession` not completing for Universal Link (https) redirect URIs. \[SDKS-5239]

* Fixed `OidcWebClient.authorize()` collapsing `FailureNode.cause` to `.unknown`, losing typed browser-cancellation and unsupported-OS error identity. \[SDKS-5295]

* Fixed 5xx PingAM responses with a parseable error body being misclassified as `FailureNode` instead of `ErrorNode`, diverging from Android. \[SDKS-5358]

* Fixed `Journey.start(backchannelUri:)` not rejecting whitespace-only `authIndexType` and `authIndexValue`, diverging from Android. \[SDKS-5359]

* Fixed the asynchronous `OidcClient.generateAuthorizeUrl(customParams:)` silently falling back to the standard (non-PAR) flow when called before `OidcClientConfig.oidcInitialize()`, which could emit `additionalParameters` onto the returned URL instead of the PAR POST body. The synchronous overload never supported PAR and is unaffected. \[SDKS-5403]

* Fixed `swift build` (macOS) failing in `PingOidc`: `OidcDeviceClient.authorize(verificationUriComplete:)` now throws `BrowserError.httpsCallbackUnsupportedOS` on non-iOS platforms instead of referencing the iOS-only `BrowserLauncher` type, and the `PingOneMFA` target's `PingOneSDK` dependency is iOS-conditioned. \[SDKS-5443]

## Orchestration SDK for React Native 1.1.0

**October 8, 2026**

### Key features

* **DaVinci module for React Native.**

  The first public release of the `@ping-identity/rn-davinci` module lets your React Native app run DaVinci flows end to end, with form rendering and submission.

  Learn more in [Using the DaVinci module for React Native](../davinci/usage/react-native/index.html).

* **PingOne Protect fraud prevention in DaVinci flows.**

  The new `@ping-identity/rn-protect` module collects behavioral data and sends Protect signals during DaVinci flows, so your React Native app can assess fraud risk.

  Learn more in [Getting started with PingOne Protect on React Native](../davinci/use-cases/protect/react-native/index.html).

* **External IdP (social sign-on) collectors in DaVinci flows.**

  Authenticate with external identity providers such as Apple, Google, and Facebook directly from DaVinci flows in your React Native app.

  Learn more in [Configure a React Native app for social sign-on](../davinci/use-cases/external-idp/react-native/index.html).

* **FIDO and passkeys in DaVinci flows.**

  Register and authenticate passkeys in DaVinci flows with the new `FidoRegistrationCollector` and `FidoAuthenticationCollector`.

  Learn more in [Getting started with FIDO on React Native](../davinci/use-cases/fido/react-native/index.html).

* **Device Authorization Grant in OIDC sign-on.**

  Sign in on devices with limited input, such as smart TVs or set-top boxes, using the new `createOidcDeviceClient` and `useDeviceAuthGrant` APIs.

  Learn more in [Authenticating devices with the Device Authorization Grant](../oidc/use-cases/device-authorization-grant/index.html).

* **Pushed Authorization Request (PAR) in OIDC sign-on.**

  Send OAuth 2.0 authorization parameters directly to the server before the redirect begins, keeping them out of the browser URL, through the new `par` client config option.

  Learn more in [Securing OIDC sign-on with Pushed Authorization Requests](../oidc/use-cases/par/index.html).

**Added**

* Added DaVinci `BooleanCollector` and `ReadOnlyTextCollector` support, plus auto-submit for collectors flagged auto-capable by the flow.

* Added DaVinci polling and QRCode collectors so flows can wait on out-of-band status and display QR codes.

* Added DaVinci phone number collector support for phone extension fields (`extension`, `showExtension`, `extensionLabel`).

* Added DaVinci label collector support for `richContent`.

* Added DaVinci password collector support for server-provided validation rules, structured password-policy validation errors (`INVALID_LENGTH`, `UNIQUE_CHARACTER`, `MAX_REPEAT`, `MIN_CHARACTERS`) with native constraint values, and a `validate` method for on-demand collector validation.

**Updated**

* Improved the `useJourneyForm` hook with typed, normalized form fields for simpler Journey callback handling in `@ping-identity/rn-journey`.

* Updated Journey `ContinueNode` to expose UI metadata, such as page header, description, submit button text, and page footer details.

* Improved Expo compatibility with config plugin ownership.

* Updated OATH typed errors to carry violated policy details, so callers can react without parsing message strings.

**Fixed**

* `SOCIAL_LOGIN_BUTTON` no longer reported in unsupported fields when an IdP collector is present in `@ping-identity/rn-davinci`.

## Orchestration SDK for Android 2.2.0

**September 25, 2026**

### Key features

* **PingOne Recognize**

  A new `recognize` module provides privacy-preserving facial biometrics for enrollment and sign-in in authentication journeys.

  Learn more in [Integrating PingOne Recognize](../journey/use-cases/recognize/index.html).

* **Backchannel authentication** \[SDKS-5157]

  The Orchestration SDK now supports transactional backchannel authentication in authentication journeys, so a third party can initiate a sign-in or transaction on behalf of your user, and your app completes it after the user approves it on their device.

  |   |                                                                                                                                                                                                                                                                       |
  | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | This is not OIDC Client-Initiated Backchannel Authentication (CIBA).This feature uses a proprietary backchannel authentication mechanism in Advanced Identity Cloud and PingAM; a transactional authentication pattern that is unrelated to the OIDC CIBA grant type. |

  Learn more in [Backchannel authentication](../journey/use-cases/backchannel-auth/index.html).

### Added

* Added a new `pingonemfa` module for PingOne MFA integration, with DaVinci `MobilePairingCollector` support for pairing PingOne MFA accounts directly within a DaVinci flow.

* Added `MetadataCollector` for DaVinci flows to support exchanging custom SDK metadata. \[SDKS-5168]

* Added `ImageCollector` for DaVinci forms to display images. \[SDKS-5169]

* Added an optional HTTP status code to `ErrorNode`. \[SDKS-5202]

### Changed

* Changed FIDO2 authentication to support per-request API selection with `useFido2ApiClient`. \[SDKS-5411]

### Fixed

* Fixed the browser redirect URI scheme manifest placeholder to apply only to debug builds, allowing release consumers to provide their own value. \[SDKS-5296]

* Fixed Journey `submitButtonText`/`pageFooter` to resolve against the device's ordered preferred-locale list. \[SDKS-5310]

* Fixed OIDC `refresh()` to no longer delete the cached token from storage or revoke a non-expired access token before refreshing. \[SDKS-5414]

* Fixed OAuth 2.0 Device Authorization Grant polling to retry on transient network and transport failures instead of terminating the flow. \[SDKS-5124]

* Fixed `AbstractValidatedCallback` throwing when PingAM returns an empty `policies` array instead of an object. \[SDKS-5260]

* Fixed `QRCodeCollector.id()` to return a stable key from the collector configuration instead of a random value. \[SDKS-5293]

* Fixed FIDO2 collectors to report WebAuthn and credential errors as actionable events instead of generic submit failures. \[SDKS-4477]

* Fixed Journey FIDO2 passkey registration crashes on API 33. \[SDKS-5411]

* Fixed Jackson dependency versions to address security vulnerabilities (CVE-2026-54512, CVE-2026-54513, CVE-2026-54514, CVE-2026-54515). \[SDKS-5199]

* Fixed missing blank-secret validation on `OathCredential`, and `OathType` now serializes as lowercase.

## Orchestration SDK for JavaScript 2.3.0

**September 25, 2026**

### Key features

* **PingOne Recognize**

  The Journey client now supports PingOne Recognize enrollment and authentication callbacks, providing privacy-preserving facial biometrics for enrollment and sign-in in authentication journeys.

  Learn more in [Integrating PingOne Recognize](../journey/use-cases/recognize/javascript/index.html).

### Enhancements

* Enhanced `WebAuthn.isConditionalMediationSupported` to now accept an optional journey step. In addition to checking browser support, the method now also reports whether the server requested conditional mediation for that step, so the result reflects the journey's configuration.

* Custom storage configuration types are now exported from the OIDC client, so you can write strongly typed custom storage implementations in TypeScript.

## Orchestration SDK for JavaScript 2.2.0

**September 16, 2026**

### Enhancements

* Added `MetadataCollector` support for DaVinci flows to support exchanging custom SDK metadata.

* Added JSON client config helper re-exports from the respective client packages, so a single import can build a client configuration from the unified JSON config.

* Added `create-journey-step` export so a Journey step is easy to deserialize after it has been serialized.

### Breaking Changes

* Changed the device client `tokenStore` configuration to accept a `CustomStorageObject` instead of the legacy `TokenStoreObject`.

  This is a breaking change for custom token-store implementations. Learn more in [Incompatible changes](breaking/breaking-changes.html#JSUNIFIED220).

### Changes

* Changed FIDO/WebAuthn `DOMException` handling in DaVinci flows to catch errors and send them to DaVinci instead of failing generically.

* Removed the `@forgerock/javascript-sdk` dependency from `device-client`.

* Fixed the HTTP header to send `ping-sdk` instead of `forgerock-sdk`.

## Orchestration SDK for iOS 2.1.1

**September 4, 2026**

### Updated

* Updated RecaptchaEnterprise dependency to 18.9.1 for Xcode 27 and iOS 27 compatibility. \[SDKS-5306]

## Orchestration SDK for JavaScript 2.1.1

**August 10, 2026**

### Fixes

* Fixed the OIDC client to always include `prompt=none` on background authorization calls, for both standard and PAR flows.

## Orchestration SDK for iOS 2.1.0

**July 22, 2026**

### Key features

* **Pushed Authorization Requests (PAR)** \[SDKS-4235]

  PAR sends OAuth 2.0 authorization parameters directly to the server before the redirect begins, keeping them out of the browser URL and reducing the chance of them being tampered with or exposed in logs or referrer headers.

  Learn more in [Configuring iOS apps for Pushed Authorization Requests](../oidc/use-cases/par/ios.html).

* **OAuth 2.0 Device Authorization Grant** \[SDKS-4785]

  The Device Authorization Grant is designed for devices with no browser or keyboard, such as smart TVs or set-top boxes. Users authenticate on a secondary device like a phone, and the primary device receives a token once sign-in completes.

  Learn more in [Configuring iOS apps for the Device Authorization Grant](../oidc/use-cases/device-authorization-grant/ios.html).

* **Standardized JSON configuration** \[SDKS-5066]

  All SDK modules now support a shared JSON object or file for configuration. This makes it straightforward to manage settings across environments and to share a single configuration file across Android, iOS, and JavaScript.

  Learn more in:

  * [Using common JSON configuration for the iOS DaVinci module](../davinci/usage/ios/02-configuring-the-davinci-module.html#common-json-configuration)

  * [Using common JSON configuration for the iOS Journey module](../journey/usage/ios/03-configuring-the-journey-module.html#common-json-configuration)

  * [Using common JSON configuration for the iOS OIDC module](../oidc/usage/ios-centralized-login.html#ios_oidc_common_json_configuration)

### Enhancements

* Added `PollingCollector` for DaVinci flows. \[SDKS-4682]

* Added `QRCodeCollector` for DaVinci flows. \[SDKS-4680]

* Added `BooleanCollector` to support Checkbox and Switch input types in DaVinci forms. \[SDKS-4920]

* Added `ReadOnlyTextCollector` for DaVinci forms. \[SDKS-4928]

* Added rich text and embedded link support to `LabelCollector` through new `RichContent` and `RichContentReplacement` types. \[SDKS-4245]

* Added support for phone number extensions in `PhoneNumberCollector`. \[SDKS-4668]

* Added `PushError.pushNumberChallengeError` to surface a distinct failure for Push Number Challenge responses. \[SDKS-5115]

* Added `preferImmediatelyAvailableCredentials` option to FIDO authentication to restrict the ceremony to locally-available credentials only, if they exist. \[SDKS-5212]

* Added `AuthMigration` module for migrating existing sessions from the legacy ForgeRock SDK. \[SDKS-4773]

* Added Page Node description, header, and footer support. \[SDKS-4762]

### Fixes

* Fixed permanent authentication failure after iCloud device migration caused by a Secure Enclave key mismatch. \[SDKS-5172]

* Fixed `PingFido` WebAuthn registration ignoring the configured `displayName` during passkey creation. \[SDKS-5211]

* Fixed `PasswordCollector` not handling nested password policies. \[SDKS-4695]

* Fixed PIN verification during device binding registration. \[SDKS-5015]

* Fixed `Protect` collector being triggered multiple times within a flow. \[SDKS-4769]

* Fixed browser close and reset logic. \[SDKS-4717]

* Fixed device binding authenticators incorrectly reporting as supported on the simulator. \[SDKS-4836]

* Fixed `DeviceBindingConfig` device name defaulting to the user-assigned name instead of the device model. \[SDKS-4850]

* Fixed `DefaultDeviceIdentifier` to reuse the legacy device identifier when available. \[SDKS-4630]

* Fixed Swift build failures caused by a platform bump and missing `canImport` guards. \[SDKS-4916]

* Fixed FIDO ceremony logs not routing through the workflow logger. \[SDKS-4924]

## Orchestration SDK for JavaScript 2.1.0

**July 8, 2026**

### Key features

* **Pushed Authorization Requests (PAR)**

  PAR sends OAuth 2.0 authorization parameters directly to the server before the redirect begins, keeping them out of the browser URL and reducing the chance of them being tampered with or exposed in logs or referrer headers.

  Learn more in [Configuring JavaScript apps for Pushed Authorization Requests](../oidc/use-cases/par/javascript.html).

* **Standardized JSON configuration**

  All SDK modules now support a shared JSON object or file for configuration. This makes it straightforward to manage settings across environments and to share a single configuration file across Android, iOS, and JavaScript.

  Learn more in:

  * [Using common JSON configuration for the JavaScript DaVinci module](../davinci/usage/javascript/02-configuring-the-davinci-module.html#common-json-configuration)

  * [Using common JSON configuration for the JavaScript Journey module](../journey/usage/javascript/03-configuring-the-journey-module.html#common-json-configuration)

  * [Using common JSON configuration for the JavaScript OIDC module](../oidc/usage/javascript-centralized-login.html#javascript_oidc_common_json_configuration)

### Added

* Added `PollingCollector` for DaVinci flows.

* Added `QrCodeCollector` for DaVinci flows.

* Added `BooleanCollector` and `ValidatedBooleanCollector` to support Checkbox input types in DaVinci forms.

* Added `PhoneNumberExtensionCollector` for phone number fields that include an extension.

* Added `ValidatedPasswordCollector` for password fields with embedded policy validation.

* Added `ImageCollector` for `IMAGE` form fields in DaVinci forms.

* Added `subscribe` method to journey and OIDC client instances.

* Added WebAuthn conditional mediation (passkey autofill) support.

* Added `user.session()` method for silent OIDC session verification (`prompt=none`).

### Updated

* Updated rich-text support of the `ReadOnlyCollector` to handle links in Translatable Rich Text (Forms).

### Fixed

* Fixed RTK Query cache lookups in `cache.getLatestResponse()` and `cache.getResponseWithId()`.

* Fixed `resume()` to correctly forward redirect query parameters from the authorization response.

* Fixed `JourneyLoginFailure` not being returned when the server sends a login failure response.

## Orchestration SDK for Android 2.1.0

**July 7, 2026**

### Key features

* **Pushed Authorization Requests (PAR)** \[SDKS-4231]

  PAR sends OAuth 2.0 authorization parameters directly to the server before the redirect begins, keeping them out of the browser URL and reducing the chance of them being tampered with or exposed in logs or referrer headers.

  Learn more in [Configuring Android apps for Pushed Authorization Requests](../oidc/use-cases/par/android.html).

* **OAuth 2.0 Device Authorization Grant** \[SDKS-4784]

  The Device Authorization Grant is designed for devices with no browser or keyboard, such as smart TVs or set-top boxes. Users authenticate on a secondary device like a phone, and the primary device receives a token once sign-in completes.

  Learn more in [Configuring Android apps for the Device Authorization Grant](../oidc/use-cases/device-authorization-grant/android.html).

* **Standardized JSON configuration** \[SDKS-5065]

  All SDK modules now support a shared JSON object or file for configuration. This makes it straightforward to manage settings across environments and to share a single configuration file across Android, iOS, and JavaScript.

  Learn more in:

  * [Using common JSON configuration for the Android DaVinci module](../davinci/usage/android/02-configuring-the-davinci-module.html#common-json-configuration)

  * [Using common JSON configuration for the Android Journey module](../journey/usage/android/03-configuring-the-journey-module.html#common-json-configuration)

  * [Using common JSON configuration for the Android OIDC module](../oidc/usage/android-centralized-login.html#android_oidc_common_json_configuration)

* **Android 17 support** \[SDKS-5191]

  Verified the Orchestration SDK for Android works with Android 17.

### Enhancements

* Added `PollingCollector` for DaVinci flows. \[SDKS-4681]

* Added `QrCodeCollector` for DaVinci flows. \[SDKS-4679]

* Added `BooleanCollector` to support Checkbox and Switch input types in DaVinci forms. \[SDKS-4919]

* Added `ReadOnlyTextCollector` for DaVinci forms to support Terms of Service and agreement displays. \[SDKS-4927]

* Added support for links in Translatable Rich Text (Forms). \[SDKS-4246]

* Added support for phone number extensions in `PhoneNumberCollector`. \[SDKS-4669]

### Fixes

* Fixed OATH and Push URI parsers to propagate typed `InvalidUriException` for structural URI parse errors. \[SDKS-5074]

* Fixed Ktor CIO engine dropping repeated `Set-Cookie` headers with mixed casing (KTOR-8614 workaround). \[SDKS-4742]

* Fixed Push Number Challenge not surfacing a distinct failure for wrong-number responses. \[SDKS-5116]

* Fixed `PasswordCollector` not handling nested Password policies. \[SDKS-4694]

## Orchestration SDK for React Native 1.0.0

**June 29, 2026**

### Key features

* **Initial release**

  The initial release of the **Orchestration SDK for React Native** is now available.

  This release supports the following key features:

  * **Authentication journeys**.

    Learn more in [Getting Started with the Journey module for React Native](../journey/usage/react-native/index.html).

  * **Magic links** for suspending and resuming authentication journeys.

    Learn more in [Setting up magic links](../journey/use-cases/magic-links/index.html).

  * **Device binding** in authentication journeys.

    Learn more in [Introducing Device Binding](../journey/use-cases/device-binding/index.html).

  * **Device profiling** in authentication journeys.

    Learn more in [Introducing Device Profiling](../journey/use-cases/device-profiling/index.html).

  * **OATH-based MFA** in authentication journeys.

    Learn more in [Integrating OATH-based one-time passcode auth journeys](../journey/use-cases/oath/index.html).

  * **Push-based MFA** in authentication journeys.

    Learn more in [Integrating with Push MFA auth journeys](../journey/use-cases/push/index.html).

  * **FIDO** and **Passkeys** in authentication journeys.

    Learn more in [Integrating with FIDO (WebAuthn) auth journeys](../journey/use-cases/fido/index.html).

  * **Social sign-on** with external identity providers.

    Learn more in [Introducing Social Sign-on](../journey/use-cases/external-idp/index.html).

  * **Self-managing MFA devices** registered in Advanced Identity Cloud and PingAM.

    Learn more in [Managing registered devices](../journey/use-cases/device-self-service/index.html).

  * **User profile self-service** for reading and updating authenticated user profiles.

    Learn more in [Introducing user profile self-service](../journey/use-cases/user-self-service/index.html).

## Orchestration SDK for Android 2.0.1

**June 1, 2026**

### Fixes

* Upgraded `bcpkix-jdk18on` from `1.81` to `1.84` to address a security vulnerability (CVE-2026-5588).

## Orchestration SDK for Android 2.0.0

**April 15, 2026**

### Key features

* **Initial release**

  The initial release of the **Orchestration SDK for Android** is now available with new features and additional support.

  This release supports the following key features:

  * **Authentication journeys**. \[SDKS-3917]

    Learn more in [Introducing Advanced Identity Cloud and PingAM Journey support](../journey/index.html).

  * **OATH-based MFA** in authentication journeys. \[SDKS-4021]

    Learn more in [Integrating OATH-based one-time passcode auth journeys](../journey/use-cases/oath/index.html).

  * **Push-based MFA** in authentication journeys. \[SDKS-4023]

    Learn more in [Integrating with Push MFA auth journeys](../journey/use-cases/push/index.html).

  * **FIDO** and **Passkeys** in authentication journeys and DaVinci flows. \[SDKS-4023]

    Learn more in [Integrating with FIDO (WebAuthn) auth journeys](../journey/use-cases/fido/index.html) and [Integrating with FIDO (WebAuthn) DaVinci flows](../davinci/use-cases/fido/index.html).

  * **Device binding** in authentication journeys. \[SDKS-4115]

    Learn more in [Introducing Device Binding](../journey/use-cases/device-binding/index.html).

  * **Device profiling** in authentication journeys. \[SDKS-4300]

    Learn more in [Introducing Device Profiling](../journey/use-cases/device-profiling/index.html).

  * **reCAPTCHA Enterprise** in authentication journeys. \[SDKS-4300]

    Learn more in [Integrate with Google reCAPTCHA Enterprise](../journey/use-cases/recaptcha-enterprise/index.html).

  * **Self-managing MFA devices** registered in Advanced Identity Cloud and PingAM. \[SDKS-4190]

    Learn more in [Managing registered devices](../journey/use-cases/device-self-service/index.html).

### Enhancements

* Added new `network` module. \[SDKS-4505]

* Added new `mfa-commons` module. \[SDKS-4106]

* Added new `auth-migration` module. \[SDKS-4716]

* Added new `device-binding-migration` modules. \[SDKS-4115]

* Added new `device-id` module. \[SDKS-4120]

* Added new `device-root` module. \[SDKS-4365]

## Orchestration SDK for iOS 2.0.0

**April 15, 2026**

### Key features

* **Initial release**

  The initial release of the **Orchestration SDK for iOS** is now available with new features and additional support.

  This release supports the following key features:

  * **Authentication journeys**. \[SDKS-3918]

    Learn more in [Introducing Advanced Identity Cloud and PingAM Journey support](../journey/index.html).

  * **OATH-based MFA** in authentication journeys. \[SDKS-4100]

    Learn more in [Integrating OATH-based one-time passcode auth journeys](../journey/use-cases/oath/index.html).

  * **Push-based MFA** in authentication journeys. \[SDKS-4105]

    Learn more in [Integrating with Push MFA auth journeys](../journey/use-cases/push/index.html).

  * **FIDO** and **Passkeys** in authentication journeys and DaVinci flows. \[SDKS-4137]

    Learn more in [Integrating with FIDO (WebAuthn) auth journeys](../journey/use-cases/fido/index.html) and [Integrating with FIDO (WebAuthn) DaVinci flows](../davinci/use-cases/fido/index.html).

  * **Device binding** in authentication journeys. \[SDKS-4117]

    Learn more in [Introducing Device Binding](../journey/use-cases/device-binding/index.html).

  * **Device profiling** in authentication journeys. \[SDKS-4128]

    Learn more in [Introducing Device Profiling](../journey/use-cases/device-profiling/index.html).

  * **reCAPTCHA Enterprise** in authentication journeys. \[SDKS-4440]

    Learn more in [Integrate with Google reCAPTCHA Enterprise](../journey/use-cases/recaptcha-enterprise/index.html).

  * **Self-managing MFA devices** registered in Advanced Identity Cloud and PingAM. \[SDKS-4491]

    Learn more in [Managing registered devices](../journey/use-cases/device-self-service/index.html).

### Enhancements

* Added new `PingNetwork` module. \[SDKS-4496]

* Added new `PingDeviceId` module. \[SDKS-4122]

* Added new `PingTamperDetector` module. \[SDKS-4366]

* Added new `PingJourneyPlugin` and `PingDavinciPlugin` modules. \[SDKS-4492]

* Added new `PingCommons` module. \[SDKS-4104]

* Added support for core callbacks in the `PingJourney` module. \[SDKS-4060]

* Added support for native social login to Facebook, Google, and Apple in Advanced Identity Cloud and PingAM journeys. \[SDKS-3898]

* Added migration mechanism for existing device binding data from the ForgeRock SDK to the Orchestration SDK for iOS. \[SDKS-4495]

### Fixes

* Updated `PingStorage` module to allow multiple DaVinci/Journey instances to have separate cookies, sessions, and token storage. \[SDKS-4588]

## Orchestration SDK for JavaScript 2.0.0

**April 15, 2026**

### Key features

* **Initial release**

  The initial release of the **Orchestration SDK for JavaScript** is now available with new features and additional support.

  This release supports the following key features:

  * **Authentication journeys**.

    Learn more in [Introducing Advanced Identity Cloud and PingAM Journey support](../journey/index.html).

  * **FIDO** and **Passkeys** in authentication journeys.

    Learn more in [Integrating with FIDO (WebAuthn) auth journeys](../journey/use-cases/fido/index.html).

  * **reCAPTCHA Enterprise** in authentication journeys.

    Learn more in [Integrate with Google reCAPTCHA Enterprise](../journey/use-cases/recaptcha-enterprise/index.html).

  * **Self-managing MFA devices** registered in Advanced Identity Cloud and PingAM.

    Learn more in [Managing registered devices](../journey/use-cases/device-self-service/index.html).

### Enhancements

* Added well-known OIDC endpoint discovery support.

  The **journey** client can now fetch configuration from the `.well-known/openid-configuration` endpoint. The realm path is automatically inferred from the well-known issuer URL.

  Learn more in [Configuring the Journey module in JavaScript](../journey/usage/javascript/03-configuring-the-journey-module.html).

### Fixes

* Fixed error handling in the `storage` client and `davinci-client`.

  * Added `isGenericError` type guard to `sdk-utilities` for runtime error validation.

  * Fixed storage client to properly catch errors from custom storage implementations, honoring the errors-as-values contract.

  * Improved `davinci-client` error handling to use explicit error checks instead of try-catch.

## DaVinci client for Android 1.3.0

**November 28, 2025**

### Enhancements

* Added support for PingOne Protect, by using the new `PingProtect` module. \[SDKS-4069]

  Learn more in [Evaluating risk with PingOne Protect](../davinci/use-cases/protect/index.html).

* Added support for Android 16 and updated `compileSdk` to version 36 and `minSdk` to 29. \[SDKS-4278]

### Fixes

* Enhanced form handling in the DaVinci SDK to automatically reset form values after submission. \[SDKS-4511]

* Improved SDK storage configuration to simplify overrides. \[SDKS-4109]

* Enhanced Storage module with cache strategy support. \[SDKS-4112]

* Refactored logger initialization for session and cookie configurations. \[SDKS-4358]

* Updated `PhoneNumberCollector` to support new JSON format. \[SDKS-4198]

* Upgraded datastore library to version 1.1.7. \[SDKS-4207]

## DaVinci client for JavaScript 1.3.0

**November 25, 2025**

### Enhancements

* Added support for the Ping Protect collector

  Learn more in [Evaluating risk with PingOne Protect](../davinci/use-cases/protect/index.html).

* Added support for pre-filled phone number and country code

## DaVinci client for iOS 1.3.1

**November 25, 2025**

### Updated

* Updated all targets to use the Swift 6 compiler. \[SDKS-4499]

### Fixes

* Fixed an issue in the `PingProtect` module causing a crash on iOS 17+ due to an incorrect actor executor assumption. \[SDKS-4494]

## DaVinci client for iOS 1.3.0

**October 23, 2025**

### Enhancements

* Added support for PingOne Protect, by using the new `PingProtect` module. \[SDKS-4073]

  Learn more in [Evaluating risk with PingOne Protect](../davinci/use-cases/protect/index.html).

### Updated

* Updated to handle the country code format in the `PhoneNumber` collector. \[SDKS-4199]

* Redesigned and improved the PingExample app. \[SDKS-4104]

## DaVinci client for Android 1.2.0

**July 8, 2025**

### Enhancements

* Added support for native social login with Google and Facebook. \[SDKS-3449]

* Added support for PingOne Forms one-time passcode (MFA) components `DEVICE_REGISTRATION`, `DEVICE_AUTHENTICATION`, and `PHONE_NUMBER`. \[SDKS-3562]

* Added access to the previous `ContinueNode` node from an `ErrorNode`. \[SDKS-3890]

* Added access to the `key` attribute of `LabelCollector`. \[SDKS-3957]

* Added support for StrongBox when generating keys. \[SDKS-4098]

## DaVinci client for iOS 1.2.0

**July 8, 2025**

### Enhancements

* Added support for native social login with Apple, Google, and Facebook. \[SDKS-3450]

* Added support for PingOne Forms one-time passcode (MFA) components `DEVICE_REGISTRATION`, `DEVICE_AUTHENTICATION`, and `PHONE_NUMBER`. \[SDKS-3563]

* Added access to the previous `ContinueNode` node from an `ErrorNode`. \[SDKS-3891]

* Added access to the `key` attribute of `LabelCollector`. \[SDKS-3956]

### Fixes

* Resolved an issue where cookies were incorrectly cleared from in-memory storage when requests contain a `Set-Cookie` header \[SDKS-4189]

### Changes

* Renamed the `PingExternal-idp` module to `PingExternalIdP`. \[SDKS-3958]

  You must update the module name in your code if you are using the previous module name and upgrade to DaVinci client for iOS 1.2.0.

## DaVinci client for JavaScript 1.2.0

**July 8, 2025**

### Enhancements

* Added support for PingOne Forms one-time passcode (MFA) components `DEVICE_REGISTRATION`, `DEVICE_AUTHENTICATION`, and `PHONE_NUMBER`.

## DaVinci client for Android 1.1.0

**April 17, 2025**

### Enhancements

* Added support for additional [PingOne Form fields](../davinci/compatibility.html#form-connector-fields-release-notes). \[SDKS-3649]

  * Label

  * Checkbox

  * Dropdown

  * Combobox

  * Radio list

  * Flow link

* Added an `external-idp` module to support social sign on with supported external IDPs by using browser redirects. \[SDKS-3662]

  Supported external IDPs:

  * Apple

  * Facebook

  * Google

* Added `Accept-Language` header to support localization. \[SDKS-3622]

* Added ability to validate PingOne Form fields. \[SDKS-3649]

* Added support for default values in PingOne Form fields. \[SDKS-3649]

* Added an interface to access `ErrorNode` and validation errors. \[SDKS-3649]

* Added a `browser` module. \[SDKS-3662]

* Added dynamic environment switching in the test sample app. \[SDKS-3642]

### Fixes

* Fixed an issue affecting the global logger when configuring a logger in DaVinci client configuration. \[SDKS-3616]

## DaVinci client for iOS 1.1.0

**April 17, 2025**

### Enhancements

* Added support for additional [PingOne Form fields](../davinci/compatibility.html#form-connector-fields-release-notes). \[SDKS-3671, SDKS-3672]

  * Label

  * Checkbox

  * Dropdown

  * Combobox

  * Radio list

  * Flow link

* Added an `external-idp` module to support social sign on with supported external IDPs by using browser redirects. \[SDKS-3720, SDKS-3920]

  Supported external IDPs:

  * Apple

  * Facebook

  * Google

* Added `Accept-Language` header to support localization. \[SDKS-3623]

* Added ability to validate PingOne Form fields. \[SDKS-3671, SDKS-3672]

* Added support for default values in PingOne Form fields. \[SDKS-3674]

* Added a `PingBrowser` module. \[SDKS-3920]

* Added Swift 6 support. \[SDKS-3728]

## DaVinci client for JavaScript 1.1.0

**April 17, 2025**

### Enhancements

* Added support for additional [PingOne Form fields](../davinci/compatibility.html#form-connector-fields-release-notes).

  * Label

  * Checkbox

  * Dropdown

  * Combobox

  * Radio list

  * Flow link

* Added support for social sign on with supported external IDPs.

  Supported external IDPs:

  * Apple

  * Facebook

  * Google

* Added the ability to call start with query parameters which the DaVinci client appends to the `/authorize` call.

* Added request middleware to amend outgoing HTTP requests, for example to override `Accept-Language` headers.

* Added ability to validate PingOne Form fields.

* Added support for default values in PingOne Form fields.

### Updated

* Updated dependency on `@forgerock/javascript-sdk` to `4.7.0`.

* Updated error node to now be submittable to help the app recover from an error state.

* Updated the checks to determine what node state the DaVinci Client is in based on the response from PingOne.

## DaVinci client 1.0.0

**December 16, 2024**

### Enhancements

* Initial release of the DaVinci client for Android. == DaVinci client 1.0.0

**December 16, 2024**

### Enhancements

* Initial release of the DaVinci client for iOS. == DaVinci client 1.0.0

**December 16, 2024**

### Enhancements

* Initial release of the DaVinci client JavaScript.

---

---
title: Release timeline
description: The release history of the Orchestration SDKs, showing when each version shipped and linking to the corresponding changelog entry
component: orchsdks
page_id: orchsdks:release-notes:timeline
canonical_url: https://developer.pingidentity.com/orchsdks/release-notes/timeline.html
llms_txt: https://developer.pingidentity.com/orchsdks/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: Mon, 10 Aug 2026 12:00:00 +0000
keywords: ["Release history", "SDK versions"]
---

# Release timeline

***Key***: *N.N.N* = Latest version

Each row links to the changelog entry for that release.

| Release date | Platform                                                                                                | SDK version | Release type(1) | Link                                                                                            |
| ------------ | ------------------------------------------------------------------------------------------------------- | ----------- | --------------- | ----------------------------------------------------------------------------------------------- |
| 2026-OCT-20  | [Orchestration SDK for iOS](changelogs/changelog_ios.html#unified_ios_2_2_0)                            | *2.2.0*     | Minor           | [[icon: file-lines, set=fa]](changelogs/changelog_ios.html#unified_ios_2_2_0)                   |
| 2026-OCT-08  | [Orchestration SDK for React Native](changelogs/changelog_react_native.html#unified_react_native_1_1_0) | *1.1.0*     | Minor           | [[icon: file-lines, set=fa]](changelogs/changelog_react_native.html#unified_react_native_1_1_0) |
| 2026-SEP-25  | [Orchestration SDK for Android](changelogs/changelog_android.html#unified_android_2_2_0)                | *2.2.0*     | Minor           | [[icon: file-lines, set=fa]](changelogs/changelog_android.html#unified_android_2_2_0)           |
| 2026-SEP-25  | [Orchestration SDK for JavaScript](changelogs/changelog_javascript.html#unified_javascript_2_3_0)       | *2.3.0*     | Minor           | [[icon: file-lines, set=fa]](changelogs/changelog_javascript.html#unified_javascript_2_3_0)     |
| 2026-SEP-16  | [Orchestration SDK for JavaScript](changelogs/changelog_javascript.html#unified_javascript_2_2_0)       | 2.2.0       | Minor           | [[icon: file-lines, set=fa]](changelogs/changelog_javascript.html#unified_javascript_2_2_0)     |
| 2026-SEP-04  | [Orchestration SDK for iOS](changelogs/changelog_ios.html#unified_ios_2_1_1)                            | 2.1.1       | Patch           | [[icon: file-lines, set=fa]](changelogs/changelog_ios.html#unified_ios_2_1_1)                   |
| 2026-AUG-10  | [Orchestration SDK for JavaScript](changelogs/changelog_javascript.html#unified_javascript_2_1_1)       | 2.1.1       | Patch           | [[icon: file-lines, set=fa]](changelogs/changelog_javascript.html#unified_javascript_2_1_1)     |
| 2026-JUL-22  | [Orchestration SDK for iOS](changelogs/changelog_ios.html#unified_ios_2_1_0)                            | 2.1.0       | Minor           | [[icon: file-lines, set=fa]](changelogs/changelog_ios.html#unified_ios_2_1_0)                   |
| 2026-JUL-08  | [Orchestration SDK for JavaScript](changelogs/changelog_javascript.html#unified_javascript_2_1_0)       | 2.1.0       | Minor           | [[icon: file-lines, set=fa]](changelogs/changelog_javascript.html#unified_javascript_2_1_0)     |
| 2026-JUL-07  | [Orchestration SDK for Android](changelogs/changelog_android.html#unified_android_2_1_0)                | 2.1.0       | Minor           | [[icon: file-lines, set=fa]](changelogs/changelog_android.html#unified_android_2_1_0)           |
| 2026-JUN-29  | [Orchestration SDK for React Native](changelogs/changelog_react_native.html#unified_react_native_1_0_0) | 1.0.0       | Major           | [[icon: file-lines, set=fa]](changelogs/changelog_react_native.html#unified_react_native_1_0_0) |
| 2026-JUN-01  | [Orchestration SDK for Android](changelogs/changelog_android.html#unified_android_2_0_1)                | 2.0.1       | Patch           | [[icon: file-lines, set=fa]](changelogs/changelog_android.html#unified_android_2_0_1)           |
| 2026-APR-15  | [Orchestration SDK for Android](changelogs/changelog_android.html#unified_android_2_0_0)                | 2.0.0       | Major           | [[icon: file-lines, set=fa]](changelogs/changelog_android.html#unified_android_2_0_0)           |
| 2026-APR-15  | [Orchestration SDK for iOS](changelogs/changelog_ios.html#unified_ios_2_0_0)                            | 2.0.0       | Major           | [[icon: file-lines, set=fa]](changelogs/changelog_ios.html#unified_ios_2_0_0)                   |
| 2026-APR-15  | [Orchestration SDK for JavaScript](changelogs/changelog_javascript.html#unified_javascript_2_0_0)       | 2.0.0       | Major           | [[icon: file-lines, set=fa]](changelogs/changelog_javascript.html#unified_javascript_2_0_0)     |

> **Collapse: 2025**
>
> | Release date | Platform                                                                               | SDK version | Release type(1) | Link                                                                                  |
> | ------------ | -------------------------------------------------------------------------------------- | ----------- | --------------- | ------------------------------------------------------------------------------------- |
> | 2025-NOV-28  | [DaVinci client for Android](changelogs/changelog_android.html#davinci_android_1_3_0)  | 1.3.0       | Minor           | [[icon: file-lines, set=fa]](changelogs/changelog_android.html#davinci_android_1_3_0) |
> | 2025-NOV-25  | [DaVinci client for JavaScript](changelogs/changelog_javascript.html#davinci_js_1_3_0) | 1.3.0       | Minor           | [[icon: file-lines, set=fa]](changelogs/changelog_javascript.html#davinci_js_1_3_0)   |
> | 2025-NOV-25  | [DaVinci client for iOS](changelogs/changelog_ios.html#davinci_ios_1_3_1)              | 1.3.1       | Patch           | [[icon: file-lines, set=fa]](changelogs/changelog_ios.html#davinci_ios_1_3_1)         |
> | 2025-OCT-23  | [DaVinci client for iOS](changelogs/changelog_ios.html#davinci_ios_1_3_0)              | 1.3.0       | Minor           | [[icon: file-lines, set=fa]](changelogs/changelog_ios.html#davinci_ios_1_3_0)         |
> | 2025-JUL-08  | [DaVinci client for Android](changelogs/changelog_android.html#davinci_android_1_2_0)  | 1.2.0       | Minor           | [[icon: file-lines, set=fa]](changelogs/changelog_android.html#davinci_android_1_2_0) |
> | 2025-JUL-08  | [DaVinci client for iOS](changelogs/changelog_ios.html#davinci_ios_1_2_0)              | 1.2.0       | Minor           | [[icon: file-lines, set=fa]](changelogs/changelog_ios.html#davinci_ios_1_2_0)         |
> | 2025-JUL-08  | [DaVinci client for JavaScript](changelogs/changelog_javascript.html#davinci_js_1_2_0) | 1.2.0       | Minor           | [[icon: file-lines, set=fa]](changelogs/changelog_javascript.html#davinci_js_1_2_0)   |
> | 2025-APR-17  | [DaVinci client for Android](changelogs/changelog_android.html#davinci_android_1_1_0)  | 1.1.0       | Minor           | [[icon: file-lines, set=fa]](changelogs/changelog_android.html#davinci_android_1_1_0) |
> | 2025-APR-17  | [DaVinci client for iOS](changelogs/changelog_ios.html#davinci_ios_1_1_0)              | 1.1.0       | Minor           | [[icon: file-lines, set=fa]](changelogs/changelog_ios.html#davinci_ios_1_1_0)         |
> | 2025-APR-17  | [DaVinci client for JavaScript](changelogs/changelog_javascript.html#davinci_js_1_1_0) | 1.1.0       | Minor           | [[icon: file-lines, set=fa]](changelogs/changelog_javascript.html#davinci_js_1_1_0)   |

> **Collapse: 2024**
>
> | Release date | Platform                                                                                       | SDK version | Release type(1) | Link                                                                                        |
> | ------------ | ---------------------------------------------------------------------------------------------- | ----------- | --------------- | ------------------------------------------------------------------------------------------- |
> | 2024-DEC-16  | [DaVinci client for Android](changelogs/changelog_android.html#davinci_android_1_0_0)          | 1.0.0       | Major           | [[icon: file-lines, set=fa]](changelogs/changelog_android.html#davinci_android_1_0_0)       |
> | 2024-DEC-16  | [DaVinci client for iOS](changelogs/changelog_ios.html#davinci_ios_1_0_0)                      | 1.0.0       | Major           | [[icon: file-lines, set=fa]](changelogs/changelog_ios.html#davinci_ios_1_0_0)               |
> | 2024-DEC-16  | [DaVinci client for JavaScript](changelogs/changelog_javascript.html#davinci_javascript_1_0_0) | 1.0.0       | Major           | [[icon: file-lines, set=fa]](changelogs/changelog_javascript.html#davinci_javascript_1_0_0) |

(1) For details about the scope of expected changes for different release types, see [Interface stability](stability.html).