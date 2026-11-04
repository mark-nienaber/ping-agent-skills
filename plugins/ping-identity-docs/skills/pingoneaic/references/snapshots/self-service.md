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

To let end users update their password through the hosted account pages profile page using the Reset link, you set a self-service journey for the password update journey. The default journey is UpdatePassword.

To change the journey for password updates:

1. In the Advanced Identity Cloud admin console, go to Authentication > Self Service Journeys.

2. If the Status is inactive, click Activate to enable it.

3. In the Journey list next to `updatePassword`, select the journey you want to use.

4. Click Save.

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

Self-service journeys primarily use PingIDM nodes.

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
title: Self-service journey mappings
description: Configure self-service journey mappings in Advanced Identity Cloud to assign journeys for self-service flows
component: pingoneaic
page_id: pingoneaic:self-service:self-service-journeys-mappings
canonical_url: https://docs.pingidentity.com/pingoneaic/self-service/self-service-journeys-mappings.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Self-Service", "Username Recovery", "Password Reset", "Update Passwords", "Registration"]
section_ids:
  default-journey-mapping: Configure default journey mappings
  custom-journey-mapping: Add a custom journey mapping
  deactivate-self-service-journey-service: Deactivate the self-service journey service
---

# Self-service journey mappings

Advanced Identity Cloud provides out-of-the-box journeys for registration, password reset, username recovery, and password update. These are configured as self-service journeys using mapping keys, with the following defaults:

| Key                 | Default journey     |
| ------------------- | ------------------- |
| `forgottenUsername` | `ForgottenUsername` |
| `registration`      | `Registration`      |
| `resetPassword`     | `ResetPassword`     |
| `updatePassword`    | `UpdatePassword`    |

You can update any of the default mappings to point to your own custom journeys. You can also add custom mappings for supported self-service journeys. For example, you can add a `connectSocial` mapping that points to a social account-linking journey from the end-user hosted account pages.

## Configure default journey mappings

1. In the Advanced Identity Cloud admin console, go to [icon: verified_user, set=material, size=inline] Authentication > Self-service Journeys.

2. If the Status is inactive, click Activate to enable it.

3. In the Settings section, select the journey for each mapping key you want to customize.

4. Click Save.

When you save a default mapping, the corresponding self-service flow uses the journey you assign. For example, hosted pages with links for registration, username recovery, and password reset use these mappings to launch the correct journey.

## Add a custom journey mapping

Use a custom mapping when you want hosted pages or another self-service entry point to launch a journey that isn't one of the default self-service flows, such as linking a social account from the hosted account pages.

1. In the Advanced Identity Cloud admin console, go to [icon: verified_user, set=material, size=inline] Authentication > Self-service Journeys.

2. If the Status is inactive, click Activate to enable it.

3. Click [icon: add, set=material, size=inline] Add mapping.

4. In the Key field, enter a name for the mapping key.

5. In the Journey list, select the journey to assign to the key.

6. Click Save.

## Deactivate the self-service journey service

Deactivating the service disables the mappings between self-service keys, such as `resetPassword`, and their assigned journeys. As a result, self-service features that rely on these mappings might be unavailable until you reactivate the service. However, deactivating the service doesn't remove the underlying journeys.

To deactivate the service:

1. In the Advanced Identity Cloud admin console, go to [icon: verified_user, set=material, size=inline] Authentication > Self-service Journeys.

2. At the top of the page, click Deactivate.

When the service is inactive, self-service journey configuration is hidden until you activate it again.

---

---
title: Self-service journeys
description: Configure Advanced Identity Cloud self-service journeys for password reset, username recovery, self-registration, and progressive profile
component: pingoneaic
page_id: pingoneaic:self-service:self-service-journeys
canonical_url: https://docs.pingidentity.com/pingoneaic/self-service/self-service-journeys.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Self-Service", "Username Recovery", "Password Reset", "Update Passwords", "Registration", "Progressive Profile"]
section_ids:
  use-cases-for-user-self-service: Self-service use cases
  journey-templates: Default self-service journeys
  auth-nodes: Common nodes for self-service journeys
---

# Self-service journeys

Self-service journeys in Advanced Identity Cloud let end users complete common account tasks without administrator assistance. To enable these features, you can use the default journey templates provided by Advanced Identity Cloud as a starting point, or build your own custom journeys. This page provides an overview of the common self-service use cases and the default journeys you can use to implement them.

