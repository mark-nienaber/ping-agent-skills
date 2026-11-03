---
title: MCP security gateway
description: Use PingGateway as an MCP security gateway to protect MCP servers with OAuth 2.1, auditing, rate limiting, and access control
component: pinggateway
version: 2026
page_id: pinggateway:mcp:index
canonical_url: https://docs.pingidentity.com/pinggateway/2026/mcp/index.html
llms_txt: https://docs.pingidentity.com/pinggateway/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-09-15T10:10:08Z
keywords: ["AI", "Model Context Protocol", "OAuth 2.1", "Security"]
section_ids:
  goals: Goals
  what_youll_do: What you'll do
  preparation: Preparation
  install-software: "Preparation task 1: Install software for the tutorials"
  run-mcp-server: "Preparation task 2: Run the sample MCP server"
  run-mcp-agent: "Preparation task 3: Run the MCP agent"
---

# MCP security gateway

[Model Context Protocol (MCP)](https://modelcontextprotocol.io/docs/getting-started/intro) offers an open standard to connect artificial intelligence (AI) agents with AI servers. By exposing services over MCP, you make them usable by AI agents.

The challenge, however, consists in implementing an appropriate, consistent, documented, and adaptable security model across the service assets you expose over MCP. PingGateway helps you meet this challenge as an MCP gateway, protecting MCP servers to:

* Allow only valid MCP requests.

* Audit MCP requests and actors.

* Throttle request rates.

* Enforce coarse-grained OAuth 2.1 security controls.

* Enforce fine-grained access control policies with PingOne Authorize, PingAuthorize, PingOne Protect, and Advanced Identity Cloud.

* Perform token transformation mapped to your security models.

![PingGateway in MCP security architecure](_images/mcp-gateway.png)

The following diagram illustrates the flow of an MCP request through PingGateway as the MCP gateway to an MCP server:

![MCP request flow through PingGateway](_images/mcp-server-flow.svg)

Business teams can focus on accelerating AI adoption in the business while identity and access management and security teams address security.

|   |                                                                                                                                                                                                                             |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | This feature has [Evolving](https://docs.pingidentity.com/pinggateway/release-notes/stability.html#interface-stability) interface stability. It's subject to change without notice, even in a minor or maintenance release. |

This page describes how to use PingGateway to protect a sample MCP server. Complete the preparation, then follow the tutorial for your OAuth 2.1 authorization server (AS): PingOne or PingOne Advanced Identity Cloud. The same approach works with other OAuth 2.1 authorization servers, including PingAM. When you understand how a tutorial works, you can adapt the pattern to protect your own MCP servers.

## Goals

When you complete a tutorial, you learn:

* How to use PingGateway to protect an MCP server.

* How to create a route to audit, protect, and validate MCP requests.

* How PingGateway acts as an MCP gateway and resource server in an MCP security architecture.

## What you'll do

Start by preparing the sample MCP software. After it works on your computer, follow the tutorial for your AS to protect the MCP server with PingGateway.

The tutorials assume you already have PingGateway and the AS set up, and only need to configure them for MCP.

The full example has two parts:

1. Prepare the sample MCP software:

   * [Install software for the tutorials](#install-software).

   * [Run the sample MCP server](#run-mcp-server).

   * [Run the sample MCP agent](#run-mcp-agent).

   By completing these tasks, you show the sample MCP software works on your computer without PingGateway.

2. Protect the sample MCP server with PingGateway:

   * [Protect an MCP server with PingOne](tutorial-pingone.html)

   * [Protect an MCP server with PingOne Advanced Identity Cloud](tutorial-aic.html)

   By following a tutorial, you show how to use PingGateway in an MCP security architecture.

## Preparation

Before trying a tutorial, prepare the sample MCP software to make sure it works on your computer.

### Preparation task 1: Install software for the tutorials

1. Install the prerequisite software on your computer:

   * [Ollama](https://ollama.com/download) for the sample MCP agent model.

   * [Python](https://www.python.org/downloads/) 3.11 or later to run the sample MCP agent and server.

2. Download the sample MCP agent and server software from [Ping Identity Download Center](https://product-downloads.pingidentity.com/) and unpack it on your computer.

### Preparation task 2: Run the sample MCP server

The sample MCP server runs as a Python script.

1. In the directory where you unpacked the sample MCP server, add the Python requirements.

   Install the requirements based on the `requirements-lock.txt` file provided with the sample MCP server:

   ```console
   $ pip install -r requirements-lock.txt
   ```

2. In the directory where you unpacked the sample MCP server, run the sample MCP server script:

   ```console
   $ uvicorn sample-mcp-server:app --host 0.0.0.0 --port 8000 --log-level info
   ```

   If necessary, learn about additional options in the `README.md` file.

You have successfully started the sample MCP server.

### Preparation task 3: Run the MCP agent

The sample MCP agent uses [Meta's Llama 3.2](https://ollama.com/library/llama3.2) model. Run it in a different terminal window from the sample MCP server.

1. Download, install, and run Ollama if you haven't already done so.

2. Install the Ollama model for the sample MCP server locally:

   ```console
   $ ollama pull llama3.2:1b
   ```

3. Run Ollama.

4. In the directory where you unpacked the sample MCP agent, add the Python requirements.

   Install the requirements based on the `requirements-lock.txt` file provided with the sample MCP agent:

   ```console
   $ pip install -r requirements-lock.txt
   ```

5. In the directory where you unpacked the sample MCP agent, run the sample MCP agent script:

   ```console
   $ python3 sample-mcp-agent.py --mcp-server-url http://localhost:8000
   ```

   If necessary, learn about additional options in the script help: `python3 sample-mcp-agent.py --help`

6. In the console where the sample MCP agent runs, notice the available commands:

   ```none
   [INFO] Discovered tools [http://localhost:8000]:
   [INFO] - geocode: Returns a list of objects containing city name, latitude, longitude, country, admin1 (region), and timezone for each matching city
   [INFO] - forecast_daily: Returns a multi-day weather forecast for a given location
   [INFO] - forecast_periods: Returns weather forecasts for each representative period of the current day
   [INFO] - forecast_hourly: Returns an hourly weather forecast for the current day
   [INFO] - weather_at_time: Returns the forecasted weather for a specific time at a given location

   Enter your message (or 'exit|quit|q'):
   ```

   This shows the sample MCP agent can connect to the sample MCP server.

7. Enter a prompt and get a response from the MCP server, then exit the agent.

   The following example uses the `forecast_daily` tool to get the daily forecast for Tokyo:

   ```none
   Enter your message (or 'exit|quit|q'): What is the daily forecast for Tokyo?
   Agent: The daily forecast for Tokyo is:

   <MCP server response with forecast details>

   Enter your message (or 'exit|quit|q'): exit
   User requested exit. Goodbye!
   ```

You have successfully run the sample MCP agent with the sample MCP server.

---

---
title: Protect an MCP server with PingOne
description: Tutorial to protect a sample MCP server using PingGateway and PingOne as the OAuth 2.1 authorization server
component: pinggateway
version: 2026
page_id: pinggateway:mcp:tutorial-pingone
canonical_url: https://docs.pingidentity.com/pinggateway/2026/mcp/tutorial-pingone.html
llms_txt: https://docs.pingidentity.com/pinggateway/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-09-15T10:10:08Z
keywords: ["AI", "Model Context Protocol", "OAuth 2.1", "Security"]
section_ids:
  before-you-begin: "Task 1: Before you begin"
  configure-as: "Task 2: Prepare PingOne as the AS"
  create-resource: Create a resource
  create-native-app: Create a native application
  configure-gateway: "Task 3: Configure PingGateway"
  start-mcp-agent: "Task 4: Start the MCP agent"
  validate-mcp: Validation
---

# Protect an MCP server with PingOne

## Task 1: Before you begin

* Complete the preparation described in [Prepare the sample MCP software](index.html#preparation).

* Make sure you can access the PingOne administration console as an administrator.

* Set up PingGateway with HTTPS on port 8443.

  The following tasks use `https://ig.example.com:8443`.

## Task 2: Prepare PingOne as the AS

Prepare PingOne to act as the OAuth 2.1 AS for MCP by creating a resource and an application.

### Create a resource

1. In the PingOne admin console, go to Applications > Resources, and click [icon: plus-circle, set=fa].

2. Set Resource Name to a name for the resource, for example, `MCP Resource`, and click Next.

3. Set Audience to the URL that PingGateway uses as the resource identifier: `https://ig.example.com:8443/p1-mcp`.

   PingGateway validates the `aud` claim in each access token against this value. Update this value if you change the gateway URL or route path.

4. Click Save.

5. On the Scopes tab, click + Add Scope, set Name to `test`, and click Save.

6. Enable the resource using the toggle at the top of the page.

7. On the Overview tab, note the Client ID and Client Secret.

   PingGateway uses these credentials to call the PingOne token introspection endpoint.

8. Add the base64-encoded client secret to the PingGateway environment:

   ```console
   $ export PINGONE_RESOURCE_SECRET=$(echo -n '<resource-client-secret>' | base64)
   ```

   The [SystemAndEnvSecretStore](../reference/SystemAndEnvSecretStore.html) in the route reads the secret ID `pingone.resource.secret` from the `PINGONE_RESOURCE_SECRET` environment variable.

9. Restart PingGateway to load the secret.

### Create a native application

Create the application that the MCP agent uses to authenticate. PingOne requires pre-registered clients. It doesn't support dynamic client registration.

1. In the PingOne admin console, go to Applications > Applications, and click [icon: plus-circle, set=fa].

2. Select Native App, set Application Name to a name, for example, `MCP Client`, and click Save.

3. On the Configuration tab, set:

   * Grant Types: Authorization Code and Refresh Token

   * Token Endpoint Auth Method: None

   * PKCE Enforcement: S256 Required

   * Redirect URIs: `http://localhost:3000/callback`

4. Click Save.

5. On the Resources tab, click [icon: pencil-alt, set=fa], select the resource you created, allow the `test` scope, and click Save.

6. On the Overview tab, note the Client ID.

   You pass this value to the sample MCP agent in [Task 4: Start the MCP agent](#start-mcp-agent).

You have successfully prepared PingOne to act as the AS.

## Task 3: Configure PingGateway

1. If the MCP server uses [server-sent events (SSE)](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events), update the `admin.json` file for PingGateway to [enable streaming](../reference/AdminHttpApplication.html#AdminHttpApplication-streamingEnabled), and restart PingGateway.

   Skip this step for the sample MCP server.

2. Add the following route to PingGateway and correct the `"properties"` settings:

   * Linux

     `$HOME/.openig/config/routes/mcp-p1.json`

   * Windows

     `%appdata%\OpenIG\config\routes\mcp-p1.json`

   ```json
   {
     "name": "mcp-p1",
     "condition": "${find(request.uri.path, '^/p1-mcp')}",
     "properties": {
       "mcpServerUrl": "http://localhost:8000",
       "gatewayUrl": "https://ig.example.com:8443",
       "pingOneAsUrl": "https://auth.pingone.com/<envId>/as",
       "pingOneIntrospectUrl": "https://auth.pingone.com/<envId>/as/introspect",
       "pingOneResourceClientId": "<resourceId>"
     },
     "baseURI": "&{mcpServerUrl}",
     "heap": [
       {
         "name": "AuditService",
         "type": "AuditService",
         "config": {
           "eventHandlers": [
             {
               "class": "org.forgerock.audit.handlers.json.JsonAuditEventHandler",
               "config": {
                 "name": "json",
                 "logDirectory": "&{ig.instance.dir}/audit",
                 "topics": [
                   "access",
                   "mcp"
                 ]
               }
             }
           ]
         }
       },
       {
         "name": "rsFilter",
         "type": "OAuth2ResourceServerFilter",
         "config": {
           "scopes": [
             "test"
           ],
           "accessTokenResolver": {
             "type": "TokenIntrospectionAccessTokenResolver",
             "config": {
               "endpoint": "&{pingOneIntrospectUrl}",
               "providerHandler": {
                 "type": "Chain",
                 "config": {
                   "filters": [
                     {
                       "type": "ClientSecretBasicAuthenticationFilter",
                       "config": {
                         "clientId": "&{pingOneResourceClientId}",
                         "clientSecretId": "pingone.resource.secret",
                         "secretsProvider": {
                           "type": "SystemAndEnvSecretStore"
                         }
                       }
                     }
                   ],
                   "handler": "ClientHandler"
                 }
               }
             }
           }
         }
       }
     ],
     "handler": {
       "type": "Chain",
       "config": {
         "filters": [
           {
             "type": "McpAuditFilter",
             "config": {
               "auditService": "AuditService"
             }
           },
           {
             "type": "McpProtectionFilter",
             "config": {
               "resourceId": "&{gatewayUrl}/p1-mcp",
               "authorizationServerUri": "&{pingOneAsUrl}",
               "resourceServerFilter": "rsFilter",
               "supportedScopes": [
                 "test"
               ]
             }
           },
           {
             "type": "McpValidationFilter",
             "config": {
               "acceptedOrigins": ".*"
             }
           },
           {
             "type": "UriPathRewriteFilter",
             "config": {
               "mappings": {
                 "/p1-mcp": "/"
               }
             }
           }
         ],
         "handler": {
           "type": "ReverseProxyHandler",
           "config": {
             "soTimeout": "20 seconds"
           }
         }
       }
     }
   }
   ```

   Source: [mcp-p1.json](../_attachments/config/routes/mcp-p1.json)

   Update the following properties:

   * `mcpServerUrl` — the URL of the MCP server. The default assumes the sample MCP server runs on your computer.

   * `gatewayUrl` — the base URL of PingGateway. The route uses this to construct the resource identifier.

   * `pingOneAsUrl` — the AS base URL for your PingOne environment, for example, `https://auth.pingone.eu/<envId>/as` for the EU region. Replace `<envId>` with your PingOne environment ID and adjust the domain for your region.

   * `pingOneIntrospectUrl` — the introspect endpoint for your environment.

   * `pingOneResourceClientId` — the resource Client ID noted in [Create a resource](#create-resource).

   Notice the following features of the route:

   * PingGateway acts as an OAuth 2.1 resource server (RS) when protecting the sample MCP server.

   * The [McpAuditFilter](../reference/McpAuditFilter.html) audits MCP requests. PingGateway records MCP audit events in an `audit/mcp.audit.json` file.

   * The [McpProtectionFilter](../reference/McpProtectionFilter.html) serves the MCP OAuth 2.1 protected resource metadata endpoint and validates that each access token is intended for this resource. The filter comes before [UriPathRewriteFilter](../reference/UriPathRewriteFilter.html) so it sees the original request path.

   * The `McpProtectionFilter` uses the default `"resourceIdPointer"` of `/aud`, which matches the `aud` claim PingOne includes in access tokens.

   * The [TokenIntrospectionAccessTokenResolver](../reference/TokenIntrospectionAccessTokenResolver.html) calls the PingOne introspect endpoint with the resource client credentials from the environment variable.

   * The [McpValidationFilter](../reference/McpValidationFilter.html) validates MCP protocol compliance for each request.

   * The [UriPathRewriteFilter](../reference/UriPathRewriteFilter.html) rewrites the route path prefix before the request reaches the MCP server.

   * The [ReverseProxyHandler](../reference/ReverseProxyHandler.html) uses a long `"soTimeout"` setting to accommodate an MCP agent receiving few or infrequent SSE updates.

   This simple route doesn't show [throttling](../reference/ThrottlingPolicies.html) or fine-grained access control. Add those features as needed to meet your security requirements.

3. Verify the PingGateway log shows the route loaded successfully.

You have successfully configured PingGateway to protect the sample MCP server.

## Task 4: Start the MCP agent

|   |                                                                                                              |
| - | ------------------------------------------------------------------------------------------------------------ |
|   | The `--client-id` argument used in this task requires the sample MCP agent from PingGateway 2026.9 or later. |

In the directory where you unpacked the sample MCP agent, start the sample MCP agent again. This time, point it to the PingGateway route and pass the application client ID you noted in [Create a native application](#create-native-app):

```console
$ python3 sample-mcp-agent.py \
    --mcp-server-url https://ig.example.com:8443/p1-mcp \
    --client-id <native-app-client-id>
```

No client secret is needed because the application uses PKCE only.

Passing `--client-id` pre-registers the client in the agent's token storage, so the agent skips dynamic client registration and uses the pre-registered client directly.

You have successfully started the sample MCP agent.

## Validation

With PingGateway protecting the MCP server, the sample MCP agent directs your browser to PingOne to sign on as an end user and authorize access to make MCP requests. If it can't open the browser, the sample MCP agent shows the URL you can paste into a private or incognito window.

1. Sign on with your PingOne user credentials and consent to the requested `test` scope before closing the browser tab as prompted.

2. In the terminal where the sample MCP agent runs, notice the available commands:

   ```text
   [INFO] Discovered tools [https://ig.example.com:8443/p1-mcp]:
   [INFO] - geocode: Returns a list of objects containing city name, latitude, longitude, country, admin1 (region), and timezone for each matching city
   [INFO] - forecast_daily: Returns a multi-day weather forecast for a given location
   [INFO] - forecast_periods: Returns weather forecasts for each representative period of the current day
   [INFO] - forecast_hourly: Returns an hourly weather forecast for the current day
   [INFO] - weather_at_time: Returns the forecasted weather for a specific time at a given location

   Enter your message (or 'exit|quit|q'):
   ```

3. Enter a prompt and get a response from the MCP server through PingGateway, then exit the agent:

   The following example uses the `forecast_daily` tool to get the daily forecast for Tokyo:

   ```text
   Enter your message (or 'exit|quit|q'): What is the daily forecast for Tokyo?
   Agent: The daily forecast for Tokyo is:

   <MCP server response with forecast details>

   Enter your message (or 'exit|quit|q'): exit
   User requested exit. Goodbye!
   ```

   Find additional details about the MCP request in the PingGateway log.

You have successfully validated PingGateway can protect the MCP server.

---

---
title: Protect an MCP server with PingOne Advanced Identity Cloud
description: Tutorial to protect a sample MCP server using PingGateway and PingOne Advanced Identity Cloud as the OAuth 2.0 authorization server
component: pinggateway
version: 2026
page_id: pinggateway:mcp:tutorial-aic
canonical_url: https://docs.pingidentity.com/pinggateway/2026/mcp/tutorial-aic.html
llms_txt: https://docs.pingidentity.com/pinggateway/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-09-15T10:10:08Z
keywords: ["AI", "Model Context Protocol", "OAuth 2.1", "Security"]
section_ids:
  before-you-begin: "Task 1: Before you begin"
  configure-as: "Task 2: Prepare Advanced Identity Cloud as the AS"
  configure-gateway: "Task 3: Configure PingGateway"
  start-mcp-agent: "Task 4: Start the MCP agent"
  validate-mcp: Validation
---

# Protect an MCP server with PingOne Advanced Identity Cloud

## Task 1: Before you begin

* Complete the preparation described in [Prepare the sample MCP software](index.html#preparation).

* Make sure you can access the PingOne Advanced Identity Cloud tenant as an administrator.

* Choose the realm to use in the PingOne Advanced Identity Cloud tenant.

  The following tasks use the `alpha` realm.

* Prepare PingGateway as described in [PingGateway and PingOne Advanced Identity Cloud](../aic/preface.html).

  After you follow the instructions to [register the PingGateway agent in Advanced Identity Cloud](../aic/preface.html#register-agent-idc), the PingGateway profile is registered with Advanced Identity Cloud as `ig_agent`.

* Update the agent profile to set the token introspection scope:

  1. Open the AM admin UI at [icon: open_in_new, set=material, size=inline] Native Consoles > Access Management.

  2. In the AM admin UI, go to Applications > Agents > Identity Gateway > ig_agent.

  3. Set Token Introspection to `Realm Only`.

  4. Click Save Changes.

* For other AS options, learn more in:

  * [Protect an MCP server with PingOne](tutorial-pingone.html)

  * [Protect an MCP server with PingFederate](../reference/McpProtectionFilter.html#McpProtectionFilter-example-pingfederate)

## Task 2: Prepare Advanced Identity Cloud as the AS

1. Sign on to the Advanced Identity Cloud admin UI as an administrator.

2. Ensure the OAuth2 Provider for your realm has an OAuth2 Access Token Modification script to support [RFC 8707, Resource Indicators for OAuth 2.0](https://www.rfc-editor.org/rfc/rfc8707.html) as required by MCP.

   If the OAuth2 Provider for your realm already uses an OAuth2 Access Token Modification script, add code to set the audience claim in the access token as shown for the following script.

   To add a new script, go to [icon: code, set=material, size=inline] Scripts > Auth Scripts > New Script > OAuth2 / OIDC > OAuth2 Access Token Modification, click Next, add the following script, and click Save and Close:

   * Name: `MCP aud script`

   * JavaScript:

     ```js
     // Make sure the `audience` claim matches the resource identifier
     (function () {
     	  accessToken.setField("audience", requestProperties.get("requestParams").get("resource").get(0));
     	  // No return value is expected. Leave it undefined.
     	  }());
     ```

     The PingGateway [McpProtectionFilter](../reference/McpProtectionFilter.html) consumes the claim specified in its `"resourceIdPointer"` setting.

3. Using the AM admin UI, update the `OAuth2 Provider` service settings for the realm.

   In the AM admin UI at [icon: open_in_new, set=material, size=inline] Native Consoles > Access Management, go to Services and change the following settings for the `OAuth2 Provider` service:

   * Advanced tab > Client Registration Scope Allowlist: Add `test`.

   * Client Dynamic Registration tab > Allow Open Dynamic Client Registration: Enable and click Save Changes.

   * Plugins tab > Access Token Modification Script: Set to `MCP aud script` if you added it as a new script and click Save Changes.

You have successfully prepared Advanced Identity Cloud to act as the AS.

## Task 3: Configure PingGateway

Previously, you prepared PingGateway for HTTPS as described in [Task 1: Before you begin](#before-you-begin). Now, configure PingGateway to protect the sample MCP server:

1. If the MCP server uses [server-sent events (SSE)](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events), update the `admin.json` file for PingGateway to [enable streaming](../reference/AdminHttpApplication.html#AdminHttpApplication-streamingEnabled), and restart PingGateway.

   Skip this step for the sample MCP server.

2. Add the following route to PingGateway updating `"properties"` as needed for your deployment:

   * Linux

     `$HOME/.openig/config/routes/mcp-aic.json`

   * Windows

     `%appdata%\OpenIG\config\routes\mcp-aic.json`

   ```json
   {
     "name": "mcp-aic",
     "condition": "${find(request.uri.path, '^/aic-mcp')}",
     "properties": {
       "amRealm": "/alpha",
       "gatewayUrl": "https://ig.example.com:8443",
       "mcpServerUrl": "http://localhost:8000",
       "tenantHostname": "myTenant.forgeblocks.com"
     },
     "baseURI": "&{mcpServerUrl}",
     "heap": [
       {
         "name": "AuditService",
         "type": "AuditService",
         "config": {
           "eventHandlers": [
             {
               "class": "org.forgerock.audit.handlers.json.JsonAuditEventHandler",
               "config": {
                 "name": "json",
                 "logDirectory": "&{ig.instance.dir}/audit",
                 "topics": [
                   "access",
                   "mcp"
                 ]
               }
             }
           ]
         }
       },
       {
         "name": "SecretsPasswords",
         "type": "Base64EncodedSecretStore",
         "config": {
           "secrets": {
             "agent.secret.id": "cGFzc3dvcmQ="
           }
         }
       },
       {
         "name": "AmService",
         "type": "AmService",
         "config": {
           "realm": "&{amRealm}",
           "agent": {
             "username": "ig_agent",
             "passwordSecretId": "agent.secret.id"
           },
           "secretsProvider": "SecretsPasswords",
           "sessionCache": {
             "enabled": true
           },
           "url": "https://&{tenantHostname}/am/"
         }
       },
       {
         "name": "rsFilter",
         "type": "OAuth2ResourceServerFilter",
         "config": {
           "scopes": [
             "test"
           ],
           "accessTokenResolver": {
             "type": "TokenIntrospectionAccessTokenResolver",
             "config": {
               "amService": "AmService",
               "providerHandler": {
                 "type": "Chain",
                 "config": {
                   "filters": [
                     {
                       "type": "HttpBasicAuthenticationClientFilter",
                       "config": {
                         "username": "ig_agent",
                         "passwordSecretId": "agent.secret.id",
                         "secretsProvider": "SecretsPasswords"
                       }
                     }
                   ],
                   "handler": "ClientHandler"
                 }
               }
             }
           }
         }
       }
     ],
     "handler": {
       "type": "Chain",
       "capture": "all",
       "config": {
         "filters": [
           {
             "type": "McpAuditFilter",
             "config": {
               "auditService": "AuditService"
             }
           },
           {
             "type": "UriPathRewriteFilter",
             "config": {
               "mappings": {
                 "/aic-mcp": "/"
               }
             }
           },
           {
             "type": "McpProtectionFilter",
             "config": {
               "resourceId": "&{gatewayUrl}/aic-mcp",
               "authorizationServerUri": "https://&{tenantHostname}/am/oauth2/realms/root/realms&{amRealm}",
               "resourceServerFilter": "rsFilter",
               "supportedScopes": [
                 "test"
               ],
               "resourceIdPointer": "/audience"
             }
           },
           {
             "type": "McpValidationFilter",
             "config": {
               "acceptedOrigins": ".*"
             }
           }
         ],
         "handler": {
           "type": "ReverseProxyHandler",
           "config": {
             "soTimeout": "20 seconds"
           }
         }
       }
     }
   }
   ```

   Source: [mcp-aic.json](../_attachments/config/routes/mcp-aic.json)

   Notice the following features of the route:

   * The sample route uses a base-64 encoded secret to connect to the AS. In production, don't include secrets in route files.

   * PingGateway acts as an OAuth 2.1 resource server (RS) when protecting the sample MCP server.

   * The [McpAuditFilter](../reference/McpAuditFilter.html) audits MCP requests. PingGateway records MCP audit events in an `audit/mcp.audit.json` file.

   * The [UriPathRewriteFilter](../reference/UriPathRewriteFilter.html) sends the request to the root resource of the MCP server. The MCP server expects requests at `/`.

   * The [McpProtectionFilter](../reference/McpProtectionFilter.html) uses the RS configuration, extending it for MCP.

   * PingGateway validates MCP requests with an [McpValidationFilter](../reference/McpValidationFilter.html).

   * The [ReverseProxyHandler](../reference/ReverseProxyHandler.html) uses a long `"soTimeout"` setting to accommodate an MCP agent receiving few or infrequent SSE updates.

   This simple route doesn't show [throttling](../reference/ThrottlingPolicies.html) or fine-grained access control. Add those features as needed to meet your security requirements.

3. Verify the PingGateway log shows the route loaded successfully.

You have successfully configured PingGateway to protect the sample MCP server.

## Task 4: Start the MCP agent

In the directory where you unpacked the sample MCP agent, start the sample MCP agent again. This time, point it to the PingGateway route for MCP requests:

```console
$ python3 sample-mcp-agent.py --mcp-server-url https://ig.example.com:8443/aic-mcp
```

You have successfully started the sample MCP agent.

## Validation

With PingGateway protecting the MCP server, the sample MCP agent directs your browser to the AS to sign on as an end user and authorize access to make MCP requests. If it can't open the browser, the sample MCP agent shows the URL you can paste into a private or incognito window.

1. Sign on with the end-user credentials (username: `demo` password: `Ch4ng3!t`) and consent to the requested `test` scope before closing the browser tab as prompted.

   You set these credentials when you [set up a demo user in PingOne Advanced Identity Cloud](../aic/preface.html#setup-user-idc).

2. In the terminal where the sample MCP agent runs, notice the available commands:

   ```text
   [INFO] Discovered tools [https://ig.example.com:8443/aic-mcp]:
   [INFO] - geocode: Returns a list of objects containing city name, latitude, longitude, country, admin1 (region), and timezone for each matching city
   [INFO] - forecast_daily: Returns a multi-day weather forecast for a given location
   [INFO] - forecast_periods: Returns weather forecasts for each representative period of the current day
   [INFO] - forecast_hourly: Returns an hourly weather forecast for the current day
   [INFO] - weather_at_time: Returns the forecasted weather for a specific time at a given location

   Enter your message (or 'exit|quit|q'):
   ```

3. Enter a prompt and get a response from the MCP server through PingGateway, then exit the agent:

   The following example uses the `forecast_daily` tool to get the daily forecast for Tokyo:

   ```text
   Enter your message (or 'exit|quit|q'): What is the daily forecast for Tokyo?
   Agent: The daily forecast for Tokyo is:

   <MCP server response with forecast details>

   Enter your message (or 'exit|quit|q'): exit
   User requested exit. Goodbye!
   ```

   Find additional details about the MCP request in the PingGateway log.

You have successfully validated PingGateway can protect the MCP server.