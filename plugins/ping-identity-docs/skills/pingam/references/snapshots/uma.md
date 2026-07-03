---
title: /json/users/{user}/oauth2/resources/labels
description: PingAM endpoint for creating, deleting, and querying User-Managed Access (UMA) user and star labels
component: pingam
version: 8.1
page_id: pingam:uma:endpoint-labels
canonical_url: https://docs.pingidentity.com/pingam/8.1/uma/endpoint-labels.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["User-Managed Access (UMA)", "Endpoints", "Resource Labels"]
page_aliases: ["uma-guide:endpoint-labels.adoc"]
---

# /json/users/{user}/oauth2/resources/labels

AM-specific endpoint used to create, delete, and query UMA user and star labels.

> **Collapse: Supported HTTP methods**
>
> | Action | HTTP method |
> | ------ | ----------- |
> | Create | POST        |
> | Query  | GET         |
> | Delete | DELETE      |

|   |                                                                                                                                                                                                                                        |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Use the AM API Explorer for detailed information about this endpoint, and to test it against your deployed AM instance.In the AM admin UI, click the Help icon, and go to API Explorer > users > *user* > oauth2 > resources > labels. |

You must compose the path to the token endpoint addressing the specific realm where the token will be issued. For example, `https://am.example.com:8443/am/json/realms/root/realms/subrealm1/users/user/oauth2/resources/labels`.

The labels endpoint does not support any parameters. To authenticate to the endpoint, send the SSO token of the resource owner as the value of the `iPlanetDirectoryPro` header.

To create a label, send an HTTP POST request to the endpoint, adding the description of the label as a JSON object in the body. For example:

```json
{
  "name" : "My Favorites",
  "type" : "STAR",
  "resourceSetIDs": [
      "UMA_resource_ID_1234567890",
      "UMA_resource_ID_0987654321"
  ]
}
```

The value of the `type` object can be `USER`, for user labels, and `STAR`, for star labels. For more information about the label types, see [UMA labels](uma-manage-resource-set-labels.html).

The `resourceSetIDs` object is an array of UMA resource IDs that the label applies to. It is not mandatory; if you do not add it, the label will be created without any resource associated. You will need to update the *resource* to add it to the label, because the labels endpoint does not support updating labels.

For examples, see [Manage UMA user and favorite labels](uma-labels-with-REST-users.html).

---

---
title: /json/users/{user}/uma/pendingrequests
description: PingAM endpoint for resource owners to list, approve, or deny pending User-Managed Access authorization requests
component: pingam
version: 8.1
page_id: pingam:uma:endpoint-pending-request
canonical_url: https://docs.pingidentity.com/pingam/8.1/uma/endpoint-pending-request.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["User-Managed Access (UMA)", "Endpoints", "Pending Request"]
page_aliases: ["uma-guide:endpoint-pending-request.adoc"]
section_ids:
  to-view-pending-resource-access-requests: View and manage pending access requests
---

# /json/users/{user}/uma/pendingrequests

AM-specific endpoint used to list, approve, or deny pending authorization requests on a resource.

> **Collapse: Supported HTTP methods**
>
> | Action               | HTTP method |
> | -------------------- | ----------- |
> | Approve, Approve All | POST        |
> | Deny, Deny All       | POST        |
> | Query                | GET         |

|   |                                                                                                                                                                                                                                       |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Use the AM API Explorer for detailed information about this endpoint, and to test it against your deployed AM instance.In the AM admin UI, click the Help icon, and then go to API Explorer > users > *user* > uma > pendingrequests. |

You must compose the path to the token endpoint addressing the specific realm where the token will be issued. For example, `https://am.example.com:8443/am/json/realms/root/realms/subrealm1/users/user/oauth2/resources/labels`.

To authenticate to the endpoint, send the SSO token of the resource owner as the value of the `iPlanetDirectoryPro` header.

The endpoint supports the following actions:

* approve

  Approves the permission request specified in the endpoint's URL. It does not grant the permission requested. Instead, it grants the scopes sent as a JSON document in the body of the `approve` call. For example:

  ```bash
  $ curl \
  --request POST \
  --header "iPlanetDirectoryPro: AQIC5wM2LY4S…​Q4MTE4NTA2*" \
  --header "Accept-API-Version: resource=1.0" \
  --data '{
            "scopes": [ "comment" ]
  }' \
  "https://am.example.com:8443/am/json/realms/root/realms/alpha/users/alice/uma/pendingrequests/0d7790de-9066-4bb6-8e81-25b6f9d0b8853?_action=approve"
  ```

* approveAll

  Approves every pending permission request for the user, but does not grant the permissions requested. Instead, it grants the scopes sent as a JSON document in the body of the `approveAll` call. For example:

  ```bash
  $ curl \
  --request POST
  --header "iPlanetDirectoryPro: AQIC5wM2LY4S…​Q4MTE4NTA2*" \
  --header "Accept-API-Version: resource=1.0" \
  --data '{
           "scopes": [
             "comment"
           ]
  }' \
  "https://am.example.com:8443/am/json/realms/root/realms/alpha/users/alice/uma/pendingrequests?_action=approveAll"
  ```

* deny

  Denies the permission request specified in the endpoint's URL. For example:

  ```bash
  $ curl \
  --request POST \
  --header "iPlanetDirectoryPro: AQIC5wM2LY4S…​Q4MTE4NTA2*" \
  --header "Accept-API-Version: resource=1.0" \
  "https://am.example.com:8443/am/json/realms/root/realms/alpha/users/alice/uma/pendingrequests/0d7790de-9066-4bb6-8e81-25b6f9d0b8853?_action=deny"
  ```

* denyAll

  Denies every pending permission request for the user. For example:

  ```bash
  $ curl \
  --request POST \
  --header "iPlanetDirectoryPro: AQIC5wM2LY4S…​Q4MTE4NTA2*" \
  --header "Accept-API-Version: resource=1.0" \
  "https://am.example.com:8443/am/json/realms/root/realms/alpha/users/alice/uma/pendingrequests?_action=denyAll"
  ```

  AM returns an HTTP 200 message with an empty body if the request is successful, and an HTTP 500 message if not.

The endpoint also supports the `_queryFilter` parameter to request a list of pending permission requests for the user. Specify `true` to match every request, `false` to mach no request. For example:

```bash
$ curl \
--request GET \
--header "iPlanetDirectoryPro: AQIC5wM2LY4S…​Q4MTE4NTA2*" \
--header "Accept-API-Version: resource=1.0" \
"https://am.example.com:8443/am/json/realms/root/realms/alpha/users/alice/uma/pendingrequests?_queryFilter=true"
{
  "result": [
    {
      "_id": "0d3190ef-6901-654b-82pa-13a6h9d0b53452",
      "user": "bob",
      "resource": "My Resource Name",
      "when": 1607002810,
      "permissions": [
        "download"
      ]
    }
  ],
  "resultCount": 1,
  "pagedResultsCookie": "10d7790de",
  "totalPagedResultsPolicy": "EXACT",
  "totalPagedResults": 0,
  "remainingPagedResults": 0
}
```

AM also provides built-in user pages in the UI to view pending resource access requests:

## View and manage pending access requests

In this UMA workflow, a user requests access to a resource that has not been explicitly shared with them. The resource owner receives a notification of the request and can choose to allow or deny access.

1. Log in to AM as the resource owner, and then go to Shares > Requests.

   ![A list of pending requests for access to your resources is displayed.](_images/uma-pending-requests.png)Figure 1. UMA Requests screen presented to the resource owner

2. Review the pending request, and take one of the following actions:

   1. Click Allow to approve the request.

      |   |                                                                                                                                                                                                                       |
      | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      |   | To remove permissions from the request, click the permission, then press either `Delete` or `Backspace`. Select the permission from the drop-down list to return it to the permissions granted to the resource owner. |

      The required UMA policy is created, and optionally, the requesting party is notified that they can now access the resource.

      The requesting party can view a list of resources to which they have access by going to Shares > Resources > Shared with me.

   2. Click Deny to prevent the requesting party from accessing the resource.

      The pending request is removed, and the requesting party is not notified.

