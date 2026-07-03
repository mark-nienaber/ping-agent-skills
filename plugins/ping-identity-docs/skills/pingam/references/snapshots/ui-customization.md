---
title: About the UI
description: Customize the PingAM Admin and User UIs by downloading source code, modifying styling, localization, and layout, then deploying modified WAR files to your instances
component: pingam
version: 8.1
page_id: pingam:ui-customization:ui-customization-intro
canonical_url: https://docs.pingidentity.com/pingam/8.1/ui-customization/ui-customization-intro.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["User Interface", "Customization", "Source Code"]
page_aliases: ["ui-customization-guide:ui-customization-intro.adoc"]
---

# About the UI

AM includes the following browser-based UIs:

* Admin UI

  Pages related to the administration of an AM server. Administrative login is delegated to the user UI.

* User UI

  End user pages and login pages.

When you deploy AM to protect applications, you can redirect users to AM pages for login and logout. The end user pages have default styling and branding but are fully customizable. You can theme them, localize them, and change their layout.

To customize the UI, download the source code and change it to suit your environment. Deploy the modified UI in your AM instances as part of your environment pipelines or package it in your custom AM `.war` files, then deploy them.

Customizing the page layout or the JavaScript resources requires a complete rebuild of the UI. You can make other customizations, such as localizing or theming the UI, by modifying the `.war` file.

The UI contains the following types of resources:

**UI resources**

| Resources                                     | Location (Admin UI)                       | Location (User UI)                                      |
| --------------------------------------------- | ----------------------------------------- | ------------------------------------------------------- |
| **JavaScript source and configuration files** | `openam-ui-admin/src/js`                  | `openam-ui-user/src/js`                                 |
| **CSS collections**                           | `openam-ui-admin/src/resources/css`       | `openam-ui-user/src/resources/css`                      |
| **Fonts**                                     | `openam-ui-admin/src/resources/fonts`     | `openam-ui-user/src/resources/fonts`                    |
| **Images**                                    | `openam-ui-admin/src/resources/images`    | `openam-ui-user/src/resources/images`                   |
| **Localization files**                        | `openam-ui-admin/src/resources/locales`   | `openam-ui-user/src/resources/locales`                  |
| **Themes**                                    | N/A                                       | `openam-ui-user/src/resources/themes`                   |
| **Partials**                                  | `openam-ui-admin/src/resources/partials`  | `openam-ui-user/src/resources/themes/default/partials`  |
| **HTML pages**                                | `openam-ui-admin/src/resources/templates` | `openam-ui-user/src/resources/themes/default/templates` |
