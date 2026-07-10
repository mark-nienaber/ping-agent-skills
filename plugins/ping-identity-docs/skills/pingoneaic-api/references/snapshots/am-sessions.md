---
title: Manage sessions over REST
description: To manage authenticated sessions using the REST API, send requests to the /json/sessions endpoint.
component: pingoneaic-api
page_id: pingoneaic-api:am-sessions:managing-sessions-REST
canonical_url: https://developer.pingidentity.com/pingoneaic-api/am-sessions/managing-sessions-REST.html
keywords: ["Sessions", "REST API", "Log Out", "Properties"]
page_aliases: ["index.adoc"]
section_ids:
  rest-api-session-information: Get information about sessions
  rest-api-token-validation: Validate sessions
  rest-api-session-refresh: Refresh server-side sessions
  rest-api-session-logout: Invalidate sessions
  invalidate-sessions-by-handle: Invalidate specific sessions
  invalidate-sessions-user: Invalidate all sessions for a user
  rest-api-session-properties: Get and set session properties
---

# Manage sessions over REST

To manage authenticated sessions using the REST API, send requests to the `/json/sessions` endpoint.

The following examples assume you've used a service account to [obtain an access token](../authenticate-to-rest-api-with-access-token.html#get_an_access_token) with the `fr:am:*` scope.

The examples also assume you've retrieved the [session token](../am-authentication/rest-using-ssotokens.html) for the authenticated session you're managing.

## Get information about sessions

To get information about a specific authenticated session:

1. Send an HTTP POST request to the `/json/sessions/` endpoint, with the `getSessionInfo` action.

2. Provide the session token in the POST data as the value of the `tokenId`.

```bash
$ curl \
--request POST \
--header 'Authorization: Bearer <access-token>' \
--header "Accept-API-Version: resource=4.0" \
--header "Content-type: application/json" \
--data '{ "tokenId": " session-token " }' \
'https://<tenant-env-fqdn>/am/json/realms/root/realms/alpha/sessions/?_action=getSessionInfo'
{
  "username": "b0f30dfb-4e01-457e-a567-c258a74e4fe2",
  "universalId": "id=b0f30dfb-4e01-457e-a567-c258a74e4fe2,ou=user,o=alpha,ou=services,ou=am-config",
  "realm": "/alpha",
  "latestAccessTime": "2024-01-12T13:49:25Z",
  "maxIdleExpirationTime": "2024-01-12T14:19:25Z",
  "maxSessionExpirationTime": "2024-01-12T15:49:24Z",
  "properties": {
    "AMCtxId": "b9275f8c-fa83-4455-bdac-d27e8d538a8f-215815",
    "AuthType": ""
  }
}
```

|   |                                                                       |
| - | --------------------------------------------------------------------- |
|   | The `getSessionInfo` action doesn't refresh the session idle timeout. |

To obtain session information about a server-side session *and* reset the idle timeout, use the `getSessionInfoAndResetIdleTime` action as follows:

```bash
$ curl \
--request POST \
--header 'Authorization: Bearer <access-token>' \
--header "Accept-API-Version: resource=4.0, protocol=1.0" \
--header "Content-type: application/json" \
--data '{ "tokenId": " session-token " }' \
'https://<tenant-env-fqdn>/am/json/realms/root/realms/alpha/sessions/?_action=getSessionInfoAndResetIdleTime'
{
  "username": "b0f30dfb-4e01-457e-a567-c258a74e4fe2",
  "universalId": "id=b0f30dfb-4e01-457e-a567-c258a74e4fe2,ou=user,o=alpha,ou=services,ou=am-config",
  "realm": "/alpha",
  "latestAccessTime": "2024-01-12T14:18:24Z",
  "maxIdleExpirationTime": "2024-01-12T14:48:24Z",
  "maxSessionExpirationTime": "2024-01-12T15:49:23Z",
  "properties": {
    "AMCtxId": "b9275f8c-fa83-4455-bdac-d27e8d538a8f-215815",
    "AuthType": ""
  }
}
```

