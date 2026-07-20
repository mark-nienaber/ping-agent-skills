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

---

---
title: Customize hosted pages
description: "Customize Advanced Identity Cloud hosted pages using themes: configure branding, logos, headers, footers, and end-user profile actions"
component: pingoneaic
page_id: pingoneaic:end-user:hosted-pages-customize
canonical_url: https://docs.pingidentity.com/pingoneaic/end-user/hosted-pages-customize.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["User Interface", "Theme", "Localization", "Authentication"]
page_aliases: ["realms:customize-enduser-uis.adoc", "uis:customize-enduser-login-uis.adoc", "uis:customize-themes-enduser-login-uis.adoc", "end-user:customize-themes-enduser-login-uis.adoc", "end-user:customize-login-enduser-pages.adoc"]
section_ids:
  add-a-custom-theme: Add a custom theme
  localize-the-favicon-and-theme-logo: Localize the favicon and theme logo
  apply-a-custom-theme-to-a-journey: Apply a custom theme to a journey
  custom-headers-and-footers: Custom headers and footers
  enable-headers-and-footers-for-a-theme: Enable headers and footers for a theme
  edit-headers-and-footers: Edit headers and footers
  localize-headers-and-footers: Localize headers and footers
  configure-actions-and-information-for-end-users: Configure actions and information for end users
  sign-on-ui: Hosted journey pages
  configure-terms-and-conditions: Configure terms and conditions
  configure-privacy-and-consent: Configure privacy and consent
  configure-security-questions: Configure security questions
  end-user-ui: Hosted account pages
  configure-visible-information-and-end-user-actions: Configure visible information and end-user actions
  prevent-end-users-from-editing-properties: Prevent end users from editing specific personal data
  use-script-tags-in-identity-cloud-end-user-and-login-uis: Use script tags in hosted pages
---

# Customize hosted pages

Themes let you customize the look and feel of Advanced Identity Cloud hosted journey and account pages, including the information presented to end users and the actions they can take.

Notes on themes:

* Advanced Identity Cloud realms have a *default* theme that includes the colors of buttons and links, typefaces, and so on. This default theme applies to the hosted journey and account pages. You can add custom themes so that your end users are presented with screens *specific to their authentication journey*.

* Custom themes let you create a different look and feel for each brand that you support, including logos, favicon, headers, footers, scripted tags, and the actions and information end users can see.

* A theme is *followed* throughout an authentication journey. This means that if an end user signs on through the hosted journey pages with a specific theme, the remaining pages in the journey will have that same theme.

## Add a custom theme

In the Advanced Identity Cloud admin console:

1. Select Hosted Pages > + New Theme.

   |   |                                                                                                                                   |
   | - | --------------------------------------------------------------------------------------------------------------------------------- |
   |   | To duplicate an existing theme, click its ellipsis icon ([icon: more_horiz, set=material, size=inline]) and then click Duplicate. |

2. Enter a theme name that describes the theme's purpose; for example, the brand associated with an authentication journey.

3. Click Save.

