---
title: Adding identifiers to authentication
description: "\"Shows how to add identifiers to a PingOne Recognize authentication operation for analytics, auditing, or telemetry purposes.\""
component: recognize
page_id: recognize:web-sdk:web-sdk-reference-authentication-identifiers
canonical_url: https://docs.pingidentity.com/recognize/web-sdk/web-sdk-reference-authentication-identifiers.html
llms_txt: https://docs.pingidentity.com/recognize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  adding-identifiers: Adding identifiers
  headless: Headless
  web-components: Web components
  retrieving-the-user-id: Retrieving the user ID
---

# Adding identifiers to authentication

The PingOne Recognize Web SDK can associate identifiers with authentication operations. This enables analytics, auditing, and orchestration.

This requires adding `OperationID` to the authentication event.

Once identifiers are enabled, use the Telemetry API to retrieve authentication event details.

## Adding identifiers

To enable authentication identifiers, add them to the authentication details, as shown in the following examples:

### Headless

For headless authentication, add the `OperationID` when opening the web socket:

```javascript
await openKeylessWebSocketConnection(sym, {
  ...,
  operation: {
    id: OPERATION_ID
  }
})
```

### Web components

For web components, add `operation-id` to the authentication component:

```html
<kl-auth
  ...
  operation-id="OPERATION_ID"
></kl-auth>
```

## Retrieving the user ID

To use the Telemetry API, you need the PingOne Recognize user ID associated with the authentication event. Use the Check Client Device API to retrieve the user ID associated with the device.

The Check Client Device API requires the following values:

|            |                                                                   |
| ---------- | ----------------------------------------------------------------- |
| Parameter  | Description                                                       |
| `api_key`  | PingOne Recognize API authorization key                           |
| `customer` | Name of the PingOne Recognize tenant associated with your account |
| `username` | Username defined during enrollment and later used to authenticate |

---

---
title: Authentication
description: "\"Shows how to authenticate (sign-on) a new user by comparing their current facial biometrics with the ones saved during PingOne Recognize enrollment.\""
component: recognize
page_id: recognize:web-sdk:web-sdk-guide-authentication
canonical_url: https://docs.pingidentity.com/recognize/web-sdk/web-sdk-guide-authentication.html
llms_txt: https://docs.pingidentity.com/recognize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  before-you-begin: Before you begin
  headless-integration: Headless integration
  web-component-integration: Web component integration
---

# Authentication

Authentication is the biometric equivalent of signing-on. PingOne Recognize compares the user's current facial biometrics with the ones saved during [enrollment](web-sdk-guide-enrollment.html).

If the biometrics match, PingOne Recognize authenticates the user.

## Before you begin

Make sure you have met the [prerequisite requirements](web-sdk-prerequisites.html) before continuing.

## Headless integration

The `@keyless/sdk-web` library lets you integrate the PingOne Recognize Web SDK without using UI controls. Here's an authentication example:

> **Collapse: Details**
>
> ```javascript
> import {
>   addKeylessEventListeners,
>   createKeylessAuth,
>   createKeylessMediaStream,
>   getKeylessCameraPermissionState,
>   getKeylessVideoMediaDevices,
>   getLastKeylessServerFrameTriggeredBiometricFilters,
>   getLastKeylessVideoFrameQuality,
>   importKeylessWebAssemblyModuleOrThrow,
>   isKeylessVideoMediaStreamAvailable,
>   KeylessError,
>   openKeylessWebSocketConnection,
>   reduceKeylessBiometricFiltersToTriggered,
>   removeKeylessEventListeners
> } from '@keyless/sdk-web'
>
> function requestTransactionJwtVerification(jwt) {}
> function requestUserCameraPermission() {}
>
> function handleCameraOperativityError(error) {}
> function handleImportKeylessWebAssemblyModuleError(error) {}
> function handleCreateKeylessMediaStreamError(error) {}
> function handleOpenKeylessWebSocketConnectionError(error) {}
>
> /**
>  * This event is fired when an error occurs during the authentication process.
>  * The error object contains a `message` property that indicates the type of error.
>  */
> function onKeylessError(sym, error) {
>   /**
>    * Removing event listeners is advised on terminal events since
>    * no more than one attempt is allowed per authentication symbol.
>    */
>   removeKeylessEventListeners(sym)
>
>   // will log the error code
>   console.error(error.message)
> }
>
> /**
>  * This event is fired when the authentication process is complete.
>  * It does not fire for failed attempts, only successful ones.
>  */
> function onKeylessFinished(sym, message) {
>   /**
>    * Removing event listeners is advised on terminal events since
>    * no more than one attempt is allowed per authentication symbol.
>    */
>   removeKeylessEventListeners(sym)
>
>   /**
>    * The `transactionJwt` is a JSON Web Token (JWT) that contains information
>    * about the authentication transaction.
>    *
>    * This token is signed by the Keyless Authentication Service and can be used
>    * to verify the authenticity of the transaction.
>    *
>    * This operation is strictly backend-to-backend and should never be performed
>    * in client-side code.
>    */
>   requestTransactionJwtVerification(message.transactionJwt)
> }
>
> /**
>  * This event is useful for providing real-time feedback to users during
>  * the authentication process, such as prompting them to adjust their position
>  * or lighting conditions to improve biometric recognition.
>  *
>  * The difference with "onKeylessVideoFrameQuality" is that this is from
>  * filters running on the server.
>  */
> function onKeylessFrameResults(sym, message) {
>   let filters
>
>   /**
>    * Returns an array of biometric filters that were triggered in the last frame.
>    * If no biometric filters were triggered, an empty array is returned.
>    */
>   filters = reduceKeylessBiometricFiltersToTriggered(message.filters)
>
>   /**
>    * Optionally, this function can be used to retrieve the filters that were triggered
>    * in the last frame.
>    *
>    * This can be useful if you need to access the last frame's triggered filters outside
>    * of the frame results event.
>    *
>    * If this function is used then this event is useful for requesting an update to the UI.
>    */
>   filters = getLastKeylessServerFrameTriggeredBiometricFilters(sym)}
>
> /**
>  * This event is useful for providing real-time feedback to users during
>  * the authentication process, such as prompting them to adjust their position
>  * or lighting conditions to improve biometric recognition.
>  *
>  * The difference with "onKeylessFrameResults" is that this is from filters
>  * running on the client.
>  */
> function onKeylessVideoFrameQuality(sym, event) {
>   /**
>    * Will log an array of filters that were triggered in this frame.
>    * If no biometric filters were triggered, an empty array is returned.
>    */
>   console.log(event.filters)
>
>   /**
>    * Optionally, this function can be used to retrieve the quality of the last
>    * video frame.
>    *
>    * This can be useful if you need to access the last video frame quality outside
>    * of the video frame quality event.
>    *
>    * If this function is used then this event is useful for requesting an update to the UI.
>    */
>   console.log(getLastKeylessVideoFrameQuality(sym))
> }
>
> async function ensureCameraOperativity() {
>   let devices, state
>
>   devices = await getKeylessVideoMediaDevices()
>
>   /**
>    * If the error is MEDIA_DEVICES_NO_VIDEO_INPUTS, it means that
>    * the user does not have any camera available.
>    */
>   if (devices instanceof Error && devices.message === KeylessError.MEDIA_DEVICES_NO_VIDEO_INPUTS) throw devices
>
>   state = await getKeylessCameraPermissionState()
>
>   /**
>    * If the camera permission state is not 'granted', request
>    * the user's device doesn't have a camera.
>    */
>   if (state !== 'granted') {
>     /**
>      * Ideally this function should take the user to a UI prompt
>      * where they can grant camera access to the website.
>      *
>      * The easiest way to trigger the browser's camera permission prompt
>      * is to call isKeylessVideoMediaStreamAvailable(), which will return
>      * a boolean indicating whether the user granted camera access or not.
>      */
>     requestUserCameraPermission()
>     throw new Error('camera permission state is not granted')
>   }
>
>   devices = await getKeylessVideoMediaDevices()
>
>   /**
>    * If the error is MEDIA_DEVICES_EMPTY_VIDEO_INPUT_LABEL, it means that
>    * even though the user has granted camera access, the browser requires
>    * the user to start a video stream to be able to read the camera labels.
>    *
>    * In this case, we perform a throwaway getUserMedia() request with
>    * isKeylessVideoMediaStreamAvailable() to start a video stream
>    * to be able to read the camera labels.
>    */
>   if (devices instanceof Error && devices.message === KeylessError.MEDIA_DEVICES_EMPTY_VIDEO_INPUT_LABEL) {
>     let available
>
>     available = await isKeylessVideoMediaStreamAvailable()
>     if (!available) throw new Error('video media stream is not available')
>
>     devices = await getKeylessVideoMediaDevices()
>   }
>
>   /**
>    * If we still have an error, throw an error to indicate that
>    * the media devices still could not be read correctly.
>    */
>   if (devices instanceof Error) throw devices
> }
>
> async function authenticateWithKeyless() {
>   let auth, options, stream, open
>
>   /**
>    * Create a Keyless authentication symbol.
>    *
>    * This symbol must be kept in memory for the duration of the authentication process.
>    * To perform multiple authentications, a new symbol must be created for each authentication.
>    */
>   auth = createKeylessAuth()
>
>   /**
>    * Add event listeners through the Keyless authentication symbol.
>    * These listeners will handle events during the authentication process.
>    */
>   addKeylessEventListeners(auth, [
>     { name: 'error', callback: (error) => onKeylessError(auth, error) },
>     { name: 'finished', callback: (message) => onKeylessFinished(auth, message) },
>     { name: 'frame-results', callback: (message) => onKeylessFrameResults(auth, message) },
>     { name: 'video-frame-quality', callback: (event) => onKeylessVideoFrameQuality(auth, event) }
>   ])
>
>   options = {
>     authorization: {
>       token: 'USER_AUTHORIZATION_FROM_CUSTOMER'
>     },
>     customer: { name: 'CUSTOMER_NAME' },
>     key: { id: 'IMAGE_ENCRYPTION_KEY_ID', value: 'IMAGE_ENCRYPTION_PUBLIC_KEY' },
>     transaction: {
>       data: 'DATA_FROM_CUSTOMER_SERVER_TO_BE_SIGNED'
>     },
>     username: 'USERNAME',
>     ws: { url: 'KEYLESS_AUTHENTICATION_SERVICE_URL' }
>   }
>
>   /**
>    * Create a media stream from the user's video input media device.
>    * This stream will be used to capture video frames for biometric analysis.
>    *
>    * Note: The user must grant permission to access the media device.
>    */
>   stream = await createKeylessMediaStream()
>   if (stream instanceof Error) return handleCreateKeylessMediaStreamError(stream)
>
>   /**
>    * Open a WebSocket connection to the Keyless Authentication Service.
>    * This connection will be used to process video frames and receive authentication results.
>    */
>   open = await openKeylessWebSocketConnection(auth, options)
>   if (open instanceof Error) return handleOpenKeylessWebSocketConnectionError(open)
> }
>
> importKeylessWebAssemblyModuleOrThrow()
>   .then(() =>
>     ensureCameraOperativity()
>       .then(() => authenticateWithKeyless())
>       .catch(handleCameraOperativityError)
>   )
>   .catch(handleImportKeylessWebAssemblyModuleError)
> ```

## Web component integration

This section shows how to use HTML to authenticate.

* React

* Vue

* Embedded

```javascript
import '@keyless/sdk-web-components'

export function KeylessAuth() {
  onError = (event) => {
    // will log the error code
    console.log(event.message)
  }

  onFinished = (event) => {
    /**
     * The `transactionJwt` is a JSON Web Token (JWT) that contains information
     * about the authentication transaction.
     *
     * This token is signed by the Keyless Authentication Service and can be used
     * to verify the authenticity of the transaction.
     *
     * This operation is strictly backend-to-backend and should never be performed
     * in client-side code.
     */
    requestTransactionJwtVerification(message.transactionJwt)
  }

  return (
    <kl-auth
      authorization-token='USER_AUTHORIZATION_FROM_CUSTOMER'
      customer='CUSTOMER_NAME'
      enable-camera-instructions
      key-id='IMAGE_ENCRYPTION_KEY_ID'
      lang='en'
      onerror={onError}
      onfinished={onFinished}
      public-key='IMAGE_ENCRYPTION_PUBLIC_KEY'
      size='375'
      theme='light'
      transaction-data='DATA_FROM_CUSTOMER_SERVER_TO_BE_SIGNED'
      username='USERNAME'
      ws-url='KEYLESS_AUTHENTICATION_SERVICE_URL'
    />
  )
}
```

```javascript
<script setup>
import '@keyless/sdk-web-components'

function onError(event) {
  // will log the error code
  console.log(event.message)
}

function onFinished(event) {
  /**
   * The `transactionJwt` is a JSON Web Token (JWT) that contains information
   * about the authentication transaction.
   *
   * This token is signed by the Keyless Authentication Service and can be used
   * to verify the authenticity of the transaction.
   *
   * This operation is strictly backend-to-backend and should never be performed
   * in client-side code.
   */
  requestTransactionJwtVerification(message.transactionJwt)
}
</script>

<template>
  <kl-auth
    customer="CUSTOMER_NAME"
    enable-camera-instructions
    @error="onError"
    @finished="onFinished"
    key="IMAGE_ENCRYPTION_PUBLIC_KEY"
    key-id="IMAGE_ENCRYPTION_KEY_ID"
    lang="en"
    size="375"
    theme="light"
    transaction-data='DATA_FROM_CUSTOMER_SERVER_TO_BE_SIGNED'
    username="USERNAME"
    ws-url="KEYLESS_AUTHENTICATION_SERVICE_URL"
  />
</template>
```

