---
title: Actions reference
description: Actions are predefined sets of nodes designed to perform specific tasks. They are not complete flows, but you can use them during flow creation to simplify the process.
component: davinci
page_id: davinci:flows:davinci_actions
canonical_url: https://docs.pingidentity.com/davinci/flows/davinci_actions.html
llms_txt: https://docs.pingidentity.com/davinci/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 21, 2026
section_ids:
  registration: Registration
  sign-up-with-tos-agreement: Sign up with TOS Agreement
  description: Description
  required-configuration: Required configuration
  outputs: Outputs
  email-verification: Email verification
  description-2: Description
  required-configuration-2: Required configuration
  outputs-2: Outputs
  mfa-device-registration: MFA Device Registration
  description-3: Description
  required-configuration-3: Required configuration
  outputs-3: Outputs
  authentication: Authentication
  mfa-device-authentication: MFA Device Authentication
  description-4: Description
  required-configuration-4: Required configuration
  inputs: Inputs
  sign-on-with-password-reset: Sign On with Password Reset
  description-5: Description
  required-configuration-5: Required configuration
  outputs-4: Outputs
  account-recovery: Account Recovery
  account-recovery-2: Account Recovery
  description-6: Description
  required-configuration-6: Required configuration
  inputs-2: Inputs
---

# Actions reference

Actions are predefined sets of nodes designed to perform specific tasks. They are not complete flows, but you can use them during flow creation to simplify the process.

Actions can be placed in the following categories:

* **Registration**: Actions that are used in the creation of new users.

* **Authentication**: Actions that are used to authenticate existing users.

* **Account Recovery**: Actions that are used to help a user recover an account.

