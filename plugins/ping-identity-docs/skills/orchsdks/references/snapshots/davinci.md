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
    // Handle error
  } else {
    // Update the FidoRegistrationCollector with the credential
    const updater = davinciClient.update(collector);
    updater(publicKeyCredential);
  }
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
    // Handle error
  } else {
    // Update the FidoAuthenticationCollector with the credential
    const updater = davinciClient.update(collector);
    updater(assertion);
  }
}

let nextStep = davinciClient.next();
```

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
    > | Field (`Collector`)                       | Description                                                                        | DaVinci module |          |            |
    > | ----------------------------------------- | ---------------------------------------------------------------------------------- | -------------- | -------- | ---------- |
    > |                                           |                                                                                    | Android        | iOS      | JavaScript |
    > | Text field(`TextCollector`)               | Collects a single text string.                                                     | ✅`1.0.0`       | ✅`1.0.0` | ✅`1.0.0`   |
    > | Password field(`PasswordCollector`)       | Collects a single text string that cannot be read from the screen.                 | ✅`1.0.0`       | ✅`1.0.0` | ✅`1.0.0`   |
    > | Submit Button(`SubmitCollector`)          | Sends the collected data to PingOne to continue the DaVinci flow.                  | ✅`1.0.0`       | ✅`1.0.0` | ✅`1.0.0`   |
    > | Flow Button(`FlowCollector`)              | Triggers an alternative flow without sending the data collected so far to PingOne. | ✅`1.0.0`       | ✅`1.0.0` | ✅`1.0.0`   |
    > | Label(`LabelCollector`)                   | Display a read-only text label.                                                    | ✅`1.1.0`       | ✅`1.1.0` | ✅`1.1.0`   |
    > | Radio / Dropdown(`SingleSelectCollector`) | Collects a single value from a choice of multiple options.                         | ✅`1.1.0`       | ✅`1.1.0` | ✅`1.1.0`   |
    >
    > **HTTP Connector SK-Component support**
    >
    > | SK-Component (`Collector`) | Description                                                                                                               | DaVinci module |          |            |
    > | -------------------------- | ------------------------------------------------------------------------------------------------------------------------- | -------------- | -------- | ---------- |
    > |                            |                                                                                                                           | Android        | iOS      | JavaScript |
    > | skIDP(`IdpCollector`)      | Presents a button to allow users to authenticate using an external identity provider, such as Apple, Facebook, or Google. | ✅`1.1.0`       | ✅`1.1.0` | ✅`1.1.0`   |
    > | skrisk(`ProtectCollector`) | Instructs the client to gather behavioral data and return it to PingOne so that it can perform risk evaluations.          | ✅`1.3.0`       | ✅`1.3.0` | ✅`1.3.0`   |

    > **Collapse: View unsupported features**
    >
    > Verify that your flow does not depend on any *unsupported* elements:
    >
    > * SKPolling components
    >
    >   The **[SKPolling](https://docs.pingidentity.com/davinci/flows/davinci_sk_components.html#skpolling)** component cannot be processed by the DaVinci Client and should not be included in flows.
    >
    >   Features such as Magic Link authentication require the **SKPolling** component and therefore cannot be used with the DaVinci Client.
    >
    > * Images
    >
    >   Images included in the flow cannot be passed to the SDK.

  For example, the [PingOne sign-on with sessions DaVinci flow](https://support.pingidentity.com/s/marketplace-integration/a7iDo00000110R2IAI/pingone-sign-on-with-sessions).

* PingOne Form Connector

  * **Show Form** capability

    > **Collapse: View supported fields**
    >
    > * [Custom Fields support](#form-connector-fields-android-compatibility)
    >
    > * [Toolbox support](#form-connector-toolbox-android-compatibility)
    >
    > **Custom Fields support**
    >
    > | Field (`Collector`)                        | Description                                                                                                     | DaVinci module |          |            |
    > | ------------------------------------------ | --------------------------------------------------------------------------------------------------------------- | -------------- | -------- | ---------- |
    > |                                            |                                                                                                                 | Android        | iOS      | JavaScript |
    > | Text Input(`TextCollector`)                | Collects a single text string.                                                                                  | ✅`1.1.0`       | ✅`1.1.0` | ✅`1.1.0`   |
    > | Password(`PasswordCollector`)              | Collects a single text string that cannot be read from the screen.                                              | ✅`1.1.0`       | ✅`1.1.0` | ✅`1.1.0`   |
    > | Dropdown(`SingleSelectCollector`)          | Collects a value from a dropdown containing one or more text strings.                                           | ✅`1.1.0`       | ✅`1.1.0` | ✅`1.1.0`   |
    > | Combobox(`MultiSelectCollector`)           | Collects a value from a dropdown containing one or more text strings, the user can enter their own text string. | ✅`1.1.0`       | ✅`1.1.0` | ✅`1.1.0`   |
    > | Radio Button List(`SingleSelectCollector`) | Collects a value from one or radio buttons.                                                                     | ✅`1.1.0`       | ✅`1.1.0` | ✅`1.1.0`   |
    > | Checkbox List(`MultiSelectCollector`)      | Collects the value of one or more checkboxes.                                                                   | ✅`1.1.0`       | ✅`1.1.0` | ✅`1.1.0`   |
    > | Phone Number Input(`PhoneNumberCollector`) | Collects a phone number, including the country code.                                                            | ✅`1.2.0`       | ✅`1.2.0` | ✅`1.2.0`   |
    >
    > **Toolbox support**
    >
    > | Field (`Collector`)                                                    | Description                                                                                                                                                             | DaVinci module |          |            |
    > | ---------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------- | -------- | ---------- |
    > |                                                                        |                                                                                                                                                                         | Android        | iOS      | JavaScript |
    > | Flow Button(`FlowCollector`)                                           | Presents a customized button.                                                                                                                                           | ✅`1.1.0`       | ✅`1.1.0` | ✅`1.1.0`   |
    > | Flow Link(`FlowCollector`)                                             | Presents a customized link.                                                                                                                                             | ✅`1.1.0`       | ✅`1.1.0` | ✅`1.1.0`   |
    > | Translatable Rich Text(`TextCollector`)                                | Presents rich text that you can translate into multiple languages.                                                                                                      | ✅`1.1.0`       | ✅`1.1.0` | ✅`1.1.0`   |
    > | Social Login(`IdpCollector`)                                           | Presents a button to allow users to authenticate using an external identity provider, such as Apple, Facebook, or Google.                                               | ✅`1.1.0`       | ✅`1.1.0` | ✅`1.1.0`   |
    > | MFA Device Selection - Authentication(`DeviceAuthenticationCollector`) | Presents a list of methods for performing multi-factor authentication (MFA).&#xA;&#xA;DaVinci client currently only supports the Email, SMS, and Voice MFA types.       | ✅`1.2.0`       | ✅`1.2.0` | ✅`1.2.0`   |
    > | MFA Device Selection - Registration(`DeviceRegistrationCollector`)     | Presents a list of methods you can register for multi-factor authentication (MFA).&#xA;&#xA;DaVinci client currently only supports the Email, SMS, and Voice MFA types. | ✅`1.2.0`       | ✅`1.2.0` | ✅`1.2.0`   |

* PingOne Protect Connector

  * **Create Risk Evaluation** capability

    | Android  | iOS      | JavaScript |
    | -------- | -------- | ---------- |
    | ✅`1.3.0` | ✅`1.3.0` | ✅`1.3.0`   |

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
    > | Field (`Collector`)                       | Description                                                                        | DaVinci module |          |            |
    > | ----------------------------------------- | ---------------------------------------------------------------------------------- | -------------- | -------- | ---------- |
    > |                                           |                                                                                    | Android        | iOS      | JavaScript |
    > | Text field(`TextCollector`)               | Collects a single text string.                                                     | ✅`1.0.0`       | ✅`1.0.0` | ✅`1.0.0`   |
    > | Password field(`PasswordCollector`)       | Collects a single text string that cannot be read from the screen.                 | ✅`1.0.0`       | ✅`1.0.0` | ✅`1.0.0`   |
    > | Submit Button(`SubmitCollector`)          | Sends the collected data to PingOne to continue the DaVinci flow.                  | ✅`1.0.0`       | ✅`1.0.0` | ✅`1.0.0`   |
    > | Flow Button(`FlowCollector`)              | Triggers an alternative flow without sending the data collected so far to PingOne. | ✅`1.0.0`       | ✅`1.0.0` | ✅`1.0.0`   |
    > | Label(`LabelCollector`)                   | Display a read-only text label.                                                    | ✅`1.1.0`       | ✅`1.1.0` | ✅`1.1.0`   |
    > | Radio / Dropdown(`SingleSelectCollector`) | Collects a single value from a choice of multiple options.                         | ✅`1.1.0`       | ✅`1.1.0` | ✅`1.1.0`   |
    >
    > **HTTP Connector SK-Component support**
    >
    > | SK-Component (`Collector`) | Description                                                                                                               | DaVinci module |          |            |
    > | -------------------------- | ------------------------------------------------------------------------------------------------------------------------- | -------------- | -------- | ---------- |
    > |                            |                                                                                                                           | Android        | iOS      | JavaScript |
    > | skIDP(`IdpCollector`)      | Presents a button to allow users to authenticate using an external identity provider, such as Apple, Facebook, or Google. | ✅`1.1.0`       | ✅`1.1.0` | ✅`1.1.0`   |
    > | skrisk(`ProtectCollector`) | Instructs the client to gather behavioral data and return it to PingOne so that it can perform risk evaluations.          | ✅`1.3.0`       | ✅`1.3.0` | ✅`1.3.0`   |

    > **Collapse: View unsupported features**
    >
    > Verify that your flow does not depend on any *unsupported* elements:
    >
    > * SKPolling components
    >
    >   The **[SKPolling](https://docs.pingidentity.com/davinci/flows/davinci_sk_components.html#skpolling)** component cannot be processed by the DaVinci Client and should not be included in flows.
    >
    >   Features such as Magic Link authentication require the **SKPolling** component and therefore cannot be used with the DaVinci Client.
    >
    > * Images
    >
    >   Images included in the flow cannot be passed to the SDK.

  For example, the [PingOne sign-on with sessions DaVinci flow](https://support.pingidentity.com/s/marketplace-integration/a7iDo00000110R2IAI/pingone-sign-on-with-sessions).

* PingOne Form Connector

  * **Show Form** capability

    > **Collapse: View supported fields**
    >
    > * [Custom Fields support](#form-connector-fields-ios-compatibility)
    >
    > * [Toolbox support](#form-connector-toolbox-ios-compatibility)
    >
    > **Custom Fields support**
    >
    > | Field (`Collector`)                        | Description                                                                                                     | DaVinci module |          |            |
    > | ------------------------------------------ | --------------------------------------------------------------------------------------------------------------- | -------------- | -------- | ---------- |
    > |                                            |                                                                                                                 | Android        | iOS      | JavaScript |
    > | Text Input(`TextCollector`)                | Collects a single text string.                                                                                  | ✅`1.1.0`       | ✅`1.1.0` | ✅`1.1.0`   |
    > | Password(`PasswordCollector`)              | Collects a single text string that cannot be read from the screen.                                              | ✅`1.1.0`       | ✅`1.1.0` | ✅`1.1.0`   |
    > | Dropdown(`SingleSelectCollector`)          | Collects a value from a dropdown containing one or more text strings.                                           | ✅`1.1.0`       | ✅`1.1.0` | ✅`1.1.0`   |
    > | Combobox(`MultiSelectCollector`)           | Collects a value from a dropdown containing one or more text strings, the user can enter their own text string. | ✅`1.1.0`       | ✅`1.1.0` | ✅`1.1.0`   |
    > | Radio Button List(`SingleSelectCollector`) | Collects a value from one or radio buttons.                                                                     | ✅`1.1.0`       | ✅`1.1.0` | ✅`1.1.0`   |
    > | Checkbox List(`MultiSelectCollector`)      | Collects the value of one or more checkboxes.                                                                   | ✅`1.1.0`       | ✅`1.1.0` | ✅`1.1.0`   |
    > | Phone Number Input(`PhoneNumberCollector`) | Collects a phone number, including the country code.                                                            | ✅`1.2.0`       | ✅`1.2.0` | ✅`1.2.0`   |
    >
    > **Toolbox support**
    >
    > | Field (`Collector`)                                                    | Description                                                                                                                                                             | DaVinci module |          |            |
    > | ---------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------- | -------- | ---------- |
    > |                                                                        |                                                                                                                                                                         | Android        | iOS      | JavaScript |
    > | Flow Button(`FlowCollector`)                                           | Presents a customized button.                                                                                                                                           | ✅`1.1.0`       | ✅`1.1.0` | ✅`1.1.0`   |
    > | Flow Link(`FlowCollector`)                                             | Presents a customized link.                                                                                                                                             | ✅`1.1.0`       | ✅`1.1.0` | ✅`1.1.0`   |
    > | Translatable Rich Text(`TextCollector`)                                | Presents rich text that you can translate into multiple languages.                                                                                                      | ✅`1.1.0`       | ✅`1.1.0` | ✅`1.1.0`   |
    > | Social Login(`IdpCollector`)                                           | Presents a button to allow users to authenticate using an external identity provider, such as Apple, Facebook, or Google.                                               | ✅`1.1.0`       | ✅`1.1.0` | ✅`1.1.0`   |
    > | MFA Device Selection - Authentication(`DeviceAuthenticationCollector`) | Presents a list of methods for performing multi-factor authentication (MFA).&#xA;&#xA;DaVinci client currently only supports the Email, SMS, and Voice MFA types.       | ✅`1.2.0`       | ✅`1.2.0` | ✅`1.2.0`   |
    > | MFA Device Selection - Registration(`DeviceRegistrationCollector`)     | Presents a list of methods you can register for multi-factor authentication (MFA).&#xA;&#xA;DaVinci client currently only supports the Email, SMS, and Voice MFA types. | ✅`1.2.0`       | ✅`1.2.0` | ✅`1.2.0`   |

* PingOne Protect Connector

  * **Create Risk Evaluation** capability

    | Android  | iOS      | JavaScript |
    | -------- | -------- | ---------- |
    | ✅`1.3.0` | ✅`1.3.0` | ✅`1.3.0`   |

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
    > | Field (`Collector`)                       | Description                                                                        | DaVinci module |          |            |
    > | ----------------------------------------- | ---------------------------------------------------------------------------------- | -------------- | -------- | ---------- |
    > |                                           |                                                                                    | Android        | iOS      | JavaScript |
    > | Text field(`TextCollector`)               | Collects a single text string.                                                     | ✅`1.0.0`       | ✅`1.0.0` | ✅`1.0.0`   |
    > | Password field(`PasswordCollector`)       | Collects a single text string that cannot be read from the screen.                 | ✅`1.0.0`       | ✅`1.0.0` | ✅`1.0.0`   |
    > | Submit Button(`SubmitCollector`)          | Sends the collected data to PingOne to continue the DaVinci flow.                  | ✅`1.0.0`       | ✅`1.0.0` | ✅`1.0.0`   |
    > | Flow Button(`FlowCollector`)              | Triggers an alternative flow without sending the data collected so far to PingOne. | ✅`1.0.0`       | ✅`1.0.0` | ✅`1.0.0`   |
    > | Label(`LabelCollector`)                   | Display a read-only text label.                                                    | ✅`1.1.0`       | ✅`1.1.0` | ✅`1.1.0`   |
    > | Radio / Dropdown(`SingleSelectCollector`) | Collects a single value from a choice of multiple options.                         | ✅`1.1.0`       | ✅`1.1.0` | ✅`1.1.0`   |
    >
    > **HTTP Connector SK-Component support**
    >
    > | SK-Component (`Collector`) | Description                                                                                                               | DaVinci module |          |            |
    > | -------------------------- | ------------------------------------------------------------------------------------------------------------------------- | -------------- | -------- | ---------- |
    > |                            |                                                                                                                           | Android        | iOS      | JavaScript |
    > | skIDP(`IdpCollector`)      | Presents a button to allow users to authenticate using an external identity provider, such as Apple, Facebook, or Google. | ✅`1.1.0`       | ✅`1.1.0` | ✅`1.1.0`   |
    > | skrisk(`ProtectCollector`) | Instructs the client to gather behavioral data and return it to PingOne so that it can perform risk evaluations.          | ✅`1.3.0`       | ✅`1.3.0` | ✅`1.3.0`   |

    > **Collapse: View unsupported features**
    >
    > Verify that your flow does not depend on any *unsupported* elements:
    >
    > * SKPolling components
    >
    >   The **[SKPolling](https://docs.pingidentity.com/davinci/flows/davinci_sk_components.html#skpolling)** component cannot be processed by the DaVinci Client and should not be included in flows.
    >
    >   Features such as Magic Link authentication require the **SKPolling** component and therefore cannot be used with the DaVinci Client.
    >
    > * Images
    >
    >   Images included in the flow cannot be passed to the SDK.

  For example, the [PingOne sign-on with sessions DaVinci flow](https://support.pingidentity.com/s/marketplace-integration/a7iDo00000110R2IAI/pingone-sign-on-with-sessions).

* PingOne Form Connector

  * **Show Form** capability

    > **Collapse: View supported fields**
    >
    > * [Custom Fields support](#form-connector-fields-js-compatibility)
    >
    > * [Toolbox support](#form-connector-toolbox-js-compatibility)
    >
    > **Custom Fields support**
    >
    > | Field (`Collector`)                        | Description                                                                                                     | DaVinci module |          |            |
    > | ------------------------------------------ | --------------------------------------------------------------------------------------------------------------- | -------------- | -------- | ---------- |
    > |                                            |                                                                                                                 | Android        | iOS      | JavaScript |
    > | Text Input(`TextCollector`)                | Collects a single text string.                                                                                  | ✅`1.1.0`       | ✅`1.1.0` | ✅`1.1.0`   |
    > | Password(`PasswordCollector`)              | Collects a single text string that cannot be read from the screen.                                              | ✅`1.1.0`       | ✅`1.1.0` | ✅`1.1.0`   |
    > | Dropdown(`SingleSelectCollector`)          | Collects a value from a dropdown containing one or more text strings.                                           | ✅`1.1.0`       | ✅`1.1.0` | ✅`1.1.0`   |
    > | Combobox(`MultiSelectCollector`)           | Collects a value from a dropdown containing one or more text strings, the user can enter their own text string. | ✅`1.1.0`       | ✅`1.1.0` | ✅`1.1.0`   |
    > | Radio Button List(`SingleSelectCollector`) | Collects a value from one or radio buttons.                                                                     | ✅`1.1.0`       | ✅`1.1.0` | ✅`1.1.0`   |
    > | Checkbox List(`MultiSelectCollector`)      | Collects the value of one or more checkboxes.                                                                   | ✅`1.1.0`       | ✅`1.1.0` | ✅`1.1.0`   |
    > | Phone Number Input(`PhoneNumberCollector`) | Collects a phone number, including the country code.                                                            | ✅`1.2.0`       | ✅`1.2.0` | ✅`1.2.0`   |
    >
    > **Toolbox support**
    >
    > | Field (`Collector`)                                                    | Description                                                                                                                                                             | DaVinci module |          |            |
    > | ---------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------- | -------- | ---------- |
    > |                                                                        |                                                                                                                                                                         | Android        | iOS      | JavaScript |
    > | Flow Button(`FlowCollector`)                                           | Presents a customized button.                                                                                                                                           | ✅`1.1.0`       | ✅`1.1.0` | ✅`1.1.0`   |
    > | Flow Link(`FlowCollector`)                                             | Presents a customized link.                                                                                                                                             | ✅`1.1.0`       | ✅`1.1.0` | ✅`1.1.0`   |
    > | Translatable Rich Text(`TextCollector`)                                | Presents rich text that you can translate into multiple languages.                                                                                                      | ✅`1.1.0`       | ✅`1.1.0` | ✅`1.1.0`   |
    > | Social Login(`IdpCollector`)                                           | Presents a button to allow users to authenticate using an external identity provider, such as Apple, Facebook, or Google.                                               | ✅`1.1.0`       | ✅`1.1.0` | ✅`1.1.0`   |
    > | MFA Device Selection - Authentication(`DeviceAuthenticationCollector`) | Presents a list of methods for performing multi-factor authentication (MFA).&#xA;&#xA;DaVinci client currently only supports the Email, SMS, and Voice MFA types.       | ✅`1.2.0`       | ✅`1.2.0` | ✅`1.2.0`   |
    > | MFA Device Selection - Registration(`DeviceRegistrationCollector`)     | Presents a list of methods you can register for multi-factor authentication (MFA).&#xA;&#xA;DaVinci client currently only supports the Email, SMS, and Voice MFA types. | ✅`1.2.0`       | ✅`1.2.0` | ✅`1.2.0`   |

* PingOne Protect Connector

  * **Create Risk Evaluation** capability

    | Android  | iOS      | JavaScript |
    | -------- | -------- | ---------- |
    | ✅`1.3.0` | ✅`1.3.0` | ✅`1.3.0`   |

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
  webviews_unsupported_davinci: JavaScript Compatibility with WebViews
  supported-davinci-fields: Supported PingOne fields and collectors
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

The Orchestration SDK for Android supports the following versions of the Android operating system:

**Supported Android versions and original release dates**

| Release    | API Levels | Released        |
| ---------- | ---------- | --------------- |
| Android 16 | 36         | August, 2025    |
| Android 15 | 35         | September, 2024 |
| Android 14 | 34         | October, 2023   |
| Android 13 | 33         | March, 2022     |
| Android 12 | 31, 32     | October, 2021   |
| Android 11 | 30         | September, 2020 |
| Android 10 | 29         | September, 2019 |

|   |                                                                                                                                                                                                                                                                                                        |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | We have updated how we determine which Android versions form our support policy for the Orchestration SDK for Android.The support policy is as follows:- Every public major release of Android within the last 6 years.

  For example, this would mean support for **Android 10** and later versions. |

**Supported browsers on Android**

* Chrome - Two most recent major versions.

The Orchestration SDK for iOS supports the following versions of the iOS operating system:

**Supported iOS versions and original release dates**

| Release | Released        |
| ------- | --------------- |
| iOS 26  | September, 2025 |
| iOS 18  | September, 2024 |
| iOS 17  | September, 2023 |
| iOS 16  | September, 2022 |

|   |                                                                                                                                                                                                                                                                                        |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | We have updated how we determine which iOS versions form our support policy for the Orchestration SDK for iOS.The support policy is as follows:- Every public major release of iOS within the last 3 years.

  For example, this would mean support for **iOS 16** and later versions. |

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

### JavaScript Compatibility with WebViews

A WebView allows you to embed a web browser into your native Android or iOS application to display HTML pages, and run JavaScript apps.

For example, the Android system WebView is based on the Google Chrome engine, and the iOS WebView is based on the Safari browser engine.

However, it is important to note that WebViews do not implement the full feature set of their respective browsers. For example, some of the browser-provided APIs that the Orchestration SDK for JavaScript requires are not available in a WebView, such as the WebAuthn APIs.

In addition, there are concerns that a WebView does not provide the same level of security as their full browser counterparts.

As the SDK requires full, spec-compliant, browser-supplied APIs for full functionality we **do not** support usage within a WebView.

We also do not support or test usage with any wrappers around WebViews.

Whilst you might be able to implement simple use-cases using the Orchestration SDK for JavaScript within a WebView, we recommend that you use an alternative such as opening a full browser, or using an in-app instance of a full browser such as [Custom Tabs](https://developer.android.com/develop/ui/views/layout/webapps/overview-of-android-custom-tabs) for Android or [SFSafariViewController](https://developer.apple.com/documentation/safariservices/sfsafariviewcontroller) for iOS.

## Supported PingOne fields and collectors

The DaVinci modules support the following connectors and capabilities:

* PingOne Forms Connector

  * **Show Form** capability

* HTTP Connector

  * **Custom HTML** capability

- PingOne Form Connector fields

- HTTP Connector fields

* [Custom Fields support](#form-connector-fields-compatibility)

* [Toolbox support](#form-connector-toolbox-compatibility)

**Custom Fields support**

| Field (`Collector`)                        | Description                                                                                                     | DaVinci module |          |            |
| ------------------------------------------ | --------------------------------------------------------------------------------------------------------------- | -------------- | -------- | ---------- |
|                                            |                                                                                                                 | Android        | iOS      | JavaScript |
| Text Input(`TextCollector`)                | Collects a single text string.                                                                                  | ✅`1.1.0`       | ✅`1.1.0` | ✅`1.1.0`   |
| Password(`PasswordCollector`)              | Collects a single text string that cannot be read from the screen.                                              | ✅`1.1.0`       | ✅`1.1.0` | ✅`1.1.0`   |
| Dropdown(`SingleSelectCollector`)          | Collects a value from a dropdown containing one or more text strings.                                           | ✅`1.1.0`       | ✅`1.1.0` | ✅`1.1.0`   |
| Combobox(`MultiSelectCollector`)           | Collects a value from a dropdown containing one or more text strings, the user can enter their own text string. | ✅`1.1.0`       | ✅`1.1.0` | ✅`1.1.0`   |
| Radio Button List(`SingleSelectCollector`) | Collects a value from one or radio buttons.                                                                     | ✅`1.1.0`       | ✅`1.1.0` | ✅`1.1.0`   |
| Checkbox List(`MultiSelectCollector`)      | Collects the value of one or more checkboxes.                                                                   | ✅`1.1.0`       | ✅`1.1.0` | ✅`1.1.0`   |
| Phone Number Input(`PhoneNumberCollector`) | Collects a phone number, including the country code.                                                            | ✅`1.2.0`       | ✅`1.2.0` | ✅`1.2.0`   |

**Toolbox support**

| Field (`Collector`)                                                    | Description                                                                                                                                                             | DaVinci module |          |            |
| ---------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------- | -------- | ---------- |
|                                                                        |                                                                                                                                                                         | Android        | iOS      | JavaScript |
| Flow Button(`FlowCollector`)                                           | Presents a customized button.                                                                                                                                           | ✅`1.1.0`       | ✅`1.1.0` | ✅`1.1.0`   |
| Flow Link(`FlowCollector`)                                             | Presents a customized link.                                                                                                                                             | ✅`1.1.0`       | ✅`1.1.0` | ✅`1.1.0`   |
| Translatable Rich Text(`TextCollector`)                                | Presents rich text that you can translate into multiple languages.                                                                                                      | ✅`1.1.0`       | ✅`1.1.0` | ✅`1.1.0`   |
| Social Login(`IdpCollector`)                                           | Presents a button to allow users to authenticate using an external identity provider, such as Apple, Facebook, or Google.                                               | ✅`1.1.0`       | ✅`1.1.0` | ✅`1.1.0`   |
| MFA Device Selection - Authentication(`DeviceAuthenticationCollector`) | Presents a list of methods for performing multi-factor authentication (MFA).&#xA;&#xA;DaVinci client currently only supports the Email, SMS, and Voice MFA types.       | ✅`1.2.0`       | ✅`1.2.0` | ✅`1.2.0`   |
| MFA Device Selection - Registration(`DeviceRegistrationCollector`)     | Presents a list of methods you can register for multi-factor authentication (MFA).&#xA;&#xA;DaVinci client currently only supports the Email, SMS, and Voice MFA types. | ✅`1.2.0`       | ✅`1.2.0` | ✅`1.2.0`   |

* [HTTP Connector field and collector support](#http-connector-fields-compatibility)

* [HTTP Connector SK-Component support](#http-connector-sk-components-compatibility)

**HTTP Connector field and collector support**

| Field (`Collector`)                       | Description                                                                        | DaVinci module |          |            |
| ----------------------------------------- | ---------------------------------------------------------------------------------- | -------------- | -------- | ---------- |
|                                           |                                                                                    | Android        | iOS      | JavaScript |
| Text field(`TextCollector`)               | Collects a single text string.                                                     | ✅`1.0.0`       | ✅`1.0.0` | ✅`1.0.0`   |
| Password field(`PasswordCollector`)       | Collects a single text string that cannot be read from the screen.                 | ✅`1.0.0`       | ✅`1.0.0` | ✅`1.0.0`   |
| Submit Button(`SubmitCollector`)          | Sends the collected data to PingOne to continue the DaVinci flow.                  | ✅`1.0.0`       | ✅`1.0.0` | ✅`1.0.0`   |
| Flow Button(`FlowCollector`)              | Triggers an alternative flow without sending the data collected so far to PingOne. | ✅`1.0.0`       | ✅`1.0.0` | ✅`1.0.0`   |
| Label(`LabelCollector`)                   | Display a read-only text label.                                                    | ✅`1.1.0`       | ✅`1.1.0` | ✅`1.1.0`   |
| Radio / Dropdown(`SingleSelectCollector`) | Collects a single value from a choice of multiple options.                         | ✅`1.1.0`       | ✅`1.1.0` | ✅`1.1.0`   |

**HTTP Connector SK-Component support**

| SK-Component (`Collector`) | Description                                                                                                               | DaVinci module |          |            |
| -------------------------- | ------------------------------------------------------------------------------------------------------------------------- | -------------- | -------- | ---------- |
|                            |                                                                                                                           | Android        | iOS      | JavaScript |
| skIDP(`IdpCollector`)      | Presents a button to allow users to authenticate using an external identity provider, such as Apple, Facebook, or Google. | ✅`1.1.0`       | ✅`1.1.0` | ✅`1.1.0`   |
| skrisk(`ProtectCollector`) | Instructs the client to gather behavioral data and return it to PingOne so that it can perform risk evaluations.          | ✅`1.3.0`       | ✅`1.3.0` | ✅`1.3.0`   |

**Unsupported features:**

Verify that your flow does not depend on any *unsupported* elements:

* SKPolling components

  The **[SKPolling](https://docs.pingidentity.com/davinci/flows/davinci_sk_components.html#skpolling)** component cannot be processed by the DaVinci Client and should not be included in flows.

  Features such as Magic Link authentication require the **SKPolling** component and therefore cannot be used with the DaVinci Client.

* Images

  Images included in the flow cannot be passed to the SDK.

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
keywords: ["DaVinci", "Flows", "Tutorial", "Source Code", "Integration", "SDK", "Android"]
section_ids:
  step_1_adding_core_dependencies: Step 1. Adding core dependencies
  step_2_authenticating_with_external_idps: Step 2. Authenticating with external IdPs
---

# Configure a JavaScript app for social sign-on

[icon: circle-check, set=far]PingOne [icon: js, set=fab]JavaScript

Complete the following high-level tasks to configure a JavaScript client app to perform social sign-on with an external identity provider (IdP):

## [Step 1. Adding core dependencies](../../../../journey/use-cases/external-idp/javascript/01_adding_core_dependencies.html)

These dependencies provide core support for social sign-on. These are the minimum required dependencies for redirecting users to the IdP for authentication.

[**Start step 1**[icon: chevrons-right, set=fas, size=xs]](../../../../journey/use-cases/external-idp/javascript/01_adding_core_dependencies.html)

## [Step 2. Authenticating with external IdPs](../../../../journey/use-cases/external-idp/javascript/02_authenticate_with_external_idps.html)

Learn how to authenticate your users with the external IdPs you have configured in your DaVinci flows.

[**Start step 3**[icon: chevrons-right, set=fas, size=xs]](../../../../journey/use-cases/external-idp/javascript/02_authenticate_with_external_idps.html)

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

## [Step 1. Adding core dependencies](../../../../journey/use-cases/external-idp/android/01_adding_core_dependencies.html)

These dependencies provide core support for social sign-on. These are the minimum required dependencies for redirecting users to the IdP for authentication.

[**Start step 1**[icon: chevrons-right, set=fas, size=xs]](../../../../journey/use-cases/external-idp/android/01_adding_core_dependencies.html)

## [Step 2. Handling URI schemes](../../../../journey/use-cases/external-idp/android/02_handling_uri_schemes.html)

You must configure your Android app to open when the server redirects the user after authentication.

[**Start step 2**[icon: chevrons-right, set=fas, size=xs]](../../../../journey/use-cases/external-idp/android/02_handling_uri_schemes.html)

## [Step 3. Authenticating with external IdPs](../../../../journey/use-cases/external-idp/android/03_authenticate_with_external_idps.html)

Learn how to authenticate your users with the external IdPs you have configured in your DaVinci flows.

[**Start step 3**[icon: chevrons-right, set=fas, size=xs]](../../../../journey/use-cases/external-idp/android/03_authenticate_with_external_idps.html)

## [Step 4. Customizing the user experience](../../../../journey/use-cases/external-idp/android/04_customize_the_user_experience.html)

You can optionally tweak the user experience for authenticating with an external IdP.

[**Start step 4**[icon: chevrons-right, set=fas, size=xs]](../../../../journey/use-cases/external-idp/android/04_customize_the_user_experience.html)

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

Complete the following high-level tasks to configure an Android client app to perform social sign-on with an external identity provider (IdP):

## [Step 1. Adding core dependencies](../../../../journey/use-cases/external-idp/ios/01_adding_core_dependencies.html)

These dependencies provide core support for social sign-on. These are the minimum required dependencies for redirecting users to the IdP for authentication.

[**Start step 1**[icon: chevrons-right, set=fas, size=xs]](../../../../journey/use-cases/external-idp/ios/01_adding_core_dependencies.html)

## [Step 2. Handling URI schemes](../../../../journey/use-cases/external-idp/ios/02_handling_uri_schemes.html)

You must configure your Android app to open when the server redirects the user after authentication.

[**Start step 2**[icon: chevrons-right, set=fas, size=xs]](../../../../journey/use-cases/external-idp/ios/02_handling_uri_schemes.html)

## [Step 3. Authenticating with external IdPs](../../../../journey/use-cases/external-idp/ios/03_authenticate_with_external_idps.html)

Learn how to authenticate your users with the external IdPs you have configured in your DaVinci flows.

[**Start step 3**[icon: chevrons-right, set=fas, size=xs]](../../../../journey/use-cases/external-idp/ios/03_authenticate_with_external_idps.html)

## [Step 4. Customizing the user experience](../../../../journey/use-cases/external-idp/ios/04_customize_the_user_experience.html)

You can optionally tweak the user experience for authenticating with an external IdP.

[**Start step 4**[icon: chevrons-right, set=fas, size=xs]](../../../../journey/use-cases/external-idp/ios/04_customize_the_user_experience.html)

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

[icon: circle-check, set=far]PingOne [icon: android, set=fab]Android [icon: apple, set=fab]iOS [icon: js, set=fab]JavaScript

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

* **PingOne Forms connector**

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

[icon: circle-check, set=far]PingOne [icon: android, set=fab]Android [icon: apple, set=fab]iOS [icon: js, set=fab]JavaScript

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

Optionally, you can choose to use the embedded SDKs of supported IdPs for Android and iOS apps. In this mode your app communicates directly with the supported IdP via its SDK. This requires additional configuration in the IdP and in your client application. These additional steps are covered in a later step for each platform.

## Connecting external identity providers in PingOne

In this section, you configure PingOne with details about the social login identity providers you want to integrate into your client apps.

The Orchestration SDKs are compatible with any OpenID Connect 1.0-compliant Identity Provider, such as those available by default in PingOne.

|   |                                                                                                                                                                                                                                                                            |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | You must configure the identity provider as a **PingOne External IdP**. Learn more in [External IdPs ](https://docs.pingidentity.com/pingone/integrations/p1_external_idps.html).Identity providers configured by using a **DaVinci Service Connector** are not supported. |

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

## Configuring DaVinci Flows for social sign-on

After connecting your chosen external identity providers to PingOne, the next step is to configure a DaVinci flow to display buttons on your login pages so that users can choose to authenticate using the external IdP.

![An Android app with three external IdP options; Google, Apple, and Facebook.](../../_images/social-sign-on-example.png)Figure 1. An Android app with three external IdP options: Google, Apple, and Facebook.

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

       [Step 2. Handling URI schemes](../../../journey/use-cases/external-idp/android/02_handling_uri_schemes.html)

     * iOS

       [Step 2. Handling URI schemes](../../../journey/use-cases/external-idp/ios/02_handling_uri_schemes.html)

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

          [Step 2. Handling URI schemes](../../../journey/use-cases/external-idp/android/02_handling_uri_schemes.html)

        * iOS

          [Step 2. Handling URI schemes](../../../journey/use-cases/external-idp/ios/02_handling_uri_schemes.html)

      The result will resemble the following:

      ![Configuring an skIdP component in an HTTP connector.](../../_images/davinci-http-connector-skidp-config.png)Figure 8. Configuring an skIdP component in an HTTP connector.

4. Save your changes.

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

  * If you are developing an Android or iOS app, you added redirect URI values to the flow to return users after authentication.

* Created an application in PingOne so that the Orchestration SDKs can connect

  * If you are developing a JavaScript app, you added redirect URI values to this application to return users after authentication.

You can now proceed to configuring your client apps to step through the DaVinci flows and perform social sign-on:

[icon: android, set=fab, size=3x]

#### [Android](../../../journey/use-cases/external-idp/android/index.html)

Configure an Android app for social sign-on

[icon: apple, set=fab, size=3x]

#### [iOS](../../../journey/use-cases/external-idp/ios/index.html)

Configure an iOS app for social sign-on

[icon: js, set=fab, size=3x]

#### [JavaScript](../../../journey/use-cases/external-idp/javascript/index.html)

Configure a JavaScript app for social sign-on

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
---

# Configuring the DaVinci module

[icon: circle-check, set=far]PingOne [icon: android, set=fab]Android

* [Install](01-installing-the-davinci-module.html)

* **Configure**

* [Navigate](03-stepping-through-davinci-flows.html)

Configure DaVinci module for Android properties to connect to PingOne and step through an associated DaVinci flow.

The following shows an example DaVinci module configuration, using the underlying `Oidc` module:

Configure DaVinci module connection properties

```kotlin
import com.pingidentity.davinci.DaVinci
import com.pingidentity.davinci.module.Oidc