4. Use the tabs and options to customize various aspects of the theme:

   | Tab           | Option   | What you can customize                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
   | ------------- | -------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | Global        | Styles   | You can customize:- Brand Colors: This includes colors for buttons, checkboxes, switches, high-level alert actions, and success actions.

   - Typography: The font applied to all journeys and customer-facing pages.

   - Buttons: The colors of buttons and their radius.

   - Links: The color of links, including when you hover over them and the option to bold all links.

   - Switches: The background color.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
   |               | Favicon  | Favicon logo displayed for all journey and account pages. You can localize the favicon. Learn more in [Localize the favicon and theme logo](#localize-the-favicon-and-theme-logo).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
   |               | Settings | The theme name and any journey(s) using this theme.	From this screen, you can select journeys to apply to your theme.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
   | Journey Pages | Styles   | You can customize:- Page Background: This includes the color of the journey background as well as a background image (optional).

   - Sign-in Card: Customize the styles of the card in the center of the journey page where end users enter their credentials. This includes the card colors, field colors, card shadow, border radius, and if the input text labels should be placed above or inside the input field.

   - Global Styles: These are the styles you set in the Global tab. Modifying this section from the Journey Pages updates the Global tab styles.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
   |               | Logo     | Logo to display for sign-on and registration pages. The displaying of the logo is optional. You can localize the logo. Learn more in [Localize the favicon and theme logo](#localize-the-favicon-and-theme-logo).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
   |               | Layout   | This includes:- Layout: The position of the sign-on card on the page.

   - Button Position: The position of the button inside the sign-on card.

   - Header: Place a header above the sign-on card. Learn more in [Custom headers and footers](#custom-headers-and-footers).

     * Add a skip to main content link in the header for accessibility: Add a button that lets screen readers skip header content.

     * Focus Options: Choose how the tab key behaves in relation to the header:

       * Always focus on header: The tab index is set to the beginning of the header and the first tab key press by an end user focuses on the first link in the header.

       * Always focus on card: The tab index is advanced to the sign-on card and the first tab key press by an end user focuses on the first link or field in the sign-on card.

       * Focus on header for initial step - focus on card for subsequent steps: On the initial browser page load of a journey, the first tab key press by an end user focuses on the first link in the header. On each subsequent browser page load as the journey progresses, the first tab key press by an end user focuses on the first link or field in the sign-on card.

   - Footer: Place a footer below the sign-on card. Learn more in [Custom headers and footers](#custom-headers-and-footers).

   - Error Heading Fallback: Turn off the error heading that displays as a fallback if there is no heading in the page content.

   - Remember Me: Add a checkbox to the sign-on card that lets end users choose to have their username remembered and prepopulated. If checked, the UI stores an end-user's username in local storage after their next sign-on attempt.

     The optional Label field lets you specify a custom label to display to the end user to replace the default label of Remember Me.

   - Scripted Tags: Add HTML scripted tags to journey pages. |
   | Account Pages | Styles   | This includes customizing the colors of:- The left end-user Navigation pane.

   - The Top Bar where the user logs out.

   - The Page Styles that present user information.

   - The Cards that are contained within the page that display various information.

   - Global Settings: These are the styles you set in the Global tab. Modifying this section from the Account Pages updates the Global tab styles.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
   |               | Logo     | Logo to display on customer-facing pages                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
   |               | Layout   | This includes:- Navigation: Configure the visibility, ordering, grouping, and icons of menu items in the hosted account pages left menu. You can also add custom menu items. Learn more in [Customize the account pages menu](hosted-pages-account.html#customize-the-account-pages-menu).

   - Footer: Place a footer below all account pages. Learn more in [Custom headers and footers](#custom-headers-and-footers).

   - Profile Page: Learn more in [Configure visible information and end-user actions](#configure-visible-information-and-end-user-actions).

   - Scripted Tags: Add HTML scripted tags to account pages.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |

5. Click Save.

6. (Optional) Configure the new theme as the default theme for the realm:

   The default theme is the theme that's used when you don't [apply a specific theme to an authentication journey](#apply-a-custom-theme-to-a-journey).

   1. In the Advanced Identity Cloud admin console, go to Hosted Pages.

   2. In the list of themes, click the new theme's ellipsis icon ([icon: more_horiz, set=material, size=inline]) and then click Set as Realm Default.

|   |                                                                                                                                                                                              |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | [Customize a theme for hosted pages](../use-cases/use-case-customize-theme.html) also demonstrates how to customize the look and feel of the hosted pages to match your company's branding . |

### Localize the favicon and theme logo

To localize the favicon or theme logo:

1. On the Global, Journey Pages, or Account Pages tabs, click the Favicon or Logo tabs from the right pane.

2. Click the favicon or logo .

3. Click + Specify a Locale.

4. In the Locale field, enter the ISO 639-1 (2 letter country code) for the language. For example, for French the value would be `fr`.

5. Click Add.

6. In the Favicon URL field or the Logo URL field, enter the URL for the favicon or logo.

   |   |                                         |
   | - | --------------------------------------- |
   |   | The images must be publicly accessible. |

7. To set alternative text for the logo, in the Alt Text field, enter alternate text.

8. Click Update.

9. Click Save.

## Apply a custom theme to a journey

In the Advanced Identity Cloud admin console:

1. Select Journeys.

2. Select the journey to apply the custom theme.

3. Click Edit.

4. Click ... > Edit Details.

5. Select Override theme.

6. Select the custom theme that you want to apply to this journey, then click Save.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Theme definitions and the mappings between authentication journeys and themes are stored in Advanced Identity Cloud as configuration objects. They are therefore "static" in terms of Advanced Identity Cloud promotion. If you add a new theme or logo, your change must go through the promotion process. Theme *selection* can be dynamic, however. If you set a theme in a page node during a journey, for example, by setting `stage var themeID=myTheme`, that theme is applied dynamically for the remainder of the journey. |

## Custom headers and footers

Each theme lets you configure localized custom headers and footers:

|               | Header                | Footer                |
| ------------- | --------------------- | --------------------- |
| Journey pages | [icon: check, set=fa] | [icon: check, set=fa] |
| Account pages | n/a                   | [icon: check, set=fa] |

Headers and footers can take HTML or inline CSS to insert links, classes, and other elements. Scripting isn't supported in headers and footers.

The account footer is separate from the journey footer. This lets you set up different buttons, links, and other elements, that display to an end user after they sign on.

### Enable headers and footers for a theme

1. In the Advanced Identity Cloud admin console, go to Hosted Pages, then select a theme.

2. Select either Journey Pages or Account Pages.

3. In the panel on the right-hand side, click Layout.

   1. Find the Header section (journey pages only), then enable the switch.

   2. Find the Footer section, then enable the switch.

### Edit headers and footers

1. Follow the [steps above](#enable-headers-and-footers-for-a-theme) to find the appropriate Header or Footer section, then click the preview to open the editor.

2. If you do not need localized content, edit the HTML as appropriate, then go to step 4.

3. If you need localized content:

   1. Add as many locales as you need. Learn more in [Localize headers and footers](#localize-headers-and-footers).

   2. Use the locale selector to change locales, and edit the HTML in each locale as appropriate.

4. Click Save.

### Localize headers and footers

1. Follow the [steps above](#enable-headers-and-footers-for-a-theme) to find the appropriate Header or Footer section, then click the preview to open the editor.

2. To add an initial locale for the existing header or footer content:

   1. Click + Specify a Locale to open a secondary modal.

   2. In the Add a Locale secondary modal, enter a locale identifier; for example, `fr` (French), or `fr-ca` (French - Canada).

   3. Click Add to add the locale and close the secondary modal.

   4. The + Specify a Locale link will now be replaced by a locale selector, with the new locale preselected.

3. To add an additional locale:

   1. Click the locale selector, then click + Add Locale to open a secondary modal.

   2. In the Add a Locale secondary modal, enter a locale identifier; for example, `es` (Spanish), or `es-ar` (Spanish - Argentina).

   3. Click Add to add the locale and close the secondary modal.

   4. The new locale will now be available in the locale selector, and be preselected. The header or footer content for the new locale will be a copy of the header or footer content from the initial locale.

   5. Translate the header or footer content for the new locale.

4. Repeat step 3 for as many locales as you need.

5. Click Save.

**Video (Video)**

<\_images/mp4/custom-theme-locale-headers-footers.mp4>

## Configure actions and information for end users

### Hosted journey pages

You can configure the following self-service features to control the actions and information displayed to end users when they sign on:

#### Configure terms and conditions

Configure the terms and conditions your end users must accept before they can complete a registration journey. Learn more in [Terms and conditions](../self-service/self-registration.html#terms-conditions).

#### Configure privacy and consent

Configure the external resources your end users can choose to share their data with. Learn more in [Privacy and consent](../self-service/self-registration.html#privacy-consent).

#### Configure security questions

Configure the security questions your end users answer during a registration journey and can later use during a reset journey to verify their identity. Learn more in [Security questions](../self-service/self-registration.html#security-questions).

### Hosted account pages

You can control the information displayed and the actions end users can take from the hosted account pages. Learn more in:

* [Configure visible information and end-user actions](#configure-visible-information-and-end-user-actions)

* [Prevent end users from editing specific personal data](#prevent-end-users-from-editing-properties)

#### Configure visible information and end-user actions

Your end users can only see the information and take actions that you configure.

To configure the information users can see and the actions they can take:

1. In the Advanced Identity Cloud admin console, go to Hosted Pages.

2. Select a theme or click + New Theme.

   If you create a new theme, enter a Name for the theme and click Save.

3. Click the Account Pages tab. This refers to the Advanced Identity Cloud admin console pages.

4. In the panel on the right-hand side, click Layout.

5. The Profile Information section determines the actions and information end users can see. Select or deselect any of the following:

   | Profile page component  | Description[]()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
   | ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | Personal Information    | Lets end users view and update their personal data. The attributes displayed depend on settings at the property level. Learn more in [User identity attributes and properties reference](../identities/user-identity-properties-attributes-reference.html).You can prevent end users from updating specific personal data. Learn more in [Prevent end users from editing specific personal data](#prevent-end-users-from-editing-properties).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
   | Sign-in & Security      | Enable any of the following:- Password: Allow end users to update their password. Uses an existing session. This correlates to the default journey UpdatePassword.

     To change the journey used for password updates:

     1. In the Advanced Identity Cloud admin console, select Native Consoles > Access Management.

     2. In the left navigation pane, click Services.

     3. Select Self Service Trees.

     4. In the updatePassword field, enter the name of the journey.

     5. Click Save Changes.

   - Security Questions: Lets end users reset their security questions on their profile.

   - 2-Step/Push Authentication: If an end user has registered a device for MFA, this option displays as enabled.

     If enabled, a Change link displays to end users. End users can click this link to view a 2-Step/Push Authentication page that displays the devices they have registered for MFA.

     For each device, end users can view when it was last used for sign on, view when it was added, edit its name, and delete it. If more than one device is registered, end users can also view which device was used most recently for sign-on. |
   | Social Sign-In          | Lets end users view the social providers that have authenticated with, such as Google or Facebook.For details on letting end users connect to social providers from their profile page, learn more in [Social authentication](../self-service/social-registration.html). After you configure social providers and create the journey, add it as the connectSocial journey for the realm:1) In the Advanced Identity Cloud admin console, select Native Consoles > Access Management.

   2) In the left navigation pane, click Services.

   3) Select Self Service Trees.

   4) Add a connectSocial field whose value is the name of the journey.

   5) Click Save Changes.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
   | Trusted Devices         | Lets end users view the devices that have been used to sign on to their account. End users can update the name of the device.	To populate the Trusted Devices tab, add the Device Profile Collector node to your authentication journeys to collect end-user device information.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
   | Authorized Applications | Lets end users view and manage the applications that have access to their personal information.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
   | Preferences             | Lets end users view and set preferences for communication. For example, an end user can select if they want to receive emails regarding special offers and services.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
   | Consent                 | Lets end users view and manage how their data is shared with third parties.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
   | Account Controls        | Lets end users download the data Advanced Identity Cloud has about them in a JSON format and lets end users delete their account (identity) information.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |

6. Click Save.

#### Prevent end users from editing specific personal data

End users can view their Advanced Identity Cloud personal data by selecting Profile > Edit Personal Info in the hosted account pages.

When you enable [personal information](#theme-personal-information) for end users in the theme, all [Advanced Identity Cloud properties](../identities/user-identity-properties-attributes-reference.html) are marked as User Editable. This means end users can view and update all their personal data directly in the hosted account pages. However, you might want to prevent end users from updating certain data. For example, email addresses could require verification, which can't be guaranteed if end users can modify them.

To prevent end users from updating specific personal data:

1. In the Advanced Identity Cloud admin console, select Native Consoles > Identity Management.

2. Select Configure > Managed Objects from the top tabs.

3. Click the user identity to update, for example Alpha\_user.

4. On the Properties tab, select the property to modify.

5. On the Details tab, select Show advanced options.

6. Deselect the User Editable option.

7. Click Save. The property is no longer editable by end users.

8. Repeat steps 4 - 7 for every property you want to prevent end users from updating.

|   |                                                                                                                                                                                                                     |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | You can hide a property from the personal data in the hosted account pages by deselecting the Viewable option. However, this hides the property of the user identity from both end users and tenant administrators. |

## Use script tags in hosted pages

You can include script tags in hosted pages to integrate third-party scripts such as customer analytics.

1. In the Advanced Identity Cloud admin console, go to Hosted Pages, then select a theme.

2. Select either Journey Pages or Account Pages.

3. In the panel on the right-hand side, click Layout.

   1. Find the Script Tags section.

   2. In the HTML field, enter your script code. The following example adds a script for the [OneTrust](https://www.cookiepro.com/) cookie consent service:

      ```js
      <script type="text/javascript" charset="UTF-8" src="https://cdn.cookielaw.org/scripttemplates/otSDKStub.js" data-domain-script="<account-id>"></script>(1)
      <script type="text/javascript">
        function OptanonWrapper() {};
      </script>
      ```

      |       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
      | ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
      | **1** | In this example, `<account-id>` needs replacing with a [OneTrust](https://www.cookiepro.com/) account ID.&#xA;&#xA;Do not attempt to use scripts with nested nodes. All nodes must be at the same level.&#xA;&#xA;The script code can include comments.&#xA;&#xA;The script code can include all valid attributes listed here: https\://developer.mozilla.org/en-US/docs/Web/HTML/Element/script#attributes.&#xA;&#xA;The script code must be wrapped in \<script> tags. |

   3. Click Save.

4. Update the tenant's [Content Security Policy](../tenants/content-security-policy.html):

   * If the tenant has an active report-only policy, update it by adding the domain of the third-party script to the `script-src` policy directive.

   * If the tenant has an active enforced policy, update it by adding the domain of the third-party script to the `script-src` policy directive.

   Learn more in [Configure CSP to let hosted pages use a script from an external domain](../tenants/content-security-policy.html#allow-hosted-pages-to-use-a-script-from-an-external-domain).

---

---
title: Debug end-user journeys
description: Debug Advanced Identity Cloud end-user journeys by enabling debug mode to inspect shared, transient, and secure state between journey nodes
component: pingoneaic
page_id: pingoneaic:end-user:debug-enduser-journeys
canonical_url: https://docs.pingidentity.com/pingoneaic/end-user/debug-enduser-journeys.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Authentication", "Journeys", "Realms", "Troubleshooting"]
page_aliases: ["uis:debug-enduser-journeys.adoc"]
section_ids:
  enable-debug-mode: Enable debug mode
  view-debug-information-in-a-pop-up-window: View debug information in a pop-up window
  shared-transient-and-secure-state: Shared, transient, and secure state
---

# Debug end-user journeys

You can debug end-user journeys in your PingOne Advanced Identity Cloud development environment as you create them. By setting a journey to debug mode, you can view information stored in [shared, transient, and secure state](#shared-transient-and-secure-state), as you navigate the journey. This lets you confirm that information is being passed correctly from node to node in the journey.

## Enable debug mode

Enable debug mode to log debug information as you navigate a journey.

1. In the Advanced Identity Cloud admin console, go to Journeys, and select a journey.

2. Hover over the journey schematic, and click Edit.

3. In the journey editor, click the debug button [icon: build_circle, set=material, size=inline] (on the top right of the toolbar). The Debug panel opens.

4. In the Debug panel, enable Debug mode.

5. Select Enable Debug Popup to display debug logs as you navigate the journey. Learn more in [view debug information in a popup window](#view-debug-information-in-a-pop-up-window).

6. Click Save to save your journey with debug mode enabled.

|   |                                                                                                                                                                                                                                                                                      |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | * Use debug mode only in your development environment.

* Before promoting a journey to your staging environment, ensure that you have deactivated debug mode and saved the journey. Journeys that are in debug mode are clearly marked with a Debug label in the journey list view. |

## View debug information in a pop-up window

View debug log output in a separate pop-up window, as you navigate a journey.

1. In the Advanced Identity Cloud admin console:

   1. [Enable debug mode](#enable-debug-mode).

   2. In the journey editor, copy the end-user journey URL from the Preview URL field (on the right, above the top toolbar).

2. In a new incognito browser window (or a separate browser):

   1. Go to the end-user journey URL that you copied in the previous step.

   2. The browser window should display an initial debug step in a new pop-up window. The pop-up window's title is Debug Popup.

3. If the pop-up window doesn't display, your browser might be blocking it:

   1. Unblock it by following the instructions for your browser:

      * For Chrome, follow the instructions under the "Allow pop-ups and redirects from a site" section in this support article: [https://support.google.com/chrome/answer/95472](https://support.google.com/chrome/answer/95472#zippy=allow-pop-ups-and-redirects-from-a-site).

      * For other [supported browsers](../product-information/supported-browsers.html), consult the browser's documentation.

   2. Refresh the browser window. The pop-up window should now display. If it doesn't display, repeat the previous step and ensure that your browser isn't blocking pop-ups.

4. Arrange the browser window and the pop-up window so that they're both clearly visible.

5. Navigate the journey in the browser window, and monitor the debug output for each step in the pop-up window.

## Shared, transient, and secure state

* Shared state

  Used by nodes to store non-sensitive information required during the authentication flow.

* Transient state

  Used by nodes to store sensitive information that Advanced Identity Cloud encrypts on round trips to the client.

* Secure state

  Used by nodes to store decrypted transient state.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | When debug mode is enabled, debug nodes are temporarily inserted between each node in the journey. Because debug nodes can change the state of node information, inserting them between each node in the journey can cause a problem if a later node expects to access information in a specific state.An example is when a node adds a password to transient state. The following debug node reads that password from transient state, which removes it. The next node in the journey expects to read the password from transient state, and when it tries to do so, this fails and causes an error. |

---

---
title: End-user UX journey flows
description: Compare centralized and embedded journey flows in Advanced Identity Cloud to choose the right sign-on experience for your end users
component: pingoneaic
page_id: pingoneaic:end-user:end-user-ux-journey-flows
canonical_url: https://docs.pingidentity.com/pingoneaic/end-user/end-user-ux-journey-flows.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["User Interface", "Journeys"]
section_ids:
  centralized-journey-flows: Centralized journey flows
  embedded-journey-flows: Embedded journey flows
---

# End-user UX journey flows

Journey flows define the sign-on experience for end users. The [End-user UX options](end-user-ux-options.html) available in PingOne Advanced Identity Cloud offer two journey flows:

* [Centralized](#centralized-journey-flows)

* [Embedded](#embedded-journey-flows)

Not every end-user UX option supports both centralized and embedded journey flows. Learn more in [Compare end-user UX options](end-user-ux-options-compare.html) for more information.

## Centralized journey flows

Centralized journey flows redirect end users to an external page to sign in. This is a common experience for most users. This approach is considered the security best practice for Advanced Identity Cloud, ensuring all your applications and websites can share the same, centralized authentication processes.

An example of a centralized journey flow is Google G Suite, where an end user is redirected to the same authentication page no matter which application they're trying to access.

The following video shows a [centralized journey flow with Ping SDKs](https://docs.pingidentity.com/sdks/latest/oidc/index.html):

**Video (Video)**

<\_images/mp4/android\_central.mp4>

Use the hosted pages and the SDK [end-user UX options](end-user-ux-options.html#ux-options) to implement centralized journey flows.

## Embedded journey flows

Embedded journey flows offer a more traditional sign-on experience, as end users are not redirected to an external page.

Embedded journey flows aren't considered to be a security best practice for the following reasons:

* Individual applications have access to end user's credentials.

* Individual applications have access to the [authorization grant](../am-oauth2/oauth2-authz-grant.html).

* Each application must manually build in security during the sign-on process.

The following video shows an [embedded journey flow with Ping SDKs](https://docs.pingidentity.com/sdks/latest/sdks/index.html):

**Video (Video)**

<\_images/mp4/android\_embedded.mp4>

Use the Login Widget and the SDK [end-user UX options](end-user-ux-options.html#ux-options) to implement embedded journey flows.

---

---
title: End-user UX options for authentication journeys and account management
description: "Choose an end-user UX option for Advanced Identity Cloud: hosted pages, Login Widget, SDKs, or REST API for authentication journeys and account management"
component: pingoneaic
page_id: pingoneaic:end-user:end-user-ux-options
canonical_url: https://docs.pingidentity.com/pingoneaic/end-user/end-user-ux-options.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["User Interface", "Journeys", "Integration", "Authentication"]
page_aliases: ["realms:applications-end-user-ui-options.adoc", "uis:ui-integration-options.adoc"]
section_ids:
  ux-options: UX options
  identity-cloud-hosted-pages: Advanced Identity Cloud hosted pages
  ping-forgerock-login-widget: Ping (ForgeRock) Login Widget
  ping-sdks: Ping SDKs
  identity-cloud-rest-api: Advanced Identity Cloud REST API
  platform-login-and-end-user-uis: Ping Identity Platform login and end-user UIs (deprecated)
---

# End-user UX options for authentication journeys and account management

When you integrate your applications with PingOne Advanced Identity Cloud, you must provide your end users with a UX (user experience) that handles authentication journeys and account management.

Advanced Identity Cloud provides these end-user UX options:

[icon: wysiwyg, set=material, size=3x]

#### [Advanced Identity Cloud hosted pages](#identity-cloud-hosted-pages)

Use Advanced Identity Cloud's built-in and fully-featured UIs with no development work.

[icon: widgets, set=material, size=3x]

#### [Ping (ForgeRock) Login Widget](#ping-forgerock-login-widget)

Use a widget to integrate authentication journeys easily into your client-side JavaScript web applications.

[icon: developer_mode, set=material, size=3x]

#### [Ping SDKs](#ping-sdks)

Use SDKs for web, Android, or iOS applications. Integrate the SDK into Advanced Identity Cloud using the REST API.

[icon: api, set=material, size=3x]

#### [Advanced Identity Cloud REST API](#identity-cloud-rest-api)

Build your own custom UIs without any Ping Identity prebuilt components and integrate with Advanced Identity Cloud REST API.

The options are not mutually exclusive, and you may need a combination of them to meet your company's requirements. For a quick take on which option is most suitable for you, learn more in [Compare end-user UX options](end-user-ux-options-compare.html).

## UX options

### Advanced Identity Cloud hosted pages

Advanced Identity Cloud hosted pages provide OOTB *(tooltip: Out of the box)* UIs for the following:

* End-user journeys, such as sign on, registration, and password reset

* End-user account activities, such as managing profile information, viewing application access, and viewing roles and entitlements

This is the most straightforward end-user UX option since all the necessary capabilities are readily available.

Hosted pages can be [customized with themes](hosted-pages-customize.html). Themes let you adjust layouts and add company logos, headers, and footers. They also let you change the colors of buttons, links, backgrounds, and more. You can create multiple themes in a realm, set the default theme for the realm, and assign specific themes to different end-user journeys.

Hosted pages are useful if you have limited theming needs or want to try new registration or authentication flows without integrating them into an application. The hosted pages UI is designed for web applications and isn't supported in native applications.

This UX option only lets you use centralized journey flows in your applications, with embedded journey flows not supported. Specifically, Ping Identity does not support embedding hosted pages in HTML frames.

This is the only UX option that supports SAML journey flows that use Advanced Identity Cloud as the IdP.

Learn more in [Hosted pages](hosted-pages.html).

### Ping (ForgeRock) Login Widget

The Ping (ForgeRock) Login Widget provides an OOTB *(tooltip: Out of the box)* UI for end-user authentication journeys, such as sign on, registration, and password reset. It doesn't provide a UI for account management.

The Login Widget is low-code and framework-agnostic; it can be initiated with a few lines of code and can be easily integrated into any modern JavaScript application. It does not currently support server-side rendering (SSR), including Node.js.

The Login Widget provides OOTB *(tooltip: Out of the box)* support for localization, social login, WebAuthn, passkey, device profile, token management, and compliance with WCAG standards. It is highly themeable and customizable with CSS and Javascript.

Learn more in [Ping (ForgeRock) Login Widget](https://docs.pingidentity.com/sdks/latest/login-widget/index.html).

### Ping SDKs

The Ping SDKs let you develop your own custom UI for web, Android, or iOS applications. You then integrate it with your Advanced Identity Cloud tenant using the [REST API](../developer-docs/authenticate-to-rest-api-overview.html).

Each SDK provides an OOTB *(tooltip: Out of the box)* UI module that allows you to prototype your custom UI; however, it is only provided as a starting point, and it is not intended for production use.

This option offers a lot of flexibility if you want to customize the behavior, layout, and theming of the UI, or want to support [Android](https://docs.pingidentity.com/sdks/latest/sdks/tutorials/android/index.html) and [iOS](https://docs.pingidentity.com/sdks/latest/sdks/tutorials/ios/index.html) applications. Using it requires a higher level of technical skill than the previous options.

SDKs can use centralized and embedded journey flows.

Learn more in [Ping SDKs](sdks.html).

### Advanced Identity Cloud REST API

The most flexible UX option is to build your own custom UIs and integrate with the Advanced Identity Cloud REST API. However, this is also the most complex and time-consuming UX option, as you need to build everything yourself without any Ping Identity prebuilt components.

In addition, you will also need deep identity implementation experience, including an understanding of how to securely store tokens locally.

Learn more in [Advanced Identity Cloud REST API](../developer-docs/authenticate-to-rest-api-overview.html).

### Ping Identity Platform login and end-user UIs (deprecated)

|   |                                                                                                                                                                                                                                                        |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | Ping Identity no longer recommends or supports this UX option due to the complexity of configuring the distributable packages. For a quick take on alternative options, learn more in [Compare end-user UX options](end-user-ux-options-compare.html). |

Ping Identity also provides the hosted pages UIs as distributable packages, known as the platform login and end-user UIs. You can self-host one or both of the UIs and configure them to use your Advanced Identity Cloud tenant.

This UX option offers flexibility if you want to customize the layout of the UIs or customize the theming beyond what the hosted pages provide. The UIs support web applications but not native applications.

This UX option also lets you use both centralized and embedded journey flows in your applications.

For background information about the platform end-user and login UIs, learn more in [Platform UIs](https://docs.pingidentity.com/platform/8/platform-setup-guide/platform-ui.html).

---

---
title: Hosted account pages
description: "Configure Advanced Identity Cloud hosted account pages for end-user self-service: profile management, MFA, delegated admin, and menu customization"
component: pingoneaic
page_id: pingoneaic:end-user:hosted-pages-account
canonical_url: https://docs.pingidentity.com/pingoneaic/end-user/hosted-pages-account.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Hosted Pages", "User Interface", "End User", "User Profile", "Identity Governance"]
page_aliases: ["identity-governance:user-tasks/user-information.adoc", "end-user:end-user-screens-actions.adoc", "end-user:end-user-pages.adoc"]
section_ids:
  summary-of-features: Summary of features
  account-pages-menu: Account pages menu
  menu-items-available-as-standard: Menu items available as standard
  menu-items-available-with-add-on-capabilities: Menu items available with add-on capabilities
  customize-the-account-pages-menu: Customize the account pages menu
  enable-delegated-administrator-menu-items: Enable delegated administrator menu items
  change-menu-item-visibility: Change the visibility of a menu item
  change-menu-item-order-and-grouping: Change menu item order and grouping
  change-menu-item-label-and-icon: Change menu item label and icon
  add-custom-menu-items: Add custom menu items
---

# Hosted account pages

Hosted account pages are pre-built, customizable web pages that provide end users with self-service capabilities for managing their accounts after they've signed on. They're a key part of the end-user experience and are designed to help you quickly set up common end-user self-service operations without needing to build your own custom web pages from scratch.

![Hosted account profile page example with full menu](_images/hosted-account-page-example-full-menu.png)Hosted account pages example page with full menu

## Summary of features

These pages allow authenticated end users to perform essential account management tasks. The specific features available depend on your Advanced Identity Cloud configuration, but commonly include:

* **Profile management**: End users can view and update their personal information (for example, name, email address, address) if they're configured to be editable.

* **Security management**:

  * **Password updates**: Allowing end users to change their password.

  * **Multi-factor authentication (MFA)**: Managing registered devices or two-step verification settings.

  * **Security questions**: Viewing or resetting their security questions.

* **Access and entitlement viewing**: End users can see details about their access within integrated applications, which often includes:

  * **My applications**: Viewing and navigating to applications they have access to.

  * **Roles and entitlements**: Seeing the roles and specific privileges (entitlements) they have been assigned in onboarded target applications.

  * **Account controls**: Allowing end users to download or delete their own account data (if enabled).

* **Identity governance**: With Identity Governance\[[1](#_footnotedef_1 "View footnote.")], end users can also:

  * **Manage delegates**: Assign individuals to handle their access reviews or other delegated items.

  * **View direct reports**: Managers can access the accounts, entitlements, and roles of their direct reports.

  * **Manage requests**: Create or view requests they have submitted for gaining access to an application, entitlement, or role.

## Account pages menu

The hosted account pages include a navigation menu that provides easy access to the various self-service features.

The items displayed in the menu depend on a number of factors:

* **Availability and visibility**: Menu items display based on their availability and visibility as follows:

  * Available as standard, visible by default to all end users.

  * Available as standard, visible based on the delegated administrator privileges of the end user.

  * Available and visible to all end users as part of an add-on capability, such as IGA\[[1](#_footnotedef_1 "View footnote.")].

* **Configuration**: You can override the visibility of menu items through configuration settings to suit your company's needs. This lets you hide certain menu items that are not relevant to your end users. For example, hiding the organization menu item from organization administrators whose regular job only requires managing users within the organization, but not the organization itself. Learn more in [Change menu item visibility](#change-menu-item-visibility).

You can also [change the order and grouping](#change-menu-item-order-and-grouping) of menu items in the navigation menu, [add custom menu items](#add-custom-menu-items), and [modify their icons](#change-menu-item-label-and-icon) to align with your branding.

### Menu items available as standard

The following table summarizes the behavior of the menu items that are available as standard in the hosted account pages:

| Menu item                                                                                                                                     | Visibility                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                                                                                             |
| --------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [icon: dashboard, set=material, size=inline] Dashboard                                                                                        | * Visible by default.

* Can be individually hidden via configuration. Learn more in [Change menu item visibility](#change-menu-item-visibility).                                                                                                                                                                                                                                                                                                                                                                                                              | Displays tasks and information that require the end user's attention.                                                                                                                                                                                                                                   |
| [icon: apps, set=material, size=inline] Applications                                                                                          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Lets the end user view and access their applications. Displays [SAML-based applications](../app-management/register-a-custom-application.html#custom-saml-app-template-sso) and [Bookmark applications](../app-management/register-a-custom-application.html#bookmark), but not OAuth 2.0 applications. |
| [icon: person, set=material, size=inline] Profile                                                                                             |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Lets the end user view and edit their account profile, including personal information.The actions available on this page vary depending on the configurations set in [Configure actions and information for end users](hosted-pages-customize.html#configure-actions-and-information-for-end-users).    |
| [icon: summarize, set=material, size=inline] Reports                                                                                          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Lets the end user view any reports shared with them by a tenant administrator.                                                                                                                                                                                                                          |
| [icon: vpn_key, set=material, size=inline] Alpha realm - Assignment  or [icon: vpn_key, set=material, size=inline] Bravo realm - Assignment   | - Visible based on delegated administrator privileges. Requires the end user to be assigned to an internal role that has at least the view privilege for the role identity type. Learn more in [Enable delegated administrator menu items](#enable-delegated-administrator-menu-items).

- Organization and user menu items also visible based on organization privileges (being an organization administrator, owner, or member).

- Can be individually hidden via configuration. Learn more in [Change menu item visibility](#change-menu-item-visibility). | Lets the end user access the management interface for the identity type.                                                                                                                                                                                                                                |
| [icon: group, set=material, size=inline] Alpha realm - Group  or [icon: group, set=material, size=inline] Bravo realm - Group                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                         |
| [icon: domain, set=material, size=inline] Alpha realm - Organization  or [icon: domain, set=material, size=inline] Bravo realm - Organization |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                         |
| [icon: assignment_ind, set=material, size=inline] Alpha realm - Role  or [icon: assignment_ind, set=material, size=inline] Bravo realm - Role |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                         |
| [icon: people, set=material, size=inline] Alpha realm - User  or [icon: people, set=material, size=inline] Bravo realm - User                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                         |
| [icon: people, set=material, size=inline] Internal Role                                                                                       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                         |

### Menu items available with add-on capabilities

The following table summarizes the behavior of the menu items that are available with add-on capabilities in the hosted account pages:

| Menu item                                                                                                           | Visibility                                                                                                                                                                                                                      | Description                                                                                                                                                                                                                                                                                                                                                                                               |
| ------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [icon: inbox, set=material, size=inline] My InboxSubmenu items:- Approvals

- Tasks

- Access Reviews

- Violations | * Visible by default with IGA\[[1](#_footnotedef_1 "View footnote.")].

* Menu items and submenu items can be individually hidden via configuration. Learn more in [Change menu item visibility](#change-menu-item-visibility). | Displays all items assigned to an end user.This includes:* Any approval items (submitted access requests) for an approver (designated owner) to act on.

* Any tasks assigned to the end user.

* Any access reviews assigned to a certifier (individual assigned to review the access).

* Any policy violations that require the end user's attention.                                                  |
| [icon: lock, set=material, size=inline] My AccessSubmenu items:* My Accounts

* My Roles

* My Entitlements         |                                                                                                                                                                                                                                 | Lets the end user view the access they have in Advanced Identity Cloud and via applications.This includes:* Accounts from onboarded target applications.

* Roles they're assigned in Advanced Identity Cloud.

* Entitlements or privileges they have in onboarded target applications.Learn more in [Request access to resources](../identity-governance/end-user/access-requests-request-access.html). |
| [icon: folder, set=material, size=inline] My DirectorySubmenu items:* My Delegates

* Direct Reports                |                                                                                                                                                                                                                                 | Lets the end user manage the delegates and direct reports (employees) they have.End users can perform the following actions:* Manage their *delegates*. Delegates are individuals that are assigned to their access reviews.

* Access their *direct reports* and the access granted to them.                                                                                                             |
| [icon: send, set=material, size=inline] My Requests                                                                 |                                                                                                                                                                                                                                 | Lets the end user view and create requests to access resources, such as target applications, entitlements, or roles.Learn more in [Request access to resources](../identity-governance/end-user/access-requests-request-access.html).                                                                                                                                                                     |

## Customize the account pages menu

### Enable delegated administrator menu items

By default, the menu items related to delegated administrator privileges (for example, `Alpha realm - User`) aren't visible to end users. These menu items become visible only when an end user is assigned to an internal role that has at least the view privilege for the corresponding identity type.

The following steps describe how to create an internal role with the necessary privileges to manage an identity type and assign it to an end user.

1. In the Advanced Identity Cloud admin console, go to Identities > Manage.

2. Click Internal Roles.

3. Click [icon: add, set=material, size=inline] New Internal Role.

4. In the New Internal Role modal:

   1. Enter a name for the internal role. For example, `Delegated Administrator`.

   2. (Optional) Enter a description for the internal role.

   3. Click Next.

5. In the Internal role Permissions modal:

   1. In the Choose an identity object list, select an identity type. For example, Alpha realm - Users.

   2. Click [icon: add, set=material, size=inline] Add.

   3. Select at least the View privilege and any additional privileges for the identity type using the Create, Update, and Delete options.

      ![Internal role Permissions modal](_images/internal-role-permissions-modal.png)

   4. (Optional) Repeat the previous three steps to add additional identity types and their corresponding privileges as necessary.

   5. Click Next.

6. In the Dynamic Internal role Assignment modal, click Next.

7. In the Time Constraint modal, click Save to create the internal role.

8. In the Internal Role page, click the Members tab, then click [icon: add, set=material, size=inline] Add Members.

9. In the Add Members modal, select a user identity from the Members list that you want to assign the internal role to, then click Save.

The end user can now see the corresponding delegated administrator menu items in the hosted account pages navigation menu when they sign on.

|   |                                                                                                                                                                                                                                                               |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | For more complex delegated administration use cases, learn more in:- [Enable managers to manage their direct reports](../use-cases/use-case-manage-reports.html)

- [Create organizations to delegate administration](../use-cases/use-case-create-orgs.html) |

### Change the visibility of a menu item

Change the visibility of menu items to streamline the end-user experience.

1. In the Advanced Identity Cloud admin console, go to Hosted Pages, then select a theme.

2. Select Account Pages.

3. In the panel on the right-hand side, click Layout, then scroll to the Navigation section.

4. To hide a menu item:

   1. Find the menu item you want to hide, and click its ellipsis icon ([icon: more_horiz, set=material, size=inline]).

   2. Click [icon: delete, set=material, size=inline] Delete. This removes the menu item from the navigation menu, although it remains available for re-adding later.

   3. Click Save.

5. To show a previously hidden menu item:

   1. Click the add icon ([icon: add, set=material, size=inline]).

   2. From the list of available menu items, select the menu item you want to show, then click Next.

   3. Configure the menu item:

      1. (Optional) Change the Label.

      2. (Optional) Change the Icon Code. For a list of available icon codes, refer to [Material Icons](https://fonts.google.com/icons?icon.set=Material+Icons\&icon.style=Outlined).

      3. (Optional) If the menu item has submenu items, select which submenu items to include using the checkboxes under Dropdown Items. By default, all submenu items are selected.

   4. Click Add.

   5. (Optional) Click the menu item's drag indicator icon ([icon: drag_indicator, set=material, size=inline]) and drag the menu item to the desired position in the menu.

   6. Click Save.

### Change menu item order and grouping

Change the order and grouping of menu items in the navigation menu to suit your company's needs.

1. In the Advanced Identity Cloud admin console, go to Hosted Pages, then select a theme.

2. Select Account Pages.

3. In the panel on the right-hand side, click Layout, then scroll to the Navigation section.

4. To reorder menu items:

   1. Click a menu item's drag indicator icon ([icon: drag_indicator, set=material, size=inline]) and drag it to the desired position in the menu.

   2. Repeat for any other menu items you want to reorder.

5. To group menu items:

   1. (Optional) Add additional divider menu items to the menu:

      1. Click the add icon ([icon: add, set=material, size=inline]).

      2. From the list of available menu items, select Divider, then click Next.

      3. Repeat as necessary to add multiple divider menu items.

   2. (Optional) Remove existing divider menu items that you don't need:

      1. Find the divider menu item you want to remove, and click its ellipsis icon ([icon: more_horiz, set=material, size=inline]).

      2. Click [icon: delete, set=material, size=inline] Delete.

   3. Click the drag indicator icon ([icon: drag_indicator, set=material, size=inline]) of a Divider menu item and drag it to the desired position in the menu to create a visual separation between groups of menu items. Repeat for any other Divider menu items you want to reposition.

   4. Click Save.

### Change menu item label and icon

Change the label or icon for your menu items to better align with your company's branding.

1. In the Advanced Identity Cloud admin console, go to Hosted Pages, then select a theme.

2. Select Account Pages.

3. In the panel on the right-hand side, click Layout, then scroll to the Navigation section.

4. Find the menu item you want to change, and click its ellipsis icon ([icon: more_horiz, set=material, size=inline]).

5. Configure the menu item:

   1. (Optional) Change the Label.

   2. (Optional) Change the Icon Code. For a list of available icon codes, refer to [Material Icons](https://fonts.google.com/icons?icon.set=Material+Icons\&icon.style=Outlined).

   3. (Optional) If the menu item has submenu items, select which submenu items to include using the checkboxes under Dropdown Items. By default, all submenu items are selected.

6. Click Save.

### Add custom menu items

Add a custom menu item to link to other Ping Identity resources such as the [PingOne Dock](https://dock.pingidentity.com/), [PingOne self service](https://docs.pingidentity.com/pingone/user_experience/p1_self_service.html), or a specific [journey](../journeys/journeys.html) or [flow](https://docs.pingidentity.com/davinci/flows/davinci_flows.html). You can also link to resources in your company that end users may need to access.

1. In the Advanced Identity Cloud admin console, go to Hosted Pages, then select a theme.

2. Select Account Pages.

3. In the panel on the right-hand side, click Layout, then scroll to the Navigation section.

4. Click the add icon ([icon: add, set=material, size=inline]).

5. From the list of available menu items, select Custom Link, then click Next.

6. Configure the menu item:

   1. Enter a menu Label.

   2. (Optional) Change the Icon Code. For a list of available icon codes, refer to [Material Icons](https://fonts.google.com/icons?icon.set=Material+Icons\&icon.style=Outlined). Otherwise, the default link icon ([icon: link, set=material, size=inline]) is used.

   3. Enter an absolute URL for the custom menu item. The URL opens in a new browser tab when the end user clicks the menu item.

   4. Click Add.

7. (Optional) Click the menu item's drag indicator icon ([icon: drag_indicator, set=material, size=inline]) and drag the menu item to the desired position in the menu.

8. Click Save.

***

[1](#_footnoteref_1). IGA is an [add-on capability](../product-information/add-on-capabilities.html).

---

---
title: Hosted pages
description: Use Advanced Identity Cloud hosted pages — pre-built journey and account pages — to deploy identity flows without building UIs from scratch
component: pingoneaic
page_id: pingoneaic:end-user:hosted-pages
canonical_url: https://docs.pingidentity.com/pingoneaic/end-user/hosted-pages.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["User Interface", "Journeys", "Hosted Pages", "Authentication"]
page_aliases: ["realms:hosted-end-user-pages.adoc", "uis:identity-cloud-hosted-pages.adoc", "end-user:identity-cloud-hosted-pages.adoc"]
section_ids:
  key-features-and-customization: Key features and customization
  learn-how-to-customize-and-use-hosted-pages: Learn how to customize and use hosted pages
  sign-on-end-user: Sign on as an end user using hosted pages
  deactivate-hosted-journey-pages: Deactivate hosted journey pages
  deactivate-hosted-account-pages: Deactivate hosted account pages
---

# Hosted pages

The hosted pages feature in Advanced Identity Cloud provides a pre-built, cloud-hosted user interface that you can use out-of-the-box for common identity operations, significantly accelerating your deployment and development time. Instead of building every sign-on, registration, and self-service profile page from scratch, Advanced Identity Cloud hosts these pages for you.

Advanced Identity Cloud offers two types of hosted pages:

* **Hosted journey pages**: These pages guide an end user through an authentication journey. You can use them for sign-on, registration, multi-factor authentication (MFA) enrollment and verification, password reset processes, or any other authentication flow defined in a journey.

* **Hosted account pages**: These pages are accessed by end users after they've successfully authenticated, allowing them to manage their own profile and security settings. You can also use them to allow delegated administration, enabling end users to manage other end users' profiles based on the permissions you assign.

|                                                                                                                  |                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| ![Hosted journey sign-on page example](_images/hosted-journey-page-example.png)Hosted journey pages example page | ![Hosted account profile page example](_images/hosted-account-page-example.png)Hosted account pages example page |

The look and feel of the hosted pages can be customized in each realm to match your company's branding guidelines using an easy-to-use editor in the Advanced Identity Cloud admin console:

![Custom themes overview page.](_images/hosted-pages-editor.png)Hosted pages editor

## Key features and customization

While they are pre-built, hosted pages are highly customizable to ensure they match your brand.

* **Theming and branding**: You can create and apply themes to customize the look and feel (colors, fonts, layout, logos) to meet your company's branding guidelines. This allows the pages to look like a seamless part of your application.

* **Localization**: Hosted pages support multiple languages (localization), allowing you to serve users in different regions with their preferred language.

* **Configurability**: Within the Advanced Identity Cloud admin console, you can configure what information is displayed and which actions users are allowed to take.

* **Easy integration**: They are the simplest UX option to implement, as they are part of the cloud service.

* **Security**: Hosted pages are maintained and updated by Ping Identity, ensuring they adhere to the latest security standards and best practices.

## Learn how to customize and use hosted pages

* [Customize hosted pages](hosted-pages-customize.html): Customize the look and feel of the sign-on (journey) pages. This includes logos, headers, footers, the layout of the overall page, and the actions and information your end users have access to in the hosted account pages.

* [Localize hosted pages](hosted-pages-localize.html): Support different languages in the hosted pages with localization.

* [Configure hosted account pages](hosted-pages-account.html): Configure hosted account pages for end-user profile management.

## Sign on as an end user using hosted pages

To sign on to the hosted account pages for a realm:

1. Access the `Login` journey using one of the following URL formats:

   * If you are using the tenant domain, use one of these URL formats, replacing \<realm> with the value `alpha` or `bravo`:

     * Full URL format:

       ```none
       https://<tenant-env-fqdn>/am/XUI/?realm=<realm>&authIndexType=service&authIndexValue=Login
       ```

     * Shortcut URL format:

       ```none
       https://<tenant-env-fqdn>/enduser/?realm=<realm>
       ```

   * If you are using a [custom domain](../realms/custom-domains.html), use one of these URL formats:

     * Full URL format:

       ```none
       https://<custom-domain-fqdn>/am/XUI/?authIndexType=service&authIndexValue=Login
       ```

     * Shortcut URL format:

       ```none
       https://<custom-domain-fqdn>/enduser/
       ```

2. Enter sign-on credentials.

3. Click Next. The end user is signed on to the hosted account pages.

## Deactivate hosted journey pages

You can use the Ping SDKs or APIs to create and host your own custom journeys. If you do this, Ping Identity recommends that you deactivate the hosted journey pages to ensure there is no risk of unauthorized access to the sign-on, registration, or password reset pages by a malicious user.

Deactivating hosted journey pages disables them in both the Alpha and Bravo realms. You cannot deactivate hosted journey pages for just one realm.

|   |                                                                                |
| - | ------------------------------------------------------------------------------ |
|   | Hosted journey pages can be deactivated independently of hosted account pages. |

When you deactivate the hosted journey pages, Advanced Identity Cloud displays the following web page to unauthorized end users:

![Screenshot of a browser showing the message 'You are not authorized to view this site'](_images/default-journeys-deactivated.png)

After you deactivate the default hosted journey pages, you can still administer the tenant environment while preventing unauthorized access to default journey information.

For an explanation about how hosted pages integrate with the default journey, learn more in [Journeys](../journeys/journeys.html).

## Deactivate hosted account pages

Hosted account pages are activated by default. If you deactivate them, you can reactivate them at any time.

You can use the Ping SDKs or APIs to create and host your own custom account pages. If you do this, Ping Identity recommends that you deactivate the hosted account pages to ensure there is no risk of unauthorized access to end-user profile information by a malicious user.

Deactivating hosted account pages disables them in both the Alpha and Bravo realms. You cannot deactivate hosted account pages for just one realm.

|   |                                                                                |
| - | ------------------------------------------------------------------------------ |
|   | Hosted account pages can be deactivated independently of hosted journey pages. |

When you deactivate the hosted account pages, Advanced Identity Cloud displays the following web page to unauthorized end users:

![Screenshot of a browser showing the message 'You are not authorized to view this site. Please sign out and try again'](_images/hosted-pages-deactivated.png)

After deactivating the default end-user profile, you can still use the hosted end-user journey UI while denying unauthorized access to end-user profiles. Your customers manage only their own profiles or delegate administration using *your* application.

1. In the Advanced Identity Cloud admin console, open the TENANT menu (upper right), and go to Tenant Settings > Global Settings.

2. Click End User UI.

3. On the End User UI page, do one of the following:

   * To activate hosted pages, beside Hosted Account Pages, click Activate. The Global Settings toggle displays the status as Active.

   * To deactivate hosted pages, beside Hosted Account Pages, click Deactivate. The Global Settings toggle displays the status as Inactive.

The change takes effect immediately.

|   |                                                                                                 |
| - | ----------------------------------------------------------------------------------------------- |
|   | When you deactivate hosted pages, all hosted pages associated with your tenant are deactivated. |

---

---
title: Localize hosted pages
description: Localize Advanced Identity Cloud hosted pages to support multiple languages using ISO-639-1 language codes for journey pages, headers, and footers
component: pingoneaic
page_id: pingoneaic:end-user:hosted-pages-localize
canonical_url: https://docs.pingidentity.com/pingoneaic/end-user/hosted-pages-localize.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["User Interface", "REST API", "Localization", "Translation", "Authentication"]
page_aliases: ["developer-docs:localizing-enduser-login-uis.adoc", "uis:localize-enduser-login-uis.adoc", "end-user:localize-enduser-login-uis.adoc", "end-user:localize-login-enduser-pages.adoc"]
section_ids:
  localize-at-feature-level: Localize at feature level
  localize-related-features: Localize related features
  localize-journey-authentication-nodes: Localize journey authentication nodes
  localize-at-ui-level: Localize at UI level
  specify-preferred-language-journeys: Specify a preferred language for journey pages
---

# Localize hosted pages

PingOne Advanced Identity Cloud lets you localize hosted pages to support the different languages of your end users. Use [ISO-639-1 language codes](https://en.wikipedia.org/wiki/List_of_ISO_639_language_codes) (for example `fr` and `de`) to provide locale specific content in as many locales as you need.

## Localize at feature level

### Localize related features

You can localize the following features related to hosted journey and account pages:

| Feature              | Description                                                                                                                                                                                                        |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Hosted pages         | Learn more in [Localize headers and footers](hosted-pages-customize.html#localize-headers-and-footers) and [Localize the favicon and theme logo](hosted-pages-customize.html#localize-the-favicon-and-theme-logo). |
| Security questions   | Learn more in [Security questions](../self-service/self-registration.html#security-questions).                                                                                                                     |
| Terms and conditions | Learn more in [Terms and conditions](../self-service/self-registration.html#terms-conditions).                                                                                                                     |
| Email templates      | Learn more in [Email templates](../tenants/email-templates.html).                                                                                                                                                  |

### Localize journey authentication nodes

You can individually localize authentication nodes that display content in hosted journey pages. For example, the [Page node](https://docs.pingidentity.com/auth-node-ref/latest/page.html) lets you add content to the Page Header property to display an initial journey message to end users. You can define as many localized versions of the message as you need:

![ui journeys page node page header modal](../tenants/_images/ui-journeys-page-node-page-header-modal.png)

## Localize at UI level

You can localize static content and server messages in the hosted pages using translation configuration. Learn more in [Localize tenant admin console and hosted pages](../tenants/tenant-localize.html).

## Specify a preferred language for journey pages

By default, Advanced Identity Cloud localizes the content of journey pages using the value of the `Accept-Language` header, which is typically derived from the language settings in the end-user's browser. You can override this behavior by appending a `locale` query parameter to the journey URL.

For example, to set the language to French, append `locale=fr` to the journey URL:

```bash
https://<tenant-env-fqdn>/am/XUI/?realm=/alpha&locale=fr&authIndexType=service&authIndexValue=Login
```

The language used to localize journey pages is determined in the following order of priority:

1. The `locale` query parameter in the journey URL (for example, `&locale=fr`).

2. The language preference set in the end-user's browser.

3. The default locale for hosted pages (`en`), used when neither a query parameter nor a browser language is provided.

---

---
title: Overview
description: Overview of Advanced Identity Cloud end-user experience options, self-service capabilities, and UI customization for authentication and account management
component: pingoneaic
page_id: pingoneaic:end-user:overview
canonical_url: https://docs.pingidentity.com/pingoneaic/end-user/overview.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
---

# Overview

PingOne Advanced Identity Cloud end users experience and regularly interact with user interfaces (UIs) and user self-service capabilities.

Advanced Identity Cloud provides different [UI customization options](end-user-ux-options.html) depending on the needs of your organization.

Advanced Identity Cloud end users can manage their own data, reset their password, retrieve their username, and more. The robust capabilities of Advanced Identity Cloud allows you to customize the end user screens, the applications they have access to, and the data they have access to. [User self-service journeys](admin-config-overview.html) by defining journeys and configuring the information end users can access, manage, and the actions they can take.

---

---
title: Ping SDKs
description: Use Ping Identity SDKs to build custom UIs for web, Android, and iOS applications against Advanced Identity Cloud REST APIs
component: pingoneaic
page_id: pingoneaic:end-user:sdks
canonical_url: https://docs.pingidentity.com/pingoneaic/end-user/sdks.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Integration", "Scripts", "REST API", "Third-Party", "Integration", "Setup &amp; Configuration", "Security"]
page_aliases: ["developer-docs:sdks.adoc"]
section_ids:
  upload_provided_files_to_integrate_with_android_or_ios_apps: Upload provided files to integrate with Android or iOS apps
---

# Ping SDKs

For an overview of all UI integration options, learn more in [End-user UX options for authentication journeys and account management](end-user-ux-options.html).

The Ping SDKs let you rapidly build applications against the PingOne Advanced Identity Cloud REST APIs.

Leverage Ping Identity's identity best practices for token exchange, security, and the optimal OAuth 2.0 flow.

Ping SDKs are highly customizable and require a high level of technical skill; therefore, the [SDK documentation](https://docs.pingidentity.com/sdks/latest/release-notes/index.html) is hosted separate from Advanced Identity Cloud documentation.

Integrate Ping SDKs with any of the following:

* [Android applications](https://docs.pingidentity.com/sdks/latest/sdks/tutorials/android-quickstart/index.html)

* [iOS applications](https://docs.pingidentity.com/sdks/latest/sdks/tutorials/ios/index.html)

* [JavaScript applications](https://docs.pingidentity.com/sdks/latest/sdks/tutorials/javascript/index.html)

## Upload provided files to integrate with Android or iOS apps

Associating a website(s) to your application is crucial when implementing Ping SDKs with Android or iOS applications. This allows you to share credentials or provide redirects within an application. Within the context of Ping SDKs, it is important to associate the SDKs with Android or iOS applications.

Google and Apple both provide ways assist in this process:

* [Android assetlinks.json](upload-android-assetlinks.html) - Establish trust between the application and a website(s) by automatically opening links for that domain.

* [iOS apple-app-site-association](upload-ios-apple-app-site-association.html) - Associate a website(s) with your application by having the associated domain file on your website and the appropriate entitlement in your application.

---

---
title: Upload an Android <code>assetlinks.json</code> file
description: Upload and manage an Android assetlinks.json file in Advanced Identity Cloud to establish trust between your Android apps and a custom domain
component: pingoneaic
page_id: pingoneaic:end-user:upload-android-assetlinks
canonical_url: https://docs.pingidentity.com/pingoneaic/end-user/upload-android-assetlinks.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Third-Party", "Integration", "Setup &amp; Configuration", "REST API", "Security"]
page_aliases: ["developer-docs:uploading-android-assetlinks.adoc", "developer-docs:upload-android-assetlinks.adoc"]
section_ids:
  high-level-process-android: High-level process
  view-an-assetlinks-json-file: View an assetlinks.json file
  upload-or-replace-an-assetlinks-json-file: Upload or replace an assetlinks.json file
  delete-an-assetlinks-json-file: Delete an assetlinks.json file
---

# Upload an Android `assetlinks.json` file

What is an Android `assetlinks.json` file?

An [Android assetlinks.json](https://developer.android.com/training/app-links/verify-android-applinks) file is a metadata file that lets your website [declare an association](https://developers.google.com/digital-asset-links/v1/getting-started) with your Android apps. By convention, it is accessed from your website using the endpoint `/.well-known/assetlinks.json`.

To help you integrate your Android apps with PingOne Advanced Identity Cloud, you can upload an `assetlinks.json` file to a tenant environment and access it through a custom domain associated with the environment. You can do this for each custom domain in your set of environments.

As the configuration in your upper environments is immutable, you can only modify the content of an `assetlinks.json` file in your development environment configuration. You must then promote any configuration changes to your upper environments.

|   |                                                                                                                                                                                      |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | Ensure you have set up a [custom domain](../realms/custom-domains.html#configure-a-custom-domain) for each environment and realm where you need to upload an `assetlinks.json` file. |

## High-level process

The high-level process to configure and promote an `assetlinks.json` file is as follows:

1. In your development environment, use the endpoint naming format `/openidm/config/fidc/assetlinks.<custom-domain-fqdn>` to set `assetlinks.json` content in your configuration with an association to a custom domain. For example, for the custom domain `id.mycompany.com`, use the endpoint `/openidm/config/fidc/assetlinks.id.mycompany.com`.

2. Promote the configuration to the upper environment that's configured to use the custom domain; for example, if your production environment is configured to use the custom domain, you will need to promote to your staging environment, and then promote again to your production environment.

3. Access the `assetlinks.json` file from your custom domain using the endpoint `/.well-known/assetlinks.json`; for example, for the custom domain `id.mycompany.com`, use the URL https\://id.mycompany.com/.well-known/assetlinks.json.

## View an `assetlinks.json` file

Use a custom domain to view an `assetlinks.json` file. You don't need to use an access token as the file is publicly accessible.

> **Collapse: Show request**
>
> ```bash
> $ curl \
> --request GET 'https://<custom-domain-fqdn>/.well-known/assetlinks.json'(1)
> ```

|       |                                                                                     |
| ----- | ----------------------------------------------------------------------------------- |
| **1** | Replace \<custom-domain-fqdn> with a custom domain, for example `id.mycompany.com`. |

> **Collapse: Show response**
>
> ```json
> {
>     "relation": [
>         "delegate_permission/common.handle_all_urls",
>         "delegate_permission/common.get_login_creds"
>     ],
>     "target": {
>         "namespace": "web",
>         "site": "https://id.mycompany.com"
>     }
> }
> ```

## Upload or replace an `assetlinks.json` file

1. Refer to the [High-level process](#high-level-process-android) for configuring and promoting an `assetlinks.json` file.

2. In your development environment:

   1. [Get an access token](../developer-docs/authenticate-to-rest-api-with-access-token.html#get_an_access_token).

   2. Set the `assetlinks.json` file contents in your configuration:

      > **Collapse: Show request**
      >
      > ```bash
      > $ curl \
      > --request PUT 'https://<tenant-env-fqdn>/openidm/config/fidc/assetlinks.<custom-domain-fqdn>' \(1) (2)
      > --header 'Authorization: Bearer <access-token>' \(3)
      > --header 'Content-Type: application/json' \
      > --data-raw '{(4)
      >   "data": [
      >     {
      >       "relation": [
      >         "delegate_permission/common.handle_all_urls",
      >         "delegate_permission/common.get_login_creds"
      >       ],
      >       "target": {
      >         "namespace": "web",
      >         "site": "https://id.mycompany.com"
      >       }
      >     }
      >   ]
      > }'
      > ```

      |       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
      | ----- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      | **1** | Replace \<tenant-env-fqdn> with the domain of your development environment; for example, `openam-mycompany.forgeblocks.com`.                                                                                                                                                                                                                                                                                                                                                                                                                        |
      | **2** | Replace \<custom-domain-fqdn> with the custom domain, for example `id.mycompany.com`.                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
      | **3** | Replace \<access-token> with the access token.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
      | **4** | Replace the example `assetlinks.json` JSON content with your own JSON content. Note that the JSON content is wrapped in a `data` object wrapper.> **Collapse: Show response**
      >
      > ```json
      > {
      >   "_id": "fidc/assetlinks.id.mycompany.com",
      >   "data": [
      >     {
      >       "relation": [
      >         "delegate_permission/common.handle_all_urls",
      >         "delegate_permission/common.get_login_creds"
      >       ],
      >       "target": {
      >         "namespace": "web",
      >         "site": "https://id.mycompany.com"
      >       }
      >     }
      >   ]
      > }
      > ``` |

   3. (Optional) Repeat the previous step for each additional custom domain that needs the `assetlinks.json` file uploading or replacing.

3. Run a series of promotions to add the development environment configuration to your upper environments. Learn more in:

   * [Manage self-service promotions using the API](../tenants/self-service-promotions-api.html)

   * [Manage self-service promotions using the admin console](../tenants/self-service-promotions-ui.html)

4. Use your custom domain to [view the assetlinks.json file](#view-an-assetlinks-json-file). If you uploaded or replaced additional `assetlinks.json` files, repeat this for each custom domain.

## Delete an `assetlinks.json` file

1. Refer to the [High-level process](#high-level-process-android) for configuring and promoting an `assetlinks.json` file.

2. In your development environment:

   1. [Get an access token](../developer-docs/authenticate-to-rest-api-with-access-token.html#get_an_access_token).

   2. Delete the `assetlinks.json` file contents from your configuration:

      > **Collapse: Show request**
      >
      > ```bash
      > $ curl \
      > --request DELETE 'https://<tenant-env-fqdn>/openidm/config/fidc/assetlinks.<custom-domain-fqdn>' \(1) (2)
      > --header 'Authorization: Bearer <access-token>'(3)
      > ```

      |       |                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
      | ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      | **1** | Replace \<tenant-env-fqdn> with the domain of your development environment, for example `openam-mycompany.forgeblocks.com`.                                                                                                                                                                                                                                                                                                                       |
      | **2** | Replace \<custom-domain-fqdn> with your custom domain, for example `id.mycompany.com`.                                                                                                                                                                                                                                                                                                                                                            |
      | **3** | Replace \<access-token> with the access token.> **Collapse: Show response**
      >
      > ```json
      > {
      >   "_id": "fidc/assetlinks.id.mycompany.com",
      >   "data": [
      >     {
      >       "relation": [
      >         "delegate_permission/common.handle_all_urls",
      >         "delegate_permission/common.get_login_creds"
      >       ],
      >       "target": {
      >         "namespace": "web",
      >         "site": "https://id.mycompany.com"
      >       }
      >     }
      >   ]
      > }
      > ``` |

   3. (Optional) Repeat the previous step for each additional custom domain that needs the `assetlinks.json` file deleting.

3. Run a series of promotions to add the development environment configuration to your upper environments. Learn more in:

   * [Manage self-service promotions using the API](../tenants/self-service-promotions-api.html)

   * [Manage self-service promotions using the admin console](../tenants/self-service-promotions-ui.html)

4. Use your custom domain to [view the assetlinks.json file](#view-an-assetlinks-json-file) and check that it is empty. If you deleted additional `assetlinks.json` files, repeat this for each custom domain.

---

---
title: Upload an iOS <code>apple-app-site-association</code> file
description: Upload and manage an iOS apple-app-site-association file in Advanced Identity Cloud to associate iOS apps with a custom domain for universal links
component: pingoneaic
page_id: pingoneaic:end-user:upload-ios-apple-app-site-association
canonical_url: https://docs.pingidentity.com/pingoneaic/end-user/upload-ios-apple-app-site-association.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Third-Party", "Integration", "Setup &amp; Configuration", "REST API", "Security"]
page_aliases: ["developer-docs:upload-ios-apple-app-site-association.adoc"]
section_ids:
  high-level-process-apple: High-level process
  view-an-apple-app-site-association-file: View an apple-app-site-association file
  upload-or-replace-an-apple-app-site-association-file: Upload or replace an apple-app-site-association file
  delete-an-apple-app-site-association-file: Delete an apple-app-site-association file
---

# Upload an iOS `apple-app-site-association` file

What is an iOS `apple-app-site-association` file?

An `apple-app-site-association` file is a metadata file that creates a secure association between your domain and your iOS apps. This lets you use universal links to open your iOS apps from your website. By convention, it is accessed from your website using the endpoint `/.well-known/apple-app-site-association`.

Learn more about creating and using a `apple-app-site-association` file in [Supporting associated domains](https://developer.apple.com/documentation/xcode/supporting-associated-domains).

To help you integrate your iOS apps with PingOne Advanced Identity Cloud, you can upload an `apple-app-site-association` file to a tenant environment and access it through a custom domain associated with the environment. You can do this for each custom domain in your set of environments.

As the configuration in your upper environments is immutable, you can only modify the content of an `apple-app-site-association` file in your development environment configuration. You must then promote any configuration changes to your upper environments.

|   |                                                                                                                                                                                                     |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Ensure you have set up a [custom domain](../realms/custom-domains.html#configure-a-custom-domain) for each environment and realm where you need to upload an iOS `apple-app-site-association` file. |

## High-level process

The high-level process to configure and promote an `apple-app-site-association` file is as follows:

1. In your development environment, use the endpoint naming format `/openidm/config/fidc/apple-app-site-association.<custom-domain-fqdn>` to set `apple-app-site-association` content in your configuration with an association to a custom domain; for example, for the custom domain `id.mycompany.com`, use the endpoint `/openidm/config/fidc/apple-app-site-association.id.mycompany.com`.

2. Promote the configuration to the upper environment that's configured to use the custom domain. For example, if your production environment is configured to use the custom domain, you will need to promote to your staging environment, and then promote again to your production environment.

3. Access the `apple-app-site-association` file from your custom domain using the endpoint `/.well-known/apple-app-site-association`; for example, for the custom domain `id.mycompany.com`, use the URL https\://id.mycompany.com/.well-known/apple-app-site-association.

## View an `apple-app-site-association` file

Use a custom domain to view an `apple-app-site-association` file. You don't need to use an access token as the file is publicly accessible.

1. View the `apple-app-site-association` file using a `GET` request:

   > **Collapse: Show request**
   >
   > ```bash
   > $ curl \
   > --request GET 'https://<custom-domain-fqdn>/.well-known/apple-app-site-association'(1)
   > ```

   |       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
   | ----- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | **1** | Replace \<custom-domain-fqdn> with your custom domain; for example, `id.mycompany.com`.> **Collapse: Show response**
   >
   > ```json
   > {
   >   "applinks": {
   >     "details": [
   >       {
   >         "appIDs": [
   >           "XXXXXXXXXX.com.example.AppName"
   >         ],
   >         "components": [
   >           {
   >             "/": "/reset/*",
   >             "comment": "Success after reset password journey"
   >           }
   >         ]
   >       }
   >     ]
   >   },
   >   "webcredentials": {
   >     "apps": [
   >       "XXXXXXXXXX.com.example.AppName"
   >     ]
   >   }
   > }
   > ``` |

## Upload or replace an `apple-app-site-association` file

1. Refer to the [High-level process](#high-level-process-apple) for configuring and promoting an `apple-app-site-association` file.

2. In your development environment:

   1. [Get an access token](../developer-docs/authenticate-to-rest-api-with-access-token.html#get_an_access_token).

   2. Set the `apple-app-site-association` file contents in your configuration:

      > **Collapse: Show request**
      >
      > ```bash
      > $ curl \
      > --request PUT 'https://<tenant-env-fqdn>/openidm/config/fidc/apple-app-site-association.<custom-domain-fqdn>' \(1) (2)
      > --header 'Authorization: Bearer <access-token>' \(3)
      > --header 'Content-Type: application/json' \
      > --data-raw '{(4)
      >   "data": {
      >     "applinks": {
      >       "details": [
      >         {
      >           "appIDs": [
      >             "XXXXXXXXXX.com.example.AppName"
      >           ],
      >           "components": [
      >             {
      >               "/": "/reset/*",
      >               "comment": "Success after reset password journey"
      >             }
      >           ]
      >         }
      >       ]
      >     },
      >     "webcredentials": {
      >       "apps": [
      >         "XXXXXXXXXX.com.example.AppName"
      >       ]
      >     }
      >   }
      > }'
      > ```

      |       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
      | ----- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      | **1** | Replace \<tenant-env-fqdn> with the domain of your development environment; for example, `openam-mycompany.forgeblocks.com`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
      | **2** | Replace \<custom-domain-fqdn> with your custom domain; for example, `id.mycompany.com`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
      | **3** | Replace \<access-token> with your access token.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
      | **4** | Replace the example `apple-app-site-association` JSON content with your own JSON content.> **Collapse: Show response**
      >
      > ```json
      > {
      >   "_id": "fidc/apple-app-site-association.id.mycompany.com",
      >   "data": {
      >     "applinks": {
      >       "details": [
      >         {
      >           "appIDs": [
      >             "XXXXXXXXXX.com.example.AppName"
      >           ],
      >           "components": [
      >             {
      >               "/": "/reset/*",
      >               "comment": "Success after reset password journey"
      >             }
      >           ]
      >         }
      >       ]
      >     },
      >     "webcredentials": {
      >       "apps": [
      >         "XXXXXXXXXX.com.example.AppName"
      >       ]
      >     }
      >   }
      > }
      > ``` |

   3. (Optional) Repeat the previous step for each additional custom domain that needs the `apple-app-site-association` file uploading or replacing.

3. Run a series of promotions to add the development environment configuration to your upper environments. Learn more in:

   * [Manage self-service promotions using the API](../tenants/self-service-promotions-api.html)

   * [Manage self-service promotions using the admin console](../tenants/self-service-promotions-ui.html)

4. Use your custom domain to [view the apple-app-site-association file](#view-an-apple-app-site-association-file). If you uploaded or replaced additional `apple-app-site-association` files, repeat this for each custom domain.

## Delete an `apple-app-site-association` file

1. Refer to the [High-level process](#high-level-process-apple) for configuring and promoting an `apple-app-site-association` file.

2. In your development environment:

   1. [Get an access token](../developer-docs/authenticate-to-rest-api-with-access-token.html#get_an_access_token).

   2. Delete the `apple-app-site-association` file contents from your configuration:

      > **Collapse: Show request**
      >
      > ```bash
      > curl \
      > --request DELETE 'https://<tenant-env-fqdn>/openidm/config/fidc/apple-app-site-association.<custom-domain-fqdn>' \(1) (2)
      > --header 'Authorization: Bearer <access-token>'(3)
      > ```

      |       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
      | ----- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      | **1** | Replace \<tenant-env-fqdn> with the domain of your development environment, for example `openam-mycompany.forgeblocks.com`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
      | **2** | Replace \<custom-domain-fqdn> with your custom domain, for example `id.mycompany.com`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
      | **3** | Replace \<access-token> with the access token.> **Collapse: Show response**
      >
      > ```json
      > {
      >   "_id": "fidc/apple-app-site-association.id.mycompany.com",
      >   "data": {
      >     "applinks": {
      >       "details": [
      >         {
      >           "appIDs": [
      >             "XXXXXXXXXX.com.example.AppName"
      >           ],
      >           "components": [
      >             {
      >               "/": "/reset/*",
      >               "comment": "Success after reset password journey"
      >             }
      >           ]
      >         }
      >       ]
      >     },
      >     "webcredentials": {
      >       "apps": [
      >         "XXXXXXXXXX.com.example.AppName"
      >       ]
      >     }
      >   }
      > }
      > ``` |

   3. (Optional) Repeat the previous step for each additional custom domain that needs the `apple-app-site-association` file deleting.

3. Run a series of promotions to add the development environment configuration to your upper environments. Learn more in:

   * [Manage self-service promotions using the API](../tenants/self-service-promotions-api.html)

   * [Manage self-service promotions using the admin console](../tenants/self-service-promotions-ui.html)

4. Use your custom domain to [view the apple-app-site-association file](#view-an-apple-app-site-association-file) and check that it is empty. If you deleted additional `apple-app-site-association` files, repeat this for each custom domain.

---

---
title: User self-service journeys
description: Configure Advanced Identity Cloud user self-service journeys for password reset, username recovery, self-registration, social authentication, and progressive profile
component: pingoneaic
page_id: pingoneaic:end-user:admin-config-overview
canonical_url: https://docs.pingidentity.com/pingoneaic/end-user/admin-config-overview.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["User Self-Service", "Username Recovery", "Password Reset", "Update Passwords", "Registration", "Progressive Profile", "Passthrough Authentication"]
section_ids:
  use_cases_for_user_self_service: Use cases for user self-service
---

# User self-service journeys

You must configure user self-service journeys in PingOne Advanced Identity Cloud before your end users can experience them. For example, you can configure journeys for password reset, username retrieval, and more.

## Use cases for user self-service

To let end users manage their own accounts in Advanced Identity Cloud, you must configure the necessary settings. For example, if you want users to create their own identities by registering themselves with Advanced Identity Cloud, you need to create a journey that collects the required information. After creating the journey, you must test it and push the journey's configuration to your production tenant.

The features end users can access depend on what you configure.

The following table references the self-service actions available to end users in Advanced Identity Cloud, provided they are configured. You can configure these self-service journeys:

| Use Case                                                                                           | Description                                                                                |
| -------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------ |
| [Simple sign-on](../self-service/login.html)                                                       | Lets end users sign on by collecting a username and password.                              |
| [Username recovery](../self-service/username-recovery.html)                                        | Lets end users recover their username.                                                     |
| [Password reset](../self-service/password-reset.html)                                              | Lets end users reset their password.                                                       |
| [Password update](../self-service/update-password.html)                                            | Lets end users update their password, after signing on and obtaining a session.            |
| [User self-registration](../self-service/self-registration.html)                                   | Lets end users register their own identity in Advanced Identity Cloud.                     |
| [Social authentication](../self-service/social-registration.html)                                  | Lets end users authenticate using social providers, such as Google or Facebook.            |
| [Progressive profile](../self-service/progressive-profile.html)                                    | Asks users for more information based on a login count.                                    |
| [Replace lost second-factor authentication devices](../use-cases/use-case-lost-second-factor.html) | Creates a journey to let end users sign on with a recovery code if they lose their device. |

For further use cases and questions about configuring the hosted account pages, learn more in [FAQ: Advanced Identity Cloud hosted End User UI](https://support.pingidentity.com/s/article/FAQ-Advanced-Identity-Cloud-hosted-End-User-UI).