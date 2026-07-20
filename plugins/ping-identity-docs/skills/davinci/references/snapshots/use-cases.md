---
title: Adding social login with PingOne
description: Adding social login lets your users sign on using existing social accounts, simplifying their sign-on process.
component: davinci
page_id: davinci:use_cases:davinci_use_cases_adding_social_login
canonical_url: https://docs.pingidentity.com/davinci/use_cases/davinci_use_cases_adding_social_login.html
llms_txt: https://docs.pingidentity.com/davinci/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 24, 2024
section_ids:
  procedure: Procedure
  creating-forms: Creating forms
  before-you-begin: Before you begin
  about-this-task: About this task
  steps: Steps
  adding-forms-to-flows: Adding forms to flows
  about-this-task-2: About this task
  steps-2: Steps
  result: Result
---

# Adding social login with PingOne

Adding social login lets your users sign on using existing social accounts, simplifying their sign-on process.

You can use the PingOne **Social Login** feature to add social login buttons to forms created in PingOne. In this solution, you create one or more forms in PingOne and then add social login buttons to those forms. You then include the forms in your DaVinci flows and perform some additional configuration for user population and account matching.

When a user reaches one of the forms, they can use an existing social account to sign on.

## Procedure

This section shows you how to create one or more forms, add social login buttons to those forms, and add the forms to one or more flows.

|   |                                                                                                                                                               |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The forms, social login options, and flows in your environment will vary. This procedure is as specific as possible while still applying to all environments. |

### Creating forms

#### Before you begin

