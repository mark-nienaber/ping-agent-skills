---
title: Client-side sessions
description: Manage client-side sessions where PingAM returns session state to clients after each request and requires it to be passed back in subsequent requests
component: pingam
version: 8.1
page_id: pingam:am-sessions:client-based-sessions
canonical_url: https://docs.pingidentity.com/pingam/8.1/am-sessions/client-based-sessions.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Sessions", "Authentication", "CTS Store (Sessions &amp; Tokens)"]
page_aliases: ["sessions-guide:client-based-sessions.adoc"]
section_ids:
  advantages_of_client_side_sessions: Advantages of client-side sessions
  session-state-client-based-limitations: Limitations of client-side sessions
  client_side_journey_sessions: Client-side journey sessions
  client_side_authenticated_sessions: Client-side authenticated sessions
---

# Client-side sessions

For *client-side sessions*, AM returns the session state to the client after each request and requires the session state to be passed in with the subsequent request.

For security reasons, you should configure AM to sign and/or encrypt client-side journey and authenticated sessions. Decrypting and verifying the session can be an expensive operation to perform on each request. AM therefore caches the decrypt sequence in memory to improve performance.

|   |                                                                                                                                                                                                                                                                             |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | * Find information about configuring client-side security in [Client-side session security](../security/session-state-configure-cookie-security.html).

* Find information about configuring AM with sticky load balancing in [Load balancing](../setup/configure-lb.html). |

## Advantages of client-side sessions

* Unlimited horizontal scalability for session infrastructure

  Client-side sessions provide unlimited horizontal scalability by storing the session state on the client as a signed and encrypted JWT.

  Overall performance on hosts using client-side sessions can be easily improved by adding more hosts to the AM deployment.

* Replication-free deployments

  Global deployments may struggle to keep their CTS token stores synchronized when distances are long and updates are frequent.

  Client-side sessions aren't constrained by the replication speed of the CTS token store. Therefore, client-side sessions are usually more suitable for deployments where a session can be serviced at any time by any server.

## Limitations of client-side sessions

The following features *aren't supported* or have *limited support* for client-side journey sessions and authenticated sessions:

