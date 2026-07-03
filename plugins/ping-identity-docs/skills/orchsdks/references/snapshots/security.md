---
title: Authentication security
description: Understand the authentication methods available in the Orchestration SDKs, including auth journey login, OIDC centralized login, and WebAuthn
component: orchsdks
page_id: orchsdks::security/security-authn
canonical_url: https://developer.pingidentity.com/orchsdks/security/security-authn.html
llms_txt: https://developer.pingidentity.com/orchsdks/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: Wed, 17 May 2023 14:10:20 +0100
keywords: ["PingOne Advanced Identity Cloud", "PingAM", "Journeys", "Setup &amp; Configuration", "Source Code", "Security", "SDK"]
---

# Authentication security

The Orchestration SDKs provide two methods for implementing authentication in your applications:

* Auth journey (embedded) login

  The app developer is responsible for building the login and registration UI.

  Uses the [Authorization code grant with PKCE](https://docs.pingidentity.com/pingam/8/oauth2-guide/oauth2-authz-grant-pkce.html) flow, based on [RFC7636](https://datatracker.ietf.org/doc/html/rfc7636).

  When using auth journeys for authentication, the SDKs do not store user credentials on the device or in the browser.

* OIDC (centralized) login

  We provide a central login UI that app developers can use with a redirect for JavaScript apps, or by using an in-app browser in Android and iOS applications.

  Android and iOS use the OAuth 2.0 for Native Apps, based on [RFC8252](https://datatracker.ietf.org/doc/html/rfc8252), which is recommended way for third-party applications to authenticate in terms of security, as user credentials are never exposed to the third-party web or native application.

Both options have their merits and drawbacks, and the choice usually depends on your use case. For more information, refer to:

* [Auth journey (embedded) login](../journey/index.html)

* [OIDC (centralized) login](../oidc/index.html)

The Orchestration SDKs also use the following protocols for authentication:

* WebAuthn for Mobile and Web Biometrics

  Based on the [WebAuthn W3C spec](https://www.w3.org/TR/webauthn/).

  * The Orchestration SDK for iOS uses a custom implementation of the protocol that has been created to offer backward compatibility older iOS versions including iOS 12.

  * The Orchestration SDK for Android uses the [Google FIDO2 API](https://developers.google.com/identity/fido/android/native-apps).

---

---
title: Data security
description: Understand how the Orchestration SDKs handle data security, including token storage, SSL Pinning, and certificate key hash configuration for iOS and Android
component: orchsdks
page_id: orchsdks::security/security-data
canonical_url: https://developer.pingidentity.com/orchsdks/security/security-data.html
llms_txt: https://developer.pingidentity.com/orchsdks/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: Wed, 17 May 2023 14:10:20 +0100
keywords: ["PingOne Advanced Identity Cloud", "PingAM", "Journeys", "Setup &amp; Configuration", "Source Code", "Security", "SDK"]
---

# Data security

The Orchestration SDKs do not save or load any user data, such as username or password, or personal information in memory. The only stored keys and data are the [Session and OAuth 2.0 tokens](security-tokens.html) required for authentication, and security-related certificates hashes.

The Orchestration SDKs for iOS and Android support *SSL Pinning*. The certificate information used is passed in the form of certificate key hashes in the SDKs configuration file. This means you do not have to bundle certificates with your iOS `.ipa` or Android `.apk` files.

---

---
title: OAuth 2.0 security with PKCE
description: Use PKCE with PingOne Advanced Identity Cloud or PingAM to secure OAuth 2.0 authorization code grants for native apps and SPAs without exposing a client secret
component: orchsdks
page_id: orchsdks::security/oauth2-pkce
canonical_url: https://developer.pingidentity.com/orchsdks/security/oauth2-pkce.html
llms_txt: https://developer.pingidentity.com/orchsdks/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: Wed, 17 May 2023 14:10:20 +0100
keywords: ["PingOne Advanced Identity Cloud", "PingAM", "Journeys", "Setup &amp; Configuration", "Source Code", "Security", "SDK"]
section_ids:
  how_pkce_works: How PKCE works
---

# OAuth 2.0 security with PKCE

Proof Key for Code Exchange (PKCE) mitigates the risks of an OAuth 2.0 attack. Without PKCE, a malicious application running in the same browser as your public client app could compromise the security of your app.

It is good practice to use PKCE for native apps and SPAs, because the code is stored on browsers and devices. Without PKCE, you'd have to include a client secret in those public-facing apps. For enhanced security, you should use PKCE whenever you have the option to use it.

## How PKCE works

Your app, with the help of our code, generates a `code_verifier` (nonce). When a user make a request, your app creates a hash of that `code_verifier` as a `code_challenge`. ForgeRock, as an authorization server, saves the hash value.

After the hash is confirmed as valid, your app exchanges its authorization code grant for an access token. Your client app, as the bearer, can use the token to access to the user's resources.

This diagram depicts the authorization code grant flow in detail:

Figure 1. Authorization code grant flow with PKCE

If you're familiar with OpenID Connect (OIDC) specifications, the web app is the *relying party*, and PingOne Advanced Identity Cloud or PingAM is the *authorization server*.

For more information on PKCE standards, see the following IETF document: [Proof key for code exchange by OAuth public clients](https://www.rfc-editor.org/rfc/rfc7636).

For more information on how we implement PKCE for native and SPA apps, refer to [Authorization code grant with PKCE](https://docs.pingidentity.com/pingam/8/oauth2-guide/oauth2-authz-grant-pkce.html).

---

---
title: Security
description: Explore how the Orchestration SDKs secure token material, authentication protocols, app data, and OAuth 2.0 flows using industry best practices
component: orchsdks
page_id: orchsdks::security/index
canonical_url: https://developer.pingidentity.com/orchsdks/security/index.html
llms_txt: https://developer.pingidentity.com/orchsdks/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: Wed, 17 May 2023 14:10:20 +0100
keywords: ["PingOne Advanced Identity Cloud", "PingAM", "Journeys", "Setup &amp; Configuration", "Source Code", "Security", "SDK"]
---

# Security

The Orchestration SDKs are built from the ground up to use best practices for securing token material and data.

Security is a very broad subject, and every environment is different. Readers are expected to do their own research and complement the information found in these topics.

[icon: file-certificate, set=fadr, size=3x]

#### [Tokens and keys](security-tokens.html)

Learn how the Orchestration SDKs secure your session and OAuth 2.0-related tokens, and the encryption used.

[icon: user-shield, set=fadr, size=3x]

#### [Authentication](security-authn.html)

Discover the protocols the Orchestration SDKs use when your app authenticates your users.

[icon: binary-lock, set=fadr, size=3x]

#### [Data](security-data.html)

What data do the Orchestration SDKs use, and what security measures help to protect it.

[icon: swap, set=fadr, size=3x]

#### [OAuth 2.0](oauth2-pkce.html)

See how the Orchestration SDKs use Proof Key for Code Exchange (PKCE) to mitigate the risks of an OAuth 2.0 attack.

---

---
title: Token and key security
description: Understand how the Orchestration SDKs store, refresh, and encrypt tokens and keys using platform hardware-backed security on Android, iOS, and JavaScript
component: orchsdks
page_id: orchsdks::security/security-tokens
canonical_url: https://developer.pingidentity.com/orchsdks/security/security-tokens.html
llms_txt: https://developer.pingidentity.com/orchsdks/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: Tue, 18 Apr 2023 11:57:06 +0100
keywords: ["PingOne Advanced Identity Cloud", "PingAM", "Journeys", "Setup &amp; Configuration", "Source Code", "Security", "SDK"]
section_ids:
  token_storage: Token storage
  session_tokens_and_cookies: Session tokens and cookies
  id_access_and_refresh_tokens: ID, access, and refresh tokens
  encryption_key_storage: Encryption key storage
  hardware-backed-key-storage: Hardware-backed key storage and encryption
---

# Token and key security

The Orchestration SDKs handle and store keys and tokens based on the security best practices of each platform.

## Token storage

Depending on the authentication use case, the SDKs will potentially have to store and be able to retrieve the session cookie, ID tokens, access tokens, and refresh tokens.

Each token is serving a different use case, and as such how the SDKs handle them can be different.

The following sections cover how the SDKs handle different types of tokens.

### Session tokens and cookies

* On Android and iOS, the session tokens are stored in either the [Android keystore](https://developer.android.com/training/articles/keystore) or [iOS keychain](https://stash.forgerock.org/projects/DX/repos/sdks-docs/pull-requests/119/overview) after authentication completes. The tokens are encrypted using a hardware-backed security key when possible and can be retrieved by the SDK on request.

* When using the Orchestration SDK for JavaScript, cookies are stored in the browser's cookie storage. The cookie name matches the one provided by PingAM (such as `iPlanetDirectoryPro`) and its value is the actual session token. When making requests to PingAM, the value is passed as an authentication cookie. This cookie is configured with the `HTTPOnly` and `Secure` attributes, which provide additional layers of security.

### ID, access, and refresh tokens

* On Android and iOS when authorization is completed any OAuth 2.0-related tokens are stored securely locally, encrypted using a hardware-backed security key when possible and can be retrieved by the SDK on request. Tokens **are not** configured as *cloud sharable* by default.

* When using the Orchestration SDK for JavaScript, the OAuth 2.0 Tokens are stored by using one of the web storage APIs provided by the browser. By default, this uses the browser's `localStorage`, but the SDK also supports `sessionStorage`.

  |   |                                                                                                                                                                                                                                            |
  | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
  |   | We recommend that JavaScript single-page applications do not use refresh tokens or any other long-running authorization elements due to the potentially unsecure nature of the storage mechanisms provided by browsers. == Token lifecycle |

The session and OAuth 2.0-related tokens the SDKs handle all have associated expiry times. When a token reaches its expiry time it becomes unusable.

A feature of the SDKs is that they manage the refresh of *OAuth 2.0 tokens*. The timing of the refresh is based on a threshold value to improve the end-user experience. The SDKs refresh tokens automatically when the token is requested from storage to be used in your application and its expiry is within the threshold.

In the case of access tokens, if a refresh token is present, then the Android and iOS SDKs will use it to obtain a new access token. If the refresh token cannot be used, is not present, or if it has expired, then the SDKs fall back to using the session token to start a new OAuth 2.0 flow.

|   |                                                                                                                                    |
| - | ---------------------------------------------------------------------------------------------------------------------------------- |
|   | The SDKs do not handle the refresh of *session tokens*. If a session token has expired, the app needs to re-authenticate the user. |

When an OAuth 2.0 or session token expires, the SDK removes any respective tokens from the secure storage and performs a cleanup. The Android and iOS SDKs also check if the current session token is the same one used to obtain the OAuth 2.0 tokens. In case of a mismatch, then these orphaned tokens are cleaned.

When using SDK logout methods to perform a `Logout` event, the SDKs revoke existing OAuth 2.0 tokens, revoke the session, and perform a local cleanup. If the SDKs are unable to revoke the session at the server—​for example the network is unavailable—​then the SDKs remove the tokens from local storage.

When using the Orchestration SDK for JavaScript, if an access token expires within the threshold limit or returns an HTTP `401 Unauthorized` error, the SDK attempts to renew it using the same session cookie that was performing the authorization code OAuth 2.0 flow.

The Orchestration SDK for JavaScript calls the `endSession` and `session?action=logout` endpoints during logout, as well as calling `revoke` whenever you use `FRUser.logout`. This ensures that the **server** invalidates the session cookie.

|   |                                                                                                                                                                                                                                     |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The Orchestration SDK for JavaScript has no *direct* control over the session cookie; it can only make requests to the browser that may or may not be acted upon. Instead, it must rely on the server to manage the cookie removal. |

## Encryption key storage

On supported platforms and devices, the Orchestration SDKs generate [Hardware-Backed encryption keys](#hardware-backed-key-storage), and uses them to encrypt and store tokens. This provides an extra level of security against attacks.

* The Orchestration SDK for iOS uses the `kSecKeyAlgorithmECIESEncryptionCofactorX963SHA256AESGCM` encryption algorithm. The key is stored in the *Secure Enclave*.

  On unsupported devices, the SDK cannot not enforce hardware-backed encryption and will save the tokens in the iOS keychain.

* The Orchestration SDK for Android uses a number of different algorithms, depending on the OS version and device functionality. It supports the following encryptors:

  * `AndroidLEncryptor`: RSA

  * `AndroidMEncryptor`: AES

  * `AndroidNEncryptor`: Similar to ***M***, with the addition of setting `setInvalidatedByBiometricEnrollment` to `true`

  * `AndroidPEncryptor`: Similar to ***N***, with the addition of using *Android Strongbox*

### Hardware-backed key storage and encryption

Both the Android and iOS SDKs use platform-provided methods to create hardware-backed encryption keys.

* On iOS the SDK creates keys within the `SecuredKey.swift` class. If `SecuredKey` generation fails, the `KeychainManager` generates the `KeychainService` with no `SecuredKey`. The values in this case will be added to the iOS keychain as `kSecClassGenericPassword` types.

  If `SecuredKey` creation is successful then the value is encrypted before being stored. The `SecuredKey.swift` class provides an `isAvailable()` public method that validates whether creation of the `SecuredKey` using Secure Enclave is available on the device or not.

  |   |                                                                                                                  |
  | - | ---------------------------------------------------------------------------------------------------------------- |
  |   | The SDKs also support devices that do not have Secure Enclave or other hardware-backed encryption functionality. |

* On Android, the SDK uses `DefaultTokenManager` and `DefaultSingleSignOnManager` for storing tokens, in addition to `SecuredSharedPreferences` on supported devices.

  Depending on the Android version, the SDK can use more specific encryptors. For more information, see `getEncryptor`. For information about the different encryptor classes, see the `auth` folder in GitHub.