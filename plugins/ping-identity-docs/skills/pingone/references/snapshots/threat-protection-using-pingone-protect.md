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
