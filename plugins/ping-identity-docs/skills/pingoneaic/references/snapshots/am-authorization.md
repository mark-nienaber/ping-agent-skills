---
title: Authorization
description: Overview of authorization features for protecting resources through policies and OAuth 2.0 scopes
component: pingoneaic
page_id: pingoneaic:am-authorization:preface
canonical_url: https://docs.pingidentity.com/pingoneaic/am-authorization/preface.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Authorization", "Policies"]
page_aliases: ["index.adoc", "authorization-guide:preface.adoc"]
---

# Authorization

This guide covers concepts, implementation procedures, and customization techniques for working with the authorization features of Advanced Identity Cloud.

[icon: book, set=fas, size=3x]

#### [Authorization](what-is-authz-decision.html)

Learn how Advanced Identity Cloud determines access according to policies.

[icon: paste, set=fas, size=3x]

#### [Create policies](configuring-policies.html)

Define resources, and protect them by creating authorization policies.

[icon: handshake, set=fas, size=3x]

#### [What is transactional authorization?](transactional-authorization.html)

Use transactional authorization to require additional authorization.

[icon: edit, set=fas, size=3x]

#### [Dynamic OAuth 2.0 scopes](oauth2-authorization.html)

Learn how to grant OAuth 2.0 scopes dynamically.

---

---
title: Authorization and policy decisions
description: Learn authorization concepts including policies, resource protection, and policy decision making
component: pingoneaic
page_id: pingoneaic:am-authorization:what-is-authz-decision
canonical_url: https://docs.pingidentity.com/pingoneaic/am-authorization/what-is-authz-decision.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Authorization", "Policy", "Resource", "Evaluation", "Agents"]
page_aliases: ["authorization-guide:what-is-authz-decision.adoc"]
section_ids:
  protecting-resources-with-policy: Protect resources
  policy-resolution: Policy decisions
  url-normalization: URL normalization
---

# Authorization and policy decisions

Advanced Identity Cloud provides *access management*, which consists of:

* Authentication: determining who is trying to access a resource

* Authorization: determining whether to grant or deny access to the resource

The decision to grant access depends on a number of factors:

* the policies governing access

* who is trying to gain access

* possible additional conditions, such as whether the access needs to happen over a secure channel or what time of day it is.

Advanced Identity Cloud relies on policies to reach authorization decisions, such as whether to grant or deny access to a resource, or to grant or deny OAuth 2.0 scopes.

Related information: [Dynamic OAuth 2.0 authorization](oauth2-authorization.html)

## Protect resources

When you configure policy sets to protect resources, Advanced Identity Cloud acts as the *policy decision point* (PDP), whereas the web and Java policy agents act as *policy enforcement points* (PEP). In other words, an agent or other PEP takes responsibility only for enforcing a policy decision made by Advanced Identity Cloud. When you configure applications and their policies in Advanced Identity Cloud, you use Advanced Identity Cloud as a *policy administration point* (PAP).

Authorization policies work to protect resources in the following way:

1. A PEP requests a policy decision from Advanced Identity Cloud, specifying the target resource(s), the policy set, and information about the subject and environment.

2. Advanced Identity Cloud, as the PDP, retrieves policies within the specified policy set that apply to the target resource(s).

3. Advanced Identity Cloud evaluates the policies to make a decision based on the conditions matching those of the subject and environment.

   When multiple policies apply for a particular resource, the default logic for combining decisions is that the first evaluation resulting in a decision to deny access takes precedence over all other evaluations.

   Advanced Identity Cloud only allows access if all applicable policies evaluate to a decision to allow access.

4. Advanced Identity Cloud communicates the policy decision to the PEP. The decision, applying policy for a subject under the specified conditions, is called an *entitlement*.

   The entitlement indicates the resource(s) it applies to, the actions permitted and denied for each resource, and, optionally, response attributes and *advice*.

![Shows the relationship between realms, policies, and policy sets.](_images/realm-app-policy-overview.png)Figure 1. Policies protecting resources

When Advanced Identity Cloud denies a request due to a failed condition, it can send advice to the PEP, so that the PEP can take remedial action.

For example, a user wants to access a particular website. The website is protected by a policy that requires authentication level 1, but the user authenticated with an email address and password, which is configured as authentication level 0. The user cannot access the website. Advanced Identity Cloud sends advice, prompting the PEP to request the user to reauthenticate using a one-time password to gain authentication level 1. Now Advanced Identity Cloud grants access to the protected page.

## Policy decisions

Advanced Identity Cloud matches policies to resources to make policy decisions.

For a policy to match:

* The resource must match one of the resource patterns defined in the policy.

* The user making the request must match a subject.

* At least one condition for each condition type must be satisfied.

When multiple policies match, the order in which Advanced Identity Cloud uses them to make a policy decision is not deterministic. However, a *deny* decision overrides an *allow* decision. By default, once Advanced Identity Cloud reaches a *deny* decision, it stops checking further policies.

> **Collapse: Example**
>
> Consider the case where Advanced Identity Cloud protects a user profile web page. A web agent installed in the web server intercepts client requests to enforce policy. The policy states that only authenticated users can access the page to view and to update their profile.
>
> When a user browses to their profile page, the web agent intercepts the request. The web agent assesses that the request is to access a protected resource, but comes from a user who has not yet logged in and so has no authorization to visit the page. The web agent redirects the user to Advanced Identity Cloud to authenticate.
>
> Advanced Identity Cloud serves a login page that collects the user's email and password, authenticates the user's credentials, and creates a session for the user. It then redirects the user to the web agent. The web agent gets a policy decision from Advanced Identity Cloud for that specific page and grants access to the page. As long as the user has a valid session with Advanced Identity Cloud, they can browse other pages and then return to their profile page, without having to enter their email and password again.
>
> Notice how Advanced Identity Cloud and the web agent handle the access in the example. The website developer can offer a profile page, but does not have to manage login or handle who can access a page. As an Advanced Identity Cloud administrator, you can change authentication and authorization independently of updates to the website. You might need to agree with website developers on how Advanced Identity Cloud identifies users, so web developers can identify users by their own names when they log in. By using Advanced Identity Cloud and web or Java agents for authentication and authorization, your organization no longer needs to update web applications when you want to add external access to your intranet for roaming users, open some of your sites to partners, only let managers access certain pages of your HR website, or allow users already logged in to their desktops to visit protected sites without having to type their credentials again.

### URL normalization

Before Advanced Identity Cloud matches a resource URL against a policy pattern, it normalizes the URL:

* Path traversals are resolved:

  `http://example.com/a/../b` is resolved to `http://example.com/b`.

  `http://example.com/a/./b` is resolved to `http://example.com/a/b`.

* If no port is specified, the default port for the scheme is added:

  `http://example.com/path` is treated as `http://example.com:80/path`.

  `https://example.com/path` is treated as `https://example.com:443/path`.

* Query string parameters are sorted alphabetically by parameter name:

  `?subject=SPBnfm+t5PlP+ISyQhVlplE22A8=&action=get` and `?action=get&subject=SPBnfm+t5PlP+ISyQhVlplE22A8=` are equivalent.

---

---
title: Authorize one-time access with transactional authz
description: Require users to authorize every access to a resource for one-time or single-use access control
component: pingoneaic
page_id: pingoneaic:am-authorization:transactional-authorization
canonical_url: https://docs.pingidentity.com/pingoneaic/am-authorization/transactional-authorization.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Transactional Authorization", "Policy", "Administration", "Configuration"]
page_aliases: ["authorization-guide:transactional-authorization.adoc"]
section_ids:
  understand_transactional_authorization: Understand transactional authorization
  configure_transactional_authorization: Configure transactional authorization
  the_user_journey: The user journey
  the_policy: The policy
  your_application: Your application
  demonstrate_transactional_authorization: Demonstrate transactional authorization
---

# Authorize one-time access with transactional authz

Transactional authorization requires a user to authorize *every* access to a resource. It's part of an Advanced Identity Cloud policy that grants single-use or one-shot access.

For example, a user might approve a financial transaction with a one-time password (OTP) sent to their device, or respond to a push notification to confirm that they have indeed signed on from an unexpected location.

Performing the extra action successfully grants access to the protected resource but only once. Later attempts to access the resource require the user to perform the configured actions again.

You implement transactional authorization as an environment condition type in an [authorization policy](configuring-policies.html) and affects the [authorization decision](what-is-authz-decision.html).

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | * Transactional authorization isn't designed to work with account lockout and doesn't increment lockout counters. Therefore, don't use transactional authorization with authentication mechanisms that are susceptible to brute force attacks, such as simple username/password authentication, or OTP authentication.

  Configure transactional authorization if you're using a strong authentication mechanism, such as [MFA: Authenticate using push notification](../am-authentication/authn-mfa-about-push.html), that isn't susceptible to brute force attacks. If you *do* use transactional authorization with a weaker authentication mechanism like OTP authentication, you *must* manage rate-limiting in some other way.

* Transactional authorization policies aren't supported for the `JwtClaim` [subject type](rest-api-authz-policies.html#subject-conditions). |

## Understand transactional authorization

The following diagram describes the sequence of events when accessing a resource protected by a REST application and an Advanced Identity Cloud policy that contains a transactional environment condition:

![Sequence of events for transaction authorization.](_images/figure-transactional-how-it-works.svg)Figure 1. Access Resources with Transactional Authorization

The sequence of events for a transaction authorization is as follows:

1. An authenticated user attempts to access a resource that's protected by Advanced Identity Cloud.

2. The REST application, a resource server, contacts Advanced Identity Cloud to evaluate the policies that apply.

