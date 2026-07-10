---
title: Client Authentication Methods
description: This comprehensive collection demonstrates all major OAuth 2.0 and OpenID Connect client authentication methods supported by PingOne. This is an educational resource for understanding when and how to use each authentication approach.
component: pingone-api
page_id: pingone-api:workflow-library:platform-sso-and-authorization/openid-connect-oidc/client-authentication-methods
canonical_url: https://developer.pingidentity.com/pingone-api/workflow-library/platform-sso-and-authorization/openid-connect-oidc/client-authentication-methods.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  authentication-methods-comparison: Authentication methods comparison
  when-to-use-each-method: When to use each method
---

# Client Authentication Methods

This comprehensive collection demonstrates all major OAuth 2.0 and OpenID Connect client authentication methods supported by PingOne. This is an educational resource for understanding when and how to use each authentication approach.

## Authentication methods comparison

| Method                | Security Level | Use Case                                       | Client Type  | Notes                                                                           |
| --------------------- | -------------- | ---------------------------------------------- | ------------ | ------------------------------------------------------------------------------- |
| `CLIENT_SECRET_BASIC` | Medium         | Traditional server-side apps                   | Confidential | * Standard HTTP Basic Authentication

* Secret in `Authorization` header        |
| `CLIENT_SECRET_POST`  | Medium         | Server-side apps, legacy systems               | Confidential | - Client credentials sent in POST body

- Easier to process for some frameworks |
| `CLIENT_SECRET_JWT`   | High           | Modern server apps requiring enhanced security | Confidential | * JWT signed with client secret

* Provides non-repudiation                     |
| `PRIVATE_KEY_JWT`     | Very High      | Enterprise apps with PKI infrastructure        | Confidential | - JWT signed with private key

- Highest security, no shared secrets            |
| `NONE`                | Low            | Public clients (SPAs, mobile apps)             | Public       | * No authentication

* Must use PKCE for security                               |

## When to use each method

**CLIENT\_SECRET\_BASIC** (Most Common)

* Best for: Traditional web applications, backend services

* Pros: Industry standard, widely supported, simple to implement

* Cons: Credentials in header (base64 encoded, not encrypted)

* Example: Node.js backend, Java Spring applications

**CLIENT\_SECRET\_POST**

* Best for: Applications where header manipulation is difficult

* Pros: Easier for some frameworks, credentials in body

* Cons: Less standard than Basic auth

* Example: Legacy systems, certain API gateways

**CLIENT\_SECRET\_JWT**

* Best For: Applications requiring enhanced security and audit trails

* Pros: Non-repudiation, tamperproof, includes expiration

* Cons: More complex implementation, requires JWT library

* Example: Financial applications, healthcare systems

**PRIVATE\_KEY\_JWT**

* Best for: Enterprise applications with PKI infrastructure

* Pros: Highest security, no shared secrets, certificate-based

* Cons: Complex setup, certificate management overhead

* Example: Banking applications, government systems

**NONE** (Public Clients)

* Best for: Single page applications (SPAs), mobile apps, native apps

* Pros: No secret management needed

* Cons: Must use PKCE, limited to certain grant types

* Example: React/Angular SPAs, iOS/Android apps

