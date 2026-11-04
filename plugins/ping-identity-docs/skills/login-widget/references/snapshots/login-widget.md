---
title: API reference
description: This page lists the modules that the Advanced Identity Cloud/PingAM Login Widget provides for use in your apps.
component: login-widget
page_id: login-widget:login-widget:widget-api-reference
canonical_url: https://developer.pingidentity.com/login-widget/login-widget/widget-api-reference.html
llms_txt: https://developer.pingidentity.com/login-widget/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: Tue, 28 Jul 2026 00:00:00 +0000
keywords: ["Source Code", "Integration"]
section_ids:
  widget-api: Widget
  configure-api: Configuration
  config-content: Content configuration options
  config-links: Links configuration options
  config-style: Style configuration options
  config-journeys-map: Journeys configuration options
  config-captcha: CAPTCHA configuration
  component-api: Component
  schema_for_component_events: Schema for component events
  journey-api: Journey
  schema_for_journey_events: Schema for journey events
  user-api: User
  schema_for_user_info_events: Schema for user.info events
  schema_for_user_tokens_events: Schema for user.tokens events
  protect-api: Protect
  protected-resources: Calling protected resources
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

The Advanced Identity Cloud/PingAM Login Widget requires the URL of your server's `.well-known/openid-configuration` endpoint. If you use OAuth/OIDC tokens, user info, or logout, it also requires an OIDC client configuration.

For information on setting up your server for use with the Advanced Identity Cloud/PingAM Login Widget, refer to [Prerequisites](tutorial.html#_prerequisites).

To provide these settings, import and `await` the async `configure()` function. Call it once at the top level of your application, before any other Widget API.

```javascript
import { configure } from '@forgerock/login-widget';

// configure() is async, so await it before calling any other Widget API
await configure({
  // REQUIRED; the well-known URL, shared by the journey and OIDC clients
  serverConfig: {
    wellknown: 'https://openam-forgerock-sdks.forgeblocks.com/am/oauth2/realms/root/realms/alpha/.well-known/openid-configuration',
  },
  // REQUIRED if you use OAuth/OIDC tokens, user info, or logout
  oidcClient: {
    clientId: 'sdkPublicClient',
    redirectUri: `${window.location.origin}/callback`,
    // OPTIONAL; defaults to 'openid'
    scope: 'openid profile email address',
  },
  // OPTIONAL; see dedicated sections below
  logger: {},
  middleware: [],
  storage: {},
  captcha: {},
  content: {},
  journeys: {},
  links: {},
  style: {},
});
```

|   |                                                                                                                                                                                                                                |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | `configure()` is asynchronous. Always `await` it, since the Advanced Identity Cloud/PingAM Login Widget constructs its internal clients during this call. Any Widget API called before `configure()` resolves throws an error. |

### Content configuration options

Use the `content` configuration element to pass custom text content to the Advanced Identity Cloud/PingAM Login Widget, replacing its default values.

You can use this method to localize user interface text for different regions. Learn more in [Localizing the widget](customize/localize.html).

Example `content` configuration

```javascript
await configure({
  serverConfig: { wellknown: 'https://openam-forgerock-sdks.forgeblocks.com/am/oauth2/realms/root/realms/alpha/.well-known/openid-configuration' },
  content: {
    userName: 'Identifier',
    passwordCallback: 'Passphrase',
    nextButton: "Let's go!",
  },
});
```

![law config custom content en](../_images/LAW/law-config-custom-content-en.png)Figure 1. Result of example content configuration

For a list of the content you can override, refer to the [en-us locale file](https://github.com/ForgeRock/forgerock-web-login-framework/blob/main/core/locales/us/en/index.json) in the Advanced Identity Cloud/PingAM Web Login Framework repository.

### Links configuration options

Use the `links` configuration element to set the full canonical URL to your terms and conditions page.

This should be a page hosted on your website or elsewhere within your app. Users are sent to this URL if they click to view the terms and conditions in the Advanced Identity Cloud/PingAM Login Widget.

This supports the `TermsAndConditionsCallback` often used in registration journeys.

Example `links` configuration

```javascript
await configure({
  serverConfig: { wellknown: 'https://openam-forgerock-sdks.forgeblocks.com/am/oauth2/realms/root/realms/alpha/.well-known/openid-configuration' },
  links: {
    termsAndConditions: 'https://example.com/terms',
  },
});
```

### Style configuration options

Use the `style` configuration element to configure the look and feel of the Advanced Identity Cloud/PingAM Login Widget.

For full guidance, including examples and screenshots, see [Configuring style properties](customize/styles/style-properties.html).

```javascript
await configure({
  serverConfig: { wellknown: 'https://openam-forgerock-sdks.forgeblocks.com/am/oauth2/realms/root/realms/alpha/.well-known/openid-configuration' },
  style: {
    checksAndRadios: 'animated',
    labels: 'floating',
    showPassword: 'button',
    logo: {
      dark: 'https://example.com/img/white-logo.png',
      light: 'https://example.com/img/black-logo.png',
      height: 300,
      width: 400,
    },
    sections: {
      header: false,
    },
    stage: {
      icon: true,
    },
    theme: {
      primaryColor: '#f46200',
      secondaryColor: '#003049',
      backgroundColor: '#ffffff',
      linkColor: '#f46200',
      fontFamily: 'Inter, sans-serif',
      buttonBorderRadius: 8,
      cardBorderRadius: 12,
    },
  },
});
```

**style properties**

| Property                       | Values                                 | Description                                                                                                                                                                                                                                                                                                                                                      |
| ------------------------------ | -------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `checksAndRadios` (*Optional*) | `animated` (default), `standard`       | Controls the rendering style of checkboxes and radio buttons.                                                                                                                                                                                                                                                                                                    |
| `labels` (*Optional*)          | `floating` (default), `stacked`        | Controls label positioning. `floating` labels animate above their field on focus; `stacked` labels sit above the field at all times.                                                                                                                                                                                                                             |
| `showPassword` (*Optional*)    | `button` (default), `checkbox`, `none` | Controls how the password visibility toggle is rendered.- `button`

  Renders a button inside the password field that toggles visibility when clicked. This is the default.

- `checkbox`

  Renders a checkbox beneath the password field that toggles visibility when checked.

- `none`

  Does not render a visibility toggle. This is the pre-2.0 behavior. |

**style.logo properties**

| Property              | Description                                       |
| --------------------- | ------------------------------------------------- |
| `light` (*Optional*)  | Full URL to the logo image for use in light mode. |
| `dark` (*Optional*)   | Full URL to the logo image for use in dark mode.  |
| `height` (*Optional*) | Number of pixels for the logo height.             |
| `width` (*Optional*)  | Number of pixels for the logo width.              |

|   |                                                                                                                                                                                                                      |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | `style.logo` only applies to the modal form factor and not the inline form factor.It accepts separate `light` and `dark` variants.To apply a single logo regardless of color scheme, use `style.theme.logo` instead. |

**style.sections properties**

| Property | Description                                                                                                                                                                                   |
| -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `header` | Boolean. Set to `true` to enable a header section that separates the logo or branding from the journey form with a dividing line. Defaults to `false`. Only applies to the modal form factor. |

**style.stage properties**

| Property | Description                                                                                                                                                                                   |
| -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `icon`   | Boolean. Set to `true` to display stage-specific icons when the journey stage matches a known value. Supported stage values are `OneTimePassword`, `DefaultRegistration`, and `DefaultLogin`. |

**style.theme properties**

| Property                                                                | Description                                                                                                                                                               |
| ----------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `primaryColor`, `primaryOffColor`                                       | Hex color values (6 or 8 digit, for example `#f46200` or `#f46200ff`) for the widget's primary brand color and its muted off-state variant.                               |
| `secondaryColor`                                                        | Hex color value for the widget's secondary brand color.                                                                                                                   |
| `backgroundColor`                                                       | Hex color for the page or modal background.                                                                                                                               |
| `cardBgColor`, `cardTextColor`                                          | Hex colors for card background and text.                                                                                                                                  |
| `bodyTextColor`                                                         | Hex color for general body text within the widget.                                                                                                                        |
| `linkColor`, `linkActiveColor`                                          | Hex colors for links in their default and active states.                                                                                                                  |
| `inputBgColor`, `inputBorderColor`, `inputLabelColor`, `inputTextColor` | Hex colors for form input background, border, label, and text.                                                                                                            |
| `inputFocusRingColor`                                                   | Hex color for the focus ring on form inputs.                                                                                                                              |
| `selectAccentColor`, `selectHoverBgColor`                               | Hex colors for `<select>` elements in their default and hover states.                                                                                                     |
| `buttonTextColor`                                                       | Hex color for button text.                                                                                                                                                |
| `buttonFocusRingColor`                                                  | Hex color for the focus ring on buttons.                                                                                                                                  |
| `fontFamily`                                                            | A CSS font family string, for example `Inter, sans-serif`.                                                                                                                |
| `logo`                                                                  | Full URL or base64 data URI to override the logo image. Applies a single logo regardless of color scheme. For separate light and dark variants, use `style.logo` instead. |
| `logoHeight`                                                            | Number of pixels for the logo height.                                                                                                                                     |
| `favicon`                                                               | Full URL for the browser tab icon.                                                                                                                                        |
| `buttonBorderRadius`, `cardBorderRadius`                                | Numbers, in pixels, controlling the corner rounding of buttons and cards.                                                                                                 |

|   |                                                                                                                                                                                                                                                                              |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | `theme.logo` accepts a single URL and is independent from `style.logo`, which accepts separate `dark` and `light` variants for the modal form factor. Use `style.logo` if you need different images per color scheme; use `theme.logo` for a single logo applied everywhere. |

### Journeys configuration options

Use the `journeys` configuration element to map HREF values rendered within the Advanced Identity Cloud/PingAM Login Widget to start a journey or authentication tree instead of visiting the URL.

![law href to journey mapping en](../_images/LAW/law-href-to-journey-mapping-en.png)Figure 2. Example HREF values in a page node

The Advanced Identity Cloud/PingAM Login Widget listens for click events on elements rendered within its container and compares the HREF to the configured mappings. If there is a match, it prevents the default action of visiting the URL and starts the journey configured in the mapping.

Mapping HREF strings to a journey

```javascript
await configure({
  serverConfig: { wellknown: 'https://openam-forgerock-sdks.forgeblocks.com/am/oauth2/realms/root/realms/alpha/.well-known/openid-configuration' },
  journeys: {
    forgotPassword: {
      journey: 'ResetPassword', // Must match actual journey name in the server
      match: ['#/service/ResetPassword'], // Array of strings that match `HREF` values (case-sensitive)
    },
  },
});
```

The Advanced Identity Cloud/PingAM Login Widget has mappings configured internally to handle the links displayed in page nodes by default. These map the HREF values that are displayed by an out-of-the-box page node to corresponding journeys in an PingOne Advanced Identity Cloud tenant. You can override the mappings if required.

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

### CAPTCHA configuration

AM does not signal invisible mode in the callback payload for either `ReCaptchaCallback` or `ReCaptchaEnterpriseCallback`. Use the `captcha` option to configure invisible rendering:

```javascript
await configure({
  serverConfig: { wellknown: 'https://openam-forgerock-sdks.forgeblocks.com/am/oauth2/realms/root/realms/alpha/.well-known/openid-configuration' },
  captcha: {
    mode: 'invisible', // 'visible' (default) | 'invisible'
  },
});
```

Refer to [Implement a CAPTCHA](use-cases/how-to-captcha.html) for more information.

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
    error: null, // null or object with `code` and `message` properties
    mounted: false, // boolean
    open: null, // boolean for the modal form factor, or null for inline form factor
    reason: null, // string to describe the reason for the event
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
  journey: 'Login', // OPTIONAL; specify the journey or tree you want to use
  query: {}, // OPTIONAL; additional query parameters to include when starting the journey
  resumeUrl: window.location.href, // OPTIONAL; the full URL for resuming a suspended journey
  recaptchaAction: 'myCaptchaTag', // OPTIONAL; tag reCAPTCHAs. Falls back to journey name.
});

// Change to a different journey
journeyEvents.change({
  journey: 'Registration',
});

// Subscribe to journey events
const unsubJourneyEvents = journeyEvents.subscribe((event) => {
  /* Run anything you want */
});