## Self-service use cases

You can configure the following self-service journeys in Advanced Identity Cloud:

| Use Case                                                                                           | Description                                                                     |
| -------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| [Simple sign-on](login.html)                                                                       | Lets end users sign on by collecting a username and password.                   |
| [Username recovery](username-recovery.html)                                                        | Lets end users recover their username.                                          |
| [Password reset](password-reset.html)                                                              | Lets end users reset their password.                                            |
| [Password update](update-password.html)                                                            | Lets end users update their password, after signing on and obtaining a session. |
| [User self-registration](self-registration.html)                                                   | Lets end users register their own identity in Advanced Identity Cloud.          |
| [Social authentication](../authentication/social-authentication.html)                              | Lets end users authenticate using social providers, such as Google or Facebook. |
| [Progressive profile](progressive-profile.html)                                                    | Asks end users for more information based on a login count.                     |
| [Replace lost second-factor authentication devices](../use-cases/use-case-lost-second-factor.html) | Lets end users sign on with a recovery code if they lose their device.          |

## Default self-service journeys

The following journey templates are included with Advanced Identity Cloud:

* Registration

  The **Registration** journey describes a basic registration flow, where Advanced Identity Cloud prompts the end user to provide several profile attributes, then attempts to create and sign-on the end user.

  Learn more in [User self-registration](self-registration.html).

  Learn more about configuring registration to include social identity providers in [Social authentication](../authentication/social-authentication.html).

* Login

  The **Login** journey describes a basic sign-on flow, where the end user is prompted to provide a username and password, then passed to a progressive profile journey before being signed on.

  Learn more in [Sign-on (login)](login.html).

  Learn more about including social identity providers in a sign-on journey in [Social authentication](../authentication/social-authentication.html).

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

## Common nodes for self-service journeys

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

Self-service journeys are further extensible through [Marketplace nodes](../journeys/marketplace.html).

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
  login-rest-sample: Example login REST output
---

# Sign-on (login)

The PingOne Advanced Identity Cloud sign-on flow is designed for self-service, as demonstrated in the **Login** journey template. This journey lets end users sign on using their Advanced Identity Cloud credentials and increments the login counter. A separate retry-limit counter tracks failed authentications and locks the end-user account if the number of retries exceeds a specified limit. End users who successfully authenticate are sent through a separate [progressive profile journey](progressive-profile.html).

|   |                                                                                                                                                                                                        |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | The **Login** journey template can be extended to include other features, such as support for identity providers. Learn more in [Social authentication](../authentication/social-authentication.html). |

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

1. In the Advanced Identity Cloud admin console, go to [icon: account_tree, set=material, size=inline] Authentication > Security Questions. From here, you can configure the questions that are presented to end users and how they should be handled.

2. Click Add Question to set additional questions for the end user.

3. On the Add a Security Question modal:

   1. Select a locale, provide the question text for that locale, and click Done.

   2. To provide the question for different locales, click Add locale and repeat the previous step.

   3. Click Save.

4. On the Settings tab, set the following:

   * Must define: The minimum number of security questions the end user must set up during registration.

   * Must answer: The minimum number of questions the end user must answer to satisfy a security prompt.

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

1. In the Advanced Identity Cloud admin console, go to [icon: touch_app, set=material, size=inline] User Experience > Terms & Conditions, and click + New Version.

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

In registration and self-service journeys, privacy and consent lets end users decide whether their information can be shared with external resources, such as sales and marketing services. Advanced Identity Cloud manages these resources as applications and uses provisioning mappings to synchronize the selected data. Learn more in [End-user data sharing](../app-management/provision-an-application.html#end-user-data-sharing).

### Configuration

To configure privacy and consent for an application:

1. In the Advanced Identity Cloud admin console, go to [icon: apps, set=material, size=inline] Applications > Applications and select the application.

2. Select the Provisioning tab.

3. Select Privacy & Consent.

4. In the Consent-based Provisioning section, click Activate to let end users prevent the sharing of their personal data.

5. To enable the end-user profile page to display the Personal Data Sharing option, go to [icon: touch_app, set=material, size=inline] User Experience > Hosted Pages, select the Realm Default theme, select Account Pages > Layout, enable Consent, and click Save.

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