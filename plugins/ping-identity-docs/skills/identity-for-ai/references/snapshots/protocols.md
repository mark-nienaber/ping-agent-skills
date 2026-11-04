---
title: AuthPlayground
description: Explore OAuth 2.0 extension protocols through an enterprise AI scenario in the AuthPlayground.
component: identity-for-ai
page_id: identity-for-ai:protocols:authplayground
canonical_url: https://developer.pingidentity.com/identity-for-ai/protocols/authplayground.html
llms_txt: https://developer.pingidentity.com/identity-for-ai/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-08-26T20:20:14Z
keywords: ["Identity for AI", "OAuth 2.0 protocols", "AuthPlayground"]
---

# AuthPlayground

The AuthPlayground is an interactive visualization tool for exploring OAuth 2.0 extension protocols using a realistic enterprise AI scenario. The playground simulates interactions between a user, an AI agent, and various backend services, showing you real HTTP requests and responses along with decoded JSON Web Tokens (JWT) so you can inspect every claim.

Whether you're evaluating a new identity architecture, onboarding an engineer to modern OAuth patterns, or trying to understand why your token exchange request returns a 400, the playground provides a controlled environment for experimenting with these questions.

[icon: circle-info, set=far, size=3x]

#### [Key concepts](authplayground-concepts.html)

Understand key concepts behind the playground

[icon: rocket_launch, set=material, size=3x]

#### [Get started](authplayground-getting-started.html)

Learn how to use the playground

[icon: play_circle, set=material, size=3x]

#### [Launch the playground](https://www.authplayground.dev)

Explore the AuthPlayground

---

---
title: AuthPlayground concepts
description: Explore OAuth 2.0 protocols, trust boundaries, identities, and authorization controls for enterprise AI workflows in the AuthPlayground.
component: identity-for-ai
page_id: identity-for-ai:protocols:authplayground-concepts
canonical_url: https://developer.pingidentity.com/identity-for-ai/protocols/authplayground-concepts.html
llms_txt: https://developer.pingidentity.com/identity-for-ai/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-08-26T20:20:14Z
keywords: ["Identity for AI", "OAuth 2.0 protocols", "OAuth 2.0", "enterprise AI", "trust boundaries", "AI security", "AuthPlayground"]
section_ids:
  the-enterprise-ai-problem: The enterprise AI problem
  the-meeting-preparation-scenario: The meeting preparation scenario
  identities-in-the-workflow: Identities in the workflow
  understanding-the-architecture: Understanding the architecture
  layer-1-user-and-ai-assistant: "Layer 1: User and AI assistant"
  layer-2-mcp-tools-agents-and-other-workloads: "Layer 2: MCP tools, agents, and other workloads"
  layer-3-downstream-enterprise-systems: "Layer 3: Downstream enterprise systems"
  trust-boundaries: Trust boundaries
  what-can-go-wrong: What can go wrong?
  securing-the-workflow-with-the-right-controls: Securing the workflow with the right controls
  key-takeaways: Key takeaways
  next-steps: Next steps
---

# AuthPlayground concepts

