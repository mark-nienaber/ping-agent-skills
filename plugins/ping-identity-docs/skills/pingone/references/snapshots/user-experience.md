---
title: Adding a custom key for DaVinci
description: Create custom key-value pairs that provide translatable text for various user-facing pages in PingOne DaVinci.
component: pingone
page_id: pingone:user_experience:p1_adding_custom_key_davinci
canonical_url: https://docs.pingidentity.com/pingone/user_experience/p1_adding_custom_key_davinci.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: Ocobter 9, 2024
section_ids:
  steps: Steps
---

# Adding a custom key for DaVinci

In addition to the Ping Identity-provided default **Standard Fields**, you can create custom key-value pairs that provide translatable text for various user-facing pages in DaVinci. The addition of custom keys is only available for the English language.

To add a custom key:

## Steps

1. In the PingOne admin console, go to **User Experience > Languages**.

2. Enable the languages for which you want to add localized content.

3. Click **English (en)** to open the details panel so that you can add the necessary custom keys.

4. In the **Module** list, select the module to view the associated keys.

   |   |                                                                                                                                              |
   | - | -------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | When modifying keys for the module, both forms configured using PingOne **Forms** and custom HTML-based forms can use the translatable text. |

   ![The English module.](_images/p1-languages-english-module.png)

5. In the **Page** list, select the **Custom Messages** page to view the associated keys.

6. Click **[icon: plus, set=fa]Add Custom Key**.

7. Select the **Component Type**.

   ![The Add Custom Key module.](_images/p1-languages-custom-key.png)

8. Change the generated unique **Key** value.

   |   |                                                                                                                                                                                                                           |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | * The key must start with a `forms.` prefix and can only contain letters, numbers, dashes, underscores, or dots.

   * The maximum number of key-value pairs for the DaVinci **Custom Messages** section is limited to 2000. |

9. Add a **Default Translation** in English.

   |   |                                                                  |
   | - | ---------------------------------------------------------------- |
   |   | The **Default Translation** cannot be more than 1024 characters. |

10. Click **Save**.

---

---
title: Adding a language
description: Use the Languages page to add a language to your PingOne environment.
component: pingone
page_id: pingone:user_experience:p1_add_a_language
canonical_url: https://docs.pingidentity.com/pingone/user_experience/p1_add_a_language.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: November 8, 2023
page_aliases: ["p1_enable_a_language.adoc"]
section_ids:
  steps: Steps
  next-steps: Next steps
---

# Adding a language

Use the **Languages** page to add a language to your PingOne environment.

## Steps

1. In the PingOne admin console, go to **User Experience > Languages** and click the **[icon: plus, set=fa]**icon.

2. In the **Add Language** panel, select a language in the list by browsing or searching for it.

   |   |                                                                                                                                                                                  |
   | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | You can select a generic language, such as **English (en)** or a language-locale pair, such as **English (United States) (en-US)**. The languages in the list are preconfigured. |

3. Click **Save Changes**.

4. In the **User Experience > Languages** list, click the language details page.

5. To enable the language, click the toggle at the top of the language details page to the right (blue).

   |   |                                                                         |
   | - | ----------------------------------------------------------------------- |
   |   | You can disable the language by clicking the toggle to the left (gray). |

## Next steps

[Configure localized content](p1_configure_localized_content.html).

---

---
title: Adding a language to an agreement
description: After you've created an agreement, add localized content to the agreement. If the content has already been added to the agreement, you can skip this step. One agreement can consist of multiple language versions of the agreement.
component: pingone
page_id: pingone:user_experience:p1_add_language_to_an_agreement
canonical_url: https://docs.pingidentity.com/pingone/user_experience/p1_add_language_to_an_agreement.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: November 8, 2023
section_ids:
  steps: Steps
  result: Result:
  next-steps: Next steps
---

# Adding a language to an agreement

After you've created an agreement, add localized content to the agreement. If the content has already been added to the agreement, you can skip this step. One agreement can consist of multiple language versions of the agreement.

## Steps

1. In the PingOne admin console, go to **User Experience > Agreements**.

2. In the **Agreements** list, locate the agreement you want to edit. Click the agreement entry to open the details panel.

3. On the **Overview** tab, click the **Edit Localized Content** button.

4. For **Languages**, click the **[icon: plus, set=fa]**button. Learn more in [Languages](p1_languages.html).

5. For **Language**, select the language that the agreement will use.

6. Click **Save**.

   ### Result:

   The language is added to the configured languages for the agreement.

## Next steps

[Creating localized content](p1_create_localized_content.html)

---

---
title: Adding a notification template
description: Add a notification template in PingOne.
component: pingone
page_id: pingone:user_experience:p1_add_notification
canonical_url: https://docs.pingidentity.com/pingone/user_experience/p1_add_notification.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: November 8, 2023
section_ids:
  steps: Steps
  result: Result
  next-steps: Next steps
---

# Adding a notification template

To add a notification template, you'll select a default notification template and customize it to meet the needs of your organization. New notifications are based on a default notification type.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | * The templates that are created to be used in DaVinci are customizable.

* To protect the email reputation scores for all of our customers, PingOne trial licensees can't use the built-in PingOne email domain (`@pingone.com`) to send email notifications with customized content. Paid licensees can customize the content, and Trial licensees can create custom email notification content when using their own SMTP server or custom email domains. Learn more in [Setting up a trusted email domain](../settings/p1_set_up_trusted_email_domain.html) and [Configuring a custom SMTP email notification server](../settings/p1_configure_custom_smtp_server.html).

* You must have the Environment Admin role to add and edit notification templates. |

## Steps

1. In the PingOne admin console, go to **User Experience > Notification Templates**.

2. Click **[icon: plus, set=fa]**.

3. In the **Add Notification** modal, enter the following:

   1. **Type**: Select the purpose of the notification template.

      * **Account Created**

        |   |                                                                                                                        |
        | - | ---------------------------------------------------------------------------------------------------------------------- |
        |   | The **Account Created** notification template is used only for accounts created as a result of a PingOne DaVinci flow. |

      * **Credential Issued**

      * **Credential Revoked**

      * **Credential Updated**

      * **Device Pairing**

      * **Digital Wallet Pairing**

      * **Email Address Verification (Admin)**

      * **Email Address Verification (User)**

      * **General**

      * **Invite (Admin)**

      * **New Device Paired**

      * **Password Recovery**

      * **PingOne Verify Email Address and Phone Number Verification**

      * **PingOne Verify ID Verification**

      * **Strong Authentication**

      * **Transaction**

      * **Verification Code**

        You can find more information about each notification type in [Notification Templates](p1_notifications.html).

   2. **Name** (optional): A unique identifier for the notification template. The name appears in the notification template list to help administrators choose the appropriate template.

4. Click **Create**.

## Result

The notification template is added to the notification templates list.

## Next steps

Edit the notification template as needed. Learn more in [Editing a notification template](p1_edit_notification.html).

---

