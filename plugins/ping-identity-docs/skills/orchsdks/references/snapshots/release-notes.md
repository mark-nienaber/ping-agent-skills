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
  unified_react_native_1_0_0: Orchestration SDK for React Native 1.0.0
  unified_android_2_0_1: Orchestration SDK for Android 2.0.1
  unified_android_2_0_0: Orchestration SDK for Android 2.0.0
  unified_ios_2_0_0: Orchestration SDK for iOS 2.0.0
  unified_javascript_2_0_0: Orchestration SDK for JavaScript 2.0.0
---

# Developer Experience changelog

Subscribe to get automatic updates:

* [icon: rss-square, set=fa][Orchestration SDKs Changelog RSS feed](developer_experience_changelog_rss.xml)

* [icon: square-envelope, set=fa][Orchestration SDKs Changelog email notifications](https://backstage.forgerock.com/account/notifications/settings)

## Latest Releases

### Orchestration SDK for React Native 1.0.0

June 29, 2026 `major`

**Key features**

* The initial release of the **Orchestration SDK for React Native** is now available.

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

June 1, 2026 `patch`

**Fixed**

* Upgraded `bcpkix-jdk18on` from `1.81` to `1.84` to address a security vulnerability (CVE-2026-5588).

### Orchestration SDK for Android 2.0.0

April 15, 2026 `major`

**Key features**

* The initial release of the **Orchestration SDK for Android** is now available with new features and additional support.

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

**Added**

* Added new `network` module. \[SDKS-4505]

* Added new `mfa-commons` module. \[SDKS-4106]

* Added new `auth-migration` module. \[SDKS-4716]

* Added new `device-binding-migration` modules. \[SDKS-4115]

* Added new `device-id` module. \[SDKS-4120]

* Added new `device-root` module. \[SDKS-4365]

### Orchestration SDK for iOS 2.0.0

April 15, 2026 `major`

**Key features**

* The initial release of the **Orchestration SDK for iOS** is now available with new features and additional support.

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

**Added**

* Added new `PingNetwork` module. \[SDKS-4496]

* Added new `PingDeviceId` module. \[SDKS-4122]

* Added new `PingTamperDetector` module. \[SDKS-4366]

* Added new `PingJourneyPlugin` and `PingDavinciPlugin` modules. \[SDKS-4492]

* Added new `PingCommons` module. \[SDKS-4104]

* Added support for core callbacks in the `PingJourney` module. \[SDKS-4060]

* Added support for native social login to Facebook, Google, and Apple in Advanced Identity Cloud and PingAM journeys. \[SDKS-3898]

* Added migration mechanism for existing device binding data from the ForgeRock SDK to the Orchestration SDK for iOS. \[SDKS-4495]

**Fixes**

* Updated `PingStorage` module to allow multiple DaVinci/Journey instances to have separate cookies, sessions, and token storage. \[SDKS-4588]

### Orchestration SDK for JavaScript 2.0.0

April 15, 2026 `major`

**Key features**

* The initial release of the **Orchestration SDK for JavaScript** is now available with new features and additional support.

  This release supports the following key features:

  * **Authentication journeys**.

    Learn more in [Introducing Advanced Identity Cloud and PingAM Journey support](../../journey/index.html).

  * **FIDO** and **Passkeys** in authentication journeys.

    Learn more in [Integrating with FIDO (WebAuthn) auth journeys](../../journey/use-cases/fido/index.html).

  * **reCAPTCHA Enterprise** in authentication journeys.

    Learn more in [Integrate with Google reCAPTCHA Enterprise](../../journey/use-cases/recaptcha-enterprise/index.html).

  * **Self-managing MFA devices** registered in Advanced Identity Cloud and PingAM.

    Learn more in [Managing registered devices](../../journey/use-cases/device-self-service/index.html).

**Added**

* Added well-known OIDC endpoint discovery support.

  The **journey** client can now fetch configuration from the `.well-known/openid-configuration` endpoint. The realm path is automatically inferred from the well-known issuer URL.

  Learn more in [Configuring the Journey module in JavaScript](../../journey/usage/javascript/03-configuring-the-journey-module.html).

**Fixed**

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
revdate: Tue, 13 Jun 2023 13:08:39 +0100
section_ids:
  ANDROID482: Orchestration SDK for Android 4.8.2
  IOS400: ForgeRock SDK for iOS 4.0.0
  ANDROID400: ForgeRock SDK for Android 4.0.0
  JS400: ForgeRock SDK for JavaScript 4.0.0
---

# Incompatible changes

*Incompatible changes* refer to changes that impact existing functionality and might have an effect on your deployment. Before you upgrade, review these lists and make the appropriate changes to your scripts and plugins.

## Orchestration SDK for Android 4.8.2

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

## ForgeRock SDK for iOS 4.0.0

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

## ForgeRock SDK for Android 4.0.0

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

## ForgeRock SDK for JavaScript 4.0.0

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
revdate: Sun, 01 Jun 2026 12:00:00 +0000
keywords: ["Features", "Source Code", "SDK", "DaVinci"]
section_ids:
  unified_android_2_0_1: Orchestration SDK for Android 2.0.1
  unified_android_2_0_0: Orchestration SDK for Android 2.0.0
  davinci_android_1_3_0: DaVinci client for Android 1.3.0
  davinci_android_1_2_0: DaVinci client for Android 1.2.0
  davinci_android_1_1_0: DaVinci client for Android 1.1.0
  davinci_android_1_0_0: DaVinci client 1.0.0
---

# Orchestration SDK for Android changelog

Subscribe to get automatic updates:

* [icon: rss-square, set=fa][Orchestration SDKs Changelog RSS feed](developer_experience_changelog_rss.xml)

* [icon: square-envelope, set=fa][Orchestration SDKs Changelog email notifications](https://backstage.forgerock.com/account/notifications/settings)

## Orchestration SDK for Android 2.0.1

June 1, 2026 `patch`

**Fixed**

* Upgraded `bcpkix-jdk18on` from `1.81` to `1.84` to address a security vulnerability (CVE-2026-5588).

## Orchestration SDK for Android 2.0.0

April 15, 2026 `major`

**Key features**

* The initial release of the **Orchestration SDK for Android** is now available with new features and additional support.

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

**Added**

* Added new `network` module. \[SDKS-4505]

* Added new `mfa-commons` module. \[SDKS-4106]

* Added new `auth-migration` module. \[SDKS-4716]

* Added new `device-binding-migration` modules. \[SDKS-4115]

* Added new `device-id` module. \[SDKS-4120]

* Added new `device-root` module. \[SDKS-4365]

## DaVinci client for Android 1.3.0

November 28, 2025 `minor`

**Added**

* Added support for PingOne Protect, by using the new `PingProtect` module. \[SDKS-4069]

  Learn more in [Evaluating risk with PingOne Protect](../../davinci/use-cases/protect/index.html).

* Added support for Android 16 and updated `compileSdk` to version 36 and `minSdk` to 29. \[SDKS-4278]

**Fixed**

* Enhanced form handling in the DaVinci SDK to automatically reset form values after submission. \[SDKS-4511]

* Improved SDK storage configuration to simplify overrides. \[SDKS-4109]

* Enhanced Storage module with cache strategy support. \[SDKS-4112]

* Refactored logger initialization for session and cookie configurations. \[SDKS-4358]

* Updated `PhoneNumberCollector` to support new JSON format. \[SDKS-4198]

* Upgraded datastore library to version 1.1.7. \[SDKS-4207]

## DaVinci client for Android 1.2.0

July 8, 2025 `minor`

**Added**

* Added support for native social login with Google and Facebook. \[SDKS-3449]

* Added support for PingOne Forms one-time passcode (MFA) components `DEVICE_REGISTRATION`, `DEVICE_AUTHENTICATION`, and `PHONE_NUMBER`. \[SDKS-3562]

* Added access to the previous `ContinueNode` node from an `ErrorNode`. \[SDKS-3890]

* Added access to the `key` attribute of `LabelCollector`. \[SDKS-3957]

* Added support for StrongBox when generating keys. \[SDKS-4098]

## DaVinci client for Android 1.1.0

April 17, 2025 `minor`

**Added**

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

**Fixed**

* Fixed an issue affecting the global logger when configuring a logger in DaVinci client configuration. \[SDKS-3616]

## DaVinci client 1.0.0

December 16, 2024 `major`

**Added**

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
revdate: Thu, 19 Jun 2025 15:44:47 +0100
keywords: ["Features", "Source Code", "SDK", "DaVinci"]
section_ids:
  unified_ios_2_0_0: Orchestration SDK for iOS 2.0.0
  davinci_ios_1_3_1: DaVinci client for iOS 1.3.1
  davinci_ios_1_3_0: DaVinci client for iOS 1.3.0
  davinci_ios_1_2_0: DaVinci client for iOS 1.2.0
  davinci_ios_1_1_0: DaVinci client for iOS 1.1.0
  davinci_ios_1_0_0: DaVinci client 1.0.0
---

# Orchestration SDK for iOS changelog

Subscribe to get automatic updates:

* [icon: rss-square, set=fa][Orchestration SDKs Changelog RSS feed](developer_experience_changelog_rss.xml)

* [icon: square-envelope, set=fa][Orchestration SDKs Changelog email notifications](https://backstage.forgerock.com/account/notifications/settings)

## Orchestration SDK for iOS 2.0.0

April 15, 2026 `major`

**Key features**

* The initial release of the **Orchestration SDK for iOS** is now available with new features and additional support.

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

**Added**

* Added new `PingNetwork` module. \[SDKS-4496]

* Added new `PingDeviceId` module. \[SDKS-4122]

* Added new `PingTamperDetector` module. \[SDKS-4366]

* Added new `PingJourneyPlugin` and `PingDavinciPlugin` modules. \[SDKS-4492]

* Added new `PingCommons` module. \[SDKS-4104]

* Added support for core callbacks in the `PingJourney` module. \[SDKS-4060]

* Added support for native social login to Facebook, Google, and Apple in Advanced Identity Cloud and PingAM journeys. \[SDKS-3898]

* Added migration mechanism for existing device binding data from the ForgeRock SDK to the Orchestration SDK for iOS. \[SDKS-4495]

**Fixes**

* Updated `PingStorage` module to allow multiple DaVinci/Journey instances to have separate cookies, sessions, and token storage. \[SDKS-4588]

## DaVinci client for iOS 1.3.1

November 25, 2025 `patch`

**Updated**

* Updated all targets to use the Swift 6 compiler. \[SDKS-4499]

**Fixed**

* Fixed an issue in the `PingProtect` module causing a crash on iOS 17+ due to an incorrect actor executor assumption. \[SDKS-4494]

## DaVinci client for iOS 1.3.0

October 23, 2025 `minor`

**Added**

* Added support for PingOne Protect, by using the new `PingProtect` module. \[SDKS-4073]

  Learn more in [Evaluating risk with PingOne Protect](../../davinci/use-cases/protect/index.html).

**Updated**

* Updated to handle the country code format in the `PhoneNumber` collector. \[SDKS-4199]

* Redesigned and improved the PingExample app. \[SDKS-4104]

## DaVinci client for iOS 1.2.0

July 8, 2025 `minor`

**Added**

* Added support for native social login with Apple, Google, and Facebook. \[SDKS-3450]

* Added support for PingOne Forms one-time passcode (MFA) components `DEVICE_REGISTRATION`, `DEVICE_AUTHENTICATION`, and `PHONE_NUMBER`. \[SDKS-3563]

* Added access to the previous `ContinueNode` node from an `ErrorNode`. \[SDKS-3891]

* Added access to the `key` attribute of `LabelCollector`. \[SDKS-3956]

**Fixed**

* Resolved an issue where cookies were incorrectly cleared from in-memory storage when requests contain a `Set-Cookie` header \[SDKS-4189]

**Changed**

* Renamed the `PingExternal-idp` module to `PingExternalIdP`. \[SDKS-3958]

  You must update the module name in your code if you are using the previous module name and upgrade to DaVinci client for iOS 1.2.0.

## DaVinci client for iOS 1.1.0

April 17, 2025 `minor`

**Added**

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

December 16, 2024 `major`

**Added**

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
revdate: Thu, 19 Jun 2025 15:44:47 +0100
keywords: ["Features", "Source Code", "SDK", "DaVinci"]
section_ids:
  unified_javascript_2_0_0: Orchestration SDK for JavaScript 2.0.0
  davinci_js_1_3_0: DaVinci client for JavaScript 1.3.0
  davinci_js_1_2_0: DaVinci client for JavaScript 1.2.0
  davinci_js_1_1_0: DaVinci client for JavaScript 1.1.0
  davinci_javascript_1_0_0: DaVinci client 1.0.0
---

# Orchestration SDK for JavaScript changelog

Subscribe to get automatic updates:

* [icon: rss-square, set=fa][Orchestration SDKs Changelog RSS feed](developer_experience_changelog_rss.xml)

* [icon: square-envelope, set=fa][Orchestration SDKs Changelog email notifications](https://backstage.forgerock.com/account/notifications/settings)

## Orchestration SDK for JavaScript 2.0.0

April 15, 2026 `major`

**Key features**

* The initial release of the **Orchestration SDK for JavaScript** is now available with new features and additional support.

  This release supports the following key features:

  * **Authentication journeys**.

    Learn more in [Introducing Advanced Identity Cloud and PingAM Journey support](../../journey/index.html).

  * **FIDO** and **Passkeys** in authentication journeys.

    Learn more in [Integrating with FIDO (WebAuthn) auth journeys](../../journey/use-cases/fido/index.html).

  * **reCAPTCHA Enterprise** in authentication journeys.

    Learn more in [Integrate with Google reCAPTCHA Enterprise](../../journey/use-cases/recaptcha-enterprise/index.html).

  * **Self-managing MFA devices** registered in Advanced Identity Cloud and PingAM.

    Learn more in [Managing registered devices](../../journey/use-cases/device-self-service/index.html).

**Added**

* Added well-known OIDC endpoint discovery support.

  The **journey** client can now fetch configuration from the `.well-known/openid-configuration` endpoint. The realm path is automatically inferred from the well-known issuer URL.

  Learn more in [Configuring the Journey module in JavaScript](../../journey/usage/javascript/03-configuring-the-journey-module.html).

**Fixed**

* Fixed error handling in the `storage` client and `davinci-client`.

  * Added `isGenericError` type guard to `sdk-utilities` for runtime error validation.

  * Fixed storage client to properly catch errors from custom storage implementations, honoring the errors-as-values contract.

  * Improved `davinci-client` error handling to use explicit error checks instead of try-catch.

## DaVinci client for JavaScript 1.3.0

November 25, 2025 `minor`

**Added**

* Added support for the Ping Protect collector

  Learn more in [Evaluating risk with PingOne Protect](../../davinci/use-cases/protect/index.html).

* Added support for pre-filled phone number and country code

## DaVinci client for JavaScript 1.2.0

July 8, 2025 `minor`

**Added**

* Added support for PingOne Forms one-time passcode (MFA) components `DEVICE_REGISTRATION`, `DEVICE_AUTHENTICATION`, and `PHONE_NUMBER`.

## DaVinci client for JavaScript 1.1.0

April 17, 2025 `minor`

**Added**

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

**Updated**

* Updated dependency on `@forgerock/javascript-sdk` to `4.7.0`.

* Updated error node to now be submittable to help the app recover from an error state.

* Updated the checks to determine what node state the DaVinci Client is in based on the response from PingOne.

## DaVinci client 1.0.0

December 16, 2024 `major`

**Added**

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
revdate: Sun, 29 Jun 2026 12:00:00 +0000
keywords: ["Features", "Source Code", "SDK", "React Native"]
section_ids:
  unified_react_native_1_0_0: Orchestration SDK for React Native 1.0.0
---

# Orchestration SDK for React Native changelog

Subscribe to get automatic updates:

* [icon: rss-square, set=fa][Orchestration SDKs Changelog RSS feed](developer_experience_changelog_rss.xml)

* [icon: square-envelope, set=fa][Orchestration SDKs Changelog email notifications](https://backstage.forgerock.com/account/notifications/settings)

## Orchestration SDK for React Native 1.0.0

June 29, 2026 `major`

**Key features**

* The initial release of the **Orchestration SDK for React Native** is now available.

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
  latest_updates: Latest updates
  unified_react_native_1_0_0: Orchestration SDK for React Native 1.0.0
  unified_android_2_0_1: Orchestration SDK for Android 2.0.1
  unified_android_2_0_0: Orchestration SDK for Android 2.0.0
  unified_ios_2_0_0: Orchestration SDK for iOS 2.0.0
  unified_javascript_2_0_0: Orchestration SDK for JavaScript 2.0.0
  davinci_android_1_3_0: DaVinci client for Android 1.3.0
  davinci_js_1_3_0: DaVinci client for JavaScript 1.3.0
  davinci_ios_1_3_1: DaVinci client for iOS 1.3.1
  davinci_ios_1_3_0: DaVinci client for iOS 1.3.0
  davinci_android_1_2_0: DaVinci client for Android 1.2.0
  davinci_ios_1_2_0: DaVinci client for iOS 1.2.0
  davinci_js_1_2_0: DaVinci client for JavaScript 1.2.0
  davinci_android_1_1_0: DaVinci client for Android 1.1.0
  davinci_ios_1_1_0: DaVinci client for iOS 1.1.0
  davinci_js_1_1_0: DaVinci client for JavaScript 1.1.0
  davinci_android_1_0_0: DaVinci client 1.0.0
  davinci_ios_1_0_0: DaVinci client 1.0.0
  davinci_javascript_1_0_0: DaVinci client 1.0.0
---

# Release Notes

Subscribe to get automatic updates:

* [icon: rss-square, set=fa][Orchestration SDKs Changelog RSS feed](changelogs/developer_experience_changelog_rss.xml)

* [icon: square-envelope, set=fa][Orchestration SDKs Changelog email notifications](https://backstage.forgerock.com/account/notifications/settings)

## Latest updates

### Orchestration SDK for React Native 1.0.0

June 29, 2026 `major`

**Key features**

* The initial release of the **Orchestration SDK for React Native** is now available.

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

### Orchestration SDK for Android 2.0.1

June 1, 2026 `patch`

**Fixed**

* Upgraded `bcpkix-jdk18on` from `1.81` to `1.84` to address a security vulnerability (CVE-2026-5588).

### Orchestration SDK for Android 2.0.0

April 15, 2026 `major`

**Key features**

* The initial release of the **Orchestration SDK for Android** is now available with new features and additional support.

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

**Added**

* Added new `network` module. \[SDKS-4505]

* Added new `mfa-commons` module. \[SDKS-4106]

* Added new `auth-migration` module. \[SDKS-4716]

* Added new `device-binding-migration` modules. \[SDKS-4115]

* Added new `device-id` module. \[SDKS-4120]

* Added new `device-root` module. \[SDKS-4365]

### Orchestration SDK for iOS 2.0.0

April 15, 2026 `major`

**Key features**

* The initial release of the **Orchestration SDK for iOS** is now available with new features and additional support.

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

**Added**

* Added new `PingNetwork` module. \[SDKS-4496]

* Added new `PingDeviceId` module. \[SDKS-4122]

* Added new `PingTamperDetector` module. \[SDKS-4366]

* Added new `PingJourneyPlugin` and `PingDavinciPlugin` modules. \[SDKS-4492]

* Added new `PingCommons` module. \[SDKS-4104]

* Added support for core callbacks in the `PingJourney` module. \[SDKS-4060]

* Added support for native social login to Facebook, Google, and Apple in Advanced Identity Cloud and PingAM journeys. \[SDKS-3898]

* Added migration mechanism for existing device binding data from the ForgeRock SDK to the Orchestration SDK for iOS. \[SDKS-4495]

**Fixes**

* Updated `PingStorage` module to allow multiple DaVinci/Journey instances to have separate cookies, sessions, and token storage. \[SDKS-4588]

### Orchestration SDK for JavaScript 2.0.0

April 15, 2026 `major`

**Key features**

* The initial release of the **Orchestration SDK for JavaScript** is now available with new features and additional support.

  This release supports the following key features:

  * **Authentication journeys**.

    Learn more in [Introducing Advanced Identity Cloud and PingAM Journey support](../journey/index.html).

  * **FIDO** and **Passkeys** in authentication journeys.

    Learn more in [Integrating with FIDO (WebAuthn) auth journeys](../journey/use-cases/fido/index.html).

  * **reCAPTCHA Enterprise** in authentication journeys.

    Learn more in [Integrate with Google reCAPTCHA Enterprise](../journey/use-cases/recaptcha-enterprise/index.html).

  * **Self-managing MFA devices** registered in Advanced Identity Cloud and PingAM.

    Learn more in [Managing registered devices](../journey/use-cases/device-self-service/index.html).

**Added**

* Added well-known OIDC endpoint discovery support.

  The **journey** client can now fetch configuration from the `.well-known/openid-configuration` endpoint. The realm path is automatically inferred from the well-known issuer URL.

  Learn more in [Configuring the Journey module in JavaScript](../journey/usage/javascript/03-configuring-the-journey-module.html).

**Fixed**

* Fixed error handling in the `storage` client and `davinci-client`.

  * Added `isGenericError` type guard to `sdk-utilities` for runtime error validation.

  * Fixed storage client to properly catch errors from custom storage implementations, honoring the errors-as-values contract.

  * Improved `davinci-client` error handling to use explicit error checks instead of try-catch.

### DaVinci client for Android 1.3.0

November 28, 2025 `minor`

**Added**

* Added support for PingOne Protect, by using the new `PingProtect` module. \[SDKS-4069]

  Learn more in [Evaluating risk with PingOne Protect](../davinci/use-cases/protect/index.html).

* Added support for Android 16 and updated `compileSdk` to version 36 and `minSdk` to 29. \[SDKS-4278]

**Fixed**

* Enhanced form handling in the DaVinci SDK to automatically reset form values after submission. \[SDKS-4511]

* Improved SDK storage configuration to simplify overrides. \[SDKS-4109]

* Enhanced Storage module with cache strategy support. \[SDKS-4112]

* Refactored logger initialization for session and cookie configurations. \[SDKS-4358]

* Updated `PhoneNumberCollector` to support new JSON format. \[SDKS-4198]

* Upgraded datastore library to version 1.1.7. \[SDKS-4207]

### DaVinci client for JavaScript 1.3.0

November 25, 2025 `minor`

**Added**

* Added support for the Ping Protect collector

  Learn more in [Evaluating risk with PingOne Protect](../davinci/use-cases/protect/index.html).

* Added support for pre-filled phone number and country code

### DaVinci client for iOS 1.3.1

November 25, 2025 `patch`

**Updated**

* Updated all targets to use the Swift 6 compiler. \[SDKS-4499]

**Fixed**

* Fixed an issue in the `PingProtect` module causing a crash on iOS 17+ due to an incorrect actor executor assumption. \[SDKS-4494]

### DaVinci client for iOS 1.3.0

October 23, 2025 `minor`

**Added**

* Added support for PingOne Protect, by using the new `PingProtect` module. \[SDKS-4073]

  Learn more in [Evaluating risk with PingOne Protect](../davinci/use-cases/protect/index.html).

**Updated**

* Updated to handle the country code format in the `PhoneNumber` collector. \[SDKS-4199]

* Redesigned and improved the PingExample app. \[SDKS-4104]

### DaVinci client for Android 1.2.0

July 8, 2025 `minor`

**Added**

* Added support for native social login with Google and Facebook. \[SDKS-3449]

* Added support for PingOne Forms one-time passcode (MFA) components `DEVICE_REGISTRATION`, `DEVICE_AUTHENTICATION`, and `PHONE_NUMBER`. \[SDKS-3562]

* Added access to the previous `ContinueNode` node from an `ErrorNode`. \[SDKS-3890]

* Added access to the `key` attribute of `LabelCollector`. \[SDKS-3957]

* Added support for StrongBox when generating keys. \[SDKS-4098]

### DaVinci client for iOS 1.2.0

July 8, 2025 `minor`

**Added**

* Added support for native social login with Apple, Google, and Facebook. \[SDKS-3450]

* Added support for PingOne Forms one-time passcode (MFA) components `DEVICE_REGISTRATION`, `DEVICE_AUTHENTICATION`, and `PHONE_NUMBER`. \[SDKS-3563]

* Added access to the previous `ContinueNode` node from an `ErrorNode`. \[SDKS-3891]

* Added access to the `key` attribute of `LabelCollector`. \[SDKS-3956]

**Fixed**

* Resolved an issue where cookies were incorrectly cleared from in-memory storage when requests contain a `Set-Cookie` header \[SDKS-4189]

**Changed**

* Renamed the `PingExternal-idp` module to `PingExternalIdP`. \[SDKS-3958]

  You must update the module name in your code if you are using the previous module name and upgrade to DaVinci client for iOS 1.2.0.

### DaVinci client for JavaScript 1.2.0

July 8, 2025 `minor`

**Added**

* Added support for PingOne Forms one-time passcode (MFA) components `DEVICE_REGISTRATION`, `DEVICE_AUTHENTICATION`, and `PHONE_NUMBER`.

### DaVinci client for Android 1.1.0

April 17, 2025 `minor`

**Added**

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

**Fixed**

* Fixed an issue affecting the global logger when configuring a logger in DaVinci client configuration. \[SDKS-3616]

### DaVinci client for iOS 1.1.0

April 17, 2025 `minor`

**Added**

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

### DaVinci client for JavaScript 1.1.0

April 17, 2025 `minor`

**Added**

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

**Updated**

* Updated dependency on `@forgerock/javascript-sdk` to `4.7.0`.

* Updated error node to now be submittable to help the app recover from an error state.

* Updated the checks to determine what node state the DaVinci Client is in based on the response from PingOne.

### DaVinci client 1.0.0

December 16, 2024 `major`

**Added**

* Initial release of the DaVinci client for Android.

### DaVinci client 1.0.0

December 16, 2024 `major`

**Added**

* Initial release of the DaVinci client for iOS.

### DaVinci client 1.0.0

December 16, 2024 `major`

**Added**

* Initial release of the DaVinci client JavaScript.