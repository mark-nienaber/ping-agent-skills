---
title: Administrative SSO lockout
description: If you misconfigure administrative single sign-on (SSO) and are locked out of the PingAccess administrative console, you can disable SSO and sign on using the native sign-on.
component: pingaccess
version: 9.1
page_id: pingaccess:troubleshooting:pa_admin_sso_lockout
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/troubleshooting/pa_admin_sso_lockout.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 21, 2023
---

# Administrative SSO lockout

If you misconfigure administrative single sign-on (SSO) *(tooltip: \<div class="paragraph">
\<p>The process of authenticating an identity (signing on) at one website (usually with a user ID and password) and then accessing resources secured by other domains without reauthenticating.\</p>
\</div>)* and are locked out of the PingAccess administrative console, you can disable SSO and sign on using the native sign-on.

Choose one of the following methods to disable SSO:

* If you can start the PingAccess server or the administrative node in a cluster, refer to [Editing `run.properties` to disable SSO](pa_editing_run_properties_to_disable_sso.html).

* If you didn't disable basic authorization, refer to [Using the administrative API to disable SSO](pa_using_the_admin_api_to_disable_sso.html).

* If basic authorization is disabled, but administrative API OAuth *(tooltip: \<div class="paragraph">
  \<p>A standard framework that enables an application (OAuth client) to obtain access tokens from an OAuth authorization server for the purpose of retrieving protected resources on a resource server.\</p>
  \</div>)* is enabled, refer to [Using the administrative API and a new token to disable SSO](pa_using_the_admin_api_and_a_new_token_to_disable_sso.html).
