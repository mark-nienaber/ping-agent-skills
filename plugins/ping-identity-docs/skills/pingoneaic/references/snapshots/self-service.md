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
