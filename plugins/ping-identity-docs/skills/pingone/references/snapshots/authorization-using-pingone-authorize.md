---
title: Adding a decision endpoint
description: Add PingOne Authorize decision endpoints to expose authorization policies for evaluation.
component: pingone
page_id: pingone:authorization_using_pingone_authorize:p1az_adding_decision_endpoints
canonical_url: https://docs.pingidentity.com/pingone/authorization_using_pingone_authorize/p1az_adding_decision_endpoints.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 15, 2026
section_ids:
  steps: Steps
  result: Result:
---

# Adding a decision endpoint

Add PingOne Authorize endpoints for stages that align with your organization's policy deployment process.

## Steps

1. In the PingOne admin console, go to **Authorization > Decision Endpoints**.

2. Click **[icon: plus, set=fa]Add Endpoint**.

3. Enter an endpoint **Name** and a **Description** that reflects the endpoint's role in the deployment process.

   The maximum name length is 256 characters.

   ![Screen capture of the Creating New Decision Endpoint window.](_images/ttq1638497876819.png)

4. If you want to deploy a particular version of a policy to the endpoint, clear the **Use latest** checkbox and select the version in the **Policy Version** list.

   If you don't deploy a particular version, the endpoint uses the latest policy version. **Use latest** republishes the latest version each time a request is made to the endpoint and can cause a slower system response.

   |   |                                                                                |
   | - | ------------------------------------------------------------------------------ |
   |   | You should only enable **Use latest** during policy development and debugging. |

5. Select the **Record recent decisions** checkbox to keep track of the last 20 [recent decisions](p1az_recent_decisions.html) made for the endpoint during the last 24 hours.

   This allows you to visualize and examine recent decisions.

   |   |                                                                                                                       |
   | - | --------------------------------------------------------------------------------------------------------------------- |
   |   | This can cause a slower system response. You should only enable this setting during policy development and debugging. |

6. Click **Save**.

   ### Result:

   The new endpoint is added to the **Decision Endpoints** page. New endpoints are listed in alphabetical order after the three default endpoints.

---

---
title: Adding a named authorization condition
description: Add named conditions to reuse conditional logic across attributes and policies.
component: pingone
page_id: pingone:authorization_using_pingone_authorize:p1_az_adding_named_conditions
canonical_url: https://docs.pingidentity.com/pingone/authorization_using_pingone_authorize/p1_az_adding_named_conditions.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: April 27, 2026
section_ids:
  steps: Steps
  choose-from: Choose from:
---

# Adding a named authorization condition

Named conditions provide a way to reuse conditional logic across attributes and policies.

Named conditions provide consistency in authorization logic and minimize repetition throughout policies. You can use named conditions as components in more complicated condition expressions.

For example, consider a named condition that compares the account status received in a decision request to a status code to determine if the account is blocked. You can use this condition in multiple policies to check a user's account status.

![Screen capture showing a condition comparing an Account Status attribute to a Block Status Code attribute using the Equals comparator.](_images/fvv1685465543159.png)

## Steps

1. In the PingOne admin console, go to **Authorization > Trust Framework**.

2. On the **Conditions** tab, click the **[icon: plus, set=fa]**icon.

3. Define general information for the named condition:

   1. Enter a unique **Name** for the condition.

      The following characters aren't allowed in the name:

      * Period (.)

      * Curly brackets ({ })

      * Pipe (|)

   2. (Optional) In the **Description** field, enter information that describes the condition's purpose.

   3. (Optional) To nest the condition under a parent in the tree, select a **Parent** condition.

      Nesting groups related conditions together. You can move the condition to another location in the tree by selecting a different parent condition. To remove nesting, click the **Delete** icon and leave the **Parent** blank.

4. To add a comparison to the condition, click **[icon: plus, set=fa]Comparison**.

   ![Screen capture showing Condition Builder fields, including the Select an Attribute list, the default Equals comparator. and the constant value input field with the Switch to attribute button.](_images/iid1685466689353.png)

5. Select an attribute to use in the comparison, select a comparator, and then enter a constant or click the **Switch to Attribute** (![fba1676849235443](_images/fba1676849235443.png)) icon to select an attribute.

   |   |                                                                                                                                                                                                                                                                                                                                       |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | When you select an attribute, you can select a property that's grayed out to [generate an attribute](p1_az_generating_attributes.html) that resolves against the parent attribute's JSON schema. If the property is nested, generate an attribute for the property above first and then generate an attribute for the child property. |

6. To nest a comparison under another comparison, click **[icon: plus, set=fa]Group**.

   Subgroups allow more permutations in comparisons. To remove nesting while keeping the comparison, click **Ungroup**.

7. To add a named condition, click **[icon: plus, set=fa]Named Condition**, select a named condition, and then select **is True** or **is False**.

8. To combine multiple conditions, named conditions, or groups, select one of the following options.

   ### Choose from:

   * **All**: Invokes the condition when all of the conditions are true. If one condition evaluates to false, the decision service ends condition evaluation. This is like adding an `AND` Boolean operator between conditions.

   * **Any**: Invokes the condition when at least one of the conditions is true. If one condition evaluates to true, the decision service ends condition evaluation. This is like adding an `OR` Boolean operator between conditions.

   * **None**: Invokes the condition when none of the conditions are true. This is like adding a `NOT` Boolean operator.

9. Click **Save Changes**.

   |   |                                                                                                                                                                                                                                                                                                        |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
   |   | You can copy a named condition defined on the **Conditions** tab for reuse by selecting **Make Copy** from the hamburger menu of that condition. If you copy a named condition with children, only the parent is duplicated. You can't copy a named condition at its point of use in a rule or policy. |

---

---
title: Adding a policy or policy set
description: Add PingOne Authorize policies and policy sets to define access rules, group rules hierarchically, and control how combining algorithms reach decisions.
component: pingone
page_id: pingone:authorization_using_pingone_authorize:p1az_adding_policy_or_policy_set
canonical_url: https://docs.pingidentity.com/pingone/authorization_using_pingone_authorize/p1az_adding_policy_or_policy_set.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 15, 2026
section_ids:
  about-this-task: About this task
  steps: Steps
  choose-from: Choose from:
---

# Adding a policy or policy set

Add PingOne Authorize policies to define the circumstances under which users can access certain resources.

## About this task

It's helpful to frame your policies in terms of what is permitted or denied.

Use policy sets to group policies and organize them hierarchically.

## Steps

1. Go to **Authorization > Policies**.

2. Click the **[icon: plus, set=fa]**icon and select one of the following:

   ### Choose from:

   * **Add Policy Set**: Add policy sets to logically group policies and other policy sets.

   * **Add Policy**: Add policies to logically group rules and other policies.

3. In the **Name** field, enter a name relevant to the business rule that you are modeling.

   |   |                                                                                            |
   | - | ------------------------------------------------------------------------------------------ |
   |   | The red dot on the right indicates that the policy or policy set contains unsaved changes. |

   ![Screen capture of the policy name showing the red dot indicating unsaved changes.](_images/guy1637366184509.png)

4. In **Applies When**, add [targets](p1az_policy_targets.html) to define when the policy is applied in decision requests.

   |   |                                                                                   |
   | - | --------------------------------------------------------------------------------- |
   |   | You cannot copy **Applies When** conditions for reuse in other policies or rules. |

5. Add rules, [conditions](p1az_conditions.html), and [statements](p1az_policy_statements.html).

   |   |                                                                                                                    |
   | - | ------------------------------------------------------------------------------------------------------------------ |
   |   | Use the hamburger menu next to the rule **Name** field to add **Applies When** conditions and statements to rules. |

6. **Optional:** Select the **Disable** check box to disable your policy or policy set.

   If you disable the policy, the decision engine skips it in evaluation and produces a `Not Applicable` decision.

   |   |                                                                                                                                                                      |
   | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | You can also disable rules. If a rule is unreachable because of the rule structure and combining algorithm, disabling that rule has no effect on the final decision. |