---
title: Adding a theme
description: Use the Branding and Themes page to add a theme to the current PingOne environment.
component: pingone
page_id: pingone:user_experience:p1_add_theme
canonical_url: https://docs.pingidentity.com/pingone/user_experience/p1_add_theme.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: April 11, 2025
section_ids:
  steps: Steps
  next-steps: Next steps
---

# Adding a theme

PingOne delivers several built-in themes. Use the **Branding and Themes** page to add a theme to the current environment. The new theme uses your **Company Name** and **Logo** if you added them in **Global Settings**. Learn more in [Editing environment branding](p1_edit_environment_branding.html).

## Steps

1. In the PingOne admin console, go to **User Experience > Branding and Themes**.

2. Click the **[icon: plus, set=fa]**icon.

3. On the **Choose a Base Theme** page, click the theme you want to start with.

   |   |                                                                                                                                                                                                                                                   |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | When you select a base theme, PingOne generates a unique name for the new version. For example, if you select the **Focus** theme as your base theme, your new theme is named **Focus 1** by default. You can edit this name before you continue. |

4. Click **Next** and select the tabs on the **Customize** page to change settings for the different page types.

   Page previews display in the left panel, and you configure settings in the **Theme Styles** panel on the right. The previews update in real time as you make changes to the settings. To switch between previews for desktop or mobile devices, click the **Desktop** or **Mobile** icon (![p1 branding themes desktop mobile icon](_images/p1-branding-themes-desktop-mobile-icon.png)).

   ![A screen capture of the Customize theme page showing the Theme Styles panel with Global and Component Specific tabs.](_images/p1-add-theme-with-settings-panel.png)

   |   |                                                                                                                                                                                         |
   | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | All page types include global theme settings, which apply across all components. Some page types also have **Component Specific** settings, which apply only to the specific component. |

5. Click the **All** tab to edit global theme settings that apply to all pages that aren't affected by component-specific styles.

   | Setting        | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
   | -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
   | **Logo**       | An image to represent the environment. Hover over the box and click the **Camera** icon ([icon: camera, set=fa]) to upload an image. Select an image in `.jpg`, `.jpeg`, `.gif`, or `.png` format up to 2 MB in size.To change the image used for the logo, click [icon: camera, set=fa]and select **Upload New Image**.To delete a logo from a theme, click [icon: camera, set=fa]and select **Remove Image**.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
   | **Footer**     | Text that appears at the bottom of each page.1) Click the toggle to the right (blue) to enable footer text, then enter the text.

   2) Click **+ Add Footer**, and select **PlainText** or **HTML**.

      By default, **English** is selected in the **Language** list. Before you can create footers in other languages, you must create and save one in English. Languages with footers are marked with a green dot and move to the top of the list.

   3) Enter text in the **Footer Content** field.

      If you selected **HTML** for your footer type, you can include the following HTML elements and associated attributes in your footer. All elements support the `class` and `style` attributes.

      * `a(href, target)`

        &#xA;&#xA;To use an href, you must include the protocol in the address, such as ftp, http, https, mailto, tel, or sms.

      * `b`

      * `blockquote(cite)`

      * `br`

      * `cite`

      * `code`

      * `dd`

      * `dl`

      * `dt`

      * `em`

      * `h1`

      * `h2`

      * `h3`

      * `hr`

      * `i`

      * `img(src, srcset, alt, title, width, height)`

      * `li`

      * `ol`

      * `p`

      * `pre`

      * `q(cite)`

      * `small`

      * `span`

      * `strike`

      * `strong`

      * `sub`

      * `sup`

      * `u`

      * `ul`

   4) Click **Save**.

   5) To add footers in additional languages, click the **Pencil** icon ([icon: pencil, set=fa]), select a different language, and add your translated text.

      &#xA;&#xA;You can't mix footer types. All footers must be either plain text or HTML, depending on what you selected in step 2.

   6) Click **Save**. |
   | **Button**     | Configure the color of the buttons, such as the **Sign on** and **Save** buttons:- **Button Fill**: The background color for the buttons.

   - **Button Text**: The color of the text on the buttons.

   - **Link Text**: The color of the text for links displayed on the buttons.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
   | **Text**       | The color of the text on the pages:- **Heading Text**: The color of the text in headings.

   - **Body Text**: The color of non-heading text.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
   | **Background** | The background to use on each page.- **None**: Do not use a background.

   - **Image**: To use an image for the background, hover over the box and click the **Camera** icon ([icon: camera, set=fa]) to upload an image. Select an image in `jpg`, `jpeg`, `gif`, or `png` format up to 2 MB in size.

     To change the image used for the background, click [icon: camera, set=fa]and select **Upload New Image**.

     To delete a background image from a theme, click [icon: camera, set=fa]and select **Remove Image**.

   - **Color**: Select a color to use for the background.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
   | **Card Color** | The color of the box around form fields.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |

