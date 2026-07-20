---
title: Password reset
description: Configure the Advanced Identity Cloud password reset journey to let end users reset their password by email verification without administrator help
component: pingoneaic
page_id: pingoneaic:self-service:password-reset
canonical_url: https://docs.pingidentity.com/pingoneaic/self-service/password-reset.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Accounts", "Journeys", "Password Reset"]
section_ids:
  reset-password-rest-sample: Example reset password REST output
---

# Password reset

Password reset lets end users reset their password without assistance from an administrator.

PingOne Advanced Identity Cloud includes a **ResetPassword** journey template, which requests an end user's email address, checks if an end user with that email exists, and if so, emails a reset link to the end user. The journey then waits until the end user clicks the link before presenting a password reset prompt.

![Sample password reset journey](_images/PlatformResetPassword.png)

|   |                                                                                                                                                                   |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Make sure the [Patch Object node](https://docs.pingidentity.com/auth-node-ref/latest/patch-object.html)'s Patch As Object field is not selected (set to `false`). |

## Example reset password REST output

When calling a reset password self-service endpoint, you will receive a JSON object back, containing callbacks for each of the nodes included in the reset password journey.

> **Collapse: Sample JSON callbacks**
>
> ```json
> {
>   "authId": "<omitted for length>",
>   "callbacks": [
>     {
>       "type": "StringAttributeInputCallback",
>       "output": [
>         {
>           "name": "name",
>           "value": "mail"
>         },
>         {
>           "name": "prompt",
>           "value": "Email Address"
>         },
>         {
>           "name": "required",
>           "value": true
>         },
>         {
>           "name": "policies",
>           "value": {}
>         },
>         {
>           "name": "failedPolicies",
>           "value": []
>         },
>         {
>           "name": "validateOnly",
>           "value": false
>         },
>         {
>           "name": "value",
>           "value": ""
>         }
>       ],
>       "input": [
>         {
>           "name": "IDToken1",
>           "value": ""
>         },
>         {
>           "name": "IDToken1validateOnly",
>           "value": false
>         }
>       ],
>       "_id": 0
>     }
>   ],
>   "header": "Reset Password",
>   "description": "Enter your email address or <a href=\"#/service/Login\">Sign in</a>"
> }
> ```

---

---
title: Password update
description: Configure the Advanced Identity Cloud password update journey to let signed-in end users change their own password without administrator assistance
component: pingoneaic
page_id: pingoneaic:self-service:update-password
canonical_url: https://docs.pingidentity.com/pingoneaic/self-service/update-password.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Accounts", "Journeys", "Nodes &amp; Trees", "Update Passwords"]
---

# Password update

Password update lets end users update their passwords without assistance from an administrator.

PingOne Advanced Identity Cloud includes an **UpdatePassword** journey template. Unlike the other self-service journey templates, the update password journey assumes the end user is already signed on and gets the end user's current session data to identify the end user. It then presents a prompt to update the end user's password and uses a [Patch Object node](https://docs.pingidentity.com/auth-node-ref/latest/patch-object.html) to update the password. An example of where you might use a journey like this is in an update password link placed in the end user's profile or settings.

![Sample update password journey](_images/PlatformUpdatePassword.png)

|   |                                                                                                                                                                               |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Make sure that the [Patch Object node](https://docs.pingidentity.com/auth-node-ref/latest/patch-object.html)'s Patch As Object field is not selected (equivalent to `false`). |

To let end users update their password through the hosted account pages profile page using the Reset link, you set a self-service tree for the password update journey. The default journey is UpdatePassword.

To change the journey for password updates:

1. In the Advanced Identity Cloud admin console, select Native Consoles > Access Management.

2. In the left navigation pane, click Services.

3. Select Self Service Trees.

4. In the updatePassword field, update the name of the journey.

5. Click Save Changes.

---

---
title: Progressive profile
description: Configure Advanced Identity Cloud progressive profiling to collect additional end-user profile information over time using journey decision nodes
component: pingoneaic
page_id: pingoneaic:self-service:progressive-profile
canonical_url: https://docs.pingidentity.com/pingoneaic/self-service/progressive-profile.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Journeys", "Nodes &amp; Trees", "Progressive Profiles"]
---

# Progressive profile

Progressive profiling lets end users provide additional profile information over time or update existing information when needed.

PingOne Advanced Identity Cloud includes a **ProgressiveProfile** journey template that checks the number of sign ons, and prompts the end user to add their marketing preferences if they haven't already. However, there are many other ways to configure a progressive profile flow to suit your needs.

Progressive profile journeys generally aren't directly linked. Instead, they are included inside other journeys, using the [Inner Tree Evaluator node](https://docs.pingidentity.com/auth-node-ref/latest/inner-tree-evaluator.html). You can connect multiple Inner Tree Evaluator nodes together, which can help you keep different progressive profile behaviors organized into their own journeys.

![Sample progressive profile journey](_images/PlatformProgressiveProfile.png)

The following nodes are associated with progressive profiles:

* [Attribute Present Decision node](https://docs.pingidentity.com/auth-node-ref/latest/attribute-present-decision.html)

  The [Attribute Present Decision node](https://docs.pingidentity.com/auth-node-ref/latest/attribute-present-decision.html) checks whether the specified attribute is present. It doesn't check the value of the attribute, only that the attribute exists. This can include attributes that might otherwise be private. A common use case for this node is when you want to check for the presence of a password.

* [Attribute Value Decision node](https://docs.pingidentity.com/auth-node-ref/latest/attribute-value-decision.html)

  The [Attribute Value Decision node](https://docs.pingidentity.com/auth-node-ref/latest/attribute-value-decision.html) checks the value of the specified attribute, and determines if it satisfies the conditions configured in the node. It can perform the following comparison operations:

  * Check whether an attribute is present.

  * Check whether the value of an attribute equals a value specified in the node.

  Like the [Attribute Present Decision node](https://docs.pingidentity.com/auth-node-ref/latest/attribute-present-decision.html), one of the possible conditions you can set is whether an attribute is present. Unlike the Attribute Present Decision node, this doesn't work on private attributes.

* [KBA Decision node](https://docs.pingidentity.com/auth-node-ref/latest/kba-decision.html)

  The [KBA Decision node](https://docs.pingidentity.com/auth-node-ref/latest/kba-decision.html) is primarily used in a progressive profile journey where you want to ensure an end user has defined answers to the minimum number of questions required by the system. This can be useful if the number of questions changes, so the end user can be prompted for any necessary additional responses when they next log in. In this case, the [KBA Decision node](https://docs.pingidentity.com/auth-node-ref/latest/kba-decision.html) would be used together with the [KBA Definition node](https://docs.pingidentity.com/auth-node-ref/latest/kba-definition.html): if the [KBA Decision node](https://docs.pingidentity.com/auth-node-ref/latest/kba-decision.html) evaluates false, the end user would then be taken to the [KBA Definition node](https://docs.pingidentity.com/auth-node-ref/latest/kba-definition.html).

* [Login Count Decision node](https://docs.pingidentity.com/auth-node-ref/latest/login-count-decision.html)

  The [Login Count Decision node](https://docs.pingidentity.com/auth-node-ref/latest/login-count-decision.html) checks whether the end user has signed on the specified number of times. It can be triggered once (using the `AT` interval) or triggered repeatedly after a set number of sign ons (using the `EVERY` interval). The sign-on count is not automatically incremented: be sure to include the [Increment Login Count node](https://docs.pingidentity.com/auth-node-ref/latest/increment-login-count.html) in your sign-on journey if you plan to use this node.

* [Profile Completeness Decision node](https://docs.pingidentity.com/auth-node-ref/latest/profile-completeness-decision.html)

  The [Profile Completeness Decision node](https://docs.pingidentity.com/auth-node-ref/latest/profile-completeness-decision.html) checks how complete an end user's profile is, and compares that amount with a percentage value set in the node. The value for profile completeness is based on the number of visible, user-editable attributes in their profile that have been filled out.

* [Query Filter Decision node](https://docs.pingidentity.com/auth-node-ref/latest/query-filter-decision.html)

  The [Query Filter Decision node](https://docs.pingidentity.com/auth-node-ref/latest/query-filter-decision.html) uses a query filter to check an end user's profile for specific information. Use this to check whether a particular field has been filled out or that the contents of a field match a specific pattern. For example, you can use this in progressive profile journeys to check if marketing preferences are set on an end user's profile. Learn more about constructing effective query filters in [Construct queries](../idm-objects/queries.html#constructing-queries).

* [Terms and Conditions Decision node](https://docs.pingidentity.com/auth-node-ref/latest/terms-and-conditions-decision.html)

  The [Terms and Conditions Decision node](https://docs.pingidentity.com/auth-node-ref/latest/terms-and-conditions-decision.html) verifies the end user has accepted the currently active set of terms and conditions. Use this node when you want to verify the end user has accepted your current terms and conditions before proceeding. Use this with the [Accept Terms and Conditions node](https://docs.pingidentity.com/auth-node-ref/latest/accept-terms-and-conditions.html): connect the [Terms and Conditions Decision node](https://docs.pingidentity.com/auth-node-ref/latest/terms-and-conditions-decision.html) False output to an [Accept Terms and Conditions node](https://docs.pingidentity.com/auth-node-ref/latest/accept-terms-and-conditions.html).

* [Time Since Decision node](https://docs.pingidentity.com/auth-node-ref/latest/time-since-decision.html)

  The [Time Since Decision node](https://docs.pingidentity.com/auth-node-ref/latest/time-since-decision.html) checks the end user's creation date against a specified amount of time. This is used when you want to have a time-based reminder for end users to check an attribute. Once the specified amount of time has elapsed, the node evaluates to `True` the next time the node is triggered, for example, by the end user signing on and going through a progressive profile journey.

---

---
title: Scripting tips
description: Access managed object attributes in Advanced Identity Cloud journey scripts using the objectAttributes object in Scripted Decision nodes
component: pingoneaic
page_id: pingoneaic:self-service:scripting-for-user-self-service
canonical_url: https://docs.pingidentity.com/pingoneaic/self-service/scripting-for-user-self-service.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Journeys", "Nodes &amp; Trees", "Shared State", "Scripts"]
section_ids:
  access_idm_properties_in_scripts: Access IDM properties in scripts
---

# Scripting tips

## Access IDM properties in scripts

User self-service journeys primarily use PingIDM nodes.

Nodes save data in the shared state of journeys. PingIDM nodes save data in the shared state differently than other nodes.

You can extend the functionality of journeys using scripts you write in the [Scripted Decision node](https://docs.pingidentity.com/auth-node-ref/latest/scripted-decision.html).

When you use a [Scripted Decision node](https://docs.pingidentity.com/auth-node-ref/latest/scripted-decision.html) node to access properties saved in the shared state by PingIDM nodes, you must reference the IDM properties using the `objectAttributes` object.

For example, to access the first name (`givenName`) from the shared state, returned from an PingIDM node, you would use the syntax:

```js
var firstName = objectAttributes.get("givenName").asString();
```

Find information on accessing [IDM properties](../identities/user-identity-properties-attributes-reference.html#reference-tables) in scripts and the shared state in [auth scripting](../developer-docs/scripting-auth.html).

---

---
title: Sign-on (login)
description: Configure the Advanced Identity Cloud sign-on journey with credential validation, retry limits, account lockout, and social identity provider support
component: pingoneaic
page_id: pingoneaic:self-service:login
canonical_url: https://docs.pingidentity.com/pingoneaic/self-service/login.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Journeys", "Nodes &amp; Trees", "Social Authentication"]
section_ids:
  social-login: Configure social identity providers
  example_social_sign_on_journey: Example social sign-on journey
  login-rest-sample: Example login REST output
---

# Sign-on (login)

The PingOne Advanced Identity Cloud sign-on flow is designed for self-service, as demonstrated in the **Login** journey template. This journey lets end users sign on using their Advanced Identity Cloud credentials and increments the login counter. A separate retry-limit counter tracks failed authentications and locks the end-user account if the number of retries exceeds a specified limit. End users who successfully authenticate are sent through a separate [progressive profile journey](progressive-profile.html).

|   |                                                                                                                                                                                    |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The **Login** journey template can be extended to include other features, such as support for identity providers. Learn more in [Social authentication](social-registration.html). |

![Example sign-on journey](_images/idcloud-login-journey.png)

The following nodes are associated with sign-on journeys:

* [Platform Username node](https://docs.pingidentity.com/auth-node-ref/latest/platform-username.html)

  The [Platform Username node](https://docs.pingidentity.com/auth-node-ref/latest/platform-username.html) is used in both sign-on and registration journeys. It collects the end user's username.

* [Platform Password node](https://docs.pingidentity.com/auth-node-ref/latest/platform-password.html)

  The [Platform Password node](https://docs.pingidentity.com/auth-node-ref/latest/platform-password.html) is used in both sign-on and registration journeys. It collects the end user's password.

* [Identity Store Decision node](https://docs.pingidentity.com/auth-node-ref/latest/cloud/identity-store-decision.html)

  The [Identity Store Decision node](https://docs.pingidentity.com/auth-node-ref/latest/cloud/identity-store-decision.html) takes a username and password and validates they match an existing end user in the identity store.

* [Retry Limit Decision node](https://docs.pingidentity.com/auth-node-ref/latest/retry-limit-decision.html)

  The [Retry Limit Decision node](https://docs.pingidentity.com/auth-node-ref/latest/retry-limit-decision.html) tracks failed authentications. If the number of failed authentications is below a specified Retry Limit, the end user can attempt authentication again. Otherwise, the node forwards to the [Account Lockout node](https://docs.pingidentity.com/auth-node-ref/latest/account-lockout.html) to lock the end-user account.

  ![node retry limit decision configuration](_images/node-retry-limit-decision-configuration.png)

* [Account Lockout node](https://docs.pingidentity.com/auth-node-ref/latest/account-lockout.html)

  The [Account Lockout node](https://docs.pingidentity.com/auth-node-ref/latest/account-lockout.html) sets the lock state of the end-user account. In this case, it is configured to lock the account. The node can also be used in a separate unlock journey to unlock the end-user account.

  ![node account lockout configuration](_images/node-account-lockout-configuration.png)

## Configure social identity providers

To include social identity providers as a method of authentication, configure the Social Identity Provider service to include some form of social registration or social account claiming. Learn more in [Social authentication](social-registration.html). After this is set up, add social identity provider support to your sign-on journey.

To get started with social sign ons, you can create a new journey, modify an existing sign-on journey, or duplicate the **Login** journey template and modify that.

### Example social sign-on journey

This example uses the following nodes:

* A [Page node](https://docs.pingidentity.com/auth-node-ref/latest/page.html) containing:

  * A [Platform Username node](https://docs.pingidentity.com/auth-node-ref/latest/platform-username.html).

  * A [Platform Password node](https://docs.pingidentity.com/auth-node-ref/latest/platform-password.html).

  * A [Select Identity Provider node](https://docs.pingidentity.com/auth-node-ref/latest/select-identity-provider.html).

* A [Social Provider Handler node](https://docs.pingidentity.com/auth-node-ref/latest/social-provider-handler.html).

* A [Data Store Decision node](https://docs.pingidentity.com/auth-node-ref/latest/data-store-decision.html).

* An [Increment Login Count node](https://docs.pingidentity.com/auth-node-ref/latest/increment-login-count.html).

* An [Inner Tree Evaluator node](https://docs.pingidentity.com/auth-node-ref/latest/inner-tree-evaluator.html).

To create the journey:

1. Connect the starting node to the [Page node](https://docs.pingidentity.com/auth-node-ref/latest/page.html).

2. Connect the Social Authentication output on the [Page node](https://docs.pingidentity.com/auth-node-ref/latest/page.html) to the [Social Provider Handler node](https://docs.pingidentity.com/auth-node-ref/latest/social-provider-handler.html).

3. On the [Social Provider Handler node](https://docs.pingidentity.com/auth-node-ref/latest/social-provider-handler.html), connect the Account Exists output to the [Increment Login Count node](https://docs.pingidentity.com/auth-node-ref/latest/increment-login-count.html). Connect the No Account Exists output to the Failure node.

4. On the [Page node](https://docs.pingidentity.com/auth-node-ref/latest/page.html), connect the Local Authentication node to the [Data Store Decision node](https://docs.pingidentity.com/auth-node-ref/latest/data-store-decision.html).

5. On the [Data Store Decision node](https://docs.pingidentity.com/auth-node-ref/latest/data-store-decision.html), connect the True output to the [Increment Login Count node](https://docs.pingidentity.com/auth-node-ref/latest/increment-login-count.html). Connect the False output to the Failure node.

6. Connect the [Increment Login Count node](https://docs.pingidentity.com/auth-node-ref/latest/increment-login-count.html) to the [Inner Tree Evaluator node](https://docs.pingidentity.com/auth-node-ref/latest/inner-tree-evaluator.html) node.

7. The [Inner Tree Evaluator node](https://docs.pingidentity.com/auth-node-ref/latest/inner-tree-evaluator.html) points to another journey, letting you chain multiple journeys together.

   By default, this is set to point to the `ProgressiveProfile` journey. Learn more about progressive profiles in [Progressive profile](progressive-profile.html).

   Connect the [Inner Tree Evaluator node](https://docs.pingidentity.com/auth-node-ref/latest/inner-tree-evaluator.html) node to the Success node.

The resulting journey looks similar to this:

![Example login journey with social identity providers enabled](_images/social-login.png)

## Example login REST output

Calling a login self-service endpoint returns a JSON object containing callbacks for each of the nodes included in the journey.

> **Collapse: Sample JSON callbacks**
>
> ```json
> {
>   "authId": "<omitted for length>",
>   "callbacks": [
>     {
>       "type": "ValidatedCreateUsernameCallback",
>       "output": [
>         {
>           "name": "policies",
>           "value": {}
>         },
>         {
>           "name": "failedPolicies",
>           "value": []
>         },
>         {
>           "name": "validateOnly",
>           "value": false
>         },
>         {
>           "name": "prompt",
>           "value": "Username"
>         }
>       ],
>       "input": [
>         {
>           "name": "IDToken1",
>           "value": ""
>         },
>         {
>           "name": "IDToken1validateOnly",
>           "value": false
>         }
>       ],
>       "_id": 0
>     },
>     {
>       "type": "ValidatedCreatePasswordCallback",
>       "output": [
>         {
>           "name": "echoOn",
>           "value": false
>         },
>         {
>           "name": "policies",
>           "value": {}
>         },
>         {
>           "name": "failedPolicies",
>           "value": []
>         },
>         {
>           "name": "validateOnly",
>           "value": false
>         },
>         {
>           "name": "prompt",
>           "value": "Password"
>         }
>       ],
>       "input": [
>         {
>           "name": "IDToken2",
>           "value": ""
>         },
>         {
>           "name": "IDToken2validateOnly",
>           "value": false
>         }
>       ],
>       "_id": 1
>     }
>   ],
>   "header": "Sign In",
>   "description": "New here? <a href=\"#/service/Registration\">Create an account</a><br><a href=\"#/service/ForgottenUsername\">Forgot username?</a> <a href=\"#/service/ResetPassword\">Forgot password?</a>"
> }
> ```

---

---
title: Social authentication
description: Configure Advanced Identity Cloud social authentication with OAuth 2.0 or OIDC identity providers, including account claiming and journey setup
component: pingoneaic
page_id: pingoneaic:self-service:social-registration
canonical_url: https://docs.pingidentity.com/pingoneaic/self-service/social-registration.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Journeys", "Nodes &amp; Trees", "Social Authentication", "OAuth 2.0", "OpenID Connect (OIDC)"]
section_ids:
  configure-social-providers: Configure social identity providers
  default-social-providers: Default social identity provider configurations
  custom-social-providers: Custom social identity provider configurations
  configure-idp: Add identity providers
  basic-social-registration: Configure basic social registration journeys
  basic-reg-tree: Set up a basic social registration journey
  account-claiming: Configure social registration with account claiming
  social-auth-connect-through-profile: Let users connect through their profile page
---

# Social authentication

You can configure user self-registration to include social identity providers as an option for users. This lets end users register and sign on to Advanced Identity Cloud using an account they have through another trusted service.

The following diagram illustrates the social login flow.

![A user authenticating with Advanced Identity Cloud using a social identity provider.](_images/social-login-flow.svg)

## Configure social identity providers

Advanced Identity Cloud supports social identity providers that are OAuth 2.0 or OpenID Connect (OIDC) 1.0-compliant.

### Default social identity provider configurations

A number of social identity providers are configured by default:

| Identity provider     | Specification | Configuration ID    |
| --------------------- | ------------- | ------------------- |
| Amazon                | OAuth 2.0     | `amazonConfig`      |
| Apple                 | OIDC          | `appleConfig`       |
| Facebook              | OAuth 2.0     | `facebookConfig`    |
| Google                | OIDC          | `googleConfig`      |
| Instagram             | OAuth 2.0     | `instagramConfig`   |
| LINE (Browser)        | OIDC          | `lineBrowserConfig` |
| LINE (Native)         | OIDC          | `lineNativeConfig`  |
| LinkedIn (Legacy) (2) | OAuth 2.0     | `linkedInConfig`    |
| LinkedIn              | OIDC          | `linkedInV2Config`  |
| Microsoft             | OAuth 2.0     | `microsoftConfig`   |
| Salesforce            | OAuth 2.0     | `salesforceConfig`  |
| Twitter               | OAuth 2.0     | `twitterConfig`     |
| VK (Vkontakte)        | OAuth 2.0     | `vkConfig`          |
| WeChat                | OAuth 2.0     | `weChatConfig`      |
| WordPress             | OAuth 2.0     | `wordpressConfig`   |
| Yahoo                 | OIDC          | `yahooConfig`       |
| itsme(1)              | OIDC          | `itsmeConfig`       |

(1) To integrate with [itsme](https://www.itsme.be/en/), you must obtain an Organization Validation (OV) certificate.

(2) The OAuth 2.0 version of the profile is [deprecated by LinkedIn](https://learn.microsoft.com/en-us/linkedin/consumer/integrations/self-serve/sign-in-with-linkedin).

### Custom social identity provider configurations

You can add providers that aren't configured by default, as long as these providers use OAuth 2.0 or OpenID Connect:

| Identity provider                                                         | Specification | Configuration ID |
| ------------------------------------------------------------------------- | ------------- | ---------------- |
| Any social identity provider that implements the OAuth 2.0 specification. | OAuth 2.0     | `oauth2Config`   |
| Any social identity provider that implements the OIDC specification.      | OIDC          | `oidcConfig`     |

### Add identity providers

1. Register a service in the identity provider, and keep the provider's documentation within reach. You will use it during this procedure.

   At minimum, you must have a client ID and a redirect URL.

   |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
   | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | A *redirect URL* is a path in Advanced Identity Cloud where the identity provider redirects the end user on successful authentication. Set it to the tenant's access management base URL, without appending any realm or journey query parameters. For example, https\://\<tenant-env-fqdn>/am.The hosted journey pages store the realm, journey, and authentication session in the browser's local storage so Advanced Identity Cloud can resume the correct flow when the identity provider redirects back. Adding parameters to the redirect URL breaks the flow\.Depending on the social identity provider and on your environment, you can change the redirect URL later.The redirect URL in the identity provider service and in the Advanced Identity Cloud client configuration must match. |

   |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
   | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | Some providers require you to enable a specific setting or API in their service:- Google

     Enable the `Gmail API` in the Google Cloud Platform.

   - Apple

     You must have access to the Apple Development Program (Enterprise program isn't eligible), and you must enable `Sign In With Apple` in the Apple Developer site.

   - LINE

     You must apply for permission for your LINE channel to access a user's email address using OIDC:

     1. In the LINE Developers console, enable Email address permission.

     2. Agree to the terms and conditions, and follow the steps to complete the application.

     3. The console displays `Applied` when your application is accepted.

     If you don't have email permission, the registration will fail with an `Invalid Attribute Syntax` error. |

2. In the Advanced Identity Cloud admin console, go to Native Consoles > Access Management > *Realm Name* > Services.

3. Click Social Identity Provider Service.

4. Go to the Secondary Configurations tab.

   Advanced Identity Cloud includes scripts and configurations for several common identity providers.

5. In the Add a Secondary Configuration drop-down list, select the required identity provider.

   If the required provider doesn't appear, select one of the following to add a custom identity provider client:

   * Client Configuration for providers that implement the OAuth2 specification

   * Client Configuration for providers that implement the OpenID Connect specification

6. Provide the client's required configuration details, such as the Client ID, Client Secret (for confidential clients), the Scope Delimiter (usually an empty space), and the Redirect URL.

   |   |                                                                                                                                                                                                                                                                                                                                    |
   | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | For OAuth 2.0 social identity providers, store the client secret in a secret store for greater security.Use the Client Secret Label Identifier to create a dynamic secret label to map to an alias for the secret.Learn more about secrets in [Use ESVs for signing and encryption keys](../tenants/esvs-signing-encryption.html). |

   Don't worry if some details are missing. You can edit the configuration later after saving the client profile for the first time.

   Save your changes to access all the configuration fields for the client.

7. Provide the client's advanced configuration details, and edit any required configuration details if needed.

   To find the required identity provider information:

   * Refer to the provider's documentation.

     Providers must specify their integration needs in their documentation, as well as their API endpoints.

     For example, providers usually have different scopes that you can configure depending on your service's needs.

     Financial-grade providers usually also require additional security-related configuration, such as `acr` values, PKCE-related settings, and more.

     Keep their documentation close while configuring the client profile.

   * Visit the provider's `.well-known` endpoint.

     OAuth 2.0/OpenID Connect-compliant providers will display much of the information you need to configure the identity provider client in their `.well-known` endpoint. For example, the endpoint should expose their endpoint URLs, and the signing and encryption algorithms they support.

     Advanced Identity Cloud is preconfigured, but you must make sure the settings for the provider haven't changed. Key preconfigured fields include:

     * The provider's URLs.

       For example, Authentication Endpoint URL, Access Token Endpoint URL, and User Profile Service URL.

     * The OAuth Scopes field.

     * The Well Known Endpoint for retrieving information about the provider.

       |   |                                                                |
       | - | -------------------------------------------------------------- |
       |   | Leave this field empty for the `LINE (Browser)` configuration. |

     * The configuration in the UI Config Properties section.

     * The script selected in the Transform Script drop-down list.

       This script is responsible for mapping attributes provided by the identity providers to a profile format compatible with Advanced Identity Cloud .

       Find more information in [Transform Script](../am-authentication/social-idp-client-reference.html#transform-script).

     |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
     | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
     |   | Some features require choosing algorithms from those supported by the provider, as well as creating secrets. Consider the following points before configuring the client:* Several capabilities in the identity provider client share the same secret IDs. For example, signing request objects and signing client authentication JWTs.

     * Every identity provider client in a realm shares the same secrets.Therefore, ensure that you configure features requiring secrets in a way that they are compatible across clients in the same realm.Find more information in [/oauth2/connect/rp/jwk\_uri](../am-oidc1/managing-rp-jwk_uri.html). |

     Learn more about client configuration settings in [Client configuration reference](../am-authentication/social-idp-client-reference.html).

8. Save your changes.

   Proceed to [Configure basic social registration journeys](#basic-social-registration).

## Configure basic social registration journeys

There are two nodes associated with identity providers:

* [Select Identity Provider node](https://docs.pingidentity.com/auth-node-ref/latest/select-identity-provider.html)

  The [Select Identity Provider node](https://docs.pingidentity.com/auth-node-ref/latest/select-identity-provider.html) prompts the end user to select a social identity provider for registration or sign on or (optionally) to continue with local registration or sign on.

  When the end user selects a provider, the journey continues to the [Social Provider Handler node](https://docs.pingidentity.com/auth-node-ref/latest/social-provider-handler.html).

* [Social Provider Handler node](https://docs.pingidentity.com/auth-node-ref/latest/social-provider-handler.html)

  The [Social Provider Handler node](https://docs.pingidentity.com/auth-node-ref/latest/social-provider-handler.html) communicates with the selected provider and collects the information provided after the end user has authorized the service. It runs the provider's configured *normalization* script to map the information into a format that Advanced Identity Cloud can consume.

  Next, the node uses a *transformation* script provided by Advanced Identity Cloud called `Normalized Profile to Managed User` to transform the profile information into a managed object.

  The node then queries the identity store available for the realm to check whether the end user already exists. If the user exists, they are signed on. If the user does not exist, the user must be created.

### Set up a basic social registration journey

1. In your realm, go to Journeys.

   You can create a new journey, modify an existing journey, or duplicate an existing journey.

2. Decide whether end users can sign on with their local credentials, and add the relevant nodes to the journey:

   * Social authentication journeys allowing local authentication might look like the following:

     ![Example social authentication with local authentication](_images/social-registration.png)

   * Social authentication journeys enforcing social authentication sign on might look like the following:

     ![Example social authentication enforcing social login](_images/social-registration-only.png)

   To configure either option, set Include local authentication in the [Select Identity Provider node](https://docs.pingidentity.com/auth-node-ref/latest/select-identity-provider.html). To support both local and social authentication in the same page, use the [Page node](https://docs.pingidentity.com/auth-node-ref/latest/page.html) as shown in the example.

3. Configure the [Social Provider Handler node](https://docs.pingidentity.com/auth-node-ref/latest/social-provider-handler.html):

   * In the Transformation Script field, select `Normalized Profile to Managed User`. This script transforms the normalized identity provider's profile object into a format that Advanced Identity Cloud can use.

     Find information on the script and the available bindings in [normalized-profile-to-managed-user.js](../am-scripting/sample-scripts.html#normalized-profile-to-managed-user-js).

   * In Client Type, select `BROWSER` when using Advanced Identity Cloud admin console or Ping SDKs for JavaScript, or `NATIVE` when using the ForgeRock SDKs for Android or iOS.

4. Configure the [Required Attributes Present node](https://docs.pingidentity.com/auth-node-ref/latest/required-attributes-present.html) and the [Create Object node](https://docs.pingidentity.com/auth-node-ref/latest/create-object.html):

   In the Identity Resource fields of each, configure the relevant managed identity resource type, such as `managed/alpha_user`.

   |   |                                                                                                                                                                                                                         |
   | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | To check for the available managed identity resource types, go to Native Consoles > Identity Management, and open the Manage drop-down list.Identity managed object types are preceded by the [icon: user, set=fa]icon. |

5. Configure the [Attribute Collector node](https://docs.pingidentity.com/auth-node-ref/latest/attribute-collector.html) adding at least the `mail`, `givenName`, and `sn` attributes.

## Configure social registration with account claiming

If your end users have one or more social identity provider accounts, they can link them to the same Advanced Identity Cloud account.

The following example builds on the basic social registration journey shown in [Set up a basic social registration journey](#basic-reg-tree):

![Example social registration with account claiming](_images/social-registration-account-claiming.png)Figure 1. Example social registration with account claiming

The journey uses the [Identify Existing User node](https://docs.pingidentity.com/auth-node-ref/latest/identify-existing-user.html) to determine if the end user is already registered in Advanced Identity Cloud . By default, the node checks that the email address associated with the account is already registered in Advanced Identity Cloud.

Ensure that you configure the Transformation Script in the [Social Provider Handler node](https://docs.pingidentity.com/auth-node-ref/latest/social-provider-handler.html), and the Identity Resource field in the [Patch Object node](https://docs.pingidentity.com/auth-node-ref/latest/patch-object.html).

Refer to [Set up a basic social registration journey](#basic-reg-tree) for tips.

## Let users connect through their profile page

To let end users connect to social identity providers through the End User UI profile page, add a mapping for your social authentication journey:

1. From the Advanced Identity Cloud admin console, select Native Consoles > Access Management.

2. From the left navigation pane, click Services.

3. Select Self Service Trees.

4. Set a new key and value and click + Add:

   * Key

     `connectSocial`

   * Value

     The name of the journey

5. Click Save Changes.

---

---
title: User self-registration
description: Configure Advanced Identity Cloud user self-registration journeys with CAPTCHA, security questions, terms and conditions, and privacy consent nodes
component: pingoneaic
page_id: pingoneaic:self-service:self-registration
canonical_url: https://docs.pingidentity.com/pingoneaic/self-service/self-registration.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Accounts", "Journeys", "Nodes &amp; Trees", "Social Authentication", "CAPTCHA", "Security Questions", "Terms &amp; Conditions"]
section_ids:
  captcha: CAPTCHA services
  security-questions: Security questions
  configuration: Configuration
  associated_nodes: Associated nodes
  terms-conditions: Terms and conditions
  configuration_2: Configuration
  associated_nodes_2: Associated nodes
  terms_and_conditions_content_formatting: Terms and conditions content formatting
  link_to_terms_and_conditions_content: Link to terms and conditions content
  privacy-consent: Privacy and consent
  configuration_3: Configuration
  associated_nodes_3: Associated nodes
  registration-rest-sample: Example registration REST output
---

# User self-registration

User self-registration lets your end users create their own accounts without assistance from an administrator.

PingOne Advanced Identity Cloud includes a **Registration** journey template that lets end users create their own account for an app or service.

![Example registration journey](_images/PlatformRegistration.png)

To configure self-registration in Advanced Identity Cloud, your registration journey requires at least the following nodes:

* [Platform Username node](https://docs.pingidentity.com/auth-node-ref/latest/platform-username.html)

  If you have changed the `userName` attribute to something else, you must configure this node to use the new attribute, for example, if you changed your configuration to use the `mail` attribute instead.

* [Attribute Collector node](https://docs.pingidentity.com/auth-node-ref/latest/attribute-collector.html)

  This collects information from the end user for any attributes that are required to create the end user profile.

  By default, required attributes include `userName`, `givenName`, `sn` (surname), and `mail` (email). The node can collect optional attributes as well, as long as any required attributes are collected.

* [Create Object node](https://docs.pingidentity.com/auth-node-ref/latest/create-object.html)

  This creates the end user in Advanced Identity Cloud.

All other nodes are optional. Some are strongly encouraged. For example, if you don't include a [Platform Password node](https://docs.pingidentity.com/auth-node-ref/latest/platform-password.html), the end user won't be able to enter a password to sign on. This node isn't always necessary, like when you provide another authentication method such as a social identity provider or when you generate a password for the end user.

Nodes that present or collect information each display on their own page by default. To collect multiple nodes into one page, place these nodes in a [Page node](https://docs.pingidentity.com/auth-node-ref/latest/page.html). There are some limitations to consider when adding nodes to a [Page node](https://docs.pingidentity.com/auth-node-ref/latest/page.html):

* Only add nodes that require interaction with the end user to a [Page node](https://docs.pingidentity.com/auth-node-ref/latest/page.html).

* At most, add one node with multiple possible outcomes in a [Page node](https://docs.pingidentity.com/auth-node-ref/latest/page.html).

* Do not add the [Email Suspend node](https://docs.pingidentity.com/auth-node-ref/latest/email-suspend.html) or the [Social Provider Handler node](https://docs.pingidentity.com/auth-node-ref/latest/social-provider-handler.html) to a [Page node](https://docs.pingidentity.com/auth-node-ref/latest/page.html).

Common nodes in a registration journey include:

* The [CAPTCHA node](https://docs.pingidentity.com/auth-node-ref/latest/captcha.html). Learn more in [CAPTCHA services](#captcha).

* The [KBA Definition node](https://docs.pingidentity.com/auth-node-ref/latest/kba-definition.html). Learn more in [Security questions](#security-questions).

* The [Accept Terms and Conditions node](https://docs.pingidentity.com/auth-node-ref/latest/accept-terms-and-conditions.html). Learn more in [Terms and conditions](#terms-conditions).

* The [Consent Collector node](https://docs.pingidentity.com/auth-node-ref/latest/consent-collector.html). Learn more in [Privacy and consent](#privacy-consent).

## CAPTCHA services

CAPTCHA is a way to challenge an end user to verify that they are human and includes a number of different services. Choose the CAPTCHA service that best suits your requirements. The default configuration in the [CAPTCHA node](https://docs.pingidentity.com/auth-node-ref/latest/captcha.html) is for Google's reCAPTCHA service. The node has been tested for use with reCAPTCHA v2 and hCaptcha v1. Other services should work, as long as they follow a similar configuration pattern.

You'll need to provide a CAPTCHA Site Key and CAPTCHA Secret Key. The rest of CAPTCHA configuration is done through the service that you are using.

## Security questions

Security questions let an end user provide answers to questions that can later be used to verify their identity. This process is also called Knowledge-Based Authentication (KBA).

### Configuration

To configure security questions:

1. In the Advanced Identity Cloud admin console, select Security > Security Questions. From here, you can configure the questions that are presented to end users and how they should be handled.

2. Click Add Question to set additional questions for the end user.

3. On the Add a Security Question modal:

   1. Select a locale, provide the question text for that locale, and click Done.

   2. To provide the question for different locales, click Add locale and repeat the previous step.

   3. Click Save.

4. On the Settings tab, set the following:

   * Must define refers to the minimum number of security questions the end user must set up during registration.

   * Must answer refers to the minimum number of questions the end user must answer to satisfy a security prompt.

|   |                                                                                                                                                                                               |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | After you deploy these security questions, don't remove or change existing questions because end users might already have included those questions during the user self-registration process. |

### Associated nodes

There are three nodes associated with KBA:

* [KBA Definition node](https://docs.pingidentity.com/auth-node-ref/latest/kba-definition.html)

  The [KBA Definition node](https://docs.pingidentity.com/auth-node-ref/latest/kba-definition.html) is used during registration. It prompts the end user to select security questions from a list and define answers to these questions for use during identity verification. The list includes an option for end users to define their own questions.

* [KBA Verification node](https://docs.pingidentity.com/auth-node-ref/latest/kba-verification.html)

  The [KBA Verification node](https://docs.pingidentity.com/auth-node-ref/latest/kba-verification.html) is used to verify an end user's identity using security questions, such as during a Reset Password journey. It displays the number of questions set in the Must Answer field in the Security Questions settings. If the end user has defined answers for more questions than required, the displayed questions are randomized.

* [KBA Decision node](https://docs.pingidentity.com/auth-node-ref/latest/kba-decision.html)

  The [KBA Decision node](https://docs.pingidentity.com/auth-node-ref/latest/kba-decision.html) is primarily used in cases of a Progressive Profile journey, where you ensure an end user has defined answers to the minimum number of questions required. This can be useful if the number of questions changes, so the end user can be prompted to complete additional questions when they next sign on. In this case, the [KBA Decision node](https://docs.pingidentity.com/auth-node-ref/latest/kba-decision.html) is used together with the [KBA Definition node](https://docs.pingidentity.com/auth-node-ref/latest/kba-definition.html). If the [KBA Decision node](https://docs.pingidentity.com/auth-node-ref/latest/kba-decision.html) evaluates false, the end user is directed to the [KBA Definition node](https://docs.pingidentity.com/auth-node-ref/latest/kba-definition.html).

## Terms and conditions

Terms and conditions display the terms and conditions for using your service. Configure the terms and conditions for using your service. These are not considered optional, and end users must accept the terms and conditions before they can progress in the account creation process.

### Configuration

To configure terms and conditions:

1. In the Advanced Identity Cloud admin console, select Terms & Conditions, and click + New Version.

2. Enter a version number for the new terms and conditions, then click Next.

   Terms and conditions are tracked using versioning. The default placeholder set of terms and conditions has a version of `0.0`, but the versioning can follow other patterns, such as dates.

3. Enter the locale for which these terms and conditions apply, expressed as its [ISO 639-1](https://www.loc.gov/standards/iso639-2/php/code_list.php) code (for example, `en` or `fr`), then click Add.

4. Enter the text of your terms and conditions:

   * Terms and conditions content is formatted using Markdown. You can also use HTML formatting, which is converted into Markdown when you save or publish. Learn more in [Terms and conditions content formatting](#terms_and_conditions_content_formatting).

     |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
     | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
     |   | When using HTML formatting, `id` and `style` attributes are stripped out when Advanced Identity Cloud converts the HTML formatting to Markdown. However, you can use the following techniques to emulate `id` and `style` attributes:- To link to different parts of the terms and conditions content, use the formatted header IDs in the HTML output. Learn more in [Link to terms and conditions content](#link_to_terms_and_conditions_content).

     - To apply CSS styles to the terms and conditions content, use the styles editor. |

   * Click Styles to switch to the styles editor. Then, enter additional CSS styles to apply to the HTML that is rendered from the Markdown.

   * The text supports localization. When you have added the terms and conditions for this locale, click Locale: locale-name, then click + Add locale to add the text for another locale.

   * Click Try it out to check how your terms and conditions appear to end users.

5. Save or publish the new version.

   |   |                                                                                                                                 |
   | - | ------------------------------------------------------------------------------------------------------------------------------- |
   |   | When you have published a version, the terms and conditions cannot be edited. Be sure to proofread your text before publishing. |

   * Click Save as Draft to save this version for future publication. You can edit a draft version.

   * Click Publish to publish this version.

     Select Set as Active Version to make this the active version of your terms and conditions. Only one version of terms and conditions can be active at a time, for each locale. Selecting this option will deactivate the currently active version, and make this version active instead.

### Associated nodes

There are two nodes associated with terms and conditions:

* [Accept Terms and Conditions node](https://docs.pingidentity.com/auth-node-ref/latest/accept-terms-and-conditions.html)

  The [Accept Terms and Conditions node](https://docs.pingidentity.com/auth-node-ref/latest/accept-terms-and-conditions.html) presents the end user with a notice that continuing means they agree with the terms and conditions you have set, along with a link to view the terms and conditions, and a button to continue. Because this node includes a button to continue by default, it should generally be the last node in a [Page node](https://docs.pingidentity.com/auth-node-ref/latest/page.html), or on its own page. The node uses the currently active version of the terms and conditions by default, so you don't need to specify the version in the node.

* [Terms and Conditions Decision node](https://docs.pingidentity.com/auth-node-ref/latest/terms-and-conditions-decision.html)

  The [Terms and Conditions Decision node](https://docs.pingidentity.com/auth-node-ref/latest/terms-and-conditions-decision.html) is used in progressive profile journeys, where you want to confirm that the end user has accepted the currently active terms and conditions. If you've updated the terms and conditions version, the decision evaluates to `false`. Connect this outcome to a [Accept Terms and Conditions node](https://docs.pingidentity.com/auth-node-ref/latest/accept-terms-and-conditions.html) to give the end user an opportunity to accept the new terms and conditions.

### Terms and conditions content formatting

The editor primarily uses Markdown to format the terms and conditions content.

You can also use HTML to add formatting to all or part of the content, but HTML is only a convenient input method, and the editor converts it to Markdown when you save or publish the content. This strips out any attributes in your HTML formatting, including `id` and `style` attributes.

|   |                                                                                                                                                                                                                    |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | Some HTML elements, such as definition lists, cannot be converted into Markdown, as there is no Markdown equivalent. These HTML elements are not converted and remain as HTML in the terms and conditions content. |

### Link to terms and conditions content

To display the terms and conditions content to the end user, the UI renders it from Markdown into HTML. When it renders the HTML output, it creates `id` attributes, but only on the header elements. To create a formatted value for each `id` attribute, it starts with the header element value, converts it to lowercase, and then removes spaces and special characters (except underscores).

Here are some examples:

| Markdown                          | Formatted header ID | HTML output                                                   |
| --------------------------------- | ------------------- | ------------------------------------------------------------- |
| `# Example 123`                   | `example123`        | `<h1 id="example123">Example 123</h1>`                        |
| `# Example!`                      | `example`           | `<h1 id="example">Example!</h1>`                              |
| `# Example -/=()%^&\*@£`          | `example`           | `<h1 id="example">Example -/=()%^&\*@£</h1>`                  |
| `# Example_1`                     | `example_1`         | `<h1 id="example_1">Example_1</h1>`                           |
| `# Example -/=()%^&\*@£_ Example` | `example_example`   | `<h1 id="example_example">Example -/=()%^&\*@£_ Example</h1>` |

To link to different parts of the terms and conditions content, you must therefore find the formatted header IDs in the HTML output and use them in your HTML anchors.

## Privacy and consent

In the context of registration and self-service, privacy and consent lets end users determine which external resources their information can be shared with, such as sales and marketing services. Advanced Identity Cloud manages these external resources as applications and lets you configure consent per application or mapping. The end user's information is *mapped* to the corresponding fields in the external service and is then synchronized. Learn more in [Resource mapping](../idm-synchronization/mappings.html).

### Configuration

To enable consent for a mapping:

1. In the Advanced Identity Cloud admin console, select Native Consoles > Identity Management.

2. Select Configure > Mappings, then select Edit on the mapping that you want to configure.

3. Select the Advanced tab, then enable Enable Privacy & Consent.

|   |                                                                                                                                                                                                                                                                 |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The above steps assume you have already created at least one mapping. You can also enable privacy and consent when creating the mapping. The same Enable Privacy & Consent switch is present when you click Create Mapping during the mapping creation process. |

### Associated nodes

There is one node associated with privacy and consent:

* [Consent Collector node](https://docs.pingidentity.com/auth-node-ref/latest/consent-collector.html)

  The [Consent Collector node](https://docs.pingidentity.com/auth-node-ref/latest/consent-collector.html) presents the end user with a list of all their mappings the user is affected by that have privacy and consent enabled. The end user can select or disable specific mappings. If you require all mappings to be allowed, there is an option in the node to make all mappings required.

  The node can be used during registration or during progressive profile journeys. If using this node in a progressive profile journey, you'll need to use the [Query Filter Decision node](https://docs.pingidentity.com/auth-node-ref/latest/query-filter-decision.html) to check for the presence of your desired mappings in the end user's `consentedMappings` attribute.

## Example registration REST output

When calling a registration self-service endpoint, you'll receive a JSON object back, containing callbacks for each of the nodes included in the registration journey.

> **Collapse: Sample JSON callbacks**
>
> ```json
> {
>   "authId": "<omitted for length>",
>   "callbacks": [
>     {
>       "type": "ValidatedCreateUsernameCallback",
>       "output": [
>         {
>           "name": "policies",
>           "value": {
>             "policyRequirements": [
>               "REQUIRED",
>               "MIN_LENGTH",
>               "VALID_TYPE",
>               "UNIQUE",
>               "CANNOT_CONTAIN_CHARACTERS"
>             ],
>             "fallbackPolicies": null,
>             "name": "userName",
>             "policies": [
>               {
>                 "policyRequirements": [
>                   "REQUIRED"
>                 ],
>                 "policyId": "required"
>               },
>               {
>                 "policyRequirements": [
>                   "REQUIRED"
>                 ],
>                 "policyId": "not-empty"
>               },
>               {
>                 "policyRequirements": [
>                   "MIN_LENGTH"
>                 ],
>                 "policyId": "minimum-length",
>                 "params": {
>                   "minLength": 1
>                 }
>               },
>               {
>                 "policyRequirements": [
>                   "VALID_TYPE"
>                 ],
>                 "policyId": "valid-type",
>                 "params": {
>                   "types": [
>                     "string"
>                   ]
>                 }
>               },
>               {
>                 "policyId": "unique",
>                 "policyRequirements": [
>                   "UNIQUE"
>                 ]
>               },
>               {
>                 "policyId": "no-internal-user-conflict",
>                 "policyRequirements": [
>                   "UNIQUE"
>                 ]
>               },
>               {
>                 "policyId": "cannot-contain-characters",
>                 "params": {
>                   "forbiddenChars": [
>                     "/"
>                   ]
>                 },
>                 "policyRequirements": [
>                   "CANNOT_CONTAIN_CHARACTERS"
>                 ]
>               }
>             ],
>             "conditionalPolicies": null
>           }
>         },
>         {
>           "name": "failedPolicies",
>           "value": []
>         },
>         {
>           "name": "validateOnly",
>           "value": false
>         },
>         {
>           "name": "prompt",
>           "value": "Username"
>         }
>       ],
>       "input": [
>         {
>           "name": "IDToken1",
>           "value": ""
>         },
>         {
>           "name": "IDToken1validateOnly",
>           "value": false
>         }
>       ],
>       "_id": 0
>     },
>     {
>       "type": "StringAttributeInputCallback",
>       "output": [
>         {
>           "name": "name",
>           "value": "givenName"
>         },
>         {
>           "name": "prompt",
>           "value": "First Name"
>         },
>         {
>           "name": "required",
>           "value": true
>         },
>         {
>           "name": "policies",
>           "value": {
>             "policyRequirements": [
>               "REQUIRED",
>               "VALID_TYPE"
>             ],
>             "fallbackPolicies": null,
>             "name": "givenName",
>             "policies": [
>               {
>                 "policyRequirements": [
>                   "REQUIRED"
>                 ],
>                 "policyId": "required"
>               },
>               {
>                 "policyRequirements": [
>                   "VALID_TYPE"
>                 ],
>                 "policyId": "valid-type",
>                 "params": {
>                   "types": [
>                     "string"
>                   ]
>                 }
>               }
>             ],
>             "conditionalPolicies": null
>           }
>         },
>         {
>           "name": "failedPolicies",
>           "value": []
>         },
>         {
>           "name": "validateOnly",
>           "value": false
>         },
>         {
>           "name": "value",
>           "value": ""
>         }
>       ],
>       "input": [
>         {
>           "name": "IDToken2",
>           "value": ""
>         },
>         {
>           "name": "IDToken2validateOnly",
>           "value": false
>         }
>       ],
>       "_id": 1
>     },
>     {
>       "type": "StringAttributeInputCallback",
>       "output": [
>         {
>           "name": "name",
>           "value": "sn"
>         },
>         {
>           "name": "prompt",
>           "value": "Last Name"
>         },
>         {
>           "name": "required",
>           "value": true
>         },
>         {
>           "name": "policies",
>           "value": {
>             "policyRequirements": [
>               "REQUIRED",
>               "VALID_TYPE"
>             ],
>             "fallbackPolicies": null,
>             "name": "sn",
>             "policies": [
>               {
>                 "policyRequirements": [
>                   "REQUIRED"
>                 ],
>                 "policyId": "required"
>               },
>               {
>                 "policyRequirements": [
>                   "VALID_TYPE"
>                 ],
>                 "policyId": "valid-type",
>                 "params": {
>                   "types": [
>                     "string"
>                   ]
>                 }
>               }
>             ],
>             "conditionalPolicies": null
>           }
>         },
>         {
>           "name": "failedPolicies",
>           "value": []
>         },
>         {
>           "name": "validateOnly",
>           "value": false
>         },
>         {
>           "name": "value",
>           "value": ""
>         }
>       ],
>       "input": [
>         {
>           "name": "IDToken3",
>           "value": ""
>         },
>         {
>           "name": "IDToken3validateOnly",
>           "value": false
>         }
>       ],
>       "_id": 2
>     },
>     {
>       "type": "StringAttributeInputCallback",
>       "output": [
>         {
>           "name": "name",
>           "value": "mail"
>         },
>         {
>           "name": "prompt",
>           "value": "Email Address"
>         },
>         {
>           "name": "required",
>           "value": true
>         },
>         {
>           "name": "policies",
>           "value": {
>             "policyRequirements": [
>               "REQUIRED",
>               "VALID_TYPE",
>               "VALID_EMAIL_ADDRESS_FORMAT"
>             ],
>             "fallbackPolicies": null,
>             "name": "mail",
>             "policies": [
>               {
>                 "policyRequirements": [
>                   "REQUIRED"
>                 ],
>                 "policyId": "required"
>               },
>               {
>                 "policyRequirements": [
>                   "VALID_TYPE"
>                 ],
>                 "policyId": "valid-type",
>                 "params": {
>                   "types": [
>                     "string"
>                   ]
>                 }
>               },
>               {
>                 "policyId": "valid-email-address-format",
>                 "policyRequirements": [
>                   "VALID_EMAIL_ADDRESS_FORMAT"
>                 ]
>               }
>             ],
>             "conditionalPolicies": null
>           }
>         },
>         {
>           "name": "failedPolicies",
>           "value": []
>         },
>         {
>           "name": "validateOnly",
>           "value": false
>         },
>         {
>           "name": "value",
>           "value": ""
>         }
>       ],
>       "input": [
>         {
>           "name": "IDToken4",
>           "value": ""
>         },
>         {
>           "name": "IDToken4validateOnly",
>           "value": false
>         }
>       ],
>       "_id": 3
>     },
>     {
>       "type": "BooleanAttributeInputCallback",
>       "output": [
>         {
>           "name": "name",
>           "value": "preferences/marketing"
>         },
>         {
>           "name": "prompt",
>           "value": "Send me special offers and services"
>         },
>         {
>           "name": "required",
>           "value": true
>         },
>         {
>           "name": "policies",
>           "value": {}
>         },
>         {
>           "name": "failedPolicies",
>           "value": []
>         },
>         {
>           "name": "validateOnly",
>           "value": false
>         },
>         {
>           "name": "value",
>           "value": false
>         }
>       ],
>       "input": [
>         {
>           "name": "IDToken5",
>           "value": false
>         },
>         {
>           "name": "IDToken5validateOnly",
>           "value": false
>         }
>       ],
>       "_id": 4
>     },
>     {
>       "type": "BooleanAttributeInputCallback",
>       "output": [
>         {
>           "name": "name",
>           "value": "preferences/updates"
>         },
>         {
>           "name": "prompt",
>           "value": "Send me news and updates"
>         },
>         {
>           "name": "required",
>           "value": true
>         },
>         {
>           "name": "policies",
>           "value": {}
>         },
>         {
>           "name": "failedPolicies",
>           "value": []
>         },
>         {
>           "name": "validateOnly",
>           "value": false
>         },
>         {
>           "name": "value",
>           "value": false
>         }
>       ],
>       "input": [
>         {
>           "name": "IDToken6",
>           "value": false
>         },
>         {
>           "name": "IDToken6validateOnly",
>           "value": false
>         }
>       ],
>       "_id": 5
>     },
>     {
>       "type": "ValidatedCreatePasswordCallback",
>       "output": [
>         {
>           "name": "echoOn",
>           "value": false
>         },
>         {
>           "name": "policies",
>           "value": {
>             "policyRequirements": [
>               "REQUIRED",
>               "MIN_LENGTH",
>               "VALID_TYPE",
>               "AT_LEAST_X_CAPITAL_LETTERS",
>               "AT_LEAST_X_NUMBERS",
>               "CANNOT_CONTAIN_OTHERS"
>             ],
>             "fallbackPolicies": null,
>             "name": "password",
>             "policies": [
>               {
>                 "policyRequirements": [
>                   "REQUIRED"
>                 ],
>                 "policyId": "not-empty"
>               },
>               {
>                 "policyRequirements": [
>                   "MIN_LENGTH"
>                 ],
>                 "policyId": "minimum-length",
>                 "params": {
>                   "minLength": 8
>                 }
>               },
>               {
>                 "policyRequirements": [
>                   "VALID_TYPE"
>                 ],
>                 "policyId": "valid-type",
>                 "params": {
>                   "types": [
>                     "string"
>                   ]
>                 }
>               },
>               {
>                 "policyId": "at-least-X-capitals",
>                 "params": {
>                   "numCaps": 1
>                 },
>                 "policyRequirements": [
>                   "AT_LEAST_X_CAPITAL_LETTERS"
>                 ]
>               },
>               {
>                 "policyId": "at-least-X-numbers",
>                 "params": {
>                   "numNums": 1
>                 },
>                 "policyRequirements": [
>                   "AT_LEAST_X_NUMBERS"
>                 ]
>               },
>               {
>                 "policyId": "cannot-contain-others",
>                 "params": {
>                   "disallowedFields": [
>                     "userName",
>                     "givenName",
>                     "sn"
>                   ]
>                 },
>                 "policyRequirements": [
>                   "CANNOT_CONTAIN_OTHERS"
>                 ]
>               }
>             ],
>             "conditionalPolicies": null
>           }
>         },
>         {
>           "name": "failedPolicies",
>           "value": []
>         },
>         {
>           "name": "validateOnly",
>           "value": false
>         },
>         {
>           "name": "prompt",
>           "value": "Password"
>         }
>       ],
>       "input": [
>         {
>           "name": "IDToken7",
>           "value": ""
>         },
>         {
>           "name": "IDToken7validateOnly",
>           "value": false
>         }
>       ],
>       "_id": 6
>     },
>     {
>       "type": "KbaCreateCallback",
>       "output": [
>         {
>           "name": "prompt",
>           "value": "Select a security question"
>         },
>         {
>           "name": "predefinedQuestions",
>           "value": [
>             "What's your favorite color?",
>             "Who was your first employer?"
>           ]
>         }
>       ],
>       "input": [
>         {
>           "name": "IDToken8question",
>           "value": ""
>         },
>         {
>           "name": "IDToken8answer",
>           "value": ""
>         }
>       ],
>       "_id": 7
>     },
>     {
>       "type": "KbaCreateCallback",
>       "output": [
>         {
>           "name": "prompt",
>           "value": "Select a security question"
>         },
>         {
>           "name": "predefinedQuestions",
>           "value": [
>             "What's your favorite color?",
>             "Who was your first employer?"
>           ]
>         }
>       ],
>       "input": [
>         {
>           "name": "IDToken9question",
>           "value": ""
>         },
>         {
>           "name": "IDToken9answer",
>           "value": ""
>         }
>       ],
>       "_id": 8
>     },
>     {
>       "type": "TermsAndConditionsCallback",
>       "output": [
>         {
>           "name": "version",
>           "value": "0.0"
>         },
>         {
>           "name": "terms",
>           "value": "Example terms..."
>         },
>         {
>           "name": "createDate",
>           "value": "2019-10-28T04:20:11.320Z"
>         }
>       ],
>       "input": [
>         {
>           "name": "IDToken10",
>           "value": false
>         }
>       ],
>       "_id": 9
>     }
>   ],
>   "header": "Sign Up",
>   "description": "Signing up is fast and easy.<br>Already have an account? <a href='#/service/Login'>Sign In</a>"
> }
> ```

---

---
title: User self-service overview
description: "Advanced Identity Cloud user self-service overview: journey nodes and templates for registration, sign-on, password reset, and username recovery"
component: pingoneaic
page_id: pingoneaic:self-service:overview
canonical_url: https://docs.pingidentity.com/pingoneaic/self-service/overview.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Accounts", "Journeys", "Nodes &amp; Trees"]
section_ids:
  auth-nodes: Nodes for self-service journeys
  journey-templates: Journey templates for user self-service
---

# User self-service overview

User self-service lets end users create and manage their own accounts, while you control the available features. You manage features and end-user journeys through the Advanced Identity Cloud admin console.

## Nodes for self-service journeys

The following nodes are designed for self-service journeys, although you can use them in any journey.

|                                                                                                                             |                                                                                                                 |                                                                                                                             |
| --------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| [Accept Terms and Conditions node](https://docs.pingidentity.com/auth-node-ref/latest/accept-terms-and-conditions.html)     | [Attribute Collector node](https://docs.pingidentity.com/auth-node-ref/latest/attribute-collector.html)         | [Attribute Present Decision node](https://docs.pingidentity.com/auth-node-ref/latest/attribute-present-decision.html)       |
| [Attribute Value Decision node](https://docs.pingidentity.com/auth-node-ref/latest/attribute-value-decision.html)           | [Consent Collector node](https://docs.pingidentity.com/auth-node-ref/latest/consent-collector.html)             | [Create Object node](https://docs.pingidentity.com/auth-node-ref/latest/create-object.html)                                 |
| [Display Username node](https://docs.pingidentity.com/auth-node-ref/latest/display-username.html)                           | [Email Suspend node](https://docs.pingidentity.com/auth-node-ref/latest/email-suspend.html)                     | [Email Template node](https://docs.pingidentity.com/auth-node-ref/latest/email-template.html)                               |
| [Identify Existing User node](https://docs.pingidentity.com/auth-node-ref/latest/identify-existing-user.html)               | [Increment Login Count node](https://docs.pingidentity.com/auth-node-ref/latest/increment-login-count.html)     | [KBA Decision node](https://docs.pingidentity.com/auth-node-ref/latest/kba-decision.html)                                   |
| [KBA Definition node](https://docs.pingidentity.com/auth-node-ref/latest/kba-definition.html)                               | [KBA Verification node](https://docs.pingidentity.com/auth-node-ref/latest/kba-verification.html)               | [Login Count Decision node](https://docs.pingidentity.com/auth-node-ref/latest/login-count-decision.html)                   |
| [Patch Object node](https://docs.pingidentity.com/auth-node-ref/latest/patch-object.html)                                   | [Platform Password node](https://docs.pingidentity.com/auth-node-ref/latest/platform-password.html)             | [Platform Username node](https://docs.pingidentity.com/auth-node-ref/latest/platform-username.html)                         |
| [Profile Completeness Decision node](https://docs.pingidentity.com/auth-node-ref/latest/profile-completeness-decision.html) | [Query Filter Decision node](https://docs.pingidentity.com/auth-node-ref/latest/query-filter-decision.html)     | [Required Attributes Present node](https://docs.pingidentity.com/auth-node-ref/latest/required-attributes-present.html)     |
| [Select Identity Provider node](https://docs.pingidentity.com/auth-node-ref/latest/select-identity-provider.html)           | [Social Provider Handler node](https://docs.pingidentity.com/auth-node-ref/latest/social-provider-handler.html) | [Terms and Conditions Decision node](https://docs.pingidentity.com/auth-node-ref/latest/terms-and-conditions-decision.html) |
| [Time Since Decision node](https://docs.pingidentity.com/auth-node-ref/latest/time-since-decision.html)                     |                                                                                                                 |                                                                                                                             |

User self-service journeys are further extensible through [Marketplace nodes](../journeys/marketplace.html).

## Journey templates for user self-service

The following journey templates are included with Advanced Identity Cloud:

* Registration

  The **Registration** journey describes a basic registration flow, where Advanced Identity Cloud prompts the end user to provide several profile attributes, then attempts to create and sign-on the end user.

  Learn more in [User self-registration](self-registration.html).

  Learn more about configuring registration to include social identity providers in [Social authentication](social-registration.html).

* Login

  The **Login** journey describes a basic sign-on flow, where the end user is prompted to provide a username and password, then passed to a progressive profile journey before being signed on.

  Learn more in [Sign-on (login)](login.html).

  Learn more about including social identity providers in a sign-on journey in [Social authentication](social-registration.html).

* ProgressiveProfile

  The **ProgressiveProfile** journey is called by the **Login** journey. It checks whether the successful sign-on count has reached a specified number. If it has reached the specified number, and end-user preferences have not been set, the end user is prompted to set those preferences. If it has not reached the specified number, the end user is returned to the **Login** journey to complete signing on.

  Learn more in [Progressive profile](progressive-profile.html).

* ResetPassword

  The **ResetPassword** journey lets end users reset their password by providing their email and answering security questions. If the questions are answered correctly, the end user is emailed a password reset link, which they must click to proceed. They are then presented with a password prompt to enter a new password.

  Learn more in [Password reset](password-reset.html).

* ForgottenUsername

  The **ForgottenUsername** journey lets end users recover their username by entering an email address. If the email address is associated with a user account, the account's username will be emailed to the end user. The email includes a link to sign on, which will take the end user through the **Login** journey.

  Learn more in [Username recovery](username-recovery.html).

* UpdatePassword

  The **Update Password** journey lets end users change their passwords. The journey assumes that the end user has already logged in successfully. It checks the end user's session data and, if the session is valid, prompts the end user to update their password.

  Learn more in [Password update](update-password.html).

---

---
title: Username recovery
description: Configure the Advanced Identity Cloud username recovery journey to email end users their username when they provide their registered email address
component: pingoneaic
page_id: pingoneaic:self-service:username-recovery
canonical_url: https://docs.pingidentity.com/pingoneaic/self-service/username-recovery.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Accounts", "Journeys", "Nodes &amp; Trees", "Forgotten Username"]
section_ids:
  forgotten-username-rest-sample: Example forgotten username REST output
---

# Username recovery

Username recovery lets end users recover their usernames using other information they remember, such as their email address.

PingOne Advanced Identity Cloud includes a **ForgottenUsername** journey template. This journey collects an end user's email address and then uses it to search for a user identity with that address. It then emails the username associated with that email address to the end user.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | When reviewing the journey template, notice that both [Identify Existing User node](https://docs.pingidentity.com/auth-node-ref/latest/identify-existing-user.html) outputs connect to the [Email Suspend node](https://docs.pingidentity.com/auth-node-ref/latest/email-suspend.html).This is recommended behavior for security reasons. Returning different outcomes potentially exposes which end users have accounts in your system. |

![Sample forgotten username journey](_images/PlatformForgottenUsername.png)

An alternative journey sends a verification link, then uses the [Display Username node](https://docs.pingidentity.com/auth-node-ref/latest/display-username.html) once the end user returns from the email.

## Example forgotten username REST output

When calling a username recovery self-service endpoint, you'll receive a JSON object back, containing callbacks for each of the nodes included in the username recovery journey.

> **Collapse: Sample JSON callbacks**
>
> ```json
> {
>   "authId": "<omitted for length>",
>   "callbacks": [
>     {
>       "type": "StringAttributeInputCallback",
>       "output": [
>         {
>           "name": "name",
>           "value": "mail"
>         },
>         {
>           "name": "prompt",
>           "value": "Email Address"
>         },
>         {
>           "name": "required",
>           "value": true
>         },
>         {
>           "name": "policies",
>           "value": {}
>         },
>         {
>           "name": "failedPolicies",
>           "value": []
>         },
>         {
>           "name": "validateOnly",
>           "value": false
>         },
>         {
>           "name": "value",
>           "value": ""
>         }
>       ],
>       "input": [
>         {
>           "name": "IDToken1",
>           "value": ""
>         },
>         {
>           "name": "IDToken1validateOnly",
>           "value": false
>         }
>       ],
>       "_id": 0
>     }
>   ],
>   "header": "Forgotten Username",
>   "description": "Enter your email address or <a href=\"#/service/Login\">Sign in</a>"
> }
> ```