3. After allowing or denying access to a resource, an entry is created in the History page.

   To view a list of actions that have occurred, go to Shares > History.

---

---
title: /json/users/{user}/uma/policies
description: Manage User-Managed Access policies in PingAM with create, read, update, delete, and query operations using the /json/users/{user}/uma/policies endpoint
component: pingam
version: 8.1
page_id: pingam:uma:endpoint-policies
canonical_url: https://docs.pingidentity.com/pingam/8.1/uma/endpoint-policies.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["User-Managed Access (UMA)", "Endpoints", "Policies"]
page_aliases: ["uma-guide:endpoint-policies.adoc"]
---

# /json/users/{user}/uma/policies

AM-specific endpoint used to create, delete, read, update, and query UMA policies.

> **Collapse: Supported HTTP methods**
>
> | Action | HTTP method |
> | ------ | ----------- |
> | Create | PUT         |
> | Read   | GET         |
> | Update | PUT         |
> | Delete | DELETE      |
> | Query  | GET         |

|   |                                                                                                                                                                                                                           |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Use the AM API Explorer for detailed information about this endpoint, and to test it against your deployed AM instance.In the AM admin UI, click the Help icon, and go to API Explorer > users > *user* > uma > policies. |

You must compose the path to the token endpoint addressing the specific realm where the token will be issued. For example, `https://am.example.com:8443/am/json/realms/root/realms/alpha/users/user/uma/policies`.

The policies endpoint does not support any parameters. To authenticate to the endpoint, send the SSO token of the resource owner as the value of the `iPlanetDirectoryPro` header.

To create or update a policy, send an HTTP PUT request to the endpoint, adding the description of the policy as a JSON object in the body. For example:

```json
{
    "policyId": "UMA_resource_ID_12345678",
    "permissions":
    [
        {
            "subject": "requesting_party_identity",
            "scopes": [
                "view",
                "comment",
                "download"
            ]
        }
    ],
  "type": "AND",
  "conditions": [
      {
          "type": "Expiration",
          "expirationDate": "1638263100"
      }
  ],


}
```

* `policyID` is an UMA resource ID. To obtain it, query the [/uma/resource\_set](endpoint-resource_set.html) endpoint.

* The entire `permissions` object is mandatory.

* `subject` is the username or identity associated with the requesting party.

  In other words, the person, device, or client that the policy grants permission to.

* The `scopes` object is an array of permissions or scopes that are granted to the `subject`.

  These scopes must match the scopes supported by the resource that the policy protects.

* The first `type` field is optional, and lets you add multiple conditions, separated by `AND` and `OR` functions.

* The second `type` field specifies the condition type. Possible values are `Expiration`, to set an expiration date on an UMA authorization, or `clientId`, to restrict the list of clients that can obtain an RPT *(tooltip: Requesting party token)*.

For examples of using this endpoint, see [UMA policies](uma-policies.html).

---

---
title: /uma/.well-known/uma2-configuration
description: Discover UMA provider configuration by querying the UMA 2.0 well-known endpoint to retrieve supported grant types, token endpoints, and resource registration URIs
component: pingam
version: 8.1
page_id: pingam:uma:endpoint-configuration
canonical_url: https://docs.pingidentity.com/pingam/8.1/uma/endpoint-configuration.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["User-Managed Access (UMA)", "Endpoints", "Configuration"]
page_aliases: ["uma-guide:endpoint-configuration.adoc"]
---

# /uma/.well-known/uma2-configuration

AM exposes an endpoint for discovering information about the UMA provider configuration.

A resource server or client can send an HTTP GET request to `/uma/.well-known/uma2-configuration` to retrieve a JSON object that shows the UMA configuration.

When making a REST API call, specify the realm in the path component of the endpoint. You must specify the entire hierarchy of the realm, starting at the Top Level Realm. Prefix each realm in the hierarchy with the `realms/` keyword. For example, `/realms/root/realms/customers/realms/europe`.

The following is an example of a GET request to the UMA 2.0 configuration discovery endpoint for a subrealm named `subrealm` in the Top Level Realm:

```bash
$ curl \
--request GET \
"https://am.example.com:8443/am/uma/realms/root/realms/alpha/.well-known/uma2-configuration"
{
    "issuer": "https://am.example.com:8443/am/oauth2/subrealm",
    "grant_types_supported": [
        "urn:ietf:params:oauth:grant-type:saml2-bearer",
        "urn:ietf:params:oauth:grant-type:uma-ticket",
        "client_credentials",
        "password",
        "authorization_code",
        "urn:ietf:params:oauth:grant-type:device_code",
        "http://oauth.net/grant_type/device/1.0"
    ],
    "token_endpoint_auth_methods_supported": [
        "client_secret_post",
        "private_key_jwt",
        "client_secret_basic"
    ],
    "revocation_endpoint_auth_methods_supported": [
        "client_secret_post",
        "private_key_jwt",
        "client_secret_basic"
    ],
    "response_types_supported": [
        "code token id_token",
        "code",
        "code id_token",
        "device_code",
        "id_token",
        "code token",
        "token",
        "token id_token"
    ],
    "jwks_uri": "https://am.example.com:8443/am/oauth2/realms/root/realms/alpha/connect/jwk_uri",
    "dynamic_client_endpoint": "https://am.example.com:8443/am/oauth2/realms/root/realms/alpha/register",
    "token_endpoint": "https://am.example.com:8443/am/oauth2/realms/root/realms/alpha/access_token",
    "authorization_endpoint": "https://am.example.com:8443/am/oauth2/realms/root/realms/alpha/authorize",
    "revocation_endpoint": "https://am.example.com:8443/am/oauth2/realms/root/realms/alpha/token/revoke",
    "introspection_endpoint": "https://am.example.com:8443/am/oauth2/realms/root/realms/alpha/introspect",
    "resource_registration_endpoint": "https://am.example.com:8443/am/uma/realms/root/realms/alpha/resource_set",
    "permission_endpoint": "https://am.example.com:8443/am/uma/realms/root/realms/alpha/permission_request"
}
```

The JSON object returned includes the following configuration information:

* `issuer`

  The URI of the issuing authorization server.

* `grant_types_supported`

  The supported OAuth 2.0 grant types.

* `token_endpoint`

  The URI to request tokens.

* `authorization_endpoint`

  The URI to request authorization for issuing a token.

* `introspection_endpoint`

  The URI to introspect an RPT.

  For more information, see [/oauth2/introspect](../am-oauth2/oauth2-introspect-endpoint.html).

* `resource_registration_endpoint`

  The URI for a resource server to register a resource.

  For more information, see [/uma/resource\_set](endpoint-resource_set.html).

* `dynamic_client_endpoint`

  The URI for registering a dynamic client.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Resource servers and clients need to be able to discover the UMA provider for a resource owner. You should consider redirecting requests to URIs at the server root, such as `https://www.example.com/.well-known/uma2-configuration`, to the well-known URIs in AM's space.For example, if your UMA provider is in a subrealm named `subrealm`, you could map the following URI: `https://www.example.com:8080/openam/uma/realms/root/realms/subrealm/.well-known/uma2-configuration`.AM supports a provider service that lets a realm have a configured option for obtaining the base URL (including protocol) for components that need to return a URL to the client. This service is used to provide the URL base that is used in the `.well-known` endpoints used in OpenID Connect 1.0 and UMA.For more information, see [Configuring the Base URL Source Service](../security/reverse-proxy.html#configure-base-url-source). |

---

---
title: /uma/claims_gathering
description: PingAM endpoint for handling interactive claims-gathering requests during User-Managed Access flows
component: pingam
version: 8.1
page_id: pingam:uma:endpoint-claims_gathering
canonical_url: https://docs.pingidentity.com/pingam/8.1/uma/endpoint-claims_gathering.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["User-Managed Access (UMA)", "Endpoints", "Claims Gathering Requests"]
page_aliases: ["uma-guide:endpoint-claims_gathering.adoc"]
---

