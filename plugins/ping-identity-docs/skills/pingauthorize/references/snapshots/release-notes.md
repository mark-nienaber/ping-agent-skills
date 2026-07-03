---
title: Release Notes
description: New features and improvements in PingAuthorize. Updated June 2026.
component: pingauthorize
version: 11.1
page_id: pingauthorize:release_notes:paz_release_notes_legacy_home
canonical_url: https://docs.pingidentity.com/pingauthorize/11.1/release_notes/paz_release_notes_legacy_home.html
llms_txt: https://docs.pingidentity.com/pingauthorize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 23, 2026
section_ids:
  pingauthorize-11-1-0-0-june-2026: PingAuthorize 11.1.0.0 (June 2026)
  added-runtime-support-for-java-25: Added runtime support for Java 25
  added-aws-iam-authentication-for-elasticache-and-s3: Added AWS IAM authentication for ElastiCache and S3
  added-custom-handling-for-non-2xx-http-service-responses: Added custom handling for non-2xx HTTP service responses
  added-support-for-multiple-self-governance-system-usernames: Added support for multiple self-governance system usernames
  added-smtp-bearer-access-token-authentication: Added SMTP bearer access token authentication
  added-correlation-id-to-gateway-request-and-response-logs: Added correlation ID to gateway request and response logs
  improved-policy-query-evaluation-performance: Improved policy query evaluation performance
  added-pagination-to-the-deployment-package-list: Added pagination to the deployment package list
  expanded-scope-claim-format-support-in-contains-claim-pair-conditions: Expanded scope claim format support in Contains Claim Pair conditions
  simplified-trust-framework-element-creation: Simplified Trust Framework element creation
  improved-access-control-rule-parsing-and-validation: Improved access control rule parsing and validation
  improved-connection-asymmetry-alarm-visibility: Improved connection-asymmetry alarm visibility
  reduced-server-startup-time-on-linux: Reduced server startup time on Linux
  improved-prometheus-metrics-output-format: Improved Prometheus metrics output format
  upgraded-the-embedded-http-server-to-jetty-12: Upgraded the embedded HTTP server to Jetty 12
  removed-scim-1-1-support: Removed SCIM 1.1 support
  updated-the-opencsv-library: Updated the opencsv library
  fixed-502-errors-when-using-an-http-proxy-with-api-external-servers: Fixed 502 errors when using an HTTP proxy with API external servers
  fixed-an-issue-with-scoped-caching: Fixed an issue with scoped caching
  fixed-the-nodetach-option-for-start-server: Fixed the --nodetach option for start-server
  fixed-a-tls-1-3-connection-termination-issue: Fixed a TLS 1.3 connection termination issue
  fixed-a-manage-profile-replace-profile-error: Fixed a manage-profile replace-profile error
  fixed-manage-profile-generate-profile-excluding-obscured-properties: Fixed manage-profile generate-profile excluding obscured properties
  fixed-a-server-shutdown-delay-issue: Fixed a server shutdown delay issue
  pingauthorize-11-0-0-2-march-2026: PingAuthorize 11.0.0.2 (March 2026)
  added-a-policy-query-logger-sdk-extension: Added a Policy Query Logger SDK extension
  fixed-an-issue-with-admin-console-icons-in-closed-environments: Fixed an issue with admin console icons in closed environments
  fixed-a-server-startup-warning-related-to-slf4j: Fixed a server startup warning related to SLF4J
  pingauthorize-11-0-0-1-march-2026: PingAuthorize 11.0.0.1 (March 2026)
  version-increased-for-administrative-purposes: Version increased for administrative purposes
  pingauthorize-11-0-0-0-december-2025: PingAuthorize 11.0.0.0 (December 2025)
  converted-the-pingauthorize-admin-console-to-react: Converted the PingAuthorize admin console to React
  step-up-authentication-for-apis: Step-up authentication for APIs
  new-json-manipulation-functions-for-spel: New JSON manipulation functions for SpEL
  added-support-for-rsassa-pss-signing-algorithms: Added support for RSASSA-PSS signing algorithms
  added-http-metrics-to-the-periodic-stats-logger: Added HTTP metrics to the Periodic Stats Logger
  standardized-url-decoding-behavior: Standardized URL decoding behavior
  documented-the-monitor-history-plugin: Documented the Monitor History plugin
  aws-java-sdk-upgrade: AWS Java SDK upgrade
  enhanced-flexibility-for-policy-query-requests: Enhanced flexibility for policy query requests
  improved-handling-of-null-values-in-redis: Improved handling of null values in Redis
  added-more-control-over-response-timestamp-precision: Added more control over response timestamp precision
  enabled-default-condition-short-circuiting-in-the-policy-editor: Enabled default condition short-circuiting in the Policy Editor
  optimized-setup-behavior-for-modern-jvms: Optimized setup behavior for modern JVMs
  improved-policy-query-performance: Improved policy query performance
  added-server-out-files-to-csd-archives: Added server.out files to CSD archives
  improved-expired-certificate-handling-for-tls-negotiation: Improved expired certificate handling for TLS negotiation
  fixed-array-handling-in-spel: Fixed array handling in SpEL
  fixed-an-issue-with-deployment-package-deletion: Fixed an issue with deployment package deletion
  fixed-an-issue-with-policy-dependency-pagination: Fixed an issue with policy dependency pagination
  fixed-an-issue-with-http-service-timeouts: Fixed an issue with HTTP service timeouts
  fixed-a-policy-editor-startup-issue: Fixed a Policy Editor startup issue
  fixed-inconsistent-url-decoding: Fixed inconsistent URL decoding
  fixed-an-issue-with-profile-replacement-in-topologies: Fixed an issue with profile replacement in topologies
  fixed-an-issue-with-performlocalcleanup-in-interactive-mode: Fixed an issue with --performLocalCleanup in interactive mode
  archive: Previous Releases