|   |                                                                                                                                                                                                                                                                                                                                                                                                                          |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | * You can't reset the idle timeout of a client-side session.

* The `AMCtxId` property represents the audit ID for the session. To return the `AMCtxId` property in the session query response (as in this example) include `AMCtxId` in the `Session Properties to return for session queries`. Under Native Consoles > Access Management, go to Realms > *Realm Name* > Services > Session Property Whitelist Service. |

## Validate sessions

To check if a session token is valid, send an HTTP POST request to the `/json/sessions/` endpoint with the `validate` action. Provide the session token in the POST data as the value of the `tokenId`.

```bash
$ curl \
--request POST \
--header "Content-type: application/json" \
--header 'Authorization: Bearer <access-token>' \
--header "Accept-API-Version: resource=4.0, protocol=1.0" \
--data '{ "tokenId": " session-token" }' \
'https://<tenant-env-fqdn>/am/json/realms/root/realms/alpha/sessions/?_action=validate'
```

If the session token is valid, Advanced Identity Cloud returns the user ID and realm:

```bash
{
  "valid": true,
  "sessionUid": "b9275f8c-fa83-4455-bdac-d27e8d538a8f-245866",
  "uid": "b0f30dfb-4e01-457e-a567-c258a74e4fe2",
  "realm": "/alpha"
}
```

By default, validating an authenticated session resets the session's idle time, which triggers a write operation to the Core Token Service (CTS) token store. To avoid this, include `refresh=false`, for example, `validate&refresh=false`.

## Refresh server-side sessions

To reset the idle time of a server-side authenticated session, send an HTTP POST request to the `/json/sessions/` endpoint, with the `refresh` action. Include the session token in the POST body as the value of the `tokenId`.

```bash
$ curl \
--request POST \
--header "Content-type: application/json" \
--header 'Authorization: Bearer <access-token>' \
--header "Accept-API-Version: resource=4.0, protocol=1.0" \
--data '{ "tokenId": " session-token " }' \
'https://<tenant-env-fqdn>/am/json/realms/root/realms/alpha/sessions/?_action=refresh'
{
  "uid": "b0f30dfb-4e01-457e-a567-c258a74e4fe2",
  "realm": "/alpha",
  "idletime": 0,
  "maxidletime": 30,
  "maxsessiontime": 120,
  "maxtime": 6826
}
```

On success, Advanced Identity Cloud resets the idle time for the server-side session, and returns timeout details of the authenticated session.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | * Resetting a server-side session's idle time triggers a write operation to the CTS token store. To avoid the overhead of write operations to the token store, use the `refresh` action *only* if you want to reset a server-side session's idle time.

* The idle time of a session is reset subject to the latest access time update frequency. Advanced Identity Cloud updates a session's latest access time *at most* this often. The default is 60 seconds.

* Advanced Identity Cloud doesn't monitor idle time for client-side sessions, so you can't use the `tokenId` of a client-side session to refresh the session's idle time. |

## Invalidate sessions

To invalidate an authenticated session, send an HTTP POST request to the `/json/sessions/` endpoint with the `logout` action. Include the session token in the POST body as the value of the `tokenId`.

```bash
$ curl \
--request POST \
--header "Content-type: application/json" \
--header 'Authorization: Bearer <access-token>' \
--header "Accept-API-Version: resource=4.0, protocol=1.0" \
--data '{ "tokenId": "session-token" }' \
'https://<tenant-env-fqdn>/am/json/realms/root/realms/alpha/sessions/?_action=logout'
{
    "result": "Successfully logged out"
}
```

If the token isn't valid (and therefore can't be invalidated), Advanced Identity Cloud returns the following error:

```json
{
  "result": "Token has expired"
}
```

### Invalidate specific sessions

