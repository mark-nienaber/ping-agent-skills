---
title: "Example: PingID FIDO security key"
description: The examples on this page present the steps comprising the following FIDO security key flows:
component: pingid-api
page_id: pingid-api::pid_c_PingIDapiExampleFIDOsecurityKey
canonical_url: https://developer.pingidentity.com/pingid-api/pid_c_PingIDapiExampleFIDOsecurityKey.html
section_ids:
  overview: Overview
  fido-security-key-pairing-flow: FIDO security key pairing flow
  fido-security-key-authentication-flow: FIDO security key authentication flow
---

# Example: PingID FIDO security key

## Overview

The examples on this page present the steps comprising the following FIDO security key flows:

1. Pairing a user's FIDO security key to their profile using the WebAuthn pairing process.

2. Authentication using a FIDO security key.

For information on WebAuthn, refer to the World Wide Web Consortium (W3C) WebAuthn reference <https://www.w3.org/TR/webauthn/>.

For further sample WebAuthn registration and authentication scenarios refer to the W3C WebAuthn scenarios reference <https://www.w3.org/TR/webauthn/#sample-scenarios>.

## FIDO security key pairing flow

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
        "webauthnType": "WebAuthn",
        "name": "User1",
        "displayName": "User1@pingidentity.com"
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

    window.WebAuthnRegistration = function WebAuthnRegistration(publicKeyCredentialCreationOptions) {
        return new Promise(function(resolve, reject) {
            if (!IsWebAuthnSupported()) {
                reject(Error("UnSupportedBrowserError"));
            }
            resolve(Register(publicKeyCredentialCreationOptions));
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

## FIDO security key authentication flow

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
          "isWebAuthnSupportedByBrowser": "true"
          }
      }
   ```

   The StartAuthentication API acts as a flow manager. It checks policies and other factors, and returns a status (errorId 30011) to indicate that the FIDO security key must be used. For example:

   ```json
    "responseBody": {
        "multipleDevicesEnabled": true,
        "userDevices": [
          {
            "enrollment": "2019-02-13 08:39:51.333",
            "sentNotClaimedSms": -1,
            "sentClaimedSms": -1,
            "availableNotClaimedSms": 0,
            "availableClaimedSms": 0,
            "pushEnabled": false,
            "displayID": null,
            "deviceUuid": "0f0eaf16-bc75-b440-0f0e-af16bc75b440",
            "deviceId": 1084997072428840000,
            "countryCode": null,
            "phoneNumber": null,
            "deviceModel": null,
            "appVersion": null,
            "email": null,
            "deviceRole": "PRIMARY",
            "hasWatch": false,
            "nickname": "Security Key 1",
            "osVersion": null,
            "type": "Security Key"
          }
        ],
        "extendedAuthenticationDetails": {
          "adminHelp": "<p style=&quot;color:blue;&quot;></p>",
          "lastSuccessfulLogin": null,
          "gracePeriod": 1504083908422
        },
        "localFallbackDeviceList": null,
        "allowedAuthenticationMethods": null,
        "cookie": null,
        "errorParams": null,
        "authenticatingDeviceId": "0f0eaf16-bc75-b440-0f0e-af16bc75b440",
        "sessionId": "webs_SA87Pd4qhAY6JM-ULRE7-yX-zlPvsQfN3bRzMEB86Gw",
        "errorId": 30011,
        "errorMsg": "webauthn.flow",
        "uniqueMsgId": "webs_SA87Pd4qhAY6JM-ULRE7-yX-zlPvsQfN3bRzMEB86Gw",
        "clientData": null
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
        "deviceUuid": "0f0eaf16-bc75-b440-0f0e-af16bc75b440",
        "webauthnType: "WebAuthn"
      }
   ```

   The WebAuthnStartAuth API call returns the response body, similar to the following example:

   ```json
    "responseBody": {
        "publicKeyCredentialOptions": "{\"challenge\":[-105,12,-73,3,-45,-70,59,120,30,100,-65,1,-119,49,61,126,-64,112,-29,-62,-113,87,51,70,-43,20,-8,-104,70,-8,-26,81],\"timeout\":120000,\"rpId\":\"pingone.com\",\"allowCredentials\":[{\"type\":\"public-key\",\"id\":[-108,35,43,99,-118,85,-65,-100,-121,97,-48,-100,-94,67,-35,15,-29,20,-3,-115,13,26,36,14,118,43,34,-53,-6,-59,-124,44,-58,60,-3,3,-19,-91,75,-46,112,-20,-109,121,-111,-80,-17,-64,0,63,-9,65,-87,-105,87,22,33,91,-107,-63,43,29,58,-20]}],\"userVerification\":\"preferred\"}",
        "sessionId": "a6b4ee5f-fbe0-403b-838a-4bb6b0520485",
        "errorId": 200,
        "errorMsg": "",
        "uniqueMsgId": "webs_-uD8DyzzMPORJWbF-M3PZxW1wrSAF-swE3pMjwGlj8k",
       "clientData": null
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

    window.WebAuthnAuthentication = function WebAuthnAuthentication(publicKeyCredentialRequestOptions) {
        return new Promise(function(resolve, reject) {
            if (IsWebAuthnSupported()) {
                resolve(Authenticate(publicKeyCredentialRequestOptions));
            }
            reject(Error("UnSupportedBrowserError"));
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
        "otp": "{\"id\":\"NclJtG2xeNiqDcvPCvjyipoyk7g4lYLSjuGfXefX-4eIAaxF9BRyVQROHJMWU9F9FuqAlbKvw1L0i-Zq2aYSCw\",\"rawId\":\"NclJtG2xeNiqDcvPCvjyipoyk7g4lYLSjuGfXefX 4eIAaxF9BRyVQROHJMWU9F9FuqAlbKvw1L0i Zq2aYSCw==\",\"type\":\"public-key\",\"response\":{\"clientDataJSON\":\"eyJjaGFsbGVuZ2UiOiIyNzU5eTE3WG51eW82dnJMazNpdDNuT3pMYkw4RmF0eFV1Y2RrVWREb1RZIiwib3JpZ2luIjoiaHR0cDovL2xvY2FsaG9zdDo4MDgwIiwidHlwZSI6IndlYmF1dGhuLmdldCJ9\",\"authenticatorData\":\"SZYN5YgOjGh0NBcPZHZgW4/krrmihjLHmVzzuoMdl2MBAAABOg==\",\"signature\":[48,69,2,33,0,188,55,238,55,35,174,165,142,28,249,147,76,141,98,81,230,248,204,205,186,5,14,32,145,119,9,88,102,28,48,194,177,2,32,44,3,86,43,30,135,43,92,223,227,183,19,157,170,192,91,37,188,54,137,45,23,155,196,225,19,127,103,83,149,122,61],\"userHandle\":\"\"}}",
        "sessionId": "webs_SA87Pd4qhAY6JM-ULRE7-yX-zlPvsQfN3bRzMEB86Gw",
        "formParameters": {
            "origin": "https://admin.pingone.com",
            "rpId": "pingone.com",
            "authWebauthnSessionId": "a6b4ee5f-fbe0-403b-838a-4bb6b0520485"
             }
      }
   ```