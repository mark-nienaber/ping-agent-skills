---
title: Custom nodes
description: Create custom authentication nodes to define properties and run custom server-side scripts for reusable journey functionality
component: pingoneaic
page_id: pingoneaic:journeys:node-designer
canonical_url: https://docs.pingidentity.com/pingoneaic/journeys/node-designer.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Authentication", "Node Designer", "Nodes &amp; Trees"]
section_ids:
  design_secure_nodes: Design secure nodes
  create-node-type: Create a custom node
  use-node: Use your custom node
  export-custom-node: Export a custom node
  import-custom-node: Import a custom node
  delete-custom-node: Delete a custom node
  example-custom-node: "Example: Generate JWT node"
---

# Custom nodes

Advanced Identity Cloud lets you create your own nodes to reuse common functionality in authentication journeys. Define properties and run custom server-side scripts in these nodes to dynamically set values and decide the outcome of journeys.

To write a script for your custom node, you can use any of the next-generation script bindings available to the [Scripted Decision node API](../am-scripting/scripting-api-node.html), including `httpClient`, `cacheManager`, and `openidm`.

For example, use custom nodes to perform these functions:

* Update email addresses for users based on their location

* Add users to a particular group

* Generate a JWT and store it in shared state

* Gather user input through [callbacks](../am-scripting/scripting-api-node.html#scripting-api-node-callbacks)

New custom nodes appear in the node list in the journey editor ready for you to include in your journey. A custom node is realm-agnostic, so you can access it from any realm, not just the realm in which you created it. You can use custom nodes in your journey like any other node, including as part of child journeys, in page nodes, and with Configuration Provider nodes.

You can also share the functionality across tenants by exporting your custom node and importing it into a different environment.

|   |                                                                                                                                                                                                                      |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | You can't use library scripts with custom nodes. Custom nodes are designed to be self-contained units so that you can import and export them. Import and export functionality isn't compatible with library scripts. |

## Design secure nodes

Before you start creating nodes, read the following points of best practice to make sure your custom nodes are as secure as possible.

* Don't add sensitive data to shared state

  Store sensitive information such as passwords in [ESVs](../tenants/esvs.html).

* Sanitize input data

  Remove sensitive information before using or storing data.

* Don't log sensitive data

  Make sure you don't output sensitive information to logs.

## Create a custom node

These steps describe how to create an example custom node called `Set Employee Details` in the Advanced Identity Cloud admin console. The node defines two properties, `Employee location` and `Employee group`. The node's script uses these values to add an email address and set state data.

1. In the Advanced Identity Cloud admin console, in either realm, go to Journeys > Custom Nodes and click [icon: plus, set=fa]New Custom Node.

   |   |                                                                                                                                                                 |
   | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | Custom nodes are global objects and don't belong to a realm, so even if you create a custom node in the `alpha` realm, you can access it from the `beta` realm. |

2. Enter node details so that you can identify the node in the journey editor.

   | Field       | Description                                                                                               |
   | ----------- | --------------------------------------------------------------------------------------------------------- |
   | Name        | The node name that's displayed in the journey editor. For example, `Set Employee Details`.                |
   | Description | (Optional) The description of the node's purpose that's displayed in the node properties.                 |
   | Category    | (Optional) Select a category from the list. Your custom node appears under this section in the node list. |
   | Tags        | (Optional) Add tags to organize the node. You can use these to search for your node in the node list.     |

3. Add node properties that you can configure in the journey editor.

   Access the properties by their names through the `properties` binding in your node script. The values depend on the journey configuration.

   | Field                    | Value                                                                                                                                                                                                                                                                                                                                                           |
   | ------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | Name                     | The property name to reference from the node script. It must be unique and can only contain alphanumeric and underscore characters. For example, `emp_group`.                                                                                                                                                                                                   |
   | Label                    | The label appears as the property name in the node properties panel. It must be unique. For example, `Employee group`.                                                                                                                                                                                                                                          |
   | Description              | (Optional) The description appears as the property tooltip.                                                                                                                                                                                                                                                                                                     |
   | Type                     | The input type:- `String`: A single alphanumeric string

   - `Number`: A single numeric string

   - `Boolean`: Lets the user select a checkbox

   - `Object`: Lets the user input a JSON object in a basic script editor                                                                                                                                              |
   | Multi-Valued             | Enables multiple separate values for `String` or `Number` properties.                                                                                                                                                                                                                                                                                           |
   | Required                 | Whether it's mandatory to enter a value for this property.                                                                                                                                                                                                                                                                                                      |
   | Enumerated Values        | For `String` input, define values that display in the UI as a list.The key must only contain upper-case letters, numbers, and underscores. The value can be any valid string.For example, the `Employee location` property has the following enumerated values:![custom node emp location](../realms/_images/custom-node-emp-location.png)                      |
   | Provide Default Value(s) | The initial property value(s) displayed in the UI.If you defined `Enumerated Values`, the default value must match an enumerated value.If you selected `Multi-Valued`, you can specify more than one default value.For example, the `Employee group` property has multiple default values:![custom node emp group](../realms/_images/custom-node-emp-group.png) |

4. Configure settings for your node.

   | Field                  | Value                                                                                                                                                                                        |
   | ---------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | Outcomes               | The named outcome paths for the node. You must specify at least one value. For example, `True` `False`.                                                                                      |
   | Require Script Inputs  | List the node state data required by the node. For example, `username`.If you don't list anything here, the node can access all shared and transient state data.                             |
   | Require Script Outputs | List the data the node outputs to shared state.If you don't list anything here, the node sets all state data.                                                                                |
   | Error Outcome          | Enable to add an extra path for scripting errors, for example, if the script references an outcome that's not defined in the Outcomes field.The outcome appears on the node as Script Error. |

5. In the Javascript editor, write or paste a [next-generation script](../am-scripting/next-generation-scripts.html) to run when a journey processes your custom node.

   Use the custom node binding, `properties`, to reference the configured values that you've defined as properties. In addition to `properties`, your script has access to all the Scripted Decision node script bindings, such as `nodestate` and `callbacks`.

   Although custom nodes are similar to Scripted Decision nodes, they have their own script context and a separate thread pool.

   Find examples of scripts and how to use the bindings in the [Scripted Decision node API](../am-scripting/scripting-api-node.html).

   For example, the following script adds an email address to the user profile and stores employee details in node state:

   ```javascript
   // Get UUID by enabling "Username as Universal Identifier"
   // in a preceding Identity Store Decision node
   var uuid = nodeState.get("username");
   var identity = idRepository.getIdentity(uuid);

   var fn = identity.getAttributeValues("givenName")[0];
   var sn = identity.getAttributeValues("sn")[0];
   var username = fn + "_" + sn;

   if (properties.emp_location == "UK") {
       identity.addAttribute("mail", username + "@example.co.uk");
   }
   else if (properties.emp_location == "FR") {
       identity.addAttribute("mail", username + "@example.fr");
   }
   else {
       identity.addAttribute("mail", username + "@example.com");
   }
   identity.store();

   nodeState.putShared("location", properties.emp_location);
   nodeState.putShared("group", properties.emp_group);

   action.goTo("True");
   ```

   |   |                                                                                                           |
   | - | --------------------------------------------------------------------------------------------------------- |
   |   | Custom node scripts only appear in the node. You can't manage these scripts under Scripts > Auth Scripts. |

6. Save your changes.

## Use your custom node

Include your new node in a journey and set values appropriate for the journey.

1. In the Advanced Identity Cloud admin console, create a [custom journey](journeys.html#custom-journey).

2. Search for your custom node in the Nodes list using the tags, node name, or by expanding the category of your node.

3. Add the node to your journey and set its properties to values that are appropriate for your authentication journey.

   |   |                                                                                                         |
   | - | ------------------------------------------------------------------------------------------------------- |
   |   | You can view all the journeys that include your custom node in Custom Nodes > *Custom node* > Overview. |

4. If you need to make changes to your node, edit its configuration in the custom node editor and return to the journey editor.

   You might need to delete the node from your journey and select a new instance to view updates.

This authentication journey uses the example custom node, Set Employee Details, to set user-specific information based on node configuration.

![custom node journey example](../realms/_images/custom-node-journey-example.png)

The node is configured with the following values:

* Employee location

  `New York`

* Employee group

  `Admin` `Sales`

For a user, `bjensen`, the node adds the email address `Babs_Jensen@example.com` to the `mail` identity profile attribute and sets the following data in `nodeState`:

```json
  ...
  "location": "New York",
  "group": [
      "Admin",
      "Sales"
  ]
  ...
}
```

## Export a custom node

To reuse nodes in other environments, you can export them to a JSON file.

1. In the Advanced Identity Cloud admin console, go to Journeys > Custom Nodes, and click Export.

2. Click Export.

3. The node definitions are downloaded to a JSON file.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | Exporting custom nodes doesn't include external dependencies. To make sure exported nodes work as expected, make a note of any dependencies before you export the node. Dependencies might include those relied on by bindings that interact with external services and configuration, for example, `openidm`, `secrets`, and `httpClient`.You can then use these notes to replicate the dependencies when importing the custom node into a different environment. |

## Import a custom node

To reuse custom nodes in other environments, you can import a JSON file containing one or more node definitions.

1. In the Advanced Identity Cloud admin console, go to Journeys > Custom Nodes, and click Import.

2. On the Import Node page, browse to and select a JSON file that contains the node definition to import.

3. Click Import.

   Advanced Identity Cloud displays an error if a node of that type already exists or the JSON is invalid.

## Delete a custom node

Deleting a custom node is a permanent operation. You can't retrieve a custom node after it's deleted.

Delete a custom node in the following ways:

* In the Advanced Identity Cloud admin console, go to Journeys > Custom Nodes, and click on the node you want to delete. Click More ([icon: ellipsis-h, set=fa]) and choose Delete.

* In the journey editor, click More ([icon: ellipsis-h, set=fa]) and choose Delete.

|   |                                                           |
| - | --------------------------------------------------------- |
|   | You can't delete a custom node if it's used in a journey. |

## Example: Generate JWT node

This example generates a signed JWT with the HMAC SHA-256 algorithm using the username and journey configuration. It then sets the generated key in shared state.

1. Create a custom node with the following settings:

   |             |                                                         |
   | ----------- | ------------------------------------------------------- |
   | Name        | Generate JWT                                            |
   | Description | Generate a signed JWT using the HMAC SHA-256 algorithm. |
   | Categories  | `Utilities`                                             |

2. Add properties with the following names and details.

   |              |                      |          |          |                       |
   | ------------ | -------------------- | -------- | -------- | --------------------- |
   | Name         | Label                | Type     | Required | Provide Default Value |
   | `audience`   | `Audience`           | `String` | Enabled  |                       |
   | `issuer`     | `Issuer`             | `String` | Enabled  |                       |
   | `signingkey` | `HMAC Signing Key`   | `String` | Enabled  | `esv.signing.key`     |
   | `validity`   | `Validity (minutes)` | `Number` | Enabled  | `5`                   |

3. Configure the node settings:

   |               |                |
   | ------------- | -------------- |
   | Outcomes      | `True` `False` |
   | Error Outcome | Enabled        |

4. Paste the following script into the JavaScript editor:

   ```java
   var aud = properties.audience;
   var iss = properties.issuer;
   var validity = properties.validity;
   var esv = properties.signingkey;

   var signingkey = systemEnv.getProperty(esv);

   var username = nodeState.get("username");

   var data = {
     jwtType:"SIGNED",
     jwsAlgorithm: "HS256",
     issuer: iss,
     subject: username,
     audience: aud,
     type: "JWT",
     validityMinutes: validity,
     signingKey: signingkey
   };

   var jwt = jwtAssertion.generateJwt(data);

   if (jwt !== null && jwt.length > 0) {
     nodeState.putShared("assertionJwt" , jwt);
     action.goTo("True");
   } else {
     action.goTo("False");
   }
   ```

5. Create a journey that includes an instance of the new node.

   For example:

   ![Generate JWT node example tree](../realms/_images/custom-node-jwt-journey.png)

6. Configure the node properties with the following values:

   * Audience

     Enter a valid value for the audience claim.

   * Issuer

     Enter a valid value for the issuer.

   * HMAC Signing Key

     Enter a valid [ESV](../tenants/esvs.html) that's mapped to an HMAC signing secret.

   ![custom node jwt node](../realms/_images/custom-node-jwt-node.png)

7. Test the journey. [Enable debug mode](../end-user/debug-enduser-journeys.html#enable-debug-mode) to verify that the JWT is added to shared state:

   ```json
   {
       "realm": "/alpha",
       "assertionJwt": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUz...rXNQ4QhFeIBC2LiH-Sr72Q4",
       ...
   }
   ```

---

---
title: Financial services journey
description: Implement a prebuilt financial services journey providing secure and adaptive digital banking with risk-based authentication and fraud detection
component: pingoneaic
page_id: pingoneaic:journeys:solution-financial-services-journey
canonical_url: https://docs.pingidentity.com/pingoneaic/journeys/solution-financial-services-journey.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Authentication", "Journeys"]
section_ids:
  about-financial-services-journey: About the financial services journey
  fs-use-case: Example use case
  fs-components: Journey components
  financial-services-before-begin: Before you begin
  financial-services-task1: "Task 1: Prepare your tenant environment"
  financial-services-custom-attributes: Add custom attributes to the alpha_user managed object
  user_profile_and_security_attributes: User profile and security attributes
  transaction_and_payment_control_attributes: Transaction and payment control attributes
  account_and_balance_attributes: Account and balance attributes
  advanced_and_calculated_attributes: Advanced and calculated attributes
  fs-optional_set_an_esv_variable: (Optional) Set an ESV variable for PingOne Protect analysis
  task_2_create_pingone_authorize_policies: "Task 2: Create PingOne Authorize policies"
  define_the_attributes: Define the attributes
  fs-payment-check-policy: Create the payment check policy
  fs-kba-policy: Create the enhanced KBA policy
  financial-services-download-import-journey: "Task 3: Download and import the journey"
  download_the_journey: Download the journey
  import_the_journey: Import the journey
  configure-financial-services-journey: "Task 4: Configure the journey components"
  configure-fs-main-journey: Configure the financial services main journey
  fs-review-set-initialize-variables: Review and set the initialize variables
  fs-configure-url: Configure the success URL
  fs-set-journey-for-all-users: Set the journey to run for all users regardless of current session
  configure-fs-threat-detection-inner-journey: Configure the Threat Detection Inner Journey
  configure-fs-mfa-auth-inner-journey: Configure the MFA Authentication Inner Journey
  configure-fs-enhanced-kba-journey: Configure the Enhanced KBA Inner Journey
  configure-fs-make-payment-inner-journey: Configure the Make Payment Inner Journey
  configure-fs-make-transfer-inner-journey: Configure the Make Transfer Inner Journey
  fs-validation: "Task 5: Validate the journey"
  before_you_begin: Before you begin
  fs-validation-low-risk-sign-on: Test a low-risk sign-on
  fs-validation-high-risk: Test a high-risk sign-on
  fs-validation-low-risk-payment: Test a low-risk payment
  fs-validation-high-risk-payment: Test a high-risk payment
  fs-journey-best-practices: Best practices
---

# Financial services journey

The Ping Identity Marketplace includes a prebuilt [financial services journey](https://marketplace.pingone.com/item/financial-services-aic-journey-pack). The journey provides secure and adaptive digital banking that protects against fraud and account takeover. It lets end users make safe payments and transfers, as well as managing accounts and privacy settings.

The journey is intended as a template. Review and adapt it to meet your organization's specific security policies and business requirements before deploying to a production environment.

**Journey download**

| Journey name       | Version | Download                                                                                              |
| ------------------ | ------- | ----------------------------------------------------------------------------------------------------- |
| Financial services | 1.0     | [Download from Marketplace](https://marketplace.pingone.com/item/financial-services-aic-journey-pack) |

This guide details the prerequisites and configuration steps to implement this solution in your Advanced Identity Cloud tenant.

## About the financial services journey

This solution uses a main journey and inner journeys to evaluate the risk level of a user's sign-on attempt. Authenticated end users can manage their account settings and make financial transactions.

### Example use case

A bank needs to protect against fraud while maintaining a smooth customer experience. To do this, they want a journey that provides adaptive security by evaluating risk signals in real time across various end-user actions, from sign-on to financial transactions and data sharing. Users should be able to set preferences, such as enabling online payments and setting transaction limits. The solution would allow routine, low-value payments to proceed seamlessly, while automatically triggering a multi-factor authentication (MFA) challenge or knowledge-based authentication (KBA) for high-value transfers or suspicious activity to verify the user's identity.

### Journey components

The financial services journey includes one main journey and nine inner journeys.

| Journey                                                   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Configuration required? |
| --------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------- |
| **Financial Services - Main Journey**                     | Orchestrates the entire user session, coordinating security checks before granting access to account management options.> **Collapse: Show details**
>
> This journey orchestrates the entire user session, acting as the main entry point.
>
> It starts by checking for an active session. If none exists, it delegates the sign-on process to the **Financial Services - SignOn Inner Journey**.
>
> After the user is authenticated, the main journey performs the following security checks to secure the session:
>
> * **Threat detection**: Calls the **Financial Services - Threat Detection Inner Journey** to evaluate the real-time risk of the sign-on attempt using PingOne Protect.
>
>   The threat detection journey sets the authentication level based on the detected risk level. A medium to high risk level increases the authentication level.
>
> * **Authentication step-up**: The **Auth Level Decision** node evaluates the user's current authentication level. A higher authentication level is interpreted as higher risk for subsequent steps, which triggers MFA.
>
>   Switching the True and False outputs of the Auth Level Decision node means a higher current authentication level is interpreted as lower risk, and MFA won't be triggered. This isn't recommended for this journey.
>
> After all security checks pass successfully, the user is redirected to the **Financial Services - Manage Account Inner Journey**, where they can access their account details and perform financial tasks.                       | Yes                     |
| **Financial Services - SignOn Inner Journey**             | Manages the initial user sign-on, including credential validation, email verification, and security checks> **Collapse: Show details**
>
> The journey performs the following checks:
>
> * **Threat analysis**: Determines if a threat analysis is required. If so, it initiates PingOne Protect for risk evaluation by calling the **Financial Services - Threat Detection Inner Journey**.
>
>   The threat detection journey sets the authentication level based on the detected risk level. A medium to high risk level increases the authentication level.
>
> * **User authentication**: Presents a sign-on page for the user to enter their username and password.
>
> * **Account status check**: Checks if the user's email address has been verified. If not, it sends an email with a link to complete the verification before allowing the user to proceed.
>
> * **Authentication step-up**: The **Auth Level Decision** node evaluates the user's current authentication level. A higher authentication level is interpreted as higher risk for subsequent steps, which triggers MFA.
>
>   Switching the True and False outputs of the Auth Level Decision node means a higher current authentication level is interpreted as lower risk, and MFA won't be triggered. This isn't recommended for this journey.
>
> * **Accept terms and conditions**: Checks if the user has accepted the latest terms and conditions. If they haven't, they're prompted to accept them.
>
> On successful completion of all checks, the user is granted access. | No                      |
| **Financial Services - Threat Detection Inner Journey**   | Performs real-time threat detection using PingOne Protect to assess session risk.> **Collapse: Show details**
>
> The journey gathers behavioral data from the user's session and determines a risk level. Depending on the assessed risk, the journey takes different paths:
>
> * **Low risk**: The journey proceeds, but also checks for indicators such as a new device or other suspicious parameters.
>
> * **Medium to high risk**: Increases the required authentication level, asking for stronger user verification before continuing.
>
> * **Specific threats** (for example, bots or man-in-the-middle): Checks if the user's account is active. If it is, the account is disabled, and an alert email is sent to the user.
>
> * **Failure**: If any part of the risk evaluation fails, the journey logs the failure and terminates.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Yes                     |
| **Financial Services - MFA Authentication Inner Journey** | Orchestrates the MFA process, prompting for and verifying a second factor.> **Collapse: Show details**
>
> The journey starts by identifying an existing user and then prompts them to select an authentication method.
>
> The journey proceeds with one of the following MFA flows:
>
> * **Email**: Generates a one-time passcode (OTP) and sends it to the user's email address for verification.
>
> * **SMS / Voice**: Uses Twilio to send a verification code to the user's registered phone number through SMS or a voice call.
>
> * **FIDO2** (WebAuthn): Initiates authentication using a security key or biometrics.
>
> * **OATH**: Asks the user to enter a verification code from an authenticator app.
>
> * **Push**: Sends a push notification to a registered device for approval.
>
> * **Magic Link**: Emails a unique link that the user clicks to sign on.
>
> For most methods, if the user fails to authenticate, they're given a limited number of retry attempts before the journey fails. The journey also includes paths for users to authenticate using a recovery code if other methods are unavailable.                                                                                                                                                                                                                                                                                                                                                                                                                          | Yes                     |
| **Financial Services - Enhanced KBA Inner Journey**       | Performs an enhanced Knowledge-based authentication (KBA) check.> **Collapse: Show details**
>
> The journey starts by identifying an existing user. It then proceeds as follows:
>
> * **Initial assessment**: Calculates a KBA threshold based on factors such as the user's transaction history and timestamps. This determines if they need to answer security questions.
>
> * **Authorization policy**: The initial assessment is sent to a PingOne Authorize policy. The policy decides whether to:
>
>   * Permit the request, allowing the user to proceed.
>
>   * Challenge the user with security questions.
>
> * **Challenge**: If challenged, the user is presented with a security question. Their response is sent back to the PingOne Authorize policy for a new decision.
>
>   This cycle repeats until the user is permitted or denied. A denial also occurs if the user runs out of questions.
>
> The specific questions used for the challenge are configured in the PingOne Authorize policy's statements. Learn more in [Create the enhanced KBA policy](#fs-kba-policy).                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Yes                     |
| **Financial Services - Manage Account Inner Journey**     | Presents as a post-authentication page that lets users perform account management tasks.> **Collapse: Show details**
>
> The journey starts by checking for an active user session. If a session is found, it displays the Manage Your Account page where the user can choose from several options, such as Make a Payment, Make a Transfer, Account Settings, or Privacy Settings.
>
> The journey might require the user to perform MFA to increase their security level:
>
> * The **Auth Level Decision** node evaluates the user's current authentication level. A higher authentication level is interpreted as higher risk for subsequent steps, which triggers MFA.
>
>   Switching the True and False outputs of the Auth Level Decision node means a higher current authentication level is interpreted as lower risk, and MFA won't be triggered. This isn't recommended for this journey.
>
> * If MFA is required, the **Modify Auth Level** node reduces the authentication level so that the user isn't prompted for MFA again in the same session.
>
> The journey then checks if a risk evaluation update with PingOne Protect is necessary and performs it.
>
> Finally, it directs the user to a separate, inner journey to handle their request.                                                                                                                                                                                                                                                                                             | No                      |
| **Financial Services - Make Transfer Inner Journey**      | Orchestrates the secure process for making transfers between a checking account and a savings account. It includes risk-based authorization checks.> **Collapse: Show details**
>
> The journey starts by identifying the user. After successful identification, the user can proceed to enter the transfer amount and other details.
>
> The journey performs the following checks:
>
> * **KBA**: Intentionally slows down the transaction to protect a user who might be getting scammed by calling the **Financial Services - Enhanced KBA Inner Journey**.
>
> * **Risk-based authorization**: Validates the input using the [PingOne Authorize node](https://docs.pingidentity.com/auth-node-ref/latest/pingone/pingone-authorize.html) to assess the transaction risk. Depending on the outcome, it might require a push notification for approval.
>
> If the transfer is permitted, the user's savings and checking account balances are updated.
>
> The journey includes paths to handle various errors, such as invalid input or insufficient balance, which typically redirect the user back to the Manage Your Account page to make corrections.                                                                                                                                                                                                                                                                                                                                                                                                   | Yes                     |
| **Financial Services - Make Payment Inner Journey**       | Orchestrates the secure process for making transfers between a checking or savings account and a credit card or mortgage account. It includes risk-based authorization checks.> **Collapse: Show details**
>
> The journey starts by identifying the user. After successful identification, the user can proceed to enter the payment amount and other details.
>
> The journey performs the following checks:
>
> * **KBA**: Intentionally slows down the transaction to protect a user who might be getting scammed, by calling the **Financial Services - Enhanced KBA Inner Journey**.
>
> * **Risk-based authorization**: Validates the input using the [PingOne Authorize node](https://docs.pingidentity.com/auth-node-ref/latest/pingone/pingone-authorize.html) to assess the transaction risk. Depending on the outcome, it might require a push notification for approval.
>
> If the payment is permitted, the user's mortgage or credit card account is updated.
>
> The journey includes paths to handle various errors, such as invalid input or insufficient balance, which typically redirect the user back to the Manage Your Account page to make corrections.                                                                                                                                                                                                                                                                                                                                                                                | Yes                     |
| **Financial Services - Account Settings Inner Journey**   | Lets authenticated users view and modify their profile and account details.> **Collapse: Show details**
>
> The journey starts by identifying the user. After successful identification, it displays the Account Settings page allowing the user to select account settings.
>
> If the user provides incorrect details, an error message shows, and the user is returned to the Account Settings page to make corrections.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | No                      |
| **Financial services - Privacy Settings Inner Journey**   | Lets authenticated users manage their data sharing and privacy preferences.> **Collapse: Show details**
>
> The journey starts by identifying the user. After successful identification, it displays the Privacy Settings page allowing the user to manage their privacy settings.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | No                      |

## Before you begin

To implement the sample financial services journey, you must have the following prerequisites:

* Tenant administrator access to your Advanced Identity Cloud development environment.

* For PingOne Protect:

  * PingOne Protect enabled in your PingOne environment. Learn more in [Getting started with PingOne Protect](https://docs.pingidentity.com/pingone/threat_protection_using_pingone_protect/p1_protect_getting_started.html).

  * PingOne Protect integrated with Advanced Identity Cloud. Learn more in [Use PingOne Protect for risk-based authentication and fraud detection](../integrations/pingone-protect.html).

* For PingOne Authorize:

  * PingOne Authorize enabled in your PingOne environment. Learn more in [Getting started with PingOne Authorize](https://docs.pingidentity.com/pingone/authorization_using_pingone_authorize/p1az_getting_started.html).

  * Your PingOne Authorize [decision endpoint](https://docs.pingidentity.com/pingone/authorization_using_pingone_authorize/p1az_decision_endpoints.html).

* Your PingOne Worker service ID. Learn more in [Set up PingOne product connections](../integrations/pingone-set-up-product-connections.html)

  |   |                                                                                                                                                                                       |
  | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | The worker application associated with the PingOne Worker Service must be granted the necessary permissions to interact with both the PingOne Protect and PingOne Authorize services. |

* For MFA:

  * If you're using Twilio for phone-based MFA, a Twilio account with access to [Twilio Verify](https://www.twilio.com).

* A test user in your `Alpha` realm with a registered email address. It's also useful to have other MFA methods configured for testing.

* A basic understanding of [journeys](journeys.html) and the [Scripted Decision node](https://docs.pingidentity.com/auth-node-ref/latest/scripted-decision.html).

## Task 1: Prepare your tenant environment

To get the journey working you must first perform some setup tasks in your Advanced Identity Cloud tenant environment.

### Add custom attributes to the `alpha_user` managed object

Add the following custom attributes to the Advanced Identity Cloud `alpha_user` managed object. Learn more in [Customize user identities using custom attributes](../identities/identity-cloud-identity-schema.html#create-custom-attributes).

|   |                                                                                                                                                                                                                                                                                                                                                                      |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | When adding new attributes, use advanced options to specify view and edit permissions:- User Editable: Select this option if you want end users to be able to edit the property value in their profile.

- Viewable: Clear this option to hide the property from the user's profile. However, this hides the property from both end users and tenant administrators. |

#### User profile and security attributes

| Name                     | Label                    | Type   | Description                                          |
| ------------------------ | ------------------------ | ------ | ---------------------------------------------------- |
| `custom_emailVerified`   | `Email verified`         | String | Confirms the user has verified their email address.  |
| `custom_mfaDevices`      | `MFA devices`            | Array  | Stores the user's registered MFA devices.            |
| `custom_latestMFADevice` | `Latest used MFA device` | String | The user's most recently used registered MFA device. |

#### Transaction and payment control attributes

| Name                       | Label                   | Type    | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| -------------------------- | ----------------------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `custom_currency`          | `Custom currency`       | String  | The user's preferred currency.Select User Editable to allow end users to change this value.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `custom_maxPaymentLimit`   | `Maximum payment limit` | Number  | The user's maximum payment limit.Ping Identity recommends that you enter a default value. For example, `20000`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| `custom_minPaymentLimit`   | `Minimum payment limit` | Number  | The user's minimum payment limit.Ping Identity recommends that you enter a default value. For example, `10`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `custom_transactionStatus` | `Transaction status`    | Boolean | Indicates whether transactions are enabled or disabled for the user.Select User Editable to allow end users to change this setting.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `custom_transactionLimit`  | `Set Transaction Limit` | Number  | The maximum transaction value allowed for a single transaction.Ping Identity recommends that you enter a default value. For example, `10000`.Select User Editable to allow end users to change this value in their account settings.&#xA;&#xA;Ping Identity recommends that the UI label for this setting is Set Transaction Limit. However, if you change it, you must also change it in the journey:&#xA;&#xA;In the Advanced Identity Cloud admin console, go to the Financial Services - Account Settings Inner Journey.&#xA;&#xA;Open the Account Settings Page node for editing.&#xA;&#xA;In the Account Setting Script, update the value of the transactionLimitLabel variable to your preferred text. |
| `custom_approvalLimit`     | `Set Approval Limit`    | Number  | The transaction value above which push authentication is required.Ping Identity recommends that you enter a default value. For example, `1000`.Select User Editable to allow end users to change this value in their account settings.&#xA;&#xA;Ping Identity recommends that the UI label for this setting is Set Approval Limit. However, if you change it, you must also change it in the journey:&#xA;&#xA;In the Advanced Identity Cloud admin console, go to the Financial Services - Account Settings Inner Journey.&#xA;&#xA;Open the Account Settings Page node for editing.&#xA;&#xA;In the Account Setting Script, update the value of the approvalLimitLabel variable to your preferred text.     |

#### Account and balance attributes

| Name                       | Label                     | Type   | Description                                                                                                                                                      |
| -------------------------- | ------------------------- | ------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `custom_checkingBalance`   | `Latest checking balance` | Number | The user's current balance in their checking account.                                                                                                            |
| `custom_savingsBalance`    | `Latest savings balance`  | Number | The user's current balance in their savings account.                                                                                                             |
| `custom_mortgageAccount`   | `Mortgage account`        | Object | Stores the user's mortgage account details. Add the following properties in the `custom_mortgageAccount` object:- `accountNumber` - string

- `balance` - number |
| `custom_creditCardAccount` | `Credit card account`     | Object | Stores the user's credit card details.Add the following properties in the `custom_creditCardAccount` object:- `accountNumber` - string

- `balance` - number     |

#### Advanced and calculated attributes

| Name                        | Label                 | Type   | Description                                                                                                                                                                                                                                                                                                                |
| --------------------------- | --------------------- | ------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `custom_accountVisibility`  | `Account visibility`  | Object | Stores user preferences for account visibility to third-party vendorsAdd the following properties in the `custom_accountVisibility` object:- `creditCard` - string

- `mortgage` - string                                                                                                                                  |
| `custom_transactionHistory` | `Transaction history` | Array  | An array of objects, where each object stores details of a past transaction. This is used to calculate the KBA threshold. A maximum of 50 days of transactions are stored.Add the following properties in the `Transaction history` object:- `from` - string

- `to` - string

- `amount` - number

- `timestamp` - number |
| `custom_kbaThreshold`       | `KBA threshold`       | Number | The threshold limit for triggering a KBA prompt, calculated based on the `custom_transactionHistory` and the requested transaction amount. The value is based on the last transaction.                                                                                                                                     |

### (Optional) Set an ESV variable for PingOne Protect analysis

The **Prerequisites & Init Variables** node in the main journey contains a script that uses the `protectAnalysisRequired` variable to determine if PingOne Protect analysis is enabled. By default, this variable is set to `true` in the script. To override this variable and control how PingOne Protect analysis is performed in different environments, you can set an [Environment Secret & Variable (ESV)](../tenants/esvs.html) variable.

1. In the Advanced Identity Cloud admin console, go to [icon: cog, set=fa]Tenant Settings > Global Settings > Environment Secrets & Variables.

2. On the Variables tab, click + Add Variable.

3. In the Add a Variable modal, enter the following information:

   |                        |                                     |
   | ---------------------- | ----------------------------------- |
   | Name                   | `p1-protect-analysis-required`      |
   | Type                   | `string`                            |
   | Description (optional) | `PingOne Protect analysis required` |
   | Value                  | `true`                              |

4. Click Save to create the variable.

5. Restart Advanced Identity Cloud services by [applying updates in the Advanced Identity Cloud admin console](../tenants/esvs-manage-ui.html#apply-updates).

## Task 2: Create PingOne Authorize policies

To perform risk-based authorization for payments and transfers, you must create two authorization policies in PingOne Authorize. These policies use custom attributes to evaluate the context of a transaction.

### Define the attributes

First, define the attributes that the policies will use to make decisions.

1. In the PingOne admin console, go to Authorization > Trust Framework.

2. Click the Attributes tab.

3. For each attribute in the following table, click + Add new Attribute and configure it with the specified values. For these attributes, you'll need to add a second resolver to set a default constant value.

   | Attribute name            | Value type | Default resolver type | Default value |
   | ------------------------- | ---------- | --------------------- | ------------- |
   | `Action`                  | String     | Constant (String)     | `Default`     |
   | `amount`                  | Number     | Constant (Number)     | `-1`          |
   | `custom_approvalLimit`    | Number     | Constant (Number)     | `-1`          |
   | `custom_transactionLimit` | Number     | Constant (Number)     | `-1`          |

   > **Collapse: Show attributes**
   >
   > ![Action attribute](_images/financial-services-sample/authorize-attributes.png)

### Create the payment check policy

This policy evaluates a payment's amount against the user's transaction limits.

1. In the PingOne admin console, go to Authorization > Policies.

2. Click the Plus icon ([icon: add, set=material, size=inline]) and select Add Policy.

3. Configure the main policy settings:

   * Name: `AIC payment checks`

   * Applies When: The policy applies when **all** of the following comparisons are true:

     * `amount` `Does Not Equal` `-1`

     * `custom_transactionLimit` `Does Not Equal` `-1`

     * `custom_approvalLimit` `Does Not Equal` `-1`

4. Add the following rules to the policy in order.

   Rule 1: Deny payments over the maximum limit

   * Name: `Deny payments over maximum transaction limit`

   * Applies When: `amount` `Greater Than` `custom_transactionLimit`

   * Effect: `Deny`

   Rule 2: Permit payments under the approval threshold

   * Name: `Permit payments less than threshold limit`

   * Applies When: `amount` `Less Than or Equal` `custom_approvalLimit`

   * Effect: `Permit`

   Rule 3: Require approval for payments over the threshold

   * Name: `Require approval for payments over threshold limit`

   * Applies When: `amount` `Greater Than` `custom_approvalLimit`

   * Effect: `Permit`

   * Statements: Add a statement with the following values:

     * Name: `Push required`

     * Code: `PUSH_REQ`

5. Click **Save Changes**.

### Create the enhanced KBA policy

This policy determines if a KBA challenge is required based on the `Action` attribute.

1. In the PingOne admin console, go to Authorization > Policies.

2. Click [icon: add, set=material, size=inline] and select Add Policy.

3. Configure the main policy settings:

   * Name: `Enhanced KBA Policy`

   * Applies When: `Action` `Does Not Equal` `Default`

4. Add the following rules to the policy in order.

   Rule 1: Deny rule

   * Name: `Deny if Action is Deny`

   * Applies When: `Action` `Equals` `deny`

   * Effect: `Deny`

   Rule 2: Permit rule

   * Name: `Permit if Action is Permit`

   * Applies When: `Action` `Equals` `permit`

   * Effect: `Permit`

   Rule 3: KBA challenge rule

   * Name: `Challenge if Action is Challenge`

   * Effect: `Permit if condition holds, otherwise deny`

   * When: `Action` `Equals` `challenge`

   * Statements: Add a statement with the following values:

     * Name: `KBA_REQUIRED`

     * Code: `KBA_REQUIRED`

     * Create: `On Permit`

     * Payload:

       > **Collapse: Show payload**
       >
       > ```json
       > {
       >   "kbaQuestionSets": [
       >     {
       >       "question": {
       >         "key": "Q1",
       >         "text": "Wait - could this be a scam?  Tell us your reason so we can protect you."
       >       },
       >       "answers": {
       >         "1": {
       >           "key": "Q1.A1",
       >           "text": "Making an investment",
       >           "action": "challenge"
       >         },
       >         "2": { "key": "Q1.A2", "text": "Account Transfer", "action": "permit" },
       >         "3": { "key": "Q1.A3", "text": "Investing in Crypto", "action": "deny" }
       >       }
       >     },
       >     {
       >       "question": {
       >         "key": "Q2",
       >         "text": "This seems to be an unusual payment. To help us protect your account, what is the primary reason for this transfer?"
       >       },
       >       "answers": {
       >         "1": {
       >           "key": "Q2.A1",
       >           "text": "Paying a family member or a friend.",
       >           "action": "permit"
       >         },
       >         "2": {
       >           "key": "Q2.A2",
       >           "text": "Purchasing a high-value item (e.g., car, jewelry).",
       >           "action": "challenge"
       >         },
       >         "3": {
       >           "key": "Q2.A3",
       >           "text": "Investing in cryptocurrency.",
       >           "action": "deny"
       >         },
       >         "4": {
       >           "key": "Q2.A4",
       >           "text": "To secure my funds after an unexpected call from my bank/police.",
       >           "action": "deny"
       >         },
       >         "5": {
       >           "key": "Q2.A5",
       >           "text": "An online investment with guaranteed high returns.",
       >           "action": "deny"
       >         }
       >       }
       >     },
       >     {
       >       "question": {
       >         "key": "Q3",
       >         "text": "We see this is a new recipient. How did you receive their account details?"
       >       },
       >       "answers": {
       >         "1": {
       >           "key": "Q3.A1",
       >           "text": "From an official company invoice or website.",
       >           "action": "permit"
       >         },
       >         "2": {
       >           "key": "Q3.A2",
       >           "text": "From an email or text message.",
       >           "action": "challenge"
       >         },
       >         "3": {
       >           "key": "Q3.A3",
       >           "text": "Over the phone from someone who called me unexpectedly.",
       >           "action": "deny"
       >         },
       >         "4": {
       >           "key": "Q3.A4",
       >           "text": "From a person I have only met on a social media or dating app.",
       >           "action": "deny"
       >         }
       >       }
       >     },
       >     {
       >       "question": {
       >         "key": "Q4",
       >         "text": "Are you being pressured to make this payment right now to avoid a fine, unlock an account, or secure a prize?"
       >       },
       >       "answers": {
       >         "1": {
       >           "key": "Q4.A1",
       >           "text": "No, I am making this payment on my own time without any pressure.",
       >           "action": "permit"
       >         },
       >         "2": {
       >           "key": "Q4.A2",
       >           "text": "Yes, I was told it must be done immediately.",
       >           "action": "deny"
       >         },
       >         "3": {
       >           "key": "Q4.A3",
       >           "text": "I am not sure if I am being pressured.",
       >           "action": "challenge"
       >         }
       >       }
       >     },
       >     {
       >       "question": {
       >         "key": "Q5",
       >         "text": "Is anyone you do not personally know guiding you through this payment on your computer or phone right now?"
       >       },
       >       "answers": {
       >         "1": {
       >           "key": "Q5.A1",
       >           "text": "No, I am in full control and completing this myself.",
       >           "action": "permit"
       >         },
       >         "2": {
       >           "key": "Q5.A2",
       >           "text": "Yes, a support agent or bank employee is helping me remotely.",
       >           "action": "deny"
       >         },
       >         "3": {
       >           "key": "Q5.A3",
       >           "text": "A friend or family member is helping me.",
       >           "action": "challenge"
       >         }
       >       }
       >     },
       >     {
       >       "question": {
       >         "key": "Q6",
       >         "text": "Have you ever met the person you are sending this money to in real life?"
       >       },
       >       "answers": {
       >         "1": {
       >           "key": "Q6.A1",
       >           "text": "Yes, they are a friend, family member, or business contact I know personally.",
       >           "action": "permit"
       >         },
       >         "2": {
       >           "key": "Q6.A2",
       >           "text": "No, I have only ever interacted with them online or over the phone.",
       >           "action": "deny"
       >         },
       >         "3": {
       >           "key": "Q6.A3",
       >           "text": "This is for an online purchase from a company.",
       >           "action": "challenge"
       >         }
       >       }
       >     },
       >     {
       >       "question": {
       >         "key": "Q7",
       >         "text": "What is the expected outcome of this payment?"
       >       },
       >       "answers": {
       >         "1": {
       >           "key": "Q7.A1",
       >           "text": "To pay for goods or services from a known vendor.",
       >           "action": "permit"
       >         },
       >         "2": {
       >           "key": "Q7.A2",
       >           "text": "To pay a tax bill or government fine I was notified of by phone or email.",
       >           "action": "deny"
       >         },
       >         "3": {
       >           "key": "Q7.A3",
       >           "text": "To claim lottery winnings, an inheritance, or a prize.",
       >           "action": "deny"
       >         },
       >         "4": {
       >           "key": "Q7.A4",
       >           "text": "To pay a contractor for home repairs.",
       >           "action": "challenge"
       >         }
       >       }
       >     }
       >   ]
       > }
       > ```

5. Click **Save Changes**.

## Task 3: Download and import the journey

### Download the journey

1. Go to [Financial Services journey](https://marketplace.pingone.com/item/financial-services-aic-journey-pack) on the Ping Identity Marketplace.

2. Click Download Integration to download the `Financial Services - Main Journey.json` file. This JSON file contains the main journey and inner journeys, scripts, and email templates required for the authentication flow.

### Import the journey

1. In the Advanced Identity Cloud admin console, click Journeys > Journeys.

2. Click [icon: add, set=material, size=inline] Add Journey, select Import, and then click Next.

3. Click either Download Backup or Skip Backup. Learn more in [Import journeys](journeys.html#import-journeys).

4. On the Import Journeys page, browse to and select `Financial Services - Main Journey.json`.

5. Select `Alpha realm users` because the journey is configured for the Alpha realm.

6. In the Conflict Resolution section, choose how the system resolves import conflicts:

   * Overwrite all conflicts (default)

   * Manually pick conflict resolution

7. Click Next.

8. Click Start Import.

9. On the Import Complete page, click Done.

10. On the left panel of the Journeys page, click Financial Services (10) view the financial services main journey and inner journeys.

## Task 4: Configure the journey components

### Configure the financial services main journey

1. On the Journeys page, click Financial Services - Main Journey and click Edit.

2. In the journey editor, configure the journey as follows:

   * [Review and set the initialize variables](#fs-review-set-initialize-variables)

   * [Configure the success URL](#fs-configure-url)

   * [Set the journey to run for all users regardless of current session](#fs-set-journey-for-all-users)

3. Click Save.

|   |                                                                                                                                                                                             |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | To save your progress, periodically click Save in the top right of the journey editor. If you don't save, you'll lose your work if the page reloads or if you lose your network connection. |

#### Review and set the initialize variables

The **Financial Services - Main Journey** includes a [Scripted Decision node](https://docs.pingidentity.com/auth-node-ref/latest/scripted-decision.html) containing the initialize variables used later in the authentication flow. This script lets you:

* Set the allowed MFA types: `FIDO2`, `OATH`, `PUSH`, `EMAIL`, `SMS`, `VOICE`.

* Enable or disable PingOne Protect analysis.

* Enable or disable [magic link](../am-authentication/suspended-auth.html).

To review and set the initial variables:

1. Click the Prerequisites & Init Variables node.

2. In the Script field, click the Pencil icon ([icon: pencil-alt, set=fa]) to open the `Financial Services - Initialize Variables` script.

3. Review the script and make changes if needed.

4. Click Save and Close.

|   |                                                                                                             |
| - | ----------------------------------------------------------------------------------------------------------- |
|   | You don't need to update the values in the Script Outputs field of the Prerequisites & Init Variables node. |

#### Configure the success URL

1. Click the Success URL node.

2. Enter the preview URL of the Financial Services - Manage Account Inner Journey. For example:

   `https://<tenant-env-fqdn>/am/XUI/?realm=alpha&authIndexType=service&authIndexValue=Financial%20Services%20-%20Manage%20Account%20Inner%20Journey`.

3. Click Save.

#### Set the journey to run for all users regardless of current session

1. In the upper right of the journey editor, click the Ellipsis icon ([icon: ellipsis-h, set=fa]) and select [icon: pencil-alt, set=fa]Edit Details.

2. Select Run journey for all users regardless of current session.

3. Click Save.

### Configure the Threat Detection Inner Journey

1. On the Journeys page, click Financial Services - Threat Detection Inner Journey and click Edit.

2. In the journey editor, configure the journey as follows:

   1. Click the PingOne Protect Initialize node and enter the following:

      * PingOne Worker Service ID: Select the ID of the PingOne Worker Service for connecting to PingOne. Learn more in [PingOne Protect Initialize node](https://docs.pingidentity.com/auth-node-ref/latest/pingone/pingone-protect-initialize.html).

   2. Click the Auth: PingOne Protect Authentication node and enter the following:

      * PingOne Worker Service ID: Select the ID of the PingOne worker service for connecting to PingOne.

      * (Optional) Risk Policy Set ID: Enter the ID of the [risk policy](https://docs.pingidentity.com/pingone/threat_protection_using_pingone_protect/p1_protect_risk_policies.html) in PingOne. Learn more in [PingOne Protect Evaluation node](https://docs.pingidentity.com/auth-node-ref/latest/pingone/pingone-protect-evaluation.html).

   3. Click the PingOne Protect Authorization node and enter the following:

      * PingOne Worker Service ID: Enter the ID of the PingOne worker service for connecting to PingOne.

      * (Optional) Risk Policy Set ID: Enter the ID of the [risk policy](https://docs.pingidentity.com/pingone/threat_protection_using_pingone_protect/p1_protect_risk_policies.html) in PingOne. Learn more in [PingOne Protect Evaluation node](https://docs.pingidentity.com/auth-node-ref/latest/pingone/pingone-protect-evaluation.html).

3. Click Save.

### Configure the MFA Authentication Inner Journey

This configuration is required if `SMS`, or `VOICE` are opted in the `allowedMFATypes` array in the `Financial Services - Initialize Variables` script in the [Prerequisites & Init Variables](#fs-optional_set_an_esv_variable) node in the main journey.

1. On the Journeys page, click `MFA Authentication Inner Journey` and click Edit.

2. In the journey editor, update the required fields in the following nodes:

   * [Twilio Verify Lookup node](https://docs.pingidentity.com/auth-node-ref/latest/cloud/twilio-verify-lookup.html)

   * [Twilio Verify Sender node](https://docs.pingidentity.com/auth-node-ref/latest/cloud/auth-node-twilio-verify-sender.html)

3. Click Save.

### Configure the Enhanced KBA Inner Journey

1. On the Journeys page, click Financial Services - Enhanced KBA Inner Journey and click Edit.

2. In the journey editor, click the PingOne Authorize node and enter the following:

   * PingOne Worker Service ID: Select the ID of the PingOne worker service for connecting to PingOne.

   * In the Decision Endpoint ID: Enter the decision endpoint ID from the service in PingOne Authorize

   Learn more about the [PingOne Authorize node](https://docs.pingidentity.com/auth-node-ref/latest/pingone/pingone-authorize.html)

3. Click Save.

### Configure the Make Payment Inner Journey

1. On the Journeys page, click Financial Services - Make Payment Inner Journey and click Edit.

2. In the journey editor, click the PingOne Authorize node and enter the following:

   * PingOne Worker Service ID: Select the ID of the PingOne worker service for connecting to PingOne.

   * In the Decision Endpoint ID: Enter the decision endpoint ID from the service in PingOne Authorize.

   Learn more about the [PingOne Authorize node](https://docs.pingidentity.com/auth-node-ref/latest/pingone/pingone-authorize.html)

3. Click Save.

### Configure the Make Transfer Inner Journey

1. On the Journeys page, click Financial Services - Make Transfer Inner Journey and click Edit.

2. In the journey editor, click the PingOne Authorize node and enter the following:

   * PingOne Worker Service ID: Select the ID of the PingOne worker service for connecting to PingOne.

   * In the Decision Endpoint ID: Enter the decision endpoint ID from the service in PingOne Authorize.

     Learn more about the [PingOne Authorize node](https://docs.pingidentity.com/auth-node-ref/latest/pingone/pingone-authorize.html)

3. Click Save.

## Task 5: Validate the journey

After configuring the journey, test the different paths to ensure the risk-based security policies work as expected. The following steps demonstrate low-risk and high-risk sign-on attempts, and low-risk and high-risk transactions.

|   |                                                                                                                                                                                                                                                                                                                              |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | To trigger different risk evaluations, you may need to adjust your [risk policies in PingOne Protect](https://docs.pingidentity.com/pingone/threat_protection_using_pingone_protect/p1_protect_risk_policies.html) or sign on using different conditions (for example, using a VPN or a new device to simulate higher risk). |

### Before you begin

Add values for the following attributes for your test user: In the Advanced Identity Cloud admin console, go to Identities > Manage.

1. Click Alpha realm - Users and

2. On the Manage Identities page, click [icon: people, set=material, size=inline] Alpha realm - Users and find and select your test user.

3. Enter values in the following fields:

   * Minimum payment limit

   * Maximum payment limit

   * Latest savings balance

   * Latest checking balance

   * Account visibility

   * Mortgage account

   * Credit card account

   * Custom currency

4. Click Save.

### Test a low-risk sign-on

1. In the Advanced Identity Cloud admin console, go to Journeys.

2. Click Financial Services - Main Journey.

3. In the Preview URL field, click [icon: copy, set=material, size=inline] and paste the URL into an incognito window.

   The browser displays the Sign In hosted journey page.

4. Enter your test user's username and password and click Next.

   The browser displays the Manage Your Account hosted account page.

   |   |                                                                                                                                                        |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
   |   | Because the sign-on is evaluated as low risk, you're authenticated without an MFA challenge. This confirms the frictionless path is working correctly. |

   ![Manage Your Account page](_images/financial-services-sample/manage-account.png)

5. Click Account Settings and complete the following:

   * The maximum allowed transaction limit during any transaction: `1000`

   * The threshold limit above which push approval step is required before successful transaction: `500`

   * Online Transactions: `Enabled`

   ![Account Settings page](_images/financial-services-sample/account-settings.png)

6. Click Save.

### Test a high-risk sign-on

This test validates that the journey blocks a sign-on attempt that PingOne Protect evaluates as high risk (for example, an attempt from an anonymous proxy).

1. Using a new incognito window or a browser configured to use a VPN, go to the preview URL for the Financial Services - Main Journey.

2. On the Sign In screen, enter your test user's username and password and click Next.

**Expected result**: The journey identifies the high-risk attempt and blocks the sign-on. An error message displays, and the user's account might be disabled. You should also receive an email notification confirming that the high-risk security response was triggered.

### Test a low-risk payment

1. If you're not already signed on, follow the steps in [Test a low-risk sign-on](#fs-validation-low-risk-sign-on) to sign on as your test user.

2. Click Make a Payment.

3. Enter a payment amount below the transaction threshold (for example, `400`).

   ![Manage Your Account page](_images/financial-services-sample/make-payment.png)

4. Click Make Payment.

**Expected result**: The payment is successful. The page confirms the transaction was completed, and the user's account balance is updated.

### Test a high-risk payment

This test validates that a payment exceeding the maximum transaction limit is blocked.

1. If you're not already signed on, follow the steps in [Test a low-risk sign-on](#fs-validation-low-risk-sign-on) to sign on as your test user and arrive at the Manage Your Account page.

2. Click Make a Payment.

3. Enter a payment amount greater than the payment limit (for example, `6000`) and complete the payment details.

4. Click Submit.

**Expected result**: The payment is denied. An error message displays, indicating that the transaction exceeds the maximum limit. This confirms the high-risk payment path is correctly blocking the transaction.

## Best practices

This sample journey provides a strong foundation for a financial services journey. When preparing to use it in a production environment, consider the following best practices:

* **Treat as a template**: Remember that this is a sample journey. Always adapt and harden it to meet your specific security policies and business requirements before deploying to production.

* **Use ESVs**: Avoid hardcoding sensitive information like API keys and IDs directly in your journey scripts. Use [ESVs](../tenants/esvs.html) to manage these values securely.

* **Test extensively**: Validate all possible user paths, including low, medium, and high-risk scenarios, as different MFA registration and authentication flows. Ensure the user experience is smooth and the security responses are correct for each case.

* **Review PingOne Protect policies**: Fine-tune your [risk policies in PingOne Protect](https://docs.pingidentity.com/pingone/threat_protection_using_pingone_protect/p1_protect_risk_policies.html) to align with your organization's risk tolerance.

---

---
title: Journey nodes
description: Reference guide for all available authentication nodes used to build journeys including basic, multi-factor, risk, and behavioral nodes
component: pingoneaic
page_id: pingoneaic:journeys:auth-nodes
canonical_url: https://docs.pingidentity.com/pingoneaic/journeys/auth-nodes.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Nodes &amp; Trees", "Journeys", "Authentication", "Data Store", "LDAP", "Identity Store", "OAuth 2.0", "Multi-factor Authentication (MFA)", "Account", "CAPTCHA", "Federation", "SAML 2.0", "Social Authentication", "Terms &amp; Condition", "Email", "Scripts"]
page_aliases: ["realms:auth-nodes.adoc"]
section_ids:
  basic-authn-nodes: Basic authentication nodes
  multifactor-authn-nodes: Multi-factor authentication nodes
  risk-authn-nodes: Risk management authentication nodes
  behavioral-authn-nodes: Behavioral authentication nodes
  contextual-authn-nodes: Contextual authentication nodes
  federation-authn-nodes: Federation authentication nodes
  identity-authn-nodes: Identity management authentication nodes
  utility-authn-nodes: Utility nodes
  uncategorized-nodes: Uncategorized nodes
  marketplace-nodes: Marketplace nodes
---

# Journey nodes

This page lists the authentication nodes available for you to use in PingOne Advanced Identity Cloud journeys.

|   |                                                                                                                          |
| - | ------------------------------------------------------------------------------------------------------------------------ |
|   | You can also create your own [custom nodes](node-designer.html) if none of the available nodes meet your business needs. |

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Even though they appear in the UI, the following nodes are incompatible with Advanced Identity Cloud and their reference documentation isn't provided:- Password Collector node (use the [Platform Password node](https://docs.pingidentity.com/auth-node-ref/latest/platform-password.html) instead)

- Username Collector node (use the [Platform Username node](https://docs.pingidentity.com/auth-node-ref/latest/platform-username.html) instead)

- Kerberos node

- Authenticate Thing node

- Register Thing node |

## Basic authentication nodes

Use the following nodes for basic authentication tasks:

* [AD Decision node](https://docs.pingidentity.com/auth-node-ref/latest/ad-decision.html)

* [Data Store Decision node](https://docs.pingidentity.com/auth-node-ref/latest/data-store-decision.html)

* [Failure node](https://docs.pingidentity.com/auth-node-ref/latest/failure.html)

* [Identity Store Decision node](https://docs.pingidentity.com/auth-node-ref/latest/cloud/identity-store-decision.html)

* [LDAP Decision node](https://docs.pingidentity.com/auth-node-ref/latest/ldap-decision.html)

* [Success node](https://docs.pingidentity.com/auth-node-ref/latest/success.html)

* [Zero Page Login Collector node](https://docs.pingidentity.com/auth-node-ref/latest/zero-page-login-collector.html)

## Multi-factor authentication nodes

Use the following nodes to configure journeys with multi-factor authentication capabilities:

* [Combined MFA Registration node](https://docs.pingidentity.com/auth-node-ref/latest/combined-mfa-registration.html)

* [Device Binding node](https://docs.pingidentity.com/auth-node-ref/latest/device-binding.html)

* [Device Binding Storage node](https://docs.pingidentity.com/auth-node-ref/latest/device-binding-storage.html)

* [Device Signing Verifier node](https://docs.pingidentity.com/auth-node-ref/latest/device-signing-verifier.html)

* [Enable Device Management node](https://docs.pingidentity.com/auth-node-ref/latest/enable-device-management.html)

* [Get Authenticator App node](https://docs.pingidentity.com/auth-node-ref/latest/get-authenticator-app.html)

* [HOTP Generator node](https://docs.pingidentity.com/auth-node-ref/latest/hotp-generator.html)

* [MFA Registration Options node](https://docs.pingidentity.com/auth-node-ref/latest/mfa-registration-options.html)

* [OATH Device Storage node](https://docs.pingidentity.com/auth-node-ref/latest/oath-device-storage.html)

* [OATH Registration node](https://docs.pingidentity.com/auth-node-ref/latest/oath-registration.html)

* [OATH Token Verifier node](https://docs.pingidentity.com/auth-node-ref/latest/oath-token-verifier.html)

* [Opt-out Multi-Factor Authentication node](https://docs.pingidentity.com/auth-node-ref/latest/opt-out-multi-factor.html)

* [OTP Collector Decision node](https://docs.pingidentity.com/auth-node-ref/latest/otp-collector-decision.html)

* [OTP Email Sender node](https://docs.pingidentity.com/auth-node-ref/latest/otp-email-sender.html)

* [OTP SMS Sender node](https://docs.pingidentity.com/auth-node-ref/latest/otp-sms-sender.html)

* [Push Registration node](https://docs.pingidentity.com/auth-node-ref/latest/push-registration.html)

* [Push Result Verifier node](https://docs.pingidentity.com/auth-node-ref/latest/push-result-verifier.html)

* [Push Sender node](https://docs.pingidentity.com/auth-node-ref/latest/push-sender.html)

* [Push Wait node](https://docs.pingidentity.com/auth-node-ref/latest/push-wait.html)

* [Recovery Code Collector Decision node](https://docs.pingidentity.com/auth-node-ref/latest/recovery-code-collector-decision.html)

* [Recovery Code Display node](https://docs.pingidentity.com/auth-node-ref/latest/recovery-code-display.html)

* [RSA SecurID node](https://docs.pingidentity.com/auth-node-ref/latest/rsa-securid.html)

* [TypingDNA Decision node](https://docs.pingidentity.com/auth-node-ref/latest/cloud/tdna-decision.html)

* [TypingDNA Recorder node](https://docs.pingidentity.com/auth-node-ref/latest/cloud/tdna-recorder.html)

* [TypingDNA Reset Profile node](https://docs.pingidentity.com/auth-node-ref/latest/cloud/tdna-reset-profile.html)

* [TypingDNA Short Phrase Collector node](https://docs.pingidentity.com/auth-node-ref/latest/cloud/tdna-short-phrase-collector.html)

* [WebAuthn Authentication node](https://docs.pingidentity.com/auth-node-ref/latest/webauthn-authentication.html)

* [WebAuthn Device Storage node](https://docs.pingidentity.com/auth-node-ref/latest/webauthn-device-storage.html)

* [WebAuthn Registration node](https://docs.pingidentity.com/auth-node-ref/latest/webauthn-registration.html)

## Risk management authentication nodes

Use the following nodes to examine the perceived risk and act on it:

* [Account Active Decision node](https://docs.pingidentity.com/auth-node-ref/latest/account-active-decision.html)

* [Account Lockout node](https://docs.pingidentity.com/auth-node-ref/latest/account-lockout.html)

* [Auth Level Decision node](https://docs.pingidentity.com/auth-node-ref/latest/auth-level-decision.html)

* [CAPTCHA node](https://docs.pingidentity.com/auth-node-ref/latest/captcha.html)

* [Legacy CAPTCHA node](https://docs.pingidentity.com/auth-node-ref/latest/legacy-captcha.html)

* [Modify Auth Level node](https://docs.pingidentity.com/auth-node-ref/latest/modify-auth-level.html)

* [PingOne Protect Evaluation node](https://docs.pingidentity.com/auth-node-ref/latest/pingone/pingone-protect-evaluation.html)

* [PingOne Protect Initialize node](https://docs.pingidentity.com/auth-node-ref/latest/pingone/pingone-protect-initialize.html)

* [PingOne Protect Result node](https://docs.pingidentity.com/auth-node-ref/latest/pingone/pingone-protect-result.html)

* [reCAPTCHA Enterprise node](https://docs.pingidentity.com/auth-node-ref/latest/recaptcha-enterprise.html)

## Behavioral authentication nodes

Use the following nodes to adjust the behavior of authentication journeys:

* [Increment Login Count node](https://docs.pingidentity.com/auth-node-ref/latest/increment-login-count.html)

* [Login Count Decision node](https://docs.pingidentity.com/auth-node-ref/latest/login-count-decision.html)

* [TypingDNA Decision node](https://docs.pingidentity.com/auth-node-ref/latest/cloud/tdna-decision.html)

* [TypingDNA Recorder node](https://docs.pingidentity.com/auth-node-ref/latest/cloud/tdna-recorder.html)

* [TypingDNA Reset Profile node](https://docs.pingidentity.com/auth-node-ref/latest/cloud/tdna-reset-profile.html)

* [TypingDNA Short Phrase Collector node](https://docs.pingidentity.com/auth-node-ref/latest/cloud/tdna-short-phrase-collector.html)

## Contextual authentication nodes

Use the following nodes to change the journey or set a cookie based on the authentication context:

* [Certificate Collector node](https://docs.pingidentity.com/auth-node-ref/latest/certificate-collector.html)

* [Certificate User Extractor node](https://docs.pingidentity.com/auth-node-ref/latest/certificate-user-extractor.html)

* [Certificate Validation node](https://docs.pingidentity.com/auth-node-ref/latest/certificate-validation.html)

* [Cookie Presence Decision node](https://docs.pingidentity.com/auth-node-ref/latest/cookie-presence-decision.html)

* [Device Geofencing node](https://docs.pingidentity.com/auth-node-ref/latest/device-geofencing.html)

* [Device Location Match node](https://docs.pingidentity.com/auth-node-ref/latest/device-location-match.html)

* [Device Match node](https://docs.pingidentity.com/auth-node-ref/latest/device-match.html)

* [Device Profile Collector node](https://docs.pingidentity.com/auth-node-ref/latest/device-profile-collector.html)

* [Device Profile Save node](https://docs.pingidentity.com/auth-node-ref/latest/device-profile-save.html)

* [Device Tampering Verification node](https://docs.pingidentity.com/auth-node-ref/latest/device-tampering-verification.html)

* [Persistent Cookie Decision node](https://docs.pingidentity.com/auth-node-ref/latest/persistent-cookie-decision.html)

* [Set Custom Cookie node](https://docs.pingidentity.com/auth-node-ref/latest/set-custom-cookie.html)

* [Set Persistent Cookie node](https://docs.pingidentity.com/auth-node-ref/latest/set-persistent-cookie.html)

## Federation authentication nodes

Use the following nodes to configure journeys with federation capabilities:

* [Legacy Social Provider Handler node](https://docs.pingidentity.com/auth-node-ref/latest/legacy-social-provider-handler.html)

* [OIDC ID Token Validator node](https://docs.pingidentity.com/auth-node-ref/latest/oidc-idtoken-validator.html)

* [SAML2 Authentication node](https://docs.pingidentity.com/auth-node-ref/latest/saml2.html)

* [Social Provider Handler node](https://docs.pingidentity.com/auth-node-ref/latest/social-provider-handler.html)

* [Write Federation Information node](https://docs.pingidentity.com/auth-node-ref/latest/write-federation-information.html)

## Identity management authentication nodes

Use the following nodes to perform identity management during an authentication journey:

* [Accept Terms and Conditions node](https://docs.pingidentity.com/auth-node-ref/latest/accept-terms-and-conditions.html)

* [Attribute Collector node](https://docs.pingidentity.com/auth-node-ref/latest/attribute-collector.html)

* [Attribute Present Decision node](https://docs.pingidentity.com/auth-node-ref/latest/attribute-present-decision.html)

* [Attribute Value Decision node](https://docs.pingidentity.com/auth-node-ref/latest/attribute-value-decision.html)

* [Consent Collector node](https://docs.pingidentity.com/auth-node-ref/latest/consent-collector.html)

* [Create Object node](https://docs.pingidentity.com/auth-node-ref/latest/create-object.html)

* [Display Username node](https://docs.pingidentity.com/auth-node-ref/latest/display-username.html)

* [Identify Existing User node](https://docs.pingidentity.com/auth-node-ref/latest/identify-existing-user.html)

* [KBA Decision node](https://docs.pingidentity.com/auth-node-ref/latest/kba-decision.html)

* [KBA Definition node](https://docs.pingidentity.com/auth-node-ref/latest/kba-definition.html)

* [KBA Verification node](https://docs.pingidentity.com/auth-node-ref/latest/kba-verification.html)

* [Pass-through Authentication node](https://docs.pingidentity.com/auth-node-ref/latest/passthrough-authentication.html)

* [Patch Object node](https://docs.pingidentity.com/auth-node-ref/latest/patch-object.html)

* [PingOne Create User node](https://docs.pingidentity.com/auth-node-ref/latest/pingone/pingone-create-user.html)

* [PingOne Delete User node](https://docs.pingidentity.com/auth-node-ref/latest/pingone/pingone-delete-user.html)

* [PingOne Identity Match node](https://docs.pingidentity.com/auth-node-ref/latest/pingone/pingone-identity-match.html)

* [PingOne Verify Completion Decision node](https://docs.pingidentity.com/auth-node-ref/latest/pingone/pingone-verify-completion-decision.html)

* [PingOne Verify Evaluation node](https://docs.pingidentity.com/auth-node-ref/latest/pingone/pingone-verify-evaluation.html)

* [Platform Password node](https://docs.pingidentity.com/auth-node-ref/latest/platform-password.html)

* [Platform Username node](https://docs.pingidentity.com/auth-node-ref/latest/platform-username.html)

* [Profile Completeness Decision node](https://docs.pingidentity.com/auth-node-ref/latest/profile-completeness-decision.html)

* [Query Filter Decision node](https://docs.pingidentity.com/auth-node-ref/latest/query-filter-decision.html)

* [Required Attributes Present node](https://docs.pingidentity.com/auth-node-ref/latest/required-attributes-present.html)

* [Select Identity Provider node](https://docs.pingidentity.com/auth-node-ref/latest/select-identity-provider.html)

* [Terms and Conditions Decision node](https://docs.pingidentity.com/auth-node-ref/latest/terms-and-conditions-decision.html)

* [Time Since Decision node](https://docs.pingidentity.com/auth-node-ref/latest/time-since-decision.html)

## Utility nodes

Use the following nodes to perform various tasks during the journey:

* [Agent Data Store Decision node](https://docs.pingidentity.com/auth-node-ref/latest/agent-data-store-decision.html)

* [Anonymous Session Upgrade node](https://docs.pingidentity.com/auth-node-ref/latest/anonymous-session-upgrade.html)

* [Anonymous User Mapping node](https://docs.pingidentity.com/auth-node-ref/latest/anonymous-user-mapping.html)

* [Backchannel Initialize node](https://docs.pingidentity.com/auth-node-ref/latest/backchannel-initialize.html)

* [Backchannel Notification node](https://docs.pingidentity.com/auth-node-ref/latest/backchannel-notification.html)

* [Backchannel Status node](https://docs.pingidentity.com/auth-node-ref/latest/backchannel-status.html)

* [Choice Collector node](https://docs.pingidentity.com/auth-node-ref/latest/choice-collector.html)

* [Configuration Provider node](https://docs.pingidentity.com/auth-node-ref/latest/config-provider.html)

* [Email Suspend node](https://docs.pingidentity.com/auth-node-ref/latest/email-suspend.html)

* [Email Template node](https://docs.pingidentity.com/auth-node-ref/latest/email-template.html)

* [Failure URL node](https://docs.pingidentity.com/auth-node-ref/latest/failure-url.html)

* [Flow Control node](https://docs.pingidentity.com/auth-node-ref/latest/flow-control.html)

* [Get Session Data node](https://docs.pingidentity.com/auth-node-ref/latest/get-session-data.html)

* [Inner Tree Evaluator node](https://docs.pingidentity.com/auth-node-ref/latest/inner-tree-evaluator.html)

* [JWT Password Replay node](https://docs.pingidentity.com/auth-node-ref/latest/jwt-password-replay.html)

* [Message node](https://docs.pingidentity.com/auth-node-ref/latest/message.html)

* [JWT Password Replay node](https://docs.pingidentity.com/auth-node-ref/latest/jwt-password-replay.html)

* [Meter node](https://docs.pingidentity.com/auth-node-ref/latest/meter.html)

* [Page node](https://docs.pingidentity.com/auth-node-ref/latest/page.html)

* [Polling Wait node](https://docs.pingidentity.com/auth-node-ref/latest/polling-wait.html)

* [Query Parameter node](https://docs.pingidentity.com/auth-node-ref/latest/query-parameter.html)

* [Register Logout Webhook node](https://docs.pingidentity.com/auth-node-ref/latest/register-logout-webhook.html)

* [Remove Session Properties node](https://docs.pingidentity.com/auth-node-ref/latest/remove-session-properties.html)

* [Request Header node](https://docs.pingidentity.com/auth-node-ref/latest/request-header.html)

* [Retry Limit Decision node](https://docs.pingidentity.com/auth-node-ref/latest/retry-limit-decision.html)

* [Scripted Decision node](https://docs.pingidentity.com/auth-node-ref/latest/scripted-decision.html)

* [Set Error Details node](https://docs.pingidentity.com/auth-node-ref/latest/set-error-details.html)

* [Set Failure Details node](https://docs.pingidentity.com/auth-node-ref/latest/set-failure-details.html)

* [Set Logout Details node](https://docs.pingidentity.com/auth-node-ref/latest/set-logout-details.html)

* [Set Session Properties node](https://docs.pingidentity.com/auth-node-ref/latest/set-session-properties.html)

* [Set State node](https://docs.pingidentity.com/auth-node-ref/latest/set-state.html)

* [Set Success Details node](https://docs.pingidentity.com/auth-node-ref/latest/set-success-details.html)

* [State Metadata node](https://docs.pingidentity.com/auth-node-ref/latest/state-metadata.html)

* [Success URL node](https://docs.pingidentity.com/auth-node-ref/latest/success-url.html)

* [Timer Start node](https://docs.pingidentity.com/auth-node-ref/latest/timer-start.html)

* [Timer Stop node](https://docs.pingidentity.com/auth-node-ref/latest/timer-stop.html)

* [Update Journey Timeout node](https://docs.pingidentity.com/auth-node-ref/latest/update-journey-timeout.html)

## Uncategorized nodes

* [App Policy Decision node](https://docs.pingidentity.com/auth-node-ref/latest/app-policy-decision.html)

* [Identity Assertion node](https://docs.pingidentity.com/auth-node-ref/latest/identity-assertion-node.html)

* [Policy Decision node](https://docs.pingidentity.com/auth-node-ref/latest/policy-decision.html)

* [RADIUS Challenge Collector node](https://docs.pingidentity.com/auth-node-ref/latest/radius-challenge-collector.html)

* [RADIUS Decision node](https://docs.pingidentity.com/auth-node-ref/latest/radius-decision.html)

* [SpyCloud node](https://docs.pingidentity.com/auth-node-ref/latest/cloud/spycloud-auth.html)

* [RADIUS Challenge Collector node](https://docs.pingidentity.com/auth-node-ref/latest/radius-challenge-collector.html)

* [RADIUS Decision node](https://docs.pingidentity.com/auth-node-ref/latest/radius-decision.html)

## Marketplace nodes

* [PingOne service](https://docs.pingidentity.com/auth-node-ref/latest/pingone/pingone-service.html)

  * [PingOne node](https://docs.pingidentity.com/auth-node-ref/latest/pingone/pingone.html)

  * [PingOne Authorize node](https://docs.pingidentity.com/auth-node-ref/latest/pingone/pingone-authorize.html)

  * [PingOne Credentials nodes](https://docs.pingidentity.com/auth-node-ref/latest/pingone/pingone-cred-overview.html)

  * [PingOne Credentials Delete Wallet node](https://docs.pingidentity.com/auth-node-ref/latest/pingone/pingone-cred-delete-wallet.html)

  * [PingOne Credentials Find Wallets node](https://docs.pingidentity.com/auth-node-ref/latest/pingone/pingone-cred-find-wallet.html)

  * [PingOne Credentials Issue node](https://docs.pingidentity.com/auth-node-ref/latest/pingone/pingone-cred-issue.html)

  * [PingOne Credentials Pair Wallet node](https://docs.pingidentity.com/auth-node-ref/latest/pingone/pingone-cred-pair-wallet.html)

  * [PingOne Credentials Revoke node](https://docs.pingidentity.com/auth-node-ref/latest/pingone/pingone-cred-revoke.html)

  * [PingOne Credentials Update node](https://docs.pingidentity.com/auth-node-ref/latest/pingone/pingone-cred-update.html)

  * [PingOne Credentials Verification node](https://docs.pingidentity.com/auth-node-ref/latest/pingone/pingone-cred-verify.html)

  * [PingOne DaVinci API node](https://docs.pingidentity.com/auth-node-ref/latest/pingone/pingone-davinci.html)

* [PingOne Verify service](https://docs.pingidentity.com/auth-node-ref/latest/pingone/pingone-verify-service.html)

  * [PingOne Verify Authentication node](https://docs.pingidentity.com/auth-node-ref/latest/pingone/pingone-verify-authn.html)

  * [PingOne Verify Proofing node](https://docs.pingidentity.com/auth-node-ref/latest/pingone/pingone-verify-proof.html)

---

---
title: Journey solutions
description: Access prebuilt solution journeys from the Ping Identity Marketplace for common use cases like financial services and threat detection
component: pingoneaic
page_id: pingoneaic:journeys:solution-journeys
canonical_url: https://docs.pingidentity.com/pingoneaic/journeys/solution-journeys.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  financial_services: Financial services
  money_transfer: Money transfer
  threat_detection_with_pingone_protect: Threat detection with PingOne Protect
  sign_on_login_with_self_service: Sign on (login) with self-service
---

# Journey solutions

The [Ping Identity Marketplace](https://marketplace.pingone.com/) includes prebuilt sample journeys for PingOne Advanced Identity Cloud, all certified by Ping Identity. These journeys provide a starting point for common identity use cases, helping you accelerate journey development. You can download and use them as templates to create your own user journeys.

## Financial services

Give end users the tools to make payments and transfers, as well as manage account and privacy settings, while providing secure and adaptive digital banking.

* [Financial services journey](solution-financial-services-journey.html)

## Money transfer

Secure high-value money transfers by evaluating the risk of each transfer in real time. The journey can step up security when needed, preventing fraud while maintaining a smooth user experience.

* [Money transfer journey](solution-money-transfer-journey.html)

## Threat detection with PingOne Protect

Incorporate threat detection into an Advanced Identity Cloud journey. This journey uses PingOne Protect to analyze user behavior and location, prompting for step-up authentication or blocking access when high-risk activity is detected.

* [Threat detection with PingOne Protect journey](solution-threat-detection-journey.html)

## Sign on (login) with self-service

Incorporate social sign-on and progressive profiling into an Advanced Identity Cloud journey. This journey demonstrates how to incorporate social sign-on, self-service registration, and progressive profiling to gather user information over time.

* [Sign on (login) with self-service](solution-login-with-self-service-journey.html)

---

---
title: Journeys
description: Create authentication flows with journeys using pre-configured templates, custom nodes, and a drag-and-drop editor to customize end-user experiences
component: pingoneaic
page_id: pingoneaic:journeys:journeys
canonical_url: https://docs.pingidentity.com/pingoneaic/journeys/journeys.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Authentication", "Features", "Journeys", "Realms", "Self-Service"]
page_aliases: ["realms:journeys.adoc", "pingoneaic::journeys.adoc", "release-notes:rapid-channel/activate-or-deactivate-journeys.adoc"]
section_ids:
  authentication-templates: Authentication templates
  login: Login
  device-profiling: Device profiling
  user_self_service_templates: User self-service templates
  registration: Registration
  progressive-profile: Progressive profile
  update-password: Update password
  reset-password: Reset password
  forgotten-username: Forgotten username
  custom-journey: Custom journeys
  default-enduser-journey: Default journey
  deactivate-journeys: Deactivate journeys
  duplicate-journeys: Duplicate journeys
  export-journeys: Export journeys
  import-journeys: Import journeys
  annotate-journeys: Annotate journeys
  comments: Comments
  sticky_notes: Sticky notes
  delete-journeys: Delete journeys
  more-information-journeys: More information
---

# Journeys

PingOne Advanced Identity Cloud comes with pre-configured end-user *journeys*. A journey is an end-to-end workflow invoked by an end user or device. Advanced Identity Cloud provides templates for common end-user journeys; for example, account registration and sign-in.

Journeys are made up of *nodes*, which define actions taken during authentication. Each node performs a single task during authentication, for example, collecting a username or making a simple decision based on a cookie.

The following table describes how you can configure journeys to customize the authentication experience for end users.

| Task                                                                | Resources                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| ------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Modify the layout and appearance of journeys.                       | Use the [Hosted pages](../end-user/hosted-pages.html).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Modify the journey templates.                                       | * Use the [Login authentication template](#login) to configure sign-in journeys.

* Use a [self-service template](#user_self_service_templates) to let end users manage their accounts or resolve simple password issues without having to engage a tenant administrator.                                                                                                                                                                                                                                                                                                                                                        |
| Create a custom journey.                                            | - Start with a blank canvas when you want to build a [custom journey](#custom-journey), and drag and drop nodes from the nodes list.

- Create a [custom node](node-designer.html) if existing nodes don't meet your business needs.                                                                                                                                                                                                                                                                                                                                                                                             |
| Set a default journey.                                              | Configure Advanced Identity Cloud to display a [default journey](#default-enduser-journey) to end users.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Create journeys based on device context.                            | Use the Ping SDKs to [configure device profiling authentication](../solution-configure-device-profiling.html).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Customize the outcome of an authentication journey with JavaScript. | Use the [auth scripting editor](../developer-docs/scripting-auth.html#manage-auth-scripts) to create and manage scripts that run during the course of the authentication journey. You can create and include script types such as the following:- [Scripted Decision node](https://docs.pingidentity.com/auth-node-ref/latest/scripted-decision.html)

- [OIDC claims](../am-oauth2/plugins-user-info-claims.html)

- [Social Provider Handler node](https://docs.pingidentity.com/auth-node-ref/latest/social-provider-handler.html)Learn more in [auth script types](../developer-docs/scripting-auth.html#auth_script_types). |
| Configure an application journey                                    | To customize the sign-on experience for a SAML 2.0 or OIDC application, you can assign it a specific authentication journey. All users who sign on to the application must then authenticate using that journey.Learn more in [Application journeys](../app-management/application-journeys.html).                                                                                                                                                                                                                                                                                                                               |
| Always run journeys                                                 | When you create a journey, you have the option to configure the journey to always run.This setting lets you enforce journeys to always run regardless of any existing user sessions or whether the journey is initiated over REST or by redirect.Enable this option when you create [custom journeys](#custom-journey).                                                                                                                                                                                                                                                                                                          |
| Evaluate application authorization within a journey.                | For OIDC and SAML 2.0 applications, you can use the [App Policy Decision node](https://docs.pingidentity.com/auth-node-ref/latest/app-policy-decision.html) to evaluate the application's access policy during authentication.Find an example use case in [Authorize application access in journeys](../use-cases/use-case-app-authz-journeys.html).                                                                                                                                                                                                                                                                             |

## Authentication templates

### Login

Create a basic Login journey for end users to authenticate and sign in to an app or service with a username and password.

**Video (Video)**

<\_images/journey-login.mp4>

1. In the Advanced Identity Cloud admin console, go to Journeys > Journeys > Login.

2. Hover over the journey schematic, and click Edit.

3. Enter information for each node in the journey:

   * [Page node](https://docs.pingidentity.com/auth-node-ref/latest/page.html)

     * [Platform Username node](https://docs.pingidentity.com/auth-node-ref/latest/platform-username.html)

     * [Platform Password node](https://docs.pingidentity.com/auth-node-ref/latest/platform-password.html)

   * [Identity Store Decision node](https://docs.pingidentity.com/auth-node-ref/latest/cloud/identity-store-decision.html)

   * [Increment Login Count node](https://docs.pingidentity.com/auth-node-ref/latest/increment-login-count.html)

   * [Inner Tree Evaluator node](https://docs.pingidentity.com/auth-node-ref/latest/inner-tree-evaluator.html)

   * [Retry Limit Decision node](https://docs.pingidentity.com/auth-node-ref/latest/retry-limit-decision.html)

   * [Account Lockout node](https://docs.pingidentity.com/auth-node-ref/latest/account-lockout.html)

   Learn about available nodes in [Journey nodes](auth-nodes.html) or how to create your own node in [custom nodes](node-designer.html).

4. To test the journey, copy the Preview URL, and paste the URL into a browser using incognito mode.

5. When you're satisfied with your journey, click Save.

Learn more about the Login journey in [Login with self-service](../self-service/login.html).

|   |                                                                                                                                                                                                                                                                                                                                                                                                                               |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | If you implement account lockout using the [Account Lockout node](https://docs.pingidentity.com/auth-node-ref/latest/account-lockout.html), it creates a persistent lockout on user accounts. User accounts can be unlocked by a tenant administrator.Advanced Identity Cloud also supports configurable persistent and duration account lockout. Learn more in [Account lockout](../am-authentication/account-lockout.html). |

### Device profiling

Use the ForgeRock SDK to create journeys that let inanimate objects authenticate based on device context. Cell phones and smartwatches are examples of devices that have their own identities. Device context provides Advanced Identity Cloud with information about how or where a device is used to authenticate.

For detailed instructions, learn more in [Configure device profiling authentication](../solution-configure-device-profiling.html).

## User self-service templates

### Registration

Create a registration journey to let end users create their own account for an app or service.

**Video (Video)**

<\_images/journey-register.mp4>

1. In the Advanced Identity Cloud admin console, go to Journeys > Journeys > Registration.

2. Hover over the journey schematic, and click Edit.

3. Enter information for each node in the journey:

   * [Page node](https://docs.pingidentity.com/auth-node-ref/latest/page.html)

     * [Platform Username node](https://docs.pingidentity.com/auth-node-ref/latest/platform-username.html)

   * [Attribute Collector node](https://docs.pingidentity.com/auth-node-ref/latest/attribute-collector.html)

   * [Platform Password node](https://docs.pingidentity.com/auth-node-ref/latest/platform-password.html)

   * [KBA Definition node](https://docs.pingidentity.com/auth-node-ref/latest/kba-definition.html)

   * [Create Object node](https://docs.pingidentity.com/auth-node-ref/latest/create-object.html)

   Learn about all available nodes in [Journey nodes](auth-nodes.html).

4. To test the journey, copy the Preview URL, and paste the URL into a browser using incognito mode.

5. When you're satisfied with your journey, click Save.

Learn more about the Registration journey in [User self-registration](../self-service/self-registration.html).

### Progressive profile

Create a Progressive Profile journey to trigger a conditional event in the journey.

The default journey triggers a reminder to set preferences for receiving news and special offers. The reminder is displayed only if the end user logs in three times without selecting preferences. If the end user makes no selection, the reminder expires and is not displayed again. If the end user selects one or more options, the preferences get set in the end user's profile.

**Video (Video)**

<\_images/journey-progressive-login.mp4>

1. In the Advanced Identity Cloud admin console, go to Journeys > Journeys > Progressive Profile.

2. Hover over the journey schematic, and click Edit.

3. Enter information for each node in the journey:

   * [Login Count Decision node](https://docs.pingidentity.com/auth-node-ref/latest/login-count-decision.html)

   * [Query Filter Decision node](https://docs.pingidentity.com/auth-node-ref/latest/query-filter-decision.html)

   * [Page node](https://docs.pingidentity.com/auth-node-ref/latest/page.html)

     * [Attribute Collector node](https://docs.pingidentity.com/auth-node-ref/latest/attribute-collector.html)

   * [Patch Object node](https://docs.pingidentity.com/auth-node-ref/latest/patch-object.html)

   Learn about all available nodes in [Journey nodes](auth-nodes.html).

4. To test the journey, copy the Preview URL, and paste the URL into a browser using incognito mode.

5. When you're satisfied with your journey, click Save.

Learn more about the Progressive Profile journey in [Progressive profile](../self-service/progressive-profile.html).

### Update password

Create an Update Password journey to let end users change their passwords. End users may be required to change passwords at regular intervals or if a password is compromised.

1. In the Advanced Identity Cloud admin console, go to Journeys > Journeys > Update Password.

2. Hover over the journey schematic, and click Edit.

3. Enter information for each node in the journey:

   * [Get Session Data node](https://docs.pingidentity.com/auth-node-ref/latest/get-session-data.html)

   * [Attribute Present Decision node](https://docs.pingidentity.com/auth-node-ref/latest/attribute-present-decision.html)

   * [Page node](https://docs.pingidentity.com/auth-node-ref/latest/page.html)

     * [Platform Password node](https://docs.pingidentity.com/auth-node-ref/latest/platform-password.html)

   * [Data Store Decision node](https://docs.pingidentity.com/auth-node-ref/latest/data-store-decision.html)

   * [Email Suspend node](https://docs.pingidentity.com/auth-node-ref/latest/email-suspend.html)

   * [Patch Object node](https://docs.pingidentity.com/auth-node-ref/latest/patch-object.html)

   Learn about all available nodes in [Journey nodes](auth-nodes.html).

4. To test the journey, copy the Preview URL, and paste the URL into a browser using incognito mode.

5. When you're satisfied with your journey, click Save.

Learn more about the Update Password journey in [Password updates](../self-service/update-password.html).

### Reset password

Create a Reset Password journey to let end users change their existing passwords. End users typically reset their passwords when they've forgotten the password they set.

**Video (Video)**

<\_images/journey-reset-password.mp4>

1. In the Advanced Identity Cloud admin console, go to Journeys > Journeys > Reset Password.

2. Hover over the journey schematic, and click Edit.

3. Enter information for each node in the journey:

   * [Page node](https://docs.pingidentity.com/auth-node-ref/latest/page.html)

     * [Attribute Collector node](https://docs.pingidentity.com/auth-node-ref/latest/attribute-collector.html)

   * [Identify Existing User node](https://docs.pingidentity.com/auth-node-ref/latest/identify-existing-user.html)

   * [Email Suspend node](https://docs.pingidentity.com/auth-node-ref/latest/email-suspend.html)

   * [Page node](https://docs.pingidentity.com/auth-node-ref/latest/page.html)

     * [Platform Password node](https://docs.pingidentity.com/auth-node-ref/latest/platform-password.html)

   * [Patch Object node](https://docs.pingidentity.com/auth-node-ref/latest/patch-object.html)

   Learn about all available nodes in [Journey nodes](auth-nodes.html).

4. To test the journey, copy the Preview URL, and paste the URL into a browser using incognito mode.

5. When you're satisfied with your journey, click Save.

Learn more about the Reset Password journey in [Password reset](../self-service/password-reset.html).

### Forgotten username

Create a Forgotten Username journey to let end users retrieve their username from their user account data.

**Video (Video)**

<\_images/journey-forgot-username.mp4>

1. In the Advanced Identity Cloud admin console, go to Journeys > Journeys > Forgotten Username.

2. Hover over the journey schematic, and click Edit.

3. Enter information for each node in the journey:

   * [Page node](https://docs.pingidentity.com/auth-node-ref/latest/page.html)

     * [Attribute Collector node](https://docs.pingidentity.com/auth-node-ref/latest/attribute-collector.html)

   * [Identify Existing User node](https://docs.pingidentity.com/auth-node-ref/latest/identify-existing-user.html)

   * [Email Suspend node](https://docs.pingidentity.com/auth-node-ref/latest/email-suspend.html)

   * [Inner Tree Evaluator node](https://docs.pingidentity.com/auth-node-ref/latest/inner-tree-evaluator.html)

   Learn about all available nodes in [Journey nodes](auth-nodes.html).

4. To test the journey, copy the Preview URL, and paste the URL into a browser using incognito mode.

5. When you're satisfied with your journey, click Save.

Learn more about the Forgotten Username journey in [Username recovery](../self-service/username-recovery.html).

## Custom journeys

Create a custom journey when none of the ready-to-use templates suits your needs.

1. In the Advanced Identity Cloud admin console, click Journeys > Journeys.

2. Click [icon: add, set=material, size=inline] Add Journey, select Start from scratch, and then click Next.

3. Enter journey details:

   * Name: Name to display in the Journeys list.

   * Identity Object: Identifier for the user or device to authenticate.

   * (Optional) Description: Summarize end user interaction.

   * (Optional) Tags: For organizing journeys to make them easier to find.

4. (Optional) Enable journey options:

   | Field                                                   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
   | ------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | Default journey for end users                           | Sets this journey as the default.                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
   | Override theme                                          | Specify a custom theme for this journey.                                                                                                                                                                                                                                                                                                                                                                                                                                           |
   | Override authenticated session timeout                  | Configure authenticated session timeouts for this journey.Learn more in [Configure authenticated session timeouts in a journey](../am-authentication/configure-authentication-trees.html#configure-auth-session-timeouts-tree).                                                                                                                                                                                                                                                    |
   | Run journey for all users regardless of current session | Configure the journey to execute regardless of any existing user sessions or whether the journey is initiated over REST or by redirect. Always running a journey doesn't necessarily require the user to authenticate every time.&#xA;&#xA;You can't configure a journey to always run when it's set as the default journey.Learn more in [Configure an authentication journey to always run](../am-authentication/configure-authentication-trees.html#enable-journey-completion). |
   | Inner Journey                                           | Prevent the journey from being used outside of its parent journey.Learn more in [Disable direct access through a child journey](../am-authentication/configure-authentication-trees.html#disable-child-journey).                                                                                                                                                                                                                                                                   |
   | Transactional Only                                      | Configure the journey as a transactional authentication journey. A transactional authentication journey only runs when Advanced Identity Cloud starts a transaction.Learn more in [Configure a transactional authentication journey](../am-authentication/configure-authentication-trees.html#configure-transactional-auth-journey).                                                                                                                                               |
   | No Session                                              | Configure the journey as a no session journey. A no session journey doesn't result in an authenticated session when it successfully completes.Learn more in [Configure a no session journey](../am-authentication/configure-authentication-trees.html#configure-nosession-tree).                                                                                                                                                                                                   |

5. Click Save to create the journey.

6. Use the journey editor to create your custom journey.\
   Drag nodes from the palette and arrange them on the blank canvas.

7. Provide information for each node, and connect nodes.

   Learn about all available nodes in [Journey nodes](auth-nodes.html).

8. To test the journey, copy the Preview URL, and paste the URL into a browser using incognito mode.

9. When you're satisfied with your journey, click Save.

## Default journey

Advanced Identity Cloud displays the default journey to end users when they access a default webpage URL. For example, application webpages commonly display a sign-in link. When the end user clicks the link, the Login journey is invoked by default.

Set a default end-user journey as follows:

* Set a new journey as the default:

  * In the Advanced Identity Cloud admin console, click Journeys > Journeys.

  * Click [icon: add, set=material, size=inline] Add Journey, select Start from scratch, and then click Next.

  * In the New Journey modal, enable the option Default journey for end users.

* Set an existing journey as the default:

  * In the Advanced Identity Cloud admin console, click Journeys > Journeys to view the list of journeys.

  * Select a journey, and click [icon: ellipsis-h, set=fa]and Set as default.

## Deactivate journeys

Deactivate a journey to prevent end users using it to authenticate. If you deactivate it, you can reactivate it at any time.

For example, if you are building a new journey in your development environment and you need to run a promotion, you can deactivate the journey prior to the promotion so that there's no risk of the journey being discovered and used by end users in your upper environments and potentially allowing insecure access. You can activate the journey in your development environment again after a promotion.

Ping Identity recommends you deactivate any default journeys not in use. Learn more in [Deactivate unused or insecure journeys](../planning/plan-security.html#deactivate-unused-or-insecure-journeys).

1. In the Advanced Identity Cloud admin console, go to Journeys > Journeys to view the existing journeys list.

2. Find the journey.

3. Click its More ([icon: ellipsis-h, set=fa]) menu:

   * To deactivate the journey, choose Deactivate, then in the Deactivate Journey dialog, click Deactivate.

   * To activate the journey, choose Activate.

You can also deactivate and activate a journey using the More ([icon: ellipsis-h, set=fa]) menu in the journey editor.

## Duplicate journeys

Duplicate a journey to preserve a template for future use. For example, if you are testing a journey, start with a duplicate. Give the duplicate journey a unique name.

Create a duplicate journey in the following ways:

* Click Journeys > Journeys to view the existing journeys list. Find the template name. Then, click its More ([icon: ellipsis-h, set=fa]) menu, and choose Duplicate.

* In the Journey editor, click More ([icon: ellipsis-h, set=fa]), and choose Duplicate.

## Export journeys

You can export journeys, including all dependencies like nodes, inner journeys, and scripts of any type apart from [library](../am-scripting/library-scripts.html) scripts.

Use this feature to export journeys from one environment, such as a development environment, to another.

1. In the Advanced Identity Cloud admin console, go to Journeys > Journeys.

2. Check the checkbox beside one or more journeys.

3. Click Export.

4. View the information on the Export Journeys page.

5. Click Export.

## Import journeys

You can import journeys, including all dependencies such as nodes, inner journeys, and scripts, and scripts of any type apart from [library](../am-scripting/library-scripts.html) scripts.

Use this feature to import a journey from one environment, such as a development environment, to another.

1. In the Advanced Identity Cloud admin console, click Journeys > Journeys.

2. Click [icon: add, set=material, size=inline] Add Journey, select Import, and then click Next.

3. Download or skip back up:

   * Download a backup of your existing journeys so that you can restore them in case of error or unexpected behavior during or after import:

     1. To view the backup summary, click Show backup summary.

     2. Click Download Backup.

   * Skip the download:

     1. Click Skip Backup.

     2. In the dialog box, click Skip Backup again.

4. Configure the import:

   1. On the Import Journeys page, browse to and select a JSON file that contains the journey's configurations to import.

   2. Select the identity object that the journey authenticates.

   3. In the Conflict Resolution section, choose how the system resolves import conflicts:

      * Overwrite all conflicts (default)

      * Manually pick conflict resolution

   4. Click Next.

   5. Review the information on the Import Summary page.

   6. Click Start Import.

   7. On the Import Complete page, click Done.

## Annotate journeys

You can annotate a journey using comments and sticky notes. Annotations help you share information when multiple tenant administrators work on the same journey.

### Comments

Use comments to have a conversation with other tenant administrators about a journey. Comments are associated with specific nodes in a journey and only one comment can be added per node. You can reply to comments multiple times and delete them if necessary. Comments and replies are visible to all tenant administrators. Comments and replies are saved automatically.

1. In the Advanced Identity Cloud admin console, go to Journeys, and click a journey name to open it in the journey editor.

2. To add a comment:

   1. In the journey editor, click the Comment icon ([icon: chat_bubble_outline, set=material, size=inline]).

   2. In the journey schema, click the node to which you want to add a comment. A comment field displays with the placeholder text Add a comment.

   3. In the comment field, enter your comment, then click the arrow icon ([icon: arrow_upward, set=material, size=inline]). The comment is added to the node. A *comment bubble* displays on the top right of the node to indicate that it has a comment. The comment bubble shows the initials of the tenant administrator who made the comment.

3. To set a color for a comment:

   1. In the journey schema, click a comment bubble on a node. This opens the comment pane.

   2. Click a colored circle at the top of the comment pane. This sets the color of the comment bubble, the comment, and any replies. Setting colors makes it easier to distinguish between multiple comment bubbles on the node.

4. To reply to a comment:

   1. In the journey schema, click a comment bubble on a node. This opens the comment pane.

   2. Click the field with the placeholder text Reply, enter your reply, then click the arrow icon ([icon: arrow_upward, set=material, size=inline]). You can reply to a comment multiple times, creating a thread of replies.

   3. (Optional) To delete a reply, click the ellipsis icon ([icon: more_horiz, set=material, size=inline]) beside it, then click Delete.

5. To delete a comment and all its replies:

   1. In the journey schema, click a comment bubble on a node. This opens the comment pane.

   2. Click the ellipsis icon ([icon: more_horiz, set=material, size=inline]) at the top of the comment pane, then click Delete.

### Sticky notes

Use sticky notes to add reminders or other information about a journey. Sticky notes aren't associated with specific nodes in a journey. Sticky notes are visible to all tenant administrators. Each tenant administrator can add multiple sticky notes. Sticky notes are saved automatically.

1. In the Advanced Identity Cloud admin console, go to Journeys, and click a journey name to open it in the journey editor.

2. To add a sticky note:

   1. In the journey editor, click the Add Sticky Note icon ([icon: sticky_note_2, set=material, size=inline]).

   2. In the journey schema, click anywhere outside a node. An empty sticky note displays and automatically takes focus.

   3. Enter your comment, then click anywhere outside the sticky note to save it.

3. To edit a sticky note:

   1. Click a sticky note to open it for editing. The sticky note automatically takes focus.

   2. Edit the text, then click anywhere outside the sticky note to save it.

4. To set a color for a sticky note:

   1. Click a sticky note to open it for editing.

   2. Click a colored circle at the top of the sticky note.

5. To delete a sticky note:

   1. Click a sticky note to open it for editing.

   2. Click the ellipsis icon ([icon: more_horiz, set=material, size=inline]) at the top of the sticky note, then click Delete.

## Delete journeys

Deleting a journey is a permanent operation. You won't be able to retrieve it after it's deleted.

Delete a journey in the following ways:

* In the Advanced Identity Cloud admin console, go to Journeys > Journeys, and check the checkbox beside one or more journeys. Click Delete Journeys.

* In the Journey editor, click More ([icon: ellipsis-h, set=fa]), and choose Delete.

|   |                                                                                                                                                                                                               |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | You can't delete a journey if it's referenced by a [SAML 2.0 app](../am-saml2/configure-providers.html#samlapp-journey) or an [OAuth 2.0 client](../am-oauth2/oauth2-register-client.html#oauth2app-journey). |

## More information

* [Nodes and journeys](../am-authentication/auth-nodes-and-journeys.html)

* [Node reference](auth-nodes.html)

---

---
title: Marketplace journey nodes
description: Extend Advanced Identity Cloud capabilities using third-party marketplace integrations including identity verification, MFA, and fraud detection
component: pingoneaic
page_id: pingoneaic:journeys:marketplace
canonical_url: https://docs.pingidentity.com/pingoneaic/journeys/marketplace.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Getting started", "Deployment", "Planning", "Journeys"]
page_aliases: ["product-information:marketplace.adoc"]
---

# Marketplace journey nodes

The [Ping Identity Marketplace](https://marketplace.pingone.com/) lets you quickly and easily extend the capabilities of the PingOne Advanced Identity Cloud by integrating third party services into your applications or user journeys. Advanced Identity Cloud provides a subset of Marketplace integrations out of the box in your environment.

Your Advanced Identity Cloud tenant provides the following Marketplace nodes. You can find them under the Marketplace header in the Advanced Identity Cloud admin console's drag-and-drop user journey editor.

| Integration                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Use case                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [BioCatch Session node](https://docs.pingidentity.com/auth-node-ref/latest/cloud/biocatch-session.html) [BioCatch Session Collector node](https://docs.pingidentity.com/auth-node-ref/latest/cloud/biocatch-session-collector.html) [BioCatch Session Profiler node](https://docs.pingidentity.com/auth-node-ref/latest/cloud/biocatch-session-profiler.html)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Integrate with [BioCatch](https://www.biocatch.com/) scoring for identity proofing, continuous authentication, and fraud protection. The BioCatch platform develops behavioral biometric profiles of online users to recognize a wide range of human and non-human cybersecurity threats including malware, remote access trojans (RATs), and robotic activity (bots).                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [Duo node (deprecated)](https://docs.pingidentity.com/auth-node-ref/latest/cloud/duo.html) [Duo Universal Prompt node](https://docs.pingidentity.com/auth-node-ref/latest/cloud/duo-univ-prompt.html)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Use Duo's solution for adaptive authentication, bring your own device (BYOD) security, cloud security, endpoint security, mobile security, and two-factor authentication.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [Fingerprint nodes](https://docs.pingidentity.com/auth-node-ref/latest/cloud/fingerprint.html)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Integrate with [fingerprint.com](https://dev.fingerprint.com/docs/quick-start-guide) to reduce fraud and improve customer experience.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [Gateway Communication overview](https://docs.pingidentity.com/auth-node-ref/latest/cloud/gateway-communication.html)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Enable a secure communication channel for Advanced Identity Cloud authentication journeys to communicate directly with the [PingGateway](../realms/gateways-agents.html#identity-gateway).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [HTTP Client node](https://docs.pingidentity.com/auth-node-ref/latest/cloud/http-client.html)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | The HTTP Client node lets you make HTTP(S) requests to APIs and services external to Advanced Identity Cloud from within a journey.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [IdentityX Auth Request Decision node](https://docs.pingidentity.com/auth-node-ref/latest/cloud/identityx-auth-request-decision.html) [IdentityX Auth Request Initiator node](https://docs.pingidentity.com/auth-node-ref/latest/cloud/identityx-auth-request-initiator.html) [IdentityX Check Enrollment Status node](https://docs.pingidentity.com/auth-node-ref/latest/cloud/identityx-check-enrollment-status.html) [IdentityX Mobile Auth Request node](https://docs.pingidentity.com/auth-node-ref/latest/cloud/identityx-mobile-auth-request.html) [IdentityX Mobile Auth Request Validate node](https://docs.pingidentity.com/auth-node-ref/latest/cloud/identityx-mobile-auth-request-validate.html) [IdentityX Sponsor User node](https://docs.pingidentity.com/auth-node-ref/latest/cloud/identityx-sponsor-user.html)                                                                                                                                                                                          | Integrate with the [Daon IdentityX platform](https://www.daon.com/technology/identityx-platform/) for MFA with mobile authentication or out-of-band authentication using a separate, secure channel.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [iProov Authentication node](https://docs.pingidentity.com/auth-node-ref/latest/cloud/iproov.html)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Integrate Advanced Identity Cloud authentication journeys with the Genuine Presence Assurance and Liveness Assurance products from [iProov](https://www.iproov.com/).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [Jumio identity verification](https://docs.pingidentity.com/auth-node-ref/latest/cloud/jumio-id-verify.html) [Jumio decision node](https://docs.pingidentity.com/auth-node-ref/latest/cloud/jumio-decision.html) [Jumio initiate node](https://docs.pingidentity.com/auth-node-ref/latest/cloud/jumio-initiate.html)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Integrate with Jumio identity verification to let you capture and submit your government-issued ID documents easily and securely.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [LexisNexis One-Time Passcode (OTP)](https://docs.pingidentity.com/auth-node-ref/latest/cloud/lexis-otp.html) [LexisNexis OTP Sender node](https://docs.pingidentity.com/auth-node-ref/latest/cloud/lexis-otp-sender.html) [LexisNexis OTP Collector node](https://docs.pingidentity.com/auth-node-ref/latest/cloud/lexis-otp-collector.html) [LexisNexis OTP Decision node](https://docs.pingidentity.com/auth-node-ref/latest/cloud/lexis-otp-decision.html)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Integrate with LexisNexis One Time Password (OTP) to use an out-of-band identity proofing method that provides stronger authentication for high-risk, high-value transactions.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [Microsoft Intune node](https://docs.pingidentity.com/auth-node-ref/latest/cloud/microsoft-intune-about.html)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Integrate with [Microsoft Intune](https://learn.microsoft.com/en-us/mem/intune/fundamentals/what-is-intune) to let you control features and settings on Android, Android Enterprise, iOS/iPadOS, macOS, and Windows 10/11 devices in your organization.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [OneSpan](https://docs.pingidentity.com/auth-node-ref/latest/cloud/onespan-about.html) [OneSpan nodes](https://docs.pingidentity.com/auth-node-ref/latest/cloud/onespan-nodes.html) [OneSpan Sample journeys](https://docs.pingidentity.com/auth-node-ref/latest/cloud/onespan-sample.html)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Integrate with [OneSpan Intelligent Adaptive Authentication (IAA)](https://www.onespan.com/products/intelligent-adaptive-authentication) to help reduce fraud, improve customer experience, and meet compliance requirements.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [Onfido Check node](https://docs.pingidentity.com/auth-node-ref/latest/cloud/onfido-check.html) [Onfido Registration node](https://docs.pingidentity.com/auth-node-ref/latest/cloud/onfido-registration.html)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Integrate an Onfido check for identity verification, matching a user with their official identification documents.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [PingOne DaVinci API node](https://docs.pingidentity.com/auth-node-ref/latest/pingone/pingone-davinci.html)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | The PingOne DaVinci API node executes an API call to PingOne DaVinci to launch a specific DaVinci flow.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [PingOne Authorize node](https://docs.pingidentity.com/auth-node-ref/latest/pingone/pingone-authorize.html)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | The PingOne Authorize node sends a decision request to a specified decision endpoint in your PingOne Authorize environment.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [PingOne Credentials nodes](https://docs.pingidentity.com/auth-node-ref/latest/pingone/pingone-cred-overview.html) [PingOne Credentials Pair Wallet node](https://docs.pingidentity.com/auth-node-ref/latest/pingone/pingone-cred-pair-wallet.html) [PingOne Credentials Find Wallets node](https://docs.pingidentity.com/auth-node-ref/latest/pingone/pingone-cred-find-wallet.html) [PingOne Credentials Delete Wallet node](https://docs.pingidentity.com/auth-node-ref/latest/pingone/pingone-cred-delete-wallet.html) [PingOne Credentials Issue node](https://docs.pingidentity.com/auth-node-ref/latest/pingone/pingone-cred-issue.html) [PingOne Credentials Update node](https://docs.pingidentity.com/auth-node-ref/latest/pingone/pingone-cred-update.html) [PingOne Credentials Revoke node](https://docs.pingidentity.com/auth-node-ref/latest/pingone/pingone-cred-revoke.html) [PingOne Credentials Verification node](https://docs.pingidentity.com/auth-node-ref/latest/pingone/pingone-cred-verify.html) | The PingOne Credentials nodes use the PingOne Credentials service to implement digital wallet pairing, credential management, and credential verification.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [PingOne Protect Initialization node](https://docs.pingidentity.com/auth-node-ref/latest/pingone/pingone-protect-initialize.html) [PingOne Protect Evaluation node](https://docs.pingidentity.com/auth-node-ref/latest/pingone/pingone-protect-evaluation.html) [PingOne Protect Result node](https://docs.pingidentity.com/auth-node-ref/latest/pingone/pingone-protect-result.html)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | PingOne Protect is a centralized identity threat protection service, securing your digital assets against online fraud attempts, such as account takeover and fraudulent new account registration.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [PingOne node (deprecated)](https://docs.pingidentity.com/auth-node-ref/latest/pingone/pingone.html) [PingOne Verify service (deprecated)](https://docs.pingidentity.com/auth-node-ref/latest/pingone/pingone-verify-service.html) [PingOne Verify Authentication node (deprecated)](https://docs.pingidentity.com/auth-node-ref/latest/pingone/pingone-verify-authn.html) [PingOne Verify Proofing node (deprecated)](https://docs.pingidentity.com/auth-node-ref/latest/pingone/pingone-verify-proof.html)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | *Deprecated*Depending on your use case, use the following nodes instead:- [PingOne Verify Evaluation node](https://docs.pingidentity.com/auth-node-ref/latest/pingone/pingone-verify-evaluation.html)

- [PingOne Verify Completion Decision node](https://docs.pingidentity.com/auth-node-ref/latest/pingone/pingone-verify-completion-decision.html)

- [PingOne Identity Match node](https://docs.pingidentity.com/auth-node-ref/latest/pingone/pingone-identity-match.html)

- [PingOne Create User node](https://docs.pingidentity.com/auth-node-ref/latest/pingone/pingone-create-user.html)

- [PingOne Delete User node](https://docs.pingidentity.com/auth-node-ref/latest/pingone/pingone-delete-user.html)

- [PingOne DaVinci node](https://docs.pingidentity.com/auth-node-ref/latest/pingone/pingone-davinci.html) |
| [RSA SecurID node (deprecated)](https://docs.pingidentity.com/auth-node-ref/latest/cloud/rsa-securid.html)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | *Deprecated*Use the [RSA SecurID](https://docs.pingidentity.com/auth-node-ref/latest/rsa-securid.html) node instead.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [Secret Double Octopus nodes](https://docs.pingidentity.com/auth-node-ref/latest/cloud/secret-double-octopus.html)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Integrate with [Secret Double Octopus (SDO)](https://doubleoctopus.com/solutions/passwordless-mfa/) to provide high-assurance, passwordless authentication system.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [SpyCloud Auth Node](https://docs.pingidentity.com/auth-node-ref/latest/cloud/spycloud-auth.html)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | Integrate with [SpyCloud](https://spycloud.com/) service with Advanced Identity Cloud to assess if a user's password is compromised.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [ThreatMetrix Authentication nodes](https://docs.pingidentity.com/auth-node-ref/latest/cloud/threat-metrix.html) [ThreatMetrix Profiler node](https://docs.pingidentity.com/auth-node-ref/latest/cloud/threat-metrix-profiler.html) [ThreatMetrix Session Query node](https://docs.pingidentity.com/auth-node-ref/latest/cloud/threat-metrix-session-query.html) [ThreatMetrix Review Status node](https://docs.pingidentity.com/auth-node-ref/latest/cloud/threat-metrix-review-status.html) [ThreatMetrix Reason Code node](https://docs.pingidentity.com/auth-node-ref/latest/cloud/threat-metrix-reason-code.html) [ThreatMetrix Update Review node](https://docs.pingidentity.com/auth-node-ref/latest/cloud/threat-metrix-update-review.html)                                                                                                                                                                                                                                                                        | Integrate [Lexis-Nexis ThreatMetrix](https://risk.lexisnexis.com/products/threatmetrix) decision tools and enable device intelligence and risk assessment in Advanced Identity Cloud.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [Twilio Identifier node](https://docs.pingidentity.com/auth-node-ref/latest/cloud/twilio-identifier.html) [Twilio Verify Collector Decision node](https://docs.pingidentity.com/auth-node-ref/latest/cloud/twilio-verify-collector-decision.html) [Twilio Verify Lookup node](https://docs.pingidentity.com/auth-node-ref/latest/cloud/twilio-verify-lookup.html) [Twilio Verify Sender node](https://docs.pingidentity.com/auth-node-ref/latest/cloud/twilio-verify-sender.html)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | Leverage Twilio for second factor authentication during new account or sign on scenarios.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |

|   |                                                                         |
| - | ----------------------------------------------------------------------- |
|   | Check this list periodically as we continue to expand our integrations. |

Find more information on developing and troubleshooting journeys in:

* [Journeys](journeys.html)

* [Debug end-user journeys](../end-user/debug-enduser-journeys.html)

* [Get audit and debug logs](../tenants/audit-debug-logs.html)

---

---
title: Money transfer journey
description: Implement a prebuilt money transfer journey providing secure financial transactions with dynamic context-aware multi-factor authentication
component: pingoneaic
page_id: pingoneaic:journeys:solution-money-transfer-journey
canonical_url: https://docs.pingidentity.com/pingoneaic/journeys/solution-money-transfer-journey.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Authentication", "Journeys"]
section_ids:
  about-money-transfer-journey: About the money transfer journey
  money-transfer-use-case: Example use case
  money-transfer-components: Journey components
  money-transfer-before-begin: Before you begin
  money-transfer-task1: "Task 1: Prepare your tenant environment"
  money-transfer-custom-attributes: Add custom attributes to the alpha_user managed object
  money-transfer-optional_set_an_esv_variable: (Optional) Set an ESV variable for PingOne Protect analysis
  money-transfer-create-email-templates: Create the email templates
  task_2_create_a_pingone_authorize_policy: "Task 2: Create a PingOne Authorize policy"
  define_the_amount_attribute: Define the amount attribute
  create_the_payment_check_policy: Create the payment check policy
  money-transfer-download-import-journey: "Task 3: Download and import the journey"
  download_the_journey: Download the journey
  import_the_journey: Import the journey
  configure-money-transfer-journey: "Task 4: Configure the journey components"
  configure-money-transfer-main-journey: Configure the money transfer main journey
  review-set-initialize-variables: Review and set the initialize variables
  configure-money-transfer-url: Configure the money transfer URL
  set-journey-for-all-users: Set the journey to run for all users regardless of current session
  configure-money-transfer-threat-detection-inner-journey: Configure the Threat Detection - Inner Journey
  configure-money-transfer-inner-journey: Configure the Money Transfer - Inner Journey
  configure-money-transfer-mfa-auth-inner-journey: Configure the MFA Authentication - Inner Journey
  money-transfer-validation: "Task 5: Validate the journey"
  money-transfer-validation-low-risk: Test a low-risk transfer
  money-transfer-validation-high-risk: Test a higher-risk transfer
  money-transfer-journey-best-practices: Best practices
---

# Money transfer journey

The Ping Identity Marketplace includes a prebuilt [money transfer journey](https://marketplace.pingone.com/item/money-transfer-aic-journey-template). The journey provides secure financial transactions by applying dynamic, context-aware multi-factor authentication (MFA). By evaluating the risk of each money transfer in real time, the journey can step up security when needed, preventing fraud while maintaining a smooth user experience.

The journey is intended as a template. Review and adapt it to meet your organization's specific security policies and business requirements before deploying to a production environment.

**Journey download**

| Journey name   | Version | Download                                                                                              |
| -------------- | ------- | ----------------------------------------------------------------------------------------------------- |
| Money transfer | 1.0     | [Download from Marketplace](https://marketplace.pingone.com/item/money-transfer-aic-journey-template) |

## About the money transfer journey

This solution uses a main journey and inner journeys to evaluate the risk level of a user's sign-on attempt. Authenticated users can make secure money transfers between their savings and checking accounts.

### Example use case

A bank wants to secure money transfer transactions and prevent fraud without creating unnecessary friction for customers. To do this, they want a journey that provides adaptive security by evaluating risk signals in real time across various end-user actions, from sign-on to financial transactions. The solution would allow routine, low-value money transfers from a known device to proceed seamlessly, while automatically triggering MFA for high-value transfers or suspicious activity to verify the user's identity.

### Journey components

The money transfer journey includes one main journey and four inner journeys.

| Journey                                                 | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Configuration required? |
| ------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------- |
| **Money Transfer - Main Journey**                       | Orchestrates a secure money transfer by managing user authentication, performing risk analysis, and stepping up security when necessary.> **Collapse: Show details**
>
> This journey starts by checking if the user has an active session. If not, it directs them through a sign-on process by calling the **Money Transfer SignOn - Inner Journey**. It then identifies the user and confirms their account is active.
>
> The journey then performs the following steps:
>
> * **Threat detection**: Calls the **Money Transfer - Threat Detection - Inner Journey** to evaluate the real-time risk of the sign-on attempt using PingOne Protect.
>
>   The threat detection journey sets the authentication level based on the detected risk level. A medium to high risk level increases the authentication level.
>
> * **Authentication step-up**: The **Auth Level Decision** node evaluates the user's current authentication level. A higher authentication level is interpreted as higher risk for subsequent steps, which triggers MFA.
>
>   Switching the True and False outputs of the Auth Level Decision node means a higher current authentication level is interpreted as lower risk, and MFA won't be triggered. This isn't recommended for this journey.
>
> * **Money transfer**: After all security checks are successfully passed, the journey proceeds to the core money transfer process by calling the **Money Transfer - Inner Journey**.
>
> * **Finalization**: The journey concludes by logging the success or failure of the PingOne Protect evaluation.  | Yes                     |
| **Money Transfer - Threat Detection - Inner Journey**   | Performs real-time threat detection using PingOne Protect to assess session risk.> **Collapse: Show details**
>
> Gathers behavioral data from the user's session and determines a risk level. Depending on the assessed risk, the journey takes different paths:
>
> * **Low risk**: The journey proceeds, but also checks for indicators such as a new device or other suspicious parameters.
>
> * **Medium to high risk**: Increases the required authentication level, asking for stronger user verification before continuing.
>
> * **Specific threats** (for example, bots or man-in-the-middle): Checks if the user's account is active. If it is, the account is disabled, and an alert email is sent to the user.
>
> * **Failure**: If any part of the risk evaluation fails, the journey logs the failure and terminates.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Yes                     |
| **Money Transfer - Inner Journey**                      | Manages the money transfer process for an authenticated user.> **Collapse: Show details**
>
> The journey starts by identifying the user. After successful identification, the user can proceed to enter the details of the money transfer.
>
> The journey validates the input using the [PingOne Authorize node](https://docs.pingidentity.com/auth-node-ref/latest/pingone/pingone-authorize.html) to assess the transaction risk.
>
> * If the transaction is permitted (low risk), the journey checks if the user has a sufficient balance, updates the balance, and displays a success message.
>
> * If the transaction requires approval (higher risk), an approval email is sent to the user. After the user approves the transfer through the email link, the journey proceeds as if it were a permitted transaction.
>
> * If the transaction is denied, the user is shown a transfer failed page.
>
> The journey includes paths to handle various errors, such as invalid input or insufficient balance, which typically redirect the user back to the transfer page to make corrections.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Yes                     |
| **Money Transfer - MFA Authentication - Inner Journey** | Orchestrates the MFA process. It prompts the user to select an MFA method (such as OTP, push, or WebAuthn) and handles the subsequent verification flow.> **Collapse: Show details**
>
> The journey starts by identifying an existing user and then prompts them to select an authentication method.
>
> The journey proceeds with one of the following MFA flows:
>
> * **Email**: Generates a one-time passcode (OTP) and sends it to the user's email address for verification.
>
> * **SMS / Voice**: Uses Twilio to send a verification code to the user's registered phone number through SMS or a voice call.
>
> * **FIDO2** (WebAuthn): Initiates authentication using a security key or biometrics.
>
> * **OATH**: Asks the user to enter a verification code from an authenticator app.
>
> * **Push**: Sends a push notification to a registered device for approval.
>
> * **Magic Link**: Emails a unique link that the user clicks to sign on.
>
> For most methods, if the user fails to authenticate, they're given a limited number of retry attempts before the journey fails. The journey also includes paths for users to authenticate using a recovery code if other methods are unavailable.                                                                                                                                                                                                                                                                                                                                                                      | Yes                     |
| **Money Transfer SignOn - Inner Journey**               | Manages the initial user sign-on, including credential validation, email verification, and security checks.> **Collapse: Show details**
>
> The journey performs the following checks:
>
> * **Threat analysis**: Determines if a threat analysis is required. If so, it initiates PingOne Protect for risk evaluation by calling the **Money Transfer - Threat Detection - Inner Journey**.
>
>   The threat detection journey sets the authentication level based on the detected risk level. A medium to high risk level increases the authentication level.
>
> * **User authentication**: Presents a sign-on page for the user to enter their username and password.
>
> * **Account status check**: Checks if the user's email address has been verified. If not, it sends an email with a link to complete the verification before allowing the user to proceed.
>
> * **Authentication step-up**: The **Auth Level Decision** node evaluates the user's current authentication level. A higher authentication level is interpreted as higher risk for subsequent steps, which triggers MFA.
>
>   Switching the True and False outputs of the Auth Level Decision node means a higher current authentication level is interpreted as lower risk, and MFA won't be triggered. This isn't recommended for this journey.
>
> * **Accept terms and conditions**: Checks if the user has accepted the latest terms and conditions. If they haven't, they're prompted to accept them.
>
> After all checks complete successfully, the journey concludes, and the user is granted access. | No                      |

> **Collapse: Show the Money Transfer journey (main journey)**
>
> ![Money transfer main journey](_images/money-transfer-sample/sample-money-transfer-journey.png)
>
> * a A [Scripted Decision node](https://docs.pingidentity.com/auth-node-ref/latest/scripted-decision.html) containing the initialize variables used in the authentication flow.
>
> * b The first call to the PingOne Protect **Money Transfer -Threat Detection - Inner Journey**
>
> * c The second call to the PingOne Protect **Money Transfer -Threat Detection - Inner Journey** for risk evaluation
>
> * d A call to the **Money Transfer - MFA Authentication - Inner Journey**
>
> * e A call to the **Money Transfer SignOn - Inner Journey**

## Before you begin

To implement the sample money transfer journey, you must have these prerequisites:

* Tenant administrator access to your Advanced Identity Cloud development environment.

* For PingOne Protect:

  * PingOne Protect enabled in your PingOne environment. Learn more in [Getting started with PingOne Protect](https://docs.pingidentity.com/pingone/threat_protection_using_pingone_protect/p1_protect_getting_started.html).

  * PingOne Protect integrated with Advanced Identity Cloud. Learn more in [Use PingOne Protect for risk-based authentication and fraud detection](../integrations/pingone-protect.html).

* For PingOne Authorize:

  * PingOne Authorize enabled in your PingOne environment. Learn more in [Getting started with PingOne Authorize](https://docs.pingidentity.com/pingone/authorization_using_pingone_authorize/p1az_getting_started.html).

  * Your PingOne Authorize [decision endpoint](https://docs.pingidentity.com/pingone/authorization_using_pingone_authorize/p1az_decision_endpoints.html).

* Your PingOne Worker Service ID. Learn more in [Set up PingOne product connections](../integrations/pingone-set-up-product-connections.html).

  |   |                                                                                                                                                                                       |
  | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | The worker application associated with the PingOne Worker Service must be granted the necessary permissions to interact with both the PingOne Protect and PingOne Authorize services. |

* For MFA:

  * An SMTP email server. Required for email-based MFA.

  * If you're using Twilio for phone-based MFA, a Twilio account with access to [Twilio Verify](https://www.twilio.com).

* A test user in your Alpha realm with a registered email address. It's also useful to have other MFA methods configured for testing.

* A basic understanding of [journeys](journeys.html) and the [Scripted Decision node](https://docs.pingidentity.com/auth-node-ref/latest/scripted-decision.html).

## Task 1: Prepare your tenant environment

To get the journey working, you must first perform some setup tasks in your Advanced Identity Cloud tenant environment.

### Add custom attributes to the `alpha_user` managed object

Several additional user attributes are required by the money transfer journey.

Add the following custom attributes to the `alpha_user` managed object. Learn more in [Customize user identities using custom attributes](../identities/identity-cloud-identity-schema.html#create-custom-attributes).

|   |                                                                                                                                                                                                                                                                                                                                                                          |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | When adding new attributes, use the advanced options to specify view and edit permissions:- User Editable: Select this option if you want end users to be able to edit the property value in their profile.

- Viewable: Clear this option to hide the property from the user's profile. However, this hides the property from both end users and tenant administrators. |

| Name                          | Label                            | Type   | Description                                                                                                                                         |
| ----------------------------- | -------------------------------- | ------ | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| `custom_emailVerified`        | `Email verified`                 | String | Confirms the user has verified their email address.                                                                                                 |
| `custom_protectActivityCity`  | `PingOne Protect activity city`  | String | The city from which the user attempts to authenticate. This attribute is used in the `Account Disabled` and `Suspicious Activity` email templates.  |
| `custom_protectActivityState` | `PingOne Protect activity state` | String | The state from which the user attempts to authenticate. This attribute is used in the `Account Disabled` and `Suspicious Activity` email templates. |
| `custom_protectDeviceOS`      | `PingOne Protect device OS`      | String | The OS of the device from which the user attempts to authenticate.                                                                                  |
| `custom_mfaDevices`           | `MFA devices`                    | Array  | Stores the user's registered MFA devices.                                                                                                           |
| `custom_latestMFADevice`      | `Latest used MFA device`         | String | The most recently used registered MFA device.                                                                                                       |
| `custom_savingsBalance`       | `Latest savings balance`         | Number | The user's savings account balance after money transfer.                                                                                            |
| `custom_checkingBalance`      | `Latest checking balance`        | Number | The user's checking account balance after money transfer.                                                                                           |
| `custom_currency`             | `Custom currency`                | String | The user's preferred currency.Select User Editable to allow end users to change this value.                                                         |

### (Optional) Set an ESV variable for PingOne Protect analysis

The **Prerequisites & Init Variables** node in the parent journey contains a script that uses the `protectAnalysisRequired` variable to determine if PingOne Protect analysis is enabled. By default, this variable is set to `true` in the script. To override this variable and control how PingOne Protect analysis is performed in different environments, you can set an [Environment Secret & Variable (ESV)](../tenants/esvs.html) variable.

1. In the Advanced Identity Cloud admin console, go to [icon: cog, set=fa]Tenant Settings > Global Settings > Environment Secrets & Variables.

2. On the Variables tab, click + Add Variable.

3. In the Add a Variable modal, enter the following information:

   |                        |                                     |
   | ---------------------- | ----------------------------------- |
   | Name                   | `p1-protect-analysis-required`      |
   | Type                   | `string`                            |
   | Description (optional) | `PingOne Protect analysis required` |
   | Value                  | `true`                              |

4. Click Save to create the variable.

5. Restart Advanced Identity Cloud services by [applying updates in the Advanced Identity Cloud admin console](../tenants/esvs-manage-ui.html#apply_updates).

### Create the email templates

You'll need to create the following email templates, which are used by **Scripted Decision** nodes to send emails at various points in the money transfer journey.

| Email template         | Description                                                                              | Example email body                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| ---------------------- | ---------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **accountDisabled**    | Email sent when PingOne Protect detects critical risk associated with the account.       | > **Collapse: Show example**
>
> ```html
> <div style="display:block;width:400px;margin:0 auto;font-family:sans-serif;border:1px solid #c5c5c5;padding:30px 20px;text-align:center">
> <img src="https://assets.pingone.com/ux/ui-library/5.0.2/images/logo-pingidentity.png" alt="Company Logo" style="height:65px;margin-bottom:10px" />
> <div style="display:block">
> <div style="display:inline-block;width:40px;height:40px;border-radius:50%;background-color:red;color:white;font-size:24px;line-height:40px;text-align:center">!</div>
> <h2 style="margin-top:10px;margin-bottom:10px">Sign-in Attempt was blocked</h2>
> <p>{{object.mail}}</p>
> <hr style="width:100%;margin-top:20px;margin-bottom:25px;border:none;border-top:1px solid #c5c5c5" />
> </div>
> <div style="text-align:left">
> <p id="alertText">Someone just attempted to sign onto your account nearby {{object.custom_protectActivityCity}}, {{object.custom_protectActivityState}}. We have disabled the account for your security. If this was you, please contact support.</p>
> <p>Thanks,
>       <br />The ${Brand Name} team
>     </p>
>   </div>
> </div>
> ```                                         |
| **newDeviceDetected**  | Email sent when PingOne Protect detects a sign-on from a new device.                     | > **Collapse: Show example**
>
> ```html
> <div style="display:block;width:400px;margin:0 auto;font-family:sans-serif;border:1px solid #c5c5c5;padding:30px 20px;text-align:center">
>   <img src="https://assets.pingone.com/ux/ui-library/5.0.2/images/logo-pingidentity.png" alt="Company Logo" style="height:65px;margin-bottom:10px" />
>   <div style="display:block">
>     <div style="display:inline-block;width:40px;height:40px;border-radius:50%;background-color:red;color:white;font-size:24px;line-height:40px;text-align:center">!</div>
>     <h2 style="margin-top:10px;margin-bottom:10px">Sign-in attempt detected</h2>
>     <p>{{object.mail}}</p>
>     <hr style="width:100%;margin-top:20px;margin-bottom:25px;border:none;border-top:1px solid #c5c5c5" />
>   </div>
>   <div style="text-align:left">
>     <p id="alertText">Someone just attempted to sign onto your account nearby {{object.custom_protectActivityCity}}, {{object.custom_protectActivityState}}. If this was not you, please consider resetting your password or contact support. Otherwise, ignore.</p>
>     <p>Thanks,
>       <br />The ${Brand Name} team
>     </p>
>   </div>
> </div>
> ``` |
| **suspiciousActivity** | Email sent when PingOne Protect detects suspicious activity associated with the account. | > **Collapse: Show example**
>
> ```html
> <div style="display:block;width:400px;margin:0 auto;font-family:sans-serif;border:1px solid #c5c5c5;padding:30px 20px;text-align:center">
>   <img src="https://assets.pingone.com/ux/ui-library/5.0.2/images/logo-pingidentity.png" alt="Company Logo" style="height:65px;margin-bottom:10px" />
>   <div style="display:block">
>     <div style="display:inline-block;width:40px;height:40px;border-radius:50%;background-color:red;color:white;font-size:24px;line-height:40px;text-align:center">!</div>
>     <h2 style="margin-top:10px;margin-bottom:10px">Sign-in attempt detected</h2>
>     <p>{{object.mail}}</p>
>     <hr style="width:100%;margin-top:20px;margin-bottom:25px;border:none;border-top:1px solid #c5c5c5" />
>   </div>
>   <div style="text-align:left">
>     <p id="alertText">Someone just attempted to sign onto your account nearby {{object.custom_protectActivityCity}}, {{object.custom_protectActivityState}}. If this was not you, please consider resetting your password or contact support. Otherwise, ignore.</p>
>     <p>Thanks,
>       <br />The ${Brand Name} team
>     </p>
>   </div>
> </div>
> ``` |
| **welcome**            | Email sent when a new user account is created.                                           | > **Collapse: Show example**
>
> ```html
> <html>
>   <head></head>
>   <body style="background-color: #324054; color: #5e6d82; padding: 60px; text-align: center;">
>     <p>Welcome. Your username is '{{object.userName}}'.</p>
>   </body>
> </html>
> ```                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| **otp**                | Email containing the user's one-time passcode (OTP).                                     | > **Collapse: Show example**
>
> ```html
> <html>
>   <head></head>
>   <body style="background-color: #324054; color: #455469; padding: 60px; text-align: center;">
>     <div class="content" style="background-color: #fff; border-radius: 4px; margin: 0 auto; padding: 48px; width: 235px;">
>       <p>
>         <img src="https://www.pingidentity.com/content/dam/picr/nav/Ping-Logo-2.svg" alt="Ping Identity logo">
>         </p>
>         <p>Hi {{object.givenName}}</p>
>         <p>Here is your One Time Password. Please enter it into the login browser window:</p>
>         <h1 id="objectotp">{{object.otp}}</h1>
>         <p>PingOne Advanced Identity Cloud</p>
>       </div>
>     </body>
>   </html>
> ```                                                                                                                                                                                                                                                                                                                                                                                                                                                             |

Learn more about creating email templates in [Email templates](../tenants/email-templates.html).

## Task 2: Create a PingOne Authorize policy

To perform risk-based authorization for transfers, you'll need to create an authorization policy in PingOne Authorize. This policy evaluates a payment's amount against the user's transaction limits.

### Define the `amount` attribute

1. In the PingOne admin console, go to Authorization > Trust Framework.

2. On the Attributes tab, click + Add new Attribute and configure it as follows.

   | Attribute name | Value type |
   | -------------- | ---------- |
   | `amount`       | `Number`   |

3. Click Save Changes.

### Create the payment check policy

1. In the PingOne admin console, go to Authorization > Policies.

2. Click the Plus icon ([icon: add, set=material, size=inline]) and select Add Policy.

3. In the Name field, enter `Payment checks`.

4. Add the following rules to the policy in order.

   Rule 1: Deny payments over the threshold

   * Name: `Deny payments over 10,000`

   * Applies When: `amount` `Greater Than` `10000`

   * Effect: `Deny`

   Rule 2: Permit payments under the threshold

   * Name: `Permit payment less than 1,000`

   * Applies When: `amount` `Less Than` `1000`

   * Effect: `Permit`

   Rule 3: Require approval between thresholds

   * Name: `Payments more than 1,000 but less than 10,000`

   * Applies When:

     * `amount` `Greater Than Or Equal` `1000`

     * `amount` `Less Than Or Equal` `10000`

   * Effect: `Permit`

   * Statements: Add a statement with the following values:

     * Name: `Approval required when amount is in this range`

     * Code: `APPROVAL_REQ`

5. Click **Save Changes**.

## Task 3: Download and import the journey

### Download the journey

1. Go to [Money Transfer journey](https://marketplace.pingone.com/item/money-transfer-aic-journey-template) on the Ping Identity Marketplace.

2. Click Download Integration to download the `Money Transfer - Main Journey.json` file. This JSON file contains the parent journey and inner journeys, scripts, and email templates required for the authentication flow.

### Import the journey

1. In the Advanced Identity Cloud admin console, click Journeys > Journeys.

2. Click [icon: add, set=material, size=inline] Add Journey, select Import, and then click Next.

3. Click either Download Backup or Skip Backup. Learn more in [Import journeys](journeys.html#import-journeys).

4. On the Import Journeys page, browse to and select `Money Transfer - Main Journey.json`.

5. Select Alpha realm users because the journey is configured for the alpha realm.

6. In the Conflict Resolution section, choose how the system resolves import conflicts:

   * Overwrite all conflicts (default)

   * Manually pick conflict resolution

7. Click Next.

8. Click Start Import.

9. On the Import Complete page, click Done.

10. On the left panel of the Journeys page, click Money Transfer (5) to view the money transfer journeys and inner journeys.

## Task 4: Configure the journey components

### Configure the money transfer main journey

1. On the Journeys page, click Money Transfer - Main Journey and click Edit.

2. In the journey editor, configure the journey as follows:

   * [Review and set the initialize variables](#review-set-initialize-variables)

   * [Configure the money transfer URL](#configure-money-transfer-url)

   * [Set the journey to run for all users regardless of current session](#set-journey-for-all-users)

3. Click Save.

|   |                                                                                                                                                                                             |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | To save your progress, periodically click Save in the top right of the journey editor. If you don't save, you'll lose your work if the page reloads or if you lose your network connection. |

#### Review and set the initialize variables

The **Money Transfer - Main Journey** includes a [Scripted Decision node](https://docs.pingidentity.com/auth-node-ref/latest/scripted-decision.html) containing the initialize variables used later in the authentication flow. This script lets you:

* Set the allowed MFA types: `FIDO2`, `OATH`, `PUSH`, `EMAIL`, `SMS`, `VOICE`.

* Enable or disable PingOne Protect analysis.

* Enable or disable [magic link](../am-authentication/suspended-auth.html).

To review and set the initial variables:

1. Click the Prerequisites & Init Variables node.

2. In the Script field, click the Pencil icon ([icon: pencil-alt, set=fa]) to open the `Money Transfer - Initialize Variables` script.

3. Review the script and make changes if needed.

4. Click Save and Close.

|   |                                                                                                             |
| - | ----------------------------------------------------------------------------------------------------------- |
|   | You don't need to update the values in the Script Outputs field of the Prerequisites & Init Variables node. |

#### Configure the money transfer URL

1. Click the Redirect To Money Transfer (Success URL) node.

2. Enter the preview URL of the Money Transfer Inner Journey. For example, `https://<tenant-env-fqdn>/am/XUI/?realm=alpha&authIndexType=service&authIndexValue=MoneyTransfer-InnerJourney`.

3. Click Save.

#### Set the journey to run for all users regardless of current session

1. In the upper right of the journey editor, click the Ellipsis icon ([icon: ellipsis-h, set=fa]) and select [icon: pencil-alt, set=fa]Edit Details.

2. Select Run journey for all users regardless of current session.

3. Click Save.

### Configure the Threat Detection - Inner Journey

1. On the Journeys page click Money Transfer - Threat Detection - Inner Journey and click Edit.

2. In the journey editor, configure the journey as follows:

   1. Click the PingOne Protect Initialize node.

   2. In the PingOne Worker Service ID field, select the ID of the PingOne Worker Service for connecting to PingOne. Learn more in [PingOne Protect Initialize node](https://docs.pingidentity.com/auth-node-ref/latest/pingone/pingone-protect-initialize.html).

   3. Click the Auth: PingOne Protect Evaluation node and enter the following:

      * PingOne Worker Service ID: Select the ID of the PingOne Worker Service for connecting to PingOne.

      * (Optional) Risk Policy Set ID: Enter the ID of the [risk policy](https://docs.pingidentity.com/pingone/threat_protection_using_pingone_protect/p1_protect_risk_policies.html) in PingOne. Learn more in [PingOne Protect Evaluation node](https://docs.pingidentity.com/auth-node-ref/latest/pingone/pingone-protect-evaluation.html)

   4. Click the Reg: PingOne Protect Evaluation node and enter the following:

      * PingOne Worker Service ID: Enter the ID of the PingOne Worker Service for connecting to PingOne.

      * (Optional) Risk Policy Set ID: Enter the ID of the [risk policy](https://docs.pingidentity.com/pingone/threat_protection_using_pingone_protect/p1_protect_risk_policies.html) in PingOne. Learn more in [PingOne Protect Result node](https://docs.pingidentity.com/auth-node-ref/latest/pingone/pingone-protect-result.html).

3. Click Save.

### Configure the Money Transfer - Inner Journey

1. On the Journeys page, click Money Transfer - Inner Journey and click Edit.

2. In the journey editor, configure the journey as follows:

   1. Click the PingOne Authorize node and enter the following:.

      * PingOne Worker Service ID: Select the ID of the PingOne Worker Service for connecting to PingOne.

      * Decision Endpoint ID: Enter the decision endpoint ID from the service in PingOne Authorize.

      * attributelist: Enter `amount`.

      * Statement Codes: Enter `APPROVAL_REQ`.

3. Click Save field.

   1. In the Decision Endpoint ID field, enter the decision endpoint ID from the service in PingOne Authorize

   Learn more about the [PingOne Authorize node](https://docs.pingidentity.com/auth-node-ref/latest/pingone/pingone-authorize.html)

4. Click Save.

### Configure the MFA Authentication - Inner Journey

This configuration is required if `SMS`, or `VOICE` are opted in the `allowedMFATypes` array in the `Money Transfer - Initialize Variables` script in the [Prerequisites & Init Variables](#money-transfer-optional_set_an_esv_variable) node in the parent journey.

1. On the Journeys page, click MFA Authentication - Inner Journey and click Edit.

2. In the journey editor, update the required fields in the following nodes:

   * [Twilio Verify Lookup node](https://docs.pingidentity.com/auth-node-ref/latest/cloud/twilio-verify-lookup.html)

   * [Twilio Verify Sender node](https://docs.pingidentity.com/auth-node-ref/latest/cloud/auth-node-twilio-verify-sender.html)

3. Click Save.

## Task 5: Validate the journey

After configuring the journey, validate the different paths to ensure the risk-based security policies work as expected. The following steps demonstrate a low-risk transfer and a higher-risk transfer that requires approval.

|   |                                                                                                                                                                                                                                                                                                                                                                            |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | To trigger different risk evaluations, you may need to adjust your [risk policies in PingOne Protect](https://docs.pingidentity.com/pingone/threat_protection_using_pingone_protect/p1_protect_risk_policies.html) for sign-on, or your PingOne Authorize policies for the transaction itself. You can also simulate higher risk by signing in from a new device or a VPN. |

Before you begin, ensure you have a test user in the `alpha` realm with a starting balance. For example, set the `custom_savingsBalance` attribute to `10000`.

### Test a low-risk transfer

This test validates the user experience when a transfer is evaluated as low risk.

1. In the Advanced Identity Cloud admin console, go to Journeys.

2. Click Money Transfer - Main Journey.

3. In the Preview URL field, click the copy icon ([icon: copy, set=material, size=inline]) and paste the URL into an incognito browser window.

   The Advanced Identity Cloud end-user UI displays the Sign In screen.

4. Enter the test user's username and password and click Next.

   Because the sign-on is evaluated as low risk, the user is authenticated and redirected to the Money Transfer page.

   ![Make a transfer](_images/money-transfer-sample/make-a-transfer.png)

5. Enter a small amount (for example, `100`) and click Make Transfer.

   ![Make a transfer](_images/money-transfer-sample/successful-transfer.png)

   **Expected result**: The transfer is successful. The page confirms the transaction was completed, and the user's account balance is updated.

### Test a higher-risk transfer

This test validates that the journey requires additional user approval for a transfer that the PingOne Authorize policy evaluates as higher risk.

1. If you're not already signed on, follow steps 1 - 4 in [Test a low-risk transfer](#money-transfer-validation-low-risk) to sign on as your test user.

2. Enter a large amount that exceeds your policy's approval threshold (for example, `5000`).

3. Click Make Transfer.

   **Expected result**: An email is sent to the user asking for approval. After the transfer is approved using the link in the email, the transaction is processed. This confirms that the step-up approval path is triggered for higher-risk transactions.

## Best practices

This sample journey provides a strong foundation for a money transfer journey. When preparing to use it in a production environment, consider the following best practices:

* **Treat as a template**: Remember that this is a sample journey. Always adapt and harden it to meet your specific security policies and business requirements before deploying to production.

* **Use ESVs**: Avoid hardcoding sensitive information like API keys and IDs directly in your journey scripts. Use [ESVs](../tenants/esvs.html) to manage these values securely.

* **Test extensively**: Validate all possible user paths, including low, medium, and high-risk scenarios, as different MFA registration and authentication flows. Ensure the user experience is smooth and the security responses are correct for each case.

* **Review PingOne Protect policies**: Fine-tune your [risk policies in PingOne Protect](https://docs.pingidentity.com/pingone/threat_protection_using_pingone_protect/p1_protect_risk_policies.html) to align with your organization's risk tolerance.

---

---
title: Node versions
description: Manage Advanced Identity Cloud authentication node versions, including how to update nodes to the latest version or revert to an earlier version.
component: pingoneaic
page_id: pingoneaic:journeys:node-versions
canonical_url: https://docs.pingidentity.com/pingoneaic/journeys/node-versions.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Authentication", "Node Versions", "Nodes &amp; Trees"]
section_ids:
  update-node: Update a node
  revert-node-version: Revert to an earlier node version
---

# Node versions

Nodes in Advanced Identity Cloud are versioned.

When a new node version is released, existing journeys that use that node aren't automatically updated. This lets you choose when to update the node in your existing journeys, giving you time to test and validate changes before rolling them out to all users.

When you add a node to your journey, the latest node version is used. However, you can revert to an earlier version of a node, if required.

## Update a node

When a new version of a node is available, you'll see a sync icon ([icon: sync, set=fa]) on the node in the journey editor.

To update a node:

1. Click the node with the sync icon ([icon: sync, set=fa]) to display the node's properties.

2. Click View Details to display the changelog for the new node version.

3. After reviewing the changelog, click Update Node to update to the latest node version.

4. Provide any missing configuration values and connect any unconnected outcomes before saving your journey.

## Revert to an earlier node version

You should always use the latest node version where possible, but you can revert to an earlier node version, if needed.

To revert to an earlier node version:

1. Click the node that you want to revert to display the node's properties.

2. Under the node name, click the current version number to display a list of available versions.

3. Select the version that you want to use and click Revert.

4. Provide any missing configuration values and connect any unconnected outcomes before saving your journey.

---

---
title: Sign on (login) with self-service
description: Implement a prebuilt login journey incorporating social sign-on and progressive profiling to gather user information over time
component: pingoneaic
page_id: pingoneaic:journeys:solution-login-with-self-service-journey
canonical_url: https://docs.pingidentity.com/pingoneaic/journeys/solution-login-with-self-service-journey.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Journeys", "Self-service"]
section_ids:
  login-self-service-use-case: Example use case
  login-self-service-prereqs: Before you begin
  login-self-service-tasks: Tasks
  login-self-service-download-journey: "Task 1: Download the sample journey"
  login-self-service-import-journey: "Task 2: Import the sample journey into Advanced Identity Cloud"
  login-self-service-journey: Login with self-service journey
  login-self-service-validation: Validation
  login-self-service-validation-steps: Steps
---

# Sign on (login) with self-service

Incorporate self-service into your Advanced Identity Cloud journeys to let end users create and manage their own accounts, while you control the available features.

The [Ping Identity Marketplace](https://marketplace.pingone.com/item/login-with-self-service-journey) includes a prebuilt [login with self-service](#login-self-service-journey) journey. This sample journey lets end users sign on using a social identity provider (IdP), such as Google or Facebook, or the username and password of an account in the Advanced Identity Cloud datastore. If the end user doesn't already have an account, they can create one using their social identity credentials.

The journey also includes progressive profiling. On their third successful sign-on attempt, end users are prompted to review their marketing preferences.

You can download the sample journey and import it into your Advanced Identity Cloud tenant. You can then modify the journey as needed to meet your requirements.

## Example use case

A company wants to simplify sign-on and reduce friction by allowing end users to sign on with their Google or Facebook accounts. Additionally, they want to remind end users to review their preferences for receiving news and special offers, ensuring more personalized experiences while staying compliant with data protection regulations.

## Before you begin

To implement the sample journey, you must have:

* Tenant administrator access to your Advanced Identity Cloud development environment.

* Social authentication configured in your Advanced Identity Cloud environment. Learn more in [Social authentication](../self-service/social-registration.html).

  |   |                                                                                                                                                                                                           |
  | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | The sample journey uses Google and Facebook for social sign-on, but you can configure and enable any of the [supported social IdPs](../self-service/social-registration.html#configure-social-providers). |

* A basic understanding of [journeys](journeys.html).

* A test end user in the `alpha` realm. Learn more in [Create test users and roles](../use-cases/use-case-test-users-and-roles.html).

## Tasks

### Task 1: Download the sample journey

1. In the Ping Identity Marketplace, go to [Login with Self-Service Journey](https://marketplace.pingone.com/item/login-with-self-service-journey).

2. Click Download to download the `Login with Self-Service Journey.json` file. This JSON file contains the journeys and scripts required for the authentication flow.

### Task 2: Import the sample journey into Advanced Identity Cloud

1. In the Advanced Identity Cloud admin console, click Journeys > Journeys.

2. Click [icon: add, set=material, size=inline] Add Journey, select Import, and then click Next.

3. Click either Download Backup or Skip Backup. Learn more in [Import journeys](journeys.html#import-journeys).

4. On the Import Journeys page, browse to and select `Login with Self-Service Journey.json`.

5. Select Alpha realm - Users because the journey is configured for the Alpha realm.

6. In the Conflict Resolution section, choose how the system resolves import conflicts:

   * Overwrite all conflicts (default)

   * Manually pick conflict resolution

   |   |                                                                                                                                                                                                                                                                      |
   | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | The progressive profile journey in the download matches the default journey included with Advanced Identity Cloud. If you've modified the default journey and want to retain your changes, select Manually pick conflict resolution and ensure it isn't overwritten. |

7. Click Next.

8. Click Start Import.

9. On the Import Complete page, click Done.

10. On the left panel of the Journeys page, click Login to view the imported journeys:

    * **[Login with self-service journey](#login-self-service-journey)** (parent)

    * **ProgressiveProfile** (inner journey). Learn more about this journey in [Progressive profile](journeys.html#progressive-profile).

## Login with self-service journey

The **Login with self-service** journey lets end users sign on using either a social IdP (such as Google or Facebook) or by entering their username and password. If they don't already have an Advanced Identity Cloud account, end users can create one using their social identity credentials. During this process, they must create a local password and accept the current terms and conditions.

The journey includes an [Inner Tree Evaluator node](https://docs.pingidentity.com/auth-node-ref/latest/inner-tree-evaluator.html) that links to a progressive profile journey. With this journey, end users are prompted to review and update their marketing preferences on their third successful login.

![Login with self-service journey](_images/sample-login-with-self-service/login-with-self-service-journey.png)

The Login with self-service journey uses the following nodes:

| Node                                                                                                                  | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| --------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Page node](https://docs.pingidentity.com/auth-node-ref/latest/page.html)                                             | Combines the following nodes onto a single page for display to the user:- [Platform Password node](https://docs.pingidentity.com/auth-node-ref/latest/platform-password.html)

- [Platform Username node](https://docs.pingidentity.com/auth-node-ref/latest/platform-username.html)

- **Validate Input** node. This [Scripted Decision node](https://docs.pingidentity.com/auth-node-ref/latest/scripted-decision.html) disables the Next button if the input fields are empty.

- [Select Identity Provider node](https://docs.pingidentity.com/auth-node-ref/latest/select-identity-provider.html). You can add or remove social IdPs as needed. Learn more in [Social authentication](../self-service/social-registration.html).

  The social IdP names must exactly match the names in your social authentication configuration, including the case.                                                                                                       |
| [Social Provider Handler node](https://docs.pingidentity.com/auth-node-ref/latest/social-provider-handler.html)       | Attempts to authenticate a user with an IdP they selected in the [Select Identity Provider node](https://docs.pingidentity.com/auth-node-ref/latest/select-identity-provider.html).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [Attribute Present Decision node](https://docs.pingidentity.com/auth-node-ref/latest/attribute-present-decision.html) | Checks the specified identity resource in the underlying identity service and determines if all attributes required to create the specified object exist within the shared node state.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [Page node](https://docs.pingidentity.com/auth-node-ref/latest/page.html)                                             | Combines the following nodes onto a single page for display to the user if they entered the required attributes:- [Platform Password node](https://docs.pingidentity.com/auth-node-ref/latest/platform-password.html)

- [Accept Terms and Conditions node](https://docs.pingidentity.com/auth-node-ref/latest/accept-terms-and-conditions.html). Prompts the user to accept or reject the currently active Terms and Conditions. Learn more in [Terms and Conditions](../self-service/self-registration.html#terms-conditions).                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [Page node](https://docs.pingidentity.com/auth-node-ref/latest/page.html)                                             | Combines the following nodes onto a single page for display to the user if they didn't enter the required attributes:- [Attribute Collector node](https://docs.pingidentity.com/auth-node-ref/latest/attribute-collector.html). This node is configured to collect required attributes for `mail`, `sn`, and `givenName`. You can reconfigure the node to collect different attributes as required.

- **Validate Input** node. This [Scripted Decision node](https://docs.pingidentity.com/auth-node-ref/latest/scripted-decision.html) validates the inputs entered by the user and disables the Next button if the required input fields are empty.

- [Accept Terms and Conditions node](https://docs.pingidentity.com/auth-node-ref/latest/accept-terms-and-conditions.html). Prompts the user to accept or reject the currently active Terms and Conditions. Learn more in [Terms and Conditions](../self-service/self-registration.html#terms-conditions). |
| [Data Store Decision node](https://docs.pingidentity.com/auth-node-ref/latest/data-store-decision.html)               | Checks that the credentials provided during local authentication match the ones stored in the realm datastore.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [Increment Login Count node](https://docs.pingidentity.com/auth-node-ref/latest/increment-login-count.html)           | If an account already exists for the user, increments the successful sign-on count property.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [Inner Tree Evaluator node](https://docs.pingidentity.com/auth-node-ref/latest/inner-tree-evaluator.html)             | Initiates the progressive profile inner journey. Learn more in [Progressive profile](journeys.html#progressive-profile).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [Create Object node](https://docs.pingidentity.com/auth-node-ref/latest/create-object.html)                           | Creates the user's account.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |

## Validation

This validation step demonstrates multiple sign-ons by an end user using their Advanced Identity Cloud username and password. On the third sign-on attempt, the end user is prompted to review and confirm their marketing preferences.

### Steps

1. In the Advanced Identity Cloud admin console, go to [icon: account_tree, set=material, size=inline] Journeys and click `Login with self-service`.

2. In the Preview URL field, click [icon: copy, set=material, size=inline] and paste the URL into an incognito window.

   The hosted pages displays the Sign On screen.

   ![Sign on with self service](_images/sample-login-with-self-service/sign-on-login-with-self-service.png)

3. Enter the test end user's username and password, and click Next.

   You are signed on to the hosted account pages as the test end user.

4. Sign off from the Advanced Identity Cloud end-user UI:

   1. Click the test end user's name in the upper-right corner of the hosted account pages.

   2. Select Sign Out.

      |   |                                                                                                                                                                            |
      | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      |   | The page you're directed to when you sign off is the *default* journey in the realm, not the **Login with self-service** journey. Learn more in [Journeys](journeys.html). |

5. Repeat steps 1 - 4 to sign on and sign off a second time.

6. Repeat steps 1 - 3 to sign on a third time. On the third sign-on attempt, you're presented with a page for selecting preferences for receiving news and special offers.

   ![Select marketing preferences](_images/sample-login-with-self-service/select-preferences.png)

7. Select the test end user's marketing preferences and click Next to sign on to the hosted account pages.

   * If the end user makes no selection, the reminder expires and isn't displayed again.

   * If the end user selects one or more options, the preferences are set in the end user's profile.

---

---
title: Threat detection with PingOne Protect journey
description: Implement a prebuilt threat detection journey using PingOne Protect to analyze user behavior and prevent fraudulent sign-ons
component: pingoneaic
page_id: pingoneaic:journeys:solution-threat-detection-journey
canonical_url: https://docs.pingidentity.com/pingoneaic/journeys/solution-threat-detection-journey.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Authentication", "Journeys"]
page_aliases: ["journey-solutions:sample-threat-detection-journey.adoc"]
section_ids:
  about-threat-detection-journey: About the threat detection journey
  threat-detection-use-case: Example use case
  threat-detection-components: Journey components
  task_1_prepare_your_tenant_environment: "Task 1: Prepare your tenant environment"
  threat-detection-before-begin: Before you begin
  threat-detection-setup-tasks: Setup tasks
  threat-detection-add-custom-attributes: Add custom attributes to the alpha_user managed object
  optional_set_an_esv_variable_for_pingone_protect_analysis: (Optional) Set an ESV variable for PingOne Protect analysis
  create-email-templates: Create the email templates
  create-logger-library-script: Create a logger library script for OTP
  threat-detection-download-import-journey: "Task 2: Download and import the journey"
  download_the_journey: Download the journey
  import_the_journey: Import the journey
  configure-threat-detection-journey: "Task 3: Configure the journey components"
  configure-parent-threat-detection-journey: Configure the Threat Detection Journey with PingOne Protect (parent journey)
  review-set-initialize-variables: Review and set the initialize variables
  enable-social-idps: Enable social identity providers
  configure-threat-detection-inner-journey: Configure the Threat Detection - Inner Journey
  configure-mfa-device-reg-inner-journey: Configure the MFA Device Registration - Inner Journey
  configure-mfa-auth-inner-journey: Configure the MFA Authentication - Inner Journey
  threat-detection-validation: "Task 4: Validate the journey"
  threat-detection-validation-steps: Test a medium-risk sign-on
  threat-detection-journey-best-practices: Best practices
---

# Threat detection with PingOne Protect journey

The Ping Identity Marketplace includes a prebuilt [authentication journey with threat detection](https://marketplace.pingone.com/item/authentication-journey-with-threat-detection) to protect against threats such as fraudulent sign-on attempts.

The journey is intended as a template. Review and adapt it to meet your organization's specific security policies and business requirements before deploying to a production environment.

**Journey download**

| Journey name                                 | Version | Download                                                                                                       |
| -------------------------------------------- | ------- | -------------------------------------------------------------------------------------------------------------- |
| Authentication Journey with Threat Detection | 2.0     | [Download from Marketplace](https://marketplace.pingone.com/item/authentication-journey-with-threat-detection) |

This guide details the prerequisites and configuration steps to implement this solution in your Advanced Identity Cloud tenant.

Learn more about [Threat detection using PingOne Protect](https://docs.pingidentity.com/pingone/threat_protection_using_pingone_protect/p1_protect_overview.html).

## About the threat detection journey

This solution uses a parent journey and inner journeys to evaluate the risk level of a user's sign-on attempt.

### Example use case

A company needs to identify and prevent fraudulent authentication when an end user attempts to sign on from an unusual geographical location. The goal is to reduce fraud while ensuring a frictionless experience for legitimate users.

With the Advanced Identity Cloud authentication with threat detection journey, the user's geographical location is evaluated as part of a real-time threat detection process. If a user attempts to sign on from a location that exceeds a defined radius from the user's expected location, it's considered medium or high risk, depending on the extent of the deviation. The user is either prompted to [step up with multi-factor authentication (MFA)](../am-sessions/session-upgrade.html) or is denied access. If authentication is blocked or requires further verification, the user is notified by email or SMS to confirm that the attempt was legitimate.

### Journey components

The threat detection journey includes one parent journey and seven inner journeys that work together to handle the authentication and threat detection flow.

| Journey                                                             | Description                                                                                                                                                                                                                                                                                                                                                                                                               | Configuration required? |
| ------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------- |
| **Threat Detection Journey with PingOne Protect** (parent journey)  | Orchestrates the overall flow. It initializes variables, presents the sign-on page, calls the appropriate inner journeys, and records the final outcome for machine learning.	The Auth Level Decision node evaluates the user's current authentication level, which is set in the Threat Detection - Inner Journey. A higher authentication level is interpreted as higher risk for subsequent steps, which triggers MFA. | Yes                     |
| **Threat Detection - Inner Journey**                                | Uses the PingOne Protect nodes to initialize the SDK, capture user behavior signals, and evaluate risk.                                                                                                                                                                                                                                                                                                                   | Yes                     |
| **MFA Device Registration - Inner Journey**                         | Manages the flow for registering a new MFA device, if required.                                                                                                                                                                                                                                                                                                                                                           | Yes                     |
| **MFA Authentication - Inner Journey**                              | Handles the MFA challenge when a user needs to step up their authentication.                                                                                                                                                                                                                                                                                                                                              | Yes                     |
| **OATH Registration - Inner Journey**                               | Sets the registration flow for OATH-based MFA.                                                                                                                                                                                                                                                                                                                                                                            | No                      |
| **Push MFA Method Registration - Inner Journey**                    | Sets the registration flow for push-based MFA.                                                                                                                                                                                                                                                                                                                                                                            | No                      |
| **WebAuthn MFA Method Registration - Inner Journey**                | Sets the registration flow for WebAuthn-based MFA.                                                                                                                                                                                                                                                                                                                                                                        | No                      |
| **Combined OATH And PUSH MFA Methods Registration - Inner Journey** | Sets the registration flow for OATH and push MFA.                                                                                                                                                                                                                                                                                                                                                                         | No                      |

> **Collapse: Show the Threat Detection Journey with PingOne Protect (parent journey)**
>
> ![Threat detection parent journey](_images/threat-detection-sample/sample-threat-detection-pingone-protect-journey.png)
>
> * a A [Scripted Decision node](https://docs.pingidentity.com/auth-node-ref/latest/scripted-decision.html) containing the initialize variables used in the authentication flow.
>
> * b The first call to the PingOne Protect **Threat Detection - Inner Journey**
>
> * c The second call to the PingOne Protect **Threat Detection - Inner Journey** for risk evaluation
>
> * d A call to the **MFA Authentication - Inner Journey**
>
> * e A call to the **MFA Device Registration - Inner Journey**

## Task 1: Prepare your tenant environment

First, ensure you have the necessary prerequisites, then perform the required setup tasks in your tenant environment.

### Before you begin

To implement the sample threat detection journey, you must have:

* Tenant administrator access to your Advanced Identity Cloud development environment.

* PingOne Protect enabled in your PingOne environment. Learn more in [Getting started with PingOne Protect](https://docs.pingidentity.com/pingone/threat_protection_using_pingone_protect/p1_protect_getting_started.html).

* PingOne Protect integrated with Advanced Identity Cloud. Learn more in [Integrate with PingOne Protect for risk evaluations](https://docs.pingidentity.com/sdks/latest/sdks/integrations/integrate-with-pingone-protect.html#steps).

* Your PingOne Worker Service ID. This is required to connect to your PingOne instance and send it the necessary data to make risk evaluations. Learn more in [Create a worker application in PingOne](https://docs.pingidentity.com/sdks/latest/sdks/integrations/pingone-protect/01-prerequisites.html).

* For MFA:

  * An SMTP email server. Required for email-based MFA.

  * If you're using Twilio for phone-based MFA, a Twilio account with access to [Twilio Verify](https://www.twilio.com).

* Social authentication configured in your Advanced Identity Cloud environment. Learn more in [Social authentication](../self-service/social-registration.html).

  |   |                                                                                                                                                                                                                                                                                                               |
  | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | The sample journey uses Google and Facebook for social sign-on, but you can configure and enable any of the [supported social identity providers](../self-service/social-registration.html#configure-social-providers). You can also disable social sign-on if you don't need it in your authentication flow. |

* A basic understanding of [journeys](journeys.html) and the [Scripted Decision node](https://docs.pingidentity.com/auth-node-ref/latest/scripted-decision.html).

### Setup tasks

To get the journey working, you'll first need to perform some setup tasks in your Advanced Identity Cloud tenant environment.

#### Add custom attributes to the `alpha_user` managed object

Several additional user attributes are required by the threat detection user journey. These attributes store information about the user's verified email, geographical location, operating system (OS), and MFA devices.

Add the following custom attributes to the `alpha_user` managed object. Learn more in [Customize user identities using custom attributes](../identities/identity-cloud-identity-schema.html#create-custom-attributes).

| Name                          | Label                            | Type   | Description                                                                                                                                         |
| ----------------------------- | -------------------------------- | ------ | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| `custom_emailVerified`        | `Email verified`                 | String | Confirms the user has verified their email address.                                                                                                 |
| `custom_protectActivityCity`  | `PingOne Protect activity city`  | String | The city from which the user attempts to authenticate. This attribute is used in the `Account Disabled` and `Suspicious Activity` email templates.  |
| `custom_protectActivityState` | `PingOne Protect activity state` | String | The state from which the user attempts to authenticate. This attribute is used in the `Account Disabled` and `Suspicious Activity` email templates. |
| `custom_protectDeviceOS`      | `PingOne Protect device OS`      | String | The OS of the device from which the user attempts to authenticate.                                                                                  |
| `custom_mfaDevices`           | `MFA devices`                    | Array  | Sets, fetches, and displays the user's registered MFA devices.                                                                                      |
| `custom_latestMFADevice`      | `Latest used MFA device`         | String | The most recent MFA device registered by the user, used in the `Device Registration FIDO` email template.                                           |

#### (Optional) Set an ESV variable for PingOne Protect analysis

The **Prerequisites & Init Variables** node in the parent journey contains a script that uses the `protectAnalysisRequired` variable to determine if PingOne Protect analysis is enabled. By default, this variable is set to `true` within the script. To override this variable and control how PingOne Protect analysis is performed in different environments, you can set an [Environment Secret & Variable (ESV)](../tenants/esvs.html) variable.

1. In the Advanced Identity Cloud admin console, go to [icon: cog, set=fa]Tenant Settings > Global Settings > Environment Secrets & Variables.

2. Click the Variables tab.

3. Click + Add Variable.

4. In the Add a Variable modal, enter the following information:

   |                        |                                     |
   | ---------------------- | ----------------------------------- |
   | Name                   | `p1-protect-analysis-required`      |
   | Type                   | `string`                            |
   | Description (optional) | `PingOne Protect analysis required` |
   | Value                  | `true`                              |

5. Click Save to create the variable.

6. Restart Advanced Identity Cloud services by [applying updates in the Advanced Identity Cloud admin console](../tenants/esvs-manage-ui.html#apply-updates).

#### Create the email templates

You'll need to create the following email templates, which are used by **Scripted Decision** nodes to send emails at various points in the threat detection journey.

| Email template         | Description                                                                        | Example email body                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| ---------------------- | ---------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **accountDisabled**    | Email sent when PingOne Protect detects critical risk associated with the account. | > **Collapse: Show example**
>
> ```html
> <div style="display:block;width:400px;margin:0 auto;font-family:sans-serif;border:1px solid #c5c5c5;padding:30px 20px;text-align:center">
> <img src="https://assets.pingone.com/ux/ui-library/5.0.2/images/logo-pingidentity.png" alt="Company Logo" style="height:65px;margin-bottom:10px" />
> <div style="display:block">
> <div style="display:inline-block;width:40px;height:40px;border-radius:50%;background-color:red;color:white;font-size:24px;line-height:40px;text-align:center">!</div>
> <h2 style="margin-top:10px;margin-bottom:10px">Sign-in Attempt was blocked</h2>
> <p>{{object.mail}}</p>
> <hr style="width:100%;margin-top:20px;margin-bottom:25px;border:none;border-top:1px solid #c5c5c5" />
> </div>
> <div style="text-align:left">
> <p id="alertText">Someone just attempted to sign onto your account nearby {{object.custom_protectActivityCity}}, {{object.custom_protectActivityState}}. We have disabled the account for your security. If this was you, please contact support.</p>
> <p>Thanks,
>       <br />The ${Brand Name} tea
>     </p>
>   </div>
> </div>
> ```                                          |
| **deviceRegistration** | Email sent when the user registers a new MFA device.                               | > **Collapse: Show example**
>
> ```html
> <div style="display:block;text-align:center;font-family:'Arial',
>   sans-serif;background-color:#f7f7f7;border:1px solid #e3e3e3;border-radius:10px;box-shadow:0 4px 8px rgba(0, 0, 0, 0.1);width:400px;margin:20px 20px;padding:30px 20px">
>   <img src="https://assets.pingone.com/ux/ui-library/5.0.2/images/logo-pingidentity.png" alt="Company Logo" style="height:65px;margin-bottom:10px" />
>   <h2 style="color:#333;font-size:24px;margin:20px 0">Sign On Device Added </h2>
>   <p style="margin:20px 0 20px;font-size:16px;color:#555">The following device was successfully added to your
>     account and can be used to authenticate. </p>
>   <p style="margin:20px 0 20px;font-size:20px;color:#222">{{object.custom_latestMFADevice}}</p>
>   <p style="margin:20px 0 20px;font-size:16px;color:#555">If you added this device, no further action is needed. </p>
>   <p style="margin:20px 0 20px;font-size:16px;color:#555">If this device wasn't added by you, consider resetting
>     your password to secure your account. </p>
> </div>
> ```                                                                                |
| **suspiciousActivity** | Email sent when PingOne Protect detects some risk associated with the account.     | > **Collapse: Show example**
>
> ```html
> <div style="display:block;width:400px;margin:0 auto;font-family:sans-serif;border:1px solid #c5c5c5;padding:30px 20px;text-align:center">
>   <img src="https://assets.pingone.com/ux/ui-library/5.0.2/images/logo-pingidentity.png" alt="Company Logo" style="height:65px;margin-bottom:10px" />
>   <div style="display:block">
>     <div style="display:inline-block;width:40px;height:40px;border-radius:50%;background-color:red;color:white;font-size:24px;line-height:40px;text-align:center">!</div>
>     <h2 style="margin-top:10px;margin-bottom:10px">Sign-in attempt detected</h2>
>     <p>{{object.mail}}</p>
>     <hr style="width:100%;margin-top:20px;margin-bottom:25px;border:none;border-top:1px solid #c5c5c5" />
>   </div>
>   <div style="text-align:left">
>     <p id="alertText">Someone just attempted to sign onto your account nearby {{object.custom_protectActivityCity}}, {{object.custom_protectActivityState}}. If this was not you, please consider resetting your password or contact support. Otherwise, ignore.</p>
>     <p>Thanks,
>       <br />The ${Brand Name} team
>     </p>
>   </div>
> </div>
> ``` |
| **welcome**            | Email sent when a new user account is created.                                     | > **Collapse: Show example**
>
> ```html
> <html>
>   <head></head>
>   <body style="background-color: #324054; color: #5e6d82; padding: 60px; text-align: center;">
>     <p>Welcome. Your username is '{{object.userName}}'.</p>
>   </body>
> </html>
> ```                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| **otp**                | Email containing the user's one-time passcode (OTP).                               | > **Collapse: Show example**
>
> ```html
> <html>
>   <head></head>
>   <body style="background-color: #324054; color: #455469; padding: 60px; text-align: center;">
>     <div class="content" style="background-color: #fff; border-radius: 4px; margin: 0 auto; padding: 48px; width: 235px;">
>       <p>
>         <img src="https://www.pingidentity.com/content/dam/picr/nav/Ping-Logo-2.svg" alt>
>         </p>
>         <p>Hi {{object.givenName}}</p>
>         <p>Here is your One Time Password. Please enter it into the login browser window:</p>
>         <h1 id="objectotp">{{object.otp}}</h1>
>         <p>PingOne Advanced Identity Cloud</p>
>       </div>
>     </body>
>   </html>
> ```                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |

Lean more about creating email templates in [Email templates](../tenants/email-templates.html).

#### Create a logger library script for OTP

If you're using OTP emails in your journey flow, you must create a [library script](../am-scripting/library-scripts.html). This script creates a logger, which is needed for OTP functionality to track and debug the process of sending OTP emails.

1. In the Advanced Identity Cloud admin console, go to Scripts > Auth Scripts, then click + New Script.

2. Select Other > Library and click Next.

3. Enter a script name and description, and paste the following script into the JavaScript field:

   ```javascript
   function XLogger(env) {
                 this.logger = env.logger;
                 this.scriptName = env.scriptName;
                 this.logPrefix = "***" + env.scriptName + ": ";
                 this.debug("logger initialised");
               }
               XLogger.prototype.debug = function (message) {
                 this.logger.debug(this.logPrefix.concat(message));
               };
               XLogger.prototype.warn = function (message) {
                 this.logger.warn(this.logPrefix.concat(message));
               };
               XLogger.prototype.error = function (message) {
                 this.logger.error(this.logPrefix.concat(message));
               };
               module.exports.XLogger = XLogger;
   ```

4. Click Save to save the script.

## Task 2: Download and import the journey

### Download the journey

1. Go to [Authentication Journey with Threat Detection](https://marketplace.pingone.com/item/authentication-journey-with-threat-detection) on the Ping Identity marketplace.

2. Click Download Integration to download a file called `Authentication Journey with Threat Detection.json`. This JSON file contains the parent journey and inner journeys, scripts, and email templates required for the authentication flow.

### Import the journey

1. In the Advanced Identity Cloud admin console, click Journeys > Journeys.

2. Click [icon: add, set=material, size=inline] Add Journey, select Import, and then click Next.

3. Click either Download Backup or Skip Backup. Learn more in [Import journeys](journeys.html#import-journeys).

4. On the Import Journeys page, browse to and select `Authentication Journey with Threat Detection.json`.

5. Select `Alpha realm users` because the journey is configured for the alpha realm.

6. In the Conflict Resolution section, choose how the system resolves import conflicts:

   * Overwrite all conflicts (default)

   * Manually pick conflict resolution

7. Click Next.

8. Click Start Import.

9. On the Import Complete page, click Done.

10. On the left panel of the Journeys page, click `Threat Detection (8)` to view the threat detection journeys and inner journeys.

![Threat detection journeys](_images/threat-detection-sample/threat-detection-journeys.png)

## Task 3: Configure the journey components

### Configure the Threat Detection Journey with PingOne Protect (parent journey)

1. On the Journeys page, click `Threat Detection Journey with PingOne Protect` and click Edit.

2. In the journey editor, configure the journey as follows:

   1. [Review and set the initialize variables](#review-set-initialize-variables).

   2. If you have configured social identity providers other than Google and Facebook, [enable social identity providers](#enable-social-idps).

3. Click Save.

|   |                                                                                                                                                                                                   |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | To save your progress, periodically click Save in the top right of the journey editor. Failure to do this results in losing your work if the page reloads or if you lose your network connection. |

#### Review and set the initialize variables

The **Threat Detection Journey with PingOne Protect** includes a [Scripted Decision node](https://docs.pingidentity.com/auth-node-ref/latest/scripted-decision.html) containing the initialize variables used later in the authentication flow. This script lets you:

* Set the allowed MFA types: `FIDO2`, `OATH`, `PUSH`, `EMAIL`, `SMS`, `VOICE`.

* Enable or disable PingOne Protect analysis.

* Enable or disable [magic link](../am-authentication/suspended-auth.html).

To review and set the initial variables:

1. Click the Prerequisites & Init Variables node.

2. In the Script field, click the Pencil icon ([icon: pencil-alt, set=fa]) to open the `Threat Detection - Initialize Variables` script.

3. Review the script and make changes if needed.

4. Click Save and Close.

|   |                                                                                                             |
| - | ----------------------------------------------------------------------------------------------------------- |
|   | You don't need to update the values in the Script Outputs field of the Prerequisites & Init Variables node. |

#### Enable social identity providers

1. Click the Page node and then click the Select Identity Provider node.

2. In the Filter Enabled Providers field, add or remove the social identity providers as needed. Only the social identity providers listed here will be presented to the end user when signing on.

   |   |                                                                                                                         |
   | - | ----------------------------------------------------------------------------------------------------------------------- |
   |   | The social provider names must exactly match the names in your social authentication configuration, including the case. |

3. Click Save.

### Configure the Threat Detection - Inner Journey

1. On the Journeys page click `Threat Detection - Inner Journey` and click Edit.

2. In the journey editor, configure the journey as follows:

   1. Click the PingOne Protect Initialize node.

   2. In the PingOne Worker Service ID field, select the ID of the PingOne worker service for connecting to PingOne. Learn more in [PingOne Protect Initialize node](https://docs.pingidentity.com/auth-node-ref/latest/pingone/pingone-protect-initialize.html).

   3. Click the Auth: PingOne Protect Evaluation node and enter the following:

      * PingOne Worker Service ID: Select the ID of the PingOne worker service for connecting to PingOne.

      * (Optional) Risk Policy Set ID: Enter the ID of the [risk policy](https://docs.pingidentity.com/pingone/threat_protection_using_pingone_protect/p1_protect_risk_policies.html) in PingOne. Learn more in [PingOne Protect Evaluation node](https://docs.pingidentity.com/auth-node-ref/latest/pingone/pingone-protect-evaluation.html)

   4. Click the Reg: PingOne Protect Evaluation node and enter the following:

      * PingOne Worker Service ID: Enter the ID of the PingOne worker service for connecting to PingOne.

      * (Optional) Risk Policy Set ID: Enter the ID of the [risk policy](https://docs.pingidentity.com/pingone/threat_protection_using_pingone_protect/p1_protect_risk_policies.html) in PingOne. Learn more in [PingOne Protect Result node](https://docs.pingidentity.com/auth-node-ref/latest/pingone/pingone-protect-result.html).

3. Click Save.

### Configure the MFA Device Registration - Inner Journey

This configuration is required if `SMS` or `VOICE` are opted in the `allowedMFATypes` array in the `Threat Detection - Initialize Variables` script in the [Prerequisites & Init Variables](#optional_set_an_esv_variable_for_pingone_protect_analysis) node in the parent journey.

1. On the Journeys page, click `MFA Device Registration - Inner Journey` and click Edit.

2. In the journey editor, update the required fields in the following nodes:

   * [Twilio Verify Lookup node](https://docs.pingidentity.com/auth-node-ref/latest/cloud/twilio-verify-lookup.html)

   * [Twilio Verify Sender node](https://docs.pingidentity.com/auth-node-ref/latest/cloud/auth-node-twilio-verify-sender.html)

3. Click Save.

### Configure the MFA Authentication - Inner Journey

This configuration is required if `EMAIL`, `SMS`, or `VOICE` are opted in the `allowedMFATypes` array in the `Threat Detection - Initialize Variables` script in the [Prerequisites & Init Variables](#optional_set_an_esv_variable_for_pingone_protect_analysis) node in the parent journey.

1. On the Journeys page, click `MFA Authentication - Inner Journey` and click Edit.

2. In the journey editor, update the required fields in the following nodes:

   * [Twilio Verify Lookup node](https://docs.pingidentity.com/auth-node-ref/latest/cloud/twilio-verify-lookup.html)

   * [Twilio Verify Sender node](https://docs.pingidentity.com/auth-node-ref/latest/cloud/auth-node-twilio-verify-sender.html)

3. Click Save.

## Task 4: Validate the journey

There are various paths the end user might go down, depending on the PingOne Protect risk evaluation and the MFA methods configured in the journey. For example, a user identified as low risk can sign on without MFA. However, for medium or high-risk sign-on attempts, the journey prompts the user to choose an MFA method, which could involve registering a new device. If a user signing on for the first time is identified as high risk, the registration attempt is blocked.

Before validating the journey, make sure you have a test user in the `alpha` realm. To authenticate using an OTP, the user must have a registered authenticator app.

### Test a medium-risk sign-on

These steps demonstrate a sign-on attempt by an end user identified as medium risk.

1. In the Advanced Identity Cloud admin console, go to Journeys and click Threat Detection Journey with PingOne Protect\`.

2. In the Preview URL field, click [icon: copy, set=material, size=inline] and paste the URL into an incognito window.

   The hosted pages displays the Sign In screen.

   ![Threat detection journey sign in screen](_images/threat-detection-sample/threat-detection-sign-in.png)

3. Enter the test user's username and password and click Next.

   A page displays prompting the user to select their preferred authentication method for MFA.

4. Select `OATH` and click Next.

   ![Select MFA method](_images/threat-detection-sample/threat-detection-select-mfa.png)

5. Enter the OTP from the test user's app, and click Submit

   ![Select MFA method](_images/threat-detection-sample/threat-detection-verification-code.png)

   You are signed on to the hosted account pages as the test user.

## Best practices

This sample journey provides a strong foundation for threat detection. When preparing to use it in a production environment, consider the following best practices:

* **Treat as a template**: Remember that this is a sample journey. Always adapt and harden it to meet your specific security policies and business requirements before deploying to production.

* **Use Environment Secrets & Variables (ESVs)**: Avoid hardcoding sensitive information like API keys and IDs directly in your journey scripts. Use [ESVs](../tenants/esvs.html) to manage these values securely.

* **Test extensively**: Validate all possible user paths, including low, medium, and high-risk scenarios, as different MFA registration and authentication flows. Ensure the user experience is smooth and the security responses are correct for each case.

* **Review PingOne Protect policies**: Fine-tune your [risk policies in PingOne Protect](https://docs.pingidentity.com/pingone/threat_protection_using_pingone_protect/p1_protect_risk_policies.html) to align with your organization's risk tolerance.