[Run in Postman](https://god.gw.postman.com/run-collection/18568624-4e4e5063-6ad7-4895-805e-ada77358488c?action=collection%2Ffork\&source=rip_markdown\&collection-url=entityId%3D18568624-4e4e5063-6ad7-4895-805e-ada77358488c%26entityType%3Dcollection%26workspaceId%3D3550b170-7818-4801-b1eb-dcb7b3f64263#?env%5BPingOne%20Workflow%20Library%20Template%20%28release%3A%202025-04-17%29%5D=W3sia2V5IjoidGxkIiwidmFsdWUiOiJjb20iLCJlbmFibGVkIjp0cnVlLCJ0eXBlIjoiZGVmYXVsdCJ9LHsia2V5IjoiYXV0aFBhdGgiLCJ2YWx1ZSI6Imh0dHBzOi8vYXV0aC5waW5nb25lLnt7dGxkfX0iLCJlbmFibGVkIjp0cnVlLCJ0eXBlIjoiZGVmYXVsdCJ9LHsia2V5IjoiYXBpUGF0aCIsInZhbHVlIjoiaHR0cHM6Ly9hcGkucGluZ29uZS57e3RsZH19L3YxIiwiZW5hYmxlZCI6dHJ1ZSwidHlwZSI6ImRlZmF1bHQifSx7ImtleSI6ImFkbWluRW52SUQiLCJ2YWx1ZSI6IiIsImVuYWJsZWQiOnRydWUsInR5cGUiOiJkZWZhdWx0In0seyJrZXkiOiJhZG1pbkFwcElEIiwidmFsdWUiOiIiLCJlbmFibGVkIjp0cnVlLCJ0eXBlIjoiZGVmYXVsdCJ9LHsia2V5IjoiYWRtaW5BcHBTZWNyZXQiLCJ2YWx1ZSI6IiIsImVuYWJsZWQiOnRydWUsInR5cGUiOiJkZWZhdWx0In0seyJrZXkiOiJlbnZJRCIsInZhbHVlIjoiIiwiZW5hYmxlZCI6dHJ1ZSwidHlwZSI6ImRlZmF1bHQifV0=)

---

---
title: CLIENT_SECRET_BASIC Flow
description: "For applications that have the tokenEndpointAuthMethod property set to CLIENT_SECRET_BASIC, you authenticate the token endpoint by setting the Authorization: Basic HTTP header in the request URL. The value is a Base64-encoded representation of \"username:password\", in which the username is the client_id and the password is the client_secret."
component: pingone-api
page_id: pingone-api:workflow-library:platform-sso-and-authorization/openid-connect-oidc/client-authentication-methods/test-the-workflow/client-secret-basic
canonical_url: https://developer.pingidentity.com/pingone-api/workflow-library/platform-sso-and-authorization/openid-connect-oidc/client-authentication-methods/test-the-workflow/client-secret-basic.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  what-youll-do: What you'll do
---

# CLIENT\_SECRET\_BASIC Flow

For applications that have the `tokenEndpointAuthMethod` property set to `CLIENT_SECRET_BASIC`, you authenticate the token endpoint by setting the `Authorization: Basic` HTTP header in the request URL. The value is a Base64-encoded representation of "username:password", in which the `username` is the `client_id` and the password is the `client_secret`.

## What you'll do

You will send an authorization request to start the workflow.

* POST request to the authorize endpoint.

* POST request to submit the user's username and password.

* POST request to get the access token.

[Run in Postman](https://god.gw.postman.com/run-collection/3468883-9f96a27d-8425-4b45-bbd2-13452eea2a40?action=collection%2Ffork\&source=rip_markdown\&collection-url=entityId%3D3468883-9f96a27d-8425-4b45-bbd2-13452eea2a40%26entityType%3Dcollection%26workspaceId%3D3550b170-7818-4801-b1eb-dcb7b3f64263#?env%5BPingOne%20Workflow%20Library%20Template%20%28release%3A%202025-04-17%29%5D=W3sia2V5IjoidGxkIiwidmFsdWUiOiJjb20iLCJlbmFibGVkIjp0cnVlLCJ0eXBlIjoiZGVmYXVsdCJ9LHsia2V5IjoiYXV0aFBhdGgiLCJ2YWx1ZSI6Imh0dHBzOi8vYXV0aC5waW5nb25lLnt7dGxkfX0iLCJlbmFibGVkIjp0cnVlLCJ0eXBlIjoiZGVmYXVsdCJ9LHsia2V5IjoiYXBpUGF0aCIsInZhbHVlIjoiaHR0cHM6Ly9hcGkucGluZ29uZS57e3RsZH19L3YxIiwiZW5hYmxlZCI6dHJ1ZSwidHlwZSI6ImRlZmF1bHQifSx7ImtleSI6ImFkbWluRW52SUQiLCJ2YWx1ZSI6IiIsImVuYWJsZWQiOnRydWUsInR5cGUiOiJkZWZhdWx0In0seyJrZXkiOiJhZG1pbkFwcElEIiwidmFsdWUiOiIiLCJlbmFibGVkIjp0cnVlLCJ0eXBlIjoiZGVmYXVsdCJ9LHsia2V5IjoiYWRtaW5BcHBTZWNyZXQiLCJ2YWx1ZSI6IiIsImVuYWJsZWQiOnRydWUsInR5cGUiOiJkZWZhdWx0In0seyJrZXkiOiJlbnZJRCIsInZhbHVlIjoiIiwiZW5hYmxlZCI6dHJ1ZSwidHlwZSI6ImRlZmF1bHQifV0=)

---

---
title: CLIENT_SECRET_BASIC Setup
description: "Authentication requirements for the token endpoint are set by the application's tokenEndpointAuthMethod property. When the application's tokenEndpointAuthMethod is set to CLIENT_SECRET_BASIC, the Authorization: Basic header represents a Base64-encoded representation of \"username:password\", in which the username is the client_id and the password is the client_secret:"
component: pingone-api
page_id: pingone-api:workflow-library:platform-sso-and-authorization/openid-connect-oidc/client-authentication-methods/environment-configuration/client-secret-basic
canonical_url: https://developer.pingidentity.com/pingone-api/workflow-library/platform-sso-and-authorization/openid-connect-oidc/client-authentication-methods/environment-configuration/client-secret-basic.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
---

# CLIENT\_SECRET\_BASIC Setup

Authentication requirements for the token endpoint are set by the application's `tokenEndpointAuthMethod` property. When the application's `tokenEndpointAuthMethod` is set to `CLIENT_SECRET_BASIC`, the `Authorization: Basic` header represents a Base64-encoded representation of "username:password", in which the username is the `client_id` and the password is the `client_secret`:

```bash
  -H 'Authorization: Basic <client_id:client_secret>' \
```

**Key points**

* Standard HTTP Basic Auth (RFC 7617)

* Credentials: `Authorization: Basic base64(clientId:clientSecret)`

* Widely supported across all platforms

* Default method for most OAuth implementations

The following workflow shows the application configuration to complete a sign-on flow using the `CLIENT_SECRET_BASIC` client authentication method. [Run in Postman](https://god.gw.postman.com/run-collection/3468883-18657ecf-491a-4b99-83b7-5ba7ca742528?action=collection%2Ffork\&source=rip_markdown\&collection-url=entityId%3D3468883-18657ecf-491a-4b99-83b7-5ba7ca742528%26entityType%3Dcollection%26workspaceId%3D3550b170-7818-4801-b1eb-dcb7b3f64263#?env%5BPingOne%20Workflow%20Library%20Template%20%28release%3A%202025-04-17%29%5D=W3sia2V5IjoidGxkIiwidmFsdWUiOiJjb20iLCJlbmFibGVkIjp0cnVlLCJ0eXBlIjoiZGVmYXVsdCJ9LHsia2V5IjoiYXV0aFBhdGgiLCJ2YWx1ZSI6Imh0dHBzOi8vYXV0aC5waW5nb25lLnt7dGxkfX0iLCJlbmFibGVkIjp0cnVlLCJ0eXBlIjoiZGVmYXVsdCJ9LHsia2V5IjoiYXBpUGF0aCIsInZhbHVlIjoiaHR0cHM6Ly9hcGkucGluZ29uZS57e3RsZH19L3YxIiwiZW5hYmxlZCI6dHJ1ZSwidHlwZSI6ImRlZmF1bHQifSx7ImtleSI6ImFkbWluRW52SUQiLCJ2YWx1ZSI6IiIsImVuYWJsZWQiOnRydWUsInR5cGUiOiJkZWZhdWx0In0seyJrZXkiOiJhZG1pbkFwcElEIiwidmFsdWUiOiIiLCJlbmFibGVkIjp0cnVlLCJ0eXBlIjoiZGVmYXVsdCJ9LHsia2V5IjoiYWRtaW5BcHBTZWNyZXQiLCJ2YWx1ZSI6IiIsImVuYWJsZWQiOnRydWUsInR5cGUiOiJkZWZhdWx0In0seyJrZXkiOiJlbnZJRCIsInZhbHVlIjoiIiwiZW5hYmxlZCI6dHJ1ZSwidHlwZSI6ImRlZmF1bHQifV0=)

---

---
title: CLIENT_SECRET_JWT Flow
description: For applications that have the tokenEndpointAuthMethod property set to CLIENT_SECRET_JWT, you authenticate the token endpoint using a JWT signed by the application's client secret to authenticate the request.
component: pingone-api
page_id: pingone-api:workflow-library:platform-sso-and-authorization/openid-connect-oidc/client-authentication-methods/test-the-workflow/client-secret-jwt
canonical_url: https://developer.pingidentity.com/pingone-api/workflow-library/platform-sso-and-authorization/openid-connect-oidc/client-authentication-methods/test-the-workflow/client-secret-jwt.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  what-youll-do: What you'll do
---

# CLIENT\_SECRET\_JWT Flow

For applications that have the `tokenEndpointAuthMethod` property set to `CLIENT_SECRET_JWT`, you authenticate the token endpoint using a JWT signed by the application's client secret to authenticate the request.

## What you'll do

You will send an authorization request to start the workflow.

* POST request to the authorize endpoint.

* POST request to submit the user's username and password.

* POST request to get the access token.

[Run in Postman](https://god.gw.postman.com/run-collection/3468883-9aa35e8d-8692-4b77-861f-9527da68b845?action=collection%2Ffork\&source=rip_markdown\&collection-url=entityId%3D3468883-9aa35e8d-8692-4b77-861f-9527da68b845%26entityType%3Dcollection%26workspaceId%3D3550b170-7818-4801-b1eb-dcb7b3f64263#?env%5BPingOne%20Workflow%20Library%20Template%20%28release%3A%202025-04-17%29%5D=W3sia2V5IjoidGxkIiwidmFsdWUiOiJjb20iLCJlbmFibGVkIjp0cnVlLCJ0eXBlIjoiZGVmYXVsdCJ9LHsia2V5IjoiYXV0aFBhdGgiLCJ2YWx1ZSI6Imh0dHBzOi8vYXV0aC5waW5nb25lLnt7dGxkfX0iLCJlbmFibGVkIjp0cnVlLCJ0eXBlIjoiZGVmYXVsdCJ9LHsia2V5IjoiYXBpUGF0aCIsInZhbHVlIjoiaHR0cHM6Ly9hcGkucGluZ29uZS57e3RsZH19L3YxIiwiZW5hYmxlZCI6dHJ1ZSwidHlwZSI6ImRlZmF1bHQifSx7ImtleSI6ImFkbWluRW52SUQiLCJ2YWx1ZSI6IiIsImVuYWJsZWQiOnRydWUsInR5cGUiOiJkZWZhdWx0In0seyJrZXkiOiJhZG1pbkFwcElEIiwidmFsdWUiOiIiLCJlbmFibGVkIjp0cnVlLCJ0eXBlIjoiZGVmYXVsdCJ9LHsia2V5IjoiYWRtaW5BcHBTZWNyZXQiLCJ2YWx1ZSI6IiIsImVuYWJsZWQiOnRydWUsInR5cGUiOiJkZWZhdWx0In0seyJrZXkiOiJlbnZJRCIsInZhbHVlIjoiIiwiZW5hYmxlZCI6dHJ1ZSwidHlwZSI6ImRlZmF1bHQifV0=)

---

---
title: CLIENT_SECRET_JWT Setup
description: Authentication requirements for the token endpoint are set by the application's tokenEndpointAuthMethod property. When the application's tokenEndpointAuthMethod is set to CLIENT_SECRET_JWT, the token endpoint uses a JWT signed by the application's client secret to authenticate the request. For information about creating the JWT and the claims in the JWT, refer to Create a client secret JWT. Token requests that use this authentication method require the client_assertion and client_assertion_type OAuth properties to specify the JWT.
component: pingone-api
page_id: pingone-api:workflow-library:platform-sso-and-authorization/openid-connect-oidc/client-authentication-methods/environment-configuration/client-secret-jwt
canonical_url: https://developer.pingidentity.com/pingone-api/workflow-library/platform-sso-and-authorization/openid-connect-oidc/client-authentication-methods/environment-configuration/client-secret-jwt.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
---

# CLIENT\_SECRET\_JWT Setup

Authentication requirements for the token endpoint are set by the application's `tokenEndpointAuthMethod` property. When the application's `tokenEndpointAuthMethod` is set to `CLIENT_SECRET_JWT`, the token endpoint uses a JWT signed by the application's client secret to authenticate the request. For information about creating the JWT and the claims in the JWT, refer to [Create a client secret JWT](../../../../../auth/auth-config-options/create-a-client-secret-jwt.html). Token requests that use this authentication method require the `client_assertion` and `client_assertion_type` OAuth properties to specify the JWT.

**Key points**

* JWT signed with `HMAC-SHA256` using client secret

* Includes claims: `iss`, `sub` (both identify the `client_id`), `aud` (token endpoint), `exp`

* Provides non-repudiation and tamper detection

* Better for audit trails and compliance requirements

The following workflow shows the application configuration to complete a sign-on flow using the `CLIENT_SECRET_JWT` client authentication method. [Run in Postman](https://god.gw.postman.com/run-collection/3468883-d63f8c64-00d1-4103-958d-a038aadf543c?action=collection%2Ffork\&source=rip_markdown\&collection-url=entityId%3D3468883-d63f8c64-00d1-4103-958d-a038aadf543c%26entityType%3Dcollection%26workspaceId%3D3550b170-7818-4801-b1eb-dcb7b3f64263#?env%5BPingOne%20Workflow%20Library%20Template%20%28release%3A%202025-04-17%29%5D=W3sia2V5IjoidGxkIiwidmFsdWUiOiJjb20iLCJlbmFibGVkIjp0cnVlLCJ0eXBlIjoiZGVmYXVsdCJ9LHsia2V5IjoiYXV0aFBhdGgiLCJ2YWx1ZSI6Imh0dHBzOi8vYXV0aC5waW5nb25lLnt7dGxkfX0iLCJlbmFibGVkIjp0cnVlLCJ0eXBlIjoiZGVmYXVsdCJ9LHsia2V5IjoiYXBpUGF0aCIsInZhbHVlIjoiaHR0cHM6Ly9hcGkucGluZ29uZS57e3RsZH19L3YxIiwiZW5hYmxlZCI6dHJ1ZSwidHlwZSI6ImRlZmF1bHQifSx7ImtleSI6ImFkbWluRW52SUQiLCJ2YWx1ZSI6IiIsImVuYWJsZWQiOnRydWUsInR5cGUiOiJkZWZhdWx0In0seyJrZXkiOiJhZG1pbkFwcElEIiwidmFsdWUiOiIiLCJlbmFibGVkIjp0cnVlLCJ0eXBlIjoiZGVmYXVsdCJ9LHsia2V5IjoiYWRtaW5BcHBTZWNyZXQiLCJ2YWx1ZSI6IiIsImVuYWJsZWQiOnRydWUsInR5cGUiOiJkZWZhdWx0In0seyJrZXkiOiJlbnZJRCIsInZhbHVlIjoiIiwiZW5hYmxlZCI6dHJ1ZSwidHlwZSI6ImRlZmF1bHQifV0=)

---

---
title: CLIENT_SECRET_POST Flow
description: For applications that have the tokenEndpointAuthMethod property set to CLIENT_SECRET_POST, you authenticate the token endpoint by setting the application's client_id and client_secret as properties in the request body.
component: pingone-api
page_id: pingone-api:workflow-library:platform-sso-and-authorization/openid-connect-oidc/client-authentication-methods/test-the-workflow/client-secret-post
canonical_url: https://developer.pingidentity.com/pingone-api/workflow-library/platform-sso-and-authorization/openid-connect-oidc/client-authentication-methods/test-the-workflow/client-secret-post.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  what-youll-do: What you'll do
---

# CLIENT\_SECRET\_POST Flow

For applications that have the `tokenEndpointAuthMethod` property set to `CLIENT_SECRET_POST`, you authenticate the token endpoint by setting the application's `client_id` and `client_secret` as properties in the request body.

## What you'll do

You will send an authorization request to start the workflow.

* POST request to the authorize endpoint.

* POST request to submit the user's username and password.

* POST request to get the access token.

[Run in Postman](https://god.gw.postman.com/run-collection/3468883-0f1c8aea-9946-461a-8908-5360cf66f9f5?action=collection%2Ffork\&source=rip_markdown\&collection-url=entityId%3D3468883-0f1c8aea-9946-461a-8908-5360cf66f9f5%26entityType%3Dcollection%26workspaceId%3D3550b170-7818-4801-b1eb-dcb7b3f64263#?env%5BPingOne%20Workflow%20Library%20Template%20%28release%3A%202025-04-17%29%5D=W3sia2V5IjoidGxkIiwidmFsdWUiOiJjb20iLCJlbmFibGVkIjp0cnVlLCJ0eXBlIjoiZGVmYXVsdCJ9LHsia2V5IjoiYXV0aFBhdGgiLCJ2YWx1ZSI6Imh0dHBzOi8vYXV0aC5waW5nb25lLnt7dGxkfX0iLCJlbmFibGVkIjp0cnVlLCJ0eXBlIjoiZGVmYXVsdCJ9LHsia2V5IjoiYXBpUGF0aCIsInZhbHVlIjoiaHR0cHM6Ly9hcGkucGluZ29uZS57e3RsZH19L3YxIiwiZW5hYmxlZCI6dHJ1ZSwidHlwZSI6ImRlZmF1bHQifSx7ImtleSI6ImFkbWluRW52SUQiLCJ2YWx1ZSI6IiIsImVuYWJsZWQiOnRydWUsInR5cGUiOiJkZWZhdWx0In0seyJrZXkiOiJhZG1pbkFwcElEIiwidmFsdWUiOiIiLCJlbmFibGVkIjp0cnVlLCJ0eXBlIjoiZGVmYXVsdCJ9LHsia2V5IjoiYWRtaW5BcHBTZWNyZXQiLCJ2YWx1ZSI6IiIsImVuYWJsZWQiOnRydWUsInR5cGUiOiJkZWZhdWx0In0seyJrZXkiOiJlbnZJRCIsInZhbHVlIjoiIiwiZW5hYmxlZCI6dHJ1ZSwidHlwZSI6ImRlZmF1bHQifV0=)

---

---
title: CLIENT_SECRET_POST Setup
description: Authentication requirements for the token endpoint are set by the application's tokenEndpointAuthMethod property. When the application's tokenEndpointAuthMethod is set to CLIENT_SECRET_POST, the request does not need an Authorization header, and the client_id and client_secret property values are submitted in the request body.
component: pingone-api
page_id: pingone-api:workflow-library:platform-sso-and-authorization/openid-connect-oidc/client-authentication-methods/environment-configuration/client-secret-post
canonical_url: https://developer.pingidentity.com/pingone-api/workflow-library/platform-sso-and-authorization/openid-connect-oidc/client-authentication-methods/environment-configuration/client-secret-post.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
---

# CLIENT\_SECRET\_POST Setup

Authentication requirements for the token endpoint are set by the application's `tokenEndpointAuthMethod` property. When the application's `tokenEndpointAuthMethod` is set to `CLIENT_SECRET_POST`, the request does not need an `Authorization` header, and the `client_id` and `client_secret` property values are submitted in the request body.

**Key points**

* Credentials in POST body: `client_id` and `client_secret` parameters

* No Authorization header needed

* Easier for frameworks that don't handle headers well

* Still requires secure transport (HTTPS)

The following workflow shows the application configuration to complete a sign-on flow using the `CLIENT_SECRET_POST` client authentication method. [Run in Postman](https://god.gw.postman.com/run-collection/3468883-57b56a3e-5ffc-4102-9530-d3043b3382ef?action=collection%2Ffork\&source=rip_markdown\&collection-url=entityId%3D3468883-57b56a3e-5ffc-4102-9530-d3043b3382ef%26entityType%3Dcollection%26workspaceId%3D3550b170-7818-4801-b1eb-dcb7b3f64263#?env%5BPingOne%20Workflow%20Library%20Template%20%28release%3A%202025-04-17%29%5D=W3sia2V5IjoidGxkIiwidmFsdWUiOiJjb20iLCJlbmFibGVkIjp0cnVlLCJ0eXBlIjoiZGVmYXVsdCJ9LHsia2V5IjoiYXV0aFBhdGgiLCJ2YWx1ZSI6Imh0dHBzOi8vYXV0aC5waW5nb25lLnt7dGxkfX0iLCJlbmFibGVkIjp0cnVlLCJ0eXBlIjoiZGVmYXVsdCJ9LHsia2V5IjoiYXBpUGF0aCIsInZhbHVlIjoiaHR0cHM6Ly9hcGkucGluZ29uZS57e3RsZH19L3YxIiwiZW5hYmxlZCI6dHJ1ZSwidHlwZSI6ImRlZmF1bHQifSx7ImtleSI6ImFkbWluRW52SUQiLCJ2YWx1ZSI6IiIsImVuYWJsZWQiOnRydWUsInR5cGUiOiJkZWZhdWx0In0seyJrZXkiOiJhZG1pbkFwcElEIiwidmFsdWUiOiIiLCJlbmFibGVkIjp0cnVlLCJ0eXBlIjoiZGVmYXVsdCJ9LHsia2V5IjoiYWRtaW5BcHBTZWNyZXQiLCJ2YWx1ZSI6IiIsImVuYWJsZWQiOnRydWUsInR5cGUiOiJkZWZhdWx0In0seyJrZXkiOiJlbnZJRCIsInZhbHVlIjoiIiwiZW5hYmxlZCI6dHJ1ZSwidHlwZSI6ImRlZmF1bHQifV0=)

---

---
title: Create a Group and Add a User
description: This activity shows you how to create a group and assign a user to that group. By default, groups are created at the environment level. Groups can also be created per population. This workflow creates an environment-level group and then calls the /users/{{userID}}/memberOfGroups endpoint to associate the specified user with the group.
component: pingone-api
page_id: pingone-api:workflow-library:platform-sso-and-authorization/groups/create-a-group-and-add-a-user
canonical_url: https://developer.pingidentity.com/pingone-api/workflow-library/platform-sso-and-authorization/groups/create-a-group-and-add-a-user.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  prerequisites: Prerequisites
---

# Create a Group and Add a User

This activity shows you how to create a group and assign a user to that group. By default, groups are created at the environment level. Groups can also be created per population. This workflow creates an environment-level group and then calls the `/users/{{userID}}/memberOfGroups` endpoint to associate the specified user with the group.

## Prerequisites

Get an access token from the worker application that you created in [Create an admin Worker app connection](../../../getting-started/create-an-admin-worker-app.html). To get a token from a different worker application in an alternate sandbox environment, run the token request endpoint using the client ID and client secret of your chosen worker app to authenticate the request. For more information, refer to [Get a PingOne admin access token](../../../getting-started/create-a-test-environment/step-1-get-access-token.html).

Click the **Run in Postman** button below to fork, or download and import, the Postman collection for this workflow to your workspace.

[Run in Postman](https://god.gw.postman.com/run-collection/18568624-e8c1ce22-1a4e-4328-a3b1-e43146b5b932?action=collection%2Ffork\&source=rip_markdown\&collection-url=entityId%3D18568624-e8c1ce22-1a4e-4328-a3b1-e43146b5b932%26entityType%3Dcollection%26workspaceId%3D3550b170-7818-4801-b1eb-dcb7b3f64263#?env%5BPingOne%20Workflow%20Library%20Template%20%28release%3A%202025-04-17%29%5D=W3sia2V5IjoidGxkIiwidmFsdWUiOiJjb20iLCJlbmFibGVkIjp0cnVlLCJ0eXBlIjoiZGVmYXVsdCJ9LHsia2V5IjoiYXV0aFBhdGgiLCJ2YWx1ZSI6Imh0dHBzOi8vYXV0aC5waW5nb25lLnt7dGxkfX0iLCJlbmFibGVkIjp0cnVlLCJ0eXBlIjoiZGVmYXVsdCJ9LHsia2V5IjoiYXBpUGF0aCIsInZhbHVlIjoiaHR0cHM6Ly9hcGkucGluZ29uZS57e3RsZH19L3YxIiwiZW5hYmxlZCI6dHJ1ZSwidHlwZSI6ImRlZmF1bHQifSx7ImtleSI6ImFkbWluRW52SUQiLCJ2YWx1ZSI6IiIsImVuYWJsZWQiOnRydWUsInR5cGUiOiJkZWZhdWx0In0seyJrZXkiOiJhZG1pbkFwcElEIiwidmFsdWUiOiIiLCJlbmFibGVkIjp0cnVlLCJ0eXBlIjoiZGVmYXVsdCJ9LHsia2V5IjoiYWRtaW5BcHBTZWNyZXQiLCJ2YWx1ZSI6IiIsImVuYWJsZWQiOnRydWUsInR5cGUiOiJkZWZhdWx0In0seyJrZXkiOiJlbnZJRCIsInZhbHVlIjoiIiwiZW5hYmxlZCI6dHJ1ZSwidHlwZSI6ImRlZmF1bHQifV0=)

---

---
title: Create a Risk Evaluation
description: This activity shows you how to create a new risk evaluation. This scenario illustrates the following common operations supported by the PingOne APIs:
component: pingone-api
page_id: pingone-api:workflow-library:pingone-protect/create-a-risk-evaluation
canonical_url: https://developer.pingidentity.com/pingone-api/workflow-library/pingone-protect/create-a-risk-evaluation.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  prerequisites: Prerequisites
  what-youll-do: What you'll do
  defining-the-risk-evaluation-resource: Defining the risk evaluation resource
---

# Create a Risk Evaluation

This activity shows you how to create a new risk evaluation. This scenario illustrates the following common operations supported by the PingOne APIs:

* Get a list of risk policy set resources

* Create a risk evaluation resource that uses a specific risk policy set

## Prerequisites

Get an access token from the worker application that you created in [Create an admin Worker app connection](../../getting-started/create-an-admin-worker-app.html). To get a token from a different worker application in an alternate sandbox environment, run the token request endpoint using the client ID and client secret of your chosen worker app to authenticate the request. For more information, refer to [Get a PingOne admin access token](../../getting-started/create-a-test-environment/step-1-get-access-token.html).

## What you'll do

To create the new risk evaluation, the following tasks must be completed successfully:

* GET request to return the list of risk policy set resources associated with the environment.

* POST request to create a new risk evaluation resource that references a risk policy set resource.

Click the **Run in Postman** button below to fork, or download and import, the Postman collection for this workflow to your workspace.

## Defining the risk evaluation resource

For the `POST` request to `/v1/environments/{{envID}}/riskEvaluations`, the risk evaluation resource definition lets you specify the risk policy set to apply to the evaluation. If a particular risk policy set is not specified, the risk evaluation uses the environment's default risk policy set to determine the risk levels for the event. In this use case, the risk evaluation sets the `riskPolicySet.id` property to the `{{riskPolicySetID}}` Postman variable, which should contain the ID of the risk policy set that you created in the [Create a risk policy set](create-a-risk-policy-set.html) activity.

The risk evaluation definition must include an `event` object that specifies details about the authentication action to evaluate against the risk policies defined in the risk policy set. In its most basic form, the event object defines a user (`user.id` and `user.type`) and an IP address (`ip`). From this information, the risk evaluation can provide a meaningful risk response for all supported risk predictors (`anonymousNetwork`, `ipRisk`, `geoVelocity`, `userRiskBehavior`) except the user risk behavior predictor, which requires the `targetResource` and `UserAgent` properties. For more information about the risk evaluation event data model, refer to [Risk Evaluations](../../protect/risk-evaluations.html) in the PingOne API Reference.

The risk evaluation process follows these steps:

1. The risk service receives an event that it is configured to monitor and evaluate.

2. A risk calculation is made for the event based on the configured risk policies.

3. The risk service returns the risk result to the client.

Click the **Run in Postman** button below to fork, or download and import, the Postman collection for this workflow to your workspace.

[Run in Postman](https://god.gw.postman.com/run-collection/18568624-2fb495d2-2a93-4768-bb4f-35b7010853f6?action=collection%2Ffork\&source=rip_markdown\&collection-url=entityId%3D18568624-2fb495d2-2a93-4768-bb4f-35b7010853f6%26entityType%3Dcollection%26workspaceId%3D3550b170-7818-4801-b1eb-dcb7b3f64263#?env%5BPingOne%20Workflow%20Library%20Template%20%28release%3A%202025-04-17%29%5D=W3sia2V5IjoidGxkIiwidmFsdWUiOiJjb20iLCJlbmFibGVkIjp0cnVlLCJ0eXBlIjoiZGVmYXVsdCJ9LHsia2V5IjoiYXV0aFBhdGgiLCJ2YWx1ZSI6Imh0dHBzOi8vYXV0aC5waW5nb25lLnt7dGxkfX0iLCJlbmFibGVkIjp0cnVlLCJ0eXBlIjoiZGVmYXVsdCJ9LHsia2V5IjoiYXBpUGF0aCIsInZhbHVlIjoiaHR0cHM6Ly9hcGkucGluZ29uZS57e3RsZH19L3YxIiwiZW5hYmxlZCI6dHJ1ZSwidHlwZSI6ImRlZmF1bHQifSx7ImtleSI6ImFkbWluRW52SUQiLCJ2YWx1ZSI6IiIsImVuYWJsZWQiOnRydWUsInR5cGUiOiJkZWZhdWx0In0seyJrZXkiOiJhZG1pbkFwcElEIiwidmFsdWUiOiIiLCJlbmFibGVkIjp0cnVlLCJ0eXBlIjoiZGVmYXVsdCJ9LHsia2V5IjoiYWRtaW5BcHBTZWNyZXQiLCJ2YWx1ZSI6IiIsImVuYWJsZWQiOnRydWUsInR5cGUiOiJkZWZhdWx0In0seyJrZXkiOiJlbnZJRCIsInZhbHVlIjoiIiwiZW5hYmxlZCI6dHJ1ZSwidHlwZSI6ImRlZmF1bHQifV0=)

---

---
title: Create a Risk Policy Set
description: This activity shows you how to create a new risk policy. This scenario illustrates the following common operations supported by the PingOne APIs:
component: pingone-api
page_id: pingone-api:workflow-library:pingone-protect/create-a-risk-policy-set
canonical_url: https://developer.pingidentity.com/pingone-api/workflow-library/pingone-protect/create-a-risk-policy-set.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  prerequisites: Prerequisites
  what-youll-do: What you'll do
  policy-set-logic: Policy set logic
---

# Create a Risk Policy Set

This activity shows you how to create a new risk policy. This scenario illustrates the following common operations supported by the PingOne APIs:

* Create a risk policy set by defining one or more risk policies

## Prerequisites

Get an access token from the worker application that you created in [Create an admin Worker app connection](../../getting-started/create-an-admin-worker-app.html). To get a token from a different worker application in an alternate sandbox environment, run the token request endpoint using the client ID and client secret of your chosen worker app to authenticate the request. For more information, refer to [Get a PingOne admin access token](../../getting-started/create-a-test-environment/step-1-get-access-token.html).

## What you'll do

To create the new risk policy set, the following tasks must be completed successfully:

* POST request to create a new risk policy set resource.

Click the **Run in Postman** button below to fork, or download and import, the Postman collection for this workflow to your workspace.

### Policy set logic

A risk policy set must have at least one defined risk policy, which includes the following components:

* **Condition.** The policy logic to define when the policy is evaluated to `true` and when it is evaluated to `false`.

* **Result.** The policy logic to define what should be returned in case the condition is evaluated to `true`.

* **Priority.** (Optional) A priority ranking to define the execution order of the different risk policies contained in the policy set.

For this use case, you will define a simple risk policy set that includes two risk policies: A whitelist that evaluates risk based on the user's IP address, and an anonymous network detection check.

The following JSON shows the elements defined in the whitelist risk policy. The `condition.contains` expression uses the `${transaction.ip}` condition variable to get the user's IP address and compare it to a range of IP addresses that are considered safe. If the user's IP address is within the range set in `condition.ipRange`, the condition evaluates to `true`, and the `result.level` is set to `LOW`, indicating low risk for this policy condition.

```none
	"riskPolicies": [
		{
			"name": "WHITELIST",
            "priority": 1,
			"result": {
				"level": "LOW"
			},
			"condition": {
				"contains": "${transaction.ip}",
				"ipRange": [
					"1.1.1.1/16",
					"2.2.2.2/24"
				]
			}
		}
    ]
[source]
```

The following JSON shows the elements defined in the anonymous network detection risk policy. The `condition.contains` expression uses the `${details.anonymousNetworkDetected}` condition variable to determine whether the user is attempting to authenticate from an anonymous network. If the `condition.value` evaluates to `true`, then the `result.level` is set to `HIGH`, indicating that this is a high-risk transaction.

```none
     ...
            "name": "ANONYMOUS_NETWORK_DETECTION",
            "priority": 2,
            "result": {
                "level": "HIGH",
                "type": "VALUE"
            },
            "condition": {
                "equals": true,
                "value": "${details.anonymousNetworkDetected}"
            },
```

For more information about risk policies, refer to [Risk Policies](../../protect/risk-policies.html).

Click the **Run in Postman** button below to fork, or download and import, the Postman collection for this workflow to your workspace.

[Run in Postman](https://god.gw.postman.com/run-collection/18568624-4bb35659-b63c-46f9-95e1-69f6d126aa00?action=collection%2Ffork\&source=rip_markdown\&collection-url=entityId%3D18568624-4bb35659-b63c-46f9-95e1-69f6d126aa00%26entityType%3Dcollection%26workspaceId%3D3550b170-7818-4801-b1eb-dcb7b3f64263#?env%5BPingOne%20Workflow%20Library%20Template%20%28release%3A%202025-04-17%29%5D=W3sia2V5IjoidGxkIiwidmFsdWUiOiJjb20iLCJlbmFibGVkIjp0cnVlLCJ0eXBlIjoiZGVmYXVsdCJ9LHsia2V5IjoiYXV0aFBhdGgiLCJ2YWx1ZSI6Imh0dHBzOi8vYXV0aC5waW5nb25lLnt7dGxkfX0iLCJlbmFibGVkIjp0cnVlLCJ0eXBlIjoiZGVmYXVsdCJ9LHsia2V5IjoiYXBpUGF0aCIsInZhbHVlIjoiaHR0cHM6Ly9hcGkucGluZ29uZS57e3RsZH19L3YxIiwiZW5hYmxlZCI6dHJ1ZSwidHlwZSI6ImRlZmF1bHQifSx7ImtleSI6ImFkbWluRW52SUQiLCJ2YWx1ZSI6IiIsImVuYWJsZWQiOnRydWUsInR5cGUiOiJkZWZhdWx0In0seyJrZXkiOiJhZG1pbkFwcElEIiwidmFsdWUiOiIiLCJlbmFibGVkIjp0cnVlLCJ0eXBlIjoiZGVmYXVsdCJ9LHsia2V5IjoiYWRtaW5BcHBTZWNyZXQiLCJ2YWx1ZSI6IiIsImVuYWJsZWQiOnRydWUsInR5cGUiOiJkZWZhdWx0In0seyJrZXkiOiJlbnZJRCIsInZhbHVlIjoiIiwiZW5hYmxlZCI6dHJ1ZSwidHlwZSI6ImRlZmF1bHQifV0=)

---

---
title: Create a Workday Propagation Connection
description: This use case shows you how to create a propagation connection between a Workday source identity store and your PingOne directory target identity store.
component: pingone-api
page_id: pingone-api:workflow-library:platform-sso-and-authorization/identity-propagation/create-a-workday-propagation-connection
canonical_url: https://developer.pingidentity.com/pingone-api/workflow-library/platform-sso-and-authorization/identity-propagation/create-a-workday-propagation-connection.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  prerequisites: Prerequisites
  workflow-order-of-operations: Workflow order of operations
---

# Create a Workday Propagation Connection

This use case shows you how to create a propagation connection between a Workday source identity store and your PingOne directory target identity store.

A Workday propagation connection is unique in requiring a writeback of information from the target, PingOne directory, to the source, Workday. Workday is demonstrated because of its unique writeback requirement. This use case guides you in successfully creating a Workday propagation connection.

This scenario illustrates the following common operations:

* Create a propagation plan.

* Create a propagation store.

* Create a writeback propagation store (applicable only to Workday).

* Create a propagation rule.

* Create a writeback propagation rule (applicable only to Workday).

* Create propagation rule mappings.

* Create writeback propagation rule mappings (applicable only to Workday).

* Create a new propagation revision.

## Prerequisites

Get an access token from the worker application that you created in [Create an admin Worker app connection](../../../getting-started/create-an-admin-worker-app.html). To get a token from a different worker application in an alternate sandbox environment, run the token request endpoint using the client ID and client secret of your chosen worker app to authenticate the request. For more information, refer to [Get a PingOne admin access token](../../../getting-started/create-a-test-environment/step-1-get-access-token.html).

## Workflow order of operations

To create a Workday inbound propagation connection, you will need to complete the following tasks:

1. Make a `POST` request to `/v1/environments/{{envID}}/passwordPolicies` to create a password policy for the population of users to synchronize with Workday.

2. Make a `POST` request to `/v1/environments/{{envID}}/populations` to create a population of users to synchronize with Workday.

3. Make a `POST` request to `/v1/environments/{{envID}}/propagation/plans` to create a Workday propagation plan.

4. Make a `POST` request to `/v1/environments/{{envID}}/propagation/stores` to create a Workday inbound source propagation store with a `type` of `Workday`.

5. Make a `POST` request to `/v1/environments/{{envID}}/propagation/stores` to create a Workday inbound target propagation store with a `type` of `PingOne`.

6. Make a `POST` request to `/v1/environments/{{envID}}/propagation/stores` to create a Workday writeback source propagation store of `type` directory (applicable only to Workday). No separate writeback target propagation store is required, the target is the Workday inbound source propagation store.

7. Make a `POST` request to `/v1/environments/{{envID}}/propagation/plans/{{planID}}/rules` to create a Workday propagation rule for mapping `Workday` attributes to `PingOne` attributes.

8. Make a `POST` request to `/v1/environments/{{envID}}/propagation/plans/{{planID}}/rules` to create a Workday propagation rule for mapping `directory` attributes to `Workday` attributes (applicable only to Workday).

9. Make a `POST` request to `/v1/environments/{{envID}}/propagation/rules/{{ruleID}}/mappings` to create a Workday inbound propagation rule mapping that associates a specific Workday attribute to a specific PingOne attribute.

10. Make a `POST` request to `/v1/environments/{{envID}}/propagation/plans/{{ruleID}}/rules` to create a Workday writeback propagation rule mapping that associates a specific `directory` attribute to a specific `Workday` attribute (applicable only to Workday).

11. Make a `GET` request to `/v1/environments/{{envID}}/propagation/rules/{{ruleID}}/mappings` to verify Workday inbound propagation rule mappings of attributes between `Workday` and `PingOne`.

12. Make a `GET` request to `/v1/environments/{{envID}}/propagation/rules/{{ruleID}}/mappings` to verify Workday writeback propagation rule mappings of attributes between `directory` and `Workday` (applicable only to Workday).

13. Make a `GET` request to `/v1/environments/{{envID}}/propagation/rules` to verify the Workday inbound propagation rule between `Workday` and `PingOne` and the Workday writeback propagation rule between `directory` and `Workday` (applicable only to Workday).

14. Make a `GET` request to `/v1/environments/{{envID}}/propagation/stores` to verify Workday propagation stores of types `Workday`, `PingOne`, and `directory`.

15. Make a `GET` request to `/v1/environments/{{envID}}/propagation/plans` to verify Workday propagation plans.

16. Make a `POST` request to `/v1/environments/{{envID}}/propagation/revisions` to create a new propagation revision to ensure all operations are reflected in the PingOne Admin Console.

Click the **Run in Postman** button below to fork, or download and import, the Postman collection for this workflow to your workspace.

[Run in Postman](https://god.gw.postman.com/run-collection/18568624-2d38766f-1c22-4eae-bf2c-509f4f71bd08?action=collection%2Ffork\&source=rip_markdown\&collection-url=entityId%3D18568624-2d38766f-1c22-4eae-bf2c-509f4f71bd08%26entityType%3Dcollection%26workspaceId%3D3550b170-7818-4801-b1eb-dcb7b3f64263#?env%5BPingOne%20Workflow%20Library%20Template%20%28release%3A%202025-04-17%29%5D=W3sia2V5IjoidGxkIiwidmFsdWUiOiJjb20iLCJlbmFibGVkIjp0cnVlLCJ0eXBlIjoiZGVmYXVsdCJ9LHsia2V5IjoiYXV0aFBhdGgiLCJ2YWx1ZSI6Imh0dHBzOi8vYXV0aC5waW5nb25lLnt7dGxkfX0iLCJlbmFibGVkIjp0cnVlLCJ0eXBlIjoiZGVmYXVsdCJ9LHsia2V5IjoiYXBpUGF0aCIsInZhbHVlIjoiaHR0cHM6Ly9hcGkucGluZ29uZS57e3RsZH19L3YxIiwiZW5hYmxlZCI6dHJ1ZSwidHlwZSI6ImRlZmF1bHQifSx7ImtleSI6ImFkbWluRW52SUQiLCJ2YWx1ZSI6IiIsImVuYWJsZWQiOnRydWUsInR5cGUiOiJkZWZhdWx0In0seyJrZXkiOiJhZG1pbkFwcElEIiwidmFsdWUiOiIiLCJlbmFibGVkIjp0cnVlLCJ0eXBlIjoiZGVmYXVsdCJ9LHsia2V5IjoiYWRtaW5BcHBTZWNyZXQiLCJ2YWx1ZSI6IiIsImVuYWJsZWQiOnRydWUsInR5cGUiOiJkZWZhdWx0In0seyJrZXkiOiJlbnZJRCIsInZhbHVlIjoiIiwiZW5hYmxlZCI6dHJ1ZSwidHlwZSI6ImRlZmF1bHQifV0=)

---

---
title: Create public client app (NONE auth)
component: pingone-api
page_id: pingone-api:workflow-library:platform-sso-and-authorization/openid-connect-oidc/client-authentication-methods/environment-configuration/none/step-1-create-a-native-application
canonical_url: https://developer.pingidentity.com/pingone-api/workflow-library/platform-sso-and-authorization/openid-connect-oidc/client-authentication-methods/environment-configuration/none/step-1-create-a-native-application.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  headers: Headers
  body: Body
  example-request: Example Request
  example-response: Example Response
---

# Create public client app (NONE auth)

##

 

```none
POST {{apiPath}}/v1/environments/{{envID}}/applications
```

This POST request creates a public client application with `NONE` authentication.

Public clients (SPAs, mobile apps, native apps) cannot securely store client secrets. Therefore, they use a `tokenEndpointAuthMethod` value of `NONE` and rely on PKCE (Proof Key for Code Exchange) for security.

The `POST {{apiPath}}/v1/environments/{{envID}}/applications` endpoint creates the new native application. To configure this application to use PKCE to authenticate the token request, set the application's `pkceEnforcement` property to `S256_REQUIRED`. With PKCE enforcement enabled, you must set the application's `tokenEndpointAuthMethod` property to `NONE`.

The response returns information about the new application, including its `id` property, which identifies the ID for this application resource. The application's ID is required to make the authorization request and to make the token request.

### Headers

Authorization      Bearer {{accessToken}}

Content-Type      application/json

### Body

raw ( application/json )

```json
{
    "enabled": true,
    "name": "Shared-Native-App",
    "description": "Public client application with NONE authentication - for SPAs and mobile apps that cannot securely store secrets. MUST use PKCE for security.",
    "type": "NATIVE_APP",
    "protocol": "OPENID_CONNECT",
    "grantTypes": [
        "AUTHORIZATION_CODE"
    ],
    "redirectUris": [
        "http://localhost:3000/callback"
    ],
    "responseTypes": [
        "CODE"
    ],
    "tokenEndpointAuthMethod": "NONE",
    "pkceEnforcement": "S256_REQUIRED"
}
```

##

### Example Request

* cURL

* C#

* Go

* HTTP

* Java

* jQuery

* NodeJS

* Python

* PHP

* Ruby

* Swift

```shell
curl --location --globoff '{{apiPath}}/v1/environments/{{envID}}/applications' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {{accessToken}}' \
--data '{
    "enabled": true,
    "name": "Shared-Native-App",
    "description": "Public client application with NONE authentication - for SPAs and mobile apps that cannot securely store secrets. MUST use PKCE for security.",
    "type": "NATIVE_APP",
    "protocol": "OPENID_CONNECT",
    "grantTypes": [
        "AUTHORIZATION_CODE"
    ],
    "redirectUris": [
        "http://localhost:3000/callback"
    ],
    "responseTypes": [
        "CODE"
    ],
    "tokenEndpointAuthMethod": "NONE",
    "pkceEnforcement": "S256_REQUIRED"
}'
```

```csharp
var options = new RestClientOptions("{{apiPath}}/v1/environments/{{envID}}/applications")
{
  MaxTimeout = -1,
};
var client = new RestClient(options);
var request = new RestRequest("", Method.Post);
request.AddHeader("Content-Type", "application/json");
request.AddHeader("Authorization", "Bearer {{accessToken}}");
var body = @"{" + "\n" +
@"    ""enabled"": true," + "\n" +
@"    ""name"": ""Shared-Native-App""," + "\n" +
@"    ""description"": ""Public client application with NONE authentication - for SPAs and mobile apps that cannot securely store secrets. MUST use PKCE for security.""," + "\n" +
@"    ""type"": ""NATIVE_APP""," + "\n" +
@"    ""protocol"": ""OPENID_CONNECT""," + "\n" +
@"    ""grantTypes"": [" + "\n" +
@"        ""AUTHORIZATION_CODE""" + "\n" +
@"    ]," + "\n" +
@"    ""redirectUris"": [" + "\n" +
@"        ""http://localhost:3000/callback""" + "\n" +
@"    ]," + "\n" +
@"    ""responseTypes"": [" + "\n" +
@"        ""CODE""" + "\n" +
@"    ]," + "\n" +
@"    ""tokenEndpointAuthMethod"": ""NONE""," + "\n" +
@"    ""pkceEnforcement"": ""S256_REQUIRED""" + "\n" +
@"}";
request.AddStringBody(body, DataFormat.Json);
RestResponse response = await client.ExecuteAsync(request);
Console.WriteLine(response.Content);
```

```golang
package main

import (
  "fmt"
  "strings"
  "net/http"
  "io"
)

func main() {

  url := "{{apiPath}}/v1/environments/{{envID}}/applications"
  method := "POST"

  payload := strings.NewReader(`{
    "enabled": true,
    "name": "Shared-Native-App",
    "description": "Public client application with NONE authentication - for SPAs and mobile apps that cannot securely store secrets. MUST use PKCE for security.",
    "type": "NATIVE_APP",
    "protocol": "OPENID_CONNECT",
    "grantTypes": [
        "AUTHORIZATION_CODE"
    ],
    "redirectUris": [
        "http://localhost:3000/callback"
    ],
    "responseTypes": [
        "CODE"
    ],
    "tokenEndpointAuthMethod": "NONE",
    "pkceEnforcement": "S256_REQUIRED"
}`)

  client := &http.Client {
  }
  req, err := http.NewRequest(method, url, payload)

  if err != nil {
    fmt.Println(err)
    return
  }
  req.Header.Add("Content-Type", "application/json")
  req.Header.Add("Authorization", "Bearer {{accessToken}}")

  res, err := client.Do(req)
  if err != nil {
    fmt.Println(err)
    return
  }
  defer res.Body.Close()

  body, err := io.ReadAll(res.Body)
  if err != nil {
    fmt.Println(err)
    return
  }
  fmt.Println(string(body))
}
```

```http
POST /v1/environments/{{envID}}/applications HTTP/1.1
Host: {{apiPath}}
Content-Type: application/json
Authorization: Bearer {{accessToken}}

{
    "enabled": true,
    "name": "Shared-Native-App",
    "description": "Public client application with NONE authentication - for SPAs and mobile apps that cannot securely store secrets. MUST use PKCE for security.",
    "type": "NATIVE_APP",
    "protocol": "OPENID_CONNECT",
    "grantTypes": [
        "AUTHORIZATION_CODE"
    ],
    "redirectUris": [
        "http://localhost:3000/callback"
    ],
    "responseTypes": [
        "CODE"
    ],
    "tokenEndpointAuthMethod": "NONE",
    "pkceEnforcement": "S256_REQUIRED"
}
```

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("application/json");
RequestBody body = RequestBody.create(mediaType, "{\n    \"enabled\": true,\n    \"name\": \"Shared-Native-App\",\n    \"description\": \"Public client application with NONE authentication - for SPAs and mobile apps that cannot securely store secrets. MUST use PKCE for security.\",\n    \"type\": \"NATIVE_APP\",\n    \"protocol\": \"OPENID_CONNECT\",\n    \"grantTypes\": [\n        \"AUTHORIZATION_CODE\"\n    ],\n    \"redirectUris\": [\n        \"http://localhost:3000/callback\"\n    ],\n    \"responseTypes\": [\n        \"CODE\"\n    ],\n    \"tokenEndpointAuthMethod\": \"NONE\",\n    \"pkceEnforcement\": \"S256_REQUIRED\"\n}");
Request request = new Request.Builder()
  .url("{{apiPath}}/v1/environments/{{envID}}/applications")
  .method("POST", body)
  .addHeader("Content-Type", "application/json")
  .addHeader("Authorization", "Bearer {{accessToken}}")
  .build();
Response response = client.newCall(request).execute();
```

```javascript
var settings = {
  "url": "{{apiPath}}/v1/environments/{{envID}}/applications",
  "method": "POST",
  "timeout": 0,
  "headers": {
    "Content-Type": "application/json",
    "Authorization": "Bearer {{accessToken}}"
  },
  "data": JSON.stringify({
    "enabled": true,
    "name": "Shared-Native-App",
    "description": "Public client application with NONE authentication - for SPAs and mobile apps that cannot securely store secrets. MUST use PKCE for security.",
    "type": "NATIVE_APP",
    "protocol": "OPENID_CONNECT",
    "grantTypes": [
      "AUTHORIZATION_CODE"
    ],
    "redirectUris": [
      "http://localhost:3000/callback"
    ],
    "responseTypes": [
      "CODE"
    ],
    "tokenEndpointAuthMethod": "NONE",
    "pkceEnforcement": "S256_REQUIRED"
  }),
};

$.ajax(settings).done(function (response) {
  console.log(response);
});
```

```javascript
var request = require('request');
var options = {
  'method': 'POST',
  'url': '{{apiPath}}/v1/environments/{{envID}}/applications',
  'headers': {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer {{accessToken}}'
  },
  body: JSON.stringify({
    "enabled": true,
    "name": "Shared-Native-App",
    "description": "Public client application with NONE authentication - for SPAs and mobile apps that cannot securely store secrets. MUST use PKCE for security.",
    "type": "NATIVE_APP",
    "protocol": "OPENID_CONNECT",
    "grantTypes": [
      "AUTHORIZATION_CODE"
    ],
    "redirectUris": [
      "http://localhost:3000/callback"
    ],
    "responseTypes": [
      "CODE"
    ],
    "tokenEndpointAuthMethod": "NONE",
    "pkceEnforcement": "S256_REQUIRED"
  })

};
request(options, function (error, response) {
  if (error) throw new Error(error);
  console.log(response.body);
});
```

```python
import requests
import json

url = "{{apiPath}}/v1/environments/{{envID}}/applications"

payload = json.dumps({
  "enabled": True,
  "name": "Shared-Native-App",
  "description": "Public client application with NONE authentication - for SPAs and mobile apps that cannot securely store secrets. MUST use PKCE for security.",
  "type": "NATIVE_APP",
  "protocol": "OPENID_CONNECT",
  "grantTypes": [
    "AUTHORIZATION_CODE"
  ],
  "redirectUris": [
    "http://localhost:3000/callback"
  ],
  "responseTypes": [
    "CODE"
  ],
  "tokenEndpointAuthMethod": "NONE",
  "pkceEnforcement": "S256_REQUIRED"
})
headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Bearer {{accessToken}}'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
```

```php
<?php
require_once 'HTTP/Request2.php';
$request = new HTTP_Request2();
$request->setUrl('{{apiPath}}/v1/environments/{{envID}}/applications');
$request->setMethod(HTTP_Request2::METHOD_POST);
$request->setConfig(array(
  'follow_redirects' => TRUE
));
$request->setHeader(array(
  'Content-Type' => 'application/json',
  'Authorization' => 'Bearer {{accessToken}}'
));
$request->setBody('{\n    "enabled": true,\n    "name": "Shared-Native-App",\n    "description": "Public client application with NONE authentication - for SPAs and mobile apps that cannot securely store secrets. MUST use PKCE for security.",\n    "type": "NATIVE_APP",\n    "protocol": "OPENID_CONNECT",\n    "grantTypes": [\n        "AUTHORIZATION_CODE"\n    ],\n    "redirectUris": [\n        "http://localhost:3000/callback"\n    ],\n    "responseTypes": [\n        "CODE"\n    ],\n    "tokenEndpointAuthMethod": "NONE",\n    "pkceEnforcement": "S256_REQUIRED"\n}');
try {
  $response = $request->send();
  if ($response->getStatus() == 200) {
    echo $response->getBody();
  }
  else {
    echo 'Unexpected HTTP status: ' . $response->getStatus() . ' ' .
    $response->getReasonPhrase();
  }
}
catch(HTTP_Request2_Exception $e) {
  echo 'Error: ' . $e->getMessage();
}
```

```ruby
require "uri"
require "json"
require "net/http"

url = URI("{{apiPath}}/v1/environments/{{envID}}/applications")

http = Net::HTTP.new(url.host, url.port);
request = Net::HTTP::Post.new(url)
request["Content-Type"] = "application/json"
request["Authorization"] = "Bearer {{accessToken}}"
request.body = JSON.dump({
  "enabled": true,
  "name": "Shared-Native-App",
  "description": "Public client application with NONE authentication - for SPAs and mobile apps that cannot securely store secrets. MUST use PKCE for security.",
  "type": "NATIVE_APP",
  "protocol": "OPENID_CONNECT",
  "grantTypes": [
    "AUTHORIZATION_CODE"
  ],
  "redirectUris": [
    "http://localhost:3000/callback"
  ],
  "responseTypes": [
    "CODE"
  ],
  "tokenEndpointAuthMethod": "NONE",
  "pkceEnforcement": "S256_REQUIRED"
})

response = http.request(request)
puts response.read_body
```

```swift
let parameters = "{\n    \"enabled\": true,\n    \"name\": \"Shared-Native-App\",\n    \"description\": \"Public client application with NONE authentication - for SPAs and mobile apps that cannot securely store secrets. MUST use PKCE for security.\",\n    \"type\": \"NATIVE_APP\",\n    \"protocol\": \"OPENID_CONNECT\",\n    \"grantTypes\": [\n        \"AUTHORIZATION_CODE\"\n    ],\n    \"redirectUris\": [\n        \"http://localhost:3000/callback\"\n    ],\n    \"responseTypes\": [\n        \"CODE\"\n    ],\n    \"tokenEndpointAuthMethod\": \"NONE\",\n    \"pkceEnforcement\": \"S256_REQUIRED\"\n}"
let postData = parameters.data(using: .utf8)

var request = URLRequest(url: URL(string: "{{apiPath}}/v1/environments/{{envID}}/applications")!,timeoutInterval: Double.infinity)
request.addValue("application/json", forHTTPHeaderField: "Content-Type")
request.addValue("Bearer {{accessToken}}", forHTTPHeaderField: "Authorization")

request.httpMethod = "POST"
request.httpBody = postData

let task = URLSession.shared.dataTask(with: request) { data, response, error in
  guard let data = data else {
    print(String(describing: error))
    return
  }
  print(String(data: data, encoding: .utf8)!)
}

task.resume()
```

### Example Response

201 Created

```json
{
    "_links": {
        "self": {
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/applications/7e94e040-aef8-402a-80fe-01a954a03465"
        },
        "environment": {
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
        },
        "metadata": {
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/applications/7e94e040-aef8-402a-80fe-01a954a03465/metadata"
        },
        "attributes": {
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/applications/7e94e040-aef8-402a-80fe-01a954a03465/attributes"
        },
        "pushCredentials": {
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/applications/7e94e040-aef8-402a-80fe-01a954a03465/pushCredentials"
        },
        "secret": {
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/applications/7e94e040-aef8-402a-80fe-01a954a03465/secret"
        },
        "grants": {
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/applications/7e94e040-aef8-402a-80fe-01a954a03465/grants"
        },
        "keyRotationPolicy": {
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/keyRotationPolicies/1cb8d0b5-c7ba-42e8-a556-240ea2410f1d"
        }
    },
    "environment": {
        "id": "abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
    },
    "id": "7e94e040-aef8-402a-80fe-01a954a03465",
    "name": "Shared-Native-App",
    "description": "Public client application with NONE authentication - for SPAs and mobile apps that cannot securely store secrets. MUST use PKCE for security.",
    "enabled": true,
    "hiddenFromAppPortal": false,
    "type": "NATIVE_APP",
    "protocol": "OPENID_CONNECT",
    "createdAt": "2026-04-20T16:33:44.010Z",
    "updatedAt": "2026-04-20T16:33:44.010Z",
    "clientId": "7e94e040-aef8-402a-80fe-01a954a03465",
    "assignActorRoles": false,
    "mobile": {
        "integrityDetection": {
            "mode": "DISABLED"
        },
        "passcodeRefreshDuration": {
            "duration": 30,
            "timeUnit": "SECONDS"
        },
        "passcodeGracePeriod": 5
    },
    "responseTypes": [
        "CODE"
    ],
    "pkceEnforcement": "S256_REQUIRED",
    "requestScopesForMultipleResourcesEnabled": false,
    "redirectUris": [
        "http://localhost:3000/callback"
    ],
    "deviceTimeout": 600,
    "grantTypes": [
        "AUTHORIZATION_CODE"
    ],
    "idpSignoff": false,
    "additionalRefreshTokenReplayProtectionEnabled": true,
    "tokenEndpointAuthMethod": "NONE",
    "parRequirement": "OPTIONAL",
    "devicePollingInterval": 5,
    "parTimeout": 60,
    "signing": {
        "keyRotationPolicy": {
            "id": "1cb8d0b5-c7ba-42e8-a556-240ea2410f1d"
        }
    }
}
```

---

---
title: DaVinci Registration Flow with PingOne Auth
description: This activity uses the PingOne application and flow policy that you configured in the DaVinci Sign-On Flow with PingOne Auth workflow. If you haven't completed this workflow, do that first before you begin the registration flow.
component: pingone-api
page_id: pingone-api:workflow-library:pingone-davinci/davinci-registration-flow-with-pingone-auth
canonical_url: https://developer.pingidentity.com/pingone-api/workflow-library/pingone-davinci/davinci-registration-flow-with-pingone-auth.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
---

# DaVinci Registration Flow with PingOne Auth

This activity uses the PingOne application and flow policy that you configured in the [DaVinci Sign-On Flow with PingOne Auth](davinci-sign-on-flow-with-pingone-auth.html) workflow. If you haven't completed this workflow, do that first before you begin the registration flow.

|   |                                                                                                                                                                                                                                                       |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | This workflow uses the default DaVinci flow policy that is included automatically when you add the DaVinci product to your environment. The default DaVinci flow includes registration actions that you will call in the flow capabilities endpoints. |

This scenario illustrates the following common operations supported by the PingOne APIs:

* Create the PingOne authorize request.

* Create the DaVinci flow capabilities requests to manage the registration workflow and get the session token.

Click the **Run in Postman** button below to fork, or download and import, the Postman collection for this workflow to your workspace.

[Run in Postman](https://god.gw.postman.com/run-collection/18568624-eec93681-1392-417d-a126-9c2ea7875c04?action=collection%2Ffork\&source=rip_markdown\&collection-url=entityId%3D18568624-eec93681-1392-417d-a126-9c2ea7875c04%26entityType%3Dcollection%26workspaceId%3D3550b170-7818-4801-b1eb-dcb7b3f64263#?env%5BPingOne%20Workflow%20Library%20Template%20%28release%3A%202025-04-17%29%5D=W3sia2V5IjoidGxkIiwidmFsdWUiOiJjb20iLCJlbmFibGVkIjp0cnVlLCJ0eXBlIjoiZGVmYXVsdCJ9LHsia2V5IjoiYXV0aFBhdGgiLCJ2YWx1ZSI6Imh0dHBzOi8vYXV0aC5waW5nb25lLnt7dGxkfX0iLCJlbmFibGVkIjp0cnVlLCJ0eXBlIjoiZGVmYXVsdCJ9LHsia2V5IjoiYXBpUGF0aCIsInZhbHVlIjoiaHR0cHM6Ly9hcGkucGluZ29uZS57e3RsZH19L3YxIiwiZW5hYmxlZCI6dHJ1ZSwidHlwZSI6ImRlZmF1bHQifSx7ImtleSI6ImFkbWluRW52SUQiLCJ2YWx1ZSI6IiIsImVuYWJsZWQiOnRydWUsInR5cGUiOiJkZWZhdWx0In0seyJrZXkiOiJhZG1pbkFwcElEIiwidmFsdWUiOiIiLCJlbmFibGVkIjp0cnVlLCJ0eXBlIjoiZGVmYXVsdCJ9LHsia2V5IjoiYWRtaW5BcHBTZWNyZXQiLCJ2YWx1ZSI6IiIsImVuYWJsZWQiOnRydWUsInR5cGUiOiJkZWZhdWx0In0seyJrZXkiOiJlbnZJRCIsInZhbHVlIjoiIiwiZW5hYmxlZCI6dHJ1ZSwidHlwZSI6ImRlZmF1bHQifV0=)

---

---
title: DaVinci Sign-On Flow with PingOne Auth
description: This activity shows you how to create a PingOne application, find and associate a DaVinci flow policy with the application, and initiate the flow using a PingOne authorize request. The authorize request sets the response_mode property to pi.flow, which tells the authorization server to return data, instead of a redirect URL. In addition, the authorize request sets the X-Requested-With HTTP header with a value of ping-sdk to return JSON instead of HTML (and scripts).
component: pingone-api
page_id: pingone-api:workflow-library:pingone-davinci/davinci-sign-on-flow-with-pingone-auth
canonical_url: https://developer.pingidentity.com/pingone-api/workflow-library/pingone-davinci/davinci-sign-on-flow-with-pingone-auth.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
---

# DaVinci Sign-On Flow with PingOne Auth

This activity shows you how to create a PingOne application, find and associate a DaVinci flow policy with the application, and initiate the flow using a PingOne authorize request. The authorize request sets the `response_mode` property to `pi.flow`, which tells the authorization server to return data, instead of a redirect URL. In addition, the authorize request sets the `X-Requested-With` HTTP header with a value of `ping-sdk` to return JSON instead of HTML (and scripts).

|   |                                                                                                                                                                                                                                                                                                                                                            |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | This workflow uses the default DaVinci flow policy that is included automatically when you add the DaVinci product to your environment. DaVinci defaults include a DaVinci flow that defines sign-on, registration, and password recovery flow actions. There is also a default DaVinci application that uses this default flow to create the flow policy. |

This scenario illustrates the following common operations supported by the PingOne APIs:

* Get the DaVinci flow policy ID.

* Assign a DaVinci flow policy to a PingOne application.

* Create the PingOne authorize request.

* Configure the DaVinci flow capability endpoints to complete the authentication steps.

* Call the PingOne token request to get an access token.

Click the **Run in Postman** button below to fork, or download and import, the Postman collection for this workflow to your workspace.

[Run in Postman](https://god.gw.postman.com/run-collection/18568624-ea2ad46c-a92a-44b2-9318-42f02fb165f8?action=collection%2Ffork\&source=rip_markdown\&collection-url=entityId%3D18568624-ea2ad46c-a92a-44b2-9318-42f02fb165f8%26entityType%3Dcollection%26workspaceId%3D3550b170-7818-4801-b1eb-dcb7b3f64263#?env%5BPingOne%20Workflow%20Library%20Template%20%28release%3A%202025-04-17%29%5D=W3sia2V5IjoidGxkIiwidmFsdWUiOiJjb20iLCJlbmFibGVkIjp0cnVlLCJ0eXBlIjoiZGVmYXVsdCJ9LHsia2V5IjoiYXV0aFBhdGgiLCJ2YWx1ZSI6Imh0dHBzOi8vYXV0aC5waW5nb25lLnt7dGxkfX0iLCJlbmFibGVkIjp0cnVlLCJ0eXBlIjoiZGVmYXVsdCJ9LHsia2V5IjoiYXBpUGF0aCIsInZhbHVlIjoiaHR0cHM6Ly9hcGkucGluZ29uZS57e3RsZH19L3YxIiwiZW5hYmxlZCI6dHJ1ZSwidHlwZSI6ImRlZmF1bHQifSx7ImtleSI6ImFkbWluRW52SUQiLCJ2YWx1ZSI6IiIsImVuYWJsZWQiOnRydWUsInR5cGUiOiJkZWZhdWx0In0seyJrZXkiOiJhZG1pbkFwcElEIiwidmFsdWUiOiIiLCJlbmFibGVkIjp0cnVlLCJ0eXBlIjoiZGVmYXVsdCJ9LHsia2V5IjoiYWRtaW5BcHBTZWNyZXQiLCJ2YWx1ZSI6IiIsImVuYWJsZWQiOnRydWUsInR5cGUiOiJkZWZhdWx0In0seyJrZXkiOiJlbnZJRCIsInZhbHVlIjoiIiwiZW5hYmxlZCI6dHJ1ZSwidHlwZSI6ImRlZmF1bHQifV0=)

---

---
title: Device Authorization Grant Flow
description: This activity shows you how to initiate a device authorization grant flow to send an activation code to the end user. The authorization and flow orchestration steps apply only to applications that specify device_code as a grant type in the application configuration.
component: pingone-api
page_id: pingone-api:workflow-library:platform-sso-and-authorization/openid-connect-oidc/device-authorization-grant-flow
canonical_url: https://developer.pingidentity.com/pingone-api/workflow-library/platform-sso-and-authorization/openid-connect-oidc/device-authorization-grant-flow.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  prerequisites: Prerequisites
---

# Device Authorization Grant Flow

This activity shows you how to initiate a device authorization grant flow to send an activation code to the end user. The authorization and flow orchestration steps apply only to applications that specify `device_code` as a grant type in the application configuration.

The following operations are supported by the PingOne APIs:

* Create an application

* Create a population and a user

* Initiate an authorize request

* Use flow APIs to complete the flow

## Prerequisites

* Get an access token from the worker application you created in [Create an admin Worker app connection](../../../getting-started/create-an-admin-worker-app.html). If you prefer to get a token from a different worker application in an alternate sandbox environment, run the token request endpoint using the client ID and client secret of your chosen worker app to authenticate the request. Refer to [Get a PingOne admin access token](../../../getting-started/create-a-test-environment/step-1-get-access-token.html).

[Run in Postman](https://god.gw.postman.com/run-collection/18568624-08fad81d-7266-4f54-aa43-803c5f6e96c8?action=collection%2Ffork\&source=rip_markdown\&collection-url=entityId%3D18568624-08fad81d-7266-4f54-aa43-803c5f6e96c8%26entityType%3Dcollection%26workspaceId%3D3550b170-7818-4801-b1eb-dcb7b3f64263#?env%5BPingOne%20Workflow%20Library%20Template%20%28release%3A%202025-04-17%29%5D=W3sia2V5IjoidGxkIiwidmFsdWUiOiJjb20iLCJlbmFibGVkIjp0cnVlLCJ0eXBlIjoiZGVmYXVsdCJ9LHsia2V5IjoiYXV0aFBhdGgiLCJ2YWx1ZSI6Imh0dHBzOi8vYXV0aC5waW5nb25lLnt7dGxkfX0iLCJlbmFibGVkIjp0cnVlLCJ0eXBlIjoiZGVmYXVsdCJ9LHsia2V5IjoiYXBpUGF0aCIsInZhbHVlIjoiaHR0cHM6Ly9hcGkucGluZ29uZS57e3RsZH19L3YxIiwiZW5hYmxlZCI6dHJ1ZSwidHlwZSI6ImRlZmF1bHQifSx7ImtleSI6ImFkbWluRW52SUQiLCJ2YWx1ZSI6IiIsImVuYWJsZWQiOnRydWUsInR5cGUiOiJkZWZhdWx0In0seyJrZXkiOiJhZG1pbkFwcElEIiwidmFsdWUiOiIiLCJlbmFibGVkIjp0cnVlLCJ0eXBlIjoiZGVmYXVsdCJ9LHsia2V5IjoiYWRtaW5BcHBTZWNyZXQiLCJ2YWx1ZSI6IiIsImVuYWJsZWQiOnRydWUsInR5cGUiOiJkZWZhdWx0In0seyJrZXkiOiJlbnZJRCIsInZhbHVlIjoiIiwiZW5hYmxlZCI6dHJ1ZSwidHlwZSI6ImRlZmF1bHQifV0=)

---

---
title: Find and Terminate a User Session
description: This activity shows you how to find and terminate a user session.
component: pingone-api
page_id: pingone-api:workflow-library:platform-sso-and-authorization/sessions-and-logout/find-and-terminate-a-user-session
canonical_url: https://developer.pingidentity.com/pingone-api/workflow-library/platform-sso-and-authorization/sessions-and-logout/find-and-terminate-a-user-session.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  prerequisites: Prerequisites
---

# Find and Terminate a User Session

This activity shows you how to find and terminate a user session.

The following operations are supported by the PingOne APIs:

* Read a user session

* Delete a user session

## Prerequisites

* Create a user and initiate a user session in [Simple Login - Username and Password](../openid-connect-oidc/simple-login-username-and-password.html).

Click the **Run in Postman** button below to fork, or download and import, the Postman collection for this workflow to your workspace.

[Run in Postman](https://god.gw.postman.com/run-collection/18568624-545436b9-d443-440a-a9b7-8cf1c3605810?action=collection%2Ffork\&source=rip_markdown\&collection-url=entityId%3D18568624-545436b9-d443-440a-a9b7-8cf1c3605810%26entityType%3Dcollection%26workspaceId%3D3550b170-7818-4801-b1eb-dcb7b3f64263#?env%5BPingOne%20Workflow%20Library%20Template%20%28release%3A%202025-04-17%29%5D=W3sia2V5IjoidGxkIiwidmFsdWUiOiJjb20iLCJlbmFibGVkIjp0cnVlLCJ0eXBlIjoiZGVmYXVsdCJ9LHsia2V5IjoiYXV0aFBhdGgiLCJ2YWx1ZSI6Imh0dHBzOi8vYXV0aC5waW5nb25lLnt7dGxkfX0iLCJlbmFibGVkIjp0cnVlLCJ0eXBlIjoiZGVmYXVsdCJ9LHsia2V5IjoiYXBpUGF0aCIsInZhbHVlIjoiaHR0cHM6Ly9hcGkucGluZ29uZS57e3RsZH19L3YxIiwiZW5hYmxlZCI6dHJ1ZSwidHlwZSI6ImRlZmF1bHQifSx7ImtleSI6ImFkbWluRW52SUQiLCJ2YWx1ZSI6IiIsImVuYWJsZWQiOnRydWUsInR5cGUiOiJkZWZhdWx0In0seyJrZXkiOiJhZG1pbkFwcElEIiwidmFsdWUiOiIiLCJlbmFibGVkIjp0cnVlLCJ0eXBlIjoiZGVmYXVsdCJ9LHsia2V5IjoiYWRtaW5BcHBTZWNyZXQiLCJ2YWx1ZSI6IiIsImVuYWJsZWQiOnRydWUsInR5cGUiOiJkZWZhdWx0In0seyJrZXkiOiJlbnZJRCIsInZhbHVlIjoiIiwiZW5hYmxlZCI6dHJ1ZSwidHlwZSI6ImRlZmF1bHQifV0=)

---

---
title: "Step 1: Create a risk policy set"
component: pingone-api
page_id: pingone-api:workflow-library:pingone-protect/create-a-risk-policy-set/step-2-create-a-risk-policy-set
canonical_url: https://developer.pingidentity.com/pingone-api/workflow-library/pingone-protect/create-a-risk-policy-set/step-2-create-a-risk-policy-set.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  headers: Headers
  body: Body
  example-request: Example Request
  example-response: Example Response
---

# Step 1: Create a risk policy set

##

 

```none
POST {{apiPath}}/v1/environments/{{envID}}/riskPolicySets
```

A risk policy is determined by the customer's specific configuration settings as well as intelligence gathered from common use cases, which are then used in event evaluation to calculate risk scores for received events.

The `POST {{apiPath}}/v1/environments/{{envID}}/riskPolicySets/` creates a new risk policy set in the specified environment. In the request body, you must define at least one risk policy in the `riskPolicies` property array, and the risk policy definition must specify a `condition` expression and a `result`. The `priority` property in the risk policy definition is optional. In this scenario, you will define the whitelist and anonymous network detection policies.

### Headers

Authorization      Bearer {{accessToken}}

Content-Type      application/json

### Body

raw ( application/json )

```json
{
    "name": "Use_Case_Risk_Policy_Set",
    "description": "Custom risk policy set",
    "defaultResult": {
        "level": "Low"
    },
    "riskPolicies": [
        {
            "name": "WHITELIST",
            "priority": 1,
            "result": {
                "level": "LOW"
            },
            "condition": {
                "contains": "${transaction.ip}",
                "ipRange": [
                    "1.1.1.1/16",
                    "2.2.2.2/24"
                ]
            }
        },
        {
            "name": "ANONYMOUS_NETWORK_DETECTION",
            "result": {
                "level": "HIGH"
            },
            "condition": {
                "value": "${details.anonymousNetworkDetected}",
                "equals": true
            }
        }
    ]
}
```

##

### Example Request

* cURL

* C#

* Go

* HTTP

* Java

* jQuery

* NodeJS

* Python

* PHP

* Ruby

* Swift

```shell
curl --location --globoff '{{apiPath}}/v1/environments/{{envID}}/riskPolicySets' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {{accessToken}}' \
--data '{
    "name": "Use_Case_Risk_Policy_Set",
    "description": "Custom risk policy set",
    "defaultResult": {
        "level": "Low"
    },
    "riskPolicies": [
        {
            "name": "WHITELIST",
            "priority": 1,
            "result": {
                "level": "LOW"
            },
            "condition": {
                "contains": "${transaction.ip}",
                "ipRange": [
                    "1.1.1.1/16",
                    "2.2.2.2/24"
                ]
            }
        },
        {
            "name": "ANONYMOUS_NETWORK_DETECTION",
            "result": {
                "level": "HIGH"
            },
            "condition": {
                "value": "${details.anonymousNetworkDetected}",
                "equals": true
            }
        }
    ]
}'
```

```csharp
var options = new RestClientOptions("{{apiPath}}/v1/environments/{{envID}}/riskPolicySets")
{
  MaxTimeout = -1,
};
var client = new RestClient(options);
var request = new RestRequest("", Method.Post);
request.AddHeader("Content-Type", "application/json");
request.AddHeader("Authorization", "Bearer {{accessToken}}");
var body = @"{" + "\n" +
@"    ""name"": ""Use_Case_Risk_Policy_Set""," + "\n" +
@"    ""description"": ""Custom risk policy set""," + "\n" +
@"    ""defaultResult"": {" + "\n" +
@"        ""level"": ""Low""" + "\n" +
@"    }," + "\n" +
@"    ""riskPolicies"": [" + "\n" +
@"        {" + "\n" +
@"            ""name"": ""WHITELIST""," + "\n" +
@"            ""priority"": 1," + "\n" +
@"            ""result"": {" + "\n" +
@"                ""level"": ""LOW""" + "\n" +
@"            }," + "\n" +
@"            ""condition"": {" + "\n" +
@"                ""contains"": ""${transaction.ip}""," + "\n" +
@"                ""ipRange"": [" + "\n" +
@"                    ""1.1.1.1/16""," + "\n" +
@"                    ""2.2.2.2/24""" + "\n" +
@"                ]" + "\n" +
@"            }" + "\n" +
@"        }," + "\n" +
@"        {" + "\n" +
@"            ""name"": ""ANONYMOUS_NETWORK_DETECTION""," + "\n" +
@"            ""result"": {" + "\n" +
@"                ""level"": ""HIGH""" + "\n" +
@"            }," + "\n" +
@"            ""condition"": {" + "\n" +
@"                ""value"": ""${details.anonymousNetworkDetected}""," + "\n" +
@"                ""equals"": true" + "\n" +
@"            }" + "\n" +
@"        }" + "\n" +
@"    ]" + "\n" +
@"}";
request.AddStringBody(body, DataFormat.Json);
RestResponse response = await client.ExecuteAsync(request);
Console.WriteLine(response.Content);
```

```golang
package main

import (
  "fmt"
  "strings"
  "net/http"
  "io"
)

func main() {

  url := "{{apiPath}}/v1/environments/{{envID}}/riskPolicySets"
  method := "POST"

  payload := strings.NewReader(`{
    "name": "Use_Case_Risk_Policy_Set",
    "description": "Custom risk policy set",
    "defaultResult": {
        "level": "Low"
    },
    "riskPolicies": [
        {
            "name": "WHITELIST",
            "priority": 1,
            "result": {
                "level": "LOW"
            },
            "condition": {
                "contains": "${transaction.ip}",
                "ipRange": [
                    "1.1.1.1/16",
                    "2.2.2.2/24"
                ]
            }
        },
        {
            "name": "ANONYMOUS_NETWORK_DETECTION",
            "result": {
                "level": "HIGH"
            },
            "condition": {
                "value": "${details.anonymousNetworkDetected}",
                "equals": true
            }
        }
    ]
}`)

  client := &http.Client {
  }
  req, err := http.NewRequest(method, url, payload)

  if err != nil {
    fmt.Println(err)
    return
  }
  req.Header.Add("Content-Type", "application/json")
  req.Header.Add("Authorization", "Bearer {{accessToken}}")

  res, err := client.Do(req)
  if err != nil {
    fmt.Println(err)
    return
  }
  defer res.Body.Close()

  body, err := io.ReadAll(res.Body)
  if err != nil {
    fmt.Println(err)
    return
  }
  fmt.Println(string(body))
}
```

```http
POST /v1/environments/{{envID}}/riskPolicySets HTTP/1.1
Host: {{apiPath}}
Content-Type: application/json
Authorization: Bearer {{accessToken}}

{
    "name": "Use_Case_Risk_Policy_Set",
    "description": "Custom risk policy set",
    "defaultResult": {
        "level": "Low"
    },
    "riskPolicies": [
        {
            "name": "WHITELIST",
            "priority": 1,
            "result": {
                "level": "LOW"
            },
            "condition": {
                "contains": "${transaction.ip}",
                "ipRange": [
                    "1.1.1.1/16",
                    "2.2.2.2/24"
                ]
            }
        },
        {
            "name": "ANONYMOUS_NETWORK_DETECTION",
            "result": {
                "level": "HIGH"
            },
            "condition": {
                "value": "${details.anonymousNetworkDetected}",
                "equals": true
            }
        }
    ]
}
```

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("application/json");
RequestBody body = RequestBody.create(mediaType, "{\n    \"name\": \"Use_Case_Risk_Policy_Set\",\n    \"description\": \"Custom risk policy set\",\n    \"defaultResult\": {\n        \"level\": \"Low\"\n    },\n    \"riskPolicies\": [\n        {\n            \"name\": \"WHITELIST\",\n            \"priority\": 1,\n            \"result\": {\n                \"level\": \"LOW\"\n            },\n            \"condition\": {\n                \"contains\": \"${transaction.ip}\",\n                \"ipRange\": [\n                    \"1.1.1.1/16\",\n                    \"2.2.2.2/24\"\n                ]\n            }\n        },\n        {\n            \"name\": \"ANONYMOUS_NETWORK_DETECTION\",\n            \"result\": {\n                \"level\": \"HIGH\"\n            },\n            \"condition\": {\n                \"value\": \"${details.anonymousNetworkDetected}\",\n                \"equals\": true\n            }\n        }\n    ]\n}");
Request request = new Request.Builder()
  .url("{{apiPath}}/v1/environments/{{envID}}/riskPolicySets")
  .method("POST", body)
  .addHeader("Content-Type", "application/json")
  .addHeader("Authorization", "Bearer {{accessToken}}")
  .build();
Response response = client.newCall(request).execute();
```

```javascript
var settings = {
  "url": "{{apiPath}}/v1/environments/{{envID}}/riskPolicySets",
  "method": "POST",
  "timeout": 0,
  "headers": {
    "Content-Type": "application/json",
    "Authorization": "Bearer {{accessToken}}"
  },
  "data": JSON.stringify({
    "name": "Use_Case_Risk_Policy_Set",
    "description": "Custom risk policy set",
    "defaultResult": {
      "level": "Low"
    },
    "riskPolicies": [
      {
        "name": "WHITELIST",
        "priority": 1,
        "result": {
          "level": "LOW"
        },
        "condition": {
          "contains": "${transaction.ip}",
          "ipRange": [
            "1.1.1.1/16",
            "2.2.2.2/24"
          ]
        }
      },
      {
        "name": "ANONYMOUS_NETWORK_DETECTION",
        "result": {
          "level": "HIGH"
        },
        "condition": {
          "value": "${details.anonymousNetworkDetected}",
          "equals": true
        }
      }
    ]
  }),
};

$.ajax(settings).done(function (response) {
  console.log(response);
});
```

```javascript
var request = require('request');
var options = {
  'method': 'POST',
  'url': '{{apiPath}}/v1/environments/{{envID}}/riskPolicySets',
  'headers': {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer {{accessToken}}'
  },
  body: JSON.stringify({
    "name": "Use_Case_Risk_Policy_Set",
    "description": "Custom risk policy set",
    "defaultResult": {
      "level": "Low"
    },
    "riskPolicies": [
      {
        "name": "WHITELIST",
        "priority": 1,
        "result": {
          "level": "LOW"
        },
        "condition": {
          "contains": "${transaction.ip}",
          "ipRange": [
            "1.1.1.1/16",
            "2.2.2.2/24"
          ]
        }
      },
      {
        "name": "ANONYMOUS_NETWORK_DETECTION",
        "result": {
          "level": "HIGH"
        },
        "condition": {
          "value": "${details.anonymousNetworkDetected}",
          "equals": true
        }
      }
    ]
  })

};
request(options, function (error, response) {
  if (error) throw new Error(error);
  console.log(response.body);
});
```

```python
import requests
import json

url = "{{apiPath}}/v1/environments/{{envID}}/riskPolicySets"

payload = json.dumps({
  "name": "Use_Case_Risk_Policy_Set",
  "description": "Custom risk policy set",
  "defaultResult": {
    "level": "Low"
  },
  "riskPolicies": [
    {
      "name": "WHITELIST",
      "priority": 1,
      "result": {
        "level": "LOW"
      },
      "condition": {
        "contains": "${transaction.ip}",
        "ipRange": [
          "1.1.1.1/16",
          "2.2.2.2/24"
        ]
      }
    },
    {
      "name": "ANONYMOUS_NETWORK_DETECTION",
      "result": {
        "level": "HIGH"
      },
      "condition": {
        "value": "${details.anonymousNetworkDetected}",
        "equals": True
      }
    }
  ]
})
headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Bearer {{accessToken}}'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
```

```php
<?php
require_once 'HTTP/Request2.php';
$request = new HTTP_Request2();
$request->setUrl('{{apiPath}}/v1/environments/{{envID}}/riskPolicySets');
$request->setMethod(HTTP_Request2::METHOD_POST);
$request->setConfig(array(
  'follow_redirects' => TRUE
));
$request->setHeader(array(
  'Content-Type' => 'application/json',
  'Authorization' => 'Bearer {{accessToken}}'
));
$request->setBody('{\n    "name": "Use_Case_Risk_Policy_Set",\n    "description": "Custom risk policy set",\n    "defaultResult": {\n        "level": "Low"\n    },\n    "riskPolicies": [\n        {\n            "name": "WHITELIST",\n            "priority": 1,\n            "result": {\n                "level": "LOW"\n            },\n            "condition": {\n                "contains": "${transaction.ip}",\n                "ipRange": [\n                    "1.1.1.1/16",\n                    "2.2.2.2/24"\n                ]\n            }\n        },\n        {\n            "name": "ANONYMOUS_NETWORK_DETECTION",\n            "result": {\n                "level": "HIGH"\n            },\n            "condition": {\n                "value": "${details.anonymousNetworkDetected}",\n                "equals": true\n            }\n        }\n    ]\n}');
try {
  $response = $request->send();
  if ($response->getStatus() == 200) {
    echo $response->getBody();
  }
  else {
    echo 'Unexpected HTTP status: ' . $response->getStatus() . ' ' .
    $response->getReasonPhrase();
  }
}
catch(HTTP_Request2_Exception $e) {
  echo 'Error: ' . $e->getMessage();
}
```

```ruby
require "uri"
require "json"
require "net/http"

url = URI("{{apiPath}}/v1/environments/{{envID}}/riskPolicySets")

http = Net::HTTP.new(url.host, url.port);
request = Net::HTTP::Post.new(url)
request["Content-Type"] = "application/json"
request["Authorization"] = "Bearer {{accessToken}}"
request.body = JSON.dump({
  "name": "Use_Case_Risk_Policy_Set",
  "description": "Custom risk policy set",
  "defaultResult": {
    "level": "Low"
  },
  "riskPolicies": [
    {
      "name": "WHITELIST",
      "priority": 1,
      "result": {
        "level": "LOW"
      },
      "condition": {
        "contains": "\${transaction.ip}",
        "ipRange": [
          "1.1.1.1/16",
          "2.2.2.2/24"
        ]
      }
    },
    {
      "name": "ANONYMOUS_NETWORK_DETECTION",
      "result": {
        "level": "HIGH"
      },
      "condition": {
        "value": "\${details.anonymousNetworkDetected}",
        "equals": true
      }
    }
  ]
})

response = http.request(request)
puts response.read_body
```

```swift
let parameters = "{\n    \"name\": \"Use_Case_Risk_Policy_Set\",\n    \"description\": \"Custom risk policy set\",\n    \"defaultResult\": {\n        \"level\": \"Low\"\n    },\n    \"riskPolicies\": [\n        {\n            \"name\": \"WHITELIST\",\n            \"priority\": 1,\n            \"result\": {\n                \"level\": \"LOW\"\n            },\n            \"condition\": {\n                \"contains\": \"${transaction.ip}\",\n                \"ipRange\": [\n                    \"1.1.1.1/16\",\n                    \"2.2.2.2/24\"\n                ]\n            }\n        },\n        {\n            \"name\": \"ANONYMOUS_NETWORK_DETECTION\",\n            \"result\": {\n                \"level\": \"HIGH\"\n            },\n            \"condition\": {\n                \"value\": \"${details.anonymousNetworkDetected}\",\n                \"equals\": true\n            }\n        }\n    ]\n}"
let postData = parameters.data(using: .utf8)

var request = URLRequest(url: URL(string: "{{apiPath}}/v1/environments/{{envID}}/riskPolicySets")!,timeoutInterval: Double.infinity)
request.addValue("application/json", forHTTPHeaderField: "Content-Type")
request.addValue("Bearer {{accessToken}}", forHTTPHeaderField: "Authorization")

request.httpMethod = "POST"
request.httpBody = postData

let task = URLSession.shared.dataTask(with: request) { data, response, error in
  guard let data = data else {
    print(String(describing: error))
    return
  }
  print(String(data: data, encoding: .utf8)!)
}

task.resume()
```

### Example Response

201 Created

```json
{
    "_links": {
        "self": {
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/riskPolicySets/22b059a4-b027-4e2c-a685-1207fa53a455"
        },
        "environment": {
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
        }
    },
    "id": "22b059a4-b027-4e2c-a685-1207fa53a455",
    "environment": {
        "id": "abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
    },
    "name": "Use_Case_Risk_Policy_Set",
    "description": "Custom risk policy set",
    "createdAt": "2021-02-25T00:05:57.566Z",
    "updatedAt": "2021-02-25T00:05:57.566Z",
    "defaultResult": {
        "level": "LOW",
        "type": "VALUE"
    },
    "riskPolicies": [
        {
            "id": "134715be-27c7-4887-97fb-e4141217e9d2",
            "environment": {
                "id": "abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
            },
            "policySet": {
                "id": "22b059a4-b027-4e2c-a685-1207fa53a455"
            },
            "name": "WHITELIST",
            "priority": 1,
            "result": {
                "level": "LOW",
                "type": "VALUE"
            },
            "condition": {
                "ipRange": [
                    "1.1.1.1/16",
                    "2.2.2.2/24"
                ],
                "contains": "${transaction.ip}"
            },
            "createdAt": "2021-02-25T00:05:57.566Z",
            "updatedAt": "2021-02-25T00:05:57.566Z"
        },
        {
            "id": "3e34788e-00f5-4480-88b5-3300e38757e1",
            "environment": {
                "id": "abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
            },
            "policySet": {
                "id": "22b059a4-b027-4e2c-a685-1207fa53a455"
            },
            "name": "ANONYMOUS_NETWORK_DETECTION",
            "priority": 2,
            "result": {
                "level": "HIGH",
                "type": "VALUE"
            },
            "condition": {
                "equals": true,
                "value": "${details.anonymousNetworkDetected}"
            },
            "createdAt": "2021-02-25T00:05:57.566Z",
            "updatedAt": "2021-02-25T00:05:57.566Z"
        }
    ],
    "default": false
}
```

---

---
title: "Step 1: Create a source population"
component: pingone-api
page_id: pingone-api:workflow-library:platform-sso-and-authorization/openid-connect-oidc/external-identity-provider-sign-on/configure-your-test-user/step-11-create-a-source-population
canonical_url: https://developer.pingidentity.com/pingone-api/workflow-library/platform-sso-and-authorization/openid-connect-oidc/external-identity-provider-sign-on/configure-your-test-user/step-11-create-a-source-population.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  headers: Headers
  body: Body
  example-request: Example Request
  example-response: Example Response
---

# Step 1: Create a source population

##

   

```none
POST {{apiPath}}/v1/environments/{{SourceEnvID}}/populations
```

Create a new population resource in the source environment using a `POST {{apiPath}}/v1/environments/{{SourceEnvID}}/populations` request.

* In the request body, the population `name` is required The `description` property is optional.

### Headers

Authorization      Bearer {{accessToken}}

Content-Type      application/json

### Body

raw ( application/json )

```json
{
    "name": "SourcePopulation_{{$timestamp}}",
    "description": "Population for simple login users"
}
```

##

### Example Request

* cURL

* C#

* Go

* HTTP

* Java

* jQuery

* NodeJS

* Python

* PHP

* Ruby

* Swift

```shell
curl --location --globoff '{{apiPath}}/v1/environments/{{SourceEnvID}}/populations' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {{accessToken}}' \
--data '{
    "name": "SourcePopulation_{{$timestamp}}",
    "description": "Population for simple login users"
}'
```

```csharp
var options = new RestClientOptions("{{apiPath}}/v1/environments/{{SourceEnvID}}/populations")
{
  MaxTimeout = -1,
};
var client = new RestClient(options);
var request = new RestRequest("", Method.Post);
request.AddHeader("Content-Type", "application/json");
request.AddHeader("Authorization", "Bearer {{accessToken}}");
var body = @"{" + "\n" +
@"    ""name"": ""SourcePopulation_{{$timestamp}}""," + "\n" +
@"    ""description"": ""Population for simple login users""" + "\n" +
@"}";
request.AddStringBody(body, DataFormat.Json);
RestResponse response = await client.ExecuteAsync(request);
Console.WriteLine(response.Content);
```

```golang
package main

import (
  "fmt"
  "strings"
  "net/http"
  "io"
)

func main() {

  url := "{{apiPath}}/v1/environments/{{SourceEnvID}}/populations"
  method := "POST"

  payload := strings.NewReader(`{
    "name": "SourcePopulation_{{$timestamp}}",
    "description": "Population for simple login users"
}`)

  client := &http.Client {
  }
  req, err := http.NewRequest(method, url, payload)

  if err != nil {
    fmt.Println(err)
    return
  }
  req.Header.Add("Content-Type", "application/json")
  req.Header.Add("Authorization", "Bearer {{accessToken}}")

  res, err := client.Do(req)
  if err != nil {
    fmt.Println(err)
    return
  }
  defer res.Body.Close()

  body, err := io.ReadAll(res.Body)
  if err != nil {
    fmt.Println(err)
    return
  }
  fmt.Println(string(body))
}
```

```http
POST /v1/environments/{{SourceEnvID}}/populations HTTP/1.1
Host: {{apiPath}}
Content-Type: application/json
Authorization: Bearer {{accessToken}}

{
    "name": "SourcePopulation_{{$timestamp}}",
    "description": "Population for simple login users"
}
```

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("application/json");
RequestBody body = RequestBody.create(mediaType, "{\n    \"name\": \"SourcePopulation_{{$timestamp}}\",\n    \"description\": \"Population for simple login users\"\n}");
Request request = new Request.Builder()
  .url("{{apiPath}}/v1/environments/{{SourceEnvID}}/populations")
  .method("POST", body)
  .addHeader("Content-Type", "application/json")
  .addHeader("Authorization", "Bearer {{accessToken}}")
  .build();
Response response = client.newCall(request).execute();
```

```javascript
var settings = {
  "url": "{{apiPath}}/v1/environments/{{SourceEnvID}}/populations",
  "method": "POST",
  "timeout": 0,
  "headers": {
    "Content-Type": "application/json",
    "Authorization": "Bearer {{accessToken}}"
  },
  "data": JSON.stringify({
    "name": "SourcePopulation_{{$timestamp}}",
    "description": "Population for simple login users"
  }),
};

$.ajax(settings).done(function (response) {
  console.log(response);
});
```

```javascript
var request = require('request');
var options = {
  'method': 'POST',
  'url': '{{apiPath}}/v1/environments/{{SourceEnvID}}/populations',
  'headers': {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer {{accessToken}}'
  },
  body: JSON.stringify({
    "name": "SourcePopulation_{{$timestamp}}",
    "description": "Population for simple login users"
  })

};
request(options, function (error, response) {
  if (error) throw new Error(error);
  console.log(response.body);
});
```

```python
import requests
import json

url = "{{apiPath}}/v1/environments/{{SourceEnvID}}/populations"

payload = json.dumps({
  "name": "SourcePopulation_{{$timestamp}}",
  "description": "Population for simple login users"
})
headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Bearer {{accessToken}}'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
```

```php
<?php
require_once 'HTTP/Request2.php';
$request = new HTTP_Request2();
$request->setUrl('{{apiPath}}/v1/environments/{{SourceEnvID}}/populations');
$request->setMethod(HTTP_Request2::METHOD_POST);
$request->setConfig(array(
  'follow_redirects' => TRUE
));
$request->setHeader(array(
  'Content-Type' => 'application/json',
  'Authorization' => 'Bearer {{accessToken}}'
));
$request->setBody('{\n    "name": "SourcePopulation_{{$timestamp}}",\n    "description": "Population for simple login users"\n}');
try {
  $response = $request->send();
  if ($response->getStatus() == 200) {
    echo $response->getBody();
  }
  else {
    echo 'Unexpected HTTP status: ' . $response->getStatus() . ' ' .
    $response->getReasonPhrase();
  }
}
catch(HTTP_Request2_Exception $e) {
  echo 'Error: ' . $e->getMessage();
}
```

```ruby
require "uri"
require "json"
require "net/http"

url = URI("{{apiPath}}/v1/environments/{{SourceEnvID}}/populations")

http = Net::HTTP.new(url.host, url.port);
request = Net::HTTP::Post.new(url)
request["Content-Type"] = "application/json"
request["Authorization"] = "Bearer {{accessToken}}"
request.body = JSON.dump({
  "name": "SourcePopulation_{{\$timestamp}}",
  "description": "Population for simple login users"
})

response = http.request(request)
puts response.read_body
```

```swift
let parameters = "{\n    \"name\": \"SourcePopulation_{{$timestamp}}\",\n    \"description\": \"Population for simple login users\"\n}"
let postData = parameters.data(using: .utf8)

var request = URLRequest(url: URL(string: "{{apiPath}}/v1/environments/{{SourceEnvID}}/populations")!,timeoutInterval: Double.infinity)
request.addValue("application/json", forHTTPHeaderField: "Content-Type")
request.addValue("Bearer {{accessToken}}", forHTTPHeaderField: "Authorization")

request.httpMethod = "POST"
request.httpBody = postData

let task = URLSession.shared.dataTask(with: request) { data, response, error in
  guard let data = data else {
    print(String(describing: error))
    return
  }
  print(String(data: data, encoding: .utf8)!)
}

task.resume()
```

### Example Response

201 Created

```json
{
    "_links": {
        "self": {
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/populations/030175e2-3122-48b1-b626-20f5dcbf1861"
        },
        "environment": {
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
        },
        "theme": {
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/themes/42ec7345-c220-4d1f-878a-bc16823c8ddd"
        }
    },
    "id": "030175e2-3122-48b1-b626-20f5dcbf1861",
    "environment": {
        "id": "abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
    },
    "name": "SourcePopulation_1776714509",
    "description": "Population for simple login users",
    "userCount": 0,
    "createdAt": "2026-04-20T19:48:29.633Z",
    "updatedAt": "2026-04-20T19:48:29.633Z",
    "default": false,
    "preferredLanguage": "en",
    "theme": {
        "id": "42ec7345-c220-4d1f-878a-bc16823c8ddd"
    }
}
```

---

---
title: "Step 1: Create a web application"
component: pingone-api
page_id: pingone-api:workflow-library:pingone-authorize/show-permissions-in-token/environment-configuration/step-1-create-a-web-application
canonical_url: https://developer.pingidentity.com/pingone-api/workflow-library/pingone-authorize/show-permissions-in-token/environment-configuration/step-1-create-a-web-application.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  headers: Headers
  body: Body
  example-request: Example Request
  example-response: Example Response
---

# Step 1: Create a web application

##

 

```none
POST {{apiPath}}/v1/environments/{{envID}}/applications
```

You can use the `POST {{apiPath}}/v1/environments/{{envID}}/applications` endpoint to create the new application. The application's `protocol` property is required, and in this example it specifies an `OPENID_CONNECT` application.

The response returns information about the new application, including its `id` property, which identifies the ID for this application resource. You will need the application's ID property value to get the application secret and to associate the sign-on policy with the application.

### Headers

Authorization      Bearer {{accessToken}}

Content-Type      application/json

### Body

raw ( application/json )

```json
{
    "enabled": true,
    "name": "CustomResourceApp_{{$timestamp}}",
    "description": "This is an OIDC Web application.",
    "type": "WEB_APP",
    "protocol": "OPENID_CONNECT",
    "grantTypes": [
        "AUTHORIZATION_CODE"
    ],
    "redirectUris": [
        "https://www.google.com"
    ],
    "responseTypes": [
        "CODE"
    ],
    "tokenEndpointAuthMethod": "CLIENT_SECRET_BASIC"
}
```

##

### Example Request

* cURL

* C#

* Go

* HTTP

* Java

* jQuery

* NodeJS

* Python

* PHP

* Ruby

* Swift

```shell
curl --location --globoff '{{apiPath}}/v1/environments/{{envID}}/applications' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {{accessToken}}' \
--data '{
    "enabled": true,
    "name": "CustomResourceApp_{{$timestamp}}",
    "description": "This is an OIDC Web application.",
    "type": "WEB_APP",
    "protocol": "OPENID_CONNECT",
    "grantTypes": [
        "AUTHORIZATION_CODE"
    ],
    "redirectUris": [
        "https://www.google.com"
    ],
    "responseTypes": [
        "CODE"
    ],
    "tokenEndpointAuthMethod": "CLIENT_SECRET_BASIC"
}'
```

```csharp
var options = new RestClientOptions("{{apiPath}}/v1/environments/{{envID}}/applications")
{
  MaxTimeout = -1,
};
var client = new RestClient(options);
var request = new RestRequest("", Method.Post);
request.AddHeader("Content-Type", "application/json");
request.AddHeader("Authorization", "Bearer {{accessToken}}");
var body = @"{" + "\n" +
@"    ""enabled"": true," + "\n" +
@"    ""name"": ""CustomResourceApp_{{$timestamp}}""," + "\n" +
@"    ""description"": ""This is an OIDC Web application.""," + "\n" +
@"    ""type"": ""WEB_APP""," + "\n" +
@"    ""protocol"": ""OPENID_CONNECT""," + "\n" +
@"    ""grantTypes"": [" + "\n" +
@"        ""AUTHORIZATION_CODE""" + "\n" +
@"    ]," + "\n" +
@"    ""redirectUris"": [" + "\n" +
@"        ""https://www.google.com""" + "\n" +
@"    ]," + "\n" +
@"    ""responseTypes"": [" + "\n" +
@"        ""CODE""" + "\n" +
@"    ]," + "\n" +
@"    ""tokenEndpointAuthMethod"": ""CLIENT_SECRET_BASIC""" + "\n" +
@"}";
request.AddStringBody(body, DataFormat.Json);
RestResponse response = await client.ExecuteAsync(request);
Console.WriteLine(response.Content);
```

```golang
package main

import (
  "fmt"
  "strings"
  "net/http"
  "io"
)

func main() {

  url := "{{apiPath}}/v1/environments/{{envID}}/applications"
  method := "POST"

  payload := strings.NewReader(`{
    "enabled": true,
    "name": "CustomResourceApp_{{$timestamp}}",
    "description": "This is an OIDC Web application.",
    "type": "WEB_APP",
    "protocol": "OPENID_CONNECT",
    "grantTypes": [
        "AUTHORIZATION_CODE"
    ],
    "redirectUris": [
        "https://www.google.com"
    ],
    "responseTypes": [
        "CODE"
    ],
    "tokenEndpointAuthMethod": "CLIENT_SECRET_BASIC"
}`)

  client := &http.Client {
  }
  req, err := http.NewRequest(method, url, payload)

  if err != nil {
    fmt.Println(err)
    return
  }
  req.Header.Add("Content-Type", "application/json")
  req.Header.Add("Authorization", "Bearer {{accessToken}}")

  res, err := client.Do(req)
  if err != nil {
    fmt.Println(err)
    return
  }
  defer res.Body.Close()

  body, err := io.ReadAll(res.Body)
  if err != nil {
    fmt.Println(err)
    return
  }
  fmt.Println(string(body))
}
```

```http
POST /v1/environments/{{envID}}/applications HTTP/1.1
Host: {{apiPath}}
Content-Type: application/json
Authorization: Bearer {{accessToken}}

{
    "enabled": true,
    "name": "CustomResourceApp_{{$timestamp}}",
    "description": "This is an OIDC Web application.",
    "type": "WEB_APP",
    "protocol": "OPENID_CONNECT",
    "grantTypes": [
        "AUTHORIZATION_CODE"
    ],
    "redirectUris": [
        "https://www.google.com"
    ],
    "responseTypes": [
        "CODE"
    ],
    "tokenEndpointAuthMethod": "CLIENT_SECRET_BASIC"
}
```

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("application/json");
RequestBody body = RequestBody.create(mediaType, "{\n    \"enabled\": true,\n    \"name\": \"CustomResourceApp_{{$timestamp}}\",\n    \"description\": \"This is an OIDC Web application.\",\n    \"type\": \"WEB_APP\",\n    \"protocol\": \"OPENID_CONNECT\",\n    \"grantTypes\": [\n        \"AUTHORIZATION_CODE\"\n    ],\n    \"redirectUris\": [\n        \"https://www.google.com\"\n    ],\n    \"responseTypes\": [\n        \"CODE\"\n    ],\n    \"tokenEndpointAuthMethod\": \"CLIENT_SECRET_BASIC\"\n}");
Request request = new Request.Builder()
  .url("{{apiPath}}/v1/environments/{{envID}}/applications")
  .method("POST", body)
  .addHeader("Content-Type", "application/json")
  .addHeader("Authorization", "Bearer {{accessToken}}")
  .build();
Response response = client.newCall(request).execute();
```

```javascript
var settings = {
  "url": "{{apiPath}}/v1/environments/{{envID}}/applications",
  "method": "POST",
  "timeout": 0,
  "headers": {
    "Content-Type": "application/json",
    "Authorization": "Bearer {{accessToken}}"
  },
  "data": JSON.stringify({
    "enabled": true,
    "name": "CustomResourceApp_{{$timestamp}}",
    "description": "This is an OIDC Web application.",
    "type": "WEB_APP",
    "protocol": "OPENID_CONNECT",
    "grantTypes": [
      "AUTHORIZATION_CODE"
    ],
    "redirectUris": [
      "https://www.google.com"
    ],
    "responseTypes": [
      "CODE"
    ],
    "tokenEndpointAuthMethod": "CLIENT_SECRET_BASIC"
  }),
};

$.ajax(settings).done(function (response) {
  console.log(response);
});
```

```javascript
var request = require('request');
var options = {
  'method': 'POST',
  'url': '{{apiPath}}/v1/environments/{{envID}}/applications',
  'headers': {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer {{accessToken}}'
  },
  body: JSON.stringify({
    "enabled": true,
    "name": "CustomResourceApp_{{$timestamp}}",
    "description": "This is an OIDC Web application.",
    "type": "WEB_APP",
    "protocol": "OPENID_CONNECT",
    "grantTypes": [
      "AUTHORIZATION_CODE"
    ],
    "redirectUris": [
      "https://www.google.com"
    ],
    "responseTypes": [
      "CODE"
    ],
    "tokenEndpointAuthMethod": "CLIENT_SECRET_BASIC"
  })

};
request(options, function (error, response) {
  if (error) throw new Error(error);
  console.log(response.body);
});
```

```python
import requests
import json

url = "{{apiPath}}/v1/environments/{{envID}}/applications"

payload = json.dumps({
  "enabled": True,
  "name": "CustomResourceApp_{{$timestamp}}",
  "description": "This is an OIDC Web application.",
  "type": "WEB_APP",
  "protocol": "OPENID_CONNECT",
  "grantTypes": [
    "AUTHORIZATION_CODE"
  ],
  "redirectUris": [
    "https://www.google.com"
  ],
  "responseTypes": [
    "CODE"
  ],
  "tokenEndpointAuthMethod": "CLIENT_SECRET_BASIC"
})
headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Bearer {{accessToken}}'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
```

```php
<?php
require_once 'HTTP/Request2.php';
$request = new HTTP_Request2();
$request->setUrl('{{apiPath}}/v1/environments/{{envID}}/applications');
$request->setMethod(HTTP_Request2::METHOD_POST);
$request->setConfig(array(
  'follow_redirects' => TRUE
));
$request->setHeader(array(
  'Content-Type' => 'application/json',
  'Authorization' => 'Bearer {{accessToken}}'
));
$request->setBody('{\n    "enabled": true,\n    "name": "CustomResourceApp_{{$timestamp}}",\n    "description": "This is an OIDC Web application.",\n    "type": "WEB_APP",\n    "protocol": "OPENID_CONNECT",\n    "grantTypes": [\n        "AUTHORIZATION_CODE"\n    ],\n    "redirectUris": [\n        "https://www.google.com"\n    ],\n    "responseTypes": [\n        "CODE"\n    ],\n    "tokenEndpointAuthMethod": "CLIENT_SECRET_BASIC"\n}');
try {
  $response = $request->send();
  if ($response->getStatus() == 200) {
    echo $response->getBody();
  }
  else {
    echo 'Unexpected HTTP status: ' . $response->getStatus() . ' ' .
    $response->getReasonPhrase();
  }
}
catch(HTTP_Request2_Exception $e) {
  echo 'Error: ' . $e->getMessage();
}
```

```ruby
require "uri"
require "json"
require "net/http"

url = URI("{{apiPath}}/v1/environments/{{envID}}/applications")

http = Net::HTTP.new(url.host, url.port);
request = Net::HTTP::Post.new(url)
request["Content-Type"] = "application/json"
request["Authorization"] = "Bearer {{accessToken}}"
request.body = JSON.dump({
  "enabled": true,
  "name": "CustomResourceApp_{{\$timestamp}}",
  "description": "This is an OIDC Web application.",
  "type": "WEB_APP",
  "protocol": "OPENID_CONNECT",
  "grantTypes": [
    "AUTHORIZATION_CODE"
  ],
  "redirectUris": [
    "https://www.google.com"
  ],
  "responseTypes": [
    "CODE"
  ],
  "tokenEndpointAuthMethod": "CLIENT_SECRET_BASIC"
})

response = http.request(request)
puts response.read_body
```

```swift
let parameters = "{\n    \"enabled\": true,\n    \"name\": \"CustomResourceApp_{{$timestamp}}\",\n    \"description\": \"This is an OIDC Web application.\",\n    \"type\": \"WEB_APP\",\n    \"protocol\": \"OPENID_CONNECT\",\n    \"grantTypes\": [\n        \"AUTHORIZATION_CODE\"\n    ],\n    \"redirectUris\": [\n        \"https://www.google.com\"\n    ],\n    \"responseTypes\": [\n        \"CODE\"\n    ],\n    \"tokenEndpointAuthMethod\": \"CLIENT_SECRET_BASIC\"\n}"
let postData = parameters.data(using: .utf8)

var request = URLRequest(url: URL(string: "{{apiPath}}/v1/environments/{{envID}}/applications")!,timeoutInterval: Double.infinity)
request.addValue("application/json", forHTTPHeaderField: "Content-Type")
request.addValue("Bearer {{accessToken}}", forHTTPHeaderField: "Authorization")

request.httpMethod = "POST"
request.httpBody = postData

let task = URLSession.shared.dataTask(with: request) { data, response, error in
  guard let data = data else {
    print(String(describing: error))
    return
  }
  print(String(data: data, encoding: .utf8)!)
}

task.resume()
```

### Example Response

201 Created

```json
{
    "_links": {
        "self": {
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/applications/9093ccb8-5079-46e7-99a4-48e9604659f6"
        },
        "environment": {
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
        },
        "metadata": {
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/applications/9093ccb8-5079-46e7-99a4-48e9604659f6/metadata"
        },
        "attributes": {
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/applications/9093ccb8-5079-46e7-99a4-48e9604659f6/attributes"
        },
        "secret": {
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/applications/9093ccb8-5079-46e7-99a4-48e9604659f6/secret"
        },
        "grants": {
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/applications/9093ccb8-5079-46e7-99a4-48e9604659f6/grants"
        },
        "keyRotationPolicy": {
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/keyRotationPolicies/1cb8d0b5-c7ba-42e8-a556-240ea2410f1d"
        }
    },
    "environment": {
        "id": "abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
    },
    "id": "9093ccb8-5079-46e7-99a4-48e9604659f6",
    "name": "CustomResourceApp_1776817799",
    "description": "This is an OIDC Web application.",
    "enabled": true,
    "hiddenFromAppPortal": false,
    "type": "WEB_APP",
    "protocol": "OPENID_CONNECT",
    "createdAt": "2026-04-22T00:29:59.348Z",
    "updatedAt": "2026-04-22T00:29:59.348Z",
    "clientId": "9093ccb8-5079-46e7-99a4-48e9604659f6",
    "assignActorRoles": false,
    "responseTypes": [
        "CODE"
    ],
    "pkceEnforcement": "OPTIONAL",
    "requestScopesForMultipleResourcesEnabled": false,
    "redirectUris": [
        "https://www.google.com"
    ],
    "deviceTimeout": 600,
    "grantTypes": [
        "AUTHORIZATION_CODE"
    ],
    "idpSignoff": false,
    "additionalRefreshTokenReplayProtectionEnabled": true,
    "tokenEndpointAuthMethod": "CLIENT_SECRET_BASIC",
    "parRequirement": "OPTIONAL",
    "devicePollingInterval": 5,
    "parTimeout": 60,
    "signing": {
        "keyRotationPolicy": {
            "id": "1cb8d0b5-c7ba-42e8-a556-240ea2410f1d"
        }
    }
}
```

---

---
title: "Step 1: Create a web application"
component: pingone-api
page_id: pingone-api:workflow-library:pingone-mfa/login-with-multifactor-authentication/environment-configuration/step-1-create-a-web-application
canonical_url: https://developer.pingidentity.com/pingone-api/workflow-library/pingone-mfa/login-with-multifactor-authentication/environment-configuration/step-1-create-a-web-application.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  headers: Headers
  body: Body
  example-request: Example Request
  example-response: Example Response
---

# Step 1: Create a web application

##

 

```none
POST {{apiPath}}/v1/environments/{{envID}}/applications
```

You can use the `POST {{apiPath}}/v1/environments/{{envID}}/applications` endpoint to create the new application. The application's `protocol` property is required, and in this example it specifies an `OPENID_CONNECT` application.

The response returns information about the new application, including its `id` property, which identifies the ID for this application resource. You will need the application's ID property value to get the application secret and to associate the sign-on policy with the application.

### Headers

Authorization      Bearer {{accessToken}}

Content-Type      application/json

### Body

raw ( application/json )

```json
{
    "enabled": true,
    "name": "WebAppWithMFA_{{$timestamp}}",
    "description": "This is an OIDC Web application.",
    "type": "WEB_APP",
    "protocol": "OPENID_CONNECT",
    "grantTypes": [
        "AUTHORIZATION_CODE"
    ],
    "redirectUris": [
        "https://www.google.com"
    ],
    "responseTypes": [
        "CODE"
    ],
    "tokenEndpointAuthMethod": "CLIENT_SECRET_BASIC"
}
```

##

### Example Request

* cURL

* C#

* Go

* HTTP

* Java

* jQuery

* NodeJS

* Python

* PHP

* Ruby

* Swift

```shell
curl --location --globoff '{{apiPath}}/v1/environments/{{envID}}/applications' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {{accessToken}}' \
--data '{
    "enabled": true,
    "name": "WebAppWithMFA_{{$timestamp}}",
    "description": "This is an OIDC Web application.",
    "type": "WEB_APP",
    "protocol": "OPENID_CONNECT",
    "grantTypes": [
        "AUTHORIZATION_CODE"
    ],
    "redirectUris": [
        "https://www.google.com"
    ],
    "responseTypes": [
        "CODE"
    ],
    "tokenEndpointAuthMethod": "CLIENT_SECRET_BASIC"
}'
```

```csharp
var options = new RestClientOptions("{{apiPath}}/v1/environments/{{envID}}/applications")
{
  MaxTimeout = -1,
};
var client = new RestClient(options);
var request = new RestRequest("", Method.Post);
request.AddHeader("Content-Type", "application/json");
request.AddHeader("Authorization", "Bearer {{accessToken}}");
var body = @"{" + "\n" +
@"    ""enabled"": true," + "\n" +
@"    ""name"": ""WebAppWithMFA_{{$timestamp}}""," + "\n" +
@"    ""description"": ""This is an OIDC Web application.""," + "\n" +
@"    ""type"": ""WEB_APP""," + "\n" +
@"    ""protocol"": ""OPENID_CONNECT""," + "\n" +
@"    ""grantTypes"": [" + "\n" +
@"        ""AUTHORIZATION_CODE""" + "\n" +
@"    ]," + "\n" +
@"    ""redirectUris"": [" + "\n" +
@"        ""https://www.google.com""" + "\n" +
@"    ]," + "\n" +
@"    ""responseTypes"": [" + "\n" +
@"        ""CODE""" + "\n" +
@"    ]," + "\n" +
@"    ""tokenEndpointAuthMethod"": ""CLIENT_SECRET_BASIC""" + "\n" +
@"}";
request.AddStringBody(body, DataFormat.Json);
RestResponse response = await client.ExecuteAsync(request);
Console.WriteLine(response.Content);
```

```golang
package main

import (
  "fmt"
  "strings"
  "net/http"
  "io"
)

func main() {

  url := "{{apiPath}}/v1/environments/{{envID}}/applications"
  method := "POST"

  payload := strings.NewReader(`{
    "enabled": true,
    "name": "WebAppWithMFA_{{$timestamp}}",
    "description": "This is an OIDC Web application.",
    "type": "WEB_APP",
    "protocol": "OPENID_CONNECT",
    "grantTypes": [
        "AUTHORIZATION_CODE"
    ],
    "redirectUris": [
        "https://www.google.com"
    ],
    "responseTypes": [
        "CODE"
    ],
    "tokenEndpointAuthMethod": "CLIENT_SECRET_BASIC"
}`)

  client := &http.Client {
  }
  req, err := http.NewRequest(method, url, payload)

  if err != nil {
    fmt.Println(err)
    return
  }
  req.Header.Add("Content-Type", "application/json")
  req.Header.Add("Authorization", "Bearer {{accessToken}}")

  res, err := client.Do(req)
  if err != nil {
    fmt.Println(err)
    return
  }
  defer res.Body.Close()

  body, err := io.ReadAll(res.Body)
  if err != nil {
    fmt.Println(err)
    return
  }
  fmt.Println(string(body))
}
```

```http
POST /v1/environments/{{envID}}/applications HTTP/1.1
Host: {{apiPath}}
Content-Type: application/json
Authorization: Bearer {{accessToken}}

{
    "enabled": true,
    "name": "WebAppWithMFA_{{$timestamp}}",
    "description": "This is an OIDC Web application.",
    "type": "WEB_APP",
    "protocol": "OPENID_CONNECT",
    "grantTypes": [
        "AUTHORIZATION_CODE"
    ],
    "redirectUris": [
        "https://www.google.com"
    ],
    "responseTypes": [
        "CODE"
    ],
    "tokenEndpointAuthMethod": "CLIENT_SECRET_BASIC"
}
```

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("application/json");
RequestBody body = RequestBody.create(mediaType, "{\n    \"enabled\": true,\n    \"name\": \"WebAppWithMFA_{{$timestamp}}\",\n    \"description\": \"This is an OIDC Web application.\",\n    \"type\": \"WEB_APP\",\n    \"protocol\": \"OPENID_CONNECT\",\n    \"grantTypes\": [\n        \"AUTHORIZATION_CODE\"\n    ],\n    \"redirectUris\": [\n        \"https://www.google.com\"\n    ],\n    \"responseTypes\": [\n        \"CODE\"\n    ],\n    \"tokenEndpointAuthMethod\": \"CLIENT_SECRET_BASIC\"\n}");
Request request = new Request.Builder()
  .url("{{apiPath}}/v1/environments/{{envID}}/applications")
  .method("POST", body)
  .addHeader("Content-Type", "application/json")
  .addHeader("Authorization", "Bearer {{accessToken}}")
  .build();
Response response = client.newCall(request).execute();
```

```javascript
var settings = {
  "url": "{{apiPath}}/v1/environments/{{envID}}/applications",
  "method": "POST",
  "timeout": 0,
  "headers": {
    "Content-Type": "application/json",
    "Authorization": "Bearer {{accessToken}}"
  },
  "data": JSON.stringify({
    "enabled": true,
    "name": "WebAppWithMFA_{{$timestamp}}",
    "description": "This is an OIDC Web application.",
    "type": "WEB_APP",
    "protocol": "OPENID_CONNECT",
    "grantTypes": [
      "AUTHORIZATION_CODE"
    ],
    "redirectUris": [
      "https://www.google.com"
    ],
    "responseTypes": [
      "CODE"
    ],
    "tokenEndpointAuthMethod": "CLIENT_SECRET_BASIC"
  }),
};

$.ajax(settings).done(function (response) {
  console.log(response);
});
```

```javascript
var request = require('request');
var options = {
  'method': 'POST',
  'url': '{{apiPath}}/v1/environments/{{envID}}/applications',
  'headers': {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer {{accessToken}}'
  },
  body: JSON.stringify({
    "enabled": true,
    "name": "WebAppWithMFA_{{$timestamp}}",
    "description": "This is an OIDC Web application.",
    "type": "WEB_APP",
    "protocol": "OPENID_CONNECT",
    "grantTypes": [
      "AUTHORIZATION_CODE"
    ],
    "redirectUris": [
      "https://www.google.com"
    ],
    "responseTypes": [
      "CODE"
    ],
    "tokenEndpointAuthMethod": "CLIENT_SECRET_BASIC"
  })

};
request(options, function (error, response) {
  if (error) throw new Error(error);
  console.log(response.body);
});
```

```python
import requests
import json

url = "{{apiPath}}/v1/environments/{{envID}}/applications"

payload = json.dumps({
  "enabled": True,
  "name": "WebAppWithMFA_{{$timestamp}}",
  "description": "This is an OIDC Web application.",
  "type": "WEB_APP",
  "protocol": "OPENID_CONNECT",
  "grantTypes": [
    "AUTHORIZATION_CODE"
  ],
  "redirectUris": [
    "https://www.google.com"
  ],
  "responseTypes": [
    "CODE"
  ],
  "tokenEndpointAuthMethod": "CLIENT_SECRET_BASIC"
})
headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Bearer {{accessToken}}'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
```

```php
<?php
require_once 'HTTP/Request2.php';
$request = new HTTP_Request2();
$request->setUrl('{{apiPath}}/v1/environments/{{envID}}/applications');
$request->setMethod(HTTP_Request2::METHOD_POST);
$request->setConfig(array(
  'follow_redirects' => TRUE
));
$request->setHeader(array(
  'Content-Type' => 'application/json',
  'Authorization' => 'Bearer {{accessToken}}'
));
$request->setBody('{\n    "enabled": true,\n    "name": "WebAppWithMFA_{{$timestamp}}",\n    "description": "This is an OIDC Web application.",\n    "type": "WEB_APP",\n    "protocol": "OPENID_CONNECT",\n    "grantTypes": [\n        "AUTHORIZATION_CODE"\n    ],\n    "redirectUris": [\n        "https://www.google.com"\n    ],\n    "responseTypes": [\n        "CODE"\n    ],\n    "tokenEndpointAuthMethod": "CLIENT_SECRET_BASIC"\n}');
try {
  $response = $request->send();
  if ($response->getStatus() == 200) {
    echo $response->getBody();
  }
  else {
    echo 'Unexpected HTTP status: ' . $response->getStatus() . ' ' .
    $response->getReasonPhrase();
  }
}
catch(HTTP_Request2_Exception $e) {
  echo 'Error: ' . $e->getMessage();
}
```

```ruby
require "uri"
require "json"
require "net/http"

url = URI("{{apiPath}}/v1/environments/{{envID}}/applications")

http = Net::HTTP.new(url.host, url.port);
request = Net::HTTP::Post.new(url)
request["Content-Type"] = "application/json"
request["Authorization"] = "Bearer {{accessToken}}"
request.body = JSON.dump({
  "enabled": true,
  "name": "WebAppWithMFA_{{\$timestamp}}",
  "description": "This is an OIDC Web application.",
  "type": "WEB_APP",
  "protocol": "OPENID_CONNECT",
  "grantTypes": [
    "AUTHORIZATION_CODE"
  ],
  "redirectUris": [
    "https://www.google.com"
  ],
  "responseTypes": [
    "CODE"
  ],
  "tokenEndpointAuthMethod": "CLIENT_SECRET_BASIC"
})

response = http.request(request)
puts response.read_body
```

```swift
let parameters = "{\n    \"enabled\": true,\n    \"name\": \"WebAppWithMFA_{{$timestamp}}\",\n    \"description\": \"This is an OIDC Web application.\",\n    \"type\": \"WEB_APP\",\n    \"protocol\": \"OPENID_CONNECT\",\n    \"grantTypes\": [\n        \"AUTHORIZATION_CODE\"\n    ],\n    \"redirectUris\": [\n        \"https://www.google.com\"\n    ],\n    \"responseTypes\": [\n        \"CODE\"\n    ],\n    \"tokenEndpointAuthMethod\": \"CLIENT_SECRET_BASIC\"\n}"
let postData = parameters.data(using: .utf8)

var request = URLRequest(url: URL(string: "{{apiPath}}/v1/environments/{{envID}}/applications")!,timeoutInterval: Double.infinity)
request.addValue("application/json", forHTTPHeaderField: "Content-Type")
request.addValue("Bearer {{accessToken}}", forHTTPHeaderField: "Authorization")

request.httpMethod = "POST"
request.httpBody = postData

let task = URLSession.shared.dataTask(with: request) { data, response, error in
  guard let data = data else {
    print(String(describing: error))
    return
  }
  print(String(data: data, encoding: .utf8)!)
}

task.resume()
```

### Example Response

201 Created

```json
{
    "_links": {
        "self": {
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/applications/633d1e1a-e492-4f93-80e8-a76dcf323e82"
        },
        "environment": {
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
        },
        "metadata": {
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/applications/633d1e1a-e492-4f93-80e8-a76dcf323e82/metadata"
        },
        "attributes": {
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/applications/633d1e1a-e492-4f93-80e8-a76dcf323e82/attributes"
        },
        "secret": {
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/applications/633d1e1a-e492-4f93-80e8-a76dcf323e82/secret"
        },
        "grants": {
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/applications/633d1e1a-e492-4f93-80e8-a76dcf323e82/grants"
        },
        "keyRotationPolicy": {
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/keyRotationPolicies/1cb8d0b5-c7ba-42e8-a556-240ea2410f1d"
        }
    },
    "environment": {
        "id": "abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
    },
    "id": "633d1e1a-e492-4f93-80e8-a76dcf323e82",
    "name": "WebAppWithMFA_1776884203",
    "description": "This is an OIDC Web application.",
    "enabled": true,
    "hiddenFromAppPortal": false,
    "type": "WEB_APP",
    "protocol": "OPENID_CONNECT",
    "createdAt": "2026-04-22T18:56:43.197Z",
    "updatedAt": "2026-04-22T18:56:43.197Z",
    "clientId": "633d1e1a-e492-4f93-80e8-a76dcf323e82",
    "assignActorRoles": false,
    "responseTypes": [
        "CODE"
    ],
    "pkceEnforcement": "OPTIONAL",
    "requestScopesForMultipleResourcesEnabled": false,
    "redirectUris": [
        "https://www.google.com"
    ],
    "deviceTimeout": 600,
    "grantTypes": [
        "AUTHORIZATION_CODE"
    ],
    "idpSignoff": false,
    "additionalRefreshTokenReplayProtectionEnabled": true,
    "tokenEndpointAuthMethod": "CLIENT_SECRET_BASIC",
    "parRequirement": "OPTIONAL",
    "devicePollingInterval": 5,
    "parTimeout": 60,
    "signing": {
        "keyRotationPolicy": {
            "id": "1cb8d0b5-c7ba-42e8-a556-240ea2410f1d"
        }
    }
}
```