---
title: PingOne MFA Connector
description: Configure the PingOne MFA connector in PingOne DaVinci to add MFA flows, user enrollment, and passwordless authentication to your applications
component: connectors
page_id: connectors::p1_mfa_connector
canonical_url: https://docs.pingidentity.com/connectors/p1_mfa_connector.html
llms_txt: https://docs.pingidentity.com/connectors/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 9, 2026
section_ids:
  setup: Setup
  resources: Resources
  requirements: Requirements
  setting-up-pingone-mfa: Setting up PingOne MFA
  setting-up-your-pingone-mfa-environment: Setting up your PingOne MFA environment
  choosing-a-pingone-worker-app: Choosing a PingOne worker app
  setting-up-the-connector: Setting up the connector
  connector-settings: Connector settings
  environment-id: Environment ID
  policy-id: Policy ID
  client-id: Client ID
  client-secret: Client Secret
  region: Region
  using-the-connector-in-a-flow: Using the connector in a flow
  enrolling-a-device: Enrolling a device
  authenticating-users: Authenticating users
  configuring-passwordless-authentication: Configuring passwordless authentication
  capabilities: Capabilities
  readDevice: Read Device
  readAllDevices: Read All Devices
  createDevice: Create Device
  activateDevice: Activate Device
  deleteDevice: Delete Device
  resendOTPForPairing: Resend OTP for Pairing
  updateDeviceNickname: Update Device Nickname
  readUserMFAEnabled: Read MFA Status
  updateUserMFAEnabled: Update MFA Status
  readDeviceAuthenticationPolicy: Read Device Authentication Policy
  createDeviceAuthentication: Create Device Authentication
  readDeviceAuthentication: Read Device Authentication
  deviceSelectDeviceAuthentication: Device Selection
  validateOtpDeviceAuthentication: Device Passcode
  validateAssertionDeviceAuthentication: FIDO Assertion
  cancelPushNotification: Cancel Push Notification
  readPairingKey: Read Pairing Key
  createPairingKey: Create Pairing Key
  deletePairingKey: Delete Pairing Key
  createAuthenticationCode: Create Authentication Code
  readAuthenticationCode: Read Authentication Code
  setDeviceOrder: Set Device Order
  cancelDeviceAuthenticationPingID: Cancel Device Authentication
  createDevicePingID: Create Device
  createDeviceAuthenticationPingID: Create Device Authentication
  createPairingKeyPingID: Create Pairing Key
  readAllDevicesPingID: Read All Devices
  evalPolicyPingID: Evaluate Policy
  registerRememberMe: Create Remembered Device
  checkRememberMe: Check Remember Me State
---

# PingOne MFA Connector

PingOne MFA is a cloud-based multi-factor authentication (MFA) *(tooltip: \<div class="paragraph">
\<p>An electronic authentication method where a user is granted access only after presenting two or more verification factors for authentication.\</p>
\</div>)* service that protects an organization's network, applications, and data resources while providing secure and seamless experiences for your customers and users.

The PingOne MFA connector supports the use of:

* Customer-friendly authentication flows to increase security without adding unnecessary friction to the end user experience

* User enrollment flows:

  * Automatically: Allow customers to automatically enroll an authentication method for users during different operations, such as registering the user email or phone number as part of a user provisioning

  * Manually: Allow users to manage their devices and add authentication methods during enrollment

  * One-time device authentication: Include device details within an authentication request. Enables a user to authenticate for one session only, without pairing the device.

* Usernameless and passwordless sign-on and authentication flows using appropriate, secure authentication methods, such as FIDO biometrics

## Setup

### Resources

