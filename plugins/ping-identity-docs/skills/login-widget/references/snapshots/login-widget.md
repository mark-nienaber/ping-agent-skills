---
title: API reference
description: This page lists the modules that the Advanced Identity Cloud/PingAM Login Widget provides for use in your apps.
component: login-widget
page_id: login-widget:login-widget:widget-api-reference
canonical_url: https://developer.pingidentity.com/login-widget/login-widget/widget-api-reference.html
revdate: Mon, 3 Jul 2023 18:00:37 +0100
keywords: ["Source Code", "Integration"]
section_ids:
  widget-api: Widget
  configuration-api: Configuration
  config-content: Content configuration options
  config-links: Links configuration options
  config-style: Style configuration options
  add_a_header_section: Add a header section
  config-journeys-map: Journeys configuration options
  component-api: Component
  schema_for_component_events: Schema for component events
  journey-api: Journey
  schema_for_journey_events: Schema for journey events
  user-api: User
  schema_for_user_info_events: Schema for user.info events
  schema_for_user_tokens_events: Schema for user.tokens events
  request-wrapper: Request
---

# API reference

This page lists the modules that the Advanced Identity Cloud/PingAM Login Widget provides for use in your apps.

## Widget

This is a compiled Svelte class. This is what instantiates the component, mounts it to the DOM, and sets up all the event listeners.

```javascript
import Widget from '@forgerock/login-widget';

// Instantiate Widget
const widget = new Widget({
  target: widgetRootEl, // REQUIRED; Element mounted in DOM
  props: {
    type: 'modal', // OPTIONAL; "modal" or "inline"; "modal" is default
  },
});

// OPTIONAL; Remove widget from DOM and destroy component listeners
widget.$destroy();
```

|   |                                                                                                                                                                                                                                                                                                                                                                                                           |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Call `$destroy()` if you instantiate the Advanced Identity Cloud/PingAM Login Widget within a part of your application frequently created and destroyed.We strongly encourage you to instantiate the modal form factor of the Advanced Identity Cloud/PingAM Login Widget high up in your application code. Instantiate it close to the top-level file in a component that is created once and preserved. |

## Configuration

The Advanced Identity Cloud/PingAM Login Widget requires information about the server instance it connects to, as well as OAuth 2.0 client configuration and other settings.