# /uma/claims\_gathering

AM-specific endpoint for handling interactive claims-gathering requests during UMA flows.

|   |                                                                                                                                                                                                           |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | This endpoint is protected by the CSRF parameter, similar to the `/oauth2/authorize` endpoint. However, the CSRF parameter only takes the value of the SHA-256 hash of the requesting party's session ID. |

> **Collapse: Supported HTTP methods**
>
> | Action  | HTTP method |
> | ------- | ----------- |
> | Request | GET         |
> | Request | POST        |

For GET requests, the endpoint does the following:

* validates that the request has all the required parameters

* checks that the provided `claims_redirect_uri` is valid

* checks whether a session was provided with the request

* if there is a session, validates the session and checks whether it was obtained by authenticating with the claims gathering tree

* if the session is invalid, rotates the permission ticket, and redirects the user to the claims gathering tree for authentication

* if the session is valid, displays a consent page, where the end user can request that a PCT *(tooltip: persisted claims token)* be issued.

For POST requests, the endpoint does the following:

* validates the CSRF token

* saves the authorization decision and the gathered claims in the permission ticket, and rotates the ticket

* returns the new ticket to the `claims_redirect_uri` so that the client can continue with the authorization flow

To authenticate to the endpoint, send the SSO token of the resource owner as the value of the `iPlanetDirectoryPro` header.

---

---
title: /uma/permission_request
description: Request permission tickets from the authorization server during the UMA 2.0 grant flow by sending a POST request with resource ID and scopes
component: pingam
version: 8.1
page_id: pingam:uma:endpoint-permission_request
canonical_url: https://docs.pingidentity.com/pingam/8.1/uma/endpoint-permission_request.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["User-Managed Access (UMA)", "Endpoints", "Permission Request"]
page_aliases: ["uma-guide:endpoint-permission_request.adoc"]
---

# /uma/permission\_request