```javascript
<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Auth</title>
    <style>
      * {
        box-sizing: border-box;
      }

      body {
        align-items: center;
        display: flex;
        justify-content: center;
        margin: 0;
        min-height: 100vh;
        padding: 8px;
      }

      kl-auth {
        border: 1px solid lightgray;
      }
    </style>
  </head>
  <body>
    <kl-auth
      customer="CUSTOMER_NAME"
      enable-camera-instructions
      key="IMAGE_ENCRYPTION_PUBLIC_KEY"
      key-id="IMAGE_ENCRYPTION_KEY_ID"
      lang="en"
      size="375"
      theme="light"
      transaction-data='DATA_FROM_CUSTOMER_SERVER_TO_BE_SIGNED'
      username="USERNAME"
      ws-url="KEYLESS_AUTHENTICATION_SERVICE_URL"
    ></kl-auth>
    <script src="./node_modules/@keyless/sdk-web-components/index.js" type="module"></script>
    <script>
      const auth = document.querySelector('kl-auth')

      auth.addEventListener('error', (event) => {
        // will log the error code
        console.log(event.message)
      })

      auth.addEventListener('finished', (event) => {
        /**
         * The `transactionJwt` is a JSON Web Token (JWT) that contains information
         * about the authentication transaction.
         *
         * This token is signed by the Keyless Authentication Service and can be used
         * to verify the authenticity of the transaction.
         *
         * This operation is strictly backend-to-backend and should never be performed
         * in client-side code.
         */
        requestTransactionJwtVerification(message.transactionJwt)
      })
    </script>
  </body>
</html>
```

---

---
title: Browser requirements
description: "\"Shows which web browsers are supported by the PingOne Recognize Web SDK.\""
component: recognize
page_id: recognize:web-sdk:web-sdk-guide-browser-requirements
canonical_url: https://docs.pingidentity.com/recognize/web-sdk/web-sdk-guide-browser-requirements.html
llms_txt: https://docs.pingidentity.com/recognize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
---

# Browser requirements

The PingOne Recognize Web SDK supports the following browsers and web views components:

* Android Browser, release 141 or later

* Android WebView, release 94 or later

* Google Chrome, release 109 or later

* Microsoft Edge, release 139 or later

* Mozilla Firefox, release 140 or later

* Opera, release 121 or later

* Opera Mobile, release 80 or later

* Apple Safari, release 18.5 or later

* Samsung Internet, release 27 or later

* Apple WKWebView, release 18.4 or later

The following browsers are not supported by PingOne Recognize:

* Microsoft Internet Explorer

* Opera Mini

---

---
title: Camera permission flow
description: "\"Describes how PingOne Recognize authorization and enrollment handles camera permission requests.\""
component: recognize
page_id: recognize:web-sdk:web-sdk-reference-camera-permission
canonical_url: https://docs.pingidentity.com/recognize/web-sdk/web-sdk-reference-camera-permission.html
llms_txt: https://docs.pingidentity.com/recognize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
---

# Camera permission flow

By default, PingOne Recognize Web SDK displays a camera permissions page during authentication and enrollment. The page explains the need for permissions and blocks further action when the user declines camera access.

