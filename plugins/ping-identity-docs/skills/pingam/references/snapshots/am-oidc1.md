---
title: /.well-known/webfinger
description: Discover the OpenID provider for an end user using the WebFinger endpoint in PingAM
component: pingam
version: 8.1
page_id: pingam:am-oidc1:rest-api-oidc-discovery-webfinger
canonical_url: https://docs.pingidentity.com/pingam/8.1/am-oidc1/rest-api-oidc-discovery-webfinger.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["OpenID Connect (OIDC)", "Standards", "Endpoints"]
page_aliases: ["oidc1-guide:rest-api-oidc-discovery-webfinger.adoc"]
section_ids:
  supported_parameters: Supported parameters
  example: Example
---

# /.well-known/webfinger

The `/.well-known/webfinger` endpoint is described in [OpenID Connect Discovery 1.0 incorporating errata set 1](https://openid.net/specs/openid-connect-discovery-1_0.html).

Use it to discover the OpenID provider for an end user.

*Do not* specify the realm in the request URL; for example:

```none
https://am.example.com:8443/am/.well-known/webfinger
```

This endpoint is disabled by default. For details, refer to [OIDC discovery](oidc-am-provider.html#configure-openid-connect-discovery).

## Supported parameters

The discovery endpoint supports the following parameters:

| Parameter  | Description                                                                                                                                                                                                                                                                                                                                                                  | Required                                              |
| ---------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------- |
| `realm`    | The AM realm to query for the user profile.                                                                                                                                                                                                                                                                                                                                  | No                                                    |
| `rel`      | The URI identifying the type of service.                                                                                                                                                                                                                                                                                                                                     | Yes; use `http://openid.net/specs/connect/1.0/issuer` |
| `resource` | The URL-encoded subject of the request.; one of:`acct:user-email` `acct:user-email@host` `http(s)://host/username` `http(s)://host:port`The `host` relates to the discovery URL. For example, if the endpoint is `http://server.example.com/am/.well-known/webfinger`, the host is `server.example.com`.The `resource` parameter does not support wildcard characters (`*`). | Yes                                                   |

## Example

```bash
$ curl \
'https://am.example.com:8443/am/.well-known/webfinger?resource=acct%3Abjensen%40example.com&rel=http%3A%2F%2Fopenid.net%2Fspecs%2Fconnect%2F1.0%2Fissuer'
{
  "subject": "acct:bjensen@example.com",
  "links": [{
    "rel": "http://openid.net/specs/connect/1.0/issuer",
    "href": "https://am.example.com:8443/am/oauth2/realms/root/realms/alpha"
  }]
}
```
