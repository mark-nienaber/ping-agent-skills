---
title: Authentication using browser redirect (PPM request)
description: PingID APIs are typically used to create custom authentication request flows.
component: pingid-api
page_id: pingid-api::pid_c_PingIDapiPpmrequest
canonical_url: https://developer.pingidentity.com/pingid-api/pid_c_PingIDapiPpmrequest.html
section_ids:
  ppm-request: PPM request
  ppm-request-workflow: PPM request workflow
  example-ppm-request: Example PPM request
  ppm-request-for-fido-authentication-with-a-hybrid-ui: PPM request for FIDO authentication with a hybrid UI
  using-ppm-request-for-fido-authentication-with-a-hybrid-ui: Using PPM request for FIDO authentication with a hybrid UI
  workflow-for-ppm-request-for-fido-pairing-and-authentication-with-a-hybrid-ui: Workflow for PPM request for FIDO pairing and authentication with a hybrid UI
  example-ppm-request-for-fido-pairing-with-a-hybrid-ui: Example PPM request for FIDO pairing with a hybrid UI
  example-ppm-request-for-fido-authentication-with-a-hybrid-ui: Example PPM request for FIDO authentication with a hybrid UI
---

# Authentication using browser redirect (PPM request)

## PPM request

PingID APIs are typically used to create custom authentication request flows.

The PPM request mechanism is available as a simpler alternative. By using the PPM request parameters as inputs, the PingID Authenticator manages the authentication flows for PingID MFA, and also provides the relevant PingID UIs. Thus, PPM request is the contract between external systems and PingIdentity MFA.

The protocol for communicating with PingID MFA is via JWT, which is a JSON representation encoded in base64 and signed using a secret key and signing algorithm. PingID MFA currently uses the HS256 algorithm.

The PPM request comprises the payload of a JWT that is sent to PingID MFA.

The request returns a response containing a JWT with a PPM response JSON payload.

### PPM request workflow

The following steps are the high-level description of the PPM request workflow:

1. Create and populate a JSON representation of a PPM request.

2. Depending on organization settings, populate the PPM request with any additional attributes required for successful authentication.

3. Sign the request to ensure the request's reliability.

4. POST the PPM request.

### Example PPM request

The following steps illustrate the PPM request workflow:

1. Populate the PPM request with all mandatory values.

   **Request payload parameters**

   Example request payload object:

   ```json
      {
           "iss":"PingFed",
           "sub":"jsmith",
           "aud":"pingidauthenticator",
           "nonce": "9t98et98ert",
           "exp":1401319565,
           "iat":1401318965,
           "jti":"12345678901075283750894",
           "confVersion": 1,
           "idpAccountId":"cde21617-6201-4f66-8866-a149625acd0b",
           "returnUrl":
      "https://sso.connect.pingidentity.com/sso/ppm/ID601c46187df0ece3fda608ed1d06e23c179c061347ce909b01"
            "attributes": [
               {
                 "name": "fname", "value": "John"
               },
               {
                 "name": "lname", "value": "Smith"
               },
               {
                 "name": "isUserAuthenticated",
                 "value": "true"
               },
               {
                 "name": "appName",
                 "value": "This is my App Name"
               },
               {
                 "name": "appIconUrl",
                 "value": "https://www.pingidentity.com/content/dam/pic/downloads/resources/Misc/PIC_square_logo_PIC_red_RGB.png"
               }
            ],
           "dst": "https://authenticator.pingone.com/pingid/ppm/auth"
      }
   ```

   The parameters included in the request payload:

   | Parameter    | Description                                                                                                                                                                                                                              |
   | ------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | idpAccountId | CAS account ID. The unique ID of the local instance that enables PingID to identify the tenant instance in its services. Its value is the org\_alias from the organization's settings.                                                   |
   | iss          | Issuer (sender) of the request, for example "PingFed".                                                                                                                                                                                   |
   | sub          | The PingOne system-level username.                                                                                                                                                                                                       |
   | aud          | The destination application that the request should go to, which is the MFA authenticating app. For example, "pingidauthenticator".                                                                                                      |
   | returnUrl    | The URL that the PPM response will be directed to.                                                                                                                                                                                       |
   | nonce        | A random unique request ID used to associate a client session with an authentication response, and to mitigate replay attacks. The value is passed without modification, from the authentication request to the authentication response. |
   | iat          | The request's "issued at" epoch time.                                                                                                                                                                                                    |
   | exp          | The request's expiration epoch time.                                                                                                                                                                                                     |
   | jti          | Optional. The JWT ID or token ID (tracking ID).                                                                                                                                                                                          |
   | idpEntityId  | Optional. Reserved for future use.                                                                                                                                                                                                       |
   | dst          | Optional. The URL of the intended destination of the request. Intended for matching server and destination content.                                                                                                                      |
   | attributes   | Optional. Contains a list of PPMAttribute elements, where PPMAttribute is a simple object comprising a name and value pair.                                                                                                              |