To invalidate specific authenticated sessions for a user, first obtain a list of the user's active sessions. Send an HTTP GET request to the `/json/sessions/` endpoint with a `queryFilter` to specify the UUID of the user and the realm to search.

For example, to obtain the list of active sessions for `bjensen` (whose UUID is `b0f30dfb-4e01-457e-a567-c258a74e4fe2`) in the `alpha` realm, the query filter value would be:

```
username eq "b0f30dfb-4e01-457e-a567-c258a74e4fe2" and realm eq "/alpha"
```

|   |                                                                                                                                          |
| - | ---------------------------------------------------------------------------------------------------------------------------------------- |
|   | The query filter value must be URL-encoded when sent over HTTP.Learn more about query filter parameters in [Query](../crest/query.html). |

In the following example, `bjensen` has two authenticated sessions. Note the value of the `sessionHandle` properties.

```bash
$ curl \
--request GET \
--header 'Authorization: Bearer <access-token>' \
--header "Accept-API-Version: resource=4.0, protocol=1.0" \
'https://<tenant-env-fqdn>/am/json/realms/root/realms/alpha/sessions?_queryFilter=username%20eq%20%22b0f30dfb-4e01-457e-a567-c258a74e4fe2%22%20and%20realm%20eq%20%22%2Falpha%22'
{
  "result": [
    {
      "_rev": "647523949",
      "username": "b0f30dfb-4e01-457e-a567-c258a74e4fe2",
      "universalId": "id=b0f30dfb-4e01-457e-a567-c258a74e4fe2,ou=user,o=alpha,ou=services,ou=am-config",
      "realm": "/alpha",
      "sessionHandle": "shandle:flz3sdj5Ts…​",
      "latestAccessTime": "2024-01-15T07:42:42.544Z",
      "maxIdleExpirationTime": "2024-01-15T08:12:42Z",
      "maxSessionExpirationTime": "2024-01-15T09:31:22Z"
    },
    {
      "_rev": "1074537861",
      "username": "b0f30dfb-4e01-457e-a567-c258a74e4fe2",
      "universalId": "id=b0f30dfb-4e01-457e-a567-c258a74e4fe2,ou=user,o=alpha,ou=services,ou=am-config",
      "realm": "/alpha",
      "sessionHandle": "shandle:SZtTnGMwnG…​",
      "latestAccessTime": "2024-01-15T07:44:00.670Z",
      "maxIdleExpirationTime": "2024-01-15T08:14:00Z",
      "maxSessionExpirationTime": "2024-01-15T09:44:00Z"
    }
  ],
  …​
}
```

To log out specific sessions, send an HTTP POST request to the `/json/sessions/` endpoint, with the `logoutByHandle` action. Include an array of the session handles to invalidate as values of the `sessionHandles` property in the POST body.

This example invalidates the sessions returned by the previous query:

```bash
$ curl \
--request POST \
--header "Content-Type: application/json" \
--header 'Authorization: Bearer <access-token>' \
--header "Accept-API-Version: resource=4.0, protocol=1.0" \
--data '{
    "sessionHandles": [
        "shandle:flz3sdj5Ts…​",
        "shandle:SZtTnGMwnG…​"
    ]
}' \
'https://<tenant-env-fqdn>/am/json/realms/root/realms/alpha/sessions/?_action=logoutByHandle'
{
    "result": {
        "shandle:flz3sdj5Ts…​": true,
        "shandle:SZtTnGMwnG…​": true
    }
}
```

### Invalidate all sessions for a user

To invalidate (log out) all authenticated sessions for a user, send an HTTP POST request to the `/json/sessions/` endpoint with the `logoutByUser` action, specifying the UUID of the user in the request payload.

This example logs out all sessions for user `bjensen` (whose UUID is `b0f30dfb-4e01-457e-a567-c258a74e4fe2`):

