---
title: Actions
description: Actions represent arbitrary values that a typical authorization request might ask to perform on a specific resource, such as view or update.
component: pingauthorize
version: 11.1
page_id: pingauthorize:pingauthorize_policy_administration_guide:paz_actions
canonical_url: https://docs.pingidentity.com/pingauthorize/11.1/pingauthorize_policy_administration_guide/paz_actions.html
llms_txt: https://docs.pingidentity.com/pingauthorize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 22, 2024
---

# Actions

Actions represent arbitrary values that a typical authorization request might ask to perform on a specific resource, such as view or update.

Common actions you might want to configure in the PingAuthorize Policy Editor are:

* `inbound-GET`

* `inbound-PATCH`

* `inbound-POST`

* `inbound-PUT`

* `outbound-GET`

* `outbound-PATCH`

* `outbound-POST`

* `outbound-PUT`

* `create`

* `delete`

* `modify`

* `retrieve`

* `search`

* `search-results`

---

---
title: Adding a named condition
description: Add named conditions to reuse conditional logic across attributes and policies.
component: pingauthorize
version: 11.1
page_id: pingauthorize:pingauthorize_policy_administration_guide:paz_named_conditions
canonical_url: https://docs.pingidentity.com/pingauthorize/11.1/pingauthorize_policy_administration_guide/paz_named_conditions.html
llms_txt: https://docs.pingidentity.com/pingauthorize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 11, 2026
section_ids:
  steps: Steps
  choose-from: Choose from:
---

# Adding a named condition

Named conditions provide a way to reuse conditional logic across attributes and policies.

Named conditions can help provide consistency in authorization logic and minimize repetition throughout policies. You can use named conditions as components in more complicated condition expressions.

For example, consider a named condition that compares the account status received in a decision request to a status code to determine if the account is blocked. You can use this condition in multiple policies to check a user's account status.

![Screen capture of an example named condition named Account Blocked, comparing the Request.Account.Status and Policy.Constants.Block Status Code attributes](_images/wkq1714675950511.png)

## Steps

1. In the Policy Editor, click **Trust Framework**, and then click the **Conditions** tab.

2. Click the **[icon: plus, set=fa]**icon.

3. Define general information for the named condition:

   1. Enter a unique **Name** for the condition.

   2. (Optional) For **Description**, enter information that describes the condition's purpose.

   3. (Optional) To nest the condition under a parent in the tree, in the **Parent** list, select a parent condition.

      Nesting helps group related conditions together. You can move the condition to another location in the tree by selecting a different parent condition.

      To remove nesting, click the **Delete** icon and leave the **Parent** blank.

4. To add a comparison to the condition, click **[icon: plus, set=fa]Comparison**.

   ![Screen capture of the condition builder](_images/mle1714676068481.png)

5. Select an attribute to use in the comparison, select a comparator, and then enter a constant or click the **C** icon to select an attribute.

6. To nest a comparison under another comparison, click **[icon: plus, set=fa]Group**.

   Subgroups allow more permutations in comparisons. To remove nesting while keeping the comparison, click **Ungroup**.

7. To reference an existing named condition within this condition, click **[icon: plus, set=fa]Named Condition**, select the condition to reference, and then select **is True or False**.

8. To combine multiple conditions, named conditions, or groups, select one of the following options.

   ### Choose from:

   * **All**: Invokes the condition when all of the conditions are true. If one condition evaluates to false, evaluation stops and the remaining conditions are not executed. This is equivalent to an `AND` Boolean operator between conditions.

   * **Any**: Invokes the condition when at least one of the conditions is true. If one condition evlautes to true, evaluation stops and the remaining conditions are not executed. This is equivalent to an `OR` Boolean operator between conditions.

   * **None**: Invokes the condition when none of the conditions are true. This is equivalent to a `NOT` Boolean operator between conditions.

9. Click **Save Changes**.

   |   |                                                                                                                                                                                                                                                                       |
   | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | You can copy a named condition for reuse by selecting **Make Copy** from the hamburger menu of that condition. If you copy a named condition with children, only the parent is duplicated. You cannot copy a named condition at its point of use in a rule or policy. |

---

---
title: Adding attributes to an allow list
description: To allow the user to modify a set of attributes limited to an allow list and return an error if the user attempts to modify any attribute outside of the allow list, create a constant in the Trust Framework and then use the constant in a policy.
component: pingauthorize
version: 11.1
page_id: pingauthorize:pingauthorize_policy_administration_guide:paz_whitelisting_attrs
canonical_url: https://docs.pingidentity.com/pingauthorize/11.1/pingauthorize_policy_administration_guide/paz_whitelisting_attrs.html
llms_txt: https://docs.pingidentity.com/pingauthorize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 10, 2023
section_ids:
  steps: Steps
---

# Adding attributes to an allow list

To allow the user to modify a set of attributes limited to an allow list and return an error if the user attempts to modify any attribute outside of the allow list, create a constant in the Trust Framework and then use the constant in a policy.

## Steps

1. Create a constant in the Trust Framework.

   1. Go to **Trust Framework** and then **Attributes**.

   2. From the **[icon: plus, set=fa]**menu, select **Add new Attribute**.

   3. For the name, replace **Untitled** with `allowlistAttributes`.

   4. Verify that in the **Parent** field, no parent is selected. To remove a parent, click the delete icon to the right of the **Parent** field.

   5. Click **[icon: plus, set=fa]Add Resolver** and set the **Resolver type** to **Constant**.

   6. Set the value of the constant to a set of square brackets that contains a comma-delimited list of the attributes that can be modified.

      For example, to allow the `email` or `userName` attributes to be modified, you would set the value of the constant to `[email, userName]`.

   As another example, to allow the user to modify a property or any of its subproperties, you must explicitly list them. So to allow modification of the `name` field on the default Users pass-through schema, set the value of the constant to `[name, name.formatted, name.givenName, name.familyName]`.

   1. In the **Value Settings** section, set **Type** to **Collection**.

   2. Click **Save changes**.

2. Modify or create a policy to use that constant collection.

   1. Go to **Policies**.

   2. Select a policy or create a new one.

   3. In the **Rules** section:

      1. Set the **Combining Algorithm** to **Unless one decision is permit, the decision will be deny**.

      2. Click **[icon: plus, set=fa]Add Rule**.

      3. For the name, replace **Untitled** with `Allow only the email and userName attributes`.

      4. Set the **Effect** to **Permit.**

      5. Under **Condition**, click **[icon: plus, set=fa]Comparison**.

      6. In the comparison, we want to compare the constant collection of permitted attributes to the `impactedAttributes` collection.

         * For the left field, select the `allowlistAttributes` attribute, which is the constant collection of permitted attributes defined in the beginning.

           You might see the field as shown below. Click the **R** immediately above **[icon: plus, set=fa]Comparison** to toggle to attribute selection.

           ![Screen capture that shows the Condition section with the R toggle](_images/zwg1585841925352.png)

         * Set the middle field (the operator) to **Contains**.

         * Set the right field to the `impactedAttributes` attribute.

           If that field has a **C** before it, click the **C** to toggle to attribute selection.

           |   |                                                                                                                          |
           | - | ------------------------------------------------------------------------------------------------------------------------ |
           |   | If `impactedAttributes` is not available, see [Restricting the modification of attributes](paz_restrict_attrs_mod.html). |

   When applied to two collections, the **Contains** operator returns true if and only if the right-side collection is a subset of the left-side collection. Thus, the rule only returns `permit` if the set of `impactedAttributes` is a subset of the list of allowed attributes in `allowlistAttributes`.