UMA permission endpoint, as defined in the [Federated Authorization for User-Managed Access (UMA) 2.0](https://docs.kantarainitiative.org/uma/wg/oauth-uma-federated-authz-2.0-08.html#permission-endpoint) specification.

Use this endpoint to request permission tickets to the authorization server during the [UMA grant flow](uma-grant-flow.html).

> **Collapse: Supported HTTP methods**
>
> | Action  | HTTP method |
> | ------- | ----------- |
> | Request | POST        |

You must compose the path to the token endpoint addressing the specific realm where the token will be issued. For example, `https://am.example.com:8443/am/uma/realms/root/realms/subrealm1/permission_request`.

The permission request endpoint does not support any parameters. To authenticate to the endpoint, send an `Authorization: Bearer` header with the PAT of the resource owner.

To request a ticket, send an HTTP POST request to the endpoint specifying the resource and the scope that the permission ticket applies to in the payload, as a JSON object that follows the UMA 2.0 specification. For example:

```bash
$ curl -X POST \
--header 'authorization: Bearer 057ad16f-7dba-4049-9f34-e609d230d43a' \
--header 'content-type: application/json' \
--data '[
    {
        "resource_id" : "ef4d750e-3831-483b-b395-c6f059b5e15d0",
        "resource_scopes" : ["download"]
    }
]' \
"https://am.example.com:8443/am/uma/realms/root/realms/alpha/permission_request"
{
    "ticket": "eyJ0eXAiOiJ…​XPeJi3E"
}
```

Both of the objects in the JSON body are required. To obtain the resource ID, query the [/uma/resource\_set](endpoint-resource_set.html) endpoint.

|   |                                                                                                                                                                                     |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The default lifetime for a permission ticket is 120 seconds. To change it, go to Realms > *realm name* > Services > UMA Provider, and edit the Permission Ticket Lifetime property. |

For an example of requesting a permission ticket in the flow, see [UMA grant flow](uma-grant-flow.html).

---

---
title: /uma/resource_set
description: Use the UMA resource registration endpoint to register, read, update, delete, and list resources for resource owners in User-Managed Access (UMA) 2.0
component: pingam
version: 8.1
page_id: pingam:uma:endpoint-resource_set
canonical_url: https://docs.pingidentity.com/pingam/8.1/uma/endpoint-resource_set.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["User-Managed Access (UMA)", "Endpoints", "Resource Sets"]
page_aliases: ["uma-guide:endpoint-resource_set.adoc"]
---

# /uma/resource\_set

This endpoint is the UMA resource registration endpoint, as defined in the [Federated Authorization for User-Managed Access (UMA) 2.0](https://docs.kantarainitiative.org/uma/wg/oauth-uma-federated-authz-2.0-08.html#resource-registration-endpoint) specification.

Use this endpoint to register, read, delete, edit, and list resources for a particular resource owner.

> **Collapse: Supported HTTP methods**
>
> | Action   | HTTP method |
> | -------- | ----------- |
> | Register | POST        |
> | Read     | GET         |
> | Update   | PUT         |
> | Delete   | DELETE      |
> | List     | GET         |

You must compose the path to the token endpoint addressing the specific realm where the token will be issued. For example, `https://am.example.com:8443/am/uma/realms/root/realms/alpha/resource_set`.

The resource registration endpoint does not support any parameters. To authenticate to the endpoint, send an `Authorization: Bearer` header with the PAT of the resource owner.

To create and update resources, add their description to the body of the call as a JSON document that follows the UMA 2.0 specification. For example:

```json
{
   "resource_scopes": [
       "view", "comment", "download"
   ],
   "name": "My Resource Name",
   "description": "An example resource stored in resourceserver.example.com",
   "type": "https://resourceserver.example.com/resources/",
   "icon_uri": "https://resourceserver.example.com/resources/resources.png"
}
```

The `resource_scopes` object is the only required object, and indicates the scopes that can be requested for the resource. Scope descriptions are not supported.

When reading, updating, and deleting a resource, you must include the resource ID in the URL. For example:

```bash
$ curl \
--header "Authorization: Bearer 515d6551-6512-5279-98b6-c0ef3f03a723" \
"https://am.example.com:8443/am/uma/realms/root/realms/alpha/resource_set/126615ba-b7fd-4660-b281-bae81aa45f7c0"
```

For examples of the different REST calls, see [UMA resources](uma-resource-sets.html).

---

---
title: AM as UMA authorization server
description: Configure PingAM as a User-Managed Access (UMA) authorization server to grant delegated consent and manage resource access policies on behalf of resource owners
component: pingam
version: 8.1
page_id: pingam:uma:uma-introduction
canonical_url: https://docs.pingidentity.com/pingam/8.1/uma/uma-introduction.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["User-Managed Access (UMA)", "Authorization", "Delegated Consent", "UMA Discovery"]
page_aliases: ["uma-guide:uma-introduction.adoc"]
section_ids:
  uma-specifications: Supported specifications
  uma-deployment-considerations: Deployment considerations
  uma-discovery-intro: UMA discovery
---

# AM as UMA authorization server

In the role of UMA authorization server, AM grants delegated consent to a *requesting party* on behalf of the resource owner, to authorize who and what can access their data, and for how long.

|   |                                                                                                                                       |
| - | ------------------------------------------------------------------------------------------------------------------------------------- |
|   | Before you configure UMA in your environment, familiarize yourself with the OAuth 2.0 standards and AM's implementation of OAuth 2.0. |

## Supported specifications

AM supports the following UMA grants and specifications:

* [User-Managed Access (UMA) 2.0 Grant for OAuth 2.0 Authorization](https://docs.kantarainitiative.org/uma/wg/oauth-uma-grant-2.0-08.html)

  This specification defines an OAuth 2.0 extension grant, allowing a party-to-party authorization mechanism where entities in a requesting party role can access protected resources authorized by the resource owner using authorization policies. The specification also defines how a resource owner can configure an authorization server with authorization grant rules to run asynchronously with the resource server using an RPT versus granting consent at runtime.

  For more information, see [UMA grant flow](uma-grant-flow.html).

* [Federated Authorization for User-Managed Access (UMA) 2.0](https://docs.kantarainitiative.org/uma/wg/oauth-uma-federated-authz-2.0-08.html)

  This specification defines the loosely coupled federation of the authorization process by means of multiple resource servers in different domains that communicate with the centralized authorization server and acts on behalf of a resource owner. The authorization server can reside locally or in another domain from the resource server(s).

|   |                                                                                                                                                                                                          |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | See the complete list of supported [OpenID Connect](../am-reference/am-supported-standards.html#standards-oidc) and [OAuth 2.0](../am-reference/am-supported-standards.html#standards-oauth2) standards. |

## Deployment considerations

The UMA 2.0 process largely involves the UMA 2.0 Grant flow, in which a requesting party obtains an RPT to access the resource, and resource registration which can occur at various stages through the UMA process by the resource owner. These stages could occur at initial resource creation, when needed for policy creation, and at resource access attempt.

Find more information in [Considerations Regarding Resource Registration Timing and Mechanism](https://kantara.atlassian.net/wiki/spaces/uma/pages/4849800/UMA+Implementer+s+Guide#UMAImplementer'sGuide-rreg-timingConsiderationsRegardingResourceRegistrationTimingandMechanism) in the *UMA Implementer's Guide*.

AM stores UMA-related data, such as resources, audit information, and labels in the configuration store by default, but this information may grow very large in environments with many users, or in environments where users own many resources.

In production environments, configure at least one external UMA store to hold UMA information.

For more information, see [UMA stores](configure-uma-storage.html).

## UMA discovery

In order to let relying parties or clients discover the URL of the UMA provider and its configuration for an end user, AM exposes the following REST endpoints:

* [/.well-known/webfinger](../am-oidc1/rest-api-oidc-discovery-webfinger.html)

* [/uma/.well-known/uma2-configuration](endpoint-configuration.html)

Discovery relies on [WebFinger](https://datatracker.ietf.org/doc/html/draft-ietf-appsawg-webfinger), a protocol to discover information about people and other entities using standard HTTP methods. WebFinger uses [Well-Known URIs](https://datatracker.ietf.org/doc/html/rfc5785), which defines the path prefix `/.well-known/` for the URLs defined by OpenID Connect Discovery.

Just like they do for OpenID Connect flows, relying parties need to find the right *host:port/deployment-uri* combination to locate the well-known endpoints. You must manage the redirection to AM using your proxies, load balancers, and others, such that a request to `http://www.example.com/.well-known/webfinger` reaches, for example, `https://am.example.com:8443/am/.well-known/webfinger`.

---

---
title: Configure external UMA stores
description: Configure external User-Managed Access stores at the server level to store UMA resources, audit data, pending requests, and resource labels across all realms
component: pingam
version: 8.1
page_id: pingam:uma:configure-external-uma-stores
canonical_url: https://docs.pingidentity.com/pingam/8.1/uma/configure-external-uma-stores.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["User-Managed Access (UMA)", "Storage", "Configuration", "Audit", "Requests", "Resoure Labels"]
page_aliases: ["uma-guide:configure-external-uma-stores.adoc"]
section_ids:
  to-configure-uma-external-rs-store: Configure an UMA resource store
  to-configure-uma-external-audit-store: Configure an UMA audit store
  to-configure-uma-external-pending-requests-store: Configure an UMA pending requests store
  to-configure-uma-external-resource-sets-labels-store: Configure an UMA resource labels store
  authenticate_to_an_uma_store_using_mtls: Authenticate to an UMA store using mTLS
---

# Configure external UMA stores

UMA stores can only be configured at the server level so that all realms in the environment can access them. The procedures in this section show you how to configure the stores across all instances in your environment.

## Configure an UMA resource store

UMA resource stores inherit most of their properties from the defaults.

Learn more in [Configure servers](../setup/deployment-configuration-reference.html#servers-configuration).

1. In the AM admin UI, go to Configure > Server Defaults > UMA > UMA Resource Store.

   * In the Store Mode field, choose External Token Store.

   * In the Root Suffix field, enter the base DN of the store. For example, `dc=uma-resources,dc=example,dc=com`.

   * Save your work.

2. Go to Configure > Server Defaults > UMA > External UMA Resource Store Configuration.

   * Enter the properties for the store.

     Find information about the available settings in [UMA properties](../setup/server-uma.html).

   * Save your work.

## Configure an UMA audit store

UMA audit stores inherit most of their configuration properties from the defaults.

Learn more in [Configure servers](../setup/deployment-configuration-reference.html#servers-configuration).

1. In the AM admin UI, go to Configure > Server Defaults > UMA > UMA Audit Store.

   * From the Store Mode drop-down list, choose External Token Store.

   * In the Root Suffix field, enter the base DN of the store.

     For example, `dc=uma-audit,dc=example,dc=com`.

   * Save your work.

2. Go to Configure > Server Defaults > UMA > External UMA Audit Store Configuration.

   * Enter the properties for the store.

     Find information about the available settings in [UMA properties](../setup/server-uma.html).

   * Save your work.

## Configure an UMA pending requests store

UMA pending requests stores inherit most of their configuration properties from the defaults.

Learn more in [Configure servers](../setup/deployment-configuration-reference.html#servers-configuration).

1. Go to Configure > Server Defaults > UMA > Pending Requests Store.

   * From the Store Mode drop-down list, choose External Token Store.

   * In the Root Suffix field, enter the base DN of the store.

     For example, `dc=uma-pending,dc=example,dc=com`.

   * Save your work.

2. Go to Configure > Server Defaults > UMA > External Pending Requests Store Configuration.

   * Enter the properties for the store.

     Find information about the available settings in [UMA properties](../setup/server-uma.html).

   * Save your work.

## Configure an UMA resource labels store

UMA resource labels stores inherit most of their configuration properties from the defaults.

Learn more in [Configure servers](../setup/deployment-configuration-reference.html#servers-configuration).

1. In the AM admin UI, go to Configure > Server Defaults > UMA > UMA Resource Labels Store.

   * From the Store Mode drop-down list, choose External Token Store.

   * In the Root Suffix field, enter the base DN of the store.

     For example, `dc=uma-labels,dc=example,dc=com`.

   * Save your work.

2. Go to Configure > Server Defaults > UMA > External UMA Resource Labels Store Configuration.

   * Enter the properties for the store.

     Find information about the available settings in [UMA properties](../setup/server-uma.html).

   * Save your work.

## Authenticate to an UMA store using mTLS

By default, AM authenticates to external UMA stores using simple (username/password) authentication. To enhance security, you can configure mutual TLS (mTLS) authentication which lets AM authenticate using a trusted certificate.

Learn more in [Secure authentication to datastores](../security/secure-data-stores.html).

---

---
title: Extend UMA
description: Extend UMA services with custom filters for resource registration, permission requests, authorization, and resource sharing workflows in PingAM
component: pingam
version: 8.1
page_id: pingam:uma:uma-customization
canonical_url: https://docs.pingidentity.com/pingam/8.1/uma/uma-customization.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["User-Managed Access (UMA)", "Extentions", "Endpoints"]
page_aliases: ["uma-guide:uma-customization.adoc"]
section_ids:
  ext-resource-registration: Resource registration extension point
  ext-permission-requests: Permission request extension point
  ext-authorization-requests: Authorization request extension point
  ext-resource-delegation: Resource sharing extension point
---

# Extend UMA

AM exposes extension points that enable you to extend UMA services when built-in functionality does not fit your deployment.

AM provides a number of extension points for extending the UMA workflow that are provided as filters and that are dynamically loaded by using the [ServiceLoader](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/ServiceLoader.html) during the UMA workflow.

## Resource registration extension point

Use the `ResourceRegistrationFilter` extension point to extend UMA resource registration functionality.

**Resource registration extension methods**

| Method                       | Parameters                                     | Description                                                                                                                           |
| ---------------------------- | ---------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| `beforeResourceRegistration` | *resourceSet* (type: `ResourceSetDescription`) | Invoked before a resource is registered in the backend.Changes made to the *resourceSet* object at this stage *will* be persisted.    |
| `afterResourceRegistration`  | *resourceSet* (type: `ResourceSetDescription`) | Invoked after a resource is registered in the backend.Changes made to the *resourceSet* object at this stage *will not* be persisted. |

## Permission request extension point

Use the `PermissionRequestFilter` extension point to extend UMA permission request functionality.

**Permission request extension methods**

| Method                | Parameters                                                                                                                 | Description                                     |
| --------------------- | -------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------- |
| `onPermissionRequest` | *resourceSet* (type: `ResourceSetDescription`)*requestedScopes* (type: `Set<String>`)*requestingClientId* (type: `String`) | Invoked before a permission request is created. |

## Authorization request extension point

Use the `RequestAuthorizationFilter` extension point to extend UMA authorization functionality.

**Authorization request extension methods**

| Method                         | Parameters                                                                                                                                                                                  | Description                                                                                                                           |
| ------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| `beforeAuthorization`          | *permissionTicket* (type: `PermissionTicket`)*requestingParty* (type: `Subject`)*resourceOwner* (type: `Subject`)*requestedScope* (type: `Set<String>`)                                     | Invoked before authorization of a request is attempted.Throws `UmaException` if authorization of the request should not be attempted. |
| `afterSuccessfulAuthorization` | *permissionTicket* (type: `PermissionTicket`)*requestingParty* (type: `Subject`)*resourceOwner* (type: `Subject`)*requestedScope* (type: `Set<String>`)*grantedScope* (type: `Set<String>`) | Invoked after a successful request authorization attempt.                                                                             |
| `afterFailedAuthorization`     | *permissionTicket* (type: `PermissionTicket`)*requestingParty* (type: `Subject`)*resourceOwner* (type: `Subject`)*requestedScope* (type: `Set<String>`)                                     | Invoked after a failed request authorization attempt.                                                                                 |

## Resource sharing extension point

Use the `ResourceDelegationFilter` extension point to extend UMA resource sharing functionality.

**Resource sharing extension methods**

| Method                             | Parameters                                                                   | Description                                                                                                                                                                                                                                                                                   |
| ---------------------------------- | ---------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `beforeResourceShared`             | *umaPolicy* (type: `UmaPolicy`)                                              | Invoked before creating a sharing policy for a resource.Changes to the *umaPolicy* object at this stage *will* be persisted.Throws `ResourceException` if a sharing policy for the resource should not be created.                                                                            |
| `afterResourceShared`              | *umaPolicy* (type: `UmaPolicy`)                                              | Invoked after creating a sharing policy for a resource.Changes to the *umaPolicy* object at this stage *will not* be persisted.                                                                                                                                                               |
| `beforeResourceSharedModification` | *currentUmaPolicy* (type: `UmaPolicy`)*updatedUmaPolicy* (type: `UmaPolicy`) | Invoked before altering the sharing policy of a resource.Changes to the *updatedUmaPolicy* object at this stage *will* be persisted.Throws `ResourceException` if the sharing policy of the resource should not be modified.                                                                  |
| `onResourceSharedDeletion`         | *umaPolicy* (type: `UmaPolicy`)                                              | Invoked before deleting the sharing policy of a resource.Throws `ResourceException` if the sharing policy of the resource should not be deleted.                                                                                                                                              |
| `beforeQueryResourceSets`          | *userId* (type: `String`)*queryFilter* (type: `QueryFilter<JsonPointer>`)    | Invoked before querying the resources owned or shared with a user.The *userId* parameter provides the ID of the user making the query request.The *queryFilter* parameter provides the incoming request query filter.Returns a `QueryFilter` that can be used to return the user's resources. |

---

---
title: First steps with UMA
description: Learn how User-Managed Access (UMA) 2.0 extends OAuth 2.0 to give resource owners granular control over protected resources through centralized authorization policies
component: pingam
version: 8.1
page_id: pingam:uma:uma-first-steps
canonical_url: https://docs.pingidentity.com/pingam/8.1/uma/uma-first-steps.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["User-Managed Access (UMA)", "OAuth 2.0", "Actors", "Actions"]
page_aliases: ["uma-guide:uma-first-steps.adoc"]
---

# First steps with UMA

UMA 2.0 is a lightweight access control protocol that defines a centralized workflow to let an entity (user or corporation) manage access to their resources.

It extends the OAuth 2.0 protocol and gives resource owners granular management of their protected resources by creating authorization policies on a centralized authorization server, such as AM.

UMA 2.0 uses the OAuth 2.0 actors in extended ways and introduces the *requesting party* as a new actor:

![AM acts as the Authorization Server in the UMA workflow.](_images/uma-workflow-overview.png)Figure 1. Actors and actions in the UMA 2.0 workflow

> **Collapse: UMA actors explained**
>
> * Resource owner
>
>   The resource owner is a user or legal entity that can grant access to a protected resource.
>
> * Client
>
>   The client is an application that can make requests with the resource owner's authorization, and on the requesting party's behalf.
>
> * Resource server
>
>   The resource server hosts resources on a resource owner's behalf, and can accept and respond to requests for protected resources.
>
>   You can configure [PingGateway](https://docs.pingidentity.com/pinggateway/2025.11/gateway-guide/uma.html) as an UMA resource server.
>
> * Authorization server
>
>   The authorization server protects resources hosted on a resource server, on behalf of resource owners.
>
>   You can set up AM to function as an authorization server in an UMA 2.0 deployment. AM provides an UMA provider service, an UMA grant type handler, and endpoints for resource registration, permission ticket generation, and UMA token introspection. AM also uses its OAuth provider service to generate OIDC ID tokens, and to provide claim tokens and policies for UMA resource management.
>
> * Requesting party
>
>   The requesting party is a user or legal entity that uses a client to access a protected resource. The requesting party may or may not be the same as the resource owner. This actor is specific to the UMA protocol.

> **Collapse: UMA actions explained**
>
> 1. Manage
>
>    The resource owner manages their resources on the resource server.
>
> 2. Protect
>
>    The authorization server and the resource server are loosely coupled elements in an UMA deployment. Because of this, the authorization server can onboard multiple resource servers in any domain. To onboard multiple resource servers, the authorization server exposes a protection API that provides resource registration, permission tickets, and token inspection endpoints to bind the resource server and authorization server.
>
>    The API endpoints are protected by a PAT *(tooltip: Protection API Token)*—an OAuth 2.0 token with a specific scope of `uma_protection`—which establishes a trust relationship between the two components.
>
>    For more information, see the [/uma/resource\_set](endpoint-resource_set.html) endpoint.
>
> 3. Control
>
>    The resource owner controls who has access to their registered resources, by creating policies on the authorization server. This lets the resource owner grant consent asynchronously, rather than when the resource is requested. As a result, the requesting party can access data using an RPT *(tooltip: Requesting party token)*.
>
>    For more information, see the [/json/users/{user}/uma/policies](endpoint-policies.html) endpoint.
>
> 4. Authorize
>
>    The client, acting on behalf of the requesting party, uses the authorization server's UMA Grant Flow to acquire an RPT *(tooltip: Requesting party token)*. The RPT is a token that is unique to the requesting party, client, authorization server, resource server, and resource owner. The requesting party and the resource owner can interact with their applications at any time. In some cases, the requesting party and the resource owner can be the same entity.
>
>    This interaction allows for party-to-party data sharing and delegated access authorization. The resource owner grants consent by policy, using the authorization server, rather than by issuing a token at runtime. Consent is thus granted *asynchronously*.
>
> 5. Access
>
>    The client presents the RPT to the resource server, which verifies its validity with the authorization server. If the token is valid and contains sufficient permissions, the resource server returns the protected resource to the requesting party.

The [example use case](uma-example.html) helps you configure and demonstrate the UMA flow.

When you are familiar with the actors and the flow, read the rest of these topics to configure UMA in production environments, and to understand the UMA functionality that the AM REST APIs offer.

For additional UMA use cases, see:

* [Case Studies](https://kantara.atlassian.net/wiki/spaces/uma/pages/4850549/Case+Studies)

* [The Kantara Initiative](https://kantarainitiative.org)

---

---
title: Manage UMA user and favorite labels
description: Use REST endpoints to create, query, and delete user and favorite labels for managing User-Managed Access resources in PingAM
component: pingam
version: 8.1
page_id: pingam:uma:uma-labels-with-REST-users
canonical_url: https://docs.pingidentity.com/pingam/8.1/uma/uma-labels-with-REST-users.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["User-Managed Access (UMA)", "User Labels", "REST", "Resource Labels"]
page_aliases: ["uma-guide:uma-labels-with-REST-users.adoc"]
section_ids:
  create-resource-set-labels-for-a-user-with-REST: Create user labels (REST)
  query-resource-set-labels-for-a-user-with-REST: Query user labels (REST)
  delete-resource-set-labels-for-a-user-with-REST: Delete user labels (REST)
  apply-user-labels-to-resource-sets: Label resources (UI)
  apply-star-label-to-resource-set: Label resources as favorites (UI)
---

# Manage UMA user and favorite labels

The `/json/users/username/oauth2/resources/labels` REST endpoint lets users manage user and favorite labels. It also provides built-in user pages in the UI.

When using the REST endpoint, specify the `username` in the URL, and provide the SSO token of that user in the `iPlanetDirectoryPro` header.

## Create user labels (REST)

1. Log in as the resource owner to obtain an SSO token:

   ```bash
   $ curl \
   --request POST \
   --header "Content-Type: application/json" \
   --header "X-OpenAM-Username: alice" \
   --header "X-OpenAM-Password: Ch4ng31t" \
   --header "Accept-API-Version: resource=2.0, protocol=1.0" \
   'https://am.example.com:8443/am/json/realms/root/realms/alpha/authenticate'
   {
       "tokenId":"AQIC5wM2LY4S…​Q4MTE4NTA2*",
       "successUrl":"/am/console",
       "realm":"/alpha"
   }
   ```

   The value returned in the `tokenId` element is the SSO token of the resource owner, *Alice*. Use this value as the contents of the `iPlanetDirectoryPro` cookie in the next step.

2. To create a new user label, send a POST request with the name of the new user label and the type, `USER`:

   ```bash
   $ curl \
   --request POST \
   --header 'Accept-API-Version: resource=1.0' \
   --header "Content-Type: application/json" \
   --header "iPlanetDirectoryPro: AQIC5wM2LY4S…​Q4MTE4NTA2*" \
   --data '{
       "name" : "New Resource Label",
       "type" : "USER"
   }' \
   "https://am.example.com:8443/am/json/realms/root/realms/alpha/users/alice/oauth2/resources/labels"
   {
     "_id": "f2069e8c-bd3e-430a-b2f6-7b9f9b523e5a0",
     "_rev": "27048065",
     "name": "New Resource Label",
     "type": "USER"
   }
   ```

   |   |                                                                      |
   | - | -------------------------------------------------------------------- |
   |   | If you set the `type` object as `STAR`, you create a favorite label. |

   On success, AM returns an HTTP 201 Created status code, and the unique identifier of the new user label in the `_id` field. Note that the label is not yet associated with a resource. To apply the new label to a resource, see [Update an UMA resource (REST)](uma-resource-sets.html#update-an-uma-resource-set).

## Query user labels (REST)

1. Log in as the resource owner to obtain an SSO token:

   ```bash
   $ curl \
   --request POST \
   --header "Content-Type: application/json" \
   --header "X-OpenAM-Username: alice" \
   --header "X-OpenAM-Password: Ch4ng31t" \
   --header "Accept-API-Version: resource=2.0, protocol=1.0" \
   'https://am.example.com:8443/am/json/realms/root/realms/alpha/authenticate'
   {
       "tokenId":"AQIC5wM2LY4S…​Q4MTE4NTA2*",
       "successUrl":"/am/console",
       "realm":"/alpha"
   }
   ```

   The value returned in the `tokenId` element is the SSO token of the resource owner, *Alice*. Use this value as the contents of the `iPlanetDirectoryPro` cookie in the next step.

2. To query the labels belonging to a user, send a GET request with `_queryFilter=true`:

   ```bash
   $ curl \
   --header "iPlanetDirectoryPro: AQIC5wM2LY4S…​Q4MTE4NTA2*" \
   --header "Accept-API-Version: resource=1.0" \
   "https://am.example.com:8443/am/json/realms/root/realms/alpha/users/alice/oauth2/resources/labels?_queryFilter=true"
   {
       "result": [
           {
               "_id": "46a3392f-1d2f-4643-953f-d51ecdf141d44",
               "name": "2022/June/Bristol",
               "type": "USER"
           },
           {
               "_id": "60b785c2-9510-40f5-85e3-9837ac272f1b1",
               "name": "Top Level/Second Level/My Label",
               "type": "USER"
           },
           {
               "_id": "ed5fad66-c873-4b80-93bb-92656eb06deb0",
               "name": "starred",
               "type": "STAR"
           },
           {
               "_id": "db2161c0-167e-4195-a832-92b2f578c96e3",
               "name": "New Resource Set Label",
               "type": "USER"
           }
       ],
       "resultCount": 4,
       "pagedResultsCookie": null,
       "totalPagedResultsPolicy": "NONE",
       "totalPagedResults": -1,
       "remainingPagedResults": -1
   }
   ```

## Delete user labels (REST)

1. Log in as the resource owner to obtain an SSO token:

   ```bash
   $ curl \
   --request POST \
   --header "Content-Type: application/json" \
   --header "X-OpenAM-Username: alice" \
   --header "X-OpenAM-Password: Ch4ng31t" \
   --header "Accept-API-Version: resource=2.0, protocol=1.0" \
   'https://am.example.com:8443/am/json/realms/root/realms/alpha/authenticate'
   {
       "tokenId":"AQIC5wM2LY4S…​Q4MTE4NTA2*",
       "successUrl":"/am/console",
       "realm":"/alpha"
   }
   ```

   The value returned in the `tokenId` element is the SSO token of the resource owner, *Alice*. Use this value as the contents of the `iPlanetDirectoryPro` cookie in the next step.

2. To delete a user label, send a DELETE request, including the ID of the label in the URL:

   ```bash
   $ curl \
   --request DELETE \
   --header "iPlanetDirectoryPro: AQIC5wM2LY4S…​Q4MTE4NTA2*" \
   --header "Accept-API-Version: resource=1.0" \
   "https://am.example.com:8443/am/json/realms/root/realms/alpha/users/alice/oauth2/resources/labels/46a3392f-1d2f-4643-953f-d51ecdf141d44"
   {
       "_id": "46a3392f-1d2f-4643-953f-d51ecdf141d44",
       "name": "2022/June/Bristol",
       "type": "USER"
   }
   ```

   On success, AM returns an HTTP 200 OK status code, and a JSON representation of the user label that was removed.

## Label resources (UI)

1. Log in to the UI as a user. The profile page is displayed.

2. Go to Shares > Resources > My Resources, and click the name of the resource to add labels to.

3. On the resource details page, click Edit Labels.

   In the edit box that is displayed, you can:

   1. Enter the label you want to add to the resource, and click `Enter`.

      If you enter a label containing forward slash (`/`) characters, a hierarchy of each component of the label is created. The resource only appears in the last component of the hierarchy.

      For example, this image shows the result of the label: `2015/October/Bristol`:

      ![Organize resources by using labels with several components](_images/uma-resource-label-hierarchy.png)

   2. Click an existing label, and then press `Delete` or `Backspace` to delete the label from the resource.

4. When you have finished editing labels you can:

   1. Click the checkmark button to save any changes made.

   2. Click the X button to cancel any changes made.

## Label resources as favorites (UI)

Mark resources as favorites to have them appear on the Starred page.

1. Log in to AM as the resource owner user. The profile page is displayed.

2. Go to Shares > Resources > My Resources, and click the name of the resource to add to the list of favorites.

3. On the resource details page, click the star icon:

   ![Add the star label to a resource to display it in the Starred list.](_images/uma-resource-label-star.png)

   To view the list of favorite resources, click Starred.

---

---
title: Prepare external UMA datastores
description: Configure PingDS instances as external datastores for User-Managed Access (UMA) resources, resource labels, audit messages, and pending requests
component: pingam
version: 8.1
page_id: pingam:uma:prepare-uma-store
canonical_url: https://docs.pingidentity.com/pingam/8.1/uma/prepare-uma-store.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["User-Managed Access (UMA)", "Storage", "Configuration", "Directory Server"]
page_aliases: ["uma-guide:prepare-uma-store.adoc"]
section_ids:
  prepare-ds-for-uma: Install and configure PingDS for UMA data
  creating-uma-base-dn: Create an UMA store base DN
  prepare-bind-user-for-uma: Create an UMA store bind account
  prepare-schema-for-uma: Create a schema for UMA-related data
---

# Prepare external UMA datastores

This page explains how to prepare DS instances as external UMA datastores. You can create separate DS instances to store the following UMA-related data:

* Resources

* Resource labels

* UMA audit messages

* Pending requests

The procedure for preparing external DS instances is similar for each of the UMA-related data types. The steps to perform are as follows:

1. If you haven't already done so, install PingDS.

2. As an administrative user, for example, `uid=admin`:

   1. Create a backend and base DN entry in the external store.

   2. Create a user account with the minimum required privileges. This user lets AM bind to the directory server, and access necessary data.

   3. Apply the relevant schema to the directory.

      Each data type requires a specific set of LDIF schema files.

      > **Collapse: LDIF files for UMA datastores**
      >
      > | Datastore          | LDIF Files                                                                                                                                                                               |
      > | ------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      > | Resources          | \*`/path/to/tomcat/webapps/am/WEB-INF/template/ldif/opendj/opendj_uma_resource_sets.ldif`                                                                                                |
      > | Resource labels    | \*`/path/to/tomcat/webapps/am/WEB-INF/template/ldif/opendj/opendj_uma_labels_schema.ldif`\*`/path/to/tomcat/webapps/am/WEB-INF/template/ldif/opendj/opendj_uma_resource_set_labels.ldif` |
      > | UMA audit messages | \*`/path/to/tomcat/webapps/am/WEB-INF/template/ldif/opendj/opendj_uma_audit.ldif`                                                                                                        |
      > | Pending requests   | \*`/path/to/tomcat/webapps/am/WEB-INF/template/ldif/opendj/opendj_uma_pending_requests.ldif`                                                                                             |

|   |                                                                                                                                                                                                                                                        |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | You can use a single external DS instance with multiple backend configurations to store each of the UMA-related data types. Change the steps in the sections below to apply the backends, schema, and administrative accounts to a single DS instance. |

This page shows how to set up a DS instance to store UMA resources. Repeat these procedures with the relevant schema files to set up a DS instance to store other types of UMA-related data.

The commands in this section use example values for user IDs and port numbers. Adjust the values to match your deployment.

## Install and configure PingDS for UMA data

1. Download and install PingDS.

   * Generate a DS deployment ID, unless you already have one:

     ```bash
     $ /path/to/opendj/dskeymgr create-deployment-id --deploymentIdPassword password
     deployment-id
     ```

     Save the deployment ID and deployment ID password, and keep the password secret. Use the same deployment ID and password for all servers in the same environment; for example, if you use replicated DS servers. Replication is not covered in this example.

   * DS doesn't provide an UMA setup profile; create an example DS UMA server by providing the parameters in a single `setup` command. For example:

     ```bash
     $ /path/to/opendj/setup \
     --instancePath '/path/to/opendj' \
     --serverId uma-resource-server\
     --deploymentId deployment-id \
     --deploymentIdPassword deployment-id-password \
     --rootUserDN uid=admin \
     --rootUserPassword str0ngAdm1nPa55word \
     --hostname uma-rs.example.com \
     --adminConnectorPort 4444 \
     --ldapPort 1389 \
     --enableStartTls \
     --ldapsPort 1636 \
     --httpsPort 8443 \
     --acceptLicense
     ```

     Find additional options for the `setup` command in [setup](https://docs.pingidentity.com/pingds/8.1/tools-reference/setup.html) in the *PingDS 8.1 Tools Reference*.

     DS doesn't start automatically after installation; **don't** start the server until you have created a backend and added the required schemas at the end of this section.

2. When the install has completed, create a backend for UMA resource data, named `umaRsStore`, and prepare for a base DN of `dc=uma-resources,dc=example,dc=com`:

   ```bash
   $ /path/to/opendj/bin/dsconfig create-backend \
   --hostname 'uma-rs.example.com' \
   --port 4444 \
   --usePkcs12TrustStore /path/to/opendj/config/keystore \
   --truststorepassword:file /path/to/opendj/config/keystore.pin \
   --backend-name umaRsStore \
   --set base-dn:dc=uma-resources,dc=example,dc=com \
   --set enabled:true \
   --type je \
   --bindDN uid=admin \
   --bindPassword str0ngAdm1nPa55word \
   --offline
   The JE Backend was created successfully
   ```

3. Share the UMA store certificate with the AM container to prepare for TLS/LDAPS. AM must connect to UMA stores over secure connections.

   DS is configured to require secure connections by default. Share the DS certificate with the AM container before continuing.

   > **Collapse: Share the DS certificate with AM**
   >
   > * On the DS host, export the DS CA certificate.
   >
   >   DS uses a deployment ID and password to generate a CA key pair. Learn more in [Deployment IDs](https://docs.pingidentity.com/pingds/8.1/security-guide/pki.html#about-deployment-ids).
   >
   >   Use the `dskeymgr` command to export the CA certificate:
   >
   >   ```bash
   >   $ /path/to/opendj/bin/dskeymgr \
   >   export-ca-cert \
   >   --deploymentId $DEPLOYMENT_ID \
   >   --deploymentIdPassword password \
   >   --outputFile /path/to/ca-cert.pem
   >   ```
   >
   > * Copy the `ca-cert.pem` file to an accessible location on the AM host.
   >
   > - Import the DS CA certificate into the AM truststore:
   >
   >   ```bash
   >   $ keytool \
   >   -importcert \
   >   -file /path/to/ca-cert.pem \
   >   -keystore /path/to/am/security/keystores/truststore
   >   -storepass truststore-password
   >   ```
   >
   > Learn more about configuring AM's truststore in [Prepare the truststore](../installation/prepare-trust-store.html).

## Create an UMA store base DN

1. Create an LDIF file to add the base DN to the UMA store, and save the file as `add-uma-base-dn.ldif`:

   ```ldif
   dn: dc=uma-resources,dc=example,dc=com
   changetype:add
   objectClass: top
   objectClass: domain
   dc: uma-resources
   ```

2. Apply the LDIF file to the DS instance by using the `ldapmodify` command:

   ```bash
   $ /path/to/opendj/bin/ldapmodify \
   --hostname 'uma-rs.example.com' \
   --port 1636 \
   --useSsl \
   --usePkcs12TrustStore /path/to/opendj/config/keystore \
   --truststorepassword:file /path/to/opendj/config/keystore.pin \
   --bindDN uid=admin \
   --bindPassword str0ngAdm1nPa55word \
   --continueOnError \
   --offline \
   add-uma-base-dn.ldif
   # ADD operation successful for DN dc=uma-resources,dc=example,dc=com
   ```

   |   |                                                                                            |
   | - | ------------------------------------------------------------------------------------------ |
   |   | If you are having trouble with the LDIF file, remove any line feeds in the ACI attributes. |

## Create an UMA store bind account

As a best practice, don't use the root `uid=admin` to access data on the directory server. Instead, create a new service account, the UMA store bind account, with limited access and fewer privileges.

1. Create an LDIF file to add the bind account to the UMA store, and save the file as `add-uma-bind-account.ldif`.

   When AM connects as the bind account to store the UMA-related data, it requires read, write, persistent search, and server-side sorting access privileges. You add these privileges by setting access control instructions (ACIs) on the base distinguished name (DN) entry you created in the previous step (for example, `dc=uma-resources,dc=example,dc=com`).

   The following is an example of a suitable `add-uma-bind-account.ldif` LDIF file:

   ```ldif
   dn: ou=admins,dc=uma-resources,dc=example,dc=com
   objectclass: top
   objectclass: organizationalUnit
   ou: admins

   dn: uid=am-uma-bind-account,ou=admins,dc=uma-resources,dc=example,dc=com
   objectclass: top
   objectclass: person
   objectclass: organizationalPerson
   objectclass: inetOrgPerson
   cn: am-uma-bind-account
   sn: am-uma-bind-account
   uid: am-uma-bind-account
   userPassword: {ds_bind_password}
   aci: (targetattr="*")(version 3.0; acl "Allow CRUDQ operations"; allow (search, read, write, add, delete)(userdn = "ldap:///uid=am-uma-bind-account,ou=admins,dc=uma-resources,dc=example,dc=com");)
   aci: (targetcontrol="2.16.840.1.113730.3.4.3")(version 3.0; acl "Allow persistent search"; allow (search, read)(userdn = "ldap:///uid=am-uma-bind-account,ou=admins,dc=uma-resources,dc=example,dc=com");)
   aci: (targetcontrol="1.2.840.113556.1.4.473")(version 3.0; acl "Allow server-side sorting"; allow (read)(userdn = "ldap:///uid=am-uma-bind-account,ou=admins,dc=uma-resources,dc=example,dc=com");)
   ```

2. Apply the LDIF file to the DS instance by using the `ldapmodify` command:

   ```bash
   $ /path/to/opendj/bin/ldapmodify \
   --hostname 'uma-rs.example.com' \
   --port 1636 \
   --useSsl \
   --usePkcs12TrustStore /path/to/opendj/config/keystore \
   --truststorepassword:file /path/to/opendj/config/keystore.pin \
   --bindDN uid=admin \
   --bindPassword str0ngAdm1nPa55word \
   --continueOnError \
   --offline \
   add-uma-bind-account.ldif
   # ADD operation successful for DN uid=am-uma-bind-account,ou=admins,dc=uma-resources,dc=example,dc=com
   ```

   |   |                                                                                            |
   | - | ------------------------------------------------------------------------------------------ |
   |   | If you are having trouble with the LDIF file, remove any line feeds in the ACI attributes. |

   The `am-uma-bind-account` account can now connect to the PingDS instance. Note that you must use the full distinguished name of the account when binding, for example `uid=am-uma-bind-account,ou=admins,dc=uma-resources,dc=example,dc=com`, with the configured password, for example `5up35tr0ng`.

## Create a schema for UMA-related data

When the DS instance is installed and operational, import the schema files required for UMA-related data. You must do this as an administrative user, such as `uid=admin`. For information on the required schema files, see [LDIF files for UMA datastores](#table-uma-store-ldifs).

|   |                                                  |
| - | ------------------------------------------------ |
|   | These steps use the LDIF files provided with AM. |

1. Replace the `@SM_CONFIG_ROOT_SUFFIX@` variable in the LDIF files with the base DN you configured in the directory server.

   For example, `dc=uma-resources,dc=example,dc=com`.

   Depending on the UMA-related data type you will store in this directory server, replace the variable in the following LDIF files:

   * `/path/to/tomcat/webapps/am/WEB-INF/template/ldif/opendj/opendj_uma_audit.ldif`

   * `/path/to/tomcat/webapps/am/WEB-INF/template/ldif/opendj/opendj_uma_resource_sets.ldif`

   * `/path/to/tomcat/webapps/am/WEB-INF/template/ldif/opendj/opendj_uma_resource_set_labels.ldif`

   * `/path/to/tomcat/webapps/am/WEB-INF/template/ldif/opendj/opendj_uma_pending_requests.ldif`

   |   |                                                                                                                                                                                                                                                           |
   | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | If you've previously edited the files to replace the variables, replace those root entry values with the new UMA directory server root entries. For example, replace occurrences of `dc=cts,dc=example,dc=com` with `dc=uma-resources,dc=example,dc=com`. |

2. Apply the required LDIF files to the store by using the `ldapmodify` command.

   The following applies the schema required for storing resources:

   ```bash
   $ /path/to/opendj/bin/ldapmodify \
   --hostname 'uma-rs.example.com' \
   --port 1636 \
   --useSsl \
   --usePkcs12TrustStore /path/to/opendj/config/keystore \
   --truststorepassword:file /path/to/opendj/config/keystore.pin \
   --continueOnError \
   --bindDN uid=admin \
   --bindPassword str0ngAdm1nPa55word \
   --offline \
   /path/to/tomcat/webapps/am/WEB-INF/template/ldif/opendj/opendj_uma_resource_sets.ldif
   # ADD operation successful for DN ou=resource_sets,dc=uma-resources,dc=example,dc=com
   ```

   For more information on the required LDIF files, refer to [LDIF files for UMA datastores](#table-uma-store-ldifs).

3. After applying all the required LDIF files, start the DS server.

   ```bash
   $ /path/to/opendj/bin/start-ds
   ```

   The DS instance is now ready to store UMA resources. To set up additional DS instances for other UMA-related data repeat the steps above, specifying the relevant schema LDIF files.

   To configure AM to use the external DS instances to store UMA-related data, refer to [Configure external UMA stores](configure-external-uma-stores.html).

---

---
title: Register and protect resources
description: Register resources in PingAM and create authorization policies to protect them at resource creation, policy creation, or access time
component: pingam
version: 8.1
page_id: pingam:uma:uma-register-resource-sets-policies
canonical_url: https://docs.pingidentity.com/pingam/8.1/uma/uma-register-resource-sets-policies.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["User-Managed Access (UMA)", "Registration", "Resource Sets", "REST"]
page_aliases: ["uma-guide:uma-register-resource-sets-policies.adoc"]
---

# Register and protect resources

Resource owners register their resources in the UMA provider, and protect them with authorization policies:

* Resource registration can occur at three different stages:

  * When the resource is initially created

  * When the resource is required for policy creation

  * When someone attempts to access the resource

    The process is the same regardless of when it is run.

* Policy creation can occur:

  * After the resource is created

  * When someone attempts to access the resource

    The process is the same regardless of when it is run. The requesting party must always run through the UMA grant flow to gain access to the resources.

    |   |                                                                                                                                                                   |
    | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    |   | Only the resource owner can create a policy to protect a resource. Administrative users, such as `amAdmin`, cannot create policies on behalf of a resource owner. |

Continue reading to learn how to register and protect resources with the AM UI and the REST APIs.

---

---
title: UMA stores
description: Configure PingAM to store User-Managed Access information, audit data, and resource labels in external data stores for production deployments
component: pingam
version: 8.1
page_id: pingam:uma:configure-uma-storage
canonical_url: https://docs.pingidentity.com/pingam/8.1/uma/configure-uma-storage.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["User-Managed Access (UMA)", "Storage", "Configuration"]
page_aliases: ["uma-guide:configure-uma-storage.adoc"]
---

# UMA stores

AM stores information about registered resources, audit information generated when users manage access to their protected resources, pending requests, and resource labels. AM stores these items in the configuration store by default.

For *demo and test purposes*, storing UMA information in the configuration store is sufficient and you do not need to take any additional action. To configure UMA for test purposes, see [UMA use case](uma-example.html).

For *production environments*, configure at least one external store to hold UMA information. Configure more stores to separate UMA objects in high-load deployments when data tuning requirements differ.

The tasks to configure UMA stores are:

[icon: database, set=fad, size=3x]

#### [Prepare DS](prepare-uma-store.html)

Prepare one or more DS instances to hold UMA data.

[icon: edit, set=fad, size=3x]

#### [Configure UMA Stores](configure-external-uma-stores.html)

Configure the newly-prepared DS instances in AM.