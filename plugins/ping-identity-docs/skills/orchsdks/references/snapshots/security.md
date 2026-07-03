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