val daVinci = DaVinci {
    logger = Logger.STANDARD
    module(Oidc) {
        clientId = "6c7eb89a-66e9-ab12-cd34-eeaf795650b2"
        discoveryEndpoint = "https://auth.pingone.com/3072206d-c6ce-ch15-m0nd-f87e972c7cc3/" +
            "as/.well-known/openid-configuration"
        scopes = mutableSetOf("openid", "profile", "email", "address", "revoke")
        redirectUri = "com.example.demo://oauth2redirect"
        additionalParameters = mapOf("customKey" to "customValue")
    }
}
```

The following properties are available for configuring the DaVinci module for Android:

**Properties**

| Property               | Description                                                                                                                                                                                                                                                                                                                                                                                              | Required? |
| ---------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------- |
| `discoveryEndpoint`    | Your PingOne server's `.well-known/openid-configuration` endpoint.*Example*:`https://auth.pingone.com/3072206d-c6ce-ch15-m0nd-f87e972c7cc3/as/.well-known/openid-configuration`                                                                                                                                                                                                                          | Yes       |
| `clientId`             | The `client_id` of the OAuth 2.0 client profile to use.For example, `6c7eb89a-66e9-ab12-cd34-eeaf795650b2`                                                                                                                                                                                                                                                                                               | Yes       |
| `scopes`               | A set of scopes to request when performing an OAuth 2.0 authorization flow\.For example, `"openid", "profile", "email", "address", "revoke"`.                                                                                                                                                                                                                                                            | Yes       |
| `redirectUri`          | The `redirect_uri` as configured in the OAuth 2.0 client profile.	This value must match a value configured in your OAuth 2.0 client.For example, `com.example.demo://oauth2redirect`.                                                                                                                                                                                                                    | Yes       |
| `timeout`              | A timeout, in seconds, for each request that communicates with the server.Default is `30` seconds.                                                                                                                                                                                                                                                                                                       | No        |
| `acrValues`            | Request which flow the PingOne server uses by adding an Authentication Context Class Reference (ACR) parameter.Enter a single DaVinci policy by using its flow policy ID.Example:`"d1210a6b0b2665dbaa5b652221badba2"`                                                                                                                                                                                    | No        |
| `logger`               | Specify which logger the Orchestration SDK should use to output messages. Select from the built-in presets `STANDARD` (the default), `WARN`, or `NONE`.You can also create and use your own logger implementation. Learn more in [Customizing logging on Android](../../customization/logging/android-custom-logging.html).                                                                              | No        |
| `additionalParameters` | Add additional key-pair parameters as query strings to the initial OAuth 2.0 call to the `/authorize` endpoint.For example, `additionalParameters = mapOf("customKey" to "customValue")`&#xA;&#xA;You can access these additional OAuth 2.0 parameters in your DaVinci flows by using the authorizationRequest.\<customParameter> property.&#xA;&#xA;Learn more in Referencing PingOne data in the flow. | No        |

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
---

