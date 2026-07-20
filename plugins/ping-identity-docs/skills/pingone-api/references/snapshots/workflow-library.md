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
title: Downloading PingOne use case collections
description: Client Authentication Methods
component: pingone-api
page_id: pingone-api:workflow-library:downloading-pingone-workflow-collections
canonical_url: https://developer.pingidentity.com/pingone-api/workflow-library/downloading-pingone-workflow-collections.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  using-the-pingone-postman-environment: Using the PingOne Postman environment
---

# Downloading PingOne use case collections

| Use Case                                                                                                                                    | Retrieve                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| ------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [Client Authentication Methods](platform-sso-and-authorization/openid-connect-oidc/client-authentication-methods.html)                      | [Run in Postman](https://god.gw.postman.com/run-collection/18568624-4e4e5063-6ad7-4895-805e-ada77358488c?action=collection%2Ffork\&source=rip_markdown\&collection-url=entityId%3D18568624-4e4e5063-6ad7-4895-805e-ada77358488c%26entityType%3Dcollection%26workspaceId%3D3550b170-7818-4801-b1eb-dcb7b3f64263#?env%5BPingOne%20Workflow%20Library%20Template%20%28release%3A%202025-04-17%29%5D=W3sia2V5IjoidGxkIiwidmFsdWUiOiJjb20iLCJlbmFibGVkIjp0cnVlLCJ0eXBlIjoiZGVmYXVsdCJ9LHsia2V5IjoiYXV0aFBhdGgiLCJ2YWx1ZSI6Imh0dHBzOi8vYXV0aC5waW5nb25lLnt7dGxkfX0iLCJlbmFibGVkIjp0cnVlLCJ0eXBlIjoiZGVmYXVsdCJ9LHsia2V5IjoiYXBpUGF0aCIsInZhbHVlIjoiaHR0cHM6Ly9hcGkucGluZ29uZS57e3RsZH19L3YxIiwiZW5hYmxlZCI6dHJ1ZSwidHlwZSI6ImRlZmF1bHQifSx7ImtleSI6ImFkbWluRW52SUQiLCJ2YWx1ZSI6IiIsImVuYWJsZWQiOnRydWUsInR5cGUiOiJkZWZhdWx0In0seyJrZXkiOiJhZG1pbkFwcElEIiwidmFsdWUiOiIiLCJlbmFibGVkIjp0cnVlLCJ0eXBlIjoiZGVmYXVsdCJ9LHsia2V5IjoiYWRtaW5BcHBTZWNyZXQiLCJ2YWx1ZSI6IiIsImVuYWJsZWQiOnRydWUsInR5cGUiOiJkZWZhdWx0In0seyJrZXkiOiJlbnZJRCIsInZhbHVlIjoiIiwiZW5hYmxlZCI6dHJ1ZSwidHlwZSI6ImRlZmF1bHQifV0=) |
| [Create a Group and Add a User](platform-sso-and-authorization/groups/create-a-group-and-add-a-user.html)                                   | [Run in Postman](https://god.gw.postman.com/run-collection/18568624-e8c1ce22-1a4e-4328-a3b1-e43146b5b932?action=collection%2Ffork\&source=rip_markdown\&collection-url=entityId%3D18568624-e8c1ce22-1a4e-4328-a3b1-e43146b5b932%26entityType%3Dcollection%26workspaceId%3D3550b170-7818-4801-b1eb-dcb7b3f64263#?env%5BPingOne%20Workflow%20Library%20Template%20%28release%3A%202025-04-17%29%5D=W3sia2V5IjoidGxkIiwidmFsdWUiOiJjb20iLCJlbmFibGVkIjp0cnVlLCJ0eXBlIjoiZGVmYXVsdCJ9LHsia2V5IjoiYXV0aFBhdGgiLCJ2YWx1ZSI6Imh0dHBzOi8vYXV0aC5waW5nb25lLnt7dGxkfX0iLCJlbmFibGVkIjp0cnVlLCJ0eXBlIjoiZGVmYXVsdCJ9LHsia2V5IjoiYXBpUGF0aCIsInZhbHVlIjoiaHR0cHM6Ly9hcGkucGluZ29uZS57e3RsZH19L3YxIiwiZW5hYmxlZCI6dHJ1ZSwidHlwZSI6ImRlZmF1bHQifSx7ImtleSI6ImFkbWluRW52SUQiLCJ2YWx1ZSI6IiIsImVuYWJsZWQiOnRydWUsInR5cGUiOiJkZWZhdWx0In0seyJrZXkiOiJhZG1pbkFwcElEIiwidmFsdWUiOiIiLCJlbmFibGVkIjp0cnVlLCJ0eXBlIjoiZGVmYXVsdCJ9LHsia2V5IjoiYWRtaW5BcHBTZWNyZXQiLCJ2YWx1ZSI6IiIsImVuYWJsZWQiOnRydWUsInR5cGUiOiJkZWZhdWx0In0seyJrZXkiOiJlbnZJRCIsInZhbHVlIjoiIiwiZW5hYmxlZCI6dHJ1ZSwidHlwZSI6ImRlZmF1bHQifV0=) |
| [Create a Risk Evaluation](pingone-protect/create-a-risk-evaluation.html)                                                                   | [Run in Postman](https://god.gw.postman.com/run-collection/18568624-2fb495d2-2a93-4768-bb4f-35b7010853f6?action=collection%2Ffork\&source=rip_markdown\&collection-url=entityId%3D18568624-2fb495d2-2a93-4768-bb4f-35b7010853f6%26entityType%3Dcollection%26workspaceId%3D3550b170-7818-4801-b1eb-dcb7b3f64263#?env%5BPingOne%20Workflow%20Library%20Template%20%28release%3A%202025-04-17%29%5D=W3sia2V5IjoidGxkIiwidmFsdWUiOiJjb20iLCJlbmFibGVkIjp0cnVlLCJ0eXBlIjoiZGVmYXVsdCJ9LHsia2V5IjoiYXV0aFBhdGgiLCJ2YWx1ZSI6Imh0dHBzOi8vYXV0aC5waW5nb25lLnt7dGxkfX0iLCJlbmFibGVkIjp0cnVlLCJ0eXBlIjoiZGVmYXVsdCJ9LHsia2V5IjoiYXBpUGF0aCIsInZhbHVlIjoiaHR0cHM6Ly9hcGkucGluZ29uZS57e3RsZH19L3YxIiwiZW5hYmxlZCI6dHJ1ZSwidHlwZSI6ImRlZmF1bHQifSx7ImtleSI6ImFkbWluRW52SUQiLCJ2YWx1ZSI6IiIsImVuYWJsZWQiOnRydWUsInR5cGUiOiJkZWZhdWx0In0seyJrZXkiOiJhZG1pbkFwcElEIiwidmFsdWUiOiIiLCJlbmFibGVkIjp0cnVlLCJ0eXBlIjoiZGVmYXVsdCJ9LHsia2V5IjoiYWRtaW5BcHBTZWNyZXQiLCJ2YWx1ZSI6IiIsImVuYWJsZWQiOnRydWUsInR5cGUiOiJkZWZhdWx0In0seyJrZXkiOiJlbnZJRCIsInZhbHVlIjoiIiwiZW5hYmxlZCI6dHJ1ZSwidHlwZSI6ImRlZmF1bHQifV0=) |
| [Create a Risk Policy Set](pingone-protect/create-a-risk-policy-set.html)                                                                   | [Run in Postman](https://god.gw.postman.com/run-collection/18568624-4bb35659-b63c-46f9-95e1-69f6d126aa00?action=collection%2Ffork\&source=rip_markdown\&collection-url=entityId%3D18568624-4bb35659-b63c-46f9-95e1-69f6d126aa00%26entityType%3Dcollection%26workspaceId%3D3550b170-7818-4801-b1eb-dcb7b3f64263#?env%5BPingOne%20Workflow%20Library%20Template%20%28release%3A%202025-04-17%29%5D=W3sia2V5IjoidGxkIiwidmFsdWUiOiJjb20iLCJlbmFibGVkIjp0cnVlLCJ0eXBlIjoiZGVmYXVsdCJ9LHsia2V5IjoiYXV0aFBhdGgiLCJ2YWx1ZSI6Imh0dHBzOi8vYXV0aC5waW5nb25lLnt7dGxkfX0iLCJlbmFibGVkIjp0cnVlLCJ0eXBlIjoiZGVmYXVsdCJ9LHsia2V5IjoiYXBpUGF0aCIsInZhbHVlIjoiaHR0cHM6Ly9hcGkucGluZ29uZS57e3RsZH19L3YxIiwiZW5hYmxlZCI6dHJ1ZSwidHlwZSI6ImRlZmF1bHQifSx7ImtleSI6ImFkbWluRW52SUQiLCJ2YWx1ZSI6IiIsImVuYWJsZWQiOnRydWUsInR5cGUiOiJkZWZhdWx0In0seyJrZXkiOiJhZG1pbkFwcElEIiwidmFsdWUiOiIiLCJlbmFibGVkIjp0cnVlLCJ0eXBlIjoiZGVmYXVsdCJ9LHsia2V5IjoiYWRtaW5BcHBTZWNyZXQiLCJ2YWx1ZSI6IiIsImVuYWJsZWQiOnRydWUsInR5cGUiOiJkZWZhdWx0In0seyJrZXkiOiJlbnZJRCIsInZhbHVlIjoiIiwiZW5hYmxlZCI6dHJ1ZSwidHlwZSI6ImRlZmF1bHQifV0=) |
| [Create a Workday Propagation Connection](platform-sso-and-authorization/identity-propagation/create-a-workday-propagation-connection.html) | [Run in Postman](https://god.gw.postman.com/run-collection/18568624-2d38766f-1c22-4eae-bf2c-509f4f71bd08?action=collection%2Ffork\&source=rip_markdown\&collection-url=entityId%3D18568624-2d38766f-1c22-4eae-bf2c-509f4f71bd08%26entityType%3Dcollection%26workspaceId%3D3550b170-7818-4801-b1eb-dcb7b3f64263#?env%5BPingOne%20Workflow%20Library%20Template%20%28release%3A%202025-04-17%29%5D=W3sia2V5IjoidGxkIiwidmFsdWUiOiJjb20iLCJlbmFibGVkIjp0cnVlLCJ0eXBlIjoiZGVmYXVsdCJ9LHsia2V5IjoiYXV0aFBhdGgiLCJ2YWx1ZSI6Imh0dHBzOi8vYXV0aC5waW5nb25lLnt7dGxkfX0iLCJlbmFibGVkIjp0cnVlLCJ0eXBlIjoiZGVmYXVsdCJ9LHsia2V5IjoiYXBpUGF0aCIsInZhbHVlIjoiaHR0cHM6Ly9hcGkucGluZ29uZS57e3RsZH19L3YxIiwiZW5hYmxlZCI6dHJ1ZSwidHlwZSI6ImRlZmF1bHQifSx7ImtleSI6ImFkbWluRW52SUQiLCJ2YWx1ZSI6IiIsImVuYWJsZWQiOnRydWUsInR5cGUiOiJkZWZhdWx0In0seyJrZXkiOiJhZG1pbkFwcElEIiwidmFsdWUiOiIiLCJlbmFibGVkIjp0cnVlLCJ0eXBlIjoiZGVmYXVsdCJ9LHsia2V5IjoiYWRtaW5BcHBTZWNyZXQiLCJ2YWx1ZSI6IiIsImVuYWJsZWQiOnRydWUsInR5cGUiOiJkZWZhdWx0In0seyJrZXkiOiJlbnZJRCIsInZhbHVlIjoiIiwiZW5hYmxlZCI6dHJ1ZSwidHlwZSI6ImRlZmF1bHQifV0=) |
| [DaVinci Registration Flow with PingOne Auth](pingone-davinci/davinci-registration-flow-with-pingone-auth.html)                             | [Run in Postman](https://god.gw.postman.com/run-collection/18568624-eec93681-1392-417d-a126-9c2ea7875c04?action=collection%2Ffork\&source=rip_markdown\&collection-url=entityId%3D18568624-eec93681-1392-417d-a126-9c2ea7875c04%26entityType%3Dcollection%26workspaceId%3D3550b170-7818-4801-b1eb-dcb7b3f64263#?env%5BPingOne%20Workflow%20Library%20Template%20%28release%3A%202025-04-17%29%5D=W3sia2V5IjoidGxkIiwidmFsdWUiOiJjb20iLCJlbmFibGVkIjp0cnVlLCJ0eXBlIjoiZGVmYXVsdCJ9LHsia2V5IjoiYXV0aFBhdGgiLCJ2YWx1ZSI6Imh0dHBzOi8vYXV0aC5waW5nb25lLnt7dGxkfX0iLCJlbmFibGVkIjp0cnVlLCJ0eXBlIjoiZGVmYXVsdCJ9LHsia2V5IjoiYXBpUGF0aCIsInZhbHVlIjoiaHR0cHM6Ly9hcGkucGluZ29uZS57e3RsZH19L3YxIiwiZW5hYmxlZCI6dHJ1ZSwidHlwZSI6ImRlZmF1bHQifSx7ImtleSI6ImFkbWluRW52SUQiLCJ2YWx1ZSI6IiIsImVuYWJsZWQiOnRydWUsInR5cGUiOiJkZWZhdWx0In0seyJrZXkiOiJhZG1pbkFwcElEIiwidmFsdWUiOiIiLCJlbmFibGVkIjp0cnVlLCJ0eXBlIjoiZGVmYXVsdCJ9LHsia2V5IjoiYWRtaW5BcHBTZWNyZXQiLCJ2YWx1ZSI6IiIsImVuYWJsZWQiOnRydWUsInR5cGUiOiJkZWZhdWx0In0seyJrZXkiOiJlbnZJRCIsInZhbHVlIjoiIiwiZW5hYmxlZCI6dHJ1ZSwidHlwZSI6ImRlZmF1bHQifV0=) |
| [DaVinci Sign-On Flow with PingOne Auth](pingone-davinci/davinci-sign-on-flow-with-pingone-auth.html)                                       | [Run in Postman](https://god.gw.postman.com/run-collection/18568624-ea2ad46c-a92a-44b2-9318-42f02fb165f8?action=collection%2Ffork\&source=rip_markdown\&collection-url=entityId%3D18568624-ea2ad46c-a92a-44b2-9318-42f02fb165f8%26entityType%3Dcollection%26workspaceId%3D3550b170-7818-4801-b1eb-dcb7b3f64263#?env%5BPingOne%20Workflow%20Library%20Template%20%28release%3A%202025-04-17%29%5D=W3sia2V5IjoidGxkIiwidmFsdWUiOiJjb20iLCJlbmFibGVkIjp0cnVlLCJ0eXBlIjoiZGVmYXVsdCJ9LHsia2V5IjoiYXV0aFBhdGgiLCJ2YWx1ZSI6Imh0dHBzOi8vYXV0aC5waW5nb25lLnt7dGxkfX0iLCJlbmFibGVkIjp0cnVlLCJ0eXBlIjoiZGVmYXVsdCJ9LHsia2V5IjoiYXBpUGF0aCIsInZhbHVlIjoiaHR0cHM6Ly9hcGkucGluZ29uZS57e3RsZH19L3YxIiwiZW5hYmxlZCI6dHJ1ZSwidHlwZSI6ImRlZmF1bHQifSx7ImtleSI6ImFkbWluRW52SUQiLCJ2YWx1ZSI6IiIsImVuYWJsZWQiOnRydWUsInR5cGUiOiJkZWZhdWx0In0seyJrZXkiOiJhZG1pbkFwcElEIiwidmFsdWUiOiIiLCJlbmFibGVkIjp0cnVlLCJ0eXBlIjoiZGVmYXVsdCJ9LHsia2V5IjoiYWRtaW5BcHBTZWNyZXQiLCJ2YWx1ZSI6IiIsImVuYWJsZWQiOnRydWUsInR5cGUiOiJkZWZhdWx0In0seyJrZXkiOiJlbnZJRCIsInZhbHVlIjoiIiwiZW5hYmxlZCI6dHJ1ZSwidHlwZSI6ImRlZmF1bHQifV0=) |
| [Device Authorization Grant Flow](platform-sso-and-authorization/openid-connect-oidc/device-authorization-grant-flow.html)                  | [Run in Postman](https://god.gw.postman.com/run-collection/18568624-08fad81d-7266-4f54-aa43-803c5f6e96c8?action=collection%2Ffork\&source=rip_markdown\&collection-url=entityId%3D18568624-08fad81d-7266-4f54-aa43-803c5f6e96c8%26entityType%3Dcollection%26workspaceId%3D3550b170-7818-4801-b1eb-dcb7b3f64263#?env%5BPingOne%20Workflow%20Library%20Template%20%28release%3A%202025-04-17%29%5D=W3sia2V5IjoidGxkIiwidmFsdWUiOiJjb20iLCJlbmFibGVkIjp0cnVlLCJ0eXBlIjoiZGVmYXVsdCJ9LHsia2V5IjoiYXV0aFBhdGgiLCJ2YWx1ZSI6Imh0dHBzOi8vYXV0aC5waW5nb25lLnt7dGxkfX0iLCJlbmFibGVkIjp0cnVlLCJ0eXBlIjoiZGVmYXVsdCJ9LHsia2V5IjoiYXBpUGF0aCIsInZhbHVlIjoiaHR0cHM6Ly9hcGkucGluZ29uZS57e3RsZH19L3YxIiwiZW5hYmxlZCI6dHJ1ZSwidHlwZSI6ImRlZmF1bHQifSx7ImtleSI6ImFkbWluRW52SUQiLCJ2YWx1ZSI6IiIsImVuYWJsZWQiOnRydWUsInR5cGUiOiJkZWZhdWx0In0seyJrZXkiOiJhZG1pbkFwcElEIiwidmFsdWUiOiIiLCJlbmFibGVkIjp0cnVlLCJ0eXBlIjoiZGVmYXVsdCJ9LHsia2V5IjoiYWRtaW5BcHBTZWNyZXQiLCJ2YWx1ZSI6IiIsImVuYWJsZWQiOnRydWUsInR5cGUiOiJkZWZhdWx0In0seyJrZXkiOiJlbnZJRCIsInZhbHVlIjoiIiwiZW5hYmxlZCI6dHJ1ZSwidHlwZSI6ImRlZmF1bHQifV0=) |
| [External Identity Provider - Sign On](platform-sso-and-authorization/openid-connect-oidc/external-identity-provider-sign-on.html)          | [Run in Postman](https://god.gw.postman.com/run-collection/18568624-2d238da4-4c7c-4b09-b17d-d9f127fb3e58?action=collection%2Ffork\&source=rip_markdown\&collection-url=entityId%3D18568624-2d238da4-4c7c-4b09-b17d-d9f127fb3e58%26entityType%3Dcollection%26workspaceId%3D3550b170-7818-4801-b1eb-dcb7b3f64263#?env%5BPingOne%20Workflow%20Library%20Template%20%28release%3A%202025-04-17%29%5D=W3sia2V5IjoidGxkIiwidmFsdWUiOiJjb20iLCJlbmFibGVkIjp0cnVlLCJ0eXBlIjoiZGVmYXVsdCJ9LHsia2V5IjoiYXV0aFBhdGgiLCJ2YWx1ZSI6Imh0dHBzOi8vYXV0aC5waW5nb25lLnt7dGxkfX0iLCJlbmFibGVkIjp0cnVlLCJ0eXBlIjoiZGVmYXVsdCJ9LHsia2V5IjoiYXBpUGF0aCIsInZhbHVlIjoiaHR0cHM6Ly9hcGkucGluZ29uZS57e3RsZH19L3YxIiwiZW5hYmxlZCI6dHJ1ZSwidHlwZSI6ImRlZmF1bHQifSx7ImtleSI6ImFkbWluRW52SUQiLCJ2YWx1ZSI6IiIsImVuYWJsZWQiOnRydWUsInR5cGUiOiJkZWZhdWx0In0seyJrZXkiOiJhZG1pbkFwcElEIiwidmFsdWUiOiIiLCJlbmFibGVkIjp0cnVlLCJ0eXBlIjoiZGVmYXVsdCJ9LHsia2V5IjoiYWRtaW5BcHBTZWNyZXQiLCJ2YWx1ZSI6IiIsImVuYWJsZWQiOnRydWUsInR5cGUiOiJkZWZhdWx0In0seyJrZXkiOiJlbnZJRCIsInZhbHVlIjoiIiwiZW5hYmxlZCI6dHJ1ZSwidHlwZSI6ImRlZmF1bHQifV0=) |
| [Find and Terminate a User Session](platform-sso-and-authorization/sessions-and-logout/find-and-terminate-a-user-session.html)              | [Run in Postman](https://god.gw.postman.com/run-collection/18568624-545436b9-d443-440a-a9b7-8cf1c3605810?action=collection%2Ffork\&source=rip_markdown\&collection-url=entityId%3D18568624-545436b9-d443-440a-a9b7-8cf1c3605810%26entityType%3Dcollection%26workspaceId%3D3550b170-7818-4801-b1eb-dcb7b3f64263#?env%5BPingOne%20Workflow%20Library%20Template%20%28release%3A%202025-04-17%29%5D=W3sia2V5IjoidGxkIiwidmFsdWUiOiJjb20iLCJlbmFibGVkIjp0cnVlLCJ0eXBlIjoiZGVmYXVsdCJ9LHsia2V5IjoiYXV0aFBhdGgiLCJ2YWx1ZSI6Imh0dHBzOi8vYXV0aC5waW5nb25lLnt7dGxkfX0iLCJlbmFibGVkIjp0cnVlLCJ0eXBlIjoiZGVmYXVsdCJ9LHsia2V5IjoiYXBpUGF0aCIsInZhbHVlIjoiaHR0cHM6Ly9hcGkucGluZ29uZS57e3RsZH19L3YxIiwiZW5hYmxlZCI6dHJ1ZSwidHlwZSI6ImRlZmF1bHQifSx7ImtleSI6ImFkbWluRW52SUQiLCJ2YWx1ZSI6IiIsImVuYWJsZWQiOnRydWUsInR5cGUiOiJkZWZhdWx0In0seyJrZXkiOiJhZG1pbkFwcElEIiwidmFsdWUiOiIiLCJlbmFibGVkIjp0cnVlLCJ0eXBlIjoiZGVmYXVsdCJ9LHsia2V5IjoiYWRtaW5BcHBTZWNyZXQiLCJ2YWx1ZSI6IiIsImVuYWJsZWQiOnRydWUsInR5cGUiOiJkZWZhdWx0In0seyJrZXkiOiJlbnZJRCIsInZhbHVlIjoiIiwiZW5hYmxlZCI6dHJ1ZSwidHlwZSI6ImRlZmF1bHQifV0=) |
| [Login with Agreement Acceptance](platform-sso-and-authorization/openid-connect-oidc/login-with-agreement-acceptance.html)                  | [Run in Postman](https://god.gw.postman.com/run-collection/18568624-0e2f0523-60c8-4704-9d4a-99599f63428a?action=collection%2Ffork\&source=rip_markdown\&collection-url=entityId%3D18568624-0e2f0523-60c8-4704-9d4a-99599f63428a%26entityType%3Dcollection%26workspaceId%3D3550b170-7818-4801-b1eb-dcb7b3f64263#?env%5BPingOne%20Workflow%20Library%20Template%20%28release%3A%202025-04-17%29%5D=W3sia2V5IjoidGxkIiwidmFsdWUiOiJjb20iLCJlbmFibGVkIjp0cnVlLCJ0eXBlIjoiZGVmYXVsdCJ9LHsia2V5IjoiYXV0aFBhdGgiLCJ2YWx1ZSI6Imh0dHBzOi8vYXV0aC5waW5nb25lLnt7dGxkfX0iLCJlbmFibGVkIjp0cnVlLCJ0eXBlIjoiZGVmYXVsdCJ9LHsia2V5IjoiYXBpUGF0aCIsInZhbHVlIjoiaHR0cHM6Ly9hcGkucGluZ29uZS57e3RsZH19L3YxIiwiZW5hYmxlZCI6dHJ1ZSwidHlwZSI6ImRlZmF1bHQifSx7ImtleSI6ImFkbWluRW52SUQiLCJ2YWx1ZSI6IiIsImVuYWJsZWQiOnRydWUsInR5cGUiOiJkZWZhdWx0In0seyJrZXkiOiJhZG1pbkFwcElEIiwidmFsdWUiOiIiLCJlbmFibGVkIjp0cnVlLCJ0eXBlIjoiZGVmYXVsdCJ9LHsia2V5IjoiYWRtaW5BcHBTZWNyZXQiLCJ2YWx1ZSI6IiIsImVuYWJsZWQiOnRydWUsInR5cGUiOiJkZWZhdWx0In0seyJrZXkiOiJlbnZJRCIsInZhbHVlIjoiIiwiZW5hYmxlZCI6dHJ1ZSwidHlwZSI6ImRlZmF1bHQifV0=) |
| [Login with an Authenticator App](pingone-mfa/login-with-an-authenticator-app.html)                                                         | [Run in Postman](https://god.gw.postman.com/run-collection/18568624-3b0a1319-61e3-47ba-b2fc-fd4b4efb87b1?action=collection%2Ffork\&source=rip_markdown\&collection-url=entityId%3D18568624-3b0a1319-61e3-47ba-b2fc-fd4b4efb87b1%26entityType%3Dcollection%26workspaceId%3D3550b170-7818-4801-b1eb-dcb7b3f64263#?env%5BPingOne%20Workflow%20Library%20Template%20%28release%3A%202025-04-17%29%5D=W3sia2V5IjoidGxkIiwidmFsdWUiOiJjb20iLCJlbmFibGVkIjp0cnVlLCJ0eXBlIjoiZGVmYXVsdCJ9LHsia2V5IjoiYXV0aFBhdGgiLCJ2YWx1ZSI6Imh0dHBzOi8vYXV0aC5waW5nb25lLnt7dGxkfX0iLCJlbmFibGVkIjp0cnVlLCJ0eXBlIjoiZGVmYXVsdCJ9LHsia2V5IjoiYXBpUGF0aCIsInZhbHVlIjoiaHR0cHM6Ly9hcGkucGluZ29uZS57e3RsZH19L3YxIiwiZW5hYmxlZCI6dHJ1ZSwidHlwZSI6ImRlZmF1bHQifSx7ImtleSI6ImFkbWluRW52SUQiLCJ2YWx1ZSI6IiIsImVuYWJsZWQiOnRydWUsInR5cGUiOiJkZWZhdWx0In0seyJrZXkiOiJhZG1pbkFwcElEIiwidmFsdWUiOiIiLCJlbmFibGVkIjp0cnVlLCJ0eXBlIjoiZGVmYXVsdCJ9LHsia2V5IjoiYWRtaW5BcHBTZWNyZXQiLCJ2YWx1ZSI6IiIsImVuYWJsZWQiOnRydWUsInR5cGUiOiJkZWZhdWx0In0seyJrZXkiOiJlbnZJRCIsInZhbHVlIjoiIiwiZW5hYmxlZCI6dHJ1ZSwidHlwZSI6ImRlZmF1bHQifV0=) |
| [Login with Multifactor Authentication](pingone-mfa/login-with-multifactor-authentication.html)                                             | [Run in Postman](https://god.gw.postman.com/run-collection/18568624-94f2e1d1-83a5-440c-bc54-be71038df69a?action=collection%2Ffork\&source=rip_markdown\&collection-url=entityId%3D18568624-94f2e1d1-83a5-440c-bc54-be71038df69a%26entityType%3Dcollection%26workspaceId%3D3550b170-7818-4801-b1eb-dcb7b3f64263#?env%5BPingOne%20Workflow%20Library%20Template%20%28release%3A%202025-04-17%29%5D=W3sia2V5IjoidGxkIiwidmFsdWUiOiJjb20iLCJlbmFibGVkIjp0cnVlLCJ0eXBlIjoiZGVmYXVsdCJ9LHsia2V5IjoiYXV0aFBhdGgiLCJ2YWx1ZSI6Imh0dHBzOi8vYXV0aC5waW5nb25lLnt7dGxkfX0iLCJlbmFibGVkIjp0cnVlLCJ0eXBlIjoiZGVmYXVsdCJ9LHsia2V5IjoiYXBpUGF0aCIsInZhbHVlIjoiaHR0cHM6Ly9hcGkucGluZ29uZS57e3RsZH19L3YxIiwiZW5hYmxlZCI6dHJ1ZSwidHlwZSI6ImRlZmF1bHQifSx7ImtleSI6ImFkbWluRW52SUQiLCJ2YWx1ZSI6IiIsImVuYWJsZWQiOnRydWUsInR5cGUiOiJkZWZhdWx0In0seyJrZXkiOiJhZG1pbkFwcElEIiwidmFsdWUiOiIiLCJlbmFibGVkIjp0cnVlLCJ0eXBlIjoiZGVmYXVsdCJ9LHsia2V5IjoiYWRtaW5BcHBTZWNyZXQiLCJ2YWx1ZSI6IiIsImVuYWJsZWQiOnRydWUsInR5cGUiOiJkZWZhdWx0In0seyJrZXkiOiJlbnZJRCIsInZhbHVlIjoiIiwiZW5hYmxlZCI6dHJ1ZSwidHlwZSI6ImRlZmF1bHQifV0=) |
| [Login with Passwordless Authentication](pingone-mfa/login-with-passwordless-authentication.html)                                           | [Run in Postman](https://god.gw.postman.com/run-collection/18568624-ccbb5af6-8f4e-41ca-b154-f2b50e116eda?action=collection%2Ffork\&source=rip_markdown\&collection-url=entityId%3D18568624-ccbb5af6-8f4e-41ca-b154-f2b50e116eda%26entityType%3Dcollection%26workspaceId%3D3550b170-7818-4801-b1eb-dcb7b3f64263#?env%5BPingOne%20Workflow%20Library%20Template%20%28release%3A%202025-04-17%29%5D=W3sia2V5IjoidGxkIiwidmFsdWUiOiJjb20iLCJlbmFibGVkIjp0cnVlLCJ0eXBlIjoiZGVmYXVsdCJ9LHsia2V5IjoiYXV0aFBhdGgiLCJ2YWx1ZSI6Imh0dHBzOi8vYXV0aC5waW5nb25lLnt7dGxkfX0iLCJlbmFibGVkIjp0cnVlLCJ0eXBlIjoiZGVmYXVsdCJ9LHsia2V5IjoiYXBpUGF0aCIsInZhbHVlIjoiaHR0cHM6Ly9hcGkucGluZ29uZS57e3RsZH19L3YxIiwiZW5hYmxlZCI6dHJ1ZSwidHlwZSI6ImRlZmF1bHQifSx7ImtleSI6ImFkbWluRW52SUQiLCJ2YWx1ZSI6IiIsImVuYWJsZWQiOnRydWUsInR5cGUiOiJkZWZhdWx0In0seyJrZXkiOiJhZG1pbkFwcElEIiwidmFsdWUiOiIiLCJlbmFibGVkIjp0cnVlLCJ0eXBlIjoiZGVmYXVsdCJ9LHsia2V5IjoiYWRtaW5BcHBTZWNyZXQiLCJ2YWx1ZSI6IiIsImVuYWJsZWQiOnRydWUsInR5cGUiOiJkZWZhdWx0In0seyJrZXkiOiJlbnZJRCIsInZhbHVlIjoiIiwiZW5hYmxlZCI6dHJ1ZSwidHlwZSI6ImRlZmF1bHQifV0=) |
| [PKCE Authorization Code Flow](platform-sso-and-authorization/openid-connect-oidc/pkce-authorization-code-flow.html)                        | [Run in Postman](https://god.gw.postman.com/run-collection/18568624-4c6f9f73-7082-4ea9-ad30-a1313cecc21d?action=collection%2Ffork\&source=rip_markdown\&collection-url=entityId%3D18568624-4c6f9f73-7082-4ea9-ad30-a1313cecc21d%26entityType%3Dcollection%26workspaceId%3D3550b170-7818-4801-b1eb-dcb7b3f64263#?env%5BPingOne%20Workflow%20Library%20Template%20%28release%3A%202025-04-17%29%5D=W3sia2V5IjoidGxkIiwidmFsdWUiOiJjb20iLCJlbmFibGVkIjp0cnVlLCJ0eXBlIjoiZGVmYXVsdCJ9LHsia2V5IjoiYXV0aFBhdGgiLCJ2YWx1ZSI6Imh0dHBzOi8vYXV0aC5waW5nb25lLnt7dGxkfX0iLCJlbmFibGVkIjp0cnVlLCJ0eXBlIjoiZGVmYXVsdCJ9LHsia2V5IjoiYXBpUGF0aCIsInZhbHVlIjoiaHR0cHM6Ly9hcGkucGluZ29uZS57e3RsZH19L3YxIiwiZW5hYmxlZCI6dHJ1ZSwidHlwZSI6ImRlZmF1bHQifSx7ImtleSI6ImFkbWluRW52SUQiLCJ2YWx1ZSI6IiIsImVuYWJsZWQiOnRydWUsInR5cGUiOiJkZWZhdWx0In0seyJrZXkiOiJhZG1pbkFwcElEIiwidmFsdWUiOiIiLCJlbmFibGVkIjp0cnVlLCJ0eXBlIjoiZGVmYXVsdCJ9LHsia2V5IjoiYWRtaW5BcHBTZWNyZXQiLCJ2YWx1ZSI6IiIsImVuYWJsZWQiOnRydWUsInR5cGUiOiJkZWZhdWx0In0seyJrZXkiOiJlbnZJRCIsInZhbHVlIjoiIiwiZW5hYmxlZCI6dHJ1ZSwidHlwZSI6ImRlZmF1bHQifV0=) |
| [Progressive Profiling - Sign-On Action](platform-sso-and-authorization/openid-connect-oidc/progressive-profiling-sign-on-action.html)      | [Run in Postman](https://god.gw.postman.com/run-collection/18568624-386c1bb7-acde-4fa1-b85f-abc3994ffff3?action=collection%2Ffork\&source=rip_markdown\&collection-url=entityId%3D18568624-386c1bb7-acde-4fa1-b85f-abc3994ffff3%26entityType%3Dcollection%26workspaceId%3D3550b170-7818-4801-b1eb-dcb7b3f64263#?env%5BPingOne%20Workflow%20Library%20Template%20%28release%3A%202025-04-17%29%5D=W3sia2V5IjoidGxkIiwidmFsdWUiOiJjb20iLCJlbmFibGVkIjp0cnVlLCJ0eXBlIjoiZGVmYXVsdCJ9LHsia2V5IjoiYXV0aFBhdGgiLCJ2YWx1ZSI6Imh0dHBzOi8vYXV0aC5waW5nb25lLnt7dGxkfX0iLCJlbmFibGVkIjp0cnVlLCJ0eXBlIjoiZGVmYXVsdCJ9LHsia2V5IjoiYXBpUGF0aCIsInZhbHVlIjoiaHR0cHM6Ly9hcGkucGluZ29uZS57e3RsZH19L3YxIiwiZW5hYmxlZCI6dHJ1ZSwidHlwZSI6ImRlZmF1bHQifSx7ImtleSI6ImFkbWluRW52SUQiLCJ2YWx1ZSI6IiIsImVuYWJsZWQiOnRydWUsInR5cGUiOiJkZWZhdWx0In0seyJrZXkiOiJhZG1pbkFwcElEIiwidmFsdWUiOiIiLCJlbmFibGVkIjp0cnVlLCJ0eXBlIjoiZGVmYXVsdCJ9LHsia2V5IjoiYWRtaW5BcHBTZWNyZXQiLCJ2YWx1ZSI6IiIsImVuYWJsZWQiOnRydWUsInR5cGUiOiJkZWZhdWx0In0seyJrZXkiOiJlbnZJRCIsInZhbHVlIjoiIiwiZW5hYmxlZCI6dHJ1ZSwidHlwZSI6ImRlZmF1bHQifV0=) |
| [Refresh Token Exchange Flow](platform-sso-and-authorization/openid-connect-oidc/refresh-token-exchange-flow.html)                          | [Run in Postman](https://god.gw.postman.com/run-collection/18568624-b7545289-1269-4f9a-9094-b9366bfd9816?action=collection%2Ffork\&source=rip_markdown\&collection-url=entityId%3D18568624-b7545289-1269-4f9a-9094-b9366bfd9816%26entityType%3Dcollection%26workspaceId%3D3550b170-7818-4801-b1eb-dcb7b3f64263#?env%5BPingOne%20Workflow%20Library%20Template%20%28release%3A%202025-04-17%29%5D=W3sia2V5IjoidGxkIiwidmFsdWUiOiJjb20iLCJlbmFibGVkIjp0cnVlLCJ0eXBlIjoiZGVmYXVsdCJ9LHsia2V5IjoiYXV0aFBhdGgiLCJ2YWx1ZSI6Imh0dHBzOi8vYXV0aC5waW5nb25lLnt7dGxkfX0iLCJlbmFibGVkIjp0cnVlLCJ0eXBlIjoiZGVmYXVsdCJ9LHsia2V5IjoiYXBpUGF0aCIsInZhbHVlIjoiaHR0cHM6Ly9hcGkucGluZ29uZS57e3RsZH19L3YxIiwiZW5hYmxlZCI6dHJ1ZSwidHlwZSI6ImRlZmF1bHQifSx7ImtleSI6ImFkbWluRW52SUQiLCJ2YWx1ZSI6IiIsImVuYWJsZWQiOnRydWUsInR5cGUiOiJkZWZhdWx0In0seyJrZXkiOiJhZG1pbkFwcElEIiwidmFsdWUiOiIiLCJlbmFibGVkIjp0cnVlLCJ0eXBlIjoiZGVmYXVsdCJ9LHsia2V5IjoiYWRtaW5BcHBTZWNyZXQiLCJ2YWx1ZSI6IiIsImVuYWJsZWQiOnRydWUsInR5cGUiOiJkZWZhdWx0In0seyJrZXkiOiJlbnZJRCIsInZhbHVlIjoiIiwiZW5hYmxlZCI6dHJ1ZSwidHlwZSI6ImRlZmF1bHQifV0=) |
| [SAML Sign-On Flow](platform-sso-and-authorization/saml/saml-sign-on-flow.html)                                                             | [Run in Postman](https://god.gw.postman.com/run-collection/18568624-cf6d652a-2338-4e26-ac96-574b3a907d40?action=collection%2Ffork\&source=rip_markdown\&collection-url=entityId%3D18568624-cf6d652a-2338-4e26-ac96-574b3a907d40%26entityType%3Dcollection%26workspaceId%3D3550b170-7818-4801-b1eb-dcb7b3f64263#?env%5BPingOne%20Workflow%20Library%20Template%20%28release%3A%202025-04-17%29%5D=W3sia2V5IjoidGxkIiwidmFsdWUiOiJjb20iLCJlbmFibGVkIjp0cnVlLCJ0eXBlIjoiZGVmYXVsdCJ9LHsia2V5IjoiYXV0aFBhdGgiLCJ2YWx1ZSI6Imh0dHBzOi8vYXV0aC5waW5nb25lLnt7dGxkfX0iLCJlbmFibGVkIjp0cnVlLCJ0eXBlIjoiZGVmYXVsdCJ9LHsia2V5IjoiYXBpUGF0aCIsInZhbHVlIjoiaHR0cHM6Ly9hcGkucGluZ29uZS57e3RsZH19L3YxIiwiZW5hYmxlZCI6dHJ1ZSwidHlwZSI6ImRlZmF1bHQifSx7ImtleSI6ImFkbWluRW52SUQiLCJ2YWx1ZSI6IiIsImVuYWJsZWQiOnRydWUsInR5cGUiOiJkZWZhdWx0In0seyJrZXkiOiJhZG1pbkFwcElEIiwidmFsdWUiOiIiLCJlbmFibGVkIjp0cnVlLCJ0eXBlIjoiZGVmYXVsdCJ9LHsia2V5IjoiYWRtaW5BcHBTZWNyZXQiLCJ2YWx1ZSI6IiIsImVuYWJsZWQiOnRydWUsInR5cGUiOiJkZWZhdWx0In0seyJrZXkiOiJlbnZJRCIsInZhbHVlIjoiIiwiZW5hYmxlZCI6dHJ1ZSwidHlwZSI6ImRlZmF1bHQifV0=) |
| [Show App Permissions in Token](pingone-authorize/show-permissions-in-token.html)                                                           | [Run in Postman](https://god.gw.postman.com/run-collection/18568624-5deaf4f0-6526-40df-aff1-15d871f65fbf?action=collection%2Ffork\&source=rip_markdown\&collection-url=entityId%3D18568624-5deaf4f0-6526-40df-aff1-15d871f65fbf%26entityType%3Dcollection%26workspaceId%3D3550b170-7818-4801-b1eb-dcb7b3f64263#?env%5BPingOne%20Workflow%20Library%20Template%20%28release%3A%202025-04-17%29%5D=W3sia2V5IjoidGxkIiwidmFsdWUiOiJjb20iLCJlbmFibGVkIjp0cnVlLCJ0eXBlIjoiZGVmYXVsdCJ9LHsia2V5IjoiYXV0aFBhdGgiLCJ2YWx1ZSI6Imh0dHBzOi8vYXV0aC5waW5nb25lLnt7dGxkfX0iLCJlbmFibGVkIjp0cnVlLCJ0eXBlIjoiZGVmYXVsdCJ9LHsia2V5IjoiYXBpUGF0aCIsInZhbHVlIjoiaHR0cHM6Ly9hcGkucGluZ29uZS57e3RsZH19L3YxIiwiZW5hYmxlZCI6dHJ1ZSwidHlwZSI6ImRlZmF1bHQifSx7ImtleSI6ImFkbWluRW52SUQiLCJ2YWx1ZSI6IiIsImVuYWJsZWQiOnRydWUsInR5cGUiOiJkZWZhdWx0In0seyJrZXkiOiJhZG1pbkFwcElEIiwidmFsdWUiOiIiLCJlbmFibGVkIjp0cnVlLCJ0eXBlIjoiZGVmYXVsdCJ9LHsia2V5IjoiYWRtaW5BcHBTZWNyZXQiLCJ2YWx1ZSI6IiIsImVuYWJsZWQiOnRydWUsInR5cGUiOiJkZWZhdWx0In0seyJrZXkiOiJlbnZJRCIsInZhbHVlIjoiIiwiZW5hYmxlZCI6dHJ1ZSwidHlwZSI6ImRlZmF1bHQifV0=) |
| [Sign-Off User Session](platform-sso-and-authorization/sessions-and-logout/sign-off-user-session.html)                                      | [Run in Postman](https://god.gw.postman.com/run-collection/18568624-6d0bda4a-c923-4f92-8fa8-f91079792b8c?action=collection%2Ffork\&source=rip_markdown\&collection-url=entityId%3D18568624-6d0bda4a-c923-4f92-8fa8-f91079792b8c%26entityType%3Dcollection%26workspaceId%3D3550b170-7818-4801-b1eb-dcb7b3f64263#?env%5BPingOne%20Workflow%20Library%20Template%20%28release%3A%202025-04-17%29%5D=W3sia2V5IjoidGxkIiwidmFsdWUiOiJjb20iLCJlbmFibGVkIjp0cnVlLCJ0eXBlIjoiZGVmYXVsdCJ9LHsia2V5IjoiYXV0aFBhdGgiLCJ2YWx1ZSI6Imh0dHBzOi8vYXV0aC5waW5nb25lLnt7dGxkfX0iLCJlbmFibGVkIjp0cnVlLCJ0eXBlIjoiZGVmYXVsdCJ9LHsia2V5IjoiYXBpUGF0aCIsInZhbHVlIjoiaHR0cHM6Ly9hcGkucGluZ29uZS57e3RsZH19L3YxIiwiZW5hYmxlZCI6dHJ1ZSwidHlwZSI6ImRlZmF1bHQifSx7ImtleSI6ImFkbWluRW52SUQiLCJ2YWx1ZSI6IiIsImVuYWJsZWQiOnRydWUsInR5cGUiOiJkZWZhdWx0In0seyJrZXkiOiJhZG1pbkFwcElEIiwidmFsdWUiOiIiLCJlbmFibGVkIjp0cnVlLCJ0eXBlIjoiZGVmYXVsdCJ9LHsia2V5IjoiYWRtaW5BcHBTZWNyZXQiLCJ2YWx1ZSI6IiIsImVuYWJsZWQiOnRydWUsInR5cGUiOiJkZWZhdWx0In0seyJrZXkiOiJlbnZJRCIsInZhbHVlIjoiIiwiZW5hYmxlZCI6dHJ1ZSwidHlwZSI6ImRlZmF1bHQifV0=) |
| [Simple Login - Username and Password](platform-sso-and-authorization/openid-connect-oidc/simple-login-username-and-password.html)          | [Run in Postman](https://god.gw.postman.com/run-collection/18568624-00d53494-a48f-4d29-9b44-adbbcab6979e?action=collection%2Ffork\&source=rip_markdown\&collection-url=entityId%3D18568624-00d53494-a48f-4d29-9b44-adbbcab6979e%26entityType%3Dcollection%26workspaceId%3D3550b170-7818-4801-b1eb-dcb7b3f64263#?env%5BPingOne%20Workflow%20Library%20Template%20%28release%3A%202025-04-17%29%5D=W3sia2V5IjoidGxkIiwidmFsdWUiOiJjb20iLCJlbmFibGVkIjp0cnVlLCJ0eXBlIjoiZGVmYXVsdCJ9LHsia2V5IjoiYXV0aFBhdGgiLCJ2YWx1ZSI6Imh0dHBzOi8vYXV0aC5waW5nb25lLnt7dGxkfX0iLCJlbmFibGVkIjp0cnVlLCJ0eXBlIjoiZGVmYXVsdCJ9LHsia2V5IjoiYXBpUGF0aCIsInZhbHVlIjoiaHR0cHM6Ly9hcGkucGluZ29uZS57e3RsZH19L3YxIiwiZW5hYmxlZCI6dHJ1ZSwidHlwZSI6ImRlZmF1bHQifSx7ImtleSI6ImFkbWluRW52SUQiLCJ2YWx1ZSI6IiIsImVuYWJsZWQiOnRydWUsInR5cGUiOiJkZWZhdWx0In0seyJrZXkiOiJhZG1pbkFwcElEIiwidmFsdWUiOiIiLCJlbmFibGVkIjp0cnVlLCJ0eXBlIjoiZGVmYXVsdCJ9LHsia2V5IjoiYWRtaW5BcHBTZWNyZXQiLCJ2YWx1ZSI6IiIsImVuYWJsZWQiOnRydWUsInR5cGUiOiJkZWZhdWx0In0seyJrZXkiOiJlbnZJRCIsInZhbHVlIjoiIiwiZW5hYmxlZCI6dHJ1ZSwidHlwZSI6ImRlZmF1bHQifV0=) |
| [Transaction Approval Using Email](pingone-mfa/transaction-approval-using-sms.html)                                                         | [Run in Postman](https://god.gw.postman.com/run-collection/18568624-5251a600-ae51-4a38-96c5-d6564d3d8c6a?action=collection%2Ffork\&source=rip_markdown\&collection-url=entityId%3D18568624-5251a600-ae51-4a38-96c5-d6564d3d8c6a%26entityType%3Dcollection%26workspaceId%3D3550b170-7818-4801-b1eb-dcb7b3f64263#?env%5BPingOne%20Workflow%20Library%20Template%20%28release%3A%202025-04-17%29%5D=W3sia2V5IjoidGxkIiwidmFsdWUiOiJjb20iLCJlbmFibGVkIjp0cnVlLCJ0eXBlIjoiZGVmYXVsdCJ9LHsia2V5IjoiYXV0aFBhdGgiLCJ2YWx1ZSI6Imh0dHBzOi8vYXV0aC5waW5nb25lLnt7dGxkfX0iLCJlbmFibGVkIjp0cnVlLCJ0eXBlIjoiZGVmYXVsdCJ9LHsia2V5IjoiYXBpUGF0aCIsInZhbHVlIjoiaHR0cHM6Ly9hcGkucGluZ29uZS57e3RsZH19L3YxIiwiZW5hYmxlZCI6dHJ1ZSwidHlwZSI6ImRlZmF1bHQifSx7ImtleSI6ImFkbWluRW52SUQiLCJ2YWx1ZSI6IiIsImVuYWJsZWQiOnRydWUsInR5cGUiOiJkZWZhdWx0In0seyJrZXkiOiJhZG1pbkFwcElEIiwidmFsdWUiOiIiLCJlbmFibGVkIjp0cnVlLCJ0eXBlIjoiZGVmYXVsdCJ9LHsia2V5IjoiYWRtaW5BcHBTZWNyZXQiLCJ2YWx1ZSI6IiIsImVuYWJsZWQiOnRydWUsInR5cGUiOiJkZWZhdWx0In0seyJrZXkiOiJlbnZJRCIsInZhbHVlIjoiIiwiZW5hYmxlZCI6dHJ1ZSwidHlwZSI6ImRlZmF1bHQifV0=) |
| [User Registration - Self-Service Flow](platform-sso-and-authorization/openid-connect-oidc/user-registration-self-service-flow.html)        | [Run in Postman](https://god.gw.postman.com/run-collection/18568624-60b7fde7-4f30-48ce-b852-4ca200124688?action=collection%2Ffork\&source=rip_markdown\&collection-url=entityId%3D18568624-60b7fde7-4f30-48ce-b852-4ca200124688%26entityType%3Dcollection%26workspaceId%3D3550b170-7818-4801-b1eb-dcb7b3f64263#?env%5BPingOne%20Workflow%20Library%20Template%20%28release%3A%202025-04-17%29%5D=W3sia2V5IjoidGxkIiwidmFsdWUiOiJjb20iLCJlbmFibGVkIjp0cnVlLCJ0eXBlIjoiZGVmYXVsdCJ9LHsia2V5IjoiYXV0aFBhdGgiLCJ2YWx1ZSI6Imh0dHBzOi8vYXV0aC5waW5nb25lLnt7dGxkfX0iLCJlbmFibGVkIjp0cnVlLCJ0eXBlIjoiZGVmYXVsdCJ9LHsia2V5IjoiYXBpUGF0aCIsInZhbHVlIjoiaHR0cHM6Ly9hcGkucGluZ29uZS57e3RsZH19L3YxIiwiZW5hYmxlZCI6dHJ1ZSwidHlwZSI6ImRlZmF1bHQifSx7ImtleSI6ImFkbWluRW52SUQiLCJ2YWx1ZSI6IiIsImVuYWJsZWQiOnRydWUsInR5cGUiOiJkZWZhdWx0In0seyJrZXkiOiJhZG1pbkFwcElEIiwidmFsdWUiOiIiLCJlbmFibGVkIjp0cnVlLCJ0eXBlIjoiZGVmYXVsdCJ9LHsia2V5IjoiYWRtaW5BcHBTZWNyZXQiLCJ2YWx1ZSI6IiIsImVuYWJsZWQiOnRydWUsInR5cGUiOiJkZWZhdWx0In0seyJrZXkiOiJlbnZJRCIsInZhbHVlIjoiIiwiZW5hYmxlZCI6dHJ1ZSwidHlwZSI6ImRlZmF1bHQifV0=) |

## Using the PingOne Postman environment

The PingOne use case collections include test scripts that write environment variables and their current values to your active Postman environment for the newly created PingOne resources.

To save and use these resource IDs, specify a Postman environment and have the following Postman environment variables set before you begin. Refer to [The PingOne Postman Environment Template](../before-you-begin/postman-and-pingone/use-the-pingone-postman-environment-template.html) for the regional domains associated with the API endpoints for these environment variables:

* `{{tld}}`

  The top level domain for your region: `com`, `ca`, `eu`, `com.au`, `sg`, or `asia`. This variable is incorporated in each of the following `{{…​Path}}` variables to make changing your region simple. When you set `{{tld}}`, the `{{…​Path}}` variables are also set to the appropriate region.

* `{{apiPath}}`

  The regional domain for the PingOne server. These IDs identify a specific configured application in PingOne.

* `{{authPath}}`

  The domain for the PingOne authentication server.

* `{{orchestratePath}}`

  The regional domain (and part of the path) for the PingOne DaVinci server.

* `{{scimPath}}`

  The regional domain (and part of the path) for the PingOne SCIM server.

* `{{envID}}`

  The UUID of an environment resource. This ID identifies your current working domain within your organization.

* `{{accessToken}}`

  A valid access token returned by the PingOne authorization server from the worker application in your current environment. For information about creating a worker application and getting an access token, refer to [Create an admin Worker app connection](../getting-started/create-an-admin-worker-app.html).

---

---
title: External Identity Provider - Sign On
description: This activity shows you how to test the external authentication flow to sign-on using an external identity provider (IdP).
component: pingone-api
page_id: pingone-api:workflow-library:platform-sso-and-authorization/openid-connect-oidc/external-identity-provider-sign-on
canonical_url: https://developer.pingidentity.com/pingone-api/workflow-library/platform-sso-and-authorization/openid-connect-oidc/external-identity-provider-sign-on.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  prerequisites: Prerequisites
---

# External Identity Provider - Sign On

This activity shows you how to test the external authentication flow to sign-on using an external identity provider (IdP).

The easiest way to do this is by using two PingOne environments. One environment will act as the service provider (SP) for an OIDC application, while the other environment is used to configure an OIDC identity provider (IdP) connection.

This activity requires completing an internal authentication flow within the external authentication flow, so it's important to take note of which environment should be used to complete each step. On the first use of external authentication, you will need to link accounts. After the accounts are linked once, you will not need to link them again.

## Prerequisites

* Get an access token from the worker application that you created in [Create an admin Worker app connection](../../../getting-started/create-an-admin-worker-app.html).

* A **destination** PingOne environment to act as the service provider (SP) for the OIDC application. You'll use this environment to configure the OIDC IdP connection. Authentication flows in this environment can be configured to allow external authentication.

* A **source** PingOne environment that will act as the OIDC IdP. Users here will be able to complete authentication flows in the destination environment.

* Cross-environment admin permissions for the destination and source environments.

This scenario illustrates the following operations supported by the PingOne APIs:

* Create an OIDC application in the source environment.

* Create an OIDC IdP in the destination environment referencing the source application.

* Create a sign-on policy in the destination environment.

* Create a sign-on policy action to enable the sign-on policy for the OIDC IdP connection.

* Set the sign-on policy as the default for the destination environment.

* Create an OIDC application in the destination environment.

* Set the sign-on policy as the default for the destination environment.

* Create a population in the source and destination environments.

* Create users in the source and destination environments.

* Initiate an authorization request.

* Read an external authentication initialization.

* Send an external authentication request.

* Get the flow for an external identity provider.

* Pass in external identity provider credentials for verification.

* Retrieve an authorization code from the authorization server by calling the resume endpoint.

* Call the external authentication callback to get the response from an external identity provider.

* Get the flow and submit credentials for account linking.

* Retrieve an authorization code from the authorization server by calling the resume endpoint.

* Exchange an authorization code for an access token.

Click the **Run in Postman** button below to fork, or download and import, the Postman collection for this workflow to your workspace.

[Run in Postman](https://god.gw.postman.com/run-collection/18568624-2d238da4-4c7c-4b09-b17d-d9f127fb3e58?action=collection%2Ffork\&source=rip_markdown\&collection-url=entityId%3D18568624-2d238da4-4c7c-4b09-b17d-d9f127fb3e58%26entityType%3Dcollection%26workspaceId%3D3550b170-7818-4801-b1eb-dcb7b3f64263#?env%5BPingOne%20Workflow%20Library%20Template%20%28release%3A%202025-04-17%29%5D=W3sia2V5IjoidGxkIiwidmFsdWUiOiJjb20iLCJlbmFibGVkIjp0cnVlLCJ0eXBlIjoiZGVmYXVsdCJ9LHsia2V5IjoiYXV0aFBhdGgiLCJ2YWx1ZSI6Imh0dHBzOi8vYXV0aC5waW5nb25lLnt7dGxkfX0iLCJlbmFibGVkIjp0cnVlLCJ0eXBlIjoiZGVmYXVsdCJ9LHsia2V5IjoiYXBpUGF0aCIsInZhbHVlIjoiaHR0cHM6Ly9hcGkucGluZ29uZS57e3RsZH19L3YxIiwiZW5hYmxlZCI6dHJ1ZSwidHlwZSI6ImRlZmF1bHQifSx7ImtleSI6ImFkbWluRW52SUQiLCJ2YWx1ZSI6IiIsImVuYWJsZWQiOnRydWUsInR5cGUiOiJkZWZhdWx0In0seyJrZXkiOiJhZG1pbkFwcElEIiwidmFsdWUiOiIiLCJlbmFibGVkIjp0cnVlLCJ0eXBlIjoiZGVmYXVsdCJ9LHsia2V5IjoiYWRtaW5BcHBTZWNyZXQiLCJ2YWx1ZSI6IiIsImVuYWJsZWQiOnRydWUsInR5cGUiOiJkZWZhdWx0In0seyJrZXkiOiJlbnZJRCIsInZhbHVlIjoiIiwiZW5hYmxlZCI6dHJ1ZSwidHlwZSI6ImRlZmF1bHQifV0=)

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
title: Groups
description: The Groups workflows provide examples of how you can create collections of users that have the same access to applications. You can also create nested groups where members of a nested group automatically become members of the parent group, inheriting the same properties and permissions as the parent group.
component: pingone-api
page_id: pingone-api:workflow-library:platform-sso-and-authorization/groups
canonical_url: https://developer.pingidentity.com/pingone-api/workflow-library/platform-sso-and-authorization/groups.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
---

# Groups

The Groups workflows provide examples of how you can create collections of users that have the same access to applications. You can also create nested groups where members of a nested group automatically become members of the parent group, inheriting the same properties and permissions as the parent group.

Group management use cases often call the following platform API resources:

| Platform API                                   | Description                                                                                                                                                                                                                                                             |
| ---------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Groups](../../platform/groups.html)           | The groups service enables you to create collections of users with the same access to applications.                                                                                                                                                                     |
| [Users](../../platform/users.html)             | User resources are unique identities within PingOne that interact with the applications and services in the environment to which the user is assigned. The users service implements directory functions to create, read, update, delete, and search for user resources. |
| [Populations](../../platform/populations.html) | A PingOne population defines a set of users, similar to an organizational unit (OU).                                                                                                                                                                                    |

---

---
title: Identity Propagation
description: PingOne can propagate user identity information from the PingOne directory to a target identity store, or from a source identity store to the PingOne directory. The service continually synchronizes changes to and from the source and target identity stores. Propagation events are triggered by any addition, change, or deletion of users or user information in the source identity store.
component: pingone-api
page_id: pingone-api:workflow-library:platform-sso-and-authorization/identity-propagation
canonical_url: https://developer.pingidentity.com/pingone-api/workflow-library/platform-sso-and-authorization/identity-propagation.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
---

# Identity Propagation

PingOne can propagate user identity information from the PingOne directory to a target identity store, or from a source identity store to the PingOne directory. The service continually synchronizes changes to and from the source and target identity stores. Propagation events are triggered by any addition, change, or deletion of users or user information in the source identity store.

These tasks show you how to use the platform APIs to perform common actions for managing identity propagations. Identity propagation use cases often call the following platform API resources:

| Platform API                                                                                       | Description                                                                                                                                                               |
| -------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Propagation Plans](../../platform/identity-propagation-provisioning/propagation-plans.html)       | The propagation plans service implements unidirectional provisioning relationships between pairs of identity stores.                                                      |
| [Propagation Stores](../../platform/identity-propagation-provisioning/propagation-stores.html)     | The propagation stores service implements connections to an identity store owned by a customer.                                                                           |
| [Propagation Rules](../../platform/identity-propagation-provisioning/propagation-rules.html)       | The propagation rules service implements unidirectional provisioning relationships between a subset of identities on a source identity store and a target identity store. |
| [Propagation Mappings](../../platform/identity-propagation-provisioning/propagation-mappings.html) | The propagation mappings service implements attribute mappings associated with identity propagation rules.                                                                |

Refer to [Provisioning](https://docs.pingidentity.com/pingone/integrations/p1_provisioning.html) for more information regarding propagation of identities and [Inbound and outbound provisioning](https://docs.pingidentity.com/pingone/integrations/p1_inbound_outbound_provisioning.html) for more information regarding inbound versus outbound identity stores.