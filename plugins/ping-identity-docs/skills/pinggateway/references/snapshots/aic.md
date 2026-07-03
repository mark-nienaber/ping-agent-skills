---
title: Move to Advanced Identity Cloud
description: Use PingGateway to route requests when switching from a self-managed PingAM deployment to PingOne Advanced Identity Cloud for OAuth 2.0, OIDC, and SAML V2.0.
component: pinggateway
version: 2026
page_id: pinggateway:aic:switch-to-saas
canonical_url: https://docs.pingidentity.com/pinggateway/2026/aic/switch-to-saas.html
revdate: 2025-12-04
section_ids:
  constraints: Constraints for this use case
  tasks: Tasks
  before_you_begin: Before you begin
  task_1_share_keys: "Task 1: Share keys"
  task_2_configure_network_settings: "Task 2: Configure network settings"
  task_3_configure_idp_settings: "Task 3: Configure IdP settings"
  task_4_set_up_pinggateway: "Task 4: Set up PingGateway"
  validation: Validation
---

# Move to Advanced Identity Cloud

PingGateway can help you switch from a self-managed or on-premise AM deployment to PingOne Advanced Identity Cloud.

This page describes how to make the move by using PingGateway in front of the existing deployment to route requests to the appropriate Advanced Identity Cloud realm endpoints.

This example covers OAuth 2.0, OpenID Connect (OIDC), and Security Assertion Markup Language (SAML) V2.0 deployments. Actual steps depend on your deployment and requirements.

