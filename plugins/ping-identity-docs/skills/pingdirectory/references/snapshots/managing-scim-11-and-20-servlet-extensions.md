---
title: Authentication requirements for SCIM 2.0 requests
description: All System for Cross-domain Identity Management (SCIM) requests on the server must use OAuth 2.0 bearer token authentication. Bearer tokens are evaluated using the SCIM 2.0 servlet extension's configured access token validators. Basic authentication isn't supported.
component: pingdirectory
version: 11.1
page_id: pingdirectory:managing_scim_11_and_20_servlet_extensions:pd_proxy_authn_reqs_scim_2_requests
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/managing_scim_11_and_20_servlet_extensions/pd_proxy_authn_reqs_scim_2_requests.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 2, 2024
page_aliases: ["pd_proxy_scim_1_1_servlet_ext_authn.adoc"]
---

# Authentication requirements for SCIM 2.0 requests

All System for Cross-domain Identity Management (SCIM) *(tooltip: \<div class="paragraph">
\<p>An application-level, HTTP-based protocol for provisioning and managing user identity information. SCIM supplies a common schema for representing users and groups and provides a REST API.\</p>
\</div>)* requests on the server must use OAuth *(tooltip: \<div class="paragraph">
\<p>A standard framework that enables an application (OAuth client) to obtain access tokens from an OAuth authorization server for the purpose of retrieving protected resources on a resource server.\</p>
\</div>)* 2.0 bearer token authentication. Bearer tokens are evaluated using the SCIM 2.0 servlet extension's configured access token *(tooltip: \<div class="paragraph">
\<p>A data object by which a client authenticates to a resource server and lays claim to authorizations for accessing particular resources.\</p>
\</div>)* validators. Basic authentication isn't supported.

In addition to requiring bearer tokens, the server doesn't process any SCIM requests unless it has at least one `encryption-settings` definition in its `encryption-settings` database. You can create the necessary definitions with the `encryption-settings` command-line tool. Learn more in [Encrypting sensitive data](../pingdirectory_server_administration_guide/pd_ds_encrypt_sensitive_data.html).

|   |                                                                                                               |
| - | ------------------------------------------------------------------------------------------------------------- |
|   | You must define encryption settings and ensure they match on the proxy and all backend PingDirectory servers. |