* PingOne documentation:

  * [Introduction to PingOne MFA](https://docs.pingidentity.com/pingone/getting_started_with_pingone/p1mfa__introduction.html)

  * [Getting started with PingOne MFA](https://docs.pingidentity.com/pingone/getting_started_with_pingone/p1mfa_getting_started.html)

  * [Adding an application](https://docs.pingidentity.com/pingone/applications/p1_applications_add_applications.html)

* PingOne DaVinci documentation:

  * [Introduction to PingOne](https://docs.pingidentity.com/pingone/introduction_to_pingone/p1_introduction.html)

  * [Getting started with PingOne](https://docs.pingidentity.com/pingone/getting_started_with_pingone/p1_getting_started.html)

  * [Adding an application](https://docs.pingidentity.com/pingone/applications/p1_applications_add_applications.html)

### Requirements

To use the connector, you'll need:

* A PingOne MFA license ([Try PingOne for free](https://www.pingidentity.com/en/try-ping.html))

* A PingOne MFA environment with a configured Worker app

* A multi-factor authentication (MFA) policy. See [MFA policies](https://docs.pingidentity.com/pingone/authentication/p1_mfa_policies.html).

### Setting up PingOne MFA

#### Setting up your PingOne MFA environment

Follow the instructions in [Getting started with PingOne MFA](https://docs.pingidentity.com/pingone/getting_started_with_pingone/p1mfa_getting_started.html).

#### Choosing a PingOne worker app

Most environments include a preconfigured worker app that you can use with DaVinci connectors.

To add a worker app:

1. Decide whether to connect to the host PingOne tenant or a different PingOne tenant.

2. In the PingOne admin console, go to **Applications > Applications**.

3. Select the preconfigured **PingOne DaVinci Connection** worker app.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | A small number of older environments might not have the preconfigured worker app. If that applies to your environment, you can:- Reuse a worker app you've already created.

- Create a new worker app.

  > **Collapse: Details**
  >
  > To create a new worker app for this connector:
  >
  > 1. Sign on to PingOne.
  >
  > 2. Create a worker app as described in the [PingOne documentation](https://docs.pingidentity.com/pingone/applications/p1_applications_add_applications.html).
  >
  > 3. Make sure you set the authentication method as `Client secret basic`.
  >
  >    The PingOne connector receives a token using your application's credentials.
  >
  > 4. Assign the following roles to the worker app:
  >
  >    * **Identity Data Admin**
  >
  >    * **Environment Admin**
  >
  > 5. Note the **Client ID**, **Client Secret**, and **Environment ID** for the worker app.
  >
  > 6. Click **Finish**.
  >
  > 7. Go to **Applications > Applications**, click the application to open the application details, and click the toggle switch in the upper right to enable the application. |

### Setting up the connector

In PingOne DaVinci, add a **PingOne MFA** connection. Learn more in [Adding a connector](https://docs.pingidentity.com/davinci/connectors/davinci_adding_a_connector.html).

#### Connector settings

##### Environment ID

Your PingOne Environment ID. In PingOne, go to **Settings > Environment Properties**.

##### Policy ID

The unique identifier for the device authentication policy. You can define MFA policies and reference them as part of the connector setup. See [MFA policies](https://docs.pingidentity.com/pingone/authentication/p1_mfa_policies.html).

##### Client ID

The Client ID for your PingOne Worker application that you identified in [Choosing a PingOne worker app](#choosing-a-pingone-worker-app). In PingOne, go to **Applications > Applications > Configuration**.

##### Client Secret

The Client Secret for your PingOne Worker application that you identified in [Choosing a PingOne worker app](#choosing-a-pingone-worker-app). In PingOne, go to **Applications > Applications > Configuration**.

##### Region

Your PingOne environment region. In PingOne, go to **Settings > Environment Properties**.

## Using the connector in a flow

### Enrolling a device

To enable users and increase MFA adoption, use the PingOne MFA connector to include a device enrollment as part of user registration or as a just-in-time (JIT) registration within an authentication flow.

The user can select an authentication method for MFA from a list of methods defined by your organization's policy. This list can include traditional methods, such as email and SMS, and more secure and frictionless methods, such as FIDO2 biometrics and a native mobile SDK.

You can define device enrollment as either mandatory or optional.

You can choose to enable MFA automatically when device enrollment completes so that the next time the user authenticates, the device is available for them to use to authenticate.

Search the [Ping Identity Marketplace](https://marketplace.pingone.com/home) for the following out-of-the-box PingOne MFA device enrollment templates:

* PingOne — Registration and MFA Enrollment

  |   |                                                                                                                                              |
  | - | -------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | This flow must include the **PingOne - Device Registration sub-flow** to provide on-the-fly device enrollment for users during registration. |

* PingOne — Registration and MFA Auto-Enrollment

  In this flow, the Admin selects which devices to enroll for the user.

Learn more in the [Creating an authentication flow](https://docs.pingidentity.com/davinci/use_cases/davinci_use_cases_creating_an_authentication_flow.html) guide.

### Authenticating users

Use the PingOne MFA connector to increase security by adding an authentication factor that requires the user to prove their identity using a trusted device.

Search the [Ping Identity Marketplace](https://marketplace.pingone.com/home) for the following out-of-the-box PingOne MFA authentication templates:

* PingOne — Sign on and MFA

  |   |                                                                                                                                              |
  | - | -------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | This flow must include the **PingOne - Device Registration sub-flow** to provide on-the-fly device enrollment for users during registration. |

* PingOne - Sign on and Adaptive MFA

  |   |                                                                                                                                                                                                                   |
  | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | This flow must include the following sub-flows:- PingOne - Device Registration sub-flow to provide on-the-fly enrollment for users that have not yet registered a device

  - PingOne - MFA Authentication sub-flow |

* PingOne - One-time use device authentication

  Indicate whether a paired device is used, or specify a device explicitly for one-time authentication.

Learn more in the [Creating an authentication flow](https://docs.pingidentity.com/davinci/use_cases/davinci_use_cases_creating_an_authentication_flow.html) guide.

### Configuring passwordless authentication

Use the PingOne MFA connector to enhance your end user's login experience and increase security by adding passwordless authentication using standard methods such as SMS, OTP, biometric authentication, and QR code scanning. The end user must enable biometric authentication on their machine and enroll it for use with PingOne MFA to benefit from frictionless biometric login, removing the need to enter a password each time they sign on.

You can use the PingOne MFA connector to design the following types of passwordless authentication flows:

* PingOne Usernameless sign-on with biometrics

  User authenticates by scanning their compatible FIDO authenticator, without requiring a username or password.

* PingOne - Passwordless authentication

  User enters a username and uses any compatible device to authenticate. If the user device is not yet registered, they must verify the device using a one-time passcode (OTP) sent to the email or mobile number (using one-time use device authentication). After successfully verifying the device they can register it for passwordess authentication.

* PingOne - Passwordless sign-on with biometrics

  User enters their username and either provides their existing password, or uses their device biometrics to authenticate.

* PingOne - QR code passwordless sign-on

  User signs on by scanning a QR code using a mobile application, with no need to input any other information.

  |   |                                                                              |
  | - | ---------------------------------------------------------------------------- |
  |   | This flow requires a custom mobile app that uses the PingOne MFA mobile SDK. |

|   |                                                                                                                                                                                                                                               |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | In order to get the benefits of frictionless biometric login instead of having to enter their user credentials each time they sign on, end users must enable biometric authentication on their device and enroll it for use with PingOne MFA. |

You can find sample passwordless authentication flows in the [Ping Identity Marketplace](https://marketplace.pingone.com/home). For help, refer to the [Creating an authentication flow](https://docs.pingidentity.com/davinci/use_cases/davinci_use_cases_creating_an_authentication_flow.html) guide.

## Capabilities

### Read Device

Read information for a device associated with a user.

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - User ID textField
>
>   The unique identifier for the user.
>
> - Device ID textField
>
>   The unique identifier for the MFA device.
>
> * default object
>
>   * properties object
>
>     * userId string required minLength: 0 maxLength: 100
>
>     * deviceId string required minLength: 0 maxLength: 100
>
> - output object
>
>   * rawResponse object
>
>     * id string
>
>     * type string
>
>     * status string
>
>     * nickname string
>
>     * phone string
>
>     * extension string
>
>     * email string
>
>     * secret string
>
>     * keyUri string
>
>     * oathToken string
>
>     * serialNumber string
>
>     * rp object
>
>       * id string
>
>       * name string
>
>     * platform string
>
>     * publicKeyCredentialCreationOptions string
>
>     * attributes object
>
>       * previousDeviceType string
>
>       * isCrossPlatform boolean
>
>     * displayName string
>
>     * createdAt string
>
>     * updatedAt string
>
>   * headers object
>
>   * statusCode integer
>
>   * device object
>
>     * id string
>
>     * type string
>
>     * status string
>
>     * nickname string
>
>     * phone string
>
>     * extension string
>
>     * email string
>
>     * secret string
>
>     * keyUri string
>
>     * oathToken string
>
>     * serialNumber string
>
>     * rp object
>
>       * id string
>
>       * name string
>
>     * platform string
>
>     * publicKeyCredentialCreationOptions string
>
>     * attributes object
>
>       * previousDeviceType string
>
>       * isCrossPlatform boolean
>
>     * displayName string
>
>     * createdAt string
>
>     * updatedAt string
>
> Output Example
>
> ```json
> {
>   "rawResponse": {
>     "device": {
>       "id": "43eb5621-eae8-4fa1-aafb-2a884d6848cb",
>       "type": "SMS",
>       "status": "ACTIVE",
>       "nickname": "Work Device",
>       "phone": "+972528888888",
>       "extension": "###1",
>       "createdAt": "2021-01-15T20:45:17.463Z",
>       "updatedAt": "2021-01-15T20:45:17.463Z"
>     }
>   }
> }
> ```

### Read All Devices

Read information for all user devices

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - User ID textField
>
>   The unique identifier for the user.
>
> - Filters toggleSwitch
>
>   Filter devices by activation status and device type.
>
> - Status dropDown
>
>   non-active devices are not usable during an authentication.
>
>   * ALL (Default)
>
>   * ACTIVE
>
>   * ACTIVATION REQUIRED
>
> - Device Types dropDownMultiSelect
>
>   * Email
>
>   * SMS
>
>   * Voice
>
>   * Authenticator App
>
>   * Mobile Applications
>
>   * Fido2 Biometrics
>
>   * Security Key
>
>   * Oath token
>
> * default object
>
>   * properties object
>
>     * userId string required minLength: 0 maxLength: 100
>
>     * setFilterFlag boolean
>
>     * statusFilter string
>
>     * deviceTypes array uniqueItems: true
>
> - output object
>
>   * rawResponse object
>
>     * \_embedded object
>
>       * devices array
>
>       * applications array
>
>       * allowedtypes array
>
>       * order array
>
>         * id string
>
>       * mfaSettings object
>
>         * environment object
>
>           * id string
>
>         * pairing object
>
>           * maxAllowedDevices integer
>
>       * mfaPolicy object
>
>         * authentication object
>
>           * deviceSelection string
>
>     * size number
>
>   * headers object
>
>   * statusCode integer
>
>   * devices array
>
>   * allowedtypes array
>
>   * applications array
>
>   * mfaSettings object
>
>     * environment object
>
>       * id string
>
>     * pairing object
>
>       * maxAllowedDevices integer
>
>   * mfaPolicy object
>
>     * authentication object
>
>       * deviceSelection string
>
>   * order array
>
>     * id string
>
> Output Example
>
> ```json
> {
>   "rawResponse": {
>     "_embedded": {
>       "devices": [
>         {
>           "device": {
>             "id": "43eb5621-eae8-4fa1-aafb-2a884d6848cb",
>             "type": "SMS",
>             "status": "ACTIVE",
>             "nickname": "Work Device",
>             "phone": "+972528888888",
>             "extension": "###1",
>             "createdAt": "2021-01-15T20:45:17.463Z",
>             "updatedAt": "2021-01-15T20:45:17.463Z"
>           }
>         }
>       ],
>       "applications": [
>         {
>           "id": "43eb4421-eae8-4fa1-aafb-2a884d6848cb",
>           "environment": {
>             "id": "143459b9-107b-48ae-8c0a-e65f94054ebb"
>           },
>           "name": "IOS nativeApp",
>           "enabled": true,
>           "mobile": {
>             "bundleId": "com.pingIdentity.p14c.sample",
>             "integrityDetection": {
>               "mode": "DISABLED"
>             }
>           }
>         }
>       ],
>       "allowedtypes": [
>         "SMS",
>         "VOICE",
>         "MOBILE",
>         "TOTP",
>         "OATH_TOKEN",
>         "YUBIKEY",
>         "PINGID_DESKTOP",
>         "PLATFORM",
>         "SECURITY_KEY"
>       ],
>       "order": [
>         {
>           "id": "43eb5621-eae8-4fa1-aafb-2a884d6848cb"
>         },
>         {
>           "id": "01f3db05-93b6-4c45-a93e-f9ac84d076c6"
>         }
>       ],
>       "mfaSettings": {
>         "environment": {
>           "id": "143459b9-107b-48ae-8c0a-e65f94054ebb"
>         },
>         "pairing": {
>           "maxAllowedDevices": 5
>         }
>       },
>       "mfaPolicy": {
>         "authentication": {
>           "deviceSelection": "DEFAULT_TO_FIRST"
>         }
>       }
>     },
>     "count": 1,
>     "size": 1
>   },
>   "devices": [
>     {
>       "device": {
>         "id": "43eb5621-eae8-4fa1-aafb-2a884d6848cb",
>         "type": "SMS",
>         "status": "ACTIVE",
>         "nickname": "Work Device",
>         "phone": "+972528888888",
>         "extension": "###1",
>         "createdAt": "2021-01-15T20:45:17.463Z",
>         "updatedAt": "2021-01-15T20:45:17.463Z"
>       }
>     }
>   ],
>   "applications": [
>     {
>       "id": "43eb4421-eae8-4fa1-aafb-2a884d6848cb",
>       "environment": {
>         "id": "143459b9-107b-48ae-8c0a-e65f94054ebb"
>       },
>       "name": "IOS nativeApp",
>       "enabled": true,
>       "mobile": {
>         "bundleId": "com.pingIdentity.p14c.sample",
>         "integrityDetection": {
>           "mode": "DISABLED"
>         }
>       }
>     }
>   ],
>   "allowedtypes": [
>     "SMS",
>     "VOICE",
>     "MOBILE",
>     "TOTP",
>     "OATH_TOKEN",
>     "YUBIKEY",
>     "PINGID_DESKTOP",
>     "PLATFORM",
>     "SECURITY_KEY"
>   ],
>   "order": [
>     {
>       "id": "43eb5621-eae8-4fa1-aafb-2a884d6848cb"
>     },
>     {
>       "id": "01f3db05-93b6-4c45-a93e-f9ac84d076c6"
>     }
>   ],
>   "mfaSettings": {
>     "environment": {
>       "id": "143459b9-107b-48ae-8c0a-e65f94054ebb"
>     },
>     "pairing": {
>       "maxAllowedDevices": 5
>     }
>   },
>   "mfaPolicy": {
>     "authentication": {
>       "deviceSelection": "DEFAULT_TO_FIRST"
>     }
>   }
> }
> ```

### Create Device

Create devices to use during authentication.

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - User ID textField
>
>   The unique identifier for the user.
>
> - Device Type dropDown
>
>   The type of device used during authentication.
>
>   * Email
>
>   * SMS
>
>   * Voice
>
>   * Authenticator App
>
>   * Mobile Applications
>
>   * Fido2 Biometrics
>
>   * Security Key
>
>   * Oath token
>
>   * Enter Device Type
>
> - * Enter Device Type textField
>   * Activation Status dropDown
>
>   The current status of the device. If a device has an ACTIVATION\_REQUIRED status, activate it before you add it as a trusted device.
>
>   * ACTIVE
>
>   * ACTIVATION REQUIRED
>
> - Phone Number textField
>
>   The phone number to associate with the device. Applies only to devices that use SMS and Voice SMS messages during authentication.
>
> - Extension textField
>
>   The phone extension for this device. It can include digits, comma, # and \*. If there is more than one extension then a comma should separate the extension and the nested extension.
>
> - Email textField
>
>   The email address to associate with the device. Applies only to devices that use email during authentication.
>
> - Device Nickname textField
>
>   A nickname that identifies this device. The device nickname is limited to 100 characters.
>
> - Relying Party ID textField
>
>   If you define a Relying Party ID (RPID) here, it overrides the RPID defined in the FIDO policy in the PingOne admin console.
>
> - Relying Party Name textField
>
>   A string that specifies the relying party's human-readable display name.
>
> - Serial Number textField
>
>   The unique identifier for the OAuth token.
>
> - Notification Policy dropDown
>
>   A unique identifier for the policy.
>
>   * Enter Notification Policy ID
>
> - * Notification Policy ID textField
>   * Notification Name dropDown
>
>   The name of a custom notification defined in PingOne. If the form you want is not listed, select Enter Custom Value.
>
>   * Enter Custom Value
>
> - Custom Value textField
>
>   You can enter a custom template name, or leave blank to use the default template. You can also enter a parameter from a previous connector, or any text.
>
> - Notification Locale textField
>
>   Add a locale to allow localized notifications for end-users. ISO Language Codes are supported.
>
> - Notification Variables variableInputList
>
>   If Custom variables are defined in the notification body, map them here.
>
> - User Agent textField
>
>   Browser user agent
>
> - Custom FIDO2 Challenge textField
>
>   Applicable for FIDO2 pairing requests. Specify a custom challenge that will replace the automatically generated challenge sent with the pairing request. Must be a valid Base64URL string that decodes to at least 32 bytes of data array.
>
> - Test Mode textField
>
>   Create device for test purposes only
>
> * default object
>
>   * properties object
>
>     * userId string required minLength: 0 maxLength: 100
>
>     * deviceType string required
>
>     * customDeviceType null/string/object
>
>     * status string required
>
>     * nickname string
>
>     * phone string
>
>     * extension string
>
>     * email string
>
>     * rpId string
>
>       Relying Party ID
>
>     * rpName string
>
>       Relying Party Name
>
>     * serialNumber string
>
>       Serial Number
>
>     * notificationPolicyId string minLength: 0 maxLength: 100
>
>     * customNotificationPolicyId null/string/object
>
>     * templateVariant null/string
>
>     * customTemplateVariant null/string/object
>
>     * templateLocale null/string
>
>     * templateVariables array
>
>     * userAgent string
>
>       User Agent
>
>     * challenge string
>
>       Custom FIDO2 Challenge
>
>     * createDeviceTestMode string
>
>       Create Test Device
>
>     * oneTimeDeviceTestMode string
>
>       Create Test Device
>
> - output object
>
>   * rawResponse object
>
>     * id string
>
>     * type string
>
>     * status string
>
>     * nickname string
>
>     * phone string
>
>     * extension string
>
>     * email string
>
>     * secret string
>
>     * keyUri string
>
>     * oathToken string
>
>     * serialNumber string
>
>     * rp object
>
>       * id string
>
>       * name string
>
>     * platform string
>
>     * publicKeyCredentialCreationOptions string
>
>     * attributes object
>
>       * previousDeviceType string
>
>       * isCrossPlatform boolean
>
>     * displayName string
>
>     * createdAt string
>
>     * updatedAt string
>
>     * test object
>
>       * otp string
>
>   * headers object
>
>   * statusCode integer
>
>   * device object
>
>     * id string
>
>     * type string
>
>     * status string
>
>     * nickname string
>
>     * phone string
>
>     * extension string
>
>     * email string
>
>     * secret string
>
>     * keyUri string
>
>     * oathToken string
>
>     * serialNumber string
>
>     * rp object
>
>       * id string
>
>       * name string
>
>     * platform string
>
>     * publicKeyCredentialCreationOptions string
>
>     * attributes object
>
>       * previousDeviceType string
>
>       * isCrossPlatform boolean
>
>     * displayName string
>
>     * createdAt string
>
>     * updatedAt string
>
> Output Example
>
> ```json
> {
>   "rawResponse": {
>     "device": {
>       "id": "43eb5621-eae8-4fa1-aafb-2a884d6848cb",
>       "type": "SMS",
>       "status": "ACTIVE",
>       "nickname": "Work Device",
>       "phone": "+972528888888",
>       "extension": "###1",
>       "createdAt": "2021-01-15T20:45:17.463Z",
>       "updatedAt": "2021-01-15T20:45:17.463Z"
>     }
>   }
> }
> ```

### Activate Device

Activate devices for the first time.

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - User ID textField
>
>   The unique identifier for the user.
>
> - Device ID textField
>
>   The unique identifier for the MFA device.
>
> - One-time Passcode textField
>
>   The one-time passcode (OTP) sent to the user.
>
> - Attestation textField
>
>   A read-only string that specifies the public key and signed challenge used to complete registration and device activation. The attestation is generated by the browser as a response to a specific user action, such as a fingerprint scan or tap on a security key.
>
> - Origin textField
>
>   The address of the server sending the initial registration challenge to the device.
>
> - OATH Token Resync toggleSwitch
>
>   Indicates if OATH token resync is permitted during registration
>
> * default object
>
>   * properties object
>
>     * userId string required minLength: 0 maxLength: 100
>
>     * deviceId string required minLength: 0 maxLength: 100
>
>     * otp string
>
>       Passcode
>
>     * attestation string
>
>       WebAuthn assertion
>
>     * origin string
>
>       Origin
>
>     * oathResync boolean
>
>       Allow OATH token resync
>
> - output object
>
>   * rawResponse object
>
>     * id string
>
>     * type string
>
>     * status string
>
>     * nickname string
>
>     * phone string
>
>     * extension string
>
>     * email string
>
>     * secret string
>
>     * keyUri string
>
>     * oathToken string
>
>     * serialNumber string
>
>     * rp object
>
>       * id string
>
>       * name string
>
>     * platform string
>
>     * publicKeyCredentialCreationOptions string
>
>     * attributes object
>
>       * previousDeviceType string
>
>       * isCrossPlatform boolean
>
>     * displayName string
>
>     * createdAt string
>
>     * updatedAt string
>
>   * headers object
>
>   * statusCode integer
>
>   * device object
>
>     * id string
>
>     * type string
>
>     * status string
>
>     * nickname string
>
>     * phone string
>
>     * extension string
>
>     * email string
>
>     * secret string
>
>     * keyUri string
>
>     * oathToken string
>
>     * serialNumber string
>
>     * rp object
>
>       * id string
>
>       * name string
>
>     * platform string
>
>     * publicKeyCredentialCreationOptions string
>
>     * attributes object
>
>       * previousDeviceType string
>
>       * isCrossPlatform boolean
>
>     * displayName string
>
>     * createdAt string
>
>     * updatedAt string
>
> Output Example
>
> ```json
> {
>   "rawResponse": {
>     "device": {
>       "id": "43eb5621-eae8-4fa1-aafb-2a884d6848cb",
>       "type": "SMS",
>       "status": "ACTIVE",
>       "nickname": "Work Device",
>       "phone": "+972528888888",
>       "extension": "###1",
>       "createdAt": "2021-01-15T20:45:17.463Z",
>       "updatedAt": "2021-01-15T20:45:17.463Z"
>     }
>   }
> }
> ```

### Delete Device

Delete devices.

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - User ID textField
>
>   The unique identifier for the user.
>
> - Device ID textField
>
>   The unique identifier for the MFA device.
>
> * default object
>
>   * properties object
>
>     * userId string required minLength: 0 maxLength: 100
>
>     * deviceId string required minLength: 0 maxLength: 100
>
> - output object
>
>   * rawResponse object
>
>   * headers object
>
>   * statusCode integer

### Resend OTP for Pairing

If user did not receive the one-time passcode (OTP) that was sent for pairing a device, you can resend the OTP.

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - User ID textField
>
>   The unique identifier for the user.
>
> - Device ID textField
>
>   The unique identifier for the MFA device.
>
> * default object
>
>   * properties object
>
>     * userId string required minLength: 0 maxLength: 100
>
>     * deviceId string required minLength: 0 maxLength: 100
>
> - output object
>
>   * rawResponse object
>
>     * id string
>
>     * type string
>
>     * status string
>
>     * nickname string
>
>     * phone string
>
>     * extension string
>
>     * email string
>
>     * secret string
>
>     * keyUri string
>
>     * oathToken string
>
>     * serialNumber string
>
>     * rp object
>
>       * id string
>
>       * name string
>
>     * platform string
>
>     * publicKeyCredentialCreationOptions string
>
>     * attributes object
>
>       * previousDeviceType string
>
>       * isCrossPlatform boolean
>
>     * displayName string
>
>     * createdAt string
>
>     * updatedAt string
>
>   * headers object
>
>   * statusCode integer
>
> Output Example
>
> ```json
> {
>   "rawResponse": {
>     "device": {
>       "id": "43eb5621-eae8-4fa1-aafb-2a884d6848cb",
>       "type": "SMS",
>       "status": "ACTIVE",
>       "nickname": "Work Device",
>       "phone": "+972528888888",
>       "extension": "###1",
>       "createdAt": "2021-01-15T20:45:17.463Z",
>       "updatedAt": "2021-01-15T20:45:17.463Z"
>     }
>   }
> }
> ```

### Update Device Nickname

Update device nicknames.

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - User ID textField
>
>   The unique identifier for the user.
>
> - Device ID textField
>
>   The unique identifier for the MFA device.
>
> - Device Nickname textField
>
>   A nickname that identifies this device. The device nickname is limited to 100 characters.
>
> * default object
>
>   * properties object
>
>     * userId string required minLength: 0 maxLength: 100
>
>     * deviceId string required minLength: 0 maxLength: 100
>
>     * nickname string required
>
>       Device nickname
>
> - output object
>
>   * rawResponse object
>
>   * headers object
>
>   * statusCode integer
>
>   * nickname string
>
> Output Example
>
> ```json
> {
>   "rawResponse": {
>     "nickname": true
>   }
> }
> ```

### Read MFA Status

Indicates whether MFA is enabled for the user.

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - User ID textField
>
>   The unique identifier for the user.
>
> * default object
>
>   * properties object
>
>     * userId string required minLength: 0 maxLength: 100
>
> - output object
>
>   * rawResponse object
>
>   * headers object
>
>   * statusCode integer
>
>   * mfaEnabled boolean
>
> Output Example
>
> ```json
> {
>   "rawResponse": {
>     "mfaEnabled": true
>   }
> }
> ```

### Update MFA Status

Enables or disables MFA for the user.

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - User ID textField
>
>   The unique identifier for the user.
>
> - Enable User MFA toggleSwitch
>
>   Enable or disable user MFA.
>
> * default object
>
>   * properties object
>
>     * userId string required minLength: 0 maxLength: 100
>
>     * mfaEnabled boolean required
>
>       MFA Enable Status Of User
>
> - output object
>
>   * rawResponse object
>
>   * headers object
>
>   * statusCode integer
>
>   * mfaEnabled boolean
>
> Output Example
>
> ```json
> {
>   "rawResponse": {
>     "mfaEnabled": true
>   }
> }
> ```

### Read Device Authentication Policy

Read MFA device authentication policies.

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - Device Authentication Policy dropDown
>
>   A unique identifier for the policy.
>
>   * Enter Device Authentication Policy ID
>
> - Device Authentication Policy ID textField required
>
> * default object
>
>   * properties object
>
>     * deviceAuthenticationPolicyId string required minLength: 0 maxLength: 100
>
>     * customDeviceAuthenticationPolicyId null/string/object
>
> - output object
>
>   * rawResponse object
>
>     * id string
>
>     * name string
>
>     * forSignOnPolicy boolean
>
>     * default boolean
>
>     * sms object
>
>       * enabled boolean
>
>       * otp object
>
>         * failure object
>
>           * count integer
>
>           * coolDown object
>
>             * duration integer
>
>             * timeUnit string
>
>         * lifeTime object
>
>           * duration integer
>
>           * timeUnit string
>
>     * email object
>
>       * enabled boolean
>
>       * otp object
>
>         * failure object
>
>           * count integer
>
>           * coolDown object
>
>             * duration integer
>
>             * timeUnit string
>
>         * lifeTime object
>
>           * duration integer
>
>           * timeUnit string
>
>     * voice object
>
>       * enabled boolean
>
>       * otp object
>
>         * failure object
>
>           * count integer
>
>           * coolDown object
>
>             * duration integer
>
>             * timeUnit string
>
>         * lifeTime object
>
>           * duration integer
>
>           * timeUnit string
>
>     * mobile object
>
>       * enabled boolean
>
>       * otp object
>
>         * failure object
>
>           * count integer
>
>           * coolDown object
>
>             * duration integer
>
>             * timeUnit string
>
>         * window object
>
>           * stepSize object
>
>             * duration integer
>
>             * timeUnit string
>
>     * totp object
>
>       * enabled boolean
>
>       * otp object
>
>         * failure object
>
>           * count integer
>
>           * coolDown object
>
>             * duration integer
>
>             * timeUnit string
>
>     * platform object
>
>       * enabled boolean
>
>     * securityKey object
>
>       * enabled boolean
>
>     * rememberMe object
>
>       * web object
>
>         * enabled boolean
>
>         * lifeTime object
>
>           * duration integer
>
>           * timeUnit string
>
>     * createdAt string
>
>     * updatedAt string
>
>   * headers object
>
>   * statusCode integer
>
>   * deviceAuthenticationPolicy object
>
>     * id string
>
>     * name string
>
>     * forSignOnPolicy boolean
>
>     * default boolean
>
>     * sms object
>
>       * enabled boolean
>
>       * otp object
>
>         * failure object
>
>           * count integer
>
>           * coolDown object
>
>             * duration integer
>
>             * timeUnit string
>
>         * lifeTime object
>
>           * duration integer
>
>           * timeUnit string
>
>     * email object
>
>       * enabled boolean
>
>       * otp object
>
>         * failure object
>
>           * count integer
>
>           * coolDown object
>
>             * duration integer
>
>             * timeUnit string
>
>         * lifeTime object
>
>           * duration integer
>
>           * timeUnit string
>
>     * voice object
>
>       * enabled boolean
>
>       * otp object
>
>         * failure object
>
>           * count integer
>
>           * coolDown object
>
>             * duration integer
>
>             * timeUnit string
>
>         * lifeTime object
>
>           * duration integer
>
>           * timeUnit string
>
>     * mobile object
>
>       * enabled boolean
>
>       * otp object
>
>         * failure object
>
>           * count integer
>
>           * coolDown object
>
>             * duration integer
>
>             * timeUnit string
>
>         * window object
>
>           * stepSize object
>
>             * duration integer
>
>             * timeUnit string
>
>     * totp object
>
>       * enabled boolean
>
>       * otp object
>
>         * failure object
>
>           * count integer
>
>           * coolDown object
>
>             * duration integer
>
>             * timeUnit string
>
>     * platform object
>
>       * enabled boolean
>
>     * securityKey object
>
>       * enabled boolean
>
>     * rememberMe object
>
>       * web object
>
>         * enabled boolean
>
>         * lifeTime object
>
>           * duration integer
>
>           * timeUnit string
>
>     * createdAt string
>
>     * updatedAt string
>
> Output Example
>
> ```json
> {
>   "rawResponse": {
>     "deviceAuthenticationPolicy": {
>       "id": "58bet177-1871-420b-b1b5-4dcad2d07958",
>       "environment": {
>         "id": "14b3c9b9-107b-48ae-8c0a-e65f94054ebb"
>       },
>       "name": "Default For Sign On Policy",
>       "sms": {
>         "enabled": true,
>         "otp": {
>           "failure": {
>             "count": 3,
>             "coolDown": {
>               "duration": 0,
>               "timeUnit": "MINUTES"
>             }
>           },
>           "lifeTime": {
>             "duration": 30,
>             "timeUnit": "MINUTES"
>           }
>         }
>       },
>       "email": {
>         "enabled": true,
>         "otp": {
>           "failure": {
>             "count": 3,
>             "coolDown": {
>               "duration": 0,
>               "timeUnit": "MINUTES"
>             }
>           },
>           "lifeTime": {
>             "duration": 30,
>             "timeUnit": "MINUTES"
>           }
>         }
>       },
>       "voice": {
>         "enabled": true,
>         "otp": {
>           "failure": {
>             "count": 3,
>             "coolDown": {
>               "duration": 0,
>               "timeUnit": "MINUTES"
>             }
>           },
>           "lifeTime": {
>             "duration": 30,
>             "timeUnit": "MINUTES"
>           }
>         }
>       },
>       "mobile": {
>         "enabled": true,
>         "otp": {
>           "failure": {
>             "count": 3,
>             "coolDown": {
>               "duration": 0,
>               "timeUnit": "MINUTES"
>             }
>           },
>           "window": {
>             "stepSize": {
>               "duration": 30,
>               "timeUnit": "MINUTES"
>             }
>           }
>         }
>       },
>       "totp": {
>         "enabled": true,
>         "otp": {
>           "failure": {
>             "count": 3,
>             "coolDown": {
>               "duration": 0,
>               "timeUnit": "MINUTES"
>             }
>           }
>         }
>       },
>       "platform": {
>         "enabled": true
>       },
>       "securityKey": {
>         "enabled": true
>       },
>       "rememberMe": {
>         "web": {
>           "enabled": false,
>           "lifeTime": {
>             "duration": 30,
>             "timeUnit": "DAYS"
>           }
>         }
>       },
>       "createdAt": "2021-07-19T18:24:58.779Z",
>       "updatedAt": "2021-07-19T18:24:58.795Z"
>     }
>   }
> }
> ```

### Create Device Authentication

Create authentication experiences with virtual or physical devices.

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - User ID Not Required toggleSwitch
>
>   Indicates whether the user id is required or obtained from the authentication method used.
>
> - User ID textField
>
>   The unique identifier for the user.
>
> - MFA Policy ID textField
>
>   The ID of your PingOne MFA device authentication policy.
>
> - User Agent textField
>
>   Browser user agent
>
> - Device Details dropDown
>
>   Indicates whether to use the user's default authentication method or to provide a specific authentication method.
>
>   * ID
>
>   * One-Time Device
>
> - Device ID textField
>
>   The selected device id
>
> - Device Type textField
>
>   The one-time device type
>
> - SMS Phone Number textField
>
>   The phone number to associate with the one-time SMS device.
>
> - Voice Phone Number textField
>
>   The phone number to associate with the one-time Voice device.
>
> - Email textField
>
>   The email address to associate with the one-time device.
>
> - Test Mode textField
>
>   Create device for test purposes only
>
> - Notification Type dropDown
>
>   Indicates whether the notification is intended for a user authentication flow or a device authorization flow.
>
>   * Strong Authentication
>
>   * Transaction
>
> - Notification Policy dropDown
>
>   A unique identifier for the policy.
>
>   * Enter Notification Policy ID
>
> - * Notification Policy ID textField
>   * Notification Name dropDown
>
>   The name of a custom notification defined in PingOne. If the form you want is not listed, select Enter Custom Value.
>
>   * Enter Custom Value
>
> - Custom Value textField
>
>   You can enter a custom template name, or leave blank to use the default template. You can also enter a parameter from a previous connector, or any text.
>
> - Notification Locale textField
>
>   Add a locale to allow localized notifications for end-users. ISO Language Codes are supported.
>
> - Notification Variables variableInputList
>
>   If Custom variables are defined in the notification body, map them here.
>
> - Mobile Payload textField
>
>   A signed challenge generated by PingOne MFA mobile SDK.
>
> - Application dropDown
>
>   The unique identifier of the native application which initiated the authentication flow.
>
>   * Enter Application ID
>
> - * Application ID textField
>   * Mobile Client Context variableInputList
>
>   Additional attributes that can be passed to the mobile application during the authentication.
>
> - Relying Party ID textField
>
>   If you define a Relying Party ID (RPID) here, it overrides the RPID defined in the FIDO policy in the PingOne admin console.
>
> - Custom FIDO2 Challenge textField
>
>   Applicable for FIDO2 authentication requests. Specify a custom challenge that will replace the automatically generated challenge sent with the authentication request. Must be a valid Base64URL string that decodes to at least 32 bytes of data array.
>
> - One-time Passcode textField
>
>   The one-time passcode (OTP) of the device used to authenticate. If the Device ID is not provided, the OTP is validated against all the applicable devices.
>
> * default object
>
>   * properties object
>
>     * userId string minLength: 0 maxLength: 100
>
>     * mfaPolicyId string minLength: 0 maxLength: 100
>
>     * authTemplateName null/string
>
>       * string
>
>         * STRONG\_AUTHENTICATION
>
>         * TRANSACTION
>
>       * null
>
>     * notificationPolicyId string minLength: 0 maxLength: 100
>
>     * customNotificationPolicyId null/string/object
>
>     * templateVariant null/string
>
>     * customTemplateVariant null/string/object
>
>     * templateLocale null/string
>
>     * templateVariables array
>
>     * mobilePayload null/string
>
>       Mobile Payload
>
>     * applicationId string minLength: 0 maxLength: 100
>
>       Application ID
>
>     * customApplicationId null/string/object
>
>     * clientContext array
>
>       Mobile Client Context
>
>     * userAgent string
>
>       User Agent
>
>     * rpId string
>
>       Relying Party ID
>
>     * deviceAuthenRpId string
>
>       Relying Party ID
>
>     * challenge string
>
>       Custom FIDO2 Challenge
>
>     * createDeviceTestMode string
>
>       Create Test Device
>
>     * oneTimeDeviceTestMode string
>
>       Create Test Device
>
>     * usernameLess boolean
>
>       User ID Not Required
>
>     * selectedDevice null/string
>
>       * string
>
>         * id
>
>         * oneTime
>
>       * null
>
>     * selectedDeviceId null/string
>
>     * oneTimeDeviceType null/string
>
>       * string
>
>         * SMS
>
>         * VOICE
>
>         * EMAIL
>
>       * null
>
>     * oneTimeSmsDevice null/string
>
>     * oneTimeVoiceDevice null/string
>
>     * oneTimeEmailDevice null/string
>
>     * otp string
>
>       Passcode
>
> - output object
>
>   * rawResponse object
>
>     * id string
>
>     * user object
>
>       * id string
>
>     * environment object
>
>       * id string
>
>     * policy object
>
>       * id string
>
>     * selectedDevice object
>
>       * id string
>
>     * application object
>
>       * id string
>
>     * status string
>
>     * authenticators array
>
>     * publicKeyCredentialRequestOptions string
>
>     * \_links object
>
>     * \_embedded object
>
>       * devices array
>
>     * test object
>
>       * otp string
>
>   * headers object
>
>   * statusCode integer
>
> Output Example
>
> ```json
> {
>   "rawResponse": {
>     "id": "43eb5621-eae8-4fa1-aafb-2a884d6848cb",
>     "environment": {
>       "id": "9ad15e9e-3ac6-43f7-a053-d46b87d6c4a7"
>     },
>     "user": {
>       "id": "c362abbc-eeeb-4ea5-b9c1-097a376b0086"
>     },
>     "status": "OTP_REQUIRED",
>     "selectedDevice": {
>       "id": "9362abac-eeeb-6ea5-b9cc-097a375b0043"
>     },
>     "policy": {
>       "id": "6122abac-eeeb-6ea5-b9cc-097a375b0043"
>     },
>     "createdAt": "2021-01-15T20:45:17.463Z",
>     "updatedAt": "2021-01-15T20:45:17.463Z",
>     "_embedded": {
>       "devices": [
>         {
>           "type": "EMAIL",
>           "email": "o******@pingidentity.com"
>         }
>       ]
>     }
>   }
> }
> ```

### Read Device Authentication

Read device authentication information.

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - Device Authentication ID textField
>
>   The unique identifier for the MFA Device Authentication.
>
> * default object
>
>   * properties object
>
>     * deviceAuthenticationId string required minLength: 0 maxLength: 100
>
>       Device Authentication ID
>
> - output object
>
>   * rawResponse object
>
>     * id string
>
>     * user object
>
>       * id string
>
>     * environment object
>
>       * id string
>
>     * policy object
>
>       * id string
>
>     * selectedDevice object
>
>       * id string
>
>     * application object
>
>       * id string
>
>     * status string
>
>     * authenticators array
>
>     * publicKeyCredentialRequestOptions string
>
>     * \_links object
>
>     * \_embedded object
>
>       * devices array
>
>   * headers object
>
>   * statusCode integer
>
> Output Example
>
> ```json
> {
>   "rawResponse": {
>     "id": "43eb5621-eae8-4fa1-aafb-2a884d6848cb",
>     "environment": {
>       "id": "9ad15e9e-3ac6-43f7-a053-d46b87d6c4a7"
>     },
>     "user": {
>       "id": "c362abbc-eeeb-4ea5-b9c1-097a376b0086"
>     },
>     "status": "OTP_REQUIRED",
>     "selectedDevice": {
>       "id": "9362abac-eeeb-6ea5-b9cc-097a375b0043"
>     },
>     "policy": {
>       "id": "6122abac-eeeb-6ea5-b9cc-097a375b0043"
>     },
>     "createdAt": "2021-01-15T20:45:17.463Z",
>     "updatedAt": "2021-01-15T20:45:17.463Z",
>     "_embedded": {
>       "devices": [
>         {
>           "type": "EMAIL",
>           "email": "o******@pingidentity.com"
>         }
>       ]
>     }
>   }
> }
> ```

### Device Selection

Enables users to choose the way they authenticate if more than one option is available.

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - Device Authentication ID textField
>
>   The unique identifier for the MFA Device Authentication.
>
> - Device ID textField
>
>   The unique identifier for the MFA device.
>
> - WebAuthn Browser Compatibility textField
>
> * default object
>
>   * properties object
>
>     * deviceId string required minLength: 0 maxLength: 100
>
>     * deviceAuthenticationId string required minLength: 0 maxLength: 100
>
>       Device Authentication ID
>
>     * compatibility null/string
>
>       WebAuthn Compatibility
>
> - output object
>
>   * rawResponse object
>
>     * id string
>
>     * user object
>
>       * id string
>
>     * environment object
>
>       * id string
>
>     * policy object
>
>       * id string
>
>     * selectedDevice object
>
>       * id string
>
>     * application object
>
>       * id string
>
>     * status string
>
>     * authenticators array
>
>     * publicKeyCredentialRequestOptions string
>
>     * \_links object
>
>     * \_embedded object
>
>       * devices array
>
>   * headers object
>
>   * statusCode integer
>
> Output Example
>
> ```json
> {
>   "rawResponse": {
>     "id": "43eb5621-eae8-4fa1-aafb-2a884d6848cb",
>     "environment": {
>       "id": "9ad15e9e-3ac6-43f7-a053-d46b87d6c4a7"
>     },
>     "user": {
>       "id": "c362abbc-eeeb-4ea5-b9c1-097a376b0086"
>     },
>     "status": "OTP_REQUIRED",
>     "selectedDevice": {
>       "id": "9362abac-eeeb-6ea5-b9cc-097a375b0043"
>     },
>     "policy": {
>       "id": "6122abac-eeeb-6ea5-b9cc-097a375b0043"
>     },
>     "createdAt": "2021-01-15T20:45:17.463Z",
>     "updatedAt": "2021-01-15T20:45:17.463Z",
>     "_embedded": {
>       "devices": [
>         {
>           "type": "EMAIL",
>           "email": "o******@pingidentity.com"
>         }
>       ]
>     }
>   }
> }
> ```

### Device Passcode

Ensures that device one-time passcodes (OTPs) are valid.

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - Device Authentication ID textField
>
>   The unique identifier for the MFA Device Authentication.
>
> - One-time Passcode textField
>
>   The one-time passcode (OTP) sent to the user.
>
> * default object
>
>   * properties object
>
>     * otp string required
>
>       Passcode
>
>     * deviceAuthenticationId string required minLength: 0 maxLength: 100
>
>       Device Authentication ID
>
> - output object
>
>   * rawResponse object
>
>     * id string
>
>     * user object
>
>       * id string
>
>     * environment object
>
>       * id string
>
>     * policy object
>
>       * id string
>
>     * selectedDevice object
>
>       * id string
>
>     * application object
>
>       * id string
>
>     * status string
>
>     * authenticators array
>
>     * publicKeyCredentialRequestOptions string
>
>     * \_links object
>
>     * \_embedded object
>
>       * devices array
>
>   * headers object
>
>   * statusCode integer
>
> Output Example
>
> ```json
> {
>   "rawResponse": {
>     "id": "43eb5621-eae8-4fa1-aafb-2a884d6848cb",
>     "environment": {
>       "id": "9ad15e9e-3ac6-43f7-a053-d46b87d6c4a7"
>     },
>     "user": {
>       "id": "c362abbc-eeeb-4ea5-b9c1-097a376b0086"
>     },
>     "status": "OTP_REQUIRED",
>     "selectedDevice": {
>       "id": "9362abac-eeeb-6ea5-b9cc-097a375b0043"
>     },
>     "policy": {
>       "id": "6122abac-eeeb-6ea5-b9cc-097a375b0043"
>     },
>     "createdAt": "2021-01-15T20:45:17.463Z",
>     "updatedAt": "2021-01-15T20:45:17.463Z",
>     "_embedded": {
>       "devices": [
>         {
>           "type": "EMAIL",
>           "email": "o******@pingidentity.com"
>         }
>       ]
>     }
>   }
> }
> ```

### FIDO Assertion

Ensures that assertions provided to authenticate devices are valid.

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - Device Authentication ID textField
>
>   The unique identifier for the MFA Device Authentication.
>
> - Assertion textField
>
>   A string that specifies the authenticator assertion response. The string contains the signed challenge needed to complete the MFA authentication.
>
> - Origin textField
>
>   The address of the server sending the initial registration challenge to the device.
>
> - WebAuthn Browser Compatibility textField
>
> * default object
>
>   * properties object
>
>     * assertion string required
>
>       WebAuthn assertion
>
>     * origin string required
>
>       Origin
>
>     * deviceAuthenticationId string required minLength: 0 maxLength: 100
>
>       Device Authentication ID
>
> - output object
>
>   * rawResponse object
>
>     * id string
>
>     * user object
>
>       * id string
>
>     * environment object
>
>       * id string
>
>     * policy object
>
>       * id string
>
>     * selectedDevice object
>
>       * id string
>
>     * application object
>
>       * id string
>
>     * status string
>
>     * authenticators array
>
>     * publicKeyCredentialRequestOptions string
>
>     * \_links object
>
>     * \_embedded object
>
>       * devices array
>
>   * headers object
>
>   * statusCode integer
>
> Output Example
>
> ```json
> {
>   "rawResponse": {
>     "id": "43eb5621-eae8-4fa1-aafb-2a884d6848cb",
>     "environment": {
>       "id": "9ad15e9e-3ac6-43f7-a053-d46b87d6c4a7"
>     },
>     "user": {
>       "id": "c362abbc-eeeb-4ea5-b9c1-097a376b0086"
>     },
>     "status": "ASSERTION_REQUIRED",
>     "selectedDevice": {
>       "id": "9362abac-eeeb-6ea5-b9cc-097a375b0043"
>     },
>     "policy": {
>       "id": "6122abac-eeeb-6ea5-b9cc-097a375b0043"
>     },
>     "publicKeyCredentialRequestOptions": "{\"challenge\":[-85,59,-40,126,-17,11,-105,-114,-112,98,26,-11,65,108,101,35,106,81,-40,49,81,-68,5,48,-6,43,-107,-2,-115,68,15,81],\"timeout\":120000,\"rpId\":\"pingone.com\",\"allowCredentials\":[{\"type\":\"public-key\",\"id\":[1,62,-107,73,-122,23,-91,-57,-123,-52,121,-112,-115,30,112,13,-76,119,55,-87,-80,94,-71,-85,111,-102,-83,115,75,-106,-44,63,-71,-14,-93,9,-19,-63,-117,4,-98,-63,80,93,-19,-118,124,87,-63,21,-5,-86,79,-99,-114,-26,-1,-92,-110,67,127,39,38,-18,71]},{\"type\":\"public-key\",\"id\":[41,-87,-83,-39,39,126,-86,-71,-93,25,-10,-79,19,58,116,62,-52,14,127,-91,35,-117,1,117,9,124,10,-23,48,-119,16,89]}],\"userVerification\":\"preferred\"}",
>     "createdAt": "2021-01-15T20:45:17.463Z",
>     "updatedAt": "2021-01-15T20:45:17.463Z",
>     "_embedded": {
>       "devices": [
>         {
>           "type": "SECURITY_KEY",
>           "rp": {
>             "id": "pingone.com",
>             "name": "{pingone} MFA"
>           }
>         }
>       ]
>     }
>   }
> }
> ```

### Cancel Push Notification

Cancels the push notification sent to user's device if it hasn't been acted on.

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - Device Authentication ID textField
>
>   The unique identifier for the MFA Device Authentication.
>
> * default object
>
>   * properties object
>
>     * deviceAuthenticationId string required minLength: 0 maxLength: 100
>
>       Device Authentication ID
>
> - output object
>
>   * rawResponse object
>
>     * id string
>
>     * user object
>
>       * id string
>
>     * environment object
>
>       * id string
>
>     * selectedDevice object
>
>       * id string
>
>     * status string
>
>     * \_embedded object
>
>       * devices array
>
>   * headers object
>
>   * statusCode integer
>
> Output Example
>
> ```json
> {
>   "rawResponse": {
>     "_embedded": {
>       "devices": [
>         {
>           "id": "e1ad986f-1497-46a7-ad2c-631b4f8311dd",
>           "type": "MOBILE",
>           "status": "ACTIVE",
>           "usableStatus": {
>             "status": "ENABLED"
>           },
>           "deviceIntegrityState": {
>             "compromised": "UNKNOWN",
>             "reason": "PLAY_ERROR",
>             "timestamp": 1714468544848
>           },
>           "os": {
>             "version": "8",
>             "type": "iOS"
>           },
>           "apiVersion": "2.0",
>           "model": {
>             "name": "Iphone 12",
>             "marketingName": "Iphone 12"
>           },
>           "application": {
>             "id": "f0d76ca7-0b65-4e44-b272-794a91d87294",
>             "nativeName": "{pingone}Internal",
>             "version": "1.11.0",
>             "name": "NativeAppForInternalApp",
>             "pushSandbox": false,
>             "passcodeRefreshDuration": {
>               "duration": 30,
>               "timeUnit": "SECONDS"
>             }
>           },
>           "pushEnabled": true,
>           "manufacturer": "apple",
>           "sdkVersion": "1.11.0(9230)",
>           "rooted": false,
>           "lockEnabled": true,
>           "locale": "en-GB",
>           "notificationProvider": "APNS",
>           "notification": "enabled",
>           "background": "unknown",
>           "allowPushNotification": true,
>           "pushStatus": {
>             "status": "ENABLED"
>           },
>           "otpEnabled": true,
>           "otpStatus": {
>             "status": "ENABLED"
>           },
>           "pushFails": [
>             1714629982277
>           ]
>         }
>       ]
>     },
>     "id": "001c2d36-fa6a-402a-9842-96b30bc7af95",
>     "environment": {
>       "id": "9ffc5b7c-4c7e-4fcc-8834-964ab0b0f914"
>     },
>     "status": "DEVICE_SELECTION_REQUIRED",
>     "selectedDevice": {
>       "id": "e1ad986f-1497-46a7-ad2c-631b4f8311dd"
>     },
>     "user": {
>       "id": "d2f8be92-4dd6-4b65-891e-f1d20cec00a8"
>     },
>     "createdAt": "2024-05-02T06:05:48.362Z",
>     "updatedAt": "2024-05-02T06:06:22.290Z",
>     "aggregateFido2Devices": false
>   }
> }
> ```

### Read Pairing Key

Read pairing key information associated with users.

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - User ID textField
>
>   The unique identifier for the user.
>
> - Pairing Key ID textField
>
>   The unique identifier for the pairing key.
>
> * default object
>
>   * properties object
>
>     * userId string required minLength: 0 maxLength: 100
>
>     * pairingKeyId string required minLength: 0 maxLength: 100
>
>       Pairing Key ID
>
> - output object
>
>   * rawResponse object
>
>     * id string
>
>     * code string
>
>     * status string
>
>     * error object
>
>       * code string
>
>       * message string
>
>     * createdAt string
>
>     * updatedAt string
>
>     * expiresAt string
>
>   * headers object
>
>   * statusCode integer
>
> Output Example
>
> ```json
> {
>   "rawResponse": {
>     "id": "b47a7af3-598c-4bc9-9ad7-43e6bf5d8cca",
>     "environment": {
>       "id": "9f1b3773-aae5-4903-b3a2-837c5b6f6467"
>     },
>     "code": "01552143316127",
>     "status": "UNCLAIMED",
>     "applications": [
>       {
>         "id": "2a0d74e5-d856-44f5-ae21-7c3ec8d9ce37"
>       }
>     ],
>     "user": {
>       "id": "8dd4ed0f-391c-40d6-a1c9-ef0f6e3e8b40"
>     },
>     "createdAt": "2021-12-21T09:37:00.816Z",
>     "updatedAt": "2021-12-21T09:37:00.816Z",
>     "expiresAt": "2021-12-23T09:37:00.816Z"
>   }
> }
> ```

### Create Pairing Key

Create pairing keys that can be used by native mobile applications to create trust with PingOne MFA.

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - User ID textField
>
>   The unique identifier for the user.
>
> - Applications dropDownMultiSelect
>
>   Select the application(s) that can be used with this pairing key. Leave this list empty to allow all available native applications in the environment to be used.
>
> * default object
>
>   * properties object
>
>     * userId string required minLength: 0 maxLength: 100
>
>     * applicationIds null/array
>
>       * array
>
>       * null
>
> - output object
>
>   * rawResponse object
>
>     * id string
>
>     * code string
>
>     * status string
>
>     * error object
>
>       * code string
>
>       * message string
>
>     * createdAt string
>
>     * updatedAt string
>
>     * expiresAt string
>
>   * headers object
>
>   * statusCode integer
>
> Output Example
>
> ```json
> {
>   "rawResponse": {
>     "id": "b47a7af3-598c-4bc9-9ad7-43e6bf5d8cca",
>     "environment": {
>       "id": "9f1b3773-aae5-4903-b3a2-837c5b6f6467"
>     },
>     "code": "01552143316127",
>     "status": "UNCLAIMED",
>     "applications": [
>       {
>         "id": "2a0d74e5-d856-44f5-ae21-7c3ec8d9ce37"
>       }
>     ],
>     "user": {
>       "id": "8dd4ed0f-391c-40d6-a1c9-ef0f6e3e8b40"
>     },
>     "createdAt": "2021-12-21T09:37:00.816Z",
>     "updatedAt": "2021-12-21T09:37:00.816Z",
>     "expiresAt": "2021-12-23T09:37:00.816Z"
>   }
> }
> ```

### Delete Pairing Key

Delete unclaimed pairing keys.

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - User ID textField
>
>   The unique identifier for the user.
>
> - Pairing Key ID textField
>
>   The unique identifier for the pairing key.
>
> * default object
>
>   * properties object
>
>     * userId string required minLength: 0 maxLength: 100
>
>     * pairingKeyId string required minLength: 0 maxLength: 100
>
>       Pairing Key ID
>
> - output object
>
>   * rawResponse object
>
>   * headers object
>
>   * statusCode integer
>
> Output Example
>
> ```json
> {
>   "rawResponse": {}
> }
> ```

### Create Authentication Code

Create a single-use code to authenticate a user during sign-on using a mobile application. You can embed this code in a scannable QR code, or require that the user manually enter it to sign on.

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - Application dropDown
>
>   The unique identifier for the mobile application used to authenticate a user.
>
>   * Enter Application ID
>
> - * Application ID textField required
>   * Duration textField
>
>   The period of time that the authentication code is valid, which can be anywhere from 10 seconds to 30 minutes.
>
> - Time Unit dropDown required
>
>   The units of time used to indicate the authentication code duration.
>
>   * SECONDS (Default)
>
>   * MINUTES
>
> - User Approval dropDown
>
>   Specify whether the user will need to approve the authentication after they scan the authentication code using a mobile application.
>
>   * REQUIRED (Default)
>
>   * NOT\_REQUIRED
>
> - Mobile Client Context variableInputList
>
>   Additional attributes that can be passed to the mobile application during the authentication.
>
> * default object
>
>   * properties object
>
>     * authenticatingApplicationId string required minLength: 0 maxLength: 100
>
>       Application ID
>
>     * customAuthenticatingApplicationId null/string/object
>
>     * duration string required
>
>       Duration in seconds
>
>     * timeUnit string
>
>     * userApproval string required
>
>     * clientContext array
>
>       Mobile Client Context
>
> - output object
>
>   * rawResponse object
>
>     * id string
>
>     * code string
>
>     * uri string
>
>     * status string
>
>     * userApproval string
>
>     * user object
>
>       * id string
>
>     * lifeTime object
>
>       * duration integer
>
>       * timeUnit string
>
>     * clientContext object
>
>     * \_embedded object
>
>       * device object
>
>         * id string
>
>         * os object
>
>           * version string
>
>           * type string
>
>         * model object
>
>           * name string
>
>           * marketingName string
>
>         * application object
>
>           * nativeName string
>
>           * version string
>
>     * error object
>
>       * code string
>
>       * message string
>
>     * createdAt string
>
>     * updatedAt string
>
>     * expiresAt string
>
>   * headers object
>
>   * statusCode integer
>
>   * authenticationCode object
>
>     * id string
>
>     * code string
>
>     * uri string
>
>     * status string
>
>     * userApproval string
>
>     * user object
>
>       * id string
>
>     * lifeTime object
>
>       * duration integer
>
>       * timeUnit string
>
>     * clientContext object
>
>     * \_embedded object
>
>       * device object
>
>         * id string
>
>         * os object
>
>           * version string
>
>           * type string
>
>         * model object
>
>           * name string
>
>           * marketingName string
>
>         * application object
>
>           * nativeName string
>
>           * version string
>
>     * error object
>
>       * code string
>
>       * message string
>
>     * createdAt string
>
>     * updatedAt string
>
>     * expiresAt string
>
> Output Example
>
> ```json
> {
>   "rawResponse": {
>     "id": "b47a7af3-598c-4bc9-9ad7-43e6bf5d8cca",
>     "environment": {
>       "id": "9f1b3773-aae5-4903-b3a2-837c5b6f6467"
>     },
>     "code": "HP2EG68O",
>     "uri": "pingonesdk?authentication_code=HP2EG68O",
>     "applications": [
>       {
>         "id": "2a0d74e5-d856-44f5-ae21-7c3ec8d9ce37"
>       }
>     ],
>     "lifeTime": {
>       "duration": 10,
>       "timeUnit": "SECONDS"
>     },
>     "userApproval": "NOT_REQUIRED",
>     "status": "UNCLAIMED",
>     "clientContext": {
>       "var1": "hello world",
>       "var2": 3
>     },
>     "_embedded": {
>       "device": {
>         "id": "dec6f008-b40e-45fd-a7ef-f255f77c5990",
>         "os": {
>           "version": "12",
>           "type": "ANDROID"
>         },
>         "model": {
>           "name": "SM-G991B",
>           "marketingName": "SM-G991B"
>         },
>         "application": {
>           "nativeName": "{pingone}Internal",
>           "version": "1.7.0"
>         }
>       }
>     },
>     "user": {
>       "id": "bec1b927-d1fb-494f-9bb5-bbe4f625f7bb"
>     },
>     "createdAt": "2021-12-21T09:37:00.816Z",
>     "updatedAt": "2021-12-21T09:37:00.816Z",
>     "expiresAt": "2021-12-23T09:37:00.816Z"
>   }
> }
> ```

### Read Authentication Code

Read the authentication code.

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - Authentication Code ID textField
>
>   The unique identifier for the authentication code.
>
> * default object
>
>   * properties object
>
>     * authenticationCodeId string required minLength: 0 maxLength: 100
>
>       Authentication Code ID
>
> - output object
>
>   * rawResponse object
>
>     * id string
>
>     * code string
>
>     * uri string
>
>     * status string
>
>     * userApproval string
>
>     * user object
>
>       * id string
>
>     * lifeTime object
>
>       * duration integer
>
>       * timeUnit string
>
>     * clientContext object
>
>     * \_embedded object
>
>       * device object
>
>         * id string
>
>         * os object
>
>           * version string
>
>           * type string
>
>         * model object
>
>           * name string
>
>           * marketingName string
>
>         * application object
>
>           * nativeName string
>
>           * version string
>
>     * error object
>
>       * code string
>
>       * message string
>
>     * createdAt string
>
>     * updatedAt string
>
>     * expiresAt string
>
>   * headers object
>
>   * statusCode integer
>
>   * authenticationCode object
>
>     * id string
>
>     * code string
>
>     * uri string
>
>     * status string
>
>     * userApproval string
>
>     * user object
>
>       * id string
>
>     * lifeTime object
>
>       * duration integer
>
>       * timeUnit string
>
>     * clientContext object
>
>     * \_embedded object
>
>       * device object
>
>         * id string
>
>         * os object
>
>           * version string
>
>           * type string
>
>         * model object
>
>           * name string
>
>           * marketingName string
>
>         * application object
>
>           * nativeName string
>
>           * version string
>
>     * error object
>
>       * code string
>
>       * message string
>
>     * createdAt string
>
>     * updatedAt string
>
>     * expiresAt string
>
> Output Example
>
> ```json
> {
>   "rawResponse": {
>     "id": "b47a7af3-598c-4bc9-9ad7-43e6bf5d8cca",
>     "environment": {
>       "id": "9f1b3773-aae5-4903-b3a2-837c5b6f6467"
>     },
>     "code": "HP2EG68O",
>     "uri": "pingonesdk?authentication_code=HP2EG68O",
>     "applications": [
>       {
>         "id": "2a0d74e5-d856-44f5-ae21-7c3ec8d9ce37"
>       }
>     ],
>     "lifeTime": {
>       "duration": 10,
>       "timeUnit": "SECONDS"
>     },
>     "userApproval": "NOT_REQUIRED",
>     "status": "UNCLAIMED",
>     "clientContext": {
>       "var1": "hello world",
>       "var2": 3
>     },
>     "_embedded": {
>       "device": {
>         "id": "dec6f008-b40e-45fd-a7ef-f255f77c5990",
>         "os": {
>           "version": "12",
>           "type": "ANDROID"
>         },
>         "model": {
>           "name": "SM-G991B",
>           "marketingName": "SM-G991B"
>         },
>         "application": {
>           "nativeName": "{pingone}Internal",
>           "version": "1.7.0"
>         }
>       }
>     },
>     "user": {
>       "id": "bec1b927-d1fb-494f-9bb5-bbe4f625f7bb"
>     },
>     "createdAt": "2021-12-21T09:37:00.816Z",
>     "updatedAt": "2021-12-21T09:37:00.816Z",
>     "expiresAt": "2021-12-23T09:37:00.816Z"
>   }
> }
> ```

### Set Device Order

Setting the device order explicitly orders a user's existing active devices

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - User ID textField
>
>   The unique identifier for the user.
>
> - Set Device Order dropDown
>
>   Select how to set the device order
>
>   * Set default device
>
>   * Set device order
>
> - Device ID textField
>
>   Enter the device ID of the device which should be set as the default device.
>
> - * Input attributes as JSON? toggleSwitch
>   * Set Device Order multipleTextFields
>
>   Enter the device IDs in the order that the devices should be listed for the user.
>
> - Attributes codeEditor
>
>   An array of objects that determines the explicit order of a user's devices. The first device listed becomes the default device. This property is used as a body parameter to set the order of existing devices.
>
>   Default:
>
>   ```none
>   {
>    "order": [
>    {
>    "id": "{{deviceID}}"
>    },
>    {
>    "id": "{{deviceID2}}"
>    }
>    ]
>   }
>   ```
>
> * default object
>
>   * properties object
>
>     * userId string required minLength: 0 maxLength: 100
>
>     * setDeviceOrder string
>
>     * defaultDeviceId string minLength: 0 maxLength: 100
>
>     * useDeviceOrderJsonAttributes boolean
>
>     * deviceOrderList array
>
>     * jsonAttributes null/string/object
>
> - output object
>
>   * rawResponse object
>
>     * \_embedded object
>
>       * devices array
>
>       * applications array
>
>       * allowedtypes array
>
>       * order array
>
>         * id string
>
>       * mfaSettings object
>
>         * environment object
>
>           * id string
>
>         * pairing object
>
>           * maxAllowedDevices integer
>
>       * mfaPolicy object
>
>         * authentication object
>
>           * deviceSelection string
>
>     * size number
>
>   * headers object
>
>   * statusCode integer
>
>   * devices array
>
>   * order array
>
>     * id string
>
> Output Example
>
> ```json
> {
>   "rawResponse": {
>     "_embedded": {
>       "devices": [
>         {
>           "device": {
>             "id": "43eb5621-eae8-4fa1-aafb-2a884d6848cb",
>             "type": "SMS",
>             "status": "ACTIVE",
>             "nickname": "Work Device",
>             "phone": "+972528888888",
>             "extension": "###1",
>             "createdAt": "2021-01-15T20:45:17.463Z",
>             "updatedAt": "2021-01-15T20:45:17.463Z"
>           }
>         }
>       ],
>       "applications": [
>         {
>           "id": "43eb4421-eae8-4fa1-aafb-2a884d6848cb",
>           "environment": {
>             "id": "143459b9-107b-48ae-8c0a-e65f94054ebb"
>           },
>           "name": "IOS nativeApp",
>           "enabled": true,
>           "mobile": {
>             "bundleId": "com.pingIdentity.p14c.sample",
>             "integrityDetection": {
>               "mode": "DISABLED"
>             }
>           }
>         }
>       ],
>       "allowedtypes": [
>         "SMS",
>         "VOICE",
>         "MOBILE",
>         "TOTP",
>         "OATH_TOKEN",
>         "YUBIKEY",
>         "PINGID_DESKTOP",
>         "PLATFORM",
>         "SECURITY_KEY"
>       ],
>       "order": [
>         {
>           "id": "43eb5621-eae8-4fa1-aafb-2a884d6848cb"
>         },
>         {
>           "id": "01f3db05-93b6-4c45-a93e-f9ac84d076c6"
>         }
>       ],
>       "mfaSettings": {
>         "environment": {
>           "id": "143459b9-107b-48ae-8c0a-e65f94054ebb"
>         },
>         "pairing": {
>           "maxAllowedDevices": 5
>         }
>       },
>       "mfaPolicy": {
>         "authentication": {
>           "deviceSelection": "DEFAULT_TO_FIRST"
>         }
>       }
>     },
>     "count": 1,
>     "size": 1
>   },
>   "devices": [
>     {
>       "device": {
>         "id": "43eb5621-eae8-4fa1-aafb-2a884d6848cb",
>         "type": "SMS",
>         "status": "ACTIVE",
>         "nickname": "Work Device",
>         "phone": "+972528888888",
>         "extension": "###1",
>         "createdAt": "2021-01-15T20:45:17.463Z",
>         "updatedAt": "2021-01-15T20:45:17.463Z"
>       }
>     }
>   ],
>   "applications": [
>     {
>       "id": "43eb4421-eae8-4fa1-aafb-2a884d6848cb",
>       "environment": {
>         "id": "143459b9-107b-48ae-8c0a-e65f94054ebb"
>       },
>       "name": "IOS nativeApp",
>       "enabled": true,
>       "mobile": {
>         "bundleId": "com.pingIdentity.p14c.sample",
>         "integrityDetection": {
>           "mode": "DISABLED"
>         }
>       }
>     }
>   ],
>   "allowedtypes": [
>     "SMS",
>     "VOICE",
>     "MOBILE",
>     "TOTP",
>     "OATH_TOKEN",
>     "YUBIKEY",
>     "PINGID_DESKTOP",
>     "PLATFORM",
>     "SECURITY_KEY"
>   ],
>   "order": [
>     {
>       "id": "43eb5621-eae8-4fa1-aafb-2a884d6848cb"
>     },
>     {
>       "id": "01f3db05-93b6-4c45-a93e-f9ac84d076c6"
>     }
>   ],
>   "mfaSettings": {
>     "environment": {
>       "id": "143459b9-107b-48ae-8c0a-e65f94054ebb"
>     },
>     "pairing": {
>       "maxAllowedDevices": 5
>     }
>   },
>   "mfaPolicy": {
>     "authentication": {
>       "deviceSelection": "DEFAULT_TO_FIRST"
>     }
>   }
> }
> ```

### Cancel Device Authentication

Cancel the authentication process for a specific device.

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - Device Authentication ID textField
>
>   The unique identifier for the MFA Device Authentication.
>
> - Reason For Cancellation\n textField
>
>   The reason that the authentication was canceled.
>
>   Possible values are SIGNOUT, CHANGE\_DEVICE, ADD\_DEVICE. Any other reason will get the value - DEFAULT.
>
> * default object
>
>   * properties object
>
>     * reason string
>
>       Reason
>
>     * deviceAuthenticationId string required minLength: 0 maxLength: 100
>
>       Device Authentication ID
>
> - output object
>
>   * rawResponse object
>
>     * id string
>
>     * user object
>
>       * id string
>
>     * environment object
>
>       * id string
>
>     * policy object
>
>       * id string
>
>     * selectedDevice object
>
>       * id string
>
>     * application object
>
>       * id string
>
>     * status string
>
>     * authenticators array
>
>     * publicKeyCredentialRequestOptions string
>
>     * \_links object
>
>     * \_embedded object
>
>       * devices array
>
>   * headers object
>
>   * statusCode integer
>
> Output Example
>
> ```json
> {
>   "rawResponse": {
>     "id": "43eb5621-eae8-4fa1-aafb-2a884d6848cb",
>     "environment": {
>       "id": "9ad15e9e-3ac6-43f7-a053-d46b87d6c4a7"
>     },
>     "user": {
>       "id": "c362abbc-eeeb-4ea5-b9c1-097a376b0086"
>     },
>     "status": "OTP_REQUIRED",
>     "selectedDevice": {
>       "id": "9362abac-eeeb-6ea5-b9cc-097a375b0043"
>     },
>     "policy": {
>       "id": "6122abac-eeeb-6ea5-b9cc-097a375b0043"
>     },
>     "createdAt": "2021-01-15T20:45:17.463Z",
>     "updatedAt": "2021-01-15T20:45:17.463Z",
>     "_embedded": {
>       "devices": [
>         {
>           "type": "EMAIL",
>           "email": "o******@pingidentity.com"
>         }
>       ]
>     }
>   }
> }
> ```

### Create Device

Create devices to use during authentication.

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - User ID textField
>
>   The unique identifier for the user.
>
> - Device Type textField
>
>   The type of device used during authentication. Supported values are: SMS, EMAIL, VOICE, TOTP, YUBIKEY, OATH\_TOKEN, PLATFORM, SECURITY\_KEY, FIDO2.
>
> - Activation Status dropDown
>
>   The current status of the device. If a device has an ACTIVATION\_REQUIRED status, activate it before you add it as a trusted device.
>
>   * ACTIVE
>
>   * ACTIVATION REQUIRED
>
> - Phone Number textField
>
>   The phone number to associate with the device. Applies only to devices that use SMS and Voice SMS messages during authentication.
>
> - Email textField
>
>   The email address to associate with the device. Applies only to devices that use email during authentication.
>
> - Device Nickname textField
>
>   A nickname that identifies this device. The device nickname is limited to 100 characters.
>
> - Relying Party ID textField
>
>   If you define a Relying Party ID (RPID) here, it overrides the RPID defined in the FIDO policy in the PingOne admin console.
>
> - Relying Party Name textField
>
>   A string that specifies the relying party's human-readable display name.
>
> - YubiKey textField
>
>   The one-time passcode used to authenticate the YubiKey.
>
> - Serial Number textField
>
>   The unique identifier for the OAuth token.
>
> - User Agent textField
>
>   Browser user agent
>
> - Custom FIDO2 Challenge textField
>
>   Applicable for FIDO2 pairing requests. Specify a custom challenge that will replace the automatically generated challenge sent with the pairing request. Must be a valid Base64URL string that decodes to at least 32 bytes of data array.
>
> - MFA Policy ID textField
>
>   The ID of the PingID policy evaluation.
>
> * default object
>
>   * properties object
>
>     * userId string required minLength: 0 maxLength: 100
>
>     * workforceDeviceType string required
>
>     * status string required
>
>     * nickname string
>
>     * phone string
>
>     * email string
>
>     * rpId string
>
>       Relying Party ID
>
>     * rpName string
>
>       Relying Party Name
>
>     * userAgent string
>
>       User Agent
>
>     * challenge string
>
>       Custom FIDO2 Challenge
>
>     * workforcePolicyMfaPolicyId string minLength: 0 maxLength: 100
>
> - output object
>
>   * rawResponse object
>
>     * id string
>
>     * type string
>
>     * status string
>
>     * nickname string
>
>     * phone string
>
>     * extension string
>
>     * email string
>
>     * secret string
>
>     * keyUri string
>
>     * oathToken string
>
>     * serialNumber string
>
>     * rp object
>
>       * id string
>
>       * name string
>
>     * platform string
>
>     * publicKeyCredentialCreationOptions string
>
>     * attributes object
>
>       * previousDeviceType string
>
>       * isCrossPlatform boolean
>
>     * displayName string
>
>     * createdAt string
>
>     * updatedAt string
>
>     * test object
>
>       * otp string
>
>   * headers object
>
>   * statusCode integer
>
>   * device object
>
>     * id string
>
>     * type string
>
>     * status string
>
>     * nickname string
>
>     * phone string
>
>     * extension string
>
>     * email string
>
>     * secret string
>
>     * keyUri string
>
>     * oathToken string
>
>     * serialNumber string
>
>     * rp object
>
>       * id string
>
>       * name string
>
>     * platform string
>
>     * publicKeyCredentialCreationOptions string
>
>     * attributes object
>
>       * previousDeviceType string
>
>       * isCrossPlatform boolean
>
>     * displayName string
>
>     * createdAt string
>
>     * updatedAt string
>
> Output Example
>
> ```json
> {
>   "rawResponse": {
>     "device": {
>       "id": "43eb5621-eae8-4fa1-aafb-2a884d6848cb",
>       "type": "SMS",
>       "status": "ACTIVE",
>       "nickname": "Work Device",
>       "phone": "+972528888888",
>       "extension": "###1",
>       "createdAt": "2021-01-15T20:45:17.463Z",
>       "updatedAt": "2021-01-15T20:45:17.463Z"
>     }
>   }
> }
> ```

### Create Device Authentication

Create authentication experiences with virtual or physical devices.

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - User ID Not Required toggleSwitch
>
>   Indicates whether the user id is required or obtained from the authentication method used.
>
> - User ID textField
>
>   The unique identifier for the user.
>
> - MFA Policy ID textField
>
>   The ID of the PingID policy evaluation.
>
> - User Agent textField
>
>   Browser user agent
>
> - Device Details dropDown
>
>   Indicates whether to use the user's default authentication method or to provide a specific authentication method.
>
>   * ID
>
>   * One-Time Device
>
> - Device ID textField
>
>   The selected device id
>
> - Device Type textField
>
>   The one-time device type
>
> - SMS Phone Number textField
>
>   The phone number to associate with the one-time SMS device.
>
> - Voice Phone Number textField
>
>   The phone number to associate with the one-time Voice device.
>
> - Email textField
>
>   The email address to associate with the one-time device.
>
> - Relying Party ID textField
>
>   If you define a Relying Party ID (RPID) here, it overrides the RPID defined in the FIDO policy in the PingOne admin console.
>
> - * WebAuthn Browser Compatibility textField
>   * Custom FIDO2 Challenge textField
>
>   Applicable for FIDO2 authentication requests. Specify a custom challenge that will replace the automatically generated challenge sent with the authentication request. Must be a valid Base64URL string that decodes to at least 32 bytes of data array.
>
> - FIDO Compatibility textField
>
>   A string that specifies the FIDO Authenticators that are allowed to be used. Options are FULL (compatible with FIDO2, platform biometrics, and security key) and NONE (not compatible with FIDO).
>
> - One-time Passcode textField
>
>   The one-time passcode (OTP) of the device used to authenticate. If the Device ID is not provided, the OTP is validated against all the applicable devices.
>
> - IP textField
>
>   The IP address of the user who initiated the flow.
>
> - Application Name textField
>
>   The name of the application being authenticated.
>
> * default object
>
>   * properties object
>
>     * userId string minLength: 0 maxLength: 100
>
>     * workforcePolicyMfaPolicyId string minLength: 0 maxLength: 100
>
>     * userAgent string
>
>       User Agent
>
>     * rpId string
>
>       Relying Party ID
>
>     * deviceAuthenRpId string
>
>       Relying Party ID
>
>     * createDeviceTestMode string
>
>       Create Test Device
>
>     * oneTimeDeviceTestMode string
>
>       Create Test Device
>
>     * usernameLess boolean
>
>       User ID Not Required
>
>     * selectedDevice null/string
>
>       * string
>
>         * id
>
>         * oneTime
>
>       * null
>
>     * selectedDeviceId null/string
>
>     * oneTimeDeviceType null/string
>
>       * string
>
>         * SMS
>
>         * VOICE
>
>         * EMAIL
>
>       * null
>
>     * oneTimeSmsDevice null/string
>
>     * oneTimeVoiceDevice null/string
>
>     * oneTimeEmailDevice null/string
>
>     * challenge string
>
>       Custom FIDO2 Challenge
>
>     * fidoCompatibility null/string
>
>       WebAuthn Compatibility
>
>     * compatibility null/string
>
>       WebAuthn Compatibility
>
>     * otp string
>
>       Passcode
>
>     * ip string
>
>       IP
>
>     * applicationName string minLength: 0 maxLength: 100
>
>       The name of the application being authenticated
>
> - output object
>
>   * rawResponse object
>
>     * id string
>
>     * user object
>
>       * id string
>
>     * environment object
>
>       * id string
>
>     * policy object
>
>       * id string
>
>     * selectedDevice object
>
>       * id string
>
>     * application object
>
>       * id string
>
>     * status string
>
>     * authenticators array
>
>     * publicKeyCredentialRequestOptions string
>
>     * \_links object
>
>     * \_embedded object
>
>       * devices array
>
>     * test object
>
>       * otp string
>
>   * headers object
>
>   * statusCode integer
>
> Output Example
>
> ```json
> {
>   "rawResponse": {
>     "id": "43eb5621-eae8-4fa1-aafb-2a884d6848cb",
>     "environment": {
>       "id": "9ad15e9e-3ac6-43f7-a053-d46b87d6c4a7"
>     },
>     "user": {
>       "id": "c362abbc-eeeb-4ea5-b9c1-097a376b0086"
>     },
>     "status": "OTP_REQUIRED",
>     "selectedDevice": {
>       "id": "9362abac-eeeb-6ea5-b9cc-097a375b0043"
>     },
>     "policy": {
>       "id": "6122abac-eeeb-6ea5-b9cc-097a375b0043"
>     },
>     "createdAt": "2021-01-15T20:45:17.463Z",
>     "updatedAt": "2021-01-15T20:45:17.463Z",
>     "_embedded": {
>       "devices": [
>         {
>           "type": "EMAIL",
>           "email": "o******@pingidentity.com"
>         }
>       ]
>     }
>   }
> }
> ```

### Create Pairing Key

Create pairing keys that can be used by the PingID mobile app to create trust with PingID.

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - User ID textField
>
>   The unique identifier for the user.
>
> - Applications dropDownMultiSelect
>
>   Select the application(s) that can be used with this pairing key. Leave this list empty to allow all available native applications in the environment to be used.
>
> - MFA Policy ID textField
>
>   The ID of the PingID policy evaluation.
>
> * default object
>
>   * properties object
>
>     * userId string required minLength: 0 maxLength: 100
>
>     * applicationIds null/array
>
>       * array
>
>       * null
>
>     * workforcePolicyMfaPolicyId string minLength: 0 maxLength: 100
>
> - output object
>
>   * rawResponse object
>
>     * id string
>
>     * code string
>
>     * status string
>
>     * error object
>
>       * code string
>
>       * message string
>
>     * createdAt string
>
>     * updatedAt string
>
>     * expiresAt string
>
>   * headers object
>
>   * statusCode integer
>
> Output Example
>
> ```json
> {
>   "rawResponse": {
>     "id": "b47a7af3-598c-4bc9-9ad7-43e6bf5d8cca",
>     "environment": {
>       "id": "9f1b3773-aae5-4903-b3a2-837c5b6f6467"
>     },
>     "code": "01552143316127",
>     "status": "UNCLAIMED",
>     "applications": [
>       {
>         "id": "2a0d74e5-d856-44f5-ae21-7c3ec8d9ce37"
>       }
>     ],
>     "user": {
>       "id": "8dd4ed0f-391c-40d6-a1c9-ef0f6e3e8b40"
>     },
>     "createdAt": "2021-12-21T09:37:00.816Z",
>     "updatedAt": "2021-12-21T09:37:00.816Z",
>     "expiresAt": "2021-12-23T09:37:00.816Z"
>   }
> }
> ```

### Read All Devices

Read information for all user devices

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - User ID textField
>
>   The unique identifier for the user.
>
> - Filters toggleSwitch
>
>   Filter devices by activation status and device type.
>
> - Status dropDown
>
>   non-active devices are not usable during an authentication.
>
>   * ALL (Default)
>
>   * ACTIVE
>
>   * ACTIVATION REQUIRED
>
> - Device Types dropDownMultiSelect
>
>   * Email
>
>   * SMS
>
>   * Voice
>
>   * Authenticator App
>
>   * Fido2 Biometrics
>
>   * Security Key
>
>   * Oath token
>
>   * YubiKey
>
>   * Desktop app
>
>   * PingID Mobile app
>
> * default object
>
>   * properties object
>
>     * userId string required minLength: 0 maxLength: 100
>
>     * setFilterFlag boolean
>
>     * statusFilter string
>
>     * workforceDeviceTypes array uniqueItems: true
>
> - output object
>
>   * rawResponse object
>
>     * \_embedded object
>
>       * devices array
>
>       * applications array
>
>       * allowedtypes array
>
>       * order array
>
>         * id string
>
>       * mfaSettings object
>
>         * environment object
>
>           * id string
>
>         * pairing object
>
>           * maxAllowedDevices integer
>
>       * mfaPolicy object
>
>         * authentication object
>
>           * deviceSelection string
>
>     * size number
>
>   * headers object
>
>   * statusCode integer
>
>   * devices array
>
>   * allowedtypes array
>
>   * applications array
>
>   * mfaSettings object
>
>     * environment object
>
>       * id string
>
>     * pairing object
>
>       * maxAllowedDevices integer
>
>   * mfaPolicy object
>
>     * authentication object
>
>       * deviceSelection string
>
>   * order array
>
>     * id string
>
> Output Example
>
> ```json
> {
>   "rawResponse": {
>     "_embedded": {
>       "devices": [
>         {
>           "device": {
>             "id": "43eb5621-eae8-4fa1-aafb-2a884d6848cb",
>             "type": "SMS",
>             "status": "ACTIVE",
>             "nickname": "Work Device",
>             "phone": "+972528888888",
>             "extension": "###1",
>             "createdAt": "2021-01-15T20:45:17.463Z",
>             "updatedAt": "2021-01-15T20:45:17.463Z"
>           }
>         }
>       ],
>       "applications": [
>         {
>           "id": "43eb4421-eae8-4fa1-aafb-2a884d6848cb",
>           "environment": {
>             "id": "143459b9-107b-48ae-8c0a-e65f94054ebb"
>           },
>           "name": "IOS nativeApp",
>           "enabled": true,
>           "mobile": {
>             "bundleId": "com.pingIdentity.p14c.sample",
>             "integrityDetection": {
>               "mode": "DISABLED"
>             }
>           }
>         }
>       ],
>       "allowedtypes": [
>         "SMS",
>         "VOICE",
>         "MOBILE",
>         "TOTP",
>         "OATH_TOKEN",
>         "YUBIKEY",
>         "PINGID_DESKTOP",
>         "PLATFORM",
>         "SECURITY_KEY"
>       ],
>       "order": [
>         {
>           "id": "43eb5621-eae8-4fa1-aafb-2a884d6848cb"
>         },
>         {
>           "id": "01f3db05-93b6-4c45-a93e-f9ac84d076c6"
>         }
>       ],
>       "mfaSettings": {
>         "environment": {
>           "id": "143459b9-107b-48ae-8c0a-e65f94054ebb"
>         },
>         "pairing": {
>           "maxAllowedDevices": 5
>         }
>       },
>       "mfaPolicy": {
>         "authentication": {
>           "deviceSelection": "DEFAULT_TO_FIRST"
>         }
>       }
>     },
>     "count": 1,
>     "size": 1
>   },
>   "devices": [
>     {
>       "device": {
>         "id": "43eb5621-eae8-4fa1-aafb-2a884d6848cb",
>         "type": "SMS",
>         "status": "ACTIVE",
>         "nickname": "Work Device",
>         "phone": "+972528888888",
>         "extension": "###1",
>         "createdAt": "2021-01-15T20:45:17.463Z",
>         "updatedAt": "2021-01-15T20:45:17.463Z"
>       }
>     }
>   ],
>   "applications": [
>     {
>       "id": "43eb4421-eae8-4fa1-aafb-2a884d6848cb",
>       "environment": {
>         "id": "143459b9-107b-48ae-8c0a-e65f94054ebb"
>       },
>       "name": "IOS nativeApp",
>       "enabled": true,
>       "mobile": {
>         "bundleId": "com.pingIdentity.p14c.sample",
>         "integrityDetection": {
>           "mode": "DISABLED"
>         }
>       }
>     }
>   ],
>   "allowedtypes": [
>     "SMS",
>     "VOICE",
>     "MOBILE",
>     "TOTP",
>     "OATH_TOKEN",
>     "YUBIKEY",
>     "PINGID_DESKTOP",
>     "PLATFORM",
>     "SECURITY_KEY"
>   ],
>   "order": [
>     {
>       "id": "43eb5621-eae8-4fa1-aafb-2a884d6848cb"
>     },
>     {
>       "id": "01f3db05-93b6-4c45-a93e-f9ac84d076c6"
>     }
>   ],
>   "mfaSettings": {
>     "environment": {
>       "id": "143459b9-107b-48ae-8c0a-e65f94054ebb"
>     },
>     "pairing": {
>       "maxAllowedDevices": 5
>     }
>   },
>   "mfaPolicy": {
>     "authentication": {
>       "deviceSelection": "DEFAULT_TO_FIRST"
>     }
>   }
> }
> ```

### Evaluate Policy

Evaluate PingID policy

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - User ID textField
>
>   The unique identifier for the user.
>
> - IP textField
>
>   The IP of the requesting device.
>
> - User Agent textField
>
>   The requesting device's user agent.
>
> - Application Id textField
>
>   The ID of the application being authenticated.
>
> - Application Name textField
>
>   The name of the application being authenticated.
>
> - Risk Level textField
>
>   The Risk Level score that is received from the Risk management service.
>
> - User Groups textField
>
>   The groups that the user is part of.
>
> - Last MFA transaction dropDown
>
>   Details of the last Multi-factor authentication (MFA) transaction.
>
>   * PingOne Cookie
>
>   * Custom
>
> - Last sign-on details textField
>
>   Enter the last sign-on section from the PingOne Cookie.
>
> - Last transaction IP textField
>
>   The IP address of the most recent transaction.
>
> - Last transaction authentication method textField
>
>   The authentication method used for the most recent transaction.
>
> - Last transaction time textField
>
>   The time at which the most recent transaction occurred.
>
> * default object
>
>   * properties object
>
>     * userId string required minLength: 0 maxLength: 100
>
>     * ip string
>
>     * riskLevel string
>
>     * applicationName string
>
>     * applicationId string
>
>     * userAgent string
>
>     * groups array
>
>     * lastMFATransaction null/string
>
>       * string
>
>         * pingoneCookieLastTransaction
>
>         * customLastTransaction
>
>       * null
>
>     * policyRecentPingOneCookie string
>
>     * policyRecentAuthMethod string
>
>     * policyRecentIp string
>
>     * policyRecentAuthTimestamp string
>
> - output object
>
>   * rawResponse object
>
>     * action string
>
>     * id string
>
>   * headers object
>
>   * statusCode integer
>
> Output Example
>
> ```json
> {
>   "rawResponse": {
>     "action": "AUTHENTICATE",
>     "id": "1a14fe10-56c9-449e-9609-bfe1d6984ffd"
>   }
> }
> ```

### Create Remembered Device

Create a known accessing device

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - User ID textField
>
>   The unique identifier for the user.
>
> - MFA Policy ID textField
>
>   The ID of your PingOne MFA device authentication policy.
>
> - Session ID textField
>
>   The active PingOne session for the user.
>
> - Device Type dropDown
>
>   * Browser
>
> - Payload textField
>
>   Identify the device via a unique device ID combined with a digital signature that ensures information collected about the device has not been tampered with.
>
> - Check Last Authentication Method textField
>
>   Check if the last authentication method used to remember the accessing device matches an allowed authentication method in the current MFA policy being used.
>
> * default object
>
>   * properties object
>
>     * userId string required minLength: 0 maxLength: 100
>
>     * mfaPolicyId string minLength: 0 maxLength: 100
>
>     * rememberMeDeviceType string required
>
>     * rememberMePayload string required
>
>     * rememberMeCookie string
>
> - output object
>
>   * rawResponse object
>
>     * id string
>
>     * type string
>
>     * status string
>
>     * nickname string
>
>     * phone string
>
>     * extension string
>
>     * email string
>
>     * secret string
>
>     * keyUri string
>
>     * oathToken string
>
>     * serialNumber string
>
>     * rp object
>
>       * id string
>
>       * name string
>
>     * platform string
>
>     * publicKeyCredentialCreationOptions string
>
>     * attributes object
>
>       * previousDeviceType string
>
>       * isCrossPlatform boolean
>
>     * displayName string
>
>     * createdAt string
>
>     * updatedAt string
>
>   * headers object
>
>     * set-cookie string
>
>   * statusCode integer
>
> Output Example
>
> ```json
> {
>   "rawResponse": {
>     "device": {
>       "id": "43eb5621-eae8-4fa1-aafb-2a884d6848cb",
>       "type": "SMS",
>       "status": "ACTIVE",
>       "nickname": "Work Device",
>       "phone": "+972528888888",
>       "extension": "###1",
>       "createdAt": "2021-01-15T20:45:17.463Z",
>       "updatedAt": "2021-01-15T20:45:17.463Z"
>     }
>   }
> }
> ```

### Check Remember Me State

Check if the accessing device is known

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - User ID textField
>
>   The unique identifier for the user.
>
> - MFA Policy ID textField
>
>   The ID of your PingOne MFA device authentication policy.
>
> - Session ID textField
>
>   The active PingOne session for the user.
>
> - Device Type dropDown
>
>   * Browser
>
> - Payload textField
>
>   Identify the device via a unique device ID combined with a digital signature that ensures information collected about the device has not been tampered with.
>
> - Cookie textField
>
>   The cookie that was generated when the remembered device was created.
>
> * default object
>
>   * properties object
>
>     * userId string required minLength: 0 maxLength: 100
>
>     * mfaPolicyId string minLength: 0 maxLength: 100
>
>     * rememberMeDeviceType string required
>
>     * rememberMePayload string required
>
>     * rememberMeCookie string required
>
> - output object
>
>   * rawResponse object
>
>     * id string
>
>     * user object
>
>       * id string
>
>     * environment object
>
>       * id string
>
>     * policy object
>
>       * id string
>
>     * selectedDevice object
>
>       * id string
>
>     * application object
>
>       * id string
>
>     * status string
>
>     * authenticators array
>
>     * publicKeyCredentialRequestOptions string
>
>     * \_links object
>
>     * \_embedded object
>
>       * devices array
>
>   * headers object
>
>   * statusCode integer
>
> Output Example
>
> ```json
> {
>   "rawResponse": {
>     "id": "43eb5621-eae8-4fa1-aafb-2a884d6848cb",
>     "environment": {
>       "id": "9ad15e9e-3ac6-43f7-a053-d46b87d6c4a7"
>     },
>     "user": {
>       "id": "c362abbc-eeeb-4ea5-b9c1-097a376b0086"
>     },
>     "status": "OTP_REQUIRED",
>     "selectedDevice": {
>       "id": "9362abac-eeeb-6ea5-b9cc-097a375b0043"
>     },
>     "policy": {
>       "id": "6122abac-eeeb-6ea5-b9cc-097a375b0043"
>     },
>     "createdAt": "2021-01-15T20:45:17.463Z",
>     "updatedAt": "2021-01-15T20:45:17.463Z",
>     "_embedded": {
>       "devices": [
>         {
>           "type": "EMAIL",
>           "email": "o******@pingidentity.com"
>         }
>       ]
>     }
>   }
> }
> ```