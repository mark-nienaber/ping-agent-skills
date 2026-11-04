---
title: Introduction to the Advanced Identity Cloud API
description: Overview of Advanced Identity Cloud REST APIs covering access management, identity management, and scripting endpoints
component: pingoneaic-api
page_id: pingoneaic-api::api-reference
canonical_url: https://developer.pingidentity.com/pingoneaic-api/api-reference.html
llms_txt: https://developer.pingidentity.com/pingoneaic-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["PingOne Advanced Identity Cloud", "Advanced Identity Cloud", "release notes", "what's new", "Advanced Identity Cloud REST API", "Advanced Identity Cloud API", "Integration"]
section_ids:
  api-versions: API versions
  the-apis: The APIs
---

# Introduction to the Advanced Identity Cloud API

Many of the features available through Advanced Identity Cloud UIs are also available through REST APIs.

|   |                                                                                                                                                                                                                                                                                    |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Some documented APIs aren't active in all Advanced Identity Cloud tenants.The REST APIs have *Evolving* interface stability. This interface is continuing to evolve and so is subject to change in backwards-incompatible ways. All changes are documented at the time of release. |

## API versions

To maintain compatibility between releases, many REST APIs are versioned (`v1.0`, `v2.0`, and so on). The version number of a feature increases when Advanced Identity Cloud introduces breaking changes to an API.

Advanced Identity Cloud provides versions for these API aspects:

* *resource*

  Any changes to the structure or syntax of a returned response result in a change to the *resource* version. For example, changing `errorMessage` to `message` in a JSON response.

* *protocol*

  Any changes to the methods used to make REST API calls result in change to the *protocol* version. For example, changing `_action` to `$action` in the required parameters of an API feature.

When an API is versioned, include resource versions in your REST calls by setting the `Accept-API-Version` request header. The following example requests *resource* version 2.0 and *protocol* version 1.0:

```
Accept-API-Version: resource=2.0, protocol=1.0
```

This header ensures you call the correct version of the API, avoiding unexpected behavior due to incompatible changes.

## The APIs

Learn more in the API reference pages:

* [Authenticate over REST](am-authentication/authn-rest.html)

* [Identity Governance APIs](_attachments/api/identity-governance-openapi.html) 1

* [Identity management](_attachments/api/index-idm.html), [REST and IDM](idm-rest-api/rest-and-idm.html)

* [Manage auth scripts](am-scripting/manage-scripts-rest.html)

* [Manage sessions over REST](am-sessions/managing-sessions-REST.html)

* [OAuth 2.0 administration endpoints](am-oauth2/oauth2-admin-endpoints.html)

* [OAuth 2.0 APIs](am-oauth2/oauth2-client-endpoints.html)

* [OIDC APIs](am-oidc1/oidc-client-endpoints.html)

* [Policy APIs](am-authorization/rest-api-authz-policies.html)

* [Tenant administration](_attachments/api/index.html)

1 Identity Governance is an add-on capability to Advanced Identity Cloud. Contact your Ping Identity representative if you want to add PingOne® Identity Governance to your Advanced Identity Cloud subscription.