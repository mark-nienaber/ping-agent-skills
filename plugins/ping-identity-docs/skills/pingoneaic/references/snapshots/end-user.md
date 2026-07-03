---
title: Compare end-user UX options
description: Compare Advanced Identity Cloud end-user UX options — hosted pages, Login Widget, SDKs, and REST API — by features, flexibility, and effort
component: pingoneaic
page_id: pingoneaic:end-user:end-user-ux-options-compare
canonical_url: https://docs.pingidentity.com/pingoneaic/end-user/end-user-ux-options-compare.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["User Interface", "Journeys", "Integration", "Authentication"]
section_ids:
  compare-development-effort-against-flexibility: Compare development effort against flexibility
  compare-specific-features: Compare specific features
---

# Compare end-user UX options

You can find background information on UX options in PingOne Advanced Identity Cloud in [End-user UX options for authentication journeys and account management](end-user-ux-options.html).

## Compare development effort against flexibility

The choice of end-user UX option is a balance between development effort and flexibility; the more flexible the option, the more complex and time-consuming it is to develop and implement:

![ux options development effort against flexibility](_images/ux-options-development-effort-against-flexibility.png)

## Compare specific features

More specifically, the end-user UX option you choose will be based on a combination of these features:

| Feature                                                                              | Hosted pages             | Login Widget                 | SDKs                         | APIs                    |
| ------------------------------------------------------------------------------------ | ------------------------ | ---------------------------- | ---------------------------- | ----------------------- |
| OOTB *(tooltip: Out of the box)* end-user authentication journey UI                  | [icon: check, set=fa]Yes | [icon: check, set=fa]Yes     | [icon: times, set=fa]No      | [icon: times, set=fa]No |
| OOTB *(tooltip: Out of the box)* end-user authentication journey support             | [icon: check, set=fa]Yes | [icon: check, set=fa]Yes     | [icon: check, set=fa]Yes     | [icon: times, set=fa]No |
| OOTB *(tooltip: Out of the box)* end-user account management UI                      | [icon: check, set=fa]Yes | [icon: times, set=fa]No      | [icon: times, set=fa]No      | [icon: times, set=fa]No |
| Hosted by                                                                            | Ping Identity            | You                          | You                          | You                     |
| Theming                                                                              | Limited                  | Some limitations             | No limitation                | No limitation           |
| Pixel-perfect implementation of design mockups                                       | [icon: times, set=fa]No  | [icon: times, set=fa]No      | [icon: check, set=fa]Yes     | Can be developed        |
| Web application (browser)                                                            | [icon: check, set=fa]Yes | [icon: check, set=fa]Yes     | Prototype UI only            | Can be developed        |
| Native applications (Android, iOS)                                                   | [icon: times, set=fa]No  | [icon: times, set=fa]No      | Prototype UI only            | Can be developed        |
| Localization                                                                         | [icon: check, set=fa]Yes | [icon: check, set=fa]Yes     | N/A                          | Can be developed        |
| [Centralized journey flow](end-user-ux-journey-flows.html#centralized-journey-flows) | [icon: check, set=fa]Yes | [icon: times, set=fa]No      | [icon: check, set=fa]Yes     | Can be developed        |
| [Embedded journey flow](end-user-ux-journey-flows.html#embedded-journey-flows)       | [icon: times, set=fa]No  | [icon: check, set=fa]Yes     | [icon: check, set=fa]Yes     | Can be developed        |
| SAML supported                                                                       | [icon: check, set=fa]Yes | [icon: times, set=fa]No      | [icon: times, set=fa]No      | Can be developed        |
| CAPTCHA supported                                                                    | [icon: check, set=fa]Yes | [icon: check, set=fa]Yes     | [icon: check, set=fa]Yes     | Can be developed        |
| QR codes supported                                                                   | [icon: check, set=fa]Yes | [icon: check, set=fa]Yes     | [icon: check, set=fa]Yes     | Can be developed        |
| WebAuthn supported                                                                   | [icon: check, set=fa]Yes | [icon: check, set=fa]Yes     | [icon: check, set=fa]Yes     | Can be developed        |
| Passkey supported                                                                    | [icon: check, set=fa]Yes | [icon: check, set=fa]Yes     | [icon: check, set=fa]Yes     | Can be developed        |
| Device profile supported                                                             | N/A                      | [icon: check, set=fa]Yes     | [icon: check, set=fa]Yes     | Can be developed        |
| Token management supported                                                           | [icon: times, set=fa]No  | [icon: check, set=fa]Yes     | [icon: check, set=fa]Yes     | Can be developed        |
| WCAG *(tooltip: Web Content Accessibility Guidelines)* compliance                    | Not always 100%          | [icon: check, set=fa]Yes     | N/A                          | Can be developed        |
| Social login                                                                         | [icon: check, set=fa]Yes | Apple, Facebook, Google only | Apple, Facebook, Google only | Can be developed        |
| Include third-party CSS and JS                                                       | [icon: times, set=fa]No  | [icon: check, set=fa]Yes     | [icon: check, set=fa]Yes     | Can be developed        |