# Configuring the DaVinci module

[icon: circle-check, set=far]PingOne [icon: apple, set=fab]iOS

* [Install](01-installing-the-davinci-module.html)

* **Configure**

* [Navigate](03-stepping-through-davinci-flows.html)

Configure DaVinci module for iOS properties to connect to PingOne and step through an associated DaVinci flow.

The following shows an example DaVinci module configuration, using the underlying `Oidc` module:

Configure DaVinci module connection properties

```swift
let daVinci = DaVinci.createDaVinci { config in
    config.logger = LogManager.standard
    // Oidc as module
    config.module(OidcModule.config) { oidcValue in
        oidcValue.clientId = "6c7eb89a-66e9-ab12-cd34-eeaf795650b2"
        oidcValue.discoveryEndpoint = "https://auth.pingone.com/3072206d-c6ce-ch15-m0nd-f87e972c7cc3/as/.well-known/openid-configuration"
        oidcValue.scopes = ["openid", "profile", "email", "address", "revoke"]
        oidcValue.redirectUri = "com.example.demo://oauth2redirect"
        oidcValue.additionalParameters = ["customKey":"customValue"]
    }
}
```

The following properties are available for configuring the DaVinci module for iOS:

**Properties**

| Property               | Description                                                                                                                                                                                                                                                                                                                                                                                               | Required? |
| ---------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------- |
| `discoveryEndpoint`    | Your PingOne server's `.well-known/openid-configuration` endpoint.*Example*:`https://auth.pingone.com/3072206d-c6ce-ch15-m0nd-f87e972c7cc3/as/.well-known/openid-configuration`                                                                                                                                                                                                                           | Yes       |
| `clientId`             | The `client_id` of the OAuth 2.0 client profile to use.For example, `6c7eb89a-66e9-ab12-cd34-eeaf795650b2`                                                                                                                                                                                                                                                                                                | Yes       |
| `scopes`               | A set of scopes to request when performing an OAuth 2.0 authorization flow\.For example, `"openid", "profile", "email", "address", "revoke"`.                                                                                                                                                                                                                                                             | Yes       |
| `redirectUri`          | The `redirect_uri` as configured in the OAuth 2.0 client profile.	This value must match a value configured in your OAuth 2.0 client.For example, `com.example.demo://oauth2redirect`.                                                                                                                                                                                                                     | Yes       |
| `timeout`              | A timeout, in seconds, for each request that communicates with the server.Default is `30` seconds.                                                                                                                                                                                                                                                                                                        | No        |
| `acrValues`            | Request which flow the PingOne server uses by adding an Authentication Context Class Reference (ACR) parameter.Enter a single DaVinci policy by using its flow policy ID.Example:`"d1210a6b0b2665dbaa5b652221badba2"`                                                                                                                                                                                     | No        |
| `logger`               | Specify which logger the Orchestration SDK should use to output messages. Select from the built-in presets `standard` (the default), `warning`, or `none`.You can also create and use your own logger implementation. Learn more in [Customizing logging on iOS](../../customization/logging/ios-custom-logging.html).                                                                                    | No        |
| `additionalParameters` | Add additional key-pair parameters as query strings to the initial OAuth 2.0 call to the `/authorize` endpoint.For example, `myConfig.additionalParameters = ["customKey":"customValue"]`&#xA;&#xA;You can access these additional OAuth 2.0 parameters in your DaVinci flows by using the authorizationRequest.\<customParameter> property.&#xA;&#xA;Learn more in Referencing PingOne data in the flow. | No        |

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
---