6. On the **Forms** tab, click one of the tabs in the **Theme Styles** panel:

   * **Global**: Edit global theme settings and preview the updated appearance of your PingOne DaVinci forms.

   * **Component Specific**: Edit settings that only affect the appearance of your forms.

     ![A screenshot of the Edit theme page showing the Forms tab selected with the Component Specific tab in focus.](_images/p1-branding-themes-forms-component-settings.png)

     |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
     | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
     |   | Your environment must include PingOne DaVinci and at least one DaVinci form to configure theme styles for forms.Your selections affect all forms in the environment, and can't be set at the form level. You can select a form from the **Form Preview** list to preview it with theme styling applied. You can also click **Edit Form** to open the **Forms** page in a separate tab and make updates the your forms as necessary.Learn more in [DaVinci Forms](p1_forms.html). |

     * General

       Use these settings to change the appearance of general elements in your forms.

       ![A screenshot image with callouts to where the setting applies in the form.](_images/p1-branding-themes-forms-general.png)

       | Setting             | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
       | ------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
       | **Header** (1)      | Text that appears at the top of each form page.To add headers:1) Click the toggle to the right (blue) to enable header text.

       2) Click **+ Add Header**, and select **PlainText** or **HTML**.

          By default, **English** is selected in the **Language** list. Before you can create headers in other languages, you must create and save one in English. Languages with headers are marked with a green dot and move to the top of the list.

       3) Enter text in the **Header Content** field.

          If you selected **HTML** for your header type, you can include the following HTML elements and associated attributes in your header. All elements support the `class` and `style` attributes.

          * `a(href, target)`

            &#xA;&#xA;To use an href, you must include the protocol in the address, such as ftp, http, https, mailto, tel, or sms.

          * `b`

          * `blockquote(cite)`

          * `br`

          * `cite`

          * `code`

          * `dd`

          * `dl`

          * `dt`

          * `em`

          * `h1`

          * `h2`

          * `h3`

          * `hr`

          * `i`

          * `img(src, srcset, alt, title, width, height)`

          * `li`

          * `ol`

          * `p`

          * `pre`

          * `q(cite)`

          * `small`

          * `span`

          * `strike`

          * `strong`

          * `sub`

          * `sup`

          * `u`

          * `ul`

       4) Click **Save**.

       5) To add headers in additional languages, click [icon: pencil, set=fa], select a different language, and add your translated text.

          &#xA;&#xA;You can't mix header types. All headers must be either plain text or HTML, depending on what you selected in step 2.

       6) Click **Save**. |
       | **Global Font** (2) | The font to use for all form text, including field labels and button text.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
       | **Logo Height** (3) | Set a height for your form logo. The maximum allowed height is 150 px.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
       | **Focus Color**     | Select an outline color to apply to a field when it's in focus.&#xA;&#xA;This setting can't be previewed because it requires user interaction to display.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |

     * Buttons

       Use these settings to change the appearance of buttons in your forms.

       ![A screen capture of a form preview with callouts to show what each button setting applies to.](_images/p1-branding-themes-forms-buttons.png)

       | Setting                         | Description                                                                                                                                                                            |
       | ------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
       | **Button Border** (1)           | Select a color for the borders around the form buttons.                                                                                                                                |
       | **Hover State Fill** (2)        | Select a button color to use when a user hovers over them.&#xA;&#xA;This setting can't be previewed because it requires user interaction to display.                                   |
       | **Hover State Border** (1)      | Select a color the borders of the buttons in your forms become when a user hovers over them.&#xA;&#xA;This setting can't be previewed because it requires user interaction to display. |
       | **Hover State Button Text** (3) | Select a color that the button text becomes when a user hovers over form buttons.&#xA;&#xA;This setting can't be previewed because it requires user interaction to display.            |
       | **Border Weight** (1)           | Select a setting for the thickness of the borders around the form buttons. Allowed values range from 0 px (no border) to 4 px.                                                         |
       | **Corner Radius** (4)           | Select a value between 0 (square) and 25 px to configure the curvature of the button corners.                                                                                          |
       | **Text Size** (3)               | Select a font size between 8 and 24 px for the button text in your forms.                                                                                                              |
       | **Text Weight** (3)             | Select a weight for the button text. For example, **Extra Light** or **Bold**.                                                                                                         |

     * Text

       Use these settings to change the appearance of specific text types in your forms.

       |   |                                                                                                                                                                                                                                                                                                                                                                |
       | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
       |   | If text formatting options were set for a particular form using the **Rich Text** component in the form builder, those text settings can't be changed using the theme settings, and the preview won't update for that form. If there were no text format changes to other forms in your environment, the theme settings are used and displayed in the preview. |

       ![A screen capture of a form preview with callouts to show what each text setting applies to.](_images/p1-branding-themes-forms-text.png)

       | Setting               | Description                                                                                                                                                                                                                                                                                                                           |
       | --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
       | **Title Text** (1)    | Select the size and weight of the title text (H1) in your forms.- **Text Size**: Select a font size between 8 and 24 px for form titles.

       - **Text Weight**: Select a weight for the title text. For example, **Extra Light** or **Bold**.                                                                                            |
       | **Subtitle Text** (2) | Select the size, weight, and color of the subtitle text (H2) in your forms.- **Text Size**: Select a font size between 8 and 24 px for form subtitles.

       - **Text Weight**: Select a weight for the subtitle text. For example, **Extra Light** or **Bold**.

       - **Subtitle Text**: Select a color for the subtitle text in your forms. |
       | **Body Text** (3)     | Select the size and weight of the main body text in your forms.- **Text Size**: Select a font size between 8 and 24 px for body text.

       - **Text Weight**: Select a weight for the body text. For example, **Extra Light** or **Bold**.                                                                                                |
       | **Link Text** (4)     | Select the size, weight, and hover color for the links in your forms.- **Text Size**: Select a font size between 8 and 24 px for link text.

       - **Text Weight**: Select a weight for the link text. For example, **Extra Light** or **Bold**.

       - **Link Text Hover**: The color of the text when a user hovers over the link.          |

     * Input Fields

       Use these settings to change the appearance of form fields that require user input.

       ![A screen capture of a form preview with callouts to show what each input field setting applies to.](_images/p1-branding-themes-forms-inputfields.png)

       | Setting           | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
       | ----------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
       | **Label** (1)     | Select the size, weight, and color of the label text for input fields in your forms.- **Text Size**: Select a font size between 8 and 24 px for field labels.

       - **Text Weight**: Select a weight for the field label text. For example, **Extra Light** or **Bold**.

       - **Label Text**: Select a color for the label text for fields.                                                                                                                                                                                                                                                                                                               |
       | **Value** (1)     | Select the size, weight, and color of the text entered by users in the input fields in your forms.- **Text Size**: Select a font size between 8 and 24 px for text entered by users.

       - **Text Weight**: Select a weight for the text entered by users. For example, **Extra Light** or **Bold**.

       - **Value Text**: Select a color for the user-entered text.&#xA;&#xA;These settings can't be previewed because they require user interaction to display.                                                                                                                                                                                          |
       | **Input Box** (2) | Select the border color, border weight, corner radius, and label position for input fields in your forms.- **Border** (2a): Select a color for the border around input fields.

       - **Border Weight** (2a): Select a setting for the thickness of the borders around the input fields. Allowed values range from 0 px (no border) to 4 px.

       - **Corner Radius** (2b): Select a value between 0 (square) and 25 px to configure the curvature of the input field corners.

       - **Label Position** (2c): Select one of the following options:

         * **Float**: Place the label inside the input box.

         * **Default**: Place the label above the input box. |

     * Card

       Use these settings to change the appearance of the card that contains all of the form elements.

       ![A screen capture of a form preview with callouts to show what each card setting applies to.](_images/p1-branding-themes-forms-card.png)

       | Setting                      | Description                                                                                                                                                               |
       | ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
       | **Border** (1)               | Select a color for the border around the card that contains all of the form elements.                                                                                     |
       | **Border Weight** (1)        | Select a setting for the thickness of the borders around the form card. Allowed values range from 0 px (no border) to 4 px.                                               |
       | **Corner Radius** (2)        | Select a value between 0 (square) and 25 px to configure the curvature of the card corners.                                                                               |
       | **Shadow** (3)               | Apply a shadow outline to the card.&#xA;&#xA;If you're using a background image, the shadow might not display clearly, particularly if the background image is very dark. |
       | **Horizontal Alignment** (4) | Select whether the card should be aligned to the left, right, or center of the form.                                                                                      |
       | **Vertical Alignment** (5)   | Select whether the card should be aligned to the top, bottom, or center of the form.                                                                                      |

7. On the **Verify** tab, click one of the tabs in the **Theme Styles** panel:

   * **Global**: Edit global theme settings and preview the updated appearance of identity verification pages.

   * **Component Specific**: Edit settings that only affect the appearance of the images on identity verification pages.

     ![Identity verification image with numbered callouts to indicate what each setting affects.](_images/p1-themes-verify-settings.png)

     | Setting                      | Description                                                                                                          |
     | ---------------------------- | -------------------------------------------------------------------------------------------------------------------- |
     | **Foreground Main** (1)      | The color used for the border around the front image and around the internal shapes in the front image.              |
     | **Foreground Highlight** (2) | The fill color used for the front image.                                                                             |
     | **Background Outline** (3)   | The color used for the borders around the background images and around the internal shapes in the background images. |