Enterprise AI becomes easier to understand when you consider the trust problems protocols solve. The [AuthPlayground](https://www.authplayground.dev) lets you explore OAuth 2.0 extension protocols using a common enterprise scenario.

|   |                                                                                                                                       |
| - | ------------------------------------------------------------------------------------------------------------------------------------- |
|   | Ready to jump right into the playground? Learn how in [Getting started with the AuthPlayground](authplayground-getting-started.html). |

## The enterprise AI problem

Imagine you're the Chief Architect at an enterprise company. Over the past year, the company has moved from isolated experiments with AI to a company-wide initiative:

* Sales wants AI to prepare account teams for customer meetings

* Support wants AI to summarize cases and highlight risk

* Engineering wants coding assistants

* HR wants policy assistants

* Finance wants AI to analyze spending trends

You face two competing directives:

1. The Chief Executive Officer (CEO) wants to use AI to make every employee more productive.

2. The Chief Information Security Officer (CISO) requires that every AI action remains secure, attributable, governed, and auditable.

These goals can be hard to reconcile. Enterprise AI is more than connecting a Large Language Model (LLM) to a few APIs. You must preserve identity, authorization, context, and accountability as AI acts across systems and services, on behalf of people or under its own machine authority.

### The meeting preparation scenario

Consider Sarah, a Senior Account Executive at your company. The night before an important customer meeting, she opens the company's AI assistant and asks:

`Prepare me for tomorrow's Apex Logistics meeting.`

For Sarah, this is one request. But behind the scenes, the AI assistant might need to:

* Read the Apex Logistics opportunity in Salesforce

* Retrieve open ServiceNow support cases

* Search relevant communications in Microsoft 365

* Analyze customer data in Salesforce and Databricks

* Review engineering Jira issues

* Generate a meeting briefing

* Potentially perform follow-up actions

One human request becomes a multi-step, multi-system workflow:

![Diagram showing the request from Sarah to the AI assistant, MCP servers, and resources.](_images/authplayground-multi-step-workflow.png)

Sarah doesn't need to understand this complexity, but the enterprise architecture must.

### Identities in the workflow

Sarah is the human identity. Non-Human Identities (NHI) might include an AI assistant, an AI agent, a Model Context Protocol (MCP) server, and other internal services. In this context, NHIs are workloads, or software performing work. Just like Sarah, workloads need identities to authenticate and be authorized.

The human and workload identity distinction matters because the enterprise needs to answer two different questions:

1. Which human initiated the activity?

2. Which software workload is performing the activity?

Sometimes, a human isn't involved. An autonomous monitoring agent, retrieval agent, or background telemetry service might operate under its own machine authority.

There are two patterns to keep in mind:

![Diagram showing the human-initiated and automous patterns.](_images/authplayground-human-autonomous-patterns.png)

Delegation is relevant when a workload exercises authority involving another principal. Workload identity doesn't depend on delegation when workloads exercise autonomous authority.

## Understanding the architecture

To handle complex workflows such as Sarah's, it helps to picture the architecture in three layers.

### Layer 1: User and AI assistant

This is how the workflow begins:

1. Sarah signs on, opens the AI assistant, and asks for help.

2. The enterprise establishes Sarah's human identity.

3. The AI assistant acts as the orchestrator. It interprets Sarah's request, determines the required work, and coordinates the work.

Knowing that Sarah authenticated is only the beginning. The enterprise must determine which software is executing, whose authority is involved, and what the software is allowed to do.

### Layer 2: MCP tools, agents, and other workloads

The AI assistant can invoke specialized workloads to perform parts of the job. For example, a planner agent might determine which information is required. A retrieval agent might gather that information. An MCP tool or gateway might provide controlled connectivity to an enterprise API.

![Diagram showing the workload workflow from AI assistant, Planner Agent, and Retrieval Agent to the MCP Gateway.](_images/authplayground-workload-chain.png)

These are software workloads participating in execution. Some operate under their own machine authority. Others participate in an operation involving delegated human authority. Some cross into another authorization domain. Others continue through a chain of internal services. These differences determine which security controls are appropriate.

### Layer 3: Downstream enterprise systems

These are the systems (such as Salesforce, ServiceNow, Databricks, Jira, Microsoft 365, or internal APIs) that hold enterprise data or perform business actions. Each system protects its own resources and can have its own authorization requirements.

Sarah's authentication to the AI assistant doesn't automatically mean that every downstream system accepts whatever credential the assistant presents. The target system must decide whether the requested operation is allowed.

### Trust boundaries

A trust boundary is a point where one security or authorization domain must decide whether to trust and allow a request coming from another context. For example:

![Diagram showing the AI workflow on one side of the trust boundary and Salesforce on the other side.](_images/authplayground-trust-boundary.png)

Crossing that boundary raises questions such as:

* Who authenticated the principal (Sarah)?

* Which workload is acting?

* Is delegated authority involved?

* Is the credential intended for this authorization domain?

* Which resource is being requested?

* What permissions should apply?

* Should the target system allow the operation?

Because of these boundaries, enterprise AI can't be secured with user authentication alone. The architecture must preserve enough trusted context for each system to make the decisions it owns.

### What can go wrong?

Without the right controls, several problems emerge.

* Generic service accounts hide accountability

  When every MCP tool uses a powerful service account, you can't tell who updated a record, for example in Salesforce. Important context is lost. When human delegation is involved, the enterprise must understand both the principal behind the request and the software actor performing the action.

* One user token becomes a universal key

  It's tempting to forward Sarah's original token everywhere. But a token issued for one application, audience, or resource shouldn't automatically become valid across every enterprise system. Salesforce, ServiceNow, and other systems can have different authorization and trust requirements.

* Powerful workload credentials create their own risk

  Giving software an identity doesn't mean giving it unlimited authority. An AI workload can have a legitimate identity and still request something it shouldn't be allowed to do.

  * Identity answers the question: Who is this?

  * Authorization answers: What is it allowed to do?

  * When delegation is involved, there's another question: What is it allowed to do using authority associated with this principal?

* Too much approval destroys usability

  The opposite extreme is to ask Sarah to approve every individual action. Approve Salesforce, then approve ServiceNow, then approve another internal service. This can cause approval fatigue and undermine the productivity AI was supposed to provide. Enterprise AI needs a middle ground:

  Preserve identity and control without turning one credential into a universal key or every AI action into another sign-on prompt.

## Securing the workflow with the right controls

Not every step in Sarah's workflow has the same security problem.

![Diagram showing the internal execution and cross trust boundary workflows side by side.](_images/authplayground-workflow-controls.png)

Protocols work together to answer different enterprise trust problems inside the workflow. They're composable pieces, not a mandatory sequence. You can combine protocols to solve specific problems your enterprise faces.

| Protocol                                                                | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| ----------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [PKCE](authplayground-pkce.html)                                        | **Protects authorization-code redemption**After the user-facing authorization flow, the client receives an authorization code. Proof Key for Code Exchange (PKCE) protects the Authorization Code grant from interception attacks by introducing a cryptographic verifier that only the legitimate client can produce.                                                                                                                                                                                                                                                                                             |
| [PAR](authplayground-par.html)                                          | **How the request reaches the authorization server**Pushed Authorization Requests (PAR) invert the traditional authorization flow. Instead of passing authorization request parameters through the browser redirect, the client pushes them directly to the authorization server first and receives a short-lived reference URI to use in the redirect. This eliminates parameter tampering in the front channel entirely.                                                                                                                                                                                         |
| [DPoP](authplayground-dpop.html)                                        | **Binds credentials to the caller's key**A bearer token is only as secure as the channel it travels on. What if someone copies the token? Demonstrating Proof of Possession (DPoP) sender-constrains access tokens by binding them to a client-generated key pair. Even if a token is intercepted, it can't be used because the attacker doesn't hold the private key.DPoP doesn't require a human or delegated authority. It can sender-constrain tokens used by autonomous workloads as well as tokens used in human-initiated workflows.                                                                        |
| [Token Exchange](authplayground-token-exchange.html)                    | **A new token for a different context**Token Exchange enables an agent or downstream service to exchange a subject's token for a new one scoped to the action it needs to perform, while the original subject remains auditable in the chain. The subject's authority is delegated to the actor, preserving the distinction between them without impersonation.                                                                                                                                                                                                                                                    |
| [RAR](authplayground-rar.html)                                          | **What's the client allowed to do?**Standard OAuth scopes are coarse-grained strings. Rich Authorization Requests (RAR) allow clients to express fine-grained authorization requirements as structured JSON objects using the `authorization_details` parameter. This is helpful when you need to authorize a specific transaction rather than a class of operations.                                                                                                                                                                                                                                              |
| [Transaction Tokens](authplayground-transaction-tokens.html)            | **Providing context in a transaction chain**Transaction Tokens are short-lived tokens designed to propagate authorization context through a chain of microservices. Each service in the chain can verify not only that the request is authorized, but that it originated from the expected upstream caller. This is critical for zero-trust service-to-service communication.                                                                                                                                                                                                                                      |
| [XAA / ID-JAG](authplayground-xaa-id-jag.html)                          | **Carries delegated user identity across the authorization domain boundary**Cross-Domain Access (XAA) / Identity Assertion JWT Authorization Grant (ID-JAG) enables cross-domain resource access by exchanging an ID Token for an ID-JAG assertion. When a user authenticates with one identity provider, but needs to access a resource governed by a different authorization server, XAA allows delegated identity information to be conveyed to another authorization domain. The receiving authorization domain evaluates that relationship under its own policy and determines what access should be granted. |
| [SPIFFE](authplayground-spiffe.html)                                    | **Which workload is running?**Secure Production Identity Framework for Everyone (SPIFFE) moves beyond service accounts and API keys. It provides cryptographic workload identity through SPIFFE Verifiable Identity Documents (SVID), giving every service in your infrastructure a verifiable identity it can use to authenticate to other services.A workload can have a SPIFFE identity and separately use a DPoP key to sender-constrain an OAuth token. SPIFFE establishes workload identity while DPoP protects use of a credential.                                                                         |
| [Resource Metadata](authplayground-resource-metadata.html)              | **What's the resource?**Protected Resource Metadata enables resource servers to advertise their own authorization requirements in a machine-readable document. Clients discover which authorization server governs a resource and which scopes or policies apply. This happens automatically, without out-of-band configuration.                                                                                                                                                                                                                                                                                   |
| [CIMD](authplayground-cimd.html)                                        | **Who's the client?**Client ID Metadata Documents (CIMD) demonstrate a model where OAuth clients are identified by an HTTPS URL hosting a JSON file as its `client_id`, instead of an opaque string registered in a directory. The authorization server fetches the client's metadata document directly from that URL, enabling self-sovereign client registration and dynamic discovery.                                                                                                                                                                                                                          |
| [Full Cross-Domain Access](authplayground-cross-domain-access-xaa.html) | **How to combine protocols**Full Cross-Domain Access combines PKCE, PAR, Token Exchange, DPoP, and XAA / ID-JAG into a single end-to-end scenario for cross-domain resource access. Each protocol contributes something to the whole picture.                                                                                                                                                                                                                                                                                                                                                                      |

## Key takeaways

One AI prompt can require many different security decisions. A human such as Sarah is sometimes the principal behind an activity. An autonomous workload can act entirely under its own machine authority. Agents, MCP tools, gateways, and services are software workloads with identities of their own. Authorization constrains what these identities are allowed to do.

Crossing an authorization boundary can require security context appropriate for the receiving domain. Internal service chains might need trusted transaction context to survive multiple hops. And possession of a token isn't always enough to use it.

As you explore individual protocols, keep returning to the underlying questions:

* Which principal is involved?

* Which workload is acting?

* Is delegated authority involved?

* What operation is being requested?

* Which authorization domain owns the decision?

* What transaction does this request belong to?

* Is the credential intended for this context?

* Can the presenter prove possession of the key associated with the token?

* Can the enterprise reconstruct what happened afterward?

The protocols solve different pieces of these problems. Together, they provide building blocks that operate across users, workloads, services, and trust boundaries without losing the identity, authorization, context, and accountability needed to govern it.

## Next steps

Learn how to [get started with the AuthPlayground](authplayground-getting-started.html).

---

---
title: Client ID Metadata Documents (CIMD) in the AuthPlayground
description: Explore how Client ID Metadata Documents help OAuth servers discover and evaluate dynamic AI and MCP clients in the Identity for AI AuthPlayground.
component: identity-for-ai
page_id: identity-for-ai:protocols:authplayground-cimd
canonical_url: https://developer.pingidentity.com/identity-for-ai/protocols/authplayground-cimd.html
llms_txt: https://developer.pingidentity.com/identity-for-ai/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-08-24T07:38:08Z
keywords: ["Identity for AI", "OAuth 2.0 protocols", "Client ID Metadata Documents", "CIMD", "dynamic AI clients", "MCP clients", "enterprise authorization", "AuthPlayground"]
section_ids:
  the-cimd-model: The CIMD model
  why-this-matters-for-ai-and-mcp: Why this matters for AI and MCP
  the-authplayground-implementation: The AuthPlayground implementation
  step-1-fetch-authorization-server-metadata: "Step 1: Fetch authorization server metadata"
  step-2-send-an-authorization-request-with-the-client-identifier-url: "Step 2: Send an authorization request with the client identifier URL"
  step-3-retrieve-the-client-id-metadata-document: "Step 3: Retrieve the client ID metadata document"
  step-4-exchange-the-authorization-code: "Step 4: Exchange the authorization code"
  how-cimd-relates-to-other-concepts: How CIMD relates to other concepts
  cimd-helps-oauth-servers-identify-dynamic-clients: CIMD helps OAuth servers identify dynamic clients
  discovery-doesnt-mean-automatic-trust: Discovery doesn't mean automatic trust
  key-takeaways: Key takeaways
---

# Client ID Metadata Documents (CIMD) in the AuthPlayground

Helping authorization servers understand dynamic AI clients.

Sarah asks the company's AI assistant to prepare her for the Apex Logistics meeting. The assistant might need Salesforce opportunity data, ServiceNow support history, and information from other enterprise systems.

Traditional OAuth deployments often rely on client registration ahead of time. The authorization server already knows the client identifier, redirect URIs, authentication method, and other metadata. In dynamic AI and Model Context Protocol (MCP) ecosystems, clients and authorization servers can operate independently. What happens when the authorization server doesn't already have a registration relationship with an AI application or MCP client?

Before the enterprise can decide what a client is allowed to access on Sarah's behalf, it needs to understand which client is making the request and where it can obtain the metadata describing this client. CIMD ([IETF draft](https://datatracker.ietf.org/doc/draft-ietf-oauth-client-id-metadata-document/)) addresses this problem.

## The CIMD model

Instead of using an opaque client identifier, such as `client_id=playground-demo-client`, in CIMD the MCP or OAuth client uses an HTTPS URL as its identifier:

```
client_id=https://.../cimd/clients/playground-demo-client
```

The HTTPS URL identifies a JSON metadata document describing the client. The client ID metadata document contains properties such as:

```
client_id
client_name
redirect_uris
grant_types
response_types
token_endpoint_auth_method
scope
```

The `client_id` is more than an opaque lookup value. It identifies the client and tells the authorization server where to retrieve the client's metadata. The specification places requirements on these identifiers. For example, the client identifier uses HTTPS and contains a path. The `client_id` inside the metadata document must exactly match the document URL.

### Why this matters for AI and MCP

Imagine that Sarah's AI assistant invokes an independently deployed MCP client that needs OAuth access to continue the workflow. CIMD gives the client a way to identify itself using an HTTPS URL from which its metadata can be retrieved.

This doesn't mean the authorization server automatically accepts an unknown client. CIMD changes how client metadata is discovered. The authorization server still decides which clients it accepts.

## The AuthPlayground implementation

**Entities involved**: Client application, CIMD service, IdP (authorization server)

The AuthPlayground demonstrates the [Client ID Metadata Document](https://www.authplayground.dev/flows/cimd) flow in four steps:

1. Fetch authorization server metadata.

2. Send an authorization request with the client identifier URL.

3. Retrieve the client ID metadata document.

4. Exchange the authorization code.

### Step 1: Fetch authorization server metadata

The client retrieves the authorization server metadata:

```json
GET /.well-known/oauth-authorization-server/idp
Accept: application/json
```

The response returns metadata:

```json
{
  "issuer": "https://.../idp",
  "authorization_endpoint": "https://.../idp/authorize",
  "token_endpoint": "https://.../idp/token",
  "pushed_authorization_request_endpoint": "https://.../idp/par",
  "client_id_metadata_document_supported": true,
  "code_challenge_methods_supported": [
    "S256"
  ]
}
```

The important signal is the `client_id_metadata_document_supported` property. A value of `true` tells the client that the authorization server supports CIMD.

### Step 2: Send an authorization request with the client identifier URL

The client starts an Authorization Code flow with PKCE. The important difference is the client identifier. Instead of a simple string such as `client_id=playground-demo-client`, the playground uses a full URL:

```json
GET /idp/authorize
    response_type=code
    client_id=https://.../cimd/clients/playground-demo-client
    redirect_uri=https://.../callback
    scope=openid profile email
    state=<state>
    code_challenge=<pkce_challenge>
    code_challenge_method=S256
```

The HTTPS URL identifies both the client and the metadata document associated with it. The rest of the authorization request is familiar OAuth.

### Step 3: Retrieve the client ID metadata document

The authorization server retrieves the metadata associated with the client identifier:

```json
GET /cimd/clients/playground-demo-client
Accept: application/json
```

The returned document describes the client:

```json
{
  "client_id": "https://.../cimd/clients/playground-demo-client",
  "client_name": "AuthPlayground CIMD Demo Client",
  "client_uri": "https://www.pingidentity.com",
  "redirect_uris": [
    "https://.../callback"
  ],
  "grant_types": [
    "authorization_code"
  ],
  "response_types": [
    "code"
  ],
  "token_endpoint_auth_method": "none",
  "scope": "openid profile email"
}
```

Two relationships are particularly important:

* The `client_id` inside the metadata document must match the URL used to identify the client in the authorization request.

* The `redirect_uri` in the authorization request must appear in the metadata document's `redirect_uris` array.

The authorization server now has metadata it can evaluate when deciding whether to proceed with the client.

|   |                                                                                                                                                                                                                                                                                      |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | The playground uses `token_endpoint_auth_method=none` for this particular client. This is a playground example, not a requirement that all CIMD clients use no client authentication. CIMD can be used with appropriate asymmetric client-authentication mechanisms where supported. |

### Step 4: Exchange the authorization code

The client performs the normal Authorization Code token exchange using PKCE:

```json
POST /idp/token
Content-Type: application/x-www-form-urlencoded

grant_type=authorization_code
code=<authorization_code>
redirect_uri=https://.../callback
client_id=https://.../cimd/clients/playground-demo-client
code_verifier=<code_verifier>
```

Notice that the HTTPS URL continues to be used as the `client_id`. The resulting access token contains claims about the user and the client:

```json
{
  "sub": "demo-user@example.com",
  "scope": "openid profile email",
  "client_id": "https://.../cimd/clients/playground-demo-client",
  "iss": "https://.../idp"
}
```

CIMD hasn't introduced a new OAuth grant type. The flow is still Authorization Code with PKCE. What changed is how the client identifies itself and how the authorization server obtains the metadata needed to understand the client.

## How CIMD relates to other concepts

### CIMD helps OAuth servers identify dynamic clients

To help Sarah prepare for her meeting, the MCP client fetching Salesforce and ServiceNow data needs OAuth access. The client uses an HTTPS metadata URL as its `client_id`. The authorization server retrieves the metadata document, evaluates the client identifier and redirect URI, and applies enterprise policy to decide whether to accept the client. If accepted, the authorization server issues an access token for the downstream integrations to Salesforce and ServiceNow.

CIMD answers which OAuth client is participating in the workflow and where to obtain the metadata needed to evaluate it. CIMD doesn't answer:

* What Salesforce data Sarah can access. That's an authorization question.

* Who Sarah is. That's an identity question.

|   |                                                                                                                                                       |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Salesforce and ServiceNow are examples of resources the AI workflow might need to reach. This doesn't imply that these SaaS platforms implement CIMD. |

### Discovery doesn't mean automatic trust

CIMD makes client metadata discoverable, but doesn't make that metadata automatically trustworthy. The authorization server remains responsible for safely retrieving and evaluating the document and deciding whether the client is acceptable. An enterprise can explicitly onboard approved clients or combine CIMD with its own client governance policies. Easier discovery shouldn't become a shortcut around enterprise security controls.

## Key takeaways

CIMD provides a standard model for making dynamic clients understandable to authorization servers. The client identifies itself with an HTTPS URL, the authorization server retrieves the associated metadata, and evaluates the client according to its own policy.

In dynamic AI and MCP ecosystems, CIMD creates a useful bridge between dynamic software and enterprise OAuth infrastructure without requiring the authorization server to blindly trust unfamiliar clients.

---

---
title: Cross-App Access (XAA) / ID-JAG in the AuthPlayground
description: Explore how XAA and ID-JAG carry delegated user identity across authorization domains in the AuthPlayground.
component: identity-for-ai
page_id: identity-for-ai:protocols:authplayground-xaa-id-jag
canonical_url: https://developer.pingidentity.com/identity-for-ai/protocols/authplayground-xaa-id-jag.html
llms_txt: https://developer.pingidentity.com/identity-for-ai/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-08-24T07:38:08Z
keywords: ["Identity for AI", "OAuth 2.0 protocols", "delegated identity", "cross-domain identity", "cross-domain access", "ID-JAG", "XAA", "token exchange", "AuthPlayground"]
section_ids:
  the-id-jag-model: The ID-JAG model
  why-alternatives-fail: Why alternatives fail
  the-authplayground-implementation: The AuthPlayground implementation
  step-1-authenticate-the-user: "Step 1: Authenticate the user"
  step-2-exchange-the-id-token-for-an-id-jag: "Step 2: Exchange the ID Token for an ID-JAG"
  step-3-present-the-id-jag: "Step 3: Present the ID-JAG"
  step-4-access-the-protected-resource: "Step 4: Access the protected resource"
  how-xaa-id-jag-relates-to-other-concepts: How XAA / ID-JAG relates to other concepts
  how-this-works-in-an-enterprise-environment: How this works in an enterprise environment
  how-xaa-id-jag-relates-to-workload-identity: How XAA / ID-JAG relates to workload identity
  key-takeaways: Key takeaways
---

# Cross-App Access (XAA) / ID-JAG in the AuthPlayground

Preserving delegated identity across enterprise AI.

When Sarah asks her AI assistant to prepare a meeting briefing for Apex Logistics, the assistant needs opportunity data from Salesforce and support history from ServiceNow. Behind the scenes, the AI assistant invokes Salesforce and ServiceNow Model Context Protocol (MCP) tools to reach those systems.

Each target system sits behind its own authorization domain, with its own policies, resources, and access tokens. The AI assistant needs a way to carry Sarah's trusted identity into each authorization domain without making her original token valid everywhere.

This creates a practical challenge. How can Sarah's trusted identity reach another authorization domain without misusing her original token? XAA ([IETF draft](https://auth-playground-qa.ping-devops.com/flows/xaa)) and the Identity JSON Assertion Grant (ID-JAG) profile solve this problem.

## The ID-JAG model

ID-JAG is a short-lived identity assertion used to carry trusted user identity into another authorization domain. It presents Sarah, for example, as authenticated by a trusted identity provider, along with an assertion created specifically for the authorization server. The receiving resource authorization server validates the assertion and decides what access to grant. The flow looks like this:

1. Sarah initiates the request.

2. The IdP authorization server performs a token exchange to issue an ID-JAG.

3. The ID-JAG crosses the authorization boundary.

4. The resource authorization server applies local policy to evaluate the ID-JAG.

5. The resource authorization server issues a local access token.

6. The local access token is used to access the protected API.

The ID-JAG isn't the final API access token. Its job is to carry Sarah's trusted identity to the authorization server responsible for the target resource. That authorization server remains in control of the actual access decision.

### Why alternatives fail

When building cross-domain integrations, teams might try cross-app access alternatives:

* Give every MCP tool a service account

  This weakens user-level accountability. If the only identity available is a generic MCP service account, you lose the connection to Sarah and fail audit requirements.

* Forward Sarah's original token everywhere

  This breaks down across authorization domains. A target authorization domain, such as ServiceNow or Salesforce, shouldn't have to accept a token because another system issued it. One token shouldn't become a universal enterprise credential.

* Ask Sarah to authenticate for every target

  Sending Sarah through a new authorization interaction every time the AI needs another system causes approval fatigue and defeats the value of the AI workflow.

ID-JAG provides a way to preserve a trusted user identity across authorization boundaries while still letting each target domain control access to its own resources.

## The AuthPlayground implementation

**Entities involved**: Client application, IdP (authorization server), authorization server B, resource server

The AuthPlayground demonstrates the [Cross-App Access (XAA) / ID-JAG](https://www.authplayground.dev/flows/xaa) flow in four steps:

1. Authenticate the user.

2. Exchange the ID token for an ID-JAG.

3. Present the ID-JAG.

4. Access the protected resource.

### Step 1: Authenticate the user

Sarah authenticates through the IdP authorization server. The playground exchanges an authorization code using Proof Key for Code Exchange (PKCE):

```json
POST /idp/token
Content-Type: application/x-www-form-urlencoded

{
  "grant_type": "authorization_code",
  "code": "<authorization_code>",
  "redirect_uri": "<callback>",
  "client_id": "playground-demo-client",
  "code_verifier": "<pkce_verifier>"
}
```

The decoded ID token contains identity and authentication context for Sarah (`demo-user@example.com`):

```json
{
  "sub": "demo-user@example.com",
  "email": "demo-user@example.com",
  "auth_time": 1786743254,
  "acr": "urn:mace:incommon:iap:silver",
  "amr": ["pwd"],
  "iss": "https://.../idp",
  "aud": "playground-demo-client"
}
```

Sarah has authenticated and the enterprise knows who she is. However, no target authorization domain has granted access yet. Authentication in one domain doesn't automatically equal authorization in another.

### Step 2: Exchange the ID Token for an ID-JAG

The AI workflow needs Salesforce data protected by another authorization domain. Instead of forwarding Sarah's original ID token, the client asks the IdP authorization server for an ID-JAG targeted to the resource authorization server:

```
POST /idp/token
Content-Type: application/x-www-form-urlencoded

grant_type=urn:ietf:params:oauth:grant-type:token-exchange
subject_token=<id_token>
subject_token_type=urn:ietf:params:oauth:token-type:id_token
requested_token_type=urn:ietf:params:oauth:token-type:id-jag
audience=https://.../as-b
client_id=playground-demo-client
```

The key parameter is `requested_token_type=urn:ietf:params:oauth:token-type:id-jag`. The response confirms the issuance of an ID-JAG:

```json
{
  "access_token": "<id_jag>",
  "issued_token_type": "urn:ietf:params:oauth:token-type:id-jag",
  "token_type": "N_A",
  "expires_in": 300
}
```

The JWT itself is explicitly typed:

```json
{
  "alg": "RS256",
  "kid": "idp-signing-key-1",
  "typ": "oauth-id-jag+jwt"
}
```

Notice the changes between the original token and the new ID-JAG:

```
Original ID Token                           ID-JAG

sub = Sarah                  ------->       sub = Sarah
iss = IdP                 Token Exchange    iss = IdP
aud = Playground client                     aud = Resource Authorization Server
                                            typ = oauth-id-jag+jwt
```

Sarah's original token hasn't been copied. A new, short-lived assertion has been created specifically for the receiving authorization domain.

### Step 3: Present the ID-JAG

The client presents the ID-JAG to the resource authorization server:

```json
POST /as-b/token
Content-Type: application/x-www-form-urlencoded

grant_type=urn:ietf:params:oauth:grant-type:jwt-bearer
assertion=<id_jag>
scope=openid read
```

The receiving authorization server can now evaluate questions such as:

* Do I trust the issuer of this ID-JAG?

* Was this assertion intended for me?

* Which user does it represent?

* How and when did the user authenticate?

* What access should I grant under my own policy?

If local policy permits the request, the resource authorization server issues its own access token. The ID-JAG provides trusted identity context, but doesn't force the target domain to grant access.

The resulting local token contains:

```json
{
  "sub": "demo-user@example.com",
  "client_id": "playground-demo-client",
  "scope": "openid read",
  "iss": "https://.../as-b",
  "aud": "https://.../rs"
}
```

The user identity crosses the authorization boundary. but the access decision is made locally under the policy protecting the target resource.

### Step 4: Access the protected resource

The client now calls the protected API using the locally issued access token, completely independent of the original ID-JAG or ID token:

```json
GET /rs/api/data
Authorization: Bearer <resource_access_token>
```

The playground returns:

```json
{
  "message": "Access granted to protected resource",
  "user": "demo-user@example.com",
  "scope": "openid read",
  "token_type": "Bearer"
}
```

## How XAA / ID-JAG relates to other concepts

### How this works in an enterprise environment

In a real-world scenario where Sarah's prompt requires data from both Salesforce and ServiceNow, this pattern happens independently for each system. Salesforce access is evaluated under the policy protecting Salesforce resources. ServiceNow access is evaluated under the policy protecting ServiceNow resources. Neither target needs to accept Sarah's original token, and neither target inherits the other system's authorization decision.

|   |                                                                                                                                                               |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | This example assumes a target authorization environment that supports the ID-JAG profile, rather than implying that Salesforce natively implements this flow. |

### How XAA / ID-JAG relates to workload identity

The MCP tool is software performing work as part of the AI workflow. ID-JAG doesn't turn the MCP tool into Sarah or establish the MCP tool's [workload identity](authplayground-spiffe.html). Those are separate concerns.

ID-JAG carries the trusted user identity into the authorization domain. A workload identity mechanism, such as SPIFFE / SVID, defines which software workload is running. In a production AI architecture, both ID-JAG and SPIFFE matter. Keeping these identities separate avoids making the MCP tool pretend to be Sarah.

## Key takeaways

Traditional applications often have predictable integration paths. Enterprise AI can fan out dynamically. One prompt might use Salesforce, ServiceNow, Databricks, Jira, Microsoft 365, and internal APIs. Each target represents a different authorization context.

ID-JAG preserves Sarah's trusted identity as requests cross authorization boundaries. The MCP tool remains software. Sarah remains the user. The authorization domain protecting the target resource remains in control of what access it grants. One user request reaches multiple enterprise systems while preserving user identity, local authorization control, and clear trust boundaries.

---

---
title: Demonstrating Proof of Possession (DPoP) in the AuthPlayground
description: "Explore how DPoP binds OAuth access tokens to a caller's key and prevents copied tokens from being replayed in enterprise AI workflows."
component: identity-for-ai
page_id: identity-for-ai:protocols:authplayground-dpop
canonical_url: https://developer.pingidentity.com/identity-for-ai/protocols/authplayground-dpop.html
llms_txt: https://developer.pingidentity.com/identity-for-ai/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-08-24T07:38:08Z
keywords: ["Identity for AI", "OAuth 2.0 protocols", "DPoP", "proof of possession", "OAuth 2.0", "OpenID connect", "PKCE", "RAR", "PAR", "transaction tokens", "token exchange", "AuthPlayground"]
section_ids:
  the-dpop-model: The DPoP model
  the-authplayground-implementation: The AuthPlayground implementation
  step-1-generate-a-dpop-key-pair: "Step 1: Generate a DPoP key pair"
  step-2-associate-the-authorization-request-with-the-dpop-key: "Step 2: Associate the authorization request with the DPoP key"
  step-3-exchange-the-code-with-a-dpop-proof: "Step 3: Exchange the code with a DPoP proof"
  the-authorization-server-binds-the-token-to-the-key: The authorization server binds the token to the key
  step-4-call-the-protected-resource: "Step 4: Call the protected resource"
  why-a-fresh-proof-is-created-for-each-request: Why a fresh proof is created for each request
  what-if-the-access-token-is-copied: What if the access token is copied?
  how-dpop-relates-to-other-concepts: How DPoP relates to other concepts
  dpop-doesnt-require-a-human-or-delegation: DPoP doesn't require a human or delegation
  dpop-isnt-workload-identity: DPoP isn't workload identity
  dpop-and-pkce-protect-different-things: DPoP and PKCE protect different things
  key-takeaways: Key takeaways
---

# Demonstrating Proof of Possession (DPoP) in the AuthPlayground

Binding tokens to the caller that holds the key.

Consider a retrieval agent running inside the enterprise AI platform. This AI workload's job is to gather information needed by another agent or application. For example:

* **Planner agent**: Requests the customer context needed for a task.

* **Retrieval agent**: Retrieves the information.

* **Customer context API**: Provides the data.

The retrieval agent might be authorized to access the customer context API under its own machine authority. There doesn't need to be a human user involved.

Suppose the access token is copied from memory, exposed in a log, forwarded to another workload, or otherwise stolen. With a traditional bearer token, possession of the token might be enough to use it. DPoP ([RFC 9449](https://datatracker.ietf.org/doc/html/rfc9449)) is designed to solve this problem.

## The DPoP model

DPoP binds an OAuth token to a cryptographic key and requires the caller to prove possession of the corresponding private key when using the token. With DPoP:

* The caller holds both an access token and a private key.

* The caller generates a DPoP proof using the private key.

* The protected resource validates both the token and the proof.

A copied access token by itself isn't enough. The caller must create a valid DPoP proof using the private key associated with the token. This is known as sender-constraining the token.

## The AuthPlayground implementation

**Entities involved**: Client application, IdP (authorization server), resource server

The AuthPlayground demonstrates the [Demonstrating Proof of Possession](https://www.authplayground.dev/flows/dpop) flow in four steps:

1. Generate a DPoP key pair.

2. Associate the authorization request with the DPoP key thumbprint.

3. Exchange the code with a DPoP proof.

4. Call the protected resource with DPoP.

### Step 1: Generate a DPoP key pair

The client generates an asymmetric key pair locally. To demonstrate this, the playground uses `RS256` and produces a public JSON Web Key (JWK) and its SHA-256 JWK thumbprint:

```json
{
  "algorithm": "RS256",
  "publicJwk": {
    "e": "AQAB",
    "kty": "RSA",
    "n": "<modulus>"
  },
  "thumbprint": "VNJmvk1zqg80Gt7XiJalF8hru82ey-yCc5oOwQpBkew"
}
```

The thumbprint is commonly represented as the `jkt`. It gives the authorization server a way to associate the resulting access token with that key. To summarize the relationships:

* **Private key**: Stays with the client and signs DPoP proofs.

* **Public key**: Used to derive the JWK thumbprint.

* **JWK thumbprint**: Represented as the `jkt`.

### Step 2: Associate the authorization request with the DPoP key

The client begins the authorization flow. In the playground, the request includes PKCE and the DPoP key thumbprint:

```json
GET /idp/authorize

response_type=code
client_id=playground-demo-client
redirect_uri=<callback>
scope=openid profile email
state=<state>
nonce=<nonce>
code_challenge=<pkce_challenge>
code_challenge_method=S256
dpop_jkt=VNJmvk1zqg80Gt7XiJalF8hru82ey-yCc5oOwQpBkew
```

The important DPoP parameter is `dpop_jkt`. This parameter associates the authorization request with the public key corresponding to the private key held by the client. The authorization server then returns an authorization code.

The client hasn't sent its private key to the authorization server yet. It will prove possession of that key cryptographically in the next step.

### Step 3: Exchange the code with a DPoP proof

The client sends the authorization code to the token endpoint. The request includes the normal Authorization Code and PKCE parameters and adds another HTTP header:

```json
DPoP: <dpop_proof_jwt>
```

The DPoP proof is a JWT signed with the private key generated in Step 1. A simplified proof for the token request contains:

```json
{
  "htm": "POST",
  "htu": "https://.../idp/token",
  "jti": "<unique_id>",
  "iat": "<timestamp>"
}
```

These claims matter because they bind the proof to the specific HTTP request:

* `htm`: Identifies the HTTP method (such as `POST`).

* `htu`: Identifies the target URI (for example, `https://…​/idp/token`).

* `iat`: Indicates when the proof was created.

* `jti`: Gives the proof a unique identifier.

The proof is a statement that the client possesses the private key and that the proof is created for a particular HTTP request.

#### The authorization server binds the token to the key

After validating the authorization code, PKCE verifier, and DPoP proof, the authorization server issues an access token. The response includes the access token and identifies it as a DPoP-bound token:

```json
{
  "token_type": "DPoP",
  "expires_in": 3600,
  "access_token": "<access_token>"
}
```

The decoded access token contains several claims:

```json
{
  "sub": "demo-user@example.com",
  "scope": "openid profile email",
  "client_id": "playground-demo-client",
  "cnf": {
    "jkt": "VNJmvk1zqg80Gt7XiJalF8hru82ey-yCc5oOwQpBkew"
  }
}
```

The important claim is the `cnf` object. This `jkt` matches the thumbprint of the key generated in Step 1. To summarize the relationships:

* **DPoP key pair**: Derives the JWK thumbprint.

* **JWK thumbprint**: Becomes the `cnf.jkt` claim.

* **DPoP-bound access token**: Contains the `cnf.jkt` claim.

The access token is now associated with this key. Possessing the access token alone isn't enough to satisfy DPoP validation.

### Step 4: Call the protected resource

The client calls the resource server. The request contains both the DPoP-bound access token and a fresh DPoP proof:

```json
GET /rs/api/data

Authorization: DPoP <access_token>
DPoP: <fresh_dpop_proof>
```

Notice that the authorization scheme is `Authorization: DPoP` rather than `Authorization: Bearer`.

The DPoP proof is freshly created for the resource request. A simplified version contains:

```json
{
  "htm": "GET",
  "htu": "https://.../rs/api/data",
  "jti": "<unique_id>",
  "iat": "<timestamp>",
  "ath": "<access_token_hash>"
}
```

The additional `ath` claim is a hash of the access token being presented. This allows the proof to be associated with the particular access token used in the request. As a result, the resource server can verify several relationships before granting access.

* The resource server checks that the DPoP proof:

  * Is signed by the expected key

  * Has the correct `htm` and `htu`

  * Is sufficiently fresh

  * Its `ath` matches the access token

* The access token's `cnf.jkt` matches the key used to sign the DPoP proof.

If these checks succeed and the token is otherwise valid, the request can proceed. The response confirms that the access is granted to the protected resource.

#### Why a fresh proof is created for each request

The DPoP proof used at the token endpoint isn't reused at the resource server. They're different HTTP requests with different methods and target URIs. The client creates a fresh proof for each request and the server validates that proof against the specific request being made.

The token endpoint proof used at the token endpoint includes:

```
htm = POST
htu = /idp/token
```

The resource proof used at the resource server includes:

```
htm = GET
htu = /rs/api/data
ath = hash(access_token)
```

Request binding is an important part of DPoP. A proof created for one endpoint shouldn't be reusable against another endpoint.

#### What if the access token is copied?

Return to the retrieval-agent example. Suppose the retrieval agent legitimately obtains a DPoP-bound token, but an unrelated workload gets a copy. The unrelated workload has the token, but doesn't have the corresponding private key. Without the matching private key, the workload can't produce a valid DPoP proof, and the resource server rejects the request. DPoP makes a copied token less useful to a party that doesn't possess the associated private key.

## How DPoP relates to other concepts

### DPoP doesn't require a human or delegation

DPoP can protect tokens used by various entities:

* Autonomous AI agents

* Backend services

* Workloads acting for a user, such as Sarah

The example with Sarah involves delegated human authority, but DPoP doesn't determine whose authority is behind an operation. DPoP works at the token use layer, regardless of the authority behind the token, to protect the credential used to perform an operation. An autonomous AI agent can use DPoP while operating entirely under its own machine authority.

### DPoP isn't workload identity

There's an important distinction between DPoP and workload identity. Suppose the retrieval agent has a [SPIFFE](authplayground-spiffe.html) identity, for example `spiffe://company.internal/agents/retrieval`. SPIFFE / SVID answers which workload is running.

DPoP answers whether the presenter possesses the key associated with the credential. A DPoP key shouldn't be treated as the workload's identity. The two mechanisms complement each other.

### DPoP and PKCE protect different things

[PKCE](authplayground-pkce.html) protects authorization-code redemption during the token request. It helps ensure that an intercepted authorization code can't be redeemed without the corresponding verifier. DPoP sender-constrains the resulting access token during the resource request. The protocols protect different stages of the OAuth flow.

## Key takeaways

The playground demonstrates the DPoP model from beginning to end:

* The client generates a key pair, and its public-key thumbprint is associated with the authorization request through `dpop_jkt`.

* At the token endpoint, the client proves possession of the private key, and the authorization server issues a DPoP-bound access token containing the corresponding `cnf.jkt`.

* When the client calls the resource server, it creates a fresh DPoP proof tied to the HTTP request and the access token.

This gives the resource server cryptographic evidence that the presenter possesses the key associated with that token.

This is important for distributed AI systems. Agents, gateways, applications, and other workloads might all need OAuth tokens. DPoP helps ensure that copying a token isn't enough for another caller to use it.

---

---
title: Full Cross-Domain Access in the AuthPlayground
description: Explore an end-to-end AuthPlayground flow combining OAuth protocols to preserve identity and protect cross-domain enterprise AI access.
component: identity-for-ai
page_id: identity-for-ai:protocols:authplayground-cross-domain-access-xaa
canonical_url: https://developer.pingidentity.com/identity-for-ai/protocols/authplayground-cross-domain-access-xaa.html
llms_txt: https://developer.pingidentity.com/identity-for-ai/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-08-24T07:38:08Z
keywords: ["Identity for AI", "OAuth 2.0 protocols", "OpenID connect", "DPoP", "PAR", "RAR", "PKCE", "ID-JAG", "token exchange", "cross-domain access", "AuthPlayground"]
section_ids:
  the-full-cross-domain-access-model: The full cross-domain access model
  the-authplayground-implementation: The AuthPlayground implementation
  step-1-generate-the-dpop-key-pair: "Step 1: Generate the DPoP key pair"
  step-2-push-the-authorization-request: "Step 2: Push the authorization request"
  step-3-authorize-the-user-with-request_uri: "Step 3: Authorize the user with request_uri"
  step-4-exchange-the-code-with-pkce-and-dpop: "Step 4: Exchange the code with PKCE and DPoP"
  step-5-exchange-the-subject-and-actor-context-for-an-id-jag: "Step 5: Exchange the subject and actor context for an ID-JAG"
  step-6-present-the-jwt-grant-with-dpop-proof-for-an-authorization-decision: "Step 6: Present the JWT grant with DPoP proof for an authorization decision"
  step-7-access-the-protected-resource-with-dpop: "Step 7: Access the protected resource with DPoP"
  bringing-it-back-to-enterprise-ai: Bringing it back to enterprise AI
  how-cross-domain-access-solves-trust-questions: How cross-domain access solves trust questions
  key-takeaways: Key takeaways
---

# Full Cross-Domain Access in the AuthPlayground

How enterprise AI safely crosses trust boundaries end to end.

Imagine you're the Chief Architect at a Sarah's company. The CEO wants AI used across the company to improve productivity. The CISO wants every AI action to remain secure, attributable, governed, and auditable. These goals are challenging when one user request has to cross multiple authorization domains.

Sarah asks the AI assistant to help her prepare for the Apex Logistics meeting. The AI assistant needs to access Salesforce opportunity data, ServiceNow support history, and information from other enterprise systems. The request must cross distinct authorization domains, each with its own policy and access control.

This scenario raises several trust questions:

* Did Sarah really authenticate?

* What's the AI workflow allowed to do?

* Which software is acting on Sarah's behalf?

* How does Sarah's identity reach another authorization domain?

* Does the target domain make its own authorization decision?

* Can a stolen token be replayed by someone else?

No single protocol answers all of those questions. The full cross-domain access flow shows how individual protocols come together in an end-to-end access path.

## The full cross-domain access model

It's tempting to think of enterprise AI security as a token problem. A token alone doesn't protect the authorization request before the browser redirect. It doesn't constrain what the AI client is asking to do, or preserve delegated identity across an authorization boundary. A token doesn't stop a stolen bearer token from being replayed.

The enterprise needs a chain of controls, each one solving a different part of the problem. Sarah's request flows through these stages:

1. Sarah initiates the request.

2. The secure authorization request uses Pushed Authorization Requests (PAR), Rich Authorization Requests (RAR), and Proof Key for Code Exchange (PKCE).

3. The authenticated user context establishes Sarah's identity.

4. Delegation combines Sarah (the subject) and the software actor.

5. Identity JSON Assertion Grant (ID-JAG) crosses the authorization boundary.

6. The target authorization server applies local policy.

7. The Demonstrating Proof of Possession (DPoP) bound access token is used to access the protected enterprise API.

These protocols coexist and work together to create, constrain, exchange, and validate the security context as the request moves through the architecture.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | The full cross-domain access flow intentionally combines several security controls to show how they work together in a high-assurance architecture. However, every production AI workflow doesn't need every protocol. The right combination depends on trust boundaries, authorization requirements, the threat model, and the sensitivity of resources.The goal of this flow isn't to prescribe one architecture for every use case. It's to show what's possible when these standards are combined. |

## The AuthPlayground implementation

**Entities involved**: Client application, IdP (authorization server), authorization server B, resource server

The AuthPlayground demonstrates the [Full Cross-Domain Access](https://www.authplayground.dev/flows/full-cross-domain) flow in seven steps:

1. Generate the DPoP key pair.

2. Push the authorization request.

3. Authorize the user with `request_uri`.

4. Exchange the code with PKCE and DPoP.

5. Exchange the subject and actor context for an ID-JAG.

6. Present the JSON Web Token (JWT) grant with DPoP proof for an authorization decision.

7. Access the protected resource with DPoP.

Let's walk through these steps using Sarah's enterprise AI request as a model.

### Step 1: Generate the DPoP key pair

Before the authorization flow begins, the client generates an asymmetric key pair. The playground computes a thumbprint for the public key:

```json
{
  "thumbprint": "kOG4j4ejqVDIY8rYxtqtme3e1TqPJmBhhLm2tRCh2zs"
}
```

The private key stays with the caller. The public-key thumbprint is derived from the public key and it's shared. The thumbprint is carried into later parts of the flow to bind credentials to the same key. This prepares the proof-of-possession mechanism that DPoP will use later.

### Step 2: Push the authorization request

The client establishes the authorization request directly with the IdP authorization server using PAR. The request includes:

```json
POST /idp/par

scope=openid profile read write delegation
code_challenge=<pkce_challenge>
code_challenge_method=S256
dpop_jkt=kOG4j4ejqVDIY8rYxtqtme3e1TqPJmBhhLm2tRCh2zs
authorization_details=[
  {
    "type": "account_information",
    "actions": ["read"]
  }
]
```

Several protocols come together:

* **PAR**: Sends the detailed authorization request directly to the authorization server instead of carrying all of it through the browser.

* **PKCE**: Introduces the `code_challenge` that protects the authorization code exchange.

* **RAR**: Adds structured authorization intent using `authorization_details`.

* **DPoP**: Introduces the public-key thumbprint (`dpop_jkt`) associated with the issued credentials.

The authorization server stores the request and returns a short-lived reference, establishing the request before the browser gets involved:

```json
{
  "request_uri": "urn:ietf:params:oauth:request_uri:35dff7b3-f034-4186-94cc-437ffa511058",
  "expires_in": 60
}
```

### Step 3: Authorize the user with `request_uri`

The browser is redirected using the short-lived reference:

```json
GET /idp/authorize
    request_uri=<request_uri>
    client_id=playground-demo-client
```

The IdP retrieves the authorization request it already has through PAR, authenticates Sarah, and returns an authorization code:

```json
{
  "code": "<authorization_code>",
  "state": "<original_state>"
}
```

The browser participates in the user-facing authorization flow, but doesn't need to carry the full authorization request.

### Step 4: Exchange the code with PKCE and DPoP

The client exchanges the authorization code, presenting the PKCE `code_verifier` and also sending a DPoP proof:

```json
POST /idp/token
DPoP: <dpop_proof>

grant_type=authorization_code
code=<authorization_code>
redirect_uri=<callback>
client_id=playground-demo-client
code_verifier=<code_verifier>
```

The resulting access token preserves context established earlier and contains RAR authorization details:

```json
{
  "authorization_details": [
    {
      "type": "account_information",
      "actions": ["read"]
    }
  ]
}
```

The access token also contains DPoP key binding:

```json
{
  "cnf": {
    "jkt": "kOG4j4ejqVDIY8rYxtqtme3e1TqPJmBhhLm2tRCh2zs"
  }
}
```

The ID token contains the delegation relationship:

```json
{
  "sub": "demo-user@example.com",
  "may_act": {
    "sub": "api-gateway@example.com"
  }
}
```

A separate actor token represents `api-gateway@example.com`. There are now two distinct identities:

* Subject: `demo-user@example.com`

* Actor: `api-gateway@example.com`, linked via the `may_act` claim

In the playground, the actor is an API gateway. In an enterprise AI architecture, that role might be an MCP gateway, AI agent, backend service, or another software workload.

|   |                                                                                                                                                                                                   |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The playground creates prerequisite credentials to keep the flow self-contained. In production, the human subject and software actor establish credentials through their own identity lifecycles. |

### Step 5: Exchange the subject and actor context for an ID-JAG

The workflow needs to cross into another authorization domain. The client performs token exchange using Sarah's ID token as the `subject_token` and the gateway credential as the `actor_token`:

```json
POST /idp/token

grant_type=urn:ietf:params:oauth:grant-type:token-exchange
subject_token=<id_token>
subject_token_type=urn:ietf:params:oauth:token-type:id_token
actor_token=<actor_token>
actor_token_type=urn:ietf:params:oauth:token-type:access_token
requested_token_type=urn:ietf:params:oauth:token-type:id-jag
audience=https://.../as-b
client_id=playground-demo-client
dpop_jkt=kOG4j4ejqVDIY8rYxtqtme3e1TqPJmBhhLm2tRCh2zs
```

This is an ID-JAG exchange because the `requested_token_type` is set to `urn:ietf:params:oauth:token-type:id-jag`. The response confirms that the `issued_token_type` matches and that the JWT `typ` is set to `oauth-id-jag+jwt`. The resulting ID-JAG includes the subject, actor, audience, and DPoP key binding:

```json
{
  "sub": "demo-user@example.com",
  "cnf": {
    "jkt": "kOG4j4ejqVDIY8rYxtqtme3e1TqPJmBhhLm2tRCh2zs"
  },
  "act": {
    "sub": "api-gateway@example.com",
    "iss": "https://.../idp"
  },
  "aud": "https://.../as-b"
}
```

The ID-JAG preserves several pieces of context:

* `sub`: Sarah remains the subject.

* `act`: The API gateway remains visible as the actor.

* `aud`: The ID-JAG is intended for authorization server B.

* `cnf.jkt`: The assertion remains bound to the DPoP key.

The software workload doesn't become Sarah. The delegated relationship remains explicit as the request crosses the authorization boundary.

### Step 6: Present the JWT grant with DPoP proof for an authorization decision

The client presents the ID-JAG to authorization server B. The ID-JAG is used as a JWT bearer authorization grant, while DPoP independently proves possession of the bound key:

```json
POST /as-b/token
DPoP: <dpop_proof>

grant_type=urn:ietf:params:oauth:grant-type:jwt-bearer
assertion=<id_jag>
scope=read write
```

Authorization server B validates the ID-JAG, verifies that it's the intended audience, evaluates the delegated identity context, validates the DPoP proof, and applies its own authorization policy. If the request is allowed, authorization server B issues an access token:

```json
{
  "sub": "demo-user@example.com",
  "scope": "read write",
  "cnf": {
    "jkt": "kOG4j4ejqVDIY8rYxtqtme3e1TqPJmBhhLm2tRCh2zs"
  },
  "iss": "https://.../as-b",
  "aud": "https://.../rs"
}
```

This is an important transition in the flow. The local access token, issued by authorization server B for the resource server, maintains the DPoP key binding.

Sarah's identity has crossed the authorization boundary, but authorization control hasn't. The target domain still decides what access to grant to the resources it protects.

### Step 7: Access the protected resource with DPoP

The client calls the protected API, sending the DPoP-bound access token and a fresh DPoP proof:

```json
GET /rs/api/data

Authorization: DPoP <access_token>
DPoP: <fresh_dpop_proof>
```

The proof is specific to this API request and includes an `ath` claim binding it to the presented access token:

```json
{
  "htm": "GET",
  "htu": "https://.../rs/api/data",
  "ath": "<hash_of_access_token>"
}
```

This enables the resource server to validate whether the token is valid for its use, and whether the caller presenting it can prove possession of the key the token is bound to. When those checks succeed, the playground returns:

```json
{
  "message": "Access granted to protected resource",
  "user": "demo-user@example.com",
  "scope": "read write",
  "token_type": "DPoP"
}
```

The chain reaches the protected resource without turning Sarah's original credential into a token that every system is expected to accept.

### Bringing it back to enterprise AI

Return to Sarah's original request to prepare for the Apex Logistics meeting. The AI assistant needs Salesforce opportunity information and ServiceNow support history. An MCP gateway might broker those calls across two distinct paths. In the Salesforce path:

1. Sarah initiates the request to the AI assistant.

2. The MCP gateway brokers the call.

3. The authorization domain issues a Salesforce-targeted ID-JAG.

4. The target authorization domain applies local policy to protect Salesforce access.

5. The Salesforce-facing API is reached using the DPoP-bound local access token.

ServiceNow information can be accessed using the same pattern. For a target authorization environment, each path in the pattern establishes its own delegated access.

|   |                                                                                                                                                                                                                   |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The playground provides an architectural example of a target authorization environment protecting Salesforce access. This doesn't imply that Salesforce natively implements this particular protocol combination. |

## How cross-domain access solves trust questions

To summarize the security properties of the full cross-domain access flow:

* Sarah remains the human subject.

* The MCP or API gateway remains identifiable as the software actor.

* RAR constrains what the workflow is asking to do.

* ID-JAG carries the delegated user identity into the target authorization domain.

* The target authorization server makes its own access decision and issues its own token.

* DPoP keeps the credential bound to the caller that possesses the corresponding private key.

Salesforce doesn't need to accept Sarah's original token. ServiceNow doesn't inherit Salesforce's authorization decision. The MCP gateway doesn't need to impersonate Sarah.

## Key takeaways

Sarah experiences a simple interaction with the AI assistant. Behind Sarah's request, the architecture makes a series of deliberate security decisions. Each protocol solves a different part of the problem, and together they form a complete cross-domain access flow.

| Protocol                    | Description                                                               |
| --------------------------- | ------------------------------------------------------------------------- |
| PAR                         | Establishes the authorization request directly with the server.           |
| PKCE                        | Protects authorization-code redemption.                                   |
| RAR                         | Constrains what the workflow requests.                                    |
| Token Exchange              | Combines subject and actor context for the next authorization domain.     |
| ID-JAG                      | Carries delegated user identity across the authorization domain boundary. |
| Target authorization server | Applies local policy and issues a local access token.                     |
| DPoP                        | Binds credentials to the caller's key.                                    |

Sarah's identity remains visible, the software actor remains distinct, authorization stays narrow, the target system retains control over its resources, and the credentials used along the way are protected against bearer-token replay.

For enterprise AI operating across multiple systems, this is more than giving an agent access. Full cross-domain access builds an access path that the enterprise can trust.

---

---
title: Getting started with the AuthPlayground
description: Get started with the AuthPlayground to explore OAuth 2.0 flows through simulated HTTP exchanges and decoded JSON Web Tokens (JWT).
component: identity-for-ai
page_id: identity-for-ai:protocols:authplayground-getting-started
canonical_url: https://developer.pingidentity.com/identity-for-ai/protocols/authplayground-getting-started.html
llms_txt: https://developer.pingidentity.com/identity-for-ai/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-09-16T00:06:46Z
keywords: ["Identity for AI", "OAuth 2.0 protocols", "AuthPlayground"]
section_ids:
  before-you-begin: Before you begin
  how-it-works: How it works
  what-to-do: What to do
---

# Getting started with the AuthPlayground

Use the [AuthPlayground](https://www.authplayground.dev) to explore OAuth 2.0 extension protocols in a controlled environment.

## Before you begin

Before you start exploring OAuth flows, learn key concepts behind the AuthPlayground to understand the simulated environment and how different protocols are represented. You can find details in [AuthPlayground concepts](authplayground-concepts.html).

## How it works

Each protocol maps to a specification (an IETF RFC or working draft) and each flow walks you through every HTTP exchange that makes it work. The backend is a lightweight simulation with no external identity provider or resource server involved. You can experiment freely without affecting a real environment.

The AuthPlayground has:

* **Real HTTP requests and responses**: Every step sends an actual request to a simulated backend and surfaces the full request and response, including headers, body, and status codes.

* **Live JSON Web Token (JWT) inspection**: When a step produces a JWT, the Token Inspector decodes the header, payload, and signature inline. You can see exactly which claims are present and what they contain.

* **Flows that build on each other**: Simpler protocols are building blocks for more complex ones. When you understand Proof Key for Code Exchange (PKCE), you'll understand why Pushed Authorization Requests (PAR) exist. When you understand both, the Full Cross-Domain Access flow starts to make sense.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The AuthPlayground is designed to make protocol behavior easy to explore and inspect. To keep each flow self-contained, some prerequisite setup, identities, credentials, and surrounding infrastructure are intentionally simplified or combined.For example, the playground might create prerequisite credentials that would normally be established independently in production. This keeps the protocol mechanics visible without prescribing how the surrounding architecture must be built.The flows demonstrate protocol mechanics and trust relationships, not a prescribed production architecture. In a real deployment, users, workloads, applications, and services would have independent identity lifecycles and security controls. |

## What to do

The AuthPlayground is hands-on and self-guided.

1. **Pick a protocol from the sidebar.**

   Each protocol corresponds to an OAuth 2.0 extension specification and includes a description and link to the RFC or specification.

2. **Step through the flow.**

   Click **Execute** in each step. The playground sends an HTTP request to a simulated backend and shows you the request and response.

3. **Inspect tokens.**

   When a step produces a JWT, the Token Inspector automatically decodes the header, payload, and signature, allowing you to examine which claims are present.

4. **Reset and repeat.**

   Click **Reset Flow** to clear all states and run the flow again from scratch.

As you explore a flow, focus on what changes or is preserved between steps. Which identities and workloads are represented? What is being authorized? Which audience or trust domain is involved? What credentials or context are created or propagated? What does each receiving system need to trust or validate?

---

---
title: Proof Key for Code Exchange (PKCE) in the AuthPlayground
description: Explore how PKCE protects OAuth authorization-code redemption from interception attacks in the AuthPlayground.
component: identity-for-ai
page_id: identity-for-ai:protocols:authplayground-pkce
canonical_url: https://developer.pingidentity.com/identity-for-ai/protocols/authplayground-pkce.html
llms_txt: https://developer.pingidentity.com/identity-for-ai/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-08-26T20:20:14Z
keywords: ["Identity for AI", "OAuth 2.0 protocols", "PKCE", "Proof Key for Code Exchange", "Authorization Code Flow", "enterprise AI", "AuthPlayground"]
section_ids:
  the-pkce-model: The PKCE model
  the-authplayground-implementation: The AuthPlayground implementation
  step-1-generate-the-verifier-and-challenge: "Step 1: Generate the verifier and challenge"
  step-2-send-the-code_challenge: "Step 2: Send the code_challenge"
  step-3-redeem-the-code-with-the-code_verifier: "Step 3: Redeem the code with the code_verifier"
  how-pkce-compares-to-other-concepts: How PKCE compares to other concepts
  bringing-it-back-to-enterprise-ai: Bringing it back to enterprise AI
  pkce-and-par: PKCE and PAR
  key-takeaways: Key takeaways
---

# Proof Key for Code Exchange (PKCE) in the AuthPlayground

Protecting the authorization code from interception attacks.

When Sarah asks her AI assistant to prepare a meeting briefing for Apex Logistics, the assistant needs data from Salesforce, ServiceNow, and other enterprise systems. Before that happens, the application must establish Sarah's authenticated session through an OAuth Authorization Code flow.

What if someone intercepts the short-lived authorization code? Can they redeem it, instead of the client that started the flow? PKCE ([RFC 7636](https://datatracker.ietf.org/doc/html/rfc7636)) protects against this by requiring the client redeeming the code to prove knowledge of a secret created when the flow began.

## The PKCE model

The client creates a high-entropy random value called the `code_verifier`. Using `S256`, it derives the `code_challenge`:

```json
"code_challenge = BASE64URL-ENCODE(SHA256(ASCII(code_verifier)))"
```

The client uses the two values at different points:

* **Authorization request**: The client sends the `code_challenge`. The verifier itself isn't sent in the authorization request.

* **Token request**: The client sends the `code_verifier`.

When the client redeems the code, the authorization server derives the challenge from the submitted verifier and compares it with the challenge associated with the original request. An intercepted authorization code alone isn't enough.

## The AuthPlayground implementation

**Entities involved**: Client application, IdP (authorization server)

The AuthPlayground demonstrates the [Proof Key for Code Exchange](https://www.authplayground.dev/flows/pkce) flow in three steps:

1. Generate `code_verifier` and `code_challenge`.

2. Send the authorization request with `code_challenge`.

3. Redeem the code with the `code_verifier`.

### Step 1: Generate the verifier and challenge

The first step happens locally without a network request. The playground generates a `code_verifier` and derives the `code_challenge` using SHA-256 and Base64url encoding:

```json
{
  "code_verifier": "zMmfa-o_LRRLZJRDwXfvZ5oyrF4K__IJnwoD9SUaZtQ",
  "code_challenge": "FSm-7wdqeus-41oeOeSjglqXdnSt-LhmvRwJgzR59DY",
  "code_challenge_method": "S256"
}
```

The client keeps the `code_verifier` and sends only the derived challenge during authorization.

### Step 2: Send the `code_challenge`

The authorization request includes the following information in the query string:

```json
GET /idp/authorize
    response_type=code
    client_id=playground-demo-client
    redirect_uri=https://.../callback
    scope=openid profile email
    code_challenge=FSm-7wdqeus-41oeOeSjglqXdnSt-LhmvRwJgzR59DY
    code_challenge_method=S256
```

The authorization server returns an authorization code through the browser redirect:

```json
302
location: https://.../callback

{
  "code": "<authorization_code>",
  "state": "<state>",
  "note": "Authorization Response: code returned via redirect_uri (RFC 6749 §4.1.2)"
}
```

At this point, the authorization code has traveled through the redirect. The original `code_verifier` hasn't. That separation is the core of PKCE.

### Step 3: Redeem the code with the `code_verifier`

The legitimate client sends both the authorization code and its original verifier:

```json
POST /idp/token
Content-Type: application/x-www-form-urlencoded

{
  "grant_type": "authorization_code",
  "code": "<authorization_code>",
  "redirect_uri": "https://.../callback",
  "client_id": "playground-demo-client",
  "code_verifier": "RvtACdjYxEsvE_kEJ6W6w3WsrG2nKZUtfepOY5EosFQ"
}
```

The authorization server derives the challenge from the submitted verifier and compares it with the challenge associated with the authorization request. The authorization server:

1. Receives the `code_verifier`.

2. Calculates the challenge using SHA-256 and Base64url encoding.

3. Compares the calculated challenge with the original `code_challenge`.

4. Returns tokens if they match, or rejects the request if they don't.

In the playground flow, the values match and the authorization server returns an access token and ID token for Sarah (`demo-user@example.com`).

## How PKCE compares to other concepts

### Bringing it back to enterprise AI

Sarah's request might eventually cause the AI assistant to reach Salesforce opportunity data or ServiceNow support history. PKCE operates much earlier in the flow:

* Sarah initiates the request to the AI assistant application.

* The application performs the authorization code flow with PKCE against the authorization server.

* The authorization server issues the tokens.

* The AI workflow uses the tokens for downstream integrations such as Salesforce or ServiceNow.

PKCE doesn't decide what Salesforce or ServiceNow will allow. It doesn't establish workload identity or carry delegated identity across authorization domains. Its job is narrower. PKCE protects authorization-code redemption to ensure that possession of an intercepted code alone isn't enough to obtain the resulting tokens.

### PKCE and PAR

PKCE and [Pushed Authorization Requests (PAR)](authplayground-par.html) are often used together, but they protect different parts of the flow:

* PAR protects how the authorization request reaches the server.

* PKCE protects authorization-code redemption.

A deployment might use one or both depending on the requirements.

## Key takeaways

The complete PKCE flow looks like this:

1. Generate `code_verifier`.

2. Derive `code_challenge`.

3. Authorize with `code_challenge`.

4. Receive `authorization_code`.

5. Redeem with `code_verifier`.

6. Receive tokens.

The important security property of PKCE is that obtaining the authorization code by itself isn't enough to redeem it. For an AI workflow that might reach many enterprise systems, PKCE gives the rest of the authorization chain a stronger starting point.

---

---
title: Protected Resource Metadata in the AuthPlayground
description: Explore how Protected Resource Metadata helps AI and MCP clients discover authorization requirements in the AuthPlayground.
component: identity-for-ai
page_id: identity-for-ai:protocols:authplayground-resource-metadata
canonical_url: https://developer.pingidentity.com/identity-for-ai/protocols/authplayground-resource-metadata.html
llms_txt: https://developer.pingidentity.com/identity-for-ai/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-08-24T07:38:08Z
keywords: ["Identity for AI", "OAuth 2.0 protocols", "protected resource metadata", "RFC 9728", "dynamic AI clients", "MCP clients", "enterprise authorization", "AuthPlayground"]
section_ids:
  the-protected-resource-metadata-model: The protected resource metadata model
  the-authplayground-implementation: The AuthPlayground implementation
  step-1-call-the-protected-resource: "Step 1: Call the protected resource"
  step-2-fetch-protected-resource-metadata: "Step 2: Fetch protected resource metadata"
  step-3-fetch-authorization-server-metadata: "Step 3: Fetch authorization server metadata"
  how-protected-resource-metadata-relates-to-other-concepts: How Protected Resource Metadata relates to other concepts
  a-supporting-protocol-for-dynamic-ai: A supporting protocol for dynamic AI
  how-it-differs-from-cimd: How it differs from CIMD
  key-takeaways: Key takeaways
---

# Protected Resource Metadata in the AuthPlayground

Helping AI clients discover how to get authorized.

Sarah asks the AI assistant to prepare her for a meeting with Apex Logistics. The AI assistant discovers an MCP server or API it needs to call, but doesn't know how these resources are protected or which authorization server to use.

OAuth 2.0 Protected Resource Metadata ([RFC 9728](https://datatracker.ietf.org/doc/html/rfc9728)) provides a standard way for clients to discover authorization information for protected resources.

## The protected resource metadata model

This protocol enables a client to discover information about a protected resource, including which authorization server protects it. The flow looks like this:

1. An AI or MCP client calls the protected resource.

2. The protected resource returns a `401` with `resource_metadata` that identifies the authorization server.

3. The client uses the metadata for OAuth authorization.

The resource tells the client that it requires authorization and provides the metadata needed to discover how it's protected.

## The AuthPlayground implementation

**Entities involved**: Client application, authorization server B, resource server

The AuthPlayground demonstrates the [Protected Resource Metadata](https://www.authplayground.dev/flows/resource-metadata) flow in three steps:

1. Call the protected resource.

2. Fetch protected resource metadata.

3. Fetch authorization server metadata.

### Step 1: Call the protected resource

The client calls the resource without an access token:

```json
GET /rs/api/data
```

The error response indicates that the resource is protected and provides a link to the metadata:

```json
401 Unauthorized

WWW-Authenticate: Bearer
  resource_metadata=".../.well-known/oauth-protected-resource/rs"
```

This link tells the client where to retrieve metadata about the protected resource.

### Step 2: Fetch protected resource metadata

The client retrieves the metadata:

```json
GET /.well-known/oauth-protected-resource/rs
```

The metadata identifies the authorization server and describes capabilities such as scopes and DPoP support:

```json
{
  "resource": "https://.../rs",
  "authorization_servers": [
    "https://.../idp"
  ],
  "scopes_supported": [
    "openid",
    "profile",
    "email",
    "read",
    "write"
  ],
  "dpop_signing_alg_values_supported": [
    "RS256",
    "ES256"
  ]
}
```

### Step 3: Fetch authorization server metadata

The client retrieves metadata from the advertised authorization server:

```json
GET /.well-known/oauth-authorization-server/idp
```

The response includes capabilities such as the authorization endpoint, token endpoint, PAR, PKCE, and other supported OAuth features. The client can use this information for authorization.

## How Protected Resource Metadata relates to other concepts

### A supporting protocol for dynamic AI

Sarah's AI assistant discovers an MCP server it needs for the Apex Logistics workflow. In dynamic AI and MCP environments, clients might not have every resource and authorization configuration hard coded ahead of time. Protected resource metadata doesn't identify the agent, authorize Sarah, establish delegation, or determine what the AI can do. Its job is to help the client discover how a protected resource expects access to be authorized.

### How it differs from CIMD

Protected Resource Metadata and [Client ID Metadata Documents (CIMD)](authplayground-cimd.html) solve opposite sides of the discovery problem. CIMD helps an authorization server discover metadata about the client. Protected resource metadata helps a client discover which authorization server protects the resource and how to reach it.

Neither protocol grants access or establishes trust by itself. Discovery provides information that must be validated and evaluated under the appropriate security policy.

## Key takeaways

Protected Resource Metadata isn't an AI-specific identity protocol. It's standard OAuth infrastructure that's useful when AI applications and MCP clients interact with resources dynamically. It contributes to the Identity for AI story by enabling an AI client to discover not only a resource, but also the authorization infrastructure required to access it.

---

---
title: Pushed Authorization Requests (PAR) in the AuthPlayground
description: Explore how Pushed Authorization Requests establish OAuth requests before browser redirects in the AuthPlayground.
component: identity-for-ai
page_id: identity-for-ai:protocols:authplayground-par
canonical_url: https://developer.pingidentity.com/identity-for-ai/protocols/authplayground-par.html
llms_txt: https://developer.pingidentity.com/identity-for-ai/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-08-24T07:38:08Z
keywords: ["Identity for AI", "OAuth protocols", "PAR", "Pushed Authorization Requests", "AuthPlayground"]
section_ids:
  the-par-model: The PAR model
  why-this-matters-for-enterprise-ai: Why this matters for enterprise AI
  the-authplayground-implementation: The AuthPlayground implementation
  step-1-push-the-authorization-request: "Step 1: Push the authorization request"
  step-2-send-the-request_uri-through-the-browser: "Step 2: Send the request_uri through the browser"
  why-the-request_uri-matters: Why the request_uri matters
  step-3-exchange-the-authorization-code: "Step 3: Exchange the authorization code"
  how-par-relates-to-other-concepts: How PAR relates to other concepts
  par-and-pkce-protect-different-parts-of-the-flow: PAR and PKCE protect different parts of the flow
  par-and-rar-work-together-naturally: PAR and RAR work together naturally
  a-supporting-protocol-for-enterprise-ai: A supporting protocol for enterprise AI
  key-takeaways: Key takeaways
---

# Pushed Authorization Requests (PAR) in the AuthPlayground

Establishing the authorization request before the browser redirect.

Sarah asks the AI assistant to prepare her for the Apex Logistics meeting. Before an application can access protected information on Sarah's behalf, it might need to send an OAuth authorization request.

In a traditional OAuth flow, an application sends authorization parameters (such as `client_id`, `redirect_uri`, requested scopes, Proof Key for Code Exchange (PKCE) challenge, state, and potentially richer authorization information) through the browser to the authorization server. PAR ([RFC 9126](https://datatracker.ietf.org/doc/html/rfc9126)) changes this dynamic.

## The PAR model

Instead of passing the full request through the browser, with PAR the client sends these parameters directly to the authorization server before the browser redirect begins. The authorization server validates and stores the request, returning a short-lived reference called a `request_uri`. The browser carries only this reference, instead of sensitive authorization details. This is the PAR flow:

1. The client sends the full authorization request to the PAR endpoint.

2. The PAR endpoint returns a `request_uri` to the client.

3. The browser carries the `request_uri` to the authorization endpoint.

### Why this matters for enterprise AI

AI can change is the richness of the authorization request. An AI workflow might need to request a particular set of resources or permissions. If [Rich Authorization Requests (RAR)](authplayground-rar.html) are also being used, the request might contain structured `authorization_details` describing a specific operation.

As requests become richer, establishing them directly with the authorization server becomes useful. The browser still participates in the user-facing authorization flow, but it doesn't need to carry the complete authorization request.

## The AuthPlayground implementation

**Entities involved**: Client application, IdP (authorization server)

The AuthPlayground demonstrates the [Pushed Authorization Requests](https://www.authplayground.dev/flows/par) flow in three steps:

1. Push the authorization request to the PAR endpoint.

2. Send the authorization request with the `request_uri` through the browser.

3. Exchange the authorization code at the token endpoint.

### Step 1: Push the authorization request

The client sends the authorization request parameters directly to the PAR endpoint:

```json
POST /idp/par
Content-Type: application/x-www-form-urlencoded

client_id=playground-demo-client
client_secret=playground-demo-secret
redirect_uri=https://.../callback
response_type=code
scope=openid profile email
state=<state>
code_challenge=<pkce_challenge>
code_challenge_method=S256
```

Notice that the client communicates directly with the authorization server rather than placing these parameters in the browser-facing authorization URL. The playground uses client authentication at the PAR endpoint through `client_id` and `client_secret`. [PKCE](authplayground-pkce.html) is already part of the request.

The authorization server processes the pushed request and returns:

```json
{
  "request_uri": "urn:ietf:params:oauth:request_uri:515c113d-0b97-4453-b52f-42d2dbac0b1b",
  "expires_in": 60
}
```

The important value is `request_uri`. It's a short-lived reference to the authorization request the server has already received. In the playground flow, the reference expires after 60 seconds.

### Step 2: Send the `request_uri` through the browser

The client can now start the user-facing authorization flow. Instead of reconstructing the original authorization request in the URL, it sends only the `request_uri` and `client_id`:

```json
GET /idp/authorize
    request_uri=urn:ietf:params:oauth:request_uri:515c113d-0b97-4453-b52f-42d2dbac0b1b
    client_id=playground-demo-client
```

Compare the direct PAR request with the browser request. The direct request contained:

```
client_id
client_secret
redirect_uri
response_type
scope
state
code_challenge
code_challenge_method
```

The front-channel browser request is now essentially the `request_uri` and `client_id`.

The authorization server uses the `request_uri` to retrieve the authorization request established in Step 1. After the user-facing authorization process succeeds, the server redirects back to the registered callback with an authorization code and the original state. This is the key change PAR introduces: the authorization request is established directly with the authorization server before the browser redirect.

#### Why the `request_uri` matters

The `request_uri` is more than just a shorter URL. It refers to authorization parameters that the authorization server has already received and processed through the PAR endpoint. This reduces reliance on the browser to carry the full authorization request and gives the authorization server an opportunity to validate the pushed parameters before user interaction proceeds. RFC 9126 also requires the `request_uri` returned by the PAR endpoint to be bound to the client that pushed the authorization request.

### Step 3: Exchange the authorization code

Once authorization succeeds, the client exchanges the authorization code at the token endpoint. The playground uses PKCE:

```json
POST /idp/token
Content-Type: application/x-www-form-urlencoded

{
  "grant_type": "authorization_code",
  "code": "<authorization_code>,
  "redirect_uri": "https://.../callback",
  "client_id": "playground-demo-client",
  "code_verifier": "<code_verifier>"
}
```

The authorization server verifies the authorization code and the PKCE verifier before issuing tokens. The playground returns an access token and ID token:

```json
{
  "token_type": "Bearer",
  "expires_in": 3600,
  "scope": "openid profile email",
  "access_token": "<access_token>",
  "id_token": "<id_token>"
}
```

PAR has already done its job by this point. The token request itself is the familiar Authorization Code flow with PKCE. What changed was how the authorization request reached the authorization server.

## How PAR relates to other concepts

### PAR and PKCE protect different parts of the flow

The playground makes the relationship between PAR and PKCE easy to see:

* PAR establishes the authorization request directly with the authorization server.

* PKCE protects redemption of the authorization code.

In Step 1, the client pushes a `code_challenge`. In Step 3, the client presents the corresponding `code_verifier`. The same flow gets protection at two different points. PAR protects the authorization request itself, while PKCE protects the authorization code redemption. PAR and PKCE are complementary, rather than alternatives.

### PAR and RAR work together naturally

RAR can make an authorization request more expressive. Instead of requesting only a simple scope such as `customer.read`, an application can use `authorization_details` to describe a specific operation:

```json
{
  "type": "customer_information",
  "actions": ["read"],
  "identifier": "apex-logistics"
}
```

PAR provides a natural way to deliver a request containing that richer authorization information directly to the authorization server.

The PAR playground flow doesn't include `authorization_details` and that's okay. PAR doesn't depend on RAR, but they work well together when an authorization request contains richer information.

### A supporting protocol for enterprise AI

Return to Sarah's meeting preparation. Suppose the AI assistant needs authorization to retrieve customer information. Without PAR, the browser-facing authorization request might need to carry the parameters describing that authorization.

With PAR, the application first establishes the request directly:

1. The AI assistant sends authorization parameters directly to the authorization server.

2. The authorization server returns a `request_uri`.

3. Sarah's browser sends the `request_uri` to the authorization server.

Sarah still goes through the normal user-facing authentication and authorization experience. PAR changes what happens before that interaction. The detailed authorization request between the client and the authorization server has already been established.

PAR is an OAuth security mechanism, not an AI-specific protocol. The same pattern can protect authorization requests for traditional web applications, financial applications, mobile applications, and other OAuth clients.

PAR's relevance to enterprise AI comes from the same reason it's useful elsewhere: clients increasingly need to send security-sensitive or detailed authorization requests. These requests benefit from being established directly with the authorization server. AI gives us another environment where richer authorization flows are likely to appear.

## Key takeaways

PAR operates at the authorization request layer and has a deliberately narrow job. It doesn't determine what Sarah is allowed to do or what an AI agent might access. Instead it changes how the authorization request reaches the authorization server.

---

---
title: Rich Authorization Requests (RAR) in the AuthPlayground
description: Explore how Rich Authorization Requests express fine-grained operations that OAuth policies can evaluate in the AuthPlayground.
component: identity-for-ai
page_id: identity-for-ai:protocols:authplayground-rar
canonical_url: https://developer.pingidentity.com/identity-for-ai/protocols/authplayground-rar.html
llms_txt: https://developer.pingidentity.com/identity-for-ai/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-08-24T07:38:08Z
keywords: ["Identity for AI", "OAuth 2.0 protocols", "rich authorization requests", "RAR", "fine-grained authorization", "enterprise AI", "AuthPlayground"]
section_ids:
  the-rar-model: The RAR model
  authorization-details-structure: Authorization details structure
  the-authplayground-implementation: The AuthPlayground implementation
  step-1-send-authorization-details: "Step 1: Send authorization details"
  the-user-can-authorize-a-specific-operation: The user can authorize a specific operation
  step-2-exchange-the-authorization-code: "Step 2: Exchange the authorization code"
  step-3-enforce-authorization-at-the-resource-server: "Step 3: Enforce authorization at the resource server"
  how-rar-relates-to-other-concepts: How RAR relates to other concepts
  giving-policy-better-information: Giving policy better information
  rar-isnt-limited-to-human-initiated-ai: RAR isn't limited to human-initiated AI
  rar-and-scopes-are-complementary: RAR and scopes are complementary
  rar-and-par-work-together-naturally: RAR and PAR work together naturally
  key-takeaways: Key takeaways
---

# Rich Authorization Requests (RAR) in the AuthPlayground

Constraining what AI is allowed to do.

Sarah asks the company's AI assistant to prepare her for a meeting with Apex Logistics. She has broad access across customer systems and can read opportunities, update records, access multiple accounts, and perform other actions required by her role.

The AI assistant's task is much narrower and requires only a specific set of information. What the AI assistant needs to do isn't the same as what Sarah can do. RAR ([RFC 9396](https://datatracker.ietf.org/doc/html/rfc9396)) provides a way for an OAuth client to describe a specific operation it wants to perform.

## The RAR model

OAuth scopes are useful for describing general capabilities. An application can request something such as `customer.read`. Some authorization decisions need more context, such as:

```
Action: Read
Customer: Apex Logistics
Data: Relevant account context
```

RAR adds the `authorization_details` parameter to OAuth, allowing clients to describe authorization requirements in a structured, machine-readable form. Authorization details can include type, actions, resource information, and other constraints. These details provide more precise information than a flat scope string alone.

### Authorization details structure

An authorization detail is a structured JSON object. Its fields depend on the type of authorization requested. An enterprise AI API example might look like this:

```json
{
  "type": "customer_information",
  "actions": ["read"],
  "identifier": "apex-logistics"
}
```

RAR gives the API a structured way to describe what is being requested. Instead of asking only for `customer.read`, the request describes which customer, which action, and any other constraints that matter to policy.

## The AuthPlayground implementation

**Entities involved**: Client application, IdP (authorization server), resource server

The AuthPlayground demonstrates the [Rich Authorization Requests](https://www.authplayground.dev/flows/rar) flow in three steps:

1. Send the authorization request with `authorization_details`.

2. Exchange the authorization code.

3. Enforce authorization at the resource server.

The playground uses a payment initiation example that makes fine-grained authorization easy to see.

### Step 1: Send authorization details

The client begins an OAuth authorization request. Alongside the usual OAuth and Proof Key for Code Exchange (PKCE) parameters, it sends `authorization_details`. The request looks like this:

```json
GET /idp/authorize

response_type=code
client_id=playground-demo-client
scope=openid
code_challenge=<pkce_challenge>
code_challenge_method=S256
authorization_details=<structured_json>
```

The decoded authorization details include the specific operation requested:

```json
[
  {
    "type": "payment_initiation",
    "instructedAmount": {
      "amount": "123.50",
      "currency": "USD"
    },
    "creditorName": "Merchant Inc",
    "creditorAccount": {
      "iban": "DE75512108001245126199"
    }
  }
]
```

Compared with a broader permission such as `payment`, the structured request tells the authorization system much more. This is the value of RAR. The authorization request describes the specific operation that needs authorization.

#### The user can authorize a specific operation

Because authorization details are structured, the authorization server can evaluate the exact operation requested. Instead of just asking if the application is allowed to make payments, the request asks if the application can make a $123.50 USD payment to Merchant Inc at a specific destination account. This is a more meaningful authorization decision. The user authorizes a particular operation rather than granting an abstract capability with little context.

### Step 2: Exchange the authorization code

The client exchanges the authorization code using the standard Authorization Code flow with PKCE. The playground request is:

```json
POST /idp/token
Content-Type: application/x-www-form-urlencoded

grant_type=authorization_code
code=<authorization_code>
redirect_uri=<callback>
client_id=playground-demo-client
code_verifier=<code_verifier>
```

The response contains an access token. The decoded token contains:

```json
{
  "sub": "demo-user@example.com",
  "scope": "openid",
  "client_id": "playground-demo-client",
  "authorization_details": [
    {
      "type": "payment_initiation",
      "instructedAmount": {
        "amount": "123.50",
        "currency": "USD"
      },
      "creditorName": "Merchant Inc",
      "creditorAccount": {
        "iban": "DE75512108001245126199"
      }
    }
  ]
}
```

Notice that the scope is `openid`, but the token also carries the richer authorization context. This level of detail can't be expressed with a flat scope string.

### Step 3: Enforce authorization at the resource server

The client calls the protected resource using the access token:

```json
GET /rs/resource

Authorization: Bearer <access_token>
```

The resource server validates the token and the authorization information associated with it. The response shows that the same structured authorization context is available at the protected resource:

```json
{
  "message": "Access granted to protected resource",
  "user": "demo-user@example.com",
  "authorization_details": [
    {
      "type": "payment_initiation",
      "instructedAmount": {
        "amount": "123.50",
        "currency": "USD"
      },
      "creditorName": "Merchant Inc",
      "creditorAccount": {
        "iban": "DE75512108001245126199"
      }
    }
  ]
}
```

The resource server isn't working from a generic statement that the user can make payments. It has structured context describing the authorized operation. This gives downstream policy something more precise to enforce.

## How RAR relates to other concepts

### Giving policy better information

Fine-grained authorization becomes essential when AI can take actions rather than simply retrieve information. Consider three requests against the same Apex Logistics account:

* Reading the opportunity is low risk

* Updating the forecast is higher risk

* Deleting the opportunity is high risk

These operations require different policy decisions. Structured authorization details give policy enough context to distinguish between them. A `read` action might be allowed automatically. An update requires additional controls. A destructive operation requires approval or is denied entirely.

RAR doesn't define business policies or a meeting preparation authorization model. It gives the authorization system a precise description of the operation to enable policies to make better decisions. The API then defines what these authorization details mean.

### RAR isn't limited to human-initiated AI

Sarah is a useful example, but RAR isn't inherently tied to a human user. Autonomous workloads also need fine-grained authorization. For example, an autonomous action agent might request a specific operation, sending `authorization_details` to the authorization server to obtain constrained authorization. The agent operates under its own machine authority and authorization details help establish what the agent is allowed to do, whether it's acting for a person or autonomously.

### RAR and scopes are complementary

RAR doesn't mean scopes disappear. Authorization details and scopes describe different parts of the authorization model. Scopes present broad capabilities, while authorization details describe fine-grained authorization requirements.

An API might use scopes, authorization details, or both depending on how its authorization model is designed. The important distinction is that RAR provides richer structure when a flat capability string isn't enough.

### RAR and PAR work together naturally

As authorization requests become richer, they can also become larger and more sensitive. This is where [Pushed Authorization Requests (PAR)](authplayground-par.html) complement RAR. PAR defines how the authorization request reaches the authorization server, pushing the request directly to the server before the browser redirect. RAR defines what is being requested. The two protocols solve different parts of the authorization problem.

## Key takeaways

RAR doesn't establish identity. It gives the authorization system a structured description of the requested operation. RAR authorizes the specific operation, not just the caller. The authorization server evaluates the structured request, the access token carries the resulting authorization context, and the resource server enforces what's authorized.

---

---
title: Secure Production Identity Framework for Everyone (SPIFFE) in the AuthPlayground
description: Explore how SPIFFE gives AI agents and other workloads verifiable identities in the AuthPlayground.
component: identity-for-ai
page_id: identity-for-ai:protocols:authplayground-spiffe
canonical_url: https://developer.pingidentity.com/identity-for-ai/protocols/authplayground-spiffe.html
llms_txt: https://developer.pingidentity.com/identity-for-ai/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-08-24T07:38:08Z
keywords: ["Identity for AI", "OAuth 2.0 protocols", "OpenID Connect", "SPIFFE", "SVID", "JWT-SVID", "workload identity", "autonomous AI", "non-human identity", "NHI", "SPIRE", "AuthPlayground"]
section_ids:
  the-spiffe-model: The SPIFFE model
  static-credentials-are-a-poor-fit: Static credentials are a poor fit
  spiffe-ids-and-svids: SPIFFE IDs and SVIDs
  the-authplayground-implementation: The AuthPlayground implementation
  step-1-fetch-a-jwt-svid: "Step 1: Fetch a JWT-SVID"
  step-2-load-the-jwt-trust-bundle: "Step 2: Load the JWT trust bundle"
  step-3-authenticate-to-the-resource-server: "Step 3: Authenticate to the resource server"
  applying-this-to-an-ai-agent: Applying this to an AI agent
  how-spiffe-relates-to-other-concepts: How SPIFFE relates to other concepts
  identity-and-authorization-are-different: Identity and authorization are different
  human-identity-isnt-required: Human identity isn't required
  when-human-delegation-matters: When human delegation matters
  where-the-idp-fits-in: Where the IdP fits in
  bridging-spiffe-into-oauth: Bridging SPIFFE into OAuth
  key-takeaways: Key takeaways
---

# Secure Production Identity Framework for Everyone (SPIFFE) in the AuthPlayground

Identity for workloads running enterprise AI.

Enterprise AI is increasingly made up of software talking to software. A typical AI platform might contain an orchestrator, planner agents, retrieval agents, policy services, MCP gateways, and other internal services. For example, a request might flow through the following components:

* **AI orchestrator**: Directs the overall flow and calls the planner agent.

* **Planner agent**: Decides what work needs to happen and delegates to other agents.

* **Retrieval agent**: Gathers information needed by another agent or application.

* **Policy service**: Evaluates decisions.

* **MCP gateway**: Provides controlled connectivity between AI workloads and tools or APIs.

These workloads can operate autonomously. They call each other and perform work without a human participating in every interaction. For one workload to trust another, they need a way to verify the identity of the caller. This is the problem [SPIFFE](https://spiffe.io/docs/latest/spiffe-specs/spiffe/) is designed to address.

## The SPIFFE model

A workload is software performing work. AI agents, MCP gateways, microservices, and other running processes are non-human identities (NHI). They don't need to represent a human to have an identity.

### Static credentials are a poor fit

Imagine the enterprise runs its AI platform on a Kubernetes cluster with these workloads:

```
Kubernetes Cluster

├── planner-agent-7d9f8
├── planner-agent-3b2c1
├── retrieval-agent-82ad4
├── mcp-gateway-5e921
└── policy-service-91ba3
```

These workloads can scale, restart, move between nodes, or exist briefly. Giving them long-lived API keys or shared secrets creates a weak relationship between the credential and the actual workload.

A shared secret tells us that a caller knows the secret. It doesn't tell us that it's the workload the system intended to trust. Network location isn't enough either. Knowing a call comes from inside the Kubernetes cluster isn't the same as knowing it's the legitimate retrieval workload. SPIFFE provides a standardized identity model for workloads.

### SPIFFE IDs and SVIDs

SPIFFE identifies a workload using a SPIFFE ID. A SPIFFE ID looks like a URI:

```
spiffe://bxcompany.internal/agents/planner
spiffe://bxcompany.internal/agents/retrieval
spiffe://bxcompany.internal/gateways/mcp
```

* The first part of the ID identifies the SPIFFE trust domain: `spiffe://bxcompany.internal`.

* The remainder identifies the workload within that domain: `/agents/retrieval`.

The workload proves its SPIFFE identity using a SPIFFE Verifiable Identity Document (SVID). SPIFFE supports different SVID forms. The playground demonstrates a JWT-SVID. To summarize the flow:

1. The running workload requests a verifiable identity from the SPIFFE Workload API.

2. The SPIFFE Workload API issues a JWT-SVID that serves as the verifiable workload identity.

SPIRE is an implementation of SPIFFE that can perform workload attestation and issue SVIDs. The workload doesn't simply claim whatever identity it wants. The SPIFFE implementation determines which identities the workload is entitled to receive.

## The AuthPlayground implementation

**Entities involved**: Client application, SPIFFE / SPIRE, resource server

The AuthPlayground demonstrates the [SPIFFE / SVID Workload Identity](https://www.authplayground.dev/flows/spiffe) flow in three steps:

1. Fetch a JWT-SVID.

2. Load the JWT trust bundle.

3. Authenticate to the resource server.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The playground exposes HTTP endpoints that model SPIFFE Workload API operations, making the flow easy to execute and inspect in a browser. The SPIFFE standard doesn't define `POST /spiffe/fetch-jwt-svid` as an HTTP API. The Workload API uses protocol buffers and RPCs, including the `FetchJWTSVID` operation. The playground HTTP calls are an interactive representation of SPIFFE operations, not the standardized transport. |

### Step 1: Fetch a JWT-SVID

The workload asks the SPIFFE Workload API for a JWT-SVID. The request looks like this:

```json
POST /spiffe/fetch-jwt-svid
Content-Type: application/json

{
  "audience": [
    "https://.../rs"
  ]
}
```

Notice that the workload supplies the audience it intends to authenticate to. It doesn't supply a requested `spiffe_id`. The SPIFFE Workload API determines which SPIFFE identities the workload is entitled to receive. This is an important part of the trust model.

The playground returns a JWT-SVID for the workload's SPIFFE ID:

```json
{
  "jwt_svids": [
    {
      "spiffe_id": "spiffe://example.org/workload/demo-service",
      "jwt_svid": "<jwt_svid>",
      "hint": "demo-workload",
      "expires_at": 1787450000
    }
  ]
}
```

The decoded JWT-SVID contains the following claims:

```json
{
  "sub": "spiffe://example.org/workload/demo-service",
  "iat": 1786578067,
  "exp": 1786581667,
  "aud": [
    "https://.../rs"
  ],
  "jti": "25bfe3f5-6348-4c52-a444-69eb31fa1fdb"
}
```

* `sub`: The workload's SPIFFE ID.

* `aud`: Identifies the audience for which this JWT-SVID was requested.

* `exp`: Keeps the credential time-bounded.

The SPIFFE Workload API specification defines JWT-SVID retrieval in an audience-oriented way. The workload requests JWT-SVIDs for a specific audience and receives SVIDs for identities that it's authorized to use.

### Step 2: Load the JWT trust bundle

The resource server needs a way to verify JWT-SVIDs issued by the SPIFFE trust domain. The playground models that as a separate verifier action:

```json
GET /spiffe/fetch-jwt-bundles
Accept: application/json
```

The response contains a bundle keyed by trust domain:

```json
{
  "bundles": {
    "spiffe://example.org": {
      "keys": [
        {
          "kty": "RSA",
          "kid": "spiffe-signing-key-1",
          "use": "jwt-svid",
          "alg": "RS256"
        }
      ]
    }
  }
}
```

The resource server can use this verification material to validate JWT-SVIDs from `spiffe://example.org`. To summarize the relationships:

* **SPIFFE trust domain**: Derives the JWT trust bundle.

* **JWT trust bundle**: Provides verification material.

* **Resource server**: Uses the bundle to verify the JWT-SVID.

This step doesn't have to occur for every individual API request. A verifier can load or refresh the bundle independently while validating JWT-SVIDs. The SPIFFE specification requires JWT bundles to be keyed by trust domain, and the verifier uses the bundle corresponding to the trust domain in the JWT-SVID subject. If it doesn't have a matching trusted bundle, the credential isn't trusted.

### Step 3: Authenticate to the resource server

The workload presents its JWT-SVID to the resource server:

```json
GET /rs/api/data

Authorization: Bearer <jwt_svid>
```

The resource server validates the JWT-SVID. Among other things, it can check:

* **Signature**: Was this JWT-SVID signed by the trusted SPIFFE domain?

* **SPIFFE ID**: Which workload is presenting it?

* **Audience**: Was this JWT-SVID issued for this resource server?

* **Expiration**: Is the credential still valid?

The playground response confirms that access is granted:

```json
{
  "message": "Access granted to protected resource",
  "user": "spiffe://example.org/workload/demo-service",
  "authorization_details": null,
  "token_type": "Bearer"
}
```

There's no human user in this flow. The identity recognized by the resource server is `spiffe://example.org/workload/demo-service`. The software workload authenticated as itself.

#### Applying this to an AI agent

Replace the playground's generic `demo-service` with a real AI workload. Suppose the enterprise has a retrieval agent whose job is to gather customer context for other agents. The agent's SPIFFE ID is `spiffe://company.internal/agents/retrieval`. The flow looks like this:

1. The retrieval agent fetches a JWT-SVID from SPIFFE / SPIRE.

2. The retrieval agent authenticates as itself to the customer context service using the JWT-SVID.

3. The customer context service validates the SVID and establishes which workload is calling it.

The service doesn't have to trust the request just because it came from inside the network. Policy can decide whether the workload is allowed to perform the requested operation.

## How SPIFFE relates to other concepts

### Identity and authorization are different

A valid SPIFFE identity doesn't mean the workload can do anything it wants. SPIFFE / SVID defines which workload is making the request. Authorization policy defines what the workload is allowed to do. These are separate decisions.

The playground demonstrates successful authentication to the resource server with a JWT-SVID. A production architecture can layer whatever authorization policy is appropriate on top of the authenticated workload identity.

### Human identity isn't required

SPIFFE is particularly important for autonomous AI. Consider a monitoring agent reading platform telemetry. The monitoring agent might run continuously and inspect platform telemetry under its own machine authority. An employee doesn't have to initiate each request. The same applies to policy agents, maintenance services, background AI processes, and many agent-to-agent interactions.

### When human delegation matters

Consider Sarah asking the AI assistant to prepare her for a meeting. The AI platform might use several workloads to complete this task, such as a planner agent, a retrieval agent, and an MCP gateway.

SPIFFE can establish the identities of the participating software workloads, but not every interaction represents delegation from Sarah. The planner might call the retrieval agent under machine authority. Delegation becomes relevant only when an authorization decision depends on Sarah's identity or authority.

The architecture might need to know:

* Who is the software? SPIFFE / SVID confirms this is the legitimate MCP workload.

* Whose authority is involved? Delegated identity confirms that this operation involves Sarah's authority.

Delegation can be added when required, but isn't a prerequisite for workload identity.

### Where the IdP fits in

The SPIFFE playground flow doesn't involve an IdP. The SPIFFE identity system establishes the workload identity, and the resource server validates it using the SPIFFE trust bundle. An enterprise IdP isn't required for this interaction.

For human identity, the flow looks different:

1. Sarah authenticates via the IdP.

2. The IdP uses OIDC / OAuth to provide human identity and authorization context.

These are separate identity planes that operate independently:

* **IdP**: Who is the human?

* **SPIFFE / SPIRE**: Which workload is running?

### Bridging SPIFFE into OAuth

There are architectures where these worlds need to connect. Many enterprise APIs expect OAuth access tokens rather than accepting JWT-SVIDs directly. One integration pattern is to use a JWT-SVID as trusted workload context when requesting an OAuth token. The flow might look like this:

1. The running workload obtains a JWT-SVID from SPIFFE / SPIRE.

2. The workload presents the JWT-SVID to the enterprise authorization server for token exchange.

3. The enterprise authorization server validates the workload identity, applies enterprise policy, and issues an OAuth access token.

4. The enterprise API accepts the OAuth access token.

The responsibilities remain separate: SPIFFE establishes which workload it is, and the enterprise authorization server determines what the workload is allowed to do. The resulting OAuth token can preserve workload-related information, such as the SPIFFE ID, that's useful for downstream policy and auditing.

This is an integration pattern, not a requirement of SPIFFE. It isn't part of the playground demonstration.

## Key takeaways

Autonomous agents, MCP gateways, microservices, and other software components need identities of their own. SPIFFE provides a standard way to give workloads verifiable identities without requiring them to impersonate humans or rely on long-lived shared credentials. Human identity and delegation can be added when a business operation requires them.

---

---
title: Token Exchange in the AuthPlayground
description: Explore how OAuth Token Exchange preserves subject and actor identities while retargeting trust for enterprise AI access in the AuthPlayground.
component: identity-for-ai
page_id: identity-for-ai:protocols:authplayground-token-exchange
canonical_url: https://developer.pingidentity.com/identity-for-ai/protocols/authplayground-token-exchange.html
llms_txt: https://developer.pingidentity.com/identity-for-ai/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-08-24T07:38:08Z
keywords: ["Identity for AI", "OAuth 2.0 protocols", "token exchange", "RFC 8693", "delegation", "impersonation", "subject", "actor", "audience", "retargeting trust", "AuthPlayground"]
section_ids:
  the-token-exchange-model: The token exchange model
  the-authplayground-implementation: The AuthPlayground implementation
  step-1-obtain-subject-and-actor-tokens: "Step 1: Obtain subject and actor tokens"
  step-2-perform-the-delegation-token-exchange: "Step 2: Perform the delegation token exchange"
  the-difference-between-may_act-and-act: The difference between may_act and act
  whats-in-the-exchanged-token: What's in the exchanged token?
  retargeting-trust: Retargeting trust
  how-token-exchange-relates-to-other-protocol-concepts: How token exchange relates to other protocol concepts
  it-doesnt-always-require-a-human: It doesn't always require a human
  it-isnt-workload-identity: It isn't workload identity
  it-differs-from-id-jag-and-transaction-tokens: It differs from ID-JAG and transaction tokens
  key-takeaways: Key takeaways
---

# Token Exchange in the AuthPlayground

Retargeting trust for enterprise AI.

When Sarah asks her AI assistant to prepare a meeting briefing, the assistant needs to access customer data. In an enterprise AI architecture, the software component performing this work could be a Model Context Protocol (MCP) gateway, an AI agent, or a backend service brokering access to enterprise APIs. In the playground, an API gateway represents this software actor.

The authorization system must track two distinct identities:

1. **Sarah (the human subject):** Her authority allows access to customer data (the protected resource).

2. **The API gateway (the software actor):** The gateway acts on Sarah's behalf while accessing those APIs.

The software actor shouldn't impersonate Sarah or use a broad service credential that loses the connection to her identity. OAuth 2.0 Token Exchange ([RFC 8693](https://datatracker.ietf.org/doc/html/rfc8693)) solves this problem.

## The token exchange model

Token exchange provides a standard way to take an existing, trusted security context and request a new token for a different audience or purpose while preserving the delegation relationship.

Token exchange does more than simply convert a token. RFC 8693 distinguishes the subject from the actor in a delegated access token. The resulting token proves both that the access is for Sarah, and that the API gateway is the specific actor exercising this authority. This is delegation rather than impersonation.

## The AuthPlayground implementation

**Entities involved**: Client application, IdP (authorization server), resource server

The AuthPlayground demonstrates the [Token Exchange](https://www.authplayground.dev/flows/token-exchange) flow in two steps:

1. Obtain subject and actor tokens.

2. Perform the delegation token exchange.

### Step 1: Obtain subject and actor tokens

This step begins with an Authorization Code flow that creates both the subject (user) and actor credentials.

|   |                                                                                                                                                                                                                                                                                |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | In a production architecture, the human subject and software actor typically establish their credentials through separate identity lifecycles. For simplicity, the playground creates both credentials during the same prerequisite step, but they remain distinct identities. |

The executed request looks like this:

```json
POST /idp/token
Content-Type: application/x-www-form-urlencoded

{
  "grant_type": "authorization_code",
  "code": "<authorization_code>",
  "redirect_uri": "<callback>",
  "client_id": "playground-demo-client",
  "code_verifier": "<pkce_verifier>"
}
```

The response contains several artifacts. The access token represents the authenticated user context:

```json
{
  "sub": "demo-user@example.com",
  "scope": "openid delegation",
  "client_id": "playground-demo-client",
  "aud": "playground-demo-client"
}
```

The ID token represents the same user. Notice the `may_act` claim. This claim indicates that `api-gateway@example.com` is eligible to act on behalf of the subject.

```json
{
  "sub": "demo-user@example.com",
  "email": "demo-user@example.com",
  "may_act": {
    "sub": "api-gateway@example.com"
  }
}
```

The response also contains an `actor_token` that represents the API gateway identity. This token is used to identify the actor in the delegation exchange.

```json
{
  "sub": "api-gateway@example.com",
  "client_id": "playground-demo-client",
  "iss": "https://.../idp",
  "aud": "https://.../idp"
}
```

Before token exchange happens, two distinct identities have been established:

* **Subject**: The party on whose behalf the token is being requested. In the `subject_token` this is `demo-user@example.com`.

* **Actor**: The party that will exercise the delegated authority. In the `actor_token` this is `api-gateway@example.com`.

### Step 2: Perform the delegation token exchange

The client application sends a token exchange request with both tokens to the authorization server:

```json
POST /idp/token
Content-Type: application/x-www-form-urlencoded

{
  "grant_type": "urn:ietf:params:oauth:grant-type:token-exchange",
  "subject_token": "<id_token>",
  "subject_token_type": "urn:ietf:params:oauth:token-type:id_token",
  "actor_token": "<actor_token>",
  "actor_token_type": "urn:ietf:params:oauth:token-type:access_token",
  "requested_token_type": "urn:ietf:params:oauth:token-type:access_token",
  "audience": "<resource_server>",
  "client_id": "playground-demo-client",
  "scope": "openid read"
}
```

Important inputs:

* `subject_token`: Identifies Sarah as the subject.

* `actor_token`: Identifies the API gateway performing the action.

* `requested_token_type`: Asks for an OAuth access token.

* `audience`: Targets the token to the protected resource.

* `scope`: Defines the permissions needed for this operation.

The authorization server evaluates the request using the `may_act` claim from the subject token to verify that the gateway is authorized to act for Sarah. If policy allows the exchange, the server issues a new access token.

#### The difference between `may_act` and `act`

These claims represent different stages of delegation:

* **Before the exchange:** The `may_act` claim in the subject token expresses an authorized relationship (the gateway is eligible to act for Sarah).

* **After the exchange:** The `act` claim in the new access token identifies the actual actor (the API gateway) currently exercising this delegated authority.

#### What's in the exchanged token?

The new composite access token contains:

```json
{
  "sub": "demo-user@example.com",
  "scope": "openid read",
  "client_id": "playground-demo-client",
  "act": {
    "sub": "api-gateway@example.com",
    "iss": "https://.../idp"
  },
  "iss": "https://.../idp",
  "aud": "https://.../rs"
}
```

This resource-facing token preserves the entire context: the human subject (`sub`), the software actor (`act`), the target resource (`aud`), and the requested permissions (`scope`).

The same model applies when an MCP gateway brokers access to enterprise systems such as Salesforce or ServiceNow. While specific integrations vary, the principle remains the same: preserve the subject and actor relationship while issuing a security context appropriate for the target.

#### Retargeting trust

The original identity token was intended for the client application. The exchanged access token is intended for the resource server. Token exchange retargets trust by changing the security context instead of simply copying Sarah's original token.

```
ID Token                                 Access Token
sub = Sarah            ------->          sub = Sarah
aud = Client           Token Exchange    act = API Gateway
may_act = API Gateway                    aud = Resource Server
                                         scope = read
```

## How token exchange relates to other protocol concepts

### It doesn't always require a human

While the playground demonstrates human delegation, token exchange also applies to machine-oriented flows where the subject is a workload. The key requirement isn't a human user, but rather the need to transform a trusted security context into a new token appropriate for the requested target.

### It isn't workload identity

Don't confuse the `actor_token` with the broader [workload identity](authplayground-spiffe.html) problem.

* **Workload identity (SPIFFE / SVID):** Establishes trust in a runtime workload (which workload is this?).

* **Token exchange:** Transforms an existing security context (what token should be issued for the requested target?).

A production system might use workload identity (such as a SPIFFE JWT-SVID) as a trusted source to establish the actor during a token exchange. The token exchange flow in the playground doesn't demonstrate this specific integration.

### It differs from ID-JAG and transaction tokens

[ID-JAG](authplayground-xaa-id-jag.html) is a specific profile used to carry delegated user identity into another authorization domain. Token exchange can act as a building block for ID-JAG, but they are not synonymous.

[Transaction tokens](authplayground-transaction-tokens.html) carry trusted transaction context through a workload call chain inside a trust domain. Token exchange is the mechanism used when a calling workload requests a Txn-Token from the token service.

## Key takeaways

The key to token exchange is distinguishing between the subject and the actor. In the enterprise AI scenario, Sarah is the subject and the API gateway is the actor.

Before the exchange, `may_act` indicates that the gateway is eligible to act for Sarah. During the exchange, the client sends Sarah's `subject_token` and the gateway's `actor_token`. After policy evaluation, the resulting access token keeps Sarah as `sub` and records the gateway in `act`.

Token exchange gives the resource-facing security context a much more accurate story than either of these alternatives:

* Sarah made the API call directly.

* A generic gateway service account made the API call.

Neither alternative is entirely true. The reality is that the API gateway (or an MCP gateway in an enterprise AI architecture) acts using authority delegated from Sarah for this audience and requested access. Token exchange represents this distinction.

---

---
title: Transaction Tokens in the AuthPlayground
description: Explore how transaction tokens preserve trusted context through distributed AI service call chains in the AuthPlayground.
component: identity-for-ai
page_id: identity-for-ai:protocols:authplayground-transaction-tokens
canonical_url: https://developer.pingidentity.com/identity-for-ai/protocols/authplayground-transaction-tokens.html
llms_txt: https://developer.pingidentity.com/identity-for-ai/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-08-24T07:38:08Z
keywords: ["Identity for AI", "OAuth 2.0 protocols", "transaction tokens", "TTS", "trust domain", "call chain", "distributed AI workflows", "AuthPlayground"]
section_ids:
  the-transaction-token-model: The transaction token model
  whats-a-trust-domain: What's a trust domain?
  a-human-isnt-required: A human isn't required
  the-authplayground-implementation: The AuthPlayground implementation
  step-1-obtain-the-subject-token: "Step 1: Obtain the subject token"
  step-2-request-the-transaction-token: "Step 2: Request the transaction token"
  step-3-propagate-the-transaction-token: "Step 3: Propagate the transaction token"
  how-transaction-tokens-relate-to-other-concepts: How transaction tokens relate to other concepts
  the-difference-between-principals-and-requesting-workloads: The difference between principals and requesting workloads
  transaction-tokens-versus-workload-identity: Transaction tokens versus workload identity
  transaction-tokens-and-token-exchange-solve-different-problems: Transaction tokens and token exchange solve different problems
  transaction-tokens-differ-from-id-jag: Transaction tokens differ from ID-JAG
  key-takeaways: Key takeaways
  short-lifetimes-matter: Short lifetimes matter
  keeping-the-call-chain-understandable: Keeping the call chain understandable
---

# Transaction Tokens in the AuthPlayground

Preserving trusted context through a chain of microservices.

Enterprise AI workflows often involve multiple services. Consider a planner agent that needs customer information to complete a task. It asks a retrieval agent to gather the information, and the retrieval agent calls account context and customer intelligence services.

As the request moves through the call chain, each service can usually identify its direct caller. Preserving the trusted context behind the overall transaction is more difficult. Several hops later, a service might know that it was called by the customer intelligence service. The enterprise needs to know:

* Which transaction does this call belong to?

* Which principal is associated with the transaction?

* Which workload originally requested the transaction token?

* What's the purpose or authorization scope of this transaction?

* Is this context valid inside this trust domain?

* Is the token still current?

Transaction tokens ([IETF draft](https://datatracker.ietf.org/doc/draft-ietf-oauth-transaction-tokens/)) carry trusted context through the call chain.

## The transaction token model

A transaction token is a short-lived, signed JSON Web Token (JWT) associated with a specific transaction and trust domain. It carries information such as:

* `sub`: Who or what is the principal of this transaction?

* `txn`: Which transaction is this?

* `req_wl`: Which workload requested the transaction token?

* `aud`: Which trust domain is this token valid in?

* `scope`: What's the purpose or authorization scope?

* `exp`: How long is this context valid?

* `iat`: When was this token issued?

A simplified example looks like this:

```json
Header {
  "typ": "txntoken+jwt",
  "alg": "RS256",
  "kid": "transaction-token-signing-key"
}

body
{
  "sub": "demo-user@example.com",
  "txn": "txn-48291",
  "req_wl": "meeting-prep-agent.bx.internal",
  "aud": "bx-ai.internal",
  "scope": "customer.meeting-prep",
  "iat": 1786575243,
  "exp": 1786575303
}
```

Actual claims and values depend on the Transaction Token Service (TTS) and deployment requirements. Downstream workloads receive a cryptographically protected representation of the transaction instead of reconstructing the security context from arbitrary headers.

### What's a trust domain?

A trust domain is a group of systems that share a common set of security controls and policies. For example, an enterprise might operate several AI services inside one governed environment.

The transaction token is valid within that trust domain, which is why the `aud` claim is important. It doesn't represent an individual service (such as `aud = Account Context Service`). Instead, it represents the entire domain (such as `aud = AI Trust Domain`). Workloads must not accept a transaction token outside the trust domain identified by its `aud` claim.

### A human isn't required

A transaction token can support a human-initiated workflow, but a human isn't required. For autonomous workloads, the transaction might originate entirely from software. The principal represented by the transaction could be a workload instead of a person.

Consider an autonomous monitoring agent versus a human-initiated meeting preparation request. In the human-initiated request, Sarah is the principal. Transaction tokens preserve trusted authorization and request context through a call chain inside a trust domain for both patterns.

## The AuthPlayground implementation

**Entities involved**: Client application, transaction token service, resource server

The AuthPlayground demonstrates the [Transaction Token](https://www.authplayground.dev/flows/txn-tokens) flow in three steps:

1. Obtain the subject token.

2. Request the transaction token.

3. Propagate the transaction token.

### Step 1: Obtain the subject token

The calling workload obtains an OAuth access token from the authorization server:

```json
POST /idp/token
Content-Type: application/x-www-form-urlencoded

{
  "grant_type": "authorization_code",
  "code": "<authorization_code>",
  "redirect_uri": "<callback>",
  "client_id": "playground-demo-client",
  "code_verifier": "<pkce_verifier>"
}
```

The response contains an access token:

```json
{
  "token_type": "Bearer",
  "expires_in": 3600,
  "scope": "openid profile email",
  "access_token": "<access_token>",
  "id_token": "<id_token>"
}
```

The OAuth access token becomes the `subject_token` used when requesting the transaction token. It establishes the subject context from which the TTS can create transaction-scoped context.

|   |                                                                                                                                                                                                                                        |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The transaction token specification is broader than this example. A Txn-Token can represent externally or internally originated transactions. An OAuth user access token isn't required for every possible transaction token use case. |

### Step 2: Request the transaction token

The calling workload requests a transaction token from the TTS:

```json
POST /tts/token
Content-Type: application/x-www-form-urlencoded

{
  "grant_type": "urn:ietf:params:oauth:grant-type:token-exchange",
  "subject_token": "<subject_token>",
  "subject_token_type": "urn:ietf:params:oauth:token-type:access_token",
  "requested_token_type": "urn:ietf:params:oauth:token-type:txn_token",
  "audience": "example.org",
  "scope": "read write",
  "request_context": "{\"req_ip\":\"203.0.113.42\",\"authn\":\"urn:mace:incommon:iap:silver\"}",
  "request_details": "{\"action\":\"read\",\"resource\":\"/api/data\"}"
}
```

Notice the following details:

* `subject_token`: Provides the subject context for the transaction.

* `requested_token_type`: Explicitly asks for a transaction token.

* `audience`: Identifies the trust domain, not an individual downstream service.

* `scope`: Expresses the permissions associated with the transaction.

The specification defines `request_context` and `request_details` as recommended parameters. They give the TTS additional context about the transaction and request. In the playground, that information appears in the resulting transaction token as:

```json
{
  "rctx": {
    "req_ip": "203.0.113.42",
    "authn": "urn:mace:incommon:iap:silver"
  },
  "tctx": {
    "action": "read",
    "resource": "/api/data"
  }
}
```

The TTS identifies the calling workload, sets `req_wl`, validates the subject context, creates a unique `txn` identifier, and issues the short-lived transaction token.

### Step 3: Propagate the transaction token

The calling workload invokes a downstream service and sends the transaction token in the dedicated HTTP header:

```json
GET /rs/api/data

Txn-Token: <transaction_token>
```

The use of a separate `Txn-Token` header is deliberate. Workloads mustn't use the standard `Authorization` header to carry the Txn-Token because they might need that header for other purposes.

The receiving workload validates the transaction token before using it for authorization. It verifies:

* **Signature**: Is the token cryptographically valid?

* **aud**: Is it valid in this trust domain?

* **exp**: Is it still current?

* **Transaction context**: Does this context authorize the requested activity?

If the workload makes another downstream call as part of the same call chain, it propagates the transaction token onward unchanged to provide execution continuity.

## How transaction tokens relate to other concepts

### The difference between principals and requesting workloads

The TTS identifies the requesting workload using the `req_wl` claim. This answers which workload requested the transaction token.

This isn't the same thing as the transaction principal. In a human-driven workflow, Sarah might be the `sub`, while the meeting prep agent is the `req_wl`. This separation is useful in AI systems because the workload executing a transaction and the principal associated with that transaction aren't always the same.

### Transaction tokens versus workload identity

A transaction token contains a `req_wl` claim identifying the requesting workload. This shouldn't be confused with a complete workload identity system.

* [Workload identity](authplayground-spiffe.html) defines which running workload this is.

* Transaction tokens define the trusted transaction context the workload participates in.

In a broader architecture, SPIFFE can establish the identity of the workload requesting the transaction token. The TTS can use trusted workload authentication when deciding whether that workload is authorized to obtain one. These layers complement each other.

### Transaction tokens and token exchange solve different problems

Transaction tokens use the [Token Exchange](authplayground-token-exchange.html) protocol when requesting a token from the TTS, but the architectural purpose differs from the cross-domain token exchange pattern.

* Cross-domain token exchange moves trusted identity and authorization into **another** trust domain.

* Transaction tokens preserve trusted transaction context through a call chain **within** a trust domain.

### Transaction tokens differ from ID-JAG

[ID-JAG](authplayground-xaa-id-jag.html) is used when delegated user identity and authorization need to cross into another authorization domain. Transaction tokens are scoped to one trust domain and carry transaction context through a call chain. A single enterprise AI workflow can use both, but at different points and for different reasons.

## Key takeaways

### Short lifetimes matter

Transaction tokens are deliberately short-lived. They aren't intended to become a broadly reusable enterprise credential. The specification notes that transaction tokens aren't inherently replay-resistant. Short lifetimes are therefore important, and the unique `txn` identifier supports auditing and replay detection.

### Keeping the call chain understandable

Without transaction context, logs from a distributed AI workflow only show which services called each other. A shared `txn` identifier gives those calls a common transaction reference. When workloads log that identifier, the enterprise has a way to associate downstream activity with the transaction that caused it. This is valuable for debugging, authorization analysis, security investigation, and auditing.

Transaction tokens give the trust domain a way to keep context intact. The TTS creates a short-lived, signed token for the transaction that identifies the transaction principal, the requesting workload, the trust domain, and the authorized purpose. Workloads have identities and security controls of their own and the transaction token adds a trusted description of the transaction they're currently participating in.

---

---
title: What is Agent2Agent (A2A) protocol?
description: Learn how the Agent2Agent (A2A) protocol enables AI agents to discover, authenticate with, and delegate tasks to other agents across frameworks.
component: identity-for-ai
page_id: identity-for-ai:protocols:idai-what-is-a2a
canonical_url: https://developer.pingidentity.com/identity-for-ai/protocols/idai-what-is-a2a.html
llms_txt: https://developer.pingidentity.com/identity-for-ai/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-09-16T20:34:52Z
keywords: ["Identity for AI", "ai identity", "ai security", "ai governance", "agent to agent", "a2a"]
page_aliases: ["a2a:index.adoc"]
section_ids:
  why-use-a2a: Why use A2A?
  how-a2a-works: How A2A works
  workflow: Workflow
  learn-more: Learn more
---

# What is Agent2Agent (A2A) protocol?

Whereas Model Context Protocol (MCP) defines how agents interact with tools, [Agent2Agent (A2A) protocol](https://a2a-protocol.org/latest/) defines how agents interact with each other.

In an ecosystem where agents exist in different domains and are built upon different frameworks, A2A defines a standardized way for agents to collaborate as autonomous peers. In practice, this means an HR agent could securely call out to a payroll agent to adjust a salary, or a travel agent could ask a calendar agent to reschedule meetings, all under a trusted, reliable framework.

## Why use A2A?

To make agent-to-agent communication as streamlined as possible, A2A is designed around the following core principles:

**Discovery:** Agents can find other agents with the desired permissions and capabilities.

**Interoperability:** Agents can pass goals, intents, and structured requests regardless of which framework they're built on.

**Delegation and Chaining:** Agents can hand off tasks to better-suited agents without the end user needing to manually orchestrate it.

**Trust and Identity:** As with tools, agents need to authenticate with each other. A2A defines how identity and permissions are enforced when agents collaborate.

## How A2A works

An A2A interaction involves the following components:

* Agent card

  A discoverable JSON file that acts as an agent's public profile. It advertises the agent's identity, capabilities, supported data modalities, and authentication requirements.

  This allows other agents to determine the most suitable agent to interact with.

* Task

  The fundamental unit of work. A task has a unique ID and progresses through a defined lifecycle, such as working, completed, or input required.

* Message and artifact

  Messages are the units of communication exchanged between agents to manage a task, while artifacts are the final, tangible outputs generated upon task completion.

### Workflow

The typical A2A workflow involves a client agent discovering an agent card, authenticating as required, and then monitoring tasks through a series of API exchanges until the remote agent delivers the artifacts to the end user.

1. A client agent, acting on behalf of the user, discovers an agent card. This could be through open discovery, a curated registry, or private API endpoints.

2. The client agent authenticates and receives a token from the remote agent's authorization server.

3. The client agent invokes the `POST /sendMessage` API to send details about the task along with its access token to the remote agent.

   The remote agent can respond with a `Message` object to negotiate the scope of a request or with a `Task` object if the agent accepts the task request, containing the `contextId` and `taskId`.

4. The client agent invokes the `POST /sendMessageStream` API with the remote agent for real-time updates of long-running tasks using Server-Sent Events (SSE).

   When the task is complete, the remote agent responds with the artifacts and the `taskId` in completed status.

## Learn more

Use the following resources to learn more about implementing A2A:

* [A2A protocol documentation](https://a2a-protocol.org/dev/)

* [Tutorials and Samples](https://a2a-protocol.org/dev/tutorials/) in the A2A protocol documentation

* Google's [A2A protocol announcement](https://developers.googleblog.com/en/a2a-a-new-era-of-agent-interoperability/)

MCP defines how agents call tools, while A2A defines how agents call each other. Both protocols rely on strong identity controls to ensure that every request, whether to a tool or to another agent, is authenticated, authorized, and auditable. Learn more about how MCP and A2A interact in [A2A and MCP: Complementary Protocols for Agentic Systems](https://a2a-protocol.org/dev/topics/a2a-and-mcp/#a2a-mcp-complementary-protocols-for-agentic-systems) in the A2A protocol documentation.

---

---
title: What is Model Context Protocol (MCP)?
description: Learn how Model Context Protocol (MCP) standardizes AI agent connections to external tools, resources, and prompts.
component: identity-for-ai
page_id: identity-for-ai:protocols:idai-what-is-mcp
canonical_url: https://developer.pingidentity.com/identity-for-ai/protocols/idai-what-is-mcp.html
llms_txt: https://developer.pingidentity.com/identity-for-ai/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-06-17T00:00:00Z
keywords: ["model context protocol", "agent-tool integration", "capability discovery", "MCP", "tool connectors"]
page_aliases: ["agents:idai-what-is-mcp.adoc"]
section_ids:
  key-benefits: Key benefits
  architecture: Architecture
  workflow: Workflow
  security-challenges: Security challenges
---

# What is Model Context Protocol (MCP)?

The foundational challenge in scaling agentic systems is managing the connections between artificial intelligence (AI) agents and the vast array of tools they need to perform their work.

To solve real-world problems, AI agents require connections to external data and services, such as APIs and databases. Without a common standard, each integration must be written and maintained separately, creating brittle connections and duplicated effort. This approach doesn't scale, especially when multiple agents use the same tools.

The [Model Context Protocol (MCP)](https://modelcontextprotocol.io/docs/getting-started/intro), developed by Anthropic, addresses this challenge by standardizing how agents connect to tools. By providing a consistent layer for agent-tool interaction, MCP reduces friction for developers, simplifies maintenance, and creates a foundation for interoperable, secure agent ecosystems.

## Key benefits

MCP's standardized integration layer delivers:

* **Consistent connection semantics**: Developers can swap in a new tool without rewriting core integration logic.

* **Secure authentication and authorization**: MCP servers support OAuth 2.0, eliminating the need for hard-coded secrets or long-lived credentials.

* **Capability discovery**: Agents can automatically discover available tools, resources, and prompts instead of relying on hard-coded lists.

* **Reduced duplication**: Multiple agents can reuse the same MCP server, reducing the operational burden of maintaining separate connectors.

## Architecture

![Example agentic MCP flow](_images/idai-mcp-flow.png)

The MCP architecture includes three core components:

* MCP host

  The application that manages MCP clients and initiates connections to MCP servers. It provides the environment in which agents operate and interact with tools and resources. For example, an AI-powered IDE.

* MCP client

  The component inside the host that maintains a standardized connection with the MCP server. It acts as a bridge between the agent's reasoning and the server's tools, resources, and prompts. The client translates agent requests into MCP-compliant messages and processes server responses in a consistent way. For example, an embedded IDE client or chatbot agent connector.

* MCP server

  A program that exposes capabilities to AI applications in a standardized and discoverable way. It acts as the central repository of tools, resources, and prompts that agents can invoke. MCP servers support OAuth 2.0 for authentication and authorization, ensuring secure access, and can run locally within a host or remotely as a centralized service.

  An MCP server can expose three main types of capabilities:

  * **Tools**: Executable functions that an agent can invoke to perform specific actions.

  * **Resources**: Contextual data that informs agent reasoning, such as files, database records, or configuration information.

  * **Prompts**: Pre-defined, templated messages or workflows that agents can present to users or use internally to structure reasoning.

MCP's technical architecture is based on the [JSON-RPC 2.0](https://www.jsonrpc.org/specification) message format. This ensures that all interactions, such as tool invocation, resource retrieval, and prompt execution, follow a consistent pattern. Each message contains a unique identifier, method name, and parameters.

## Workflow

A typical MCP workflow unfolds as part of an agent's reasoning-action loop:

1. **Initialization**: The MCP host launches an MCP client, which connects to the MCP server. The client queries the server for available tools, resources, and prompts. The agent inspects this metadata to understand which capabilities are available before taking action.

2. **Invocation**: When the agent determines that a specific tool or resource is needed, the MCP client sends a JSON-RPC request to the server, specifying the method and any required parameters.

3. **Execution**: The server applies authentication and authorization checks using OAuth 2.0 and least-privilege scopes, ensuring the client is permitted to execute the requested action. The server then performs the requested operation.

4. **Response**: Results are returned in a standardized JSON-RPC response. If an error occurs, the response includes a structured error object. The client relays the results to the agent, which incorporates them into its reasoning.

5. **Iteration**: Based on the results, the agent might issue additional MCP requests, chaining tool calls or resource queries to achieve higher-level goals. This iterative process allows the agent to refine its reasoning and dynamically adapt to changing conditions or new data.

6. **Observability & Logging** (Optional): Hosts or clients might log requests, responses, and execution traces to support debugging, auditing, or performance monitoring.

In the following example, an agent is connected to a support team's ticketing system. The MCP server exposes a tool called `searchTickets`, which lets agents query tickets by status, assignee, or other fields.

Suppose a support agent makes the following query to an AI agent:

Show me all my open tickets.

The LLM then processes this request and makes the following MCP call:

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "searchTickets",
  "params": {
    "status": "open",
    "assignee": "me"
  }
}
```

* `method`: The MCP tool being called (`searchTickets`)

* `params`: The query parameters for filtering tickets

The MCP server returns a structured list of open tickets:

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": [
    {
      "ticketId": "123",
      "title": "Login issue",
      "priority": "high"
    },
    {
      "ticketId": "124",
      "title": "Billing discrepancy",
      "priority": "medium"
    }
  ]
}
```

The agent acting as the MCP client can now summarize tickets for the user, suggest next steps, or chain further requests by calling other MCP tools.

## Security challenges

While MCP streamlines tool integration, it also introduces new identity and security challenges. Each MCP server must enforce strong authentication and authorization to ensure only trusted clients can access tools and resources.

Common security challenges include:

* Configuring OAuth 2.0 correctly to avoid reliance on static secrets

* Implementing least-privilege scopes so agents can only access the data they need

* Securing multi-tenant MCP servers with fine-grained access control to prevent data leakage across users

* Protecting against denial-of-service with unbounded tool calls, and mitigating risks from prompt injection that could trigger malicious tool execution

Learn more about MCP security best practices in [Securing MCP servers with OAuth 2.0](../identity/idai-securing-mcp-servers-oauth.html).