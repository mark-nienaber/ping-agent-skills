---
title: Introduction to PingGateway
description: "Introduction to PingGateway: covers deployment patterns (reverse proxy, forward proxy, microgateway), the object model, sessions, and API descriptors"
component: pinggateway
version: 2026
page_id: pinggateway:about:preface
canonical_url: https://docs.pingidentity.com/pinggateway/2026/about/preface.html
llms_txt: https://docs.pingidentity.com/pinggateway/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2025-04-02T12:24:35Z
keywords: ["Configuration", "JSON", "Public Key Infrastructure (PKI)", "OAuth 2.0", "SAML 2.0", "Java", "Agents", "Journeys", "Data Store", "Authentication", "Nodes &amp; Trees", "Users"]
page_aliases: ["index.adoc"]
---

# Introduction to PingGateway

PingGateway uses Ping Identity Platform capabilities to protect web applications, APIs, and microservices.

[icon: lock, set=fad, size=3x]

#### [Reverse proxy](reverse-proxy.html)

Front protected applications with PingGateway.

[icon: plus-circle, set=fad, size=3x]

#### [Forward proxy](forward-proxy.html)

Add capabilities to applications with PingGateway.

[icon: cloud, set=fad, size=3x]

#### [Microservice](about-microgateway.html)

Run PingGateway as a microgateway in containerized environments.

[icon: cogs, set=fad, size=3x]

#### [Object model](about-processing.html)

Understand the PingGateway processing model.

[icon: user-tag, set=fad, size=3x]

#### [Sessions](about-sessions.html)

Understand PingGateway sessions.

[icon: file-code, set=fad, size=3x]

#### [API descriptors](api-descriptor.html)

Get API descriptors for PingGateway endpoints.

---

---
title: PingGateway API descriptors
description: Get API descriptors from PingGateway Common REST endpoints at runtime, using _api or _crestapi query parameters in development mode
component: pinggateway
version: 2026
page_id: pinggateway:about:api-descriptor
canonical_url: https://docs.pingidentity.com/pinggateway/2026/about/api-descriptor.html
llms_txt: https://docs.pingidentity.com/pinggateway/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2025-10-02T14:29:53Z
section_ids:
  get-api-descriptors-for-a-router: Get API descriptors for a router
  get_an_api_descriptor_for_the_uma_service: Get an API descriptor for the UMA service
  get_an_api_descriptor_for_the_main_router: Get an API descriptor for the main router
  get_an_api_descriptor_for_pinggateway_instances: Get an API descriptor for PingGateway instances
---

# PingGateway API descriptors

Common REST endpoints in PingGateway serve API descriptors at runtime.