---

# Release Notes

New features and improvements in PingAuthorize. Updated June 2026.

Subscribe to get automatic updates: [icon: rss-square, set=fa][PingAuthorize Release Notes RSS feed](paz_release_notes_legacy_home.xml)

## PingAuthorize 11.1.0.0 (June 2026)

### Added runtime support for Java 25

New PAZ-21209

We added JRE support for Oracle JDK 25 and OpenJDK 25.

|   |                                                                                                                                                              |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | Refer to the [upgrade considerations](../upgrading_pingauthorize/paz_upgrade_consids.html) for Java-related actions you must take when upgrading to Java 25. |

### Added AWS IAM authentication for ElastiCache and S3

New PAZ-21190

We added support for IAM Roles for Service Accounts (IRSA) with Amazon S3 deployment package and snapshot stores, and AWS KMS encryption. Omit static AWS access keys to use IRSA-projected credentials when running on Amazon EKS. Learn more in [Adding an Amazon S3 deployment package store to PingAuthorize](../pingauthorize_server_administration_guide/paz_amazons3_deploy_package.html).

We also added support for AWS Identity and Access Management (IAM) authentication for ElastiCache attribute and service caches. This removes the need to store Redis passwords in configuration files. Set `use-iam-auth` to `true` in your ElastiCache configuration to use short-lived IAM tokens instead of a static password. Learn more in [Configuring Trust Framework attribute caching for development](../pingauthorize_server_administration_guide/paz_tf_attribute_cache_external.html) and [Configuring Trust Framework attribute caching for production](../pingauthorize_server_administration_guide/paz_tf_attribute_cache_embedded.html).

### Added custom handling for non-2xx HTTP service responses

New PAZ-22196

We added the ability to pass non-2xx responses from HTTP services to policy evaluation as meaningful inputs, rather than treating them solely as failures. This allows policies to distinguish between expected service responses and genuine infrastructure errors, enabling more precise authorization decisions based on the full range of service outcomes.