2. Depending on organization settings, populate the PPM request with any additional attributes required for successful authentication.

   Optional sub-attributes in the "attributes" object:

   | Parameter                                               | Description                                                                                                                                      |
   | ------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
   | fname                                                   | User's first name. Used by PingID.                                                                                                               |
   | lname                                                   | User's last name. Used by PingID.                                                                                                                |
   | email/mail/USER\_ATTRIBUTE\_EMAIL/dirMail               | User's mail. Used by PingID.                                                                                                                     |
   | phone/phoneNumber/USER\_ATTRIBUTE\_PHONE/dirPhoneNumber | User's phone. Used by PingID.                                                                                                                    |
   | isUserAuthenticated                                     | Validates first factor authentication. Must be set to true in order to pass authentication.                                                      |
   | appName                                                 | The application name that is passed to the adapter, to enable PingID to mutually authenticate the user.                                          |
   | appIconUrl                                              | The application icon URL passed to the adapter to enable PingID to authenticate the user. For example, a branded icon for the PingID Mobile App. |
   | pingidIp                                                | The IP of the accessing device. Used by PingID policy, if configured.                                                                            |
   | saasid                                                  | The application's ID. Used by PingID policy, if configured.                                                                                      |
   | pingidSpAlias                                           | The calling app. If empty, its value will default to "pingone".                                                                                  |
   | pingidHostName                                          | RDP (reserved for future use).                                                                                                                   |
   | pingidOpSystem                                          | RDP (reserved for future use).                                                                                                                   |
   | pingidInstallVer                                        | RDP (reserved for future use).                                                                                                                   |
   | pingidIsRemote                                          | RDP (reserved for future use).                                                                                                                   |

3. Sign the request's JSON representation. Signing is mandatory, to ensure the request's reliability. The signature requires:

   * The relevant organization base64 secret key from the PingOne client integration settings file.

   * The signing algorithm.

   The token can be created using any certified JWT library.

