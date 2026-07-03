---
title: Choose your sample
description: This page describes the sample deployment alternatives and how the Advanced Identity Software components interact.
component: platform
version: 8
page_id: platform:sample-setup:overview
canonical_url: https://docs.pingidentity.com/platform/8/sample-setup/overview.html
page_aliases: ["platform-setup-guide:overview.adoc"]
section_ids:
  sample_separate_identity_stores: "Sample: separate identity stores"
  sample_shared_identity_store: "Sample: shared identity store"
  component-interaction: Component interaction
  next_step: Next step
---

# Choose your sample

This page describes the sample deployment alternatives and how the Advanced Identity Software components interact.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | This is *not* a comprehensive Advanced Identity Software implementation guide. These sample setup instructions show a minimal integration of Advanced Identity Software components to get you started.Ping Advanced Identity Software offers maximum extensibility and flexibility in self-managed deployments. Advanced Identity Software includes many features and options these sample setup instructions do not cover. If you don't need maximum extensibility and flexibility, there are simpler alternatives:- To consume the Advanced Identity Software as a service, use [PingOne Advanced Identity Cloud](https://docs.pingidentity.com/pingoneaic).

- To deploy in Kubernetes, start with the [ForgeOps](https://docs.pingidentity.com/forgeops/2025.1) reference implementation.For help with your deployment and to validate your plans before deploying in production, contact [Ping Identity](https://www.pingidentity.com). |

## Sample: separate identity stores

[This sample deployment](deployment1.html) has an external PingDS server configured as the PingAM configuration store and PingAM identity store (shown separately in the illustration). The PingIDM repository is an external JDBC database. The sample was tested with MySQL. The deployment uses an LDAP connector to synchronize the identities between PingIDM and PingAM.

PingGateway serves as a single-point of entry for Platform UI access:

![separate-id-store](_images/separate-id-store.png)

## Sample: shared identity store

[This sample deployment](deployment2.html) has an external PingDS server configured as the PingAM configuration store and shared by the PingAM and PingIDM servers share an external PingDS server as the identity store (shown separately in the illustration). No synchronization configuration is required.

PingGateway serves as a single-point of entry for Platform UI access:

![shared-id-store](_images/shared-id-store.png)

|   |                                                                                                                                                                                                            |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | In both sample deployments, the Platform UIs can run in separate Docker containers. If you want to run the Platform UIs in containers, [get Docker](https://docs.docker.com/get-docker/) before you start. |

## Component interaction

An Advanced Identity Software configuration relies on multiple components working together. The following image shows how the PingAM OAuth 2 clients interact with the PingIDM resource server filter (`rsFilter`) to grant access through the Platform UIs:

![client-interaction](_images/client-interaction.png)

1. The Platform UIs send a request to the PingAM Authorization Endpoint.

2. If the end user is authenticated, the user agent is redirected back to the UI, according to the Redirection URI request parameter.

3. If the end user is not authenticated, the PingAM Authorization Endpoint redirects the user agent to the Advanced Identity Software Login UI.

4. After successful authentication, the Advanced Identity Software Login UI redirects the user agent back to the PingAM Authorization Endpoint, according to the GoTo request parameter.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | * Don't use the PingIDM stand-alone End User UI if you're running PingAM and PingIDM in an Advanced Identity Software deployment. This UI is delivered with PingIDM under `ui/enduser`. It is *not* the same as the `platform-enduser` UI and won't work in an Advanced Identity Software deployment.

* By default, the IDM admin UI only supports users from the PingAM root realm. If you need to support users from other realms, adjust the `/oauth2/` references in the `/path/to/openidm/ui/admin/default/index.html` file:

  ```html
  commonSettings.authorizationEndpoint = calculatedAMUriLink.href + '/oauth2/authorize';

  AppAuthHelper.init({
      clientId: commonSettings.clientId,
      authorizationEndpoint: commonSettings.authorizationEndpoint,
      tokenEndpoint: calculatedAMUriLink.href + '/oauth2/access_token',
      revocationEndpoint: calculatedAMUriLink.href + '/oauth2/token/revoke',
      endSessionEndpoint: calculatedAMUriLink.href + '/oauth2/connect/endSession',
  ```

  For example, if your realm is named `alpha`, replace `/oauth2/` with `/oauth2/realms/root/realms/alpha/`. |

## Next step

* [icon: check-square-o, set=fa][Choose your sample](overview.html)

* [icon: square-o, set=fa]*[Prepare the servers](server-settings.html)*

* Separate identity stores

  * [icon: square-o, set=fa][Set up PingDS](deployment1.html)

  * [icon: square-o, set=fa][Set up PingAM](am-setup-1.html)

  * [icon: square-o, set=fa][Set up PingIDM](idm-setup-1.html)

* Shared identity store

  * [icon: square-o, set=fa][Set up PingDS](deployment2.html)

  * [icon: square-o, set=fa][Set up PingAM](am-setup-2.html)

  * [icon: square-o, set=fa][Set up PingIDM](idm-setup-2.html)

* [icon: square-o, set=fa][Protect the deployment](protect-deployment.html)

* [icon: square-o, set=fa][Set up the Platform UIs](platform-ui.html)

* [icon: square-o, set=fa][Test your deployment](test-deployment.html)
