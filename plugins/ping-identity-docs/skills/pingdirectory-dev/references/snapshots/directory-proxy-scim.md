---
title: Authentication
description: Authenticate PingDirectory and PingDirectoryProxy SCIM 2.0 API requests with an OAuth 2.0 access (bearer) token, as defined by RFC 6750. Obtain the bearer token through an OAuth 2 authorization server, such as PingFederate. Add the bearer token to the Authorization header of your requests.
component: pingdirectory
page_id: pingdirectory:directory-proxy-scim:authentication
canonical_url: https://developer.pingidentity.com/pingdirectory/directory-proxy-scim/authentication.html
---

# Authentication

Authenticate PingDirectory and PingDirectoryProxy SCIM 2.0 API requests with an OAuth 2.0 access (bearer) token, as defined by [RFC 6750](https://datatracker.ietf.org/doc/html/rfc6750). Obtain the bearer token through an OAuth 2 authorization server, such as PingFederate. Add the bearer token to the Authorization header of your requests.

```none
curl --location --request GET '{{apiPath}}/scim/v2/Users/5caa81af-ec05-41ff-a709-c7378007a99c?attributes=userName' \
--header 'Authorization: Bearer eyJraWQiOiJBY2Nlc3MgVG9rZW4gU2lnbmluZ...' \
--header 'Accept: application/scim+json' \
--header 'Accept-Encoding: gzip, deflate'
```

If the access token is missing, expired, or invalid, the server responds with a status code of `401 Unauthorized`.

```json
{
    "schemas": [
        "urn:ietf:params:scim:api:messages:2.0:Error"
    ],
    "scimType": "invalid_token",
    "status": 401,
    "detail": "Access token is expired or otherwise invalid."
}
```