4. POST the signed JWT to the authenticator endpoint:

   ```
    https://authenticator.pingone.com/pingid/ppm/auth
   ```

   Pass the following HTTP parameters in the POST request:

   | Parameter        | Description                                                                                                                  |
   | ---------------- | ---------------------------------------------------------------------------------------------------------------------------- |
   | idp\_account\_id | The IDP account ID and organization alias. This is identical to the value of the PPMRequest object's idpAccountId attribute. |
   | iss              | The sender application. This is identical to the value of the PPMRequest object's iss attribute.                             |
   | ppm\_request     | The signed JWT.                                                                                                              |

   The authentication response will be passed to the address in the return URL which is defined in the request object.

   The PPM response will return either a successful authentication status, or one of the following error codes in the case of a failure:

   | Error code  | Description                  |
   | ----------- | ---------------------------- |
   | AUTH\_001   | System error                 |
   | AUTH\_002   | Configuration error          |
   | PINGID\_001 | General authentication error |
   | PINGID\_002 | Invalid state                |
   | PINGID\_003 | Request expired              |
   | PINGID\_004 | Invalid session              |
   | PINGID\_005 | Invalid phone number         |
   | PINGID\_006 | Enrollment general error     |
   | PINGID\_007 | Device not enabled           |

   **Response payload parameters**

   PPM success response JSON structure example:

   ```json
      {
        "iss": "pingidauthenticator",
        "sub": "jsmith",
        "aud": "PingFed",
        "nonce": "zPxFKYXf1UUUypmg3dpz",
        "exp": 1494319263,
        "iat": 1494318963,
        "jti": "RYKCTVYY3KIKI===",
        "status": "success",
        "idpAccountId": "3636ccf8-0110-4230-b5dc-ef0280780239",
        "authnContext": "urn:oasis:names:tc:SAML:2.0:ac:classes:Telephony",
        "inResponseTo": "9t98et98ert",
        "dst": "https://sso.connect.pingidentity.com/sso/ppm/ID601c46187df0ece3fda608ed1d06e23c179c061347ce909b01"
      }
   ```

   PPM failure response JSON structure example:

   ```json
      {
        "iss": "pingidauthenticator",
        "sub": "jsmith",
        "aud": "PingFed",
        "exp": 1494317985,
        "iat": 1494317685,
        "jti": "CHVTII5FASSYY===",
        "status": "failure",
        "idpAccountId": "3636ccf8-0110-4230-b5dc-ef0280780239",
        "inResponseTo": "9t98et98ert",
        "errorCode": "PFAUTH_002",
        "message": "The PingID user does not have a registered device but the MFA request was from PingFederate and indicated that the user had not been previously authenticated.",
        "dst": "https://sso.connect.pingidentity.com/sso/ppm/ID601c46187df0ece3fda608ed1d06e23c179c061347ce909b01"
      }
   ```

   The parameters included in the response payload object are:

   | Parameter    | Description                                                                                                                                                                                                                                                       |
   | ------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | iss          | The module where the authentication occurred. This is the value of the request's aud parameter.                                                                                                                                                                   |
   | idpAccountId | CAS account id. The unique ID of the local instance, to enable PingID to identify the tenant instance in its services. This is the value of the request's iss parameter.                                                                                          |
   | sub          | The PingOne system-level username. This is the value of the sub parameter in the request.                                                                                                                                                                         |
   | aud          | The application to return to. This is the value of the request's iss parameter.                                                                                                                                                                                   |
   | nonce        | The value that was provided for the *nonce* parameter in the request.*Note: In some cases of request failure, the response will not include a value for the nonce parameter even though it was provided in the request. Your code should take this into account.* |
   | iat          | The response's "issued at" epoch time.                                                                                                                                                                                                                            |
   | exp          | The response's expiration epoch time.                                                                                                                                                                                                                             |
   | jti          | Newly generated random unique ID.                                                                                                                                                                                                                                 |
   | status       | The status of the authentication operation: success or failure.                                                                                                                                                                                                   |
   | inResponseTo | The tracking ID, passed from the request's jti field.                                                                                                                                                                                                             |
   | dst          | The destination URL. This is the value of the request's returnUrl parameter.                                                                                                                                                                                      |
   | errorCode    | The error status code resulting in the event of a failed transaction.                                                                                                                                                                                             |
   | message      | The error message resulting in the event of a failed transaction.                                                                                                                                                                                                 |
   | authnContext | The authentication context URI. For example, "urn:oasis:names:tc:SAML:2.0:ac:classes:Telephony".                                                                                                                                                                  |
   | group        | User groups from the directory in JSON array format.                                                                                                                                                                                                              |

## PPM request for FIDO authentication with a hybrid UI

### Using PPM request for FIDO authentication with a hybrid UI

FIDO's WebAuthn standard specification requires the registration (pairing) domain and the authentication domain to be the same. However, there are scenarios where this is not the case, for example, when the registration process is done with a custom UI that is hosted on a custom domain, while the authentication process is with PingID's out of the box UI and PingOne's domain.