The access check uses the `Permissions.query` method to determine camera access. Learn more in the Mozilla [reference page](https://developer.mozilla.org/en-US/docs/Web/API/Permissions/query).

If the Permissions API is not supported in the user's browser, PingOne Recognize uses an alternate approach that displays the camera permissions check the first time they open a page using the Web SDK. Results are saved in browser session storage.

You can skip the permissions check by setting the session storage value directly, either programmatically or manually.

The `@keyless/sdk-web` package exposes the `setKeylessCameraPermissionStorageItem` function. Use this to set the `state` key to one of the following values:

| Value     | Description                     |
| --------- | ------------------------------- |
| `denied`  | Access to the camera is denied  |
| `granted` | Access to the camera is allowed |

The session storage value can also be set manually. To do this, update the `kl-camera-permission` key.

To avoid common errors, you should use the `setKeylessCameraPermissionStorageItem` function instead of setting the value manually.

---

---
title: Changelog
description: Details recent changes to the PingOne Recognize Web SDK
component: recognize
page_id: recognize:web-sdk:web-sdk-changelog
canonical_url: https://docs.pingidentity.com/recognize/web-sdk/web-sdk-changelog.html
llms_txt: https://docs.pingidentity.com/recognize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  3-0-0: 3.0.0
  highlights: Highlights
  2-4-2: 2.4.2
  fixes: Fixes
  2-4-1: 2.4.1
  fixes-2: Fixes
  2-4: 2.4
  highlights-2: Highlights
  deprecations: Deprecations
  breaking-changes: Breaking Changes
  new-apis: New APIs
  2-3-1: 2.3.1
  highlights-3: Highlights
  breaking-changes-2: Breaking Changes
  fixes-3: Fixes
  2-3: 2.3
  highlights-4: Highlights
  deprecations-2: Deprecations
  breaking-changes-3: Breaking Changes
  2-2-1: 2.2.1
  fixes-4: Fixes
  2-2: 2.2
  highlights-5: Highlights
  2-1-2: 2.1.2
  highlights-6: Highlights
  2-1-1: 2.1.1
  fixes-5: Fixes
  2-1: 2.1
  highlights-7: Highlights
  2-0: 2.0
  highlights-8: Highlights
---

# Changelog

## 3.0.0

### Highlights

* Upgrade to v2 HTTP API

* Better network stability

* Security improvements

## 2.4.2

### Fixes

* Allows browser extensions to detect the PingOne Recognize Web SDK

## 2.4.1

### Fixes

* Fix edge case with camera permissions

## 2.4

### Highlights

* Active Face Quality Filters running on the client

### Deprecations

* **\[Headless]** The `getLastKeylessFrameResults` function has been replaced by `getLastKeylessServerFrameResults`

* **\[Headless]** The `getLastKeylessFrameTriggeredBiometricFilters` function has been replaced by `getLastKeylessServerFrameTriggeredBiometricFilters`

### Breaking Changes

* **\[Headless]** The SDK added the `CREATE_MEDIA_STREAM_ARGS_UNSET` error, which should be localized as a generic system error

* **\[Web Components]** The localization for the `kl-camera-tip` component and the `SERVER_RECOGNITION_FAILED` error has changed structure. To learn more, refer to [Localization](web-sdk-reference-localization.html)

### New APIs

* **\[Headless]** The `getLastKeylessServerError` function returns the last server error tied to the attempt

* **\[Headless]** The `getLastVideoFrameQuality` function returns the quality of the last video frame from the camera stream, the quality is computed on the client

* **\[Web Components]** The `kl-auth` and `kl-enroll` elements emit a new `video-frame-quality` event

## 2.3.1

### Highlights

* Removes client-side Lockout Policy

### Breaking Changes

* **\[Headless]** The `DEFAULT_KEYLESS_LOCKOUT_TIME`, `DEFAULT_KEYLESS_LOCKOUT_TOLERANCE` and `DEFAULT_KEYLESS_LOCKOUT_WINDOW` constants are no longer exported

* **\[Headless]** The `KeylessLockoutAttempt` and `KeylessLockoutOptions` interfaces are no longer exported

* **\[Headless]** The `getLastKeylessLockoutAttempt`, `etLockoutExpirationDate` and `getLockoutTime` functions are no longer exported

* **\[Headless]** The `getServerLockoutExpirationDate` function was renamed to `getKeylessServerLockoutExpirationDate`

* **\[Headless]** The lockout field in the `KeylessOptions` interface was removed

* **\[Web Components]** The `enable-lockout`, `lockout-time`, l\`ockout-tolerance\`. and `lockout-window` attributes are no longer available

### Fixes

* Fix edge case with camera permissions

## 2.3

### Highlights

* Passive Face Quality Filters running on the client

* Smaller WebAssembly binary size

* Better Remote Logging

### Deprecations

* **\[Headless]** The `importKeylessWebAssemblyModule` function now optionally takes `url.binary` instead of `url.file` in the options argument

* **\[Web Components]** The `kl-auth` and `kl-enroll` elements now optionally take the `wasm-binary-url` attribute instead of `wasm-file-url`

### Breaking Changes

* The `@keyless/sdk-web` and `@keyless/sdk-web-components` packages now include a `wasm.data` file, make sure to bundle it or the SDK will not work

## 2.2.1

### Fixes

* Fix Firefox on Android unable to grant camera permissions

## 2.2

### Highlights

* Single-Thread by default with opt-in Multi-Thread

* COEP/COOP Security Headers are no longer required by default

## 2.1.2

### Highlights

* Faster Camera Startup Time

* Better Camera Permission Flow

## 2.1.1

### Fixes

* Fix Operation ID Forwarding

## 2.1

### Highlights

* CDN Distribution

* Prettier Web Components UI

* Better Tampering Protections

## 2.0

### Highlights

* Better Headless APIs

* Tampering Protections

---

---
title: Components
description: "\"Describes PingOne Recognize Web SDK components and how to use them.\""
component: recognize
page_id: recognize:web-sdk:web-sdk-introduction-components
canonical_url: https://docs.pingidentity.com/recognize/web-sdk/web-sdk-introduction-components.html
llms_txt: https://docs.pingidentity.com/recognize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  headless-enrollment: Headless enrollment
  web-component-enrollment: Web component enrollment
  idv-bridge-saas-enrollment: IDV Bridge SaaS enrollment
  headless-authentication: Headless authentication
  web-component-authentication: Web component authentication
---

# Components

The diagrams below show how the PingOne Recognize Web SDK, which runs within your web app on the user's browser, interacts with your application server and with the PingOne Recognize network.

## Headless enrollment

Headless enrollment occurs when you register a user or device without a user experience; that is, without using any additional interaction or UI controls.

To do this with the PingOne Recognize Web SDK, use client-side JavaScript in your web application.

During enrollment, your web app creates a PingOne Recognize enroll symbol and establishes a connection to the PingOne Recognize Authentication Service. It then:

1. Waits for the "begin-stream" event and sends the first face frame.

2. Waits for the "frame-results" event and sends one more face frame.

3. The wait will continue in a loop until either:

   1. The `error` event is fired which means that most likely the biometric pipeline failed, or another error stopped the process.

   2. The `stop-stream` event is fired which means that the biometric pipeline succeeded.

4. Now the PingOne Recognize Authentication Service will extract the vectors of the last frame sent and perform the recognition process.

5. Waits for the "finished" event.

![Architecture diagram showing the headless enrollment flow. A User feeds into a Camera, which connects to the @keyless/sdk-web library running inside a Customer Website in a Web Browser. The library sends data to the Authentication Service, which contains the Core Low Level SDK and Biometric SDK components. The Authentication Service writes to a KMS and a Database, and passes results to the Core Backend. Blue shaded boxes indicate Web SDK components; yellow boxes indicate Keyless dependencies.](_images/web-sdk-introduction-components-headless-enrollment-diagram.png)

## Web component enrollment

|   |                                                                                                                                                                                                                      |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | PingOne Recognize uses [Web Components](https://developer.mozilla.org/en-US/docs/Web/API/Web_components) to be framework agnostic. These custom elements should work in any environment that supports this standard. |

During enrollment, your web app loads and renders the `kl-enroll` web component, the component will establish a connection to the PingOne Recognize Authentication Service as soon as it is mounted, then it:

1. Checks if the user has consented to the usage of their camera, the permission must be granted to proceed.

2. Checks if the user is on a desktop device and has multiple cameras.

   If so, the user is asked to pick one to avoid using the wrong camera by default.

   This doesn't work on mobile devices, which prefer the selfie camera by default.

3. Starts sending face frames to the PingOne Recognize Authentication Service at a set framerate.

4. Waits for the "finished" event.

![Architecture diagram showing the web component enrollment flow. A User feeds into a Camera, which connects to the @keyless/sdk-web-components library running inside a Customer Website in a Web Browser. The library sends data to the Authentication Service, which contains the Core Low Level SDK and Biometric SDK components. The Authentication Service writes to a KMS and a Database, and passes results to the Core Backend. Blue shaded boxes indicate Web SDK components; yellow boxes indicate Keyless dependencies.](_images/web-sdk-introduction-web-component-enrollment-diagram.png)

## IDV Bridge SaaS enrollment

|   |                                                                                                                                                                                                                                                                           |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | In this context the enrollment happens on the server-side, requiring no interaction from the user unless manually implemented by the integrator on their client. Head to [IDV Bridge space](https://docs.keyless.io/idv-bridge) for more information about this solution. |

During enrollment, your back-end service will perform a POST request to the PingOne Recognize Authentication Service following these steps:

1. Generates a new `AES-GCM` or `AES-GCM-SIV` key.

2. Encrypts the face image with the `AES-GCM` or `AES-GCM-SIV` key.

3. Encrypts the `AES-GCM` or `AES-GCM-SIV` key with the `RSAES-OAEP-SHA-256` public key also known as `IMAGE_ENCRYPTION_PUBLIC_KEY`.

4. Performs the POST request and waits for a 201 response status code.

![Architecture diagram showing the IDV Bridge SaaS enrollment flow. A Customer Backend sends a request directly to the Authentication Service, which contains the Core Low Level SDK and Biometric SDK components. The Authentication Service writes to a KMS and a Database, and passes results to the Core Backend. This flow is entirely backend-to-backend with no browser or user interaction. Blue shaded boxes indicate Web SDK components; yellow boxes indicate Keyless dependencies.](_images/web-sdk-introduction-components-idv-saas-enrollment-diagram.png)

## Headless authentication

Headless authentication doesn't use a user interface. It uses client-side JavaScript to authenticate the user.

Your web app creates a PingOne Recognize auth symbol and establishes a connection to the PingOne Recognize Authentication Service, then:

1. Waits for the "begin-stream" event and sends the first face frame.

2. Waits for the "frame-results" event and sends one more face frame.

3. The wait will continue in a loop until either of:

   1. The "error" event is fired which means that most likely the biometric pipeline failed, or another error stopped the process.

   2. The "stop-stream" event is fired which means that the biometric pipeline succeeded.

4. Now the PingOne Recognize Authentication Service will extract the vectors of the last frame sent and perform the recognition process.

5. Waits for the "finished" event.

![Architecture diagram showing the headless authentication flow. A User feeds into a Camera, which connects to the @keyless/sdk-web library running inside a Customer Website in a Web Browser. The library sends data to the Authentication Service, which contains the Core Low Level SDK and Biometric SDK components. The Authentication Service writes to a KMS and a Database, and passes results to the Core Backend. Blue indicates Web SDK components; yellow indicates Keyless dependencies.](_images/web-sdk-components-headless-authentication-diagram.png)

## Web component authentication

|   |                                                                                                                                                                                                                |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | PingOne Recognize uses [Web Components](https://developer.mozilla.org/en-US/docs/Web/API/Web_components) to be framework agnostic. Custom elements should work in any environment that supports this standard. |

During authentication, your web app loads and renders the `kl-auth` web component, the component will establish a connection to the PingOne Recognize Authentication Service as soon as it is mounted, then it:

1. Checks if the user has consented to the usage of their camera, the permission must be granted to proceed.

2. Checks if the user is on a desktop device and has multiple cameras.

   If so, the user is asked to pick one to avoid using the wrong camera.

   This doesn't happen on mobile devices, which prefer the selfie camera by default.

3. Starts sending face frames to the PingOne Recognize Authentication Service at a set framerate.

4. Waits for the "finished" event.

![Architecture diagram showing the web component authentication flow. A User feeds into a Camera, which connects to the @keyless/sdk-web-components library running inside a Customer Website in a Web Browser. The library sends data to the Authentication Service, which contains the Core Low Level SDK and Biometric SDK components. The Authentication Service writes to a KMS and a Database, and passes results to the Core Backend. Blue indicates Web SDK components; yellow indicates Keyless dependencies.](_images/web-sdk-components-web-component-authentication-diagram.png)

---

---
title: Enrollment
description: "\"Shows how to enroll a new user by connecting their facial biometrics to PingOne Recognize account.\""
component: recognize
page_id: recognize:web-sdk:web-sdk-guide-enrollment
canonical_url: https://docs.pingidentity.com/recognize/web-sdk/web-sdk-guide-enrollment.html
llms_txt: https://docs.pingidentity.com/recognize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  before-you-begin: Before you begin
  headless-integration: Headless integration
  component-integration: Web component integration
---

# Enrollment

Enrollment is the process of registering a new user by connecting their facial biometrics to a PingOne Recognize account. During this process, a full and unobstructed view of the user's face is required.

Enrollment with Web SDK can happen in two ways:

* Live enrollment using the PingOne Recognize Web SDK JavaScript libraries.

* [IDV Bridge SaaS](../idv-bridge/idv-bridge-saas.html) using the PingOne Recognize Authentication Service

This page explains how to perform interactive live enrollment on the front-end.

PingOne Recognize also supports [component interoperability](#idv-bridge:idv-bridge-component-interoperability), so that users can be enrolled using IDV Bridge (on-premises) or the Mobile SDK. Authentication can be performed later using JavaScript and the Web SDK.

## Before you begin

Review the [prerequisites requirements](web-sdk-prerequisites.html) before continuing.

## Headless integration

The `@keyless/sdk-web` library lets you integrate the PingOne Recognize Web SDK without using a user interface. Here's a simple enrollment:

> **Collapse: Details**
>
> ```javascript
> import {
>   addKeylessEventListeners,
>   createKeylessEnroll,
>   createKeylessMediaStream,
>   getKeylessCameraPermissionState,
>   getKeylessVideoMediaDevices,
>   getLastKeylessServerFrameTriggeredBiometricFilters,
>   getLastKeylessVideoFrameQuality,
>   importKeylessWebAssemblyModuleOrThrow,
>   isKeylessVideoMediaStreamAvailable,
>   KeylessError,
>   openKeylessWebSocketConnection,
>   reduceKeylessBiometricFiltersToTriggered,
>   removeKeylessEventListeners
> } from '@keyless/sdk-web'
>
> function requestTransactionJwtVerification(jwt) {}
> function requestUserCameraPermission() {}
>
> function handleCameraOperativityError(error) {}
> function handleImportKeylessWebAssemblyModuleError(error) {}
> function handleCreateKeylessMediaStreamError(error) {}
> function handleOpenKeylessWebSocketConnectionError(error) {}
>
> /**
>  * This event is fired when an error occurs during the enrollment process.
>  * The error object contains a `message` property that indicates the type of error.
>  */
> function onKeylessError(sym, error) {
>   /**
>    * Removing event listeners is advised on terminal events since
>    * no more than one attempt is allowed per enrollment symbol.
>    */
>   removeKeylessEventListeners(sym)
>
>   // will log the error code
>   console.error(error.message)
> }
>
> /**
>  * This event is fired when the enrollment process is complete.
>  * It does not fire for failed attempts, only successful ones.
>  */
> function onKeylessFinished(sym, message) {
>   /**
>    * Removing event listeners is advised on terminal events since
>    * no more than one attempt is allowed per enrollment symbol.
>    */
>   removeKeylessEventListeners(sym)
>
>   /**
>    * The `transactionJwt` is a JSON Web Token (JWT) that contains information
>    * about the enrollment transaction.
>    *
>    * This token is signed by the Keyless Authentication Service and can be used
>    * to verify the authenticity of the transaction.
>    *
>    * This operation is strictly backend-to-backend and should never be performed
>    * in client-side code.
>    */
>   requestTransactionJwtVerification(message.transactionJwt)
> }
>
> /**
>  * This event is useful for providing real-time feedback to users during
>  * the enrollment process, such as prompting them to adjust their position
>  * or lighting conditions to improve biometric recognition.
>  *
>  * The difference with "onKeylessVideoFrameQuality" is that this is from
>  * filters running on the server.
>  */
> function onKeylessFrameResults(sym, message) {
>   let filters
>
>   /**
>    * Returns an array of biometric filters that were triggered in the last frame.
>    * If no biometric filters were triggered, an empty array is returned.
>    */
>   filters = reduceKeylessBiometricFiltersToTriggered(message.filters)
>
>   /**
>    * Optionally, this function can be used to retrieve the filters that were triggered
>    * in the last frame.
>    *
>    * This can be useful if you need to access the last frame's triggered filters outside
>    * of the frame results event.
>    *
>    * If this function is used then this event is useful for requesting an update to the UI.
>    */
>   filters = getLastKeylessServerFrameTriggeredBiometricFilters(sym)
> }
>
> /**
>  * This event is useful for providing real-time feedback to users during
>  * the enrollment process, such as prompting them to adjust their position
>  * or lighting conditions to improve biometric recognition.
>  *
>  * The difference with "onKeylessFrameResults" is that this is from filters
>  * running on the client.
>  */
> function onKeylessVideoFrameQuality(sym, event) {
>   /**
>    * Will log an array of filters that were triggered in this frame.
>    * If no biometric filters were triggered, an empty array is returned.
>    */
>   console.log(event.filters)
>
>   /**
>    * Optionally, this function can be used to retrieve the quality of the last
>    * video frame.
>    *
>    * This can be useful if you need to access the last video frame quality outside
>    * of the video frame quality event.
>    *
>    * If this function is used then this event is useful for requesting an update to the UI.
>    */
>   console.log(getLastKeylessVideoFrameQuality(sym))
> }
>
> async function ensureCameraOperativity() {
>   let devices, state
>
>   devices = await getKeylessVideoMediaDevices()
>
>   /**
>    * If the error is MEDIA_DEVICES_NO_VIDEO_INPUTS, it means that
>    * the user's device doesn't have a camera.
>    */
>   if (devices instanceof Error && devices.message === KeylessError.MEDIA_DEVICES_NO_VIDEO_INPUTS) throw devices
>
>   state = await getKeylessCameraPermissionState()
>
>   /**
>    * If the camera permission state is not 'granted', request
>    * the user to grant camera access.
>    */
>   if (state !== 'granted') {
>     /**
>      * Ideally this function should take the user to a UI prompt
>      * where they can grant camera access to the website.
>      *
>      * The easiest way to trigger the browser's camera permission prompt
>      * is to call isKeylessVideoMediaStreamAvailable(), which will return
>      * a boolean indicating whether the user granted camera access or not.
>      */
>     requestUserCameraPermission()
>     throw new Error('camera permission state is not granted')
>   }
>
>   devices = await getKeylessVideoMediaDevices()
>
>   /**
>    * If the error is MEDIA_DEVICES_EMPTY_VIDEO_INPUT_LABEL, it means that
>    * even though the user has granted camera access, the browser requires
>    * the user to start a video stream to be able to read the camera labels.
>    *
>    * In this case, we perform a throwaway getUserMedia() request with
>    * isKeylessVideoMediaStreamAvailable() to start a video stream
>    * to be able to read the camera labels.
>    */
>   if (devices instanceof Error && devices.message === KeylessError.MEDIA_DEVICES_EMPTY_VIDEO_INPUT_LABEL) {
>     let available
>
>     available = await isKeylessVideoMediaStreamAvailable()
>     if (!available) throw new Error('video media stream is not available')
>
>     devices = await getKeylessVideoMediaDevices()
>   }
>
>   /**
>    * If we still have an error, throw an error to indicate that
>    * the media devices still could not be read correctly.
>    */
>   if (devices instanceof Error) throw devices
> }
>
> async function enrollWithKeyless() {
>   let enroll, options, stream, open
>
>   /**
>    * Create a Keyless enrollment symbol.
>    *
>    * This symbol must be kept in memory for the duration of the enrollment process.
>    * To perform multiple enrollments, a new symbol must be created for each enrollment.
>    */
>   enroll = createKeylessEnroll()
>
>   /**
>    * Add event listeners through the Keyless enrollment symbol.
>    * These listeners will handle events during the enrollment process.
>    */
>   addKeylessEventListeners(enroll, [
>     { name: 'error', callback: (error) => onKeylessError(enroll, error) },
>     { name: 'finished', callback: (message) => onKeylessFinished(enroll, message) },
>     { name: 'frame-results', callback: (message) => onKeylessFrameResults(enroll, message) },
>     { name: 'video-frame-quality', callack: (event) => onKeylessVideoFrameQuality(enroll, event) }
>   ])
>
>   options = {
>     authorization: {
>         token: 'USER_AUTHORIZATION_FROM_CUSTOMER'
>     },
>     customer: { name: 'CUSTOMER_NAME' },
>     key: { id: 'IMAGE_ENCRYPTION_KEY_ID', value: 'IMAGE_ENCRYPTION_PUBLIC_KEY' },
>     transaction: {
>       data: 'DATA_FROM_CUSTOMER_SERVER_TO_BE_SIGNED'
>     },
>     username: 'USERNAME',
>     ws: { url: 'KEYLESS_AUTHENTICATION_SERVICE_URL' }
>   }
>
>   /**
>    * Create a media stream from the user's video input media device.
>    * This stream will be used to capture video frames for biometric analysis.
>    *
>    * Note: The user must grant permission to access the media device.
>    */
>   stream = await createKeylessMediaStream()
>   if (stream instanceof Error) return handleCreateKeylessMediaStreamError(stream)
>
>   /**
>    * Open a WebSocket connection to the Keyless Authentication Service.
>    * This connection will be used to process video frames and receive enrollment results.
>    */
>   open = await openKeylessWebSocketConnection(enroll, options)
>   if (open instanceof Error) return handleOpenKeylessWebSocketConnectionError(open)
> }
>
> importKeylessWebAssemblyModuleOrThrow()
>   .then(() =>
>     ensureCameraOperativity()
>       .then(() => enrollWithKeyless())
>       .catch(handleCameraOperativityError)
>   )
>   .catch(handleImportKeylessWebAssemblyModuleError)
> ```

## Web component integration

This section shows how to integrate the PingOne Recognize Web SDK directly into a web application.

* React

* Vue

* Embedded

```javascript
import '@keyless/sdk-web-components'

export function KeylessEnroll() {
  function requestTransactionJwtVerification(jwt) {}

  onError = (event) => {
    // will log the error code
    console.log(event.message)
  }

  onFinished = (event) => {
    /**
     * The `transactionJwt` is a JSON Web Token (JWT) that contains information
     * about the enrollment transaction.
     *
     * This token is signed by the Keyless Authentication Service and can be used
     * to verify the authenticity of the transaction.
     *
     * This operation is strictly backend-to-backend and should never be performed
     * in client-side code.
     */
    requestTransactionJwtVerification(message.transactionJwt)
  }

  return (
    <kl-enroll
      authorization-token='USER_AUTHORIZATION_FROM_CUSTOMER'
      customer='CUSTOMER_NAME'
      enable-camera-instructions
      key-id='IMAGE_ENCRYPTION_KEY_ID'
      lang='en'
      onerror={onError}
      onfinished={onfinished}
      public-key='IMAGE_ENCRYPTION_PUBLIC_KEY'
      size='375'
      theme='light'
      transaction-data='DATA_FROM_CUSTOMER_SERVER_TO_BE_SIGNED'
      username='USERNAME'
      ws-url='KEYLESS_AUTHENTICATION_SERVICE_URL'
    />
  )
}
```

```javascript
<script setup>
import '@keyless/sdk-web-components'

function requestTransactionJwtVerification(jwt) {}

function onError(event) {
// will log the error code
console.log(event.message)
}

function onFinished(event) {
/**
* The `transactionJwt` is a JSON Web Token (JWT) that contains information
* about the enrollment transaction.
*
* This token is signed by the Keyless Authentication Service and can be used
* to verify the authenticity of the transaction.
*
* This operation is strictly backend-to-backend and should never be performed
* in client-side code.
*/
requestTransactionJwtVerification(message.transactionJwt)
}
</script>

<template>
<kl-enroll
customer="CUSTOMER_NAME"
enable-camera-instructions
@error="onError"
@finished="onFinished"
key="IMAGE_ENCRYPTION_PUBLIC_KEY"
key-id="IMAGE_ENCRYPTION_KEY_ID"
lang="en"
size="375"
theme="light"
transaction-data='DATA_FROM_CUSTOMER_SERVER_TO_BE_SIGNED'
username="USERNAME"
ws-url="KEYLESS_AUTHENTICATION_SERVICE_URL"
/>
</template>
```

```javascript
<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Enroll</title>
    <style>
      * {
        box-sizing: border-box;
      }

      body {
        align-items: center;
        display: flex;
        justify-content: center;
        margin: 0;
        min-height: 100vh;
        padding: 8px;
      }

      kl-enroll {
        border: 1px solid lightgray;
      }
    </style>
  </head>
  <body>
    <kl-enroll
      customer="CUSTOMER_NAME"
      enable-camera-instructions
      key="IMAGE_ENCRYPTION_PUBLIC_KEY"
      key-id="IMAGE_ENCRYPTION_KEY_ID"
      lang="en"
      size="375"
      theme="light"
      transaction-data='DATA_FROM_CUSTOMER_SERVER_TO_BE_SIGNED'
      username="USERNAME"
      ws-url="KEYLESS_AUTHENTICATION_SERVICE_URL"
    ></kl-enroll>
    <script src="./node_modules/@keyless/sdk-web-components/index.js" type="module"></script>
    <script>
      const enroll = document.querySelector('kl-enroll')

      function requestTransactionJwtVerification(jwt)

      enroll.addEventListener('error', (event) => {
        // will log the error code
        console.log(event.message)
      })

      enroll.addEventListener('finished', (event) => {
        /**
         * The `transactionJwt` is a JSON Web Token (JWT) that contains information
         * about the enrollment transaction.
         *
         * This token is signed by the Keyless Authentication Service and can be used
         * to verify the authenticity of the transaction.
         *
         * This operation is strictly backend-to-backend and should never be performed
         * in client-side code.
         */
        requestTransactionJwtVerification(message.transactionJwt)
      })
    </script>
  </body>
</html>
```

---

---
title: Error handling
description: "\"Explains the errors that can occur when using the PingOne Recognize Web SDK and how to handle them.\""
component: recognize
page_id: recognize:web-sdk:web-sdk-reference-error-handling
canonical_url: https://docs.pingidentity.com/recognize/web-sdk/web-sdk-reference-error-handling.html
llms_txt: https://docs.pingidentity.com/recognize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  error-types: Error types
  registering-event-listeners: Registering event listeners
  handling-errors: Handling errors
  error-reference: Error reference
  web-component-error-handling: Web component error handling
---

# Error handling

The PingOne Recognize Web SDK can generate a variety of errors when processing authentication (`KeylessAuth`) and enrollment (`KeylessEnroll`) requests.

## Error types

The PingOne Recognize Web SDK generates the following error types:

* General `error` events common to web applications

* WebSocket specific (`ws-error`) errors

## Registering event listeners

To handle errors, register an error event listener, as shown in the following example:

```javascript
import { createKeylessAuth } from '@keyless/sdk-web'

function onKeylessError(error) {
  // will log the error code
  console.log(error.message)
}

const auth = createKeylessAuth()

// register the error event listener
addKeylessEventListener(auth, 'error', onKeylessError)

// opening a connection without the required options will always emit an error
openKeylessWebSocketConnection(auth, {})
```

Enrollment components, such as `KeylessEnroll`, also support error event listeners.

## Handling errors

When errors occur, the `error` object passed to the event listener contains an error code defined in the `KeylessError` enumeration exported by the `@keyless/sdk-web` package:

> **Collapse: Details**
>
> ```javascript
> enum KeylessError {
>   FRAME_RESULTS_SET_UNSET = 'FRAME_RESULTS_SET_UNSET',
>   OPTIONS_UNSET = 'OPTIONS_UNSET',
>
>   MEDIA_DEVICES_EMPTY_VIDEO_INPUT_LABEL = 'MEDIA_DEVICES_EMPTY_VIDEO_INPUT_LABEL',
>   MEDIA_DEVICES_NO_VIDEO_INPUTS = 'MEDIA_DEVICES_NO_VIDEO_INPUTS',
>
>   MEDIA_STREAM_ABORT = 'MEDIA_STREAM_ABORT',
>   MEDIA_STREAM_INVALID_STATE = 'MEDIA_STREAM_INVALID_STATE',
>   MEDIA_STREAM_NOT_ALLOWED = 'MEDIA_STREAM_NOT_ALLOWED',
>   MEDIA_STREAM_NOT_FOUND = 'MEDIA_STREAM_NOT_FOUND',
>   MEDIA_STREAM_NOT_READABLE = 'MEDIA_STREAM_NOT_READABLE',
>   MEDIA_STREAM_OVERCONSTRAINED = 'MEDIA_STREAM_OVERCONSTRAINED',
>   MEDIA_STREAM_SECURITY = 'MEDIA_STREAM_SECURITY',
>   MEDIA_STREAM_TYPE = 'MEDIA_STREAM_TYPE',
>
>   SERVER_CUSTOMER_NOT_FOUND = 'SERVER_CUSTOMER_NOT_FOUND',
>   SERVER_INTERNAL_ERROR = 'SERVER_INTERNAL_ERROR',
>   SERVER_RECOGNITION_FAILED = 'SERVER_RECOGNITION_FAILED',
>
>   SESSION_MANAGER_NOT_NULL = 'SESSION_MANAGER_NOT_NULL',
>   SESSION_MANAGER_NULL = 'SESSION_MANAGER_NULL',
>
>   EXCEPTION = 'EXCEPTION',
>   RUNTIME_VIOLATION = 'RUNTIME_VIOLATION',
>   SYMBOL_DESCRIPTION_UNSET = 'SYMBOL_DESCRIPTION_UNSET',
>
>   SESSION_ID_UNSET = 'SESSION_ID_UNSET',
>
>   CUSTOMER_UNSET = 'CUSTOMER_UNSET',
>   USERNAME_UNSET = 'USERNAME_UNSET',
>
>   WEB_ASSEMBLY_ABORTED = 'WEB_ASSEMBLY_ABORTED',
>   WEB_ASSEMBLY_FACTORY_FAILED = 'WEB_ASSEMBLY_FACTORY_FAILED',
>   WEB_ASSEMBLY_IMPORT_FAILED = 'WEB_ASSEMBLY_IMPORT_FAILED',
>   WEB_ASSEMBLY_NOT_READY = 'WEB_ASSEMBLY_NOT_READY',
>   WEB_ASSEMBLY_MODULE_NOT_FOUND = 'WEB_ASSEMBLY_MODULE_NOT_FOUND',
>
>   USER_LOCKOUT_EXPIRATION_UNSET = 'USER_LOCKOUT_EXPIRATION_UNSET'
>   SERVER_INVALID_REQUEST = 'SERVER_INVALID_REQUEST'
>   SERVER_INVALID_RESPONSE = 'SERVER_INVALID_RESPONSE'
>   SESSION_DATABASE_ERROR = 'SESSION_DATABASE_ERROR'
>   SESSION_MEDIA_STREAM_TIMEOUT = 'SESSION_MEDIA_STREAM_TIMEOUT'
>   SESSION_MEDIA_STREAM_UNSET = 'SESSION_MEDIA_STREAM_UNSET'
>   SERVICE_URL_PARSE_FAILED = 'SERVICE_URL_PARSE_FAILED'
>   SERVICE_URL_UNSET = 'SERVICE_URL_UNSET'
>   SLUG_UNSUPPORTED = 'SLUG_UNSUPPORTED'
>
> }
> ```

## Error reference

|                                         |                                                                                                                                                                                                                                                                                                                                                                                                 |
| --------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Error**                               | **Description**                                                                                                                                                                                                                                                                                                                                                                                 |
| `FRAME_RESULTS_SET_UNSET`               | Internal error; contact Support                                                                                                                                                                                                                                                                                                                                                                 |
| `OPTIONS_UNSET`                         | Internal error; contact Support                                                                                                                                                                                                                                                                                                                                                                 |
| `WEB_SOCKET_MESSAGE_SET_UNSET`          | Internal error; contact Support                                                                                                                                                                                                                                                                                                                                                                 |
| `MEDIA_DEVICES_EMPTY_VIDEO_INPUT_LABEL` | The user did not grant permission to use the camera                                                                                                                                                                                                                                                                                                                                             |
| `MEDIA_DEVICES_NO_VIDEO_INPUTS`         | The user's device does not have a camera                                                                                                                                                                                                                                                                                                                                                        |
| `MEDIA_STREAM_ABORT`                    | An `AbortError` exception occurred when attempting to retrieve media data from the user's device. Learn more about `AbortError` exceptions in Mozilla's `MediaDevice.getUserMedia()` [reference page](https://developer.mozilla.org/en-US/docs/Web/API/MediaDevices/getUserMedia#exceptions).                                                                                                   |
| `MEDIA_STREAM_INVALID_STATE`            | An `InvalidStateError` exception occurred when attempting to retrieve media data from the user's device. Learn more about `InvalidStateError` exceptions in Mozilla's `MediaDevice.getUserMedia()` [reference page](https://developer.mozilla.org/en-US/docs/Web/API/MediaDevices/getUserMedia#exceptions).                                                                                     |
| `MEDIA_STREAM_NOT_ALLOWED`              | A `NotAllowed` exception occurred when attempting to retrieve media data from the user's device. Learn more about `NotAllowedError` exceptions in Mozilla's `MediaDevice.getUserMedia()` [reference page](https://developer.mozilla.org/en-US/docs/Web/API/MediaDevices/getUserMedia#exceptions).                                                                                               |
| `MEDIA_STREAM_NOT_FOUND`                | A `NotFoundError` exception occurred when attempting to retrieve media data from the user's device. Learn more about `NotFoundError` exceptions in Mozilla's `MediaDevice.getUserMedia()` [reference page](https://developer.mozilla.org/en-US/docs/Web/API/MediaDevices/getUserMedia#exceptions).                                                                                              |
| `MEDIA_STREAM_NOT_READABLE`             | A `NotReadableError` exception occurred when attempting to retrieve media data from the user's device. Learn more about `NotReadableError` exceptions in Mozilla's `MediaDevice.getUserMedia()` [reference page](https://developer.mozilla.org/en-US/docs/Web/API/MediaDevices/getUserMedia#exceptions).                                                                                        |
| `MEDIA_STREAM_OVERCONSTRAINED`          | An `OverconstrainedError` exception occurred when attempting to retrieve media data from the user's device. Learn more about `OverconstrainedError` exceptions in Mozilla's `MediaDevice.getUserMedia()` [reference page](https://developer.mozilla.org/en-US/docs/Web/API/MediaDevices/getUserMedia#exceptions).                                                                               |
| `MEDIA_STREAM_SECURITY`                 | A `SecurityError` exception occurred when attempting to retrieve media data from the user's device. Learn more about `SecurityError` exceptions in Mozilla's `MediaDevice.getUserMedia()` [reference page](https://developer.mozilla.org/en-US/docs/Web/API/MediaDevices/getUserMedia#exceptions).                                                                                              |
| `MEDIA_STREAM_TYPE`                     | A `TypeError` exception occurred when attempting to retrieve media data from the user's device. Learn more about `TypeError` exceptions in Mozilla's `MediaDevice.getUserMedia()` [reference page](https://developer.mozilla.org/en-US/docs/Web/API/MediaDevices/getUserMedia#exceptions).                                                                                                      |
| `SERVER_CUSTOMER_NOT_FOUND`             | The customer does not exist. Contact Support.                                                                                                                                                                                                                                                                                                                                                   |
| `SERVER_INTERNAL_ERROR`                 | Internal error; contact Support                                                                                                                                                                                                                                                                                                                                                                 |
| `SERVER_RECOGNITION_FAILED`             | Biometric error. Contact Support                                                                                                                                                                                                                                                                                                                                                                |
| `SERVER_USER_LOCKED_OUT`                | The user is locked out of the server.                                                                                                                                                                                                                                                                                                                                                           |
| `SESSION_MANAGER_NOT_NULL`              | Integration error. The attempt must complete or be disposed using `deleteKeylessAuth` or `deleteKeylessEnroll`. Otherwise, calling `createKeylessAuth` or `createKeylessEnroll` triggers this error                                                                                                                                                                                             |
| `SESSION_MANAGER_NULL`                  | Integration error. The `createKeylessAuth` or `createKeylessEnroll` functions must be called before using `createKeylessVideoStream`, `createKeylessVideoElement` or `openKeylessWebSocketConnection`.This error also occurs when you don't have the proper security headers to run Web Assembly in your server. Learn more in [Security headers](web-sdk-prerequisites.html#security-headers). |
| `EXCEPTION`                             | Generic web assembly error. Contact Support.                                                                                                                                                                                                                                                                                                                                                    |
| `RUNTIME_VIOLATION`                     | Tampering detected. Contact Support.                                                                                                                                                                                                                                                                                                                                                            |
| `SYMBOL_DESCRIPTION_UNSET`              | Internal error; contact Support                                                                                                                                                                                                                                                                                                                                                                 |
| `SESSION_ID_UNSET`                      | Internal error; contact Support                                                                                                                                                                                                                                                                                                                                                                 |
| `CUSTOMER_UNSET`                        | Integration error. The `customer.name` option is either undefined or empty                                                                                                                                                                                                                                                                                                                      |
| `USERNAME_UNSET`                        | Integration error. The `username` option is either undefined or empty                                                                                                                                                                                                                                                                                                                           |
| `WEB_ASSEMBLY_ABORTED`                  | The web assembly runtime aborted on an unexpected condition. Contact Support.                                                                                                                                                                                                                                                                                                                   |
| `WEB_ASSEMBLY_FACTORY_FAILED`           | The web assembly initialization failed. Contact Support.                                                                                                                                                                                                                                                                                                                                        |
| `WEB_ASSEMBLY_IMPORT_FAILED`            | The web assembly import failed. Contact Support.                                                                                                                                                                                                                                                                                                                                                |
| `WEB_ASSEMBLY_NOT_READY`                | Integration error. The `importKeylessWebAssemblyModule` was not called before using other APIs.                                                                                                                                                                                                                                                                                                 |
| `WEB_ASSEMBLY_MODULE_NOT_FOUND`         | Internal error; contact Support.                                                                                                                                                                                                                                                                                                                                                                |
| `USER_LOCKOUT_EXPIRATION_UNSET`         | Internal error; contact Support.                                                                                                                                                                                                                                                                                                                                                                |
| `SERVER_INVALID_REQUEST`                | Internal error; contact Support.                                                                                                                                                                                                                                                                                                                                                                |
| `SERVER_INVALID_RESPONSE`               | Internal error; contact Support.                                                                                                                                                                                                                                                                                                                                                                |
| `SESSION_DATABASE_ERROR`                | Internal error; contact Support.                                                                                                                                                                                                                                                                                                                                                                |
| `SESSION_MEDIA_STREAM_TIMEOUT`          | The user failed to pass the quality filters in time.                                                                                                                                                                                                                                                                                                                                            |
| `SESSION_MEDIA_STREAM_UNSET`            | Integration error. The `createKeylessVideoElement` function must be called after `createKeylessVideoStream`.                                                                                                                                                                                                                                                                                    |
| `SERVICE_URL_PARSE_FAILED`              | Integration error. `The service.url` option is not a valid URL.                                                                                                                                                                                                                                                                                                                                 |
| `SERVICE_URL_UNSET`                     | Integration error. The `service.url` option is either undefined or empty.                                                                                                                                                                                                                                                                                                                       |
| `SLUG_UNSUPPORTED`                      | Internal error; contact Support.                                                                                                                                                                                                                                                                                                                                                                |

## Web component error handling

Web components inherit errors from the `@keyless/sdk-web` library. Use the [Error reference](#error-reference) to diagnose errors in web components.

The following example shows how to handle an error event within a `<kl-auth>` web component:

> **Collapse: Details**
>
> ```javascript
> <!doctype html>
> <html lang="en">
>   <head>
>     <meta charset="UTF-8" />
>     <meta name="viewport" content="width=device-width, initial-scale=1.0" />
>     <title>Auth</title>
>     <style>
>       * {
>         box-sizing: border-box;
>       }
>
>       body {
>         align-items: center;
>         display: flex;
>         justify-content: center;
>         margin: 0;
>         min-height: 100vh;
>         padding: 8px;
>       }
>
>       kl-auth {
>         border: 1px solid lightgray;
>       }
>     </style>
>   </head>
>   <body>
>     <kl-auth
>       authorization-token="USER_AUTHORIZATION_FROM_CUSTOMER"
>       customer="CUSTOMER_NAME"
>       enable-camera-instructions
>       lang="en"
>       size="375"
>       theme="light"
>       transaction-data='DATA_FROM_CUSTOMER_SERVER_TO_BE_SIGNED'
>       username="USERNAME"
>       service-url="KEYLESS_AUTHENTICATION_SERVICE_URL"
>     ></kl-auth>
>     <script src="@keyless/sdk-web-components/index.js" type="module"></script>
>     <script>
>       const auth = document.querySelector('kl-auth')
>
>       auth.addEventListener('error', (event) => {
>         // will print the error code
>         console.error(event.message)
>       })
>     </script>
>   </body>
> </html>
> ```

The SDK extends the `ErrorEvent` to provide the error code inside the error message and to include additional errors:

```javascript
enum KeylessComponentsError {
  QUEUE_UNSET = 'QUEUE_UNSET',
  SYMBOL_UNSET = 'SYMBOL_UNSET',

}
```

Each `KeylessComponentsError` error represents an internal error. Contact Support.

---

---
title: Getting started with the PingOne Recognize Web SDK
description: The PingOne Recognize Web SDK helps authenticate people, not just devices.
component: recognize
page_id: recognize:web-sdk:web-sdk-getting-started
canonical_url: https://docs.pingidentity.com/recognize/web-sdk/web-sdk-getting-started.html
llms_txt: https://docs.pingidentity.com/recognize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  using-the-pingone-recognize-web-sdk: Using the PingOne Recognize Web SDK
  next-steps: Next steps
---

# Getting started with the PingOne Recognize Web SDK

## Using the PingOne Recognize Web SDK

To learn how to use the Web SDK to embed biometric authentication in your web-based applications and devices:

1. Understand how the PingOne Recognize [components interact](web-sdk-introduction-components.html) with your application server.

2. Understand how typical [authentication flows](web-sdk-introduction-integration-flows.html) interact with your application.

3. Follow the [getting started](web-sdk-guide-getting-started.html) guide.

## Next steps

Learn about authentication and enrollment using the [Identity Verification (IDV) Bridge](../idv-bridge/idv-bridge-saas.html).

---

---
title: Getting started with the Web SDK
description: "\"Shows how to get started with the PingOne Recognize Web SDK.\""
component: recognize
page_id: recognize:web-sdk:web-sdk-guide-getting-started
canonical_url: https://docs.pingidentity.com/recognize/web-sdk/web-sdk-guide-getting-started.html
llms_txt: https://docs.pingidentity.com/recognize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  before-you-begin: Before you begin
  keys: Keys
  installation: Installation
---

# Getting started with the Web SDK

In this short guide, you will learn how to integrate the PingOne Recognize Web SDK in your web application, and enroll and authenticate users through the PingOne Recognize platform.

Take time to become familiar with the authentication [components](web-sdk-introduction-components.html) and common authentication [integration flows](web-sdk-introduction-integration-flows.html).

## Before you begin

Verify the [prerequisite requirements](web-sdk-prerequisites.html) before you begin.

## Keys

Make sure you have all the required keys.

* `CLOUDSMITH_TOKEN` to download the Web SDK from cloudsmith repository

* `CUSTOMER_NAME` to define the customer

* `KEYLESS_AUTHENTICATION_SERVICE_URL` to establish a connection

## Installation

To set up the Web SDK, use a package manager to install the SDK locally or load it from the PingOne Recognize content distribution network (CDN).

* Package manager

* CDN

First, authenticate to the PingOne Recognize Cloudsmith repository.

Create a file called `.npmrc` in the root folder of your project and then add the following line:

```none
@keyless:registry=https://npm.cloudsmith.io/keyless/partners/
```

Use your PingOne Recognize authorization token to launch this command on your terminal:

```none
npm config set //npm.cloudsmith.io/keyless/partners/:_authToken=CLOUDSMITH_TOKEN
```

Use the following command to install `@keyless/sdk-web`:

```none
npm install @keyless/sdk-web@3.0.0
```

You can also use alternate package managers.

Use the following command to install `@keyless/sdk-web-components`:

```none
npm install @keyless/sdk-web-components@3.0.0
```

To set up content distribution network (CDN) access:

|   |                                                            |
| - | ---------------------------------------------------------- |
|   | You should not use these scripts without integrity checks. |

```html
<script type="importmap">
{
"integrity": {
"https://d3hz8ozgrmhn4r.cloudfront.net/sdk-web-components/3.0.0/index.js": "sha512-9an20J/GVcx4T2lpmke1Y17U/tXnDzgpaLT48D3zA1CQgjOObOQX3pRqn3FjDi305iFrIqYJyFMm+JDw1tzt/Q==",
"https://d3hz8ozgrmhn4r.cloudfront.net/sdk-web-components/3.0.0/wasm.js": "sha512-dHaXKpUC0k7IamjAUUH4u4/3980WmRnW5+IFxXLEFxcK8g8xId2Zu1rsSqRx2GdRsktQuNmTSADqsLOtMbBmzw==",
"https://d3hz8ozgrmhn4r.cloudfront.net/sdk-web-components/3.0.0/pthreads/wasm.js": "sha512-PLlzx/8ikPMIiH5hv1a0aAOvvHxQl8Oz0GfpdquQ/vTwqEbriUEcFPu0v9s/haAprT+x/mDagwx3BFIwfww/BQ=="
}
}
</script>
<script
crossorigin="anonymous"
integrity="sha512-9an20J/GVcx4T2lpmke1Y17U/tXnDzgpaLT48D3zA1CQgjOObOQX3pRqn3FjDi305iFrIqYJyFMm+JDw1tzt/Q=="
src="https://d3hz8ozgrmhn4r.cloudfront.net/sdk-web-components/3.0.0/index.js"
type="module"
></script>
```

---

---
title: Integration flows
description: "\"Describes how PingOne Recognize components interact with applications.\""
component: recognize
page_id: recognize:web-sdk:web-sdk-introduction-integration-flows
canonical_url: https://docs.pingidentity.com/recognize/web-sdk/web-sdk-introduction-integration-flows.html
llms_txt: https://docs.pingidentity.com/recognize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  introduction: Introduction
  integration-overview: Integration overview
  live-enrollment-flow: Live enrollment flow
  authentication-flow: Authentication flow
  authentication-in-a-web-application: Authentication in a web application
  pingone-recognize-web-components: PingOne Recognize web components
  pingone-recognize-web-sdk: PingOne Recognize Web SDK
  pingone-recognize-authentication-service: PingOne Recognize authentication service
---

# Integration flows

## Introduction

Learn how the PingOne Recognize Web SDK components can be integrated into a web application and backend server, to enable biometric authentication.

## Integration overview

### Live enrollment flow

To authenticate with PingOne Recognize, a user must first enroll their biometric template.

PingOne Recognize enrollment registers the user's biometric features in a privacy-preserving manner using a variety of methods supported by the Web SDK.

### Authentication flow

The most common authentication scenarios for the PingOne Recognize Web SDK are:

* access to a web application

* authorization as a second factor

### Authentication in a web application

In this scenario, the user is using a web app to access a resource that requires strong authentication. Because the web app uses the PingOne Recognize Web SDK to connect to the PingOne Recognize Authentication Service, the user authenticates successfully once they pass liveness and recognition checks.

## PingOne Recognize web components

PingOne Recognize Web is composed of two main elements:

* PingOne Recognize Web SDK

* PingOne Recognize Authentication Service

### PingOne Recognize Web SDK

The PingOne Recognize Web SDK supports all baseline browsers, and exposes API methods to interact with the PingOne Recognize Privacy-Preserving Network to perform the following actions:

* Enroll a user

* Authenticate

### PingOne Recognize authentication service

The PingOne Recognize SaaS backend offers APIs which can be used to perform specific operations through backend-to-backend calls. For example, you can enroll users individually or in bulk using selfies captured by other services. To learn more, refer to [IDV Bridge SaaS](../idv-bridge/idv-bridge-saas.html).

---

---
title: Localization
description: "\"Shows how to use localization packs to support multiple languages with the PingOne Recognize Web SDK.\""
component: recognize
page_id: recognize:web-sdk:web-sdk-reference-localization
canonical_url: https://docs.pingidentity.com/recognize/web-sdk/web-sdk-reference-localization.html
llms_txt: https://docs.pingidentity.com/recognize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  component-attributes: Component attributes
  localizationpack-interface: LocalizationPack interface
  default-english-language-pack: Default English language pack
  example-customizing-instruction-heading: "Example: Customizing instruction heading"
---

# Localization

The text in PingOne Recognize Web SDK components can be localized to other languages.

Use the `lang` attribute to set the default language of a Web SDK component.

## Component attributes

The `<kl-auth>`, `<kl-auth-dialog>`, `<kl-enroll>`, and `<kl-enroll-dialog>` components each support two attributes that help manage localization:

|                                                   |                                 |                                                                                                                                                                                             |
| ------------------------------------------------- | ------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Attribute**                                     | **Type**                        | **Description**                                                                                                                                                                             |
| `localization-packs`, `localizationPacks`         | `LocalizationPack[]`            | Pass an array of localization packs to this attribute. If a localization pack uses a language that already exists, the new values replace values defined in the existing localization pack. |
| `localization-variables`, `localizationVariables` | `Record<number \| string, any>` | Localization variables represent dynamic values to be inserted into existing localization strings by replacing the `{variable}` with the new text.                                          |

Customize component text values using custom localization pack arrays and dynamic localization variables.

### LocalizationPack interface

A localization pack is an array of objects declared using the following types:

```javascript
interface LocalizationPack {
    data: LocalizationPackData;
    language: string;
}

interface LocalizationPackData {
    [key: string]: string | LocalizationPackData;
}
```

### Default English language pack

The following example shows the default PingOne Recognize language pack and serves as a reference for customization:

> **Collapse: Details**
>
> ```javascript
> {
>   auth: {
>     step: {
>       bootstrap: {
>         headline: 'Authentication Process',
>         text: 'Take a selfie to authenticate through Keyless on the platform.'
>       },
>       'camera-instructions': {
>         headline: 'Authentication Process',
>         text: 'Take a selfie to authenticate through Keyless on the platform.',
>         button: "All set. I'm ready"
>       },
>       'camera-permission': {
>         prompt: {
>           headline: 'Allow Camera Access',
>           text: 'We need access to your camera to authenticate you. Please allow the browser to access your camera.',
>           button: 'Continue'
>         },
>         granted: {
>           headline: 'Allow Camera Access',
>           text: 'We need access to your camera to authenticate you. Please allow the browser to access your camera.',
>           button: 'Continue'
>         },
>         denied: {
>           headline: 'Camera Access Denied',
>           text: 'Looks like you denied camera access on this website, we need access to your camera to authenticate you.\n\nPlease allow the browser to access your camera.',
>           button: 'Retry'
>         }
>       },
>       'camera-stream-boot': {
>         tip: 'Preparing your camera'
>       },
>       done: {
>         headline: 'Authentication Successful',
>         text: 'You can now proceed to the platform.'
>       },
>       error: {
>         headline: 'Something went wrong',
>         text: 'We were unable to authenticate you. {message} <code style="font-size: 12px">[{code}]</code>',
>         button: 'Retry'
>       },
>       'microphone-permission': {
>         prompt: {
>           headline: 'Allow Microphone Access',
>           text: 'We need access to your microphone to authenticate you. Please allow the browser to access your microphone.',
>           button: 'Continue'
>         },
>         granted: {
>           headline: 'Allow Microphone Access',
>           text: 'We need access to your microphone to authenticate you. Please allow the browser to access your microphone.',
>           button: 'Continue'
>         },
>         denied: {
>           headline: 'Microphone Access Denied',
>           text: 'Looks like you denied microphone access on this website, we need access to your microphone to authenticate you.\n\nPlease allow the browser to access your microphone.',
>           button: 'Retry'
>         }
>       },
>       'server-computation': {
>         headline: 'Authenticating...',
>         text: 'Your selfie was captured correctly, we are processing your photo'
>       },
>       'stm-choice': {
>         headline: 'Authentication Process',
>         text: 'Take a selfie to authenticate through Keyless on the platform.',
>         button: 'Continue on Phone',
>         secondary_button: 'Authenticate on Desktop'
>       },
>       'stm-qrcode': {
>         headline: 'Scan the QR Code',
>         text: 'Scan the QR code with your phone to continue the authentication process.',
>         button: {
>           false: 'Copy Link',
>           true: 'Copied to Clipboard'
>         }
>       }
>     }
>   },
>   camera_instructions: {
>     alignment: 'Center your face in the frame',
>     look: 'Look directly at the screen',
>     lighting: 'Ensure you are in a well-lit area',
>     accessories: 'Remove any eyewear or hats'
>   },
>   camera_select: {
>     headline: 'Select a Camera',
>     text: 'We detected more than one webcam connected to your device. Choose one for the process.'
>   },
>   camera_tip: {
>     /**
>      * Client
>      */
>     FaceAbsent: 'Show your face in the frame',
>     FaceMultiple: 'Show only one face in the frame',
>     FaceOffCenter: 'Center your face in the frame',
>     FacePartial: 'Show your full face in the frame',
>     FaceTooLarge: 'Move your face farther from the device',
>     FaceTooSmall: 'Move your face closer to the device',
>     /**
>      * Server
>      */
>     eyes_closed: 'Open your eyes',
>     face_angle_too_large: 'Look into the camera',
>     face_is_occluded: 'Remove any obstructions from your face',
>     face_missing: 'Show your face in the frame',
>     face_multiple: 'Show only one face in the frame',
>     face_partial: 'Show your full face in the frame',
>     face_too_close: 'Move your face farther from the device',
>     face_too_small: 'Move your face closer to the device',
>     image_black_and_white: 'Move in a well-lit area',
>     image_metadata_low_light: 'Move in a well-lit area',
>     no_movement_from_device: 'Pick up your device',
>     no_movement_from_subject: 'Tilt your face slightly',
>     /**
>      * Shared
>      */
>     none: 'Keep your face still'
>   },
>   enroll: {
>     step: {
>       bootstrap: {
>         headline: 'Enrollment Process',
>         text: 'Take a selfie to create an account on Keyless and easily register on the platform.'
>       },
>       'camera-instructions': {
>         headline: 'Enrollment Process',
>         text: 'Take a selfie to create an account on Keyless and easily register on the platform.',
>         button: 'Continue'
>       },
>       'camera-permission': {
>         prompt: {
>           headline: 'Allow Camera Access',
>           text: 'We need access to your camera to create your account. Please allow the browser to access your camera.',
>           button: 'Continue'
>         },
>         granted: {
>           headline: 'Allow Camera Access',
>           text: 'We need access to your camera to create your account. Please allow the browser to access your camera.',
>           button: 'Continue'
>         },
>         denied: {
>           headline: 'Camera Access Denied',
>           text: 'Looks like you denied camera access on this website, we need access to your camera to create your account.\n\nPlease allow the browser to access your camera.',
>           button: 'Retry'
>         }
>       },
>       'camera-stream-boot': {
>         tip: 'Preparing your camera'
>       },
>       done: {
>         headline: 'Account created',
>         text: 'You can now access and authenticate simply by using your face.'
>       },
>       error: {
>         headline: 'Something went wrong',
>         text: 'We were unable to create your account. {message} <code style="font-size: 12px">[{code}]</code>',
>         button: 'Retry'
>       },
>       'microphone-permission': {
>         prompt: {
>           headline: 'Allow Microphone Access',
>           text: 'We need access to your microphone to create your account. Please allow the browser to access your microphone.',
>           button: 'Continue'
>         },
>         granted: {
>           headline: 'Allow Microphone Access',
>           text: 'We need access to your microphone to create your account. Please allow the browser to access your microphone.',
>           button: 'Continue'
>         },
>         denied: {
>           headline: 'Microphone Access Denied',
>           text: 'Looks like you denied microphone access on this website, we need access to your microphone to create your account.\n\nPlease allow the browser to access your microphone.',
>           button: 'Retry'
>         }
>       },
>       'server-computation': {
>         headline: 'Crafting your private key',
>         text: 'Hold on, it will just take a moment'
>       },
>       'stm-choice': {
>         headline: 'Enrollment Process',
>         text: 'Take a selfie to create an account on Keyless and easily register on the platform.',
>         button: 'Continue on Phone',
>         secondary_button: 'Enroll on Desktop'
>       },
>       'stm-qrcode': {
>         headline: 'Scan the QR Code',
>         text: 'Please scan the QR code with your phone to continue the enrollment process.',
>         button: {
>           false: 'Copy Link',
>           true: 'Copied to Clipboard'
>         }
>       }
>     }
>   },
>   error: {
>     /**
>      * Collector Errors
>      */
>     FRAME_RESULTS_SET_UNSET: 'Please contact our support.',
>     OPTIONS_UNSET: 'Please contact our support.',
>     VIDEO_ELEMENT_UNSET: 'Please contact our support.',
>     VIDEO_ELEMENT_EVENT_LISTENERS_UNSET: 'Please contact our support.',
>     WEB_SOCKET_MESSAGE_SET_UNSET: 'Please contact our support.',
>
>     /**
>      * Media Device Errors
>      */
>     MEDIA_DEVICES_EMPTY_AUDIO_INPUT_LABEL: 'Please allow the browser to access your microphone and try again.',
>     MEDIA_DEVICES_EMPTY_VIDEO_INPUT_LABEL: 'Please allow the browser to access your camera and try again.',
>     MEDIA_DEVICES_NO_VIDEO_INPUTS: 'No camera was found. Please connect a camera and try again.',
>
>     /**
>      * Media Stream Errors
>      */
>     MEDIA_STREAM_ABORT: 'Please make sure your camera is not being used by another application and try again.',
>     MEDIA_STREAM_INVALID_STATE: 'Please make sure your camera is not being used by another application and try again.',
>     MEDIA_STREAM_NOT_ALLOWED: 'Please make sure you granted camera access permission and that no other application is using your camera, then try again.',
>     MEDIA_STREAM_NOT_FOUND: 'No camera was found. Please connect a camera and try again.',
>     MEDIA_STREAM_NOT_READABLE: 'Please make sure your camera is not being used by another application and try again.',
>     MEDIA_STREAM_OVERCONSTRAINED: 'The camera does not meet our minimum requirements. Please use a different camera and try again.',
>     MEDIA_STREAM_SECURITY: 'Please contact our support.',
>     MEDIA_STREAM_TYPE: 'Please contact our support.',
>     MEDIA_STREAM_UNSET: 'Please contact our support.',
>
>     /**
>      * Server Errors
>      */
>     SERVER_CUSTOMER_NOT_FOUND: 'Please contact our support.',
>     SERVER_FACE_DOES_NOT_MATCH: 'Make sure you are in a well-lit environment, possibly without any eyewear or hats.',
>     SERVER_FORBIDDEN: 'Please try again or contact our support if the problem persists.',
>     SERVER_IMAGE_ENCRYPT_FAILED: 'Please contact our support.',
>     SERVER_INTERNAL_ERROR: 'Please try again or contact our support if the problem persists.',
>     SERVER_NO_ATTEMPTS_LEFT: 'Please contact our support.',
>     SERVER_RECOGNITION_FAILED: {
>       eyes_closed: 'Make sure your eyes are open, possibly without any eyewear.',
>       face_angle_too_large: 'Make sure you are looking into the camera.',
>       face_is_occluded: 'Make sure to remove any obstructions from your face, possibly any eyewear or hats.',
>       face_missing: 'Make sure to show your face in the frame, possibly without any eyewear or hats.',
>       face_multiple: 'Make sure to show only one face in the frame, possibly with a plain background.',
>       face_partial: 'Make sure to show your full face in the frame.',
>       face_too_close: 'Make sure to move your face farther from the device.',
>       face_too_small: 'Make sure to move your face closer to the device.',
>       image_black_and_white: 'Make sure you are in a well-lit environment.',
>       image_metadata_low_light: 'Make sure you are in a well-lit environment.',
>       no_movement_from_device: 'Make sure to pick up your device.',
>       no_movement_from_subject: 'Make sure to tilt your face slightly every now and then.',
>       none: 'Make sure you are in a well-lit environment, possibly without any eyewear or hats.'
>     },
>     SERVER_TIMEOUT: 'Please try again or contact our support if the problem persists.',
>     SERVER_UNAVAILABLE_SERVICE: 'Please try again or contact our support if the problem persists.',
>     SERVER_UNPROCESSABLE_EVENT: 'Please contact our support.',
>     SERVER_USER_ALREADY_ENROLLED: 'The account {username} already exists.',
>     SERVER_USER_LOCKED_OUT: 'Too many attempts. You can try again in {lockout_expiration}.',
>     SERVER_USER_NOT_FOUND: 'The account {username} does not exist.',
>     SERVER_VALIDATION_FAILED: 'Please contact our support.',
>
>     /**
>      * Session Manager Errors
>      */
>     SESSION_MANAGER_NOT_NULL: 'Please contact our support.',
>     SESSION_MANAGER_NULL: 'Please contact our support.',
>
>     /**
>      * Special Errors
>      */
>     CREATE_MEDIA_STREAM_ARGS_UNSET: 'Please contact our support.',
>     EXCEPTION: 'Please contact our support.',
>     RUNTIME_VIOLATION: 'Please contact our support.',
>     SYMBOL_DESCRIPTION_UNSET: 'Please contact our support.',
>
>     /**
>      * Storage Errors
>      */
>     SESSION_ID_UNSET: 'Please contact our support.',
>
>     /**
>      * Verify Connect Options Errors
>      */
>     CUSTOMER_UNSET: 'Please contact our support.',
>     KEY_DECODE_FAILED: 'Please contact our support.',
>     KEY_UNSET: 'Please contact our support.',
>     KEY_ID_UNSET: 'Please contact our support.',
>     USERNAME_UNSET: 'Please contact our support.',
>     WEB_SOCKET_URL_PARSE_FAILED: 'Please contact our support.',
>     WEB_SOCKET_URL_UNSET: 'Please contact our support.',
>
>     /**
>      * Web Assembly Errors
>      */
>     WEB_ASSEMBLY_ABORTED: 'Please try again or contact our support if the problem persists.',
>     WEB_ASSEMBLY_FACTORY_FAILED: 'Please contact our support.',
>     WEB_ASSEMBLY_IMPORT_FAILED: 'Please contact our support.',
>     WEB_ASSEMBLY_NOT_READY: 'Please contact our support.',
>     WEB_ASSEMBLY_MODULE_NOT_FOUND: 'Please contact our support.',
>
>     /**
>      * Web Socket Errors
>      */
>     WEB_SOCKET_ERROR: 'Please try again or contact our support if the problem persists.',
>     WEB_SOCKET_OPEN: 'Please try again or contact our support if the problem persists.',
>     WEB_SOCKET_TIMEOUT: 'Please try again or contact our support if the problem persists.',
>     WEB_SOCKET_UNEXPECTED_CLOSE: 'Please try again or contact our support if the problem persists.',
>
>     /**
>      * Flow Errors
>      */
>     QUEUE_UNSET: 'Please contact our support.',
>     SYMBOL_UNSET: 'Please contact our support.',
>
>     /**
>      * Cancel or Close Errors
>      */
>     NONCANCELABLE: 'Please try again or contact our support if the problem persists.'
>   }
> }
> ```

When creating custom language packs, remember that the `language` specified in the pack must match the value specified in the `lang` attribute of the web component. Otherwise, the component ignores the custom language pack.

### Example: Customizing instruction heading

This example customizes the title of the camera instructions for an authorization component:

> **Collapse: Details**
>
> ```javascript
> <!doctype html>
> <html lang="en">
>   <head>
>     <meta charset="UTF-8" />
>     <meta name="viewport" content="width=device-width, initial-scale=1.0" />
>     <title>Auth</title>
>     <style>
>       * {
>         box-sizing: border-box;
>       }
>
>       body {
>         align-items: center;
>         display: flex;
>         justify-content: center;
>         margin: 0;
>         min-height: 100vh;
>         padding: 8px;
>       }
>
>       kl-auth {
>         border: 1px solid lightgray;
>       }
>     </style>
>   </head>
>   <body>
>     <kl-auth
>       authorization-token="USER_AUTHORIZATION_FROM_CUSTOMER"
>       customer="CUSTOMER_NAME"
>       enable-camera-instructions
>       key="IMAGE_ENCRYPTION_PUBLIC_KEY"
>       key-id="IMAGE_ENCRYPTION_KEY_ID"
>       lang="en"
>       size="375"
>       theme="light"
>       transaction-data='DATA_FROM_CUSTOMER_SERVER_TO_BE_SIGNED'
>       username="USERNAME"
>       ws-url="KEYLESS_AUTHENTICATION_SERVICE_URL"
>     ></kl-auth>
>     <script src="@keyless/sdk-web-components/index.js"></script>
>     <script>
>       const auth = document.querySelector('kl-auth')
>
>       auth.localizationPacks = [
>         {
>           data: {
>             auth: {
>               step: {
>                 'camera-instructions': {
>                   headline: 'Custom Camera Instructions Title',
>                 }
>               }
>             }
>           },
>           language: 'en'
>         }
>       ]
>     </script>
>   </body>
> </html>
> ```

---

---
title: Lockout policy
description: "\"Explains the PingOne Recognize lockout policy, what it means for users, and how to customize it.\""
component: recognize
page_id: recognize:web-sdk:web-sdk-reference-lockout-policy
canonical_url: https://docs.pingidentity.com/recognize/web-sdk/web-sdk-reference-lockout-policy.html
llms_txt: https://docs.pingidentity.com/recognize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  lockout-settings-and-options: Lockout settings and options
  how-it-works: How it works
  lockout-policy-application: Lockout policy application
  when-users-are-suspended: When users are suspended
---

# Lockout policy

Users have a limited number of attempts to authorize access within a limited period of time. When authorization failures exceed this limit, PingOne Recognize blocks further authentication attempts for a period of time.

Three options control the limits and time periods involved.

## Lockout settings and options

|                            |                                                                                                                                       |                              |
| -------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------- |
| **Lockout configurations** | **Description**                                                                                                                       | **Default (SaaS customers)** |
| Max failed attempts        | Number of authorization failures allowed before lockout.                                                                              | 5                            |
| Time window                | The window of time (in seconds) where multiple authorization failures lead to lockout. Successful authentication resets this to zero. | 600s (10 minutes)            |
| Suspension period          | Number of seconds the user must wait before next authorization attempt.                                                               | 600s (10 minutes)            |

On-premises deployments can customize the defaults.

## How it works

The lockout policy is applied for each user of a PingOne Recognize deployment, based on an internal user ID.

Lockouts apply across the deployment, which means that a user locked out by a Web SDK app is also locked out of apps using the Mobile SDK. Developers should track authentication errors and provide appropriate responses.

Failed authentications affect the entire deployment. Any successful authentication resets the failure count to zero (`0`).

The lockout policy cannot be disabled. You can set values that effectively allow unlimited failures. To learn more, contact Support.

### Lockout policy application

The lockout policy applies only to authentication failures.

Because PingOne Recognize generates internal IDs only when authentication succeeds, the policy doesn't apply to enrollment failures.

### When users are suspended

When users are suspended, authorization attempts fail with `USER_LOCKED_OUT` errors.

When this happens:

* The user must wait until the suspension period expires. PingOne Recognize cannot cancel or bypass the suspension.

* Additional authentication failures do not affect an active suspension period.

* During the suspension period, PingOne Recognize blocks biometric authentication for the user. PingOne Recognize doesn't consume additional circuits during suspension.

---

---
title: Multi-threading
description: "\"Shows how to enable multi-threading in PingOne Recognize using the Web SDK.\""
component: recognize
page_id: recognize:web-sdk:web-sdk-reference-multi-threaded
canonical_url: https://docs.pingidentity.com/recognize/web-sdk/web-sdk-reference-multi-threaded.html
llms_txt: https://docs.pingidentity.com/recognize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  enabling-multi-threading: Enabling multi-threading
  headless: Headless
  web-components: Web components
  security-headers: Security headers
---

# Multi-threading

Starting with v2.2, PingOne Recognize is single-threaded by default. Enable multi-threading to improve performance.

## Enabling multi-threading

PingOne Recognize supports WebAssembly (WASM) POSIX threads (pthreads). Enable multi-threading by adding the appropriate flag, as shown in the following examples:

### Headless

```javascript
await importKeylessWebAssemblyModule({
  ...,
  pthreads: true
})
```

### Web components

```html
<kl-auth
...
enable-wasm-pthreads
></kl-auth>
```

## Security headers

Multi-threading requires two security headers. If either header is missing or has an incorrect value, you cannot enable multi-threading.

|                              |                |
| ---------------------------- | -------------- |
| Name                         | Value          |
| Cross-Origin-Embedder-Policy | `require-corp` |
| Cross-Origin-Opener-Policy   | `same-origin`  |

When loading resources from external domains, use the `crossorigin` attribute. To learn more, refer to [Cross-Origin-Embedder-Policy: Avoiding COEP Blockage with CORS](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Cross-Origin-Embedder-Policy#avoiding_coep_blockage_with_cors)

---

---
title: Prerequisites
description: "\"Describes prerequisites for using the PingOne Recognize Web SDK.\""
component: recognize
page_id: recognize:web-sdk:web-sdk-prerequisites
canonical_url: https://docs.pingidentity.com/recognize/web-sdk/web-sdk-prerequisites.html
llms_txt: https://docs.pingidentity.com/recognize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  run-as-module: Run as module
  webassembly-bundling: WebAssembly bundling
  security-headers: Security headers
---

# Prerequisites

The PingOne Recognize Web SDK requires three conditions, involving module loading, bundling, and the use of security headers.

## Run as module

The Web SDK includes two modules:

* `@keyless/sdk-web`

* `@keyless/sdk-web-components`

The entry point for each module is `index.js`.

Each module must be loaded as a JavaScript module, as shown in the following examples:

* Headless

* Web components

```html
<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Keyless Web SDK</title>
  </head>
  <body>
    <script type="module">
      import { ... } from '@keyless/sdk-web/index.js'
    </script>
  </body>
</html>
```

```html
<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Keyless Web SDK Components</title>
  </head>
  <body>
    <kl-auth-or-enroll></kl-auth-or-enroll>
    <script src="@keyless/sdk-web-components/index.js" type="module"></script>
  </body>
</html>
```

## WebAssembly bundling

When using a bundler to build your web app, verify that it supports `.wasm` files.

## Security headers

|   |                                                                                                                                   |
| - | --------------------------------------------------------------------------------------------------------------------------------- |
|   | This requirement applies only when using multi-threading. Learn more in [Multi-threading](web-sdk-reference-multi-threaded.html). |

The Web Assembly module requires two security headers to run. If the header values are incorrect, you won't be able to use the PingOne Recognize Web SDK.

| Name                         | Value        |
| ---------------------------- | ------------ |
| Cross-Origin-Embedder-Policy | require-corp |
| Cross-Origin-Opener-Policy   | same-origin  |

Common issues include missing headers or headers with invalid values.

When loading resources from an external domain, use the `crossorigin` attribute. For details, refer to [Cross-Origin-Embedder-Policy: Avoiding COEP Blockage With CORS](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Cross-Origin-Embedder-Policy#avoiding_coep_blockage_with_cors).

---

---
title: Signing transactions
description: "\"Shows how to sign PingOne Recognize transaction data after successful authentication or enrollment.\""
component: recognize
page_id: recognize:web-sdk:web-sdk-reference-signing-transactions
canonical_url: https://docs.pingidentity.com/recognize/web-sdk/web-sdk-reference-signing-transactions.html
llms_txt: https://docs.pingidentity.com/recognize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  headless-integration: Headless integration
  web-component-integration: Web component integration
  verifying-the-transaction: Verifying the transaction
---

# Signing transactions

The PingOne Recognize Web SDK can digitally sign transaction data when PingOne Recognize authentication or enrollment actions succeed.

The signed transaction is a JSON web token (JWT) that the server can verify, which ensures:

* That PingOne Recognize completed the original operation.

* The transaction data is intact.

## Headless integration

To sign transaction data without using a user interface, start with one of the baseline integrations:

* For authentication, use [Headless authentication integration](web-sdk-guide-authentication.html#headless-integration).

* For enrollment, use [Headless enrollment integration](web-sdk-guide-enrollment.html#headless-integration).

Next, include the transaction data payload when using `openKeylessWebSocketConnection` to open a web socket:

```javascript
await openKeylessWebSocketConnection(sym, {
  ...,
  transaction: {
    data: TRANSACTION_DATA
  }
})
```

Finally, add an event listener to the `finished` event of your web socket:

```javascript
addKeylessEventListener(sym, 'finished', (event) => {
  // will log the JWT
  console.log(event.data.JWT)
})
```

## Web component integration

To sign transaction data using web components, start with a baseline integration:

* For authentication, use a [Web component authentication integration](web-sdk-guide-authentication.html#component-integration).

* For enrollment, use a [Web component enrollment integration](web-sdk-guide-enrollment.html#component-integration).

Next, add a `transaction-data` attribute to your web component:

```javascript
<kl-auth-or-enroll
  ...
  transaction-data="TRANSACTION_DATA"
></kl-auth-or-enroll>
```

Finally, add an event listener to the `finished` event of your web component:

```javascript
auth_or_enroll.addEventListener('finished', (event) => {
  // will log the JWT
  console.log(event.detail.JWT)
})
```

## Verifying the transaction

There are two ways to verify the transaction data:

1. Use `GET /v2/verify-jwt/public-key` to retrieve and import the customer public key. Then, use the response `result` to verify the transaction data.

2. Use `POST /v2/verify-jwt` to send the transaction data in the request body and then check the result.

Run these tasks on the backend server to avoid leaking keys or other sensitive data.

---

---
title: User authorization
description: Web SDK supports a first factor provided by the integrator during the flow.
component: recognize
page_id: recognize:web-sdk:web-sdk-reference-user-authorization
canonical_url: https://docs.pingidentity.com/recognize/web-sdk/web-sdk-reference-user-authorization.html
llms_txt: https://docs.pingidentity.com/recognize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  update-customer-configuration: Update Customer Configuration
  issuing-a-token: Issuing a token
  pass-the-token-to-web-sdk-client: Pass the token to Web SDK client
  headless-integration: Headless Integration
  web-component-integration: Web component integration
  error-handling: Error Handling
---

# User authorization

Web SDK supports a first factor provided by the integrator during the flow, when enforced the user won't be able to perform an authentication/enrollment operation unless they have a valid user authorization.

This acts as a first defensive measure to stop bad actors from authenticating/enrolling as someone else.

In order to enable and enforce this verification process three steps are required:

1. Updating the customer configuration

2. Issuing a token on your backend

3. Passing the token to Web SDK on the frontend

## Update Customer Configuration

There are two configuration items belonging to user authorization:

|                             |                              |                                                                                                                                            |
| --------------------------- | ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| **Name**                    | **Type**                     | **Description**                                                                                                                            |
| User Authorization Type     | `"None"` \| `"RemoteJWKSet"` | The verification type, it's possible to disable it with `"None"` or enable the verification against a remote JWK set with `"RemoteJWKSet"` |
| User Authorization JWKs URI | `string`                     | The URI to specify if `"RemoteJWKSet"` is set in the `User Authorization Type`                                                             |

This configuration can only be updated by the Keyless staff, please communicate the desired values and the team will take care of it.

## Issuing a token

Before starting a session, your backend generates a short-lived JWT signed with one of the keys published at your JWKS endpoint.

The token must satisfy these requirements:

|           |                                        |
| --------- | -------------------------------------- |
| **Claim** | **Required value**                     |
| `sub`     | The username passed to the SDK session |
| `aud`     | `authentication-service`               |
| `iat`     | Issued-at time (Unix timestamp)        |
| `exp`     | Expiry time (Unix timestamp)           |

There's also a few more constraints: \* The system tolerates up to 5 minutes of clock skew. \* The tokens should be short-lived (5 – 10 minutes is sufficient). \* The tokens are single-use for the duration of one session.

Example JWT payload:

```javascript
{
  "sub": "user-123",
  "aud": "authentication-service",
  "iat": 1718400000,
  "exp": 1718400300
}
```

## Pass the token to Web SDK client

Once the token has been issued it needs to be set in the Web SDK client configuration, here's how.

### Headless Integration

Please base the integration code from the following guides:

* [Enrollment Headless Integration](web-sdk-guide-enrollment.html)

* [Authentication Headless Integration](web-sdk-guide-authentication.html)

The user authorization can be set in the openKeylessWebSocketConnection options:

```javascript
await openKeylessWebSocketConnection(sym, {
  ...,
  authorization: {
    token: 'USER_AUTHORIZATION_FROM_CUSTOMER'
  }
})
```

## Web component integration

Please base the integration code from the following guides:

* [Enrollment Web Component Integration](web-sdk-guide-enrollment.html)

* [Authentication Web Component Integration](web-sdk-guide-authentication.html)

The user authorization can be set through the `authorization-token` attribute:

```javascript
<kl-auth-or-enroll
  ...
  authorization-token="USER_AUTHORIZATION_FROM_CUSTOMER"
></kl-auth-or-enroll>
```

## Error Handling

In case the token is missing, expired, or the subject does not match the username, the session is rejected with a `SERVER_FORBIDDEN` error before any biometric processing occurs.

---

---
title: User interface customization
description: "\"Shows how to customize the user interface (UI) components provided with the PingOne Recognize Web SDK.\""
component: recognize
page_id: recognize:web-sdk:web-sdk-reference-customization
canonical_url: https://docs.pingidentity.com/recognize/web-sdk/web-sdk-reference-customization.html
llms_txt: https://docs.pingidentity.com/recognize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  customizing-user-interface-elements: Customizing user interface elements
  interface-structure: Interface structure
  default-style-values: Default style values
  example-setting-colors: "Example: Setting colors"
  slots: Slots
  example-changing-the-spinner: "Example: Changing the spinner"
  example-retry-when-liveness-fails: "Example: Retry when liveness fails"
---

# User interface customization

You can use the Web SDK to customize the appearance of PingOne Recognize user interface (UI) components by setting property values.

## Customizing user interface elements

Update the `theme-options` or `themeOptions` attributes with an object using the following structure:

> **Collapse: Details**
>
> ```javascript
> interface ThemeOptions {
>   colors: {
>     dark: {
>       primary: string
>       onPrimary: string
>       secondary: string
>       onSecondary: string
>       secondaryContainer: string
>       onSecondaryContainer: string
>       surface: string
>       onSurface: string
>       surfaceVariant: string
>       onSurfaceVariant: string
>     }
>     light: {
>       primary: string
>       onPrimary: string
>       secondary: string
>       onSecondary: string
>       secondaryContainer: string
>       onSecondaryContainer: string
>       surface: string
>       onSurface: string
>       surfaceVariant: string
>       onSurfaceVariant: string
>     }
>   }
>   elements: {
>     button: {
>       host: {
>         borderRadius: string
>         fontSize: string
>         fontWeight: string
>         padding: string
>       }
>       size: {
>         small: {
>           host: {
>             fontSize: string
>             padding: string
>           }
>         }
>       }
>       variant: {
>         text: {
>           host: {
>             borderBottom: string
>             hover: {
>               opacity: string
>             }
>           }
>         }
>       }
>     }
>     camera: {
>       host: {
>         after: {
>           background: string
>           height: string
>         }
>         before: {
>           background: string
>           height: string
>         }
>       }
>     }
>     cameraCorners: {
>       svg: {
>         strokeWidth: string
>       }
>     }
>     cameraInstructions: {
>       host: {
>         gap: string
>       }
>       li: {
>         borderRadius: string
>         gap: string
>         padding: string
>       }
>       liText: {
>         fontSize: string
>       }
>     }
>     cameraSelect: {
>       labels: {
>         gap: string
>         padding: string
>       }
>       labelsHeadline: {
>         fontSize: string
>         fontWeight: string
>       }
>       labelsText: {
>         fontSize: string
>         fontWeight: string
>       }
>       list: {
>         borderRadius: string
>         margin: string
>         padding: string
>         top: string
>       }
>       option: {
>         borderRadius: string
>         marginTop: string
>         padding: string
>       }
>     }
>     dialog: {
>       host: {
>         border: string
>         borderRadius: string
>         boxShadow: string
>       }
>     }
>     poweredBy: {
>       host: {
>         gap: string
>         height: string
>       }
>       icon: {
>         height: string
>         width: string
>       }
>       span: {
>         fontSize: string
>         fontWeight: string
>         letterSpacing: string
>       }
>     }
>     qrcode: {
>       host: {
>         borderRadius: string
>         padding: string
>       }
>     }
>     root: {
>       buttonCameraSelect: {
>         right: string
>         top: string
>       }
>       buttonCancel: {
>         left: string
>         top: string
>       }
>       buttonClose: {
>         left: string
>         top: string
>       }
>       buttonFlash: {
>         right: string
>         top: string
>       }
>       buttonPin: {
>         height: string
>         width: string
>       }
>       buttonsSwitchToMobileChoice: {
>         gap: string
>       }
>       cameraBiometric: {
>         width: string
>       }
>       cameraTip: {
>         backdropFilter: string
>         borderRadius: string
>         fontSize: string
>         fontWeight: string
>         height: string
>         padding: string
>         top: string
>       }
>       headline: {
>         fontSize: string
>         fontWeight: string
>         marginTop: string
>       }
>       host: {
>         borderRadius: string
>         gap: string
>         padding: string
>       }
>       poweredBy: {
>         bottom: string
>       }
>       text: {
>         fontSize: string
>         fontWeight: string
>       }
>       texts: {
>         gap: string
>       }
>     }
>   }
> }
> ```

### Interface structure

The theme options structure includes two main properties, `colors` and `elements`.

The `colors` block supports dark mode settings by providing `dark` and `light` objects, which each define color settings for the corresponding display mode.

The following diagram shows how each sub-property applies to the user interface.

![Annotated screenshot of the authentication error screen showing how color theme properties map to UI elements. The card background maps to the surface property. The card border maps to surfaceVariant. The error animation icon (a red circle with an X) is labeled as the Lottie slot. The heading 'Something went wrong' maps to onSurface, the primary body text color. The error description text maps to onSurfaceVariant, the secondary body text color. The Retry button background maps to primary, the button and spinner color. The button label text maps to onPrimary, the button text color.](_images/web-sdk-web-sdk-reference-customization-color-semantics.png)

The properties of the `elements` object affect the corresponding UI elements. Each property corresponds to a specific user interface element except for the `ae` property, which refers to the abstraction layer behind the authentication (`a`) and enroll (`e`) operations.

Style changes applied to an element property affect the corresponding user interface element.

### Default style values

The following example shows the default style values for PingOne Recognize:

> **Collapse: Details**
>
> ```javascript
> {
>   colors: {
>     dark: {
>       primary: '#1833B8',
>       onPrimary: '#FFFFFF',
>       secondary: '#FFD900',
>       onSecondary: '#1A1A1A',
>       error: '#BA3B1B',
>       secondaryContainer: '#2B2B2B',
>       onSecondaryContainer: '#F8F8F8',
>       surface: '#14161C',
>       onSurface: '#F8F8F8',
>       surfaceVariant: '#2B2B2B',
>       onSurfaceVariant: '#808080'
>     },
>     light: {
>       primary: '#151E74',
>       onPrimary: '#FFFFFF',
>       secondary: '#FFDE33',
>       onSecondary: '#1A1A1A',
>       error: '#BA3B1B',
>       secondaryContainer: '#F5F5F5',
>       onSecondaryContainer: '#1A1A1A',
>       surface: '#FFFFFF',
>       onSurface: '#1A1A1A',
>       surfaceVariant: '#F5F5F5',
>       onSurfaceVariant: '#808080'
>     }
>   },
>   elements: {
>     button: {
>       host: {
>         borderRadius: '8px',
>         fontSize: '14px',
>         fontWeight: '500',
>         padding: '14px 16px'
>       },
>       size: {
>         small: {
>           host: {
>             fontSize: '12px',
>             padding: '6px 8px'
>           }
>         }
>       },
>       variant: {
>         text: {
>           host: {
>             borderBottom: '1px solid',
>             hover: {
>               opacity: '0.1'
>             }
>           }
>         }
>       }
>     },
>     camera: {
>       host: {
>         after: {
>           background: 'linear-gradient(0deg, rgba(0, 0, 0, 0.25) 0%, rgba(0, 0, 0, 0) 100%)',
>           height: '25%'
>         },
>         before: {
>           background: 'linear-gradient(180deg, rgba(0, 0, 0, 0.25) 0%, rgba(0, 0, 0, 0) 100%)',
>           height: '25%'
>         }
>       }
>     },
>     cameraCorners: {
>       svg: {
>         strokeWidth: '3px'
>       }
>     },
>     cameraInstructions: {
>       host: {
>         gap: '8px'
>       },
>       li: {
>         borderRadius: '8px',
>         gap: '16px',
>         padding: '16px'
>       },
>       liText: {
>         fontSize: '14px'
>       }
>     },
>     cameraSelect: {
>       labels: {
>         gap: '12px',
>         padding: '24px 0 calc(24px - 8px) 0'
>       },
>       labelsHeadline: {
>         fontSize: '24px',
>         fontWeight: '500'
>       },
>       labelsText: {
>         fontSize: '16px',
>         fontWeight: '500'
>       },
>       list: {
>         borderRadius: '16px',
>         margin: '16px',
>         padding: '16px',
>         top: '32px !important'
>       },
>       option: {
>         borderRadius: '8px',
>         marginTop: '8px',
>         padding: '20px 16px'
>       }
>     },
>     dialog: {
>       host: {
>         border: '1px solid',
>         borderRadius: '16px',
>         boxShadow: '0px 4px 16px rgba(0, 0, 0, 0.25)'
>       }
>     },
>     poweredBy: {
>       host: {
>         gap: '6px',
>         height: '12px'
>       },
>       icon: {
>         height: '7px',
>         width: '55px'
>       },
>       span: {
>         fontSize: '9px',
>         fontWeight: '500',
>         letterSpacing: '2px'
>       }
>     },
>     qrcode: {
>       host: {
>         borderRadius: '8px',
>         padding: '4px'
>       }
>     },
>     root: {
>       buttonCameraSelect: {
>         right: 'calc(16px + 18px + 16px)',
>         top: '18px'
>       },
>       buttonCancel: {
>         left: '16px',
>         top: '16px'
>       },
>       buttonClose: {
>         left: '16px',
>         top: '16px'
>       },
>       buttonFlash: {
>         right: '18px',
>         top: '18px'
>       },
>       buttonPin: {
>         height: '16px',
>         width: '16px'
>       },
>       buttonsSwitchToMobileChoice: {
>         gap: '4px'
>       },
>       cameraBiometric: {
>         width: '100%'
>       },
>       cameraTip: {
>         backdropFilter: 'blur(4px)',
>         borderRadius: '4px',
>         fontSize: '12px',
>         fontWeight: '500',
>         height: '24px',
>         padding: '0px 8px',
>         top: '14px'
>       },
>       headline: {
>         fontSize: '24px',
>         fontWeight: '600',
>         marginTop: '32px'
>       },
>       host: {
>         borderRadius: '16px',
>         gap: '32px',
>         padding: '16px 16px 28px 16px'
>       },
>       poweredBy: {
>         bottom: '8px'
>       },
>       text: {
>         fontSize: '16px',
>         fontWeight: '400'
>       },
>       texts: {
>         gap: '8px'
>       }
>     }
>   }
> }
> ```

## Example: Setting colors

The following example shows how to change the primary and secondary colors by updating the `themeOptions` property of the PingOne Recognize authorization object (`auth`):

> **Collapse: Details**
>
> ```javascript
> <!doctype html>
> <html lang="en">
>   <head>
>     <meta charset="UTF-8" />
>     <meta name="viewport" content="width=device-width, initial-scale=1.0" />
>     <title>Auth</title>
>     <style>
>       * {
>         box-sizing: border-box;
>       }
>
>       body {
>         align-items: center;
>         display: flex;
>         justify-content: center;
>         margin: 0;
>         min-height: 100vh;
>         padding: 8px;
>       }
>
>       kl-auth {
>         border: 1px solid lightgray;
>       }
>     </style>
>   </head>
>   <body>
>     <kl-auth
>       customer="CUSTOMER_NAME"
>       enable-camera-instructions
>       key="IMAGE_ENCRYPTION_PUBLIC_KEY"
>       key-id="IMAGE_ENCRYPTION_KEY_ID"
>       lang="en"
>       size="375"
>       theme="light"
>       transaction-data='DATA_FROM_CUSTOMER_SERVER_TO_BE_SIGNED'
>       username="USERNAME"
>       ws-url="KEYLESS_AUTHENTICATION_SERVICE_URL"
>     ></kl-auth>
>     <script src="./node_modules/@keyless/sdk-web-components/index.js" type="module"></script>
>     <script>
>       const auth = document.querySelector('kl-auth')
>
>       auth.themeOptions = {
>         colors: {
>           light: {
>             primary: '#000',
>             onPrimary: '#fff',
>             surface: '#fff',
>             onSurface: '#000'
>           }
>         }
>       }
>     </script>
>   </body>
> </html>
> ```

## Slots

The PingOne Recognize Web SDK uses `<slot>` elements to customize the following components:

* `<kl-auth>`

* `<kl-auth-dialog>`

* `<kl-enroll>`

* `<kl-enroll-dialog>`

Each component supports the following slots:

|                             |                                                                                                                                                                                                        |
| --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `button-cancel`             | The circle button with the left arrow icon on the top left of the component. When clicked, it reconnects to the WebSocket and restarts the process from the beginning.                                 |
| `button-close`              | The circle button with the X icon on the top right of the component. when clicked, it closes the WebSocket connection and activates the close event used by the dialog components to close the dialog. |
| `lottie-spinner`            | The spinner animation.                                                                                                                                                                                 |
| `lottie-done`               | The checkmark animation.                                                                                                                                                                               |
| `lottie-error`              | The error animation.                                                                                                                                                                                   |
| `texts`                     | The title and description block.                                                                                                                                                                       |
| `camera-instructions`       | The list of camera instructions that the user should follow to perform a successful authentication or enrollment.                                                                                      |
| `button-camera-permissions` | The button that checks and potentially requests the camera permission to the user.                                                                                                                     |
| `camera-tip`                | The text tip on the top of the component when the cameras are on that suggests to the user how to better frame themself, only shown if camera checks are enabled.                                      |
| `camera-select`             | The select that is shown when the user is on a desktop device and has multiple cameras, grants the user the capability of picking a different camera than the default one.                             |
| `button-flash`              | The circle button with the flash icon on the top right of the component, its action is to force a white background on the screen.                                                                      |
| `camera-backdrop`           | The blurry camera stream that stays behind the main camera stream, its purpose is mainly for design.                                                                                                   |
| `camera-biometric`          | The main camera stream, useful for the user to adjust their camera quality in realtime.                                                                                                                |
| `buttons-stm-choice`        | The switch to mobile buttons, the primary button leads to a qrcode that lets the user continue the flow on their phone. The secondary button lets the user continue the flow on their current device.  |
| `stm-qrcode`                | The QR code that allows the user to continue the flow on their phone.                                                                                                                                  |
| `button-retry`              | The retry button, reconnects to the WebSocket and restarts the whole flow from zero.                                                                                                                   |
| `powered-by`                | The powered by PingOne Recognize element, always visible when enabled at the bottom of the component.                                                                                                  |

### Example: Changing the spinner

This example changes the appearance of the spinner in the authorization component. It defines a custom CSS style rule (`#custom-spinner`) and then assigns it to the spinner slot of the `<kl-auth>` element.

> **Collapse: Details**
>
> ```javascript
> <!doctype html>
> <html lang="en">
>   <head>
>     <meta charset="UTF-8" />
>     <meta name="viewport" content="width=device-width, initial-scale=1.0" />
>     <title>Auth</title>
>     <style>
>       * {
>         box-sizing: border-box;
>       }
>
>       body {
>         align-items: center;
>         display: flex;
>         justify-content: center;
>         margin: 0;
>         min-height: 100vh;
>         padding: 8px;
>       }
>
>       kl-auth {
>         border: 1px solid lightgray;
>       }
>
>       #custom-spinner {
>         width: 48px;
>         height: 48px;
>         border: 5px solid black;
>         border-bottom-color: transparent;
>         border-radius: 50%;
>         display: inline-block;
>         box-sizing: border-box;
>         animation: rotation 1s linear infinite;
>       }
>
>       @keyframes rotation {
>         0% {
>             transform: rotate(0deg);
>         }
>         100% {
>             transform: rotate(360deg);
>         }
>       }
>     </style>
>   </head>
>   <body>
>     <kl-auth
>       customer="CUSTOMER_NAME"
>       enable-camera-instructions
>       key="IMAGE_ENCRYPTION_PUBLIC_KEY"
>       key-id="IMAGE_ENCRYPTION_KEY_ID"
>       lang="en"
>       size="375"
>       theme="light"
>       transaction-data='DATA_FROM_CUSTOMER_SERVER_TO_BE_SIGNED'
>       username="USERNAME"
>       ws-url="KEYLESS_AUTHENTICATION_SERVICE_URL"
>     >
>       <div id="custom-spinner" slot="spinner"></div>
>     </kl-auth>
>     <script src="./node_modules/@keyless/sdk-web-components/index.js" type="module"></script>
>   </body>
> </html>
> ```

### Example: Retry when liveness fails

This example shows how to display components in specific situations. Here:

* The **Retry** button is initially hidden by assigning a custom CSS rule to a custom button named `custom-button-retry`.

* The button is assigned to the `button-retry` slot of the `<kl-auth>` elements.

* Events are added to the button to control visibility when the button is clicked and when the liveness check fails.