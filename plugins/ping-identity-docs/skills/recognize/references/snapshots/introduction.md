---
title: Account recovery
description: This page explains the options customers have when using PingOne Recognize to support account recovery.
component: recognize
page_id: recognize:introduction:account_recovery
canonical_url: https://docs.pingidentity.com/recognize/introduction/account_recovery.html
llms_txt: https://docs.pingidentity.com/recognize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: April 15, 2026
section_ids:
  enroll-a-new-device-via-client-state: Enroll on a new device
  how-it-works: How it works
  managing-multiple-enrolled-devices: Managing multiple enrolled devices
  keyless-client-devices: PingOne Recognize Client Devices
---

# Account recovery

PingOne Recognize helps organizations recover accounts and enroll new devices when users lose access to their originally enrolled device. The account recovery and device enrollment flows use the PingOne Recognize Mobile SDK.

PingOne Recognize offers two services as part of a device or account recovery experience:

* [Enroll a new device](#enroll-a-new-device-via-client-state)

* [Managing multiple enrolled devices](#managing-multiple-enrolled-devices)

## Enroll on a new device

For customers who've already established trusted alternative second factors, such as passwords, SMS one-time passwords (OTPs), or email magic links, PingOne Recognize's face matching is typically used in combination with existing factors to enroll the new device.

### How it works

1. The user downloads the app on a new device, enters their username, and authenticates using a first factor (for example, password, SMS OTP, or email magic link).

2. Customers invoke the PingOne Recognize Mobile SDK, retrieve the PingOne Recognize ID associated with the user and the client state generated during enrollment, and send this to the SDK to enable secure account recovery.

3. The SDK recovery flow captures a selfie and authenticates that the originally enrolled user is genuinely present, without revealing or processing biometric data outside the user's device.

4. If successful, the new device is bound to the user's identity, enabling ongoing authentication for login, step-up, or payment use cases.

5. Optional: Users can review and [delete previously bound devices](#managing-multiple-enrolled-devices).

Learn more in [Account Recovery (Mobile SDK)](../mobile-sdk/mobile-sdk-account-recovery.html).

Learn more in [Retrieve and delete devices via API](https://docs.keyless.io/consumer/server-api/devices).

## Managing multiple enrolled devices

Customers can use the API to retrieve and delete devices bound to user identities. This allows users to have multiple devices and reduces risks associated with device loss.

Use GET and DELETE APIs to build a device management experience that allows users to:

* View and manage bound devices.

* Delete any listed device.

* Add a new device when needed.

Learn more in [GET and DELETE user devices](https://docs.keyless.io/consumer/server-api/devices)

Learn more in [Add user device](../mobile-sdk/mobile-sdk-account-recovery.html)

## PingOne Recognize Client Devices

For account recovery, PingOne Recognize Client Devices and Client States are relevant subsets of device entities. PingOne Recognize Client Devices represent user profiles containing non-PII data that allows a user to authenticate on a new device or channel (mobile or web apps).

Within this category, PingOne Recognize allows customers to generate a **Client State** during enrollment for device types before activation or binding for ongoing two-factor authentication. After binding, a new **SDK Device** is generated. Each device receives a DeviceID and can be one of the following types:

1. **Backup:** The **Client State** typically stored by the PingOne Recognize customer so a user can later authenticate on a new camera-enabled physical device. Generated through IDV Bridge or Live Enrollment and later used during account recovery.

2. **Temporary:** Similar to Backup, but recommended when the customer does not need to store the client state beyond the current flow, such as when enrollment is immediately followed by activation or binding.

3. **SDK:** Applied when a user profile has been activated through a mobile or web app to support ongoing authentication via the Mobile SDK. It contains additional keys and metadata to support device and facial authentication in a privacy-preserving manner.

---

---
title: Authentication
description: This page explains the use cases and deployment methods for PingOne Recognize authentication.
component: recognize
page_id: recognize:introduction:authentication
canonical_url: https://docs.pingidentity.com/recognize/introduction/authentication.html
llms_txt: https://docs.pingidentity.com/recognize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: April 15, 2026
section_ids:
  login: Sign-on
  mobile-sdk: Mobile SDK
  web-sdk: Web SDK
  step-up: Step-up
  payments: Payment authentication (PSD2/3 compliant)
  no-camera-preview-beta: No camera preview [BETA]
---

# Authentication

After users are enrolled, you can use PingOne Recognize to authenticate them at three different steps of a user journey:

* [Sign-on](#login)

* [Step-up](#step-up)

* [Payments](#payments)

## Sign-on

Use the PingOne Recognize login flow to verify the enrolled user and device before granting access.

### Mobile SDK

PingOne Recognize offers Android and iOS SDKs to enable logins from your app's login or account creation page. Flutter and React Native (BETA) bridges are also supported.

The captured image is securely encrypted and sent to the PingOne Recognize server to verify a match to the originally enrolled user. No biometric data is stored.

The Mobile SDK can also generate a JSON Web Token (JWT) with a custom payload, allowing customers to manage and audit login sessions.

Learn more:

* [Mobile SDK](../mobile-sdk/mobile-sdk-authentication.html)

* [JWT Signing](../mobile-sdk/mobile-sdk-jwt-signing.html)

### Web SDK

Customers can integrate the login flow into their own web-based services.

Learn more in [Web SDK^](../web-sdk/web-sdk-getting-started.html).

## Step-up

PingOne Recognize provides in-app step-up authentication for high-risk actions like address or credential changes, offering stronger security than passwords or SMS one-time passwords (OTPs).

The authentication flow is identical to the [Login](#login) process, whether you use the Mobile SDK or the Web SDK. The JWT signing feature can help customers verify changes made in a custom payload.

## Payment authentication (PSD2/3 compliant)

PingOne Recognize offers dynamic linking for businesses required to comply with PSD2 Strong Customer Authentication (SCA) regulations.

This is supported through a user interface launched using the Mobile SDK, displaying custom payload details, such as transfer amounts and recipients.

Upon successful authentication, the SDK issues a JSON Web Token (JWT) containing a signature of the provided payload.

Per regulatory requirements, PingOne Recognize allows customers to set (enroll) a PIN (personal identification number) as a knowledge factor to authenticate transactions as an alternative to face authentication. This PIN can also be authenticated, changed, or deleted using the API.

Learn more:

* [Dynamic Linking](../mobile-sdk/mobile-sdk-dynamic-linking.html)

* [JWT signing](../mobile-sdk/mobile-sdk-jwt-signing.html)

* [PIN](../mobile-sdk/mobile-sdk-pin-authentication.html)

## No camera preview \[BETA]

PingOne Recognize now offers a "No Camera Preview" variant where a small icon appears as an overlay instead of opening the front-facing camera on the user's device.

This option can be configured using the SDK for any use case, authentication, or user.

Learn more in [Camera Preview Customization (BETA)](../mobile-sdk/mobile-sdk-authentication.html).

---

---
title: Component interoperability
description: This page outlines how customers can allow users to authenticate on different platforms (web/mobile) regardless of which component they initially enroll from by leveraging client state.
component: recognize
page_id: recognize:introduction:component-interoperability
canonical_url: https://docs.pingidentity.com/recognize/introduction/component-interoperability.html
llms_txt: https://docs.pingidentity.com/recognize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  interoperability-between-pingone-recognize-components: Interoperability between PingOne Recognize components
  how-pingone-recognize-client-state-works: How PingOne Recognize client state works
  possible-scenarios-relating-to-interoperability: Possible Scenarios relating to interoperability
---

# Component interoperability

PingOne Recognize currently consists of three main product components:

| Component                      | Facilitates user enrollment | Enables authentication |
| ------------------------------ | --------------------------- | ---------------------- |
| IDV Bridge (OnPremise or Saas) | [icon: check, set=fa]       | [icon: x, set=fa]      |
| Mobile SDK                     | [icon: check, set=fa]       | [icon: check, set=fa]  |
| Web SDK                        | [icon: check, set=fa]       | [icon: check, set=fa]  |

## Interoperability between PingOne Recognize components

All these components can now operate in an interconnected manner. A user can complete the enrollment process on any of these components and later authenticate on a different component without needing to re-enroll.

The technology enabling this seamless interoperability is called the **PingOne Recognize Client State**.

### How PingOne Recognize client state works

The PingOne Recognize client state can be generated by any of the components listed above.

* It can be consumed by either the Web SDK or Mobile SDK to enable cross-platform authentication. Client state is used to authenticate:

* **Mobile SDK**: a new client state is created on this device and for this specific UserID to allow for on-going authentication of that user from that device.

* **Web SDK**: a new client state is stored on the PingOne Recognize server for this specific UserID to allow for ongoing authentication from any browser where the customer chooses to initiate PingOne Recognize as a 2nd factor for authentication.

This interoperability opens up various use cases for PingOne Recognize authentication.

### Possible Scenarios relating to interoperability

1. **Live Enrollment → cross-platform authentication**

   Users enroll into PingOne Recognize by taking a selfie through a PingOne Recognize UI deployed by our customers into their own Mobile or Web apps using our SDKs.

   * [Enroll users through the Web SDK](#web-sdk/web-sdk-guide/enrollment) and then activate them in your Mobile app at a later stage to authenticate there without the need to re-enroll.

   * [Enroll users on the Mobile SDK](#consumer/mobile-sdk-guide/enrollment) and authenticate them in your web application (again without any re-enrollment).

2. **IDV Bridge → cross-platform authentication**

   Customers have captured a selfie, typically during KYC/Onboarding flows, and enroll this image into PingOne Recognize via:

   * **On-Premise** - enroll user selfies through the "PingOne Recognize Agent" component installed inside their own infrastructure, and subsequently allow them to authenticate using your web or mobile app at a later date with client state.

   * This option ensures that the selfies stay within your own infrastructure and therefore the entire process remains 100% privacy preserving.

   * **SaaS** - enroll user selfies through our [authentication service api](../idv-bridge/idv-bridge-saas.html), where the UserID is created instantly and client state can be stored to subsequently authenticate through your web or mobile app.

   * The selfie is sent to a secure enclave in PingOne Recognize and instantly transformed into a cryptographic key. No biometric data or PII is then stored.

---

---
title: Enrollment
description: This page explains two enrollment options customers can use to enroll users into PingOne Recognize for ongoing authentication.
component: recognize
page_id: recognize:introduction:enrollment
canonical_url: https://docs.pingidentity.com/recognize/introduction/enrollment.html
llms_txt: https://docs.pingidentity.com/recognize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: April 15, 2026
section_ids:
  live-enrollment: Live Enrollment
  who-its-for: Who it's for
  what-it-does: What it does
  how-it-works: How it works
  mobile-sdk: Mobile SDK
  web-sdk: Web SDK
  idv-bridge-enrollment: IDV Bridge
  who-its-for-1: Who it's for?
  what-it-does-1: What it does
  how-it-works-2: How it works
---

# Enrollment

Before users can authenticate with PingOne Recognize, they must be enrolled. Enrollment registers a user's face and device, creating a biometric template that future authentication attempts are compared to. PingOne Recognize supports two enrollment methods: live enrollment and IDV Bridge enrollment.

## Live Enrollment

### Who it's for

Businesses that want to use the PingOne Recognize selfie-capture process either:

1. During onboarding of new users.

2. As a way to enhance the authentication experience for existing authenticated users (by enhancing security and usability).

### What it does

With live enrollment, PingOne Recognize provides a user interface to create a digital identity, which is then used as a base template when a user attempts to authenticate in the future.

This involves capturing facial biometrics and device details. Passive liveness technology also helps ensure that the user is a real person.

### How it works

#### Mobile SDK

The PingOne Recognize Mobile SDK allows you to embed selfie capture and enrollment into your own Android or iOS app.

This is the recommended and most secure approach, as the selfie is processed exclusively on the customer's device and no biometric data is stored after enrollment.

Learn more in [Mobile SDK](../mobile-sdk/mobile-sdk-introduction.html).

#### Web SDK

The PingOne Recognize Web SDK allows you to integrate the enrollment experience into your web-based services. The captured image is securely encrypted and sent to the PingOne Recognize server, where it is transformed into a private key. No biometric data is stored.

## IDV Bridge

### Who it's for?

Businesses that have already created a biometric template as part of an existing Know Your Customer (KYC) or Identity Verification (IDV) flow.

### What it does

IDV Bridge uses a user's existing portrait for future authentication attempts. This removes the need for live enrollment while linking PingOne Recognize authentication to a portrait or selfie captured during onboarding.

Typically, clients use this solution in one of two ways:

1. **Bulk upload of selfies:** Clients who've collected a significant number of selfies or identity documents, typically during onboarding or KYC, can use IDV Bridge to passively enroll users into the PingOne Recognize system for ongoing authentication.

2. **Single selfie upload:** Clients that already have a selfie-capture step in their onboarding flow can send this image to IDV Bridge to enroll users into PingOne Recognize without adding an additional step.

This approach reduces risk by transforming facial biometric data into a secure cryptographic key, enabling image deletion, and improving user experience by removing the need for active live enrollment with PingOne Recognize.

### How it works

PingOne Recognize has two deployment options for uploading previously captured face portraits:

1. **IDV Bridge SaaS**: A backend-to-backend option where businesses pass encrypted images to the authentication service API for enrollment.

   Learn more in [IDV Bridge SaaS](https://app.gitbook.com/s/GASbg2fEvbZEZpc4GHMZ/readme/idv-bridge-saas).

---

---
title: Introduction to PingOne Recognize
description: This page introduces PingOne Recognize and helps you navigate the documentation.
component: recognize
page_id: recognize:introduction:introduction_to_p1recognize
canonical_url: https://docs.pingidentity.com/recognize/introduction/introduction_to_p1recognize.html
llms_txt: https://docs.pingidentity.com/recognize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: April 15, 2026
section_ids:
  1-enrollment: 1. Enrollment
  2-authentication: 2. Authentication
  account-recovery: 3. Account recovery
  workforce: 4. Workforce
---

# Introduction to PingOne Recognize

PingOne Recognize provides four functional capabilities for integration into a workflow:

## 1. Enrollment

To authenticate users with PingOne Recognize, they must first be enrolled by registering a face.

This can be done in two ways:

* **Live enrollment:** PingOne Recognize provides a user interface (UI) to create a biometric template that future authentication attempts are compared to. This captures facial biometrics and device details. Passive liveness technology also checks that the user is a real person.

* **IDV Bridge enrollment:** This method is for businesses that already have created a biometric template, typically using a selfie as part of a Know Your Customer (KYC) or Identity Verification (IDV) flow. IDV Bridge uses that template for future authentication attempts. This removes the need for live enrollment while still tying PingOne Recognize authentication to the user's existing biometric template.

Learn more in [Enrollment](enrollment.html).

## 2. Authentication

After users are enrolled, PingOne Recognize can authenticate them at various steps in the user journey. This is done through a UI that confirms the user is the same person who enrolled. With a glance at the camera, the user verifies face and device for multi-factor security and confirms presence using liveness checks.

Typical steps in the user journey include:

* **Login**

* **Step-up actions** (for example, changing personal data)

* **Payment authentication** (using PingOne Recognize Strong Customer Authentication (SCA) and dynamic linking)

Learn more in [Authentication](authentication.html).

## 3. Account recovery

Because PingOne Recognize multi-factor authentication includes device authentication, two options are available to recover devices and accounts.

* **Enrolling a new device:** Where the device is not registered through enrollment, PingOne Recognize facial biometrics are typically used in combination with another authentication factor to enroll the new device. Recommended options include a password, SMS one-time passwords (OTPs), or email magic links.

* **Managing multiple enrolled devices:** Customers can use the API to retrieve and delete devices that user identities are bound to.

* Supporting multiple enrolled devices can reduce the impact of losing a device and help simplify account recovery workflows.

Learn more in [Account Recovery](account_recovery.html).

## 4. Workforce

Using the previous three core components, PingOne Recognize also provides apps, integrations, and wrappers tailored for employee authentication:

* **PingOne Recognize Authenticator app:** Enrollment and authentication through app-based push notification.

* **WebSDK:** Enrollment and authentication through a web browser (OIDC and SAML wrappers are also available).