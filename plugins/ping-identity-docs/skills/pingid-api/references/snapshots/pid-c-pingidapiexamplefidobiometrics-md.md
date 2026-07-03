---
title: "Example: PingID FIDO biometrics"
description: The examples on this page present the steps comprising the following FIDO biometrics flows:
component: pingid-api
page_id: pingid-api::pid_c_PingIDapiExampleFIDObiometrics
canonical_url: https://developer.pingidentity.com/pingid-api/pid_c_PingIDapiExampleFIDObiometrics.html
section_ids:
  overview: Overview
  fido-biometrics-pairing-flow: FIDO biometrics pairing flow
  fido-biometrics-authentication-flow: FIDO biometrics authentication flow
---

# Example: PingID FIDO biometrics

## Overview

The examples on this page present the steps comprising the following FIDO biometrics flows:

1. Pairing a user's FIDO biometrics device to their profile using the WebAuthn pairing process.

2. Authentication using FIDO biometrics.

For information on WebAuthn, refer to the World Wide Web Consortium (W3C) WebAuthn reference <https://www.w3.org/TR/webauthn/>.\
For further sample WebAuthn registration and authentication scenarios refer to the W3C WebAuthn scenarios reference <https://www.w3.org/TR/webauthn/#sample-scenarios>.

## FIDO biometrics pairing flow

The WebAuthn pairing process using the PingID APIs requires the following flow:

1. Initiate the pairing process using the WebAuthnStartPairing API. For example:

   ```
    https://idpxnyl3m.pingidentity.com/pingid/rest/4/webauthnstartpairing/do
   ```

   Request Body Parameters:

   ```json
    "reqBody": {
        "rpId": "pingone.com",
        "rpName": "PingID Web Authentication",
        "userName": "fidouser1",
        "webauthnType": "webauthn_platform"
      }
   ```

   The API call returns the response body, similar to the following example:

   ```json
    {
      "responseBody": {
        "publicKeyCredentialOptions": "<publicKeyCredentialOptions >",
        "sessionId": "b6367b8e-1da8-490d-9c6d-6814cb2cfc81",
        "errorMsg": "",
        "errorId": 200,
        "uniqueMsgId": "webs_0vntDNAOWRwTL1W5_RbsNzuol1lu0eKfzRSJeC86QKM",
        "clientData": null
      }
    }
   ```

2. Call the navigator.credentials.create method using the publicKeyCredentialOptions returned from the WebAuthnStartPairing API, per the WebAuthnRegistration function in the following code sample:

   ```javascript
    var authAbortController = window.PublicKeyCredential ? new AbortController() : null;
    var authAbortSignal = window.PublicKeyCredential ? authAbortController.signal : null;

    window.abortWebAuthnSignal = function abortWebAuthnSignal() {
        authAbortController.abort();
        authAbortController = new AbortController();
        authAbortSignal = authAbortController.signal;
    }

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

    window.WebAuthnPlatformRegistration = function WebAuthnPlatformRegistration(publicKeyCredentialCreationOptions) {
        return new Promise(function(resolve, reject) {
            isWebAuthnPlatformAuthenticatorAvailable().then(function (result) {
                if (result) {
                    resolve(Register(publicKeyCredentialCreationOptions));
                }
                reject(Error("UnSupportedBrowserError"));
            });
        });
    }

    function Register(publicKeyCredentialCreationOptions) {
        return new Promise(function(resolve, reject) {
            var options = JSON.parse(publicKeyCredentialCreationOptions);
            var publicKeyCredential = {};
            publicKeyCredential.rp = options.rp;
            publicKeyCredential.user = options.user;
            publicKeyCredential.user.id = new Uint8Array(options.user.id);
            publicKeyCredential.challenge = new Uint8Array(options.challenge);
            publicKeyCredential.pubKeyCredParams = options.pubKeyCredParams;
            // Optional parameters
            if ('timeout' in options) {
                publicKeyCredential.timeout = options.timeout;
            }
            if ('excludeCredentials' in options) {
                publicKeyCredential.excludeCredentials = credentialListConversion(options.excludeCredentials);
            }
            if ('authenticatorSelection' in options) {
                publicKeyCredential.authenticatorSelection = options.authenticatorSelection;
            }
            if ('attestation' in options) {
                publicKeyCredential.attestation = options.attestation;
            }
            if ('extensions' in options) {
                publicKeyCredential.extensions = options.extensions;
            }
            console.log(publicKeyCredential);
            navigator.credentials.create({"publicKey": publicKeyCredential, "signal": authAbortSignal})
                .then(function (newCredentialInfo) {
                    // Send new credential info to server for verification and registration.
                    console.log(newCredentialInfo);
                    var publicKeyCredential = {};
                    if ('id' in newCredentialInfo) {
                        publicKeyCredential.id = newCredentialInfo.id;
                    }
                    if ('type' in newCredentialInfo) {
                        publicKeyCredential.type = newCredentialInfo.type;
                    }
                    if ('rawId' in newCredentialInfo) {
                        publicKeyCredential.rawId = toBase64Str(newCredentialInfo.rawId);
                    }
                    if (!newCredentialInfo.response) {
                        throw "Missing 'response' attribute in credential response";
                    }
                    var response = {};
                    response.clientDataJSON = toBase64Str(newCredentialInfo.response.clientDataJSON);
                    response.attestationObject = toBase64Str(newCredentialInfo.response.attestationObject);
                    publicKeyCredential.response = response;
                    resolve(JSON.stringify(publicKeyCredential));
                }).catch(function (err) {
                    // No acceptable authenticator or user refused consent. Handle appropriately.
                    console.log(err);
                    reject(Error(err.name));
            });
        });
    }

    function credentialListConversion(list) {
        var credList = [];
        for (var i=0; i < list.length; i++) {
            var cred = {
                type: list[i].type,
                id: new Uint8Array(list[i].id)
            };
            if (list[i].transports) {
                cred.transports = list[i].transports;
            }
            credList.push(cred);
        }
        return credList;
    }

    function toBase64Str(bin){
        return btoa(String.fromCharCode.apply(null, new Uint8Array(bin)));
    }
   ```

