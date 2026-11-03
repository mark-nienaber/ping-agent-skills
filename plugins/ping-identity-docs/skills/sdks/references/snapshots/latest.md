---
title: Access resources using Token Vault
description: After you complete the set up of the Token Vault successfully, you can use the Ping (ForgeRock) SDK for JavaScript or any HTTP or fetch library to request protected resources.
component: sdks
version: latest
page_id: sdks:token-vault:getting-started/04-obtain-tokens
canonical_url: https://docs.pingidentity.com/sdks/latest/token-vault/getting-started/04-obtain-tokens.html
llms_txt: https://docs.pingidentity.com/sdks/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: Tue, 18 Jul 2023 14:37:51 +0100
keywords: ["Setup &amp; Configuration", "OAuth 2.0", "Integration", "Source Code"]
section_ids:
  request_tokens: Request tokens
  make_requests: Make requests
  revoke_tokens: Revoke tokens
  use_convenience_methods: Use convenience methods
  has_method: The has method
  refresh_method: The refresh method
---

# Access resources using Token Vault

After you complete the set up of the Token Vault successfully, you can use the Ping (ForgeRock) SDK for JavaScript or any HTTP or `fetch` library to request protected resources.

With the exception of refreshing tokens, and configuration of the token storage mechanism, using the Ping (ForgeRock) SDK for JavaScript with the Token Vault is almost entirely transparent.

The Token Vault manages token lifecycle automatically. If you enable refresh tokens in your OAuth 2.0 client, the Token Vault automatically refreshes access tokens.

## Request tokens

Use the `TokenManager` class from the SDK as usual to request tokens and have them safely stored within the Token Vault Proxy:

```javascript
import { TokenManager } from '@forgerock/javascript-sdk';

const tokens = TokenManager.getTokens();

console.log(tokens); // Refresh & Access Token values will be redacted
```

You can verify the tokens are stored under the origin of the Token Vault Proxy, not the origin of your main app, by using the developer tools in your browser.

The response your app and the SDK receive contains redacted values. This is expected behavior and increases security.

For example:

```json
{
    "accessToken": "REDACTED",
    "idToken": "eyJ0eXAiOiJKV1QiLCJra...7r8soMCk8A7QdQpg",
    "refreshToken": "REDACTED",
    "tokenExpiry": 1690712227226,
}
```

## Make requests

Use the native `fetch` API or any HTTP request library that emits a fetch event.

For example, you could use the `HttpClient` module provided in the Ping (ForgeRock) SDK for JavaScript.

The Token Vault Interceptor routes any of these requests that matches its configuration through the Token Vault Proxy so that the relevant tokens get attached before reaching your resource server.

## Revoke tokens

To remove tokens and log the user out, use the `FRUser` class as usual:

```javascript
import { FRUser } from '@forgerock/javascript-sdk';

FRUser.logout();
```

This destroys the user's session, revokes tokens on the server, and removes tokens from the Token Vault Proxy.

## Use convenience methods

The `tokenVaultStore` object provides some convenience functions for use in your apps.

These methods are useful as your main app does not have any direct access to the tokens in the Token Vault.

### The `has` method

Use the `has` method to determine whether the Token Vault has relevant tokens stored.

The method returns an object with a `hasTokens` property and a boolean value. It does not return the tokens.

```javascript
const tokenVaultStore = register.store();

const { hasTokens } = tokenVaultStore.has();

console.log(hasTokens); // logs `true` or `false`
```

|   |                                                                                                                                                                                                                                                                            |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | This method reflects the presence of tokens but does not validate those tokens. They may have expired or were revoked by the server.To validate the tokens use the `UserManager.getCurrentUser` method. You can consider the tokens valid if the method returns user data. |

### The `refresh` method

Use the `refresh` method to manually request that the Token Vault refreshes its tokens.

The Token Vault attempts to refresh tokens automatically when required, but you can use this `refresh` method to force a refresh of the tokens, if needed.

The method returns an object with a `refreshTokens` property with a boolean value.

```javascript
const tokenVaultStore = register.store();

const { refreshTokens } = tokenVaultStore.refresh();

console.log(refreshTokens); // logs `true` or `false`
```

---

---
title: Android OIDC login tutorials
description: Follow these Android tutorials to integrate your apps using OpenID Connect login to the following servers:
component: sdks
version: latest
page_id: sdks:oidc:tutorials/android/index
canonical_url: https://docs.pingidentity.com/sdks/latest/oidc/tutorials/android/index.html
llms_txt: https://docs.pingidentity.com/sdks/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: Mon, 3 Jul 2023 18:00:37 +0100
keywords: ["OAuth 2.0", "OpenID Connect", "Tutorial", "Source Code", "Integration", "SDK", "Android"]
---

# Android OIDC login tutorials

Follow these Android tutorials to integrate your apps using OpenID Connect login to the following servers:

![](../../../_images/logos/PingOne.png)

#### [PingOne](pingone/index.html)

![](../../../_images/logos/PingOneAICStacked.png)

#### [PingOne Advanced Identity Cloud](aic/index.html)

![](../../../_images/logos/PingAM.png)

#### [PingAM](pingam/index.html)

![](../../../_images/logos/PingFederate.png)

#### [PingFederate](pingfed/index.html)

---

---
title: API reference
description: Browse API reference documentation for the Ping (ForgeRock) Authenticator module:
component: sdks
version: latest
page_id: sdks:authenticator-module:reference
canonical_url: https://docs.pingidentity.com/sdks/latest/authenticator-module/reference.html
llms_txt: https://docs.pingidentity.com/sdks/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: Mon, 3 Jul 2023 18:00:37 +0100
---

# API reference

Browse API reference documentation for the Ping (ForgeRock) Authenticator module:

[icon: android, set=fab, size=3x]

#### [Android](https://developer.pingidentity.com/reference/sdks/android/api-reference-4.7.0/forgerock-authenticator/index.html)

ForgeRock Authenticator API reference for Android.

[icon: apple, set=fab, size=3x]

#### [iOS](https://developer.pingidentity.com/reference/sdks/ios/api-reference-4-6-0/FRAuthenticator/index.html)

ForgeRock Authenticator API reference for iOS.

---

---
title: API reference
description: Browse API reference documentation for Token Vault:
component: sdks
version: latest
page_id: sdks:token-vault:reference
canonical_url: https://docs.pingidentity.com/sdks/latest/token-vault/reference.html
llms_txt: https://docs.pingidentity.com/sdks/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: Mon, 3 Jul 2023 18:00:37 +0100
---

# API reference

Browse API reference documentation for Token Vault:

[icon: lock-hashtag, set=fadl, size=3x]

#### [Token Vault](https://developer.pingidentity.com/reference/sdks/javascript/token-vault-api-4-2-1/index.html)

Token Vault API reference.

---

---
title: Apple iOS OIDC login tutorials
description: Follow these iOS tutorials to integrate your apps using OpenID Connect login to the following servers:
component: sdks
version: latest
page_id: sdks:oidc:tutorials/ios/index
canonical_url: https://docs.pingidentity.com/sdks/latest/oidc/tutorials/ios/index.html
llms_txt: https://docs.pingidentity.com/sdks/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: Mon, 3 Jul 2023 18:00:37 +0100
keywords: ["OAuth 2.0", "OpenID Connect", "Tutorial", "Source Code", "Integration", "SDK", "iOS"]
---

# Apple iOS OIDC login tutorials

Follow these iOS tutorials to integrate your apps using OpenID Connect login to the following servers:

![](../../../_images/logos/PingOne.png)

#### [PingOne](pingone/index.html)

![](../../../_images/logos/PingOneAICStacked.png)

#### [PingOne Advanced Identity Cloud](aic/index.html)

![](../../../_images/logos/PingAM.png)

#### [PingAM](pingam/index.html)

![](../../../_images/logos/PingFederate.png)

#### [PingFederate](pingfed/index.html)

---

---
title: Associate your app with your server
description: To associate your server with your Android app you need to make public, verifiable statements by using a Digital Asset Links JSON file (assetlinks.json).
component: sdks
version: latest
page_id: sdks:sdks:use-cases/mobile-biometrics/android/01-prepare-assetlinks-json-file
canonical_url: https://docs.pingidentity.com/sdks/latest/sdks/use-cases/mobile-biometrics/android/01-prepare-assetlinks-json-file.html
llms_txt: https://docs.pingidentity.com/sdks/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: Thu, 24 Apr 2025 14:44:20 +0100
keywords: ["PingOne Advanced Identity Cloud", "PingAM", "Journeys", "Setup &amp; Configuration", "Source Code", "Use Case", "SDK"]
section_ids:
  get_sha_256_fingerprint_of_your_signing_certificates: Get SHA-256 fingerprint of your signing certificates
  host_the_digital_asset_links_json_file: Host the digital asset links JSON file
  summary: Summary