|   |                                                                                                                                                                                                            |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | [Ping Identity Professional Services](https://www.pingidentity.com/en/support/professional-services.html) can assist you with this and other deployment projects. Don't hesitate to contact them for help. |

## Constraints for this use case

This high-level use case applies to self-managed or on-premise AM deployments with:

* AM playing the role of identity provider (IdP) for OAuth 2.0, OpenID Connect (OIDC), or Security Assertion Markup Language (SAML) V2.0.

  Advanced Identity Cloud can play the IdP role in these deployments.

* At most two realms.

  Advanced Identity Cloud supports `alpha` and `bravo` realms.

  The steps and examples in this page focus on switching a single realm deployment. Repeat the instructions as needed for a two-realm deployment.

* A single FQDN as the entry point to AM services.

  Advanced Identity Cloud lets you configure custom domains per realm.

  The deployment can achieve this with either a site configuration or by using a DNS mapping for the Advanced Identity Cloud realm.

* Signing and encryption keys you can export from AM and import into Advanced Identity Cloud.

  Advanced Identity Cloud needs the same keys as the AM deployment so the client applications and service providers (SPs) continue to trust tokens and assertions without changes.

This use case *doesn't* apply to deployments that don't follow these constraints.

This use case also *doesn't* address how to:

* Move data from a self-managed deployment to PingOne Advanced Identity Cloud.

  You must migrate the data separately before switching to Advanced Identity Cloud.

  The data to migrate includes client application and end-user profiles, authentication journeys, and policies.

  End users, client applications, and SPs must find their data in the Advanced Identity Cloud tenant as in the AM deployment.

* Adapt custom code and custom integrations to work with PingOne Advanced Identity Cloud.

* Prevent Advanced Identity Cloud access from direct requests that don't go through PingGateway.

  If needed, you can do this with [PingOne Advanced Identity Cloud Proxy Connect](proxy-connect.html).

## Tasks

The following tasks describe how to use PingGateway to switch from an AM deployment to a deployment with a *single Advanced Identity Cloud tenant*, such as a development tenant.

After you [promote your tenant configuration](https://docs.pingidentity.com/pingoneaic/tenants/self-service-promotions.html) and ESVs, Update the PingGateway configuration, such as its configuration properties, to match the current tenant.

### Before you begin

Make sure:

* The AM deployment fits the [Constraints for this use case](#constraints).

* You can access and configure the PingOne Advanced Identity Cloud tenant as an administrator.

* You can configure DNS settings for the custom domain in Advanced Identity Cloud.

* You can install and configure PingGateway in the existing AM deployment.

### Task 1: Share keys

1. Export the IdP signing and encryption keys from AM.

   Learn more in the AM documentation on [Secrets, certificates, and keys](https://docs.pingidentity.com/pingam/8.1/security/secrets-certs-keys.html).

2. Import each key into Advanced Identity Cloud as an environment secret (ESV).

   Learn more in the Advanced Identity Cloud documentation on [managing ESVs](https://docs.pingidentity.com/pingoneaic/tenants/esvs-manage-ui.html).

3. In the AM admin UI for the target realm, map each ESV to the corresponding realm key alias.

   For example, the OAuth 2.0 signing keys map to the following key aliases, depending on the algorithm:

   * `am.services.oauth2.stateless.signing.ES256`

   * `am.services.oauth2.stateless.signing.ES384`

   * `am.services.oauth2.stateless.signing.ES512`

   * `am.services.oauth2.stateless.signing.HMAC`

   * `am.services.oauth2.stateless.signing.RSA`

   The SAML V2.0 ESVs map to the following key aliases:

   * `am.default.applications.federation.entity.providers.saml2.idp.encryption`

   * `am.default.applications.federation.entity.providers.saml2.idp.signing`

   Find the complete lists of key aliases using the links in the Advanced Identity Cloud documentation on [secret labels](https://docs.pingidentity.com/pingoneaic/am-reference/secret-id-mappings.html) and the AM documentation on [default key aliases](https://docs.pingidentity.com/pingam/8.1/security/change-signing-key.html).

You have successfully shared the relevant keys from the AM deployment with the Advanced Identity Cloud tenant.

### Task 2: Configure network settings

In the Advanced Identity Cloud tenant:

1. Configure a custom domain for the target realm in Advanced Identity Cloud to match the FQDN used by the AM deployment.

   Don't yet change the DNS settings to point to Advanced Identity Cloud, as requests must go through PingGateway first.

   Learn more in the Advanced Identity Cloud documentation on [custom domains](https://docs.pingidentity.com/pingoneaic/realms/custom-domains.html).

2. Configure cross-origin resource sharing (CORS) settings for the target realm in Advanced Identity Cloud as needed.

   Learn more in the Advanced Identity Cloud documentation on [CORS](https://docs.pingidentity.com/pingoneaic/tenants/cors.html).

You have successfully prepared the target realm in Advanced Identity Cloud to use the same FQDN as the AM deployment but haven't yet updated DNS to change the FQDN to direct to Advanced Identity Cloud.

### Task 3: Configure IdP settings

In the Advanced Identity Cloud tenant:

1. Go to the AM admin UI for the target realm.

2. Under Services, configure the `OAuth2Provider` service settings to match the AM deployment for OAuth 2.0 and OIDC.

   When the AM deployment doesn't use DNS aliases for realms, the issuer claim in Advanced Identity Cloud ID tokens can differ from those in the AM deployment. In this case, override the `iss` claim in Advanced Identity Cloud to match the AM deployment. Add `iss` to OpenID Connect > Overrideable Id\_Token Claims and edit the OIDC claims script for the realm to return the expected value.

3. Under Applications > Federation, configure the circle of trust (CoT) and hosted IdP settings using the same entity ID and meta alias to match the AM deployment for SAML V2.0.

   With the same entity ID, the IdP metadata for Advanced Identity Cloud matches the AM deployment and avoids changes for SPs. By using the same names settings for the CoT, you make it easier to compare the two deployments.

   Make sure you duplicate the SAML IdP location settings from the AM deployment in Advanced Identity Cloud. The single sign-on (SSO) and single logout (SLO) endpoints use these to validate the destination attribute in SSO and SLO requests. This ensures SP requests using the original AM IdP remain valid.

You have successfully configured Advanced Identity Cloud to act as the IdP for OAuth 2.0, OIDC, and SAML V2.0.

### Task 4: Set up PingGateway

The examples in this section set up PingGateway for an AM deployment moving to an Advanced Identity Cloud deployment. The two deployments have these characteristics:

* AM deployment base URL

  `https://company.example.com/openam`

* AM realm to move

  `customers`

* Advanced Identity Cloud access management base URL

  `https://openam-company.forgeblocks.com/am`

* Advanced Identity Cloud target realm

  `alpha`

Follow these steps to set up PingGateway:

1. Install PingGateway in the existing AM deployment.

   Learn more in [Installing PingGateway](../installation-guide/preface.html).

2. Add a file for configuration properties to route requests, adapting the following example for your deployment:

   * Linux

     `$HOME/.openig/config/s2sProps.json`

   * Windows

     `%appdata%\OpenIG\config\s2sProps.json`

   > **Collapse: Show source**
   >
   > (Source: [s2sProps.json](../_attachments/config/s2sProps.json))
   >
   > ```json
   > {
   >   "s2s": {
   >     "aicUrl": "https://openam-company.forgeblocks.com",
   >     "aicHost": "openam-company.forgeblocks.com",
   >     "aicHostHeader": "company.example.com",
   >     "mappings": {
   >       "amFromPath": "/openam",
   >       "aicToPath": "/am",
   >       "saml": {
   >         "idp": {
   >           "amSSORedirect": "/openam/SSORedirect/metaAlias/customers/idp",
   >           "aicSSORedirect": "/am/SSORedirect/metaAlias/alpha/idp",
   >           "amSSOPOST": "/openam/SSOPOST/metaAlias/customers/idp",
   >           "aicSSOPOST": "/am/SSOPOST/metaAlias/alpha/idp",
   >           "amSLORedirect": "/openam/IDPSloRedirect/metaAlias/customers/idp",
   >           "aicSLORedirect": "/am/IDPSloRedirect/metaAlias/alpha/idp",
   >           "amSLOPOST": "/openam/IDPSloPOST/metaAlias/customers/idp",
   >           "aicSLOPOST": "/am/IDPSloPOST/metaAlias/alpha/idp"
   >         }
   >       },
   >       "openid": {
   >         "am": "/am/oauth2/realms/root/realms/customers",
   >         "aic": "/am/oauth2/realms/root/realms/alpha"
   >       }
   >     }
   >   }
   > }
   > ```

3. Edit the PingGateway `config.json` file to reference the properties file and use the properties.

   > **Collapse: Show source**
   >
   > (Source: [config-s2s.json](../_attachments/config/config-s2s.json))
   >
   > ```json
   > {
   >   "properties": {
   >     "$location:s2s": "${fileToUrl(openig.configDirectory)}/s2sProps.json"
   >   },
   >   "heap": [
   >     {
   >       "name": "Router",
   >       "type": "Router",
   >       "config": {
   >         "directory": "${openig.configDirectory}/routes"
   >       }
   >     },
   >     {
   >       "name": "RewriteAmPaths",
   >       "type": "UriPathRewriteFilter",
   >       "config": {
   >         "mappings": {
   >           "${s2s.mappings.amFromPath}": "${s2s.mappings.aicToPath}",
   >           "${s2s.mappings.saml.idp.amSSORedirect}": "${s2s.mappings.saml.idp.aicSSORedirect}",
   >           "${s2s.mappings.saml.idp.amSSOPOST}": "${s2s.mappings.saml.idp.aicSSOPOST}",
   >           "${s2s.mappings.saml.idp.amSLORedirect}": "${s2s.mappings.saml.idp.aicSLORedirect}",
   >           "${s2s.mappings.saml.idp.amSLOPOST}": "${s2s.mappings.saml.idp.aicSLOPOST}",
   >           "${s2s.mappings.openid.am}": "${s2s.mappings.openid.aic}"
   >         }
   >       }
   >     },
   >     {
   >       "name": "SetAicHostHeader",
   >       "type": "HeaderFilter",
   >       "config": {
   >         "messageType": "REQUEST",
   >         "replace": {
   >           "host": [
   >             "${s2s.aicHost}"
   >           ]
   >         }
   >       }
   >     },
   >     {
   >       "name": "ResetCookieDomain",
   >       "type": "SetCookieUpdateFilter",
   >       "config": {
   >         "cookies": {
   >           ".*": {
   >             "domain": "${s2s.aicHostHeader}"
   >           }
   >         }
   >       }
   >     }
   >   ],
   >   "handler": "Router"
   > }
   > ```

   This configuration adds filters to:

   * Map AM request paths to the Advanced Identity Cloud endpoints.

   * Rewrite the host header in requests to match the Advanced Identity Cloud tenant domain.

   * Set the cookie domain to match the Advanced Identity Cloud custom domain.

4. Restart PingGateway to load the configuration changes.

5. Add a route to direct filtered requests to Advanced Identity Cloud:

   * Linux

     `$HOME/.openig/config/routes/s2s.json`

   * Windows

     `%appdata%\OpenIG\config\routes\s2s.json`

   > **Collapse: Show route**
   >
   > (Source: [s2s.json](../_attachments/config/routes/s2s.json))
   >
   > ```json
   > {
   >   "name": "S2S",
   >   "baseURI": "${s2s.aicUrl}",
   >   "handler": {
   >     "type": "Chain",
   >     "config": {
   >       "filters": [
   >         "ResetCookieDomain",
   >         "RewriteAmPaths",
   >         "SetAicHostHeader"
   >       ],
   >       "handler": "ReverseProxyHandler"
   >     }
   >   }
   > }
   > ```

   This route applies the filters defined in the configuration and directs requests to the Advanced Identity Cloud endpoints.

You have successfully set up PingGateway to route requests from the AM deployment to the Advanced Identity Cloud target realm.

## Validation

When testing your setup:

* Use test clients and SPs that represent the traffic in the existing AM deployment.

* As a baseline, test the existing AM deployment to define the expected behavior.

* After rolling out PingGateway, test the same clients and SPs to verify they work as expected with Advanced Identity Cloud.

After you validate all client applications and SPs work as expected with PingGateway, consider updating the DNS settings for the custom domain to point to Advanced Identity Cloud directly. After you do this and validate everything still works, you can retire the existing deployment.

You have successfully demonstrated how to switch from a self-managed or on-premise AM deployment to PingOne Advanced Identity Cloud.
