---
title: PingAM REST API reference
description: Access management REST API reference covering protocol versions, versioning, and endpoint specifications
component: pingoneaic
page_id: pingoneaic:am-rest:preface
canonical_url: https://docs.pingidentity.com/pingoneaic/am-rest/preface.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["REST API"]
page_aliases: ["index.adoc", "REST-guide:preface.adoc"]
---

# PingAM REST API reference

These pages describe specific characteristics of the PingAM REST APIs. For an overview of PingAM REST APIs, refer to [Advanced Identity Cloud REST](../developer-docs/crest/about-crest.html).

---

---
title: REST API endpoints
description: Access management REST API endpoints for authentication, authorization, OAuth 2.0, OpenID Connect, and session management
component: pingoneaic
page_id: pingoneaic:am-rest:rest-endpoints
canonical_url: https://docs.pingidentity.com/pingoneaic/am-rest/rest-endpoints.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["REST API", "OpenID Connect (OIDC)", "OAuth 2.0", "Authentication"]
page_aliases: ["REST-guide:rest-endpoints.adoc"]
---

# REST API endpoints

REST API endpoints are discussed in detail in the following sections:

* [Authenticate over REST](../am-authentication/authn-rest.html)

  How to use the REST APIs to authenticate to Advanced Identity Cloud.

* [Request policy decisions over REST](../am-authorization/rest-api-authz-policy-decisions.html)

  How to use the REST APIs for requesting authorization decisions from Advanced Identity Cloud.

* [OAuth 2.0 endpoints](../am-oauth2/oauth2-client-endpoints.html)

  How to use OAuth 2.0-specific endpoints to request access and refresh tokens, as well as introspecting and revoking them.

* [Manage scripts over REST](../am-scripting/manage-scripts-rest.html)

  How to use the REST APIs to manage authentication and authorization scripts.

* [OAuth 2.0 administration endpoints](../am-oauth2/oauth2-admin-endpoints.html)

  How to use Advanced Identity Cloud REST APIs to perform OAuth 2.0 administrative tasks such as registering, reading, and deleting clients.

* [OIDC 1.0 endpoints](../am-oidc1/oidc-client-endpoints.html)

  How to use OpenID Connect-specific endpoints to retrieve information about an authenticated user, as well as validate ID tokens and check sessions.

* [Manage sessions over REST](../am-sessions/managing-sessions-REST.html)

  How to use the REST APIs to manage Advanced Identity Cloud sessions.

---

---
title: REST API versions
description: REST API versioning strategy using Accept-API-Version headers for protocol and resource versions
component: pingoneaic
page_id: pingoneaic:am-rest:rest-api-versioning
canonical_url: https://docs.pingidentity.com/pingoneaic/am-rest/rest-api-versioning.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["REST API", "JSON", "CSRF"]
page_aliases: ["REST-guide:rest-api-versioning.adoc"]
section_ids:
  rest-api-explicit-version: Specify versions
  rest-api-versioning-messages: Version messages
---

# REST API versions

Versioning in the REST APIs helps ensure compatibility between releases. The version number of a feature increases for each non-backwards-compatible change.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                              |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Always include *resource* versions in your REST calls. This ensures your applications remain compatible when Advanced Identity Cloud is updated.Advanced Identity Cloud has cross-site request forgery (CSRF) protection for all the endpoints under `/am/json`. This protection requires all requests other than GET, HEAD, or OPTIONS to include one of the following headers:- `Accept-API-Version`

- `X-Requested-With` |

## Specify versions

REST APIs use the `Accept-API-Version` header to specify protocol and resource versions:

Accept-API-Version: protocol=*version*,resource=*version*

* `protocol`

  The version reflects changes in the REST protocol, such as common method parameters and headers specified by the protocol itself, or the input or response conventions it prescribes.

  For example, protocol version 2.2 introduced a `_countOnly` parameter.

* `resource`

  The version reflects changes in the resource implementation, including JSON representation of resources, input parameters required, and incompatible behavior changes.

  For example, the version changes when `errorMessage` changes to `message` in a JSON response.

The following example requests resource version 2.0 and protocol version 1.0:

```bash
$ curl \
--request POST \
--header "Content-Type: application/json" \
--header "X-OpenAM-Username: bjensen" \
--header "X-OpenAM-Password: Secret12!" \
--header "Accept-API-Version: resource=2.0, protocol=1.0" \
'https://<tenant-env-fqdn>/am/json/realms/root/realms/alpha/authenticate'
```

## Version messages

REST API responses include a `content-api-version` header to indicate the resource or protocol versions used to service the request. The following example shows a request for a version 2.0 resource and a response including a version 2.1 resource:

```bash
$ curl \
--request POST \
--include \
--header "Content-Type: application/json" \
--header "X-OpenAM-Username: bjensen" \
--header "X-OpenAM-Password: Secret12!" \
--header "Accept-API-Version: resource=2.0, protocol=1.0" \
'https://<tenant-env-fqdn>/am/json/realms/root/realms/alpha/authenticate'
...
content-api-version: resource=2.1
...
```

When the request has an incomplete version specification or is missing the header, the response includes a `warning` header:

```bash
$ curl \
--request POST \
--include \
--header "Content-Type: application/json" \
--header "X-OpenAM-Username: bjensen" \
--header "X-OpenAM-Password: Secret12!" \
'https://<tenant-env-fqdn>/am/json/realms/root/realms/alpha/authenticate'
...
content-api-version: resource=2.1
warning: 100 OpenAM REST "No Accept-API-Version specified"
warning: 100 chf "Accept-API-Version should be included in the request."
...
```

If the version specification prevents Advanced Identity Cloud from serving the request, the response status is HTTP 404 Not Found and the response headers are not included:

```bash
$ curl \
--request POST \
--include \
--header "Content-Type: application/json" \
--header "X-OpenAM-Username: bjensen" \
--header "X-OpenAM-Password: Secret12!" \
--header "Accept-API-Version: resource=42.0, protocol=1.0" \
'https://<tenant-env-fqdn>/am/json/realms/root/realms/alpha/authenticate'
HTTP/2 404
...
```

In this error case the response body is empty.

---

---
title: Specify realms in URLs
description: Specify realms in access management REST API URLs using hostnames or path parameters
component: pingoneaic
page_id: pingoneaic:am-rest:rest-realms
canonical_url: https://docs.pingidentity.com/pingoneaic/am-rest/rest-realms.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["REST API", "Realms"]
page_aliases: ["REST-guide:rest-realms.adoc"]
section_ids:
  in_the_hostname: In the hostname
  in_the_path: In the path
---

# Specify realms in URLs

Specify the realm in the hostname or the path of the URL depending on the settings for the realm.

## In the hostname

If you define a [custom domain](../realms/custom-domains.html) for the realm, you can target the realm using the hostname instead of the path.

For example, suppose the `alpha` realm uses the custom domain `auth.example.com`. Client applications can access a user profile without showing the realm name as in the following example:

```
https://auth.example.com/am/json/users/a0325ea4-9d9b-4056-931b-ab64704cc3da
```

## In the path

You can specify the realm in the path of the URL. For example, use the following URL to authenticate in the `alpha` realm:

```
https://<tenant-env-fqdn>/am/json/realms/root/realms/alpha/authenticate
```

If you specify a custom domain and a path, the path determines the realm. For example, the following URL references a user profile in the `bravo` realm, not the realm with custom domain `auth.example.com`:

```
https://auth.example.com/am/json/realms/root/realms/bravo/users/8cf34972-bdec-4dfa-a34e-536647fb60ff
```