|   |                                                                                                                        |
| - | ---------------------------------------------------------------------------------------------------------------------- |
|   | Actions are currently available in the [PingOne Marketplace](https://marketplace.pingone.com/browse?products=davinci). |

## Registration

Registration actions are used in the creation of new users.

### Sign up with TOS Agreement

This action lets a user create an account and agree to a TOS.

![A screen capture of the Sign Up With TOS Agreement action.](_images/Actions-Sign-Up-with-TOS-Agreement.png)

#### Description

This action presents the user with an account registration form including an agreement. It then uses an authentication connector to create the user account.

#### Required configuration

To configure the action:

1. Click the **Registration** node, then in the **Agreement** field, select an agreement to present to the user.

   To find the agreement ID, sign on to PingOne and go to **User Experience** > **Agreements**. Select the agreement and click the API tab to view the policy ID.

2. Click the **Authentication** node, then in the **Population** field, select a user population in which to create the user.

   To find the population ID, sign on to PingOne and go to **Directory** > **Populations**. Select the population to view the population ID.

3. Connect the beginning and ending nodes to the rest of your flow.

#### Outputs

This action identifies the user.

### Email verification

This action lets a user verify an email address.

![A screen capture of the Email Verification action.](_images/Actions-Email-Verification.png)

#### Description

This action presents the user with a registration form. An authentication node creates the user and sends a verification code, then an email verification form displays. If the user submits a verification code, an authentication node verifies the code. If the user clicks **Resend Code**, an authentication node resends the code if the retry limit has not been reached.

#### Required configuration

To configure the action:

1. Click the first **Authentication** node, then in the **Population** field, select a user population in which to create the user.

   To find the population ID, sign on to PingOne and go to **Directory** > **Populations**. Select the population to view the population ID.

2. Connect the beginning and ending nodes to the rest of your flow.

#### Outputs

This action identifies the user.

### MFA Device Registration

This action lets a user register an MFA device.

![A screen capture of the MFA Device Registration action.](_images/Actions-MFA-Device-Registration.png)

#### Description

This action presents users with a form for selecting an MFA device. If the user selects authenticator, email, text, or voice, it uses a function connector to set visibility parameters, then if the MFA method uses OTP, it presents the user with a form on which to enter their email or phone number.

The action then uses an MFA node to begin device registration. If the device type is OTP or TOTP, it presents a form on which the user can enter a passcode. If the device type is FIDO, it presents a form on which the user can configure a FIDO2 authentication method. In either case, an MFA node then completes the device registration.

#### Required configuration

To configure the action:

1. Click the first **MFA** node, then in the **MFA Policy ID** list, select an MFA policy to use.

   To find the MFA policy ID, sign on to PingOne and go to **Authentication** > **MFA**. Select the policy to view the policy ID.

2. Connect the beginning and ending nodes to the rest of your flow.

#### Outputs

This action identifies the user.

## Authentication

This section describes actions that are used to authenticate existing users.

### MFA Device Authentication

This action lets a user authenticate using a known MFA device.

![A screen capture of the MFA Device Authentication action.](_images/Actions-MFA-Device-Authentication-2.png)

#### Description

This action uses an MFA node to check the authentication policy. If the MFA policy's method selection is set to Prompt user to select, a form prompts the user to select an MFA device. If the user selects authenticator, email, text, or voice, it uses a function connector to set visibility parameters.

The action then uses an MFA node to begin device authentication. If the device type is OTP or TOTP, it presents a form on which the user can enter a passcode. If the device type is FIDO, it presents a form on which the user can configure a FIDO2 authentication method. In either case, an MFA node then completes the device authentication.

#### Required configuration

To configure the action:

1. Click the first **MFA** node, then in the **MFA Policy ID** list, select an MFA policy to use.

   To find the MFA policy ID, sign on to PingOne and go to **Authentication** > **MFA**. Select the policy to view the policy ID.

2. Connect the beginning and ending nodes to the rest of your flow.

#### Inputs

This action requires an identified user.

### Sign On with Password Reset

This action lets a user sign on and reset their password if necessary.

![A screen capture of the Sign On with Password Reset action.](_images/Actions-Sign-In-Password-Reset.png)

#### Description

This action presents the user with a sign on form. An Authentication node checks if the user requires a new password. If the user does not require a new password, an authentication node authenticates the user. If the user requires a new password, a form prompts the user for a new password, then an authentication node updates the password.

#### Required configuration

To configure the action:

1. Click the second **Authentication** node, then in the **Agreement** field, select an agreement to present to the user.

   To find the agreement ID, sign on to PingOne and go to **User Experience** > **Agreements**. Select the agreement and click the API tab to view the policy ID.

2. Connect the beginning and ending nodes to the rest of your flow.

#### Outputs

This action requires an identified user.

## Account Recovery

This section describes actions that are used to help a user recover an account.

### Account Recovery

This action lets a user recover an account.

![A screen capture of the Account Recovery action.](_images/Actions-account-recovery.png)

#### Description

This action presents the user with a password recovery form. It then uses an authentication node to send a recovery code, and presents the user with a new password form. If the user completes the form and continues, an authentication node resets their password. If the user resends the code, an authentication node checks the number of retries and resends the code if the retry limit has not been reached.

#### Required configuration

To configure the action, connect the beginning and ending nodes to the rest of your flow.

#### Inputs

This action requires an identified user.

---

---
title: Adding an item to the canvas
description: When you create or add to a flow, you do so by adding nodes or groups of nodes to the canvas using the icon. This presents the following options for additions to the flow:
component: davinci
page_id: davinci:flows:davinci_adding_an_item_to_the_canvas
canonical_url: https://docs.pingidentity.com/davinci/flows/davinci_adding_an_item_to_the_canvas.html
llms_txt: https://docs.pingidentity.com/davinci/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: October 25, 2023
---

# Adding an item to the canvas

When you create or add to a flow, you do so by adding nodes or groups of nodes to the canvas using the [icon: plus, set=fa]icon. This presents the following options for additions to the flow:

* **Connector**: Adds a connector of any sort to the canvas.

  This can be an existing connector that's already configured in your environment, or a new connector.

* **User Interface**: Adds a connector with a user interface to the connector.

  This can be either a PingOne forms connector, a custom HTML form using the HTTP connector, or a basic message using the HTTP connector.

* **Subflow**: Adds a flow conductor connector that launches a subflow that you select.

---

---
title: Adding annotations
description: Add annotations to make a flow more comprehensible to yourself and others developing the flow.
component: davinci
page_id: davinci:flows:davinci_adding_annotations
canonical_url: https://docs.pingidentity.com/davinci/flows/davinci_adding_annotations.html
llms_txt: https://docs.pingidentity.com/davinci/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: October 25, 2023
section_ids:
  steps: Steps
---

# Adding annotations

Add annotations to make a flow more comprehensible to yourself and others developing the flow.

## Steps

1. In DaVinci, click the **Flows** tab.

2. Find the flow and click **... > Edit**.

3. Right-click the flow canvas.

4. Click **Add Annotation**.

5. Click the annotation.

6. (Optional) Update the annotation properties.

   1. In the **Annotation Text** field, enter the text to display in the annotation.

   2. In the **Background Color** selector, select a color for the annotation background.

   3. In the **Text Color** selector, select a color for the annotation text.

   4. In the **Width** field, enter a width in pixels for the annotation.

   5. In the **Height** field, enter a height in pixels for the annotation.

   6. Select **Stroke Enabled** to add a border around the annotation.

   7. In the **Stroke Width** field, enter a width in pixels for the stroke.

   8. In the **Stroke Color** selector, select a color for the stroke.

   9. In the **Corner Radius** field, enter a radius in pixels for the rounding of the annotation corners.

   10. In the **Font Size** field, enter a font size for the annotation text.

   11. In the **Font Style** selector, select a font style. Valid options are **Normal**, **Bold**, and **Italic**.

   12. In the **Font Family** field, enter a font for the annotation text.

7. Click **Apply**.

---

---
title: Adding SK-Components to a connector
description: Add an SK-Component to the HTML Template section of a connector such as the HTTP connector to add additional capabilities to the user-facing page for that node.
component: davinci
page_id: davinci:flows:davinci_adding_sk_components
canonical_url: https://docs.pingidentity.com/davinci/flows/davinci_adding_sk_components.html
llms_txt: https://docs.pingidentity.com/davinci/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: November 15, 2023
section_ids:
  about-this-task: About this task
  steps: Steps
  next-steps: Next steps
---

# Adding SK-Components to a connector

Add an SK-Component to the **HTML Template** section of a connector such as the HTTP connector to add additional capabilities to the user-facing page for that node.

## About this task

You can add SK-Components to multiple connectors, but this example adds an SK-Component to an HTTP node in your flow.

## Steps

1. Add an HTTP connector to your flow.

   |   |                                                                                                                                   |
   | - | --------------------------------------------------------------------------------------------------------------------------------- |
   |   | For more information on adding a connector to your flow, see [Adding a connector](../connectors/davinci_adding_a_connector.html). |

   A node is added to your flow.

2. In your flow, select the node that you added in the previous step.

3. Select the **Custom HTML Template** capability.

4. In the **HTML Template** section of the **General** tab, click the **{}** icon.

   ![Screenshot showing the HTML Template field with the \\{} icon in the lower right.](_images/dkb1700084211470.png)

5. In the **Choose Connection** list, select **SK-Component**.

   You see a complete list of available components below the **HTML Template** section.

   ![Screenshot showing the HTML Template field with a list of available SK-Components.](_images/ygb1700084360003.png)

6. Select an SK-Component to include with your custom HTML for that page.

   For example, adding the `skbutton` component under your text displays a button for the user-facing page when the flow is run.

7. Click the component that appears in the **HTML Template** to view configuration options.

   |   |                                                                                                                                                                                              |
   | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | SK-Components have different configuration options based on their functionality. For an overview of each component's configuration options, see [SK-Components](davinci_sk_components.html). |

8. Click **Apply** after you finish adding your content and one or more SK-Components.

## Next steps

Click the **Save**, **Deploy**, and **Try Flow** buttons to view the user-facing page created by your custom HTML and test any SK-Components that you included.

---

---
title: Changing a connector instance
description: To use a different instance of a selected connector while retaining its in-flow configuration, change the linked connector.
component: davinci
page_id: davinci:flows:davinci_changing_a_linked_connection
canonical_url: https://docs.pingidentity.com/davinci/flows/davinci_changing_a_linked_connection.html
llms_txt: https://docs.pingidentity.com/davinci/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: October 11, 2023
section_ids:
  about-this-task: About this task
  steps: Steps
  result: Result
---

# Changing a connector instance

To use a different instance of a selected connector while retaining its in-flow configuration, change the linked connector.

## About this task

|   |                                                                                                                                                            |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | When you change the linked connector for a node, all other nodes in the flow that use the same connector type are updated to use the new linked connector. |

## Steps

1. Click the **Flows** tab.

2. Locate and open the flow.

3. Right-click the node.

4. Click **Change Linked Connector (for nodes of the same type)**.

5. Select a new connector instance from the **Replace Connector** window.

## Result

All nodes in the flow of the selected connector type now use the new connector instance.

---

---
title: Cloning a flow
description: Clone a flow to create an identical new flow.
component: davinci
page_id: davinci:flows:davinci_cloning_a_flow
canonical_url: https://docs.pingidentity.com/davinci/flows/davinci_cloning_a_flow.html
llms_txt: https://docs.pingidentity.com/davinci/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: February 2, 2023
section_ids:
  about-this-task: About this task
  steps: Steps
  result: Result
---

# Cloning a flow

Clone a flow to create an identical new flow.

## About this task

Cloning an existing flow lets you use the existing flow's steps and settings as a starting point for a modified flow.

## Steps

1. In DaVinci, click the **Flows** tab.

2. Find the flow you want to clone and click **... > Clone**.

## Result

A new flow is created with identical naming, steps, and settings. The description of the new flow indicates the time at which it was cloned.

---

---
title: Cloning a node
description: Clone a node to add an identical node to the flow.
component: davinci
page_id: davinci:flows:davinci_cloning_a_node
canonical_url: https://docs.pingidentity.com/davinci/flows/davinci_cloning_a_node.html
llms_txt: https://docs.pingidentity.com/davinci/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: February 2, 2023
section_ids:
  steps: Steps
---

# Cloning a node

Clone a node to add an identical node to the flow.

## Steps

1. In DaVinci, click the **Flows** tab.

2. Locate and open the flow.

3. Right-click the node.

4. Click **Clone**.

---

---
title: Common flow variables
description: Flow templates created by Ping Identity use variables to make it easy for you to configure the flow. Although each flow uses a unique set of variables, the most common ones are defined in this list.
component: davinci
page_id: davinci:flows:davinci_common_flow_variables
canonical_url: https://docs.pingidentity.com/davinci/flows/davinci_common_flow_variables.html
llms_txt: https://docs.pingidentity.com/davinci/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: October 6, 2023
---

# Common flow variables

Flow templates created by Ping Identity use variables to make it easy for you to configure the flow. Although each flow uses a unique set of variables, the most common ones are defined in this list.

|   |                                                                                                                                                                                                     |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | If your flow uses variables that aren't listed below, check the flow template listing in the [Ping Identity Marketplace](https://marketplace.pingone.com/browse?contentType=davinciFlows) for help. |

To configure the variables, go to the **Variables** tab in the main DaVinci menu. If a flow uses variables that you already have set, you don't need to configure them again. If a flow uses new variables, DaVinci automatically adds them to your **Variables** list.

![A screen capture of the Variables tab with two variables highlighted.](_images/bvj1669070355038.png)

**Table 1. Common Flow Variables**

| Variable Name      | Description                                                                                                                                                       |
| ------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **origin**         | Your PingOne domain, such as `auth.pingone.com`.&#xA;&#xA;Change this value if your region is Canada, EMEA, or APAC, or you have a custom PingOne domain.         |
| **originURL**      | Your PingOne URL, such as `https://auth.pingone.com`.&#xA;&#xA;Change this value if your region is Canada, EMEA, or APAC, or you have a custom PingOne domain.    |
| **companyLogo**    | Your company logo image URL, such as `https://cloudacme.example.com/logo.png`.This enhances the user experience with your brand.                                  |
| **companyName**    | Your company name.This enhances the user experience with your brand.                                                                                              |
| **relyingParty**   | The name of the relying party, such as `PingOne`.                                                                                                                 |
| **relyingPartyID** | The ID of the relying party, such as `auth.pingone.com`.&#xA;&#xA;Change this value if your region is Canada, EMEA, or APAC, or you have a custom PingOne domain. |

---

---
title: Content Security Policies
description: Content Security Policy (CSP) is a browser security feature that mitigates common web security threats (such as cross-site scripting and clickjacking) by explicitly defining what resources a website can load. CSP can be implemented by defining a set of policy directives in the HTTP headers of a website. It's enforced at the browser level, with all browsers supporting a common set of policy directives.
component: davinci
page_id: davinci:flows:davinci_content_security_policies
canonical_url: https://docs.pingidentity.com/davinci/flows/davinci_content_security_policies.html
llms_txt: https://docs.pingidentity.com/davinci/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 28, 2026
section_ids:
  baseline-policy: Baseline policy
  using-a-custom-csp: Using a custom CSP
  mitigating-csp-issues: Mitigating CSP issues
  adding-scripts-dynamically: Adding scripts dynamically
  adding-event-handlers: Adding event handlers
  managing-scripts-injected-by-network-infrastructure: Managing scripts injected by network infrastructure
  use-cases: Use cases
  controlling-iframe-usage: Controlling iframe usage
  report-to-a-monitoring-service: Report to a monitoring service
  csp-best-practices: CSP best practices
---

# Content Security Policies

Content Security Policy (CSP) is a browser security feature that mitigates common web security threats (such as cross-site scripting and clickjacking) by explicitly defining what resources a website can load. CSP can be implemented by defining a set of policy directives in the HTTP headers of a website. It's enforced at the browser level, with all browsers supporting a common set of policy directives.

There are two types of CSP:

* Report-only policy: Set in the `Content-Security-Policy-Report-Only` HTTP header, the browser won't enforce the defined policy directives but will report violations.

* Enforced policy: Set in the `Content-Security-Policy` HTTP header, the browser enforces the defined policy directives.

## Baseline policy

DaVinci uses a report-only baseline CSP for all flows that use the `auth` domain. This baseline CSP will begin to be enforced in September. You can override this CSP for specific flows if your environment has a custom domain.

|   |                                                         |
| - | ------------------------------------------------------- |
|   | This CSP is sent as a header, not as a tag or meta-tag. |

```
script-src 'nonce-<random>' 'strict-dynamic' 'unsafe-eval' 'unsafe-inline' https: http:;
object-src 'none';
base-uri 'none';
```

These directives are used in the baseline policy:

* `script-src 'nonce-<random>'`: Only scripts tagged with the specified nonce are allowed to execute. This nonce is included in the CSP response header and automatically applied to scripts that are included in the flow.

  * `'strict-dynamic'`: Trust propagates from scripts that have the nonce to any scripts that they load.

  * `'unsafe-inline'`: Included as a fallback for older browser versions that don't support nonces. This directive is ignored if the browser version supports nonces.

  * `http:`: Included as a fallback for older browser versions that don't support nonces. This directive is ignored if the browser version supports nonces.

  * `https:`: Included as a fallback for older browser versions that don't support nonces. This directive is ignored if the browser version supports nonces.

  * `'unsafe-eval'`: Allows certain dependencies of the DaVinci JavaScript widget to work correctly.

* `object-src 'none'`: Browser plugins such as Flash aren't permitted to load.

* `base-uri 'none'`: The page cannot set a base URL. This directive prevents \<base> tag injection attacks.

A CSP in enforce mode can block scripts from being loaded and prevent other modifications to the page, which can cause flow executions to fail. When a violation occurs, the JavaScript console includes an error message similar to the following:

```
Refused to execute inline script because it violates the following Content Security Policy directive: "script-src 'nonce-rAnd0m'". Either the 'unsafe-inline' keyword, a hash ('sha256-...'), or a nonce-source ('nonce-...') is required to enable inline execution.
```

## Using a custom CSP

Instead of using the baseline enforced CSP, you can configure any flow to use an alternate CSP in enforce mode, an alternate CSP in report-only mode, or both. This option is only available if your environment has a custom domain. Learn more in [Editing flow settings](davinci_editing_flow_settings.html).

## Mitigating CSP issues

You can modify your flow or your environment to mitigate common CSP issues.

### Adding scripts dynamically

Because of the strict-dynamic directive, scripts with the nonce can load additional scripts without having to explicitly add the nonce. The nonce propagates automatically on modern browsers. However, older browsers might not honor the strict-dynamic directive. For maximum compatibility across browsers, a pattern like this is recommended for loading additional scripts into the page.

```javascript
const getCspNonce = () => {
  const nonceScript = document?.querySelector('#davinciWidgetScriptElement')
  const nonce = nonceScript?.nonce || nonceScript?.getAttribute('nonce')
  return (typeof nonce === 'string' && nonce !== '') ? nonce : ''
}

const script = document.createElement('script')
script.nonce = getCspNonce()
script.src = "https://mydomain.com/myscript.js"
document.head.appendChild(script)
```

Inline scripts can be added in a similar way:

```javascript
const getCspNonce = () => {
  const nonceScript = document?.querySelector('#davinciWidgetScriptElement')
  const nonce = nonceScript?.nonce || nonceScript?.getAttribute('nonce')
  return (typeof nonce === 'string' && nonce !== '') ? nonce : ''
}

const script = document.createElement('script')
script.nonce = getCspNonce()
script.innerHTML = "console.log('this is an inline script')"
document.head.appendChild(script)
```

### Adding event handlers

You can add event handlers that won't be blocked by the CSP by avoiding the use of the `setAttribute` method. For example:

```javascript
const btn = document.getElementById("btn");
btn.addEventListener("click", () => {
  alert("clicked");
});
```

### Managing scripts injected by network infrastructure

Network infrastructure, such as reverse proxies, can inject scripts into HTML responses. Because those scripts might not include the nonce, the browser could block them.

If you're using network infrastructure like this, review the network infrastructure's documentation to see if it automatically integrates with the application-defined CSP or whether any special configuration is required.

## Use cases

### Controlling iframe usage

The baseline CSP allows DaVinci pages to be loaded in iframes by external websites. This can expose users to the risk of clickjacking attacks, including possible harvesting of credentials. To prevent DaVinci pages from being loaded in any external website, add the following directive to your custom CSP: `frame-ancestors 'none';`.

Alternatively, you can allow other pages on your custom domain to load DaVinci pages in an iframe by specifying `frame-ancestors 'self';`. You can allow additional specified domains to load DaVinci pages by listing the domains, as follows: `frame-ancestors 'self' https://example.com https://example.org;`.

### Report to a monitoring service

By default, CSP policy violations are logged to the browser console and contained to each end user's computer or device.

To configure policy violations for all end users to be logged to a monitoring service, add the report-uri policy directive and specify an endpoint set up to receive CSP policy violation JSON payloads. The following examples configure the CSP report monitoring service provided by [Report URI](#https://report-uri.com/products/content_security_policy) to monitor report-only policy violations:

* For your report-only policy:

  1. Configure a CSP in your flow settings to add or update the report-uri policy directive:

     ```
     Content-Security-Policy-Report-Only: ... report-uri https://<subdomain>.report-uri.com/r/d/csp/reportOnly;
     ```

     Replace \<subdomain> with the subdomain of your Report URI account.

  2. Test hosted pages and check that violations are reported to your Report URI account.

* For your enforced policy:

  1. Configure a CSP in your flow settings to add or update the following policy directive:

     ```
     Content-Security-Policy: ... report-uri https://<subdomain>.report-uri.com/r/d/csp/enforce;
     ```

## CSP best practices

* **Build your CSP incrementally**: When implementing a CSP, it's best to start with a minimal set of directives and gradually expand it as you identify the resources your application needs. This helps avoid breaking functionality while still enhancing security.

* **Start with report-only mode**: Always begin by implementing your CSP in report-only mode. This allows you to monitor and identify any violations without blocking legitimate resources.

* **Be specific with directives and sources**: When defining your CSP directives, be as specific as possible with the allowed sources. Avoid using overly broad directive values like \* unless absolutely necessary, as this can undermine the security benefits of CSP.

* **Browser compatibility**: Test your CSP configuration in different browsers to ensure compatibility. Some browsers might not support all CSP directives or values.

* **Monitor violations**: Actively review the browser console for reported violations. This helps you understand how your policy impacts your applications and identify any missing directives or sources.

* **CSP reporting service**: Consider using a CSP reporting service to collect and analyze CSP violations across all end users. This can help you identify patterns and trends in CSP violations, which can inform your security strategy.

* **Iterate and refine**: Based on the reported violations, incrementally add or modify policy directives. This iterative approach minimizes the risk of breaking functionality.

* **Regularly review and update policies**: Your websites and applications evolve, and so should your CSP. Regularly review your CSP configurations to ensure they remain relevant and effective:

  * **New features and integrations**: When adding new features or integrating with third-party services, remember to update your CSP to allow necessary resources.

  * **Security audits**: Include CSP review as part of your regular security audits.

---

---
title: Copying nodes
description: Copy one or more nodes to paste them into the current flow or into another flow.
component: davinci
page_id: davinci:flows:davinci_copying_nodes
canonical_url: https://docs.pingidentity.com/davinci/flows/davinci_copying_nodes.html
llms_txt: https://docs.pingidentity.com/davinci/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: February 2, 2023
section_ids:
  steps: Steps
  result: Result
---

# Copying nodes

Copy one or more nodes to paste them into the current flow or into another flow.

## Steps

1. In DaVinci, click the **Flows** tab.

2. Locate and open the flow.

3. Select one or more nodes.

4. Right-click the nodes.

5. Click **Copy**.

## Result

The nodes are copied. Paste the nodes by right-clicking the background of any flow and clicking **Paste Nodes**.

---

---
title: Deleting a flow
description: Delete an existing flow.
component: davinci
page_id: davinci:flows:davinci_deleting_a_flow
canonical_url: https://docs.pingidentity.com/davinci/flows/davinci_deleting_a_flow.html
llms_txt: https://docs.pingidentity.com/davinci/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: February 2, 2023
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Deleting a flow

Delete an existing flow.

## About this task

|   |                                                          |
| - | -------------------------------------------------------- |
|   | Verify that the flow you intend to delete is not in use. |

## Steps

1. In DaVinci, click the **Flows** tab.

2. Find the flow you want to delete and click **... > Delete**. On the confirmation modal, click **Delete**.

---

---
title: Deleting a node
description: Delete a node to remove it from the flow and break any connections to it.
component: davinci
page_id: davinci:flows:davinci_deleting_a_node
canonical_url: https://docs.pingidentity.com/davinci/flows/davinci_deleting_a_node.html
llms_txt: https://docs.pingidentity.com/davinci/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: February 2, 2023
section_ids:
  steps: Steps
---

# Deleting a node

Delete a node to remove it from the flow and break any connections to it.

## Steps

1. In DaVinci, click the **Flows** tab.

2. Locate and open the flow.

3. Right-click the node.

4. Click **Delete**.

   A confirmation modal opens.

5. Click **Delete**.

---

---
title: Disabling or enabling a node
description: Disable a node to temporarily prevent it from being executed when the flow is run. Enable it to execute the node as normal.
component: davinci
page_id: davinci:flows:davinci_disablng_or_enabling_a_node
canonical_url: https://docs.pingidentity.com/davinci/flows/davinci_disablng_or_enabling_a_node.html
llms_txt: https://docs.pingidentity.com/davinci/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: February 2, 2023
section_ids:
  steps: Steps
---

# Disabling or enabling a node

Disable a node to temporarily prevent it from being executed when the flow is run. Enable it to execute the node as normal.

## Steps

1. In DaVinci, click the **Flows** tab.

2. Locate and open the flow.

3. Right-click the node.

4. Click **Disable** or **Enable**.

---

---
title: Editing flow settings
description: Configure the settings that apply to the flow as a whole.
component: davinci
page_id: davinci:flows:davinci_editing_flow_settings
canonical_url: https://docs.pingidentity.com/davinci/flows/davinci_editing_flow_settings.html
llms_txt: https://docs.pingidentity.com/davinci/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: October 14, 2025
page_aliases: ["ROOT:davinci-legacy-browser-ea.adoc"]
section_ids:
  steps: Steps
---

# Editing flow settings

Configure the settings that apply to the flow as a whole.

## Steps

1. In the DaVinci admin console, click the **Flows** tab.

2. Find the flow and click **... > Edit**.

3. Click **More options ( [icon: ellipsis-v, set=fa]) > Flow Settings** to show the flow settings.

4. (Optional) Click the **General** tab to configure general settings for the flow.

   | Option                                                   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
   | -------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
   | **PingOne Flow**                                         | Indicates that the flow is a PingOne flow, enabling it to be included in PingOne flow policies and launched directly from PingOne.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
   | **Validate Flows when Changes are Saved**                | Automatically validate the flow whenever it is saved.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
   | **Require Authentication to Initiate Flow**              | Require authentication as part of the flow initiation.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
   | **Legacy Browser and WebView Compatible Rendering Mode** | Switches the flow to support rendering in a legacy browser directly or within a WebView compatible with legacy browsers. This setting is intended for legacy systems that rely on Trident 7+ or EdgeHTML 18+ WebView rendering engines in situations where upgrading to a Chromium browser is not yet possible.Some elements and features are limited or unavailable when this setting is enabled:- PingOne Forms can't be used.

   - You can't use Google reCAPTCHA.

   - SVG animations can only be used by including them in a **Custom HTML Template**.

   - FIDO2 functionality might be limited.

   - PingOne Protect uses version 5.5.2.

   - Images (such as logos) can't be added directly in HTML nodes. Instead, you must add them using the **Custom CSS Rules** option.

   - JavaScript styling might render differently. Take the following steps if your flow is a Ping authorized productized flow that uses JavaScript:

     * Test the flow in a legacy browser or WebView environment.

     * Enable the **Use Custom JavaScript** setting.

     * In the **Custom JavaScript Files** section, add the `https://assets.pingone.com/ux/end-user-nano/0.1.0-alpha.16/src/element-qsa-scope.js`, `https://assets.pingone.com/ux/end-user-nano/0.1.0-alpha.16/src/ie11CustomProperties.js`, and `https://assets.pingone.com/ux/end-user-nano/0.1.0-alpha.21/src/msapplication-overrides.js` files.

   - CSS styling might render differently. Take the following steps if your flow is a Ping authorized productized flow that uses CSS:

     * Test the flow in a legacy browser or WebView environment.

     * If you are using the PingOne DaVinci default CSS, ensure that the latest CSS version is configured in the **Custom CSS Files** section, include the `https://assets.pingone.com/ux/astro-nano/0.1.0-alpha.18/icons.css` and `https://assets.pingone.com/ux/end-user-nano/0.1.0-alpha.21/end-user-nano.css` files, and include the following custom CSS rule:

       ```none
       .companyLogo

       { /* Ping Logo */ background-image: url("https://uploads.pingone.com/environments/6a3d153e-e285-4ac6-8388-5ac0b9f9aa53/images/bcac3292-cfca-49d3-8f58-2bd288582cf3_33abd619-ad95-456f-8bf8-f0af2cff760f_original.png"); width: 200px; height: auto; background-size: cover; background-repeat: no-repeat; background-position: center; }

       .footerLogo { /* Ping Logo */ background-image: url("https://authenticator.pingone.com/pingid/assets/images/ping-logo.sm.2x.png"); width: 105px !important; height: auto; background-size: cover; background-repeat: no-repeat; background-position: center; }``
       ``` |
   | **Flow Timeout (in seconds)**                            | A timeout value for the entire flow, beginning when the flow is invoked. The default value is 300 (five minutes) and the maximum value is 172800 (two days).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
   | **Flow HTTP Response Timeout (in seconds)**              | A timeout value for any HTTP call made by any node in the flow. The default value is 15 and the maximum value is 120.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
   | **Enable Content Security Policy**                       | Restricts the domains from which content can be loaded.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
   | **CSP Value**                                            | If you selected **Enable Content Security Policy**, enter your content security policy in text form.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |

5. (Optional) Click the **Logging** tab to configure logging levels and sensitive data protections for the flow.

   | Option                           | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
   | -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | **Log Level**                    | The logging level for the flow, which determines what events are logged and which nodes are highlighted in flow analytics.The options are:- **None**: Prevents logging.

   - **Error**: Logs **Start Interaction** and **Send Error Response** events, which provides basic details about the error including a high-level reason. Flow analytics will highlight every node that was activated. This is the default level.

   - **Info**: Logs events showing the actions taken by every active node, as well as identifiers such as `correlationId` and `transactionId` where relevant. Flow analytics will highlight every node that was activated.

   - **Debug**: Logs detailed events about the actions taken by every active node, including node inputs and outputs, as well as identifiers such as `correlationId` and `transactionId` where relevant. Flow analytics will highlight every node that was activated.

     &#xA;&#xA;When Debug Mode is selected, the logs can include sensitive data, such as credentials or personal information. |
   | **Scrub Sensitive Information**  | Remove the values of sensitive fields from analytics. When you enable this setting, the **Sensitive Information Fields** field displays. The values of the fields you specify are removed from analytics.	Some sensitive fields are always removed from analytics regardless of this setting. Learn more in Viewing flow analytics.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
   | **Sensitive Information Fields** | If you selected **Scrub Sensitive Information**, enter one or more fields to designate as sensitive. The values of these fields are removed from analytics.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |

6. (Optional) Click the **Customizations** tab to configure UI customizations for the flow.

   * Expand the **Page Customization** section to customize page settings:

     | Option                      | Description                                                                                                            |
     | --------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
     | **Page Title**              | An HTML page title to use in place of the default title.                                                               |
     | **Favicon URL**             | A link to a favicon for the flow.                                                                                      |
     | **Disable DaVinci CSS**     | Prevents the default DaVinci CSS rules from being applied to the flow.                                                 |
     | **Use Custom CSS**          | Apply custom CSS to the user-visible nodes in the flow.                                                                |
     | **Custom CSS Rules**        | If you selected **Use Custom CSS**, enter the CSS code to apply.                                                       |
     | **Custom CSS files**        | If you selected **Use Custom CSS**, enter one or more links to the CSS code to apply.                                  |
     | **Use Custom JavaScript**   | Apply a custom JavaScript to the user-visible nodes in the flow.                                                       |
     | **Custom JavaScript files** | If you selected **Use Custom Script**, enter one or more links to JavaScript files to apply to the user-visible nodes. |

   * Expand the **Error Screen Customization** section to customize error screens:

     | Option                                  | Description                                                                                                                                                                                                                                                                      |
     | --------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
     | **Use Custom Timeout Error Screen**     | Use a custom timeout error screen instead of the standard DaVinci error screen.&#xA;&#xA;If a flow uses magic links or external identity providers, the custom flow timeout error might not display for timeouts that occur during the execution of those nodes.                 |
     | **Customize Timeout Error Screen HTML** | If you selected **Use Custom Timeout Error Screen**, enter the HTML for your custom timeout error screen.                                                                                                                                                                        |
     | **Customize Timeout Error Screen CSS**  | If you selected **Use Custom Timeout Error Screen**, enter the CSS for your custom timeout error screen.                                                                                                                                                                         |
     | **Custom Timeout Error Message**        | Enter text to display as a timeout error message. If this field is blank, the default timeout error message is used.                                                                                                                                                             |
     | **Error Page Logo**                     | A list for selecting the logo to display on the error page. The options are:- **None**: Displays no logo.

     - **Ping Identity Logo**: Displays a Ping Identity logo.

     - **Use Custom Logo URL**: Displays a logo from a URL that you specify using the **Custom Logo URL** field. |
     | **Custom Logo URL**                     | The URL for a brand logo to use on error screens if **Use Custom Logo URL** is selected in the **Error Page Logo** list.                                                                                                                                                         |

   * Expand the **Immediate Loading Screen Customization** section to customize what displays when a node is still loading.

     | Option                                  | Description                                               |
     | --------------------------------------- | --------------------------------------------------------- |
     | **Show Intermediate Loading Page**      | Display an intermediate screen between nodes in the flow. |
     | **Intermediate Loading Page HTML**      | Enter HTML for the loading screen.                        |
     | **Intermediate Loading Page CSS Rules** | Enter CSS for the loading screen.                         |

7. (Optional) Click the **Security** tab to configure security settings for the flow.

   | Option                                          | Description                                                                                                                                                                                                                                                                                         |
   | ----------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | **Enforce Content Security Policy**             | Enables the use of a custom Content Security Policy (CSP) in enforce mode.This option is only available if your environment has a custom domain. If you don't have a custom domain, the baseline CSP is applied. Learn more in [Content Security Policies](davinci_content_security_policies.html). |
   | **Enforced Content Security Policy Value**      | The CSP to apply to the flow if **Enforce Content Security Policy** is enabled.                                                                                                                                                                                                                     |
   | **Report-Only Content Security Policy**         | Enables the use of a Content Security Policy (CSP) in report-only mode.This option is only available if your environment has a custom domain. If you don't have a custom domain, the baseline CSP is applied. Learn more in [Content Security Policies](davinci_content_security_policies.html).    |
   | **Report Destination URL**                      | The URL to which CSP reports from the **Report-Only Content Security Policy** are sent if **Report-Only Content Security Policy** is enabled.                                                                                                                                                       |
   | **Report-Only Content Security Policy Value**   | The CSP to apply to the flow in report-only mode if **Report-Only Content Security Policy** is enabled.                                                                                                                                                                                             |
   | **Enable Content Security Policy (Deprecated)** | A deprecated field that enabled the use of a custom Content Security Policy (CSP) in enforce mode.If you are using this setting, switch to the **Enforce Content Security Policy** setting.                                                                                                         |
   | **CSP value (Deprecated)**                      | A deprecated field for the CSP to enforce if **Enable Content Security Policy (Deprecated)** was enabled.If you are using this field, switch to the **Enforced Content Security Policy Value** field.                                                                                               |

8. Click **Save**.

---

---
title: Editing the input schema
description: Configure the information that's provided to the flow when it is invoked. This lets you map in external parameters for dynamic content or logic.
component: davinci
page_id: davinci:flows:davinci_editing_the_input_schema
canonical_url: https://docs.pingidentity.com/davinci/flows/davinci_editing_the_input_schema.html
llms_txt: https://docs.pingidentity.com/davinci/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 19, 2024
section_ids:
  steps: Steps
---

# Editing the input schema

Configure the information that's provided to the flow when it is invoked. This lets you map in external parameters for dynamic content or logic.

## Steps

1. In DaVinci, click the **Flows** tab.

2. Find the flow and click **... > Edit**.

3. Click **Input Schema**.

4. On the **Input Schema** tab, add one or more properties to the input schema:

   1. Click **Add** to add a new property.

   2. In the **Parameter Name** field, enter a name for the input parameter.

      |   |                                                      |
      | - | ---------------------------------------------------- |
      |   | The name `challenge` is reserved and cannot be used. |

   3. (Optional) In the **Description** field, enter a description for the input property.

   4. In the **Data Type** list, select a data type for the input property.

   5. Select **Required** if the property is required for the flow.

5. (Optional) Click **All Required?** to change the **Required** setting of all properties.

6. (Optional) Click **Edit** to reorder or remove properties, and then click **Close**.

   | Option      | Description                           |
   | ----------- | ------------------------------------- |
   | **Delete**  | Click to remove a property.           |
   | **Reorder** | Click and drag to reorder a property. |

7. Click **Save**.

---

---
title: Editing the output schema
description: Configure the information included in the output when the flow completes.
component: davinci
page_id: davinci:flows:davinci_editing_the_output_schema
canonical_url: https://docs.pingidentity.com/davinci/flows/davinci_editing_the_output_schema.html
llms_txt: https://docs.pingidentity.com/davinci/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: February 2, 2023
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Editing the output schema

Configure the information included in the output when the flow completes.

## About this task

The output from the flow is generated using a JSON schema with `output` as a root object.

## Steps

1. In DaVinci, click the **Flows** tab.

2. Find the flow and click **... > Edit**.

3. Click **More options ( [icon: ellipsis-v, set=fa]) > Output Schema** to show the output schema.

4. Update the JSON schema.

   You can add one or more parameters to the properties section. For example, this output schema outputs the errorMessage and selectedDeviceOtpEnabled properties:

   ```json
   {
     "output": {
       "type": "object",
       "additionalProperties":true,
       "properties": {
         "errorMessage": {
           "type": "string",
           "displayName": "Error Message",
           "preferredControlType": "textField",
           "enableParameters": true,
           "propertyName": "errorMessage"
         },
         "selectedDeviceOtpEnabled": {
           "type":"bool"
         }
       }
     }
   }
   ```

5. Click **Save**.

---

---
title: Exporting a flow
description: Export a flow to create a flow backup file that you can analyze or import into another environment.
component: davinci
page_id: davinci:flows:davinci_exporting_a_flow
canonical_url: https://docs.pingidentity.com/davinci/flows/davinci_exporting_a_flow.html
llms_txt: https://docs.pingidentity.com/davinci/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: October 14, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
  choose-from: Choose from:
---

# Exporting a flow

Export a flow to create a flow backup file that you can analyze or import into another environment.

## About this task

Exporting a flow creates a JSON version of the flow. You can use this file to:

* Copy flows between your different environments, such as between test and production

* Create backups or store flows in external version control systems

* Share the flow with colleagues who use a different environment

You can also export forms that are part of the flow. Learn more in [Importing and exporting forms](https://docs.pingidentity.com/pingone/user_experience/p1_import_export_forms.html).

Ping support might also request flows for troubleshooting purposes.

## Steps

1. In DaVinci, click the **Flows** tab.

2. Open the flow that you want to export.

3. Choose one of the export options:

   ### Choose from:

   * To export the current version, click **More options ( [icon: ellipsis-v, set=fa]) > Download Flow JSON**.

   * To export a previous version, go to **More options ( [icon: ellipsis-v, set=fa]) > Flow Versions**, locate the version that you want to export, and click **... > Download Flow JSON**.

4. (Optional) Select **Include Variable Values** to include the current values of company or flow variables that are used in the flow.

   |   |                                                                                                                                                             |
   | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | Because variables can contain secret or proprietary information, only use this option for flows that you do not plan to share outside of your organization. |

5. (Optional) If the flow uses subflows, select **Include Subflows** to include the subflows in the JSON file.

   |   |                                                                                                                                           |
   | - | ----------------------------------------------------------------------------------------------------------------------------------------- |
   |   | If you plan to import the flow into another environment for a second time, you can disable this option to avoid reimporting the subflows. |

   |   |                                                                                                                                                                                                                                                                |
   | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | If you selected **Include Subflows**, and the flow contains **Flow Conductor** nodes that use invalid subflows or subflow versions, an error message displays detailing the issues. You must resolve these issues before exporting the flow with its subflows. |

6. (Optional) If the flow includes forms, select **Include Forms** to include any forms that are part of the flow.

7. Click **Export**.

---

---
title: Flow editing options
description: You can control many flow properties using the More options ( ) menu while editing a flow.
component: davinci
page_id: davinci:flows:davinci_flow_editing_options
canonical_url: https://docs.pingidentity.com/davinci/flows/davinci_flow_editing_options.html
llms_txt: https://docs.pingidentity.com/davinci/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: October 18, 2023
---

# Flow editing options

You can control many flow properties using the **More options ( [icon: ellipsis-v, set=fa])** menu while editing a flow.

| Option                                                               | Description                                                                                                                                                                                                                                            |
| -------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **More options ( [icon: ellipsis-v, set=fa]) > Enable Flow**         | Enables or disables the flow. Disabled flows cannot be used by end users.                                                                                                                                                                              |
| **More options ( [icon: ellipsis-v, set=fa]) > Show Node ID**        | Displays the node ID for each node, just beneath the node itself.                                                                                                                                                                                      |
| **More options ( [icon: ellipsis-v, set=fa]) > Analytics**           | Displays flow analytics. Learn more in [Viewing flow analytics](davinci_viewing_flow_analytics.html).                                                                                                                                                  |
| **More options ( [icon: ellipsis-v, set=fa]) > Flow Versions**       | Displays a list of versions of the flow\.This list notes the latest version, the deployed version, and the changes that were made in each version.                                                                                                     |
| **More options ( [icon: ellipsis-v, set=fa]) > Clone Flow**          | Clones the flow. Learn more in [Cloning a flow](davinci_cloning_a_flow.html).                                                                                                                                                                          |
| **More options ( [icon: ellipsis-v, set=fa]) > Download Flow Image** | Downloads a PNG image of the flow.                                                                                                                                                                                                                     |
| **More options ( [icon: ellipsis-v, set=fa]) > Download Flow JSON**  | Downloads a JavaScript Object Notation (JSON) *(tooltip: \<div class="paragraph">&#xA;\<p>An open, lightweight data-interchange format that uses human-readable text to store and transmit data.\</p>&#xA;\</div>)* file containing the complete flow. |
| **More options ( [icon: ellipsis-v, set=fa]) > Input Schema**        | Configures the flow's input schema. Learn more in [Editing the input schema](davinci_editing_the_input_schema.html).                                                                                                                                   |
| **More options ( [icon: ellipsis-v, set=fa]) > Output Schema**       | Configures the flow's output schema. Learn more in [Editing the output schema](davinci_editing_the_output_schema.html).                                                                                                                                |
| **More options ( [icon: ellipsis-v, set=fa]) > Flow Settings**       | Configures the flow settings. Learn more in [Editing flow settings](davinci_editing_flow_settings.html).                                                                                                                                               |

---

---
title: Flow limits
description: These limits affect the creation of flows.
component: davinci
page_id: davinci:flows:davinci_flow_limits
canonical_url: https://docs.pingidentity.com/davinci/flows/davinci_flow_limits.html
llms_txt: https://docs.pingidentity.com/davinci/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 4, 2024
---

# Flow limits

These limits affect the creation of flows.

Some connectors have additional limitations; see the connector documentation for your connectors to learn more.

For PingOne standard platform limits, see [PingOne standard platform limits](https://docs.pingidentity.com/pingone/getting_started_with_pingone/p1_platform_limits.html).

Flow limits

| Property                                              | Limit                                                   | Description                                                                                                                                                                                          |
| ----------------------------------------------------- | ------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Resource                                              | 100                                                     | Your environment can contain a maximum of 100 of each entity type. This limitation applies to flows and connections, but not to variables or end users. Each flow is limited to 100 stored versions. |
| Variable                                              | 200, 1 MB each                                          | Your environment can include a total of 200 variables across all variable types. Each variable can have a maximum size of 1 MB.                                                                      |
| API payload                                           | 10 MB                                                   | The maximum payload size for any API call (such as POST, GET, or DELETE) made within a flow.                                                                                                         |
| Number of times a node can be run per flow invocation | 20                                                      | If a flow repeats one or more nodes, each node can be run a maximum of 20 times. This limitation doesn't apply to polling nodes.                                                                     |
| Flow timeout                                          | Default is 5 minutes. Maximum possible is 2 days.       | A timeout value for the entire flow, beginning when the flow is invoked.Editable for each flow. Learn more in [Editing flow settings](davinci_editing_flow_settings.html).                           |
| Flow HTTP response timeout                            | Default is 15 seconds. Maximum possible is 120 seconds. | A timeout value for any HTTP call made by any node in the flow\.Editable for each flow. Learn more in [Editing flow settings](davinci_editing_flow_settings.html).                                   |
| Node payload                                          | 1 MB                                                    | The maximum size of the payload sent by a node to future nodes.                                                                                                                                      |

---

---
title: Flow Validation Rules
description: The following errors can be identified by flow validation:
component: davinci
page_id: davinci:flows:davinci_flow_validation_rules
canonical_url: https://docs.pingidentity.com/davinci/flows/davinci_flow_validation_rules.html
llms_txt: https://docs.pingidentity.com/davinci/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: October 13, 2025
section_ids:
  errors: Errors
  warnings: Warnings
---

# Flow Validation Rules

## Errors

The following errors can be identified by flow validation:

| Error                                                                                      | Description                                                                                                                                                                                                                                                   |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Flow is empty**                                                                          | The flow does not contain any nodes.                                                                                                                                                                                                                          |
| **Flow has multiple start points or a floating node**                                      | There are multiple nodes that could act as starting points for the flow.                                                                                                                                                                                      |
| **Disabled node found**                                                                    | The flow contains one or more disabled nodes, which can cause issues when a flow is run.                                                                                                                                                                      |
| **Subflow configuration error**                                                            | The flow launches a subflow, but the subflow or subflow version are not valid.                                                                                                                                                                                |
| **Circular subflow dependency found**                                                      | The flow launches a subflow, but that subflow launches the parent flow, creating an infinite loop.                                                                                                                                                            |
| **Unused variable found**                                                                  | A flow instance variable is defined by a variable connector but is not used in the flow.                                                                                                                                                                      |
| **Undefined variable found**                                                               | A variable that is not defined in the flow is being referenced.                                                                                                                                                                                               |
| **Subflow input schema missing**                                                           | The flow launches a subflow, but the flow conductor node does not provide one or more values that are required by the subflow input schema.                                                                                                                   |
| **Incorrect ending nodes for PingOne flow**                                                | The flow is a PingOne flow, but it includes branches that do not conclude with a PingOne Authentication connector node using either the **Return Success Response (Redirect Flows)** capability or the **Return Error Response (Redirect Flows)** capability. |
| **Form not selected**                                                                      | The flow includes a **Forms** connector node that doesn't have a form selected.                                                                                                                                                                               |
| **Connector capability not configured**                                                    | The flow contains a node that does not have a selected capability.                                                                                                                                                                                            |
| **Referenced node in local variable doesn't exist**                                        | The flow contains a node that references a value from an unavailable node ID.                                                                                                                                                                                 |
| **Invalid subflow configuration: PingOne flow selected as subflow.**                       | The subflow configured in the flow connector is a PingOne flow. PingOne flows cannot be used as subflows.                                                                                                                                                     |
| **Invalid configurations for 'A == B (Multiple Conditions)' capability**                   | A functions connector node using the 'A == B (Multiple Conditions)' capability doesn't have defined outcomes. Define at least one expected outcome value.                                                                                                     |
| **Missing target node in 'Go to Node' capability**                                         | A teleport node is missing a destination.                                                                                                                                                                                                                     |
| **Input schema missing for teleport node.**                                                | A teleport node is missing an input schema.                                                                                                                                                                                                                   |
| **"Expire Flow Instance Cache" enabled in an intermediate node**                           | The **Expire Flow Instance Cache** setting is enabled on a node that's not an end node. When this setting is enabled on an intermediate node, it can cause functions such as localization to fail.                                                            |
| **Incorrect "Additional Fields in the Response" in Send Success JSON Response capability** | The **Send Success JSON Response** node has an incorrect configuration in the additional fields included in the response. Make sure that a key and value are provided for each additional field, or remove any additional field that aren't necessary.        |
| **Incorrect "Additional Fields in the Response" in Send Error JSON Response capability**   | The **Send Error JSON Response** node has an incorrect configuration in the additional fields included in the response. Make sure that a key and value are provided for each additional field, or remove any additional field that aren't necessary.          |
| **Unsupported false branch after teleport node**                                           | A teleport node includes a false exit branch. Only true branches are valid after a teleport node.                                                                                                                                                             |
| **Missing site key configuration for reCAPTCHA**                                           | A reCAPTCHA component within an HTML node needs to have a site key configured.                                                                                                                                                                                |
| **Missing "Property Name" for Output Fields in Custom HTML Template capability**           | A Custom HTML Template node is missing keys for one or more output fields. You must add keys if you plan to launch the flow using the Ping SDKs.                                                                                                              |

## Warnings

The following warnings can be identified by flow validation:

| Error                                                                        | Description                                                                                                                                                                                                                                                                                                                                                                          |
| ---------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Log level set to Debug**                                                   | The log level for the flow is set to **Debug**. You should only use this log level if you are actively troubleshooting an issue. Learn more in [Editing flow settings](davinci_editing_flow_settings.html).                                                                                                                                                                          |
| **Missing node title**                                                       | A node has no title, which makes identifying the node challenging.                                                                                                                                                                                                                                                                                                                   |
| **Missing node description**                                                 | A node has no description, which makes identifying the node's purpose challenging.                                                                                                                                                                                                                                                                                                   |
| **Incorrect node color**                                                     | A **Send Success Response** or **Send Error Response** node does not have the recommended node color. Using a consistent color for these nodes makes it easier to identify the flow's endpoints.                                                                                                                                                                                     |
| **Invalid output mapping for 'A == B (Multiple Conditions)' capability**     | A functions connector node using the 'A == B (Multiple Conditions)' capability has an invalid output mapping. Each defined outcome should be mapped to the next node, and the high level function connector node should not be mapped to another node.                                                                                                                               |
| **Unmapped outcome(s) in 'A == B (Multiple Conditions)' capability**         | A functions connector node is missing one or more outcomes.                                                                                                                                                                                                                                                                                                                          |
| **"Invoke UI Subflow" capability used, but target subflow has no UI nodes.** | The **Invoke UI Subflow** capability is being used to target a subflow that does not have a UI node as the first node of the subflow. Use the **Invoke Subflow** capability instead if the flow has no UI component.If the flow has a UI component but this error appears, include a hidden UI node as the first node in the flow to prevent the error and prevent subflow timeouts. |