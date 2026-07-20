---
title: Authenticate endpoints
description: To authenticate to Advanced Identity Cloud using REST, send an HTTP POST request to the json/authenticate endpoint. Specify the realm hierarchy, starting at the root; for example, /realms/root/realms/alpha.
component: pingoneaic-api
page_id: pingoneaic-api:am-authentication:authenticate-endpoint-parameters
canonical_url: https://developer.pingidentity.com/pingoneaic-api/am-authentication/authenticate-endpoint-parameters.html
keywords: ["Authentication", "Nodes &amp; Trees", "Journeys", "REST API"]
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

If not specified, Advanced Identity Cloud authenticates the user against the [default journey](https://docs.pingidentity.com/pingoneaic/latest/am-authentication/realm-auth-config.html) configured for the realm.

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

  Note that the resource must be URL-encoded. Authentication will fail if no policy matches the resource.

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

  Learn more in <https://docs.pingidentity.com/pingoneaic/latest/am-authorization/transactional-authorization.html>.

### `authIndexValue`

This parameter sets a value for the specific `authIndexType`.

Required: Yes, when using the `authIndexType` parameter.

### `noSession`

When set to `true`, this parameter specifies that Advanced Identity Cloud should not return a session when authenticating a user.

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

## `/json/authenticate/backchannel`

Lets a third-party federation service initiate and monitor a [backchannel authentication](backchannel-authentication.html) flow.

### `/authenticate/backchannel/initialize`

Initiates a backchannel authentication request. This endpoint has no additional parameters.

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

    The subject name.

* `data` (object, optional)

  Data to add to the initial authentication journey state, as key-value pairs. For example:

  ```none
  "type": "service",
  "value": "Login"
  ```

  Restricted fields: `realm` and `authLevel`.

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
>     "name": "bjensen"
>   },
>   "trackingId": "Y5tyzQi9cGVJjy2L"
> }',
> "https://[.var]##<tenant-env-fqdn>##/am/json/realms/root/realms/alpha/authenticate/backchannel/initialize"
> {
>   "transaction": "b3070138-cd73-4ef2-bd58-812602d7b757",
>   "redirectUri": "https://[.var]##<tenant-env-fqdn>##/am/UI/Login?realm=/alpha&authIndexType=transaction&authIndexValue=b3070138-cd73-4ef2-bd58-812602d7b757"
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
> "https://[.var]##<tenant-env-fqdn>##/am/json/realms/root/realms/alpha/authenticate/backchannel/info"
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
description: Advanced Identity Cloud provides the /json/authenticate endpoint for authentication, and the /json/sessions endpoint for managing sessions and logging out.
component: pingoneaic-api
page_id: pingoneaic-api:am-authentication:authn-rest
canonical_url: https://developer.pingidentity.com/pingoneaic-api/am-authentication/authn-rest.html
keywords: ["Authentication", "REST API"]
page_aliases: ["index.adoc"]
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
title: Backchannel authentication
description: Backchannel authentication lets a third-party federation service initiate authentication with Advanced Identity Cloud on behalf of a user. The federation service collects the user data and transmits this data directly to Advanced Identity Cloud. Advanced Identity Cloud redirects the user to complete the authentication process without having to re-enter the collected data. Backchannel authentication provides a seamless user experience and is more secure as users don't have to enter credentials multiple times.
component: pingoneaic-api
page_id: pingoneaic-api:am-authentication:backchannel-authentication
canonical_url: https://developer.pingidentity.com/pingoneaic-api/am-authentication/backchannel-authentication.html
keywords: ["Authentication", "Backchannel"]
section_ids:
  demonstrate-backchannel-authentication: Demonstrate backchannel authentication
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

Backchannel authentication lets a third-party federation service initiate authentication with Advanced Identity Cloud on behalf of a user. The federation service collects the user data and transmits this data directly to Advanced Identity Cloud. Advanced Identity Cloud redirects the user to complete the authentication process without having to re-enter the collected data. Backchannel authentication provides a seamless user experience and is more secure as users don't have to enter credentials multiple times.

Backchannel authentication uses a [transactional authorization](https://docs.pingidentity.com/pingoneaic/latest/am-authorization/transactional-authorization.html) process with requests sent to the [backchannel authentication REST endpoints](#backchannel-endpoints). Data supplied by the federation service is saved in a *transaction* with a specific transaction ID. When the user starts their authentication journey in Advanced Identity Cloud, the transaction locates the federation-provided data and inserts it into the journey's shared state.

The following diagram illustrates the backchannel authentication flow.

![backchannel-auth](https://kroki.io/plantuml/svg/eNqFVNuO0zAQffdXjLIPy0rbBq3gpUClEkCqxEqoaT_AiSeJqWMH22kpf8Rv8GWMc9k2sIW8RLLPnDlzziTxLQN6EtOcrCwrD79-wsPLh1cwC6_X8EXqEtYCtZf-RDDbGMu9NJp1ddtKOsiNQKC3N5AhtA4F4PdctU4eUJ1AakJojXkog6P01T9YA6kzhT9yi2AsOLQHmaObdzdX68Bo6mSKAq0D1-bVsyRBocKSK-gYJLqO9VgZqPgBwylaUi81ATlkUovQUFGtdgi8tIg1gf4zxHzwxkCJGumMSknDtxZ1jiAk8fAaCmtq8MG_Qiq8h8YaktgrkmMLxbXfPX6-h8r7ZhHHTThoazV3prU5FsaWONfo45F-XvlasduY8dYb3dYZWojeZsubm7uIMVKqEN7zfJ9XnCJRQLAqTJD3NhbKHBlruKUT2VAviHbkXgTchWDt9OoTChz8HyzugAWKKW4lDpy0iQu3lGlFB16tE8YC9WxJdQtYnQVhb8JzbRgj8GxJxQtIUQuwYX7nQ8IXI2GcnWeNpabMuZI_QtKiMXJMMrQHwT0HTlQ8DzkQ0x5py6nFoCwNK3KG0lpz8JZrx_vNpoNkm74hKb61enK1_tAx025JS98B7DbrYYLA9zTC-RZe0CBXbIOvlL3G013HOW0zWtkZk5i6UUg2hk1dPf6Z9UAzjNgL2YwaujlJw9_eT9Ia8STyCvicU1JhvqeN534iuqIlyBDDT6KXKy5N3_RmRtuLitRz3zp4B-kuST6macR-AxduqEQ=?id=figure-backchannel-auth)

## Demonstrate backchannel authentication

These steps use an OAuth 2.0 client to mimic the third-party federation service. The client initializes the backchannel authentication transaction and Advanced Identity Cloud redirects the user to a simple login journey to complete authentication.

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

This example assumes a simple journey that lets the user log in by supplying only their password. The username is provided by the third-party federation service as part of the backchannel authentication request.

The name of the journey is `Login`.

![backchannel auth journey](../_images/backchannel-auth-journey.png)

|   |                                                                                                                                                                                                                                                                                                                                                                             |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | To prevent users from authenticating directly through this journey, either for security reasons or because the journey is insufficient as a complete authentication service, configure it as a [transactional authentication journey](https://docs.pingidentity.com/pingoneaic/latest/am-authentication/auth-nodes-and-journeys.html#configure-transactional-auth-journey). |

### Configure the OAuth 2.0 provider service

1. Under Native Consoles > Access Management, go to Realms > *Realm Name* > Services > OAuth2 Provider > Advanced.

2. In the Client Registration Scope Allowlist field, add `back_channel_authentication` and click Save.

3. In the Grant Types field, add `Client Credentials` if it isn't already there.

Find more information in [Authorization server configuration](https://docs.pingidentity.com/pingoneaic/latest/am-oauth2/oauth2-configure-authz.html).

### Create an OAuth 2.0 client

The OAuth 2.0 client represents the third-party federation service.

Create a confidential client named `myClient` with the following configuration:

* **Client ID**: `myClient`

* **Client secret**: `my-client-secret`

* **Scope(s)**: `back_channel_authentication`

* **Grant Types**: `Client Credentials`

Find more information in [Client application registration](https://docs.pingidentity.com/pingoneaic/latest/am-oauth2/oauth2-register-client.html).

### Configure the Base URL Source

By default, the base URL of the redirect URI is retrieved from the incoming HTTP request. For this demonstration, configure a fixed base URL with the value of your Advanced Identity Cloud host.

1. Under Native Consoles > Access Management, go to Realms > *Realm Name* > Services and click Add a Service.

2. Select `Base URL Source` and click Create.

3. In the Base URL Source list, select `Fixed value`.

4. Set the Fixed value base URL to your Advanced Identity Cloud host, for example:

   ```bash
   https://<tenant-env-fqdn>/am
   ```

5. Click Save Changes.

### Allowlist session properties (optional)

When you query the state of a successful backchannel authentication, you might want to obtain certain session details. To do this, configure the Session Property Whitelist Service and specify any properties to be included in a query response.

1. Go to Realms > *Realm Name* > Services, and click Add a Service.

2. Select `Session Property Whitelist Service` and click Create.

3. In the Allowlisted Session Property Names, enter the session properties you want to obtain.

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

Find more information in [Client application authentication](https://docs.pingidentity.com/pingoneaic/latest/am-oauth2/oauth2-client-auth.html).

### Initialize the backchannel authentication transaction

This section assumes that a user has already signed on to the third-party federation service and that the service has their *username*.

As the OAuth 2.0 client, send an HTTP POST request to the `/authenticate/backchannel/initialize` endpoint. Specify the authentication journey to which the user should be redirected and the username in the JSON payload.

Optionally, specify a custom tracking ID that lets the federation service track the request through Advanced Identity Cloud. If provided, Advanced Identity Cloud logs this ID and its own audit tracking ID. The custom tracking ID must be a string of 36 characters or fewer and can include only the characters `A-Z` `a-z` `0-9` `-` and `_`.

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
  "trackingId": "Y5tyzQi9cGVJjy2L"
}' \
"https://<tenant-env-fqdn>/am/json/realms/root/realms/alpha/authenticate/backchannel/initialize"
{
  "transaction": "b3070138-cd73-4ef2-bd58-812602d7b757",
  "redirectUri": "https://<tenant-env-fqdn>/am/XUI/Login?realm=/alpha&authIndexType=transaction&authIndexValue=b3070138-cd73-4ef2-bd58-812602d7b757"
}
```

Advanced Identity Cloud returns a transaction ID and the complete redirect URI, including the transaction ID.

### Complete the backchannel authentication

In a real-world scenario, the user follows the `redirectUri` provided in the response and completes the authentication.

As user bjensen, open the provided redirect URI in a browser window:

![backchannel login](../_images/backchannel-login.png)

Enter bjensen's password. Her username was provided in the backchannel initiation request.

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

* An array of `auditTrackingIds`, including the standard audit ID Advanced Identity Cloud generates and any custom tracking IDs supplied in the initial request.

* Any allowlisted `sessionProperties`.

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
description: Nodes use these callbacks to recover additional information from the request, such as a header or a certificate.
component: pingoneaic-api
page_id: pingoneaic-api:am-authentication:callbacks-backchannel
canonical_url: https://developer.pingidentity.com/pingoneaic-api/am-authentication/callbacks-backchannel.html
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

## LanguageCallback

Retrieves the locale from the request header for localizing text presented to the user.

Class to import in scripts: `javax.security.auth.callback.LanguageCallback`

Learn more in [LanguageCallback](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/javax/security/auth/callback/LanguageCallback.html).

## ScriptTextOutputCallback

Inserts a script into the page presented to the user; for example, to collect data about the user's environment.

Class to import in scripts: `com.sun.identity.authentication.callbacks.ScriptTextOutputCallback`

## X509CertificateCallback

Retrieves an X.509 certificate, for example, from a header.

Class to import in scripts: `com.sun.identity.authentication.spi.X509CertificateCallback`

---

---
title: Interactive callbacks
description: Nodes return the following callbacks to request information.
component: pingoneaic-api
page_id: pingoneaic-api:am-authentication:callbacks-interactive
canonical_url: https://developer.pingidentity.com/pingoneaic-api/am-authentication/callbacks-interactive.html
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

The [Attribute Collector node](https://docs.pingidentity.com/auth-node-ref/latest/attribute-collector.html) uses this instead of a [ConfirmationCallback](#ConfirmationCallback) to apply IDM policies and validate the response.

| Callback output field | Description                                                                                                                                                                                                                                                                                                                                                                                               |
| --------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `failedPolicies`      | An array of JSON objects describing validation policies that the input failed. The object is empty until the input is provided and validation fails.                                                                                                                                                                                                                                                      |
| `name`                | A string containing the name of the attribute in the user profile.                                                                                                                                                                                                                                                                                                                                        |
| `policies`            | An array of JSON objects describing IDM validation policies the input must pass. An empty JSON object if the node does not require validation.                                                                                                                                                                                                                                                            |
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

## DeviceBindingCallback

Binds a client device to a user.

| Callback output field | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| --------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `userId`              | The ID of the user to bind the device to.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `username`            | The username of the user to bind the device to.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `authenticationType`  | Specifies how the client secures access to the private key. Available options are:- `BIOMETRIC`

  Request that the client secures access to the cryptography keys with biometric security, such as a fingerprint.

- `BIOMETRIC_ALLOW_FALLBACK`

  Request that the client secures access to the cryptography keys with biometric security, such as a fingerprint, but allow use of the device PIN if biometric is unavailable.

- `APPLICATION_PIN`

  Request that the client secures access to the cryptography keys with an application-specific PIN.

- `NONE`

  Request that the client generates a keypair, but does not secure access to them. |
| `challenge`           | A string containing the challenge the client should sign with the private key and return for validation.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `title`               | A string containing an optional title to display when requesting biometric authentication to secure access to the keypair.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| `subtitle`            | A string containing an optional subtitle to display when requesting biometric authentication to secure access to the keypair.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `description`         | A string containing optional descriptive text to display when requesting biometric authentication to secure access to the keypair.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `timeout`             | An integer specifying the number of seconds to wait for device binding to complete before reporting a timeout error.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |

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

1. Generate a keypair and secure access to it as defined by the `authenticationType` field.

2. Generate a JSON web token (JWT) that has the ID of the user in the subject (`sub`) field and the original value of the `challenge`.

   For example:

   ```
   {
       "sub": "id=bjensen,ou=user,dc=am,dc=example,dc=com",
       "challenge": "6IBkTEPcMQ0xCghIclmDLost2ssGO5cPDs0AjUhmDTo="
   }
   ```

3. Sign the JWT using the RS512 algorithm to create a JSON Web Signature (JWS).

4. Complete the callback, returning the JWS, the key ID (`KID`) of the keypair, the public key, and the name and the unique ID of the device.

The server verifies the returned information and persists it in the user's profile if correct.

Example response data

```none
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

## DeviceSigningVerifierCallback

Verifies the signature of data from a registered device.

| Callback output field | Description                                                                                                              |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------ |
| `userId`              | The ID of the user authenticating, if already determined by the authentication journey.                                  |
| `challenge`           | A string containing the challenge the client should sign with the private key and return for validation.                 |
| `title`               | A string containing an optional title to display when requesting biometric authentication to access the keypair.         |
| `subtitle`            | A string containing an optional subtitle to display when requesting biometric authentication to access the keypair.      |
| `description`         | A string containing optional descriptive text to display when requesting biometric authentication to access the keypair. |
| `timeout`             | An integer specifying the number of seconds to wait for device signing to complete before reporting a timeout error.     |

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

```none
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

## NameCallback

Collects a string entered by the user, such as a username.

Example

```json
{
  "callbacks": [{
    "type": "NameCallback",
    "output": [{
      "name": "prompt",
      "value": "User Name"
    }],
    "input": [{
      "name": "IDToken1",
      "value": ""
    }]
  }]
}
```

Class to import in scripts: `javax.security.auth.callback.NameCallback`

## NumberAttributeInputCallback

Collects a numeric attribute, such as size or age.

The [Attribute Collector node](https://docs.pingidentity.com/auth-node-ref/latest/attribute-collector.html) uses this to apply IDM policies and validate the response.

| Callback output field | Description                                                                                                                                                                                                                                                                                                                                                                                               |
| --------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `failedPolicies`      | An array of JSON objects describing validation policies that the input failed. The object is empty until the input is provided and validation fails.                                                                                                                                                                                                                                                      |
| `name`                | A string containing the name of the attribute in the user profile.                                                                                                                                                                                                                                                                                                                                        |
| `policies`            | An array of JSON objects describing IDM validation policies the input must pass. An empty JSON object if the node does not require validation.                                                                                                                                                                                                                                                            |
| `prompt`              | A string containing the description of the information required from the user.                                                                                                                                                                                                                                                                                                                            |
| `required`            | A boolean indicating whether input is required for this attribute.                                                                                                                                                                                                                                                                                                                                        |
| `validateOnly`        | When the node requires validation, this boolean indicates whether to apply validation policies only, or to validate the input and continue to the next node. When `true`, the node only performs input validation and does not continue to the next node.When `true`, this lets the UI validate input as the user types instead of validating the input once and continuing the journey to the next node. |
| `value`               | A string containing a default value for the attribute, if required.                                                                                                                                                                                                                                                                                                                                       |

In the input, return the value and a boolean to set `validateOnly`.

Class to import in scripts: `org.forgerock.openam.authentication.callbacks.NumberAttributeInputCallback`

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

## StringAttributeInputCallback

Collects string attributes, such as city names, telephone numbers, and postcodes.

The [Attribute Collector node](https://docs.pingidentity.com/auth-node-ref/latest/attribute-collector.html) uses this instead of a [TextInputCallback](#TextInputCallback) to apply IDM policies and validate the response.

| Callback output field | Description                                                                                                                                                                                                                                                                                                                                                                                               |
| --------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `failedPolicies`      | An array of JSON objects describing validation policies that the input failed. The object is empty until the input is provided and validation fails.                                                                                                                                                                                                                                                      |
| `name`                | A string containing the name of the attribute in the user profile.                                                                                                                                                                                                                                                                                                                                        |
| `policies`            | An array of JSON objects describing IDM validation policies the input must pass. An empty JSON object if the node does not require validation.                                                                                                                                                                                                                                                            |
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

The [Platform Password node](https://docs.pingidentity.com/auth-node-ref/latest/platform-password.html) uses this instead of a [PasswordCallback](#PasswordCallback) to apply IDM policies and validate the response.

| Callback output field | Description                                                                                                                                                                                                                                                                                                                                                                                              |
| --------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `failedPolicies`      | An array of JSON objects describing validation policies that the input failed. The object is empty until the input is provided and validation fails.                                                                                                                                                                                                                                                     |
| `name`                | A string containing the name of the attribute in the user profile.                                                                                                                                                                                                                                                                                                                                       |
| `policies`            | An array of objects describing IDM validation policies the input must pass. An empty JSON object if the node does not require validation.                                                                                                                                                                                                                                                                |
| `prompt`              | A string containing the description of the information required from the user.                                                                                                                                                                                                                                                                                                                           |
| `validateOnly`        | When the node requires validation, this boolean indicates whether to apply validation policies only, or to validate the input and continue to the next node. When `true`, the node only performs input validation and doesn't continue to the next node.When `true`, this lets the UI validate input as the user types instead of validating the input once and continuing the journey to the next node. |

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

## ValidatedCreateUsernameCallback

Collects a username.

The [Platform Username node](https://docs.pingidentity.com/auth-node-ref/latest/platform-username.html) uses this instead of a [NameCallback](#NameCallback) to apply IDM policies and validate the response.

| Callback output field | Description                                                                                                                                                                                                                                                                                                                                                                                              |
| --------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `failedPolicies`      | An array of JSON objects describing validation policies that the input failed. The object is empty until the input is provided and validation fails.                                                                                                                                                                                                                                                     |
| `name`                | A string containing the name of the attribute in the user profile.                                                                                                                                                                                                                                                                                                                                       |
| `policies`            | An array of objects describing IDM validation policies the input must pass. An empty JSON object if the node does not require validation.                                                                                                                                                                                                                                                                |
| `prompt`              | A string containing the description of the information required from the user.                                                                                                                                                                                                                                                                                                                           |
| `validateOnly`        | When the node requires validation, this boolean indicates whether to apply validation policies only, or to validate the input and continue to the next node. When `true`, the node only performs input validation and doesn't continue to the next node.When `true`, this lets the UI validate input as the user types instead of validating the input once and continuing the journey to the next node. |

Example

```json
{
  "callbacks": [{
    "type": "ValidatedCreateUsernameCallback",
    "output": [{
      "name": "policies",
      "value": {
        "policyRequirements": ["REQUIRED", "VALID_TYPE", "VALID_USERNAME", "CANNOT_CONTAIN_CHARACTERS", "MIN_LENGTH", "MAX_LENGTH"],
        "fallbackPolicies": null,
        "name": "userName",
        "policies": [{
          "policyRequirements": ["REQUIRED"],
          "policyId": "required"
        }, {
          "policyRequirements": ["VALID_TYPE"],
          "policyId": "valid-type",
          "params": {
            "types": ["string"]
          }
        }, {
          "policyId": "valid-username",
          "policyRequirements": ["VALID_USERNAME"]
        }, {
          "policyId": "cannot-contain-characters",
          "params": {
            "forbiddenChars": ["/"]
          },
          "policyRequirements": ["CANNOT_CONTAIN_CHARACTERS"]
        }, {
          "policyId": "minimum-length",
          "params": {
            "minLength": 1
          },
          "policyRequirements": ["MIN_LENGTH"]
        }, {
          "policyId": "maximum-length",
          "params": {
            "maxLength": 255
          },
          "policyRequirements": ["MAX_LENGTH"]
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
      "value": "Username"
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

Class to import in scripts: `org.forgerock.openam.authentication.callbacks.ValidatedUsernameCallback`

---

---
title: Log in over REST
description: To authenticate using REST, send an HTTP POST request to the json/authenticate endpoint. You must specify the realm hierarchy. Prefix each realm in the hierarchy with the realms/ keyword; for example, /realms/root/realms/alpha.
component: pingoneaic-api
page_id: pingoneaic-api:am-authentication:login-using-rest
canonical_url: https://developer.pingidentity.com/pingoneaic-api/am-authentication/login-using-rest.html
keywords: ["Authentication", "Callbacks", "REST API"]
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

After successful authentication, Advanced Identity Cloud returns a `tokenId` that applications can present as a cookie value for other operations that require authentication. The `tokenId` is known as the *session token*. Learn how applications can use session tokens in [Session tokens after authentication](rest-using-ssotokens.html).

If `HttpOnly` cookies are enabled, and a client makes a call to the `/json/authenticate` endpoint with a valid SSO token, Advanced Identity Cloud returns the `tokenId` field **empty**. For example:

```json
{
    "tokenId":"",
    "successUrl":"/enduser/?realm=/alpha",
    "realm":"/alpha"
}
```

|   |                                                                                                                                                                             |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | To authenticate a user without providing them with a session, use the `noSession` parameter. Learn more in [Authenticate endpoints](authenticate-endpoint-parameters.html). |

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

```none
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

```none
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
      "_id": 0
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
'https://<tenant-env-fqdn>/am/json/realms/root/realms/alpha/authenticate'
{
  "tokenId": "lWY23F4fuC7cu4Fq4GQa5u6drlQ...*",
  "successUrl": "/enduser/?realm=/alpha",
  "realm": "/alpha"
}
```

In complex authentication journeys, Advanced Identity Cloud could send several callbacks sequentially. Each must be completed and returned to Advanced Identity Cloud until authentication is successful.

Learn about the callbacks Advanced Identity Cloud can return in [Return callback information](callbacks-supported.html).

---

---
title: Log out over REST
description: Authenticated users can log out with the token cookie value and an HTTP POST request to /json/sessions/?_action=logout:
component: pingoneaic-api
page_id: pingoneaic-api:am-authentication:logout-using-rest
canonical_url: https://developer.pingidentity.com/pingoneaic-api/am-authentication/logout-using-rest.html
keywords: ["Authentication", "Sessions", "REST API"]
---

# Log out over REST

Authenticated users can log out with the token cookie value and an HTTP POST request to `/json/sessions/?_action=logout`:

```bash
$ curl \
--request POST \
--header "<session-cookie-name>: AQICS...NzEz*" \
--header "Accept-API-Version: resource=3.1, protocol=1.0" \
'https://<tenant-env-fqdn>/am/json/realms/root/realms/alpha/sessions/?_action=logout'
{
    "result":"Successfully logged out"
}
```

---

---
title: Read-only callbacks
description: Nodes use these callbacks to return information to the client application or to display information to the user.
component: pingoneaic-api
page_id: pingoneaic-api:am-authentication:callbacks-read-only
canonical_url: https://developer.pingidentity.com/pingoneaic-api/am-authentication/callbacks-read-only.html
keywords: ["Authentication", "Callbacks", "REST API"]
section_ids:
  metadatacallback: MetadataCallback
  pollingwaitcallback: PollingWaitCallback
  RedirectCallback: RedirectCallback
  suspendedtextoutputcallback: SuspendedTextOutputCallback
  textoutputcallback: TextOutputCallback
---

# Read-only callbacks

Nodes use these callbacks to return information to the client application or to display information to the user.

## MetadataCallback

Injects key-value pairs into the authentication process.

Example

```json
{
  "callbacks": [{
    "type": "MetadataCallback",
    "output": [{
      "name": "data",
      "value": {
        "myParameter": "MyValue"
      }
    }]
  }]
}
```

Class to import in scripts: `com.sun.identity.authentication.spi.MetadataCallback`

## PollingWaitCallback

Indicates the number of milliseconds to wait before responding to the callback.

Example

```json
{
  "callbacks": [{
    "type": "PollingWaitCallback",
    "output": [{
      "name": "waitTime",
      "value": "8000"
    }, {
      "name": "message",
      "value": "Waiting for response..."
    }]
  }]
}
```

Class to import in scripts: `org.forgerock.openam.authentication.callbacks.PollingWaitCallback`

## RedirectCallback

Redirects the user-agent.

The [Social Provider Handler node](https://docs.pingidentity.com/auth-node-ref/latest/social-provider-handler.html) returns this callback when its Client Type is set to `BROWSER`, and the client must redirect the user to the social provider for authentication.

Example

```json
{
  "callbacks": [{
    "type": "RedirectCallback",
    "output": [{
      "name": "redirectUrl",
      "value": "https://accounts.google.com/o/oauth2/v2/auth?nonce..."
    }, {
      "name": "redirectMethod",
      "value": "GET"
    }, {
      "name": "trackingCookie",
      "value": true
    }]
  }]
}
```

Advanced Identity Cloud uses a `trackingCookie` to store the authentication identifier that reflects the client's place in the authentication process.

Class to import in scripts: `com.sun.identity.authentication.spi.RedirectCallback`

## SuspendedTextOutputCallback

Provides a message to display to the user when the authentication journey is suspended.

| Callback output field | Description                                                                                      |
| --------------------- | ------------------------------------------------------------------------------------------------ |
| `message`             | A string containing a message to display to the user.                                            |
| `messageType`         | A number indicating the severity of the message:- `0`: Information

- `1`: Warning

- `2`: Error |

Example

```json
{
  "callbacks": [{
    "type": "SuspendedTextOutputCallback",
    "output": [{
      "name": "message",
      "value": "An email has been sent to your inbox."
    }, {
      "name": "messageType",
      "value": "0"
    }]
  }]
}
```

Class to import in scripts: `org.forgerock.openam.auth.node.api.SuspendedTextOutputCallback`

## TextOutputCallback

Provides a message to display to the user.

| Callback output field | Description                                                                                      |
| --------------------- | ------------------------------------------------------------------------------------------------ |
| `message`             | A string containing a message to display to the user.                                            |
| `messageType`         | A number indicating the severity of the message:- `0`: Information

- `1`: Warning

- `2`: Error |

Example

```json
{
  "callbacks": [{
    "type": "TextOutputCallback",
    "output": [{
      "name": "message",
      "value": "Default message"
    }, {
      "name": "messageType",
      "value": "0"
    }]
  }]
}
```

Class to import in scripts: `javax.security.auth.callback.TextOutputCallback`

Learn more in [TextOutputCallback](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/javax/security/auth/callback/TextOutputCallback.html).

---

---
title: Return callback information
description: The /json/authenticate endpoint supports callback mechanisms to perform complex authentication journeys. When Advanced Identity Cloud needs to return or request information, it returns a JSON object with the authentication step, the authentication identifier, and the related callbacks.
component: pingoneaic-api
page_id: pingoneaic-api:am-authentication:callbacks-supported
canonical_url: https://developer.pingidentity.com/pingoneaic-api/am-authentication/callbacks-supported.html
keywords: ["Authentication", "Callbacks"]
section_ids:
  example-callback: Example callback
---

# Return callback information

The `/json/authenticate` endpoint supports callback mechanisms to perform complex authentication journeys. When Advanced Identity Cloud needs to return or request information, it returns a JSON object with the authentication step, the authentication identifier, and the related callbacks.

Advanced Identity Cloud supports the following callback types:

* [Read-only callbacks](callbacks-read-only.html)

  Read-only callbacks provide information to the user, such as text messages or the period of time a user must wait before continuing their authentication journey.

* [Interactive callbacks](callbacks-interactive.html)

  Interactive callbacks request information from the user. For example, their username and password, or a request that they select between different configured options.

* [Backchannel callbacks](callbacks-backchannel.html)

  Backchannel callbacks let Advanced Identity Cloud access additional information from the user's request. For example, a specific header or certificate.

Read-only and interactive callbacks have an array of `output` elements that can be displayed to the end user. The JSON returned in an interactive callback includes an array of `input` elements that must be completed and returned to Advanced Identity Cloud. For example:

```none
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

## Example callback

The following example shows a request for authentication, and Advanced Identity Cloud's response with the `NameCallback` and `PasswordCallback`:

```bash
$ curl \
--request POST \
--header "Content-Type: application/json" \
--header "Accept-API-Version: resource=2.0, protocol=1.0" \
'https://<tenant-env-fqdn>/am/json/realms/root/realms/alpha/authenticate'
```

```none
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
| **2** | The type of callback. It must be listed on this page.                                                                                   |
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
      "_id": 0
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
'https://<tenant-env-fqdn>/am/json/realms/root/realms/alpha/authenticate'
{
  "tokenId": "lWY23F4fuC7cu4Fq4GQa5u6drlQ...*",
  "successUrl": "/enduser/?realm=/alpha",
  "realm": "/alpha"
}
```

In complex authentication journeys, Advanced Identity Cloud could send several callbacks sequentially. Each must be completed and returned to Advanced Identity Cloud until authentication is successful.

---

---
title: Session tokens after authentication
description: After successful authentication, Advanced Identity Cloud returns a tokenId that applications can present as a cookie value for other operations that require authentication. The tokenId contains a session token—​a representation of the exchange of information and credentials between Advanced Identity Cloud and the user or identity.
component: pingoneaic-api
page_id: pingoneaic-api:am-authentication:rest-using-ssotokens
canonical_url: https://developer.pingidentity.com/pingoneaic-api/am-authentication/rest-using-ssotokens.html
keywords: ["Authentication", "Sessions", "REST API"]
page_aliases: ["authentication-guide:rest-using-ssotokens.adoc"]
---

# Session tokens after authentication

After successful authentication, Advanced Identity Cloud returns a `tokenId` that applications can present as a cookie value for other operations that require authentication. The `tokenId` contains a [session](https://docs.pingidentity.com/pingoneaic/latest/am-sessions/about-sessions.html) token—​a representation of the exchange of information and credentials between Advanced Identity Cloud and the user or identity.

If server-side sessions are enabled, the `tokenId` is a reference to the session state stored in the CTS token store.

The following is a common scenario when accessing Advanced Identity Cloud by using REST API calls:

1. Call the `/json/authenticate` endpoint to log a user in.

   This call returns a `tokenID` value, which is used in subsequent calls to identify the user:

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

   The returned `tokenID` is called a *session token* (also referred to as an SSO token). Each REST API call made after successful authentication must present the session token in the HTTP header as proof of authentication.

2. Call one or more additional REST APIs on behalf of the authenticated user.

   Each REST API call passes the user's `tokenID` back to Advanced Identity Cloud in the HTTP header as proof of previous authentication.

   The following is a *partial* example of a `curl` command that inserts the token ID returned from a prior successful authentication attempt into the HTTP header:

   ```bash
   $ curl \
   --request POST \
   --header "Content-Type: application/json" \
   --header "<session-cookie-name>: AQIC5wM...TU3OQ*" \
   --header "Accept-API-Version: resource=2.0, protocol=1.0" \
   --data '{...}'
   ...
   ```

   Observe that the session token is inserted into a header field named `<session-cookie-name>`. This header field name must correspond to the name of the tenant session cookie.

   |   |                                                                                                                                                                                                          |
   | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | To find the name of the session cookie, read [How do I view the tenant session cookie name?](https://docs.pingidentity.com/pingoneaic/latest/am-sessions/about-sessions.html#proc-change-session-cookie) |

   Once a user has authenticated, you do *not* need to insert login credentials in the HTTP header in subsequent REST API calls. Note the absence of `X-OpenAM-Username` and `X-OpenAM-Password` headers in the preceding example.

   Users must have appropriate privileges to access Advanced Identity Cloud functionality using the REST API.

3. Use the REST API to log the user out of Advanced Identity Cloud, as described in [Log out over REST](logout-using-rest.html).

   As with other REST API calls made after a user has authenticated, the REST API call to log out of Advanced Identity Cloud requires the user's `tokenID` in the HTTP header.