```bash
$ curl \
--request POST \
--header "Content-Type: application/json" \
--header 'Authorization: Bearer <access-token>' \
--header "Accept-API-Version: resource=5.1, protocol=1.0" \
--data '{"username": "b0f30dfb-4e01-457e-a567-c258a74e4fe2"}' \
'https://<tenant-env-fqdn>/am/json/realms/root/realms/alpha/sessions/?_action=logoutByUser'
{
  "result": true
}
```

## Get and set session properties

Use the REST API to read and update properties on authenticated sessions. Define the properties you want to get and set in the [Session Property Whitelist Service](https://docs.pingidentity.com/pingoneaic/latest/am-reference/realm-services-configuration.html#realm-amsessionpropertywhitelist) configuration.

You can use the REST API to:

* Get the names of the properties that you can read or update. This is the same set of properties configured in the Session Property Whitelist service.

* Read and update property values.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The ability to set, change and delete session properties is affected by the *session state*:* For server-side sessions, you can manipulate session properties at any time during the session's lifetime.

* For client-side sessions, you can manipulate session properties only during the authentication process, before the user receives the session token from Advanced Identity Cloud. For example, you can set or delete properties on a client-side session from within a post-authentication plugin. |

Differentiate the user who performs the operation from the session affected by the operation as follows:

* Use an [access token](../authenticate-to-rest-api-with-access-token.html#get_an_access_token) for the service account authorized to access these endpoints.

* Specify the session token of the user whose session you want to read or modify as the `tokenId` parameter in the body of the REST API call.

The following examples assume you configured a property named `LoginLocation` in the Session Property Whitelist service.

To retrieve the names and values of the properties you can get or set, send an HTTP POST request to the `json/sessions` endpoint, with the `getSessionProperties` action:

```bash
$ curl \
--request POST \
--header 'Authorization: Bearer <access-token>' \
--header "Accept-API-Version: resource=3.1, protocol=1.0" \
--header "Content-type: application/json" \
--data '{ "tokenId": " "session-token" " }' \
'https://<tenant-env-fqdn>/am/json/realms/root/sessions/?_action=getSessionProperties'
{
    "LoginLocation": ""
}
```

To set the value of a session property, send an HTTP POST request to the `/json/sessions/` endpoint, with the `updateSessionProperties` action:

```bash
$ curl \
--request POST \
--header "Content-Type: application/json" \
--header 'Authorization: Bearer <access-token>' \
--header "Accept-API-Version: resource=3.1, protocol=1.0" \
--data '{ "tokenId": " "session-token" ", "LoginLocation":"40.748440, -73.984559"}' \
'https://<tenant-env-fqdn>/am/json/realms/root/sessions/?_action=updateSessionProperties'
{
    "LoginLocation": "40.748440, -73.984559"
}
```

To set multiple properties in a single REST API call, specify the list of properties and their values in the JSON payload; for example:

```
--data '{"property1":"value1", "property2":"value2"}'
```

If the service account you're using to modify the session doesn't have sufficient access privileges, Advanced Identity Cloud returns a 403 Forbidden error.

You can't set properties internal to Advanced Identity Cloud sessions. If you try to modify an internal property in a REST API call, Advanced Identity Cloud also returns a 403 Forbidden error:

```bash
$ curl \
--request POST \
--header "Content-Type: application/json" \
--header 'Authorization: Bearer <access-token>' \
--header "Accept-API-Version: resource=3.1, protocol=1.0" \
--data '{"AuthLevel":"5", "tokenId": " "session-token" "}' \
'https://<tenant-env-fqdn>/am/json/realms/root/sessions/?_action=updateSessionProperties'
{
    "code": 403,
    "reason": "Forbidden",
    "message": "Forbidden"
}
```

Find a list of the default session properties in [Session properties](https://docs.pingidentity.com/pingoneaic/latest/am-authentication/auth-nodes-and-journeys.html#session-properties).