# Configuring the DaVinci module

[icon: circle-check, set=far]PingOne [icon: js, set=fab]JavaScript

* [Install](01-installing-the-davinci-module.html)

* **Configure**

* [Navigate](03-stepping-through-davinci-flows.html)

Configure DaVinci module for JavaScript properties to connect to PingOne and step through an associated DaVinci flow.

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
    serverConfig: {
      wellknown: 'https://auth.pingone.com/3072206d-c6ce-ch15-m0nd-f87e972c7cc3/as/.well-known/openid-configuration',
      timeout: 3000,
    },
    scope: '"openid", "email", "address", "profile", "phone"',
    responseType: 'code',
  },
});
```

The following properties are available for configuring the DaVinci module for JavaScript:

1. [Properties of the `config{}` object](#config-props)

2. [Properties of the `logger{}` object](#logger-props)

**confg{} Properties**

| Property                    | Description                                                                                                                                                                     | Required? |
| --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------- |
| `serverConfig`              | An interface for configuring how the SDK contacts the PingAM instance.Contains `wellknown` and `timeout`.                                                                       | Yes       |
| `serverConfig: {wellknown}` | Your PingOne server's `.well-known/openid-configuration` endpoint.*Example*:`https://auth.pingone.com/3072206d-c6ce-ch15-m0nd-f87e972c7cc3/as/.well-known/openid-configuration` | Yes       |
| `serverConfig: {timeout}`   | A timeout, in milliseconds, for each request that communicates with your server.For example, for 30 seconds specify `30000`.Defaults to `5000` (5 seconds).                     | No        |
| `clientId`                  | The `client_id` of the OAuth 2.0 client profile to use.For example, `6c7eb89a-66e9-ab12-cd34-eeaf795650b2`                                                                      | Yes       |
| `scope`                     | A list of scopes to request when performing an OAuth 2.0 authorization flow, separated by spaces.For example, `"openid", "email", "address", "profile", "phone"`.               | No        |
| `responseType`              | The type of OAuth 2.0 flow to use, either `code` or `token`.Defaults to `code`.                                                                                                 | No        |