---

---
title: Adding targets to a policy
description: Add targets to identify the requests to which the policy applies its fine-grained authorization logic. If no targets are attached to a policy, the policy applies to all requests. To make a policy only apply for all requests to a certain database, for example, add the database domain as a target.
component: pingauthorize
version: 11.1
page_id: pingauthorize:pingauthorize_policy_administration_guide:paz_add_targets_policy
canonical_url: https://docs.pingidentity.com/pingauthorize/11.1/pingauthorize_policy_administration_guide/paz_add_targets_policy.html
llms_txt: https://docs.pingidentity.com/pingauthorize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 30, 2023
section_ids:
  steps: Steps
  example: Example
---

# Adding targets to a policy

Add targets to identify the requests to which the policy applies its fine-grained authorization logic. If no targets are attached to a policy, the policy applies to all requests. To make a policy only apply for all requests to a certain database, for example, add the database domain as a target.

## Steps

1. Go to the policy where you want to add targets.

2. Click the [icon: plus, set=fa]next to Applies to.

3. In the left pane, click Components.

   The list of components includes the items you created in the Trust Framework. Drag the appropriate domains, services, identity classes, and actions from the components to the Applies to target section on the policy.

   For example, to target Mobile Banking requests, drag that domain in. To target all banking groups, add the Banking Channels domain, which is the parent of the Online Banking and Mobile Banking domains. Because the top level is also a target, this step adds a total of three targets.

   ![Screen capture of the Components tab showing Rules, Targets, Statements, Domains, and Services](_images/siw1687904312770.png)

4. Click Save changes.

## Example

The following example features three domains because the Banking Channels definition is the parent of the other definitions. Logically, applying an OR operation within the definition type selects one of the channels.

The following graph shows how the server evaluates the group of targets.

![Diagram showing evaluation of targets with OR operations between domains, an OR operation between actions, and then AND operations across domains, services, and actions](_images/top1577128602273.png)

---

---
title: Allowing attributes to be modified by administrators
description: To allow any attribute to be modified, such as for an administrator account, the policy decision point (PDP) does not need to check the impactedAttributes attribute.
component: pingauthorize
version: 11.1
page_id: pingauthorize:pingauthorize_policy_administration_guide:paz_allow_attrs_mod
canonical_url: https://docs.pingidentity.com/pingauthorize/11.1/pingauthorize_policy_administration_guide/paz_allow_attrs_mod.html
llms_txt: https://docs.pingidentity.com/pingauthorize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 10, 2023
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Allowing attributes to be modified by administrators

To allow any attribute to be modified, such as for an administrator account, the policy decision point (PDP) does not need to check the `impactedAttributes` attribute.

## About this task

To create a policy that allows an administrator to modify any attributes, complete the following step.

## Steps

* Create a policy, and then add a rule with the Effect set to Permit the decision based on the Condition that the user is an administrator.

  To check the user, for example, you can set up a condition to compare whether `HttpRequest.AccessToken.scope` equals `administrator`.

---

---
title: Attribute caching
description: The policy decision point (PDP) and the PingAuthorize Policy Editor support caching for attributes. The ability to cache resolved attributes can deliver significant performance gains for the PDP.
component: pingauthorize
version: 11.1
page_id: pingauthorize:pingauthorize_policy_administration_guide:paz_attr_caching
canonical_url: https://docs.pingidentity.com/pingauthorize/11.1/pingauthorize_policy_administration_guide/paz_attr_caching.html
llms_txt: https://docs.pingidentity.com/pingauthorize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 29, 2026
section_ids:
  caching-strategies: Caching strategies
  caching-behavior: Caching behavior
---

# Attribute caching

The policy decision point (PDP) and the PingAuthorize Policy Editor support caching for attributes. The ability to cache resolved attributes can deliver significant performance gains for the PDP.

This section focuses on the individual cache options that you can set at the attribute level. See [Configuring Trust Framework attribute caching for development](../pingauthorize_server_administration_guide/paz_tf_attribute_cache_external.html) or [Configuring Trust Framework attribute caching for production](../pingauthorize_server_administration_guide/paz_tf_attribute_cache_embedded.html) for more information.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | When using AWS ElastiCache for external Redis caching, you can use static credentials or IAM authentication as the authentication method. If you choose IAM authentication, you must restart the PingAuthorize Server to fall back to static credentials.IAM authentication failures can reveal service or attribute cache errors. Learn more about how to resolve these in [Troubleshooting AWS IAM authentication issues](../troubleshooting_pingauthorize_server/paz_troubleshoot_aws_iam_auth_issues.html). |

## Caching strategies

Attribute caching can be indefinite or time-limited, with or without the scope of another attribute value:

* With time-limited caching, you set the duration for which the cache lives (**Time to Live**) before it expires.

* With **Scope** set to an attribute, the cached value remains valid as long as that attribute's value stays the same. If the scope attribute's value changes, the system invalidates the cache for the attribute you're defining.

  In the following example, as long as the `sessionId` value remains the same, the value of the attribute you're defining is cached. When the `sessionId` changes, the system invalidates the cache and uses normal resolution:

  ![Screen capture of the Caching section settings for a Trust Framework attribute](_images/paz-time-limited-caching-with-scope-attribute.png)

## Caching behavior

Attribute caching uses a one-level approach where cache entries are stored and retrieved from the single configured cache type. If the attribute does not exist in the cache, the PDP resolves the attribute automatically by using the appropriate attribute resolvers and then adds it to the cache. All subsequent attribute usages use the cached value until it expires from the cache, which results in another attribute resolution.

|   |                                                                                                                                                                                                                                                                                                                                     |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The cache key for a Trust Framework attribute value includes a hash of the values required for it to resolve. If one of these values changes, the cache key automatically becomes invalid. You can think of this arrangement as an aggregation of `Scope` parameters that guard against inconsistencies between your cached values. |

---

---
title: Attribute interpolation
description: With attribute interpolation, you reference an attribute in a field. The system resolves the value of the referenced attribute, replacing the reference with the value itself.
component: pingauthorize
version: 11.1
page_id: pingauthorize:pingauthorize_policy_administration_guide:paz_attribute_interpolation
canonical_url: https://docs.pingidentity.com/pingauthorize/11.1/pingauthorize_policy_administration_guide/paz_attribute_interpolation.html
llms_txt: https://docs.pingidentity.com/pingauthorize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: October 7, 2022
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Attribute interpolation

With attribute interpolation, you reference an attribute in a field. The system resolves the value of the referenced attribute, replacing the reference with the value itself.

## About this task

You can use attribute interpolation in any field that has the label icon, shown below.

![Icon of a Trust Framework attribute](_images/qky1588961068221.png)

## Steps

1. To reference an attribute in one of these fields, type two open curly brackets (`\{\{`) to open the attribute tree menu. Continue typing the full path to the attribute or select each level of the attribute in the attribute tree menu.

   ![Screen capture showing two open curly braces opening the attribute tree menu to reference Test or children of Test](_images/pmx1588962041620.png)

2. Complete the reference by typing two close curly brackets (`}}`) or by selecting the **}} complete expression** item from the attribute tree menu.

   ![Screen capture showing the attribute tree menu with options for the attribute reference Test.Child](_images/sgl1588962176262.png)

