---
title: Adding strong authentication in JavaScript
description: Use the FIDO module to register and authenticate FIDO authenticators in JavaScript apps built with the DaVinci client
component: orchsdks
page_id: orchsdks:davinci:use-cases/fido/javascript/javascript-fido-davinci-flows
canonical_url: https://developer.pingidentity.com/orchsdks/davinci/use-cases/fido/javascript/javascript-fido-davinci-flows.html
llms_txt: https://developer.pingidentity.com/orchsdks/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: Thu, 13 Nov 2025 14:14:33 +0100
keywords: ["FIDO", "WebAuthn", "MFA", "Hardware", "Source Code", "Integration", "SDK", "JavaScript"]
section_ids:
  JavaScript_fido_module: Step 1. Installing modules
  step_2_initialize_the_fido_client: Step 2. Initialize the FIDO client
  step_3_registering_fido_authenticators: Step 3. Registering FIDO authenticators
  step_4_authenticating_using_a_fido_authenticator: Step 4. Authenticating using a FIDO authenticator
  fido-client-errors: Step 5. Handling FIDO client-side errors
---

# Adding strong authentication in JavaScript

[icon: circle-check, set=far]PingOne [icon: js, set=fab]JavaScript

The FIDO module offers a streamlined API for handling FIDO interactions.

It abstracts away the complexities of the underlying FIDO protocols, allowing you to quickly add strong authentication to your applications.

## Step 1. Installing modules

To add FIDO to your JavaScript apps you need this module:

* `fido`

The `fido` module for JavaScript is exported as a member of the `@forgerock/davinci-client` **npm** package.

To install the DaVinci client and member modules:

* Install the DaVinci client into your JavaScript apps using `npm`:

  Install the DaVinci client

  ```shell
  npm install @forgerock/davinci-client --save
  ```

## Step 2. Initialize the FIDO client

You need to import the **FIDO** module into your project, and initialize both the DaVinci client, and the FIDO API:

1. In your JavaScript app, import the DaVinci client, and `fido` module as named imports:

   Import the DaVinci client

   ```javascript
   import { davinci, fido } from '@forgerock/davinci-client';
   ```

2. Initialize the DaVinci client, and `fido` module:

   ```javascript
   const davinciClient = await davinci({ config });
   const fidoApi = fido();
   ```

   |   |                                                                                                                                                         |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | Learn more about initializing the DaVinci client in [Configuring the DaVinci module](../../../usage/javascript/02-configuring-the-davinci-module.html). |

## Step 3. Registering FIDO authenticators

To register a FIDO authenticator, use the `register()` function. The function returns a promise with `FidoRegistrationInputValue`, which contains the correctly-formatted public key credential, or a `GenericError`:

Registering a FIDO authenticator in a DaVinci flow

```javascript
if (collector.type === 'FidoRegistrationCollector') {
  const credentialOptions = collector.output.config.publicKeyCredentialCreationOptions;
  const publicKeyCredential = await fidoApi.register(credentialOptions);

  if ('error' in publicKeyCredential) {
    // Handle the error
  }

  // Update the FidoRegistrationCollector with the credential or error
  const updater = davinciClient.update(collector);
  updater(publicKeyCredential);
}

let nextStep = davinciClient.next();
```

## Step 4. Authenticating using a FIDO authenticator

To authenticate using a registered FIDO authenticator, use the `authenticate()` function. The function returns a promise containing either `FidoAuthenticationInputValue`, which contains the assertion you can return to DaVinci, or `GenericError`:

Authenticating with a FIDO authenticator in a DaVinci flow

```javascript
if (collector.type === 'FidoAuthenticationCollector') {
  const credentialOptions = collector.output.config.publicKeyCredentialRequestOptions;
  const assertion = await fidoApi.authenticate(credentialOptions);

  if ('error' in assertion) {
    // Handle the error
  }

  // Update the FidoAuthenticationCollector with the credential or error
  const updater = davinciClient.update(collector);
  updater(assertion);
}

let nextStep = davinciClient.next();
```

## Step 5. Handling FIDO client-side errors

If a call to `register()` or `authenticate()` fails, the returned promise resolves to a `GenericError` instead of a credential or assertion. That error object carries a `code` property, typed as `FidoErrorCode`, which normalizes the underlying WebAuthn `DOMException` into one of the following values:

* `NotAllowedError`

* `AbortError`

* `InvalidStateError`

* `NotSupportedError`

* `SecurityError`

* `TimeoutError`

* `UnknownError` - Returned when the underlying error doesn't match any of the recognized WebAuthn error names.

|   |                                                                                                                                                                                     |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The **FIDO** module does not automatically submit a client-side error back to DaVinci. Reporting the error, and deciding when to progress the flow afterwards, is left to your app. |

To report a client-side error, call `davinciClient.update(collector)` with the error object, the same way you would with a successful credential or assertion, and then call `next()` when you're ready to continue the flow:

Reporting a FIDO client-side error to DaVinci

```javascript
const publicKeyCredential = await fidoApi.register(credentialOptions);

if ('error' in publicKeyCredential) {
  console.error(publicKeyCredential.code, publicKeyCredential.message);

  const updater = davinciClient.update(collector);
  updater(publicKeyCredential); // Send the error's `code` and `message` back to the flow
}

// Call `next()` when you're ready to continue, for example after showing the user a message
let nextStep = davinciClient.next();
```

DaVinci flows can use the reported `code` to branch. For example, to offer a retry after a `TimeoutError`, or to fall back to another authentication method after a `NotAllowedError`.

---

---
title: Before you begin
description: Details the prerequisites for the DaVinci Android tutorial, covering compatibility with PingOne, DaVinci, and Android versions, as well as the necessary server-side configuration.
component: orchsdks
page_id: orchsdks:davinci:try-it-out/android/00_before-you-begin
canonical_url: https://developer.pingidentity.com/orchsdks/davinci/try-it-out/android/00_before-you-begin.html
llms_txt: https://developer.pingidentity.com/orchsdks/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: Fri, 17 Oct 2025 14:50:55 +0100
keywords: ["DaVinci", "Android", "Prerequisites", "Compatibility", "Server Configuration", "Tutorial"]
section_ids:
  compatibility: Compatibility
  prerequisites: Prerequisites
  server_configuration: Server configuration
---

# Before you begin

[icon: circle-check, set=far]PingOne [icon: android, set=fab]Android

* **Prepare**

* [Download](01_downloading-forgerocksdk.html)

* [Configure](02_configuring-sample-for-davinci.html)

* [Run](03_running-sample-pingone.html)

To successfully complete this tutorial refer to the prerequisites in this section.

The tutorial also requires a configured PingOne instance.

## Compatibility

* PingOne

  * Your PingOne instance must have DaVinci enabled.

- DaVinci flows

  Ensure your flows only use supported connectors, capabilities and fields for user interactions:

* HTTP Connector

  * **Custom HTML** capability

    > **Collapse: View supported fields**
    >
    > * [HTTP Connector field and collector support](#http-connector-fields-android-compatibility)
    >
    > * [HTTP Connector SK-Component support](#http-connector-sk-components-android-compatibility)
    >
    > **HTTP Connector field and collector support**
    >
    > | Field                                                                                             | Collector                      |                                |                               |                              |
    > | ------------------------------------------------------------------------------------------------- | ------------------------------ | ------------------------------ | ----------------------------- | ---------------------------- |
    > |                                                                                                   | Android                        | iOS                            | JavaScript                    | React Native                 |
    > | **Text field**Collects a single text string.                                                      | `TextCollector``1.0.0`         | `TextCollector``1.0.0`         | `TextCollector``1.0.0`        | TextCollector`1.1.0`         |
    > | **Password field**Collects a single text string that cannot be read from the screen.              | `PasswordCollector``1.0.0`     | `PasswordCollector``1.0.0`     | `PasswordCollector``1.0.0`    | PasswordCollector`1.1.0`     |
    > | **Submit Button**Sends the collected data to PingOne to continue the DaVinci flow.                | `SubmitCollector``1.0.0`       | `SubmitCollector``1.0.0`       | `SubmitCollector``1.0.0`      | SubmitCollector`1.1.0`       |
    > | **Flow Button**Triggers an alternative flow without sending the data collected so far to PingOne. | `FlowCollector``1.0.0`         | `FlowCollector``1.0.0`         | `FlowCollector``1.0.0`        | FlowCollector`1.1.0`         |
    > | **Label**Display a read-only text label.                                                          | `ReadOnlyTextCollector``1.1.0` | `LabelCollector``1.1.0`        | `ReadOnlyCollector``1.1.0`    | LabelCollector`1.1.0`        |
    > | **Radio** / **Dropdown**Collects a single value from a choice of multiple options.                | `SingleSelectCollector``1.1.0` | `SingleSelectCollector``1.1.0` | `SingleValueCollector``1.1.0` | SingleSelectCollector`1.1.0` |
    >
    > **HTTP Connector SK-Component support**
    >
    > | SK-Component                                                                                                                       | DaVinci module            |                           |                           |                         |
    > | ---------------------------------------------------------------------------------------------------------------------------------- | ------------------------- | ------------------------- | ------------------------- | ----------------------- |
    > |                                                                                                                                    | Android                   | iOS                       | JavaScript                | React Native            |
    > | **skIDP**Presents a button to allow users to authenticate using an external identity provider, such as Apple, Facebook, or Google. | `IdpCollector``1.1.0`     | `IdpCollector``1.1.0`     | `IdpCollector``1.1.0`     | IdpCollector`1.1.0`     |
    > | **skrisk**Instructs the client to gather behavioral data and return it to PingOne so that it can perform risk evaluations.         | `ProtectCollector``1.3.0` | `ProtectCollector``1.3.0` | `ProtectCollector``1.3.0` | ProtectCollector`1.1.0` |

    > **Collapse: View unsupported features**
    >
    > Verify that your flow does not depend on any *unsupported* elements:
    >
    > * SKPolling components
    >
    >   The [**SKPolling**](https://docs.pingidentity.com/davinci/flows/davinci_sk_components.html#skpolling) component cannot be processed by the DaVinci Client and should not be included in flows.
    >
    >   Features such as Magic Link authentication require the **SKPolling** component and therefore cannot be used with the DaVinci Client.
    >
    > * Images
    >
    >   Images embedded in a Custom HTML Template, such as background images or logos, cannot be passed to the Orchestration SDK as structured data.

* PingOne Form Connector

  * **Show Form** capability

    > **Collapse: View supported fields**
    >
    > * [Connector property support](#form-connector-properties-android-compatibility)
    >
    > * [Custom Fields support](#form-connector-fields-android-compatibility)
    >
    > * [Toolbox support](#form-connector-toolbox-android-compatibility)
    >
    > **Connector property support**
    >
    > | Property                                                                                                                                                                               | Collector                 |                           |                           |                         |
    > | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------- | ------------------------- | ------------------------- | ----------------------- |
    > |                                                                                                                                                                                        | Android                   | iOS                       | JavaScript                | React Native            |
    > | **Enable Device Profiling**Instructs PingOne Protect to collect device information.                                                                                                    | `ProtectCollector``2.0.0` | `ProtectCollector``2.0.0` | `ProtectCollector``2.0.0` | ProtectCollector`1.1.0` |
    > | **Include Behavioral Data**When enabled, PingOne Protect collects behavioral data to identify non-human activity.You must first select **Enable Device Profiling** to use this option. | `ProtectCollector``2.0.0` | `ProtectCollector``2.0.0` | `ProtectCollector``2.0.0` | ProtectCollector`1.1.0` |
    >
    > **Custom Fields support**
    >
    > | Field                                                                                                                                                                                                                                                                             | Collector                      |                                |                                                                                                                                                                                                                                    |                              |
    > | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------ | ------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------- |
    > |                                                                                                                                                                                                                                                                                   | Android                        | iOS                            | JavaScript                                                                                                                                                                                                                         | React Native                 |
    > | **Checkbox**Collects `true` or `false` from a checkbox or switch.                                                                                                                                                                                                                 | `BooleanCollector``2.1.0`      | `BooleanCollector``2.1.0`      | `BooleanCollector` / `ValidatedBooleanCollector`\[[1](#_footnotedef_1 "View footnote.")]`2.1.0`***[1](#_footnoteref_1). `ValidatedBooleanCollector` is returned for required checkboxes, and `BooleanCollector` for optional ones. | BooleanCollector`1.1.0`      |
    > | **Checkbox List**Collects the value of one or more checkboxes.                                                                                                                                                                                                                    | `MultiSelectCollector``1.1.0`  | `MultiSelectCollector``1.1.0`  | `MultiValueCollector``1.1.0`                                                                                                                                                                                                       | MultiSelectCollector`1.1.0`  |
    > | **Combobox**Collects a value from a dropdown containing one or more text strings.                                                                                                                                                                                                 | `MultiSelectCollector``1.1.0`  | `MultiSelectCollector``1.1.0`  | `MultiValueCollector``1.1.0`                                                                                                                                                                                                       | MultiSelectCollector`1.1.0`  |
    > | **Dropdown**Collects a value from a dropdown containing one or more text strings.                                                                                                                                                                                                 | `SingleSelectCollector``1.1.0` | `SingleSelectCollector``1.1.0` | `SingleValueCollector``1.1.0`                                                                                                                                                                                                      | SingleSelectCollector`1.1.0` |
    > | **Password**Collects a single text string that cannot be read from the screen, and optionally verifies the provided value against a policy.\[[2](#_footnotedef_2 "View footnote.")]***[2](#_footnoteref_2). Support for verification against password policies was added in 2.1.0 | `PasswordCollector``1.1.0`     | `PasswordCollector``1.1.0`     | `PasswordCollector``1.1.0`                                                                                                                                                                                                         | PasswordCollector`1.1.0`     |
    > | **New Password**Collects a new password and validates it against the environment's password policy. Optionally presents password requirements to the user.                                                                                                                        | ❌                              | ❌                              | `ValidatedPasswordCollector``2.1.0`                                                                                                                                                                                                | ❌                            |
    > | **Phone Number Input**Collects a phone number, with optional country code, and extension values.\[[3](#_footnotedef_3 "View footnote.")]***[3](#_footnoteref_3). Support for the extension value was added in 2.1.0                                                               | `PhoneNumberCollector``1.2.0`  | `PhoneNumberCollector``1.2.0`  | `PhoneNumberCollector` / `PhoneNumberExtensionCollector``1.2.0`                                                                                                                                                                    | PhoneNumberCollector`1.1.0`  |
    > | **Radio Button List**Collects a value from one or radio buttons.                                                                                                                                                                                                                  | `SingleSelectCollector``1.1.0` | `SingleSelectCollector``1.1.0` | `SingleValueCollector``1.1.0`                                                                                                                                                                                                      | SingleSelectCollector`1.1.0` |
    > | **Submit Button**Presents a button for form submission.                                                                                                                                                                                                                           | `SubmitCollector``1.1.0`       | `SubmitCollector``1.1.0`       | `SubmitCollector``1.1.0`                                                                                                                                                                                                           | SubmitCollector`1.1.0`       |
    > | **Text Input**Collects a single text string.                                                                                                                                                                                                                                      | `TextCollector``1.1.0`         | `TextCollector``1.1.0`         | `TextCollector``1.1.0`                                                                                                                                                                                                             | TextCollector`1.1.0`         |
    >
    > **Toolbox support**
    >
    > | Field                                                                                                                                                                                                                                   | Collector                                                          |                                                                    |                                                                    |                                                                |
    > | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | -------------------------------------------------------------- |
    > |                                                                                                                                                                                                                                         | Android                                                            | iOS                                                                | JavaScript                                                         | React Native                                                   |
    > | **Agreement**Presents text configured in PingOne under **User Experience** > **Agreements**, such as terms of service.                                                                                                                  | `ReadOnlyTextCollector``2.1.0`                                     | `ReadOnlyTextCollector``2.1.0`                                     | `ReadOnlyCollector``2.1.0`                                         | ReadOnlyTextCollector`1.1.0`                                   |
    > | **FIDO2**Allows users to perform multi-factor authentication with a FIDO2 device, or register a new device.                                                                                                                             | `FidoAuthenticationCollector` / `FidoRegistrationCollector``1.3.0` | `FidoAuthenticationCollector` / `FidoRegistrationCollector``1.3.0` | `FidoAuthenticationCollector` / `FidoRegistrationCollector``1.3.0` | FidoAuthenticationCollector / FidoRegistrationCollector`1.1.0` |
    > | **Image**Presents an image.                                                                                                                                                                                                             | `ImageCollector``2.2.0`                                            | `ImageCollector``2.2.0`                                            | `ImageCollector``2.1.0`                                            | ❌                                                              |
    > | **Flow Button**Presents a customized button.                                                                                                                                                                                            | `FlowCollector``1.1.0`                                             | `FlowCollector``1.1.0`                                             | `FlowCollector``1.1.0`                                             | FlowCollector`1.1.0`                                           |
    > | **Flow Link**Presents a customized link.                                                                                                                                                                                                | `FlowCollector``1.1.0`                                             | `FlowCollector``1.1.0`                                             | `FlowCollector``1.1.0`                                             | FlowCollector`1.1.0`                                           |
    > | **MFA Device Selection - Authentication**Presents a list of methods for performing multi-factor authentication (MFA).&#xA;&#xA;DaVinci client supports the FIDO2, Email, SMS, and Voice MFA types.                                      | `DeviceAuthenticationCollector``1.2.0`                             | `DeviceAuthenticationCollector``1.2.0`                             | `DeviceAuthenticationCollector``1.2.0`                             | DeviceAuthenticationCollector`1.1.0`                           |
    > | **MFA Device Selection - Registration**Presents a list of methods you can register for multi-factor authentication (MFA).&#xA;&#xA;DaVinci client supports the FIDO2, Email, SMS, and Voice MFA types.                                  | `DeviceRegistrationCollector``1.2.0`                               | `DeviceRegistrationCollector``1.2.0`                               | `DeviceRegistrationCollector``1.2.0`                               | DeviceRegistrationCollector`1.1.0`                             |
    > | **Polling**Presents an activity indicator which allows you to pause or loop the flow while the user completes an action.                                                                                                                | `PollingCollector``2.1.0`                                          | `PollingCollector``2.1.0`                                          | `PollingCollector``2.1.0`                                          | PollingCollector`1.1.0`                                        |
    > | **QR Code**Presents a QR code containing data, for example, a URL.                                                                                                                                                                      | `QRCodeCollector``2.1.0`                                           | `QRCodeCollector``2.1.0`                                           | `QrCodeCollector``2.1.0`                                           | QRCodeCollector`1.1.0`                                         |
    > | **Social Login**Presents a button to allow users to authenticate using an external identity provider, such as Apple, Facebook, or Google.                                                                                               | `IdpCollector``1.1.0`                                              | `IdpCollector``1.1.0`                                              | `IdpCollector``1.1.0`                                              | IdpCollector`1.1.0`                                            |
    > | **Translatable Rich Text**Presents rich text, including links, that you can translate into multiple languages.\[[4](#_footnotedef_4 "View footnote.")]***[4](#_footnoteref_4). Support for links in rich text fields was added in 2.1.0 | `LabelCollector``1.1.0`                                            | `LabelCollector``1.1.0`                                            | `RichTextCollector``1.1.0`                                         | LabelCollector`1.1.0`                                          |

* PingOne Protect Connector

  * **Create Risk Evaluation** capability

    > **Collapse: View supported fields**
    >
    > **PingOne Protect Connector support overview**
    >
    > | Capability                                                                                                                | Collector                 |                           |                           |                         |
    > | ------------------------------------------------------------------------------------------------------------------------- | ------------------------- | ------------------------- | ------------------------- | ----------------------- |
    > |                                                                                                                           | Android                   | iOS                       | JavaScript                | React Native            |
    > | **Create Risk Evaluation**Sends device and behavioral data collected by PingOne Protect to DaVinci for a risk evaluation. | `ProtectCollector``1.3.0` | `ProtectCollector``1.3.0` | `ProtectCollector``1.3.0` | ProtectCollector`1.1.0` |

* DaVinci SDK Integrator

  * **Exchange Custom Metadata with DaVinci SDK** capability

    > **Collapse: View supported fields**
    >
    > **DaVinci SDK Integrator support overview**
    >
    > | Capability                                                                                                                                                 | Collector                  |                            |                            |
    > | ---------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------- | -------------------------- | -------------------------- |
    > |                                                                                                                                                            | Android                    | iOS                        | JavaScript                 |
    > | **Exchange Custom Metadata**Exchanges custom JSON metadata and payloads between a DaVinci flow and the app, pausing flow execution until the app responds. | `MetadataCollector``2.2.0` | `MetadataCollector``2.2.0` | `MetadataCollector``2.2.0` |

- Android

  This sample requires at least Android API 23 (Android 6.0)

- Java

  This sample requires at least Java 8 (v1.8).

## Prerequisites

* Android Studio

  Download and install [Android Studio](https://developer.android.com/studio), which is available for many popular operating systems.

* An Android emulator or physical device

  To try the quick start application as you develop it, you need an Android device. To add a virtual, emulated Android device to Android Studio, refer to [Create and manage virtual devices](https://developer.android.com/studio/run/managing-avds), on the **Android Developers** website.

## Server configuration

You must configure your PingOne instance for use with the DaVinci module.

Ask your PingOne administrator to complete the following tasks:

* Configure a DaVinci flow

* Create a DaVinci application

* Configure PingOne for DaVinci flow invocation

To learn how to complete these steps, refer to [Launching a flow with a Ping SDK](https://docs.pingidentity.com/davinci/integrating_flows_into_applications/davinci_sdk_launching_a_flow_with_the_sdk.html) in the *PingOne DaVinci documentation*.

---

---
title: Before you begin
description: Details the prerequisites for the DaVinci iOS tutorial, covering compatibility with PingOne, DaVinci, and iOS versions, as well as the necessary server-side configuration.
component: orchsdks
page_id: orchsdks:davinci:try-it-out/ios/00_before-you-begin
canonical_url: https://developer.pingidentity.com/orchsdks/davinci/try-it-out/ios/00_before-you-begin.html
llms_txt: https://developer.pingidentity.com/orchsdks/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: Fri, 17 Oct 2025 14:50:55 +0100
keywords: ["DaVinci", "iOS", "Prerequisites", "Compatibility", "Server Configuration", "Tutorial"]
section_ids:
  compatibility: Compatibility
  prerequisites: Prerequisites
  server_configuration: Server configuration
---

# Before you begin

[icon: circle-check, set=far]PingOne [icon: apple, set=fab]iOS

* **Prepare**

* [Download](01_downloading-forgerocksdk.html)

* [Configure](02_configuring-sample-for-davinci.html)

* [Run](03_running-sample-pingone.html)

To successfully complete this tutorial refer to the prerequisites in this section.

The tutorial also requires a configured PingOne instance.

## Compatibility

* PingOne

  * Your PingOne instance must have DaVinci enabled.

- DaVinci flows

  Ensure your flows only use supported connectors, capabilities and fields for user interactions:

* HTTP Connector

  * **Custom HTML** capability

    > **Collapse: View supported fields**
    >
    > * [HTTP Connector field and collector support](#http-connector-fields-ios-compatibility)
    >
    > * [HTTP Connector SK-Component support](#http-connector-sk-components-ios-compatibility)
    >
    > **HTTP Connector field and collector support**
    >
    > | Field                                                                                             | Collector                      |                                |                               |                              |
    > | ------------------------------------------------------------------------------------------------- | ------------------------------ | ------------------------------ | ----------------------------- | ---------------------------- |
    > |                                                                                                   | Android                        | iOS                            | JavaScript                    | React Native                 |
    > | **Text field**Collects a single text string.                                                      | `TextCollector``1.0.0`         | `TextCollector``1.0.0`         | `TextCollector``1.0.0`        | TextCollector`1.1.0`         |
    > | **Password field**Collects a single text string that cannot be read from the screen.              | `PasswordCollector``1.0.0`     | `PasswordCollector``1.0.0`     | `PasswordCollector``1.0.0`    | PasswordCollector`1.1.0`     |
    > | **Submit Button**Sends the collected data to PingOne to continue the DaVinci flow.                | `SubmitCollector``1.0.0`       | `SubmitCollector``1.0.0`       | `SubmitCollector``1.0.0`      | SubmitCollector`1.1.0`       |
    > | **Flow Button**Triggers an alternative flow without sending the data collected so far to PingOne. | `FlowCollector``1.0.0`         | `FlowCollector``1.0.0`         | `FlowCollector``1.0.0`        | FlowCollector`1.1.0`         |
    > | **Label**Display a read-only text label.                                                          | `ReadOnlyTextCollector``1.1.0` | `LabelCollector``1.1.0`        | `ReadOnlyCollector``1.1.0`    | LabelCollector`1.1.0`        |
    > | **Radio** / **Dropdown**Collects a single value from a choice of multiple options.                | `SingleSelectCollector``1.1.0` | `SingleSelectCollector``1.1.0` | `SingleValueCollector``1.1.0` | SingleSelectCollector`1.1.0` |
    >
    > **HTTP Connector SK-Component support**
    >
    > | SK-Component                                                                                                                       | DaVinci module            |                           |                           |                         |
    > | ---------------------------------------------------------------------------------------------------------------------------------- | ------------------------- | ------------------------- | ------------------------- | ----------------------- |
    > |                                                                                                                                    | Android                   | iOS                       | JavaScript                | React Native            |
    > | **skIDP**Presents a button to allow users to authenticate using an external identity provider, such as Apple, Facebook, or Google. | `IdpCollector``1.1.0`     | `IdpCollector``1.1.0`     | `IdpCollector``1.1.0`     | IdpCollector`1.1.0`     |
    > | **skrisk**Instructs the client to gather behavioral data and return it to PingOne so that it can perform risk evaluations.         | `ProtectCollector``1.3.0` | `ProtectCollector``1.3.0` | `ProtectCollector``1.3.0` | ProtectCollector`1.1.0` |

    > **Collapse: View unsupported features**
    >
    > Verify that your flow does not depend on any *unsupported* elements:
    >
    > * SKPolling components
    >
    >   The [**SKPolling**](https://docs.pingidentity.com/davinci/flows/davinci_sk_components.html#skpolling) component cannot be processed by the DaVinci Client and should not be included in flows.
    >
    >   Features such as Magic Link authentication require the **SKPolling** component and therefore cannot be used with the DaVinci Client.
    >
    > * Images
    >
    >   Images embedded in a Custom HTML Template, such as background images or logos, cannot be passed to the Orchestration SDK as structured data.

* PingOne Form Connector

  * **Show Form** capability

    > **Collapse: View supported fields**
    >
    > * [Connector property support](#form-connector-properties-ios-compatibility)
    >
    > * [Custom Fields support](#form-connector-fields-ios-compatibility)
    >
    > * [Toolbox support](#form-connector-toolbox-ios-compatibility)
    >
    > **Connector property support**
    >
    > | Property                                                                                                                                                                               | Collector                 |                           |                           |                         |
    > | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------- | ------------------------- | ------------------------- | ----------------------- |
    > |                                                                                                                                                                                        | Android                   | iOS                       | JavaScript                | React Native            |
    > | **Enable Device Profiling**Instructs PingOne Protect to collect device information.                                                                                                    | `ProtectCollector``2.0.0` | `ProtectCollector``2.0.0` | `ProtectCollector``2.0.0` | ProtectCollector`1.1.0` |
    > | **Include Behavioral Data**When enabled, PingOne Protect collects behavioral data to identify non-human activity.You must first select **Enable Device Profiling** to use this option. | `ProtectCollector``2.0.0` | `ProtectCollector``2.0.0` | `ProtectCollector``2.0.0` | ProtectCollector`1.1.0` |
    >
    > **Custom Fields support**
    >
    > | Field                                                                                                                                                                                                                                                                             | Collector                      |                                |                                                                                                                                                                                                                                    |                              |
    > | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------ | ------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------- |
    > |                                                                                                                                                                                                                                                                                   | Android                        | iOS                            | JavaScript                                                                                                                                                                                                                         | React Native                 |
    > | **Checkbox**Collects `true` or `false` from a checkbox or switch.                                                                                                                                                                                                                 | `BooleanCollector``2.1.0`      | `BooleanCollector``2.1.0`      | `BooleanCollector` / `ValidatedBooleanCollector`\[[1](#_footnotedef_1 "View footnote.")]`2.1.0`***[1](#_footnoteref_1). `ValidatedBooleanCollector` is returned for required checkboxes, and `BooleanCollector` for optional ones. | BooleanCollector`1.1.0`      |
    > | **Checkbox List**Collects the value of one or more checkboxes.                                                                                                                                                                                                                    | `MultiSelectCollector``1.1.0`  | `MultiSelectCollector``1.1.0`  | `MultiValueCollector``1.1.0`                                                                                                                                                                                                       | MultiSelectCollector`1.1.0`  |
    > | **Combobox**Collects a value from a dropdown containing one or more text strings.                                                                                                                                                                                                 | `MultiSelectCollector``1.1.0`  | `MultiSelectCollector``1.1.0`  | `MultiValueCollector``1.1.0`                                                                                                                                                                                                       | MultiSelectCollector`1.1.0`  |
    > | **Dropdown**Collects a value from a dropdown containing one or more text strings.                                                                                                                                                                                                 | `SingleSelectCollector``1.1.0` | `SingleSelectCollector``1.1.0` | `SingleValueCollector``1.1.0`                                                                                                                                                                                                      | SingleSelectCollector`1.1.0` |
    > | **Password**Collects a single text string that cannot be read from the screen, and optionally verifies the provided value against a policy.\[[2](#_footnotedef_2 "View footnote.")]***[2](#_footnoteref_2). Support for verification against password policies was added in 2.1.0 | `PasswordCollector``1.1.0`     | `PasswordCollector``1.1.0`     | `PasswordCollector``1.1.0`                                                                                                                                                                                                         | PasswordCollector`1.1.0`     |
    > | **New Password**Collects a new password and validates it against the environment's password policy. Optionally presents password requirements to the user.                                                                                                                        | ❌                              | ❌                              | `ValidatedPasswordCollector``2.1.0`                                                                                                                                                                                                | ❌                            |
    > | **Phone Number Input**Collects a phone number, with optional country code, and extension values.\[[3](#_footnotedef_3 "View footnote.")]***[3](#_footnoteref_3). Support for the extension value was added in 2.1.0                                                               | `PhoneNumberCollector``1.2.0`  | `PhoneNumberCollector``1.2.0`  | `PhoneNumberCollector` / `PhoneNumberExtensionCollector``1.2.0`                                                                                                                                                                    | PhoneNumberCollector`1.1.0`  |
    > | **Radio Button List**Collects a value from one or radio buttons.                                                                                                                                                                                                                  | `SingleSelectCollector``1.1.0` | `SingleSelectCollector``1.1.0` | `SingleValueCollector``1.1.0`                                                                                                                                                                                                      | SingleSelectCollector`1.1.0` |
    > | **Submit Button**Presents a button for form submission.                                                                                                                                                                                                                           | `SubmitCollector``1.1.0`       | `SubmitCollector``1.1.0`       | `SubmitCollector``1.1.0`                                                                                                                                                                                                           | SubmitCollector`1.1.0`       |
    > | **Text Input**Collects a single text string.                                                                                                                                                                                                                                      | `TextCollector``1.1.0`         | `TextCollector``1.1.0`         | `TextCollector``1.1.0`                                                                                                                                                                                                             | TextCollector`1.1.0`         |
    >
    > **Toolbox support**
    >
    > | Field                                                                                                                                                                                                                                   | Collector                                                          |                                                                    |                                                                    |                                                                |
    > | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | -------------------------------------------------------------- |
    > |                                                                                                                                                                                                                                         | Android                                                            | iOS                                                                | JavaScript                                                         | React Native                                                   |
    > | **Agreement**Presents text configured in PingOne under **User Experience** > **Agreements**, such as terms of service.                                                                                                                  | `ReadOnlyTextCollector``2.1.0`                                     | `ReadOnlyTextCollector``2.1.0`                                     | `ReadOnlyCollector``2.1.0`                                         | ReadOnlyTextCollector`1.1.0`                                   |
    > | **FIDO2**Allows users to perform multi-factor authentication with a FIDO2 device, or register a new device.                                                                                                                             | `FidoAuthenticationCollector` / `FidoRegistrationCollector``1.3.0` | `FidoAuthenticationCollector` / `FidoRegistrationCollector``1.3.0` | `FidoAuthenticationCollector` / `FidoRegistrationCollector``1.3.0` | FidoAuthenticationCollector / FidoRegistrationCollector`1.1.0` |
    > | **Image**Presents an image.                                                                                                                                                                                                             | `ImageCollector``2.2.0`                                            | `ImageCollector``2.2.0`                                            | `ImageCollector``2.1.0`                                            | ❌                                                              |
    > | **Flow Button**Presents a customized button.                                                                                                                                                                                            | `FlowCollector``1.1.0`                                             | `FlowCollector``1.1.0`                                             | `FlowCollector``1.1.0`                                             | FlowCollector`1.1.0`                                           |
    > | **Flow Link**Presents a customized link.                                                                                                                                                                                                | `FlowCollector``1.1.0`                                             | `FlowCollector``1.1.0`                                             | `FlowCollector``1.1.0`                                             | FlowCollector`1.1.0`                                           |
    > | **MFA Device Selection - Authentication**Presents a list of methods for performing multi-factor authentication (MFA).&#xA;&#xA;DaVinci client supports the FIDO2, Email, SMS, and Voice MFA types.                                      | `DeviceAuthenticationCollector``1.2.0`                             | `DeviceAuthenticationCollector``1.2.0`                             | `DeviceAuthenticationCollector``1.2.0`                             | DeviceAuthenticationCollector`1.1.0`                           |
    > | **MFA Device Selection - Registration**Presents a list of methods you can register for multi-factor authentication (MFA).&#xA;&#xA;DaVinci client supports the FIDO2, Email, SMS, and Voice MFA types.                                  | `DeviceRegistrationCollector``1.2.0`                               | `DeviceRegistrationCollector``1.2.0`                               | `DeviceRegistrationCollector``1.2.0`                               | DeviceRegistrationCollector`1.1.0`                             |
    > | **Polling**Presents an activity indicator which allows you to pause or loop the flow while the user completes an action.                                                                                                                | `PollingCollector``2.1.0`                                          | `PollingCollector``2.1.0`                                          | `PollingCollector``2.1.0`                                          | PollingCollector`1.1.0`                                        |
    > | **QR Code**Presents a QR code containing data, for example, a URL.                                                                                                                                                                      | `QRCodeCollector``2.1.0`                                           | `QRCodeCollector``2.1.0`                                           | `QrCodeCollector``2.1.0`                                           | QRCodeCollector`1.1.0`                                         |
    > | **Social Login**Presents a button to allow users to authenticate using an external identity provider, such as Apple, Facebook, or Google.                                                                                               | `IdpCollector``1.1.0`                                              | `IdpCollector``1.1.0`                                              | `IdpCollector``1.1.0`                                              | IdpCollector`1.1.0`                                            |
    > | **Translatable Rich Text**Presents rich text, including links, that you can translate into multiple languages.\[[4](#_footnotedef_4 "View footnote.")]***[4](#_footnoteref_4). Support for links in rich text fields was added in 2.1.0 | `LabelCollector``1.1.0`                                            | `LabelCollector``1.1.0`                                            | `RichTextCollector``1.1.0`                                         | LabelCollector`1.1.0`                                          |

* PingOne Protect Connector

  * **Create Risk Evaluation** capability

    > **Collapse: View supported fields**
    >
    > **PingOne Protect Connector support overview**
    >
    > | Capability                                                                                                                | Collector                 |                           |                           |                         |
    > | ------------------------------------------------------------------------------------------------------------------------- | ------------------------- | ------------------------- | ------------------------- | ----------------------- |
    > |                                                                                                                           | Android                   | iOS                       | JavaScript                | React Native            |
    > | **Create Risk Evaluation**Sends device and behavioral data collected by PingOne Protect to DaVinci for a risk evaluation. | `ProtectCollector``1.3.0` | `ProtectCollector``1.3.0` | `ProtectCollector``1.3.0` | ProtectCollector`1.1.0` |

* DaVinci SDK Integrator

  * **Exchange Custom Metadata with DaVinci SDK** capability

    > **Collapse: View supported fields**
    >
    > **DaVinci SDK Integrator support overview**
    >
    > | Capability                                                                                                                                                 | Collector                  |                            |                            |
    > | ---------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------- | -------------------------- | -------------------------- |
    > |                                                                                                                                                            | Android                    | iOS                        | JavaScript                 |
    > | **Exchange Custom Metadata**Exchanges custom JSON metadata and payloads between a DaVinci flow and the app, pausing flow execution until the app responds. | `MetadataCollector``2.2.0` | `MetadataCollector``2.2.0` | `MetadataCollector``2.2.0` |

- iOS

  This sample app is compatible with iOS 12 and later.

## Prerequisites

* Xcode

  You can download the latest version for free from <https://developer.apple.com/xcode/>.

## Server configuration

You must configure your PingOne instance for use with the DaVinci module.

Ask your PingOne administrator to complete the following tasks:

* Configure a DaVinci flow

* Create a DaVinci application

* Configure PingOne for DaVinci flow invocation

To learn how to complete these steps, refer to [Launching a flow with a Ping SDK](https://docs.pingidentity.com/davinci/integrating_flows_into_applications/davinci_sdk_launching_a_flow_with_the_sdk.html) in the *PingOne DaVinci documentation*.

---

---
title: Before you begin
description: Details the prerequisites for the DaVinci JavaScript tutorial, covering compatibility with PingOne and DaVinci, Node.js requirements, and the necessary server-side OIDC application configuration.
component: orchsdks
page_id: orchsdks:davinci:try-it-out/javascript/00_before-you-begin
canonical_url: https://developer.pingidentity.com/orchsdks/davinci/try-it-out/javascript/00_before-you-begin.html
llms_txt: https://developer.pingidentity.com/orchsdks/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: Fri, 17 Oct 2025 14:50:55 +0100
keywords: ["DaVinci", "JavaScript", "Prerequisites", "Compatibility", "Server Configuration", "Tutorial"]
section_ids:
  compatibility: Compatibility
  prerequisites: Prerequisites
  server_configuration: Server configuration
---

# Before you begin

[icon: circle-check, set=far]PingOne [icon: js, set=fab]JavaScript

* **Prepare**

* [Download](01_downloading-forgerocksdk.html)

* [Install](02_configuring-forgerocksdk-core-project-js.html)

* [Configure](03_configuring-sample-forgerocksdk-js.html)

* [Run](04_running-sample-forgerocksdk-js.html)

To successfully complete this tutorial refer to the prerequisites in this section.

The tutorial also requires a configured server.

## Compatibility

* PingOne

  * Your PingOne instance must have DaVinci enabled.

- DaVinci flows

  Ensure your flows only use supported connectors, capabilities and fields for user interactions:

* HTTP Connector

  * **Custom HTML** capability

    > **Collapse: View supported fields**
    >
    > * [HTTP Connector field and collector support](#http-connector-fields-js-compatibility)
    >
    > * [HTTP Connector SK-Component support](#http-connector-sk-components-js-compatibility)
    >
    > **HTTP Connector field and collector support**
    >
    > | Field                                                                                             | Collector                      |                                |                               |                              |
    > | ------------------------------------------------------------------------------------------------- | ------------------------------ | ------------------------------ | ----------------------------- | ---------------------------- |
    > |                                                                                                   | Android                        | iOS                            | JavaScript                    | React Native                 |
    > | **Text field**Collects a single text string.                                                      | `TextCollector``1.0.0`         | `TextCollector``1.0.0`         | `TextCollector``1.0.0`        | TextCollector`1.1.0`         |
    > | **Password field**Collects a single text string that cannot be read from the screen.              | `PasswordCollector``1.0.0`     | `PasswordCollector``1.0.0`     | `PasswordCollector``1.0.0`    | PasswordCollector`1.1.0`     |
    > | **Submit Button**Sends the collected data to PingOne to continue the DaVinci flow.                | `SubmitCollector``1.0.0`       | `SubmitCollector``1.0.0`       | `SubmitCollector``1.0.0`      | SubmitCollector`1.1.0`       |
    > | **Flow Button**Triggers an alternative flow without sending the data collected so far to PingOne. | `FlowCollector``1.0.0`         | `FlowCollector``1.0.0`         | `FlowCollector``1.0.0`        | FlowCollector`1.1.0`         |
    > | **Label**Display a read-only text label.                                                          | `ReadOnlyTextCollector``1.1.0` | `LabelCollector``1.1.0`        | `ReadOnlyCollector``1.1.0`    | LabelCollector`1.1.0`        |
    > | **Radio** / **Dropdown**Collects a single value from a choice of multiple options.                | `SingleSelectCollector``1.1.0` | `SingleSelectCollector``1.1.0` | `SingleValueCollector``1.1.0` | SingleSelectCollector`1.1.0` |
    >
    > **HTTP Connector SK-Component support**
    >
    > | SK-Component                                                                                                                       | DaVinci module            |                           |                           |                         |
    > | ---------------------------------------------------------------------------------------------------------------------------------- | ------------------------- | ------------------------- | ------------------------- | ----------------------- |
    > |                                                                                                                                    | Android                   | iOS                       | JavaScript                | React Native            |
    > | **skIDP**Presents a button to allow users to authenticate using an external identity provider, such as Apple, Facebook, or Google. | `IdpCollector``1.1.0`     | `IdpCollector``1.1.0`     | `IdpCollector``1.1.0`     | IdpCollector`1.1.0`     |
    > | **skrisk**Instructs the client to gather behavioral data and return it to PingOne so that it can perform risk evaluations.         | `ProtectCollector``1.3.0` | `ProtectCollector``1.3.0` | `ProtectCollector``1.3.0` | ProtectCollector`1.1.0` |

    > **Collapse: View unsupported features**
    >
    > Verify that your flow does not depend on any *unsupported* elements:
    >
    > * SKPolling components
    >
    >   The [**SKPolling**](https://docs.pingidentity.com/davinci/flows/davinci_sk_components.html#skpolling) component cannot be processed by the DaVinci Client and should not be included in flows.
    >
    >   Features such as Magic Link authentication require the **SKPolling** component and therefore cannot be used with the DaVinci Client.
    >
    > * Images
    >
    >   Images embedded in a Custom HTML Template, such as background images or logos, cannot be passed to the Orchestration SDK as structured data.

* PingOne Form Connector

  * **Show Form** capability

    > **Collapse: View supported fields**
    >
    > * [Connector property support](#form-connector-properties-js-compatibility)
    >
    > * [Custom Fields support](#form-connector-fields-js-compatibility)
    >
    > * [Toolbox support](#form-connector-toolbox-js-compatibility)
    >
    > **Connector property support**
    >
    > | Property                                                                                                                                                                               | Collector                 |                           |                           |                         |
    > | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------- | ------------------------- | ------------------------- | ----------------------- |
    > |                                                                                                                                                                                        | Android                   | iOS                       | JavaScript                | React Native            |
    > | **Enable Device Profiling**Instructs PingOne Protect to collect device information.                                                                                                    | `ProtectCollector``2.0.0` | `ProtectCollector``2.0.0` | `ProtectCollector``2.0.0` | ProtectCollector`1.1.0` |
    > | **Include Behavioral Data**When enabled, PingOne Protect collects behavioral data to identify non-human activity.You must first select **Enable Device Profiling** to use this option. | `ProtectCollector``2.0.0` | `ProtectCollector``2.0.0` | `ProtectCollector``2.0.0` | ProtectCollector`1.1.0` |
    >
    > **Custom Fields support**
    >
    > | Field                                                                                                                                                                                                                                                                             | Collector                      |                                |                                                                                                                                                                                                                                    |                              |
    > | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------ | ------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------- |
    > |                                                                                                                                                                                                                                                                                   | Android                        | iOS                            | JavaScript                                                                                                                                                                                                                         | React Native                 |
    > | **Checkbox**Collects `true` or `false` from a checkbox or switch.                                                                                                                                                                                                                 | `BooleanCollector``2.1.0`      | `BooleanCollector``2.1.0`      | `BooleanCollector` / `ValidatedBooleanCollector`\[[1](#_footnotedef_1 "View footnote.")]`2.1.0`***[1](#_footnoteref_1). `ValidatedBooleanCollector` is returned for required checkboxes, and `BooleanCollector` for optional ones. | BooleanCollector`1.1.0`      |
    > | **Checkbox List**Collects the value of one or more checkboxes.                                                                                                                                                                                                                    | `MultiSelectCollector``1.1.0`  | `MultiSelectCollector``1.1.0`  | `MultiValueCollector``1.1.0`                                                                                                                                                                                                       | MultiSelectCollector`1.1.0`  |
    > | **Combobox**Collects a value from a dropdown containing one or more text strings.                                                                                                                                                                                                 | `MultiSelectCollector``1.1.0`  | `MultiSelectCollector``1.1.0`  | `MultiValueCollector``1.1.0`                                                                                                                                                                                                       | MultiSelectCollector`1.1.0`  |
    > | **Dropdown**Collects a value from a dropdown containing one or more text strings.                                                                                                                                                                                                 | `SingleSelectCollector``1.1.0` | `SingleSelectCollector``1.1.0` | `SingleValueCollector``1.1.0`                                                                                                                                                                                                      | SingleSelectCollector`1.1.0` |
    > | **Password**Collects a single text string that cannot be read from the screen, and optionally verifies the provided value against a policy.\[[2](#_footnotedef_2 "View footnote.")]***[2](#_footnoteref_2). Support for verification against password policies was added in 2.1.0 | `PasswordCollector``1.1.0`     | `PasswordCollector``1.1.0`     | `PasswordCollector``1.1.0`                                                                                                                                                                                                         | PasswordCollector`1.1.0`     |
    > | **New Password**Collects a new password and validates it against the environment's password policy. Optionally presents password requirements to the user.                                                                                                                        | ❌                              | ❌                              | `ValidatedPasswordCollector``2.1.0`                                                                                                                                                                                                | ❌                            |
    > | **Phone Number Input**Collects a phone number, with optional country code, and extension values.\[[3](#_footnotedef_3 "View footnote.")]***[3](#_footnoteref_3). Support for the extension value was added in 2.1.0                                                               | `PhoneNumberCollector``1.2.0`  | `PhoneNumberCollector``1.2.0`  | `PhoneNumberCollector` / `PhoneNumberExtensionCollector``1.2.0`                                                                                                                                                                    | PhoneNumberCollector`1.1.0`  |
    > | **Radio Button List**Collects a value from one or radio buttons.                                                                                                                                                                                                                  | `SingleSelectCollector``1.1.0` | `SingleSelectCollector``1.1.0` | `SingleValueCollector``1.1.0`                                                                                                                                                                                                      | SingleSelectCollector`1.1.0` |
    > | **Submit Button**Presents a button for form submission.                                                                                                                                                                                                                           | `SubmitCollector``1.1.0`       | `SubmitCollector``1.1.0`       | `SubmitCollector``1.1.0`                                                                                                                                                                                                           | SubmitCollector`1.1.0`       |
    > | **Text Input**Collects a single text string.                                                                                                                                                                                                                                      | `TextCollector``1.1.0`         | `TextCollector``1.1.0`         | `TextCollector``1.1.0`                                                                                                                                                                                                             | TextCollector`1.1.0`         |
    >
    > **Toolbox support**
    >
    > | Field                                                                                                                                                                                                                                   | Collector                                                          |                                                                    |                                                                    |                                                                |
    > | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | -------------------------------------------------------------- |
    > |                                                                                                                                                                                                                                         | Android                                                            | iOS                                                                | JavaScript                                                         | React Native                                                   |
    > | **Agreement**Presents text configured in PingOne under **User Experience** > **Agreements**, such as terms of service.                                                                                                                  | `ReadOnlyTextCollector``2.1.0`                                     | `ReadOnlyTextCollector``2.1.0`                                     | `ReadOnlyCollector``2.1.0`                                         | ReadOnlyTextCollector`1.1.0`                                   |
    > | **FIDO2**Allows users to perform multi-factor authentication with a FIDO2 device, or register a new device.                                                                                                                             | `FidoAuthenticationCollector` / `FidoRegistrationCollector``1.3.0` | `FidoAuthenticationCollector` / `FidoRegistrationCollector``1.3.0` | `FidoAuthenticationCollector` / `FidoRegistrationCollector``1.3.0` | FidoAuthenticationCollector / FidoRegistrationCollector`1.1.0` |
    > | **Image**Presents an image.                                                                                                                                                                                                             | `ImageCollector``2.2.0`                                            | `ImageCollector``2.2.0`                                            | `ImageCollector``2.1.0`                                            | ❌                                                              |
    > | **Flow Button**Presents a customized button.                                                                                                                                                                                            | `FlowCollector``1.1.0`                                             | `FlowCollector``1.1.0`                                             | `FlowCollector``1.1.0`                                             | FlowCollector`1.1.0`                                           |
    > | **Flow Link**Presents a customized link.                                                                                                                                                                                                | `FlowCollector``1.1.0`                                             | `FlowCollector``1.1.0`                                             | `FlowCollector``1.1.0`                                             | FlowCollector`1.1.0`                                           |
    > | **MFA Device Selection - Authentication**Presents a list of methods for performing multi-factor authentication (MFA).&#xA;&#xA;DaVinci client supports the FIDO2, Email, SMS, and Voice MFA types.                                      | `DeviceAuthenticationCollector``1.2.0`                             | `DeviceAuthenticationCollector``1.2.0`                             | `DeviceAuthenticationCollector``1.2.0`                             | DeviceAuthenticationCollector`1.1.0`                           |
    > | **MFA Device Selection - Registration**Presents a list of methods you can register for multi-factor authentication (MFA).&#xA;&#xA;DaVinci client supports the FIDO2, Email, SMS, and Voice MFA types.                                  | `DeviceRegistrationCollector``1.2.0`                               | `DeviceRegistrationCollector``1.2.0`                               | `DeviceRegistrationCollector``1.2.0`                               | DeviceRegistrationCollector`1.1.0`                             |
    > | **Polling**Presents an activity indicator which allows you to pause or loop the flow while the user completes an action.                                                                                                                | `PollingCollector``2.1.0`                                          | `PollingCollector``2.1.0`                                          | `PollingCollector``2.1.0`                                          | PollingCollector`1.1.0`                                        |
    > | **QR Code**Presents a QR code containing data, for example, a URL.                                                                                                                                                                      | `QRCodeCollector``2.1.0`                                           | `QRCodeCollector``2.1.0`                                           | `QrCodeCollector``2.1.0`                                           | QRCodeCollector`1.1.0`                                         |
    > | **Social Login**Presents a button to allow users to authenticate using an external identity provider, such as Apple, Facebook, or Google.                                                                                               | `IdpCollector``1.1.0`                                              | `IdpCollector``1.1.0`                                              | `IdpCollector``1.1.0`                                              | IdpCollector`1.1.0`                                            |
    > | **Translatable Rich Text**Presents rich text, including links, that you can translate into multiple languages.\[[4](#_footnotedef_4 "View footnote.")]***[4](#_footnoteref_4). Support for links in rich text fields was added in 2.1.0 | `LabelCollector``1.1.0`                                            | `LabelCollector``1.1.0`                                            | `RichTextCollector``1.1.0`                                         | LabelCollector`1.1.0`                                          |

* PingOne Protect Connector

  * **Create Risk Evaluation** capability

    > **Collapse: View supported fields**
    >
    > **PingOne Protect Connector support overview**
    >
    > | Capability                                                                                                                | Collector                 |                           |                           |                         |
    > | ------------------------------------------------------------------------------------------------------------------------- | ------------------------- | ------------------------- | ------------------------- | ----------------------- |
    > |                                                                                                                           | Android                   | iOS                       | JavaScript                | React Native            |
    > | **Create Risk Evaluation**Sends device and behavioral data collected by PingOne Protect to DaVinci for a risk evaluation. | `ProtectCollector``1.3.0` | `ProtectCollector``1.3.0` | `ProtectCollector``1.3.0` | ProtectCollector`1.1.0` |

* DaVinci SDK Integrator

  * **Exchange Custom Metadata with DaVinci SDK** capability

    > **Collapse: View supported fields**
    >
    > **DaVinci SDK Integrator support overview**
    >
    > | Capability                                                                                                                                                 | Collector                  |                            |                            |
    > | ---------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------- | -------------------------- | -------------------------- |
    > |                                                                                                                                                            | Android                    | iOS                        | JavaScript                 |
    > | **Exchange Custom Metadata**Exchanges custom JSON metadata and payloads between a DaVinci flow and the app, pausing flow execution until the app responds. | `MetadataCollector``2.2.0` | `MetadataCollector``2.2.0` | `MetadataCollector``2.2.0` |

## Prerequisites

* Node and NPM

  The SDK requires a minimum Node.js version of `18`, and is tested on versions `18` and `20`. To get a supported version of Node.js, refer to the [Node.js download page](https://nodejs.org/en/download/).

  You will also need `npm` to build the code and run the samples.

## Server configuration

You must configure your PingOne instance for use with the DaVinci module.

Ask your PingOne administrator to complete the following tasks:

* Configure a DaVinci flow

* Create a DaVinci application

* Configure PingOne for DaVinci flow invocation

To learn how to complete these steps, refer to [Launching a flow with a Ping SDK](https://docs.pingidentity.com/davinci/integrating_flows_into_applications/davinci_sdk_launching_a_flow_with_the_sdk.html) in the *PingOne DaVinci documentation*.

The values you'll need when configuring the OIDC application in PingOne for this tutorial are as follows:

**Property values for OIDC application in PingOne**

| Property                               | Value required for tutorial                     |
| -------------------------------------- | ----------------------------------------------- |
| **Token Auth Method**                  | `None`                                          |
| **Response Type**                      | `Code`                                          |
| **Grant Type**                         | `Authorization Code`                            |
| **Redirect URIs**                      | `http://localhost:8443/callback.html`           |
| **Signoff URLs**                       | `http://localhost:8443`                         |
| **Terminate User Session by ID Token** | `Enabled`                                       |
| **Allowed Origins**                    | `http://localhost:8443` `http://localhost:9443` |

---

---
title: Before you begin
description: Prerequisites, compatibility requirements, and PingOne DaVinci configuration steps needed before starting the React Native tutorial.
component: orchsdks
page_id: orchsdks:davinci:try-it-out/react-native/00_before-you-begin
canonical_url: https://developer.pingidentity.com/orchsdks/davinci/try-it-out/react-native/00_before-you-begin.html
llms_txt: https://developer.pingidentity.com/orchsdks/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["PingOne", "DaVinci", "Setup &amp; Configuration", "Source Code", "Tutorial", "SDK", "React Native"]
section_ids:
  compatibility: Compatibility
  prerequisites: Prerequisites
  server_configuration: Server configuration
---

# Before you begin

[icon: circle-check, set=far]PingOne [icon: react, set=fab]React Native

* **Prepare**

* [Download](01_download_samples.html)

* [Install](02_prepare-projects.html)

* [Configure](03_configure_sample.html)

* [Run](04_run_the_sample.html)

To successfully complete this tutorial, refer to the prerequisites and compatibility requirements in this section.

The tutorial also requires a configured PingOne instance.

## Compatibility

* React Native

  This sample app requires React Native 0.80.1 or later.

* iOS

  This sample app requires iOS 16.0 or later.

* Android

  This sample app requires Android 10 (API level 29) or later.

* PingOne

  * Your PingOne instance must have DaVinci enabled.

- DaVinci flows

  Ensure your flows only use supported connectors, capabilities and fields for user interactions:

* HTTP Connector

  * **Custom HTML** capability

    > **Collapse: View supported fields**
    >
    > * [HTTP Connector field and collector support](#http-connector-fields-react-native-compatibility)
    >
    > * [HTTP Connector SK-Component support](#http-connector-sk-components-react-native-compatibility)
    >
    > **HTTP Connector field and collector support**
    >
    > | Field                                                                                             | Collector                      |                                |                               |                              |
    > | ------------------------------------------------------------------------------------------------- | ------------------------------ | ------------------------------ | ----------------------------- | ---------------------------- |
    > |                                                                                                   | Android                        | iOS                            | JavaScript                    | React Native                 |
    > | **Text field**Collects a single text string.                                                      | `TextCollector``1.0.0`         | `TextCollector``1.0.0`         | `TextCollector``1.0.0`        | TextCollector`1.1.0`         |
    > | **Password field**Collects a single text string that cannot be read from the screen.              | `PasswordCollector``1.0.0`     | `PasswordCollector``1.0.0`     | `PasswordCollector``1.0.0`    | PasswordCollector`1.1.0`     |
    > | **Submit Button**Sends the collected data to PingOne to continue the DaVinci flow.                | `SubmitCollector``1.0.0`       | `SubmitCollector``1.0.0`       | `SubmitCollector``1.0.0`      | SubmitCollector`1.1.0`       |
    > | **Flow Button**Triggers an alternative flow without sending the data collected so far to PingOne. | `FlowCollector``1.0.0`         | `FlowCollector``1.0.0`         | `FlowCollector``1.0.0`        | FlowCollector`1.1.0`         |
    > | **Label**Display a read-only text label.                                                          | `ReadOnlyTextCollector``1.1.0` | `LabelCollector``1.1.0`        | `ReadOnlyCollector``1.1.0`    | LabelCollector`1.1.0`        |
    > | **Radio** / **Dropdown**Collects a single value from a choice of multiple options.                | `SingleSelectCollector``1.1.0` | `SingleSelectCollector``1.1.0` | `SingleValueCollector``1.1.0` | SingleSelectCollector`1.1.0` |
    >
    > **HTTP Connector SK-Component support**
    >
    > | SK-Component                                                                                                                       | DaVinci module            |                           |                           |                         |
    > | ---------------------------------------------------------------------------------------------------------------------------------- | ------------------------- | ------------------------- | ------------------------- | ----------------------- |
    > |                                                                                                                                    | Android                   | iOS                       | JavaScript                | React Native            |
    > | **skIDP**Presents a button to allow users to authenticate using an external identity provider, such as Apple, Facebook, or Google. | `IdpCollector``1.1.0`     | `IdpCollector``1.1.0`     | `IdpCollector``1.1.0`     | IdpCollector`1.1.0`     |
    > | **skrisk**Instructs the client to gather behavioral data and return it to PingOne so that it can perform risk evaluations.         | `ProtectCollector``1.3.0` | `ProtectCollector``1.3.0` | `ProtectCollector``1.3.0` | ProtectCollector`1.1.0` |

    > **Collapse: View unsupported features**
    >
    > Verify that your flow does not depend on any *unsupported* elements:
    >
    > * SKPolling components
    >
    >   The [**SKPolling**](https://docs.pingidentity.com/davinci/flows/davinci_sk_components.html#skpolling) component cannot be processed by the DaVinci Client and should not be included in flows.
    >
    >   Features such as Magic Link authentication require the **SKPolling** component and therefore cannot be used with the DaVinci Client.
    >
    > * Images
    >
    >   Images embedded in a Custom HTML Template, such as background images or logos, cannot be passed to the Orchestration SDK as structured data.

* PingOne Form Connector

  * **Show Form** capability

    > **Collapse: View supported fields**
    >
    > * [Connector property support](#form-connector-properties-react-native-compatibility)
    >
    > * [Custom Fields support](#form-connector-fields-react-native-compatibility)
    >
    > * [Toolbox support](#form-connector-toolbox-react-native-compatibility)
    >
    > **Connector property support**
    >
    > | Property                                                                                                                                                                               | Collector                 |                           |                           |                         |
    > | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------- | ------------------------- | ------------------------- | ----------------------- |
    > |                                                                                                                                                                                        | Android                   | iOS                       | JavaScript                | React Native            |
    > | **Enable Device Profiling**Instructs PingOne Protect to collect device information.                                                                                                    | `ProtectCollector``2.0.0` | `ProtectCollector``2.0.0` | `ProtectCollector``2.0.0` | ProtectCollector`1.1.0` |
    > | **Include Behavioral Data**When enabled, PingOne Protect collects behavioral data to identify non-human activity.You must first select **Enable Device Profiling** to use this option. | `ProtectCollector``2.0.0` | `ProtectCollector``2.0.0` | `ProtectCollector``2.0.0` | ProtectCollector`1.1.0` |
    >
    > **Custom Fields support**
    >
    > | Field                                                                                                                                                                                                                                                                             | Collector                      |                                |                                                                                                                                                                                                                                    |                              |
    > | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------ | ------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------- |
    > |                                                                                                                                                                                                                                                                                   | Android                        | iOS                            | JavaScript                                                                                                                                                                                                                         | React Native                 |
    > | **Checkbox**Collects `true` or `false` from a checkbox or switch.                                                                                                                                                                                                                 | `BooleanCollector``2.1.0`      | `BooleanCollector``2.1.0`      | `BooleanCollector` / `ValidatedBooleanCollector`\[[1](#_footnotedef_1 "View footnote.")]`2.1.0`***[1](#_footnoteref_1). `ValidatedBooleanCollector` is returned for required checkboxes, and `BooleanCollector` for optional ones. | BooleanCollector`1.1.0`      |
    > | **Checkbox List**Collects the value of one or more checkboxes.                                                                                                                                                                                                                    | `MultiSelectCollector``1.1.0`  | `MultiSelectCollector``1.1.0`  | `MultiValueCollector``1.1.0`                                                                                                                                                                                                       | MultiSelectCollector`1.1.0`  |
    > | **Combobox**Collects a value from a dropdown containing one or more text strings.                                                                                                                                                                                                 | `MultiSelectCollector``1.1.0`  | `MultiSelectCollector``1.1.0`  | `MultiValueCollector``1.1.0`                                                                                                                                                                                                       | MultiSelectCollector`1.1.0`  |
    > | **Dropdown**Collects a value from a dropdown containing one or more text strings.                                                                                                                                                                                                 | `SingleSelectCollector``1.1.0` | `SingleSelectCollector``1.1.0` | `SingleValueCollector``1.1.0`                                                                                                                                                                                                      | SingleSelectCollector`1.1.0` |
    > | **Password**Collects a single text string that cannot be read from the screen, and optionally verifies the provided value against a policy.\[[2](#_footnotedef_2 "View footnote.")]***[2](#_footnoteref_2). Support for verification against password policies was added in 2.1.0 | `PasswordCollector``1.1.0`     | `PasswordCollector``1.1.0`     | `PasswordCollector``1.1.0`                                                                                                                                                                                                         | PasswordCollector`1.1.0`     |
    > | **New Password**Collects a new password and validates it against the environment's password policy. Optionally presents password requirements to the user.                                                                                                                        | ❌                              | ❌                              | `ValidatedPasswordCollector``2.1.0`                                                                                                                                                                                                | ❌                            |
    > | **Phone Number Input**Collects a phone number, with optional country code, and extension values.\[[3](#_footnotedef_3 "View footnote.")]***[3](#_footnoteref_3). Support for the extension value was added in 2.1.0                                                               | `PhoneNumberCollector``1.2.0`  | `PhoneNumberCollector``1.2.0`  | `PhoneNumberCollector` / `PhoneNumberExtensionCollector``1.2.0`                                                                                                                                                                    | PhoneNumberCollector`1.1.0`  |
    > | **Radio Button List**Collects a value from one or radio buttons.                                                                                                                                                                                                                  | `SingleSelectCollector``1.1.0` | `SingleSelectCollector``1.1.0` | `SingleValueCollector``1.1.0`                                                                                                                                                                                                      | SingleSelectCollector`1.1.0` |
    > | **Submit Button**Presents a button for form submission.                                                                                                                                                                                                                           | `SubmitCollector``1.1.0`       | `SubmitCollector``1.1.0`       | `SubmitCollector``1.1.0`                                                                                                                                                                                                           | SubmitCollector`1.1.0`       |
    > | **Text Input**Collects a single text string.                                                                                                                                                                                                                                      | `TextCollector``1.1.0`         | `TextCollector``1.1.0`         | `TextCollector``1.1.0`                                                                                                                                                                                                             | TextCollector`1.1.0`         |
    >
    > **Toolbox support**
    >
    > | Field                                                                                                                                                                                                                                   | Collector                                                          |                                                                    |                                                                    |                                                                |
    > | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | -------------------------------------------------------------- |
    > |                                                                                                                                                                                                                                         | Android                                                            | iOS                                                                | JavaScript                                                         | React Native                                                   |
    > | **Agreement**Presents text configured in PingOne under **User Experience** > **Agreements**, such as terms of service.                                                                                                                  | `ReadOnlyTextCollector``2.1.0`                                     | `ReadOnlyTextCollector``2.1.0`                                     | `ReadOnlyCollector``2.1.0`                                         | ReadOnlyTextCollector`1.1.0`                                   |
    > | **FIDO2**Allows users to perform multi-factor authentication with a FIDO2 device, or register a new device.                                                                                                                             | `FidoAuthenticationCollector` / `FidoRegistrationCollector``1.3.0` | `FidoAuthenticationCollector` / `FidoRegistrationCollector``1.3.0` | `FidoAuthenticationCollector` / `FidoRegistrationCollector``1.3.0` | FidoAuthenticationCollector / FidoRegistrationCollector`1.1.0` |
    > | **Image**Presents an image.                                                                                                                                                                                                             | `ImageCollector``2.2.0`                                            | `ImageCollector``2.2.0`                                            | `ImageCollector``2.1.0`                                            | ❌                                                              |
    > | **Flow Button**Presents a customized button.                                                                                                                                                                                            | `FlowCollector``1.1.0`                                             | `FlowCollector``1.1.0`                                             | `FlowCollector``1.1.0`                                             | FlowCollector`1.1.0`                                           |
    > | **Flow Link**Presents a customized link.                                                                                                                                                                                                | `FlowCollector``1.1.0`                                             | `FlowCollector``1.1.0`                                             | `FlowCollector``1.1.0`                                             | FlowCollector`1.1.0`                                           |
    > | **MFA Device Selection - Authentication**Presents a list of methods for performing multi-factor authentication (MFA).&#xA;&#xA;DaVinci client supports the FIDO2, Email, SMS, and Voice MFA types.                                      | `DeviceAuthenticationCollector``1.2.0`                             | `DeviceAuthenticationCollector``1.2.0`                             | `DeviceAuthenticationCollector``1.2.0`                             | DeviceAuthenticationCollector`1.1.0`                           |
    > | **MFA Device Selection - Registration**Presents a list of methods you can register for multi-factor authentication (MFA).&#xA;&#xA;DaVinci client supports the FIDO2, Email, SMS, and Voice MFA types.                                  | `DeviceRegistrationCollector``1.2.0`                               | `DeviceRegistrationCollector``1.2.0`                               | `DeviceRegistrationCollector``1.2.0`                               | DeviceRegistrationCollector`1.1.0`                             |
    > | **Polling**Presents an activity indicator which allows you to pause or loop the flow while the user completes an action.                                                                                                                | `PollingCollector``2.1.0`                                          | `PollingCollector``2.1.0`                                          | `PollingCollector``2.1.0`                                          | PollingCollector`1.1.0`                                        |
    > | **QR Code**Presents a QR code containing data, for example, a URL.                                                                                                                                                                      | `QRCodeCollector``2.1.0`                                           | `QRCodeCollector``2.1.0`                                           | `QrCodeCollector``2.1.0`                                           | QRCodeCollector`1.1.0`                                         |
    > | **Social Login**Presents a button to allow users to authenticate using an external identity provider, such as Apple, Facebook, or Google.                                                                                               | `IdpCollector``1.1.0`                                              | `IdpCollector``1.1.0`                                              | `IdpCollector``1.1.0`                                              | IdpCollector`1.1.0`                                            |
    > | **Translatable Rich Text**Presents rich text, including links, that you can translate into multiple languages.\[[4](#_footnotedef_4 "View footnote.")]***[4](#_footnoteref_4). Support for links in rich text fields was added in 2.1.0 | `LabelCollector``1.1.0`                                            | `LabelCollector``1.1.0`                                            | `RichTextCollector``1.1.0`                                         | LabelCollector`1.1.0`                                          |

* PingOne Protect Connector

  * **Create Risk Evaluation** capability

    > **Collapse: View supported fields**
    >
    > **PingOne Protect Connector support overview**
    >
    > | Capability                                                                                                                | Collector                 |                           |                           |                         |
    > | ------------------------------------------------------------------------------------------------------------------------- | ------------------------- | ------------------------- | ------------------------- | ----------------------- |
    > |                                                                                                                           | Android                   | iOS                       | JavaScript                | React Native            |
    > | **Create Risk Evaluation**Sends device and behavioral data collected by PingOne Protect to DaVinci for a risk evaluation. | `ProtectCollector``1.3.0` | `ProtectCollector``1.3.0` | `ProtectCollector``1.3.0` | ProtectCollector`1.1.0` |

* DaVinci SDK Integrator

  * **Exchange Custom Metadata with DaVinci SDK** capability

    > **Collapse: View supported fields**
    >
    > **DaVinci SDK Integrator support overview**
    >
    > | Capability                                                                                                                                                 | Collector                  |                            |                            |
    > | ---------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------- | -------------------------- | -------------------------- |
    > |                                                                                                                                                            | Android                    | iOS                        | JavaScript                 |
    > | **Exchange Custom Metadata**Exchanges custom JSON metadata and payloads between a DaVinci flow and the app, pausing flow execution until the app responds. | `MetadataCollector``2.2.0` | `MetadataCollector``2.2.0` | `MetadataCollector``2.2.0` |

## Prerequisites

The React Native development environment must be fully configured before you begin.

Follow the official [React Native environment setup guide](https://reactnative.dev/docs/set-up-your-environment) and ensure the following tools are installed:

* Node.js and Yarn

  Install [Node.js](https://nodejs.org/) version 20 or later.

  This project uses Yarn. Install Yarn by running:

  ```shell
  corepack enable
  ```

* Xcode (iOS only)

  Download and install [Xcode](https://developer.apple.com/xcode/) from the Mac App Store.

  Xcode 16 or later is recommended.

* Ruby and Bundler (iOS only)

  Ruby 3.3.6 or later is required to manage CocoaPods.

  Install [Bundler](https://bundler.io/) with:

  ```shell
  gem install bundler
  ```

* CocoaPods (iOS only)

  CocoaPods is installed locally during the tutorial.

* Android Studio (Android only)

  Download and install [Android Studio](https://developer.android.com/studio).

  An Android emulator or physical device is required to run the app.

* Java (Android only)

  JDK 21 is required by the current Ping Android SDK dependencies used by the sample app.

  Check that you are correctly setting the `JAVA_HOME` environment variable.

  For example, a `~/.zshrc` file might contain the following:

  ```shell
  export JAVA_HOME=$(/usr/libexec/java_home -v21)
  export PATH="$JAVA_HOME/bin:$PATH"
  ```

* `keytool` (Android only)

  `keytool` is part of the Java Development Kit and is used to generate the debug signing keystore required for the Android build.

## Server configuration

You must configure your PingOne instance for use with the DaVinci module.

Ask your PingOne administrator to complete the following tasks:

* Configure a DaVinci flow

* Create a DaVinci application

* Configure PingOne for DaVinci flow invocation

To learn how to complete these steps, refer to [Launching a flow with a Ping SDK](https://docs.pingidentity.com/davinci/integrating_flows_into_applications/davinci_sdk_launching_a_flow_with_the_sdk.html) in the *PingOne DaVinci documentation*.

The OAuth 2.0 client must allow the redirect URI used by the sample app. You will enter the client ID, discovery endpoint, redirect URI, scopes, and, optionally, the DaVinci flow policy in the sample app's `.env` file.

---

---
title: Before you begin
description: Explains the necessary server-side configuration for implementing one-time passcode (OTP) authentication, including setting up MFA policies in PingOne and configuring DaVinci flows.
component: orchsdks
page_id: orchsdks:davinci:use-cases/otp/00_before-you-begin
canonical_url: https://developer.pingidentity.com/orchsdks/davinci/use-cases/otp/00_before-you-begin.html
llms_txt: https://developer.pingidentity.com/orchsdks/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: Fri, 9 Jan 2026 17:23:51 +0000
keywords: ["DaVinci", "OTP", "MFA", "Server Configuration", "PingOne", "Flows"]
section_ids:
  compatibility: Compatibility
  configuring_strong_authentication_mfa_methods_in_pingone: Configuring strong authentication (MFA) methods in PingOne
  configuring_an_mfa_policy_to_use_one_time_passcodes: Configuring an MFA policy to use one-time passcodes
  configuring_davinci_flows_for_one_time_passcodes: Configuring DaVinci Flows for one-time passcodes
  otp-in-dv-flow-forms: Configuring DaVinci Forms for one-time passcodes
  creating_a_davinci_form: Creating a DaVinci Form
  adding_a_form_to_a_davinci_flow: Adding a form to a DaVinci flow
  launch-davinci-sdks: Configuring a DaVinci flow to be launched by the Orchestration SDKs
  next_steps: Next Steps
  related_links: Related links
---

# Before you begin

[icon: circle-check, set=far]PingOne [icon: android, set=fab]Android [icon: apple, set=fab]iOS [icon: js, set=fab]JavaScript

To complete this tutorial, refer to the prerequisites in this section.

The tutorial also requires a configured server.

## Compatibility

* PingOne

  * Your PingOne instance must have DaVinci enabled.

* DaVinci

  * Your DaVinci flow uses the [PingOne MFA Connector](https://docs.pingidentity.com/connectors/p1_mfa_connector.html).

  * You have an MFA policy in PingOne configured to only use the following one-time passcode methods:

    * Email

    * SMS

    * Voice

## Configuring strong authentication (MFA) methods in PingOne

In this section, you configure PingOne to be able to authenticate users with one-time password methods supported by the Orchestration SDKs.

Select one or more of the OTP delivery methods below for instructions on configuring them in PingOne:

[icon: envelope, set=far, size=3x]

#### [Email](https://docs.pingidentity.com/pingone/strong_authentication_mfa/p1_strong_auth_email.html)

Configuring email authentication

[icon: mobile-signal, set=far, size=3x]

#### [SMS or Voice](https://docs.pingidentity.com/pingone/strong_authentication_mfa/p1_strong_auth_sms_voice_authentication.html)

Configuring SMS and voice authentication

## Configuring an MFA policy to use one-time passcodes

After configuring the OTP delivery methods you must create an MFA policy in PingOne. An MFA policy configures the relevant settings for the authentication methods that you want to enable.

Learn more in [Configuring an MFA policy for strong authentication](https://docs.pingidentity.com/pingone/strong_authentication_mfa/p1_creating_an_mfa_policy_for_strong_auth.html).

## Configuring DaVinci Flows for one-time passcodes

After configuring OTP delivery methods and creating an MFA policy, the next step is to configure a DaVinci flow to display buttons in your app so that users can choose which OTP delivery method to use.

### Configuring DaVinci Forms for one-time passcodes

Complete the following steps to integrate one-time passcodes with PingOne using DaVinci Forms.

#### Creating a DaVinci Form

1. [Create a form](https://docs.pingidentity.com/pingone/user_experience/p1_creating_form.html) to display your selected external identity providers.

   |   |                                                                                                                                                                           |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | PingOne includes a number of prebuilt templates that you can modify as required.![Out-of-the-box DaVinci Forms templates.](../../_images/davinci-forms-templates-OTP.png) |

2. To add one-time passcode delivery methods to the form:

   1. From the **Toolbox** tab, drag either of the following components onto your form:

      * **[icon: trackpad_input, set=material, size=inline] MFA Device Selection - Authentication**

        Use this component when users are signing in to the system with an existing account, and have previously registered their email or phone number.

      * **[icon: trackpad_input, set=material, size=inline] MFA Device Selection - Registration**

        Use this component when users are registering an account. The next step in the flow would be to ask for their email address or phone number.

      ![Adding an MFA selection list to a form in PingOne](../../_images/davinci-form-otp-select-auth.png)Figure 1. Adding an MFA selection list to a form in PingOne.

      |   |                                                                                                                                                                                |
      | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
      |   | The form preview area and configuration panel for the MFA components list all MFA methods.The actual list displayed to users is limited by the MFA policy you created earlier. |

3. Save your changes.

Learn more in [Creating a form](https://docs.pingidentity.com/pingone/user_experience/p1_creating_form.html) in the PingOne documentation.

#### Adding a form to a DaVinci flow

When you have created your MFA option forms, you must now include them as part of your DaVinci flow.

1. [Add the forms](https://docs.pingidentity.com/connectors/forms_connector.html#including-a-form-in-a-flow) you created to display OTP delivery options to a flow by using the [PingOne Forms connector](https://docs.pingidentity.com/connectors/forms_connector.html).

   ![Example of a Forms Connector in a DaVinci flow.](../../_images/davinci-form-select-device.png)Figure 2. Example of a Forms Connector in a DaVinci flow.

2. Save your changes.

## Configuring a DaVinci flow to be launched by the Orchestration SDKs

Now that your DaVinci flow is configured to display your OTP delivery methods you must configure PingOne so that you can launch the flow by using the Orchestration SDKs.

This involves performing the following high-level steps:

1. Checking that your DaVinci flow uses only [compatible connectors and fields](../../compatibility.html).

2. Creating an application in DaVinci to connect PingOne to the DaVinci flow.

3. Creating an application in PingOne that the Orchestration SDKs can connect to and access the DaVinci application and its PingOne Flow Policy.

To learn how to complete the steps, refer to [Launching a flow with a Ping SDK](https://docs.pingidentity.com/davinci/integrating_flows_into_applications/davinci_sdk_launching_a_flow_with_the_sdk.html) in the DaVinci documentation.

## Next Steps

Now that you have configured PingOne with OTP options, added them to a DaVinci flow, and configured applications so that the Orchestration SDKs can launch them, you are ready to connect the Orchestration SDKs.

## Related links

* [Adding a connector](https://docs.pingidentity.com/davinci/connectors/davinci_adding_a_connector.html)

* [HTTP Connector](https://docs.pingidentity.com/connectors/http_connector.html#adding-custom-html)

* [DaVinci Forms](https://docs.pingidentity.com/pingone/user_experience/p1_forms.html)

  * [Adding a form to a DaVinci flow](https://docs.pingidentity.com/connectors/forms_connector.html#including-a-form-in-a-flow)

---

---
title: Compatibility
description: Details the compatibility of the DaVinci modules, including supported operating systems, browsers, and the specific PingOne fields and collectors that are supported.
component: orchsdks
page_id: orchsdks:davinci:compatibility
canonical_url: https://developer.pingidentity.com/orchsdks/davinci/compatibility.html
llms_txt: https://developer.pingidentity.com/orchsdks/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: Fri, 9 Jan 2026 17:23:51 +0000
keywords: ["DaVinci", "Compatibility", "Supported OS", "Browsers", "PingOne Fields", "Collectors"]
section_ids:
  supported-servers: Supported server versions
  supported-os: Supported operating systems and browsers
  supported-davinci-fields: Supported PingOne fields and collectors
  webviews_unsupported_davinci: JavaScript Compatibility with WebViews
---

# Compatibility

[icon: circle-check, set=far]PingOne [icon: android, set=fab]Android [icon: apple, set=fab]iOS [icon: js, set=fab]JavaScript

## Supported server versions

The **DaVinci** module is compatible with the following servers:

* PingOne

  Current version.

## Supported operating systems and browsers

Select a platform below to view the supported operating systems and browsers.

* Android

* iOS

* JavaScript / Login Widget

* React Native

The Orchestration SDK for Android supports the following versions of the Android operating system:

**Supported Android versions and original release dates**

| Release    | API Levels | Release date    |
| ---------- | ---------- | --------------- |
| Android 17 | 37         | June, 2026      |
| Android 16 | 36         | August, 2025    |
| Android 15 | 35         | September, 2024 |
| Android 14 | 34         | October, 2023   |
| Android 13 | 33         | March, 2022     |
| Android 12 | 31, 32     | October, 2021   |
| Android 11 | 30         | September, 2020 |

|   |                                                                                                                                                                                                                                                                                                        |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | We have updated how we determine which Android versions form our support policy for the Orchestration SDK for Android.The support policy is as follows:- Every public major release of Android within the last 6 years.

  For example, this would mean support for **Android 11** and later versions. |

**Supported browsers on Android**

* Chrome - Two most recent major versions.

The Orchestration SDK for iOS supports the following versions of the iOS operating system:

**Supported iOS versions and original release dates**

| Release | Release date    |
| ------- | --------------- |
| iOS 27  | September, 2026 |
| iOS 26  | September, 2025 |
| iOS 18  | September, 2024 |
| iOS 17  | September, 2023 |

|   |                                                                                                                                                                                                                                                                                        |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | We have updated how we determine which iOS versions form our support policy for the Orchestration SDK for iOS.The support policy is as follows:- Every public major release of iOS within the last 3 years.

  For example, this would mean support for **iOS 17** and later versions. |

**Supported browsers on iOS**

* Safari - Two most recent major versions.

The Orchestration SDK for JavaScript, and the Advanced Identity Cloud/PingAM Login Widget support the [desktop](#js-desktop-browsers) and [mobile](#js-desktop-browsers) browsers listed below.

**Minimum supported Desktop browser versions**

* Chrome 83

* Firefox 77

* Safari 13

* Microsoft Edge 83 (Chromium)

**Supported Mobile browsers**

* iOS (Safari) - Two most recent major versions of the operating system.

* Android (Chrome) - Two most recent major versions of the operating system.

The Orchestration SDK for React Native modules wrap the native Android and iOS Orchestration SDK modules, so supported operating systems and browsers are a superset of the Android and iOS support listed in the tabs above.

Support depends on the platform the app runs on:

**Supported Android versions and original release dates**

| Release    | API Levels | Release date    |
| ---------- | ---------- | --------------- |
| Android 17 | 37         | June, 2026      |
| Android 16 | 36         | August, 2025    |
| Android 15 | 35         | September, 2024 |
| Android 14 | 34         | October, 2023   |
| Android 13 | 33         | March, 2022     |
| Android 12 | 31, 32     | October, 2021   |
| Android 11 | 30         | September, 2020 |

**Supported iOS versions and original release dates**

| Release | Release date    |
| ------- | --------------- |
| iOS 27  | September, 2026 |
| iOS 26  | September, 2025 |
| iOS 18  | September, 2024 |
| iOS 17  | September, 2023 |

## Supported PingOne fields and collectors

The DaVinci modules support the following connectors and capabilities:

* PingOne Forms Connector

  * **Show Form** capability

* HTTP Connector

  * **Custom HTML** capability

* PingOne Protect Connector

  * **Create Risk Evaluation** capability

* DaVinci SDK Integrator

  * **Exchange Custom Metadata with DaVinci SDK** capability

* PingOne MFA Connector

  * **Mobile Pairing** capability

- PingOne Form Connector fields

- HTTP Connector fields

- PingOne Protect Connector fields

- DaVinci SDK Integrator fields

- PingOne MFA Connector fields

* [Connector property support](#form-connector-properties-compatibility)

* [Custom Fields support](#form-connector-fields-compatibility)

* [Toolbox support](#form-connector-toolbox-compatibility)

**Connector property support**

| Property                                                                                                                                                                               | Collector                 |                           |                           |                         |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------- | ------------------------- | ------------------------- | ----------------------- |
|                                                                                                                                                                                        | Android                   | iOS                       | JavaScript                | React Native            |
| **Enable Device Profiling**Instructs PingOne Protect to collect device information.                                                                                                    | `ProtectCollector``2.0.0` | `ProtectCollector``2.0.0` | `ProtectCollector``2.0.0` | ProtectCollector`1.1.0` |
| **Include Behavioral Data**When enabled, PingOne Protect collects behavioral data to identify non-human activity.You must first select **Enable Device Profiling** to use this option. | `ProtectCollector``2.0.0` | `ProtectCollector``2.0.0` | `ProtectCollector``2.0.0` | ProtectCollector`1.1.0` |

**Custom Fields support**

| Field                                                                                                                                                                                                                                                                             | Collector                      |                                |                                                                                                                                                                                                                                    |                              |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------ | ------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------- |
|                                                                                                                                                                                                                                                                                   | Android                        | iOS                            | JavaScript                                                                                                                                                                                                                         | React Native                 |
| **Checkbox**Collects `true` or `false` from a checkbox or switch.                                                                                                                                                                                                                 | `BooleanCollector``2.1.0`      | `BooleanCollector``2.1.0`      | `BooleanCollector` / `ValidatedBooleanCollector`\[[1](#_footnotedef_1 "View footnote.")]`2.1.0`***[1](#_footnoteref_1). `ValidatedBooleanCollector` is returned for required checkboxes, and `BooleanCollector` for optional ones. | BooleanCollector`1.1.0`      |
| **Checkbox List**Collects the value of one or more checkboxes.                                                                                                                                                                                                                    | `MultiSelectCollector``1.1.0`  | `MultiSelectCollector``1.1.0`  | `MultiValueCollector``1.1.0`                                                                                                                                                                                                       | MultiSelectCollector`1.1.0`  |
| **Combobox**Collects a value from a dropdown containing one or more text strings.                                                                                                                                                                                                 | `MultiSelectCollector``1.1.0`  | `MultiSelectCollector``1.1.0`  | `MultiValueCollector``1.1.0`                                                                                                                                                                                                       | MultiSelectCollector`1.1.0`  |
| **Dropdown**Collects a value from a dropdown containing one or more text strings.                                                                                                                                                                                                 | `SingleSelectCollector``1.1.0` | `SingleSelectCollector``1.1.0` | `SingleValueCollector``1.1.0`                                                                                                                                                                                                      | SingleSelectCollector`1.1.0` |
| **Password**Collects a single text string that cannot be read from the screen, and optionally verifies the provided value against a policy.\[[2](#_footnotedef_2 "View footnote.")]***[2](#_footnoteref_2). Support for verification against password policies was added in 2.1.0 | `PasswordCollector``1.1.0`     | `PasswordCollector``1.1.0`     | `PasswordCollector``1.1.0`                                                                                                                                                                                                         | PasswordCollector`1.1.0`     |
| **New Password**Collects a new password and validates it against the environment's password policy. Optionally presents password requirements to the user.                                                                                                                        | ❌                              | ❌                              | `ValidatedPasswordCollector``2.1.0`                                                                                                                                                                                                | ❌                            |
| **Phone Number Input**Collects a phone number, with optional country code, and extension values.\[[3](#_footnotedef_3 "View footnote.")]***[3](#_footnoteref_3). Support for the extension value was added in 2.1.0                                                               | `PhoneNumberCollector``1.2.0`  | `PhoneNumberCollector``1.2.0`  | `PhoneNumberCollector` / `PhoneNumberExtensionCollector``1.2.0`                                                                                                                                                                    | PhoneNumberCollector`1.1.0`  |
| **Radio Button List**Collects a value from one or radio buttons.                                                                                                                                                                                                                  | `SingleSelectCollector``1.1.0` | `SingleSelectCollector``1.1.0` | `SingleValueCollector``1.1.0`                                                                                                                                                                                                      | SingleSelectCollector`1.1.0` |
| **Submit Button**Presents a button for form submission.                                                                                                                                                                                                                           | `SubmitCollector``1.1.0`       | `SubmitCollector``1.1.0`       | `SubmitCollector``1.1.0`                                                                                                                                                                                                           | SubmitCollector`1.1.0`       |
| **Text Input**Collects a single text string.                                                                                                                                                                                                                                      | `TextCollector``1.1.0`         | `TextCollector``1.1.0`         | `TextCollector``1.1.0`                                                                                                                                                                                                             | TextCollector`1.1.0`         |

**Toolbox support**

| Field                                                                                                                                                                                                                                   | Collector                                                          |                                                                    |                                                                    |                                                                |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | -------------------------------------------------------------- |
|                                                                                                                                                                                                                                         | Android                                                            | iOS                                                                | JavaScript                                                         | React Native                                                   |
| **Agreement**Presents text configured in PingOne under **User Experience** > **Agreements**, such as terms of service.                                                                                                                  | `ReadOnlyTextCollector``2.1.0`                                     | `ReadOnlyTextCollector``2.1.0`                                     | `ReadOnlyCollector``2.1.0`                                         | ReadOnlyTextCollector`1.1.0`                                   |
| **FIDO2**Allows users to perform multi-factor authentication with a FIDO2 device, or register a new device.                                                                                                                             | `FidoAuthenticationCollector` / `FidoRegistrationCollector``1.3.0` | `FidoAuthenticationCollector` / `FidoRegistrationCollector``1.3.0` | `FidoAuthenticationCollector` / `FidoRegistrationCollector``1.3.0` | FidoAuthenticationCollector / FidoRegistrationCollector`1.1.0` |
| **Image**Presents an image.                                                                                                                                                                                                             | `ImageCollector``2.2.0`                                            | `ImageCollector``2.2.0`                                            | `ImageCollector``2.1.0`                                            | ❌                                                              |
| **Flow Button**Presents a customized button.                                                                                                                                                                                            | `FlowCollector``1.1.0`                                             | `FlowCollector``1.1.0`                                             | `FlowCollector``1.1.0`                                             | FlowCollector`1.1.0`                                           |
| **Flow Link**Presents a customized link.                                                                                                                                                                                                | `FlowCollector``1.1.0`                                             | `FlowCollector``1.1.0`                                             | `FlowCollector``1.1.0`                                             | FlowCollector`1.1.0`                                           |
| **MFA Device Selection - Authentication**Presents a list of methods for performing multi-factor authentication (MFA).&#xA;&#xA;DaVinci client supports the FIDO2, Email, SMS, and Voice MFA types.                                      | `DeviceAuthenticationCollector``1.2.0`                             | `DeviceAuthenticationCollector``1.2.0`                             | `DeviceAuthenticationCollector``1.2.0`                             | DeviceAuthenticationCollector`1.1.0`                           |
| **MFA Device Selection - Registration**Presents a list of methods you can register for multi-factor authentication (MFA).&#xA;&#xA;DaVinci client supports the FIDO2, Email, SMS, and Voice MFA types.                                  | `DeviceRegistrationCollector``1.2.0`                               | `DeviceRegistrationCollector``1.2.0`                               | `DeviceRegistrationCollector``1.2.0`                               | DeviceRegistrationCollector`1.1.0`                             |
| **Polling**Presents an activity indicator which allows you to pause or loop the flow while the user completes an action.                                                                                                                | `PollingCollector``2.1.0`                                          | `PollingCollector``2.1.0`                                          | `PollingCollector``2.1.0`                                          | PollingCollector`1.1.0`                                        |
| **QR Code**Presents a QR code containing data, for example, a URL.                                                                                                                                                                      | `QRCodeCollector``2.1.0`                                           | `QRCodeCollector``2.1.0`                                           | `QrCodeCollector``2.1.0`                                           | QRCodeCollector`1.1.0`                                         |
| **Social Login**Presents a button to allow users to authenticate using an external identity provider, such as Apple, Facebook, or Google.                                                                                               | `IdpCollector``1.1.0`                                              | `IdpCollector``1.1.0`                                              | `IdpCollector``1.1.0`                                              | IdpCollector`1.1.0`                                            |
| **Translatable Rich Text**Presents rich text, including links, that you can translate into multiple languages.\[[4](#_footnotedef_4 "View footnote.")]***[4](#_footnoteref_4). Support for links in rich text fields was added in 2.1.0 | `LabelCollector``1.1.0`                                            | `LabelCollector``1.1.0`                                            | `RichTextCollector``1.1.0`                                         | LabelCollector`1.1.0`                                          |

* [HTTP Connector field and collector support](#http-connector-fields-compatibility)

* [HTTP Connector SK-Component support](#http-connector-sk-components-compatibility)

**HTTP Connector field and collector support**

| Field                                                                                             | Collector                      |                                |                               |                              |
| ------------------------------------------------------------------------------------------------- | ------------------------------ | ------------------------------ | ----------------------------- | ---------------------------- |
|                                                                                                   | Android                        | iOS                            | JavaScript                    | React Native                 |
| **Text field**Collects a single text string.                                                      | `TextCollector``1.0.0`         | `TextCollector``1.0.0`         | `TextCollector``1.0.0`        | TextCollector`1.1.0`         |
| **Password field**Collects a single text string that cannot be read from the screen.              | `PasswordCollector``1.0.0`     | `PasswordCollector``1.0.0`     | `PasswordCollector``1.0.0`    | PasswordCollector`1.1.0`     |
| **Submit Button**Sends the collected data to PingOne to continue the DaVinci flow.                | `SubmitCollector``1.0.0`       | `SubmitCollector``1.0.0`       | `SubmitCollector``1.0.0`      | SubmitCollector`1.1.0`       |
| **Flow Button**Triggers an alternative flow without sending the data collected so far to PingOne. | `FlowCollector``1.0.0`         | `FlowCollector``1.0.0`         | `FlowCollector``1.0.0`        | FlowCollector`1.1.0`         |
| **Label**Display a read-only text label.                                                          | `ReadOnlyTextCollector``1.1.0` | `LabelCollector``1.1.0`        | `ReadOnlyCollector``1.1.0`    | LabelCollector`1.1.0`        |
| **Radio** / **Dropdown**Collects a single value from a choice of multiple options.                | `SingleSelectCollector``1.1.0` | `SingleSelectCollector``1.1.0` | `SingleValueCollector``1.1.0` | SingleSelectCollector`1.1.0` |

**HTTP Connector SK-Component support**

| SK-Component                                                                                                                       | DaVinci module            |                           |                           |                         |
| ---------------------------------------------------------------------------------------------------------------------------------- | ------------------------- | ------------------------- | ------------------------- | ----------------------- |
|                                                                                                                                    | Android                   | iOS                       | JavaScript                | React Native            |
| **skIDP**Presents a button to allow users to authenticate using an external identity provider, such as Apple, Facebook, or Google. | `IdpCollector``1.1.0`     | `IdpCollector``1.1.0`     | `IdpCollector``1.1.0`     | IdpCollector`1.1.0`     |
| **skrisk**Instructs the client to gather behavioral data and return it to PingOne so that it can perform risk evaluations.         | `ProtectCollector``1.3.0` | `ProtectCollector``1.3.0` | `ProtectCollector``1.3.0` | ProtectCollector`1.1.0` |

**Unsupported features:**

Verify that your flow does not depend on any *unsupported* elements:

* SKPolling components

  The [**SKPolling**](https://docs.pingidentity.com/davinci/flows/davinci_sk_components.html#skpolling) component cannot be processed by the DaVinci Client and should not be included in flows.

  Features such as Magic Link authentication require the **SKPolling** component and therefore cannot be used with the DaVinci Client.

* Images

  Images embedded in a Custom HTML Template, such as background images or logos, cannot be passed to the Orchestration SDK as structured data.

**PingOne Protect Connector support overview**

| Capability                                                                                                                | Collector                 |                           |                           |                         |
| ------------------------------------------------------------------------------------------------------------------------- | ------------------------- | ------------------------- | ------------------------- | ----------------------- |
|                                                                                                                           | Android                   | iOS                       | JavaScript                | React Native            |
| **Create Risk Evaluation**Sends device and behavioral data collected by PingOne Protect to DaVinci for a risk evaluation. | `ProtectCollector``1.3.0` | `ProtectCollector``1.3.0` | `ProtectCollector``1.3.0` | ProtectCollector`1.1.0` |

**DaVinci SDK Integrator support overview**

| Capability                                                                                                                                                 | Collector                  |                            |                            |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------- | -------------------------- | -------------------------- |
|                                                                                                                                                            | Android                    | iOS                        | JavaScript                 |
| **Exchange Custom Metadata**Exchanges custom JSON metadata and payloads between a DaVinci flow and the app, pausing flow execution until the app responds. | `MetadataCollector``2.2.0` | `MetadataCollector``2.2.0` | `MetadataCollector``2.2.0` |

**PingOne MFA Connector support overview**

| Capability                                                                                                      | Collector                       |                                 |            |
| --------------------------------------------------------------------------------------------------------------- | ------------------------------- | ------------------------------- | ---------- |
|                                                                                                                 | Android                         | iOS                             | JavaScript |
| **Mobile Pairing**Pairs the user's PingOne MFA account directly within a DaVinci flow, without leaving the app. | `MobilePairingCollector``2.2.0` | `MobilePairingCollector``2.2.0` | ❌          |

### JavaScript Compatibility with WebViews

A WebView allows you to embed a web browser into your native Android or iOS application to display HTML pages, and run JavaScript apps.

For example, the Android system WebView is based on the Google Chrome engine, and the iOS WebView is based on the Safari browser engine.

However, it is important to note that WebViews do not implement the full feature set of their respective browsers. For example, some of the browser-provided APIs that the Orchestration SDK for JavaScript requires are not available in a WebView, such as the WebAuthn APIs.

In addition, there are concerns that a WebView does not provide the same level of security as their full browser counterparts.

As the SDK requires full, spec-compliant, browser-supplied APIs for full functionality we **do not** support usage within a WebView.

We also do not support or test usage with any wrappers around WebViews.

Whilst you might be able to implement simple use-cases using the Orchestration SDK for JavaScript within a WebView, we recommend that you use an alternative such as opening a full browser, or using an in-app instance of a full browser such as [Custom Tabs](https://developer.android.com/develop/ui/views/layout/webapps/overview-of-android-custom-tabs) for Android or [SFSafariViewController](https://developer.apple.com/documentation/safariservices/sfsafariviewcontroller) for iOS.

---

---
title: Configure a JavaScript app for social sign-on
description: Configure a JavaScript app to authenticate users with an external identity provider using DaVinci flows
component: orchsdks
page_id: orchsdks:davinci:use-cases/external-idp/javascript/index
canonical_url: https://developer.pingidentity.com/orchsdks/davinci/use-cases/external-idp/javascript/index.html
llms_txt: https://developer.pingidentity.com/orchsdks/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: Tue, 25 Mar 2025 11:00:37 +0100
keywords: ["PingOne", "DaVinci", "Flows", "Setup &amp; Configuration", "Source Code", "Use Case", "SDK", "IdP", "JavaScript"]
section_ids:
  step_1_adding_core_dependencies: Step 1. Adding core dependencies
  step_2_authenticating_with_external_idps: Step 2. Authenticating with external IdPs
---

# Configure a JavaScript app for social sign-on

[icon: circle-check, set=far]PingOne [icon: js, set=fab]JavaScript

Complete the following high-level tasks to configure a JavaScript client app to perform social sign-on with an external identity provider (IdP):

## [Step 1. Adding core dependencies](01_adding_core_dependencies.html)

These dependencies provide core support for social sign-on. These are the minimum required dependencies for redirecting users to the IdP for authentication.

[**Start step 1**[icon: chevrons-right, set=fas, size=xs]](01_adding_core_dependencies.html)

## [Step 2. Authenticating with external IdPs](02_authenticate_with_external_idps.html)

Learn how to authenticate your users with the external IdPs you have configured in your DaVinci flows.

[**Start step 2**[icon: chevrons-right, set=fas, size=xs]](02_authenticate_with_external_idps.html)

---

---
title: Configure a React Native app for social sign-on
description: Configure a React Native app to perform social sign-on with an external identity provider using DaVinci flows
component: orchsdks
page_id: orchsdks:davinci:use-cases/external-idp/react-native/index
canonical_url: https://developer.pingidentity.com/orchsdks/davinci/use-cases/external-idp/react-native/index.html
llms_txt: https://developer.pingidentity.com/orchsdks/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: Thu, 4 Sep 2026 00:00:00 +0000
keywords: ["PingOne", "DaVinci", "Flows", "Setup &amp; Configuration", "Source Code", "Use Case", "SDK", "IdP", "React Native"]
section_ids:
  before_you_begin: Before you begin
  step_1_adding_core_dependencies: Step 1. Adding core dependencies
  step_2_handling_uri_schemes: Step 2. Handling URI schemes
  step_3_configuring_native_provider_sdks: Step 3. Configuring native provider SDKs
  step_4_authenticating_with_external_idps: Step 4. Authenticating with external IdPs
---

# Configure a React Native app for social sign-on

[icon: circle-check, set=far]PingOne [icon: react, set=fab]React Native

Complete the following high-level tasks to configure a React Native app to perform social sign-on with an external identity provider (IdP):

## [Before you begin](../before-you-begin.html)

Ensure that you have completed the prerequisites before starting the numbered steps on this page below.

You need to have configured Apple, Facebook, and Google as external identity providers in PingOne, and set up the DaVinci flows your client app will step through.

[**Complete prerequisites**[icon: chevrons-right, set=fas, size=xs]](../before-you-begin.html)

## [Step 1. Adding core dependencies](01_adding_core_dependencies.html)

Install the **External IdP**, **DaVinci**, and supporting modules.

[**Start step 1**[icon: chevrons-right, set=fas, size=xs]](01_adding_core_dependencies.html)

## [Step 2. Handling URI schemes](02_handling_uri_schemes.html)

Register a URI scheme on Android and iOS so the OS can route provider redirects back to your app.

[**Start step 2**[icon: chevrons-right, set=fas, size=xs]](02_handling_uri_schemes.html)

## [Step 3. Configuring native provider SDKs](03_configuring_native_provider_sdks.html)

Add and configure the native SDK for each provider you want to support. The React Native **External IdP** module authenticates users with the provider's native SDK, and falls back to a browser redirect when the native SDK is not linked.

[**Start step 3**[icon: chevrons-right, set=fas, size=xs]](03_configuring_native_provider_sdks.html)

## [Step 4. Authenticating with external IdPs](04_authenticate_with_external_idps.html)

Learn how to authenticate your users with the external IdPs you have configured in your DaVinci flows.

[**Start step 4**[icon: chevrons-right, set=fas, size=xs]](04_authenticate_with_external_idps.html)

---

---
title: Configure an Android app for social sign-on
description: Configure an Android app to perform social sign-on with an external identity provider using DaVinci flows
component: orchsdks
page_id: orchsdks:davinci:use-cases/external-idp/android/index
canonical_url: https://developer.pingidentity.com/orchsdks/davinci/use-cases/external-idp/android/index.html
llms_txt: https://developer.pingidentity.com/orchsdks/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: Tue, 25 Mar 2025 11:00:37 +0100
keywords: ["PingOne", "DaVinci", "Flows", "Setup &amp; Configuration", "Source Code", "Use Case", "SDK", "IdP"]
section_ids:
  step_1_adding_core_dependencies: Step 1. Adding core dependencies
  step_2_handling_uri_schemes: Step 2. Handling URI schemes
  step_3_authenticating_with_external_idps: Step 3. Authenticating with external IdPs
  step_4_customizing_the_user_experience: Step 4. Customizing the user experience
---

# Configure an Android app for social sign-on

[icon: circle-check, set=far]PingOne [icon: android, set=fab]Android

Complete the following high-level tasks to configure an Android client app to perform social sign-on with an external identity provider (IdP):

## [Step 1. Adding core dependencies](01_adding_core_dependencies.html)

These dependencies provide core support for social sign-on. These are the minimum required dependencies for redirecting users to the IdP for authentication.

[**Start step 1**[icon: chevrons-right, set=fas, size=xs]](01_adding_core_dependencies.html)

## [Step 2. Handling URI schemes](02_handling_uri_schemes.html)

You must configure your Android app to open when the server redirects the user after authentication.

[**Start step 2**[icon: chevrons-right, set=fas, size=xs]](02_handling_uri_schemes.html)

## [Step 3. Authenticating with external IdPs](03_authenticate_with_external_idps.html)

Learn how to authenticate your users with the external IdPs you have configured in your DaVinci flows.

[**Start step 3**[icon: chevrons-right, set=fas, size=xs]](03_authenticate_with_external_idps.html)

## [Step 4. Customizing the user experience](04_customize_the_user_experience.html)

You can optionally tweak the user experience for authenticating with an external IdP.

[**Start step 4**[icon: chevrons-right, set=fas, size=xs]](04_customize_the_user_experience.html)

---

---
title: Configure an iOS app for social sign-on
description: Configure an iOS app to support social sign-on with external identity providers using DaVinci flows
component: orchsdks
page_id: orchsdks:davinci:use-cases/external-idp/ios/index
canonical_url: https://developer.pingidentity.com/orchsdks/davinci/use-cases/external-idp/ios/index.html
llms_txt: https://developer.pingidentity.com/orchsdks/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: Tue, 25 Mar 2025 11:00:37 +0100
keywords: ["PingOne", "DaVinci", "Flows", "Setup &amp; Configuration", "Source Code", "Use Case", "SDK", "IdP"]
section_ids:
  step_1_adding_core_dependencies: Step 1. Adding core dependencies
  step_2_handling_uri_schemes: Step 2. Handling URI schemes
  step_3_authenticating_with_external_idps: Step 3. Authenticating with external IdPs
  step_4_customizing_the_user_experience: Step 4. Customizing the user experience
---

# Configure an iOS app for social sign-on

[icon: circle-check, set=far]PingOne [icon: apple, set=fab]iOS

Complete the following high-level tasks to configure an iOS client app to perform social sign-on with an external identity provider (IdP):

## [Step 1. Adding core dependencies](01_adding_core_dependencies.html)

These dependencies provide core support for social sign-on. These are the minimum required dependencies for redirecting users to the IdP for authentication.

[**Start step 1**[icon: chevrons-right, set=fas, size=xs]](01_adding_core_dependencies.html)

## [Step 2. Handling URI schemes](02_handling_uri_schemes.html)

You must configure your iOS app to open when the server redirects the user after authentication.

[**Start step 2**[icon: chevrons-right, set=fas, size=xs]](02_handling_uri_schemes.html)

## [Step 3. Authenticating with external IdPs](03_authenticate_with_external_idps.html)

Learn how to authenticate your users with the external IdPs you have configured in your DaVinci flows.

[**Start step 3**[icon: chevrons-right, set=fas, size=xs]](03_authenticate_with_external_idps.html)

## [Step 4. Customizing the user experience](04_customize_the_user_experience.html)

You can optionally tweak the user experience for authenticating with an external IdP.

[**Start step 4**[icon: chevrons-right, set=fas, size=xs]](04_customize_the_user_experience.html)

---

---
title: Configure client apps for one-time passcodes
description: Explains how to handle `DeviceRegistrationCollector` and `DeviceAuthenticationCollector` in your Android, iOS, and JavaScript apps to implement one-time passcode authentication.
component: orchsdks
page_id: orchsdks:davinci:use-cases/otp/01_handle-one-time-passcodes-in-client-apps
canonical_url: https://developer.pingidentity.com/orchsdks/davinci/use-cases/otp/01_handle-one-time-passcodes-in-client-apps.html
llms_txt: https://developer.pingidentity.com/orchsdks/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: Fri, 9 Jan 2026 17:23:51 +0000
keywords: ["DaVinci", "OTP", "Client Apps", "Android", "iOS", "JavaScript", "Collectors"]
section_ids:
  android-otp: Configure an Android app to use one-time passcodes
  ios-otp: Configure an iOS app to use one-time passcodes
  javascript-otp: Configure a JavaScript app to use one-time passcodes
---

# Configure client apps for one-time passcodes

[icon: circle-check, set=far]PingOne [icon: android, set=fab]Android [icon: apple, set=fab]iOS [icon: js, set=fab]JavaScript

Select your platform to discover how to configure your client application to use one-time passcodes during an authentication flow.

[icon: android, set=fab, size=3x]

#### [Android](#android-otp)

Configure an Android app to use one-time passcodes

[icon: apple, set=fab, size=3x]

#### [iOS](#ios-otp)

Configure an iOS app to use one-time passcodes

[icon: js, set=fab, size=3x]

#### [JavaScript](#javascript-otp)

Configure a JavaScript app to use one-time passcodes

## Configure an Android app to use one-time passcodes

Your app must handle the `DeviceRegistrationCollector` and `DeviceAuthenticationCollector` collector types that DaVinci sends. These contain details of the available one-time passcode delivery methods.

|   |                                                                                                                 |
| - | --------------------------------------------------------------------------------------------------------------- |
|   | Learn more about setting up an app to receive collectors in the [Try the DaVinci module](../../tutorials.html). |

Loop through the collectors returned by DaVinci, ensuring you handle the one-time passcode collectors:

```kotlin
continueNode.collectors.forEach {
    when (it) {

        // Other collectors here...

        is DeviceRegistrationCollector -> {
            // Compose to display DeviceRegistrationCollector
            DeviceRegistration(it, onNext)
        }
        is DeviceAuthenticationCollector -> {
            // Compose to display DeviceAuthenticationCollector
            DeviceAuthentication(it, onNext)
        }
        // Compose to display PhoneNumberCollector
        is PhoneNumberCollector -> PhoneNumber (it, onNodeUpdated)
    }
}
```

After collecting the data for a node you can proceed to the next node in the flow by calling the `next()` method on your current `node` object.

Learn more about `node.next()` in [Continuing a DaVinci flow](../../usage/android/03-stepping-through-davinci-flows.html#node-next).

Sample collector view files:

* [Sample DeviceRegistration.kt code](https://github.com/ForgeRock/ping-android-sdk/blob/master/samples/app/src/main/java/com/pingidentity/samples/app/davinci/collector/DeviceRegistration.kt)

* [Sample DeviceAuthentication.kt code](https://github.com/ForgeRock/ping-android-sdk/blob/master/samples/app/src/main/java/com/pingidentity/samples/app/davinci/collector/DeviceAuthentication.kt)

* [Sample PhoneNumber.kt code](https://github.com/ForgeRock/ping-android-sdk/blob/master/samples/app/src/main/java/com/pingidentity/samples/app/davinci/collector/PhoneNumber.kt)

## Configure an iOS app to use one-time passcodes

Your app must handle the `DeviceRegistrationCollector` and `DeviceAuthenticationCollector` collector types that DaVinci sends. These contain details of the available one-time passcode delivery methods.

|   |                                                                                                                 |
| - | --------------------------------------------------------------------------------------------------------------- |
|   | Learn more about setting up an app to receive collectors in the [Try the DaVinci module](../../tutorials.html). |

Loop through the collectors returned by DaVinci, ensuring you handle the one-time passcode collectors:

```swift
ForEach(continueNode.collectors , id: \.id) { collector in
    switch collector {

    // Other collectors here...

    case is DeviceRegistrationCollector:
        if let deviceRegistrationCollector = collector as? DeviceRegistrationCollector {
            DeviceRegistrationView(field: deviceRegistrationCollector, onNext: onNext)
        }
    case is DeviceAuthenticationCollector:
        if let deviceAuthenticationCollector = collector as? DeviceAuthenticationCollector {
            DeviceAuthenticationView(field: deviceAuthenticationCollector, onNext: onNext)
        }
    case is PhoneNumberCollector:
        if let phoneNumberCollector = collector as? PhoneNumberCollector {
            PhoneNumberView(field: phoneNumberCollector, onNodeUpdated: onNodeUpdated)
        }
    default:
        EmptyView()
    }
}
```

After collecting the data for a node you can proceed to the next node in the flow by calling the `next()` method on your current `node` object.

Learn more about `node.next()` in [Continuing a DaVinci flow](../../usage/ios/03-stepping-through-davinci-flows.html#node-next).

Sample collector view files:

* [Sample DeviceRegistrationView.swift code](https://github.com/ForgeRock/ping-ios-sdk/blob/master/SampleApps/PingExample/PingExample/Collectors/DeviceRegistrationView.swift)

* [Sample DeviceAuthenticationView.swift code](https://github.com/ForgeRock/ping-ios-sdk/blob/master/SampleApps/PingExample/PingExample/Collectors/DeviceAuthenticationView.swift)

* [Sample PhoneNumberView.swift code](https://github.com/ForgeRock/ping-ios-sdk/blob/master/SampleApps/PingExample/PingExample/Collectors/PhoneNumberView.swift)

## Configure a JavaScript app to use one-time passcodes

Your app must handle the `DeviceRegistrationCollector` and `DeviceAuthenticationCollector` collector types that DaVinci sends. These contain details of the available one-time passcode delivery methods.

You might also need to handle `PhoneNumberCollector` collectors, if the user chooses Voice or SMS as their MFA method, for example.

|   |                                                                                                                 |
| - | --------------------------------------------------------------------------------------------------------------- |
|   | Learn more about setting up an app to receive collectors in the [Try the DaVinci module](../../tutorials.html). |

Loop through the collectors returned by DaVinci, ensuring you handle the one-time passcode collectors:

```typescript
const collectors = davinciClient.getCollectors();

collectors.forEach((collector) => {
  if (
    collector.type === 'DeviceRegistrationCollector' ||
    collector.type === 'DeviceAuthenticationCollector'
  ) {
    deviceComponent(
      collector, // Object of the collector
      davinciClient.update(collector), // Return updater for collector
    );
  } else if (collector.type === 'PhoneNumberCollector') {
    phoneNumberComponent(
      collector, // Object of the collector
      davinciClient.update(collector), // Return updater for collector
    );
  }
});
```

In this example, a `deviceComponent` or `phoneNumberComponent` component handles rendering the relevant user interface. Pass the selected option into the `updater()` method:

Example `deviceComponent` file to render OTP selection

```typescript
export default function deviceComponent(
  collector: DeviceRegistrationCollector | DeviceAuthenticationCollector,
  updater: Updater,
) {
  const groupLabel = collector.output.label || 'Select an option';

  // Bind to options to handle user selection
  function eventHandler(event) {
    const selectedValue = // get value from event's target element

    updater(selectedValue);
  }

  // Iterate over the options and render each
  for (const option of collector.output.options) {
    const elementLabel = option.label;
    const elementValue = option.value;

    // Render each element to DOM
  }
}
```

Example `phoneNumberComponent` file to render OTP selection

```typescript
export default function phoneNumberComponent(
  collector: PhoneNumberCollector,
  updater: Updater,
) {
  const phoneLabel = collector.output.label || 'Phone Number';

  // Get default or existing values
  const countryCodeValue = collector.output.value.countryCode;
  const phoneNumberValue = collector.output.value.phoneNumber;

  // This just uses a mutable object for simplicity
  let phoneObject = {
    countryCode: countryCodeValue,
    phoneNumber: phoneNumberValue,
  };

  // Add change event listener to country code select
  function handleCountryCodeEvent(event) {
    const selectedValue = // get value from event's target element

    // Mutate object then pass to updater
    phoneNumber = { ...phoneObject, countryCode: selectedValue };
    updater(phoneNumber);
  }

  // Add change event listener to phone number input
  function handlePhoneNumberEvent(event) {
    const selectedValue = // get value from event's target element

    // Mutate object then pass to updater
    phoneNumber = { ...phoneObject, phoneNumber: selectedValue };
    updater(phoneNumber);
  }

  // Render both country code select and phone number input
}
```

---

---
title: Configuring PingOne for PingOne Protect
description: Explains the necessary server-side prerequisites for integrating PingOne Protect, including configuring risk policies and adding risk evaluations to your DaVinci flows.
component: orchsdks
page_id: orchsdks:davinci:use-cases/protect/before-you-begin
canonical_url: https://developer.pingidentity.com/orchsdks/davinci/use-cases/protect/before-you-begin.html
llms_txt: https://developer.pingidentity.com/orchsdks/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["DaVinci", "PingOne Protect", "Prerequisites", "Server Configuration", "Risk Policy", "Flows"]
section_ids:
  risk-policy: Configuring a PingOne Protect risk policy
  add-to-flows: Adding PingOne Protect risk evaluations to DaVinci flows
  next_steps: Next steps
---

# Configuring PingOne for PingOne Protect

[icon: circle-check, set=far]PingOne [icon: android, set=fab]Android [icon: apple, set=fab]iOS [icon: js, set=fab]JavaScript [icon: react, set=fab]React Native

In this step, you set up your PingOne server to perform risk evaluations.

To prepare your PingOne server to perform risk evaluations, complete the following steps:

1. [Configuring a PingOne Protect risk policy](#risk-policy)

2. [Adding PingOne Protect risk evaluations to DaVinci flows](#add-to-flows)

## Configuring a PingOne Protect risk policy

Risk policies determine how the various risk predictors are combined and how the aggregated risk score should be translated into a final risk level of low, medium, or high.

PingOne provides a builtin risk policy that you can use as-is. You can also edit the default policy, or create your own.

Learn more in the PingOne documentation:

* [Editing a risk policy](https://docs.pingidentity.com/pingone/threat_protection_using_pingone_protect/p1_protect_editing_risk_policy.html)

* [Adding a risk policy](https://docs.pingidentity.com/pingone/threat_protection_using_pingone_protect/p1_protect_adding_risk_policy.html)

You'll need to use the ID of your risk policy in the next step, [Adding PingOne Protect risk evaluations to DaVinci flows](#add-to-flows).

## Adding PingOne Protect risk evaluations to DaVinci flows

You can now add risk evaluations to different types of flows, such as sign-on with MFA or passwordless sign-on.

The DaVinci Client supports the following DaVinci flow configurations:

* **PingOne Forms connector properties**

  Enable the **Enable Device Profiling** and **Include Behavioral Data** properties.

  ![pingone form connector protect settings](../../../_images/protect/pingone-form-connector-protect-settings.png)

* **HTTP connector**

  Add the `skrisk` component to your custom HTML template.

  ![pingone http connector skrisk](../../../_images/protect/pingone-http-connector-skrisk.png)

Learn more about how to configure and add these connectors to your DaVinci flows:

* [Form Connector](https://docs.pingidentity.com/connectors/form_connector.html)

* [HTTP Connector](https://docs.pingidentity.com/connectors/http_connector.html)

## Next steps

Select your platform to discover how to configure your client application to perform PingOne Protect risk evaluations when you are using DaVinci flows:

[icon: android, set=fab, size=3x]

#### [Android](android/index.html)

Integrate Android apps with PingOne Protect DaVinci flows

[icon: apple, set=fab, size=3x]

#### [iOS](ios/index.html)

Integrate iOS apps with PingOne Protect DaVinci flows

[icon: js, set=fab, size=3x]

#### [JavaScript](javascript/index.html)

Integrate JavaScript apps with PingOne Protect DaVinci flows

[icon: react, set=fab, size=3x]

#### [React Native](react-native/index.html)

Integrate React Native apps with PingOne Protect DaVinci flows

---

---
title: Configuring social sign-on in PingOne
description: Configure PingOne with external identity providers and set up DaVinci flows for social sign-on before building your client apps
component: orchsdks
page_id: orchsdks:davinci:use-cases/external-idp/before-you-begin
canonical_url: https://developer.pingidentity.com/orchsdks/davinci/use-cases/external-idp/before-you-begin.html
llms_txt: https://developer.pingidentity.com/orchsdks/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: Thu, 24 Apr 2025 14:44:20 +0100
keywords: ["DaVinci", "Flows", "Tutorial", "Source Code", "Integration", "SDK", "JavaScript"]
section_ids:
  compatibility: Compatibility
  overview: Overview
  connecting_external_identity_providers_in_pingone: Connecting external identity providers in PingOne
  configuring_facebook_login_mode_in_pingone: Configuring Facebook Login mode in PingOne
  configuring_davinci_flows_for_social_sign_on: Configuring DaVinci Flows for social sign-on
  idp-in-dv-flow-forms: Option A. Configuring DaVinci Forms for social sign-on
  creating_a_davinci_form: Creating a DaVinci Form
  forms_redirect: Adding a form to a DaVinci flow
  ipd-in-dv-flow-http-connector: "Option B: Configuring the HTTP Connector for social sign-on"
  adding_the_http_connector_to_a_davinci_flow: Adding the HTTP Connector to a DaVinci flow
  custom_html_redirect: Building a custom HTML sign-on page
  launch-davinci-sdks: Configuring a DaVinci flow to be launched by the Orchestration SDKs
  next_steps: Next Steps
---

# Configuring social sign-on in PingOne

[icon: circle-check, set=far]PingOne [icon: android, set=fab]Android [icon: apple, set=fab]iOS [icon: js, set=fab]JavaScript [icon: react, set=fab]React Native

In this section, you set your identity providers (IdP) to work with your apps through PingOne and DaVinci flows.

## Compatibility

* PingOne

  * Your PingOne instance must have DaVinci enabled.

  * Only **PingOne External IdPs** are supported.

    * Identity providers configured using a **DaVinci Service Connector** are not supported.

## Overview

The high-level tasks you'll complete in this section configure PingOne to perform social sign-on, and allow the DaVinci Client to step through the configured flows.

The **External IdP** module defaults to using a browser redirect method when encountering social sign-on nodes. This mode is the simplest to configure, and supports all of the IdPs that PingOne itself supports.

In this mode PingOne interacts with the IdP to authenticate users on your app's behalf, and then redirects back to your app to continue the flow. This makes the overall configuration simpler, as your app only communicates with PingOne, not individual IdPs.

Optionally, you can choose to use the embedded SDKs of supported IdPs for Android and iOS apps. In this mode your app communicates directly with the supported IdP by using their own SDK. This requires additional configuration in the IdP and in your client application. These additional steps are covered in a later step for each platform.

## Connecting external identity providers in PingOne

In this section, you configure PingOne with details about the social login identity providers you want to integrate into your client apps.

The Orchestration SDKs are compatible with any OpenID Connect 1.0-compliant Identity Provider, such as those available by default in PingOne.

|   |                                                                                                                                                                                                                                              |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | You must configure the identity provider as a [**PingOne External IdP**](https://docs.pingidentity.com/pingone/integrations/p1_external_idps.html).Identity providers configured by using a **DaVinci Service Connector** are not supported. |

Ping Identity has tested the steps in this tutorial with the Identity Providers listed below. Select a provider to view the PingOne documentation with instructions on how to configure an external IdP in PingOne:

[icon: apple, set=fab, size=3x]

#### [Apple](https://docs.pingidentity.com/pingone/integrations/p1_add_idp_apple_prereqs.html)

Adding an identity provider - Apple

[icon: facebook, set=fab, size=3x]

#### [Facebook](https://docs.pingidentity.com/pingone/integrations/p1_addidentityproviderfacebook.html)

Adding an identity provider - Facebook

[icon: google, set=fab, size=3x]

#### [Google](https://docs.pingidentity.com/pingone/integrations/p1_addidentityprovidergoogle.html)

Adding an identity provider - Google

### Configuring Facebook Login mode in PingOne

Meta offers two different login modes for authenticating:

* Classic login

  Allows Tracking and returns an OAuth access token.

  Requires that the user grants the **App Tracking Transparency (ATT)** permission in iOS.

* Limited Login

  Prevents access to your Facebook friends, photos, and pages is disabled to prevent cross-app tracking.

  Limited Login uses an OIDC flow and returns an ID token.

To select the mode to use, when adding Facebook as an external IdP in PingOne, configure the **Login Mode** to use:

![pingone external idp facebook limited login](../../_images/pingone-external-idp-facebook-limited-login.png)

If you have already added Facebook as an external IdP in PingOne, you can edit the **Login Mode** as follows:

1. In the PingOne admin console, go to **Integrations** > **External IdPs** and browse or search for the Facebook IdP you want to edit.

2. Click the IdP to open its details panel.

3. On the **Connection** tab, click the **Pencil** icon ([icon: pencil, set=fas]).

4. Change the **Login Mode** as required.

5. Save your changes.

Learn more in [Limited Login for iOS](https://developers.facebook.com/documentation/facebook-login/ios/limited-login/ios) in the *Facebook Login* documentation.

## Configuring DaVinci Flows for social sign-on

After connecting your chosen external identity providers to PingOne, the next step is to configure a DaVinci flow to display buttons on your login pages so that users can choose to authenticate using the external IdP.

![An Android app with three external IdP options; Apple, Facebook, and Google.](../../_images/social-sign-on-example.png)Figure 1. An Android app with three external IdP options: Apple, Facebook, and Google.

The Orchestration SDKs support two options for adding social sign-on to your DaVinci flows. Choose *one* of the following options:

[icon: pen-field, set=far, size=3x]

#### [DaVinci Forms](#idp-in-dv-flow-forms)

DaVinci Forms is a drag-and-drop form builder that allows you to create custom forms without having to write HTML.

[icon: code, set=far, size=3x]

#### [HTTP Connector](#ipd-in-dv-flow-http-connector)

This powerful and versatile connector lets you show custom HTML pages in your DaVinci orchestration flows.

### Option A. Configuring DaVinci Forms for social sign-on

DaVinci Forms is a drag-and-drop form builder that allows you to create custom forms without having to write HTML.

|   |                                                                                                                                                      |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | You do not need to configure a form if you have chosen [Option B: Configuring the HTTP Connector for social sign-on](#ipd-in-dv-flow-http-connector) |

Complete the following steps to integrate external IdPs with PingOne using DaVinci Forms.

#### Creating a DaVinci Form

1. [Create a form](https://docs.pingidentity.com/pingone/user_experience/p1_creating_form.html) to display your selected external identity providers.

   |   |                                                                                                                                                                               |
   | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | PingOne includes a number of prebuilt templates that you can modify as required.![Out-of-the-box DaVinci Forms templates.](../../_images/davinci-forms-templates-sign-on.png) |

2. To add external identity providers to the form:

   1. From the **Toolbox** tab, drag a **[icon: exit_to_app, set=material, size=inline] Social Login** field onto the form for each external identity provider you want to display.

   2. In **PingOne External Identity Provider**, select the external IdP you created earlier. For example, Google.

      ![Configuring a Social Login field to use Google as the external IdP.](../../_images/davinci-form-sign-in-with-google-field.png)Figure 2. Configuring a Social Login field to use Google as the external IdP.

3. Save your changes.

Learn more in [Creating a form](https://docs.pingidentity.com/pingone/user_experience/p1_creating_form.html) in the PingOne documentation.

#### Adding a form to a DaVinci flow

When you have added your external identity providers to your form, you must now include it as part of your DaVinci flow.

1. Add the form you created for external IdPs to a flow by using the [PingOne Forms connector](https://docs.pingidentity.com/connectors/forms_connector.html).

   ![Example of a Forms Connector in a DaVinci flow.](../../_images/davinci-form-connector.png)Figure 3. Example of a Forms Connector in a DaVinci flow.

2. Select the PingOne Forms connector you just added, click the **General** tab, and in **Application Return URL**, enter the URL to redirect the user to after authentication with the external IdP:

   * JavaScript client apps

     Enter the URL where you are hosting your JavaScript application.

     For example, `https://sdkapp.example.com:8443`

   * Mobile apps

     Enter a custom URI scheme for redirecting users to your client app after social sign-on.

     For example, `myapp://example.com`

     You will need to configure your apps to respond to this URL in a later step.

     * Android

       [Step 2. Handling URI schemes](android/02_handling_uri_schemes.html)

     * iOS

       [Step 2. Handling URI schemes](ios/02_handling_uri_schemes.html)

     * React Native

       [Step 2. Handling URI schemes](react-native/02_handling_uri_schemes.html)

   The result will resemble the following

   ![Configuring a return URL in the PingOne Form Connector.](../../_images/davinci-form-connector-redirect-uri.png)Figure 4. Configuring a return URL in the PingOne Form Connector.

3. Apply your changes.

You can now proceed to [Configuring a DaVinci flow to be launched by the Orchestration SDKs](#launch-davinci-sdks).

### Option B: Configuring the HTTP Connector for social sign-on

This powerful and versatile connector lets you show custom HTML pages in your DaVinci orchestration flows.

|   |                                                                                                                                                    |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | You do not need to configure the HTTP Connector if you have chosen [Option A. Configuring DaVinci Forms for social sign-on](#idp-in-dv-flow-forms) |

Complete the following steps to integrate external IdPs with PingOne by adding the HTTP Connector to a DaVinci flow.

#### Adding the HTTP Connector to a DaVinci flow

1. You must add the **HTTP** connector to your DaVinci flow so that it can display your custom HTML sign-on page.

   ![An HTTP connector added to a DaVinci flow.](../../_images/davinci-http-connector-in-dv-flow.png)Figure 5. An HTTP connector added to a DaVinci flow.

   To learn more, refer to [Adding a connector](https://docs.pingidentity.com/davinci/connectors/davinci_adding_a_connector.html).

#### Building a custom HTML sign-on page

With the HTTP Collector in place in the flow, you can now add custom HTML to display the sign-on page.

1. Select the HTTP Connector you added to your DaVinci flow, and add custom HTML to display a sign-on form.

   ![Example custom HTML form in an HTTP connector.](../../_images/davinci-http-connector-code.png)Figure 6. Example custom HTML form in an HTTP connector.

   To learn more about adding custom HTML, refer to [Building a custom page](https://docs.pingidentity.com/connectors/http_connector.html#building-a-custom-page).

2. Add an **[skIdP](https://docs.pingidentity.com/davinci/flows/davinci_sk_components.html#skidp)** component to your custom HTML for each external IdP option you want to display.

   ![An HTTP connector with custom HTML showing 3 skIdP components.](../../_images/davinci-http-connector-with-skidp.png)Figure 7. An HTTP connector with custom HTML showing three skIdP components.

   To learn more, refer to [Adding SK-Components to a connector](https://docs.pingidentity.com/davinci/flows/davinci_adding_sk_components.html).

3. Configure the **skIdP** component to use an external IdP:

   1. In the **HTML Template** field, select an **skIdP** component to view the **Update Component** modal.

   2. Select the **Identity Provider** tab.

   3. In **Identity Provider Connector**, select `PingOne Authentication`.

   4. In **PingOne External Identity Provider**, select one of the external IdPs you configured earlier.

   5. Enable **Link with PingOne User**.

      Failure to enable this option causes errors when attempting to use the flow with the Orchestration SDKs.

   6. In **Application Return to Url**, enter the URL to redirect the user to after authentication with the external IdP:

      * JavaScript client apps

        Enter the URL where you are hosting your JavaScript application.

        For example, `https://sdkapp.example.com:8443`

      * Mobile apps

        Enter a custom URI scheme for redirecting users to your client app after social sign-on.

        For example, `myapp://example.com`

        You will need to configure your apps to respond to this URL in a later step.

        * Android

          [Step 2. Handling URI schemes](android/02_handling_uri_schemes.html)

        * iOS

          [Step 2. Handling URI schemes](ios/02_handling_uri_schemes.html)

        * React Native

          [Step 2. Handling URI schemes](react-native/02_handling_uri_schemes.html)

      The result will resemble the following:

      ![Configuring an skIdP component in an HTTP connector.](../../_images/davinci-http-connector-skidp-config.png)Figure 8. Configuring an skIdP component in an HTTP connector.

4. Save your changes.

For Facebook Limited Login, the `skIdP` component produces the same `IdpCollector` used by the Forms path. The iOS application selects the mode by setting `facebookLimitedLoginEnabled`; changing the HTML button does not change the token type. In classic mode, the SDK sends an `accessToken`. In Limited mode, it sends an `idToken`.

Ensure that the PingOne Facebook connector has the `p14c-72745-facebook-limited-login` capability enabled and can accept and validate the OIDC ID token before enabling Limited Login in the iOS application.

You can now proceed to [Configuring a DaVinci flow to be launched by the Orchestration SDKs](#launch-davinci-sdks).

## Configuring a DaVinci flow to be launched by the Orchestration SDKs

Now that your DaVinci flow is configured to display your selected external IdPs you must configure PingOne so that you can launch the flow by using the Orchestration SDKs.

This involves performing the following high-level steps:

* Checking that your DaVinci flow uses only [compatible connectors and fields](../../compatibility.html).

* Creating an application in DaVinci to connect PingOne to the DaVinci flow.

* Creating an application in PingOne that the Orchestration SDKs can connect to and access the DaVinci application and its PingOne Flow Policy.

Complete the steps in [Launching a flow with a Ping SDK](https://docs.pingidentity.com/davinci/integrating_flows_into_applications/davinci_sdk_launching_a_flow_with_the_sdk.html) in the DaVinci documentation.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Configuring redirects to JavaScript client appsIf you are developing a JavaScript client application you must configure the application you create in PingOne to redirect users back to your app after authentication.In the application you created in PingOne, configure the **Redirect URIs** field on the **Configuration** tab with the URL of your JavaScript client app.![Configuring redirect URIs in PingOne.](../../_images/pingone-app-javascript-redirect.png)Figure 9. Configuring redirect URIs in PingOneWe recommend your app has a dedicated route to handle users returning from an external IdP.For example, `https://example.com/login/resume`.This helps to prevent redirect loops in your apps, and makes handling social sign-on simpler. |

## Next Steps

In this section you completed the following tasks:

* Added client credentials in your IdPs so that your app and server can connect

* Configured PingOne with the details of the client credentials you created in the IdPs

* Added relevant IdP nodes to a DaVinci flow

  * If you are developing a mobile app, you added redirect URI values to the flow to return users after authentication.

* Created an application in PingOne so that the Orchestration SDKs can connect

  * If you are developing a JavaScript app, you added redirect URI values to this application to return users after authentication.

You can now proceed to configuring your client apps to step through the DaVinci flows and perform social sign-on:

[icon: android, set=fab, size=3x]

#### [Android](android/index.html)

Configure an Android app for social sign-on

[icon: apple, set=fab, size=3x]

#### [iOS](ios/index.html)

Configure an iOS app for social sign-on

[icon: js, set=fab, size=3x]

#### [JavaScript](javascript/index.html)

Configure a JavaScript app for social sign-on

[icon: react, set=fab, size=3x]

#### [React Native](react-native/index.html)

Configure a React Native app for social sign-on

---

---
title: Configuring the DaVinci module
description: Explains how to configure the DaVinci module for Android by setting properties to connect to PingOne and step through a DaVinci flow.
component: orchsdks
page_id: orchsdks:davinci:usage/android/02-configuring-the-davinci-module
canonical_url: https://developer.pingidentity.com/orchsdks/davinci/usage/android/02-configuring-the-davinci-module.html
llms_txt: https://developer.pingidentity.com/orchsdks/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: Fri, 9 Jan 2026 17:23:51 +0000
keywords: ["DaVinci", "Android", "Configuration", "Properties", "PingOne", "Integration"]
section_ids:
  full-configuration: Full configuration
  common-json-configuration: Common JSON configuration
  configuration_property_reference: Configuration property reference
---

# Configuring the DaVinci module

[icon: circle-check, set=far]PingOne [icon: android, set=fab]Android

* [Install](01-installing-the-davinci-module.html)

* **Configure**

* [Navigate](03-stepping-through-davinci-flows.html)

Configure DaVinci module for Android properties to connect to PingOne and step through an associated DaVinci flow.

There are two methods for configuring the DaVinci module:

* [Full configuration](#full-configuration)

  Use the Kotlin builder DSL to access all available settings, including Android-specific options such as custom HTTP clients and storage configuration.

* [Common JSON configuration](#common-json-configuration)

  Use a shared key-value structure that works identically across Android, iOS, and JavaScript, letting you load a single config file across platforms.

## Full configuration

The following shows an example DaVinci module configuration, using the underlying `Oidc` module:

Configure DaVinci module connection properties

```kotlin
import com.pingidentity.davinci.DaVinci
import com.pingidentity.davinci.module.Oidc

val davinciClient = DaVinci {
    logger = Logger.STANDARD
    module(Oidc) {
        clientId = "6c7eb89a-66e9-ab12-cd34-eeaf795650b2"
        discoveryEndpoint = "https://auth.pingone.com/3072206d-c6ce-ch15-m0nd-f87e972c7cc3/" +
            "as/.well-known/openid-configuration"
        scopes = mutableSetOf("openid", "profile", "email", "address", "revoke")
        redirectUri = "com.example.demo://oauth2redirect"
        par = true
        additionalParameters = mapOf("customKey" to "customValue")
    }
}
```

## Common JSON configuration

You can provide the same configuration as a JSON object, which lets you share a single config file across Android, iOS, and JavaScript.

Configure the `DaVinci` module from a JSON object

```kotlin
val davinciClient = DaVinci(buildJsonObject {
    put("timeout", 30000) // milliseconds
    put("log", "WARN")
    putJsonObject("oidc") {
        put("clientId", "6c7eb89a-66e9-ab12-cd34-eeaf795650b2")
        put("discoveryEndpoint",
            "https://auth.pingone.com/3072206d-c6ce-ch15-m0nd-f87e972c7cc3/as/.well-known/openid-configuration")
        putJsonArray("scopes") {
            add("openid"); add("profile"); add("email"); add("revoke")
        }
        put("redirectUri", "com.example.demo://oauth2redirect")
    }
}).getOrThrow()
```

Optionally, you can store this JSON in a file alongside your app and load it at runtime so the same file can be shared across platforms.

|   |                                                                                                                                                                                                                                                                  |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The JSON factory and the native `DaVinci {}` builder DSL are mutually exclusive, there is no combined form.If you need Android-specific settings such as `httpClient` or storage configuration, use the native builder DSL for the entire configuration instead. |

## Configuration property reference

The following properties are available when configuring the DaVinci module for Android.

The **JSON property** column shows the equivalent key when using JSON configuration.

**DaVinci module configuration properties for Android**

| Property               | JSON property               | Description                                                                                                                                                                                                                                                                                                                                                                                              | Required? |
| ---------------------- | --------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------- |
| `logger`               | `log`                       | Specify which logger the Orchestration SDK should use to output messages. Select from the built-in presets `STANDARD` (the default), `WARN`, or `NONE`.You can also create and use your own logger implementation. Learn more in [Customizing logging on Android](../../customization/logging/android-custom-logging.html).In JSON configuration, use the `log` property at the root level.              | No        |
| `timeout`              | `timeout`                   | A timeout, in seconds, for each request that communicates with the server.Default is `30` seconds.When using JSON configuration, specify `timeout` at the root level with the value in milliseconds:```json
{
  "timeout": 30000
}
```                                                                                                                                                                   | No        |
| `acrValues`            | `oidc.acrValues`            | Request which flow the PingOne server uses by adding an Authentication Context Class Reference (ACR) parameter.Enter a single DaVinci policy by using its flow policy ID.Example:`"d1210a6b0b2665dbaa5b652221badba2"`                                                                                                                                                                                    | No        |
| `additionalParameters` | `oidc.additionalParameters` | Add additional key-pair parameters as query strings to the initial OAuth 2.0 call to the `/authorize` endpoint.For example, `additionalParameters = mapOf("customKey" to "customValue")`&#xA;&#xA;You can access these additional OAuth 2.0 parameters in your DaVinci flows by using the authorizationRequest.\<customParameter> property.&#xA;&#xA;Learn more in Referencing PingOne data in the flow. | No        |
| `clientId`             | `oidc.clientId`             | The `client_id` of the OAuth 2.0 client profile to use.For example, `6c7eb89a-66e9-ab12-cd34-eeaf795650b2`                                                                                                                                                                                                                                                                                               | Yes       |
| `discoveryEndpoint`    | `oidc.discoveryEndpoint`    | Your PingOne server's `.well-known/openid-configuration` endpoint.*Example*:`https://auth.pingone.com/3072206d-c6ce-ch15-m0nd-f87e972c7cc3/as/.well-known/openid-configuration`                                                                                                                                                                                                                          | Yes       |
| `par`                  | `oidc.par`                  | Whether to use Pushed Authorization Requests (PAR) for communicating with the authorization server.Learn more in [Securing OIDC sign-on with Pushed Authorization Requests](../../../oidc/use-cases/par/index.html).                                                                                                                                                                                     | No        |
| `redirectUri`          | `oidc.redirectUri`          | The `redirect_uri` as configured in the OAuth 2.0 client profile.	This value must match a value configured in your OAuth 2.0 client.For example, `com.example.demo://oauth2redirect`.                                                                                                                                                                                                                    | Yes       |
| `scopes`               | `oidc.scopes`               | A set of scopes to request when performing an OAuth 2.0 authorization flow\.For example, `"openid", "profile", "email", "address", "revoke"`.                                                                                                                                                                                                                                                            | Yes       |
| `display`              | `oidc.display`              | How the authorization server should display the authentication UI.- `page`

  Full-page redirect (default).

- `popup`

  Pop-up window.

- `touch`

  Optimized for touch-based devices.

- `wap`

  Optimized for WAP/mobile browsers.                                                                                                                                                                 | No        |
| `loginHint`            | `oidc.loginHint`            | A hint to pre-populate the username field on the authorization server's sign-on page.For example, `user@example.com`                                                                                                                                                                                                                                                                                     | No        |
| `nonce`                | `oidc.nonce`                | A value to associate with the ID token to prevent replay attacks.If not set, the SDK generates a nonce automatically.                                                                                                                                                                                                                                                                                    | No        |
| `prompt`               | `oidc.prompt`               | Controls whether the authorization server prompts the user for re-authentication or consent.Select one of the following:- `none`

  No UI; returns an error if interaction is required.

- `login`

  Force re-authentication.

- `consent`

  Request consent even if previously granted.

- `select_account`

  Prompt to select an account.                                                           | No        |
| `refreshThreshold`     | `oidc.refreshThreshold`     | The number of seconds before token expiry at which the SDK proactively refreshes the token.Defaults to `0`, meaning the SDK refreshes only when the token has expired.                                                                                                                                                                                                                                   | No        |
| `signOutRedirectUri`   | `oidc.signOutRedirectUri`   | The URI to redirect to after sign-out.Maps to the `post_logout_redirect_uri` parameter in the end-session request.This value must be registered in your OAuth 2.0 client.                                                                                                                                                                                                                                | No        |
| `uiLocales`            | `oidc.uiLocales`            | Space-separated BCP 47 language tags indicating the preferred display language for the authorization server's UI.For example, `en-US fr`                                                                                                                                                                                                                                                                 | No        |

---

---
title: Configuring the DaVinci module
description: Explains how to configure the DaVinci module for iOS by setting properties to connect to PingOne and step through a DaVinci flow.
component: orchsdks
page_id: orchsdks:davinci:usage/ios/02-configuring-the-davinci-module
canonical_url: https://developer.pingidentity.com/orchsdks/davinci/usage/ios/02-configuring-the-davinci-module.html
llms_txt: https://developer.pingidentity.com/orchsdks/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: Fri, 9 Jan 2026 17:23:51 +0000
keywords: ["DaVinci", "iOS", "Configuration", "Properties", "PingOne", "Integration"]
section_ids:
  full-configuration: Full configuration
  common-json-configuration: Common JSON configuration
  configuration_property_reference: Configuration property reference
---

# Configuring the DaVinci module

[icon: circle-check, set=far]PingOne [icon: apple, set=fab]iOS

* [Install](01-installing-the-davinci-module.html)

* **Configure**

* [Navigate](03-stepping-through-davinci-flows.html)

Configure DaVinci module for iOS properties to connect to PingOne and step through an associated DaVinci flow.

There are two methods for configuring the DaVinci module:

* [Full configuration](#full-configuration)

  Use the Swift builder closure to access all available settings, including iOS-specific options such as keychain access groups, custom HTTP clients, and storage configuration.

* [Common JSON configuration](#common-json-configuration)

  Use a shared key-value structure that works identically across Android, iOS, and JavaScript, letting you load a single config file across platforms.

## Full configuration

The following shows an example DaVinci module configuration, using the underlying `Oidc` module:

Configure DaVinci module connection properties

```swift
let davinciClient = DaVinci.createDaVinci { config in
    config.logger = LogManager.standard
    // Oidc as module
    config.module(OidcModule.config) { oidcValue in
        oidcValue.clientId = "6c7eb89a-66e9-ab12-cd34-eeaf795650b2"
        oidcValue.discoveryEndpoint = "https://auth.pingone.com/3072206d-c6ce-ch15-m0nd-f87e972c7cc3/as/.well-known/openid-configuration"
        oidcValue.scopes = ["openid", "profile", "email", "address", "revoke"]
        oidcValue.redirectUri = "com.example.demo://oauth2redirect"
        oidcValue.par = true
        oidcValue.additionalParameters = ["customKey":"customValue"]
    }
}
```

## Common JSON configuration

You can provide the same configuration as a JSON-compatible dictionary, which lets you share a single config file across Android, iOS, and JavaScript.

Configure the `DaVinci` module from a JSON dictionary

```swift
let json: [String: Any] = [
    "timeout": 30000, // milliseconds
    "log": "WARN",
    "oidc": [
        "clientId": "6c7eb89a-66e9-ab12-cd34-eeaf795650b2",
        "discoveryEndpoint":
            "https://auth.pingone.com/3072206d-c6ce-ch15-m0nd-f87e972c7cc3/as/.well-known/openid-configuration",
        "scopes": ["openid", "profile", "email", "revoke"],
        "redirectUri": "com.example.demo://oauth2redirect"
    ]
]

switch DaVinci.createDaVinci(json: json) {
case .success(let davinciClient):
    // use davinciClient
case .failure(let error):
    // handle configuration error
}
```

Optionally, you can store this JSON in a file alongside your app and load it at runtime so the same file can be shared across platforms.

|   |                                                                                                                                                                                                                                                                                                              |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | The JSON factory and the native `DaVinci.createDaVinci { }` builder closure are mutually exclusive, there is no combined form.If you need iOS-specific settings such as keychain access groups, `httpClient`, or storage configuration, use the native builder closure for the entire configuration instead. |

## Configuration property reference

The following properties are available when configuring the DaVinci module for iOS.

The **JSON property** column shows the equivalent key when using JSON configuration.

**DaVinci module configuration properties for iOS**

| Property               | JSON property               | Description                                                                                                                                                                                                                                                                                                                                                                                               | Required? |
| ---------------------- | --------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------- |
| `logger`               | `log`                       | Specify which logger the Orchestration SDK should use to output messages. Select from the built-in presets `standard` (the default), `warning`, or `none`.You can also create and use your own logger implementation. Learn more in [Customizing logging on iOS](../../customization/logging/ios-custom-logging.html).In JSON configuration, use the `log` property at the root level.                    | No        |
| `timeout`              | `timeout`                   | A timeout, in seconds, for each request that communicates with the server.Default is `30` seconds.When using JSON configuration, specify `timeout` at the root level with the value in milliseconds:```json
{
  "timeout": 30000
}
```                                                                                                                                                                    | No        |
| `acrValues`            | `oidc.acrValues`            | Request which flow the PingOne server uses by adding an Authentication Context Class Reference (ACR) parameter.Enter a single DaVinci policy by using its flow policy ID.Example:`"d1210a6b0b2665dbaa5b652221badba2"`                                                                                                                                                                                     | No        |
| `additionalParameters` | `oidc.additionalParameters` | Add additional key-pair parameters as query strings to the initial OAuth 2.0 call to the `/authorize` endpoint.For example, `myConfig.additionalParameters = ["customKey":"customValue"]`&#xA;&#xA;You can access these additional OAuth 2.0 parameters in your DaVinci flows by using the authorizationRequest.\<customParameter> property.&#xA;&#xA;Learn more in Referencing PingOne data in the flow. | No        |
| `clientId`             | `oidc.clientId`             | The `client_id` of the OAuth 2.0 client profile to use.For example, `6c7eb89a-66e9-ab12-cd34-eeaf795650b2`                                                                                                                                                                                                                                                                                                | Yes       |
| `discoveryEndpoint`    | `oidc.discoveryEndpoint`    | Your PingOne server's `.well-known/openid-configuration` endpoint.*Example*:`https://auth.pingone.com/3072206d-c6ce-ch15-m0nd-f87e972c7cc3/as/.well-known/openid-configuration`                                                                                                                                                                                                                           | Yes       |
| `par`                  | `oidc.par`                  | Whether to use Pushed Authorization Requests (PAR) for communicating with the authorization server.Learn more in [Securing OIDC sign-on with Pushed Authorization Requests](../../../oidc/use-cases/par/index.html).                                                                                                                                                                                      | No        |
| `redirectUri`          | `oidc.redirectUri`          | The `redirect_uri` as configured in the OAuth 2.0 client profile.	This value must match a value configured in your OAuth 2.0 client.For example, `com.example.demo://oauth2redirect`.                                                                                                                                                                                                                     | Yes       |
| `scopes`               | `oidc.scopes`               | A set of scopes to request when performing an OAuth 2.0 authorization flow\.For example, `"openid", "profile", "email", "address", "revoke"`.                                                                                                                                                                                                                                                             | Yes       |
| `display`              | `oidc.display`              | How the authorization server should display the authentication UI.- `page`

  Full-page redirect (default).

- `popup`

  Pop-up window.

- `touch`

  Optimized for touch-based devices.

- `wap`

  Optimized for WAP/mobile browsers.                                                                                                                                                                  | No        |
| `loginHint`            | `oidc.loginHint`            | A hint to pre-populate the username field on the authorization server's sign-on page.For example, `user@example.com`                                                                                                                                                                                                                                                                                      | No        |
| `nonce`                | `oidc.nonce`                | A value to associate with the ID token to prevent replay attacks.If not set, the SDK generates a nonce automatically.                                                                                                                                                                                                                                                                                     | No        |
| `prompt`               | `oidc.prompt`               | Controls whether the authorization server prompts the user for re-authentication or consent.Select one of the following:- `none`

  No UI; returns an error if interaction is required.

- `login`

  Force re-authentication.

- `consent`

  Request consent even if previously granted.

- `select_account`

  Prompt to select an account.                                                            | No        |
| `refreshThreshold`     | `oidc.refreshThreshold`     | The number of seconds before token expiry at which the SDK proactively refreshes the token.Defaults to `0`, meaning the SDK refreshes only when the token has expired.                                                                                                                                                                                                                                    | No        |
| `signOutRedirectUri`   | `oidc.signOutRedirectUri`   | The URI to redirect to after sign-out.Maps to the `post_logout_redirect_uri` parameter in the end-session request.This value must be registered in your OAuth 2.0 client.                                                                                                                                                                                                                                 | No        |
| `uiLocales`            | `oidc.uiLocales`            | Space-separated BCP 47 language tags indicating the preferred display language for the authorization server's UI.For example, `en-US fr`                                                                                                                                                                                                                                                                  | No        |

---

---
title: Configuring the DaVinci module
description: Explains how to configure the DaVinci module for JavaScript by setting properties to connect to PingOne and step through a DaVinci flow.
component: orchsdks
page_id: orchsdks:davinci:usage/javascript/02-configuring-the-davinci-module
canonical_url: https://developer.pingidentity.com/orchsdks/davinci/usage/javascript/02-configuring-the-davinci-module.html
llms_txt: https://developer.pingidentity.com/orchsdks/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: Fri, 9 Jan 2026 17:23:51 +0000
keywords: ["DaVinci", "JavaScript", "Configuration", "Properties", "PingOne", "Integration"]
section_ids:
  full-configuration: Full configuration
  common-json-configuration: Common JSON configuration
  configuration_property_reference: Configuration property reference
---

# Configuring the DaVinci module

[icon: circle-check, set=far]PingOne [icon: js, set=fab]JavaScript

* [Install](01-installing-the-davinci-module.html)

* **Configure**

* [Navigate](03-stepping-through-davinci-flows.html)

Configure DaVinci module for JavaScript properties to connect to PingOne and step through an associated DaVinci flow.

There are two methods for configuring the DaVinci module:

* [Full configuration](#full-configuration)

  Use the JavaScript factory function to access all available settings, including JavaScript-specific options such as request middleware and custom loggers.

* [Common JSON configuration](#common-json-configuration)

  Use a shared key-value structure that works identically across Android, iOS, and JavaScript, letting you load a single config file across platforms.

## Full configuration

The following shows a full DaVinci module configuration:

Configure DaVinci module connection properties

```javascript
import { davinci } from '@forgerock/davinci-client';

const davinciClient = await davinci({
  logger: {
    level: 'warn',
    custom: customLogger,
  },
  config: {
    clientId: '6c7eb89a-66e9-ab12-cd34-eeaf795650b2',
    redirectUri: 'https://localhost:8443/callback',
    serverConfig: {
      wellknown: 'https://auth.pingone.com/3072206d-c6ce-ch15-m0nd-f87e972c7cc3/as/.well-known/openid-configuration',
      timeout: 3000,
    },
    scope: 'openid profile email phone',
    responseType: 'code',
  },
});
```

## Common JSON configuration

You can provide the same configuration as a JSON object, which lets you share a single config file across Android, iOS, and JavaScript.

Use the `makeDavinciConfig()` helper from `@forgerock/sdk-utilities` to convert the JSON to native config, then pass it to `davinci()`:

Configure the `DaVinci` module from a JSON object

```javascript
import { davinci } from '@forgerock/davinci-client';
import { makeDavinciConfig } from '@forgerock/sdk-utilities';

const unifiedConfig = {
    timeout: 30000, // milliseconds
    log: 'WARN',
    oidc: {
        clientId: '6c7eb89a-66e9-ab12-cd34-eeaf795650b2',
        discoveryEndpoint:
            'https://auth.pingone.com/3072206d-c6ce-ch15-m0nd-f87e972c7cc3/as/.well-known/openid-configuration',
        scopes: ['openid', 'profile', 'email', 'revoke'],
        redirectUri: 'https://localhost:8443/callback',
    },
};

const davinciClient = await davinci({
    config: makeDavinciConfig(unifiedConfig),
});
```

Because `makeDavinciConfig()` returns a standard native config object, you can combine it with JavaScript-specific options in the same `davinci()` call:

Combining JSON config with JavaScript-specific options

```javascript
const davinciClient = await davinci({
    config: makeDavinciConfig(unifiedConfig),
    logger: { level: 'debug', custom: myCustomLogger },
    requestMiddleware: [customHeaderMiddleware],
});
```

The `makeDavinciConfig()` helper maps JSON properties to the native config automatically:

* `oidc.discoveryEndpoint` → `config.serverConfig.wellknown`

* `oidc.scopes` (array) → `config.scope` (space-separated string)

* `timeout` → `config.serverConfig.timeout`

Optionally, you can store the JSON in a file alongside your app and load it at runtime so the same file can be shared across platforms.

## Configuration property reference

The following properties are available when configuring the DaVinci module for JavaScript.

The **JSON property** column shows the equivalent key when using JSON configuration.

1. [Properties of the `config{}` object](#config-props)

2. [Properties of the `logger{}` object](#logger-props)

**config{} Properties**

| Property                    | JSON property            | Description                                                                                                                                                                                                                                                                         | Required? |
| --------------------------- | ------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------- |
| `serverConfig: {timeout}`   | `timeout`                | A timeout, in milliseconds, for each request that communicates with your server.For example, for 30 seconds specify `30000`.Defaults to `5000` (5 seconds).When using JSON configuration, specify `timeout` at the root level.                                                      | No        |
| `serverConfig: {wellknown}` | `oidc.discoveryEndpoint` | Your PingOne server's `.well-known/openid-configuration` endpoint.*Example*:`https://auth.pingone.com/3072206d-c6ce-ch15-m0nd-f87e972c7cc3/as/.well-known/openid-configuration`                                                                                                     | Yes       |
| `clientId`                  | `oidc.clientId`          | The `client_id` of the OAuth 2.0 client profile to use.For example, `6c7eb89a-66e9-ab12-cd34-eeaf795650b2`                                                                                                                                                                          | Yes       |
| `redirectUri`               | `oidc.redirectUri`       | The `redirect_uri` as configured in the OAuth 2.0 client profile.	This value must match a value configured in your OAuth 2.0 client.For example, `https://localhost:8443/callback`.                                                                                                 | Yes       |
| `scope`                     | `oidc.scopes`            | A list of scopes to request when performing an OAuth 2.0 authorization flow, separated by spaces.For example, `"openid", "email", "address", "profile", "phone"`.When using JSON configuration, provide scopes as an array. The SDK joins the values into a space-separated string. | Yes       |
| `par`                       | `oidc.par`               | Whether to use Pushed Authorization Requests (PAR) for communicating with the authorization server.Learn more in [Securing OIDC sign-on with Pushed Authorization Requests](../../../oidc/use-cases/par/index.html).                                                                | No        |
| `responseType`              |                          | The type of OAuth 2.0 flow to use, either `code` or `token`.Defaults to `code`.                                                                                                                                                                                                     | No        |

**logger{} Properties**

| Property | JSON property | Description                                                                                                                                                                                                                                                                                                                                                                                                                         | Required? |
| -------- | ------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------- |
| `level`  | `log`         | Specify what level of logging the Orchestration SDK should output.Select one of the following:- `none`

- `error`

- `warn`

- `info` (the default)

- `debug`Learn more in [Configuring JavaScript logging](../../customization/logging/javascript-custom-logging.html#configuring-logging-on-javascript).In JSON configuration, set the `log` property at the root level, with values `NONE`, `ERROR`, `WARN`, `INFO` or `DEBUG`. | No        |
| `custom` |               | Specify a custom logger the Orchestration SDK should use to output messages.Learn more in [Customizing JavaScript logging](../../customization/logging/javascript-custom-logging.html#customize-logger-javascript).Example:`customLogger`                                                                                                                                                                                           | No        |

---

---
title: Configuring the DaVinci module in React Native
description: Configure the DaVinci client in React Native to connect to PingOne and start a flow
component: orchsdks
page_id: orchsdks:davinci:usage/react-native/03-configuring-the-davinci-module
canonical_url: https://developer.pingidentity.com/orchsdks/davinci/usage/react-native/03-configuring-the-davinci-module.html
llms_txt: https://developer.pingidentity.com/orchsdks/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: Thu, 27 Aug 2026 00:00:00 +0000
keywords: ["DaVinci", "React Native", "Configuration", "PingOne", "OIDC"]
section_ids:
  configuring_logging: Configuring logging
---

# Configuring the DaVinci module in React Native

[icon: circle-check, set=far]PingOne [icon: react, set=fab]React Native

* [Prepare](01-configuring-the-server.html)

* [Install](02-installing-the-davinci-module.html)

* **Configure**

* [Start](04-starting-a-davinci-flow.html)

* [Navigate](05-stepping-through-davinci-flows.html)

* [Manage](06-handling-sessions.html)

You must configure a DaVinci client to connect to your PingOne instance.

To configure a client, call `createDaVinciClient()` and provide the OIDC configuration in the `modules` property:

Configuring a DaVinci client

```typescript
import { createDaVinciClient } from '@ping-identity/rn-davinci';

const davinciClient = createDaVinciClient({
  modules: {
    oidc: {
      clientId: '6c7eb89a-66e9-ab12-cd34-eeaf795650b2',
      discoveryEndpoint: 'https://auth.pingone.com/3072206d-c6ce-ch15-m0nd-f87e972c7cc3/as/.well-known/openid-configuration',
      redirectUri: 'org.forgerock.demo://oauth2redirect',
      scopes: ['openid', 'profile', 'email'],
    },
  },
  timeout: 30000,
});
```

Update the following properties with values that match your environment:

* *clientId*

  The client ID from the OAuth 2.0 application you created in PingOne.

  For example, `6c7eb89a-66e9-ab12-cd34-eeaf795650b2`

* *discoveryEndpoint*

  The OIDC discovery endpoint for your PingOne environment.

  For example, `https://auth.pingone.com/3072206d-c6ce-ch15-m0nd-f87e972c7cc3/as/.well-known/openid-configuration`.

* *redirectUri*

  The redirect URI configured in the OAuth 2.0 application.

  This value must exactly match a redirect URI configured in PingOne.

  For example, `org.forgerock.demo://oauth2redirect`

* *scopes*

  The OIDC scopes to request. The example requests the `openid`, `profile`, and `email` scopes.

* *timeout*

  The maximum time, in milliseconds, that the client waits for a response from the server.

  Default is `15000` (15 seconds).

## Configuring logging

If you installed the `@ping-identity/rn-logger` package, create a logger and pass it to the client configuration:

Configuring the DaVinci logger

```typescript
import { logger } from '@ping-identity/rn-logger';

const davinciClient = createDaVinciClient({
  logger: logger({ level: 'debug' }),
  modules: {
    oidc: {
      clientId: '6c7eb89a-66e9-ab12-cd34-eeaf795650b2',
      discoveryEndpoint: 'https://auth.pingone.com/3072206d-c6ce-ch15-m0nd-f87e972c7cc3/as/.well-known/openid-configuration',
      redirectUri: 'org.forgerock.demo://oauth2redirect',
    },
  },
});
```

Pass the `level` parameter to configure the amount of detail the Orchestration SDK outputs. Choose from, `debug`, `info`, `warn`, `error`, or `none`.

---

---
title: Configuring the server for React Native
description: Configure PingOne with the prerequisite tasks required before using the DaVinci module in a React Native app
component: orchsdks
page_id: orchsdks:davinci:usage/react-native/01-configuring-the-server
canonical_url: https://developer.pingidentity.com/orchsdks/davinci/usage/react-native/01-configuring-the-server.html
llms_txt: https://developer.pingidentity.com/orchsdks/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: Thu, 27 Aug 2026 00:00:00 +0000
keywords: ["DaVinci", "React Native", "PingOne", "Server configuration", "Flows"]
section_ids:
  supported_collectors: Supported collectors
---

# Configuring the server for React Native

[icon: circle-check, set=far]PingOne [icon: react, set=fab]React Native

* **Prepare**

* [Install](02-installing-the-davinci-module.html)

* [Configure](03-configuring-the-davinci-module.html)

* [Start](04-starting-a-davinci-flow.html)

* [Navigate](05-stepping-through-davinci-flows.html)

* [Manage](06-handling-sessions.html)

You must configure your PingOne instance for use with the DaVinci module.

Ask your PingOne administrator to complete the following tasks:

* Configure a DaVinci flow

* Create a DaVinci application

* Configure PingOne for DaVinci flow invocation

To learn how to complete these steps, refer to [Launching a flow with a Ping SDK](https://docs.pingidentity.com/davinci/integrating_flows_into_applications/davinci_sdk_launching_a_flow_with_the_sdk.html) in the *PingOne DaVinci documentation*.

## Supported collectors

Your app must handle the collector types that your DaVinci flow returns.

For the current list of supported DaVinci fields and collectors, see [Supported PingOne fields and collectors](../../compatibility.html#supported-davinci-fields).

---

---
title: Customizing DaVinci module storage on Android
description: Configure DaVinci storage on Android using built-in or custom storage solutions, including encrypted DataStore and caching options
component: orchsdks
page_id: orchsdks:davinci:customization/storage/customize-android-storage
canonical_url: https://developer.pingidentity.com/orchsdks/davinci/customization/storage/customize-android-storage.html
llms_txt: https://developer.pingidentity.com/orchsdks/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: Thu, 22 Jan 2026 12:23:51 +0000
section_ids:
  add_dependencies: Add dependencies
  install-protect-android: Adding dependencies
  using_the_provided_storage_solutions: Using the provided storage solutions
  provided_default_storage_solutions: Provided default storage solutions
  configuring_storage_solutions: Configuring storage solutions
  caching: Enabling caching
  implementing_your_own_custom_storage: Implementing your own custom storage
---

# Customizing DaVinci module storage on Android

[icon: circle-check, set=far]PingOne [icon: android, set=fab]Android

Depending on the authentication use case, you may need to store and retrieve ID tokens, access tokens, refresh tokens, or cookies.

Each token is serving a different use case, and as such how you handle them can be different.

The Orchestration SDKs employ identity best practices for storing data by default. However there are use cases where you might need to customize how the SDK stores data.

For example, you might be running on hardware that provides specialized security features, or perhaps target older hardware that cannot handle the latest algorithms.

For these cases, you can customize the provided storage solutions, or provide your own custom storage classes.

## Add dependencies

To customize your storage solution you need to add the `storage` module to your project.

### Adding dependencies

To add the storage module dependencies to your Android project:

1. In the **Project** tree view of your Android Studio project, open the `Gradle Scripts/build.gradle.kts` file for the *module*.

2. In the `dependencies` section, add the required dependencies:

   Example `dependencies` section after editing `build.gradle.kts`:

   ```gradle
   dependencies {
     // DaVinci orchestration module
     implementation("com.pingidentity.sdks:davinci:2.2.0")

     // Storage module
     implementation("com.pingidentity.sdks:storage:2.2.0")
   }
   ```

## Using the provided storage solutions

You can use the default storage solutions and configure them to suit your requirements.

### Provided default storage solutions

You can use the default storage solutions in your apps, depending on the type of data you want to store.

* `MemoryStorage`

  Storage that stores data in memory.

  |   |                                                                                                                                                                                                 |
  | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | Data stored using the `MemoryStorage` solution is kept in plain text and is not encrypted.A device that can output a memory dump may expose sensitive information, such as access or ID tokens. |

* `DataStoreStorage`

  Storage backed by [Jetpack DataStore](https://developer.android.com/topic/libraries/architecture/datastore).

  |   |                                                                                               |
  | - | --------------------------------------------------------------------------------------------- |
  |   | Data stored using the `DataStoreStorage` solution is kept in plain text and is not encrypted. |

* `EncryptedDataStoreStorage`

  Encrypted version of the `DataStoreStorage` solution, also backed by [Jetpack DataStore](https://developer.android.com/topic/libraries/architecture/datastore).

  |   |                                              |
  | - | -------------------------------------------- |
  |   | All SDK modules use this solution by default |

### Configuring storage solutions

You can customize aspects of the storage solutions by passing parameters when creating a storage instance.

On Android, you can configure the `EncryptedDataStoreStorage` storage solution with the following properties:

**Android EncryptedDataStoreStorage properties**

| Property             | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| -------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `cacheStrategy`      | Enable caching of the data.Learn more in [Enabling caching](#caching).- Default value

  `CacheStrategy.NO_CACHE`                                                                                                                                                                                                                                                                                                                                                                                                       |
| `fileName`           | The name of the file used for persistent storage.- Default values

  * OpenID Connect token storage

    `com.pingidentity.sdk.v1.tokens`

  * Cookie storage

    `com.pingidentity.sdk.v1.cookies`                                                                                                                                                                                                                                                                                                                    |
| `keyAlias`           | The string used as the alias for the key. When provided, enables encryption using `AndroidKeyStore`.You can use any value that does not clash with any other key names. A common pattern is `<top-level-domain>.<company-name>.<version>.KEYS`.For example, `com.example.v1.KEYS`.- Default values

  * OpenID Connect token storage

    `com.pingidentity.sdk.v1.tokens`

  * Cookie storage

    `com.pingidentity.sdk.v1.cookies`                                                                                   |
| `strongBoxPreferred` | When `true` the storage module attempts to use hardware-backed [StrongBox](https://developer.android.com/privacy-and-security/keystore#StrongBoxKeyMint) functionality for key storage, if available on the client device.Some devices implement StrongBox, but are not optimal. You can use the [`Build`](https://developer.android.com/reference/android/os/Build) class to conditionally apply the `strongBoxPreferred` flag based on the device manufacturer, model, or other properties.- Default value

  `false` |

The following code shows examples of customizing storage solutions:

Customizing the `EncryptedDataStoreStorage` storage solution

```kotlin
module(Oidc) {
    clientId = "6c7eb89a-66e9-ab12-cd34-eeaf795650b2"
    discoveryEndpoint = "https://auth.pingone.ca/3072206d-c6ce-ch15-m0nd-f87e972c7cc3/as/.well-known/openid-configuration"

    // OpenID Connect storage configuration options
    storage {
        fileName = "myOidcTokens"
        keyAlias = "com.example.v1.KEYS"
        strongBoxPreferred = true
        cacheStrategy = CacheStrategy.CACHE_ON_FAILURE
    }
}
module(Cookie) {
    // The cookie name to persist
    persist = mutableListOf("ST", "ST-NO-SS")
    // Cookie storage configuration options
    storage {
        strongBoxPreferred = false
    }
}
```

#### Enabling caching

You can add caching to each storage solution depending on the requirements of the type of data you store.

|   |                                                                                                                                                                         |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Data stored in a cache is kept in plain text and is not encrypted.A device that can output a memory dump may expose sensitive information, such as access or ID tokens. |

Use the `cacheStrategy` property when creating a storage instance to configure the type of cache the storage uses. The available options are as follows:

* `CacheStrategy.NO_CACHE`

  The default for each storage solution.

  Prevents caching and always fetches data from storage.

  Use for critical data that must always be up-to-date.

* `CacheStrategy.CACHE_ON_FAILURE`

  Caches data in memory if the storage operation fails.

  Use to overcome storage interruptions, and allow fallback data reads.

* `CacheStrategy.CACHE`

  Always caches data in memory.

  Use for non-critical, but highly performant data reads.

  **Example**:

  Creating a storage instance with cache enabled

  ```kotlin
  val storage = DataStoreStorage<String> {
      fileName = "com.pingidentity.sdk.v1.tokens"
      cacheStrategy = CacheStrategy.CACHE
  }
  ```

## Implementing your own custom storage

You can create your own custom storage solutions by implementing the `Storage` interface. For example, you could implement a file-based or cloud-based storage solution.

You must implement the following functions in each storage class:

* `save()`

  Stores an item in the customized storage.

* `get()`

  Retrieves an item from the customized storage.

* `delete()`

  Removes an item from the customized storage.

The `Storage` interface on Android

```kotlin
class Memory<T : @Serializable Any> : Storage<T> {
  private var data: T? = null

  override suspend fun save(item: T?) {
    data = item
  }

  override suspend fun get(): T? = data

  override suspend fun delete() {
    data = null
  }
}

// Delegate the MemoryStorage to the Storage
inline fun <reified T : @Serializable Any> MemoryStorage(): Storage<T> = StorageDelegate(Memory())
```

Use your custom storage solution in a module as follows:

Using a custom storage solution

```kotlin
module(Cookie) {
    persist = mutableListOf("ST", "ST-NO-SS")
    storage = { MemoryStorage() }
}
```

|   |                                                                                                                                                                                                                         |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Use an equals sign when assigning a custom class to the `storage` property in the module configuration.You do not need an equals sign when passing configuration settings to the default storage solution for a module. |