3. Complete the pairing process, using the WebAuthnFinishPairing API. The publicKeyCredentialJson parameter must be assigned the value returned from the navigator.credentials.create function of the previous step (publicKeyCredential from the code example above). For example:

   ```
    https://idpxnyl3m.pingidentity.com/pingid/rest/4/webauthnfinishpairing/do
   ```

   Request Body Parameters:

   ```json
        "reqBody": {
            "rpId": "pingone.com",
            "sessionId": "b6367b8e-1da8-490d-9c6d-6814cb2cfc81",
            "userName": "fidouser1",
            "origin": "https://admin.pingone.com",
            "publicKeyCredentialJson": "<output returned from navigator.credentials.create  function>"
          }
   ```

## FIDO biometrics authentication flow

The WebAuthn authentication process using the PingID APIs requires the following flow:

1. Initiate the authentication process using the StartAuthentication API. For example:

   ```
    https://idpxnyl3m.pingidentity.com/pingid/rest/4/startauthentication/do
   ```

   Request Body Parameters:

   ```json
    "reqBody": {
      "spAlias": "web",
      "userName": "fidouser1",
      "deviceId": 1084997072428840000,
      "formParameters": {
          "isWebAuthnSupportedByBrowser": "true",
          "isWebAuthnPlatformAuthenticatorAvailable": "true"
          }
      }
   ```

   The StartAuthentication API acts as a flow manager. It checks policies and other factors, and returns a status (errorId 30013) to indicate that the FIDO biometrics device must be used. For example:

   ```json
    {
      "responseBody": {
        "clientData": null,
        "errorId": 30013,
        "errorMsg": "webauthn.platform.flow",
        "sessionId": "webs_ohi_90P-I1eISGQJbnI82BHjd03y9NodA6ki_Z1v0t17ZX0",
        "cookie": null,
        "errorParams": null,
        "authenticatingDeviceId": "16e3f7de-f6af-9cf0-16e3-f7def6af9cf0",
        "localFallbackDeviceList": null,
        "allowedAuthenticationMethods": null,
        "excludeAuthenticationMethods": [
          "RESCUE"
        ],
        "extendedAuthenticationDetails": {
          "lastSuccessfulLogin": null,
          "gracePeriod": 1504083908422,
          "adminHelp": "<p style=&quot;color:blue;&quot;></p>"
        },
        "userDevices": [
          {
            "type": "FIDO2 Biometrics",
            "osVersion": null,
            "appVersion": null,
            "enrollment": "2019-06-27 06:00:02.469",
            "phoneNumber": null,
            "countryCode": null,
            "sentNotClaimedSms": -1,
            "sentClaimedSms": -1,
            "availableNotClaimedSms": 0,
            "availableClaimedSms": 0,
            "pushEnabled": false,
            "email": null,
            "deviceId": 1084997072428840000,
            "deviceUuid": "16e3f7de-f6af-9cf0-16e3-f7def6af9cf0",
            "deviceRole": "PRIMARY",
            "nickname": "Windows Hello 1",
            "deviceModel": null,
            "displayID": "webauthn_platform_windows",
            "hasWatch": false
          }
        ],
        "multipleDevicesEnabled": true,
        "uniqueMsgId": "webs_ohi_90P-I1eISGQJbnI82BHjd03y9NodA6ki_Z1v0t17ZX0"
      }
    }
   ```