---

---
title: Attribute name, description, and location
description: You can give attributes any name that is unique and does not contain a period (.).
component: pingauthorize
version: 11.1
page_id: pingauthorize:pingauthorize_policy_administration_guide:paz_attr_name_desc_loc
canonical_url: https://docs.pingidentity.com/pingauthorize/11.1/pingauthorize_policy_administration_guide/paz_attr_name_desc_loc.html
llms_txt: https://docs.pingidentity.com/pingauthorize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 5, 2023
---

# Attribute name, description, and location

You can give attributes any name that is unique and does not contain a period (.).

To ensure that the system can interpolate the attribute, avoid the following characters:

* `{`

* `}`

* `|`

You can give the attribute a description to help policy editors understand the attribute's purpose. This description is only displayed when a user navigates to the attribute.

You can change the location of an attribute in the attribute tree using the Parent field.

---

---
title: Attributes
description: Attributes provide the context that enables fine-grained policies.
component: pingauthorize
version: 11.1
page_id: pingauthorize:pingauthorize_policy_administration_guide:paz_attributes
canonical_url: https://docs.pingidentity.com/pingauthorize/11.1/pingauthorize_policy_administration_guide/paz_attributes.html
llms_txt: https://docs.pingidentity.com/pingauthorize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 29, 2022
---

# Attributes

Attributes provide the context that enables fine-grained policies.

Attribute values come from a multitude of sources. You can use the original values or modify the values. You can then use the final values in other attributes, [Adding a named condition](paz_named_conditions.html), or rules.

The system resolves an attribute only when its value is required as part of the decision request evaluation. For example, if a rule checks whether a customer's device "Risk Score" is high, then the system only attempts to resolve the attribute corresponding to "Risk Score" if that rule is required.

---

---
title: Branch changes and history
description: "After creating branches to organize your organizations' distinct work contexts, you can commit changes to policies and the Trust Framework, revert unwanted changes, or create snapshots of important policy states."
component: pingauthorize
version: 11.1
page_id: pingauthorize:pingauthorize_policy_administration_guide:paz_managing_change_history
canonical_url: https://docs.pingidentity.com/pingauthorize/11.1/pingauthorize_policy_administration_guide/paz_managing_change_history.html
llms_txt: https://docs.pingidentity.com/pingauthorize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 16, 2025
---

# Branch changes and history

After creating [branches](paz_managing_branches.html) to organize your organizations' distinct work contexts, you can commit changes to policies and the Trust Framework, revert unwanted changes, or create snapshots of important policy states.

Learn more about branch changes and history:

* [Committing changes](paz_commit_changes.html)

* [Reverting changes](paz_revert_changes.html)

* [Creating a snapshot](paz_generate_snapshots.html)

* [Merging snapshots](paz_merge_snapshot.html)

---

---
title: Combining algorithms
description: Policies can combine multiple rules to produce a Permit, Deny, Indeterminate, or Not Applicable decision.
component: pingauthorize
version: 11.1
page_id: pingauthorize:pingauthorize_policy_administration_guide:paz_rules_combine_algs
canonical_url: https://docs.pingidentity.com/pingauthorize/11.1/pingauthorize_policy_administration_guide/paz_rules_combine_algs.html
llms_txt: https://docs.pingidentity.com/pingauthorize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 23, 2025
section_ids:
  ca_evaluate_all: Evaluate all
  example-detecting-fraud-with-full-rule-visibility: "Example: Detecting fraud with full rule visibility"
---

# Combining algorithms

Policies can combine multiple rules to produce a `Permit`, `Deny`, `Indeterminate`, or `Not Applicable` decision.

