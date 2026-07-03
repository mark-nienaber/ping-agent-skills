---
title: AM as a RADIUS client
description: Configure PingAM as a RADIUS client to authenticate users against a RADIUS server using RADIUS Decision and Challenge Collector nodes
component: pingam
version: 8.1
page_id: pingam:am-authentication:radius-client
canonical_url: https://docs.pingidentity.com/pingam/8.1/am-authentication/radius-client.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Authentication", "Journeys", "Nodes &amp; Trees", "RADIUS"]
page_aliases: ["radius-server-guide:radius-auth-module.adoc", "radius-server:radius-auth-module.adoc"]
section_ids:
  configure_radius_authentication: Configure RADIUS authentication
---

# AM as a RADIUS client

The following diagram illustrates the flow of packets between AM (the RADIUS client) and the RADIUS server during an authentication conversation, where the RADIUS server requests a one-time password (OTP) from the user:

![Flows between a user, the authentication nodes, and an external RADIUS server.](_images/radius-auth-nodes-flow.svg)

All conversations between AM and the RADIUS server are secured with a shared secret (mapped to the `am.authentication.nodes.radius.identifier.secret` label).

## Configure RADIUS authentication

AM provides two authentication nodes to handle RADIUS authentication, where AM is acting as a RADIUS client:

