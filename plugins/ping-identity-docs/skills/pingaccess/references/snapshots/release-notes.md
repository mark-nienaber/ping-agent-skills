---
title: Release notes
description: New features and improvements in PingAccess. Updated June 2026.
component: pingaccess
version: 9.1
page_id: pingaccess:release_notes:pa_release_notes
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/release_notes/pa_release_notes.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 2, 2026
section_ids:
  pa-91: PingAccess 9.1.0
  use-cspnonce-to-embed-inline-javascript-into-templates: Use <cspNonce> to embed inline JavaScript into templates
  authenticate-with-a-qr-code: Authenticate with a QR code
  trace-requests-across-pingaccess: Trace requests across PingAccess
  added-support-for-java-25: Added support for Java 25
  set-audience-to-the-as-issuer-to-comply-with-rfc-7523: Set audience to the AS issuer to comply with RFC 7523
  rotate-the-admin-config-query-certificate-without-restarting-engine-nodes: Rotate the admin config query certificate without restarting engine nodes
  set-the-language-your-sign-on-page-displays-in: Set the language your sign-on page displays in
  retry-post-requests-that-failed-because-of-an-unknownhostexception: Retry POST requests that failed because of an UnknownHostException
  retain-existing-application-resource-ids-throughout-upgrade-process: Retain existing application resource IDs throughout upgrade process
  checking-application-resource-ids: Checking application resource IDs
  updated-third-party-dependencies: Updated third-party dependencies
  improved-bouncy-castle-security: Improved Bouncy Castle security
  updated-the-apache-log4j-library-to-version-2-25-3: Updated the Apache Log4j library to version 2.25.3
  updated-nettys-parsing-behavior: Updated Netty's parsing behavior
  updated-component-dependencies: Updated component dependencies
  addressed-potential-request-smuggling-security-vulnerability: Addressed potential request smuggling security vulnerability
  addressed-potential-resource-allocation-security-vulnerability: Addressed potential resource allocation security vulnerability
  fixed-unnecessary-warnings-logged-for-jwks-atvs: Fixed unnecessary warnings logged for JWKS ATVs
  fixed-an-issue-with-creating-new-third-party-services: Fixed an issue with creating new third-party services
  fixed-500-errors-caused-by-key-rolling: Fixed 500 errors caused by key rolling
  fixed-performance-degradation-issue-with-upgrading-larger-configurations: Fixed performance degradation issue with upgrading larger configurations
  fixed-an-issue-with-modified-json-templates-not-carrying-over-on-an-upgrade: Fixed an issue with modified JSON templates not carrying over on an upgrade
  fixed-an-apache-commons-logging-classpath-warning: Fixed an Apache Commons Logging classpath warning
  fixed-application-level-rule-evaluation: Fixed application-level rule evaluation
  fixed-slow-admin-api-response: Fixed slow admin API response
  fixed-an-issue-with-automatic-resource-ordering: Fixed an issue with automatic resource ordering
  fixed-an-issue-causing-the-admin-console-to-show-a-blank-page: Fixed an issue causing the admin console to show a blank page
  fixed-an-issue-blocking-key-pair-imports: Fixed an issue blocking key pair imports
  fixed-a-post-preservation-encoding-issue-when-not-using-utf-8: Fixed a POST preservation encoding issue when not using UTF-8
  pingaccess-add-on-sdk-class-is-incompatible-in-groovy-script-rules-with-java-17-and-later: PingAccess Add-On SDK class is incompatible in Groovy script rules with Java 17 and later
  fips-mode-validation-doesnt-cover-imported-key-pairs-for-sha1: FIPS mode validation doesn't cover imported key pairs for SHA1
  pa-904: PingAccess 9.0.4 (June 2026)
  retry-post-requests-that-failed-because-of-an-unknownhostexception-2: Retry POST requests that failed because of an UnknownHostException
  updated-component-dependencies-2: Updated component dependencies
  addressed-potential-request-smuggling-security-vulnerability-2: Addressed potential request smuggling security vulnerability
  addressed-potential-resource-allocation-security-vulnerability-2: Addressed potential resource allocation security vulnerability
  fixed-an-issue-with-automatic-resource-ordering-2: Fixed an issue with automatic resource ordering
  fixed-an-issue-causing-the-admin-console-to-show-a-blank-page-2: Fixed an issue causing the admin console to show a blank page
  fixed-an-issue-blocking-key-pair-imports-2: Fixed an issue blocking key pair imports
  fixed-a-post-preservation-encoding-issue-when-not-using-utf-8-2: Fixed a POST preservation encoding issue when not using UTF-8
  pa-903: PingAccess 9.0.3 (May 2026)
  updated-the-apache-log4j-library-to-version-2-25-3-2: Updated the Apache Log4j library to version 2.25.3
  updated-nettys-parsing-behavior-2: Updated Netty's parsing behavior
  fixed-an-apache-commons-logging-classpath-warning-2: Fixed an Apache Commons Logging classpath warning
  fixed-application-level-rule-evaluation-2: Fixed application-level rule evaluation
  pa-902: PingAccess 9.0.2 (March 2026)
  fixed-unnecessary-warnings-logged-for-jwks-atvs-2: Fixed unnecessary warnings logged for JWKS ATVs
  fixed-an-issue-with-creating-new-third-party-services-2: Fixed an issue with creating new third-party services
  fixed-500-errors-caused-by-key-rolling-2: Fixed 500 errors caused by key rolling
  fixed-performance-degradation-issue-with-upgrading-larger-configurations-2: Fixed performance degradation issue with upgrading larger configurations
  pa-901: PingAccess 9.0.1 (February 2026)
  fixed-unnecessary-modifications-made-by-the-pingauthorize-access-control-rule: Fixed unnecessary modifications made by the PingAuthorize access control rule
  pa-90: PingAccess 9.0.0 (December 2025)
  java-11-removal: Java 11 removal
  configure-email-reminders-about-expiring-certificates: Configure email reminders about expiring certificates
  configure-access-token-revocation-at-the-application-level: Configure access token revocation at the application level
  configure-custom-properties-for-pingaccess-applications: Configure custom properties for PingAccess applications
  map-incoming-request-parameters-from-the-requested-resource-to-the-token-provider: Map incoming request parameters from the requested resource to the token provider
  use-the-pingaccess-agent-for-nginx-with-nginx-r35: Use the PingAccess agent for NGINX with NGINX R35
  add-your-own-jwks-endpoints-for-access-token-validation: Add your own JWKS endpoints for access token validation
  updated-the-run-sh-script: Updated the run.sh script
  rsa-1-5-with-pkcs1-removal: RSA 1.5 with PKCS#1 removal
  upgraded-components-bundled-with-pingaccess: Upgraded components bundled with PingAccess
  removed-unused-apache-commons-dependencies: Removed unused Apache Commons dependencies
  upgraded-netty-component: Upgraded Netty component
  fixed-unread-message-body-handling: Fixed unread message body handling
  fixed-500-error-with-api-applications-using-pingauthorize-access-control-rules: Fixed 500 error with API applications using PingAuthorize access control rules
  fixed-conflicts-during-response-header-reading: Fixed conflicts during response header reading
  fixed-an-issue-with-swapped-json-logging-templates: Fixed an issue with swapped JSON logging templates
  fixed-configuration-import-failure-in-specific-admin-sso-environments: Fixed configuration import failure in specific admin SSO environments
  fixed-an-issue-with-an-acr-generator-ignoring-the-prompt-request-parameter: Fixed an issue with an ACR generator ignoring the Prompt Request Parameter
  fixed-an-admin-api-issue-with-modifying-wildcard-virtual-hosts: Fixed an admin API issue with modifying wildcard virtual hosts
  improved-vague-admin-api-error-message-for-resource-response-generators: Improved vague admin API error message for resource response generators
  zero-downtime-upgrade-limitation: Zero downtime upgrade limitation
  ipv6-limitation: IPv6 limitation
  request-preservation-not-supported-with-safari-private-browsing: Request preservation not supported with Safari private browsing
  engine-and-admin-replica-connection-issue: Engine and Admin Replica connection issue
  token-processor-issue: Token processor issue
  firefox-limitation-for-time-range-rules: Firefox limitation for time range rules
  risk-based-authorization-rule-issue-during-upgrade: Risk-based authorization rule issue during upgrade
  virtual-hosts-with-shared-host-names-retention-issue: Virtual hosts with shared host names retention issue
  asynchronous-front-channel-logout-issue: Asynchronous front-channel logout issue
  invalid-special-characters-permitted-in-identity-mappings: Invalid special characters permitted in identity mappings
  ui-failure-when-assigning-new-key-pair: UI failure when assigning new key pair
  slow-restarts-in-fips-mode: Slow restarts in FIPS mode
  cloudhsm-limited-in-java8u261: CloudHSM limited in Java8u261
  kong-api-limitation: Kong API limitation
  certificate-revocation-list-memory-issue: Certificate revocation list memory issue
  spurious-warning-after-upgrade-or-startup-on-windows: Spurious warning after upgrade or startup on Windows
  deadlock-when-importing-applications-with-significant-reuse: Deadlock when importing applications with significant reuse
  hibernate-deadlock-errors: Hibernate deadlock errors
  console-log-settings-page-doesnt-immediately-reflect-changes-made-in-the-api: Console Log Settings page doesn't immediately reflect changes made in the API
  mutual-tls-with-tls-1-3-might-not-work-with-some-target-servers: Mutual TLS with TLS 1.3 might not work with some target servers
  sni-isnt-set-up-for-virtual-hosts-only-used-in-redirects: SNI isn't set up for virtual hosts only used in redirects
  cannot-assign-rule-sets-containing-a-singular-cors-rule: Cannot assign rule sets containing a singular CORS rule
  saving-overwrites-the-sslciphers-and-sslprotocol-fields-in-the-administrative-api: Saving overwrites the sslCiphers and sslProtocol fields in the administrative API
  cannot-use-fips-mode-with-a-safenet-luna-hsm: Cannot use FIPS mode with a Safenet Luna HSM
  acme-account-creation-fails-while-pingaccess-is-in-fips-mode: ACME account creation fails while PingAccess is in FIPS mode
  device-profiling-causes-infinite-loop-when-using-chrome-devtools: Device profiling causes infinite loop when using Chrome Devtools
  pa-16103: Key pairs cause SSL exception when using Luna HSM Client 10.8
  pingaccess-cant-shut-down-when-using-luna-hsm-client-10-8: PingAccess can't shut down when using Luna HSM Client 10.8
  404-error-for-swagger-1-2-specification-api-docs: 404 error for Swagger 1.2 specification API docs
  cloudhsm-key-pairs-arent-usable-in-fips-mode: CloudHSM key pairs aren't usable in FIPS mode
  modified-json-templates-dont-carry-over-on-an-upgrade: Modified JSON templates don't carry over on an upgrade
  previous-releases: Previous releases
