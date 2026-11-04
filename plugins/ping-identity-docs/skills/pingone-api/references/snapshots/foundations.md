---
title: Access services through scopes and roles
description: Explains how PingOne self-management scopes and administrator role assignments determine access to platform resources
component: pingone-api
page_id: pingone-api:foundations:pingone-roles-scopes-and-permissions/access-services-through-scopes-and-roles/index
canonical_url: https://developer.pingidentity.com/pingone-api/foundations/pingone-roles-scopes-and-permissions/access-services-through-scopes-and-roles/index.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-08-11
---

# Access services through scopes and roles

User applications rely on self-management scopes to grant users access to a subset of PingOne resources. For more information about scopes, refer to [Resource scopes](../../../platform/resources/resource-scopes/index.html). Conversely, administrator applications use role assignments to determine the actions a user or client can perform. For more information about roles, refer to [Roles](../../../platform/roles/index.html) in the *PingOne Platform APIs*.

For detailed information about scopes, refer to the following topics:

* [PingOne self-management scopes](pingone-self-management-scopes.html)

* [OpenID Connect (OIDC) scopes](openid-connect-oidc-scopes.html)

* [Custom scopes](custom-scopes.html)

---

---
title: Access tokens and ID tokens
description: "Explains PingOne access tokens and ID tokens, how they're obtained, their default lifetimes, and how to use them in API requests"
component: pingone-api
page_id: pingone-api:foundations:authentication-concepts/access-tokens-and-id-tokens/index
canonical_url: https://developer.pingidentity.com/pingone-api/foundations/authentication-concepts/access-tokens-and-id-tokens/index.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-08-25
section_ids:
  token-lifetime: Token lifetime
---

# Access tokens and ID tokens

All tokens in PingOne are JSON Web Tokens (JWTs) signed using the RS256 signing algorithm, except for refresh tokens which can be opaque. Access tokens are credential strings that represent authorization to access a protected resource. Client applications obtain access tokens by making OAuth 2 or OpenID Connect requests to an authorization server; resource servers require clients to authenticate using access tokens.

Access tokens are obtained from the token endpoint (when using the client credentials or authorization code grant types) or from the authorization endpoint (when using the implicit grant type). Access tokens are typically granted on behalf of a specific authenticated user. (Tokens granted directly to applications are called application tokens.)

