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