PingID supports use cases of FIDO hybrid mode authentication, where a custom UI (not hosted by PingID) is used for registration, while PingID's out of the box UI is used for authentication. PPM request, which was originally developed to support authentication, also supports explicit FIDO registration.

For example, when users select a FIDO authentication method, they are redirected to PingID's registration page to enroll for that authentication method. After confirming their presence and registering with FIDO credentials, they are redirected back to the organization's page.

Refer to the sample code in [Ping Identity's GitHub repository](https://github.com/pingidentity/pingid-devices-management-sample).

### Workflow for PPM request for FIDO pairing and authentication with a hybrid UI

The following steps are the high-level description of the PPM request workflow for FIDO pairing with a hybrid UI:

1. Verify that the browser supports WebAuthn registration (pairing).

2. Create and populate a JSON representation of a PPM request.

3. Populate the PPM request with the additional attribute required for the FIDO hybrid UI use case.

4. Sign the request to ensure the request's reliability.

5. POST redirect to the PPM request.

### Example PPM request for FIDO pairing with a hybrid UI

The following steps illustrate the PPM request workflow for FIDO pairing with a hybrid UI:

1. Verify that the browser supports WebAuthn registration (pairing).

   a) For FIDO security key:

   ```javascript
    window.IsWebAuthnSupported = function IsWebAuthnSupported() {
        if (!window.PublicKeyCredential) {
            console.log("Web Authentication API is not supported on this browser.");
            return false;
        }
        return true;
    }
   ```

   b) For FIDO biometrics:

   ```javascript
    window.IsWebAuthnSupported = function IsWebAuthnSupported() {
        if (!window.PublicKeyCredential) {
            console.log("Web Authentication API is not supported on this browser.");
            return false;
        }
        return true;
    }
    window.isWebAuthnPlatformAuthenticatorAvailable = function isWebAuthnPlatformAuthenticatorAvailable() {
        var timer;
        var p1 = new Promise(function(resolve) {
            timer = setTimeout(function() {
                console.log("isWebAuthnPlatformAuthenticatorAvailable - Timeout");
                resolve(false);
            }, 1000);
        });
        var p2 = new Promise(function(resolve) {
            if (IsWebAuthnSupported() && window.PublicKeyCredential.isUserVerifyingPlatformAuthenticatorAvailable) {
                resolve(
                    window.PublicKeyCredential.isUserVerifyingPlatformAuthenticatorAvailable().catch(function(err) {
                        console.log(err);
                        return false;
                    }));
            }
            else {
                resolve(false);
            }
        });
        return Promise.race([p1, p2]).then(function (res) {
            clearTimeout(timer);
            console.log("isWebAuthnPlatformAuthenticatorAvailable - " +  res);
            return res;
        });
    }
   ```

2. Populate the PPM request with all mandatory values.

   **Request payload parameters**

   Example request payload object:

   ```json
    {
      "iss": "PingFed",
      "sub": "username",
      "aud": "md",
      "nonce": "whPAxcspnuBDIt6EhSq9",
      "exp": 1573130051,
      "iat": 1573128251,
      "jti": "",
      "idpAccountId": "a3407e72-71af-4831-a6a1-37e5e94fc07d",
      "attributes": [
            { "name": "webauthnEnrollmentType", "value": "webauthn_platform" },
            { "name": "webauthnDisplayName", "value": "User1@pingidentity.com" },
            { "name": "webauthnName", "value": "User1" }
        ],
      "returnUrl": "http://httpbin.org/post"
    }
   ```

   The parameters included in the request payload:

   | Parameter    | Description                                                                                                                                                                                                                              |
   | ------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | idpAccountId | CAS account ID. The unique ID of the local instance that enables PingID to identify the tenant instance in its services. Its value is the org\_alias from the organization's settings.                                                   |
   | iss          | Issuer (sender) of the request, for example "PingFed".                                                                                                                                                                                   |
   | sub          | The PingOne system-level username.                                                                                                                                                                                                       |
   | aud          | The destination application that the request should go to, which is the MFA authenticating app. For example, "pingidauthenticator".                                                                                                      |
   | returnUrl    | The URL that the PPM response will be directed to.                                                                                                                                                                                       |
   | nonce        | A random unique request ID used to associate a client session with an authentication response, and to mitigate replay attacks. The value is passed without modification, from the authentication request to the authentication response. |
   | iat          | The request's "issued at" epoch time.                                                                                                                                                                                                    |
   | exp          | The request's expiration epoch time.                                                                                                                                                                                                     |
   | jti          | Optional. The JWT ID or token ID (tracking ID).                                                                                                                                                                                          |
   | idpEntityId  | Optional. Reserved for future use.                                                                                                                                                                                                       |
   | dst          | Optional. The URL of the intended destination of the request. Intended for matching server and destination content.                                                                                                                      |
   | attributes   | Optional. Contains a list of PPMAttribute elements, where PPMAttribute is a simple object comprising a name and value pair.                                                                                                              |

