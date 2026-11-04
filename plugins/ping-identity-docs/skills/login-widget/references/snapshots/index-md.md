---
title: Advanced Identity Cloud/PingAM Login Widget
description: PingOne Advanced Identity Cloud PingAM Login Widget
component: login-widget
page_id: login-widget::index
canonical_url: https://developer.pingidentity.com/login-widget/index.html
llms_txt: https://developer.pingidentity.com/login-widget/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: Tue, 28 Jul 2026 00:00:00 +0000
keywords: ["Integration", "Features", "Source Code"]
page_aliases: ["ROOT:javascript/webloginframework.adoc"]
section_ids:
  topics: Topics
  functionality: Functionality
  requirements: Requirements
---

# Advanced Identity Cloud/PingAM Login Widget

[icon: circle-check, set=far]PingOne Advanced Identity Cloud [icon: circle-check, set=far]PingAM [icon: js, set=fab]Login Widget

The Advanced Identity Cloud/PingAM Login Widget is an all-inclusive UI component to help you add authentication, user registration, and other self-service journeys into your web applications.

You can use the Advanced Identity Cloud/PingAM Login Widget within React, Vue, Angular and a number of other modern JavaScript frameworks, as well as vanilla JavaScript.

It does not currently support server-side rendering (SSR), including Node.js.

The Advanced Identity Cloud/PingAM Login Widget uses `@forgerock/journey-client` for journey execution, and `@forgerock/oidc-client` for OAuth/OIDC tokens, user info, and logout. It adds a user interface and state management on top, eliminating the need to develop and maintain UI components for complex authentication experiences.

This rendering layer uses [Svelte](https://svelte.dev/) and [Tailwind](https://tailwindcss.com/), but these are "compiled away" resulting in no runtime dependencies.

The resulting Advanced Identity Cloud/PingAM Login Widget is both library- and framework-agnostic.

## Topics

Get started with the Advanced Identity Cloud/PingAM Login Widget in the following sections:

[icon: graduation-cap, set=fad, size=3x]

#### [Tutorial](login-widget/tutorial.html)

Learn how to install the Advanced Identity Cloud/PingAM Login Widget, add it to your applications and manage user authentication and self-service journeys.

[icon: paint-brush, set=fad, size=3x]

#### [Themes](login-widget/customize/styles/build-time.html)

Discover how to reconfigure the Advanced Identity Cloud/PingAM Login Widget to use different colors, fonts, or sizing, or select between the light and dark modes.

[icon: route, set=fad, size=3x]

#### [Use cases](login-widget/use-cases.html)

Find out how to achieve some common use case scenarios using the Advanced Identity Cloud/PingAM Login Widget.

[icon: thumbs-up, set=fad, size=3x]

#### [Integrations](login-widget/integrations.html)

Integrate the Advanced Identity Cloud/PingAM Login Widget into various different frameworks.

[icon: code, set=fad, size=3x]

#### [API](login-widget/widget-api-reference.html)

Access a list of the modules included in the Advanced Identity Cloud/PingAM Login Widget and the API they offer.

## Functionality

The Advanced Identity Cloud/PingAM Login Widget supports the following PingOne Advanced Identity Cloud and PingAM features:

| [icon: check, set=fa]Supported                                                                                                                                                                                                                                                                                                                                                             | [icon: times, set=fa]Unsupported                                                            |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------- |
| * Page node

* Username

* Password

* QR code scan-to-register

* Push authentication and registration

* One-time passwords and registration

* Recovery codes

* WebAuthn

* Device profiles

* Social login providers:

  * Apple

  * Facebook

  * Google

* Email suspend, or "magic links"

* CAPTCHA display

  * hCaptcha

  * reCAPTCHA v2

  * reCAPTCHA v3

* PingOne Protect | - Centralized login

- `TextOutputCallback` callbacks containing scripts

- SAML federation |

## Requirements

The Advanced Identity Cloud/PingAM Login Widget is designed to work with the following:

* An ECMAScript module or CommonJS enabled client-side JavaScript app

* A "modern", fully-featured browser such as Chrome, Firefox, Safari, or Chromium Edge

The Advanced Identity Cloud/PingAM Login Widget supports vanilla JavaScript and many frameworks. It is tested against the following:

| [icon: check, set=fa]Tested | [icon: times, set=fa]Unsupported                 |
| --------------------------- | ------------------------------------------------ |
| * React

* Svelte

* Vue    | - Server-side rendering (SSR), including Node.js |

The Advanced Identity Cloud/PingAM Login Widget is ***not designed or tested*** for use with the following:

* Internet Explorer

* Legacy Edge

* WebView

* Electron

* Modified, browser-like environments