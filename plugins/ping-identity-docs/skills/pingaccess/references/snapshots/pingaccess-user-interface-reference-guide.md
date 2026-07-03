---
title: Access header
description: The Access header contains options related to access control, such as rules, web sessions, and token validation.
component: pingaccess
version: 9.1
page_id: pingaccess:pingaccess_user_interface_reference_guide:pa_access_header
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/pingaccess_user_interface_reference_guide/pa_access_header.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: March 15, 2023
---

# Access header

The **Access** header contains options related to access control, such as rules, web sessions, and token validation.

The **Access** header contains these menu options:

* [Rules](pa_rules.html)

* [Authentication](pa_authentication.html)

* [Identity mappings](pa_identity_mappings.html)

* [Web sessions](pa_web_sessions.html)

* [Token validation](pa_token_validation.html)

* [Unknown resources](pa_unknown_resources.html)

* [Managing risk policies](pa_risk_policies_overview.html)

---

---
title: Adding a cross-origin request rule
description: Use cross-origin resource sharing (CORS) to let a web server grant access to restricted resources, such as fonts, JavaScript, and images, to an application that's served by another domain. This is done without granting access to those resources beyond a list of predefined origin servers.
component: pingaccess
version: 9.1
page_id: pingaccess:pingaccess_user_interface_reference_guide:pa_adding_a_cross_origin_request_rule
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/pingaccess_user_interface_reference_guide/pa_adding_a_cross_origin_request_rule.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: December 4, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Adding a cross-origin request rule

Use cross-origin resource sharing (CORS) to let a web server grant access to restricted resources, such as fonts, JavaScript, and images, to an application that's served by another domain. This is done without granting access to those resources beyond a list of predefined origin servers.

## About this task

Before a CORS request is sent, the originating web server generally sends a pre-flight `OPTIONS` request if the client's request includes credentials. This pre-flight request is used to determine if the target server will permit the originating web server to process CORS requests.

PingAccess can evaluate the headers provided in a CORS request to grant or deny access to resources.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | If the target application has an **Application Type** of `API`, you can allow the protected application to handle the request instead of PingAccess.To do this with a resource path that is protected by PingAccess and requires user authentication, configure a second resource with the same path pattern. Make sure to set the **Methods** field to `OPTIONS` and clear the **Anonymous** option. This configuration allows the API request to be handled anonymously. |

## Steps

1. Click **Access**, then go to **Rules > Rules**.

2. Click **[icon: plus, set=fa]Add Rule**.

3. In the **Name** field, enter a unique name up to 64 characters long.

   Special characters and spaces are allowed.

4. In the **Type** list, select **Cross-Origin Request**.

5. In the **Allowed Origins** field, enter one or more origin values.

   1. Click **[icon: plus, set=fa]New Value** to add additional values.

      |   |                                                                                                            |
      | - | ---------------------------------------------------------------------------------------------------------- |
      |   | Avoid using a value of `*` in this field. While this is a valid configuration, it is an insecure practice. |

6. (Optional) To configure additional options, click **Show Advanced Settings**.

   1. To permit user credentials to be used in determining access, enable **Allow Credentials**.

   2. If you entered a wildcard in the **Allowed Origins** field, select the **Mask Wildcard Policy** checkbox to replace the `Access-Control-Allow-Origin` response header with the value provided in the request's `Origin` header.

   3. To modify the **Allowed Request Headers** values, use the following options:

      * To add a new header, click **[icon: plus, set=fa]New Value**.

      * To edit an existing header, click the field and make your changes.

      * To remove an existing header, click the **Delete** icon.

      The default headers are `Authorization`, `Content-Type`, and `Accept`.

   4. To respond to CORS preflight requests with the expected response header, `Access-Control-Allow-Private-Network: true`, select **Allow Private Access Network**.

      |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
      | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      |   | Google Chrome CORS preflight requests will soon include a new request header: `Access-Control-Request-Private-Network: true`. If preflight requests that contain this header do not receive a `Access-Control-Allow-Private-Network: true` header in response, access requests will be denied.Learn more about these headers in <https://developer.chrome.com/blog/private-network-access-preflight?hl=en#what_to_do_if_your_website_is_affected>. |

   5. To make specific response headers available to the client that originated the cross-origin request, enter the headers in the **Exposed Response Headers** field.

   6. To add additional headers to the list, click **[icon: plus, set=fa]New Value**.

   7. To define the request methods allowed in cross-origin requests, enter the desired overrides in the **Overridden Request Methods** field.

   8. To modify the amount of time that the pre-flight `OPTIONS` request is cached, enter the maximum age (in seconds) in the **OPTIONS Cache Max Age** field.

      The default is `600` seconds.

7. Click **Save**.

---

---
title: Adding a PingOne connection
description: Configure PingOne Protect for connectivity with PingAccess:
component: pingaccess
version: 9.1
page_id: pingaccess:pingaccess_user_interface_reference_guide:pa_adding_a_p1_connection
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/pingaccess_user_interface_reference_guide/pa_adding_a_p1_connection.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 9, 2024
section_ids:
  steps: Steps
  result: Result:
  next-steps: Next steps
---

# Adding a PingOne connection

## Steps

1. Configure PingOne Protect for connectivity with PingAccess:

   1. In your PingOne administrative environment, go to **Integrations → PingFederate**.

      Currently, you must use a PingFederate connection because PingAccess does not have one of its own.

   2. Expand an existing connection or click the **[icon: plus, set=fa]**icon to create a new one.

   3. On the **Overview** tab, click the **[icon: plus, set=fa]**icon next to **Credentials**.

   4. Click the **Copy to clipboard** icon, then click **Done**.

      ### Result:

      This copies a JSON Web Token (JWT) *(tooltip: \<div class="paragraph">
      \<p>An IETF standard container format for a JSON object used for the secure exchange of content, such as identity or entitlement information. You can find the industry standard in \<a href="https\://datatracker.ietf.org/doc/html/rfc7519">RFC 7519\</a>.\</p>
      \</div>)* to your clipboard that contains information on your PingOne environment.

2. Configure PingAccess for connectivity with PingOne Protect:

   1. In PingAccess, go to **Settings → System → PingOne Connections** and click **+Add PingOne Connection**.

   2. Complete the fields.

      For more information, see [PingOne connection field descriptions](pa_p1_connection_field_descriptions.html).

   3. Click **Save**.

## Next steps

After you've created a connection, you can assign it to a specific risk policy through the **Risk Policies** page. For more information, see [Adding a risk policy](pa_adding_a_risk_policy.html).

---

---
title: Adding a redirect
description: Add a new redirect in PingAccess.
component: pingaccess
version: 9.1
page_id: pingaccess:pingaccess_user_interface_reference_guide:pa_adding_a_redirect
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/pingaccess_user_interface_reference_guide/pa_adding_a_redirect.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: February 6, 2023
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Adding a redirect

Add a new redirect in PingAccess.

## About this task

Map the host and port of an incoming request to a different target.

## Steps

1. Click **Applications**, then go to **Applications > Redirects**.

2. Click **[icon: plus, set=fa]Add Redirect**.

3. In the **Source** field, enter the source host and port that you want to redirect.

4. In the **Target** field, enter the target host and post that indicates the destination for the redirect.

5. **Optional:** To use HTTPS for the request made to the redirect target, select the **Secure Target** check box.

6. In the **Response Code** field, enter the HTTP response code you want to associate with the redirect.

   `301` is specified as the default.

7. To audit redirects, select the **Audit** check box.

8. To confirm your changes, click **Save**.

---

---
title: Adding a risk policy
description: Make sure that:
component: pingaccess
version: 9.1
page_id: pingaccess:pingaccess_user_interface_reference_guide:pa_adding_a_risk_policy
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/pingaccess_user_interface_reference_guide/pa_adding_a_risk_policy.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 14, 2023
section_ids:
  before-you-begin: Before you begin
  about-this-task: About this task
  steps: Steps
  next-steps: Next steps
---

# Adding a risk policy

## Before you begin

Make sure that:

* You have set up a PingOne connection in PingAccess.

* You have your PingOne credential easily accessible to copy and paste.

For more information, see [Adding a PingOne connection](pa_adding_a_p1_connection.html).

## About this task

To add a risk policy:

## Steps

1. In the PingAccess administrative console, go to **Access → Risk Policies** and click **+Add Risk Policy**.