3. Because the policy has a transaction environment condition, Advanced Identity Cloud creates a transaction token in the Core Token Service (CTS) store. The initial transaction token state is set to `CREATED`.

   The transaction token includes the following information about the policy evaluation:

   * Realm

   * Resource

   * Subject

   * Audit tracking ID

   * Authentication method

   To protect against tampering, Advanced Identity Cloud verifies that these details don't change and match those in the incoming requests for the duration of the transaction.

   The transaction token has a time-to-live (TTL), defined in the [Transaction Authentication service](../am-reference/services-configuration.html#realm-transaction). The default TTL is 180 seconds. If the transaction is not completed within this time, the token is deleted, and the flow must be restarted. Change the default TTL if the transaction includes authentication actions that take more time to complete. For example, using HOTP authentication for an OTP over email.

   You can configure the time-to-live per realm. Refer to [Transaction Authentication service](../am-reference/services-configuration.html#realm-transaction).

4. In the JSON response to the policy evaluation request, Advanced Identity Cloud returns the transaction ID—​the unique ID of the newly created transaction token—​in the `TransactionConditionAdvice` array of the `advices` object:

   ```json
   {
       "resource": "https://bank.example.com:443/withdraw?amount=100.00",
       "actions": {},
       "attributes": {},
       "advices": {
           "TransactionConditionAdvice": [
               "7b8bfd4c-60fe-4271-928d-d09b94496f84"
           ]
       },
       "ttl": 0
   }
   ```

5. Because the JSON response to the evaluation doesn't grant any actions but contains advices, the REST application (resource server) extracts the transaction ID and returns it to the authentication service to start the authentication.

   The query parameters sent as part of the request for actions include an `authIndexType` of `transaction` and the transaction ID as the `authIndexValue`.

6. Advanced Identity Cloud extracts the transaction ID, verifies the corresponding transaction token, and changes the state to `IN_PROGRESS`.

   If the transaction ID isn't in the expected state or doesn't exist, Advanced Identity Cloud returns a `401 Unauthorized` error. For example:

   ```json
   {
       "code": 401,
       "reason": "Unauthorized",
       "message": "Unable to read transaction.",
       "detail": {
           "errorCode": "128"
       }
   }
   ```

7. Advanced Identity Cloud responds with the callbacks necessary to satisfy any environment conditions.

   |   |                                                                                                                                                                                                                                                               |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | The advices returned by transaction environment conditions have the lowest precedence when compared to the other condition advices. End users must respond to non-transactional condition advices before they respond to the transactional condition advices. |

8. The REST application (resource server) renders the callbacks and presents them to the user.

9. The user completes the required actions.

   For example, the user completes the journey specified in the policy, by responding to a push notification on their registered mobile device to confirm a transaction.

   If the user doesn't complete the required actions, Advanced Identity Cloud returns an HTTP 200 message, and redirects the user to the protected resource. Policy evaluation fails since the transactional authorization process failed.

10. Advanced Identity Cloud verifies the transaction token and changes the state to `COMPLETED`.

11. With the transaction now complete, Advanced Identity Cloud returns the original token.

    Note that the authentication performed as part of an authorization flow does not behave the same as a standard authentication. The differences are:

    * The user's original session isn't upgraded or altered in any way.

    * Failing the authentication during the authorization flow doesn't increment account lockout counters.

12. The REST application (resource server) requests the policy decision again, including the ID of the completed transaction as a value in the `TxId` array of the `environment` object:

    ```json
    {
        "resources" : ["https://bank.example.com:443/withdraw?amount=100.00"],
        "application" : "iPlanetAMWebAgentService",
        "subject" : {
            "ssoToken" : "AQIC5w...*AJTMQAA*"
        },
        "environment": {
            "TxId": ["7b8bfd4c-60fe-4271-928d-d09b94496f84"]
        }
    }
    ```

13. Advanced Identity Cloud verifies that the transaction was authorized and that the transaction token is in the `COMPLETED` state.

14. If the transaction completes successfully, the authorization continues.

    Advanced Identity Cloud marks the transaction token for deletion so that it can't be used to grant more than one access.

15. As the authentication required to complete the transaction was successful, Advanced Identity Cloud returns the result of the policy reevaluation.

    For example, the following response grants the `POST` and `GET` actions to the resource `https://bank.example.com:443/withdraw?amount=100.00`:

    ```json
    {
        "resource": "https://bank.example.com:443/withdraw?amount=100.00",
        "actions": {
            "POST": true,
            "GET": true
        },
        "attributes": {},
        "advices": {},
        "ttl": 0
    }
    ```

    |   |                                                                                                                                                                               |
    | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    |   | Successful transactional authorization responses set the time-to-live (`ttl`) value to zero to ensure that the policy decision isn't cached and can't be used more than once. |

16. The user is able to access the protected resource once.

    Additional attempts to access a resource protected by a policy containing a transactional environment condition require a new transaction to be completed.

## Configure transactional authorization

To use transactional authorization, you must coordinate the configuration of:

* An appropriate user journey for the transaction.

* The Advanced Identity Cloud policy or policies that use the journey.

* Support for transactional authorization in your applications.

### The user journey

The journey communicates to the user what they're authorizing when they approve the transaction, and gives them the means to approve (or reject) the operation.

For example, if the transaction involves a withdrawal from the user's bank account, you could configure a [multi-factor authentication](../am-authentication/authn-introduction-authn.html#about-mfa) journey that displays "Confirm $100 withdrawal from Example Bank?" with Yes and No options for a push notification to a registered device, or sends an OTP to a registered device with a similar message.

Configure the journey in the same realm as the policy.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Consider the following points when configuring the journey:- To prevent users from authenticating directly through this journey, either for security reasons or because the journey is insufficient as a complete authentication service, configure it as a [transactional authentication journey](../am-authentication/configure-authentication-trees.html#configure-transactional-auth-journey).

- You can't use a [Set Failure Details node](https://docs.pingidentity.com/auth-node-ref/latest/set-failure-details.html) with transactional authentication. A failed transaction returns a `200 OK` response, and the node only adds failure details for a `401 Unauthorized` response. |

### The policy

A transactional authorization policy specifies the following:

* The conditions that trigger the required authorization.

* The journey the end user must complete to authorize the transaction.

In other respects, it's a standard Advanced Identity Cloud authorization policy, configured under Native Consoles > Access Management.

The following example policy applies to the `/withdraw` endpoint. Its transactional authorization environment condition specifies that the user must complete the `AuthorizeTransaction` journey to authorize access to the endpoint:

![Policy to approve withdrawls](_images/transactional-authorization-policy.png)

To add the environment condition, set:

* Type

  `Transaction`

* Authentication Strategy

  `Authenticate to Tree`

* Strategy Specifier

  The name of the journey

### Your application

A quick way to protect your application is to use Ping Identity software. PingGateway, Ping SDKs, and agents all support transactional authorization.

* When using PingGateway to protect your application, configure it for use with Advanced Identity Cloud.

  Refer to the [Advanced Identity Cloud](https://docs.pingidentity.com/pinggateway/latest/aic/preface.html) pages in the PingGateway documentation. These pages describe how to use PingGateway as an OAuth 2.0 client of Advanced Identity Cloud and resource server. They also describe and how to use cross-domain single sign on (CDSSO) for applications that aren't in your tenant's domain.

  Also refer to the PingGateway documentation to [configure PingGateway as a policy enforcement point (PEP) when using CDSSO](https://docs.pingidentity.com/pinggateway/latest/gateway-guide/policy-enforcement.html#pep-cdsso). PingGateway as a PEP transparently manages redirection when Advanced Identity Cloud policy requires transactional authorization.

* When using the Ping SDKs, refer to [Perform transactional authorization](https://docs.pingidentity.com/sdks/latest/sdks/use-cases/how-to-perform-transactional-authorization.html).

* When using an agent to protect your application, refer to the Java agent page on [enforcing Advanced Identity Cloud policy decisions](https://docs.pingidentity.com/java-agents/latest/identity-cloud-guide/pep.html) or the web agent page on [enforcing Advanced Identity Cloud policy decisions](https://docs.pingidentity.com/web-agents/latest/identity-cloud-guide/pep.html).

## Demonstrate transactional authorization

After configuring the journey, the policy, and your application, access the protected resource.

The example described here involves a bank withdrawal operation. The following steps put the end user interaction with Advanced Identity Cloud in context:

1. Barbara Jensen browses her online bank at `https://bank.example.com` and signs on to access her account:

   ![Signing on at the online bank](_images/transactional-bank-signon.png)

2. Barbara prepares to withdraw $100 from her account using the online bank application.

   The application as PEP continues to contact Advanced Identity Cloud for policy decisions as Barbara browses through the application.

3. Barbara confirms her intention to complete the withdrawal, triggering the application to access the `/withdraw` endpoint.

   When requesting a policy decision for this endpoint, the application gets advices indicating transactional authorization.

   It redirects Barbara to the journey required for this transaction according to the policy. The important step of the journey is the decision to authorize the withdrawal:

   ![Confirming a withdrawal](_images/transactional-bank-withdrawal.png)

4. Barbara receives the money and a receipt page after the application finishes processing the transaction with Advanced Identity Cloud.

The steps the application follows to perform transactional authorization are identical to those for session upgrade. For details, refer to [Session upgrade with MFA](../am-sessions/session-upgrade.html).

---

---
title: Dynamic OAuth 2.0 authorization
description: Grant OAuth 2.0 scopes dynamically based on policies rather than static client configuration
component: pingoneaic
page_id: pingoneaic:am-authorization:oauth2-authorization
canonical_url: https://docs.pingidentity.com/pingoneaic/am-authorization/oauth2-authorization.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Authorization", "OAuth 2.0", "Scope", "Policy"]
page_aliases: ["authorization-guide:oauth2-authorization.adoc"]
section_ids:
  example_use_case: Example use case
  how_it_works: How it works
  validate_oauth_2_0_scope_policies: Validate OAuth 2.0 scope policies
  prepare_a_demonstration: Prepare a demonstration
  oauth2-authz-oath2-provider: OAuth 2.0 provider
  oauth2-authz-scope-policy: OAuth 2.0 scope policy
  oauth2-authz-client: OAuth 2.0 client
  oauth2-authz-resource-owner: Resource owner
  test_the_demonstration: Test the demonstration
  non_interactive: Non-interactive
  interactive: Interactive
  implied_consent: Implied consent
---

# Dynamic OAuth 2.0 authorization

Advanced Identity Cloud can grant OAuth 2.0 scopes statically or dynamically:

* Static scopes (default)

  OAuth 2.0 client configurations specify the allowed and, optionally, default scopes.

  When the client requests allowed scopes and the resource owner consents to grant the client access, Advanced Identity Cloud issues the token with the scopes requested.

  When different users use the same client that requests scopes `A` and `B`, the access token always includes scopes `A` and `B`.

* Dynamic scopes

  OAuth 2.0 client configurations specify the allowed and, optionally, default scopes.

  1. You configure policies for OAuth 2.0 scope decisions.

  2. You configure the client or the OAuth 2.0 provider service to use the policy engine for scope decisions.

  Advanced Identity Cloud checks each scope against the applicable OAuth 2.0 scope policies and grants or denies access to scopes dynamically.

  When different users use the same client that requests scopes `A` and `B`, the access token scopes can differ.

## Example use case

A company supports custom OAuth 2.0 clients for internal applications. The use of the internal applications is bound by the terms and conditions in the contracts of those who work for the company. The terms and conditions grant the internal applications access to profile information the company maintains. It would be redundant to prompt employees and contractors for consent to access their profile information.

An Advanced Identity Cloud administrative user creates policies to grant the `profile` scope for all internal client tokens.

## How it works

![How policies determine whether to grant or deny an OAuth 2.0 scope](_images/oauth2-realm-app-policy-overview.png)Figure 1. Policies for dynamic scopes

Advanced Identity Cloud processes consent based on the policy decision:

* If a policy grants access to a scope (`GRANT=true`), consent is automatic.

  Advanced Identity Cloud does not prompt the user to grant access.

* If a policy denies access to a scope (`GRANT=false`), Advanced Identity Cloud omits the scope from any resulting token.

  Advanced Identity Cloud does not prompt the user to grant access.

* If no policy grants or denies access, then the result depends on the flow.

  When the flow is interactive as in authorization or device code flows, Advanced Identity Cloud prompts the user to grant access or uses the saved consent state if available.

  If the flow is not interactive as in resource owner password or client credentials flows, Advanced Identity Cloud omits the scope from any resulting token.

  For details about which flows are interactive, refer to the examples in [OAuth 2.0 grant flows](../am-oauth2/oauth2-implementing-flows.html) and [OIDC grant flows](../am-oidc1/oidc-implementing-flows.html).

The default scopes behavior doesn't change for dynamic authorization. Advanced Identity Cloud only evaluates default scopes from the OAuth 2.0 client profile when the client doesn't request a scope. Advanced Identity Cloud follows the same rules to deduce consent for both default and requested scopes.

When issuing refresh tokens, Advanced Identity Cloud issues the same scopes as for the access token, unless a policy explicitly denies one of the scopes.

## Validate OAuth 2.0 scope policies

Writing policies for OAuth 2.0 might not be straightforward if your environment requires complex conditions. The easiest way to validate OAuth 2.0 policies is to configure a client to use the policies and request some tokens.

## Prepare a demonstration

Start by preparing the demonstration:

1. [Configure the OAuth 2.0 provider](#oauth2-authz-oath2-provider).

2. [Create a sample policy](#oauth2-authz-scope-policy).

3. [Create an OAuth 2.0 client](#oauth2-authz-client).

4. [Create a resource owner account](#oauth2-authz-resource-owner).

### OAuth 2.0 provider

Configure the OAuth 2.0 provider service to use the policy engine for scope decisions:

1. Under Native Consoles > Access Management, go to Realms > alpha > Services > OAuth2 Provider.

2. Enable Use Policy Engine for Scope decisions.

### OAuth 2.0 scope policy

The sample scope policy denies access to the `email` scope.

1. Under Native Consoles > Access Management, go to Realms > alpha > Authorization > Policy Sets and select Default OAuth2 Scopes Policy Set to edit the policy set.

   This is the `oauth2Scopes` policy.

2. Click + Add a Policy, use the following settings, and create the policy:

   * Name

     `Dynamic OAuth 2.0 Scopes`

   * Resource Type

     `OAuth2 Scope`

   * Resources

     Select `*` as the pattern and add `email` as the scope.

3. Click the Actions tab, set `GRANT` to `Deny`, and save your changes.

4. Click the Subjects tab, set the subject type to `Authenticated Users`, and save your changes.

The resulting policy reflects your work:

![OAuth 2.0 policy denying the email scope for all authenticated users](_images/oauth2-scope-policy.png)Figure 2. OAuth 2.0 scopes policy

### OAuth 2.0 client

The OAuth 2.0 client profile in this example overrides the OAuth 2.0 provider settings. This lets you test the scope policy without affecting other clients.

1. Create a confidential OAuth 2.0 client account.

   In the Advanced Identity Cloud admin console, select Applications > + Add Application, and create a new Web application with the following settings:

   * Client ID: `myClient`

   * Client Secret: `mySecret`

2. Add the following settings in the client profile and save your work:

   * Name

     `Dynamic scopes client`

   * Sign-in URLs

     `https://www.example.com:443/callback`

   * Grant Types

     `Authorization Code`\
     `Client Credentials`\
     `Implicit`\
     `Refresh Token`\
     `Resource Owner Password Credentials`

   * Scopes

     `openid`\
     `profile`\
     `email`

3. Override the OAuth 2.0 provider settings for this client:

   Under Native Consoles > Access Management, select Realms > alpha > Applications > OAuth 2.0 > Clients > myClient. On the OAuth2 Provider Overrides tab, update the following settings and save your work:

   * Enable OAuth2 Provider Overrides: Enabled

   * Use Policy Engine for Scope decisions: Enabled

   * Scopes Policy Set: `oauth2Scopes`

### Resource owner

Create the OAuth 2.0 resource owner account:

1. In the Advanced Identity Cloud admin console, select Identities > + Add Identity and complete the required fields. For example:

   1. Username: `bjensen`

   2. Password: `Secret12!`

   3. Email address: `bjensen@example.com`

2. Record the username and password.

## Test the demonstration

Test the feature with non-interactive and interactive flows.

The sample policy denies the `email` scope for all authenticated users. The `profile` scope has no policy - it's a *no-policy-match* case. The tests show how Advanced Identity Cloud handles each case depending on the flow type.

### Non-interactive

This test uses the [resource owner password credentials](../am-oauth2/oauth2-ropc-grant.html) (ROPC) flow:

* The OAuth 2.0 client credentials are `myClient:mySecret`.

* The resource owner credentials are the username and password you recorded: `bjensen:Secret12!`.

* The requested scopes are `openid`, `profile`, and `email`.

```bash
$ curl \
--request POST \
--user 'myClient:mySecret' \
--data 'scope=openid profile email' \
--data 'grant_type=password' \
--data 'username=bjensen' \
--data 'password=Secret12!' \
"https://<tenant-env-fqdn>/am/oauth2/realms/root/realms/alpha/access_token"
{
  "access_token": "...",
  "refresh_token": "...",
  "scope": "openid",
  "id_token": "...",
  "token_type": "Bearer",
  "expires_in": 3599
}
```

Notice the access token has `"scope": "openid"`. Advanced Identity Cloud removed both `email` and `profile` from the scopes:

* `email`: a policy explicitly denies it (`GRANT=false`), so Advanced Identity Cloud omits it.

* `profile`: no policy matches this scope, so Advanced Identity Cloud also omits it.

In non-interactive flows, Advanced Identity Cloud treats no-policy-match scopes the same as explicitly denied scopes.

### Interactive

This test uses the [implicit](../am-oauth2/oauth2-implicit-grant.html) flow. It stops after demonstrating the user consent phase of the process.

1. In a web browser, go to the `/authorize` endpoint to initiate the implicit flow.

   ```none
   https://<tenant-env-fqdn>/am/oauth2/realms/root/realms/alpha/authorize?scope=openid+profile+email&response_type=id_token&client_id=myClient&nonce=123&state=456&redirect_uri=https://www.example.com:443/callback
   ```

2. Sign in with the resource owner's credentials.

3. Observe the prompt for consent that doesn't include the `email` scope:

   ![Advanced Identity Cloud prompts for consent to access the profile scope.](_images/oauth2-example-oidc.png)Figure 3. Consent for the profile scope

The consent page shows `profile` but not `email`:

* `email`: the policy explicitly denies it (`GRANT=false`), so Advanced Identity Cloud omits it from the consent page entirely.

* `profile`: no policy matches this scope, so Advanced Identity Cloud presents it for the user to grant or deny.

In interactive flows, Advanced Identity Cloud doesn't treat no-policy-match scopes the same as explicitly denied scopes. Instead, it presents them for user consent.

|   |                                                                                                                                                                                                                                                                                                                                                           |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | To explicitly deny a scope in interactive flows, you must create a policy that sets `GRANT` to `Deny` for that scope and the relevant condition. Without an explicit deny policy, a scope that fails a policy condition (for example, a user who doesn't meet a group membership requirement) is still presented for consent rather than denied outright. |

### Implied consent

If you enable Implied consent on the client application, Advanced Identity Cloud auto-grants no-policy-match scopes, in both interactive and non-interactive flows.

---

---
title: Policies
description: Define policies to grant or deny access based on resources, actions, subjects, and environment conditions
component: pingoneaic
page_id: pingoneaic:am-authorization:configuring-policies
canonical_url: https://docs.pingidentity.com/pingoneaic/am-authorization/configuring-policies.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Authorization", "Policy"]
page_aliases: ["authorization-guide:configuring-policies.adoc"]
---

# Policies

Authorization *policies* let Advanced Identity Cloud determine whether to grant a subject access to a resource.

A policy defines the following:

* *resources*

  The resource to which access is restricted, such as a web page, a mobile app, or a boarding area in an airport.

* *actions*

  The verbs that describe what users can do to the resource, such as *read* a web page, *submit* a web form, or *access* a boarding area.

* *subject conditions*

  Who the policy applies to, such as all authenticated users, only administrators, or only passengers with valid tickets for planes leaving soon.

* *environment conditions*

  The circumstances under which the policy applies, such as only during work hours, only when accessing from a specific IP address, or only when the flight is scheduled to leave within the next four hours.

* *response attributes*

  Information that Advanced Identity Cloud attaches to a response following a policy decision, such as a name, email address, or frequent flyer status.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Policy conditions don't determine the outcome of the policy but determine whether a specific policy is applicable and whether its actions should contribute towards the overall policy decision. If a condition fails (due to authentication failure, for example), Advanced Identity Cloud disregards the corresponding policy and assesses any other configured policies to make the authorization decision. |

---

---
title: Policies in the UI
description: Create and manage authorization policies through the native console with conditions and response attributes
component: pingoneaic
page_id: pingoneaic:am-authorization:policies-ui
canonical_url: https://docs.pingidentity.com/pingoneaic/am-authorization/policies-ui.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Authorization", "Policy", "Configuration"]
page_aliases: ["authorization-guide:policies-ui.adoc"]
section_ids:
  policy-names: Policy type names
  resources: Resources
  policy-actions: Policy actions
  conditions: Conditions
  subjects: Subjects
  environments: Environments
  response-attributes: Response attributes
  example: Example
---

# Policies in the UI

You manage authorization policies through the AM native admin console native console. You can only create a policy as part of a [policy set](policy-sets-ui.html).

To configure a policy, go to Native Consoles > Access Management > Realms > *Realm Name* > Authorization > Policy Sets and select the name of the policy set in which to configure the policy.

| To...           | Action                                                                                                                                                                                |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Create a policy | Click Add a Policy.When creating a policy, specify a [name](#policy-names), a [resource type](configuring-resource-types.html), and at least one [resource](#resources).Click Create. |
| Modify a policy | Click the policy name or the pencil icon ([icon: pencil-alt, set=fa]).                                                                                                                |
| Delete a policy | Click the delete icon ([icon: times, set=fa]) or click the policy name then x Delete.                                                                                                 |

## Policy type names

Don't use any of the following characters in policy, policy set, or resource type names:

* Double quotes (`"`)

* Plus sign (`+`)

* Comma (`,`)

* Less than (`<`)

* Equals (`=`)

* Greater than (`>`)

* Backslash (`\`)

* Forward slash (`/`)

* Semicolon (`;`)

* Null (`\u0000`)

## Resources

To define resources that the policy applies to:

1. Click the Resources pencil icon ([icon: pencil-alt, set=fa]) or the Resources tab.

2. Select a resource type from the Resource Type list.

   The resource type determines which resource patterns are available. The `OAuth2 Scope` resource type contains the same resource patterns as the `URL` resource type, as well as the `*` pattern.

   Use the resource patterns that are most relevant for the scopes in your environment.

   Learn more about resource types in [Resource types](configuring-resource-types.html).

3. Select a resource pattern from the Resources drop-down list.

4. Replace the asterisks with values for matching resources, and click Add.

   Learn more about resource patterns in [Resource type patterns](resource-types-ui.html#policy-patterns-wildcards).

5. Optionally, click Add Resource to add more resource patterns, or click ([icon: times, set=fa]) to delete a resource pattern.

6. Save your changes.

## Policy actions

To define policy actions that allow or deny access to a resource:

1. Click the Actions pencil icon ([icon: pencil-alt, set=fa]) or the Actions tab.

2. Click Add an Action to select an action from the drop-down list.

3. Select whether to allow or deny the action on the resources.

4. Optionally, add further actions, or click ([icon: times, set=fa]) to delete actions.

5. Save your changes.

## Conditions

To define subject and environment conditions:

* Combine logical operators with blocks of configured parameters to create a rule set. The policy uses this rule set to filter requests for resources.

* Use drag and drop to nest logical operators at multiple levels to create complex rule sets.

  ![Nested subject conditions](_images/policy-subjects.png)

* A gray horizontal bar indicates a valid point to drop a block.

  ![Drop blocks into drop points, which are shown as a gray horizontal band.](_images/policy-editor-valid-drop-points.png)

### Subjects

To define the subject conditions that the policy applies to:

1. Click Add a Subject Condition, choose the [type](#subject-types) from the drop-down menu, and provide any required subject values.

2. When complete, click the check icon ([icon: check, set=fa]) and drag the block into a valid drop point in the rule set.

3. To add a logical operator, click Add a Logical Operator, choose between `All Of`, `Not`, and `Any Of` from the drop-down list, and drag the block into a valid drop point in the rule set.

4. To edit a condition, click the edit icon ([icon: pencil-alt, set=fa]), or click ([icon: times, set=fa]) to delete.

5. Continue combining logical operators and subject conditions and click Save Changes when you've finished.

| Subject condition types  | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Authenticated Users      | Any user that has successfully authenticated with Advanced Identity Cloud.                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Users & Groups           | Search for and select one or more users or groups under the Realms > *Realm Name* > Identities or the Groups tab.                                                                                                                                                                                                                                                                                                                                                                                                              |
| OpenID Connect/Jwt Claim | Validate a claim within a JSON Web Token (JWT).Type the name of the claim to validate in the Claim Name field, for example, `sub`, and the required value in the Claim Value field, and click the check icon ([icon: check, set=fa]).Repeat the step to enter additional claims.The claim(s) will be part of the JWT payload together with the JWT header and signature. The JWT is sent in the authorization header of the bearer token.This condition type only supports string equality comparisons, and is case-sensitive. |
| Never Match              | Never match any subject. This disables the policy.If you do not set a subject condition, `Never Match` is the default. In other words, you must set a subject condition for the policy to apply.To match regardless of the subject, configure a `Never Match` subject condition inside a logical `Not` block.                                                                                                                                                                                                                  |

### Environments

To define the environment conditions the policy applies to:

1. Click Add an Environment Condition, select an environment condition type from the Type list, and provide any required values.

   The fields differ, according to the type you've selected. Learn more in [Environment condition types](#environment-types).

   |   |                                                                              |
   | - | ---------------------------------------------------------------------------- |
   |   | `Script` is the only environment condition available for OAuth 2.0 policies. |

2. When complete, click the check icon ([icon: check, set=fa]) button and drag the block into a valid drop point in the rule set.

3. To add a logical operator, click Add a Logical Operator, choose between `All Of`, `Not`, and `Any Of` from the drop-down list, and drag the block into a valid drop point in the rule set.

4. To edit a condition, click the edit icon ([icon: pencil-alt, set=fa]), or click ([icon: times, set=fa]) to delete.

5. Continue combining logical operators and subject conditions and click Save Changes when you've finished.

**Environment condition types**

| Environment condition type                      | Description                                                                                                                                                                                                                                                             | Additional fields                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| ----------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Active Session Time                             | Set a condition for the maximum duration the authenticated session has been active.                                                                                                                                                                                     | * `Max Session Time`: Set the period the session can be active, in seconds.

* `Terminate Session`: Set to `True` if the session must end when it reaches the `Max Session Time`. If set to `True`, the end user will need to reauthenticate.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Authentication Level (greater than or equal to) | The policy tests the required authentication level.                                                                                                                                                                                                                     | - `Authentication level`: Set the minimum acceptable authentication level.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Authentication Level (less than or equal to)    | The policy tests the required authentication level.                                                                                                                                                                                                                     | * `Authentication level`: Set the maximum acceptable authentication level.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Authentication by Module Instance               | This property doesn't apply to Advanced Identity Cloud.                                                                                                                                                                                                                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Authentication by Service                       | The policy tests the authentication journey used.                                                                                                                                                                                                                       | `Authenticate To Service`: Set the journey through which the end user must authenticate.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Authentication to a Realm                       | The policy evaluates the realm to which the end user authenticated. A session can belong to only one realm. Session upgrade between realms is not allowed.                                                                                                              | `Authenticate to a realm`: Set the realm to which the end user must authenticate.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Current Session Properties                      | The policy evaluates property values set in the authenticated session.                                                                                                                                                                                                  | - `Ignore Value Case`: Set to `True` to make the test case-insensitive.

- `Properties`: Set the properties you want to evaluate using the format `property:value`. For example, use `clientType:genericHTML` to test whether the value of the `clientType` property is equal to `genericHTML`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| IDM User                                        | Lets you query an IDM resource to form the basis of the policy evaluation.                                                                                                                                                                                              | * `Identity Resource`: The identity resource to query, for example, `managed/alpha_user`.

* `Query Field`: The unique IDM attribute that identifies the user, for example, `userName`.

* `Decision Field`: The IDM attribute whose value is evaluated, for example, `roles/*/name` or `/manager/userName`.

* `Comparator`: Select the comparator to create the query, for example, `Equal to`.

* `Value`: Enter the value of the `Decision Field` property that must match for the policy to evaluate to true, for example `administrator`.                                                                                                                                                                                                                                                                                                                                                                                                             |
| IPv4 Address/DNS Name                           | The policy evaluates the IP version 4 address from which the request originated.The IP address is taken from the `requestIp` value of policy decision requests. If the `requestIp` isn't provided, Advanced Identity Cloud uses the IP address stored in the SSO token. | - `Start IP`, `End IP`: Specify a range of addresses to test against. In each field, enter four sets of up to three digits, separated by periods (.)..

  If you set only one of the `Start IP` or `End IP` fields, it's used as a single IP address to match.

- `DNS Name`: Optionally, specify a domain against which requests are filtered.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| IPv6 Address/DNS Name                           | The policy evaluates the IP version 6 address from which the request originated.The IP address is taken from the `requestIp` value of policy decision requests. If the `requestIp` isn't provided, Advanced Identity Cloud uses the IP address stored in the SSO token. | * `Start IP` and `End IP`: Specify a range of addresses to test against. In each field, enter eight sets of four hexadecimal characters, separated by a colon (`:`).

  If you set only one of the Start IP or End IP fields, it's used as a single IP address to match.

* `DNS Name`: Optionally, specify a domain against which requests are filtered.

  Use an asterisk (`*`) in the DNS name to match multiple subdomains. For example, `*.example.com` applies to requests from `www.example.com`, `secure.example.com`, or any other subdomain of `example.com`.                                                                                                                                                                                                                                                                                                                                                                                    |
| Identity Membership                             | The policy evaluates the user's UUID.                                                                                                                                                                                                                                   | `AM Identity Name`: The policy applies if the end user's UUID is a member of at least one of the AMIdentity objects specified here.For example, use this type to filter requests on the identity of a Web Service Client (WSC).	Java agents and web agents don't support the Identity Membership environment condition. Use the Users & Groups subject condition instead.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| OAuth2 Scope                                    | The policy evaluates whether an authorization request includes all the specified OAuth 2.0 scopes.                                                                                                                                                                      | `Scopes`: Enter the OAuth 2.0 scopes using the syntax described in RFC 6749, [Access Token Scope](https://www.rfc-editor.org/rfc/rfc6749.html#section-3.3).Separate multiple scope strings with spaces, for example, `openid profile`.Scope strings match regardless of the order in which they occur, so `openid profile` is equivalent to `profile openid`.The condition is also met when additional scope strings are provided beyond those required to match the specified list. For example, if the condition specifies `openid profile`, then `openid profile email` also matches.                                                                                                                                                                                                                                                                                                                                                                    |
| Resource/Environment/IP Address                 | The policy evaluates a complex condition, such as whether the end user is making a request from a specific host, and has also authenticated in a particular way.                                                                                                        | `Resource/Environment/IP Address`: Enter a condition in the form of an `IF…​ELSE` statement.The `IF` statement can specify either `IP` to match the end user's IP address, or `dnsName` to match their DNS name.If the `IF` statement is true, the `THEN` statement must also be true for the condition to be fulfilled. If not, {} returns relevant advice in the policy evaluation request.The available parameters for the `THEN` statement are as follows:* `service`: The authentication journey used to authenticate the end user

* `authlevel`: The minimum required authentication level

* `role`: The role of the authenticated end user

* `user`: The name of the authenticated end user

* `redirectURL`: The URL the end user was redirected from.

* `realm`: The realm to which the end user authenticated.The IP address can be IPv4, IPv6, or a hybrid of the two. Example: `IF IP=[127.0.0.1] THEN role=admins`.                        |
| Script                                          | The policy evaluates the outcome of a JavaScript.                                                                                                                                                                                                                       | `Script Name`: Select the script the policy evaluates. Learn more about scripting policy conditions in [Scripted policy conditions](scripted-policy-condition.html).`Script` is the only environmental condition available for OAuth 2.0 policies. Use scripts to capture the `ClientId` environmental attribute.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Time (day, date, time, and timezone)            | The policy evaluates a time condition.                                                                                                                                                                                                                                  | - `Start Time`

- `End Time`

- `Start Day`

- `End Day`

- `Start Date`

- `End Date`Set values in start:end pairs.* `Time Zone`: Select a time zone from the list.> **Collapse: Example**
>
> ![Day, date and time conditions in policies must consist of a start and an end value.](_images/policy-environment-time.png)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Transaction                                     | The policy evaluates successful completion of a [transactional authorization](transactional-authorization.html).Transactional authorization requires the end user to authenticate for each access to the resource.                                                      | * `Authentication Strategy`: Select from the following:

  * `Authenticate to Realm`: The full path of a realm in which the end user must successfully authenticate to access the protected resource. For example, `/alpha`.

  * `Authenticate to Tree`: The authentication journey the end user must successfully traverse to access the protected resource.

  * `Auth Level`: The minimum [authentication level](../am-authentication/auth-nodes-and-journeys.html#authentication-levels-trees) the end user must achieve to access the protected resource.

  `Authenticate to Chain` and `Authenticate to Module` are *not applicable to Advanced Identity Cloud*.

* `Strategy Specifier`: Enter the realm, tree or level.

  If you specify an Auth Level, you must ensure there are methods available to end users to reach that level. If none are found, the policy returns a 400 Bad request error when attempting to complete the transaction. |

|   |                                                                       |
| - | --------------------------------------------------------------------- |
|   | The LDAP Filter Condition isn't supported in Advanced Identity Cloud. |

## Response attributes

Add user attributes from the identity repository as response attributes—​either as subject attribute or static attributes—​to the request header at policy decision time.

Note that response attributes are not available for the `OAuth2 Scope` resource type.

The web or Java agent for the protected resources/applications, or the protected resources/applications themselves, retrieve the policy response attributes to customize the application.

To define response attributes in the policy:

1. Click the Response Attributes edit icon ([icon: pencil-alt, set=fa]) or the Response Attributes tab.

2. To add subject attributes, select them from the Subject attributes drop-down list.

   To remove an entry, select the value, and click Delete (Windows/GNU/Linux) or `Backspace` (Mac OS X).

3. To add a static attribute, specify the key-value pair for each static attribute. Enter the Property Name and its corresponding Property Value in the fields, and click Add (`+`).

   To edit a static attribute, click the edit icon ([icon: pencil-alt, set=fa]), or click ([icon: times, set=fa]) to delete.

4. Continue adding subject and static attributes, and when finished, click Save Changes.

## Example

This example policy requires authenticated end users to have a session no longer than 30 minutes to access resources at `https://www.example.com:*/*`.

![Example policy](_images/policy-example.png)

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | Before testing your OAuth 2.0 policies, ensure your OAuth 2.0 provider is configured to interact with Advanced Identity Cloud's authorization service:1) Under Native Consoles > Access Management, go to Realms > *Realm Name* > Services > OAuth2 Provider.

2) Ensure that Use Policy Engine for Scope decisions is enabled.For more information about testing OAuth 2.0 policies, refer to [Dynamic OAuth 2.0 authorization](oauth2-authorization.html). |

---

---
title: Policies over REST
description: Manage authorization policies over REST including resources, actions, subjects, and conditions
component: pingoneaic
page_id: pingoneaic:am-authorization:rest-api-authz-policies
canonical_url: https://docs.pingidentity.com/pingoneaic/am-authorization/rest-api-authz-policies.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Authorization", "Policy", "REST API", "Configuration"]
page_aliases: ["authorization-guide:rest-api-authz-policies.adoc"]
section_ids:
  policy_resource_objects: Policy resource objects
  environment-conditions: Environment conditions
  subject-conditions: Subject conditions
  access_the_endpoints: Access the endpoints
  rest-api-authz-policies-query: Query policies
  rest-api-authz-policies-read: Read a policy
  rest-api-authz-policies-create: Create a policy
  rest-api-authz-policies-update: Update a policy
  rest-api-authz-policies-delete: Delete a policy
  rest-api-authz-policies-copy-move-policies: Copy and move policies
  rest-api-authz-condition-types: Environment conditions
  rest-api-authz-subject-types: Subject conditions
  rest-api-authz-decision-combiners: Decision combiners
---

# Policies over REST

You can manage authorization policies over REST at the `policies` endpoint.

Policies belong to a [policy set](configuring-policy-sets.html).

## Policy resource objects

The policy resources are JSON objects. A policy object can include the following fields. The fields have JSON values—​strings, numbers, objects, sets, arrays, `true`, `false`, and `null`.

| Policy field          | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| --------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `_id`, `name`(1)      | A string identifying the policy.This string matches the policy name part of the URL path to the resource.Don't use any of the following characters in policy, policy set, or resource type names:- Double quotes (`"`)

- Plus sign (`+`)

- Comma (`,`)

- Less than (`<`)

- Equals (`=`)

- Greater than (`>`)

- Backslash (`\`)

- Forward slash (`/`)

- Semicolon (`;`)

- Null (`\u0000`)                                                                                                                                                                                                                    |
| `_rev`(1)             | A system-generated revision string.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `actionValues`        | An object where each field is an action name.The [resource type](configuring-resource-types.html) of the [policy set](configuring-policy-sets.html) governs the available actions.The value for each action name field is a boolean indicating whether to allow the action by default. (Advanced Identity Cloud also accepts `0` for `false` and any non-zero numeric value for `true`.)                                                                                                                                                                                                                             |
| `active`              | A boolean indicating whether Advanced Identity Cloud considers the policy active for evaluation purposes.Default: `false`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `applicationName`     | A string identifying the policy set that contains the policy.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| `condition`           | An optional object specifying the [environment conditions](#environment-conditions) where the policy applies.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| `description`         | A string describing the policy.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| `resourceAttributes`  | An optional array of response attribute objects; does not apply to `OAuth2 Scope` resource types.The default implementation returns statically defined attributes and attributes from user profiles. A response attribute object has these fields:- `type`

  The implementation type:

  * `Static` for statically defined attributes

  * `User` for attributes from the user profile

- `propertyName`

  The attribute name.

- `propertyValues`

  * For static attributes, the attribute values.

  * For user attributes, not used; Advanced Identity Cloud determines the values when evaluating the policy. |
| `resources`           | An array of the resource name pattern strings to which the policy applies.The [resource type](configuring-resource-types.html) must allow the patterns.                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `resourceTypeUuid`    | An optional string identifying the resource type that governs the policy.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `subject`             | An optional object specifying the [subject conditions](#subject-conditions) where the policy applies.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `createdBy`(1)        | A string indicating who created the policy.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `creationDate`(1)     | An integer containing the creation time in milliseconds since January 1, 1970.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `lastModifiedBy`(1)   | A string indicating who last changed the policy.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `lastModifiedDate`(1) | An integer containing the last modified time in milliseconds since January 1, 1970.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |

(1) Do not change the value of this field.

### Environment conditions

Environment conditions clarify where the policy applies.

Express environment conditions as single conditions or combine them using boolean operators. The following example demonstrates a single environment condition that requires an `access` OAuth 2.0 scope:

```json
{
  "condition": {
    "type": "OAuth2Scope",
    "requiredScopes": ["access"]
  }
}
```

The following example demonstrates a combined environment condition that excludes Saturday, Sunday, and a range of IP addresses:

```json
{
  "type": "NOT",
  "condition": {
    "type": "OR",
    "conditions": [{
      "type": "SimpleTime",
      "startTime": "",
      "endTime": "",
      "startDay": "sat",
      "endDay": "sun",
      "enforcementTimeZone": "US/Mountain"
    }, {
      "type": "IPv4",
      "startIp": "192.168.0.1",
      "endIp": "192.168.0.255",
      "ipRange": [],
      "dnsName": []
    }]
  }
}
```

The boolean operator strings to combine conditions in JSON correspond to these properties in the UI:

* `AND` is All of.

* `OR` is Any of.

* `NOT` is Not.

Use the following environment conditions in your policies:

* `AMIdentityMembership`

  Applies to this array of users and groups.

  ```json
  {
    "type": "AMIdentityMembership",
    "amIdentityName": ["id=1dff18dc-ac57-4388-8127-dff309f80002,ou=user,o=alpha,ou=services,ou=am-config"]
  }
  ```

  The ForgeRock Java and web agents do not support the `AMIdentityMembership` environment condition. Use the `Identity` subject condition instead.

* `AuthLevel`

  Requires at least the specified authentication level.

  ```json
  {
    "type": "AuthLevel",
    "authLevel": 2
  }
  ```

* `AuthenticateToRealm`

  Requires authentication to the specified realm.

  ```json
  {
    "type": "AuthenticateToRealm",
    "authenticateToRealm": "alpha"
  }
  ```

* `AuthenticateToService`

  Requires authentication with the specified journey (tree).

  ```json
  {
      "type": "AuthenticateToService",
      "authenticateToService": "PushAuthentication"
  }
  ```

* `IdmUser`

  Lets you query an IDM resource to form the basis of the policy evaluation.

  ```json
  {
      "type": "IdmUser",
      "identityResource": "managed/alpha_user",
      "queryField": "userName",
      "decisionField": "effectiveRoles",
      "comparator": "CONTAINS",
      "value": "manager"
  }
  ```

  For multivalued attributes, use a wildcard search to find all possible values. For example:

  ```json
  {
    "type": "IdmUser",
    "identityResource": "managed/alpha_user",
    "queryField": "frIndexedString1",
    "decisionField": "frIndexedMultivalued2/*",
    "comparator": "REGEX",
    "value": ".*test-string.*"
  }
  ```

* `IPv4` or `IPv6`

  Requires a request from the specified IP address range or domain name.

  ```json
  {
    "type": "IPv4",
    "startIp": "127.0.0.1",
    "endIp": "127.0.0.255"
  }
  ```

  Omit `startIp` and `endIp` and use the `dnsName` field to specify an array of domain name strings:

  ```json
  {
    "type": "IPv4",
    "dnsName": ["*.example.com"]
  }
  ```

* `LDAPFilter`

  Requires the LDAP representation of the user's profile matches the specified LDAP search filter.

  ```json
  {
    "type": "LDAPFilter",
    "ldapFilter": "(&(c=US)(preferredLanguage=en-us))"
  }
  ```

* `LEAuthLevel`

  Requires at most the specified authentication level.

  ```json
  {
    "type": "LEAuthLevel",
    "authLevel": 2
  }
  ```

* `OAuth2Scope`

  Requires the specified OAuth 2.0 scopes.

  ```json
  {
    "type": "OAuth2Scope",
    "requiredScopes": ["access"]
  }
  ```

* `ResourceEnvIP`

  Requires a complex condition.

  The following example requires an authentication level of at least 4 for requests from an IP address in `127.168.10.*`:

  ```json
  {
    "type": "ResourceEnvIP",
    "resourceEnvIPConditionValue": ["IF IP=[127.168.10.*] THEN authlevel=4"]
  }
  ```

  Each `resourceEnvIPConditionValue` has one or more `IF...THEN...[ELSE...THEN]` statements.

  When the `IF` statement is true, a true `THEN` statement fulfills the condition.

  The `IF` statement specifies either:

  * An IPv4, IPv6, or hybrid address to match the IP address. The IP address can include wildcards.

  * A `dnsName` to match DNS name. The IP address can be IPv4 or IPv6 format, or a hybrid of the two, and can include wildcard characters.

  | `THEN` parameter | Description                               |
  | ---------------- | ----------------------------------------- |
  | `authlevel`      | The minimum required authentication level |
  | `realm`          | The realm where authentication completed  |
  | `redirectURL`    | The URL the user was redirected from      |
  | `role`           | The role of the authenticated user        |
  | `service`        | The authentication journey                |
  | `user`           | The name of the authenticated user        |

* `Script`

  Lets you customize the policy decision with a script. Reference the script using the script ID.

  ```json
  {
    "type": "Script",
    "scriptId": "9de3eb62-f131-4fac-a294-7bd170fd4acb"
  }
  ```

  You can find more information about using a script to evaluate policies in [Scripted policy conditions](scripted-policy-condition.html).

* `Session`

  Sets the maximum age of the authenticated session, and whether to terminate old sessions, forcing reauthentication.

  ```json
  {
    "type": "Session",
    "maxSessionTime": "10",
    "terminateSession": false
  }
  ```

* `SessionProperty`

  Require attributes set in the authenticated session.

  ```json
  {
    "type": "SessionProperty",
    "ignoreValueCase": true,
    "properties": {
      "CharSet": ["UTF-8"],
      "clientType": ["genericHTML"]
    }
  }
  ```

* `SimpleTime`

  Set a time range. The `type` is the only required field.

  ```json
  {
    "type": "SimpleTime",
    "startTime": "07:00",
    "endTime": "19:00",
    "startDay": "mon",
    "endDay": "fri",
    "startDate": "2023:01:01",
    "endDate": "2023:12:31",
    "enforcementTimeZone": "GMT+0:00"
  }
  ```

### Subject conditions

Subject conditions specify who the policy targets.

Express subject conditions as single conditions or combine them using boolean operators. The following example of a single subject condition means the policy applies to all authenticated users:

```json
{
  "subject": {
    "type": "AuthenticatedUsers"
  }
}
```

The following example of a combined subject condition means the policy applies to either of two users:

```json
{
  "type": "OR",
  "subjects": [{
    "type": "Identity",
    "subjectValues": ["id=014c54bd-6078-4639-8316-8ce0e7746fa4,ou=user,o=alpha,ou=services,ou=am-config"]
  }, {
    "type": "Identity",
    "subjectValues": ["id=1dff18dc-ac57-4388-8127-dff309f80002,ou=user,o=alpha,ou=services,ou=am-config"]
  }]
}
```

The boolean operator strings to combine conditions in JSON correspond to these properties in the UI:

* `AND` is All of.

* `OR` is Any of.

* `NOT` is Not.

The `type` field specifies the subject:

* `AuthenticatedUsers`

  Applies to any user that successfully authenticated to Advanced Identity Cloud regardless of the realm.

  To limit this to a specific realm, add an `AuthenticateToRealm` environment condition to the policy.

* `Identity`

  Applies to the specified users or groups.

  The following example means the policy applies to members of the account administrators group:

  ```json
  {
    "type": "Identity",
    "subjectValues": ["id=account-administrators,ou=group,o=alpha,ou=services,ou=am-config"]
  }
  ```

* `JwtClaim`

  Applies based on a claim in a user's JSON web token (JWT).

  ```json
  {
    "type": "JwtClaim",
    "claimName": "sub",
    "claimValue": "1dff18dc-ac57-4388-8127-dff309f80002"
  }
  ```

* `NONE`

  Never applies; Advanced Identity Cloud never evaluates the policy as part of a decision.

## Access the endpoints

The REST calls to manage policies rely on an account with the appropriate privileges:

1. Create a policy administrator.

   In the Advanced Identity Cloud admin console, select Identities > Manage > *Realm Name* Realm - Users > + New *Realm Name* Realm - User and fill the required fields.

   Record the username and password.

2. Create a group that grants the privileges to the policy administrator.

   Under Native Consoles > Access Management, select Realms > *Realm Name* > Identities > Groups > + Add Group to create a group with the following settings:

   * Group ID

     `am-policy-admins`

   * Members

     The policy administrator whose username you recorded

   * Privileges

     Policy Admin\
     Condition Types Read Access\
     Decision Combiners Read Access\
     Entitlement Rest Access\
     Subject Types Read Access

3. Before making REST calls to manage policies, authenticate as the policy administrator:

   ```bash
   $ curl \
   --request POST \
   --header 'Content-Type: application/json' \
   --header 'X-OpenAM-Username: <policy-admin-username>' \
   --header 'X-OpenAM-Password: <policy-admin-password>' \
   --header 'Accept-API-Version: resource=2.0, protocol=1.0' \
   'https://<tenant-env-fqdn>/am/json/realms/root/realms/alpha/authenticate'
   {
     "tokenId": "<policy-admin-tokenId>",
     "successUrl": "/enduser/?realm=/alpha",
     "realm": "/alpha"
   }
   ```

   For additional details, refer to [Session tokens after authentication](../am-authentication/rest-using-ssotokens.html).

   Use the `<policy-admin-tokenId>` as the value of the `<session-cookie-name>` header to access the REST endpoints.

## Query policies

To list all the policy sets defined for a realm, send an HTTP GET request to the `/json/realms/root/realms/Realm Name/policies` endpoint with `_queryFilter=true` as the query string parameter.

```bash
$ curl \
--header "<session-cookie-name>: <policy-admin-tokenId>" \
--header "Accept-API-Version: resource=1.0, protocol=2.1" \
'https://<tenant-env-fqdn>/am/json/realms/root/realms/alpha/policies?_queryFilter=true
{
  "result": [{
    "_id": "myExamplePolicy",
    "_rev": "1669650078159",
    "name": "myExamplePolicy",
    "active": true,
    "description": "",
    "resources": ["*://*:*/*", "*://*:*/*?*"],
    "applicationName": "myPolicySet",
    "actionValues": {
      "GET": true,
      "PUT": true
    },
    "subject": {
      "type": "Identity",
      "subjectValues": ["id=1dff18dc-ac57-4388-8127-dff309f80002,ou=user,o=alpha,ou=services,ou=am-config"]
    },
    "lastModifiedBy": "id=a980a458-2654-4d4f-a12a-d4bfa39534f7,ou=user,ou=am-config",
    "lastModifiedDate": "2022-11-28T15:41:18.159Z",
    "createdBy": "id=a980a458-2654-4d4f-a12a-d4bfa39534f7,ou=user,ou=am-config",
    "creationDate": "2022-11-28T15:39:04.82Z"
  }],
  "resultCount": 1,
  "pagedResultsCookie": null,
  "totalPagedResultsPolicy": "NONE",
  "totalPagedResults": -1,
  "remainingPagedResults": 0
}
```

Adapt the [query string parameters](../developer-docs/crest/query.html) to refine the results.

| Field              | Supported `_queryFilter` operators                                                                                 |
| ------------------ | ------------------------------------------------------------------------------------------------------------------ |
| `name`             | Equals (`eq`)                                                                                                      |
| `applicationName`  |                                                                                                                    |
| `description`      |                                                                                                                    |
| `createdBy`        |                                                                                                                    |
| `lastModifiedBy`   |                                                                                                                    |
| `creationDate`     | Equals (`eq`)(1) Greater than or equal to (`ge`) Greater than (`gt`) Less than or equal to (`le`) Less than (`lt`) |
| `lastModifiedDate` |                                                                                                                    |

(1) Do not use regular expression patterns with `eq`.

To list policies that explicitly reference a user or group as part of a subject condition, send an HTTP GET request to the `/json/realms/root/realms/Realm Name/policies` endpoint with the query string parameters `_queryId=queryByIdentityUid` and `uid=universal-uid`, where *universal-uid* is the universal ID for the user or group.

```bash
$ curl \
--header "<session-cookie-name>: <policy-admin-tokenId>" \
--header "Accept-API-Version: resource=1.0" \
--header "Content-Type: application/json" \
'https://<tenant-env-fqdn>/am/json/realms/root/realms/alpha/policies?_queryId=queryByIdentityUid&uid=id=1dff18dc-ac57-4388-8127-dff309f80002,ou=user,o=alpha,ou=services,ou=am-config'
{
  "result": [{
    "_id": "myExamplePolicy",
    "_rev": "1669650078159",
    "name": "myExamplePolicy",
    "active": true,
    "description": "",
    "resources": ["*://*:*/*", "*://*:*/*?*"],
    "applicationName": "myPolicySet",
    "actionValues": {
      "GET": true,
      "PUT": true
    },
    "subject": {
      "type": "Identity",
      "subjectValues": ["id=1dff18dc-ac57-4388-8127-dff309f80002,ou=user,o=alpha,ou=services,ou=am-config"]
    },
    "lastModifiedBy": "id=a980a458-2654-4d4f-a12a-d4bfa39534f7,ou=user,ou=am-config",
    "lastModifiedDate": "2022-11-28T15:41:18.159Z",
    "createdBy": "id=a980a458-2654-4d4f-a12a-d4bfa39534f7,ou=user,ou=am-config",
    "creationDate": "2022-11-28T15:39:04.82Z"
  }],
  "resultCount": 1,
  "pagedResultsCookie": null,
  "totalPagedResultsPolicy": "NONE",
  "totalPagedResults": -1,
  "remainingPagedResults": 0
}
```

The following caveats apply when querying policies by user or group:

* Advanced Identity Cloud does not evaluate group membership.

  When you specify only groups in the condition, Advanced Identity Cloud does not also return policies for users who are members of the specified groups.

* Advanced Identity Cloud supports only exact matches for users and groups; you cannot use wildcards.

* Advanced Identity Cloud only returns policies with `Identity` subject conditions—​not `AMIdentityMembership` environment conditions.

* Advanced Identity Cloud does not return policies with subject conditions that only contain the user or group in a logical *NOT* operator.

## Read a policy

To read an individual policy in a realm, send an HTTP GET request to the `/json/realms/root/realms/Realm Name/policies/policy-name` endpoint.

```bash
$ curl \
--header "<session-cookie-name>: <policy-admin-tokenId>" \
--header "Accept-API-Version: resource=1.0" \
'https://<tenant-env-fqdn>/am/json/realms/root/realms/alpha/policies/myExamplePolicy'
{
  "_id": "myExamplePolicy",
  "_rev": "1669650078159",
  "name": "myExamplePolicy",
  "active": true,
  "description": "",
  "resources": ["*://*:*/*", "*://*:*/*?*"],
  "applicationName": "myPolicySet",
  "actionValues": {
    "GET": true,
    "PUT": true
  },
  "subject": {
    "type": "Identity",
    "subjectValues": ["id=1dff18dc-ac57-4388-8127-dff309f80002,ou=user,o=alpha,ou=services,ou=am-config"]
  },
  "lastModifiedBy": "id=a980a458-2654-4d4f-a12a-d4bfa39534f7,ou=user,ou=am-config",
  "lastModifiedDate": "2022-11-28T15:41:18.159Z",
  "createdBy": "id=a980a458-2654-4d4f-a12a-d4bfa39534f7,ou=user,ou=am-config",
  "creationDate": "2022-11-28T15:39:04.82Z"
}
```

## Create a policy

To create a policy in a realm, send an HTTP POST request to the `/json/realms/root/realms/Realm Name/policies` endpoint with `_action=create` as the query string parameter and a JSON representation of the policy as the POST data.

```bash
$ curl \
--request POST \
--header "<session-cookie-name>: <policy-admin-tokenId>" \
--header "Accept-API-Version: resource=1.0" \
--header "Content-Type: application/json" \
--data '{
  "name": "myNewExamplePolicy",
  "active": true,
  "description": "Example policy",
  "applicationName": "myPolicySet",
  "actionValues": {
    "POST": false,
    "GET": true
  },
  "resources": ["https://www.example.com:443/*", "https://www.example.com:443/*?*"],
  "subject": {
    "type": "Identity",
    "subjectValues": ["id=1dff18dc-ac57-4388-8127-dff309f80002,ou=user,o=alpha,ou=services,ou=am-config"]
  },
  "resourceTypeUuid": "76656a38-5f8e-401b-83aa-4ccb74ce88d2"
}' \
'https://<tenant-env-fqdn>/am/json/realms/root/realms/alpha/policies/?_action=create'
{
  "_id": "myExamplePolicy",
  "_rev": "1669650078159",
  "name": "myExamplePolicy",
  "active": true,
  "description": "",
  "resources": ["https://www.example.com:443/*", "https://www.example.com:443/*?*"],
  "applicationName": "myPolicySet",
  "actionValues": {
    "GET": true,
    "POST": false
  },
  "subject": {
    "type": "Identity",
    "subjectValues": ["id=1dff18dc-ac57-4388-8127-dff309f80002,ou=user,o=alpha,ou=services,ou=am-config"]
  },
  "lastModifiedBy": "id=a980a458-2654-4d4f-a12a-d4bfa39534f7,ou=user,ou=am-config",
  "lastModifiedDate": "2022-11-28T15:41:18.159Z",
  "createdBy": "id=a980a458-2654-4d4f-a12a-d4bfa39534f7,ou=user,ou=am-config",
  "creationDate": "2022-11-28T15:39:04.82Z"
}
```

|   |                                                                                                                                                                                                                       |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Before testing OAuth 2.0 policies, configure the `OAuth2 Provider` service for the realm to Use Policy Engine for Scope decisions.For details, refer to [Dynamic OAuth 2.0 authorization](oauth2-authorization.html). |

## Update a policy

To update an individual policy in a realm, send an HTTP PUT request to the `/json/realms/root/realms/Realm Name/policies/policy-name` endpoint with a JSON representation of the updated policy as the PUT data.

```bash
$ curl \
--request PUT \
--header "<session-cookie-name>: <policy-admin-tokenId>" \
--header "Accept-API-Version: resource=1.0" \
--header "Content-Type: application/json" \
--data '{
  "id": "myNewExamplePolicy",
  "_rev": "1669721075177",
  "name": "myNewExamplePolicy",
  "active": true,
  "description": "Example policy",
  "resources": ["https://www.example.com:443/*?*", "https://www.example.com:443/*"],
  "applicationName": "myPolicySet",
  "actionValues": {
    "POST": true,
    "GET": true
  },
  "subject": {
    "type": "Identity",
    "subjectValues": ["id=1dff18dc-ac57-4388-8127-dff309f80002,ou=user,o=alpha,ou=services,ou=am-config"]
  }
}' \
'https://<tenant-env-fqdn>_/am/json/realms/root/realms/alpha/policies/myNewExamplePolicy'
{
  "_id": "myNewExamplePolicy",
  "_rev": "1669721293147",
  "name": "myNewExamplePolicy",
  "active": true,
  "description": "Example policy",
  "resources": ["https://www.example.com:443/*?*", "https://www.example.com:443/*"],
  "applicationName": "myPolicySet",
  "actionValues": {
    "POST": true,
    "GET": true
  },
  "subject": {
    "type": "Identity",
    "subjectValues": ["id=1dff18dc-ac57-4388-8127-dff309f80002,ou=user,o=alpha,ou=services,ou=am-config"]
  },
  "lastModifiedBy": "id=1dff18dc-ac57-4388-8127-dff309f80002,ou=user,o=alpha,ou=services,ou=am-config",
  "lastModifiedDate": "2022-11-29T11:28:13.147Z",
  "createdBy": "id=1dff18dc-ac57-4388-8127-dff309f80002,ou=user,o=alpha,ou=services,ou=am-config",
  "creationDate": "2022-11-29T11:24:35.177Z"
}
```

## Delete a policy

To delete an individual policy in a realm, send an HTTP DELETE request to the `/json/realms/root/realms/Realm Name/policies/policy-name` endpoint.

```bash
$ curl \
--request DELETE \
--header "<session-cookie-name>: <policy-admin-tokenId>" \
--header "Accept-API-Version: resource=1.0" \
'https://<tenant-env-fqdn>/am/json/realms/root/realms/alpha/policies/myNewExamplePolicy'
{"_id":"myNewExamplePolicy","_rev":"0"}
```

## Copy and move policies

To copy or move an individual policy, send an HTTP POST request to the `/json/realms/root/realms/Realm Name/policies/policyName` endpoint. Include the appropriate parameters and POST data.

The appropriate parameters for copying and moving policies take the following into account:

* The realm in the URL is the realm of the policy or policies to copy or to move.

* The policy name in the URL is the name of an individual policy to copy or to move.

* Specify either `_action=copy` or `_action=move` as the query string parameter.

* When moving policies from one realm to another, use a tenant administrator's AM session cookie to authenticate.

  The policy administrator is a member of a realm, and does not have access to change another realm's settings.

The following example copies `myExamplePolicy` from the `alpha` realm to `Copied policy` in the `bravo` realm.

```bash
$ curl \
--request POST \
--header "<session-cookie-name>: <tenant-admin-tokenId>" \
--header "Accept-API-Version: resource=2.1" \
--header "Content-Type: application/json" \
--data '{
  "to": {
    "name": "Copied policy",
    "realm": "/bravo",
    "resourceType": "76656a38-5f8e-401b-83aa-4ccb74ce88d2"
  }
}' \
'https://<tenant-env-fqdn>/am/json/realms/root/realms/alpha/policies/myExamplePolicy?_action=copy'
{
  "name": "Copied policy",
  "...": "..."
}
```

The POST data JSON object for copying and moving individual policies has these fields:

| Outer field | Inner field    | Description                                                                                                                                                             |
| ----------- | -------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `to`        | `name`         | The target policy.Required unless you are copying or moving a policy to a different realm, and you want the target policy to have the same name as the original policy. |
|             | `application`  | The target policy set.Required when copying or moving a policy to a different policy set.                                                                               |
|             | `realm`        | The target realm.Required when copying or moving a policy to a different realm.                                                                                         |
|             | `resourceType` | The resource type UUID for the target policy.The resource type must exist in the target realm.Required when copying or moving a policy to a different realm.            |

The following example moves `myExamplePolicy` to `Moved policy` in the same realm. The policy administrator can complete this request because the target is in the same realm.

```bash
$ curl \
--request POST \
--header "<session-cookie-name>: <policy-admin-tokenId>" \
--header "Accept-API-Version: resource=2.1" \
--header "Content-Type: application/json" \
--data '{
  "to": {
    "name": "Moved policy",
    "realm": "/alpha",
    "resourceType": "76656a38-5f8e-401b-83aa-4ccb74ce88d2"
  }
}' \
'https://<tenant-env-fqdn>/am/json/realms/root/realms/alpha/policies/myExamplePolicy?_action=move'
{
  "name": "Moved policy",
  "...": "..."
}
```

To copy or move multiple policies, send an HTTP POST request to the `/json/realms/root/realms/Realm Name/policies` endpoint with the appropriate parameters and POST data.

The following example copies all the policies in `myPolicySet` to the `bravo` realm:

* The target policy set already exists in the `bravo` realm. It allows the same policies as its counterpart in the `alpha` realm.

* The `bravo` realm has resource types matching those in the `alpha` realm.

```bash
$ curl \
--request POST \
--header "<session-cookie-name>: <tenant-admin-tokenId>" \
--header "Accept-API-Version: resource=2.1" \
--header "Content-Type: application/json" \
--data '{
  "from": {
    "application": "myPolicySet"
  },
  "to": {
    "realm": "/bravo",
    "namePostfix": "-copy"
  },
  "resourceTypeMapping": {
    "d60b7a71-1dc6-44a5-8e48-e4b9d92dee8b": "d60b7a71-1dc6-44a5-8e48-e4b9d92dee8b",
    "76656a38-5f8e-401b-83aa-4ccb74ce88d2": "76656a38-5f8e-401b-83aa-4ccb74ce88d2"
  }
}' \
'https://<tenant-env-fqdn>/am/json/realms/root/realms/alpha/policies?_action=copy'
[{
  "name": "Moved policy-copy",
  "...": "..."
}]
```

The POST data JSON object for copying and moving multiple policies has these fields:

| Outer field           | Inner field                                   | Description                                                                                                                                                                |
| --------------------- | --------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `from`                | `application`                                 | The policy set to copy or move policies from.Required.                                                                                                                     |
| `to`                  | `application`                                 | The target policy set.Required when copying or moving policies to a different policy set.                                                                                  |
|                       | `realm`                                       | The target realm.Required when copying or moving policies to a different realm.                                                                                            |
|                       | `namePostfix`                                 | A string appended to target policy names to prevent clashes.Required.                                                                                                      |
| `resourceTypeMapping` | The UUID(s) of the original resource type(s). | The UUID(s) of the target resource type(s).Each pair of resource types must have the same resource patterns.Required when copying or moving policies to a different realm. |

## Environment conditions

You can read and query [environment condition](#environment-conditions) schema over REST.

The schemas describe the environment condition JSON objects that you include in authorization policies. Each environment condition schema has these fields:

* `title`

  The short name for the environment condition.

* `logical`

  Whether the type is a logical operator or takes a predicate.

* `config`

  The layout of the environment condition object.

Environment conditions have these characteristics:

* Environment conditions are the same for each realm.

* The only environment condition for OAuth 2.0 policies is `Script`. Use scripts to capture the `ClientId` environment attribute.

To list all environment condition schemas, send an HTTP GET request to the `/json/realms/root/realms/Realm Name/conditiontypes` endpoint with `_queryFilter=true` as the query string parameter.

```bash
$ curl \
--header "<session-cookie-name>: <policy-admin-tokenId>" \
--header "Accept-API-Version: resource=1.0, protocol=2.1" \
'https://<tenant-env-fqdn>/am/json/realms/root/realms/alpha/conditiontypes?_queryFilter=true'
```

> **Collapse: Display output**
>
> ```json
> {
>   "result": [{
>     "_id": "AMIdentityMembership",
>     "title": "AMIdentityMembership",
>     "logical": false,
>     "config": {
>       "type": "object",
>       "properties": {
>         "amIdentityName": {
>           "type": "array",
>           "items": {
>             "type": "string"
>           }
>         }
>       }
>     }
>   }, {
>     "_id": "AND",
>     "title": "AND",
>     "logical": true,
>     "config": {
>       "type": "object",
>       "properties": {
>         "conditions": {
>           "type": "array"
>         }
>       }
>     }
>   }, {
>     "_id": "AuthLevel",
>     "title": "AuthLevel",
>     "logical": false,
>     "config": {
>       "type": "object",
>       "properties": {
>         "authLevel": {
>           "type": "integer"
>         }
>       }
>     }
>   }, {
>     "_id": "AuthScheme",
>     "title": "AuthScheme",
>     "logical": false,
>     "config": {
>       "type": "object",
>       "properties": {
>         "authScheme": {
>           "type": "array",
>           "items": {
>             "type": "string"
>           }
>         },
>         "applicationIdleTimeout": {
>           "type": "integer"
>         },
>         "applicationName": {
>           "type": "string"
>         }
>       }
>     }
>   }, {
>     "_id": "AuthenticateToRealm",
>     "title": "AuthenticateToRealm",
>     "logical": false,
>     "config": {
>       "type": "object",
>       "properties": {
>         "authenticateToRealm": {
>           "type": "string"
>         }
>       }
>     }
>   }, {
>     "_id": "AuthenticateToService",
>     "title": "AuthenticateToService",
>     "logical": false,
>     "config": {
>       "type": "object",
>       "properties": {
>         "authenticateToService": {
>           "type": "string"
>         }
>       }
>     }
>   }, {
>     "_id": "IPv4",
>     "title": "IPv4",
>     "logical": false,
>     "config": {
>       "type": "object",
>       "properties": {
>         "startIp": {
>           "type": "string"
>         },
>         "endIp": {
>           "type": "string"
>         },
>         "dnsName": {
>           "type": "array",
>           "items": {
>             "type": "string"
>           }
>         }
>       }
>     }
>   }, {
>     "_id": "IPv6",
>     "title": "IPv6",
>     "logical": false,
>     "config": {
>       "type": "object",
>       "properties": {
>         "startIp": {
>           "type": "string"
>         },
>         "endIp": {
>           "type": "string"
>         },
>         "dnsName": {
>           "type": "array",
>           "items": {
>             "type": "string"
>           }
>         }
>       }
>     }
>   }, {
>     "_id": "LDAPFilter",
>     "title": "LDAPFilter",
>     "logical": false,
>     "config": {
>       "type": "object",
>       "properties": {
>         "ldapFilter": {
>           "type": "string"
>         }
>       }
>     }
>   }, {
>     "_id": "LEAuthLevel",
>     "title": "LEAuthLevel",
>     "logical": false,
>     "config": {
>       "type": "object",
>       "properties": {
>         "authLevel": {
>           "type": "integer"
>         }
>       }
>     }
>   }, {
>     "_id": "NOT",
>     "title": "NOT",
>     "logical": true,
>     "config": {
>       "type": "object",
>       "properties": {
>         "condition": {
>           "type": "object",
>           "properties": {}
>         }
>       }
>     }
>   }, {
>     "_id": "OAuth2Scope",
>     "title": "OAuth2Scope",
>     "logical": false,
>     "config": {
>       "type": "object",
>       "properties": {
>         "requiredScopes": {
>           "type": "array",
>           "items": {
>             "type": "string"
>           }
>         }
>       }
>     }
>   }, {
>     "_id": "OR",
>     "title": "OR",
>     "logical": true,
>     "config": {
>       "type": "object",
>       "properties": {
>         "conditions": {
>           "type": "array"
>         }
>       }
>     }
>   }, {
>     "_id": "Policy",
>     "title": "Policy",
>     "logical": false,
>     "config": {
>       "type": "object",
>       "properties": {
>         "className": {
>           "type": "string"
>         },
>         "properties": {
>           "type": "object"
>         }
>       }
>     }
>   }, {
>     "_id": "ResourceEnvIP",
>     "title": "ResourceEnvIP",
>     "logical": false,
>     "config": {
>       "type": "object",
>       "properties": {
>         "resourceEnvIPConditionValue": {
>           "type": "array",
>           "items": {
>             "type": "string"
>           }
>         }
>       }
>     }
>   }, {
>     "_id": "Script",
>     "title": "Script",
>     "logical": false,
>     "config": {
>       "type": "object",
>       "properties": {
>         "scriptId": {
>           "type": "string"
>         }
>       }
>     }
>   }, {
>     "_id": "Session",
>     "title": "Session",
>     "logical": false,
>     "config": {
>       "type": "object",
>       "properties": {
>         "maxSessionTime": {
>           "type": "number"
>         },
>         "terminateSession": {
>           "type": "boolean",
>           "required": true
>         }
>       }
>     }
>   }, {
>     "_id": "SessionProperty",
>     "title": "SessionProperty",
>     "logical": false,
>     "config": {
>       "type": "object",
>       "properties": {
>         "ignoreValueCase": {
>           "type": "boolean",
>           "required": true
>         },
>         "properties": {
>           "type": "object"
>         }
>       }
>     }
>   }, {
>     "_id": "SimpleTime",
>     "title": "SimpleTime",
>     "logical": false,
>     "config": {
>       "type": "object",
>       "properties": {
>         "startTime": {
>           "type": "string"
>         },
>         "endTime": {
>           "type": "string"
>         },
>         "startDay": {
>           "type": "string"
>         },
>         "endDay": {
>           "type": "string"
>         },
>         "startDate": {
>           "type": "string"
>         },
>         "endDate": {
>           "type": "string"
>         },
>         "enforcementTimeZone": {
>           "type": "string"
>         }
>       }
>     }
>   }, {
>     "_id": "Transaction",
>     "title": "Transaction",
>     "logical": false,
>     "config": {
>       "type": "object",
>       "properties": {
>         "authenticationStrategy": {
>           "type": "string"
>         },
>         "strategySpecifier": {
>           "type": "string"
>         }
>       }
>     }
>   }],
>   "resultCount": 20,
>   "pagedResultsCookie": null,
>   "totalPagedResultsPolicy": "NONE",
>   "totalPagedResults": -1,
>   "remainingPagedResults": 0
> }
> ```

To read an environment condition schema, send an HTTP GET request to the `/json/realms/root/realms/Realm Name/conditiontypes/condition-type` endpoint.

```bash
$ curl \
--header "<session-cookie-name>: <policy-admin-tokenId>" \
--header "Accept-API-Version: resource=1.0" \
'https://<tenant-env-fqdn>/am/json/realms/root/realms/alpha/conditiontypes/IPv4'
{
  "_id": "IPv4",
  "_rev": "1669721841603",
  "title": "IPv4",
  "logical": false,
  "config": {
    "type": "object",
    "properties": {
      "startIp": {
        "type": "string"
      },
      "endIp": {
        "type": "string"
      },
      "dnsName": {
        "type": "array",
        "items": {
          "type": "string"
        }
      }
    }
  }
}
```

## Subject conditions

You can read and query [subject condition](#subject-conditions) schema over REST.

The schemas describe the subject condition JSON objects that you include in authorization policies. Each environment condition schema has these fields:

* `title`

  The short name for the subject condition.

* `logical`

  Whether the type is a logical operator or takes a predicate.

* `config`

  The layout of the subject condition object.

Subject conditions are the same for each realm.

To list all subject condition schemas, send an HTTP GET request to the `/json/realms/root/realms/Realm Name/subjecttypes` endpoint with `_queryFilter=true` as the query string parameter.

```bash
$ curl \
--header "<session-cookie-name>: <policy-admin-tokenId>" \
--header "Accept-API-Version: resource=1.0, protocol=2.1" \
'https://<tenant-env-fqdn>/am/json/realms/root/realms/alpha/subjecttypes?_queryFilter=true'
```

> **Collapse: Display output**
>
> ```json
> {
>   "result": [{
>     "_id": "AND",
>     "title": "AND",
>     "logical": true,
>     "config": {
>       "type": "object",
>       "properties": {
>         "subjects": {
>           "type": "array"
>         }
>       }
>     }
>   }, {
>     "_id": "AuthenticatedUsers",
>     "title": "AuthenticatedUsers",
>     "logical": false,
>     "config": {
>       "type": "object",
>       "properties": {}
>     }
>   }, {
>     "_id": "Identity",
>     "title": "Identity",
>     "logical": false,
>     "config": {
>       "type": "object",
>       "properties": {
>         "subjectValues": {
>           "type": "array",
>           "items": {
>             "type": "string"
>           }
>         }
>       }
>     }
>   }, {
>     "_id": "JwtClaim",
>     "title": "JwtClaim",
>     "logical": false,
>     "config": {
>       "type": "object",
>       "properties": {
>         "claimName": {
>           "type": "string"
>         },
>         "claimValue": {
>           "type": "string"
>         }
>       }
>     }
>   }, {
>     "_id": "NONE",
>     "title": "NONE",
>     "logical": false,
>     "config": {
>       "type": "object",
>       "properties": {}
>     }
>   }, {
>     "_id": "NOT",
>     "title": "NOT",
>     "logical": true,
>     "config": {
>       "type": "object",
>       "properties": {
>         "subject": {
>           "type": "object",
>           "properties": {}
>         }
>       }
>     }
>   }, {
>     "_id": "OR",
>     "title": "OR",
>     "logical": true,
>     "config": {
>       "type": "object",
>       "properties": {
>         "subjects": {
>           "type": "array"
>         }
>       }
>     }
>   }, {
>     "_id": "Policy",
>     "title": "Policy",
>     "logical": false,
>     "config": {
>       "type": "object",
>       "properties": {
>         "name": {
>           "type": "string"
>         },
>         "className": {
>           "type": "string"
>         },
>         "values": {
>           "type": "array",
>           "items": {
>             "type": "string"
>           }
>         }
>       }
>     }
>   }],
>   "resultCount": 8,
>   "pagedResultsCookie": null,
>   "totalPagedResultsPolicy": "NONE",
>   "totalPagedResults": -1,
>   "remainingPagedResults": 0
> }
> ```

To read a subject condition schema, send an HTTP GET request to the `/json/realms/root/realms/Realm Name/subjecttypes/subject-type` endpoint.

```bash
$ curl \
--header "<session-cookie-name>: <policy-admin-tokenId>" \
--header "Accept-API-Version: resource=1.0, protocol=2.1" \
'https://<tenant-env-fqdn>/am/json/realms/root/realms/alpha/subjecttypes/Identity'
{
  "_id": "Identity",
  "_rev": "1669721896953",
  "title": "Identity",
  "logical": false,
  "config": {
    "type": "object",
    "properties": {
      "subjectValues": {
        "type": "array",
        "items": {
          "type": "string"
        }
      }
    }
  }
}
```

## Decision combiners

Decision combiners describe how to resolve policy decisions when multiple policies apply.

Decision combiners are the same for each realm.

To list all decision combiners, send an HTTP GET request to the `/json/realms/root/realms/Realm Name/decisioncombiners` endpoint with `_queryFilter=true` as the query string parameter.

```bash
$ curl \
--header "<session-cookie-name>: <policy-admin-tokenId>" \
--header "Accept-API-Version: resource=1.0, protocol=2.1" \
'https://<tenant-env-fqdn>/am/json/realms/root/realms/alpha/decisioncombiners?_queryFilter=true'
{
  "result": [{
    "_id": "DenyOverride",
    "title": "DenyOverride"
  }],
  "resultCount": 1,
  "pagedResultsCookie": null,
  "totalPagedResultsPolicy": "NONE",
  "totalPagedResults": -1,
  "remainingPagedResults": 0
}
```

To read a decision combiner, send an HTTP GET request to the `/json/realms/root/realms/Realm Name/decisioncombiners/decision-combiner` endpoint.

```bash
$ curl \
--header "<session-cookie-name>: <policy-admin-tokenId>" \
--header "Accept-API-Version: resource=1.0" \
'https://<tenant-env-fqdn>/am/json/realms/root/realms/alpha/decisioncombiners/DenyOverride'
{"_id":"DenyOverride","_rev":"1669722054745","title":"DenyOverride"}
```

---

---
title: Policy sets
description: Group policies with similar characteristics into policy sets that protect websites and applications
component: pingoneaic
page_id: pingoneaic:am-authorization:configuring-policy-sets
canonical_url: https://docs.pingidentity.com/pingoneaic/am-authorization/configuring-policy-sets.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Authorization", "Policy", "Configuration"]
page_aliases: ["authorization-guide:rest-api-authz-application-types.adoc", "authorization-guide:configuring-policy-sets.adoc"]
section_ids:
  default-policy-sets: Default policy sets
  agents-and-policy-sets: Agents and policy sets
---

# Policy sets

Advanced Identity Cloud uses a *policy* to determine whether to grant a principal access to a resource.

Policies belong to *policy sets*. Policy sets define a template for policies that apply to one or more [*resource types*](configuring-resource-types.html). A policy set groups policies with similar characteristics that protect websites, web applications, or other resources. It eliminates the need to configure the same basic settings repeatedly for each policy.

*Application types* are templates for policy sets. Application types aren't available under Native Consoles > Access Management. When you define a policy or policy set over REST, the application type appears in the JSON resource, for example, `"iPlanetAMWebAgentService"`.

## Default policy sets

Advanced Identity Cloud includes the following default policy sets:

* Customer Application Policy Set (`customerApplicationPolicySet`)

  The policy set is designed for application authorization journeys. It uses the `Authentication` resource type to simplify authentication flows.

  Learn about app authorization journeys in the [App Policy Decision node](https://docs.pingidentity.com/auth-node-ref/latest/app-policy-decision.html) documentation.

* Default OAuth2 Scopes Policy Set (`oauth2Scopes`)

  Use this policy set for `OAuth2 Scope` resource types.

|   |                                                                        |
| - | ---------------------------------------------------------------------- |
|   | Create your own policy sets to control access to `URL` resource types. |

## Agents and policy sets

You can specify a policy set and the realm in a web or Java agent profile.

Advanced Identity Cloud directs requests from the agent to the specified realm and policy set, providing compatibility with older web and Java agents.

Find more information in the agent documentation:

* Java agents

  [Policy Evaluation Realm Map](https://docs.pingidentity.com/java-agents/latest/properties-reference/org.forgerock.agents.policy.evaluation.realm.map.html)\
  [Policy Set Map](https://docs.pingidentity.com/java-agents/latest/properties-reference/org.forgerock.agents.policy.set.map.html)

* Web agents

  [Policy Evaluation Realm](https://docs.pingidentity.com/web-agents/latest/properties-reference/org.forgerock.openam.agents.config.policy.evaluation.realm.html)\
  [Policy Set](https://docs.pingidentity.com/web-agents/latest/properties-reference/org.forgerock.openam.agents.config.policy.evaluation.application.html)

---

---
title: Policy sets in the UI
description: Create and manage policy sets that group policies for protecting websites and applications
component: pingoneaic
page_id: pingoneaic:am-authorization:policy-sets-ui
canonical_url: https://docs.pingidentity.com/pingoneaic/am-authorization/policy-sets-ui.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Authorization", "Policy", "Configuration"]
page_aliases: ["authorization-guide:policy-sets-ui.adoc"]
section_ids:
  policy_set_names: Policy set names
---

# Policy sets in the UI

You manage policy sets under Native Consoles > Access Management. Go to Realms > *Realm Name* > Authorization > Policy Sets.

| To...               | Action                                                                                                                                                           |
| ------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Create a policy set | Click + New Policy Set.When creating a policy set, specify an ID and select at least one resource type.You cannot change the ID after you create the policy set. |
| Modify a policy set | Click the policy set name or the pencil icon ([icon: pencil-alt, set=fa]).                                                                                       |
| Delete a policy set | Click the delete icon ([icon: times, set=fa]) or click the policy set name then the x Delete button.You can't delete a set that contains policies.               |

## Policy set names

Don't use any of the following characters in policy, policy set, or resource type names:

* Double quotes (`"`)

* Plus sign (`+`)

* Comma (`,`)

* Less than (`<`)

* Equals (`=`)

* Greater than (`>`)

* Backslash (`\`)

* Forward slash (`/`)

* Semicolon (`;`)

* Null (`\u0000`)

---

---
title: Policy sets over REST
description: Manage policy sets over REST to create, read, update, and delete authorization policy sets
component: pingoneaic
page_id: pingoneaic:am-authorization:rest-api-authz-applications
canonical_url: https://docs.pingidentity.com/pingoneaic/am-authorization/rest-api-authz-applications.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Authorization", "Policy", "Resource", "Configuration", "REST API"]
page_aliases: ["authorization-guide:rest-api-authz-applications.adoc"]
section_ids:
  access_the_endpoint: Access the endpoint
  rest-api-authz-applications-query: Query policy sets
  rest-api-authz-applications-read: Read a policy set
  rest-api-authz-applications-create: Create a policy set
  rest-api-authz-applications-update: Update a policy set
  rest-api-authz-applications-delete: Delete a policy set
---

# Policy sets over REST

You can manage policy sets over REST at the `applications` endpoint. ("Application" is the internal name for a policy set.)

Advanced Identity Cloud stores policy sets as JSON objects. A policy set can include the following fields. The fields have JSON values—​strings, numbers, objects, sets, arrays, `true`, `false`, and `null`.

| Policy set field      | Description                                                                                                                                                                                                                                                                                                                         |
| --------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `_id`, `name`         | A unique string identifying the policy set.Don't use any of the following characters in policy, policy set, or resource type names:- Double quotes (`"`)

- Plus sign (`+`)

- Comma (`,`)

- Less than (`<`)

- Equals (`=`)

- Greater than (`>`)

- Backslash (`\`)

- Forward slash (`/`)

- Semicolon (`;`)

- Null (`\u0000`) |
| `_rev`(1)             | A system-generated revision string.                                                                                                                                                                                                                                                                                                 |
| `actions`             | An object where each field is an action name.The value for each action name field is a boolean indicating whether to allow the action by default.                                                                                                                                                                                   |
| `applicationType`     | A string containing the application type name.Use `"iPlanetAMWebAgentService"`.                                                                                                                                                                                                                                                     |
| `attributeNames`      | An optional array of response attribute name strings restricting what policies in this set can return.                                                                                                                                                                                                                              |
| `conditions`          | An array of environment condition identifier strings defining environment conditions allowed for policies in this set.                                                                                                                                                                                                              |
| `description`         | An optional text string to help identify the policy set.                                                                                                                                                                                                                                                                            |
| `editable`            | A boolean indicating whether you can edit this policy set definition after creation.                                                                                                                                                                                                                                                |
| `entitlementCombiner` | An optional string identifying how Advanced Identity Cloud evaluates multiple policies for a resource.Use `"DenyOverride"`.                                                                                                                                                                                                         |
| `realm`               | A string identifying the realm for this policy set.                                                                                                                                                                                                                                                                                 |
| `resources`           | An array of resource pattern strings for resources governed by policies in this set.                                                                                                                                                                                                                                                |
| `resourceComparator`  | An optional string identifying the fully qualified class name of the implementation to match resources for policies.                                                                                                                                                                                                                |
| `saveIndex`           | An optional string identifying the fully qualified class name of the implementation to save indexes for policies.                                                                                                                                                                                                                   |
| `searchIndex`         | An optional string identifying the fully qualified class name of the implementation to index policies.                                                                                                                                                                                                                              |
| `subjects`            | Array of subject type identifier strings defining subject types allowed for policies in this set.                                                                                                                                                                                                                                   |
| `createdBy`(1)        | A string indicating who created the policy set.                                                                                                                                                                                                                                                                                     |
| `creationDate`(1)     | An integer containing the creation time in milliseconds since January 1, 1970.                                                                                                                                                                                                                                                      |
| `lastModifiedBy`(1)   | A string indicating who last changed the policy set.                                                                                                                                                                                                                                                                                |
| `lastModifiedDate`(1) | An integer containing the last modified time in milliseconds since January 1, 1970.                                                                                                                                                                                                                                                 |

(1) Do not change the value of this field.

## Access the endpoint

The REST calls to manage policy sets rely on an account with the appropriate privileges:

1. Create a policy set administrator.

   In the Advanced Identity Cloud admin console, select Identities > Manage > *Realm Name* Realm - Users > + New *Realm Name* Realm - User and fill the required fields.

   Record the username and password.

2. Create a group that grants the privileges to the policy set administrator.

   Under Native Consoles > Access Management, select Realms > *Realm Name* > Identities > Groups > + Add Group. Create a group with the following settings:

   * Group ID

     `am-policy-set-admins`

   * Members

     The policy set administrator whose username you recorded

   * Privileges

     Policy Admin\
     Application Modify Access\
     Application Read Access

3. Before making REST calls to manage policy sets, authenticate as the policy set administrator:

   ```bash
   $ curl \
   --request POST \
   --header 'Content-Type: application/json' \
   --header 'X-OpenAM-Username: <policy-set-admin-username>' \
   --header 'X-OpenAM-Password: <policy-set-admin-password>' \
   --header 'Accept-API-Version: resource=2.0, protocol=1.0' \
   'https://<tenant-env-fqdn>/am/json/realms/root/realms/alpha/authenticate'
   {
     "tokenId": "<policy-set-admin-tokenId>",
     "successUrl": "/enduser/?realm=/alpha",
     "realm": "/alpha"
   }
   ```

   For additional details, refer to [Session tokens after authentication](../am-authentication/rest-using-ssotokens.html).

   Use the `<policy-set-admin-tokenId>` as the value of the `<session-cookie-name>` header to access the REST endpoints.

## Query policy sets

To list all the policy sets defined for a realm, send an HTTP GET request to the `/json/realms/root/realms/Realm Name/applications` endpoint with `_queryFilter=true` as the query string parameter.

```bash
$ curl \
--header "<session-cookie-name>: <policy-set-admin-tokenId>" \
--header "Accept-API-Version: resource=1.0" \
'https://<tenant-env-fqdn>/am/json/realms/root/realms/alpha/applications?_queryFilter=true'
{
  "result": [{
    "_id": "oauth2Scopes",
    "name": "oauth2Scopes",
    "description": "The built-in Application used by the OAuth2 scope authorization process.",
    "attributeNames": [],
    "createdBy": "id=dsameuser,ou=user,ou=am-config",
    "conditions": ["Script", "AMIdentityMembership", "IPv6", "SimpleTime", "IPv4", "LEAuthLevel", "LDAPFilter", "AuthScheme", "Session", "AND", "AuthenticateToRealm", "ResourceEnvIP", "SessionProperty", "OAuth2Scope", "OR", "Transaction", "NOT", "AuthLevel", "AuthenticateToService"],
    "lastModifiedBy": "id=dsameuser,ou=user,ou=am-config",
    "creationDate": 1578580064992,
    "lastModifiedDate": 1595479030629,
    "subjects": ["AuthenticatedUsers", "NOT", "Identity", "OR", "AND", "NONE", "JwtClaim"],
    "saveIndex": null,
    "searchIndex": null,
    "entitlementCombiner": "DenyOverride",
    "resourceComparator": null,
    "editable": true,
    "applicationType": "iPlanetAMWebAgentService",
    "actions": {
      "GRANT": true
    },
    "resources": ["*://*:*/*", "*://*:*/*?*", "*"],
    "realm": "/alpha"
  }],
  "resultCount": 1,
  "pagedResultsCookie": null,
  "totalPagedResultsPolicy": "NONE",
  "totalPagedResults": -1,
  "remainingPagedResults": 0
}
```

Adapt the [query string parameters](../developer-docs/crest/query.html) to refine the results.

| Field              | Supported `_queryFilter` operators                                                                                 |
| ------------------ | ------------------------------------------------------------------------------------------------------------------ |
| `name`             | Equals (`eq`)                                                                                                      |
| `description`      |                                                                                                                    |
| `createdBy`        |                                                                                                                    |
| `lastModifiedBy`   |                                                                                                                    |
| `creationDate`     | Equals (`eq`)(1) Greater than or equal to (`ge`) Greater than (`gt`) Less than or equal to (`le`) Less than (`lt`) |
| `lastModifiedDate` |                                                                                                                    |

(1) Do not use regular expression patterns with `eq`.

## Read a policy set

To read a specific policy set in a realm, send an HTTP GET request to the `/json/realms/root/realms/Realm Name/applications/policy-set-name` endpoint.

```bash
$ curl \
--header "<session-cookie-name>: <policy-set-admin-tokenId>" \
--header "Accept-API-Version: resource=1.0" \
'https://<tenant-env-fqdn>/am/json/realms/root/realms/alpha/applications/oauth2Scopes'
{
  "_id": "oauth2Scopes",
  "_rev": "1595479030629",
  "name": "oauth2Scopes",
  "description": "The built-in Application used by the OAuth2 scope authorization process.",
  "attributeNames": [],
  "createdBy": "id=dsameuser,ou=user,ou=am-config",
  "conditions": ["Script", "AMIdentityMembership", "IPv6", "SimpleTime", "IPv4", "LEAuthLevel", "LDAPFilter", "AuthScheme", "Session", "AND", "AuthenticateToRealm", "ResourceEnvIP", "SessionProperty", "OAuth2Scope", "OR", "Transaction", "NOT", "AuthLevel", "AuthenticateToService"],
  "lastModifiedBy": "id=dsameuser,ou=user,ou=am-config",
  "creationDate": 1578580064992,
  "lastModifiedDate": 1595479030629,
  "subjects": ["AuthenticatedUsers", "NOT", "Identity", "OR", "AND", "NONE", "JwtClaim"],
  "saveIndex": null,
  "searchIndex": null,
  "entitlementCombiner": "DenyOverride",
  "resourceComparator": null,
  "editable": true,
  "applicationType": "iPlanetAMWebAgentService",
  "actions": {
    "GRANT": true
  },
  "resources": ["*://*:*/*", "*://*:*/*?*", "*"],
  "realm": "/alpha"
}
```

## Create a policy set

To create a policy set in a realm, send an HTTP POST request to the `/json/realms/root/realms/Realm Name/applications` endpoint with `_action=create` as the query string parameter and a JSON representation of the policy set as the POST data.

```bash
$ curl \
--request POST \
--header "Content-Type: application/json" \
--header "<session-cookie-name>: <policy-set-admin-tokenId>" \
--header "Accept-API-Version: resource=1.0" \
--data '{
  "name": "samplePolicySet",
  "description": "Sample policy set",
  "conditions": ["Script", "AMIdentityMembership", "IPv6", "IPv4", "SimpleTime", "LEAuthLevel", "LDAPFilter", "AuthScheme", "Session", "AND", "AuthenticateToRealm", "ResourceEnvIP", "Policy", "OAuth2Scope", "SessionProperty", "OR", "Transaction", "NOT", "AuthLevel", "AuthenticateToService"],
  "subjects": ["AuthenticatedUsers", "NOT", "Identity", "OR", "AND", "NONE", "Policy", "JwtClaim"],
  "entitlementCombiner": "DenyOverride",
  "attributeNames": [],
  "saveIndex": null,
  "searchIndex": null,
  "resourceComparator": null,
  "applicationType": "iPlanetAMWebAgentService",
  "actions": {
    "HEAD": true,
    "DELETE": true,
    "POST": true,
    "GET": true,
    "OPTIONS": true,
    "PUT": true,
    "PATCH": true
  },
  "resources": ["*://*:*/*", "*://*:*/*?*"],
  "realm": "/alpha"
}' \
'https://<tenant-env-fqdn>/am/json/realms/root/realms/alpha/applications/?_action=create'
{
  "_id": "samplePolicySet",
  "_rev": "1669134131264",
  "name": "samplePolicySet",
  "description": "Sample policy set",
  "attributeNames": [],
  "createdBy": "id=1dff18dc-ac57-4388-8127-dff309f80002,ou=user,o=alpha,ou=services,ou=am-config",
  "conditions": ["Script", "AMIdentityMembership", "IPv6", "IPv4", "SimpleTime", "LEAuthLevel", "LDAPFilter", "AuthScheme", "Session", "AND", "AuthenticateToRealm", "ResourceEnvIP", "Policy", "OAuth2Scope", "SessionProperty", "OR", "Transaction", "NOT", "AuthLevel", "AuthenticateToService"],
  "lastModifiedBy": "id=1dff18dc-ac57-4388-8127-dff309f80002,ou=user,o=alpha,ou=services,ou=am-config",
  "creationDate": 1669134131264,
  "lastModifiedDate": 1669134131264,
  "subjects": ["AuthenticatedUsers", "NOT", "Identity", "OR", "AND", "NONE", "Policy", "JwtClaim"],
  "saveIndex": null,
  "searchIndex": null,
  "entitlementCombiner": "DenyOverride",
  "resourceComparator": null,
  "editable": true,
  "applicationType": "iPlanetAMWebAgentService",
  "actions": {
    "HEAD": true,
    "DELETE": true,
    "POST": true,
    "GET": true,
    "OPTIONS": true,
    "PUT": true,
    "PATCH": true
  },
  "resources": ["*://*:*/*", "*://*:*/*?*"],
  "realm": "/alpha"
}
```

## Update a policy set

To update a specific policy set in a realm, send an HTTP PUT request to the `/json/realms/root/realms/Realm Name/applications/policy-set-name` endpoint with a JSON representation of the updated policy set as the PUT data.

```bash
$ curl \
--request PUT \
--header "Content-Type: application/json" \
--header "<session-cookie-name>: <policy-set-admin-tokenId>" \
--header "Accept-API-Version: resource=1.0" \
--data '{
  "name": "samplePolicySet",
  "description": "Sample policy set",
  "conditions": ["Script", "AMIdentityMembership", "IPv6", "IPv4", "SimpleTime", "LEAuthLevel", "LDAPFilter", "AuthScheme", "Session", "AND", "AuthenticateToRealm", "ResourceEnvIP", "Policy", "OAuth2Scope", "SessionProperty", "OR", "Transaction", "NOT", "AuthLevel", "AuthenticateToService"],
  "subjects": ["AuthenticatedUsers", "NOT", "Identity", "OR", "AND", "NONE", "Policy", "JwtClaim"],
  "entitlementCombiner": "DenyOverride",
  "attributeNames": [],
  "saveIndex": null,
  "searchIndex": null,
  "resourceComparator": null,
  "applicationType": "iPlanetAMWebAgentService",
  "actions": {
    "HEAD": true,
    "DELETE": false,
    "POST": true,
    "GET": true,
    "OPTIONS": true,
    "PUT": false,
    "PATCH": false
  },
  "resources": ["*://*:*/*", "*://*:*/*?*"],
  "realm": "/alpha"
}' \
'https://<tenant-env-fqdn>/am/json/realms/root/realms/alpha/applications/samplePolicySet'
{
  "_id": "samplePolicySet",
  "_rev": "1669134221194",
  "name": "samplePolicySet",
  "description": "Sample policy set",
  "attributeNames": [],
  "createdBy": "id=1dff18dc-ac57-4388-8127-dff309f80002,ou=user,o=alpha,ou=services,ou=am-config",
  "conditions": ["Script", "AMIdentityMembership", "IPv6", "IPv4", "SimpleTime", "LEAuthLevel", "LDAPFilter", "AuthScheme", "Session", "AND", "AuthenticateToRealm", "ResourceEnvIP", "Policy", "OAuth2Scope", "SessionProperty", "OR", "Transaction", "NOT", "AuthLevel", "AuthenticateToService"],
  "lastModifiedBy": "id=1dff18dc-ac57-4388-8127-dff309f80002,ou=user,o=alpha,ou=services,ou=am-config",
  "creationDate": 1669134131264,
  "lastModifiedDate": 1669134221194,
  "subjects": ["AuthenticatedUsers", "NOT", "Identity", "OR", "AND", "NONE", "Policy", "JwtClaim"],
  "saveIndex": null,
  "searchIndex": null,
  "entitlementCombiner": "DenyOverride",
  "resourceComparator": null,
  "editable": true,
  "applicationType": "iPlanetAMWebAgentService",
  "actions": {
    "HEAD": true,
    "DELETE": false,
    "POST": true,
    "GET": true,
    "OPTIONS": true,
    "PATCH": false,
    "PUT": false
  },
  "resources": ["*://*:*/*", "*://*:*/*?*"],
  "realm": "/alpha"
}
```

## Delete a policy set

To delete a policy set in a realm, send an HTTP DELETE request to the `/json/realms/root/realms/Realm Name/applications/policy-set-name` endpoint.

```bash
$ curl \
--request DELETE \
--header "<session-cookie-name>: <policy-set-admin-tokenId>" \
--header "Accept-API-Version: resource=1.0" \
'https://<tenant-env-fqdn>/am/json/realms/root/realms/alpha/applications/samplePolicySet'
{"_id":"samplePolicySet","_rev":"0"}
```

You cannot delete a policy set that contains policies. If you attempt to delete the policy set, Advanced Identity Cloud returns an HTTP 409 Conflict status code and a message like the one in the following example:

```bash
$ curl \
--request DELETE \
--header "<session-cookie-name>: <policy-set-admin-tokenId>" \
--header "Accept-API-Version: resource=1.0" \
'https://<tenant-env-fqdn>/am/json/realms/root/realms/alpha/applications/oauth2Scopes'
{
  "code": 409,
  "reason": "Conflict",
  "message": "Application cannot be altered because policies exist within the Application. Remove all policies from the Application before attempting to delete the Application."
}
```

Remove the policies from the set before you delete it.

---

---
title: Request authorization from Advanced Identity Cloud
description: Configure policy enforcement points to request authorization decisions from the system
component: pingoneaic
page_id: pingoneaic:am-authorization:requesting-authorization
canonical_url: https://docs.pingidentity.com/pingoneaic/am-authorization/requesting-authorization.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Authorization", "Policy", "Agents"]
page_aliases: ["authorization-guide:requesting-authorization.adoc"]
---

# Request authorization from Advanced Identity Cloud

When you have configured Advanced Identity Cloud to determine whether to grant or deny access based on your configured [policies](configuring-policies.html), you must configure policy enforcement points (PEPs) to use Advanced Identity Cloud.

The Ping Identity Platform provides the following PEPs:

* Web agents and Java agents

  Add-on components installed on the web server or container that serves your applications. The web and Java agents are tightly integrated with Advanced Identity Cloud and serve exclusively as PEPs.

  For more information, refer to [Policy enforcement](https://docs.pingidentity.com/web-agents/latest/user-guide/pep.html) in the ForgeRock web agents documentation, or to [Policy enforcement](https://docs.pingidentity.com/java-agents/latest/user-guide/pep.html) in the ForgeRock Java agents documentation.

* PingGateway

  A high-performance reverse proxy server that can also function as a PEP.

  For more information, refer to [Policy enforcement](https://docs.pingidentity.com/pinggateway/latest/gateway-guide/policy-enforcement.html) in the PingGateway documentation.

The Ping Identity Platform PEPs intercept inbound client requests to access resources in your website or application. Based on internal rules, the PEPs can defer requests to Advanced Identity Cloud for policy evaluation. Because they are tightly integrated with Advanced Identity Cloud, you do not need additional code to request policy evaluation or to manage advices.

ForgeRock recommends you use the Ping Identity Platform PEPs; however, you can code your own and make REST calls to Advanced Identity Cloud to request policy evaluation.

Related information: [Request policy decisions over REST](rest-api-authz-policy-decisions.html)

---

---
title: Request policy decisions over REST
description: Request policy evaluation decisions over REST for specific resources and subjects with environment context
component: pingoneaic
page_id: pingoneaic:am-authorization:rest-api-authz-policy-decisions
canonical_url: https://docs.pingidentity.com/pingoneaic/am-authorization/rest-api-authz-policy-decisions.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Authorization", "Policy", "REST API", "Evaluation"]
section_ids:
  access_the_endpoint: Access the endpoint
  rest-api-authz-policy-decision-concrete: Request policy decisions for specific resources
  rest-api-authz-policy-decision-advice: Policy decision advice
  rest-api-authz-policy-decision-subtree: Request policy decisions for a tree of resources
---

# Request policy decisions over REST

You can request policy decisions from Advanced Identity Cloud by using the REST API. Advanced Identity Cloud evaluates requests based on the context and the policies configured and returns decisions that indicate what actions are allowed or denied, as well as any attributes or advice for the resources specified.

|   |                                                    |
| - | -------------------------------------------------- |
|   | This section does not apply to OAuth 2.0 policies. |

Use the `/json/realms/root/realms/realm-name/policies` endpoints to request policy evaluation.

When making a REST API call, specify the realm in the path component of the endpoint. You must specify the entire hierarchy of the realm. Prefix each realm in the hierarchy with the `realms/` keyword. For example, `/realms/root/realms/alpha`.

To request decisions for specific resources, refer to [Request policy decisions for specific resources](#rest-api-authz-policy-decision-concrete).

To request decisions for a resource and all resources beneath it, refer to [Request policy decisions for a tree of resources](#rest-api-authz-policy-decision-subtree).

## Access the endpoint

The REST calls to request policy decisions require that the subjects have the appropriate privileges:

1. Create a group that grants the privileges required to request policy decisions.

   Under Native Consoles > Access Management, select Realms > *Realm Name* > Identities > Groups > + Add Group to create a group with the following settings:

   * Group ID

     `am-policy-evaluators`

   * Members

     Users that will perform policy evaluations

   * Privileges

     Entitlement Rest Access

2. Before making REST calls to evaluate policies, authenticate as the user whose access you want to evaluate:

   ```bash
   $ curl \
   --request POST \
   --header 'Content-Type: application/json' \
   --header 'X-OpenAM-Username: <subject-username>' \
   --header 'X-OpenAM-Password: <subject-password>' \
   --header 'Accept-API-Version: resource=2.0, protocol=1.0' \
   'https://<tenant-env-fqdn>/am/json/realms/root/realms/alpha/authenticate'
   {
     "tokenId": "<subject-tokenId>",
     "successUrl": "/enduser/?realm=/alpha",
     "realm": "/alpha"
   }
   ```

   For additional details, refer to [Session tokens after authentication](../am-authentication/rest-using-ssotokens.html).

   Use the `<subject-tokenId>` as the value of the `<session-cookie-name>` header to access the REST endpoints.

## Request policy decisions for specific resources

To request policy decisions for specific resources, send an HTTP POST request to the `policies` endpoint with the `evaluate` action, for example: `/json/realms/root/realms/alpha/policies?_action=evaluate`.

The payload for the HTTP POST is a JSON object that specifies at least the resources and takes the following form.

```json
{
    "resources": [
        "resource1",
        "resource2",
        ...,
        "resourceN"
    ],
    "application": "The policy set that contains the policies to evaluate against",
    "subject": {
        "ssoToken": "SSO token ID string",
        "jwt": "JSON Web Token string",
        "claims": {
            "key": "value",
            ...
        }
    },
    "environment": {
        "optional key1": [
            "value",
            "another value",
            ...
        ],
        "optional key2": [
            "value",
            "another value",
            ...
        ],
        ...
    }
}
```

The values for the fields shown above are explained below:

* `resources`

  This required field specifies the list of resources for which to return decisions.

  For example, depending on the patterns defined in the policy set, you could request decisions for resource URLs.

  ```json
  {
      "resources": [
          "http://www.example.com/index.html",
          "http://www.example.com/do?action=run"
      ]
  }
  ```

* `application`

  This field holds the name of the policy set, for example, `samplePolicySet`.

  For more on policy sets, refer to [Policy sets over REST](rest-api-authz-applications.html).

* `subject`

  This optional field holds an object that represents the subject.

  If you do not specify the subject, Advanced Identity Cloud uses the SSO token ID of the subject making the request.

  You can specify one or more of the following keys. If you specify multiple keys, the subject can have multiple associated principals, and you can use subject conditions corresponding to any type in the request.

  * `ssoToken`

    The value is the SSO token ID string for the subject, returned for example on successful authentication as described in [Authenticate over REST](../am-authentication/authn-rest.html).

    You can use an OpenID Connect ID token if the client that the token was issued for is authorized to use ID tokens as session tokens. For more information, refer to [ID tokens as session tokens](../am-oidc1/oidc-additional-use-cases.html#idtokens-as-session-tokens).

  * `jwt`

    The value is a JWT string.

  * `claims`

    The value is an object (map) of JWT claims to their values. Any string is permitted, but you must include the `sub` claim.

* `environment`

  This optional field holds a map of keys to lists of values.

  If you do not specify the environment, the default is an empty map.

The example below requests policy decisions for two URL resources. The `<session-cookie-name>` header sets the SSO token for a user who has access to perform the operation.

```bash
$ curl \
--request POST \
--header "Content-Type: application/json" \
--header "Accept-API-Version: resource=2.1" \
--header "<session-cookie-name>: AQIC5..." \
--data '{
    "resources":[
        "http://www.example.com/index.html",
        "http://www.example.com/do?action=run"
    ],
    "application":"iPlanetAMWebAgentService"
}' \
"https://<tenant-env-fqdn>/am/json/realms/root/realms/alpha/policies/?_action=evaluate"
[
    {
        "resource":"http://www.example.com/do?action=run",
        "actions":{

        },
        "attributes":{

        },
        "advices":{
            "AuthLevelConditionAdvice":[
                "3"
            ]
        }
    },
    {
        "resource":"http://www.example.com/index.html",
        "actions":{
            "POST":false,
            "GET":true
        },
        "attributes":{
            "cn":[
                "babs"
            ]
        },
        "advices":{

        }
    }
]
```

In the JSON list of decisions returned for each resource, Advanced Identity Cloud includes these fields.

* `resource`

  A resource specified in the request.

  The decisions returned are not guaranteed to be in the same order as the resources were requested.

* `actions`

  A map of action name keys to Boolean values that indicate whether the action is allowed (`true`) or denied (`false`) for the specified resource.

  In the example, for resource `http://www.example.com:80/index.html` HTTP GET is allowed, whereas HTTP POST is denied.

* `attributes`

  A map of attribute names to their values if any response attributes are returned according to applicable policies.

  In the example, the policy that applies to `http://www.example.com:80/index.html` causes the value of the subject's "cn" profile attribute to be returned.

* `advices`

  A map of advice names to their values if any advice is returned according to applicable policies.

  The `advices` field can provide hints regarding what Advanced Identity Cloud needs to take the authorization decision.

  In the example, the policy that applies to `http://www.example.com:80/do?action=run` requests that the subject be authenticated at an authentication level of at least 3.

  ```json
  {
      "advices": {
          "AuthLevelConditionAdvice": [
              "3"
          ]
      }
  }
  ```

  Refer to [Policy decision advice](#rest-api-authz-policy-decision-advice) for details.

You can use the query string parameters `_prettyPrint=true` to make the output easier to read, and `_fields=field-name[,field-name...]` to limit the fields returned in the output.

## Policy decision advice

When Advanced Identity Cloud returns a policy decision, the JSON for the decision can include an "advices" field. This field contains hints for the policy enforcement point.

```json
{
    "advices": {
        "type": [
            "advice"
        ]
    }
}
```

The "advices" returned depend on policy conditions. For more information about policy conditions, refer to [Policies over REST](rest-api-authz-policies.html).

This section shows examples of the different types of policy decision advice and the conditions that cause Advanced Identity Cloud to return the advice.

`AuthLevel` and `LEAuthLevel` condition failures can result in advice showing the expected or maximum possible authentication level. For example, failure against the following condition:

```json
{
    "type": "AuthLevel",
    "authLevel": 2
}
```

Leads to this advice:

```json
{
    "AuthLevelConditionAdvice": [
        "2"
    ]
}
```

An `AuthenticateToRealm` condition failure can result in advice showing the name of the realm to which authentication is required. For example, failure against the following condition:

```json
{
    "type": "AuthenticateToRealm",
    "authenticateToRealm": "alpha"
}
```

Leads to this advice:

```json
{
    "AuthenticateToRealmConditionAdvice": [
        "/alpha"
    ]
}
```

An `AuthenticateToService` condition failure can result in advice showing the name of the required authentication journey. For example, failure against the following condition:

```json
{
    "type": "AuthenticateToService",
    "authenticateToService": "MyIdentityCloudJourney"
}
```

Leads to this advice:

```json
{
    "AuthenticateToServiceConditionAdvice": [
        "MyIdentityCloudJourney"
    ]
}
```

A `ResourceEnvIP` condition failure can result in advice that indicates corrective action to be taken. The advice varies, depending on what the condition tests. For example, failure against the following condition:

```json
{
    "type": "ResourceEnvIP",
    "resourceEnvIPConditionValue": [
        "IF IP=[127.0.0.12] THEN authlevel=4"
    ]
}
```

Leads to this advice:

```json
{
    "AuthLevelConditionAdvice": [
        "4"
    ]
}
```

Failure against a different type of `ResourceEnvIP` condition, such as the following:

```json
{
    "type": "ResourceEnvIP",
    "resourceEnvIPConditionValue": [
        "IF IP=[127.0.0.11] THEN service=MyIdentityCloudJourney"
    ]
}
```

Leads to this advice:

```json
{
    "AuthenticateToServiceConditionAdvice": [
        "MyIdentityCloudJourney"
    ]
}
```

A `Session` condition failure can result in advice showing that access was denied because the user's session was active longer than allowed by the condition. The advice also shows if the user's session was terminated and reauthentication is required. For example, failure against the following condition:

```json
{
    "type": "Session",
    "maxSessionTime": "10",
    "terminateSession": false
}
```

Leads to this advice:

```json
{
    "SessionConditionAdvice": [
        "deny"
    ]
}
```

When policy evaluation denials occur against the following conditions, Advanced Identity Cloud does not return any advice:

* `IPv4`

* `IPv6`

* `LDAPFilter`

* `OAuth2Scope`

* `SessionProperty`

* `SimpleTime`

When policy evaluation is requested for a nonexistent or inactive subject, Advanced Identity Cloud returns an HTTP 200 code and a response that contains no actions or advice. Access to the resource is denied.

## Request policy decisions for a tree of resources

This section shows how you can request policy decisions over REST for a resource and all other resources in the subtree beneath it.

When making a REST API call, specify the realm in the path component of the endpoint. You must specify the entire hierarchy of the realm. Prefix each realm in the hierarchy with the `realms/` keyword. For example, `/realms/root/realms/alpha`.

To request policy decisions for a tree of resources, send an HTTP POST request to the `policies` endpoint with the `evaluateTree` action; for example `/json/realms/root/realms/alpha/policies?_action=evaluateTree`. The payload for the HTTP POST is a JSON object that specifies at least the root resource and takes the following form.

```json
{
    "resource": "resource string",
    "application": "policy set that contains the policies to evaluate against",
    "subject": {
        "ssoToken": "SSO token ID string",
        "jwt": "JSON Web Token string",
        "claims": {
            "key": "value",
            ...
        }
    },
    "environment": {
        "optional key1": [
            "value",
            "another value",
            ...
        ],
        "optional key2": [
            "value",
            "another value",
            ...
        ],
        ...
    }
}
```

The values for the fields shown above are explained below:

* `resource`

  This required field specifies the root resource for the decisions to return.

  For example, depending on the patterns defined in the policy set, you could request decisions for resource URLs.

  ```json
  {
      "resource": "http://www.example.com/"
  }
  ```

* `application`

  This field holds the name of the policy set, for example, `samplePolicySet`.

  For more on policy sets, refer to [Policy sets over REST](rest-api-authz-applications.html).

* `subject`

  This optional field holds an object that represents the subject. You can specify one or more of the following keys. If you specify multiple keys, the subject can have multiple associated principals, and you can use subject conditions corresponding to any type in the request.

  * `ssoToken`

    The value is the SSO token ID string for the subject, returned for example on successful authentication as described in [Authenticate over REST](../am-authentication/authn-rest.html).

  * `jwt`

    The value is a JWT string.

  * `claims`

    The value is an object (map) of JWT claims to their values. If you do not specify the subject, Advanced Identity Cloud uses the SSO token ID of the subject making the request.

* `environment`

  This optional field holds a map of keys to lists of values.

  If you do not specify the environment, the default is an empty map.

The example below requests policy decisions for `http://www.example.com/`. The `<session-cookie-name>` header sets the SSO token for a user who has access to perform the operation, and the subject takes the SSO token of the user who wants to access a resource.

```bash
$ curl \
--request POST \
--header "Content-Type: application/json" \
--header "<session-cookie-name>: AQIC5...NDU1*" \
--header "Accept-API-Version: resource=1.0" \
--data '{
    "resource": "http://www.example.com/",
    "subject": { "ssoToken": "AQIC5...zE4*" }
}' \
"https://<tenant-env-fqdn>/am/json/realms/root/realms/alpha/policies/?_action=evaluateTree"
[
    {
        "resource":"http://www.example.com/",
        "actions":{
            "GET":true,
            "OPTIONS":true,
            "HEAD":true
        },
        "attributes":{

        },
        "advices":{

        }
    },
    {
        "resource":"http://www.example.com/",
        "actions":{
            "POST":false,
            "PATCH":false,
            "GET":true,
            "DELETE":true,
            "OPTIONS":true,
            "HEAD":true,
            "PUT":true
        },
        "attributes":{
            "myStaticAttr":[
                "myStaticValue"
            ]
        },
        "advices":{

        }
    },
    {
        "resource":"http://www.example.com/?*",
        "actions":{
            "POST":false,
            "PATCH":false,
            "GET":false,
            "DELETE":false,
            "OPTIONS":true,
            "HEAD":false,
            "PUT":false
        },
        "attributes":{

        },
        "advices":{
            "AuthLevelConditionAdvice":[
                "3"
            ]
        }
    }
]
```

Advanced Identity Cloud returns decisions not only for the specified resource, but also for matching resource names in the tree whose root is the specified resource.

In the JSON list of decisions returned for each resource, Advanced Identity Cloud includes these fields:

* `resource`

  A resource name whose root is the resource specified in the request.

  The decisions returned are not guaranteed to be in the same order as the resources were requested.

* `actions`

  A map of action name keys to Boolean values that indicate whether the action is allowed (`true`) or denied (`false`) for the specified resource.

  In the example, for matching resources with a query string only HTTP OPTIONS is allowed according to the policies configured.

* `attributes`

  A map of attribute names to their values if any response attributes are returned according to applicable policies.

  In the example, the policy that applies to `http://www.example.com:80/*` causes a static attribute to be returned.

* `advices`

  A map of advice names to their values if any advice is returned according to applicable policies.

  The `advices` field can provide hints regarding what Advanced Identity Cloud needs to take the authorization decision.

  In the example, the policy that applies to resources with a query string requests that the subject authenticates at an authentication level of at least 3.

  Notice that with the `advices` field present, no `advices` appear in the JSON response.

  ```json
  {
      "advices": {
          "AuthLevelConditionAdvice": [ "3" ]
      }
  }
  ```

You can use the query string parameters `_prettyPrint=true` to make the output easier to read, and `_fields=field-name[,field-name...]` to limit the fields returned in the output.

---

---
title: Resource types
description: Define templates for resources and actions that policies use to protect access to applications
component: pingoneaic
page_id: pingoneaic:am-authorization:configuring-resource-types
canonical_url: https://docs.pingidentity.com/pingoneaic/am-authorization/configuring-resource-types.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Authorization", "Policy", "Resource"]
page_aliases: ["authorization-guide:configuring-resource-types.adoc"]
section_ids:
  default-resource-types: Default resource types
---

# Resource types

Resource types define a template for the resources that policies apply to, and the actions that can be performed on those resources.

Advanced Identity Cloud needs a *policy* to decide whether a user can access a resource. When you configure a policy, you also configure a resource (or a pattern to match several resources) that the policy applies to, and the actions that the policy allows or denies.

Resource types are templates that you can define once and reuse in several policies. For example, you could create a template that always allows PUT and POST operations from your internal network.

## Default resource types

Advanced Identity Cloud includes the following resource types by default:

* `Authentication`

  The `Authentication` resource type supports the identification of applications during the authentication journey using unique identifiers like client IDs (for OAuth 2.0 or OIDC) or entity IDs (for SAML 2.0). It contains a single wildcard pattern, `*`.

  This resource type supports the `Access` action, which can be allowed or denied.

* `OAuth2 Scope`

  The `OAuth2 Scope` resource type acts as a template for granting or denying OAuth 2.0 scopes. It contains a string-based scope pattern, `*`, and two URL-based scope patterns, such as `*://*:*/*?*`.

  The resource supports the `GRANT` action, which can be allowed or denied.

* `URL`

  The `URL` resource type acts as a template for protecting web pages or applications. It contains resource patterns, such as `*://*:*/*?*`, that can be more specific when used in the policy.

  This resource type supports the following actions:

  GET\
  POST\
  PUT\
  HEAD\
  PATCH\
  DELETE\
  OPTIONS

  For example, an application for Example.com's HR service might contain resource types that constrain all policies to apply to URL resource types under `http*://example.com/hr*` and `http*://example.com/hr*?*`, and only allow HTTP `GET` and `POST` actions.

---

---
title: Resource types in the UI
description: Define resource type patterns and actions with wildcard matching for policy evaluation
component: pingoneaic
page_id: pingoneaic:am-authorization:resource-types-ui
canonical_url: https://docs.pingidentity.com/pingoneaic/am-authorization/resource-types-ui.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Authorization", "Policy", "Resource", "Configuration"]
page_aliases: ["authorization-guide:resource-types-ui.adoc"]
section_ids:
  resource_type_names: Resource type names
  policy-patterns-wildcards: Resource type patterns
  wildcards: Wildcards
  wildcards_in_schemes_hosts_and_port_numbers: Wildcards in schemes, hosts, and port numbers
  wildcards_in_paths: Wildcards in paths
  wildcards_in_query_strings: Wildcards in query strings
  non_ascii_characters: Non-ASCII characters
  resource_type_actions: Resource type actions
  resource-types-console: Example
---

# Resource types in the UI

You manage resource types under Native Consoles > Access Management > Realms > *Realm Name* > Authorization > Resource Types.

| To...                  | Action                                                                                                                                                                                               |
| ---------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Create a resource type | Click New Resource Type.When creating a resource type, specify at least one action and one pattern.                                                                                                  |
| Modify a resource type | Click the resource type name or the pencil icon ([icon: pencil-alt, set=fa]).                                                                                                                        |
| Delete a resource type | Click the delete icon ([icon: times, set=fa]) or click the resource type name then the x Delete button.You can't delete a resource type if any policies or policy sets depend on that resource type. |

## Resource type names

Don't use any of the following characters in policy, policy set, or resource type names:

* Double quotes (`"`)

* Plus sign (`+`)

* Comma (`,`)

* Less than (`<`)

* Equals (`=`)

* Greater than (`>`)

* Backslash (`\`)

* Forward slash (`/`)

* Semicolon (`;`)

* Null (`\u0000`)

## Resource type patterns

Policies apply to resources that match their patterns.

* A policy belongs to a policy set.

* A policy set permits one or more resource types in their policies.

* A policy can only define patterns that fit the patterns of its resource types.

### Wildcards

Resource type patterns can include a mix of literal characters and wildcards, `*` or `-*-`. Wildcards can appear anywhere in a resource type pattern to match resources, such as URLs or OAuth 2.0 scopes.

* Do not mix `*` and `-*-` in the same pattern.

* Wildcards cannot be escaped.

* Comparisons are not case-sensitive.

### Wildcards in schemes, hosts, and port numbers

When using wildcards for the scheme and authority parts of a URL:

* The pattern `*://*:*/*` matches these URLs:

  `http://www.example.com:80/index.html`\
  `https://www.example.com:443/index.html`\
  `http://www.example.net:8080/index.html`

* Omitting the port number implies the default port number for the scheme:

  `http://www.example.com/*` is the same as `http://www.example.com:80/*`.

  `https://www.example.com/*` is the same as `https://www.example.com:443/*`.

### Wildcards in paths

Wildcards have these properties in a URL path:

* The wildcard `*` matches *multiple* path segments.

  For example, `https://www.example.com/*` matches `https://www.example.com/`, `https://www.example.com/index.html`, and `https://www.example.com/company/images/logo.png`.

* The wildcard `-*-` matches *a single* path segment.

  For example, `https://www.example.com/-*-` matches `https://www.example.com/index.html`.

  It does not match `https://www.example.com/company/resource.html` or `https://www.example.com/company/images/logo.png`.

* Duplicate slashes (`//`) count as a single slash.

  `http://www.example.com//path/` and `http://www.example.com/path//` are equivalent.

* A trailing slash counts as a distinct part of the resource to match.

  `https://www.example.com/path` and `https://www.example.com/path/` are not equivalent.

### Wildcards in query strings

Wildcards do not match `?`.

Add explicit patterns to match URLs with query strings:

* When matching URLs protected by a web or Java agent, an asterisk (`*`) at the end of a pattern after `?` matches *one or more* characters, not zero or more characters.

  For example, `https://www.example.com/*?*` matches `https://www.example.com/users?_action=create`, not `https://www.example.com/users?`.

  To match all URLs under `https://www.example.com/`, specify three patterns:

  `https://www.example.com/*`\
  `https://www.example.com/*?`\
  `https://www.example.com/*?*`

* When matching resources with a `policies?_action=evaluate` REST call, an asterisk (`*`) at the end of a pattern after `?` matches *zero or more* characters.

  For example, `https://www.example.com/*?*` matches `https://www.example.com/users?_action=create` and `https://www.example.com/users?`.

  To match all URLs under `http://www.example.com/`, specify two patterns:

  `https://www.example.com/*`\
  `https://www.example.com/*?*`

* Advanced Identity Cloud normalizes query strings before checking whether a policy matches a resource.

  To normalize the query string, Advanced Identity Cloud sorts the query string field-value pairs alphabetically by field name. These query strings are equivalent:

  `?subject=SPBnfm+t5PlP+ISyQhVlplE22A8=&action=get`\
  `?action=get&subject=SPBnfm+t5PlP+ISyQhVlplE22A8=`

### Non-ASCII characters

Use percent-encoding for non-ASCII characters in resource patterns.

For example, to match resources under the Internationalized Resource Identifier (IRI) `https://www.example.com/forstå/` use:

`https://www.example.com:443/forst%C3%A5/*`\
`https://www.example.com:443/forst%C3%A5/*?*`

## Resource type actions

Advanced Identity Cloud policies use actions to grant or deny access to a resource. A policy can only determine actions defined by its resource types.

Choose a name that summarizes the action the principal aims to perform on the resource. The default state for each action is either Allow or Deny.

## Example

The following screen creates a resource type for policies to switch lights on and off:

![Add the patterns and actions that policies using this resource type can make use of.](_images/resource-types-console.png)Figure 1. Configuring a resource type in the UI

---

---
title: Resource types over REST
description: Manage resource types over REST to define templates for policy resources and allowed actions
component: pingoneaic
page_id: pingoneaic:am-authorization:rest-api-authz-resource-types
canonical_url: https://docs.pingidentity.com/pingoneaic/am-authorization/rest-api-authz-resource-types.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Authorization", "Policy", "Resource", "REST API", "Configuration"]
page_aliases: ["authorization-guide:rest-api-authz-resource-types.adoc"]
section_ids:
  access_the_endpoints: Access the endpoints
  rest-api-authz-resource-types-query: Query resource types
  rest-api-authz-resource-types-read: Read a resource type
  rest-api-authz-resource-types-create: Create a resource type
  rest-api-authz-resource-types-update: Update a resource type
  rest-api-authz-resource-types-delete: Delete a resource type
---

# Resource types over REST

You can manage resource types over REST at the `resourcetypes` endpoint.

Advanced Identity Cloud stores resource types as JSON objects. A resource type can include the following fields. The fields have JSON values—​strings, numbers, objects, sets, arrays, `true`, `false`, and `null`.

| Resource type field   | Description                                                                                                                                                                                                                                                                                                                                 |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `_id`, `uuid`(1)      | A unique, system-generated UUID string.Use this string to identify a specific resource type. Do not change the generated UUID.                                                                                                                                                                                                              |
| `_rev`(1)             | A system-generated revision string.                                                                                                                                                                                                                                                                                                         |
| `name`                | A human-readable name string for the resource type.Don't use any of the following characters in policy, policy set, or resource type names:- Double quotes (`"`)

- Plus sign (`+`)

- Comma (`,`)

- Less than (`<`)

- Equals (`=`)

- Greater than (`>`)

- Backslash (`\`)

- Forward slash (`/`)

- Semicolon (`;`)

- Null (`\u0000`) |
| `description`         | An optional text string to help identify the resource type.                                                                                                                                                                                                                                                                                 |
| `patterns`            | An array of resource pattern strings specifying URLs or resource names to protect.For details, refer to [Resource type patterns](resource-types-ui.html#policy-patterns-wildcards).                                                                                                                                                         |
| `actions`             | An object where each field is an action name.The value for each action name field is a boolean indicating whether to allow the action by default in policies that derive from this resource type.                                                                                                                                           |
| `createdBy`(1)        | A string indicating who created the resource type.                                                                                                                                                                                                                                                                                          |
| `creationDate`(1)     | An integer containing the creation time in milliseconds since January 1, 1970.                                                                                                                                                                                                                                                              |
| `lastModifiedBy`(1)   | A string indicating who last changed the resource type.                                                                                                                                                                                                                                                                                     |
| `lastModifiedDate`(1) | An integer containing the last modified time in milliseconds since January 1, 1970.                                                                                                                                                                                                                                                         |

(1) Do not change the value of this field.

## Access the endpoints

The REST calls to manage resource types rely on an account with the appropriate privileges:

1. Create a resource type administrator.

   In the Advanced Identity Cloud admin console, select Identities > Manage > *Realm Name* Realm - Users > + New *Realm Name* Realm - User and fill the required fields.

   Record the username and password.

2. Create a group that grants the privileges to the resource type administrator.

   Under Native Consoles > Access Management, select Realms > *Realm Name* > Identities > Groups > + Add Group to create a group with the following settings:

   * Group ID

     `am-resource-type-admins`

   * Members

     The resource type administrator whose username you recorded

   * Privileges

     Policy Admin\
     Resource Type Modify Access\
     Resource Type Read Access

3. Before making REST calls to manage resource types, authenticate as the resource type administrator:

   ```bash
   $ curl \
   --request POST \
   --header 'Content-Type: application/json' \
   --header 'X-OpenAM-Username: <resource-type-admin-username>' \
   --header 'X-OpenAM-Password: <resource-type-admin-password>' \
   --header 'Accept-API-Version: resource=2.0, protocol=1.0' \
   'https://<tenant-env-fqdn>/am/json/realms/root/realms/alpha/authenticate'
   {
     "tokenId": "<resource-type-admin-tokenId>",
     "successUrl": "/enduser/?realm=/alpha",
     "realm": "/alpha"
   }
   ```

   For additional details, refer to [Session tokens after authentication](../am-authentication/rest-using-ssotokens.html).

   Use the `<resource-type-admin-tokenId>` as the value of the `<session-cookie-name>` header to access the REST endpoints.

## Query resource types

To list all the resource types defined for a realm, send an HTTP GET request to the `/json/realms/root/realms/Realm Name/resourcetypes` endpoint with `_queryFilter=true` as the query string parameter.

```bash
$ curl \
--header "<session-cookie-name>: <resource-type-admin-tokenId>" \
--header "Accept-API-Version: resource=1.0" \
'https://<tenant-env-fqdn>/am/json/realms/root/realms/alpha/resourcetypes?_queryFilter=true'
[{
  "result": [{
    "_id": "fcaee7dc-f99c-43b1-b10d-592e1c4bd394",
    "uuid": "fcaee7dc-f99c-43b1-b10d-592e1c4bd394",
    "name": "Light",
    "description": "",
    "patterns": ["light://*/*"],
    "actions": {
      "switch_off": false,
      "switch_on": false
    },
    "createdBy": "id=a980a458-2654-4d4f-a12a-d4bfa39534f7,ou=user,ou=am-config",
    "creationDate": 1669038769034,
    "lastModifiedBy": "id=a980a458-2654-4d4f-a12a-d4bfa39534f7,ou=user,ou=am-config",
    "lastModifiedDate": 1669038769034
  }, {
    "_id": "76656a38-5f8e-401b-83aa-4ccb74ce88d2",
    "uuid": "76656a38-5f8e-401b-83aa-4ccb74ce88d2",
    "name": "URL..."
  }, {
    "_id": "d60b7a71-1dc6-44a5-8e48-e4b9d92dee8b",
    "uuid": "d60b7a71-1dc6-44a5-8e48-e4b9d92dee8b",
    "name": "OAuth2 Scope..."
  }],
  "resultCount": 3,
  "pagedResultsCookie": null,
  "totalPagedResultsPolicy": "NONE",
  "totalPagedResults": -1,
  "remainingPagedResults": 0
}
```

Adapt the [query string parameters](../developer-docs/crest/query.html) to refine the results.

| Field         | Supported `_queryFilter` operators               |
| ------------- | ------------------------------------------------ |
| `uuid`        | Equals (`eq`) Contains (`co`) Starts with (`sw`) |
| `name`        |                                                  |
| `description` |                                                  |
| `patterns`    |                                                  |
| `actions`     |                                                  |

## Read a resource type

To read a resource type in a realm, send an HTTP GET request to the `/json/realms/root/realms/Realm Name/resourcetypes/uuid` endpoint, where *uuid* is the value of the `"uuid"` field for the resource.

```bash
$ curl \
--header "<session-cookie-name>: <resource-type-admin-tokenId>" \
--header "Accept-API-Version: resource=1.0" \
'https://<tenant-env-fqdn>/am/json/realms/root/realms/alpha/resourcetypes/fcaee7dc-f99c-43b1-b10d-592e1c4bd394'
{
  "_id": "fcaee7dc-f99c-43b1-b10d-592e1c4bd394",
  "_rev": "1669045336245",
  "uuid": "fcaee7dc-f99c-43b1-b10d-592e1c4bd394",
  "name": "Light",
  "description": "",
  "patterns": ["light://*/*"],
  "actions": {
    "switch_off": false,
    "switch_on": false
  },
  "createdBy": "id=a980a458-2654-4d4f-a12a-d4bfa39534f7,ou=user,ou=am-config",
  "creationDate": 1669038769034,
  "lastModifiedBy": "id=a980a458-2654-4d4f-a12a-d4bfa39534f7,ou=user,ou=am-config",
  "lastModifiedDate": 1669038769034
}
```

## Create a resource type

To create a resource type in a realm, send an HTTP POST request to the `/json/realms/root/realms/Realm Name/resourcetypes` endpoint with `_action=create` as the query string parameter and a JSON representation of the resource type as the POST data.

Advanced Identity Cloud generates the UUID for the resource.

```bash
$ curl \
--request POST \
--header "Content-Type: application/json" \
--header "<session-cookie-name>: <resource-type-admin-tokenId>" \
--header "Accept-API-Version: resource=1.0" \
--data '{
  "name": "My Resource Type",
  "actions": {
    "LEFT": true,
    "RIGHT": true,
    "UP": true,
    "DOWN": true
  },
  "patterns": ["https://device/location/*"]
}' \
'https://<tenant-env-fqdn>/am/json/realms/root/realms/alpha/resourcetypes/?_action=create'
{
  "_id": "c7e09ca1-a0db-4434-9327-ca685ae99899",
  "uuid": "c7e09ca1-a0db-4434-9327-ca685ae99899",
  "name": "My Resource Type",
  "description": null,
  "patterns": ["https://device/location/*"],
  "actions": {
    "RIGHT": true,
    "DOWN": true,
    "UP": true,
    "LEFT": true
  },
  "createdBy": "id=1dff18dc-ac57-4388-8127-dff309f80002,ou=user,o=alpha,ou=services,ou=am-config",
  "creationDate": 1669045619375,
  "lastModifiedBy": "id=1dff18dc-ac57-4388-8127-dff309f80002,ou=user,o=alpha,ou=services,ou=am-config",
  "lastModifiedDate": 1669045619375
}
```

## Update a resource type

To update a resource type in a realm, send an HTTP PUT request to the `/json/realms/root/realms/Realm Name/resourcetypes/uuid` endpoint, where *uuid* is the value of the `"uuid"` field for the resource. Include a JSON representation of the resource type as the PUT body, making sure the `"uuid"` and `"_id"` fields match the original resource.

```bash
$ curl \
--request PUT \
--header "Content-Type: application/json" \
--header "<session-cookie-name>: <resource-type-admin-tokenId>" \
--header "Accept-API-Version: resource=1.0" \
--data '{
  "name": "My Resource Type",
  "actions": {
    "LEFT": true,
    "RIGHT": true,
    "UP": false,
    "DOWN": false
  },
  "patterns": ["https://device/location/*"]
}' \
'https://<tenant-env-fqdn>/am/json/realms/root/realms/alpha/resourcetypes/c7e09ca1-a0db-4434-9327-ca685ae99899'
{
  "_id": "c7e09ca1-a0db-4434-9327-ca685ae99899",
  "uuid": "c7e09ca1-a0db-4434-9327-ca685ae99899",
  "name": "My Resource Type",
  "description": null,
  "patterns": ["https://device/location/*"],
  "actions": {
    "RIGHT": true,
    "DOWN": false,
    "UP": false,
    "LEFT": true
  },
  "createdBy": "id=1dff18dc-ac57-4388-8127-dff309f80002,ou=user,o=alpha,ou=services,ou=am-config",
  "creationDate": 1669045619375,
  "lastModifiedBy": "id=1dff18dc-ac57-4388-8127-dff309f80002,ou=user,o=alpha,ou=services,ou=am-config",
  "lastModifiedDate": 1669045765822
}
```

## Delete a resource type

To delete a resource type from a realm, send an HTTP DELETE request to the `/json/realms/root/realms/Realm Name/resourcetypes/uuid` endpoint, where *uuid* is the value of the `"uuid"` field for the resource.

```bash
$ curl \
--request DELETE \
--header "<session-cookie-name>: <resource-type-admin-tokenId>" \
--header "Accept-API-Version: resource=1.0" \
'https://<tenant-env-fqdn>/am/json/realms/root/realms/alpha/resourcetypes/c7e09ca1-a0db-4434-9327-ca685ae99899'
{"_id":"c7e09ca1-a0db-4434-9327-ca685ae99899","_rev":"0"}
```

You can't delete a resource type if a policy set or policy depends on it. If you attempt to delete a resource type that is in use, Advanced Identity Cloud returns an HTTP 409 Conflict status code and a message like the one in the following example:

```bash
$ curl \
--request DELETE \
--header "<session-cookie-name>: <resource-type-admin-tokenId>" \
--header "Accept-API-Version: resource=1.0" \
'https://<tenant-env-fqdn>/am/json/realms/root/realms/alpha/resourcetypes/76656a38-5f8e-401b-83aa-4ccb74ce88d2'
{
  "code": 409,
  "reason": "Conflict",
  "message": "Unable to remove resource type 76656a38-5f8e-401b-83aa-4ccb74ce88d2 because it is referenced in the policy model."
}
```

Remove the dependency on the resource type from all policy sets and policies before you delete it.

---

---
title: Scripted policy conditions
description: Use JavaScript scripts as environment conditions to customize authorization policy evaluation
component: pingoneaic
page_id: pingoneaic:am-authorization:scripted-policy-condition
canonical_url: https://docs.pingidentity.com/pingoneaic/am-authorization/scripted-policy-condition.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Authorization", "Policy", "Administration", "Scripting", "Evaluation"]
page_aliases: ["authorization-guide:scripted-policy-condition.adoc"]
section_ids:
  sec-scripted-policy-condition-prepare: Prepare a demonstration
  scripted-policy-privilege: Policy administrator account
  scripted-policy-enduser: End user account
  scripted-policy-script: Create a script
  scripted-policy-policy: Create a policy
  scripted-policy-condition-evaluate: Try the demonstration
  scripting-api-oauth2-policy: Scripted OAuth 2.0 scopes policy conditions
---

# Scripted policy conditions

You can use scripts to tailor the actions Advanced Identity Cloud takes as part of policy evaluation.

This example uses a next-generation policy condition script.

Find information about the available bindings for legacy and next-generation policy condition scripts in the [Policy condition script API](../am-scripting/policy-condition-scripting-api.html).

## Prepare a demonstration

To demonstrate an example policy condition script:

* [Create a policy administrator user](#scripted-policy-privilege).

* [Create an end user](#scripted-policy-enduser).

* [Create a policy condition script](#scripted-policy-script)

* [Create a policy that uses the script](#scripted-policy-policy).

### Policy administrator account

This account represents the policy enforcement point (PEP) account. It has the Entitlement Rest Access privilege required to request Advanced Identity Cloud policy decisions over HTTP using the REST API. In a production environment, use a PEP like PingGateway or a web or Java agent in this role.

1. Create a policy administrator.

   In the Advanced Identity Cloud admin console, select Identities > Manage > + New Alpha Realm - User and fill the required fields.

   Record the username and password.

2. Create a group that grants the Entitlement Rest Access privilege to the policy administrator.

   Under Native Consoles > Access Management, select Realms > alpha > Identities > Groups > + Add Group to create a group with the following settings:

   * Group ID

     `am-policy-evaluation`

   * Members

     The policy administrator whose username you recorded

   * Privileges

     Entitlement Rest Access

### End user account

This account represents the end user who tries to access online resources.

1. Create a user.

   In the Advanced Identity Cloud admin console, select Identities > Manage > + New Alpha Realm - User and fill the required fields.

   Record the username and password.

2. In the Home Address field of the user profile, enter `United States`.

### Create a script

1. Under Native Consoles > Access Management, go to Realms > alpha > Scripts and click +New Script.

2. Create your script with the following values:

   * Name

     `Location Authorization Script`

   * Script Type

     `Policy Condition`

   * Evaluator Version

     `Next Generation`

3. In the Script field, paste the following JavaScript:

   > **Collapse: Next-generation policy condition example script**
   >
   > ```javascript
   > var userAddress, userIP, resourceHost;
   >
   > if (validateAndInitializeParameters()) {
   >     var countryFromUserIP = getCountryFromUserIP();
   >     logger.info("Country retrieved from user's IP: " + countryFromUserIP);
   >     var countryFromResourceURI = getCountryFromResourceURI();
   >     logger.info("Country retrieved from resource URI: " + countryFromResourceURI);
   >     if (userAddress === countryFromUserIP && userAddress === countryFromResourceURI) {
   >         logger.info("Authorization succeeded");
   >         responseAttributes.put("countryOfOrigin", [countryFromUserIP]);
   >         authorized = true;
   >     } else {
   >         logger.info("Authorization failed");
   >         authorized = false;
   >     }
   > } else {
   >     logger.error("Required parameters not found. Authorization failed.");
   >     authorized = false;
   > }
   > function getCountryFromUserIP() {
   >     var options = {
   >         method: "GET",
   >         headers: {
   >             "Content-Type": "application/json"
   >         }
   >     };
   >     var requestURL = "http://ip-api.com/json/" + userIP;
   >     var response = httpClient.send(requestURL, options).get();
   >     if (response.status === 200) {
   >         var result = JSON.parse(response.text());
   >         if (result) {
   >             return result.country;
   >         }
   >     } else {
   >         logger.error("Error generating IP location: " + response.statusText);
   >     }
   > }
   > function getCountryFromResourceURI() {
   >     var options = {
   >         method: "GET",
   >         headers: {
   >             "Content-Type": "application/json"
   >         }
   >     };
   >     var requestURL = "http://ip-api.com/json/" + resourceHost;
   >     var response = httpClient.send(requestURL, options).get();
   >     if (response.status === 200) {
   >         var result = JSON.parse(response.text());
   >         if (result) {
   >             return result.country;
   >         }
   >     } else {
   >         logger.error("Error generating IP location: " + response.statusText);
   >     }
   > }
   > function validateAndInitializeParameters() {
   >     var userAddressList = identity.getAttributeValues("postalAddress");
   >     if (userAddressList == null || userAddressList.isEmpty()) {
   >         logger.error("No address specified for user: " + username);
   >         return false;
   >     }
   >     userAddress = userAddressList[0];
   >     if (!environment) {
   >         logger.error("No environment parameters specified in the evaluation request.");
   >         return false;
   >     }
   >     var ipList = environment.get("IP");
   >     if (ipList == null || ipList.length == 0) {
   >         logger.error("No IP specified in the evaluation request environment parameters.");
   >         return false;
   >     }
   >     userIP = ipList[0];
   >     if (!resourceURI) {
   >         logger.error("No resource URI specified.");
   >         return false;
   >     }
   >     resourceHost = resourceURI.match(/^(.*:\/\/)(www\.)?([A-Za-z0-9\-\.]+)(:[0-9]+)?(.*)$/)[3];
   >     return true;
   > }
   > ```

4. Save your changes.

### Create a policy

The policy references the script through environmental conditions.

1. Create a policy set for policies regarding URLs.

   Under Native Consoles > Access Management, go to Realms > alpha > Authorization > Policy Sets > + New Policy Set to create a policy set with the following settings:

   * Id

     `am-policy-set`

   * Resource Types

     `URL`

2. Create a policy in the policy set.

   Click + Add a Policy to create a policy with the following settings:

   * Name

     `Scripted policy example`

   * Resource Types

     `URL`

   * Resources

     `*://*:*/*`, `*://*:*/*?*`

3. In the new policy, update the settings.

   Allow HTTP GET access by all authenticated users when permitted by the script:

   * Actions

     GET: Allow

   * Subjects

     Type: `Authenticated Users`

   * Environments

     Type: `Script`, Script Name: `Location Authorization Script`

   When modifying settings in the policy editor, select the edit icon [icon: pencil-alt, set=fa]to begin changing the setting, the check icon [icon: check, set=fa]to confirm the change, then Save Changes to commit the change.

4. Verify the policy settings.

   ![Policy settings for the Scripted policy example](_images/scripted-policy-example.png)

## Try the demonstration

The `policies?_action=evaluate` endpoint lets a policy administrator make a REST call over HTTP to get a policy decision from Advanced Identity Cloud. Policy decisions for URL policies show at least the HTTP actions the user can perform. Find more information in [Request policy decisions over REST](rest-api-authz-policy-decisions.html).

Here, when Advanced Identity Cloud grants the user access to complete an HTTP GET request to the resource, the decision includes `"actions":{"GET":true}`. When Advanced Identity Cloud denies access, the decision includes `"actions":{}`.

The REST call to the `policies?_action=evaluate` endpoint requires:

* An SSO token ID for the policy administrator making the request.

* An SSO token ID for the end user attempting to access the resource.

* A request body that specifies who is attempting to access what in what way under what conditions.

  1. Get an SSO token for the policy administrator:

     ```bash
     $ curl \
     --request POST \
     --header 'Content-Type: application/json' \
     --header 'X-OpenAM-Username: policy-admin-username' \
     --header 'X-OpenAM-Password: policy-admin-password' \
     --header 'Accept-API-Version: resource=2.0, protocol=1.0' \
     'https://<tenant-env-fqdn>/am/json/realms/root/realms/alpha/authenticate'
     {
       "tokenId":"policy-admin-tokenId",
       "successUrl": "/am/console",
       "realm": "/alpha"
     }
     ```

  2. Obtain an SSO token for the end user:

     ```bash
     $ curl \
     --request POST \
     --header 'Content-Type: application/json' \
     --header 'X-OpenAM-Username: end-user-username' \
     --header 'X-OpenAM-Password: end-user-password' \
     --header 'Accept-API-Version: resource=2.0, protocol=1.0' \
     'https://<tenant-env-fqdn>/am/json/realms/root/realms/alpha/authenticate'
     {
       "tokenId":"end-user-tokenId",
       "successUrl": "/am/console",
       "realm": "/alpha"
     }
     ```

  3. Request evaluation for a request by an end user in the United States to access a resource located in the United States.

     The script lets users access resources located in their country of residence. PingOne Advanced Identity Cloud grants access when both the user's home country and IP address match the resource location.

     ```bash
     $ curl \
     --header '<session-cookie-name>: policy-admin-tokenId' \
     --request POST \
     --header 'Content-Type: application/json' \
     --header "Accept-API-Version: resource=2.1" \
     --data '{
       "resources": ["https://www.whitehouse.gov:443/about-the-white-house/"],
       "actions": {"GET": true},
       "application": "am-policy-set",
       "subject": {
           "ssoToken": "end-user-tokenId"
       },
       "environment": {
         "IP": ["8.8.8.8"]
       }
     }' \
     'https://<tenant-env-fqdn>/am/json/realms/root/realms/alpha/policies?_action=evaluate'
     [{
       "resource": "https://www.whitehouse.gov:443/about-the-white-house/",
       "actions": {
         "GET": true
       },
       "attributes": {
         "countryOfOrigin": ["United States"]
       },
       "advices": {},
       "ttl": <ttl>
     }]
     ```

     The script adds `"attributes":{"countryOfOrigin": ["United States"]}` to the result when Advanced Identity Cloud grants access.

  4. Request evaluation for a request by an end user in France to access a resource located in the United States.

     The user's IP address (`88.174.153.24`) maps to a French location, so no actions are returned:

     ```bash
     $ curl \
     --header '<session-cookie-name>: policy-admin-tokenId' \
     --request POST \
     --header 'Content-Type: application/json' \
     --header "Accept-API-Version: resource=2.1" \
     --data '{
       "resources": ["https://www.whitehouse.gov:443/about-the-white-house/"],
       "actions": {"GET": true},
       "application": "am-policy-set",
       "subject": {
         "ssoToken": "end-user-tokenId"
       },
       "environment": {
         "IP": ["88.174.153.24"]
       }
     }' \
     'https://<tenant-env-fqdn>/am/json/realms/root/realms/alpha/policies?_action=evaluate'
     [{
       "resource": "https://www.whitehouse.gov:443/about-the-white-house/",
       "actions": {},
       "attributes": {},
       "advices": {},
       "ttl": <ttl>
     }]
     ```

     The response returns both `attributes` and the `actions` as empty fields. To verify the authorization outcome, look for an `Authorization failed` entry in the logs.

## Scripted OAuth 2.0 scopes policy conditions

To customize OAuth 2.0 scope decisions, configure the `oauth2Scopes` policy with an [environment script condition](policies-ui.html#environments) that references an OAuth 2.0 policy condition script.

The following JavaScript writes the ID of the OAuth 2.0 client to the debug log and then authorizes the request:

```javascript
logger.message("Client ID: " + environment.get("clientId"));
authorized=true;
```

OAuth 2.0 policy condition scripts can access the bindings available to the [Policy condition script API](../am-scripting/policy-condition-scripting-api.html), except for the `environment` object. Instead of an IP property, this object returns the ID for the client making the authorization request.

For example, the following shows an `environment` map with a single entry:

```none
"environment": {
    "clientId": [
        "MyOAuth2Client"
    ]
}
```