3. Populate the PPM request with the additional webauthnEnrollmentType attribute (in the request's "attributes" object), required for the hybrid use case. Optionally, you can also provide values for the webauthnName and webauthnDisplayName attributes.

   | Parameter              | Description                                                                                                                                                                                                                                                                                                                                                  |
   | ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
   | webauthnEnrollmentType | Valid values:\<ul>\<li>"webauthn" for pairing a FIDO security key.\</li>\<li>"webauthn\_platform" for pairing a FIDO biometric device.\</li>\</ul>                                                                                                                                                                                                           |
   | webauthnName           | Provide a value for this parameter if you would like to display specific user information text on the account selection screen instead of the default information displayed by the device for the name field. The string can be up to 100 characters. (Keep in mind that the actual number of characters that will be displayed is device-dependent.)        |
   | webauthnDisplayName    | Provide a value for this parameter if you would like to display specific user information text on the account selection screen instead of the default information displayed by the device for the displayName field. The string can be up to 100 characters. (Keep in mind that the actual number of characters that will be displayed is device-dependent.) |

4. Sign the request's JSON representation. Signing is mandatory, to ensure the request's reliability.\
   The signature requires:

   * The relevant organization base64 secret key from the PingOne client integration settings file.

   * The signing algorithm.

   The token can be created using any certified JWT library.

5. POST the redirect to PPM request endpoint:

   ```
    https://authenticator.pingone.com/registration/webauthn
   ```

   Pass the following HTTP parameters in the POST request:

| Parameter    | Description                                                                                                                                                            |
| ------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| orgUuid      | The unique ID of the local instance that enables PingID to identify the tenant instance in its services. Its value is the org\_alias from the organization's settings. |
| ppm\_request | The signed JWT.                                                                                                                                                        |

The authentication response will be passed to the address in the return URL which is defined in the request object.

The PPM response will return either a successful authentication status, or one of the following error codes in the case of a failure:

| Error code              | Description                                                       |
| ----------------------- | ----------------------------------------------------------------- |
| BROWSER\_NOT\_SUPPORTED | The web browser is not supported for WebAuthn operations.         |
| INVALID\_PPM            | The request payload sent in the PPM request is not valid.         |
| MAX\_DEVICES            | The maximum number of permitted paired devices has been exceeded. |

**Response payload parameters**

PPM success response JSON structure example:

```json
{
  "iss": "md",
  "sub": "username6",
  "aud": "PingFed",
  "nonce": "whPAxcspnuBDIt6EhSq9",
  "exp": 1573128721,
  "iat": 1573128691,
  "status": "success",
  "idpAccountId": "4bc336c9-a8fa-44d0-ac8c-7bf042e064ea",
  "authnContext": "urn:oasis:names:tc:SAML:2.0:ac:classes:Telephony",
  "inResponseTo": "",
  "dst": "http://httpbin.org/post"
}
```

PPM failure response JSON structure example:

```json
{
  "iss": "md",
  "sub": "username6",
  "aud": "PingFed",
  "nonce": "whPAxcspnuBDIt6EhSq9",
  "exp": 1573128941,
  "iat": 1573128911,
  "status": "failure",
  "idpAccountId": "4bc336c9-a8fa-44d0-ac8c-7bf042e064ea",
  "authnContext": "urn:oasis:names:tc:SAML:2.0:ac:classes:Telephony",
  "inResponseTo": "",
  "errorCode": "BROWSER_NOT_SUPPORTED",
  "message": "Browser does not support selected registration method",
  "dst": "http://httpbin.org/post"
}
```

The parameters included in the response payload object are:

| Parameter    | Description                                                                                                                                                                                                                                                              |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| iss          | The module where the authentication occurred. This is the value of the request's aud parameter.                                                                                                                                                                          |
| idpAccountId | CAS account id. The unique ID of the local instance, to enable PingID to identify the tenant instance in its services. This is the value of the request's iss parameter.                                                                                                 |
| sub          | The PingOne system-level username. This is the value of the sub parameter in the request.                                                                                                                                                                                |
| aud          | The application to return to. This is the value of the request's iss parameter.                                                                                                                                                                                          |
| nonce        | The value that was provided for the *nonce* parameter in the request.\<br>\_Note: In some cases of request failure, the response will not include a value for the nonce parameter even though it was provided in the request. Your code should take this into account.\_ |
| iat          | The response's "issued at" epoch time.                                                                                                                                                                                                                                   |
| exp          | The response's expiration epoch time.                                                                                                                                                                                                                                    |
| jti          | Newly generated random unique ID.                                                                                                                                                                                                                                        |
| status       | The status of the authentication operation: success or failure.                                                                                                                                                                                                          |
| inResponseTo | The tracking ID, passed from the request's jti field.                                                                                                                                                                                                                    |
| dst          | The destination URL. This is the value of the request's returnUrl parameter.                                                                                                                                                                                             |
| errorCode    | The error status code resulting in the event of a failed transaction.                                                                                                                                                                                                    |
| message      | The error message resulting in the event of a failed transaction.                                                                                                                                                                                                        |
| authnContext | The authentication context URI. For example, "urn:oasis:names:tc:SAML:2.0:ac:classes:Telephony".                                                                                                                                                                         |

### Example PPM request for FIDO authentication with a hybrid UI

The following steps illustrate the PPM request workflow for FIDO authentication with a hybrid UI.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The purpose of this example is to test authentication for an instance of a FIDO device that was paired with a hybrid UI. This specific example does not include authentication policy processing, and should be used only for internal testing purposes. Follow the instructions of the [PPM request workflow](#ppm-request-workflow) and its [Example PPM request](#example-ppm-request), for implementation of comprehensive authentication. |

1. Verify that the browser supports WebAuthn authentication.

   a) For FIDO security key:

   ```javascript
    window.IsWebAuthnSupported = function IsWebAuthnSupported() {
        if (!window.PublicKeyCredential) {
            console.log("Web Authentication API is not supported on this browser.");
            return false;
        }
        return true;
    }
   ```

   b) For FIDO biometrics:

   ```javascript
    window.IsWebAuthnSupported = function IsWebAuthnSupported() {
        if (!window.PublicKeyCredential) {
            console.log("Web Authentication API is not supported on this browser.");
            return false;
        }
        return true;
    }
    window.isWebAuthnPlatformAuthenticatorAvailable = function isWebAuthnPlatformAuthenticatorAvailable() {
        var timer;
        var p1 = new Promise(function(resolve) {
            timer = setTimeout(function() {
                console.log("isWebAuthnPlatformAuthenticatorAvailable - Timeout");
                resolve(false);
            }, 1000);
        });
        var p2 = new Promise(function(resolve) {
            if (IsWebAuthnSupported() && window.PublicKeyCredential.isUserVerifyingPlatformAuthenticatorAvailable) {
                resolve(
                    window.PublicKeyCredential.isUserVerifyingPlatformAuthenticatorAvailable().catch(function(err) {
                        console.log(err);
                        return false;
                    }));
            }
            else {
                resolve(false);
            }
        });
        return Promise.race([p1, p2]).then(function (res) {
            clearTimeout(timer);
            console.log("isWebAuthnPlatformAuthenticatorAvailable - " +  res);
            return res;
        });
    }
   ```