Clients present access tokens when making requests to a resource server (for example, the PingOne API endpoints) using bearer token authentication as described by [RFC 6750](https://tools.ietf.org/html/rfc6750). Here is a sample request using an access token:

```bash
curl -X GET "https://api.pingone.com/v1/environments" \
-H "Content-type: application/json" \
-H "Authorization: Bearer {{accessToken}}"
```

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Calls to the PingOne Management APIs require an admin-level access token to authenticate the requests. An access token from a Worker app gives you admin-level access to the PingOne APIs. A Worker app's roles and permissions determine the authorized access to PingOne API resources. For more information about access tokens, roles, and scopes, refer to [Access services](../../pingone-roles-scopes-and-permissions/access-services-through-scopes-and-roles/index.html). |

## Token lifetime

By default, access tokens have a time to live (TTL) of 60 minutes. However, if you have a custom resource specified in your OIDC appliction's resource grant, you can set `accessTokenValiditySeconds` on that resource's token. For more information, refer to [POST Create Resource](../../../platform/resources/resources-1/create-resource.html#post-create-resource).

Refresh tokens have a default lifetime of 30 days. You can change this value by configuring the `refreshTokenDuration` property in your OIDC application. For more information, refer to the [Applications OIDC settings data model](../../../platform/application-management.html#applications-oidc-settings-data-model).

ID tokens have a lifetime of 60 minutes. This value is not configurable.

---

---
title: Administrator permissions and role assignments
description: Explains how PingOne Worker application role assignments determine administrator permissions and access to platform APIs
component: pingone-api
page_id: pingone-api:foundations:pingone-roles-scopes-and-permissions/administrator-permissions-and-role-assignments
canonical_url: https://developer.pingidentity.com/pingone-api/foundations/pingone-roles-scopes-and-permissions/administrator-permissions-and-role-assignments.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-08-11
section_ids:
  worker-application-permissions: Worker application permissions
  worker-applications-and-environments: Worker applications and environments
---

# Administrator permissions and role assignments

Unlike user self-service applications, administrator applications use role assignments to determine the actions a user or client can perform. For external API client applications, the access tokens do not use scopes to control access to resources. Instead, the actor's role assignments determine resource access.

## Worker application permissions

Administrator applications that interact with non-self Platform APIs are classified as a `WORKER` application type. This application type supports only the `OPENID_CONNECT` protocol. A worker application that uses the `client_credentials` grant type inherits the same role assignments as the user or application that created the application. These role assignments can be cross-environment, which allows access to APIs for other environments.

|   |                                                                                                                                                                                                                                                                                                                                                                               |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Worker applications can use a user-based grant type (`implicit` or `authorization_code`). With this configuration, you can assign only OIDC scopes to the application. When getting a token using a user-based grant type, the user's role assignments are used. When getting a token using the `client_credentials` grant type, the application's role assignments are used. |

Role assignments determine access to APIs (refer to [Application role assignments](../../platform/applications/application-role-assignments/index.html) and [User role assignments](../../platform/users/user-role-assignments/index.html) in the *PingOne Platform APIs*. Users and clients cannot create or use clients that have more privileges than the worker application itself. For example, an actor with only the Identity Data Admin role cannot create a worker application that has Environment Admin privileges. Likewise, access to an application's client secret is restricted based on the accessing user's or application's role assignments. If an actor has only the Identity Data Admin role, it is not able to see the client secret. Similar roles can have different privileges, or restrictions, based on the role's scope. For example, an actor with an Environment Admin role over a single environment cannot access the client secret of an application with Environment Admin privileges over the entire organization.

PingOne roles include a set of permissions that allow access to PingOne resources. For example, the Identity Data Admin role grants access to PingOne resources for these user management actions:

* Read, create, update, and delete user resources

* Read, create, update, and delete device management resources

* Assign identity resources

* Bulk user import

* Read, create, update and delete population resources

* Update user password resources

* Read user password state resources

* Read password policy resources

* Read audit reporting activities resources

* Read schema resources

The actor (user or client) assigning roles to the application must have the permissions that they are trying to assign. In other words, the requesting user or client must have the same (or broader) role assignments as the target application's role assignments. This prevents a lesser privileged user (such as a Client Application Developer) from creating a more privileged `client_credentials` application (such as an Environment Admin).

When retrieving access tokens for `WORKER` applications, the authorization service checks to make sure the user or client has at least one role assignment. If not, the token request is rejected. If at least one role assignment exists, the authorization service creates a token with no scopes except for the requested OIDC scopes. When accessing platform APIs with this token, it retrieves the actor's entitlements, which ensures that clients and users can access only the resources that their role assignments allow.

### Worker applications and environments

When a worker application with Environment Admin privileges creates a new environment, that application is given Identity Data Admin and Client Application developer role assignments for the new environment. Only the worker application can perform Identity Data Admin operations in that environment (refer to the list of Identity Data Admin actions above). However, the worker application can give the same role assignment to another user or worker application.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Access to a worker application's client secret requires having a superset of the worker application's role assignments. Initially, the worker application is granted all of the role assignments of the admin (or worker app) that created it, which gives the admin access to the worker application's secret (or any other admin with a superset of those role assignments).However, if the worker application ever gains new role assignments (for example, by creating a new environment and being granted role assignments to cover the new environment), then this may mean that the admin who originally created the worker application can no longer access its secret.One way to address this condition is to make sure that if an environment is created by a worker application, then that worker application should grant the newly received role assignments to any admins who need access to the worker application's secret. |

---

---
title: API attacks
description: Describes measures PingOne takes and steps you can take to prevent API attacks, including OAuth 2.0, rate limiting, and TLS encryption
component: pingone-api
page_id: pingone-api:foundations:api-security/api-attack-prevention
canonical_url: https://developer.pingidentity.com/pingone-api/foundations/api-security/api-attack-prevention.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-08-14
section_ids:
  what-pingone-does-to-prevent-against-api-attacks: What PingOne does to prevent against API attacks
  what-you-can-do-to-prevent-api-attacks-for-your-pingone-deployment: What you can do to prevent API attacks for your PingOne deployment
---

# API attacks

## What PingOne does to prevent against API attacks

* API access is secured using OAuth 2.0, which provides token-based authentication. This ensures that APIs are only accessible by authorized users or systems. Using short-duration tokens, rather than static API keys, PingOne significantly reduces the risk of stolen credentials being misused. For more information refer to [OpenID Connect/OAuth 2 APIs](../auth-apis-overview/openid-connect-oauth-2.html) and [OpenID Connect/OAuth 2](../../auth/openid-connect-oauth-2/index.html).

* User authentication is secured using OpenID Connect (OIDC) on top of OAuth 2.0, reducing the risk of API abuse by verifying user identities before granting access. For more information refer to [Authentication flow states](../authentication-concepts/pingone-authentication-flow-states/index.html).

* API authentication is secured using JSON Web Tokens (JWTs). JWTs are compact, encrypted tokens containing JSON content (claims) that are signed to ensure their integrity. PingOne verifies the signature of each JWT before granting access to APIs. For more information refer to [Access tokens and ID tokens](../authentication-concepts/access-tokens-and-id-tokens/index.html), [Token](../../auth/openid-connect-oauth-2/token/index.html), and [Configuration options](../../auth/auth-config-options/index.html).

* An API gateway is used for centralized management of API requests, and adherence to PingOne security protocols. The API gateway acts as an intermediary between clients and backend services, managing API traffic going through endpoints that require API authentication. The API gateway applies security policies, enforces rate limits, and handles authentication for API requests.

* Token expiration is enforced, ensuring that tokens expire after a predefined period. In case of suspicious activity or compromised tokens, tokens can be immediately revoked, rendering them useless to attackers. For more information refer to [Access tokens and ID tokens](../authentication-concepts/access-tokens-and-id-tokens/index.html).

* Rate limiting is enforced to control the volume of API requests that a user or system can make within a certain time frame. This prevents API abuse, such as brute-force attacks, credential stuffing, or excessive traffic that could degrade performance or lead to service outages. For more information refer to [PingOne standard platform limits](https://docs.pingidentity.com/pingone/getting_started_with_pingone/p1_platform_limits.html).

* Transport Layer Security (TLS) is used to encrypt all API communications between clients, services, and PingOne. This ensures that data transmitted via APIs is protected from interception and tampering during transit, preventing Man-in-the-Middle (MitM) attacks. For more information refer to [TLS and cipher suite requirements](../../before-you-begin/index.html#tls-and-cipher-suite-requirements).

## What you can do to prevent API attacks for your PingOne deployment

* Ensure that PingOne API credentials are securely stored and managed. Avoid hardcoding client secrets in applications or exposing them in public repositories. For more information refer to [Configuration options](../../auth/openid-connect-oauth-2/index.html#configuration-options) and [PingOne Credentials](../../credentials/index.html).

* Implement Role-Based Access Control (RBAC) by defining OAuth scopes for your API users and applications, ensuring that they only have access to the resources they need. This limits the attack surface by preventing over-privileged access to sensitive data or services. For more information refer to [Roles, scopes, and permissions](../pingone-roles-scopes-and-permissions/index.html).

* Use a Web Application Firewall (WAF) in front of your applications to protect against common API attacks like SQL injection, XSS, and DDoS attacks. A WAF inspects incoming API traffic and blocks malicious requests before they reach your application, ensuring that only legitimate traffic passes through.

---

---
title: API requests
description: Explains PingOne API request conventions, including regional endpoints, authorization, HTTP methods, UUIDs, and placeholder syntax
component: pingone-api
page_id: pingone-api:foundations:conventions/pingone-api-requests
canonical_url: https://developer.pingidentity.com/pingone-api/foundations/conventions/pingone-api-requests.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-08-12
section_ids:
  public-endpoints: Public endpoints
  authorization: Authorization
  conventions-http-methods: HTTP methods
  replacing-a-resource: Replacing a resource
  partial-updates-to-a-resource: Partial updates to a resource
  supported-data-exchange-formats: Supported data exchange formats
  endpoint-example-variations: Endpoint example variations
  data-models: Data models
  uuids-for-resource-identification: UUIDs for resource identification
  placeholder-syntax: Placeholder syntax
  request-model-and-query-parameter-expandable-sections: Request model and query parameter expandable sections
  link-expansion: Link expansion
  try-a-request: Try a Request
  changing-example-request-language: Changing example request language
  cors-support: Cross-origin resource sharing
  forced-type-conversion-of-floating-point-numbers-in-requests: Forced type conversion of floating point numbers in requests
---

# API requests

## Public endpoints

This section discusses making requests to public endpoints using geographic domains in your PingOne environment. If you use the Postman environment template retrieved when you [Download the PingOne Postman collections](../../before-you-begin/index.html#the-pingone-postman-collections), set the value of `{{tld}}` to the top level domain (TLD) appropriate to your region. Refer to [PingOne API domains](../../before-you-begin/index.html#pingone-api-domains) in the *PingOne Platform APIs* for more information. When you set `{{tld}}`, the `{{…​Path}}` variables are also set to the appropriate region.

PingOne offers separate services that each require all its API requests go to an exclusive domain. Use the tables below to determine the service endpoint and top level domain `{{tld}}` value of the geography appropriate for your environment:

| Region                                     | Code | Top level domain |
| ------------------------------------------ | ---- | ---------------- |
| North America geography (excluding Canada) | NA   | `com` (default)  |
| Canada region                              | CA   | `ca`             |
| European Union region                      | EU   | `eu`             |
| Australia region                           | AU   | `com.au`         |
| Singapore region                           | SG   | `sg`             |
| Asia-Pacific region                        | AP   | `asia`           |

|   |                                                                                                |
| - | ---------------------------------------------------------------------------------------------- |
|   | An organization can define and manage environments in only one geographic domain at this time. |

| Service            | Postman variable      | Endpoint                                  | Description                                                       |
| ------------------ | --------------------- | ----------------------------------------- | ----------------------------------------------------------------- |
| **Environments**   | `{{apiPath}}`         | `https://api.pingone.{{tld}`              | PingOne API services for environments.                            |
| **Authentication** | `{{authPath}}`        | `https://auth.pingone.{{tld}}`            | PingOne API services for authentication.                          |
| **DaVinci**        | `{{orchestratePath}}` | `https://orchestrate-api.pingone.{{tld}}` | PingOne API services for DaVinci Management.                      |
| **SCIM**           | `{{scimPath}}`        | `https://scim-api.pingone.{{tld}}`        | PingOne API services for Cross-domain Identity Management (SCIM). |

## Authorization

To make a call to the PingOne API, you'll need an OAuth 2.0 access token for API authentication. The access token (a JSON Web Token) is accepted per [RFC 6750](https://tools.ietf.org/html/rfc6750) most commonly through the `Authorization` HTTP request header. In the code samples in this document, the access token is expressed in the request header as `Authorization: Bearer accessToken`, where `accessToken` is a full base64url-encoded JSON web token generated by the authentication service.

## HTTP methods

The PingOne API supports the following HTTP methods. Note that a resource may not support all listed methods below. When a method is not supported, the platform returns a `405 METHOD NOT ALLOWED` error in the response.

* `POST`

  Creates a new resource in the collection. If a specific resource is identified, it performs an operation on that resource.

* `PUT`

  Updates a resource in the collection. If a specific resource is identified, it updates all attribute values of the resource.

* `PATCH`

  Updates the attributes on an object or a partial update for the specified attributes.

* `GET`

  Lists or queries a collection of resources. If a specific resource is identified, it returns the attribute values for the specific resource.

* `DELETE`

  Deletes or unlinks a resource from the collection.

A resource supports updating either by replacing the resource (`PUT`) or partially updating the resource (`PATCH`).

### Replacing a resource

A `PUT` request is a replace operation. Requests submitted using `PUT` will replace attribute values specified in the request and clear any attribute values that aren't specified.

A null value is represented in a resource by omitting the property, although you can specify `null` to explicitly clear the value.

### Partial updates to a resource

A `PATCH` operation performs partial updates of a resource. The body of a `PATCH` operation is similar to that of a `PUT` operation. However, omitting an attribute in a `PATCH` operation results in the attribute being ignored.

You can use a value of `null` to explicitly clear the value.

### Supported data exchange formats

The PingOne API supports JSON as the data exchange format with UTF-8 character encoding required for request body content. For `PUT`, `POST`, and `PATCH` operations, the `Content-type` request header identifies the format of the request body. A Content-type request header value of `application/json` specifies the data exchange format as JSON, which, by default, sets the character encoding to UTF-8. Here is a sample:

```bash
curl -vX PUT "https://api.pingone.com/v1/environments/{{envID}}/populations/{{popID}}" \
-H "Content-type: application/json" \
-H "Authorization: Bearer accessToken" \
-d "{
  "name" : "Finance",
  "description" : "Finance and accounting group"
}"
```

### Endpoint example variations

For clarity of request variations, we present the example requests in our documentation as though they're separate endpoints.

For example, the [POST Create Application](../../platform/applications/applications-1/create-application-oidc-protocol---web-app.html#post-create-application-oidc-protocol---web-app) operation has several request variations. Rather than showing multiple examples, we break this down into multiple reference pages.

### Data models

PingOne data models list the possible properties in a request or response body for each endpoint at a high level. The data models have five columns, described below.

* **Property**

  The name of the property.

* **Type**

  The valid data type for the property value. Possible options include: String, Integer, Boolean, Array.

* **Required**

  Whether the property is required for creating, updating, or otherwise modifying or acting upon a resource.

* **Mutable**

  Whether the property can be changed after its initial setting. The possible options are:

  * Mutable - Values that can be provided as input when creating, updating, or otherwise modifying or acting upon a resource.

  * Read-only - Values provided in the response resource only and not used/ignored for input.

  * Immutable - Values provided in the input when creating a resource, but otherwise treated as read-only for subsequent operations.

* **Description**

  A more detailed definition of the property. This could include a list of accepted values, the default value when left blank, circumstances in which the property is required or optional, or just an example value.

### UUIDs for resource identification

Resources in PingOne are identified by their associated UUID (universally unique identifier). API requests use UUIDs in the request URL to specify the resources involved in the operation. For clarity, the code samples in this API Reference use descriptive variables such as `{{envID}}`, `{{userID}}`, `{{appID}}`, and `{{deviceID}}` to represent the UUIDs assigned to PingOne resources.

For example, the following sample request URL specifies a unique device associated with a unique user in a unique environment. The resource ID variables represent specific UUIDs for PingOne resources.

```bash
curl -X "GET" "https://api.pingone.com/v1/environments/{{envID}}/users/{{userID}}/devices/{{deviceID}}"
```

The actual request URL with UUIDs looks like this:

```bash
curl -X "GET" "https://api.pingone.com/v1/environments/5caa81af-ec05-41ff-a709-c7378007a99c/users/8ce55f02-2077-4493-9a6d-0385df1f0772/devices/4ca9eb79-be29-4a1f-9a23-b29d58606e18"
```

There are a few exceptions to this convention. Notifications template names in PingOne are identified by the template name `{{templateName}}` rather than by a UUID. For example, the following request URL returns information about a specific template:

```bash
curl -X "GET" "https://api.pingone.com/v1/environments/5caa81af-ec05-41ff-a709-c7378007a99c/templates/{{templateName}}
```

The `{{templateName}}` variable is replaced by one of the pre-defined notifications template names in PingOne. The actual request URL that uses a defined notifications template called `strong_authentication` looks like this:

```bash
curl -X "GET" "https://api.pingone.com/v1/environments/5caa81af-ec05-41ff-a709-c7378007a99c/templates/strong_authentication
```

### Placeholder syntax

Some requests use placeholder syntax to reference platform resource entities as variables. When placeholder syntax is required, the PingOne resource used as a variable is expressed in placeholder syntax format as `${attribute}`. For example, when mapping a SAML `name` attribute to the PingOne `username` attribute, the value of the PingOne attribute in the POST request body is expressed as `${user.username}`. In most cases where placeholder syntax is required, the placeholder references attributes in the PingOne `user` schema. The variable is written as a path to the value: `${user.path.to.value}`. For example, to reference the `name.family` user attribute, the variable is written as `${user.name.family}`.

Placeholder syntax is also used to express sign-on policy condition variables. For example, a condition variable to specify the last completed time the password authenticator was used for sign on is expressed as `${session.lastSignOn.withAuthenticator.pwd.at}`.

Placeholders in sign-on policy conditions often specify a value or range of values to meet the sign-on condition. For example, the sign-on policy associated with the following condition prevents sign-on from devices that contain the remote IP address value specified by the variable `${flow.request.http.remoteIp}` in the specified IP address ranges.

```json
"condition": {
   "not": {
        "ipRange": [
            "10.1.1.1/8",
            "10.0.0.0/8"
        ],
        "contains": "${flow.request.http.remoteIp}"
    }
}
```

Placeholders are also used to specify external identity provider attributes. For example, to specify a Facebook attribute that is mapped to a PingOne attribute, the Facebook attribute is expressed as `${providerAttributes.<Facebook attribute name>}`. For example, the following expression maps the PingOne `username` attribute to the Facebook `email` attribute.

```json
{
    "name": "username",
    "value": "${providerAttributes.email}"
    "update": "EMPTY_ONLY",
}
```

The following table shows the PingOne resources that use Placeholder syntax in POST requests.

| PingOn resource                                                                                | Placeholder example                                                                                                                                                      |
| ---------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [Sign-on policy actions](../../platform/sign-on-policies/sign-on-policy-actions/index.html)    | `${session.lastSignOn.at}` `${session.lastSignOn.withAuthenticator.pwd.at}` `${session.lastSignOn.withAuthenticator.mfa.at}` `${flow.request.http.remoteIp}` `${user.*}` |
| [Identity providers](../../platform/identity-provider-management/index.html)                   | `${providerAttributes.<IdP attribute name>}`                                                                                                                             |
| [Notifications templates](../../platform/notifications/index.html)                             | `${user.username}` `${OTP}`                                                                                                                                              |
| [Resource attributes](../../platform/resources/resource-attributes/index.html)                 | `${user.email}`                                                                                                                                                          |
| [SAML attribute mapping](../../platform/applications/application-attribute-mapping/index.html) | `${user.id}`                                                                                                                                                             |

### Request model and query parameter expandable sections

Request model and query parameters expandable sections are included in our API documentation when applicable.

For an example of each, refer to the expandable Request model and Query parameters sections in [Create Application (OIDC Protocol - Worker App)](../../platform/applications/applications-1/create-application-oidc-protocol---worker-app.html#post-create-application-oidc-protocol---worker-app).

### Link expansion

You can optimize the information returned by a request through link expansion. Link expansion is helpful when you need the query to return detailed information from an additional resource in the response data. You can identify a resource to expand using the `expand` query string parameter in the request.

Here is a sample that requests data for a specific user and expands the `passwordPolicy` attribute to show the password policy's attribute data.

```bash
curl -X GET "https://api.pingone.com/v1/environments/{{envID}}/users/{{userID}}/password?expand=passwordPolicy" \
-H "Authorization: Bearer accessToken"
```

When using the `expand` parameter in the request, the returned JSON includes an embedded `passwordPolicy` resource to show the details of the password policy associated with this user:

```json
{
    "_links": {
        "self": {
            "href": "https://api.pingone.com/v1/environments/5caa81af-ec05-41ff-a709-c7378007a99c/users/b94f4977-0d52-4c9d-a5da-e7d42a82f613/password"
        },
        "environment": {
            "href": "https://api.pingone.com/v1/environments/5caa81af-ec05-41ff-a709-c7378007a99c"
        },
        "user": {
            "href": "https://api.pingone.com/v1/environments/5caa81af-ec05-41ff-a709-c7378007a99c/users/b94f4977-0d52-4c9d-a5da-e7d42a82f613"
        },
        "passwordPolicy": {
            "href": "https://api.pingone.com/v1/environments/5caa81af-ec05-41ff-a709-c7378007a99c/passwordPolicies/9ad15e9e-3ac6-43f7-86d3-01018f6ef0ad"
        },
        "password.check": {
            "href": "https://api.pingone.com/v1/environments/5caa81af-ec05-41ff-a709-c7378007a99c/users/b94f4977-0d52-4c9d-a5da-e7d42a82f613/password"
        },
        "password.reset": {
            "href": "https://api.pingone.com/v1/environments/5caa81af-ec05-41ff-a709-c7378007a99c/users/b94f4977-0d52-4c9d-a5da-e7d42a82f613/password"
        },
        "password.set": {
            "href": "https://api.pingone.com/v1/environments/5caa81af-ec05-41ff-a709-c7378007a99c/users/b94f4977-0d52-4c9d-a5da-e7d42a82f613/password"
        },
        "password.recover": {
            "href": "https://api.pingone.com/v1/environments/5caa81af-ec05-41ff-a709-c7378007a99c/users/b94f4977-0d52-4c9d-a5da-e7d42a82f613/password"
        }
    },
    "environment": {
        "id": "5caa81af-ec05-41ff-a709-c7378007a99c"
    },
    "user": {
        "id": "b94f4977-0d52-4c9d-a5da-e7d42a82f613"
    },
    "passwordPolicy": {
        "id": "9ad15e9e-3ac6-43f7-86d3-01018f6ef0ad"
    },
    "status": "NO_PASSWORD",
    "lastChangedAt": "2019-05-21T18:01:07.413Z",
    "_embedded": {
        "passwordPolicy": {
            "_links": {
                "self": {
                    "href": "https://api.pingone.com/v1/environments/5caa81af-ec05-41ff-a709-c7378007a99c/passwordPolicies/9ad15e9e-3ac6-43f7-86d3-01018f6ef0ad"
                },
                "environment": {
                    "href": "https://api.pingone.com/v1/environments/5caa81af-ec05-41ff-a709-c7378007a99c"
                }
            },
            "id": "9ad15e9e-3ac6-43f7-86d3-01018f6ef0ad",
            "environment": {
                "id": "5caa81af-ec05-41ff-a709-c7378007a99c"
            },
            "name": "Standard",
            "description": "A standard policy that incorporates industry best practices",
            "excludesProfileData": true,
            "notSimilarToCurrent": true,
            "excludesCommonlyUsed": true,
            "maxAgeDays": 182,
            "minAgeDays": 1,
            "maxRepeatedCharacters": 2,
            "minUniqueCharacters": 5,
            "history": {
                "count": 6,
                "retentionDays": 365
            },
            "lockout": {
                "failureCount": 5,
                "durationSeconds": 900
            },
            "length": {
                "min": 8,
                "max": 255
            },
            "minCharacters": {
                "1234567890": 1,
                "abcdefghijklmnopqrstuvwxyz": 1,
                "ABCDEFGHIJKLMNOPQRSTUVWXYZ": 1,
                "~!@#$%^&*()-_=+[]{}|;:,.<>/?": 1
            },
            "default": true
        }
    }
}
```

### Try a Request

Our documentation includes an interactive *Try a Request* feature. The *Try a Request* feature enables you to configure and send a PingOne API request and get a response from within the documentation. This is a quick way to interactively test a PingOne API request without needing to use either Postman or the command line.

The *Try a Request* option is shown at the end of each API reference page. For an example, try the *Try a Request* button in [Create User](../../platform/users/users-1/create-user.html#post-create-user).

### Changing example request language

PingOne API documentation includes example requests for each operation. By default, the request is shown in cURL, however, the programming language can be changed by selecting the Language drop-down.

The image below shows the Language drop-down in the example request in [Create User](../../platform/users/users-1/create-user.html#post-create-user).

![Example Request - Language drop-down](../../_images/p1_ExampleRequestLanguage.png)

### Cross-origin resource sharing

PingOne supports cross-origin resource sharing (CORS), which gives applications running at different domains permission to access resources on PingOne servers. For example, an application at <https://myapp.com> that uses PingOne to authenticate users needs to request permission to access resources at <https://auth.pingone.com> before authentication operations are executed. In this case, a request is made to the resource owner (auth.pingone.com) from the requestor (myapp.com) using CORS headers to ask for access privileges. The response from auth.pingone.com returns the CORS `Access-Control-Allow-Origin` header with a value that confirms the requestor's access rights.

PingOne servers are configured to trust all origins when using access tokens. However, when requesting sensitive resources that use PingOne session cookies for authentication, only specified origins will be trusted. The following endpoints require session cookies for authentication, and only the origins specified in the application's `corsSettings` property will be trusted when calling these endpoints:

```text
/{envId}/saml20/idp/sso
/{envId}/saml20/idp/startsso
/{envId}/saml20/resume
/{envId}/saml20/idp/slo
/{envId}/as/authorize
/{envId}/as/resume
/{envId}/as/signoff
/{envId}/wsf/sts/{appId}
/{envId}/wsf/mex/{appId}
/{envId}/wsf/prp/{appId}
/{envId}/wsf/prp/resume
```

When using session cookies for authentication, no origins will be trusted when calling these endpoints:

```text
/{envId}/rp/authenticate/{envId}/rp/callback/{callbackId}
/{envId}/saml20/sp/sso
/{envId}/saml20/sp/acs
/{envId}/saml20/sp/jwtacs
/{envId}/as/txs
```

Consequently, when defining an application's connection to PingOne, you generally do not need to add your application's domain to a list of trusted origins. Cross-origin requests that use HTTP methods to modify the resource, such as `PUT`, `PATCH`, `POST`, and `DELETE`, trigger a preflight request to ensure that the initial request can be sent. The browser initiates a preflight HTTP `OPTIONS` request to verify that the HTTP method used in the actual request is allowed. In these cases, the response from auth.pingone.com to the preflight request returns a response with the CORS `Access-Control-Allow-Methods` header to specify the allowed methods.

When making CORS requests, only these headers can be used:

* `Accept`

* `Accept-Language`

* `Content-Language`

* `Content-Type`

* `Range`

* `Authorization`

* `Content-Length`

* `Cookie`

* `Correlation-Id`

* `Origin`

* `Origin-Cookies`

* `Referer` or `Referrer`

* `X-Amz-Date`

* `X-Amz-Security-Token`

* `X-Api-Key`

* `X-client-version`

* `X-Content-Type-Options`

When accessing CORS responses, you're restricted to reading only the `Correlation-Id` header (as well as the request body).

Attempting to submit or access headers that are not listed above may prevent you from making CORS requests or reading the responses.

### Forced type conversion of floating point numbers in requests

PingOne truncates a `float` value submitted in the JSON request body to a matching `int` value for services other than flow orchestration. For example, in the following request body JSON, the `minAgeDays` value can be submitted with a value of `1.5`.

```json
{
  "name": "Standard",
  "description": "A standard policy that incorporates industry best practices",
  "excludesProfileData": true,
  "notSimilarToCurrent": true,
  "excludesCommonlyUsed": true,
  "maxAgeDays": 182,
  "minAgeDays": 1.5,
  "maxRepeatedCharacters": 2,
  "minUniqueCharacters": 5,
  "history": {
    "count": 6,
    "retentionDays": 365
  },
  "lockout": {
    "failureCount": 5,
    "durationSeconds": 900
  },
  "length": {
    "min": 8,
    "max": 255
  },
  "minCharacters": {
    "~!@#$%^&*()-_=+[]{}|;:,.<>/?": 1,
    "0123456789": 1,
    "ABCDEFGHIJKLMNOPQRSTUVWXYZ": 1,
    "abcdefghijklmnopqrstuvwxyz": 1
  },
  "default": true
}
```

The request will execute. However, the response shows that the `minAgeDays` value is converted automatically to an `int` value:

```json
{
  "_links": {
    "self": {
      "href": "https://api.pingone.com/v1/environments/5caa81af-ec05-41ff-a709-c7378007a99c/passwordPolicies/ad53ea0b-28b3-413f-a762-46eaf929ab78"
    },
    "environment": {
      "href": "https://api.pingone.com/v1/environments/5caa81af-ec05-41ff-a709-c7378007a99c"
    }
  },
  "id": "ad53ea0b-28b3-413f-a762-46eaf929ab78",
  "environment": {
    "id": "5caa81af-ec05-41ff-a709-c7378007a99c"
  },
  "name": "Standard",
  "description": "A standard policy that incorporates industry best practices",
  "excludesProfileData": true,
  "notSimilarToCurrent": true,
  "excludesCommonlyUsed": true,
  "maxAgeDays": 182,
  "minAgeDays": 1,
  "maxRepeatedCharacters": 2,
  "minUniqueCharacters": 5,
  "history": {
    "count": 6,
    "retentionDays": 365
  },
  "lockout": {
    "failureCount": 5,
    "durationSeconds": 900
  },
  "length": {
    "min": 8,
    "max": 255
  },
  "minCharacters": {
    "~!@#$%^&*()-_=+[]{}|;:,.<>/?": 1,
    "0123456789": 1,
    "ABCDEFGHIJKLMNOPQRSTUVWXYZ": 1,
    "abcdefghijklmnopqrstuvwxyz": 1
  },
  "default": true
}
```

Note that the value of the floating point number is not rounded. It is trimmed by removing the decimal portion of the value.

For flow orchestration services such as sign-on policy actions, `float` values submitted in the JSON request body generate an `INVALID_VALUE` error. For example, the following request body with a `priority` attribute value of `1.5` generates an error:

```json
{
    "priority": 1.5,
    "type": "MULTI_FACTOR_AUTHENTICATION",
    "recovery": {
    	"enabled": false
    },
    "sms": {
        "enabled": true
    },
    "voice": {
        "enabled": true
    },
    "email": {
        "enabled": true
    },
    "applications": [
        {
            "id": "5e81bba1-1234-457c-926a-aae0e9876543",
            "autoEnrollment":{"enabled":true}
        }
    ]
}
```

The response error looks like this:

```json
{
  "id": "15051F81-2500-4BBB-BE4A-0AF31DD50205",
  "code": "INVALID_REQUEST",
  "message": "The request could not be completed. The request was malformed or invalid.",
  "details": [
    {
      "code": "INVALID_VALUE",
      "target": "priority",
      "message": "Invalid value for attribute."
    }
  ]
}
```

---

---
title: API responses
description: Explains PingOne API response conventions, including HTTP headers, response codes, HAL data structure, relationships, and caching
component: pingone-api
page_id: pingone-api:foundations:conventions/pingone-api-responses
canonical_url: https://developer.pingidentity.com/pingone-api/foundations/conventions/pingone-api-responses.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-08-11
section_ids:
  http-response-headers: HTTP response headers
  http-response-codes: HTTP response codes
  synchronous-responses: Synchronous responses
  asynchronous-responses: Asynchronous responses
  response-data-structure: Response data structure
  relationships-links-and-references: Relationships, links, and references
  caching: Caching
---

# API responses

## HTTP response headers

The PingOne API includes information about the result of the operation in the HTTP headers. This enables you to determine the appropriate action to take without having to parse the response body.

The following HTTP Headers are returned by every operation:

* `Access-Control-Allow-Headers`

  Used in response to a cross-origin resource sharing (CORS) preflight request to indicate the HTTP headers that can be used when making a request.

* `Access-Control-Allow-Max-Age`

  Specifies how long the results of a CORS preflight request can be cached.

* `Access-Control-Allow-Methods`

  Specifies the method or methods allowed when accessing the resource in response to a CORS preflight request.

* `Cache-Control`

  Specifies directives for caching mechanisms in both requests and responses.

* `Content-Type`

  Specifies the data exchange format for the response data.

* `Correlation-Id`

  A custom header.

* `Date`

  Shows the date the response was sent.

* `Expires`

  Shows the date and time when the response expires.

* `Pragma`

  Used for backwards compatibility with HTTP/1.0 caches in which the Cache-Control HTTP/1.1 header is not yet present.

* `Strict-Transport-Security`

  Allows a web site to tell browsers that the site should only be accessed using HTTPS, instead of HTTP.

* `Transfer-Encoding`

  Specifies the form of encoding used to safely transfer the entity to the user.

* `Vary`

  Determines how to match future request headers to decide whether a cached response can be used rather than requesting a fresh one from the origin server. It is used by the server to indicate which headers it used when selecting a representation of a resource in a content negotiation algorithm.

* `Via`

  Used for tracking message forwards, avoiding request loops, and identifying the protocol capabilities of senders along the request/response chain.

* `X-Content-Type-Options`

  A marker used by the server to indicate that the MIME types advertised in the Content-Type headers should not be changed and be followed.

* `X-Frame-Options`

  This denies rendering in a frame where there is a frame mismatch.

* `X-XSS-Protection`

  A feature of Internet Explorer, Chrome, and Safari that stops pages from loading when the browsers detect reflected cross-site scripting (XSS) attacks.

## HTTP response codes

The PingOne API returns the status of an operation as a registered HTTP response code. The HTTP response codes can be summarized as:

* `200-299`

  Confirms a successful call.

* `300-399`

  Indicates that the call or subsequent calls should be made to another resource.

* `400-499`

  Shows that an exception occurred, generally due to client code, insufficient permissions, or incorrect parameters.

* `500-599`

  Shows that an error occurred, generally due to an issue with the service (for example, a service outage).

Operations can also return additional information about a failed operation in the HTTP response body.

### Synchronous responses

Responses for synchronous operations have the following behavior:

* `GET` operations

  A request that returns a body also returns the code `200 OK` with the resource in the body of the response.

* `POST` operations

  A request that creates a new resource returns `201 CREATED` with a `Location` header containing the location of the created resource.

* `PUT` or `PATCH` operations

  A request that updates a resource returns `200 OK` and the full resource in the body.

* `DELETE` operations

  A request that deletes a resource returns `204 NO CONTENT`.

### Asynchronous responses

The PingOne API can create a long-running or asynchronous operation that can be monitored by a client. An asynchronous operation will have the following behavior:

* `POST` operations

  Responses include `202 ACCEPTED` with a `Location` header containing the location of the newly created operation. The client can poll the provided location to check the status of the operation. The operation may also return a suggested number of seconds for the client to recheck the status using the `Retry-After` HTTP header.

* Canceling long-running operations

  Some resources may allow the client to cancel an operation by performing a `DELETE` request on the created resource.

* Clean up

  The PingOne API will clean up operation history according to the application requirements (such as, keep the last `n` results, or purge results after the client has verified its success).

## Response data structure

HAL (Hypertext Application Language) is a formatting convention that provides hyperlinks to related resources returned by an API request. For example, a `GET {{apiPath}}/v1/environments/{{envID}}/users/{{userID}}` request returns data for a specific user resource. The `_links` object in the JSON response data shows the hyperlinks to related resources associated with this user. You can use the `roleAssignments` link to get role assignments associated with this user, or the `password.reset` link to perform password management actions on this user resource.

```json
{
    "_links": {
        "self": {
            "href": "https://api.pingone.com/v1/environments/5caa81af-ec05-41ff-a709-c7378007a99c/users/8376797d-641c-4e7b-8bc1-2fdf71916cab"
        },
        "environment": {
            "href": "https://api.pingone.com/v1/environments/5caa81af-ec05-41ff-a709-c7378007a99c"
        },
        "population": {
            "href": "https://api.pingone.com/v1/environments/5caa81af-ec05-41ff-a709-c7378007a99c/populations/60971d3b-cc5a-4601-9c44-2be541f91bf1"
        },
        "devices": {
            "href": "https://api.pingone.com/v1/environments/5caa81af-ec05-41ff-a709-c7378007a99c/users/8376797d-641c-4e7b-8bc1-2fdf71916cab/devices"
        },
        "roleAssignments": {
            "href": "https://api.pingone.com/v1/environments/5caa81af-ec05-41ff-a709-c7378007a99c/users/8376797d-641c-4e7b-8bc1-2fdf71916cab/roleAssignments"
        },
        "password": {
            "href": "https://api.pingone.com/v1/environments/5caa81af-ec05-41ff-a709-c7378007a99c/users/8376797d-641c-4e7b-8bc1-2fdf71916cab/password"
        },
        "password.reset": {
            "href": "https://api.pingone.com/v1/environments/5caa81af-ec05-41ff-a709-c7378007a99c/users/8376797d-641c-4e7b-8bc1-2fdf71916cab/password"
        },
        "password.set": {
            "href": "https://api.pingone.com/v1/environments/5caa81af-ec05-41ff-a709-c7378007a99c/users/8376797d-641c-4e7b-8bc1-2fdf71916cab/password"
        },
        "password.check": {
            "href": "https://api.pingone.com/v1/environments/5caa81af-ec05-41ff-a709-c7378007a99c/users/8376797d-641c-4e7b-8bc1-2fdf71916cab/password"
        },
        "password.recover": {
            "href": "https://api.pingone.com/v1/environments/5caa81af-ec05-41ff-a709-c7378007a99c/users/8376797d-641c-4e7b-8bc1-2fdf71916cab/password"
        },
        "linkedAccounts": {
            "href": "https://api.pingone.com/v1/environments/5caa81af-ec05-41ff-a709-c7378007a99c/users/8376797d-641c-4e7b-8bc1-2fdf71916cab/linkedAccounts"
        },
        "account.sendVerificationCode": {
            "href": "https://api.pingone.com/v1/environments/5caa81af-ec05-41ff-a709-c7378007a99c/users/8376797d-641c-4e7b-8bc1-2fdf71916cab"
        }
    },
    "_embedded": {
        "password": {
            "status": "PASSWORD_EXPIRED"
        },
        "population": {
            "_links": {
                "self": {
                    "href": "https://api.pingone.com/v1/environments/5caa81af-ec05-41ff-a709-c7378007a99c/populations/60971d3b-cc5a-4601-9c44-2be541f91bf1"
                },
                "environment": {
                    "href": "https://api.pingone.com/v1/environments/5caa81af-ec05-41ff-a709-c7378007a99c"
                }
            },
            "id": "60971d3b-cc5a-4601-9c44-2be541f91bf1"
        }
    },
    "id": "8376797d-641c-4e7b-8bc1-2fdf71916cab",
    "environment": {
        "id": "5caa81af-ec05-41ff-a709-c7378007a99c"
    },
    "createdAt": "2020-02-18T20:50:14.092Z",
    "email": "tomjones@example.com",
    "enabled": true,
    "lifecycle": {
        "status": "ACCOUNT_OK"
    },
    "mfaEnabled": false,
    "name": {
        "given": "Tom",
        "family": "Jones"
    },
    "population": {
        "id": "60971d3b-cc5a-4601-9c44-2be541f91bf1"
    },
    "updatedAt": "2020-02-18T20:50:14.092Z",
    "username": "tomjones"
}
```

In addition, the `_embedded` resources returned by the request can be used as a navigation option to explore related resources. For example, `population` is returned as an `_embedded` resource in the response, and you can use the embedded resource's `self` link to initiate a `GET {{apiPath}}/v1/environments/{{envID}}/populations/{{popID}}` request to return data about the population associated with this user.

## Relationships, links, and references

Relationships between resources or operations can be described as follows:

* Relationships (one-to-one)

  Where a resource is directly related to another resource (such as employee to manager, user to population, logo to brand), the relationship is generally represented by an attribute as a first-class citizen of the resource. For example:

  * `_links` object : Contains an href to the actual resource.

  * Payload : Contains the reference as an attribute with the ID. The name of the `_links` attribute and the attribute in the payload must be the same).

  * Expandable : Yes.

* Relationships (one-to-many or many-to-one)

  Where a resource or resources may be related to a collection or to many resources. For example, a user to group membership:

  * `_links` object : Contains an href to the actual resource or collection.

  * Payload : May contain the reference as an attribute with the ID. The name of the `_links` attribute and the attribute in the payload must be the same).

  * Expandable : No.

* Informal relationships and links

  Provides navigation and self-discovery of the API and its related resources (such as next page of search results, next authentication service to invoke, or with which environment the resource is associated). For example:

  * `_links` object : Contains an href to the actual resource, collection, or URL.

  * Payload : Cannot contain the reference as an attribute.

  * Expandable : No.

These relationships and references are represented as follows:

* Links are represented using JSON HAL conventions (such as in a `_links` object).

* Links are represented as absolute URLs.

* Links can be expanded using the `expand` parameter. The links can also be referenced using the "property-as-resource" pattern.

* References as attributes have an `id` value and can also have additional attributes (such as `displayName`).

|   |                                                                                                                                               |
| - | --------------------------------------------------------------------------------------------------------------------------------------------- |
|   | For information about error messages, refer to [Error codes](../../platform/reference/index.html#error-codes) in the *PingOne Platform APIs*. |

## Caching

The PingOne API generally implements HTTP caching of operation responses. When HTTP caching is implemented, the following HTTP response headers are included:

* `ETag`

  An arbitrary string for the version of a representation. This includes the media type in the hash value. For example: `ETag`: `"686897696a7c876b7e"`.

* `Date`

  The date and time the response was returned. For example: `Date`: `Sun, 06 Nov 1994 08:49:37 GMT`.

* `Cache-Control`

  The maximum number of seconds a response can be cached. If caching is not supported for the response, the value is `no-cache`. For example: `Cache-Control`: `360` or `Cache-Control`: `no-cache`.

* `Expires`

  If `Cache-Control` is supplied, this header contains the timestamp for when the response expires. If caching is not supported for the response, this header is not present. For example: `Expires`: `Sun, 06 Nov 1994 08:49:37 GMT`.

* `Pragma`

  When the `Cache-Control` value is `no-cache`, this header is also set to `no-cache`. If caching is not supported for the response, this header is not present. For example: `Pragma`: `no-cache`.

* `Last-Modified`

  The timestamp for when the resource itself was last modified. For example: `Last-Modified`: `Sun, 06 Nov 1994 08:49:37 GMT`.

* `Varies`

  This header is included for user-specific headers (such as `Authorization`) in multi-tenant scenarios.

---

---
title: Applications
description: Describes PingOne application types and the endpoints to manage application connections, grants, role assignments, and attribute mapping
component: pingone-api
page_id: pingone-api:foundations:management-apis-overview/application-management-apis
canonical_url: https://developer.pingidentity.com/pingone-api/foundations/management-apis-overview/application-management-apis.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-08-11
section_ids:
  managing-applications: Managing applications
---

# Applications

Application resources define the connection between PingOne and the actual application (also known as a client connection). PingOne supports several application types. When you make a request to define a new application, you must specify the `type` property that specifies one of the following application types:

* **Web application**

  A browser-based application with a server-side component, such as ASP, CGI, JSP/Java, Node.js, or Ruby on Rails applications.

* **Native application**

  An application that is installed and run directly on the local operating system, like Java, Objective-C, Swift, or React applications. Native applications are typically intended for native devices.

* **Single-page application**

  A browser-based application that runs on the front-end with no server-side component, such as Sencha Touch, AngularJS, and React applications. A single-page application runs on the client side after it loads, so it cannot keep a client secret.

* **Non-interactive**

  A web application that does not require user interaction through the web browser, like a command line interface, a service, or a daemon.

* **Worker**

  An administrator application that can interact with platform APIs. Access to platform APIs is determined by the user's or application's role assignments.

* **Platform applications**

  PingOne creates platform applications (PingOne Admin Console, PingOne Application Portal, PingOne Self-Service - MyAccount, and PingFederate-SSO) when the environment is created. The PingFederate-SSO platform application is created only if the PingOne environment includes PingFederate, and unlike the other platform applications, PingFederate-SSO application information is not returned through a GET request.

|   |                                                                                                                                                                                                                                                                                                                                     |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | For any application type (except Worker/Non-interactive), you can specify either `NONE`, `CLIENT_SECRET_BASIC`, or `CLIENT_SECRET_POST` as the `tokenEndpointAuthMethod` attribute value. Non-interactive applications use the `CLIENT_CREDENTIALS` grant type, which does not support a `tokenEndpointAuthMethod` value of `NONE`. |

## Managing applications

The base endpoint, `/v1/environments/{{envID}}/applications`, provides endpoint operations to create, read, update, and delete OIDC and SAML application connections. There are `POST` request examples to show the required properties to create each type of application connection. For more information, refer to [Application Operations](../../platform/applications/applications-1/index.html) in the *PingOne Platform APIs*.

The secret endpoint, `/v1/environments/{{envID}}/applications/{{appID}}/secret`, provides endpoint operations to read and update the application's secret, if the requesting actor has a superset of the application's role assignments. For more information, refer to [Application Secret](../../platform/applications/application-secret/index.html) in the *PingOne Platform APIs*.

Applications support the following additional configuration properties:

* **Application resource grants**

  The application resource grants endpoint, `/v1/environments/{{envID}}/applications/{{appID}}/grants`, provides endpoint operations to create, read, update, and delete the resource grant associated with the application connection. For more information, refer to [Application Resource Grants](../../platform/applications/application-resource-grants/index.html) in the *PingOne Platform APIs*.

* **Application sign-on policy assignments**

  The application sign-on policy assignments endpoint, `/v1/environments/{{envID}}/applications/{{appID}}/signOnPolicyAssignments`, provides endpoint operations to create, read, update, and delete the sign-on policies associated with the application connection. For more information, refer to [Application Sign-On Policy Assignments](../../platform/applications/application-sign-on-policy-assignments/index.html) in the *PingOne Platform APIs*.

* **Application role assignments**

  The application role assignments endpoint, `/v1/environments/{{envID}}/applications/{{appID}}/roleAssignments`, provides endpoint operations to create, read, update, and delete the role assignments associated with the application connection. For more information, refer to [Application Role Assignments](../../platform/applications/application-role-assignments/index.html) in the *PingOne Platform APIs*.

* **Application attribute mapping**

  The application attribute mapping endpoint, `/v1/environments/{{envID}}/applications/{{appID}}/roleAssignments`, lets you customize the content of an ID token or a SAML assertion by adding custom attributes and their values. For more information, refer to [Application Attribute Mapping](../../platform/applications/application-attribute-mapping/index.html) in the *PingOne Platform APIs*.

* **Application MFA push credentials**

  Push credentials are required for sending push notifications to a native application. The endpoint, `/v1/environments/{{envID}}/applications/{{appID}}/pushCredentials`, provides endpoint operations to create, read, update, and delete the push credentials associated with the application connection. This section provides examples for both `APNS` and `FCM` push credential types. For more information, refer to [Application MFA Push Credentials](../../platform/applications/application-mfa-push-credentials/index.html) in the *PingOne Platform APIs*.

> **Collapse: Related topics**
>
> * [Authorization and authentication by application type](../authentication-concepts/authorization-and-authentication-by-application-type/index.html)

---

---
title: Authentication flow states
description: Explains PingOne authentication flow states and the sign-on actions, such as login, MFA, and progressive profiling, that complete a workflow
component: pingone-api
page_id: pingone-api:foundations:authentication-concepts/pingone-authentication-flow-states/index
canonical_url: https://developer.pingidentity.com/pingone-api/foundations/authentication-concepts/pingone-authentication-flow-states/index.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-08-11
section_ids:
  common-authentication-actions: Common authentication actions
---

# Authentication flow states

An application's sign-on policy determines the flow states and the corresponding actions required to complete an authentication workflow. When the authentication workflow begins, the flow gets the list of sign-on policies assigned to the application and evaluates the policy conditions that must be met to complete sign on. The sign-on policy evaluation logic is shown in the diagram below:

![Sign-on policy evaluation logic](../../../_images/p1_PolicyLogic.svg)

For more information about sign-on policies, refer to [Sign-on policies](../../../platform/sign-on-policies/index.html), [Sign-on policy actions](../../../platform/sign-on-policies/sign-on-policy-actions/index.html), and [Application sign-on policy assignments](../../../platform/applications/application-sign-on-policy-assignments/index.html) in the *PingOne Platform APIs*.

## Common authentication actions

The PingOne flow API supports single-factor and multi-factor actions to complete an authentication workflow. For a single-factor login flow, there are four branches that allow the user to submit a username and password (or create a new account). PingOne also supports an identity first discovery action that identifies the user and determines the user's applicable identity provider and authentication methods. For a multi-factor authentication action, there are two branches in which either a one-time password (OTP) or a push confirmation is used as the second factor in the authentication workflow.

PingOne supports a progressive profiling action that prompts users to provide additional data at sign on. This action type does not authenticate users. It is used only to obtain additional profile data.

* [Login action](login-action.html)

  * Sign on with username and password

  * Forgot password

  * Register user

  * Sign on with identity provider

* [Identifier first action](identifier-first-action.html)

* [Multi-factor (MFA) action](multi-factor-mfa-action.html)

  * Push authentication

* [Progressive profiling action](progressive-profiling-action.html)

|   |                                                                                                                                                        |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | For more information about flow states and their associated sign-on actions, refer to [Flows](../../../auth/flows/index.html) in *Platform Auth APIs*. |

---

---
title: Authorization and authentication
description: Overviews PingOne authorization and authentication workflow concepts, including application types, grant types, flow states, and tokens
component: pingone-api
page_id: pingone-api:foundations:authentication-concepts/index
canonical_url: https://developer.pingidentity.com/pingone-api/foundations/authentication-concepts/index.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-08-11
---

# Authorization and authentication

The following section provides additional information about PingOne platform authorization and authentication workflows. It also includes detailed information about access tokens and ID tokens.

* [Authorization and authentication by application type](authorization-and-authentication-by-application-type/index.html)

  PingOne supports several application types. When you define a new application, you must specify the `type` property value that best describes the application.

* [Authorization flow by grant type](authorization-flow-by-grant-type/index.html)

  Authorization and authentication sign-on flows depend on the application's grant type. When you define a new application, you must specify its grant type.

* [PingOne authentication flow states](pingone-authentication-flow-states/index.html)

  An application's sign-on policy determines the flow states and the corresponding actions required to complete the workflow.

* [Access tokens and ID tokens](access-tokens-and-id-tokens/index.html)

  Access tokens and ID tokens are credential strings that provide authorization to access a protected resource. All tokens in PingOne are signed JSON Web Tokens (JWTs).

* [Postman collection-level authorization](postman-collection-level-authorization/index.html)

  We use Postman to create our PingOne API docs, and have supplied our Postman collections for you to download. There's also an accompanying Postman Environment template already populated with the variables used in the collections. In PingOne collections, the authorization method is defined at the collection level, and this section describes how to use collection-level request authentication in Postman.

---

---
title: Authorization and authentication APIs
description: Overviews the PingOne Authorization and Authentication APIs, including OAuth 2, OpenID Connect, SAML 2.0, external authentication, and flow orchestration
component: pingone-api
page_id: pingone-api:foundations:auth-apis-overview/index
canonical_url: https://developer.pingidentity.com/pingone-api/foundations/auth-apis-overview/index.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-08-11
---

# Authorization and authentication APIs

The PingOne Authorization and Authentication APIs provide services to query the authorization server, run authentication workflows, and receive access tokens from the authorization server. An authentication workflow can include local authentication actions (login), multi-factor authentication actions, and other external actions. The Authentication API includes the flow orchestration and action services needed to configure an authentication workflow.

* [OAuth 2 and OpenID Connect](openid-connect-oauth-2.html)

  OpenID Connect is an authentication protocol that PingOne-connected applications can use to authenticate users and get user data through claims. The OAuth 2 framework defines several methods by which a client can obtain authorization to access protected resources using an access token.

* [SAML 2.0](saml-2.0.html)

  The SAML service provides support for the SAML protocol to authorize clients and allow clients to obtain a requestor's authentication state. The SAML service implements functions to initiate SAML 2.0 single sign-on and single logout authentication flows.

* [External authentication](external-authentication.html)

  The external authentication API provides endpoints for performing end user authentication with PingOne-supported external identity providers. End users are redirected immediately to the authentication initialization endpoint at the external authentication service. After sign-on, they are redirected back to Pingone, where the external authentication API validates the token or assertion returned from the external identity provider.

* [Flows](flows.html)

  The PingOne flow orchestration service configures the steps required to authenticate the actor that initiates the authentication request. The service is responsible for the authentication session and making calls to specific actions required by the authentication workflow.

---

---
title: Authorization and authentication by application type
description: Describes the PingOne application types (web, native, single-page, non-interactive, worker) and the authorization flow for each
component: pingone-api
page_id: pingone-api:foundations:authentication-concepts/authorization-and-authentication-by-application-type/index
canonical_url: https://developer.pingidentity.com/pingone-api/foundations/authentication-concepts/authorization-and-authentication-by-application-type/index.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-08-11
section_ids:
  authorization-flow-steps: Authorization flow steps
---

# Authorization and authentication by application type

PingOne supports several application types. When you make a `POST {{apiPath}}/v1/environments/{{envID}}/applications` request to define a new application, you must specify the `type` property that best describes the application. PingOne supports the following application types:

* [Web applications](web-applications.html)

  A browser-based application with a server-side component, such as ASP, CGI, JSP/Java, Node.js, or Ruby on Rails applications.

* [Native applications](native-and-single-page-applications.html)

  An application that is installed and run directly on the local operating system, like Java, Objective-C, Swift, or React applications. Native applications are typically intended for native devices.

* [Single-page applications](native-and-single-page-applications.html)

  A browser-based application that runs on the front-end with no server-side component, such as Sencha Touch, AngularJS, and React applications. A single-page application runs on the client side after it loads, so it cannot keep a client secret.

* [Non-interactive applications](non-interactive-applications.html)

  A web application that does not require user interaction through the web browser, like a command line interface, a service, or a daemon.

* [Worker applications](worker-applications.html)

  An administrator application that can interact with platform APIs. Access to platform APIs is determined by the user's or application's role assignments.

## Authorization flow steps

An authorization grant gives applications the capability to authenticate users and access secure resources. The following steps describe the application authorization flow:

1. The application initiates the authorization flow through a `GET` or `POST` request to the `authorize` endpoint.

2. The authorization service generates the access token for the `implicit` grant.

3. For `authorization_code` and `client_credentials` grants, the application calls the `/{{envID}}/as/token` endpoint to acquire the access token.

For more information about authorization, refer to [OpenID Connect/OAuth 2](../../auth-apis-overview/openid-connect-oauth-2.html).

---

---
title: Authorization code grant type
description: Walks through the PingOne authorization_code grant type flow using GET and POST authorize requests to obtain an access token
component: pingone-api
page_id: pingone-api:foundations:authentication-concepts/authorization-flow-by-grant-type/authorization-code-grant-type
canonical_url: https://developer.pingidentity.com/pingone-api/foundations/authentication-concepts/authorization-flow-by-grant-type/authorization-code-grant-type.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-08-11
section_ids:
  authorization-code-authorize-request-using-get: Authorization code authorize request using GET
  authorization-code-authorize-request-using-post: Authorization code authorize request using POST
---

# Authorization code grant type

If the grant type is `authorization_code`, PingOne returns an authorization code in the response to the application's authorization request. The `Location` HTTP header returned by the `/as/resume` endpoint contains the authorization code. The authorization code returned in the resume endpoint response is used by the `/as/token` endpoint to get an ID token, an access token, or both.

PingOne supports `GET` and `POST` HTTP methods for initiating the authorize request.

## Authorization code authorize request using GET

**Step 1:** Send an authorize request to the PingOne authorization server using `GET`.

```bash
curl --location --request GET '{{authPath}}/{{envID}}/as/authorize?response_type=code&client_id={{appID}}&redirect_uri={{redirect_uri}}&scope=openid'
```

The request requires the following properties in the request URL:

* `response_type`: For an authorization_code grant the response type is `code`.

* `client_id`: The application's ID.

* `redirect_uri`: The URL to redirect the browser after sign on.

* `scope`: The permissions that specify accessible resources.

The response returns a `Location` HTTP header that specifies the URL for the sign-on screen and the flow ID for the sign-on workflow. For information about additional optional query parameters that can be set on the request, refer to [Authorize (authorization_code)](../../../auth/openid-connect-oauth-2/authorization/authorize-authorization_code.html#get-authorize-authorization_code-get) in *Platform Auth APIs*.

**Step 2:** After the sign-on flow completes, call the resume endpoint.

```bash
curl --location --request GET '{{authPath}}/{{envID}}/as/resume?flowId={{flowID}}' \
--header 'Cookie: {{sessionToken}}'
```

The request requires the following properties in the request URL:

* `flowID`: The ID for the authentication flow.

The `Location` HTTP header returned by the resume endpoint contains the code. Note that the PingOne API uses session token cookies to establish the user's authentication session and maintain the session throughout the workflow, allowing the flow to redirect back to the authorization server to get the token.

**Step 3:** Call the token endpoint to exchange the authorization code for a token.

```bash
curl --location --request POST '{{authPath}}/{{envID}}/as/token' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'grant_type=authorization_code' \
--data-urlencode 'code={{authCode}}' \
--data-urlencode 'redirect_uri={{redirect_uri}}'
```

The request requires the following properties in the request URL:

* `grant_type`: The grant type of the token request. In this example, the value is `authorization_code`.

* `code`: The authorization code value returned by the resume endpoint.

* `redirect_uri`: The URL that specifies the return entry point of the application.

The token endpoint response returns the access token, ID token, or both. For information about the authorization code token request based on the application's `tokenEndpointAuthMethod`, refer to [Token](../../../auth/openid-connect-oauth-2/token/index.html) in *Platform Auth APIs*.

## Authorization code authorize request using POST

The authorize request using `POST` is essentially the same as `GET`. The `POST` request accepts all the same parameters as the `GET` request. For the POST request, parameters and their values are Form Serialized by adding the parameter names and values to the entity body of the HTTP request and specifying the `Content-Type: application/x-www-form-urlencoded` request header.

**Step 1:** Send an authorize request to the PingOne authorization server using `POST`.

```bash
curl --location --request POST '{{authPath}}/{{envID}}/as/authorize' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'response_type=code' \
--data-urlencode 'client_id={{appID}}' \
--data-urlencode 'redirect_uri={{redirect_uri}}' \
--data-urlencode 'scope=openid'
```

The request requires the following properties in the request URL:

* `response_type`: For an authorization_code grant the response type is `code`.

* `client_id`: The application's ID.

* `redirect_uri`: The URL to redirect the browser after sign on.

* `scope`: The permissions that specify accessible resources.

The response returns a `Location` HTTP header that specifies the URL for the sign-on screen and the flow ID for the sign-on workflow. For information about additional optional query parameters that can be set on the request, refer to [Authorize (authorization_code)](../../../auth/openid-connect-oauth-2/authorization/authorize-authorization_code-1.html#post-authorize-authorization_code-post) in *Platform Auth APIs*.

**Step 2:** After the sign-on flow completes, call the resume endpoint.

```bash
curl --location --request GET '{{authPath}}/{{envID}}/as/resume?flowId={{flowID}}' \
--header 'Cookie: {{sessionToken}}'
```

**Step 3:** Call the token endpoint to exchange the authorization code for a token.

```bash
curl --location --request POST '{{authPath}}/{{envID}}/as/token' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'grant_type=authorization_code' \
--data-urlencode 'code={{authCode}}' \
--data-urlencode 'redirect_uri={{redirect_uri}}'
```

---

---
title: Authorization flow by grant type
description: Describes the PingOne authorization request flow for each supported grant type, including authorization code, implicit, hybrid, and CIBA
component: pingone-api
page_id: pingone-api:foundations:authentication-concepts/authorization-flow-by-grant-type/index
canonical_url: https://developer.pingidentity.com/pingone-api/foundations/authentication-concepts/authorization-flow-by-grant-type/index.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-08-11
---

# Authorization flow by grant type

The authorization request flow depends on the grant type you have selected for the application.

* [Authorization code grant type](authorization-code-grant-type.html)

  If the application's grant type is `authorization_code`, PingOne returns an authorization code in the response to the application's authorization request. The authorization code is used by the `/as/token` endpoint to get an ID token, an access token, or both.

* [Implicit grant type](implicit-grant-type.html)

  If the application's grant type is `implicit`, the response to the authorization request is an `id_token`, a `token` (access token), or both, depending on the value of the `response_type` parameter in the authorization request.

* [Hybrid grant type](hybrid-grant-type.html)

  In a hybrid authorize flow, an authorization code is returned from the authorization endpoint, some tokens are returned from the authorization endpoint, and others are returned from the token endpoint. The authorization endpoint's `response_type` property specifies the `code` type and it also specifies `id_token`, or `token`, or both.

* [PKCE parameters](pkce-parameters.html)

  For added security, you can also include Proof Key for Code Exchange (PKCE) parameters in the authorization request for the code and hybrid grant types. PKCE for OAuth uses either plain text or a cryptographic hash of a random string that is included in the authorization request (`code_challenge`) along with the encoding method used (`code_challenge_method`). When the authorization code is issued in the response, the original plain text or random string (`code_verifier`) is included in the token request.

* [Device code grant type](device-code-grant-type.html)

  If the grant type is `device_code`, PingOne returns an activation code in the response to the `POST /{{envID}}/as/device_authorization` request. It starts a flow that gives OAuth-enabled devices, such as smart TVs, the ability to complete user authorization and access protected resources.

* [Token exchange grant type](token-exchange-grant-type.html)

  If an application's grant type is `token_exchange`, PingOne returns an access token in response to the `POST /{{envID}}/as/token` request. The application presents a `subject_token` and optionally, an `actor_token`. Currently, this grant type only issues custom resource access tokens, and not PingOne API access tokens (those with an audience of `https://api.pingone.<region>`).

* [CIBA grant type](ciba-grant-type.html)

  If the grant type is `ciba`, PingOne returns an `auth_req_id` value in the response to the `POST /{{envID}}/as/cibaAuthorization` request. The application then polls the `POST /{{envID}}/as/token` endpoint for tokens, including the `auth_req_id` value in the body of the request.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The PingOne platform also supports the `client_credentials` grant type for admin applications, which is not covered in this topic. For information about admin applications that use the `client_credentials` grant type, refer to [Authorization and authentication by application type](../authorization-and-authentication-by-application-type/index.html) and [Token Admin App (client_credentials)](../../../auth/openid-connect-oauth-2/token/token-admin-app-client_credentials.html) in the *PingOne Platform APIs*. |

---

---
title: Bearer Token
description: Explains how to configure a PingOne Postman collection to use Bearer Token authorization and retrieve an access token
component: pingone-api
page_id: pingone-api:foundations:authentication-concepts/postman-collection-level-authorization/bearer-token
canonical_url: https://developer.pingidentity.com/pingone-api/foundations/authentication-concepts/postman-collection-level-authorization/bearer-token.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-08-11
---

# Bearer Token

Bearer tokens enable requests to authenticate using an access key, such as a JSON Web Token (JWT) used by PingOne. The token is three base64url strings separated by periods, and specified in the variable used by the Authorization header.

To configure a PingOne collection to use `Bearer Token` for authorization:

1. Click on the collection.

2. Click the **Authorization** tab.

3. Select `Bearer Token` from **Type**.

4. In **Token**, type `{{accessToken}}`, the variable from the environment variable template.

You should always place your API key value in the variable. Authorization requests in PingOne collections that return an access token automatically set the `{{accessToken}}` variable to the returned access token.

Postman appends the **Token** value to the text `Bearer` in the required format to the request Authorization header: `Authorization: Bearer <access token>`.

Before you can run Postman requests that use `Bearer Token`, you must retrieve an access token. To retrieve an access token manually in Postman:

1. Run [Token Admin App (client_credentials)](../../../auth/openid-connect-oauth-2/token/token-admin-app-client_credentials.html).

   The script on the Tests tab sets the `{{accessToken}}` environment variable to `access_token` from the response.

2. Postman applies `{{accessToken}}` to requests with Authorization `Inherit auth from parent` until it expires.

3. Repeat these steps.

---

---
title: CIBA grant type
description: Explains the PingOne Client-Initiated Backchannel Authentication (CIBA) grant type flow, including the authorization and token endpoints
component: pingone-api
page_id: pingone-api:foundations:authentication-concepts/authorization-flow-by-grant-type/ciba-grant-type
canonical_url: https://developer.pingidentity.com/pingone-api/foundations/authentication-concepts/authorization-flow-by-grant-type/ciba-grant-type.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-08-11
section_ids:
  ciba-authorization-endpoint: CIBA authorization endpoint
  token-endpoint: Token endpoint
  response-codes: Response codes
---

# CIBA grant type

The Client-Initiated Backchannel Authentication (CIBA) flow is an [OpenID Connect specification](https://openid.net/specs/openid-client-initiated-backchannel-authentication-core-1_0.html). CIBA involves a consumption device, on which the user interacts with the relying party (RP), and an authentication device, on which the user authenticates with the OpenID Provider and grants consent.

|   |                                                                                                                                                                                   |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The CIBA specification defines three token delivery modes: poll, ping, and push. PingOne currently only supports poll mode, specifically only standard polling, not long polling. |

Consider a typical CIBA flow where:

1. An end uses selects $50 on a gas pump (the consumption device).

2. The point-of-sale application (the RP) sends a request to PingOne (the OpenID Provider).

3. PingOne invokes a PingOne MFA integration or DaVinci flow to prompt the user's device (the authentication device), such as their smartphone.

4. The user approves the transaction on their device.

The application must be configured with a `grantTypes` value of `ciba`, and a `tokenEndpointAuthMethod` value of `CLIENT_SECRET_BASIC`, `CLIENT_SECRET_JWT`, `PRIVATE_KEY_JWT`, or `CLIENT_SECRET_POST`.

## CIBA authorization endpoint

First, the application initiates the CIBA flow with the `POST /{{envID}}/as/cibaAuthorization` endpoint. In the body of this auth request, the application identifies the target end user with one of three properties:

* `login_hint`

  The application provides a string that PingOne can map to a user, such as a username or email address.

* `id_token_hint`

  The application provides an ID token representing a previous authentication for the target user. This ID token must have been issued by PingOne.

* `login_hint_token`

  The application provides a JWT containing the user ID as a claim. This token is created and signed by the application. Learn more in [Create a login_hint_token JWT](../../../auth/auth-config-options/create-a-login_hint_token-jwt.html).

|   |                                                                      |
| - | -------------------------------------------------------------------- |
|   | Providing more than one of these properties will result in an error. |

The auth endpoint returns an `auth_req_id` value that the application then sends to the `POST /{{envID}}/as/token` to receive an access token and ID token.

## Token endpoint

Next, the application polls the `POST /{{envID}}/as/token` endpoint for tokens. The request body must include the `auth_req_id` value returned from the CIBA authorization endpoint, and the `grant_type` value of `urn:openid:params:grant-type:ciba`.

Using the poll token delivery method, the application continues to poll this endpoint until it receives a success response or an error response indicating a terminal state.

Once the user approves the request on their authentication device, PingOne returns a successful token response with an access token and ID token.

### Response codes

If the user has not yet responded to the authentication request, PingOne returns the following token response:

```
{
    "error": "authorization_pending",
    "error_description": "The request could not be completed. There was an issue processing the request.: The authorization request is still pending. (Correlation ID: <id>)"
}
```

If the application on the consumption device sends its token request too frequently, PingOne returns the following token response:

```
{
    "error": "slow_down",
    "error_description": "The request could not be completed. There was an issue processing the request.: The authorization request is still pending. Please slow down the poll requests. (Correlation ID: <id>)"
}
```

If the user declines the request, PingOne returns the following token response:

```
{
    "error": "access_denied",
    "error_description": "The request could not be completed. There was an issue processing the request.: The authorization request has been denied. (Correlation ID: <id>)"
}
```

If the CIBA request has expired, PingOne returns the following token response:

```
{
    "error": "expired_token",
    "error_description": "The request could not be completed. There was an issue processing the request.: The authorization request for the provided auth_req_id has expired. (Correlation ID: <id>)"
}
```

---

---
title: Code injection
description: Describes measures PingOne takes and steps you can take to prevent code injection attacks such as SQL injection and cross-site scripting
component: pingone-api
page_id: pingone-api:foundations:api-security/code-injection-prevention
canonical_url: https://developer.pingidentity.com/pingone-api/foundations/api-security/code-injection-prevention.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-08-11
section_ids:
  what-pingone-does-to-prevent-against-code-injection: What PingOne does to prevent against code injection
  what-you-can-do-to-prevent-code-injection-for-your-pingone-deployment-and-applications: What you can do to prevent code injection for your PingOne deployment and applications
---

# Code injection

## What PingOne does to prevent against code injection

* Strict input validation (such as for form inputs, query parameters, and API requests) is enforced to ensure user-provided data is checked against expected formats. By validating inputs against defined rules (such as, acceptable characters, data types, and length), PingOne prevents attackers from injecting malicious code into application fields.

* Content Security Policy (CSP) headers are used to control the resources (such as, scripts, styles, images) that can be loaded and executed by the browser. This prevents cross-site scripting (XSS) attacks, a common form of code injection, by ensuring that only trusted and pre-approved scripts can be executed, and inline scripts are blocked.

* Parameterized queries and prepared statements are used to protect against SQL injection attacks. These methods separate user inputs from the actual SQL query, ensuring that even if an attacker tries to inject SQL commands, this will be treated as plain data, preventing them from executing unauthorized database queries. For more information refer to [Parameterized ACIs](https://docs.pingidentity.com/pingdirectory/latest/pingdirectory_security_guide/pd_sec_parameterized_acis.html), [Optimized page searches using caching](https://docs.pingidentity.com/pingdirectory/latest/pingdirectory_server_administration_guide/pd_ds_optimize_paged_search_caching.html), and [Searching entries](https://docs.pingidentity.com/pingdirectory/latest/pingdirectory_server_administration_guide/pd_ds_search_entries.html).

* Regular code reviews and static analysis tools are used to detect potential injection vulnerabilities during our development process. By identifying and addressing vulnerabilities early, PingOne reduces the likelihood of code injection issues in production environments.

* Automated dynamic application security scans are used to identify vulnerabilities, such as SQL injection and XSS, in web applications. These scans help detect injection vulnerabilities before attackers can exploit them.

* Regular third-party penetration testing is conducted on the PingOne platform to simulate real-world attacks, including code injection attempts. These tests help ensure that the platform's defenses are strong enough to withstand sophisticated injection attacks.

## What you can do to prevent code injection for your PingOne deployment and applications

* Implement Intrusion Detection Systems (IDS) for your applications to monitor network traffic for suspicious behavior or abnormal requests that may indicate a code injection attempt. Real-time monitoring ensures administrators are alerted to unusual activity, and can respond quickly.

* Use secure server configurations for your applications to reduce your attack surface and limit potential vulnerabilities. For instance, disable unnecessary ports and services, and keep software updated with the latest security patches.

* Follow the least privilege principle, ensuring that both users and applications have only the minimum permissions necessary to perform their tasks. This limits the damage that can be done if an attacker successfully executes code. For more information refer to [Roles, scopes, and permissions](../pingone-roles-scopes-and-permissions/index.html).

---

---
title: Control access to applications through roles and groups
description: Explains how to use PingOne application accessControl properties to restrict access to OIDC and SAML applications by role or group
component: pingone-api
page_id: pingone-api:foundations:pingone-roles-scopes-and-permissions/control-access-to-applications-through-roles-and-groups
canonical_url: https://developer.pingidentity.com/pingone-api/foundations/pingone-roles-scopes-and-permissions/control-access-to-applications-through-roles-and-groups.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-08-11
section_ids:
  application-access-control-for-openid-connect-applications: Application access control for OpenID Connect applications
  application-access-control-for-saml-applications: Application access control for SAML applications
---

# Control access to applications through roles and groups

The applications data model includes optional `accessControl` properties that, when set, specify the conditions that must be met by an authenticating actor to access the application. The application properties that control application access are:

* `accessControl.role.type`

  This property specifies that an administrator role is required to access the application. When set, the only option for this property is `ADMIN_USERS_ONLY`, which means that the actor must be assigned at least one or more of the following administrator roles: Organization Admin, Environment Admin, Identity Data Admin, or Client Application Developer. For more information about roles, refer to [Roles](../../platform/roles/index.html) in the *PingOne Platform APIs*. If this property is not set, access to the application is not restricted by administrator roles.

* `accessControl.group.type`

  This property specifies that the actor must be associated with a particular group (or groups) to access the application. When set, this property can be set to `ANY_GROUP`, which means that the actor must be a member of at least one group specified in the `accessControl.group.groups` property. This property can also be set to `ALL_GROUPS`, which means that the actor must belong to all groups specified in the `accessControl.group.groups` property. If this property is not set, access to the application is not restricted by groups.

* `accessControl.group.groups`

  This property specifies a list of one or more groups that control access to the application. If there is more than one group, then the actor must belong to at least one group (if `ANY_GROUP` is the value of `accessControl.group.type`) or all groups (if `ALL_GROUPS` is the value of `accessControl.group.type`). If this property is not set, access to the application is not restricted by groups.

## Application access control for OpenID Connect applications

When `accessControl` properties are set for an application, the authenticating actor must meet the requirements specified in the application's `accessControl` properties to get a token.

To implement role-based application access control:

1. Set the `accessControl.role.type` property value to `ADMIN_USERS_ONLY`.

2. Ensure that the authenticating actor has at least one assigned administrator role.

If the actor has an assigned administrator role, a token is issued that allows access to the application.

To implement group-based application access control:

1. Set the `accessControl.group.type` and `accessControl.group.groups` properties. (If you set one of the application's access control group properties, you must set the other.)

2. Set the property value for the `accessControl.group.type`. The options are `ANY_GROUP` and `ALL_GROUPS`.

3. Set the `accessControl.group.groups` property value to list the group IDs to which an actor must belong. For information about obtaining group IDs, refer to [Groups](../../platform/groups/index.html) in the *PingOne Platform APIs*.

If the actor belongs to at least one group (for the `ANY_GROUP` type), or all groups (for the `ALL_GROUPS` type), a token is issued that allows access to the application.

|   |                                                                                                                                                                                                                                                                                                                                                               |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | For OIDC applications, if the `grant_type` is either `authorization_code` or `implicit`, then the application's `accessControl` conditions are evaluated to determine whether the user can be issued a token. If the user already has an access token, application access conditions are not evaluated to refresh token or to token introspection operations. |

## Application access control for SAML applications

When `accessControl` properties are set for a SAML application, the authenticating actor must meet the requirements specified in the application's `accessControl` properties to get an assertion. The steps to define the `accessControl` properties for role-based and group-based conditions are the same as for OIDC applications. If the authenticating actor meets the the application's access control conditions, an assertion is created. If the conditions are not met, a sign-on attempt returns an authorization failed error.

---

---
title: Conventions
description: Overviews the conventions used to call PingOne APIs, including request formatting, response handling, and query parameter filtering
component: pingone-api
page_id: pingone-api:foundations:conventions/index
canonical_url: https://developer.pingidentity.com/pingone-api/foundations/conventions/index.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-08-11
---

# Conventions

This topic describes how to call PingOne APIs, how responses are returned by the PingOne resource server, and how collections that support filtering can be fine-tuned using query parameters on the request. The following sections provide information about these conventions:

* [PingOne API requests](pingone-api-requests.html)

* [PingOne API responses](pingone-api-responses.html)

---

---
title: Custom scopes
description: Explains custom resource scopes and custom PingOne API scopes, and how they control access to protected endpoints and user attributes
component: pingone-api
page_id: pingone-api:foundations:pingone-roles-scopes-and-permissions/access-services-through-scopes-and-roles/custom-scopes
canonical_url: https://developer.pingidentity.com/pingone-api/foundations/pingone-roles-scopes-and-permissions/access-services-through-scopes-and-roles/custom-scopes.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-08-11
section_ids:
  custom-resource-scopes: Custom resource scopes
  custom-pingone-api-scopes: Custom PingOne API scopes
---

# Custom scopes

Resources are the protected endpoints that applications request access to using OAuth 2 authorization services. The PingOne platform includes two predefined resources, `PingOne API`, which is a defined resource that represents the PingOne APIs, and `openid`, which represents OpenID Connect scopes. These resources have self scopes that grant an actor permission to perform CRUD operations on the actor's data (such as `p1:create:device`, `p1:read:device`, `p1:update:device`, and `p1:delete:device`).

In addition, the platform lets you configure additional resources and their associated self scopes. For example, a custom resource such as `https://api.acme-photo.com` might have `upload:photos`, `read:photos`, `edit:photos`, and `delete:photos` scopes that give users permission to manage their photo libraries.

PingOne supports the following two types of resource scopes.

## Custom resource scopes

Custom resource scopes are associated with protected endpoints on a non-PingOne resource server. Custom resources can be associated with an application either exclusively, or in addition to the platform's predefined resources. When an application is associated with both the PingOne platform resource and a custom resource, an authorization request cannot include scopes from both PingOne and the custom resource.

If you do specify scopes from both PingOne and the custom resource in the authorize request, the request returns the following error:

```none
The request could not be completed. One or more validation errors were in the request.: May not request scopes for multiple resources (Correlation ID: 8E7B23B8-6761-4532-8AFC-4B723D52FF5D).
```

OIDC-based applications in PingOne can now request an access token that accesses scopes from multiple custom resources in a single request. This capability simplifies the application authentication and authorization process and reduces the number of requests an application must make. By default, if more than one resource is associated with the application, actors need to make separate authorization requests to get a token for the desired resource scopes. However, if the `requestScopesForMultipleResourcesEnabled` OIDC property on the application is set to `true`, then the application accepts scopes from multiple custom resources, eliminating the need to make multiple authorize requests.

For more information, refer to [Applications OIDC settings data model](../../../platform/application-management.html#applications-oidc-settings-data-model), [Resource Scopes](../../../platform/resources/resource-scopes/index.html), and [Create scope](../../../platform/resources/resource-scopes/create-custom-resource-scope.html#post-create-custom-resource-scope) in the *PingOne Platform APIs*.

## Custom PingOne API scopes

Custom PingOne API scopes control access to specific user schema attributes. As described above, a PingOne platform custom scope is based on an existing platform scope and uses the `schemaAttributes` property in the scope's definition to list the specific user attributes that the end user has permission to read or update. For example, a scope that grants permission to update only the user's email address would list only the `email` attribute in the `schemaAttributes` property. This PingOne custom scope is named by adding a descriptive suffix to the base PingOne scope name: `p1:update:user:email-only`.

For more information about defining custom PingOne API scopes, refer to [Create PingOne access control scope](../../../platform/resources/resource-scopes/create-pingone-access-control-scope.html#post-create-pingone-access-control-scope) in the *PingOne Platform APIs*.

---

---
title: Device code grant type
description: Walks through the PingOne device_code grant type flow used by OAuth-enabled devices such as smart TVs to authorize access
component: pingone-api
page_id: pingone-api:foundations:authentication-concepts/authorization-flow-by-grant-type/device-code-grant-type
canonical_url: https://developer.pingidentity.com/pingone-api/foundations/authentication-concepts/authorization-flow-by-grant-type/device-code-grant-type.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-08-11
section_ids:
  authorization-for-a-device-authorize-grant-request: Authorization for a device authorize grant request
---

# Device code grant type

If the grant type is `device_code`, PingOne returns an activation code in the response to the `POST /{{envID}}/as/device_authorization` request. This authorize endpoint is used only with device authorization grant flows. It starts a flow that gives OAuth enabled devices such as smart TVs the ability to complete user authorization and access protected resources.

Unlike the PingOne `as/authorize` request, which returns a `302 Location` header in the response, the `/as/device_authorization` endpoint returns a `200 OK` successful operation message. The response body returns the `user_code` property value (the activation code) as well as the verification URI (a short web address) that end users visit on another device to enter (or confirm) the activation code.

The steps below outline the device authorization grant flow.

## Authorization for a device authorize grant request

The `POST /{{envID}}/as/device_authorization` request takes all configuration paramaters in the endpoint's request body. Parameters and their values are Form Serialized by adding the parameter names and values to the entity body of the HTTP request and specifying the `Content-Type: application/x-www-form-urlencoded` request header.

**Step 1:** Send an authorize request to the PingOne authorization server using `POST`.

```bash
curl --location --request POST '{{authPath}}/{{envID}}/as/device_authorization' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'client_id={{deviceAppID}}' \
--data-urlencode 'scope=openid'
```

The request requires the following properties:

* `client_id`: The application ID for an application that specifies the `device_code` grant type.

* `scope`: The permissions that specify accessible resources.

The response returns a `200 OK` message with the following properties:

```json
{
    "device_code": "96624b82-1469-46a9-a4f8-544970b62c37",
    "user_code": "GKHF-JQBC",
    "verification_uri": "https://auth.pingone.com/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/device",
    "verification_uri_complete": "https://auth.pingone.com/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/device?user_code=GKHF-JQBC",
    "expires_in": 600,
    "interval": 5
}
```

**Step 2:** Start the flow using `GET {{authPath}}/{{envID}}/device/{{appIdentifier}}` or `GET {{authPath}}/{{envID}}/device`.

|   |                                                                                                                                                                                                                                                                                                                                         |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The endpoint's `{{appIdentifier}}` value is set on the application configuration. This ID can be the PingOne application ID or another unique secondary identifier. When using the `/device` endpoint for a device authorization grant flow without the application identifier, the flow uses the environment's default sign-on policy. |

The response returns a `Location` HTTP header that specifies the URL for the sign-on screen and the flow ID.

**Step 3:** The sign-on flow calls the `POST /{{envID}}/flows/{{flowID}}` flow orchestration endpoints to prompt the end user to complete the actions required by the sign-on policy, and perform the following two device code actions: (1) confirm the device activation code, and (2) accept device authorization grant consent.

This flow action confirms the activation code:

```bash
curl --location --request POST '{{authPath}}/{{envID}}/flows/{{flowID}}' \
--header 'Content-Type: application/vnd.pingidentity.deviceAuthGrant.userCode.verify+json' \
--data-raw '{
    "userCode": "{{userCode}}"
}'
```

This flow action accepts consent:

```bash
curl --location --request POST '{{authPath}}/{{envID}}/flows/{{flowID}}' \
--header 'Content-Type: application/vnd.pingidentity.deviceAuthGrant.consent+json' \
--data-raw '{
	"accept": true
}'
```

**Step 4:** Call the token endpoint to exchange the device code for a token. Note that the `grant_type` parameter in the request body uses the IETF-specified syntax to identify the device code grant type (`urn:ietf:params:oauth:grant-type:device_code`).

```bash
curl --location --request POST '{{authPath}}/{{envID}}/as/token' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'grant_type=urn:ietf:params:oauth:grant-type:device_code' \
--data-urlencode 'device_code={{deviceCode}}' \
--data-urlencode 'client_id={{deviceAppID}}'
```

|   |                                                                                                                                                                   |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | In the token request above, the application's configuration has the `tokenEndpointAuthMethod` set to `NONE`. In this case, no `Authorization` header is required. |

For more information about the endpoints used in a device authorization grant flow, refer to [Device Authorization Grant](../../../auth/openid-connect-oauth-2/device-authorization-grant/index.html) and [Device Authorization Grant Flows](../../../auth/flows/index.html#device-authorization-grant-flows) in the *Platform Auth APIs*.