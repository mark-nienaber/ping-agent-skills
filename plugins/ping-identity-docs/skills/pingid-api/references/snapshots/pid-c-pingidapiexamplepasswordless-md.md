---
title: "Example: PingID FIDO passwordless Authentication"
description: "The examples on this page present the steps comprising passwordless authentication flows, with configurations where application policies are evaluated (when the admin has configured enforcePolicy = \"true\"), and without policy evaluation (when the admin has configured enforcePolicy = \"false\")."
component: pingid-api
page_id: pingid-api::pid_c_PingIDapiExamplePasswordless
canonical_url: https://developer.pingidentity.com/pingid-api/pid_c_PingIDapiExamplePasswordless.html
section_ids:
  overview: Overview
  fido-passwordless-authentication-flow: FIDO passwordless authentication flow
---

# Example: PingID FIDO passwordless Authentication

## Overview

The examples on this page present the steps comprising passwordless authentication flows, with configurations where application policies are evaluated (when the admin has configured **enforcePolicy** = "**true**"), and without policy evaluation (when the admin has configured **enforcePolicy** = "**false**").

## FIDO passwordless authentication flow

The passwordless authentication process using the PingID APIs requires the following flow:

1. Initiate the authentication process using the StartWebAuthnPasswordlessAuth API. For example:

   ```
    https://idpxnyl3m.pingidentity.com/pingid/rest/4/startwebauthnpasswordlessauth/do
   ```

   Request Body Parameters:

   ```json
    "reqBody": {
      "rpId": "pingone.com",
      "origin": "https://admin.pingone.com",
      "spAlias": "web"
    }
   ```

   The StartWebAuthnPasswordlessAuth API acts as a flow manager. It returns the publicKeyCredentialOptions required in the next step. For example:

   ```json
    {
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
    }
   ```

2. Call the navigator.credentials.get method using the publicKeyCredentialOptions returned from the StartWebAuthnPasswordlessAuth API in the previous step. As an example, refer to the following code sample:

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

    function toBase64Str(bin){
        return btoa(String.fromCharCode.apply(null, new Uint8Array(bin)));
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
   ```

3. Complete the authentication process, using the FinishWebAuthnPasswordlessAuth API. The FinishWebAuthnPasswordlessAuth API's publicKeyCredentialJson parameter must be assigned the value returned in the publicKeyCredential parameter of the navigator.credentials.get function of the previous step. For example:

   ```
    https://idpxnyl3m.pingidentity.com/pingid/rest/4/finishwebauthnpasswordlessauth/do
   ```

   Request Body Parameters:

   ```json
    "reqBody": {
        "publicKeyCredentialJson": "<returned from navigator.credentials.get>",
        "sessionId": "webs_btwh200zYkv1LfUAvmc1MIJWzGXjS4jPTr2saKcOcuA"
     }
   ```

   If FinishWebAuthnPasswordlessAuth returns the status `errorId=200`, the passwordless flow ends. This indicates that the admin has set the **enforcePolicy** parameter to "**false**".

   If FinishWebAuthnPasswordlessAuth returns the status `errorId=30014`, it indicates that the admin has set the **enforcePolicy** parameter to "**true**". In this case, the StartAuthentication API must be run with the relevant "**memberOf**" group parameter, to complete the authentication flow. For example:

   ```json
    "reqBody": {
      "spAlias": "web",
      "userName": "marcher",
     "sessionId":"webs_btwh200zYkv1LfUAvmc1MIJWzGXjS4jPTr2saKcOcuA",
      "clientData": "Session data echoed back to the requestor",
      "enforcePolicy": "true",
      "ipAddr": "103.25.46.58",
      "application": "google.com",
      "reqDevFP": "\{User-Agent=\"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36\"}",
      "memberOf": ["CN=aliceA,OU=US,OU=Americas,DC=net","CN=bobB,OU=EU,OU=England,DC=net"],
        "formParameters": {
            "isWebAuthnSupportedByBrowser": "true",
            "isWebAuthnPlatformAuthenticatorAvailable": "true"}
    }
   ```