* RADIUS Decision node

  The [RADIUS Decision node](https://docs.pingidentity.com/auth-node-ref/8.1/radius-decision.html) performs authentication with the RADIUS server.

  The node performs the following actions:

  * Sends an `Access-Request` packet to the RADIUS server to initiate the authentication request.

  * Handles the RADIUS server's response to determine the outcome of the authentication attempt.

  * Sends additional `Access-Request` packets if the RADIUS server responds with an `Access-Challenge` packet requesting more information from the user.

* RADIUS Challenge Collector node

  The [RADIUS Challenge Collector node](https://docs.pingidentity.com/auth-node-ref/8.1/radius-challenge-collector.html) presents challenge messages to users, such as requesting an OTP, and collects their response.

Create a journey using these nodes to implement RADIUS authentication:

![RADIUS authentication journey](_images/radius-journey.png)

Learn more in the [RADIUS authentication example](https://docs.pingidentity.com/auth-node-ref/8.1/radius-decision.html#example).

---

---
title: AM as a RADIUS server
description: Use PingAM as a RADIUS server to authenticate users from external RADIUS clients through authentication journeys, supporting multi-factor authentication with compatible nodes and callbacks
component: pingam
version: 8.1
page_id: pingam:am-authentication:radius-server
canonical_url: https://docs.pingidentity.com/pingam/8.1/am-authentication/radius-server.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Authentication", "Journeys", "Nodes &amp; Trees", "RADIUS"]
page_aliases: ["radius-server-guide:radius-server-service.adoc", "radius-server:radius-server-service.adoc", "radius-server-guide:radius-limitations.adoc", "radius-server:radius-limitations.adoc"]
section_ids:
  create-auth-journey: Create an authentication journey
  example_journey: Example journey
  configure-radius-server: Configure the RADIUS server service
---

# AM as a RADIUS server

The RADIUS server service provides a RADIUS server within AM. The server authenticates users connecting from external RADIUS clients using an authentication journey.

The following diagram illustrates the flow of packets between an external RADIUS client and AM (the RADIUS server) during an authentication conversation, where the RADIUS server requests a one-time password (OTP) from the user:

![Flows between a user, an external RADIUS client, and AM.](_images/radius-server-flow-multi-factor.svg)

## Create an authentication journey

Create journeys to authenticate users connecting to the RADIUS server from external RADIUS clients. Each RADIUS client configuration in the RADIUS server service must specify a journey to use for authentication.

The RADIUS protocol is more limited than a browser-based HTTP flow. As a result, consider the following constraints when designing your journeys for RADIUS authentication:

* **The first interactive node must be a Page node**

  The RADIUS server requires the username and password together in the initial `Access-Request`. To achieve this, the journey must start with a Page node that contains both a Username Collector and a Password Collector node.

* **Journeys can only include compatible nodes**

  > **Collapse: Compatible nodes**
  >
  > Only the following nodes are compatible with the RADIUS protocol:
  >
  > * [Username Collector node](https://docs.pingidentity.com/auth-node-ref/8.1/am-only/username-collector.html)
  >
  > * [Password Collector node](https://docs.pingidentity.com/auth-node-ref/8.1/am-only/password-collector.html)
  >
  > * [Page node](https://docs.pingidentity.com/auth-node-ref/8.1/page.html)
  >
  > * [DataStore Decision node](https://docs.pingidentity.com/auth-node-ref/8.1/data-store-decision.html)
  >
  > * [Choice Collector node](https://docs.pingidentity.com/auth-node-ref/8.1/choice-collector.html)
  >
  > * [OTP Collector Decision node](https://docs.pingidentity.com/auth-node-ref/8.1/otp-collector-decision.html)
  >
  > * [Scripted Decision node](https://docs.pingidentity.com/auth-node-ref/8.1/scripted-decision.html)
  >
  > * [HOTP Generator node](https://docs.pingidentity.com/auth-node-ref/8.1/hotp-generator.html)
  >
  > * [OTP Email Sender node](https://docs.pingidentity.com/auth-node-ref/8.1/otp-email-sender.html)
  >
  > * [OTP SMS Sender node](https://docs.pingidentity.com/auth-node-ref/8.1/otp-sms-sender.html)
  >
  > * [Inner Tree Evaluator node](https://docs.pingidentity.com/auth-node-ref/8.1/inner-tree-evaluator.html)
  >
  > * [Flow Control node](https://docs.pingidentity.com/auth-node-ref/8.1/inner-tree-evaluator.html)

* **Scripted nodes can only use compatible callbacks**

  > **Collapse: Compatible callbacks**
  >
  > Only the following callbacks are compatible with the RADIUS protocol:
  >
  > * [NameCallback](callbacks-interactive.html#NameCallback)
  >
  > * [PasswordCallback](callbacks-interactive.html#PasswordCallback)
  >
  > * [ChoiceCallback](callbacks-interactive.html#ChoiceCallback)
  >
  > * [ConfirmationCallback](callbacks-interactive.html#ConfirmationCallback)

* **Use Page nodes to customize `Access-Challenge` messages**

  Nodes that prompt for user input, such as the OTP Collector Decision node, send a simple default message (for example, `One-time Password`) in the `Access-Challenge`.

  To provide more context or instructions, place the node inside a Page node. You can then use the Page node's Page Header property to define custom text, which will prepend the default prompt.

  > **Collapse: OTP Example**
  >
  > This example demonstrates how to customize the `Access-Challenge` message displayed when using an OTP Collector Decision node to request an OTP for MFA.
  >
  > 1. Include the OTP Collector Decision node in a Page node as shown in the example journey.
  >
  > 2. Configure the Page node as follows:
  >
  >    * Page Header
  >
  >      `Please check your email, we have sent you a code:`
  >
  > The following message is shown to the user when the RADIUS server sends an `Access-Challenge` packet requesting the OTP:
  >
  > ```none
  > Please check your email, we have sent you a code: One-time Password
  > ```

### Example journey

The following example RADIUS journey collects a username and password, and then sends an OTP email for multi-factor authentication (MFA) if the credentials are valid:

![Example RADIUS server journey with MFA](_images/example-radius-server-journey.png)

## Configure the RADIUS server service

For each RADIUS client that's connecting to the AM RADIUS server, create a separate client configuration within the service, and specify the journey to use for authentication. After you have created the RADIUS clients, you can configure and enable the RADIUS server service.

1. In the AM admin UI, go to Configure > Global Services > RADIUS Server.

2. On the Secondary Configurations tab, click Add a Secondary Configuration.

3. Enter the Name and Client Secret for the RADIUS client configuration, and click Create.

4. Configure the remaining properties for the RADIUS client, ensuring you specify the realm and journey in Handler Class Configuration Properties. For example:

   ```properties
   realm=/alpha
   tree=RADIUS-ClientA-Journey
   ```

   Find more information about these properties in [RADIUS server service](../setup/services-configuration.html#global-radiusserverservice).

5. Click Save Changes.

6. If you have multiple RADIUS clients connecting to the AM RADIUS server, create a client configuration for each one.

   You don't need to configure *all* your RADIUS clients when you configure the RADIUS server service initially. You can add and remove clients over time as needed.

7. Return to the Configuration tab in the RADIUS server service.

8. Configure the properties for the RADIUS server, ensuring you set the Enabled field to `YES` to start the RADIUS server.

   Find more information about these properties in [RADIUS server service](../setup/services-configuration.html#global-radiusserverservice).

9. Click Save Changes.

The RADIUS server starts immediately when you save the configuration if the Enabled field is set to `YES`.

|   |                                                                                                                                                                                                                                                                                                                                           |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | By default, AM caches up to 5,000 RADIUS clients concurrently.You can change the maximum number of RADIUS clients that can be cached concurrently by setting the `org.forgerock.openam.radius.server.context.cache.size` [advanced server property](../setup/server-advanced.html#org.forgerock.openam.radius.server.context.cache.size). |

---

---
title: Authenticate endpoints
description: Reference REST API endpoint parameters for authenticating to PingAM using the `/json/authenticate` endpoint
component: pingam
version: 8.1
page_id: pingam:am-authentication:authenticate-endpoint-parameters
canonical_url: https://docs.pingidentity.com/pingam/8.1/am-authentication/authenticate-endpoint-parameters.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Authentication", "Nodes &amp; Trees", "REST API"]
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

To authenticate to AM using REST, send an HTTP POST request to the `json/authenticate` endpoint. Specify the realm hierarchy, starting at the Top Level Realm and prefix each realm in the hierarchy with the `realms/` keyword. For example, `/realms/root/realms/customers/realms/europe`.

## `/json/authenticate`

The following list describes the `json/authenticate` endpoint parameters:

### `authIndexType`

The `authIndexType` specifies the type of authentication the user will perform. Always use this parameter in conjunction with the `authIndexValue` to provide additional information about how the user is authenticating.

If not specified, AM authenticates the user against the [default authentication service](authn-core-settings.html) configured for the realm.

The `authIndexType` can be one of the following:

* `composite_advice`

  When the `authIndexType` is `composite_advice`, the `authIndexValue` must be a URL-encoded composite advice string.

  Use the `composite_advice` type to indicate which authentication services to use when logging in a user.

  This example indicates that the user should authenticate with an authentication level of at least 10:

  ```bash
  $ curl -G \
  --request POST \
  --header "Content-Type: application/json" \
  --header 'Accept-API-Version: resource=2.0, protocol=1.0' \
  --data-urlencode 'authIndexType=composite_advice' \
  --data-urlencode 'authIndexValue=<Advices>
      <AttributeValuePair>
          <Attribute name="AuthLevelConditionAdvice"/>
          <Value>10</Value>
      </AttributeValuePair>
  </Advices>' \
  'https://am.example.com:8443/am/json/realms/root/authenticate'
  ```

  |   |                                                                                                                        |
  | - | ---------------------------------------------------------------------------------------------------------------------- |
  |   | This `curl` command URL-encodes the XML values. The `--get` option appends them as query string parameters to the URL. |

  Possible options for `Advices` are:

  * `AuthenticateToServiceConditionAdvice`. Requires the name of an authentication tree. For example:

    ```xml
    <Advices>
      <AttributeValuePair>
        <Attribute name="AuthenticateToServiceConditionAdvice"/>
        <Value>myExampleTree</Value>
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

  * `AuthLevelConditionAdvice`. Requires an authentication level.

    For example:

    ```xml
    <Advices>
      <AttributeValuePair>
        <Attribute name="AuthLevelConditionAdvice"/>
        <Value>10</Value>
      </AttributeValuePair>
    </Advices>
    ```

  * `AuthenticateToTreeConditionAdvice`. Requires the name of an authentication tree. For example:

    ```xml
    <Advices>
      <AttributeValuePair>
        <Attribute name="AuthenticateToTreeConditionAdvice"/>
        <Value>PersistentCookieTree</Value>
      </AttributeValuePair>
    </Advices>
    ```

  You can specify multiple advice conditions and combine them. For example:

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
    <AttributeValuePair>
      <Attribute name="AuthLevelConditionAdvice"/>
      <Value>10</Value>
    </AttributeValuePair>
  </Advices>
  ```

* `resource`

  When the `authIndexType` is `resource`, the `authIndexValue` must be a URL protected by an AM policy.

  For example, to log into AM using a policy matching the `https://www.example.com` resource, you could use the following:

  ```bash
  $ curl \
  --request POST \
  --header 'Accept-API-Version: resource=2.0, protocol=1.0' \
  'https://am.example.com:8443/am/json/realms/root/realms/alpha/authenticate?authIndexType=resource&authIndexValue=https%3A%2F%2Fwww.example.com'
  ```

  The resource must be URL-encoded. Authentication fails if no policy matches the resource.

* `service`

  When the `authIndexType` is `service`, the `authIndexValue` is the tree AM must use to authenticate the user.

  For example, to authenticate using the `Login` authentication tree, you could use the following:

  ```bash
  $ curl \
  --request POST \
  --header 'Accept-API-Version: resource=2.0, protocol=1.0' \
  'https://am.example.com:8443/am/json/realms/root/realms/alpha/authenticate?authIndexType=service&authIndexValue=Login'
  ```

  If `authIndexType=service` and no `authIndexValue` is specified, the default service is used. This is similar to no `authIndexType` being set.

* `transaction`

  When the `authIndexType` is `transaction`, the `authIndexValue` must be the unique ID of a transaction token.

  Learn more in [Transactional authorization](../am-authorization/transactional-authorization.html).

  If there are several authentication services that satisfy the authentication requirements, AM presents them as a choice callback to the user. Return the required [callbacks](login-using-REST.html#login-callbacks) to AM to authenticate.

  Required: No.

### `authIndexValue`

This parameter sets a value for the specific `authIndexType`.

Required: Yes, when using the `authIndexType` parameter.

### `noSession`

When set to `true`, this parameter specifies that AM shouldn't return a session when authenticating a user.

For example:

```bash
$ curl \
--request POST \
--header "Content-Type: application/json" \
--header "Accept-API-Version: resource=2.0, protocol=1.0" \
--header "X-OpenAM-Username: bjensen" \
--header "X-OpenAM-Password: Ch4ng31t" \
'https://am.example.com:8443/am/json/realms/root/realms/alpha/authenticate?noSession=true'
{
    "successUrl": "/am/console",
    "realm": "/"
}
```

Required: No.

|   |                                                                                                                                                                                    |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | You can include a message in the success response by adding a [Set Success Details node](https://docs.pingidentity.com/auth-node-ref/8.1/set-success-details.html) to the journey. |

## `/json/authenticate/backchannel`

Lets a third-party federation service initiate and monitor a [backchannel authentication](backchannel-authentication.html) flow.

### `/authenticate/backchannel/initialize`

Initiates a backchannel authentication request. This endpoint has no additional query parameters.

|   |                                                                                                                                                                                                 |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | You must access this endpoint with an OAuth 2.0 token that has the `back_channel_authentication` scope. The token must have been granted by the same AM instance specified in the redirect URI. |

The request body can include the following parameters:

* `type` (string, mandatory)

  The authentication type. Currently, only `service` is supported.

* `value` (string, mandatory)

  The name of the AM authentication tree to direct the user or agent to.

* `subject` (object, optional)

  The subject of the authentication:

  * `type` (string, mandatory)

    The subject type: `user` or `agent`.

  * `name` (string, mandatory)

    The subject name: either their `userName` or their identity `_id`.

* `data` (object, optional)

  Initialization data to add to the authentication journey state, as key-value pairs. For example:

  ```json
  "username": "bjensen",
  "_id": "2e8a7f9f-9d08-4f45-bd47-08e9549347e7"
  ```

  Restricted fields: `realm` and `authLevel`.

* `allowRetry`

  * When `true` (the default behavior), the end user can retry the backchannel transaction if it fails.

  * When `false`, the backchannel authentication token goes into the `Failure` state the first time the backchannel transaction fails.

* `trackingId` (string, optional)

  A tracking ID to add to the audit logs for this authentication flow. If provided, AM logs this ID in addition to its own audit tracking ID. This lets a federation service track the flow of backchannel authentication requests through AM using their own tracking IDs.

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
>     "name": "bjensen"
>   },
>   "data": {
>     "userName": "bjensen"
>   },
>   "trackingId": "Y5tyzQi9cGVJjy2L"
> }',
> "https://am.example.com:8443/am/json/realms/root/realms/alpha/authenticate/backchannel/initialize"
> {
>   "transaction": "b3070138-cd73-4ef2-bd58-812602d7b757",
>   "redirectUri": "https://am.example.com:8443/am/UI/Login?realm=/alpha&authIndexType=transaction&authIndexValue=b3070138-cd73-4ef2-bd58-812602d7b757"
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
> "https://am.example.com:8443/am/json/realms/root/realms/alpha/authenticate/backchannel/info"
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

  Additional information about the user's session, if one was created successfully. You can use the [Set Session Properties node](https://docs.pingidentity.com/auth-node-ref/8.1/set-session-properties.html) to add properties to a session in a journey. You must configure a Session Property Whitelist Service for the realm to allow these properties to be published.

---

---
title: Authenticate over REST
description: "Use PingAM's REST API to authenticate users and manage sessions with the `/json/authenticate` and `/json/sessions` endpoints"
component: pingam
version: 8.1
page_id: pingam:am-authentication:authn-rest
canonical_url: https://docs.pingidentity.com/pingam/8.1/am-authentication/authn-rest.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Authentication", "REST API"]
section_ids:
  login-using-REST: Log in to AM over REST
  authenticate-UTF-8: UTF-8 usernames
  providing-auth-information: Authenticate to specific authentication trees
  login-callbacks: Return callback information to AM
---

# Authenticate over REST

AM provides the `/json/authenticate` endpoint for authentication, and the `/json/sessions` endpoint for managing sessions and logging out.

The following table summarizes authentication operations you can perform using REST:

| Task                                                                                                                                                                                                                                        | Resources                                                                             |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| **Authenticate to AM**Authenticating to AM means logging in to a specific realm and receiving a session token from AM. Add parameters to the authentication request to provide AM with more information about how you want to authenticate. | [Log in to AM over REST](#login-using-REST)                                           |
| **Use the session token**AM provides you with a session token after authenticating to a realm. Use this token in subsequent calls to AM. For example, when using REST calls to create, modify, or delete configuration objects.             | [Session token after authentication](rest-using-ssotokens.html)                       |
| **Log out of AM**Log out your users by sending a `logout` action to the `/json/sessions` endpoint.                                                                                                                                          | [Log out of AM over REST](logout-using-rest.html)                                     |
| **Invalidate sessions**Obtain all the sessions for a given user and invalidate them to ensure they are logged out of AM.                                                                                                                    | [Invalidate sessions](../am-sessions/managing-sessions-REST.html#invalidate-sessions) |

## Log in to AM over REST

To authenticate to AM using REST, make an HTTP POST request to the `json/authenticate` endpoint. You must specify the entire hierarchy of the realm, starting at the Top Level Realm. Prefix each realm in the hierarchy with the `realms/` keyword. For example, `/realms/root/realms/customers/realms/europe`.

|   |                                                                                                                                                                                                                 |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The `/json/authenticate` endpoint doesn't support the CRUDPAQ verbs and therefore doesn't technically satisfy REST architectural requirements. The term *REST-like* describes this endpoint better than *REST*. |

AM uses the default authentication service configured for the realm. You can override the default by [specifying authentication services](#providing-auth-information) and other options in the REST request.

AM provides both simple authentication methods, such as providing username and password, and complex authentication journeys that may involve a tree with inner tree evaluation and/or multi-factor authentication.

For authentication journeys where providing a username and password is enough, you can log in to AM using a `curl` command similar to the following:

```bash
$ curl \
--request POST \
--header "Content-Type: application/json" \
--header "X-OpenAM-Username: bjensen" \
--header "X-OpenAM-Password: Ch4ng31t" \
--header "Accept-API-Version: resource=2.0, protocol=1.0" \
'https://am.example.com:8443/am/json/realms/root/realms/alpha/authenticate'
{
    "tokenId":"AQIC5wM…​TU3OQ*",
    "successUrl":"/am/console",
    "realm":"/alpha"
}
```

The username and password are sent in headers. This zero page login mechanism works only for name/password authentication.

Note that the POST body is empty; otherwise, AM interprets the body as a continuation of an existing authentication attempt, one that uses a supported [callback](#login-callbacks) mechanism. AM implements callback mechanisms to support complex authentication journeys, such as those where the user needs to be redirected to a third party or interact with a device as part of multi-factor authentication.

After a successful authentication, AM returns a `tokenId` object that applications can present as a cookie value for other operations that require authentication. This object is known as the session token. Find information about how applications can use the session token in [Session token after authentication](rest-using-ssotokens.html).

If `HttpOnly` cookies are enabled and a client calls the `/json/authenticate` endpoint with a valid SSO token, AM returns the `tokenId` field **empty**.

For example:

```json
{
    "tokenId":"",
    "successUrl":"/am/console",
    "realm":"/alpha"
}
```

|   |                                                                                                                                                                                               |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | You can request AM to authenticate a user without providing them a session by using the `noSession` parameter. Learn more in [Authenticate endpoints](authenticate-endpoint-parameters.html). |

### UTF-8 usernames

To use UTF-8 usernames and passwords in calls to the `/json/authenticate` endpoint, base64-encode the string, and wrap the string as described in [RFC 2047](https://www.rfc-editor.org/info/rfc2047):

```
encoded-word = "=?" charset "?" encoding "?" encoded-text "?="
```

For example, to authenticate using a UTF-8 username, such as `ɗëɱø`, perform the following steps:

1. Encode the string in base64 format: `yZfDq8mxw7g=`.

2. Wrap the base64-encoded string as per RFC 2047: `=?UTF-8?B?yZfDq8mxw7g=?=`.

3. Use the result in the `X-OpenAM-Username` header passed to the authentication endpoint as follows:

   ```bash
   $ curl \
   --request POST \
   --header "Content-Type: application/json" \
   --header "X-OpenAM-Username: =?UTF-8?B?yZfDq8mxw7g=?=" \
   --header "X-OpenAM-Password: Ch4ng31t" \
   --header "Accept-API-Version: resource=2.0, protocol=1.0" \
   'https://am.example.com:8443/am/json/realms/root/realms/alpha/authenticate'
   {
       "tokenId": "AQIC5w…​NTcy*",
       "successUrl": "/am/console",
       "realm":"/alpha"
   }
   ```

## Authenticate to specific authentication trees

You can provide AM with additional information about how you are authenticating. For example, you can specify the authentication tree you want to use, or request from AM a list of the authentication services that would satisfy a particular authentication condition.

The following example shows how to specify the `Example` tree by using the `authIndexType` and `authIndexValue` query string parameters:

```bash
$ curl \
--request POST \
--header "X-OpenAM-Username: bjensen" \
--header "X-OpenAM-Password: Ch4ng31t" \
--header 'Accept-API-Version: resource=2.0, protocol=1.0' \
'https://am.example.com:8443/am/json/realms/root/realms/alpha/authenticate?authIndexType=service&authIndexValue=Example'
```

You can exchange `Example` with any other tree.

Find information about using the `authIndexType` parameter to authenticate to specific services in [Authenticate endpoints](authenticate-endpoint-parameters.html).

## Return callback information to AM

The `/json/authenticate` endpoint supports callback mechanisms to perform complex authentication journeys. Whenever AM needs to return or request information, it will return a JSON object with the authentication step, the authentication identifier, and the related callbacks.

The following types of callbacks are available:

* Read-only callbacks

  AM uses read-only callbacks to provide information to the user, such as text messages or the amount of time that the user needs to wait before continuing their authentication journey.

* Interactive callbacks

  Interactive callbacks request information from the user. Use these, for example, to request a user's username and password or to request that the user select between options.

* Backchannel callbacks

  AM uses backchannel callbacks when it needs to access additional information from the user's request. For example, when it requires a particular header or a certificate.

Read-only and interactive callbacks have an array of `output` elements suitable for displaying to the end user. The JSON returned in interactive callbacks also contains an array of `input` elements that must be completed and returned to AM.

For example:

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

Depending on how complex the authentication journey is, AM may return several callbacks sequentially. Each must be completed and returned to AM until authentication is successful.

The following example shows a request for authentication, and AM's response of the `NameCallback` and `PasswordCallback` callbacks:

```bash
$ curl \
--request POST \
--header "Content-Type: application/json" \
--header "Accept-API-Version: resource=2.0, protocol=1.0" \
'https://am.example.com:8443/am/json/realms/root/realms/alpha/authenticate'
{
  "authId": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJvdGsiOiJ…​", (1)
  "template": "",
  "stage": "DataStore1",
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

|       |                                                                                                              |
| ----- | ------------------------------------------------------------------------------------------------------------ |
| **1** | The JWT that uniquely identifies the authentication context to AM.                                           |
| **2** | The type of callback. It must be listed under [Supported callbacks](callbacks-supported.html).               |
| **3** | The information AM offers about this callback. Usually, this information is displayed to the user in the UI. |
| **4** | The information AM is requesting. The user must fill the `"value": ""` object with the required information. |

To respond to a callback, send back the whole JSON object with the missing values filled. The following example shows how to respond to the `NameCallback` and `PasswordCallback` callbacks, with the `bjensen` and `Ch4ng31t` values filled:

```bash
$ curl \
--request POST \
--header "Content-Type: application/json" \
--header "Accept-API-Version: resource=2.0, protocol=1.0" \
--data '{
   "authId":""eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJvdGsiOiJ…​",
   "template":"",
   "stage":"DataStore1",
   "callbacks":[
      {
         "type":"NameCallback",
         "output":[
            {
               "name":"prompt",
               "value":" User Name: "
            }
         ],
         "input":[
            {
               "name":"IDToken1",
               "value":"bjensen"
            }
         ]
      },
      {
         "type":"PasswordCallback",
         "output":[
            {
               "name":"prompt",
               "value":" Password: "
            }
         ],
         "input":[
            {
               "name":"IDToken2",
               "value":"Ch4ng31t"
            }
         ]
      }
   ]
}' \
'https://am.example.com:8443/am/json/realms/root/realms/alpha/authenticate'
{
    "tokenId":"AQIC5wM…​TU3OQ*",
    "successUrl": "/am/console",
    "realm":"/alpha"
}
```

On complex authentication journeys, AM may send several callbacks sequentially. Each must be completed and returned to AM until authentication is successful.

Find information about the callbacks AM can return in [Supported callbacks](callbacks-supported.html).

---

---
title: Authenticate with a browser
description: "Authenticate users with PingAM's extended user interface by specifying realms and authentication parameters in browser URLs"
component: pingam
version: 8.1
page_id: pingam:am-authentication:authn-from-browser
canonical_url: https://docs.pingidentity.com/pingam/8.1/am-authentication/authn-from-browser.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Authentication", "Realms", "Browser"]
page_aliases: ["authentication-guide:authn-from-browser.adoc"]
section_ids:
  authn-from-browser-XUI-realm: Specify the realm in the URL
  authn-from-browser-parameters: Authentication parameters
  authn-from-browser-XUI-examples: Example UI login URLs
---

# Authenticate with a browser

When using AM's extended user interface (XUI), the base URL to authenticate to points to `/XUI/#login` under the deployment URL, such as `https://am.example.com:8443/am/XUI/#login`.

The base URL to log out is similar, for example, `https://am.example.com:8443/am/XUI/#logout/`.

When authenticating using a browser, you can send AM a [realm](#authn-from-browser-XUI-realm) and also different [authentication parameters](#authn-from-browser-parameters) that would help you customize the user's experience.

## Specify the realm in the URL

When making a request to the UI, specify the realm or realm alias as the value of a `realm` parameter in the query string, or the DNS alias in the domain component of the URL. If you don't use a realm alias, you must specify the entire hierarchy of the realm. For example: `https://am.example.com:8443/am/XUI/?realm=/customers/europe#login/`.

The following table demonstrates additional examples:

**How to specify the realm in UI login URLs**

| Description                                                        | Example URL                                                         |
| ------------------------------------------------------------------ | ------------------------------------------------------------------- |
| Full path of the realm as a parameter of `XUI`                     | `https://am.example.com:8443/am/XUI/?realm=/customers/europe#login` |
| Realm alias of the realm as a parameter of `XUI`                   | `https://am.example.com:8443/am/XUI/?realm=alpha#login`             |
| DNS Alias of the realm as the fully qualified host name in the URL | `https://myRealm.example.com:8443/am/XUI/#login`                    |

The DNS alias is overridden by any use of either the full path or a realm alias as a query string parameter.

## Authentication parameters

AM accepts the following parameters in the query string. Except for the `IDToken` parameters, don't set a parameter more than once in a single query.

* arg=newsession

  Request that AM end the user's current session and start a new session.

- ForceAuth

  If `ForceAuth=true`, request that AM force the user to authenticate even if they already have a valid session.

  When `ForceAuth=true`, on successful authentication, AM issues new session tokens to users on reauthentication, even if the current session already meets the security requirements.

  |   |                                                                                   |
  | - | --------------------------------------------------------------------------------- |
  |   | This parameter is case-sensitive. Using `forceAuth` or `forceauth` has no effect. |

- goto

  On successful authentication, or successful logout, request that AM redirect the user to the specified location. Values must be URL-encoded. For more information, refer to [Success and failure redirection URLs](redirection-url-precedence.html).

- gotoOnFail

  On authentication failure, request that AM redirect the user to the specified location. Values must be URL-encoded. For more information, refer to [Success and failure redirection URLs](redirection-url-precedence.html).

- locale

  Request that AM display the user interface in the specified, supported locale. Locale can also be set in the user's profile, in the HTTP header from her browser, configured in AM, and so on.

- realm

  Request that AM authenticate the user to the specified realm.

- service

  Request that AM authenticate the user with the specified authentication tree.

### Example UI login URLs

Use any of the options listed in [Authentication parameters](#authn-from-browser-parameters) as URL parameters. Note that URL parameters must appear *before* any occurrences of the pound or hash character (`#`). The following are example URLs with parameters:

**Example UI Login URLs**

| Description                                                                                                                  | Example URL                                                                       |
| ---------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| Log in to the Top Level Realm, requesting that AM display the user interface in German.                                      | `https://am.example.com:8443/am/XUI/?realm=/&locale=de#login`                     |
| Log in to the `alpha` realm, requesting that AM display the user interface in German.                                        | `https://am.example.com:8443/am/XUI/?realm=/alpha&locale=de#login`                |
| Log in to the `alpha` realm using the `myTree` authentication tree, requesting that AM display the user interface in German. | `https://am.example.com:8443/am/XUI/?realm=/alpha&locale=de&service=myTree#login` |

---

---
title: Authentication and SSO
description: Understand authentication and single sign-on (SSO) concepts, implementation procedures, and customization techniques in PingAM
component: pingam
version: 8.1
page_id: pingam:am-authentication:preface
canonical_url: https://docs.pingidentity.com/pingam/8.1/am-authentication/preface.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Authentication", "Single Sign-on (SSO)"]
page_aliases: ["index.adoc", "authentication-guide:preface.adoc"]
---

# Authentication and SSO

These topics cover concepts, implementation procedures, and customization techniques for working with the authentication and single sign-on (SSO) features of PingAM.

[icon: cogs, set=fad, size=3x]

#### [Configure AM for authentication](authn-implementation-authn.html)

Learn about AM's authentication mechanisms.

[icon: cubes, set=fad, size=3x]

#### [Nodes and trees](auth-nodes-and-journeys.html)

Learn about nodes and trees, which are used to create authentication journeys.

[icon: th-list, set=fad, size=3x]

#### [Multi-factor authentication](authn-mfa.html)

Require that users provide multiple forms of identification when logging in to services.

[icon: users, set=fad, size=3x]

#### [Single sign-on](about-sso.html)

Enable single sign-on (SSO) so that users can log in once with a single set of credentials.

[icon: comments, set=fad, size=3x]

#### [Social authentication](social-registration.html)

Allow users to authenticate to your services by using third-party identity providers.

[icon: handshake, set=fad, size=3x]

#### [RADIUS authentication](radius-authentication.html)

Learn how AM supports the RADIUS protocol to provide RADIUS authentication.

---

---
title: Authentication reference
description: Reference information for authentication configuration settings, endpoints, and scripting API in PingAM
component: pingam
version: 8.1
page_id: pingam:am-authentication:authn-reference
canonical_url: https://docs.pingidentity.com/pingam/8.1/am-authentication/authn-reference.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Authentication"]
page_aliases: ["authentication-guide:authn-reference.adoc"]
---

# Authentication reference

Use the links in this table to find reference information about authentication configuration settings, endpoints and the scripting API for authentication in AM.

| Link                                                                              | Description                                                                                                   |
| --------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| [Core authentication attributes](authn-core-settings.html)                        | The settings for configuring authentication in AM at the realm or global level.                               |
| [Node reference](auth-nodes-reference.html)                                       | Describes the nodes available in AM and how to configure them.                                                |
| [Authenticate endpoints](authenticate-endpoint-parameters.html)                   | The authentication endpoints and their parameters.                                                            |
| [Social identity provider client configuration](social-idp-client-reference.html) | The settings required for configuring social authentication.                                                  |
| [Configure AM services](../setup/services-configuration.html)                     | How to configure AM services.                                                                                 |
| [Supported callbacks](callbacks-supported.html)                                   | The supported callbacks.                                                                                      |
| [Scripted Decision node API](../am-scripting/scripting-api-node.html)             | The API for [Scripted Decision node](https://docs.pingidentity.com/auth-node-ref/8.1/scripted-decision.html). |

Learn more about configuring AM settings and services in [Reference](../am-reference/preface.html).

---

---
title: Authenticator apps
description: Use authenticator apps for multi-factor authentication with PingAM, supporting PingID, ForgeRock Authenticator, and third-party TOTP-based applications
component: pingam
version: 8.1
page_id: pingam:am-authentication:authenticator-app
canonical_url: https://docs.pingidentity.com/pingam/8.1/am-authentication/authenticator-app.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Authentication", "Multi-factor Authentication (MFA)"]
page_aliases: ["authn-mfa-download-app.adoc", "authentication-guide:authenticator-app.adoc"]
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

PingAM supports a number of authenticator apps:

* [PingID mobile app](#ping-id-mobile-app)

* [ForgeRock Authenticator app](#forgerock-authenticator-app)

* [Other authenticator apps](#other-authenticator-apps)

## PingID mobile app

The PingID mobile app is the default supported authenticator app for performing MFA with AM. This app supports time-based one-time passwords (TOTPs) only. It doesn't support HMAC-based one-time passwords (HOTPs).

Depending on their device type, end users can download the PingID mobile app from one of the following locations:

* [Apple App Store](https://apps.apple.com/us/app/pingid/id891247102) (for iOS devices)

* [Google Play](https://play.google.com/store/apps/details?id=prod.com.pingidentity.pingid) (for Android devices)

* [PingID Downloads site](https://www.pingidentity.com/en/resources/downloads/pingid.html)

They must register the PingID mobile app with AM to use it as an additional factor when logging in.

## ForgeRock Authenticator app

The ForgeRock Authenticator app supports time-based one-time passwords (TOTPs) and HMAC-based one-time passwords (HOTPs).

Depending on their device type, end users can download the ForgeRock Authenticator app from one of the following locations:

* [Apple App Store](https://apps.apple.com/app/forgerock-authenticator/id1038442926) (for iOS devices)

* [Google Play](https://play.google.com/store/apps/details?id=com.forgerock.authenticator) (for Android devices)

|   |                                                                                                                                                                                                                                                                                                       |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Although the PingID mobile app is the default supported authenticator app for performing MFA with AM, there is no smooth migration path from the ForgeRock Authenticator app to the PingID mobile app. If you're already using the ForgeRock Authenticator app for MFA, you should continue to do so. |

## Other authenticator apps

You can perform MFA with any third-party authenticator app that supports the Time-Based One-Time Password (TOTP) open standard. For example, Google Authenticator or Salesforce Authenticator.

To build your own authenticator app, integrate the Ping (ForgeRock) Authenticator module using Ping SDKs.

Find the instructions for [Android](https://docs.pingidentity.com/sdks/latest/authenticator-module/getting-started/01-setup-your-project.html#android) or [iOS](https://docs.pingidentity.com/sdks/latest/authenticator-module/getting-started/01-setup-your-project.html#ios).

---

---
title: Backchannel authentication
description: "Enable a third-party federation service to initiate PingAM authentication on behalf of users by submitting user data directly to PingAM's backchannel authentication endpoints"
component: pingam
version: 8.1
page_id: pingam:am-authentication:backchannel-authentication
canonical_url: https://docs.pingidentity.com/pingam/8.1/am-authentication/backchannel-authentication.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Authentication", "Backchannel"]
page_aliases: ["authentication-guide:backchannel-authentication.adoc"]
section_ids:
  demonstrate_backchannel_authentication: Demonstrate backchannel authentication
  create-auth-journey: Create an authentication journey
  configure-oauth-service: Configure the OAuth 2.0 provider service
  create-oauth-client: Create an OAuth 2.0 client
  configure-base-url-source: Configure the Base URL Source
  allowlist-session-properties: Allowlist session properties (optional)
  get-access-token: Get an access token
  intialize-the-transaction: Initialize the backchannel authentication transaction
  complete-backchannel-auth: Complete the backchannel authentication
  check-the-status: Check the status of the backchannel authentication request
  backchannel-endpoints: Backchannel authentication REST endpoints
---

# Backchannel authentication

Backchannel authentication lets a third-party federation service initiate authentication with AM on behalf of a user. The federation service collects the user data and transmits this data directly to AM. AM redirects the user to complete the authentication process without having to re-enter the collected data. Backchannel authentication provides a seamless user experience and is more secure as users don't have to enter credentials multiple times.

|   |                                                                                                                                                                                                                                                                                                                                                |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The backchannel authentication flow described here is an AM feature. It's distinct from the following OpenID Connect (OIDC) flows, which also use the term *backchannel*:- [OIDC backchannel request grant](../am-oidc1/openid-connect-backchannel-request-flow.html) (CIBA)

- [OIDC backchannel logout](../am-oidc1/backchannel-logout.html) |

Backchannel authentication uses a [transactional authorization](../am-authorization/transactional-authorization.html) process with requests sent to the [backchannel authentication REST endpoints](#backchannel-endpoints). Data supplied by the federation service is saved in a *transaction* with a specific transaction ID. When the user starts their authentication journey in AM, the transaction locates the federation-provided data and inserts it into the journey's shared state.

The following diagram illustrates the backchannel authentication flow.

![Sequence diagram illustrating backchannel authentication flow.](_images/backchannel-auth.svg)

## Demonstrate backchannel authentication

These steps use an OAuth 2.0 client to mimic the third-party federation service. The client initializes the backchannel authentication transaction and AM redirects the user to a simple login journey to complete authentication.

The process includes the following steps:

1. [Create an authentication journey](#create-auth-journey)

2. [Configure the OAuth 2.0 provider service](#configure-oauth-service)

3. [Create an OAuth 2.0 client](#create-oauth-client)

4. [Configure the Base URL Source](#configure-base-url-source)

5. [Allowlist session properties (optional)](#allowlist-session-properties)

6. [Get an access token](#get-access-token)

7. [Initialize the backchannel authentication transaction](#intialize-the-transaction)

8. [Complete the backchannel authentication](#complete-backchannel-auth)

9. [Check the status of the backchannel authentication request](#check-the-status)

### Create an authentication journey

This example assumes a simple journey that lets the user log in by supplying only their password. The username is provided by the third-party federation service as part of the backchannel authentication request and is added to the journey's shared state, so the journey doesn't need to collect it.

The name of the journey is `Login`.

![backchannel auth journey](_images/backchannel-auth-journey.png)

|   |                                                                                                                                                                                                                                                                                            |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | To prevent users from authenticating directly through this tree, either for security reasons or because the tree is insufficient as a complete authentication service, configure it as a [transactional authentication tree](configure-auth-trees.html#configure-transactional-auth-tree). |

### Configure the OAuth 2.0 provider service

1. In the AM admin UI, go to Realms > *realm name* > Services > OAuth2 Provider > Advanced.

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

### Configure the Base URL Source

By default, the base URL of the redirect URI is retrieved from the incoming HTTP request. For this demonstration, configure a fixed base URL with the value of your AM host.

1. In the AM admin UI, go to Realms > *realm name* > Services and click Add a Service.

2. Select `Base URL Source` and click Create.

3. In the Base URL Source list, select `Fixed value`.

4. Set the Fixed value base URL to your AM host, for example, `https://am.example.com:8443/am`.

5. Click Save Changes.

### Allowlist session properties (optional)

When you query the state of a successful backchannel authentication, you might want to obtain certain session details. To do this, configure the Session Property Whitelist Service and specify any properties to be included in a query response.

1. Go to Realms > *realm name* > Services, and click Add a Service.

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
"https://am.example.com:8443/am/oauth2/realms/root/realms/alpha/access_token"
{
  "access_token": "FnpG1lU0fUooJFY-82sq3UiAnGA",
  "scope": "back_channel_authentication",
  "token_type": "Bearer",
  "expires_in": 3599
}
```

Find more information in [OAuth 2.0 client authentication](../am-oauth2/oauth2-client-auth.html).

### Initialize the backchannel authentication transaction

This section assumes that a user has already signed on to the third-party federation service and that the service has their *username*.

As the OAuth 2.0 client, send an HTTP POST request to the `/authenticate/backchannel/initialize` endpoint. Specify the authentication journey (`Login` in this example) to which the user should be redirected and the user in the JSON payload.

Optionally, include a `data` object to add initialization data to the journey's shared state such as `userName`, and a `trackingId` to let the federation service track the request through AM. If a `trackingId` is provided, AM logs this ID and its own audit tracking ID. The custom tracking ID must be a string of 36 characters or less and can include only the characters `A-Z` `a-z` `0-9` `-` and `_`.

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
    "name": "bjensen"
  },
  "data": {
    "userName": "bjensen"
  },
  "trackingId": "Y5tyzQi9cGVJjy2L"
}',
"https://am.example.com:8443/am/json/realms/root/realms/alpha/authenticate/backchannel/initialize"
{
  "transaction": "b3070138-cd73-4ef2-bd58-812602d7b757",
  "redirectUri": "https://am.example.com:8443/am/XUI/Login?realm=/alpha&authIndexType=transaction&authIndexValue=b3070138-cd73-4ef2-bd58-812602d7b757"
}
```

AM returns a transaction ID and the complete redirect URI, including the transaction ID.

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
"https://am.example.com:8443/am/json/realms/root/realms/alpha/authenticate/backchannel/info"
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

  |   |                                                                                                                            |
  | - | -------------------------------------------------------------------------------------------------------------------------- |
  |   | If you don't set `allowRetry` to `false` when you initiate the backchannel transaction, it won't return a `DENIED` result. |

* An array of `auditTrackingIds`, including the standard audit ID AM generates and any custom tracking IDs supplied in the initial request.

* Any allowlisted `sessionProperties`.

  Learn more in [Allowlist session properties (optional)](#allowlist-session-properties).

## Backchannel authentication REST endpoints

AM exposes the following REST endpoints for backchannel authentication:

| Endpoint                               | Description                                                                                                                                                                                                                                                                                                    |
| -------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `/authenticate/backchannel/initialize` | Lets a third-party federation service initiate a backchannel authentication flow.                                                                                                                                                                                                                              |
| `/authenticate/backchannel/info`       | Lets a third-party federation service verify that a backchannel authentication process completed successfully.	You must access this endpoint with an OAuth 2.0 token that has the back\_channel\_authentication scope. The token must have been granted by the same AM instance specified in the redirect URI. |

Find reference information on these endpoints in [json/authenticate/backchannel](authenticate-endpoint-parameters.html#rest-authenticate-backchannel).

---

---
title: Backchannel callbacks
description: Retrieve additional information from authentication requests using backchannel callbacks for headers, certificates, and locale data
component: pingam
version: 8.1
page_id: pingam:am-authentication:callbacks-backchannel
canonical_url: https://docs.pingidentity.com/pingam/8.1/am-authentication/callbacks-backchannel.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Authentication", "Callbacks", "REST API"]
page_aliases: ["authn-backchannel-callbacks.adoc", "authentication-guide:callbacks-backchannel.adoc"]
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

* Class to import

  `com.sun.identity.authentication.spi.HttpCallback`

Learn more in [HttpCallback](../_attachments/apidocs/com/sun/identity/authentication/spi/HttpCallback.html).

## LanguageCallback

Retrieves the locale from the request header for localizing text presented to the user.

* Class to import

  `javax.security.auth.callback.LanguageCallback`

Learn more in [LanguageCallback](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/javax/security/auth/callback/LanguageCallback.html).

## ScriptTextOutputCallback

Inserts a script into the page presented to the user; for example, to collect data about the user's environment.

|   |                                                                                                                                                                                                                                                                     |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Don't use `ScriptTextOutputCallback` to build custom user interfaces or style the login page. Scripts injected this way might rely on specific PingAM JavaScript or HTML that isn't guaranteed to remain stable. This could cause them to break in future upgrades. |

* Class to import

  `com.sun.identity.authentication.callbacks.ScriptTextOutputCallback`

Learn more in [ScriptTextOutputCallback](../_attachments/apidocs/com/sun/identity/authentication/callbacks/ScriptTextOutputCallback.html).

## X509CertificateCallback

Retrieves an X.509 certificate, for example, from a header.

* Class to import

  `com.sun.identity.authentication.spi.X509CertificateCallback`

Learn more in [X509CertificateCallback](../_attachments/apidocs/com/sun/identity/authentication/spi/X509CertificateCallback.html).

---

---
title: Configure authentication
description: Configure authentication mechanisms, realm defaults, redirection URLs, and identity stores to set up flexible authentication paths in PingAM realms
component: pingam
version: 8.1
page_id: pingam:am-authentication:authn-implementation-authn
canonical_url: https://docs.pingidentity.com/pingam/8.1/am-authentication/authn-implementation-authn.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Authentication", "Nodes &amp; Trees", "Realms", "Setup &amp; Configuration"]
page_aliases: ["authentication-guide:authn-implementation-authn.adoc"]
---

# Configure authentication

The authentication process is very flexible and can be adapted to suit your specific deployment. The number of choices can seem daunting, but when you understand the basic process, you'll be able to configure custom authentication paths to protect access to the applications in your organization.

You configure authentication per realm. When you create a new realm, it inherits the authentication configuration of the parent realm. This can save time, especially if you are configuring several subrealms.

The following table summarizes the high-level tasks required to configure authentication in a realm:

| Task                                                                                                                                                                                                                                                               | Resources                                                                 |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------- |
| **Configure the required authentication mechanisms**You need to decide how your users are going to log in. For example, you may require your users to provide multiple credentials, or to log in using third-party identity providers, such as Facebook or Google. | * [Nodes and trees](auth-nodes-and-journeys.html)                         |
| **Configure the realm defaults for authentication**Authentication trees use several defaults that are configured at realm level. Review and configure them to suit your environment.                                                                               | - [Core authentication attributes](authn-core-settings.html)              |
| **Configure the success and failure URLs for the realm**By default, AM redirects users to the UI after successful authentication. No failure URL is defined by default.                                                                                            | * [Success and failure redirection URLs](redirection-url-precedence.html) |
| **Configure an identity store in your realm.**The identity store you configure in the realm should contain those users that would log in to the realm.                                                                                                             | - [Identity stores](../setup/setting-up-identity-stores.html)             |

---

---
title: Configure authentication trees
description: Configure authentication trees over REST to enable or disable them, restrict access, specify identity resources, and customize session behavior
component: pingam
version: 8.1
page_id: pingam:am-authentication:configure-auth-trees
canonical_url: https://docs.pingidentity.com/pingam/8.1/am-authentication/configure-auth-trees.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Authentication", "Nodes &amp; Trees", "Setup &amp; Configuration"]
page_aliases: ["authentication-guide:configure-auth-trees.adoc"]
section_ids:
  disable-authn-tree: Enable and disable an authentication tree
  disable-inner-tree: Disable direct access through an inner tree
  update-platform-identity-resource-trees: Specify IDM identity resources in trees
  enable-tree-completion: Configure an authentication tree to always run
  configure-nosession-tree: Configure a no session tree
  configure-transactional-auth-tree: Configure a transactional authentication tree
  configure-journey-session-duration-tree: Configure journey session duration in a tree
  configure-auth-session-timeouts-tree: Configure authenticated session timeouts in a tree
---

# Configure authentication trees

You configure authentication trees over REST by sending PUT requests to update the tree configuration. You must include the tree ID and all the nodes in the tree in the request. You can find information on the required parameters in the [online REST API reference](../am-rest/about-api-explorer.html).

This table outlines the high-level tasks for configuring authentication trees:

| Task                                                                                        | Description                                                                                                                                                                                 |
| ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Enable and disable an authentication tree](#disable-authn-tree)                            | Disable trees during development or when they aren't in use to enhance security.                                                                                                            |
| [Disable direct access through an inner tree](#disable-inner-tree)                          | Prevent an inner tree from being called directly, ensuring it's only used within its parent journey.                                                                                        |
| [Specify IDM identity resources in trees](#update-platform-identity-resource-trees)         | Specify the identity object a tree should use when integrated with IDM, if it's not the default `managed/user`.                                                                             |
| [Configure an authentication tree to always run](#enable-tree-completion)                   | Force a tree to execute on every authentication attempt, even if a valid session already exists.                                                                                            |
| [Configure a no session tree](#configure-nosession-tree)                                    | Create a journey that completes successfully without creating an authenticated session, ideal for tasks like delegated administration.                                                      |
| [Configure a transactional authentication tree](#configure-transactional-auth-tree)         | Indicate a tree can only be used for transactional authentication purposes, including backchannel authentication, OAuth 2.0 app trees, SAML 2.0 app trees, and transactional authorization. |
| [Configure journey session duration in a tree](#configure-journey-session-duration-tree)    | Override the maximum duration of the journey session for a specific tree, for example, to allow more time for an email verification step.                                                   |
| [Configure authenticated session timeouts in a tree](#configure-auth-session-timeouts-tree) | Set custom session idle and maximum timeout values for authenticated sessions created by a specific tree.                                                                                   |

## Enable and disable an authentication tree

Custom authentication trees are enabled by default when you save them. For security purposes, you can disable custom authentication trees during development and testing to prevent accidentally allowing access through these trees. Rather than having unused authentication trees enabled, you should disable the default authentication trees until you need them.

When a user attempts to authenticate through a disabled tree, AM returns a `No configuration found` error.

To enable or disable an authentication tree, send a PUT request to update the tree configuration. Include the tree ID and all the nodes in the tree, and set the `enabled` property.

> **Collapse: Example**
>
> ```bash
> $ curl \
> --request PUT \
> --header "iPlanetDirectoryPro: AQIC5wM…​TU3OQ*" \
> --header "Content-Type: application/json" \
> --header "Accept-API-Version: protocol=2.1,resource=3.0" \
> --data '{
>   "entryNodeId": "c11e9cf8-ef48-4740-876f-6300e2f46aef",
>   "nodes": {
>    ...
>   },
>   "enabled": false
> }' \
> "https://am.example.com:8443/am/json/realms/root/realms/alpha/realm-config/authentication/authenticationtrees/trees/myAuthTree"
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

## Disable direct access through an inner tree

An inner tree or child tree lets you nest authentication logic. There is no limit to the depth of nesting.

You configure an inner tree like any other tree then call it from a parent tree using an [Inner Tree Evaluator node](https://docs.pingidentity.com/auth-node-ref/8.1/inner-tree-evaluator.html).

You could want to hide inner trees as complete services. In other words, you could want to prevent users from authenticating directly through an inner tree, either for security reasons or because the inner tree is insufficient as a complete authentication service. Additionally, inner trees can't be used as [transactional authentication trees](#configure-transactional-auth-tree).

To prevent a tree from being used outside of its parent tree, set the `innerTreeOnly` property to `true` in the tree configuration. Send a PUT request to update the tree configuration, including the tree ID and all the nodes in the tree.

> **Collapse: Example**
>
> ```bash
> $ curl \
> --request PUT \
> --header "iPlanetDirectoryPro: AQIC5wM…​TU3OQ*" \
> --header "Content-Type: application/json" \
> --header "Accept-API-Version: protocol=2.1,resource=3.0" \
> --data '{
>   "entryNodeId": "c11e9cf8-ef48-4740-876f-6300e2f46aef",
>   "nodes": {
>    ...
>   },
>   "innerTreeOnly": true
> }' \
> "https://am.example.com:8443/am/json/realms/root/realms/alpha/realm-config/authentication/authenticationtrees/trees/myAuthTree"
> {
>   "_id": "myAuthTree",
>   "_rev": "1081620278",
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

|   |                                                                                                                                                                                                                                                   |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | To find out if the current tree is configured as an inner tree only, include a Scripted Decision node with a script that calls `journey.innerJourney()`.Learn more in [Get journey details](../am-scripting/script-bindings.html#common-journey). |

## Specify IDM identity resources in trees

When running AM as part of an integrated platform with IDM, trees configured to use the Ping Advanced Identity Software need to identify the type of identity resource or object the tree is working with.

To do this, set the `identityResource` property to the required identity resource or object in the tree configuration. Send a PUT request to update the tree configuration, including the tree ID and all the nodes in the tree.

If the property isn't included in the tree configuration, it defaults to `managed/user`.

> **Collapse: Example**
>
> The following example sets `identityResource` to use a managed object in IDM called `newObjectType`:
>
> ```bash
> $ curl \
> --request PUT \
> --header "iPlanetDirectoryPro: AQIC5wM…​TU3OQ*" \
> --header "Content-Type: application/json" \
> --header "Accept-API-Version: protocol=2.1,resource=3.0" \
> --data '{
>    "entryNodeId":"e301438c-0bd0-429c-ab0c-66126501069a",
>   "nodes": {
>    ...
>   },
>    "description":"Example tree description",
>    "identityResource":"managed/newObjectType"
>  }' \
> "https://am.example.com:8443/am/json/realms/root/realm-config/authentication/authenticationtrees/trees/myAuthTree"
> ```

## Configure an authentication tree to always run

You can configure a tree to always run, whether a user authenticated successfully and a session exists or not. If enabled, the tree runs even when the session was created through a different tree and irrespective of the value of the [ForceAuth](authn-from-browser.html#authentication-forceAuth) parameter.

|   |                                                                                                                                                                                                                                                                                                    |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | You can't set a tree to always run when it's set as the default authentication service.Also, to prevent unexpected behavior in the authentication flow, don't configure the tree to always run when it's mapped to the default [acr](../am-oidc1/oidc-authentication-requirements.html#acr-claim). |

If a user successfully signs on using a specific authentication tree and then tries to reauthenticate to the same tree while the session is still valid, the default behavior is for the authentication flow to skip the processing of the tree. For example, the [Set Session Properties node](https://docs.pingidentity.com/auth-node-ref/8.1/set-session-properties.html) is never run in this scenario:

![Authentication tree to demonstrate mustRun property](_images/auth-mustrun-tree.png)

However, to make sure the tree always runs and sets the session property even when a valid authenticated session exists, set the `mustRun` property to `true` in the tree configuration.

To do this, send a PUT request to update the tree configuration including the tree ID and all the nodes in the tree.

> **Collapse: Example**
>
> ```bash
> $ curl \
> --request PUT \
> --header "iPlanetDirectoryPro: AQIC5wM…​TU3OQ*" \
> --header "Content-Type: application/json" \
> --header "Accept-API-Version: protocol=2.1,resource=3.0" \
> --data '{
>   "entryNodeId": "83fa0ce2-1b0f-4f8f-83fb-0d2648339797",
>   "nodes": {
>    ...
>   },
>   "mustRun": true
> }' \
> "https://am.example.com:8443/am/json/realms/root/realms/alpha/realm-config/authentication/authenticationtrees/trees/myAuthTree"
> {
>   "_id": "myAuthTree",
>   "_rev": "71943491",
>   "entryNodeId": "83fa0ce2-1b0f-4f8f-83fb-0d2648339797",
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

|   |                                                                                                                                                                                                                                      |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | To find out if the current tree is configured to always run, include a Scripted Decision node with a script that calls `journey.mustRun()`.Learn more in [Get journey details](../am-scripting/script-bindings.html#common-journey). |

## Configure a no session tree

A no session tree doesn't result in an authenticated session when it successfully completes.

A common use case for a no session tree is a delegated admin task, such as an administrator changing a user's password. In this scenario, you don't want an authenticated session to be created when the administrator enters the credentials of the user whose password they are changing.

|   |                                                                                                                                                                                                                                                                                                                                                                       |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | This can also be achieved by setting the [`noSession` query parameter](authenticate-endpoint-parameters.html#nosession). However, consider that an end user could remove the query parameter to create a session.If the `noSession` property is set to `true` in either the tree or the query parameter, the resulting journey won't create an authenticated session. |

To configure a no session tree, set the `noSession` property to `true` in the tree configuration. Send a PUT request to update the tree configuration, including the tree ID and all the nodes in the tree.

> **Collapse: Example**
>
> ```bash
> $ curl \
> --request PUT \
> --header "iPlanetDirectoryPro: AQIC5wM…​TU3OQ*" \
> --header "Content-Type: application/json" \
> --header "Accept-API-Version: protocol=2.1,resource=3.0" \
> --data '{
>   "entryNodeId": "c11e9cf8-ef48-4740-876f-6300e2f46aef",
>   "nodes": {
>    ...
>   },
>   "noSession": true
> }' \
> "https://am.example.com:8443/am/json/realms/root/realms/alpha/realm-config/authentication/authenticationtrees/trees/myAuthTree"
> {
>   "_id": "myAuthTree",
>   "_rev": "1081620278",
>   "uiConfig": {},
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

## Configure a transactional authentication tree

In AM, certain advanced authentication flows initiate a temporary, secure process known as a *transaction* to handle a specific authentication or authorization event.

You can configure trees for these flows as *transactional authentication trees* to manage the user interaction required to complete the transaction. This prevents users from authenticating directly through the tree, either for security reasons or because the transactional tree is insufficient as a complete authentication service. Additionally, transactional authentication trees can't be used as [inner trees](#disable-inner-tree).

|   |                                                                                                             |
| - | ----------------------------------------------------------------------------------------------------------- |
|   | You don't *have to* configure the tree used in a transactional flow as a transactional authentication tree. |

A transactional authentication tree only runs when AM starts a transaction, which happens when AM does one of the following:

* Initializes [backchannel authentication](backchannel-authentication.html) using either the `/authenticate/backchannel/initialize` endpoint or the [Backchannel Initialize node](https://docs.pingidentity.com/auth-node-ref/8.1/backchannel-initialize.html).

* Runs a [SAML 2.0 app](../am-saml2/saml2-providers-and-cots.html#samlapp-tree) tree for a remote SP.

* Runs an [OAuth 2.0 app](../am-oauth2/oauth2-register-client.html#oauth2app-tree) tree when AM is acting as an authorization server.

* Enforces a [transactional authorization](../am-authorization/transactional-authorization.html) policy.

To configure a transactional authentication tree, set the `transactionalOnly` property to `true` in the tree configuration. Send a PUT request to update the tree configuration, including the tree ID and all the nodes in the tree.

> **Collapse: Example**
>
> ```bash
> $ curl \
> --request PUT \
> --header "iPlanetDirectoryPro: AQIC5wM…​TU3OQ*" \
> --header "Content-Type: application/json" \
> --header "Accept-API-Version: protocol=2.1,resource=3.0" \
> --data '{
>   "entryNodeId": "c11e9cf8-ef48-4740-876f-6300e2f46aef",
>   "nodes": {
>    ...
>   },
>   "transactionalOnly": true
> }' \
> "https://am.example.com:8443/am/json/realms/root/realms/alpha/realm-config/authentication/authenticationtrees/trees/myAuthTree"
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

## Configure journey session duration in a tree

The maximum duration of a journey session is derived by AM as described in [Maximum duration](suspended-auth.html#maximum-duration).

You can override global and realm level duration values in an individual tree if required. For example, a tree that requires email verification could have a longer duration than a simple tree that authenticates users with a username and password.

|   |                                                                                                                                                                                                         |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Duration values set in a tree can be overridden at the node level. Learn more in [Maximum duration](suspended-auth.html#maximum-duration).Additionally, duration values set on inner trees are ignored. |

Learn more in [Suspend journey progress](suspended-auth.html).

To change the authentication tree duration, set the `treeTimeout` property to the required number of minutes in the tree configuration. Send a PUT request to update the tree configuration, including the tree ID and all the nodes in the tree.

> **Collapse: Example**
>
> ```bash
> $ curl \
> --request PUT \
> --header "iPlanetDirectoryPro: AQIC5wM…​TU3OQ*" \
> --header "Content-Type: application/json" \
> --header "Accept-API-Version: protocol=2.1,resource=3.0" \
> --data '{
>   "entryNodeId": "c11e9cf8-ef48-4740-876f-6300e2f46aef",
>   "nodes": {
>    ...
>   },
>   "treeTimeout": 10
> }' \
> "https://am.example.com:8443/am/json/realms/root/realms/alpha/realm-config/authentication/authenticationtrees/trees/myAuthTree"
> {
>   "_id": "myAuthTree",
>   "_rev": "1081620278",
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

## Configure authenticated session timeouts in a tree

Timeout settings for an authenticated session are derived by AM as described in [Configure authenticated session timeout settings](../am-sessions/session-state-session-termination.html#auth-session-termination-config).

You can override global and realm level timeout values in an individual tree if required. For example, a tree that implements MFA could have a longer authenticated session timeout than a simple tree that authenticates users with a username and password.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                         |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Session timeouts set in a tree can be overridden at the node or user level. Learn more in [Configure authenticated session timeout settings](../am-sessions/session-state-session-termination.html#auth-session-termination-config).Session timeout values set on inner trees are ignored. However, if session timeouts are set at the *node* level in an inner tree, the updated timeouts are used in the parent tree. |

Learn more in [Session termination](../am-sessions/session-state-session-termination.html).

To change the session timeouts in a tree, set the `maximumSessionTime` and `maximumIdleTime` properties to the required number of minutes in the tree configuration. Send a PUT request to update the tree configuration, including the tree ID and all the nodes in the tree.

> **Collapse: Example**
>
> The following example sets the `maximumSessionTime` to an hour and the `maximumIdleTime` to 15 minutes for authenticated sessions established through this tree:
>
> ```bash
> $ curl \
> --request PUT \
> --header "iPlanetDirectoryPro: AQIC5wM…​TU3OQ*" \
> --header "Content-Type: application/json" \
> --header "Accept-API-Version: protocol=2.1,resource=3.0" \
> --data '{
>   "entryNodeId": "c11e9cf8-ef48-4740-876f-6300e2f46aef",
>   "nodes": {
>    ...
>   },
>   "maximumSessionTime": 60,
>   "maximumIdleTime": 15
> }' \
> "https://am.example.com:8443/am/json/realms/root/realms/alpha/realm-config/authentication/authenticationtrees/trees/myAuthTree"
> {
>   "_id": "myAuthTree",
>   "_rev": "1081620278",
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

---

---
title: Configure webhooks
description: Configure webhooks to send HTTP POST requests to a server when specific events occur during authenticated sessions, such as user logout
component: pingam
version: 8.1
page_id: pingam:am-authentication:auth-tree-webhooks
canonical_url: https://docs.pingidentity.com/pingam/8.1/am-authentication/auth-tree-webhooks.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Authentication", "REST API", "Setup &amp; Configuration"]
page_aliases: ["authentication-guide:auth-tree-webhooks.adoc"]
section_ids:
  create-webhook: Create a webhook
  example-webhook: Example webhook
---

# Configure webhooks

Use *webhooks* to send an HTTP POST request to a server when a specific event occurs during an authenticated session, such as a user logging out.

Webhooks are used from within authentication trees by the [Register Logout Webhook node](https://docs.pingidentity.com/auth-node-ref/8.1/register-logout-webhook.html).

## Create a webhook

1. In the AM admin UI, go to Realms > *realm name* > Authentication > Webhooks.

   1. To create a new webhook, select Create Webhook, specify a webhook name, and click Create.

   2. To edit an existing webhook, select the name of the webhook.

   ![Creating a new authentication webhook.](_images/trees-webhook-create.png)

2. Configure the following settings:

   * Url

     Specifies the URL to which the HTTP POST is sent when the event occurs.

   * Body

     Specifies the body of the HTTP POST. You can send different formats by also setting the correct Content-Type header in the `Header` property, for example:

     * **Form Data**. Enter the body value in the format `parameter=value&parameter2=value2`, and set a `Content-Type` header of `application/x-www-form-urlencoded`.

     * **JSON Data**. Enter the body value in the format `{"parameter":"value","parameter2":"value2"}`, and set a `Content-Type` header of `application/json`.

   * Headers

     Specifies any HTTP headers to add to the POST.

     To add a header, enter the name of the header in the `Key` field, and the value, and click Add (➕).

     To remove a header, click Delete (✖).

   The fields in a webhook support variables for retrieving values from the authenticated session after the user has successfully authenticated.

   Specify a variable in the following format:

   ```
   ${variable_name}
   ```

   To access the type of webhook event, use the `WebhookEventType` parameter key to return one of the following possible values:

   * `LOGOUT`

   * `UPGRADE`

   * `DESTROY`

   * `MAX_TIMEOUT`

   * `IDLE_TIMEOUT`

   For example, to retrieve the event type as a query parameter: `&event=${WebhookEventType}`

   You can use a variable to access custom properties added to the session with the [Set Session Properties node](https://docs.pingidentity.com/auth-node-ref/8.1/set-session-properties.html) as well as the following default session properties:

   > **Collapse: Default Session Properties**
   >
   > | Property                     | Example value                                                  | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
   > | ---------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   > | `AMCtxId`                    | 22e73c81-708e-4849-b064-db29b68ef943-105372                    | The audit ID for the session. This is logged as the `trackingIds` field in AM access audit logs.                                                                                                                                                                                                                                                                                                                                                                     |
   > | `amlbcookie`                 | 01                                                             | The cookie that identifies the AM server that generated the session. For environments with multiple AM servers, this can be used for load balancer stickiness.                                                                                                                                                                                                                                                                                                       |
   > | `authInstant`                | 2022-02-28T14:06:31Z                                           | The exact time that authentication completed.                                                                                                                                                                                                                                                                                                                                                                                                                        |
   > | `AuthLevel`                  | 5                                                              | The authentication level of the session, determined by the login mechanism used to create the session. For example, a tree can have an authentication level of 10.Step-up authentication is triggered if an authentication level specified by an agent or policy that is designed to protect a resource, is greater than or equal to the value of the `AuthLevel` session property.For more information, see [Session upgrade](../am-sessions/session-upgrade.html). |
   > | `AuthType`                   | DataStore                                                      | *Not supported*.                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
   > | `CharSet`                    | UTF-8                                                          | The character set for the session, set to `UTF-8`.                                                                                                                                                                                                                                                                                                                                                                                                                   |
   > | `clientType`                 | genericHTML                                                    | The type of client, set to `genericHTML`.                                                                                                                                                                                                                                                                                                                                                                                                                            |
   > | `FullLoginURL`               | /am/XUI/?realm=%2Falpha                                        | The full login URL, including query parameters.                                                                                                                                                                                                                                                                                                                                                                                                                      |
   > | `Host`                       | 192.0.2.1                                                      | The originating IP address of the authentication request.                                                                                                                                                                                                                                                                                                                                                                                                            |
   > | `HostName`                   | 192.0.2.1                                                      | The host name that was used when the session was authenticated.                                                                                                                                                                                                                                                                                                                                                                                                      |
   > | `IndexType`                  | service                                                        | Based on the value of the `authIndexValue` query parameter during authentication. Typically, this is set to `service`.                                                                                                                                                                                                                                                                                                                                               |
   > | `Locale`                     | en\_US                                                         | The session locale.                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
   > | `loginURL`                   | /am/XUI                                                        | The base login URL. A subset of `FullLoginURL`.                                                                                                                                                                                                                                                                                                                                                                                                                      |
   > | `OidcSid`                    | g0wmSpoAIwH6HAwCnurvRcfYqh4                                    | Unique session ID used by AM to determine whether OIDC ID tokens granted for the same client relate to the same session. This appears when `Enable Session Management` (`storeOpsToken`) is set to true in the OAuth 2.0 provider settings.                                                                                                                                                                                                                          |
   > | `Organization`               | o=alpha,ou=services,dc=am,dc=example,dc=com                    | The DN of the realm where authentication took place.                                                                                                                                                                                                                                                                                                                                                                                                                 |
   > | `Principal`                  | id=bjensen,ou=user,o=alpha,ou=services,dc=am,dc=example,dc=com | The value of `sun.am.UniversalIdentifier`.                                                                                                                                                                                                                                                                                                                                                                                                                           |
   > | `Principals`                 | bjensen                                                        | The username of the user. *Not supported*.                                                                                                                                                                                                                                                                                                                                                                                                                           |
   > | `Service`                    | Login                                                          | The name of the tree that was used to authenticate this session.                                                                                                                                                                                                                                                                                                                                                                                                     |
   > | `successURL`                 | /am/console                                                    | The URL that was redirected to, upon a successful login request.                                                                                                                                                                                                                                                                                                                                                                                                     |
   > | `sun.am.UniversalIdentifier` | id=bjensen,ou=user,o=alpha,ou=services,dc=am,dc=example,dc=com | The DN of the user (username is lowercase).                                                                                                                                                                                                                                                                                                                                                                                                                          |
   > | `UserId`                     | bjensen                                                        | The `id` value from the `Principal` property.                                                                                                                                                                                                                                                                                                                                                                                                                        |
   > | `UserProfile`                | Required                                                       | Can be one of: `Required`, `Create`, `Ignore`, or `CreateWithAlias`. Based on the value of the `dynamicProfileCreation` authentication configuration. Values other than `Ignore` indicates that user profile attributes were mapped based on the `User Attribute Mapping to Session Attribute` setting. See [authentication configuration](authn-core-settings.html#authn-core-post-auth) for details.Default: `Required`.                                           |
   > | `UserToken`                  | bjensen                                                        | The username.                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
   > | `XUSRef`                     | 8700f1a5-904e-4849-8b2b-cb25296ef453-291173                    | If the [cross-upgrade session reference property](../setup/services-configuration.html#global-session-xusref) is enabled, this value identifies the session through its lifecycle. This is logged in the `trackingIds` field in AM audit logs for session creation and upgrade events.                                                                                                                                                                               |

## Example webhook

The following figure shows an example webhook using variable substitutions:

![Example authentication webhook.](_images/trees-webhook-example.png)

|   |                                                                                                                                                                                   |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Specifying a variable that isn't present in the user's session puts the literal variable text in the HTTP POST request, for example `user=${UserId}`, rather than `user=bjensen`. |

---

---
title: Core authentication attributes
description: Configure core authentication attributes that apply to all authentication performed to a PingAM realm
component: pingam
version: 8.1
page_id: pingam:am-authentication:authn-core-settings
canonical_url: https://docs.pingidentity.com/pingam/8.1/am-authentication/authn-core-settings.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Authentication", "Realms", "Setup &amp; Configuration"]
page_aliases: ["authentication-guide:authn-core-settings.adoc"]
---

# Core authentication attributes

Every AM realm has a set of authentication properties that applies to all authentication performed to that realm. The settings are referred to as core authentication attributes.

To configure core authentication attributes for an entire AM deployment, go to Configure > Authentication in the AM admin UI, and click Core Attributes.

To override the global core authentication configuration in a realm, go to Realms > *realm name* > Authentication > Settings in the AM admin UI.

`amster` service name: `Authentication`

> **Collapse: Global Attributes**
>
> The following properties are available under the Global Attributes tab:
>
> * LDAP Connection Pool Size
>
>   Sets a minimum and a maximum number of LDAP connections to be used by any authentication node that connects to a specific directory server. This connection pool is different to the SDK connection pool configured in the `serverconfig.xml` file.
>
>   Format is `host:port:minimum:maximum`.
>
>   `amster` attribute: `ldapConnectionPoolSize`
>
> * Default LDAP Connection Pool Size
>
>   Sets the default minimum and maximum number of LDAP connections to be used by any authentication node that connects to any directory server. This connection pool is different to the SDK connection pool configured in the `serverconfig.xml` file.
>
>   Format is `minimum:maximum`.
>
>   When tuning for production, start with 10 minimum, 65 maximum. For example, `10:65`.
>
>   `amster` attribute: `ldapConnectionPoolDefaultSize`
>
> * Remote Auth Security
>
>   When enabled, AM requires the authenticating application to send its SSO token. This allows AM to obtain the username and password associated with the application.
>
>   `amster` attribute: `remoteAuthSecurityEnabled`
>
> * Keep Post Process Objects for Logout Processing
>
>   When enabled, AM stores instances of post-processing classes into the authenticated session. When the user logs out, the original post-processing classes are called instead of new instances. This may be required for special logout processing.
>
>   Enabling this setting increases the memory usage of AM.
>
>   `amster` attribute: `keepPostProcessInstances`

> **Collapse: Core**
>
> The following properties are available under the Core tab:
>
> * Administrator Authentication Configuration
>
>   The default authentication tree used when an administrative user, such as `amAdmin`, logs in to the AM admin UI.
>
>   |   |                                                                                                                                       |
>   | - | ------------------------------------------------------------------------------------------------------------------------------------- |
>   |   | You can't set a tree configured to [always run](configure-auth-trees.html#enable-tree-completion) as the default authentication tree. |
>
> * Organization Authentication Configuration
>
>   The default authentication tree used when a non-administrative user logs in to AM.
>
>   |   |                                                                                                                                       |
>   | - | ------------------------------------------------------------------------------------------------------------------------------------- |
>   |   | You can't set a tree configured to [always run](configure-auth-trees.html#enable-tree-completion) as the default authentication tree. |
>
>   `amster` attribute: `orgConfig`

> **Collapse: User Profile**
>
> The following properties are available under the User Profile tab:
>
> * `User Profile`
>
>   Specifies whether a user profile needs to exist in the user datastore, or should be created on successful authentication. The possible values are:
>
>   * `true`. Dynamic.
>
>     After successful authentication, AM creates a user profile if one does not already exist. AM then issues the SSO token. AM creates the user profile in the user datastore configured for the realm.
>
>   * `createAlias`. Dynamic with User Alias.
>
>     After successful authentication, AM creates a user profile that contains the `User Alias List` attribute, which defines one or more aliases for mapping a user's multiple profiles.
>
>   * `ignore`. Ignored.
>
>     After successful authentication, AM issues an SSO token regardless of whether a user profile exists in the datastore. The presence of a user profile is not checked.
>
>     |   |                                                                                                                                                                           |
>     | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
>     |   | Any functionality that needs to map values to profile attributes, such as SAML 2.0 or OAuth 2.0, won't operate correctly if the User Profile property is set to `ignore`. |
>
>   * `false`. Required.
>
>     After successful authentication, the user must have a user profile in the user datastore configured for the realm in order for AM to issue an SSO token.
>
> Set this attribute's value to one of the following: `true`, `createAlias`, `ignore`, or `false`.
>
> * User Profile Dynamic Creation Default Roles
>
>   Specifies the distinguished name (DN) of a role to be assigned to a new user whose profile is created when either the `true` or `createAlias` options are selected under the User Profile property. There are no default values. The role specified must be within the realm for which the authentication process is configured.
>
>   This role can't be a filtered role. If you want to automatically assign specific services to the user, configure the Required Services property in the user profile.
>
>   |   |                                                                                                                            |
>   | - | -------------------------------------------------------------------------------------------------------------------------- |
>   |   | This functionality is [deprecated](https://docs.pingidentity.com/pingam/release-notes/stability.html#interface-stability). |
>
>   `amster` attribute: `defaultRole`
>
> * Alias Search Attribute Name
>
>   After a user is successfully authenticated, the user's profile is retrieved. AM first searches for the user based on the datastore settings. If that fails to find the user, AM will use the attributes listed here to look up the user profile. This setting accepts any datastore specific attribute name.
>
>   `amster` attribute: `aliasAttributeName`

> **Collapse: Account Lockout**
>
> The following properties are available under the Account Lockout tab:
>
> * Login Failure Lockout Mode
>
>   When enabled, AM deactivates the LDAP attribute defined in the Lockout Attribute Name property in the user's profile upon login failure. This attribute works in conjunction with the other account lockout and notification attributes.
>
>   `amster` attribute: `loginFailureLockoutMode`
>
> * Login Failure Lockout Count
>
>   The number of attempts a user has to authenticate within the time interval defined in Login Failure Lockout Interval before being locked out.
>
>   `amster` attribute: `loginFailureCount`
>
> * Login Failure Lockout Interval
>
>   The time in minutes during which failed login attempts are counted.
>
>   * If one failed login attempt is followed by a second failed attempt within this defined lockout interval, the lockout count starts, and the user is locked out if the number of attempts reaches the number defined by the Login Failure Lockout Count property.
>
>   * If an attempt within the defined lockout interval proves successful before the number of attempts reaches the number defined by the Login Failure Lockout Count property, the lockout count is reset.
>
>   `amster` attribute: `loginFailureDuration`
>
> * Email Address to Send Lockout Notification
>
>   One or more email addresses to which notification is sent if a user lockout occurs.
>
>   Separate multiple addresses with spaces, and append `|locale|charset` to addresses for recipients in non-English locales.
>
>   `amster` attribute: `lockoutEmailAddress`
>
> * Warn User After N Failures
>
>   The number of authentication failures after which AM displays a warning message that the user will be locked out.
>
> * Login Failure Lockout Duration
>
>   The number of minutes a user must wait after a lockout before attempting to authenticate again. Entering a value greater than `0` enables duration lockout and disables persistent (physical) lockout. *Duration lockout* means the user's account is locked for the number of minutes specified. The account is unlocked after the time period has passed.
>
>   `amster` attribute: `lockoutDuration`
>
> * Lockout Duration Multiplier
>
>   Defines a value by which to multiply the value of the Login Failure Lockout Duration attribute for each successive lockout. For example, if Login Failure Lockout Duration is set to 3 minutes, and the Lockout Duration Multiplier is set to 2, the user is locked out of the account for 6 minutes. After the 6 minutes has elapsed, if the user again provides the wrong credentials, the lockout duration is then 12 minutes. With the Lockout Duration Multiplier, the lockout duration is incrementally increased based on the number of times the user has been locked out.
>
>   `amster` attribute: `lockoutDurationMultiplier`
>
> * Lockout Attribute Name
>
>   The LDAP attribute used for persistent (physical) lockout. The default attribute is `inetuserstatus`, although the field in the AM admin UI is empty.
>
>   Possible values for the default attribute are `Active`, `Inactive` and `Deleted`.
>
>   The Lockout Attribute Value field must also contain an appropriate value.
>
>   `amster` attribute: `lockoutAttributeName`
>
> * Lockout Attribute Value
>
>   The value to set the lockout attribute to when an account is locked. The default value is `Inactive`, although the field in the AM admin UI is empty. The Lockout Attribute Name field must also contain an appropriate value.
>
>   `amster` attribute: `lockoutAttributeValue`
>
> * Invalid Attempts Data Attribute Name
>
>   The LDAP attribute used to hold the number of failed authentication attempts towards Login Failure Lockout Count. Although the field in the AM admin UI is empty, AM stores this data in the `sunAMAuthInvalidAttemptsDataAttrName` attribute defined in the `sunAMAuthAccountLockout` objectclass by default.
>
>   `amster` attribute: `invalidAttemptsDataAttributeName`
>
> * Store Invalid Attempts in Data Store
>
>   When enabled, AM stores the information regarding failed authentication attempts as the value of the `Invalid Attempts Data Attribute Name` in the user datastore. Information stored includes the number of invalid attempts, the time of the last failed attempt, lockout time and lockout duration. Storing this information in the identity store allows it to be shared among multiple instances of AM.
>
>   Enable this property to track invalid log in attempts when using [server-side](../am-sessions/cts-based-sessions.html) or [client-side](../am-sessions/client-based-sessions.html) journey sessions.
>
>   `amster` attribute: `storeInvalidAttemptsInDataStore`

> **Collapse: General**
>
> The following properties are available under the General tab:
>
> * Default Authentication Locale
>
>   Specifies the default language subtype to be used by the Authentication service. The default value is `en_US`.
>
>   `amster` attribute: `locale`
>
> * Identity Types
>
>   This property was used only for authentication with modules and chains and is no longer documented.
>
> * Pluggable User Status Event Classes
>
>   This property was used only for authentication with modules and chains and is no longer documented.
>
> * Use Client-Side Sessions
>
>   When enabled, AM assigns *client-side* sessions to users authenticating to this realm. Otherwise, AM users authenticating to this realm are assigned *server-side* sessions.
>
>   Learn more in [Introduction to sessions](../am-sessions/about-sessions.html).
>
>   `amster` attribute: `statelessSessionsEnabled`
>
> * Two Factor Authentication Mandatory
>
>   This property was used only for authentication with modules and chains and is no longer documented.
>
> * External Login Page URL
>
>   If the authentication user interface is hosted separately from AM, this property specifies the URL of the external login user interface.
>
>   When set, AM uses the provided URL as the base of the resume URI instead of using the Base URL Source Service to obtain the base URL.
>
>   If authentication is suspended in an authentication tree, AM uses this URL to construct the resume URI.
>
>   Find more information about the Base URL Source Service in [Configure the Base URL source service](../security/reverse-proxy.html#configure-base-url-source).
>
>   `amster` attribute: `externalLoginPageUrl`
>
> * Default Authentication Level
>
>   This property was used only for authentication with modules and chains and is no longer documented.

> **Collapse: Trees**
>
> The following properties are available under the Trees tab:
>
> * Authentication session state management scheme
>
>   The location where AM stores journey sessions.
>
>   Possible values are:
>
>   * `CTS`. AM stores journey sessions [server-side](../am-sessions/cts-based-sessions.html), in the CTS token store.
>
>   * `JWT`. AM sends the journey session [to the client](../am-sessions/client-based-sessions.html) as a JWT.
>
>   * `In-Memory`. AM stores journey sessions in its memory.
>
>   Learn more in [Introduction to sessions](../am-sessions/about-sessions.html).
>
>   Default: `JWT` (new installations), `In-Memory` (after upgrade)
>
>   `amster` attribute: `authenticationSessionsStateManagement`
>
> * Max duration (minutes)
>
>   The maximum allowed duration of a journey session, including any time spent in the suspended state, in minutes.
>
>   Values from `1` to `2147483647` are allowed.
>
>   Default: `5`
>
>   `amster` attribute: `authenticationSessionsMaxDuration`
>
> * Suspended authentication duration (minutes)
>
>   The length of time a journey session can be suspended in minutes.
>
>   Suspending a journey session allows time for out-of-band authentication methods, such as responding to emailed codes or performing an action on an additional device. The value must be less than or equal to the total time allowed for a journey session, specified in the `Max duration (minutes)` property.
>
>   Values from `1` to `2147483647` are allowed.
>
>   Default: `5`
>
> * Enable Allowlisting
>
>   When enabled, AM allowlists journey sessions to protect them against replay attacks.
>
>   Default: Disabled
>
>   `amster` attribute: `authenticationSessionsWhitelist`
>
> * Stops sending tokenId
>
>   When [HttpOnly session cookies](../security/sec-rest-httponly.html) are enabled and a client calls the `/json/authenticate` endpoint with a valid SSO token, AM returns an empty `tokenId` field.
>
>   Disable this property to have AM send a valid token ID in this scenario.
>
>   |   |                                                                                                                                                                                        |
>   | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
>   |   | For security reasons, you should leave this property enabled. If you have migrated an existing deployment, adjust your clients to expect an empty token ID, then enable this property. |
>
>   Default: Enabled
>
>   `amster` attribute: `authenticationTreeCookieHttpOnly`

> **Collapse: Security**
>
> The following properties are available under the Security tab:
>
> * Persistent Cookie Encryption Certificate Alias
>
>   Specifies the key pair alias in the AM keystore to use for encrypting persistent cookies.
>
>   |   |                                                                                                                                                                                                                                                                                                                                                                |
>   | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
>   |   | This property is deprecated. Use the rotatable secret mapping `am.authentication.nodes.persistentcookie.encryption` instead.If AM finds a matching secret in the secret store for `am.authentication.nodes.persistentcookie.encryption`, this alias is ignored.Learn more about rotating secrets in [Map and rotate secrets](../security/secret-mapping.html). |
>
>   Default: `test`
>
>   `amster` attribute: `keyAlias`
>
> * Zero Page Login
>
>   This property was used only for authentication with modules and chains and is no longer documented.
>
> * Zero Page Login Referer Allowlist
>
>   This property was used only for authentication with modules and chains and is no longer documented.
>
> * Zero Page Login Allowed Without Referer?
>
>   This property was used only for authentication with modules and chains and is no longer documented.
>
> * Add clear-site-data Header on Logout
>
>   When enabled, AM adds the [Clear-Site-Data](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Clear-Site-Data) header to successful logout responses. The `Clear-Site-Data` directive instructs the browser to delete relevant site data on logout. This directive includes `cache`, `cookies`, `storage`, and `executionContexts`.
>
>   Default: true (enabled)
>
>   `amster` attribute: `addClearSiteDataHeader`
>
> - Organization Authentication Signing Secret
>
>   The HMAC shared secret for signing RESTful authentication requests. This secret should be Base64 encoded and at least 128 bits in length. By default, a cryptographically secure, random value is generated.
>
>   When users attempt to authenticate to the UI, AM uses this secret to sign a JSON Web Token (JWT). The JWT contains the journey session ID, realm, and authentication index type value, but *doesn't* contain the user's credentials.
>
>   |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
>   | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
>   |   | * This configuration property is deprecated and will be removed in a future release.
>
>     If you're using a secret store of type Keystore, HSM, Google KMS, or Google Secret Manager, map the `am.authn.authid.signing.HMAC` secret label to a secret instead. If you map this secret label *and* set the configuration property, the mapped secret takes precedence.
>
>   * You can map multiple secrets to the `am.authn.authid.signing.HMAC` secret label to enable secret rotation.
>
>     AM signs the authentication token with the *active* secret but checks all mapped secrets when verifying the authentication token signature. Therefore, if you rotate the active secret while an authentication request is in progress, the returned authentication token can still be verified.
>
>     If you *delete* the secret that was used to sign an authentication token, the `authID` returned in the authentication request can't be verified and authentication fails. |
>
>   `amster` attribute: `sharedSecret`

> **Collapse: Post Authentication Processing**
>
> The following properties are available under the Post Authentication Processing tab:
>
> * Default Success Login URL
>
>   Accepts a list of values that specifies where users are directed after successful authentication. The format of this attribute is `client-type|URL` although the only value you can specify at this time is a URL which assumes the type HTML. The default value is `/am/console`. Values that do not specify HTTP have that appended to the deployment URI.
>
>   `amster` attribute: `loginSuccessUrl`
>
> * Default Failure Login URL
>
>   Accepts a list of values that specifies where users are directed after authentication has failed. The format of this attribute is `client-type|URL` although the only value you can specify at this time is a URL which assumes the type HTML. Values that do not specify HTTP have that appended to the deployment URI.
>
>   `amster` attribute: `loginFailureUrl`
>
> * Generate UserID Mode
>
>   This property was used only for authentication with modules and chains and is no longer documented.
>
> * Pluggable User Name Generator Class
>
>   This property was used only for authentication with modules and chains and is no longer documented.
>
> * User Attribute Mapping to Session Attribute
>
>   This property was used only for authentication with modules and chains and is no longer documented.

---

---
title: Create authentication trees
description: Create authentication trees in PingAM using the UI designer or REST API to define custom authentication flows with nodes and connectors
component: pingam
version: 8.1
page_id: pingam:am-authentication:create-auth-trees
canonical_url: https://docs.pingidentity.com/pingam/8.1/am-authentication/create-auth-trees.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Authentication", "Nodes &amp; Trees", "Setup &amp; Configuration"]
page_aliases: ["authentication-guide:create-auth-trees.adoc"]
section_ids:
  create-authn-tree-ui: Create a tree in the UI
  create-authn-tree-rest: Create a tree over REST
  example: Example
---

# Create authentication trees

## Create a tree in the UI

1. In the AM admin UI, go to Realms > *realm name* > Authentication > Trees and click Create Tree.

2. Enter a tree name, for example `myAuthTree`, and click Create.

   The authentication tree designer displays with the Start entry point connected to the Failure exit point.

   The authentication tree designer provides the following features on the toolbar:

   **Authentication tree designer toolbar**

   | Button                                                           | Usage                                                             |
   | ---------------------------------------------------------------- | ----------------------------------------------------------------- |
   | ![icon-trees-auto-layout](../_images/icon-trees-auto-layout.png) | Lay out and align nodes according to the order they're connected. |
   | ![icon-trees-full-screen](../_images/icon-trees-full-screen.png) | Toggle the designer window between normal and full screen layout. |
   | ![icon-trees-delete-node](../_images/icon-trees-delete-node.png) | Remove the selected node. You can't delete the Start entry point. |

3. Add a node to the tree by dragging the node from the Components panel on the left-hand side, and dropping it into the designer area.

   The list of authentication nodes is divided into categories. Click the category title to expand and collapse the categories.

   Use the filter text field to restrict the list of authentication nodes. This will match on the node's name and any tags applied to the node:

   ![Filters match on the node's name, and any tags applied to the node.](_images/auth-tree-component-panel.png)

4. Configure the node properties by using the right-hand panel.

   You can find more information on the available properties for each node in [Node reference](auth-nodes-reference.html).

5. Connect the node to the tree as follows:

   1. Select and drag the output connector from an existing node and drop it onto the new node.

   2. Select and drag the output connector from the new node and drop it onto an existing node.

   Nodes have one or more connectors, displayed as dots on the node. Unconnected connectors appear red until you connect them to other nodes in the tree.

   |   |                                                                                             |
   | - | ------------------------------------------------------------------------------------------- |
   |   | *Input* connectors appear on the left of the node, *output* connectors appear on the right. |

   A line is drawn between the connectors of connected nodes, and the connectors no longer appear red.

6. To change a connection, select and drag the green connector in the connection and drop it onto the new location.

7. Continue adding, connecting and removing nodes until the tree is complete, then click Save.

8. Test your authentication tree by navigating to a URL similar to the following: `https://am.example.com:8443/am/XUI/?realm=/alpha&service=myAuthTree#login`

## Create a tree over REST

To create an authentication tree over REST, send individual PUT requests to create each node. Then send a PUT request to create the tree, specifying a tree ID and including all the nodes in the tree. You can find information on the required parameters in the [online REST API reference](../am-rest/about-api-explorer.html), and the latest node definitions in [List latest node definitions](list-latest-node-definitions.html).

Consider the following when creating authentication trees using the REST API:

* You must re-create each node when creating a new authentication tree.

* Include the version of the node you want to create in the request URL.

  If the version doesn't exist, an HTTP 404 Not Found status code is returned, as follows:

  ```json
  {
      "code": 404,
      "reason": "Not Found",
      "message": "Resource 'n.0' not found"
  }
  ```

  |   |                                                                                                                                                                                                          |
  | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | To find the latest version for a node, send a POST request to the `realm-config/authentication/authenticationtrees/nodes/node-name` endpoint with `_action=getLatestType` as the query string parameter. |

* Each node must have a valid UUID as its identifier. You can generate UUIDs online, for example, using the [Online UUID Generator](https://www.uuidgenerator.net/).

  If you don't use a valid UUID, authentication will fail with the following error:

  ```
  ERROR: Could not get SMS service: authenticationTreesService java.lang.IllegalArgumentException: Invalid UUID string: 12345
  ```

* The `entryNodeId` field specified when creating the authentication tree is the UUID of the first node in the tree.

* The `outcome` field specified when creating the authentication tree is the UUID of the next node. This allows you to move between nodes.

* The Success and Failure nodes have the following static UUIDs:

  * Success node: `70e691a5-1e33-4ac3-a356-e7b6d60d92e0`

  * Failure node: `e301438c-0bd0-429c-ab0c-66126501069a`

  These UUIDs remain constant across all authentication trees and AM versions.

### Example

Complete these steps to create a simple authentication tree consisting of three nodes: [Username Collector node](https://docs.pingidentity.com/auth-node-ref/8.1/am-only/username-collector.html), [Password Collector node](https://docs.pingidentity.com/auth-node-ref/8.1/am-only/password-collector.html), and [Data Store Decision node](https://docs.pingidentity.com/auth-node-ref/8.1/data-store-decision.html).

1. Generate UUIDs for each of the nodes you want to create. This example uses the following UUIDs:

   * Username Collector node: `8f9d2280-caa7-433f-93a9-1f64f4cae60a`

   * Password Collector node: `54f14341-d1b7-436f-b159-d1f9b6c626eb`

   * Data Store Decision node: `3fc7ce22-fc79-4131-85f2-f1844709d042`

2. Authenticate to AM as the `amAdmin` user:

   ```bash
   $ curl \
   --request POST \
   --header "Content-Type: application/json" \
   --header "X-OpenAM-Username: amadmin" \
   --header "X-OpenAM-Password: password" \
   --header "Accept-API-Version: resource=2.0, protocol=1.0" \
   'https://am.example.com:8443/am/json/realms/root/realms/alpha/authenticate'
   {
       "tokenId":"AQIC5wM…​TU3OQ*",
       "successUrl":"/am/console",
       "realm":"/alpha"
   }
   ```

3. Create a version 2 Username Collector node, where the UUID is the one you generated in step 1:

   ```bash
   $ curl \
   --request PUT \
   --header "iPlanetDirectoryPro: AQIC5wM…​TU3OQ*" \
   --header "Content-Type: application/json" \
   --header "Accept-API-Version: protocol=2.1,resource=3.0" \
   --header "If-None-Match: *" \
   --data '{
     "_id": "8f9d2280-caa7-433f-93a9-1f64f4cae60a",
     "_type": {
       "_id": "UsernameCollectorNode",
       "name": "Username Collector"
     }
   }' \
   "https://am.example.com:8443/am/json/realms/root/realms/alpha/realm-config/authentication/authenticationtrees/nodes/UsernameCollectorNode/2.0/8f9d2280-caa7-433f-93a9-1f64f4cae60a"
   {
     "_id": "8f9d2280-caa7-433f-93a9-1f64f4cae60a",
     "_rev": "280717409",
     "prepopulate": false,
     "_type": {
       "_id": "UsernameCollectorNode",
       "name": "Username Collector",
       "collection": true,
       "version": "2.0"
     },
     "_outcomes": [
       {
         "id": "outcome",
         "displayName": "Outcome"
       }
     ]
   }
   ```

4. Create a version 1 Password Collector node, where the UUID is the one you generated in step 1:

   ```bash
   $ curl \
   --request PUT \
   --header "iPlanetDirectoryPro: AQIC5wM…​TU3OQ*" \
   --header "Content-Type: application/json" \
   --header "Accept-API-Version: protocol=2.1,resource=3.0" \
   --header "If-None-Match: *" \
   --data '{
     "_id": "54f14341-d1b7-436f-b159-d1f9b6c626eb",
     "_type": {
       "_id": "PasswordCollectorNode",
       "name": "Password Collector"
     }
   }' \
   "https://am.example.com:8443/am/json/realms/root/realms/alpha/realm-config/authentication/authenticationtrees/nodes/PasswordCollectorNode/1.0/54f14341-d1b7-436f-b159-d1f9b6c626eb"
   {
     "_id": "54f14341-d1b7-436f-b159-d1f9b6c626eb",
     "_rev": "792175357",
     "_type": {
       "_id": "PasswordCollectorNode",
       "name": "Password Collector",
       "collection": true,
       "version": "1.0"
     },
     "_outcomes": [
       {
         "id": "outcome",
         "displayName": "Outcome"
       }
     ]
   }
   ```

5. Create a version 1 Data Store Decision node, where the UUID is the one you generated in step 1:

   ```bash
   $ curl \
   --request PUT \
   --header "iPlanetDirectoryPro: AQIC5wM…​TU3OQ*" \
   --header "Content-Type: application/json" \
   --header "Accept-API-Version: protocol=2.1,resource=3.0" \
   --header "If-None-Match: *" \
   --data '{
     "_id": "3fc7ce22-fc79-4131-85f2-f1844709d042",
     "_type": {
       "_id": "DataStoreDecisionNode",
       "name": "Data Store Decision"
     }
   }' \
   "https://am.example.com:8443/am/json/realms/root/realms/alpha/realm-config/authentication/authenticationtrees/nodes/DataStoreDecisionNode/1.0/3fc7ce22-fc79-4131-85f2-f1844709d042"
   {
     "_id": "3fc7ce22-fc79-4131-85f2-f1844709d042",
     "_rev": "2145625368",
     "_type": {
       "_id": "DataStoreDecisionNode",
       "name": "Data Store Decision",
       "collection": true,
       "version": "1.0"
     },
     "_outcomes": [
       {
         "id": "true",
         "displayName": "True"
       },
       {
         "id": "false",
         "displayName": "False"
       }
     ]
   }
   ```

6. Create the authentication tree with these three nodes, where the UUIDs are the ones you used to create the nodes. Make sure you set `entryNodeId` to the UUID of the first node, include the node versions, and set the `outcome` of each node to the UUID of the next node:

   ```bash
   $ curl \
   --request PUT \
   --header "iPlanetDirectoryPro: AQIC5wM…​TU3OQ*" \
   --header "Content-Type: application/json" \
   --header "Accept-API-Version: protocol=2.1,resource=3.0" \
   --header "If-None-Match: *" \
   --data '{
     "entryNodeId": "8f9d2280-caa7-433f-93a9-1f64f4cae60a",
     "nodes": {
       "8f9d2280-caa7-433f-93a9-1f64f4cae60a": {
         "displayName": "Username Collector",
         "nodeType": "UsernameCollectorNode",
         "version": "2.0",
         "connections": {
           "outcome": "54f14341-d1b7-436f-b159-d1f9b6c626eb"
         }
       },
       "54f14341-d1b7-436f-b159-d1f9b6c626eb": {
         "displayName": "Password Collector",
         "nodeType": "PasswordCollectorNode",
         "version": "1.0",
         "connections": {
           "outcome": "3fc7ce22-fc79-4131-85f2-f1844709d042"
         }
       },
       "3fc7ce22-fc79-4131-85f2-f1844709d042": {
         "displayName": "Data Store Decision",
         "nodeType": "DataStoreDecisionNode",
         "version": "1.0",
         "connections": {
           "false": "e301438c-0bd0-429c-ab0c-66126501069a",
           "true": "70e691a5-1e33-4ac3-a356-e7b6d60d92e0"
         }
       }
     }
   }' \
   "https://am.example.com:8443/am/json/realms/root/realms/alpha/realm-config/authentication/authenticationtrees/trees/myNewTree"
   {
     "_id": "myNewTree",
     "_rev": "2061817222",
     "entryNodeId": "8f9d2280-caa7-433f-93a9-1f64f4cae60a",
     "innerTreeOnly": false,
     "noSession": false,
     "mustRun": false,
     "enabled": true,
     "transactionalOnly": false,
     "uiConfig": {},
     "nodes": {
       "8f9d2280-caa7-433f-93a9-1f64f4cae60a": {
         "displayName": "Username Collector",
         "nodeType": "UsernameCollectorNode",
         "version": "2.0",
         "connections": {
           "outcome": "54f14341-d1b7-436f-b159-d1f9b6c626eb"
         }
       },
       "54f14341-d1b7-436f-b159-d1f9b6c626eb": {
         "displayName": "Password Collector",
         "nodeType": "PasswordCollectorNode",
         "version": "1.0",
         "connections": {
           "outcome": "3fc7ce22-fc79-4131-85f2-f1844709d042"
         }
       },
       "3fc7ce22-fc79-4131-85f2-f1844709d042": {
         "displayName": "Data Store Decision",
         "nodeType": "DataStoreDecisionNode",
         "version": "1.0",
         "connections": {
           "false": "e301438c-0bd0-429c-ab0c-66126501069a",
           "true": "70e691a5-1e33-4ac3-a356-e7b6d60d92e0"
         }
       }
     }
   }
   ```

7. Verify the tree has been created in the AM admin UI. It should look similar to this:

   ![example tree](_images/example-tree.png)

---

---
title: Create logout hooks
description: Create logout hooks to run custom server-side logic when users log out, such as redirecting users or adding information to the logout response
component: pingam
version: 8.1
page_id: pingam:am-authentication:create-logout-hook
canonical_url: https://docs.pingidentity.com/pingam/8.1/am-authentication/create-logout-hook.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Authentication", "Nodes &amp; Trees", "Setup &amp; Configuration"]
section_ids:
  core-class-logout-hook: Core class of a logout hook
  register-logout-hook: Register a logout hook
---

# Create logout hooks

Use logout hooks to run custom server-side logic on logout. Logout hooks can perform tasks like redirecting the user on logout or adding information to the logout response that's sent to a client application.

You register a logout hook from a specific authentication node during the authentication journey. Registered logout hooks are run when:

* a user clicks the Log Out link from the self-service profile pages

* a POST request is sent to `/json/sessions/?_action=logout` to end a user's session

* a GET request is sent to the `/oauth2/connect/endSession` endpoint to end a user's session

AM includes the `SetResponseDetailsLogoutHook`, which adds logout details to the response when a tree ends with a logout. This hook is used by the [Set Logout Details node](https://docs.pingidentity.com/auth-node-ref/8.1/set-logout-details.html).

## Core class of a logout hook

This example shows an excerpt from the `SetResponseDetailsLogoutHook` class. The Set Logout Details node uses this logout hook to add logout details to the response on logout.

```java
public class SetResponseDetailsLogoutHook implements LogoutHook {                        1
    ...
    @Inject                                                                              2
    public SetResponseDetailsLogoutHook(@Assisted Optional<HttpServletRequest> request,
            @Assisted JsonValue data) {
        this.request = request;
        this.data = data;
    }

    @Override
    public void onLogout() {                                                             3
        request.ifPresent(request → {
            Map<String, Object> newLogoutDetails = data.asMap();
            if (newLogoutDetails != null && !newLogoutDetails.isEmpty()) {
                Map<String, Object> logoutDetails = new HashMap<>();
                Map<String, Object> existingLogoutDetails =
                        (Map<String, Object>) request.getAttribute(LOGOUT_DETAILS_ATTRIBUTE);
                if (existingLogoutDetails != null) {
                    logoutDetails.putAll(existingLogoutDetails);
                    logoutDetails.putAll(newLogoutDetails);
                } else {
                    logoutDetails = newLogoutDetails;
                }
                request.setAttribute(LOGOUT_DETAILS_ATTRIBUTE, logoutDetails);
            }
        });
    }
}
```

1 Your core class must implement the `LogoutHook` interface, which provides the `onLogout()` method for the authentication framework to call.

Learn more in the [LogoutHook](../_attachments/apidocs/org/forgerock/openam/auth/logouthook/api/LogoutHook.html) interface in the *AM Public API Javadoc*.

2 AM uses the Google Guice framework for dependency injection.

The `@Inject` annotation on the constructor tells Guice to create a new instance of the hook and provide all required service objects and contextual parameters.

The `@Assisted` annotation is for parameters that are specific to the current authentication transaction:

* [Request](../_attachments/apidocs/org/forgerock/http/protocol/Request.html): The HTTP request that started the authentication journey.

* [JsonValue](../_attachments/apidocs/org/forgerock/json/JsonValue.html): The data passed when registering the logout hook.

* [SSOToken](../_attachments/apidocs/com/iplanet/sso/SSOToken.html): The token that contains session details after a successful authentication.

* [Response](../_attachments/apidocs/org/forgerock/http/protocol/Response.html): The outgoing HTTP response that will be sent to the user agent. You can modify this response, for example, by adding cookies.

* [Realm](../_attachments/apidocs/org/forgerock/openam/core/realms/Realm.html): The realm where authentication is taking place.

3 The `onLogout()` method contains the hook's core logic. The framework runs this method on logout.

## Register a logout hook

To register a logout hook, your node class must call the `registerLogoutHook()` method.

For example, the `SetLogoutDetailsNode` registers its hook like this:

```java
    @Override
    public Action process(TreeContext context) throws NodeProcessException {
        JsonValue data = json(config.logoutDetails());
        return goToNext().registerLogoutHook(SetResponseDetailsLogoutHook.class, data).build();
    }
```

Learn more about the `registerLogoutHook()` method in [ActionBuilder](../_attachments/apidocs/org/forgerock/openam/auth/node/api/Action.ActionBuilder.html).

---

---
title: Create tree hooks
description: Create custom server-side logic that runs after authentication trees complete successfully, such as setting persistent cookies or logging audit events
component: pingam
version: 8.1
page_id: pingam:am-authentication:post-authn-plugins-treehook
canonical_url: https://docs.pingidentity.com/pingam/8.1/am-authentication/post-authn-plugins-treehook.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Authentication", "Nodes &amp; Trees", "Setup &amp; Configuration"]
page_aliases: ["authentication-guide:post-authn-plugins-treehook.adoc"]
section_ids:
  develop-tree-hooks-core: Core class of an authentication tree hook
  register-tree-hook: Register an authentication tree hook
---

# Create tree hooks

Use tree hooks to run custom server-side logic **after** an authentication tree successfully completes and creates a session. Tree hooks can perform post-authentication tasks, like setting persistent cookies, logging detailed audit events, or adding information to the final response that's sent to the client.

A hook isn't a standalone component. You register it from a specific authentication node during the authentication journey. When the tree finishes successfully, AM runs all registered hooks, which lets them act on the new session.

AM includes the following built-in authentication tree hooks:

| Tree hook                        | Used by node                                                                                                       | Details                                                                                                                                                                                                                                                                                                  |
| -------------------------------- | ------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `CreatePersistentCookieTreeHook` | [Set Persistent Cookie node](https://docs.pingidentity.com/auth-node-ref/8.1/set-persistent-cookie.html)           | Creates a JWT that contains session, encryption, and node details. The JWT is then used to set a persistent cookie on the response.                                                                                                                                                                      |
| `ErrorDetailsTreeHook`           | [Set Error Details node](https://docs.pingidentity.com/auth-node-ref/8.1/set-error-details.html)                   | Adds error details to the response when a tree ends in a failure state.To add error details to the message when the `acceptException()` method runs, inject the [TreeFailureResponse](../_attachments/apidocs/org/forgerock/openam/auth/node/api/TreeFailureResponse.html) object into your tree hook.   |
| `FailureDetailsTreeHook`         | [Set Failure Details node](https://docs.pingidentity.com/auth-node-ref/8.1/set-failure-details.html)               | Adds failure details to the response when a tree ends in a failure state.To add failure details to the message when the `acceptFailure()` method runs, inject the [TreeFailureResponse](../_attachments/apidocs/org/forgerock/openam/auth/node/api/TreeFailureResponse.html) object into your tree hook. |
| `SuccessDetailsTreeHook`         | [Set Success Details node](https://docs.pingidentity.com/auth-node-ref/8.1/set-success-details.html)               | Adds success details to the response.                                                                                                                                                                                                                                                                    |
| `UpdatePersistentCookieTreeHook` | [Persistent Cookie Decision node](https://docs.pingidentity.com/auth-node-ref/8.1/persistent-cookie-decision.html) | Recreates the specified persistent cookie with a new idle time and JWT `kid` header value.                                                                                                                                                                                                               |

## Core class of an authentication tree hook

This example shows an excerpt from the `UpdatePersistentCookieTreehook` class. The Persistent Cookie Decision node uses this tree hook to recreate and refresh a persistent cookie after a successful login.

```java
/**
 * A TreeHook for updating a persistent cookie.
 */
@TreeHook.Metadata(configClass = PersistentCookieDecisionNode.Config.class)     1
public class UpdatePersistentCookieTreeHook implements TreeHook {               2
    ...
    @Inject                                                                     3
    UpdatePersistentCookieTreeHook(@Assisted Request request,
            @Assisted Response response,
            @Assisted PersistentCookieDecisionNode.Config config,
            @Assisted Realm realm,
            PersistentJwtStringSupplier persistentJwtStringSupplier,
            PersistentCookieResponseHandler persistentCookieResponseHandler,
            SecretReferenceCache secretReferenceCache){
        this.request = request;
        this.response = response;
        this.config = config;
        this.persistentJwtStringSupplier = persistentJwtStringSupplier;
        this.persistentCookieResponseHandler = persistentCookieResponseHandler;
        this.secretCache = secretReferenceCache.realm(realm);
    }

    @Override
    public void accept() throws TreeHookException {                             4
        logger.debug("UpdatePersistentCookieTreeHook.accept");
        String orgName = PersistentCookieResponseHandler.getOrgName(response);
        Cookie originalJwt = getJwtCookie(request, config.persistentCookieName());

        if (originalJwt == null) {
            return;
        }
        // ... Logic to update and set cookie on response
    }
  //...
}
```

1 The `@TreeHook.Metadata` annotation registers the class as a Tree Hook and links it to a configuration class. In this case, it specifies that the hook uses the settings that you define for the `PersistentCookieDecisionNode`.

2 Your core class must implement the `TreeHook` interface, which makes sure it has methods like `accept()` that the authentication framework can call.

Learn more in the [TreeHook](../_attachments/apidocs/org/forgerock/openam/auth/node/api/TreeHook.html) interface in the *AM Public API Javadoc*.

3 AM uses the Google Guice framework for dependency injection.

The `@Inject` annotation on the constructor tells Guice to create a new instance of the hook and provide all required service objects and contextual parameters.

The `@Assisted` annotation is for parameters that are specific to the current authentication transaction:

* [Request](../_attachments/apidocs/org/forgerock/http/protocol/Request.html): The HTTP request that started the authentication journey.

* [Response](../_attachments/apidocs/org/forgerock/http/protocol/Response.html): The outgoing HTTP response that will be sent to the user agent. You can modify this response, for example, by adding cookies.

* `config`: The node configuration object. The type is defined by the `configClass` property in the `@TreeHook.Metadata` annotation.

* [Realm](../_attachments/apidocs/org/forgerock/openam/core/realms/Realm.html): The realm where authentication is taking place.

* [SSOToken](../_attachments/apidocs/com/iplanet/sso/SSOToken.html): The token that contains session details after a successful authentication.

* [TreeFailureResponse](../_attachments/apidocs/org/forgerock/openam/auth/node/api/TreeFailureResponse.html): An object that contains failure details for the `acceptFailure()` message and error details for the `acceptException()` message.

4 The `accept()` method contains the hook's core logic. The framework runs this method only after the authentication tree completes successfully.

You can optionally override the `acceptFailure()` or `acceptException()` methods to define what happens on failure or exception outcomes.

## Register an authentication tree hook

To register a tree hook, your node class must call the `addSessionHook()` method on an `ActionBuilder` instance.

For example, the `PersistentCookieDecisionNode` registers its hook like this:

```java
 @Override
 public Action process(TreeContext context) throws NodeProcessException {
    ...
    actionBuilder = actionBuilder
        .replaceSharedState(context.sharedState.copy().put(USERNAME, userName))
        .withUniversalId(identityService.getUniversalId(userName, realm, USER))
        .withIdentifiedIdentity(userName, USER)
        .putSessionProperty(generateSessionPropertyName(config.persistentCookieName()),
                config.persistentCookieName())
        .addSessionHook(UpdatePersistentCookieTreeHook.class, nodeId, getClass().getSimpleName());
    ...
```

You can specify a node version in the `addSessionHook()` method. This lets you associate different tree hooks with different node versions.

If you omit the version, it defaults to version 1 of the node.

Learn more about the `addSessionHook()` method in [ActionBuilder](../_attachments/apidocs/org/forgerock/openam/auth/node/api/Action.ActionBuilder.html).

---

---
title: Custom scripted nodes
description: Create custom node types with server-side scripts to reuse common functionality in authentication journeys and dynamically set values or outcomes
component: pingam
version: 8.1
page_id: pingam:am-authentication:node-designer
canonical_url: https://docs.pingidentity.com/pingam/8.1/am-authentication/node-designer.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Authentication", "Node Designer", "Nodes &amp; Trees"]
page_aliases: ["authentication-guide:node-designer.adoc"]
section_ids:
  design_secure_nodes: Design secure nodes
  create-node-type: Create a node type
  import-node-type: Import a node type
  export-node-type: Export a node type
  use_your_custom_node_type: Use your custom node type
  delete-node-type: Delete a node type
  example_generate_jwt_node: "Example: Generate JWT node"
---

# Custom scripted nodes

With AM's Node Designer, you can create your own node types to reuse common functionality in journeys. Define node properties and run custom server-side scripts in these nodes to dynamically set values and decide the outcome of authentication journeys.

To write a script for your custom node, you can use any of the next-generation script bindings available to the [Scripted Decision node API](../am-scripting/scripting-api-node.html), including `httpClient`, `cacheManager`, and `openidm`.

For example, use the Node Designer to create node types that perform functions such as:

* Update email addresses for users based on their location

* Add users to a particular group

* Generate a JWT and store it in shared state

* Gather user input through [callbacks](../am-scripting/scripting-api-node.html#scripting-api-node-callbacks)

New node types appear in the Components panel of the tree designer ready for you to include in your authentication journey with a simple drag and drop. You can use custom node types in your journey like any other node, including as part of inner trees, in page nodes, and with Configuration Provider nodes.

You can also share the functionality by exporting your custom node type and importing it into a different environment.

|   |                                                                                                                                                                                                                                        |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | You can't use library scripts with custom scripted nodes. Custom scripted nodes are designed to be self-contained units so that you can import and export them. Import and export functionality isn't compatible with library scripts. |

## Design secure nodes

Before you start creating custom scripted nodes, read the following points of best practice to make sure your custom nodes are as secure as possible.

* Don't add sensitive data to shared state

  Store sensitive information such as passwords in secrets.

* Sanitize input data

  Remove sensitive information before using or storing data.

* Don't log sensitive data

  Make sure you don't output sensitive information to logs.

Find more information in [Security considerations](../auth-nodes/secure-nodes.html).

## Create a node type

1. In the AM admin UI, go to Realms > *realm name* > Authentication > Node Designer and click [icon: plus, set=fa]Create Node Type.

   |   |                                                                                                                                                               |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | Custom node types are global objects and don't belong to a realm, so even if you create a node type in one realm, you can still access it from another realm. |

2. On the `New Node Type` page, enter a unique service name using lowercase letters or numbers only. Also, enter a suitable name for your node type to be displayed in the tree designer.

   For example, `setemployeedetails` and `Set Employee Details`, respectively.

   The service name is a fixed reference to the node type, but you can change the display name later.

3. In the Node Designer editor, set or review the following fields:

   | Field         | Value                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
   | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | Display Name  | The name displayed in the tree editor. This provides the default name for new nodes of this type. Must be unique.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
   | Description   | The description for the node type. The description isn't displayed in the editor.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
   | Outcomes      | Enter one or more names for the outcome paths of this node. You can't name an outcome `Script Error` because that's reserved for the `Error Outcome` path.For example, `true` `false`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
   | Node Inputs   | Optionally, list the node state data available to the node.For example, `username`.Default: `*`(The node can access all shared and transient state data)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
   | Node Outputs  | Optionally, list the data the node outputs to shared state.Default: `*`(The node sets all state data)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
   | Properties    | A JSON object that contains the node configuration. The keys can be accessed from your script through the `properties` binding. The values depend on the journey configuration.For example, this configuration defines properties for an employee's location and group:```json
   {
     "emp_group": {                                  (1)
       "title": "Employee group",                    (2)
       "description": "Specify all relevant groups", (3)
       "required": true,                             (4)
       "type": "STRING",                             (5)
       "defaultValue": ["Admin", "Sales"],           (6)
       "multivalued": true                           (7)
     },
     "emp_location": {
       "title": "Employee location",
       "description": "Select the primary location",
       "required": true,
       "type": "STRING",
       "defaultValue": "UK",
       "options": {                                  (8)
           "UK": "London",
           "US": "New York"
       }
     }
   }
   ```1	The key that can be accessed from the script, for example, properties.emp\_group.&#xA;2	Required. The title of the property appears as the property name. Must be unique.&#xA;3	The description appears as the tooltip in the tree designer.&#xA;4	Required. Whether it's mandatory to enter a value for this property.&#xA;5	Required. The input type: STRING, NUMBER, BOOLEAN, or OBJECT.&#xA;6	The initial value(s) for this property that's displayed in the UI. If you define options, this value must match one of the option keys.&#xA;7	Enables multiple values for a single property for all types except OBJECT. Must be false if options are provided. Default: false.&#xA;8	Define key/value pairs to display options in a drop-down list. The key must only contain alphanumeric characters and underscores and can't consist only of digits. The values displayed in the list can be any valid string.These example properties display in the tree designer view as follows:![node designer properties](_images/node-designer-properties.png) |
   | Script        | Write or paste in a [next-generation script](../am-scripting/next-generation-scripts.html) that runs when your custom node is processed.Use the Node Designer binding, `properties`, to reference the configured values that you've defined in the Properties field. In addition to `properties`, your script has access to all the Scripted Decision node script bindings, such as `callbacks`, `nodeState`, and `idRepository`. Find examples of scripts and how to use the bindings in the [Scripted Decision node API](../am-scripting/scripting-api-node.html).&#xA;&#xA;Although custom nodes are similar to Scripted Decision nodes, they have their own script context and a separate thread pool. Learn more about scripting thread pools in Thread pools.For example, this script adds an email address to the user profile and stores employee details in node state:```javascript
   var username = nodeState.get("username");
   var identity = idRepository.getIdentity(username);

   if (properties.emp_location == "UK") {
       identity.addAttribute("mail", username + "@example.co.uk");
   }
   else {
       identity.addAttribute("mail", username + "@example.com");
   }
   identity.store();

   nodeState.putShared("location", properties.emp_location);
   nodeState.putShared("group", properties.emp_group);

   action.goTo("true");
   ```	Node Designer scripts only appear in the Node Designer. You can't manage these scripts under Realms > realm name > Scripts.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
   | Error Outcome | Enable to add an extra path for scripting errors, for example, if the script references an outcome that's not defined in the Outcomes field. The outcome appears on the node as Script Error.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
   | Category      | Select a category from the list. Your node type appears under this section in the tree designer view.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
   | Tags          | Add tags to organize the node. You can use these to search for a node type in the tree designer.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
   | Changelog     | Optionally, add a changelog for this version of the node to provide a record of changes for a node.&#xA;&#xA;To retrieve all the changelogs for a node, send a POST request to the realm-config/authentication/authenticationtrees/nodes/designer-service-name?\_action=versionInfo endpoint.&#xA;&#xA;Example response&#xA;\[&#xA;  {&#xA;    "version": "1.0",&#xA;    "changelog": "No changelog entry found"&#xA;  },&#xA;  {&#xA;    "version": "2.0",&#xA;    "changelog": "Updated the node to replace the secretValue attribute with secretLabelIdentifier."&#xA;  }&#xA;]&#xA;&#xA;Include the node version in the request URL to return the changelog only for the specified node version.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |

4. Save your changes.

## Import a node type

To reuse node types in other environments, you can import a JSON file containing one or more node types.

1. In the AM admin UI, go to Node Designer and click Import.

2. On the Import Nodes page, drag the JSON file into the Import File box or click in the box to open a file browser and select the JSON file.

3. Click Import.

   AM displays an error if a node of that type already exists or the JSON is invalid.

## Export a node type

To reuse node types in other environments, you can export them to a JSON file.

1. In the AM admin UI, go to Node Designer and select one or more node types from the list to export.

2. Click Export.

3. The node types are downloaded to a JSON file.

|   |                                                                                                                                                                                                                                                                                                                                                                                                           |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Exporting node types doesn't include external dependencies. To make sure exported node types work as expected, record dependencies such as those relied on by bindings that interact with external services and configuration, for example, `openidm`, `secrets`, and `httpClient`.You can then use these notes to replicate the dependencies when importing the node types into a different environment. |

## Use your custom node type

Create a journey that references your new node type and configure values appropriate for that journey.

1. In the AM admin UI, go to Realms > *realm name* > Authentication > Trees and [create a tree](create-auth-trees.html#create-authn-tree-ui).

2. Search for your custom node type in the Components panel using the tags, the name, or the category of your node.

3. Add the node to your tree and set its properties to values that are appropriate for your authentication journey.

4. If you need to make changes to your node type, edit its configuration in the Node Designer and return to the tree designer.

   You might need to delete the node from your journey and select a new instance to view updates.

The following example includes the custom node type, Set Employee Details in a journey that sets user-specific information based on node configuration after a successful authentication.

![node designer tree example](_images/node-designer-tree-example.png)

The node is configured with the following values:

* Employee location

  `New York`

* Employee group

  `Admin` `Sales`

For a user, `bjensen`, the node adds the email address `bjensen@example.com` to the `mail` identity profile attribute and the debug node outputs the following updates to `nodeState`:

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

## Delete a node type

Deleting a custom node type is a permanent operation. You won't be able to retrieve it after it's deleted.

1. In the AM admin UI, go to Realms > *realm name* > Authentication > Node Designer.

2. Select the checkbox next to one or more node types. Click x Delete.

|   |                                                                            |
| - | -------------------------------------------------------------------------- |
|   | You can't delete a custom node type if a journey uses a node of that type. |

## Example: Generate JWT node

This example generates a signed JWT using the HMAC SHA-256 algorithm based on tree configuration and the username. It then sets the generated key in shared state.

1. Create a custom node type with the following settings:

   | Field         | Value                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
   | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | Display Name  | Generate JWT                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
   | Description   | Select an algorithm to generate a key for encryption / decryption purposes.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
   | Outcomes      | `true` `false`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
   | Node Inputs   | \*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
   | Node Outputs  | \*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
   | Properties    | ```json
   {
     "issuer": {
       "title": "Issuer",
       "type": "STRING",
       "description": "The issuer (iss) claim",
       "required": true
     },
     "audience": {
       "title": "Audience",
       "type": "STRING",
       "description": "The audience (aud) claim",
       "required": true
     },
     "signingkey": {
       "title": "HMAC Signing Key",
       "type": "STRING",
       "description": "The secret label for the HMAC signing key",
       "defaultValue": "scripted.node.secret",
       "required": true
     },
     "validity": {
       "title": "Validity (minutes)",
       "type": "NUMBER",
       "required": true,
       "defaultValue": 5
     }
   }
   ```           |
   | Script        | ```java
   var aud = properties.audience;
   var iss = properties.issuer;
   var validity = properties.validity;
   var secret = properties.signingkey;

   var signingkey = secrets.getGenericSecret(secret).getAsUtf8();

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
     action.goTo("true");
   } else {
     action.goTo("false");
   }
   ``` |
   | Error Outcome | Enabled                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
   | Tags          | `Utilities`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |

2. Create a journey that includes an instance of the new node type.

   For example:

   ![Generate JWT node example tree](_images/node-designer-jwt-tree.png)

3. Configure the node with a secret label mapped to an HMAC signing secret and values for the `issuer` and `audience` JWT claims.

   ![node designer jwt properties](_images/node-designer-jwt-properties.png)

4. Test the journey. The JWT is added to shared state:

   ```json
   {
       "realm": "/alpha",
       "assertionJwt": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUz...rXNQ4QhFeIBC2LiH-Sr72Q4",
       ...
   }
   ```

---

---
title: Customize nodes
description: Customize PingAM authentication journey nodes by using Node Designer or building custom Java nodes, which require fewer files and simpler deployment than modules
component: pingam
version: 8.1
page_id: pingam:am-authentication:customize-nodes
canonical_url: https://docs.pingidentity.com/pingam/8.1/am-authentication/customize-nodes.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  files_used_in_module_and_node_development: Files used in module and node development
  methods_used_in_module_and_node_development: Methods used in module and node development
---

# Customize nodes

Customizing nodes is simpler than customizing authentication modules. You have two options, depending on your use case:

* Use [AM's Node Designer](node-designer.html) to create your own scripted node types to reuse common functionality in journeys.

* Build your own [custom Java nodes](../auth-nodes/preface.html).

  Node development requires fewer files, has fewer methods to implement, and has a simpler deployment process compared to module development.

## Files used in module and node development

The following table shows how files from a typical module development project map to their equivalents in a node development project:

| Module files                                                                                    | Node equivalent           | Details                                                                               |
| ----------------------------------------------------------------------------------------------- | ------------------------- | ------------------------------------------------------------------------------------- |
| `pom.xml`                                                                                       | `pom.xml`                 | The Maven project file structure is similar for both.                                 |
| * `amAuthSampleAuth.xml`

* `SampleAuth.java`

* `SampleAuthPrincipal.java`

* `SampleAuth.xml` | `authNodeName.java`       | The logic from multiple module files is consolidated into the single core Java class. |
| `amAuthSampleAuth.properties`                                                                   | `authNodeName.properties` | The properties file for UI strings has a direct equivalent.                           |
| `SampleAuthPlugin.java`                                                                         | `authNodeNamePlugin.java` | The plugin registration class has a direct equivalent.                                |

Learn more about the node development files in [Files contained in the Maven project](../auth-nodes/preparing-for-nodes.html#files-in-maven-project)

## Methods used in module and node development

The following table shows the method mapping between the SampleAuth module example and custom nodes:

| Module methods                                                                                                                                         | Node equivalent                                 | Details                                                                                                                                                                                                                                                                                                 |
| ------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `public void init(…​)`                                                                                                                                 | `public interface Config {}`                    | The `init` method, which handled module configuration via a `Map` of options, is replaced by a strongly-typed `Config` interface. This provides better type safety and makes configuration clearer.                                                                                                     |
| * `public int process(…​)`

* `public Principal getPrincipal()`

* `setErrorText(…​)`, `substituteUIStrings(…​)`

* Methods from the `Principal` class | `public Action process(TreeContext context) {}` | The complex state management, callback handling, and principal creation logic spread across multiple methods in the module are consolidated into a single `process` method. This method returns an `Action` object that encapsulates the outcome and any necessary state changes, simplifying the flow. |

Learn more about the node development methods in [Config interface](../auth-nodes/core-config.html) and [Action class](../auth-nodes/core-action.html).

---

---
title: Implement CAPTCHA
description: Configure CAPTCHA services including Google reCAPTCHA and hCaptcha to verify users are human within authentication trees
component: pingam
version: 8.1
page_id: pingam:am-authentication:captcha-support
canonical_url: https://docs.pingidentity.com/pingam/8.1/am-authentication/captcha-support.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Authentication", "Nodes &amp; Trees"]
page_aliases: ["authentication-guide:captcha-support.adoc"]
section_ids:
  captcha-postman-collection: Test the CAPTCHA node
---

# Implement CAPTCHA

CAPTCHA is a way to challenge a user to verify that they are human, and includes a number of different services. Choose the CAPTCHA service that best suits your requirements. The default configuration in the [CAPTCHA node](https://docs.pingidentity.com/auth-node-ref/8.1/captcha.html) is for Google's reCAPTCHA service. You must provide a CAPTCHA Site Key and CAPTCHA Secret Key to use the node.

## Test the CAPTCHA node

ForgeRock provides a [Postman](https://www.postman.com/) collection to configure AM to test the CAPTCHA node. The Postman collection contains the queries to demonstrate the CAPTCHA node with reCAPTCHA V2, V3 and with hCaptcha. Before you start, set up a reCAPTCHA V2 and V3 site, and an hCaptcha site, and copy their site and secret keys.

1. Download and install [Postman](https://www.postman.com/downloads).

2. Download the [ForgeRock CAPTCHA Collection](../_attachments/collections/ForgeRock_CAPTCHA_Collection.json).

3. Import the collection into Postman:

   * Select File > Import …​ > Upload Files.

   * Select the CAPTCHA collection, and click Open, then click Import.

4. Change the collection variables to suit your environment:

   * On the Collections tab, select the ForgeRock CAPTCHA Collection.

   * Click on the Variables tab, and set the value of at least the following variables:

     * `URL_base`

     * `admin_password`

     * `demo_username`

     * `demo_password`

   * Click Update to save your changes.

     You are ready to run the collection.

5. After creating the authentication trees, visit the following URLs in your browser to demonstrate the login flow for each CAPTCHA type:

   * URL\_base/XUI/?realm=sub\_realm\&service=recaptchav3

   * URL\_base/XUI/?realm=sub\_realm\&service=recaptchav2

   * URL\_base/XUI/?realm=sub\_realm\&service=hcaptcha

   Use the demo\_username and demo\_password to log in.