// Recommended: call when your UI component is destroyed
unsubJourneyEvents();
```

|   |                                                                                                                                                                                                                                                                                               |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | PingOne Protect risk evaluations are initialized separately via `protect.start()`, not through the `journey()` API.Refer to [Step 2. Configure the Advanced Identity Cloud/PingAM Login Widget for PingOne Protect](integrations/pingone-protect/02-configure-login-widget-for-protect.html). |

### Schema for `journey` events

The schema for `journey` events is as follows:

Schema for `journey` events

```javascript
{
  journey: {
    completed: false, // boolean
    error: null, // null or object when the journey fails:
    // {
    //   code: null,         // number; HTTP status code, e.g. 401
    //   message: null,      // string; human-readable failure reason
    //   stage: null,        // string; page node stage value, if set
    //   troubleshoot: null, // always null; reserved for future use
    //   detail: null,       // object; extra detail from the server, e.g. { failureUrl: 'https://...' }
    // }
    loading: false, // boolean
    step: null, // null or object with the last step object from the server
    successful: false, // boolean
    response: null, // null or object if successful containing the success response from the server
  },
  oauth: {
    completed: false, // boolean
    error: null, // null or object with `code` (optional), `message`, and `troubleshoot` properties
    loading: false, // boolean
    successful: false, // boolean
    response: null, // null or object with OAuth/OIDC tokens
  },
  user: {
    completed: false, // boolean
    error: null, // null or object with `code` (optional), `message`, and `troubleshoot` properties
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

The `user.info` and `user.tokens` methods require use of OAuth 2.0, so you must configure `oidcClient` in your call to `configure()`.

The `user.info` method also requires a scope value of `openid`, which is the default.

You can use `user.logout` with both OAuth 2.0 and session-based authentication.

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

To force the Advanced Identity Cloud/PingAM Login Widget to obtain fresh tokens from the server rather than returning cached tokens:

```javascript
tokenEvents.get({ forceRenew: true });
```

### Schema for `user.info` events

The schema for `user.info` events is as follows:

Schema for `user.info` events

```javascript
{
    completed: false, // boolean
    error: null,  // null or object with `code` (optional), `message`, and `troubleshoot` properties
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
    error: null,  // null or object with `code` (optional), `message`, and `troubleshoot` properties
    loading: false, // boolean
    successful: false, // boolean
    response: null, // object returned from the `/access_token` endpoint
}
```

## Protect

Use the `protect` module to manually control the PingOne Signals SDK: starting data collection, returning collected data, and pausing or resuming behavioral data capture.

Refer to [Step 2. Configure the Advanced Identity Cloud/PingAM Login Widget for PingOne Protect](integrations/pingone-protect/02-configure-login-widget-for-protect.html) for full details and code examples.

## Calling protected resources

The Advanced Identity Cloud/PingAM Login Widget does not provide an HTTP client for calling protected resources.

To call a protected endpoint, get the current access token from `user.tokens().get()` and call `fetch()` yourself, adding the `Authorization` header:

```javascript
import { user } from '@forgerock/login-widget';

const tokenEvents = user.tokens();
const { response: tokens } = await tokenEvents.get();

const response = await fetch('https://protected.resource.com', {
  method: 'GET',
  headers: {
    Authorization: `Bearer ${tokens.accessToken}`,
  },
});
```

|   |                                                                                                                                                                                                                                                                                                                                                                                                                             |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Earlier versions of the Advanced Identity Cloud/PingAM Login Widget exposed a `request` export that automatically refreshed tokens on a 401 response and parsed Identity Gateway policy advice. These behaviors are not provided by the Advanced Identity Cloud/PingAM Login Widget 2.0 and must be implemented by the consumer if needed.Refer to [Breaking changes](../release-notes/breaking.html) for more information. |

---

---
title: Before you begin
description: Complete prerequisites and configure PingOne Advanced Identity Cloud or PingAM before running the ReactJS Login Widget sample
component: login-widget
page_id: login-widget:login-widget:try-it-out/reactjs-todo-login-widget/00_before-you-begin
canonical_url: https://developer.pingidentity.com/login-widget/login-widget/try-it-out/reactjs-todo-login-widget/00_before-you-begin.html
llms_txt: https://developer.pingidentity.com/login-widget/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: Thu, 20 Aug 2026 00:00:00 +0000
keywords: ["PingOne Advanced Identity Cloud", "PingAM", "Login Widget", "ReactJS", "Setup &amp; Configuration", "Source Code", "Tutorial"]
section_ids:
  prerequisites: Prerequisites
  server_configuration: Server configuration
  aic-reactjs: PingOne Advanced Identity Cloud
  am-reactjs: PingAM
  next: Next
---

# Before you begin

[icon: circle-check, set=far]PingOne Advanced Identity Cloud [icon: circle-check, set=far]PingAM [icon: js, set=fab]Login Widget

* **Prepare**

* [Download](01_download_samples.html)

* [Configure](02_configure_sample.html)

* [Run](03_run_the_sample.html)

To successfully complete this tutorial, refer to the prerequisites in this section.

The tutorial also requires a configured PingOne Advanced Identity Cloud tenant or PingAM server.

This tutorial targets ReactJS web applications running in a browser. It does not cover React Native, which uses a separate framework and mobile application runtime.

## Prerequisites

* Node.js and npm

  The sample requires Node.js `24.2.0` or newer. To get a supported version of Node.js, refer to the [Node.js download page](https://nodejs.org/en/download/).

  You will also need `npm` to install the workspace dependencies and run the sample applications.

* Local development environment

  The ReactJS client runs over HTTPS at `https://localhost:8443` by default. Follow the current setup instructions in the [Login Widget sample repository](https://github.com/ForgeRock/sdk-sample-apps/tree/main/javascript/reactjs-todo-login-widget) for any local certificate or browser trust prompts.

## Server configuration

This tutorial requires you to configure one of the following servers:

|                                                                                                                                       |                                                                                      |
| ------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------ |
| [![PingOneAICStacked](../../../_images/logos/PingOneAICStacked.png)](#aic-reactjs)[**PingOne Advanced Identity Cloud**](#aic-reactjs) | [![PingAM](../../../_images/logos/PingAM.png)](#am-reactjs)**[PingAM](#am-reactjs)** |

### PingOne Advanced Identity Cloud

> **Collapse: Task 1. Configure CORS**
>
> [Cross-origin resource sharing](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS) (CORS) lets user agents make cross-domain server requests. In PingOne Advanced Identity Cloud, you can configure CORS to allow browsers from trusted domains to access PingOne Advanced Identity Cloud protected resources. For example, you might want a custom web application running on your own domain to get an end-user's profile information using the PingOne Advanced Identity Cloud REST API.
>
> The Advanced Identity Cloud/PingAM Login Widget samples and tutorials use `https://localhost:8443` as the host domain, which you should add to your CORS configuration.
>
> For this Login Widget sample, also add `http://localhost:9443` for the Todo API server when your CORS configuration requires it.
>
> If you are using a different domain for hosting SDK applications, ensure you add them to the CORS configuration as accepted origin domains.
>
> To update the CORS configuration in PingOne Advanced Identity Cloud, follow these steps:
>
> 1. Log in to your PingOne Advanced Identity Cloud tenant.
>
> 2. At the top right of the screen, click your name, and then select Tenant settings.
>
> 3. On the Global Settings tab, click Cross-Origin Resource Sharing (CORS).
>
> 4. Perform one of the following actions:
>
>    * If listed, click PingSDK.
>
>    * If there isn't an existing CORS configuration listed, click [icon: plus, set=fa]Add a CORS Configuration, select Ping SDK, and then click Next.
>
>      The **Ping SDK** template contains many of the default values used in these tutorials.
>
> 5. In Accepted Origins:
>
>    1. Ensure `https://localhost:8443` is listed.
>
>    2. Add `http://localhost:9443` for the Todo API server.
>
>    3. Add any DNS aliases you use to host your Ping (ForgeRock) SDK for JavaScript applications.
>
> 6. Complete the remaining fields to suit your environment.
>
>    This documentation assumes the following configuration, required for the tutorials and sample applications:
>
>    | Property            | Values                                                                                    |
>    | ------------------- | ----------------------------------------------------------------------------------------- |
>    | `Accepted Origins`  | `https://localhost:8443``http://localhost:9443`                                           |
>    | `Accepted Methods`  | `GET``POST`                                                                               |
>    | `Accepted Headers`  | `content-type``x-requested-with``x-requested-platform``accept-api-version``authorization` |
>    | `Exposed Headers`   | `authorization``content-type`                                                             |
>    | `Enable Caching`    | `True`                                                                                    |
>    | `Max Age`           | `600`                                                                                     |
>    | `Allow Credentials` | `True`                                                                                    |
>
>    |   |                                                                       |
>    | - | --------------------------------------------------------------------- |
>    |   | Click Show advanced settings to be able to edit all available fields. |
>
> 7. Click Save CORS Configuration.

> **Collapse: Task 2. Create a demo user**
>
> The samples and tutorials in this documentation often require that you have an identity set up so that you can test authentication.
>
> To create a demo user in PingOne Advanced Identity Cloud, follow these steps:
>
> 1. Log in to your PingOne Advanced Identity Cloud tenant.
>
> 2. In the left panel, click Identities > Manage.
>
> 3. Click [icon: plus, set=fa]New Alpha realm - User.
>
> 4. Enter the following details:
>
>    * **Username** = `demo`
>
>    * **First Name** = `Demo`
>
>    * **Last Name** = `User`
>
>    * **Email Address** = `demo.user@example.com`
>
>    * **Password** = `Ch4ng3it!`
>
> 5. Click Save.

> **Collapse: Task 3. Create an authentication journey**
>
> Authentication journeys provide fine-grained authentication by allowing multiple paths and decision points throughout the flow. Authentication journeys are made up of nodes that define actions taken during authentication.
>
> Each node performs a single task, such as collecting a username or making a simple decision. Nodes can have multiple outcomes rather than just success or failure.
>
> You'll need an authentication journey configured on your server to try out the **Journey** module. That journey must only use [callbacks supported by the Advanced Identity Cloud/PingAM Login Widget](../../widget-api-reference.html).
>
> |   |                                                                                                                |
> | - | -------------------------------------------------------------------------------------------------------------- |
> |   | You can use the default **Login** journey that both Advanced Identity Cloud and PingAM include out-of-the-box. |
>
> To create your own authentication journey for use when testing the Ping (ForgeRock) SDKs, follow these steps:
>
> The sample defaults to the journey names `Login` and `Registration`. Create or use a Login journey for authentication, and create a Registration journey if you want to test registration. If you use different names, set `JOURNEY_LOGIN` and `JOURNEY_REGISTER` to those names in the ReactJS application's `.env` file.
>
> 1. In your PingOne Advanced Identity Cloud tenant, navigate to Journeys, and click [icon: plus, set=fa]New Journey.
>
> 2. Enter a name, such as `sdkUsernamePasswordJourney` and click Save.
>
>    The authentication journey designer appears.
>
> 3. Drag the following nodes into the designer area:
>
>    * **Page Node**
>
>    * **Platform Username**
>
>    * **Platform Password**
>
>    * **Data Store Decision**
>
> 4. Drag and drop the **Platform Username** and **Platform Password** nodes onto the **Page Node**, so that they both appear on the same page when logging in.
>
> 5. Connect the nodes as follows:
>
>    ![sdk username password journey idcloud en](../../../_images/sdk-username-password-journey-idcloud-en.png)Figure 1. Example username and password authentication journey
>
> 6. Click Save.

> **Collapse: Task 4. Register a public OAuth 2.0 client**
>
> Public clients do not use a client secret to obtain tokens because they are unable to keep them hidden. The Ping (ForgeRock) SDKs commonly use this type of client to obtain tokens, as they cannot guarantee safekeeping of the client credentials in a browser or on a mobile device.
>
> To register a *public* OAuth 2.0 client application for use with the SDKs in PingOne Advanced Identity Cloud, follow these steps:
>
> 1. Log in to your PingOne Advanced Identity Cloud tenant.
>
> 2. In the left panel, click Applications.
>
> 3. Click [icon: plus, set=fa]Custom Application.
>
> 4. Select OIDC - OpenId Connect as the sign-in method, and then click Next.
>
> 5. Select Native / SPA as the application type, and then click Next.
>
> 6. In Name, enter a name for the application, such as `Public SDK Client`.
>
> 7. In Owners, select a user that is responsible for maintaining the application, and then click Next.
>
>    |   |                                                                                    |
>    | - | ---------------------------------------------------------------------------------- |
>    |   | When trying out the SDKs, you could select the `demo` user you created previously. |
>
> 8. In Client ID, enter `sdkPublicClient`
>
> 9. Select **Configure for SDK Sample Apps**.
>
> 10. Click Create Application.
>
>     PingOne Advanced Identity Cloud creates the application and displays the details screen.
>
> 11. On the Sign On tab:
>
>     1. In Sign-In URLs, ensure the following values appear, or add them if they don't:
>
>        `https://localhost:8443/callback.html`
>
>        |   |                                                             |
>        | - | ----------------------------------------------------------- |
>        |   | Also add any other domains where you host SDK applications. |
>
>     2. In Grant Types, ensure the following values appear:
>
>        `Authorization Code`
>
>        `Refresh Token`
>
>     3. In Scopes, ensure the following values appear:
>
>        `openid profile email`
>
> 12. Click Show advanced settings, and on the Authentication tab, confirm the following properties:
>
>     1. In Token Endpoint Authentication Method, select `none`.
>
>     2. In Client Type, select `Public`.
>
>     3. Enable the Implied Consent property.
>
> 13. Click Save.
>
> The application is now configured to accept client connections from and issue OAuth 2.0 tokens to the example applications and tutorials covered by this documentation.

> **Collapse: Task 5. Register a confidential OAuth 2.0 client**
>
> Confidential clients are able to securely store credentials and are commonly used for server-to-server communication. For example, the "Todo" API backend provided with the SDK samples uses a confidential client to obtain tokens.
>
> To register a *confidential* OAuth 2.0 client application for use with the SDKs in PingOne Advanced Identity Cloud, follow these steps:
>
> 1. Log in to your PingOne Advanced Identity Cloud tenant.
>
> 2. In the left panel, click Applications.
>
> 3. Click [icon: plus, set=fa]Custom Application.
>
> 4. Select OIDC - OpenId Connect as the sign-in method, and then click Next.
>
> 5. Select Web as the application type, and then click Next.
>
> 6. In Name, enter a name for the application, such as `Confidential SDK Client`.
>
> 7. In Owners, select a user responsible for maintaining the application, and then click Next.
>
>    |   |                                                                                    |
>    | - | ---------------------------------------------------------------------------------- |
>    |   | When trying out the SDKs, you could select the `demo` user you created previously. |
>
> 8. On the Web Settings page:
>
>    1. In Client ID, enter `sdkConfidentialClient`
>
>    2. In Client Secret, enter a strong password and make a note of it for later use.
>
>       For example, `5tr0ngP@S5w0rd!`
>
>       |   |                                                                                                                                               |
>       | - | --------------------------------------------------------------------------------------------------------------------------------------------- |
>       |   | The client secret is not available to view after this step.If you forget it, you must reset the secret and reconfigure any connected clients. |
>
>    3. Click Create Application.
>
>       PingOne Advanced Identity Cloud creates the application and displays the details screen.
>
> 9. On the Sign On tab, In **General Settings** click Show advanced settings, and then select the Access tab:
>
>    1. In Default Scopes, enter `am-introspect-all-tokens`.
>
> 10. Click Save.

> **Collapse: Task 6. Configure the OAuth 2.0 provider service**
>
> The provider specifies the supported OAuth 2.0 configuration options for a realm.
>
> To ensure the PingOne Advanced Identity Cloud OAuth 2.0 provider service is configured for use with the Ping (ForgeRock) SDKs, follow these steps:
>
> 1. In your PingOne Advanced Identity Cloud tenant, navigate to Native Consoles > Access Management.
>
> 2. In the left panel, click [icon: plug, set=fa]Services.
>
> 3. In the list of services, click OAuth2 Provider.
>
> 4. On the Core tab, ensure Issue Refresh Tokens is enabled.
>
> 5. On the Consent tab, ensure Allow Clients to Skip Consent is enabled.
>
> 6. Click Save Changes.

### PingAM

Authentication trees provide the equivalent functionality in PingAM that authentication journeys provide in PingOne Advanced Identity Cloud. The following tasks use the PingAM admin UI and refer to these resources as trees.

> **Collapse: Task 1. Configure CORS**
>
> [Cross-origin resource sharing](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS) (CORS) lets user agents make cross-domain server requests. In PingAM, you can configure CORS to allow browsers from trusted domains to access PingAM protected resources. For example, you might want a custom web application running on your own domain to get an end-user's profile information using the PingAM REST API.
>
> The Ping (ForgeRock) SDK for JavaScript samples and tutorials all use `https://localhost:8443` as the host domain, which you should add to your CORS configuration.
>
> For this Login Widget sample, also add `http://localhost:9443` for the Todo API server when your CORS configuration requires it.
>
> If you are using a different URL for hosting SDK applications, ensure you add them to the CORS configuration as accepted origin domains.
>
> To enable CORS in PingAM, and create a CORS filter to allow requests from your configured domain names, follow these steps:
>
> 1. Log in to the PingAM admin UI as an administrator.
>
> 2. Navigate to Configure > Global Services > CORS Service > Configuration, and set the Enable the CORS filter property to `true`.
>
>    |   |                                                                                                                      |
>    | - | -------------------------------------------------------------------------------------------------------------------- |
>    |   | If this property is not enabled, CORS headers are not added to responses from PingAM, and CORS is disabled entirely. |
>
> 3. On the Secondary Configurations tab, click Add a Secondary Configuration.
>
> 4. In the Name field, enter `OrchSDK`.
>
> 5. in the Accepted Origins field, enter any DNS aliases you use for your SDK apps.
>
>    1. Add `http://localhost:9443` for the Todo API server.
>
>       This documentation assumes the following configuration:
>
>       | Property           | Values                                                                                    |
>       | ------------------ | ----------------------------------------------------------------------------------------- |
>       | `Accepted Origins` | `https://localhost:8443``http://localhost:9443`                                           |
>       | `Accepted Methods` | `GET``POST`                                                                               |
>       | `Accepted Headers` | `content-type``x-requested-with``x-requested-platform``accept-api-version``authorization` |
>       | `Exposed Headers`  | `authorization``content-type`                                                             |
>
> 6. Click Create.
>
>    PingAM displays the configuration of your new CORS filter.
>
> 7. On the CORS filter configuration page:
>
>    1. Ensure Enable the CORS filter is enabled.
>
>    2. Set the Max Age property to `600`
>
>    3. Ensure Allow Credentials is enabled.
>
> 8. Click Save Changes.

> **Collapse: Task 2. Create a demo user**
>
> The samples and tutorials in this documentation often require that you have an identity set up so that you can test authentication.
>
> To create a demo user in PingAM, follow these steps:
>
> 1. Log in to the PingAM admin UI as an administrator.
>
> 2. Navigate to [icon: address-card, set=fa]Identities, and then click [icon: plus, set=fa]Add Identity.
>
> 3. Enter the following details:
>
>    * **User ID** = `demo`
>
>    * **Password** = `Ch4ng3it!`
>
>    * **Email Address** = `demo.user@example.com`
>
> 4. Click Create.

> **Collapse: Task 3. Create an authentication tree**
>
> Authentication trees provide fine-grained authentication by allowing multiple paths and decision points throughout the authentication flow. Authentication trees are made up of nodes that define actions taken during authentication.
>
> Each node performs a single task, such as collecting a username or making a simple decision. Nodes can have multiple outcomes rather than just success or failure.
>
> To create a simple tree for use when testing the Ping (ForgeRock) SDKs, follow these steps:
>
> The sample defaults to the tree names `Login` and `Registration`. Create or use a Login tree for authentication, and create a Registration tree if you want to test registration. If you use different names, set `JOURNEY_LOGIN` and `JOURNEY_REGISTER` to those names in the ReactJS application's `.env` file.
>
> 1. Under Realm Overview, click Authentication Trees, then click Create Tree.
>
> 2. Enter a tree name, for example `sdkUsernamePasswordJourney`, and then click Create.
>
>    The authentication tree designer appears, showing the Start entry point connected to the Failure exit point.
>
> 3. Drag the following nodes from the Components panel on the left side into the designer area:
>
>    * **Page Node**
>
>    * **Username Collector**
>
>    * **Password Collector**
>
>    * **Data Store Decision**
>
> 4. Drag and drop the **Username Collector** and **Password Collector** nodes onto the **Page Node**, so that they both appear on the same page when logging in.
>
> 5. Connect the nodes as follows:
>
>    ![trees node login example](../../../_images/trees-node-login-example.png)Figure 2. Example username and password authentication tree
>
> 6. Select the **Page Node**, and in the Properties pane, set the Stage property to `UsernamePassword`.
>
>    |   |                                                                                                            |
>    | - | ---------------------------------------------------------------------------------------------------------- |
>    |   | You can configure the node properties by selecting a node and altering properties in the right-hand panel. |
>
>    One of the samples uses this specific value to determine the custom UI to display.
>
> 7. Click **Save**.

> **Collapse: Task 4. Register a public OAuth 2.0 client**
>
> Public clients do not use a client secret to obtain tokens because they are unable to keep them hidden. The Ping (ForgeRock) SDKs commonly use this type of client to obtain tokens, as they cannot guarantee safekeeping of the client credentials in a browser or on a mobile device.
>
> To register a *public* OAuth 2.0 client application for use with the SDKs in AM, follow these steps:
>
> 1. Log in to the PingAM admin UI as an administrator.
>
> 2. Navigate to [icon: list-alt, set=fa]Applications > OAuth 2.0 > Clients, and then click [icon: plus, set=fa]Add Client.
>
> 3. In Client ID, enter `sdkPublicClient`.
>
> 4. Leave Client secret empty.
>
> 5. In Redirection URIs, enter the following values:
>
>    `https://localhost:8443/callback.html`
>
>    |   |                                                                        |
>    | - | ---------------------------------------------------------------------- |
>    |   | Also add any other domains where you will be hosting SDK applications. |
>
> 6. In Scopes, enter the following values:
>
>    `openid profile email`
>
> 7. Click Create.
>
>    PingAM creates the new OAuth 2.0 client, and displays the properties for further configuration.
>
> 8. On the Core tab:
>
>    1. In Client type, select `Public`.
>
>    2. Disable Allow wildcard ports in redirect URIs.
>
>    3. Click Save Changes.
>
> 9. On the Advanced tab:
>
>    1. In Grant Types, enter the following values:
>
>       ```none
>       Authorization Code
>       Refresh Token
>       ```
>
>    2. In Token Endpoint Authentication Method, select `None`.
>
>    3. Enable the Implied consent property.
>
> 10. Click Save Changes.

> **Collapse: Task 5. Register a confidential OAuth 2.0 client**
>
> Confidential clients are able to store credentials securely and are commonly used for server-to-server communication.
>
> To register a *confidential* OAuth 2.0 client application for use with the SDKs in AM, follow these steps:
>
> 1. Log in to the PingAM admin UI as an administrator.
>
> 2. Navigate to [icon: list-alt, set=fa]Applications > OAuth 2.0 > Clients, and then click [icon: plus, set=fa]Add Client.
>
> 3. In Client ID, enter `sdkConfidentialClient`.
>
> 4. In Client Secret, enter a strong password and make a note of it for later use.
>
>    For example, `5tr0ngP@S5w0rd!`
>
>    |   |                                                                                                                                               |
>    | - | --------------------------------------------------------------------------------------------------------------------------------------------- |
>    |   | The client secret is not available to view after this step.If you forget it, you must reset the secret and reconfigure any connected clients. |
>
> 5. In Default Scopes, enter `am-introspect-all-tokens`.
>
>    PingAM creates the new OAuth 2.0 client and displays the properties for further configuration.
>
> 6. On the Advanced tab:
>
>    1. Enable the Implied consent property.
>
> 7. Click Save Changes.

> **Collapse: Task 6. Configure the OAuth 2.0 provider service**
>
> The provider specifies the supported OAuth 2.0 configuration options for a realm.
>
> To ensure the PingAM OAuth 2.0 provider service is configured for use with the Ping (ForgeRock) SDKs, follow these steps:
>
> 1. Log in to the PingAM admin UI as an administrator.
>
> 2. In the left panel, click [icon: plug, set=fa]Services.
>
> 3. In the list of services, click OAuth2 Provider.
>
> 4. On the Core tab, ensure Issue Refresh Tokens is enabled.
>
> 5. On the Consent tab, ensure Allow Clients to Skip Consent is enabled.
>
> 6. Click Save Changes.

## Next

Next, you can [download the sample repository](01_download_samples.html).

---

---
title: Configuring style properties
description: "Configure the Advanced Identity Cloud/PingAM Login Widget style element: colors, fonts, logos, password visibility, stage icons, header sections, and theme properties"
component: login-widget
page_id: login-widget:login-widget:customize/styles/style-properties
canonical_url: https://developer.pingidentity.com/login-widget/login-widget/customize/styles/style-properties.html
llms_txt: https://developer.pingidentity.com/login-widget/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: Tue, 12 Aug 2026 00:00:00 +0000
keywords: ["Customization", "User Interface", "Style", "Configuration", "CSS", "Properties"]
section_ids:
  adding_a_header_section: Adding a header section
  configuring_theme_colors_and_fonts: Configuring theme colors and fonts
  see_also: See also
---

# Configuring style properties

Use the `style` configuration element to configure the look and feel of the Advanced Identity Cloud/PingAM Login Widget. Style properties are set as part of the initial widget configuration, before the widget starts. Pass them to `configure()` and await it before starting any journey.

See [Step 4. Configure the widget](../../tutorial/04-configure-sdk.html) for more on the configuration step.

![modal theme params en](../../../_images/LAW/modal-theme-params-en.png)Figure 1. Use the `style` property to control aspects of the display

*Key*:

1. Use `style/logo` to add images for use in dark or light modes

2. Set `style/stage/icon` to `true` to render UI specific to certain stage parameter values. Supported stage values are:

   * `OneTimePassword` - enable the Advanced Identity Cloud/PingAM Login Widget to display one-time password entry forms correctly.

   * `DefaultRegistration` - adds UI elements to the display most suitable for user self-registration forms.

   * `DefaultLogin` - adds UI elements to the display most suitable for user log in forms.

3. A section that displays the Page Header and Page Description fields from the page node configuration

4. To float labels above their respective fields, set `style/labels` to `floating`

5. Use `style/showPassword` to control how the password visibility toggle is rendered

Adding logos and enabling icons

```javascript
import { configure } from '@forgerock/login-widget';

await configure({
  serverConfig: {
    wellknown: 'https://openam-forgerock-sdks.forgeblocks.com/am/oauth2/realms/root/realms/alpha/.well-known/openid-configuration',
  },
  style: {
    checksAndRadios: 'animated',
    labels: 'floating',
    showPassword: 'button',
    logo: {
      dark: 'https://example.com/img/white-logo.png',
      light: 'https://example.com/img/black-logo.png',
      height: 300,
      width: 400,
    },
    sections: {
      header: false,
    },
    stage: {
      icon: true,
    },
  },
});
```

|   |                                                                                               |
| - | --------------------------------------------------------------------------------------------- |
|   | The `sections` property only applies to the modal form factor and not the inline form factor. |

Learn more about the available properties in [Style configuration options](../../widget-api-reference.html#config-style) in the [API reference](../../widget-api-reference.html).

## Adding a header section

Enabling the header section separates the logo or branding from the journey form.

If you set `header: true` within the `style/sections` property, the modal uses a section with a separating line, and extra space:

![modal widget with header](../../../_images/android/modal-widget-with-header.png)Figure 2. Modal form factor with header enabled

By default, the separating section is not enabled:

![modal widget without header](../../../_images/android/modal-widget-without-header.png)Figure 3. Default modal form factor with header disabled

## Configuring theme colors and fonts

Use the properties in the `style/theme` configuration element to set brand colors, typography, border radii, and per-component styles.

|   |                                                                                                                                                               |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | For structural changes beyond what these properties expose, such as spacing and breakpoints, see [Customizing default themes at build time](build-time.html). |

Each `style/theme` configuration property maps to a scoped CSS custom property on the widget's root element.

```javascript
import { configure } from '@forgerock/login-widget';

await configure({
  serverConfig: {
    wellknown: 'https://openam-forgerock-sdks.forgeblocks.com/am/oauth2/realms/root/realms/alpha/.well-known/openid-configuration',
  },
  style: {
    theme: {
      primaryColor: '#f46200',
      secondaryColor: '#003049',
      backgroundColor: '#ffffff',
      linkColor: '#f46200',
      fontFamily: 'Inter, sans-serif',
      buttonBorderRadius: 8,
      cardBorderRadius: 12,
    },
  },
});
```

The `theme` properties available are as follows:

**style.theme properties**

| Property                                                                | Description                                                                                                                                                               |
| ----------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `primaryColor`, `primaryOffColor`                                       | Hex color values (6 or 8 digit, for example `#f46200` or `#f46200ff`) for the widget's primary brand color and its muted off-state variant.                               |
| `secondaryColor`                                                        | Hex color value for the widget's secondary brand color.                                                                                                                   |
| `backgroundColor`                                                       | Hex color for the page or modal background.                                                                                                                               |
| `cardBgColor`, `cardTextColor`                                          | Hex colors for card background and text.                                                                                                                                  |
| `bodyTextColor`                                                         | Hex color for general body text within the widget.                                                                                                                        |
| `linkColor`, `linkActiveColor`                                          | Hex colors for links in their default and active states.                                                                                                                  |
| `inputBgColor`, `inputBorderColor`, `inputLabelColor`, `inputTextColor` | Hex colors for form input background, border, label, and text.                                                                                                            |
| `inputFocusRingColor`                                                   | Hex color for the focus ring on form inputs.                                                                                                                              |
| `selectAccentColor`, `selectHoverBgColor`                               | Hex colors for `<select>` elements in their default and hover states.                                                                                                     |
| `buttonTextColor`                                                       | Hex color for button text.                                                                                                                                                |
| `buttonFocusRingColor`                                                  | Hex color for the focus ring on buttons.                                                                                                                                  |
| `fontFamily`                                                            | A CSS font family string, for example `Inter, sans-serif`.                                                                                                                |
| `logo`                                                                  | Full URL or base64 data URI to override the logo image. Applies a single logo regardless of color scheme. For separate light and dark variants, use `style.logo` instead. |
| `logoHeight`                                                            | Number of pixels for the logo height.                                                                                                                                     |
| `favicon`                                                               | Full URL for the browser tab icon.                                                                                                                                        |
| `buttonBorderRadius`, `cardBorderRadius`                                | Numbers, in pixels, controlling the corner rounding of buttons and cards.                                                                                                 |

|   |                                                                                                                                                                                                                                                                              |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | `theme.logo` accepts a single URL and is independent from `style.logo`, which accepts separate `dark` and `light` variants for the modal form factor. Use `style.logo` if you need different images per color scheme; use `theme.logo` for a single logo applied everywhere. |

## See also

* [Customizing default themes at build time](build-time.html): structural style changes requiring a Tailwind rebuild

* [Style configuration options](../../widget-api-reference.html#config-style): full `style` configuration reference

---

---
title: Customizing default themes at build time
description: Customize Advanced Identity Cloud/PingAM Login Widget themes at build time by modifying the Tailwind configuration file and rebuilding the widget from source
component: login-widget
page_id: login-widget:login-widget:customize/styles/build-time
canonical_url: https://developer.pingidentity.com/login-widget/login-widget/customize/styles/build-time.html
llms_txt: https://developer.pingidentity.com/login-widget/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: Tue, 12 Aug 2026 00:00:00 +0000
keywords: ["Customization", "User Interface", "Tailwind", "Build"]
page_aliases: ["login-widget:theme.adoc", "login-widget:customize/theme.adoc"]
section_ids:
  switch_between_light_and_dark_themes: Switch between light and dark themes
  customizing_the_default_themes: Customizing the default themes
  recommendations: Recommendations
  supported_customization: Supported customization
---

# Customizing default themes at build time

The Advanced Identity Cloud/PingAM Login Widget provides a default theme with both light and dark modes.

![law dark theme example en](../../../_images/LAW/law-dark-theme-example-en.png)Figure 1. Example of the modal component in dark mode

You can alter these themes by updating a Tailwind configuration file and rebuilding the Advanced Identity Cloud/PingAM Login Widget

|   |                                                                                                                                                                                                                                |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | If your organization's UX or brand requires pixel-perfect UIs developed in accordance to Photoshop, Figma or other "design mocks", Advanced Identity Cloud/PingAM Login Widget might not be able to support such requirements. |

## Switch between light and dark themes

To switch to the dark mode, you can manually add `tw_dark` to the `<body>` element:

```html
<body class="tw_dark"></body>
```

The Advanced Identity Cloud/PingAM Login Widget defaults to the light mode if the class is not present.

You can programmatically apply the class if required:

```javascript
const prefersDarkTheme = window.matchMedia('(prefers-color-scheme: dark)').matches;
if (prefersDarkTheme) {
    document.body.classList.add('tw_dark');
}
```

## Customizing the default themes

To reconfigure the theme to use different colors, fonts, or sizing you can provide new values to the Tailwind configuration file and rebuild the Advanced Identity Cloud/PingAM Login Widget, as follows:

1. Download the Advanced Identity Cloud/PingAM Web Login Framework from the GitHub repository:

   `git clone https://github.com/ForgeRock/forgerock-web-login-framework.git`

2. In a terminal window, navigate to the root of the Advanced Identity Cloud/PingAM Web Login Framework:

   `cd forgerock-web-login-framework`

3. Run `pnpm` to download and install the required packages and modules:

   `pnpm install`

4. Run the development script:

   `pnpm run dev`

5. Run Storybook:

   `pnpm run storybook`

   Make a note of the URLs to the Storybook UI listed in the terminal output:

   ![law custom theme storybook url en](../../../_images/LAW/law-custom-theme-storybook-url-en.png)Figure 2. URLs to the Storybook UI

6. Open the `tailwind.config.cjs` file in the root of the Advanced Identity Cloud/PingAM Web Login Framework and adjust your theme by adding them under the `extend` property:

   ```javascript
   // tailwind.config.cjs
   module.exports = {
     content: ['./src/**/*.{html,js,svelte,ts}', './.storybook/preview-head.html'],
     darkMode: 'class',
     presets: [require('./themes/default/config.cjs')],
     theme: {
       extend: {
         // Add your customizations here
         colors: {
           body: {
             light: 'darkblue',
           },
           primary: {
             dark: 'darkorange',
           },
           background: {
             light: "gainsboro",
           },
         },
         fontFamily: {
           sans: ['Impact'],
         },
       },
     },
   };
   ```

7. Navigate to the Storybook UI provided in the terminal output earlier to view your changes:

   ![law custom theme storybook en](../../../_images/LAW/law-custom-theme-storybook-en.png)Figure 3. Customized registration modal in Storybook

   Changes you make to the `tailwind.config.cjs` file are automatically reflected in the Storybook UI when you save them to disk.

### Recommendations

Anything configurable in Tailwind is also configurable in the theme. The custom properties the default theme uses are stored in the `/themes/default/tokens.cjs` file.

We recommend you do not directly modify these default theme files. Only modify the root `tailwind.config.cjs`.

### Supported customization

Using the methods on this page, you can customize:

* Colors

* Fonts

* Type sizes

* Spacing

* Breakpoints

---

---
title: Customizing the Advanced Identity Cloud/PingAM Login Widget
description: The Advanced Identity Cloud/PingAM Login Widget is designed to be flexible and can be customized to suit many different situations.
component: login-widget
page_id: login-widget:login-widget:customize/index
canonical_url: https://developer.pingidentity.com/login-widget/login-widget/customize/index.html
llms_txt: https://developer.pingidentity.com/login-widget/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: Tue, 25 Mar 2025 11:00:37 +0100
keywords: ["PingOne Advanced Identity Cloud", "PingAM", "Journeys", "Setup &amp; Configuration", "Source Code", "Use Case", "SDK", "IdP"]
section_ids:
  localization: Localization
  styling: Styling
---

# Customizing the Advanced Identity Cloud/PingAM Login Widget

The **Advanced Identity Cloud/PingAM Login Widget** is designed to be flexible and can be customized to suit many different situations.

Learn more about customizing the widget in the sections below:

## [Localization](localize.html)

Alter the default text that appears in the Advanced Identity Cloud/PingAM Login Widget, including how to respond to different locales.

[**Read more**[icon: chevrons-right, set=fas, size=xs]](localize.html)

## Styling

The Advanced Identity Cloud/PingAM Login Widget supports two approaches to styling.

Use **Configuring style properties** to set brand colors, typography, and component styles through the JavaScript API, without having to rebuild.

Use **Building styles into the widget** when you need to change structural properties such as spacing, breakpoints, or the full color palette, which require rebuilding the widget from source.

[icon: palette, set=fad, size=3x]

#### [Configuring style properties](styles/style-properties.html)

Set brand colors, typography, border radii, and per-component styles through the `style/theme` configuration element during initialization.

[icon: code, set=fad, size=3x]

#### [Building styles into the widget](styles/build-time.html)

Modify spacing, breakpoints, and color palettes by rebuilding the widget with a customized Tailwind configuration.

---

---
title: Implement a CAPTCHA
description: The Advanced Identity Cloud/PingAM Login Widget supports the use of a CAPTCHA (Completely Automated Public Turing test to tell Computers and Humans Apart), which helps to prevent automated scripts from attempting to authenticate to your servers.
component: login-widget
page_id: login-widget:login-widget:use-cases/how-to-captcha
canonical_url: https://developer.pingidentity.com/login-widget/login-widget/use-cases/how-to-captcha.html
llms_txt: https://developer.pingidentity.com/login-widget/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: Tue, 28 Jul 2026 00:00:00 +0000
keywords: ["Integration", "Journeys", "Features", "Social Authentication", "Standards"]
section_ids:
  supported_captcha_variants: Supported CAPTCHA variants
  visible_and_invisible_captcha_modes: Visible and invisible CAPTCHA modes
  configure_your_app: Configure your app
  test_a_captcha: Test a CAPTCHA
  troubleshooting: Troubleshooting
---

# Implement a CAPTCHA

The Advanced Identity Cloud/PingAM Login Widget supports the use of a CAPTCHA (Completely Automated Public Turing test to tell Computers and Humans Apart), which helps to prevent automated scripts from attempting to authenticate to your servers.

To use a CAPTCHA in the Advanced Identity Cloud/PingAM Login Widget, add a [CAPTCHA node](https://docs.pingidentity.com/auth-node-ref/latest/captcha.html) or [reCAPTCHA Enterprise node](https://docs.pingidentity.com/auth-node-ref/latest/recaptcha-enterprise.html) to your authentication journey.

## Supported CAPTCHA variants

Advanced Identity Cloud/PingAM Login Widget supports the following CAPTCHA variants:

| CAPTCHA variant                                                                         | Support                                                                                                             | Node                                                                                                      |
| --------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- |
| [hCaptcha](https://www.hcaptcha.com/)                                                   | [icon: check, set=fa]Active[icon: check, set=fa]Invisible[icon: times, set=fa]Passive / 99% Passive                 | [CAPTCHA node](https://docs.pingidentity.com/auth-node-ref/latest/captcha.html)                           |
| [reCAPTCHA v2](https://developers.google.com/recaptcha/docs/display)                    | [icon: check, set=fa]Full, including [Invisible reCAPTCHA](https://developers.google.com/recaptcha/docs/invisible). | [CAPTCHA node](https://docs.pingidentity.com/auth-node-ref/latest/captcha.html)                           |
| [reCAPTCHA v3](https://developers.google.com/recaptcha/docs/v3)                         | [icon: check, set=fa]Full                                                                                           | [CAPTCHA node](https://docs.pingidentity.com/auth-node-ref/latest/captcha.html)                           |
| [reCAPTCHA Enterprise](https://cloud.google.com/security/products/recaptcha-enterprise) | [icon: check, set=fa]Full, including invisible (score-based) mode.                                                  | [reCAPTCHA Enterprise node](https://docs.pingidentity.com/auth-node-ref/latest/recaptcha-enterprise.html) |

## Visible and invisible CAPTCHA modes

CAPTCHA providers typically offer two rendering modes:

* Visible (active) mode

  The CAPTCHA renders a visible widget, usually a checkbox, inside the login form. The user must interact with it before they can submit the form.

* Invisible mode

  No visible widget appears in the login form. Instead, the CAPTCHA runs an automated risk assessment in the background when the page loads. If the provider's scoring determines the request looks suspicious, it may surface a challenge popup for the user to complete. Otherwise, authentication proceeds without any visible interruption.

The Advanced Identity Cloud/PingAM Login Widget defaults to visible mode. To enable invisible mode, pass `mode: 'invisible'` in the `captcha` option when configuring the widget:

```javascript
import { configure } from '@forgerock/login-widget';

await configure({
    serverConfig: {
        wellknown: 'https://openam-forgerock-sdks.forgeblocks.com/am/oauth2/realms/root/realms/alpha/.well-known/openid-configuration',
    },
    // ... other config options ...
    captcha: {
        mode: 'invisible', // 'visible' (default) | 'invisible'
    },
});
```

The `mode` value applies to whichever CAPTCHA provider is configured in your authentication journey node, for example hCaptcha, reCAPTCHA v2, or reCAPTCHA Enterprise.

When invisible mode is active and the CAPTCHA challenge fails or expires, the Advanced Identity Cloud/PingAM Login Widget displays an inline error alert prompting the user to try again.

## Configure your app

The Advanced Identity Cloud/PingAM Login Widget automatically injects the CAPTCHA provider script into your page when it encounters a CAPTCHA callback. You do not need to add a `<script>` tag manually.

If you prefer to load the script yourself, for example to control when it loads relative to other resources, you can add it to the `<head>` of your page. The widget detects that the provider is already available and skips its own injection.

* **hCaptcha**

  ```html
  <script src="https://js.hcaptcha.com/1/api.js" async defer></script>
  ```

* **reCAPTCHA v2**

  ```html
  <script async src="https://www.google.com/recaptcha/api.js"></script>
  ```

* **reCAPTCHA v3**

  If pre-loading reCAPTCHA v3, append your site key as a `render` query parameter:

  ```html
  <script async src="https://www.google.com/recaptcha/api.js?render={reCAPTCHA_site_key}"></script>
  ```

  You can add a `recaptchaAction` property with a custom value when calling the journey. That value tags the event in the reCAPTCHA console so that you can track different usage:

  ```javascript
  import { journey } from '@forgerock/login-widget';

  const journeyEvents = journey();

  journeyEvents.start({
      journey: 'reCAPTCHAv3journey',
      // ...any other journey config required...
      recaptchaAction: 'loginVIPArea', // optional; falls back to journey name
  });
  ```

  If you do not provide a `recaptchaAction` value, the Advanced Identity Cloud/PingAM Login Widget attempts to use the name of the journey instead, if available.

* **reCAPTCHA Enterprise**

  The Advanced Identity Cloud/PingAM Login Widget handles the `ReCaptchaEnterpriseCallback` automatically when the journey contains the [reCAPTCHA Enterprise node](https://docs.pingidentity.com/auth-node-ref/latest/recaptcha-enterprise.html).

  No additional script setup is required beyond configuring the node in your authentication journey.

  For invisible (score-based) Enterprise keys, also set `captcha: { mode: 'invisible' }` in your widget configuration. Learn more in [Visible and invisible CAPTCHA modes](#visible_and_invisible_captcha_modes).

  You can add a `recaptchaAction` property with a custom value when calling the journey. That value tags the event in the reCAPTCHA Enterprise console so that you can track different usage:

  ```javascript
  import { journey } from '@forgerock/login-widget';

  const journeyEvents = journey();

  journeyEvents.start({
      journey: 'reCAPTCHAEnterpriseJourney',
      // ...any other journey config required...
      recaptchaAction: 'loginVIPArea', // falls back to journey name
  });
  ```

  |   |                                                                                                              |
  | - | ------------------------------------------------------------------------------------------------------------ |
  |   | For reCAPTCHA Enterprise, either `recaptchaAction` or `journey` must be provided for the CAPTCHA to execute. |

## Test a CAPTCHA

With your app configured, you can visit any journey that contains a [CAPTCHA node](https://docs.pingidentity.com/auth-node-ref/latest/captcha.html) or [reCAPTCHA Enterprise node](https://docs.pingidentity.com/auth-node-ref/latest/recaptcha-enterprise.html) to test a CAPTCHA with the Advanced Identity Cloud/PingAM Login Widget.

For example, the following image shows how the Advanced Identity Cloud/PingAM Login Widget displays a reCAPTCHA v2 challenge, alongside a platform username and platform password nodes, all within a single page node:

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
description: The Advanced Identity Cloud/PingAM Login Widget supports many common authentication and self-service use cases out of the box.
component: login-widget
page_id: login-widget:login-widget:use-cases
canonical_url: https://developer.pingidentity.com/login-widget/login-widget/use-cases.html
llms_txt: https://developer.pingidentity.com/login-widget/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: Tue, 28 Jul 2026 00:00:00 +0000
keywords: ["Integration", "Features"]
---

# Implement your use cases with the Advanced Identity Cloud/PingAM Login Widget

The Advanced Identity Cloud/PingAM Login Widget supports many common authentication and self-service use cases out of the box.

[icon: user-key, set=fadl, size=3x]

#### [Passkeys](use-cases/passkeys.html)

Register passkeys, and let users sign in with autofill

[icon: user-clock, set=fadl, size=3x]

#### [Multi-factor authentication](use-cases/how-to-oath-otp.html)

Register OATH and Push devices with a QR code, and verify one-time passwords

[icon: user-circle-plus, set=fadl, size=3x]

#### [Social sign-on](use-cases/how-to-social-login.html)

Authenticate users with external identity providers

[icon: wand-magic-sparkles, set=fadl, size=3x]

#### [Magic links](use-cases/how-to-magic-links.html)

Suspend and resume authentication journeys via email

[icon: magnifying-glass-chart, set=fadl, size=3x]

#### [CAPTCHA](use-cases/how-to-captcha.html)

Detect and block automated authentication attempts

---

---
title: Implementing passkey autofill
description: Passkey autofill, sometimes known as WebAuthn Conditional UI, lets users sign in by selecting a passkey directly from the browser's native autofill picker on the username field.
component: login-widget
page_id: login-widget:login-widget:use-cases/passkeys/passkey-autofill
canonical_url: https://developer.pingidentity.com/login-widget/login-widget/use-cases/passkeys/passkey-autofill.html
llms_txt: https://developer.pingidentity.com/login-widget/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: Tue, 28 Jul 2026 00:00:00 +0000
keywords: ["WebAuthn", "Passkeys", "Conditional UI", "FIDO2", "Autofill"]
section_ids:
  how_it_works: How it works
  passkey-autocomplete-journey: Configuring your authentication journey
  browser_and_https_requirements: Browser and HTTPS requirements
  configuring_the_login_widget_for_passkey_autofill: Configuring the Login Widget for passkey autofill
  related_use_cases: Related use cases
---

# Implementing passkey autofill

Passkey autofill, sometimes known as **WebAuthn Conditional UI**, lets users sign in by selecting a passkey directly from the browser's native autofill picker on the username field.

When the user clicks or tabs into the username field, the browser presents any passkeys registered for that site.

Selecting one completes authentication immediately, with no password required. If the user has no passkeys, or dismisses the picker, the login form continues to work as normal, so the experience degrades gracefully with no disruption.

The Advanced Identity Cloud/PingAM Login Widget activates passkey autofill automatically when it detects the right combination of callbacks from the server.

No additional widget configuration is required.

|   |                                                                                                                                                                                                                                                                                                                                                                 |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Passkey autofill requires PingAM 8.1 or later, or PingOne Advanced Identity Cloud.It depends on version 2 of both the [WebAuthn Authentication node](https://docs.pingidentity.com/auth-node-ref/latest/webauthn-authentication.html) and the [Page node](https://docs.pingidentity.com/auth-node-ref/latest/page.html), which were introduced in that release. |

|   |                                                                                                                                             |
| - | ------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Before a user can sign in with passkey autofill, they need a registered passkey. Refer to [Registering a passkey](register-a-passkey.html). |

## How it works

When the Advanced Identity Cloud/PingAM Login Widget encounters a [page node configured for passkey autocomplete](#passkey-autocomplete-journey), it takes the following actions:

1. Adds `autocomplete="username webauthn"` to the username field, which signals to the browser that passkey autofill should be offered.

2. Starts a background [conditional credential request](https://www.w3.org/TR/credential-management-1/#mediation-requirements) using the WebAuthn challenge from the `MetadataCallback`.

The browser then displays its native passkey picker attached to the username field:

![passkeys autofill sample app](../../../_images/passkeys-autofill-sample-app.png)

When the user selects a passkey, the widget completes the WebAuthn assertion and submits the step automatically.

## Configuring your authentication journey

To configure an authentication journey for passkey autocomplete, add the following nodes together inside a **[Page node](https://docs.pingidentity.com/auth-node-ref/latest/page.html) (version 2)**:

* **[Platform Username node](https://docs.pingidentity.com/auth-node-ref/latest/platform-username.html)**

  Collects the username.

  To add the required `autocomplete` attributes to the rendered field in the Login Widget, add the following values to the **Autocomplete Values** property of the node, in this order:

  1. `username`

  2. `webauthn`

  The result resembles the following:

  ![passkeys autofill journey username node](../../../_images/passkeys-autofill-journey-username-node.png)

* **[WebAuthn Authentication node](https://docs.pingidentity.com/auth-node-ref/latest/webauthn-authentication.html) (version 2)**

  Issues the WebAuthn challenge and handles the assertion response.

  The following settings are required for passkey autofill:

  * **Mediation**

    Set to `CONDITIONAL`.

    This is what instructs the browser to show passkeys inline in the autofill UI rather than triggering a separate popup.

  * **Username from device**

    Must be **Enabled**.

  * **Version**

    Must be `v2.0` or later. This version contains an outcome path so that users without a passkey can fall through to a normal username and password flow.

Connect the **Outcome** outcome to nodes that handle username and password authentication.

Connect the **Success** outcome to nodes that handle the successful authentication using the passkey. For example, you could connect directly to the green checkmark **Success** node to complete the journey.

The result resembles the following:

![passkey autofill journey](../../../_images/passkey-autofill-journey.png)Figure 1. Basic authentication journey for passkey autofill

## Browser and HTTPS requirements

Passkey autofill is a browser-native capability that requires a secure context:

* **HTTPS** is required in production. Browsers will not expose passkeys on plain HTTP origins.

  * **`localhost`** is treated as a secure context by browsers, so passkey autofill works without HTTPS during local development.

* The browser must support WebAuthn Conditional UI. Current versions of Chrome, Edge, Safari, and Firefox all support it.

  The widget checks for support at runtime; if the browser does not support conditional mediation, the username field behaves as normal with no error.

## Configuring the Login Widget for passkey autofill

No additional widget-specific configuration is required.

The Advanced Identity Cloud/PingAM Login Widget detects and enables passkey autofill automatically.

## Related use cases

* [Registering a passkey](register-a-passkey.html)

  Let a signed-in user register a new passkey.

---

---
title: Integrate the Advanced Identity Cloud/PingAM Login Widget into a ReactJS web app
description: In this tutorial, you will learn how to integrate the Advanced Identity Cloud/PingAM Login Widget into a simple React app that you scaffold using Vite.
component: login-widget
page_id: login-widget:login-widget:integrations/how-integrate-with-react
canonical_url: https://developer.pingidentity.com/login-widget/login-widget/integrations/how-integrate-with-react.html
llms_txt: https://developer.pingidentity.com/login-widget/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: Tue, 28 Jul 2026 00:00:00 +0000
keywords: ["Integration", "Third-Party", "Framework"]
section_ids:
  requirements: Requirements
  configure_your_server: Configure your server
  create_a_vite_app: Create a Vite app
  install_the_advanced_identity_cloudpingam_login_widget: Install the Advanced Identity Cloud/PingAM Login Widget
  prepare_the_html: Prepare the HTML
  prepare_the_css: Prepare the CSS
  configure_the_advanced_identity_cloudpingam_login_widget_at_app_boot: Configure the Advanced Identity Cloud/PingAM Login Widget at app boot
  instantiate_and_mount_the_advanced_identity_cloudpingam_login_widget: Instantiate and mount the Advanced Identity Cloud/PingAM Login Widget
  controlling_the_component: Controlling the component
  start_a_journey: Start a journey
  authenticating_a_user: Authenticating a user
  logging_a_user_out: Logging a user out
---

# Integrate the Advanced Identity Cloud/PingAM Login Widget into a ReactJS web app

In this tutorial, you will learn how to integrate the Advanced Identity Cloud/PingAM Login Widget into a simple React app that you scaffold using Vite.

If you want to run a complete React application instead of creating one from scratch, see [Try the ReactJS Todo Login Widget sample](../try-it-out/reactjs-todo-login-widget/index.html). That guide uses the Webpack-based sample in the SDK Sample Apps repository and its shared Todo API.

You install the Advanced Identity Cloud/PingAM Login Widget using `npm`, add an element to the HTML file for mounting the modal form factor, and wrap the app's CSS in a layer.

With the app prepared, you then configure the widget at the top level of your app, import and instantiate its components, and start a journey. You subscribe to the events the Advanced Identity Cloud/PingAM Login Widget emits so that the app can respond and display the appropriate UI.

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

## Configure the Advanced Identity Cloud/PingAM Login Widget at app boot

`configure()` is asynchronous and must complete before any other Widget API is called. The cleanest place to `await` it in a Vite + React app is in `src/main.jsx`, before rendering the app.

In your IDE, open `src/main.jsx` and update it to import the widget CSS, `await configure()`, and only then render the app:

```javascript
import React from 'react';
import ReactDOM from 'react-dom/client';
import { configure } from '@forgerock/login-widget';
import '@forgerock/login-widget/widget.css';
import App from './App.jsx';
import './index.css';

await configure({
  serverConfig: {
    wellknown: 'https://openam-forgerock-sdks.forgeblocks.com/am/oauth2/realms/root/realms/alpha/.well-known/openid-configuration',
  },
  oidcClient: {
    clientId: 'sdkPublicClient',
    redirectUri: `${window.location.origin}/callback`,
    scope: 'openid profile email address',
  },
});

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
);
```

|   |                                                                                                                                                        |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | Vite supports top-level `await` in modules by default.If you use a bundler that does not, wrap the `configure()` call and the render in an async IIFE. |

## Instantiate and mount the Advanced Identity Cloud/PingAM Login Widget

Now that the widget is configured at app boot, `App.jsx` can instantiate it against the widget root element you added to `index.html`.

Open `src/App.jsx`. Import `Widget` from `@forgerock/login-widget` and `useEffect` from React:

```javascript
import React, { useEffect, useState } from 'react';
import Widget from '@forgerock/login-widget';
```

Inside the `App` component, write a `useEffect` with an empty dependency array to instantiate the widget once when the component mounts and destroy it on unmount:

```javascript
function App() {

  useEffect(() => {
    const widget = new Widget({ target: document.getElementById('widget-root') });

    return () => {
      widget.$destroy();
    };
  }, []);

  // ...
```

|   |                                                                                                                                                                                                                          |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | The empty dependency array tells React this effect has no dependencies and should only run once.The returned function destroys the widget when the component unmounts, so a remount does not add two widgets to the DOM. |

In your browser, the app doesn't look any different. This is because the widget, by default, is invisible at startup.

To ensure it is working as expected, inspect the DOM in the browser developer tools.

Open the `<div id="widget-root">` element in the DOM, and you should see the Advanced Identity Cloud/PingAM Login Widget mounted within it:

![law react instantiated en](../../_images/LAW/law-react-instantiated-en.png)Figure 2. Instantiated and mounted modal form factor

## Controlling the component

An invisible Advanced Identity Cloud/PingAM Login Widget is not all that useful, so your next task is to pull in the `component` module to manage the component's events.

Add `component` to the list of imports and call it inside the component:

```javascript
import Widget, { component } from '@forgerock/login-widget';

// ...

function App() {
  const componentEvents = component();

  // ...
```

Now that you have a reference to the `component` events observable, you can trigger an event such as `open`, and you can also listen for events.

Repurpose the existing count is 0 button within the `App` component.

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

This is expected, because the Advanced Identity Cloud/PingAM Login Widget does not yet have a journey to render.

Click the button in the top-right to close the modal. The modal should be dismissed as expected.

## Start a journey

Now that you have the modal mounted and functional, add the `journey` module so you can start an authentication flow.

Add `journey` to the imports and call it inside the component to get a `journeyEvents` observable:

```javascript
import Widget, { component, journey } from '@forgerock/login-widget';

// ...

function App() {
  const componentEvents = component();
  const journeyEvents = journey();

  // ...
```

Within the Login button's `onClick` handler, call `journeyEvents.start()` so that clicking the button both opens the modal and requests the first authentication step from the server:

```javascript
<button onClick={() => {
    journeyEvents.start();
    componentEvents.open();
  }}>
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

Next, use React's `useState` hook to save the user information.

1. Add a `useState` call at the top of the `App` component, defaulting to `null`

2. Change the condition from just truthy to `userInfo !== event.user.response`

3. Replace the `console.log` with the `setUserInfo` function

4. Add the `userInfo` variable in the dependency array of the `useEffect`

The top part of your `App` function component should resemble the following:

```javascript
function App() {
  const [userInfo, setUserInfo] = useState(null);
  const componentEvents = component();
  const journeyEvents = journey();

  useEffect(() => {
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
import Widget, { component, journey, user } from '@forgerock/login-widget';
```

Next, configure the app to display the button as a Login button when the user has not yet authenticated and a Logout button when the user has already logged in:

1. Wrap the button element with braces containing a ternary, using the *falsiness* of the `userInfo` as the condition

2. When no `userInfo` exists—​the user is logged out—​render the Login button

3. Write a Logout button with an `onClick` handler to run the `user.logout` function

The resulting JSX should resemble this:

```javascript
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
llms_txt: https://developer.pingidentity.com/login-widget/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
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
llms_txt: https://developer.pingidentity.com/login-widget/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: Mon, 3 Jul 2023 18:00:37 +0100
---

# Integrating the Advanced Identity Cloud/PingAM Login Widget

Find out how you can integrate the Advanced Identity Cloud/PingAM Login Widget with different frameworks and libraries.

* [Integrate with PingOne Protect for risk evaluations](integrations/integrate-with-pingone-protect.html)

  The Advanced Identity Cloud/PingAM Login Widget can integrate with PingOne Protect to evaluate the risk involved in a transaction.

  Use PingOne Protect in your authentication journeys to help prevent identity fraud by incorporating advanced features and real-time detection.

* [Integrate Login Widget into a ReactJS web app](integrations/how-integrate-with-react.html)

  Learn how to integrate the Advanced Identity Cloud/PingAM Login Widget into a simple ReactJS web app that you scaffold using Vite.

* [Try the ReactJS Todo Login Widget sample](try-it-out/reactjs-todo-login-widget/index.html)

  Configure and run the Webpack-based React Todo sample from the [SDK Sample Apps repository](https://github.com/ForgeRock/sdk-sample-apps/tree/main/javascript/reactjs-todo-login-widget). The sample demonstrates Login and Registration journeys, a protected Todo API, and login and logout with the Advanced Identity Cloud/PingAM Login Widget.

---

---
title: Localizing the widget
description: The Advanced Identity Cloud/PingAM Login Widget uses variables with default values for all strings it displays when rendering the user interface.
component: login-widget
page_id: login-widget:login-widget:customize/localize
canonical_url: https://developer.pingidentity.com/login-widget/login-widget/customize/localize.html
llms_txt: https://developer.pingidentity.com/login-widget/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: Tue, 28 Jul 2026 00:00:00 +0000
keywords: ["Customization", "User Interface", "Locale"]
---

# Localizing the widget

The Advanced Identity Cloud/PingAM Login Widget uses variables with default values for all strings it displays when rendering the user interface.

> **Collapse: Show variable names and default values**
>
> **Default localization values**
>
> | Variable                                                            | Default text                                                                                                                                                                                                                                                                                                                     |
> | ------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
> | `adminRegInvalidInviteHeader`                                       | Invitation not valid                                                                                                                                                                                                                                                                                                             |
> | `adminRegInvalidInviteDescription`                                  | This invitation can't be used. Please contact your administrator or \<a href='https\://support.pingidentity.com/' target='\_blank' rel='noopener noreferrer'>Ping Support\</a> for help.                                                                                                                                         |
> | `adminRegOtpHeader`                                                 | Admin Invite Code                                                                                                                                                                                                                                                                                                                |
> | `adminRegOtpDescription`                                            | We've sent a 6-digit code to your email. Enter it below to continue.                                                                                                                                                                                                                                                             |
> | `adminRegOtpError`                                                  | That code isn't correct or may have expired. Please try again.                                                                                                                                                                                                                                                                   |
> | `adminRegOtpResendPrompt`                                           | Didn't get a code?                                                                                                                                                                                                                                                                                                               |
> | `adminRegOtpResend`                                                 | Resend                                                                                                                                                                                                                                                                                                                           |
> | `adminRegPrivacyPolicyHeader`                                       | Accept Privacy Policy                                                                                                                                                                                                                                                                                                            |
> | `adminRegPrivacyPolicyDescription`                                  | Select your region of residence to review the applicable privacy policy.                                                                                                                                                                                                                                                         |
> | `adminRegPrivacyPolicySelectRegion`                                 | Region of residence                                                                                                                                                                                                                                                                                                              |
> | `adminRegPrivacyPolicyAgreement`                                    | I agree to the Ping Identity \<a target='\_blank' rel='noopener noreferrer' href='https\://www\.pingidentity.com/en-us/docs/legal/privacy'>privacy policy\</a>.                                                                                                                                                                  |
> | `adminRegSendVerificationCode`                                      | Send Verification Code                                                                                                                                                                                                                                                                                                           |
> | `adminRegWelcomeHeader`                                             | Welcome to PingOne Advanced Identity Cloud                                                                                                                                                                                                                                                                                       |
> | `adminRegWelcomeDescriptionPre`                                     | You've been invited to administer the                                                                                                                                                                                                                                                                                            |
> | `adminRegWelcomeDescriptionPost`                                    | tenant in PingOne Advanced Identity Cloud.                                                                                                                                                                                                                                                                                       |
> | `adminRegWelcomeVerification`                                       | Before you can begin, we need to verify your email address. Click the button below and we'll send you a one-time verification code.                                                                                                                                                                                              |
> | `alreadyHaveAnAccount`                                              | Already have an account? \<a href='?journey'>Sign in here!\</a>                                                                                                                                                                                                                                                                  |
> | `backToDefault`                                                     | Back to Sign In                                                                                                                                                                                                                                                                                                                  |
> | `backToLogin`                                                       | Back to Sign In                                                                                                                                                                                                                                                                                                                  |
> | `captchaError`                                                      | CAPTCHA verification failed. Please try again.                                                                                                                                                                                                                                                                                   |
> | `closeModal`                                                        | Close                                                                                                                                                                                                                                                                                                                            |
> | `charactersCannotRepeatMoreThan`                                    | Character cannot repeat more than {max} times                                                                                                                                                                                                                                                                                    |
> | `charactersCannotRepeatMoreThanCaseInsensitive`                     | Character cannot repeat more than {max} times (case insensitive)                                                                                                                                                                                                                                                                 |
> | `checkYourEmail`                                                    | Check your email                                                                                                                                                                                                                                                                                                                 |
> | `chooseDifferentUsername`                                           | Please choose a different username.                                                                                                                                                                                                                                                                                              |
> | `chooseYourDeviceForIdentityVerification`                           | Choose your device for identity verification.                                                                                                                                                                                                                                                                                    |
> | `confirmPassword`                                                   | Confirm password                                                                                                                                                                                                                                                                                                                 |
> | `constraintViolationForPassword`                                    | Password does not meet the requirements.                                                                                                                                                                                                                                                                                         |
> | `constraintViolationForValue`                                       | Value does not meet the requirements.                                                                                                                                                                                                                                                                                            |
> | `continueButton`                                                    | Continue                                                                                                                                                                                                                                                                                                                         |
> | `continueWith`                                                      | Continue with                                                                                                                                                                                                                                                                                                                    |
> | `copyAndPasteUrlBelow`                                              | Or, copy and paste the URL below into your authentictor app.                                                                                                                                                                                                                                                                     |
> | `copyUrl`                                                           | Copy URL                                                                                                                                                                                                                                                                                                                         |
> | `customSecurityQuestion`                                            | Custom security question                                                                                                                                                                                                                                                                                                         |
> | `deviceName`                                                        | Device name                                                                                                                                                                                                                                                                                                                      |
> | `doesNotMeetMinimumCharacterLength`                                 | At least {min} character(s)                                                                                                                                                                                                                                                                                                      |
> | `downloadTheApp`                                                    | Download the app                                                                                                                                                                                                                                                                                                                 |
> | `dontGetLockedOut`                                                  | Don't get locked out of your account!                                                                                                                                                                                                                                                                                            |
> | `dontHaveAnAccount`                                                 | No account? \<a href='?journey=Registration'>Register here!\</a>                                                                                                                                                                                                                                                                 |
> | `ensurePasswordIsMoreThan`                                          | Password must contain at least {minPasswordLength} character(s).                                                                                                                                                                                                                                                                 |
> | `ensurePasswordHasOne`                                              | Password must contain at least 1 capital letter, 1 number, and 1 special character.                                                                                                                                                                                                                                              |
> | `enterVerificationCode`                                             | Enter verification code                                                                                                                                                                                                                                                                                                          |
> | `exceedsMaximumCharacterLength`                                     | Exceeds maximum of {max} characters                                                                                                                                                                                                                                                                                              |
> | `fieldCanNotContainFollowingCharacters`                             | Cannot contain these character(s): {chars}                                                                                                                                                                                                                                                                                       |
> | `fieldCanNotContainFollowingValues`                                 | Cannot contain these value(s): {fields}                                                                                                                                                                                                                                                                                          |
> | `forgotPassword`                                                    | Forgot password?                                                                                                                                                                                                                                                                                                                 |
> | `forgotUsername`                                                    | Forgot username?                                                                                                                                                                                                                                                                                                                 |
> | `getAuthenticatorApp`                                               | Set up the ForgeRock Authenticator                                                                                                                                                                                                                                                                                               |
> | `getAuthenticatorAppDescription`                                    | To get started, you need to register your device using the ForgeRock Authenticator app.                                                                                                                                                                                                                                          |
> | `getAuthenticatorAppLinks`                                          | Get the app from the \<a href='https\://itunes.apple.com/app/forgerock-authenticator/id1038442926' target='\_blank' rel='noopener noreferrer'>Apple App Store\</a> or on \<a href='https\://play.google.com/store/apps/details?id=com.forgerock.authenticator' target='\_blank' rel='noopener noreferrer'>Google Play Store\</a> |
> | `givenName`                                                         | First name                                                                                                                                                                                                                                                                                                                       |
> | `inputRequiredError`                                                | Value is required                                                                                                                                                                                                                                                                                                                |
> | `loading`                                                           | Loading …​                                                                                                                                                                                                                                                                                                                       |
> | `loginButton`                                                       | Sign in                                                                                                                                                                                                                                                                                                                          |
> | `loginFailure`                                                      | Sign in failed                                                                                                                                                                                                                                                                                                                   |
> | `loginHeader`                                                       | Sign in                                                                                                                                                                                                                                                                                                                          |
> | `loginSuccess`                                                      | Sign in successful!                                                                                                                                                                                                                                                                                                              |
> | `mail`                                                              | Email address                                                                                                                                                                                                                                                                                                                    |
> | `minimumNumberOfNumbers`                                            | At least {num} number(s)                                                                                                                                                                                                                                                                                                         |
> | `minimumNumberOfLowercase`                                          | At least {num} lowercase letter(s)                                                                                                                                                                                                                                                                                               |
> | `minimumNumberOfUppercase`                                          | At least {num} uppercase letter(s)                                                                                                                                                                                                                                                                                               |
> | `minimumNumberOfSymbols`                                            | At least {num} symbol(s)                                                                                                                                                                                                                                                                                                         |
> | `nameCallback`                                                      | Username                                                                                                                                                                                                                                                                                                                         |
> | `nameYourDevice`                                                    | Name your device                                                                                                                                                                                                                                                                                                                 |
> | `next`                                                              | Next                                                                                                                                                                                                                                                                                                                             |
> | `nextButton`                                                        | Next                                                                                                                                                                                                                                                                                                                             |
> | `notToExceedMaximumCharacterLength`                                 | No more than {max} characters                                                                                                                                                                                                                                                                                                    |
> | `noLessThanMinimumCharacterLength`                                  | At least {min} character(s)                                                                                                                                                                                                                                                                                                      |
> | `onMobileOpenInAuthenticator`                                       | On mobile? Open link in Authenticator.                                                                                                                                                                                                                                                                                           |
> | `optionallyNameDevice`                                              | Optionally name your device                                                                                                                                                                                                                                                                                                      |
> | `passwordCallback`                                                  | Password                                                                                                                                                                                                                                                                                                                         |
> | `passwordCannotContainCommonPasswords`                              | Password cannot contain common passwords                                                                                                                                                                                                                                                                                         |
> | `passwordCannotContainCommonPasswordsOrBeReversible`                | Password cannot contain common passwords or reversible text                                                                                                                                                                                                                                                                      |
> | `passwordCannotContainCommonPasswordsOrBeReversibleStringsLessThan` | Password cannot contain common passwords or reversible text less than {min} characters                                                                                                                                                                                                                                           |
> | `passwordRequirements`                                              | Password requirements:                                                                                                                                                                                                                                                                                                           |
> | `pleaseCheckValue`                                                  | Please check this value                                                                                                                                                                                                                                                                                                          |
> | `pleaseConfirm`                                                     | Please confirm                                                                                                                                                                                                                                                                                                                   |
> | `preferencesMarketing`                                              | Send me special offers and services                                                                                                                                                                                                                                                                                              |
> | `preferencesUpdates`                                                | Send me news and updates                                                                                                                                                                                                                                                                                                         |
> | `provideCustomQuestion`                                             | Provide custom security question                                                                                                                                                                                                                                                                                                 |
> | `qrCodeNotWorking`                                                  | Not working or need an alternative method?                                                                                                                                                                                                                                                                                       |
> | `qrCodeFailedToRender`                                              | QR Code failed to render. Please notify your support administrator. You are welcome to use the alternative methods below.                                                                                                                                                                                                        |
> | `qrCodeImportFailure`                                               | We are unable to render your QR Code. Please use one of the alternative methods below.                                                                                                                                                                                                                                           |
> | `redirectingTo`                                                     | Redirecting you to                                                                                                                                                                                                                                                                                                               |
> | `registerButton`                                                    | Register                                                                                                                                                                                                                                                                                                                         |
> | `registerHeader`                                                    | Register                                                                                                                                                                                                                                                                                                                         |
> | `registerSuccess`                                                   | Registration successful!                                                                                                                                                                                                                                                                                                         |
> | `requiredField`                                                     | Value is required                                                                                                                                                                                                                                                                                                                |
> | `registerYourDevice`                                                | Register {name}                                                                                                                                                                                                                                                                                                                  |
> | `scanQrCodeWithAuthenticator`                                       | Scan the QR code image below with the ForgeRock Authenticator app to register your device with your login.                                                                                                                                                                                                                       |
> | `securityAnswer`                                                    | Security answer                                                                                                                                                                                                                                                                                                                  |
> | `securityQuestions`                                                 | Security question(s)                                                                                                                                                                                                                                                                                                             |
> | `securityQuestionsPrompt`                                           | Provide security question(s) and answer(s):                                                                                                                                                                                                                                                                                      |
> | `setupTwoStepVerification`                                          | Set up 2-step verification                                                                                                                                                                                                                                                                                                       |
> | `setupTwoStepVerificationButton`                                    | Set up                                                                                                                                                                                                                                                                                                                           |
> | `setupTwoStepVerificationDescription`                               | To protect your account, add a second authentication method.                                                                                                                                                                                                                                                                     |
> | `setupTwoStepVerificationWarning`                                   | Starting April 2, 2024, you must sign in using 2-step verification. \<a class='alert-link' href='https\://backstage.forgerock.com/docs/idcloud/latest/product-information/migration-dependent-features/tenant-administrator-mandatory-2-step-verification-faq.html' target='\_blank' rel='noopener noreferrer'>Learn more\</a>.  |
> | `shouldContainANumber`                                              | Should contain a number                                                                                                                                                                                                                                                                                                          |
> | `shouldContainAnUppercase`                                          | Should contain an uppercase letter                                                                                                                                                                                                                                                                                               |
> | `shouldContainALowercase`                                           | Should contain a lowercase letter                                                                                                                                                                                                                                                                                                |
> | `shouldContainASymbol`                                              | Should contain a symbol                                                                                                                                                                                                                                                                                                          |
> | `showPassword`                                                      | Show password                                                                                                                                                                                                                                                                                                                    |
> | `signalsEvaluation`                                                 | Evaluating device information.                                                                                                                                                                                                                                                                                                   |
> | `skipButton`                                                        | Skip                                                                                                                                                                                                                                                                                                                             |
> | `skipForNow`                                                        | Skip for now                                                                                                                                                                                                                                                                                                                     |
> | `sn`                                                                | Last name                                                                                                                                                                                                                                                                                                                        |
> | `submit`                                                            | Submit                                                                                                                                                                                                                                                                                                                           |
> | `submitButton`                                                      | Submit                                                                                                                                                                                                                                                                                                                           |
> | `successMessage`                                                    | Success!                                                                                                                                                                                                                                                                                                                         |
> | `termsAndConditions`                                                | Please accept our Terms & Conditions                                                                                                                                                                                                                                                                                             |
> | `termsAndConditionsLinkText`                                        | View full Terms & Conditions                                                                                                                                                                                                                                                                                                     |
> | `tryAgain`                                                          | Please try again                                                                                                                                                                                                                                                                                                                 |
> | `twoFactorAuthentication`                                           | Two factor authentication                                                                                                                                                                                                                                                                                                        |
> | `useThisNewMfaToHelpVerifyYourIdentity`                             | Use this new device or Multi-Factor Authentication method to help verify your identity.                                                                                                                                                                                                                                          |
> | `useValidEmail`                                                     | Please use a valid email address.                                                                                                                                                                                                                                                                                                |
> | `unrecoverableError`                                                | There was an error in the form submission.                                                                                                                                                                                                                                                                                       |
> | `unknownLoginError`                                                 | Unknown login failure has occurred.                                                                                                                                                                                                                                                                                              |
> | `unknownNetworkError`                                               | Unknown network request failure has occurred.                                                                                                                                                                                                                                                                                    |
> | `url`                                                               | URL:                                                                                                                                                                                                                                                                                                                             |
> | `useDeviceForIdentityVerification`                                  | Use your device for identity verification.                                                                                                                                                                                                                                                                                       |
> | `useOneOfTheseCodes`                                                | Use one of these codes to authenticate if you lose your device, which has been named: \<em>{name}\</em>                                                                                                                                                                                                                          |
> | `userName`                                                          | Username                                                                                                                                                                                                                                                                                                                         |
> | `usernameRequirements`                                              | Username requirements:                                                                                                                                                                                                                                                                                                           |
> | `useTheAuthenticatorAppOnYourPhone`                                 | Find the verification code using the authenticator app on your phone.                                                                                                                                                                                                                                                            |
> | `validatedCreatePasswordCallback`                                   | Password                                                                                                                                                                                                                                                                                                                         |
> | `validatedCreateUsernameCallback`                                   | Username                                                                                                                                                                                                                                                                                                                         |
> | `valueRequirements`                                                 | Value requirements:                                                                                                                                                                                                                                                                                                              |
> | `verifyYourIdentity`                                                | Verify your identity                                                                                                                                                                                                                                                                                                             |
> | `yourDevice`                                                        | Your device                                                                                                                                                                                                                                                                                                                      |
> | `yourMultiFactorAuthIsEnabled`                                      | Your new device or MFA is enabled                                                                                                                                                                                                                                                                                                |
> | `yourRecoveryCodesToAccessAccountForLostDevice`                     | If you lose your device, or don't have it with you, a recovery code is the only way to sign in to your account with 2-step verification enabled. It's strongly recommended that you print and store these codes in a safe place. \<b>Each code can only be used once\</b>."                                                      |

You can use the `content` configuration element to specify custom values for these variables, or to localize text content.

To localize the text the Advanced Identity Cloud/PingAM Login Widget displays, provide the localized strings in the `content` configuration element when you call `configure()`. If you don't override the content strings, the widget uses the default `en-us` strings.

The `content` object is passed once during `configure()`. To select strings based on the user's browser locale, build the content object first and then pass it to a single `await configure()` call:

Example `content` configuration

```javascript
import { configure } from '@forgerock/login-widget';

const userLang = navigator.language || navigator.userLanguage;

const localizedContent = userLang === 'fr-CA'
  ? {
      userName: 'Identifiant',
      passwordCallback: 'Phrase secrète',
      nextButton: 'Nous allez en route!',
    }
  : {
      userName: 'Identifier',
      passwordCallback: 'Passphrase',
      nextButton: "Let's go!",
    };

await configure({
  serverConfig: {
    wellknown: 'https://openam-forgerock-sdks.forgeblocks.com/am/oauth2/realms/root/realms/alpha/.well-known/openid-configuration',
  },
  content: localizedContent,
});
```

![Custom values displayed when locale is not \`fr-CA\`](../../_images/LAW/law-config-custom-content-en.png)Figure 1. Custom values displayed when locale is not `fr-CA`

---

---
title: Log in with social authentication
description: Social authentication provides your users with a choice of ways to sign in that suits them.
component: login-widget
page_id: login-widget:login-widget:use-cases/how-to-social-login
canonical_url: https://developer.pingidentity.com/login-widget/login-widget/use-cases/how-to-social-login.html
llms_txt: https://developer.pingidentity.com/login-widget/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: Tue, 28 Jul 2026 00:00:00 +0000
keywords: ["Integration", "Journeys", "Features", "Social Authentication", "Standards"]
---

# Log in with social authentication

Social authentication provides your users with a choice of ways to sign in that suits them.

The Advanced Identity Cloud/PingAM Login Widget supports social authentication with the following providers:

* Apple

* Facebook

* Google

* LinkedIn

* Microsoft Entra ID

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

// This snippet assumes the widget has already been configured elsewhere in your
// app via `await configure({...})`. Refer to the tutorial for the full setup.
const journeyEvents = journey();

const url = new URL(location.href);
const codeParam = url.searchParams.get('code');
const stateParam = url.searchParams.get('state');
const formPostEntryParam = url.searchParams.get('form_post_entry');

if (formPostEntryParam || (codeParam && stateParam)) {
    journeyEvents.start({ resumeUrl: location.href });
}
```

The `location.href` value includes any query parameters returned from the social provider. Without all the query parameters, the Advanced Identity Cloud/PingAM Login Widget might not be able to rehydrate the journey and continue as needed.

---

---
title: Multi-factor authentication with OATH and Push
description: The Advanced Identity Cloud/PingAM Login Widget provides UI elements for registering a new OATH or Push device by scanning a QR code with the ForgeRock Authenticator app, and for verifying a one-time password from an already-registered device.
component: login-widget
page_id: login-widget:login-widget:use-cases/how-to-oath-otp
canonical_url: https://developer.pingidentity.com/login-widget/login-widget/use-cases/how-to-oath-otp.html
llms_txt: https://developer.pingidentity.com/login-widget/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: Tue, 28 Jul 2026 00:00:00 +0000
keywords: ["Integration", "Journeys", "Features", "Multi-factor Authentication (MFA)", "Standards"]
section_ids:
  register-device: Registering a device with a QR code
  configure_your_authentication_journey: Configure your authentication journey
  test_the_registration_flow: Test the registration flow
  verify-otp: Verifying a one-time password
  recovery-codes: Displaying recovery codes
  configure_your_authentication_journey_2: Configure your authentication journey
  test_the_flow: Test the flow
  related_use_cases: Related use cases
---

# Multi-factor authentication with OATH and Push

The Advanced Identity Cloud/PingAM Login Widget provides UI elements for registering a new OATH or Push device by scanning a QR code with the ForgeRock Authenticator app, and for verifying a one-time password from an already-registered device.

This page covers:

* [Registering a device with a QR code](#register-device)

* [Verifying a one-time password](#verify-otp)

* [Displaying recovery codes](#recovery-codes)

## Registering a device with a QR code

Use the [Combined MFA Registration node](https://docs.pingidentity.com/auth-node-ref/latest/combined-mfa-registration.html) or [Push Registration node](https://docs.pingidentity.com/auth-node-ref/latest/push-registration.html) node to let a user register a new device by scanning a QR code with the ForgeRock Authenticator app, instead of typing in a shared secret manually.

When the Advanced Identity Cloud/PingAM Login Widget encounters a step containing QR code data, it automatically:

1. Renders a QR code image the user can scan with their authenticator app.

2. Provides a fallback link and copyable URL for users who cannot scan the code, for example if testing on the same device that renders the widget.

3. If the step also includes a polling callback, polls the server until the user completes registration on their device, then continues the journey automatically.

No additional widget configuration is required. This behavior is automatic whenever the journey step matches this shape.

### Configure your authentication journey

Add the [Combined MFA Registration node](https://docs.pingidentity.com/auth-node-ref/latest/combined-mfa-registration.html) or [Push Registration node](https://docs.pingidentity.com/auth-node-ref/latest/push-registration.html) node to a registration journey.

Connect the node's outcomes to handle both successful registration and any failure paths your journey requires.

|   |                                                                                                                                                                                                                                                                                                                                                                   |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The [Combined MFA Registration node](https://docs.pingidentity.com/auth-node-ref/latest/combined-mfa-registration.html) node lets users choose between Push and OATH registration in a single step. Use the [Push Registration node](https://docs.pingidentity.com/auth-node-ref/latest/push-registration.html) node if you only want to offer Push registration. |

### Test the registration flow

With your journey configured, start it in an app using the Advanced Identity Cloud/PingAM Login Widget. When you reach the registration step, the widget displays:

* A QR code image

* A collapsible section with a direct link to open the registration URL in the ForgeRock Authenticator app, and a copyable URL, useful when testing in a browser on the same device as the authenticator app

* A loading indicator while the widget polls the server for registration completion

Scan the QR code with the ForgeRock Authenticator app (or open the fallback link on a mobile device) to complete registration. The journey continues automatically once the server detects the new device.

## Verifying a one-time password

The Advanced Identity Cloud/PingAM Login Widget provides UI elements for the **OATH Token Verifier** node but not currently the standalone **OATH Registration** node. Use the QR code registration flow above instead.

Once a user has registered the ForgeRock Authenticator for one-time passwords, for example using the flow above, the Advanced Identity Cloud/PingAM Login Widget can accept a one-time password from the authenticator app.

The Advanced Identity Cloud/PingAM Login Widget requires that the **OATH Token Verifier** node is contained within a **Page node** configured with a specific Stage property.

In the containing **Page Node**, set the Stage property to `OneTimePassword`:

![law oath journey with stage en](../../_images/LAW/law-oath-journey-with-stage-en.png)Figure 1. OATH journey example

The Advanced Identity Cloud/PingAM Login Widget detects that stage value as a special case and renders the appropriate UI:

![law oath ui with stage en](../../_images/LAW/law-oath-ui-with-stage-en.png)Figure 2. Rendering with the `OneTimePassword` stage property

If you do not put the **OATH Token Verifier** node within a **Page node**, the Advanced Identity Cloud/PingAM Login Widget will not render the UI correctly:

![law oath ui en](../../_images/LAW/law-oath-ui-en.png)Figure 3. Rendering a lone **OATH Token Verifier** node

## Displaying recovery codes

Use the [Recovery Code Display node](https://docs.pingidentity.com/auth-node-ref/latest/recovery-code-display.html) node after a device registration step to give users backup codes they can use to authenticate if they lose access to their registered device.

When the Advanced Identity Cloud/PingAM Login Widget encounters this node's callback, it automatically renders the device name and a formatted grid of recovery codes for the user to save or print.

### Configure your authentication journey

Add the [Recovery Code Display node](https://docs.pingidentity.com/auth-node-ref/latest/recovery-code-display.html) node to your registration journey, after the node that registers the device.

To let users authenticate with a previously issued recovery code, add the [Recovery Code Collector Decision node](https://docs.pingidentity.com/auth-node-ref/latest/recovery-code-collector-decision.html) node to your login journey.

### Test the flow

Complete a device registration journey that includes the [Recovery Code Display node](https://docs.pingidentity.com/auth-node-ref/latest/recovery-code-display.html) node. After registration succeeds, the Advanced Identity Cloud/PingAM Login Widget displays:

* A header confirming that MFA is now enabled

* The name of the registered device

* A list of one-time-use recovery codes

|   |                                                                                                                                                                                                                                                         |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The server returns recovery codes only once, immediately after registration.Advise your users to save or print them before continuing, as the Advanced Identity Cloud/PingAM Login Widget does not provide a way to view previously issued codes again. |

## Related use cases

* [Passkeys](passkeys.html)

  Passwordless sign-in and registration with passkeys.

---

---
title: Passkeys
description: Passkeys let users sign in without a password, using a FIDO2 credential backed by their device, a browser-saved passkey, or a hardware security key.
component: login-widget
page_id: login-widget:login-widget:use-cases/passkeys
canonical_url: https://developer.pingidentity.com/login-widget/login-widget/use-cases/passkeys.html
llms_txt: https://developer.pingidentity.com/login-widget/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: Tue, 28 Jul 2026 00:00:00 +0000
keywords: ["WebAuthn", "Passkeys", "FIDO2", "Multi-factor Authentication (MFA)"]
---

# Passkeys

Passkeys let users sign in without a password, using a FIDO2 credential backed by their device, a browser-saved passkey, or a hardware security key.

The Advanced Identity Cloud/PingAM Login Widget supports both sides of the passkey lifecycle:

* [Registering a passkey](passkeys/register-a-passkey.html)

  Let a signed-in user register a new passkey for their account.

* [Implementing passkey autofill](passkeys/passkey-autofill.html)

  Let users sign in by selecting a registered passkey directly from the browser's native autofill picker on the username field.

---

---
title: Registering a passkey
description: The Advanced Identity Cloud/PingAM Login Widget provides UI elements for the WebAuthn Registration node node, letting a signed-in user register a new passkey backed by their device, browser, or a hardware security key.
component: login-widget
page_id: login-widget:login-widget:use-cases/passkeys/register-a-passkey
canonical_url: https://developer.pingidentity.com/login-widget/login-widget/use-cases/passkeys/register-a-passkey.html
llms_txt: https://developer.pingidentity.com/login-widget/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: Tue, 28 Jul 2026 00:00:00 +0000
keywords: ["WebAuthn", "Passkeys", "FIDO2", "Multi-factor Authentication (MFA)"]
section_ids:
  how_it_works: How it works
  configure_your_authentication_journey: Configure your authentication journey
  test_the_registration_flow: Test the registration flow
  recovery-codes: Displaying recovery codes
  configure_your_authentication_journey_2: Configure your authentication journey
  test_the_flow: Test the flow
  related_use_cases: Related use cases
---

# Registering a passkey

The Advanced Identity Cloud/PingAM Login Widget provides UI elements for the [WebAuthn Registration node](https://docs.pingidentity.com/auth-node-ref/latest/webauthn-registration.html) node, letting a signed-in user register a new passkey backed by their device, browser, or a hardware security key.

No additional widget configuration is required. The Advanced Identity Cloud/PingAM Login Widget detects a registration step from its callback shape and renders the appropriate UI automatically.

## How it works

When the Advanced Identity Cloud/PingAM Login Widget encounters a WebAuthn registration step, it takes the following actions:

1. Prompts the user to optionally name the new device, for example **My Work Laptop**.

2. Calls the browser's `navigator.credentials.create()` API to create a new passkey, using the challenge and relying party details from the server.

3. Submits the resulting credential to the server to complete registration.

![Browser prompt to create a new passkey](../../../_images/chrome/chrome-create-passkey-en.png)Figure 1. Creating a passkey

The exact prompt the user sees depends on their browser, operating system, and available authenticators. For example, the browser might show a platform biometric prompt, such as Touch ID or Windows Hello, for a device-bound passkey, or a picker for a hardware security key.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | If the user cancels the browser prompt, or the browser reports another WebAuthn error, the Advanced Identity Cloud/PingAM Login Widget does not display its own error message.It still submits the step to the server with the error recorded, so the [WebAuthn Registration node](https://docs.pingidentity.com/auth-node-ref/latest/webauthn-registration.html) node's Client Error outcome fires as expected. Route that outcome to a message or fallback in your journey. |

## Configure your authentication journey

Because registering a passkey requires an authenticated session, add the [WebAuthn Registration node](https://docs.pingidentity.com/auth-node-ref/latest/webauthn-registration.html) node **after** a successful sign-in step in your journey, rather than as part of the sign-in journey itself.

|   |                                                                                                                                                                                                                                                                                                                                                                                                       |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Use the same configuration values in the [WebAuthn Registration node](https://docs.pingidentity.com/auth-node-ref/latest/webauthn-registration.html) node as you use in any [WebAuthn Authentication node](https://docs.pingidentity.com/auth-node-ref/latest/webauthn-authentication.html) nodes in your sign-in journeys.Configuration mismatches between these nodes cause authentication to fail. |

In the [WebAuthn Registration node](https://docs.pingidentity.com/auth-node-ref/latest/webauthn-registration.html) node:

1. In Origin domains, enter the URL where you host your app, for example `https://app.example.com`.

   |   |                                                                                                           |
   | - | --------------------------------------------------------------------------------------------------------- |
   |   | If you leave Origin domains empty, the server uses the origin of incoming requests as an accepted origin. |

2. In Accepted signing algorithms, include one or more of `ES256` and `RS256`.

3. Ensure Limit registrations is **not enabled**, so returning users can register more than one passkey.

4. Optionally, use Authentication attachment to control which type of authenticator the browser offers:

   | Value            | Description                                                                                          |
   | ---------------- | ---------------------------------------------------------------------------------------------------- |
   | `PLATFORM`       | Only allow authenticators built into the user's device, such as Face ID, Touch ID, or Windows Hello. |
   | `CROSS_PLATFORM` | Only allow external authenticators, such as hardware security keys.                                  |
   | `UNSPECIFIED`    | Allow either type. This is the default.                                                              |

5. Optionally, to support usernameless sign-in later, enable Username to device.

## Test the registration flow

Sign in to your app, then start a journey that includes the [WebAuthn Registration node](https://docs.pingidentity.com/auth-node-ref/latest/webauthn-registration.html) node.

The Advanced Identity Cloud/PingAM Login Widget prompts for an optional device name, then invokes the browser's passkey creation flow. Complete the browser's prompt to finish registration.

After a device is registered, [configure passkey autofill](passkey-autofill.html) to let the user sign in with it, or add a [WebAuthn Authentication node](https://docs.pingidentity.com/auth-node-ref/latest/webauthn-authentication.html) node without conditional mediation to require an explicit passkey sign-in step.

## Displaying recovery codes

Use the [Recovery Code Display node](https://docs.pingidentity.com/auth-node-ref/latest/recovery-code-display.html) node after a device registration step to give users backup codes they can use to authenticate if they lose access to their registered device.

When the Advanced Identity Cloud/PingAM Login Widget encounters this node's callback, it automatically renders the device name and a formatted grid of recovery codes for the user to save or print.

### Configure your authentication journey

Add the [Recovery Code Display node](https://docs.pingidentity.com/auth-node-ref/latest/recovery-code-display.html) node to your registration journey, after the node that registers the device.

To let users authenticate with a previously issued recovery code, add the [Recovery Code Collector Decision node](https://docs.pingidentity.com/auth-node-ref/latest/recovery-code-collector-decision.html) node to your login journey.

### Test the flow

Complete a device registration journey that includes the [Recovery Code Display node](https://docs.pingidentity.com/auth-node-ref/latest/recovery-code-display.html) node. After registration succeeds, the Advanced Identity Cloud/PingAM Login Widget displays:

* A header confirming that MFA is now enabled

* The name of the registered device

* A list of one-time-use recovery codes

|   |                                                                                                                                                                                                                                                         |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The server returns recovery codes only once, immediately after registration.Advise your users to save or print them before continuing, as the Advanced Identity Cloud/PingAM Login Widget does not provide a way to view previously issued codes again. |

## Related use cases

* [Implementing passkey autofill](passkey-autofill.html)

  Let users sign in with a registered passkey from the browser's autofill picker.

---

---
title: Step 1. Download the samples
description: Provides instructions on how to download the sample app repository for the JavaScript OIDC sign-on module tutorial with Advanced Identity Cloud.
component: login-widget
page_id: login-widget:login-widget:try-it-out/reactjs-todo-login-widget/01_download_samples
canonical_url: https://developer.pingidentity.com/login-widget/login-widget/try-it-out/reactjs-todo-login-widget/01_download_samples.html
llms_txt: https://developer.pingidentity.com/login-widget/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: Thu, 2 Apr 2026 11:33:37 +0100
keywords: ["OAuth 2.0", "OpenID Connect", "Tutorial", "Source Code", "Integration", "SDK", "JavaScript", "Advanced Identity Cloud", "sample app"]
---

# Step 1. Download the samples

[icon: circle-check, set=far]PingOne Advanced Identity Cloud [icon: circle-check, set=far]PingAM [icon: js, set=fab]Login Widget

* [Prepare](00_before-you-begin.html)

* **Download**

* [Configure](02_configure_sample.html)

* [Run](03_run_the_sample.html)

The quickest and easiest way to get started with the Advanced Identity Cloud/PingAM Login Widget is to download and run one of our sample apps from the **SDK Sample Apps** repository.

This repo contains example apps that demonstrate Advanced Identity Cloud/PingAM Login Widget functionality.

To download or clone a copy of the SDK Sample Apps repo, complete these steps:

1. In a web browser, navigate to <https://github.com/ForgeRock/sdk-sample-apps>.

2. Download the source code using one of the following methods:

   * Download a ZIP file

     1. Click Code, and then click Download ZIP.

        ![download samples zip](../../../_images/download-samples-zip.png)Figure 1. Downloading a zip file of the sample apps repo.

     2. Extract the contents of the downloaded ZIP file to a suitable location.

   * Use a Git-compatible tool to clone the repo locally

     1. Click Code, and then copy the HTTPS URL.

        ![download samples git clone](../../../_images/download-samples-git-clone.png)Figure 2. Downloading the sample apps repo using Git clone.

     2. Use the URL to clone the repository to a suitable location.

        For example, from the command-line you could run:

        ```shell
        git clone https://github.com/ForgeRock/sdk-sample-apps.git
        ```

After completing these steps, you will have a local folder named `sdk-sample-apps`. Inside, you'll find separate folders for the Android, iOS, JavaScript, and React Native sample app projects.

You can find the Advanced Identity Cloud/PingAM Login Widget sample apps in the `/javascript` folder.

---

---
title: Step 1. Install the widget
description: You can add the Advanced Identity Cloud/PingAM Login Widget to your app by using npm, or you can download it from GitHub and build it yourself, adding results to your project directly.
component: login-widget
page_id: login-widget:login-widget:tutorial/01-install
canonical_url: https://developer.pingidentity.com/login-widget/login-widget/tutorial/01-install.html
llms_txt: https://developer.pingidentity.com/login-widget/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: Wed, 17 May 2023 14:10:20 +0100
keywords: ["Integration", "Getting Started"]
section_ids:
  npm: Install the Advanced Identity Cloud/PingAM Login Widget with npm
  build: Build a customized Advanced Identity Cloud/PingAM Login Widget
  next: Next
---

# Step 1. Install the widget

You can add the Advanced Identity Cloud/PingAM Login Widget to your app by using npm, or you can download it from GitHub and build it yourself, adding results to your project directly.

* [Install the Advanced Identity Cloud/PingAM Login Widget with npm](#npm)

  The easiest way to add the Advanced Identity Cloud/PingAM Login Widget to your project.

* [Build a customized Advanced Identity Cloud/PingAM Login Widget](#build)

  If you want to [customize the styles](../customize/styles/build-time.html) included in the Advanced Identity Cloud/PingAM Login Widget, you need to download the Advanced Identity Cloud/PingAM Web Login Framework source, make your modifications, and build a customized package.

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

3. Run `pnpm` to download and install the required packages and modules:

   `pnpm install`

4. Build the Advanced Identity Cloud/PingAM Login Widget with `pnpm`:

   `pnpm run build:widget`

5. Copy the built `dist/` directory into your app project

6. Import the `Widget` component into your app:

   `import Widget from '../path/to/dist/index.js';`

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
llms_txt: https://developer.pingidentity.com/login-widget/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
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
title: Step 2. Configure connection properties
description: Explains how to configure the connection properties in the ReactJS Todo Login Widget sample for PingOne Advanced Identity Cloud or PingAM
component: login-widget
page_id: login-widget:login-widget:try-it-out/reactjs-todo-login-widget/02_configure_sample
canonical_url: https://developer.pingidentity.com/login-widget/login-widget/try-it-out/reactjs-todo-login-widget/02_configure_sample.html
llms_txt: https://developer.pingidentity.com/login-widget/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: Thu, 20 Aug 2026 00:00:00 +0000
keywords: ["PingOne Advanced Identity Cloud", "PingAM", "Login Widget", "ReactJS", "OAuth 2.0", "Setup &amp; Configuration", "Source Code", "Tutorial"]
section_ids:
  react-api-server-env: Configure the API server app
  react-env: Configure the ReactJS client app
---

# Step 2. Configure connection properties

[icon: circle-check, set=far]PingOne Advanced Identity Cloud [icon: circle-check, set=far]PingAM [icon: js, set=fab]Login Widget

* [Prepare](00_before-you-begin.html)

* [Download](01_download_samples.html)

* **Configure**

* [Run](03_run_the_sample.html)

There are two projects in this tutorial that require configuration:

* [Backend API server](#react-api-server-env)

  A backend REST API server that uses a confidential OAuth 2.0 client to validate access tokens. The API server handles storage and retrieval of your personal Todo items.

* [Client ReactJS app](#react-env)

  The front-end client app, written in ReactJS, that handles the Login Widget UI and authentication journeys or trees.

## Configure the API server app

1. In the IDE of your choice, open the `sdk-sample-apps` folder you cloned previously.

2. Copy the `.env.example` file in the `sdk-sample-apps/javascript/todo-api` folder and save it with the name `.env` within this same directory.

   Example API server `sdk-sample-apps/javascript/todo-api/.env` file

   ```properties
   # 'AIC' or 'PINGONE'
   SERVER_TYPE=
   # AM URL for AIC or PingAM, or PingOne base URL with environment ID
   SERVER_URL=
   # 'alpha' or 'bravo' for AIC, 'root' for PingAM. Not used for PingOne.
   REALM_PATH=
   # Confidential client ID for AIC and PingAM or WebApp public client ID for PingOne
   REST_OAUTH_CLIENT=
   # Confidential client secret for AIC or PingAM. Not used for PingOne.
   REST_OAUTH_SECRET=
   PORT=9443
   ```

3. Update the configuration block with the details of your server environment.

   * *SERVER\_TYPE*

     Set to `AIC` for PingOne Advanced Identity Cloud or PingAM.

   * *SERVER\_URL*

     The URL of the server to connect to, including the deployment path of the Access Management component.

     * PingOne Advanced Identity Cloud example

       `https://openam-forgerock-sdks.forgeblocks.com/am`

     * PingAM example

       `https://openam.example.com:8443/openam`

   * *PORT*

     The port number on which to run the TODO API server.

     You'll need this port number when configuring the client app to connect to the TODO API server.

     If not specified, the TODO API server defaults to running on port `9443`

   * *REALM\_PATH*

     The realm in which the confidential OAuth 2.0 client profile is configured.

     * PingOne Advanced Identity Cloud example

       `alpha` or `bravo`

     * PingAM example

       `root`

   * *REST\_OAUTH\_CLIENT*

     The client ID of the confidential OAuth 2.0 application you created earlier.

     For example, sdkConfidentialClient

   * *REST\_OAUTH\_SECRET*

     The secret of the confidential OAuth 2.0 application you created earlier.

     For example, `5tr0ngP@S5w0rd!`

   The result will resemble the following:

   Example completed API server `sdk-sample-apps/javascript/todo-api/.env` file

   ```properties
   # 'AIC' or 'PINGONE'
   SERVER_TYPE=AIC
   # AM URL for AIC or PingOne base URL with env ID for PingOne
   SERVER_URL=https://openam-forgerock-sdks.forgeblocks.com/am
   PORT=9443
   # 'alpha' or 'bravo' for AIC server type. Not used for PingOne.
   REALM_PATH=alpha
   # Confidential client ID for AIC or WebApp public client ID for PingOne
   REST_OAUTH_CLIENT=sdkConfidentialClient
   # Confidential client secret for AIC. Not used for PingOne.
   REST_OAUTH_SECRET=5tr0ngP@S5w0rd!
   ```

4. Save your changes.

## Configure the ReactJS client app

1. In the IDE of your choice, open the `sdk-sample-apps` folder you cloned previously.

2. Copy the `.env.example` file in the `sdk-sample-apps/javascript/reactjs-todo-login-widget` folder and save it with the name `.env` within this same directory.

   Example client `sdk-sample-apps/javascript/reactjs-todo-login-widget/.env` file

   ```properties
   WELLKNOWN_URL=
   WEB_OAUTH_CLIENT=
   SCOPE=openid profile email
   PORT=8443
   API_URL=http://localhost:9443
   DEBUGGER_OFF=true
   DEVELOPMENT=true
   JOURNEY_LOGIN=Login
   JOURNEY_REGISTER=Registration

   # required when PingOne Protect callbacks are present
   PINGONE_ENV_ID=
   ```

3. Update the configuration block with the details of your server environment.

   * *WELLKNOWN\_URL*

     The `.well-known` endpoint from your server.

     * PingOne Advanced Identity Cloud

       Copy the discovery URI from the public OAuth 2.0 client in the admin console. For example:

       `https://openam-forgerock-sdks.forgeblocks.com/am/oauth2/alpha/.well-known/openid-configuration`

     * PingAM

       Form the URL from the AM base URL, `/oauth2`, the complete realm hierarchy, and `/.well-known/openid-configuration`. For example:

       `https://openam.example.com:8443/openam/oauth2/realms/root/.well-known/openid-configuration`

   * *WEB\_OAUTH\_CLIENT*

     The client ID of your *public* OAuth 2.0 application for the ReactJS web application.

     For example, `sdkPublicClient`.

   * *SCOPE*

     The scopes you added to your public OAuth 2.0 application.

     Scopes should be space-separated, and the entire value should be enclosed in single quotes.

     For example, `'openid profile email'`.

   * *PORT*

     The port on which to serve the ReactJS client.

     Defaults to `8443`.

   * *API\_URL*

     The URL and port number on which you are running the TODO API backend server.

     For example, `http://localhost:9443`.

   * *DEBUGGER\_OFF*

     Set to `true` to disable `debugger` statements in the app.

     These statements are for learning the Login Widget integration points at runtime in your browser. When you open the browser's developer tools, the app pauses at each integration point.

   * *DEVELOPMENT*

     When `true`, this provides better debugging during development.

   * *JOURNEY\_LOGIN*

     The name of the login journey in PingOne Advanced Identity Cloud, or login tree in PingAM.

     Defaults to `Login`.

   * *JOURNEY\_REGISTER*

     The name of the registration journey or tree.

     Defaults to `Registration`.

   * *PINGONE\_ENV\_ID*

     The PingOne environment identifier.

     Set this value when your configured journey or tree uses PingOne Protect callbacks. Otherwise, leave it empty.

   The result will resemble the following:

   Example client `sdk-sample-apps/javascript/reactjs-todo-login-widget/.env` file

   ```properties
   WELLKNOWN_URL=https://example.forgeblocks.com/am/oauth2/alpha/.well-known/openid-configuration
   WEB_OAUTH_CLIENT=sdkPublicClient
   SCOPE='openid profile email'
   PORT=8443
   API_URL=http://localhost:9443
   DEBUGGER_OFF=true
   DEVELOPMENT=true
   JOURNEY_LOGIN=Login
   JOURNEY_REGISTER=Registration
   PINGONE_ENV_ID=
   ```

4. Save your changes.