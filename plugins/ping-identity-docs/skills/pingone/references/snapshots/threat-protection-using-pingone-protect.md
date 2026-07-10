---
title: Adding a risk policy
description: Add a risk policy using PingOne Protect.
component: pingone
page_id: pingone:threat_protection_using_pingone_protect:p1_protect_adding_risk_policy
canonical_url: https://docs.pingidentity.com/pingone/threat_protection_using_pingone_protect/p1_protect_adding_risk_policy.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 30, 2025
section_ids:
  before-you-begin: Before you begin
  steps: Steps
  example: Example:
  example-2: Example:
  best-practice-mitigation-rule-ordering: "Best practice: Mitigation rule ordering"
  less-effective-order: Less effective order
  recommended-order: Recommended order
  next-steps: Next steps
---

# Adding a risk policy

Every PingOne environment with the PingOne Protect service includes a default risk policy. You can create additional risk policies for different scenarios. For example, you might need to use a stricter risk policy in some situations and a more lenient risk policy in other situations. Learn more in [Introduction to risk policies](p1_protect_getting_started.html#essential_concepts) and [Risk policies](p1_protect_risk_policies.html).

With PingOne Protect, you can create two types of policies:

* **Global**

  Allows you to configure predictor scores, risk thresholds to map the scores to a risk level, and overrides or mitigations to take priority over the scores and levels. When using a global risk policy, you must choose which risk policy to pass to the risk evaluation.

* **Targeted**

  Allows you to define risk policies for different targets, including flow types, applications being accessed, and user groups to which the risk policy will apply. You can also configure predictor scores, risk thresholds to map the scores to a risk level, and mitigations.

  During risk evaluations, targeted policies are processed in the order displayed in the **Targeted Policies** list. You can set the order in which the targeted policies are evaluated. Processing stops when the target criteria for a policy are met.

In both types of policies, a mitigation is an action that you recommend if a given condition is met. For example, you can configure a mitigation rule to deny access if the email reputation predictor returns high risk. When the condition is met, the recommended action that you created is returned in the risk evaluation response.

|   |                                                                                                                                                                                             |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Customize risk policies only after you've accumulated and analyzed sufficient risk evaluation data. Learn more in [Reviewing risk evaluations](p1_protect_reviewing_risk_evaluations.html). |

## Before you begin

* You must have a PingOne Protect license and add the service to your PingOne environment. Learn more in [Adding the PingOne Protect service to your environment](p1_protect_getting_started.html#add_service) and [Predictors](p1_protect_risk_predictors.html).

|   |                                                                                                                                                                                                           |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | If you have a PingID license only, you can configure a risk policy with limited predictors. Learn more in [Creating a risk policy with an MFA-only license](p1_creating_risk_policies_for_mfa_only.html). |

* [Configure predictors](p1_protect_managing_predictors.html) you want to include in your risk policy.

* Add any applications and user groups you want to use as targets for your risk policy. Learn more in:

  * [Adding an application](../applications/p1_applications_add_applications.html)

  * [Adding non-application-portal applications](../applications/p1_external_apps_not_included_in_apps_portal.html)

  * [Managing groups](../directory/p1_managing_groups.html)

* Configure any MFA policies you want to use in a mitigation rule. Learn more in [Configuring an MFA policy for strong authentication](../strong_authentication_mfa/p1_creating_an_mfa_policy_for_strong_auth.html).

## Steps

1. In the PingOne admin console, go to **Threat Protection > Risk Policies**.

2. Click the tab for the type of policy you want to add:

   * **Global**: A global policy is a legacy risk policy.

   * **Targeted**: A targeted policy allows you to configure a risk policy with conditions, including flow types, user groups, or applications.

3. Click the **[icon: plus, set=fa]**icon to add a risk policy.

   |   |                                                                                                                                                                                                                                                                                                                                                        |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
   |   | You can optionally use the Risk Policy Assistant to create a new global policy and assign different scores to the various predictors to maximize the accuracy of your risk evaluations. The Risk Policy Assistant creates the policy based on your answers to questions about your use case. To launch the Risk Policy Assistant, click **Assistant**. |

4. For **Name**, enter a unique name for the risk policy.

5. For targeted policies, in the **Target** section, select targets to use as criteria for when to use this policy:

   | Target           | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
   | ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | **Flow type**    | Select the applicable checkboxes for the type of flows to which this risk policy will be applied:- **Registration**: Initial creation of an account

   - **Authentication**: Standard authentication for sign-on or actions such as a password change

   - **Authorization**: Verification of whether the user is authorized to perform a specific action (for example, a profile change) using tools such as PingOne Authorize

   - **Access**: Verification of whether the user can access the relevant application using tools such as PingAccess

   - **Transaction**: Authentication that occurs for a purchase or other monetary transactionLearn more about flow types in [Risk policy flow types](p1_protect_risk_policies.html#flow-type-recommended-predictors) and in [Risk Evaluations](https://developer.pingidentity.com/pingone-api/protect/risk-evaluations.html) in the PingOne Protect API documentation. |
   | **Applications** | Choose the applications to which this risk policy will be applied:- To apply the risk policy to all current and future applications in your PingOne environment, select the **All Applications** checkbox.

   - To choose specific applications, select the checkboxes for the desired applications in the **Applications** list.Learn more in [Applications](../applications/p1_application_types.html) and [Adding non-application-portal applications](../applications/p1_external_apps_not_included_in_apps_portal.html).                                                                                                                                                                                                                                                                                                                                                                                         |
   | **Groups**       | Choose the user groups to which this risk policy will be applied:- To apply the risk policy to all current and future groups in your PingOne environment, select the **All Groups** checkbox.

   - To choose specific groups, select the checkboxes for the desired groups in the **Groups** list.Learn more in [Groups](../directory/p1_groups.html).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |

6. For **Predictor Scores**, map the risk level for each predictor to a score.

   * To add a predictor, click **[icon: plus, set=fa]Add Predictor**, select the predictor type in the **Risk Model** list, and set the score. The maximum score is 100.

     |   |                                                                                                                                                                                                            |
     | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
     |   | Only predictors you've configured already show in the **Risk Model** list. Learn more about configuring a new predictor to add in a risk policy in [Adding predictors](p1_protect_adding_predictors.html). |

   * To delete a predictor, click the **Delete** icon.

   ### Example:

   If the risk level for the IP velocity predictor is calculated as **Medium**, you can assign a score of 50. For **High** risk level, you can assign a score of 75.

7. For **Risk thresholds**, set the total risk score to be considered **High** and **Medium** final risk levels.

8. Configure overrides or mitigations for your risk policy:

   * **Risk level Override**: For global policies, set rules that take priority over the calculated final risk level for a policy if the condition is met.

     You can create an override rule to assign the final risk level for the policy as high if the calculated risk level for the bot detection predictor results in medium.

     1. In the **Rules** section, select **Risk level Override**.

     2. To add a new override, click **[icon: plus, set=fa]Add Rule**.

     3. In the **Risk Model** list, select a predictor type or condition.

     4. In the **Score** list, select the overall risk level for the selected predictor that this rule will override.

        In the previous example, you would select **Medium** for **Score** if you want to create a rule to return **High** for the policy when the selected predictor risk level is calculated as medium.

     5. In the **Return** list, select the final risk level to return for the overall policy when the condition you selected for **Score** is met.

        In the previous example, you would select **High** to create an override rule that returns high for the overall policy risk level if the selected predictor risk level is calculated as **Medium**.

     6. (Optional) For **Notes**, you can enter text that's returned in the risk evaluation response.

   * **Mitigation**: Define custom recommended actions to be included in the risk evaluation response with the calculated risk levels. Mitigation rules are evaluated in order from top to bottom and stop processing at the first match. Order mitigation rules from smallest to largest scope so that a broad rule doesn't prevent more specific rules from being evaluated. Only the first matching rule triggers, and all rules below it are skipped.

     When the conditions are met, the mitigation is returned in the risk evaluation response as the value for `result.mitigations[].action`. Learn more in [Targeted risk policies](https://developer.pingidentity.com/pingone-api/protect/risk-policies.html#targeted-risk-policies) in the PingOne Protect API documentation.

     1. In the **Rules** section, select **Mitigation**.

     2. To add a new action, click **[icon: plus, set=fa]Add**.

     3. In the **Rule** list, select criteria for which to create a recommended action, such as a predictor, risk level, or risk score.

     4. For **Operator**, select the applicable operator for the rule you want to create.

     5. For **Value** or **Level**, select criteria based on the **Rule** you selected.

     6. In the **Returned Action** list, select the action to recommend when the conditions for this rule are met.

     7. (Optional) For **Notes**, you can enter text that is returned in the risk evaluation response.

        ### Example:

        You can select **MFA** to define a custom action to prompt the user to complete MFA if the conditions are met. When you select **MFA**, you can also choose an **MFA policy for Authentication** and **MFA policy for Registration** to use when prompting the user to complete MFA. When the conditions of this rule are met, a mitigation of `MFA` is returned in the risk evaluation response as the value for `result.mitigations[].action`. Learn more in [Targeted risk policies](https://developer.pingidentity.com/pingone-api/protect/risk-policies.html#targeted-risk-policies) in the PingOne Protect API documentation.

   ![A screen capture of a new mitigation rule for when Geovelocity Anomaly equals True to recommend MFA.](_images/p1-protect-mitigation-rule.png)

9. Click **Apply**.

## Best practice: Mitigation rule ordering

Use the following examples for guidance when configuring mitigation rules. Order mitigation rules from smallest to largest scope so that a broad rule doesn't prevent more specific rules from being evaluated. Only the first matching rule triggers, and all rules below it are skipped.

### Less effective order

The following mitigation rules are ordered with the largest scope first, causing processing to stop before all rules are evaluated:

1. When the policy risk level equals High, deny the user.

2. When the Adversary in the Middle (AitM) predictor equals high risk level, deny and suspend the user.

3. When the Bot Detection predictor equals high risk level, set a custom recommended action.

With this ordering, rules 2 and 3 never trigger because the evaluation stops at the first match (rule 1). Because rule 1 is a broad condition, the more specific AitM and Bot Detection predictor rules aren't triggered.

### Recommended order

Using the same rules from the previous example, order mitigation rules from smallest to largest scope so that a broad rule doesn't prevent more specific rules from being evaluated:

1. When the AitM predictor equals high risk level, deny and suspend the user.

2. When the Bot Detection predictor equals high risk level, set a custom recommended action.

3. When the policy risk level equals High, deny the user.

![A screen capture of three mitigation rules from the described example.](_images/p1-protect-risk-policy-mitigation-example.png)

## Next steps

In the **Targeted Policies** list, you can click **Reorder** to change the order that policies are evaluated during risk evaluations. Policies are processed in the order displayed in the **Targeted Policies** list. Processing stops when the target criteria for a policy are met. You can drag the policies in the **Set Policy Priority** list to change the order in which the policies are evaluated and click **Save**.

Before modifying an existing risk policy in use, create a staging policy to test how the changes will affect risk evaluations. Learn more in [Creating and managing staging policies](p1_protect_creating_managing_staging_policies.html).

---

---
title: Adding composite predictors
description: Use PingOne Protect composite predictors to combine multiple risk predictors and factors into a single predictor.
component: pingone
page_id: pingone:threat_protection_using_pingone_protect:p1_protect_adding_composite_predictors
canonical_url: https://docs.pingidentity.com/pingone/threat_protection_using_pingone_protect/p1_protect_adding_composite_predictors.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: March 5, 2025
section_ids:
  condition-options: Condition options
  example-scenario: Example scenario
  steps: Steps
  example: Example:
  p1_protect_composite_use_cases: Example use cases
  next-steps: Next steps
---

# Adding composite predictors

Each of the standard risk predictors represents a single risk factor. Use composite predictors to combine a number of risk predictors and factors into a single predictor, such as when you're concerned about the use of an anonymous network only when a user location anomaly is also reported.

## Condition options

You decide what level of risk you want to assign when the various conditions defined in the composite predictor are and aren't met. Composite predictors can include both the standard predictor types provided and any custom predictors you created.

In addition to default and custom predictors, you can include the following risk factors in composite predictors:

* Country

* State

* IP

* IP range

* IP domain organization

* Internet service provider (ISP)

* Rule IDs for the Bot Detection, Traffic Anomaly, and Suspicious Device predictors

* Target resource name (target application)

* User groups

* User ID

* User name

## Example scenario

You want the Geovelocity Anomaly predictor to ignore a long list of IP addresses. The allow list can include up to 400 IP addresses for one predictor. If you need more than 400 IP addresses, you can add another Geovelocity Anomaly predictor, combine the two predictors in a composite predictor (using the **All** operator), and add the composite predictor in the risk policy.

## Steps

1. In the PingOne admin console, go to **Threat Protection > Predictors**.

2. To add a new predictor, click the **[icon: plus, set=fa]**icon.

3. For the predictor type, choose **Composite**.

4. In the **Display Name** field, enter a name for the predictor.

   The display name is used in the Threat Protection Dashboard and policy configuration.

5. In the **Compact Name** field, enter a short name that's returned in the API response.

   |   |                                                          |
   | - | -------------------------------------------------------- |
   |   | You can't change the compact name after it's been saved. |

6. To determine the conditions for each set of criteria, use **All**, **Any**, or **None**.

   You can also nest sets of conditions.

7. Select a predictor type or risk factor, select an operator, and enter or select the value.

   * To use one value as the criterion, such as a single country, use the **Equals** or **Not Equals** operators.

   * To specify multiple values, such as a group of countries, use the **Is In** or **Not In** operators.

   * To use **Bot Detection Rule ID**, **Suspicious Device Rule ID**, or **Traffic Anomaly Rule ID**, use the **Is In** or **Not In** operators and select specific rules to create overrides when those rules are triggered in the risk evaluation. This allows for fine-grained control and is useful when a specific rule causes legitimate authentication attempts to be labeled as high risk. Learn more in [Predictor rules](p1_protect_predictor_rules.html).

   * If you're using **User Groups** as a criterion, use the **Is In** or **Not In** operators to specify any number of groups and enter the names of the PingOne user groups to check what PingOne user groups the user belongs to.

     |   |                                                                                                                                                                                                |
     | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
     |   | When you use the **Is In** or **Not In** operators to define a set of possible values for a risk factor that takes free text, such as **State**, provide the values as a comma-separated list. |

   * If you're using **User ID** or **User Name** as a criterion, you can also use the **Contains** operator, which checks whether the user ID or user name includes the specified substring. For example, you could check whether the user ID contains a certain domain name. The **Contains** operator isn't case-sensitive.

8. To add additional criteria, click **[icon: plus, set=fa]Item** to add a new criteria item, or **[icon: plus, set=fa]Group** to add a new group of criteria.

   |   |                                                                                                                                                                                                                          |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
   |   | If the **[icon: plus, set=fa]Item** and **[icon: plus, set=fa]Group** buttons are grayed out, it's an indication that you've reached the maximum number of criteria items that can be included in a composite predictor. |

9. For **Risk Level Equals**, select **Low**, **Medium**, or **High** to determine the risk level result when the set of criteria is met.

   ### Example:

   In addition to taking into account the results of multiple individual risk predictors, you can include conditions that relate to the total number of predictors in a policy that were low, medium, or high risk.

   For example, you can create a composite predictor that specifies that the predictor should get a result of high risk if any of the following conditions are true:

   * **IP Reputation** is high risk.

   * **IP Velocity** is high risk.

   * Any three predictors in the policy being evaluated are found to be high risk.

10. (Optional) Add additional conditions to evaluate if the first set of conditions is not met.

    |   |                                                               |
    | - | ------------------------------------------------------------- |
    |   | Predictor conditions are applied in order from top to bottom. |

11. Click **[icon: plus, set=fa]Else**.

    1. Configure the criteria and the risk level.

       |   |                                                                            |
       | - | -------------------------------------------------------------------------- |
       |   | You can configure up to three sets of conditions in a composite predictor. |

    2. (Optional) To configure the risk level result to assign if none of the defined conditions is met, select **Low**, **Medium**, or **High** for **Else Return** at the bottom of the page.

       |   |                                                    |
       | - | -------------------------------------------------- |
       |   | The default value for **Else Return** is **None**. |

    ![A screen capture of a composite predictor with 2 sets of conditions.](_images/pwu1695069121911.png)

12. Click **Save**.

## Example use cases

The following table lists example use cases and how to set up composite predictors to support them:

| Use case                 | Operator | Filter example                                                            | Risk level |
| ------------------------ | -------- | ------------------------------------------------------------------------- | ---------- |
| Deny list for countries  | **Any**  | **Country Equals United States****Country Equals United Kingdom**         | **High**   |
| Allow list for countries | **All**  | **Country Not Equals United States****Country Not Equals United Kingdom** | **Low**    |
| Ignore users             | **Any**  | **User Name Equals** `testuser123`**User Name Equals** `qa_test`          | **Low**    |
| Non-routable IPs         | **Any**  | **IP Is In** `10.0.0.0/8,172.16.0.0/12,192.168.0.0/16`                    | **Medium** |

## Next steps

After a composite predictor yields a result, you can use the result in the same ways as the results of individual risk predictors:

* You can assign the predictor a score to be used with the other predictors in your risk policy to calculate a final risk level.

* You can define an override that uses the composite predictor so that in cases where the predictor conditions are met, you can directly assign a final risk level and ignore the other predictors in the risk policy.

---

---
title: Adding custom predictors
description: Custom predictors allow you to include data not represented by any of the out-of-the-box PingOne Protect predictors.
component: pingone
page_id: pingone:threat_protection_using_pingone_protect:p1_protect_adding_custom_predictors
canonical_url: https://docs.pingidentity.com/pingone/threat_protection_using_pingone_protect/p1_protect_adding_custom_predictors.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: February 19, 2025
section_ids:
  steps: Steps
  choose-from: Choose from:
---

# Adding custom predictors

Custom predictors allow you to include risk-related data that isn't represented by any of the out-of-the-box risk predictors that PingOne Protect provides.

The data for a custom predictor can be:

* Information that PingOne Protect has, but isn't included in one of the standard predictors, such as the country where the user trying to access the resource is currently located

* External risk-related data that you provide as input, such as information on managed and unmanaged devices from PingFederate

You can define three types of custom risk predictors:

* IP range: Definition of risk levels associated with different IP ranges

* String matching: Definition of risk levels associated with different values of input provided as a string

* Numeric range: Definition of risk levels associated with different values of input provided as a number

Custom predictors are treated like the out-of-the-box predictors in terms of:

* Being able to add them to risk policies

* Viewing data for the predictors in the **Threat Protection Dashboard**

* Inclusion of the data in PingOne Audit logs

You can add a maximum of 15 custom predictors per environment.

## Steps

1. In the PingOne admin console, go to **Threat Protection > Predictors**.

2. To add a new predictor, click the **[icon: plus, set=fa]**icon.

3. For the predictor type, select **Custom**.

4. In the **Display Name** field, enter a name for the predictor.

   The display name is used in the **Threat Protection Dashboard** and policy configuration.

5. In the **Compact Name** field, enter a short name that will be returned in the API response.

   |   |                                                          |
   | - | -------------------------------------------------------- |
   |   | You can't change the compact name after it's been saved. |

6. The **Attribute Mapping** field is used to point to the variable that will contain the data that's being used to determine high, medium, or low risk for the predictor. The field can take any of the following types of data:

   ### Choose from:

   * One of the fields included in the `details` object returned in the API response for risk evaluations, such as `details.country`. In this case, you would enter `${details.country}` in the **Attribute Mapping** field.

   * One of the fields included in the `event` object included in the API request for risk evaluations, such as `event.browser.userAgent`. In this case, you would enter`${event.browser.userAgent}` in the **Attribute Mapping** field.

   * Data that you're providing from an external source. You provide the data by including a new field in the `event` object in the `Create risk evaluation` API request, for example, `event.managedDevice`. In this case, you would enter `${event.managedDevice}` in the **Attribute Mapping** field.

     Learn more about the fields included in the `details` and `event` objects in the Details data model and Event data model tables in the [Risk evaluation section](https://developer.pingidentity.com/pingone-api/protect/risk-evaluations.html) of the PingOne API documentation.

     |   |                                                                                                                                                                                                                                                 |
     | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
     |   | If you defined a flow in DaVinci where custom attributes are provided as input to the risk evaluation, you must add `customAttributes` after `event` in the **AttributeMapping** field. For example, `${event.customAttributes.managedDevice}`. |

7. In the **Fallback Predictor Decision Value** list, select a default risk level to use in case the attribute isn't provided.

8. In the **Risk Level Mapping** section:

   1. Select the type of input that's being provided for the comparison:

      * **Range** for numeric range input

      * **IP Ranges** for IP range input

      * **List Item** for string-matching input

   2. Enter the values that will be considered **Low**, **Medium**, and **High** risk.

      1. For string matching, enter one string in each text field.

      2. Click **Add List Item** if you want to provide more than one string for any of the three risk levels.

         |   |                                                                                                                                                                                                                                                                                                                                                                                                                         |
         | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
         |   | * If a value appears in more than one of the risk categories (**Low**, **Medium**, **High**), the more strict risk category is used for the value.

         * For numeric input, the input is assigned to a specific risk level (**Low**, **Medium**, **High**) if it's greater than or equal to the **Min** value and less than the **Max** value.

         * For a string-matching custom predictor, you can define up to 50 strings. |

9. Click **Save**.

---

---
title: Adding predictors
description: Add additional predictors to a PingOne Protect risk policy to identify possible fraudulent user behaviors.
component: pingone
page_id: pingone:threat_protection_using_pingone_protect:p1_protect_adding_predictors
canonical_url: https://docs.pingidentity.com/pingone/threat_protection_using_pingone_protect/p1_protect_adding_predictors.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: March 5, 2025
section_ids:
  steps: Steps
---

# Adding predictors

Add additional predictors to a risk policy to identify possible fraudulent user behaviors.

PingOne Protect allows you to add additional predictors to the out-of-the-box predictors in a risk policy. You can add custom predictors, composite predictors, and additional versions of certain out-of-the-box predictors. Learn more in [Predictors](p1_protect_risk_predictors.html), [Adding custom predictors](p1_protect_adding_custom_predictors.html), and [Adding composite predictors](p1_protect_adding_composite_predictors.html).

When you create a new predictor, it's included by default in any subsequent risk policies you create.

When creating predictors, consider the following points regarding the relationship between the **Predictors** page and the **Risk Policies** page:

* When you create a new environment, it includes a default risk policy.

* When you first go to the **Predictors** page, you see the predictors that are included in the default risk policy.

* When you customize predictors, you see the change immediately in any risk policies that use the predictors that you modified.

* When you create new predictors, you can use them when you update existing risk policies or when you create new risk policies.

Most out-of-the-box predictors have settings you can configure. Learn more in [Configuring predictors](p1_protect_managing_predictors.html).

For most scenarios, you don't need to add additional out-of-the-box predictors, but there could be specific circumstances when you need to add them. As an example scenario, you have a different risk policy for different user populations: one group of users travels frequently, and the other group never travels. In this scenario, you can add two **User Location Anomaly** predictors, each configured with a different radius distance and use the two predictors in different risk policies.

To add predictors:

## Steps

1. In the PingOne admin console, go to **Threat Protection > Predictors**.

2. To add a new predictor, click the **[icon: plus, set=fa]**icon.

3. For **Predictor**, choose the predictor type you want to add.

   |   |                                                                    |
   | - | ------------------------------------------------------------------ |
   |   | You can only add additional predictors of certain predictor types. |

4. In the **Display Name** field, enter a name for the predictor.

   The display name is used in the **Threat Protection Dashboard** and policy configuration.

5. In the **Compact Name** field, enter a short name that is returned in the API response.

   |   |                                                          |
   | - | -------------------------------------------------------- |
   |   | You can't change the compact name after it's been saved. |

6. [Configure the predictor](p1_protect_managing_predictors.html).

7. Click **Save**.

---

---
title: Best practices for PingOne Protect
description: Use these best practices to get the most out of PingOne Protect.
component: pingone
page_id: pingone:threat_protection_using_pingone_protect:p1_protect_best_practices
canonical_url: https://docs.pingidentity.com/pingone/threat_protection_using_pingone_protect/p1_protect_best_practices.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: April 4, 2024
section_ids:
  risk-policies: Risk policies
  risk-evaluation-results: Risk evaluation results
  predictors: Predictors
  signals-protect-sdk: Signals (Protect) SDK
  flows-in-davinci: Flows in DaVinci
---

# Best practices for PingOne Protect

Follow these recommendations to get the most out of PingOne Protect.

## Risk policies

* When you add the PingOne Protect service to a PingOne environment, it includes a default risk policy. You should use this policy for your initial testing of risk evaluations. After you've seen how this default policy affects the flow experience for your users, you can go back and fine-tune it by customizing individual predictors. You can also create multiple risk policies.

* Train risk models with production data for 1 - 3 weeks for workforce usage or 2 - 4 weeks for customer usage. This should be done with the default risk policy.

* Use the PingOne Protect dashboards to analyze the risk evaluation results. Identify false positive results, meaning situations that are identified as High risk even though they are interactions with legitimate users.

  Identify the causes of these false positives. Adjust the scores for the different risk predictors in the risk policy to try to reduce the incidence of false positives.

* Use score-based policies rather than weight-based policies. Score-based policies provide more control over the overall calculation because you can specify an exact numerical score that should be assigned when PingOne Protect determines that there is a medium or high-risk level for a predictor.

  |   |                                                                                                                                |
  | - | ------------------------------------------------------------------------------------------------------------------------------ |
  |   | **Weights** in risk policies have been deprecated for new PingOne environments but can still be used in existing environments. |

* Define and review risk thresholds deliberately. The thresholds you set in the risk policy determine how the numerical risk score is translated to Low, Medium, or High, so tune thresholds to align with your organization's security posture and business requirements.

* Align the predictors you add to a risk policy with the flow type. Refer to the following table for guidance on the predictors to use in risk policies for the most common flow types:

  | Flow type      | Description                                                                                | Predictors                                                                                                                                                                                                                                                                                                                            |
  | -------------- | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  | Registration   | Initial creation of an account                                                             | Focus on new account fraud:- Anonymous Network Detection

  - Bot Detection

  - Email Reputation

  - IP Reputation

  - Suspicious Device

  - Traffic Anomaly

  - User Velocity                                                                                                                                                               |
  | Authentication | Standard authentication for sign-on                                                        | Focus on returning-user sign-ons:- Adversary-in-the-Middle

  - Anonymous Network Detection

  - Bot Detection

  - Geovelocity Anomaly

  - IP Reputation

  - IP Velocity

  - New Device

  - PingID Device Trust (workforce only)

  - Suspicious Device

  - Traffic Anomaly

  - User-Based Risk Behavior

  - User Location Anomaly

  - User Velocity |
  | Transaction    | Sensitive transactions, such as profile changes, monetary transactions, or account linking | Use the same predictors as the authentication flow type but define them separately to improve audit and reporting clarity.                                                                                                                                                                                                            |

* Before modifying an existing risk policy that is in use, use a staging policy to test how the changes will affect risk evaluations.

* When configuring mitigation rules, order them from smallest to largest scope so that a broad rule doesn't prevent more specific rules from being evaluated. Mitigation rules are evaluated top to bottom and stop processing at the first match. After the first match is triggered, all rules below it are skipped.

## Risk evaluation results

When a risk evaluation is performed, the PingOne API returns detailed information in addition to the overall risk level that was calculated on the basis of the risk policy used. This information includes data about the event, the user and the device used, and the risk results for the individual predictors in the risk policy. You can take these supplemental details into account when determining how to proceed in the flow.

When deciding how a flow should proceed based on the risk evaluation response, consider:

* The type of flow, such as initial registration, ordinary authentication to access an application, or authentication prior to a monetary transaction

* The specific risk factors included in the risk policy that was used

* The type of business need, such as security needs versus need for less friction in the user experience, or the frequency of fraud instances

* The various risk mitigation tools you have available, such as multi-factor authentication (MFA) or knowledge-based authentication (KBA)

You can also use the detailed information in the response to better understand what led to the overall risk level and then fine-tune your risk policies.

The following are the key details returned in the response, ordered by level of importance.

| Response detail            | Recommendation                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| -------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `result.recommendedAction` | In some cases, a specific course of action is recommended. For example, when the calculated risk level is HIGH and a bot is suspected, there is a recommendation to carry out the additional bot mitigation steps that your organization has available.                                                                                                                                                                                                                                                                                                                                                                                                              |
| `result.value`             | This field has a value only if you defined an override in your policy and included text in the **Notes** section.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| `result.level`             | The overall risk level calculated.- When the risk level is equal to Low, the flow should probably continue without providing any additional friction for the user.

- When the risk level is equal to Medium, an MFA challenge should probably be issued, although in some scenarios, you may decide that even at this level there is no need for any additional friction.

- When the risk level is equal to High, you should present a challenge stronger than an ordinary MFA push.&#xA;&#xA;Because there are conditions where a High risk level will be returned even for legitimate users, you should probably not block a user completely in such situations. |
| `result.score`             | The raw risk score before the conversion to the Low, Medium, or High risk level. This provides a higher degree of granularity, and you can check how much the score exceeds the thresholds used for converting to risk level.                                                                                                                                                                                                                                                                                                                                                                                                                                        |

## Predictors

* Ordinarily, you don't need more than one predictor of each type. However, when you have different types of users, you might want to have multiple versions of the predictor so that you can use different versions in different risk policies.

  For example, if you have users who travel frequently, you could create one User Location Anomaly predictor that assigns a risk level of High if a user authenticates from outside the radius that you defined and create a second, more lenient User Location Anomaly predictor that can be applied to the users who travel frequently.

* If you use composite predictors, it will usually be to combine multiple types of predictors when you're interested in the interaction between them, such as assigning a risk level of High for authentications from an anonymous network only if there's also a User Location Anomaly.

  However, there are situations where you want to combine multiple predictors of the same type. For example, a Geovelocity predictor allows you to compose an allow list of up to 400 IPs. To compose a larger list of allowed IPs, you can create a composite predictor that contains two different Geovelocity predictors.

* Review and set predictor retention periods to determine how long data is stored for specific predictors that rely on historical context. Learn more in [Protect Settings](p1_protect_general_protect_settings.html).

## Signals (Protect) SDK

* Implement the Signals (Protect) SDK in your applications. Certain risk predictors, such as the Bot Detection and New Device predictors, rely on the supplemental risk-related information supplied by the Signals SDK.

* Use modern, supported browsers for interactions that include the Signals SDK. If your deployment includes legacy embedded browsers, refer to [Troubleshooting embedded browser issues](p1_protect_troubleshooting.html#p1_protect_embedded_browsers) for guidance.

## Flows in DaVinci

* Each flow where you include a risk evaluation should include two different PingOne Protect connectors:

  * Add a connector with the `Create Risk Evaluation` capability at a point in the flow where you want to base the next action on the risk score assigned. For example, show an MFA prompt for MEDIUM or HIGH, but automatically grant access if the risk is deemed Low.

  * Add a connector with the `Update Risk Evaluation` capability at a point in the flow after authentication has been completed. This capability represents the system's ability to learn over time in order to improve results. Always include an update connector in your flows because the learning mechanism is essential for risk evaluation precision.

* Use the `skrisk` component in your flow to automatically obtain the information from the Signals SDK.

  |   |                                                                                                                                                                                                                                                                                                                                                           |
  | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | This approach can only be used for web applications. For iOS or Android apps, you must manually implement the steps described in the [SDK documentation](https://developer.pingidentity.com/pingone-api/native-sdks/pingone-risk-sdks/risk_evaluation_sdk.html), and then include in your flow a variable that represents the data obtained from the SDK. |

* In the HTTP connector that you add before the connector that creates the risk evaluation, make sure that the `skrisk` component is at the beginning of the HTML template. All HTML tags that you add should be below the `skrisk` component in the **HTML Template** field.

---

---
title: Browser distribution
description: View risk evaluations by browser family in the PingOne Protect Browser Distribution dashboard chart.
component: pingone
page_id: pingone:threat_protection_using_pingone_protect:p1_protect_browser_distribution
canonical_url: https://docs.pingidentity.com/pingone/threat_protection_using_pingone_protect/p1_protect_browser_distribution.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: February 19, 2025
---

# Browser distribution

The **Browser Distribution** chart shows the number of recorded risk evaluations by user browser family.

To access the **Browser Distribution** chart, go to **Monitoring > Threat Protection**.

![A screen capture of the Browser distribution graph. The legend is directly above the chart. The Filters and Date Range sections are on the left side of the graph, and the monitored risk data table is below it.](_images/pko1612372689454.png)

The drill-down table shows more detailed information about each risk evaluation event, such as IP address and target application.

Scroll to the right to see additional columns. Learn more about using the filtered search bar in [Filtered searching](p1_protect_dashboard.html#section_dpy_gqs_h4b).

You can click a column header to sort the results by that value. Results are sorted by the **Time** column by default, with the most recent entries listed first.

---

---
title: Configuring predictors
description: You can configure and edit the settings for PingOne Protect predictors at any time.
component: pingone
page_id: pingone:threat_protection_using_pingone_protect:p1_protect_managing_predictors
canonical_url: https://docs.pingidentity.com/pingone/threat_protection_using_pingone_protect/p1_protect_managing_predictors.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: February 21, 2025
section_ids:
  steps: Steps
---

# Configuring predictors

You can configure and edit details and configuration settings for out-of-the-box, custom, and composite predictors at any time.

Most predictor types allow you to define a **Fallback Predictor Decision Value**, which is the risk level that should be assigned to the predictor if there's insufficient information to calculate the risk level. This can occur for a number of reasons, such as:

* The predictor is still in the training period.

* The basic information required (for example, the location of the user) can't be obtained.

Learn more in [Predictors](p1_protect_risk_predictors.html).

## Steps

1. In the PingOne admin console, go to **Threat Protection > Predictors**.

2. Click the predictor type to expand the predictor list, then click the specific predictor that you want to edit.

3. Edit the predictor details and configuration settings:

   * To edit **Display Name** and **Description**, click the **More Options** (⋮) icon and click **Rename**.

   * To edit configuration settings, click the **Pencil** icon ([icon: pencil, set=fa]) and edit any of the following:

     | Predictor                          | Settings                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
     | ---------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
     | **Adversary-in-the-Middle (AitM)** | Use the **Fallback Predictor Decision Value** list to select the risk level that this predictor should be assigned if there's insufficient information to calculate the risk level.Use the **Domain Allow List** field to provide a comma-separated list of the domains that are legitimate for your resources. These will be compared with the domains that your users are trying to access to verify that they were not the target of phishing attempts.If you don't specify one or more domains, PingOne Protect sets a short learning period to learn the domains that your users are accessing, and these domains are added to the allow list. The learned domains are displayed under **Domain Allow List**.                                                                                                                                                                                                                                            |
     | **Anonymous Network Detection**    | Use the **Fallback Predictor Decision Value** list to select the risk level that this predictor should be assigned if there's insufficient information to calculate the risk level.In the **Allow List** field, enter the IP addresses for which anonymous network considerations should be ignored. This must be one or more ranges of IP addresses in classless inter-domain routing (CIDR) *(tooltip: \<div class="paragraph">&#xA;\<p>A method for allocating IP addresses and for IP routing.\</p>&#xA;\</div>)* format, separated by commas, for example, `1.1.1.1/24, 1.1.2.1/12`. For IP addresses in IPv4 format, you can use IP ranges. For IP addresses in IPv6 format, you must add each address to the list individually.                                                                                                                                                                                                                        |
     | **Bot Detection**                  | Use the **Fallback Predictor Decision Value** list to select the risk level that this predictor should be assigned if there's insufficient information to calculate the risk level.Use the **Track events without SDK payload** option to expand the types of bot activity that PingOne Protect can detect. To use this option, you must configure the [PingOne Signals (Protect) SDK](https://developer.pingidentity.com/pingone-api/native-sdks/pingone-risk-sdks/risk_evaluation_sdk.html) to pass the SDK payload into the risk evaluation.Use the **Excluded Rules** list to exclude specific rules from risk level results. Learn more in [Predictor rules](p1_protect_predictor_rules.html).                                                                                                                                                                                                                                                           |
     | **Email Reputation**               | Use the **Fallback Predictor Decision Value** list to select the risk level that this predictor should be assigned if there's insufficient information to calculate the risk level.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
     | **Geovelocity**                    | Use the **Fallback Predictor Decision Value** list to select the risk level that this predictor should be assigned if there's insufficient information to calculate the risk level.In the **Allow List** field, enter the IP addresses for which anonymous network considerations should be ignored. This must be one or more ranges of IP addresses in CIDR format, separated by commas, for example, `1.1.1.1/24, 1.1.2.1/12`. For IP addresses in IPv4 format, you can use IP ranges. For IP addresses in IPv6 format, each address must be added to the list individually.                                                                                                                                                                                                                                                                                                                                                                                |
     | **IP Reputation**                  | Use the **Fallback Predictor Decision Value** list to select the risk level that this predictor should be assigned if there's insufficient information to calculate the risk level.In the **Allow List** field, enter the IP addresses for which anonymous network considerations should be ignored. This must be one or more ranges of IP addresses in CIDR format, separated by commas, for example, `1.1.1.1/24, 1.1.2.1/12`. For IP addresses in IPv4 format, you can use IP ranges. For IP addresses in IPv6 format, each address must be added to the list individually.                                                                                                                                                                                                                                                                                                                                                                                |
     | **IP Velocity**                    | You can't configure settings for the **IP Velocity** predictor.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
     | **New Device**                     | Use the **Fallback Predictor Decision Value** list to select the risk level that this predictor should be assigned if there's insufficient information to calculate the risk level.Use the **Activation Date** field to specify a date when the learning process for the predictor should be restarted and all devices identified before this date should be ignored. You can use this in conjunction with the fallback setting to force strong authentication when moving the predictor to production.&#xA;&#xA;Activation Date uses UTC time.                                                                                                                                                                                                                                                                                                                                                                                                               |
     | **PingID Device Trust**            | Use the **Fallback Predictor Decision Value** list to select the risk level that this predictor should be assigned if there's insufficient information to calculate the risk level.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
     | **Suspicious Device**              | Use the **Fallback Predictor Decision Value** list to select the risk level that this predictor should be assigned if there's insufficient information to calculate the risk level.Use the **Signed SDK Payload is Required** option to specify that the predictor requires that the payload from the Signals (Protect) SDK be provided as a signed JSON Web Token (JWT).&#xA;&#xA;Before selecting this option for your predictor, verify that you've enabled the option to have the SDK payload provided as a signed JWT in the initialization code for the SDK. If you're using DaVinci flows, you can enable the signed JWT option when configuring the skrisk component in your flows. Learn more in the documentation for the web version of the Signals SDK and PingOne Protect DaVinci connector.Use the **Excluded Rules** list to exclude specific rules from risk level results. Learn more in [Predictor rules](p1_protect_predictor_rules.html). |
     | **Traffic Anomaly**                | Use the **Fallback Predictor Decision Value** list to select the risk level that this predictor should be assigned if there's insufficient information to calculate the risk level.Use the **Users per Device** option to set the maximum number of users per device to be considered **Medium** and **High** risk for the specified timeframe.Use the **Excluded Rules** list to exclude specific rules from risk level results. Learn more in [Predictor rules](p1_protect_predictor_rules.html).                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
     | **User Location Anomaly**          | Use the **Fallback Predictor Decision Value** list to select the risk level that this predictor should be assigned if there's insufficient information to calculate the risk level.Enter the radius **Distance** and select the **Measurement** units (miles or kilometers).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
     | **User-Based Risk Behavior**       | Use the **Fallback Predictor Decision Value** list to select the risk level that this predictor should be assigned if there's insufficient information to calculate the risk level.Use the **Detect compromised user accounts** option to specify that PingOne Protect should attempt to detect compromised user accounts and take this into account when calculating the risk level for this predictor.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
     | **User Velocity**                  | You can't configure settings for the **User Velocity** predictor.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |

4. Click **Save**.

---

---
title: Creating a risk policy with an MFA-only license
description: There are various prerequisites you should be aware of when creating a workforce risk policy for user authentication. This section guides you through the steps needed.
component: pingone
page_id: pingone:threat_protection_using_pingone_protect:p1_creating_risk_policies_for_mfa_only
canonical_url: https://docs.pingidentity.com/pingone/threat_protection_using_pingone_protect/p1_creating_risk_policies_for_mfa_only.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  before-you-begin: Before you begin
  create-applications-and-user-groups: Create applications and user groups
  create-one-or-more-mfa-policies: Create one or more MFA policies
  create-relevant-predictors: Create relevant predictors
  workforce-only-recreate-legacy-pingid-policy-rules: (Workforce only) Recreate legacy PingID policy rules
  create-a-risk-policy-with-an-mfa-only-license: Create a risk policy with an MFA-only license
---

# Creating a risk policy with an MFA-only license

There are various prerequisites you should be aware of when creating a workforce risk policy for user authentication. This section guides you through the steps needed.

## Before you begin

You need to create all the applications, groups, policies, and predictors that you might want to reference in your risk policy.

If you skip this step, they won't be available for you to select when configuring your risk policies.

### Create applications and user groups

* Create any groups to which you want to apply the risk policy.

  Learn more in [Groups](../directory/p1_groups.html).

* Create any applications to which you want to apply the risk policy.

  Learn more in [Applications](../applications/p1_application_types.html) and [Including external groups in an application](../applications/p1_include_external_groups_in_applications.html).

* If you're using PingFederate as your identity provider (IdP), make sure you connect any OIDC applications to your PingFederate instance.

  Learn more in [Editing an application - OIDC](../applications/p1_edit_application_oidc.html).

* (Workforce only) If you migrated your PingID account to PingOne and want to apply PingID policies to a PingOne group, you must first sync the group to PingOne.

  Learn more in [Outbound group provisioning](../integrations/p1_provisioning_outbound_group_provisioning.html) and [Creating a group](../directory/p1_create_group.html).

### Create one or more MFA policies

Create one or more [MFA policies](../strong_authentication_mfa/p1_creating_an_mfa_policy_for_strong_auth.html) that cover the use cases to which you might want to apply a risk policy.

**Example scenarios**:

* Use cases for different departments in your organization, such as Finance, HR, and IT.

* High, medium, and low risk use cases. Create a different MFA policy with different allowed methods for each risk level.

* Different MFA methods, such as an MFA policy for FIDO authentication or an MFA policy for less secure MFA methods, such as SMS or voice.

  Learn more in [Configuring an MFA policy for strong authentication](../strong_authentication_mfa/p1_creating_an_mfa_policy_for_strong_auth.html).

### Create relevant predictors

Create and configure any predictors that might you want to use in your risk policy. You can find a list of predictors that are supported with an MFA-only license in [Risk policies for MFA-only licenses](p1_protect_risk_policies_mfa_only.html).

You can create [composite predictors](p1_protect_adding_composite_predictors.html) to cover more complex scenarios.

|   |                                                                                                   |
| - | ------------------------------------------------------------------------------------------------- |
|   | Within a risk policy, you can only reference predictors that already exist in the predictor list. |

#### (Workforce only) Recreate legacy PingID policy rules

Admins that formerly managed PingID policy through the PingID admin portal can use composite predictors to recreate legacy PingID policy rules.

Examples of useful composite predictors you might want to create include:

* [Allowed or disallowed countries predictor](p1_protect_recreating_legacy_pingid_rules.html)

* [Recent authentication from company network predictor](p1_protect_recreating_legacy_pingid_rules.html)

Learn more about using predictors to recreate legacy PingID policy rules in PingOne in [Using predictors to recreate legacy PingID policy rules](p1_protect_recreating_legacy_pingid_rules.html).

## Create a risk policy with an MFA-only license

Create a risk policy and add the relevant predictors to the mitigations list.

1. In the PingOne admin portal, go to Threat Protection > Risk Policies, and click the **+** icon.

2. Enter a unique name for the risk policy.

3. Select the user groups and applications to which you want the policy to apply.

4. In the **Mitigations** section, for each predictor that you want to add, click **+Add** and select and configure the predictor rules:

   1. Use the **Operator**, **Level**, and **Returned Action** fields to define the action you want, based on the risk level returned by the rule.

   2. If you select **MFA** as the **Returned Action**, configure the following fields:

      * **Authentication**: Select the MFA policy to apply during an authentication flow.

      * **Registration**: Select the MFA policy to apply during a registration flow.

   3. Drag and drop the rules to arrange them in the order you want them to be considered. PingOne evaluates mitigation rules separately in the order they're listed.

   4. Click **Apply**.

      PingOne evaluates risk policies separately by the order in which they're listed in the **Risk Policies** list.

5. (Optional) To change the order in which this policy is evaluated, in the **Risk Policies** list, click **Reorder**, drag the policy to the desired position, and then click **Save**.

---

---
title: Creating and managing staging policies
description: Create and manage staging policies in PingOne Protect to test risk policy changes before promoting them to production.
component: pingone
page_id: pingone:threat_protection_using_pingone_protect:p1_protect_creating_managing_staging_policies
canonical_url: https://docs.pingidentity.com/pingone/threat_protection_using_pingone_protect/p1_protect_creating_managing_staging_policies.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: February 20, 2025
section_ids:
  about-this-task: About this task
  steps: Steps
  result: Result:
  result-2: Result:
---

# Creating and managing staging policies

To test risk policy changes before putting them into production, you can create a staging policy that is associated with the risk policy that you're currently using.

## About this task

When an evaluation event occurs for the production risk policy, the incoming risk data is also passed through the staging policy affiliated with the production policy, creating two sets of risk evaluation data: one for the production policy and one for its associated staging policy.

Staging policies are set to expire after 3 months, and the expiration date is displayed next to the risk policy name.

When a staging policy expires, incoming risk data is no longer passed through the staging policy for evaluation.

![A screen capture of a risk policy with its associated staging policy below it](_images/ejv1663062229897.png)

In the PingOne admin console, go to **Threat Protection > Risk Policies**:

## Steps

* To create a staging policy, click the **More Options** (⋮) icon for the policy and select **Create staging policy**.

  ### Result:

  A policy editing window opens, and you can make the changes that you want to test.

* To promote the staging policy to production, click the **More Options** (⋮) icon for the policy, and select **Promote to production**.

  ### Result:

  When you promote a staging policy to production:

  * The settings in the staging policy are copied to production and replace the production policy settings. The policy name and ID remain the same.

  * The staging policy is deleted from the **Risk Policies** list.

  |   |                                                                        |
  | - | ---------------------------------------------------------------------- |
  |   | A staging policy can be promoted to production even if it has expired. |

* To delete a staging policy, click the **More Options** (⋮) icon and select **Delete**.

---

---
title: Deleting a predictor
description: Delete a custom predictor in PingOne Protect.
component: pingone
page_id: pingone:threat_protection_using_pingone_protect:p1_protect_deleting_predictors
canonical_url: https://docs.pingidentity.com/pingone/threat_protection_using_pingone_protect/p1_protect_deleting_predictors.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: February 19, 2025
section_ids:
  steps: Steps
---

# Deleting a predictor

You can only delete additional predictors that you added. The default predictors can't be deleted.

## Steps

1. In the PingOne admin console, go to **Threat Protection > Predictors**.

2. On the predictor that you want to delete, click the **More Options** (⋮) icon.

3. Click **Delete**.

---

---
title: Editing a risk policy
description: Edit an existing risk policy using PingOne Protect.
component: pingone
page_id: pingone:threat_protection_using_pingone_protect:p1_protect_editing_risk_policy
canonical_url: https://docs.pingidentity.com/pingone/threat_protection_using_pingone_protect/p1_protect_editing_risk_policy.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 2, 2025
section_ids:
  steps: Steps
  next-steps: Next steps
---

# Editing a risk policy

Edit an existing risk policy only after you've accumulated sufficient risk evaluation data and analyzed it so that you can make informed decisions about how to fine-tune your risk policy. Learn more in [Reviewing risk evaluations](p1_protect_reviewing_risk_evaluations.html).

|   |                                                                                                                                                                                                                                            |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | Before modifying an existing risk policy in use, create a staging policy to test how the changes will affect risk evaluations. Learn more in [Creating and managing staging policies](p1_protect_creating_managing_staging_policies.html). |

## Steps

1. In the PingOne admin console, go to **Threat Protection > Risk Policies**.

2. Click the tab for the type of policy you want to edit:

   * **Global**

   * **Targeted**

3. Click the policy you want to edit to open the details panel, then click the **Pencil** icon.

4. Edit the policy configuration settings as needed.

5. Click **Apply**.

## Next steps

In the **Targeted Policies** list, you can click **Reorder** to change the order that policies are evaluated during risk evaluations. Policies are processed in the order displayed in the **Targeted Policies** list. Processing stops when the target criteria for a policy are met. You can drag the policies in the **Set Policy Priority** list to change the order in which the policies are evaluated and click **Save**.

---

---
title: Evaluating staging policy risk data
description: "Test PingOne Protect risk policy changes before putting them into production by creating a staging policy associated with the risk policy that you're currently using."
component: pingone
page_id: pingone:threat_protection_using_pingone_protect:p1_protect_evaluating_staging_policy
canonical_url: https://docs.pingidentity.com/pingone/threat_protection_using_pingone_protect/p1_protect_evaluating_staging_policy.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: March 5, 2025
section_ids:
  before-you-begin: Before you begin
  steps: Steps
  result: Result:
  example: Example:
  next-steps: Next steps
---

# Evaluating staging policy risk data

To test risk policy changes before actually putting them into production, you can create a staging policy associated with the risk policy that you're currently using.

After creating your staging policy, you can view risk data to determine how your policy changes affect end users. View risk data from a staging policy in the **Threat Protection Dashboard**.

## Before you begin

[Create a staging policy](p1_protect_creating_managing_staging_policies.html).

## Steps

1. In the PingOne admin console, go to **Monitoring > Threat Protection**.

2. Click the **Risk Events** graph.

3. Review the total counts above the default graph, which shows only production event types.

   ![A screen capture of Risk Event data with only production event types.](_images/rkz1686777337456.png)

4. Click the **Event Types** dropdown, and select both the **Production** and **Staging** checkboxes.

   ### Result:

   The graph refreshes to display risk event data from both production and staging risk policies.

5. Review the updated total counts to see how your staging policy affects each risk level.

   ![A screen capture of Risk Event data with production and staging event types.](_images/hjk1686777578235.png)

6. Review the data in the drill-down table.

   |   |                                                                                                                                             |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | Only events that have triggered a specific risk predictor, such as geovelocity anomaly, or have an aggregated risk score of high are shown. |

   1. Examine the **Risk Policy** column to determine whether each risk event is associated with the production or staging policy. Check risk events specifically from the staging policy and review how the changes you made affect the data.

      ![A screen capture of risk events.](_images/qnu1686778390080.png)

   2. Scroll across to the **Predictors** column, and click **Details** in any risk event row to review the score for each configured predictor and the reason.

      ### Example:

      If you added the **New Device** predictor in your staging policy and do not use this predictor in your production policy, a risk event is triggered only in the staging policy when a user signs on with a new device. In the **Predictors Details** for this risk event, the **New Device** predictor shows a **High** score because the device has not been used recently. This allows you to test how your changes to the staging policy might affect users with real-time risk data passed from the production policy.

      ![A screen capture of the Predictors Details for a risk event.](_images/gyr1686778117759.png)

## Next steps

Make any further adjustments to your staging policy if needed. After evaluating your staging policy, you can decide whether to [promote the staging policy to production](p1_protect_creating_managing_staging_policies.html).

---

---
title: Getting started with PingOne Protect
description: Prevent account takeover, new account fraud, and MFA and password fatigue with PingOne Protect.
component: pingone
page_id: pingone:threat_protection_using_pingone_protect:p1_protect_getting_started
canonical_url: https://docs.pingidentity.com/pingone/threat_protection_using_pingone_protect/p1_protect_getting_started.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: March 5, 2025
section_ids:
  threat-protection-dashboard: Threat Protection Dashboard
  how-pingone-protect-works: How PingOne Protect works
  essential_concepts: Key concepts
  intro_risk_policies: Introduction to risk policies
  the-default-risk-policy: The default risk policy
  staging-policies: Staging policies
  custom-risk-policies: Custom risk policies
  intro_predictors: Introduction to predictors
  intro_risk_evaluations: Introduction to risk evaluations
  intro_api_risk_evaluations: Introduction to using the PingOne API for risk evaluations
  try_sample_app: Trying PingOne Protect with a sample app
  before-you-begin: Before you begin
  about-this-task: About this task
  steps: Steps
  result: Result:
  result-2: Result:
  get_up_running: Getting up and running
  add_service: Adding the PingOne Protect service to your environment
  before-you-begin-2: Before you begin
  steps-2: Steps
  result-3: Result
  p1_protect_integrate: Integrating PingOne Protect with user journeys
  before-you-begin-3: Before you begin
  steps-3: Steps
  using-the-pingone-protect-integration-kit-with-pingfederate: Using the PingOne Protect Integration Kit with PingFederate
  before-you-begin-4: Before you begin
  steps-4: Steps
  choose-from: Choose from:
  building-a-custom-flow-with-pingone-davinci: Building a custom flow with PingOne DaVinci
  before-you-begin-5: Before you begin
  about-this-task-2: About this task
  steps-5: Steps
  troubleshooting: Troubleshooting
  using-the-pingone-api: Using the PingOne API
  about-this-task-3: About this task
  steps-6: Steps
  integrating-with-pingone-advanced-identity-cloud: Integrating with PingOne Advanced Identity Cloud
  before-you-begin-6: Before you begin
  about-this-task-4: About this task
  steps-7: Steps
  getting-input-from-the-pingone-signals-protect-sdk: Getting input from the PingOne Signals (Protect) SDK
  about-this-task-5: About this task
  steps-8: Steps
  choose-from-2: Choose from:
  choose-from-3: Choose from:
  third_party_scores: Using third-party risk scores with PingOne Protect
  sending-third-party-data-to-pingone-protect: Sending third-party data to PingOne Protect
  validating-received-third-party-data-in-pingone-protect: Validating received third-party data in PingOne Protect
  configuring-custom-predictors-using-custom-attributes: Configuring custom predictors using custom attributes
  running-analyzing-and-adjusting-your-risk-policy: Running, analyzing, and adjusting your risk policy
  about-this-task-6: About this task
  steps-9: Steps
  next-steps: Next steps
---

# Getting started with PingOne Protect

Prevent account takeover, new account fraud, and multi-factor authentication (MFA) *(tooltip: \<div class="paragraph">
\<p>An electronic authentication method where a user is granted access only after presenting two or more verification factors for authentication.\</p>
\</div>)* and password fatigue with PingOne Protect.

By evaluating multiple attack vectors, assigning risk scores, and providing insights, PingOne Protect triggers mitigation tools to block attacks and allow legitimate users to authenticate easily.

PingOne Protect allows enterprises to:

* Stop account takeover and new account fraud.

* Improve user experience by reducing MFA prompts and going passwordless.

* Create intelligent policies that aggregate multiple predictors and assign a risk score.

You can use PingOne Protect in user access, authentication, authorization, registration, and transaction flows.

The two basic elements used in the risk analysis process are predictors and risk policies:

* Predictors

  A predictor looks at a single factor, for example, whether or not a user is trying to authenticate from an anonymous network, and yields an estimated risk level. Learn more in [Predictors](p1_protect_risk_predictors.html).

* Risk policy

  A risk policy combines a number of individual risk predictors, looks at the risk level estimated for each of the predictors, and then yields an overall risk level of **Low**, **Medium**, or **High**. Learn more in [Risk policies](p1_protect_risk_policies.html).

PingOne creates risk evaluations when a user initiates a flow, and the risk policy determines how the aggregated risk score from the risk evaluation should be translated into a final risk level. Learn more in [Risk evaluations](p1_protect_risk_evaluations.html).

## Threat Protection Dashboard

To help you assess how risk evaluations are impacting user flows, PingOne includes the **Threat Protection Dashboard**. The dashboard displays top-level information and includes a number of charts that you can use to get detailed information on specific aspects of the data.

Learn more in [Threat Protection Dashboard](p1_protect_dashboard.html).

## How PingOne Protect works

PingOne Protect dynamically evaluates risk data and calculates a risk level. You can create risk policies to control the response that the end user receives depending on the risk level.

The following diagram shows how PingOne Protect works.

![A diagram showing how PingOne Protect works.](_images/jpo1687550100235.png)

1. The user initiates the flow.

   Possible [types of user flows](https://developer.pingidentity.com/pingone-api/protect/risk-evaluations.html) are access, authentication, authorization, registration, or transaction. You can also specify a flow subtype to provide additional detail about the context of the flow, such as if the user performed a password reset or signed on with their username and password. Learn more about flow types and subtypes in the [PingOne Protect API documentation](https://developer.pingidentity.com/pingone-api/protect/risk-evaluations.html).

2. PingOne Protect evaluates risk levels based on various data points, such as network, location, device hardware and settings, behavioral biometrics, and more.

3. The PingOne Protect risk policy calculates the risk based on policy settings.

4. PingOne Protect returns a detailed response that includes data about the event, the user and their device, predictor results, and the risk policy result.

   Learn more in [Risk evaluations](p1_protect_risk_evaluations.html).

   |   |                                                                                                                                                                                                                       |
   | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | You can use the PingOne API to configure and retrieve risk policies and evaluations. Learn more in the [PingOne Protect API documentation](https://developer.pingidentity.com/pingone-api/protect/introduction.html). |

   The policy result can include the following attributes:

   * `result.level`

     The response always returns this attribute. Values can be `LOW`, `MEDIUM`, and `HIGH`.

   * `result.score`

     The response always returns this attribute and includes the numeric score that the policy calculates. The score determines the risk level based on the policy threshold.

   * `result.recommendedAction`

     The response might return this attribute based on the attack vector. This attribute enhances the risk level attribute and provides information on how the user flow should continue. Possible values are:

     * `ACCOUNT_RECOVERY`: There are indications that the user's account may have been compromised, so you should have them follow your account recovery procedure.

     * `AITM_MITIGATION`: You should take steps to mitigate the damage from an Adversary-in-the-Middle (AitM) attack. For an AitM attack, the user's credentials have been intercepted, so in addition to blocking the access request, you should lock the user's account until the password is changed.

     * `BOT_MITIGATION`: You should take steps to handle a scenario where a bot is involved.

     * `DENY`: When a risk level of `HIGH` is calculated for a traffic anomaly predictor, you should deny access because the repeated risk evaluations are likely a sign of a brute force attack.

     * `TEMP_EMAIL_MITIGATION`: The user has specified a disposable email address, which is an indication of a fraud attempt.

   * `result.mitigations`

     This attribute is included in the result when a mitigation rule is configured in the risk policy to define custom recommended actions and the conditions of the rule are met.

   * `result.value`

     The response might return this attribute. `result.value` is free text that you can add to a policy override. Override rules are not necessary in most cases, but you can use them in scenarios that require blocking a user (for example, known IPs that you want to block).

     Learn more about policy overrides and mitigations in [Risk policies](p1_protect_risk_policies.html).

     You can find a full response example in [PingOne Protect API documentation](https://developer.pingidentity.com/pingone-api/protect/risk-evaluations/create-risk-evaluation.html).

5. The risk policy makes a decision based on the response, and the user flow continues based on the decision.

## Key concepts

To fully leverage the capabilities of PingOne Protect, familiarize yourself with the following key concepts:

* [Introduction to risk policies](#intro_risk_policies)

* [Introduction to predictors](#intro_predictors)

* [Introduction to risk evaluations](#intro_risk_evaluations)

* [Introduction to using the PingOne API for risk evaluations](#intro_api_risk_evaluations)

### Introduction to risk policies

The risk policy looks at the risk level estimated for each of the predictors and then yields an overall risk level of **Low**, **Medium**, or **High**. When you define a user journey with the tools provided by Ping Identity, you decide which of your defined risk policies you would like to associate with that flow. For some situations, you might need to use a stricter risk policy, while for others, you could use a more lenient risk policy.

#### The default risk policy

When you add the PingOne Protect service to a PingOne environment, it includes a default risk policy. This is the recommended policy for your initial testing of risk evaluations.

The default risk policy has the following characteristics:

* It uses the **Scores** approach, which gives you a higher degree of control than the **Weights** approach.

  |   |                                                                                                                                |
  | - | ------------------------------------------------------------------------------------------------------------------------------ |
  |   | **Weights** in risk policies have been deprecated for new PingOne environments but can still be used in existing environments. |

* It includes all of the out-of-the-box predictors.

* It assigns a score of 50 for **High** risk for some of the predictors and a score of 75 for **High** risk for the remaining predictors. This is based on the premise that the IP-related predictors are less indicative of risky situations than the other predictors.

The risk level for each predictor type is calculated separately. Most predictor types require training and learn from successful events. You can also configure a fallback value for most predictor types to use if there is insufficient information to calculate a risk level.

Learn more in [Predictors](p1_protect_risk_predictors.html).

You can also create custom predictors that leverage external or processed data. Learn more in [Adding custom predictors](p1_protect_adding_custom_predictors.html).

#### Staging policies

Staging policies allow you to fine tune and test risk policy changes before releasing changes to your production policy and does not affect your end users until you promote a staging policy to production.

Learn more in [Creating and managing staging policies](p1_protect_creating_managing_staging_policies.html).

#### Custom risk policies

|   |                                                                                                       |
| - | ----------------------------------------------------------------------------------------------------- |
|   | Customize risk policies only after you've accumulated sufficient authentication data and analyzed it. |

Use the **Risk Policies** page in PingOne to modify the default risk policy or create additional risk policies of your own. Learn more in [Risk policies](p1_protect_risk_policies.html).

### Introduction to predictors

Predictors are the basic building blocks that form risk policies. A predictor looks at a single factor, such as whether or not a user is trying to authenticate from an anonymous network. Each predictor yields an estimated risk level. For some predictors, the levels are **Low** and **High**. For other predictors, the levels are **Low**, **Medium**, and **High**.

PingOne Protect leverages the following risk predictors to learn user behavior and detect anomalies:

| Predictor                      | Description                                                                                                                                                                                                                               |
| ------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Adversary-in-the-Middle (AitM) | Checks the domain name that the user is trying to access in order to identify AitM attacks.                                                                                                                                               |
| Anonymous network detection    | Analyzes IP address data from a user's device to determine if the address is originating from any type of anonymous network, such as unknown VPNs, Tor, or proxies to mask the IP address.                                                |
| Bot detection                  | Leverages advanced analysis of mouse, keyboard, touch, and mobile sensors, as well as device attributes, to detect non-human behavior, automated frameworks, recorders, and more.                                                         |
| Email reputation               | Detects the use of disposable email addresses during registration.                                                                                                                                                                        |
| Geovelocity anomaly            | Analyzes location data to calculate if travel time between two session locations is physically possible.                                                                                                                                  |
| IP reputation                  | Analyzes data from different intelligence sources to determine the probability an IP address is associated with malicious activity and to request stronger authentication to verify the user's identity.                                  |
| IP velocity                    | Tracks the number of distinct IPs used per user.                                                                                                                                                                                          |
| New device                     | Takes into account the risk associated with users trying to access applications from unknown devices or devices that have not been used for sign-on in the recent past.                                                                   |
| PingID device trust            | Establishes device trust by collecting device information through the PingID device trust agent installed on an organization's workstations.                                                                                              |
| Suspicious device              | Scrutinizes browser, operating system, and hardware attributes to identify suspicious settings or inconsistencies between these attributes collected from the device.                                                                     |
| Traffic anomaly                | Monitors users, devices, and sessions to detect traffic anomalies, such as a large number of risk evaluations requested for a single user within a short period of time or a large number of users per device during a given time period. |
| User-based risk behavior       | Compares a transaction with the typical behavior of that specific user.                                                                                                                                                                   |
| User location anomaly          | Detects a user's sign-on location and checks it against previously saved authentication locations.                                                                                                                                        |
| User velocity                  | Tracks the number of distinct users per IP.                                                                                                                                                                                               |

Learn more about each predictor in [Predictors](p1_protect_risk_predictors.html).

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | The PingOne Risk license allows you to use the following predictors in your risk policies. The remaining predictors require a PingOne Protect license.- Anonymous Network Detection

- Geovelocity Anomaly

- IP Reputation

- IP Velocity

- New Device

- User-Based Risk Behavior

- User Location Anomaly

- User VelocityTo upgrade your license to PingOne Protect and gain access to the additional predictors, contact your account team for more details. |

The risk level for each predictor type is calculated separately. Most predictor types require training and learn from successful events. You can configure a fallback value for most predictor types to use if there is insufficient information to calculate a risk level.

You can also create custom predictors that leverage external or processed data. Learn more in [Customizing predictors](p1_protect_risk_predictors.html#section_jxv_2pv_xxb).

### Introduction to risk evaluations

Risk evaluations calculate the risk level and other risk-related details associated with an event. The PingOne Protect risk policy then calculates the risk based on policy settings and returns a detailed response that includes data about the event, the user and their device, predictor results, and the risk policy result. You can view the results from risk evaluations to see how your risk policy is performing.

Learn more about risk evaluations and how to use them in:

* [Risk evaluations](p1_protect_risk_evaluations.html)

* [Updating completion status for risk evaluations](p1_protect_updating_completion_status_risk_evaluations.html)

* [Providing feedback for risk evaluations](p1_protect_providing_feedback_risk_evaluations.html)

* [Reviewing risk evaluations](p1_protect_reviewing_risk_evaluations.html)

### Introduction to using the PingOne API for risk evaluations

You can use the PingOne API to:

* Create and manage risk predictors

* Create and manage risk policies

* Create risk evaluations

* Update the completion status of risk evaluations to improve the accuracy of future risk evaluations

Learn more in the [PingOne Protect section](https://developer.pingidentity.com/pingone-api/protect/introduction.html) of the PingOne API documentation.

## Trying PingOne Protect with a sample app

### Before you begin

Sign up for a PingOne trial. Learn more in [Starting a PingOne trial](../getting_started_with_pingone/p1_start_a_p1_trial.html).

### About this task

Signing up for a PingOne trial is a great way to experience the functionality of PingOne Protect with an automatically generated sample application. This sample app is a Ping-maintained application that allows you to design registration and sign-on experiences for your customers and test them in the app.

With your PingOne trial, you can try PingOne Protect and quickly and easily simulate risk events with the sample app to test how predictors work. The sample app allows you to test the capabilities of PingOne Protect in addition to other PingOne services, such as PingOne MFA and PingOne SSO, and can be tailored to your industry.

|   |                                                                                                                                                     |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Learn more about trying PingOne Protect in your existing PingOne user journey instead of with a trial in [Getting up and running](#get_up_running). |

To try PingOne Protect with a sample app:

### Steps

1. In the PingOne admin console, click **Add Environment**.

2. Select **Customer solution**, and click **Next**.

   |   |                                                                                                                   |
   | - | ----------------------------------------------------------------------------------------------------------------- |
   |   | When you create a **Customer solution**, your new environment automatically includes the PingOne Protect service. |

3. Click **Next** again to create the environment.

4. Enter the details for your environment, select the **Include a solution designer to easily design and test experiences** check box, and click **Finish**.

   #### Result:

   Your new PingOne environment is created and automatically opens.

5. Choose if you want to tailor your experience for your industry, or click **Skip**.

   #### Result:

   PingOne creates a sample app based on your selection. You can click **Get Started** to view the tour or close the tour pop-up window.

6. [Test the predictors](p1_protect_testing_risk_predictors.html).

   |   |                                                                                                  |
   | - | ------------------------------------------------------------------------------------------------ |
   |   | The PingOne Protect capabilities are available in the **Authentication** flow of the sample app. |

## Getting up and running

Follow these steps to start using PingOne Protect as part of your user journeys.

While PingOne Protect provides many ways to customize predictors and to combine them in a risk policy, it also provides out-of-the-box predictors and a default risk policy that combines these predictors.

When you first start with PingOne Protect, the best approach is to use the default risk policy that is provided. After you've seen how this default policy affects the flow experience for your users, you can go back and fine-tune it by customizing individual predictors or creating multiple risk policies.

Because you'll use the default risk policy, your only task at the beginning is the integration of PingOne Protect with your user journey.

The main steps required to start using PingOne Protect are:

1. Integrate PingOne Protect into a user journey.

2. Configure the PingOne Signals (Protect) SDK.

3. Run and analyze your predictors:

   1. Run PingOne Protect to train the predictor models.

   2. Use the PingOne Protect dashboard to analyze the results.

   3. Adjust the scores for the predictors in the risk policy.

      ![A diagram of the PingOne Risk of the run, analyze, and adjust cyclical process.](_images/oms1686780602268.png)

4. Repeat step 3 as needed.

### Adding the PingOne Protect service to your environment

To get started, add the PingOne Protect service to your PingOne environment.

#### Before you begin

* If you don't have a PingOne account yet, [start a PingOne trial](../getting_started_with_pingone/p1_start_a_p1_trial.html).

* Make sure that you can [sign on to the PingOne admin console](../getting_started_with_pingone/p1_access_admin_console.html).

* [Add an environment](../getting_started_with_pingone/p1_solution_add_environment.html) to organize your services.

* Make sure that you have the Environment Admin and Identity Data Admin roles in your PingOne environment. Learn more in [Managing user roles](../directory/p1_manage_user_roles.html).

#### Steps

1. In the PingOne admin console, go to **Overview**.

2. Next to **Services**, click the **[icon: plus, set=fa]**icon.

3. Click **[icon: plus, set=fa]Add** to add the **PingOne Protect** service.

4. In the **Add a Service** window, click **Finish**.

#### Result

PingOne Protect is displayed in the sidebar.

### Integrating PingOne Protect with user journeys

After you add PingOne Protect to your environment, integrate PingOne Protect into a user journey.

#### Before you begin

You'll need a PingOne account with at least one environment that includes the PingOne Protect service. Learn more in [Add an environment](../getting_started_with_pingone/p1_solution_add_environment.html).

You can integrate your risk policy into a user journey in one of the following ways:

* Using the integration with PingFederate

* Building a custom flow with PingOne DaVinci

* Using the PingOne API

* Integrating with PingOne Advanced Identity Cloud or PingAM

Regardless of the integration approach you use, the high-level steps are the same. The steps below use an authentication flow as an example for integration, but you can also use other user journeys, such as registration and authorization:

#### Steps

1. Integrate into an authentication flow.

   The following diagram shows a high-level overview of PingOne Protect integrated in silent mode into an example authentication flow.

   ![A diagram of how PingOne Protect works in silent mode.](_images/zdv1686757833051.png)

2. Send transaction feedback.

3. Configure a risk policy.

   The simplest approach is to use the default risk policy. You can also edit the default risk policy.

4. Add risk evaluation to your authentication flow.

   The following diagram shows an example of PingOne Protect integrated into an authentication flow with risk levels affecting the flow.

   ![A diagram of how PingOne Protect works with risk evaluation enabled.](_images/cyz1686758346502.png)

* PingFederate

* DaVinci

* API

* PingOne Advanced Identity Cloud

## Using the PingOne Protect Integration Kit with PingFederate

### Before you begin

Before proceeding, make sure PingFederate is installed. Learn more in [Installing PingFederate](https://docs.pingidentity.com/pingfederate/latest/installing_and_uninstalling_pingfederate/pf_installing_pf.html).

### Steps

1. Deploy the files for the type of integration kit you're using to your PingFederate directory:

   #### Choose from:

   * [PingOne Protect Integration Kit](https://docs.pingidentity.com/integrations/pingone/pingone_protect_integration_kit/pf_p1_protect_ik_deploying_the_integration_files.html)

   * [PingOne Risk Integration Kit](https://docs.pingidentity.com/integrations/pingone/pingone_risk_integration_kit/pf_p1_risk_ik_deploying_the_integration_files.html)

     |   |                                                                                                                                                                                 |
     | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
     |   | The PingOne Protect Integration Kit 1.0 works with PingFederate 11.3 and later. The PingOne Risk Integration Kit will continue to support PingFederate versions 10.2 and later. |

2. To allow PingFederate to communicate with PingOne, [create a connection between PingOne and PingFederate](https://docs.pingidentity.com/integrations/pingone/pingone_risk_integration_kit/pf_p1_risk_ik_connecting_pf_to_p1.html).

3. To configure the integration kit, follow the steps in the documentation for the integration type that you selected in step 1.

## Building a custom flow with PingOne DaVinci

### Before you begin

Add PingOne DaVinci to your PingOne environment. Learn more in [Adding an environment](../getting_started_with_pingone/p1_getting_started_adding_environment.html).

### About this task

PingOne DaVinci is the graphic orchestration tool used for designing flows, such as user registration and authentication flows. Learn more about using PingOne DaVinci in the [DaVinci documentation](https://docs.pingidentity.com/davinci/davinci_landing_page.html).

You can use the PingOne Protect connector to define different paths in an user journey flow, based on the result of a risk evaluation.

For example, you can use a risk evaluation connector before a MFA *(tooltip: \<div class="paragraph">
\<p>An electronic authentication method where a user is granted access only after presenting two or more verification factors for authentication.\</p>
\</div>)* step, and then define different paths based on the risk score calculated:

* Skip the MFA challenge if low risk.

* Use a specific authentication method if user behavior data suggests medium or high risk.

* Block access completely in a high-risk situation, such as when the recommended action is equal to bot mitigation.

  ![A screen capture of a DaVinci flow with a PingOne Protect connector, showing the user flow for different risk levels.](_images/zqr1688075451034.png)

For examples of using the PingOne Protect connector in different types of flows, see the following templates in the [Flow Library](https://docs.pingidentity.com/davinci/flows/davinci_using_davinci_flow_templates.html):

* PingOne - Sign On and Adaptive MFA

* PingID - MFA flow + Protect

* PingID - FIDO2 Passwordless + Protect

To use Protect connectors in a flow:

### Steps

1. After you have added DaVinci to your PingOne environment, ensure any risk connectors you add to your flows already have been configured with the correct information for environment ID, client ID, and client secret.

   If you import a flow from a different PingOne environment, you must go to the settings for the Protect connector and update this information to reflect the environment where you're adding the flow.

2. Add two different Protect connectors to your flow by following the documentation for the [PingOne Protect connector](https://docs.pingidentity.com/connectors/p1_protect_connector.html):

   1. Add a Protect connector with the Create Risk Evaluation capability.

      The response returns a final risk evaluation result - `High`, `Medium`, or `Low`. The Protect connector with the `Create Risk Evaluation` capability should be added at a point in the flow where you would like to base the next action on the risk score assigned, for example, show an MFA prompt for Medium or High, but automatically grant access if the risk is deemed Low.

   2. Add risk evaluation feedback to the flow by adding a Protect connector with the Update Risk Evaluation capability.

      This step is included after authentication has been completed, and it consists of sending an update with the final state of the transaction, such as `SUCCESS` or `FAIL`. The Update Risk Evaluation capability represents the system's ability to learn over time in order to improve results. You should always include an update connector in your flow because this step is essential for improving the accuracy of the machine learning models.

      |   |                                                                                                                                                                |
      | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      |   | Flows may take users on different paths. Make sure to include a Protect connector with the Update Risk Evaluation capability at the end of each possible path. |

### Troubleshooting

If you are having issues with the PingOne Protect Connector, try the following:

* For each connector in the flow, make sure that all of the mandatory inputs have been provided.

* If you are using the `skrisk` component to include the data provided by the PingOne Signals (Protect) SDK, make sure that you have carried out the necessary steps.

* Use the [Analytics feature](https://docs.pingidentity.com/davinci/davinci_best_practices/davinci_best_practices_debugging_and_analytics.html) to see where the flow stopped.

* Select the **Options** icon, and turn on **Show Node ID**. This will make it easier to identify the source of inputs and outputs.

## Using the PingOne API

### About this task

To integrate using the PingOne API:

### Steps

1. Create a worker application and get an access token.

   Learn more in [Adding an application](../applications/p1_applications_add_applications.html) and [Getting an access token](../applications/p1_getaccesstoken.html).

2. Add risk evaluation to your user flow.

   Learn more in the [Risk evaluation section](https://developer.pingidentity.com/pingone-api/protect/risk-evaluations.html) in the PingOne Protect API documentation.

   The response returns a final risk evaluation result of `High`, `Medium`, or `Low`.

3. Add risk evaluation feedback to the flow.

   This step is included after authentication has been completed, and it consists of sending an update with the final state of the transaction, such as `SUCCESS` or `FAIL`. This step is essential for improving the accuracy of the machine learning models. Learn more in [PUT UPDATE Risk Evaluation](https://developer.pingidentity.com/pingone-api/protect/risk-evaluations/update-risk-evaluation.html) in the PingOne Protect API documentation.

4. [Modify the default risk policy](p1_protect_risk_policies.html) or [create one of your own risk policy set with the API](https://developer.pingidentity.com/pingone-api/protect/risk-policies/create_risk_policy_set_scores.html).

## Integrating with PingOne Advanced Identity Cloud

### Before you begin

Make sure you have:

* A PingOne Advanced Identity Cloud administrator account

* A PingOne account

  Learn more in [Starting a PingOne trial](../getting_started_with_pingone/p1_start_a_p1_trial.html).

* The client ID and client secret for a PingOne environment

* A risk policy configured in PingOne (or use the default risk policy)

* A worker application with the Identity Data Admin role assigned in PingOne

### About this task

Advanced Identity Cloud is a comprehensive identity and access management (IAM) service that lets you deploy applications anywhere: on-premises, in your own private cloud, or in your choice of public cloud. With Advanced Identity Cloud, you can manage user journeys and take advantage of the PingOne Protect threat protection features by integrating the three PingOne Protect nodes into your journey.

### Steps

1. [Configure the PingOne Service](https://docs.pingidentity.com/auth-node-ref/latest/pingone/pingone-service.html) in Advanced Identity Cloud.

2. Set up your user journey in Advanced Identity Cloud with the three PingOne Protect nodes in the journey:

   1. The [PingOne Protect Initialization node](https://docs.pingidentity.com/auth-node-ref/latest/pingone/pingone-protect-initialize.html) to initialize the PingOne Protect Web SDK on the client device.

   2. The [PingOne Protect Evaluation node](https://docs.pingidentity.com/auth-node-ref/latest/pingone/pingone-protect-evaluation.html) to calculate the risk level and other risk-related details associated with an event.

   3. The [PingOne Protect Result node](https://docs.pingidentity.com/auth-node-ref/latest/pingone/pingone-protect-result.html) to update the risk evaluation configuration or modify the completion status of the resource when the risk evaluation is still in progress.

3. Validate that the PingOne Protect Evaluation node is working by checking the PingOne **Audit** log for **Risk Evaluation Created** events.

### Getting input from the PingOne Signals (Protect) SDK

Certain risk predictors, such as the **New Device** predictor, rely on supplemental risk-related information that is supplied by the PingOne Signals (Protect) SDK.

#### About this task

The default risk policy includes predictors that are dependent upon this input. To get reliable risk evaluations right from the start, you must carry out the steps to include the required code in your applications and include the information from the Signals SDK in your user journeys.

#### Steps

1. Add the required Signals SDK code into your web applications, Android applications, and iOS applications.

   ##### Choose from:

   * [PingOne Signals (Protect) SDK for Web](https://developer.pingidentity.com/pingone-api/native-sdks/pingone-risk-sdks/risk_evaluation_sdk_web.html)

   * [PingOne Signals (Protect) SDK for Android](https://developer.pingidentity.com/pingone-api/native-sdks/pingone-risk-sdks/risk_evaluation_sdk_android.html)

   * [PingOne Signals (Protect) SDK for iOS](https://developer.pingidentity.com/pingone-api/native-sdks/pingone-risk-sdks/risk_evaluation_sdk_ios.html)

2. Include the information from the Signals SDK in your flows using one of the following methods:

   ##### Choose from:

   * PingOne Protect Integration Kit for PingFederate: Integrate device profiling with one of following:

     * [PingOne Protect Integration Kit](https://docs.pingidentity.com/integrations/pingone/pingone_protect_integration_kit/pf_p1_protect_ik_integrating_device_profiling.html)

     * [PingOne Risk Integration Kit](https://docs.pingidentity.com/integrations/pingone/pingone_risk_integration_kit/pf_p1_risk_ik_integrating_device_profiling.html)

   * PingOne Protect API: [Create risk evaluations](https://developer.pingidentity.com/pingone-api/protect/risk-evaluations/create-risk-evaluation.html).

   * PingOne DaVinci: Include the [PingOne Protect connector](https://docs.pingidentity.com/connectors/p1_protect_connector.html) as part of a user flow.

   * PingOne Advanced Identity Cloud: Include the [PingOne Protect authentication nodes](https://docs.pingidentity.com/pingoneaic/integrations/pingone-protect.html) as part of journey.

### Using third-party risk scores with PingOne Protect

The best threat protection often means leveraging multiple risk and fraud services. PingOne Protect allows administrators to send third-party data and other risk signal vendor scores, for example sending information from PingFederate whether a device is managed and not.

There are three steps to ingesting third-party risk data into PingOne Protect:

1. Send the third-party data to PingOne Protect by creating custom attributes to map the values to.

2. Validate that PingOne Protect received the third-party data.

3. Configure a custom predictor using the custom attributes.

   Custom predictors allow you to plug in external data sources and reference custom attributes. You can use custom predictors to determine a risk score for unmanaged devices or map third-party risk scores to high, medium, or low. You can also add custom predictors to risk policies, apply overrides, and view analytics in the dashboards.

#### Sending third-party data to PingOne Protect

PingOne Protect cannot invoke a third-party API directly, so the external data must be sent into the evaluation call from another service, and the values need to be mapped into custom attributes.

Depending on your identity service providers, there are multiple ways to send third-party data to PingOne Protect:

* PingOne DaVinci

  The most straightforward approach is using PingOne DaVinci to retrieve a third-party data feed and pass the response back into PingOne Protect. Use purpose-built PingOne DaVinci connectors to get risk evaluations from vendors such as Castle, LexisNexis, or Securonix. You can also configure a generic REST call to get risk information from other vendors.

  Learn more in:

  * [PingOne Protect connector](https://docs.pingidentity.com/connectors/p1_protect_connector.html)

  * [Setting up custom attributes](https://docs.pingidentity.com/connectors/p1_protect_connector.html)

  * Example connectors:

    * [Castle connector](https://docs.pingidentity.com/connectors/castle_connector.html)

    * [LexisNexis connector](https://docs.pingidentity.com/connectors/lexisnexis_connector.html)

    * [Securonix connector](https://pingone-davinci.github.io/documentation/securonix/)

    * [PingOne DaVinci HTTP connector](https://docs.pingidentity.com/connectors/http_connector.html) (generic API call)

* PingFederate

  Use PingFederate integration kits to retrieve third-party data in combination with the PingOne Protect Integration Kit to configure custom attributes to map the data into PingOne Protect.

  Learn more in:

  * [PingOne Protect Integration Kit](https://docs.pingidentity.com/integrations/pingone/pingone_protect_integration_kit/pf_p1_protect_ik.html)

  * [Setting up custom attributes](https://docs.pingidentity.com/integrations/pingone/pingone_protect_integration_kit/pf_p1_protect_ik_using_custom_risk_predictors.html)

  * Example integration kits:

    * [ID DataWeb Integration Kit](https://docs.pingidentity.com/integrations/iddataweb/pf_iddataweb_ik.html)

    * [iovation Integration Kit](https://docs.pingidentity.com/integrations/iovation/pf_iovation_ik.html)

    * [ThreatMetrix Integration Kit](https://docs.pingidentity.com/integrations/threatmetrix/pf_threatmetrix_ik.html)

    * Mobile device management (MDM) integration kits:

      * [Intune Integration Kit](https://docs.pingidentity.com/integrations/intune/pf_intune_ik.html)

      * [MobileIron Integration Kit](https://docs.pingidentity.com/integrations/mobileiron/pf_mobileiron_ik.html)

      * [Workspace ONE UEM Integration Kit](https://docs.pingidentity.com/integrations/workspaceone-uem/pf_workspaceone_uem_ik.html) (formerly known as AirWatch)

* PingOne API

  Use the PingOne API to retrieve risk evaluations from third-party risk providers. You can add custom attributes to `event` objects by adding the attribute to the `event` object in the body of a risk evaluation request. Learn more in [Risk evaluations](https://developer.pingidentity.com/pingone-api/protect/risk-evaluations.html) in the PingOne Protect API documentation.

* PingOne Authorize

  Use PingOne Authorize to call PingOne Protect for risk evaluations as part of a PingOne authorization policy. Learn more in [Connecting to PingOne Protect](../authorization_using_pingone_authorize/p1_az_connecting_p1_risk.html).

#### Validating received third-party data in PingOne Protect

After you send the third-party data to PingOne Protect, validate that the data was received either using the PingOne admin console or the API:

* PingOne admin console: To view a risk evaluation, follow the steps in [Reviewing risk evaluations](p1_protect_reviewing_risk_evaluations.html).

* PingOne API: Create a risk evaluation and review the response. Learn more in the [PingOne Protect API documentation](https://developer.pingidentity.com/pingone-api/protect/risk-evaluations/create-risk-evaluation.html).

|   |                                                                                                                               |
| - | ----------------------------------------------------------------------------------------------------------------------------- |
|   | In a risk evaluation, the custom attributes appear in the `event {…​}` section near the end of the JSON in a risk evaluation. |

#### Configuring custom predictors using custom attributes

After sending third-party data and validating that it was received in PingOne, configure custom predictors that use the custom attributes that you previously created:

* PingOne admin console: Learn more in [Adding custom predictors](p1_protect_adding_custom_predictors.html).

* PingOne API: Learn more in [Custom risk predictors](https://developer.pingidentity.com/pingone-api/protect/risk-predictors.html) in the PingOne Protect API documentation.

### Running, analyzing, and adjusting your risk policy

To make informed decisions about how to fine-tune risk predictors and policies, you'll have to accumulate a certain amount of data on authentication attempts and how the risk evaluation impacts them.

#### About this task

You should use the default risk policy for the initial period before you start customizing the policy or defining multiple risk policies.

Fine-tuning your policy is an iterative process and should follow this approach:

#### Steps

1. Train the risk models with production data for 1 - 3 weeks for workforce usage or 2 - 4 weeks for customer usage. This should be done with the default risk policy.

2. Use the **Threat Protection Dashboard** to analyze the results. Identify false positive results, meaning situations that are identified as **High** risk even though they are legitimate users. Check what's causing these false positives.

3. Adjust the scores for the different risk predictors in the risk policy to see if you can reduce the incidence of false positives.

   ![A diagram of the cyclical process of managing your risk policy.](_images/rza1686848398503.png)

## Next steps

After you've familiarized yourself with how PingOne Protect works and have it running, refer to the following for next steps to deepen your understanding:

* To learn more about how the predictors work, you can [test predictors by simulating risk events in a sample application](p1_protect_testing_risk_predictors.html).

* Learn more about customizing predictors that leverage external or processed data in [Custom predictors](p1_protect_risk_predictors.html#section_jxv_2pv_xxb) and [Adding custom predictors](p1_protect_adding_custom_predictors.html).

* Learn more about building and customizing your own risk policies in [Risk policies](p1_protect_risk_policies.html).

* To test and fine-tune risk policy changes before promoting them into production, you can create a staging policy and view how your changes impact your users. Learn more in [Evaluating staging policy risk data](p1_protect_evaluating_staging_policy.html).

---

---
title: High risk models
description: View the High Risk Models chart in PingOne Protect to see the distribution of risk model types and identify the most prevalent risk factors.
component: pingone
page_id: pingone:threat_protection_using_pingone_protect:p1_protect_high_risk_models
canonical_url: https://docs.pingidentity.com/pingone/threat_protection_using_pingone_protect/p1_protect_high_risk_models.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: February 19, 2025
---

# High risk models

The **High Risk Models** chart shows the distribution of each type of risk model, regardless of the configured risk policy.

You can use the **High Risk Models** chart to see which risk factors are most prevalent.

To access the **High Risk Models** chart, go to **Monitoring > Threat Protection**.

![A screen capture of the Risk Models page showing a bar graph of the high risk model distribution over the past week.](_images/ykq1616085775187.png)

The drill-down table shows more detailed information about each risk evaluation event, including user, IP address, and target application.

Scroll to the right to see additional columns. Learn more about using the filtered search bar in [Filtered searching](p1_protect_dashboard.html#section_dpy_gqs_h4b).

You can click a column header to sort the results by that value. Results are sorted by the **Time** column by default, with the most recent entries listed first.

---

---
title: Introduction to PingOne Protect
description: PingOne Protect is a cloud-based service that uses machine learning and risk policies to detect threats and calculate risk scores.
component: pingone
page_id: pingone:threat_protection_using_pingone_protect:p1_protect_introduction
canonical_url: https://docs.pingidentity.com/pingone/threat_protection_using_pingone_protect/p1_protect_introduction.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: February 14, 2025
---

# Introduction to PingOne Protect

PingOne Protect is a cloud-based service that applies machine learning and configurable, intelligent security policies to analyze user identity and detect potential threats.

PingOne Protect combines multiple internal and external risk factors to provide a single access point for calculating and retrieving risk scores. Use the user interface to create risk policies and configure the scores of various risk predictors into a single risk score. You can also view data and analytics on high-risk events and get in-depth insights on the authentication behavior of your users.

![A screen capture of the PingOne Protect dashboard.](_images/stf1635456746930.png)

By implementing risk policies, you can control the authentication flow depending on the risk level. For example, you can force high-risk users to step up to stronger authentication or deny them access while providing a frictionless experience for trusted users.

PingOne Protect leverages the following predictors to learn user behavior and detect anomalies:

* Adversary-in-the-Middle

* Anonymous network detection

* Bot detection

* Device (new device and suspicious device)

* Email reputation

* Geovelocity anomaly

* IP reputation

* PingID device trust

* Traffic anomaly

* User-based risk behavior

* User location anomaly

* Velocity (user velocity and IP velocity)

|   |                                                                                                                                                                                                  |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | The suspicious device and bot detection predictors are only available if you have a license for PingOne Protect. If you have a PingOne Risk license, contact your account team for more details. |

Learn more in [PingOne Protect key concepts](p1_protect_getting_started.html#essential_concepts) and the [PingOne Protect Datasheet](https://www.pingidentity.com/en/resources/client-library/data-sheets/3528-pingone-risk.html).

---

---
title: OS distribution
description: View risk evaluations by operating system type in the PingOne Protect OS Distribution dashboard chart.
component: pingone
page_id: pingone:threat_protection_using_pingone_protect:p1_protect_os_distribution
canonical_url: https://docs.pingidentity.com/pingone/threat_protection_using_pingone_protect/p1_protect_os_distribution.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: February 19, 2025
---

# OS distribution

The **OS Distribution** chart shows the number of recorded risk evaluations by user operating system type.

To access the **OS Distribution** chart, go to **Monitoring > Threat Protection**.

![A screen capture of the OS distribution pie chart. The legend is directly above the chart. The Filters and Date Range sections are on the left side of the graph, and the monitored risk data table is below it.](_images/mbd1612373007744.png)

The drill-down table shows more detailed information about each risk evaluation event, such as IP address and target application.

Scroll to the right to see additional columns. Learn more about using the filtered search bar in [Filtered searching](p1_protect_dashboard.html#section_dpy_gqs_h4b).

You can click a column header to sort the results by that value. Results are sorted by the **Time** column by default, with the most recent entries listed first.

---

---
title: PingOne Signals (Protect) SDK
description: Use the PingOne Signals (Protect) SDK to obtain risk-related information and pass it to the risk evaluation.
component: pingone
page_id: pingone:threat_protection_using_pingone_protect:p1_protect_signals_sdk
canonical_url: https://docs.pingidentity.com/pingone/threat_protection_using_pingone_protect/p1_protect_signals_sdk.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: February 19, 2025
section_ids:
  integrations: Integrations
  predictors-dependent-on-the-sdk: Predictors dependent on the SDK
---

# PingOne Signals (Protect) SDK

You can use the PingOne Signals (Protect) SDK to obtain information for additional risk-related variables and then pass this information on to the risk evaluation.

Learn more in the [Signals SDK documentation](https://developer.pingidentity.com/pingone-api/native-sdks/pingone-risk-sdks/risk_evaluation_sdk.html).

## Integrations

The Signals SDK can be used in conjunction with the following:

* [PingOne Protect Integration Kit for PingFederate](https://docs.pingidentity.com/integrations/pingone/pingone_protect_integration_kit/pf_p1_protect_ik_integrating_device_profiling.html)

* [PingOne Risk Integration Kit for PingFederate](https://docs.pingidentity.com/integrations/pingone/pingone_risk_integration_kit/pf_p1_risk_ik_integrating_device_profiling.html)

* [PingOne Protect API](https://developer.pingidentity.com/pingone-api/protect/risk-evaluations/create-risk-evaluation.html)

* [Part of a flow designed with PingOne DaVinci using the PingOne Protect connector](https://docs.pingidentity.com/connectors/p1_protect_connector.html)

* [Part of a journey designed with PingOne Advanced Identity Cloud PingOne Protect authentication nodes](https://docs.pingidentity.com/pingoneaic/integrations/pingone-protect.html)

## Predictors dependent on the SDK

The following predictors require the Signals SDK:

* Adversary-in-the-Middle (AitM)

* Bot Detection

* Suspicious Device

* User-Based Risk Behavior

The New Device predictor doesn't require the Signals SDK, but it's recommended as the best way to identify devices.

Learn more in [Predictors](p1_protect_risk_predictors.html).

---

---
title: Predictor rules
description: Use this rule reference to fine-tune the PingOne Protect Bot Detection, Suspicious Device, Traffic Anomaly, and composite predictors.
component: pingone
page_id: pingone:threat_protection_using_pingone_protect:p1_protect_predictor_rules
canonical_url: https://docs.pingidentity.com/pingone/threat_protection_using_pingone_protect/p1_protect_predictor_rules.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 22, 2026
section_ids:
  bot-detection-predictor: Bot Detection predictor
  suspicious-device-predictor: Suspicious Device predictor
  traffic-anomaly-predictor: Traffic Anomaly predictor
---

# Predictor rules

This reference topic lists the predefined rules used by the PingOne Protect predictors that evaluate rule-based conditions and patterns:

* [Bot Detection](#bot-detection-predictor)

* [Suspicious Device](#suspicious-device-predictor)

* [Traffic Anomaly](#traffic-anomaly-predictor)

You can also include specific rules for these predictors when creating a [composite predictor](p1_protect_adding_composite_predictors.html).

When configuring these predictors, you can exclude specific rules from risk level results. This fine-grained control is useful when a specific rule causes legitimate authentication attempts to be labeled as high risk.

## Bot Detection predictor

The following rules are used by the Bot Detection predictor:

| Rule ID | Rule                                              | Description                                                                                                                                                                                                                                                                            |
| ------- | ------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 600     | Automation framework - headless browser           | Flags indicators associated with automated browsing environments.                                                                                                                                                                                                                      |
| 601     | Automation framework                              | Detects known browser automation frameworks.                                                                                                                                                                                                                                           |
| 603     | Non-human keyboard interaction                    | Highlights keyboard behavior patterns that appear non-human.                                                                                                                                                                                                                           |
| 604     | Non-human mouse interaction                       | Highlights mouse interaction patterns that appear automated or synthetic.                                                                                                                                                                                                              |
| 610     | Suspicious user agent                             | Flags user-agent characteristics commonly associated with automation.                                                                                                                                                                                                                  |
| 612     | Media mismatch                                    | Detects inconsistencies between reported media capabilities and device profile.                                                                                                                                                                                                        |
| 618     | Hosting service with a suspicious device property | Flags potentially risky combinations of hosting-network and device characteristics.                                                                                                                                                                                                    |
| 623     | Automation driver tools                           | Detects automation driver tooling in the browser environment.                                                                                                                                                                                                                          |
| 625     | Screen resolution anomaly                         | Flags unusual display properties often associated with nonstandard environments.                                                                                                                                                                                                       |
| 627     | CPU cores anomaly                                 | Flags improbable hardware capacity reports.                                                                                                                                                                                                                                            |
| 628     | Browser loading anomaly                           | Detects browser initialization patterns associated with automation masking.                                                                                                                                                                                                            |
| 629     | Browser anomaly                                   | Highlights anomalous browser behavior that can indicate manipulation.                                                                                                                                                                                                                  |
| 631     | Invalid Chrome properties                         | Flags unexpected behavior in Chrome-specific runtime properties.                                                                                                                                                                                                                       |
| 632     | Automation framework on emulated device           | Detects signs that a session is running in an emulated environment.                                                                                                                                                                                                                    |
| 640     | Accelerometer anomaly                             | Flags motion-sensor patterns that are inconsistent with expected device behavior.                                                                                                                                                                                                      |
| 642     | Touch interaction duration anomaly                | Flags unusual touch interaction timing patterns.                                                                                                                                                                                                                                       |
| 660     | AI-based browser automation                       | Detects indicators of artificial intelligence (AI)-assisted or scripted browser control.This rule is enabled when the Signals SDK opt-in flag is set to `DetectAIAgents=True` and evaluates device and browser characteristics that strongly indicate AI or automated session control. |

## Suspicious Device predictor

The following rules are used by the Suspicious Device predictor:

| Rule ID | Rule                                                                                           | Description                                                                             |
| ------- | ---------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| 501     | Suspicious user agent                                                                          | Flags user-agent details inconsistent with expected device and browser patterns.        |
| 505     | Device properties mismatch                                                                     | Detects inconsistencies across device, browser, and graphics signals.                   |
| 508     | Suspicious device fingerprint                                                                  | Flags suspicious device fingerprint characteristics.                                    |
| 509     | Suspicious browser engine                                                                      | Detects inconsistencies between fingerprint signals and the reported browser engine.    |
| 510     | Mismatched between different attributes of the device                                          | Indicates conflicts across core device attributes.                                      |
| 518     | Device is missing expected sensors data such as accelerometer or gyroscope for a mobile device | Flags mobile devices missing expected sensor capabilities.                              |
| 520     | Mismatch in browser properties                                                                 | Detects inconsistencies across reported browser platform properties.                    |
| 521     | Browser API manipulation                                                                       | Detects signs of browser API or runtime property manipulation.                          |
| 530     | Indicate devices that are running as emulators on a PC                                         | Flags mobile sessions that appear to run in desktop-based emulation.                    |
| 531     | Indicate virtual Android devices                                                               | Flags Android sessions that appear to run in virtualized environments.                  |
| 532     | Indicate virtual iOS devices                                                                   | Flags iOS sessions that appear to run in simulated environments.                        |
| 534     | Device with suspicious network properties                                                      | Flags suspicious or inconsistent network-related device signals.                        |
| 535     | Compromised device                                                                             | Flags indicators that an Android device may be compromised.                             |
| 537     | Emulated Android browser detected                                                              | Flags browser sessions that appear to run in Android emulators.                         |
| 538     | Indicates whether the app is running using a cloning app                                       | Detects signs that an application is running in a cloned environment.                   |
| 540     | Suspicious mobile country code                                                                 | Flags potentially suspicious mobile network-code patterns.                              |
| 556     | Suspicious touchpoints                                                                         | Highlights touch input characteristics that appear inconsistent or implausible.         |
| 557     | Timezone offset mismatch                                                                       | Flags inconsistencies between reported time zone and time-offset signals.               |
| 562     | Indicates an Android device that is routing traffic through forward proxy                      | Flags Android sessions that appear to use proxy-based routing.                          |
| 590     | Application runs in debug mode                                                                 | Flags applications running with development-oriented settings.                          |
| 591     | Device configured for development                                                              | Highlights device setup patterns associated with development or testing configurations. |

## Traffic Anomaly predictor

The following rules are used by the Traffic Anomaly predictor:

| Rule ID | Rule                                                                             | Description                                                                                                                                               |
| ------- | -------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 801     | Multiple events by a user in short time                                          | Flags unusually high event activity for a user over a short period.                                                                                       |
| 803     | Number of unique users per device is above High threshold                        | Flags devices associated with an unusually high number of users.                                                                                          |
| 804     | Number of unique users per device is above Medium threshold                      | Flags devices associated with an elevated number of users.                                                                                                |
| 805     | Suspicious email address reuse                                                   | Detects potentially suspicious reuse patterns in email identities.                                                                                        |
| 806     | Unusual number of unique users or devices per browser token in registration flow | Flags unusually broad account or device activity tied to a single browser token.                                                                          |
| 807     | Email plus alias abuse                                                           | Detects repeated attempts to register a new user using email alias variations (for example, baseemailaddress+alias\@example.com) that can indicate abuse. |

---

---
title: Predictors
description: PingOne Protect predictors learn user behavior and detect anomalies.
component: pingone
page_id: pingone:threat_protection_using_pingone_protect:p1_protect_risk_predictors
canonical_url: https://docs.pingidentity.com/pingone/threat_protection_using_pingone_protect/p1_protect_risk_predictors.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: February 12, 2025
section_ids:
  adversary-in-the-middle-aitm: Adversary-in-the-Middle (AitM)
  anonymous-network-detection: Anonymous Network Detection
  bot-detection: Bot Detection
  email-reputation: Email Reputation
  geovelocity-anomaly: Geovelocity Anomaly
  ip-reputation: IP Reputation
  ip-velocity: IP Velocity
  new-device: New Device
  pingid-device-trust: PingID Device Trust
  suspicious-device: Suspicious Device
  traffic-anomaly: Traffic Anomaly
  user-based-risk-behavior: User-Based Risk Behavior
  user-location-anomaly: User Location Anomaly
  user-velocity: User Velocity
  ip-address-selection: IP address selection
  section_jxv_2pv_xxb: Customizing predictors
---

# Predictors

When you add the PingOne Protect service to a PingOne environment, the environment includes one predictor of each basic type that's supported. For example, you could have one Anonymous Network predictor and one IP Reputation predictor. The default name of the predictor is the name of the category.

PingOne Protect leverages the following risk predictors to learn user behavior and detect anomalies:

* [Adversary-in-the-Middle (AitM)](#adversary-in-the-middle-aitm)

* [Anonymous Network Detection](#anonymous-network-detection)

* [Bot Detection](#bot-detection)

* [Email Reputation](#email-reputation)

* [Geovelocity Anomaly](#geovelocity-anomaly)

* [IP Reputation](#ip-reputation)

* [IP Velocity](#ip-velocity)

* [New Device](#new-device)

* (Workforce only) [PingID Device Trust](#pingid-device-trust)

* [Suspicious Device](#suspicious-device)

* [Traffic Anomaly](#traffic-anomaly)

* [User-Based Risk Behavior](#user-based-risk-behavior)

* [User Location Anomaly](#user-location-anomaly)

* [User Velocity](#user-velocity)

You can also customize the default predictors and supplement the default predictors with predictors of your own using custom and composite predictors.

Learn more about how the predictors work in [Testing predictors](p1_protect_testing_risk_predictors.html).

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | The PingOne Risk license allows you to use the following predictors in your risk policies. The remaining predictors require a PingOne Protect license.- Anonymous Network Detection

- Geovelocity Anomaly

- IP Reputation

- IP Velocity

- New Device

- User-Based Risk Behavior

- User Location Anomaly

- User VelocityTo upgrade your license to PingOne Protect and gain access to the additional predictors, contact your account team for more details. |

## Adversary-in-the-Middle (AitM)

Adversary-in-the-Middle (AitM) is a variant of Man-in-the-Middle attacks. In AitM, a malicious actor uses a reverse proxy to position themselves between a user and an online service to obtain user credentials and session tokens. This type of attack circumvents the protection provided by one-time passcode (OTP)-based multi-factor authentication (MFA) *(tooltip: \<div class="paragraph">
\<p>An electronic authentication method where a user is granted access only after presenting two or more verification factors for authentication.\</p>
\</div>)* and is a common technique in phishing attempts.

The predictor checks the domain name that the user is trying to access in order to identify AitM attacks.

When the risk evaluation result indicates an AitM attack, you should both block the attempt to access the resource and lock the user account because the malicious actors have obtained the user's credentials. The account should be unlocked only after the user password has been changed.

|   |                                                                       |
| - | --------------------------------------------------------------------- |
|   | The PingOne Signals (Protect) SDK is required for the AitM predictor. |

## Anonymous Network Detection

Malicious actors typically use anonymous networks, such as unknown VPNs, Tor, and proxies, to mask their IP address. PingOne Protect analyzes IP address data from a user's device to determine if the address originates from any type of anonymous network. If so, the user can be prompted for step-up authentication or denied access.

You can configure a fallback value for this predictor type to use if there's insufficient information to calculate a risk level. PingOne Protect also supports creating an allow list of networks, ensuring that legitimate VPN users can access authorized resources.

## Bot Detection

Bot attacks are becoming more prevalent with malicious actors using a wide variety of attack vectors, from credential stuffing and brute force attacks to password spraying and fake accounts.

PingOne Protect detects non-human activity, including agentic artificial intelligence (AI) automation, computer-using agents (CUAs), automated frameworks, and recorders.

To determine whether activity is bot-driven, the predictor analyzes the following:

* Browser fingerprint and environment inconsistencies

* Behavioral telemetry, such as mouse, keyboard, touch, and mobile sensors

* Device attributes and characteristics

* HTTP message signatures

If the predictor detects bot activity, the risk evaluation returns a high-risk result and recommends bot mitigation. PingOne Protect can also identify a subset of specific agent types in the risk evaluation response.

You can configure a fallback value for this predictor type to use if there's insufficient information to calculate a risk level.

This predictor uses rule-based conditions and patterns to detect risk. You can configure the predictor to exclude one or more rules, such as when a specific rule causes legitimate authentication attempts to be labeled as high risk. Learn more in [Predictor rules](p1_protect_predictor_rules.html).

|   |                                                                                |
| - | ------------------------------------------------------------------------------ |
|   | The PingOne Signals (Protect) SDK is required for the Bot Detection predictor. |

## Email Reputation

The use of disposable email addresses is a common characteristic of fraudulent activity. The Email Reputation predictor detects the use of disposable email addresses during registration.

You can add the predictor to your risk policies, and you can also define a specific course of action if the `result.recommendedAction` field in the risk evaluation response equals `TEMP_EMAIL_MITIGATION`, such as blocking the registration attempt.

## Geovelocity Anomaly

Users frequently sign on to the same application from multiple locations throughout the day. A time lapse between two sign-on locations that is shorter than the time it would take to travel between the two points could indicate suspicious activity. PingOne Protect analyzes location data to calculate if travel time between two session locations is physically possible. If the elapsed time is calculated to be impossible, the user can be prompted with step-up authentication or denied access.

For example, if a user signs on to an application from the United States and then attempts to sign on again 2 hours later from Japan, the Geovelocity Anomaly predictor alerts on this anomaly.

You can configure a fallback value for this predictor type to use if there's insufficient information to calculate a risk level. You can customize a Geovelocity Anomaly predictor by creating an allow list of IP addresses for which these time and distance calculations should be ignored.

## IP Reputation

IP addresses that have been involved in malicious activities, such as distributed denial-of-service (DDoS) attacks or spam activity, are considered risky. The more frequently an IP address is used for malicious activities, the higher its risk score. If a user attempts to access an application that is associated with an IP address previously involved with suspicious activity, the probability of potentially risky behavior increases. PingOne Protect analyzes data from different intelligence sources to determine the probability an IP address is associated with malicious activity and to request stronger authentication to verify the user's identity.

You can configure a fallback value for this predictor type to use if there's insufficient information to calculate a risk level. You can also customize an IP Reputation predictor by creating an allow list of IP addresses for which the IP Reputation score should be ignored.

## IP Velocity

Compromised accounts can be associated with many different IP addresses. PingOne Protect detects the number of IP addresses a user is leveraging and alerts on anomalies. This predictor learns user behavior and dynamically adjusts the thresholds for each user. For example, if a user attempts to access their account from six different IP addresses within a short time frame, the IP Velocity model detects an anomaly.

## New Device

New Device predictors allow your risk policy to take into account the risk associated with users trying to access applications from unknown devices or devices that have not been used in the past 12 months.

The New Device predictor identifies individual devices using the following attributes and checks for the attributes in the following order:

1. External device ID: If you want to maintain your own device IDs, you can assign external device IDs that are not managed by the PingOne Signals (Protect) SDK (for example, device serial number or mobile application installation ID).

   An example scenario where you might use external device IDs is if your mobile native app incorporates a WebView. In such cases, the mobile Signals SDK and the web Signals SDK provide different device IDs. By providing your own external device IDs, you have a consistent ID to identify devices. External device ID can be [mapped through the API](https://developer.pingidentity.com/pingone-api/protect/risk-evaluations.html) or in a [DaVinci flow using the PingOne Protect connector](https://docs.pingidentity.com/connectors/p1_protect_connector.html).

2. Device ID: When you implement the Signals SDK, it generates and stores a device ID for each user device. If the SDK payload has been successfully sent to the risk evaluation, you see a `deviceID` field in the response to the Create Risk Evaluation API request.

3. Cookie + user agent: Set a persistent cookie and the user agent using the API, the PingOne Protect connector in a DaVinci flow, or [PingOne Protect nodes](https://docs.pingidentity.com/auth-node-ref/latest/pingone/pingone-protect-evaluation.html) in a PingOne Advanced Identity Cloud or PingAM user journey.

You can configure a fallback value for this predictor type to use if there's insufficient information to calculate a risk level. Optionally, you can set an activation date for the model to restart the learning process and ignore all devices identified before this date.

Retention for historical data is managed centrally in [Protect Settings](p1_protect_general_protect_settings.html).

## PingID Device Trust

With the rise in cybersecurity and data breaches, it's best practice for your organization to use a device trust process to safeguard your internal and customer data. The PingID Device Trust predictor allows PingOne to establish device trust with your organization's workstations, adds further security to your user sign-on flows, and reduces risk through the PingID device trust agent.

The PingID Device Trust agent is a lightweight application used in workforce use cases to add contextual data from your organization's workstations during user sign-on flows. To use the PingID Device Trust predictor in a PingOne Protect risk policy, you must install the PingID Device Trust agent on workstations from which your organization's employees sign on to corporate applications. The following contextual data can be added to flows:

* Operating system details, including type, version, patch level, and update status

* Device identification, including external device ID if you're using a third-party device hygiene system

* User authorization and authentication information on the device

Based on the information collected by the agent, PingOne Protect can establish device trust by determining if the device is known or unknown and includes the trust status in the risk evaluation response, such as `TRUST_VERIFIED` or `TRUST_VERIFICATION_FAILED`.

You can configure a fallback value for this predictor type to use if there's insufficient information to calculate a risk level.

Learn more in [Using the PingID Device Trust agent](../strong_authentication_mfa/p1_using_the_workforce_trust_agent.html).

|   |                                                              |
| - | ------------------------------------------------------------ |
|   | The PingID Device Trust predictor requires a PingID license. |

## Suspicious Device

The Suspicious Device predictor checks for suspicious settings or mismatches between browser, operating system, and hardware attributes to detect emulators, super user permissions, virtual machines, mirroring applications, tampered devices and more. PingOne Protect detects suspicious devices by analyzing various data points, including:

* Operating system

* Browser type and version

* Hardware information

* Device settings

Using these data points, the predictor can differentiate between legitimate and suspicious devices and doesn't require any device history to detect anomalies. For example, the Suspicious Device predictor can detect attempts to attack with mobile emulators and flags such activity as high risk.

You can configure a fallback value for this predictor type to use if there's insufficient information to calculate a risk level.

You can also specify that the predictor requires that the payload from the Signals (Protect) SDK be provided as a signed JWT.

This predictor uses rule-based conditions and patterns to detect risk. You can configure the predictor to exclude one or more rules, such as when a specific rule causes legitimate authentication attempts to be labeled as high risk. Learn more in [Predictor rules](p1_protect_predictor_rules.html).

|   |                                                                                    |
| - | ---------------------------------------------------------------------------------- |
|   | The PingOne Signals (Protect) SDK is required for the Suspicious Device predictor. |

## Traffic Anomaly

The Traffic Anomaly predictor detects traffic anomalies, such as brute force attacks, by monitoring various data points, including users, devices, and sessions. Currently, the predictor:

* Detects situations where there are a large number of risk evaluations requested for a single user within a short period of time

* Optionally can detect situations where the number of users per device during a given period of time is suspicious

* Flags these activities as high risk

The Traffic Anomaly predictor will eventually include additional rules, some of which you'll be able to enable or disable.

When a risk level of high is calculated for a Traffic Anomaly predictor, the `result.recommendedAction` field in the risk evaluation response returns the value `DENY`. In these situations, you should deny access because the repeated risk evaluations are likely a sign of a brute force attack.

This predictor uses rule-based conditions and patterns to detect risk. You can configure the predictor to exclude one or more rules, such as when a specific rule causes legitimate authentication attempts to be labeled as high risk. Learn more in [Predictor rules](p1_protect_predictor_rules.html).

## User-Based Risk Behavior

The User-Based Risk Behavior model compares a transaction with the typical behavior of that specific user. For example, if a user accesses an application that they rarely use, User-Based Risk Behavior detects an anomaly.

User-Based Risk Behavior is a machine-learning model that continuously updates. The model learns each user's behavior from various data points, including:

* Operating system

* Browser type and version

* Activity time frame

* Geolocation (country)

* Application being accessed

* Device settings and characteristics

The machine-learning model characterizes abnormal activity as low, medium, or high risk. Thresholds for this predictor are dynamic and might change between different users.

You can configure a fallback value for this predictor type to use if there's insufficient information to calculate a risk level.

The predictor also includes an option to have PingOne Protect attempt to detect compromised user accounts and take this into account when calculating the risk level for the predictor. If you enable this option, you can also define an account recovery course of action for cases where the `result.recommendedAction` field in the risk evaluation response equals `ACCOUNT_RECOVERY`.

Retention for historical data is managed centrally in [Protect Settings](p1_protect_general_protect_settings.html).

|   |                                                                                                |
| - | ---------------------------------------------------------------------------------------------- |
|   | The PingOne Signals (Protect) SDK is required for the user-based risk behavior predictor type. |

## User Location Anomaly

User Location Anomaly predictors allow you to define a radius around the location of the previous successful sign-on attempts. If a sign-on attempt occurs at a location whose distance from the user's expected location is greater than the radius you defined, it's considered medium or high risk, depending on the extent of the deviation from the defined radius. This information can be used in authentication policies to reduce the risk of unintentional push notification approval and account takeover (ATO) attacks.

The default radius is 50 kilometers. The units for the radius can be set to miles or kilometers. The smallest radius that can be defined is 10 miles (16 KM) and the largest is 100 miles (160 KM).

You can also configure a fallback value to use if there's insufficient information to calculate a risk level.

Retention for historical data is managed centrally in [Protect Settings](p1_protect_general_protect_settings.html).

## User Velocity

Stolen user accounts are becoming more common. A malicious user can have multiple sets of credentials originating from the same IP address. PingOne Protect detects the number of users originating from the same IP address and alerts on anomalies.

For example, if a workforce organization has 50 users who typically work from the same IP address at their office location, but 100 users attempt to authenticate from this IP address, the user velocity model alerts on this anomaly. Thresholds for this predictor are changed dynamically.

## IP address selection

PingOne Protect is most effective when provided with a valid public, routable client IP address. Several risk predictors depend on IP-based context, such as the Geovelocity Anomaly, IP Velocity, and IP Reputation predictors. When the IP is private, internal, or represents an intermediary, such as a proxy or web application firewall (WAF), instead of an end user, PingOne Protect has less reliable network and location context, reducing detection accuracy and increasing false positives.

Nonroutable IP addresses are private network ranges (such as 10.0.0.0/8, 172.16.0.0/12, and 192.168.0.0/16) that can't be routed over the public internet and are used for internal networking behind network address translation (NAT), firewalls, or routers. Devices using nonroutable IP addresses share a public IP when accessing the internet through NAT.

PingOne Protect uses the following priority order to select an IP address for risk evaluations:

1. If `event.ip` is routable, `event.ip` is used for evaluations.

2. If `event.ip` is nonroutable, the Signals SDK attempts to identify a user's public IP address for evaluations.

3. If the Signals SDK output isn't available, `event.ip` is used for evaluations, even if the value is nonroutable.

## Customizing predictors

|   |                                                                                           |
| - | ----------------------------------------------------------------------------------------- |
|   | Customize predictors only after you've accumulated sufficient event data and analyzed it. |

When you define your own risk policies, you might be satisfied to use the out-of-the-box predictors provided and adjust the degree to which each predictor is taken into account. If you want to further refine the process, you can customize the individual predictors.

The PingOne Protect predictors can be:

* Customized instances of the basic predictor types

* Multiple risk predictors combined into a single composite predictor

* Custom predictors that use risk data from external sources

There are three ways to customize the predictors that can be included in risk policies:

* Fine-tune out-of-the-box predictors

  You can customize the out-of-the-box predictors by:

  * Renaming the predictor

  * Editing the settings contained in some predictors.

  For example, for the **IP Reputation** predictor, you can modify the fallback decision value or add a list of IPs that should always be considered low risk.

  In addition to changing the settings of some default predictors, you can create additional predictors of certain types. For example, you can create:

  * A predictor of type **User Location Anomaly** called `Strict User Location Anomaly` with the distance set to 20 km and the fallback value set to **High** risk.

  * A second predictor of type **User Location Anomaly** called `Lenient User Location Anomaly` with the distance set to 50 km and the fallback value set to **Medium** risk.

  This makes it easy for you to include the strict predictor in a risk policy that you use for highly-sensitive applications and include the more lenient predictor in a risk policy that you use for less-sensitive applications.

* Create composite predictors

  Each out-of-the-box risk predictor represents a single risk factor. In some cases, you might need to combine multiple risk predictors and factors into a single predictor, such as when you're concerned about the use of an anonymous network only when a user location anomaly is also reported. This is where composite predictors come in.

  In a composite predictor, you define conditions based on individual predictors, and you decide what level of risk should be assigned when the defined conditions are and are not met. Composite predictors can include both the standard predictor types provided and any custom predictors that you have created in addition to several risk factors, such as country and IP range.

  In addition to taking into account the results of multiple individual risk predictors, you can include conditions that relate to the total number of predictors in a policy that were **Low**, **Medium**, or **High** risk.

  Learn more in [Adding composite predictors](p1_protect_adding_composite_predictors.html).

* Create custom predictors

  In addition to including the out-of-the-box predictors in a risk policy, you can create custom predictors to include other sources of risk in your risk policies.

  Custom predictors can include the following types of comparisons:

  * Numerical comparisons, using ranges you have defined for **Low**, **Medium**, and **High** risk

  * Checking if an IP falls into a range of IPs that you have defined

  * String-matching

    Find descriptions of the types of information that you can include as a custom predictor in the fields for the details and event objects in the **Details data model** and **Event data model** tables in the [Risk evaluations section](https://developer.pingidentity.com/pingone-api/protect/risk-evaluations.html) of the PingOne API documentation. You can also refer to the [sample response](https://developer.pingidentity.com/pingone-api/protect/risk-evaluations/create-risk-evaluation.html) to see an example Create risk evaluation API request.

    Learn more in [Adding custom predictors](p1_protect_adding_custom_predictors.html).

---

---
title: Protect Settings
description: Use the Protect Settings page to specify maximum data retention periods for the risk data used by specific predictors.
component: pingone
page_id: pingone:threat_protection_using_pingone_protect:p1_protect_general_protect_settings
canonical_url: https://docs.pingidentity.com/pingone/threat_protection_using_pingone_protect/p1_protect_general_protect_settings.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  predictor-retention-periods: Predictor retention periods
---

# Protect Settings

Use the **Protect Settings** page to set maximum data retention periods for the risk data used by specific predictors that rely on historical context. Retention periods are centrally configured on this page per environment and applied to the supported predictors.

Centralized data retention provides:

* Improved model learning, anomaly detection, and risk evaluation.

* Operational consistency.

* Alignment with privacy and compliance requirements, including the California Consumer Privacy Act (CCPA) and the EU General Data Protection Regulation (GDPR).

Data older than the configured threshold is securely and automatically deleted by scheduled cleanup processes. You can review retention period changes and deletion activity in the [PingOne audit logs](../monitoring/p1_running_audit_report.html).

To change the data retention periods, in the PingOne admin console, go to **Threat Protection > Protect Settings**.

## Predictor retention periods

You can define different data retention periods in days for each of the following risk predictors:

* New Device

* User-Based Risk Behavior

* User Location Anomaly

|   |                                                                                                                                     |
| - | ----------------------------------------------------------------------------------------------------------------------------------- |
|   | When you modify the maximum data retention period, the new period applies only to new data collected after you changed the setting. |