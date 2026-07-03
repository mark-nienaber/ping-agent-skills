---
title: UI Studio
description: The UI Studio lets you create user interface templates that match your company style and branding, which you can include in flows using an HTTP connector.
component: davinci
page_id: davinci:ui_studio:davinci_ui_studio
canonical_url: http://docs.pingidentity.com/davinci/ui_studio/davinci_ui_studio.html
llms_txt: http://docs.pingidentity.com/davinci/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 22, 2023
section_ids:
  creating-a-ui-template: Creating a UI template
  steps: Steps
  editing-a-ui-template: Editing a UI template
  steps-2: Steps
  deleting-a-ui-template: Deleting a UI template
  steps-3: Steps
---

# UI Studio

The UI Studio lets you create user interface templates that match your company style and branding, which you can include in flows using an HTTP connector.

## Creating a UI template

Create a UI template to control the UI design inside your flows.

## Steps

1. Click the **UI Studio** tab.

2. Click **Add UI Template**.

3. Enter a **Name** for the UI template.

4. (Optional) In the **Description** field, enter a description for the UI template.

5. Find the newly created UI template and click **Edit**.

6. (Optional) Enter HTML for your UI template:

   1. Click the **HTML** tab.

   2. In the **Template (HTML)** field, enter the HTML for your UI.

   3. In the **Form Validation Rules** section, click **Add** to add one or more properties to evaluate.

   4. In the **Property Name** field, enter a property name.

   5. Click **Add** to add one or more rules for the property.

   6. For each rule, select a rule in the **Rule Name** list.

   7. For each **Required** rule, enter a **Validation Message** that displays if the required property is not present.

   8. For each **Email** rule, enter a **Validation Message** that displays if the property is not a valid email.

   9. For each **Length** rule, enter a **Minimum**, **Maximum**, or **Exact** value for the property and a **Validation Message** that is displayed for each length restriction that isn't met.

   10. For each **Format** rule, enter the **Regex** that defines the required format and the **Validation Message** that displays if the property doesn't match the format.

   11. For each **Equality** rule, enter the **Other Property** that this property must match, and the **Validation Message** that displays if the properties don't match.

7. (Optional) Enter CSS for your UI template:

   1. Click the **CSS** tab.

   2. In the **Style (CSS)** field, enter the CSS for your UI.

8. (Optional) Enter a script for your UI template:

   1. Click the **Script** tab.

   2. In the **Script (JavaScript)** field, enter the script for your UI.

9. (Optional) Enter a schema for your UI template:

   1. Click the **Schema** tab.

   2. In the **Input Schema** field, enter the input schema for your UI.

   3. In the **Output Schema** field, enter the output schema for your UI.

10. Click **Apply**.

## Editing a UI template

Edit an existing UI template.

### Steps

1. Click the **UI Studio** tab.

2. Find the UI template and click **Edit**.

3. Update the desired fields in the UI template.

4. Click **Apply**.

## Deleting a UI template

Delete an existing UI template.

### Steps

1. Click the **UI Studio** tab.

2. Find the UI template and click **Delete**.

3. In the confirmation window, click **Delete**.