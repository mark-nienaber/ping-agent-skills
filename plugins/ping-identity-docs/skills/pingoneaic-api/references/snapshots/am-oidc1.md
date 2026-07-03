---
title: /.well-known/webfinger
description: The /.well-known/webfinger endpoint is described in OpenID Connect Discovery 1.0 incorporating errata set 1.
component: pingoneaic-api
page_id: pingoneaic-api:am-oidc1:rest-api-oidc-discovery-webfinger
canonical_url: https://developer.pingidentity.com/pingoneaic-api/am-oidc1/rest-api-oidc-discovery-webfinger.html
keywords: ["OpenID Connect (OIDC)", "Standards", "Endpoints"]
section_ids:
  supported-parameters: Supported parameters
  example: Example
---

# /.well-known/webfinger

The `/.well-known/webfinger` endpoint is described in [OpenID Connect Discovery 1.0 incorporating errata set 1](https://openid.net/specs/openid-connect-discovery-1_0.html).

Use it to discover the OpenID provider for an end user.

*Do not* specify the realm in the request URL; for example:

```none
https://<tenant-env-fqdn>/am/.well-known/webfinger
```

This endpoint is disabled by default. Learn more in [OIDC discovery](https://docs.pingidentity.com/pingoneaic/latest/am-oidc1/oidc-am-provider.html#configure-openid-connect-discovery).

## Supported parameters

The discovery endpoint supports the following parameters:

| Parameter  | Description                                                                                                                                                                                                                                                                                                                                                                  | Required                                              |
| ---------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------- |
| `realm`    | The Advanced Identity Cloud realm to query for the user profile.                                                                                                                                                                                                                                                                                                             | No                                                    |
| `rel`      | The URI identifying the type of service.                                                                                                                                                                                                                                                                                                                                     | Yes; use `http://openid.net/specs/connect/1.0/issuer` |
| `resource` | The URL-encoded subject of the request.; one of:`acct:user-email` `acct:user-email@host` `http(s)://host/username` `http(s)://host:port`The `host` relates to the discovery URL. For example, if the endpoint is `http://server.example.com/am/.well-known/webfinger`, the host is `server.example.com`.The `resource` parameter does not support wildcard characters (`*`). | Yes                                                   |

## Example

```bash
$ curl \
'https://<tenant-env-fqdn>/am/.well-known/webfinger?resource=acct%3Abjensen%40example.com&rel=http%3A%2F%2Fopenid.net%2Fspecs%2Fconnect%2F1.0%2Fissuer'
{
  "subject": "acct:bjensen@example.com",
  "links": [{
    "rel": "http://openid.net/specs/connect/1.0/issuer",
    "href": "https://<tenant-env-fqdn>/am/oauth2/realms/root/realms/alpha"
  }]
}
```