To evaluate the overall decision of a policy, the policy decision point (PDP) applies a combining algorithm. The default algorithm that is set on a new policy is **The first applicable will be the final decision**. If the [evaluate all](#ca_evaluate_all) option isn't selected, this algorithm stops evaluating as soon as it reaches a decision that is not `Not Applicable`.

The following table identifies available combining algorithms and describes their effects. The diagrams show one example of a decision evaluation for each combining algorithm; other evaluation paths are possible. The diagram legend is displayed before the table. The first column in each diagram represents the overall decision returned by the policy. The second column represents child decisions that produce the resulting policy decision.

![Legend for the combining algorithm diagrams.](_images/paz-combining-algorithm-legend.png)

| Combining algorithm                                                                                                                                                                                                                                                                       | Details                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **A single permit will override any deny decisions**![Diagram showing an example path for single permit overriding any deny decisions.](_images/paz-ca-single-permit-overrides.png)                                                                                                       | If any children produce the decision `Permit`, the policy returns `Permit` and stops evaluating rules.If no `Permit` is generated, all rules are evaluated. The policy returns `Indeterminate` if a child produces `Indeterminate`. Otherwise, the policy returns `Deny` if a child produces `Deny`.If none of the previous situations occur, the policy returns `Not Applicable`.                                                                                            |
| **A single deny will override any permit decisions**![Diagram showing an example path for single deny overriding any permit decisions.](_images/paz-ca-single-deny-overrides.png)                                                                                                         | If any children produce the decision `Deny`, the policy returns `Deny` and stops evaluating rules.If no `Deny` is generated, all rules are evaluated. The policy returns `Indeterminate` if a child produces `Indeterminate`. Otherwise, the policy returns `Permit` if a child produces `Permit`.If none of the previous situations occur, the policy returns `Not Applicable`.                                                                                              |
| **Unless one decision is deny, the decision will be permit**![Diagram showing an example path for unless one decision is deny, the decision will be permit.](_images/paz-ca-unless-deny-permit.png)                                                                                       | The policy defaults to `Permit` unless any of its children produce the decision `Deny`. The evaluation of rules stops as soon as a `Deny` is produced.                                                                                                                                                                                                                                                                                                                        |
| **Unless one decision is permit, the decision will be deny**![Diagram showing an example path for unless one decision is permit, the decision will be deny.](_images/paz-ca-unless-permit-deny.png)                                                                                       | The policy defaults to `Deny` unless any of its children produce the decision `Permit`. The evaluation of rules stops as soon as a `Permit` is produced.                                                                                                                                                                                                                                                                                                                      |
| **The first applicable decision will be the final decision**![Diagram showing an example path for the first applicable decision will be the final decision.](_images/paz-ca-first-applicable.png)                                                                                         | Evaluates the children in turn until one produces an applicable value of `Permit`, `Deny`, or `Indeterminate`. If the evaluation produces no applicable decisions, the policy returns `Not Applicable`.                                                                                                                                                                                                                                                                       |
| **Only one child may produce a decision. If more than one is produced, the result will be indeterminate**![Diagram showing an example path for only one child may produce a decision. If more than one is produced, the result will be indeterminate.](_images/paz-ca-only-one-child.png) | Evaluates the children in turn. If at any point two children produce a decision other than `Not Applicable`, evaluation stops, and the policy returns `Indeterminate`. If at any point a single child produces an `Indeterminate` decision, evaluation stops, and the policy returns `Indeterminate`.If exactly one child produces an applicable decision, the policy uses it. If the evaluation produces no applicable decisions, the policy returns `Not Applicable`.       |
| **Permit if the weighted average of applicable child decisions meets the threshold, otherwise deny**![Diagram showing an example path for a group of rules evaluating to a final decision based on their weights and a decision threshold value](_images/paz-ca-weighted-average.png)     | Assigns the policy's children weights between `0` and `100`. If a child returns `Permit`, the weight is added to a running total. If a child returns `Deny`, the weight is subtracted from the running total.After evaluating all children, the PDP divides the total by the number of children and compares that average against the threshold. If the average is greater than or equal to the threshold, the policy returns `Permit`. Otherwise, the policy returns `Deny`. |

## Evaluate all

By default, combining algorithms stop evaluating a policy's child elements as soon as a final decision is reached. For example, when using the **The first applicable decision will be the final decision** combining algorithm, evaluation ends immediately if any child returns a `Permit` or `Deny`.

To override this behavior and ensure that all child policies or rules are evaluated, select the **Evaluate All** checkbox next to the **Combining Algorithm** list.

![Screen capture of Evaluate All checkbox selected next to the Combining Algorithm list.](_images/paz-ca-evaluate-all.png)

Selecting **Evaluate All** ensures that every child element is evaluated, even if a final decision has already been reached. Although this behavior doesn't affect the final decision, it allows statement information, such as the reason for transaction denial, to propagate up to the parent policy. This information is useful for auditing, debugging, and understanding policy outcomes.

|   |                                                                                                                                                        |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | Even with **Evaluate All** selected, [targets](paz_add_targets_policy.html) still determine whether a policy or rule is evaluated for a given request. |

### Example: Detecting fraud with full rule visibility

Consider a bank that approves or denies transactions based on multiple risk signals. These signals are modeled as child rules under a **Fraud detection** policy, which uses the **A single deny will override any permit decisions** combining algorithm.

![Screen capture of the Fraud detection policy with four risk signal rules defined.](_images/paz-ca-fraud-detection-policy.png)

The policy includes the following rules:

* **Transaction amount exceeds threshold**: Denies if the transaction amount exceeds 10,000 USD.

* **Unusual geolocation**: Denies if the transaction originates from an IP or country not associated with the account.

* **New device used**: Denies if the transaction comes from a device not associated with the account.

* **Unusual transaction time**: Denies if the transaction occurs at an unusual time.

Each rule includes a `denied-reason` statement explaining why the rule denied the transaction.

With **Evaluate All** selected, the policy evaluates every rule, regardless of whether an earlier rule has returned a `Deny`. This provides analysts full visibility into every risk signal, helping detect fraud patterns, meet audit requirements, and enforce internal risk policies more effectively.

Without **Evaluate All** selected, the combining algorithm stops evaluating when the first `Deny` occurs, skipping evaluation of other potentially relevant rules. For example, if the transaction amount exceeds the threshold, the policy doesn't evaluate the geolocation or device rules, and their corresponding denial reasons aren't included in the final decision.

---

---
title: Committing changes
description: To save your policy and Trust Framework changes, commit your changes.
component: pingauthorize
version: 11.1
page_id: pingauthorize:pingauthorize_policy_administration_guide:paz_commit_changes
canonical_url: https://docs.pingidentity.com/pingauthorize/11.1/pingauthorize_policy_administration_guide/paz_commit_changes.html
llms_txt: https://docs.pingidentity.com/pingauthorize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 17, 2025
section_ids:
  steps: Steps
---

# Committing changes

To save your policy and Trust Framework changes, commit your changes.

After you finish building, testing, and analyzing your policies, commit the changes. Committed changes cannot be reverted.

After you commit changes, you can create a deployment package from the commit. Learn more in [Exporting a policy deployment package](../pingauthorize_server_administration_guide/paz_export_deployment_package.html).

## Steps

1. In the Policy Editor, click **Branch Manager**.

2. On the **Version Control** tab, select the branch in which to make the commit.

3. Click **Commit New Changes**.

   |   |                                                                                |
   | - | ------------------------------------------------------------------------------ |
   |   | For this button to become available, the branch must have uncommitted changes. |

---

---
title: Conditional targets (Applies to)
description: "You can use conditional targets to extend the capability of the \"Applies to\" concept when creating attribute-based access control (ABAC) rules and policies."
component: pingauthorize
version: 11.1
page_id: pingauthorize:pingauthorize_policy_administration_guide:paz_conditional_targets
canonical_url: https://docs.pingidentity.com/pingauthorize/11.1/pingauthorize_policy_administration_guide/paz_conditional_targets.html
llms_txt: https://docs.pingidentity.com/pingauthorize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 30, 2023
---

# Conditional targets (Applies to)

You can use conditional targets to extend the capability of the "Applies to" concept when creating attribute-based access control (ABAC) rules and policies.

Conditional targets extend the capability of the "Applies to" concept because they:

* Permit the interweaving of targets with other conditional logic.

* Allow standalone logic to determine if and when a policy or rule applies.

To enable this functionality, click **Applies to** and then **When**.

You can include the following types of conditions in a logical expression:

* Attribute comparison – Allows the comparison of an attributes *(tooltip: \<div class="paragraph">
  \<p>Distinct characteristics that describe a subject. If the subject is a website user, attributes can include a name, group affiliation, email address, and attributes alike.\</p>
  \</div>)* with another attribute or with a constant.

* Request comparison – Allows the matching of incoming requests by answering questions like "Is the requested service equal to `Banking.Payment`?"

* Named condition – Click **[icon: plus, set=fa]Named Condition** to show a **Named Condition** drop-down list that displays named conditions.

The following image provides an example. See [Conditions](paz_conditions.html) for more information.

![Screen capture of a target that applies to all requests when the Risk.Combined Score attribute is greater than 100 and the service is Banking.Payment](_images/pnh1577128693477.png)

You can navigate conditions using the Up Arrow and the Down Arrow to move between members of a group or using the Left Arrow and Right Arrow to move in and out of nested groups.

You can reorder conditions by dragging the handles on the left. To reorder using the keyboard, press Tab to go to the condition, press Enter to select the condition, press the Up Arrow or Down Arrow to go to the desired location, and press Enter to drop the condition in the new location.

To switch between Attribute Comparison mode and Request Comparison mode, click **A** and **R**, respectively, to the left of the comparator.

![Screen capture of the toggle to go between Attribute Comparison mode and Request Comparison mode.](_images/nxp1577128822227.png)

---

---
title: Conditions
description: Use conditions in PingAuthorize attributes, rules, and policies to define authorization logic by comparing one thing to another.
component: pingauthorize
version: 11.1
page_id: pingauthorize:pingauthorize_policy_administration_guide:paz_conditions
canonical_url: https://docs.pingidentity.com/pingauthorize/11.1/pingauthorize_policy_administration_guide/paz_conditions.html
llms_txt: https://docs.pingidentity.com/pingauthorize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 30, 2026
section_ids:
  paz_combining_conditions: Combining conditions
  condition_comparators: Condition comparators
---

# Conditions

Use conditions in PingAuthorize attributes, rules, and policies to define authorization logic by comparing one thing to another. Conditions evaluate to either `true` or `false`.

You can compare requests, attributes, constant values, and regular expressions in conditions. Conditions can also serve as [targets](paz_conditional_targets.html) that define when a policy or rule applies to a decision request. For example, you can target a rule so that it applies when a payment amount is greater than or equal to a payment limit.

![Screen capture showing a condition comparing a Payment Amount attribute to a Payment Limit attribute using the Greater Than Or Equal comparator.](_images/gaf1686002855074.png)

When you define a condition, on the left side, select an attribute or request type that represents unknown or variable information to be validated. On the right side, enter known or predefined criteria in the form of an attribute, request, or constant value. This keeps logical statements consistent regardless of what's being compared.

## Combining conditions

You can create complex conditional statements by grouping multiple conditions using logical operators. Conditions within a group are evaluated from top to bottom according to the selected logical operator.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | By default, condition evaluation ends as soon as a final outcome is determined. For a comprehensive audit trail of condition evaluations, you can disable this behavior when testing policies in [external policy decision point (PDP) mode](../pingauthorize_server_administration_guide/paz_config_external_pdp.html). Learn more in [Configuring condition short-circuiting in the Policy Editor](../pingauthorize_server_administration_guide/paz_pe_config_short_circuit.html). |

* **All**: All conditions in the group must evaluate to `true` for the group to evaluate to `true`. When one condition evaluates to false, evaluation ends.

* **Any**: At least one condition in the group must evaluate to `true` for the group to evaluate to `true`. When one condition evaluates to `true`, evaluation stops and the remaining conditions aren't executed.

* **None**: All conditions in the group must evaluate to `false` for the group to evaluate to `true`. When one condition evaluates to `true`, evaluation stops and the remaining conditions aren't executed.

You can drag collapsed conditions to rearrange them and change the order in which they're evaluated.

You can add conditions directly to [resolvers](paz_resolvers.html) and rules or define them on the **Components** tab of the **Library** as reusable [named conditions](paz_named_conditions.html).

## Condition comparators

You can use the following comparators in condition comparisons.

|   |                                                                                                                                   |
| - | --------------------------------------------------------------------------------------------------------------------------------- |
|   | For simplicity, the table groups logical comparator pairs together, but you can only use one comparator at a time in a condition. |

**Attribute comparators**

| Comparator                                                         | Supported data types                                                                                     | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| ------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Contains****Does Not Contain**                                   | Collection, String                                                                                       | Checks whether a string or collection contains, or doesn't contain, another string. Use this comparator when you know part of a value that you want to check.&#xA;&#xA;Matches for strings can differ from matches for collections. For example, the string 1234 contains the constant 23, but the collection \[1234] doesn't contain this constant. One possible matching collection for the constant 23 is \[21, 22, 23].                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| **Contains Claim Pair****Does Not Contain Claim Pair**             | String                                                                                                   | Add defense in depth by validating token claims as part of the authorization layer. Checks whether a JSON Web Token (JWT) *(tooltip: \<div class="paragraph">&#xA;\<p>An IETF standard container format for a JSON object used for the secure exchange of content, such as identity or entitlement information. You can find the industry standard in \<a href="https\://datatracker.ietf.org/doc/html/rfc7519">RFC 7519\</a>.\</p>&#xA;\</div>)* contains a given claim pair. Encrypted tokens aren't supported.To create a comparison:1) Select an attribute of type String that resolves to a JWT.

2) Select the **Contains Claim Pair** or **Does Not Contain Claim Pair** comparator.

3) Enter a claim pair using the syntax `<claim-name>=<claim-value>.`&#xA;&#xA;The claim value has to exactly match one of the possible values of that claim contained in the token. For example, aud=api1 will match against a token containing the claim "aud": "api1" or "aud"=\["api1", "api2"].To check a multivalued claim, create a comparator for each value you want to check. Multivalued `scope` claims in the token can be expressed as a space-delimited string, a comma-delimited string, or a JSON array of strings. To avoid unexpected behavior, use only one delimiter type. |
| **Ends With****Does Not End With**                                 | String                                                                                                   | Checks whether a string ends with, or doesn't end with, another string.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| **Equals****Does Not Equal**                                       | Boolean, Collection, Date, Date Time, Duration, JSON, Number, Period, String, Time, XML, Zoned Date Time | Checks whether two values are equal or not equal.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| **Greater Than****Less Than**                                      | Boolean, Date, Date Time, Duration, Number, String, Time, Zoned Date Time                                | Checks whether a value is greater than, or less than, another value.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| **Greater Than Or Equal****Less Than Or Equal**                    | Boolean, Date, Date Time, Duration, Number, String, Time, Zoned Date Time                                | Checks whether a value is greater than or equal to, or less than or equal to, another value.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| **Has Valid Signature For JWKS****Has Invalid Signature For JWKS** | String, JSON                                                                                             | Add defense in depth by validating tokens as part of the authorization layer. Checks the following for a JWT:- Whether the signature can be verified using one of the public keys in the JSON web key set (JWKS)