**logger{} Properties**

| Property | Description                                                                                                                                                                                                                                                                                                 | Required? |
| -------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------- |
| `level`  | Specify what level of logging the Orchestration SDK should output.Select one of the following:- `none`

- `error`

- `warn`

- `info` (the default)

- `debug`Learn more in [Configuring JavaScript logging](../../customization/logging/javascript-custom-logging.html#configuring-logging-on-javascript). | No        |
| `custom` | Specify a custom logger the Orchestration SDK should use to output messages.Learn more in [Customizing JavaScript logging](../../customization/logging/javascript-custom-logging.html#customize-logger-javascript).Example:`customLogger`                                                                   | No        |

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
     implementation("com.pingidentity.sdks:davinci:2.0.1")

     // Storage module
     implementation("com.pingidentity.sdks:storage:2.0.1")
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

---

---
title: Customizing DaVinci module storage on iOS
description: Configure the DaVinci iOS SDK storage module to use built-in or custom storage solutions, with optional caching and encryption
component: orchsdks
page_id: orchsdks:davinci:customization/storage/customize-ios-storage
canonical_url: https://developer.pingidentity.com/orchsdks/davinci/customization/storage/customize-ios-storage.html
llms_txt: https://developer.pingidentity.com/orchsdks/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: Thu, 22 Jan 2026 12:23:51 +0000
section_ids:
  add_dependencies: Add dependencies
  install-protect-ios: Adding iOS dependencies
  add_dependencies_using_cocoapods: Add dependencies using CocoaPods
  add_dependencies_using_swift_package_manager: Add dependencies using Swift Package Manager
  using_the_provided_storage_solutions: Using the provided storage solutions
  provided_default_storage_solutions: Provided default storage solutions
  configuring_storage_solutions: Configuring storage solutions
  caching: Enabling caching
  encrypt-ios: Encrypting storage instances on iOS
  implementing_your_own_custom_storage: Implementing your own custom storage
---

# Customizing DaVinci module storage on iOS

[icon: circle-check, set=far]PingOne [icon: apple, set=fab]iOS

Depending on the authentication use case, you may need to store and retrieve ID tokens, access tokens, refresh tokens, or cookies.

Each token is serving a different use case, and as such how you handle them can be different.

The Orchestration SDKs employ identity best practices for storing data by default. However there are use cases where you might need to customize how the SDK stores data.

For example, you might be running on hardware that provides specialized security features, or perhaps target older hardware that cannot handle the latest algorithms.

For these cases, you can customize the provided storage solutions, or provide your own custom storage classes.

## Add dependencies

To customize your storage solution you need to add the `storage` module to your project.

### Adding iOS dependencies

You can use CocoaPods or the Swift Package Manager to add the dependencies to your iOS project.

#### Add dependencies using CocoaPods

1. If you do not already have CocoaPods, install the [latest version](https://guides.cocoapods.org/using/getting-started.html).

2. If you do not already have a Podfile, in a terminal window, run the following command to create a new [Podfile](https://guides.cocoapods.org/syntax/podfile.html):

   ```podfile
   pod init
   ```

3. Add the following lines to your Podfile:

   ```podfile
   pod 'Storage' // Add-on for customizing storage
   ```

4. Run the following command to install pods:

   ```
   pod install
   ```

#### Add dependencies using Swift Package Manager

1. With your project open in **Xcode**, select File > Add Package Dependencies.

2. In the search bar, enter the iOS repository URL: `https://github.com/ForgeRock/ping-ios-sdk`.

3. Select the `ping-ios-sdk` package, and then click Add Package.

4. In the Choose Package Products dialog, ensure that the `Storage` library is added to your target project.

5. Click Add Package.

6. In your project, import the library:

   ```swift
   // Import the Storage library
   import Storage
   ```

## Using the provided storage solutions

You can use the default storage solutions, and configure them to suit your requirements.

### Provided default storage solutions

You can use the default storage solutions in your apps, depending on the type of data you want to store.

* `MemoryStorage`

  Storage that stores data in memory.

  |   |                                                                                                                                                                                                 |
  | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | Data stored using the `MemoryStorage` solution is kept in plain text and is not encrypted.A device that can output a memory dump may expose sensitive information, such as access or ID tokens. |

* `KeychainStorage`

  Storage backed by the [iOS keychain](https://support.apple.com/en-gb/guide/security/secb0694df1a/web).

  This storage solution does not encrypt the data by default.

### Configuring storage solutions

You can customize aspects of the storage solutions by passing parameters when creating a storage instance.

The available properties are listed below:

**iOS storage properties**

| Property    | Description                                                                                                                                                                                            | Storage types                          |
| ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------- |
| `account`   | A user-defined string to uniquely identify the storage instance.                                                                                                                                       | * `MemoryStorage`

* `KeychainStorage` |
| `cacheable` | Enable caching of the data.Learn more in [Enabling caching](#caching).* Default value

  `CacheStrategy.NO_CACHE`                                                                                      | - `MemoryStorage`

- `KeychainStorage` |
| `encryptor` | Enable encryption of the data, by specifying the encryptor to use.Learn more in [Encrypting storage instances on iOS](#encrypt-ios).Available options are:- `SecuredKeyEncryptor()`

- `NoEncryptor()` | * `MemoryStorage`

* `KeychainStorage` |

The following code shows an example of customizing storage solutions and using custom types:

Customizing the `KeychainStorage` storage solution

```swift
// Define the custom data to store
struct Dog: Codable {
    let name: String
    let breed: String
}

// Create custom storage for custom data
let customStorage = KeychainStorage<Dog>(
  account: "myStorageId"
)

// Persist custom data
try? await customStorage.save(item: Dog(name: "Lucky", breed: "Golden Retriever"))

// Retrieve custom data
let storedData = try? await customStorage.get()
```

#### Enabling caching

You can add caching to each storage solution depending on the requirements of the type of data you store.

|   |                                                                                                                                                                         |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Data stored in a cache is kept in plain text and is not encrypted.A device that can output a memory dump may expose sensitive information, such as access or ID tokens. |

Use the `cacheable` property when creating a storage instance to enable caching:

Creating a storage instance with cache enabled

```swift
let customStorage = KeychainStorage<Dog>(
  account: "myStorageId",
  cacheable: true
)
```

#### Encrypting storage instances on iOS

On iOS, you can enable encryption for any storage instance that implements the `StorageDelegate` protocol, including all the built-in storage solutions.

Creating a storage instance that uses `SecuredKeyEncryptor`

```swift
let customStorage = KeychainStorage<Dog>(
  account: "myStorageId",
  encryptor: SecuredKeyEncryptor() ?? NoEncryptor()
)
```

The `KeychainStorage` uses the `NoEncryptor` encryptor by default or if not specified.

You can create your own custom encryptor by implementing the `Encryptor` protocol:

Creating a custom encryptor for a storage instance

```swift
struct MyEncryptor: Encryptor {
  func encrypt(data: Data) async throws -> Data {
    // Implement the encryption logic
  }

  func decrypt(data: Data) async throws -> Data {
    // Implement the decryption logic
  }
}
```

## Implementing your own custom storage

You can create your own custom storage solutions by implementing the `Storage` interface:

The `Storage` interface on iOS

```swift
public class CustomStorage<T: Codable>: Storage {
  private var data: T?

  public func save(item: T) async throws {
    data = item
  }

  public func get() async throws → T?  {
    return data
  }

  public func delete() async throws {
    data = nil
  }

}

public class CustomStorageDelegate<T: Codable>: StorageDelegate<T> {
  public init(cacheable: Bool = false) {
    super.init(delegate: CustomStorage<T>(), cacheable: cacheable)
  }
}
```

For example, you could implement a file-based or cloud-based storage solution. You must implement the following functions in each storage class:

* `save()`

  Stores an item in the customized storage.

* `get()`

  Retrieves an item from the customized storage.

* `delete()`

  Removes an item from the customized storage.

Use your custom storage solution in a module as follows:

Using a custom storage solution

```swift
let config = OathConfiguration.build { config in
  config.storage = myCustomStorage()
  config.enableCredentialCache = false
  config.logger = customLogger
}
```

|   |                                                                                                                                                                                                                         |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Use an equals sign when assigning a custom class to the `storage` property in the module configuration.You do not need an equals sign when passing configuration settings to the default storage solution for a module. |

---

---
title: Customizing logging on Android
description: Configure logging in DaVinci Android apps using preset loggers or define custom loggers to control log output and troubleshoot authentication flows
component: orchsdks
page_id: orchsdks:davinci:customization/logging/android-custom-logging
canonical_url: https://developer.pingidentity.com/orchsdks/davinci/customization/logging/android-custom-logging.html
llms_txt: https://developer.pingidentity.com/orchsdks/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["DaVinci", "Android", "Logging", "Debug", "Console"]
section_ids:
  configuring_android_logcat_logging: Configuring Android Logcat logging
  defining_and_using_custom_loggers: Defining and using custom loggers
  android_logger_module: Step 1. Installing modules
  step_2_defining_and_using_custom_loggers: Step 2. Defining and using custom loggers
---

# Customizing logging on Android

[icon: circle-check, set=far]PingOne [icon: android, set=fab]Android

When you develop applications with the Orchestration SDK, you might need to understand its internal workings or troubleshoot unexpected behavior.

Use logging to gain crucial insights into your application's operations, identify issues, verify expected functionality, and better understand authentication flows.

This section covers how to configure and customize the logging output from the Orchestration SDK for Android.

## Configuring Android Logcat logging

To configure the logging output from the Orchestration SDK for Android, specify the logger to use in the client module configuration:

Setting the logging level in the DaVinci client configuration

```kotlin
import com.pingidentity.logger.Logger

val daVinci = DaVinci {
  logger = Logger.STANDARD
  module(Oidc) {
    clientId = "6c7eb89a-66e9-ab12-cd34-eeaf795650b2"
    discoveryEndpoint = "https://auth.pingone.com/3072206d-c6ce-ch15-m0nd-f87e972c7cc3/as/.well-known/openid-configuration"
    scopes = mutableSetOf("openid", "profile", "email", "address", "revoke")
    redirectUri = "com.example.demo://oauth2redirect"
  }
}
```

The Orchestration SDK for Android includes the following logger presets:

| Logger preset | Description                                                        |
| ------------- | ------------------------------------------------------------------ |
| `STANDARD`    | Outputs all log messages to the Android Logcat.                    |
| `WARN`        | Outputs only warning and error log messages to the Android Logcat. |
| `NONE`        | Prevents all log messages.                                         |

|   |                                                                                                                                                                                                                                                                                                 |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The `STANDARD` logger tags messages in Android Logcat with the Orchestration SDK version. You can filter the console to only show the tagged messages:![Filtering Android Logcat output by tag](../../../_images/logger/android-logcat-tag.png)Figure 1. Filtering Android Logcat output by tag |

## Defining and using custom loggers

In addition to the preset loggers you can create your own loggers. For example, you could output Orchestration SDK for Android messages to a file or a third-party service, or filter which messages to display.

### Step 1. Installing modules

To create custom loggers, you need to add the **Logger** module for Android as a dependency to your project:

* `logging`

To install the module into your Android app:

1. In the **Project** tree view of your Android Studio project, open the `build.gradle.kts` file.

2. In the `dependencies` section, add the `logger` module as a dependency:

   ```gradle
   dependencies {
     implementation("com.pingidentity.sdks:logger:2.0.1")
   }
   ```

|   |                                                                        |
| - | ---------------------------------------------------------------------- |
|   | Remember to synchronize your Gradle project after adding dependencies. |

### Step 2. Defining and using custom loggers

To create a custom logger, first define a class and override each of the logger methods with the new behavior.

For example, the following code creates a custom logger named `WARN_ERROR_ONLY`, that only outputs warning and error messages, and ignores both info and debug messages:

Defining a custom logger class on Android

```kotlin
import com.pingidentity.logger.Logger.Companion.logger

open class WarnErrorOnlyLogger : Logger {

    override fun d(message: String) {
    }

    override fun i(message: String) {
    }

    override fun w(message: String, throwable: Throwable?) {
        println("$message: $throwable")
    }

    override fun e(message: String, throwable: Throwable?) {
        println("$message: $throwable")
    }
}

val Logger.Companion.WARN_ERROR_ONLY: Logger by lazy {
    WarnErrorOnlyLogger()
}
```

To use the custom logger in your app, specify the logger's name, just as with the preset loggers:

Using a custom logger for the DaVinci module on Android

```kotlin
val daVinci = DaVinci {
  logger = WARN_ERROR_ONLY
  module(Oidc) {
    clientId = "6c7eb89a-66e9-ab12-cd34-eeaf795650b2"
    discoveryEndpoint = "https://auth.pingone.com/3072206d-c6ce-ch15-m0nd-f87e972c7cc3/as/.well-known/openid-configuration"
    scopes = mutableSetOf("openid", "profile", "email", "address", "revoke")
    redirectUri = "com.example.demo://oauth2redirect"
  }
}
```

---

---
title: Customizing logging on iOS
description: Configure custom logging in your iOS app to capture and route DaVinci SDK log output for debugging and monitoring
component: orchsdks
page_id: orchsdks:davinci:customization/logging/ios-custom-logging
canonical_url: https://developer.pingidentity.com/orchsdks/davinci/customization/logging/ios-custom-logging.html
llms_txt: https://developer.pingidentity.com/orchsdks/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["DaVinci", "iOS", "Logging", "Debug", "Console"]
section_ids:
  configuring_ios_logging: Configuring iOS logging
  defining_and_using_custom_loggers: Defining and using custom loggers
  ios_logger_module: Step 1. Installing modules
  add_dependencies_using_spm_swift_package_manager: Add dependencies using SPM (Swift Package Manager)
  add_dependencies_using_cocoapods: Add dependencies using CocoaPods
  step_2_defining_and_using_custom_loggers: Step 2. Defining and using custom loggers
---

# Customizing logging on iOS

[icon: circle-check, set=far]PingOne [icon: apple, set=fab]iOS

When you develop applications with the Orchestration SDK, you might need to understand its internal workings or troubleshoot unexpected behavior.

Use logging to gain crucial insights into your application's operations, identify issues, verify expected functionality, and better understand authentication flows.

This section covers how to configure and customize the logging output from the Orchestration SDK for iOS.

## Configuring iOS logging

To configure the logging output from the Orchestration SDK for iOS, specify the logger to use in the client module configuration:

Setting the logging level in the DaVinci client configuration

```swift
import PingLogger

let daVinci = DaVinci.createDaVinci { config in
  config.logger = LogManager.standard
  config.module(OidcModule.config) { oidcValue in
    oidcValue.clientId = "6c7eb89a-66e9-ab12-cd34-eeaf795650b2"
    oidcValue.discoveryEndpoint = "https://auth.pingone.com/3072206d-c6ce-ch15-m0nd-f87e972c7cc3/as/.well-known/openid-configuration"
    oidcValue.scopes = ["openid", "profile", "email", "address", "revoke"]
    oidcValue.redirectUri = "com.example.demo://oauth2redirect"
  }
}
```

The Orchestration SDK for iOS includes the following logger presets:

| Logger preset | Description                                                 |
| ------------- | ----------------------------------------------------------- |
| `standard`    | Outputs all log messages to the console.                    |
| `warning`     | Outputs only warning and error log messages to the console. |
| `none`        | Prevents all log messages.                                  |

|   |                                                                                                                                                                                                                                                                             |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The `standard` logger tags messages in the console with the Orchestration SDK version. You can filter the console to only show the tagged messages:![Filtering console output by tag](../../../_images/logger/ios-console-tag.png)Figure 1. Filtering console output by tag |

## Defining and using custom loggers

In addition to the preset loggers you can create your own loggers. For example, you could output Orchestration SDK for Android messages to a file or a third-party service, or filter which messages to display.

### Step 1. Installing modules

To create custom loggers, you need to add the **Logger** module for iOS as a dependency to your project.

You can use Swift Package Manager (SPM) or Cocoapods to add the dependencies to your iOS project.

#### Add dependencies using SPM (Swift Package Manager)

You can install this by using SPM (Swift Package Manager) on the generated iOS project.

1. In Xcode,in the Project Navigator, right-click your project, and then click Add Package Dependencies…​.

2. In the **Search or Enter Package URL** field, enter the URL of the repo containing the DaVinci module for iOS, `https://github.com/ForgeRock/ping-ios-sdk.git`.

3. In **Add to Project**, select the name of your project, and then click **Add Package**.

   Xcode shows a dialog containing the libraries available in the Orchestration SDK for iOS.

4. Select the `PingLogger` library, and in the **Add to Target** column select the name of your project.

5. Repeat the previous step for any other Orchestration SDK libraries you want to add to your project.

6. Click **Add Package**.

   Xcode displays the chosen libraries and any prerequisites they might have in the **Package Dependencies** pane of the Project Navigator:

   ![Package dependencies in the Xcode package navigator pane.](../../_images/Xcode-package-dependencies-dv-client.png)Figure 2. Package dependencies in the Xcode package navigator pane.

#### Add dependencies using CocoaPods

1. If you do not already have CocoaPods, install the [latest version](https://guides.cocoapods.org/using/getting-started.html).

2. If you do not already have a Podfile, in a terminal window, run the following command to create a new [Podfile](https://guides.cocoapods.org/syntax/podfile.html):

   ```
   pod init
   ```

3. Add the following lines to your Podfile:

   ```
   pod 'PingLogger'
   ```

4. Run the following command to install pods:

   ```
   pod install
   ```

### Step 2. Defining and using custom loggers

To create a custom logger, first define a class and override each of the logger methods with the new behavior.

For example, the following code creates a custom logger named `warningErrorOnly`, that only outputs warning and error messages, and ignores both info and debug messages:

Defining a custom logger class on iOS

```swift
import PingLogger

struct WarningErrorOnlyLogger: Logger {

  func i(_ message: String) {
  }

  func d(_ message: String) {
  }

  func w(_ message: String, error: Error?) {
    if let error = error {
      print("\(message): \(error)")
    } else {
      print(message)
    }
  }

  func e(_ message: String, error: Error?) {
    if let error = error {
      print("\(message): \(error)")
    } else {
      print(message)
    }
  }
}

extension LogManager {
  static var warningErrorOnly: Logger {
    return WarningErrorOnlyLogger()
  }
}
```

To use the custom logger in your app, specify the logger's name, just as with the preset loggers:

Using a custom logger with the DaVinci module on iOS

```swift
let daVinci = DaVinci.createDaVinci { config in
  config.logger = warningErrorOnly
  config.module(OidcModule.config) { oidcValue in
    oidcValue.clientId = "6c7eb89a-66e9-ab12-cd34-eeaf795650b2"
    oidcValue.discoveryEndpoint = "https://auth.pingone.com/3072206d-c6ce-ch15-m0nd-f87e972c7cc3/as/.well-known/openid-configuration"
    oidcValue.scopes = ["openid", "profile", "email", "address", "revoke"]
    oidcValue.redirectUri = "com.example.demo://oauth2redirect"
  }
}
```

---

---
title: Customizing logging on JavaScript
description: Configure logging levels and custom logger functions in the Orchestration SDK for JavaScript to redirect or filter SDK output
component: orchsdks
page_id: orchsdks:davinci:customization/logging/javascript-custom-logging
canonical_url: https://developer.pingidentity.com/orchsdks/davinci/customization/logging/javascript-custom-logging.html
llms_txt: https://developer.pingidentity.com/orchsdks/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["DaVinci", "JavaScript", "Logging", "Debug", "Console"]
section_ids:
  configuring_javascript_logging: Configuring JavaScript logging
  customize-logger-javascript: Customizing JavaScript logging
---

# Customizing logging on JavaScript

[icon: circle-check, set=far]PingOne [icon: js, set=fab]JavaScript

When you develop applications with the Orchestration SDK, you might need to understand its internal workings or troubleshoot unexpected behavior.

Use logging to gain crucial insights into your application's operations, identify issues, verify expected functionality, and better understand authentication flows.

This section covers how to configure and customize the logging output from the Orchestration SDK for JavaScript.

## Configuring JavaScript logging

To configure the logging output from the Orchestration SDK for JavaScript, inside the `logger` object, specify the level to use for logging in the `level` property in the client module configuration:

Setting the logging level in the DaVinci client configuration

```javascript
const davinciClient = await davinci({
  logger: {
    level: 'warn',
  },
  config: {
    clientId: '6c7eb89a-66e9-ab12-cd34-eeaf795650b2',
    serverConfig: {
      wellknown: 'https://auth.pingone.com/3072206d-c6ce-ch15-m0nd-f87e972c7cc3/as/.well-known/openid-configuration',
      timeout: 3000,
    },
    scope: '"openid", "email", "address", "profile", "phone"',
    responseType: 'code',
  },
});
```

The Orchestration SDK for JavaScript supports the following logger levels:

| Level   | Priority | Description                                                                          |
| ------- | -------- | ------------------------------------------------------------------------------------ |
| `none`  | `-1`     | Does not output any log messages.                                                    |
| `error` | `0`      | Log messages describing errors that have occurred.                                   |
| `warn`  | `1`      | Log messages detailing possible issues that aren't yet errors.                       |
| `info`  | `3`      | Log messages for expected activities during regular usage.This is the default value. |
| `debug` | `4`      | Log messages intended only for development and troubleshooting.                      |

The Orchestration SDK outputs messages that have a priority equal to, or less than your chosen level.

For example, if you set the level to `warn`, the module outputs `warn` and `error` messages.

## Customizing JavaScript logging

The Orchestration SDK for JavaScript allows developers to customize the default logger behavior. For example, you might want to redirect the logs to an external service, or pipe them to a file.

To customize how the Orchestration SDK outputs logger messages:

1. Create a function that implements the `LoggerFunctions` interface.

   For example, the following code adds a prefix to output from the SDK before logging it to the console:

   ```javascript
   const customLogger = {
     error: (...args) => console.error(`[Ping SDK Error]:`, ...args),
     warn: (...args) => console.warn(`[Ping SDK Warning]:`, ...args),
     info: (...args) => console.info(`[Ping SDK Info]:`, ...args),
     debug: (...args) => console.debug(`[Ping SDK Debug]:`, ...args)
   };
   ```

   The signature of the interface defaults to the following:

   `(...msgs: unknown[]) => void`

2. Specify the custom logger to use in the `custom` property in the `logger` object of your client module configuration:

   Setting the logging level in the DaVinci client configuration

   ```javascript
   const davinciClient = await davinci({
     logger: {
       level: 'debug',
       custom: customLogger,
     },
     config: {
       clientId: '6c7eb89a-66e9-ab12-cd34-eeaf795650b2',
       serverConfig: {
         wellknown: 'https://auth.pingone.com/3072206d-c6ce-ch15-m0nd-f87e972c7cc3/as/.well-known/openid-configuration',
         timeout: 3000,
       },
       scope: '"openid", "email", "address", "profile", "phone"',
       responseType: 'code',
     },
   });
   ```

The Orchestration SDK redirects its logging output to your custom logger:

![Custom logger output in the Chrome developer console.](../../../_images/logger/chrome-console-custom-logger.png)Figure 1. Custom logger output in the Chrome developer console.

|   |                                                                                                                                                                                                                                                           |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | You might need to adjust the default console output filters in your browser's developer console, to view output from the Orchestration SDK.For example, to view `debug` level messages in Chrome, make sure you enable **Verbose** output in the console. |