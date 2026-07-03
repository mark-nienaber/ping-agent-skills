---
title: Configuring service provider-initiated SSO
description: You can imitate a service provider (SP)-initiated single sign-on (SSO) experience by configuring your WebSphere Application Server (WAS) to redirect unauthenticated users to the PingFederate SSO page.
component: websphere
page_id: websphere:setup:pf_websphere_integration_configuring_service_provider_initiated_sso
canonical_url: https://docs.pingidentity.com/integrations/websphere/setup/pf_websphere_integration_configuring_service_provider_initiated_sso.html
revdate: July 5, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Configuring service provider-initiated SSO

You can imitate a service provider (SP)-initiated single sign-on (SSO) experience by configuring your WebSphere Application Server (WAS) to redirect unauthenticated users to the PingFederate SSO page.

## About this task

|   |                                                                                                                 |
| - | --------------------------------------------------------------------------------------------------------------- |
|   | This part of the configuration is optional. If you only want identity provider-initiated SSO, skip these steps. |

By default, when an unauthenticated user tries to access a protected resource, the WebSphere Application Server (WAS) captures the requested resource URL in a browser cookie, then directs the user to a default error page.

You can override this behavior to redirect the user to the PingFederate SSO page instead. After the user authenticates, the WebSphere Application Server redirects them to the original resource URL stored in the cookie.

This creates a sign on experience that is similar to SP-initated SSO. For a true SAML-based solution, see [Enabling SAML SP-Initiated web single sign-on (SSO)](https://www.ibm.com/support/knowledgecenter/SSEQTP_9.0.5/com.ibm.websphere.base.doc/ae/tsec_enable_saml_sp_sso.html) in the WebSphere documentation.

## Steps

1. In your WebSphere trusted association interceptor (TAI) configuration, add filter properties to allow the WAS to identify requests that should be authenticated by PingFederate. Follow the guide in the **SAML TAI filter property** section of [SAML web single sign-on (SSO) trust association interceptor (TAI) custom properties](https://www.ibm.com/support/knowledgecenter/SSEQTP_9.0.5/com.ibm.websphere.base.doc/ae/rwbs_samltaiproperties.html) in the WebSphere documentation.

2. In your TAI configuration, change the `sso_<id>.sp.login.error.page` property to the **SSO Application Endpoint** URL that you noted in [Creating a single sign-on connection](gnc1590516299053.html).