8. On the **End User Application** tab, click one of the tabs in the **Theme Styles** panel:

   * **Global**: Edit global theme settings and preview the updated appearance of system applications, such as the **Application Portal** and **Self-Service - My Account**.

   * **Component Specific**: Edit settings that only affect the appearance of system applications, such as the **Application Portal** and **Self-Service - My Account**.

     | Setting              | Description                                    |
     | -------------------- | ---------------------------------------------- |
     | **Background Color** | The background color used for the application. |

9. Click the **Authentication Policy** tab to edit global theme settings and preview the updated appearance of the sign-on and registration pages in your environment.

   |   |                                                                       |
   | - | --------------------------------------------------------------------- |
   |   | There are no component-specific styles for **Authentication Policy**. |

10. Click **Save**.

    The theme is added to the list on the **Branding and Themes** page.

    |   |                                                                                                     |
    | - | --------------------------------------------------------------------------------------------------- |
    |   | You can also customize an existing theme. Learn more in [Editing a theme](p1_customize_theme.html). |

## Next steps

[Selecting an active theme](p1_select_theme.html)

---

---
title: Adding an agreement
description: Use the Agreements page to create a new agreement. You can use agreements to prompt your users to consent to various policies. Learn more in Authentication policies.
component: pingone
page_id: pingone:user_experience:p1_add_an_agreement
canonical_url: https://docs.pingidentity.com/pingone/user_experience/p1_add_an_agreement.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: November 8, 2023
section_ids:
  steps: Steps
  result: Result
  next-steps: Next steps
---

# Adding an agreement

Use the **Agreements** page to create a new agreement. You can use agreements to prompt your users to consent to various policies. Learn more in [Authentication policies](../authentication/p1_authenticationpolicies.html).

## Steps

1. In the PingOne admin console, go to **User Experience > Agreements**.

2. Click the **[icon: plus, set=fa]**icon.

3. Enter the following information:

   * **Name**: A unique identifier for the agreement.

   * **Description** (optional): A brief characterization of the agreement.

   * **Reconsent every**: Specify the duration of the agreement consent, that is, how often the user will have to reconsent to the agreement. Select **Never**, or select **Number of days** and enter a value.

4. Click **Save**.

## Result

The agreement is created and added to the **Agreements** list.

## Next steps

[Adding a language to an agreement](p1_add_language_to_an_agreement.html)

---

---
title: Adding the agreement to the authentication policy
description: To start gathering consents from end users, add the agreement to the appropriate authentication policy.
component: pingone
page_id: pingone:user_experience:p1_add_agreement_to_authentication_policy
canonical_url: https://docs.pingidentity.com/pingone/user_experience/p1_add_agreement_to_authentication_policy.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: November 8, 2023
section_ids:
  steps: Steps
---

# Adding the agreement to the authentication policy

To start gathering consents from end users, add the agreement to the appropriate authentication policy.

## Steps

1. In the PingOne admin console, go to **Authentication > Authentication**.

2. Open the authentication policy you want to add the agreement to.

3. Click the **[icon: pencil, set=fa]**icon to open the policy in edit mode.

4. Click **[icon: plus, set=fa]Add step**.

5. Select **Terms of service prompt**.

6. For **Terms of service agreement**, select the appropriate agreement. If the expected agreement isn't shown, it might not have been added. Learn more in [Adding an agreement](p1_add_an_agreement.html).

7. To see the agreement as it will appear to end users, click **Preview**.

8. Click **Save**.

---

---
title: Agreements
description: You can require end users to consent to an agreement that is part of a sign-on policy in PingOne.
component: pingone
page_id: pingone:user_experience:p1_agreements
canonical_url: https://docs.pingidentity.com/pingone/user_experience/p1_agreements.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 17, 2024
---

# Agreements

You can require end users to consent to an agreement that is part of a sign-on policy.

Whether to require consent is based on configuration settings and the user's consent history. If the user doesn't have any consents for any of the configured agreements, then PingOne will require the user to consent. End users can see their most recent consent in the self-service application. Administrators can use auditing to see a history of the consents that the end user has accepted. Learn more in [Auditing for agreement consents](p1_audit_agreements.html).

You can configure an agreement for each language and locale. If there's no exact match, then PingOne defaults to the general language (without locale). If there is no language match, then PingOne uses the default language for the environment. You can find more information on adding languages in [Languages](p1_languages.html).

For the localized agreement text, you can use any UTF-8 characters up to a maximum of 32,000 characters.

---

---
title: Auditing for agreement consents
description: You can run an audit report to see more information about agreements, such as when an agreement was accepted or revoked. You can also use the User details page to see a user's consent history. Learn more in Viewing the consent history for a specific user.
component: pingone
page_id: pingone:user_experience:p1_audit_agreements
canonical_url: https://docs.pingidentity.com/pingone/user_experience/p1_audit_agreements.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: November 8, 2023
section_ids:
  steps: Steps
---

# Auditing for agreement consents

You can run an audit report to see more information about agreements, such as when an agreement was accepted or revoked. You can also use the **User details** page to see a user's consent history. Learn more in [Viewing the consent history for a specific user](p1_view_consent_history.html).

## Steps

1. In the PingOne admin console, go to **Monitoring > Audit**.

2. For **Time range**, enter the appropriate time span for the report.

3. For **Filter type**, select **Event type**.

4. For **Filter**, select one or more of the following. You can search or browse for event types.

   * **Agreement accepted**: An agreement was accepted by the end user.

   * **Agreement revoked**: An agreement was revoked by the end user.

5. To limit the report to a particular user, use a secondary filter with `User Name` or `User ID`.

6. Click **Run**.

---

---
title: Branding and Themes
description: "Use the Branding and Themes page in PingOne to quickly define a set of colors and images to best match your company's branding."
component: pingone
page_id: pingone:user_experience:p1_branding_themes
canonical_url: https://docs.pingidentity.com/pingone/user_experience/p1_branding_themes.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: April 23, 2025
section_ids:
  learn-more: Learn more
---

# Branding and Themes

Use branding themes to quickly define a set of colors and images to best match your company's branding and easily change the look of standard authentication policy forms, the application portal, the self-service portal, PingOne forms, and identity verification pages for a particular environment.

## Learn more

* [Viewing a list of available themes](p1_view_themes.html)

* [Previewing a theme](p1_preview_theme.html)

* [Editing environment branding](p1_edit_environment_branding.html)

* [Adding a theme](p1_add_theme.html)

* [Editing a theme](p1_customize_theme.html)

* [Upgrading legacy themes](p1_themes_upgrading.html)