| Functionality                                                                                                         | Details                                                                  |
| --------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------ |
| [Session quotas](../security/session-quotas.html)                                                                     | Not supported                                                            |
| [Session idle timeout](../security/session-state-session-termination.html)                                            | Not supported                                                            |
| [Cross-domain single sign-on with restricted tokens](../security/enable-cdsso-cookie-hijacking-protection.html)       | Not supported for web and Java agents                                    |
| [Session signing and encryption](../security/session-state-configure-cookie-security.html#policy_agent5_client-based) | Not supported for web and Java agents                                    |
| [Uncompressed sessions](../security/session-state-configure-cookie-security.html#policy_agent5_client-based)          | Not supported for web and Java agents                                    |
| [SAML 2.0 single logout using the SOAP binding](../am-saml2/saml2-configuration.html#saml2-and-session-state)         | Not supported for journey sessions.Supported for authenticated sessions. |
| [Session management using the AM admin UI](managing-sessions-console.html)                                            | Not supported                                                            |
| [Session notification](../setup/services-configuration.html#global-session)                                           | Limited support                                                          |

## Client-side journey sessions

Client-side journey sessions are configured by default in new installations.

While progressing through the authentication tree, the journey session state is returned to the client after each call to the `authenticate` endpoint and stored in the `authId` object of the JSON response.

If the realm the user authenticated to is configured for server-side authenticated sessions, AM creates the authenticated session in the CTS token store when the journey completes.

Storing journey sessions on the client allows any AM server to handle the journey at any point in time without load balancing requirements.

Journey session allowlisting is an optional feature that maintains a list of in-progress journey sessions and their progress in the journey to protect against replay attacks. Learn more in [Journey session allowlisting](../security/auth-session-whitelist.html).

## Client-side authenticated sessions

For browser-based clients, AM sets a cookie in the browser that contains the session state. When the browser transmits the cookie back to AM, AM decodes the session state from the cookie. For REST-based clients, AM sends the cookie in a header. Find more information about session cookies in [Session cookies and session security](session-state-cookies.html).

Session denylisting is an optional feature that maintains a list of logged out client-side authenticated sessions in the CTS token store. Find more information about session termination and session denylisting in [Session termination](session-state-session-termination.html).

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | A user is granted a client-side journey session *while they are completing the authentication tree*. If session denylisting is enabled, this journey session is "logged out" when the tree is completed, to prevent replay attacks. This "logging out" adds the journey session to the session *denylist* for client-side sessions. In the CTS store, this takes the form of a `SESSION_BLACKLIST` token that exists for the life of the journey session. |

Learn more in [Choose where to store sessions](session-state-use-cases.html).

---

---
title: Configure client-side sessions
description: Configure client-side sessions in PingAM to store session state on the client instead of the server, including authentication journey and authenticated sessions
component: pingam
version: 8.1
page_id: pingam:am-sessions:impl-client-based-sessions
canonical_url: https://docs.pingidentity.com/pingam/8.1/am-sessions/impl-client-based-sessions.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Sessions", "Authentication", "CTS Store (Sessions &amp; Tokens)", "Setup &amp; Configuration", "Storage"]
page_aliases: ["sessions-guide:impl-client-based-sessions.adoc"]
section_ids:
  proc-configure-client-based-auth-sessions: Configure client-side journey sessions
  proc-configure-client-based-sessions: Configure client-side authenticated sessions
---

# Configure client-side sessions

Client-side sessions require additional setup in your environment to keep the sessions safe, and to ensure both the browser and the web server where AM runs can manage large cookies. Additionally, some AM features can't be used with client-side sessions. Review the following list before configuring client-side sessions:

Planning for client-side sessions

* Make sure the trust store used by AM has the necessary certificates installed:

  * A certificate is required for encrypting JWTs containing client-side sessions.

  * If you are using RS256 signing, then a certificate is required to sign JWTs. (HMAC signing uses a shared secret.)

  The same certificates must be stored on all servers participating in an AM site. Find information about managing certificates for AM in [Secrets, certificates, and keys](../security/secrets-certs-keys.html).

* Make sure your users' browsers can accommodate larger session cookie sizes required by client-side sessions. Find information about session cookie sizes in [Session cookies and session security](session-state-cookies.html).

* Make sure the AM web container can accommodate an HTTP header that is 16K in size or greater. When using Apache Tomcat as the AM web container, configure the `server.xml` file's `maxHttpHeaderSize` property to `16384` or higher.

* Make sure your deployment doesn't require any of the capabilities specified in the list of [limitations](client-based-sessions.html#session-state-client-based-limitations) that apply to client-side sessions.

## Configure client-side journey sessions

1. In the AM admin UI, go to Realms > *realm name* > Authentication > Settings > Trees.

2. From the Authentication session state management scheme drop-down list, select `JWT`.

3. In the Max duration (minutes) field, enter the maximum life of the journey session in minutes.

   You can also set the maximum duration in a tree or at the node level. Learn more in [Maximum duration](../am-authentication/suspended-auth.html#maximum-duration).

4. Save your changes.

5. Go to Configure > Authentication > Core > Security.

6. In the Organization Authentication Signing Secret field, enter a base64-encoded HMAC secret that AM uses to sign the JWT that is passed back and forth between the client and AM during the authentication process. The secret must be at least 128-bits in length.

7. Save your changes.

8. Protect your client-side journey sessions.

   Learn more in [Client-side session security](../security/session-state-configure-cookie-security.html).

## Configure client-side authenticated sessions

1. In the AM admin UI, go to Realms > *realm name* > Authentication > Settings > General.

2. Select the Use Client-Side Sessions check box.

3. Save your changes.

4. Protect your client-side authenticated sessions.

   Learn more in [Client-side session security](../security/session-state-configure-cookie-security.html).

5. Verify that AM creates a client-side authenticated session when non-administrative users authenticate to the realm.

   Perform the following steps:

   * Authenticate to the AM admin UI as the top-level administrator (by default, the `amAdmin` user). Note that sessions for the top-level administrator are always stored in the CTS token store.

   * Go to Realms > *realm name* > Sessions.

   * Verify that a session is present for the `amAdmin` user.

   * In your browser, examine the AM cookie, named `iPlanetDirectoryPro` by default. Copy and paste the cookie's value into a text file and note its size.

   * Open an incognito browser window that won't have access to the `iPlanetDirectoryPro` cookie for the `amAdmin` user.

   * Authenticate to AM as a non-administrative user in the realm for which you enabled client-side authenticated sessions. Make sure you don't authenticate as the `amAdmin` user this time.

   * In your browser, examine the `iPlanetDirectoryPro` cookie. Copy and paste the cookie's value into a second text file and note its size. The size of the client-side session cookie's value should be considerably larger than the size of the cookie used by the server-side session for the `amAdmin` user. If the cookie isn't bigger, you've not enabled client-side authenticated sessions correctly.

   * Return to the original browser window in which the AM admin UI appears.

   * Refresh the window containing the Sessions page.

   * Verify that a session still appears for the `amAdmin` user, but that no session appears for the non-administrative user in the realm with client-side authenticated sessions enabled.

---

---
title: Configure in-memory journey sessions
description: Configure PingAM to store journey sessions in memory using sticky load balancing and HMAC signing
component: pingam
version: 8.1
page_id: pingam:am-sessions:impl-in-memory-auth-sessions
canonical_url: https://docs.pingidentity.com/pingam/8.1/am-sessions/impl-in-memory-auth-sessions.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Sessions", "CTS Store (Sessions &amp; Tokens)", "Setup &amp; Configuration", "Load Balancer", "Storage"]
page_aliases: ["sessions-guide:impl-in-memory-auth-sessions.adoc"]
---

# Configure in-memory journey sessions

Follow these steps to store journey sessions in AM's memory:

1. Make sure you have configured AM for [sticky load balancing](../setup/configure-lb.html).

2. In the AM admin UI, go to Realms > *realm name* > Authentication > Settings > Trees.

3. From the Authentication session state management scheme drop-down list, select `In-Memory`.

4. In the Max duration (minutes) field, enter the maximum life of the journey session in minutes.

   You can also set the maximum duration in a tree or at the node level. Learn more in [Maximum duration](../am-authentication/suspended-auth.html#maximum-duration).

5. Save your changes.

6. Go to Configure > Authentication > Core > Security.

7. In the Organization Authentication Signing Secret field, enter a base64-encoded HMAC secret that AM uses to sign the JWT that is passed back and forth between the client and AM during the authentication process. The secret must be, at least, 128-bits in length.

8. Save your changes.

---

---
title: Configure server-side sessions
description: Configure PingAM to use server-side sessions stored in the CTS token store for journey and authenticated sessions
component: pingam
version: 8.1
page_id: pingam:am-sessions:impl-CTS-based-sessions
canonical_url: https://docs.pingidentity.com/pingam/8.1/am-sessions/impl-CTS-based-sessions.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Sessions", "Authentication", "CTS Store (Sessions &amp; Tokens)", "Setup &amp; Configuration", "Storage"]
page_aliases: ["sessions-guide:impl-CTS-based-sessions.adoc"]
section_ids:
  proc-configure-server-side-auth-sessions: Configure server-side journey sessions
  proc-configure-server-side-sessions: Configure server-side authenticated sessions
---

# Configure server-side sessions

By default, AM configures the CTS token store schema in the AM configuration store. Before configuring your AM deployment to use server-side journey or authenticated sessions, we recommend you install and configure an external CTS token store. Learn more in [Core Token Service (CTS)](../cts/preface.html).

Server-side journey and authenticated sessions benefit from configuring sticky load balancing. Learn more in [Load balancing](../setup/configure-lb.html).

## Configure server-side journey sessions

1. In the AM admin UI, go to Realms > *realm name* > Authentication > Settings > Trees.

2. From the Authentication session state management scheme drop-down list, select `CTS`.

3. In the Max duration (minutes) field, enter the maximum life of the journey session in minutes.

   You can also set the maximum duration in a tree or at the node level. Learn more in [Maximum duration](../am-authentication/suspended-auth.html#maximum-duration).

4. Save your changes.

5. Go to Configure > Authentication > Core > Security.

6. In the Organization Authentication Signing Secret field, enter a base64-encoded HMAC secret that AM uses to sign the JWT that is passed back and forth between the client and AM during the authentication process. The secret must be at least 128-bits in length.

7. Save your changes.

## Configure server-side authenticated sessions

1. In the AM admin UI, go to Realms > *realm name* > Authentication > Settings > General.

2. Ensure the Use Client-Side Sessions check box is not selected.

3. Save your changes.

4. Verify that AM creates a server-side authenticated session when non-administrative users authenticate to the realm. Perform the following steps:

   * Authenticate to AM as a non-administrative user in the realm you enabled for server-side sessions.

   * In a different browser, authenticate to AM as an administrative user. For example, `amAdmin`.

   * Go to Realms > *realm name* > Sessions.

   * Verify that a session is present for the non-administrative user.

---

---
title: In-memory sessions
description: Store journey session state in PingAM memory during authentication, then transition to server-side or client-side storage after successful authentication
component: pingam
version: 8.1
page_id: pingam:am-sessions:sec-in-memory-sessions
canonical_url: https://docs.pingidentity.com/pingam/8.1/am-sessions/sec-in-memory-sessions.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Sessions", "Cookie", "Storage", "Configuration", "Load Balancer"]
page_aliases: ["sessions-guide:sec-in-memory-sessions.adoc"]
section_ids:
  advantages_of_in_memory_sessions: Advantages of in-memory sessions
  in_memory_journey_sessions: In-memory journey sessions
  in_memory_authenticated_sessions: In-memory authenticated sessions
---

# In-memory sessions

In-memory sessions reside in AM's memory. AM sends clients a reference to the session, but the reference doesn't contain any of the session state information.

## Advantages of in-memory sessions

* Faster performance with equivalent host

  AM servers configured for in-memory journey sessions can validate more sessions per second per host than those configured for client-side or server-side journey sessions.

* Session information isn't in browser cookies

  Journey session information resides in AM's memory, and isn't accessible to users. With client-side sessions, journey session information is held in browser cookies.

## In-memory journey sessions

In-memory journey sessions are configured by default after an upgrade.

While progressing through the authentication tree, the journey session state is returned to the client after each call to the `authenticate` endpoint and stored in the `authId` object of the JSON response.

AM maintains the user's journey session in its memory. After the journey has completed, AM performs the following tasks:

* If the realm to which the user has authenticated is configured for server-side authenticated sessions, AM stores the authenticated session in the CTS token store and deletes the journey session from memory.

* If the realm to which the user has authenticated is configured for client-side authenticated sessions, AM stores the authenticated session in a cookie on the user's browser and deletes the journey session from memory.

Journey session allowlisting is an optional feature that maintains a list of in-progress journey sessions and their progress in the authentication flow to protect against replay attacks. Learn more in [Journey session allowlisting](../security/auth-session-whitelist.html).

|   |                                                                                                                                                                                                                                                                                                                                                 |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Deployments where AM stores journey sessions in memory require sticky load balancing to route all requests for a specific journey to the same AM server. If a request reaches a different AM server, the journey starts again.Find information about configuring AM with sticky load balancing in [Load balancing](../setup/configure-lb.html). |

## In-memory authenticated sessions

*AM doesn't support in-memory sessions for authenticated users*.

---

---
title: Introduction to sessions
description: Understand how PingAM uses journey sessions and authenticated sessions to track user interactions and manage access to resources, and decide where to store them
component: pingam
version: 8.1
page_id: pingam:am-sessions:about-sessions
canonical_url: https://docs.pingidentity.com/pingam/8.1/am-sessions/about-sessions.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Sessions", "CTS Store (Sessions &amp; Tokens)", "Load Balancer"]
page_aliases: ["sessions-guide:about-sessions.adoc"]
section_ids:
  session_location: Session location
  auth-session-storage: Where to store journey sessions
  session-storage: Where to store authenticated sessions
---

# Introduction to sessions

AM uses two types of tokens that represent an exchange of information, usually interactive, between AM and a user or identity:

* *Journey sessions*, which AM creates to track progress through a journey. These sessions last for the duration of the journey.

* *Authenticated sessions*, which AM creates after a user has authenticated successfully to manage the user's or entity's access to resources.

AM session-related services are stateless unless otherwise indicated. They don't hold any session information local to the AM instances.

Instead, they store session information either in the CTS token store (*server-side sessions*) or on the client (*client-side sessions*).

## Session location

Sessions have different characteristics depending on where AM stores the sessions.

Both journey sessions and authenticated sessions can be stored on the client or on the server.

Session location is configured at the realm level.

The following table illustrates where AM can store sessions:

**Session storage location**

|                        | In the CTS token store | On the client                    | In AM's memory            |
| ---------------------- | ---------------------- | -------------------------------- | ------------------------- |
| Journey sessions       | ✔                      | ✔ (Default in new installations) | ✔ (Default after upgrade) |
| Authenticated sessions | ✔ (Default)            | ✔                                | ✖                         |

|   |                                                                                                                                                                                                                                                                                                                                                                                       |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | You can configure different session locations within the same AM deployment to suit the requirements of each realm.You can also configure the *journey* session location independently of the *authenticated* session location. For example, you could configure the same realm for client-side journey sessions and server-side authenticated sessions if it suits your environment. |

Choosing where to store sessions is an important decision you must make by realm. Review the information in the following tables before configuring sessions.

### Where to store journey sessions

Consider the following factors when choosing storage location for journey sessions.

**Impact of storage location for journey sessions**

|                                        | Server-side journey sessions                                                                                  | Client-side journey sessions                                      | In-memory journey sessions                                       |
| -------------------------------------- | ------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------- | ---------------------------------------------------------------- |
| **Session location**                   | Authoritative source: CTS token store. Sessions might also be cached in AM's memory for improved performance. | On the client. No CTS storage or replication overheads.           | In AM server's memory.                                           |
| **Load balancer requirements**         | None. Session stickiness recommended for performance.                                                         | None. Session stickiness recommended for performance.             | Session stickiness.                                              |
| **Core token service usage**           | Authoritative source for authenticated sessions. Session allowlisting, when enabled.                          | Session allowlisting, when enabled.                               | None.                                                            |
| **Uninterrupted session availability** | No special configuration required.                                                                            | No special configuration required.                                | Not available.                                                   |
| **Session security**                   | Sessions reside in the CTS token store, and are not accessible to users.                                      | Sessions reside on the client and should be signed and encrypted. | Sessions reside in AM's memory, and are not accessible to users. |

### Where to store authenticated sessions

Consider the following factors when choosing storage location for authenticated sessions.

**Impact of storage location for authenticated sessions**

|                                         | Server-side authenticated sessions                                                                                          | Client-side authenticated sessions                               |
| --------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------- |
| **Hardware**                            | Higher I/O and memory consumption.                                                                                          | Higher CPU consumption.                                          |
| **Logical hosts**                       | Variable or large number of hosts.                                                                                          | Variable or large number of hosts.                               |
| **Session monitoring**                  | Available.                                                                                                                  | Not available.                                                   |
| **Session location**                    | Authoritative source: CTS token store. Authenticated sessions could also be cached in AM's memory for improved performance. | In a cookie in the client.                                       |
| **Load balancer requirements**          | None. Session stickiness recommended for performance.                                                                       | None. Session stickiness recommended for performance.            |
| **Uninterrupted session availability**  | No special configuration required.                                                                                          | No special configuration required.                               |
| **Core token service usage**            | Authoritative source for authenticated sessions.                                                                            | Provides session denylisting for logged out sessions.            |
| **Core token service demand**           | Heavier.                                                                                                                    | Lighter.                                                         |
| **Session security**                    | Authenticated sessions reside in the CTS token store, and aren't accessible to users.                                       | Authenticated sessions should be signed and encrypted.(1)        |
| **Cross-domain single sign-on support** | All AM capabilities supported.                                                                                              | Web agents and Java agents: Supported without restricted tokens. |

(1) Web agents and Java agents support either signing or encrypting client-side sessions, but not both. Learn more in [Client-side session security and agents](../security/session-state-configure-cookie-security.html#policy_agent5_client-based).

---

---
title: Manage sessions using REST
description: Use REST API endpoints to retrieve session information, validate session tokens, and refresh server-side sessions in PingAM
component: pingam
version: 8.1
page_id: pingam:am-sessions:managing-sessions-REST
canonical_url: https://docs.pingidentity.com/pingam/8.1/am-sessions/managing-sessions-REST.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Sessions", "REST API", "Log Out", "Properties"]
page_aliases: ["authentication-guide:action-invalidating-sessions.adoc", "sessions-guide:managing-sessions-REST.adoc"]
section_ids:
  rest-api-session-information: Get information about sessions
  rest-api-token-validation: Validate sessions
  rest-api-session-refresh: Refresh server-side sessions
  invalidate-sessions: Invalidate sessions
  invalidate-sessions-by-handle: Invalidate specific sessions
  invalidate-sessions-user: Invalidate all sessions for a user
  rest-api-session-properties: Get and set session properties
---

# Manage sessions using REST

To manage authenticated sessions using REST, send requests to the `/json/sessions` endpoint, as shown in the following examples.

## Get information about sessions

To get information about an authenticated session, send an HTTP POST request to the `/json/sessions/` endpoint, using the `getSessionInfo` action.

This action returns information about the session token provided in the `iPlanetDirectoryPro` header by default. To get information about a different session token, include it in the POST body as the value of the `tokenId` parameter.

|   |                                                                                                                                                                                                                                                                                                                                                               |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | To retrieve custom session properties in authentication trees, use a [Scripted Decision node](https://docs.pingidentity.com/auth-node-ref/8.1/scripted-decision.html) for user attributes and session properties or a [Set Session Properties node](https://docs.pingidentity.com/auth-node-ref/8.1/set-session-properties.html) for session properties only. |

The following example shows an administrative user passing their session token in the `iPlanetDirectoryPro` header and the session token of `bjensen` as the value of the `tokenId`:

```bash
$ curl \
--request POST \
--header "iPlanetDirectoryPro: AQICS…​NzEz*" \
--header "Accept-API-Version: resource=4.0" \
--header "Content-type: application/json" \
--data '{ "tokenId": "BXCCq…​NX*1*" }' \
'https://am.example.com:8443/am/json/realms/root/sessions/?_action=getSessionInfo'
{
    "username": "bjensen",
    "universalId": "id=bjensen,ou=user,dc=am,dc=example,dc=com",
    "realm": "/",
    "latestAccessTime": "2024-02-21T14:31:18Z",
    "maxIdleExpirationTime": "2024-02-21T15:01:18Z",
    "maxSessionExpirationTime": "2024-02-21T16:29:56Z",
    "properties": {
        "AMCtxId": "aba7b4f3-16ff-4680-b06a-d7ba237d3730-91932"
    }
}
```

The `getSessionInfo` action doesn't refresh the session idle timeout. To obtain session information about a server-side session *and* reset the idle timeout, use the `getSessionInfoAndResetIdleTime` action, as follows:

```bash
$ curl \
--request POST \
--header "iPlanetDirectoryPro: AQICS…​NzEz*" \
--header "Accept-API-Version: resource=4.0, protocol=1.0" \
--header "Content-type: application/json" \
--data '{ "tokenId": "BXCCq…​NX*1*" }' \
'https://am.example.com:8443/am/json/realms/root/sessions/?_action=getSessionInfoAndResetIdleTime'
{
    "username": "bjensen",
    "universalId": "id=bjensen,ou=user,dc=am,dc=example,dc=com",
    "realm": "/",
    "latestAccessTime": "2020-02-21T14:32:49Z",
    "maxIdleExpirationTime": "2020-02-21T15:02:49Z",
    "maxSessionExpirationTime": "2020-02-21T16:29:56Z",
    "properties": {
        "AMCtxId": "aba7b4f3-16ff-4680-b06a-d7ba237d3730-91932"
    }
}
```

|   |                                                                                                                                                                                                                                                                                                                                                                                           |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | * You can't reset the idle timeout of a client-side session.

* The `AMCtxId` property represents the audit ID for the session. To return the `AMCtxId` property in the session query response (as in this example) you must include `AMCtxId` in the Session Properties to return for session queries field under Realms > *realm name* > Services > Session Property Whitelist Service. |

## Validate sessions

To check if a session token is valid, send an HTTP POST request to the `/json/sessions/` endpoint with the `validate` action. Provide the session token in the POST data as the value of the `tokenId` parameter.

Provide the session token of an *administrative user* in the `iPlanetDirectoryPro` header.

|   |                                                                                                           |
| - | --------------------------------------------------------------------------------------------------------- |
|   | If you don't specify a `tokenId`, this request validates the session in the `iPlanetDirectoryPro` header. |

The following example shows an administrative user, such as `amAdmin`, validating a session token for `bjensen`:

```bash
$ curl \
--request POST \
--header "Content-type: application/json" \
--header "iPlanetDirectoryPro: AQICS…​NzEz*" \
--header "Accept-API-Version: resource=3.0, protocol=1.0" \
--data '{ "tokenId": "BXCCq…​NX*1*" }' \
'https://am.example.com:8443/am/json/realms/root/sessions?_action=validate'
```

If the session token is valid, the user ID and its realm is returned:

```bash
{
  "valid": true,
  "sessionUid": "c888fe06-dcb4-43e9-b74a-db838c163aa6-164702",
  "uid": "bjensen",
  "realm": "/alpha"
}
```

By default, validating an authenticated session resets the session's idle time, which triggers a write operation to the CTS token store. To avoid this, include `refresh=false`, for example, `validate&refresh=false`.

## Refresh server-side sessions

To reset the idle time of a server-side authenticated session, send an HTTP POST request to the `/json/sessions/` endpoint, with the `refresh` action. This action refreshes the session token provided in the `iPlanetDirectoryPro` header by default. To refresh a different session token, include it in the POST body as the value of the `tokenId` query parameter.

The following example shows an administrative user passing their session token in the `iPlanetDirectoryPro` header, and bjensen's session token as the `tokenId` parameter:

```bash
$ curl \
--request POST \
--header 'Content-Type: application/json' \
--header "iPlanetDirectoryPro: AQICS…​NzEz*" \
--header "Accept-API-Version: resource=3.1, protocol=1.0" \
--data '{ "tokenId": "BXCCq…​NX*1*" }' \
'https://am.example.com:8443/am/json/realms/root/sessions/?_action=refresh'
{
  "uid": "bjensen",
  "realm": "/alpha",
  "idletime": 0,
  "maxidletime": 30,
  "maxsessiontime": 120,
  "maxtime": 6171
}
```

On success, AM resets the idle time for the server-side session, and returns timeout details of the authenticated session.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | * Resetting a server-side session's idle time triggers a write operation to the CTS token store. To avoid the overhead of write operations to the token store, use the `refresh` action *only* if you want to reset a server-side session's idle time.

* The idle time of a session is reset subject to the [latest access time update frequency](../setup/services-configuration.html#latest-access-time-update-frequency). AM updates a session's latest access time at most this often. The default is 60 seconds.

* AM doesn't monitor idle time for client-side sessions, so you can't use the `tokenId` of a client-side session to refresh the session's idle time. |

## Invalidate sessions

To invalidate an authenticated session, send an HTTP POST request to the `/json/sessions/` endpoint with the `logout` action. This action invalidates the session token provided in the `iPlanetDirectoryPro` header by default:

```bash
$ curl \
--request POST \
--header "Content-type: application/json" \
--header "iPlanetDirectoryPro: AQICS…​NzEz*" \
--header "Accept-API-Version: resource=3.1, protocol=1.0" \
'https://am.example.com:8443/am/json/realms/root/realms/alpha/sessions/?_action=logout'
{
     "result": "Successfully logged out"
 }
```

On success, AM invalidates the authenticated session and returns a success message.

If the token isn't valid and can't be invalidated, an error message is returned:

```json
{
  "result": "Token has expired"
}
```

An administrative user can invalidate the session of another authenticated user by providing the session token as the value of the `tokenId` query parameter.

This example shows an administrative user passing their session token in the `iPlanetDirectoryPro` header and invalidating bjensen's session by passing her session token in the `tokenId` parameter:

```bash
$ curl \
--request POST \
--header "Content-type: application/json" \
--header "iPlanetDirectoryPro: AQICS…​NzEz*" \
--header "Accept-API-Version: resource=3.1, protocol=1.0" \
--data '{ "tokenId": "BXCCq…​NX*1*" }' \
'https://am.example.com:8443/am/json/realms/root/sessions/?_action=logout'
 {
     "result": "Successfully logged out"
 }
```

### Invalidate specific sessions

To invalidate specific authenticated sessions for a user, first obtain a list of the user's active sessions. Send an HTTP GET request to the `/json/sessions/` endpoint, using the SSO token of an administrative user, such as `amAdmin` as the value of the `iPlanetDirectoryPro` header.

Use a `queryFilter` to specify the name of the user and the realm to search.

For example, to obtain the list of active sessions for `bjensen` in the `alpha` realm, the query filter value would be:

```
username eq "bjensen" and realm eq "/alpha"
```

|   |                                                                                                                                                                   |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The query filter value must be URL-encoded when sent over HTTP.Learn more about query filter parameters in [Query](../am-rest/rest-intro.html#about-crest-query). |

In the following example, there are two authenticated sessions. Note the value of the `sessionHandle` properties.

```bash
$ curl \
--request GET \
--header "iPlanetDirectoryPro: AQICS…​NzEz*" \
--header "Accept-API-Version: resource=3.1, protocol=1.0" \
'https://am.example.com:8443/am/json/realms/root/realms/alpha/sessions?_queryFilter=username%20eq%20%22bjensen%22%20and%20realm%20eq%20%22%2Falpha%22'
{
  "result": [
    {
      "username": "bjensen",
      "universalId": "id=bjensen,ou=user,o=alpha,ou=services,dc=am,dc=example,dc=com",
      "realm": "/alpha",
      "sessionHandle": "shandle:ITnOR5S…​AA.",
      "latestAccessTime": "2022-11-11T09:32:28.265Z",
      "maxIdleExpirationTime": "2022-11-11T10:02:28Z",
      "maxSessionExpirationTime": "2022-11-11T11:32:28Z"
    },
    {
      "username": "bjensen",
      "universalId": "id=bjensen,ou=user,o=alpha,ou=services,dc=am,dc=example,dc=com",
      "realm": "/alpha",
      "sessionHandle": "shandle:JfMui6O…​AA.",
      "latestAccessTime": "2022-11-11T09:32:24.395Z",
      "maxIdleExpirationTime": "2022-11-11T10:02:24Z",
      "maxSessionExpirationTime": "2022-11-11T11:32:24Z"
    }
  ],
  "resultCount": 2,
  "pagedResultsCookie": null,
  "totalPagedResultsPolicy": "NONE",
  "totalPagedResults": -1,
  "remainingPagedResults": -1
}
```

To log out specific sessions, send an HTTP POST request to the `/json/sessions/` endpoint, with the `logoutByHandle` action. Include an array of the session handles to invalidate as values of the `sessionHandles` property in the POST body.

Use the SSO token of an administrative user, such as `amAdmin`, as the value of the `iPlanetDirectoryPro` header.

This example invalidates the sessions returned by the previous query:

```bash
$ curl \
--request POST \
--header "Content-Type: application/json" \
--header "iPlanetDirectoryPro: AQICS…​NzEz*" \
--header "Accept-API-Version: resource=3.1, protocol=1.0" \
--data '{
    "sessionHandles": [
        "shandle:ITnOR5S…​AA.",
        "shandle:JfMui6O…​AA."
    ]
}' \
'https://am.example.com:8443/am/json/realms/root/realms/alpha/sessions/?_action=logoutByHandle'
{
  "result": {
    "shandle:ITnOR5S…​AAA.": true,
    "shandle:JfMui6O…​AA.": true
  }
}
```

### Invalidate all sessions for a user

To invalidate (log out) all authenticated sessions for a user, send an HTTP POST request to the `/json/sessions/` endpoint with the `logoutByUser` action, specifying the username in the request payload.

Provide the session token of an *administrative user* in the `iPlanetDirectoryPro` header. Users can invalidate their own sessions by providing their session token in the `iPlanetDirectoryPro` header and their username in the body of the request.

This example logs out all bjensen's sessions:

```bash
$ curl \
--request POST \
--header "Content-Type: application/json" \
--header "iPlanetDirectoryPro: AQICS…​NzEz*" \
--header "Accept-API-Version: resource=5.1, protocol=1.0" \
--data '{"username": "bjensen"}' \
'https://am.example.com:8443/am/json/realms/root/sessions/?_action=logoutByUser'
{
  "result": true
}
```

Session invalidation by user works slightly differently for server-side and client-side sessions.

* Server-side sessions

  Logout by user simply deletes all authenticated sessions for that user. This action creates an `AM-SESSION-LOGGED-OUT` event in the activity log and an `AM-LOGOUT` event in the authentication log, as with any other session termination.

* Client-side sessions

  When the user logs out, a *logout token* is created. If there is only one AM instance in the site, the logout token is added to a local cache of that AM instance. If there are multiple AM instances in the site, the other instances poll the CTS a specified interval to update their logout token cache. Learn more in the [Enable Invalidation of Sessions Based on User Identifier](../setup/services-configuration.html#global-session-client-side-logout) property.

  An `AM-LOGOUT-USER-TOKEN` event is created in the activity log when the user is logged out. The action is `CREATE` or `UPDATE` depending on whether a token for the user being logged out already exists. The `userId` component of this audit entry is that of the caller, not of the target. For example, if an administrative user logs out another user, the `userId` is that of the administrative user, not that of the user being logged out. The `objectId` indicates the target of the operation.

  A `DELETE` event is audited when the logout token expires and is deleted from the CTS.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | - Logout by user is called on a specific realm. If the same user has existing sessions in multiple realms, you must perform the action in each realm to invalidate *all* sessions for that user.

- Logout by user is disabled for client-side sessions by default. To let administrators invalidate all *client-side* sessions for a specific user, set Enable Invalidation of Sessions Based on User Identifier to `true` in the [client-side session properties](../setup/services-configuration.html#global-session-client-based-sessions) before you perform the action. |

## Get and set session properties

Use the REST API to read and update properties on authenticated sessions. Define the properties you want to set in the session property allowlist service configuration. Find information on allowlisting session properties in the [Session Property Whitelist service](../setup/services-configuration.html#global-amsessionpropertywhitelist).

You can use the REST API to:

* Get the names of the properties that you can read or update. This is the same set of properties configured in the Session Property Whitelist service.

* Read and update property values.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The ability to set, change and delete session properties is affected by the *session state*:* For server-side sessions, you can manipulate session properties at any time during the session's lifetime.

* For client-side sessions, you can manipulate session properties only during the authentication process, before the user receives the session token from AM. For example, you can set or delete properties on a client-side session from within a post-authentication plugin. |

Differentiate the user who performs the operation from the session affected by the operation as follows:

* Specify the session token of the user performing the operation on session properties in the `iPlanetDirectoryPro` header.

* Specify the session token of the user whose session is to be read or modified as the `tokenId` parameter in the body of the REST API call.

* Omit the `tokenId` parameter from the body of the REST API call if the session of the user performing the operation is the same session that you want to read or modify.

The following examples assume that you configured a property named `LoginLocation` in the Session Property Whitelist service.

To retrieve the names and values of the properties you can get or set, send an HTTP POST request to the `json/sessions` endpoint, with the `getSessionProperties` action:

```bash
$ curl \
--request POST \
--header "Content-type: application/json" \
--header "iPlanetDirectoryPro: AQICS…​NzEz*" \
--header "Accept-API-Version: resource=3.1, protocol=1.0" \
--data '{ "tokenId": "BXCCq…​NX*1*" }' \
'https://am.example.com:8443/am/json/realms/root/sessions/?_action=getSessionProperties'
{
    "LoginLocation": ""
}
```

To set the value of a session property, send an HTTP POST request to the `/json/sessions/` endpoint, with the `updateSessionProperties` action. If you do not specify a `tokenId` parameter in the request body, the operation affects the session specified in the `iPlanetDirectoryPro` header:

```bash
$ curl \
--request POST \
--header "Content-Type: application/json" \
--header "iPlanetDirectoryPro: AQICS…​NzEz*" \
--header "Accept-API-Version: resource=3.1, protocol=1.0" \
--data '{"LoginLocation":"40.748440, -73.984559"}' \
'https://am.example.com:8443/am/json/realms/root/sessions/?_action=updateSessionProperties'
{
    "LoginLocation": "40.748440, -73.984559"
}
```

To set multiple properties in a single REST API call, specify the list of properties and their values in the JSON payload; for example:

```
--data '{"property1":"value1", "property2":"value2"}'
```

To set the value of a session property on another user's session, specify the session token of the user performing the action in the `iPlanetDirectoryPro` header and the session token to be modified as the value of the `tokenId`:

```bash
$ curl \
--request POST \
--header "Content-Type: application/json" \
--header "iPlanetDirectoryPro: AQICS…​NzEz*" \
--header "Accept-API-Version: resource=3.1, protocol=1.0" \
--data '{"LoginLocation": "40.748440, -73.984559", "tokenId": "BXCCq…​NX*1*"}' \
'https://am.example.com:8443/am/json/realms/root/sessions/?_action=updateSessionProperties'
{
    "LoginLocation": "40.748440, -73.984559"
}
```

If the user attempting to modify the session doesn't have sufficient access privileges, the preceding examples result in a 403 Forbidden error.

You can't set properties internal to AM sessions. If you try to modify an internal property in a REST API call, AM also returns a 403 Forbidden error; for example:

```bash
$ curl \
--request POST \
--header "Content-Type: application/json" \
--header "iPlanetDirectoryPro: AQICS…​NzEz*" \
--header "Accept-API-Version: resource=3.1, protocol=1.0" \
--data '{"AuthLevel":"5", "tokenId": "BXCCq…​NX*1*"}' \
'https://am.example.com:8443/am/json/realms/root/sessions/?_action=updateSessionProperties'
{
    "code": 403,
    "reason": "Forbidden",
    "message": "Forbidden"
}
```

Find a list of the default session properties in [Session properties](../am-authentication/auth-tree-webhooks.html#session-properties).

---

---
title: Server-side sessions
description: Store server-side sessions in the CTS token store and cache them in PingAM server memory to improve performance and support all authentication features
component: pingam
version: 8.1
page_id: pingam:am-sessions:cts-based-sessions
canonical_url: https://docs.pingidentity.com/pingam/8.1/am-sessions/cts-based-sessions.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Sessions", "Authentication", "CTS Store (Sessions &amp; Tokens)", "Storage"]
page_aliases: ["sessions-guide:cts-based-sessions.adoc"]
section_ids:
  advantages_of_server_side_sessions: Advantages of server-side sessions
  server_side_journey_sessions: Server-side journey sessions
  server_side_authenticated_sessions: Server-side authenticated sessions
---

# Server-side sessions

Server-side sessions reside in the CTS token store and can be cached in memory on one or more AM servers to improve system performance.

|   |                                                                                                                   |
| - | ----------------------------------------------------------------------------------------------------------------- |
|   | Find information about configuring AM with sticky load balancing in [Load balancing](../setup/configure-lb.html). |

If the session request is redirected to an AM server that doesn't have the session cached, that server must retrieve the session from the CTS token store.

AM stores server-side sessions in the CTS token store and caches sessions in server memory. If a server with cached sessions fails, or if the load balancer in front of AM servers directs a request to a server that doesn't have the session cached, the AM server retrieves the session from the CTS token store, incurring performance overhead.

AM sends a reference to the session to the client, but the reference doesn't contain any of the session state information. AM can modify a session during its lifetime without changing the client's reference to the session.

## Advantages of server-side sessions

* Full feature support

  Server-side sessions support all AM features, such as CDSSO and quotas. Client-side sessions don't. Learn more in [Limitations of client-side sessions](client-based-sessions.html#session-state-client-based-limitations).

  |   |                                                                                             |
  | - | ------------------------------------------------------------------------------------------- |
  |   | This advantage doesn't apply to journey sessions because they don't provide these features. |

* Session information isn't resident in browser cookies

  With both server-side journey sessions and authenticated sessions, all the information about the session resides in the CTS and could be cached on one or more AM servers. With client-side authenticated sessions, session information is held in browser cookies. This information could be very long-lived.

## Server-side journey sessions

While progressing through the authentication tree, the session reference is returned to the client after a call to the `authenticate` endpoint and stored in the `authId` object of the JSON response.

AM maintains the journey session in the CTS token store. After the journey has completed, AM returns session state to the client and deletes the server-side authenticated session if the realm to which the user has authenticated is configured for client-side authenticated sessions.

Journey session allowlisting is an optional feature that maintains a list of in-progress journey sessions and their progress in the journey to protect against replay attacks. Learn more in [Journey session allowlisting](../security/auth-session-whitelist.html).

## Server-side authenticated sessions

Once the user is authenticated, the session reference is known as an *SSO token*. For browser clients, AM sets a cookie in the browser that contains the session reference. For REST clients, AM returns the session reference in response to calls to the `authentication` endpoint.

Learn more in [Session cookies and session security](session-state-cookies.html).

Related information: [Choose where to store sessions](session-state-use-cases.html)

---

---
title: Session cookies and session security
description: Understand how PingAM session cookies work, their structure for client-side and server-side sessions, and configure security measures against hijacking and tampering
component: pingam
version: 8.1
page_id: pingam:am-sessions:session-state-cookies
canonical_url: https://docs.pingidentity.com/pingam/8.1/am-sessions/session-state-cookies.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Sessions", "Cookie", "Security"]
page_aliases: ["sessions-guide:session-state-cookies.adoc"]
---

# Session cookies and session security

Authenticated sessions require the user or client to be able to hold on to cookies. Cookies provided by AM's Session Service can contain a JSON Web Token (JWT) with the session or just a reference to where the session is stored.

AM issues a cookie to the user or entity regardless of the session location for client-side and server-side sessions. By default, the cookie's name is `iPlanetDirectoryPro`. For authenticated sessions stored in the CTS token store, the cookie contains a reference to the session in the CTS token store and several other pieces of information. For authenticated sessions stored on the client, the `iPlanetDirectoryPro` cookie contains all the information that would be held in the CTS token store.

Client-side session cookies consist of two parts: The first part of the cookie is identical to the cookie used by server-side sessions, which ensures the compatibility of the cookies regardless of the session location. The second part is a JSON Web Token (JWT), which contains session information, as illustrated below:

* `iPlanetDirectoryPro` cookie for server-side authenticated sessions:

  ```none
  AQIC...sswo.*AAJ...MA..*
  ```

* `iPlanetDirectoryPro` cookie for client-side authenticated sessions:

  ```none
  AQIC...sswo.*AAJ...MA..*ey....................................fQ.
  ```

Note that the examples are not to scale. The size of the client-side session cookie increases when you customize AM to store additional attributes in users' sessions. You're responsible for ensuring the size of the cookie doesn't exceed the maximum cookie size allowed by your end users' browsers.

Since the session cookie is either a pointer to the authenticated session or the actual session itself, you must configure AM to secure the session cookie against hijacking, session tampering, and other security concerns.

For example, terminating a session effectively logs the user or entity out of all realms, but the way AM terminates sessions has security implications depending on where AM stores the sessions. You can also configure the session time-to-live, idle timeout, the number of concurrent sessions for a user, and others.

Related information:

* [Secure sessions](../security/securing-sessions.html)

* [Secure session cookies](../security/securing-cookies.html)

* [What information is contained in the AM session cookie?](https://support.pingidentity.com/s/article/FAQ-Cookies-in-PingAM#sessioncookieinfo)

---

---
title: Session termination
description: AM manages active sessions, allowing single sign-on when authenticated users attempt to access system resources in AM's control.
component: pingam
version: 8.1
page_id: pingam:am-sessions:session-state-session-termination
canonical_url: https://docs.pingidentity.com/pingam/8.1/am-sessions/session-state-session-termination.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
page_aliases: ["sessions-guide:session-state-session-termination.adoc"]
section_ids:
  auth-session-termination-config: Configure authenticated session timeout settings
  enable-dynamic-session-realm: Enable dynamic session attributes for the realm
  session-max-timeout: Set maximum session time-to-live
  session-idle-timeout: Set maximum session idle timeout
  session-state-configure-denylist: Configure client-side session denylisting
---

# Session termination

AM manages active sessions, allowing single sign-on when authenticated users attempt to access system resources in AM's control.

Authenticated sessions are terminated when a configured timeout is reached or when a user performs actions that cause session termination. Session termination effectively logs the user out of all systems protected by AM.

With server-side authenticated sessions, AM terminates sessions in four situations:

* When a user explicitly logs out.

* When an administrator monitoring sessions explicitly terminates an authenticated session.

* When an authenticated session exceeds the maximum time-to-live.

* When a user is idle for longer than the maximum session idle time.

Under these circumstances, AM responds by removing server-side authenticated sessions from the CTS token store and from AM server memory caches. With the authenticated session no longer present in CTS, AM forces the user to reauthenticate during subsequent attempts to access protected resources.

When a user explicitly logs out of AM, AM also attempts to invalidate the `iPlanetDirectoryPro` cookie in users' browsers by sending a `Set-Cookie` header with an invalid session ID and a cookie expiration time that's in the past. In the case of administrator session termination and session timeout, AM can't invalidate the `iPlanetDirectoryPro` cookie until the next time the user accesses AM.

Session termination differs for client-side authenticated sessions. Since client-side authenticated sessions aren't maintained in the CTS token store, administrators can't monitor or terminate them. Because AM doesn't modify the `iPlanetDirectoryPro` cookie for client-side sessions after authentication, the session idle time isn't maintained in the cookie. Therefore, AM doesn't automatically terminate client-side authenticated sessions that have exceeded the idle timeout.

Find information about tracking idle time in PingGateway in [AmSessionIdleTimeoutFilter](https://docs.pingidentity.com/pinggateway/2025.11/reference/AmSessionIdleTimeoutFilter.html).

As with server-side authenticated sessions, AM attempts to invalidate the `iPlanetDirectoryPro` cookie from a user's browser when the user logs out. When the maximum session time is exceeded, AM also attempts to invalidate the `iPlanetDirectoryPro` cookie in the user's browser the next time the user accesses AM.

It's important to understand that AM can't guarantee cookie invalidation. For example, the HTTP response containing the `Set-Cookie` header might be lost. This isn't an issue for server-side sessions, because a logged-out session no longer exists in the CTS token store, and a user who attempts to access AM after previously logging out will be forced to reauthenticate.

However, without the guarantee of cookie invalidation, deployments with client-side sessions can experience issues. For example, a logged-out user could still have an `iPlanetDirectoryPro` cookie but AM wouldn't know they had logged out. Therefore, AM supports a feature that takes additional action when users log out of client-side sessions. AM can maintain a list of logged out client-side sessions in a session denylist in the CTS token store. Whenever users attempt to access AM with client-side sessions, AM checks the session denylist to validate that the user has not, in fact, logged out.

Because AM doesn't modify client-side session cookies after they're stored in the end user's browser, and client-side sessions contain the session maximum time-to-live, you must protect them against tampering. Learn more in [Client-side session security](../security/session-state-configure-cookie-security.html).

## Configure authenticated session timeout settings

Session timeout settings (`maximum session time` and `maximum idle time`) can be set in different locations to provide greater control over terminating authenticated sessions.

AM determines which settings to apply to the authenticated session in the following order of precedence:

1. The session timeout settings for a user.

   Go to Realms > *realm name* > Identities > *username* > Services > Session to set user level session timeout values.

   If the `Session` service isn't listed, click Add Service and select `Session` in the list.

2. The session timeout settings in a node:

   * Configure session timeout settings in the [Set Session Properties node](https://docs.pingidentity.com/auth-node-ref/8.1/set-session-properties.html).

   * Configure session timeout settings in the [Scripted Decision node](https://docs.pingidentity.com/auth-node-ref/8.1/scripted-decision.html) using the `withMaxIdleTime` and `withMaxSessionTime` methods.

     Learn more in [Set authenticated session timeouts](../am-scripting/scripting-api-node.html#scripting-api-node-session-timeouts).

   If a tree has multiple nodes that set session timeouts, AM uses the settings associated with the last executed node to determine the timeouts for the resulting authenticated session.

   If an inner tree includes nodes that set session timeouts, AM uses the updated timeouts in the parent tree.

3. The session timeout settings for an authentication tree.

   Set the `maximumSessionTime` and `maximumIdleTime` properties in the tree configuration.

   Session timeout values set on an inner tree are ignored.

   Learn more in [Configure authenticated session timeouts in a tree](../am-authentication/configure-auth-trees.html#configure-auth-session-timeouts-tree).

4. The session timeout values set in the realm.

   Enable the Session service in the realm to set realm level session timeout values.

   Learn more in [Enable dynamic session attributes for the realm](#enable-dynamic-session-realm).

5. The session timeout values set globally for the AM site.

   The default maximum session timeout is `120` minutes and the default maximum idle time is `30` minutes.

   Go to Configure > Sessions > Dynamic Attributes to change the default session timeout values.

   Learn more in [Dynamic attributes](../setup/services-configuration.html#global-session-dynamic-attributes).

### Enable dynamic session attributes for the realm

To configure the session termination settings for a particular realm, enable the Session service:

1. In the AM admin UI, go to Realms > *realm name* > Services.

2. Check if the `Session` service appears in the list of services configured for the realm.

   If it doesn't, click Add a Service and select `Session` in the list.

   The Session page appears, showing the Dynamic Attributes tab.

3. Click Save Changes.

Learn more in [Dynamic attributes](../setup/services-configuration.html#global-session-dynamic-attributes).

### Set maximum session time-to-live

When configuring the maximum session time-to-live (TTL), you must balance security and user experience. Depending on your application, it could be acceptable for your users to log in once a month. Financial applications, for example, tend to expire their sessions in less than an hour.

The longer an authenticated session is valid, the larger the window during which a malicious user could impersonate a user if they were able to hijack a session cookie.

The maximum session time-to-live is `120` minutes by default.

The following steps configure the maximum session time in a realm, but you can also [configure](#auth-session-termination-config) it for a user, in a node, in a tree or globally:

1. In the AM admin UI, go to Realms > *realm name* > Services > Session > Dynamic Attributes.

2. In the Maximum Session Time field, set a value suitable for your environment.

3. Save your changes.

If you update the maximum session TTL, consider reviewing the expiry time for OAuth 2.0 JWTs according to your business needs. It may be convenient to set them to the same value, but there are times when these values need to be different.

1. To update the JWT lifetime for individual OIDC clients:

   1. In the AM admin UI, go to Realms > *realm name* > Applications > OAuth 2.0 > Clients > *client ID* > OpenID Connect.

   2. Set OpenID Connect JWT Token Lifetime (seconds) to the same duration as the maximum session TTL (minutes).

      This value overrides the JWT lifetime set for the OAuth 2.0 provider.

2. To update the JWT lifetime for the OAuth2 Provider service:

   1. In the AM admin UI, go to Realms > *realm name* > Services > OAuth2 Provider > OpenID Connect.

   2. Set OpenID Connect JWT Token Lifetime (seconds) to the same duration as the maximum session TTL (minutes).

### Set maximum session idle timeout

Consider a user with a valid authenticated session navigating through pages or making changes to the configuration. If for any reason they leave their desk and their computer remains open, a malicious user could take the opportunity to impersonate them.

Session idle timeout can help mitigate those situations by logging out users after a specified duration of inactivity.

The maximum session idle timeout is `30` minutes by default.

|   |                                                                                                                                    |
| - | ---------------------------------------------------------------------------------------------------------------------------------- |
|   | You can only use session idle timeout in realms configured for [server-side sessions](cts-based-sessions.html#cts-based-sessions). |

The following steps configure the maximum idle time in a realm, but you can also [configure](#auth-session-termination-config) it for a user, in a node, in a tree or globally:

1. In the AM admin UI, go to Realms > *realm name* > Services > Session > Dynamic Attributes.

2. On the Maximum Idle Time property, configure a value suitable for your environment.

3. Save your changes.

## Configure client-side session denylisting

Session denylisting makes sure users who have logged out of client-side sessions can't achieve single sign-on without reauthenticating to AM. Session denylisting doesn't apply to journey sessions.

1. Make sure you deployed the Core Token Service (CTS) during AM installation.

   The session denylist is stored in the CTS token store.

2. Go to Configure > Global Services, click Session, and locate the Client-Side Sessions tab.

3. Select the Enable Session Denylisting option to enable session denylisting for client-side authenticated sessions.

   When you configure one or more AM realms for client-side sessions, you should enable session denylisting to track session logouts across multiple AM servers.

   Changing the value of this property takes effect immediately.

4. Configure the Session Denylist Cache Size property.

   AM maintains a cache of logged-out client-side authenticated sessions. The cache size should be approximately equal to the number of logouts expected during the maximum session time.

   Increase the default value of 10,000 if the expected number of logouts during this period is significantly higher. If the session denylist cache is too small, AM reads denylist entries from the CTS token store instead of getting them from cache, which can lead to a small reduction in performance.

   Changing the value of this property takes effect immediately.

5. Configure the Denylist Poll Interval property.

   AM polls the Core Token service for changes to logged-out sessions if session denylisting is enabled. By default, the polling interval is 10 seconds.

   The longer the polling interval, the more time a malicious user has to connect to other AM servers in a cluster and make use of a stolen session cookie. Shortening the polling interval improves the security for logged out sessions, but could reduce AM performance due to increased network activity.

   Changing the value of this property doesn't take effect until you restart AM.

6. Configure the Denylist Purge Delay property.

   When session denylisting is enabled, AM tracks each logged-out session for the maximum session time plus the denylist purge delay. For example, if a session has a maximum time of 120 minutes and the denylist purge delay is one minute, AM tracks the session for 121 minutes. Increase the denylist purge delay if you expect system clock skews in a cluster of AM servers to be greater than one minute. There is no need to increase the denylist purge delay for servers running a clock synchronization protocol, such as Network Time Protocol.

   Changing the value of this property doesn't take effect until you restart AM.

7. Click Save Changes.

   |   |                                                                                                                                                                                               |
   | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | Enabling or disabling the session denylist, or altering the cache size, takes effect immediately.Changes to any other session denylist properties **don't** take effect until you restart AM. |

Find detailed information about session service attributes in [session configuration](../setup/services-configuration.html#global-session).

---

---
title: Session upgrade
description: Configure session upgrade to allow authenticated users to provide additional credentials and access sensitive resources
component: pingam
version: 8.1
page_id: pingam:am-sessions:session-upgrade
canonical_url: https://docs.pingidentity.com/pingam/8.1/am-sessions/session-upgrade.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Sessions", "Authentication", "Step-up Authentication", "Configuration", "REST API"]
page_aliases: ["sessions-guide:session-upgrade.adoc"]
section_ids:
  what_triggers_a_session_upgrade: What triggers a session upgrade?
  session_upgrade_outcomes: Session upgrade outcomes
  session-upgrade-prerequisites: Session upgrade prerequisites
  proc-session-upgrade-configuration: Configure AM for session upgrade
  proc-session-upgrade-browser: Perform session upgrade with a browser
  proc-session-upgrade-REST: Perform session upgrade over REST
---

# Session upgrade

Authenticated sessions can be upgraded to provide access to sensitive resources.

Consider a website for a university. Some resources, such as courses and degree catalogs, are free for anyone to access and don't need to be protected. The university also provides the students with a portal they can use to access their grades. This portal is protected with a policy that requires users to authenticate. To pay tuition, students are required to present additional credentials to increase their authentication level and gain access to these functions.

Allowing authenticated users to provide additional credentials to access sensitive resources is called session upgrade. Session upgrade is AM's mechanism to perform step-up authentication.

## What triggers a session upgrade?

Session upgrade is triggered in the following situations:

* An authenticated user is redirected to a URL that has the `ForceAuth` parameter set to `true` for the same authentication tree that was used to create the current session.

  For example, `https://am.example.com:8443/am/XUI/?realm=/alpha&ForceAuth=true#login`

  In this case, the user is asked to reauthenticate to the default authentication tree in the `alpha` realm even if the current session already satisfies the authentication requirements.

  When a new authenticated session is created, the old authenticated session should no longer be valid. For client-side sessions, invalidating the old session depends on the value of the [Enable Session Denylisting](session-state-session-termination.html#session-state-configure-denylist) configuration option:

  * If this option is `false` (default), both the old and new authenticated sessions are considered valid after the session upgrade.

  * If this option is `true`, the old authenticated session is no longer valid

* An authenticated user is redirected to a different authentication tree than the one that created their current session.

  For example, the user authenticated through the `Login` tree and later is sent to a URL that specifies a different tree:

  `https://am.example.com:8443/am/XUI/?realm=/alpha&service=StepUpMFA#login`

  In this case, AM upgrades the session if the existing authentication doesn't meet the new tree's requirements. You don't need to set `ForceAuth=true` when moving the user to a different tree because the change of tree itself triggers session upgrade.

* An authenticated user tries to access a resource protected by a web or Java agent, or a custom policy enforcement point (PEP).

  In this case, AM sends the agent or PEP an *advice* that the user must perform one of the following actions:

  * Authenticate at an authentication level greater than the current level

  * Authenticate using a specific tree

  The session upgrade flow during policy evaluation is as follows:

  1. An authenticated user tries to access a resource.

  2. The PEP, for example a web or Java agent, sends the request to AM for an authorization decision.

  3. AM returns an authorization decision that denies access to the resource, and returns an *advice* indicating that the user must present additional credentials to access the resource.

  4. The policy enforcement point sends the user back to AM for session upgrade.

  5. The user provides additional credentials. For example, they might provide a one-time password, swipe their phone screen, or use face recognition.

  6. AM authenticates the user.

  7. The user can now access the sensitive resource.

## Session upgrade outcomes

The following outcomes can result from a session upgrade:

* Successful

  AM performs one of the following actions depending on the type of authenticated session configured for the realm:

  * If the realm is configured for server-side authenticated sessions, the resulting action depends on the mechanism used to perform session upgrade:

    * When using the `ForceAuth` parameter, AM issues new session tokens to users on reauthentication, even if the current authenticated session already meets the security requirements.

    * When using *advices*, AM copies the session properties to a new authenticated session and hands the client a new session token to replace the original one. The new authenticated session reflects the successful authentication to a higher level.

  * If the realm is configured for client-side authenticated sessions, AM hands the client a new session token to replace the original one. The new authenticated session reflects the successful authentication to a higher level.

* Unsuccessful

  AM leaves the authenticated session as it was before the attempt at stronger authentication.

  If session upgrade fails because the login page times out, AM redirects the user's browser to the success URL from the last successful authentication.

|   |                                                                                                                                                                                             |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Anonymous sessions can be upgraded to non-anonymous sessions by using the [Anonymous Session Upgrade node](https://docs.pingidentity.com/auth-node-ref/8.1/anonymous-session-upgrade.html). |

## Session upgrade prerequisites

* Configure a PEP, for example, a web or Java agent, that enforces AM policies on a website or application.

  AM web and Java agents handle session upgrade without additional configuration because the agents are built to handle AM's advices. If you build your own PEPs, you must take advices and session upgrade into consideration.

  Learn more in the [Web Agents](https://docs.pingidentity.com/web-agents/2025.3) and [Java Agents](https://docs.pingidentity.com/java-agents/2025.3) documentation, and in [Request policy decisions over REST](../am-authorization/rest-api-authz-policy-decisions.html) (For RESTful PEPs).

* Configure an authorization policy to protect a resource protected by the Java or web agent, or a RESTful PEP.

  The following example policy allows GET and POST access to the `*://*:*/sample/*` resource to any authenticated user:

  ![Only authenticated users can access the resource](_images/pre-session-upgrade-config.png)

|   |                                                                                                                                                                                                                                                                                                                                                                       |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | To track an authenticated session through a session upgrade, enable the [cross-upgrade session reference property](../setup/services-configuration.html#global-session-xusref), which retains its value throughout the session lifecycle. Enabling this property ensures the session reference is recorded in the [audit logs](../monitoring/audit-logging-ref.html). |

## Configure AM for session upgrade

1. Configure an authentication tree that validates a user's credentials during session upgrade.

   No additional configuration is required to perform session upgrade.

   |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
   |   | Because session upgrade is a mechanism that can be used to grant users access to sensitive information, consider configuring a strong authentication method such as [multi-factor authentication (MFA)](../am-authentication/authn-introduction-authn.html#about-mfa). Also consider session lifetime in your environment. For example, if users should only have access to the protected resource to perform an operation, such as checking the balance of an account, consider implementing [transactional authorization](../am-authorization/transactional-authorization.html) instead. |

2. Configure at least one of the following environment conditions in the authentication policy that you created as part of the [prerequisites](#session-upgrade-prerequisites):

   * Authentication level (greater than or equal to)

     Use this condition to present a list of authentication trees that provide a greater or equal authentication level to the one specified in the condition. The user can choose a tree if more than one tree meets the criteria of the condition.

     The following policy requires an authentication tree that provides an authentication level of 3 or greater:

     ![Session upgrade authentication by authentication level environment condition](_images/session-upgrade-auth-level.png)

   - Authentication by service

     Use this condition to specify the authentication tree the user must authenticate through. For example, the following policy requires the user to sign on using the `Example` tree:

     ![Session upgrade authentication by service environment condition](_images/session-upgrade-service.png)

     Authentication tree names are case-sensitive.

   You can find more information about configuring policies and environment conditions in [Policies](../am-authorization/policies.html).

3. Test session upgrade using a browser or REST:

   * [Perform session upgrade with a browser](#proc-session-upgrade-browser)

   * [Perform session upgrade over REST](#proc-session-upgrade-REST)

## Perform session upgrade with a browser

To upgrade an authenticated session using a browser, perform the following steps:

1. Ensure you have performed the tasks in [Session upgrade prerequisites](#session-upgrade-prerequisites) and [Configure AM for session upgrade](#proc-session-upgrade-configuration).

2. In a browser, go to your protected resource.

   For example, `http://www.example.com:9090/sample`.

   The agent redirects the browser to the AM login screen.

3. Sign on to AM as the user that should access the resource. For example, sign on as `bjensen`.

   AM requires additional credentials to grant access to the resource. For example, if you set the policy environment condition to `Authentication by Service` and `Example`, you will be required to sign on again as `bjensen`.

4. Authenticate as `bjensen`.

   Providing credentials for a different user will fail.

   You can now access the protected resource.

## Perform session upgrade over REST

To upgrade an authenticated session using REST, perform the following steps:

1. Ensure you have performed the tasks in [Session upgrade prerequisites](#session-upgrade-prerequisites) and [Configure AM for session upgrade](#proc-session-upgrade-configuration).

2. Sign on as an administrative user that has permission to evaluate policies, such as `amAdmin`.

   For example:

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

   |   |                                                                                                                                                |
   | - | ---------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | You can also [assign privileges to a user to evaluate policies](../am-authorization/scripted-policy-condition.html#scripted-policy-privilege). |

3. Sign on as the user that should access the resources.

   For example, sign on as `bjensen`:

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

4. Request a policy decision from AM for a protected resource, in this case, `https://am.example.com:9090/sample`.

   The `iPlanetDirectoryPro` header sets the SSO token for the administrative user, and the `subject` element of the payload sets the SSO token for `bjensen`.

   > **Collapse: Example**
   >
   > ```bash
   > $ curl --request POST \
   >  --header "Content-Type: application/json" \
   >  --header "iPlanetDirectoryPro: AQIC5wM2…​" \
   >  --header "Accept-API-Version:protocol=1.0,resource=2.1" \
   >  --data '{
   >  "resources": [
   >      "http://www.example.com:9090/sample"
   >  ],
   >  "application": "iPlanetAMWebAgentService",
   >  "subject": { "ssoToken": "AQIC5wM…​TU3OQ*"}
   > }' \
   > "https://am.example.com:8443/am/json/realms/root/realms/alpha/policies?_action=evaluate"
   > [
   >    {
   >       "resource":"http://www.example.com:9090/sample",
   >       "actions":{
   >
   >       },
   >       "attributes":{
   >
   >       },
   >       "advices":{
   >          "AuthLevelConditionAdvice":[
   >             "3"
   >          ]
   >       },
   >       "ttl":9223372036854775807
   >    }
   > ]
   > ```

   AM returns an advice, which means that the user must present additional credentials to access that resource.

   You can find more information about requesting policy decisions in [Request policy decisions over REST](../am-authorization/rest-api-authz-policy-decisions.html).

5. Format the advice as XML, without spaces or line breaks.

   The following example is spaced and tabulated for readability purposes only:

   ```xml
   <Advices>
       <AttributeValuePair>
          <Attribute name="AuthLevelConditionAdvice"/>
          <Value>3</Value>
       </AttributeValuePair>
   </Advices>
   ```

   |   |                                                                                                                                                                                                                                                                                          |
   | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | The example shows the XML render of a single advice. Depending on the conditions configured in the policy, the advice may contain several lines. Learn more in [Policy decision advice](../am-authorization/rest-api-authz-policy-decisions.html#rest-api-authz-policy-decision-advice). |

6. URL-encode the XML advice.

   For example:

   ```
   %3CAdvices%3E%3CAttributeValuePair%3E%3CAttribute%20name%3D%22AuthLevelConditionAdvice%22%2F%3E%3CValue%3E3%3C%2FValue%3E%3C%2FAttributeValuePair%3E%3C%2FAdvices%3E
   ```

   Ensure there are no spaces between tags when URL-encoding the advice.

7. Call AM's `authenticate` endpoint to request information about the advice.

   Use the following details:

   * Add the following URL parameters:

     * `authIndexType=composite_advice`

     * `authIndexValue=URL-encoded-Advice`

   * Set the `iPlanetDirectoryPro` cookie as the SSO token for `bjensen`.

   > **Collapse: Example**
   >
   > ```bash
   > $ curl --request POST \
   > --header "Content-Type: application/json" \
   > --cookie "iPlanetDirectoryPro=AQIC5wM…​TU3OQ*" \
   > --header "Accept-API-Version: protocol=1.0,resource=2.1" \
   > 'https://am.example.com:8443/am/json/realms/root/realms/alpha/authenticate?authIndexType=composite_advice&authIndexValue=%3CAdvices%3E%3CAttributeValuePair%3E…​'
   > {
   >    "authId":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhdXRoSW5kZ…​",
   >    "template":"",
   >    "stage":"DataStore1",
   >    "header":"Sign in",
   >    "callbacks":[
   >       {
   >          "type":"NameCallback",
   >          "output":[
   >             {
   >                "name":"prompt",
   >                "value":"User Name:"
   >             }
   >          ],
   >          "input":[
   >             {
   >                "name":"IDToken1",
   >                "value":""
   >             }
   >          ]
   >       },
   >       {
   >          "type":"PasswordCallback",
   >          "output":[
   >             {
   >                "name":"prompt",
   >                "value":"Password:"
   >             }
   >          ],
   >          "input":[
   >             {
   >                "name":"IDToken2",
   >                "value":""
   >             }
   >          ]
   >       }
   >    ]
   > }
   > ```

   AM returns information about how the user can authenticate in a callback. In this case, providing a username and password. You can find a list of possible callbacks, and more information about the `/json/authenticate` endpoint in [Authenticate over REST](../am-authentication/authn-rest.html).

8. Call AM's `authenticate` endpoint to provide the required callback information.

   Use the following details:

   * Add the following URL query parameters:

     * `authIndexType=composite_advice`

     * `authIndexValue=URL-encoded-Advice`

   * Set the `iPlanetDirectoryPro` cookie as the SSO token for `bjensen`.

   * Send as data the complete payload AM returned in the previous step, ensuring you provide the requested callback information.

     Provide the username and password for `bjensen` in the `input` objects.

   > **Collapse: Example**
   >
   > ```bash
   > $ curl \
   >   --request POST \
   >   --header 'Content-Type: application/json' \
   >   --header "Accept-API-Version: protocol=1.0,resource=2.1" \
   >   --cookie "iPlanetDirectoryPro=AQIC5wM…​TU3OQ*" \
   >   --data '{
   >       "authId": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhdXRoSW5kZ…​",
   >       "template": "",
   >       "stage": "DataStore1",
   >       "header": "Sign in",
   >       "callbacks": [
   >         {
   >           "type": "NameCallback",
   >           "output": [
   >             {
   >               "name": "prompt",
   >               "value": "User Name:"
   >             }
   >           ],
   >           "input": [
   >             {
   >               "name": "IDToken1",
   >               "value": "bjensen"
   >             }
   >           ]
   >         },
   >         {
   >           "type": "PasswordCallback",
   >           "output": [
   >             {
   >               "name": "prompt",
   >               "value": "Password:"
   >             }
   >           ],
   >           "input": [
   >             {
   >               "name": "IDToken2",
   >               "value": "Ch4ng31t"
   >             }
   >           ]
   >         }
   >       ]
   >     }' \
   > 'https://am.example.com:8443/am/json/realms/root/realms/alpha/authenticate?authIndexType=composite_advice&authIndexValue=%3CAdvices%3E%3CAttributeValuePair%3E…​'
   > {
   >    "tokenId":"wpU01SaTq4X2x…​NDVFMAAlMxAAA.*",
   >    "successUrl":"/am/console",
   >    "realm":"/alpha"
   > }
   > ```

   AM returns a new SSO token for `bjensen`.

9. Request a new policy decision from AM for the protected resource.

   The `iPlanetDirectoryPro` header sets the SSO token for the administrative user, and the subject element of the payload sets the new SSO token for `bjensen`:

   > **Collapse: Example**
   >
   > ```bash
   > $ curl --request POST \
   > --header "Content-Type: application/json" \
   > --header "iPlanetDirectoryPro: AQIC5wM2…​" \
   > --header "Accept-API-Version:protocol=1.0,resource=2.1" \
   > --data '{
   >    "resources":[
   >       "http://www.example.com:9090/sample"
   >    ],
   >    "application":"iPlanetAMWebAgentService",
   >    "subject":{
   >       "ssoToken":"wpU01SaTq4X2x…​NDVFMAAlMxAAA.*"
   >    }
   > }' \
   > "https://am.example.com:8443/am/json/realms/root/realms/alpha/policies/policies?_action=evaluate"
   >
   > [
   >    {
   >       "resource":"http://www.example.com:9090/sample",
   >       "actions":{
   >          "POST":true,
   >          "GET":true
   >       },
   >       "attributes":{
   >
   >       },
   >       "advices":{
   >
   >       },
   >       "ttl":9223372036854775807
   >    }
   > ]
   > ```

   AM returns that `bjensen` can perform `POST` and `GET` operations on the resource.

---

---
title: Sessions
description: Manage sessions in your PingAM environment by learning session concepts, step-up authentication, session storage options, and session cookie security
component: pingam
version: 8.1
page_id: pingam:am-sessions:preface
canonical_url: https://docs.pingidentity.com/pingam/8.1/am-sessions/preface.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Sessions"]
page_aliases: ["index.adoc", "sessions-guide:preface.adoc"]
---

# Sessions

These topics cover concepts and implementation procedures to manage sessions in your AM environment.

This information is written for administrators configuring AM's authentication and authorization components.

[icon: book, set=fad, size=3x]

#### [Introduction to sessions](about-sessions.html)

Learn about the different types of sessions in AM.

[icon: cogs, set=fad, size=3x]

#### [Session upgrade](session-upgrade.html)

Discover how AM performs step-up authentication.

[icon: exchange-alt, set=fad, size=3x]

#### [Compare sessions](session-state-use-cases.html)

Decide where sessions should be stored in each realm.

[icon: user-secret, set=fad, size=3x]

#### [The session cookie](session-state-cookies.html)

Learn about the session cookie, and why you must secure it.

---

---
title: View and manage sessions
description: View and manage active server-side authenticated sessions by realm in the PingAM administrator console
component: pingam
version: 8.1
page_id: pingam:am-sessions:managing-sessions-console
canonical_url: https://docs.pingidentity.com/pingam/8.1/am-sessions/managing-sessions-console.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Sessions", "User Interface"]
page_aliases: ["sessions-guide:managing-sessions-console.adoc"]
---

# View and manage sessions

The AM admin UI lets the administrator view and manage active server-side authenticated sessions by realm by going to Realms > *realm name* > Sessions.

![The AM administrator can view and invalidate server-side sessions.](_images/session-management.png)Figure 1. Sessions Page

To search for active sessions, enter a username in the search box. AM retrieves the sessions for the user and displays them within a table. If no active server-side session is found, AM displays a session not found message.

You can end any sessions—except the current `amAdmin` user's session—by selecting it and clicking the Invalidate Selected button. As a result, the user has to authenticate again.

|   |                                                                                                                                                                                       |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Deleting a user doesn't automatically remove any of the user's server-side sessions. After deleting a user, check for any sessions for the user and remove them on the Sessions page. |

|   |                                                                                                         |
| - | ------------------------------------------------------------------------------------------------------- |
|   | Use the [REST API](../am-authentication/authn-rest.html) for advanced functionality regarding sessions. |