2. Populate the PPM request with all mandatory values.

   **Request payload parameters**

   Example request payload object:

   ```json
    {
      "iss": "PingFed",
      "sub": "username",
      "aud": "pingidauthenticator",
      "nonce": "whPAxcspnuBDIt6EhSq9",
      "exp": 1573130051,
      "iat": 1573128251,
      "jti": "",
      "idpAccountId": "a3407e72-71af-4831-a6a1-37e5e94fc07d",
      "attributes": [
        {
            "name": "pingidSpAlias",
            "value": "web"
         },
         {
            "name": "webAuthnDeviceId",
            "value": "939033434233545000"
         }
      ],
      "returnUrl": "http://httpbin.org/post"
    }
   ```

   The parameters included in the request payload:

   | Parameter    | Description                                                                                                                                                                                                                              |
   | ------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | idpAccountId | CAS account ID. The unique ID of the local instance that enables PingID to identify the tenant instance in its services. Its value is the org\_alias from the organization's settings.                                                   |
   | iss          | Issuer (sender) of the request, for example "PingFed".                                                                                                                                                                                   |
   | sub          | The PingOne system-level username.                                                                                                                                                                                                       |
   | aud          | The destination application that the request should go to, which is the MFA authenticating app. For example, "pingidauthenticator".                                                                                                      |
   | returnUrl    | The URL that the PPM response will be directed to.                                                                                                                                                                                       |
   | nonce        | A random unique request ID used to associate a client session with an authentication response, and to mitigate replay attacks. The value is passed without modification, from the authentication request to the authentication response. |
   | iat          | The request's "issued at" epoch time.                                                                                                                                                                                                    |
   | exp          | The request's expiration epoch time.                                                                                                                                                                                                     |
   | jti          | Optional. The JWT ID or token ID (tracking ID).                                                                                                                                                                                          |
   | idpEntityId  | Optional. Reserved for future use.                                                                                                                                                                                                       |
   | dst          | Optional. The URL of the intended destination of the request. Intended for matching server and destination content.                                                                                                                      |
   | attributes   | Optional. Contains a list of PPMAttribute elements, where PPMAttribute is a simple object comprising a name and value pair.                                                                                                              |

