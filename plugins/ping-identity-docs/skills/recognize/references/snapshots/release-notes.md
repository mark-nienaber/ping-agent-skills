---
title: PingOne Recognize Release Notes
description: Release notes for the PingOne Recognize product, including the Mobile SDK and Web SDK.
component: recognize
page_id: recognize:release-notes:index
canonical_url: https://docs.pingidentity.com/recognize/release-notes/index.html
llms_txt: https://docs.pingidentity.com/recognize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-10-19T10:52:24Z
page_aliases: ["mobile-sdk:mobile-sdk-changelog.adoc", "web-sdk:web-sdk-changelog.adoc"]
---

# PingOne Recognize Release Notes

Review release notes for the PingOne Recognize [Mobile](../mobile-sdk/mobile-sdk-introduction.html) and [Web](../web-sdk/web-sdk-getting-started.html) SDKs.

* Mobile SDK

* Web SDK

|   |                                                                                                                                                                                                                                                                                                        |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | Releases marked as `release candidate - rc` are available to selected customers in advance of the official release through the `partners-rc` Cloudsmith repository. Regression tests and QA activity are incomplete, and shipping these versions into production environments is strongly discouraged. |

***

**6.0.2**

**Highlights**

* We added server-side liveness support through the new `mobileLivenessMode` configuration property. You can now run liveness processing on the PingOne Recognize backend instead of, or in addition to, the mobile device. Refer to [Liveness type](../mobile-sdk/mobile-sdk-liveness-settings.html#liveness-type) for details.

* We added the `BALANCED` liveness security level to the existing levels (`DEVELOPMENT`, `LEVEL_1`, and `LEVEL_2`). `BALANCED` prioritizes usability while providing liveness protection. Refer to [Liveness level configuration](../mobile-sdk/mobile-sdk-liveness-settings.html#liveness-level-configuration) for details.

***

**6.0.1**

**Highlights**

* We now only log a device that might not be genuine. The SDK doesn't return errors because this check is currently silent.

***

**6.0.0**

**Highlights**

* New branding logo for the PingOne Recognize authentication flows.

**Breaking changes**

* Removed deprecated IDP/IAM support `iamToken` field can no longer be used from configurations.

* Removed deprecated `temporaryState` and `shouldRetrieveTemporaryState` fields, use [clientState](../mobile-sdk/mobile-sdk-generating-client-state.html) instead.

* Removed deprecated `LivenessConfiguration` entries: you can no longer use liveness configurations prefixed with `PASSIVE_`. See [liveness settings](../mobile-sdk/mobile-sdk-liveness-settings.html) for the available liveness levels.

* Removed deprecated `withDevicePrivileges` from `SetupConfig`.

* Removed deprecated `.isEnrolled`, you should use `validateUserAndDeviceActive`, see [user and device management](../mobile-sdk/mobile-sdk-user-and-device-management.html).

* Removed `.internalId`, see [user and device management](../mobile-sdk/mobile-sdk-user-and-device-management.html) to get the user identifier.

* Removed deprecated `getDeviceEncryptionPublicKey()`.

* We removed the error `title` and error `cause`, see section below for guidelines on error handling. If you were not using those fields there are no breaking changes, we advise in any case to follow the guidelines below to handle errors from PingOne Recognize SDK.

**Error handling guidelines**

Errors have a specific `type` that identifies the error, we are keeping the error code for backward compatibility. We advise you to use the error type to perform logic (for example, exhaustive iteration over the error "enums").

The error type or the code are useful to "categorize" the error and based on the error category suggest a path forward for the user see `Notes/Recommendations` in the error tables from [error handling](../mobile-sdk/mobile-sdk-error-handling.html).

We introduced a new field useful to debug the error: the `debuggingInfo: Map<String, String>` field.

|   |                                                                                                |
| - | ---------------------------------------------------------------------------------------------- |
|   | The `debuggingInfo` is intended for developers. Don't return the `debuggingInfo` to end users. |

We now propagate lower level error details in the `debuggingInfo`. The changes divided by error categories:

* KeylessIntegrationError:

  * `ConfigurationFailed` has been replaced by `InvalidConfiguration`.

  * `MissingLoggingConfiguration` has been removed.

  * `InvalidApiKey` subclass removed (invalid API key is now propagated as `InvalidConfiguration` and will contain the reason if the api key is invalid into the `debuggingInfo`).

  * `SdkDynamicLinkingMalformedPayload` renamed to `DynamicLinkingMalformedPayload`.

  * `InvalidClientState` added to the error types.

* KeylessInternalError

  * Nested Sdk open class has been replaced by top-level subclass `SdkGeneric`, again use the `debuggingInfo` for all the details.

* `UnableToConfigureLogging` had been replaced by `LoggingConfigurationFailed`.

* Added `BiomGeneric` and `CoreGeneric` errors: this helps categorize the underlying issue, then the code inside `debuggingInfo` will provide internal details on the issue.

* KeylessUserError

  * `Spoofing` has been replaced by `GenuinePresenceNotEstablished`.

  * `CameraPermissionNotGranted` has been renamed to `CameraPermissionDenied`.

  * `MaskDetected` -deprecated- has been removed.

  * `DeviceTampered` -deprecated- has been removed.

  * `OutdatedApp` has been added: indicates that the PingOne Recognize SDK version is too old to communicate correctly with the PingOne Recognize backend.

***

**5.92**

**Fixes**

* `IllegalStateException` unregistered `ActivityResultLauncher`

  * In some case with back navigation on Android the `ActivityResultLauncher` wasn't registered correctly because we called it on the `onActivityCreated` instead of `onActivityStarted`. We reverted back to calling the `registerForActivityResult` during `onActivityStarted` lifecycle hook.

***

**5.9.1**

**Highlights**

* **UI Feedback to center face**

  * The region of interest is now closer to the user face to facilitate the face positioning near the center of the screen.

**Anti-Inject variant**

*Only for customers using the PingOne Recognize Anti-Inject SDK variant*

* Updated the anti-inject library to 3.6.2-0: this will require the provisioning of new licenses (configFile).

* Fix for CERTIFICATE_VERIFICATION_ERROR being reported as potential malicious activity.

**5.8.12**

**Highlights**

* **Camera optimizations**

  * We enhanced the camera configuration to prioritize aspect ratio and resolution selection, also optimized the device format selection. We expect these changes to improve usability during authentication sessions.

* **Liveness plugins adjustments**

  * Liveness environment aware will fall back to an opportunistic selection strategy: if the device natively supports the characteristic to enable the liveness environment aware feature it will be enabled by default. This will not add friction on devices where the feature cannot be supported.

**5.8.6 Android - 5.8.7 iOS**

**Highlights**

* Filter & Liveness Enhancements: Introduced priority-based filter selection, smoothed filter transitions, and refined the visual feedback for the Region of Interest (ROI) based on filter states.

**Fixes**

* Fixed a bug to ensure the loading screen hides correctly on the main thread.

**Anti-Inject variant**

*Only for customers using the PingOne Recognize Anti-Inject SDK variant*

* We introduced validation logic to detect, log, and safely handle invalid SDK artifacts.

**5.8.0 Android**

* **Added Kotlin 2 and Ktor 3 support**

  * **Potential breaking changes -** *the adoption of Ktor 3 might result in a breaking change for SDK consumers, with some changes required in specific setups. The last known Ktor 2 version is [v2.3.13](https://github.com/ktorio/ktor/releases/tag/2.3.13), dated November 2024. Please follow the [official migration instructions](https://ktor.io/docs/migrating-3.html).*

**5.7.3**

**Highlights**

* **Live feedback for Authentication UI**

  * Instructions to guide the user to a successful authentication so that the user can address the liveness requirements in real time have now been added, as per the Enrollment UI.

* **Lighter touch Enrollment for Recovery flows**

  * We introduced a PresentationStyle configuration parameter for enrollment: it is now possible to perform an enrollment showing a UI that is similar to the authentication UI (acting as overlay on top of the customer application).

* **Multiple Secret support**

  * We now support more than one custom secret. It is possible to provide an identifier for a secret and store multiple secrets in the Keyless SDK.

* **Biometric Model update**

  * We continue to iterate on our biometric model with the goal of preventing malicious attacks.

**5.5.0**

**Anti-Inject variant**

*Only for customers using the Keyless Anti-Inject SDK variant*

* Biometric assets are now encrypted leveraging the Anti-Inject SDK signing functionalities.

**Fixes**

* Removed an issue where the SDK occasionally triggered a crash if the user tapped the "X" button at a specific point after the enrollment selfie had been captured.

***

**5.4.1**

**Deprecations**

* We updated our liveness levels naming as follows:

  | Before                     | After       |
  | -------------------------- | ----------- |
  | PASSIVE_STANDALONE_MEDIUM  | DEVELOPMENT |
  | PASSIVE_STANDALONE_HIGH    | LEVEL_1     |
  | PASSIVE_STANDALONE_HIGHEST | LEVEL_2     |

  The PASSIVE_STANDALONE\_\* values are now deprecated. The default is set to `LEVEL_1`. For details, refer to [Liveness Settings](../mobile-sdk/mobile-sdk-liveness-settings.html).

**Fixes**

* iOS: return PIN error instead of a generic error when the user enters the wrong PIN.

***

**5.4.0**

**Breaking Change**

* We updated the cloudsmith artifacts' naming convention, with a summary of the changes as follows:

```text
Android: from keyless-android-sdk to keyless-mobile-sdk

iOS (SPM): from keyless.KeylessSDK to keyless.mobile-sdk

iOS (CocoaPods): from KeylessSDK to keyless-mobile-sdk
```

Please follow [getting started](../mobile-sdk/mobile-sdk-getting-started.html) to fetch the latest version.

***

**5.3.3**

**Highlights**

* We have now switched the liveness environment aware configuration default to `livenessEnvironmentAware = false`. For more details, go to the [Liveness Settings](../mobile-sdk/mobile-sdk-liveness-settings.html) section.

***

**5.3.2**

**Anti-Inject variant**

*Only for customers using the Keyless Anti-Inject SDK variant*

* Fine-tune error `error code: 40002, error message: device might not be genuine` based on updated security level.

**5.3.1 iOS**

**Fixes**

* Avoid stripping debug symbols to run on iOS simulators.

***

**5.3.0**

**Highlights**

* The existing lockout policy is now applied for enrollment using the client state. See the [lockout policy](../mobile-sdk/mobile-sdk-lockout-policy.html) page for all details.

**Fixes**

* Improved Error Handling for Spoofing errors: the SDK will return a Rejected taking into consideration internal filters. The Rejected error will take precedence over the incorrect Spoofing error.

**Anti-Inject variant**

*Only for customers using the Keyless Anti-Inject SDK variant*

* Upon calling `Keyless.configure` you will now get an error if we detect that device is not genuine. The error is `error code: 40002, error message: device might not be genuine`. You shall redirect your users through a different flow since Keyless configuration will fail and it won't not possible to enroll or authenticate.

***

**5.2.1**

**Highlights**

* Introduced a **Client State** type for clearer Client State handling.

* This change means that on the [Keyless dashboard](https://dash.keyless.io/), customers using this SDK version and above will be able to see the type of "Keyless Client Devices" on the individual user pages.

* This clears up the confusion where "Devices" of the users were displayed but there was no way to distinguish bound client devices (now labelled 'Device Type: SDK) or client states stored or used by integrator to authenticate users in future using temporary or backup client states (Device Type: Temporary or Backup).

**Deprecations**

* **Temporary State** terminology is now deprecated in favor of **Client State**.

* Flows such as Enroll from Temporary State, for example, will be deprecated having made Enroll from Client State available as a direct replacement.

* This is to clean-up a legacy issue where the terms Temporary State and Client State were used interchangeably.

* From now on Client State is the preferred term and has two types: `Temporary` and `Backup`, and represents the non-PII data stored or leveraged by customers to support future authentications on Mobile or Web SDK, such as a [new device activation](../mobile-sdk/mobile-sdk-account-recovery.html) flow.

***

**5.2.0**

**Highlights**

* UI: optionally display a chip to show a loader before an authentication. This has been added as in some instances integrators have found there is a slight delay for the camera preview to open.

* Check the Authentication loading in the [Text UI customization](../mobile-sdk/mobile-sdk-ui-customization.html) section for more details.

**Fixes**

* Fix: For the error xMinPercentage is not in valid range \\\[0.0..1.0] - Region of interest will be full screen in case we get inconsistent values.

* Note we believe this error was particularly prevalent on foldable devices or tablets but should be largely resolved from this release onwards.

* Fix: update tensorflow to resolve a [known issue](https://github.com/tensorflow/tensorflow/issues/75815) that was causing a crash in a very low % of cases on android devices.

**Breaking changes**

* Removed the deprecated configuration builders. We believe that all of our customers have already moved to the remaining configuration: `SetupConfig`, `EnrollConfig`, `AuthConfig`, and `DeEnrollConfig` and therefore no action is required.

* Removed deprecated `UserInfo` APIs.

* Removed the possibility to specify a path to Keyless artifacts introduced in version [4.7.3](#mobile-sdk-4.7.3).

***

**5.1.4**

*Only for customers using the Networking module feature*

**Fixes**

* Fix (Android): camera deprecation issues on Samsung Galaxy A23.

* Fix (iOS): off-load networking module lockout request from the main thread.

***

**5.1.3**

*Only for customers using the Networking module feature*

**Fixes**

* Fix: additional call on protocol level for information on rate limited requests.

***

**5.1.2 Android**

**Highlights**

* 16 KB page size support - [official docs](https://developer.android.com/guide/practices/page-sizes).

***

**5.1.1**

**Highlights**

*Only for customers using the Keyless Anti-Inject variant for enhanced frames injection prevention*

* Build variant is available for selected customers through `partners-rasp`.

* Improved initialization performance for frames injection prevention to enhance the overall experience by reducing load times.

**Fixes**

* Fix (Android): camera resolution issues on Samsung Galaxy A23.

***

**5.1.0**

**Highlights**

* **Enrollment Frame**: Integrators can specify whether or not to retrieve an enrollment frame, acquired during the user's selfie capture during the enrollment or account recovery flow. See details in the [Enrollment Frame](../mobile-sdk/mobile-sdk-enrollment.html) section.

* **Enhanced Anti-Inject**: this release introduces a new option for enhanced injection attack prevention.

***

**5.0.5 iOS - 5.0.6 Android**

**Highlights**

* **Environment-Aware Liveness Detection**: a new, optional check has been introduced to enhance liveness detection, helping to ensure the user is in a suitable setting for verification. This feature is enabled by default. To disable it, set `livenessEnvironmentAware = false` in the configuration for enrollment, authentication, or de-enrollment. See details in the [Liveness Settings](../mobile-sdk/mobile-sdk-liveness-settings.html) section.

* **Face Occlusion Detection for Enrollment**: during the enrollment process, the SDK now provides immediate feedback to the user if their face is partially covered. A message, "Make sure your face is clearly visible," will be displayed to guide them..

**Fixes**

* Improved Error Handling for Temporary States: the SDK now returns a more specific internal error (`error code: 539`) if the maximum number of temporary states is reached during an operation.

* Added a Cancellation Button to the Camera View: an "x" button has been added to the top-left corner of the camera screen during enrollment, allowing users to safely cancel the face scan process.

***

**5.0.3**

**Highlights**

* **Enroll from photo preview**: This feature introduces the ability to enroll users using a photo provided from a trusted source.

* Developer Responsibility: You are responsible for ensuring that the photo originates from a verified and trusted source (for example, an official identity document).

* Security Note: Exposing this functionality to your end-users without rigorous verification of the photo's origin may introduce vulnerabilities, such as a user enrolling with another individual's facial image. Please implement appropriate safeguards.

**Enhancement: biometric processing**

* Improved biometric performance through optimizations in frame timestamp processing.

***

**5.0.1**

**Highlights**

* **New Enrollment UX**: a freshened up, new User Interface has been implemented and made available.

* It now displays **real-time feedback** about the quality of the processed image, allowing users to address the issues based on the messages shown during face capture.

* Note these messages aren't customizable since they 're tied to Keyless image processing.

* The **temporary state now displays the enrollment UI**. The change means that users will experience an onboarding flow as for plain enrollment (without temporary state).

* This change was made based on customer feedback in recognition of the fact that some users will be experiencing Keyless for the first time, specifically if they were enrolled with [IDV Bridge](../idv-bridge/idv-bridge-introduction.html).

* The UI differences are reported in the `SDK v5` tab of the [UI customization section](../mobile-sdk/mobile-sdk-ui-customization.html).

* **Fixes in this release**

* Added `showScreenFailureFlow` for consistency with the happy path `showScreenSuccessFlow`. By default the SDK shows an error screen for unhappy paths but the caller app can opt-out from this default behavior.

* Return an error if camera permission is not granted. Keyless prompts the user for camera permission and now also informs the caller app that permission was not granted returning the error `30009 - camera denied` .

* See [user errors](../mobile-sdk/mobile-sdk-error-handling.html#user-errors) for details of this and all other errors.

**Improved error handling and information**

Integrators familiar with our [error handling documentation](../mobile-sdk/mobile-sdk-error-handling.html) will notice that we have:

* Added more detailed insight and guidance for the different types of errors and the relevant error code ranges for integrators to be aware of.

* More clearly laid out the different types of User Errors with their codes & descriptions.

* **"Rejected" error -** we have split out instances where Liveness could not be established into a new "Rejected" error. Previously these were all labelled as "Spoofing" errors, however we recognized that in some instances these incorrectly added a framed the authentication attempt as more malicious than was fair.\ Please note, the guidance remains that all modelling is in some way predictive and therefore we would still advise that "Spoofing" does not guarantee that there was malicious intent and for various reasons it's still better to assume positive intent in how you handle these with users.

**SDK Size Reduction**

Following customer feedback, we have reduced the size of the biometric libraries which has reduced both the iOS and Android SDK integration and download size. Please note that integration size can vary significantly between customers so please contact us if you have questions in this area.

**Support for iOS emulator**

The Keyless iOS SDK can now be run on an iOS emulator on both Windows PC or Mac, allowing integrators to achieve faster develop and test cycles as they make changes.

**Deprecations**

* Liveness timeout no longer has effect and will be removed in future releases.

* This change was made given a set of comprehensive improvements to the Liveness biometrics models. We plan to support configuration options to support both faster and slower authentication and enrollment experiences in upcoming releases.

* The mobile SDK Lockout policy, which had some reported inconsistencies, is now managed on the backend so no longer has an effect and will be removed in future releases.

* This change was implemented based on customer feedback and done in conjunction with other changes:

* Client side errors (example Liveness failures) now are sent to the server side and will impact the server side policy.

* The server side policy can now be configured per customer tenant (max failed attempts, time period, suspension period). Speak to the Keyless team if you would like to review and change your lockout policy.

**Breaking changes**

* With the new UI, texts shown to the user have changed. If you are using text customization, make sure you update to the identifiers from the `SDK v5` [text section](../mobile-sdk/mobile-sdk-ui-customization.html).

* The API `showScreenSuccessFaceCapture` is no longer available since enrollment no longer considers the successful face capture step.

* The `successAnimationEnabled` and later `showScreenSuccessFlow` field has been renamed to `showSuccessFeedback`.

* The `showScreenFailureFlow` field has been renamed to `showFailureFeedback`.

* The `showScreenInstructions` field has been renamed to `showInstructionsScreen`.

* The enrollment progress `onProgress` callback is no longer available since progress is not shown with the updated UX.

***

**4.8.2 iOS - 4.8.3 Android**

**Highlights**

* Improved biometric performance.

* Improved error handling and information - [docs](../mobile-sdk/mobile-sdk-error-handling.html).

* SDK Size Reduction.

* Support for iOS emulator.

* Fix (Android): addressed biometric performance on Pixel devices.

* Fix (Android): on premise remove validate device before authenticate

**Improved error handling and information**

* **Introduced a new "Rejected" error -** we have split out instances where Liveness could not be established into a new "Rejected" error. Previously these were all labelled as "Spoofing" errors, however we recognized that in some instances these incorrectly added a framed the authentication attempt as more malicious than was fair.\ Please note, the guidance remains that all modelling is in some way predictive and therefore we would still advise that "Spoofing" does not guarantee that there was malicious intent and for various reasons it's still better to assume positive intent in how you handle these with users.

**SDK Size Reduction**

Following customer feedback, we have reduced the size of the biometric libraries which has reduced both the iOS and Android SDK integration and download size. Please note that integration size can vary significantly between customers so please contact us if you have questions in this area.

**Support for iOS emulator**

The Keyless iOS SDK can now be run on an iOS emulator on both Windows PC or Mac, allowing integrators to achieve faster develop and test cycles as they make changes.

***

**4.7.5 iOS - 4.7.6 Android**

**Highlights**

* Fix: fix client state retro compatibility with version >2.0.0 of the Keyless Agent

***

**4.7.4**

**Highlights**

* UX: optional screens - it is now possible to opt out of the optional screens you don't wish to show - [docs](../mobile-sdk/mobile-sdk-ui-customization.html)

* Enhancement: query remaining lockout time - [docs](../mobile-sdk/mobile-sdk-user-and-device-management.html#lockout-management)\\

  **UX: optional screens**

We understand that the experience our customers create for their end users is of the utmost importance. To provide greater flexibility, we've made certain screens and steps in the Authentication and Enrollment flows optional. These screens will remain visible by default, but you now have the ability to opt out of displaying those that aren't relevant to your workflow. You can find more details in the [documentation](../mobile-sdk/mobile-sdk-ui-customization.html).

Please note that the camera view and Step 2 ("Enrollment Progress") will remain mandatory for now, as they are critical to ensuring liveness detection and security during the capture process. However, Step 2 is highly customizable in terms of text and color scheme to align with your branding.

In upcoming releases, we will also be adding sample code and "User Flow" guides to further empower integrators and designers in tailoring their user experience.

**Enhancement: query remaining lockout time**

Customers can configure the maximum number of errors a user can make before being locked out for a 10-minute period.

Based on customer feedback, we've enhanced this feature to allow querying the remaining lockout time (in seconds) after a user has been locked out. For implementation details, refer to the [documentation](../mobile-sdk/mobile-sdk-user-and-device-management.html#lockout-management).

This enhancement enables customers to display the remaining lockout time to users at any given moment, improving transparency and user experience.

**Bugs and Fixes**

* **Fix (Android):** Resolved a compatibility issue between the Compose Material library and Flutter.

***

**4.7.3**

* UX: SDK Theme is customizable by customer - [docs](../mobile-sdk/mobile-sdk-ui-customization.html)

* Feature: possibility to specify a path to Keyless artifacts. Artifacts are provided by Keyless by default. Artifacts path can be overridden by the customer.

***

**4.7.2**

* Feature: improved PSD2 compliance - [docs](../mobile-sdk/mobile-sdk-dynamic-linking.html)

* Feature: account recovery - [docs](../mobile-sdk/mobile-sdk-account-recovery.html)

* Fix: remove lottie dependency

* UX: remove success animation in favor of static image

***

**4.7.0**

* API Surface: deprecate builder pattern in favor of optional config constructor parameters (builders are deprecated)

* Feature: expose SDK logs to customer app - [docs](../mobile-sdk/mobile-sdk-logging.html)

* Feature: expose JWT signature compatible with core backend key pairs - [docs](../mobile-sdk/mobile-sdk-jwt-signing.html)

***

**4.6.7**

* Bugfix: internal data cleanup

* Performance improvements: avoid unnecessary assets extraction

***

**4.6.6**

Feature: Shared Circuits: integrators can now set the desired number of shared circuits when calling an sdk configure Fix: Liveness: update liveness setting for higher security

***

**4.6.5**

* Feature: enroll with Keyless from an Auth0 user's IdToken

***

**4.6.3**

* Dynamic linking feature: new API exposing interface to choose one authentication method (BiomAuthConfig | PinAuthConfig)

* UI customization: it is now possible to customize the font for Keyless SDK screens

* UI customization: it is now possible to customize the brand color (primary accent color) for Keyless SDK screens

***

**3.2.0**

**Highlights**

* Accessibility improvements

* Security enhancements

***

**3.1.0**

**Highlights**

* Better biometric quality filters

* Improved performance on Android WebViews

* Support for returning the recognition frame

***

**3.0.0**

**Highlights**

* Upgrade to v2 HTTP API

* Better network stability

* Security improvements

***

**2.4.2**

**Fixes**

* Allows browser extensions to detect the PingOne Recognize Web SDK

***

**2.4.1**

**Fixes**

* Fix edge case with camera permissions

***

**2.4**

**Highlights**

* Active Face Quality Filters running on the client

**Deprecations**

* **\[Headless]** The `getLastKeylessFrameResults` function has been replaced by `getLastKeylessServerFrameResults`

* **\[Headless]** The `getLastKeylessFrameTriggeredBiometricFilters` function has been replaced by `getLastKeylessServerFrameTriggeredBiometricFilters`

**Breaking Changes**

* **\[Headless]** The SDK added the `CREATE_MEDIA_STREAM_ARGS_UNSET` error, which should be localized as a generic system error

* **\[Web Components]** The localization for the `kl-camera-tip` component and the `SERVER_RECOGNITION_FAILED` error has changed structure. To learn more, refer to [Localization](../web-sdk/web-sdk-reference-localization.html)

**New APIs**

* **\[Headless]** The `getLastKeylessServerError` function returns the last server error tied to the attempt

* **\[Headless]** The `getLastVideoFrameQuality` function returns the quality of the last video frame from the camera stream, the quality is computed on the client

* **\[Web Components]** The `kl-auth` and `kl-enroll` elements emit a new `video-frame-quality` event

***

**2.3.1**

**Highlights**

* Removes client-side Lockout Policy

**Breaking Changes**

* **\[Headless]** The `DEFAULT_KEYLESS_LOCKOUT_TIME`, `DEFAULT_KEYLESS_LOCKOUT_TOLERANCE` and `DEFAULT_KEYLESS_LOCKOUT_WINDOW` constants are no longer exported

* **\[Headless]** The `KeylessLockoutAttempt` and `KeylessLockoutOptions` interfaces are no longer exported

* **\[Headless]** The `getLastKeylessLockoutAttempt`, `etLockoutExpirationDate` and `getLockoutTime` functions are no longer exported

* **\[Headless]** The `getServerLockoutExpirationDate` function was renamed to `getKeylessServerLockoutExpirationDate`

* **\[Headless]** The lockout field in the `KeylessOptions` interface was removed

* **\[Web Components]** The `enable-lockout`, `lockout-time`, l\`ockout-tolerance\`. and `lockout-window` attributes are no longer available

**Fixes**

* Fix edge case with camera permissions

***

**2.3**

**Highlights**

* Passive Face Quality Filters running on the client

* Smaller WebAssembly binary size

* Better Remote Logging

**Deprecations**

* **\[Headless]** The `importKeylessWebAssemblyModule` function now optionally takes `url.binary` instead of `url.file` in the options argument

* **\[Web Components]** The `kl-auth` and `kl-enroll` elements now optionally take the `wasm-binary-url` attribute instead of `wasm-file-url`

**Breaking Changes**

* The `@keyless/sdk-web` and `@keyless/sdk-web-components` packages now include a `wasm.data` file, make sure to bundle it or the SDK will not work

***

**2.2.1**

**Fixes**

* Fix Firefox on Android unable to grant camera permissions

***

**2.2**

**Highlights**

* Single-Thread by default with opt-in Multi-Thread

* COEP/COOP Security Headers are no longer required by default

***

**2.1.2**

**Highlights**

* Faster Camera Startup Time

* Better Camera Permission Flow

***

**2.1.1**

**Fixes**

* Fix Operation ID Forwarding

***

**2.1**

**Highlights**

* CDN Distribution

* Prettier Web Components UI

* Better Tampering Protections

***

**2.0**

**Highlights**

* Better Headless APIs

* Tampering Protections