---
title: Authentication
description: How authentication works in the AIC MCP Server, including OAuth 2.0 PKCE and Device Code flows.
component: build-with-ai
page_id: build-with-ai:aic-mcp-server:authentication
canonical_url: https://developer.pingidentity.com/build-with-ai/aic-mcp-server/authentication.html
llms_txt: https://developer.pingidentity.com/build-with-ai/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: April 20, 2026
keywords: ["MCP", "authentication", "OAuth", "PKCE", "Device Code", "AIC"]
section_ids:
  local-deployment-pkce: Local deployment (PKCE)
  docker-deployment-device-code: Docker deployment (Device Code)
  authentication-constraints: Authentication constraints
---

# Authentication

The AIC MCP Server uses human-centric authentication to ensure all actions are traceable to an individual user.

## Local deployment (PKCE)

When running the AIC MCP Server locally, the server uses the OAuth 2.0 Authorization Code flow with PKCE (Proof Key for Code Exchange):

![PKCE authentication flow diagram showing the four phases: first tool use, token storage, automatic reuse, and auto re-authentication](_images/pkce-auth-flow.svg)

* 1 First tool use

  Your browser opens automatically for user login at PingOne Advanced Identity Cloud when you use a tool for the first time in a session.

* 2 Token storage

  Access tokens are stored securely in the OS keychain:

  * macOS Keychain

  * Windows Credential Manager

  * Linux Secret Service (Freedesktop.org API)

* 3 Automatic reuse

  Cached tokens are used for subsequent tool calls within the same session.

* 4 Auto re-authentication

  When tokens expire during a session, your browser opens again for a new login.

|   |                                                                                                                                                                                                                                                                                                              |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | **Administrator access required:** The AIC MCP Server requires administrative authentication and provides administrative capabilities to your PingOne Advanced Identity Cloud development and sandbox environments. All operations are performed as the authenticated administrator and are fully auditable. |

## Docker deployment (Device Code)

When running in a Docker container, the server uses the OAuth 2.0 Device Code Flow:

1. When authentication is required, your MCP client displays a URL and a code.

2. Open the URL in your browser and enter the code.

3. Accept the prompt in your client.

4. Tokens are stored ephemerally in the container filesystem and deleted on container restart.

|   |                                                                                                                                                          |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Docker deployment uses MCP form elicitation for the Device Code Flow. This requires MCP client support for form elicitation, which is currently limited. |

## Authentication constraints

The AIC MCP Server enforces several authentication constraints by design:

* **Human-centric only:** Only authentication flows that tie actions to an individual human are supported. Client credentials and non-interactive flows are explicitly forbidden.

* **No static secrets:** The server does not allow configuration with or storage of a static `client_secret`.

* **Tokens never stored in plain text:** All tokens are stored in the OS encrypted keychain (local) or ephemerally in memory (Docker). Tokens are never written to disk in plain text files, logs, or shell history.

* **Reauthentication on startup:** Each time the server starts, a fresh authentication is required.

* **Sandbox and Development only:** The AIC MCP Server configurations are only available in Development and Sandbox tenants.
