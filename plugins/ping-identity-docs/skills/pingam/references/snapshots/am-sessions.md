---
title: Choose where to store sessions
description: Configure PingAM to store journey and authenticated sessions server-side in the CTS token store, client-side as encrypted JWTs, or in-memory based on your deployment requirements
component: pingam
version: 8.1
page_id: pingam:am-sessions:session-state-use-cases
canonical_url: https://docs.pingidentity.com/pingam/8.1/am-sessions/session-state-use-cases.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Sessions", "Authentication", "CTS Store (Sessions &amp; Tokens)", "Cookie", "Storage"]
page_aliases: ["sessions-guide:session-state-use-cases.adoc"]
---

# Choose where to store sessions

You can configure the journey session storage location independently from the authenticated session storage location. For example, you could configure the same realm for client-side journey sessions and server-side authenticated sessions if it suits your environment.

AM stores server-side sessions in the CTS token store and caches sessions in server memory. If a server with cached sessions fails, or if the load balancer in front of AM servers directs a request to a server that doesn't have the authenticated session cached, the AM server retrieves the session from the CTS token store, incurring performance overhead.

Choosing where to store sessions is an important decision you must make by realm. Consider the information in the following tables before configuring sessions:

> **Collapse: Advantages of server-side sessions**
>
> | Advantage                                                                                                                                                                                                                                                                                                                                           | Applies to journey sessions? | Applies to authenticated sessions? |
> | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------- | ---------------------------------- |
> | **Full feature support**Server-side sessions support all AM features, such as CDSSO and quotas. Client-side sessions don't. Learn more in [Limitations of client-side sessions](impl-client-based-sessions.html#session-state-client-based-limitations).This advantage doesn't apply to journey sessions because they don't provide these features. | —                            | ✔                                  |
> | **Session information isn't resident in browser cookies**With server-side sessions, all the information about the session resides in the CTS and could be cached on one or more AM servers. With client-side sessions, session information is held in browser cookies. This information could be very long-lived.                                   | ✔                            | ✔                                  |

> **Collapse: Advantages of client-side sessions**
>
> | Advantage                                                                                                                                                                                                                                                                                                                                                                                        | Applies to journey sessions? | Applies to authenticated sessions? |
> | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------- | ---------------------------------- |
> | **Unlimited horizontal scalability for session infrastructure**Client-side sessions provides unlimited horizontal scalability for your sessions by storing the session state on the client as a signed and encrypted JWT.Overall performance on hosts using client-side sessions can be easily improved by adding more hosts to the AM deployment.                                               | ✔                            | ✔                                  |
> | **Replication-free deployments**Global deployments can struggle to keep their CTS token store replication in sync when distances are long and updates are frequent.Client-side sessions aren't constrained by the replication speed of the CTS token store. Therefore, client-side sessions are usually more suitable for deployments where a session can be serviced at any time by any server. | ✔                            | ✔                                  |

> **Collapse: Advantages of in-memory sessions**
>
> | Advantage                                                                                                                                                                                                                     | Applies to journey sessions? | Applies to authenticated sessions? |
> | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------- | ---------------------------------- |
> | **Faster performance with equivalent host**AM servers configured for in-memory journey sessions can validate more sessions per second per host than those configured for client-side or server-side journey sessions.         | ✔                            | ✖                                  |
> | **Session information isn't resident in browser cookies**Journey session information resides in AM's memory and isn't accessible to users. With client-side sessions, journey session information is held in browser cookies. | ✔                            | ✖                                  |

> **Collapse: Impact of storage location for journey sessions**
>
> |                                        | Server-side journey sessions                                                                                | Client-side journey sessions                                      | In-memory journey sessions                                      |
> | -------------------------------------- | ----------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------- | --------------------------------------------------------------- |
> | **Session location**                   | Authoritative source: CTS token store. Sessions can also be cached in AM's memory for improved performance. | On the client.                                                    | In AM server's memory.                                          |
> | **Load balancer requirements**         | None. Session stickiness recommended for performance.                                                       | None. Session stickiness recommended for performance.             | Session stickiness.                                             |
> | **Core token service usage**           | Authoritative source for authenticated sessions. Session allowlisting, when enabled.                        | Session allowlisting, when enabled.                               | None.                                                           |
> | **Uninterrupted session availability** | No special configuration required.                                                                          | No special configuration required.                                | Not available.                                                  |
> | **Session security**                   | Sessions reside in the CTS token store, and aren't accessible to users.                                     | Sessions reside on the client and should be signed and encrypted. | Sessions reside in AM's memory, and aren't accessible to users. |

> **Collapse: Impact of storage location for sessions**
>
> |                                         | Server-side Sessions                                                                                        | Client-side Sessions                                             |
> | --------------------------------------- | ----------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------- |
> | **Hardware**                            | Higher I/O and memory consumption.                                                                          | Higher CPU consumption.                                          |
> | **Logical hosts**                       | Variable or large number of hosts.                                                                          | Variable or large number of hosts.                               |
> | **Session monitoring**                  | Available.                                                                                                  | Not available.                                                   |
> | **Session location**                    | Authoritative source: CTS token store. Sessions can also be cached in AM's memory for improved performance. | In a cookie in the client.                                       |
> | **Load balancer requirements**          | None. Session stickiness recommended for performance.                                                       | None. Session stickiness recommended for performance.            |
> | **Uninterrupted session availability**  | No special configuration required.                                                                          | No special configuration required.                               |
> | **Core token service usage**            | Authoritative source for authenticated sessions.                                                            | Provides session denylisting for logged out sessions.            |
> | **Core token service demand**           | Heavier.                                                                                                    | Lighter.                                                         |
> | **Session security**                    | Sessions reside in the CTS token store, and aren't accessible to users.                                     | Sessions should be signed and encrypted.(1)                      |
> | **Cross-domain single sign-on support** | All AM capabilities supported.                                                                              | Web agents and Java agents: Supported without restricted tokens. |
>
> (1) Web agents and Java agents support either signing or encrypting client-side sessions, but not both. Learn more in [Client-side session security and agents](../security/session-state-configure-cookie-security.html#policy_agent5_client-based).