2. Invoke the WebAuthnStartAuth API. For example:

   ```
    https://idpxnyl3m.pingidentity.com/pingid/rest/4/webauthnstartauth/do
   ```

   Request Body Parameters:

   ```json
    "reqBody": {
        "rpId": "pingone.com",
        "userName": "fidouser1",
        "deviceUuid": "16e3f7de-f6af-9cf0-16e3-f7def6af9cf0",
        "webauthnType: "webauthn_platform"
      }
   ```

   The WebAuthnStartAuth API call returns the response body, similar to the following example:

   ```json
    {
      "responseBody": {
        "clientData": null,
        "errorId": 200,
        "errorMsg": "",
        "sessionId": "abec8ed8-13fc-4c49-a157-9db1ffaf74f4",
        "publicKeyCredentialOptions": "{\"challenge\":[-22,-63,-8,98,-35,-54,92,-25,-13,-76,-51,86,-120,63,-11,89,45,-20,86,-63,114,-65,26,34,13,-84,-4,112,-110,66,-12,-31],\"timeout\":120000,\"rpId\":\"pingone.com\",\"allowCredentials\":[{\"type\":\"public-key\",\"id\":[11,35,-62,-60,-118,-97,126,80,17,121,-30,-50,122,8,-42,-87,-123,56,29,106,90,68,57,-99,-108,13,45,93,11,-13,80,54],\"transports\":[\"internal\"]}],\"userVerification\":\"preferred\"}",
        "uniqueMsgId": "webs_ohi_slDY5XVgotezgpFMNlCIW7NtLvLrWxVo8gFCe14AXw4"
      }
    }
   ```

3. Call the navigator.credentials.get method using the publicKeyCredentialOptions returned from the WebAuthnStartAuth API in the previous step. As an example, refer to the WebAuthnAuthentication function in the following code sample:

   ```javascript
    var authAbortController = window.PublicKeyCredential ? new AbortController() : null;
    var authAbortSignal = window.PublicKeyCredential ? authAbortController.signal : null;

    window.abortWebAuthnSignal = function abortWebAuthnSignal() {
        authAbortController.abort();
        authAbortController = new AbortController();
        authAbortSignal = authAbortController.signal;
    }

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

    window.WebAuthnPlatformAuthentication = function WebAuthnPlatformAuthentication(publicKeyCredentialRequestOptions) {
        return new Promise(function(resolve, reject) {
            isWebAuthnPlatformAuthenticatorAvailable().then(function (result) {
                if (result) {
                    resolve(Authenticate(publicKeyCredentialRequestOptions));
                }
                reject(Error("UnSupportedBrowserError"));
            });
        });
    }

    function Authenticate(publicKeyCredentialRequestOptions) {
        return new Promise(function(resolve, reject) {
            var options = JSON.parse(publicKeyCredentialRequestOptions);
            var publicKeyCredential = {};
            publicKeyCredential.challenge = new Uint8Array(options.challenge);
            if ('allowCredentials' in options) {
                publicKeyCredential.allowCredentials = credentialListConversion(options.allowCredentials);
            }
            if ('rpId' in options) {
                publicKeyCredential.rpId = options.rpId;
            }
            if ('timeout' in options) {
                publicKeyCredential.timeout = options.timeout;
            }
            if ('userVerification' in options) {
                publicKeyCredential.userVerification = options.userVerification;
            }
            console.log(publicKeyCredential);
            navigator.credentials.get({"publicKey": publicKeyCredential})
                .then(function (assertion) {
                    // Send new credential info to server for verification and registration.
                    console.log(assertion);
                    var publicKeyCredential = {};
                    if ('id' in assertion) {
                        publicKeyCredential.id = assertion.id;
                    }
                    if ('rawId' in assertion) {
                        publicKeyCredential.rawId = toBase64Str(assertion.rawId);
                    }
                    if ('type' in assertion) {
                        publicKeyCredential.type = assertion.type;
                    }
                    var response = {};
                    response.clientDataJSON = toBase64Str(assertion.response.clientDataJSON);
                    response.authenticatorData = toBase64Str(assertion.response.authenticatorData);
                    response.signature = toBase64Str(assertion.response.signature);
                    response.userHandle = toBase64Str(assertion.response.userHandle);
                    publicKeyCredential.response = response;
                    resolve(JSON.stringify(publicKeyCredential));
                }).catch(function (err) {
                // No acceptable authenticator or user refused consent. Handle appropriately.
                console.log(err);
                reject(Error(err.name));
            });
        });
    }

    function credentialListConversion(list) {
        var credList = [];
        for (var i=0; i < list.length; i++) {
            var cred = {
                type: list[i].type,
                id: new Uint8Array(list[i].id)
            };
            if (list[i].transports) {
                cred.transports = list[i].transports;
            }
            credList.push(cred);
        }
        return credList;
    }

    function toBase64Str(bin){
        return btoa(String.fromCharCode.apply(null, new Uint8Array(bin)));
    }
   ```

4. Complete the authentication process, using the AuthOffline API. The AuthOffline API's publicKeyCredentialJson parameter must be assigned the value returned in the publicKeyCredential parameter of the navigator.credentials.get function of the previous step. For example:

   ```
    https://idpxnyl3m.pingidentity.com/pingid/rest/4/authoffline/do
   ```

   Request Body Parameters:

   ```json
    "reqBody": {
    "spAlias": "web",
    "userName": "fidouser1",
    "otp": "<output from navigator.credentials.get function>",
    "sessionId": "webs_ohi_90P-I1eISGQJbnI82BHjd03y9NodA6ki_Z1v0t17ZX0",
    "formParameters": {
        "origin": "https://admin.pingone.com",
        "rpId": "pingone.com",
        "authWebauthnSessionId": "abec8ed8-13fc-4c49-a157-9db1ffaf74f4"
         }
     }
   ```