2. Complete the fields.

   For more information, see [Risk policy field descriptions](pa_risk_policy_field_descriptions.html).

   |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
   |   | You can only configure a PingOne risk policy in PingOne Protect.If you haven't enabled device profiling in a PingAccess risk policy configuration, then you shouldn't include **New Device** or other device-related PingOne predictor types in the associated PingOne risk policy.Some of these device-related predictor types are included in the default PingOne risk policy. If you haven't enabled device profiling, make sure to remove the following predictor types from your configuration or adjust the weights or scores associated with them:- Anonymous network detection

   - Geovelocity anomaly

   - IP reputation

   - IP velocity

   - New device

   - User location anomalyFor more information, see [Risk policies](https://docs.pingidentity.com/pingone/threat_protection_using_pingone_protect/p1_protect_risk_policies.html) in the PingOne documentation. |

3. Click **Save**.

## Next steps

After you've created a PingAccess risk policy, you can assign it to a specific application or resource. For more information, see [Application field descriptions](pa_application_field_descriptions.html) or [Adding application resources](pa_adding_application_resources.html).

---

---
title: Adding a Safenet Luna provider
description: Add a Safenet Luna provider to begin using hardware security module (HSM)-stored key pairs in PingAccess.
component: pingaccess
version: 9.1
page_id: pingaccess:pingaccess_user_interface_reference_guide:pa_adding_a_safenet_luna_provider
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/pingaccess_user_interface_reference_guide/pa_adding_a_safenet_luna_provider.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: February 6, 2023
section_ids:
  before-you-begin: Before you begin
  steps: Steps
---

# Adding a Safenet Luna provider

Add a Safenet Luna provider to begin using hardware security module (HSM) *(tooltip: \<div class="paragraph">
\<p>A dedicated cryptographic processor designed to manage and protect digital keys. HSMs act as trust anchors that protect the cryptographic key lifecycle by securely managing, processing, and storing cryptographic keys inside a hardened, tamper-resistant device.\</p>
\</div>)*-stored key pairs in PingAccess.

## Before you begin

* Configure your hardware security module.

* Configure a Luna client on the PingAccess system. The PingAccess service must have full permissions over the client.

* Move the `/usr/safenet/lunaclient/lib/libCryptoki2_64.so` library on Linux systems, or the `\Program Files\SafeNet\LunaClient\win32\cryptoki.dll` library on Windows systems, to the `deploy` directory on the PingAccess system.

## Steps

1. Click **Security**, then go to **HSM Providers**.

2. Click **[icon: plus, set=fa]Add HSM Provider**.

3. In the **Name** field, enter a name for the HSM provider.

4. From the **Type** list, select **Safenet Luna Provider**.

5. In the **Slot ID** field, enter the slot ID of the HSM slot to use.

6. In the **Library** field, enter the name of the library you copied from the Luna client to the `deploy` directory.

7. In the **Password** field, enter a password for connecting to the HSM provider.

8. Click **Save**.

9. Restart PingAccess.

---

---
title: Adding access token validators
description: Add an access token validator to verify signed or encrypted access tokens in PingAccess.
component: pingaccess
version: 9.1
page_id: pingaccess:pingaccess_user_interface_reference_guide:pa_adding_access_token_validators
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/pingaccess_user_interface_reference_guide/pa_adding_access_token_validators.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: December 4, 2025
section_ids:
  before-you-begin: Before you begin
  steps: Steps
  adding-multiple-jwks-endpoint-access-token-validators: Adding multiple JWKS endpoint access token validators
  before-you-begin-2: Before you begin
  steps-2: Steps
---

# Adding access token validators

Add an access token validator to verify signed or encrypted access tokens in PingAccess.

## Before you begin

If you want to validate access tokens with your own JWKS endpoint, create a [third-party service](pa_third_party_services.html) for the JWKS endpoint before configuring an access token validator.

## Steps

1. Click **Access**, then go to **Token Validation > Access Token Validators**.

2. Click **[icon: plus, set=fa]Add Access Token Validator**.

3. In the **Name** field, enter a name for the token validator.

4. In the **Type** list, select the type of key you want to validate.

   The token provider configuration specifies which type of key. You can find information about configuring PingFederate as the token provider in [Configuring JSON token management](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_beareraccesstokenmgmtplugintasklet_configureauthnadapterstate.html).

5. (Optional) In the **Description** field, enter a description for the token validator.

6. To validate access tokens with your own JWKS endpoint, in the **Third-Party Service** list, select a JWKS endpoint you configured as a third-party service previously.

   |   |                                                                                                                                                                                                                                                                               |
   | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | The third-party service's target is used as a host. If you select a third-party service in this list, that service acts as the primary access token validator and overrides any other configured token provider for the application associated with this third-party service. |

7. In the **Path** field, specify the endpoint path to verify the signature.

   This entry must start with a forward slash (/), and must not end with a forward slash (/). PingFederate token provider configuration informs the host and port. PingAccess permits query strings in the path.

8. (Optional) In the **Subject Attribute Name** field, enter the attribute expected as the subject.

   If this value is configured and the specified subject attribute name isn't present in the token, validation fails.

9. (Optional) In the **Issuer** field, enter the expected value of the issuer to include in the access token.

   If this value is configured and the specified issuer isn't present in the token, validation fails.

10. (Optional) In the **Audience** field, specify the audience value to include in the access token.

    If this value is configured and the specified audience isn't present in the token, validation fails.

11. If you don't want to validate access tokens for an audience value, you must select the **Skip Audience Validation** checkbox.

12. Click **Save**.

## Adding multiple JWKS endpoint access token validators

Add a **Multiple JSON Web Key Set (JWKS) Endpoint** access token validator to define multiple endpoints or issuers.

### Before you begin

If you want to validate access tokens with your own JWKS endpoint, create a [third-party service](pa_third_party_services.html) for the JWKS endpoint before configuring an access token validator.

### Steps

1. Click **Access**, then go to **Token Validation > Access Token Validators**.

2. Click **[icon: plus, set=fa]Add Access Token Validator**.

3. In the **Name** field, enter a name for the token validator.

4. In the **Type** list, select **Multiple JSON Web Key Set (JWKS) Endpoint**.

5. (Optional) In the **Description** field, enter a description for the token validator.

6. In the **Third-Party Service** list, select a JWKS endpoint you configured as a third-party service previously to validate access tokens with.

   |   |                                                                                                                                                                                                                                                                               |
   | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | The third-party service's target is used as a host. If you select a third-party service in this list, that service acts as the primary access token validator and overrides any other configured token provider for the application associated with this third-party service. |

7. In the **Path** field, specify the endpoint path to verify the signature.

   This entry must start with a forward slash (/), and must not end with a forward slash (/). PingFederate token provider configuration informs the host and port. PingAccess permits query strings in the path.

8. (Optional) In the **Subject Attribute Name** field, enter the attribute expected as the subject.

   If this value is configured and the specified subject attribute name isn't present in the token, validation fails.

9. (Optional) In the **Issuer** field, enter the expected value of the issuer to include in the access token.

   If this value is configured and the specified issuer isn't present in the token, validation fails.

   |   |                                                                                                                                                                                                                                                                                                                               |
   | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | A **Multiple JSON Web Key Set (JWKS) Endpoint** access token validator (ATV) processes each JWKS with the matching issuer from the access token. The issuer value is looked at first, if it's present.If a matching issuer isn't configured, the ATV cycles through all the JWKS endpoints until it finds the one that works. |

10. (Optional) In the **Audience** field, specify the audience value to include in the access token.

    If this value is configured and the specified audience isn't present in the token, validation fails.

11. If you don't want to validate access tokens for an audience value, you must select the **Skip Audience Validation** checkbox.

12. Click **+ Add Row** and repeat steps 6 - 11 for any additional endpoints.

13. Click **Save**.

---

---
title: Adding agents
description: Create new agents in PingAccess.
component: pingaccess
version: 9.1
page_id: pingaccess:pingaccess_user_interface_reference_guide:pa_adding_agents
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/pingaccess_user_interface_reference_guide/pa_adding_agents.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: March 27, 2025
section_ids:
  steps: Steps
---

# Adding agents

Create new agents in PingAccess.

## Steps

1. In the PingAccess console, go to **Applications > Agents**.

2. Click **[icon: plus, set=fa]Add Agent**.

3. Complete the fields.

   You can find more information about the fields in [Agent field descriptions](pa_agent_field_descriptions.html).

4. To configure advanced settings, click **Show Advanced**.

5. To save the configuration and download the `<agent-name>_agent.properties` file for use with the PingAccess agent, click **Save & Download**.

   |   |                                                                                                                                                                                                                                                                                                                                               |
   | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | The shared secret is generated by the PingAccess server and identified on this page with a timestamp. You can delete existing secrets by clicking **Remove** in the **secret** field. If an additional secret is needed, [edit](pa_editing_agents.html) the agent and click **Save & Download** to generate and download a new shared secret. |

   PingAccess can generate additional agent `agent.properties` files containing the specified information that can configure the agent plugin. Existing configurations can also be downloaded again if necessary.

---

---
title: Adding an application
description: Add a new application in PingAccess.
component: pingaccess
version: 9.1
page_id: pingaccess:pingaccess_user_interface_reference_guide:pa_adding_an_app
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/pingaccess_user_interface_reference_guide/pa_adding_an_app.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: February 6, 2023
section_ids:
  steps: Steps
---

# Adding an application

Add a new application in PingAccess.

## Steps

1. Click **Applications**, then go to **Applications > Applications**.

2. Click **[icon: plus, set=fa]Add Application**.

3. Complete the fields.

   Learn more in [Application field descriptions](pa_application_field_descriptions.html).

4. Click **Save**.

   **Save & Go to Resources** lets you configure additional application resources. Learn more in [Adding application resources](pa_adding_application_resources.html).

   |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
   |   | When you save the application, PingAccess verifies that the redirect Uniform Resource Identifier (URI) *(tooltip: \<div class="paragraph">&#xA;\<p>Identifies a web resource with a string of characters conforming to a specified format.\</p>&#xA;\</div>)* for the application's virtual host is configured in PingFederate. If PingAccess determines that the redirect URI is not defined, you will see the following warning:```
   Save succeeded. Unable to find a matching Redirect URI in the PingFederate OAuth Client configuration for <VHost>/pa/oidc/cb
   ```If you see this warning, ensure that there is a redirect URI that matches your configuration. If you have a wildcard in your virtual host configuration, ensure the redirect URI list includes the same wildcard host definition, otherwise you might have a configuration that is only valid in some circumstances.This validation is performed if the **Application Type** is `Web` or `Web + API`, a **Web Session** is selected, and the PingFederate Administration connection is configured. |

---

---
title: Adding an authentication requirements rule
description: Add an authentication requirements rule in PingAccess to limit access to resources or applications protected by PingAccess based on the access control rule (ACR) values returned by the PingFederate request AuthN context authentication selector.
component: pingaccess
version: 9.1
page_id: pingaccess:pingaccess_user_interface_reference_guide:pa_adding_an_authn_requirements_rule
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/pingaccess_user_interface_reference_guide/pa_adding_an_authn_requirements_rule.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: February 6, 2023
section_ids:
  before-you-begin: Before you begin
  about-this-task: About this task
  steps: Steps
---

# Adding an authentication requirements rule

Add an authentication requirements rule in PingAccess to limit access to resources or applications protected by PingAccess based on the access control rule (ACR) values returned by the PingFederate request AuthN context authentication selector.

## Before you begin

Verify that you have:

* A PingFederate configuration that uses the `Requested AuthN Context Authentication Selector`

* A configured authentication list

## About this task

An authentication requirements rule allows authentication requirements to be applied when a policy decision is being made by the PingAccess engine, allowing an entire application or individual resources to require a particular authentication type.

This rule also allows for configurations that require more secure authentication methods, such as multi-factor authentication (MFA) *(tooltip: \<div class="paragraph">
\<p>An electronic authentication method where a user is granted access only after presenting two or more verification factors for authentication.\</p>
\</div>)*. For example, a website might allow a user to authenticate and view personal data using only a user name and password, but editing their personal data could require an additional PingID verification step. When used in this manner, an additional step-up authentication event is automatically triggered.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                             |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | To ensure that step-up authentication is triggered, this rule should always be positioned first in a list of rules, rule sets, or rule set groups, regardless of whether the criteria is `Any` or `All`.PingAccess uses rules to trigger different authentication paths in PingFederate. If the authentication requirements rule isn't the first item in a list, then it isn't sent to PingFederate in the initial request. |

## Steps

1. Click **Access**, then go to **Rules > Rules**.

2. Click **[icon: plus, set=fa]Add Rule**.

3. In the **Name** field, enter a unique name, up to 64 characters long.

   Special characters and spaces are allowed.

4. From the **Type** list, select **Authentication Requirements**.

5. Select an [Authentication Requirements List](pa_configuring_authn_reqs_lists.html).

6. Select a **Minimum Authentication Requirement**.

   |   |                                                                                                                                    |
   | - | ---------------------------------------------------------------------------------------------------------------------------------- |
   |   | The possible values for the **Minimum Authentication Requirement** are derived from the selected Authentication Requirements list. |

7. **Optional:** In the **Max Age (M)** field, enter a maximum time since the last authentication. If the user's session has not authenticated in this timeframe, the user is prompted to reauthenticate.

   A value of -1 indicates no maximum age.

8. Click **Save**.

---

---
title: Adding an AWS CloudHSM provider
description: To use hardware security module (HSM)-stored key pairs in PingAccess, add an Amazon Web Services (AWS) CloudHSM provider in the PingAccess administrative console.
component: pingaccess
version: 9.1
page_id: pingaccess:pingaccess_user_interface_reference_guide:pa_adding_an_aws_cloudhsm_provider
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/pingaccess_user_interface_reference_guide/pa_adding_an_aws_cloudhsm_provider.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 16, 2023
section_ids:
  before-you-begin: Before you begin
  about-this-task: About this task
  steps: Steps
  troubleshooting: Troubleshooting
  next-steps: Next steps
  setting-up-a-new-installation-of-aws-cloudhsm: Setting up a new installation of AWS CloudHSM
  before-you-begin-2: Before you begin
  steps-2: Steps
  choose-from: Choose from:
  choose-from-2: Choose from:
  next-steps-2: Next steps
  upgrading-from-client-sdk-3-to-client-sdk-5: Upgrading from Client SDK 3 to Client SDK 5
  about-this-task-2: About this task
  steps-3: Steps
  result: Result
---

# Adding an AWS CloudHSM provider

To use hardware security module (HSM) *(tooltip: \<div class="paragraph">
\<p>A dedicated cryptographic processor designed to manage and protect digital keys. HSMs act as trust anchors that protect the cryptographic key lifecycle by securely managing, processing, and storing cryptographic keys inside a hardened, tamper-resistant device.\</p>
\</div>)*-stored key pairs in PingAccess, add an Amazon Web Services (AWS) *(tooltip: \<div class="paragraph">
\<p>An Amazon subsidiary providing cloud computing platforms.\</p>
\</div>)* CloudHSM provider in the PingAccess administrative console.

## Before you begin

PingAccess 7.3 and later no longer support AWS CloudHSM Client SDK 3.

* If you're upgrading the CloudHSM Client SDK from 3.x to 5.x, see [Upgrading from Client SDK 3 to Client SDK 5](pa_upgrading_from_sdk3_to_sdk5.html) before trying to add a CloudHSM provider in the PingAccess administrative console.

* If you are creating a new installation of AWS CloudHSM Client SDK 5, see [Setting up a new installation of AWS CloudHSM](pa_installing_cloudhsm_initially.html) before trying to add a CloudHSM provider in the PingAccess administrative console.

|   |                                                                                                                                                                                                                                                                                                                                      |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | Follow these steps to set up Client SDK 5 and integrate it with PingAccess even if you're just upgrading the Client SDK from 3.x to 5.x. Client SDK 5 no longer uses a client daemon. This changes the steps necessary to set up an AWS CloudHSM provider because the client process doesn't run separately from PingAccess anymore. |

## About this task

To add an AWS CloudHSM provider in the PingAccess administrative console:

## Steps

1. In PingAccess, go to **Security → HSM Providers**, and click **[icon: plus, set=fa]Add HSM Provider**.

2. In the **Name** field, enter a name for the HSM provider.

3. In the **Type** list, select **AWS CloudHSM Provider**.

4. In the **User** field, enter a username used to connect to the HSM provider.

5. In the **Password** field, enter a password used to connect to the HSM provider.

6. **Optional:** In the **Partition** field, enter the partition to use on the HSM provider.

7. Click **Save**.

8. Restart PingAccess.

## Troubleshooting

PingAccess 7.3 and later contain a workaround to bypass the following known issues by default:

1. `RSASSA-PSS` signing algorithms fail with `Java8u261` or later. HSM vendors and core Java use different naming conventions for the `RSASSA-PSS` algorithm.

2. PingAccess Cloud HSM functionality works in FIPS mode but not in regular mode for `Java8u261` and later.

If you experience either of these known issues, you can edit the `additional.security.jdk.tls.disabledAlgorithms` property in the `run.properties` file to bypass them. For more information, see the following example:

```
additional.security.jdk.tls.disabledAlgorithms=RSASSA-PSS, TLSv1.3
```

## Next steps

Begin creating and assigning [key pairs](pa_key_pairs.html). For more information on creating key pairs, see [Generating new key pairs](pa_generating_new_key_pairs.html) or [Importing existing key pairs](pa_importing_existing_key_pairs.html).

## Setting up a new installation of AWS CloudHSM

### Before you begin

* Configure your hardware security module. You must have a AWS CloudHSM cluster to complete step 3. Learn more in the [Amazon documentation](https://docs.aws.amazon.com/cloudhsm/latest/userguide/getting-started.html).

* Ensure that a supported Java version is installed on the PingAccess server.

  You can find more information on how to set up a Java Runtime Environment (JRE) *(tooltip: \<div class="paragraph">
  \<p>A software layer that provides the class libraries and resources needed for a Java program to run.\</p>
  \</div>)* in [Installing PingAccess on your system](../installing_and_uninstalling_pingaccess/pa_installing_pa_on_your_system.html). Make sure that you use a non-Oracle version of Java (such as Corretto).

* You must deploy PingAccess on an operating system that AWS CloudHSM supports. You can find mutually supported operating systems by referring to [System requirements](../installing_and_uninstalling_pingaccess/pa_installation_requirements.html#system-reqs) in the PingAccess documentation and [Supported platforms for the client SDKs](https://docs.aws.amazon.com/cloudhsm/latest/userguide/client-supported-platforms.html) in the AWS CloudHSM documentation.

To set up a new installation of AWS CloudHSM Client SDK 5 and integrate it with PingAccess:

### Steps

1. Request a crypto user (CU) account from your AWS CloudHSM administrator.

   |   |                                                                                                                                                                                                                                                        |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
   |   | You will need to reference your username and password for this account during steps 4 - 5 of [Adding an AWS CloudHSM provider](pa_adding_an_aws_cloudhsm_provider.html). PingAccess uses this information to establish a connection with AWS CloudHSM. |

2. Install and configure the AWS CloudHSM Java Cryptography Extension (JCE) provider for Client SDK 5.

   Learn more in [Install and use the AWS CloudHSM JCE provider for Client SDK 5](https://docs.aws.amazon.com/cloudhsm/latest/userguide/java-library-install_5.html) in the AWS CloudHSM documentation.

   |   |                                                                                                                                                                                                                                                                               |
   | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | You can't install the JCE provider if you already have the AWS CloudHSM client installed because of the structural changes made to the client between 3.x and 5.x. If you're upgrading from PingAccess 7.2 or earlier, you must remove any existing CloudHSM client software. |

3. Connect the Client SDK to the AWS CloudHSM cluster.

   You can find more information on how to connect the Client SDK in [Bootstrap the Client SDK](https://docs.aws.amazon.com/cloudhsm/latest/userguide/cluster-connect.html#connect-how-to) in the AWS CloudHSM documentation. Use the **JCE provider** tab.

4. Run the appropriate command for your operating system to ensure that keys are available to use.

   |   |                                                                                               |
   | - | --------------------------------------------------------------------------------------------- |
   |   | You must complete this step even if you don't plan to use a cluster containing multiple HSMs. |

   #### Choose from:

   * On Linux operating systems, run the `sudo /opt/cloudhsm/bin/configure-jce --disable-key-availability-check` command.

   * On Windows operating systems, run the `C:\Program Files\Amazon\CloudHSM\bin\configure-jce.exe --disable-key-availability-check` command.

5. If you plan to use elliptic curve (EC) keys for decryption, run the appropriate command for your operating system.

   #### Choose from:

   * On Linux operating systems, run the `sudo /opt/cloudhsm/bin/configure-jce --enable-ecdh-without-kdf` command.

   * On Windows operating systems, run the `C:\Program Files\Amazon\CloudHSM\bin\configure-jce.exe --enable-ecdh-without-kdf` command.

6. Configure a new PingAccess installation on the network interconnected to the HSM.

   You can find more information on how to install PingAccess in [Installing PingAccess on your system](../installing_and_uninstalling_pingaccess/pa_installing_pa_on_your_system.html).

   |   |                                                                                                               |
   | - | ------------------------------------------------------------------------------------------------------------- |
   |   | To integrate an existing PingAccess installation with your HSM, skip this step and proceed to step 7 instead. |

7. To enable the Java interface and PingAccess integration, copy the `cloudhsm-jce-5.x.0.jar` file to the `pingaccess/deploy` directory.

   |   |                                                                                                                                                                                                                       |
   | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | * On Linux operating systems, the file location is `/opt/cloudhsm/java/cloudhsm-jce-5.x.0.jar`.

   * On Windows operating systems, the file location is `C:\Program Files\Amazon\CloudHSM\java\cloudhsm-jce-5.x.0.jar`. |

### Next steps

Return to [Adding an AWS CloudHSM provider](pa_adding_an_aws_cloudhsm_provider.html) to finish setting up an AWS CloudHSM provider in the admin console.

## Upgrading from Client SDK 3 to Client SDK 5

### About this task

Upgrading from Client SDK 3 to Client SDK 5 requires you to have a source version of PingAccess that you plan to upgrade to or past a target version of PingAccess 7.3 or later.

To upgrade the AWS CloudHSM Client SDK from 3.x to 5.x to integrate it with a target version of PingAccess 7.3 or later:

### Steps

1. Ensure that the source version of PingAccess that you plan to upgrade to or past version 7.3 is running.

   |   |                                                             |
   | - | ----------------------------------------------------------- |
   |   | Do not stop this source version of PingAccess until step 7. |

2. Stop the CloudHSM 3 standalone client with the `sudo service cloudhsm-client stop` command.

3. Move or delete the `/opt/cloudhsm` file.

   |   |                                                                                                                                                                                                                                                                       |
   | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | You can't complete step 4 if you already have the AWS CloudHSM client installed because of the structural changes made to the client between 3.x and 5.x. If you are upgrading from PingAccess 7.2 or earlier, you must remove any existing CloudHSM client software. |

4. Install the JCE 5 client.

   For more information, see [Install and use the AWS CloudHSM JCE provider for Client SDK 5](https://docs.aws.amazon.com/cloudhsm/latest/userguide/java-library-install_5.html) in the AWS CloudHSM documentation.

5. Copy the `cloudhsm-5.x.0.jar` file into the `pingaccess/deploy` directory of the target version of PingAccess that you plan to upgrade to.

6. Run the PingAccess upgrade.

   For more information, see [Upgrading PingAccess](../upgrading_pingaccess/pa_upgrading_pa_landing_topic.html).

7. Stop the source version of PingAccess.

   For more information, see [Stopping PingAccess](../installing_and_uninstalling_pingaccess/pa_stopping_pa.html).

### Result

You have upgraded to your target version of PingAccess and integrated AWS CloudHSM Client SDK 5 with it.

---

---
title: Adding application resources
description: Add application resources to existing applications in PingAccess.
component: pingaccess
version: 9.1
page_id: pingaccess:pingaccess_user_interface_reference_guide:pa_adding_application_resources
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/pingaccess_user_interface_reference_guide/pa_adding_application_resources.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 9, 2026
section_ids:
  about-this-task: About this task
  steps: Steps
  choose-from: Choose from:
  choose-from-2: Choose from:
  choose-from-3: Choose from:
  choose-from-4: Choose from:
  choose-from-5: Choose from:
  choose-from-6: Choose from:
---

# Adding application resources

Add application resources to existing applications in PingAccess.

## About this task

An application resource is a component within an application that requires a different level of security. These instructions describe how to add, edit, and delete application resources and how to configure resource ordering, authentication policy, and application type.

There are two resource types: standard and virtual.

* Standard resources

  Standard resources exist on the target destination, and users can be directed to them.

* Virtual resources

  Virtual resources exist only in PingAccess. When a user attempts to access them, PingAccess generates a specified response.

|   |                                                                                                                                                                                                                                                                                                                                  |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Some applications allow you to specify the parameters of a request in the query string or the POST body. If you are managing such an application and are defining its resources using query parameters, use caution when defining the resource to ensure that PingAccess and the application treat the resource in the same way. |

## Steps

1. Click **Applications**, then go to **Applications > Applications**.

2. Click to expand the application that you want to modify resources on, then click the **Pencil** icon and click the **Resources** tab.

   ### Choose from:

   * To add a resource, click **Add Resource**.

     |   |                                                                                                                                                                                                                                                                             |
     | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
     |   | A group containing all global unprotected resources is displayed on the first **Resources** page. Review this list before adding a resource to make sure that there won't be a conflict between the new resource's path patterns and any unprotected resource path pattern. |

   * To edit a resource, expand the resource and click the **Pencil** icon.

   * To delete the resource, expand the resource and click the **Delete** icon.

3. Enter a unique **Name** of up to 64 characters, including special characters and spaces.

4. Enter a list of Uniform Resource Locator (URL) *(tooltip: \<div class="paragraph">
   \<p>Identifies a resource according to its internet location.\</p>
   \</div>)* path patterns within the context root that identify this resource.

   If [resource ordering](pa_application_resources.html#section_ys3_mhr_ddb) is enabled, select the path pattern type, **Basic** or **Regex**.

   The path pattern must start with a forward slash (/). It begins after the application context root and extends to the end of the URL.

   If automatic path pattern evaluation ordering is in use (default), patterns can contain one or more wildcard characters (`*`). No use of wildcards is assumed. For example, there is a difference between `/app/` and `/app/*`. If a request matches more than one resource, the most specific match is used.

   If you enable manual path pattern ordering (resource ordering), you can use regular expressions in the path pattern. When one or more path patterns contain a regular expression, you can't revert to automatic path pattern ordering unless you remove that path pattern

   |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | If you have specified a regular expression, make sure that you select the **Regex** path pattern type. If you don't, the pattern will be interpreted incorrectly as a **Basic** text string.The application reserved path can't be used as a path pattern when the context root is `/`. The default application reserved path is `/pa`(`/pa*`). You can modify the default application reserved path using the PingAccess admin application programming interface (API) *(tooltip: \<div class="paragraph">&#xA;\<p>A specification of interactions available for building software to access an application or service.\</p>&#xA;\</div>)*.If you selected the **Use context root as reserved resource base path** checkbox on your application, you can't use the application context root as a path pattern either. This checkbox turns the application context root into a reserved resource, and a reserved application context root can't be used in an application's resource paths. |

5. If you have enabled resource ordering, select an option in the **Query Parameters** section.

   The **Query Parameters** section lets you define the resource by query parameters in addition to path patterns.

   ### Choose from:

   * To define the resource without regard to query parameters, select **Match Any**.

   * To define the resource using one or more query parameters, select **Match Specific**:

     * Select **Matches No Parameters** to match the result to the resource if no query parameters are present and if at least one query parameter is present and matches. If this option is deselected, at least one query parameter must be present and must match.

     * Enter one or more **Name**-**Value** pairs, or enter a **Name** and select **Any** to match any value for the given name.

6. Select a **Resource Authentication** type.

   ### Choose from:

   * If the resource requires the same authentication as the root application, select **Standard**.

   * If this resource has no authentication requirements, select **Anonymous**. Identity mappings are still applied if the user is already authenticated. Access control and processing rules are applied where applicable.

   * If this resource has no authentication requirements, select **Unprotected**. Processing rules are applied where applicable. No application or resource access control policy is applied.

   |   |                                                                                                                                                                                                                                            |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
   |   | These options are not available for unprotected applications.* Web applications are unprotected when they don't have an associated web session.

   * API applications are unprotected when they aren't protected by an authorization server. |

7. If the application is a protected web application with a web session, select an **Authentication Challenge Policy** to generate authentication challenge responses for the resource or click **[icon: plus, set=fa]Create** to create a new authentication challenge policy. Otherwise, proceed to the next step.

8. If you are using the PingOne Protect integration on a protected web application, select a **Risk Policy** to enforce on the resource or click **+Create** to create a new risk policy. Otherwise, proceed to the next step.

   |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
   | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | You must set up a PingOne connection before you can create a risk policy. You can find more information on how to set these up through the administrative console in [Adding a PingOne connection](pa_adding_a_p1_connection.html) and [Adding a risk policy](pa_adding_a_risk_policy.html). You can find more information on the capabilities that a risk policy can provide in [PingOne Protect integration](../agents_and_integrations/pa_p1risk_policy_eval_integration.html).A risk policy applied at the resource level takes precedence over one applied at the application level. PingOne risk policies depend on mapping user identity attributes to the risk evaluation requests, so the PingAccess administrative console will prevent you from saving an unprotected application or resource with a risk policy. |

9. (Optional) If you're using an **API** or **Web + API** type application and want to configure different DPoP settings for the application resource than the global DPoP settings that you configured in the [token provider](pa_token_provider.html):

   |   |                                                                                                                         |
   | - | ----------------------------------------------------------------------------------------------------------------------- |
   |   | If you are using PingFederate as the token provider, you must use PingFederate 11.3 or later to configure DPoP support. |

   1. Select **Override DPoP Settings**.

   2. In the **DPoP Type** list, select the level of OAuth 2.0 Demonstrating Proof of Possession (DPoP) support that you want to enable for access token validation:

      * **Off** (default): PingAccess doesn't accept DPoP-bound access tokens, only bearer tokens.

      * **Enabled**: PingAccess accepts both bearer tokens and DPoP-bound access tokens.

      * **Required**: PingAccess doesn't accept bearer tokens, only DPoP-bound access tokens.

   3. To require each DPoP proof to contain a nonce value during validation that was provided by PingAccess when the access token was created, per [RFC 9449 section 9](https://www.rfc-editor.org/rfc/inline-errata/rfc9449.html#:~:text=Next%20Nonce%20Value-,9.%20%20Resource%20Server%2DProvided%20Nonce,-Resource%20servers%20can), select **Require Nonce**.

      This check box is cleared by default.

   4. In the **DPoP Proof Lifetime (SEC.)** field, enter the duration, in seconds, that a DPoP proof should be considered valid after it's issued.

      |   |                                                                                                                                                    |
      | - | -------------------------------------------------------------------------------------------------------------------------------------------------- |
      |   | As a security best practice, keep this value low and consistent with the DPoP implementation of your API client. The default value is 120 seconds. |

10. In the **Methods** list, select one or more methods supported by the resource.

    You can find a list of common HTTP methods and their intended usage in [RFC 9110: HTTP Semantics](https://www.rfc-editor.org/rfc/rfc9110.html#section-9).

    |   |                                                                      |
    | - | -------------------------------------------------------------------- |
    |   | PingAccess doesn't support the `CONNECT`, `PRI`, or `QUERY` methods. |

    Leave the asterisk default if the resource supports all other HTTP methods, including custom methods.

    Defining methods for a resource allows more fine-grained access control policies on resources. If you have a server optimized for writing data (POST, PUT) and a server optimized for reading data (GET), you might want to segment traffic based on the operation being performed.

11. To log information about the transaction to the audit store, select the **Audit** checkbox.

12. If the application type is **Web + API**, and **SPA Support** is disabled on the root application, indicate whether the application resource should override the fallback type specified for the main application.

    If you select **Yes** for this option, select the method to be used for the application resource when a request doesn't contain a web session cookie or OAuth *(tooltip: \<div class="paragraph">
    \<p>A standard framework that enables an application (OAuth client) to obtain access tokens from an OAuth authorization server for the purpose of retrieving protected resources on a resource server.\</p>
    \</div>)* token.

    |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
    | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    |   | Carefully consider your configuration when making this selection. Changing the application fallback type can have unexpected effects on resources that do not override the fallback.For example, if you configure a **Web + API** application with a fallback type of **Web** along with several resources that do not override the fallback type, these resources will emit a `401` response (rather than a `302` to PingFederate) if you later change the fallback type to **API** on the main application.The PingAccess runtime uses fallback type to determine which processing flow (Web or API) to use when the request doesn't contain a web session or an API OAuth Bearer token. When a request doesn't contain either of these authentication mechanisms, it relies on this configuration to determine which processing flow to use. |

13. To enable the resource, select the **Enabled** checkbox.

14. In the **Resource Type** list, select a resource type:

    ### Choose from:

    * If the resource exists on the target destination, select **Standard**.

    * If the resource only exists in PingAccess, select **Virtual**. PingAccess generates a response when a user attempts to access the resource.

15. If you selected the **Virtual** resource type, in the **Type** list, select a response generator type:

    ### Choose from:

    * To redirect the user to a new URL with the specified response code, select **Redirect**.

    * To create a response using a specified template, select **Template**.

    * To make user attributes available to other applications as a JavaScript Object Notation (JSON) *(tooltip: \<div class="paragraph">
      \<p>An open, lightweight data-interchange format that uses human-readable text to store and transmit data.\</p>
      \</div>)* payload, select **JSON Identity Mapping**.

    * To end the application web session and optionally redirect the user to a specific landing page after logout, select **Logout**. All applications using the same web session are logged out.

      |   |                                                                                                         |
      | - | ------------------------------------------------------------------------------------------------------- |
      |   | You can only use the **Logout** virtual resource type if PingFederate is the configured token provider. |

16. If you selected the **Redirect** response generator, specify the redirect parameters:

    1. In the **Redirect URL** field, enter a relative or absolute URL to which users should be redirected.

    2. In the **Response Code** list, select a response code:

       * **301 – Moved permanently**

         This is a permanent redirect that doesn't require the redirect to maintain the original HTTP method.

       * **302 – Found**

         This is a temporary redirect that doesn't require the redirect to maintain the original HTTP method.

       * **307 – Temporary Redirect**

         This is a temporary redirect that requires the redirect to maintain the original HTTP method.

       * **308 – Permanent Redirect**

         This is a permanent redirect that requires the redirect to maintain the original HTTP method.

    3. To opt out of automatic URL encoding, deselect the **Encode URL** checkbox.

       Learn more in the **Opt out of automatic URL encoding** release note in [PingAccess 8.1 (June 2024)](../release_notes/pa_release_notes.html#previous-releases).

17. If you selected the **Template** response generator, specify the template parameters:

    1. In the **Media Type** list, select or enter a media type for the template.

    2. In the **Template** field, enter a template in Velocity Template Language (VTL).

       When a user accesses the virtual resource, the template is processed and returned as the response. The template can include information about the user, resource, and application according to the following data model.

       > **Collapse: Data model**
       >
       > * `application.name` (string)
       >
       >   The name of the requested application.
       >
       > * `application.realm` (string)
       >
       >   The OAuth *(tooltip: \<div class="paragraph">
       >   \<p>A standard framework that enables an application (OAuth client) to obtain access tokens from an OAuth authorization server for the purpose of retrieving protected resources on a resource server.\</p>
       >   \</div>)* realm associated with the application. If the realm isn't defined by the application, it is inferred to be the requested authority and the application's context root.
       >
       > * `cspNonce` (string)
       >
       >   Use this variable to add a nonce attribute to any inline JavaScript.
       >
       > * `exchangeId` (string)
       >
       >   The ID of the current transaction.
       >
       > * `identity.attributes` (object)
       >
       >   Contains user attributes set by the token provider. For example, `identity.attributes.role` could contain a role set by the token provider. This property is only available if the user is authenticated.
       >
       > * `identity.subject` (string)
       >
       >   The subject name of the identity. This property is only available if the user is authenticated.
       >
       > * `identity.trackingID` (string)
       >
       >   The tracking ID of the identity. This property is only available if the user is authenticated.
       >
       > * `resource.name` (string)
       >
       >   The name of the requested resource.

    3. In the **Response Code** list, select a response code:

       * `200`: OK

       * `201`: Created

       * `400`: Bad Request

       * `401`: Unauthorized

       * `403`: Forbidden

       * `404`: Not Found

       * `405`: Method Not Allowed

18. If you selected the **JSON Identity Mapping** response generator, select **Inclusion List** or **Exclusion List**:

    ### Choose from:

    * To map the specified attributes to corresponding property names, select **Inclusion List**. If you select this option, enter a corresponding **Attribute Name** and **Property Name** on each row. Click **[icon: plus, set=fa]Add Row** to add additional rows.

    * To expose all attributes except for those you specify, select **Exclusion List**. If you select this option, enter zero or more excluded attributes in the **Excluded Attributes** field.

19. If you selected the **Logout** response generator, specify the logout parameters:

    1. (Optional) In the **Post-logout Redirect URI** field, enter a Uniform Resource Identifier (URI) *(tooltip: \<div class="paragraph">
       \<p>Identifies a web resource with a string of characters conforming to a specified format.\</p>
       \</div>)* to which the user is directed after logout. The format of this URI determines the logout behavior:

       * No URI: single logout (SLO) *(tooltip: \<div class="paragraph">
         \<p>The process of signing a user out of multiple sites where the user has started a SSO session.\</p>
         \</div>)* defaults to the token provider settings.

       * Absolute URL without variables: The PingAccess session is cleared and SLO isn't triggered.

       * URL containing the `${SLO}` variable: The `${SLO}` variable is replaced with the PingFederate `ping_end_session_endpoint`, which triggers SLO.

         For example, if the PingFederate `ping_end_session_endpoint` is `https://pingfederate:9031/idp/startSLO.ping`, a value of `${SLO}?TargetResource=https://example.com` would direct the user to the PingFederate endpoint, trigger SLO, and then redirect the user to `https://example.com`.

       * Relative path: The relative path is appended to the application path to form the destination and SLO isn't triggered.

       * PingFederate parameters: The parameters are passed to PingFederate and SLO is triggered. You can find more information in [IdP endpoints](https://docs.pingidentity.com/pingfederate/latest/developers_reference_guide/pf_idp_endpoints.html).

    2. To opt out of automatic URL encoding, deselect the **Encode URL** checkbox.

       Learn more in the **Opt out of automatic URL encoding** release note in [PingAccess 8.1 (June 2024)](../release_notes/pa_release_notes.html#previous-releases).

    3. If session validation and single logout aren't available with the token provider, you can select the **Revoke Access Token** checkbox to prevent session replay after a user signs off.

       Access token revocation should be compatible with any OIDC provider. Error messages are available in the PingAccess error log. When you enable this checkbox, PingAccess:

       * Sends an access token revocation request for the associated application to the token provider during sign off, per [RFC 7009](https://www.rfc-editor.org/rfc/rfc7009.txt). This prevents potential bad actors from using stored cookies during future authorization requests when PingAccess must refresh the user attributes.

         |   |                                                                                                                                         |
         | - | --------------------------------------------------------------------------------------------------------------------------------------- |
         |   | For the access token revocation request, PingAccess uses the client credentials configured on the associated application's web session. |

       * Clears user attributes from the local cache on the engine that received the sign-off request if the **Cache User Attributes** setting is enabled.

20. Click **Save**.

---

---
title: Adding certificates to key pairs
description: To modify the certificates included in a chain, remove the certificates from the key pair and add them again. Alternatively, delete the certificate and recreate it by importing a new certificate file and adding certificates to the key pair.
component: pingaccess
version: 9.1
page_id: pingaccess:pingaccess_user_interface_reference_guide:pa_adding_certificates_to_key_pairs
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/pingaccess_user_interface_reference_guide/pa_adding_certificates_to_key_pairs.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 21, 2023
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Adding certificates to key pairs

## About this task

|   |                                                                                                                                                                                                                                                  |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | To modify the certificates included in a chain, remove the certificates from the key pair and add them again. Alternatively, delete the certificate and recreate it by importing a new certificate file and adding certificates to the key pair. |

To add a certificate to an existing key pair:

## Steps

1. Click **Security**, then go to **Key Pairs > Key Pairs**.

2. Click to expand an existing key pair.

3. In the **Key Pair Chain Certificate** list, select **Add Certificate**.

4. To browse for and select the certificate file, click **Choose File**.

5. Click **Add**.

---

---
title: Adding certificates to trusted certificate groups
description: Add a certificate to an existing trusted certificate group.
component: pingaccess
version: 9.1
page_id: pingaccess:pingaccess_user_interface_reference_guide:pa_adding_certificates_to_trusted_certificate_groups
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/pingaccess_user_interface_reference_guide/pa_adding_certificates_to_trusted_certificate_groups.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: February 6, 2023
section_ids:
  steps: Steps
---

# Adding certificates to trusted certificate groups

Add a certificate to an existing trusted certificate group.

## Steps

1. Click **Security**, then go to **Certificates > Trusted Certificate Groups**.

2. Drag a certificate into an existing trusted certificate group.

---

---
title: Adding global unprotected resources
description: Create a new global unprotected resource in PingAccess.
component: pingaccess
version: 9.1
page_id: pingaccess:pingaccess_user_interface_reference_guide:pa_adding_global_unprotected_resources
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/pingaccess_user_interface_reference_guide/pa_adding_global_unprotected_resources.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: February 6, 2023
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Adding global unprotected resources

Create a new global unprotected resource in PingAccess.

## About this task

|   |                                                                                                                                                                                                                                                                                                                                                                |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The following steps describe how to globally make resources unprotected. Because any resource captured by the wildcard path of any entry is left unprotected for all applications, you must carefully plan these entries. To make a resource unprotected for a specific application, see [Adding application resources](pa_adding_application_resources.html). |

## Steps

1. Click **Applications**, then go to **Applications > Global Unprotected Resources**.

2. Click **[icon: plus, set=fa]Add Global Unprotected Resource**.

3. In the **Name** field, enter a name for the entry.

4. **Optional:** In the **Description** field, enter a description for the entry.

5. **Optional:** If you want to record access requests for this resource in the audit store, select the **Audit** check box.

6. In the **Path Pattern** field, specify the path pattern that identifies the global unprotected resource.

   This entry must start with a forward-slash (/) and can contain one or more wildcard characters (`*`), such as:

   * `/*.jpg`

   * `/resources/*.css`

   * `/*/resources/favicon.ico`

     |   |                                                                                                                                                                                                                                                              |
     | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
     |   | Global unprotected resource paths are relative to the application context root. Reserved paths such as `/pa`, `/pa/`, or `/pa/*` are allowed at the global level, but will not be evaluated for applications that are configured with a context root of `/`. |

7. To enable the global unprotected resource, select the **Enabled** check box.

8. Click **Save**.

---

---
title: Adding Groovy script rules
description: Add a Groovy script rule to provide advanced rule logic that extends PingAccess rule development beyond the capabilities of the packaged Rules.
component: pingaccess
version: 9.1
page_id: pingaccess:pingaccess_user_interface_reference_guide:pa_adding_groovy_script_rules
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/pingaccess_user_interface_reference_guide/pa_adding_groovy_script_rules.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 17, 2023
section_ids:
  about-this-task: About this task
  steps: Steps
  example: Example:
  choose-from: Choose from:
---

# Adding Groovy script rules

Add a Groovy script rule to provide advanced rule logic that extends PingAccess rule development beyond the capabilities of the packaged [Rules](pa_rules.html).

## About this task

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Through Groovy scripts, PingAccess administrators can perform sensitive operations that might affect system behavior and security. Since the regular Groovy rule and the OAuth *(tooltip: \<div class="paragraph">&#xA;\<p>A standard framework that enables an application (OAuth client) to obtain access tokens from an OAuth authorization server for the purpose of retrieving protected resources on a resource server.\</p>&#xA;\</div>)* Groovy rule differ in the scope of their functionality, the relevant rules are tagged for Web App or for application programming interface (API) *(tooltip: \<div class="paragraph">&#xA;\<p>A specification of interactions available for building software to access an application or service.\</p>&#xA;\</div>)*, respectively, in the rules list. |

## Steps

1. Click **Access**, then go to **Rules > Rules**.

2. Click **[icon: plus, set=fa]Add Rule**.

3. In the **Name** field, enter a unique name, up to 64 characters long.

   Special characters and spaces are allowed.

4. In the **Type** list, select **Groovy Script (for Web App)**.

5. In the **Groovy Script** field, enter the Groovy script to use for rule evaluation.

   ### Example:

   To validate that an HTTP request does not come from Internet Explorer, you might include the `requestHeaderDoesntContain("User-Agent", "InternetExplorer")` PingAccess matcher in your Groovy script.

   Groovy script rules must end execution with a matcher instance. For more information, see [Matcher usage reference](../reference_guides/pa_matcher_usage_ref.html).

6. To configure rejection handling, click **Show Advanced Settings**, then select a rejection handling method.

   ### Choose from:

   * If you select **Default**, use the **Rejection Handler** list to select an existing [rejection handler](pa_rejection_handlers.html) that defines whether to display an error template or redirect to a URL.

   * If you select **Basic**, you can customize an error message to display as part of the default error page rendered in the end user's browser if rule evaluation fails. This page is among the templates you can modify with your own branding or other information. If you select **Basic**, provide the following:

     1. In the **Error Response Code** field, enter the HTTP status response code to send if rule evaluation fails.

        The default is `403`.

     2. In the **Error Response Status Message** field, enter the HTTP status response message to send if rule evaluation fails.

        The default is `Forbidden`.

     3. In the **Error Response Template File** field, enter the HTML template page for customizing the error message that displays if rule evaluation fails. This template file is located in the `<PA_HOME>/conf/template/` directory.

     4. From the **Error Response Content Type** list, select the type of content for the error response.

        This lets the client properly display the response.

7. Click **Save**.

---

---
title: Adding HTTP request header rules
description: Add an HTTP request header rule to examine a request and determine whether to grant access to a requested resource based on a match found in one of the specified headers in the HTTP request.
component: pingaccess
version: 9.1
page_id: pingaccess:pingaccess_user_interface_reference_guide:pa_adding_http_request_header_rules
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/pingaccess_user_interface_reference_guide/pa_adding_http_request_header_rules.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: February 13, 2023
section_ids:
  about-this-task: About this task
  steps: Steps
  choose-from: Choose from:
---

# Adding HTTP request header rules

Add an HTTP request header rule to examine a request and determine whether to grant access to a requested resource based on a match found in one of the specified headers in the HTTP request.

## About this task

If more than one **Field** and **Value** pair is listed, then all conditions must match in order for the rule to succeed.

## Steps

1. Click **Access**, then go to **Rules > Rules**.

2. Click **[icon: plus, set=fa]Add Rule**.

3. In the **Name** field, enter a unique name, up to 64 characters long.

   Special characters and spaces are allowed.

4. From the **Type** list, select **HTTP Request Header**.

5. In the **Field** column, in the **Header** field, enter a header name you want to match to grant or not grant the client access.

6. In the **Value** field, enter a value for the header you want to match in order to grant or not grant the client access.

   The wildcard (`*`) character is supported.

   |   |                                                                                                                                                                                         |
   | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | If you want to match on the `Host` header, include both the host and port in the **Value** field, or add a wildcard after the hostname (`host*` or `host:*`) to match the HTTP request. |

7. If additional header pairs are needed, click **Add Row** to add an additional row, then repeat steps 5-6.

8. If the values should be an exact match to the value case, select the **Case Sensitive** check box.

9. If access is not allowed when a match is found, select the **Negate** check box.

   |   |                                                                                                                                                                                                                                                                                                                                  |
   | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | Ensure that the attribute name entered in the **Field** field is spelled correctly and exists. If you enter an attribute that does not exist and you select **Negate**, the rule will always succeed. The **Negate** control applies to the entire set of conditions specified, and passes the rule if any condition is not met. |

10. To configure rejection handling, click **Show Advanced Settings**, then select a rejection handling method.

    ### Choose from:

    * If you select **Default**, use the **Rejection Handler** list to select an existing [rejection handler](pa_rejection_handlers.html) that defines whether to display an error template or redirect to a URL.

    * If you select **Basic**, you can customize an error message to display as part of the default error page rendered in the end user's browser if rule evaluation fails. This page is among the templates you can modify with your own branding or other information. If you select **Basic**, provide the following:

      1. In the **Error Response Code** field, enter the HTTP status response code to send if rule evaluation fails.

         The default is `403`.

      2. In the **Error Response Status Message** field, enter the HTTP status response message to send if rule evaluation fails.

         The default is `Forbidden`.

      3. In the **Error Response Template File** field, enter the HTML template page for customizing the error message that displays if rule evaluation fails. This template file is located in the `<PA_HOME>/conf/template/` directory.

      4. From the **Error Response Content Type** list, select the type of content for the error response.

         This lets the client properly display the response.

11. Click **Save**.

---

---
title: Adding HTTP request parameter rules
description: Add an HTTP request parameter rule to examine a request and determine whether to grant access to a requested resource based on a match found in specified form parameters of the HTTP request.
component: pingaccess
version: 9.1
page_id: pingaccess:pingaccess_user_interface_reference_guide:pa_adding_http_request_parameter_rules
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/pingaccess_user_interface_reference_guide/pa_adding_http_request_parameter_rules.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: February 13, 2023
section_ids:
  about-this-task: About this task
  steps: Steps
  choose-from: Choose from:
---

# Adding HTTP request parameter rules

Add an HTTP request parameter rule to examine a request and determine whether to grant access to a requested resource based on a match found in specified form parameters of the HTTP request.

## About this task

Add an HTTP request parameter rule determines if the parameters are passed as part of the Uniform Resource Locator (URL) *(tooltip: \<div class="paragraph">
\<p>Identifies a resource according to its internet location.\</p>
\</div>)* query string parameters or as part of a request body submitted using an HTTP PUT or POST method. If the request is a POST request, the `content-type` must be set to `application/x-www-form-urlencoded` to process the field names in the request.

If this rule is applied to an agent configuration, only URL query string parameters are compared, because the agent does not receive the request body for processing.

If more than one **Field** and **Value** pair is listed, then all conditions must match for the rule to succeed.

## Steps

1. Click **Access**, then go to **Rules > Rules**.

2. Click **[icon: plus, set=fa]Add Rule**.

3. In the **Name** field, enter a unique name, up to 64 characters long.

   Special characters and spaces are allowed.

4. From the **Type** list, select **HTTP Request Parameter**.

5. In the **Field** column, in the **Parameter** field, enter a parameter name you want to match to grant or not grant the client access.

6. In the **Value** field, enter a value for the parameter you want to match in order to grant or deny the client access.

   The wildcard (`*`) character is supported.

   |   |                                                                                                                                                                                                                                                       |
   | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | Values entered here will be URL-encoded prior to the comparison. For example, if the value specified in the **Value** field is `v1 v2`, when the engine performs the comparison, this value will convert to `v1%20v2` before the search is performed. |

7. If additional parameters pairs are needed, click **Add Row** to add an additional row, then repeat steps 5-6.

8. If the values should be an exact match to the value case, select the **Case Sensitive** check box.

9. If access is not allowed when a match is found, select the **Negate** check box.

   |   |                                                                                                                                                                                                                                                                                                         |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | Ensure that the field name you enter is spelled correctly and exists. If you enter a field name that does not exist and you select **Negate**, the rule will always succeed. The **Negate** control applies to the entire set of conditions specified, and passes the rule if any condition is not met. |

10. To configure rejection handling, click **Show Advanced Settings**, then select a rejection handling method.

    ### Choose from:

    * If you select **Default**, use the **Rejection Handler** list to select an existing [rejection handler](pa_rejection_handlers.html) that defines whether to display an error template or redirect to a URL.

    * If you select **Basic**, you can customize an error message to display as part of the default error page rendered in the end user's browser if rule evaluation fails. This page is among the templates you can modify with your own branding or other information. If you select **Basic**, provide the following:

      1. In the **Error Response Code** field, enter the HTTP status response code to send if rule evaluation fails.

         The default is `403`.

      2. In the **Error Response Status Message** field, enter the HTTP status response message to send if rule evaluation fails.

         The default is `Forbidden`.

      3. In the **Error Response Template File** field, enter the HTML template page for customizing the error message that displays if rule evaluation fails. This template file is located in the `<PA_HOME>/conf/template/` directory.

      4. From the **Error Response Content Type** list, select the type of content for the error response.

         This lets the client properly display the response.

11. Click **Save**.

---

---
title: Adding network range rules
description: Add a network range rule to examine a request and determine whether to grant access to a target site based on whether the IP address falls within a specified range, using Classless Inter-Domain Routing notation.
component: pingaccess
version: 9.1
page_id: pingaccess:pingaccess_user_interface_reference_guide:pa_adding_network_range_rules
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/pingaccess_user_interface_reference_guide/pa_adding_network_range_rules.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: February 6, 2023
section_ids:
  steps: Steps
  choose-from: Choose from:
---

# Adding network range rules

Add a network range rule to examine a request and determine whether to grant access to a target site based on whether the IP address falls within a specified range, using Classless Inter-Domain Routing notation.

## Steps

1. Click **Access**, then go to **Rules > Rules**.

2. Click **[icon: plus, set=fa]Add Rule**.

3. In the **Name** field, enter a unique name, up to 64 characters long.

   Special characters and spaces are allowed.

4. From the **Type** list, select **Network Range**.

5. In the **Network Range** field, enter a network range value, such as `127.0.0.1/8`.

   PingAccess supports IPv4 addresses.

6. Select **Negate** if when a match is found, access is not allowed.

7. If you want to override source address handling defined in the **HTTP Requests** configuration, click **Show Advanced Settings** and perform the following steps:

   1. Click **Override Request IP Source Configuration**.

   2. In the **Headers** field, enter the headers used to define the source IP address to use.

   3. Select the **Header Value Location** to use when multiple addresses are present in the specified header.

      Valid values are `Last` (the default) and `First`.

   4. Click **Fall Back to Last Hop IP** to determine if, when the specified **Headers** are not present, PingAccess should return a `Forbidden` result or if it should use the address of the previous hop as the source to make policy decisions.

   5. To configure rejection handling, select a rejection handling method:

      ### Choose from:

      * If you select **Default**, use the **Rejection Handler** list to select an existing [rejection handler](pa_rejection_handlers.html) that defines whether to display an error template or redirect to a URL.

      * If you select **Basic**, you can customize an error message to display as part of the default error page rendered in the end-user's browser if rule evaluation fails. This page is among the templates you can modify with your own branding or other information. If you select **Basic**, provide the following:

        1. In the **Error Response Code** field, enter the HTTP status response code to send if rule evaluation fails.

           The default is `403`.

        2. In the **Error Response Status Message** field, enter the HTTP status response message to send if rule evaluation fails.

           The default is `Forbidden`.

        3. In the **Error Response Template File** field, enter the HTML template page for customizing the error message that displays if rule evaluation fails.

           This template file is located in the `<PA_HOME>/conf/template/` directory.

        4. In the **Error Response Content Type** list, select the type of content for the error response.

           This lets the client properly display the response.

8. Click **Save**.

---

---
title: Adding OAuth attribute rules
description: Add an OAuth attribute rule to examine a request and determine whether to grant access to a target service based on a match found between the attributes associated with an OAuth access token and attribute values specified in the rule.
component: pingaccess
version: 9.1
page_id: pingaccess:pingaccess_user_interface_reference_guide:pa_adding_oauth_attribute_rules
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/pingaccess_user_interface_reference_guide/pa_adding_oauth_attribute_rules.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: February 6, 2023
section_ids:
  steps: Steps
  choose-from: Choose from:
---

# Adding OAuth attribute rules

Add an OAuth attribute rule to examine a request and determine whether to grant access to a target service based on a match found between the attributes associated with an OAuth access token and attribute values specified in the rule.

## Steps

1. Click **Access**, then go to **Rules > Rules**.

2. Click **[icon: plus, set=fa]Add Rule**.

3. In the **Name** field, enter a unique name, up to 64 characters long.

   Special characters and spaces are allowed.

4. From the **Type** list, select **OAuth Attribute**.

5. From the **Attribute Name** list, select the attribute name you want to match to an attribute associated with an OAuth access token.

6. In the **Attribute Value** field, enter the value to match.

   |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
   | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | The attribute values come from the contract in your OAuth *(tooltip: \<div class="paragraph">&#xA;\<p>A standard framework that enables an application (OAuth client) to obtain access tokens from an OAuth authorization server for the purpose of retrieving protected resources on a resource server.\</p>&#xA;\</div>)* access token manager in PingFederate. For more information, see [Defining access token attribute contract](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_defining_access_token_attribute_contract.html). |

7. Add additional rows of attribute name and value pairs as needed.

   |   |                                                                                      |
   | - | ------------------------------------------------------------------------------------ |
   |   | If multiple rows are included here, all conditions must match for the rule to match. |

8. Select **Negate** if, when a match is found, access is not allowed.

   |   |                                                                                                                                                                                          |
   | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | Verify what you enter for the attribute. If you enter an attribute that does not exist, such as if the attribute is misspelled, and you select **Negate**, the rule will always succeed. |

9. To configure rejection handling, click **Show Advanced Settings**, then select a rejection handling method.

   ### Choose from:

   * If you select **Default**, use the **Rejection Handler** list to select an existing [rejection handler](pa_rejection_handlers.html) that defines whether to display an error template or redirect to a URL.

   * If you select **Basic**, you can customize an error message to display as part of the default error page rendered in the end user's browser if rule evaluation fails. This page is among the templates you can modify with your own branding or other information. If you select **Basic**, provide the following:

     1. In the **Error Response Code** field, enter the HTTP status response code to send if rule evaluation fails.

        The default is `403`.

     2. In the **Error Response Status Message** field, enter the HTTP status response message to send if rule evaluation fails.

        The default is `Forbidden`.

     3. In the **Error Response Template File** field, enter the HTML template page for customizing the error message that displays if rule evaluation fails. This template file is located in the `<PA_HOME>/conf/template/` directory.

     4. From the **Error Response Content Type** list, select the type of content for the error response.

        This lets the client properly display the response.

10. Click **Save**.