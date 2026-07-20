---
title: Client-side sessions
description: Client-side session storage with JWT encoding in session cookies
component: pingoneaic
page_id: pingoneaic:am-sessions:client-side-sessions
canonical_url: https://docs.pingidentity.com/pingoneaic/am-sessions/client-side-sessions.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Sessions", "Authentication", "CTS Store (Sessions &amp; Tokens)"]
page_aliases: ["sessions-guide:client-side-sessions.adoc"]
section_ids:
  client_side_journey_sessions: Client-side journey sessions
  client_side_authenticated_sessions: Client-side authenticated sessions
  secure_client_side_sessions: Secure client-side sessions
---

# Client-side sessions

Advanced Identity Cloud creates sessions either as client-side sessions or server-side sessions. The session location depends on the [session configuration](../am-authentication/realm-auth-config.html#session-config-switch).

For client-side sessions, Advanced Identity Cloud returns the entire session state to the client in a session cookie after a request. The cookie is then passed back to Advanced Identity Cloud with each subsequent request.

## Client-side journey sessions

Advanced Identity Cloud uses *journey sessions* to manage progress through a journey.

Journey sessions are configured as client-side sessions by default.

While progressing through the journey, the journey session state is returned to the client after each call to the `authenticate` endpoint, and stored in the `authId` object of the JSON response.

Storing journey sessions on the client lets Advanced Identity Cloud handle the journey at any point in time.

For realms configured for server-side sessions, Advanced Identity Cloud attempts to invalidate client-side journey sessions after creating the server-side authenticated sessions.

## Client-side authenticated sessions

Advanced Identity Cloud creates *authenticated sessions* after a user has authenticated successfully.

For browser-based clients that use client-side authenticated sessions, Advanced Identity Cloud sets a cookie in the browser that contains the session state. When the browser returns the cookie, Advanced Identity Cloud decodes the session state from the cookie.

For REST-based clients, Advanced Identity Cloud sends the cookie in a header.

## Secure client-side sessions

For improved security, you should [configure Advanced Identity Cloud to sign and/or encrypt](configure-client-side-sessions.html) client-side journey and authenticated sessions. Decrypting and verifying the session can be an expensive operation to perform on each request. Advanced Identity Cloud therefore caches the decrypt sequence in memory to improve performance.

---

---
title: Configure client-side sessions
description: Configure client-side journey and authenticated session storage and signing
component: pingoneaic
page_id: pingoneaic:am-sessions:configure-client-side-sessions
canonical_url: https://docs.pingidentity.com/pingoneaic/am-sessions/configure-client-side-sessions.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Sessions", "Authentication", "CTS Store (Sessions &amp; Tokens)", "Setup &amp; Configuration", "Storage"]
page_aliases: ["sessions-guide:configure-client-side-sessions.adoc"]
section_ids:
  proc-configure-client-based-auth-sessions: Client-side journey sessions
  proc-configure-client-based-sessions: Client-side authenticated sessions
  verify_client_side_authenticated_sessions: Verify client-side authenticated sessions
---

# Configure client-side sessions

Advanced Identity Cloud uses two types of tokens that represent an exchange of information, usually interactive, between Advanced Identity Cloud and a user or entity:

* *Journey sessions*, which Advanced Identity Cloud creates to track progress through a journey. These sessions last for the duration of the journey.

* *Authenticated sessions*, which Advanced Identity Cloud creates after a user has authenticated successfully to manage the user's or entity's access to resources.

You can configure Advanced Identity Cloud to use [client-side](client-side-sessions.html) or [server-side](server-side-sessions.html) journey and authenticated sessions.

This page covers how to configure Advanced Identity Cloud to use client-side journey and authenticated sessions.

## Client-side journey sessions

1. Under Native Consoles > Access Management, go to Realms > *Realm Name* > Authentication > Settings.

2. Switch to the Trees tab.

3. From the Authentication session state management scheme drop-down list, select `JWT`.

4. In the Max duration (minutes) field, adjust the maximum life of the journey session in minutes.

   You can also set the maximum duration in a journey or at the node level. Learn more in [Maximum duration](../am-authentication/suspended-auth.html#maximum-duration).

5. Save your changes.

When Advanced Identity Cloud creates tenant environments, it generates signing secrets: unique, secure, random values for signing journey sessions.

To override the generated signing secret:

1. On the Authentication - Settings page, switch to the Security tab.

2. In the Organization Authentication Signing Secret field, enter a base64-encoded HMAC secret at least 128 bits long.

   |   |                                                                                                                                                                                                                                      |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
   |   | If you choose to override the generated signing secret, specify different values in your development, staging, and production tenant environments, so development sessions aren't valid in your production environment, for example. |

3. Save your changes.

## Client-side authenticated sessions

1. Under Native Consoles > Access Management, go to Realms > *Realm Name* > Authentication > Settings.

2. Switch to the General tab.

3. Select Use Client-Side Sessions.

4. Save your changes.

## Verify client-side authenticated sessions

The service doesn't track client-side authenticated sessions:

1. Authenticate to the realm configured for client-side authenticated sessions as a non-administrative user:

   ```bash
   $ curl \
   --request POST \
   --header 'Content-Type: application/json' \
   --header 'X-OpenAM-Username: <non-admin-username>' \
   --header 'X-OpenAM-Password: <non-admin-password>' \
   --header 'Accept-API-Version: resource=2.0, protocol=1.0' \
   'https://<tenant-env-fqdn>/am/json/realms/root/realms/alpha/authenticate'
   {
       "tokenId":"<token-id>",
       "successUrl": "/enduser/?realm=/alpha",
       "realm":"/alpha"
   }
   ```

2. Under Native Consoles > Access Management, go to Realms > *Realm Name* > Identities > *Username* to find the user identifier at the top of the profile page; for example:

   ![The profile page shows the user identifier.](_images/get-user-id.png)

3. Go to Realms > *Realm Name* > Sessions.

   With the user identifier, [search for the session](manage-sessions-ui.html). You should find no authenticated sessions for the non-administrative user:

   ![The service does not track client-side sessions.](_images/no-server-side-session.png)

---

---
title: Configure server-side sessions
description: Configure server-side session storage in CTS token store
component: pingoneaic
page_id: pingoneaic:am-sessions:configure-server-side-sessions
canonical_url: https://docs.pingidentity.com/pingoneaic/am-sessions/configure-server-side-sessions.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Sessions", "Authentication", "CTS Store (Sessions &amp; Tokens)", "Setup &amp; Configuration", "Storage"]
page_aliases: ["sessions-guide:configure-server-side-sessions.adoc"]
section_ids:
  proc-configure-server-side-auth-sessions: Server-side journey sessions
  proc-configure-server-side-sessions: Server-side authenticated sessions
  verify_server_side_authenticated_sessions: Verify server-side authenticated sessions
---

# Configure server-side sessions

By default, Advanced Identity Cloud realms use server-side sessions.

Advanced Identity Cloud uses two types of tokens that represent an exchange of information, usually interactive, between Advanced Identity Cloud and a user or entity:

* *Journey sessions*, which Advanced Identity Cloud creates to track progress through a journey. These sessions last for the duration of the journey.

* *Authenticated sessions*, which Advanced Identity Cloud creates after a user has authenticated successfully to manage the user's or entity's access to resources.

You can configure Advanced Identity Cloud to use [client-side](client-side-sessions.html) or [server-side](server-side-sessions.html) journey and authenticated sessions.

This page covers how to configure Advanced Identity Cloud to use server-side journey and authenticated sessions if the default realm settings have changed.

## Server-side journey sessions

1. Under Native Consoles > Access Management, go to Realms > *Realm Name* > Authentication > Settings.

2. Switch to the Trees tab.

3. From the Authentication session state management scheme drop-down list, select `CTS`.

4. In the Max duration (minutes) field, adjust the maximum life of the journey session in minutes.

   You can also set the maximum duration in a journey or at the node level. Learn more in [Maximum duration](../am-authentication/suspended-auth.html#maximum-duration).

5. Save your changes.

When Advanced Identity Cloud creates tenant environments, it generates signing secrets: unique, secure, random values for signing journey sessions.

To override the generated signing secret:

1. On the Authentication - Settings page, switch to the Security tab.

2. In the Organization Authentication Signing Secret field, enter a base64-encoded HMAC secret at least 128 bits long.

   |   |                                                                                                                                                                                                                                      |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
   |   | If you choose to override the generated signing secret, specify different values in your development, staging, and production tenant environments, so development sessions aren't valid in your production environment, for example. |

3. Save your changes.

## Server-side authenticated sessions

1. Under Native Consoles > Access Management, go to Realms > *Realm Name* > Authentication > Settings.

2. Switch to the General tab.

3. Clear Use Client-Side Sessions.

4. Save your changes.

## Verify server-side authenticated sessions

You can find server-side authenticated sessions:

1. Authenticate to the realm configured for server-side authenticated sessions as a non-administrative user:

   ```bash
   $ curl \
   --request POST \
   --header 'Content-Type: application/json' \
   --header 'X-OpenAM-Username: <non-admin-username>' \
   --header 'X-OpenAM-Password: <non-admin-password>' \
   --header 'Accept-API-Version: resource=2.0, protocol=1.0' \
   'https://<tenant-env-fqdn>/am/json/realms/root/realms/alpha/authenticate'
   {
       "tokenId":"<token-id>",
       "successUrl": "/enduser/?realm=/alpha",
       "realm":"/alpha"
   }
   ```

2. Under Native Consoles > Access Management, go to Realms > *Realm Name* > Identities > *Username* to find the user identifier at the top of the profile page; for example:

   ![The profile page shows the user identifier.](_images/get-user-id.png)

3. Go to Realms > *Realm Name* > Sessions.

   With the user identifier, [search for the session](manage-sessions-ui.html). You should find the authenticated session for the non-administrative user:

   ![The service tracks server-side sessions.](_images/server-side-session-tracking.png)

---

---
title: Introduction to sessions and cookies
description: Concepts of journey and authenticated sessions, storage types, and cookies
component: pingoneaic
page_id: pingoneaic:am-sessions:about-sessions
canonical_url: https://docs.pingidentity.com/pingoneaic/am-sessions/about-sessions.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Sessions", "CTS Store (Sessions &amp; Tokens)"]
page_aliases: ["sessions-guide:about-sessions.adoc", "release-notes:rapid-channel/configure-the-sso-cookie-name-for-your-tenant.adoc"]
section_ids:
  sessions_and_cookies: Sessions and cookies
  session_location: Session location
  session-cookie-name: Session cookie name
  journey_session_allowlist: Journey session allowlist
  configure_journey_session_allowlisting: Configure journey session allowlisting
---

# Introduction to sessions and cookies

Advanced Identity Cloud uses two types of tokens that represent an exchange of information, usually interactive, between Advanced Identity Cloud and a user or entity:

* *Journey sessions*, which Advanced Identity Cloud creates to track progress through a journey. These sessions last for the duration of the journey.

* *Authenticated sessions*, which Advanced Identity Cloud creates after a user has authenticated successfully to manage the user's or entity's access to resources.

## Sessions and cookies

Sessions require the user or client to be able to hold on to cookies.

Advanced Identity Cloud issues a cookie to the user or entity at the beginning of a journey. This cookie corresponds to a journey session.

Advanced Identity Cloud issues another cookie to the user or entity after successful authentication. This cookie corresponds to an authenticated session.

The content in these cookies differs depending on the session type and location.

## Session location

Both journey and authenticated sessions can be stored on the client or on the server.

Sessions stored on the server are called [server-side sessions](server-side-sessions.html). Server-side sessions are stored in a database internal to Advanced Identity Cloud called the Core Token Service (CTS) token store.

Sessions stored on the client are called [client-side sessions](client-side-sessions.html). Client-side sessions are stored in the session cookie.

Regardless of the session location, Advanced Identity Cloud issues a cookie to the user or entity. However, the content in the session cookies differs depending on the session's location:

* Server-side sessions contain a *reference* to the session's location in the CTS token store and several other pieces of information. The details about server-side sessions are maintained in the CTS token store.

* Client-side session cookies contain all the details about the session.

Because server-side sessions only contain references to the locations where the session details are stored, while client-side cookies contain all the details about sessions, client-side session cookies are significantly larger than server-side session cookies.

Session location is configurable by realm. The following table illustrates where Advanced Identity Cloud can store sessions:

**Session storage location**

|                        | In the CTS token store | On the client |
| ---------------------- | ---------------------- | ------------- |
| Journey sessions       | ✔                      | ✔ (Default)   |
| Authenticated sessions | ✔ (Default)            | ✔             |

Session storage location can differ per realm to suit specific realm requirements.

Find more information about configuring session locations in:

* [Client-side journey sessions](configure-client-side-sessions.html#proc-configure-client-based-auth-sessions)

* [Client-side authenticated sessions](configure-client-side-sessions.html#proc-configure-client-based-sessions)

* [Server-side journey sessions](configure-server-side-sessions.html#proc-configure-server-side-auth-sessions)

* [Server-side authenticated sessions](configure-server-side-sessions.html#proc-configure-server-side-sessions)

## Session cookie name

Advanced Identity Cloud provides a unique, pseudo-random session cookie name for each tenant.

You can change the value of your tenant's cookie name. You might want to do this for these reasons:

* You want to integrate a legacy system into Advanced Identity Cloud, and it expects to ingest a specific cookie name.

* You want to set the cookie name to a format preferred by your company.

To change the session cookie name:

1. In the Advanced Identity Cloud admin console, open the TENANT menu (upper right).

2. Select Tenant Settings.

3. Select Global Settings.

4. (Optional) View or copy the Cookie field value.

5. Click Cookie.

6. In the Cookie page:

   * To change the cookie name, modify the name in the CookieName field. Invalid values for the cookie name are `iPlanetDirectoryPro` and `Prefix__HOST`.

   * To set the cookie name to its default name, click Reset to Default.

   |   |                                                                                    |
   | - | ---------------------------------------------------------------------------------- |
   |   | Changing the cookie name will invalidate all authenticated sessions in the tenant. |

7. Click Save.

|   |                                                                                                          |
| - | -------------------------------------------------------------------------------------------------------- |
|   | Throughout this documentation, the tenant session cookie name is referred to as `<session-cookie-name>`. |

## Journey session allowlist

Journey session *allowlisting* is an optional feature that maintains a list of journey sessions and their progress in the journey to protect against replay attacks.

When journey session allowlisting is enabled, Advanced Identity Cloud generates a key-value pair for each journey session and stores it for the length of the journey in the following ways:

* For client-side journey sessions, Advanced Identity Cloud stores the key-value pair in the CTS token store.

* For server-side journey sessions, Advanced Identity Cloud creates the key-value pair as a session property in the journey session.

Each time the journey reaches an authentication node, Advanced Identity Cloud modifies the value of the stored key-value pair and sends it to the user or client that's progressing through the journey. The next request to Advanced Identity Cloud to continue the journey must contain the key-value pair and must match the value expected by Advanced Identity Cloud.

If the user or client can't provide the key-value pair with the values Advanced Identity Cloud expects, Advanced Identity Cloud doesn't continue the journey, therefore protecting the journey against malicious users wanting to rewind to a previous node.

Find more information about the allowlisting setting in [Trees](../am-authentication/realm-auth-config.html#authn-core-trees).

### Configure journey session allowlisting

1. In the Advanced Identity Cloud admin console, select Native Consoles > Access Management.

2. Go to Realms > *Realm Name* > Authentication > Settings > Trees.

3. Choose Enable Allowlisting.

4. Click Save Changes.

---

---
title: Manage active session quotas
description: Enable and configure maximum active sessions per user
component: pingoneaic
page_id: pingoneaic:am-sessions:enable-active-session-quotas
canonical_url: https://docs.pingidentity.com/pingoneaic/am-sessions/enable-active-session-quotas.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Sessions", "Quotas", "CTS Store (Sessions &amp; Tokens)", "Load Balancer"]
section_ids:
  enable_active_session_quotas: Enable active session quotas
  adjust_the_number_of_allowed_active_sessions: Adjust the number of allowed active sessions
---

# Manage active session quotas

Enabling session quotas allows you to control the maximum number of active sessions a user can have. The quota applies to all active sessions for the same user, and once a user reaches the session limit, the system removes the least recently used authenticated session for that user.

You enable session quotas by adding an [ESV](../tenants/esvs.html) variable called `esv-global-session-quotas-enable-constraints`, set to `ON`. You must add this ESV to each environment (development, staging and production) where you want to enable session quotas.

The default active session limit is `5`. This applies to alpha, bravo, and top-level realms, impacting both managed users and admins. If needed, you can adjust the allowed number of active sessions for alpha and/or bravo realms through the Access Management native console.

## Enable active session quotas

1. In the Advanced Identity Cloud admin console, go to Tenant Settings > Global Settings > Environment Secrets & Variables.

2. Click the Variables tab, and then click + Add Variable.

3. Enter the following details:

   * Name: `global-session-quotas-enable-constraints`

   * Type: `string`

   * Value: `ON`

4. Click Save.

If you need to disable active session quotas, delete the ESV or change the Value field to `OFF`.

## Adjust the number of allowed active sessions

You can adjust the number of allowed active sessions for alpha and/or bravo realms.

1. In the Advanced Identity Cloud admin console, go to Native Consoles > Access Management > Services.

2. If the session service hasn't already been added, click Add a Service.

3. Select Session, and then click Create.

4. In the Active User Sessions field, enter the number of allowed active user sessions. The default is `5`.

5. Click Save Changes.

Advanced Identity Cloud deletes the user's least recently used authenticated session when the value in the Active User Sessions field is reached.

---

---
title: Manage sessions over REST
description: Manage authenticated sessions using REST API with query and revocation
component: pingoneaic
page_id: pingoneaic:am-sessions:managing-sessions-REST
canonical_url: https://docs.pingidentity.com/pingoneaic/am-sessions/managing-sessions-REST.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Sessions", "REST API", "Log Out", "Properties"]
page_aliases: ["authentication-guide:invalidate-sessions.adoc", "pingoneaic:release-notes:rapid-channel/session-revocation-by-id.adoc", "sessions-guide:managing-sessions-REST.adoc"]
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

The following examples assume you've used a service account to [obtain an access token](../developer-docs/authenticate-to-rest-api-with-access-token.html#get_an_access_token) with the `fr:am:*` scope.

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

|   |                                                                                                                                                         |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The query filter value must be URL-encoded when sent over HTTP.Learn more about query filter parameters in [Query](../developer-docs/crest/query.html). |

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

Use the REST API to read and update properties on authenticated sessions. Define the properties you want to get and set in the [Session Property Whitelist Service](../am-reference/services-configuration.html#realm-amsessionpropertywhitelist) configuration.

You can use the REST API to:

* Get the names of the properties that you can read or update. This is the same set of properties configured in the Session Property Whitelist service.

* Read and update property values.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The ability to set, change and delete session properties is affected by the *session state*:* For server-side sessions, you can manipulate session properties at any time during the session's lifetime.

* For client-side sessions, you can manipulate session properties only during the authentication process, before the user receives the session token from Advanced Identity Cloud. For example, you can set or delete properties on a client-side session from within a post-authentication plugin. |

Differentiate the user who performs the operation from the session affected by the operation as follows:

* Use an [access token](../developer-docs/authenticate-to-rest-api-with-access-token.html#get_an_access_token) for the service account authorized to access these endpoints.

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

You can't set properties internal to Advanced Identity Cloud sessions. If you try to modify an internal property in a REST API call, Advanced Identity Cloud also returns a 403 Forbidden error; for example:

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

Find a list of the default session properties in [Session properties](../am-authentication/auth-nodes-and-journeys.html#session-properties).

---

---
title: Server-side sessions
description: Server-side session storage in CTS token store with caching support
component: pingoneaic
page_id: pingoneaic:am-sessions:server-side-sessions
canonical_url: https://docs.pingidentity.com/pingoneaic/am-sessions/server-side-sessions.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Sessions", "Authentication", "CTS Store (Sessions &amp; Tokens)", "Storage"]
page_aliases: ["sessions-guide:cts-based-sessions.adoc cts-based-sessions.adoc"]
section_ids:
  server_side_journey_sessions: Server-side journey sessions
  server_side_authenticated_sessions: Server-side authenticated sessions
  server_side_sessions_and_in_memory_caching: Server-side sessions and in-memory caching
---

# Server-side sessions

Server-side sessions live in an internal datastore called the Core Token Service (CTS) token store.

When you configure Advanced Identity Cloud to use server-side sessions, Advanced Identity Cloud sends session references to clients. The references don't contain any session state information. Advanced Identity Cloud can modify a server-side session during its lifetime without changing the client's reference to the session.

## Server-side journey sessions

Advanced Identity Cloud uses *journey sessions* to manage progress through a journey.

While progressing through the journey, the session reference is returned to the client after each call to the `authenticate` endpoint and stored in the `authId` object of the JSON response.

Advanced Identity Cloud maintains the journey session in the CTS token store. After the journey has completed, Advanced Identity Cloud returns session state to the client and deletes the server-side authenticated session if the realm to which the user has authenticated is configured for client-side authenticated sessions.

## Server-side authenticated sessions

After the user has successfully authenticated, Advanced Identity Cloud returns a session reference, which is known as an *SSO token*.

For browser clients, Advanced Identity Cloud sets a cookie in the browser that contains the session reference.

For REST clients, Advanced Identity Cloud returns the session reference in response to calls to the `authentication` endpoint.

## Server-side sessions and in-memory caching

Server-side sessions can be cached in memory. When a session that's being requested is cached, session retrieval is nearly instantaneous.

Advanced Identity Cloud automatically caches server-side sessions after retrieving them from the CTS token store. No configuration is required to enable server-side session caching.

---

---
title: Session termination
description: Configure session timeout settings and termination policies
component: pingoneaic
page_id: pingoneaic:am-sessions:session-state-session-termination
canonical_url: https://docs.pingidentity.com/pingoneaic/am-sessions/session-state-session-termination.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Sessions", "Authentication", "CTS Store (Sessions &amp; Tokens)", "Log Out", "Configuration"]
page_aliases: ["sessions-guide:session-state-session-termination.adoc"]
section_ids:
  auth-session-termination-config: Configure authenticated session timeout settings
  add-session-service-realm: Add the Session service to the realm
  session-max-timeout: Set maximum session time-to-live
  session-idle-timeout: Set maximum session idle timeout
---

# Session termination

Authenticated sessions enable single sign-on, letting authenticated users access system resources in Advanced Identity Cloud's control without reauthenticating.

Authenticated sessions are terminated when a configured timeout is reached or when a user performs actions that cause session termination. Session termination effectively logs the user out of all systems protected by Advanced Identity Cloud.

Advanced Identity Cloud terminates server-side authenticated sessions in four situations:

* When a user explicitly logs out.

* When an administrator monitoring sessions [explicitly terminates an authenticated session.](manage-sessions-ui.html)

* When an authenticated session exceeds the [maximum time-to-live](#session-max-timeout).

* When a user is idle for longer than the [maximum session idle time](#session-idle-timeout).

Under these circumstances, Advanced Identity Cloud responds by removing server-side authenticated sessions from the CTS token store and from server memory caches. With the authenticated session no longer present in CTS, Advanced Identity Cloud forces the user to reauthenticate during subsequent attempts to access protected resources.

When a user explicitly logs out of Advanced Identity Cloud, Advanced Identity Cloud also attempts to invalidate the tenant session cookie in the user's browser by sending a `Set-Cookie` header with an invalid session ID and a cookie expiration time that's in the past. In the case of administrator session termination and session timeout, Advanced Identity Cloud can't invalidate the tenant session cookie until the next time the user accesses Advanced Identity Cloud.

## Configure authenticated session timeout settings

Session timeout settings (`maximum session time` and `maximum idle time`) can be set in different locations to provide greater control over terminating authenticated sessions.

Advanced Identity Cloud determines which settings to apply to the authenticated session in the following order of precedence:

1. The session timeout settings for a user.

   Under Native Consoles > Access Management, go to Realms > *Realm Name* > Identities > *Username* > Services > Session to set user level session timeout values.

   If the `Session` service isn't listed, click Add Service and select `Session` in the list.

2. The session timeout settings in a node:

   * Configure session timeout settings in the [Set Session Properties node](https://docs.pingidentity.com/auth-node-ref/latest/auth-node-set-session-properties.html).

   * Configure session timeout settings in the [Scripted Decision node](https://docs.pingidentity.com/auth-node-ref/latest/auth-node-scripted-decision.html) using the `withMaxIdleTime` and `withMaxSessionTime` methods.

     Learn more in [Set authenticated session timeouts](../am-scripting/scripting-api-node.html#scripting-api-node-session-timeouts).

   If a journey has multiple nodes that set session timeouts, Advanced Identity Cloud uses the settings associated with the last executed node to determine the timeouts for the resulting authenticated session.

   If a child journey includes nodes that set session timeouts, Advanced Identity Cloud uses the updated timeouts in the parent journey.

3. The session timeout settings for an authentication journey.

   Session timeout values set on a child journey are ignored.

   Learn more in [Configure authenticated session timeouts in a journey](../am-authentication/auth-nodes-and-journeys.html#configure-auth-session-timeouts-tree).

4. The session timeout values set in the realm.

   The default maximum session timeout is `120` minutes and the default maximum idle time is `30` minutes.

   Enable the Session service in the realm to set realm level session timeout values.

   Learn more in [Add the Session service to the realm](#add-session-service-realm).

### Add the Session service to the realm

Before you can configure the settings for session termination in a realm, add the Session service configuration to that realm if necessary:

1. Under Native Consoles > Access Management, go to Realms > *Realm Name*.

2. Select Services.

3. Open the interface that lets you configure session termination:

   * If the Session service appears in the list of services configured for the realm, select Session.

   * If the Session service doesn't appear in the list of services configured for the realm, add it:

     1. Click Add a Service.

     2. Select Session in the list.

   The Session page appears, showing the Dynamic Attributes tab.

4. Click Save Changes.

Learn more in [Dynamic attributes](../am-reference/services-configuration.html#realm-session-dynamic-attributes).

### Set maximum session time-to-live

When configuring the maximum session time-to-live, balance security and user experience. Depending on your application, it could be acceptable for your users to log in once a month. Financial applications, for example, often terminate their sessions in less than an hour.

The longer an authenticated session is valid, the larger the window during which a malicious user could impersonate a user if they were able to hijack a session cookie.

The maximum session time-to-live is `120` minutes by default.

The following steps configure the maximum session time in a realm, but you can also [configure](#auth-session-termination-config) it for a user, in a node or in a journey:

1. Under Native Consoles > Access Management, go to Realms > *Realm Name*.

2. Select Services.

3. Select Session.

4. On the Maximum Session Time property, configure a value suitable for your environment.

5. Save your changes.

If you update the maximum session time-to-live, you should also set the expiry time for JWT tokens to the same value:

1. Update the JWT token lifetimes for individual OIDC applications:

   1. In the Advanced Identity Cloud admin console, select Applications.

   2. Select the OIDC application you want to update.

   3. On the Sign On tab, scroll down to General Settings, then click Show advanced settings.

   4. On the Token Lifetimes tab, specify the following properties in seconds:

      * Access token lifetime (seconds)

      * JWT token lifetime (seconds)

   5. Click Save.

2. Update the JWT token lifetimes for the OAuth2 Provider service:

   1. In the Advanced Identity Cloud admin console, select Native Consoles > Access Management.

   2. Select Services > OAuth2 Provider.

   3. On the Core tab, specify the following property in seconds:

      * Access Token Lifetime (seconds)

   4. On the OpenID Connect tab, specify the following property in seconds:

      * OpenID Connect JWT Token Lifetime (seconds)

   5. Click Save Changes.

### Set maximum session idle timeout

Consider a user with a valid authenticated session navigating through pages or making changes to the configuration. If for any reason they leave their desk and their computer remains open, a malicious user could take the opportunity to impersonate them.

Session idle timeout can help mitigate those situations by logging out users after a specified duration of inactivity.

The maximum session idle timeout is `30` minutes by default.

|   |                                                                                                                                      |
| - | ------------------------------------------------------------------------------------------------------------------------------------ |
|   | You can only use session idle timeout in realms configured for [server-side sessions](server-side-sessions.html#cts-based-sessions). |

The following steps configure the maximum idle time in a realm, but you can also [configure](#auth-session-termination-config) it for a user, in a node or in a journey:

1. Under Native Consoles > Access Management, go to Realms > *Realm Name*.

2. Select Services.

3. Select Session.

4. On the Maximum Idle Time property, configure a value suitable for your environment.

5. Save your changes.

---

---
title: Session upgrade with MFA
description: Step-up authentication with multi-factor requirement for sensitive resources
component: pingoneaic
page_id: pingoneaic:am-sessions:session-upgrade
canonical_url: https://docs.pingidentity.com/pingoneaic/am-sessions/session-upgrade.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Sessions", "Authentication", "Step-up Authentication", "Configuration", "REST API"]
page_aliases: ["sessions-guide:session-upgrade.adoc"]
section_ids:
  how_it_works: How it works
  session-upgrade-prerequisites: PEP-based session upgrade
  proc-session-upgrade-REST: Working with advice
---

# Session upgrade with MFA

When an authenticated user must present additional credentials to access sensitive resources, Advanced Identity Cloud provides *session upgrade* to perform step-up authentication.

This lets you require credentials only when you really need them. A user signs in quickly to access protected resources like their profile data or their shopping cart. When they are ready to make a purchase, the session upgrade mechanism requires authentication with another factor (MFA).

For *single-use* step-up authentication, read [Authorize one-time access with transactional authz](../am-authorization/transactional-authorization.html) instead.

## How it works

A client application, an authentication journey, or a policy enforcement point (PEP) initiates session upgrade:

* A client application triggers session upgrade directly.

  The application redirects the authenticated user to the appropriate journey in one of two ways:

  * To **force reauthentication with the same journey**, add the `ForceAuth=true` query string parameter. The following example reauthenticates the user in the `alpha` realm with the `StrongAuthJourney` even if the current session already satisfies the authentication requirements:

    ```none
    https://<tenant-env-fqdn>/am/XUI/?realm=alpha&ForceAuth=true&authIndexType=service&authIndexValue=StrongAuthJourney
    ```

  * **Upgrade the session by redirecting the user to a different journey**. For example, the user authenticated through the `Login` journey and later is sent to a URL that specifies the `StrongAuthJourney`.

    In this case, the change of journey itself triggers session upgrade, so you don't need to include the `ForceAuth` parameter.

* An authentication journey with the [Anonymous Session Upgrade node](https://docs.pingidentity.com/auth-node-ref/latest/anonymous-session-upgrade.html) upgrades an anonymous session.

* Advanced Identity Cloud advises a PEP to initiate session upgrade.

  In this case, PingGateway, a web agent, a Java agent, or a custom PEP protects sensitive resources.

  You configure [authorization policies](../am-authorization/configuring-policies.html) to require basic authentication for protected resources and session upgrade for sensitive protected resources.

  Session upgrade proceeds as follows:

  ![The sequence diagram illustrates web and Java agents CDSSO flow.](_images/session-upgrade-flow.svg)

  1. An authenticated user requests a sensitive resource.

  2. The PEP requests a policy decision from Advanced Identity Cloud.

  3. Advanced Identity Cloud returns an authorization decision denying access to the resource with *advice* to specify a journey for reauthentication.

  4. The PEP redirects to Advanced Identity Cloud for session upgrade.

  5. The user reauthenticates with the specified journey; for example, with an additional factor.

  6. Advanced Identity Cloud authenticates the user and returns a new session allowing access to the sensitive resource.

**Session upgrade outcomes**

| Session upgrade | Session type | Outcome                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| --------------- | ------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Success         | Client-side  | Issue a new authenticated session.                                                                                                                                                                                                                                                                                                                                                                                                      |
|                 | Server-side  | The outcome depends on what led to session upgrade:- ForceAuth=true

  Issue a new authenticated session even if the existing session met the security requirements.

- [Anonymous Session Upgrade node](https://docs.pingidentity.com/auth-node-ref/latest/anonymous-session-upgrade.html)

  Issue a new authenticated session.

- PEP used *advice*

  Issue a new authenticated session with a copy of existing session properties. |
| Failure         | Any          | Retain existing user session.If session upgrade failed because the login page timed out, redirect the user-agent to the success URL from the last successful authentication.                                                                                                                                                                                                                                                            |

## PEP-based session upgrade

Perform the following tasks to deploy session upgrade with a PEP:

1. Set up a PEP to enforce Advanced Identity Cloud authorization policies.

   Further reading:

   * [PingGateway documentation](https://docs.pingidentity.com/pinggateway/latest)

   * [Java agent documentation](https://docs.pingidentity.com/java-agents/latest)

   * [Web agent documentation](https://docs.pingidentity.com/web-agents/latest)

   * [Request policy decisions over REST](../am-authorization/rest-api-authz-policy-decisions.html)

2. Set up [authorization policies](../am-authorization/configuring-policies.html).

   The following example policy grants any authenticated user access to `*://*:*/sample*` resources:

   ![Any authenticated user can access sample resources](_images/pre-session-upgrade-config.png)

3. Set up an [authentication journey](../journeys/journeys.html) to use for session upgrade.

   For example, configure a journey using a strong authentication mechanism such as MFA.

4. Set up additional authorization policies with conditions to trigger session upgrade.

   The following example policy requires reauthentication with the `StrongAuthJourney` to access `*://*:*/sensitive*` resources:

   ![Access to sensitive resources requires session upgrade](_images/session-upgrade-service.png)

   Authentication journey names are case-sensitive.

## Working with advice

When you use PingGateway, a Java agent, or a web agent as a PEP, the PEP performs session upgrade when necessary.

If you create your own PEP, it must work with policy *advice* [using the REST API](../am-authorization/rest-api-authz-policy-decisions.html). You can try the following demonstration without installing a PEP or an application to protect:

1. Prepare by configuring the policies and journey described in [PEP-based session upgrade](#session-upgrade-prerequisites).

   For the `StrongAuthJourney`, duplicate the default journey to keep authentication simple to demonstrate.

2. [Create a user profile](../identities/manage-identities.html#create_a_user_profile) and record the username and password.

3. Grant the user access to [evaluate policies](../am-authorization/rest-api-authz-policy-decisions.html).

4. Authenticate as the user you created:

   ```bash
   $ curl \
   --request POST \
   --header 'Content-Type: application/json' \
   --header 'X-OpenAM-Username: <username>' \
   --header 'X-OpenAM-Password: <password>' \
   --header 'Accept-API-Version: resource=2.0, protocol=1.0' \
   'https://<tenant-env-fqdn>/am/json/realms/root/realms/alpha/authenticate'
   {
     "tokenId": "<tokenId>",
     "successUrl": "/enduser/?realm=/alpha",
     "realm": "/alpha"
   }
   ```

5. Request a policy decision for an authorized resource, `https://www.example.com/sample`:

   ```bash
   $ curl \
   --request POST \
   --cookie '<session-cookie-name>=<tokenId>' \
   --header 'Content-Type: application/json' \
   --header 'Accept-API-Version: resource=2.0, protocol=1.0' \
   --data '{
     "resources": ["https://www.example.com/sample"],
     "application": "myPolicySet",
     "subject": {
       "ssoToken": "<tokenId>"
     }
   }' \
   'https://<tenant-env-fqdn>/am/json/realms/root/realms/alpha/policies?_action=evaluate'
   [{
     "resource": "https://www.example.com/sample",
     "actions": {
       "POST": true,
       "GET": true
     },
     "attributes": {},
     "advices": {},
     "ttl": <timestamp>
   }]
   ```

   GET and POST actions are allowed.

6. Request a policy decision for a resource requiring session upgrade, `https://www.example.com/sensitive`:

   ```bash
   $ curl \
   --request POST \
   --cookie '<session-cookie-name>=<tokenId>' \
   --header 'Content-Type: application/json' \
   --header 'Accept-API-Version: resource=2.0, protocol=1.0' \
   --data '{
     "resources": ["https://www.example.com/sensitive"],
     "application": "myPolicySet",
     "subject": {
       "ssoToken": "<tokenId>"
     }
   }' \
   'https://<tenant-env-fqdn>/am/json/realms/root/realms/alpha/policies?_action=evaluate'
   [{
     "resource": "https://www.example.com/sensitive",
     "actions": {},
     "attributes": {},
     "advices": {
       "AuthenticateToServiceConditionAdvice": ["/alpha:StrongAuthJourney"]
     },
     "ttl": <timestamp>
   }]
   ```

   According to the policy, no actions are allowed. Advanced Identity Cloud returns advice instead.

7. Format the advice as XML without spaces or line breaks.

   The following formatted example shows the structure of the XML:

   ```xml
   <Advices>
     <AttributeValuePair>
       <Attribute name="AuthenticateToServiceConditionAdvice"/>
       <Value>/alpha:StrongAuthJourney</Value>
     </AttributeValuePair>
   </Advices>
   ```

   Advice can include multiple attribute-value pairs.

8. Remember to remove any spaces and blanks around tags and URL-encode the XML advice:

   `%3CAdvices%3E%3CAttributeValuePair%3E%3CAttribute%20name%3D%22AuthenticateToServiceConditionAdvice%22%2F%3E%3CValue%3E%2Falpha%3AStrongAuthJourney%3C%2FValue%3E%3C%2FAttributeValuePair%3E%3C%2FAdvices%3E`

9. Use the advice to authenticate again with the existing authenticated session:

   In the authentication request set the following:

   * `authIndexType=composite_advice`

   * `authIndexValue=URL-encoded-XML`

   * The user's current SSO token as the cookie

   ```bash
   $ curl \
   --request POST \
   --header 'Content-Type: application/json' \
   --cookie '<session-cookie-name>=<tokenId>' \
   --header 'Accept-API-Version: resource=2.1, protocol=1.0' \
   'https://<tenant-env-fqdn>/am/json/realms/root/realms/alpha/authenticate?authIndexType=composite_advice&authIndexValue=<URL-encoded-XML>'
   {
     "authId": "<auth-id>",
     "callbacks": [{
       "type": "NameCallback",
       "output": [{
         "name": "prompt",
         "value": "User Name"
       }],
       "input": [{
         "name": "IDToken1",
         "value": ""
       }],
       "_id": 0
     }, {
       "type": "PasswordCallback",
       "output": [{
         "name": "prompt",
         "value": "Password"
       }],
       "input": [{
         "name": "IDToken2",
         "value": ""
       }],
       "_id": 1
     }],
     "header": "Sign In",
     "description": "New here? <a href=\"#/service/Registration\">Create an account</a><br><a href=\"#/service/ForgottenUsername\">Forgot username?</a><a href=\"#/service/ResetPassword\"> Forgot password?</a>"
   }
   ```

   Advanced Identity Cloud returns an authentication callback as the response body. Learn more in [Authenticate over REST](../am-authentication/authn-rest.html).

10. Renew the request with the same parameters and cookie as before, responding to the callback with the details in the request body:

    ```bash
    $ curl \
    --request POST \
    --header 'Content-Type: application/json' \
    --cookie '<session-cookie-name>=<tokenId>' \
    --header 'Accept-API-Version: resource=2.1, protocol=1.0' \
    --data '{
      "authId": "<auth-id>",
      "callbacks": [{
        "type": "NameCallback",
        "output": [{
          "name": "prompt",
          "value": "User Name"
        }],
        "input": [{
          "name": "IDToken1",
          "value": "<username>"
        }],
        "id": 0
      }, {
        "type": "PasswordCallback",
        "output": [{
          "name": "prompt",
          "value": "Password"
        }],
        "input": [{
          "name": "IDToken2",
          "value": "<password>"
        }],
        "_id": 1
      }]
    }' \
    'https://<tenant-env-fqdn>_/am/json/realms/root/realms/alpha/authenticate?authIndexType=composite_advice&authIndexValue=<URL-encoded-XML>'
    {
      "tokenId": "<new-tokenId>",
      "successUrl": "/enduser/?realm=/alpha",
      "realm": "/alpha"
    }
    ```

    Advanced Identity Cloud returns a new SSO token on successful authentication. This represents the upgraded session.

11. Request a policy decision for the resource again using the new SSO token:

    ```bash
    $ curl \
    --request POST \
    --cookie '<session-cookie-name>=<new-tokenId>' \
    --header 'Content-Type: application/json' \
    --header 'Accept-API-Version: resource=2.0, protocol=1.0' \
    --data '{
      "resources": ["https://www.example.com/sensitive"],
      "application": "myPolicySet",
      "subject": {
        "ssoToken": "<new-tokenId>"
      }
    }' \
    'https://<tenant-env-fqdn>/am/json/realms/root/realms/alpha/policies?_action=evaluate'
    [{
      "resource": "https://www.example.com/sensitive",
      "actions": {
        "POST": true,
        "GET": true
      },
      "attributes": {},
      "advices": {},
      "ttl": <timestamp>
    }]
    ```

    Notice that the user now has access.

---

---
title: Sessions
description: Introduction to session management concepts and procedures
component: pingoneaic
page_id: pingoneaic:am-sessions:preface
canonical_url: https://docs.pingidentity.com/pingoneaic/am-sessions/preface.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Sessions"]
page_aliases: ["index.adoc", "sessions-guide:preface.adoc"]
---

# Sessions

These topics cover concepts and implementation procedures to manage sessions with Advanced Identity Cloud.

[icon: book, set=fas, size=3x]

#### [Sessions and cookies](about-sessions.html)

Learn about the different types of sessions in Advanced Identity Cloud.

[icon: edit, set=fas, size=3x]

#### [Manage sessions](manage-sessions-ui.html)

View and manage sessions in the UI or over REST.

[icon: cogs, set=fas, size=3x]

#### [Session upgrade](session-upgrade.html)

Discover how Advanced Identity Cloud performs step-up authentication.

---

---
title: View and terminate sessions (UI)
description: View and terminate user sessions using the Access Management console
component: pingoneaic
page_id: pingoneaic:am-sessions:manage-sessions-ui
canonical_url: https://docs.pingidentity.com/pingoneaic/am-sessions/manage-sessions-ui.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Sessions", "User Interface"]
page_aliases: ["sessions-guide:manage-sessions-ui.adoc"]
section_ids:
  view-sessions: View authenticated sessions
  terminate-sessions: Terminate authenticated sessions
---

# View and terminate sessions (UI)

If you have configured Advanced Identity Cloud to use [server-side authenticated sessions](server-side-sessions.html), you can view and terminate users' sessions under Native Consoles > Access Management.

Learn about advanced functionality that's not available in the UI in [Manage sessions over REST](managing-sessions-REST.html).

## View authenticated sessions

1. Under Native Consoles > Access Management, go to Realms > *Realm Name*.

2. Select Sessions.

3. The Sessions page appears with a single field in which to enter a username.

   Advanced Identity Cloud uses generated UUIDs for usernames. To get a UUID:

   1. In the Advanced Identity Cloud admin console, go to Identities > Manage.

   2. From the *Realm Name* - Users list, click the user for which you want to obtain the UUID.

   3. Click Raw JSON from the left-hand menu, and copy the value for `_id`. For example, `0c8a31fa-a763-4fca-9352-0c3cc84a2138`.

4. Paste the UUID in the Session page's username field.

5. Click the entry in the drop-down list to search for the user's authenticated sessions.

   If the user has active server-side sessions, Advanced Identity Cloud retrieves the authenticated sessions for the user and displays them in a table:

   ![An administrator can view and invalidate server-side sessions.](_images/session-management.png)

## Terminate authenticated sessions

To terminate a user's server-side authenticated session:

1. [View the user's authenticated sessions](#view-sessions).

2. Select the authenticated session you want to terminate.

3. Click the Invalidate Selected button.

After you terminate a user's session, the user must reauthenticate to access resources protected by Advanced Identity Cloud.

Deleting a user doesn't remove a user's server-side authenticated sessions. After deleting a user, use the preceding steps to check for any authenticated sessions for the user and invalidate them.