- If a token expiry was set, whether the token is expiredA valid token must have a verified signature and not be expired.&#xA;&#xA;PingAuthorize supports both RSA-encoded and EDSCA-encoded signatures. Encrypted tokens are not supported.To create a comparison:1) Select an attribute of type String that resolves to a JWT.

2) Select the **Has Valid Signature For JWKS** or **Has Invalid Signature For JWKS** comparator.

3) Select a JSON attribute that resolves to a JWKS.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| **In CIDR Block****Not In CIDR Block**                             | String                                                                                                   | Simplify adding network checks to support your zero trust policies. Verifies whether a user's IP address is in, or not in, an IP subnet range. IPv4 and IPv6 addresses are supported.To create a comparison:1) Select an attribute that resolves to a valid IP address.

2) Select the **In CIDR Block** or **Not In CIDR Block** comparator.

3) Enter the IP address range as a constant or select an attribute that resolves to the IP address range.You must express the IP address range in Classless Inter-Domain Routing (CIDR) notation (the bitmask indicates the size of the routing prefix):```
IP address/bitmask
```For example, consider a condition that checks for IP addresses between 192.0.2.0 - 192.0.2.15. CIDR notation for this range is `192.0.2.0/28`. If the IP address attribute resolves to `192.0.2.1`, for example, the condition evaluates to `true`.&#xA;&#xA;For help expressing an IP address range in CIDR notation, use a CIDR calculator.                                                                                                                                                                                                                                                                                                             |
| **Is In****Is Not In**                                             | Collection, String                                                                                       | Checks whether a string or a collection is in, or not in, another collection.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| **Regular Expression**                                             | String                                                                                                   | Checks whether a string matches a regular expression.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| **Starts With****Does Not Start With**                             | String                                                                                                   | Checks whether a value starts with, or doesn't start with, another value.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |

**Request comparators**

| Comparator                    | Description                                                                                                                                                                                                                                                                                                                                                      |
| ----------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Matches****Does Not Match** | Checks whether the inbound request name starts with, or does not start with, the conditional request name.&#xA;&#xA;For Matches to be true, the inbound request name must contain the entirety of the conditional request name. For example, if the conditional domain is BankingChannels.OnlineBanking, a request domain of BankingChannels evaluates to false. |
| **Equals****Does Not Equal**  | Checks whether the inbound request equals, or does not equal, the conditional request.                                                                                                                                                                                                                                                                           |

---

---
title: Connecting a service
description: Service connections in PingAuthorize enable you to augment authorization events with real-time data.
component: pingauthorize
version: 11.1
page_id: pingauthorize:pingauthorize_policy_administration_guide:paz_connecting_a_service
canonical_url: https://docs.pingidentity.com/pingauthorize/11.1/pingauthorize_policy_administration_guide/paz_connecting_a_service.html
llms_txt: https://docs.pingidentity.com/pingauthorize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 29, 2026
section_ids:
  steps: Steps
  choose-from: Choose from:
---

# Connecting a service

Connect PingAuthorize to external services to define data integrations.

Service connections in PingAuthorize enable you to augment authorization events with real-time data. For example, you might use signals obtained from a risk service connection in a policy that determines whether a device requires step-up authentication.

## Steps

1. In the Policy Editor, go to **Trust Framework**.

2. Click the **Services** tab, and then click the **[icon: plus, set=fa]**icon.

3. Enter a unique **Name** for the service.

   |   |                                          |
   | - | ---------------------------------------- |
   |   | Periods (.) are not allowed in the name. |

4. (Optional) Enter a **Description** of the service's purpose.

   The description is only visible on the **Services** tab, but it can help policy authors understand how to use services in policies.

5. (Optional) To nest the service under a parent in the tree, in the **Parent** list, select a parent service.

   Nesting helps group related services together. You can move the service to another location in the tree by selecting a different parent service. To remove nesting, click the **Delete** icon and leave **Parent** blank.

6. Select a **Service Type**.

   ### Choose from:

   * **None**: This is for a parent service. Nest other services under a parent to help organize services in the tree structure. There are no additional settings to complete for this type of service.

   * **Database**: Connects to relational databases and retrieves information through SQL queries. Learn more about database service settings in [Database services](paz_database_services.html).

   * **HTTP**: Connects to HTTP endpoints accessible over the public internet. Learn more about HTTP service settings in [HTTP services](paz_http_services.html).

   * **LDAP**: Connects to LDAP sources and retrieves information through database queries. Learn more about LDAP service settings in [LDAP services](paz_ldap_services.html).

7. (Optional) In the **Value Settings** section, define the **Type** of data returned by the service, and select the **Secrets** checkbox to encrypt that data in PingAuthorize logs.

   Depending on which mode you've configured for PingAuthorize, service data secrets are recorded in one of these logs:

   * [Embedded PDP mode](../pingauthorize_server_administration_guide/paz_config_embedded_pdp.html): The service data values are encrypted in `PingAuthorize/logs/policy-decision.log`.

   * [External PDP mode](../pingauthorize_server_administration_guide/paz_config_external_pdp.html): The service data values are encrypted in `PingAuthorize-PAP/logs/decision-audit.log`.

   To decrypt a service's data values, run the following command:

   ```
   'echo -n "RSNH/SPsNJSFQyyLSxdKsw==" | base64 -d | openssl enc -aes-128-ecb -d -K "54655374506153735068526153653939"
   ```

   In the previous example, `RSNH/SPsNJSFQyyLSxdKsw==` represents the encrypted service value string, and `54655374506153735068526153653939` represents the encryption key in hexadecimal. By default, the encryption key is `TeStPaSsPhRaSe99` and cannot be changed.

