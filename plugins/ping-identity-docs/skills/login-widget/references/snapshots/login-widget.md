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
