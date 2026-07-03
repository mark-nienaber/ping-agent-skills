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
