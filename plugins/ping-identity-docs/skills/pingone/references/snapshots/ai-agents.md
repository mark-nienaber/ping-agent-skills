---
title: AI agent logging and auditing
description: Use the Audit page to review information about AI agent events and actions in PingOne.
component: pingone
page_id: pingone:ai_agents:p1_ai_agent_logging
canonical_url: https://docs.pingidentity.com/pingone/ai_agents/p1_ai_agent_logging.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  steps: Steps
  result: Result
---

# AI agent logging and auditing

You can run reports to see a summary of AI agent events or actions performed in PingOne. Learn more in [Running an audit report](../monitoring/p1_running_audit_report.html).

You can find a complete list of events logged in PingOne in [Audit Reporting Events](https://developer.pingidentity.com/pingone-api/platform/reference/audit-reporting-events.html) in the PingOne API documentation.

## Steps

1. In the PingOne admin console, go to **Monitoring > Audit**.

2. Enter the report parameters:

   * **Time Range**: Limit the report results to a specified range of time.

     |   |                                                                                                                                                                                                                                                                                                                                                                                                                       |
     | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
     |   | Data up to 14 days old relative to the current date is available immediately. Data older than 14 days must be requested from the **Audit** page or using the API, and you can't request data for dates that are more than 2 years (730 days) before the current date. You can run reports a maximum of 14 days at a time. If you enter an invalid time range, you're prompted to adjust it before you run the report. |

   * **Selected Fields**: Specify which columns appear in the results list.

   * **Time Zone**: Specify which time zone to use in the results list. The timestamp shows the date and time for the selected time zone.

   * **Filter Type**: Select any of the following filter types to limit the results to AI agent activity and then select a filter. AI agent events use the application event types.

     | **Filter Type** | **Filter**                                                                                                                                                              |
     | --------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
     | **Application** | Select the AI agent for which you want to limit results.                                                                                                                |
     | **Event Type**  | Select any of the following to limit the event types to application-related event types:- **Application Created**

     - **Application Deleted**

     - **Application Updated** |
     | **Resource ID** | Paste the ID of an AI agent to limit results. You can find the ID on the **Overview** tab of the AI agent.                                                              |

     ![A screen capture of the Audit Parameters for AI agent events.](_images/p1_ai_agent_audit_parameters.png)

   * **Secondary Filter Type**: Specify a secondary filter to limit the results to a particular type, user, or resource. You must specify a primary filter type before you can select a secondary filter type.

3. Click **Run**.

## Result

Results display based on the parameters you selected. The following image shows results for AI agent events:

![A screen capture of the Audit Results for AI agent events.](_images/p1_ai_agent_audit_logging.png)

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | * The **Available Dates (UTC)** section lists the dates for the data that's available to query or has been requested.

* Depending on the number of days requested and the average number of events logged per day, the process can take from 2 to 24 hours. You can request a maximum of 14 days of data from within the data retention period and you can't request additional data while another request is pending.

  If you have a valid email address in PingOne, you'll be notified when the requested data is available. At that point, you can return to the **Audit** page and run queries against the data for the timeframe requested. The retrieved data is available for 14 days from the date of the retrieval request. |

---

---
title: AI Agents
description: Use AI Agents in PingOne.
component: pingone
page_id: pingone:ai_agents:p1_ai_agents
canonical_url: https://docs.pingidentity.com/pingone/ai_agents/p1_ai_agents.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  agent-identity-and-lifecycle: Agent identity and lifecycle
  delegation-not-impersonation: Delegation, not impersonation
  least-privilege-permissions: Least privilege permissions
  human-in-the-loop-hitl-approvals: Human-in-the-loop (HITL) approvals
  attribution-and-auditing: Attribution and auditing
---

# AI Agents

Artificial intelligence (AI) agents are non-human identities that perform actions on behalf of users or systems. In PingOne, registering these agents as first-class OAuth 2.0 identities enables you to manage who owns them, how they authenticate, and which tools and APIs they can access.

Learn more about agents in [What are AI agents?](https://developer.pingidentity.com/identity-for-ai/agents/idai-what-are-agents.html)

|   |                                                                                                                                                                                                                |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | AI agent capabilities in PingOne are available only with the Agent IAM Core solution package. Learn more in [Agent IAM Core solution package](../introduction_to_pingone/p1_introduction.html#agent_iam_core). |

## Agent identity and lifecycle

You can onboard, enable, update, and disable agents in PingOne. Each agent has a unique identity with its own credentials and lifecycle. This enables centralized management of your agents, their owners, and their resource permissions across your customer and workforce use cases. To manage AI agent owners, you can grant the applicable users with the **Application Owner** role and assign the required AI agents. Learn more in [Managing user roles](../directory/p1_manage_user_roles.html).

To get started, [add an AI agent](p1_managing_ai_agents.html).

## Delegation, not impersonation

To securely act on a user's behalf without impersonating them, agents use the OAuth 2.0 Token Exchange flow. The process works as follows:

* The agent presents the authenticated user's access token (the subject token) alongside its own client credentials (the actor token).

* PingOne evaluates the agent's identity, the user's consent, and the requested scopes to issue a new, downscoped access token.

* The delegation token contains an act (actor) claim, which clearly communicates to downstream resources that the agent is acting on behalf of a human user. The agent never sees the user's credentials.

Learn more in [Configuring OAuth 2.0 token exchange](../use_cases/p1_oauth_2_token_exchange.html).

## Least privilege permissions

The delegation token is short-lived and might require additional token exchanges as the agent performs new actions or accesses different resources. Audience restriction ensures the token is only valid at a specific resource server, preventing acceptance of unauthorized tokens. Resource and scope mappings enforce least-privilege access to backend APIs and MCP servers.

You can find an end to end use case for onboarding a digital assistant and enforcing access control in [Securing AI agents with PingOne and PingGateway](https://developer.pingidentity.com/identity-for-ai/identity/idai-securing-agents-pingone.html).

## Human-in-the-loop (HITL) approvals

If an agent needs to perform a high-risk action, such as transferring funds, PingOne can enforce a human-in-the-loop (HITL) approval. Using flows like client initiated backchannel authentication (CIBA), the agent's request is paused while the human user receives a push notification to explicitly approve or deny the action in real time.

Learn more about [configuring a CIBA flow](../use_cases/p1_configure_ciba_flow.html).

## Attribution and auditing

Because agents operate with their own unique identities and utilize delegation tokens, downstream systems and gateways can uniquely identify both the acting agent and the originating user. This generates a centralized audit trail of all agent-initiated activity, ensuring full accountability, traceability, and compliance.

Learn more in [AI agent logging and auditing](p1_ai_agent_logging.html).

---

---
title: Deleting AI agents
description: Delete AI Agents managed by PingOne.
component: pingone
page_id: pingone:ai_agents:p1_deleting_ai_agents
canonical_url: https://docs.pingidentity.com/pingone/ai_agents/p1_deleting_ai_agents.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  steps: Steps
---

# Deleting AI agents

Use the **AI Agents** page to delete artificial intelligence (AI) agents managed by PingOne.

## Steps

1. In the PingOne admin console, go to **AI Agents**.

   You can search for agents or filter your search to a particular AI agent.

2. Click the **More Options** (⋮) icon on the AI agent entry you want to delete and click **Delete**.

3. In the **Delete** modal, click **Delete**.

---

---
title: Managing AI agents
description: Add or edit AI Agents in PingOne.
component: pingone
page_id: pingone:ai_agents:p1_managing_ai_agents
canonical_url: https://docs.pingidentity.com/pingone/ai_agents/p1_managing_ai_agents.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 13, 2026
section_ids:
  before-you-begin: Before you begin
  adding-an-ai-agent: Adding an AI agent
  steps: Steps
  next-steps: Next steps
  p1_edit_ai_agent: Editing an AI agent
  steps-2: Steps
---

# Managing AI agents

Use the **AI Agents** page to add and edit artificial intelligence (AI) agents to be managed by PingOne. Learn more in [AI Agents](p1_ai_agents.html).

## Before you begin

Ensure you have a license for the [Agent IAM Core solution package](../introduction_to_pingone/p1_introduction.html#agent_iam_core).

|   |                                                                                                                                              |
| - | -------------------------------------------------------------------------------------------------------------------------------------------- |
|   | If you don't have this license, the **AI Agents** page provides an option to unlock AI agent capabilities by contacting Ping Identity Sales. |

## Adding an AI agent

Add an AI agent to register the agent with a unique identity and manage its authentication settings and access to resources.

### Steps

1. In the PingOne admin console, go to **AI Agents** and click the **[icon: plus, set=fa]**icon.

2. Enter the following:

   * **Name**: A unique identifier for the AI agent.

   * **Description** (optional): A brief description of the agent, such as `Retail Chatbot` or `Workforce Assistant`.

   * **Icon** (optional): A graphic representation of the AI agent. Use a file up to 1 MB in JPG, JPEG, GIF, or PNG format.

3. Click **Save**.

### Next steps

Complete the configuration steps in [Editing an AI agent](#p1_edit_ai_agent).

## Editing an AI agent

Edit an AI agent to configure its authentication settings and access to resources.

### Steps

1. In the PingOne admin console, go to **AI Agents** and browse or search for the AI agent you want to edit.

2. Click the AI agent entry to open the details panel.

3. On the **Overview** tab, click the **Pencil** icon ([icon: pencil, set=fa]) and enter or edit the following:

   | Field           | Description                                                                                       |
   | --------------- | ------------------------------------------------------------------------------------------------- |
   | **Name**        | The name for the AI agent.                                                                        |
   | **Description** | A brief description of the AI agent.                                                              |
   | **Icon**        | A graphic representation of the AI agent. Use a file up to 1 MB in JPG, JPEG, GIF, or PNG format. |

4. Click **Save**.

5. On the **Configuration** tab, click [icon: pencil, set=fa]and enter or edit the following:

   | Field                                              | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
   | -------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | **Response Type**                                  | Select **Code**, **Access Token**, or **ID Token** for the response type.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
   | **Grant Type**                                     | Select **Authorization Code**, **Implicit**, **Client Credentials**, **CIBA**, **Device Authorization**, **Refresh Token**, or **Token Exchange** for the grant type.Learn more in [Grant types](../applications/p1_grant_types.html).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
   | **PKCE Enforcement**                               | Select a value for PKCE code challenge enforcement. This value determines how the AI agent creates the code challenge from the code verifier.Learn more in [PKCE enforcement](../applications/p1_pkce_enforcement.html).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
   | **Refresh Token** configuration                    | Select this option to enable the **Refresh Token** grant type. You can specify the following:- **Refresh Token Format**

     The type of refresh token PingOne issues for the AI agent in exchange for an expired access token:

     * **Opaque Token**: Contains a unique, unreadable string and doesn't require a digital signature. This will be the only refresh token type issued after March 1, 2027.

     * **JSON Web Token**: Contains claims and information about the user's authentication status, and requires a digital signature. This option is only available until March 1, 2027, after which it will be deprecated.

     Learn more about the timeline for JWT deprecation in [Refresh tokens](../applications/p1_refresh_tokens.html).

   - **Refresh Token Duration**

     The lifetime of the refresh tokens. The default value is 30 days. Valid values are between 60 seconds and 1826 days (for **Opaque Token**).

   - **Refresh Token Rolling Duration**

     How long the AI agent can use the refresh token grant type to obtain a new access token and a new refresh token after the most recent user authentication event. The default value is 180 days. Valid values are between 60 seconds and 1826 days (for **Opaque Token**).&#xA;&#xA;Refresh Token Rolling Duration must be longer than or equal to the Refresh Token Duration.- **Refresh Token Rolling Grace Period**

     The amount of time that a rolled refresh token remains valid if the client failed to receive an updated one during a roll. Valid values are between 0 and 86,400 seconds (24 hours). A value of `0` means that a refresh token becomes invalid after it's rolled.                                                                          |
   | **Redirect URIs**                                  | The address to which PingOne forwards the OIDC response after authentication.&#xA;&#xA;The Redirect URI can't contain a fragment component, such as #somedata. Learn more in Redirection endpoint in the IETF documentation.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
   | **Allow Redirect URI Patterns**                    | Use a wildcard for flexibility in managing redirect URIs. Learn more in [Redirect URIs](../applications/p1_wildcard_redirect_uri.html).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
   | **Token Endpoint Authentication Method**           | Select one of the following:- **None**

   - **Client Secret Basic**

   - **Client Secret Post**

   - **Client Secret JWT**

   - **Private Key JWT**Learn more in [Token endpoint authentication methods](../applications/p1_token_endpoint_authentication_methods.html).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
   | **Require Pushed Authorization Request**           | Require the AI agent to send its authorization requests directly to PingOne without going through the browser. Requiring this can safeguard sensitive information from end-user devices. If **Require Pushed Authorization Request** isn't selected, the AI agent can send plain authorization requests or pushed authorization requests. Learn more in [Pushed authorization requests](../applications/p1_pushed_authorization_request.html).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
   | **Pushed Authorization Request Reference Timeout** | Specify how long the pushed authorization request should be valid. The default value is 60 seconds.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
   | **Additional Refresh Token Replay Protection**     | Outside of the optional rolling grace period, refresh tokens are intended for one-time use. For increased security, enable this option so that PingOne can invalidate both access and refresh tokens when a refresh token is reused. Learn more in [Refresh token rotation](../applications/p1_refresh_token_rotation.html).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
   | **Initiate Login URI**                             | The AI agent's login initiation endpoint for third parties to begin the sign-on process.If provided, PingOne redirects users to this URI to initiate sign-on (SSO) to PingOne. The AI agent is responsible for implementing the relevant OIDC flow when the **Initiate Login URI** is requested.Learn more in [Initiating Login from a Third Party](https://openid.net/specs/openid-connect-core-1_0.html#ThirdPartyInitiatedLogin) in the OIDC specification. This URI is required if you want the AI agent to show in the PingOne application portal. Learn more in [Application portal](../applications/p1_application_portal_showing_applications.html).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
   | **Target Link URI**                                | The URI for the AI agent. If provided, PingOne redirects AI agent users to this URI after the user is authenticated.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
   | **Signoff URLs**                                   | The URLs to which the browser can be redirected after user signs off from the AI agent.If you include a `post_logout_redirect_uri` query parameter in the `/signoff` request, with the same value that was set in the AI agent, the browser will redirect the user to the matching URL.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
   | **Request Parameter Signature Requirement**        | Specify how the AI agent sends the optional `request` parameter in its authorization requests.Click **Compare Options** for a description of the different settings.- **Default**: Allow the AI agent to send authorization requests with or without the `request` parameter. If using the request parameter, the AI agent must include a digital signature.

   - **Require signed request parameters**: Requires the AI agent to use the `request` parameter and include a digital signature of it in its authorization requests.

   - **Allow unsigned request parameters**: Allows the AI agent to send authorization requests with or without the `request` parameter. If using the `request` parameter, including a digital signature is optional for the AI agent.Learn more in [Request Parameter Signature Requirement](../applications/p1_request_parameter_signature_requirement.html).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
   | **Token Header Options**                           | Select **Include the x5t parameter in the header of access tokens, ID tokens, and JWT-based refresh tokens** if the AI agent, custom resource, or both require the `x5t` parameter in the digital signature verification process. The `x5t` parameter acts as a fingerprint for the X.509 certificate and provides increased security by identifying the specific key used to sign the token.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
   | **ID Token Duration**                              | The lifetime of the ID token. A duration of 1 hour or less is recommended.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
   | **PingOne API Access Token Duration**              | The lifetime of the PingOne API access token. A duration of 1 hour or less is recommended. This setting is applicable only if this AI agent is allowed to request PingOne API scopes.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
   | **OpenID Connect Session Management**              | Facilitate OIDC session management by allowing AI agents in the same browsing mode, such as private or normal browsing mode, to monitor the PingOne user session. Only AI agents running in the same browsing mode can monitor the PingOne user session.To use this option, your PingOne environment must be configured with a custom domain, such as `sso.example.com`, and the AI agents must be accessible under that domain. For example, `apps.example.com/app1` and `apps.example.com/app2` or `app1.example.com` and `app2.example.com`. Learn more in [Setting up a custom domain](../settings/p1_set_up_custom_domain.html).When enabled, the `session_state` parameter is included in the PingOne authorization response with the session status, such as `unchanged`, `changed`, or `error`. Learn more in [OIDC session management](https://developer.pingidentity.com/pingone-api/foundations/authentication-concepts/oidc-session-management.html) in the PingOne API documentation and [Best practices: Session management](https://docs.pingidentity.com/solution-guides/best_practice_guides/bp_session_mgmt.html).&#xA;&#xA;The default idle timeout is 30 days. To set a shorter idle timeout of fewer than 30 days:&#xA;&#xA;Build a PingOne DaVinci flow that includes the Return Success Response (Redirect Flows) node from the PingOne Authentication connector.&#xA;&#xA;In the Return Success Response (Redirect Flows) node, set the Idle Timeout value to the desired amount of time, such as 5 minutes.&#xA;&#xA;Assign the flow to the applicable AI agents.&#xA;&#xA;If a user session is deleted because of a PingOne session API request or is purged by the system, it doesn't trigger a changed response. |
   | **Request scopes to access multiple resources**    | Enable this option to allow the AI agent to request scopes from multiple custom resources in a single request.To use this option, any custom resources that the AI agent requests access to must have the following configurations across all requested [custom resources](../applications/p1_editresource.html):- **Overview** tab: **Access token time to live** must be set to the same value.

   - **Attributes** tab: The mapping configuration of the `sub` attribute must be the same.

   - **Attributes** tab: Any other attribute using the same name in multiple custom resources must have the same mapping configurations.

   - **Scopes** tab: The scope names must be unique so that PingOne can determine which custom resource and associated scope that the AI agent is attempting to access.

   - **Permissions** tab: For environments with PingOne Authorize, permissions names must be unique if [Include user permissions in access tokens](../applications/p1_application_permissions.html#p1-permissions-access-tokens) is enabled.If any of these configurations aren't consistent across the requested custom resources, the request results in an error.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
   | **Terminate User Session by ID Token**             | Enable this option to allow the AI agent to send requests for PingOne to terminate end-user sessions at the `/idpSignoff` endpoint using only the ID token.The audience claim value in the ID token must match the client ID of the AI agent so that PingOne can identify the session to be terminated. The AI agent isn't required to have access to the session token cookie.Learn more in the [PingOne API documentation](https://developer.pingidentity.com/pingone-api/auth/openid-connect-oauth-2/idp-signoff.html).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
   | **CORS Settings**                                  | Specifies the CORS options for the AI agent. Learn more in [Cross-origin resource sharing](../applications/p1_cors.html).- **Allow any CORS-safe origin** (default): Allows the AI agent to access resources from a domain that is CORS-safelisted, according to the [Fetch specification](https://fetch.spec.whatwg.org/#cors-safelisted-request-header).

   - **Allow specific origins**: Allows the AI agent to access resources from a specific domain.

     * **Allowed origins**: Specifies the allowed origin domains for CORS. You can specify a domain pattern or a valid IPv4 address. If you use a domain pattern, you can specify one wildcard to match incoming requests.

       &#xA;&#xA;You can't use the wildcard on the domain name.&#xA;&#xA;For example, the following search patterns are valid:&#xA;&#xA;https\://\*.test.com&#xA;&#xA;https\://www\.app\*.test.com&#xA;&#xA;The following patterns are not valid:&#xA;&#xA;https\://test\*.com&#xA;&#xA;https\://www\.app.test\*.com

   - **Disallow all origins**: Don't allow the AI agent to access resources from a cross-origin domain.&#xA;&#xA;After you make changes to the CORS Settings, it can take several minutes for the new settings to take effect, due to time-to-live configuration on the resource.                                                                                                                                                                                                                                                                                                                                                                                                                                                        |

6. On the **Resources** tab, click [icon: pencil, set=fa]and select the checkboxes to add appropriate OAuth scopes for the AI agent. Click the **Selected scopes** tab to see the scopes that are currently selected for the AI agent.

   The OAuth scopes determine the resources that the AI agent can access. If you add OIDC scopes here, the AI agent inherits the attributes associated with that scope.

   If the AI agent uses the refresh token grant type, add the `offline_access` scope to enable the AI agent to request a refresh token from PingOne on a per-request basis. For example, when the AI agent needs a refresh token, it includes the `offline_access` scope in its request, and PingOne includes a refresh token in its token response. However, when the AI agent doesn't need a refresh token, it doesn't include the scope in the request, and PingOne therefore doesn't include a refresh token in its token response.

   If the `offline_access` scope is not added to an AI agent that uses the refresh token grant type, PingOne always includes a refresh token in its token response, whether the AI agent needs a refresh token or not.

   To customize the lifetime of access tokens for AI agents, you must configure a custom resource, set the desired access token lifetime, and then add those scopes to the AI agent. Learn more in [Customizing access token lifetime](../applications/p1_customizing_access_token_lifetime.html).

7. On the **Policies** tab, click [icon: pencil, set=fa]and select the authentication policies for the AI agent.

   If you have a DaVinci license, you can select PingOne policies or DaVinci flow policies, but not both. If you don't have a DaVinci license, you'll see PingOne policies only.

   To add one or more PingOne authentication policies, click the **PingOne Policies** tab. If the AI agent was previously configured with one or more DaVinci flow policies, click **Deselect all other Policies** to remove them from the AI agent, then select the PingOne authentication policies you want to apply to the AI agent. PingOne authentication policies are applied in the order in which they appear in the list. Click the **Selected PingOne Policies** tab, reorder the policies as needed, then click **Save**.

   To add one or more DaVinci flow policies, click the **DaVinci Policies** tab. If the AI agent was previously configured with one or more PingOne authentication policies, click **Deselect all other Policies** to remove them from the AI agent, then select the DaVinci flow policies you want to apply to the AI agent. PingOne applies the first DaVinci flow policy in the list. Click the **Selected DaVinci Policies** tab, reorder the policies as needed, then click **Save**.

   For OAuth-based AI agents, you can specify another policy in the `acr_values` parameter in the authorization request. The `acr_values` parameter specifies the sign-on policies that PingOne should use for authentication. You can include any policies assigned to the AI agent. Specify either a single DaVinci policy by flow policy ID or one or more PingOne policies by name, separated by spaces or the encoded space character `%20`. For example, `acr_values=d1210a6b0b2665dbaa5b652221badba2` or `acr_values=Single_Factor%20Multi_Factor`.

   Learn more in [Authentication policies for applications](../applications/p1_auth_policies_for_applications.html).

8. Click **Save**.

9. On the **Attribute Mappings** tab, click [icon: pencil, set=fa], select a PingOne user attribute, and map it to an attribute in the AI agent that you're adding.

   Learn more in [Customizing OIDC attributes for an application](../applications/p1_customizing_oidc_attributes_for_application.html).

   1. Enter an AI agent attribute and then select the corresponding PingOne attribute in the list.

   2. Click the **Gear** icon ([icon: gear, set=fa]) to use the expression builder to build an attribute mapping.

      Learn more in [Using the expression builder](../pingone_expression_language/p1_use_expression_builder.html).

10. Click **Save**.

11. On the **Access** tab, click [icon: pencil, set=fa]and enter or edit the following:

    | Field                          | Description                                                                                                                                                                                                                                                                    |
    | ------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
    | **Application Portal Display** | Determines whether an AI agent icon appears in the application portal, even if the user would see the AI agent in the application portal based on the group membership policy. Learn more in [Application access control](../applications/p1_application_access_control.html). |
    | **Admin Only Access**          | Specifies that a user with an administrator role is required to access the application. The user must have one of the following roles:- `Organization Admin`

    - `Environment Admin`

    - `Identity Data Admin`

    - `Client Application Developer`                                 |
    | **Group Membership Policy**    | Select the group membership policy for the AI agent. Learn more in [Groups](../directory/p1_groups.html).                                                                                                                                                                      |

12. Click **Save**.

13. (Optional) For workforce MFA use cases, to connect the AI agent to your PingFederate instance, download the AI agent properties file and upload it to the relevant PingID adapter instance in PingFederate.

    Learn more in [Configuring a PingID adapter instance](https://docs.pingidentity.com/pingid/pingid_integrations/configuring_a_pid_adapter_instance.html).

14. Click **Save**.

15. To enable the AI agent, click the toggle at the top of the details panel to the right (blue).

    You can disable the AI agent by clicking the toggle to the left (gray).

    |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
    | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
    |   | If you selected **Response Type = Code** and **Grant Type = Authorization Code**, there is also an **Integrate** tab that you can use to test your configuration. Generate code snippets from this tab and copy them into a web application so that you can ensure that the authorization and authentication configuration is working as intended.Learn more in [Integrate PingOne with a Node.js Express app](../pingone_tutorials/p1_tutorial_integrate_nodejs_express_app.html) and [Integrate Ping SDK for JavaScript with PingOne](https://docs.pingidentity.com/sdks/latest/sdks/tutorials/javascript/index.html). |

---

---
title: Viewing AI agents
description: View AI Agents in PingOne.
component: pingone
page_id: pingone:ai_agents:p1_viewing_ai_agents
canonical_url: https://docs.pingidentity.com/pingone/ai_agents/p1_viewing_ai_agents.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  steps: Steps
  result: Result:
---

# Viewing AI agents

Use the **AI Agents** page to view details for artificial intelligence (AI) agents managed by PingOne.

|   |                                                                                                                                                                                                                |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | AI agent capabilities in PingOne are available only with the Agent IAM Core solution package. Learn more in [Agent IAM Core solution package](../introduction_to_pingone/p1_introduction.html#agent_iam_core). |

## Steps

1. In the PingOne admin console, go to **AI Agents**.

   You can search for agents or filter the list to find a specific AI agent.

   ### Result:

   The **AI Agents** page displays a list of configured AI agents.

2. To open the details panel for a specific AI agent, click the agent entry.

   The AI agent details panel includes the following tabs:

   * Overview

     **General Settings**

     General information about the AI agent. Use this section to see AI agent details at a glance.

     * **Name**: The name of the AI agent.

     * **ID**: The unique identifier for the AI agent.

     * **Description**: A brief description of the AI agent.

     * **Environment ID**: The environment where the AI agent is configured.

     * **Client ID**: A unique identifier for the application. You might need this value to obtain an access token or integrate the AI agent. Keep this value confidential.

     * **Client Secret**: A shared secret used for authentication and integration. Keep this value confidential.

     * **Generate New Secret**: Update the client secret and select how long to retain the previous secret in the confirmation modal.

     * **Get Access Token**: View or copy the access token for the AI agent. Learn more in [Getting an access token](../applications/p1_getaccesstoken.html).

     **Connection Details**

     Endpoints used to set up or configure the AI agent.

     * **OIDC Discovery Endpoint**

     * **Initiate Single Sign-On URL**

   * Configuration

     Configuration settings that control authentication, redirects, and security behavior.

     **OIDC Settings**

     * **Token Auth Method**: Client Secret Basic

     * **Response Type**: Code

     * **Grant Types**:

       * Token Exchange

       * CIBA

       * Authorization Code

     * **PKCE Enforcement**

     **Redirect Settings**

     * **Redirect URIs**

     * **Allow Redirect URI Patterns**

     **Security**

     * **JSON Web Key Set**

     * **Signing Key**

   * Resources

     Scopes that the AI agent can request.

   * Policies

     Authentication policies that determine how user identities are verified when accessing the AI agent.

   * Attribute Mappings

     Associations between PingOne user attributes and OIDC attributes in the AI agent.

   * Access

     User groups that are allowed to access the AI agent.

   * Integrate

     Third-party applications that are integrated with the AI agent.