When you get an API descriptor for an endpoint, PingGateway returns a resource describing the APIs at the endpoint and any child endpoints. Use the API descriptor with an OpenAPI tool like [Swagger UI](https://swagger.io/tools/swagger-ui/) to generate documentation.

When you start PingGateway or add or edit routes, PingGateway records endpoint locations in the PingGateway `logs/route-system.log` file and endpoint locations for subroutes in the specific log files for the routes.

To get the API descriptor for a specific endpoint, PingGateway must be in development mode. Make an HTTP GET request to the endpoint with one of the following query string parameters:

* `_api` for the API accessible over HTTP.

  You can get this API descriptor for partial URLs.

  The JSON API descriptor follows the OpenAPI specification.

* `_crestapi` for a proprietary, compact representation independent of the transport protocol.

  You can't get this API descriptor for partial URLs.

  The JSON API descriptor follows the proprietary specification for Common REST endpoints.

Learn more in [Common REST API documentation](../reference/AboutCrest.html#about-crest-api-descriptors).

## Get API descriptors for a router

|   |                                                                                                          |
| - | -------------------------------------------------------------------------------------------------------- |
|   | Switch to [development mode](../configure/operating-modes.html#development-mode) to get API descriptors. |

With PingGateway running as described in [Getting started with PingGateway](../getting-started/preface.html), use the following query to get an API descriptor for the router:

```console
$ curl http://ig.example.com:8085/api/system/objects/_router/routes\?_api
```

Output

```json
{
     "swagger": "2.0",
     "info": {
          "version": "2026.6.0",
          "title": "PingGateway"
     },
     "host": "0:0:0:0:0:0:0:1",
     "basePath": "/api/system/objects/_router/routes",
     "tags": [
          {
               "name": "Routes Endpoint"
          }
     ],
     "...": "..."
}
```

Alternatively, get a Common REST API descriptor with the `?_crestapi` query string.

## Get an API descriptor for the UMA service

|   |                                                                                                          |
| - | -------------------------------------------------------------------------------------------------------- |
|   | Switch to [development mode](../configure/operating-modes.html#development-mode) to get API descriptors. |

With the UMA tutorial running as described in [UMA support with PingAM](../gateway-guide/uma.html), use the following query to get an API descriptor for the UMA share API:

```console
$ curl http://ig.example.com:8085/api/system/objects/_router/routes/00-uma/objects/umaservice/share\?_api
```

Output

```json
{
     "swagger": "2.0",
     "info": {
          "version": "2026.6.0",
          "title": "PingGateway"
     },
     "host": "0:0:0:0:0:0:0:1",
     "basePath": "/api/system/objects/_router/routes/00-uma/objects/umaservice/share",
     "tags": [
          {
               "name": "Manage UMA Share objects"
          }
     ],
     "...": "..."
}
```

Alternatively, get a Common REST API descriptor with the `?_crestapi` query string.

## Get an API descriptor for the main router

|   |                                                                                                          |
| - | -------------------------------------------------------------------------------------------------------- |
|   | Switch to [development mode](../configure/operating-modes.html#development-mode) to get API descriptors. |

With PingGateway running, use the following query to get an API descriptor for the main router and child endpoints:

```console
$ curl http://ig.example.com:8085/api/system/objects/_router\?_api
```

Output

```json
{
     "swagger": "2.0",
     "info": {
          "version": "2026.6.0",
          "title": "PingGateway"
     },
     "host": "ig.example.com:8085",
     "basePath": "/api/system/objects/_router",
     "tags": [
          {
               "name": "Monitoring endpoint"
          },
          {
               "name": "Manage UMA Share objects"
          },
          {
               "name": "Routes Endpoint"
          }
     ],
     "...": "..."
}
```

The above URL is a partial URL, so you can't use the `?_crestapi` query string to get a Common REST API descriptor.

## Get an API descriptor for PingGateway instances

|   |                                                                                                          |
| - | -------------------------------------------------------------------------------------------------------- |
|   | Switch to [development mode](../configure/operating-modes.html#development-mode) to get API descriptors. |

With a PingGateway instance running, use the following query to get an API descriptor:

```console
$ curl http://ig.example.com:8085/api\?_api
```

Output

```json
{
     "swagger": "2.0",
     "info": {
          "version": "2026.6.0",
          "title": "PingGateway"
     },
     "host": "ig.example.com:8085",
     "basePath": "/api",
     "tags": [
          {
               "name": "Internal Storage for UI Models"
          },
          {
               "name": "Monitoring endpoint"
          },
          {
               "name": "Manage UMA Share objects"
          },
          {
               "name": "Routes Endpoint"
          },
          {
               "name": "Server Info"
          }
     ],
     "...": "..."
}
```

If you add routes after the request is performed, run the query again to get the updated API descriptor.

The above URL is a partial URL, so you can't use the `?_crestapi` query string to get a Common REST API descriptor.

---

---
title: PingGateway as a forward proxy
description: Configure PingGateway as a forward proxy to regulate outbound traffic, and adapt and enrich requests to external services
component: pinggateway
version: 2026
page_id: pinggateway:about:forward-proxy
canonical_url: https://docs.pingidentity.com/pinggateway/2026/about/forward-proxy.html
llms_txt: https://docs.pingidentity.com/pinggateway/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2025-04-02T12:24:35Z
keywords: ["Proxy", "Forward proxy"]
---

# PingGateway as a forward proxy

As a forward proxy, PingGateway is an intermediate connection point between an internal client and an external service. PingGateway regulates outbound traffic to the service and can adapt and enrich requests.

The following image illustrates PingGateway as a forward proxy:

![The gateway regulates traffic and enriches or adapts requests.](_images/ig-forward-proxy.png)

PingGateway provides the following features as a forward proxy:

* Addition of authentication or authorization to the request

* Addition of tracer IDs to the requests

* Addition or removal of request headers or scopes

---

---
title: PingGateway as a microgateway
description: Deploy PingGateway as a microgateway in containerized environments to separate security concerns from business logic
component: pinggateway
version: 2026
page_id: pinggateway:about:about-microgateway
canonical_url: https://docs.pingidentity.com/pinggateway/2026/about/about-microgateway.html
llms_txt: https://docs.pingidentity.com/pinggateway/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2025-04-02T12:24:35Z
---

# PingGateway as a microgateway

In containerized environments, PingGateway runs as a microgateway. Use PingGateway with business microservices to separate the security concerns of your applications from their business logic. For example, use PingGateway with the Token Validation Microservice to provide access token validation at the edge of your namespace. Find an example in [PingGateway as a microgateway](../gateway-guide/microgateway-protect-service.html).

The following image illustrates the request flow in an example deployment:

![Deploying a microgateway](_images/ig-mgw2.png)

PingGateway processes the request in the following steps:

1. A client requests access to Secured Microservice A, providing a stateful OAuth 2.0 access token as credentials.

2. Microgateway A intercepts the request and passes the access token to the Token Validation Microservice for validation using the `/introspect` endpoint.

3. The Token Validation Microservice requests the Authorization Server to validate the token.

4. The Authorization Server introspects the token and sends the introspection result to the Token Validation Microservice.

5. The Token Validation Microservice caches the introspection result and sends it to Microgateway A. Microgateway A forwards the result to Secured Microservice A.

6. Secured Microservice A uses the introspection result to decide how to process the request. In this case, it continues processing the request. Secured Microservice A asks for additional information from Secured Microservice B, providing the validated token as credentials.

7. Microgateway B intercepts the request and passes the access token to the Token Validation Microservice for validation using the `/introspect` endpoint.

8. The Token Validation Microservice retrieves the introspection result from the cache and sends it back to Microgateway B. Microgateway B forwards the result to Secured Microservice B.

9. Secured Microservice B uses the introspection result to decide how to process the request. In this case, it passes its response to Secured Microservice A through Microgateway B.

10. Secured Microservice A passes its response to the client through Microgateway A.

---

---
title: PingGateway as a reverse proxy
description: How PingGateway acts as a reverse proxy to intercept traffic, enforce policies, and enable OAuth 2.0, OpenID Connect, and SSO
component: pinggateway
version: 2026
page_id: pinggateway:about:reverse-proxy
canonical_url: https://docs.pingidentity.com/pinggateway/2026/about/reverse-proxy.html
llms_txt: https://docs.pingidentity.com/pinggateway/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2025-04-02T12:24:35Z
keywords: ["Proxy", "Reverse proxy"]
---

# PingGateway as a reverse proxy

As a reverse proxy, PingGateway is an intermediate connection point between external clients and internal services. PingGateway intercepts client requests and server responses, enforcing policies, and routing and shaping traffic.

The following image illustrates PingGateway as a reverse proxy:

![The gateway helps integrate existing services into newer architectures.](_images/ig-reverse-proxy.png)

PingGateway provides the following features as a reverse proxy:

* Ping Identity Platform integration

* Application and API security

* Credential replay

* OAuth 2.0 support

* OpenID Connect 1.0 support

* Network traffic control

* Proxy with request and response capture

* Request and response rewriting

* SAML 2.0 federation support

* Single sign-on (SSO)

---

---
title: PingGateway object model
description: Explains how PingGateway processes HTTP requests and responses through chains of filters and handlers, and describes the object model
component: pinggateway
version: 2026
page_id: pinggateway:about:about-processing
canonical_url: https://docs.pingidentity.com/pinggateway/2026/about/about-processing.html
llms_txt: https://docs.pingidentity.com/pinggateway/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2025-04-02T12:24:35Z
---

# PingGateway object model

PingGateway processes HTTP requests and responses by passing them through user-defined chains of filters and handlers. The filters and handlers can access the request and response at each step in the chain. They make it possible to alter the request or response and collect contextual information.

The following image illustrates how PingGateway processes a request and response through a chain:

![The incoming request is processed by a request filter](_images/chain.svg)

When PingGateway processes a request, it first builds an object representation of the request. The object representation includes parsed query/form parameters, cookies, headers, and the entity. PingGateway initializes a runtime context to provide metadata about the request and applied transformations. PingGateway passes the request representation into the chain.

In the request flow, filters modify the request representation and can enrich the runtime context with computed information. A `ClientHandler` serializes the entity content and can encode additional query parameters as described in [RFC 3986: Query](https://www.rfc-editor.org/rfc/rfc3986#section-3.4).

In the response flow, filters build a response representation with headers and the entity.

The route configuration in [Adding headers and logging results](../reference/HeaderFilter.html#HeaderFilter-example-logging) shows the flow through a chain to a protected application.

---

---
title: PingGateway sessions
description: "Understand and configure PingGateway sessions: in-memory and JWT-based session types, cookie handling, and session stickiness"
component: pinggateway
version: 2026
page_id: pinggateway:about:about-sessions
canonical_url: https://docs.pingidentity.com/pinggateway/2026/about/about-sessions.html
llms_txt: https://docs.pingidentity.com/pinggateway/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-02-23T12:00:00Z
section_ids:
  sessions-in-memory: In-memory sessions
  sessions-jwt-based: JWT-based sessions
  session-stickiness: Session stickiness
---

# PingGateway sessions

PingGateway uses sessions to group requests from a user-agent or other source and to collect and share information across the requests.

PingGateway supports [in-memory](#sessions-in-memory) and [JWT-based](#sessions-jwt-based) sessions.

* For in-memory sessions, PingGateway stores the session data in memory (default). It sets a session cookie on the user-agent that references the session.

* For JSON Web Token (JWT-based) sessions, the user-agent stores the session data. PingGateway puts the session data in a JWT stored as one or more session cookies on the user-agent.

By default, PingGateway uses different session cookie names for administrative and non-administrative connections.

Handlers and filters can access session data through the [SessionContext](../reference/SessionContext.html).

Session sharing is not thread-safe, so it is not suitable for concurrent exchanges.

**In-memory and JWT-based sessions**

| Feature                                                                               | In-memory sessions                                                                                  | JWT-based sessions                                                                                                                                                       |
| ------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Cookie size                                                                           | Unlimited                                                                                           | The maximum size of the JWT session cookie for a user-agent is 4 KBytes.If the cookie exceeds this size, PingGateway automatically splits it into multiple cookies.      |
| Default session cookie name                                                           | * `IG_ADMIN_SESSIONID` (administrative connections)

* `IG_SESSIONID` (other connections)           | `openig-jwt-session`                                                                                                                                                     |
| Data types the session can store                                                      | All types                                                                                           | [JSON-compatible types](https://www.json.org/json-en.html), such as strings, numbers, booleans, null, and arrays, lists, and maps containing only JSON-compatible types. |
| Session sharing between PingGateway servers for load balancing and failover           | Possible using [session stickiness](#session-stickiness)                                            | Possible because the session is a cookie on the user-agent; PingGateway servers must share any encryption keys.                                                          |
| Risk of data inconsistency when simultaneous requests modify the content of a session | Low because PingGateway stores the session content for all exchanges.Processing is not thread-safe. | Higher because the session content is reconstructed from the JWT for each request.Concurrent exchanges don't have the same content.                                      |

## In-memory sessions

PingGateway uses in-memory sessions by default.

To configure sessions, use an [InMemorySessionManager](../reference/InMemorySessionManager.html) as the `"session"` in the [AdminHttpApplication (`admin.json`)](../reference/AdminHttpApplication.html) for administrative requests and the [GatewayHttpApplication (`config.json` )](../reference/GatewayHttpApplication.html) or individual [Route](../reference/Route.html) for other requests.

The default session duration is 30 minutes. Even if the session is empty, the session remains usable until the timeout.

PingGateway can store any object type in an in-memory session.

Because PingGateway stores in-memory session content and shares it across all exchanges, simultaneous requests can update the session with low risk of the data becoming inconsistent. Sessions aren't thread-safe, however; different requests can simultaneously read and modify a shared session.

## JWT-based sessions

To configure JWT-based sessions, use a [JwtSessionManager](../reference/JwtSessionManager.html) for the `"session"` in the [AdminHttpApplication (`admin.json`)](../reference/AdminHttpApplication.html) for administrative requests and the [GatewayHttpApplication (`config.json` )](../reference/GatewayHttpApplication.html) or individual [Route](../reference/Route.html) for other requests.

PingGateway serializes session information as a JWT that is encrypted using authenticated encryption and optionally compressed. PingGateway stores the JWT in one or more session cookies on the user-agent. The JWT contains session attributes as JSON with a marker for the session timeout:

* PingGateway can only serialize [JSON-compatible types](https://www.json.org/json-en.html) in JWT session cookies.

* The maximum size of the JWT session cookie for a user-agent is 4 KBytes. If the cookie exceeds this size, PingGateway automatically splits it into multiple cookies.

* When PingGateway serializes an empty session, it marks the supporting cookie as expired, so the user-agent effectively discards it.

  To prevent PingGateway from cleaning up empty session cookies, add information to the session context with an [AssignmentFilter](../reference/AssignmentFilter.html#AssignmentFilter-example-addinfo).

PingGateway manages JWT-based sessions as follows:

* When a request enters a route using JWT-based sessions PingGateway:

  * Creates the [SessionContext](../reference/SessionContext.html).

  * Verifies the cookie signature.

  * Decrypts the content of the cookie.

  * Checks the current date is before the session timeout.

* As the request passes through the filters and handlers in the route, the filters and handlers can read and modify the session content.

* When the request returns to the point where the session was created, such the entrance to a route or `config.json`, PingGateway updates the cookie as follows:

  * If the session content has changed, PingGateway:

    * Serializes the session.

    * Creates one or more new JWT session cookies with the new content.

    * Encrypts the cookies using authenticated encryption.

    * Assigns the cookies an appropriate expiration time.

    * Returns the cookies in the response.

  * If the session is empty, PingGateway:

    * Deletes the session.

    * Creates a new expired JWT session cookie

    * Returns the cookie in the response.

  * If the session content has not changed, PingGateway does nothing.

Because the session content is stored on the user-agent, PingGateway servers can easily share JWT-based sessions. The user-agent returns the JWT cookies and any PingGateway server can unpack and use the session content.

When PingGateway updates JWT-based sessions in simultaneous requests, there is a high risk of the data becoming inconsistent. PingGateway reconstructs the session content for each exchange. Concurrent exchanges don't have the same content. PingGateway doesn't share sessions across requests. Each request has its own session objects that it modifies as necessary, writing its own session to the session cookie regardless of what other requests do.

## Session stickiness

Session stickiness helps ensure a client request goes to the server holding the original session data. With session stickiness, a load balancer in front of multiple PingGateway servers sends all requests from the same client session to the same server.

How you configure session stickiness depends on your load balancer.

Configure session stickiness whenever PingGateway stores session data attached to a server-side context. For example, configure session stickiness when using in-memory sessions and multiple PingGateway servers.