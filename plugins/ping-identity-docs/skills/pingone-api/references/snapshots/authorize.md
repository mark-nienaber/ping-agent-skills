---
title: API Access Management
description: The PingOne Authorize API access management service provides tools to externalize the management and evaluation of access control policies for HTTP-based APIs. The access control policies defined in the API Service configuration are enforced through an API gateway, which delegates policy evaluation using a Ping Identity-provided integration kit that connects with the PingOne API.
component: pingone-api
page_id: pingone-api:authorize:api-access-management
canonical_url: https://developer.pingidentity.com/pingone-api/authorize/api-access-management.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
---

# API Access Management

The PingOne Authorize API access management service provides tools to externalize the management and evaluation of access control policies for HTTP-based APIs. The access control policies defined in the API Service configuration are enforced through an API gateway, which delegates policy evaluation using a Ping Identity-provided integration kit that connects with the PingOne API.

The integration kit installed in your API gateway authenticates to PingOne. You configure a gateway and obtain a gateway credential. This credential is used to configure the API gateway integration kit. For more information, refer to [PingOne Authorize API Gateway Integration Kits](https://docs.pingidentity.com/pingone/authorization_using_pingone_authorize/p1az_api_gateway_is.html).

To create a gateway resource, refer to [Create API Gateway Integration](../platform/gateway-management/gateways/create-api-gateway-integration.html). In addition, API access management also uses the gateways credentials service. For more information, refer to [Gateway Credentials](../platform/gateway-management/gateway-credentials.html).

---

---
title: API Operations
description: The PingOne /v1/environments/{{envID}}/apiServers/{{apiServerID}}/operations endpoint provides operations to create, read, update, and delete API service operations in PingOne. Each operation is defined by one or more paths, and each path must have a unique pattern.
component: pingone-api
page_id: pingone-api:authorize:api-access-management/api-operations
canonical_url: https://developer.pingidentity.com/pingone-api/authorize/api-access-management/api-operations.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  path-parameter-pattern-syntax: Path parameter pattern syntax
  assigning-admin-roles-and-permissions-to-this-service: Assigning admin roles and permissions to this service
  api-server-operations-data-model: API service operations data model
  response-codes: Response codes
---

# API Operations

The PingOne `/v1/environments/{{envID}}/apiServers/{{apiServerID}}/operations` endpoint provides operations to create, read, update, and delete API service operations in PingOne. Each operation is defined by one or more paths, and each path must have a unique pattern.

## Path parameter pattern syntax

If a path pattern has a type of `PARAMETER`, the following syntax rules apply to the parameter expression:

* The pattern must start with a slash.

* A single `*` (wildcard) matches any character except a `/`.

* A double `**` matches the rest of the path. It cannot be followed by any characters in the pattern.

* A path segment can be matched using a named parameter, with syntax like `/{variable}`.

* Nested named parameters are not allowed, meaning `{name1{name2}}` is an invalid expression.

* Partial path segment matches are not allowed, meaning `/part1{part2}` is an invalid expression.

* A literal left curly bracket, right curly bracket, backslash, or wildcard can be matched by preceding the character with a backslash: `\{, \{, \\, \*`.

* The following characters are not allowed in parameter names: `'{', '}', '\', '/'`.

* Parameter names must be unique within an expression, meaning `/{name1}/resource/{name1}` is an invalid expression.

* ASCII control characters are invalid anywhere in the pattern.

## Assigning admin roles and permissions to this service

Admin role assignments determine access to PingOne APIs. When assigning admin roles to this service, refer to [PingOne Permissions by Service](../../platform/reference/roles-and-permissions-in-pingone/permissions-by-service.html) for the service-specific permissions.

You can also choose to assign admin roles based on particular service resources. Refer to [PingOne Permissions by Resource](../../platform/reference/roles-and-permissions-in-pingone/permissions-by-resource.html) when assigning admin roles per service resources.

Admin assignments to roles are set by:

* [Automatic assignment for some roles](../../platform/roles/predefined-roles.html#automatic-role-assignment).

* [Group Role Assignments](../../platform/group-role-assignments/group-role-assignments.html).

* [User Role Assignments](../../platform/users/user-role-assignments.html).

Refer to [Roles Management](../../platform/roles.html) for more information.

## API service operations data model

| Property                                         | Type         | Required | Mutable   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| ------------------------------------------------ | ------------ | -------- | --------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `id`                                             | String       | N/A      | Read-only | The ID of the API service operation. This is randomly generated when the operation is created.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `name`                                           | String       | Required | Mutable   | The name of the API service operation.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `accessControl`                                  | Object       | Optional | Mutable   | The access control configuration for the operation.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| `accessControl.authentication`                   | Object       | Optional | Mutable   | Defines the authentication requirements for this operation. One or both of the `acrs` or `maxAge` fields must be provided.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| `accessControl.authentication.acrs`              | Array        | Optional | Mutable   | The `acrs` array is currently limited to a single entry.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| `accessControl.authentication.acrs.element`      | Object       | Required | Mutable   | The relationship reference to a PingOne authentication policy.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `accessControl.authentication.acrs.element.id`   | String       | Required | Mutable   | The ID of the authentication policy.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `accessControl.authentication.acrs.element.type` | String       | Required | Mutable   | Identifies the authentication policy type. Valid values are `PINGONE`, which identifies a sign-on policy, and `DAVINCI`, which identifies a flow policy.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| `accessControl.authentication.maxAge`            | Number       | Optional | Mutable   | Specifies the maximum acceptable time in seconds since the user was last authenticated. If provided, the value must be a nonzero positive integer.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `accessControl.group`                            | Object       | Optional | Mutable   | The group membership requirements for the operation. The `groups` array must be non-empty when the `group` object is included. The `groups` array must not contain more than 25 elements.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `accessControl.group.groups`                     | Array        | Required | Mutable   | The list of groups that define the access requirements for the operation. The end user must be a member of one or more of these groups to gain access to the operation. This is a required property if `accessControl.group` is set. The ID must reference a group that exists at the time the data is persisted. There is no referential integrity between a group and this configuration. If a group is subsequently deleted, the access control configuration will continue to reference that group.                                                                                                                                                                                                                                                                                                                                                                                                                |
| `accessControl.group.groups.element`             | Relationship | Required | Mutable   | The ID of the group, wrapped in an object, for future extensibility. This is a required property if `operations.value.accessControl.group` is set.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `accessControl.group.groups.element.id`          | String       | Required | Read-only | A UUID that specifies the group ID. This is a required property if `accessControl.group` is set.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `accessControl.permission`                       | Object       | Optional | Mutable   | Defines the application permission requirements for the operation.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `accessControl.permission.id`                    | string       | Required | Mutable   | An application permission ID that defines the access requirements for the operation. The end user must be entitled to the specified application permission to gain access to the operation. This is a required property if `accessControl.permission` is set.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `accessControl.scope`                            | Object       | Optional | Mutable   | Defines the scope membership requirements for the operation.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `accessControl.scope.matchType`                  | String       | Optional | Mutable   | An enumeration defining the match type of the scope rule. `ALL` means the client must be authorized with all scopes configured in the `scopes` array to obtain access. `ANY` means the client must be authorized with one or more of the scopes.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `accessControl.scope.scopes`                     | Array        | Required | Mutable   | A list of scopes that define the access requirements for the operation. The client must be authorized with `ANY` or `ALL` of the scopes to be granted access, depending on the `matchType` configuration.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `accessControl.scope.scopes.element`             | Object       | Required | Mutable   | The relationship reference to a PingOne scope.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `accessControl.scope.scopes.element.id`          | String       | Required | Read-only | The ID of the scope.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `methods`                                        | Array        | Optional | Mutable   | The methods that define the operation. No duplicates are allowed. Each element must be a valid HTTP token, according to [RFC 7230](https://datatracker.ietf.org/doc/html/rfc7230), and cannot exceed 64 characters. An empty array is not valid. To indicate that an operation is defined for every method, the `methods` array should be set to null. The `methods` array is limited to 10 entries.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `methods.element`                                | String       | Optional | Mutable   | The name of the HTTP method. This value is case-sensitive.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| `paths`                                          | Array        | Required | Mutable   | The paths that define the operation. The same literal pattern is not allowed within the same operation (the pattern of a `paths` element must be unique as compared to all other patterns in the same `paths` array). However, the same literal pattern is allowed in different operations (for example, OperationA, `/path1`, OperationB, `/path1` is valid). The `paths` array is limited to 10 entries.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| `paths.element`                                  | Object       | Required | Mutable   | The defined pattern that identifies the parent operation.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `paths.element.pattern`                          | String       | Required | Mutable   | The pattern used to identify the path or paths for the operation. The semantics of the pattern are determined by the type. For any type, the pattern can contain characters that are otherwise invalid in a URL path. Invalid characters are handled by performing matching against a percent-decoded HTTP request target path. This allows an administrator to configure patterns without worrying about percent encoding special characters. When the `type` is `PARAMETER`, the syntax outlined in the table below is enforced. Additionally, the pattern must contain a wildcard, double wildcard or named parameter. When the `type` is `EXACT`, the pattern can be any byte sequence except for ASCII control characters such as line feeds or carriage returns. The length of the pattern cannot exceed 2048 characters. The path pattern must not contain empty path segments such as `/../`, `//`, and `/./`. |
| `paths.element.type`                             | String       | Required | Mutable   | The type of the pattern. Options are `EXACT` (the verbatim pattern is compared against the path from the request using a case-sensitive comparison) and `PARAMETER` (the pattern is compared against the path from the request using a case-sensitive comparison, using the syntax below to encode wildcards and named parameters).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| `policy.id`                                      | String       | Optional | Read-only | The ID of the root policy.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |

## Response codes

| Code | Message                                                               |
| ---- | --------------------------------------------------------------------- |
| 200  | Successful operation.                                                 |
| 201  | Successfully created.                                                 |
| 204  | Successfully removed. No content.                                     |
| 400  | The request could not be completed.                                   |
| 401  | You do not have access to this resource.                              |
| 403  | You do not have permissions or are not licensed to make this request. |
| 404  | The requested resource was not found.                                 |

---

---
title: API Services
description: The PingOne /v1/environments/{{envID}}/apiServers endpoint provides operations to create, read, update, and delete API services in PingOne. An API service models a customer's APIs, which are then protected by the PingOne API access management service.
component: pingone-api
page_id: pingone-api:authorize:api-access-management/api-services
canonical_url: https://developer.pingidentity.com/pingone-api/authorize/api-access-management/api-services.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  assigning-admin-roles-and-permissions-to-this-service: Assigning admin roles and permissions to this service
  api-server-data-model: API service data model
  path-parameter-pattern-syntax: Path parameter pattern syntax
  api-server-limit-filter-data: Limiting and filtering data
  response-codes: Response codes
---

# API Services

The PingOne `/v1/environments/{{envID}}/apiServers` endpoint provides operations to create, read, update, and delete API services in PingOne. An API service models a customer's APIs, which are then protected by the PingOne API access management service.

|   |                                                              |
| - | ------------------------------------------------------------ |
|   | PingOne enforces a limit of 25 API services per environment. |

## Assigning admin roles and permissions to this service

Admin role assignments determine access to PingOne APIs. When assigning admin roles to this service, refer to [PingOne Permissions by Service](../../platform/reference/roles-and-permissions-in-pingone/permissions-by-service.html) for the service-specific permissions.

You can also choose to assign admin roles based on particular service resources. Refer to [PingOne Permissions by Resource](../../platform/reference/roles-and-permissions-in-pingone/permissions-by-resource.html) when assigning admin roles per service resources.

Admin assignments to roles are set by:

* [Automatic assignment for some roles](../../platform/roles/predefined-roles.html#automatic-role-assignment).

* [Group Role Assignments](../../platform/group-role-assignments/group-role-assignments.html).

* [User Role Assignments](../../platform/users/user-role-assignments.html).

Refer to [Roles Management](../../platform/roles.html) for more information.

## API service data model

| Property                                           | Type         | Required | Mutable   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| -------------------------------------------------- | ------------ | -------- | --------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `accessControl.custom`                             | Object       | Optional | Mutable   | Defines if the operation will use custom policy rather than the "Group" or "Scope" `accessControl` requirement.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `accessControl.custom.enabled`                     | Boolean      | Optional | Mutable   | If `TRUE`, custom policy will be used for the endpoint. Defaults to `FALSE`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| `authorizationServer`                              | Object       | Required | Mutable   | A container for properties related to the authorization server that will issue access tokens used to access the APIs.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| `authorizationServer.externalOAuthServer`          | Object       | Optional | Mutable   | A container object for fields related to the API service's external OAuth 2 authorization server. Must not be provided if `authorizationServer.type` is `PINGONE_SSO`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `authorizationServer.externalOAuthServer.audience` | String       | Required | Mutable   | The expected audience for incoming access tokens issued by the External OAuth Server. The runtime will reject bearer tokens not issued for this audience by checking for a matching value in the aud claim. The maximum length is 1024.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| `authorizationServer.externalOAuthServer.id`       | UUID         | Required | Mutable   | The ID of the related External OAuth Server.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| `authorizationServer.resource`                     | Relationship | Required | Mutable   | The resource defines the characteristics of the OAuth 2.0 access tokens used to get access to the APIs on the API service such as the audience and scopes. Must not be provided if `authorizationServer.type` is `EXTERNAL`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| `authorizationServer.resource.id`                  | String       | Required | Mutable   | The UUID of the custom PingOne resource. This property must identify a PingOne resource with a `type` property value of `CUSTOM`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `authorizationServer.type`                         | String       | Optional | Mutable   | The type of authorization server that will issue access tokens. Valid options are `PINGONE_SSO` or `EXTERNAL`. Defaults to `PINGONE_SSO`. Must be the same value as the `directory.type`. If `PINGONE_SSO`, the `authorizationServer.externalOAuthServer` field must not be provided. If `EXTERNAL`, the `authorizationServer.resource` field must not be provided.                                                                                                                                                                                                                                                                                                                                                        |
| `baseUrls`                                         | Array        | Required | Mutable   | The possible base URLs that an end-user will use to access the APIs hosted on the customer's API service. Multiple base URLs may be specified to support cases where the same API may be available from multiple URLs (for example, from a user-friendly domain URL and an internal domain URL). Base URLs must be valid absolute URLs with the `https` or `http` scheme. If the path component is non-empty, it must not end in a trailing slash. The path must not contain empty backslash, dot, or double-dot segments. It must not have a query or fragment present, and the host portion of the authority must be a DNS hostname or valid IP (IPv4 or IPv6). The length must be less than or equal to 256 characters. |
| `directory`                                        | Object       | Optional | Mutable   | A container object for fields related to the user directory used to issue access tokens for accessing the APIs. If not provided, the `directory.type` will default to `PINGONE_SSO`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `directory.type`                                   | String       | Required | Mutable   | The type of directory that will be used to issue access tokens. Valid options are `PINGONE_SSO` or `EXTERNAL`. Defaults to `PINGONE_SSO`. Must be the same value as the `authorizationServer.type`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| `id`                                               | String       | Optional | Mutable   | The resource's unique identifier.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `name`                                             | String       | Required | Mutable   | The API service resource name. The `name` value must be unique among all API services, and it must be a valid resource name.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| `policy.id`                                        | String       | Optional | Read-only | The ID of the root policy.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |

### Path parameter pattern syntax

If a path pattern has a type of `PARAMETER`, the following syntax rules apply to the parameter expression:

* The pattern must start with a slash.

* A single `*` (wildcard) matches any character except a `/`.

* A double `**` matches the rest of the path. It cannot be followed by any characters in the pattern.

* A path segment can be captured with syntax like `/{variable}`.

* Nested captures are not allowed, meaning `{name1{name2}}` is an invalid expression.

* Partial path segment matches are not allowed, meaning `/part1{part2}` is an invalid expression.

* A literal left curly bracket, right curly bracket, backslash, or wildcard can be matched by preceding the character with a backslash: `\{, \{, \\, \*`.

* The following characters are not allowed in parameter names: `'{', '}', '\', '/'`.

* Parameter names must be unique within an expression, meaning `/{name1}/resource/{name1}` is an invalid expression.

* ASCII control characters are invalid anywhere in the pattern.

## Limiting and filtering data

You can limit the number of results returned on the [Read API Services](api-services/read-api-servers.html) request with the `limit` parameter. Refer to [Paging and ordering collections](../../platform/reference/paging-ordering-collections.html) for more information about use of the `limit` parameter, as well as other methods of controlling pagination.

You can filter response data by applying a SCIM filtering expression to the [Read API Services](api-services/read-api-servers.html) request. These SCIM operators can be applied to the following attributes:

* `eq` (equals)

  Supported attributes: `authorizationServer.externalOAuthServer.id`

## Response codes

| Code | Message                                                               |
| ---- | --------------------------------------------------------------------- |
| 200  | Successful operation.                                                 |
| 201  | Successfully created.                                                 |
| 204  | Successfully removed. No content.                                     |
| 400  | The request could not be completed.                                   |
| 401  | You do not have access to this resource.                              |
| 403  | You do not have permissions or are not licensed to make this request. |
| 404  | The requested resource was not found.                                 |

---

---
title: Application Permissions
description: The PingOne Authorize application resources and roles service provides endpoints to define custom roles and permissions within PingOne to protect external application resources.
component: pingone-api
page_id: pingone-api:authorize:application-permissions
canonical_url: https://developer.pingidentity.com/pingone-api/authorize/application-permissions.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
---

# Application Permissions

The PingOne Authorize application resources and roles service provides endpoints to define custom roles and permissions within PingOne to protect external application resources.

To create and manage application roles and permissions, see:

* [View application resources](application-permissions/application-resources.html)

  Provides endpoints to list the representations of external applications in PingOne. For create, update, and delete operations for application resources, refer to [Application resources](application-permissions/application-resources.html).

* [Application resource permissions](application-permissions/application-resource-permissions.html)

  Provides endpoints to define and manage permissions on the application resource.

* [Application roles](application-permissions/application-roles.html)

  Provides endpoints to define and manage application roles in PingOne. Roles contain application permissions. Application roles can be assigned to PingOne users.

* [Application role permissions](application-permissions/application-role-permissions.html)

  Provides endpoints to define and manage access control permissions, expected to be defined by a customer application developer. An application permission is comprised of an action and a protected resource, such as `read:accounts`. When a permission is added to a role, it creates a role entry. A subject assigned to a role is authorized for the permissions represented by the role's entries.

* [Application role assignments by role](application-permissions/application-role-assignments.html)

  Provides an endpoint to read application role assignments by role. The endpoint specifies a role ID in the request URL and the operation returns the role assignments associated with the identified role.

* [User application role assignments](../platform/users/user-application-role-assignments.html)

  Provides endpoints to define and manage application role assignments associated with user resources.

---

---
title: Application Resource Permissions
description: The PingOne Authorize {{apiPath}}/v1/environments/{{envID}}/applicationResources/{{appResourceID}}/permissions endpoint provides operations to create, read, update, and delete application resource permissions in PingOne.
component: pingone-api
page_id: pingone-api:authorize:application-permissions/application-resource-permissions
canonical_url: https://developer.pingidentity.com/pingone-api/authorize/application-permissions/application-resource-permissions.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  authorize-application-resources-permissions-data-model: Application resources permissions data model
  response-codes: Response codes
---

# Application Resource Permissions

The PingOne Authorize `{{apiPath}}/v1/environments/{{envID}}/applicationResources/{{appResourceID}}/permissions` endpoint provides operations to create, read, update, and delete application resource permissions in PingOne.

## Application resources permissions data model

| Property         | Type   | Required | Mutable   | Description                                                    |
| ---------------- | ------ | -------- | --------- | -------------------------------------------------------------- |
| `action`         | String | Required | Mutable   | The action associated with this permission.                    |
| `description`    | String | Optional | Mutable   | The resource's description.                                    |
| `environment.id` | String | N/A      | Read-only | The unique identifier for the associated environment.          |
| `id`             | String | N/A      | Read-only | The resource's unique identifier.                              |
| `key`            | String | N/A      | Read-only | The `resource.name:action` pair of the permission.             |
| `resource`       | Object | N/A      | Read-only | An object that identifies the associated application resource. |
| `resource.id`    | String | N/A      | Read-only | The ID for the associated application resource.                |
| `resource.name`  | String | N/A      | Read-only | The name of the associated application resource.               |

## Response codes

| Code | Message                                                               |
| ---- | --------------------------------------------------------------------- |
| 200  | Successful operation.                                                 |
| 201  | Successfully created.                                                 |
| 204  | Successfully removed. No content.                                     |
| 400  | The request could not be completed.                                   |
| 401  | You do not have access to this resource.                              |
| 403  | You do not have permissions or are not licensed to make this request. |
| 404  | The requested resource was not found.                                 |

---

---
title: Application Resources
description: The PingOne Authorize {{apiPath}}/v1/environments/{{envID}}/applicationResources endpoint provides operations to read application resources in PingOne. For information about create, update, and delete operations for application resources, refer to Create Application Resource, Update Application Resource, and Delete Application Resource.
component: pingone-api
page_id: pingone-api:authorize:application-permissions/application-resources
canonical_url: https://developer.pingidentity.com/pingone-api/authorize/application-permissions/application-resources.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  authorize-application-resources-data-model: API application resources data model
  response-codes: Response codes
---

# Application Resources

The PingOne Authorize `{{apiPath}}/v1/environments/{{envID}}/applicationResources` endpoint provides operations to read application resources in PingOne. For information about create, update, and delete operations for application resources, refer to [Create Application Resource](../../platform/resources/application-resources/create-application-resource.html), [Update Application Resource](../../platform/resources/application-resources/update-application-resource.html), and [Delete Application Resource](../../platform/resources/application-resources/delete-application-resource.html).

## API application resources data model

| Property      | Type   | Required | Mutable   | Description                                                              |
| ------------- | ------ | -------- | --------- | ------------------------------------------------------------------------ |
| `description` | String | Optional | Mutable   | The application resource's description.                                  |
| `id`          | String | N/A      | Read only | The resource's unique identifier.                                        |
| `name`        | String | Required | Mutable   | The application resource name. The `name` value must be unique.          |
| `parent`      | Object | Required | Read only | The application resource's parent.                                       |
| `parent.type` | String | Required | Read only | The application resource's parent type. Options are `PING_ONE_RESOURCE`. |
| `parent.id`   | String | Required | Read only | The application resource's parent ID.                                    |

## Response codes

| Code | Message                                                               |
| ---- | --------------------------------------------------------------------- |
| 200  | Successful operation.                                                 |
| 201  | Successfully created.                                                 |
| 204  | Successfully removed. No content.                                     |
| 400  | The request could not be completed.                                   |
| 401  | You do not have access to this resource.                              |
| 403  | You do not have permissions or are not licensed to make this request. |
| 404  | The requested resource was not found.                                 |

---

---
title: Application Role Assignments
description: The PingOne Authorize`{{apiPath}}/v1/environments/{{envID}}/applicationRoles/{{appRoleID}}/assignments` endpoint provides operations to read application role assignments in PingOne.
component: pingone-api
page_id: pingone-api:authorize:application-permissions/application-role-assignments
canonical_url: https://developer.pingidentity.com/pingone-api/authorize/application-permissions/application-role-assignments.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  application-role-assignments-data-model: Appliction role assignments data model
  response-codes: Response codes
---

# Application Role Assignments

The PingOne Authorize\`{{apiPath}}/v1/environments/{{envID}}/applicationRoles/{{appRoleID}}/assignments\` endpoint provides operations to read application role assignments in PingOne.

## Appliction role assignments data model

| Property  | Type   | Required | Mutable   | Description                                                                                   |
| --------- | ------ | -------- | --------- | --------------------------------------------------------------------------------------------- |
| `id`      | String | N/A      | Read-only | The ID of the API server operation. This is randomly generated when the operation is created. |
| `role`    | Object | N/A      | Read only | The role associated with the role assignment.                                                 |
| `subject` | Object | N/A      | Read only | The user associated with the role assignment.                                                 |

## Response codes

| Code | Message                                                               |
| ---- | --------------------------------------------------------------------- |
| 200  | Successful operation.                                                 |
| 400  | The request could not be completed.                                   |
| 401  | You do not have access to this resource.                              |
| 403  | You do not have permissions or are not licensed to make this request. |
| 404  | The requested resource was not found.                                 |

---

---
title: Application Role Permissions
description: The PingOne Authorize {{apiPath}}/v1/environments/{{envID}}/applicationRoles/{{appRoleID}}/permissions endpoint provides operations to add, read, and delete the permissions associated with application roles.
component: pingone-api
page_id: pingone-api:authorize:application-permissions/application-role-permissions
canonical_url: https://developer.pingidentity.com/pingone-api/authorize/application-permissions/application-role-permissions.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  application-roles-permissions-data-model: Application roles permissions data model
  response-codes: Response codes
---

# Application Role Permissions

The PingOne Authorize `{{apiPath}}/v1/environments/{{envID}}/applicationRoles/{{appRoleID}}/permissions` endpoint provides operations to add, read, and delete the permissions associated with application roles.

## Application roles permissions data model

| Property        | Type   | Required | Mutable   | Description                                                    |
| --------------- | ------ | -------- | --------- | -------------------------------------------------------------- |
| `action`        | String | N/A      | Read-only | The action associated with this permission.                    |
| `description`   | String | N/A      | Read-only | The permission description.                                    |
| `id`            | String | N/A      | Read-only | The permission's unique identifier.                            |
| `key`           | String | N/A      | Read-only | The `resource.name:action` pair of the permission.             |
| `resource`      | Object | N/A      | Read-only | An object that identifies the associated application resource. |
| `resource.id`   | String | N/A      | Read-only | The ID of the resource associated with this role.              |
| `resource.name` | String | N/A      | Read-only | The name of the resource associated with this role.            |

## Response codes

| Code | Message                                                               |
| ---- | --------------------------------------------------------------------- |
| 200  | Successful operation.                                                 |
| 201  | Successfully created.                                                 |
| 204  | Successfully removed. No content.                                     |
| 400  | The request could not be completed.                                   |
| 401  | You do not have access to this resource.                              |
| 403  | You do not have permissions or are not licensed to make this request. |
| 404  | The requested resource was not found.                                 |

---

---
title: Application Roles
description: The PingOne Authorize {{apiPath}}/v1/environments/{{envID}}/applicationRoles endpoint provides operations to create, read, update, and delete application roles in PingOne.
component: pingone-api
page_id: pingone-api:authorize:application-permissions/application-roles
canonical_url: https://developer.pingidentity.com/pingone-api/authorize/application-permissions/application-roles.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  application-roles-data-model: Application roles data model
  response-codes: Response codes
---

# Application Roles

The PingOne Authorize `{{apiPath}}/v1/environments/{{envID}}/applicationRoles` endpoint provides operations to create, read, update, and delete application roles in PingOne.

## Application roles data model

| Property      | Type   | Required | Mutable   | Description                              |
| ------------- | ------ | -------- | --------- | ---------------------------------------- |
| `description` | String | Optoinal | Mutable   | The description of the application role. |
| `id`          | String | N/A      | Read-only | The ID of the application role.          |
| `name`        | String | Required | Mutable   | The name of the application role.        |

## Response codes

| Code | Message                                                               |
| ---- | --------------------------------------------------------------------- |
| 200  | Successful operation.                                                 |
| 201  | Successfully created.                                                 |
| 204  | Successfully removed. No content.                                     |
| 400  | The request could not be completed.                                   |
| 401  | You do not have access to this resource.                              |
| 403  | You do not have permissions or are not licensed to make this request. |
| 404  | The requested resource was not found.                                 |

---

---
title: Authorization Decisions
description: The PingOne Authorize decision service provides:
component: pingone-api
page_id: pingone-api:authorize:authorization-decisions
canonical_url: https://developer.pingidentity.com/pingone-api/authorize/authorization-decisions.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
---

# Authorization Decisions

The PingOne Authorize decision service provides:

**Decision evaluation**

* Runtime evaluation of decision requests against a given policy decision resource. For more information, refer to [Decision Evaluation](authorization-decisions/decision-evaluation.html)

**Decision endpoint management**

* Creation of decision endpoints that allow efficient evaluation of policies developed in the PingOneAuthorize Policy Editor Service.

* Control over which version of the policies are deployed to each decision endpoint, giving your organization control over how and when policies are rolled out.

For more information, refer to [Decision Endpoints](authorization-decisions/decision-endpoints.html)

---

---
title: Authorize Gateway Decision Evaluation
description: Decision requests to an Authorize gateway instance are used to determine whether a user or system is permitted to perform a specific action.
component: pingone-api
page_id: pingone-api:authorize:authorize-gateways/authorize-gateway-decision-evaluation/authorize-gateway-decision-evaluation
canonical_url: https://developer.pingidentity.com/pingone-api/authorize/authorize-gateways/authorize-gateway-decision-evaluation/authorize-gateway-decision-evaluation.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
---

# Authorize Gateway Decision Evaluation

Decision requests to an Authorize gateway instance are used to determine whether a user or system is permitted to perform a specific action.

The decision evaluation endpoints for Authorize gateway instances can handle individual and bulk decision requests.

See the following API examples:

* [Evaluate an Individual Decision Request](evaluate-an-individual-decision-request/create-an-individual-decision-request.html) for evaluating a single decision request that includes a set of parameters and optional PingOne user context.

* [Evaluate a Bulk Decision Request](evaluate-a-bulk-decision-request/create-a-bulk-decision-request.html) for evaluating an array of individual decision requests with a single API call. Bulk requests reduce latency and network overhead when you need to evaluate several access scenarios at once.

---

---
title: Authorize Gateways
description: Authorize gateways combine the advantages of centralized policy administration with the benefits of on-premise decision evaluation and enforcement.
component: pingone-api
page_id: pingone-api:authorize:authorize-gateways/authorize-gateways
canonical_url: https://developer.pingidentity.com/pingone-api/authorize/authorize-gateways/authorize-gateways.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
---

# Authorize Gateways

Authorize gateways combine the advantages of centralized policy administration with the benefits of on-premise decision evaluation and enforcement.

See the following topics for more information:

* [Authorize gateways](https://docs.pingidentity.com/pingone/integrations/p1_authz_gateways.html) in the PingOne admin documentation.

* [Authorize Gateway Decision Evaluation](authorize-gateway-decision-evaluation/authorize-gateway-decision-evaluation.html) provides the decision evaluation endpoints for Authorize gateway instances.

In addition, the PingOne gateway endpoints provide capabilities for Authorize gateway management.

See the following Authorize gateway examples:

* [Create Authorize gateway](../../platform/gateway-management/gateways/create-authorize-gateway.html)

* [Read All Authorize gateways](../../platform/gateway-management/gateways/read-all-authorize-gateways.html)

* [Read One Authorize gateway](../../platform/gateway-management/gateways/read-one-authorize-gateway.html)

* [Read All Authorize gateway Instances](../../platform/gateway-management/gateway-instances/read-all-authorize-gateway-instances.html)

* [Update Authorize gateway](../../platform/gateway-management/gateways/update-authorize-gateway.html)

---

---
title: Create API Server Operation
description: The POST {{apiPath}}/v1/environments/{{envID}}/apiServers/{{apiServerID}}/operations request creates a new API service operation associated with the environment and API service specified in the request URL.
component: pingone-api
page_id: pingone-api:authorize:api-access-management/api-operations/create-api-server-operation
canonical_url: https://developer.pingidentity.com/pingone-api/authorize/api-access-management/api-operations/create-api-server-operation.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  prerequisites: Prerequisites
  headers: Headers
  body: Body
  example-request: Example Request
  example-response: Example Response
---

# Create API Server Operation

##

```none
POST {{apiPath}}/v1/environments/{{envID}}/apiServers/{{apiServerID}}/operations
```

The `POST {{apiPath}}/v1/environments/{{envID}}/apiServers/{{apiServerID}}/operations` request creates a new API service operation associated with the environment and API service specified in the request URL.

### Prerequisites

* Refer to [PingOne Authorize API Access Management](../../api-access-management.html) for important overview information.

> **Collapse: Request Model**
>
> For property descriptions, refer to [API service operations data model](../api-operations.html#api-server-operations-data-model).
>
> | Property                                | Type         | Required |
> | --------------------------------------- | ------------ | -------- |
> | `accessControl`                         | Object       | Optional |
> | `accessControl.custom`                  | Object       | Optional |
> | `accessControl.custom.enabled`          | Boolean      | Optional |
> | `accessControl.group`                   | Object       | Optional |
> | `accessControl.group.groups`            | Array        | Required |
> | `accessControl.group.groups.element`    | Relationship | Required |
> | `accessControl.group.groups.element.id` | String       | Required |
> | `accessControl.permission`              | Object       | Optional |
> | `accessControl.permission.id`           | Object       | Optional |
> | `accessControl.scope`                   | Object       | Optional |
> | `accessControl.scope.matchType`         | String       | Optional |
> | `accessControl.scope.scopes`            | Array        | Required |
> | `accessControl.scope.scopes.element`    | Object       | Required |
> | `accessControl.scope.scopes.element.id` | String       | Required |
> | `methods`                               | Array        | Optional |
> | `name`                                  | String       | Required |
> | `paths`                                 | Array        | Required |
> | `paths.type`                            | String       | Required |
> | `paths.pattern`                         | String       | Required |

### Headers

Authorization      Bearer {{accessToken}}

Content-Type      application/json

### Body

raw ( application/json )

```json
{
    "name": "AccountsPayable",
    "paths": [
        {
            "type": "EXACT",
            "pattern": "/accountsPayable"
        }
    ],
    "methods": [
        "POST",
        "PUT"
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
curl --location --globoff '{{apiPath}}/v1/environments/{{envID}}/apiServers/{{apiServerID}}/operations' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {{accessToken}}' \
--data '{
    "name": "AccountsPayable",
    "paths": [
        {
            "type": "EXACT",
            "pattern": "/accountsPayable"
        }
    ],
    "methods": [
        "POST",
        "PUT"
    ]
}'
```

```csharp
var options = new RestClientOptions("{{apiPath}}/v1/environments/{{envID}}/apiServers/{{apiServerID}}/operations")
{
  MaxTimeout = -1,
};
var client = new RestClient(options);
var request = new RestRequest("", Method.Post);
request.AddHeader("Content-Type", "application/json");
request.AddHeader("Authorization", "Bearer {{accessToken}}");
var body = @"{" + "\n" +
@"    ""name"": ""AccountsPayable""," + "\n" +
@"    ""paths"": [" + "\n" +
@"        {" + "\n" +
@"            ""type"": ""EXACT""," + "\n" +
@"            ""pattern"": ""/accountsPayable""" + "\n" +
@"        }" + "\n" +
@"    ]," + "\n" +
@"    ""methods"": [" + "\n" +
@"        ""POST""," + "\n" +
@"        ""PUT""" + "\n" +
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

  url := "{{apiPath}}/v1/environments/{{envID}}/apiServers/{{apiServerID}}/operations"
  method := "POST"

  payload := strings.NewReader(`{
    "name": "AccountsPayable",
    "paths": [
        {
            "type": "EXACT",
            "pattern": "/accountsPayable"
        }
    ],
    "methods": [
        "POST",
        "PUT"
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
POST /v1/environments/{{envID}}/apiServers/{{apiServerID}}/operations HTTP/1.1
Host: {{apiPath}}
Content-Type: application/json
Authorization: Bearer {{accessToken}}

{
    "name": "AccountsPayable",
    "paths": [
        {
            "type": "EXACT",
            "pattern": "/accountsPayable"
        }
    ],
    "methods": [
        "POST",
        "PUT"
    ]
}
```

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("application/json");
RequestBody body = RequestBody.create(mediaType, "{\n    \"name\": \"AccountsPayable\",\n    \"paths\": [\n        {\n            \"type\": \"EXACT\",\n            \"pattern\": \"/accountsPayable\"\n        }\n    ],\n    \"methods\": [\n        \"POST\",\n        \"PUT\"\n    ]\n}");
Request request = new Request.Builder()
  .url("{{apiPath}}/v1/environments/{{envID}}/apiServers/{{apiServerID}}/operations")
  .method("POST", body)
  .addHeader("Content-Type", "application/json")
  .addHeader("Authorization", "Bearer {{accessToken}}")
  .build();
Response response = client.newCall(request).execute();
```

```javascript
var settings = {
  "url": "{{apiPath}}/v1/environments/{{envID}}/apiServers/{{apiServerID}}/operations",
  "method": "POST",
  "timeout": 0,
  "headers": {
    "Content-Type": "application/json",
    "Authorization": "Bearer {{accessToken}}"
  },
  "data": JSON.stringify({
    "name": "AccountsPayable",
    "paths": [
      {
        "type": "EXACT",
        "pattern": "/accountsPayable"
      }
    ],
    "methods": [
      "POST",
      "PUT"
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
  'url': '{{apiPath}}/v1/environments/{{envID}}/apiServers/{{apiServerID}}/operations',
  'headers': {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer {{accessToken}}'
  },
  body: JSON.stringify({
    "name": "AccountsPayable",
    "paths": [
      {
        "type": "EXACT",
        "pattern": "/accountsPayable"
      }
    ],
    "methods": [
      "POST",
      "PUT"
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

url = "{{apiPath}}/v1/environments/{{envID}}/apiServers/{{apiServerID}}/operations"

payload = json.dumps({
  "name": "AccountsPayable",
  "paths": [
    {
      "type": "EXACT",
      "pattern": "/accountsPayable"
    }
  ],
  "methods": [
    "POST",
    "PUT"
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
$request->setUrl('{{apiPath}}/v1/environments/{{envID}}/apiServers/{{apiServerID}}/operations');
$request->setMethod(HTTP_Request2::METHOD_POST);
$request->setConfig(array(
  'follow_redirects' => TRUE
));
$request->setHeader(array(
  'Content-Type' => 'application/json',
  'Authorization' => 'Bearer {{accessToken}}'
));
$request->setBody('{\n    "name": "AccountsPayable",\n    "paths": [\n        {\n            "type": "EXACT",\n            "pattern": "/accountsPayable"\n        }\n    ],\n    "methods": [\n        "POST",\n        "PUT"\n    ]\n}');
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

url = URI("{{apiPath}}/v1/environments/{{envID}}/apiServers/{{apiServerID}}/operations")

http = Net::HTTP.new(url.host, url.port);
request = Net::HTTP::Post.new(url)
request["Content-Type"] = "application/json"
request["Authorization"] = "Bearer {{accessToken}}"
request.body = JSON.dump({
  "name": "AccountsPayable",
  "paths": [
    {
      "type": "EXACT",
      "pattern": "/accountsPayable"
    }
  ],
  "methods": [
    "POST",
    "PUT"
  ]
})

response = http.request(request)
puts response.read_body
```

```swift
let parameters = "{\n    \"name\": \"AccountsPayable\",\n    \"paths\": [\n        {\n            \"type\": \"EXACT\",\n            \"pattern\": \"/accountsPayable\"\n        }\n    ],\n    \"methods\": [\n        \"POST\",\n        \"PUT\"\n    ]\n}"
let postData = parameters.data(using: .utf8)

var request = URLRequest(url: URL(string: "{{apiPath}}/v1/environments/{{envID}}/apiServers/{{apiServerID}}/operations")!,timeoutInterval: Double.infinity)
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
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/apiServers/a82aa1c1-1a8e-4b6e-a43e-2266ebd57626/operations/ad5d139a-c4b3-40d9-a030-29b393391ecc"
        },
        "environment": {
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
        },
        "apiServer": {
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/apiServers/a82aa1c1-1a8e-4b6e-a43e-2266ebd57626"
        }
    },
    "id": "ad5d139a-c4b3-40d9-a030-29b393391ecc",
    "name": "AccountsPayable",
    "methods": [
        "POST",
        "PUT"
    ],
    "paths": [
        {
            "type": "EXACT",
            "pattern": "/accountsPayable"
        }
    ]
}
```

---

---
title: Create API Service
description: The following sample shows the POST {{apiPath}}/v1/environments/{{envID}}/apiServers operation to create a new API service endpoint resource associated with the environment specified in the request URL. The request body specifies the name, baseUrls, and authorizationServer.resource.id value that specifies the UUID for a custom resource defined in PingOne.
component: pingone-api
page_id: pingone-api:authorize:api-access-management/api-services/create-api-server
canonical_url: https://developer.pingidentity.com/pingone-api/authorize/api-access-management/api-services/create-api-server.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  prerequisites: Prerequisites
  headers: Headers
  body: Body
  example-request: Example Request
  example-response: Example Response
---

# Create API Service

##

```none
POST {{apiPath}}/v1/environments/{{envID}}/apiServers
```

The following sample shows the `POST {{apiPath}}/v1/environments/{{envID}}/apiServers` operation to create a new API service endpoint resource associated with the environment specified in the request URL. The request body specifies the `name`, `baseUrls`, and `authorizationServer.resource.id` value that specifies the UUID for a custom resource defined in PingOne.

### Prerequisites

* Refer to [PingOne Authorize](../../../workflow-library/pingone-authorize.html) and [PingOne Authorize API Access Management](../../api-access-management.html) for important overview information.

* Use [Create Resource](../../../platform/resources/resources-1/create-resource.html) to create an authorization server resource entity for the `customP1ResourceID` variable. Use [Read All Resources](../../../platform/resources/resources-1/read-all-resources.html) to find an existing resource entity ID.

* Use [Create Group](../../../platform/groups/create-group.html) to create a user group for the optional `groupID` variable. Use [Read All Groups](../../../platform/groups/read-all-groups.html) to find an existing user group ID.

> **Collapse: Request Model**
>
> For property descriptions, refer to [API service data model](../api-services.html#api-server-data-model).
>
> | Property                                           | Type         | Required |
> | -------------------------------------------------- | ------------ | -------- |
> | `authorizationServer`                              | Object       | Required |
> | `authorizationServer.externalOAuthServer`          | Object       | Optional |
> | `authorizationServer.externalOAuthServer.audience` | String       | Required |
> | `authorizationServer.externalOAuthServer.id`       | String       | Required |
> | `authorizationServer.resource`                     | Relationship | Required |
> | `authorizationServer.resource.id`                  | UUID         | Required |
> | `authorizationServer.type`                         | String       | Optional |
> | `baseUrls`                                         | Array        | Required |
> | `name`                                             | String       | Required |

### Headers

Authorization      Bearer {{accessToken}}

Content-Type      application/json

### Body

raw ( application/json )

```json
{
    "name": "Banking API-Advanced",
    "baseUrls": [
        "https://api.example.com/advbanking/v1",
        "https://example-api.cdn/advbanking/v1"
    ],
    "authorizationServer": {
        "resource": {
            "id": "{{customP1ResourceID}}"
        }
    }
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
curl --location --globoff '{{apiPath}}/v1/environments/{{envID}}/apiServers' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {{accessToken}}' \
--data '{
    "name": "Banking API-Advanced",
    "baseUrls": [
        "https://api.example.com/advbanking/v1",
        "https://example-api.cdn/advbanking/v1"
    ],
    "authorizationServer": {
        "resource": {
            "id": "{{customP1ResourceID}}"
        }
    }
}'
```

```csharp
var options = new RestClientOptions("{{apiPath}}/v1/environments/{{envID}}/apiServers")
{
  MaxTimeout = -1,
};
var client = new RestClient(options);
var request = new RestRequest("", Method.Post);
request.AddHeader("Content-Type", "application/json");
request.AddHeader("Authorization", "Bearer {{accessToken}}");
var body = @"{" + "\n" +
@"    ""name"": ""Banking API-Advanced""," + "\n" +
@"    ""baseUrls"": [" + "\n" +
@"        ""https://api.example.com/advbanking/v1""," + "\n" +
@"        ""https://example-api.cdn/advbanking/v1""" + "\n" +
@"    ]," + "\n" +
@"    ""authorizationServer"": {" + "\n" +
@"        ""resource"": {" + "\n" +
@"            ""id"": ""{{customP1ResourceID}}""" + "\n" +
@"        }" + "\n" +
@"    }" + "\n" +
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

  url := "{{apiPath}}/v1/environments/{{envID}}/apiServers"
  method := "POST"

  payload := strings.NewReader(`{
    "name": "Banking API-Advanced",
    "baseUrls": [
        "https://api.example.com/advbanking/v1",
        "https://example-api.cdn/advbanking/v1"
    ],
    "authorizationServer": {
        "resource": {
            "id": "{{customP1ResourceID}}"
        }
    }
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
POST /v1/environments/{{envID}}/apiServers HTTP/1.1
Host: {{apiPath}}
Content-Type: application/json
Authorization: Bearer {{accessToken}}

{
    "name": "Banking API-Advanced",
    "baseUrls": [
        "https://api.example.com/advbanking/v1",
        "https://example-api.cdn/advbanking/v1"
    ],
    "authorizationServer": {
        "resource": {
            "id": "{{customP1ResourceID}}"
        }
    }
}
```

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("application/json");
RequestBody body = RequestBody.create(mediaType, "{\n    \"name\": \"Banking API-Advanced\",\n    \"baseUrls\": [\n        \"https://api.example.com/advbanking/v1\",\n        \"https://example-api.cdn/advbanking/v1\"\n    ],\n    \"authorizationServer\": {\n        \"resource\": {\n            \"id\": \"{{customP1ResourceID}}\"\n        }\n    }\n}");
Request request = new Request.Builder()
  .url("{{apiPath}}/v1/environments/{{envID}}/apiServers")
  .method("POST", body)
  .addHeader("Content-Type", "application/json")
  .addHeader("Authorization", "Bearer {{accessToken}}")
  .build();
Response response = client.newCall(request).execute();
```

```javascript
var settings = {
  "url": "{{apiPath}}/v1/environments/{{envID}}/apiServers",
  "method": "POST",
  "timeout": 0,
  "headers": {
    "Content-Type": "application/json",
    "Authorization": "Bearer {{accessToken}}"
  },
  "data": JSON.stringify({
    "name": "Banking API-Advanced",
    "baseUrls": [
      "https://api.example.com/advbanking/v1",
      "https://example-api.cdn/advbanking/v1"
    ],
    "authorizationServer": {
      "resource": {
        "id": "{{customP1ResourceID}}"
      }
    }
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
  'url': '{{apiPath}}/v1/environments/{{envID}}/apiServers',
  'headers': {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer {{accessToken}}'
  },
  body: JSON.stringify({
    "name": "Banking API-Advanced",
    "baseUrls": [
      "https://api.example.com/advbanking/v1",
      "https://example-api.cdn/advbanking/v1"
    ],
    "authorizationServer": {
      "resource": {
        "id": "{{customP1ResourceID}}"
      }
    }
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

url = "{{apiPath}}/v1/environments/{{envID}}/apiServers"

payload = json.dumps({
  "name": "Banking API-Advanced",
  "baseUrls": [
    "https://api.example.com/advbanking/v1",
    "https://example-api.cdn/advbanking/v1"
  ],
  "authorizationServer": {
    "resource": {
      "id": "{{customP1ResourceID}}"
    }
  }
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
$request->setUrl('{{apiPath}}/v1/environments/{{envID}}/apiServers');
$request->setMethod(HTTP_Request2::METHOD_POST);
$request->setConfig(array(
  'follow_redirects' => TRUE
));
$request->setHeader(array(
  'Content-Type' => 'application/json',
  'Authorization' => 'Bearer {{accessToken}}'
));
$request->setBody('{\n    "name": "Banking API-Advanced",\n    "baseUrls": [\n        "https://api.example.com/advbanking/v1",\n        "https://example-api.cdn/advbanking/v1"\n    ],\n    "authorizationServer": {\n        "resource": {\n            "id": "{{customP1ResourceID}}"\n        }\n    }\n}');
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

url = URI("{{apiPath}}/v1/environments/{{envID}}/apiServers")

http = Net::HTTP.new(url.host, url.port);
request = Net::HTTP::Post.new(url)
request["Content-Type"] = "application/json"
request["Authorization"] = "Bearer {{accessToken}}"
request.body = JSON.dump({
  "name": "Banking API-Advanced",
  "baseUrls": [
    "https://api.example.com/advbanking/v1",
    "https://example-api.cdn/advbanking/v1"
  ],
  "authorizationServer": {
    "resource": {
      "id": "{{customP1ResourceID}}"
    }
  }
})

response = http.request(request)
puts response.read_body
```

```swift
let parameters = "{\n    \"name\": \"Banking API-Advanced\",\n    \"baseUrls\": [\n        \"https://api.example.com/advbanking/v1\",\n        \"https://example-api.cdn/advbanking/v1\"\n    ],\n    \"authorizationServer\": {\n        \"resource\": {\n            \"id\": \"{{customP1ResourceID}}\"\n        }\n    }\n}"
let postData = parameters.data(using: .utf8)

var request = URLRequest(url: URL(string: "{{apiPath}}/v1/environments/{{envID}}/apiServers")!,timeoutInterval: Double.infinity)
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
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/apiServers/6cdedf90-f9e4-4c2e-b238-091adbb156fe"
        },
        "resource": {
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/resources/d8a56a22-caf3-4053-8221-298a12e013ab"
        },
        "operations": {
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/apiServers/6cdedf90-f9e4-4c2e-b238-091adbb156fe/operations"
        },
        "environment": {
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
        }
    },
    "environment": {
        "id": "abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
    },
    "id": "6cdedf90-f9e4-4c2e-b238-091adbb156fe",
    "name": "Banking API-Advanced",
    "baseUrls": [
        "https://api.example.com/advbanking/v1",
        "https://example-api.cdn/advbanking/v1"
    ],
    "authorizationServer": {
        "resource": {
            "id": "d8a56a22-caf3-4053-8221-298a12e013ab"
        },
        "type": "PINGONE_SSO"
    },
    "directory": {
        "type": "PINGONE_SSO"
    }
}
```

---

---
title: Create Application Permissions
description: The following sample shows the POST {{apiPath}}/v1/environments/{{envID}}/applicationResources/{{appResourceID}}/permissions operation to create a new application resource permission. The request body specifies the action`and an optional `description.
component: pingone-api
page_id: pingone-api:authorize:application-permissions/application-resource-permissions/create-application-permissions
canonical_url: https://developer.pingidentity.com/pingone-api/authorize/application-permissions/application-resource-permissions/create-application-permissions.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  prerequisites: Prerequisites
  headers: Headers
  body: Body
  example-request: Example Request
  example-response: Example Response
---

# Create Application Permissions

##

```none
POST {{apiPath}}/v1/environments/{{envID}}/applicationResources/{{appResourceID}}/permissions
```

The following sample shows the `POST {{apiPath}}/v1/environments/{{envID}}/applicationResources/{{appResourceID}}/permissions` operation to create a new application resource permission. The request body specifies the ``action`and an optional `description``.

### Prerequisites

* Use [Create Application Resource](../../../platform/resources/application-resources/create-application-resource.html) to create an application resource ID for the `{{appResourceID}}` variable. Use [Read All Application Resources](../../../platform/resources/application-resources/read-application-resources.html) to find an existing application resource entity ID.

> **Collapse: Request Model**
>
> For complete descriptions, refer to [Application resources permissions data model](../application-resource-permissions.html#authorize-application-resources-permissions-data-model).
>
> | Property      | Type   | Required |
> | ------------- | ------ | -------- |
> | `action`      | String | Required |
> | `description` | String | Optional |

### Headers

Authorization      Bearer {{accessToken}}

Content-Type      application/json

### Body

raw ( application/json )

```json
{
    "action": "write",
    "description": "Update documents"
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
curl --location --globoff '{{apiPath}}/v1/environments/{{envID}}/applicationResources/{{appResourceID}}/permissions' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {{accessToken}}' \
--data '{
    "action": "write",
    "description": "Update documents"
}'
```

```csharp
var options = new RestClientOptions("{{apiPath}}/v1/environments/{{envID}}/applicationResources/{{appResourceID}}/permissions")
{
  MaxTimeout = -1,
};
var client = new RestClient(options);
var request = new RestRequest("", Method.Post);
request.AddHeader("Content-Type", "application/json");
request.AddHeader("Authorization", "Bearer {{accessToken}}");
var body = @"{" + "\n" +
@"    ""action"": ""write""," + "\n" +
@"    ""description"": ""Update documents""" + "\n" +
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

  url := "{{apiPath}}/v1/environments/{{envID}}/applicationResources/{{appResourceID}}/permissions"
  method := "POST"

  payload := strings.NewReader(`{
    "action": "write",
    "description": "Update documents"
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
POST /v1/environments/{{envID}}/applicationResources/{{appResourceID}}/permissions HTTP/1.1
Host: {{apiPath}}
Content-Type: application/json
Authorization: Bearer {{accessToken}}

{
    "action": "write",
    "description": "Update documents"
}
```

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("application/json");
RequestBody body = RequestBody.create(mediaType, "{\n    \"action\": \"write\",\n    \"description\": \"Update documents\"\n}");
Request request = new Request.Builder()
  .url("{{apiPath}}/v1/environments/{{envID}}/applicationResources/{{appResourceID}}/permissions")
  .method("POST", body)
  .addHeader("Content-Type", "application/json")
  .addHeader("Authorization", "Bearer {{accessToken}}")
  .build();
Response response = client.newCall(request).execute();
```

```javascript
var settings = {
  "url": "{{apiPath}}/v1/environments/{{envID}}/applicationResources/{{appResourceID}}/permissions",
  "method": "POST",
  "timeout": 0,
  "headers": {
    "Content-Type": "application/json",
    "Authorization": "Bearer {{accessToken}}"
  },
  "data": JSON.stringify({
    "action": "write",
    "description": "Update documents"
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
  'url': '{{apiPath}}/v1/environments/{{envID}}/applicationResources/{{appResourceID}}/permissions',
  'headers': {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer {{accessToken}}'
  },
  body: JSON.stringify({
    "action": "write",
    "description": "Update documents"
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

url = "{{apiPath}}/v1/environments/{{envID}}/applicationResources/{{appResourceID}}/permissions"

payload = json.dumps({
  "action": "write",
  "description": "Update documents"
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
$request->setUrl('{{apiPath}}/v1/environments/{{envID}}/applicationResources/{{appResourceID}}/permissions');
$request->setMethod(HTTP_Request2::METHOD_POST);
$request->setConfig(array(
  'follow_redirects' => TRUE
));
$request->setHeader(array(
  'Content-Type' => 'application/json',
  'Authorization' => 'Bearer {{accessToken}}'
));
$request->setBody('{\n    "action": "write",\n    "description": "Update documents"\n}');
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

url = URI("{{apiPath}}/v1/environments/{{envID}}/applicationResources/{{appResourceID}}/permissions")

http = Net::HTTP.new(url.host, url.port);
request = Net::HTTP::Post.new(url)
request["Content-Type"] = "application/json"
request["Authorization"] = "Bearer {{accessToken}}"
request.body = JSON.dump({
  "action": "write",
  "description": "Update documents"
})

response = http.request(request)
puts response.read_body
```

```swift
let parameters = "{\n    \"action\": \"write\",\n    \"description\": \"Update documents\"\n}"
let postData = parameters.data(using: .utf8)

var request = URLRequest(url: URL(string: "{{apiPath}}/v1/environments/{{envID}}/applicationResources/{{appResourceID}}/permissions")!,timeoutInterval: Double.infinity)
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
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/applicationResources/9fc45050-4e39-4f98-9de5-dbff01659a14/permissions/47ab2789-3f3d-4f25-b5bf-efc9f8d363b1"
        },
        "environment": {
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
        },
        "resource": {
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/applicationResources/9fc45050-4e39-4f98-9de5-dbff01659a14"
        }
    },
    "environment": {
        "id": "abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
    },
    "id": "47ab2789-3f3d-4f25-b5bf-efc9f8d363b1",
    "action": "write",
    "resource": {
        "id": "9fc45050-4e39-4f98-9de5-dbff01659a14",
        "name": "portfolios"
    },
    "description": "Update documents",
    "key": "portfolios:write"
}
```

---

---
title: Create Application Role
description: The POST {{apiPath}}/v1/environments/{{envID}}/applicationRoles request creates a new application role.
component: pingone-api
page_id: pingone-api:authorize:application-permissions/application-roles/create-application-role
canonical_url: https://developer.pingidentity.com/pingone-api/authorize/application-permissions/application-roles/create-application-role.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  headers: Headers
  body: Body
  example-request: Example Request
  example-response: Example Response
---

# Create Application Role

##

```none
POST {{apiPath}}/v1/environments/{{envID}}/applicationRoles
```

The `POST {{apiPath}}/v1/environments/{{envID}}/applicationRoles` request creates a new application role.

> **Collapse: Request Model**
>
> For property descriptions, refer to [Application roles data model](../application-roles.html#application-roles-data-model).
>
> | Property      | Type   | Required |
> | ------------- | ------ | -------- |
> | `name`        | String | Required |
> | `description` | String | Optional |

### Headers

Authorization      Bearer {{accessToken}}

Content-Type      application/json

### Body

raw ( application/json )

```json
{
    "name": "CEO",
    "description": "The CEO"
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
curl --location --globoff '{{apiPath}}/v1/environments/{{envID}}/applicationRoles' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {{accessToken}}' \
--data '{
    "name": "CEO",
    "description": "The CEO"
}'
```

```csharp
var options = new RestClientOptions("{{apiPath}}/v1/environments/{{envID}}/applicationRoles")
{
  MaxTimeout = -1,
};
var client = new RestClient(options);
var request = new RestRequest("", Method.Post);
request.AddHeader("Content-Type", "application/json");
request.AddHeader("Authorization", "Bearer {{accessToken}}");
var body = @"{" + "\n" +
@"    ""name"": ""CEO""," + "\n" +
@"    ""description"": ""The CEO""" + "\n" +
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

  url := "{{apiPath}}/v1/environments/{{envID}}/applicationRoles"
  method := "POST"

  payload := strings.NewReader(`{
    "name": "CEO",
    "description": "The CEO"
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
POST /v1/environments/{{envID}}/applicationRoles HTTP/1.1
Host: {{apiPath}}
Content-Type: application/json
Authorization: Bearer {{accessToken}}

{
    "name": "CEO",
    "description": "The CEO"
}
```

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("application/json");
RequestBody body = RequestBody.create(mediaType, "{\n    \"name\": \"CEO\",\n    \"description\": \"The CEO\"\n}");
Request request = new Request.Builder()
  .url("{{apiPath}}/v1/environments/{{envID}}/applicationRoles")
  .method("POST", body)
  .addHeader("Content-Type", "application/json")
  .addHeader("Authorization", "Bearer {{accessToken}}")
  .build();
Response response = client.newCall(request).execute();
```

```javascript
var settings = {
  "url": "{{apiPath}}/v1/environments/{{envID}}/applicationRoles",
  "method": "POST",
  "timeout": 0,
  "headers": {
    "Content-Type": "application/json",
    "Authorization": "Bearer {{accessToken}}"
  },
  "data": JSON.stringify({
    "name": "CEO",
    "description": "The CEO"
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
  'url': '{{apiPath}}/v1/environments/{{envID}}/applicationRoles',
  'headers': {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer {{accessToken}}'
  },
  body: JSON.stringify({
    "name": "CEO",
    "description": "The CEO"
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

url = "{{apiPath}}/v1/environments/{{envID}}/applicationRoles"

payload = json.dumps({
  "name": "CEO",
  "description": "The CEO"
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
$request->setUrl('{{apiPath}}/v1/environments/{{envID}}/applicationRoles');
$request->setMethod(HTTP_Request2::METHOD_POST);
$request->setConfig(array(
  'follow_redirects' => TRUE
));
$request->setHeader(array(
  'Content-Type' => 'application/json',
  'Authorization' => 'Bearer {{accessToken}}'
));
$request->setBody('{\n    "name": "CEO",\n    "description": "The CEO"\n}');
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

url = URI("{{apiPath}}/v1/environments/{{envID}}/applicationRoles")

http = Net::HTTP.new(url.host, url.port);
request = Net::HTTP::Post.new(url)
request["Content-Type"] = "application/json"
request["Authorization"] = "Bearer {{accessToken}}"
request.body = JSON.dump({
  "name": "CEO",
  "description": "The CEO"
})

response = http.request(request)
puts response.read_body
```

```swift
let parameters = "{\n    \"name\": \"CEO\",\n    \"description\": \"The CEO\"\n}"
let postData = parameters.data(using: .utf8)

var request = URLRequest(url: URL(string: "{{apiPath}}/v1/environments/{{envID}}/applicationRoles")!,timeoutInterval: Double.infinity)
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
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/applicationRoles"
        },
        "environment": {
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
        },
        "permissions": {
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/applicationRoles/permissions"
        }
    },
    "environment": {
        "id": "abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
    },
    "id": "f1d45fa4-0c94-45f9-8872-47a38d4c1b72",
    "name": "CEO",
    "description": "The CEO"
}
```

---

---
title: Create Application Role Permission
description: The POST {{apiPath}}/v1/environments/{{envID}}/applicationRoles/{{appRoleID}}/permissions request associates an application resource permission with the application role specified in the request URL. The request body takes an application resource permission ID as the value for the id property.
component: pingone-api
page_id: pingone-api:authorize:application-permissions/application-role-permissions/create-application-role-permission
canonical_url: https://developer.pingidentity.com/pingone-api/authorize/application-permissions/application-role-permissions/create-application-role-permission.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  headers: Headers
  body: Body
  example-request: Example Request
  example-response: Example Response
---

# Create Application Role Permission

##

```none
POST {{apiPath}}/v1/environments/{{envID}}/applicationRoles/{{appRoleID}}/permissions
```

The `POST {{apiPath}}/v1/environments/{{envID}}/applicationRoles/{{appRoleID}}/permissions` request associates an application resource permission with the application role specified in the request URL. The request body takes an application resource permission ID as the value for the `id` property.

When creating a relationship between an application role and an application permission, you cannot change any existing application permission properties, nor can you create a new application permission.

> **Collapse: Request Model**
>
> For complete descriptions, refer to [Application roles permissions data model](../application-role-permissions.html#application-roles-permissions-data-model).
>
> These properties are read-only:
>
> | Property      | Type   | Required |
> | ------------- | ------ | -------- |
> | `action`      | String | N/A      |
> | `description` | String | N/A      |
> | `id`          | String | N/A      |

|   |                                                                                                                                                                                                  |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | The `id` property returned by this POST request is the same ID as the application resource permission ID specified in the request body. This operation does not generate a unique ID in PingOne. |

### Headers

Authorization      Bearer {{accessToken}}

Content-Type      application/json

### Body

raw ( application/json )

```json
{
    "id": "{{appResourcePermissionID}}"
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
curl --location --globoff '{{apiPath}}/v1/environments/{{envID}}/applicationRoles/{{appRoleID}}/permissions' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {{accessToken}}' \
--data '{
    "id": "{{appResourcePermissionID}}"
}'
```

```csharp
var options = new RestClientOptions("{{apiPath}}/v1/environments/{{envID}}/applicationRoles/{{appRoleID}}/permissions")
{
  MaxTimeout = -1,
};
var client = new RestClient(options);
var request = new RestRequest("", Method.Post);
request.AddHeader("Content-Type", "application/json");
request.AddHeader("Authorization", "Bearer {{accessToken}}");
var body = @"{" + "\n" +
@"    ""id"": ""{{appResourcePermissionID}}""" + "\n" +
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

  url := "{{apiPath}}/v1/environments/{{envID}}/applicationRoles/{{appRoleID}}/permissions"
  method := "POST"

  payload := strings.NewReader(`{
    "id": "{{appResourcePermissionID}}"
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
POST /v1/environments/{{envID}}/applicationRoles/{{appRoleID}}/permissions HTTP/1.1
Host: {{apiPath}}
Content-Type: application/json
Authorization: Bearer {{accessToken}}

{
    "id": "{{appResourcePermissionID}}"
}
```

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("application/json");
RequestBody body = RequestBody.create(mediaType, "{\n    \"id\": \"{{appResourcePermissionID}}\"\n}");
Request request = new Request.Builder()
  .url("{{apiPath}}/v1/environments/{{envID}}/applicationRoles/{{appRoleID}}/permissions")
  .method("POST", body)
  .addHeader("Content-Type", "application/json")
  .addHeader("Authorization", "Bearer {{accessToken}}")
  .build();
Response response = client.newCall(request).execute();
```

```javascript
var settings = {
  "url": "{{apiPath}}/v1/environments/{{envID}}/applicationRoles/{{appRoleID}}/permissions",
  "method": "POST",
  "timeout": 0,
  "headers": {
    "Content-Type": "application/json",
    "Authorization": "Bearer {{accessToken}}"
  },
  "data": JSON.stringify({
    "id": "{{appResourcePermissionID}}"
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
  'url': '{{apiPath}}/v1/environments/{{envID}}/applicationRoles/{{appRoleID}}/permissions',
  'headers': {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer {{accessToken}}'
  },
  body: JSON.stringify({
    "id": "{{appResourcePermissionID}}"
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

url = "{{apiPath}}/v1/environments/{{envID}}/applicationRoles/{{appRoleID}}/permissions"

payload = json.dumps({
  "id": "{{appResourcePermissionID}}"
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
$request->setUrl('{{apiPath}}/v1/environments/{{envID}}/applicationRoles/{{appRoleID}}/permissions');
$request->setMethod(HTTP_Request2::METHOD_POST);
$request->setConfig(array(
  'follow_redirects' => TRUE
));
$request->setHeader(array(
  'Content-Type' => 'application/json',
  'Authorization' => 'Bearer {{accessToken}}'
));
$request->setBody('{\n    "id": "{{appResourcePermissionID}}"\n}');
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

url = URI("{{apiPath}}/v1/environments/{{envID}}/applicationRoles/{{appRoleID}}/permissions")

http = Net::HTTP.new(url.host, url.port);
request = Net::HTTP::Post.new(url)
request["Content-Type"] = "application/json"
request["Authorization"] = "Bearer {{accessToken}}"
request.body = JSON.dump({
  "id": "{{appResourcePermissionID}}"
})

response = http.request(request)
puts response.read_body
```

```swift
let parameters = "{\n    \"id\": \"{{appResourcePermissionID}}\"\n}"
let postData = parameters.data(using: .utf8)

var request = URLRequest(url: URL(string: "{{apiPath}}/v1/environments/{{envID}}/applicationRoles/{{appRoleID}}/permissions")!,timeoutInterval: Double.infinity)
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

200 OK

```json
{
    "_links": {
        "self": {
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/applicationRoles/f1d45fa4-0c94-45f9-8872-47a38d4c1b72/permissions"
        },
        "environment": {
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
        }
    },
    "environment": {
        "id": "abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
    },
    "id": "4c56f473-48c2-4256-ad8d-a6c15803447a",
    "action": "read",
    "resource": {
        "id": "3e8c0da7-8094-4554-9ba8-b61a7778b159",
        "name": "accounts"
    },
    "description": "List documents"
}
```

---

---
title: Create Decision Endpoint
description: There are two create options. You can configure a policy decision endpoint to reference a specific policy version. Or, you can configure a policy decision endpoint that is always up-to-date.
component: pingone-api
page_id: pingone-api:authorize:authorization-decisions/decision-endpoints/create-decision-endpoint
canonical_url: https://developer.pingidentity.com/pingone-api/authorize/authorization-decisions/decision-endpoints/create-decision-endpoint.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  prerequisites: Prerequisites
  headers: Headers
  body: Body
  example-request: Example Request
  example-response: Example Response
---

# Create Decision Endpoint

##

```none
POST {{apiPath}}/v1/environments/{{envID}}/decisionEndpoints
```

There are two create options. You can configure a policy decision endpoint to reference a specific policy version. Or, you can configure a policy decision endpoint that is always up-to-date.

In cases where a specific policy version is defined in the request, the policy decision service fetches the policy configuration at that version from the policy editor service and stores it locally. When no policy version is defined (always up-to-date), the decision endpoint is recorded in the local database with no policy configuration. Access to the policy editor service is not required in this case.

The following sample shows the `POST {{apiPath}}/v1/environments/{{envID}}/decisionEndpoints` operation to create a new policy decision endpoint resource associated with the environment specified in the request URL. The request body specifies the `name`, `description`, `authorizationVersion` (the policy version), and `recordRecentRequests` attributes.

|   |                                                                                                                                                                                    |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | When a policy decision endpoint does not specify a policy version, the policy decision service fetches the current policy configuration at runtime from the policy editor service. |

### Prerequisites

* Refer to [Authorization Decisions](../decision-endpoints.html) for important overview information.

> **Collapse: Request Model**
>
> For property descriptions, refer to [Policy decision service data model](../decision-endpoints.html#policy-decision-service-data-model).
>
> | Property                  | Type    | Required |
> | ------------------------- | ------- | -------- |
> | `alternateId`             | UUID    | Optional |
> | `authorizationVersion.id` | UUID    | Optional |
> | `description`             | String  | Required |
> | `id`                      | UUID    | Required |
> | `name`                    | String  | Required |
> | `owned`                   | Boolean | Optional |
> | `policyId`                | UUID    | Optional |
> | `recordRecentRequests`    | Boolean | Required |

### Headers

Authorization      Bearer {{accessToken}}

Content-Type      application/json

### Body

raw ( application/json )

```json
{
    "name": "Test Endpoint",
    "description": "Endpoint for use in tests",
    "authorizationVersion": {
        "id": "{{authorizationVersionID}}"
    },
    "recordRecentRequests": true
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
curl --location --globoff '{{apiPath}}/v1/environments/{{envID}}/decisionEndpoints' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {{accessToken}}' \
--data '{
    "name": "Test Endpoint",
    "description": "Endpoint for use in tests",
    "authorizationVersion": {
        "id": "{{authorizationVersionID}}"
    },
    "recordRecentRequests": true
}'
```

```csharp
var options = new RestClientOptions("{{apiPath}}/v1/environments/{{envID}}/decisionEndpoints")
{
  MaxTimeout = -1,
};
var client = new RestClient(options);
var request = new RestRequest("", Method.Post);
request.AddHeader("Content-Type", "application/json");
request.AddHeader("Authorization", "Bearer {{accessToken}}");
var body = @"{" + "\n" +
@"    ""name"": ""Test Endpoint""," + "\n" +
@"    ""description"": ""Endpoint for use in tests""," + "\n" +
@"    ""authorizationVersion"": {" + "\n" +
@"        ""id"": ""{{authorizationVersionID}}""" + "\n" +
@"    }," + "\n" +
@"    ""recordRecentRequests"": true" + "\n" +
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

  url := "{{apiPath}}/v1/environments/{{envID}}/decisionEndpoints"
  method := "POST"

  payload := strings.NewReader(`{
    "name": "Test Endpoint",
    "description": "Endpoint for use in tests",
    "authorizationVersion": {
        "id": "{{authorizationVersionID}}"
    },
    "recordRecentRequests": true
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
POST /v1/environments/{{envID}}/decisionEndpoints HTTP/1.1
Host: {{apiPath}}
Content-Type: application/json
Authorization: Bearer {{accessToken}}

{
    "name": "Test Endpoint",
    "description": "Endpoint for use in tests",
    "authorizationVersion": {
        "id": "{{authorizationVersionID}}"
    },
    "recordRecentRequests": true
}
```

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("application/json");
RequestBody body = RequestBody.create(mediaType, "{\n    \"name\": \"Test Endpoint\",\n    \"description\": \"Endpoint for use in tests\",\n    \"authorizationVersion\": {\n        \"id\": \"{{authorizationVersionID}}\"\n    },\n    \"recordRecentRequests\": true\n}");
Request request = new Request.Builder()
  .url("{{apiPath}}/v1/environments/{{envID}}/decisionEndpoints")
  .method("POST", body)
  .addHeader("Content-Type", "application/json")
  .addHeader("Authorization", "Bearer {{accessToken}}")
  .build();
Response response = client.newCall(request).execute();
```

```javascript
var settings = {
  "url": "{{apiPath}}/v1/environments/{{envID}}/decisionEndpoints",
  "method": "POST",
  "timeout": 0,
  "headers": {
    "Content-Type": "application/json",
    "Authorization": "Bearer {{accessToken}}"
  },
  "data": JSON.stringify({
    "name": "Test Endpoint",
    "description": "Endpoint for use in tests",
    "authorizationVersion": {
      "id": "{{authorizationVersionID}}"
    },
    "recordRecentRequests": true
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
  'url': '{{apiPath}}/v1/environments/{{envID}}/decisionEndpoints',
  'headers': {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer {{accessToken}}'
  },
  body: JSON.stringify({
    "name": "Test Endpoint",
    "description": "Endpoint for use in tests",
    "authorizationVersion": {
      "id": "{{authorizationVersionID}}"
    },
    "recordRecentRequests": true
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

url = "{{apiPath}}/v1/environments/{{envID}}/decisionEndpoints"

payload = json.dumps({
  "name": "Test Endpoint",
  "description": "Endpoint for use in tests",
  "authorizationVersion": {
    "id": "{{authorizationVersionID}}"
  },
  "recordRecentRequests": True
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
$request->setUrl('{{apiPath}}/v1/environments/{{envID}}/decisionEndpoints');
$request->setMethod(HTTP_Request2::METHOD_POST);
$request->setConfig(array(
  'follow_redirects' => TRUE
));
$request->setHeader(array(
  'Content-Type' => 'application/json',
  'Authorization' => 'Bearer {{accessToken}}'
));
$request->setBody('{\n    "name": "Test Endpoint",\n    "description": "Endpoint for use in tests",\n    "authorizationVersion": {\n        "id": "{{authorizationVersionID}}"\n    },\n    "recordRecentRequests": true\n}');
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

url = URI("{{apiPath}}/v1/environments/{{envID}}/decisionEndpoints")

http = Net::HTTP.new(url.host, url.port);
request = Net::HTTP::Post.new(url)
request["Content-Type"] = "application/json"
request["Authorization"] = "Bearer {{accessToken}}"
request.body = JSON.dump({
  "name": "Test Endpoint",
  "description": "Endpoint for use in tests",
  "authorizationVersion": {
    "id": "{{authorizationVersionID}}"
  },
  "recordRecentRequests": true
})

response = http.request(request)
puts response.read_body
```

```swift
let parameters = "{\n    \"name\": \"Test Endpoint\",\n    \"description\": \"Endpoint for use in tests\",\n    \"authorizationVersion\": {\n        \"id\": \"{{authorizationVersionID}}\"\n    },\n    \"recordRecentRequests\": true\n}"
let postData = parameters.data(using: .utf8)

var request = URLRequest(url: URL(string: "{{apiPath}}/v1/environments/{{envID}}/decisionEndpoints")!,timeoutInterval: Double.infinity)
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
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/decisionEndpoints/bcb106be-96fa-4479-b3ee-dbd7666e4da2"
        },
        "authorizationVersion": {
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/authorizationVersions/d7437c70-3082-11ee-80bd-adfbbca2bf5b"
        },
        "environment": {
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
        }
    },
    "id": "bcb106be-96fa-4479-b3ee-dbd7666e4da2",
    "name": "Test Endpoint",
    "description": "Endpoint for use in tests",
    "authorizationVersion": {
        "id": "d7437c70-3082-11ee-80bd-adfbbca2bf5b"
    },
    "recordRecentRequests": true,
    "owned": false,
    "environment": {
        "id": "abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
    }
}
```

---

---
title: Create External OAuth Server
description: The following sample shows the POST {{apiPath}}/v1/environments/{{envID}}/externalOAuthServers operation to create a new external OAuth server resource associated with the environment specified in the request URL.
component: pingone-api
page_id: pingone-api:authorize:api-access-management/external-oauth-servers/create-external-oauth-server
canonical_url: https://developer.pingidentity.com/pingone-api/authorize/api-access-management/external-oauth-servers/create-external-oauth-server.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  prerequisites: Prerequisites
  headers: Headers
  body: Body
  example-request: Example Request
  example-response: Example Response
---

# Create External OAuth Server

##

```none
POST {{apiPath}}/v1/environments/{{envID}}/externalOAuthServers
```

The following sample shows the `POST {{apiPath}}/v1/environments/{{envID}}/externalOAuthServers` operation to create a new external OAuth server resource associated with the environment specified in the request URL.

When successful, a `201 CREATED` message and the new external OAuth server resource is returned.

### Prerequisites

* Refer to [PingOne Authorize API Access Management](../../api-access-management.html) for important overview information.

> **Collapse: Request Model**
>
> For property descriptions, refer to [External OAuth server data model](../external-oauth-servers.html#external-oauth-server-data-model)
>
> | Property                        | Type   | Required |
> | ------------------------------- | ------ | -------- |
> | `description`                   | String | Optional |
> | `issuers`                       | Array  | Optional |
> | `name`                          | String | Required |
> | `type`                          | String | Required |
> | `validation`                    | Object | Required |
> | `validation.clockSkewTolerance` | Number | Optional |
> | `validation.jwks`               | String | Optional |
> | `validation.jwksUrl`            | String | Optional |
> | `validation.type`               | String | Required |

### Headers

Authorization      Bearer {{accessToken}}

Content-Type      application/json

### Body

raw ( application/json )

```json
{
  "name": "Example_2",
  "description": "OAuth server resource example",
  "type": "EXTERNAL",
  "issuers": [
    "https://example.com/as"
  ],
  "validation": {
    "type": "JWKS_URL",
    "jwksUrl": "https://example.com/as/jwks",
    "clockSkewTolerance": 5
  }
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
curl --location --globoff '{{apiPath}}/v1/environments/{{envID}}/externalOAuthServers' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {{accessToken}}' \
--data '{
  "name": "Example_2",
  "description": "OAuth server resource example",
  "type": "EXTERNAL",
  "issuers": [
    "https://example.com/as"
  ],
  "validation": {
    "type": "JWKS_URL",
    "jwksUrl": "https://example.com/as/jwks",
    "clockSkewTolerance": 5
  }
}'
```

```csharp
var options = new RestClientOptions("{{apiPath}}/v1/environments/{{envID}}/externalOAuthServers")
{
  MaxTimeout = -1,
};
var client = new RestClient(options);
var request = new RestRequest("", Method.Post);
request.AddHeader("Content-Type", "application/json");
request.AddHeader("Authorization", "Bearer {{accessToken}}");
var body = @"{" + "\n" +
@"  ""name"": ""Example_2""," + "\n" +
@"  ""description"": ""OAuth server resource example""," + "\n" +
@"  ""type"": ""EXTERNAL""," + "\n" +
@"  ""issuers"": [" + "\n" +
@"    ""https://example.com/as""" + "\n" +
@"  ]," + "\n" +
@"  ""validation"": {" + "\n" +
@"    ""type"": ""JWKS_URL""," + "\n" +
@"    ""jwksUrl"": ""https://example.com/as/jwks""," + "\n" +
@"    ""clockSkewTolerance"": 5" + "\n" +
@"  }" + "\n" +
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

  url := "{{apiPath}}/v1/environments/{{envID}}/externalOAuthServers"
  method := "POST"

  payload := strings.NewReader(`{
  "name": "Example_2",
  "description": "OAuth server resource example",
  "type": "EXTERNAL",
  "issuers": [
    "https://example.com/as"
  ],
  "validation": {
    "type": "JWKS_URL",
    "jwksUrl": "https://example.com/as/jwks",
    "clockSkewTolerance": 5
  }
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
POST /v1/environments/{{envID}}/externalOAuthServers HTTP/1.1
Host: {{apiPath}}
Content-Type: application/json
Authorization: Bearer {{accessToken}}

{
  "name": "Example_2",
  "description": "OAuth server resource example",
  "type": "EXTERNAL",
  "issuers": [
    "https://example.com/as"
  ],
  "validation": {
    "type": "JWKS_URL",
    "jwksUrl": "https://example.com/as/jwks",
    "clockSkewTolerance": 5
  }
}
```

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("application/json");
RequestBody body = RequestBody.create(mediaType, "{\n  \"name\": \"Example_2\",\n  \"description\": \"OAuth server resource example\",\n  \"type\": \"EXTERNAL\",\n  \"issuers\": [\n    \"https://example.com/as\"\n  ],\n  \"validation\": {\n    \"type\": \"JWKS_URL\",\n    \"jwksUrl\": \"https://example.com/as/jwks\",\n    \"clockSkewTolerance\": 5\n  }\n}");
Request request = new Request.Builder()
  .url("{{apiPath}}/v1/environments/{{envID}}/externalOAuthServers")
  .method("POST", body)
  .addHeader("Content-Type", "application/json")
  .addHeader("Authorization", "Bearer {{accessToken}}")
  .build();
Response response = client.newCall(request).execute();
```

```javascript
var settings = {
  "url": "{{apiPath}}/v1/environments/{{envID}}/externalOAuthServers",
  "method": "POST",
  "timeout": 0,
  "headers": {
    "Content-Type": "application/json",
    "Authorization": "Bearer {{accessToken}}"
  },
  "data": JSON.stringify({
    "name": "Example_2",
    "description": "OAuth server resource example",
    "type": "EXTERNAL",
    "issuers": [
      "https://example.com/as"
    ],
    "validation": {
      "type": "JWKS_URL",
      "jwksUrl": "https://example.com/as/jwks",
      "clockSkewTolerance": 5
    }
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
  'url': '{{apiPath}}/v1/environments/{{envID}}/externalOAuthServers',
  'headers': {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer {{accessToken}}'
  },
  body: JSON.stringify({
    "name": "Example_2",
    "description": "OAuth server resource example",
    "type": "EXTERNAL",
    "issuers": [
      "https://example.com/as"
    ],
    "validation": {
      "type": "JWKS_URL",
      "jwksUrl": "https://example.com/as/jwks",
      "clockSkewTolerance": 5
    }
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

url = "{{apiPath}}/v1/environments/{{envID}}/externalOAuthServers"

payload = json.dumps({
  "name": "Example_2",
  "description": "OAuth server resource example",
  "type": "EXTERNAL",
  "issuers": [
    "https://example.com/as"
  ],
  "validation": {
    "type": "JWKS_URL",
    "jwksUrl": "https://example.com/as/jwks",
    "clockSkewTolerance": 5
  }
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
$request->setUrl('{{apiPath}}/v1/environments/{{envID}}/externalOAuthServers');
$request->setMethod(HTTP_Request2::METHOD_POST);
$request->setConfig(array(
  'follow_redirects' => TRUE
));
$request->setHeader(array(
  'Content-Type' => 'application/json',
  'Authorization' => 'Bearer {{accessToken}}'
));
$request->setBody('{\n  "name": "Example_2",\n  "description": "OAuth server resource example",\n  "type": "EXTERNAL",\n  "issuers": [\n    "https://example.com/as"\n  ],\n  "validation": {\n    "type": "JWKS_URL",\n    "jwksUrl": "https://example.com/as/jwks",\n    "clockSkewTolerance": 5\n  }\n}');
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

url = URI("{{apiPath}}/v1/environments/{{envID}}/externalOAuthServers")

http = Net::HTTP.new(url.host, url.port);
request = Net::HTTP::Post.new(url)
request["Content-Type"] = "application/json"
request["Authorization"] = "Bearer {{accessToken}}"
request.body = JSON.dump({
  "name": "Example_2",
  "description": "OAuth server resource example",
  "type": "EXTERNAL",
  "issuers": [
    "https://example.com/as"
  ],
  "validation": {
    "type": "JWKS_URL",
    "jwksUrl": "https://example.com/as/jwks",
    "clockSkewTolerance": 5
  }
})

response = http.request(request)
puts response.read_body
```

```swift
let parameters = "{\n  \"name\": \"Example_2\",\n  \"description\": \"OAuth server resource example\",\n  \"type\": \"EXTERNAL\",\n  \"issuers\": [\n    \"https://example.com/as\"\n  ],\n  \"validation\": {\n    \"type\": \"JWKS_URL\",\n    \"jwksUrl\": \"https://example.com/as/jwks\",\n    \"clockSkewTolerance\": 5\n  }\n}"
let postData = parameters.data(using: .utf8)

var request = URLRequest(url: URL(string: "{{apiPath}}/v1/environments/{{envID}}/externalOAuthServers")!,timeoutInterval: Double.infinity)
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
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/externalOAuthServers/29e4c577-fea1-490c-a537-97264419ca81"
        },
        "environment": {
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
        },
        "apiServers": {
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/apiServers?filter=authorizationServer.externalOAuthServer.id%20eq%20%2229e4c577-fea1-490c-a537-97264419ca81%22"
        }
    },
    "id": "29e4c577-fea1-490c-a537-97264419ca81",
    "environment": {
        "id": "abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
    },
    "name": "Example_1",
    "description": "OAuth server resource example",
    "type": "EXTERNAL",
    "issuers": [
        "https://example.com/as"
    ],
    "validation": {
        "type": "JWKS_URL",
        "jwksUrl": "https://example.com/as/jwks",
        "clockSkewTolerance": 5
    }
}
```

---

---
title: Decision Endpoints
description: The PingOne policy decision service provides operations to create, read, update and delete decision policy versions in PingOne.
component: pingone-api
page_id: pingone-api:authorize:authorization-decisions/decision-endpoints
canonical_url: https://developer.pingidentity.com/pingone-api/authorize/authorization-decisions/decision-endpoints.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  assigning-admin-roles-and-permissions-to-this-service: Assigning admin roles and permissions to this service
  policy-decision-service-data-model: Policy decision service data model
  policy-decision-management-events-generated: Policy decision management events generated
  response-codes: Response codes
---

# Decision Endpoints

The PingOne policy decision service provides operations to create, read, update and delete decision policy versions in PingOne.

## Assigning admin roles and permissions to this service

Admin role assignments determine access to PingOne APIs. When assigning admin roles to this service, refer to [PingOne Permissions by Service](../../platform/reference/roles-and-permissions-in-pingone/permissions-by-service.html) for the service-specific permissions.

You can also choose to assign admin roles based on particular service resources. Refer to [PingOne Permissions by Resource](../../platform/reference/roles-and-permissions-in-pingone/permissions-by-resource.html) when assigning admin roles per service resources.

Admin assignments to roles are set by:

* [Automatic assignment for some roles](../../platform/roles/predefined-roles.html#automatic-role-assignment).

* [Group Role Assignments](../../platform/group-role-assignments/group-role-assignments.html).

* [User Role Assignments](../../platform/users/user-role-assignments.html).

Refer to [Roles Management](../../platform/roles.html) for more information.

## Policy decision service data model

| Property                     | Type    | Required | Mutable | Description                                                                                                                                                                                                                                                           |
| ---------------------------- | ------- | -------- | ------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `alternateId`                | UUID    | Optional | Mutable | A string that specifies alternative unique identifier for the endpoint, which provides a method for locating the resource by a known, fixed identifier.                                                                                                               |
| `authorizationVersion.id`    | UUID    | Optional | Mutable | A string that specifies the ID of the Authorization Version deployed to this endpoint. Versioning allows independent development and deployment of policies. If omitted, the endpoint always uses the latest policy version available from the policy editor service. |
| `authorizationVersion.href`  | String  | Optional | Mutable | A string that specifies the request URL for the authorization version endpoint.                                                                                                                                                                                       |
| `authorizationVersion.title` | String  | Optional | Mutable | A string that specifies the title for the authorization version response.                                                                                                                                                                                             |
| `authorizationVersion.type`  | String  | Optional | Mutable | A string that specifies the content type for the authorization version response.                                                                                                                                                                                      |
| `description`                | String  | Required | Mutable | A string that specifies the description of the policy decision resource.                                                                                                                                                                                              |
| `id`                         | UUID    | Required | Mutable | A string that specifies the resource's unique identifier.                                                                                                                                                                                                             |
| `name`                       | String  | Required | Mutable | A string that specifies the policy decision resource name.                                                                                                                                                                                                            |
| `owned`                      | Boolean | Optional | Mutable | A boolean that when true restricts modifications of the endpoint to PingOne-owned clients.                                                                                                                                                                            |
| `policyId`                   | UUID    | Optional | Mutable | A string that specifies the ID of the root policy configured for this endpoint. If omitted, the policy editor service decides on a suitable default.                                                                                                                  |
| `recentDecisions.href`       | String  | Optional | Mutable | A string that specifies the request URL for the recent decisions endpoint.                                                                                                                                                                                            |
| `recentDecisions.title`      | String  | Optional | Mutable | A string that specifies the title for the recent decisions response.                                                                                                                                                                                                  |
| `recentDecisions.type`       | String  | Optional | Mutable | A string that specifies the content type for the recent decisions response.                                                                                                                                                                                           |
| `recordRecentRequests`       | Boolean | Required | Mutable | A boolean that specifies whether to record a limited history of recent decision requests and responses, which can be queried through a separate API.                                                                                                                  |

## Policy decision management events generated

Refer to [Audit Reporting Events](../../platform/audit-activities.html) for the events generated.

### Response codes

| Code | Message                                                               |
| ---- | --------------------------------------------------------------------- |
| 200  | Successful operation.                                                 |
| 201  | Successfully created.                                                 |
| 204  | Successfully removed. No content.                                     |
| 400  | The request could not be completed.                                   |
| 401  | You do not have access to this resource.                              |
| 403  | You do not have permissions or are not licensed to make this request. |
| 404  | The requested resource was not found.                                 |