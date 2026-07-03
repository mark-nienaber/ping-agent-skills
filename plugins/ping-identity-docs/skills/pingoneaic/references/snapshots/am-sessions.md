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