Create an external identity provider for each social login option that you plan to use. Learn more in [External IDPs](https://docs.pingidentity.com/pingone/integrations/p1_external_idps.html).

#### About this task

First, create one or more forms in PingOne.

|   |                                                                                                                                                                                                                                |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | This procedure does not cover all of the options available in the **Forms** section. Learn more about all available options in the [Forms documentation](https://docs.pingidentity.com/pingone/user_experience/p1_forms.html). |

#### Steps

1. Sign on to PingOne and go to **User Experience > Forms**.

2. Click the **[icon: plus, set=fa]**icon to create a new form.

3. In the **Form Name** field, enter `User Information Example`.

4. In the **Form Usage** list, select **DaVinci Flow Forms**.

5. Click **Add Form**.

6. Select a template or a blank form as a starting point.

7. Add one or more social login options:

   1. Click the **Toolbox** tab.

   2. Drag a **Social Login** button from the left panel onto the form.

   3. Click the new **Social Login** button in the form to display its properties.

   4. In the **App Type** list, select a social login application.

   5. (Optional) Repeat steps b-d to add additional social login options to the form.

   6. (Optional) Update the width and style settings.

8. (Optional) Drag one or more **PingOne Attribute Fields** onto the form.

9. Click **Save**.

### Adding forms to flows

#### About this task

After adding social login to your forms, add the forms to your flow.

|   |                                                                                                                                                                                                                                             |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | This procedure does not discuss all of the options available for the PingOne Forms connector. Learn more about all available options in the [Forms connector documentation](https://docs.pingidentity.com/connectors/forms_connector.html). |

#### Steps

1. Sign on to DaVinci and click the **Flows** tab.

2. Find the flow to which you want to add the forms and go to **... > Edit**.

3. Click the **[icon: plus, set=fa]**icon to add a node.

4. In the **Add Connector** list, select the **PingOne Forms** connector.

5. Click and drag a line from the new node to the existing nodes.

6. Click the **PingOne Forms** node.

7. Select the **Show Form** capability.

8. In the **Form** list, select your form.

9. (Optional) Configure the social login-specific settings:

   1. Enable **Link with PingOne User** to link the social account with the existing PingOne user.

   2. Select a **PingOne Population** for user linking, or select **Use Population ID** to specify a population ID.

   3. In the **Population ID** field, enter a population ID to use for user linking. This field is only displayed if you selected **Use Population ID** in the **PingOne Population** field.

10. Click **Apply**.

11. (Optional) Repeat steps 3-10 for each additional form that you want to add.

12. (Optional) Repeat steps 2-11 for each additional flow.

#### Result

The flows now include the forms which include social login. Integrate these flows into your environment using a redirect to begin using them. Learn more in [Launching a PingOne flow with a redirect](../integrating_flows_into_applications/davinci_launch_flow_redirect.html).

---

---
title: Creating an authentication flow
description: Create a flow to authenticate a user and optionally reset their password.
component: davinci
page_id: davinci:use_cases:davinci_use_cases_creating_an_authentication_flow
canonical_url: https://docs.pingidentity.com/davinci/use_cases/davinci_use_cases_creating_an_authentication_flow.html
llms_txt: https://docs.pingidentity.com/davinci/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: February 2, 2023
section_ids:
  copying-the-flow-template: Copying the flow template
  steps: Steps
  creating-the-flow: Creating the flow
  steps-2: Steps
---

# Creating an authentication flow

Create a flow to authenticate a user and optionally reset their password.

## Copying the flow template

Copy the **DaVinci Flow - PingOne Sign On and Password Reset** template.

### Steps

1. Go to the [Ping Identity Marketplace](https://marketplace.pingone.com/browse?contentType=davinciFlows).

2. Find and open the **DaVinci Flow - PingOne Sign On and Password Reset** flow.

3. Click **Download Integration**.

4. Save the flow JSON.

## Creating the flow

Create a new flow using the **PingOne - Sign On and Password Reset** template.

### Steps

1. Sign on to your DaVinci environment.

2. Click the **Flows** tab.

3. Click **Add Flow**.

4. Click **Import From JSON** and select the saved template.

   ![A screen capture of the creation options displayed when creating a new flow. The Import From JSON option is highlighted.](_images/aod1646418421785.png)

5. (Optional) Update the name and description of the flow.

6. Click **Import**.

7. Click the **PingOne User Lookup** connector.

8. Click the **Edit Connector** icon.

   ![A screen capture of the edit connector icon.](../_images/rbh1646418951869.png)

9. In the **Environment ID** field, enter your PingOne environment ID.

10. In the **Client ID** field, enter your PingOne client ID.

11. In the **Client Secret** field, enter your PingOne client secret.

12. Click **Apply**.

13. Click **Save**.

14. Click **Deploy**.

---

---
title: Localizing flows with PingOne
description: Localizing a flow lets you present a single flow to customers who use multiple languages, providing a better experience for customers and reducing backend complexity.
component: davinci
page_id: davinci:use_cases:davinci_use_cases_localizing_flows
canonical_url: https://docs.pingidentity.com/davinci/use_cases/davinci_use_cases_localizing_flows.html
llms_txt: https://docs.pingidentity.com/davinci/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 22, 2023
section_ids:
  procedure: Procedure
  creating-forms: Creating forms
  about-this-task: About this task
  steps: Steps
  adding-languages-and-translations: Adding languages and translations
  about-this-task-2: About this task
  steps-2: Steps
  adding-forms-to-flows: Adding forms to flows
  about-this-task-3: About this task
  steps-3: Steps
  result: Result
---

# Localizing flows with PingOne

Localizing a flow lets you present a single flow to customers who use multiple languages, providing a better experience for customers and reducing backend complexity.

You can use the PingOne **Languages** feature to provide translations for forms created in PingOne. In this solution, you create one or more forms in PingOne and then use the **Languages** feature to add translations for the fields, options, error messages, and other content used by those forms. You then include the forms in your DaVinci flows.

When a user reaches one of the forms, PingOne uses their browser's language setting to present them with the correct translation of the form.

## Procedure

This section shows you how to create one or more forms, add translations for those forms, and add the forms to one or more flows.

|   |                                                                                                                                                    |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The forms, languages, and flows in your environment will vary. This procedure is as specific as possible while still applying to all environments. |

### Creating forms

#### About this task

First, create one or more forms in PingOne.

|   |                                                                                                                                                                                                                                              |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | This procedure does not cover all of the options available in the **Forms** section. You can find information about all available options in the [Forms documentation](https://docs.pingidentity.com/pingone/user_experience/p1_forms.html). |

#### Steps

1. Sign on to PingOne and go to **User Experience > Forms**.

2. Click the **[icon: plus, set=fa]**icon to create a new form.

3. In the **Form Name** field, enter `User Information Example`.

4. In the **Form Usage** list, select **DaVinci Flow Forms**.

5. Click **Add Form**.

6. Select a template or a blank form as a starting point.

7. (Optional) Add one or more custom fields and create a translation key for each one:

   1. Drag the custom field onto the form.

   2. In the left pane, click the translation key icon in the **Label** field.

      ![This screenshot shows the Label field with the translation key icon highlighted.](_images/kel1685120582765.png)

   3. Select **Create New Key**.

   4. In the **Key** column, enter an internal name for the key.

   5. In the **Default Translation** column, enter the value of the key in your environment's default language.

   6. Click **Select**.

8. (Optional) Drag one or more **PingOne Attribute Fields** onto the form.

9. Click **Save**.

### Adding languages and translations

#### About this task

After creating your forms, enable one or more languages, then provide translations for the fields in your forms for each enabled language.

|   |                                                                                                                                                                                                                                                   |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | This procedure does not discuss all options available in the **Languages** section. For more information about all available options, see the [Languages documentation](https://docs.pingidentity.com/pingone/user_experience/p1_languages.html). |

#### Steps

1. Sign on to PingOne and go to **User Experience > Languages**.

2. Click the **[icon: plus, set=fa]**icon to add a language.

3. In the **Languages** list, select a language to add.

4. Click **Save Changes**.

5. Select the language that you added from the list of languages.

6. In the **Module** list, select **DaVinci Forms**.

7. Provide translations for the standard fields in your forms:

   1. In the **Page** list, select **Standard Fields**.

   2. Click the **Pencil** icon.

   3. Enter translations for the standard fields that you used in your forms.

   4. Click **Save**.

8. Provide translations for the custom fields in your forms:

   1. In the **Page** list, select **Custom Messages**.

   2. Click the **Pencil** icon.

   3. Enter translations for the custom fields that you used in your forms.

   4. Click **Save**.

9. Provide translations for additional text that you used in your forms:

   1. In the **Page** list, select **Others**.

   2. Click the **Pencil** icon.

   3. Enter translations for the additional text that you used in your forms.

   4. Click **Save**.

10. (Optional) Repeat steps 5-9 for each additional language that you have enabled.

### Adding forms to flows

#### About this task

After adding your languages and translations for your forms, add the forms to your flow.

|   |                                                                                                                                                                                                                                              |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | This procedure does not discuss all of the options available for the Form connector. For more information about all available options, see the [Form connector documentation](https://docs.pingidentity.com/connectors/form_connector.html). |

#### Steps

1. Sign on to DaVinci and click the **Flows** tab.

2. Find the flow to which you want to add the forms and go to **... > Edit**.

3. Click the **[icon: plus, set=fa]**icon to add a node.

4. In the **Add Connector** list, select the **PingOne Forms** connector.

5. Click and drag a line from the new node to the existing nodes.

6. Click the **PingOne Forms** node.

7. Select the **Show Form** capability.

8. In the **Form** list, select your form.

9. Click **Apply**.

10. (Optional) Repeat steps 3-9 for each additional form that you want to add.

11. (Optional) Repeat steps 2-10 for each additional flow.

#### Result

The flows now include the forms, which use the language defined in the user's browser settings. Integrate these flows into your environment using a redirect to begin using them. Learn more in [Launching a PingOne flow with a redirect](../integrating_flows_into_applications/davinci_launch_flow_redirect.html).

---

---
title: Use Cases
description: These use cases showcase ways in which you can use flows to solve specific business challenges.
component: davinci
page_id: davinci:use_cases:davinci_use_cases
canonical_url: https://docs.pingidentity.com/davinci/use_cases/davinci_use_cases.html
llms_txt: https://docs.pingidentity.com/davinci/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 28, 2024
---

# Use Cases

These use cases showcase ways in which you can use flows to solve specific business challenges.

* [Creating an authentication flow](davinci_use_cases_creating_an_authentication_flow.html)

* [Localizing flows with PingOne](davinci_use_cases_localizing_flows.html)

* [Adding social login with PingOne](davinci_use_cases_adding_social_login.html)

Some solutions also combine DaVinci with PingOne or other tools to address more complex business challenges.

* PingOne for Customers Passwordless: This solution uses PingOne and a set of tailored DaVinci flows to create a registration and sign-on process that incorporates passwordless, password, and multi-factor authentication (MFA) options. Learn more in the [PingOne for Customers Passwordless documentation](https://docs.pingidentity.com/pingone-solutions/pingone-customers-passwordless/index.html).

* PingOne for Customers Plus: This solution uses PingOne and a set of tailored DaVinci flows to create a registration and sign-on process that incorporates a variety of MFA options. Learn more in the [PingOne for Customers Plus documentation](https://docs.pingidentity.com/pingone-solutions/pingone-customers-plus/index.html).

* Financial Services: This solution uses PingOne and a set of tailored DaVinci flows to provide end users a secure way to make payments and transfers. Learn more in the [Financial Services documentation](https://docs.pingidentity.com/pingone-solutions/financial-services/index.html).

* Gift Card Redemption: This solution uses PingOne and a set of tailored DaVinci flows to provide a secure way for users to redeem gift cards, including step-up authentication and the ability for users to update their email address and other information. Learn more in the [Gift Card Redemption documentation](https://docs.pingidentity.com/pingone-solutions/gift-card-auth/index.html).

* Healthcare: This solution uses PingOne and a set of tailored DaVinci flows to provide a secure way for patients to manage accounts and for customer service representatives to help users with account management. Learn more in the [Healthcare flow pack documentation](https://docs.pingidentity.com/pingone-solutions/healthcare/index.html).

* Microsoft Entra ID: This solution lets customers use an external authentication provider for multi-factor authentication (MFA) through Entra ID. In this use case, you'll learn how to set up Entra ID, PingOne SSO, and PingID to support external MFA in Entra ID. In this scenario, Entra ID is the identity provider (IdP), and PingOne SSO and PingID are the external authentication provider. Learn more in [Setting up PingOne SSO, DaVinci, and PingID as the external MFA provider for Microsoft Entra ID](https://docs.pingidentity.com/pingone/use_cases/p1_set_up_external_mfa_provider_microsoft_entra_davinci.html).

* Client-initiated backchannel authentication (CIBA): CIBA enables an end user to use an application on one device and grants consent to the application on another device. Because PingOne uses DaVinci to orchestrate the out-of-band authentication and authorization experience, you can design a PingOne DaVinci CIBA flow that suits the needs of your organization. Learn more in [Configuring a CIBA flow](https://docs.pingidentity.com/pingone/use_cases/p1_configure_ciba_flow.html).