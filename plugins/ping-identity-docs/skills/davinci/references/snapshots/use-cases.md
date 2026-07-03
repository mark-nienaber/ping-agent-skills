---
title: Adding social login with PingOne
description: Adding social login lets your users sign on using existing social accounts, simplifying their sign-on process.
component: davinci
page_id: davinci:use_cases:davinci_use_cases_adding_social_login
canonical_url: http://docs.pingidentity.com/davinci/use_cases/davinci_use_cases_adding_social_login.html
llms_txt: http://docs.pingidentity.com/davinci/llms.txt
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

Create an external identity provider for each social login option that you plan to use. Learn more in [External IDPs](http://docs.pingidentity.com/pingone/integrations/p1_external_idps.html).

#### About this task

First, create one or more forms in PingOne.

|   |                                                                                                                                                                                                                               |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | This procedure does not cover all of the options available in the **Forms** section. Learn more about all available options in the [Forms documentation](http://docs.pingidentity.com/pingone/user_experience/p1_forms.html). |

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

|   |                                                                                                                                                                                                                                            |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | This procedure does not discuss all of the options available for the PingOne Forms connector. Learn more about all available options in the [Forms connector documentation](http://docs.pingidentity.com/connectors/forms_connector.html). |

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
