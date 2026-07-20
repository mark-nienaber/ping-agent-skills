---
title: Account lockout
description: Lock user accounts after repeated failed login attempts to defend against brute-force attacks
component: pingoneaic
page_id: pingoneaic:am-authentication:account-lockout
canonical_url: https://docs.pingidentity.com/pingoneaic/am-authentication/account-lockout.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  configure-account-lockout: Configure account lockout
  success-and-failure-nodes: Success and Failure nodes
  success-node: Success node
  failure-node: Failure node
  lockout_specific_nodes: Lockout-specific nodes
---

# Account lockout

Account lockout is a security mechanism that locks a user account after repeated failed login attempts. It is used to slow down brute-force attacks and compensate for weak password policies.

You can configure account lockout in one of the following ways:

* Persistent lockout

  Persistent (physical) lockout locks the user account indefinitely. A tenant administrator can release the lock by setting the account status to active.

  For persistent lockout, Advanced Identity Cloud sets the user account status to inactive. This makes it easy for a tenant administrator to search for user accounts with a persistent lockout set. It also means that if you synchronize your user accounts from Advanced Identity Cloud to another datastore, you can track locked accounts in the downstream datastore.

  This is the default type of account lockout and Ping Identity recommends it as the best way to mitigate brute force attacks.

* Duration lockout

  Duration lockout locks the user account for a specified duration. The lock is automatically released after the specified duration.

  Unlike persistent lockout, the user account status remains active. Instead, Advanced Identity Cloud tracks the locked state internally. This makes it harder for a tenant administrator to search for user accounts with a duration lockout set. It also means that if you synchronize your user accounts from Advanced Identity Cloud to another datastore, you cannot track locked accounts in the downstream datastore. However, it is possible to configure the Invalid Attempts Data Attribute Name to persist metadata about failed authentication attempts to a specified user account attribute — refer to [Configure account lockout](#configure-account-lockout).

|   |                                                                                                                                                                      |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Failed login attempts during the [transactional authorization](../am-authorization/transactional-authorization.html) flow do not increment account lockout counters. |

## Configure account lockout

1. In the Advanced Identity Cloud admin console, select Native Consoles > Access Management.

2. Go to Realms > *Realm Name* > Authentication > Settings > Account Lockout.

3. Enable lockout by checking Login Failure Lockout Mode, then set the number of attempts and the lockout interval. You can also opt to warn users after several consecutive failures.

4. To configure persistent lockout:

   1. Set Login Failure Lockout Duration to 0.

   2. Check Store Invalid Attempts in Data Store.

5. To configure duration lockout:

   1. Set Login Failure Lockout Duration to a positive integer value representing number of minutes. Set a value of at least 15. Optionally, configure a multipier to increase the lockout duration on each successive lockout.

   2. Check Store Invalid Attempts in Data Store.

   3. Set Invalid Attempts Data Attribute Name to `sunAMAuthInvalidAttemptsData`. Alternatively, to persist invalid attempts metadata to the user account, set Invalid Attempts Data Attribute Name to a valid attribute; for example, `fr-attr-istr1`. For a list of valid attributes, refer to the [User identity attributes and properties reference](../identities/user-identity-properties-attributes-reference.html).

6. Click Save Changes.

## Success and Failure nodes

If you enable account lockout in a realm, the Success and Failure nodes play a key role in modifying journey behavior. The Success node resets the number of invalid attempts to zero. The Failure node increments the number of invalid attempts and triggers Warn User After N Failures messages.

### Success node

This node does the following:

* Checks the Status property of the user profile, when reached. If the account is marked as `Inactive`, the node fails the authentication with an error message:

  ![Account locked error when reaching Success node.](_images/trees-error-lockout.png)

  The error message is returned in the JSON response if authenticating to the journey over REST:

  ```json
  {
      "code":401,
      "reason":"Unauthorized",
      "message":"User Locked Out.",
      "detail":
      {
          "failureUrl":""
      }
  }
  ```

* If the User Status property is set to `Active`, the node resets the failure count in the user profile, when reached.

### Failure node

This node does the following:

* If you select Authentication > Settings > Account Lockout > Login Failure Lockout Mode for the realm (under Native Consoles > Access Management), the node checks the invalid attempts property of the user profile. It returns a warning message if the number of failed attempts is equal to or greater than the configured Warn User After N Failures value:

  ![Invalid attempts limit warning when reaching Failure node.](_images/trees-warning-attempts.png)

  The error message is returned in the JSON response if authenticating to the journey over REST:

  ```json
  {
      "code":401,
      "reason":"Unauthorized",
      "message":"Warning: You will be locked out after 1 more failure(s).",
      "detail":
      {
          "failureUrl":""
      }
  }
  ```

* Increments the failure count in the user profile, when reached.

* Returns an error message if the account is marked as `Inactive`:

  ![Account locked error when reaching Failure node.](_images/trees-error-lockout.png)

  The error message is returned in the JSON response if authenticating to the journey over REST:

  ```json
  {
      "code":401,
      "reason":"Unauthorized",
      "message":"User Locked Out.",
      "detail":
      {
          "failureUrl":""
      }
  }
  ```

## Lockout-specific nodes

Authentication journeys also provide lockout-specific nodes for checking and changing the status of a user:

* [Account Active Decision node](https://docs.pingidentity.com/auth-node-ref/latest/account-active-decision.html)

  Use this node to determine whether an account is considered locked or unlocked.

  * The account is considered locked under these conditions:

    * The status is `inactive`.

    * The status is `active` and a duration lockout is set on the account.

  * The account is considered unlocked under this condition:

    * The status is `active` and no duration lockout is set on the account.

* [Account Lockout node](https://docs.pingidentity.com/auth-node-ref/latest/account-lockout.html)

  Use this node to change the account's status to inactive or active.

  When setting an account to inactive, the node does not consider the realm's account lockout settings, so effectively sets a persistent lockout on the account.

  When setting an account to active, the node also resets the failed attempts and lockout duration counters.

---

---
title: Authenticate endpoints
description: Configure REST endpoint parameters for specifying authentication services, realms, and other options
component: pingoneaic
page_id: pingoneaic:am-authentication:authenticate-endpoint-parameters
canonical_url: https://docs.pingidentity.com/pingoneaic/am-authentication/authenticate-endpoint-parameters.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Authentication", "Nodes &amp; Trees", "Journeys", "REST API"]
page_aliases: ["authentication-guide:authenticate-endpoint-parameters.adoc"]
section_ids:
  jsonauthenticate: /json/authenticate
  authindextype: authIndexType
  authindexvalue: authIndexValue
  nosession: noSession
  rest-authenticate-backchannel: /json/authenticate/backchannel
  authenticatebackchannelinitialize: /authenticate/backchannel/initialize
  authenticatebackchannelinfo: /authenticate/backchannel/info
---

# Authenticate endpoints

To authenticate to Advanced Identity Cloud using REST, send an HTTP POST request to the `json/authenticate` endpoint. Specify the realm hierarchy, starting at the root; for example, `/realms/root/realms/alpha`.

## `/json/authenticate`

The following list describes the `json/authenticate` endpoint parameters:

### `authIndexType`

The `authIndexType` specifies the type of authentication the user will perform. Always use this parameter in conjunction with the `authIndexValue` to provide additional information about how the user is authenticating.

If not specified, Advanced Identity Cloud authenticates the user against the [default journey](realm-auth-config.html) configured for the realm.

The `authIndexType` can be one of the following:

* `composite_advice`

  When the `authIndexType` is `composite_advice`, the `authIndexValue` must be a URL-encoded composite advice string.

  Use the `composite_advice` type to indicate which authentication services to use when logging in a user.

  This example indicates that the user should authenticate through the `myExampleJourney`:

  ```bash
  $ curl --get \
  --request POST \
  --header "Content-Type: application/json" \
  --header 'Accept-API-Version: resource=2.0, protocol=1.0' \
  --data-urlencode 'authIndexType=composite_advice' \
  --data-urlencode 'authIndexValue=<Advices>
       <AttributeValuePair>
          <Attribute name="AuthenticateToServiceConditionAdvice"/>
          <Value>myExampleJourney</Value>
        </AttributeValuePair>
  </Advices>' \
  'https://<tenant-env-fqdn>/am/json/realms/root/realms/alpha/authenticate'
  ```

  |   |                                                                                                                        |
  | - | ---------------------------------------------------------------------------------------------------------------------- |
  |   | This `curl` command URL-encodes the XML values. The `--get` option appends them as query string parameters to the URL. |

  Possible options for `Advices` are:

  * `AuthenticateToServiceConditionAdvice`. Requires the name of an authentication journey. For example:

    ```xml
    <Advices>
      <AttributeValuePair>
        <Attribute name="AuthenticateToServiceConditionAdvice"/>
        <Value>myExampleJourney</Value>
      </AttributeValuePair>
    </Advices>
    ```

  * `AuthenticateToTreeConditionAdvice`. Also requires the name of an authentication journey. For example:

    ```xml
    <Advices>
      <AttributeValuePair>
        <Attribute name="AuthenticateToTreeConditionAdvice"/>
        <Value>PersistentCookieJourney</Value>
      </AttributeValuePair>
    </Advices>
    ```

  * `AuthenticateToRealmConditionAdvice`. Requires the name of a realm. For example:

    ```xml
    <Advices>
      <AttributeValuePair>
        <Attribute name="AuthenticateToRealmConditionAdvice"/>
        <Value>alpha</Value>
      </AttributeValuePair>
    </Advices>
    ```

  You can specify multiple advice conditions. For example:

  ```xml
  <Advices>
    <AttributeValuePair>
      <Attribute name="AuthenticateToServiceConditionAdvice"/>
      <Value>ldapService</Value>
    </AttributeValuePair>
    <AttributeValuePair>
      <Attribute name="AuthenticateToServiceConditionAdvice"/>
      <Value>Example</Value>
    </AttributeValuePair>
  </Advices>
  ```

* `resource`

  When the `authIndexType` is `resource`, the `authIndexValue` must be a URL protected by an Advanced Identity Cloud policy.

  For example, to log into Advanced Identity Cloud using a policy matching the `https://www.example.com` resource, you could use the following:

  ```bash
  $ curl \
  --request POST \
  --header 'Accept-API-Version: resource=2.0, protocol=1.0' \
  'https://<tenant-env-fqdn>/am/json/realms/root/realms/alpha/authenticate?authIndexType=resource&authIndexValue=https%3A%2F%2Fwww.example.com'
  ```

  The resource must be URL-encoded. Authentication fails if no policy matches the resource.

* `service`

  When the `authIndexType` is `service`, the `authIndexValue` is the journey Advanced Identity Cloud must use to authenticate the user.

  For example, to authenticate using the built-in `login` authentication journey, you could use the following:

  ```bash
  $ curl \
  --request POST \
  --header 'Accept-API-Version: resource=2.0, protocol=1.0' \
  'https://<tenant-env-fqdn>/am/json/realms/root/realms/alpha/authenticate?authIndexType=service&authIndexValue=Login'
  ```

  If `authIndexType=service` and no `authIndexValue` is specified, the default service is used. This is similar to no `authIndexType` being set.

  If there are several authentication services that satisfy the authentication requirements, Advanced Identity Cloud presents them as a choice callback to the user. Return the required [callbacks](login-using-rest.html#login-callbacks) to Advanced Identity Cloud to authenticate.

  Required: No.

* `transaction`

  When the `authIndexType` is `transaction`, the `authIndexValue` must be the unique ID of a transaction token.

  Learn more in [Authorize one-time access with transactional authz](../am-authorization/transactional-authorization.html).

### `authIndexValue`

This parameter sets a value for the specific `authIndexType`.

Required: Yes, when using the `authIndexType` parameter.

### `noSession`

When set to `true`, this parameter specifies that Advanced Identity Cloud shouldn't return a session when authenticating a user.

For example:

```bash
$ curl \
--request POST \
--header "Content-Type: application/json" \
--header "Accept-API-Version: resource=2.0, protocol=1.0" \
--header "X-OpenAM-Username: bjensen" \
--header "X-OpenAM-Password: Secret12!" \
'https://<tenant-env-fqdn>/am/json/realms/root/realms/alpha/authenticate?noSession=true'
{
  "successUrl": "/enduser/?realm=/alpha",
  "realm": "/alpha"
}
```

Required: No.

|   |                                                                                                                                                                                       |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | You can include a message in the success response by adding a [Set Success Details node](https://docs.pingidentity.com/auth-node-ref/latest/set-success-details.html) to the journey. |

## `/json/authenticate/backchannel`

Lets a third-party federation service initiate and monitor a [backchannel authentication](backchannel-authentication.html) flow.

### `/authenticate/backchannel/initialize`

Initiates a backchannel authentication request. This endpoint has no additional query parameters.

|   |                                                                                                                                                                                                                    |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | You must access this endpoint with an OAuth 2.0 token that has the `back_channel_authentication` scope. The token must have been granted by the same Advanced Identity Cloud tenant specified in the redirect URI. |

The request body can include the following parameters:

* `type` (string, mandatory)

  The authentication type. Currently, only `service` is supported.

* `value` (string, mandatory)

  The name of the journey to direct the user or agent to.

* `subject` (object, optional)

  The subject of the authentication:

  * `type` (string, mandatory)

    The subject type: `user` or `agent`.

  * `name` (string, mandatory)

    The subject name: their identity `_id`.

* `data` (object, optional)

  Initialization data to add to the authentication journey state, as key-value pairs. For example:

  ```json
  "username": "ce3c42e2-6f9c-4451-8590-9ee40fad3f83",
  "_id": "ce3c42e2-6f9c-4451-8590-9ee40fad3f83"
  ```

  Restricted fields: `realm` and `authLevel`.

* `allowRetry`

  * When `true` (the default behavior), the end user can retry the backchannel transaction if it fails.

  * When `false`, the backchannel authentication token goes into the `Failure` state the first time the backchannel transaction fails.

* `trackingId` (string, optional)

  A tracking ID to add to the audit logs for this authentication flow. If provided, Advanced Identity Cloud logs this ID in addition to its own audit tracking ID. This lets a federation service track the flow of backchannel authentication requests through Advanced Identity Cloud using their own tracking IDs.

  The custom tracking ID must be a string of 36 characters or less and can include only the following characters:

  `A-Z` `a-z` `0-9` `-` and `_`

> **Collapse: Example**
>
> ```bash
> $ curl \
> --request POST \
> --header "Content-Type: application/json" \
> --header "Accept-API-Version: resource=1, protocol=2.0" \
> --header "Authorization: Bearer FnpG1lU0fUooJFY-82sq3UiAnGA" \
> --data '{
>   "type": "service",
>   "value": "Login",
>   "subject": {
>     "type": "user",
>     "name": "ce3c42e2-6f9c-4451-8590-9ee40fad3f83"
>   },
>   "data": {
>     "userName": "ce3c42e2-6f9c-4451-8590-9ee40fad3f83"
>   },
>   "trackingId": "Y5tyzQi9cGVJjy2L"
> }',
> "https://<tenant-env-fqdn>/am/json/realms/root/realms/alpha/authenticate/backchannel/initialize"
> {
>   "transaction": "b3070138-cd73-4ef2-bd58-812602d7b757",
>   "redirectUri": "https://<tenant-env-fqdn>/am/UI/Login?realm=/alpha&authIndexType=transaction&authIndexValue=b3070138-cd73-4ef2-bd58-812602d7b757"
> }
> ```

### `/authenticate/backchannel/info`

Provides information on the status of a [backchannel authentication](backchannel-authentication.html) flow. This endpoint has no additional parameters.

The request body must include the following parameter:

* `transaction` (string, mandatory)

  The ID of the transaction associated with the authentication tree being queried.

> **Collapse: Example**
>
> ```bash
> $ curl \
> --request POST \
> --header "Content-Type: application/json" \
> --header "Accept-API-Version: resource=1, protocol=2.0" \
> --header "Authorization: Bearer B158QzJzokTTwhAF6DshB0XQ0Rg" \
> --data '{
>     "transaction": "b3070138-cd73-4ef2-bd58-812602d7b757"
> }' \
> "https://<tenant-env-fqdn>/am/json/realms/root/realms/alpha/authenticate/backchannel/info"
> {
>   "state": "CREATED",
>   "result": "UNKNOWN",
>   "auditTrackingIds": [
>     "82d76902-7d18-41ea-9ae6-05643b05d018-166108"
>   ],
>   "type": "service",
>   "value": "Login",
>   "subject": {
>     "type": "user",
>     "name": "bjensen"
>   }
> }
> ```

The response of a request to this endpoint includes the following properties:

* `state` (string)

  The state of the authentication journey. Possible values include:

  * `CREATED`

  * `IN_PROGRESS`

  * `COMPLETED`

* `result` (string)

  The result of the authentication. Possible values include:

  * `UNKNOWN`

  * `APPROVED`

  * `DENIED`

* `auditTrackingIds` (array)

  An array of IDs that can be used to link requests that are part of the same flow.

* `type` (string)

  The type of authentication that was performed. Currently, only `service` is supported.

* `value` (string)

  The name of the authentication journey that was performed.

* `subject` (object)

  The subject of the authentication.

* `type` (string)

  The subject type of the subject. Possible values are `user` and `agent`.

* `name` (string)

  The name of the subject.

* `sessionProperties` (object)

  Additional information about the user's session, if one was created successfully. You can use the [Set Session Properties node](https://docs.pingidentity.com/auth-node-ref/latest/set-session-properties.html) to add properties to a session in a journey. You must configure a Session Property Whitelist Service for the realm to allow these properties to be published.

---

---
title: Authenticate over REST
description: Authenticate over REST using the json/authenticate endpoint and manage sessions without UI
component: pingoneaic
page_id: pingoneaic:am-authentication:authn-rest
canonical_url: https://docs.pingidentity.com/pingoneaic/am-authentication/authn-rest.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Authentication", "REST API"]
page_aliases: ["authentication-guide:authn-rest.adoc"]
---

# Authenticate over REST

Advanced Identity Cloud provides the `/json/authenticate` endpoint for authentication, and the `/json/sessions` endpoint for managing sessions and logging out.

The following table summarizes authentication operations you can perform using REST:

| Task                                                                                                                                                                                                                                                                                                                            | Resources                                                                                 |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| **Authenticate to Advanced Identity Cloud**Authenticating to Advanced Identity Cloud means logging in to a specific realm and receiving a session token from Advanced Identity Cloud. Add parameters to the authentication request to provide Advanced Identity Cloud with more information about how you want to authenticate. | [Log in over REST](login-using-rest.html)                                                 |
| **Use the session token**Advanced Identity Cloud returns a session token when you authenticate to a realm. Use this token in subsequent calls to Advanced Identity Cloud. For example, when using REST calls to create, modify, or delete configuration objects.                                                                | [Session tokens after authentication](rest-using-ssotokens.html)                          |
| **Log out of Advanced Identity Cloud**Log out users by sending a `logout` action to the `/json/sessions` endpoint.                                                                                                                                                                                                              | [Log out over REST](logout-using-rest.html)                                               |
| **Invalidate sessions**Invalidate specific sessions, or invalidate all sessions for a user to ensure they are logged out of Advanced Identity Cloud.                                                                                                                                                                            | [Invalidate sessions](../am-sessions/managing-sessions-REST.html#rest-api-session-logout) |
| **Return callback information**The `/json/authenticate` endpoint supports callback mechanisms to return and request information.                                                                                                                                                                                                | [Return callback information](callbacks-supported.html)                                   |

---

---
title: Authenticate with a browser
description: Customize user authentication by specifying realm, journey, and locale in browser URLs
component: pingoneaic
page_id: pingoneaic:am-authentication:authn-from-browser
canonical_url: https://docs.pingidentity.com/pingoneaic/am-authentication/authn-from-browser.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Authentication", "Realms", "Browser"]
page_aliases: ["authentication-guide:authn-from-browser.adoc"]
section_ids:
  authn-from-browser-realm: Specify the realm in the URL
  authn-from-browser-parameters: Authentication parameters
  authn-from-browser-XUI-examples: Example UI login URLs
---

# Authenticate with a browser

When you authenticate to Advanced Identity Cloud using a browser, you can specify the [realm](#authn-from-browser-realm) and the [authentication parameters](#authn-from-browser-parameters) in the URL, to customize the user's authentication experience.

## Specify the realm in the URL

Specify the realm as the value of the `realm` parameter in the URL. Preface the realm name with a forward slash (`/`); for example:

```
https://<tenant-env-fqdn>/am/login/?realm=/alpha
```

## Authentication parameters

Advanced Identity Cloud accepts the following parameters in the URL query string.

* arg=newsession

  Request that Advanced Identity Cloud end the user's current session and start a new session.

- ForceAuth

  If `ForceAuth=true`, request that Advanced Identity Cloud force the user to authenticate even if they already have a valid session.

  On successful authentication, Advanced Identity Cloud issues new session tokens to reauthenticating users, even if the current session already meets the security requirements.

  |   |                                                                                   |
  | - | --------------------------------------------------------------------------------- |
  |   | This parameter is case-sensitive. Using `forceAuth` or `forceauth` has no effect. |

- goto

  On successful authentication, or successful logout, request that Advanced Identity Cloud redirect the user to the specified location. Values must be URL-encoded.

  For details, refer to [Success and failure redirection URLs](redirection-url-precedence.html).

- gotoOnFail

  On authentication failure, request that Advanced Identity Cloud redirect the user to the specified location. Values must be URL-encoded.

  For details, refer to [Success and failure redirection URLs](redirection-url-precedence.html).

- locale

  Request that Advanced Identity Cloud display the user interface in the specified, supported locale. The locale can also be set in the user's profile, in the HTTP header from their browser, or configured in Advanced Identity Cloud.

- realm

  Request that Advanced Identity Cloud authenticate the user to the specified realm.

- resource

  Set this parameter to `true` to request resource-based authentication.

- service

  Request that Advanced Identity Cloud authenticate the user with the specified authentication journey.

### Example UI login URLs

Use any of the options listed in [Authentication parameters](#authn-from-browser-parameters) as URL parameters. Note that URL parameters must appear *before* any occurrences of the pound or hash character (`#`).

The following are example URLs with parameters:

**Example UI Login URLs**

| Description                                                                                                                                             | Example URL                                                                        |
| ------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| Log in to the `alpha` realm, requesting that Advanced Identity Cloud display the user interface in German.                                              | `https://<tenant-env-fqdn>/am/XUI/?realm=/alpha&locale=de#login`                   |
| Log in to the `alpha` realm using the `myJourney` authentication journey, requesting that Advanced Identity Cloud display the user interface in German. | `https://<tenant-env-fqdn>/am/XUI/?realm=/alpha&locale=de&service=myJourney#login` |

---

---
title: Authentication and SSO
description: Overview of authentication and single sign-on topics including journeys, MFA, and social authentication
component: pingoneaic
page_id: pingoneaic:am-authentication:preface
canonical_url: https://docs.pingidentity.com/pingoneaic/am-authentication/preface.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Authentication", "Realms", "Setup &amp; Configuration"]
page_aliases: ["index.adoc", "authentication-guide:preface.adoc"]
---

# Authentication and SSO

These topics cover concepts, implementation, and customization of the authentication and single sign-on (SSO) features of Advanced Identity Cloud.

[icon: cogs, set=fas, size=3x]

#### [Configure Advanced Identity Cloud for authentication](authn-implementation-authn.html)

Learn about Advanced Identity Cloud's authentication mechanisms.

[icon: cubes, set=fad, size=3x]

#### [Nodes and journeys](auth-nodes-and-journeys.html)

Learn about creating authentication journeys.

[icon: th-list, set=fas, size=3x]

#### [Multi-factor authentication](authn-mfa.html)

Require that users provide multiple forms of identification when logging in to services.

[icon: users, set=fas, size=3x]

#### [Single sign-On](about-sso.html)

Enable single sign-on (SSO) so that users can log in once with a single set of credentials.

[icon: comments, set=fas, size=3x]

#### [Social authentication](social-authentication.html)

Allow users to authenticate to your services by using third-party identity providers.

[icon: handshake, set=fad, size=3x]

#### [RADIUS authentication](radius-authentication.html)

Learn how Advanced Identity Cloud supports the RADIUS protocol to provide RADIUS authentication.

---

---
title: Authentication reference
description: Reference links for authentication configuration, endpoints, nodes, services, and scripting APIs
component: pingoneaic
page_id: pingoneaic:am-authentication:authn-reference
canonical_url: https://docs.pingidentity.com/pingoneaic/am-authentication/authn-reference.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Authentication"]
page_aliases: ["authentication-guide:authn-reference.adoc"]
---

# Authentication reference

Use the links in this table to find reference information about authentication configuration settings, endpoints, and the scripting API for authentication in Advanced Identity Cloud.

| Link                                                                  | Description                                                                                                                    |
| --------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| [Core authentication attributes](realm-auth-config.html)              | The realm settings for configuring authentication in Advanced Identity Cloud.                                                  |
| [Journey nodes](../journeys/auth-nodes.html)                          | Describes the nodes available in Advanced Identity Cloud and how to configure them.                                            |
| [Authenticate endpoints](authenticate-endpoint-parameters.html)       | The authentication endpoints and their parameters.                                                                             |
| [Client configuration reference](social-idp-client-reference.html)    | The settings required for configuring social authentication.                                                                   |
| [Configure services](../am-reference/services-configuration.html)     | How to configure Advanced Identity Cloud services.                                                                             |
| [Return callback information](callbacks-supported.html)               | The supported callbacks.                                                                                                       |
| [Scripted Decision node API](../am-scripting/scripting-api-node.html) | The API for the [Scripted Decision node](https://docs.pingidentity.com/auth-node-ref/latest/auth-node-scripted-decision.html). |

Learn more about configuring Advanced Identity Cloud settings and services in [Reference](../am-reference/preface.html).

---

---
title: Authenticator apps
description: Download and use authenticator apps for multi-factor authentication with one-time passwords and push notifications
component: pingoneaic
page_id: pingoneaic:am-authentication:authenticator-app
canonical_url: https://docs.pingidentity.com/pingoneaic/am-authentication/authenticator-app.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Authentication", "Multi-factor Authentication (MFA)"]
page_aliases: ["authentication-guide:authn-mfa-download-app.adoc", "authn-mfa-download-app.adoc"]
section_ids:
  ping-id-mobile-app: PingID mobile app
  forgerock-authenticator-app: ForgeRock Authenticator app
  other-authenticator-apps: Other authenticator apps
---

# Authenticator apps

An authenticator app is an application, installed on a device, that end users use for multi-factor authentication (MFA).

In general, an authenticator app does the following:

* Supports push notifications from the authentication server.

* Generates one-time passwords (OTPs) that the end user is required to provide, usually in addition to a password, when logging into their account.

Advanced Identity Cloud supports a number of authenticator apps:

* [PingID mobile app](#ping-id-mobile-app)

* [ForgeRock Authenticator app](#forgerock-authenticator-app)

* [Other authenticator apps](#other-authenticator-apps)

## PingID mobile app

The PingID mobile app is the default supported authenticator app for performing MFA with Advanced Identity Cloud. This app supports time-based one-time passwords (TOTPs) only. It doesn't support HMAC-based one-time passwords (HOTPs).

Depending on their device type, end users can download the PingID mobile app from one of the following locations:

* [Apple App Store](https://apps.apple.com/us/app/pingid/id891247102) (for iOS devices)

* [Google Play](https://play.google.com/store/apps/details?id=prod.com.pingidentity.pingid) (for Android devices)

* [PingID Downloads site](https://www.pingidentity.com/en/resources/downloads/pingid.html)

They must register the PingID mobile app with Advanced Identity Cloud to use it as an additional factor when logging in.

## ForgeRock Authenticator app

The ForgeRock Authenticator app supports time-based one-time passwords (TOTPs) and HMAC-based one-time passwords (HOTPs).

Depending on their device type, end users can download the ForgeRock Authenticator app from one of the following locations:

* [Apple App Store](https://apps.apple.com/app/forgerock-authenticator/id1038442926) (for iOS devices)

* [Google Play](https://play.google.com/store/apps/details?id=com.forgerock.authenticator) (for Android devices)

|   |                                                                                                                                                                                                                                                                                                                            |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Although the PingID mobile app is the default supported authenticator app for performing MFA with Advanced Identity Cloud, there is no smooth migration path from the ForgeRock Authenticator app to the PingID mobile app. If you're already using the ForgeRock Authenticator app for MFA, you should continue to do so. |

## Other authenticator apps

You can perform MFA with any third-party authenticator app that supports the Time-Based One-Time Password (TOTP) open standard. For example, Google Authenticator or Salesforce Authenticator.

To build your own authenticator app, integrate the Ping (ForgeRock) Authenticator module using Ping SDKs.

Read the SDKs documentation for instructions for [Android](https://docs.pingidentity.com/sdks/latest/authenticator-module/getting-started/01-setup-your-project.html#android) and [iOS](https://docs.pingidentity.com/sdks/latest/authenticator-module/getting-started/01-setup-your-project.html#ios).

---

---
title: Backchannel authentication
description: Let third-party federation services initiate authentication and transmit user data directly to the system
component: pingoneaic
page_id: pingoneaic:am-authentication:backchannel-authentication
canonical_url: https://docs.pingidentity.com/pingoneaic/am-authentication/backchannel-authentication.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Authentication", "Backchannel"]
section_ids:
  demonstrate_backchannel_authentication: Demonstrate backchannel authentication
  create-auth-journey: Create an authentication journey
  configure-oauth-service: Configure the OAuth 2.0 provider service
  create-oauth-client: Create an OAuth 2.0 client
  allowlist-session-properties: Allowlist session properties (optional)
  get-access-token: Get an access token
  intialize-the-transaction: Initialize the backchannel authentication transaction
  complete-backchannel-auth: Complete the backchannel authentication
  check-the-status: Check the status of the backchannel authentication request
  backchannel-endpoints: Backchannel authentication REST endpoints
---

# Backchannel authentication

Backchannel authentication lets a third-party federation service initiate authentication with Advanced Identity Cloud on behalf of a user. The federation service collects the user data and transmits this data directly to Advanced Identity Cloud. Advanced Identity Cloud redirects the user to complete the authentication process without having to re-enter the collected data. Backchannel authentication provides a seamless user experience and is more secure as users don't have to enter credentials multiple times.

|   |                                                                                                                                                                                                                                                                                                                                                                     |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The backchannel authentication flow described here is an Advanced Identity Cloud feature. It's distinct from the following OpenID Connect (OIDC) flows, which also use the term *backchannel*:- [OIDC backchannel request grant](../am-oidc1/openid-connect-backchannel-request-flow.html) (CIBA)

- [OIDC backchannel logout](../am-oidc1/backchannel-logout.html) |

Backchannel authentication uses a [transactional authorization](../am-authorization/transactional-authorization.html) process with requests sent to the [backchannel authentication REST endpoints](#backchannel-endpoints). Data supplied by the federation service is saved in a *transaction* with a specific transaction ID. When the user starts their authentication journey in Advanced Identity Cloud, the transaction locates the federation-provided data and inserts it into the journey's shared state.

The following diagram illustrates the backchannel authentication flow.

![Sequence diagram illustrating backchannel authentication flow.](_images/backchannel-auth.svg)

## Demonstrate backchannel authentication

These steps use an OAuth 2.0 client to mimic the third-party federation service. The client initializes the backchannel authentication transaction and Advanced Identity Cloud redirects the user to a simple login journey to complete authentication.

The process includes the following steps:

1. [Create an authentication journey](#create-auth-journey)

2. [Configure the OAuth 2.0 provider service](#configure-oauth-service)

3. [Create an OAuth 2.0 client](#create-oauth-client)

4. [Allowlist session properties (optional)](#allowlist-session-properties)

5. [Get an access token](#get-access-token)

6. [Initialize the backchannel authentication transaction](#intialize-the-transaction)

7. [Complete the backchannel authentication](#complete-backchannel-auth)

8. [Check the status of the backchannel authentication request](#check-the-status)

### Create an authentication journey

This example assumes a simple journey that lets the user log in by supplying only their password. The username is provided by the third-party federation service as part of the backchannel authentication request and is added to the journey's shared state, so the journey doesn't need to collect it.

The name of the journey is `Login`.

![backchannel auth journey](_images/backchannel-auth-journey.png)

|   |                                                                                                                                                                                                                                                                                                                  |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | To prevent users from authenticating directly through this journey, either for security reasons or because the journey is insufficient as a complete authentication service, configure it as a [transactional authentication journey](configure-authentication-trees.html#configure-transactional-auth-journey). |

### Configure the OAuth 2.0 provider service

1. Under Native Consoles > Access Management, go to Realms > *Realm Name* > Services > OAuth2 Provider > Advanced.

2. In the Client Registration Scope Allowlist field, add `back_channel_authentication`.

3. In the Grant Types field, add `Client Credentials` if it isn't already there.

4. Click Save Changes.

Find more information in [Authorization server configuration](../am-oauth2/oauth2-configure-authz.html).

### Create an OAuth 2.0 client

The OAuth 2.0 client represents the third-party federation service.

Create a confidential client named `myClient` with the following configuration:

* **Client ID**: `myClient`

* **Client secret**: `my-client-secret`

* **Scope(s)**: `back_channel_authentication`

* **Grant Types**: `Client Credentials`

Find more information in [Client application registration](../am-oauth2/oauth2-register-client.html).

### Allowlist session properties (optional)

When you query the state of a successful backchannel authentication, you might want to obtain certain session details. To do this, configure the Session Property Whitelist Service and specify any properties to be included in a query response.

1. Go to Realms > *Realm Name* > Services, and click Add a Service.

2. Select `Session Property Whitelist Service` and click Create.

3. In the Allowlisted Session Property Names, enter the session properties you want to obtain.

   For example, enter `authInstant`, `AMCtxId`, and `Service` to include the session properties shown in the [Check the status of the backchannel authentication request](#check-the-status) example.

4. Click Save Changes.

### Get an access token

Get an access token with a scope of `back_channel_authentication` using the client credentials grant. For example:

```bash
$ curl \
--request POST \
--data "grant_type=client_credentials" \
--data "client_id=myClient" \
--data "client_secret=my-client-secret" \
--data "scope=back_channel_authentication" \
"https://<tenant-env-fqdn>/am/oauth2/realms/root/realms/alpha/access_token"
{
  "access_token": "FnpG1lU0fUooJFY-82sq3UiAnGA",
  "scope": "back_channel_authentication",
  "token_type": "Bearer",
  "expires_in": 3599
}
```

Find more information in [Client application authentication](../am-oauth2/oauth2-client-auth.html).

### Initialize the backchannel authentication transaction

This section assumes that a user has already signed on to the third-party federation service and that the service has their *username*.

As the OAuth 2.0 client, send an HTTP POST request to the `/authenticate/backchannel/initialize` endpoint. Specify the authentication journey (`Login` in this example) to which the user should be redirected and the user in the JSON payload.

Optionally, include a `data` object to add initialization data to the journey's shared state such as `userName`, and a `trackingId` to let the federation service track the request through Advanced Identity Cloud. If a `trackingId` is provided, Advanced Identity Cloud logs this ID and its own audit tracking ID. The custom tracking ID must be a string of 36 characters or fewer and can include only the characters `A-Z` `a-z` `0-9` `-` and `_`.

Find more information about the request body in [/authenticate/backchannel/initialize](authenticate-endpoint-parameters.html#authenticatebackchannelinitialize).

For example:

```bash
$ curl \
--request POST \
--header "Content-Type: application/json" \
--header "Accept-API-Version: resource=1, protocol=2.0" \
--header "Authorization: Bearer FnpG1lU0fUooJFY-82sq3UiAnGA" \
--data '{
  "type": "service",
  "value": "Login",
  "subject": {
    "type": "user",
    "name": "ce3c42e2-6f9c-4451-8590-9ee40fad3f83"
  },
  "data": {
    "userName": "ce3c42e2-6f9c-4451-8590-9ee40fad3f83"
  },
  "trackingId": "Y5tyzQi9cGVJjy2L"
}' \
"https://<tenant-env-fqdn>/am/json/realms/root/realms/alpha/authenticate/backchannel/initialize"
{
  "transaction": "b3070138-cd73-4ef2-bd58-812602d7b757",
  "redirectUri": "https://<tenant-env-fqdn>/am/UI/Login?realm=/alpha&authIndexType=transaction&authIndexValue=b3070138-cd73-4ef2-bd58-812602d7b757"
}
```

Advanced Identity Cloud returns a transaction ID and the complete redirect URI, including the transaction ID.

|   |                                                                                                                                                                                                                                                                                                             |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | By default, an end user can retry the backchannel transaction if it fails, until it times out. To change this behavior, set `allowRetry` to `false` in the request body. In this case, the backchannel authentication token goes into the `Failure` state the first time the backchannel transaction fails. |

### Complete the backchannel authentication

In a real-world scenario, the user follows the `redirectUri` provided in the response and completes the authentication.

As user bjensen, open the provided redirect URI in a browser window:

![backchannel login](_images/backchannel-login.png)

Enter bjensen's password. Her username was provided in the initialize request and placed into the journey's shared state by the transaction, so the journey doesn't need to prompt for it.

Click Next and observe that bjensen is authenticated.

### Check the status of the backchannel authentication request

Using the same access token, send an HTTP POST request to the `/authenticate/backchannel/info` endpoint, specifying the transaction ID in the JSON payload. For example:

```bash
$ curl \
--request POST \
--header "Content-Type: application/json" \
--header "Accept-API-Version: resource=1, protocol=2.0" \
--header "Authorization: Bearer Nc_SMVZ85VTJ_CDpaqO5JkMBOAs" \
--data '{
    "transaction": "b3070138-cd73-4ef2-bd58-812602d7b757"
}' \
"https://<tenant-env-fqdn>/am/json/realms/root/realms/alpha/authenticate/backchannel/info"
{
  "state": "COMPLETED",
  "result": "APPROVED",
  "auditTrackingIds": [
    "82d76902-7d18-41ea-9ae6-05643b05d018-1029776",
    "trackingId": "Y5tyzQi9cGVJjy2L"
  ],
  "type": "service",
  "value": "Login",
  "subject": {
    "type": "user",
    "name": "bjensen"
  },
  "sessionProperties": {
    "authInstant": "2024-12-03T14:04:31Z"
    "AMCtxId": "1289ff8c-c712-9215-b282-bad671f56vy2-847363"
    "Service": "Login"
  }
}
```

The response includes the following:

* The `state` of the transaction (`CREATED`, `IN_PROGRESS`, or `COMPLETED`)

* The `result` of the backchannel authentication (`UNKNOWN`, `APPROVED`, or `DENIED`)

  |   |                                                                                                                         |
  | - | ----------------------------------------------------------------------------------------------------------------------- |
  |   | A `DENIED` result is only possible if you've set `allowRetry` to `false` when you initiate the backchannel transaction. |

* An array of `auditTrackingIds`, including the standard audit ID Advanced Identity Cloud generates and any custom tracking IDs supplied in the initial request.

* Any allowlisted `sessionProperties`.

  Learn more in [Allowlist session properties (optional)](#allowlist-session-properties).

## Backchannel authentication REST endpoints

Advanced Identity Cloud exposes the following REST endpoints for backchannel authentication:

| Endpoint                               | Description                                                                                                                                                                                                                                                                                                                       |
| -------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `/authenticate/backchannel/initialize` | Lets a third-party federation service initiate a backchannel authentication flow.                                                                                                                                                                                                                                                 |
| `/authenticate/backchannel/info`       | Lets a third-party federation service verify that a backchannel authentication process completed successfully.	You must access this endpoint with an OAuth 2.0 token that has the back\_channel\_authentication scope. The token must have been granted by the same Advanced Identity Cloud tenant specified in the redirect URI. |

Find reference information on these endpoints in [json/authenticate/backchannel](authenticate-endpoint-parameters.html#rest-authenticate-backchannel).

---

---
title: Backchannel callbacks
description: Handle backchannel callbacks to access HTTP headers, certificates, and request metadata during authentication
component: pingoneaic
page_id: pingoneaic:am-authentication:callbacks-backchannel
canonical_url: https://docs.pingidentity.com/pingoneaic/am-authentication/callbacks-backchannel.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Authentication", "Callbacks", "REST API"]
page_aliases: ["authentication-guide:authn-backchannel-callbacks.adoc", "authn-backchannel-callbacks.adoc"]
section_ids:
  httpcallback: HttpCallback
  languagecallback: LanguageCallback
  scripttextoutputcallback: ScriptTextOutputCallback
  x509certificatecallback: X509CertificateCallback
---

# Backchannel callbacks

Nodes use these callbacks to recover additional information from the request, such as a header or a certificate.

## HttpCallback

Accesses user credentials sent in the `Authorization` header:

```
Authorization: Basic bXlDbGllbnQ6Zm9yZ2Vyb2Nr
```

Class to import in scripts: `com.sun.identity.authentication.spi.HttpCallback`

Learn more in [HttpCallback](../_attachments/apidocs/com/sun/identity/authentication/spi/HttpCallback.html).

## LanguageCallback

Retrieves the locale from the request header for localizing text presented to the user.

Class to import in scripts: `javax.security.auth.callback.LanguageCallback`

Learn more in [LanguageCallback](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/javax/security/auth/callback/LanguageCallback.html).

## ScriptTextOutputCallback

Inserts a script into the page presented to the user; for example, to collect data about the user's environment.

|   |                                                                                                                                                                                                                                                                                      |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | Don't use `ScriptTextOutputCallback` to build custom user interfaces or style the login page. Scripts injected this way might rely on specific Advanced Identity Cloud JavaScript or HTML that isn't guaranteed to remain stable. This could cause them to break in future releases. |

Class to import in scripts: `com.sun.identity.authentication.callbacks.ScriptTextOutputCallback`

Learn more in [ScriptTextOutputCallback](../_attachments/apidocs/com/sun/identity/authentication/callbacks/ScriptTextOutputCallback.html).

## X509CertificateCallback

Retrieves an X.509 certificate, for example, from a header.

Class to import in scripts: `com.sun.identity.authentication.spi.X509CertificateCallback`

Learn more in [X509CertificateCallback](../_attachments/apidocs/com/sun/identity/authentication/spi/X509CertificateCallback.html).

---

---
title: Client configuration reference
description: Configure social identity provider clients with OAuth2, OIDC, JWT, and encryption settings
component: pingoneaic
page_id: pingoneaic:am-authentication:social-idp-client-reference
canonical_url: https://docs.pingidentity.com/pingoneaic/am-authentication/social-idp-client-reference.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Authentication", "Social Authentication", "Setup &amp; Configuration"]
page_aliases: ["authentication-guide:social-idp-client-reference.adoc"]
---

# Client configuration reference

* Enabled

  Whether the provider is enabled.

  Required: Yes.

* Auth ID Key

  The attribute the social identity provider uses to identify an authenticated individual. For example, `id`, `sub`, and `user_id`.

  Required: Yes.

* Client ID

  The `client_id` parameter as described in [section 2.2](https://www.rfc-editor.org/rfc/rfc6749.html#section-2.2) of *The OAuth 2.0 Authorization Framework* specification.

  Required: Yes.

* Client Secret

  The `client_secret` parameter as described in [section 2.3](https://www.rfc-editor.org/rfc/rfc6749.html#section-2.3) of *The OAuth 2.0 Authorization Framework* specification.

  |   |                                                                                                                                                                                                                              |
  | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | This property is deprecated. Use the Client Secret Label Identifier instead.If you set a Client Secret Label Identifier and Advanced Identity Cloud finds a matching secret in a secret store, the Client Secret is ignored. |

  Required: No.

* Client Secret Label Identifier

  An identifier used to create a *secret label* for mapping to a secret in a secret store.

  Advanced Identity Cloud uses this identifier to create a specific secret label for this service instance, using the template `am.social.providers.identifier.secret` where identifier is the value of Client Secret Label Identifier.

  The identifier can only contain alphanumeric characters `a-z`, `A-Z`, `0-9`, and periods (`.`). It can't start or end with a period.

  If you set a Client Secret Label Identifier and Advanced Identity Cloud finds a matching secret in a secret store, the Client Secret is ignored.

  Required: No.

* Authentication Endpoint URL

  The URL to the social provider's endpoint handling authentication as described in [section 3.1](https://www.rfc-editor.org/rfc/rfc6749.html#section-3.1) of *The OAuth 2.0 Authorization Framework*. For example, `https://accounts.google.com/oauth2/v2/auth`.

  Required: Yes.

* Access Token Endpoint URL

  The URL to the endpoint handling access tokens as described in [section 3.2](https://www.rfc-editor.org/rfc/rfc6749.html#section-3.2) of *The OAuth 2.0 Authorization Framework* specification. For example, `https://www.googleapis.com/oauth2/v4/token`.

  Required: Yes.

* User Profile Service URL

  The user profile URL that returns profile information. For example, `https://www.googleapis.com/oauth2/v3/userinfo`.

  This URL should return JSON objects in its response.

  Required: No.

* Token Introspection Endpoint URL

  The URL to the endpoint handling access token validation, as described in the [*OAuth 2.0 Token Introspection*](https://www.rfc-editor.org/info/rfc7662) specification. For example, `https://oauth2.googleapis.com/tokeninfo`.

  Required: No.

* Redirect URL

  The URL to which the identity provider will redirect the user after authenticating, as described in [Section 3.1.2](https://www.rfc-editor.org/rfc/rfc6749.html#section-3.1.2) of *The OAuth 2.0 Authorization Framework* specification.

  This URL is usually a page or path in Advanced Identity Cloud. For example, `https://<tenant-env-fqdn>/am?_realm=alpha`. The URL is also registered in the identity provider's service.

  If you're using an app built with the Ping SDKs for Android or iOS, you can also use a custom URI scheme as the redirect. For example, `com.example.sdkapp:redirect_uri_path` or `auth://com.example.ios.sdkapp`.

  |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
  | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | * When using the `FORM_POST` response mode, you must specify the `form_post` endpoint in the redirection URL. For example, `https://[.var]##_<tenant-env-fqdn>_##/am/oauth2/client/form_post/social IdP client`.

    Find more information in [Response Mode](#response-mode).

  * If you encounter domain validation prompts when using `forgeblocks.com` and `id.forgerock.io` domains as redirect URLs in your Google OAuth 2.0 applications, you must [use a custom domain](../realms/custom-domains.html), and then set up [domain verification with Google](../realms/custom-domains.html#custom-domain-google).

  * If you encounter `No provider found` errors when using `forgeblocks.com` and `id.forgerock.io` domains as redirect URLs in your OAuth 2.0 applications, either modify the redirect URL to include a realm identifier, or [use a custom domain](../realms/custom-domains.html):

    * Incorrect:

      ```
      https://<tenant-env-fqdn>/am/oauth2/client/form_post/...
      ```

    * Correct:

      ```
      https://<tenant-env-fqdn>/am/oauth2/<realm>/client/form_post/...
      ```

      *or*

      ```
      https://<custom-domain>/am/oauth2/client/form_post/...
      ```

      A custom domain acts as a realm DNS alias, so when it's used as a redirect URL, you don't have to specify the realm because Advanced Identity Cloud implicitly knows which realm to use. |

  Required: Yes.

* Redirect after form post URL

  The URL of a custom login page or application. Advanced Identity Cloud will send processed form post data related to social login authentication to that URL as the value of the `form_post_entry` query parameter.

  To continue the authentication journey, the custom login page is responsible for making a call to the Advanced Identity Cloud `/json/authenticate` endpoint with the authentication ID (`authID`) and the processed form data (`form_post_entry`).

  Configure this property when the following is true:

  * The `FORM_POST` response mode is configured.

  * Your users log in to Advanced Identity Cloud using custom login pages, such as apps using the Ping SDKs, instead of the Advanced Identity Cloud admin console.

    Required: No.

* Scope Delimiter

  The delimiter used to separate scope values. For example, a blank space (``), or a comma character (`,`).

  Most providers use a blank space.

  Required: Yes.

* OAuth Scopes

  The list of scopes to request from the provider.

  The scopes that the provider returns depends on the permissions that the resource owner, such as the end user, grants to the client application.

  For example, Google exposes its supported scopes in their [OAuth 2.0 Scopes for Google APIs](https://developers.google.com/identity/protocols/oauth2/scopes) documentation.

  Required: Yes.

* Client Authentication Method

  How the client should authenticate to the provider. Possible values are:

  * `CLIENT_SECRET_POST`

    The client sends the client ID and the secret in the `client_ID` and the `client_secret` parameters in the body of the request.

  * `CLIENT_SECRET_BASIC`

    The client sends the client ID and the secret in a basic authorization header with the base64-encoded value of *client-id:client-secret*.

  * `PRIVATE_KEY_JWT`

    The client sends its credentials to the provider in a signed JWT as specified in the [JSON Web Token (JWT) Profile for OAuth 2.0 Client Authentication and Authorization Grants](https://www.rfc-editor.org/info/rfc7523).

  * `ENCRYPTED_PRIVATE_KEY_JWT`

    The client sends its credentials to the provider in a signed, then encrypted JWT as specified in the [JSON Web Token (JWT) Profile for OAuth 2.0 Client Authentication and Authorization Grants](https://www.rfc-editor.org/info/rfc7523).

  Some authentication methods require additional configuration:

  > **Collapse: How do I configure JWT authentication with signed JWTs?**
  >
  > 1. Obtain a list of supported signing algorithms from the provider's `.well-known` endpoint, and decide which one you will use.
  >
  > 2. In the JWT Signing Algorithm field, enter the signing algorithm that Advanced Identity Cloud will use to sign the JWT. For example, `RSA256`.
  >
  >    This field may already be configured if the client is sending request objects.
  >
  > 3. Provide a JWK with the public key to the identity provider. Read their documentation for more information.
  >
  >    For example, you could copy the contents of the public JWK in a field in the provider's service configuration, or you could configure the realm's `/oauth2/connect/rp/jwk_uri` endpoint, which exposes the client's public keys.
  >
  >    Configure the realm's `/oauth2/connect/rp/jwk_uri` endpoint in the provider, which exposes the client's public keys. Read the provider's documentation for more information.
  >
  > 4. Change the value in the Private Key JWT Expiration Time (seconds) field, if needed. It has a sensible value preconfigured, but you may need to tune it for your provider.

  > **Collapse: How do I configure JWT authentication with signed and encrypted JWTs?**
  >
  > 1. Follow the steps in [How do I configure JWT authentication with signed JWTs?](#JWT-auth-signing) to configure Advanced Identity Cloud to sign authentication JWTs.
  >
  >    Now you're ready to configure Advanced Identity Cloud to encrypt authentication JWTs.
  >
  > 2. Obtain a list of supported encryption algorithms and methods from the provider's `.well-known` endpoint, and decide which one you will use.
  >
  > 3. In the JWT Encryption Algorithm field, select the encryption algorithm.
  >
  >    If the required encryption algorithm doesn't appear in the list, check the reference entry for the [JWT Encryption Algorithm](#jwt-encryption-algorithm) field for information on how to add it.
  >
  >    This field may already be configured if the client is encrypting request objects.
  >
  > 4. In the JWT Encryption Method field, select the encryption method.
  >
  >    This field may already be configured if the client is encrypting request objects.
  >
  > 5. In the JWKS URI Endpoint field, configure the URI containing the provider's public JWK set.
  >
  >    Obtain the URI from the provider's `.well-known` endpoint, or their documentation.
  >
  >    Advanced Identity Cloud will use the JWK URI to fetch the provider's public encryption key.
  >
  > 6. Perform one of the following steps depending on the encryption method you configured:
  >
  >    1. If you chose Direct AES Encryption method, select `NONE` in the JWT Signing Algorithm field. Signing is redundant with this encryption method.
  >
  >    2. If you chose an encryption method different from the Direct AES Encryption method, configure signing. Find more information in [How do I configure JWT authentication with signed JWTs?](#JWT-auth-signing).

  Required: Yes.

* PKCE Method

  Specifies the PKCE transformation method Advanced Identity Cloud uses when making requests to the provider's authorization endpoint, as specified in [Section 4.2](https://www.rfc-editor.org/rfc/rfc7636.html#section-4.2) of the *Proof Key for Code Exchange by OAuth Public Clients* specification.

  Select `NONE` to disable PKCE transformations.

  Required: No.

* Request Parameter JWT Option

  (OIDC providers only) Specifies whether Advanced Identity Cloud should provide a request object JWT to the provider. Possible values are:

  * `NONE`

    Advanced Identity Cloud doesn't send a request object to the provider.

  * `REFERENCE`

    The request object JWT is stored in Advanced Identity Cloud's CTS token store, and Advanced Identity Cloud exposes a unique identifier for it using the `oauth2/request_uri` endpoint for the realm. The URL to the endpoint and the JWT's unique identifier are passed to the provider in the `request_uri` parameter of the request.

    Ensure that the provider can reach the endpoint.

    An example of the URL is `https://platform.example.com:8443/am/realms/root/realms/myRealm/oauth2/request_uri/requestobjectID`

    |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
    | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    |   | When integrating with [itsme®](https://www.itsme.be/en/), ensure that the base URL of Advanced Identity Cloud contains the `443` port. For example, `https://platform.example.com:443/am`.To do this, configure the Base URL Source service:1) Under Native Consoles > Access Management, go to Realms > *Realm Name* > Services.

    2) Add a `Base URL Source` service (if one isn't already configured) or select it to change its properties:

       ![A screenshot showing itsme example configuration details for the Base URL Source service.](_images/base-URL-itsme.png) |

  * `VALUE`

    Advanced Identity Cloud appends the JWT as the value of the `request` parameter of the request.

    > **Collapse: How do I configure the client to send signed request objects?**
    >
    > 1. In the Request Parameter JWT Option field, select either `VALUE` or `REFERENCE`.
    >
    >    Read your identity provider's documentation for more information.
    >
    > 2. Obtain a list of supported signing algorithms from the provider's `.well-known` endpoint, and decide which one you will use.
    >
    > 3. In the JWT Signing Algorithm field, select the signing algorithm that Advanced Identity Cloud will use to sign the request object. For example, `RS256`.
    >
    >    This field may already be configured if the client is using JWT client authentication.
    >
    > 4. Provide a JWK with the public key to the identity provider. Read their documentation for more information.
    >
    >    For example, you could copy the contents of the public JWK in a field in the provider's service configuration, or you could configure the realm's `/oauth2/connect/rp/jwk_uri` endpoint, which exposes the client's public keys.
    >
    >    Configure the realm's `/oauth2/connect/rp/jwk_uri` endpoint in the provider, which exposes the client's public keys. Read the provider's documentation for more information.

    > **Collapse: How do I configure the client to send signed and encrypted request objects?**
    >
    > 1. Follow the steps in [How do I configure the client to send signed request objects?](#how-to-sign-request-objects) to configure Advanced Identity Cloud to send signed request objects.
    >
    >    Now you're ready to configure Advanced Identity Cloud to send encrypted request objects.
    >
    > 2. Enable Encrypt Request Parameter JWT.
    >
    > 3. Obtain a list of supported encryption algorithms and methods from the provider's `.well-known` endpoint, and decide which one you will use.
    >
    > 4. In the JWT Encryption Algorithm field, select the encryption algorithm.
    >
    >    If the required encryption algorithm doesn't appear in the list, check the reference entry for the [JWT Encryption Algorithm](#jwt-encryption-algorithm) field for information on how to add it.
    >
    >    This field may already be configured if the client is encrypting authentication JTWs.
    >
    > 5. In the JWT Encryption Method field, select the encryption method.
    >
    >    This field may already be configured if the client is encrypting authentication JWTs.
    >
    > 6. In the JWKS URI Endpoint field, configure the URI containing the provider's public JWK set.
    >
    >    Obtain the URI from the provider's `.well-known` endpoint.
    >
    >    Advanced Identity Cloud will use the JWK URI to fetch the provider's public encryption key.
    >
    > 7. Perform one of the following steps depending on the encryption method you configured:
    >
    >    1. If you chose Direct AES Encryption method, select `NONE` in the JWT Signing Algorithm field. Signing is redundant with this encryption method.
    >
    >    2. If you chose an encryption method different from the Direct AES Encryption method, configure signing. Find more information in [How do I configure the client to send signed request objects?](#how-to-sign-request-objects).

* Require exp claim in Request Object

  (OIDC providers only) If enabled, the `exp` claim must be included in JWT request objects in the [/oauth2/authorize](../am-oauth2/oauth2-authorize-endpoint.html) request.

  The `exp` (expiration time) claim defines the lifetime of the JWT, after which the JWT is no longer valid.

  The default value of this attribute is false.

* Encrypt Request Parameter JWT

  Specifies whether the request parameter must be encrypted when Request Parameter JWT Option is set to `REFERENCE` or `VALUE`.

* ACR Values

  (OIDC providers only) A space-separated list, in order of preference, of the client's `acr` values.

  Required: No.

* Well Known Endpoint

  (OIDC providers only) The URL for retrieving information about the provider, such as endpoints, and public keys. For example, `https://accounts.google.com/.well-known/openid-configuration`.

  |   |                                                                |
  | - | -------------------------------------------------------------- |
  |   | Leave this field empty for the `LINE (Browser)` configuration. |

  Required: No.

* Request Object Audience

  (OIDC providers only) The intended audience (`aud`) of the request object when the Request Parameter JWT Option field is set to `VALUE` or `REFERENCE`.

  When not configured, Advanced Identity Cloud uses the value of the Issuer field.

* Private Key JWT Audience

  (OIDC providers only) The intended audience (`aud`) of the private key JWT when performing an authentication using the `PRIVATE_KEY_JWT` client authentication method.

When not configured, Advanced Identity Cloud uses the value of the Access Token Endpoint URL field.

* OP Encrypts ID Tokens

  (OIDC providers only) Whether the provider encrypts ID Tokens.

  > **Collapse: How do I configure Advanced Identity Cloud to receive encrypted tokens?**
  >
  > 1. Provide a JWK with the public key to the identity provider. Read the identity provider's documentation for more information.
  >
  >    For example, you could copy the contents of the public JWK in a field in the provider's service configuration, or you could configure the realm's `/oauth2/connect/rp/jwk_uri` endpoint, which exposes the client's public keys.
  >
  >    Configure the realm's `/oauth2/connect/rp/jwk_uri` endpoint in the provider, which exposes the client's public keys. Read the provider's documentation for more information.

  Required: No.

* Issuer

  (OIDC providers only) The issuer of ID Tokens.

  Either specify a regular expression or a string value that must exactly match the value returned in the ID token, depending on the configuration of the [Issuer comparison check](#issuer-comparison-check) setting.

  Obtain the `issuer` value from the provider's `.well-known` endpoint.

  Required: Yes.

* Enable Native Nonce

  (OIDC providers only) When enabled, the provider native SDK must include a `nonce` claim in the ID token. The value of the claim must be the value of the `nonce` claim sent in the Authentication Request.

  Required: No.

* User Info Response Format

  (OIDC providers only) The format in which the provider's `userinfo` endpoint returns data.

  Some options require additional configuration:

  > **Collapse: How do I configure the client to receive signed userinfo JWTs?**
  >
  > 1. In the JWKS URI Endpoint field, configure the URL containing the provider's public JWK set. Obtain it from the provider's `.well-known` endpoint, or their documentation.
  >
  >    Advanced Identity Cloud will use this URL to fetch the provider's public signing key.

  > **Collapse: How do I configure the client to receive signed, then encrypted userinfo JWTs?**
  >
  > 1. Follow the steps in [How do I configure the client to receive signed userinfo JWTs?](#signed-userinfo-JWT) to configure Advanced Identity Cloud to receive signed JWTs.
  >
  >    Now you're ready to configure Advanced Identity Cloud to receive encrypted JWTs.
  >
  > 2. Provide a JWK with the public key to the identity provider. Read their documentation for more information.
  >
  >    For example, you could copy the contents of the public JWK in a field in the provider's service configuration, or you could configure the realm's `/oauth2/connect/rp/jwk_uri` endpoint, which exposes the client's public keys.
  >
  >    Configure the realm's `/oauth2/connect/rp/jwk_uri` endpoint in the provider, which exposes the client's public keys. Read the provider's documentation for more information.

  Possible values are:

  * `JSON`

    The provider's `userinfo` endpoint returns a JSON object.

  * `SIGNED_JWT`

    The provider's `userinfo` endpoint returns a signed JWT.

  * `SIGNED_THEN_ENCRYPTED_JWT`

    The provider's `userinfo` endpoint returns a signed, then encrypted JWT.

* JWKS URI Endpoint

  The URI that contains the public keys of the identity provider. Advanced Identity Cloud will use these keys to verify signatures or to encrypt objects.

  Configure this field when:

  * Client Authentication Method is set to `ENCRYPTED_PRIVATE_KEY_JWT`.

  * Encrypt Request Parameter JWT is enabled.

  * User Info Response Format is set to `SIGNED_JWT` or `SIGNED_THEN_ENCRYPTED_JWT`.

  Required: No.

* Claims

  Any claims on the request object, in JSON format. These claims must conform to the [claims request parameter](https://openid.net/specs/openid-connect-core-1_0.html#ClaimsParameter), as defined in the *OpenID Connect specification*.

* JWT Signing Algorithm

  The signing algorithm supported by the provider that Advanced Identity Cloud uses to sign the following:

  * Client authentication JWTs when Client Authentication Method is set to `PRIVATE_KEY_JWT`.

  * (OIDC providers only) Request JWTs when Request Parameter JWT Option is set to `VALUE` or `REFERENCE`.

  Obtain a list of the supported algorithms from the provider's `.well-known` endpoint. Select `NONE` if the client will encrypt the JWT with the Direct AES Encryption method, because the signature will be redundant.\
  Required: No.

- JWT Encryption Algorithm

  The encryption algorithm supported by the provider that Advanced Identity Cloud should use to encrypt client authentication JWTs when Client Authentication Method is set to `PRIVATE_KEY_JWT`, and (OIDC providers only) request JWTs when Request Parameter JWT Option is set to `VALUE` or `REFERENCE`.

  If set to `NONE`, Advanced Identity Cloud won't encrypt the JWTs. Obtain a list of the supported algorithms from the provider's `.well-known` endpoint.

  Required: No.

- JWT Encryption Method

  The encryption algorithm supported by the provider that Advanced Identity Cloud should use to encrypt the following:

  * Client authentication JWTs when Client Authentication Method is set to `PRIVATE_KEY_JWT`.

  * (OIDC providers only) Request JWTs when Request Parameter JWT Option is set to `VALUE` or `REFERENCE`.

  Use in conjunction with `JWT Encryption Algorithm`. Obtain a list of the supported methods from the provider's `.well-known` endpoint.\
  Required: No.

- Private Key JWT Expiration Time (seconds)

  Specifies the amount of time, in seconds, that Advanced Identity Cloud will cache the client authentication JWT before creating a new one.

  Caching the JWT avoids creating a new one for every client authentication. However, it may also become invalid if the provider changes its configuration.

  Required: No.

* Response Mode

  (OIDC providers only) Specify the way the provider will return ID tokens to Advanced Identity Cloud. Possible values are:

  * `DEFAULT`. The provider returns the ID token as query parameters, as explained in the [OpenID Connect Core 1.0 incorporating errata set 1](https://openid.net/specs/openid-connect-core-1_0.html) specification.

    Most preconfigured providers use the `DEFAULT` response mode.

  * `FORM_POST`. The provider returns the ID token by submitting an HTML form using the HTTP POST method, as explained in the [OAuth 2.0 Form Post Response Mode](https://openid.net/specs/oauth-v2-form-post-response-mode-1_0.html) specification.

    When using this response mode, add the `/oauth2/client/form_post/social IdP client` URI to the Redirect URL, where *social IdP client* is the name of the social identity provider client that you're configuring. For example, `https://[.var]##_<tenant-env-fqdn>_##/am/oauth2/client/form_post/myAppleClient` or `https://[.var]##_<tenant-env-fqdn>_##/am/oauth2/alpha/client/form_post/myAppleClient` if you need to specify a realm.

    By default, the `form_post` endpoint processes the post data, encrypts it, and redirects with it back to the authentication journey to resume authentication.

    However, environments using custom login pages need to configure the Redirect after form post URL property to redirect back to the custom login pages.

    Required: Yes.

- Certificate Revocation Checking Options

  Specify one or more options to be used by the TLS certificate revocation checking mechanism.

  The possible values are:

  * `ONLY_END_ENTITY`: Only check the revocation status of end-entity certificates.

  * `PREFER_CRLS`: Prefer certificate revocation lists (CRLs) to Online Certificate Status Protocol (OCSP).

  * `NO_FALLBACK`: Disable the fallback mechanism.

  * `SOFT_FAIL`: Allow revocation check to succeed if the revocation status cannot be determined due to a network error.

  * `DISABLE_REVOCATION_CHECKING`: Disable all revocation checking.

  Including `DISABLE_REVOCATION_CHECKING` as one of the options will prevent any revocation checking. For further details of the other options, refer to: [PKIXRevocationChecker.Option](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/security/cert/PKIXRevocationChecker.Option.html).

  If no options are selected, the default behavior is to enable revocation checking with `SOFT_FAIL`.

  If the certificate doesn't specify any OCSP or CRL endpoints, the revocation checking will hard fail even if the `SOFT_FAIL` option is enabled. In this case, an administrator could disable revocation checking.

* Use Custom TrustStore

  Specifies whether a custom truststore is used to verify the server certificate of the `.well-known` endpoint or JWKs URI of an OpenID provider (OP) in a TLS handshake.

  If enabled, a secret label is generated dynamically using the alphanumeric characters of the client configuration name. For example, a client configuration called `sampleOidcConfig` results in a secret label named `am.services.oidc.reliant.party.sampleOidcConfig.truststore`.

  Note that an administrator must map the generated secret label to an alias that exists in the realm secret store.

  If this setting is not enabled, the default truststore is used to verify the server certificate.

- Request Native App for UserInfo

  (Apple SSO) When enabled, this flag indicates that the native app can send the user's `userinfo` in JSON format.

  Apple returns the `userinfo` only *once*, when the user first consents to send their details, and not on subsequent authentication attempts. In addition, the user has the option *not* to consent to Apple sending their `userinfo`.

  If you're progressively profiling the `userinfo` with data from other social providers—​usually, using a [Patch Object node](https://docs.pingidentity.com/auth-node-ref/latest/patch-object.html)--there is a risk of overwriting the user's details with blank values when the user authenticates through Apple SSO.

  To mitigate this risk, you can add a [Scripted Decision node](https://docs.pingidentity.com/auth-node-ref/latest/scripted-decision.html) to your authentication journey to assess whether `userinfo` is provided.

  > **Collapse: How do I use a Scripted Decision node to check ?**
  >
  > The [normalized-profile-to-managed-user.js](../am-scripting/sample-scripts.html#normalized-profile-to-managed-user-js) script sets a boolean flag (`nameEmptyOrNull`) that indicates whether Apple returned the user's `firstName` and `lastName`.
  >
  > Add a [Scripted Decision node](https://docs.pingidentity.com/auth-node-ref/latest/scripted-decision.html) to your journey that evaluates the flag and sets the outcome accordingly; for example:
  >
  > * Next-generation
  >
  > * Legacy
  >
  > ```javascript
  > if (nodeState.get('nameEmptyOrNull')) {
  >   action.goTo("true");
  > } else {
  >   action.goTo("false");
  > }
  > ```
  >
  > ```javascript
  > var fr = JavaImporter(org.forgerock.openam.auth.node.api.Action);
  >
  > if (nodeState.get('nameEmptyOrNull')) {
  >   action = fr.Action.goTo("true").build();
  > } else {
  > action = fr.Action.goTo("false").build();
  > }
  > ```
  >
  > You can now configure your journey to patch the `userinfo` object based on the outcome of the [Scripted Decision node](https://docs.pingidentity.com/auth-node-ref/latest/scripted-decision.html). If you need to progressively profile the user information on every authentication, *regardless of whether the user's first name and last name are returned by the OIDC provider*, you can use another [Scripted Decision node](https://docs.pingidentity.com/auth-node-ref/latest/scripted-decision.html) that does the following:
  >
  > * If the user details aren't present, route the `userinfo` patch through a [Patch Object node](https://docs.pingidentity.com/auth-node-ref/latest/patch-object.html) configured to ignore the `firstName` and `lastName`. (In the Ignored Fields list, add `givenName` to ignore the `firstName` and `sn` to ignore the `lastName`.)
  >
  > * If the user details are present, route the `userinfo` patch through a [Patch Object node](https://docs.pingidentity.com/auth-node-ref/latest/patch-object.html) that patches the full object.
  >
  > For more information, refer to [First name and last name are missing when signing in to Identity Cloud or AM 7.x using Apple social sign-on](https://backstage.forgerock.com/knowledge/kb/article/a82054946) in the *ForgeRock Knowledge Base*.

  Required: No.

- UI Config Properties

  Specifies a map of properties defined and consumed in the UI. The map affects how the identity provider's logo will show on the login page.

  > **Collapse: Advanced Identity Cloud common end user UI properties**
  >
  > * `buttonImage`: A relative path to an image in the End User UI.
  >
  > * `buttonCustomStyle`: Any custom CSS you wish to apply to the button outside of normal End User UI styling.
  >
  > * `buttonClass`: Adds the specified class to the identity provider button, for any additional styling you want to apply.
  >
  > * `buttonCustomStyleHover`: Adds custom styling when the cursor is hovering over the button.
  >
  > * `buttonDisplayName`: The name of the identity provider, which will be included either on the button or in the button's `alt` attribute, depending on styling.

  Required: Yes

* Transform Script

  A script to convert the provider's raw profile object into a normalized object, also referred to as a *normalization* script.

  Each social identity provider returns different user profile information using their own attribute names.

  For example, Google's OIDC `/userinfo` endpoint returns claims, which Advanced Identity Cloud stores in a `rawProfile` object. The following `google-profile-normalization.js` script maps the attributes of this object to Advanced Identity Cloud profile attributes:

  * Legacy

  * Next-generation

  ```javascript
  (function () {
      var frJava = JavaImporter(
          org.forgerock.json.JsonValue
      );

      var normalizedProfileData = frJava.JsonValue.json(frJava.JsonValue.object());

      normalizedProfileData.put('id', rawProfile.get('sub'));
      normalizedProfileData.put('displayName', rawProfile.get('name'));
      normalizedProfileData.put('givenName', rawProfile.get('given_name'));
      normalizedProfileData.put('familyName', rawProfile.get('family_name'));
      normalizedProfileData.put('photoUrl', rawProfile.get('picture'));
      normalizedProfileData.put('email', rawProfile.get('email'));
      normalizedProfileData.put('username', rawProfile.get('email'));
      normalizedProfileData.put('locale', rawProfile.get('locale'));

      return normalizedProfileData;
  }());
  ```

  ```javascript
  function () {
      var normalizedProfileData = {};
      normalizedProfileData.id = rawProfile.get('sub');
      normalizedProfileData.displayName = rawProfile.get('name');
      normalizedProfileData.givenName = rawProfile.get('given_name');
      normalizedProfileData.familyName = rawProfile.get('family_name');
      normalizedProfileData.photoUrl = rawProfile.get('picture');
      normalizedProfileData.email = rawProfile.get('email');
      normalizedProfileData.username = rawProfile.get('email');
      normalizedProfileData.locale = rawProfile.get('locale');
      return normalizedProfileData;
  }();
  ```

  The script returns a JsonValue object containing normalized attributes in the following format:

  ```bash
  ("platformAttributeName", rawProfile.providerAttributeName)
  ```

  Even if field names are the same, such as `email` and `rawProfile.email`, they still need to be mapped for them to be included in the returned JSON object.

  Advanced Identity Cloud provides default scripts for other preconfigured identity providers. Find information about the bindings and expected return values in the `identity provider-profile-normalization.*` scripts in [Sample scripts](../am-scripting/sample-scripts.html) and in the [Social IdP scripting API](../am-scripting/social-idp-profile-transformation-api.html).

  To write your own script in Javascript for an identity provider, go to Realms > *Realm Name* > Scripts, and use the provided scripts as a reference.

  When a user authenticates, the social authentication journey calls another transformation script set in the [Social Provider Handler node](https://docs.pingidentity.com/auth-node-ref/latest/social-provider-handler.html) to convert the attributes again; this time into an identity object that Advanced Identity Cloud can process.

  |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
  | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | Social authentication nodes expect every attribute to have a value. In other words, the attributes returned by the identity provider can't be empty or `null`, or the journey will end with an error.For example, if a user tries to log in using Google as the identity provider, but they didn't configure a surname in their account, Google returns `null` as the value of the `familyName` for the identity, and social authentication fails.Ensure all users have their social profiles configured correctly, or modify the transformation scripts so that they don't collect null or empty attributes. |

  Required: Yes

- Issuer comparison check

  (OIDC providers only) Determines how the expected issuer value should match the actual value of the `iss` claim:

  * `EXACT`: Advanced Identity Cloud performs a string comparison between the expected and actual issuer values, which must result in an exact match.

  * `REGEX`: Advanced Identity Cloud evaluates the expected issuer value as a regular expression, against which the actual value must match.

    This lets social identity providers use a common issuer value for multiple tenants, which is replaced with a unique value during the OIDC authentication flow. For example, `^https://login.microsoftonline.com/(.*)/v2.0$` is successfully matched against `https://login.microsoftonline.com/tenant-d5c6a592-eec6-47f0/v2.0`.

    |   |                                                                                                                                                                                                                                                                      |
    | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    |   | Consider the performance impact when constructing regular expressions as the comparison is performed for each social identity provider interaction.Also, ensure the regular expression is as specific as possible to avoid matching against incorrect issuer values. |

---

---
title: Configure Advanced Identity Cloud for authentication
description: Configure authentication mechanisms and success/failure URLs for realm-level authentication behavior
component: pingoneaic
page_id: pingoneaic:am-authentication:authn-implementation-authn
canonical_url: https://docs.pingidentity.com/pingoneaic/am-authentication/authn-implementation-authn.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Authentication", "Nodes &amp; Trees", "Realms", "Setup &amp; Configuration"]
page_aliases: ["authentication-guide:authn-implementation-authn.adoc"]
---

# Configure Advanced Identity Cloud for authentication

Authentication journeys are extremely flexible, and you can adapt them to suit your specific deployment. Although the number of choices can seem daunting, when you understand the basic process, you'll be able to configure custom journeys to securely protect access to the applications in your organization.

The following table summarizes the high-level tasks required to configure authentication in a realm:

| Task                                                                                                                                                                                                                                                               | Resources                                                               |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------- |
| **Configure the required authentication mechanisms**You need to decide how your users are going to log in. For example, you may require your users to provide multiple credentials, or to log in using third-party identity providers, such as Facebook or Google. | [Nodes and journeys](auth-nodes-and-journeys.html)                      |
| **Configure the success and failure URLs for the realm**By default, Advanced Identity Cloud redirects users to the UI after successful authentication. No failure URL is defined by default.                                                                       | [Success and failure redirection URLs](redirection-url-precedence.html) |

---

---
title: Configure authentication webhooks
description: Send HTTP POST requests to external services when authentication events occur during journeys
component: pingoneaic
page_id: pingoneaic:am-authentication:auth-tree-webhooks
canonical_url: https://docs.pingidentity.com/pingoneaic/am-authentication/auth-tree-webhooks.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
---

# Configure authentication webhooks

Use *webhooks* to send an HTTP POST request to a server when a specific event occurs during an authenticated session, such as a user logging out.

Webhooks are used from within authentication journeys, by the [Register Logout Webhook node](https://docs.pingidentity.com/auth-node-ref/latest/register-logout-webhook.html).

To create a webhook:

1. Under Native Consoles > Access Management, go to Realms > *Realm Name* > Authentication > Webhooks.

2. Select Create Webhook, specify a Webhook Name, and select Create.

   ![Creating a new authentication webhook.](_images/trees-webhook-create.png)

3. Configure the following settings:

   * Url

     The URL to which the HTTP POST is sent when the event occurs.

   * Body

     The body of the HTTP POST. To send different data formats, set the correct Content-Type header in the `Header` property, for example:

     * **Form Data**. Enter the body value in the format `parameter=value&parameter2=value2`, and set a `Content-Type` header of `application/x-www-form-urlencoded`.

     * **JSON Data**. Enter the body value in the format `{"parameter":"value","parameter2":"value2"}`, and set a `Content-Type` header of `application/json`.

   * Headers

     Any HTTP headers to add to the POST.

     To add a header, enter the name of the header in the `Key` field, and the value, and then click Add (➕).

     To remove a header, click Delete (✖).

   The fields in a webhook support variables for retrieving values from the user's session after successfully authenticating. Specify a variable in the following format: `${variable_name}`.

   To access the type of webhook event, use the `WebhookEventType` parameter key to return one of the following possible values:

   * `LOGOUT`

   * `UPGRADE`

   * `DESTROY`

   * `MAX_TIMEOUT`

   * `IDLE_TIMEOUT`

   For example, to retrieve the event type as a query parameter: `&event=${WebhookEventType}`

   You can use a variable to access custom properties added to the session with the [Set Session Properties node](https://docs.pingidentity.com/auth-node-ref/latest/set-session-properties.html) as well as the following default session properties:

   > **Collapse: Default session properties**
   >
   > | Property                     | Example value                                                  | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
   > | ---------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   > | `AMCtxId`                    | 22e73c81-708e-4849-b064-db29b68ef943-105372                    | The audit ID for the session. This is logged as the `trackingIds` field in Advanced Identity Cloud access audit logs.                                                                                                                                                                                                                                                                                                                                                |
   > | `authInstant`                | 2022-02-28T14:06:31Z                                           | The exact time that authentication completed.                                                                                                                                                                                                                                                                                                                                                                                                                        |
   > | `AuthLevel`                  | 5                                                              | The authentication level of the session, determined by the login mechanism used to create the session. For example, a journey can have an authentication level of 10.Step-up authentication is triggered if an authentication level specified by an agent or policy that is designed to protect a resource, is greater than or equal to the value of the `AuthLevel` session property.Learn more in [Session upgrade with MFA](../am-sessions/session-upgrade.html). |
   > | `CharSet`                    | UTF-8                                                          | The character set for the session, set to `UTF-8`.                                                                                                                                                                                                                                                                                                                                                                                                                   |
   > | `clientType`                 | genericHTML                                                    | The type of client, set to `genericHTML`.                                                                                                                                                                                                                                                                                                                                                                                                                            |
   > | `FullLoginURL`               | https\://example.forgeblocks.com/platform/?realm=alpha         | The full login URL, including query parameters.                                                                                                                                                                                                                                                                                                                                                                                                                      |
   > | `Host`                       | 192.0.2.1                                                      | The originating IP address of the authentication request.                                                                                                                                                                                                                                                                                                                                                                                                            |
   > | `HostName`                   | 192.0.2.1                                                      | The host name that was used when the session was authenticated.                                                                                                                                                                                                                                                                                                                                                                                                      |
   > | `IndexType`                  | service                                                        | Based on the value of the `authIndexValue` query parameter during authentication. Typically, this is set to `service`.                                                                                                                                                                                                                                                                                                                                               |
   > | `Locale`                     | en\_US                                                         | The session locale.                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
   > | `loginURL`                   | /am/XUI                                                        | The base login URL. A subset of `FullLoginURL`.                                                                                                                                                                                                                                                                                                                                                                                                                      |
   > | `OidcSid`                    | g0wmSpoAIwH6HAwCnurvRcfYqh4                                    | Unique session ID used by Advanced Identity Cloud to determine whether OIDC ID tokens granted for the same client relate to the same session. This appears when `Enable Session Management` (`storeOpsToken`) is set to true in the OAuth 2.0 provider settings.                                                                                                                                                                                                     |
   > | `Organization`               | o=alpha,ou=services,dc=am,dc=example,dc=com                    | The DN of the realm where authentication took place.                                                                                                                                                                                                                                                                                                                                                                                                                 |
   > | `Principal`                  | id=bjensen,ou=user,o=alpha,ou=services,dc=am,dc=example,dc=com | The value of `sun.am.UniversalIdentifier`.                                                                                                                                                                                                                                                                                                                                                                                                                           |
   > | `Principals`                 | bjensen                                                        | The username for the session.                                                                                                                                                                                                                                                                                                                                                                                                                                        |
   > | `Service`                    | Example                                                        | The name of the journey that was used to authenticate this session.                                                                                                                                                                                                                                                                                                                                                                                                  |
   > | `successURL`                 | /am/console                                                    | The URL that was redirected to, upon a successful login request.                                                                                                                                                                                                                                                                                                                                                                                                     |
   > | `sun.am.UniversalIdentifier` | id=bjensen,ou=user,o=alpha,ou=services,dc=am,dc=example,dc=com | The DN of the user (username is lowercase).                                                                                                                                                                                                                                                                                                                                                                                                                          |
   > | `UserId`                     | bjensen                                                        | The `id` value from the `Principal` property.                                                                                                                                                                                                                                                                                                                                                                                                                        |
   > | `UserProfile`                | Required                                                       | Can be one of: `Required`, `Create`, `Ignore`, or `CreateWithAlias`. Based on the value of the `dynamicProfileCreation` authentication configuration. Values other than `Ignore` indicates that user profile attributes were mapped based on the `User Attribute Mapping to Session Attribute` setting. Learn more in [authentication configuration](realm-auth-config.html#authn-core-post-auth).Default: `Required`.                                               |
   > | `UserToken`                  | bjensen                                                        | The username, as defined in the `Principal` property.                                                                                                                                                                                                                                                                                                                                                                                                                |

   The following figure shows an example webhook, using variable substitutions:

   ![Example authentication webhook.](_images/trees-webhook-example.png)

   |   |                                                                                                                                                                                   |
   | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | Specifying a variable that isn't present in the user's session puts the literal variable text in the HTTP POST request, for example `user=${UserId}`, rather than `user=bjensen`. |

---

---
title: Configure journeys
description: Configure journey properties including enablement, session creation, session timeouts, and transactional use
component: pingoneaic
page_id: pingoneaic:am-authentication:configure-authentication-trees
canonical_url: https://docs.pingidentity.com/pingoneaic/am-authentication/configure-authentication-trees.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Authentication", "Nodes &amp; Trees", "Journeys", "Setup &amp; Configuration"]
section_ids:
  identity-resource-journeys: Specify the identity object type for a journey
  disable-authn-tree: Enable and disable an authentication journey
  disable-child-journey: Disable direct access through an inner journey
  enable-journey-completion: Configure an authentication journey to always run
  configure-nosession-tree: Configure a no session journey
  configure-transactional-auth-journey: Configure a transactional authentication journey
  configure-journey-session-duration-tree: Configure journey session duration in a journey
  configure-auth-session-timeouts-tree: Configure authenticated session timeouts in a journey
---

# Configure journeys

You can configure journeys in the Advanced Identity Cloud admin console or over REST:

* Advanced Identity Cloud admin console:

  1. Go to Journeys > Journeys > *journey name* > Edit.

  2. In the journey editor, click the More ([icon: ellipsis-h, set=fa]) menu at the top right of the page, then click Edit Details and update the journey configuration.

* REST: Send a PUT request to update the journey configuration. You must include the journey ID and all the nodes in the journey in the request.

This table outlines the high-level tasks for configuring authentication journeys:

| Task                                                                                           | Description                                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Specify the identity object type for a journey](#identity-resource-journeys)                  | Specify the identity object a journey should use. For example `Alpha realm - Users`.                                                                                                         |
| [Enable and disable an authentication journey](#disable-authn-tree)                            | Disable journeys during development or when they aren't in use to enhance security.                                                                                                          |
| [Disable direct access through an inner journey](#disable-child-journey)                       | Prevent an inner journey from being called directly, ensuring it's only used within its parent journey.                                                                                      |
| [Configure an authentication journey to always run](#enable-journey-completion)                | Force a journey to execute on every authentication attempt, even if a valid session already exists.                                                                                          |
| [Configure a no session journey](#configure-nosession-tree)                                    | Create a journey that completes successfully without creating an authenticated session, ideal for tasks like delegated administration.                                                       |
| [Configure a transactional authentication journey](#configure-transactional-auth-journey)      | Indicate a journey can only be used for transactional authentication purposes, including backchannel authentication, OIDC or SAML 2.0 application journeys, and transactional authorization. |
| [Configure journey session duration in a journey](#configure-journey-session-duration-tree)    | Override the maximum duration of the journey session for a specific journey, for example, to allow more time for an email verification step.                                                 |
| [Configure authenticated session timeouts in a journey](#configure-auth-session-timeouts-tree) | Set custom session idle and maximum timeout values for authenticated sessions created by a specific journey.                                                                                 |

## Specify the identity object type for a journey

Journeys assume a specific *identity object type*. The nodes in the journey use this object type to verify the identity, for example, users, roles, or organizations. Only objects of type *user* can authenticate. The default journeys provided with Advanced Identity Cloud assume the object authenticating through the journey is a *realm-name* user, for example `Alpha realm - Users` or `Bravo realm - Users`.

When you create a new journey, you select the object type in the Identity Object list.

To change the object type of an existing journey:

1. In the Advanced Identity Cloud admin console, go to Journeys > Journeys > *journey name* > Edit.

2. In the journey editor, click the More ([icon: ellipsis-h, set=fa]) menu at the top right of the page, then click Edit Details.

3. Select a new object type from the Identity Object list.

## Enable and disable an authentication journey

Custom authentication journeys are *enabled* by default, when they are saved. For security purposes, you can disable custom journeys during development and testing, to prevent accidentally allowing access through these journeys. Rather than having unused journeys enabled, you should disable the default journeys until you need them.

When a user attempts to authenticate through a disabled journey, Advanced Identity Cloud returns a `Tree does not exist` error.

To enable or disable a journey through the Advanced Identity Cloud admin console, follow the steps to [deactivate journeys](../journeys/journeys.html#deactivate-journeys).

To enable or disable a journey over REST, send a PUT request to update the journey configuration. Specify the journey ID, the nodes in the journey, and set the `enabled` property.

> **Collapse: Example**
>
> ```bash
> $ curl \
> --header "Content-Type: application/json" \
> --header "Authorization: Bearer <access-token>" \
> --header "Accept-API-Version: protocol=2.1,resource=3.0" \
> --request PUT \
> --data '{
>   "entryNodeId": "c11e9cf8-ef48-4740-876f-6300e2f46aef",
>   "nodes": {
>    ...
>   },
>   "enabled": false
> }' \
> 'https://<tenant-env-fqdn>/am/json/realms/root/realms/alpha/realm-config/authentication/authenticationtrees/trees/myAuthTree'
> {
>   "_id": "myAuthTree",
>   "_rev": "2070284866",
>   "entryNodeId": "c11e9cf8-ef48-4740-876f-6300e2f46aef",
>   "innerTreeOnly": false,
>   "noSession": false,
>   "mustRun": false,
>   "enabled": false,
>   "transactionalOnly": false,
>   "uiConfig": {},
>   "nodes": {
>    ...
>   }
> }
> ```

## Disable direct access through an inner journey

An inner (or child) journey lets you nest authentication logic. There is no limit to the depth of nesting.

You configure an inner journey like any other journey and call it from a parent journey using an [Inner Tree Evaluator node](https://docs.pingidentity.com/auth-node-ref/latest/inner-tree-evaluator.html).

You might want to hide inner journeys as complete services. In other words, you might want to prevent users from authenticating directly through a inner journey, either for security reasons or simply because the inner journey is insufficient as a complete authentication service. Additionally, inner journeys can't be used as [transactional authentication journeys](#configure-transactional-auth-journey).

To use the Advanced Identity Cloud admin console to ensure an inner journey is only called from its parent, select the Inner journey checkbox when you create a [custom journey](../journeys/journeys.html#custom-journey) or edit an existing journey.

To configure an inner journey over REST, send a PUT request to update the journey configuration. Specify the journey ID, the nodes in the journey, and set the `innerTreeOnly` property to `true`.

> **Collapse: Example**
>
> ```bash
> $ curl \
> --header "Content-Type: application/json" \
> --header "Authorization: Bearer <access-token>" \
> --header "Accept-API-Version: protocol=2.1,resource=3.0" \
> --request PUT \
> --data '{
>   "entryNodeId": "c11e9cf8-ef48-4740-876f-6300e2f46aef",
>   "nodes": {
>    ...
>   },
>   "innerTreeOnly": true
> }' \
> 'https://<tenant-env-fqdn>/am/json/realms/root/realms/alpha/realm-config/authentication/authenticationtrees/trees/myAuthTree"
> {
>   "_id": "myAuthTree",
>   "_rev": "2070284866",
>   "entryNodeId": "c11e9cf8-ef48-4740-876f-6300e2f46aef",
>   "innerTreeOnly": true,
>   "noSession": false,
>   "mustRun": false,
>   "enabled": true,
>   "transactionalOnly": false,
>   "uiConfig": {},
>   "nodes": {
>    ...
>   }
> }
> ```

|   |                                                                                                                                                                                                                                                         |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | To find out if the current journey is configured as an inner journey only, include a Scripted Decision node with a script that calls `journey.innerJourney()`.Learn more in [Get journey details](../am-scripting/script-bindings.html#common-journey). |

## Configure an authentication journey to always run

You can set a journey to always execute whether a user has already authenticated successfully and a session exists or not. If enabled, the journey runs even when the session was created through a different journey and irrespective of the value of the [ForceAuth](authn-from-browser.html#authentication-forceAuth) parameter.

If you have configured an [application journey](../app-management/application-journeys.html) by associating a journey with an OIDC or a SAML 2.0 application, then you don't need to configure the journey to always run because this is default functionality for application journeys.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | You can't configure a journey to always run when it's set as the **default** journey.Because the default journey is often used as a fallback option for many authentication flows, for example, for Ping SDKs flows over REST, a forced execution of a journey could inadvertently lead to unexpected behavior.Also, to prevent unexpected behavior in the authentication flow, don't configure a journey to always run when it's mapped to the [default ACR](../am-oidc1/oidc-authentication-requirements.html#acr-claim). |

If a user successfully logs in using a specific authentication journey and then tries to reauthenticate to the same journey while the session is still valid, the default behavior is for the authentication flow to skip the processing of the journey.

For example, the [Set Session Properties node](https://docs.pingidentity.com/auth-node-ref/latest/set-session-properties.html) is never run in this scenario:

![Authentication journey to demonstrate mustRun property](_images/auth-mustrun-journey.png)

To use the Advanced Identity Cloud admin console to make sure the journey always runs, select the Run journey for all users regardless of current session checkbox when you create a [custom journey](../journeys/journeys.html#custom-journey) or edit an existing journey.

To use the REST API to configure a journey to always run, send a PUT request to update the journey configuration. Specify the journey ID, the nodes in the journey, and set the `mustRun` property to `true`.

> **Collapse: Example**
>
> ```bash
> $ curl \
> --header "Content-Type: application/json" \
> --header "Authorization: Bearer <access-token>" \
> --header "Accept-API-Version: protocol=2.1,resource=3.0" \
> --request PUT \
> --data '{
>   "entryNodeId": "83fa0ce2-1b0f-4f8f-83fb-0d2648339797",
>   "nodes": {
>    ...
>   },
>   "mustRun": true
> }' \
> 'https://<tenant-env-fqdn>/am/json/realms/root/realms/alpha/realm-config/authentication/authenticationtrees/trees/myAuthTree"
> {
>   "_id": "myAuthTree",
>   "_rev": "2070284866",
>   "entryNodeId": "c11e9cf8-ef48-4740-876f-6300e2f46aef",
>   "innerTreeOnly": false,
>   "noSession": false,
>   "mustRun": true,
>   "enabled": true,
>   "transactionalOnly": false,
>   "uiConfig": {},
>   "nodes": {
>    ...
>   }
> }
> ```

## Configure a no session journey

A no session journey doesn't result in an authenticated session when it successfully completes.

A common use case for a no session journey is a delegated admin task, such as an administrator changing a user's password. In this scenario, you don't want an authenticated session to be created when the administrator enters the credentials of the user whose password they're changing.

|   |                                                                                                                                                                                                                                                                                                                                                                          |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | This can also be achieved by setting the [`noSession` query parameter](authenticate-endpoint-parameters.html#nosession). However, consider that an end user could remove the query parameter to create a session.If the `noSession` property is set to `true` in either the journey or the query parameter, the resulting journey won't create an authenticated session. |

To use the Advanced Identity Cloud admin console to configure a no session journey, select the No Session checkbox when you create a [custom journey](../journeys/journeys.html#custom-journey) or edit an existing journey.

To configure a no session journey over REST, send a PUT request to update the journey configuration. Specify the journey ID, the nodes in the journey, and set the `noSession` property to `true`.

> **Collapse: Example**
>
> ```bash
> $ curl \
> --header "Content-Type: application/json" \
> --header "Authorization: Bearer <access-token>" \
> --header "Accept-API-Version: protocol=2.1,resource=3.0" \
> --request PUT \
> --data '{
>   "entryNodeId": "c11e9cf8-ef48-4740-876f-6300e2f46aef",
>   "nodes": {
>    ...
>   },
>   "noSession": true
> }' \
> "https://<tenant-env-fqdn>/am/json/realms/root/realms/alpha/realm-config/authentication/authenticationtrees/trees/myAuthTree"
> {
>   "_id": "myAuthTree",
>   "_rev": "2070284866",
>   "entryNodeId": "c11e9cf8-ef48-4740-876f-6300e2f46aef",
>   "innerTreeOnly": false,
>   "noSession": true,
>   "mustRun": false,
>   "enabled": true,
>   "transactionalOnly": false,
>   "uiConfig": {},
>   "nodes": {
>    ...
>   }
> }
> ```

## Configure a transactional authentication journey

In Advanced Identity Cloud, certain advanced authentication flows initiate a temporary, secure process known as a *transaction* to handle a specific authentication or authorization event.

You can configure journeys for these flows as *transactional authentication journeys* to manage the user interaction required to complete the transaction. This prevents users from authenticating directly through the journey, either for security reasons or because the transactional journey is insufficient as a complete authentication service. Additionally, transactional authentication journeys can't be used as [child journeys](#disable-child-journey).

|   |                                                                                                                   |
| - | ----------------------------------------------------------------------------------------------------------------- |
|   | You don't *have to* configure the journey used in a transactional flow as a transactional authentication journey. |

A transactional authentication journey only runs when Advanced Identity Cloud starts a transaction, which happens when Advanced Identity Cloud does one of the following:

* Initializes [backchannel authentication](backchannel-authentication.html) using either the `/authenticate/backchannel/initialize` endpoint or the [Backchannel Initialize node](https://docs.pingidentity.com/auth-node-ref/latest/backchannel-initialize.html).

* Runs a [SAML 2.0 application](../app-management/application-journeys.html#saml-application-journeys) journey for a remote SP.

* Runs an [OIDC 2.0 application](../app-management/application-journeys.html#oidc-application-journeys) journey when Advanced Identity Cloud is acting as an authorization server.

* Enforces a [transactional authorization](../am-authorization/transactional-authorization.html) policy.

To use the Advanced Identity Cloud admin console to make the journey a transactional authentication journey, select the Transactional Only checkbox when you create a [custom journey](../journeys/journeys.html#custom-journey) or edit an existing journey.

To configure a transactional authentication journey over REST, send a PUT request to update the journey configuration. Specify the journey ID, the nodes in the journey, and set the `transactionalOnly` property to `true`.

> **Collapse: Example**
>
> ```bash
> $ curl \
> --header "Content-Type: application/json" \
> --header "Authorization: Bearer <access-token>" \
> --header "Accept-API-Version: protocol=2.1,resource=3.0" \
> --request PUT \
> --data '{
>   "entryNodeId": "c11e9cf8-ef48-4740-876f-6300e2f46aef",
>   "nodes": {
>    ...
>   },
>   "transactionalOnly": true
> }' \
> "https://<tenant-env-fqdn>/am/json/realms/root/realms/alpha/realm-config/authentication/authenticationtrees/trees/myAuthTree"
> {
>   "_id": "myAuthTree",
>   "_rev": "1081620278",
>   "uiConfig": {},
>   "entryNodeId": "c11e9cf8-ef48-4740-876f-6300e2f46aef",
>   "innerTreeOnly": false,
>   "noSession": false,
>   "mustRun": false,
>   "enabled": true,
>   "transactionalOnly": true,
>   "uiConfig": {},
>   "nodes": {
>    ...
>   }
> }
> ```

## Configure journey session duration in a journey

The maximum duration of a journey session is derived by Advanced Identity Cloud as described in [Maximum duration](suspended-auth.html#maximum-duration).

You can override realm level duration values in an individual journey if required. For example, a journey that requires email verification could have a longer duration than a simple journey that authenticates users with a username and password.

|   |                                                                                                                                                                                                               |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Duration values set in a journey can be overridden at the node level. Learn more in [Maximum duration](suspended-auth.html#maximum-duration).Additionally, duration values set on inner journeys are ignored. |

Learn more in [Suspend journey progress](suspended-auth.html).

To change the authentication journey duration, set the `treeTimeout` property to the required number of minutes in the journey configuration. Send a PUT request to update the journey configuration, including the journey ID and all the nodes in the journey.

> **Collapse: Example**
>
> ```bash
> $ curl \
> --header "Content-Type: application/json" \
> --header "Authorization: Bearer <access-token>" \
> --header "Accept-API-Version: protocol=2.1,resource=3.0" \
> --request PUT \
> --data '{
>   "entryNodeId": "c11e9cf8-ef48-4740-876f-6300e2f46aef",
>   "nodes": {
>    ...
>   },
>   "treeTimeout": 10
> }' \
> "https://<tenant-env-fqdn>/am/json/realms/root/realms/alpha/realm-config/authentication/authenticationtrees/trees/myAuthTree"
> {
>   "_id": "myAuthTree",
>   "_rev": "2070284866",
>   "entryNodeId": "c11e9cf8-ef48-4740-876f-6300e2f46aef",
>   "innerTreeOnly": false,
>   "noSession": false,
>   "mustRun": false,
>   "treeTimeout": 10,
>   "enabled": true,
>   "transactionalOnly": false,
>   "uiConfig": {},
>   "nodes": {
>    ...
>   }
> }
> ```

## Configure authenticated session timeouts in a journey

Timeout settings for an authenticated session are derived by Advanced Identity Cloud as described in [Configure authenticated session timeout settings](../am-sessions/session-state-session-termination.html#auth-session-termination-config).

You can override realm level timeout values in an individual journey if required. For example, a journey that implements MFA could have a longer authenticated session timeout than a simple journey that authenticates users with a username and password.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Session timeouts set in a journey can be overridden at the node or user level. Learn more in [Configure authenticated session timeout settings](../am-sessions/session-state-session-termination.html#auth-session-termination-config).Session timeout values set on child journeys are ignored. However, if session timeouts are set at the *node* level in a child journey, the updated timeouts are used in the parent journey. |

Learn more in [Session termination](../am-sessions/session-state-session-termination.html).

To use the Advanced Identity Cloud admin console to change the session timeouts, select the Override authenticated session timeout checkbox when you create a [custom journey](../journeys/journeys.html#custom-journey) or edit an existing journey. Then enter the required number of minutes in the Maximum Authenticated Session Time and Maximum Authenticated Session Idle Time fields.

To configure the session timeouts over REST, send a PUT request to update the journey configuration. Specify the journey ID, the nodes in the journey, and set the `maximumSessionTime` and `maximumIdleTime` properties to the required number of minutes.

> **Collapse: Example**
>
> The following example sets the `maximumSessionTime` to an hour and the `maximumIdleTime` to 15 minutes for authenticated sessions established through this journey:
>
> ```bash
> $ curl \
> --header "Content-Type: application/json" \
> --header "Authorization: Bearer <access-token>" \
> --header "Accept-API-Version: protocol=2.1,resource=3.0" \
> --request PUT \
> --data '{
>   "entryNodeId": "c11e9cf8-ef48-4740-876f-6300e2f46aef",
>   "nodes": {
>    ...
>   },
>   "maximumSessionTime": 60,
>   "maximumIdleTime": 15
> }' \
> "https://<tenant-env-fqdn>/am/json/realms/root/realms/alpha/realm-config/authentication/authenticationtrees/trees/myAuthTree"
> {
>   "_id": "myAuthTree",
>   "_rev": "2070284866",
>   "entryNodeId": "c11e9cf8-ef48-4740-876f-6300e2f46aef",
>   "innerTreeOnly": false,
>   "maximumSessionTime": 60,
>   "maximumIdleTime": 15,
>   "noSession": false,
>   "mustRun": false,
>   "enabled": true,
>   "transactionalOnly": false,
>   "uiConfig": {},
>   "nodes": {
>    ...
>   }
> }
> ```

|   |                                                                                                                                                                                                                                         |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | To find out if the current journey is configured to always run, include a Scripted Decision node with a script that calls `journey.mustRun()`.Learn more in [Get journey details](../am-scripting/script-bindings.html#common-journey). |

---

---
title: Core authentication attributes
description: Configure core authentication attributes including lockout, post-authentication processing, and security settings
component: pingoneaic
page_id: pingoneaic:am-authentication:realm-auth-config
canonical_url: https://docs.pingidentity.com/pingoneaic/am-authentication/realm-auth-config.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Authentication", "Realms", "Setup &amp; Configuration"]
page_aliases: ["authentication-guide:core-module-conf-hints.adoc", "authentication-guide:realm-auth-config.adoc", "authn-core-settings.adoc", "authentication-guide:authn-core-settings.adoc"]
---

# Core authentication attributes

Advanced Identity Cloud users always authenticate to a realm. Each realm has a set of authentication settings that apply to all authentication performed to that realm. The settings are referred to as *core authentication attributes*.

To configure the default core authentication attributes for a realm, go to Native Consoles > Access Management > Realms > *Realm Name* > Authentication > Settings.

Edit the attributes on this page to configure authentication behavior.

> **Collapse: Core**
>
> The following properties are available under the Core tab:
>
> * Administrator Authentication Configuration
>
>   The default authentication journey used when an administrative user authenticates.
>
> * Organization Authentication Configuration
>
>   The default authentication journey used when a non-administrative user authenticates.

> **Collapse: User Profile**
>
> The following properties are available under the User Profile tab:
>
> * `User Profile`
>
>   Whether a user profile needs to exist in the user data store, or should be created on successful authentication. The possible values are:
>
>   * `true`. Dynamic.
>
>     After successful authentication, Advanced Identity Cloud creates a user profile if one does not already exist. Advanced Identity Cloud then issues the SSO token. Advanced Identity Cloud creates the user profile in the user data store configured for the realm.
>
>   * `createAlias`. Dynamic with User Alias.
>
>     After successful authentication, Advanced Identity Cloud creates a user profile that contains the `User Alias List` attribute, which defines one or more aliases for mapping a user's multiple profiles.
>
>   * `ignore`. Ignored.
>
>     After successful authentication, Advanced Identity Cloud issues an SSO token regardless of whether a user profile exists in the data store. The presence of a user profile is not checked.
>
>     |   |                                                                                                                                                                           |
>     | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
>     |   | Any functionality which needs to map values to profile attributes, such as SAML or OAuth 2.0, will not operate correctly if the User Profile property is set to `ignore`. |
>
>   * `false`. Required.
>
>     After successful authentication, the user must have a user profile in the user data store configured for the realm in order for Advanced Identity Cloud to issue an SSO token.
>
> * User Profile Dynamic Creation Default Roles
>
> |   |                                                          |
> | - | -------------------------------------------------------- |
> |   | This property does not apply to Advanced Identity Cloud. |
>
> * Alias Search Attribute Name
>
>   After a user is successfully authenticated, the user's profile is retrieved. Advanced Identity Cloud first searches for the user based on the data store settings. If that fails to find the user, Advanced Identity Cloud uses the attributes listed here to look up the user profile. This setting accepts any data store specific attribute name.

> **Collapse: Account Lockout**
>
> The following properties are available under the Account Lockout tab:
>
> * Login Failure Lockout Mode
>
>   When enabled, Advanced Identity Cloud deactivates the LDAP attribute defined in the Lockout Attribute Name property in the user's profile upon login failure. This attribute works in conjunction with the other account lockout and notification attributes.
>
> * Login Failure Lockout Count
>
>   The number of attempts a user has to authenticate within the time interval defined in Login Failure Lockout Interval before being locked out.
>
> * Login Failure Lockout Interval
>
>   The time in minutes during which failed login attempts are counted.
>
>   * If one failed login attempt is followed by a second failed attempt within this defined lockout interval, the lockout count starts, and the user is locked out if the number of attempts reaches the number defined by the Login Failure Lockout Count property.
>
>   * If an attempt within the defined lockout interval proves successful before the number of attempts reaches the number defined by the Login Failure Lockout Count property, the lockout count is reset.
>
> * Email Address to Send Lockout Notification
>
>   One or more email addresses to which notification is sent if a user lockout occurs.
>
>   Separate multiple addresses with spaces, and append `|locale|charset` to addresses for recipients in non-English locales.
>
> * Warn User After N Failures
>
>   The number of authentication failures after which Advanced Identity Cloud displays a warning message that the user will be locked out.
>
> * Login Failure Lockout Duration
>
>   The number of minutes a user must wait after a lockout before attempting to authenticate again. Entering a value greater than `0` enables duration lockout and disables persistent (physical) lockout. *Duration lockout* means the user's account is locked for the number of minutes specified. The account is unlocked after the time period has passed.
>
> * Lockout Duration Multiplier
>
>   Defines a value by which to multiply the value of the Login Failure Lockout Duration attribute for each successive lockout. For example, if Login Failure Lockout Duration is set to 3 minutes, and the Lockout Duration Multiplier is set to 2, the user is locked out of the account for 6 minutes. After the 6 minutes has elapsed, if the user again provides the wrong credentials, the lockout duration is then 12 minutes. With the Lockout Duration Multiplier, the lockout duration is incrementally increased based on the number of times the user has been locked out.
>
> * Lockout Attribute Name
>
>   The LDAP attribute used for persistent (physical) lockout. The default attribute is `inetuserstatus`, although the field is empty in the UI.
>
>   Possible values for the default attribute are `Active`, `Inactive` and `Deleted`.
>
>   The Lockout Attribute Value field must also contain an appropriate value.
>
> * Lockout Attribute Value
>
>   The value to set the lockout attribute to when an account is locked. The default value is `Inactive`, although the field is empty in the UI. The Lockout Attribute Name field must also contain an appropriate value.
>
> * Invalid Attempts Data Attribute Name
>
>   The LDAP attribute used to hold the number of failed authentication attempts towards Login Failure Lockout Count. Although the field is empty in the UI, Advanced Identity Cloud stores this data in the `sunAMAuthInvalidAttemptsDataAttrName` attribute defined in the `sunAMAuthAccountLockout` objectclass by default.
>
> * Store Invalid Attempts in Data Store
>
>   When enabled, Advanced Identity Cloud stores the information regarding failed authentication attempts as the value of the Invalid Attempts Data Attribute Name in the user data store. Information stored includes number of invalid attempts, time of last failed attempt, lockout time and lockout duration.

> **Collapse: General**
>
> The following properties are available under the General tab:
>
> * Default Authentication Locale
>
>   The default language subtype to be used by the Authentication Service. The default value is `en_US`.
>
> * Identity Types
>
> |   |                                                          |
> | - | -------------------------------------------------------- |
> |   | This property does not apply to Advanced Identity Cloud. |
>
> * Pluggable User Status Event Classes
>
> |   |                                                          |
> | - | -------------------------------------------------------- |
> |   | This property does not apply to Advanced Identity Cloud. |
>
> \+
>
> * Use Client-Side Sessions
>
>   When enabled, Advanced Identity Cloud assigns *client-side* sessions to users authenticating to this realm. Otherwise, Advanced Identity Cloud users authenticating to this realm are assigned *server-side* sessions.
>
> * External Login Page URL
>
>   The URL of the external login user interface, if the authentication user interface is hosted separately from Advanced Identity Cloud.
>
>   When set, Advanced Identity Cloud uses the provided URL as the base of the resume URI, rather than using the Base URL Source Service to obtain the base URL. Advanced Identity Cloud uses this URL when constructing the resume URI if authentication is suspended in an authentication journey.
>
> * Default Authentication Level
>
> |   |                                                          |
> | - | -------------------------------------------------------- |
> |   | This property does not apply to Advanced Identity Cloud. |

> **Collapse: Trees**
>
> The following properties are available under the Trees tab:
>
> * Authentication session state management scheme
>
>   The location where Advanced Identity Cloud stores journey sessions.
>
>   Possible values are:
>
>   * `CTS`. Advanced Identity Cloud stores journey sessions [server-side](../am-sessions/server-side-sessions.html), in the CTS token store.
>
>   * `JWT`. Advanced Identity Cloud sends the journey session to the client as a JWT.
>
>   * `In-Memory`. Advanced Identity Cloud stores journey sessions in its memory.
>
>   Learn more in [Introduction to sessions and cookies](../am-sessions/about-sessions.html).
>
>   Default: `JWT` (new installations), `In-Memory` (after upgrade)
>
> - Max duration (minutes)
>
>   The maximum allowed duration of a journey session, including any time spent in the suspended state, in minutes.
>
>   Values from `1` to `2147483647` are allowed.
>
>   Default: `5`
>
> - Suspended authentication duration (minutes)
>
>   The length of time a journey session can be suspended in minutes.
>
>   Suspending a journey session allows time for out-of-band authentication methods, such as responding to emailed codes or performing an action on an additional device. The value must be less than or equal to the total time allowed for a journey session, specified in the *Max duration (minutes)* property.
>
>   Values from `1` to `2147483647` are allowed.
>
>   Default: `5`
>
> - Enable Allowlisting
>
>   When enabled, Advanced Identity Cloud allowlists journey sessions to protect them against replay attacks.
>
>   Default: Disabled

> **Collapse: Security**
>
> The following properties are available under the Security tab:
>
> * Module Based Authentication
>
>   This property doesn't apply to Advanced Identity Cloud.
>
> * Persistent Cookie Encryption Certificate Alias
>
>   The key pair alias in the Advanced Identity Cloud keystore to use for encrypting persistent cookies.
>
>   |   |                                                                                                                                                                                                                                                                                                                                                                                                                           |
>   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
>   |   | This property is deprecated. Use the rotatable secret mapping `am.authentication.nodes.persistentcookie.encryption` instead.If Advanced Identity Cloud finds a matching secret in the secret store for `am.authentication.nodes.persistentcookie.encryption`, this alias is ignored.Learn more about mapping and rotating secrets in [Use ESVs for signing and encryption keys](../tenants/esvs-signing-encryption.html). |
>
>   Default: `test`
>
> * Zero Page Login
>
> |   |                                                          |
> | - | -------------------------------------------------------- |
> |   | This property does not apply to Advanced Identity Cloud. |
>
> * Zero Page Login Referer Allowlist
>
> |   |                                                          |
> | - | -------------------------------------------------------- |
> |   | This property does not apply to Advanced Identity Cloud. |
>
> * Zero Page Login Allowed Without Referer?
>
> |   |                                                          |
> | - | -------------------------------------------------------- |
> |   | This property does not apply to Advanced Identity Cloud. |
>
> * Add clear-site-data Header on Logout
>
> |   |                                                          |
> | - | -------------------------------------------------------- |
> |   | This property does not apply to Advanced Identity Cloud. |
>
> * Organization Authentication Signing Secret
>
>   Specifies a cryptographically-secure random-generated HMAC shared secret for signing RESTful authentication requests. When users attempt to authenticate, Advanced Identity Cloud signs a JSON Web Token (JWT) containing this shared secret. The JWT contains the journey session ID, realm, and authentication index type value, but *doesn't* contain the user's credentials.
>
>   When modifying this value, ensure the new shared secret is Base-64 encoded and at least 128 bits in length.

> **Collapse: Post Authentication Processing**
>
> The following properties are available under the Post Authentication Processing tab:
>
> * Default Success Login URL
>
>   Accepts a list of values that specifies where users are directed after successful authentication. The format of this attribute is `client-type|URL` although the only value you can specify at this time is a URL which assumes the type HTML. The default value is `/enduser/?realm=/alpha`. Values that do not specify HTTP have that appended to the deployment URI.
>
> * Default Failure Login URL
>
>   Accepts a list of values that specifies where users are directed after authentication has failed. The format of this attribute is `client-type|URL` although the only value you can specify at this time is a URL which assumes the type HTML. Values that do not specify HTTP have that appended to the deployment URI.
>
> * Authentication Post Processing Classes
>
> |   |                                                          |
> | - | -------------------------------------------------------- |
> |   | This property does not apply to Advanced Identity Cloud. |
>
> * Generate UserID Mode
>
> |   |                                                          |
> | - | -------------------------------------------------------- |
> |   | This property does not apply to Advanced Identity Cloud. |
>
> * Pluggable User Name Generator Class
>
> |   |                                                          |
> | - | -------------------------------------------------------- |
> |   | This property does not apply to Advanced Identity Cloud. |
>
> * User Attribute Mapping to Session Attribute
>
> |   |                                                                                                                                                                                                                                                                                                                                                                                                        |
> | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
> |   | This property does not apply to Advanced Identity Cloud.For authentication journeys, use the [Scripted Decision node](https://docs.pingidentity.com/auth-node-ref/latest/scripted-decision.html) to retrieve user attributes and session properties, or the [Set Session Properties node](https://docs.pingidentity.com/auth-node-ref/latest/set-session-properties.html) for session properties only. |

---

---
title: Interactive callbacks
description: Use interactive callbacks to collect user input like usernames, passwords, and selections during authentication
component: pingoneaic
page_id: pingoneaic:am-authentication:callbacks-interactive
canonical_url: https://docs.pingidentity.com/pingoneaic/am-authentication/callbacks-interactive.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Authentication", "Callbacks", "Setup &amp; Configuration"]
page_aliases: ["authentication-guide:authn-interactive-callbacks.adoc", "authn-interactive-callbacks.adoc"]
section_ids:
  BooleanAttributeInputCallback: BooleanAttributeInputCallback
  ChoiceCallback: ChoiceCallback
  ConfirmationCallback: ConfirmationCallback
  ConsentMappingCallback: ConsentMappingCallback
  DeviceBindingCallback: DeviceBindingCallback
  DeviceProfileCallback: DeviceProfileCallback
  DeviceSigningVerifierCallback: DeviceSigningVerifierCallback
  hiddenvaluecallback: HiddenValueCallback
  IdPCallback: IdPCallback
  KbaCreateCallback: KbaCreateCallback
  NameCallback: NameCallback
  NumberAttributeInputCallback: NumberAttributeInputCallback
  PasswordCallback: PasswordCallback
  PingOneProtectEvaluationCallback: PingOneProtectEvaluationCallback
  PingOneProtectInitializeCallback: PingOneProtectInitializeCallback
  SelectIdPCallback: SelectIdPCallback
  StringAttributeInputCallback: StringAttributeInputCallback
  TermsAndConditionsCallback: TermsAndConditionsCallback
  TextInputCallback: TextInputCallback
  ValidatedCreatePasswordCallback: ValidatedCreatePasswordCallback
  ValidatedCreateUsernameCallback: ValidatedCreateUsernameCallback
---

# Interactive callbacks

Nodes return the following callbacks to request information.

## BooleanAttributeInputCallback

Collects a boolean-style confirmation, such as yes/no or true/false.

The [Attribute Collector node](https://docs.pingidentity.com/auth-node-ref/latest/attribute-collector.html) uses this instead of a [ConfirmationCallback](#ConfirmationCallback) to apply policies and validate the response.

| Callback output field | Description                                                                                                                                                                                                                                                                                                                                                                                               |
| --------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `failedPolicies`      | An array of JSON objects describing validation policies that the input failed. The object is empty until the input is provided and validation fails.                                                                                                                                                                                                                                                      |
| `name`                | A string containing the name of the attribute in the user profile.                                                                                                                                                                                                                                                                                                                                        |
| `policies`            | An array of JSON objects describing [validation policies](../idm-objects/policies.html) the input must pass. An empty JSON object if the node does not require validation.                                                                                                                                                                                                                                |
| `prompt`              | A string containing the description of the information required from the user.                                                                                                                                                                                                                                                                                                                            |
| `required`            | A boolean indicating whether input is required for this attribute.                                                                                                                                                                                                                                                                                                                                        |
| `validateOnly`        | When the node requires validation, this boolean indicates whether to apply validation policies only, or to validate the input and continue to the next node. When `true`, the node only performs input validation and does not continue to the next node.When `true`, this lets the UI validate input as the user types instead of validating the input once and continuing the journey to the next node. |
| `value`               | A string containing a default value for the attribute, if required.                                                                                                                                                                                                                                                                                                                                       |

Example

```json
{
  "callbacks": [{
    "type": "BooleanAttributeInputCallback",
    "output": [{
      "name": "name",
      "value": "preferences/marketing"
    }, {
      "name": "prompt",
      "value": "Send me special offers and services"
    }, {
      "name": "required",
      "value": true
    }, {
      "name": "policies",
      "value": {}
    }, {
      "name": "failedPolicies",
      "value": []
    }, {
      "name": "validateOnly",
      "value": false
    }, {
      "name": "value",
      "value": false
    }],
    "input": [{
      "name": "IDToken1",
      "value": false
    }, {
      "name": "IDToken1validateOnly",
      "value": false
    }]
  }]
}
```

In the input, return the value and a boolean to set `validateOnly`.

Class to import in scripts: `org.forgerock.openam.authentication.callbacks.BooleanAttributeInputCallback`

Learn more in [BooleanAttributeInputCallback](../_attachments/apidocs/org/forgerock/openam/authentication/callbacks/BooleanAttributeInputCallback.html).

## ChoiceCallback

Provides a list of choices and collects the selected choice.

In the input, return `0` if the user selected the first choice, `1` for the second choice, and so forth.

Example

```json
{
  "callbacks": [{
    "type": "ChoiceCallback",
    "output": [{
      "name": "prompt",
      "value": "Choose one"
    }, {
      "name": "choices",
      "value": ["Choice A", "Choice B", "Choice C"]
    }, {
      "name": "defaultChoice",
      "value": 2
    }],
    "input": [{
      "name": "IDToken1",
      "value": 0
    }]
  }]
}
```

Class to import in scripts: `javax.security.auth.callback.ChoiceCallback`

Learn more in [ChoiceCallback](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/javax/security/auth/callback/ChoiceCallback.html).

## ConfirmationCallback

Collects a boolean-style confirmation, such as yes/no or true/false with an optional "Cancel" choice.

| Callback output field | Description                                                                                                             |
| --------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| `defaultOption`       | A number identifying the default option in the array of `options`, counting from `0`.                                   |
| `messageType`         | A number indicating the severity of the message:- `0`: Information

- `1`: Warning

- `2`: Error                        |
| `optionType`          | A number indicating the type of confirmation:- `-1`: Unspecified

- `0`: Yes/no

- `1`: Yes/no/cancel

- `2`: OK/cancel |
| `options`             | An array of strings containing the option text for display to the user.                                                 |
| `prompt`              | A string containing the description of the choice to display to the user.                                               |

Example

```json
{
  "callbacks": [{
    "type": "ConfirmationCallback",
    "output": [{
      "name": "prompt",
      "value": ""
    }, {
      "name": "messageType",
      "value": 0
    }, {
      "name": "options",
      "value": ["Submit", "Start Over", "Cancel"]
    }, {
      "name": "optionType",
      "value": -1
    }, {
      "name": "defaultOption",
      "value": 1
    }],
    "input": [{
      "name": "IDToken1",
      "value": 0
    }]
  }]
}
```

In the input, return `0` if the user selected the first choice, `1` for the second choice, and so forth.

Class to import in scripts: `javax.security.auth.callback.ConfirmationCallback`

Learn more in [ConfirmationCallback](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/javax/security/auth/callback/ConfirmationCallback.html).

## ConsentMappingCallback

Provides profile attributes that require user consent and collects consent from the user.

| Callback output field | Description                                                                   |
| --------------------- | ----------------------------------------------------------------------------- |
| `accessLevel`         | A string containing the access level description for display to the user.     |
| `displayName`         | A string containing the name for display to the user.                         |
| `fields`              | An array containing names of the attributes to share.                         |
| `icon`                | A string containing an icon specification for the privacy and consent notice. |
| `isRequired`          | A boolean indicating whether consent is required.                             |
| `message`             | A string containing the privacy and consent notice for display to the user.   |
| `name`                | A string containing the name of the mapping.                                  |

Example

```json
{
  "callbacks": [{
    "type": "ConsentMappingCallback",
    "output": [{
      "name": "name",
      "value": "managedUser_managedUser"
    }, {
      "name": "displayName",
      "value": "Test Mapping"
    }, {
      "name": "icon",
      "value": ""
    }, {
      "name": "accessLevel",
      "value": "Actual Profile"
    }, {
      "name": "isRequired",
      "value": true
    }, {
      "name": "message",
      "value": "You consent to your data being shared with external services."
    }, {
      "name": "fields",
      "value": []
    }],
    "input": [{
      "name": "IDToken1",
      "value": false
    }]
  }]
}
```

The user must give consent to all attributes or to none; in the input, return a single boolean value.

Class to import in scripts: `org.forgerock.openam.authentication.callbacks.ConsentMappingCallback`

Learn more in [ConsentMappingCallback](../_attachments/apidocs/org/forgerock/openam/authentication/callbacks/ConsentMappingCallback.html).

## DeviceBindingCallback

Binds a client device to a user.

| Callback output field | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| --------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `userId`              | The ID of the user to bind the device to.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `username`            | The username of the user to bind the device to.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `authenticationType`  | Specifies how the client secures access to the private key. Available options are:- `BIOMETRIC`

  Request that the client secures access to the cryptography keys with biometric security, such as a fingerprint.

- `BIOMETRIC_ALLOW_FALLBACK`

  Request that the client secures access to the cryptography keys with biometric security, such as a fingerprint, but allow use of the device PIN if biometric is unavailable.

- `APPLICATION_PIN`

  Request that the client secures access to the cryptography keys with an application-specific PIN.

- `NONE`

  Request that the client generates a key pair, but does not secure access to them. |
| `challenge`           | A string containing the challenge the client should sign with the private key and return for validation.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `title`               | A string containing an optional title to display when requesting biometric authentication to secure access to the key pair.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| `subtitle`            | A string containing an optional subtitle to display when requesting biometric authentication to secure access to the key pair.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `description`         | A string containing optional descriptive text to display when requesting biometric authentication to secure access to the key pair.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `timeout`             | An integer specifying the number of seconds to wait for device binding to complete before reporting a timeout error.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |

Example response data

```json
{
  "authId": "...",
  "callbacks": [
    {
      "type": "DeviceBindingCallback",
      "output": [
        {
          "name": "userId",
          "value": "id=bjensen,ou=user,dc=am,dc=example,dc=com"
        },
        {
          "name": "username",
          "value": "bjensen"
        },
        {
          "name": "authenticationType",
          "value": "BIOMETRIC_ALLOW_FALLBACK"
        },
        {
          "name": "challenge",
          "value": "6IBkTEPcMQ0xCghIclmDLost2ssGO5cPDs0AjUhmDTo="
        },
        {
          "name": "title",
          "value": "Authentication required"
        },
        {
          "name": "subtitle",
          "value": "Cryptography device binding"
        },
        {
          "name": "description",
          "value": "Please authenticate with biometrics to proceed"
        },
        {
          "name": "timeout",
          "value": 60
        }
      ],
      "input": [
        {
          "name": "IDToken1jws",
          "value": ""
        },
        {
          "name": "IDToken1deviceName",
          "value": ""
        },
        {
          "name": "IDToken1deviceId",
          "value": ""
        },
        {
          "name": "IDToken1clientError",
          "value": ""
        }
      ]
    }
  ]
}
```

The client device should perform the following high-level steps to fulfil this callback:

1. Generate a key pair and secure access to it as defined by the `authenticationType` field.

2. Generate a JSON web token (JWT) that has the ID of the user in the subject (`sub`) field and the original value of the `challenge`.

   For example:

   ```
   {
       "sub": "id=bjensen,ou=user,dc=am,dc=example,dc=com",
       "challenge": "6IBkTEPcMQ0xCghIclmDLost2ssGO5cPDs0AjUhmDTo="
   }
   ```

3. Sign the JWT using the RS512 algorithm to create a JSON Web Signature (JWS).

4. Complete the callback, returning the JWS, the key ID (`KID`) of the key pair, the public key, and the name and the unique ID of the device.

The server verifies the returned information and persists it in the user's profile if correct.

Example response data

```json
{
  "authId": "...",
  "callbacks": [
    {
      "type": "DeviceBindingCallback",
      "output": [...],
      "input": [
        {
          "name": "IDToken1jws",
          "value": "eyJhbGciOiJIUzI1NiI....JV_adQssw5cB6aDS6m_kwIiw"
        },
        {
          "name": "IDToken1deviceName",
          "value": "Example Brand Version Android Device"
        },
        {
          "name": "IDToken1deviceId",
          "value": "ae9573dbbf442e7f-8e0c8b428409e0f1c"
        },
        {
          "name": "IDToken1clientError",
          "value": ""
        }
      ]
    }
  ]
}
```

Class to import in scripts: `org.forgerock.openam.authentication.callbacks.DeviceBindingCallback`

Learn more in [DeviceBindingCallback](../_attachments/apidocs/org/forgerock/openam/authentication/callbacks/DeviceBindingCallback.html).

## DeviceProfileCallback

Collects information about the device used to authenticate.

| Callback output field | Description                                                                       |
| --------------------- | --------------------------------------------------------------------------------- |
| `metadata`            | A boolean indicating whether to collect device metadata.                          |
| `location`            | A boolean indicating whether to collect the device location.                      |
| `message`             | A string containing optional text to display while collecting device information. |

Example

```json
{
  "callbacks": [{
    "type": "DeviceProfileCallback",
    "output": [{
      "name": "metadata",
      "value": true
    }, {
      "name": "location",
      "value": true
    }, {
      "name": "message",
      "value": "Collecting....."
    }],
    "input": [{
      "name": "IDToken1",
      "value": ""
    }]
  }]
}
```

In the input, return escaped JSON resembling the following example response data.

Example response data

```json
{
  "identifier": "aec3fe784...o3Xjiizyb9=",
  "alias": "Pixel 3 XL",
  "metadata": {
    "platform": {
      "platform": "Android",
      "version": 28,
      "device": "generic_x86_arm",
      "deviceName": "AOSP on IA Emulator",
      "model": "AOSP on IA Emulator",
      "brand": "google",
      "locale": "en_US",
      "timeZone": "America/Vancouver",
      "jailBreakScore": 1
    },
    "hardware": {
      "hardware": "ranchu",
      "manufacturer": "Google",
      "storage": 774,
      "memory": 1494,
      "cpu": 4,
      "display": {
        "width": 1440,
        "height": 2621,
        "orientation": 1
      },
      "camera": {
        "numberOfCameras": 2
      }
    },
    "browser": {
      "agent": "Dalvik/2.1.0 (Linux; U; Android 9; AOSP on IA Emulator Build/PSR1.180720.117)"
    },
    "bluetooth": {
      "supported": false
    },
    "network": {
      "connected": true
    },
    "telephony": {
      "networkCountryIso": "us",
      "carrierName": "Android"
    }
  },
  "location": {
    "latitude": 51.431534,
    "Longitude": -2.622353
  }
}
```

The `location` and `metadata` fields are required when their values are `true` in the output. The `alias` and `identifier` fields are optional and provided when the client uses the Ping SDKs.

* `alias`

  A friendly name for the device often derived from the make and model.

* `identifier`

  A unique identifier string that can be used to later match the device.

* `location`

  Latitude and longitude of the device.

* `metadata`

  Refer to the example response data for details.

Class to import in scripts: `org.forgerock.openam.authentication.callbacks.DeviceProfileCallback`

Learn more in [DeviceProfileCallback](../_attachments/apidocs/org/forgerock/openam/authentication/callbacks/DeviceProfileCallback.html).

## DeviceSigningVerifierCallback

Verifies the signature of data from a registered device.

| Callback output field | Description                                                                                                               |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| `userId`              | The ID of the user authenticating, if already determined by the authentication journey.                                   |
| `challenge`           | A string containing the challenge the client should sign with the private key and return for validation.                  |
| `title`               | A string containing an optional title to display when requesting biometric authentication to access the key pair.         |
| `subtitle`            | A string containing an optional subtitle to display when requesting biometric authentication to access the key pair.      |
| `description`         | A string containing optional descriptive text to display when requesting biometric authentication to access the key pair. |
| `timeout`             | An integer specifying the number of seconds to wait for device signing to complete before reporting a timeout error.      |

Example response data

```json
{
  "authId": "...",
  "callbacks": [
    {
      "type": "DeviceSigningVerifierCallback",
      "output": [
        {
          "name": "userId",
          "value": ""
        },
        {
          "name": "challenge",
          "value": "Kc4dc14on98DYFzr5SoP2n3TC/JWAcAqTJMjCM+T27Y="
        },
        {
          "name": "title",
          "value": "Authentication required"
        },
        {
          "name": "subtitle",
          "value": "Cryptography device binding"
        },
        {
          "name": "description",
          "value": "Please complete with biometric to proceed"
        },
        {
          "name": "timeout",
          "value": 60
        }
      ],
      "input": [
        {
          "name": "IDToken1jws",
          "value": ""
        },
        {
          "name": "IDToken1clientError",
          "value": ""
        }
      ]
    }
  ]
}
```

The client device should perform the following high-level steps to fulfill this callback:

1. Generate a JSON web token (JWT) that has the ID of the user in the subject (`sub`) field) and the original value of the `challenge`.

   For example:

   ```
   {
       "sub": "id=bjensen,ou=user,dc=am,dc=example,dc=com",
       "challenge": "6IBkTEPcMQ0xCghIclmDLost2ssGO5cPDs0AjUhmDTo="
   }
   ```

2. Sign the JWT using the RS512 algorithm to create a JSON Web Signature (JWS).

3. Complete the callback, returning the JWS.

The server verifies the signature against the stored public key.

Example response data

```json
{
  "authId": "...",
  "callbacks": [
    {
      "type": "DeviceSigningVerifierCallback",
      "output": [...],
      "input": [
        {
          "name": "IDToken1jws",
          "value": "eyJhbGciOiJIUzI1NiI....JV_adQssw5cB6aDS6m_kwIiw"
        },
        {
          "name": "IDToken1clientError",
          "value": ""
        }
      ]
    }
  ]
}
```

Class to import in scripts: `org.forgerock.openam.authentication.callbacks.DeviceSigningVerifierCallback`

Learn more in [DeviceSigningVerifierCallback](../_attachments/apidocs/org/forgerock/openam/authentication/callbacks/DeviceSigningVerifierCallback.html).

## HiddenValueCallback

Provides form values that are to remain hidden from the user.

Example

```json
{
  "callbacks": [{
    "type": "HiddenValueCallback",
    "output": [{
      "name": "value",
      "value": "6186c911-b3be-4dbc-8192-bdf251392072"
    }, {
      "name": "id",
      "value": "jwt"
    }],
    "input": [{
      "name": "IDToken1",
      "value": "jwt"
    }]
  }]
}
```

Class to import in scripts: `com.sun.identity.authentication.callbacks.HiddenValueCallback`

Learn more in [HiddenValueCallback](../_attachments/apidocs/com/sun/identity/authentication/callbacks/HiddenValueCallback.html).

## IdPCallback

Collects the result of a native OAuth 2.0 or OIDC request to a social identity provider.

The [Social Provider Handler node](https://docs.pingidentity.com/auth-node-ref/latest/social-provider-handler.html) returns this callback when its Client Type is set to `NATIVE`.

The output provides the information required to perform the request. Clients built using the Ping SDKs for Android or iOS use this to authenticate to the social identity provider with the mobile OS native APIs.

| Callback output field | Description                                                                                                               |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| `acrValues`           | An array containing the Authentication Context Class Reference values for the native authentication request.              |
| `clientId`            | A string containing the identifier for the native authentication request.                                                 |
| `nonce`               | A string containing the nonce for the native authentication request.                                                      |
| `provider`            | A string containing a name for the provider.                                                                              |
| `redirectUri`         | A string containing the redirection URI for the native authentication request.                                            |
| `request`             | A string containing the Request Object for the native authentication request.                                             |
| `requestUri`          | A string containing a URL that references a resource containing the Request Object for the native authentication request. |
| `scopes`              | An array containing the scopes for the native authentication request.                                                     |

Example

```json
{
  "callbacks": [{
    "type": "IdPCallback",
    "output": [{
      "name": "provider",
      "value": "amazon"
    }, {
      "name": "clientId",
      "value": "amzn1.application-oa2-client.f0c11aa1f8504f8da26a346ccc55a39e"
    }, {
      "name": "redirectUri",
      "value": "https://localhost:8443/am"
    }, {
      "name": "scopes",
      "value": ["profile"]
    }, {
      "name": "nonce",
      "value": ""
    }, {
      "name": "acrValues",
      "value": []
    }, {
      "name": "request",
      "value": ""
    }, {
      "name": "requestUri",
      "value": ""
    }],
    "input": [{
      "name": "IDToken1token",
      "value": ""
    }, {
      "name": "IDToken1token_type",
      "value": ""
    }]
  }]
}
```

In the input, return a JWT `id_token`, `access_token` or authorization code for the token, and `id_token`, `access_token` or `authorization_code` for the token type.

Class to import in scripts: `org.forgerock.openam.authentication.callbacks.IdPCallback`

Learn more in [IdPCallback](../_attachments/apidocs/org/forgerock/openam/authentication/callbacks/IdPCallback.html).

## KbaCreateCallback

Collects knowledge-based authentication (KBA) answers to questions defined in the user profile, or user-defined question and answer pairs.

Example

```json
{
  "callbacks": [{
    "type": "KbaCreateCallback",
    "output": [{
      "name": "prompt",
      "value": "Select a security question"
    }, {
      "name": "predefinedQuestions",
      "value": ["What's your favorite color?"]
    }],
    "input": [{
      "name": "IDToken1question",
      "value": ""
    }, {
      "name": "IDToken1answer",
      "value": ""
    }]
  }]
}
```

In the input, return an empty `IDTokenNumberquestion` value when `IDTokenNumberanswer` corresponds to `predefinedQuestions[Number]`. For user-provided questions, return both.

Class to import in scripts: `org.forgerock.openam.authentication.callbacks.KbaCreateCallback`

Learn more in [KbaCreateCallback](../_attachments/apidocs/org/forgerock/openam/authentication/callbacks/KbaCreateCallback.html).

## NameCallback

Collects a string entered by the user, such as a username.

| Callback output field | Description                                                                                                                                                                                                                                                                                                                                                       |
| --------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `prompt`              | A string containing the description of the information required from the user.                                                                                                                                                                                                                                                                                    |
| `autocompleteValues`  | An array of strings containing autocomplete values. These values are used by the browser to provide autofill suggestions to the user when they're prompted for their username.This output field is omitted unless the [Platform Username node](https://docs.pingidentity.com/auth-node-ref/latest/platform-username.html) is configured with autocomplete values. |

Example

```json
{
  "callbacks": [
    {
      "type": "NameCallback",
      "output": [
        {
          "name": "prompt",
          "value": "User Name"
        },
        {
          "name": "autocompleteValues",
          "value": ["username", "webauthn"]
        }
      ],
      "input": [
        {
          "name": "IDToken1",
          "value": ""
        }
      ]
    }
  ]
}
```

Class to import in scripts: `javax.security.auth.callback.NameCallback`

Learn more in [NameCallback](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/javax/security/auth/callback/NameCallback.html).

## NumberAttributeInputCallback

Collects a numeric attribute, such as size or age.

The [Attribute Collector node](https://docs.pingidentity.com/auth-node-ref/latest/attribute-collector.html) uses this to apply policies and validate the response.

| Callback output field | Description                                                                                                                                                                                                                                                                                                                                                                                               |
| --------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `failedPolicies`      | An array of JSON objects describing validation policies that the input failed. The object is empty until the input is provided and validation fails.                                                                                                                                                                                                                                                      |
| `name`                | A string containing the name of the attribute in the user profile.                                                                                                                                                                                                                                                                                                                                        |
| `policies`            | An array of JSON objects describing [validation policies](../idm-objects/policies.html) the input must pass. An empty JSON object if the node does not require validation.                                                                                                                                                                                                                                |
| `prompt`              | A string containing the description of the information required from the user.                                                                                                                                                                                                                                                                                                                            |
| `required`            | A boolean indicating whether input is required for this attribute.                                                                                                                                                                                                                                                                                                                                        |
| `validateOnly`        | When the node requires validation, this boolean indicates whether to apply validation policies only, or to validate the input and continue to the next node. When `true`, the node only performs input validation and does not continue to the next node.When `true`, this lets the UI validate input as the user types instead of validating the input once and continuing the journey to the next node. |
| `value`               | A string containing a default value for the attribute, if required.                                                                                                                                                                                                                                                                                                                                       |

In the input, return the value and a boolean to set `validateOnly`.

Class to import in scripts: `org.forgerock.openam.authentication.callbacks.NumberAttributeInputCallback`

Learn more in [NumberAttributeInputCallback](../_attachments/apidocs/org/forgerock/openam/authentication/callbacks/NumberAttributeInputCallback.html).

## PasswordCallback

Collects a password value.

Example

```json
{
  "callbacks": [{
    "type": "PasswordCallback",
    "output": [{
      "name": "prompt",
      "value": "Password"
    }],
    "input": [{
      "name": "IDToken1",
      "value": ""
    }]
  }]
}
```

Class to import in scripts: `javax.security.auth.callback.PasswordCallback`

Learn more in [PasswordCallback](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/javax/security/auth/callback/PasswordCallback.html).

## PingOneProtectEvaluationCallback

Instructs the client to return the data captured by the [PingOne Signals (Protect) SDK](https://docs.pingidentity.com/pingone/threat_protection_using_pingone_protect/p1_protect_signals_sdk.html) so that a risk evaluation can be completed.

| Callback output field | Description                                                                                        |
| --------------------- | -------------------------------------------------------------------------------------------------- |
| `pauseBehavioralData` | A boolean indicating whether to stop collecting behavioral data after returning the existing data. |

Example

```json
{
  "callbacks":[
    {
      "type":"PingOneProtectEvaluationCallback",
      "output":[
        {
          "name":"pauseBehavioralData",
          "value":true
        }
      ],
      "input":[
        {
          "name":"IDToken1signals",
          "value":""
        },
        {
          "name":"IDToken1clientError",
          "value":""
        }
      ]
    }
  ]
}
```

In the input:

* In `IDToken1signals`, return the data captured by the PingOne Signals SDK.

* In `IDToken1clientError`, return an empty string to signal success, or an error string to indicate that the client was unable to process the request.

- Class to import

  `org.forgerock.openam.authentication.callbacks.PingOneProtectEvaluationCallback`

Learn more in [PingOneProtectEvaluationCallback](../_attachments/apidocs/org/forgerock/openam/authentication/callbacks/PingOneProtectEvaluationCallback.html).

## PingOneProtectInitializeCallback

Instructs the client to initialize the [PingOne Signals (Protect) SDK](https://docs.pingidentity.com/pingone/threat_protection_using_pingone_protect/p1_protect_signals_sdk.html) to gather information during a transaction.

| Callback output field      | Description                                                                                                                                         |
| -------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| `envId`                    | A string containing the PingOne environment ID.                                                                                                     |
| `consoleLogEnabled`        | A boolean indicating whether to output SDK log messages to the developer console.                                                                   |
| `deviceAttributesToIgnore` | An array of device attributes to ignore when collecting device signals.                                                                             |
| `customHost`               | A string containing a custom host URL from which to retrieve a "Pong" token.Not currently used.                                                     |
| `lazyMetadata`             | A boolean indicating whether to calculate metadata on demand.When `false`, metadata is calculated automatically after initialization.               |
| `behavioralDataCollection` | A boolean indicating whether to collect behavioral data.                                                                                            |
| `disableHub`               | A boolean indicating whether the client stores device data in the browser's localStorage only.When `false`, the client uses an iframe if supported. |
| `deviceKeyRsyncIntervals`  | An integer indicating the number of days that device attestation can rely upon the device fallback key.                                             |
| `enableTrust`              | A boolean indicating whether to tie the device payload to a non-extractable crypto key stored in the browser for content authenticity verification. |
| `disableTags`              | A boolean indicating whether to collect tag data.                                                                                                   |

Example

```json
{
  "type":"PingOneProtectInitializeCallback",
  "output":[
    {
      "name":"envId",
      "value":"3072206d-c6ce-4c19-a366-f87e972c7cc3"
    },
    {
      "name":"consoleLogEnabled",
      "value":false
    },
    {
      "name":"deviceAttributesToIgnore",
      "value":[
        "field1",
        "field2"
      ]
    },
    {
      "name":"customHost",
      "value":""
    },
    {
      "name":"lazyMetadata",
      "value":false
    },
    {
      "name":"behavioralDataCollection",
      "value":true
    },
    {
      "name":"deviceKeyRsyncIntervals",
      "value":14
    },
    {
      "name":"enableTrust",
      "value":false
    },
    {
      "name":"disableTags",
      "value":false
    },
    {
      "name":"disableHub",
      "value":false
    }
  ],
  "input":[
    {
      "name":"IDToken1clientError",
      "value":""
    }
  ]
}
```

In the input `IDToken1clientError` field, return an empty string to signal success, or define any error string to indicate initialization of the SDK failed.

* Class to import

  `org.forgerock.openam.authentication.callbacks.PingOneProtectInitializeCallback`

Learn more in [PingOneProtectInitializeCallback](../_attachments/apidocs/org/forgerock/openam/authentication/callbacks/PingOneProtectInitializeCallback.html).

## SelectIdPCallback

Collects a choice of an enabled social identity provider or local authentication.

The [Select Identity Provider node](https://docs.pingidentity.com/auth-node-ref/latest/select-identity-provider.html) returns this callback when multiple social identity providers are enabled, or when Local Authentication is enabled alongside at least one provider.

In the input, return the provider name, such as `amazon` or `localAuthentication`.

Example

```json
{
  "callbacks": [{
    "type": "SelectIdPCallback",
    "output": [{
      "name": "providers",
      "value": [{
        "provider": "amazon",
        "uiConfig": {
          "buttonCustomStyle": "background: linear-gradient(to bottom, #f7e09f 15%,#f5c646 85%);color: black;border-color: #b48c24;",
          "buttonImage": "",
          "buttonClass": "fa-amazon",
          "buttonDisplayName": "Amazon",
          "buttonCustomStyleHover": "background: linear-gradient(to bottom, #f6c94e 15%,#f6c94e 85%);color: black;border-color: #b48c24;"
        }
      }, {
        "provider": "google",
        "uiConfig": {
          "buttonImage": "images/g-logo.png",
          "buttonCustomStyle": "background-color: #fff; color: #757575; border-color: #ddd;",
          "buttonClass": "",
          "buttonCustomStyleHover": "color: #6d6d6d; background-color: #eee; border-color: #ccc;",
          "buttonDisplayName": "Google"
        }
      }, {
        "provider": "localAuthentication"
      }]
    }, {
      "name": "value",
      "value": ""
    }],
    "input": [{
      "name": "IDToken1",
      "value": ""
    }]
  }]
}
```

Class to import in scripts: `org.forgerock.openam.authentication.callbacks.SelectIdPCallback`

Learn more in [SelectIdPCallback](../_attachments/apidocs/org/forgerock/openam/authentication/callbacks/SelectIdPCallback.html).

## StringAttributeInputCallback

Collects string attributes, such as city names, telephone numbers, and postcodes.

The [Attribute Collector node](https://docs.pingidentity.com/auth-node-ref/latest/attribute-collector.html) uses this instead of a [TextInputCallback](#TextInputCallback) to apply policies and validate the response.

| Callback output field | Description                                                                                                                                                                                                                                                                                                                                                                                               |
| --------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `failedPolicies`      | An array of JSON objects describing validation policies that the input failed. The object is empty until the input is provided and validation fails.                                                                                                                                                                                                                                                      |
| `name`                | A string containing the name of the attribute in the user profile.                                                                                                                                                                                                                                                                                                                                        |
| `policies`            | An array of JSON objects describing [validation policies](../idm-objects/policies.html) the input must pass. An empty JSON object if the node does not require validation.                                                                                                                                                                                                                                |
| `prompt`              | A string containing the description of the information required from the user.                                                                                                                                                                                                                                                                                                                            |
| `required`            | A boolean indicating whether input is required for this attribute.                                                                                                                                                                                                                                                                                                                                        |
| `validateOnly`        | When the node requires validation, this boolean indicates whether to apply validation policies only, or to validate the input and continue to the next node. When `true`, the node only performs input validation and does not continue to the next node.When `true`, this lets the UI validate input as the user types instead of validating the input once and continuing the journey to the next node. |
| `value`               | A string containing a default value for the attribute, if required.                                                                                                                                                                                                                                                                                                                                       |

Example

```json
{
  "callbacks": [{
    "type": "StringAttributeInputCallback",
    "output": [{
      "name": "name",
      "value": "givenName"
    }, {
      "name": "prompt",
      "value": "First Name"
    }, {
      "name": "required",
      "value": true
    }, {
      "name": "policies",
      "value": {
        "policyRequirements": ["REQUIRED", "VALID_TYPE"],
        "fallbackPolicies": null,
        "name": "givenName",
        "policies": [{
          "policyRequirements": ["REQUIRED"],
          "policyId": "required"
        }, {
          "policyRequirements": ["VALID_TYPE"],
          "policyId": "valid-type",
          "params": {
            "types": ["string"]
          }
        }],
        "conditionalPolicies": null
      }
    }, {
      "name": "failedPolicies",
      "value": []
    }, {
      "name": "validateOnly",
      "value": false
    }, {
      "name": "value",
      "value": ""
    }],
    "input": [{
      "name": "IDToken1",
      "value": ""
    }, {
      "name": "IDToken1validateOnly",
      "value": false
    }]
  }]
}
```

When input validation is not required, the `policies` contain an empty object:

```json
{
  "name": "policies",
  "value": {}
}
```

In the input, return the value and a boolean to set `validateOnly`.

Class to import in scripts: `org.forgerock.openam.authentication.callbacks.StringAttributeInputCallback`

Learn more in [StringAttributeInputCallback](../_attachments/apidocs/org/forgerock/openam/authentication/callbacks/StringAttributeInputCallback.html).

## TermsAndConditionsCallback

Displays the current terms and conditions and collects the user's agreement to them.

Example

```json
{
  "callbacks": [
    {
      "type": "TermsAndConditionsCallback",
      "output": [
        {
          "name": "version",
          "value": "0.0"
        },
        {
          "name": "terms",
          "value": "Terms and conditions text that you must agree to."
        },
        {
          "name": "createDate",
          "value": "2022-10-28T04:20:11.320Z"
        }
      ],
      "input": [
        {
          "name": "IDToken1",
          "value": false
        }
      ]
    }
  ]
}
```

In the input, return `true` if the user agrees to the terms and conditions.

Class to import in scripts: `org.forgerock.openam.authentication.callbacks.TermsAndConditionsCallback`

Learn more in [TermsAndConditionsCallback](../_attachments/apidocs/org/forgerock/openam/authentication/callbacks/TermsAndConditionsCallback.html).

## TextInputCallback

Collects text input from the user.

Example

```json
{
  "callbacks": [{
    "type": "TextInputCallback",
    "output": [{
      "name": "prompt",
      "value": "Provide a nickname for this account"
    }],
    "input": [{
      "name": "IDToken1",
      "value": ""
    }]
  }]
}
```

Class to import in scripts: `javax.security.auth.callback.TextInputCallback`

Learn more in [TextInputCallback](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/javax/security/auth/callback/TextInputCallback.html).

## ValidatedCreatePasswordCallback

Collects a password value.

The [Platform Password node](https://docs.pingidentity.com/auth-node-ref/latest/platform-password.html) uses this instead of a [PasswordCallback](#PasswordCallback) to apply policies and validate the response.

| Callback output field | Description                                                                                                                                                                                                                                                                                                                                                                                              |
| --------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `policies`            | An array of objects describing [validation policies](../idm-objects/policies.html) the input must pass. An empty JSON object if the node doesn't require validation.                                                                                                                                                                                                                                     |
| `failedPolicies`      | An array of JSON objects describing validation policies that the input failed. The object is empty until the input is provided and validation fails.                                                                                                                                                                                                                                                     |
| `validateOnly`        | When the node requires validation, this boolean indicates whether to apply validation policies only, or to validate the input and continue to the next node. When `true`, the node only performs input validation and doesn't continue to the next node.When `true`, this lets the UI validate input as the user types instead of validating the input once and continuing the journey to the next node. |
| `prompt`              | A string containing the description of the information required from the user.                                                                                                                                                                                                                                                                                                                           |

Example

```json
{
  "callbacks": [{
    "type": "ValidatedCreatePasswordCallback",
    "output": [{
      "name": "echoOn",
      "value": false
    }, {
      "name": "policies",
      "value": {
        "policyRequirements": ["VALID_TYPE", "MIN_LENGTH", "AT_LEAST_X_CAPITAL_LETTERS", "AT_LEAST_X_NUMBERS", "CANNOT_CONTAIN_OTHERS"],
        "fallbackPolicies": null,
        "name": "password",
        "policies": [{
          "policyRequirements": ["VALID_TYPE"],
          "policyId": "valid-type",
          "params": {
            "types": ["string"]
          }
        }, {
          "policyId": "minimum-length",
          "params": {
            "minLength": 8
          },
          "policyRequirements": ["MIN_LENGTH"]
        }, {
          "policyId": "at-least-X-capitals",
          "params": {
            "numCaps": 1
          },
          "policyRequirements": ["AT_LEAST_X_CAPITAL_LETTERS"]
        }, {
          "policyId": "at-least-X-numbers",
          "params": {
            "numNums": 1
          },
          "policyRequirements": ["AT_LEAST_X_NUMBERS"]
        }, {
          "policyId": "cannot-contain-others",
          "params": {
            "disallowedFields": ["userName", "givenName", "sn"]
          },
          "policyRequirements": ["CANNOT_CONTAIN_OTHERS"]
        }],
        "conditionalPolicies": null
      }
    }, {
      "name": "failedPolicies",
      "value": []
    }, {
      "name": "validateOnly",
      "value": false
    }, {
      "name": "prompt",
      "value": "Password"
    }],
    "input": [{
      "name": "IDToken1",
      "value": ""
    }, {
      "name": "IDToken1validateOnly",
      "value": false
    }]
  }]
}
```

In the input, return the value and a boolean to set `validateOnly`.

Class to import in scripts: `org.forgerock.openam.authentication.callbacks.ValidatedPasswordCallback`

Learn more in [ValidatedPasswordCallback](../_attachments/apidocs/org/forgerock/openam/authentication/callbacks/ValidatedPasswordCallback.html).

## ValidatedCreateUsernameCallback

Collects a username.

The [Platform Username node](https://docs.pingidentity.com/auth-node-ref/latest/platform-username.html) uses this instead of a [NameCallback](#NameCallback) to apply policies and validate the response.

| Callback output field | Description                                                                                                                                                                                                                                                                                                                                                                                              |
| --------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `policies`            | An array of objects describing [validation policies](../idm-objects/policies.html) the input must pass. An empty JSON object if the node doesn't require validation.                                                                                                                                                                                                                                     |
| `failedPolicies`      | An array of JSON objects describing validation policies that the input failed. The object is empty until the input is provided and validation fails.                                                                                                                                                                                                                                                     |
| `validateOnly`        | When the node requires validation, this boolean indicates whether to apply validation policies only, or to validate the input and continue to the next node. When `true`, the node only performs input validation and doesn't continue to the next node.When `true`, this lets the UI validate input as the user types instead of validating the input once and continuing the journey to the next node. |
| `prompt`              | A string containing the description of the information required from the user.                                                                                                                                                                                                                                                                                                                           |
| `autocompleteValues`  | An array of strings containing autocomplete values. These values are used by the browser to provide autofill suggestions to the user when they're prompted for their username.This output field is omitted unless the [Platform Username node](https://docs.pingidentity.com/auth-node-ref/latest/platform-username.html) is configured with autocomplete values.                                        |

Example

```json
{
  "callbacks": [
    {
      "type": "ValidatedCreateUsernameCallback",
      "output": [
        {
          "name": "policies",
          "value": {
            "policyRequirements": ["VALID_USERNAME", "CANNOT_CONTAIN_CHARACTERS", "MIN_LENGTH", "MAX_LENGTH"],
            "fallbackPolicies": null,
            "name": "userName",
            "policies": [
              {
                "policyId": "valid-username",
                "policyRequirements": ["VALID_USERNAME"]
              },
              {
                "policyId": "cannot-contain-characters",
                "params": {
                  "forbiddenChars": ["/"]
                },
                "policyRequirements": ["CANNOT_CONTAIN_CHARACTERS"]
              },
              {
                "policyId": "minimum-length",
                "params": {
                  "minLength": 1
                },
                "policyRequirements": ["MIN_LENGTH"]
              },
              {
                "policyId": "maximum-length",
                "params": {
                  "maxLength": 255
                },
                "policyRequirements": ["MAX_LENGTH"]
              }
            ],
            "conditionalPolicies": null
          }
        },
        {
          "name": "failedPolicies",
          "value": []
        },
        {
          "name": "validateOnly",
          "value": false
        },
        {
          "name": "prompt",
          "value": "Username"
        },
        {
          "name": "autocompleteValues",
          "value": ["username", "webauthn"]
        }
      ],
      "input": [
        {
          "name": "IDToken1",
          "value": ""
        },
        {
          "name": "IDToken1validateOnly",
          "value": false
        }
      ]
    }
  ]
}
```

In the input, return the value and a boolean to set `validateOnly`.

Class to import in scripts: `org.forgerock.openam.authentication.callbacks.ValidatedUsernameCallback`

Learn more in [ValidatedUsernameCallback](../_attachments/apidocs/org/forgerock/openam/authentication/callbacks/ValidatedUsernameCallback.html).

---

---
title: Introduction to authentication
description: Learn authentication concepts including nodes, journeys, sessions, and multi-factor authentication
component: pingoneaic
page_id: pingoneaic:am-authentication:authn-introduction-authn
canonical_url: https://docs.pingidentity.com/pingoneaic/am-authentication/authn-introduction-authn.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Authentication", "Multi-factor Authentication (MFA)"]
page_aliases: ["authentication-guide:authn-introduction-authn.adoc"]
section_ids:
  intro-nodes-trees: Nodes and journeys
  intro-sessions: Sessions
  about-mfa: Multi-factor authentication
---

# Introduction to authentication

*Authentication* is the act of confirming a user's identity, for example, by providing a set of credentials.

As part of an access management strategy, authentication is tightly coupled with authorization; usually, not only is it important to confirm that a user is who they say they are, but also to ensure that they can only access a subset of information.

Consider a user who wants to access an online shop. As the owner of the shop, you want to ensure the user identity is confirmed (as it's tied to their shipping and email addresses and payment information). You also want to ensure that they can only access their own information.

You can deploy a web agent on the web server hosting the online shop. The agent redirects the user's request to an Advanced Identity Cloud login page, where the user enters their credentials, such as username and password. Advanced Identity Cloud determines who the user is, and whether the user has the right to access the protected page. Advanced Identity Cloud then redirects the user back to the protected page with authorization credentials that can be verified by the agent. The agent allows the user authorized by Advanced Identity Cloud to access the page.

In the same way, you can also use Advanced Identity Cloud to protect physical devices connected on the Internet of Things (IoT). For example, a delivery van tracking system could have its proxying gateway authenticate to a brokering system using an X.509 certificate to allow it to enable an HTTPS protocol and then connect to sensors in its delivery trucks. If the X.509 certificate is valid, the brokering system can monitor a van's fuel consumption, speed, mileage, and overall engine condition to maximize each van's operating efficiency.

## Nodes and journeys

Advanced Identity Cloud implements authentication with *authentication nodes and journeys*.

Advanced Identity Cloud provides several different authentication nodes. You can also develop your own nodes based on your authentication requirements.

You connect nodes to create a journey that guides users through the authentication process.

Learn more in [Nodes and journeys](auth-nodes-and-journeys.html).

## Sessions

Advanced Identity Cloud creates a journey session to track the user's progress through an authentication journey. After the user has authenticated, Advanced Identity Cloud creates an authenticated session to manage the user's access to resources.

Learn more in [Sessions](../am-sessions/preface.html).

## Multi-factor authentication

*Multi-factor authentication* (MFA) is an authentication technique that requires users to provide multiple forms of identification when logging in to AM.

Multi-factor authentication provides a more secure method for users to access their accounts with the help of a *device*.

Learn more in [Multi-factor authentication (MFA)](authn-mfa.html).

---

---
title: Limitations of passwordless push authentication
description: Understand security limitations when using push notifications alone for passwordless authentication
component: pingoneaic
page_id: pingoneaic:am-authentication:mfa-push-passwordless-limitations
canonical_url: https://docs.pingidentity.com/pingoneaic/am-authentication/mfa-push-passwordless-limitations.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Authentication", "Multi-factor Authentication (MFA)"]
page_aliases: ["authentication-guide:mfa-push-passwordless-limitations.adoc"]
---

# Limitations of passwordless push authentication

When authenticating to a passwordless push authentication journey, the user enters their user ID, but not their password. Advanced Identity Cloud sends a push notification to their device to complete the authentication.

Be aware of the following limitations when you implement passwordless push authentication:

* Unsolicited push messages can be sent to a user's registered device by anyone who knows (or is able to guess) their user ID.

* If a malicious user attempts to authenticate by using push at the same time as a legitimate user, the legitimate user might unintentionally approve the malicious attempt. This is because push notifications only contain the username and issuer in the text, and it's not easy to determine which notification relates to which authentication attempt.

Consider using push notifications as part of MFA, and not on their own.

---

---
title: List latest node definitions
description: Retrieve current node definitions including versions, schemas, and configurations using REST
component: pingoneaic
page_id: pingoneaic:am-authentication:list-latest-node-definitions
canonical_url: https://docs.pingidentity.com/pingoneaic/am-authentication/list-latest-node-definitions.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Authentication", "Nodes &amp; Trees", "Journeys", "REST API"]
---

# List latest node definitions

Use the `listLatestNodeDefinitions` action on the `realm-config/authentication/authenticationtrees/nodes` endpoint to get the most up-to-date definitions for all available nodes. This information is useful when creating or updating journeys because it provides the current node details.

This endpoint returns a list of node definitions for the *latest* version of each node, including the following information:

* Node version

* Node schema

  The node schema includes the configuration property type, which is required when creating [ESV variables](../tenants/esvs.html#variable-expression-types) to use in nodes. Make sure the ESV `expressionType` matches the property `type`.

  For example, to create an ESV variable for the Minimum Password Length property in the Identity Store Decision node, you'd set the ESV `expressionType` to `int` to match the property type returned in the node schema, as shown in the example response below.

* Configuration template

* Node outcomes

The following example shows a partial response for the `IdentityStoreDecisionNode`:

```bash
$ curl \
--request POST \
--header "Authorization: Bearer <access-token>" \
--header "Content-Type: application/json" \
--header "Accept-API-Version: protocol=2.1,resource=3.0" \
"https://<tenant-env-fqdn>/json/realms/root/realms/alpha/realm-config/authentication/authenticationtrees/nodes?_action=listLatestNodeDefinitions"
{
    "result": {
      ...
        "IdentityStoreDecisionNode": {
            "_id": "IdentityStoreDecisionNode",
            "name": "Identity Store Decision",
            "collection": true,
            "tags": [
                "basic authn",
                "basic authentication"
            ],
            "metadata": {
                "tags": [
                    "basic authn",
                    "basic authentication"
                ]
            },
            "help": "Verifies that the username and password values exist in the Identity Store configured in the realm.",
            "version": "1.0",
            "schema": {
                "type": "object",
                "properties": {
                    "minimumPasswordLength": {
                        "title": "Minimum Password Length",
                        "description": "When the password is changed the node will reject passwords which are shorter than this value. If this value is set to 0 the minimum password length is not checked by the node.",
                        "propertyOrder": 200,
                        "type": "integer",
                        "exampleValue": "",
                        "default": 8
                    },
                    "useUniversalIdForUsername": {
                        "title": "Username as Universal Identifier",
                        "description": "Set to true to allow the username to be represented by the user's universal identifier (uuid).  If set to false, the username representation will remain unchanged.",
                        "propertyOrder": 300,
                        "type": "boolean",
                        "exampleValue": "",
                        "default": false
                    },
                    "mixedCaseForPasswordChangeMessages": {
                        "title": "Use mixed case for password change messages",
                        "description": "Defines whether password change messages returned are in mixed (sentence) case or uppercase. Default: false",
                        "propertyOrder": 400,
                        "type": "boolean",
                        "exampleValue": "",
                        "default": false
                    }
                },
                "required": [
                    "minimumPasswordLength",
                    "useUniversalIdForUsername",
                    "mixedCaseForPasswordChangeMessages"
                ]
            },
            "template": {
                "useUniversalIdForUsername": false,
                "minimumPasswordLength": 8,
                "mixedCaseForPasswordChangeMessages": false
            },
            "outcomes": [
                {
                    "id": "TRUE",
                    "displayName": "True"
                },
                {
                    "id": "FALSE",
                    "displayName": "False"
                },
                {
                    "id": "LOCKED",
                    "displayName": "Locked"
                },
                {
                    "id": "CANCELLED",
                    "displayName": "Cancelled"
                },
                {
                    "id": "EXPIRED",
                    "displayName": "Expired"
                }
            ]
        },
      ...
}
```

---

---
title: List registered devices over REST
description: Query REST API to retrieve lists of registered MFA devices by type for a user
component: pingoneaic
page_id: pingoneaic:am-authentication:authn-mfa-list-devices
canonical_url: https://docs.pingidentity.com/pingoneaic/am-authentication/authn-mfa-list-devices.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Authentication", "Multi-factor Authentication (MFA)"]
section_ids:
  authn-mfa-list-oath-devices: List OATH devices
  authn-mfa-list-push-devices: List push devices
  authn-mfa-list-webauthn-devices: List WebAuthn devices
  authn-mfa-list-bound-devices: List bound devices
---

# List registered devices over REST

Advanced Identity Cloud provides a REST API to retrieve information about MFA devices registered to a user.

When making a REST API call, specify the realm in the path component of the endpoint. You must specify the entire hierarchy of the realm. Prefix each realm in the hierarchy with the `realms/` keyword. For example, `/realms/root/realms/alpha`.

The following examples assume that you have [obtained an access token](../developer-docs/authenticate-to-rest-api-with-access-token.html) with the appropriate scopes.

|   |                                                                                                          |
| - | -------------------------------------------------------------------------------------------------------- |
|   | The API calls reference the user by `_id`. You can get this ID from the raw JSON for the user's profile. |

## List OATH devices

To retrieve the list of OATH devices registered to a user, query the `users/user/devices/2fa/oath` endpoint.

The following example lists the OATH devices for a user in the `alpha` realm. The user's `_id` in this example is `014c54bd-6078-4639-8316-8ce0e7746fa4`.

```bash
$ curl \
--request GET \
--header "authorization: Bearer access-token" \
'https://<tenant-env-fqdn>/am/json/realms/root/realms/alpha/users/014c54bd-6078-4639-8316-8ce0e7746fa4/devices/2fa/oath?_queryFilter=true'
{
  "result" : [
    {
      "_id" : "ff1db8bf-d2d7-46e1-926a-568b877f87a5",
      "_rev" : "172031596",
      "createdDate": 1749572704744,
      "lastAccessDate": 1749658650801,
      "deviceName" : "OATH Device",
      "uuid" : "ff1db8bf-d2d7-46e1-926a-568b877f87a5",
      "deviceManagementStatus" : false
    }
  ],
  "resultCount" : 1,
  "pagedResultsCookie" : null,
  "totalPagedResultsPolicy" : "NONE",
  "totalPagedResults" : -1,
  "remainingPagedResults" : -1
}
```

## List push devices

To retrieve the list of push devices registered to a user, query the `users/user/devices/2fa/push` endpoint.

The following example lists the push devices for a user in the `alpha` realm. The user's `_id` in this example is `014c54bd-6078-4639-8316-8ce0e7746fa4`.

```bash
$ curl \
--request GET \
--header "authorization: Bearer access-token" \
'https://<tenant-env-fqdn>/am/json/realms/root/realms/alpha/users/014c54bd-6078-4639-8316-8ce0e7746fa4/devices/2fa/push?_queryFilter=true'
{
  "result" : [
    {
      "_id" : "ff1db8bf-d2d7-46e1-926a-568b877f87a5",
      "_rev" : "172031596",
      "createdDate": 1749572704744,
      "lastAccessDate": 1749658650801,
      "deviceName" : "Push Device",
      "uuid" : "ff1db8bf-d2d7-46e1-926a-568b877f87a5",
      "deviceManagementStatus" : false
    }
  ],
  "resultCount" : 1,
  "pagedResultsCookie" : null,
  "totalPagedResultsPolicy" : "NONE",
  "totalPagedResults" : -1,
  "remainingPagedResults" : -1
}
```

## List WebAuthn devices

To return a list of WebAuthn devices registered to a user, query the `users/user/devices/2fa/webauthn` endpoint.

The following example lists the WebAuthn devices for a user in the `alpha` realm. The user's `_id` in this example is `014c54bd-6078-4639-8316-8ce0e7746fa4`.

```bash
$ curl \
--request GET \
--header "authorization: Bearer access-token" \
'https://<tenant-env-fqdn>/am/json/realms/root/realms/alpha/users/014c54bd-6078-4639-8316-8ce0e7746fa4/devices/2fa/webauthn?_queryFilter=true'
{
  "result": [
    {
      "_id": "ff1db8bf-d2d7-46e1-926a-568b877f87a5",
      "_rev": "163664231",
      "createdDate": 1749572704744,
      "lastAccessDate": 1749658650801,
      "credentialId": "XGJpYNYv4AHG9sHHgxFfTw",
      "deviceName": "New Security Key",
      "uuid": "ff1db8bf-d2d7-46e1-926a-568b877f87a5",
      "deviceManagementStatus": false
    }
  ],
  "resultCount": 1,
  "pagedResultsCookie": null,
  "totalPagedResultsPolicy": "NONE",
  "totalPagedResults": -1,
  "remainingPagedResults": -1
}
```

## List bound devices

To return a list of bound devices for a user, query the `users/user/devices/2fa/binding` endpoint. Learn more about binding devices to a user profile in [device binding](https://docs.pingidentity.com/sdks/latest/sdks/use-cases/how-to-bind-devices.html).

The following example lists the bound devices for a user in the `alpha` realm. The user's `_id` in this example is `014c54bd-6078-4639-8316-8ce0e7746fa4`.

```bash
$ curl \
--request GET \
--header "authorization: Bearer access-token" \
'https://<tenant-env-fqdn>/am/json/realms/root/realms/alpha/users/014c54bd-6078-4639-8316-8ce0e7746fa4/devices/2fa/binding?_queryFilter=true'
{
  "result": [
    {
      "_id": "ff1db8bf-d2d7-46e1-926a-568b877f87a5",
      "_rev": "192142989",
      "createdDate": 1749572704744,
      "lastAccessDate": 1749658650801,
      "deviceId": "e2e84b5d2a927abdcb85570bac9701c390a92751",
      "deviceName": "iOS Device",
      "uuid": "ff1db8bf-d2d7-46e1-926a-568b877f87a5",
      "deviceManagementStatus": false
    }
  ],
  "resultCount": 1,
  "pagedResultsCookie": null,
  "totalPagedResultsPolicy": "NONE",
  "totalPagedResults": -1,
  "remainingPagedResults": -1
}
```

---

---
title: Log in over REST
description: Authenticate users over REST by providing credentials or completing callback-based authentication flows
component: pingoneaic
page_id: pingoneaic:am-authentication:login-using-rest
canonical_url: https://docs.pingidentity.com/pingoneaic/am-authentication/login-using-rest.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Authentication", "Callbacks", "REST API"]
page_aliases: ["authentication-guide:login-using-rest.adoc"]
section_ids:
  authenticate-UTF-8: UTF-8 usernames and passwords
  providing-auth-information: Authenticate to specific authentication services
  login-callbacks: Return callback information
---

# Log in over REST

To authenticate using REST, send an HTTP POST request to the `json/authenticate` endpoint. You must specify the realm hierarchy. Prefix each realm in the hierarchy with the `realms/` keyword; for example, `/realms/root/realms/alpha`.

|   |                                                                                                                                                                                                                   |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The `/json/authenticate` endpoint does not support the CRUDPAQ verbs and therefore does not technically satisfy REST architectural requirements. The term *REST-like* describes this endpoint better than *REST*. |

By default, you authenticate using the default authentication service configured for the realm. To override the default, [specify authentication services](#providing-auth-information) and other options in the REST request.

Advanced Identity Cloud supports simple authentication methods, such as providing a username and password, and complex authentication journeys that might involve nested journey evaluations and multi-factor authentication.

For authentication journeys where providing a username and password is sufficient, you can log in by providing these credentials in headers. The following command logs in user `bjensen` with password `Secret12!`:

```bash
$ curl \
--request POST \
--header 'Content-Type: application/json' \
--header 'X-OpenAM-Username: bjensen' \
--header 'X-OpenAM-Password: Secret12!' \
--header 'Accept-API-Version: resource=2.0, protocol=1.0' \
'https://<tenant-env-fqdn>/am/json/realms/root/realms/alpha/authenticate'
{
    "tokenId":"AQIC5wM...TU3OQ*",
    "successUrl": "/enduser/?realm=/alpha",
    "realm":"/alpha"
}
```

This zero page login mechanism works only for username/password authentication.

Note that the POST body is empty. If you submit a POST body, Advanced Identity Cloud interprets the body as a continuation of an existing authentication attempt that uses a supported [callback](#login-callbacks) mechanism. Callback mechanisms support complex authentication journeys, such as those where the user must be redirected to a third party or interact with a device as part of multi-factor authentication.

After successful authentication, Advanced Identity Cloud returns a `tokenId` that applications can present as a cookie value for other operations that require authentication. The `tokenId` is known as the *session token*. For information about how applications can use session tokens, refer to [Session tokens after authentication](rest-using-ssotokens.html).

If `HttpOnly` cookies are enabled, and a client makes a call to the `/json/authenticate` endpoint with a valid SSO token, Advanced Identity Cloud returns the `tokenId` field **empty**. For example:

```json
{
    "tokenId":"",
    "successUrl":"/enduser/?realm=/alpha",
    "realm":"/alpha"
}
```

|   |                                                                                                                                                                                     |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | To authenticate a user without providing them with a session, use the `noSession` parameter. For details, refer to [Authenticate endpoints](authenticate-endpoint-parameters.html). |

## UTF-8 usernames and passwords

To use UTF-8 usernames and passwords in calls to the `/json/authenticate` endpoint, base64-encode the string, then wrap the string as described in [RFC 2047](https://www.rfc-editor.org/info/rfc2047):

```
encoded-word = "=?" charset "?" encoding "?" encoded-text "?="
```

For example, to authenticate using a UTF-8 username, such as `Åström`, follow these steps:

1. Encode the string in base64 format: `w4VzdHLDtm0=`.

2. Wrap the base64-encoded string, as per RFC 2047: `=?UTF-8?B?w4VzdHLDtm0=?=`.

3. Use the result in the `X-OpenAM-Username` header passed to the authentication endpoint as follows:

   ```bash
   $ curl \
   --request POST \
   --header 'Content-Type: application/json' \
   --header 'X-OpenAM-Username: =?UTF-8?B?w4VzdHLDtm0=?=' \
   --header 'X-OpenAM-Password: Secret12!' \
   --header 'Accept-API-Version: resource=2.0, protocol=1.0' \
   'https://<tenant-env-fqdn>/am/json/realms/root/realms/alpha/authenticate'
   {
     "tokenId": "DDZUA0Ellb4bOt...AIwMQ..*",
     "successUrl": "/enduser/?realm=/alpha",
     "realm": "/alpha"
   }
   ```

## Authenticate to specific authentication services

You can provide Advanced Identity Cloud with additional information about how a user is authenticating. For example, you can specify a particular authentication journey, or request a list of the authentication services that would satisfy an authentication condition.

The following example specifies the `Login` journey by using the `authIndexType` and `authIndexValue` parameters:

```bash
$ curl \
--request POST \
--header 'X-OpenAM-Username: bjensen' \
--header 'X-OpenAM-Password: Secret12!' \
--header 'Accept-API-Version: resource=2.0, protocol=1.0' \
'https://<tenant-env-fqdn>/am/json/realms/root/realms/alpha/authenticate?authIndexType=service&authIndexValue=Login'
```

You can replace the `Login` journey with any other journey configured in the realm.

For details about using the `authIndexType` parameter to authenticate to specific services, refer to [Authenticate endpoints](authenticate-endpoint-parameters.html).

## Return callback information

The `/json/authenticate` endpoint supports callback mechanisms to perform complex authentication journeys. When Advanced Identity Cloud needs to return or request information, it returns a JSON object with the authentication step, the authentication identifier, and the related callbacks.

The following callback types are available:

* Read-only callbacks

  Read-only callbacks provide information to the user, such as text messages or the period of time a user must wait before continuing their authentication journey.

* Interactive callbacks

  Interactive callbacks request information from the user; for example, their username and password, or a request that they select between different configured options.

* Backchannel callbacks

  Backchannel callbacks let Advanced Identity Cloud access additional information from the user's request; for example, a specific header or certificate.

Read-only and interactive callbacks have an array of `output` elements that can be displayed to the end user. The JSON returned in an interactive callback includes an array of `input` elements that must be completed and returned to Advanced Identity Cloud. For example:

```json
"output": [
    {
        "name": "prompt",
        "value": " User Name: "
    }
    ],
"input": [
    {
        "name": "IDToken1",
        "value": ""
    }
]
```

The value of some interactive callbacks can be returned as headers, such as the `X-OpenAM-Username` and `X-OpenAM-Password` headers, but most of them must be returned in JSON as a response to the request.

Depending on how complex the authentication journey is, Advanced Identity Cloud could return several callbacks sequentially. Each must be completed and returned to Advanced Identity Cloud until authentication is successful.

The following example shows a request for authentication, and Advanced Identity Cloud's response with the `NameCallback` and `PasswordCallback`:

```bash
$ curl \
--request POST \
--header "Content-Type: application/json" \
--header "Accept-API-Version: resource=2.0, protocol=1.0" \
'https://<tenant-env-fqdn>/am/json/realms/root/realms/alpha/authenticate'
```

```json
{
  "authId": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJvdGsiOiJ...", (1)
  "callbacks": [
    {
      "type": "NameCallback", (2)
      "output": [ (3)
        {
          "name": "prompt",
          "value": " User Name: "
        }
      ],
      "input": [ (4)
        {
          "name": "IDToken1",
          "value": ""
        }
      ]
    },
    {
      "type": "PasswordCallback",
      "output": [
        {
          "name": "prompt",
          "value": " Password: "
        }
      ],
      "input": [
        {
          "name": "IDToken2",
          "value": ""
        }
      ]
    }
  ]
}
```

|       |                                                                                                                                         |
| ----- | --------------------------------------------------------------------------------------------------------------------------------------- |
| **1** | The JWT that uniquely identifies the authentication context to Advanced Identity Cloud.                                                 |
| **2** | The type of callback. It must be listed under [Return callback information](callbacks-supported.html).                                  |
| **3** | The information Advanced Identity Cloud offers about this callback. Usually, this information would be displayed to the user in the UI. |
| **4** | The information Advanced Identity Cloud is requesting. The user must complete the `"value": ""` field with the required information.    |

To respond to a callback, send back the whole JSON object, including the missing values. The following example shows how to respond to the `NameCallback` and `PasswordCallback` callbacks, returning the username (`bjensen`) and the password (`Secret12!`):

```bash
$ curl \
--request POST \
--header "Content-Type: application/json" \
--header "Accept-API-Version: resource=2.0, protocol=1.0" \
--data '{
  "authId":""eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJvdGsiOiJ...",
  "callbacks": [
    {
      "type": "NameCallback",
      "output": [
        {
          "name": "prompt",
          "value": "User Name"
        }
      ],
      "input": [
        {
          "name": "IDToken1",
          "value": "bjensen"
        }
      ],
      "id": 0
    },
    {
      "type": "PasswordCallback",
      "output": [
        {
          "name": "prompt",
          "value": "Password"
        }
      ],
      "input": [
        {
          "name": "IDToken2",
          "value": "Secret12!"
        }
      ],
      "_id": 1
    }
  ],
}' \
'https://<tenant-env-fqdn>_/am/json/realms/root/realms/alpha/authenticate'
{
  "tokenId": "lWY23F4fuC7cu4Fq4GQa5u6drlQ...*",
  "successUrl": "/enduser/?realm=/alpha",
  "realm": "/alpha"
}
```

In complex authentication journeys, Advanced Identity Cloud could send several callbacks sequentially. Each must be completed and returned to Advanced Identity Cloud until authentication is successful.

For details about the callbacks Advanced Identity Cloud can return, refer to [Return callback information](callbacks-supported.html).