7. Click **Save changes**.

   |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
   | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | To copy a policy or rule for reuse, select **Make Copy** from the hamburger menu of that policy element. You cannot make copies of policy sets.If you copy policies containing **Library** rules or statements, those **Library** elements are reused in the new policy, not copied. For example, if you copy a policy that contains a custom rule, which in turn contains a **Library** statement, the rule is copied but the statement is reused. |

---

---
title: Adding a worker application for the PingOne Authorize service
description: Add a worker application in PingOne to enable PingOne Authorize dynamic authorization API actions and configure the required roles and token authentication.
component: pingone
page_id: pingone:authorization_using_pingone_authorize:p1az_adding_worker_app
canonical_url: https://docs.pingidentity.com/pingone/authorization_using_pingone_authorize/p1az_adding_worker_app.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 15, 2026
section_ids:
  steps: Steps
  result: Result:
  next-steps: Next steps
---

# Adding a worker application for the PingOne Authorize service

After PingOne Authorize is in your PingOne environment, add a worker application to enable dynamic authorization API actions for the service.

PingOne integrates with client applications through application connections that define access to PingOne resources. A worker application is a userless service application connection that can perform administrator functions. Access is encoded in the worker application's access token, which you submit with API requests. Learn more about how PingOne manages access to applications in [Applications](../applications/p1_application_types.html).

|   |                                                                                                                                                                                                                                                                                           |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | You must assign the Environment Admin and Identity Data Admin roles, or a custom role with equivalent permissions, to the worker application after you create it. Learn more in [Configuring roles for a worker application](../applications/p1_configurerolesforworkerapplication.html). |

## Steps

1. In the PingOne admin console, go to **Applications > Applications**.

2. Click the **[icon: plus, set=fa]**icon next to **Applications**.

3. For **Application Name** and **Description**, enter a unique identifier for the application and a brief characterization of the application.

   ![Screen capture showing the name and description of the worker app on the Create App Profile page.](_images/asu1638650528863.png)

4. For the **Application Type**, click **Worker**.

5. Click **Save**.

   ### Result:

   The **Applications** page displays your worker application.

6. On the **Roles** tab, click **Grant Roles**.

7. In **Available responsibilities**, select the following roles:

   * **Identity Data Admin** role for your environment

   * **Environment Admin** role for your organization, or for a specific environment

     The **Granted responsibilities** tab provides a simplified view of your selected roles.

     ![Screen capture showing the name and description of the worker app on the Create App Profile page.](_images/p1az-worker-app-roles.png)

8. Click **Save**.

9. []()(Optional) Configure the **Token Endpoint Authentication Method**.

   [HTTP services](p1_az_connecting_an_http_service.html) that access PingOne APIs with the client credentials grant type expect credentials in the body of a token request (`client_secret_post`) instead of in the `Authorization` header (`client_secret_basic`).

   1. On the **Configuration** tab, click the **[icon: pencil, set=fa]**icon.

   2. In the **Token Endpoint Authentication Method** list, select **Client Secret Post**.

   3. Click **Save**.

10. To enable the application, click the **Enable** toggle.

    ![Screen capture showing the enable toggle for the worker app.](_images/xiz1638651053664.png)

## Next steps

Complete these tutorials to familiarize yourself with PingOne Authorize capabilities:

* [Manage API access](p1az_aam_tutorial_manage_api_access.html)

* [Build dynamic authorization policies](p1az_dynamic_authorization_tutorials.html)

---

---
title: Adding an application role
description: Add application roles in PingOne Authorize to group permissions by function and assign them to users.
component: pingone
page_id: pingone:authorization_using_pingone_authorize:p1_az_adding_application_roles
canonical_url: https://docs.pingidentity.com/pingone/authorization_using_pingone_authorize/p1_az_adding_application_roles.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 15, 2026
section_ids:
  before-you-begin: Before you begin
  about-this-task: About this task
  steps: Steps
  example: Example:
  result: Result:
  next-steps: Next steps
---

# Adding an application role

Add application roles to group application permissions by function, then control access to application resources by assigning roles to users.

## Before you begin

* [Add the application permissions](../applications/p1_add_application_permissions.html) that you want to grant to your roles.

* [Add the users](../directory/p1_adduser.html) that you want to assign to roles.

## About this task

Roles determine which permissions a user has. A user can perform an action on an application resource if they have a role with the associated permission.

|   |                                                                      |
| - | -------------------------------------------------------------------- |
|   | You can add up to 128 application roles in each PingOne environment. |

## Steps

1. Go to **Authorization > Application Roles**.

2. Click the **[icon: plus, set=fa]**icon next to **Application Roles**.

3. Enter a unique **Application Role Name** and an optional **Description**. Click **Next**.

   |   |                                                                                                                                                                     |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | The name can include Unicode letters, marks, numbers, spaces, forward slashes, dots, apostrophes, underscores, and hyphens, with a maximum length of 20 characters. |

   ### Example:

   For example, you could add an `Invoicing Processor` role for the BizPro invoicing application to give Invoicing Processors permissions to read, write, pay, and update invoices.

   ![Screen capture showing the Application Role Name and Description fields in the Add Application Role window.](_images/yis1705003594939.png)

4. Select the permissions that you want to assign to the role.

   Permission names list the application resource and action separated by a colon. For reference, the PingOne resource associated with the application resource is displayed next to the checkbox.

   ![Screen capture showing selected permission checkboxes in the Assign Permissions window.](_images/zlm1705003754568.png)

5. Click **Next**.

6. Select the users that you want to assign to the role.

   ### Result:

   Selected users will have the permissions that are assigned to the role.

   ![Screen capture showing selected user checkboxes in the Add User window.](_images/hiw1705003945283.png)

7. Click **Save**.

## Next steps

Add additional roles and assign users to grant them the permissions assigned to the roles.

For example, in the BizPro invoicing application, Billing Supervisors might need permissions to read and void invoices. Add a `Billing Supervisor` role and assign the `Invoices:Read` and `Invoices:Void` permissions to it.

---

---
title: Adding an attribute
description: Learn how to use the Trust Framework to add an attribute that you can use in a dynamic authorization policy.
component: pingone
page_id: pingone:authorization_using_pingone_authorize:p1az_tutorial_adding_an_attribute
canonical_url: https://docs.pingidentity.com/pingone/authorization_using_pingone_authorize/p1az_tutorial_adding_an_attribute.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 6, 2026
section_ids:
  steps: Steps
  result: Result:
  next-steps: Next steps
---

# Adding an attribute

Learn how to use the **Trust Framework** to add an attribute that you can use in a dynamic authorization policy.

You need to know the payment amount to determine if it's greater or less than $10,000 USD, so let's add an attribute for the amount to the [Trust Framework](p1az_trust_framework.html).

The **Trust Framework** provides an enterprise-wide view of your data and service ecosystem. It's where your organization's technical personnel capture definitions for digital assets, services, and users across all domains in your organization, including:

* Attributes used in policies

* Connections to APIs

* Information points used as data sources for attributes

When you use business-friendly names to define resources in the **Trust Framework**, policy authors can easily refer to these resources without worrying about how the information is retrieved and populated.

## Steps

1. In the PingOne admin console, go to **Authorization > Trust Framework**.

2. If it isn't already displayed, click the **Attributes** tab.

   You can see the [built-in user attributes](p1_az_built_in_attributes.html) that come with PingOne Authorize. You're going to add a new attribute for the amount.

   ![Screen capture of the Attributes tab in the PingOne Authorize Trust Framework showing the ID attribute nested under PingOne and User.](_images/p1az-tutorial-built-in-attrs.png)

3. Click the **[icon: plus, set=fa]**icon.

4. For the attribute **Name**, enter `Amount`.

   |   |                                                                                                                                                                                                                                             |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | If you selected another attribute before you added `Amount`, `Amount` is nested under the parent attribute. Nesting helps group related attributes together. To keep things simple, you won't nest the `Amount` attribute in this tutorial. |

5. Verify that there is no **Parent** selected. If a parent exists, click the **Delete** icon to remove it.

   To get the payment amount, which is the value of the attribute, you'll add a resolver. [Resolvers](p1_az_resolvers.html) define where the initial data for an attribute comes from.