* [Cloning a theme](p1_themes_cloning.html)

* [Selecting an active theme](p1_select_theme.html)

* [Deleting a theme](p1_delete_theme.html)

---

---
title: Changing the default language
description: Use the Languages page in PingOne to change the default language.
component: pingone
page_id: pingone:user_experience:p1_change_default_language
canonical_url: https://docs.pingidentity.com/pingone/user_experience/p1_change_default_language.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: November 8, 2023
section_ids:
  steps: Steps
---

# Changing the default language

Use the **Languages** page to change the default language.

The default language is the language that most users of your applications will see when they receive a notification or agreement.

|   |                                                                                                                                                                                               |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | To set a language as the default language, it must be enabled and have no configuration issues, such as incomplete localized text. Learn more in [Viewing languages](p1_view_languages.html). |

## Steps

1. In the PingOne admin console, go to **User Experience > Languages**.

2. In the **Enabled languages** section, to the right of the language that you want to be the default language, click the **More Options** (⋮) icon, and then click **Make default**.

3. In the confirmation message, click **Confirm**.

---

---
title: Cloning a theme
description: Clone a PingOne theme to test the effect of theme changes without immediately deploying the changes to end users.
component: pingone
page_id: pingone:user_experience:p1_themes_cloning
canonical_url: https://docs.pingidentity.com/pingone/user_experience/p1_themes_cloning.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: November 21, 2025
section_ids:
  steps: Steps
  result: Result
---

# Cloning a theme

To test changes to theme settings without immediately changing the theme for all of your end users, you can clone a theme and make your changes to the clone. The cloned theme will have a new theme ID.

This option is particularly useful for testing the effect of theme changes on a single PingOne DaVinci form to ensure that it's working as expected. To test the effect of newer settings on a legacy theme, clone the theme first, and then migrate the clone and make your changes. Afer you've validated that everything works as expected, you can migrate the original theme, maintaining the theme ID and ensuring that you don't have to update all of your forms to use a new ID.

To clone a theme, do the following.

## Steps

1. In the PingOne admin console, go to **User Experience > Branding and Themes** and browse or search for the theme you want to clone.

2. Click the **More options** (⋮) icon and select **Clone Theme**.

## Result

A copy of the theme is created. The theme name is `<original-theme-name>-Clone`.

The **Clone Theme** option is available for legacy and new themes.

---

---
title: Configuring a registration form
description: You can use forms created in User Experience > Forms to allow users to register and sign terms and conditions configured in User Experience > Agreements. You can find more information on configuring agreements for use in forms in Agreements.
component: pingone
page_id: pingone:user_experience:p1_configuring_registration_form
canonical_url: https://docs.pingidentity.com/pingone/user_experience/p1_configuring_registration_form.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: April 3, 2025
section_ids:
  steps: Steps
  result: Result
---

# Configuring a registration form

You can use forms created in **User Experience > Forms** to allow users to register and sign terms and conditions configured in **User Experience > Agreements**. You can find more information on configuring agreements for use in forms in [Agreements](p1_agreements.html).

To create a simple registration form with agreements:

## Steps

1. In the PingOne admin console, go to **User Experience > Forms**.

2. Click the **[icon: plus, set=fa]**icon and select the **Agreement** form.

3. (Optional) Customize the templated form using the form builder. Learn more in [Form configuration](p1_form_configuration.html).

   ![The Create Your Profile templated form.](_images/p1-forms-agreements-template.png)

## Result