8. (Optional) In the **Timeout and Retry** section, configure the following properties.

   |   |                                                                                                                                                                                                                                                                                                      |
   | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | When you select **Return Full Response** for HTTP services, PingAuthorize returns non-2xx responses without applying retries. Your authorization policies must determine how to route and handle these responses. Learn more in [Return full response](paz_http_services.html#return_full_response). |

   * **Request Timeout**: The time that PingAuthorize waits, in milliseconds, for a service request to complete.

     The default timeout is `2000`. If the timeout elapses before a successful service response, PingAuthorize cancels the service request, resulting in a timeout error.

   * **Number of retries**: The number of times that PingAuthorize attempts a service request again when the initial request fails or times out. To try the service request only once, set this value to `0`.

     |   |                                                                                    |
     | - | ---------------------------------------------------------------------------------- |
     |   | If the service responds with a 4xx error, PingAuthorize won't attempt any retries. |

   * **Retry Strategy**: The approach that PingAuthorize uses when retrying service requests.

     * **Fixed Interval** (default): PingAuthorize waits for the specified retry delay between service requests.

     * **Exponential Backoff**: PingAuthorize uses the specified retry delay as a base and waits for an exponentially increasing amount of time between service requests.

   * **Retry Delay**: The time that PingAuthorize waits, in milliseconds, between service requests.

     * For fixed interval retries, PingAuthorize waits this number of milliseconds between each service request.

     * For exponential backoff retries, PingAuthorize multiplies this number by 2^n, where n is the number of retries already attempted.

       For example, if the retry delay is 1000 milliseconds, PingAuthorize makes the initial service request, then waits 1000 milliseconds before making a second request, 2000 milliseconds before making a third request, and so on.

   * **Delay Jitter**: The amount of variability, as a percentage, that PingAuthorize applies to the retry delay between each service request.

     Delay jitter reduces the chance of synchronized retries and cascading service failures.

     If this value is set to `10%` and the retry delay is set to 1000 milliseconds with exponential backoff, the delays in the previous example would be 1000±100 milliseconds, 2000±100 milliseconds, 4000±100 milliseconds, and so on.

     If this value is set to `10%` and the retry delay is set to a fixed interval of 1000 milliseconds, PingAuthorize waits 1000±100 milliseconds before making a second request, 1000±100 milliseconds before making a third request, and so on.

9. (Optional) In the **Rate Limits** section, enter a **Requests per Second** value to set the maximum number of requests that decision points can make to the service per second.

   The default value is `1000000`.

10. []()(Optional) Configure the **Circuit Breaker**.

    Circuit breakers enhance system resilience by preventing request overload. When enabled, circuit breakers monitor service calls, temporarily halt requests to services that appear unavailable, and then test those services for recovery. Circuit breakers can be open (blocking service requests), half-open (allowing test service requests), or closed (allowing service requests).

    |   |                                                                                                                            |
    | - | -------------------------------------------------------------------------------------------------------------------------- |
    |   | Circuit breaker functionality is intended only for service requests made by the PingAuthorize Server in embedded PDP mode. |

    |   |                                                                                                                                                                                                                                                                                                                    |
    | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
    |   | When you select **Return Full Response** for HTTP services, PingAuthorize returns non-2xx responses without applying circuit breaker logic. Your authorization policies must determine how to route and handle these responses. Learn more in [Return full response](paz_http_services.html#return_full_response). |

    ![Screen capture of the service's Circuit Breaker settings.](_images/paz-circuit-breaker-settings.png)

    1. Select the **Enable Circuit Breaker** checkbox.

    2. For **Failure Threshold**, enter the number of consecutive failed service calls required to open the circuit breaker.

       When the breaker is open, PingAuthorize blocks all requests to the service.

    3. For **Reset delay**, enter the number of seconds the circuit breaker should wait in an open state before transitioning to a half-open state.

       When the breaker is half-open, the system allows a limited number of requests to the service, testing if the underlying issue has been resolved before fully closing the breaker.

    4. For **Success Threshold**, enter the number of consecutive successful service calls required to close the circuit breaker.

       When the breaker is closed, the service is considered healthy and all service requests are allowed to pass through normally. If requests to the service fail before the success threshold is met, the breaker re-opens.

       The Debug Trace logger records messages indicating the current state of each circuit breaker. Learn more in [Circuit breaker logging](../pingauthorize_server_administration_guide/paz_enable_detailed_logging.html#circuit_breaker_logging).

11. (Optional) Enable caching for the service.

    Caching improves system performance by storing data returned from a service and reusing it on subsequent service requests until the cache expires. Learn more in [Service caching](paz_service_caching.html).

    1. Select the **Enable Caching** checkbox.

    2. For the **Time to Live**, enter the number of minutes that you want to store data retrieved from the service in the cache.

       ![Screen capture of the Cache Settings section of a service with the Enable Caching checkbox selected.](_images/wol1701472209245.png)

       The maximum time to live is 1440 minutes or 1 day.

    3. (Optional) Click **[icon: plus, set=fa]Header** and select headers to exclude from the cache key.

       ![Screen capture of the Cache Settings section of a service with the Enable Caching checkbox selected and an example header exclusion](_images/dsv1701472286291.png)

       Because any changes to the cache key invalidate the service cache, removing headers preserves the validity of the cache even when values of those headers change.

---

---
title: Copying elements
description: To build your authorization logic more quickly and accurately, you can make editable copies of many of your Policy Editor entities.
component: pingauthorize
version: 11.1
page_id: pingauthorize:pingauthorize_policy_administration_guide:paz_entity_copy
canonical_url: https://docs.pingidentity.com/pingauthorize/11.1/pingauthorize_policy_administration_guide/paz_entity_copy.html
llms_txt: https://docs.pingidentity.com/pingauthorize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 13, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
  result: Result:
---

# Copying elements

To build your authorization logic more quickly and accurately, you can make editable copies of many of your Policy Editor entities.

## About this task

Within the Policies and Trust Framework pages, you can copy whole definitions, policies, rules, statements, and Library entities. See the following table for page-specific capabilities and limitations.

| Policy Editorpage                      | Capabilities and limitations                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| -------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Trust Framework                        | * You can copy any definition.

* With the exception of resolvers, you can't copy a portion of a definition.

  * Copy the whole definition to duplicate any of its content, or manually copy the element between definitions.

* When you copy a definition that contains child definitions, only the parent definition is duplicated.

* You can't copy definition hierarchy trees.                                                                                                                         |
| Policies                               | - You can copy any policy, rule, or statement.

- You can't copy policy sets.

- You can't copy targets, conditions, or properties within a policy or rule.

- When you copy policies containing rules, targets, or statements belonging to the Library, these entities get reused in the new policy, not copied.

- When you copy rules or statements within a policy, you must save the policy.                                                                                                             |
| Library                                | * On the Library tab, you can copy top-level Library rules, targets, and statements.

  * You can also copy statements within rules.

  * You can't copy targets within rules.

* You can copy Library rules and statements at their point of use.

  * When you make copies of Library entities within rules or policies, the copies display at the point of use and on the Library tab.

* Where relevant, the copying capabilities and limitations listed for the Policies page apply to Library entities. |
| Trust Framework, Policies, and Library | - You can't use Make Copy in the tree structure view.

- You must save any unsaved changes to an entity before making a copy.                                                                                                                                                                                                                                                                                                                                                                                 |

## Steps

1. To create a copy of a Policy Editor entity, click Make Copy in the hamburger menu.

   ![Screen capture of using Make Copy to copy an attribute in the Trust Framework.](_images/eti1686766224950.png)

   ### Result:

   The Policy Editor creates a duplicate of the entity and its contents. The new duplicate's name is formed by adding the prefix \[Copy of] to the original name, as in the following image.

   ![Screen capture of a duplicate Trust Framework attribute created using Make Copy.](_images/vcx1686767993451.png)

2. **Optional:** Make edits to the new entity.

---

---
title: Creating a branch
description: Create a branch to start an independent line of policy development. You can create a branch at the root level, import a snapshot as a new branch, or base a subbranch on a commit in an existing branch.
component: pingauthorize
version: 11.1
page_id: pingauthorize:pingauthorize_policy_administration_guide:paz_create_branch
canonical_url: https://docs.pingidentity.com/pingauthorize/11.1/pingauthorize_policy_administration_guide/paz_create_branch.html
llms_txt: https://docs.pingidentity.com/pingauthorize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 25, 2025
page_aliases: ["paz_create_top_level_branch"]
section_ids:
  creating-a-root-branch: Creating a root branch
  steps: Steps
  importing_snapshot_as_branch: Importing a snapshot
  steps-2: Steps
  creating-a-subbranch-from-a-commit: Creating a subbranch from a commit
  steps-3: Steps
  result: Result
---

# Creating a branch

Create a branch to start an independent line of policy development. You can create a branch at the root level, import a snapshot as a new branch, or base a subbranch on a commit in an existing branch.

## Creating a root branch

Create a root branch to begin a new line of policy development from scratch.

|   |                                                                                                                                                                                                                                                                         |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | You can create up to 100 root branches in the Policy Editor, including system and self-governance branches that might not be visible to the user. The Branch Manager displays a visual counter showing how many branches have been created out of the 100-branch limit. |

### Steps

1. In the Policy Editor, go to **Branch Manager > Version Control**.

2. From the **[icon: plus, set=fa]**menu, select **Create new root branch**.

   ![Screen capture of the Create new root branch option in the Branch Manager's Version Control configuration.](_images/paz-branch-manager-create-new-root-branch.png)

3. Enter a name for the new branch.

   |   |                              |
   | - | ---------------------------- |
   |   | Branch names must be unique. |

4. Click **Save Branch**.

## Importing a snapshot

Import previously exported snapshot files as branches to share and restore Trust Framework definitions and policies across users and environments.

A snapshot file contains all the entities and policies from an existing branch. Learn more in [Creating a snapshot](paz_generate_snapshots.html).

### Steps

1. In the Policy Editor, click **Branch Manager**.

2. On the **Version Control** tab, click **[icon: plus, set=fa]**, and then select **Import Snapshot**.

   ![Screen capture of the Import Snapshot option highlighted on the Version Control tab.](_images/paz-import-branch.png)

3. Select the appropriate snapshot file.

4. Specify a unique name for the branch.

5. Click **Import**.

6. (Optional) Click **Commit New Changes** to commit the initial state of the policy branch.

## Creating a subbranch from a commit

You can create a subbranch as a child of a commit in another branch. The subbranch shares the history and contents of the parent branch up to that commit.

Learn more about branch commits in [Committing changes](paz_commit_changes.html).

### Steps

1. In the Policy Editor, click **Branch Manager**.

2. On the **Version Control** tab, select the commit from which to branch.

   To branch from the latest uncommitted changes, make sure to commit before proceeding.

3. Click the hamburger menu and select **Create new branch from commit**.

   ![Screen capture of the commit hamburger menu with the Create new branch from commit option highlighted.](_images/paz-create-subbranch.png)

4. Specify a unique name for the branch.

5. Click **Save Branch**.

### Result

The system creates a new subbranch with the selected commit as the branch point.

---

---
title: Creating a partial snapshot export
description: Create a partial export to build an export snapshot of specifically selected entities from the Trust Framework, Policy Sets, and the Library.
component: pingauthorize
version: 11.1
page_id: pingauthorize:pingauthorize_policy_administration_guide:paz_create_partial_export
canonical_url: https://docs.pingidentity.com/pingauthorize/11.1/pingauthorize_policy_administration_guide/paz_create_partial_export.html
llms_txt: https://docs.pingidentity.com/pingauthorize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 28, 2023
section_ids:
  steps: Steps
---

# Creating a partial snapshot export

Create a partial export to build an export snapshot of specifically selected entities from the Trust Framework, Policy Sets, and the Library.

## Steps

1. Click Branch Manager.

2. Click Export Partial Snapshot.

3. Select the desired items from the list on the left.

4. Click Add selection to Snapshot at the top of the pane on the left.

   This step adds the entity to the Selected entities list. The exported snapshot automatically includes all dependencies so you do not need to explicitly select each individual dependency.

5. Click Export.

---

---
title: Creating a policy to control the set of actions for a specific resource
description: For a given resource, control the outcomes (deny or permit) of actions on the resource.
component: pingauthorize
version: 11.1
page_id: pingauthorize:pingauthorize_policy_administration_guide:paz_create_policy_control_actions
canonical_url: https://docs.pingidentity.com/pingauthorize/11.1/pingauthorize_policy_administration_guide/paz_create_policy_control_actions.html
llms_txt: https://docs.pingidentity.com/pingauthorize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: December 9, 2025
section_ids:
  steps: Steps
---

# Creating a policy to control the set of actions for a specific resource

For a given resource, control the outcomes (deny or permit) of actions on the resource. In particular, the policy focuses on the Users resource and then denies deletes but permits retrieves.

## Steps

1. In the Policy Editor, go to **Policies** in the left pane and then click **Policies** along the top.

2. From the **[icon: plus, set=fa]**menu, select **Add Policy**.

3. For the name, replace **Untitled** with `Control actions for the User resource`.

4. Click the **[icon: plus, set=fa]**next to **Applies to**.

5. Click **Add definitions and targets, or drag from Components** and add the **SCIM2.Users** service.

6. Set **Combining Algorithm** to **Unless one decision is deny, the decision will be permit**.

   You should have a screen similar to the following one for the policy so far.

   ![Screen capture of the Policies tab displaying the Control actions for the User resource policy, configured as specified](_images/paz-policy-solutions-control-users-resource.png)

7. Add a rule to deny the deletion of User resources.

   1. Click **[icon: plus, set=fa]Add Rule**.

   2. For the name, replace **Untitled** with `Action: delete`.

   3. Set **Effect** to **Deny**.

   4. Click **[icon: plus, set=fa]Comparison**.

   5. In the first field, click the **A** to toggle to an **R**, and in that field's list, select **Action**.

   6. In the second field, select **Equals**.

   7. In the third field, select the **delete** action.

   8. Add a statement to provide a custom message.

      1. Within the rule, click **Show Statements**.

      2. Click **[icon: plus, set=fa]**next to **Statements**.

      3. Click **[icon: plus, set=fa]Add Statement > Denied Reason**.

      4. For the name, specify `denied-reason`.

      5. Set **Applies To** to **Deny**.

      6. In the **Payload** field:

         * Remove

           `Example:`

         * Change

           `Human-readable error message`

           to

           `System has restricted the ability to delete User resources`

   9. Click **Save changes**.

      Your rule should be similar to the following one.

      ![Screen capture of the Rule to deny deletion of User resources with a custom denied reason , configured as specified](_images/nzd1687903208250.png)

8. Add a rule to permit the retrieval of User resources.

   1. Click **[icon: plus, set=fa]Add Rule.**

   2. For the name, replace **Untitled** with `Action: retrieve`.

   3. Set **Effect** to **Permit**.

   4. Click **[icon: plus, set=fa]Comparison**.

   5. In the first field, click the **A** to toggle to an **R**, and in that field's list, select **Action**.

   6. In the second field, select **Equals**.

   7. In the third field, select the **retrieve** action.

   8. Click **Save changes**.

      Your rule should be similar to the following one.

      ![Screen capture of the rule to permit retrieval of User resources, configured as specified](_images/lad1687903375368.png)

9. Send test requests to the SCIM service, and verify data using the Policy Editor's Decision Visualiser.

---

---
title: Creating a policy to dynamically modify a resource based on the SCIM resource type
description: Given an attribute defined in multiple resource types, modify the attribute differently depending on the resource type.
component: pingauthorize
version: 11.1
page_id: pingauthorize:pingauthorize_policy_administration_guide:paz_create_policy_modify
canonical_url: https://docs.pingidentity.com/pingauthorize/11.1/pingauthorize_policy_administration_guide/paz_create_policy_modify.html
llms_txt: https://docs.pingidentity.com/pingauthorize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: December 9, 2025
section_ids:
  steps: Steps
---

# Creating a policy to dynamically modify a resource based on the SCIM resource type

Given an attribute defined in multiple resource types, modify the attribute differently depending on the resource type. In particular, this policy focuses on the retrieve action and changes the `cn` attribute to one value for the Users resource type and to another value for the Devices resource type.

## Steps

1. In the Policy Editor, go to **Policies** in the left pane and then click **Policies** along the top.

2. From the **[icon: plus, set=fa]**menu, select **Add Policy**.

3. For the name, replace **Untitled** with `Modify cn attribute based on the resource type`.

4. Click the **[icon: plus, set=fa]**icon next to **Applies to**.

5. Click **Add definitions and targets, or drag from Components** and add the **retrieve** action.

6. Set **Combining Algorithm** to **Unless one decision is deny, the decision will be permit**.

   You should have a screen similar to the following one for the policy so far.

   ![Screen capture of the Policies tab showing the Modify cn attribute based on the resource type policy, configured as specified](_images/hdl1610651918660.png)

7. Add a rule for the Users resource.

   1. Click **[icon: plus, set=fa]Add Rule.**

   2. For the name, replace **Untitled** with `If resource type is Users`.

   3. Click **[icon: plus, set=fa]Comparison**.

   4. In the **Select an Attribute** list, select the `SCIM2.resource.meta.resourceType` attribute.

   5. In the second field, select **Equals**.

   6. In the third field, specify `Users` as the constant.

   7. Add statements to modify attributes.

      1. Within the rule, click **Show Statements**.

      2. Click the **[icon: plus, set=fa]**icon next to **Statements**.

      3. Click **[icon: plus, set=fa]Add Statement > Modify Attributes**.

      4. For the name, specify `Modify cn for users resource`.

      5. Set **Applies To** to **Permit**.

      6. Set the **Payload** field to `\{"cn":"USERS_MOD"}`.

   8. Click **Save changes**.

      Your rule should be similar to the following one.

      ![Screen capture of the rule for the Users resource, configured as specified](_images/ojz1610652174879.png)

8. Add a rule for the Devices resource.

   1. Click **[icon: plus, set=fa]Add Rule.**

   2. For the name, replace **Untitled** with `If resource type is Devices`.

   3. Click **[icon: plus, set=fa]Comparison**.

   4. In the **Select an Attribute** list, select the `SCIM2.resource.meta.resourceType` attribute.

   5. In the second field, select **Equals**.

   6. In the third field, specify `Devices` as the constant.

   7. Add statements to modify attributes.

      1. Within the rule, click **Show Statements**.

      2. Click the **[icon: plus, set=fa]**icon next to **Statements**.

      3. Click **[icon: plus, set=fa]Add Statement > Modify Attributes**.

      4. For the name, specify `Modify cn for devices resource`.

      5. Set **Applies To** to **Permit**.

      6. Set the **Payload** field to `\{"cn":"DEVICES_MOD"}`.

   8. Click **Save changes**.

      Your rule should be similar to the following one.

      ![Screen capture of the rule for the Devices resource, configured as specified](_images/cpw1610652291758.png)

9. Send test requests to the SCIM service, and verify data using the Policy Editor's Decision Visualiser.