---

# Release notes

New features and improvements in PingAccess. Updated June 2026.

Subscribe for automatic updates: [icon: rss-square, set=fa][PingAccess Release Notes RSS Feed](../release_notes/pa_release_notes.xml)

## PingAccess 9.1.0

Released in June 2026.

### Use *\<cspNonce>* to embed inline JavaScript into templates

New PA-11502

We've made the following changes to all `Content-Security-Policy` (CSP) response headers that PingAccess sends:

* Deprecated the **unsafe-inline** directive.

* Added the **base-uri** directive.

Inline JavaScript script elements and CSS style tags are still allowed after the deprecation of **unsafe-inline**, but they now require valid nonce attributes. Use the new velocity template variable *\<cspNonce>* to add a nonce attribute to any inline JavaScript. Learn more in:

* The `Content-Security-Policy` header default values in the [PingAccess configuration file reference](../reference_guides/pa_config_file_ref.html#pa-security-headers-properties).

* Step 17b in [Adding application resources](../pingaccess_user_interface_reference_guide/pa_adding_application_resources.html).

* The **Templated Challenge** table entry in [Authentication challenge response generator descriptions](../pingaccess_user_interface_reference_guide/pa_acr_generator_descriptions.html).

* The [Unsafe inline script](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Content-Security-Policy/script-src#unsafe_inline_script) section in the MDN Web Docs.

### Authenticate with a QR code

New PA-16117

PingAccess now supports the device authorization grant flow, which allows users to sign on by entering a code after visiting a verification URI on a secondary device. This change makes it easier to authenticate when using a device without a keyboard, reducing friction and potential typos.

Configure the new [**Device Authorization Challenge**](../pingaccess_user_interface_reference_guide/pa_acr_generator_descriptions.html#device) challenge response generator (CRG) to present a QR code to an unauthenticated user attempting to access a protected resource. Scanning the QR code or entering the verification URI into a browser redirects the user to a pre-filled code submission page. After authenticating, all the user needs to do is verify the code and click **Submit**.

Use the new system-generated [**Device Authorization Grant**](../pingaccess_user_interface_reference_guide/pa_authentication.html#device-authz-grant) authentication challenge policy (ACP) as an example.

### Trace requests across PingAccess

New PA-16090

We added the ability to perform distributed tracing for inbound and outbound requests to the PingAccess server. This change simplifies troubleshooting by giving you better observability of server processing across request workflows. For example, you could troubleshoot a bottleneck to identify which components might be contributing to latency issues.

To enable support for distributed tracing, we added a new property to the `run.properties` file and created the `<PA_HOME>/conf/opentelemetry.properties` file to provide control over the OpenTelemetry configuration.

Learn more in [Distributed tracing](../troubleshooting/pa_distributed_tracing.html).

### Added support for Java 25

New PA-16295, PA-16468

* Added support for Java 25. Learn more in the **JRE section** of the [PingAccess system requirements](../installing_and_uninstalling_pingaccess/pa_installation_requirements.html#system-reqs).

* Removed outdated cipher suites from the `pa.fips.tls.ciphers` property's default value. These outdated cipher suites correlated with Java versions that PingAccess no longer supports. Learn more in [Entering FIPS mode](../configuring_and_customizing_pingaccess/pa_fips_mode.html).

### Set audience to the AS issuer to comply with RFC 7523

New PA-16306

[RFC 7523](https://datatracker.ietf.org/doc/html/rfc7523#section-3) now requires stricter handling of the audience claim in private key JWT OAuth client authentication. You must set the audience claim to the issuer identifier of the target Authorization Server.

To address these RFC updates, we added the **Private Key JWT Audience** list to all token providers configurable in the admin console. Learn more in the following sections of the PingAccess documentation:

* PingFederate: [Configuring a PingFederate runtime](../pingaccess_user_interface_reference_guide/pa_pf_runtime.html)

* PingOne: [Configuring PingOne](../pingaccess_user_interface_reference_guide/pa_configuring_p1.html)

* PingOne Advanced Identity Cloud: [Configuring PingOne Advanced Identity Cloud or PingAM as the token provider](../pingaccess_user_interface_reference_guide/pa_configuring_p1aic_or_pingam_as_the_token_provider.html)

* Common: [Configuring OpenID Connect token providers](../pingaccess_user_interface_reference_guide/pa_configuring_oidc.html), [Configuring OAuth authorization servers](../pingaccess_user_interface_reference_guide/pa_configuring_oauth_authz_servers.html).

  |   |                                                                                                                                                                                   |
  | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | For [Configuring OAuth authorization servers](../pingaccess_user_interface_reference_guide/pa_configuring_oauth_authz_servers.html), we also added the **Issuer Endpoint** field. |

By default, **Private Key JWT Audience** is set to **Audience Endpoint** to support backwards compatibility. You should change this selection to **Issuer** or **Both** in your authorization server configuration at your earliest convenience to ensure compliance with RFC 7523.

### Rotate the admin config query certificate without restarting engine nodes

New PA-16316

To rotate certificates previously, you needed to update the `bootstrap.properties` file manually and restart each PingAccess engine node. Delaying certificate rotation on the engine nodes could leave engine nodes unable to connect to the admin node after updating the config query listener, leading to service outages.

PingAccess now uses a two-port certificate rotation approach. Engine nodes poll the [`/engines/rest/config-query-certificate` endpoint](../reference_guides/pa_api_endpoints.html) to retrieve new certificates and add them to the engine node's truststore.

Make sure to review the [PingAccess 9.1 upgrade considerations](../upgrading_pingaccess/pa_upgrade_considerations.html#rotate) and check the [Port requirements](../installing_and_uninstalling_pingaccess/pa_installation_requirements.html#port-reqs), then assign a new key pair to the config query HTTPS listener to kick the changes off. Learn more in [Automatic engine node key rotation for config query listeners](../pingaccess_user_interface_reference_guide/pa_assigning_key_pairs.html#autorotation).

### Set the language your sign-on page displays in

New PA-16317

We've added a new advanced web session setting, the **UI Locales** field. This change makes it possible to set [IETF BCP 47 language tags](https://datatracker.ietf.org/doc/html/rfc5646) using the **ui\_locales** OIDC request parameter, enabling you to provide the sign-on page in a wider variety of languages for end users.

|   |                                                                                                                                               |
| - | --------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Language customization through the **ui\_locales** parameter is available through the sign-on flow only, and applies only to the web session. |

Learn more in [Configuring advanced web session settings](../pingaccess_user_interface_reference_guide/pa_advanced_web_session_settings.html).

### Retry POST requests that failed because of an `UnknownHostException`

New PA-16346

We've added a new availability profile setting, **Retry on Unknown Host**. Select this checkbox to retry a failed POST request against other configured backchannel hosts if the original request failed because of an `UnknownHostException`. This setting can improve service reliability during potential DNS changes.

You can find more information in [Creating availability profiles](../pingaccess_user_interface_reference_guide/pa_creating_availability_profiles.html).

### Retain existing application resource IDs throughout upgrade process

Improved PA-16261

PingAccess now prevents application resource IDs from changing when you [upgrade](../upgrading_pingaccess/pa_upgrading_pa_landing_topic.html) to PingAccess 9.1 or later from any version. This change enables you to reference application resource IDs in custom scripts stably and makes post-upgrade cleanup more efficient.

#### Checking application resource IDs

You can review the audit log output after upgrading PingAccess to confirm that a resource's *original id* and *new id* match. Look for an entry that reads like the following example:

> **Collapse: Example log entry**
>
> ```none
> 2026-03-10T01:06:09,259 (1)
> Entity imported into /applications/<num>/resources: original id '3', new id '3' (2)
> ```
>
> |       |                                                                                                                                                                                                         |
> | ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
> | **1** | The timestamp of the transaction, written in [ISO 8601 format](https://www.iso.org/iso-8601-date-and-time-format.html).                                                                                 |
> | **2** | \<num> is a number indicating which application the resource belongs to. To identify what number an application correlates with, open the application for editing and check the URL in your search bar. |

### Updated third-party dependencies

Security PA-16291

Updated third-party dependencies to address a potential security vulnerability.

### Improved Bouncy Castle security

Security PA-16298, PA-16214

Addressed potential security vulnerabilities relating to Bouncy Castle.

### Updated the Apache Log4j library to version 2.25.3

Security PA-16321

Upgraded the Apache Log4j library to address a potential security vulnerability.

### Updated Netty's parsing behavior

Security PA-16459

Updated Netty's parsing behavior to address a potential security vulnerability.

### Updated component dependencies

Security PA-16477

Updated dependency versions to address potential security vulnerabilities.

### Addressed potential request smuggling security vulnerability

Security PA-16521

Addressed a potential security vulnerability related to request smuggling.

### Addressed potential resource allocation security vulnerability

Security PA-16522

Addressed a potential security vulnerability related to resource allocation for multi-part headers.

### Fixed unnecessary warnings logged for JWKS ATVs

Fixed PA-16320

Fixed an issue that caused the JWKS access token validators (ATVs) to generate unnecessary warning logs if you had configured a **Path** but not a **Third-Party Service**. This issue could occur when using API OAuth authentication with either JWKS ATV.

### Fixed an issue with creating new third-party services

Fixed PA-16328

Fixed an issue that prevented PingAccess from assigning an availability handler when creating a new [**Third-Party Service**](../pingaccess_user_interface_reference_guide/pa_third_party_services.html) with the default **Availability Profile**. This issue could occur when running PingAccess in a cluster.

### Fixed `500` errors caused by key rolling

Fixed PA-16348

Fixed an issue that caused `500` errors after a key roll was triggered because the key roll period had elapsed. This issue could occur when using local access token validation.

### Fixed performance degradation issue with upgrading larger configurations

Fixed PA-16367

Fixed a performance degradation issue that occurred when upgrading to PingAccess 9.0. This issue could occur for configurations that have one or more applications with a large number of resources and rule sets.

### Fixed an issue with modified JSON templates not carrying over on an upgrade

Fixed PA-16449

Fixed an issue that prevented modified files in the `conf/log4j/json-templates` directory from carrying over to the target version when upgrading a PingAccess server. Additionally, PingAccess no longer logs warning messages about not migrating the `json-templates` during the upgrade.

### Fixed an Apache Commons Logging classpath warning

Fixed PA-16458

Fixed an issue that caused PingAccess to log the following warning on startup or during an upgrade when using Java 17 or later:

```none
Standard Commons Logging discovery in action with spring-jcl: please remove commons-logging.jar from classpath in order to avoid potential conflicts
```

### Fixed application-level rule evaluation

Fixed PA-16463

Fixed an issue that caused PingAccess not to evaluate rules applied at the application level.

### Fixed slow admin API response

Fixed PA-16475, PA-16532

Fixed an issue that caused slow responses from the `/engines/certificates` PingAccess admin API endpoint.

### Fixed an issue with automatic resource ordering

Fixed PA-16495

Fixed an issue that caused automatic resource ordering to leave out root resources if another resource had been configured with the `/*` path pattern.

### Fixed an issue causing the admin console to show a blank page

Fixed PA-16508

Fixed an issue that caused the PingAccess admin console to show a blank page when trying to view the **References** tab on a key pair, after configuring a JWT identity mapping without giving the **Custom Claims** field a value.

### Fixed an issue blocking key pair imports

Fixed PA-16530

Fixed an issue that prevented PingAccess from importing key pairs that contain `otherName` attributes configured in the **Subject Alternative Name** field.

### Fixed a POST preservation encoding issue when not using UTF-8

Fixed PA-16531

Fixed an issue that sometimes caused PingAccess to end POST parameter processing early if it encountered non-UTF-8 bytes that could be interpreted as valid UTF-8 bytes.

### PingAccess Add-On SDK class is incompatible in Groovy script rules with Java 17 and later

Issue PA-16292

The PingAccess Add-on SDK class `com.pingidentity.pa.sdk.http.ResponseBuilder` isn't compatible in Groovy script rules with Java 17 and later.

### FIPS mode validation doesn't cover imported key pairs for SHA1

Issue PA-16346, PA-16488

FIPS mode validation doesn't prevent administrators from importing key pairs that contain chained certificates with a SHA1 signature algorithm. SHA1 isn't FIPS-compliant.

As a workaround, set `jdk.sha1.restriction.enabled=true` to enforce exclusion of key pairs that use SHA1 in key pair and certificate imports.

## PingAccess 9.0.4 (June 2026)

### Retry POST requests that failed because of an `UnknownHostException`

New PA-16346

We've added a new availability profile setting, **Retry on Unknown Host**. Select this checkbox to retry a failed POST request against other configured backchannel hosts if the original request failed because of an `UnknownHostException`. This setting can improve service reliability during potential DNS changes.

You can find more information in [Creating availability profiles](../pingaccess_user_interface_reference_guide/pa_creating_availability_profiles.html).

### Updated component dependencies

Security PA-16477

Updated dependency versions to address potential security vulnerabilities.

### Addressed potential request smuggling security vulnerability

Security PA-16521

Addressed a potential security vulnerability related to request smuggling.

### Addressed potential resource allocation security vulnerability

Security PA-16522

Addressed a potential security vulnerability related to resource allocation for multi-part headers.

### Fixed an issue with automatic resource ordering

Fixed PA-16495

Fixed an issue that caused automatic resource ordering to leave out root resources if another resource had been configured with the `/*` path pattern.

### Fixed an issue causing the admin console to show a blank page

Fixed PA-16508

Fixed an issue that caused the PingAccess admin console to show a blank page when trying to view the **References** tab on a key pair, after configuring a JWT identity mapping without giving the **Custom Claims** field a value.

### Fixed an issue blocking key pair imports

Fixed PA-16530

Fixed an issue that prevented PingAccess from importing key pairs that contain `otherName` attributes configured in the **Subject Alternative Name** field.

### Fixed a POST preservation encoding issue when not using UTF-8

Fixed PA-16531

Fixed an issue that sometimes caused PingAccess to end POST parameter processing early if it encountered non-UTF-8 bytes that could be interpreted as valid UTF-8 bytes.

## PingAccess 9.0.3 (May 2026)

### Updated the Apache Log4j library to version 2.25.3

Security PA-16321

Upgraded the Apache Log4j library to address a potential security vulnerability.

### Updated Netty's parsing behavior

Security PA-16459

Updated Netty's parsing behavior to address a potential security vulnerability.

### Fixed an Apache Commons Logging classpath warning

Fixed PA-16458

Fixed an issue that caused PingAccess to log the following warning on startup or during an upgrade when using Java 17 or later:

```none
Standard Commons Logging discovery in action with spring-jcl: please remove commons-logging.jar from classpath in order to avoid potential conflicts
```

### Fixed application-level rule evaluation

Fixed PA-16463

Fixed an issue that caused PingAccess not to evaluate rules applied at the application level.

## PingAccess 9.0.2 (March 2026)

### Fixed unnecessary warnings logged for JWKS ATVs

Fixed PA-16320

Fixed an issue that caused the JWKS access token validators (ATVs) to generate unnecessary warning logs if you had configured a **Path** but not a **Third-Party Service**. This issue could occur when using API OAuth authentication with either JWKS ATV.

### Fixed an issue with creating new third-party services

Fixed PA-16328

Fixed an issue that prevented PingAccess from assigning an availability handler when creating a new [**Third-Party Service**](../pingaccess_user_interface_reference_guide/pa_third_party_services.html) with the default **Availability Profile**. This issue could occur when running PingAccess in a cluster.

### Fixed `500` errors caused by key rolling

Fixed PA-16348

Fixed an issue that caused `500` errors after a key roll was triggered because the key roll period had elapsed. This issue could occur when using local access token validation.

### Fixed performance degradation issue with upgrading larger configurations

Fixed PA-16367

Fixed a performance degradation issue that occurred when upgrading to PingAccess 9.0. This issue could occur for configurations that have one or more applications with a large amount of resources and rule sets.

## PingAccess 9.0.1 (February 2026)

### Fixed unnecessary modifications made by the PingAuthorize access control rule

Fixed PA-16283

By default, PingAccess removes extra backslashes and quotation marks when processing PingAuthorize access control rules. This can cause issues downstream when parsing request bodies attempting to use escape characters.

Added a new checkbox to the [PingAuthorize access control rule](../pingaccess_user_interface_reference_guide/pa_adding_pingauth_access_control_rules.html) configuration, **Unescape Request Body**. Select this checkbox to prevent PingAccess from removing extra backslashes or quotation marks used as escape characters.

## PingAccess 9.0.0 (December 2025)

### Java 11 removal

Info PA-16062

Ping Identity removed Java 11 support from PingAccess in December 2025. You must upgrade to a supported Java version before installing PingAccess 9.0 or later. Learn more about supported Java versions in [PingAccess system requirements](../installing_and_uninstalling_pingaccess/pa_installation_requirements.html#system-reqs).

### Configure email reminders about expiring certificates

New PA-16064

Create an SMTP notification publisher to have PingAccess send email reminders about expiring certificates. This makes it easier to manage multiple certificates and prevent service interruptions.

Learn more in [Notifications](../pingaccess_user_interface_reference_guide/pa-notifications-lp.html).

### Configure access token revocation at the application level

New PA-16065

Added a new checkbox on logout virtual resources and admin SSO settings, **Revoke Access Token**.

Use this setting to revoke access tokens maintained in the associated PingAccess web session per [RFC 7009](https://www.rfc-editor.org/rfc/rfc7009.txt) when someone accesses a logout virtual resource or when the PingAccess admin signs off.

This provides additional security and helps prevent session replay in cases where session validation and single logout aren't available with the token provider. For example, you could use **Revoke Access Token** to sign off individual applications without disrupting the token provider session.

Learn more in [Adding application resources](../pingaccess_user_interface_reference_guide/pa_adding_application_resources.html) and [Configuring admin UI SSO authentication](../pingaccess_user_interface_reference_guide/pa_configuring_admin_ui_sso_authn_lp.html#configuring-admin-ui-sso-authentication).

### Configure custom properties for PingAccess applications

New PA-16066

Define custom properties globally and set specific values for them at the application level to provide additional information about your applications. Use these extended properties to provide meaningful details to admins and sort through configured applications more efficiently.

Learn more in [Managing extended properties](../pingaccess_user_interface_reference_guide/pa-managing-extended-properties.html).

### Map incoming request parameters from the requested resource to the token provider

New PA-16087

Added a new advanced web session setting, **Passthrough Request Parameters**. Use this table to select parameters from the requested resource and map them to OIDC parameters the token provider uses during the access request.

This enables you to pass information to the token provider to customize user sign-on experience and make it more consistent with your brand. For example:

* Forward the username to prefill this value in the sign-on template

* Forward an organization ID to display branding that the user expects

Learn more in [Configuring advanced web session settings](../pingaccess_user_interface_reference_guide/pa_advanced_web_session_settings.html).

### Use the PingAccess agent for NGINX with NGINX R35

New PA-16223

Added support for NGINX R35 and dropped support for NGINX R31. Learn more in [NGINX agent system requirements](../agents_and_integrations/pa_nginx_system_reqs.html).

### Add your own JWKS endpoints for access token validation

New PA-16225

PingAccess now allows you to validate access tokens against JWKS endpoints that aren't hosted by the token provider, enabling you to validate access tokens against multiple issuers.

Add your JWKS endpoint as a [third-party service](../pingaccess_user_interface_reference_guide/pa_third_party_services.html) by specifying the host and port. Then use the new **Third-Party Service** list in the access token validator configuration to select the third-party service you created.

Learn more in [Adding access token validators](../pingaccess_user_interface_reference_guide/pa_adding_access_token_validators.html).

### Updated the `run.sh` script

Security PA-14023

Added a new property to the `run.sh` script to enhance security.

### RSA 1.5 with PKCS#1 removal

Security PA-14094

Removed support for RSA 1.5 with PKCS#1 to enhance security.

### Upgraded components bundled with PingAccess

Security PA-16107, PA-16108, & PA-16109

* Updated ehcache.

* Upgraded CSD tool.

* Replaced `javax-el` instances with `jakarta-el`.

### Removed unused Apache Commons dependencies

Security PA-16113

Removed unused dependencies on the Apache Commons Validator and BeanUtils components.

### Upgraded Netty component

Security PA-16211

Upgraded the Netty component to fix issues with chunk parsing and overlarge buffers.

### Fixed unread message body handling

Fixed PA-7068

Fixed an issue that caused `com.pingidentity.pa.sdk.http.Exchange#setResponse` to immediately discard the body of an existing response, which could have put a backend connection into an unknown state if the connection was going to be reused.

`com.pingidentity.pa.sdk.http.Exchange#setRequest` behaved similarly with existing requests. Now, the body of a request or response that's going to be replaced isn't discarded until the replacement message has been written successfully.

Also fixed an issue that caused `com.pingidentity.pa.sdk.http.Message#setBody` and `com.pingidentity.pa.sdk.http.Message#setBodyContent` to put backend connections into an unknown state because they weren't discarding the message body.

### Fixed `500` error with API applications using PingAuthorize access control rules

Fixed PA-16114

Fixed an issue that sometimes caused a `500` error when using the [PingAuthorize access control rule](../pingaccess_user_interface_reference_guide/pa_adding_pingauth_access_control_rules.html) with a PingAccess API application. This issue could occur with `PUT` and `POST` requests made when there was already a high volume of requests.

### Fixed conflicts during response header reading

Fixed PA-16122

Fixed an issue that sometimes caused conflicts during asynchronous backend connection handling when PingAccess modified response headers.

### Fixed an issue with swapped JSON logging templates

Fixed PA-16227

Fixed an issue that swapped the contents of the `<PA_HOME>/conf/log4j/json-templates/sideband-client-audit-log.json` file and the `<PA_HOME>/conf/log4j/json-templates/sideband-audit-log.json` file.

Also added the `exchangeId` to the `pingaccess-log.json` file.

### Fixed configuration import failure in specific admin SSO environments

Fixed PA-16237

Fixed an issue that caused configuration imports to fail if prompted by an administrator. This issue was applicable if both the administrator and platform administrator roles were enabled in an environment using admin SSO without a configured admin token provider.

### Fixed an issue with an ACR generator ignoring the **Prompt Request Parameter**

Fixed PA-16240

Fixed an issue that caused the **OIDC Authentication Request Redirect** [authentication challenge response generator](../pingaccess_user_interface_reference_guide/pa_acr_generator_descriptions.html) to ignore the **Prompt Request Parameter** configured in the [authentication challenge policy](../pingaccess_user_interface_reference_guide/pa-managing-acps.html).

### Fixed an admin API issue with modifying wildcard virtual hosts

Fixed PA-16244

Fixed an issue that caused `PUT` API operations to fail when trying to modify a virtual host containing a wildcard. This issue was applicable to environments using a proxied PingFederate token provider.

### Improved vague admin API error message for resource response generators

Fixed PA-16266

Improved vague error messaging for invalid input formats in resource response generators. This error message now identifies the invalid value and the corresponding field.

### Zero downtime upgrade limitation

Issue PAPQ-1034

PingAccess 6.3 deployments that use the Sideband API feature can't be upgraded using the zero downtime upgrade procedure. You must use a planned outage to upgrade such an environment.

### IPv6 limitation

Issue PA-1894

Incorrect handling for IPv6 literals in host header. Note that IPv6 isn't currently supported.

### Request preservation not supported with Safari private browsing

Issue PA-2896

Request preservation isn't supported with Safari Private Browsing.

### Engine and Admin Replica connection issue

Issue PA-4888

Engines and admin replicas don't connect to the admin console if a combination of IP addresses and DNS names are used.

### Token processor issue

Issue PA-6262

The token processor can't connect to a JWKS endpoint using SSL when using an IP instead of a host name. To workaround this issue, add the host name as the subject alt name on the key pair.

### Firefox limitation for time range rules

Issue PA-8651

Firefox doesn't correctly support the HTML5 time tag. When using the [time range rule](../pingaccess_user_interface_reference_guide/pa_adding_time_range_rules.html), enter time in 24-hour format.

### Risk-based authorization rule issue during upgrade

Issue PA-10505

Upgrades will fail with a risk-based authorization rule if a third-party service isn't used in the rule.

### Virtual hosts with shared host names retention issue

Issue PA-11390

If you create multiple virtual hosts with a shared host name and associate the host name with a server key pair, the virtual hosts retain the connection with the server key pair even if they are subsequently renamed. The virtual host must be deleted and recreated to remove the association.

### Asynchronous front-channel logout issue

Issue PA-12647

Asynchronous front-channel logout might fail in some browsers depending on end-user settings. You can find browser-specific workarounds in [Managing single logout in different browsers](https://support.pingidentity.com/s/article/Managing-Single-Log-Out-in-different-browsers) in the Ping Identity Knowledge Base.

### Invalid special characters permitted in identity mappings

Issue PA-13214

Invalid special characters (`(),/;<⇒?@[\]\{}"`) can be added to the certificate to Header Mapping field in an identity mapping. Adding this identity mapping to an application will cause `400` errors when the application is accessed.

### UI failure when assigning new key pair

Issue PA-13500

Assigning a new key pair to the Admin HTTPS listener if the browser doesn't trust the new key pair can prevent the UI from functioning. The workaround is to close the browser and reopen it so that all connections to the admin node use the new certificate.

### Slow restarts in FIPS mode

Issue PA-14239

If PingAccess is repeatedly stopped and restarted in FIPS mode, subsequent restarts can take up to 5 minutes to complete. The workaround is to use a tool such as rng-tools to refresh `/dev/random` and make more entropy available faster. For example:

```
sudo yum install rng-tools
sudo rngd -b
```

### CloudHSM limited in Java8u261

Issue PA-14414

CloudHSM functionality works in FIPS mode but not in regular mode for `Java8u261` and later. `RSASSA-PSS` signing algorithms fail with `Java8u261` or later, and HSM vendors and core Java use different naming conventions for the `RSASSA-PSS` algorithm. There is a documented workaround in [Adding an AWS CloudHSM provider](../pingaccess_user_interface_reference_guide/pa_adding_an_aws_cloudhsm_provider.html).

### Kong API limitation

Issue PA-14466

Due to an outstanding defect in the Kong API Gateway, the `ping-auth` plugin currently doesn't support requests that utilize the `Transfer-Encoding` header. If PingAccess is used as the external authorization server, the [rewrite content rule](../pingaccess_user_interface_reference_guide/pa_adding_rewrite_content_rules.html) can prevent the page from displaying.

### Certificate revocation list memory issue

Issue PA-14621

If a client certificate has a certificate revocation list (CRL) DistributionPoint that points to an extremely large CRL, PingAccess might suffer from high memory usage leading to Out of memory (OOM) exceptions.

### Spurious warning after upgrade or startup on Windows

Issue PA-14907

After starting PingAccess for the first time on a Windows system or upgrading PingAccess on a Windows system, a warning message is logged reporting that the `pa.jwk` file was not made non-executable. This message can be ignored.

### Deadlock when importing applications with significant reuse

Issue PA-14978

A race condition caused by importing applications with significant reuse of virtual hosts or context roots can deadlock the Apache Derby DB.

PingAccess 7.3 added systematic deadlock handling to reattempt operations that lead to a deadlock condition in Apache Derby. Learn more about this original fix in [PA-14974 in the PingAccess 7.3 release notes](#previous-releases).

However, a specific fix for this deadlock scenario will be added in a future release to reduce wasted cycles and warning or error log messages.

### Hibernate deadlock errors

Issue PA-14985

There are a few potential scenarios when the PingAccess data layer might encounter deadlocks. PingAccess should be able to recover from these deadlocks, so hibernate error logs can be ignored when followed by the log message `Recovered from database deadlock with transaction retry.`

### Console **Log Settings** page doesn't immediately reflect changes made in the API

Issue PA-15351

If you have the administrative console and API open at the same time and you're on a console page that isn't **Log Settings**, the **Log Settings** page won't immediately populate any log changes that you make in the API.

To work around this issue, go to the **Log Settings** page. Perform a hard refresh, or go to another page and then return to **Log Settings**.

### Mutual TLS with TLS 1.3 might not work with some target servers

Issue PA-15499

Mutual TLS with a backend site that requires post-handshake authentication isn't supported when using TLS 1.3. Current workaround options are to remove the requirement for post-handshake authentication from the backend site or to disable TLS 1.3.

### SNI isn't set up for virtual hosts only used in redirects

Issue PA-15559

Currently, SNI is only set up for virtual hosts that are actively configured in an application. This can prevent PingAccess from presenting an expected certificate for a given redirect host.

The workaround is to configure the source host in a redirect as the virtual host for a disabled PingAccess application.

### Cannot assign rule sets containing a singular CORS rule

Issue PA-15785

Rule sets or rule set groups containing a singular CORS rule can't be assigned to applications or resources. Attempts result in the following validation error:

```
Invalid rule assignment for Application '<app_name>': assigning multiple Cross-Origin Request Policies to a Resource or RuleSet isn't allowed.
```

### Saving overwrites the **sslCiphers** and **sslProtocol** fields in the administrative API

Issue PA-15863

Saving a configuration in the PingAccess administrative console overwrites the values of the API-only fields **sslCiphers** and **sslProtocols**.

This issue is only relevant for the following pages in the administrative console:

* **System > Token Provider** (with **PingOne Advanced Identity Cloud / PingAM** selected)

* **System > Admin Authentication > Admin Token Provider**

It affects the following administrative API endpoints:

* `/pingone/advancedIdentityCloud`

* `/auth/tokenProvider`

### Cannot use FIPS mode with a Safenet Luna HSM

Issue PA-15928

[Federal Information Processing Standards (FIPS) mode](../configuring_and_customizing_pingaccess/pa_fips_mode.html) doesn't work with [Safenet Luna HSM](../pingaccess_user_interface_reference_guide/pa_adding_a_safenet_luna_provider.html). Trying to configure a key pair or enter FIPS mode with a key pair already configured causes a `Null Pointer Exception` error.

### ACME account creation fails while PingAccess is in FIPS mode

Issue PA-15929

[Federal Information Processing Standards (FIPS) mode](../configuring_and_customizing_pingaccess/pa_fips_mode.html) can't be used with [ACME certificate management](../pingaccess_user_interface_reference_guide/pa_managing_certificates_for_key_pairs_with_acme.html) if you need to create an ACME account.

### Device profiling causes infinite loop when using Chrome Devtools

Issue PA-16094

Performing PingOne Protect device profiling with Chrome Devtools open causes an infinite loop. To proceed with device profiling, close Chrome Devtools.

### Key pairs cause SSL exception when using Luna HSM Client 10.8

Issue PA-16103

Key pairs stored in a Safenet Luna HSM cause SSL exceptions if using Luna HSM Client 10.8.

A potential workaround for this issue is to disable TLS 1.3 and RSASSA-PSS in the `run.properties` file. You can find more information in the **TLS/SSL** section of the PingAccess [Configuration file reference](../reference_guides/pa_config_file_ref.html#pa-tls-ssl).

### PingAccess can't shut down when using Luna HSM Client 10.8

Issue PA-16104

PingAccess fails to shut down when the Safenet Luna HSM `libCryptoki2.so` directory is in the `deploy` directory, which is a deployment requirement for [Adding a Safenet Luna provider](../pingaccess_user_interface_reference_guide/pa_adding_a_safenet_luna_provider.html) on a Linux system. This is an issue specific to Luna HSM Client 10.8.

### `404` error for Swagger 1.2 specification API docs

Issue PA-16230

Trying to access the Swagger 1.2 specification information for specific individual endpoints (such as `/pa-admin-api/v3/api-docs/pa/accessTokenValidators`) currently results in a `404 Not Found` error.

This happens because Swagger 1.2 isn't fully compatible with JDK 17. Ping Identity recommends using the OAS 2.0 specifications instead, which you can find at https\://*\<pa\_admin\_host>*:*\<pa\_admin\_port>*/pa-admin-api/v3/api-docs/pa/api-docs-v2.json. Learn more in [Administrative API endpoints](../reference_guides/pa_admin_api_endpoints.html).

### CloudHSM key pairs aren't usable in FIPS mode

Issue PA-16236

Trying to use CloudHSM key pairs in [Managing Federal Information Processing Standards (FIPS) mode](../configuring_and_customizing_pingaccess/pa_fips_mode.html) prompts an `ERR_SSL_PROTOCOL_ERROR` message.

### Modified JSON templates don't carry over on an upgrade

Issue PA-16449

When upgrading a PingAccess server, modified files in the `conf/log4j/json-templates` directory don't carry over to the target version. Additionally, PingAccess logs warning messages about not migrating the `json-templates` during the upgrade, even if you made no edits to the template files.

## Previous releases

You can find information about enhancements and issues resolved in previous releases of PingAccess, beginning with PingAccess 3.2, in the [Ping Identity Documentation Archive](https://docs.pingidentity.com/archive/).

For information about enhancements and issues resolved in other actively maintained releases of PingAccess, refer to the following release notes:

* [PingAccess 9.0](https://docs.pingidentity.com/pingaccess/9.0/release_notes/pa_release_notes.html)

* [PingAccess 8.3](https://docs.pingidentity.com/pingaccess/8.3/release_notes/pa_release_notes.html)

* [PingAccess 8.2](https://docs.pingidentity.com/pingaccess/8.2/release_notes/pa_release_notes.html)

* [PingAccess 8.1](https://docs.pingidentity.com/pingaccess/8.1/release_notes/pa_release_notes.html)

* [PingAccess 8.0](https://docs.pingidentity.com/pingaccess/8.0/release_notes/pa_release_notes.html)

* [PingAccess 7.3](https://docs.pingidentity.com/pingaccess/7.3/release_notes/pa_release_notes.html)

* [PingAccess 7.2](https://docs.pingidentity.com/pingaccess/7.2/release_notes/pa_release_notes.html)