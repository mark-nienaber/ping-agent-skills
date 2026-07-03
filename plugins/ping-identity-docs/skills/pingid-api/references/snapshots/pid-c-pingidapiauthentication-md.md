---
title: PingID Authentication API
description: A PingID authentication request can be fulfilled by two methods depending on the account configuration, the users preferences and the users devices available at the time of the authentication:
component: pingid-api
page_id: pingid-api::pid_c_PingIDapiAuthentication
canonical_url: https://developer.pingidentity.com/pingid-api/pid_c_PingIDapiAuthentication.html
section_ids:
  the-pingid-authentication-api: The PingID Authentication API
  start-authentication-workflow: Start Authentication Workflow
  cancel-authentication-workflow: Cancel Authentication Workflow
  online-authentication-workflow: Online Authentication Workflow
  offline-authentication-workflow: Offline Authentication Workflow
  backup-authentication-workflow: Backup Authentication Workflow
  fido-authentication-workflow: FIDO Authentication Workflow
  fido-passwordless-authentication-workflow: FIDO Passwordless Authentication Workflow
  the-yubikey-authentication-device: The YubiKey Authentication Device
  startauthentication: StartAuthentication
  authstatus: AuthStatus
  cancelauthentication: CancelAuthentication
  authenticateonline: AuthenticateOnline
  authenticateoffline: AuthenticateOffline
  webauthnstartauth-fido-security-key-fido-biometrics-fido2-devices: WebAuthnStartAuth (FIDO security key, FIDO biometrics, FIDO2 devices)
  startwebauthnpasswordlessauth: StartWebAuthnPasswordlessAuth
  finishwebauthnpasswordlessauth: FinishWebAuthnPasswordlessAuth
---

# PingID Authentication API

## The PingID Authentication API

A PingID authentication request can be fulfilled by two methods depending on the account configuration, the users preferences and the users devices available at the time of the authentication:

* **Online authentication**, which is used to trigger an authentication action on an end-user's device (i.e. a fingerprint or swipe action). This process uses the AuthenticateOnline API operation.

* **Offline authentication**, which is used to validate a one-time password (OTP) provided to the end-user (via the PingID app, email, SMS, voice, YubiKey, FIDO security key or OATH token). This process uses the AuthenticateOffline operation which is always called after an AuthenticateOnline operation.

In version 4.9 and higher of the API, an authentication request will commence by calling the StartAuthentication operation. This operation will determine the appropriate workflow to perform based on the configuration of the PingOne account.

## Start Authentication Workflow

Each authentication should start by calling the StartAuthentication operation. The StartAuthentication response will guide the developer on how to proceed with the authentication, depending on the account configuration the users preferences and whether the users devices are available at the time of the authentication. The account preference that is evaluated is the "Multiple Devices" mode option available in the administration console.

The Multiple Devices mode has two options:

* **Device Selection Mode:** The user should be displayed with a list of his available devices and select the device he wants to authenticate with.

* **Default Device Mode:** The user has a default (primary) device to be used by default, the list of other available devices can displayed if the user chooses to change the authentication device by canceling the currently active authentication.

The response of StartAuthentication includes information that is vital to the rest of the authentication flow including a session ID that is used throughout the flow and should be passed with every call in this flow, the list of user devices and a flag indicating whether the account has the multiple devices mode enabled. After parsing the response, one of the following three flows will apply:

* **Device selection flow:** Display the list of available devices to the user. Once the user selects a device, StartAuthentication should be called again with the selected device ID and the session ID from the original StartAuthentication response.

* **Online Authentication:** The user has configured a preference for authentication by PingID mobile application.

* **Offline Authentication:**The user has configured a preference for authentication by SMS, voice message, email, desktop, YubiKey, FIDO security key or OATH token.

For example, the following sequence describes a StartAuthentication flow:

1. The service provider triggers a StartAuthentication request to the PingID service along with the authenticating user's username.

2. The PingID service will response with a message indicating either to:

   a) Continue with either the online or offline authentication flow with a specific device ID

   b) Display a list of devices to the user so they can select a device to use

3. If the result was b) to display the list of devices, the application should prompt the user to select the device, then re-submit a StartAuthentication request passing along the device ID the user selected.

![pid i startAuthentication](_images/pid_i_startAuthentication.png)

## Cancel Authentication Workflow

The CancelAuthentication operation is used to cancel an active, ongoing, authentication. In a scenario where the user started an authentication with one device and decided they want to change their authentication device, CancelAuthentication should be called to cancel the currently active authentication.

|   |                                                                                                                                                                                                                                                                                                                                |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | This step is mandatory for online authentication done with a mobile app, since the mobile app cannot have more than one active authentication running at any given time. Although this step is not mandatory for other authentication devices types (SMS, voice message, email, desktop or Yubikey), it is highly recommended. |

For example, the following sequence describes a CancelAuthentication flow when the user authenticates by the PingID mobile application to a service provider:

1. The service provider triggers a StartAuthentication request to the PingID server along with the authenticating user's username.

2. PingID server responds with:

   * Appropriate action to take based on account settings (in this example, the AuthenticateOnline flow)

   * List of devices associated with the user (in this example, the default device will be used for multi-factor authentication)

   * Session ID

3. The service provider sends an AuthenticateOnline request to the PingID service.

4. The PingID server pushes an authentication request to the user's mobile device.

5. The service provider displays a "Please wait…​" screen which includes an option for the user to change their authentication device.

6. In this scenario the user does not have their mobile phone with them, and chooses to change their authentication device.

7. The service provider sends CancelAuthentication request to the PingID server.

8. The service provider displays the list of devices paired for the user that were received with the response to the initial StartAuthentication call.

9. The user selects an alternate device.

10. The service provider starts the authentication flow again by calling StartAuthentication, passing the username and device ID of the alternate device.

## Online Authentication Workflow

Online authentication is performed when all of the following conditions apply:

* The user has configured a preference for online authentication.

* The user's device is accessible over the internet.

* The user's device can receive push notifications.

Usually, online authentication is performed after the user has entered username and password values. The user is prompted to authenticate using the PingID mobile application. The PingID server is notified of the verification action, and it notifies the service provider that authentication has succeeded, and the user can enter the requested application.

|   |                                                                                                                                |
| - | ------------------------------------------------------------------------------------------------------------------------------ |
|   | In PingID API version 4.9 and higher, the initial authentication request should start with the start authentication operation. |

This is the sequence of events in the online authentication workflow example, described in the diagram below:

1. The service provider sends an online authentication request to the PingID server along with the username.

2. The PingID server pushes a message to the user's mobile device, prompting the user to swipe a button displayed in the message, or to perform fingerprint identification.

3. The user swipes the button or submits a valid fingerprint, and a verification message is sent to the PingID server.

4. The PingID server sends a success message to the service provider, which now allows the user to login to the requested application.

![pid i authenticateOnlineWorkflow](_images/pid_i_authenticateOnlineWorkflow.png)

## Offline Authentication Workflow

Offline authentication is performed when one of the following conditions applies:

* The user has configured a preference for authentication by SMS, voice message, email, YubiKey, FIDO security key or OATH token.

* The user's device is inaccessible over the internet.

* The user's device cannot receive push notifications (due to a firewall or other local restrictions).

* In this case, the user must manually enter a one-time password which is generated by the PingID mobile or desktop application, by a YubiKey, sent via SMS, voice message or email, depending on the situation.

|   |                                                                                       |
| - | ------------------------------------------------------------------------------------- |
|   | The OTP used for offline authentication is an HOTP — an HMAC-based one-time password. |

This is the sequence of events in the offline authentication workflow example described in the diagram below:

1. The service provider sends a start authentication request to the PingID server along with the username.

2. The PingID server sends either a "device unreachable" status, or the OTP access method configured by the user, to the service provider, together with a session ID.

3. The service provider prompts the user to enter a one-time password.

4. The user retrieves the OTP from the appropriate source, then enters it in the service provider's prompt page.

5. The service provider sends an offline authentication request, containing the OTP that the user entered and the session ID it received, to the PingID server.

6. The PingID server sends a success message to the service provider, which now allows the user to login to the requested application.

![pid i authenticateOfflineWorkflow](_images/pid_i_authenticateOfflineWorkflow.png)

## Backup Authentication Workflow

If a user's authenticating device is lost or stolen, or they do not have it when attempting to access a protected resource, the backup authentication configuration can be configured to provide them with a one-time passcode to log in. Backup authentication uses the email and phone attributes stored in your organization's user directory to present the user with a one-time passcode via SMS, Voice, or Email.

To activate backup authentication via the PingID APIs:

1. Call [AuthenticateOnline](#authenticateonline) using only the following parameters in the request body:

   * `authType` set to `ONE_TIME_DEVICE`

   * `spAlias` set to `rescuecode`

   * `userName` set to the relevant username

   * `deviceType` set to one of `Email`, `SMS` or `Voice`

   * `deviceData` set to an email address or phone number, depending on the `deviceType` setting. For example:

   ```json
    {
      "authType": "ONE_TIME_DEVICE",
      "spAlias": "rescuecode",
      "userName": "marcher",
      "deviceType": "Email",
      "deviceData": "username@emaildomain.com"
    }
   ```

2. Call [AuthenticateOffline](#authenticateoffline) with the request body containing `spAlias` set to `rescuecode`, `userName` set to the relevant username, `otp` set to the OTP that the user received, and `sessionId` set to the session ID that was returned in the response to the `AuthenticateOnline` request. For example:

   ```json
    {
      "spAlias": "rescuecode",
      "userName": "marcher",
      "otp": "111111",
      "sessionId": "abcd123",
      "clientData": "Session data echoed back to the requestor"
    }
   ```

## FIDO Authentication Workflow

When a user wants to authenticate using a FIDO2 or U2F security key, or a FIDO2 supported biometrics device, the service provider initiates the authentication process with the StartAuthentication API, which acts as a flow manager for the authentication process. The StartAuthentication API checks policies and other factors, and when relevant, returns a status (errorId 30011 for FIDO security key, or errorID 30013 for FIDO biometrics) to indicate that the security key must be used.

The service provider then invokes the WebAuthnStartAuth API, which returns parameter data required for public key credentials. These parameters are used as an input for the call to the browser's "navigator.credentials.get" function, which is the next step in the WebAuthn authentication flow. The "navigator.credentials.get" function returns the public key credentials. The AuthOffline API then uses public key credentials and input parameters in its request body, and completes the authentication of the FIDO security key or FIDO supported biometrics device.\
For further information, refer to:

* [Example: PingID FIDO security key](pid_c_PingIDapiExampleFIDOsecurityKey.html)

* [Example: PingID FIDO biometrics](pid_c_PingIDapiExampleFIDObiometrics.html)

PingID supports use cases of FIDO hybrid mode authentication, where a custom UI (not hosted by PingID) is used for registration, while PingID's out of the box UI is used for authentication. PPM request, which was originally developed to support authentication, also supports explicit FIDO registration. For further information see [PPM request for FIDO authentication with a hybrid UI](pid_c_PingIDapiPpmrequest.html).

## FIDO Passwordless Authentication Workflow

When a user wants to do passwordless authentication using a supported biometrics device, the service provider initiates the authentication process with the StartWebAuthnPasswordlessAuth API, which acts as a flow manager for the authentication process, and returns parameter data required for public key credentials. These parameters are used as an input for the call to the browser's "navigator.credentials.get" function, which is the next step in the authentication flow. The user is prompted for a biometric gesture, such as a fingerprint or face scan.

The `navigator.credentials.get` function returns the public key credentials. The FinishWebAuthnPasswordlessAuth API then uses public key credentials and input parameters in its request body, and completes the authentication of the supported biometrics device.

The FinishWebAuthnPasswordlessAuth API is also used to check for optional policy enforcement. When the admin has configured the policy as enforced, the errorId is returned with a value of 30014, and then the StartAuthentication API must be run with the relevant "memberOf" group parameter, to complete the authentication flow.

For further information, refer to [Example: PingID Passwordless Authentication](pid_c_PingIDapiExamplePasswordless.html).

![pid i FIDOpasswordlessWorkflow](_images/pid_i_FIDOpasswordlessWorkflow.png)

## The YubiKey Authentication Device

Some organizations use a 3rd-party hardware device called a YubiKey (produced by Yubico) to generate One-Time Passwords (OTPs). PingID enables integration with this type of device. To authenticate a user who is using a YubiKey, the Service Provider uses offline authentication, while providing the OTP generated by the YubiKey, which the user enters manually. In this authentication mode, users are paired with YubiKey devices rather than with mobile devices.

## StartAuthentication

When an organizations user want to access a service that is protected by PingID MFA, the service provider will first use StartAuthentication. For example, a customer wants to logon to an online banking service, or an employee wants to access the organizations email platform. After the user enters a username and password and clicks a "Login" button, the service provider sends a StartAuthentication request to the PingID service. The response will return all the necessary information required to complete the authentication. Start authentication takes into consideration the account's multiple devices configuration, the device selection mode configuration, the users preferences and the users devices available at the time of the authentication.

This is the StartAuthentication URL:

```
https://idpxnyl3m.pingidentity.com/pingid/rest/4/startauthentication/do
```

**Request Body Parameters**

Example reqBody object in the API payload:

```json
"reqHeader": { ... },
"reqBody": {
  "spAlias": "web",
  "userName": "marcher",
  "deviceId": 284159158921096000,
  "sessionId": "webs_jRyBWbUG87sYYh2UlG-TBoVNC6A8kXadFtj4qCMGrl4",
  "clientData": "Session data echoed back to the requestor",
  "enforcePolicy": "true",
  "ipAddr": "103.25.46.58",
  "application": "google.com",
  "cookie": "eyJ0dGwiOiIyMDIyLTEyLTAxVDEyOjU0OjEyLjcyMSIsInppcCI6IkRFRiIsImFsZyI6IkEyNTZLVyIsImVuYyI6IkExMjhDQkMtSFMyNTYifQ.2F6W1HOHNSYAJ5fOiWf25HUugxuO_GIuHir3vzhakzj9FtOpAFd7iw.NEUoexj_iw31XPlbYVnXWA.CMVgGFlDhrWySmAcSR6AxDwAMwHCvW1N81CINn_kMEG1l7DcwHJUHv_Lj_udzLoDLgoOxO5TG_rfUO4Lioi4fcqjMBi2kXvRDasPRrKj4feuZoeAbqTHYjhEyUHpaTA7Tesc7R3f2CJtEUjQue5HUoGCUo8gU9y0akOEAToCjSn9_H45F2OyveD0yMnRi7WSEn_ZaoFx55HIaQMl1q8vJE2S8d47FbyW2jBQLbie7G130gESW1Ck4NpoMzs_dbtXQsZ9hOeqUXf_SwYkuQm7BjkmDAmemTA7of1ZU-f_ZFfNNlRh4nFIOTVw_JCZg3e-hI4q6F_xUFl6da8mzrJnRphyjv-_A0MNOY5CFOxLeCT5QU_Hubggfvgaqyy7O_GdkmwrItcWePTspIrQZGNo3q-zSEjx40iJgcukt4I1P3D2nnyrMUpuEizt4PynsS7d7r7jlMDgwpn83chcsK95H_JKS-3ozgtQSysW-sy1Qjf_WJNSkbUyCgf6CPwXoRlEJr3ip4d7AHfvqs_9Xezpwbi8aywagKStrVpQe6T4mNCjoRIt78KlsTIYUdV0wwgmFZTAhlSwsv_bahV2sVJmd77PdbtOYiJcB7r7jyy0IU8gz1Y7EOV9s7IoSdjuF58mLH2Xj5UYCOs1TB08VTPqDcA8RIH5Vg-dWmD55i0_D-lQ9KVNbnYBBMV3345NVy-NMpIOst8SsJZiM4ebTwWQE6EKm6Enbp045pJTBhJ6gQXSaI-jXqw2VkLYHyUqmSkqBfqPVu5yC144rpxfMuX0GjIm0ARJTYBj87MfhgUJdvicOwYbBILwEIzqORuodqeT.1D2of3ZcLD4i9F13rUCgUA",
  "reqDevFP":"{\"User-Agent\":\"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36\"}",
  "memberOf": ["CN=aliceA,OU=US,OU=Americas,DC=net","CN=bobB,OU=EU,OU=England,DC=net"],
    "formParameters": {
        "isWebAuthnSupportedByBrowser": "true",
        "isWebAuthnPlatformAuthenticatorAvailable": "true"}
}
```

The parameters included in the reqBody object are:

| Parameter      | DataType              | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| -------------- | --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| spAlias        | String                | The PingID service that is being used. In this context, the value of the parameter must be "web". For more information, see [PingID Services](pid_c_PingIDapiUserManagement.html#pingid-services).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| userName       | String                | The user's PingID username.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| deviceId       | Long                  | To specify a specific device to authenticate with. (In device selection mode, the first call will return a list of devices for the user to choose from, a second call is done with a session id and a device id in the request to specify the exact device to authenticate with).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| sessionId      | String                | The session id returned from a previous call to start authentication.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| clientData     | String                | Optional. This value is returned unchanged in the API response. It can be used to save state and/or client context data for the application between API calls.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| enforcePolicy  | Boolean               | Set this parameter to "true" to activate policy evaluation. Default: false.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| async          | Boolean               | Set this parameter to "true" to activate asynchronous authentication. Default: false.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| ipAddr         | String                | The requesting device's IP address. Required in cases where enforcePolicy = "true" and IP address policies are evaluated. When the ipAddr parameter has a value, it is validated to check that the value is in IP address format.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| application    | String                | The requested application's ID, as defined in the application list in the Policy section of the PingID admin portal. Required in cases where enforcePolicy = "true" and application policies are evaluated. Maximum length: 500 characters.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| cookie         | String                | The PingID cookie received in the previous authentication response, in cases where enforcePolicy = "true". On completion of a successful authentication using `AuthenticateOnline`, the cookie parameter returned in the `AuthenticateOnline` response is populated with the latest authentication transaction's data. For policy evaluation purposes, save this parameter and use it in the user's next authentication request. If you are using asynchronous authentication (`async` parameter = true), then in most cases the cookie to use in the next `StartAuthentication` call is the cookie that was returned in the response body when `AuthStatus` was called. However, there are situations where there is no need for polling with `AuthStatus` and a cookie is included in the response to `StartAuthentication`, for example, if a user logs in within the time limit set in the "recent authentication" rule in a policy. The criterion to use to distinguish between the cases is the `errorId` included in the response to `StartAuthentiation`. If the value of `errorid` is 200, there is no need to poll with `AuthStatus`, and the response to `StartAuthentication` will include the cookie that you should save and use in the next call. (If this is the initial call to StartAuthentication, then there is no cookie to include.) Maximum length: 5000 characters                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| reqDevFP       | String                | The requesting device's user agent. Required in cases where enforcePolicy = "true" and the device's attributes are evaluated. Maximum length: 50000 characters                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| memberOf       | json array            | List of users and groups. Required in cases where enforcePolicy = "true" and group policies are evaluated. Maximum items: 1000.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| formParameters | Map \<String, String> | Optional key/value pairs- **\`isWebAuthnSupportedByBrowser \`** The "isWebAuthnSupportedByBrowser" key has a default value of "true", making the assumption that the client browser supports WebAuthn. In the case of a FIDO security key flow, the client browser's ability to support WebAuthn should be checked before activating this API.

  If the browser does not support WebAuthn, it will fail since it cannot find the "navigator.credentials.get" and "navigator.credentials.create" JavaScript functions. Set the "isWebAuthnSupportedByBrowser" to "false" when the browser does not support WebAuthn. When "isWebAuthnSupportedByBrowser" is "false", FIDO devices will be ignored, and the server will attempt to retrieve and list the user's next device (if multiple devices exist for that user).

  If no other devices exist for this user, it will return HTTP status 400 with error code 20570 (WEBAUTHN\_NOT\_SUPPORTED\_BY\_BROWSER). Refer to [Example: PingID FIDO security key](pid_c_PingIDapiExampleFIDOsecurityKey.html)

- **`isWebAuthnPlatformAuthenticatorAvailable`** The "isWebAuthnPlatformAuthenticatorAvailable" key has a default value of "true", making the assumption that the client browser supports FIDO biometrics. In the case of a FIDO biometrics flow, the client browser's ability to support FIDO biometrics should be checked before activating this API.

  If the browser does not support FIDO biometrics, it will fail.

  When "isWebAuthnPlatformAuthenticatorAvailable" is "false", FIDO biometric devices will be ignored, and the server will attempt to retrieve and list the user's next device (if multiple devices exist for that user).

  Refer to [Example: PingID FIDO biometrics](pid_c_PingIDapiExampleFIDObiometrics.html).

  If no other devices exist for this user, it will return HTTP status 400 with error code 20570 (WEBAUTHN\_NOT\_SUPPORTED\_BY\_BROWSER). |

**Response Body Parameters**

Example response body:

```json
"responseBody": {
  "extendedAuthenticationDetails": {
    "adminHelp": "Contact your system administrator",
    "gracePeriod": 1454076723000,
    "lastSuccessfulLogin": 1453991562000,
    "numberForMatching": 14
  },
  "userDevices": [
    "deviceDetails": {
      "email": null,
      "appVersion": "1.6.2(OE5700)",
      "hasWatch": false,
      "countryCode": null,
      "sentClaimedSms": -1,
      "phoneNumber": null,
      "nickname": "username",
      "deviceModel": "samsung SM-G920F",
      "enrollment": "2016-01-11 07:03:14.371",
      "availableNotClaimedSms": 0,
      "availableClaimedSms": 0,
      "deviceRole": "PRIMARY",
      "pushEnabled": true,
      "deviceId": 284159158921096000,
      "sentNotClaimedSms": -1,
      "type": "Android",
      "osVersion": "5.1.1"
    },
    "deviceDetails": {
      "email": null,
      "appVersion": null,
      "hasWatch": false,
      "countryCode": null,
      "sentClaimedSms": -1,
      "phoneNumber": null,
      "nickname": "YubiKey",
      "deviceModel": null,
      "enrollment": "2016-02-09 08:04:08.023",
      "availableNotClaimedSms": 0,
      "availableClaimedSms": 0,
      "deviceRole": "SECONDARY",
      "pushEnabled": false,
      "deviceId": 285234913243546570,
      "sentNotClaimedSms": -1,
      "type": "YubiKey",
      "osVersion": null
    } ],
  "multipleDevicesEnabled": true,
  "sessionId": "webs_COQgngDLjctrLWRMObANUrKkHVbk46OtVL4Uo35XcZ8",
  "cookie": "eyJ0dGwiOiIyMDIyLTEyLTAxVDEyOjU0OjEyLjcyMSIsInppcCI6IkRFRiIsImFsZyI6IkEyNTZLVyIsImVuYyI6IkExMjhDQkMtSFMyNTYifQ.2F6W1HOHNSYAJ5fOiWf25HUugxuO_GIuHir3vzhakzj9FtOpAFd7iw.NEUoexj_iw31XPlbYVnXWA.CMVgGFlDhrWySmAcSR6AxDwAMwHCvW1N81CINn_kMEG1l7DcwHJUHv_Lj_udzLoDLgoOxO5TG_rfUO4Lioi4fcqjMBi2kXvRDasPRrKj4feuZoeAbqTHYjhEyUHpaTA7Tesc7R3f2CJtEUjQue5HUoGCUo8gU9y0akOEAToCjSn9_H45F2OyveD0yMnRi7WSEn_ZaoFx55HIaQMl1q8vJE2S8d47FbyW2jBQLbie7G130gESW1Ck4NpoMzs_dbtXQsZ9hOeqUXf_SwYkuQm7BjkmDAmemTA7of1ZU-f_ZFfNNlRh4nFIOTVw_JCZg3e-hI4q6F_xUFl6da8mzrJnRphyjv-_A0MNOY5CFOxLeCT5QU_Hubggfvgaqyy7O_GdkmwrItcWePTspIrQZGNo3q-zSEjx40iJgcukt4I1P3D2nnyrMUpuEizt4PynsS7d7r7jlMDgwpn83chcsK95H_JKS-3ozgtQSysW-sy1Qjf_WJNSkbUyCgf6CPwXoRlEJr3ip4d7AHfvqs_9Xezpwbi8aywagKStrVpQe6T4mNCjoRIt78KlsTIYUdV0wwgmFZTAhlSwsv_bahV2sVJmd77PdbtOYiJcB7r7jyy0IU8gz1Y7EOV9s7IoSdjuF58mLH2Xj5UYCOs1TB08VTPqDcA8RIH5Vg-dWmD55i0_D-lQ9KVNbnYBBMV3345NVy-NMpIOst8SsJZiM4ebTwWQE6EKm6Enbp045pJTBhJ6gQXSaI-jXqw2VkLYHyUqmSkqBfqPVu5yC144rpxfMuX0GjIm0ARJTYBj87MfhgUJdvicOwYbBILwEIzqORuodqeT.1D2of3ZcLD4i9F13rUCgUA",
  "errorId": 30007,
  "errorMsg": "Continue the authentication flow using online flow",
  "uniqueMsgId": "webs_COQgngDLjctrLWRMObANUrKkHVbk46OtVL4Uo35XcZ8",
  "clientData": "Session data echoed back to the requestor"
}
```

The parameters included in the `responseBody` object are:

| Parameters                    | DataType | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| ----------------------------- | -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| clientData                    | String   | The value sent in the request's clientData field.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| errorId                       | Int      | A numeric response code. For multiple devices, the following values can be used to evaluate the next action to take:- 30001 - Offline authentication (SMS)

- 30002 - Offline authentication (Voice)

- 30003 - Offline authentication (Application)

- 30004 - Offline authentication (YubiKey)

- 30005 - Offline authentication (Email)

- 30007 - Online authentication (Application)

- 30008 - Device selection prompt

- 30010 — Online asynchronous authentication: waiting for client response- 30011 — Offline authentication (FIDO security key)

- 30013 — Offline authentication (FIDO biometrics)            |
| errorMsg                      | String   | A textual description of the response, if there was one.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| sessionId                     | String   | The session ID will be used with other calls in the flow, may be used in an online authentication flow, offline authentication flow or in a second start authentication flow.                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| uniqueMsgId                   | String   | A unique ID for the response message. This is logged and used to track the specific transaction for troubleshooting purposes.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| cookie                        | String   | In cases where enforcePolicy = "true" and you are using asynchronous authentication (`async` parameter = true), a cookie is returned in the response body when `AuthStatus` is called. However, there are situations where there is no need for polling with `AuthStatus` and a cookie is included in the response to `StartAuthentication`, for example, if a user logs in within the time limit set in the "recent authentication" rule in a policy. In cases where the response to `StartAuthentication` includes a cookie, this is the cookie that you should save and include in the next `StartAuthentication` call. |
| extendedAuthenticationDetails | Object   | Contains additional information used by the authentication process. See details in the extendedAuthenticationDetails table below.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| userDevices                   | Array    | A list of one or more deviceDetails objects containing information about the user's paired devices. See details in the deviceDetails table below.                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| multipleDevicesEnabled        | Boolean  | Indicates whether the multiple devices feature is enabled for the account.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |

The extendedAuthenticationDetails object:

| Parameters          | DataType         | Description                                                                                                                                                                                                                                                                                              |
| ------------------- | ---------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| adminHelp           | String           | Descriptive prompt the application can display to direct the end user for help.                                                                                                                                                                                                                          |
| gracePeriod         | DateTime (epoch) | When the grace period to allow bypassing PingID authentication expires (in UNIX epoch format).                                                                                                                                                                                                           |
| lastSuccessfulLogin | DateTime (epoch) | Last time this user successfully authenticated (in UNIX epoch format).                                                                                                                                                                                                                                   |
| numberForMatching   | Integer          | Number shown on the authentication screen. The user must select the same number in PingID mobile app to authenticate successfully. Value in response is null for flows where number-matching is not enabled and for flows that cannot use number-matching because the `async` flag is not set to `true`. |

The deviceDetails objects (one or more objects) in the userDevices list:

| Parameters             | DataType | Description                                                                                                                                                                                                                                        |
| ---------------------- | -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| email                  | String   | The user's email address for the OTP message (non-null if email authentication is configured).                                                                                                                                                     |
| appVersion             | String   | The PingID application version installed on the device.                                                                                                                                                                                            |
| hasWatch               | Boolean  | Indicates whether the authentication device is an Apple iWatch.                                                                                                                                                                                    |
| countryCode            | String   | The country code of the device's phone number (non-null if SMS or voice authentication is configured).                                                                                                                                             |
| sentClaimedSms         | Int      | \[Deprecated] The times within the current day that the user requested an OTP via SMS or voice message and used the OTP for authentication.                                                                                                        |
| phoneNumber            | String   | The user's assigned phone number.                                                                                                                                                                                                                  |
| nickname               | String   | A nickname assigned to the user.                                                                                                                                                                                                                   |
| deviceModel            | String   | The manufacturer and model information for the device.                                                                                                                                                                                             |
| enrollment             | DateTime | Format is: yyyy-MM-dd HH:mm:ss.SSS. U.S. MST timezone.                                                                                                                                                                                             |
| availableNotClaimedSms | Int      | The remaining available times within the current day that the user can request an OTP via SMS or voice message, without using the OTP for authentication. This value is reset daily (it is limited because of the costs incurred for the user).    |
| availableClaimedSms    | Int      | The remaining available times within the current day that the user can request an OTP via SMS or voice message, which is then used for authentication. This value is reset daily (it is limited because of the costs incurred for the user).       |
| deviceRole             | String   | The authenticating role of the device. This can be PRIMARY or SECONDARY.                                                                                                                                                                           |
| pushEnabled            | Boolean  | Indicates whether the authentication process can push data to the device.                                                                                                                                                                          |
| deviceId               | Long     | Uniquely identifies the device.                                                                                                                                                                                                                    |
| displayID              | String   | The ID of the device, according to the device's type. For example:- Device model (Mobile device)

- Serial number (YubiKey)

- Country code and phone number (SMS and Voice)

- Email address (Email)

- Client browser platform (FIDO biometrics) |
| sentNotClaimedSms      | Int      | \[Deprecated] The times within the current day that the user requested an OTP via SMS or voice message without using the OTP for authentication).                                                                                                  |
| type                   | String   | The type of device used (such as, Android or Yubikey).                                                                                                                                                                                             |
| osVersion              | String   | If applicable, the operating system version used by the device (null if offline authentication is configured).                                                                                                                                     |
| oathSerialNumber       | String   | The serial number of the device if it is an OATH token. Null, if the device is not an OATH token.                                                                                                                                                  |
| oathTokenType          | String   | Type of token, if the device is an OATH token.Possible values:- HOTP

- TOTPNull, if the device is not an OATH token                                                                                                                               |

## AuthStatus

The authentication status operation can be used during an asynchronous authentication flow, following the StartAuthentication operation.

In the regular synchronous online flow, the StartAuthentication operation returns a status (30007) indicating that the flow is the online authentication flow. The client then follows with the AuthenticateOnline operation, which waits up to the maximum permitted time for a push notification.

In contrast, in the asynchronous flow, the StartAuthentication operation is invoked with the async parameter set to true. The server sends a push notification to the mobile. While waiting for a user response, the status on the server remains **wait** (30010). The client should then repeatedly call the AuthStatus operation (in contrast to the AuthenticateOnline operation used in the synchronous flow), until the server returns any status other than the **wait** status (30010), i.e. either a success (200) or a failure status.

This is the AuthStatus URL:

```
https://idpxnyl3m.pingidentity.com/pingid/rest/4/authstatus/do
```

**Request Body Parameters**

Example reqBody object in the API payload:

```json
"reqHeader": { ... },
"reqBody": {
  "sessionId": "webs_IAjpPLQ5nKz2DPZCbOXVhA5-JaeIVqOMExTK03NuF6k",
  "clientData": "Session data echoed back to the requestor"
}
```

The parameters included in the reqBody object are:

| Parameters | DataType | Description                                                                                                                                                    |
| ---------- | -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| sessionId  | String   | The session id return from a previous call to start authentication.                                                                                            |
| clientData | String   | Optional. This value is returned unchanged in the API response. It can be used to save state and/or client context data for the application between API calls. |

**Response Body Parameters**

Example response body:

```json
{
    "errorMsg": "",
    "uniqueMsgId":"webs_sOFLeIP0EOlR-BnOCN_DTLv1uMpivQRoFN68edsYi4Y",
    "errorId": 200,
    "cookie": "eyJ0dGwiOiIyMDIyLTEyLTAxVDEyOjU0OjEyLjcyMSIsInppcCI6IkRFRiIsImFsZyI6IkEyNTZLVyIsImVuYyI6IkExMjhDQkMtSFMyNTYifQ.2F6W1HOHNSYAJ5fOiWf25HUugxuO_GIuHir3vzhakzj9FtOpAFd7iw.NEUoexj_iw31XPlbYVnXWA.CMVgGFlDhrWySmAcSR6AxDwAMwHCvW1N81CINn_kMEG1l7DcwHJUHv_Lj_udzLoDLgoOxO5TG_rfUO4Lioi4fcqjMBi2kXvRDasPRrKj4feuZoeAbqTHYjhEyUHpaTA7Tesc7R3f2CJtEUjQue5HUoGCUo8gU9y0akOEAToCjSn9_H45F2OyveD0yMnRi7WSEn_ZaoFx55HIaQMl1q8vJE2S8d47FbyW2jBQLbie7G130gESW1Ck4NpoMzs_dbtXQsZ9hOeqUXf_SwYkuQm7BjkmDAmemTA7of1ZU-f_ZFfNNlRh4nFIOTVw_JCZg3e-hI4q6F_xUFl6da8mzrJnRphyjv-_A0MNOY5CFOxLeCT5QU_Hubggfvgaqyy7O_GdkmwrItcWePTspIrQZGNo3q-zSEjx40iJgcukt4I1P3D2nnyrMUpuEizt4PynsS7d7r7jlMDgwpn83chcsK95H_JKS-3ozgtQSysW-sy1Qjf_WJNSkbUyCgf6CPwXoRlEJr3ip4d7AHfvqs_9Xezpwbi8aywagKStrVpQe6T4mNCjoRIt78KlsTIYUdV0wwgmFZTAhlSwsv_bahV2sVJmd77PdbtOYiJcB7r7jyy0IU8gz1Y7EOV9s7IoSdjuF58mLH2Xj5UYCOs1TB08VTPqDcA8RIH5Vg-dWmD55i0_D-lQ9KVNbnYBBMV3345NVy-NMpIOst8SsJZiM4ebTwWQE6EKm6Enbp045pJTBhJ6gQXSaI-jXqw2VkLYHyUqmSkqBfqPVu5yC144rpxfMuX0GjIm0ARJTYBj87MfhgUJdvicOwYbBILwEIzqORuodqeT.1D2of3ZcLD4i9F13rUCgUA",
    "clientData": "Session data echoed back to the requestor"
}
```

The parameters included in the responseBody object are:

| Parameters  | DataType | Description                                                                                                                                                                                                                                                                                                                                             |
| ----------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| errorMsg    | String   | A textual description of the error, if there was one.                                                                                                                                                                                                                                                                                                   |
| uniqueMsgId | String   | A unique ID for the response message. This is logged and used to track the specific transaction for troubleshooting purposes.                                                                                                                                                                                                                           |
| errorId     | Int      | A numeric response code:- 200 - Success: the server received the push notification that completed the authentication

- 30010 — Online asynchronous authentication: waiting for client response

- In the event of a failure, an error status code indicating the cause of the failure (refer to [PingID Error Codes](pid_c_PingIDapiErrorCodes.html)). |
| cookie      | String   | In cases where enforcePolicy = "true", a cookie is returned in the response body when `AuthStatus` is called. This is the cookie that you should save and include in the next `StartAuthentication` call.                                                                                                                                               |
| clientData  | String   | The value sent in the request's clientData field.                                                                                                                                                                                                                                                                                                       |

## CancelAuthentication

The cancel authentication operation can be used to cancel an in progress authentication when a user wishes to change their authentication device after the authentication flow has commenced.

This is the CancelAuthentication URL:

```
https://idpxnyl3m.pingidentity.com/pingid/rest/4/cancelauthentication/do
```

**Request Body Parameters**

Example reqBody object in the API payload:

```json
"reqHeader": { ... },
"reqBody": {
  "cancelAuthenticationType": "CHANGE_DEVICE",
  "sessionId": "webs_IAjpPLQ5nKz2DPZCbOXVhA5-JaeIVqOMExTK03NuF6k",
  "clientData": "Session data echoed back to the requestor"
}
```

The parameters included in the reqBody object are:

| Parameters               | DataType | Description                                                                                                                                                                                                                                                                                                                                                              |
| ------------------------ | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| cancelAuthenticationType | String   | The reason for canceling the authentication, also displayed at the mobile applications cancellation screen. Values:- CHANGE\_DEVICE - The user wants to change the authentication device.

- ADD\_DEVICE - The user wants to manage their devices. (they will need to authenticate to get into the self service device management screen)

- DEFAULT - a generic reason. |
| sessionId                | String   | The session id return from a previous call to start authentication.                                                                                                                                                                                                                                                                                                      |
| clientData               | String   | Optional.This value is returned unchanged in the API response. It can be used to save state and/or client context data for the application between API calls.                                                                                                                                                                                                            |

**Response Body Parameters**

Example response body:

```json
{
 "errorMsg": "",
 "uniqueMsgId":"webs_sOFLeIP0EOlR-BnOCN_DTLv1uMpivQRoFN68edsYi4Y",
 "errorId": 200,
 "clientData": "Session data echoed back to the requestor"
}
```

The parameters included in the responseBody object are:

| Parameters  | DataType | Description                                                                                                                   |
| ----------- | -------- | ----------------------------------------------------------------------------------------------------------------------------- |
| clientData  | String   | The value sent in the request's clientData field.                                                                             |
| errorId     | Int      | A numeric error code.                                                                                                         |
| errorMsg    | String   | A textual description of the error, if there was one.                                                                         |
| uniqueMsgId | String   | A unique ID for the response message. This is logged and used to track the specific transaction for troubleshooting purposes. |

## AuthenticateOnline

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | The `authonline` endpoint has been deprecated. Use `startauthentication` instead in conjunction with `authstatus`.In addition to using `startauthentication` for any new code you write for authentication flows, you should consider modifying any existing code that uses `authonline`, replacing it with calls to `startauthentication`. Initiating authentication with `startauthentication` and then polling for results using `authstatus` provides the following advantages:- Use of an event-driven application pattern provides greater flexibility and scalability

- Clearer tracking of authentication sessions through transaction IDs

- More control over the user experience

- Easier handling of multi-step or delayed authentications (such as push approvals) without locking your application into a blocking synchronous process

- Compatibility with future enhancements for PingID

- If you migrate your PingID environment to PingOne, you may encounter authentication issues if your code uses `authonline` rather than the asynchronous approach |

When an organization's user want to access a service that is protected by PingID authentication, the service provider will first try to use online authentication. For example, a customer wants to logon to an online banking service, or an employee wants to access the organization's email platform. After the user enters a username and password and clicks a "Logon" button, the service provider sends an AuthenticateOnline request to the PingID service. If the operation is successful, PingID pushes a message to the user's mobile device, requesting the user to swipe a button or scan a fingerprint. When the user has performed this action, the service provider allows the user to proceed to its entry page.

When you attempt online authentication and the device is not reachable or does not claim the request (for example, the device's lock screen prevents it), the authentication process enters offline mode. You can then use the AuthenticateOffline operation or retry AuthenticateOnline.

When you attempt online authentication and the device claims the request (opens the app), but the user does not respond in time, the authentication process remains in online mode. The intent is that online authentication will then be attempted again.

This is the AuthenticateOnline URL:

```
https://idpxnyl3m.pingidentity.com/pingid/rest/4/authonline/do
```

**Request Body Parameters**

Example reqBody object in the API payload:

```json
"reqHeader": { ... },
"reqBody": {
  "formParameters": {
    "sp_name": "My Application",
    "sp_logo": "https://www.mycorp.com/images/myapp.png",
    "org_logo": "https://www.mycorp.com/images/org_logo.png",
    "bg_color": "#ADADAD",
    "bg_image": "https://www.mycorp.com/images/bg_image.png",
    "FirstTimeAfterPairing": "false"
  },
  "spAlias": "web",
  "userName": "marcher",
  "authType": "CONFIRM",
  "deviceId": 2841591,
  "clientData": "Session data echoed back to the requestor",
  "enforcePolicy": "true",
  "ipAddr": "103.25.46.58",
  "application": "google.com",
  "cookie": "eyJ0dGwiOiIyMDIyLTEyLTAxVDEyOjU0OjEyLjcyMSIsInppcCI6IkRFRiIsImFsZyI6IkEyNTZLVyIsImVuYyI6IkExMjhDQkMtSFMyNTYifQ.2F6W1HOHNSYAJ5fOiWf25HUugxuO_GIuHir3vzhakzj9FtOpAFd7iw.NEUoexj_iw31XPlbYVnXWA.CMVgGFlDhrWySmAcSR6AxDwAMwHCvW1N81CINn_kMEG1l7DcwHJUHv_Lj_udzLoDLgoOxO5TG_rfUO4Lioi4fcqjMBi2kXvRDasPRrKj4feuZoeAbqTHYjhEyUHpaTA7Tesc7R3f2CJtEUjQue5HUoGCUo8gU9y0akOEAToCjSn9_H45F2OyveD0yMnRi7WSEn_ZaoFx55HIaQMl1q8vJE2S8d47FbyW2jBQLbie7G130gESW1Ck4NpoMzs_dbtXQsZ9hOeqUXf_SwYkuQm7BjkmDAmemTA7of1ZU-f_ZFfNNlRh4nFIOTVw_JCZg3e-hI4q6F_xUFl6da8mzrJnRphyjv-_A0MNOY5CFOxLeCT5QU_Hubggfvgaqyy7O_GdkmwrItcWePTspIrQZGNo3q-zSEjx40iJgcukt4I1P3D2nnyrMUpuEizt4PynsS7d7r7jlMDgwpn83chcsK95H_JKS-3ozgtQSysW-sy1Qjf_WJNSkbUyCgf6CPwXoRlEJr3ip4d7AHfvqs_9Xezpwbi8aywagKStrVpQe6T4mNCjoRIt78KlsTIYUdV0wwgmFZTAhlSwsv_bahV2sVJmd77PdbtOYiJcB7r7jyy0IU8gz1Y7EOV9s7IoSdjuF58mLH2Xj5UYCOs1TB08VTPqDcA8RIH5Vg-dWmD55i0_D-lQ9KVNbnYBBMV3345NVy-NMpIOst8SsJZiM4ebTwWQE6EKm6Enbp045pJTBhJ6gQXSaI-jXqw2VkLYHyUqmSkqBfqPVu5yC144rpxfMuX0GjIm0ARJTYBj87MfhgUJdvicOwYbBILwEIzqORuodqeT.1D2of3ZcLD4i9F13rUCgUA",
  "reqDevFP": "\{User-Agent=\"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36\"}",
  "memberOf": ["CN=aliceA,OU=US,OU=Americas,DC=net","CN=bobB,OU=EU,OU=England,DC=net"]
}
```

The parameters included in the reqBody object are:

| Parameters     | DataType   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| -------------- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| authType       | String     | Type of authentication mechanism to use. This is one of the following values:- CONFIRM: Use the authentication type configured in the PingID account settings.

- FINGERPRINT\_PERMISSIVE: Use fingerprint authentication only if the user has configured this preference.

- FINGERPRINT\_RESTRICTIVE: Use fingerprint authentication for any device that supports it, regardless of user configuration.

- FINGERPRINT\_HARD\_RESTRICTIVE: Enforce fingerprint authentication for any device that supports it, regardless of user configuration, and do not allow authentication using banner messages.

- OTP: Force the PingID server to return immediately to perform an OTP authentication only (rather than prompt or wait for the online authentication flow to complete).

- ONE\_TIME\_DEVICE: Use the one time device option for backup authentication. |
| clientData     | String     | Optional. This value is returned unchanged in the API response. It can be used to save state and/or client context data for the application between API calls.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| spAlias        | String     | The PingID service that is being used. In this context, the value of the parameter should be "web" to indicate a web authentication or "rescuecode" to indicate a backup authentication. For more information, see [PingID Services](pid_c_PingIDapiUserManagement.html#pingid-services).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| userName       | String     | The user's PingID username.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| deviceId       | Long       | To specify a specific device to authenticate with. (if not specified, the authentication request will be sent to the default device)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| enforcePolicy  | Boolean    | Set this parameter to "true" to activate policy evaluation. + Default: false.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| ipAddr         | String     | The requesting device's IP address. + Required in cases where enforcePolicy = "true" and IP address policies are evaluated. + When the ipAddr parameter has a value, it is validated to check that the value is in IP address format.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| application    | String     | The requested application's ID, as defined in the application list in the Policy section of the PingID admin portal. + Required in cases where enforcePolicy = "true" and application policies are evaluated. + Maximum length: 500 characters.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| cookie         | String     | The PingID cookie received in the previous authentication response, in cases where enforcePolicy = "true". On completion of a successful authentication using AuthenticateOnline, the cookie parameter returned in the AuthenticateOnline response is populated with the latest authentication transaction's data. For policy evaluation purposes, save this parameter and use it in the user's next authentication request. + Maximum length: 5000 characters                                                                                                                                                                                                                                                                                                                                                                                                     |
| reqDevFP       | String     | The requesting device's user agent. + Required in cases where enforcePolicy = "true" and the device's attributes are evaluated. + Maximum length: 50000 characters                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| memberOf       | json array | List of users and groups. + Required in cases where enforcePolicy = "true" and group policies are evaluated. + Maximum items: 1000.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| deviceType     | String     | Required in cases of backup authentication flows. In a backup authentication, it must be one of:- Email

- SMS

- Voice                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| deviceData     | String     | Required in cases of backup authentication flows. Depending on the selected "deviceType", it must be a phone number or an email address.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| formParameters | Object     | Additional parameters used to customize the authentication. See table below.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |

The formParameters object can contain the following parameters:

| Parameters            | DataType     | Description                                                                                                                                                                                                |
| --------------------- | ------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| sp\_logo              | String (URL) | A URL pointing to an image file of the service provider's logo (PNG file), which is displayed within the PingID application during authentication.                                                         |
| sp\_name              | String       | The name of the service requesting authentication, which is displayed within the PingID app during authentication.                                                                                         |
| org\_logo             | String (URL) | A URL pointing to an image to use as the "organization" logo (the company icon at the top of the PingID authentication screen.                                                                             |
| bg\_color             | String       | A HEX color code for the PingID authentication screen background color.                                                                                                                                    |
| bg\_image             | String (URL) | A URL pointing to an image to use as the background of the PingID authentication screen.                                                                                                                   |
| FirstTimeAfterPairing | Boolean      | Indicates whether this is the first time that authentication is requested after a device was paired with this user. This flag can be used to display a "successful pairing" message during authentication. |

**Response Body Parameters**

Example response body:

```json
{
 "extendedOnlineDetails": {
   "lastSuccessfulLogin": 1437646014000,
   "deviceOSVersion": "4.1.2",
   "deviceFp": "bWxjelNMUEEyUzZEQ0J6NFBqcmE=",
   "performedFormType": "SLIDER",
   "gracePeriod": 1436335200000,
   "adminHelp": "",
   "deviceType": "Android",
   "gpsLocation": {
    "altitude": 297.79999999999995,
    "latitude": 39.748881,
    "longitude": -104.993769,
    "accuracy": 20
   }
 },
 "sessionId": null,
 "errorMsg": "",
 "uniqueMsgId":"webs_sOFLeIP0EOlR-BnOCN_DTLv1uMpivQRoFN68edsYi4Y",
 "errorId": 200,
 "clientData": "Session data echoed back to the requestor",
 "cookie": "eyJ0dGwiOiIyMDIyLTEyLTAxVDEyOjU0OjEyLjcyMSIsInppcCI6IkRFRiIsImFsZyI6IkEyNTZLVyIsImVuYyI6IkExMjhDQkMtSFMyNTYifQ.2F6W1HOHNSYAJ5fOiWf25HUugxuO_GIuHir3vzhakzj9FtOpAFd7iw.NEUoexj_iw31XPlbYVnXWA.CMVgGFlDhrWySmAcSR6AxDwAMwHCvW1N81CINn_kMEG1l7DcwHJUHv_Lj_udzLoDLgoOxO5TG_rfUO4Lioi4fcqjMBi2kXvRDasPRrKj4feuZoeAbqTHYjhEyUHpaTA7Tesc7R3f2CJtEUjQue5HUoGCUo8gU9y0akOEAToCjSn9_H45F2OyveD0yMnRi7WSEn_ZaoFx55HIaQMl1q8vJE2S8d47FbyW2jBQLbie7G130gESW1Ck4NpoMzs_dbtXQsZ9hOeqUXf_SwYkuQm7BjkmDAmemTA7of1ZU-f_ZFfNNlRh4nFIOTVw_JCZg3e-hI4q6F_xUFl6da8mzrJnRphyjv-_A0MNOY5CFOxLeCT5QU_Hubggfvgaqyy7O_GdkmwrItcWePTspIrQZGNo3q-zSEjx40iJgcukt4I1P3D2nnyrMUpuEizt4PynsS7d7r7jlMDgwpn83chcsK95H_JKS-3ozgtQSysW-sy1Qjf_WJNSkbUyCgf6CPwXoRlEJr3ip4d7AHfvqs_9Xezpwbi8aywagKStrVpQe6T4mNCjoRIt78KlsTIYUdV0wwgmFZTAhlSwsv_bahV2sVJmd77PdbtOYiJcB7r7jyy0IU8gz1Y7EOV9s7IoSdjuF58mLH2Xj5UYCOs1TB08VTPqDcA8RIH5Vg-dWmD55i0_D-lQ9KVNbnYBBMV3345NVy-NMpIOst8SsJZiM4ebTwWQE6EKm6Enbp045pJTBhJ6gQXSaI-jXqw2VkLYHyUqmSkqBfqPVu5yC144rpxfMuX0GjIm0ARJTYBj87MfhgUJdvicOwYbBILwEIzqORuodqeT.1D2of3ZcLD4i9F13rUCgUA"
}
```

The parameters included in the responseBody object are:

| Parameters            | DataType | Description                                                                                                                                                                                                                               |
| --------------------- | -------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| clientData            | String   | The value sent in the request's clientData field.                                                                                                                                                                                         |
| errorId               | Int      | A numeric error code.                                                                                                                                                                                                                     |
| errorMsg              | String   | A textual description of the error, if there was one.                                                                                                                                                                                     |
| sessionId             | String   | If online authentication fails for any reason, the session ID will be used when requesting offline authentication.                                                                                                                        |
| uniqueMsgId           | String   | A unique ID for the response message. This is logged and used to track the specific transaction for troubleshooting purposes.                                                                                                             |
| extendedOnlineDetails | Object   | An object containing additional information. See details in the table below.                                                                                                                                                              |
| cookie                | String   | A new PingID cookie received in cases where enforcePolicy = "true". For policy evaluation purposes, save the updated value of the cookie parameter, and use it in the user's next authentication request. Maximum length: 5000 characters |

Extended online details:

| Parameters          | DataType         | Description                                                                                    |
| ------------------- | ---------------- | ---------------------------------------------------------------------------------------------- |
| lastSuccessfulLogin | DateTime (epoch) | Last time this user auccessfully authenticated (in UNIX epoch format).                         |
| deviceOSVersion     | String           | OS version of the device.                                                                      |
| deviceFp            | String           | PingID device fingerprint.                                                                     |
| performedFormType   | String           | Which form type was used for authentication, value will be "SLIDER".                           |
| gracePeriod         | DateTime (epoch) | When the grace period to allow bypassing PingID authentication expires (in UNIX epoch format). |
| adminHelp           | String           | Descriptive prompt the application can display to direct the end user for help.                |
| deviceType          | String           | Device type (such as, Android, iPhone).                                                        |
| gpsLocation         | Object           | GPS location of the device at authentication.                                                  |

## AuthenticateOffline

Offline authentication is performed when one of the following conditions applies:

* The user has configured a preference for authentication by SMS, voice message, email, YubiKey, FIDO security key or OATH token.

* The user's device is inaccessible over the internet.

* The user's device cannot receive push notifications (due to a firewall or other local restrictions).

Before the AuthenticateOffline operation can be performed, the user must manually enter a one-time password which is generated by the PingID mobile app, by a YubiKey or FIDO security key or FIDO biometrics, or sent via SMS, voice message or email. Once the user has entered the OTP, the service provider application calls AuthenticateOffline, while passing the OTP value to PingID.

In the case of a FIDO security key or FIDO biometrics authentication flow, activation of the WebAuthnStartAuth API and the call to the browser's navigator.credentials.get function are required prior to the AuthenticateOffline API activation. WebAuthnStartAuth and the navigator.credentials.get function generate values which are used as AuthenticateOffline API input parameters. The AuthenticateOffline API completes the FIDO security key or FIDO biometrics authentication flow. For further information, refer to:

* [Example: PingID FIDO security key](pid_c_PingIDapiExampleFIDOsecurityKey.html)

* [Example: PingID FIDO biometrics](pid_c_PingIDapiExampleFIDObiometrics.html)

This is the AuthenticateOffline URL:

```
https://idpxnyl3m.pingidentity.com/pingid/rest/4/authoffline/do
```

**Request Body Parameters**

Example reqBody object in the API payload:

```json
"reqHeader": { ... },
"reqBody": {
  "spAlias": "web",
  "userName": "marcher",
  "otp": "111111",
  "sessionId": "abcd123",
  "clientData": "Session data echoed back to the requestor"
}
```

The parameters included in the reqBody object are:

| Parameters     | DataType                | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| -------------- | ----------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| otp            | String                  | The "otp" parameter value may be one of the following, depending on the authenticating device:- Mobile, SMS, voice or email devices: The value of the one-time passcode that the user entered.

- YubiKey which features OTP support: The value of the encrypted one-time passcode generated by the YuibiKey.

- FIDO security key: The authentication assertion response from the authenticator.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| sessionId      | String                  | The sessionId value returned in the AuthenticateOnline response.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| clientData     | String                  | Optional. This value is returned unchanged in the API response. It can be used to save state and/or client context data for the application between API calls.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| spAlias        | String                  | The PingID service that is being used. In this context, the value of the parameter should be "web" to indicate a web authentication or "rescuecode" to indicate a backup authentication. For more information, see [PingID Services](pid_c_PingIDapiUserManagement.html#pingid-services).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| userName       | String                  | The user's PingID username.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| formParameters | Map + \<String, String> | Optional key/value pairs, unless the authenticating device is a FIDO security key. When implementing an OATH token resync during an authentication flow, you can instruct the server to try to match an invalid OTP against a larger test window, by providing the following key/value pair:- `"oathResync":"true"`Provide the following mandatory parameters when the authenticating device is a FIDO security key:- origin: The scheme and domain of the URL that the user wants to access. - rpId: The domain of the URL that the user wants to access. The rpId that is used for pairing must be used for authentication. - authWebauthnSessionId: The WebAuthn session ID.If any of the mandatory parameters are not valid, an internal server error is returned.Refer to:- [Example: PingID FIDO security key](pid_c_PingIDapiExampleFIDOsecurityKey.html)- [Example: PingID FIDO biometrics](pid_c_PingIDapiExampleFIDObiometrics.html) |

**Response Body Parameters**

Example response body:

```json
{
 "sessionId": "abcd123",
 "errorMsg": "",
 "uniqueMsgId":"webs_sOFLeIP0EOlR-BnOCN_DTLv1uMpivQRoFN68edsYi4Y",
 "errorId": 200,
 "clientData": "Session data echoed back to the requestor",
 "cookie": "eyJ0dGwiOiIyMDIyLTEyLTAxVDEyOjU0OjEyLjcyMSIsInppcCI6IkRFRiIsImFsZyI6IkEyNTZLVyIsImVuYyI6IkExMjhDQkMtSFMyNTYifQ.2F6W1HOHNSYAJ5fOiWf25HUugxuO_GIuHir3vzhakzj9FtOpAFd7iw.NEUoexj_iw31XPlbYVnXWA.CMVgGFlDhrWySmAcSR6AxDwAMwHCvW1N81CINn_kMEG1l7DcwHJUHv_Lj_udzLoDLgoOxO5TG_rfUO4Lioi4fcqjMBi2kXvRDasPRrKj4feuZoeAbqTHYjhEyUHpaTA7Tesc7R3f2CJtEUjQue5HUoGCUo8gU9y0akOEAToCjSn9_H45F2OyveD0yMnRi7WSEn_ZaoFx55HIaQMl1q8vJE2S8d47FbyW2jBQLbie7G130gESW1Ck4NpoMzs_dbtXQsZ9hOeqUXf_SwYkuQm7BjkmDAmemTA7of1ZU-f_ZFfNNlRh4nFIOTVw_JCZg3e-hI4q6F_xUFl6da8mzrJnRphyjv-_A0MNOY5CFOxLeCT5QU_Hubggfvgaqyy7O_GdkmwrItcWePTspIrQZGNo3q-zSEjx40iJgcukt4I1P3D2nnyrMUpuEizt4PynsS7d7r7jlMDgwpn83chcsK95H_JKS-3ozgtQSysW-sy1Qjf_WJNSkbUyCgf6CPwXoRlEJr3ip4d7AHfvqs_9Xezpwbi8aywagKStrVpQe6T4mNCjoRIt78KlsTIYUdV0wwgmFZTAhlSwsv_bahV2sVJmd77PdbtOYiJcB7r7jyy0IU8gz1Y7EOV9s7IoSdjuF58mLH2Xj5UYCOs1TB08VTPqDcA8RIH5Vg-dWmD55i0_D-lQ9KVNbnYBBMV3345NVy-NMpIOst8SsJZiM4ebTwWQE6EKm6Enbp045pJTBhJ6gQXSaI-jXqw2VkLYHyUqmSkqBfqPVu5yC144rpxfMuX0GjIm0ARJTYBj87MfhgUJdvicOwYbBILwEIzqORuodqeT.1D2of3ZcLD4i9F13rUCgUA"
}
```

The parameters included in the responseBody object are:

| Parameters         | DataType              | Description                                                                                                                                                                                                                                                                                                                                      |
| ------------------ | --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| clientData         | String                | The value sent in the request's clientData field.                                                                                                                                                                                                                                                                                                |
| cookie             | String                | A new PingID cookie received in cases where enforcePolicy = "true". For policy evaluation purposes, save the updated value of the cookie parameter, and use it in the user's next authentication request. Maximum length: 5000 characters                                                                                                        |
| errorId            | Int                   | A numeric error code.                                                                                                                                                                                                                                                                                                                            |
| errorMsg           | String                | A textual description of the error, if there was one.                                                                                                                                                                                                                                                                                            |
| uniqueMsgId        | String                | A unique ID for the response message. This is logged and used to track the specific transaction for troubleshooting purposes.                                                                                                                                                                                                                    |
| sessionId          | String                | The sessionId value sent in the request.                                                                                                                                                                                                                                                                                                         |
| embeddedParameters | Map \<String, String> | Optional key/value pairs:- oathSerialNumber

- oathTokenType: HOTP or TOTPFor OATH tokens, it is used to provide the client with the oathSerialNumber and oathTokenType.In device management, it provides instructions to the user based on the token type, or sends the resync request with the serial number, without the user re-entering it. |

## WebAuthnStartAuth (FIDO security key, FIDO biometrics, FIDO2 devices)

The WebAuthnStartAuth API is an integral step in authentication flows for FIDO security keys, FIDO biometrics, and FIDO2 devices. On the basis of input parameters provided as outputs from the StartAuth API, the WebAuthnStartAuth API returns parameter data for public key credentials. These parameters are required as an input for the next step in the WebAuthn authentication flow, the call to the browser's navigator.credentials.get function, which will return the public key credentials. For further information, refer to [Example: PingID FIDO security key](pid_c_PingIDapiExampleFIDOsecurityKey.html) and [Example: PingID FIDO biometrics](pid_c_PingIDapiExampleFIDObiometrics.html).

This is the WebAuthnStartAuth URL:

```
https://idpxnyl3m.pingidentity.com/pingid/rest/4/webauthnstartauth/do
```

**Request Body Parameters**

Example reqBody object in the API payload for security key:

```json
"reqHeader": { ... },
"reqBody": {
  "rpId": "pingone.com",
  "userName": "fidouser1",
  "deviceUuid": "0f0eaf16-bc75-b440-0f0e-af16bc75b440",
  "webauthnType": "WebAuthn"
}
```

Example reqBody object in the API payload for biometrics:

```json
"reqBody": {
    "rpId": "pingone.com",
    "userName": "fidouser1",
    "deviceUuid": "16e3f7de-f6af-9cf0-16e3-f7def6af9cf0",
    "webauthnType": "webauthn_platform"
  }
```

The parameters included in the reqBody object are:

| Parameters   | DataType | Description                                                                                                                                                                                            |
| ------------ | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| rpId         | String   | Domain of the service provider. The rpId that is used for pairing must be used for authentication.                                                                                                     |
| userName     | String   | The user's PingID username.                                                                                                                                                                            |
| deviceUuid   | String   | The FIDO security key's unique device ID or the FIDO biometric platform's unique device ID. Mandatory for FIDO security keys, optional for FIDO biometrics and for FIDO2 devices.                      |
| webauthnType | String   | Set to `WebAuthn` for authentication of a FIDO security key. Set to `webauthn_platform` for authentication of a FIDO2 supported biometric platform. For FIDO2 devices, this parameter is not required. |

**Response Body Parameters**

Example response body:

```json
{
    "clientData": null,
    "errorId": 200,
    "errorMsg": "",
    "sessionId": "abec8ed8-13fc-4c49-a157-9db1ffaf74f4",
    "publicKeyCredentialOptions": "{\"challenge\":[-22,-63,-8,98,-35,-54,92,-25,-13,-76,-51,86,-120,63,-11,89,45,-20,86,-63,114,-65,26,34,13,-84,-4,112,-110,66,-12,-31],\"timeout\":120000,\"rpId\":\"pingone.com\",\"allowCredentials\":[{\"type\":\"public-key\",\"id\":[11,35,-62,-60,-118,-97,126,80,17,121,-30,-50,122,8,-42,-87,-123,56,29,106,90,68,57,-99,-108,13,45,93,11,-13,80,54],\"transports\":[\"internal\"]}],\"userVerification\":\"preferred\"}",
    "uniqueMsgId": "webs_ohi_slDY5XVgotezgpFMNlCIW7NtLvLrWxVo8gFCe14AXw4"
}
```

The parameters included in the response body object are:

| Parameters                 | DataType | Description                                                                                                                                          |
| -------------------------- | -------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| publicKeyCredentialOptions | String   | JSON structure containing parameters for retrieving the public key credentials for the FIDO security key, FIDO biometrics, or FIDO2 device.          |
| sessionId                  | String   | The WebAuthn session ID.                                                                                                                             |
| errorId                    | Int      | A numeric response code indicating the success or failure state of the API call.                                                                     |
| errorMsg                   | String   | Text describing the state or cause of an unsuccessful API call.                                                                                      |
| clientData                 | String   | This value is returned unchanged in the API response. It can be used to save state and/or client context data for the application between API calls. |
| deviceId                   | String   | Unique identifier for the device being paired.                                                                                                       |
| deviceUuid                 | String   | UUID representation of the device being paired.                                                                                                      |

## StartWebAuthnPasswordlessAuth

The StartWebAuthnPasswordlessAuth API is an integral step in the passwordless authentication flow. The StartWebAuthnPasswordlessAuth API returns parameter data for public key credentials. These parameters are required as an input for the next step in the passwordless authentication flow, the call to the browser's navigator.credentials.get function, which will return the public key credentials. For further information, refer to [Example: PingID Passwordless Authentication](pid_c_PingIDapiExamplePasswordless.html).

This is the StartWebAuthnPasswordlessAuth URL:

```
https://idpxnyl3m.pingidentity.com/pingid/rest/4/startwebauthnpasswordlessauth/do
```

**Request Body Parameters**

```json
"reqBody": {
    "rpId": "pingone.com",
    "origin": "https://admin.pingone.com",
    "spAlias": "web"
  }
```

| Parameters | DataType | Description                                                                                                                                                                                                                   |
| ---------- | -------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| rpId       | String   | Domain of the service provider. The rpId that is used for pairing must be used for authentication.                                                                                                                            |
| origin     | String   | The scheme and domain of the URL that the user wants to access.                                                                                                                                                               |
| spAlias    | String   | The PingID service that is being used. In this context, the value of the parameter must be "web". For more information, see [PingID Services](/{{pingidApisPath}}/pingid-api/pid_c_PingIDapiUserManagement/#PingID-Services). |

**Response Body Parameters**

Example reqBody object in the API payload:

```json
"responseBody": {
    "clientData": null,
    "errorId": 200,
    "errorMsg": "",
    "sessionId": "webs_btwh200zYkv1LfUAvmc1MIJWzGXjS4jPTr2saKcOcuA",
    "cookie": null,
    "errorParams": null,
    "publicKeyCredentialOptions": "{\"challenge\":[-33,47,7,-85,84,4,46,55,-20,1,96,-61,118,-95,50,-33,-66,117,-108,-70,69,-13,82,124,43,94,95,81,26,-86,84,50],\"timeout\":120000,\"rpId\":\"pingone.com\",\"allowCredentials\":[],\"userVerification\":\"preferred\"}",
    "uniqueMsgId": "webs_btwh200zYkv1LfUAvmc1MIJWzGXjS4jPTr2saKcOcuA"
  }
```

The parameters included in the response body object are:

| Parameters                 | DataType | Description                                                                                                                                                                                                                               |
| -------------------------- | -------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| clientData                 | String   | This value is returned unchanged in the API response. It can be used to save state and/or client context data for the application between API calls.                                                                                      |
| errorId                    | Int      | A numeric response code indicating the success or failure state of the API call.                                                                                                                                                          |
| errorMsg                   | String   | Text describing the state or cause of an unsuccessful API call.                                                                                                                                                                           |
| sessionId                  | String   | The WebAuthn session ID.                                                                                                                                                                                                                  |
| cookie                     | String   | A new PingID cookie received in cases where enforcePolicy = "true". For policy evaluation purposes, save the updated value of the cookie parameter, and use it in the user's next authentication request. Maximum length: 5000 characters |
| publicKeyCredentialOptions | String   | JSON structure containing parameters for retrieving the public key credentials.                                                                                                                                                           |
| uniqueMsgId                | String   | A unique ID for the response message. This is logged and used to track the specific transaction for troubleshooting purposes.                                                                                                             |

## FinishWebAuthnPasswordlessAuth

The FinishWebAuthnPasswordlessAuth API is an integral step in the passwordless authentication flow. The FinishWebAuthnPasswordlessAuth uses the value returned in the publicKeyCredential parameter of the navigator.credentials.get function.

The FinishWebAuthnPasswordlessAuth API is also used to check for optional policy enforcement. When the admin has configured the policy as enforced, the errorId is returned with a value of 30014, and then the StartAuthentication API must be run with the relevant "memberOf" group parameter, to complete the authentication flow.

For further information, refer to [Example: PingID Passwordless Authentication](pid_c_PingIDapiExamplePasswordless.html).

This is the FinishWebAuthnPasswordlessAuth URL:

```
https://idpxnyl3m.pingidentity.com/pingid/rest/4/finishwebauthnpasswordlessauth/do
```

**Request Body Parameters**

Example reqBody object in the API payload:

```json
"reqBody": {
    "publicKeyCredentialJson": "<returned from navigator.credentials.get>",
    "sessionId": "webs_btwh200zYkv1LfUAvmc1MIJWzGXjS4jPTr2saKcOcuA"
  }
```

The parameters included in the reqBody object are:

| Parameter               | DataType | Description                                                                    |
| ----------------------- | -------- | ------------------------------------------------------------------------------ |
| publicKeyCredentialJson | String   | Returned from "**navigator.credentials.get**".                                 |
| sessionId               | String   | The session id returned from a previous call to StartWebAuthnPasswordlessAuth. |

**Response Body Parameters**

* Example response, when the admin has configured enforcePolicy = "false":

  ```json
    {
    "responseBody": {
      "clientData": null,
      "errorId": 200,
      "errorMsg": "",
      "userName": marcher,
      "uniqueMsgId": "webs_OnrdXH9gmelZ1P-GXyWa0zBA7Y6dXDfveO-G8-4n62s"
    }
  ```

* Example response, when the admin has configured enforcePolicy = "true":

  ```json
      {
      "responseBody": {
          "clientData": null,
          "errorId": 30014,
          "errorMsg": "policy.evaluation.required",
          "userName": marcher,
          "uniqueMsgId": "webs_OnrdXH9gmelZ1P-GXyWa0zBA7Y6dXDfveO-G8-4n62s"
      }
  ```

The parameters included in the reqBody object are:

| Parameter   | DataType | Description                                                                                                                                                    |
| ----------- | -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| clientData  | String   | Optional. This value is returned unchanged in the API response. It can be used to save state and/or client context data for the application between API calls. |
| errorId     | Int      | A numeric error code.                                                                                                                                          |
| errorMsg    | String   | A textual description of the response, if there was one.                                                                                                       |
| userName    | String   | The user's PingID username.                                                                                                                                    |
| uniqueMsgId | String   | A unique ID for the response message. This is logged and used to track the specific transaction for troubleshooting purposes.                                  |