6. Click **[icon: plus, set=fa]Add Resolver**.

   Keep the default Resolver type of **Request Parameter** so that the value of your attribute comes from a parameter in the decision request. Later in the tutorial, you'll use a field in the decision request body to provide a value for the request parameter. So far your attribute looks like this.

   ![Screen capture of the Details tab for the Amount attribute showing a Request Parameter resolver.](_images/cna1637363639867.png)

   Next let's make sure that the value of the attribute is a number.

7. In **Value Settings**, for the **Type**, select **Number**.

   ![Screen capture of Value Settings for the Amount attribute showing that the Type is Number.](_images/eqm1637364049051.png)

8. Click **Save Changes**.

   ### Result:

   Your new attribute is displayed in the attribute list.

   ![Screen capture of the Amount attribute on the Attributes tab.](_images/p1-az-tutorial-attr-result-list.png)

## Next steps

You used the **Trust Framework** to create a simple attribute that represents the payment amount. Now that you've added an attribute, you're ready to [use the attribute in a policy](p1az_tutorial_adding_and_testing_policies.html#tutorial-add-policy).

---

---
title: Adding an authorization attribute
description: Add attributes to provide data used in authorization policies and decision evaluations.
component: pingone
page_id: pingone:authorization_using_pingone_authorize:p1_az_adding_attributes
canonical_url: https://docs.pingidentity.com/pingone/authorization_using_pingone_authorize/p1_az_adding_attributes.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: April 27, 2026
section_ids:
  before-you-begin: Before you begin
  steps: Steps
  next-steps: Next steps
---

# Adding an authorization attribute

Add attributes to map your organization's data to a form that authorization policies can evaluate. Attributes serve as the data inputs that PingOne Authorize resolves and uses when making policy decisions.

## Before you begin

Before adding attributes:

* Plan how you want to organize them in the **Attributes** tree. You can nest attributes under parent attributes to group related attributes together.

* Establish naming conventions for your attributes to make them easier to identify and understand. For example, you might prefix attributes that resolve from the same data source with the same string.

## Steps

1. Add a new attribute:

   1. In the PingOne admin console, go to **Authorization > Trust Framework**.

   2. On the **Attributes** tab, click the **[icon: plus, set=fa]**icon.

2. Define general information for the attribute:

   1. Enter a unique **Name** for the attribute.

      To ensure that PingOne Authorize can [resolve attribute references](p1_az_interpolating_attributes.html), the following characters aren't allowed in the name:

      * Period (.)

      * Curly brackets ({ })

      * Pipe (|)

   2. (Optional) In the **Description** field, enter information that describes the attribute's purpose.

      The description is only visible on the **Attributes** tab, but it can help policy authors understand how to use the attribute in policies.

   3. (Optional) To nest the attribute under a parent in the tree, select a **Parent** attribute.

      Nesting groups related attributes together. You can move an attribute to another location in the tree by selecting a different parent attribute. To remove nesting, click the **Delete** icon and leave the **Parent** blank.

3. (Optional) To define where the attribute pulls information from, [add resolvers](p1_az_adding_resolvers_to_attributes.html).

4. (Optional) [Add value processors](p1_az_adding_processors_to_attributes.html) that transform the attribute's value.

5. (Optional) [Add value settings](p1_az_adding_value_settings_to_attributes.html) that define the attribute's data type and default value.

6. Click **Save changes**.

   |   |                                                                                                                                                                                                                                                                                                                                                                                                              |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
   |   | You can copy an attribute for reuse by selecting **Make Copy** from the hamburger menu of that attribute. You can't copy a portion of an attribute definition, with the exception of resolvers. You must copy the whole attribute definition to duplicate any of its content or manually copy the content between definitions.If you copy an attribute with child attributes, only the parent is duplicated. |

## Next steps

After saving the attribute, you can [add repetition settings](p1_az_adding_repetition_settings_to_attributes.html) to resolve the attribute's values from a collection.

---

---
title: Adding an external OAuth server in PingOne Authorize
description: Add an external OAuth server to enable PingOne Authorize to validate access tokens issued by external token sources.
component: pingone
page_id: pingone:authorization_using_pingone_authorize:p1_az_adding_external_oauth_servers
canonical_url: https://docs.pingidentity.com/pingone/authorization_using_pingone_authorize/p1_az_adding_external_oauth_servers.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 5, 2025
keywords: ["external OAuth client;external token issuer"]
section_ids:
  before-you-begin: Before you begin
  steps: Steps
  choose-from: Choose from:
  next-steps: Next steps
---

# Adding an external OAuth server in PingOne Authorize

Add an external OAuth server to enable PingOne Authorize to validate access tokens issued by external token sources.

You can add up to 25 external OAuth servers in each environment and assign the same external OAuth server to multiple API services.

## Before you begin

* Ensure that the external OAuth server issues access tokens that meet API Access Management requirements. Learn more in [External OAuth servers](p1_az_external_oauth_servers.html).

* In the system that issues tokens, create an OAuth 2.0 client application.

  You'll need the following information from the token issuer:

  * Token issuer identifier

  * JWKS endpoint URI or JWKS document

  * Token audience

## Steps

1. In the PingOne admin console, go to **Authorization > External OAuth Servers**.

2. Click the **[icon: plus, set=fa]**icon next to **External OAuth Servers** to add an external OAuth server.

3. Enter a **Name** that identifies the external OAuth server.

   Each external OAuth server in the environment must have a unique name of up to 256 characters.

4. (Optional) Enter a **Description** of the external OAuth server's purpose.

5. In **Issuers**, enter the token issuer identifier.

   ![Screen capture showing the OAuth server Name, Description, Issuers, JWKS URL, and Clock Skew Tolerance fields in the Add External OAuth Server panel.](_images/p1-az-aam-ext-oauth-add.png)Example

   In PingOne Advanced Identity Cloud, you can use the `/oauth2/realms/root/.well-known/openid-configuration` endpoint to identify the issuer. For example, a PingAM issuer identifier might be `https://example.com:8443/am/oauth2/realms/root/realms/alpha`. Learn more in [Access the keys exposed by the JWK URI endpoint](https://docs.pingidentity.com/pingoneaic/latest/am-oidc1/managing-jwk_uri.html#obtaining-public-signing-key) in the PingAM documentation.

6. (Optional) To add additional issuers, click **+ Add Issuer**.

7. In the **JSON Web Key Set Method** section, select the method PingOne Authorize uses to retrieve public keys for JWT signature verification.

   ### Choose from:

   * **JWKS URL**: Enter the JSON Web Key Set Uniform Resource Identifier address in the **JWKS URL** field.

     Example

     In PingOne Advanced Identity Cloud, you can use the well-known endpoint mentioned in step 5 to identify the JWKS URL. For example, a PingAM JWKS URL might be `https://example.com:8443/am/oauth2/realms/root/realms/alpha/connect/jwk_uri`.

   * **JWKS**: Paste the contents of a JWKS document in the **JWKS** field. The JWKS document contains the public keys the OAuth server uses to sign its JWTs.

8. Enter a **Clock Skew Tolerance** value, or use the arrows to increase or decrease the value.

   Clock skew accounts for small time differences between PingOne and the external OAuth server's system clocks. When validating time-based token claims, such as `nbf` (not before) and `exp` (expires), PingOne Authorize allows a time difference up to the tolerance value.

   |   |                                                                                                                                                                                                                          |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
   |   | If PingOne Authorize frequently rejects valid tokens, consider increasing the clock skew tolerance. However, a higher tolerance can compromise security by allowing tokens that are already expired or aren't valid yet. |

9. Click **Save**.

## Next steps

Associate the external OAuth server with an API service. Learn more in [Defining your API in PingOne Authorize](p1az_add_api_service.html).

|   |                                                                                                                        |
| - | ---------------------------------------------------------------------------------------------------------------------- |
|   | Whenever you update external OAuth server settings, you must deploy each API service associated with the OAuth server. |

---

---
title: Adding and testing a policy
description: Add and test a dynamic authorization policy that uses an attribute in PingOne Authorize.
component: pingone
page_id: pingone:authorization_using_pingone_authorize:p1az_tutorial_adding_and_testing_policies
canonical_url: https://docs.pingidentity.com/pingone/authorization_using_pingone_authorize/p1az_tutorial_adding_and_testing_policies.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 15, 2026
section_ids:
  tutorial-add-policy: Adding a policy
  steps: Steps
  result: Result:
  result-2: Result:
  tutorial-test-policy: Testing the policy
  about-this-task: About this task
  steps-2: Steps
  result-3: Result:
  result-4: Result:
  next-steps: Next steps
---

# Adding and testing a policy

Learn how to add and test a dynamic authorization policy that uses an attribute.

## Adding a policy

Policies model business requirements into authorization logic. They're built by business analysts who understand your application requirements and the regulations you're complying with.

Let's add a policy that will deny payments over 10,000 USD.

### Steps

1. Go to **Authorization > Policies**.

   On the **Policies** tab, you'll see the default policy set called **Policies**. Policy sets are like folders that you can use to group and organize policies. You're going to add your policy to the default policy set.

   ![Screen capture of the Policies policy set on the Policies tab.](_images/tdv1637365837651.png)

2. Select the root policy set **Policies**, then click the **[icon: plus, set=fa]**icon and select **Add Policy**.

3. For the policy **Name**, enter `Payment checks`.

   The red dot on the right indicates that there are unsaved changes in the policy.

   ![Screen capture of the policy name showing the red dot indicating unsaved changes.](_images/guy1637366184509.png)

   Now you need a rule that defines the policy logic.

4. Click **[icon: plus, set=fa]Add Rule**.

   To keep things simple, leave out the description for now. When you develop your own policies, you can enter a description to document the underlying business case for the rule or the specific business policy the rule is enforcing.

5. For the rule **Name**, enter `Deny payments over 10000 USD`.

6. Because you want to deny certain payments, select **Deny** for the **Effect**.

   Let's make a comparison to determine if the payment amount is over $10,000 USD.

7. Click the hamburger menu next to the **Name** field and select **Add "Applies When"**.

   1. In the **Applies When** section, click **[icon: plus, set=fa]Comparison**.

   2. In **Select an attribute**, select **Amount**, which is the attribute that you added to the **Trust Framework**.

   3. For the comparator, select **Greater Than Or Equal**.

   4. For the constant value, enter `10000`.

      #### Result:

      Your rule looks like this:

      ![Screen capture of the Deny payments over 10000 USD rule showing the comparison to determine if the payment amount is over 10000.](_images/p1az-tutorial-deny-payment-rule.png)

8. Click **Save changes**.

   #### Result:

   Your new policy is displayed in the default policy set.

   ![Screen capture of the Payment checks policy nested under the default Policies policy set.](_images/hst1637367410176.png)

## Testing the policy

### About this task

Next you'll test your policy to make sure it does what you expect.

### Steps

1. Go to **Authorization > Policies**, then select the **Payment checks** policy and click the **Test** tab.

2. In the **Request** section, in the **Attributes** list, select the **Amount** attribute and enter `10900` as the attribute value.

   ![Screen capture of the Testing Scenario tab showing a request with the Amount attribute set to a value of 10900.](_images/ved1637446522210.png)

3. Click **Execute**.

   #### Result:

   The **Visualization** tab shows a deny result, as you'd expect, because the amount is over 10000. The policy is working.

   ![Screen capture showing the visualization flow of the deny result.](_images/nri1637446893971.png)

   Now let's test a value less than 10,000 to see if the policy handles it.

4. Click the **Testing Scenario** tab, enter `9900` as the attribute value, and click **Execute**.

   ![Screen capture of the Testing Scenario tab showing a request with the Amount attribute set to a value of 9900.](_images/ble1637447542764.png)

   #### Result:

   A second **Test Results** tab is displayed that shows a result that's not applicable. Your rule only applies to amounts greater than or equal to 10000, so right now the rule doesn't apply to amounts less than 10000. This neutral decision indicates that the policy doesn't apply in this situation.

   ![Screen capture showing the visualization flow of the not applicable result.](_images/hvh1637447968820.png)

   You have more work to do with your policy to account for amounts less than $10,000 USD.

### Next steps

You used the amount attribute to build a basic policy with a rule that denies payments over $10,000 USD. Then you tested your policy and found that it doesn't account for payments less than $10,000 USD.

Let's [update and retest the policy](p1az_tutorial_updating_and_retesting_policies.html).

---

---
title: Adding custom policies for API services and operations
description: With an API gateway integration, you can define custom policies that target inbound requests and outbound responses for API services and operations.
component: pingone
page_id: pingone:authorization_using_pingone_authorize:p1az_adding_custom_policies_for_api_services_and_operations
canonical_url: https://docs.pingidentity.com/pingone/authorization_using_pingone_authorize/p1az_adding_custom_policies_for_api_services_and_operations.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: December 2, 2025
section_ids:
  before-you-begin: Before you begin
  about-this-task: About this task
  steps: Steps
  choose-from: Choose from:
---

# Adding custom policies for API services and operations

With an API gateway integration, you can define custom policies that target inbound requests and outbound responses for API services and operations.

## Before you begin

If custom policies are not enabled for your API service, enable them by clicking **Enable Custom Policies** on the API service's **Overview** tab.

## About this task

Custom policies control access to APIs in complex authorization scenarios. When you enable custom policies for an API service, PingOne Authorize generates a policy tree for the API service. The tree structure is system-owned and reflects the API service and its operations. You can't modify the policy sets and policies in the tree, but you can add your own custom policies to **Custom** policy sets in the tree.

The tree structure is organized as follows.

![Screen capture showing the API Service policy set for the Meme Game.](_images/fqa1690825789014.png)

Top-level policy sets include:

* **API Service *\<Name>***: This is the top level policy set for the API service. It serves as a container for everything nested underneath it.

* **API Service and Operations**: This policy set ensures that combining algorithms work correctly for AAM rules and policies.

The next level contains the request and response policies and policy sets for each API service.

![Screen capture showing the Inbound Request policy set for the Meme Game API Service.](_images/gky1690825877262.png)

These include:

* **Inbound Request**: This policy set is a container for rules and custom policies that target inbound requests for the API service.

  * **Basic Rules**: This policy is reserved for rules generated by the system that target inbound requests for the API service. The rules are based on the API Service configuration.

  * **Custom**: This policy set is where you add your own custom policies that target inbound requests for the API service.

* **Outbound Response**: This policy set is a container for rules and custom policies that target outbound responses from the API service. Its children have the same structure as the **Inbound Request** policy set.

Each operation under the API service shares a similar structure.

![Screen capture showing the Get Memes of Another User Operation policy set for the Meme Game API Service.](_images/qyu1690825978459.png)

Operation policies and policy sets include:

* **Operation *\<Name>***: This is the top level policy set for the operation. It serves as a container for everything nested underneath it.

* **Inbound Request**: This policy set is a container for rules and custom policies that target inbound requests for the specific operation.

  * **Basic Rules**: This policy stores group and scope-based rules that target inbound requests for the operation. The policy is generated automatically by the system when you add basic rules to an operation.

  * **Custom**: This policy set is where you add your own custom policies that target inbound requests for the operation.

* **Outbound Response**: This policy set is a container for rules and custom policies that target outbound responses from the specific operation. It has nested children for **Basic Rules** and **Custom** policies.

## Steps

1. Go to **Authorization > Policies**, and expand the **API Access Management** policy tree, then expand the policy tree for your API service.

   For example, consider an API service that protects health records and an API operation to get the records. You want to write a policy that allows a user to view only their own health records.

   ![Screen capture showing the policy tree with the Health Records API Service policy set expanded to show child policy sets.](_images/cbm1697230764873.png)

2. In the policy tree, select the **Custom** policy set nested under the request or response that you want the policy to target:

   ### Choose from:

   * API service **Inbound Request**: This is for policies that will be executed by any API call to any endpoint in the API service. For example, policies that control access based on user characteristics, such as account status or risk score, or whether certain scopes or claims are present in the access token, or whether requests are from certain IP address ranges.

   * API service **Outbound Response**: This is for policies that will modify responses to any API call in the API service. For example, a policy that rewrites the value of an attribute that appears in all responses, such as a URL that uses a private host name.

   * Operation **Inbound Request**: This is for policies that are restricted to specific endpoints. For example, a policy that requires an extra claim in the access token for a POST or PUT request, but not for a GET request, or a policy that constrains a search query to resources owned by the requester, such as allowing a user to view only their own health records.

   * Operation **Outbound Response**: This is for policies that modify responses to API calls to specific endpoints. For example, a policy that filters the attributes of JSON responses to remove sensitive fields that the API can return, such as information that a user hasn't consented to sharing with a requester.

   For the health records example, you would select the **Custom** policy set for inbound requests to the operation.

   ![Screen capture showing the Custom policy set for inbound requests to the GET Records operation nested under the Health Records API Service policy set.](_images/wqz1697231037161.png)

3. Click the **[icon: plus, set=fa]**icon and select **Add Policy**.

4. In the **Name** field, enter a name relevant to the business rule that you are modeling.

   ![Screen capture showing the User identity check policy Name and Description fields.](_images/lsf1697231232345.png)

5. Add rules, [conditions](p1az_conditions.html), and [statements](p1az_policy_statements.html) to the policy as needed.

   For the health records example, consider the following API operation to get a user's health records:

   ![Screen capture showing the Method and Path for the Get user's health records operation.](_images/jcx1697231734994.png)

   This rule allows access to health records only when the access token's subject claim matches the user ID in the request path. The attribute on the right hand side of the comparison represents the user ID path parameter in the API operation `/records/user/{userId}`. You can find more information about this attribute in [API Access Management attributes](p1_az_built_in_attributes.html#p1-aam-attr). Learn more about accessing information about the requesting user from PingOne Directory or an external directory in [API services](p1az_api_services.html).

   ![Screen capture showing the Permit access to user's own records rule with an Applies When condition that compares the access token subject to the user ID path parameter in the decision request.](_images/hla1697232040674.png)

   For more details about the components used in policies, see [Authorization policies](p1az_policies.html).

6. Click **Save changes**.

7. To deploy the policy, go to **Authorization > API Services**, and select the corresponding API service.

   ![Screen capture showing the Deploy button on the Overview tab of the Health Records API service.](_images/xhz1697232249129.png)

8. Click **Deploy**.

---

---
title: Adding repetition settings to an authorization attribute
description: Add repetition settings to an attribute to resolve attribute values from a collection.
component: pingone
page_id: pingone:authorization_using_pingone_authorize:p1_az_adding_repetition_settings_to_attributes
canonical_url: https://docs.pingidentity.com/pingone/authorization_using_pingone_authorize/p1_az_adding_repetition_settings_to_attributes.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: January 15, 2026
section_ids:
  before-you-begin: Before you begin
  steps: Steps
---

# Adding repetition settings to an authorization attribute

Add repetition settings to an attribute to resolve its values from a collection.

A repeating attribute requires a repetition source that points to a collection. To get values from each repetition of the collection, the repeating attribute must have a resolver set to **Current Repetition Value**.

|   |                                                                                                                                                                                                                                                                                  |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | You can also use repeating attributes in named conditions and named processors. If an attribute uses a named condition or value processor, any repeating attributes referenced in the condition or value processor must have the same repetition source as the attribute itself. |

## Before you begin

[Add an attribute](p1_az_adding_attributes.html) that serves as the repetition source.

|   |                                                                                        |
| - | -------------------------------------------------------------------------------------- |
|   | The value setting **Type** for the repetition source attribute must be **Collection**. |

For example, consider the following attribute that retrieves a collection of payment transactions from a service response. This attribute will serve as the repetition source for a repeating attribute that retrieves the transaction amount.

![Screen capture showing a Collection attribute that resolves a collection of transactions from a service response.](_images/tek1677452001612.png)

## Steps

1. Go to **Authorization > Trust Framework** and click the **Attributes** tab.

2. Select the attribute to which you want to add repetition settings.

3. Click the hamburger menu in the **Name** field and select **Add repetition settings**.

4. In the **Repeat for each item of** list in the **Repetition Settings** section, select a repetition source attribute.

   ![Screen capture showing the Repeat for each item of field in the Repetition Settings section of an attribute.](_images/mve1677452499260.png)

5. Expand **Resolvers** and click **[icon: plus, set=fa]Add Resolver**.

6. In the **Resolver type** list, select **Current Repetition Value**.

   This resolves the attribute against individual items in the collection.

   ![Screen capture showing the Resolver type set to Current Repetition Value and a Value Processor with a JSON Path processor expression that gets the transaction amount.](_images/p1az-repetition-settings-resolver.png)

7. Click **Save changes**.

---

---
title: Adding resolvers to an attribute
description: Add resolvers to a PingOne Authorize attribute to define its data source.
component: pingone
page_id: pingone:authorization_using_pingone_authorize:p1_az_adding_resolvers_to_attributes
canonical_url: https://docs.pingidentity.com/pingone/authorization_using_pingone_authorize/p1_az_adding_resolvers_to_attributes.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 15, 2026
section_ids:
  before-you-begin: Before you begin
  steps: Steps
---

# Adding resolvers to an attribute

Optionally, add resolvers to define where an attribute pulls information from.

## Before you begin

[Add an attribute](p1_az_adding_attributes.html) and configure the attribute's general settings.

## Steps

1. Add a resolver to the attribute:

   1. In the **Resolvers** section, do one of the following:

      * Click **[icon: plus, set=fa]Add Resolver**.

      * Click **[icon: plus, set=fa]Add Parent Resolver**.

        |   |                                                                                                                                                                                                                                  |
        | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
        |   | This is an optional shortcut that resolves the attribute against its parent. You can add a parent resolver if the attribute has a parent and doesn't already have a parent resolver. If you add a parent resolver, skip step 1c. |

        ![Screen capture showing the Resolver Name and Resolver Type fields, and the +Add Resolver and +Add Parent Resolver buttons.](_images/din1677105054409.png)

   2. **Optional:** Update the **Resolver Name**.

      By default, the name is a combination of the resolver type and associated information, such as the attribute name for an **Attribute** resolver.

   3. Select a **Resolver type**.

      For more information about resolver types, see [Resolvers](p1_az_resolvers.html).

2. **Optional:** To invoke a resolver only under certain conditions, add [conditions](p1az_conditions.html) to the resolver:

   1. Click the hamburger menu next to the **Resolver Name** and select **Add Condition**.

      |   |                                          |
      | - | ---------------------------------------- |
      |   | You can remove a condition the same way. |

   2. To add a comparison to the condition, click **[icon: plus, set=fa]Comparison**.

      ![Screen capture showing the Select an Attribute list, the comparator list, and the constant or attribute field in a resolver condition.](_images/ibj1677105692510.png)

   3. Select an attribute to use in the comparison, select a comparator, and then enter a constant or click the **Switch to Attribute** (![fba1676849235443](_images/fba1676849235443.png)) icon to select an attribute.

      When you select an attribute, you can select a property that's grayed out to [generate an attribute](p1_az_generating_attributes.html) that resolves against the parent attribute's JSON schema. If the property is nested, generate an attribute for the property above first, and then generate an attribute for the child property.

   4. To nest a comparison under another comparison, click **[icon: plus, set=fa]Group**.

      Subgroups allow more permutations in comparisons. To remove nesting while keeping the comparison, click **Ungroup**.

   5. To select a [named condition](p1_az_adding_named_conditions.html), click **[icon: plus, set=fa]Named Condition**, select a condition, and then select **is True** or **is False**.

   6. To combine multiple conditions, named conditions, or groups, select one of the following options:

      * **All**: Invokes the resolver when all of the conditions are true. If one condition evaluates to false, evaluation stops and the remaining conditions are not executed. This is like adding an `AND` Boolean operator between conditions.

      * **Any**: Invokes the resolver when at least one of the conditions is true. If one condition evaluates to true, evaluation stops and the remaining conditions are not executed. This is like adding an `OR` Boolean operator between conditions.

      * **None**: Invokes the resolver when none of the conditions are true. This is like adding a `NOT` Boolean operator.

3. Add processors to transform the value returned by the resolver.

   For details, see [Adding value processors to an attribute](p1_az_adding_processors_to_attributes.html).

   |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
   | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | Icons next to the **Resolver Name** field indicate at a glance whether a resolver has conditions, processors, or both.![Screen capture showing the condition and processor icons next to the Resolver Name field.](_images/eow1677106950158.png)You can copy resolvers defined in an attribute by selecting **Make Copy** from the hamburger menu of that resolver. Copying a resolver also copies any processors or conditions defined in that resolver. |

---

---
title: Adding statements to policies and rules
description: Include statements in rules and policies to perform additional processing as part of an authorization decision.
component: pingone
page_id: pingone:authorization_using_pingone_authorize:p1az_adding_statements_to_policies_and_rules
canonical_url: https://docs.pingidentity.com/pingone/authorization_using_pingone_authorize/p1az_adding_statements_to_policies_and_rules.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 11, 2025
section_ids:
  steps: Steps
  choose-from: Choose from:
  choose-from-2: Choose from:
  next-steps: Next steps
---

# Adding statements to policies and rules

Include statements in rules and policies to perform additional processing as part of an authorization decision.

You can add [statements](p1az_policy_statements.html) to the policy as a whole and to individual rules, or you can pull in statement templates from the **Library**.

|   |                                                                                                                                                                          |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | Some [built-in statements](p1az_statement_templates.html) require an API gateway integration and a policy or rule that targets an [API service](p1az_api_services.html). |

You can drag collapsed statements to rearrange them and change the order in which they're evaluated.

## Steps

1. In the PingOne admin console, go to **Authorization > Policies**, and click a policy or [add a new policy](p1az_adding_policy_or_policy_set.html).

2. Do one of the following to add a statement.

   ### Choose from:

   * In the **Statement** section, click **+Add Statement**.

   * From the **Library** on the **Components** tab, drag a statement template into the **Statement** section. Statements pulled in from the **Library** are read-only. To make changes to the statement, click the hamburger menu next to the **Obligatory** checkbox and select **Replace with clone**.

     |   |                                                                                                                                                                                                                                                                                                                                                                                                                                         |
     | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
     |   | * Changes you make to a clone don't affect the template in the **Library**.

     * You can add statements to individual rules the same way that you add them to policies. To add a statement to a rule, click the hamburger menu next to the rule **Name** field and select **Add Statement**. Then click **[icon: plus, set=fa]Add Statement** or drag a statement template from the **Library** to the **Statement** section in the rule. |

3. Enter a **Name** and an optional **Description** for the statement.

4. (Optional) Select the **Obligatory** checkbox to make the statement a required condition for authorization.

   PingOne Authorize handles obligations differently in dynamic authorization and API Access Management:

   * Dynamic authorization: PingOne Authorize doesn't enforce obligations in policies published to decision endpoints. The decision service includes the obligation in the decision response and it's the client's responsibility to enforce the obligation.

   * API Access Management: PingOne Authorize attempts to enforce obligations in policies published to API services. If the decision service can't fulfill an obligation, the decision evaluation fails and returns an error to the client.

     |   |                                                                                                                             |
     | - | --------------------------------------------------------------------------------------------------------------------------- |
     |   | If a non-obligatory statement can't be fulfilled, the decision service logs an error and continues the decision evaluation. |

5. Enter a statement **Code** to identify the type of statement.

   If you pulled in a statement template, use the default code populated from the template. Otherwise, enter your own code. For example, you can enter a code such as `MFA_REQ` or `APPROVE` to return a statement code to a DaVinci flow.

   Learn more about built-in statement codes and payloads in [Statement templates](p1az_statement_templates.html).

6. In the **Create** list, select the kinds of decisions produced by the policy or rule that will create the statement.

   Statements can apply to `Permit`, `Deny`, `Permit or Deny`, or `Indeterminate` decisions. Select **When Applicable** if the statement applies to any of these. This is the default option.

   |   |                                                                                                                                                                                                                                                                   |
   | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | If you're using a [built-in statement](p1az_statement_templates.html) in a policy that targets protected API services and operations, make sure you select **On Permit**. If the policy or rule produces a `Deny` decision, built-in statements aren't processed. |

   ![Screen capture showing an Include Attributes statement with a name, description, code, and payload. The statement applies to Permit decisions.](_images/zle1666983441336.png)

7. In the **Attach to final decision** list, select an option for how the statement propagates through the decision tree and whether it's returned in the overall decision response.

   ### Choose from:

   * **When all decisions in path match**: The statement is returned when the decision for the rule or policy with which the statement is associated matches all decisions in the path. For example, when the decision for the rule with which the statement is associated is `Permit`, and all decisions in the path are `Permit`, the statement is returned. This is the default option.

   * **When final decision matches "Create" condition**: The statement is returned when the decision for the rule or policy with which the statement is associated matches the overall decision. For example, when the decision for the rule with which the statement is associated is `Permit`, and the overall decision is `Permit`, the statement is returned even if there are `Deny` decisions in between.

   * **Always**: The statement is always returned, unless there's an error in the associated decision.

8. (Optional) In the **Payload** field, enter JSON parameters that govern the actions that the decision point performs when it applies the statement.

   Payloads can include static or interpolated data and provide instructions for things such as filtering and transforming headers, query parameters, and request and response bodies. You can find payload examples in [Statement templates](p1az_statement_templates.html).

   |   |                                                                                                                                    |
   | - | ---------------------------------------------------------------------------------------------------------------------------------- |
   |   | To experiment with JSONPath expressions, use a JSONPath evaluator, such as the [JSONPath Online Evaluator](https://jsonpath.com/). |

9. (Optional) To include attributes relevant to the statement in the decision response, drag one or more attributes from the **Components** tab to the **Attach** field.

10. (Optional) To add the statement to the **Library** as a reusable component, click the hamburger menu next to the **Obligatory** checkbox and select **Add to library**.

11. Click **Save changes**.

## Next steps

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | To reuse a statement in other policies or rules, you can make a copy of it by selecting **Make Copy** from the hamburger menu of that statement. You can copy custom **Library** statements and statements in Library rules, but you can't copy top-level, bootstrapped Library statements.You can copy any Library statement at its point of use. If you copy a Library statement in a rule or policy, the copy displays at the point of use and on the **Library** tab. |

---

---
title: Adding the PingOne Authorize service to your environment
description: Add the PingOne Authorize service to a PingOne environment to enable dynamic authorization and API Access Management capabilities.
component: pingone
page_id: pingone:authorization_using_pingone_authorize:p1az_adding_p1az_service_to_your_environment
canonical_url: https://docs.pingidentity.com/pingone/authorization_using_pingone_authorize/p1az_adding_p1az_service_to_your_environment.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 15, 2026
section_ids:
  before-you-begin: Before you begin
  steps: Steps
---

# Adding the PingOne Authorize service to your environment

To get started with PingOne Authorize, add the service to your PingOne environment.

## Before you begin

* If you don't have a PingOne account yet, [start a PingOne trial](../getting_started_with_pingone/p1_start_a_p1_trial.html).

* Make sure you can [sign on to the PingOne admin console](../getting_started_with_pingone/p1_access_admin_console.html).

* [Add an environment](../getting_started_with_pingone/p1_solution_add_environment.html) to organize your services.

* Make sure you have the Environment Admin and Identity Data Admin roles, or a custom role with equivalent permissions, in your PingOne environment. Learn more in [Managing user roles](../directory/p1_manage_user_roles.html).

## Steps

1. In your PingOne environment, go to **Overview**.

2. Next to **Services**, click the **[icon: plus, set=fa]**icon.

3. Click **[icon: plus, set=fa]Add** to add the **PingOne Authorize** service.

   ![Screen capture showing PingOne Authorize in the Add a Service list.](_images/tam1638807778818.png)

4. In the **Add a Service** window, click **Finish**.

   PingOne Authorize is displayed in the left navigation pane.

---

---
title: Adding value processors to an attribute
description: Define value processors to transform the value returned by an attribute or an attribute resolver.
component: pingone
page_id: pingone:authorization_using_pingone_authorize:p1_az_adding_processors_to_attributes
canonical_url: https://docs.pingidentity.com/pingone/authorization_using_pingone_authorize/p1_az_adding_processors_to_attributes.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: January 15, 2026
section_ids:
  before-you-begin: Before you begin
  steps: Steps
  choose-from: Choose from:
---

# Adding value processors to an attribute

Define value processors to transform the value returned by an attribute or an attribute resolver.

## Before you begin

[Add an attribute](p1_az_adding_attributes.html) and configure the attribute's general settings.

## Steps

1. To add a value processor, do one of the following.

   ### Choose from:

   * **At the attribute level**: Click the **Value Processors** section and click **[icon: plus, set=fa]Add Value Processor**.

     ![Screen capture showing the Processor Name, Processor type, expression, and Value Type fields and the +Add Value Processor button.](_images/p1az-adding-value-processor.png)

   * **At the resolver level**: In the **Resolvers** section, click the hamburger menu next to the **Resolver Name** field and select **Add Processing**.

     ![Screen capture showing processor fields in the Then apply value processors section of a resolver.](_images/p1az-adding-processing-to-resolver.png)

2. (Optional) Update the **Processor Name** field.

3. Select a **Processor** type and enter an expression for the value processor.

   You can find more information about value processor types and expressions in [Processors](p1az_processors.html). The **Label** (![ncd1678229333989](_images/ncd1678229333989.png)) icon indicates that you can [reference attributes](p1_az_interpolating_attributes.html) in the expression.

4. In the **Value type** list, select a [data type](p1_az_value_settings.html) for the transformed value returned after the expression is applied.

---

---
title: Adding value settings to an attribute
description: Define the data type and optional default value for a PingOne Authorize attribute.
component: pingone
page_id: pingone:authorization_using_pingone_authorize:p1_az_adding_value_settings_to_attributes
canonical_url: https://docs.pingidentity.com/pingone/authorization_using_pingone_authorize/p1_az_adding_value_settings_to_attributes.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 15, 2026
section_ids:
  before-you-begin: Before you begin
  steps: Steps
---

# Adding value settings to an attribute

Define the attribute's data type and an optional default value for the attribute.

## Before you begin

[Add an attribute](p1_az_adding_attributes.html) and configure the attribute's general settings.

## Steps

1. **Optional:** In the **Value Settings** section, select the **Default value** check box, and then enter a default value.

   This provides the attribute with a value when it can't otherwise be resolved.

   ![Screen capture showing the Default Value check box, the default value field, and the Type field in attribute Value Settings.](_images/ddk1677111758594.png)

2. To constrain the set of allowable values for the attribute, select a data **Type**.

   For details, see [Value settings](p1_az_value_settings.html).

3. **Optional:** If the data type is **JSON**, enter a valid **JSON Schema**.

   ![Screen capture showing an example JSON schema in attribute Value Settings.](_images/luv1677112009290.png)

   |   |                                                                                      |
   | - | ------------------------------------------------------------------------------------ |
   |   | You can [generate attributes](p1_az_generating_attributes.html) based on the schema. |

---

---
title: API Access Management
description: API Access Management in PingOne Authorize integrates with your API gateway to secure your APIs with centralized access control policies.
component: pingone
page_id: pingone:authorization_using_pingone_authorize:p1_az_api_access_management
canonical_url: https://docs.pingidentity.com/pingone/authorization_using_pingone_authorize/p1_az_api_access_management.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: December 2, 2025
keywords: ["access control;API access"]
section_ids:
  key-components: Key components
  getting-started: Getting started
  p1_aam_wf_p1sso: Using API Access Management with PingOne SSO as the token source
  before-you-begin: Before you begin
  steps: Steps
  choose-from: Choose from:
  p1_aam_wf_ext: Using API Access Management with an external token source
  before-you-begin-2: Before you begin
  steps-2: Steps
---

# API Access Management

API Access Management in PingOne Authorize integrates with your API gateway to secure your APIs with centralized access control policies.

You can control access to your APIs based on a number of factors, such as:

* Access token scopes

* User characteristics such as location, time zone, and full or part-time employee status

* An allow list of IP addresses

Use [built-in rules](p1az_add_api_service_operations.html) to get started with access control and [custom policies](p1az_adding_custom_policies_for_api_services_and_operations.html) for more complex access management scenarios. [Statements](p1az_policy_statements.html) enable you to include, modify, or exclude content in API requests and responses.

## Key components

An [API service](p1az_api_services.html) is a logical container in PingOne Authorize that represents a related set of API operations you want to protect. API Access Management rejects requests that don't match any API service's base URL.

As a basic form of access control, API Access Management validates tokens issued by PingOne SSO and external token sources such as PingOne Advanced Identity Cloud and PingOne Advanced Services. API Access Management rejects requests without a valid access token. Learn more about access control with external token sources in [External OAuth servers in PingOne Authorize](p1_az_external_oauth_servers.html).

An [API gateway](p1az_api_gateways.html) is the bridge between your protected API and PingOne Authorize. A PingOne Authorize integration kit works alongside your API gateway to intercept incoming API calls and enforce your authorization policies. Ping Identity provides [integration kits](https://marketplace.pingone.com/browse?products=authorize\&contentType=integrations) for the following popular third-party gateways:

* [Amazon Web Services](p1_az_amazon_web_services_integration.html)

* [Apigee](p1az_apigee_integration.html)

* [Kong Gateway](p1az_kong_gateway_integration.html)

* [Kong Konnect](p1_az_kong_konnect_integration.html)

Learn more about API Access Management components and the decision request flow in [How API Access Management works](p1az_introduction.html#section_lvy_vgt_zsb).

|   |                                                                                                                 |
| - | --------------------------------------------------------------------------------------------------------------- |
|   | API Access Management works with HTTP APIs and OAuth 2.0 applications, but doesn't work with SAML applications. |

## Getting started

Follow these high-level steps to configure API Access Management components. The process varies based on whether access tokens are issued by PingOne SSO or an external token source. ​

* PingOne SSO

* External token source

### Using API Access Management with PingOne SSO as the token source

#### Before you begin

Make sure your PingOne environment includes PingOne SSO and PingOne Authorize.

#### Steps

1. [Define an API service](p1az_add_api_service.html) that represents your protected APIs.

2. Add an [API gateway](p1az_api_gateways.html) in PingOne that represents your gateway.

3. [Configure an integration kit](p1az_api_gateway_is.html) to connect your API gateway to PingOne.

4. Develop access control rules and policies for protected API operations:

   ##### Choose from:

   * [Use built-in access control rules](p1az_add_api_service_operations.html).

   * [Define custom policies](p1az_adding_custom_policies_for_api_services_and_operations.html).

5. [Add an application](../applications/p1_applications_add_applications.html) in PingOne that represents an API client.

6. Use the client application to make a request to the protected API.

   The request is routed through your API gateway and the integration kit, and then PingOne Authorize evaluates relevant policies and returns an authorization decision that permits or denies access to the requested API resource.

7. To validate the process, [examine recent decisions](p1az_recent_decisions.html) and the [audit log](p1az_monitoring_decision_endpoint_events.html).

### Using API Access Management with an external token source

#### Before you begin

* Make sure your PingOne environment includes PingOne Authorize.

* Ensure that your token source issues access tokens that meet API Access Management requirements. Learn more in [External OAuth servers](p1_az_external_oauth_servers.html).

#### Steps

1. In the system that issues tokens, create an OAuth 2.0 client application.

   In the next steps, you'll need the following information from the token issuer:

   * Token issuer identifier

   * JWKS endpoint URI or JWKS document

   * Token audience

2. In PingOne, [add an external OAuth server](p1_az_adding_external_oauth_servers.html) that represents your token issuer.

3. [Define an API service](p1az_add_api_service.html) that represents your protected APIs.

   Select **External OAuth Server** as the access token source.

4. Add an [API gateway](p1az_api_gateways.html) in PingOne that represents your gateway.

5. [Configure an integration kit](p1az_api_gateway_is.html) to connect your API gateway to PingOne.

6. [Develop custom policies](p1az_adding_custom_policies_for_api_services_and_operations.html) for protected API operations.

   |   |                                                                                                                                                                                                            |
   | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | You can use built-in attributes based on access token claims in your policies. Learn more about these attributes in [Access token-related attributes](p1_az_built_in_attributes.html#p1-token-attributes). |

7. Use the client application to make a request to the protected API.

   The request is routed through your API gateway and the integration kit, and then PingOne Authorize evaluates relevant policies and returns an authorization decision that permits or denies access to the requested API resource.

8. To validate the process, [examine recent decisions](p1az_recent_decisions.html) and the [audit log](p1az_monitoring_decision_endpoint_events.html).

---

---
title: API gateways
description: An API gateway in PingOne Authorize defines the connection between your API gateway and PingOne Authorize and authenticates your API gateway to PingOne.
component: pingone
page_id: pingone:authorization_using_pingone_authorize:p1az_api_gateways
canonical_url: https://docs.pingidentity.com/pingone/authorization_using_pingone_authorize/p1az_api_gateways.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 6, 2025
---

# API gateways

An API gateway in PingOne Authorize defines the connection between your API gateway and PingOne Authorize and authenticates your API gateway to PingOne.

Ping Identity provides [integration kits](p1az_api_gateway_is.html) for third-party API gateways that make it easier for you to manage access control in your APIs. Working with the integration kit in your API gateway, PingOne Authorize uses the best practices of OAuth to manage API access control across these distributed systems.

PingOne Authorize also integrates natively with PingGateway, enabling you to apply low-code access controls for APIs and web applications. Learn more about [integrating PingOne Authorize with PingGateway](https://docs.pingidentity.com/pinggateway/latest/pingone/aam.html) in the PingGateway documentation.

For seamless policy-based access control for your HTTP APIs, configure an integration with PingOne Authorize to have your API gateway enforce authorization rules managed in PingOne Authorize. In addition to configuring an API gateway integration, you can [edit](p1az_edit_api_gateway.html) or [delete](p1az_delete_api_gateway.html) an API gateway, or [rotate a gateway credential](p1az_rotating_gateway_credential.html).

Learn more about how traffic flows through an API gateway and PingOne Authorize in [How API Access Management works](p1az_introduction.html#section_lvy_vgt_zsb).

---

---
title: API services
description: An API service is the fundamental unit of access control in PingOne Authorize that represents the API you want to protect.
component: pingone
page_id: pingone:authorization_using_pingone_authorize:p1az_api_services
canonical_url: https://docs.pingidentity.com/pingone/authorization_using_pingone_authorize/p1az_api_services.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 5, 2025
section_ids:
  access-control-policies: Access control policies
  token-management: Token management
  pingone-sso-token-source: PingOne SSO token source
  external-token-source: External token source
  policy-deployment: Policy deployment
---

# API services

An API service is the fundamental unit of access control in PingOne Authorize that represents the API you want to protect.

## Access control policies

To control access to your APIs, you can use built-in access control rules and custom policies. Built-in access control rules grant access based on:

* Authorized scopes

* User membership in groups

* User permissions

* Authentication policy

* Time since last authentication

Learn more about these rules in [Defining operations for protected actions](p1az_add_api_service_operations.html).

For more complex access control scenarios, you can define custom policies in the **API Access Management** policy tree. Learn more in [Adding custom policies for API services and operations](p1az_adding_custom_policies_for_api_services_and_operations.html).

## Token management

An API service groups related API operations into a protected domain, such as https\://example-api-domain.com, that clients access with a single access token. When you [define an API service](p1az_add_api_service.html), you can use PingOne SSO to issue access tokens and manage users for the API service, or you can use external token sources such as PingOne Advanced Services or PingOne Advanced Identity Cloud.

### PingOne SSO token source

If you use PingOne SSO to issue tokens for the API service, PingOne Authorize works with PingOne resources and applications to manage access control for your API. You can configure access control rules that are tightly integrated with PingOne. You can also define custom policies that handle more complex authorization scenarios.

Each API service is associated with a PingOne resource. This resource is a representation of your API for OAuth authorization purposes. Resources have scopes that are used in access token configuration. Scopes determine which resources a client can access. PingOne Authorize uses scopes to:

* Ensure that the access token presented by a client was issued for your API. In this basic access control check, PingOne Authorize verifies that the audience claim in the access token for the client request matches the audience value configured for the API service's associated resource.

  |   |                                                                                                                                                                                                                                                                                            |
  | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
  |   | After you define an API service, make sure that you [add a PingOne application](../applications/p1_applications_add_applications.html) that's allowed to access your protected API service. To allow access, grant the application the same scope that you configured for the API service. |

* Determine the extent of access allowed to a client. For example, your API might require a `user:read` scope for reading user data and a `user:write` scope for modifying user data. You can configure a built-in access control rule to perform authorized scope checks.

When authorizing an HTTP request, if the request's access token includes a subject, PingOne Authorize automatically populates the built-in [`PingOne.User`](p1_az_built_in_attributes.html) attribute with the requesting user's data.

### External token source

If access tokens come from an external token source, PingOne Authorize validates the access token and inspects its claims. You can use the claims in custom policies to secure your APIs with claims-based access control. You can't use built-in access control rules when tokens come from external sources.

PingOne Authorize doesn't automatically provide identity information about the requesting user in built-in user attributes when tokens come from an external source. Instead, if the request's access token includes a subject claim, you can use the `PingOne.API Access Management.Identity.Access Token.Subject` attribute to resolve user identity information from an external directory. Learn more in [API Access Management attributes](p1_az_built_in_attributes.html).

Learn more about external token sources in [External OAuth servers in PingOne Authorize](p1_az_external_oauth_servers.html).

## Policy deployment

Each API service has a system-owned [decision endpoint](p1az_decision_endpoints.html) that provides an environment for managing and deploying authorization policies relevant to the API service. The decision endpoint is created when you deploy the API service for the first time, and it has the same name as the API service. Learn more in [Deploying an API service](p1az_deploying_api_services.html).

---

---
title: Application roles
description: Application roles in PingOne Authorize group permissions by function to control user access to application resources.
component: pingone
page_id: pingone:authorization_using_pingone_authorize:p1_az_application_roles
canonical_url: https://docs.pingidentity.com/pingone/authorization_using_pingone_authorize/p1_az_application_roles.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 15, 2026
---

# Application roles

Application roles provide a way to group permissions by function and assign them to users.

Application roles are collections of [application permissions](../applications/p1_application_permissions.html). When you assign a user to a role, you grant the user all of the permissions for that role.

|   |                                                                                                                                                                                                                                                                                                                                                   |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | PingOne [administrator roles](../directory/p1_roles.html) are collections of permissions that give PingOne admins access to resources in the PingOne admin console, such as organizations, environments, and identities.Application roles help you manage access to the application resources developed by your organization's engineering teams. |

You can assign the same permission to multiple roles. For example, at a bank, both an account administrator and loan officer could have permission to view accounts.

You can also assign multiple roles to the same user. For example, at a small regional bank, Jim might be both an account administrator and a loan officer.

You can assign users to roles when you create an application role or when you edit a user. Learn more in [Adding an application role](p1_az_adding_application_roles.html) and [Managing user roles](../directory/p1_manage_user_roles.html).

|   |                                                                          |
| - | ------------------------------------------------------------------------ |
|   | Roles and permissions are currently scoped to an environment in PingOne. |