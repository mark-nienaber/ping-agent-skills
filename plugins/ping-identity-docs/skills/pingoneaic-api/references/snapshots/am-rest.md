---
title: REST API versions
description: To maintain compatibility between releases, many REST APIs are versioned (v1.0, v2.0, and so on). The version number of a feature increases when Advanced Identity Cloud introduces breaking changes to an API.
component: pingoneaic-api
page_id: pingoneaic-api:am-rest:rest-api-versioning
canonical_url: https://developer.pingidentity.com/pingoneaic-api/am-rest/rest-api-versioning.html
keywords: ["REST API", "JSON", "CSRF"]
section_ids:
  rest-api-explicit-version: Specify versions
  rest-api-versioning-messages: Version messages
---

# REST API versions

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

If the version specification prevents Advanced Identity Cloud from serving the request, the response status is HTTP 404 Not Found and the response headers aren't included:

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

In this error case, the response body is empty.
