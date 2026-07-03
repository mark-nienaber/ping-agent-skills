---
title: /json/token/macaroon
description: Use the /json/token/macaroon endpoint to inspect and manipulate macaroon tokens in PingAM OAuth 2.0 and OpenID Connect flows
component: pingam
version: 8.1
page_id: pingam:am-oauth2:oauth2-introspect-macaroon-endpoint
canonical_url: https://docs.pingidentity.com/pingam/8.1/am-oauth2/oauth2-introspect-macaroon-endpoint.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["OAuth 2.0", "OpenID Connect (OIDC)", "Endpoints", "Macaroons", "Scope"]
page_aliases: ["varlist-oauth2-introspect-macaroon-endpoint.adoc", "oauth2-guide:oauth2-introspect-macaroon-endpoint.adoc"]
---

# /json/token/macaroon

The `/json/token/macaroon` endpoint lets you inspect and manipulate [macaroon tokens](oauth2-macaroons.html).

Specify the realm in the request URL; for example:

```none
https://am.example.com:8443/am/oauth2/realms/root/realms/alpha/token/macaroon
```

This endpoint supports these parameters:

| Field             | Description                                             |
| ----------------- | ------------------------------------------------------- |
| `action=inspect`  | Return details about the macaroon.                      |
| `action=restrict` | Add a caveat to the macaroon, returning a new macaroon. |

You can manipulate macaroons locally using a macaroon library. Anyone in possession of a macaroon token can inspect and restrict the macaroon securely.

The following example restricts the scope of a macaroon token and inspects the result. The original scope of the unrestricted token is `openid profile`:

```bash
$ curl \
--request POST \
--header "Content-Type: application/json" \
--header "cache-control: no-cache" \
--data '{
  "macaroon": "<macaroon-token>",
  "caveat": {"type": "first-party", "identifier": {"scope": "profile"}}
}' \
'https://am.example.com:8443/am/json/realms/root/realms/alpha/token/macaroon?_action=restrict'
{
  "macaroon": "<restricted-macaroon-token>"
}

$ curl \
--request POST \
--header "Content-Type: application/json" \
--header "cache-control: no-cache" \
--data '{"macaroon": "<restricted-macaroon-token>"}' \
'https://am.example.com:8443/am/json/realms/root/realms/alpha/token/macaroon?_action=inspect'
{
  "identifier": "<identifier>",
  "location": "",
  "caveats": [{
    "type": "first-party",
    "identifier": {
      "scope": "profile"
    }
  }],
  "signature": "<signature>"
}
```

|   |                                                                                                                                                                                                                                              |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | OIDC clients must ensure the following information is present in the JSON:- The `openid` scope; for example, `"scopes": ["profile", "openid"]`.

- The `id_token` response type; for example, `"response_types": ["code", "id_token code"]`. |
