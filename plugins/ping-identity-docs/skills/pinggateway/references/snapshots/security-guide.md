---
title: Access to PingGateway
description: Secure your PingGateway deployment by restricting network access, applying least privilege, removing non-essential features, and keeping software up to date
component: pinggateway
version: 2026
page_id: pinggateway:security-guide:access
canonical_url: https://docs.pingidentity.com/pinggateway/2026/security-guide/access.html
revdate: 2025-04-01T17:53:34Z
keywords: ["Security", "Account", "Authorization", "Cryptographic Keys", "Encryption Keys", "REST API"]
section_ids:
  use_a_pinggateway_service_account: Use a PingGateway service account
  non-essential-access: Remove non-essential access
  non-essential-features: Remove non-essential features
  update-patches: Update patches
  general-sessions: Manage sessions
  expire_pingone_advanced_identity_cloud_and_am_sessions: Expire PingOne Advanced Identity Cloud and AM sessions
  validate_the_signature_of_pingone_advanced_identity_cloud_and_am_session_cookies: Validate the signature of PingOne Advanced Identity Cloud and AM session cookies
  general-cookies: Manage cookies
---

# Access to PingGateway

The following sections describe how to prevent unwanted access to your deployment, and reduce the amount of non-essential information that it provides.

## Use a PingGateway service account

Install and run PingGateway from a dedicated service account. This is optional when evaluating PingGateway, but essential in production installations. For more information, refer to [Create a PingGateway service account](../installation-guide/prepare.html#run-from-user-account).

## Remove non-essential access

Make sure only authorized people can access your servers and applications through the appropriate network, using the appropriate ports, and by presenting strong-enough credentials.

Apply the principle of least privilege to PingGateway logs and configuration directories. For more information, refer to [Configuration location](../configure/configure.html#configuration-location).

Make sure that users connect to systems through the latest versions of TLS, and audit system access periodically.

Restrict access to your monitoring data by protecting the Prometheus Scrape Endpoint and Common REST Monitoring Endpoint (deprecated). Learn more from [Protecting the monitoring endpoints](../maintenance-guide/monitoring.html#proc-monitor-plat-protect).

Prevent PingGateway from scanning for changes to routes. For information, see `scanInterval` in [Router](../reference/Router.html).

Disable administration endpoints and Studio by setting the PingGateway run mode to `production`. For information, refer to [PingGateway operating modes](../configure/operating-modes.html).

## Remove non-essential features

The more features you have turned on, the greater the attack surface. If something isn't used, uninstall it, disable it, or protect access to it.

## Update patches

Prevent the exploitation of security vulnerabilities by using up-to-date versions of PingGateway and third-party software.

Review and follow the Ping Identity security advisories.

Follow similar lists from all of your vendors.

## Manage sessions

### Expire PingOne Advanced Identity Cloud and AM sessions

To minimize the time an attacker can attack an active session, set expiration timeouts for every PingOne Advanced Identity Cloud and AM session. Set timeouts according to context of the deployment, balancing security and usability so that the user can complete operations without the session frequently expiring.

Learn more in OWASP's [Session Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html#session-expiration).

Set a maximum session lifetime and idle time in PingOne Advanced Identity Cloud:

* In the Advanced Identity Cloud admin UI, select [icon: open_in_new, set=material, size=inline] Native Consoles > Access Management.

* In the AM admin UI, select Services > Add a Service and add a Session service.

* Specify the following properties in minutes:

  * Maximum Session Time

  * Maximum Idle Time

Set a maximum session lifetime and idle time in PingAM:

* In the AM admin UI, select Services > Add a Service and add a Session service.

* Specify the following properties in minutes:

  * Maximum Session Time

  * Maximum Idle Time

### Validate the signature of PingOne Advanced Identity Cloud and AM session cookies

Always configure `verificationSecretId` in the [CrossDomainSingleSignOnFilter](../reference/CrossDomainSingleSignOnFilter.html).

When `verificationSecretId` is not configured, PingGateway doesn't verify the signature of AM session tokens, increasing the risk of CDSSO token tampering.

## Manage cookies

Increase the security of cookies genrated by PingGateway or the protected application in the following ways:

* Change the default name of cookies to prevent them from being easily associated with an application.

* Create cookies with the `secure` flag to ensure that browsers cannot transmit the cookie over non-SSL.

  When cookies have the `secure` flag, the first hop of the connection between the user agent and protected application must be secure (over HTTPs); subsequent hops don't have to be secure. In this example, the first hop from the user agent to NGINX is secure, the subsequent hop to PingGateway is not secure:

  ```none
  User agent -> NGINX (https://acme.com) -> PingGateway (http://gateway:8080)-> protected application (https://internal.app:8081)
  ```

* Create cookies with the `httpOnly` flag, to ensure that the cookie cannot be accessed through client-side scripts, and to mitigate any cross-site scripting attacks.

  Cookies are `httpOnly` by default in `admin.json`, InMemorySessionManager, JwtSessionManager, CrossDomainSingleSignOnFilter, and FragmentFilter.

* Set the `samesite` attribute of cookies to `STRICT` or `LAX`. Learn more in [SameSite cookies](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Set-Cookie/SameSite).

* Set a timeout for cookies to strike a good compromise between security and usability.

Harden a PingGateway configuration by configuring the following objects:

* Configure the `cookie` property of the [InMemorySessionManager](../reference/InMemorySessionManager.html) or [JwtSessionManager](../reference/JwtSessionManager.html).

* For authentication results, configure the `authCookie` property of the [CrossDomainSingleSignOnFilter](../reference/CrossDomainSingleSignOnFilter.html).

* For the fragment part of a URI when a request triggers a login redirect, configure the `cookie` property of [FragmentFilter](../reference/FragmentFilter.html).
