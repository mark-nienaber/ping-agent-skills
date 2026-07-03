---
title: Access tokens and ID tokens
description: Learn how PingOne uses access tokens and ID tokens in OAuth 2 and OIDC requests.
component: pingone
page_id: pingone:applications:p1_access_token_id_token
canonical_url: https://docs.pingidentity.com/pingone/applications/p1_access_token_id_token.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: January 9, 2023
section_ids:
  related-links: Related links
---

# Access tokens and ID tokens

Access tokens are credential strings that represent authorization to access a protected resource.

Client applications obtain access tokens by making OAuth 2 or OpenID Connect (OIDC) requests to an authorization server. Resource servers require clients to authenticate using access tokens.

Access tokens are obtained from the token endpoint, when using the client credentials grant type, or from the authorization endpoint, when using the implicit grant type. Access tokens are typically granted on behalf of a specific authenticated user. Tokens granted directly to applications are called application tokens.

## Related links

* [Customizing access tokens](p1_customize_access_token.html)