Learn more in [HTTP services](../pingauthorize_policy_administration_guide/paz_http_services.html#return_full_response).

### Added support for multiple self-governance system usernames

New PAZ-20203

The `--selfGovernanceSystemUsername` setup parameter now accepts a comma-separated list of usernames, allowing multiple self-governance administrators to manage the Policy Editor.

Learn more in [Installing the Policy Editor non-interactively](../installing_and_uninstalling_pingauthorize/paz_install_pe_noninteractive.html) and [Self-governance](../pingauthorize_policy_administration_guide/paz_self_gov.html).

### Added SMTP bearer access token authentication

New DS-48730

The server now supports SMTP authentication by bearer access token. You can obtain a token through the OAuth 2.0 client credentials flow or configure a static token.

### Added correlation ID to gateway request and response logs

Improved PAZ-22371

API security gateway request and response logs now include the correlation ID and request ID associated with each client request, enabling end-to-end correlation with policy decision and service logs.

Learn more in [Managing HTTP correlation IDs](../pingauthorize_server_administration_guide/paz_manage_http_corr_ids.html).

### Improved policy query evaluation performance

Improved PAZ-20454

We improved policy query evaluation for requests with a large number of permutations. Request data is now parsed once per request rather than once per permutation, reducing processing overhead and improving response times.

### Added pagination to the deployment package list

Improved PAZ-19361

The deployment package list in the Branch Manager now supports pagination, giving you access to the full package history in environments with more than 100 deployment packages.

Learn more in [Deployment packages](../pingauthorize_policy_administration_guide/paz_managing_deployment_packages.html).

### Expanded scope claim format support in Contains Claim Pair conditions

Improved PAZ-22138

The **Contains Claim Pair** and **Does Not Contain Claim Pair** conditions now accept scope claims expressed as a JSON array of strings or a comma-delimited string, in addition to the existing space-delimited string format.

Learn more in [Conditions](../pingauthorize_policy_administration_guide/paz_conditions.html#condition_comparators).

### Simplified Trust Framework element creation

Improved PAZ-22320

We've simplified the creation of Trust Framework elements. The **+** button now opens the element's definition form directly without an intermediate menu.

### Improved access control rule parsing and validation

Improved DS-51399

We added a new mechanism for parsing and validating access control rules. The new parser runs alongside the existing one and might help identify problematic ACIs and provide more useful error messages for malformed rules.

All currently valid ACIs continue to be accepted and operate as before. The server raises an administrative alert upon encountering any ACIs not supported by the new parser.

|   |                                                                                                                             |
| - | --------------------------------------------------------------------------------------------------------------------------- |
|   | We plan to remove the existing parser in a future release. At that time, ACIs flagged by the new parser won't be permitted. |

### Improved connection-asymmetry alarm visibility

Improved DS-49225

You can now quickly identify peers causing topology connection-asymmetry alarms. The mirrored subtree manager monitor entry automatically includes the `peer-inbound-only` and `peer-outbound-only` attributes if any servers appear in only the inbound or outbound connection set. Connection-asymmetry alarm messages include the names of the peers involved.

### Reduced server startup time on Linux

Improved DS-50645

To reduce server startup time when you run `start-server`, we reduced the number of Java processes that get created before starting the server. This change only applies to Linux and is enabled by default.

|   |                                                                                                                                                                                                                                                                                                                                                                 |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | In deployments that run multiple server instances per node, parallel server startups can increase short-term CPU load, because JVM initialization occurs at the same time across instances. This effect might be more noticeable with this improvement enabled.To revert to the prior behavior, set the environment variable `UNBOUNDID_FAST_START` to `false`. |

### Improved Prometheus metrics output format

Improved DS-51115

The Prometheus Monitoring HTTP Servlet Extension now groups metrics with the same name under common `HELP` and `TYPE` headers, which more closely follows the standard for annotating metric families in Prometheus.

### Upgraded the embedded HTTP server to Jetty 12

Info DS-51450

We upgraded the embedded HTTP server from Jetty 11 to Jetty 12. Most behavior is preserved, with the following exceptions:

* HTTP requests with unencoded reserved characters in path segments (for example, a literal forward slash in a distinguished name such as `/directory/v1/sn=Sch/m*i^d`) now receive a `400 Bad Request` response instead of being silently truncated at the reserved character. Clients using the Directory REST API, SCIM API, or any other HTTP servlet extension must percent-encode reserved characters in URL path segments. For example, encode a forward slash in an attribute value as `%2F`, a caret as `%5E`, and a question mark as `%3F`. This requirement is specified in [RFC 3986](https://datatracker.ietf.org/doc/html/rfc3986) and is now enforced.

* The `Location` header in HTTP redirect responses now always contains an absolute URI as required by [RFC 7231](https://datatracker.ietf.org/doc/html/rfc7231). Update any clients that relied on a relative URI in this header.

### Removed SCIM 1.1 support

Info DS-49199

We removed SCIM 1.1 and related functionality from the server. Migrate any functionality to SCIM 2.0.

|   |                                                                                                                                                                                                                                                                                        |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | If the server uses SCIM 1.1, you must remove the servlet extensions from all HTTP connection handlers before upgrading. For example:```shell
$ bin/dsconfig set-connection-handler-prop \
    --handler-name "HTTPS Connection Handler" \
    --remove http-servlet-extension:SCIM
``` |

### Updated the opencsv library

Info DS-51436

We updated the opencsv library from the abandoned `net.sf.opencsv` 2.3 to the current `com.opencsv` 5.10.

### Fixed 502 errors when using an HTTP proxy with API external servers

Fixed PAZ-22700

We fixed an issue where gateway API endpoint requests failed with `502 Bad Gateway` when the API external server had an HTTP proxy external server configured.

### Fixed an issue with scoped caching

Fixed PAZ-22768

We fixed an issue where missing inputs for cached attributes could cause policy evaluation to fail, even when the service call to resolve that attribute was successful.

### Fixed the `--nodetach` option for `start-server`

Fixed DS-51565

We fixed the `--nodetach` option for `start-server` so that it correctly prevents the server from starting in a detached manner.

### Fixed a TLS 1.3 connection termination issue

Fixed DS-51445

We fixed an issue that could cause a small percentage of LDAP connections secured with TLS 1.3 to be prematurely terminated.

### Fixed a `manage-profile replace-profile` error

Fixed DS-51396

We fixed an issue where the `manage-profile replace-profile` tool could fail with a `DirectoryNotEmptyException` during upgrades in environments where the logs directory was mounted as a separate volume. The failure was caused by the tool holding an internal lock on a background optimization file during the upgrade process. Now, the tool correctly releases these locks and skips migration of non-essential cache files.

We also fixed an issue where the `setup` tool didn't always correctly apply the `--optionCacheDirectory` argument.

### Fixed `manage-profile generate-profile` excluding obscured properties

Fixed DS-51245

We fixed an issue where, after an upgrade, `manage-profile generate-profile` excluded `dsconfig` commands from the profile that set obscured properties.

### Fixed a server shutdown delay issue

Fixed DS-51291

We fixed an issue where a large number of peer connections or unresponsive peers could cause excessively long server shutdown times.

## PingAuthorize 11.0.0.2 (March 2026)

### Added a Policy Query Logger SDK extension

New PAZ-21778

We added a new Policy Query Logger extension to the Server SDK for customizing how policy query requests, responses, and permutations are logged. You can use this extension to:

* Define custom log formats and destinations.

* Integrate with external logging systems.

Learn more in [Server SDK Extensions](../pingauthorize_server_administration_guide/paz_managing_sdk_extensions.html).

### Fixed an issue with admin console icons in closed environments

Fixed DS-50165

The admin console now properly displays icons when running in an environment that doesn't have access to the internet, such as a closed environment.

### Fixed a server startup warning related to SLF4J

Fixed DS-50990

We resolved the following server startup warning: `SLF4J(E): A service provider failed to instantiate: org.slf4j.spi.SLF4JServiceProvider: Provider org.slf4j.impl.PingSLF4JServiceProvider not found.`

## PingAuthorize 11.0.0.1 (March 2026)

### Version increased for administrative purposes

Info

The PingAuthorize version number was incremented due to changes released for PingDirectory. There are no release notes for this version of PingAuthorize.

## PingAuthorize 11.0.0.0 (December 2025)

### Converted the PingAuthorize admin console to React

New DS-44421

We've rebuilt the PingAuthorize admin console from AngularJS to a modern React-based interface. The updated console offers improved performance, accessibility, and maintainability while preserving familiar configuration and monitoring workflows.

In addition to this restyling, we've introduced:

* **Read-only mode support**: You can now place the admin console into read-only mode using the `system.readOnly` configuration property, preventing changes to server configuration.

* **Expert-level configuration**: The admin console's `configuration.complexity` property now defaults to `expert`, allowing you to view and create expert-level configuration objects.

* **Configurable console name**: You can now change the admin console's displayed title using the `branding.appName` configuration property.

|   |                                                                            |
| - | -------------------------------------------------------------------------- |
|   | The React-based admin console requires PingAuthorize Server 11.0 or later. |

Learn more in [Using the PingAuthorize admin console](../pingauthorize_server_administration_guide/paz_using_admin_console.html).

### Step-up authentication for APIs

New PAZ-17047

You can now force step-up authentication when users access sensitive resources. When authenticated users try to access higher-risk data, such as salary information, health records, or premium content, you can require a higher level of authentication and also set limits on the amount of time allowed since the last authentication event.

Use the new **Auth Challenge** statement type to implement step-up authentication requirements in your policies. Learn more in [Step-up authentication for APIs](../pingauthorize_policy_administration_guide/paz_step_up_auth.html).

### New JSON manipulation functions for SpEL

New PAZ-17686

PingAuthorize now includes productized JSON data manipulation functions for SpEL, making it easier to query, filter, and transform JSON data directly within policies.

This release introduces the following functions:

* `data_associateByKey`: Joins two JSON arrays or objects based on a shared key, allowing you to enrich one data set with related information from another.

* `data_containsKey`: Filters a JSON collection to return only objects that contain a specific key.

By providing native support for common JSON operations, these functions improve policy clarity, consistency, and performance while reducing reliance on custom expressions.

Learn more in [SpEL processing examples](../pingauthorize_policy_administration_guide/paz_spel_example_functions.html).

### Added support for RSASSA-PSS signing algorithms

New PAZ-19054

The ID Token Validator and JWT Access Token Validator now support the PS256, PS384, and PS512 signing algorithms for OIDC-based logins to the PingAuthorize admin console or Policy Editor.

Learn more in [Access token validator types](../pingauthorize_server_administration_guide/paz_access_token_val_types.html).

### Added HTTP metrics to the Periodic Stats Logger

New PAZ-17947

We've added support for HTTP metrics in the Periodic Stats Logger, offering deeper insights into HTTP request flow and PingAuthorize Server performance. When enabled, the server captures detailed statistics at rolling 1-minute, 5-minute, and 15-minute intervals to help monitor short-term spikes and longer-term trends.

Learn more in [Enabling HTTP metrics in the Periodic Stats Logger](../pingauthorize_server_administration_guide/paz_enable_http_metrics_stats_logger.html).

### Standardized URL decoding behavior

Info PAZ-20178

We've standardized URL decoding behavior:

* **Policy evaluation**: The PingAuthorize Server now decodes the incoming request URL, including the path and query parameters, exactly once before policy evaluation.

* **Request forwarding**: The PingAuthorize Server now forwards the original, unmodified request URL to the backend resource server.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Backend resource servers must now perform their own URL decoding in accordance with [RFC-3986](https://datatracker.ietf.org/doc/html/rfc3986). If your resource servers previously relied on PingAuthorize to forward fully-decoded request URLs, now these servers might fail to process encoded URLs correctly. You must update these servers to handle encoded URLs or deploy a proxy to decode traffic before it reaches the server. |

### Documented the Monitor History plugin

Info PAZ-18453

We've added documentation for the PingAuthorize Server's Monitor History plugin, a server component designed to help analyze performance issues and server crashes. This new documentation details how to:

* Capture the server state leading up to a crash or restart.

* View Java Virtual Machine (JVM) stack traces to identify blocked or stuck threads.

* Monitor resource usage and work queue depth over time.

Learn more in [Using the Monitor History plugin](../pingauthorize_server_administration_guide/paz_using_monitor_history_plugin.html).

### AWS Java SDK upgrade

Info PAZ-18383

We've upgraded to AWS Java SDK v2. This upgrade changes the default behavior for Amazon S3 connections to use virtual-hosted-style URLs, disabling legacy path-style access by default.

If your Amazon S3 deployment package stores require path-style access (for example, `https://s3.amazonaws.com/<bucket-name>`), enable the **Use Path Style Access** option in the PingAuthorize S3 store configuration to maintain connectivity.

Learn more in [Adding an Amazon S3 deployment package store to PingAuthorize](../pingauthorize_server_administration_guide/paz_amazons3_deploy_package.html).

### Enhanced flexibility for policy query requests

Improved PAZ-19611

We've enhanced the `/query` endpoint of the JSON PDP API to support more expressive and open-ended authorization queries:

* You can now include up to two unbound attributes per request for broader discovery scenarios.

* You can now include up to three multivalued attributes per request for complex batch-style evaluations.

* You can now resolve query attributes dynamically using other query attributes. For example, the system can first resolve a list of resources and then, for each resource, resolve the list of actions applicable to it.

Learn more in [Query requests](../pingauthorize_server_administration_guide/paz_json_pdp_api_flow.html#json_pdp_query_requests).

### Improved handling of null values in Redis

Improved PAZ-19569

We've enhanced the Redis attribute cache to handle missing or null values more gracefully, with improved validation and clearer logging to simplify troubleshooting and improve system stability.

### Added more control over response timestamp precision

Improved PAZ-20713

We've added a new Policy Decision Service configuration property, `use-microseconds-timestamp`, which allows you to enforce microsecond-precision timestamps for `governance-engine` API responses. This option improves compatibility with clients that expect legacy timestamp formats.

Learn more in [JSON PDP API response format](../pingauthorize_server_administration_guide/paz_json_pdp_api_flow.html#json_pdp_response).

### Enabled default condition short-circuiting in the Policy Editor

Improved PAZ-18291

Compound conditions in the Policy Editor now short-circuit by default, matching the existing behavior of the PingAuthorize Server. This ensures that policy evaluation stops as soon as a condition is met, improving performance and providing a consistent experience between policy testing and decision runtime.

### Optimized `setup` behavior for modern JVMs

Improved DS-50603

For new installations, `bin/setup` no longer sets the JVM option `ConcGCThreads`, allowing modern JVMs to select the optimal value automatically.

### Improved policy query performance

Improved PAZ-13111

We've improved the performance of policy queries by applying an optimization pass that significantly reduces the size of internal policy structures.

### Added `server.out` files to CSD archives

Improved SUPP-441

To add details about the server state before shutdown, the `collect-support-data` tool now includes up to five of the latest timestamped `server.out` files in the CSD archive.

### Improved expired certificate handling for TLS negotiation

Fixed DS-49269, DS-49270

We've fixed an issue that could cause the server to select an expired certificate when performing TLS negotiation with an external server that has a key manager provider and requests a client certificate chain.

The server now presents an expired certificate only if the key store doesn't include any certificate chains with currently valid certificates.

We've also added the `ssl-cert-nickname` property to the external server configuration, which allows you to control which client certificate chain the server presents to that external server. If this property isn't configured, the server attempts to automatically select an appropriate certificate chain.

### Fixed array handling in SpEL

Fixed PAZ-12964

We've fixed an issue where a SpEL expression returning an array (such as from the `.split()` function) would cause a `PROCESSING_ERROR`. These results are now correctly handled as collections.

### Fixed an issue with deployment package deletion

Fixed PAZ-5577

We've fixed an issue where deployment packages actively deployed to a deployment package store could be deleted. Now, to delete a deployment package, you must first deploy a different package to the relevant store.

### Fixed an issue with policy dependency pagination

Fixed PAZ-18631

We've fixed an issue where the Policy Editor's `/dependencies` endpoint returned extraneous data, leading to incorrect pagination. The endpoint now reports only valid child policies, ensuring consistent and accurate results.

### Fixed an issue with HTTP service timeouts

Fixed PAZ-20345

We've fixed an issue where HTTP Service calls would incorrectly time out after 10 seconds, even when a longer request timeout was configured.

### Fixed a Policy Editor startup issue

Fixed PAZ-19762

We've fixed an issue in the admin point application configuration that could prevent the Policy Editor from starting properly.

### Fixed inconsistent URL decoding

Fixed PAZ-20178

We've fixed an issue where inconsistent URL decoding could allow double-URL-encoded requests to bypass path-based access controls in API security gateway mode.

### Fixed an issue with profile replacement in topologies

Fixed DS-50197

We've fixed an issue where using the `manage-profile` tool to replace a profile would fail if the new profile and original profile each contained topology external servers with identical names.

### Fixed an issue with `--performLocalCleanup` in interactive mode

Fixed DS-48553

Running `remove-defunct-server --performLocalCleanup` in interactive mode no longer attempts to establish a connection to another live server in the topology.

## Previous Releases

For information about enhancements and issues resolved in previous major and minor releases of PingAuthorize, refer to the following:

* [10.3](https://docs.pingidentity.com/pingauthorize/10.3/release_notes/paz_release_notes_legacy_home.html)

* [10.2](https://docs.pingidentity.com/pingauthorize/10.2/release_notes/paz_release_notes_legacy_home.html)

* [10.1](https://docs.pingidentity.com/pingauthorize/10.1/release_notes/paz_release_notes_legacy_home.html)