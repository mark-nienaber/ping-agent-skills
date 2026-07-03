---
title: Authentication
description: How authentication works in the DaVinci MCP Server, including OAuth 2.0 PKCE flow, token storage, and regional configuration.
component: build-with-ai
page_id: build-with-ai:davinci-mcp-server:authentication
canonical_url: https://developer.pingidentity.com/build-with-ai/davinci-mcp-server/authentication.html
llms_txt: https://developer.pingidentity.com/build-with-ai/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 1, 2026
keywords: ["MCP", "authentication", "OAuth", "PKCE", "PingOne", "DaVinci", "keychain"]
section_ids:
  authentication-flow: Authentication flow
  worker-application-requirements: Worker application requirements
  regional-and-custom-domain-support: Regional and custom domain support
  authentication-constraints: Authentication constraints
  troubleshooting: Troubleshooting
---

# Authentication

The DaVinci MCP Server uses OAuth 2.0 Authorization Code flow with PKCE (Proof Key for Code Exchange) to ensure all actions are traceable to an individual PingOne user.

## Authentication flow

![DaVinci MCP tools diagram](_images/mcp-tools-diagram.png)

* 1 Tool discovery

  Your MCP client connects to the DaVinci MCP Server and discovers the available tools in the `davinci_admin` collection.

* 2 Tool request from the AI agent

  When you ask for DaVinci data (for example, flows or applications), the AI agent chooses the appropriate tool and sends a tool call to the server.

* 3 User authentication and token retrieval

  If no valid token exists, the server opens your browser for PingOne login and completes the OAuth 2.0 PKCE flow through `http://127.0.0.1:7474/callback`.

* 4 DaVinci API execution

  After authentication, the server calls the corresponding DaVinci APIs using your user context and returns structured results.

* 5 Response returned to the MCP client

  The server sends the tool response back to your MCP client, and your assistant presents it in natural language.

|   |                                                                                                                                                  |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | Port `7474` must be available on `localhost` for the OAuth callback to succeed. If another process is using this port, authentication will fail. |

## Worker application requirements

The DaVinci MCP Server requires a PingOne worker application configured as a public client with PKCE. During token exchange, no `client_secret` is used.

The worker application must have:

* **Grant Types:** `Authorization Code`

* **Response Type:** `Code`

* **PKCE Enforcement:** `S256_REQUIRED`

* **Redirect URIs:** `http://127.0.0.1:7474/callback`

* **Token Endpoint Authentication Method:** `None`

For step-by-step setup instructions, refer to [Try it out](getting-started.html).

## Regional and custom domain support

The server connects to PingOne using the `ROOT_DOMAIN` environment variable. Set it to match your PingOne region:

| Region        | Value                            |
| ------------- | -------------------------------- |
| North America | `pingone.com`                    |
| Europe        | `pingone.eu`                     |
| Asia Pacific  | * `pingone.asia`

* `pingone.au` |
| Singapore     | `pingone.sg`                     |

If your organization uses a custom PingOne domain, set `CUSTOM_DOMAIN` to override the default. `ROOT_DOMAIN` selects the region, while `DAVINCI_MCP_ENVIRONMENT_ID` selects the specific environment within that region.

## Authentication constraints

The DaVinci MCP Server enforces the following authentication constraints:

* **Human-centric only:** Only browser-based flows that tie actions to an individual user are supported. Client credentials and non-interactive flows are not permitted.

* **No static secrets:** The server does not accept or store a static `client_secret`.

* **Tokens never stored in plain text:** All tokens are stored in the OS encrypted keychain. Tokens are never written to disk in plain text files, logs, or shell history.

## Troubleshooting

* **Port conflict**

  The callback server uses port `7474`. If authentication fails immediately, check whether another process is using this port.

* **Authentication timeout**

  The browser login must be completed within 5 minutes. If it times out, restart the tool call to trigger a new login.

* **Invalid or corrupted tokens**

  Use the `--logout` flag to clear stored tokens from the keychain and start again:

  ```bash
  npx -y @ping-identity/davinci-mcp-server start --logout
  ```

* **Keychain access on Linux**

  Ensure `libsecret` is installed for `keytar` to access the Linux Secret Service.
