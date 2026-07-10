---
title: Native SDKs
description: The PingOne Native SDKs are iOS and Android client SDKs for PingOne services built to interact with the PingOne Platform API. Currently, native PingOne SDKs are available for these services:
component: pingone-api
page_id: pingone-api:native-sdks:introduction
canonical_url: https://developer.pingidentity.com/pingone-api/native-sdks/introduction.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
page_aliases: ["index.adoc"]
section_ids:
  assigning-admin-roles-and-permissions-to-this-service: Assigning admin roles and permissions to this service
---

# Native SDKs

The PingOne Native SDKs are iOS and Android client SDKs for PingOne services built to interact with the PingOne Platform API. Currently, native PingOne SDKs are available for these services:

* [PingOne MFA](pingone-mfa-mobile-sdks.html)

* [PingOne Neo](pingone-neo-native-sdks.html)

* [PingOne Protect](pingone-risk-sdks/risk_evaluation_sdk.html)

To integrate your mobile and web apps with PingOne DaVinci, or for OIDC redirect login, refer to the [Ping SDKs](https://docs.pingidentity.com/sdks/latest/index.html).

## Assigning admin roles and permissions to this service

Admin role assignments determine access to PingOne APIs. When assigning admin roles to this service, refer to [PingOne Permissions by Service](../platform/reference/roles-and-permissions-in-pingone/permissions-by-service.html) for the service-specific permissions.

You can also choose to assign admin roles based on particular service resources. Refer to [PingOne Permissions by Resource](../platform/reference/roles-and-permissions-in-pingone/permissions-by-resource.html) when assigning admin roles per service resources.

Admin assignments to roles are set by:

* [Automatic assignment for some roles](../platform/roles/predefined-roles.html#automatic-role-assignment).

* [Group Role Assignments](../platform/group-role-assignments/group-role-assignments.html).

* [User Role Assignments](../platform/users/user-role-assignments.html).

Refer to [Roles Management](../platform/roles.html) for more information.

---

---
title: PingOne MFA Native SDK flows
description: The automatic enrollment flow requires as little as one extra step from the user. The first time the user logs into an application which has an embedded PingOne Native SDK component, they are asked if they wish to trust that device. Once they approve, PingOne works behind the scenes, without requiring anything else from the user.
component: pingone-api
page_id: pingone-api:native-sdks:pingone-mfa-mobile-sdks/pingone-mfa-mobile-sdk-flows
canonical_url: https://developer.pingidentity.com/pingone-api/native-sdks/pingone-mfa-mobile-sdks/pingone-mfa-mobile-sdk-flows.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  pairing-automatic-enrollment: Pairing - automatic enrollment
  implement-automatic-pairing-of-native-app-as-mfa-authenticator-app: Implement automatic pairing of native app as MFA authenticator app
  admin-tasks: Admin tasks
  developer-tasks: Developer tasks
  automatic-device-authorization: Automatic device authorization
  implement-automatic-device-authorization: Implement automatic device authorization
  admin-tasks-2: Admin tasks
  developer-tasks-2: Developer tasks
  authentication-code-flow: Authentication code flow
  implement-an-authentication-code-flow: Implement an authentication code flow
  admin-tasks-3: Admin tasks
  developer-tasks-3: Developer tasks
  automatic-unpairing-of-device-if-mobile-app-uninstalled: Automatic unpairing of device if mobile app uninstalled
---

# PingOne MFA Native SDK flows

## Pairing - automatic enrollment

The automatic enrollment flow requires as little as one extra step from the user. The first time the user logs into an application which has an embedded PingOne Native SDK component, they are asked if they wish to trust that device. Once they approve, PingOne works behind the scenes, without requiring anything else from the user.

During user authentication, a native app communicates with the PingOne platform to generate a token. The token allows pairing the device to the user in the context of a customer application. The user is not required to type or scan anything.

![A diagram showing the PingOne Mobile SDK automatic enrollment flow.](../../_images/p1_MobileSDKFlowAutoEnroll.png)

1. The user is identified on the customer native application, usually with a unique user identifier, for example, a username.

2. The PingOne Native SDK returns a native payload to the customer native application. The payload is a small data package created by the PingOne Native SDK component, which is used as part of the device's authorization.

3. The customer native application sends an authentication request to the PingOne Platform, including the native payload.

4. The customer native application receives an ID token.

5. The customer native application passes the ID token to the PingOne Native SDK.

6. The PingOne Native SDK returns a pairing object to the customer native application, to pair or ignore the device.

7. The customer native application prompts the user for the approve or deny action via a dialog. Based on the user's choice, the customer native application notifies PingOne Native SDK.

8. The PingOne Native SDK completes the transaction accordingly, by communicating directly with PingOne Platform.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | **Note:** If you have enabled auto-enrollment, there may be situations where authentication succeeds but registration is unsuccessful for various reasons. One such scenario would be a situation where you have limited the number of authentication methods that a user can define, and when the user authenticated with your mobile application, they passed the maximum number of allowed methods. Keep in mind that in such cases, the user will not be aware that registration has failed. |

### Implement automatic pairing of native app as MFA authenticator app

In order to enable automatic pairing of a native app as an MFA authenticator app, there are several tasks that must be coordinated between admin and developers.\
In brief, you will do the following:

* Create a native application with Authenticator configuration.

* Configure a sign-on policy containing an MFA step that references an MFA policy where the native application is configured as an authenticator.

* Assign the sign-on policy to the native app.

* Write code in the application to support automatic app enrollment.

Follow the detailed steps below:

Supply the relevant details for the admin to do the following in the PingOne admin console:

#### Admin tasks

1. Create a native app. Refer to [Add an application - Native](https://docs.pingidentity.com/pingone/applications/p1_applications_add_applications.html).

2. In [Edit an application](https://docs.pingidentity.com/pingone/applications/p1_edit_application_native.html), on the **Mobile** tab:

   * Add the **Package name** (Android) and **Bundle ID** (iOS) of your native application.

   * Configure the push credentials per platform.

3. Create a new MFA policy.

4. In the MFA policy, use the **Add Application** option to select the name of your mobile app. In the settings for the app you added, select the Auto Enrollment option.

5. Create a sign-on policy, and add an MFA step. Refer to [Add an authentication policy](https://docs.pingidentity.com/pingone/authentication/p1_add_an_auth_policy.html).

6. In the MFA step, select the MFA policy that you configured. Also, if you want to allow automatic enrollment even if the user does not have any existing paired devices, set the "NONE OR INCOMPATIBLE METHODS" setting to Bypass.

7. Return to the **Applications** page and edit your mobile application. On the **Policies** tab, choose the sign-on policy that you created. This is necessary so that the authenticator element of your application will be launched when users try to access the application.

#### Developer tasks

In your native application code (also described in the iOS and Android README.md files, refer to [PingOne Native SDK for iOS](https://github.com/pingidentity/pingone-mobile-sdk-ios) or [PingOne Native SDK for Android](https://github.com/pingidentity/pingone-mobile-sdk-android)):

1. Get the native payload from the SDK (`PingOne.generateMobilePayload()`)

2. Pass the received payload of the OIDC request to the authorization service, as the `mobilePayload` query parameter.

3. Call `processIdToken()` with the token you received from PingOne platform.

4. If automatic pairing is triggered (i.e. the user was not already paired with the device), `processIdToken()` will return a pairing object with `approve()` and `deny()` functions. Calling `approve()` will pair the user with the device.

## Automatic device authorization

During automatic device authorization, a native app communicates with the PingOne platform to generate a token. The token allows authenticating the user device in the context of a customer application. The user is not aware of this, and is not required to type or scan anything.

![A diagram showing the PingOne Mobile SDK automatic device authorization flow.](../../_images/p1_MobileSDKFlowAutoAuthorize.png)

1. The customer native app requests a native payload from the PingOne Native SDK.

2. The PingOne Native SDK returns a native payload to the customer native application.

3. The customer native application sends an authentication request to the PingOne Platform, including the native payload.

4. If the platform's authentication flow (sign-on policy) contains an MFA step, and extra verification is disabled, the platform verifies that the native device is paired and active, authenticates the native device, and the MFA step succeeds. The flow skips to step 9.

5. The platform verifies that the native device is paired and active and sends a "silent" push notification to the native application via the APNS/GCM notification service.

6. The native application passes the "silent" notification to the PingOne Native SDK.

7. The PingOne Native SDK acknowledges receiving the "silent" push by sending a confirmation directly to the PingOne platform.

8. The platform authenticates the native device, and the MFA step succeeds.

9. The customer native application receives an ID token from the PingOne Platform.

10. The customer native application passes the ID token to the PingOne Native SDK.

11. The PingOne Native SDK returns null to the customer native application, indicating that authorization has completed and no further action needs to be taken.

### Implement automatic device authorization

#### Admin tasks

The admin configuration that was implemented for automatic enrollment, is applied to automatic device authorization.

1. Create a native app, or edit an existing app. Refer to [Add an application - Native](https://docs.pingidentity.com/pingone/applications/p1_applications_add_applications.html).

2. In [Edit an application](https://docs.pingidentity.com/pingone/applications/p1_edit_application_native.html), on the **Mobile** tab:

   * Add the **Package name** (Android) and **Bundle ID** (iOS) of your native application.

   * Configure the push credentials per platform.

3. Create a new MFA policy.

4. In the MFA policy, use the Add Application option to select the name of your mobile app. In the settings for the app you added, enable **Device Authorization**. In the Extra Verification drop-down list, you can optionally select Permissive or Restrictive. For details on these two options, refer to [Adding an MFA policy](https://docs.pingidentity.com/pingone/authentication/p1_creating_an_mfa_policy.html).

5. Create a sign-on policy, and add an MFA step. Refer to [Add an authentication policy](https://docs.pingidentity.com/pingone/authentication/p1_add_an_auth_policy.html).

6. In the MFA step, select the MFA policy that you configured.

7. Return to the Applications page and edit your mobile application. On the Policies tab, choose the sign-on policy that you created. This is necessary so that the MFA policy you configured and included in the sign-on policy will be applied when users try to access the application.

#### Developer tasks

In your native application code (also described in the iOS and Android README.md files, refer to [PingOne Native SDK for iOS](https://github.com/pingidentity/pingone-mobile-sdk-ios) or [PingOne Native SDK for Android](https://github.com/pingidentity/pingone-mobile-sdk-android)):

1. Get the native payload from the SDK (`PingOne.generateMobilePayload()`)

2. Pass the received payload of the OIDC request to the authorization service, as the `mobilePayload` query parameter.

3. Call `processIdToken()` with the token you received from PingOne platform.

4. If device authorization is triggered (i.e. verification that the user's device is already paired and active), `processIdToken()` will return null, indicating that authorization has completed and no further action needs to be taken.

[]()

## Authentication code flow

The authentication code flow enables users to sign on without any data entry, such as providing a username, password, or entering a one-time passcode. The user scans the code, and if successful, gains access to an application's services.

During an authentication code flow, a native app communicates with the PingOne platform to initiate authentication with an authentication code, which can be a QR code. The flow starts with a call to the [Create Authentication Code](/pingone/mfa/v1/api/#post-create-authentication-code) endpoint. The Mobile SDK validates the code value and returns an `AuthenticationObject` to the mobile app.

![A diagram showing the PingOne Mobile SDK authentication code flow.](../../_images/p1_MobileSDKFlowQRAuthentication.png)

1. The customer mobile app requests an authentication code flow from the PingOne Mobile SDK.

2. The Mobile SDK requests validation of the authentication code value from the PingOne platform.

3. If the authentication code value is validated by the PingOne platform, the Mobile SDK creates an `AuthenticationObject`.

4. The Mobile SDK returns the `AuthenticationObject` to the customer mobile app.

5. If the `status` property value of the `AuthenticationObject` is `CLAIMED`, the flow continues. For all other `status` values, the flow ends.

6. If the number of users is two or more, the flow presents the user with an option to choose a specific user from the list. If the `AuthenticationObject` specifies only one user, the flow continues without requiring this step.

7. If the user approval setting has a value of `REQUIRED`, the mobile app prompts the user to approve or deny the current authentication session. If user approval is set to `NOT_REQUIRED`, the authentication flow skips this step.

8. The customer mobile app makes a validation request to the Mobile SDK.

9. The Mobile SDK claims authentication with the selected user and queries the PingOne server.

10. The PingOne server returns an authentication status.

### Implement an authentication code flow

#### Admin tasks

To configure direct triggering of the mobile application in an authentication code flow:

1. Create a native app, or edit an existing app. Refer to [Add an application - Native](https://docs.pingidentity.com/pingone/applications/p1_applications_add_applications.html).

2. Use the Authenticator tab to allow mobile authentication for the app. If your organization uses the PingOne MFA SDK to allow authentication with a QR code in certain flows, the admin can optionally configure a universal link or schema app link to enable direct triggering of the mobile application when scanning a QR code with a QR scanner. Refer to [Editing an application - Native](https://docs.pingidentity.com/pingone/applications/p1_edit_application_native.html).

#### Developer tasks

In your native application code (also described in the iOS and Android README.md files, refer to [PingOne Native SDK for iOS](https://github.com/pingidentity/pingone-mobile-sdk-ios) or [PingOne Native SDK for Android](https://github.com/pingidentity/pingone-mobile-sdk-android)):

1. Pass the retrieved authentication code to the mobile SDK by calling `PingOne.authenticate()`.

2. Parse the retrieved `AuthenticationObject`. If the status field equals `CLAIMED`, proceed to the next step.

3. If the number of users is more than one and/or the value of the field `needsApproval` equals `REQUIRED`, the `AuthenticationObject` will contain `approve()` and `deny()` options.

4. Call the `approve()` method of the `AuthenticationObject` with the corresponding `userId` to complete the authentication.

## Automatic unpairing of device if mobile app uninstalled

If a user who has already paired a device uninstalls the mobile app, PingOne responds to the unanswered push by automatically unpairing the device and removing it from the user's device list.

This mechanism uses the response received from the Google and Apple notification servers.

Note that Apple does not guarantee a specific response to push notifications after an application is uninstalled, so this feature may not always work on iOS devices.

In situations where an *unregistered* response is not received from the Google or Apple notification server, MFA flows will continue to prompt for push confirmation, and this may result in a status of PUSH\_CONFIRMATION\_TIMED\_OUT.

---

---
title: PingOne MFA Native SDKs
description: The PingOne Native SDK provides the ability to integrate PingOne MFA functionality into your native applications. Topics include:
component: pingone-api
page_id: pingone-api:native-sdks:pingone-mfa-mobile-sdks
canonical_url: https://developer.pingidentity.com/pingone-api/native-sdks/pingone-mfa-mobile-sdks.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
---

# PingOne MFA Native SDKs

The PingOne Native SDK provides the ability to integrate PingOne MFA functionality into your native applications. Topics include:

* [PingOne MFA Native SDK flows](pingone-mfa-mobile-sdks/pingone-mfa-mobile-sdk-flows.html)

* [PingOne Native SDK for Android](pingone-mfa-mobile-sdks/pingone-mfa-mobile-sdk-for-android.html)

* [PingOne Native SDK for iOS](pingone-mfa-mobile-sdks/pingone-mobile-sdk-for-ios.html)

* [PingOne MFA SDK error codes](pingone-mfa-mobile-sdks/pingone_mfa_sdk_errror_codes.html)

---

---
title: PingOne MFA SDK error codes
description: The pairing object always returns both a push authenticator status and an OTP status. If the status is FAILED, a Push authenticator error code and message or an OTP error code and message is returned with the status.
component: pingone-api
page_id: pingone-api:native-sdks:pingone-mfa-mobile-sdks/pingone_mfa_sdk_errror_codes
canonical_url: https://developer.pingidentity.com/pingone-api/native-sdks/pingone-mfa-mobile-sdks/pingone_mfa_sdk_errror_codes.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  pairing-object-error-codes: Pairing object error codes
  push-authenticator-error-codes: Push authenticator error codes
  otp-error-codes: OTP error codes
---

# PingOne MFA SDK error codes

## Pairing object error codes

The pairing object always returns both a push authenticator status and an OTP status. If the status is `FAILED`, a *Push authenticator error code and message* or an *OTP error code and message* is returned with the status.

## Push authenticator error codes

| Error code                                                      | Description                                                                                                                                                                                                                                                             |
| --------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Any error string returned from APNS, for example `Unregistered` | Refer to more error codes and descriptions in [Handling notification responses from APNs](https://developer.apple.com/documentation/usernotifications/setting_up_a_remote_notification_server/handling_notification_responses_from_apns) in the Apple developer portal. |
| Any error string returned from FCM, for example `Unregistered`  | Refer to more error codes and descriptions in [Error codes for FCM failure conditions](https://firebase.google.com/docs/reference/fcm/rest/v1/ErrorCode) in the Firebase portal.                                                                                        |
| `MissingPushCredentials`                                        | There are no push credentials on the PingOne server.                                                                                                                                                                                                                    |
| `MissingDeviceToken`                                            | There is no device token on the PingOne server.                                                                                                                                                                                                                         |
| `PushDisabled`                                                  | The push was disabled via the native SDK API.                                                                                                                                                                                                                           |

## OTP error codes

| Error code                       | Description                                                                                                                                        |
| -------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| `OneTimePasscodeRetriesExceeded` | On device pairing, the OTP can be verified within 3 attempts. On `checkOTP`, the OTP can be verified within 3 attempts in every 15 minutes.        |
| `InvalidOneTimePasscode`         | The user entered an invalid OTP.                                                                                                                   |
| `OneTimePasscodeExpired`         | On device pairing, the OTP can be verified within 15 minutes. On `checkOTP`, there are no limitations except for `OneTimePasscodeRetriesExceeded`. |
| `UnSynchronizedClock`            | The native clock not synchronized with the generated secret.                                                                                       |

---

---
title: PingOne MFA SDK for Android
description: The PingOne MFA Native SDK provides the ability to integrate PingOne MFA functionality into your native applications.
component: pingone-api
page_id: pingone-api:native-sdks:pingone-mfa-mobile-sdks/pingone-mfa-mobile-sdk-for-android
canonical_url: https://developer.pingidentity.com/pingone-api/native-sdks/pingone-mfa-mobile-sdks/pingone-mfa-mobile-sdk-for-android.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  overview: Overview
  pingone-mfa-native-sdk-sample-app: PingOne MFA Native SDK sample app
  authenticator-sample-app: Authenticator sample app
  mobile-device-integrity-check: Mobile device integrity check
  mobile-device-integrity-check-admin-ui-configuration: Mobile device integrity check - admin UI configuration
  mobile-device-integrity-check-android-implementation: Mobile device integrity check - Android implementation
  pingone-mfa-native-sdk-api-android: PingOne MFA Native SDK API - Android
---

# PingOne MFA SDK for Android

## Overview

The PingOne MFA Native SDK provides the ability to integrate PingOne MFA functionality into your native applications.

The PingOne MFA Native SDK API for Android is included in the SDK package. The functions, parameters and error codes are listed below.

The PingOne MFA Native SDK package is available for download at <https://github.com/pingidentity/pingone-mobile-sdk-android>. Further details for setup and integrating PingOne MFA Native SDK into your native apps are available in the [README](https://github.com/pingidentity/pingone-mobile-sdk-android/blob/master/README.md) file in the Android folder of the downloadable package.

The PingOne MFA SDK for Android supports the following software versions:

* Android 9 (API 28) and above

Refer to [Edit an application](https://docs.pingidentity.com/pingone/applications/p1_edit_application_native.html) in the admin guide for the server-side configuration steps.

|   |                                                                                                           |
| - | --------------------------------------------------------------------------------------------------------- |
|   | When developing applications for Android, you must use version 2.0.0 or later of the MFA SDK for Android. |

## PingOne MFA Native SDK sample app

The PingOne MFA Native SDK bundle provides a sample app that includes all the basic flows in order to help you get started.

The sample app package for Android is available for download at <https://github.com/pingidentity/pingone-mobile-sdk-android>. Further details are available in the [README](https://github.com/pingidentity/pingone-mobile-sdk-android/blob/master/README.md) file in the Android folder of the downloadable package.

## Authenticator sample app

The Authenticator sample app is a native app that has the sole function of performing strong authentication. It provides a simple example for developers and solution architects, to enable easy and rapid deployment of an authenticator app with minimal effort.

For scenarios which solely require creation of a native authenticator rather than a full native app, the Authenticator sample app offers a passwordless and secured solution, that only requires compilation of the sample with customer's branding and credentials, and uploading it to the app store.

The Authenticator sample app package for Android is available for download at <https://github.com/pingidentity/pingone-authenticator-sample-app-android/>.

## Mobile device integrity check

PingOne has an integrated mobile device integrity check in its MFA flows, which allows mobile applications to deny access when a mobile device is suspected to be compromised.

### Mobile device integrity check - admin UI configuration

Each application must be set up and configured in the organization's PingOne environment, either in the admin UI, or using the MFA devices API. The development team provides the admin with the application name and details.

The admin's configuration of device integrity detection is detailed in the PingOne admin guide. Refer to [Editing an application - Native](https://docs.pingidentity.com/pingone/applications/p1_edit_application_native.html).

### Mobile device integrity check - Android implementation

PingOne uses Google's Play Integrity API to check the integrity of the mobile device. For details on the capabilities of the Play Integrity API, refer to the [Play Integrity API documentation](https://developer.android.com/google/play/integrity).

Mobile app developers are responsible for enabling and monitoring usage of the Play Integrity API.

The following steps are required:

1. Create a Google Cloud project or use an existing one\
   For details on working with Google Cloud projects, refer to [Creating and managing projects](https://cloud.google.com/resource-manager/docs/creating-managing-projects). The PingOne mobile SDK component requires the number of your Google Cloud project.

2. Enable the Google Play Integration API\
   Go to *APIs and Services* and select *Enable APIs and Services*. Search for the Play Integrity API, select it, and then select *Enable*.

3. Link your application to the Google Cloud project\
   Applications distributed on Google Play must be linked to the Google Cloud project so that they can call the Play Integrity API. In the developer console of the Google Play Store, choose your application. Go to Setup > App integrity > Google Cloud Project, and link your application to the Google Cloud project where you've enabled the Play Integrity API.

4. Configure how your responses are encrypted and decrypted (optional)\
   For applications distributed on Google Play, you can choose between Google-managed response encryption (the default and recommended option) and self-managed response encryption. For both of these options, you'll need to provide the relevant keys in the PingOne console when you define the application. Refer to [Configure how your responses are encrypted and decrypted](https://developer.android.com/google/play/integrity/setup#configure-response-encryption) for more information on managing and downloading response encryption keys.

5. Monitor Play Integrity API usage\
   If your quota for Play Integrity API usage is reached, users could end up getting blocked. So it's important to monitor Play Integrity usage. For more information on usage tiers and requesting a higher quota, refer to [API usage tiers](https://developer.android.com/google/play/integrity/overview#usage-tiers).

6. Request a higher quota if needed\
   The form for requesting a move to a higher usage tier includes questions that are application-dependent. For the question *How are you calling the Play Integrity API?*, select the *A third party I'm using in the app is calling the API* option, and specify *PingOne Mobile SDK Android*.

7. Estimate the number of queries per day to request a specific tier\
   The quota request should take into account both your application's expected traffic and the mobile SDK component's caching and retry policy. If there was a successful response from the Play Integrity API that passed the integrity test, no additional Play Integration requests will be made until after the integrity check cache duration that you defined for the application.

## PingOne MFA Native SDK API - Android

Refer to the [API documentation](https://pingidentity.github.io/pingone-mobile-sdk-android/index.html).

---

---
title: PingOne MFA SDK for iOS
description: The PingOne MFA Native SDK provides the ability to integrate PingOne MFA functionality into your native applications.
component: pingone-api
page_id: pingone-api:native-sdks:pingone-mfa-mobile-sdks/pingone-mobile-sdk-for-ios
canonical_url: https://developer.pingidentity.com/pingone-api/native-sdks/pingone-mfa-mobile-sdks/pingone-mobile-sdk-for-ios.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  overview: Overview
  pingone-mfa-native-sdk-sample-app: PingOne MFA Native SDK sample app
  authenticator-sample-app: Authenticator sample app
  mobile-device-integrity-check: Mobile device integrity check
  mobile-device-integrity-check-admin-ui-configuration: Mobile device integrity check - admin UI configuration
  pingone-mfa-native-sdk-api-ios: PingOne MFA Native SDK API - iOS
---

# PingOne MFA SDK for iOS

## Overview

The PingOne MFA Native SDK provides the ability to integrate PingOne MFA functionality into your native applications.

The PingOne MFA Native SDK API for iOS is declared in the `PingOne.h` header file included in the SDK package. This header file (replicated below) includes descriptions for all functions, parameters and error codes.

The PingOne MFA Native SDK package is available for download at <https://github.com/pingidentity/pingone-mobile-sdk-ios>. Further details for setup and integrating PingOne MFA Native SDK into your native apps are available in the [README](https://github.com/pingidentity/pingone-mobile-sdk-ios/blob/master/README.md) file.

The PingOne SDK for iOS supports the following software versions:

* Xcode 14 or later

* iOS 15.0 or later

Refer to [Edit an application](https://docs.pingidentity.com/pingone/applications/p1_edit_application_native.html) in the admin guide for the server-side configuration steps.

|   |                                                                                                   |
| - | ------------------------------------------------------------------------------------------------- |
|   | When developing applications for iOS, you must use version 2.0.0 or later of the MFA SDK for iOS. |

## PingOne MFA Native SDK sample app

The PingOne MFA Native SDK bundle provides a sample app that includes all the basic flows in order to help you get started.

The sample app package for iOS is available for download at <https://github.com/pingidentity/pingone-mobile-sdk-ios>. Further details are available in the [README](https://github.com/pingidentity/pingone-mobile-sdk-ios/blob/master/README.md) file.

## Authenticator sample app

The Authenticator sample app is a native app that has the sole function of performing strong authentication. It provides a simple example for developers and solution architects, to enable easy and rapid deployment of an authenticator app with minimal effort.

For scenarios which solely require creation of a native authenticator rather than a full native app, the Authenticator sample app offers a passwordless and secured solution, that only requires compilation of the sample with customer's branding and credentials, and uploading it to the app store.

The Authenticator sample app package for iOS is available for download at <https://github.com/pingidentity/pingone-authenticator-sample-app-ios>. Further details are available in the [README](https://github.com/pingidentity/pingone-authenticator-sample-app-ios/blob/master/README.md) file.

## Mobile device integrity check

PingOne has an integrated mobile device integrity check in its MFA flows, that allows mobile applications to deny access when a mobile device is suspected to be compromised.

### Mobile device integrity check - admin UI configuration

Each application must be set up and configured in the organization's PingOne environment, either in the admin UI, or using the MFA devices API. The development team provides the admin with the application name and details.

The admin's configuration of device integrity detection is detailed in the PingOne admin guide. Refer to [Editing an application - Native](https://docs.pingidentity.com/pingone/applications/p1_edit_application_native.html).

## PingOne MFA Native SDK API - iOS

Refer to the [API documentation](https://pingidentity.github.io/pingone-mobile-sdk-ios/documentation/pingonesdk).

---

---
title: PingOne Neo Native SDKs
description: PingOne Neo is a decentralized identity solution that gives control of identity data back to users. PingOne Neo empowers businesses to give their users full control over how they securely store and share verified credentials without unnecessary friction.
component: pingone-api
page_id: pingone-api:native-sdks:pingone-neo-native-sdks
canonical_url: https://developer.pingidentity.com/pingone-api/native-sdks/pingone-neo-native-sdks.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
---

# PingOne Neo Native SDKs

PingOne Neo is a decentralized identity solution that gives control of identity data back to users. PingOne Neo empowers businesses to give their users full control over how they securely store and share verified credentials without unnecessary friction.

PingOne Neo provides enterprises with identity verification capabilities and the capability to issue identity claims for users to store in their wallet app and verify user data. Embed personal identity using these SDKs into a service to issue digital cards to users and let them store verifiable, shareable data in their wallet app.

PingOne Neo has two components:

* [PingOne Verify Native SDKs](pingone-neo-native-sdks/pingone-verify-native-sdks.html)

* [PingOne Wallet Native SDKs](pingone-neo-native-sdks/pingone-wallet-native-sdks.html)

---

---
title: PingOne Protect Native SDKs
description: You can use the PingOne Signals (Protect) SDK to obtain information for additional risk-related variables and then pass this information on to the risk evaluation.
component: pingone-api
page_id: pingone-api:native-sdks:pingone-risk-sdks/risk_evaluation_sdk
canonical_url: https://developer.pingidentity.com/pingone-api/native-sdks/pingone-risk-sdks/risk_evaluation_sdk.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
---

# PingOne Protect Native SDKs

You can use the PingOne Signals (Protect) SDK to obtain information for additional risk-related variables and then pass this information on to the risk evaluation.

The data provided by the Signals SDK can be used with the following:

* [PingOne Protect Integration Kit for PingFederate](https://docs.pingidentity.com/integrations/pingone/pingone_protect_integration_kit/pf_p1_protect_ik_integrating_device_profiling.html)

* [PingOne Risk Integration Kit for PingFederate (versions 1.3.1 or 1.3)](https://docs.pingidentity.com/integrations/pingone/pingone_risk_integration_kit/pf_p1_risk_ik_integrating_device_profiling.html)

* [PingOne Protect API](../../protect/risk-evaluations/create-risk-evaluation.html)

* [PingOne DaVinci flows that use the PingOne Protect connector](https://docs.pingidentity.com/connectors/p1_protect_connector.html)

* [PingOne Advanced Identity Cloud journeys that include PingOne Protect authentication nodes](https://docs.pingidentity.com/pingoneaic/integrations/pingone-protect.html)

---

---
title: PingOne Protect SDK for Android
description: Using the Android version of the SDK involves the following steps:
component: pingone-api
page_id: pingone-api:native-sdks:pingone-risk-sdks/risk_evaluation_sdk_android
canonical_url: https://developer.pingidentity.com/pingone-api/native-sdks/pingone-risk-sdks/risk_evaluation_sdk_android.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  pingone-signals-protect-sdk-for-android-version-5-2-0: PingOne Signals (Protect) SDK for Android (version 5.2.0)
  adding-the-sdk-to-your-app-dependencies: Adding the SDK to your app dependencies
  sdk-initialization: SDK initialization
  getting-the-data-for-risk-assessment: Getting the data for risk assessment
---

# PingOne Protect SDK for Android

## PingOne Signals (Protect) SDK for Android (version 5.2.0)

Using the Android version of the SDK involves the following steps:

* Adding Maven Central repository

* Adding the SDK to your app dependencies

* Initializing the SDK

* Getting the data for risk assessment

### Adding the SDK to your app dependencies

Add the following to your application-level build.gradle file:

|   |                                                                                                                                        |
| - | -------------------------------------------------------------------------------------------------------------------------------------- |
|   | Update the path to match the version of the PingOne Signals SDK for Android that you are using. Currently the latest version is 5.2.0. |

`implementation "com.pingidentity.signals:android-sdk:5.2.0"`

### SDK initialization

Extend the `Application` class and add the following in the `onCreate` method:

```none
public class MyApplication extends Application {

    @Override
    public void onCreate() {
        super.onCreate();

        // optional
        PingOneSignals.setInitCallback(new InitCallback() {
            @Override
            public void onError(@NonNull String message, @NonNull String code, @NonNull String id) {
                Log.i("PingOneSignals", "onError " + message + " code: " + code + " id: " + id);
            }

            @Override
            public void onInitialized() {
                Log.i("PingOneSignals ", "SDK Initialized");
            }
        });

      POInitParams initParams = new POInitParams();
      initParams.setEnvId(<envId>); // optional
      // If you are using the PingFed authentication API and version 1.3 of the Integration Kit, uncomment the following line to turn off the collection of behavioral data
      // initParams.setBehavioralDataCollection(false);
      PingOneSignals.init(this, initParams);
    }
}
```

|   |                                                                                                                   |
| - | ----------------------------------------------------------------------------------------------------------------- |
|   | The code above contains the String placeholder <\`envId\`>. Replace this with the ID of your PingOne environment. |

Optionally, set an event listener to get calls on successful or failed SDK initialization.

### Getting the data for risk assessment

Get the data for risk assessment by adding a call to the SDK's `getData` method, and pass as a parameter a class that implements the `GetDataCallback` interface, for example:

```none
import com.pingidentity.signalssdk.sdk.GetDataCallback;
import com.pingidentity.signalssdk.sdk.SignalsCollection;

public class MyClass {

    public void callGetData() {
          PingOneSignals.getData(new GetDataCallback() {
                   @Override
                     public void onSuccess(@NonNull String data) {
                              Log.i("PingOneSignals ", "data:  " + data);
                      }

                    @Override
                    public void onFailure(@NonNull String reason) {
                             Log.i("PingOneSignals ", "onFailure reason: " + reason);
                    }
           });
    }
}
```

---

---
title: PingOne Protect SDK for iOS
description: Using the iOS version of the SDK involves the following steps:
component: pingone-api
page_id: pingone-api:native-sdks:pingone-risk-sdks/risk_evaluation_sdk_ios
canonical_url: https://developer.pingidentity.com/pingone-api/native-sdks/pingone-risk-sdks/risk_evaluation_sdk_ios.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  pingone-signals-protect-sdk-for-ios-version-5-4-0: PingOne Signals (Protect) SDK for iOS (version 5.4.0)
  adding-the-sdk-to-your-app: Adding the SDK to your app
  adding-the-sdk-to-your-app-using-cocoapods: Adding the SDK to your app using CocoaPods
  adding-the-sdk-to-your-app-using-swift-package-manager: Adding the SDK to your app using Swift Package Manager
  sdk-initialization: SDK initialization
  getting-the-data-for-risk-assessment: Getting the data for risk assessment
---

# PingOne Protect SDK for iOS

## PingOne Signals (Protect) SDK for iOS (version 5.4.0)

Using the iOS version of the SDK involves the following steps:

* Adding the SDK to your app using CocoaPods or Swift Package Manager

* Importing the SDK module

* Initializing the SDK

* Getting the data for risk assessment

### Adding the SDK to your app

#### Adding the SDK to your app using CocoaPods

If you're new to CocoaPods, refer to the [official documentation](https://guides.cocoapods.org/using/using-cocoapods) for information on how to create and use Podfiles.

Open your project's Podfile and add the following to your app's target:

|   |                                                                                                                                           |
| - | ----------------------------------------------------------------------------------------------------------------------------------------- |
|   | Update the pod version to match the version of the PingOne Signals SDK for iOS that you are using. Currently the latest version is 5.4.0. |

`pod 'PingOneSignals', '~> 5.4.0'`

Run pod install from the command line:

`pod install`

#### Adding the SDK to your app using Swift Package Manager

1. Select File > Add Packages…​ in Xcode's menu bar.

2. Search for the PingOne Signals SDK using the repo's URL: <https://github.com/pingidentity/pingone-signals-sdk-ios>

3. Set the Dependency Rule to Branch with the value 'main' or select an exact version, and make sure that `Add to Project` is set to your project.

4. Select `Add Package`.

5. Verify that the package was downloaded in your project.

### SDK initialization

Initialize the SDK. You'll typically do this in your app's `application:didFinishLaunchingWithOptions:` method, or any other entry point during your application launch. For example:

```none
import PingOneSignals

let initParams = POInitParams()
initParams.envId = <envId> // optional
// If you are using the PingFed authentication API and version 1.3 of the Integration Kit, uncomment the following line to turn off the collection of behavioral data
// initParams.behavioralDataCollection = false
let pingOneSignals = PingOneSignals.initSDK(initParams: initParams)

pingOneSignals.setInitCallback { error in
    if let error = error {
        print("Init failed - \(error.localizedDescription)")
    } else {
        print("SDK Initialized")
    }
}
```

|   |                                                                                                                   |
| - | ----------------------------------------------------------------------------------------------------------------- |
|   | The code above contains the String placeholder <\`envId\`>. Replace this with the ID of your PingOne environment. |

Optionally, set an event listener to get calls on successful or failed SDK initialization.

### Getting the data for risk assessment

Get the data for risk assessment by adding a call to the SDK's `getData` method, for example:

```none
import PingOneSignals

let pingOneSignals = PingOneSignals.sharedInstance()
pingOneSignals?.getData { data, error in
    if let data = data {
        print("data: \(data)")
    } else if let error = error {
        print("error getting data: \(error)")
    }
}
```

---

---
title: PingOne Protect SDK for Web
description: When using the PingFederate Authentication API, use the version of the Signals SDK that supports the Risk/Protect Integration Kit that you installed in PingFederate:
component: pingone-api
page_id: pingone-api:native-sdks:pingone-risk-sdks/risk_evaluation_sdk_web
canonical_url: https://developer.pingidentity.com/pingone-api/native-sdks/pingone-risk-sdks/risk_evaluation_sdk_web.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  pingone-signals-protect-sdk-for-web: PingOne Signals (Protect) SDK for Web
  version-of-the-signals-sdk-to-use: Version of the Signals SDK to use
  npm-package-for-signals-sdk: npm package for Signals SDK
  main-steps: Main steps
  importing-the-script: Importing the script
  initializing-the-sdk: Initializing the SDK
  getting-the-data-for-risk-assessment: Getting the data for risk assessment
  update-your-content-security-policy-csp: Update your Content Security Policy (CSP)
---

# PingOne Protect SDK for Web

## PingOne Signals (Protect) SDK for Web

### Version of the Signals SDK to use

When using the PingFederate Authentication API, use the version of the Signals SDK that supports the Risk/Protect Integration Kit that you installed in PingFederate:

* For all versions of the PingOne Protect Integration Kit, use version 5.2.10 or later of the PingOne Signals SDK.

* For PingOne Risk Integration Kit 1.3.1, use version 5.2.10 or later of the PingOne Signals SDK.

* For PingOne Risk Integration Kit 1.3, use version 5.0.3 of the PingOne Signals SDK.

When integrating through the PingOne API, always use the latest version of the PingOne Signals SDK

### npm package for Signals SDK

There is also an [npm package for the Signals SDK](https://www.npmjs.com/package/@ping-identity/pingone-signals-web-sdk) that you can use. The readme file for the package contains the relevant instructions.

### Main steps

Using the web SDK involves the following steps:

* Importing the necessary script

* Initializing the SDK

* Getting the data for risk assessment

* Update your Content Security Policy (CSP)

#### Importing the script

Import the required script by including the following code segment in each relevant page.

To use the latest version of the PingOne Signals SDK, use `latest` in the path:

```none
<script
        src="https://apps.pingone.com/signals/web-sdk/latest/signals-sdk.js"
        defer>
</script>
```

To use a specific version of the PingOne Signals SDK, include the version number in the path. For example:

```none
<script
        src="https://apps.pingone.com/signals/web-sdk/5.6.10/signals-sdk.js"
        defer>
</script>
```

#### Initializing the SDK

Initialize the SDK by adding a listener for the `PingOneSignalsReadyEvent` event:

```none
function onPingOneSignalsReady(callback) {
    if (window['_pingOneSignalsReady']) {
        callback();
    } else {
        document.addEventListener('PingOneSignalsReadyEvent', callback);
    }
}
```

Then, if you are using version 5.3.7 or later of the Signals SDK, use this following code.

|   |                                                                                                                                                                                                                                                                                                                                                                                    |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The example shown here includes a number of options that you can turn on in the initialization code. Some of these, such as those for the PingID Device Trust agent, have equivalent UI elements in PingFederate and PingOne DaVinci that can be used to enable the options. If you use these UI elements, there is no need to include the options in the SDK initialization code. |

```none
onPingOneSignalsReady(function () {
    _pingOneSignals.init({
        // If you are using the PingFed authentication API and version 1.3 of the PingOne Risk Integration Kit, uncomment the following line to turn off the collection of behavioral data
        // behavioralDataCollection: false,
        // By default, the SDK creates a "tags" array containing the URLs visited and the time of the visit. Uncomment the following line to disable the collection of this data
        // disableTags: true,
        // Set universalDeviceIdentification to true if you want the device data in the SDK payload to be provided as a signed JWT
        // universalDeviceIdentification: true,
        // Set htmlGeoLocation to true if you want the SDK payload to include browser-based user location data if the user has provided their consent
        // htmlGeoLocation: true,
        // Set agentIdentification to true if you are using risk policies that contain the PingID Device Trust predictor
        // agentIdentification: true,
        // If you have set agentIdentification to true, use agentTimeout to specify the timeout the trust agent should use if you don't want to use the default timeout setting. Can be between 200 and 10,000 milliseconds.
        // agentTimeout: 5000,
        // If you have set agentIdentification to true, use agentPort to specify the port to use when connecting to the trust agent if you don't want to use the default port (9400)
        // agentPort: 8800,
        // Set isIAFDetectionEnabled to true to have the SDK detect AI agents
        // isIAFDetectionEnabled: true
        //
    }).then(function () {
        console.log("PingOne Signals initialized successfully");
    }).catch(function (e) {
        console.error("SDK Init failed", e);
    });
});
```

If you are using a version of the SDK between 5.2.1 and 5.3.6, use the following code:

```none
onPingOneSignalsReady(function () {
    _pingOneSignals.init({
        // If you are using the PingFed authentication API and version 1.3 of the Integration Kit, uncomment the following line to turn off the collection of behavioral data
        // behavioralDataCollection: false
    }).then(function () {
        console.log("PingOne Signals initialized successfully");
    }).catch(function (e) {
        console.error("SDK Init failed", e);
    });
});
```

If you are using version 5.0.3 or earlier of the Signals SDK, use the following code:

```none
onPingOneSignalsReady(function () {
    _pingOneSignals.initSilent({
        envId : <envId>
    }).then(function () {
        console.log("PingOne Signals initialized successfully");
    }).catch(function (e) {
        console.error("SDK Init failed", e);
    });
});
```

|   |                                                                                                                   |
| - | ----------------------------------------------------------------------------------------------------------------- |
|   | The code above contains the String placeholder <\`envId\`>. Replace this with the ID of your PingOne environment. |

#### Getting the data for risk assessment

Get the data for risk assessment by adding a call to the SDK's `getData` method, for example:

```none
_pingOneSignals.getData()
   .then(function (result) {
       console.log("get data completed: " + result)
   }).catch(function (e) {
       console.error('getData Error!', e);
});
```

#### Update your Content Security Policy (CSP)

Even if you are running the Signals SDK from your server or using the npm package, the SDK must communicate with the PingOne server, so add the following to your CSP:

```none
script-src 'self' https://apps.pingone.com;
connect-src 'self' https://apps.pingone.com;
style-src 'self' https://apps.pingone.com 'unsafe-inline';
```

---

---
title: PingOne Verify Native SDKs
description: PingOne Verify Native SDKs collect information required for verifying a user's identity and share the collected information with the PingOne Verify service. PingOne Verify Native SDKs are available in for two operating systems:
component: pingone-api
page_id: pingone-api:native-sdks:pingone-neo-native-sdks/pingone-verify-native-sdks
canonical_url: https://developer.pingidentity.com/pingone-api/native-sdks/pingone-neo-native-sdks/pingone-verify-native-sdks.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
---

# PingOne Verify Native SDKs

PingOne Verify Native SDKs collect information required for verifying a user's identity and share the collected information with the PingOne Verify service. PingOne Verify Native SDKs are available in for two operating systems:

* [PingOne Verify SDK for iOS](pingone-verify-native-sdks/pingone-verify-native-sdk-for-ios.html)

* [PingOne Verify SDK for Android](pingone-verify-native-sdks/pingone-verify-native-sdk-for-android.html)

---

---
title: PingOne Verify SDK for Android
description: The PingOne Verify SDK enables you to integrate PingOne Verify functionality into your native applications.
component: pingone-api
page_id: pingone-api:native-sdks:pingone-neo-native-sdks/pingone-verify-native-sdks/pingone-verify-native-sdk-for-android
canonical_url: https://developer.pingidentity.com/pingone-api/native-sdks/pingone-neo-native-sdks/pingone-verify-native-sdks/pingone-verify-native-sdk-for-android.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
---

# PingOne Verify SDK for Android

The PingOne Verify SDK enables you to integrate PingOne Verify functionality into your native applications.

The PingOne Veridy Native SDK package is available for download at <https://github.com/pingidentity/pingone-verify-mobile-sdk-android>. Further details for setup and integrating PingOne Verify Native SDK into your native apps are available in the [README](https://github.com/pingidentity/pingone-verify-mobile-sdk-android/blob/master/README.md) file in the top level folder of the downloadable package.

---

---
title: PingOne Verify SDK for iOS
description: The PingOne Verify SDK enables you to integrate PingOne Verify functionality into your native applications.
component: pingone-api
page_id: pingone-api:native-sdks:pingone-neo-native-sdks/pingone-verify-native-sdks/pingone-verify-native-sdk-for-ios
canonical_url: https://developer.pingidentity.com/pingone-api/native-sdks/pingone-neo-native-sdks/pingone-verify-native-sdks/pingone-verify-native-sdk-for-ios.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
---

# PingOne Verify SDK for iOS

The PingOne Verify SDK enables you to integrate PingOne Verify functionality into your native applications.

The PingOne Verify Native SDK package is available for download at <https://github.com/pingidentity/pingone-verify-mobile-sdk-ios>. Further details for setup and integrating PingOne Verify Native SDK into your native apps are available in the [README](https://github.com/pingidentity/pingone-verify-mobile-sdk-ios/blob/master/README.md) file in the top level folder of the downloadable package.

---

---
title: PingOne Wallet Native SDK for Android
description: The PingOne Wallet SDK enables you to integrate PingOne Wallet functionality into your native applications.
component: pingone-api
page_id: pingone-api:native-sdks:pingone-neo-native-sdks/pingone-wallet-native-sdks/pingone-wallet-native-sdk-for-android
canonical_url: https://developer.pingidentity.com/pingone-api/native-sdks/pingone-neo-native-sdks/pingone-wallet-native-sdks/pingone-wallet-native-sdk-for-android.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
---

# PingOne Wallet Native SDK for Android

The PingOne Wallet SDK enables you to integrate PingOne Wallet functionality into your native applications.

The PingOne Wallet Native SDK package is available for download at <https://github.com/pingidentity/pingone-wallet-mobile-sdk-android>. Further details for setup and integrating PingOne Wallet Native SDK into your native apps are available in the [README](https://github.com/pingidentity/pingone-wallet-mobile-sdk-android/blob/master/README.md) file in the top level folder of the downloadable package.

---

---
title: PingOne Wallet Native SDK for iOS
description: The PingOne Wallet SDK enables you to integrate PingOne Wallet functionality into your native applications.
component: pingone-api
page_id: pingone-api:native-sdks:pingone-neo-native-sdks/pingone-wallet-native-sdks/pingone-wallet-native-sdk-for-ios
canonical_url: https://developer.pingidentity.com/pingone-api/native-sdks/pingone-neo-native-sdks/pingone-wallet-native-sdks/pingone-wallet-native-sdk-for-ios.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
---

# PingOne Wallet Native SDK for iOS

The PingOne Wallet SDK enables you to integrate PingOne Wallet functionality into your native applications.

The PingOne Wallet Native SDK package is available for download at <https://github.com/pingidentity/pingone-wallet-mobile-sdk-ios>. Further details for setup and integrating PingOne Wallet Native SDK into your native apps are available in the [README](https://github.com/pingidentity/pingone-wallet-mobile-sdk-ios/blob/master/README.md) file in the top level folder of the downloadable package.

---

---
title: PingOne Wallet Native SDKs
description: This defines the usage and interfaces of the PingOne Wallet Native SDKs to interact with PingOne credentialing services. The SDK provides for a user to receive, save, and share credentials for identification and verification purposes. PingOne Wallet Native SDKs are available in for two operating systems:
component: pingone-api
page_id: pingone-api:native-sdks:pingone-neo-native-sdks/pingone-wallet-native-sdks
canonical_url: https://developer.pingidentity.com/pingone-api/native-sdks/pingone-neo-native-sdks/pingone-wallet-native-sdks.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  pingone-wallet-native-sdk-flows: PingOne Wallet Native SDK flows
  wallet-initialization: Wallet initialization
  credential-presentation: Credential presentation
---

# PingOne Wallet Native SDKs

This defines the usage and interfaces of the PingOne Wallet Native SDKs to interact with PingOne credentialing services. The SDK provides for a user to receive, save, and share credentials for identification and verification purposes. PingOne Wallet Native SDKs are available in for two operating systems:

* [PingOne Wallet Native SDK for iOS](pingone-wallet-native-sdks/pingone-wallet-native-sdk-for-ios.html)

* [PingOne Wallet Native SDK for Android](pingone-wallet-native-sdks/pingone-wallet-native-sdk-for-android.html)

## PingOne Wallet Native SDK flows

### Wallet initialization

When the wallet SDK initializes for the first time, it creates a new application instance for the default geographic supplied in the PingOneWalletClient.Builder, registers with the credentials service, and saves the application identifier with cryptographic keys locally. When the SDK receives a request for another region, it registers the same set of keys with the credential service running in the geographywhere the request originated before processing the request.

![PingOne Wallet Native SDK wallet initialization flow diagram](../../_images/p1Credentials-walletInitialization.png)

### Credential presentation

Upon scanning a QR, receiving a notification, or clicking a deep link the application passes the information to the SDK. The SDK then uses this information to fetch and parse the Presentation Request, and find the credentials in storage that match. These pass back to the Wallet Application that decides and approves which credentials to share. The SDK identifies the protocol in the presentation request (Native vs OPENID4VP) and prepares a Presentation Response accordingly. If the request is for presenting credentials for a session on the same device, the SDK asks the app to redirect the user to the corresponding URL in the browser after submitting the presentation response.

![PingOne Wallet Native SDK credential presentation flow diagram](../../_images/p1Credentials-credentialPresentation.png)

---

---
title: SDK Changelog
description: Jan 21, 2026
component: pingone-api
page_id: pingone-api:native-sdks:pingone-risk-sdks/protect_sdk_changelog
canonical_url: https://developer.pingidentity.com/pingone-api/native-sdks/pingone-risk-sdks/protect_sdk_changelog.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  signals-protect-sdk-for-ios: Signals (Protect) SDK for iOS
  signals-protect-sdk-for-android: Signals (Protect) SDK for Android
  signals-protect-sdk-for-web: Signals (Protect) SDK for Web
---

# SDK Changelog

## Signals (Protect) SDK for iOS

| Release Date | Description                                                                                                                                                                                                                            |
| ------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Jan 21, 2026 | Version 5.4.0- The Signals SDK now supports iOS 26 with Xcode 26.

- For iOS apps that used version 5.3.0 of the Signals SDK, there were cases where the app would crash upon being launched. This issue has been fixed (TRIAGE-30884) |
| Mar 23, 2025 | Version 5.3.0- For user location information, the Signals SDK now takes into account GPS data if the application has requested location permissions.                                                                                   |
| Nov 6, 2024  | Version 5.2.8- The Signals SDK now takes into account mobile device permissions and additional sensor readings.                                                                                                                        |

## Signals (Protect) SDK for Android

| Release Date   | Description                                                                                                                                                                                                                                                             |
| -------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Jan 21, 2026   | Version 5.3.0- The Signals SDK is now targeted for Level 36 (Android 16).                                                                                                                                                                                               |
| March 23, 2025 | Version 5.2.0- For user location information, the Signals SDK now takes into account GPS data if the application has requested location permissions.                                                                                                                    |
| Nov 6, 2024    | Version 5.1.6- The Signals SDK now takes into account mobile device permissions and additional sensor readings.

- The minimum Android version supported is now Level 21 (Android 5.0).

- The Signals SDK uses the Android features included in Level 34 (Android 14). |

## Signals (Protect) SDK for Web

| Release Date | Description                                                                                                                                                                                                                                                                                                                                         |
| ------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Jun 30, 2026 | Version 5.6.10- The SDK can now detect AI agents (requires turning on the `isIAFDetectionEnabled` property).

- Improvements aimed at further increasing the accuracy of risk evaluations.

- Performance enhancements.                                                                                                                             |
| Mar 16, 2026 | Version 5.6.9- Improved browser fingerprint.

- General efficiency improvements.                                                                                                                                                                                                                                                                    |
| Mar 9, 2026  | Version 5.6.8- Initial npm package for the PingOne Signals SDK.                                                                                                                                                                                                                                                                                     |
| Jan 21, 2026 | Version 5.6.7- Contains improvements aimed at further increasing the accuracy of risk evaluations.                                                                                                                                                                                                                                                  |
| Oct 23, 2025 | Version 5.6.3- Now includes an option to have the SDK payload include browser-based user location data if the user has provided their consent.                                                                                                                                                                                                      |
| Jun 4, 2025  | Version 5.6.0- Enhancements have been made to the signal-collection engine to keep pace with changes in the browser landscape.                                                                                                                                                                                                                      |
| Mar 4, 2025  | Version 5.5.0- Includes support for the new PingID Device Trust predictor. The predictor requires that the [PingID Device Trust agent](https://docs.pingidentity.com/pingone/strong_authentication_mfa/p1_using_the_workforce_trust_agent.html) be installed on users' computers, and requires both a PingID license and a PingOne Protect license. |
| Oct 10, 2024 | Version 5.4.0- Contains improvements to behavioral data collection.

- Verified that code change made in earlier version resolved issue related to Content Security Policy (CSP).                                                                                                                                                                   |