---
title: MCP security gateway
description: Use PingGateway as an MCP security gateway to protect MCP servers with OAuth 2.0, auditing, rate limiting, and access control
component: pinggateway
version: 2026
page_id: pinggateway:mcp:index
canonical_url: https://docs.pingidentity.com/pinggateway/2026/mcp/index.html
revdate: 2026-03-17T18:00:00Z
keywords: ["AI", "Model Context Protocol", "OAuth 2.0", "Security"]
section_ids:
  goals: Goals
  what_youll_do: What you'll do
  preparation: Preparation
  install-software: "Preparation task 1: Install software for this tutorial"
  run-mcp-server: "Preparation task 2: Run the sample MCP server"
  run-mcp-agent: "Preparation task 3: Run the MCP agent"
  tutorial: Tutorial
  before-you-begin: "Tutorial task 1: Before you begin"
  configure-as: "Tutorial task 2: Prepare Advanced Identity Cloud as the AS"
  configure-gateway: "Tutorial task 3: Configure PingGateway"
  start-mcp-agent: "Tutorial task 4: Start the MCP agent"
  validate-mcp: Validation
---

# MCP security gateway

[Model Context Protocol (MCP)](https://modelcontextprotocol.io/docs/getting-started/intro) offers an open standard to connect artificial intelligence (AI) agents with AI servers. By exposing services over MCP, you make them usable by AI agents.

The challenge, however, consists in implementing an appropriate, consistent, documented, and adaptable security model across the service assets you expose over MCP. PingGateway helps you meet this challenge as an MCP gateway, protecting MCP servers to:

* Allow only valid MCP requests.

* Audit MCP requests and actors.

* Throttle request rates.

* Enforce coarse-grained OAuth 2.0 security controls.

* Enforce fine-grained access control policies with PingOne Authorize, PingAuthorize, PingOne Protect, and Advanced Identity Cloud.

* Perform token transformation mapped to your security models.

![PingGateway in MCP security architecure](_images/mcp-gateway.png)

The following diagram illustrates the flow of an MCP request through PingGateway as the MCP gateway to an MCP server:

![MCP request flow through PingGateway](_images/mcp-server-flow.svg)

Business teams can focus on accelerating AI adoption in the business while identity and access management and security teams address security.

|   |                                                                                                                                                                                                                             |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | This feature has [Evolving](https://docs.pingidentity.com/pinggateway/release-notes/stability.html#interface-stability) interface stability. It's subject to change without notice, even in a minor or maintenance release. |

This page shows how to protect a sample MCP server using Advanced Identity Cloud as the OAuth 2.0 authorization server (AS). Follow similar steps when using PingOne or PingAM as the AS and to protect your own MCP servers.

## Goals

When you complete this tutorial, you will know:

* How to use PingGateway to protect an MCP server.

* How to create a route to audit, protect, and validate MCP requests.

* How PingGateway acts as an MCP gateway and resource server in an MCP security architecture.

## What you'll do

In this tutorial, you will start by preparing the sample MCP software with the server to protect. Once the MCP software works on your computer, you will use PingGateway to protect the MCP server.

The tutorial assumes you already have PingGateway and the AS set up, and only need to configure them for MCP.

The full example has two parts with multiple tasks each:

1. Prepare the sample MCP software:

   * [Install software for this tutorial](#install-software).

   * [Run the sample MCP server](#run-mcp-server).

   * [Run the sample MCP agent](#run-mcp-agent).

   By completing these tasks, you show the sample MCP software works on your computer without PingGateway or Advanced Identity Cloud.

2. Protect the sample MCP server with PingGateway:

   * [Prepare PingGateway to connect to you Advanced Identity Cloud tenant](#before-you-begin).

   * [Prepare Advanced Identity Cloud as the OAuth 2.0 AS for MCP.](#configure-as)

   * [Configure PingGateway to protect the sample MCP server](#configure-gateway).

   * [Restart the sample MCP agent](#start-mcp-agent).

   * [Validate PingGateway can protect the MCP server](#validate-mcp).

   By completing these tasks, you show how to use PingGateway in an MCP security architecture.

## Preparation

Before trying the tutorial, prepare the sample MCP software to make sure it works on your computer.

### Preparation task 1: Install software for this tutorial

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

## Tutorial

Now you know the sample MCP software works on your computer. Show you can protect the sample MCP server with PingGateway using Advanced Identity Cloud as the AS.

### Tutorial task 1: Before you begin

* Prepare the sample MCP software as described in [Preparation](#preparation).

* Make sure you can access the PingOne Advanced Identity Cloud tenant as an administrator.

* Choose the realm to use in the PingOne Advanced Identity Cloud tenant.

  The following tasks use the `alpha` realm.

* Prepare PingGateway as described in [PingGateway and PingOne Advanced Identity Cloud](../aic/preface.html).

  After you follow the instructions to [register the PingGateway agent in Advanced Identity Cloud](../aic/preface.html#register-agent-idc), the PingGateway profile is registered with Advanced Identity Cloud as `ig_agent`.

* Update the agent profile to set the token introspection scope:

  1. Open the AM admin UI at [icon: open_in_new, set=material, size=inline] Native Consoles > Access Management.

  2. In the AM admin UI, go to Applications > Agents > Identity Gateway > ig\_agent.

  3. Set Token Introspection to `Realm Only`.

  4. Click Save Changes.

### Tutorial task 2: Prepare Advanced Identity Cloud as the AS

1. Sign on to the Advanced Identity Cloud admin UI as an administrator.

2. Make sure you have an OAuth2 Access Token Modification script to support [RFC 8707, Resource Indicators for OAuth 2.0](https://www.rfc-editor.org/rfc/rfc8707.html) as required by MCP.

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

     The PingGateway [McpProtectionFilter](../reference/McpProtectionFilter.html) will consume the claim specified in its `"resourceIdPointer"` setting.

3. Using the AM admin UI, update the `OAuth2 Provider` service settings for the realm.

   In the AM admin UI at [icon: open_in_new, set=material, size=inline] Native Consoles > Access Management, go to Services and change the following settings for the `OAuth2 Provider` service:

   * Advanced tab > Client Registration Scope Allowlist: Add `test`.

   * Client Dynamic Registration tab > Allow Open Dynamic Client Registration: Enable and click Save Changes.

   * Plugins tab > Access Token Modification Script: Set to `MCP aud script` if you added it as a new script and click Save Changes.

You have successfully prepared Advanced Identity Cloud to act as the AS.

### Tutorial task 3: Configure PingGateway

Previously, you prepared PingGateway for HTTPS as described in [Tutorial task 1: Before you begin](#before-you-begin). Now, configure PingGateway to protect the sample MCP server:

1. In the `admin.json` file for PingGateway, [enable streaming](../reference/AdminHttpApplication.html#AdminHttpApplication-streamingEnabled):

   ```none
   "streamingEnabled": true
   ```

   PingGateway requires this setting for [server-side events (SSE)](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events), part of MCP.

2. Restart PingGateway to apply the change.

3. Add the following route to PingGateway updating `"properties"` as needed for your deployment:

   * Linux

     `$HOME/.openig/config/routes/mcp.json`

   * Windows

     `%appdata%\OpenIG\config\routes\mcp.json`

   ```json
   {
     "name": "mcp",
     "condition": "${find(request.uri.path, '^/mcp')}",
     "properties": {
       "amUrl": "https://myTenant.forgeblocks.com/am/",
       "amRealm": "/alpha",
       "gatewayUrl": "https://ig.example.com:8443",
       "mcpServerUrl": "http://localhost:8000"
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
           "url": "&{amUrl}",
           "realm": "&{amRealm}",
           "agent": {
             "username": "ig_agent",
             "passwordSecretId": "agent.secret.id"
           },
           "secretsProvider": "SecretsPasswords",
           "sessionCache": {
             "enabled": true
           }
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
                 "/mcp": "/"
               }
             }
           },
           {
             "type": "McpProtectionFilter",
             "config": {
               "resourceId": "&{gatewayUrl}/mcp",
               "authorizationServerUri": "&{amUrl}oauth2/realms/root/realms&{amRealm}",
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

   Source: [mcp.json](../_attachments/config/routes/mcp.json)

   Notice the following features of the route:

   * The sample route uses a base-64 encoded secret to connect to the AS. In production, don't include secrets in route files.

   * PingGateway acts as an OAuth 2.0 resource server (RS) when protecting the sample MCP server.

   * The [McpAuditFilter](../reference/McpAuditFilter.html) audits MCP requests. PingGateway records MCP audit events in an `audit/mcp.audit.json` file.

   * The [UriPathRewriteFilter](../reference/UriPathRewriteFilter.html) sends the request to the root resource of the MCP server. The MCP server expects requests at `/`.

   * The [McpProtectionFilter](../reference/McpProtectionFilter.html) uses the RS configuration, extending it for MCP.

   * PingGateway validates MCP requests with an [McpValidationFilter](../reference/McpValidationFilter.html).

   * The [ReverseProxyHandler](../reference/ReverseProxyHandler.html) uses a long `"soTimeout"` setting to accommodate an MCP agent receiving few or infrequent SSE updates.

   This simple route doesn't show [throttling](../reference/ThrottlingPolicies.html) or fine-grained access control. Add those features as needed to meet your security requirements.

4. Check the PingGateway log to verify the route loads successfully.

You have successfully configured PingGateway to protect the sample MCP server.

### Tutorial task 4: Start the MCP agent

In the directory where you unpacked the sample MCP agent, start the sample MCP agent again. This time, point it to the PingGateway route for MCP requests:

```console
$ python3 sample-mcp-agent.py --mcp-server-url https://ig.example.com:8443/mcp
```

You have successfully started the sample MCP agent.

## Validation

With PingGateway protecting the MCP server, the sample MCP agent directs you to the AS to sign on as an end user and authorize access to make MCP requests.

1. Copy the authorization URL the sample MCP agent now displays in your terminal window.

   The URL looks similar to `https://myTenant.forgeblocks.com/am/oauth2/realms/root/realms/alpha/authorize?response_type=code&client_id=…​`

2. In your browser's privacy or incognito mode, go to the authorization URL you copied.

3. Sign on with the end-user credentials (username: `demo` password: `Ch4ng3!t`) and consent to the requested `test` scope before closing the browser tab as prompted.

   You set these credentials when you [set up a demo user in PingOne Advanced Identity Cloud](../aic/preface.html#setup-user-idc).

4. In the terminal where the sample MCP agent runs, notice the available commands:

   ```none
   [INFO] Discovered tools [https://ig.example.com:8443/mcp]:
   [INFO] - geocode: Returns a list of objects containing city name, latitude, longitude, country, admin1 (region), and timezone for each matching city
   [INFO] - forecast_daily: Returns a multi-day weather forecast for a given location
   [INFO] - forecast_periods: Returns weather forecasts for each representative period of the current day
   [INFO] - forecast_hourly: Returns an hourly weather forecast for the current day
   [INFO] - weather_at_time: Returns the forecasted weather for a specific time at a given location

   Enter your message (or 'exit|quit|q'):
   ```

5. Enter a prompt and get a response from the MCP server through PingGateway, then exit the agent:

   The following example uses the `forecast_daily` tool to get the daily forecast for Tokyo:

   ```none
   Enter your message (or 'exit|quit|q'): What is the daily forecast for Tokyo?
   Agent: The daily forecast for Tokyo is:

   <MCP server response with forecast details>

   Enter your message (or 'exit|quit|q'): exit
   User requested exit. Goodbye!
   ```

   Find additional details about the MCP request in the PingGateway log.

You have successfully validated PingGateway can protect the MCP server.