---

# Associate your app with your server

To associate your server with your Android app you need to make public, verifiable statements by using a Digital Asset Links JSON file (`assetlinks.json`).

Example `assetlinks.json` file

```json
[
    {
        "relation": [
            "delegate_permission/common.handle_all_urls",
            "delegate_permission/common.get_login_creds"
        ],
        "target": {
            "namespace": "android_app",
            "package_name": "com.example.app",
            "sha256_cert_fingerprints": [
                "E6:5A:5D:37:22:FC...22:99:20:03:E6:47"
            ]
        }
    }
]
```

## Get SHA-256 fingerprint of your signing certificates

The `assetlinks.json` file includes SHA-256 fingerprints of the certificates you use to sign your Android applications. The steps for obtaining the fingerprint depend on the method you use to distribute your application.

* Android App Bundles

* Local debug keys

If you are using Android App Bundles to distribute your apps, then the hashes of the certificate used to sign your application are available in the Android Developer console.

Follow these steps to obtain the SHA-256 hash of your signing certificate:

1. Configure your Android App Bundle for signing. Google has a number of methods for managing the signing certificates, including uploading your own or having Google manage them for you.

   For information on how to set up signing, refer to [Sign your app](https://developer.android.com/studio/publish/app-signing) in the Google Developer Documentation.

2. In the [Google Play Console](https://play.google.com/console):

   1. Select the app that will be supporting mobile biometrics.

   2. Navigate to Setup > App integrity > App signing.

      ![android signing certificates en](../../../../_images/android/android-signing-certificates-en.png)Figure 1. App signing keys in the Google Play Console

   3. In the App signing key certificate section, copy the SHA-256 certificate fingerprint value.

      |   |                                                                                                                    |
      | - | ------------------------------------------------------------------------------------------------------------------ |
      |   | In the Digital Asset Links JSON section is a file that you can copy with the SHA-256 fingerprint already in place. |

3. Create or update an `assetlinks.json` with the values copied from the Google Play Console for your app.

For more information on creating an `assetlinks.json` file, refer to [Google Digital Asset Links](https://developers.google.com/digital-asset-links/v1/getting-started).

You must manually generate a SHA-256 fingerprint of your signing key in the following scenarios:

* You are signing your APK with the default debug.jks that Android Studio created for the project

* You are signing your APK with your own keys that you have generated that have not been uploaded to the Google Play Console

Follow these steps to obtain the SHA-256 hash of your signing certificate:

1. In the `build.gradle` file for your application, check the settings defined in the `signingConfigs` property:

   Example signingConfigs when using the default debug.jks

   ```gradle
   signingConfigs {
       debug {
           storeFile file('../debug.jks')
           storePassword 'android'
           keyAlias 'androiddebugkey'
           keyPassword 'android'
       }
   }
   ```

2. In a terminal window, navigate to the location of the JKS file, and then run the following command:

   ```shell
   keytool -list -v -alias <keyAlias> -keystore <storeFile> | grep SHA256
   ```

   |   |                                                                                                                                                                                                       |
   | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | Swap the *\<keyAlias>* and *\<storeFile>* placeholders with the values you obtained from your project. For example:`keytool -list -v -alias "androiddebugkey" -keystore "./debug.jks" \| grep SHA256` |

3. When requested, enter the keystore password, as specified in the `keyPassword` property in the `build.gradle` file.

   The command prints the SHA-256 fingerprint of the signing key:

   ```shell
   Enter keystore password:  android
   SHA256: E6:5A:5D:37:22:FC...22:99:20:03:E6:47
   Signature algorithm name: SHA256withRSA
   ```

4. Create or update an `assetlinks.json` with the SHA-256 fingerprint, and the details of your app.

For more information on creating an `assetlinks.json` file, refer to [Google Digital Asset Links](https://developers.google.com/digital-asset-links/v1/getting-started).

## Host the digital asset links JSON file

* For PingOne Advanced Identity Cloud deployments, refer to [Upload an Android assetlinks.json file](https://backstage.forgerock.com/docs/idcloud/latest/developer-docs/upload-android-assetlinks.html).

* For self-managed deployments, host the file at `https://<your domain>/.well-known/assetlinks.json`.

## Summary

You have now created and uploaded a digital asset links JSON file.

You can now proceed to [Configure biometric authentication journeys](02-node-configurations.html).

---

---
title: Authenticate by using a WebAuthn device
description: After the user registers their mobile device they can use it as an authenticator, with its registered key pair, through the WebAuthn Authentication node, which the Ping (ForgeRock) SDK for Android returns as a WebAuthnAuthenticationCallback.
component: sdks
version: latest
page_id: sdks:sdks:use-cases/mobile-biometrics/android/05-user-authentication
canonical_url: https://docs.pingidentity.com/sdks/latest/sdks/use-cases/mobile-biometrics/android/05-user-authentication.html
llms_txt: https://docs.pingidentity.com/sdks/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: Tue, 27 Jun 2023 18:31:07 +0100
keywords: ["PingOne Advanced Identity Cloud", "PingAM", "Journeys", "Setup &amp; Configuration", "Source Code", "Use Case", "SDK"]
section_ids:
  webauthnkeyselector: WebAuthnKeySelector
---

# Authenticate by using a WebAuthn device

After the user registers their mobile device they can use it as an authenticator, with its registered key pair, through the WebAuthn Authentication node, which the Ping (ForgeRock) SDK for Android returns as a `WebAuthnAuthenticationCallback`.

If the device supports [passkeys](https://developers.google.com/identity/passkeys/supported-environments), the operating system displays a list of available passkeys:

![android select passkey en](../../../../_images/android/android-select-passkey-en.jpg)Figure 1. Select the passkey to use for WebAuthn

Note that removing credentials stored on the client device does not remove the associated data from the server. You will need to register the device again after removing credentials from the client.

As part of authentication process, the SDK provides the `WebAuthnAuthenticationCallback` for authenticating the device as a credential.

* Android - Java

* Android - Kotlin

```java
WebAuthnAuthenticationCallback callback = node.getCallback(WebAuthnAuthenticationCallback.class);
callback.authenticate(requireContext(), node, webAuthnKeySelector.DEFAULT, new FRListener<Void>() {
    @Override
    public void onSuccess(Void result) {
        // Authentication is successful
        // Continue the journey by calling next()
    }

    @Override
    public void onException(Exception e) {
        // An error occurred during the authentication process
        // Continue the journey by calling next()
    }
});
```

```kotlin
fun WebAuthnAuthenticationCallback(
    callback: WebAuthnAuthenticationCallback,
    node: Node,
    onCompleted: () -> Unit
) {

    val context = LocalContext.current

    try {
        callback.authenticate(context, node)
        // Authentication successful
        currentOnCompleted()
    } catch (e: CancellationException) {
        // User cancelled authentication
    } catch (e: Exception) {
        // An error occurred during the authentication process
        currentOnCompleted()
    }
}
```

|   |                                                                                                                                                                                                                                                                                                                                      |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | The `WebAuthnAuthenticationCallback.authenticate()` method has a parameter, `Node`.If the current node has both `WebAuthnAuthenticationCallback` and `HiddenValueCallback` callbacks then the SDK automatically sets the outcome of the authentication process for both success and failure to the designated `HiddenValueCallback`. |

## WebAuthnKeySelector

An optional `WebAuthnKeySelector` parameter can be provided for authentication.

The `WebAuthnKeySelector.select()` method is invoked when `Username from device` is enabled in the WebAuthn Authentication node. This feature requires that `Username to device` is enabled in the WebAuthn Registration node as well. With these options enabled, the registered key pair is associated with the username, and the SDK can present a list of registered keys to the user to continue the authentication process without collecting a username.

|   |                                                                                                                                                                                                                                                                                                                |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The `sourceList` is a list of `PublicKeyCredentialSource` constructed during registration. You can alter the string value and present the altered value to the user; however, you **must** return the selected `PublicKeyCredentialSource` as it was provided in the original list to the provided `listener`. |

```java
callback.authenticate(this, node, new WebAuthnKeySelector() {
    @Override
    public void select(@NonNull FragmentManager fragmentManager,
                       @NonNull List<PublicKeyCredentialSource> sourceList,
                       @NonNull FRListener<PublicKeyCredentialSource> listener) {
        //Always pick the first one.
        listener.onSuccess(sourceList.get(0));
    }
}, new FRListener<Void>() {
    @Override
    public void onSuccess(Void result) {
        //...
    }

    @Override
    public void onException(Exception e) {
        //...
    }
});
```

---

---
title: Authenticate by using a WebAuthn device
description: After the user's mobile device has been registered in PingAM, the device can be used as an authenticator with its registered key pair through the WebAuthn Authentication node, which is returned as a WebAuthnAuthenticationCallback by the Ping (ForgeRock) SDK for iOS.
component: sdks
version: latest
page_id: sdks:sdks:use-cases/mobile-biometrics/ios/04-user-authentication
canonical_url: https://docs.pingidentity.com/sdks/latest/sdks/use-cases/mobile-biometrics/ios/04-user-authentication.html
llms_txt: https://docs.pingidentity.com/sdks/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: Wed, 14 Jun 2023 14:36:02 +0100
keywords: ["PingOne Advanced Identity Cloud", "PingAM", "Journeys", "Setup &amp; Configuration", "Source Code", "Use Case", "SDK"]
section_ids:
  select_credentials: Select credentials
---

# Authenticate by using a WebAuthn device

After the user's mobile device has been registered in PingAM, the device can be used as an authenticator with its registered key pair through the WebAuthn Authentication node, which is returned as a `WebAuthnAuthenticationCallback` by the Ping (ForgeRock) SDK for iOS.

If the device supports [Passkeys](https://developer.apple.com/passkeys/), the operating system displays passkeys that can be used:

![ios select passkey en](../../../../_images/ios/ios-select-passkey-en.png)Figure 1. Select a passkey to use for WebAuthn

Note that removing credentials stored on the client device does not remove the associated data from the server. You will need to register the device again after removing credentials from the client.

With `WebAuthnAuthenticationCallback`, you must implement the following protocol method to handle the authentication process:

```swift
public protocol PlatformAuthenticatorAuthenticationDelegate {
    func selectCredential(keyNames: [String], selectionCallback: @escaping WebAuthnCredentialsSelectionCallback)
}
```

As part of authentication process, the SDK provides the `WebAuthnAuthenticationCallback` for authenticating the device as a credential.

```swift
if let authenticationCallback = callback as? WebAuthnAuthenticationCallback {

    authenticationCallback.delegate = self

    // Note that the `Node` parameter in `.authenticate()` is an optional parameter.
    // If the node is provided, the SDK automatically returns the assertion
    // in the HiddenValueCallback.

    authenticationCallback.authenticate(
        node: node,
        window: UIApplication.shared.windows.first,
        preferImmediatelyAvailableCredentials: false,
        usePasskeysIfAvailable: true
    ) { (assertion) in
        // Authentication is successful
        // Submit the Node using Node.next()
    } onError: { (error) in
        // An error occurred during the authentication process
        // Submit the Node using Node.next()
    }
}
```

Set the `usePasskeysIfAvailable` parameter to `true` to enable passkeys on supported devices.

When passkeys are enabled, the device offers the ability to sign in using passkeys stored an a separate supported device, by first scanning a QR code.

![ios passkeys from another device en](../../../../_images/ios/ios-passkeys-from-another-device-en.png)Figure 2. Use a stored passkey from another device by first scanning the QR code

To prevent this behavior and only accept passkeys stored on the initial client device, set the `preferImmediatelyAvailableCredentials` parameter to `true`.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The `WebAuthnAuthenticationCallback.authenticate()` method has an optional parameter, `Node`.If the current node contains both `WebAuthnAuthenticationCallback` and `HiddenValueCallback` callbacks, and this node is passed as a parameter to the `WebAuthnAuthenticationCallback.authenticate()` method, then the SDK automatically returns the outcome of the authentication process for both success and failure into the designated `HiddenValueCallback`.If the node is not provided, the assertion or error outcome **must** be set manually. |

## Select credentials

The `func selectCredential()` method is invoked when `Username from device` is enabled in the WebAuthn Authentication node. This feature requires that `Username to device` is enabled in the WebAuthn Registration node as well. With these options enabled, the registered key pair is associated with the username, and the SDK can present a list of registered keys to the user to continue the authentication process without collecting a username.

|   |                                                                                                                                                                                                                                                                    |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | The `keyName` is an array of strings constructed as `<User's displayName> <Registered Timestamp>`.You may alter the string value, and present the altered value to the user, but you **must** return the key name string as it was provided in the original array. |

```swift
func selectCredential(keyNames: [String], selectionCallback: @escaping WebAuthnCredentialsSelectionCallback) {
    let actionSheet = UIAlertController(title: "Select Credentials", message: nil, preferredStyle: .actionSheet)

    for keyName in keyNames {
        actionSheet.addAction(UIAlertAction(title: keyName, style: .default, handler: { (action) in
            selectionCallback(keyName)
        }))
    }

    actionSheet.addAction(UIAlertAction(title: "Cancel", style: .cancel, handler: { (action) in
        selectionCallback(nil)
    }))

    guard let vc = self.viewController else {
        return
    }

    if actionSheet.popoverPresentationController != nil {
        actionSheet.popoverPresentationController?.sourceView = self
        actionSheet.popoverPresentationController?.sourceRect = self.bounds
    }

    DispatchQueue.main.async {
        viewController.present(actionSheet, animated: true, completion: nil)
    }
}
```

---

---
title: Authentication journey deep-dive tutorial for Android
description: This tutorial guides you through creating a Ping (ForgeRock) SDK-enabled Android app from beginning to end. The app connects to a PingOne Advanced Identity Cloud tenant or PingAM server to authenticate a user using an authentication journey.
component: sdks
version: latest
page_id: sdks:sdks:tutorials/android/index
canonical_url: https://docs.pingidentity.com/sdks/latest/sdks/tutorials/android/index.html
llms_txt: https://docs.pingidentity.com/sdks/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: Mon, 3 Jul 2023 18:00:37 +0100
keywords: ["PingOne Advanced Identity Cloud", "PingAM", "Journeys", "Setup &amp; Configuration", "Source Code", "Tutorial", "SDK"]
section_ids:
  before_you_begin: Before you begin
  step_1_configure_the_development_environment: Step 1. Configure the development environment
  step_2_configure_connection_properties: Step 2. Configure connection properties
  step_3_initialize_the_sdk: Step 3. Initialize the SDK
  step_4_create_a_status_view: Step 4. Create a status view
  step_5_add_login_and_logout_calls: Step 5. Add login and logout calls
  step_6_create_ui_to_handle_the_callbacks: Step 6. Create UI to handle the callbacks
  step_7_test_the_app: Step 7. Test the app
---

# Authentication journey deep-dive tutorial for Android

**This tutorial guides you through creating a Ping (ForgeRock) SDK-enabled Android app from beginning to end. The app connects to a PingOne Advanced Identity Cloud tenant or PingAM server to authenticate a user using an authentication journey.**

You'll step through the user authentication journey and display the appropriate user interface, meaning you get to implement the design to your requirements.

|   |                                                                                                                                         |
| - | --------------------------------------------------------------------------------------------------------------------------------------- |
|   | To get up and running in the shortest time, try the [Authentication journey quick start for Android](../android-quickstart/index.html). |

## [Before you begin](00_before-you-begin.html)

Before you begin this tutorial ensure you have set up your PingOne Advanced Identity Cloud tenant or PingAM server with the required configuration.

For example, you will need an OAuth 2.0 client application set up, as well as an authentication journey for the app to navigate.

[**Complete prerequisites**[icon: chevrons-right, set=fas, size=xs]](00_before-you-begin.html)

## [Step 1. Configure the development environment](01_configure-the-dev-environment.html)

In this step, you set up your environment to create Android applications using the freely-available Android Studio IDE.

You then create a new application project and configure it to use the Ping (ForgeRock) SDK for Android.

[**Start step 1**[icon: chevrons-right, set=fas, size=xs]](01_configure-the-dev-environment.html)

## [Step 2. Configure connection properties](02_configure-sdk-connection-strings.html)

In this step, you provide your application with the settings it needs to connect to your PingOne Advanced Identity Cloud or PingAM instance.

For example, which authentication tree to use, and the realm it is a part of.

[**Start step 2**[icon: chevrons-right, set=fas, size=xs]](02_configure-sdk-connection-strings.html)

## [Step 3. Initialize the SDK](03_initialize-sdk.html)

In this step, you enable debug logging during development.

You then and add a call to the `FRAuth.start()` method, which initializes the SDK and loads the configuration you have defined in the previous step.

[**Start step 3**[icon: chevrons-right, set=fas, size=xs]](03_initialize-sdk.html)

## [Step 4. Create a status view](04_create-status-view.html)

In this step, you create a layout and add buttons to log in and log out your user, as well as a text view field to show their current authentication status.

You also add the code to update the value displayed in the text view.

[**Start step 4**[icon: chevrons-right, set=fas, size=xs]](04_create-status-view.html)

## [Step 5. Add login and logout calls](05_add-login-logout.html)

In this step, you update the app with the `NodeListener` interface, which manages the client side of the authentication journey.

[**Start step 5**[icon: chevrons-right, set=fas, size=xs]](05_add-login-logout.html)

## [Step 6. Create UI to handle the callbacks](06_handle-the-callbacks.html)

In this step, you add a UI fragment to obtain credentials from the user, and code to open that fragment when the callback is received.

You also add code to populate the callback with the credentials and return it to the server, completing the authentication journey.

[**Start step 6**[icon: chevrons-right, set=fas, size=xs]](06_handle-the-callbacks.html)

## [Step 7. Test the app](07_test-the-app.html)

In this step, you will test your application.

You run it in the emulator or on your Android device, perform authentication with a demo user, check the log for success messages, and then log out the user.

[**Test app**[icon: chevrons-right, set=fas, size=xs]](07_test-the-app.html)

---

---
title: Authentication journey quick start for Android
description: Prepare
component: sdks
version: latest
page_id: sdks:sdks:tutorials/android-quickstart/index
canonical_url: https://docs.pingidentity.com/sdks/latest/sdks/tutorials/android-quickstart/index.html
llms_txt: https://docs.pingidentity.com/sdks/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: Mon, 3 Jul 2023 18:00:37 +0100
keywords: ["PingOne Advanced Identity Cloud", "PingAM", "Journeys", "Setup &amp; Configuration", "Source Code", "Tutorial", "SDK"]
page_aliases: ["android:configuring/configuring-forgerock-sdk-settings-for-your-android-app.adoc"]
section_ids:
  before_you_begin: Before you begin
  step_1_download_the_samples: Step 1. Download the samples
  step_2_configure_connection_properties: Step 2. Configure connection properties
  step_3_test_the_app: Step 3. Test the app
---

# Authentication journey quick start for Android

* [Prepare](00_before-you-begin.html)

* [Download](01_downloading-forgerocksdk.html)

* [Configure](02_configure_android_embedded-quickstart_for_aic_or_pingam.html)

* [Run](03_running_android-quickstart.html)

***

**In this quick start tutorial you update one of our sample applications to connect to your PingOne Advanced Identity Cloud tenant or PingAM server to authenticate a user.**

The app steps through a simple authentication journey and returns a session token. The app is then able to obtain user info from the server, and finally sign out to terminate the session.

|   |                                                                                                                                                                |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | To learn how to create an app from scratch to authenticate your users, try the [Authentication journey deep-dive tutorial for Android](../android/index.html). |

## [Before you begin](00_before-you-begin.html)

Before you begin this tutorial ensure you have set up your PingOne Advanced Identity Cloud tenant or PingAM server with the required configuration.

For example, you will need an OAuth 2.0 client application set up, as well as an authentication journey for the app to navigate.

[**Complete prerequisites**[icon: chevrons-right, set=fas, size=xs]](00_before-you-begin.html)

## [Step 1. Download the samples](01_downloading-forgerocksdk.html)

To start this tutorial, you need to download the SDK sample apps repo, which contains the projects you will use.

[**Start step 1**[icon: chevrons-right, set=fas, size=xs]](01_downloading-forgerocksdk.html)

## [Step 2. Configure connection properties](02_configure_android_embedded-quickstart_for_aic_or_pingam.html)

In this step, you configure the "kotlin-ui-prototype" sample app to connect to the OAuth 2.0 application you created in PingOne Advanced Identity Cloud or PingAM.

[**Start step 2**[icon: chevrons-right, set=fas, size=xs]](02_configure_android_embedded-quickstart_for_aic_or_pingam.html)

## [Step 3. Test the app](03_running_android-quickstart.html)

In this step, you will test your application.

You run it in the emulator or on your Android device, perform authentication with a demo user, obtain OAuth 2.0 tokens, and then log out the user.

[**Test app**[icon: chevrons-right, set=fas, size=xs]](03_running_android-quickstart.html)

---

---
title: Authentication journey tutorial for a React Native app
description: This tutorial covers the basics of running a protected mobile app with React Native.
component: sdks
version: latest
page_id: sdks:sdks:tutorials/react-native/index
canonical_url: https://docs.pingidentity.com/sdks/latest/sdks/tutorials/react-native/index.html
llms_txt: https://docs.pingidentity.com/sdks/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  before_you_begin: Before you begin
  step_1_download_the_samples: Step 1. Download the samples
  step_2_configure_the_projects: Step 2. Configure the projects
  step_3_configure_connection_properties: Step 3. Configure connection properties
  step_4_build_and_run_the_apps: Step 4. Build and run the apps
---

# Authentication journey tutorial for a React Native app

**This tutorial covers the basics of running a protected mobile app with React Native.**

Ping Identity does not provide a React Native version of the Ping SDK. Instead we present this example of "bridge code" for connecting the Ping (ForgeRock) SDK for Android and iOS to the React Native layer.

This guide covers how to implement the following application features using the Ping (ForgeRock) SDKs:

1. Authentication through a simple journey/tree.

2. Requesting OAuth/OIDC tokens.

3. Requesting user information.

4. Logging a user out.

![react native todos screen](../../../_images/build-reactnative-part-one/react-native-todos-screen.webp)Figure 1. The to-do sample app

## [Before you begin](00_before-you-begin.html)

Before you begin this tutorial ensure you have set up your PingOne Advanced Identity Cloud tenant or PingAM server with the required configuration.

For example, you will need to configure an OAuth 2.0 client application, as well as an authentication journey for the app to navigate.

[**Complete prerequisites**[icon: chevrons-right, set=fas, size=xs]](00_before-you-begin.html)

## [Step 1. Download the samples](01_downloading-samples.html)

To start this tutorial, you need to download the SDK sample apps repo, which contains the projects you will use.

[**Start step 1**[icon: chevrons-right, set=fas, size=xs]](01_downloading-samples.html)

## [Step 2. Configure the projects](02_configure-the-projects.html)

In this step you install the dependencies the projects require.

[**Start step 2**[icon: chevrons-right, set=fas, size=xs]](02_configure-the-projects.html)

## [Step 3. Configure connection properties](03_configure_connection_properties.html)

In this step, you configure the samples to connect to the authentication tree/journey and OAuth 2.0 client you created when setting up your server configuration.

[**Start step 3**[icon: chevrons-right, set=fas, size=xs]](03_configure_connection_properties.html)

## [Step 4. Build and run the apps](04_build_and_run_the_app.html)

Build and run the apps, and try out the API backend by creating and editing todo items.

[**Start step 4**[icon: chevrons-right, set=fas, size=xs]](04_build_and_run_the_app.html)

---

---
title: Authentication journey tutorial for Angular
description: In this tutorial you build out a sample Angular SPA and make use of a Node.js REST API server sample app.
component: sdks
version: latest
page_id: sdks:sdks:tutorials/angular/index
canonical_url: https://docs.pingidentity.com/sdks/latest/sdks/tutorials/angular/index.html
llms_txt: https://docs.pingidentity.com/sdks/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  before_you_begin: Before you begin
  step_1_download_the_samples: Step 1. Download the samples
  step_2_configure_connection_properties: Step 2. Configure connection properties
  step_3_build_and_run_the_projects: Step 3. Build and run the projects
  step_4_implement_the_ping_forgerock_sdk: Step 4. Implement the Ping (ForgeRock) SDK
---

# Authentication journey tutorial for Angular

**In this tutorial you build out a sample Angular SPA and make use of a Node.js REST API server sample app.**

This guide uses the Ping (ForgeRock) SDK for JavaScript to implement the following application features:

* Dynamic authentication form for login.

* OAuth/OIDC token acquisition through the Authorization Code Flow with PKCE.

* Protected client-side routing.

* Resource requests to a protected REST API.

* Log out - revoke tokens and end session.

![todos page with todos](../../../_images/build-angular-app/todos-page-with-todos.png)Figure 1. The Todo page of the sample app.

## [Before you begin](00_before-you-begin.html)

Before you begin this tutorial ensure you have set up your PingOne Advanced Identity Cloud tenant or PingAM server with the required configuration.

For example, you will need to configure CORS, have an OAuth 2.0 client application set up, as well as an authentication journey for the app to navigate.

[**Complete prerequisites**[icon: chevrons-right, set=fas, size=xs]](00_before-you-begin.html)

## [Step 1. Download the samples](01_downloading-forgerocksdk.html)

To start this tutorial, you need to download the SDK sample apps repo, which contains the projects you will use.

[**Start step 1**[icon: chevrons-right, set=fas, size=xs]](01_downloading-forgerocksdk.html)

## [Step 2. Configure connection properties](02_configure-the-projects.html)

Configure both the Todo client app, and the API backend server app to connect to the OAuth 2.0 application you created in PingOne Advanced Identity Cloud or PingAM.

[**Start step 2**[icon: chevrons-right, set=fas, size=xs]](02_configure-the-projects.html)

## [Step 3. Build and run the projects](03_build_and_run_the_app.html)

In this step you build and run the API backend server app, and then the Todo client app.

There are also troubleshooting tips if the apps do not start as expected.

[**Start step 3**[icon: chevrons-right, set=fas, size=xs]](03_build_and_run_the_app.html)

## [Step 4. Implement the Ping (ForgeRock) SDK](04_implement_the_sdk.html)

In this final step you implement the Ping (ForgeRock) SDK into the Todo client app, so that it handles the responses from your PingOne Advanced Identity Cloud tenant or PingAM server, can get tokens and user information, and supports logging out.

[**Start step 4**[icon: chevrons-right, set=fas, size=xs]](04_implement_the_sdk.html)

---

---
title: Authentication journey tutorial for Flutter
description: This tutorial covers the basics of developing a protected mobile app with Flutter. It focuses on developing the Android and iOS bridge code along with a minimal Flutter UI to authenticate a user.
component: sdks
version: latest
page_id: sdks:sdks:tutorials/flutter/index
canonical_url: https://docs.pingidentity.com/sdks/latest/sdks/tutorials/flutter/index.html
llms_txt: https://docs.pingidentity.com/sdks/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  before_you_begin: Before you begin
  step_1_download_the_samples: Step 1. Download the samples
  step_2_configure_the_projects: Step 2. Configure the projects
  step_3_build_and_run_the_project: Step 3. Build and run the project
  step_4a_implement_ios_bridge_code: Step 4a. Implement iOS bridge code
  step_4b_implement_android_bridge_code: Step 4b. Implement Android bridge code
  step_5_implement_the_ui_in_flutter: Step 5. Implement the UI in Flutter
---

# Authentication journey tutorial for Flutter

**This tutorial covers the basics of developing a protected mobile app with Flutter. It focuses on developing the Android and iOS bridge code along with a minimal Flutter UI to authenticate a user.**

Bridge code development is a concept common to mobile apps built using hybrid technologies. Hybrid is a term used when a portion of the mobile app uses a language that is not native to the platform (Android and Java or iOS and Swift).

Flutter is an open source framework by Google for building beautiful, natively compiled, multi-platform applications from a single codebase. Flutter requires this bridging code to provide the hybrid layer (Dart) access to native APIs (Swift in this case) or dependencies.

This guide uses the Ping (ForgeRock) SDK to implement the following application features:

1. Authentication through a simple journey/tree.

2. Requesting OAuth/OIDC tokens.

3. Requesting user information.

4. Logging a user out.

![flutter todos screen](../../../_images/build-flutter-part-one/flutter-todos-screen.png)Figure 1. The to-do sample app

## [Before you begin](00_before-you-begin.html)

Before you begin this tutorial ensure you have set up your PingOne Advanced Identity Cloud tenant or PingAM server with the required configuration.

For example, you will need to configure CORS, have an OAuth 2.0 client application set up, as well as an authentication journey for the app to navigate.

[**Complete prerequisites**[icon: chevrons-right, set=fas, size=xs]](00_before-you-begin.html)

## [Step 1. Download the samples](01_downloading-samples.html)

To start this tutorial, you need to download the SDK sample apps repo, which contains the projects you will use.

[**Start step 1**[icon: chevrons-right, set=fas, size=xs]](01_downloading-samples.html)

## [Step 2. Configure the projects](02_configure-the-projects.html)

In this step you install the dependencies the projects require, and configure the connection properties.

[**Start step 2**[icon: chevrons-right, set=fas, size=xs]](02_configure-the-projects.html)

## [Step 3. Build and run the project](04_build_and_run_the_app.html)

Build and run the apps, and learn about *Hot Module Reloading*.

[**Start step 3**[icon: chevrons-right, set=fas, size=xs]](04_build_and_run_the_app.html)

## [Step 4a. Implement iOS bridge code](05_implement_the_sdk.html)

In this step you implement the iOS bridge code and add methods for starting the Ping (ForgeRock) SDK, logging a user in, stepping through a journey, and finally logging a user out.

[**Start step 4a**[icon: chevrons-right, set=fas, size=xs]](05_implement_the_sdk.html)

## [Step 4b. Implement Android bridge code](05a_implement_the_sdk_android.html)

In this step you implement the Android bridge code and add methods for starting the Ping (ForgeRock) SDK, logging a user in, stepping through a journey, and finally logging a user out.

[**Start step 4b**[icon: chevrons-right, set=fas, size=xs]](05_implement_the_sdk.html)

## [Step 5. Implement the UI in Flutter](06_implement_login_ui_in_flutter.html)

In this final step you implement the user interface for logging in, and code for submitting the forms. You will also handle returning to the list view, requesting user info, and handling logout triggers.

This is also the moment you can try out the fully functioning app.

[**Start step 5**[icon: chevrons-right, set=fas, size=xs]](06_implement_login_ui_in_flutter.html)

---

---
title: Authentication journey tutorial for iOS
description: Prepare
component: sdks
version: latest
page_id: sdks:sdks:tutorials/ios/index
canonical_url: https://docs.pingidentity.com/sdks/latest/sdks/tutorials/ios/index.html
llms_txt: https://docs.pingidentity.com/sdks/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
page_aliases: ["ios:configuring/configuring-forgerock-sdk-settings-iosapp.adoc"]
section_ids:
  before_you_begin: Before you begin
  step_1_download_the_samples: Step 1. Download the samples
  step_2_configure_connection_properties: Step 2. Configure connection properties
  step_3_test_the_app: Step 3. Test the app
---

# Authentication journey tutorial for iOS

* [Prepare](00_before-you-begin.html)

* [Download](01_downloading-forgerocksdk.html)

* [Configure](02_configuring-sample-for-aic-or-pingam.html)

* [Run](03_running-sample-pingone.html)

***

**In this tutorial you update a sample app to step through an authentication journey, meaning you get to design and implement the user interface to your requirements.**

The sample navigates through a simple authentication journey, and obtains OAuth 2.0 tokens for the user.

## [Before you begin](00_before-you-begin.html)

Before you begin this tutorial ensure you have set up your PingOne Advanced Identity Cloud tenant or PingAM server with the required configuration.

For example, you will need an OAuth 2.0 client application set up, as well as an authentication journey for the app to navigate.

[**Complete prerequisites**[icon: chevrons-right, set=fas, size=xs]](00_before-you-begin.html)

## [Step 1. Download the samples](01_downloading-forgerocksdk.html)

To start this tutorial, you need to download the SDK sample apps repo, which contains the projects you will use.

[**Start step 1**[icon: chevrons-right, set=fas, size=xs]](01_downloading-forgerocksdk.html)

## [Step 2. Configure connection properties](02_configuring-sample-for-aic-or-pingam.html)

In this step, you configure the "uikit-quickstart" sample app to connect to the OAuth 2.0 application you created in PingOne Advanced Identity Cloud or PingAM.

[**Start step 2**[icon: chevrons-right, set=fas, size=xs]](02_configuring-sample-for-aic-or-pingam.html)

## [Step 3. Test the app](03_running-sample-pingone.html)

In this step, you will test your application.

You run it in the emulator or on your iOS device, perform authentication with a demo user, check the log for success messages, and then log out the user.

[**Test app**[icon: chevrons-right, set=fas, size=xs]](03_running-sample-pingone.html)

---

---
title: Authentication journey tutorial for iOS
description: Prepare
component: sdks
version: latest
page_id: sdks:oidc:tutorials/ios/pingfed/index
canonical_url: https://docs.pingidentity.com/sdks/latest/oidc/tutorials/ios/pingfed/index.html
llms_txt: https://docs.pingidentity.com/sdks/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  before_you_begin: Before you begin
  step_1_download_the_samples: Step 1. Download the samples
  step_2_configure_connection_properties: Step 2. Configure connection properties
  step_3_test_the_app: Step 3. Test the app
---

# Authentication journey tutorial for iOS

* [Prepare](00_before-you-begin.html)

* [Download](01_downloading-forgerocksdk.html)

* [Configure](02_configuring-sample-for-pingfed.html)

* [Run](03_running-sample-pingfed.html)

***

**In this tutorial you update a sample app that uses OIDC-based login to obtain tokens by redirecting to the PingFederate UI for authentication.**

The sample connects to the `.well-known` endpoint of your PingFederate server to obtain the correct URIs to authenticate the user, and redirects to your PingFederate server's login UI.

After authentication, PingFederate redirects the browser back to your application, which then obtains an OAuth 2.0 access token and displays the related user information.

## [Before you begin](00_before-you-begin.html)

Before you begin this tutorial ensure you have set up your PingFederate server with the required configuration.

For example, you will need to configure an OAuth 2.0 client application.

[**Complete prerequisites**[icon: chevrons-right, set=fas, size=xs]](00_before-you-begin.html)

## [Step 1. Download the samples](01_downloading-forgerocksdk.html)

To start this tutorial, you need to download the SDK sample apps repo, which contains the projects you will use.

[**Start step 1**[icon: chevrons-right, set=fas, size=xs]](01_downloading-forgerocksdk.html)

## [Step 2. Configure connection properties](02_configuring-sample-for-pingfed.html)

In this step, you configure the sample app to connect to the OAuth 2.0 application you created in PingFederate.

[**Start step 2**[icon: chevrons-right, set=fas, size=xs]](02_configuring-sample-for-pingfed.html)

## [Step 3. Test the app](03_running-sample-pingfed.html)

In the following procedure, you run the sample app that you configured in the previous step.

The sample connects to your PingFederate server to obtain the correct URIs to authenticate the user, and redirects the browser to your PingFederate server.

After authentication, PingFederate redirects the browser back to your application, which then obtains an OAuth 2.0 access token and displays the related user information.

[**Test app**[icon: chevrons-right, set=fas, size=xs]](03_running-sample-pingfed.html)

---

---
title: Authentication journey tutorial for iOS
description: Prepare
component: sdks
version: latest
page_id: sdks:oidc:tutorials/ios/pingone/index
canonical_url: https://docs.pingidentity.com/sdks/latest/oidc/tutorials/ios/pingone/index.html
llms_txt: https://docs.pingidentity.com/sdks/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  before_you_begin: Before you begin
  step_1_download_the_samples: Step 1. Download the samples
  step_2_configure_connection_properties: Step 2. Configure connection properties
  step_3_test_the_app: Step 3. Test the app
---

# Authentication journey tutorial for iOS

* [Prepare](00_before-you-begin.html)

* [Download](01_downloading-forgerocksdk.html)

* [Configure](02_configuring-sample-for-pingone.html)

* [Run](03_running-sample-pingone.html)

***

**In this tutorial you update a sample app that uses OIDC-based login to obtain tokens by redirecting to the PingOne UI for authentication.**

The sample connects to the `.well-known` endpoint of your PingOne server to obtain the correct URIs to authenticate the user, and redirects to your PingOne server's login UI.

After authentication, PingOne redirects the browser back to your application, which then obtains an OAuth 2.0 access token and displays the related user information.

## [Before you begin](00_before-you-begin.html)

Before you begin this tutorial ensure you have set up your PingOne server with the required configuration.

For example, you will need to have an OAuth 2.0 client application set up, and a demo user to authenticate.

[**Complete prerequisites**[icon: chevrons-right, set=fas, size=xs]](00_before-you-begin.html)

## [Step 1. Download the samples](01_downloading-forgerocksdk.html)

To start this tutorial, you need to download the SDK sample apps repo, which contains the projects you will use.

[**Start step 1**[icon: chevrons-right, set=fas, size=xs]](01_downloading-forgerocksdk.html)

## [Step 2. Configure connection properties](02_configuring-sample-for-pingone.html)

In this step, you configure the sample app to connect to the OAuth 2.0 application you created in PingOne.

[**Start step 2**[icon: chevrons-right, set=fas, size=xs]](02_configuring-sample-for-pingone.html)

## [Step 3. Test the app](03_running-sample-pingone.html)

To test the app, run the sample that you configured in the previous step.

The sample connects to your PingOne server to obtain the correct URIs to authenticate the user, and redirects the browser to your PingOne server.

After authentication, PingOne redirects the browser back to your application, which then obtains an OAuth 2.0 access token and displays the related user information.

[**Test app**[icon: chevrons-right, set=fas, size=xs]](03_running-sample-pingone.html)

---

---
title: Authentication journey tutorial for JavaScript
description: Prepare
component: sdks
version: latest
page_id: sdks:sdks:tutorials/javascript/index
canonical_url: https://docs.pingidentity.com/sdks/latest/sdks/tutorials/javascript/index.html
llms_txt: https://docs.pingidentity.com/sdks/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
page_aliases: ["javascript:configuring/configuring-forgerock-sdk-settings-for-your-javascript-app.adoc", "sdks:integrations/IntegrateyourSPAwithFIDC.adoc"]
section_ids:
  before_you_begin: Before you begin
  step_1_download_the_samples: Step 1. Download the samples
  step_2_install_the_dependencies: Step 2. Install the dependencies
  step_3_configure_connection_properties: Step 3. Configure connection properties
  step_4_test_the_app: Step 4. Test the app
---

# Authentication journey tutorial for JavaScript

* [Prepare](00_before-you-begin.html)

* [Download](01_downloading-forgerocksdk.html)

* [Install](02_configuring-forgerocksdk-core-project-js.html)

* [Configure](03_configuring-sample-forgerocksdk-js.html)

* [Run](04_running-sample-forgerocksdk-js.html)

***

**In this tutorial you update a sample app to step through an authentication journey, meaning you get to design and implement the user interface to your requirements.**

The sample navigates through a simple authentication journey, and obtains OAuth 2.0 tokens for the user.

## [Before you begin](00_before-you-begin.html)

Before you begin this tutorial ensure you have set up your PingOne Advanced Identity Cloud tenant or PingAM server with the required configuration.

For example, you will need to configure CORS, have an OAuth 2.0 client application set up, as well as an authentication journey for the app to navigate.

[**Complete prerequisites**[icon: chevrons-right, set=fas, size=xs]](00_before-you-begin.html)

## [Step 1. Download the samples](01_downloading-forgerocksdk.html)

To start this tutorial, you need to download the SDK sample apps repo, which contains the projects you will use.

[**Start step 1**[icon: chevrons-right, set=fas, size=xs]](01_downloading-forgerocksdk.html)

## [Step 2. Install the dependencies](02_configuring-forgerocksdk-core-project-js.html)

The sample projects need a number of dependencies that you can install by using the `npm` command.

For example, the Ping (ForgeRock) SDK for JavaScript itself is one of the dependencies.

[**Start step 2**[icon: chevrons-right, set=fas, size=xs]](02_configuring-forgerocksdk-core-project-js.html)

## [Step 3. Configure connection properties](03_configuring-sample-forgerocksdk-js.html)

In this step, you configure the "embedded-login" sample app to connect to the OAuth 2.0 application you created in PingOne Advanced Identity Cloud or PingAM.

[**Start step 3**[icon: chevrons-right, set=fas, size=xs]](03_configuring-sample-forgerocksdk-js.html)

## [Step 4. Test the app](04_running-sample-forgerocksdk-js.html)

The final step is to run the sample app. The sample connects to your server and walks through your authentication journey or tree.

After successful authentication, the sample obtains an OAuth 2.0 access token and displays the related user information.

[**Test app**[icon: chevrons-right, set=fas, size=xs]](04_running-sample-forgerocksdk-js.html)

---

---
title: Authentication journey tutorial for ReactJS
description: In this tutorial you build out a sample ReactJS SPA and make use of a Node.js REST API server sample app.
component: sdks
version: latest
page_id: sdks:sdks:tutorials/reactjs/index
canonical_url: https://docs.pingidentity.com/sdks/latest/sdks/tutorials/reactjs/index.html
llms_txt: https://docs.pingidentity.com/sdks/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  before_you_begin: Before you begin
  step_1_download_the_samples: Step 1. Download the samples
  step_2_configure_connection_properties: Step 2. Configure connection properties
  step_3_build_and_run_the_projects: Step 3. Build and run the projects
  step_4_implement_authentication_using_the_ping_forgerock_sdk: Step 4. Implement authentication using the Ping (ForgeRock) SDK
  step_5_start_an_oauth_2_0_flow: Step 5. Start an OAuth 2.0 flow
  step_6_manage_access_tokens: Step 6. Manage access tokens
  step_7_handle_logout_requests: Step 7. Handle logout requests
  step_8_test_the_app: Step 8. Test the app
---

# Authentication journey tutorial for ReactJS

**In this tutorial you build out a sample ReactJS SPA and make use of a Node.js REST API server sample app.**

This guide uses the Ping (ForgeRock) SDK for JavaScript to implement the following application features:

* Dynamic authentication form for login.

* OAuth/OIDC token acquisition through the Authorization Code Flow with PKCE.

* Protected client-side routing.

* Resource requests to a protected REST API.

* Log out - revoke tokens and end session.

![The to-do sample app](../../../_images/build-reactjs-app/todos-page-with-todos.png)Figure 1. Screenshot of the to-do page of the sample app

## [Before you begin](00_before-you-begin.html)

Before you begin this tutorial ensure you have set up your PingOne Advanced Identity Cloud tenant or PingAM server with the required configuration.

For example, you will need to configure CORS, have an OAuth 2.0 client application set up, as well as an authentication journey for the app to navigate.

[**Complete prerequisites**[icon: chevrons-right, set=fas, size=xs]](00_before-you-begin.html)

## [Step 1. Download the samples](01_downloading-forgerocksdk.html)

To start this tutorial, you need to download the SDK sample apps repo, which contains the projects you will use.

[**Start step 1**[icon: chevrons-right, set=fas, size=xs]](01_downloading-forgerocksdk.html)

## [Step 2. Configure connection properties](02_configure-the-projects.html)

Configure both the Todo client app, and the API backend server app to connect to the OAuth 2.0 application you created in PingOne Advanced Identity Cloud or PingAM.

[**Start step 2**[icon: chevrons-right, set=fas, size=xs]](02_configure-the-projects.html)

## [Step 3. Build and run the projects](03_build_and_run_the_app.html)

In this step you build and run the API backend server app, and then the Todo client app.

There are also troubleshooting tips if the apps do not start as expected.

[**Start step 3**[icon: chevrons-right, set=fas, size=xs]](03_build_and_run_the_app.html)

## [Step 4. Implement authentication using the Ping (ForgeRock) SDK](04_implement_the_sdk.html)

In this step you implement the Ping (ForgeRock) SDK into the Todo client app, so that it authenticates a user and handles the responses from your PingOne Advanced Identity Cloud tenant or PingAM server.

[**Start step 4**[icon: chevrons-right, set=fas, size=xs]](04_implement_the_sdk.html)

## [Step 5. Start an OAuth 2.0 flow](05_implement_oidc.html)

In this step you use the session token you received in the previous step to start an Oauth 2.0 flow.

[**Start step 5**[icon: chevrons-right, set=fas, size=xs]](05_implement_oidc.html)

## [Step 6. Manage access tokens](06_handling_access_tokens.html)

In this step you implement code to handle the presence of an access token, and getting user info from the OAuth 2.0 endpoint.

[**Start step 6**[icon: chevrons-right, set=fas, size=xs]](06_handling_access_tokens.html)

## [Step 7. Handle logout requests](07_handling_sign_out.html)

In this step you implement code to terminate the session and revoke tokens.

[**Start step 7**[icon: chevrons-right, set=fas, size=xs]](07_handling_sign_out.html)

## [Step 8. Test the app](08_testing_the_app.html)

In this final step you run the completed sample application.

[**Test it out**[icon: chevrons-right, set=fas, size=xs]](08_testing_the_app.html)

---

---
title: Authentication security
description: The Ping (ForgeRock) SDKs provide two methods for implementing authentication in your applications:
component: sdks
version: latest
page_id: sdks:sdks:security/security-authn
canonical_url: https://docs.pingidentity.com/sdks/latest/sdks/security/security-authn.html
llms_txt: https://docs.pingidentity.com/sdks/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: Wed, 17 May 2023 14:10:20 +0100
keywords: ["PingOne Advanced Identity Cloud", "PingAM", "Journeys", "Setup &amp; Configuration", "Source Code", "Security", "SDK"]
---

# Authentication security

The Ping (ForgeRock) SDKs provide two methods for implementing authentication in your applications:

* Auth journey (embedded) login

  The app developer is responsible for building the login and registration UI.

  Uses the [Authorization code grant with PKCE](https://docs.pingidentity.com/pingam/8/oauth2-guide/oauth2-authz-grant-pkce.html) flow, based on [RFC7636](https://datatracker.ietf.org/doc/html/rfc7636).

  When using auth journeys for authentication, the SDKs do not store user credentials on the device or in the browser.

* OIDC (centralized) login

  We provide a central login UI that app developers can use with a redirect for JavaScript apps, or by using an in-app browser in Android and iOS applications.

  Android and iOS use the OAuth 2.0 for Native Apps, based on [RFC8252](https://datatracker.ietf.org/doc/html/rfc8252), which is recommended way for third-party applications to authenticate in terms of security, as user credentials are never exposed to the third-party web or native application.

Both options have their merits and drawbacks, and the choice usually depends on your use case. For more information, refer to:

* [Auth journey (embedded) login](../index.html)

* [OIDC (centralized) login](../../oidc/index.html)

The Ping (ForgeRock) SDKs also use the following protocols for authentication:

* WebAuthn for Mobile and Web Biometrics

  Based on the [WebAuthn W3C spec](https://www.w3.org/TR/webauthn/).

  * The Ping (ForgeRock) SDK for iOS uses a custom implementation of the protocol that has been created to offer backward compatibility older iOS versions including iOS 12. For more information, see [Supported operating systems](../../release-notes/compatibility.html#supported-os).

  * The Ping (ForgeRock) SDK for Android uses the [Google FIDO2 API](https://developers.google.com/identity/fido/android/native-apps).

---

---
title: Before you begin
description: You need to download the SDK sample apps repo, which contains the projects you will use for this tutorial.
component: sdks
version: latest
page_id: sdks:oidc:use-cases/custom-login-ui/00-before-you-begin
canonical_url: https://docs.pingidentity.com/sdks/latest/oidc/use-cases/custom-login-ui/00-before-you-begin.html
llms_txt: https://docs.pingidentity.com/sdks/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: Thu, 20 Feb 2025 10:30:37 +0100
keywords: ["OAuth 2.0", "OpenID Connect", "SDK"]
section_ids:
  step_1_downloading_the_samples: Step 1. Downloading the samples
  step_2_installing_the_dependencies: Step 2. Installing the dependencies
  step_3_hosting_the_sample_apps: Step 3. Hosting the sample apps
  obtaining_your_local_ip_address: Obtaining your local IP address
  creating_a_dns_alias_for_the_javascript_client_application: Creating a DNS alias for the JavaScript client application
---

# Before you begin

## Step 1. Downloading the samples

You need to download the SDK sample apps repo, which contains the projects you will use for this tutorial.

1. In a web browser, navigate to the [SDK Sample Apps repository](https://github.com/ForgeRock/sdk-sample-apps).

2. Download the source code using one of the following methods:

   * Download a ZIP file

     1. Click **Code**, and then click **Download ZIP**.

     2. Extract the contents of the downloaded ZIP file to a suitable location.

   * Use a Git-compatible tool to clone the repo locally

     1. Click **Code**, and then copy the HTTPS URL.

     2. Use the URL to clone the repository to a suitable location.

        For example, from the command-line you could run:

        ```shell
        git clone https://github.com/ForgeRock/sdk-sample-apps.git
        ```

The result of these steps is a local folder named `sdk-sample-apps`.

## Step 2. Installing the dependencies

In the following procedure, you install the required modules and dependencies, including the Ping (ForgeRock) SDK for JavaScript.

1. In a terminal window, navigate to the `sdk-sample-apps/javascript` folder.

2. To install the required packages, enter the following:

   ```shell
   npm install
   ```

   The `npm` tool downloads the required packages, and places them inside a `node_modules` folder.

## Step 3. Hosting the sample apps

In a production scenario your custom login UI app would have its own fully-qualified domain name that your Android, iOS, and JavaScript clients could all connect to.

For simplicity, in this tutorial you will serve your custom login UI app from the local IP address of your host computer.

Using the local IP of your host computer means Android and iOS apps running on a simulator can resolve the address, and also JavaScript apps running locally.

### Obtaining your local IP address

Complete the following steps to obtain your local IP address:

* Windows

* macOS

1. In a command prompt, enter `ipconfig /all`

   Windows displays information about the network adapters in your computer.

   > **Collapse: Show example output**
   >
   > ```
   > Windows IP Configuration
   >    Host Name . . . . . . . . . . . . : Windows
   >    Primary Dns Suffix  . . . . . . . :
   >    Node Type . . . . . . . . . . . . : Hybrid
   >    IP Routing Enabled. . . . . . . . : No
   >    WINS Proxy Enabled. . . . . . . . : No
   >
   > Ethernet adapter Ethernet:
   >    Media State . . . . . . . . . . . : Media disconnected
   >    Description . . . . . . . . . . . : E3100G 2.5 Gigabit Ethernet Controller
   >    Physical Address. . . . . . . . . : 74-34-E2-2b-30-44
   >    DHCP Enabled. . . . . . . . . . . : Yes
   >    Autoconfiguration Enabled . . . . : Yes
   >
   > Wireless LAN adapter Local Area Connection* 1:
   >    Media State . . . . . . . . . . . : Media disconnected
   >    Description . . . . . . . . . . . : Microsoft Wi-Fi Direct Virtual Adapter
   >    Physical Address. . . . . . . . . : 67-6C-EB-B3-46-82
   >    DHCP Enabled. . . . . . . . . . . : Yes
   >    Autoconfiguration Enabled . . . . : Yes
   >
   > Wireless LAN adapter Wi-Fi:
   >    Description . . . . . . . . . . . : Wireless Network Adapter (210NGW)
   >    Physical Address. . . . . . . . . : 87-6C-DF-C9-17-90
   >    DHCP Enabled. . . . . . . . . . . : Yes
   >    Autoconfiguration Enabled . . . . : Yes
   >    IPv6 Address. . . . . . . . . . . : 2406:3d08:2f61:1400::2d47
   >    Lease Obtained. . . . . . . . . . : January 27, 2025 11:09:26 AM
   >    Lease Expires . . . . . . . . . . : January 28, 2025 6:09:26 AM
   >    IPv6 Address. . . . . . . . . . . : 2406:3d08:2f61:1400::2d47
   >    Temporary IPv6 Address. . . . . . : 2604:2b08:2f93:2600:b479:b5b4:25ff:acc8
   >    Link-local IPv6 Address . . . . . : fe54::d9e5:16ff:d9d4:e22%10
   >    IPv4 Address. . . . . . . . . . . : 192.168.0.35
   >    Subnet Mask . . . . . . . . . . . : 255.255.255.0
   >    Lease Obtained. . . . . . . . . . : January 27, 2025 11:09:24 AM
   >    Lease Expires . . . . . . . . . . : January 29, 2025 11:09:26 AM
   >    Default Gateway . . . . . . . . . : fe80::bb8:c0ee:fea5:8c58%10
   >                                        192.168.0.1
   >    DHCP Server . . . . . . . . . . . : 192.168.0.1
   >    DHCPv6 IAID . . . . . . . . . . . : 893252287
   >    DHCPv6 Client DUID. . . . . . . . : 00-01-00-01-1b-87-59-2D-74-86-C4-3C-30-88
   >    DNS Servers . . . . . . . . . . . : 2025:4e8:0:230b::11
   >                                        2025:4e8:0:230c::11
   >                                        8.8.8.8
   >    NetBIOS over Tcpip. . . . . . . . : Enabled
   > ```

2. Ignoring adapters where the **Media State** property is listed as `Media Disconnected`, locate the ethernet or wireless adapter that connects to your router.

3. Make a note of the **IPv4 Address** field.

   |   |                                                                                                                                                       |
   | - | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | The address will often start with `192.168.`, `10.0.`, or `172.16.`, which are the first digits of the commonly used reserved private IPv4 addresses. |

   In this case, the local IPv4 IP address is `192.168.0.35`.

   You will use this address to access your custom UI app for this tutorial.

1) In a terminal window, enter `ifconfig`

   macOS displays information about the network interfaces in your computer.

   > **Collapse: Show example output**
   >
   > ```
   > lo0: flags=8049<UP,LOOPBACK,RUNNING,MULTICAST> mtu 16384
   > 	options=1203<RXCSUM,TXCSUM,TXSTATUS,SW_TIMESTAMP>
   > 	inet 127.0.0.1 netmask 0xff000000
   > 	inet6 ::1 prefixlen 128
   > 	inet6 fe80::1%lo0 prefixlen 64 scopeid 0x1
   > 	nd6 options=201<PERFORMNUD,DAD>
   > gif0: flags=8010<POINTOPOINT,MULTICAST> mtu 1280
   > stf0: flags=0<> mtu 1280
   > anpi0: flags=8863<UP,BROADCAST,SMART,RUNNING,SIMPLEX,MULTICAST> mtu 1500
   > 	options=400<CHANNEL_IO>
   > 	ether 22:d0:cb:e5:fd:09
   > 	media: none
   > 	status: inactive
   > en3: flags=8863<UP,BROADCAST,SMART,RUNNING,SIMPLEX,MULTICAST> mtu 1500
   > 	options=404<VLAN_MTU,CHANNEL_IO>
   > 	ether f8:e4:3b:ad:67:c5
   > 	inet6 fe80::ca4:9a6c:f835:80c9%en8 prefixlen 64 secured scopeid 0x7
   > 	inet6 fd84:bb80:dd60:23b3:855:171f:3651:b7de prefixlen 64 autoconf secured
   > 	inet 192.168.0.35 netmask 0xffffff00 broadcast 192.168.0.255
   > 	nd6 options=201<PERFORMNUD,DAD>
   > 	media: autoselect (1000baseT <full-duplex>)
   > 	status: active
   > en1: flags=8963<UP,BROADCAST,SMART,RUNNING,PROMISC,SIMPLEX,MULTICAST> mtu 1500
   > 	options=460<TSO4,TSO6,CHANNEL_IO>
   > 	ether 36:e5:80:6e:d1:40
   > 	media: autoselect <full-duplex>
   > 	status: inactive
   > en2: flags=8963<UP,BROADCAST,SMART,RUNNING,PROMISC,SIMPLEX,MULTICAST> mtu 1500
   > 	options=460<TSO4,TSO6,CHANNEL_IO>
   > 	ether 36:e5:80:6e:d1:44
   > 	media: autoselect <full-duplex>
   > 	status: inactive
   > bridge0: flags=8863<UP,BROADCAST,SMART,RUNNING,SIMPLEX,MULTICAST> mtu 1500
   > 	options=63<RXCSUM,TXCSUM,TSO4,TSO6>
   > 	ether 36:e5:80:6e:d1:40
   > 	Configuration:
   > 		id 0:0:0:0:0:0 priority 0 hellotime 0 fwddelay 0
   > 		maxage 0 holdcnt 0 proto stp maxaddr 100 timeout 1200
   > 		root id 0:0:0:0:0:0 priority 0 ifcost 0 port 0
   > 		ipfilter disabled flags 0x0
   > 	member: en1 flags=3<LEARNING,DISCOVER>
   > 	        ifmaxaddr 0 port 11 priority 0 path cost 0
   > 	member: en2 flags=3<LEARNING,DISCOVER>
   > 	        ifmaxaddr 0 port 12 priority 0 path cost 0
   > 	member: en3 flags=3<LEARNING,DISCOVER>
   > 	        ifmaxaddr 0 port 13 priority 0 path cost 0
   > 	media: <unknown type>
   > 	status: inactive
   > ap1: flags=8863<UP,BROADCAST,SMART,RUNNING,SIMPLEX,MULTICAST> mtu 1500
   > 	options=6460<TSO4,TSO6,CHANNEL_IO,PARTIAL_CSUM,ZEROINVERT_CSUM>
   > 	ether d6:0f:2c:90:e9:b6
   > 	nd6 options=201<PERFORMNUD,DAD>
   > 	media: autoselect (none)
   > 	status: inactive
   > en0: flags=8863<UP,BROADCAST,SMART,RUNNING,SIMPLEX,MULTICAST> mtu 1500
   > 	options=6460<TSO4,TSO6,CHANNEL_IO,PARTIAL_CSUM,ZEROINVERT_CSUM>
   > 	ether c6:2a:06:29:ee:28
   > 	nd6 options=201<PERFORMNUD,DAD>
   > 	media: autoselect
   > 	status: inactive
   > utun0: flags=8051<UP,POINTOPOINT,RUNNING,MULTICAST> mtu 1500
   > 	inet6 fe80::a19f:5de6:a4ca:fd90%utun0 prefixlen 64 scopeid 0x13
   > 	nd6 options=201<PERFORMNUD,DAD>
   > ```

2) Looking at interfaces where the **status** property is listed as `active`, locate the ethernet or wireless interface that connects to your router.

   Often the prefix of the interface is `en`.

3) Make a note of the IPv4 address in the **inet** field.

   |   |                                                                                                                                                       |
   | - | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | The address will often start with `192.168.`, `10.0.`, or `172.16.`, which are the first digits of the commonly used reserved private IPv4 addresses. |

   In this case, the local IPv4 IP address is `192.168.0.35`.

   You will use this address to access your custom UI app for this tutorial.

### Creating a DNS alias for the JavaScript client application

You should assign a DNS alias to your localhost address to help differentiate the client application from the custom UI application during this tutorial.

You can choose whatever host name you prefer for your client application. This tutorial uses `sdkapp.example.com`.

Complete the following steps to configure a DNS alias for your local IP address:

* Windows

* macOS

1. As an administrator, in a text editor open the `%SystemRoot%\system32\drivers\etc\hosts` file.

2. Add the following:

   `127.0.0.1 sdkapp.example.com`

3. Close and save the file.

1) As an administrator, in a text editor open the `/etc/hosts` file.

2) Add the following:

   `127.0.0.1 sdkapp.example.com`

3) Close and save the file.