You can now use the form in your DaVinci flow with the [Form connector](https://docs.pingidentity.com/connectors/form_connector.html).

---

---
title: Configuring a sign-on form
description: You can use forms created in User Experience > Forms to allow users to sign on with credentials, social login providers, or a magic link.
component: pingone
page_id: pingone:user_experience:p1_configuring_sign_on_form
canonical_url: https://docs.pingidentity.com/pingone/user_experience/p1_configuring_sign_on_form.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: April 3, 2025
section_ids:
  creating-a-sign-on-form-with-username-and-password: Creating a sign-on form with username and password
  steps: Steps
  result: Result
  creating-a-sign-on-form-with-social-login: Creating a sign-on form with social login
  before-you-begin: Before you begin
  steps-2: Steps
  result-2: Result
  creating-a-sign-on-form-with-a-magic-link: Creating a sign-on form with a magic link
  steps-3: Steps
---

# Configuring a sign-on form

You can use forms created in **User Experience > Forms** to allow users to sign on with credentials, social login providers, or a magic link.

## Creating a sign-on form with username and password

To configure a simple sign-on form to allow users to authenticate with their credentials:

### Steps

1. In the PingOne admin console, go to **User Experience > Forms**.

2. Click the **[icon: plus, set=fa]**icon and select the **Sign On** template.

3. (Optional) Customize the templated form using the form builder. Learn more in [Form configuration](p1_form_configuration.html).

   ![The Sign On form template.](_images/p1-forms-sign-on-template.png)

4. Click **Save**.

### Result

You can now use the form in your DaVinci flow with the [Form connector](https://docs.pingidentity.com/connectors/form_connector.html).

## Creating a sign-on form with social login

### Before you begin

In the PingOne admin console, go to **Integrations > External IdPs** and configure social login providers. Learn more in [Adding a vendor-specific identity provider in PingOne](../integrations/p1_adding_vendor_specific_idps.html).

|   |                                                                                                                                                         |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | If you don't have social login providers configured in your PingOne environment, the **Social Login** component won't be available in the form builder. |

### Steps

To configure a sign-on form with social login:

1. In the PingOne admin console, go to **User Experience > Forms**, click **[icon: plus, set=fa]**and select the **Sign On** template.

2. Add a **Divider** component and optionally add a centered label, such as `OR`, to the divider.

3. Add one or more **Social Login** components below the divider to allow the end user to authenticate with social login.

4. (Optional) You can further customize the templated form in the form builder. Learn more in [Form configuration](p1_form_configuration.html).

### Result

You can now use the form in your DaVinci flow with the [Form connector](https://docs.pingidentity.com/connectors/form_connector.html).

## Creating a sign-on form with a magic link

![A Magic Link Authentication form providing a key for the Form connector and the value of the Form connector outputting an OTP challenge to the user-facing screen.](_images/p1-forms-magic-link.jpg)

To configure a sign-on form with magic link:

### Steps

1. Create an email prompt form:

   1. In the PingOne admin console, go to **User Experience > Forms**.

   2. Click **[icon: plus, set=fa]**and select **Blank Form**.

   3. In the **Form Name** field, enter a title for the form, such as `Sign On`.

   4. (Optional) Enter a **Form Description**.

   5. In **Fields > PingOne Attribute Fields > Contact**, drag an **Email** field onto the form.

   6. In the **Form Toolbox**, drag a **Submit Button** component onto the form.

2. Create a magic link prompt form:

   1. In the PingOne admin console, go to **User Experience > Forms**.

   2. Create a form with the **Magic Link Prompt** template.

   3. (Optional) Customize the templated form using the form builder. Learn more in [Form configuration](p1_form_configuration.html).

3. Configure the DaVinci flow:

   1. Add a Challenge connector node in your flow and create an out-of-band challenge flow pattern. Learn more about creating challenges in [Challenge connector](https://docs.pingidentity.com/connectors/challenge_connector.html).

   2. Add a Form connector node and select the **Show Form** capability.

   3. Toggle **Enable Polling** on and set it up to poll the challenge created earlier in the flow by the Challenge connector.

   4. In the **Dynamic Text** table, map the user's email address or phone number with the `magicLinkHint` **Key**.

---

---
title: Configuring an MFA form
description: You can use forms created in User Experience > Forms to allow users to register and authenticate with multi-factor authentication (MFA), by one-time passcode (OTP), FIDO2, or an authenticator app.
component: pingone
page_id: pingone:user_experience:p1_configuring_mfa_form
canonical_url: https://docs.pingidentity.com/pingone/user_experience/p1_configuring_mfa_form.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: April 3, 2025
section_ids:
  creating-an-mfa-form-with-otp: Creating an MFA form with OTP
  steps: Steps
  result: Result
  creating-an-mfa-form-with-fido2-registration: Creating an MFA form with FIDO2 registration
  steps-2: Steps
  creating-an-mfa-form-with-fido2-authentication: Creating an MFA form with FIDO2 authentication
  steps-3: Steps
  creating-an-mfa-form-with-the-authenticator-app: Creating an MFA form with the authenticator app
  steps-4: Steps
  result-2: Result
---

# Configuring an MFA form

You can use forms created in **User Experience > Forms** to allow users to register and authenticate with multi-factor authentication (MFA) *(tooltip: \<div class="paragraph">
\<p>An electronic authentication method where a user is granted access only after presenting two or more verification factors for authentication.\</p>
\</div>)*, by one-time passcode (OTP) *(tooltip: \<div class="paragraph">
\<p>A passcode valid for only one sign-on or transaction on a computer system or other digital device. Also known as a one-time password, one-time PIN, or dynamic password.\</p>
\</div>)*, FIDO2, or an authenticator app.

## Creating an MFA form with OTP

To create an MFA form for registration or authentication with OTP:

### Steps

1. In the PingOne admin console, go to **User Experience > Forms**.

2. Click the **[icon: plus, set=fa]**icon and select one of the following OTP templates:

   * **Email OTP Prompt - Registration**

   * **Email OTP Prompt - Authentication**

   * **SMS OTP Prompt - Registration**

   * **SMS OTP Prompt - Authentication**

   * **Voice OTP Prompt - Registration**

   * **Voice OTP Prompt - Authentication**

3. (Optional) Customize the templated form in the form builder.

4. Click **Save**.

### Result

You can now use the form in your DaVinci flow with the [Form connector](https://docs.pingidentity.com/connectors/form_connector.html).

## Creating an MFA form with FIDO2 registration

To configure FIDO2 in PingOne Forms for registration:

### Steps

1. Create a FIDO2 form:

   1. In the PingOne admin console, go to **User Experience > Forms**.

   2. Click the **[icon: plus, set=fa]**icon and select the **FIDO2 - Registration** template.

   3. (Optional) Customize the templated form in the form builder.

   4. Click **Save**.

2. In DaVinci, configure the flow.

   ![A DaVinci FIDO2 MFA flow. This first Form connector is set to Create Device, followed by a Form connector using Show Form with FIDO2 Registration selected. The final Form connector is set to Activate Device.](_images/p1-forms-fido2-registration.png)

   1. Add a PingOne MFA connector node and select the **Create Device** capability.

      |   |                                                                                                           |
      | - | --------------------------------------------------------------------------------------------------------- |
      |   | This connector is necessary for **Public Key Credential Creation** field in the following Form connector. |

   2. In a subsequent node, add a Form connector and select the **Show Form** capability, then select the FIDO2 registration form you created in **User Experience > Forms**.

   3. In a subsequent node, add another PingOne MFA node and select the **Activate Device** capability.

## Creating an MFA form with FIDO2 authentication

To configure FIDO2 in PingOne Forms for authentication:

### Steps

1. Create a FIDO2 form:

   1. In the PingOne admin console, go to **User Experience > Forms**.

   2. Click the **[icon: plus, set=fa]**icon and select the **FIDO2 - Authentcation** template.

2. (Optional) Customize the templated form in the form builder.

3. Click **Save**.

4. Configure the DaVinci flow.

   ![A DaVinci FIDO2 MFA flow. The first Form connector is set to Create Device Authentication, followed by a Form connector using Show Form with FIDO2 Authentication selected. The final Form connector is set to FIDO Assertion.](_images/p1-forms-fido2-authentication.png)

   1. In your PingOne DaVinci flow, add a PingOne MFA connector and select the **Create Device Authentication** capability.

      |   |                                                                                                              |
      | - | ------------------------------------------------------------------------------------------------------------ |
      |   | This connector is necessary for the **Public Key Credential Request** field in the following Form connector. |

   2. In a subsequent node, add a Form connector and select the **Show Form** capability, then select the FIDO2 authentication form you created in **User Experience > Forms**.

   3. In a subsequent node, add another PingOne MFA node and select the **FIDO Assertion** capability.

## Creating an MFA form with the authenticator app

To create a simple registration or authentication form with an authenticator app prompt:

### Steps

1. In the PingOne admin console, go to **User Experience > Forms**.

2. Click the **[icon: plus, set=fa]**icon and select either the **Authenticator App Prompt - Registration** or **Authenticator App Prompt - Authentication** form.

3. (Optional) Customize the templated form in the form builder.

4. Click **Save**.

### Result

You can now use the form in your DaVinci flow with the [Form connector](https://docs.pingidentity.com/connectors/form_connector.html).

---

---
title: Configuring conditional component visibility
description: Configure PingOne forms to show or hide components so that a form can be more modular with conditional component visibility.
component: pingone
page_id: pingone:user_experience:p1_configuring_conditional_component_visibility
canonical_url: https://docs.pingidentity.com/pingone/user_experience/p1_configuring_conditional_component_visibility.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 19, 2026
section_ids:
  steps: Steps
  use-case-reusing-one-form-for-multiple-scenarios: "Use case: Reusing one form for multiple scenarios"
  steps-2: Steps
---

# Configuring conditional component visibility

You can configure components so that they're shown or hidden in a user-facing form based on one or more Boolean values pulled from your DaVinci flow.

|   |                                                                                                                                                                                                       |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The following components don't have visibility controls:- **Submit button**

- **MFA Device Selection - Authentication**

- **MFA Device Selection - Registration**

- **FIDO2**

- **Error Display** |

## Steps

To configure conditional component visibility:

1. In the PingOne admin console, go to **User Experience > Forms**.

2. Click the **Pencil** ([icon: pencil, set=fa]) icon next to the form to configure.

3. Select a component in the form builder.

4. In the **Visibility Type** list, select whether the component is always visible, shown by default, or hidden by default.

5. (Optional) Change the default **Visibility Key**. You'll need this key for the PingOne Form connector's **Component Visibility** field.

6. Click **Save**.

7. Configure conditional component visibility in the [Form connector](https://docs.pingidentity.com/connectors/form_connector.html).

   1. In your DaVinci flow, add the PingOne Form connector.

   2. Select the **Show Form** capability.

   3. In the **Form** list, select the form you configured with conditional component visibility in your PingOne admin console.

   4. In the **Component Visibility** field, you can populate the **Value** for the key associated with each component that was either **Hidden by default** or **Shown by default** when you created the form.

   5. For each **Key**, select a variable from your flow that will act as a Boolean to show or hide the components associated with the key.

8. Click **Apply**.

## Use case: Reusing one form for multiple scenarios

In this example, we'll build an one-time passcode (OTP) *(tooltip: \<div class="paragraph">
\<p>A passcode valid for only one sign-on or transaction on a computer system or other digital device. Also known as a one-time password, one-time PIN, or dynamic password.\</p>
\</div>)* prompt form for registration that will allow a user to register with either an email or an SMS.

## Steps

1. In the PingOne admin console, go to **User Experience > Forms**.

2. Click the **[icon: plus, set=fa]**icon.

3. Enter a form name and optional description and click **Add Form**.

4. Select **Email OTP Prompt - Registration**.

5. On the **Fields** and **Toolbox** tabs, customize the form to include components for an SMS OTP prompt for registration:

   ![Form configured in the form builder with components for both email and SMS OTP registration.](_images/p1-forms-conditional-components.png)

6. To make the user-facing form a conditional form that shows an OTP form for email by default but can also be an SMS OTP form based on Boolean values in the DaVinci flow:

   1. Click the **Rich Text** heading component for email in the form builder.

   2. In the configuration panel, set the **Visibility Type** to **Show by default**.

   3. (Optional) Change the **Visibility Key** to something meaningful, such as `otpEmail`.

      |   |                                                                                                                                                           |
      | - | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
      |   | This key doesn't need to be unique because multiple components can share the same **Visibility Key**, allowing you to show or hide a group of components. |

   4. Repeat for the **Rich Text** description and **Email Address** components, ensuring the **Visibility Key** is `otpEmail` so the components are grouped for visibility.

   5. Repeat these steps for the SMS OTP form components, but set the **Visibility** to **Hide by default** and create a shared **Visibility Key**, such as `otpText`.

7. Click **Save**.

8. Configure conditional component visibility in the Form connector.

   1. In your DaVinci flow, add the PingOne Form connector.

   2. Select the **Show Form** capability.

   3. In the **Form** list, select the form you configured with conditional component visibility in your PingOne admin console.

   4. In the **Component Visibility** field, you can populate the **Value** for the key associated with each component that was either **Hidden by default** or **Shown by default** when you created the form.

   5. For each **Key**, select a variable from your flow that will act as a Boolean to show or hide the components associated with the key.

9. Click **Apply**.

---

---
title: Configuring localized content
description: Use the Agreements, Notification Templates, and Forms pages to set up localized content for each language.
component: pingone
page_id: pingone:user_experience:p1_configure_localized_content
canonical_url: https://docs.pingidentity.com/pingone/user_experience/p1_configure_localized_content.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: August 16, 2024
section_ids:
  steps: Steps
  next-steps: Next steps
---

# Configuring localized content

Use the **Agreements**, **Notification Templates**, and **Forms** pages to set up localized content for each language.

## Steps

* To set up localization for agreements, follow the steps for [Creating localized content](p1_create_localized_content.html).

* To set up localization for notifications, follow the steps in [Notification Templates](p1_notifications.html).

* To set up localization for PingOne Forms, follow the steps for [Using translatable keys](p1_using_translatable_keys.html).

## Next steps

Make sure that the appropriate language is enabled for that language to appear in end user sign-on screens. Learn more in [Viewing languages](p1_view_languages.html).

---

---
title: Configuring the Self Service portal end-user experience
description: Configure what information appears to the end user in PingOne Self Service.
component: pingone
page_id: pingone:user_experience:p1_configure_self_service
canonical_url: https://docs.pingidentity.com/pingone/user_experience/p1_configure_self_service.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 22, 2025
section_ids:
  steps: Steps
---

# Configuring the Self Service portal end-user experience

You can configure what information appears to end users in **Self Service**, also known as the PingOne Self-Service - MyAccount app. You can choose the sign-off method that PingOne uses when end users sign off from the MyAccount app. Learn more in [System applications](../applications/p1_system_applications.html).

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | This topic only applies to configuration that affects what end users can see and do in the Self-Service portal. You can manage the application, including defining authentication requirements, adding an authentication policy, configuring access control, and fine-tuning API scopes:1) Go to **Applications > Applications > PingOne Self-Service - MyAccount** application

2) Use the **Resources**, **Policies**, and **Access** tabs to make changes.Learn more about configuring the application in [Editing an application](../applications/p1_editing_applications.html) and about adding an authentication policy in [Setting up end-user authentication for the Self Service portal](p1_setting_up_authentication_self_service.html). |

## Steps

1. In the PingOne admin console, go to **User Experience > Self Service**.

2. Click the **Pencil** icon ([icon: pencil, set=fa]).

3. Select or clear the following options as appropriate for your organization:

   | Setting                    | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
   | -------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
   | **Branding and Themes**    |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
   | **Apply Active Theme**     | Apply the branding and themes configured for the environment to the MyAccount app.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
   | **Show Footer**            | Show the theme's footer at the bottom of the MyAccount app.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
   | **Self Service Section**   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
   | **Manage Profile**         | Allow end users to edit their own profile attributes. If this option is enabled, end users can modify their profile details, such as name, address, and phone number. The specific attributes vary depending on the environment configuration.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
   | **Manage Authentication**  | Allow end users to manage their authentication methods, such as email, security key, text message, or authenticator app.&#xA;&#xA;Users should always include the country code when pairing a device. Phone formats across the globe are constantly expanding and changing. If the country code isn't included, issues might occur with message delivery.Choose from the following options:- **Enable or Disable MFA**: Allow end users to enable or disable multi-factor authentication (MFA) *(tooltip: \<div class="paragraph">&#xA;\<p>An electronic authentication method where a user is granted access only after presenting two or more verification factors for authentication.\</p>&#xA;\</div>)* for their account. This option is relevant for Customer Identity and Access Management (CIAM) users.

   - **Manage PingID Devices via MyAccount**: Allow PingID users to manage their devices from the MyAccount app. This option is relevant for PingID workforce users from environments that are converged with PingOne. Learn more in [Using MyAccount to manage PingID devices (Workforce only)](p1_using_myaccount_to_manage_wf_devices.html)

     &#xA;&#xA;Selecting Manage PingID Devices via My account also:&#xA;&#xA;Enables the Allow user actions according to granted authentication scopes option in the MyAccount app Resources tab. This option provides users with a limited set of scopes until they authenticate.&#xA;&#xA;Adds the MyAccount app to all PingID policies that already include Device Management.&#xA;&#xA;To allow PingID users to manage their account with limited scopes, you must also ensure an MFA policy or MFA DaVinci flow policy is added to the MyAccount app.&#xA;&#xA;To add a policy to the app, refer to Associating an authentication policy with a web app.&#xA;&#xA;To disable reduced scopes, refer to Editing scopes for an application.&#xA;&#xA;Learn more about PingOne API scopes and their function in PingOne Self-management scopes.

   - **None**: Do not enable either option. |
   | **Change Password**        | Allow end users to change their own passwords.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
   | **Manage Linked Accounts** | Allow end users to manage the linked accounts that are used during authentication.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
   | **Manage Sessions**        | Allow end users to view or sign off from PingOne sessions.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
   | **View Agreements**        | Allow users to see the agreements to which they've consented.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
   | **Manage OAuth Consents**  | Allow users to view and revoke OAuth consents to which they've agreed.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
   | **Sign Off Method**        | Determine which sign-off method PingOne uses when users sign off from the MyAccount app. Choose either of the following options:- **OIDC Logout** (default): Allow the end user to sign off from the MyAccount app using OpenID Connect (OIDC) *(tooltip: \<div class="paragraph">&#xA;\<p>An authentication protocol built on top of OAuth that authenticates users and enables clients (relying parties) of all types to request and receive information about authenticated sessions and users. OIDC is extensible, allowing clients to use optional features such as encryption of identity data, discovery of OpenID Providers (OAuth authorization servers), and session management.\</p>&#xA;\</div>)* relying party (RP)-initiated logout. This option invalidates access tokens, refresh tokens, and ID tokens associated with the session. When selected, PingOne doesn't send SAML 2.0 single logout requests to SAML identity providers or applications.

     Learn more in the [OIDC RP-Initiated Logout 1.0 documentation](https://openid.net/specs/openid-connect-rpinitiated-1_0.html).

   - **SAML 2.0 Single Logout**: Initiate SAML 2.0 single logout when the user signs off from the MyAccount app. Access tokens, refresh tokens, and ID tokens obtained during the session remain valid until they expire or are revoked.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |

4. Click **Save**.

---

---
title: Creating a form
description: Creating a form in PingOne allows you to provide branded user experiences through custom forms without writing custom HTML. You can quickly implement these forms in DaVinci with the Form connector. After you create a form in User Experience > Forms, using either a blank form or a form template, you can customize your form. Learn more in Form configuration.
component: pingone
page_id: pingone:user_experience:p1_creating_form
canonical_url: https://docs.pingidentity.com/pingone/user_experience/p1_creating_form.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: April 3, 2025
section_ids:
  steps: Steps
  result: Result:
---

# Creating a form

Creating a form in PingOne allows you to provide branded user experiences through custom forms without writing custom HTML. You can quickly implement these forms in DaVinci with the Form connector. After you create a form in **User Experience > Forms**, using either a blank form or a form template, you can customize your form. Learn more in [Form configuration](p1_form_configuration.html).

In this example, you create a form using a template that's set up for your own branding and localization to be quickly included in a DaVinci flow.

## Steps

1. Create a form in PingOne:

   1. In the PingOne admin console, go to **User Experience > Forms**.

   2. Click the **[icon: plus, set=fa]**icon.

   3. In the **Form Name** field, enter a name for the form.

      |   |                                                                 |
      | - | --------------------------------------------------------------- |
      |   | This form name is used internally and isn't displayed to users. |

   4. (Optional) In the **Form Description** field, enter a description for the form.

   5. Click **Add Form**.

      ### Result:

      A modal opens listing the available templates.

   6. Select **Blank Form** to create a custom form or select a preconfigured form that's appropriate for your use case.

2. Customize your form. Learn more in [Form configuration](p1_form_configuration.html).

3. In the **User Experience > Branding and Themes** section, customize your form with branding and themes. Learn more in [Branding and Themes](p1_branding_themes.html).

   |   |                                                                                                                                                                                              |
   | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | If you have customizations in DaVinci Forms as well as in **Branding and Themes**, the style configured in DaVinci Forms takes precedence over styles configured in **Branding and Themes**. |

4. To support localization for the user-facing text in your form, add translatable keys in the configuration settings for the form. Learn more in [Using translatable keys](p1_using_translatable_keys.html).

5. To implement the form in DaVinci, add and configure the Form connector in DaVinci. Learn more in [Form connector documentation](https://docs.pingidentity.com/connectors/form_connector.html).

---

---
title: Creating localized content
description: After you add a language version to an agreement, you can enter the localized text that makes up the agreement. Each time you modify the localized agreement content, the revision number is incremented. You configure each new revision to require re-consent, if needed.
component: pingone
page_id: pingone:user_experience:p1_create_localized_content
canonical_url: https://docs.pingidentity.com/pingone/user_experience/p1_create_localized_content.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: January 24, 2025
section_ids:
  steps: Steps
  next-steps: Next steps
---

# Creating localized content

After you add a language version to an agreement, you can enter the localized text that makes up the agreement. Each time you modify the localized agreement content, the revision number is incremented. You configure each new revision to require re-consent, if needed.

## Steps

1. In the PingOne admin console, go to **User Experience > Agreements**.

2. In the **Agreements** list, locate the agreement you want to edit. Click the agreement entry to open the details panel.

3. On the **Overview** tab, click the **Edit Localized Content** button.

4. On the left side, under **Languages**, click the language you want to edit.

5. Enter or edit the following information:

   * **Localized agreement title**: Enter or edit the title as it should appear in this language.

   * **Agreement format**: Specify the type of content for the agreement text: plain text or HTML. With HTML, you can style the agreement text and include hyperlinks. The following HTML elements are allowed: `a`, `br`, `p`, `b`, `i`, `em`, `h1`, `h2`, `h3`, `strong`.

     |   |                                                                                                                                                                                                                                                                                                       |
     | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
     |   | * Hyperlinks must use the `https` protocol.

     * To set up a hyperlink that opens in a new browser window, add the `target="blank"` attribute to the `<a>` element. For example, `<a href="https://www.example.com" target="blank">Terms and conditions</a>`.

     * The `<script>` element is not allowed. |

   * **Localized Agreement Content**: Enter or paste the text of the agreement.

   * **Acceptance label**: The text that is displayed for the affirmative option. For example, `I accept`.

   * **Continue label**: The text that is displayed for the user to continue after accepting the agreement. For example, `Continue`.

   * **Don't accept label**: The text that is displayed for the negative option. For example, `I don't accept`.

   * **Effective date**: Specify when the agreement should go into effect.

   * **Require new consent**: Specify whether users will have to re-consent if the agreement is updated.

6. Click **Save**.

## Next steps

[Previewing an agreement](p1_preview_agreement.html)