For information on setting up your server for use with the Advanced Identity Cloud/PingAM Login Widget, refer to [Prerequisites](tutorial.html#_prerequisites).

To provide these settings, import and use the `configuration` module and its `set()` method.

The Advanced Identity Cloud/PingAM Login Widget uses the same underlying configuration properties as the main SDK.

```javascript
import { configuration } from '@forgerock/login-widget';

const myConfig = configuration();
myConfig.set({
  forgerock: {
    /**
     * REQUIRED; SDK configuration object
     */
    serverConfig: {
      baseUrl: 'https://openam-forgerock-sdks.forgeblocks.com/am',
      timeout: 3000, // Number (in milliseconds); 3 to 5 seconds should be fine
    },
    /**
     * OPTIONAL, *BUT ENCOURAGED*, CONFIGURATION
     * Remaining config is optional with fallback values shown
     */
    clientId: 'sdkPublicClient', // String; defaults to 'WebLoginWidgetClient'
    realmPath: 'alpha', // String; defaults to 'alpha'
    redirectUri: window.location.href, // URL string; defaults to `window.location.href`
    scope: 'openid profile email address', // String; defaults to 'openid email'
  },
  /**
   * OPTIONAL; Pass custom content
   */
  content: {},
  /**
   * OPTIONAL; Provide link for terms and conditions page
   */
  links: {},
  /**
   * OPTIONAL; Provide style configuration
   */
  style: {},
  /**
   * OPTIONAL; Map HREFs to journeys or trees
   */
  journeys: {},
});
```

### Content configuration options

Use the `content` configuration element to pass custom text content to the Advanced Identity Cloud/PingAM Login Widget, replacing its default values.

You can use this method to localize user interface text for different regions. Learn more in [Localizing the widget](customize/localize.html).

Example `content` configuration

```javascript
const myConfig = configuration();

myConfig.set({
     content: {
        "userName": "Identifier",
        "passwordCallback": "Passphrase",
        "nextButton": "Let's go!",
    },
});
```

![law config custom content en](../_images/LAW/law-config-custom-content-en.png)Figure 1. Result of example content configuration

For a list of the content you can override, refer to the [en-us locale file](https://github.com/ForgeRock/forgerock-web-login-framework/blob/beta/src/locales/us/en/index.json) in the Advanced Identity Cloud/PingAM Web Login Framework repository.

### Links configuration options

Use the `links` configuration element to set the full canonical URL to your terms and conditions page.

This should be a page hosted on your website or elsewhere within your app. Users are sent to this URL if they click to view the terms and conditions in the Advanced Identity Cloud/PingAM Login Widget.

This supports the `TermsAndConditionsCallback` often used in registration journeys.

Example `links` configuration

```javascript
const myConfig = configuration();

myConfig.set({
    links: {
        termsAndConditions: 'https://example.com/terms',
    },
});
```

### Style configuration options

Use the `style` configuration element to configure the look and feel of the Advanced Identity Cloud/PingAM Login Widget. This allows you to choose the type of labels used or provide a logo for the modal.

![modal theme params en](../_images/LAW/modal-theme-params-en.png)Figure 2. Use the `style` property to control aspects of the display

*Key*:

1. Use `style/logo` to add images for use in dark or light modes

2. Set `style/stage/icon` to `true` to render UI specific to certain stage parameter values. Supported stage values are:

   * `OneTimePassword` - enable the Advanced Identity Cloud/PingAM Login Widget to display one-time password entry forms correctly.

   * `DefaultRegistration` - adds UI elements to the display most suitable for user self-registration forms.

   * `DefaultLogin` - adds UI elements to the display most suitable for user log in forms.

3. A section that displays the Page Header and Page Description fields from the page node configuration

4. To float labels above their respective fields, set `style/labels` to `floating`

Adding logos and enabling icons

```javascript
const myConfig = configuration();

myConfig.set({
  style: {
    checksAndRadios: 'animated', // OPTIONAL; choices are 'animated' or 'standard'
    labels: 'floating', // OPTIONAL; choices are 'floating' or 'stacked'
    logo: {
      // OPTIONAL; only used with modal form factor
      dark: 'https://example.com/img/white-logo.png', // OPTIONAL; used if theme has a dark variant
      light: 'https://example.com/img/black-logo.png', // REQUIRED if logo property is provided; full URL
      height: 300, // OPTIONAL; number of pixels for providing additional controls to logo display
      width: 400, // OPTIONAL; number of pixels for providing additional controls to logo display
    },
    sections: {
      // OPTIONAL; only used with modal form factor
      header: false, // OPTIONAL; separate the logo section from the rest of the modal
    },
    stage: {
      icon: true, // OPTIONAL; displays generic icons for the provided stages
    },
  },
});
```

|   |                                                                                                  |
| - | ------------------------------------------------------------------------------------------------ |
|   | The `logo` and `sections` properties only apply to the "modal" form factor and not the "inline". |

#### Add a header section

Enabling the header section separates the logo or branding from the journey form.

If you set `header: true` within the `style/sections` property, the modal uses a section with a separating line, and extra space:

![modal widget with header](../_images/android/modal-widget-with-header.png)Figure 3. Modal form factor with header enabled

By default, the separating section is not enabled:

![modal widget without header](../_images/android/modal-widget-without-header.png)Figure 4. Default modal form factor with header disabled

### Journeys configuration options

Use the `journeys` configuration element to map HREF values rendered within the Advanced Identity Cloud/PingAM Login Widget to start a journey or authentication tree instead of visiting the URL.

![law href to journey mapping en](../_images/LAW/law-href-to-journey-mapping-en.png)Figure 5. Example HREF values in a page node

The Advanced Identity Cloud/PingAM Login Widget listens for click events on elements rendered within its container and compares the HREF to the configured mappings. If there is a match, it prevents the default action of visiting the URL and starts the journey configured in the mapping.

Mapping HREF strings to a journey

```javascript
config.set({
  forgerock: {
    // SDK config
  },
  journeys: {
    forgetCookie: { // Any string, as long as it's not overriding a default mapping
      journey: 'ForgetCookie', // Must match actual journey name in the {fr_server}
      match: [ '#/service/ForgetCookie' ], // Array of strings that match `HREF` values (case-sensitive)
    }
  }
});
```

The Advanced Identity Cloud/PingAM Login Widget has mappings configured internally to handle the links displayed in page nodes by default. These map the HREF values that are displayed by an out-of-the-box page node to corresponding journeys in an PingOne Advanced Identity Cloud tenant. You can override the mappings if required or add your own.

Default HREF strings to journey mappings

```javascript
forgotPassword: {
    journey: 'ResetPassword',
    match: ['#/service/ResetPassword', '?journey=ResetPassword'],
},
forgotUsername: {
    journey: 'ForgottenUsername',
    match: ['#/service/ForgottenUsername', '?journey=ForgottenUsername'],
},
login: {
    journey: 'Login',
    match: ['#/service/Login', '?journey', '?journey=Login'],
},
register: {
    journey: 'Registration',
    match: ['#/service/Registration', '?journey=Registration'],
},
```

## Component

Use the `component` module for subscribing to modal and inline form factor events and for opening and controlling the modal form factor.

Call the `component()` method and assign the result to a variable to receive the observable. Subscribe to the observable to listen and react to the state of the Advanced Identity Cloud/PingAM Login Widget component.

```javascript
import { component } from '@forgerock/login-widget';

// Initiate the component API
const componentEvents = component();

// Know when the component, both modal and inline has been mounted.
// When using the modal type, you will also receive open and close events.
// The property `reason` will be either "auto", "external", or "user"

const unsubComponentEvents = componentEvents.subscribe((event) => {
    /* Run anything you want */
});

// Open the modal
componentEvents.open();

// Close the modal
componentEvents.close();

// Recommended: call when your UI component is destroyed
unsubComponentEvents();
```

### Schema for `component` events

The schema for `component` events is as follows:

Schema for `component` events

```javascript
{
    lastAction: null, // null or the most recent action; one of `close`, `open`, or `mount`
    error: null, // null or object with `code`, `message`, and `step` that failed
    mounted: false, // boolean
    open: null, // boolean for the modal form factor, or null for inline form factor
    reason: null, // string to describe the reason for the event
    type: null, // 'modal' or 'inline'
}
```

Use the `reason` value to determine why the modal has closed.

The possible `reason` values are:

* `user`

  The user closed the dialog within the UI

* `auto`

  The modal was closed because the user successfully authenticated

* `external`

  The application called the `close()` function

## Journey

Use the `journey` module to manage interaction with authentication and self-service journeys.

```javascript
import { journey } from '@forgerock/login-widget';

// Call to start the journey
// Optional config can be passed in, see below for more details
const journeyEvents = journey({
  oauth: true, // OPTIONAL; defaults to true; uses OAuth flow for acquiring tokens
  user: true, // OPTIONAL; default to true; returns user information from `userinfo` endpoint
});

// Start a journey
journeyEvents.start({
  forgerock: {}, // OPTIONAL; configuration overrides
  journey: 'Login', // OPTIONAL; specify the journey or tree you want to use
  resumeUrl: window.location.href, // OPTIONAL; the full URL for resuming a tree
  recaptchaAction: 'myCaptchaTag', // OPTIONAL; tag v3 reCAPTCHAs. Fallback to journey name.
  pingProtect: { // Set manually, or obtain from `PingOneProtectInitializeCallback` callback.
    // REQUIRED; Your {p1_name} environment identifier.
    envId: '3072206d-c6ce-4c19-a366-f87e972c7cc3',
    // OPTIONAL; When `true`, collect behavioral data.
    behavioralDataCollection: true,
    // OPTIONAL; When `true`, output SDK log messages in the developer console.
    consoleLogEnabled: false,
  },
});

// Subscribe to journey events
const unsubJourneyEvents = journeyEvents.subscribe((event) => {
  /* Run anything you want */
});

// Recommended: call when your UI component is destroyed
unsubJourneyEvents();
```

### Schema for `journey` events

The schema for `journey` events is as follows:

Schema for `journey` events

```javascript
{
  journey: {
    completed: false, // boolean
    error: null, // null or object with `code`, `message`, and `step` that failed
    loading: false, // boolean
    step: null, // null or object with the last step object from the server
    successful: false, // boolean
    response: null, // null or object if successful containing the success response from the server
  },
  oauth: {
    completed: false, // boolean
    error: null, // null or object with `code` and `message` properties
    loading: false, // boolean
    successful: false, // boolean
    response: null, // null or object with OAuth/OIDC tokens
  },
  user: {
    completed: false, // boolean
    error: null, // null or object with `code` and `message` properties
    loading: false, // boolean
    successful: false, // boolean
    response: null, // null or object with user information driven by OAuth scope config
  },
}
```

## User

Use the `user` module to access methods for managing users:

* `user.info`

* `user.tokens`

* `user.logout`

The `user.info` and `user.tokens` methods requires use of OAuth 2.0. The `user.info` method also requires a scope value of `openid`.

The Advanced Identity Cloud/PingAM Login Widget is configured to use both requirements by default.

You can use the `user.logout` method with both OAuth 2.0 and session-based authentication.

```javascript
import { user } from '@forgerock/login-widget';

/**
 * User info API
 */
const userEvents = user.info();

// Subscribe to user info changes
const unsubUserEvents = userEvents.subscribe((event) => {
  // Return current, *local*, user info and future state changes
  console.log(event);
});

// Fetch/get fresh user info from the server
userEvents.get(); // New state is returned in your `userEvents.subscribe` callback function

/**
 * User tokens API
 */
const tokenEvents = user.tokens();

// Subscribe to user token changes
const unsubTokenEvents = tokenEvents.subscribe((event) => {
  // Return current, *local*, user tokens and future state changes
  console.log(event);
});

// Return existing user tokens if available and not expired or about to expire
// Otherwise obtain fresh ones from the server
tokenEvents.get(); // State is returned in your `tokenEvents.subscribe` callback function

/**
 * Logout
 * Log user out and clear user data (info and tokens)
 */
user.logout(); // Resets user and emits event to your info and tokens' `.subscribe` callback function

// Recommended: call when your UI component is destroyed
unsubUserEvents();
unsubTokenEvents();
```

You can use `get()` with both `user.info` and `user.tokens` to obtain the user's profile or OAuth 2.0 tokens. The `get()` function maps to the following methods in the Ping (ForgeRock) SDK for JavaScript, and support the same parameters:

* `userEvents.get()` = `UserManager.getCurrentUser()`

* `tokenEvents.get()` = `TokenManager.getTokens()`

For example, when getting a user's tokens you can force the Advanced Identity Cloud/PingAM Login Widget to obtain fresh tokens from the server as follows:

```javascript
tokenEvents.get({forceRenew: true});
```

Refer to the [Ping (ForgeRock) SDK for JavaScript API reference](https://developer.pingidentity.com/reference/sdks/javascript/api-reference-core-4-9/index.html) for more information.

### Schema for `user.info` events

The schema for `user.info` events is as follows:

Schema for `user.info` events

```javascript
{
    completed: false, // boolean
    error: null,  // null or object with `code`, `message`, and `step` that failed
    loading: false, // boolean
    successful: false, // boolean
    response: null, // object returned from the `/userinfo` endpoint
}
```

### Schema for `user.tokens` events

The schema for `user.tokens` events is as follows:

Schema for `user.tokens` events

```javascript
{
    completed: false, // boolean
    error: null,  // null or object with `code`, `message`, and `step` that failed
    loading: false, // boolean
    successful: false, // boolean
    response: null, // object returned from the `/access_token` endpoint
}
```

## Request

The Advanced Identity Cloud/PingAM Login Widget has an alias to the Ping (ForgeRock) SDK for JavaScript's `HttpClient.request` method, which is a convenience wrapper around the native `fetch`. This method will auto-inject the access token into the `Authorization` header and manage some of the lifecycle around the token.

```javascript
import { request } from '@forgerock/login-widget';

const response = await request({ init: { method: 'GET' }, url: 'https://protected.resource.com' });
```

The full `options` object:

```javascript
{
  bypassAuthentication: false, // Boolean; if true, the access token is not injected into the `Authorization` header
  init: {
    // Options object for `fetch` API: https://developer.mozilla.org/en-US/docs/Web/API/fetch
  },
  timeout: 3000, // Fetch timeout in milliseconds
  url: 'https://protected.resource.com', // String; the URL of the resource

  // Unsupported properties
  authorization: {},
  requiresNewToken: () => {},
}
```

For more information, refer to the [HttpClient reference documentation](https://developer.pingidentity.com/reference/sdks/javascript/api-reference-core-4-9/classes/http-client.HttpClient.html).

---

---
title: Customizing the Advanced Identity Cloud/PingAM Login Widget
description: The Advanced Identity Cloud/PingAM Login Widget is designed to be flexible and can be customized to suit many different situations.
component: login-widget
page_id: login-widget:login-widget:customize/index
canonical_url: https://developer.pingidentity.com/login-widget/login-widget/customize/index.html
revdate: Tue, 25 Mar 2025 11:00:37 +0100
keywords: ["PingOne Advanced Identity Cloud", "PingAM", "Journeys", "Setup &amp; Configuration", "Source Code", "Use Case", "SDK", "IdP"]
section_ids:
  localization: Localization
  theming: Theming
---

# Customizing the Advanced Identity Cloud/PingAM Login Widget

The **Advanced Identity Cloud/PingAM Login Widget** is designed to be flexible and can be customized to suit many different situations.

Learn more about customizing the widget in the sections below:

## [Localization](localize.html)

Alter the default text that appears in the Advanced Identity Cloud/PingAM Login Widget, including how to respond to different locales.

[**Read more**[icon: chevrons-right, set=fas, size=xs]](localize.html)

## [Theming](theme.html)

Learn how to alter the default light and dark themes by using the Tailwind configuration file.

[**Read more**[icon: chevrons-right, set=fas, size=xs]](theme.html)

---

---
title: Implement a CAPTCHA
description: The Advanced Identity Cloud/PingAM Login Widget supports the use of a CAPTCHA (Completely Automated Public Turing test to tell Computers and Humans Apart), which helps to prevent automated scripts from attempting to authenticate to your servers.
component: login-widget
page_id: login-widget:login-widget:use-cases/how-to-captcha
canonical_url: https://developer.pingidentity.com/login-widget/login-widget/use-cases/how-to-captcha.html
revdate: Wed, 4 July 2024 11:27:20 +0100
keywords: ["Integration", "Journeys", "Features", "Social Authentication", "Standards"]
section_ids:
  supported_captcha_variants: Supported CAPTCHA variants
  configure_your_app: Configure your app
  test_a_captcha: Test a CAPTCHA
  troubleshooting: Troubleshooting
---

# Implement a CAPTCHA

The Advanced Identity Cloud/PingAM Login Widget supports the use of a CAPTCHA (Completely Automated Public Turing test to tell Computers and Humans Apart), which helps to prevent automated scripts from attempting to authenticate to your servers.

To use a CAPTCHA in the Advanced Identity Cloud/PingAM Login Widget, add the [CAPTCHA node](https://docs.pingidentity.com/auth-node-ref/latest/captcha.html) to your authentication journey.

## Supported CAPTCHA variants

Advanced Identity Cloud/PingAM Login Widget supports the following CAPTCHA variants:

| CAPTCHA variant                                                                         | Support                                                                                                          |
| --------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| [hCaptcha](https://www.hcaptcha.com/)                                                   | [icon: check, set=fa]Active[icon: times, set=fa]Passive / 99% Passive[icon: times, set=fa]Invisible              |
| [reCAPTCHA v2](https://developers.google.com/recaptcha/docs/display)                    | [icon: minus, set=fa]Full, except [Invisible reCAPTCHA](https://developers.google.com/recaptcha/docs/invisible). |
| [reCAPTCHA v3](https://developers.google.com/recaptcha/docs/v3)                         | [icon: check, set=fa]Full                                                                                        |
| [reCAPTCHA Enterprise](https://cloud.google.com/security/products/recaptcha-enterprise) | [icon: times, set=fa]Not currently supported                                                                     |

## Configure your app

The Advanced Identity Cloud/PingAM Login Widget cannot inject the scripts necessary to use a CAPTCHA in your app.

You must add the relevant scripts yourself, usually to the `<head>` of the page:

* **hCaptcha**

  If you are using hCaptcha with the Advanced Identity Cloud/PingAM Login Widget, you must first have the JavaScript loaded into your app's DOM:

  ```html
  <script src="https://js.hcaptcha.com/1/api.js" async defer></script>
  ```

* **reCAPTCHA v2**

  If you are using Google reCAPTCHA v2 with the Advanced Identity Cloud/PingAM Login Widget, you must first have the JavaScript loaded into your app's DOM:

  ```html
  <script async src="https://www.google.com/recaptcha/api.js"></script>
  ```

* **reCAPTCHA v3**

  If you are using Google reCAPTCHA v3, you must append your site key in a query string parameter named `render`:

  ```html
  <script async src="https://www.google.com/recaptcha/api.js?render={reCAPTCHA_site_key}"></script>
  ```

  When calling a journey that uses reCAPTCHA v3 you can add a `recaptchaAction` property with a custom value. That value tags the event in the reCAPTCHA console so that you can track different usage:

  ```javascript
  journey.start({
      journey: 'reCAPTCHAv3journey',
      // …​.any other journey config required…​.
      recaptchaAction: 'loginVIPArea', // reCAPTCHA v3 only, falls back to journey name
  });
  ```

  If you do not provide a `recaptchaAction` value, the SDK attempts to use the name of the journey instead, if available.

## Test a CAPTCHA

With your app configured and the necessary scripts in place, you can visit any journey that contains a [CAPTCHA node](https://docs.pingidentity.com/auth-node-ref/latest/captcha.html) to test a CAPTCHA with the Advanced Identity Cloud/PingAM Login Widget.

For example, the following image shows how the Advanced Identity Cloud/PingAM Login Widget handles a CAPTCHA node alongside a platform username and platform password nodes, all within a single page node:

![Login Widget handling reCAPTCHA v2 in a page node](../../_images/login-widget-reCAPTCHAv2-en.png)Figure 1. Login Widget handling reCAPTCHA v2 in a page node

## Troubleshooting

This section contains information on how to diagnose issues when using a CAPTCHA with the Advanced Identity Cloud/PingAM Login Widget.

* Why does the reCAPTCHA display "ERROR for site owner: Invalid key type"?

  Ensure the site key you have specified in the [CAPTCHA node](https://docs.pingidentity.com/auth-node-ref/latest/captcha.html) is configured for the version of reCAPTCHA type you want to use.

  For example, the following image shows a configuration for v2 Tickbox:

  ![recaptcha v2 google settings en](../../_images/recaptcha-v2-google-settings-en.png)

  When using a v2 site key, do not select ReCaptcha V3 Node in the CAPTCHA node configuration.

* Why does the browser console display "Error: Invalid site key or not loaded in api.js"?

  Ensure you have added the correct site key value as a `render` query parameter of the Google `api.js` script.

  For example:

  ```html
  <script async src="https://www.google.com/recaptcha/api.js?render=1249672216234"></script>
  ```

* Why does the reCAPTCHA display "Localhost is not in the list of supported domains for this site key."?

  The `localhost` domain is blocked from working with reCAPTCHA by default.

  You can add the domain to the site key configuration for testing purposes if required.

  |   |                                                                                |
  | - | ------------------------------------------------------------------------------ |
  |   | It can take several minutes for changes to the allowed domains to take effect. |

  For more information, refer to [Google's reCAPTCHA documentation](https://developers.google.com/recaptcha/docs/faq#localhost_support).

---

---
title: Implement your use cases with the Advanced Identity Cloud/PingAM Login Widget
description: Find out how to achieve some common use case scenarios using the Advanced Identity Cloud/PingAM Login Widget.
component: login-widget
page_id: login-widget:login-widget:use-cases
canonical_url: https://developer.pingidentity.com/login-widget/login-widget/use-cases.html
revdate: Wed, 17 May 2023 14:10:20 +0100
keywords: ["Integration", "Features"]
---

# Implement your use cases with the Advanced Identity Cloud/PingAM Login Widget

Find out how to achieve some common use case scenarios using the Advanced Identity Cloud/PingAM Login Widget.

* [Log in with social authentication](use-cases/how-to-social-login.html)

  Social authentication provides your users with a choice of ways to sign in that suits them.

  Select from supported social providers in a journey to initiate an OAuth 2.0 flow to authenticate with the social provider, before returning to the original journey.

* [Log in with OATH one-time passwords](use-cases/how-to-oath-otp.html)

  If your users have registered the ForgeRock Authenticator for one-time passwords using a browser for example, then an app using the Advanced Identity Cloud/PingAM Login Widget will be able to accept the one-time password from the authenticator app.

* [Implement a CAPTCHA](use-cases/how-to-captcha.html)

  Help to prevent automated scripts from attempting to authenticate to your servers by implementing a CAPTCHA in your Advanced Identity Cloud/PingAM Login Widget app.

* [Suspend journeys with "magic links"](use-cases/how-to-magic-links.html)

  You can use the Email Suspend Node within your journeys to support a number of authentication experiences, including verifying a user's email address, building a "forgot password" flow, or using an email address for multifactor authentication.

---

---
title: Integrate the Advanced Identity Cloud/PingAM Login Widget into a React app
description: In this tutorial, you will learn how to integrate the Advanced Identity Cloud/PingAM Login Widget into a simple React app that you scaffold using Vite.
component: login-widget
page_id: login-widget:login-widget:integrations/how-integrate-with-react
canonical_url: https://developer.pingidentity.com/login-widget/login-widget/integrations/how-integrate-with-react.html
revdate: Wed, 17 May 2023 14:10:20 +0100
keywords: ["Integration", "Third-Party", "Framework"]
section_ids:
  requirements: Requirements
  configure_your_server: Configure your server
  create_a_vite_app: Create a Vite app
  install_the_advanced_identity_cloudpingam_login_widget: Install the Advanced Identity Cloud/PingAM Login Widget
  prepare_the_html: Prepare the HTML
  prepare_the_css: Prepare the CSS
  import_and_configure_the_advanced_identity_cloudpingam_login_widget: Import and configure the Advanced Identity Cloud/PingAM Login Widget
  instantiate_and_mount_the_advanced_identity_cloudpingam_login_widget: Instantiate and mount the Advanced Identity Cloud/PingAM Login Widget
  controlling_the_component: Controlling the component
  calling_the_authorization_server: Calling the authorization server
  authenticating_a_user: Authenticating a user
  logging_a_user_out: Logging a user out
---

# Integrate the Advanced Identity Cloud/PingAM Login Widget into a React app

In this tutorial, you will learn how to integrate the Advanced Identity Cloud/PingAM Login Widget into a simple React app that you scaffold using Vite.

You install the Advanced Identity Cloud/PingAM Login Widget using `npm`, add an element to the HTML file for mounting the modal form factor, and wrap the app's CSS in a layer.

With the app prepared, you then import and instantiate various components of the Advanced Identity Cloud/PingAM Login Widget to start a journey. You subscribe to the events the Advanced Identity Cloud/PingAM Login Widget emits so that the app can respond and display the appropriate UI.

When you have successfully authenticated a user, you add code to log the user out and invalidate their tokens, as well as update the UI to alter the button state.

## Requirements

1. Node 18+

2. NPM 8+

## Configure your server

Configure your PingOne Advanced Identity Cloud or self-managed PingAM server by following the steps in the [Advanced Identity Cloud/PingAM Login Widget Tutorial](../tutorial.html#_prerequisites).

* When creating the OAuth 2.0 client, add the URL that you are using to host the app to the Sign-In URLs property.

  |   |                                                                                                                   |
  | - | ----------------------------------------------------------------------------------------------------------------- |
  |   | The URL is output to the console when you run the `npm run dev` command, and defaults to `http://localhost:5173/` |

* If your instance has the default Login journey, you can use that instead of creating a new journey as described in the tutorial.

## Create a Vite app

1. In a terminal window, create a Vite app with React as the template:

   ```shell
   npm create vite@latest login-widget-react-demo -- --template react
   ```

   For more information, refer to [Scaffolding Your First Vite Project](https://vitejs.dev/guide/#scaffolding-your-first-vite-project) in the Vite developer documentation.

2. When completed, change to the new directory, for example `login-widget-react-demo`, and then install dependencies with `npm`:

   ```shell
   npm install
   ```

3. Run the app in developer mode:

   ```shell
   npm run dev
   ```

4. In a web browser, open the URL output by the previous command to render the app. The URL is usually `http://localhost:5173`

   ![law react vite app en](../../_images/LAW/law-react-vite-app-en.png)Figure 1. Example Vite + React app

|   |                                                                                                                                                                                                                                      |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | Use a different browser for development testing than the one you use to log into PingOne Advanced Identity Cloud or PingAM.This prevents admin user and test user sessions colliding and causing unexpected authentication failures. |

## Install the Advanced Identity Cloud/PingAM Login Widget

In a new terminal window, install the Advanced Identity Cloud/PingAM Login Widget using `npm`:

```shell
npm install @forgerock/login-widget
```

## Prepare the HTML

In your preferred IDE, open the directory where you created the Vite app, and then open the `index.html` file.

To implement the modal form factor, create a root element to contain the Advanced Identity Cloud/PingAM Login Widget.

Add `<div id="widget-root"></div>` toward the bottom of the `<body>` element but before the `<script>` tag:

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <link rel="icon" type="image/svg+xml" href="/vite.svg" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Vite + React</title>
  </head>
  <body>
    <div id="root"></div>
    <!-- Widget mount point -->
    <div id="widget-root"></div>
    <script type="module" src="/src/main.jsx"></script>
  </body>
</html>
```

## Prepare the CSS

You should wrap the app's CSS using `@layer`. This helps control the CSS cascade.

To wrap the app's CSS, in your IDE, open `src/index.css` and `src/App.css` and wrap them both with the following code:

```css
@layer app {
    /* existing styles */
    #root {
        max-width: 1280px;
        margin: 0 auto;
        padding: 2rem;
        text-align: center;
    }

    .logo {
        height: 6em;
        padding: 1.5em;
        will-change: filter;
        transition: filter 300ms;
    }
    /* ... */
}
```

You can then specify the order of the various layers as follows:

```html
<style>
  @layer app;
  /* List the Widget layers last */
  @layer 'fr-widget.base';
  @layer 'fr-widget.utilities';
  @layer 'fr-widget.components';
  @layer 'fr-widget.variants';
</style>
```

## Import and configure the Advanced Identity Cloud/PingAM Login Widget

In your IDE, open the top-level application file, often called `App.jsx`.

Import the `Widget` class, the `configuration` module, and the CSS:

```javascript
import Widget, { configuration } from '@forgerock/login-widget';
import '@forgerock/login-widget/widget.css';
```

Add a call to the `configuration` method within your `App` function component and save off the return value to a `config` variable for later use.

This internally prepares the `Widget` for use.

```javascript
function App() {
  const [count, setCount] = useState(0);

  // Initiate all the Widget modules
  const config = configuration();

  // ...
```

## Instantiate and mount the Advanced Identity Cloud/PingAM Login Widget

To continue, you need to import `useEffect` from the React library. This is to control the execution of a number of statements you are going to write.

After importing `useEffect`, write it into the component with an empty dependency array:

```javascript
import React, { useEffect, useState } from 'react';

// ...

function App() {

  // ...

  useEffect(() => {}, []);

  // ...
```

|   |                                                                                                              |
| - | ------------------------------------------------------------------------------------------------------------ |
|   | The empty dependency array is to tell React this has no dependencies at this point and should only run once. |

Now that you have the `useEffect` written, follow these steps:

1. Instantiate the `Widget` class within `useEffect`

2. In the arguments, pass an object with a `target` property that specifies the DOM element you created in an earlier step

3. Assign its return value to a `widget` variable

4. Return a function that calls `widget.$destroy()`

```javascript
useEffect(() => {
  const widget = new Widget({ target: document.getElementById('widget-root') });

  return () => {
    widget.$destroy();
  };
}, []);
```

|   |                                                                                                                                                            |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The reason for the returned function is for proper clean up when the React component unmounts.If it remounts, you do not get two widgets added to the DOM. |

In your browser, the app doesn't look any different. This is because the Widget, by default, is invisible at startup.

To ensure it is working as expected, inspect the DOM in the browser developer tools.

Open the `<div id="widget-root">` element in the DOM, and you should see the Advanced Identity Cloud/PingAM Login Widget mounted within it:

![law react instantiated en](../../_images/LAW/law-react-instantiated-en.png)Figure 2. Instantiated and mounted modal form factor

## Controlling the component

An invisible Advanced Identity Cloud/PingAM Login Widget is not all that useful, so your next task is to pull in the `component` module to manage the component's events.

1. Add the `component` module to the list of imports from the `@forgerock/login-widget`

2. Call the `component` function just under the `configuration` function

3. Assign its return value to a `componentEvents` variable:

```javascript
import Widget, { component, configuration } from '@forgerock/login-widget';

// ...

function App() {
  // ...

  const config = configuration();
  const componentEvents = component();

  // ...
```

Now that you have a reference to the `component` events observable, you can trigger an event such as `open`, and you can also listen for events.

Before calling the `open` method, repurpose the existing count is 0 button within the `App` component.

1. Within the button's `onClick` handler, change the `setCount` function to `componentEvents.open`

2. Change the button text to read "Login"

The result resembles the following:

```javascript
<button
  onClick={() => {
    componentEvents.open();
  }}>
  Login
</button>
```

You can now revisit your test browser and click the Login button. The modal opens and displays a "spinner" animating on repeat.

This is expected, because the Advanced Identity Cloud/PingAM Login Widget does not yet have any information to render.

Click the button in the top-right to close the modal. The modal should be dismissed as expected.

Now that you have the modal mounted and functional, move on to the next step which configures the Advanced Identity Cloud/PingAM Login Widget to be able to call the authorization server to get authentication data.

## Calling the authorization server

Before the Advanced Identity Cloud/PingAM Login Widget can connect you need to use the `config` variable you created earlier.

Call its `set` method within the exiting `useEffect`, and provide the configuration values for your server:

```javascript
useEffect(() => {

  config.setAsync({
    forgerock: {
      serverConfig: {
        wellknown: 'https://openam-forgerock-sdks.forgeblocks.com/am/oauth2/realms/root/realms/alpha/.well-known/openid-configuration',
        timeout: 3000,
      },
    },
  });

  const widget = new Widget({ target: document.getElementById('widget-root')});

  // ...
```

Now that you have the Advanced Identity Cloud/PingAM Login Widget configured, add the `journey` module to the list of imports so that you can start the authentication flow:

```javascript
import Widget, {
  component,
  configuration,
  journey,
} from '@forgerock/login-widget';
```

Execute the `journey` function and assign its returned value to a `journeyEvents` variable. Do this underneath the other existing "event" variables:

```javascript
import Widget, { component, configuration, journey } from '@forgerock/login-widget';

// ...

function App() {
  // ...

  const config = configuration();
  const componentEvents = component();
  const journeyEvents = journey();

  // ...
```

This new observable provides access to journey events. Within the Login button's `onClick` handler add the `start` method.

Now, when you open the modal, you also call `start` to request the first authentication step from the server.

```javascript
<button onClick={() => {
    journeyEvents.start();
    componentEvents.open();
  }>
  Login
</button>
```

You are now capable of authenticating a user. With an existing user, authenticate as that user and see what happens.

If successful, you'll notice the modal dismisses itself but your app is not capturing anything from this action. Proceed to the next step to capture user data.

## Authenticating a user

There are multiple ways to capture the event of a successful login and access the user information.

In this guide, you use the `journeyEvents` observable created previously.

Within the existing `useEffect` function:

1. Call the `subscribe` method and assign its return value to an unsubscribe variable

2. Pass in a function that logs the emitted events to the console

3. Call the unsubscribe function within the return function of `useEffect`

```javascript
// ...

useEffect(() => {
  // ...

  const widget = new Widget({ target: document.getElementById('widget-root') });

  const journeyEventsUnsub = journeyEvents.subscribe((event) => {
    console.log(event);
  });

  return () => {
    widget.$destroy();
    journeyEventsUnsub();
  };
}, []);
```

|   |                                                                                                                       |
| - | --------------------------------------------------------------------------------------------------------------------- |
|   | Unsubscribing from the observable is important to avoid memory leaks if the component mounts and unmounts frequently. |

Revisit your app in the test browser, but remove all of the browser's cookies and Web Storage to ensure you have a fresh start.

|   |                                                                                                                                                          |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | In Chromium browsers, you can find it under the "Application" tab of the developer tools.In Firefox and Safari, you can find it under the "Storage" tab. |

Once you have deleted all the cookies and storage, refresh the browser and try to log in your test user.

You will notice in the developer tools console that a lot of events are emitted.

Initially, you may not have much need for all this data, but over time, this information might become more valuable to you.

To narrow down all of this information, capture just one piece of the event: the user response after successfully logging in.

To do that, you can add a conditional, as follows:

* Add an `if` condition within the `subscribe` callback function that tests for the existence of the user response.

  ```javascript
  const journeyEventsUnsub = journeyEvents.subscribe((event) => {
    if (event.user.response) {
      console.log(event.user.response);
    }
  });
  ```

With the above condition, the Advanced Identity Cloud/PingAM Login Widget only writes out the user information when it's *truthy*. This helps narrow down the information to what is useful right now.

Remove all the cookies and Web Storage again and refresh the page. Try logging in again, and you should see only one log of the user information when it's available:

Example `user.event.response` output

```javascript
{
    email: 'sdk.demo-user@example.com',
    sub: '54c77653-dc88-48fb-ac6b-d5078ebe9fb0',
    subname: '54c77653-dc88-48fb-ac6b-d5078ebe9fb0'
}
```

Next, repurpose the `useState` hook that's already used in the component to save the user information.

1. Change the zeroth index of the returned value from `count` to `userInfo`

2. Change the first index of the returned value from `setCount` to `setUserInfo`

3. Change the default value passed into the `useState` from `0` to `null`

4. Change the condition from just truthy to `userInfo !== event.user.response`

5. Replace the `console.log` with the `setUserInfo` function

6. Add the `userInfo` variable in the dependency array of the `useEffect`

The top part of your `App` function component should resemble the following:

```javascript
function App() {
  const [userInfo, setUserInfo] = useState(null);

  // Initiate all the Widget modules
  const config = configuration();
  const componentEvents = component();
  const journeyEvents = journey();

  useEffect(() => {
    // Set the Widget's configuration
    config.setAsync({
      forgerock: {
        serverConfig: {
          wellknown: 'https://openam-forgerock-sdks.forgeblocks.com/am/oauth2/realms/root/realms/alpha/.well-known/openid-configuration',
          timeout: 3000,
        }
      }
    });

    // Instantiate the Widget and assign it to a variable
    const widget = new Widget({ target: document.getElementById('widget-root') });

    // Subscribe to journey observable and assign unsubscribe function to variable
    const journeyEventsUnsub = journeyEvents.subscribe((event) => {
      if (userInfo !== event.user.response) {
        setUserInfo(event.user.response);
      }
    });

    // Return a function that destroys the Widget and unsubscribes from the journey observable
    return () => {
      widget.$destroy();
      journeyEventsUnsub();
    };
  }, [userInfo]);

  // ...
```

|   |                                                                                                                                                                                                                                                                      |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The condition comparing `userInfo` to `event.user.response` reduces the number of times the `setUserInfo` is called as it will now only be called if what is set in the hook is different than what is emitted from the Advanced Identity Cloud/PingAM Login Widget. |

Now that you have the user data set into the React component, print it out into the DOM.

1. Replace the paragraph tag containing the text `Edit <code>src/App.jsx</code> and save to test HMR` with a `<pre>` tag

2. Within the `<pre>` tag, write a pair of braces: `{}`

3. Within these braces, use the `JSON.stringify` method to serialize the `userInfo` value

Your JSX should now look like this:

```javascript
<pre>{JSON.stringify(userInfo, null, ' ')}</pre>
```

|   |                                                                                                 |
| - | ----------------------------------------------------------------------------------------------- |
|   | The `null` and `' '` (literal space character) help format the JSON to be more reader-friendly. |

After clearing the browser data, try logging the user in and observe the user info get rendered onto the page after success.

![law react user info](../../_images/LAW/law-react-user-info.png)Figure 3. User info displaying after successful log in

## Logging a user out

The final step is to log the user out, clearing all the user-related cookies, storage, and cache.

To do this, add the `user` module to the list of imports from the Advanced Identity Cloud/PingAM Login Widget:

```javascript
import Widget, {
  configuration,
  component,
  journey,
  user,
} from '@forgerock/login-widget';
```

Next, configure the app to display the button as a Login button when the user has not yet authenticated and a Logout button when the user has already logged in:

1. Wrap the button element with braces containing a ternary, using the *falsiness* of the `userInfo` as the condition

2. When no `userInfo` exists—​the user is logged out—​render the Login button

3. Write a Logout button with an `onClick` handler to run the `user.logout` function

The resulting JSX should resemble this:

```javascript
import Widget, { user, component, configuration, journey } from '@forgerock/login-widget';

// ...

<h1>Vite + React</h1>
<div className="card">
  {
    !userInfo ? (
      <button
        onClick={() => {
          journeyEvents.start();
          componentEvents.open();
        }}>
        Login
      </button>
    ) : (
      <button
        onClick={() => {
          user.logout();
        }}>
        Logout
      </button>
    )
  }
  <pre>{JSON.stringify(userInfo, null, ' ')}</pre>
</div>
// ...
```

|   |                                                                                                                                                                                                                    |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | You do not have to add code to reset the `userInfo` with the `setUserInfo` function, because you are already "listening" to events emitted from the `user` observable nested within the `journeyEvents` subscribe. |

If your app is already reacting to the presence of user info, it should be rendering the Logout button already. Click it and observe the application reacting.

You should now be able to log a user in and out, with the app reacting to the changes in state.

---

---
title: Integrate with PingOne Protect for risk evaluations
description: The Advanced Identity Cloud/PingAM Login Widget can integrate with PingOne Protect to evaluate the risk involved in a transaction.
component: login-widget
page_id: login-widget:login-widget:integrations/integrate-with-pingone-protect
canonical_url: https://developer.pingidentity.com/login-widget/login-widget/integrations/integrate-with-pingone-protect.html
section_ids:
  steps: Steps
---

# Integrate with PingOne Protect for risk evaluations

The Advanced Identity Cloud/PingAM Login Widget can integrate with [PingOne Protect](https://www.pingidentity.com/en/platform/capabilities/threat-protection/pingone-protect.html) to evaluate the risk involved in a transaction.

|   |                                                                                                                                                                                                                                                                                                                                        |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | PingOne Protect is supported in the following servers:- Advanced Identity Cloud

  Use the official PingOne Protect nodes

- PingAM 7.5 and later

  Use the official PingOne Protect nodes

- PingAM 7.2 - 7.4

  Use the [marketplace PingOne Protect nodes](https://backstage.forgerock.com/marketplace/entry/0N4Pho4BHzclhgZmJDZV) |

![A flowchart illustrating how risk predictors evaluate many different data points to determine whether to allow a user access or prompt mitigation.](../../_images/pingone-protect.png)Figure 1. A flowchart illustrating how risk predictors evaluate many different data points.

You can instruct the Advanced Identity Cloud/PingAM Login Widget to gather information during a transaction. Your app can then collate this information together and request a risk evaluation from PingOne.

Based on the response from Protect, you can choose whether to allow or deny the transaction or perform additional mitigation, such as bot detection measures.

You can use the audit functionality in PingOne to view the risk evaluations:

![Risk evaluation records in the PingOne audit viewer.](../../_images/pingone-audit-risk-evaluations-en.png)Figure 2. Risk evaluation records in the PingOne audit viewer.

## Steps

* [Step 1. Set up the servers](pingone-protect/01-prerequisites.html)

  In this step, you set up your PingOne Advanced Identity Cloud or PingAM server, and your PingOne instance to perform risk evaluations.

  For example, you create a worker application in PingOne and configure your server to access it. You also create an authentication journey that uses the relevant nodes.

* [Step 2. Configure the Advanced Identity Cloud/PingAM Login Widget for PingOne Protect](pingone-protect/02-configure-login-widget-for-protect.html)

  With everything prepared, you can now configure the Advanced Identity Cloud/PingAM Login Widget to evaluate risk by using PingOne Protect.

---

---
title: Integrating the Advanced Identity Cloud/PingAM Login Widget
description: Find out how you can integrate the Advanced Identity Cloud/PingAM Login Widget with different frameworks and libraries.
component: login-widget
page_id: login-widget:login-widget:integrations
canonical_url: https://developer.pingidentity.com/login-widget/login-widget/integrations.html
revdate: Mon, 3 Jul 2023 18:00:37 +0100
---

# Integrating the Advanced Identity Cloud/PingAM Login Widget

Find out how you can integrate the Advanced Identity Cloud/PingAM Login Widget with different frameworks and libraries.

* [Integrate with PingOne Protect for risk evaluations](integrations/integrate-with-pingone-protect.html)

  The Advanced Identity Cloud/PingAM Login Widget can integrate with PingOne Protect to evaluate the risk involved in a transaction.

  Use PingOne Protect in your authentication journeys to help prevent identity fraud by incorporating advanced features and real-time detection.

* [Integrate Login Widget into a React app](integrations/how-integrate-with-react.html)

  Learn how to integrate the Advanced Identity Cloud/PingAM Login Widget into a simple React app that you scaffold using Vite.

---

---
title: Localizing the widget
description: The Advanced Identity Cloud/PingAM Login Widget uses variables with default values for all strings it displays when rendering the user interface.
component: login-widget
page_id: login-widget:login-widget:customize/localize
canonical_url: https://developer.pingidentity.com/login-widget/login-widget/customize/localize.html
revdate: Mon, 17 Feb 2025 15:07:20 +0100
keywords: ["Customization", "User Interface", "Locale"]
---

# Localizing the widget

The Advanced Identity Cloud/PingAM Login Widget uses variables with default values for all strings it displays when rendering the user interface.

> **Collapse: Show variable names and default values**
>
> **Default localization values**
>
> | Variable                                                            | Default text                                                                                                                                                                                                                                                                |
> | ------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
> | `alreadyHaveAnAccount`                                              | Already have an account? \<a href='?journey'>Sign in here!\</a>                                                                                                                                                                                                             |
> | `backToDefault`                                                     | Back to Sign In                                                                                                                                                                                                                                                             |
> | `backToLogin`                                                       | Back to Sign In                                                                                                                                                                                                                                                             |
> | `closeModal`                                                        | Close                                                                                                                                                                                                                                                                       |
> | `charactersCannotRepeatMoreThan`                                    | Character cannot repeat more than {max} times                                                                                                                                                                                                                               |
> | `charactersCannotRepeatMoreThanCaseInsensitive`                     | Character cannot repeat more than {max} times (case insensitive)                                                                                                                                                                                                            |
> | `checkYourEmail`                                                    | Check your email                                                                                                                                                                                                                                                            |
> | `chooseDifferentUsername`                                           | Please choose a different username.                                                                                                                                                                                                                                         |
> | `chooseYourDeviceForIdentityVerification`                           | Choose your device for identity verification.                                                                                                                                                                                                                               |
> | `confirmPassword`                                                   | Confirm password                                                                                                                                                                                                                                                            |
> | `constraintViolationForPassword`                                    | Password does not meet the requirements.                                                                                                                                                                                                                                    |
> | `constraintViolationForValue`                                       | Value does not meet the requirements.                                                                                                                                                                                                                                       |
> | `continueWith`                                                      | Continue with                                                                                                                                                                                                                                                               |
> | `copyAndPasteUrlBelow`                                              | Or, copy and paste the URL below into your authentictor app.                                                                                                                                                                                                                |
> | `copyUrl`                                                           | Copy URL                                                                                                                                                                                                                                                                    |
> | `customSecurityQuestion`                                            | Custom security question                                                                                                                                                                                                                                                    |
> | `deviceName`                                                        | Device name                                                                                                                                                                                                                                                                 |
> | `doesNotMeetMinimumCharacterLength`                                 | At least {min} character(s)                                                                                                                                                                                                                                                 |
> | `dontGetLockedOut`                                                  | Don't get locked out of your account!                                                                                                                                                                                                                                       |
> | `dontHaveAnAccount`                                                 | No account? \<a href='?journey=Registration'>Register here!\</a>                                                                                                                                                                                                            |
> | `ensurePasswordIsMoreThan`                                          | Password must contain at least {minPasswordLength} character(s).                                                                                                                                                                                                            |
> | `ensurePasswordHasOne`                                              | Password must contain at least 1 capital letter, 1 number, and 1 special character.                                                                                                                                                                                         |
> | `enterVerificationCode`                                             | Enter verification code                                                                                                                                                                                                                                                     |
> | `exceedsMaximumCharacterLength`                                     | Exceeds maximum of {max} characters                                                                                                                                                                                                                                         |
> | `fieldCanNotContainFollowingCharacters`                             | Cannot contain these character(s): {chars}                                                                                                                                                                                                                                  |
> | `fieldCanNotContainFollowingValues`                                 | Cannot contain these value(s): {fields}                                                                                                                                                                                                                                     |
> | `forgotPassword`                                                    | Forgot password?                                                                                                                                                                                                                                                            |
> | `forgotUsername`                                                    | Forgot username?                                                                                                                                                                                                                                                            |
> | `givenName`                                                         | First name                                                                                                                                                                                                                                                                  |
> | `inputRequiredError`                                                | Value is required                                                                                                                                                                                                                                                           |
> | `loading`                                                           | Loading …​                                                                                                                                                                                                                                                                  |
> | `loginButton`                                                       | Sign in                                                                                                                                                                                                                                                                     |
> | `loginFailure`                                                      | Sign in failed                                                                                                                                                                                                                                                              |
> | `loginHeader`                                                       | Sign in                                                                                                                                                                                                                                                                     |
> | `loginSuccess`                                                      | Sign in successful!                                                                                                                                                                                                                                                         |
> | `mail`                                                              | Email address                                                                                                                                                                                                                                                               |
> | `minimumNumberOfNumbers`                                            | At least {num} number(s)                                                                                                                                                                                                                                                    |
> | `minimumNumberOfLowercase`                                          | At least {num} lowercase letter(s)                                                                                                                                                                                                                                          |
> | `minimumNumberOfUppercase`                                          | At least {num} uppercase letter(s)                                                                                                                                                                                                                                          |
> | `minimumNumberOfSymbols`                                            | At least {num} symbol(s)                                                                                                                                                                                                                                                    |
> | `nameCallback`                                                      | Username                                                                                                                                                                                                                                                                    |
> | `nameYourDevice`                                                    | Name your device                                                                                                                                                                                                                                                            |
> | `next`                                                              | Next                                                                                                                                                                                                                                                                        |
> | `nextButton`                                                        | Next                                                                                                                                                                                                                                                                        |
> | `notToExceedMaximumCharacterLength`                                 | No more than {max} characters                                                                                                                                                                                                                                               |
> | `noLessThanMinimumCharacterLength`                                  | At least {min} character(s)                                                                                                                                                                                                                                                 |
> | `onMobileOpenInAuthenticator`                                       | On mobile? Open link in Authenticator.                                                                                                                                                                                                                                      |
> | `optionallyNameDevice`                                              | Optionally name your device                                                                                                                                                                                                                                                 |
> | `passwordCallback`                                                  | Password                                                                                                                                                                                                                                                                    |
> | `passwordCannotContainCommonPasswords`                              | Password cannot contain common passwords                                                                                                                                                                                                                                    |
> | `passwordCannotContainCommonPasswordsOrBeReversible`                | Password cannot contain common passwords or reversible text                                                                                                                                                                                                                 |
> | `passwordCannotContainCommonPasswordsOrBeReversibleStringsLessThan` | Password cannot contain common passwords or reversible text less than {min} characters                                                                                                                                                                                      |
> | `passwordRequirements`                                              | Password requirements:                                                                                                                                                                                                                                                      |
> | `pleaseCheckValue`                                                  | Please check this value                                                                                                                                                                                                                                                     |
> | `pleaseConfirm`                                                     | Please confirm                                                                                                                                                                                                                                                              |
> | `preferencesMarketing`                                              | Send me special offers and services                                                                                                                                                                                                                                         |
> | `preferencesUpdates`                                                | Send me news and updates                                                                                                                                                                                                                                                    |
> | `provideCustomQuestion`                                             | Provide custom security question                                                                                                                                                                                                                                            |
> | `qrCodeNotWorking`                                                  | Not working or need an alternative method?                                                                                                                                                                                                                                  |
> | `qrCodeFailedToRender`                                              | QR Code failed to render. Please notify your support administrator. You are welcome to use the alternative methods below.                                                                                                                                                   |
> | `qrCodeImportFailure`                                               | We are unable to render your QR Code. Please use one of the alternative methods below.                                                                                                                                                                                      |
> | `redirectingTo`                                                     | Redirecting you to                                                                                                                                                                                                                                                          |
> | `registerButton`                                                    | Register                                                                                                                                                                                                                                                                    |
> | `registerHeader`                                                    | Register                                                                                                                                                                                                                                                                    |
> | `registerSuccess`                                                   | Registration successful!                                                                                                                                                                                                                                                    |
> | `requiredField`                                                     | Value is required                                                                                                                                                                                                                                                           |
> | `registerYourDevice`                                                | Register {name}                                                                                                                                                                                                                                                             |
> | `scanQrCodeWithAuthenticator`                                       | Scan the QR code image below with the ForgeRock Authenticator app to register your device with your login.                                                                                                                                                                  |
> | `securityAnswer`                                                    | Security answer                                                                                                                                                                                                                                                             |
> | `securityQuestions`                                                 | Security question(s)                                                                                                                                                                                                                                                        |
> | `securityQuestionsPrompt`                                           | Provide security question(s) and answer(s):                                                                                                                                                                                                                                 |
> | `shouldContainANumber`                                              | Should contain a number                                                                                                                                                                                                                                                     |
> | `shouldContainAnUppercase`                                          | Should contain an uppercase letter                                                                                                                                                                                                                                          |
> | `shouldContainALowercase`                                           | Should contain a lowercase letter                                                                                                                                                                                                                                           |
> | `shouldContainASymbol`                                              | Should contain a symbol                                                                                                                                                                                                                                                     |
> | `showPassword`                                                      | Show password                                                                                                                                                                                                                                                               |
> | `signalsEvaluation`                                                 | Evaluating device information.                                                                                                                                                                                                                                              |
> | `skipButton`                                                        | Skip                                                                                                                                                                                                                                                                        |
> | `sn`                                                                | Last name                                                                                                                                                                                                                                                                   |
> | `submit`                                                            | Submit                                                                                                                                                                                                                                                                      |
> | `submitButton`                                                      | Submit                                                                                                                                                                                                                                                                      |
> | `successMessage`                                                    | Success!                                                                                                                                                                                                                                                                    |
> | `termsAndConditions`                                                | Please accept our Terms & Conditions                                                                                                                                                                                                                                        |
> | `termsAndConditionsLinkText`                                        | View full Terms & Conditions                                                                                                                                                                                                                                                |
> | `tryAgain`                                                          | Please try again                                                                                                                                                                                                                                                            |
> | `twoFactorAuthentication`                                           | Two factor authentication                                                                                                                                                                                                                                                   |
> | `useThisNewMfaToHelpVerifyYourIdentity`                             | Use this new device or Multi-Factor Authentication method to help verify your identity.                                                                                                                                                                                     |
> | `useValidEmail`                                                     | Please use a valid email address.                                                                                                                                                                                                                                           |
> | `unrecoverableError`                                                | There was an error in the form submission.                                                                                                                                                                                                                                  |
> | `unknownLoginError`                                                 | Unknown login failure has occurred.                                                                                                                                                                                                                                         |
> | `unknownNetworkError`                                               | Unknown network request failure has occurred.                                                                                                                                                                                                                               |
> | `url`                                                               | URL:                                                                                                                                                                                                                                                                        |
> | `useDeviceForIdentityVerification`                                  | Use your device for identity verification.                                                                                                                                                                                                                                  |
> | `useOneOfTheseCodes`                                                | Use one of these codes to authenticate if you lose your device, which has been named: \<em>{name}\</em>                                                                                                                                                                     |
> | `userName`                                                          | Username                                                                                                                                                                                                                                                                    |
> | `usernameRequirements`                                              | Username requirements:                                                                                                                                                                                                                                                      |
> | `useTheAuthenticatorAppOnYourPhone`                                 | Find the verification code using the authenticator app on your phone.                                                                                                                                                                                                       |
> | `validatedCreatePasswordCallback`                                   | Password                                                                                                                                                                                                                                                                    |
> | `validatedCreateUsernameCallback`                                   | Username                                                                                                                                                                                                                                                                    |
> | `valueRequirements`                                                 | Value requirements:                                                                                                                                                                                                                                                         |
> | `verifyYourIdentity`                                                | Verify your identity                                                                                                                                                                                                                                                        |
> | `yourDevice`                                                        | Your device                                                                                                                                                                                                                                                                 |
> | `yourMultiFactorAuthIsEnabled`                                      | Your new device or MFA is enabled                                                                                                                                                                                                                                           |
> | `yourRecoveryCodesToAccessAccountForLostDevice`                     | If you lose your device, or don't have it with you, a recovery code is the only way to sign in to your account with 2-step verification enabled. It's strongly recommended that you print and store these codes in a safe place. \<b>Each code can only be used once\</b>." |

You can use the `content` configuration element to specify custom values for these variables, or to localize text content.

To localize the text the Advanced Identity Cloud/PingAM Login Widget displays, you must provide the localized strings in the `content` configuration element when you initialize the widget. If you don't override the content strings, the widget uses the default `en-us` strings.

For example, the following code specifies localized content for the `fr-ca` locale and also overrides the default `en-us` values:

Example `content` configuration

```javascript
var userLang = navigator.language || navigator.userLanguage;

switch(userLang) {
  case 'fr-CA':
    config.set({
      content: {
        "userName": "Identifiant",
        "passwordCallback": "Phrase secrète",
        "nextButton": "Nous allez en route!",
      },
    });
    break;
  default:
    config.set({
      content: {
        "userName": "Identifier",
        "passwordCallback": "Passphrase",
        "nextButton": "Let's go!",
      },
    });
}
```

![Custom values displayed when locale is not \`fr-CA\`](../../_images/LAW/law-config-custom-content-en.png)Figure 1. Custom values displayed when locale is not `fr-CA`

---

---
title: Log in with OATH one-time passwords
description: The Advanced Identity Cloud/PingAM Login Widget provides UI elements for the OATH Token Verifier node but not currently the OATH Registration.
component: login-widget
page_id: login-widget:login-widget:use-cases/how-to-oath-otp
canonical_url: https://developer.pingidentity.com/login-widget/login-widget/use-cases/how-to-oath-otp.html
revdate: Wed, 17 May 2023 14:10:20 +0100
keywords: ["Integration", "Journeys", "Features", "Multi-factor Authentication (MFA)", "Standards"]
---

# Log in with OATH one-time passwords

The Advanced Identity Cloud/PingAM Login Widget provides UI elements for the **OATH Token Verifier** node but not currently the **OATH Registration**.

If your users have registered the ForgeRock Authenticator for one-time passwords using a browser, for example, then an app using the Advanced Identity Cloud/PingAM Login Widget will be able to accept the one-time password from the authenticator app.

The Advanced Identity Cloud/PingAM Login Widget requires that the **OATH Token Verifier** node is contained within a **Page node** configured with a specific Stage property.

In the containing **Page Node**, set the Stage property to `OneTimePassword`:

![law oath journey with stage en](../../_images/LAW/law-oath-journey-with-stage-en.png)Figure 1. OATH journey example

The Advanced Identity Cloud/PingAM Login Widget detects that stage value as a special case and renders the appropriate UI:

![law oath ui with stage en](../../_images/LAW/law-oath-ui-with-stage-en.png)Figure 2. Rendering with the `OneTimePassword` stage property

If you do not put the **OATH Token Verifier** node within a **Page node**, the Advanced Identity Cloud/PingAM Login Widget will not render the UI correctly:

![law oath ui en](../../_images/LAW/law-oath-ui-en.png)Figure 3. Rendering a lone **OATH Token Verifier** node

---

---
title: Log in with social authentication
description: Social authentication provides your users with a choice of ways to sign in that suits them.
component: login-widget
page_id: login-widget:login-widget:use-cases/how-to-social-login
canonical_url: https://developer.pingidentity.com/login-widget/login-widget/use-cases/how-to-social-login.html
revdate: Wed, 17 May 2023 14:10:20 +0100
keywords: ["Integration", "Journeys", "Features", "Social Authentication", "Standards"]
---

# Log in with social authentication

Social authentication provides your users with a choice of ways to sign in that suits them.

The Ping (ForgeRock) SDK for JavaScript supports social authentication with the following providers:

* Apple

* Facebook

* Google

Selecting one of these providers in a journey initiates an OAuth 2.0 flow allowing them to authenticate themselves with the social provider before returning to the original journey.

To enable this flow you need to:

1. Offer a choice of social identity providers using the **Select Identity Provider** node.

   * Optionally, you can allow users to skip social authentication and enter their credentials in the same form, provided nodes such as a username collector are also present.

2. Handle the OAuth 2.0 flow for your users using the **Social Provider Handler Node**.

3. Determine if the user signed in to the social provider maps to a known user by adding the **Identify Existing User Node**.

The following is an example journey for social authentication:

![law social login journey en](../../_images/LAW/law-social-login-journey-en.png)Figure 1. Example social login journey

|   |                                                                                                                                                                                                                                                                                                                                                                              |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | For a detailed guide covering the creation of social authentication journeys, refer to [How do I create end user journeys for social registration and login in PingOne Advanced Identity Cloud?](https://support.pingidentity.com/s/article/How-do-I-create-end-user-journeys-for-social-registration-and-login-in-Advanced-Identity-Cloud) in the Backstage Knowledge Base. |

On the client side, the Advanced Identity Cloud/PingAM Login Widget handles the selection of the identity provider and redirection to the provider.

You need to ensure your app manages the return back from the provider. To handle the return from a social provider, detect `code`, `state` and `form_post_entry` query parameters, as these instruct the Advanced Identity Cloud/PingAM Login Widget to resume authentication using the current URL:

Detect social authentication query parameters and continue the journey

```javascript
import { journey } from '@forgerock/login-widget';

const journeyEvents = journey();

const url = new URL(location.href);
const codeParam = url.searchParams.get('code');
const stateParam = url.searchParams.get('state');
const formPostEntryParam = url.searchParams.get('form_post_entry');

if (formPostEntryParam || (codeParam && stateParam)) {
    journey.start({ resumeUrl: location.href });
}
```

The `location.href` value includes any query parameters returned from the social provider. Without all the query parameters, the Advanced Identity Cloud/PingAM Login Widget might not be able to rehydrate the journey and continue as needed.

---

---
title: Step 1. Install the widget
description: You can add the Advanced Identity Cloud/PingAM Login Widget to your app by using Node Package Manager (npm), or you can download it from GitHub and build it yourself, adding results to your project directly.
component: login-widget
page_id: login-widget:login-widget:tutorial/01-install
canonical_url: https://developer.pingidentity.com/login-widget/login-widget/tutorial/01-install.html
revdate: Wed, 17 May 2023 14:10:20 +0100
keywords: ["Integration", "Getting Started"]
section_ids:
  npm: Install the Advanced Identity Cloud/PingAM Login Widget with npm
  build: Build a customized Advanced Identity Cloud/PingAM Login Widget
  next: Next
---

# Step 1. Install the widget

You can add the Advanced Identity Cloud/PingAM Login Widget to your app by using Node Package Manager (npm), or you can download it from GitHub and build it yourself, adding results to your project directly.

* [Install the Advanced Identity Cloud/PingAM Login Widget with npm](#npm)

  The easiest way to add the Advanced Identity Cloud/PingAM Login Widget to your project.

* [Build a customized Advanced Identity Cloud/PingAM Login Widget](#build)

  If you want to [customize the themes](../customize/theme.html) included in the Advanced Identity Cloud/PingAM Login Widget, you need to download the Advanced Identity Cloud/PingAM Web Login Framework source, make your modifications, and build a customized package.

## Install the Advanced Identity Cloud/PingAM Login Widget with npm

Add the Advanced Identity Cloud/PingAM Login Widget to your project using npm as follows:

`npm install @forgerock/login-widget`

Next, you can [Step 2. Configure the CSS](02-configure-css.html).

## Build a customized Advanced Identity Cloud/PingAM Login Widget

The following steps show how to download the Advanced Identity Cloud/PingAM Web Login Framework and build the Advanced Identity Cloud/PingAM Login Widget:

1. Download the Advanced Identity Cloud/PingAM Web Login Framework from the Git repository:

   `git clone https://github.com/ForgeRock/forgerock-web-login-framework.git`

2. In a terminal window, navigate to the root of the Advanced Identity Cloud/PingAM Web Login Framework:

   `cd forgerock-web-login-framework`

3. Run `npm` to download and install the required packages and modules:

   `npm install`

4. Build the Advanced Identity Cloud/PingAM Login Widget with `npm`:

   `npm run build:widget`

5. Copy the built `package/` directory into your app project

6. Import the `Widget` component into your app:

   `import Widget from '../path/to/package/index.js';`

   |   |                                                                                                             |
   | - | ----------------------------------------------------------------------------------------------------------- |
   |   | The exact syntax for importing the widget into your app varies depending on the technologies your app uses. |

## Next

Next, you can [Step 2. Configure the CSS](02-configure-css.html).

---

---
title: Step 1. Set up the servers
description: In this step, you set up your PingOne Advanced Identity Cloud or PingAM server, and your PingOne instance to perform risk evaluations.
component: login-widget
page_id: login-widget:login-widget:integrations/pingone-protect/01-prerequisites
canonical_url: https://developer.pingidentity.com/login-widget/login-widget/integrations/pingone-protect/01-prerequisites.html
section_ids:
  pingone-worker-app: Create a worker application in PingOne
  pingone-worker-service: Configure the PingOne Worker service in your server
  prerequisites: Prerequisites
  register_the_client_secret_in_the_server: Register the client secret in the server
  p1-worker-service: Configure the PingOne worker service
  map_the_client_secret_label_identifier_to_a_secret: Map the Client Secret Label Identifier to a secret
  map_secrets_in_advanced_identity_cloud: Map secrets in Advanced Identity Cloud
  map_secrets_in_self_managed_am: Map secrets in self-managed AM
  pingone-protect-journey: Configure a journey to perform PingOne Protect risk evaluations
---

# Step 1. Set up the servers

In this step, you set up your PingOne Advanced Identity Cloud or PingAM server, and your PingOne instance to perform risk evaluations.

1. [Create a worker application in PingOne](#pingone-worker-app)

2. [Configure the PingOne Worker service in your server](#pingone-worker-service)

3. [Configure a journey to perform PingOne Protect risk evaluations](#pingone-protect-journey)

## Create a worker application in PingOne

To allow your server to access the PingOne administration API you must create a [worker application](https://docs.pingidentity.com/pingone/applications/p1_applications_add_applications.html) in PingOne.

The worker application provides the client credentials your server uses to communicate with the PingOne admin APIs using the OpenID Connect protocol.

To create a worker application in PingOne:

1. In the PingOne administration console, navigate to **Applications** [icon: angle-right, set=fa] **Applications**, and then click Add ([icon: circle-plus, set=fas, size=lg]).

2. In the Add Application panel:

   1. In Application name, enter a unique identifier for the worker application.

      For example, `Ping (ForgeRock) SDK Worker`.

   2. Optionally, enter a Description for the application and select an Icon.

      These do not affect the operation of the worker application but do help you identify it in the list.

   3. In Application Type, select Worker.

   4. Click Save.

3. In the application properties panel for the worker application you created:

   1. On the Roles tab, click Grant Roles.

   2. On the Available responsibilities tab, select the Identity Data Admin row, and ensure the environment is correct.

   3. Click Save.

   4. On the Overview tab, ensure your worker application resembles the following image, and then enable it by using the toggle (1):

      ![Example worker application in PingOne](../../../_images/pingone-worker-application-en.png)Figure 1. Example worker application in PingOne

   5. Make a note of the Environment ID, Client ID, and Client Secret values (2).

      You need these values in the next step when you [Configure the PingOne Worker service in your server](#pingone-worker-service).

## Configure the PingOne Worker service in your server

After you [create a worker application](#pingone-worker-app) in PingOne, you must configure the PingOne Worker service in your server with the credentials.

### Prerequisites

You need the following values from the PingOne Worker application you created in PingOne:

* Client ID

  Client ID of the worker application in PingOne.

  Example: `6c7eb89a-66e9-ab12-cd34-eeaf795650b2`

* Client Secret

  Client secret of the worker application in PingOne.

  |   |                                                                                                                                                                                 |
  | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | Use the Secret Mask ([icon: eye-slash, set=far]) or Copy to Clipboard ([icon: copy, set=far, flip=vertical]) buttons to obtain the value in the PingOne administration console. |

  Example: `Ch15~o5Hm8N4_eS_m8~ARrV0KQAIQS6d.sJWe8TMXurEb~KWexY_p0gelR`

* Environment ID

  Identifier of the environment that contains the worker application in PingOne.

  Example: `3072206d-c6ce-ch15-m0nd-f87e972c7cc3`

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The PingOne Worker Service requires a configured OAuth2 provider service in your server.* If you are using a self-managed AM server, you must [configure the OAuth2 Provider service in a realm to expose the OAuth 2.0 endpoints and OAuth 2.0 administration REST endpoints.](https://docs.pingidentity.com/pingam/8/oauth2-guide/oauth2-configure-authz.html).

* The OAuth2 provider service is preconfigured in Advanced Identity Cloud. |

### Register the client secret in the server

You need to make the client secret of the worker application in PingOne available for use in the PingOne worker service.

* Advanced Identity Cloud

  If you are using Advanced Identity Cloud you will need to create an environment secret to hold the client secret value, as follows:

  1. In the Advanced Identity Cloud admin UI, go to [icon: cog, set=fa]Tenant Settings > Global Settings > Environment Secrets & Variables.

  2. Click the Secrets tab.

  3. Click + Add Secret.

  4. In the Add a Secret modal window, enter the following information:

     |             |                                                                                                                                                                                                                                                                                                                                           |
     | ----------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
     | Name        | Enter a secret name. For example, `ping-protect-client-secret`.	Secret names cannot be modified after the secret has been created.                                                                                                                                                                                                        |
     | Description | (optional) Enter a description of the purpose of the secret.                                                                                                                                                                                                                                                                              |
     | Value       | Enter the Client Secret value you obtained when creating the worker application in PingOne.For example, `Ch15~o5Hm8N4_eS_m8~ARrV0KQAIQS6d.sJWe8TMXurEb~KWexY_p0gelR`.The field obscures the secret value by default. You can optionally click the visibility toggle ([icon: eye-slash, set=fa]) to view the secret value as you enter it. |

  5. Click Save to create the variable.

  6. Click **View Update**, check the details of the new secret, and then click **Apply Update**.

     Advanced Identity Cloud displays a final confirmation page.

     ![aic save esv secret en](../../../_images/aic-save-esv-secret-en.png)Figure 2. Apply updated secrets in Advanced Identity Cloud

  7. Click Apply Now.

     Advanced Identity Cloud propagates the new secret and its value to all servers. You **must** wait until the secrets have propagated throughout the environment before attempting to use the secret.

     The Environment Secrets & Variables page displays the following message while the update is in progress:

     ![aic esv propagate en](../../../_images/aic-esv-propagate-en.png)Figure 3. Propagating secrets in progress in Advanced Identity Cloud.

* Self-managed AM

  For information on adding secret values for use in services in a self-managed AM instance, refer to [Create key aliases](https://docs.pingidentity.com/pingam/8/security-guide/configuring-keys.html#creating-new-keys) in the AM documentation.

### Configure the PingOne worker service

To configure the PingOne worker service:

1. If you are using PingOne Advanced Identity Cloud, in the administration console navigate to Native Consoles > Access Management.

2. In the AM admin UI, click Services.

3. If the PingOne Worker Service is in the list of services, select it.

4. If you do not yet have a PingOne Worker Service:

   1. Click [icon: plus, set=fa]Add a Service.

   2. In Choose a service type, select `PingOne Worker Service`, and then click Create.

5. On the Secondary Configurations tab, click [icon: plus, set=fa]Add a Secondary Configuration.

6. On the New workers configuration page:

   1. Enter a Name for the configuration.

      For example, `SDK PingOne Worker`.

      You use this value when you configure an authentication journey that performs risk evaluations.

   2. In Client ID, enter the client ID of the PingOne Worker application you created earlier.

   3. In Client Secret Label Identifier, enter an identifier to create a specific secret label to represent the client secret of the worker application.

      For example, `workerAppClientSecret`.

      The secret label uses the template `am.services.pingone.worker.identifier.clientsecret` where identifier is the Client Secret Label Identifier value.

      This field can only contain characters `a-z`, `A-Z`, `0-9`, and `.` and can't start or end with a period.

   4. In Environment ID, enter the environment ID containing the PingOne Worker application you created earlier.

   5. Click Create

7. On the Workers Configuration page, ensure that the PingOne API Server URL and PingOne Authorization Server URL are correct for the region of your PingOne servers:

   **PingOne URLs by region**

   | Region                          | Authorization URL           | API URL                       |
   | ------------------------------- | --------------------------- | ----------------------------- |
   | North America(Excluding Canada) | `https://auth.pingone.com`  | `https://api.pingone.com/v1`  |
   | Canada                          | `https://auth.pingone.ca`   | `https://api.pingone.ca/v1`   |
   | Europe                          | `https://auth.pingone.eu`   | `https://api.pingone.eu/v1`   |
   | Asia-Pacific                    | `https://auth.pingone.asia` | `https://api.pingone.asia/v1` |

8. Confirm your configuration resembles the image below, and then click Save changes.

   ![Example worker service configuration in AM](../../../_images/pingone-worker-service-example-en.png)Figure 4. Example worker application in PingOne

### Map the Client Secret Label Identifier to a secret

To make the client secret available to the PingOne Worker Service, you must map the secret to the ID created.

#### Map secrets in Advanced Identity Cloud

1. In the Advanced Identity Cloud admin UI, click **Native Consoles > Access Management**.

2. In the AM admin UI (native console), go to **Realm > Secret Stores**.

3. Click the ESV secret store, then click Mappings.

4. Click + Add Mapping.

   1. In Secret Label, select the label generated when you entered the Client Secret Label Identifier previously.

      For example, `am.services.pingone.worker.workerAppClientSecret.clientsecret`.

   2. In aliases, enter the name of the ESV secret you created earlier, including the `esv-` prefix, and then click Add.

      For example, `esv-ping-protect-client-secret`

   The result resembles the following:

   ![Example mapping of the Client Secret Label Identifier value.](../../../_images/pingone-worker-mapping-aic-en.png)

5. Click Create.

To learn more about mapping secrets and label identifiers in Advanced Identity Cloud, refer to [Secret labels](https://docs.pingidentity.com/pingoneaic/latest/am-reference/secret-id-mappings.html).

#### Map secrets in self-managed AM

To learn about mapping secrets in self-managed AM, refer to [Map and rotate secrets](https://docs.pingidentity.com/pingam/8/security-guide/secret-mapping.html).

You have now configured the PingOne Worker service in your server. You can now [Configure a journey to perform PingOne Protect risk evaluations](#pingone-protect-journey).

## Configure a journey to perform PingOne Protect risk evaluations

To make risk evaluations in PingOne, you must configure an authentication journey in your server.

The following table covers the authentication nodes and callbacks for integrating your authentication journeys with PingOne Protect.

| Node                                                                                                                              | Callback                                                                                                                                                    | Description                                                                                                            |
| --------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| [PingOne Protect Initialization node](https://docs.pingidentity.com/auth-node-ref/latest/pingone/pingone-protect-initialize.html) | [PingOneProtectInitializeCallback](https://docs.pingidentity.com/pingam/8/authentication-guide/callbacks-interactive.html#PingOneProtectInitializeCallback) | Instruct the embedded PingOne Signals SDK to start gathering contextual information.                                   |
| [PingOne Protect Evaluation node](https://docs.pingidentity.com/auth-node-ref/latest/pingone/pingone-protect-evaluation.html)     | [PingOneProtectEvaluationCallback](https://docs.pingidentity.com/pingam/8/authentication-guide/callbacks-interactive.html#PingOneProtectEvaluationCallback) | Returns contextual information that the server can send to your PingOne Protect instance to perform a risk evaluation. |
| [PingOne Protect Result node](https://docs.pingidentity.com/auth-node-ref/latest/pingone/pingone-protect-result.html)             | Non-interactive                                                                                                                                             | Inform the PingOne Protect instance about the status of the transaction.                                               |

In your server, log in as an administrator and create a new authentication journey similar to the following example:

![An example PingOne Protect journey](../../../_images/pingone-protect-example-journey.png)Figure 5. An example PingOne Protect journey

* The [PingOne Protect Initialize node](https://docs.pingidentity.com/auth-node-ref/latest/pingone/pingone-protect-initialize.html) 1 instructs the SDK to initialize the PingOne Protect Signals API with the configured properties.

  Initialize the PingOne Protect Signals API as early in the journey as possible, before any user interaction.

  This enables it to gather sufficient contextual data to make an informed risk evaluation.

  |   |                                                                                                                                                                                    |
  | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | You can initialize the PingOne Protect Signals API whenever you want to start collecting data. This could be at application startup, or when a particular page or view is visited. |

* The user enters their credentials, which are verified against the identity store.

* The [PingOne Protect Evaluation node](https://docs.pingidentity.com/auth-node-ref/latest/pingone/pingone-protect-evaluation.html) 2 performs a risk evaluation against a risk policy in PingOne.

  The example journey continues depending on the outcome:

  * `High`

    The journey requests that the user respond to a push notification.

  * `Medium` or `Low`

    The risk is not significant, so no further authentication factors are required.

  * `Exceeds Score Threshold`

    The score returned is higher than the configured threshold and is considered too risky to complete successfully.

  * `Failure`

    The risk evaluation could not be completed, so the authentication attempt continues to the Failure node.

  * `BOT_MITIGATION`

    The risk evaluation returned a recommended action to check for the presence of a human, so the journey continues to a CAPTCHA node.

  * `ClientError`

    The client returned an error when attempting to capture the data to perform a risk evaluation, so the authentication attempt continues to the Failure node.

* An instance of the [PingOne Protect Result node](https://docs.pingidentity.com/auth-node-ref/latest/pingone/pingone-protect-result.html) 3 returns the `Success` result to PingOne, which can be viewed in the audit console to help with analysis and risk policy tuning.

* A second instance of the [PingOne Protect Result node](https://docs.pingidentity.com/auth-node-ref/latest/pingone/pingone-protect-result.html) 4 returns the `Failed` result to PingOne, which can be viewed in the audit console to help with analysis and risk policy tuning.

You have now configured a suitable authentication journey in your server. You can now proceed to [Step 2. Configure the Advanced Identity Cloud/PingAM Login Widget for PingOne Protect](02-configure-login-widget-for-protect.html).

---

---
title: Step 2. Configure the Advanced Identity Cloud/PingAM Login Widget for PingOne Protect
description: Integrating the Advanced Identity Cloud/PingAM Login Widget with PingOne Protect enables you to perform risk evaluations during your customer's journey.
component: login-widget
page_id: login-widget:login-widget:integrations/pingone-protect/02-configure-login-widget-for-protect
canonical_url: https://developer.pingidentity.com/login-widget/login-widget/integrations/pingone-protect/02-configure-login-widget-for-protect.html
section_ids:
  init: Initialize data collection
  return-data: Return collected data for a risk evaluation
  pause-resume: Pause and resume behavioral data capture
---

# Step 2. Configure the Advanced Identity Cloud/PingAM Login Widget for PingOne Protect

Integrating the Advanced Identity Cloud/PingAM Login Widget with PingOne Protect enables you to perform risk evaluations during your customer's journey.

Complete the following tasks to fully integrate with PingOne Protect:

1. [Initialize data collection](#init)

2. [Pause and resume behavioral data capture](#pause-resume)

3. [Return collected data for a risk evaluation](#return-data)

## Initialize data collection

You must initialize the PingOne Signals SDK so that it collects the data needed to evaluate risk.

The earlier you can initialize the PingOne Signals SDK, the more data it can collect to make a risk evaluation.

There are two options for initializing the PingOne Signals SDK in the Advanced Identity Cloud/PingAM Login Widget:

1. The Advanced Identity Cloud/PingAM Login Widget automatically initializes the PingOne Signals SDK on receipt of a `PingOneProtectInitializeCallback` callback from a journey you have started.

2. Manually initialize the PingOne Signals SDK, import the module and pass in any [configuration parameters](#init-params) you need, as follows:

   ```js
   import Widget, { configuration, journey, protect } from '@forgerock/login-widget';

   new Widget({ target: widgetEl });

   // Start PingOne Protect Signals SDK
   await protect.start({
     envId: 3072206d-c6ce-ch15-m0nd-f87e972c7cc3,
     behavioralDataCollection: true,
     consoleLogEnabled: true,
   });
   ```

   The PingOne Signals SDK supports a number of parameters which you can supply yourself, or are contained in the `PingOneProtectInitializeCallback` callback.

   > **Collapse: Show PingOne Signals SDK  parameters**
   >
   > |                              |                            |                                 |                                                                                                                                                                                                                                                |
   > | ---------------------------- | -------------------------- | ------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   > | **Parameter**                |                            |                                 | **Description**                                                                                                                                                                                                                                |
   > | ***Android***                | ***iOS***                  | ***JavaScript***                |                                                                                                                                                                                                                                                |
   > | `envID`                      |                            |                                 | Required. Your PingOne environment identifier.                                                                                                                                                                                                 |
   > | `deviceAttributesToIgnore`   |                            |                                 | Optional. A list of device attributes to ignore when collecting device signals.For example, `AUDIO_OUTPUT_DEVICES` or `IS_ACCEPT_COOKIES`.                                                                                                     |
   > | `isBehavioralDataCollection` | `behavioralDataCollection` |                                 | When `true`, collect behavioral data.Default is `true`.                                                                                                                                                                                        |
   > | `isConsoleLogEnabled`        | `consoleLogEnabled`        |                                 | When `true`, output SDK log messages in the developer console.Default is `false`.                                                                                                                                                              |
   > | `isLazyMetadata`             | `lazyMetadata`             |                                 | When `true`, calculate metadata on demand rather than automatically after calling `start`.Default is `false`.                                                                                                                                  |
   > | N/A                          |                            | `deviceKeyRsyncIntervals`       | Number of days that device attestation can rely upon the device fallback key.Default: `14`                                                                                                                                                     |
   > | N/A                          |                            | `disableHub`                    | When `true`, the client stores device data in the browser's `localStorage` only.When `false` the client uses an iframe.Default is `false`.                                                                                                     |
   > | N/A                          |                            | `disableTags`                   | When `true`, the client does not collect tag data.Tags are used to record the pages the user visited, forming a browsing history.Default is `false`.                                                                                           |
   > | N/A                          |                            | `enableTrust`                   | When `true`, tie the device payload to a non-extractable crypto key stored in the browser for content authenticity verification.Default is `false`.                                                                                            |
   > | N/A                          |                            | `externalIdentifiers`           | Optional. A list of custom identifiers that are associated with the device entity in PingOne Protect.                                                                                                                                          |
   > | N/A                          |                            | `hubUrl`                        | Optional. The iframe URL to use for cross-storage device IDs.                                                                                                                                                                                  |
   > | N/A                          |                            | `waitForWindowLoad`             | When `true`, initialize the SDK on the `load` event, instead of the `DOMContentLoaded` event.Default is `true`.                                                                                                                                |
   > | N/A                          |                            | `universalDeviceIdentification` | Optional. When `true`, device data in the payload returned to the server is provided as a signed JWT.                                                                                                                                          |
   > | N/A                          |                            | `agentIdentification`           | Set to `true` when using risk policies that contain the [PingID Device Trust](https://docs.pingidentity.com/pingone/threat_protection_using_pingone_protect/p1_protect_risk_predictors.html#pingid-device-trust) predictor.Default is `false`. |
   > | N/A                          |                            | `agentTimeout`                  | If you have enabled `agentIdentification`, use `agentTimeout` to specify a connection timeout, in milliseconds.Specifying a value overrides the default.Default is `1000`.                                                                     |
   > | N/A                          |                            | `agentPort`                     | If you have enabled `agentIdentification`, use `agentPort` to specify the port for connecting to the trust agent.Specifying a value overrides the default.Default is `9400`.                                                                   |

## Return collected data for a risk evaluation

To perform risk evaluations, the PingOne server requires the captured data.

There are two options for returning data in the Advanced Identity Cloud/PingAM Login Widget:

1. On receipt of a `PingOneProtectEvaluationCallback` callback within a journey, the Advanced Identity Cloud/PingAM Login Widget automatically returns the captured data.

2. Use the `getData()` method to manually return the captured data:

   ```js
   import Widget, { configuration, journey, protect } from '@forgerock/login-widget';

   new Widget({ target: widgetEl });

   // Start PingOne Protect Signals SDK
   await protect.start({
     envId: 3072206d-c6ce-ch15-m0nd-f87e972c7cc3,
     behavioralDataCollection: true,
     consoleLogEnabled: true,
   });

   // Return gathered data to the server
   await protect.getData();
   ```

## Pause and resume behavioral data capture

The PingOne Protect Signals SDK can capture behavioral data, such as how the user interacts with the app, to help when performing evaluations.

There are scenarios where you might want to pause the collection of behavioral data. For example, the user might not be interacting with the app, or you only want to use device attribute data to be considered when performing PingOne Protect evaluations. You can then resume behavioral data collection when required.

There are two options for pausing and resuming behavioral data capture in the Advanced Identity Cloud/PingAM Login Widget:

1. The `PingOneProtectEvaluationCallback` callback can include a flag to pause or resume behavioral capture, which the Advanced Identity Cloud/PingAM Login Widget automatically responds to.

2. Use the `pauseBehavioralData()` and `resumeBehavioralData()` methods to manually pause or resume the capture of behavioral data:

   ```js
   import Widget, { configuration, journey, protect } from '@forgerock/login-widget';

   new Widget({ target: widgetEl });

   // Start PingOne Protect Signals SDK
   await protect.start({
     envId: 3072206d-c6ce-ch15-m0nd-f87e972c7cc3,
     behavioralDataCollection: true,
     consoleLogEnabled: true,
   });

   // Return gathered data to the server
   await protect.getData();

   // Pause behavioral data collection
   protect.pauseBehavioralData();

   // Resume behavioral data collection
   protect.resumeBehavioralData();
   ```

---

---
title: Step 2. Configure the CSS
description: You can use any of the following methods to add the default Advanced Identity Cloud/PingAM Login Widget styles to your app:
component: login-widget
page_id: login-widget:login-widget:tutorial/02-configure-css
canonical_url: https://developer.pingidentity.com/login-widget/login-widget/tutorial/02-configure-css.html
revdate: Wed, 17 May 2023 14:10:20 +0100
keywords: ["Integration", "Getting Started", "Customization", "User Interface"]
section_ids:
  examples: Examples
  controlling_the_css_cascade: Controlling the CSS cascade
  next: Next
---

# Step 2. Configure the CSS

You can use any of the following methods to add the default Advanced Identity Cloud/PingAM Login Widget styles to your app:

1. Import it into your JavaScript project as a module.

2. Import it using a CSS preprocessor, like Sass, Less, or PostCSS.

If you decide to import the CSS into your JavaScript, make sure your bundler is able to import and process the CSS as a module. If using a CSS preprocessor, configure your preprocessor to access files from within your package or from a directory.

## Examples

Import the CSS into your JavaScript:

* npm

* Local

```javascript
// app.js
import '@forgerock/login-widget/widget.css';
```

```javascript
// app.js
import '../path/to/widget.css';
```

Import the CSS into your CSS:

* npm

* Local

```css
/* style.css */
@import '@forgerock/login-widget/widget.css';
```

```javascript
/* style.css */
@import '../path/to/widget.css';
```

## Controlling the CSS cascade

How the browser applies styles to an app can depend on the order you import or declare CSS into it, referred to as the *cascade*.

You can use the `@layer` CSS rule to declare a cascade layer, ensuring Advanced Identity Cloud/PingAM Login Widget styles apply separately from your own.

For more information, refer to [`@layer`](https://developer.mozilla.org/en-US/docs/Web/CSS/@layer) in the MDN docs.

|   |                                                                                                                                                                                  |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The Advanced Identity Cloud/PingAM Login Widget styles will not overwrite any of your CSS.They are namespaced to help prevent collisions and use a CSS selector prefix of `tw_`. |

To create a cascade layer for the Advanced Identity Cloud/PingAM Login Widget styles:

1. Wrap your existing styles in a new layer, for example, "app":

   ```css
   @layer app {
       /* Your app's existing CSS */
   }
   ```

2. Declare the order of layers in your index HTML file before loading any CSS.

   |   |                                                                |
   | - | -------------------------------------------------------------- |
   |   | The Widget has multiple `@layer` declarations in its CSS files |

   ```html
   <style type="text/css">
     /* Your existing "app" CSS layer first */
     @layer app;

     /* List the Widget layers after your own styles */
     @layer 'fr-widget.base';
     @layer 'fr-widget.utilities';
     @layer 'fr-widget.components';
     @layer 'fr-widget.variants';
   </style>
   ```

   |   |                                                                                                                                                                                                                                                               |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | The CSS imported for the Widget will not overwrite any of your app's CSS. It's all namespaced to ensure there are no collisions. To help achieve this, the Advanced Identity Cloud/PingAM Login Widget uses a selector naming convention with a `tw_` prefix. |

## Next

Next, you can [Step 3. Import the widget](03-import.html)

---

---
title: Step 3. Import the widget
description: To use the Advanced Identity Cloud/PingAM Login Widget, import the modules you want to use into your app:
component: login-widget
page_id: login-widget:login-widget:tutorial/03-import
canonical_url: https://developer.pingidentity.com/login-widget/login-widget/tutorial/03-import.html
revdate: Wed, 17 May 2023 14:10:20 +0100
keywords: ["Integration", "Getting Started"]
section_ids:
  next: Next
---

# Step 3. Import the widget

To use the Advanced Identity Cloud/PingAM Login Widget, import the modules you want to use into your app:

```javascript
// Import the Login Widget
import Widget, { configuration } from '@forgerock/login-widget';
```

The exact syntax for importing the widget depends on the module system you are using.

The Advanced Identity Cloud/PingAM Login Widget exports a number of different modules, each providing different functionality.

**Advanced Identity Cloud/PingAM Login Widget modules**

| Module          | Description                                                                                                                                                                                      | API reference                                                                 |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------- |
| `Widget`        | Use this main class to instantiate the Advanced Identity Cloud/PingAM Login Widget, mount it into the DOM, and set up event listeners.                                                           | [Widget API reference](../widget-api-reference.html#widget-api)               |
| `configuration` | Use this module to configure the Advanced Identity Cloud/PingAM Login Widget. You can configure the settings it needs to contact the authorization server, styles, layout, and override content. | [Configuration API reference](../widget-api-reference.html#configuration-api) |
| `journey`       | Use this module to configure and start an authentication journey.                                                                                                                                | [Journey API reference](../widget-api-reference.html#journey-api)             |
| `component`     | Use this module to subscribe to events triggered by the Advanced Identity Cloud/PingAM Login Widget and for controlling the modal form factor.                                                   | [Component API reference](../widget-api-reference.html#component-api)         |
| `user`          | Use this module for managing users in the Advanced Identity Cloud/PingAM Login Widget, such as obtaining user or token information, and logging users out.                                       | [User API reference](../widget-api-reference.html#user-api)                   |

## Next

Next, you can [Step 4. Configure the widget](04-configure-sdk.html).

---

---
title: Step 4. Configure the widget
description: The Advanced Identity Cloud/PingAM Login Widget requires information about the server instance it connects to, as well as OAuth 2.0 client configuration and other settings.
component: login-widget
page_id: login-widget:login-widget:tutorial/04-configure-sdk
canonical_url: https://developer.pingidentity.com/login-widget/login-widget/tutorial/04-configure-sdk.html
revdate: Mon, 3 Jul 2023 18:00:37 +0100
keywords: ["Integration", "Getting Started", "Setup &amp; Configuration"]
section_ids:
  sdk_configuration_properties: SDK configuration properties
  config-props: Server
  oauth_2_0: OAuth 2.0
  storage: Storage
  logging: Logging
  general: General
  endpoints: Endpoints
  next: Next
---

# Step 4. Configure the widget

The Advanced Identity Cloud/PingAM Login Widget requires information about the server instance it connects to, as well as OAuth 2.0 client configuration and other settings.

To provide these settings, import and use the `configuration` module and its `set()` method.

The Advanced Identity Cloud/PingAM Login Widget uses the same underlying [configuration properties](#config-props) as the main SDK. Add your configuration under the `forgerock` property:

Example Advanced Identity Cloud/PingAM Login Widget configuration

```javascript
// Import the modules
import Widget, { configuration } from '@forgerock/login-widget';

// Create a configuration instance
const myConfig = configuration();

// Set the configuration properties
myConfig.set({
  forgerock: {
    // Minimum required configuration:
    serverConfig: {
        baseUrl: 'https://openam-forgerock-sdks.forgeblocks.com/am',
        timeout: 3000,
    },
    // Optional configuration:
    clientId: 'sdkPublicClient', // The default is `WebLoginWidgetClient`
    realmPath: 'alpha',  // This is the default if not specified
    redirectUri: window.location.href,  // This is the default if not specified
    scope: 'openid profile email address', // The default is `openid profile` if not specified
  },
});
```

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Set your Advanced Identity Cloud/PingAM Login Widget configuration at the top level of your application, such as its `index.js` or `app.js` file.This ensures the Advanced Identity Cloud/PingAM Login Widget has the configuration needed to call out to your PingOne Advanced Identity Cloud or PingAM server whenever and wherever you use its APIs in your app.For example, you must set the configuration before starting a journey with `journeyEvents.start()` or calling either `userEvents.get()` or `tokenEvents.get()`. |

## SDK configuration properties

The configuration properties available in both the SDK and the Advanced Identity Cloud/PingAM Login Widget are as follows:

## Server

**Properties**

| Property                    | Description                                                                                                                                                                                                                                                                                                                                                                                                                       |
| --------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `serverConfig`              | An interface for configuring how the SDK contacts the PingAM instance.Contains `baseUrl` and `timeout`.                                                                                                                                                                                                                                                                                                                           |
| `serverConfig: {baseUrl}`   | The base URL of the server to connect to, including port and deployment path.*Identity Cloud example*:`https://openam-forgerock-sdks.forgeblocks.com/am`*Self-hosted example*:`https://openam.example.com:8443/openam`                                                                                                                                                                                                            |
| `serverConfig: {wellknown}` | A URL to the server's `.well-known/openid-configuration` endpoint.Use the `Config.setAsync()` method to set SDK configuration using values derived from those provided at the URL.*Example*:`https://openam-forgerock-sdks.forgeblocks.com/am/oauth2/realms/root/realms/alpha/.well-known/openid-configuration`*Self-hosted example*:`https://openam.example.com:8443/openam/oauth2/realms/root/.well-known/openid-configuration` |
| `serverConfig: {timeout}`   | A timeout, in milliseconds, for each request that communicates with your server.For example, for 30 seconds specify `30000`.Defaults to `5000` (5 seconds).                                                                                                                                                                                                                                                                       |
| `realmPath`                 | The realm in which the OAuth 2.0 client profile and authentication journeys are configured.For example, `alpha`.Defaults to the self-hosted top-level realm `root`.                                                                                                                                                                                                                                                               |
| `tree`                      | The name of the user ***authentication*** tree configured in your server.For example, `sdkUsernamePasswordJourney`.                                                                                                                                                                                                                                                                                                               |

## OAuth 2.0

**Properties**

| Property         | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| ---------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `clientId`       | The `client_id` of the OAuth 2.0 client profile to use.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| `redirectUri`    | The `redirect_uri` as configured in the OAuth 2.0 client profile.&#xA;&#xA;The Ping (ForgeRock) SDK for JavaScript attempts to load the redirect page to capture the OAuth 2.0 code and state query parameters that the server appended to the redirect URL.&#xA;&#xA;If the page you redirect to does not exist, takes a long time to load, or runs any JavaScript you might get a timeout, delayed authentication, or unexpected errors.&#xA;&#xA;To ensure the best user experience, we highly recommend that you redirect to a static HTML page with minimal HTML and no JavaScript when obtaining OAuth 2.0 tokens.For example, `https://localhost:8443/callback.html`. |
| `scope`          | A list of scopes to request when performing an OAuth 2.0 authorization flow, separated by spaces.For example, `openid profile email address`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `oauthThreshold` | A threshold, in seconds, to refresh an OAuth 2.0 token before the `access_token` expires.Defaults to `30` seconds.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |

## Storage

**Properties**

| Property     | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `tokenStore` | The API to use for storing tokens on the client:- `sessionStorage`

  Store tokens using the `sessionStorage` API. The browser clears session storage when a page session ends.

- `localStorage`

  Store tokens using the `localStorage` API. The browser saves local storage data across browser sessions. This is the default setting, as it provides the highest browser compatibility.

- `{{custom}}`

  Specify a custom implementation that has functions that can set, retrieve, and remove, items from a custom storage scheme. |
| `prefix`     | Override the default `fr` prefix string applied to the keys used for storing data on the client, such as tokens, device IDs, and information about the steps in a journey.For example, the key used for storing tokens consists of the `prefix`, followed by the ID of the OAuth 2.0 client:`fr-sdkPublicClient`.                                                                                                                                                                                                                          |

## Logging

**Properties**

| Property   | Description                                                                                                                                                                    |
| ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `logLevel` | Specify whether the SDK should output its log messages in the console and the level of messages to display.One of:- `none` (default)

- `info`

- `warn`

- `error`

- `debug` |
| `logger`   | Specify a function to override the default logging behavior.                                                                                                                   |

## General

**Properties**

| Property         | Description                                                                                                                                                                                                                                                                                                                                                |
| ---------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `platformHeader` | Specify whether to include an `X-Requested-Platform` header in outgoing requests.The server can use the value of this header to alter the logic of an authentication flow. For example, if the value indicates a JavaScript web app, the journey could avoid device binding nodes, as they are only supported by Android and iOS apps.Defaults to `false`. |

## Endpoints

**Properties**

| Property                                   | Description                                                                                                              |
| ------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| `serverConfig: { paths: { authenticate }}` | Override the path to the authorization server's `authenticate` endpoint.*Default*: `json/{realmPath}/authenticate`       |
| `serverConfig: { paths: { authorize }}`    | Override the path to the authorization server's `authorize` endpoint.*Default*: `oauth2/{realmPath}/authorize`           |
| `serverConfig: { paths: { accessToken }}`  | Override the path to the authorization server's `access_token` endpoint.*Default*: `oauth2/{realmPath}/access_token`     |
| `serverConfig: { paths: { revoke }}`       | Override the path to the authorization server's `revoke` endpoint.*Default*: `oauth2/{realmPath}/token/revoke`           |
| `serverConfig: { paths: { userInfo }}`     | Override the path to the authorization server's `userinfo` endpoint.*Default*: `oauth2/{realmPath}/userinfo`             |
| `serverConfig: { paths: { sessions }}`     | Override the path to the authorization server's `sessions` endpoint.*Default*: `json/{realmPath}/sessions`               |
| `serverConfig: { paths: { endSession }}`   | Override the path to the authorization server's `endSession` endpoint.*Default*: `oauth2/{realmPath}/connect/endSession` |

## Next

Next, you can [Step 5. Instantiate the widget](05-instantiate.html).

---

---
title: Step 5. Instantiate the widget
description: To use the Advanced Identity Cloud/PingAM Login Widget in your app you must choose an appropriate place to mount it. Then, you need to choose which form factor to implement, either inline, or modal.
component: login-widget
page_id: login-widget:login-widget:tutorial/05-instantiate
canonical_url: https://developer.pingidentity.com/login-widget/login-widget/tutorial/05-instantiate.html
revdate: Mon, 3 Jul 2023 18:00:37 +0100
keywords: ["Integration", "Getting Started", "Setup &amp; Configuration"]
section_ids:
  html: Choose where to mount the Advanced Identity Cloud/PingAM Login Widget
  modal: Instantiate the modal form factor
  inline: Instantiate the inline form factor
  next: Next
---

# Step 5. Instantiate the widget

To use the Advanced Identity Cloud/PingAM Login Widget in your app you must choose an appropriate place to mount it. Then, you need to choose which form factor to implement, either inline, or modal.

With those decisions made, you can instantiate the Advanced Identity Cloud/PingAM Login Widget in your app, ready for your users to start their authentication or self-service journey.

## Choose where to mount the Advanced Identity Cloud/PingAM Login Widget

To implement the Advanced Identity Cloud/PingAM Login Widget, we recommend you add a new element into your HTML file.

For most single page applications (SPA) this is your `index.html` file.

This new element should be a direct child element of `<body>` and not within the element where you mount your SPA.

Example HTML structure

```html
<!DOCTYPE html>
<html lang="en">
<head>
<!-- ... -->
</head>
<body>
    <!-- Root element for main app -->
    <div id="root"></div>

    <!-- Root element for Widget -->
    <div id="widget-root"></div>

    <!-- scripts ... -->
  </body>
</html>
```

|   |                                                                                                                                                                                                      |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | We recommend that you do not inject the element into which you mount the modal form factor in your app. This can cause virtual DOM issues.Instead, manually hard-code the element in your HTML file. |

## Instantiate the modal form factor

To use the default Advanced Identity Cloud/PingAM Login Widget modal form factor, import the modules into your app and instantiate the widget as follows:

Instantiate the modal form factor

```javascript
// Import the Login Widget
import Widget, { configuration } from '@forgerock/login-widget';

// Configure SDK options
const myConfig = configuration();

myConfig.set({
  forgerock: {
    serverConfig: {
        baseUrl: 'https://openam-forgerock-sdks.forgeblocks.com/am',
        timeout: 3000,
    },
    // Optional but recommended configuration:
    realmPath: 'alpha',
    clientId: 'sdkPublicClient',
    redirectUri: window.location.href,
    scope: 'openid profile email address'
    },
  },
});

// Get the element in your HTML into which you will mount the widget
const widgetRootEl = document.getElementById('widget-root');

// Instantiate Widget with the `new` keyword
new Widget({
  target: widgetRootEl,
});
```

This mounts the Advanced Identity Cloud/PingAM Login Widget into the DOM. The modal form factor is the default and is hidden when first instantiated.

Top open the modal, import the `component` module, assign the function, and call its `open()` method:

Open the modal

```javascript
// Import the Login Widget
import Widget, { configuration, component } from '@forgerock/login-widget';

// Configure SDK options
const myConfig = configuration();

myConfig.set({
  forgerock: {
    serverConfig: {
        baseUrl: 'https://openam-forgerock-sdks.forgeblocks.com/am',
        timeout: 3000,
    },
    // Optional but recommended configuration:
    realmPath: 'alpha',
    clientId: 'sdkPublicClient',
    redirectUri: window.location.href,
    scope: 'openid profile email address'
    },
  },
});

// Get the element in your HTML into which you will mount the widget
const widgetRootEl = document.getElementById('widget-root');

// Instantiate Widget with the `new` keyword
new Widget({
  target: widgetRootEl, // Any existing element from static HTML file
});

// Assign the component function
const componentEvents = component();

// Call the open() method, for example after a button click
const loginButton = document.getElementById('loginButton');

loginButton.addEventListener('click', () => {
  componentEvents.open();
});
```

The modal form factor opens and displays a spinner graphic until you [start a journey](06-journey.html).

|   |                                                                                                                                       |
| - | ------------------------------------------------------------------------------------------------------------------------------------- |
|   | The modal form factor closes itself when a journey completes successfully.You can also close it by calling `componentEvents.close();` |

## Instantiate the inline form factor

You override the default Advanced Identity Cloud/PingAM Login Widget modal form factor and instead use the inline form factor. The inline form factor mounts within your application's controlled DOM, so it is important to consider how your framework mounts elements to the DOM.

For example, the inline form factor cannot mount into a virtual DOM element, such as those used by React. In this scenario, you must wait until the element has been property mounted to the real DOM before instantiating the Advanced Identity Cloud/PingAM Login Widget.

To use the inline form factor, instantiate the widget with a `type: 'inline'` property, as follows:

Instantiate the inline form factor

```javascript
// Import the Advanced Identity Cloud/PingAM Login Widget
import Widget, { configuration } from '@forgerock/login-widget';

import { useRef } from 'react';

// Configure SDK options
const myConfig = configuration();

myConfig.set({
  forgerock: {
    serverConfig: {
        baseUrl: 'https://openam-forgerock-sdks.forgeblocks.com/am',
        timeout: 3000,
    },
    // Optional but recommended configuration:
    realmPath: 'alpha',
    clientId: 'sdkPublicClient',
    redirectUri: window.location.href,
    scope: 'openid profile email address'
    },
  },
});

// Target needs to be an actual DOM element, so ref is needed with inline type
const widgetElement = useRef(null);

// Instantiate Widget with the `new` keyword
new Widget({
  target: widgetElement.current,
  props: {
    type: 'inline', // Override the default 'modal' form factor
  },
});
```

The inline form factor loads into the specified DOM element and displays a spinner graphic until you [start a journey](06-journey.html).

## Next

Next, you can [Step 6. Start a journey](06-journey.html).

---

---
title: Step 6. Start a journey
description: The Advanced Identity Cloud/PingAM Login Widget displays a loading spinner graphic if it does not yet have a callback from the server to render.
component: login-widget
page_id: login-widget:login-widget:tutorial/06-journey
canonical_url: https://developer.pingidentity.com/login-widget/login-widget/tutorial/06-journey.html
revdate: Mon, 3 Jul 2023 18:00:37 +0100
keywords: ["Integration", "Getting Started", "Setup &amp; Configuration", "Journeys"]
section_ids:
  journeyEvents-params: Configure start() parameters
  journey-params: Configure journey() parameters
  listen_for_journey_completion: Listen for journey completion
  next: Next
---

# Step 6. Start a journey

The Advanced Identity Cloud/PingAM Login Widget displays a loading spinner graphic if it does not yet have a callback from the server to render.

You must specify and start a journey to make the initial call to the server and obtain the first callback.

To start a journey, import the `journey` function and execute it to receive a `journeyEvents` object. After you have this `journeyEvents` object, you can call the `journeyEvents.start()` method, which starts making requests to the server for the initial form fields.

You can call the `journeyEvents.start()` method anywhere in your application, or anytime, as long as it is after calling the configuration's `set()` method and after instantiating the Widget.

Start the default journey

```javascript
// Import the Login Widget
import Widget, { configuration, journey } from '@forgerock/login-widget';

// Configure SDK options
const myConfig = configuration();

myConfig.set({
  forgerock: {
    serverConfig: {
        baseUrl: 'https://openam-forgerock-sdks.forgeblocks.com/am',
        timeout: 3000,
    },
    // Optional but recommended configuration:
    realmPath: 'alpha',
    clientId: 'sdkPublicClient',
    redirectUri: window.location.href,
    scope: 'openid profile email address'
    },
  },
});

// Get the element in your HTML into which you will mount the widget
const widgetRootEl = document.getElementById('widget-root');

// Instantiate Widget with the `new` keyword
new Widget({
  target: widgetRootEl,
});

// Assign the journey function
const journeyEvents = journey();

// Ensure you call `.start` *AFTER* instantiating the Widget
journeyEvents.start();
```

This starts the journey configured as the default in your server and renders the initial callback.

To specify which journey to use and other parameters, refer to [Configure start() parameters](#journeyEvents-params).

## Configure start() parameters

If you do not pass any parameters when calling the `start()` method the Advanced Identity Cloud/PingAM Login Widget will use whichever journey is marked as the default in your server.

The Advanced Identity Cloud/PingAM Login Widget will also use the values configured in the last invocation of the configuration's `set()` method.

You can override both of these behaviors by passing in JSON parameters:

**Optional start() parameters**

| Parameter   | Description                                                                                                                                                                                                                |
| ----------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `journey`   | Specify the name of the journey to use.If not specified, the Advanced Identity Cloud/PingAM Login Widget uses whichever journey is marked as the default                                                                   |
| `forgerock` | Override the current SDK configuration with any new or altered settings.For more information, refer to [Step 4. Configure the widget](04-configure-sdk.html).                                                              |
| `resumeUrl` | Specify the full URL to visit if resuming a suspended journey. The server uses this to return your users to your application after clicking a "magic link" in an email, for example.The default is `window.location.href`. |

Example of specifying the journey to use:

```javascript
// Specify a different journey
journeyEvents.start({
  journey: 'sdkRegistrationJourney',
});
```

For more information, refer to [journey](../widget-api-reference.html#journey-api) in the API reference.

## Configure journey() parameters

If you do not pass any parameters when calling the `journey()` function the Advanced Identity Cloud/PingAM Login Widget will attempt to retrieve OAuth 2.0 tokens and user information by default.

You can override this behavior by passing in the following JSON parameters:

**Optional journey() parameters**

| Parameter | Description                                                                                                                                                                                                              |
| --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `oauth`   | Set to `false` to prevent the Advanced Identity Cloud/PingAM Login Widget attempting to obtain OAuth 2.0 tokens after successfully completing a journey.The default is `true`.                                           |
| `user`    | Set to `user` to prevent the Advanced Identity Cloud/PingAM Login Widget attempting to obtain user information by calling the `/oauth2/userinfo` endpoint after successfully completing a journey.The default is `true`. |

Example - obtaining only a user session token:

```javascript
const journeyEvents = journey({
    oauth: false,
    user: false,
});
```

For more information, refer to [journey API reference](../widget-api-reference.html#journey-api)

## Listen for journey completion

Use the `journeyEvents.subscribe` method to know when a user has completed their journey.

A summary of the events for a journey and their order is as follow:

1. Journey is loading

2. Journey is complete

3. Tokens are loading

4. Tokens are complete

5. Userinfo is loading

6. Userinfo is complete

Pass a callback function into this method to run on journey related events, of which there will be many, and each event object you receive contains a lot of information about the event.

You conditionally check for the events you are interested in and ignore what you do not need.

Example - subscribe to journey events

```javascript
journeyEvents.subscribe((event) => {
  // Called multiple times, filtering by event data is recommended
  if (event.journey.successful) {
    // Only output successfull journey log entries
    console.log(event);
  }
});
```

## Next

Next, you can learn more information about observables and how to [Step 7. Subscribe to events](07-subscribe.html).

---

---
title: Step 7. Subscribe to events
description: "The Advanced Identity Cloud/PingAM Login Widget has a number of asynchronous APIs, which are designed around an event-centric observable pattern. It uses Svelte's simplified, standard observable implementation called a \"store\"."
component: login-widget
page_id: login-widget:login-widget:tutorial/07-subscribe
canonical_url: https://developer.pingidentity.com/login-widget/login-widget/tutorial/07-subscribe.html
revdate: Wed, 17 May 2023 14:10:20 +0100
keywords: ["Integration", "Getting Started", "Setup &amp; Configuration"]
section_ids:
  assign_an_observable: Assign an observable
  subscribe_to_observable_events: Subscribe to observable events
  unsubscribe_from_an_observable: Unsubscribe from an observable
  get_current_local_values: Get current local values
  get_updated_values: Get updated values
  use_promises_rather_than_observables: Use promises rather than observables
---

# Step 7. Subscribe to events

The Advanced Identity Cloud/PingAM Login Widget has a number of asynchronous APIs, which are designed around an event-centric *observable* pattern. It uses Svelte's simplified, standard observable implementation called a "store".

|   |                                                                                                                                                                       |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | These Svelte stores are embedded into the Advanced Identity Cloud/PingAM Login Widget itself.They are not a dependency that your app layer needs to import or manage. |

For more information on Svelte stores, refer to the [Svelte documentation](https://svelte.dev/docs#component-format-script-4-prefix-stores-with-$-to-access-their-values-store-contract).

This observable pattern is optimal for UI development as it allows for a dynamic user experience. You can update your application in response to the events occurring within the Advanced Identity Cloud/PingAM Login Widget. For example, the Advanced Identity Cloud/PingAM Login Widget has events such as "loading", "completed", "success", and, "failure".

## Assign an observable

You can create a variable and assign the observable to it:

Assign an observable

```javascript
const userInfoEvents = user.info();
```

## Subscribe to observable events

An observable is a stream of events over time. The Advanced Identity Cloud/PingAM Login Widget invokes the callback for each and every event from the observable, until you unsubscribe from it.

Use the `subscribe()` method on your variable to observe the event stream:

Example userInfoEvents observable

```javascript
userInfoEvents.subscribe((event) => {
  if (event.loading) {
    console.log('User info is being requested from server');
  } else if (event.successful) {
    console.log('User info request was successful');
    console.log(event.response);
  } else if (event.error) {
    console.error('User info request failed');
    console.error(event.error.message);
  }
});
```

For information on the events each observable returns, refer to the [API reference](../widget-api-reference.html).

## Unsubscribe from an observable

Unlike a JavaScript *promise*, an observable does not resolve and then get cleaned up after completion.

You need to unsubscribe from an observable if it is no longer needed. This is especially important if you are subscribing to observables in a component that gets created and destroyed many times over. Subscribing to an observable over and over without unsubscribing creates a memory leak.

To unsubscribe, assign the function that is returned from calling the `subscribe()` method to a variable. Call this variable at a later time to unsubscribe from the obeservable.

Example unsubscribe from an observable

```javascript
const unsubUserInfoEvents = userInfoEvents.subscribe((event) => console.log(event));

// ...

// Unsubscribe when no longer needed
unsubUserInfoEvents();
```

You *do not need* to unsubscribe from observables if you subscribe to observables in a top-level component of your app that is only initiated once, and is retained over the lifetime of your application.

A good location in which to subscribe to observables might be the central state management component or module of your application.

## Get current local values

The Advanced Identity Cloud/PingAM Login Widget stores a number of important values internally.

You can get the current values stored within the Advanced Identity Cloud/PingAM Login Widget without subscribing to any future events or their resulting state changes by calling `subscribe()` and then immediately calling its unsubscribe method:

Get current stored values and unsubscribe

```javascript
// Create variable for user info
let userInfo;

// Call subscribe, get the current local value, and then immediately call the returned function
userInfoEvents.subscribe((event) => (userinfo = event.response))(); // <-- notice the second pair of parentheses
```

## Get updated values

You can ask the Advanced Identity Cloud/PingAM Login Widget to request new, fresh values from the server, rather than just what it has stored locally, by calling the observable action methods, such as `get`.

Get latest values from the server

```javascript
userInfoEvents.get();
```

When using the observable pattern, you can call this method and forget about it. The get causes any `subscribe` callback functions you have for the observable to receive the events and new state.

The `subscribe` can exist before or after this `get` call, and it will still capture the resulting events.

## Use promises rather than observables

We recommend observables, but the choice is up to you.

All of the Advanced Identity Cloud/PingAM Login Widget APIs that involve network calls have an alternative promise implementation that you can use.

The following example again shows `userInfoEvents` but converted to use promises:

Using promises rather than observables

```javascript
// async-await
let userInfo;
async function example() {
  try {
    userInfo = await userInfoEvents.get();
  } catch (err) {
    console.log(err);
  }
}

// Promise
let userInfo;
userInfoEvents
  .get()
  .then((data) => (userInfo = data))
  .catch((err) => console.log(err));
```

---

---
title: "Suspend journeys with \"magic links\""
description: "You can use the Email Suspend Node within your journeys to support a number of experiences, including verifying a user's email address, building a \"forgot password\" flow or using an email address for multifactor authentication."
component: login-widget
page_id: login-widget:login-widget:use-cases/how-to-magic-links
canonical_url: https://developer.pingidentity.com/login-widget/login-widget/use-cases/how-to-magic-links.html
revdate: Wed, 17 May 2023 14:10:20 +0100
keywords: ["Integration", "Journeys", "Features"]
section_ids:
  configure_the_authentication_server: Configure the authentication server
  handle_suspend_ids_in_your_app: Handle suspend IDs in your app
---

# Suspend journeys with "magic links"

You can use the Email Suspend Node within your journeys to support a number of experiences, including verifying a user's email address, building a "forgot password" flow or using an email address for multifactor authentication.

The node suspends the journey until the user clicks a link—​referred to as a *magic link*--in their email. This link contains a generated unique code that can continue the suspended journey.

This page shows how to configure the Advanced Identity Cloud/PingAM Login Widget to take advantage of this feature.

## Configure the authentication server

1. Add the Email Suspend Node to the journey to suspend it until the user continues the journey from the link found in their email.

   ![how to magic links tree en](../../_images/LAW/how-to-magic-links-tree-en.png)Figure 1. Insert the Email Suspend Node into your journey

2. Configure the External Login Page URL property in the Access Management native console to match your custom app's URL. This ensures the magic links are able to redirect users to your app to resume the journey. If not specified, the default behavior is to route users to the login page.

   ![how to magic links remote login en](../../_images/LAW/how-to-magic-links-remote-login-en.png)Figure 2. Configure external login URL in the PingAM native console

3. When the Advanced Identity Cloud/PingAM Login Widget encounters the Email Suspend Node, it renders the string configured in the Email Suspend Message property configured in the node. The user is not able to continue the journey until they click the link emailed to them.

## Handle suspend IDs in your app

When your app handles a magic link, it needs to recognize it as a special condition and provide the Advanced Identity Cloud/PingAM Login Widget with the full URL that the user clicked in their email.

Return this URL, including all query parameters, to the server as the value of the `resumeUrl` parameter:

```javascript
import { journey } from '@forgerock/login-widget';

const journeyEvents = journey();

const url = new URL(location.href);
const suspendedId = url.searchParams.get('suspendedId');

if (suspendedId) {
  journeyEvents.start({ resumeUrl: location.href });
}
```

The `location.href` value includes all query parameters included in the magic link. Without all the query parameters, the Advanced Identity Cloud/PingAM Login Widget might not be able to rehydrate the journey and continue as needed.