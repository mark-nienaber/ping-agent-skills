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