3. Populate the PPM request with the additional pingidSpAlias and webAuthnDeviceId attributes (in the request's "attributes" object), required for the hybrid use case.

   | Parameter        | Description                                                           |
   | ---------------- | --------------------------------------------------------------------- |
   | pingidSpAlias    | Set this parameter's value to "web" to indicate a web authentication. |
   | webAuthnDeviceId | Specify the FIDO device that will perform the authentication.         |

4. Sign the request's JSON representation. Signing is mandatory, to ensure the request's reliability.

   The signature requires:

   * The relevant organization base64 secret key from the PingOne client integration settings file.

   * The signing algorithm.

   The token can be created using any certified JWT library.

5. POST the redirect to PPM request endpoint:

   ```
    https://authenticator.pingone.com/pingid/ppm/hybrid/webauthn/auth
   ```

   Pass the following HTTP parameters in the POST request:

| Parameter        | Description                                                                                                                                                            |
| ---------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| idp\_account\_id | The unique ID of the local instance that enables PingID to identify the tenant instance in its services. Its value is the org\_alias from the organization's settings. |
| ppm\_request     | The signed JWT.                                                                                                                                                        |
| iss              | Issuer (sender) of the request, for example "PingFed".                                                                                                                 |

The authentication response will be passed to the address in the return URL which is defined in the request object.

The PPM response will return either a successful authentication status, or one of the following error codes in the case of a failure:

| Error code              | Description                                                                                                             |
| ----------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| ABORT\_ERROR            | The authentication was canceled.                                                                                        |
| AUTH\_GENERIC\_ERROR    | Error occurred during authentication with PingID. Try again.                                                            |
| BROWSER\_NOT\_SUPPORTED | This browser doesn't support your current authentication method. Try a different browser or contact your administrator. |
| INVALID\_PPM            | PPM request is invalid.\<br>PPM request has expired.                                                                    |
| INVALID\_STATE\_ERROR   | We didn't recognize the security key you used. Try again with the correct key.                                          |
| NOT\_ALLOWED\_ERROR     | The authentication was canceled.                                                                                        |
| SECURITY\_ERROR         | You have been blocked due to an attempted security violation. Contact your administrator for more information.          |
| USER\_DOES\_NOT\_EXIST  | User does not exist.                                                                                                    |

**Response payload parameters**

PPM success response JSON structure example:

```json
{
  "iss": "pingidauthenticator",
  "sub": "username6",
  "aud": "PingFed",
  "nonce": "whPAxcspnuBDIt6EhSq9",
  "exp": 1573128721,
  "iat": 1573128691,
  "status": "success",
  "idpAccountId": "4bc336c9-a8fa-44d0-ac8c-7bf042e064ea",
  "authnContext": "urn:oasis:names:tc:SAML:2.0:ac:classes:Telephony",
  "inResponseTo": "",
  "dst": "http://httpbin.org/post"
}
```

PPM failure response JSON structure example:

```json
{
  "iss": "pingidauthenticator",
  "sub": "username6",
  "aud": "PingFed",
  "nonce": "whPAxcspnuBDIt6EhSq9",
  "exp": 1573128941,
  "iat": 1573128911,
  "status": "failure",
  "idpAccountId": "4bc336c9-a8fa-44d0-ac8c-7bf042e064ea",
  "authnContext": "urn:oasis:names:tc:SAML:2.0:ac:classes:Telephony",
  "inResponseTo": "",
  "errorCode": "BROWSER_NOT_SUPPORTED",
  "message": "This browser doesn't support your current authentication method. Try a different browser or contact your administrator.",
  "dst": "http://httpbin.org/post"
}
```

The parameters included in the response payload object are:

| Parameter    | Description                                                                                                                                                                                                                                                              |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| iss          | The module where the authentication occurred. This is the value of the request's aud parameter.                                                                                                                                                                          |
| idpAccountId | CAS account id. The unique ID of the local instance, to enable PingID to identify the tenant instance in its services. This is the value of the request's iss parameter.                                                                                                 |
| sub          | The PingOne system-level username. This is the value of the sub parameter in the request.                                                                                                                                                                                |
| aud          | The application to return to. This is the value of the request's iss parameter.                                                                                                                                                                                          |
| nonce        | The value that was provided for the *nonce* parameter in the request.\<br>\_Note: In some cases of request failure, the response will not include a value for the nonce parameter even though it was provided in the request. Your code should take this into account.\_ |
| iat          | The response's "issued at" epoch time.                                                                                                                                                                                                                                   |
| exp          | The response's expiration epoch time.                                                                                                                                                                                                                                    |
| jti          | Newly generated random unique ID.                                                                                                                                                                                                                                        |
| status       | The status of the authentication operation: success or failure.                                                                                                                                                                                                          |
| inResponseTo | The tracking ID, passed from the request's jti field.                                                                                                                                                                                                                    |
| dst          | The destination URL. This is the value of the request's returnUrl parameter.                                                                                                                                                                                             |
| errorCode    | The error status code resulting in the event of a failed transaction.                                                                                                                                                                                                    |
| message      | The error message resulting in the event of a failed transaction.                                                                                                                                                                                                        |
| authnContext | The authentication context URI. For example, "urn:oasis:names:tc:SAML:2.0:ac:classes:Telephony".                                                                                                                                                                         |